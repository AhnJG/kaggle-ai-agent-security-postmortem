# How coding agents supported the research

Coding agents assisted with implementation, plans, reviews, and competitor-material
analysis; I directed the work and made submission decisions. Public notebooks and
discussions provided substantial starting ideas and code, credited in [NOTICE](../NOTICE).
The contribution was adaptation, integration, experiments, and evidence review.
The available log does not justify a precise percentage of AI-written code or a
fixed author/reviewer role for each model across the entire project.

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
