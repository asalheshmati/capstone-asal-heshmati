# TechTalk AI Career Copilot — OpenAI execution package

Owner: Asal Heshmati. Prepared 9 October 2026. Builder: CTO.new. AI provider: OpenAI API only.

## Your next action
1. Extract this ZIP.
2. Open your existing TechTalk project in CTO.new. Preserve the existing application and source history.
3. Attach the five files in `resources/` to its project context. If no resource attachment control exists, paste the contents into the builder chat in the order shown in `START_HERE.md`. Ask CTO to write them to the repository.
4. Paste `prompts/01_inspect_and_connect_openai.md` into the CTO.new builder chat.
5. Add your key through the project's secure backend secret control when CTO identifies it. Never put a key in the prompt, resource documents or browser code.
6. Proceed through prompts 02–08 only after the preceding acceptance check passes.

Read `START_HERE.md` for the short guide, `execution_plan_30_hours.md` for the exact plan, and `final_audit.md` for the evidence still needed.

## What this package contains
- Source analysis and an exact rubric matrix for both rounds.
- Five curated builder resource files and eight staged build prompts.
- Seven complete synthetic candidate cases, two synthetic job descriptions per case, references and validation tests.
- An executable scoring module, a server-side OpenAI reference pipeline and a LangSmith evaluation adapter for the actual CTO app.
- ROI scenario data, reproducible calculations and five scenario charts.
- Use case, POC, MVP, risk, EU AI Act, GDPR, pilot and roadmap documents.
- An executive PowerPoint with notes, its slide-by-slide text and a four-minute demo script.

## Evidence status
Documents, fixtures, arithmetic and package validation can be completed here. A prompt does not prove an application works. The CTO repository, current live build, OpenAI credential and LangSmith project were not supplied as an accessible execution environment in this turn. The earlier conversation reports a live acceptance test, but this package does not reuse that as a newly observed result.

The reference pipeline is supporting code for CTO to adapt, not a substitute for the required CTO.new application. Live inference, file upload support, deployment, LangSmith traces, recording and instructor feedback remain evidence tasks. No simulated result is marked as an AI test pass.

## Repository placement
Keep your existing Round 1 material in its original folders. Add this package's Markdown and resources to the same repository. Put actual app source under `mvp/` or retain the current app layout and document it. `requirements.txt` covers the Python evaluation utilities, not CTO's actual app dependencies. Export and commit CTO's package manifest and lockfile when available.

## Reproduction
Run `python -m unittest discover -s tests -v` for local scoring and evaluator checks.
Run `python scripts/roi_model.py` to reproduce the scenario CSVs and charts.
For LangSmith, install `requirements.txt` in your own environment, configure the secrets in `.env.example`, and follow `evaluation/langsmith.md`. Set `MVP_EVAL_URL` to the protected evaluation endpoint implemented by prompt 07 so the experiment measures the real app.

Use only synthetic data for the capstone demonstration. Originals and source references remain preserved in the source inventory. Do not publish proprietary TechTalk transcripts without the client's permission.
