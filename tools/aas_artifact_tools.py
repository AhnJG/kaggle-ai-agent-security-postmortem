#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY_PATH = REPO_ROOT / "results/scored_artifacts.csv"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="AAS helper tools for hashing, scored-registry checks, and result-json summaries."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    sha_parser = subparsers.add_parser("sha256", help="Compute sha256 for a file.")
    sha_parser.add_argument("path", help="Target file path.")
    sha_parser.add_argument("--short", type=int, default=12, help="Short hash prefix length.")
    sha_parser.add_argument("--json", action="store_true", help="Emit JSON.")

    reg_parser = subparsers.add_parser(
        "registry-check",
        help="Check whether a file or hash matches the scored registry.",
    )
    reg_parser.add_argument("--file", help="Candidate file path.")
    reg_parser.add_argument("--sha256", help="Full or prefixed sha256 to query.")
    reg_parser.add_argument("--code", help="Optional code label override.")
    reg_parser.add_argument(
        "--registry",
        default=str(DEFAULT_REGISTRY_PATH),
        help="Registry CSV path.",
    )
    reg_parser.add_argument("--short", type=int, default=12, help="Short hash prefix length.")
    reg_parser.add_argument("--json", action="store_true", help="Emit JSON.")

    sum_parser = subparsers.add_parser(
        "json-summary",
        help="Summarize a local validation result JSON.",
    )
    sum_parser.add_argument("path", help="Result JSON path.")
    sum_parser.add_argument("--limit", type=int, default=12, help="Max rows per summary table.")
    sum_parser.add_argument("--json", action="store_true", help="Emit JSON.")

    return parser.parse_args()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_relative(path: Path) -> str | None:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return None


def file_payload(path_str: str, short: int) -> dict[str, Any]:
    path = Path(path_str).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    digest = file_sha256(path)
    return {
        "path": str(path),
        "repo_relative_path": repo_relative(path),
        "code": path.stem,
        "size_bytes": path.stat().st_size,
        "sha256": digest,
        "sha256_short": digest[:short],
    }


def load_registry(path_str: str) -> list[dict[str, str]]:
    path = Path(path_str).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Registry not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def normalize_sha_prefix(sha_value: str, short: int) -> str:
    normalized = sha_value.strip().lower()
    if not 12 <= short <= 64:
        raise ValueError("registry hash prefixes must contain 12 to 64 characters")
    if any(char not in "0123456789abcdef" for char in normalized) or len(normalized) > 64:
        raise ValueError("sha256 must contain hexadecimal characters only, at most 64")
    if len(normalized) < short:
        raise ValueError(f"sha256 must have at least {short} hex chars, got {len(normalized)}")
    return normalized[:short]


def select_existing(record: dict[str, Any], keys: list[str]) -> dict[str, Any]:
    return {key: record[key] for key in keys if key in record and record[key] not in (None, "", [])}


def render_table(records: list[dict[str, Any]], keys: list[str]) -> str:
    if not records:
        return "(none)"
    normalized_rows: list[list[str]] = []
    widths = [len(key) for key in keys]
    for record in records:
        row = []
        for idx, key in enumerate(keys):
            value = record.get(key, "")
            if isinstance(value, float):
                cell = f"{value:.6f}".rstrip("0").rstrip(".")
            elif isinstance(value, list):
                cell = ",".join(str(item) for item in value)
            else:
                cell = str(value)
            widths[idx] = max(widths[idx], len(cell))
            row.append(cell)
        normalized_rows.append(row)

    lines = []
    lines.append(" | ".join(key.ljust(widths[idx]) for idx, key in enumerate(keys)))
    lines.append("-+-".join("-" * width for width in widths))
    for row in normalized_rows:
        lines.append(" | ".join(cell.ljust(widths[idx]) for idx, cell in enumerate(row)))
    return "\n".join(lines)


def summarize_aggregate(aggregate: dict[str, Any]) -> dict[str, Any]:
    summary = select_existing(
        aggregate,
        ["verdict", "reason", "recommended_plan", "caveat", "supported_plans", "thresholds"],
    )
    for key, value in aggregate.items():
        if key in summary:
            continue
        if isinstance(value, (str, int, float, bool)):
            summary[key] = value
    return summary


def collect_resolved_harnesses(value: Any, bucket: set[str]) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key == "resolved_harness" and isinstance(nested, str):
                bucket.add(nested)
            else:
                collect_resolved_harnesses(nested, bucket)
        return
    if isinstance(value, list):
        for nested in value:
            collect_resolved_harnesses(nested, bucket)


def flatten_nested_plans(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    flattened: list[dict[str, Any]] = []
    for row in rows:
        plans = row.get("plans")
        if not isinstance(plans, list):
            continue
        model = row.get("model")
        resolved_harness = row.get("resolved_harness")
        for plan in plans:
            if not isinstance(plan, dict):
                continue
            flattened.append(
                {
                    "model": model,
                    "resolved_harness": resolved_harness,
                    **plan,
                }
            )
    return flattened


def compact_records(records: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    return records[:limit]


def summarize_json(path_str: str, limit: int) -> dict[str, Any]:
    path = Path(path_str).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"JSON not found: {path}")
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)

    aggregate = data.get("aggregate", {})
    rows = data.get("rows", [])
    cells = data.get("cells", [])
    plans = data.get("plans", [])

    resolved_harnesses: set[str] = set()
    collect_resolved_harnesses(data, resolved_harnesses)

    summary: dict[str, Any] = {
        "file": str(path),
        "probe_kind": data.get("probe_kind"),
        "date": data.get("date"),
        "harness_request": data.get("harness_request"),
        "full_hops": data.get("full_hops"),
        "resolved_harnesses": sorted(resolved_harnesses),
        "counts": {
            "rows": len(rows) if isinstance(rows, list) else 0,
            "cells": len(cells) if isinstance(cells, list) else 0,
            "plans": len(plans) if isinstance(plans, list) else 0,
            "aggregate_rows": len(aggregate.get("rows", []))
            if isinstance(aggregate, dict) and isinstance(aggregate.get("rows"), list)
            else 0,
        },
        "aggregate": summarize_aggregate(aggregate) if isinstance(aggregate, dict) else {},
        "tables": {},
    }

    aggregate_rows = aggregate.get("rows", []) if isinstance(aggregate, dict) else []
    if isinstance(aggregate_rows, list) and aggregate_rows:
        aggregate_keys = [
            "plan_name",
            "model",
            "mean_ok_marker_http_post",
            "mean_posts",
            "hit_target_rate",
            "mean_latency_s",
            "mean_raw_per_s",
            "raw_per_s_ratio_vs_single",
            "n_error_measured",
        ]
        summary["tables"]["aggregate_rows"] = compact_records(
            [select_existing(row, aggregate_keys) for row in aggregate_rows if isinstance(row, dict)],
            limit,
        )

    nested_plan_rows = flatten_nested_plans(rows) if isinstance(rows, list) else []
    if nested_plan_rows:
        nested_keys = [
            "model",
            "resolved_harness",
            "plan",
            "target_posts",
            "mean_posts",
            "hit_target_rate",
            "mean_interact_s",
            "no_tool_rate",
        ]
        summary["tables"]["nested_plan_rows"] = compact_records(
            [select_existing(row, nested_keys) for row in nested_plan_rows],
            limit,
        )

    if isinstance(cells, list) and cells:
        cell_keys = [
            "model",
            "plan_name",
            "target_posts",
            "n_ok_measured",
            "n_error_measured",
            "mean_ok_marker_http_post",
            "hit_target_rate",
            "mean_latency_s",
            "mean_raw_per_s",
        ]
        summary["tables"]["cells"] = compact_records(
            [select_existing(cell, cell_keys) for cell in cells if isinstance(cell, dict)],
            limit,
        )

    if isinstance(plans, list) and plans:
        plan_keys = ["name", "plan", "kind", "target_posts"]
        summary["tables"]["plans"] = compact_records(
            [select_existing(plan, plan_keys) for plan in plans if isinstance(plan, dict)],
            limit,
        )

    return summary


def print_sha256(payload: dict[str, Any]) -> None:
    print(f"path: {payload['path']}")
    print(f"repo_relative_path: {payload['repo_relative_path']}")
    print(f"code: {payload['code']}")
    print(f"size_bytes: {payload['size_bytes']}")
    print(f"sha256: {payload['sha256']}")
    print(f"sha256_short: {payload['sha256_short']}")


def print_registry_summary(payload: dict[str, Any]) -> None:
    print(f"verdict: {payload['verdict']}")
    if payload.get("candidate"):
        candidate = payload["candidate"]
        print(f"candidate_code: {candidate.get('code')}")
        print(f"candidate_path: {candidate.get('path')}")
        print(f"candidate_sha256_short: {candidate.get('sha256_short')}")
    print(f"exact_matches: {len(payload['exact_matches'])}")
    print(f"code_matches: {len(payload['code_matches'])}")
    print(f"path_matches: {len(payload['path_matches'])}")
    if payload.get("message"):
        print(f"message: {payload['message']}")
    for label in ["exact_matches", "code_matches", "path_matches"]:
        matches = payload[label]
        if matches:
            print("")
            print(f"{label}:")
            print(
                render_table(
                    matches,
                    ["date", "code", "score", "sha256_12", "status", "path"],
                )
            )


def print_json_summary(summary: dict[str, Any]) -> None:
    print(f"file: {summary['file']}")
    print(f"probe_kind: {summary.get('probe_kind')}")
    print(f"date: {summary.get('date')}")
    print(f"harness_request: {summary.get('harness_request')}")
    print(f"full_hops: {summary.get('full_hops')}")
    print(f"resolved_harnesses: {','.join(summary.get('resolved_harnesses', [])) or '(none)'}")
    counts = summary.get("counts", {})
    print(
        "counts: "
        f"rows={counts.get('rows', 0)}, "
        f"cells={counts.get('cells', 0)}, "
        f"plans={counts.get('plans', 0)}, "
        f"aggregate_rows={counts.get('aggregate_rows', 0)}"
    )
    aggregate = summary.get("aggregate", {})
    if aggregate:
        print("")
        print("aggregate:")
        for key, value in aggregate.items():
            if isinstance(value, dict):
                print(f"- {key}: {json.dumps(value, ensure_ascii=False, sort_keys=True)}")
            elif isinstance(value, list):
                print(f"- {key}: {', '.join(str(item) for item in value)}")
            else:
                print(f"- {key}: {value}")

    tables = summary.get("tables", {})
    for label in ["aggregate_rows", "nested_plan_rows", "cells", "plans"]:
        rows = tables.get(label)
        if not rows:
            continue
        keys = list(rows[0].keys())
        print("")
        print(f"{label}:")
        print(render_table(rows, keys))


def command_sha256(args: argparse.Namespace) -> int:
    payload = file_payload(args.path, args.short)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_sha256(payload)
    return 0


def command_registry_check(args: argparse.Namespace) -> int:
    if not args.file and not args.sha256:
        raise ValueError("registry-check requires --file or --sha256")

    candidate: dict[str, Any] = {}
    if args.file:
        candidate = file_payload(args.file, args.short)

    sha_prefix = normalize_sha_prefix(args.sha256 or candidate["sha256"], args.short)
    query_code = args.code or candidate.get("code")
    query_path = candidate.get("repo_relative_path")
    registry_rows = load_registry(args.registry)

    exact_matches = []
    for row in registry_rows:
        stored_hash = (row.get("sha256") or row.get("sha256_12", "")).lower()
        compared_length = min(len(stored_hash), len(sha_prefix))
        if compared_length >= 12 and stored_hash[:compared_length] == sha_prefix[:compared_length]:
            exact_matches.append(row)
    code_matches = [row for row in registry_rows if query_code and row.get("code") == query_code]
    path_matches = [row for row in registry_rows if query_path and row.get("path") == query_path]

    if exact_matches:
        verdict = "EXACT_RESUBMIT_BLOCKED"
        message = "Exact scored artifact already exists in the registry."
    elif code_matches or path_matches:
        verdict = "NEW_HASH_NAME_COLLISION_WARNING"
        message = "Hash is new, but code or path already appears in the scored registry."
    else:
        verdict = "SAFE_NEW_HASH"
        message = "No exact match in the supplied registry. The bundled registry is a subset, not resubmission clearance."

    payload = {
        "verdict": verdict,
        "message": message,
        "candidate": {
            "code": query_code,
            "path": query_path or candidate.get("path"),
            "sha256_short": sha_prefix,
        },
        "exact_matches": exact_matches,
        "code_matches": code_matches,
        "path_matches": path_matches,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_registry_summary(payload)
    return 0


def command_json_summary(args: argparse.Namespace) -> int:
    summary = summarize_json(args.path, args.limit)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print_json_summary(summary)
    return 0


def main() -> int:
    args = parse_args()
    try:
        if args.command == "sha256":
            return command_sha256(args)
        if args.command == "registry-check":
            return command_registry_check(args)
        if args.command == "json-summary":
            return command_json_summary(args)
        raise ValueError(f"Unknown command: {args.command}")
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
