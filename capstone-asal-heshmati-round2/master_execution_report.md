# Master prompt execution — Outputs A–J

The current implementation provider is OpenAI API only, with CTO.new retained as the builder.

| Output | Prepared result | File or folder |
|---|---|---|
| A — Source analysis | All 18 source files, teaching rules, labels/duplicates and requirement matrix | source_analysis.md; requirements_matrix.md |
| B — Scope | One evidence workflow, 2 JDs, 2 fit reports, master + 2 tailored CVs | resources/01_product_scope.md; architecture.md |
| C — Architecture | Existing app backend + OpenAI structured outputs, rule context and deterministic scoring | architecture.md |
| D — Build instructions | Where to paste resources/prompts and 8 acceptance-gated stages | START_HERE.md; prompts/; CTO_Prompt_TechTalk_OpenAI.docx |
| E — Tests | 7 full synthetic candidates, references, evaluator utilities and actual-app LangSmith adapter | evaluation/; mvp/; tests/ |
| F — Business | 9 price/conversion scenarios, 12/36-month ROI, break-even, downside, 12 risks | roi_risk_assessment.md; business/; charts/ |
| G — Capstone docs | Use case, POC/MVP evidence records, compliance, GDPR/DPIA, strategy and setup | root Markdown; compliance/; poc/; mvp/ |
| H — Presentation | 20 editable slides, speaker notes and four-minute demo script | presentation.pptx; presentation/ |
| I — Roadmap | 30 days of pilot and prioritized modules | roadmap_30_days.md |
| J — Audit | Evidence-specific PASS/PARTIAL/MISSING/NEEDS VERIFICATION | final_audit.md |

Read execution_plan_30_hours.md for the hour-by-hour plan. Your first action is to attach resources/01–05 to the existing CTO project and paste prompts/01_inspect_and_connect_openai.md.

Ten local scoring/evaluator checks pass and the ROI calculations reconcile. Actual MVP inference, LangSmith results, demo recording, application source export and original Round 1 evidence remain to be attached. critical_inputs.md identifies what is needed.
