# Output A — Source analysis

## Source inventory
All 18 supplied files were retrieved or extracted. Long transcripts were retrieved through their final text line. Parsed document page markers and transcript timestamps provide source locations. Original filenames are preserved below even where their labels conflict with content.

| File | Relevant content |
|---|---|
| Capstone Brief(1).docx | Two rounds, every student builds a working MVP; public/synthetic data; sector research and 4–6 charts. |
| Capstone Evaluation Rubric(1).docx | Exact Round 1 and Round 2 grading weights; Campus submission identifiers. |
| Capstone Round 1 Deliverables(1).docx | Round 1 repository, mini set, presentation and feedback requirements. |
| Capstone Round 2 Deliverables(1).docx | Nine deliverable areas, evidence requirements and repository structure. |
| Capstone Round 2 Deliverables Guide(1).docx | Substantially repeats the Round 2 checklist; does not add another project. |
| Capstone Round 2 Deliverables-Presentation Demo(1).docx | Repeats checklist and submission label. Does not contain the separate pf-05 presentation timing guide. |
| CAPSTONE TEMPLETS(1).docx | Planning template, decision gate, time boxes and definition of done. |
| TechTalk Day 0.pdf | Actual content: Breaking Down Behavioural Questions. STARL examples, not CV onboarding. |
| TechTalk - CV Templates(1).pdf | Template formats: short summary, action/task/result bullets, around four bullets per role, skills and section variants. |
| TechDay 1.txt | DAY 1 Career Accelerator, Sep 2026; CV and LinkedIn optimization. Embedded URL o9SuvJUkxIM. |
| TechDay 2.txt | Embedded header says DAY 3, not Day 2. URL jc4imDT9_No. Gap analysis and interview preparation. |
| TechTalk  Day 4.docx | Mastering Transferable Skills for Career Change: evidence, concrete examples, projects and positioning. |
| TechTalk DAY 5(1).docx | Role selection, master CV, LinkedIn positioning and community feedback tasks. |
| TechTalk Day 6(1).docx | Recruiter perspective: essential versus nice-to-have requirements, gaps, interview and career-break guidance. |
| TechTalk7(1).docx | Generalist career examples and demonstrating solutions to employer problems; opening appears mid-discussion. |
| TechTalk Day 8(1).docx | Recruiter discovery, direct applications and referrals; master CV and narrow LinkedIn positioning. |
| Masterprompt for Capstone Project.txt | A–J outputs, 30 working hours, mandatory CTO.new, MVP and future scope. |
| CTO-Prompt-TechTalk AI Career Copilot..docx | Initial five-stage build prompt. Updated deliverable uses OpenAI API only. |

## TechTalk rules and product interpretation
The exact rule IDs and source locators are in `resources/02_techtalk_rules.md`. Summaries are paraphrases rather than quotations.

- Focus positioning on a clear role or coherent role family. Build separate master CVs when the families diverge. Keep LinkedIn focused on the primary target.
- Prepare a strong base CV once. Tailor its headline, short summary, skills emphasis and most relevant achievements rather than altering career facts.
- Aim for no more than two CV pages. Use conventional section titles, readable formatting and concise bullets. The app must check rendered page count before claiming a two-page export.
- Template bullets follow action, task/project, and result. Add metrics only when the candidate has supplied them. A factual qualitative outcome is preferable to an invented number.
- The template suggests a short two-to-four-line summary and around four bullets per role. Its note allows experienced candidates to omit the summary, so this is a configurable choice.
- Demonstrate transferable skills through actual work. Explain the connection to a target task without converting it into invented sector tenure or technical expertise.
- Distinguish essentials from preferred requirements. A percentage match does not compensate for an essential requirement the candidate explicitly does not meet.
- LinkedIn content should use relevant role and skill terms in the headline, About, experience and skills. Featured projects and recommendations support credibility. Direct account editing stays outside the MVP.
- Use projects and case studies to demonstrate new skills. Future learning suggestions must connect to gaps and finished work, not award certificates before completion.
- Use STARL for behavioural preparation: situation, task, action, results, learning. Day 0 belongs to a future interview module.

## Contradictions and unresolved evidence
1. The three Round 2 guides duplicate the deliverable checklist. Use one canonical checklist, with the rubric as the scoring authority.
2. `TechDay 2.txt` says DAY 3 inside the transcript. A separately supplied Day 3 URL uses `iFYVwFIh6lo`. That video has no supplied transcript for this package. Keep both references and request confirmation rather than silently relabeling either.
3. `TechTalk Day 0.pdf` is a behavioural interview resource. `TechTalk7(1).docx` appears to contain only part of a session. Do not imply a complete course archive.
4. Some workshop claims generalize ATS behavior, percentages and recruiter habits. They are coaching claims without independent validation in the supplied material. Do not encode ATS guarantees, universal rejection rules, interview probabilities, or the anecdotes as market statistics.
5. TechTalk already refers to an AI assistant in premium resources in Day 5. The opportunity is an integrated evidence-based workflow and editable outputs. It is inaccurate to pitch the client as having no AI support.
6. Product choice: one underlying factual profile plus a master CV and two targeted documents. For unrelated role families, offer separate base documents in a later release. This is an explicit product adaptation, not a claimed TechTalk instruction.
7. Candidate confirmation means candidate-attested, not independently verified. Use provenance labels: CV evidence, candidate-attested, independently checked if actual verification exists, and unclear.
8. These Ironhack files describe requirements. They do not supply Asal's completed Round 1 work, instructor feedback, test results or original charts.
9. The supplied Presentation Demo file does not include the separately referenced `pf-05-project-presentation.md`. The deck covers all stated topics, but exact pitch duration and cohort-specific slide rules require confirmation.
10. Circle screenshot, active paid membership figures, conversion, usage, billing and formal content license were not available in the reviewed set. 40,000 users and $50/month are user-provided assumptions.

## Knowledge base design
The five small files in `resources/` contain scoped product requirements, teaching rules with sources, scoring policy, security/privacy boundaries and output contracts. They support a simple rules-in-context MVP. No embedding database is necessary for this version. Later retrieval should index approved passages with filename, section, timestamp/page and version, and retain rule provenance in recommendations.

## Requirement authority
Use rubric weights and the exact Round 2 checklist. The master prompt adds stronger requested outputs such as 30 hours, staged CTO prompts, commercial scenario analysis and presentation notes. The attached CTO prompt cannot override source accuracy, evidence rules or the user's explicit OpenAI provider choice.
