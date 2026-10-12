# Function and configuration reference

Read [the walk-through](code_walkthrough.md) first for the reasons behind the four
policies. This reference points to the preserved implementations. It documents
behavior; it does not provide a standalone SDK setup or change the historical code.

## v3_livefill

Source: [v3_livefill.py](../src/attacks/v3_livefill.py).

| Function | Input / output and responsibility | Why it is there |
|---|---|---|
| `_alpha2(i)` | Converts `i % 676` to a two-letter label | Short, deterministic text |
| `_label(i)` | Adds the quotient suffix beyond the first 676 labels | Prevent repeats caused by the modulo alone |
| `_url(i)` | Builds a destination string | Vary a candidate field consistently |
| `_msg(i)` | Formats a message containing the indexed destination and marker | Separate text construction from testing |
| `_fired(env)` | Returns a boolean from the exported tool-event trace; unavailable/non-dictionary trace returns `False` | Keep messages with the desired observed tool event |
| `AttackAlgorithm.run(env, config)` | Handles absent environment and configuration, then calls `_fill()` | SDK entry point |
| `AttackAlgorithm._fill(env, budget, hops)` | Warms up, estimates room, tries messages, and returns accepted candidates | Balance trial filtering, wall time, and estimated replay cost |

| Constant | Value | Actual role |
|---|---:|---|
| `HARD_N_CAP` | 2000 | Maximum accepted candidate count |
| `FILL_BUDGET_FRAC` | 0.95 | Wall deadline measured from the run start |
| `REPLAY_SAFE_FRAC` | 0.97 | Estimated replay allowance before subtracting warm-up elapsed time |
| `SLOWEST0` | 25 seconds | Initial lower bound for the retained maximum trial-cost estimate |
| `SLOWEST_MULT` | 1.35 | Multiplies that estimate for the next-trial reserve |
| `LAT_FLOOR_S` | 0.001 seconds | Lower bound in the trial-cost update; it cannot reduce the 25-second initializer |

The measured trial interval includes reset, interaction, and `_fired()` processing.
Rejected trials use wall time but do not add to accepted `replay_cost`. These are
construction-time measurements, not observations of later hosted replay.

## method21 and method39

Sources: [method21](../src/attacks/method21_family_race.py) and
[method39](../src/attacks/method39_broad_permodel_race.py). For method39, the functions
below live inside the `attack_code` string; the outer file writes that string to disk.

| Function / field | Responsibility | Important boundary |
|---|---|---|
| `_alpha2()`, `_label()`, `_url()` | Build indexed destination strings | Text diversity is not proof of scored-cell novelty |
| `_msg(style, i)` | Select a text template by style and substitute the indexed destination | It builds text; Python is not executing the named tool |
| `_count_marker_posts(env)` | Count successful `http.post` events containing the marker; unavailable/non-dictionary trace returns 0 | Event count is not a predicate score |
| `_probe_once(env, message, probe_hops)` | Reset, interact, and return `(matching_event_count, elapsed)` | Elapsed includes reset and interact, but excludes trace export/counting |
| `AttackAlgorithm.run(env, config)` | Warm up, sample styles, rank them, and return one-style candidate batch | The final batch is not tested item by item |
| `fires` | Add one when an attempt has at least one matching event | Multiple events in an attempt still contribute only one fire |
| `stats` | Keep fires, attempts, and summed measured elapsed time by style | A deadline can leave styles partially sampled or absent |
| `chosen` | Start at `DEFAULT_STYLE`; replace it only when the best measured style has a fire | A no-hit race keeps the default |

| Constant / choice | method21 | method39 |
|---|---|---|
| `DEFAULT_STYLE` | `apreimp` | `apreimp` |
| `STYLES` | `apreimp`, `direct_call`, `urltail_harmony`, `json_plain` | `apreimp`, `apreimp_terse`, `apreimp_min`, `apreimp_tool`, `raw_schema_bare` |
| `PROBE_HOPS` | 1 | 2 |
| `WIDE_REPS` | 16 per style | 8 per style |
| `PROBE_BUDGET_FRAC` | 0.18 | 0.18 |
| `BLIND_N` | 2000 | 2000 |
| `FALLBACK_N` | 32 when `env is None` | 32 when `env is None` |

Both use a default 9,000-second budget if the configured value is absent or falsey.
The supplied hop configuration is clamped to 1–8, then further limited by
`PROBE_HOPS`. These caps govern generation-time probes; they do not measure the
hosted replay's actual hop use.
An exception in warm-up returns 2,000 default candidates; an exception in a style
trial is instead recorded as zero posts and 0.001 seconds.

The `[RANK]` diagnostic prints `hit_rate / average_elapsed / throughput / attempts`
for each measured style. The final diagnostic includes `chosen`, the returned
count, probe hops, and measured-style count. A printed style count does not imply
every style received all requested trials. Hosted submission UI availability of
these diagnostics is not established by the source.

### What the style labels refer to

These describe the current `_msg()` branches, not independently verified advantages.

| Label | Text-construction choice |
|---|---|
| `apreimp` (both files) | Imperative request followed by an analysis-channel delimiter string |
| `direct_call` (method21) | Tool-call-like expression |
| `urltail_harmony` (method21) | Destination presented later in the instruction, with the delimiter suffix |
| `json_plain` (method21) | Instruction containing JSON-shaped tool arguments; the whole message is not just JSON |
| `apreimp_terse` (method39) | Baseline-like request with an explicitly brief final reply |
| `apreimp_min` (method39) | Shorter request wording, a stop instruction, and a brief final reply |
| `apreimp_tool` (method39) | Explicit tool name and argument names in the instruction |
| `raw_schema_bare` (method39) | Requests a raw tool-call serialization and no surrounding prose |

The delimiter text and raw-format request are message content. The source does
not establish how every hosted formatter interprets them or their isolated score
effect. No style is selected by a hard-coded model-identity branch.

## method44

Source: [method44_static_list_continue_k4.py](../src/attacks/method44_static_list_continue_k4.py).
The implementation is inside `attack_code`, followed by a file-writing wrapper.

| Function / constant | Responsibility | Why it is there |
|---|---|---|
| `_alpha2()`, `_label()`, `_url()` | Shared indexed-label construction | Deterministic candidate fields |
| `_urls(start_idx, n)` | Build `n` consecutive destination strings | Construct a group of requested actions |
| `_list_continue_msg(base_idx, target_posts)` | Put the destination list and a continuation request into one message | Request multiple sequential actions in later model replay |
| `AttackAlgorithm.run(env, config)` | Ignore both inputs and build the fixed candidate batch | Remove the chooser and generation-time trials |
| `URL_STRIDE = 16` | Start group `i` at index `i * 16` | Keep four-index groups apart between candidates |
| `BLIND_N = 2000` | Number of candidate objects constructed | Fixed batch size, not guaranteed findings |

There are 2,000 one-message candidates, each containing four intended destinations.
There are no construction-time `env.interact()` calls or per-candidate acceptance
checks in this file.

## Supporting diagnostics and artifact tools

These helpers answer different questions from the submission policies. The probe
setup, fixtures, model weights, and recorded result JSON files are not fully bundled;
see [probe limitations](../probes/README.md). They were inspected for this guide,
not executed with models.

| File | What it does | What its output cannot establish |
|---|---|---|
| [local_gateway_probe.py](../probes/local_gateway_probe.py) | Writes a diagnostic implementation configured for 600 candidates, locates runtime inputs, and starts the local gateway or competition rerun server branch | Findings are not a count of every replay attempt; fewer findings do not isolate JSON-format failure or a particular bottleneck |
| [aas_step4_decode_floor_throughput_probe.py](../probes/aas_step4_decode_floor_throughput_probe.py) | Compares single-action message styles through `_replay_one()`; summarizes elapsed time, events, generations, and a score proxy | `implied_N` and `implied_row_score` are conditional proxy calculations, not hosted predictions or proof of a decode floor |
| [aas_step4_throughput_structure_fixedcost_probe.py](../probes/aas_step4_throughput_structure_fixedcost_probe.py) | Compares single/multiple-action plans and fits `_ols()` to total elapsed time versus assistant-generation count | Fitted intercept `F` and slope `L` are not isolated measurements of prefill, decoding, or transferable speedup |
| [aas_step4_fixed_cost_decompose_probe.py](../probes/aas_step4_fixed_cost_decompose_probe.py) | `_timed_candidate()` separates reset and interact time; `_fit_prefill_decode()` regresses interact time against matching post count | Fields called `prefill_s` and `decode_s` are fitted coefficients, not directly instrumented model-stage timings |
| [aas_artifact_tools.py](../tools/aas_artifact_tools.py) | Computes file hashes, queries a registry, and summarizes existing JSON | A registry no-match is not evidence that an artifact was never scored; the bundled registry has only two entries |

The H1/H2 replay helpers calculate `raw = 16 * matching_posts + (2 if any else 0)`.
That is a convenient diagnostic proxy, **not** the SDK's full predicate sum and
global scored-cell novelty accounting. A field named `fired_exfil` is checked
separately from that proxy. The current [scoring explanation](scoring_mechanics.md)
gives the actual retained SDK formula and its limits.

For the hash tool, `file_sha256()` identifies exact bytes; `repo_relative()` and
`DEFAULT_REGISTRY_PATH` keep the lookup within this archive; `normalize_sha_prefix()`
checks a 12–64-character hexadecimal query prefix. `command_registry_check()`
distinguishes a hash-prefix match from a name/path collision, and
`summarize_json()` presents stored fields without running or re-evaluating a model.
A prefix match is less specific than comparing all 64 hash characters.

## Read the historical comments with the current interpretation

The source retains original comments about “100% firing,” specific model behavior,
front-scoring limits, prefill, and expected score effects. Treat these as historical
beliefs or hypotheses where they exceed direct code behavior. This guide preserves
the code bytes while distinguishing intention, observed traces, and hosted outcomes.
For results and corrections, use [the post-mortem](postmortem.md),
[hypothesis ledger](hypotheses_ledger.md), and [data provenance](../results/README.md).
