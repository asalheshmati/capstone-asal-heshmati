# EU AI Act classification, obligations and conformity summary
Assessment date: 9 October 2026. Intended use: candidate-controlled career coaching and factual document editing. Assessment owner: TechTalk product/legal owner to confirm before a real-data launch.

## 1. Step-by-step classification
1. The workflow uses a general-purpose model to infer recommendations and generate text, so it is an AI system. OpenAI supplies the underlying model; the party placing the integrated application on the market under its name may be the system provider. Confirm TechTalk/developer contracts rather than automatically assigning only deployer duties.
2. P0 does not use prohibited manipulation, biometrics, emotion recognition, social scoring or discriminatory traits. Examine actual app behavior rather than relying on this scope statement.
3. No regulated product safety component is intended. Article 6(1) product rules therefore do not appear relevant to the current design.
4. Annex III 4(a) covers systems intended for recruitment/selection, application analysis/filtering and candidate evaluation. This MVP is restricted to private assistance for the candidate's own documents. It does not rank applicants for employers, reject applications, select a shortlist or determine employment access. It also does not determine education admission, learning assessments or course eligibility.
5. Provisional conclusion: the restricted coaching/editing workflow appears outside the listed high-risk decision use cases, with applicable transparency obligations. This is a reasoned intended-purpose assessment, not a blanket exemption for any tool described as a career copilot. The numerical alignment function is a boundary that requires legal review of intended use and distribution before launch.
6. If the product evaluates or filters applicants on behalf of employers, supports material hiring decisions, or controls access to education, reclassify. Human approval alone does not exempt it. If an Annex III system profiles natural persons, Article 6(3)'s non-high-risk exception cannot be relied on. Document actual purpose and any exception assessment/registration required by Articles 6 and 49.

Classification is provisional pending actual-source inspection, intended-purpose contractual controls and legal review. The capstone can demonstrate the limited intended use without certifying a commercial release.

## 2. Applicable requirements for the current scope
| Topic | Planned control | Evidence/status |
|---|---|---|
| Article 4 AI literacy | Train owners/coaches on evidence, hallucination, score meaning, limits and escalation | Training checklist prepared; delivery pending |
| Article 50(1) interaction disclosure | Show clear AI assistance disclosure before first interaction, accessible to users | Required by resource files; actual UI unverified |
| Article 50(2) generated-content marking | Assess machine-readable marking duties and editing exception; implement applicable marking without changing candidate facts | Legal/technical implementation assessment pending |
| Article 50(4) public-interest text/deepfakes | Current CV documents do not target public-interest publishing/deepfakes; reassess if publishing modules added | Boundary documented |
| User control | Candidate confirms evidence, edits documents, sees uncertainty and can clear app session | Required design; actual behavior unverified |
| Change governance | Reassess class for employer/admin ranking, admissions or new profiling use | Product owner gate |

Do not claim that every AI-edited CV must visibly display an AI label, or that an editing exception applies automatically to substantive CV generation. Make the Article 50(2) assessment explicit and preserve applicable provenance.

## 3. Current timeline
The Commission's current official framework page reports general applicability and transparency rules from 2 August 2026, AI literacy from 2 February 2025, Annex III high-risk obligations from 2 December 2027, and regulated-product high-risk obligations from 2 August 2028 after the AI Omnibus entered into force on 27 July 2026. This pack uses that current timeline rather than the older August 2026 high-risk deadline. Record the exact applicable consolidated law and competent-authority guidance at launch.

## 4. Conformity assessment summary (approximately 1–2 pages)
**System and boundary.** TechTalk AI Career Copilot prepares private candidate documents and requirements-alignment advice from candidate-controlled evidence. It uses OpenAI API, source-based rules and deterministic arithmetic. Excluded uses are employer selection/ranking, autonomous eligibility decisions, biometrics and admissions assessment.

**Assessment path.** The current intended use does not appear to require the high-risk conformity-assessment route. Consequently this document is an internal conformity/readiness summary, not an EU declaration of conformity, certificate, registration or CE mark. Provider identity, model/data contracts, applicable transparency duties and actual safeguards must be checked before commercial use. A favorable classification does not establish GDPR compliance.

**Available documentation.** The use case, scoped teaching rules, scoring policy, architecture, seven synthetic fixtures, deterministic utility checks, risk register and DPIA draft exist. The sources identify proposed controls and test gates. No new actual CTO runtime, LangSmith experiment, full production security assessment or enacted policy evidence is claimed here.

**Verification work.** Inspect actual UI disclosure, source prompts, rule references, structured schemas, secret placement and data retention. Run synthetic factuality, hard-condition, score and recovery tests. Confirm no actual role allows employers to rank or exclude applicants. Determine whether generated CV outputs fall within a standard-editing exception or require machine-readable marking. Verify vendor/legal agreements and nominate monitoring and incident owners.

**Release decision.** Permit a synthetic capstone demonstration once actual core tests pass. Permit a real-data pilot only after privacy controls, contracts and intended-purpose assessment are approved by responsible owners. A production declaration cannot be issued from these unexecuted evidence items. Retest whenever prompt, model, role access or purpose changes.

**If high-risk use is introduced.** Establish lifecycle risk management, data governance, technical documentation, logs, transparency/instructions, meaningful human oversight, accuracy/robustness/security, quality management, registration/conformity and monitoring/incident processes. Select the correct Article 43 route for the use case and applicable standards, rather than assuming every employment system needs the same external certification. Do not launch employer filtering as a small extension of the coaching MVP.

**Accountability.** TechTalk's product/legal owner signs the actual-purpose assessment. Technical owner supplies evidence from actual code and configuration. Asal supplies consulting analysis and the capstone evidence pack. Review at each material release and any change of intended purpose.

## 5. Technical documentation outline
1. System identity, provider/deployer roles, version, intended purpose and prohibited uses.
2. UI, user groups, access roles and human interaction/oversight.
3. Architecture, components, OpenAI model/API settings, processing locations and dependencies.
4. Approved source corpus, rule provenance, licenses and updates.
5. Candidate/JD input schemas, extraction and scoring logic, N/A and uncertainty behavior.
6. Prompt versions, constraints, output contracts and factuality controls.
7. Data governance, minimization, storage, retention, transfers and trace redaction.
8. Validation datasets, references, experiments, metrics, failures and known limits.
9. Security/error handling, threat scenarios, injection and secret checks.
10. Risk register and mitigation evidence, fairness and accessibility assessment.
11. Change control, rollback, monitoring and incident escalation.
12. Classification reasoning, Article 50 assessment and applicable conformity records.

## Sources
- Commission framework/timeline: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Current official Annex III: https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3
- Article 6: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6
- Article 50: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50
- Underlying Regulation (EU) 2024/1689 and AI Omnibus Regulation (EU) 2026/1744 as linked by the Commission. EUR-Lex pages returned a verification wall in this session; consolidated service-desk text and Commission timeline were used, and launch review should retain the final applicable legal text.
