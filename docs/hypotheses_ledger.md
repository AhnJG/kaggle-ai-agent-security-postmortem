# Retrospective hypothesis ledger

This is a retrospective synthesis, not a new preregistration. The full
[historical log](experiment_log_ko.md) includes changing assumptions, failed tests,
and corrections. Public and Private scores below are from the
[curated submission table](../results/submissions.csv); individual Private values
were entered manually after the contest. [Data provenance](../results/README.md).

Verdicts apply to the tested implementation and evidence layer:
`supported / falsified / degenerate / inconclusive`.

| Hypothesis or claim | Verdict | Evidence and boundary |
|---|---|---|
| The tested single-post EXFILTRATION entries retain points on Private. | **falsified in the recorded evaluations** | All 140 successful rows labeled EXFILTRATION have Private 0. This does not identify the hidden guardrail's mechanism. |
| The tested CONFUSED_DEPUTY entries retain points on Private. | **supported retrospectively** | Five labeled rows have equal Public and Private values; the best is `v11_deputy_transfer`, 14.605. This equality was not observable in July and is not a universal transfer guarantee. |
| More posts per candidate improve Public score. | **falsified for the tested variants** | The v26 k4/k8/k16/k32 entries score 80.190 / 73.615 / 51.765 / 38.870; method44 k4 scores 73.245 and method46 k8 64.230. These are historical comparisons, not a matched causal test against method39. |
| A per-model family race causes a higher Public score. | **inconclusive causally** | method39 records the maximum, 93.835. A best observed score alone does not isolate the effect of routing or quantify a noise band. |
| A Gemma-native format improves the tested entry. | **falsified against the intended historical target** | method28: 69.120; method38: 81.925. Aggregate scores do not show which model or phase caused the difference. |
| Decode-min alone establishes a new Public advantage. | **inconclusive** | method37: 90.045. No matched replicated estimate or isolated decode measurement is bundled. |
| Only the first 200–250 candidates are scored, so front ordering improves results. | **inconclusive** | This began as a community observation. method30: 76.680; method41: 88.560. Neither verifies that replay rule. |
| The tested fixed/routed multi-message entries beat the banked Public best. | **falsified for that batch** | method64/71/73/76/77: 80.280 / 80.250 / 84.300 / 78.045 / 73.085; all below historical method39 93.835. This does not reject every multi-message strategy. |
| The tested untrusted chain yields a Public advantage. | **falsified for the submitted implementation** | `untrusted_combo`: 0.000. Neither that score nor a local rule check rules out every possible chain. |
| The method83 synonym prompt bypasses the local guardrail. | **falsified in the recorded local probe** | The log records 0% for the tested local configuration and withdrawal of the family. The runtime setup and result JSON are not bundled; this is not hosted Private evidence. |
| A latency classifier routes the models reliably. | **inconclusive from this table** | method61, explicitly labeled latency gate, scores 66.290. The old ledger incorrectly used method25, which is labeled a JSON-args entry; routing diagnosis needs branch traces. |
| Public score alone is adequate for final selection. | **contradicted by this entry's recorded outcomes** | Two selected exfiltration rows have Private 0, while unselected rows retain points. Hidden-defense risk had already been discussed during the contest. |

The final method88–92 rows add retrospective submission information absent from
some frozen development notes. Two are marked as scored after the deadline and
three as format errors. They do not retrospectively upgrade the artifact-only
checks in those notes into runtime validation or pre-deadline final selections.
