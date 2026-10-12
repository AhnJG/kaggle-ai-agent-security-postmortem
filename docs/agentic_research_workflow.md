# How coding agents supported the research

This entry combined public starting material, owner-directed experiments, and
coding-agent assistance. Its engineering contribution was adaptation, integration,
variant comparisons, diagnostics, and evidence review.

## Contributions and decision ownership

| Contributor or source | Documented contribution | Responsibility or scope |
|---|---|---|
| Project owner (Team Sian) | Directed the research, selected experiment changes, and reviewed results with coding-agent support | Made final submission decisions, including the selections discussed in the [post-mortem](postmortem.md) |
| Claude / Codex | Assisted with implementation, diagnostic code, submission plans, reviews, and public-material analysis | Supported the work; the retained record does not identify the author of every code block or establish causal score gains from an agent |
| Public notebooks and discussions | Supplied substantial starting ideas, code, and runtime references | Upstream authors and license scope are recorded in [NOTICE](../NOTICE); adaptation is distinguished from independent invention |

### The recorded Claude/Codex task division

Later operating rules assigned the following primary tasks:

| Tool | Assigned tasks |
|---|---|
| Claude | New code, submission batch cards, compilation checks, hashes, and path organization |
| Codex | Evidence-boundary audits, result interpretation, document-conflict checks, and stale/degenerate judgments |

This is a documented task assignment, not proof that the same division held for
every earlier experiment or that every assigned check was completed. The
[historical log](experiment_log_ko.md) contains changing plans, interpretations,
and corrections. It does not support a precise percentage of AI-written code,
fixed authorship by tool, or a claim that agent review made all measurements valid.

The source is the development archive's `codex/ACTIVE/README_CURRENT.md`, section
`Claude/Codex 역할 분리`, inspected on October 12, 2026. That control file is not
bundled here; the following short excerpt preserves the role-assignment evidence.
It is historical documentation, not an instruction to execute work:

```text
Claude
  새 코드 작성
  제출 배치 카드 작성
  compile / hash / 경로 정리
Codex
  증거 경계 감사
  결과 해석
  문서 충돌 점검
  stale / degenerate 판정
```

The [AI-assistance reflection (Korean)](ai_assistance_reflection_ko.md) documents
38 review items spanning measurement, interpretation, delivery, and state management.
Each item separates recorded outcomes from causal assumptions and distinguishes
explicit AI-output mistakes from errors whose authorship or cause is uncertain.
The owner retains responsibility for experiment and final-selection decisions.

## The workflow as it developed

Later in the project, operating rules formalized candidate identity and decision
criteria before probes or submissions:

```text
path, sha256, purpose, hypothesis, one_changed_factor,
success, failure, next_action, same_window_comparison,
historical_reference, forbidden_interpretation
```

The historical record is uneven. These later rules do not prove that every earlier
experiment had a complete preregistration or independent comparison. Some final
score-max batches used a historical benchmark rather than a same-window control.

The rules distinguished three evidence layers:

| Layer | Supported use | Limit |
|---|---|---|
| `local_gguf` | syntax, branches, rough local behavior | does not establish hosted performance |
| `cm391` board-like proxy | candidate compression in the proxy | can disagree with Kaggle |
| Kaggle Public score | observed score in that evaluation | does not isolate cause or establish Private rank |

Only the Private leaderboard determines final standing. During the contest its
scores were hidden, so diversification was a decision under uncertainty, not a
measured Private-performance optimization.

A hash registry guarded against repeating exact scored artifacts. The public
repository bundles a **two-file subset** of that historical registry, covering
method39 and method44. The helper can inspect those hashes; a no-match result is
not clearance to submit an artifact again.

```bash
python tools/aas_artifact_tools.py sha256 src/attacks/method39_broad_permodel_race.py
python tools/aas_artifact_tools.py registry-check --file src/attacks/method39_broad_permodel_race.py
```

## What the record can support

The [Korean log](experiment_log_ko.md) preserves plans, results, and changing
interpretations. Some probes helped reject implementation-specific ideas without
using competition submissions. The public archive includes selected scripts, not
all setup helpers or result JSON files, so those runs are not fully reproducible
from this repository.

The process also made measurement mistakes. A September 2 correction withdrew
claims based on incorrectly defined `timeout_free_n` and `unique_cells` metrics.
Other analyses inferred a replay count or prefill bottleneck too confidently from
aggregate scores and timing. Preserving corrections is part of the useful record;
it is not evidence that every original conclusion was sound.

## The selection failure

The log discussed Private-defense uncertainty and explored hedges before the end.
Nevertheless, the curated table marks two high-Public exfiltration entries as the
final selections, both with Private 0. The missed step was carrying the already
recognized uncertainty into selection, rather than merely documenting it.

A future decision record should ask what evidence supports transfer, what remains
unknown, and which alternatives cover different failure mechanisms. “Unknown”
should remain a real answer; a neat template cannot make a hidden outcome known.

## Contribution-writing references

The following first-party project write-ups were consulted on October 12, 2026
for how to describe contributions. Their workflows and results are the respective
authors' reports; they are not evidence of what happened in this project.

| Reference | How it describes contributions | Applied here |
|---|---|---|
| [CSIRO Image2Biomass agentic solution](https://github.com/Chihiro-n/csiro-biomass-agentic-solution#experiment-workflow) | Names the coding agents, discloses implementation assistance, and describes the human-facing experiment and submission workflow | Name the tools and supported tasks, with decision ownership stated separately; do not borrow its claim about the amount of AI-written implementation |
| [Kaggriculture solution — Team contributions](https://github.com/msdsm/kaggriculture-solution#team-contributions) | Uses a contributor-to-work table with concrete model, planner, and analysis tasks; source notes appear separately | Use specific activities in a compact table and keep upstream source credit visible |
| [ROGII Public-LB post-mortem](https://github.com/ElMatiOfficial/kaggle-solutions/blob/main/writeups/20-rogii-wellbore-geology.md) | Separates the inherited public solution from the authors' own measurements and analysis | Distinguish public starting code, adaptation, and this entry's experiment record |
