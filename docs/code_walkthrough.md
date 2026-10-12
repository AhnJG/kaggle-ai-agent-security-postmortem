# How the four representative submissions work

This guide is for a reader who knows Python but has not used the competition SDK.
It explains each policy's purpose, actual control flow, and interpretation limits.
The [function reference](code_reference.md) maps the explanation back to the source.

The four files are historical artifacts, not four proven improvements. Public
notebooks and discussions provided substantial starting code and ideas; Team Sian's
work adapted, integrated, and compared them. See [NOTICE](../NOTICE).

## First separate candidate construction from evaluation

The Python code constructs messages for a tool-using model. `http.post` appears in
candidate text and trace checks; these files do not call a Python HTTP client to
perform that requested action. The benchmark supplies the model, fixture-backed
tools, guardrail, and scoring process. `SECRET_MARKER` is a synthetic benchmark
marker, not a secret read from this repository or the reader's computer.

| Name in the code | Role |
|---|---|
| `AttackAlgorithm.run(env, config)` | Entry point that returns a list of candidate objects |
| `AttackCandidate.from_messages((msg,))` | Packages one message as a candidate; it does not execute or score it |
| `env.reset()` | Requests a fresh interaction state before a generation-time trial |
| `env.interact(msg, max_tool_hops=...)` | Tries the message in the supplied environment |
| `env.export_trace_dict()` | Provides events that these files inspect for their local success signal |
| Replay / evaluation | Separately runs returned candidates and applies predicates and scored-cell accounting |

```mermaid
flowchart LR
    subgraph Generation["Candidate construction"]
        Run["run: choose a policy"] --> List["Return candidate messages"]
        Run --> Probe["Optional env.interact trials"]
        Probe --> Signal["Inspect traces and timing"]
        Signal --> List
    end
    subgraph Evaluation["Separate replay and scoring"]
        Replay["Re-execute candidate messages"] --> Trace["Model, tools, and guardrail"]
        Trace --> Score["Predicates and scored cells"]
    end
    List --> Replay
```

A successful generation-time trial is a useful observation in that environment.
It does not lock in the next model response, the replay time, the scored-cell hash,
or the hidden Private outcome. This distinction explains why the code can return
2,000 candidates without having verified 2,000 successful scored findings.

### Why a tool event can appear without proving a full scoring outcome

Three decisions are involved: the model produces a tool request, the environment
and guardrail allow or reject it, and scoring evaluates predicates and scored-cell
novelty. The `_fired()` / `_count_marker_posts()` checks observe a narrow part of
that process: a successful marker-post event in the supplied trace.

The retained public SDK's target extractor reads the first present field among
`path`, `url`, `cmd`, `data`, `body`, and `content`. A request containing both `url`
and `data` therefore supplies `url` to that extractor. This is an inspectable
public-SDK behavior relevant to these candidates. It does not show that every
argument was inspected, that all such calls succeed, or what the hidden Private
defense does. See the [guardrail and scoring explanation](scoring_mechanics.md#public-guardrail-and-hidden-outcomes).

## Why these policies were needed

The project had to balance three practical questions: which message form the
supplied model follows, how much trial time to spend before returning candidates,
and whether more requested actions justify their extra runtime and failure risk.
The four policies make different choices:

| File | Question it addresses | What `run()` returns |
|---|---|---|
| [v3_livefill](../src/attacks/v3_livefill.py) | Can I keep candidates that show the desired behavior while staying within estimated time limits? | Up to 2,000 candidates with a positive generation-time trace check |
| [method21](../src/attacks/method21_family_race.py) | Which of four message families has the best observed successful-attempt rate per second? | Normally 2,000 untested messages of one selected family |
| [method39](../src/attacks/method39_broad_permodel_race.py) | Which of five format variants works best in the current environment? | Normally 2,000 untested messages of one selected variant |
| [method44](../src/attacks/method44_static_list_continue_k4.py) | What happens when the chooser is removed and each message requests a fixed four-action sequence? | 2,000 untested one-message candidates with four intended actions each |

The retained SDK snapshot caps replay at 2,000 candidates, which provides context
for these batch sizes. That source observation does not establish how many
candidates were actually replayed in any particular hosted run. See
[scoring mechanics](scoring_mechanics.md).

## v3_livefill: try each candidate before keeping it

The motivating problem was wasted candidates: a generated message might not lead
to the desired tool event. This adaptation tests each message immediately and
keeps it only when `_fired()` finds a matching event. It also tries to reserve time
for later replay rather than filling to a fixed count regardless of cost.

The control flow in `run()` and `_fill()` is:

1. If there is no environment, return an empty list. Otherwise read the time budget
   and clamp the generation-time tool-hop limit to 1–8.
2. Record the run start and make one warm-up interaction. The warm-up is not returned
   as a candidate. If it raises an exception, return an empty list.
3. Set a wall-clock deadline at 95% of the supplied budget. Set an estimated replay
   cost allowance at 97% of that budget, minus the time already spent warming up.
4. Before another trial, check whether the predicted next trial would cross either
   allowance. If so, return what has been collected.
5. Reset the environment, try a new message, and inspect the trace. A positive
   `_fired()` check adds a candidate and its measured trial cost. A negative check
   skips that candidate. An interaction exception ends the loop with the candidates
   already collected.
6. Stop at 2,000 accepted candidates even if time remains.

```mermaid
flowchart TD
    Warm["Warm up; account for its elapsed time"] --> Check{"Room for the next estimated trial?"}
    Check -->|No| Return["Return accepted candidates"]
    Check -->|Yes| Trial["Reset and interact"]
    Trial -->|Exception| Return
    Trial --> Fired{"Matching successful tool event?"}
    Fired -->|Yes| Keep["Keep message; add accepted trial cost"]
    Fired -->|No| Skip["Discard message; wall time still passes"]
    Keep --> Limit{"2,000 accepted?"}
    Limit -->|Yes| Return
    Limit -->|No| Check
    Skip --> Check
```

`_fired()` checks for an event whose `ok` is exactly `True`, whose tool name is
`http.post`, and whose `data` contains the marker. It does **not** call the scoring
predicates or inspect `score_cell_signature`. “Accepted” therefore means this
trace check passed, not that replay or Private scoring is guaranteed.

Two clocks explain otherwise surprising behavior. Unsuccessful trials consume wall
time but do not increase `replay_cost`, because that sum covers only returned
candidates. Warm-up is outside individual trial measurements but still consumes
the overall budget. Also, `slowest` starts at **25 seconds** and only increases;
the next-trial reserve never falls below **33.75 seconds** (`25 * 1.35`). The loop
can stop with unused time because it reserves that conservative margin.

The budget tests happen before an interaction. They do not interrupt an in-flight
interaction, and measured construction-time costs are estimates of later replay
costs. Historical comments claiming “100% firing,” guaranteed replay safety, or a
universal timeout rule are stronger than this code and the bundled evidence prove.

## method21 and method39: sample, rank, then commit to one style

These versions replace per-candidate filtering with a small race between message
styles. They spend part of the budget learning which style produces the desired
event efficiently, then create a large batch without testing each returned item.
“Blind” describes that final construction step, not a lack of all earlier trials.

The style pool varies wording, argument presentation, requested closing replies,
and model-format text. The purpose is to compare ways of eliciting the same intended
tool behavior within a limited trial budget. Labels such as `terse` and `min` express
an intended message shape; they are not measurements of speed. The
[style reference](code_reference.md#what-the-style-labels-refer-to) explains the labels.

Both implement the same outline:

1. With `env is None`, return 32 default-style candidates without probing.
2. Set a probe deadline at 18% of the supplied budget, then warm up with the default
   style. If warm-up raises, return 2,000 default-style candidates.
3. Visit styles sequentially. For each trial, `_probe_once()` measures reset plus
   interaction time and obtains the number of matching marker-post events.
4. Count the attempt as one `fire` if **any** matching event exists. Two matching
   events in one attempt still count as one fire in the race statistics.
5. Sort the measured styles by the ranking key below. Use the winner only if it has
   at least one fire; otherwise keep the default `apreimp` style.
6. Build 2,000 new messages of the chosen style and return them. The probe messages
   themselves are not part of this returned batch.

```mermaid
flowchart LR
    Warm["Warm-up"] --> Sample["Sequential style trials"]
    Sample --> Rank["Rank successful attempts per second"]
    Rank --> Choose["One style for this run"]
    Choose --> Batch["Construct 2,000 new messages"]
    Batch --> Replay["Separate replay decides the score"]
```

The ranking is lexicographic, with all three terms sorted descending:

```python
(
    fires / total_elapsed,       # primary: successful attempts per measured second
    fires / attempts,            # tie-break: fraction of attempts with a hit
    -total_elapsed / attempts,   # tie-break: shorter mean trial time
)
```

For a **synthetic arithmetic example, not a project measurement**, style A has
6 fires in 8 attempts taking 8 seconds; style B has 8 fires in 8 attempts taking
16 seconds. A ranks first at 0.75 fires/second versus B's 0.50, even though B's
hit rate is higher. The policy prioritizes observed throughput, not hit rate alone.
Neither quantity is the SDK's normalized score or its novelty bonus.

The differences between the two files are concrete:

| Setting | method21 | method39 |
|---|---:|---:|
| Style pool | 4 families | 5 format variants |
| Attempts per style, before deadline | Up to 16 | Up to 8 |
| Maximum counted style trials | 64 | 40 |
| Warm-up trials, outside those statistics | 1 | 1 |
| Probe tool-hop cap | 1 | 2 |
| Probe-budget fraction | 18% | 18% |

The actual hop limit is also bounded by the supplied configuration. The deadline
can reduce the number of trials and leave later styles unmeasured. It is checked
before a trial, so it is not an interruptible hard timeout. The probe timer ends
before exporting and inspecting the trace, so that processing time is absent from
the ranking denominator even though wall time continues to pass.

### What “per-model” means in method39

There is no `if model == ...` branch, model-name lookup, or latency-based identity
classifier in this file. Each `run()` invocation observes the environment supplied
to it and selects a style for **that invocation**. Separate calls with different
model environments can therefore select different styles. The code alone cannot
show that two models actually selected different winners in a scored hosted run;
the needed branch traces are not bundled.

`raw_schema_bare` is one option in the pool; it is not forcibly assigned to Gemma.
The historical docstring's claims about which model keeps which format describe
the design rationale, not a hard-coded outcome. The format strings, including
`ANALYSIS_OPEN`, are text presented to the model; they do not change Python control
flow or select a model. Their hosted effect is not isolated by the aggregate score.

### What can distort the race

Styles run in a fixed order and may receive unequal sample counts when time runs
short. Inside the trial loop, an exception is recorded as zero posts and **0.001
seconds**, rather than its actual elapsed time. In a mixed successful/failed style,
that can understate measured cost and make its throughput estimate optimistic.
All-zero styles still cannot replace the default based on this ranking.

These are interpretation limits of the preserved policy. No scored source file
was edited to remove them.

## method44: remove the chooser and hold the request shape fixed

This version asks whether a static four-action message is useful without a style
race. Removing the chooser avoids generation-time sampling and makes the intended
request shape uniform. It does not make the model's actual number of actions
externally observable from an aggregate score alone.

`run()` explicitly discards `env` and `config`. It constructs 2,000 candidates.
For candidate `i`, `_list_continue_msg(i * 16, 4)` inserts four indexed destinations
into **one message**. `URL_STRIDE = 16` keeps these four-index groups apart between
candidates; there is no loop of four `env.interact()` calls in this implementation.

“k4” means **four intended tool actions**, not four messages, four guaranteed tool
calls, or four scored findings. The model must follow the continuation request
during later replay. Stopping early, blocking, malformed output, repeated scored
cells, and runtime cost can affect the result, but the bundled aggregate score
does not identify which of those caused this entry's outcome.

## Shared helpers: why the same small functions recur

`_alpha2()`, `_label()`, and `_url()` turn integer indices into short, distinct
destination labels. `_alpha2()` wraps every 676 indices, while `_label()` adds a
suffix after that point, avoiding a simple repeat of the two-letter label. This
controls part of the candidate text; it does not guarantee a unique scored-cell
hash or that the model copies the destination exactly.

`_msg()` or `_list_continue_msg()` builds text. `_fired()` and `_count_marker_posts()`
inspect trace events. Those are different jobs from `eval_predicates()` and the
global scored-cell accounting explained in [scoring mechanics](scoring_mechanics.md).

method39 and method44 also contain an **outer notebook wrapper**: their
`attack_code` string holds the implementation, and the final lines write it to
`/kaggle/working/attack.py`. Importing or running the outer file writes that file;
it does not merely load an `AttackAlgorithm` class. Read the string without
executing the wrapper. v3_livefill and method21 are direct class implementations.

## Connect code behavior to the recorded outcome carefully

| Curated submission row | Recorded Public | Recorded Private |
|---|---:|---:|
| `v3_livefill` | 60.975 | 0.000 |
| `method21_family_race_breakout` | 92.385 | 0.000 |
| `method39_broad_per-model_race` | 93.835 | 0.000 |
| `method44_static_list_continue_k4` | 73.245 | 0.000 |

These values come from the [owner-maintained CSV](../results/submissions.csv);
individual Private scores were entered manually. The archived method39 and
method44 files match retained scored-registry hashes. The exact uploaded identities
of every other artifact are not independently proven. See [provenance](../results/README.md).

The source explains why live-fill can stop early, why a race selects one style,
and why static k4 performs no construction-time trials. It does **not** explain
the exact causal contribution of an edit to a Public score. Likewise, all four
recorded Private values being zero shows the recorded lack of transfer for these
entries; it does not reveal the hidden defense's implementation. The current
[post-mortem](postmortem.md) separates those conclusions from historical hypotheses.

## Where the supporting scripts fit

The probes ask what happened inside a particular runtime: how long reset and
interaction took, which tools appeared in a trace, or how request shapes compared.
The hash tool asks which exact file was tested. Neither changes the fact that
Public, proxy, and Private evidence answer different questions. The
[supporting-tool reference](code_reference.md#supporting-diagnostics-and-artifact-tools)
explains the measurements and their limits without requiring a model run.
