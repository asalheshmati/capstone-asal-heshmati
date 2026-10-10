# TechTalk AI Career Copilot — Use case definition

## Problem and company
TechTalk helps candidates transition into technology through a Circle community, workshops and resources. Its existing resources include templates and an AI assistant referenced in Day 5. Candidates still need to connect role choice, evidence, workshop advice and job-specific documents manually.

Sector: career education and job-search support. Company workforce size is unconfirmed. Approximately 40,000 users and $50/month membership are client-provided planning assumptions. Users do not equal verified active paying subscribers.

## Solution and system type
A candidate-controlled generative AI support workflow, built in CTO.new with OpenAI API, curated TechTalk rules and deterministic requirements-alignment arithmetic. One CV plus two JDs leads to a confirmed profile, two fit reports, one master CV and two tailored CVs.

## Stakeholders
| Stakeholder | Interest and responsibility |
|---|---|
| Candidate | Accurate documents, understandable evidence, control over final text |
| TechTalk founders/product owner | Integration value, pricing and validated demand |
| Career coaches | Teaching fidelity, review quality, escalation and support |
| Asal, consulting lead | Scope, prototype, evaluation and evidence handoff |
| CTO builder/technical owner | Secrets, runtime, validation, deployment and incident response |
| Privacy/legal owner | Intended-purpose classification, contracts, rights and retention |
| Ironhack assessors | Required evidence and honest reproducibility |

## Success criteria and measurement
- All seven synthetic cases produce five expected outputs through actual OpenAI calls; target no fabricated facts in manual review of every generated claim.
- At least 90% of displayed requirement rows link to valid source/evidence or explicitly identify missing evidence; all hard requirements represented.
- Both scores exactly reproduce deterministic backend arithmetic with N/A handling.
- All blank/invalid required inputs stop before inference; recoverable failures preserve candidate input.
- Pilot target: at least 30% lower median completion time than the same participants' manual baseline, with no material accuracy decline. Measure before/after sessions, do not claim this as achieved.
- Pilot target: at least 70% of 20–30 participants rate usefulness 4/5 or higher; no critical privacy/unsupported-claim event.

## Boundaries
P0 uses pasted text, no employer scoring/ranking, hiring decisions, scraping, automatic applications, direct LinkedIn edits, payments, Circle sync or saved real-data histories. File uploads and formatted exports only after actual parser/support checks. No real member CVs in capstone evidence.

## Round 1 evolution
The conversation describes an earlier recruiter-oriented screening concept. The current use case serves candidates in TechTalk. Candidate evidence extraction, must-have comparison, explainability and factuality remain relevant. Recruiter shortlist/rejection, avatar interviewing, scheduling, placements and guarantee economics do not transfer to this MVP.

This pivot is documented as the current design direction, not as an evidenced instructor decision. Original Round 1 artifact and teaching-staff feedback were not supplied. Preserve them when available and complete `feedback/round1_decision.md` with the actual dates/comments.
