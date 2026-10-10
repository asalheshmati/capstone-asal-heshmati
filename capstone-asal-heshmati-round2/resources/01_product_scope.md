# Product scope — TechTalk AI Career Copilot
Provider: OpenAI API only. Builder: CTO.new. User: candidate who controls their own CV.

P0 inputs: pasted CV (file upload only when verified), current role/location, optional projects, two target labels and exactly two full pasted JDs. Third JD is optional only after the two-JD flow passes.

P0 journey: input → extraction → candidate corrects and confirms factual profile and missing-information answers → comparison → deterministic scoring → generate documents → candidate edits → copy/download text.

P0 outputs: five tabs in this order: Job fit A, Job fit B, Master CV, Tailored CV A, Tailored CV B. Retain any working current flow before introducing navigation changes.

Each report: score/band, five-category breakdown with N/A handling, requirement table and evidence, hard-requirement block, top matches, unclear evidence, suggestions, interview topics and explicit non-prediction text. Include evidence completeness separately from score.

All three CVs share the exact factual history. Master contains approved career record with relevant emphasis. Tailored documents target A/B respectively. Never rename actual past titles into target titles. Do not confuse an aspirational headline with current employment.

P1 only after gates: PDF/DOCX parsing, PDF/DOCX exports, LinkedIn copy, five learning links, account/history. P2 and future: live discovery, automatic applications, billing, Circle integration, portfolio sites, social monitoring, avatar interviews. No multi-agent application architecture.

30-hour delivery target: core app, evaluation evidence, complete consulting docs, deck and demo. Public/synthetic capstone data only. No visual polish while core AI is failing.
