# Prioritized 30-hour execution plan

Thirty working hours, one-hour allocations. Documentation prepared here reduces writing time, but actual application/evaluation evidence still consumes the listed slots. There is no optional-feature allocation before P0–P2 pass.

| Hour | Priority | Objective/tool | Prompt or action | Expected output | Acceptance | Dependency | Fallback |
|---:|---|---|---|---|---|---|---|
| 1 | P0 | Scope and source check — Documents | Read source_analysis.md and requirements_matrix.md; resolve source labels without inventing data. | Scope locked | P0 matches two JDs and three CVs | None | Use current source inventory |
| 2 | P0 | Existing-project inspection — CTO.new | Paste prompts/01_inspect_and_connect_openai.md | Actual stack and change list | Existing app/source preserved | Hour 1 | Export source or screenshot inspection report |
| 3 | P0 | OpenAI secret and backend request — CTO.new | Paste prompts/01_inspect_and_connect_openai.md | Real server response | No frontend key; successful real request | Hour 2 | Fix access/quota, keep pasted input |
| 4 | P0 | Input validation — CTO.new | Paste prompts/01_inspect_and_connect_openai.md | CV + A/B role/JD inputs | Blank CV/JD blocked before API | Hour 3 | Pasted text only |
| 5 | P0 | Evidence extraction — CTO.new | Paste prompts/02_candidate_evidence.md | Structured factual profile | Exact source quotes; stable dates/titles | Hour 4 | Reduce parser to pasted text |
| 6 | P0 | Clarification and approval — CTO.new | Paste prompts/02_candidate_evidence.md | Editable questions/profile | Corrections affect next step | Hour 5 | Five fixed questions plus manual approval |
| 7 | P0 | JD extraction — CTO.new | Paste prompts/03_fit_reports_and_scoring.md | Essential/preferred/hard requirements | JD quotes; mutually exclusive categories | Hour 6 | Shorten JD to full relevant text, no scraping |
| 8 | P0 | Comparison A — CTO.new | Paste prompts/03_fit_reports_and_scoring.md | Evidence table A | Unknown ≠ absent skill | Hour 7 | Show clear evidence rows before CV work |
| 9 | P0 | Comparison B — CTO.new | Paste prompts/03_fit_reports_and_scoring.md | Evidence table B | No cross-job leakage | Hour 8 | Same comparison function for both jobs |
| 10 | P0 | Deterministic scoring — CTO.new | Paste prompts/03_fit_reports_and_scoring.md | Scores + category details | Weights/N/A recompute; hard flag visible | Hour 9 | Use provided pure scoring module |
| 11 | P0 | Master CV — CTO.new | Paste prompts/04_factual_cv_generation.md | Approved factual base CV | No new facts or incomplete certificate awarded | Hour 10 | Plain-text CV |
| 12 | P0 | Tailored A — CTO.new | Paste prompts/04_factual_cv_generation.md | Role A CV + change log | Career facts unchanged | Hour 11 | Change summary and relevant bullet order only |
| 13 | P0 | Tailored B — CTO.new | Paste prompts/04_factual_cv_generation.md | Role B CV + change log | No invented technical qualification | Hour 12 | Same approved profile and minimal tailoring |
| 14 | P0 | Review/copy/export — CTO.new | Paste prompts/05_review_and_errors.md | Five tabs and text controls | Edit, copy and .txt download work | Hour 13 | No PDF/DOCX export |
| 15 | P0 | Error recovery and secret check — CTO.new | Paste prompts/05_review_and_errors.md | Recoverable errors | Timeout/quota/schema states; no secret leak | Hour 14 | One bounded retry, preserve input |
| 16 | P0 | Seven-case acceptance run — CTO.new | Paste prompts/06_synthetic_acceptance.md | Actual outputs + first results | Seven cases recorded with timestamps | Hour 15 | Prioritize hallucination/hard-blocker failures |
| 17 | P0 | Failure repair — CTO.new | Paste prompts/06_synthetic_acceptance.md | Corrected failing cases | Affected checks pass; no fabricated metrics | Hour 16 | Remove optional features |
| 18 | P1 | LangSmith instrumentation — CTO.new | Paste prompts/07_langsmith_actual_app.md | Actual app traces | Synthetic stages visible with versions | Hour 17 | Trace protected endpoint end to end |
| 19 | P1 | Dataset and experiment — LangSmith/terminal | Paste prompts/07_langsmith_actual_app.md | Dataset + evaluator experiment | Actual app target; seven cases evaluated | Hour 18 | Python protected endpoint adapter |
| 20 | P1 | Evaluation review and export — LangSmith | Review factual fidelity, failures, latency and evidence. Export actual results and screenshots. | Measured evaluation report | Every case has observed result | Hour 19 | Export screenshots/results when link sharing blocked |
| 21 | P1 | ROI and risk reconciliation — Markdown/Python | Recompute business CSVs and replace validated client assumptions when available. | 12/36-month scenario business case | Revenue/cost/ROI reconcile | Hour 1 | Keep labeled scenarios |
| 22 | P1 | EU AI Act review — Markdown | Review intended purpose and classification. Complete the supplied conformity summary and technical outline against actual app behavior. | Classification/obligations record | Candidate coaching boundary documented | Hour 20 | Block employer-use expansion |
| 23 | P1 | GDPR and DPIA review — Markdown | Validate actual data flow, processor roles, retention, rights and transfers against the app. | GDPR pack | No unverified region or deletion claims | Hours 20–22 | Synthetic-only demo until real-data controls confirmed |
| 24 | P0 | POC/MVP reproduction evidence — CTO.new/Markdown | Paste prompts/08_release_and_evidence.md | Source, screenshots, dependencies, real setup | Fresh reader can reproduce | Hour 20 | Document gaps explicitly |
| 25 | P1 | Pilot and GTM plan — Markdown | Review strategic_plan.md with the actual test results and nominate pilot owners. | Pilot gates and pricing | POC→pilot→rollout explicit | Hours 21–24 | Small internal synthetic pilot |
| 26 | P2 | Deck results update — PowerPoint | Replace evaluation/status slides with measured app and LangSmith results; preserve honest claims. | Client-ready deck | Claims trace to evidence | Hour 25 | Use supplied text/notes with measured fields |
| 27 | P2 | Demo recording — Browser/recorder | Follow presentation/demo_script.md and record 2–5 minutes. | Four-minute recording | Candidate→reports→three CVs visible | Hour 26 | Use last verified build and backup recording |
| 28 | P2 | Rehearsal and questions — PowerPoint | Rehearse business, technical and compliance explanation with timing. | Rehearsal and backup plan | Pitch fits cohort timing | Hour 27 | Cut optional roadmap detail |
| 29 | P2 | Submission audit — Markdown/Git | Review each final_audit.md row; link evidence; keep original Round 1 files. | Evidence matrix and clean repo | No prompt-only feature marked PASS | Hour 28 | Leave unresolved row honest |
| 30 | P0 | Final live check and handoff — CTO.new/Campus | Paste prompts/08_release_and_evidence.md | Verified URLs + complete submission | One core live flow passes; correct submission IDs | Hour 29 | Backup recording with disclosed limitation |

## Time gates
- Hour 3: actual OpenAI response. If absent, fix access and backend connection before UI work.
- Hour 10: two traceable fit reports with correct arithmetic.
- Hour 15: all five outputs, edit/copy/text export and errors.
- Hour 20: seven real case results plus actual LangSmith experiment.
- Hour 25: documented business/compliance/pilot pack and reproducible source.
- Hour 30: presentation, 2–5-minute recording, final audit and submission.

Any blocked hour consumes its budget. Use its fallback and cut optional work. Do not convert synthetic fixtures into invented results to meet a time gate.
