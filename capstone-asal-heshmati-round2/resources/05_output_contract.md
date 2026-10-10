# Output contract v1

Every source evidence item has id, fact, exact source quote, source locator and provenance status. Each CV bullet has supporting evidence IDs. New candidate answers become separate candidate-attested evidence items after confirmation. Never promote a vague claim to independently verified.

Candidate profile: name/contact only for document rendering, unchanged employers/titles/dates, education, certifications with completion status, projects, tools/skills and questions. Do not use contact fields in scoring.

Job report: job_label, target_role, overall_score, alignment_band, evidence_coverage, category_breakdown, hard_requirements, requirement_assessments, top_matches, unclear_evidence, tailoring_suggestions, interview_topics, scoring_version and non_prediction_statement.

Requirement assessment: id, requirement_text, JD_quote, category, evidence_ids, evidence_quote(s), status (direct/partial/not_documented/contradicted), rationale. Backend sets numeric credit and category arithmetic.

CVs: master, tailored_a and tailored_b, each with headline, optional short summary, skills, experience, education, certifications, projects, plain_text and change_log. Claims needing confirmation appear outside copyable CV text. Drafts with unsupported claims must be blocked from being labeled factual.

Review UI: five result tabs in required order, editable text, copy feedback, .txt download, clear session. Rerunning after input changes invalidates old reports. Generated edits remain user text and are marked as edited, not silently re-verified. Regenerate only on explicit user action.

Error states: invalid input, unsupported file, insufficient extracted text, missing key, timeout, quota/rate limit, refusal, incomplete response, invalid JSON/schema. Preserve input and provide one concrete retry/fallback action.

Required provenance display: recommendation → applicable TT rule IDs or G rule IDs → original source; assessment → candidate evidence → JD quote. File attachment to a builder is not runtime retrieval. Store curated rules in server source and verify the actual OpenAI prompt includes them.
