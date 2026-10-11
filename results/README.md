# Data provenance and artifact identity

`submissions.csv` is an owner-maintained retrospective table, not an untouched
Kaggle API export. The owner confirmed on October 11, 2026 that individual Private
scores were entered manually. No original per-submission export or screenshot is
bundled. Public scores are historical recorded values; the table's individual rows,
notebook versions, family labels, and final-selection flags have not all been
independently verified against Kaggle submission IDs.

## What is independently confirmed

The official [leaderboard](https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/leaderboard)
was inspected on October 11, 2026, using the Public and Private tabs and searching
for Team Sian (member profile `arki13`):

| Tab | Rank | Score |
|---|---:|---:|
| Public | 223 | 93.83500 |
| Private | 3,231 | 0.00000 |

The team row displays 120 entries. That UI count is not equated with this table's
179 rows, which include errors and retrospective records. No verified explanation
for the count difference is claimed. A full final leaderboard snapshot and medal
calculation are not bundled; total-team counts, zero-score team counts, and precise
counterfactual medal ranks are omitted from the current narrative.

## Internal consistency of the supplied CSV

| Status | Rows |
|---|---:|
| Succeeded | 158 |
| Succeeded (after deadline) | 2 |
| Submission Format Error | 18 |
| Kaggle Error | 1 |
| Total | 179 |

Both-score numeric rows: 160. Failed rows have missing scores, not zero scores.
The figures distinguish the two after-deadline rows. Among the 158 `Succeeded`
rows, 140 are labeled EXFILTRATION and five CONFUSED_DEPUTY. All 140 recorded
EXFILTRATION Private values are zero; all five deputy Public/Private pairs are
equal. These are checks of the supplied table, not independent validation of the
manual transcription or mechanism labels.

`final_selected=yes` appears on `v27_adapt` and
`method39_broad_per-model_race`; those flags are retrospective owner records.
Submission order is not a timestamp. A notebook version is not a submission ID.
Family labels summarize intended composition and are not per-model branch evidence.

## Code identity

`scored_artifacts.csv` contains only two historical file hashes, method39 and
method44. Their published Python files match the development project's retained
scored-artifact registry hashes. This independently identifies the archived file
versions; it does not supply an external proof of which code Kaggle evaluated.

`artifact_manifest.json` preserves SHA-256 hashes of the seven source/plan files
before and after publication editing. Only v3_livefill's attribution header changed;
its historical code body is preserved. The three Markdown plans and the method21
standalone implementation match retained development copies, but their exact
uploaded notebook identities are not established by that comparison.

The public registry is deliberately a subset. A no-match result from the helper
cannot certify that another artifact was never scored, and must not be interpreted
as authorization or advice to resubmit anything.

The original development ledger and current-state documents were not changed by
this publication review. No competition submission or model experiment was run.
