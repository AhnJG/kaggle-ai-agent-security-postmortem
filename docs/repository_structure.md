# Repository structure references

The layout was reviewed on October 11, 2026 against these related repositories:

| Project | Observed organization | Applied here |
|---|---|---|
| [Microsoft LLMail-Inject challenge analysis](https://github.com/microsoft/llmail-inject-challenge-analysis) | Its README introduces the closed challenge and links analysis content; challenge implementation is a separate repository. | Lead with the result and analysis, then link records and historical artifacts. |
| [ETH Zurich AgentDojo](https://github.com/ethz-spylab/agentdojo) | Documentation, source, examples, notebooks, and run outputs have separate locations. | Keep documentation, score records, Python artifacts, and archived plans distinct. |
| [UIUC InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) | Source, data, and assets are separated, with setup and evaluation explained in the README. | Keep figure reproduction instructions beside clear data provenance and runtime limitations. |

This is a retrospective archive, so its entry points are:

- `README.md`: outcome, navigation, figure reproduction, attribution.
- `docs/`: current analysis and an explicitly historical experiment log.
- `results/`: curated CSV, provenance, artifact identities, and figures.
- `src/attacks/`: preserved historical Python artifacts.
- `reference/submission_notebooks/`: preserved multi-candidate Markdown plans.
- `probes/`: diagnostic cells, with their incomplete setup documented.
- `tools/`: hashing and result inspection helpers.
- `third_party/`: upstream license notices.

These projects were consulted for organization. Experimental code and discussion
origins are recorded separately in [NOTICE](../NOTICE).
