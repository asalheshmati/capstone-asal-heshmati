# Five stakeholder scenario charts
All five charts derive from the explicit planning assumptions in business/assumptions.json. They show hypothetical commercial outcomes, not observed TechTalk revenue or public labor-market data.

| File | Stakeholder question | Metric and interpretation |
|---|---|---|
| 01_revenue_scenarios.png | How do $10/$15/$20 and 1%/3%/5% affect revenue? | First-month gross revenue on an assumed 40,000-user base |
| 02_churn_cohort.png | How much of an initial cohort remains? | Active payers at 3% monthly churn, no new acquisition |
| 03_cumulative_net_benefit.png | Does the baseline recoup costs over time? | Cumulative receipts minus all modeled costs, including $4,000 upfront |
| 04_operating_break_even.png | How many payers cover monthly costs? | Ceiling of $750 fixed cost divided by per-payer contribution |
| 05_operating_cost.png | Which expenses matter most? | First month ongoing cost breakdown, excluding upfront spending |

Reproduce from package root with python scripts/roi_model.py. CSVs preserve unrounded values. Chart rationale: isolate one commercial decision per chart. These are useful consulting evidence but do not complete the Round 1 public-dataset research requirement or prove willingness to pay. Original Round 1 charts remain to be supplied/preserved.
