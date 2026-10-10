# Security, data and intended-purpose boundaries

OpenAI credentials stay on the server in OPENAI_API_KEY. OPENAI_MODEL is configurable. No frontend prefixes such as VITE_ or NEXT_PUBLIC_ for secrets. No keys in Git, screenshots, browser bundles, prompts or API error details.

Use Responses API structured outputs through a supported current OpenAI SDK, with store=false. Validate parsed output against schema. Handle refusal/incomplete response, timeouts, provider 429/5xx, absent key and schema errors. At most one bounded retry for transient errors. Do not switch providers automatically.

MVP sessions use browser memory only, with Clear session. Avoid persistent CV history in P0. An uploaded file is temporary, private, size/type checked, parsed on the backend, and deleted after extraction. Confirm actual hosting/storage behavior before making deletion claims. PDF image scans fall back to pasted text rather than adding OCR to the deadline.

The capstone uses synthetic data. LangSmith traces are enabled only for synthetic evaluation sessions. Production traces use redaction and minimization after separate privacy review. Never log full real CVs, personal identifiers or API secrets by default.

Candidate-controlled coaching only: no employer ranking, application filtering, hiring shortlist, auto-rejection, admissions decisions or eligibility decisions. Reassess EU AI Act classification before changing intended purpose. Do not label employer candidate evaluation minimal risk merely because a human approves it.

Before input show AI assistance and review requirement. Keep all factual fields editable. Attestation and evidence labels remain distinct. Never use age, gender, ethnicity, disability, religion, marital status, photos or name as scoring signals.

For production, establish actual controller/processor roles, contracts, lawful bases, retention, region and transfer mechanisms before processing member CVs. Application Clear session does not erase third-party abuse logs. store=false does not establish Zero Data Retention or EU-only processing.

An evaluation endpoint must require a private service credential and synthetic-only input. Keep it disabled outside testing. Do not expose a public paid-inference endpoint without limits.
