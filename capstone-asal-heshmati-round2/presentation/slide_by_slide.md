## Slide 1 — TechTalk AI Career Copilot

Candidate-controlled factual documents; OpenAI API; CTO.new

Speaker notes: Present the candidate-facing scope. This deck supports a pilot decision, with evidence readiness shown honestly. Source: Masterprompt for Capstone Project.txt and CTO prompt. The user selected OpenAI API.

## Slide 2 — The candidate still applies the advice manually

TechTalk teaches role choice, CV writing and LinkedIn positioning.

Candidates still connect their evidence to individual job requirements.

The proposed workflow turns those lessons into reviewed documents.

Client assumptions: ~40,000 users and ~$50/month membership.

Speaker notes: TechTalk already supplies workshops, templates and an AI assistant in premium resources. Do not claim all resources are static or no AI exists. 40,000 users and $50 membership are user-provided assumptions, not verified paying members. Sources: TechTalk DAY 5(1).docx, source_analysis.md, master prompt.

## Slide 3 — Round 1 foundation and the candidate-facing pivot

Retained knowledge | Current direction
Candidate evidence and job requirements | Private candidate coaching and factual CVs
Explainability, must-haves and evaluation | Two JDs and three controlled documents
Prior research and staff feedback | Original artifacts still need to be attached
Commercial analysis | Scenario data; no invented market findings

Speaker notes: The supplied documents contain assignment requirements, not Asal's actual completed Round 1 submission or instructor feedback. Conversation described recruiter screening; current product is candidate support. Preserve original artifacts. Source: Capstone Brief, Capstone Evaluation Rubric, Round 1 Deliverables, feedback/round1_decision.md.

## Slide 4 — TechTalk rules shape the outputs

A clear role family and a reusable factual base.

Short summaries and concise action–task–result bullets.

Real achievements and transferable skills supported by evidence.

Essentials and hard conditions remain separate from preferred skills.

LinkedIn copy follows the primary target in a later module.

Speaker notes: Sources: CV Templates pp 1–6; TechDay 1 01:08–01:11, 01:38–01:42, 01:59–02:15; TechTalk Day 4 pp 12–15; Day 5 pp 4–7; Day 6 pp 3–6. Paraphrase: clear target, brief summary, action/task/result, evidence-based transferability, distinguish essential criteria. Numeric workshop anecdotes are not validated product claims.

## Slide 5 — One workflow produces five reviewed outputs

Input | Output
CV and candidate corrections | Master CV
Target A and JD A | Fit report A + Tailored CV A
Target B and JD B | Fit report B + Tailored CV B
Candidate review | Editable text, copy and .txt download

Speaker notes: P0 inputs are a CV, two target labels and two full pasted JDs. Ask bounded questions and confirm evidence. Five tabs follow existing tested order. Third JD, formatted file parsing, LinkedIn and saved accounts are optional after acceptance. Sources: master prompt, resources/01_product_scope.md.

## Slide 6 — Candidate review sits before document generation

1   Candidate supplies CV, targets and two JDs.

2   AI extracts evidence; candidate corrects and confirms it.

3   Backend compares requirements and calculates alignment.

4   AI generates CVs from the same approved factual record.

5   Candidate reviews, edits and exports the text.

Speaker notes: Explain extraction, then candidate correction/attestation, comparison/scoring, generation, final edit/export. Candidate-attested is not independently verified. Source architecture.md and output contract. No automated applications or employment decisions.

## Slide 7 — Prepared artifacts and live evidence have different status

Ready in this package | Still requires actual execution
Sources, resource files and build prompts | Current CTO app with secure OpenAI calls
Seven full test fixtures and evaluator utilities | Actual case outputs and factual review
Business, risk and compliance documents | LangSmith dataset, traces and experiment
Deck, notes and four-minute demo script | Recording, source export and staff feedback

Speaker notes: This is a complete preparation and consulting package, not an evidence-complete MVP submission. An earlier conversation reported live acceptance; no current actual-app test or LangSmith run occurred in this turn. Final audit distinguishes written readiness from observed feature behavior.

## Slide 8 — OpenAI calls run through the existing backend

Layer | Implementation decision
Application | Existing CTO.new frontend and backend
AI | OpenAI Responses API + structured schema
Knowledge and score | Curated source rules + backend arithmetic
Session and evaluation | Memory session + synthetic LangSmith traces

Speaker notes: Use the actual CTO app stack after repository inspection. OpenAI Responses structured outputs, store=false, schema validation; deterministic scoring. Curated rules live in server prompts. Browser memory and temporary file parsing only if verified. LangSmith synthetic tracing. Source: architecture.md; https://developers.openai.com/api/docs/guides/structured-outputs ; https://docs.cto.new/essentials/overview . Model is configurable, provisional gpt-4.1-mini, actual access pending.

## Slide 9 — Alignment scoring remains explainable

Design weights before N/A normalization (%)

{"cats":["Essential","Experience","Skills","Preferred","Portfolio"],"series":[{"name":"Weight","values":[40,25,20,10,5],"fill":"#5f8700"}]}

Speaker notes: Weights are product design choices, not hiring science. Each JD criterion assigned once. Direct=1, partial=.5, unknown/contradicted=0. Categories absent from JD are N/A and excluded from denominator. Unknown majority yields insufficient-information band. Hard conditions show independently. Source resources/03_scoring_policy.md and mvp/scoring.py.

## Slide 10 — Four-minute demonstration

0:00–1:20   Inputs, extraction and candidate confirmation.

1:20–2:05   Evidence, scores and mandatory conditions.

2:05–3:20   Three CVs, factual consistency and edit/export.

3:20–4:00   Actual LangSmith evidence and pilot decision.

Speaker notes: Follow presentation/demo_script.md. Use synthetic C01. Recording must show actual extraction, evidence review, two reports, master/tailored documents and copy/download. The script exists; the video is not recorded. Update this slide with actual live URL and build ID after validation. Do not show API secrets.

## Slide 11 — Seven cases test the behaviors that matter

Evaluation target | Required evidence
No fabricated career facts | Manual review of all generated CV claims
Traceable requirements and hard conditions | Source quote checks + semantic review
Score arithmetic and N/A behavior | Deterministic backend recomputation
Actual app performance | LangSmith experiment and real case results

Speaker notes: Seven fixture cases cover recruiter automation, teacher transferability, in-progress cert and career break, SQL gap, licensing blocker, sparse evidence and prompt injection. Ten local scoring/evaluator checks pass. That result does not measure LLM quality. Actual LangSmith experiment and manual review remain missing. Source evaluation/synthetic_cases.json, tests/test_scoring_and_evaluators.py, evaluation/langsmith.md.

## Slide 12 — Pricing and conversion drive scenario revenue

First-month gross revenue on assumed 40,000 users (USD)

{"cats":["$10/month","$15/month","$20/month"],"series":[{"name":"1% converts","values":[4000,6000,8000],"fill":"#c1ed35"},{"name":"3% converts","values":[12000,18000,24000],"fill":"#5f8700"},{"name":"5% converts","values":[20000,30000,40000],"fill":"#183a25"}]}

Speaker notes: All values are scenarios on an unverified 40,000-user base. 1%,3%,5% initial conversion yields 400,1200,2000 initial payers. Gross first-month revenue only, before churn/refunds/costs. Prices $10,$15,$20. Source business/roi_scenarios.csv and scripts/roi_model.py. No existing membership revenue is counted.

## Slide 13 — The $15 baseline depends on verified member reach

40,000-user base, 3% conversion | 12 months | 36 months
Receipts after refunds | $180,021 | $391,592
Total modeled cost | $39,330 | $88,274
Net benefit | $140,691 | $303,318
ROI | 357.7% | 343.6%

Speaker notes: Base inputs: $4,000 upfront, $750 fixed/month, 3% monthly churn with no replacement, 2% refunds, 3%+$0.30 payment cost, $0.40 API and $1 support per payer/month. ROI=(receipts after refunds minus total costs)/total costs. Source roi_risk_assessment.md. If only 1,000 reachable eligible users convert at 3%, initial payers=30 and the 12-month model loses money. This is the key validation dependency.

## Slide 14 — Operating break-even is 60 payers at $15

Active paying subscribers needed for recurring costs

{"cats":["$10/month","$15/month","$20/month"],"series":[{"name":"Payers","values":[97,60,44],"fill":"#5f8700"}]}

Speaker notes: Contributions per payer are $7.80,$12.55,$17.30 for $10,$15,$20. Fixed $750/month. Ceiling gives 97,60,44 payers. This covers recurring operation, not initial $4,000. API baseline from official gpt-4.1-mini price page: https://developers.openai.com/api/docs/models/gpt-4.1-mini . Actual costs/usage remain unmeasured. Source scripts/roi_model.py and business/assumptions.json.

## Slide 15 — Release gates address the material risks

Risk | L×I | Required control
Invented career claim | 20 | Approved facts and full claim review
CV or trace disclosure | 15 | Private backend and minimized traces
Employer-use classification change | 15 | Purpose review before scope expansion
Essential condition hidden by score | 15 | Independent mandatory-condition block
Low demand or high churn | 16 | Opt-in pilot and member validation
Unverified deletion/transfer claims | 15 | Vendor contracts and actual data map

Speaker notes: Full document contains twelve risk rows with 1–5 likelihood and impact, mitigations and owners. This slide highlights six. Scores are initial risk estimates, not measured residuals. Stop release on fabricated qualifications, omitted blockers or CV disclosure. Source roi_risk_assessment.md and short DPIA.

## Slide 16 — Candidate coaching has a defined legal boundary

Current scope: private coaching and factual candidate documents.

Provisional class: outside listed high-risk selection uses, with transparency duties.

Employer filtering, ranking or eligibility use requires reassessment.

AI disclosure and literacy apply; generated-output marking needs review.

Current Annex III high-risk timeline: 2 December 2027.

Speaker notes: Provisional inference, not certification: restricted candidate coaching appears outside Annex III recruitment-selection use, but numerical scoring and distribution need intended-purpose review. Employer applicant filtering/evaluation triggers high-risk assessment. Profiling blocks Article6(3) exception for AnnexIII systems, human review alone not exempting. Current timeline checked9Oct2026: transparency/general applicability2Aug2026, AnnexIII high-risk2Dec2027, regulated products2Aug2028. Sources: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai ; https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3 ; /article-6 ; /article-50 . Written conformity summary/technical outline in compliance pack, production controls unverified.

## Slide 17 — Personal data controls precede a real-member pilot

Keep the capstone demonstration synthetic.

Minimize CV content and keep credentials on the backend.

Document vendors, legal bases, retention and cross-border transfers.

Support review, correction, export and applicable erasure rights.

Verify actual behavior before making privacy claims to members.

Speaker notes: Synthetic capstone only. Production requires actual controller/processor roles, necessity-based lawful basis, data minimization, retention/rights and transfers. Session clearing does not erase provider logs. Responses store=false is not Zero Data Retention or proof of EU-only processing. Complete DPIA screening and short DPIA with owner sign-off. Sources compliance/gdpr_documentation.md; OpenAI data controls https://developers.openai.com/api/docs/guides/your-data ; Commission/EDPB linked in document.

## Slide 18 — An opt-in pilot comes before rollout

Phase | Gate before expansion
POC — 30 working hours | Core workflow + actual evaluation evidence
Pilot readiness — days 1–7 | Content rights, data controls and owner review
Opt-in pilot — days 8–21 | 20–30 users, time/usefulness/cost measured
Pricing decision — days 22–30 | Validate $10 / $15 / $20 and unit economics

Speaker notes: Plan20–30 adult participants, source licenses, vendor/data controls, support and rollback. Proposed gates≥30% median task-time saving,≥70% usefulness4/5+,≥90% evidence provenance, no critical unsupported fact/privacy event. Prices10/15/20 are hypotheses. Do not invent revenue or user feedback. Existing premium AI support means incremental value and pricing must be validated. Source strategic_plan.md.

## Slide 19 — Later modules follow core evidence and pilot results

Next: LinkedIn copy and five verified learning recommendations.

Version 2: permitted job discovery with original links and freshness.

Version 3: tracking, interview practice and portfolio guidance.

Billing, Circle integration and saved history require separate implementation.

Speaker notes: Sources roadmap_30_days.md and master prompt. LinkedIn copy/learning suggestions are P1 after core. Version2 permitted employer/board discovery with original links and deduplication; no blanket social scraping permission. Version3 tracking/interview/portfolio. No automatic messages/applications authorized by this presentation.

## Slide 20 — The next decision is a measured pilot

Complete actual app/evaluation; validate member reach and data controls; pilot then decide rollout.

Speaker notes: Recommend finishing current MVP/evaluation evidence and confirming member reach/pricing before rollout. Askclient for intendedpurpose/contentrights/privateproject source and commercial assumptions. Asal owns build/evidence; technical owner app/secrets; coaches factual fidelity; privacy/legal roles/data; founders pricing/pilot. Final submission needs actual app, experiment, recording, source and originalRound1 work. Sources final_audit.md, strategic_plan.md.
