# ROI, monetization and risk assessment
All money is USD. Scenarios, not actual company revenue. Source business assumptions: master prompt. Recomputed 9 October 2026 using scripts/roi_model.py and unrounded CSV data.

## Assumptions and cost inputs
| Input | Value | Status and interpretation |
|---|---:|---|
| Community users | 40,000 | Unverified user-provided scenario base, not confirmed paying/eligible members |
| Existing membership | $50/month | Unverified context; excluded from incremental add-on revenue |
| Add-on prices | $10 / $15 / $20 | Hypotheses to test |
| Initial conversion | 1% / 3% / 5% | Initial cohort converts once; no replacements assumed |
| Monthly churn | 3% | Modeling assumption; compounded monthly |
| Refunds | 2% of gross | Assumption; deducted from receipts |
| Payment cost | 3% of gross + $0.30 per active payer/month | Planning allowance, not a processor quote |
| API allowance | $0.40 per active payer/month | Budget assumption subject to measured usage |
| Support | $1 per active payer/month | Cost allowance, not demonstrated workload |
| Hosting | $150/month | Planning estimate |
| Storage | $20/month | Future private production storage allowance |
| Maintenance | $500/month | Estimate |
| Evaluation/monitoring | $80/month | Estimate |
| Fixed recurring total | $750/month | Sum of hosting, storage, maintenance and monitoring |
| Development | 30 hours × $75 = $2,250 | Imputed consultant cost, not an invoice |
| Setup/testing | $750 | One-time estimate |
| Initial privacy/legal review | $1,000 | Planning estimate; no claim that this buys production conformity |
| Upfront total | $4,000 | Pilot/MVP scenario, not a quote for full commercial rollout |

Taxes, financing and incremental marketing acquisition costs are excluded from both revenue and costs. No currency conversion is applied. If acquisition spending is needed, add it to monthly costs. Full production integration and compliance remediation may require a separate budget. The 36-month model assumes stable prices and cost policy, so it is a scenario horizon rather than a forecast.

## API cost basis
The checked OpenAI gpt-4.1-mini page lists $0.40 input and $1.60 output per million tokens. At an assumed 15,000 input + 9,000 output tokens across one complete workflow, cost is $0.0204 per run. Five runs/month cost $0.102 before retries/evaluation. An approximate 4× buffer motivates the $0.40 monthly allowance. Measure actual tokens, output length and retry rate before selling an allowance. The model is a provisional cost baseline; quality results decide whether it is suitable.
Source: https://developers.openai.com/api/docs/models/gpt-4.1-mini . Source prices checked 9 Oct 2026. Hosting, payment, support and maintenance numbers are explicit estimates rather than external sourced prices.

## Calculation definitions
For month t: active = initial cohort × 0.97^(t−1). Gross = active × price. Receipts = gross × 0.98. Payment fees = gross × 0.03 + active × $0.30. Variable cost = active × ($0.40 API + $1 support). Total cost = upfront + recurring fixed + payment fees + variable costs over the chosen horizon.

Net benefit = receipts − total cost. ROI = net benefit / total cost × 100. Revenue after refunds is not net profit. Monthly contribution per payer = price × (1−0.02−0.03) − $0.30 − $0.40 − $1. Operating break-even = ceiling($750 / contribution). Cumulative cash payback also includes the upfront $4,000.

## All nine pricing/conversion scenarios
| Price/month | Initial conversion | Initial payers | Month 1 gross | 12-month net benefit | 12-month ROI | 36-month net benefit | 36-month ROI |
|---|---:|---:|---:|---:|---:|---:|---:|
| $10 | 1% | 400 | $4,000 | $18,840 | 89.0% | $38,261 | 78.5% |
| $10 | 3% | 1,200 | $12,000 | $82,521 | 220.1% | $176,783 | 209.8% |
| $10 | 5% | 2,000 | $20,000 | $146,202 | 271.6% | $315,306 | 263.2% |
| $15 | 1% | 400 | $6,000 | $38,230 | 175.6% | $80,439 | 160.6% |
| $15 | 3% | 1,200 | $18,000 | $140,691 | 357.7% | $303,318 | 343.6% |
| $15 | 5% | 2,000 | $30,000 | $243,152 | 427.5% | $526,197 | 416.1% |
| $20 | 1% | 400 | $8,000 | $57,620 | 257.4% | $122,618 | 238.4% |
| $20 | 3% | 1,200 | $24,000 | $198,861 | 483.1% | $429,853 | 465.9% |
| $20 | 5% | 2,000 | $40,000 | $340,102 | 567.4% | $737,088 | 553.7% |

## Base and downside
Baseline $15 × 3% × 40,000 users: initial 1,200 payers. Month 1 gross $18,000, receipts $17,640, payment fees $900, API $480, support $1,200, fixed $750. Ongoing first-month cost $3,330, contribution after fixed costs $14,310, before initial development cost. Cumulative modeled payback occurs in month 1.

12 months: receipts $180,021, total cost $39,330, net benefit $140,691, ROI 357.7%.
36 months: receipts $391,592, total cost $88,274, net benefit $303,318, ROI 343.6%.

The base appears attractive because it assumes immediate conversion from a very large unverified reachable base. If only 1,000 eligible users are reachable at 3% conversion, initial payers are 30. At $15, 12-month net benefit becomes $-9,158, ROI -67.0%, and cash payback does not occur within 12 months. This sensitivity makes membership validation a client decision gate.

## Break-even
| Price/month | Contribution/payer/month | Active payers for operating break-even |
|---|---:|---:|
| $10 | $7.80 | 97 |
| $15 | $12.55 | 60 |
| $20 | $17.30 | 44 |

Operating break-even does not mean upfront cost has been repaid. Churn eventually reduces a cohort unless retention or new acquisition offsets it. Track both active paid members and net contribution.

## Candidate value hypothesis
If a candidate spends 45 minutes producing a master CV and two tailored versions manually and 15 minutes with reviewed AI outputs, the saving is 30 minutes/run. Four runs/month save two hours; at an assumed personal time value of $15/hour, that is $30 of time value versus a $15 add-on. These are illustrative hypotheses, not measured results or promised interview benefit. Collect a manual baseline in the pilot.

## Risk matrix (likelihood and impact 1–5)
| Risk/type | L | I | Score | Mitigation | Owner/trigger |
|---|---:|---:|---:|---|---|
| Fabricated qualification or result — ethical/technical | 4 | 5 | 20 | Approved profile, evidence IDs, full factual review, block unsupported claims | Technical/coach owner; any invented qualification stops release |
| CV/trace disclosure — regulatory/security | 3 | 5 | 15 | Private backend, minimization, no real CV traces, access controls and DPA | Technical/privacy owner; disclosure stops pilot |
| Employment use crosses high-risk boundary — regulatory | 3 | 5 | 15 | Candidate-only scope, no employer ranking, classify at scope change | Product/legal owner; employer feature request triggers review |
| Bias or misleading score — ethical | 3 | 4 | 12 | Protected attributes excluded, paired tests, hard conditions and uncertainty visible | Coach/product owner; score changes on irrelevant trait prompt review |
| Missing essential condition hidden by score — technical/ethical | 3 | 5 | 15 | Independent mandatory-condition block and reference tests | Technical owner; omitted blocker stops release |
| API quota/outage/schema failure — technical | 3 | 3 | 9 | Bounded retries, validated outputs, clear errors, last verified build/recording | Technical owner; failure-rate trend triggers incident |
| Cost escalation from large inputs/retries — operational | 3 | 3 | 9 | Size caps, token monitoring, quota/fair use and measured cost | Product owner; cost/payer exceeds allowance |
| Low conversion or high churn — commercial | 4 | 4 | 16 | Validate eligible reach, pricing and usefulness before integration | Founders; no paid pilot without demand evidence |
| Client content rights unclear — legal/IP | 3 | 4 | 12 | Approve licensed corpus, cite provenance, no transcript redistribution to public repo | Client owner; missing permission blocks commercial use |
| Deletion/transfer claims exceed actual controls — regulatory | 3 | 5 | 15 | Validate vendor contracts, region, logs, retention and rights workflows | Privacy owner; unsupported claim blocks real-data pilot |
| 30-hour scope expands — operational | 4 | 4 | 16 | Hour gates, paste/text export, postpone optional features | Asal; missing hour-10 reports freezes additions |
| Prompt injection — technical | 3 | 4 | 12 | Treat CV/JD text as data, no tools/secrets in model, case C07 and output validation | Technical owner; instruction execution blocks release |

These ratings are initial design estimates. Actual pilot incidents and observed failures update likelihood, controls and residual risk.
