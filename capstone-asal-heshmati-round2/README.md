# TechTalk AI Career Copilot — Capstone Round 2

Author: Asal Heshmati. AI provider: OpenAI API. Builder: CTO.new.

A candidate supplies a CV and two job descriptions, reviews their extracted factual profile, and receives two explainable job-fit reports, one master CV and two tailored CVs.

## Submission status

This repository contains the prepared Round 2 documents, presentation, builder prompts, schemas, synthetic dataset, evaluation utilities and scoring reference code. Actual CTO application source, current live verification, POC screenshots/workflow export, demo recording, LangSmith experiment results and original Round 1 artifacts still need to be added. Reference Python code does not establish a working deployed MVP.

Read `SUBMISSION_CHECKLIST.md` and `final_audit.md` before submitting.

## Deliverables

| Required item | Repository path | Status |
|---|---|---|
| Use case definition | `use_case_definition.md` | Prepared |
| POC documentation | `poc/poc_documentation.md` | Prepared; workflow evidence and recording pending |
| ROI and risks | `roi_risk_assessment.md`, `business/`, `scripts/roi_model.py` | Prepared |
| EU AI Act | `compliance/eu_ai_act_compliance.md` | Draft analysis prepared |
| GDPR | `compliance/gdpr_documentation.md` | Draft analysis prepared |
| Deployment and commercialization | `strategic_plan.md` | Prepared |
| Presentation | `presentation.pptx`, `presentation/demo_script.md` | Deck and script prepared; recorded demo pending |
| MVP | `mvp/mvp_documentation.md`, `mvp/` | Reference utilities; actual application source pending |
| LangSmith | `evaluation/langsmith.md`, `evaluation/synthetic_cases.json`, `evaluation/run_langsmith.py` | Dataset inputs and adapter prepared; live experiment pending |
| Round 1 continuity | `feedback/round1_decision.md`, `round1/README.md` | Pivot documented; original submission and feedback pending |

## Local utility checks

From this repository root:

```bash
python -m unittest discover -s tests -v
```

The ten tests check scoring, evidence checks, hard conditions and fixtures. They do not call OpenAI or measure live AI performance.

`requirements.txt` describes Python reference/evaluation dependencies. Follow `evaluation/langsmith.md` to install dependencies and run an experiment against the real application. Configure secrets privately using the names in `.env.example`.

## Build and application handoff

Follow `START_HERE.md`, `BUILD_GUIDE.md` and prompts `01`–`08` in the existing CTO project. Preserve existing app history and Round 1 materials. Add the exported application source and actual dependency manifest/lockfile without overwriting its working layout. Record real install, build and run instructions in `mvp/mvp_documentation.md`.

## GitHub upload

Extract the ZIP and upload the contents of this directory to your existing capstone repository, preserving Round 1 folders. Include `.gitignore` and `.env.example`. Commit synthetic examples and reviewed source files. Keep keys, real candidate records and private logs out of commits.

For a local checkout, copy these files into it and review `git status` before committing. This ZIP has no Git history and has not been published to GitHub.

`file_manifest.json` records archive content hashes, excluding itself. No license is assigned to client materials.
