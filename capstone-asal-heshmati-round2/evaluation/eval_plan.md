# Evaluation plan — Round 1 criteria extended for current use case

Five core criteria: factual fidelity, requirement/evidence traceability, hard-requirement handling, deterministic score correctness, end-to-end outputs/recovery. Seven complete synthetic cases are in synthetic_cases.json with reference constraints. Actual outputs, manual pass/fail and reasons have not been invented.

| Criterion | Measurement | Proposed gate |
|---|---|---|
| Factual fidelity | Human review of each claim in all 3 CVs for all 7 cases | Zero invented employers/titles/dates/certificates/metrics/tools |
| Traceability | Exact quote checks plus semantic human review | ≥90% requirement rows trace correctly or flag missing evidence |
| Hard requirements | Inspect all mandatory conditions against supplied evidence | 100% accounted for; unmet/unknown visible regardless of score |
| Arithmetic | Recompute categories, N/A denominator and bands | 100% deterministic agreement |
| Workflow/recovery | Real app produces five outputs; blank required inputs cause no call | 7/7 valid flows; all specified error scenarios pass |

Also record p50/p95 latency and inference tokens/cost, repeated-run stability, user edits and paired irrelevant-attribute perturbation. A small synthetic set measures selected behaviors, not real hiring success, demographic fairness or production robustness. No score threshold predicts ATS outcomes.

Round 1 mini set requires actual scored runs even without LangSmith. Preserve actual prior results when supplied. The new fixture set does not retroactively establish those runs or staff feedback.
