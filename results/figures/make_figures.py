"""Regenerate figures from the owner-maintained score table (no Kaggle execution)."""

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIGURE_DIR = Path(__file__).resolve().parent
CSV_PATH = FIGURE_DIR.parent / "submissions.csv"


def load_scores():
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    scored = []
    for row in rows:
        public, private = row["public_score"], row["private_score"]
        if not public and not private:
            continue
        if not public or not private:
            raise ValueError(f"Only one score present at order {row['order']}")
        row = dict(row)
        row["public_score"], row["private_score"] = float(public), float(private)
        row["order"] = int(row["order"])
        if not all(math.isfinite(row[key]) for key in ["public_score", "private_score"]):
            raise ValueError(f"Non-finite score at order {row['order']}")
        scored.append(row)
    if not scored:
        raise ValueError("No numeric score pairs in submissions.csv")
    return sorted(scored, key=lambda row: row["order"])


def main():
    scored = load_scores()
    style = {
        "exfiltration": ("#d64a45", "o", "EXFILTRATION"),
        "confused_deputy": ("#2a78d6", "s", "CONFUSED_DEPUTY"),
        "mixed_hedge": ("#149765", "D", "mixed / hedge"),
        "other": ("#8b8b85", "x", "other / baseline"),
    }
    upper = max(100, max(row["public_score"] for row in scored) * 1.1)
    fig, ax = plt.subplots(figsize=(8.5, 6.4))
    ax.plot([0, upper], [0, upper], "--", lw=1, color="#9a9a93", zorder=1)
    ax.text(upper - 3, upper - 8, "public = private", rotation=38,
            color="#6f6f69", fontsize=8, ha="right")
    for family in ["exfiltration", "other", "mixed_hedge", "confused_deputy"]:
        points = [row for row in scored if
                  (row["family"] if row["family"] in style else "other") == family]
        color, marker, label = style[family]
        kwargs = {} if marker == "x" else {"edgecolors": "white", "linewidths": .5}
        ax.scatter([row["public_score"] for row in points],
                   [row["private_score"] for row in points], s=43,
                   color=color, marker=marker, alpha=.8, zorder=3, label=label, **kwargs)

    final = [row for row in scored if row["final_selected"] == "yes"]
    for row, offset in zip(final, [(-32, 17), (-6, 33)]):
        ax.annotate(f"recorded final pick: {row['public_score']:.3f} → {row['private_score']:g}",
                    (row["public_score"], row["private_score"]),
                    xytext=(row["public_score"] + offset[0], row["private_score"] + offset[1]),
                    ha="right", fontsize=8,
                    arrowprops={"arrowstyle": "-", "lw": .8, "color": "#52514e"})
    best = max(scored, key=lambda row: row["private_score"])
    ax.annotate(f"best recorded Private: {best['private_score']:.3f}",
                (best["public_score"], best["private_score"]),
                xytext=(best["public_score"] + 9, best["private_score"] + 29), fontsize=8,
                arrowprops={"arrowstyle": "-", "lw": .8, "color": "#52514e"})
    ax.set(xlabel="Public score", ylabel="Private score",
           title=f"Public vs. Private: {len(scored)} numeric score pairs",
           xlim=(-3, upper), ylim=(-3, upper))
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(True, lw=.4, color="#e6e6e2", zorder=0)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    fig.text(.5, .015, "Owner-maintained table; individual Private scores entered manually.",
             ha="center", fontsize=8, color="#6f6f69")
    fig.tight_layout(rect=(0, .035, 1, 1))
    fig.savefig(FIGURE_DIR / "public_vs_private.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9.5, 4.5))
    orders = [row["order"] for row in scored]
    ax.plot(orders, [row["public_score"] for row in scored], lw=1.2,
            color="#2a78d6", marker="o", ms=2.5, label="Public")
    ax.scatter(orders, [row["private_score"] for row in scored], s=12,
               color="#d64a45", zorder=3, label="Private")
    late = [row for row in scored if row["status"] == "Succeeded (after deadline)"]
    if late:
        ax.scatter([row["order"] for row in late], [row["public_score"] for row in late],
                   s=70, marker="o", facecolors="none", edgecolors="#c98500", linewidths=1.5,
                   zorder=4, label="marked after deadline")
    ax.scatter([row["order"] for row in final], [row["public_score"] for row in final],
               s=85, marker="*", color="#292929", zorder=4, label="recorded final picks")
    ax.set(xlabel="Submission order (not calendar time)", ylabel="Score",
           title="Recorded scores over submission order", ylim=(-3, upper))
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(True, lw=.4, color="#e6e6e2")
    ax.legend(frameon=False, fontsize=8, loc="upper left", ncol=2)
    fig.text(.5, .015, "Failed rows are omitted; missing scores are not zero scores.",
             ha="center", fontsize=8, color="#6f6f69")
    fig.tight_layout(rect=(0, .04, 1, 1))
    fig.savefig(FIGURE_DIR / "public_timeline.png", dpi=150)
    plt.close(fig)
    print(f"Saved 2 figures from {len(scored)} numeric score pairs in {CSV_PATH.name}.")


if __name__ == "__main__":
    main()
