# Historical diagnostic scripts

These scripts were written for Kaggle notebooks, not as a standalone Python package.
They require the competition SDK, fixtures, and model runtime. The three
`aas_step4_*` files are notebook continuation cells: their docstrings list the
setup helpers that must already exist (`COMP_DIR`, model factories, and server
cleanup helpers). That setup notebook and recorded JSON outputs are not bundled.

Consequently this repository supports inspection of these diagnostics, not a
complete reproduction of their reported runs. Local `local_gguf` results establish
behavior in that environment; a `cm391` board-like runtime is a proxy. Neither
establishes a hosted score or the hidden guardrail's behavior.

`local_gateway_probe.py` uses the organizers' local gateway and a community runtime
approach credited in [NOTICE](../NOTICE). It writes `/kaggle/working/attack.py` and
may install `llama-cpp-python` if missing; inspect it in a dedicated Kaggle workspace
with the required inputs before running. It does not submit an entry itself.
The publication edits create the output directory and replace an invalid pip
option; no hosted or model execution was performed to validate those edits.

Some comments in the historical scripts express stronger causal interpretations
than their measurements support. In particular, an intercept fitted to total
`interact()` time is not an isolated measurement of model prefill, and findings
counts alone cannot identify a model-format failure. See the current interpretation
in [scoring_mechanics.md](../docs/scoring_mechanics.md).
