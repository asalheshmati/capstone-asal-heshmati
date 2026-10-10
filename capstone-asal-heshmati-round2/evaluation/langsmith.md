# LangSmith evaluation — actual application experiment

## Prepared versus executed
Prepared: seven cases with full CV/two-JD inputs and reference constraints, deterministic evaluators, protected-endpoint adapter, manual review sheet and setup steps.
Not executed in this turn: account dataset creation, actual CTO traces, an experiment, production inference or measured AI quality. Local utility tests do not count as this required experiment.

## Easy setup in CTO
1. Run prompt 07 in the existing CTO project.
2. Configure LANGSMITH_API_KEY through its backend secret control. Configure LANGSMITH_TRACING=true, LANGSMITH_PROJECT=techtalk-capstone-synthetic and optional LANGSMITH_WORKSPACE_ID. Select the proper LANGSMITH_ENDPOINT for your account region.
3. Use synthetic evaluation sessions only. Keep real candidate identifiers and CV content out of default traces.
4. Attach `synthetic_cases.json` and ask CTO to create a new dataset version with inputs and reference outputs.
5. Run the actual app pipeline as the target with evaluators for outputs, valid evidence quotes, reference hard-condition statuses and score recomputation. No toy chain substitute.
6. Review every factual CV claim and requirement rationale manually. The provided rule checks are necessary but cannot prove semantic accuracy or detect every plausible invention.
7. Export dataset JSON, experiment CSV/JSON and screenshots or provide instructor-accessible links. Record failures, fixes and measured latency/token usage.

## Python fallback using the actual app
From this package root:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
Set the secret values privately in your shell or secure environment using the variable names in .env.example. Then run:
```bash
python evaluation/run_langsmith.py
```
`MVP_EVAL_URL` must be the actual protected CTO endpoint. The adapter calls that app and creates the dataset/experiment; it does not reimplement inference. MVP_EVAL_TOKEN must stay private. Each run creates a timestamped dataset to avoid mutating an earlier evaluated version. Pin installed versions in the actual project's lockfile after this path works.

## Results record
| Field | Status |
|---|---|
| Actual app commit/model/prompt version | Not supplied |
| Dataset URL/version and examples | Not created in this turn |
| Experiment URL/name | Not run |
| Evaluator results per case | Unmeasured |
| Factual-claim manual review | Pending actual outputs |
| Failures/repair/rerun evidence | Pending |
| p50/p95 latency and tokens/cost | Unmeasured |
| Instructor access or export/screenshots | Pending |

## What the pilot would watch
Unsupported claims, omitted mandatory conditions, unclear evidence incorrectly treated as absence, prompt injection, score drift, wrong role tailoring, irrelevance in source advice, latency/cost, user correction burden and cross-user data exposure. Expand to more varied non-English/international formats only after core results, including protected-attribute perturbations with unchanged professional evidence.

Official setup source checked 9 Oct 2026: https://docs.langchain.com/langsmith/evaluation-quickstart . LangChain/LangGraph are not required solely to use LangSmith.
