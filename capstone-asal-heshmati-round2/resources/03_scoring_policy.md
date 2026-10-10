# Scoring policy v1

Design weights: essential 40, experience 25, technical/transferable skills 20, preferred 10, portfolio 5. These are proposed product weights, not validated hiring science.

Requirements must cite the JD verbatim in their source field and belong to exactly one category. Classify a must-have tool in essential, rather than counting it in both essential and skills. Add independently stated experience/skill requirements to their respective categories. Flag hard requirements separately from weighted categories.

Evidence values: documented direct match = 1.0; documented partial match = 0.5; not documented/unclear = 0; explicitly contradicted = 0. Each has a reason and quote(s). Candidate-attested answers may count as evidence with a visible attestation label. The system does not independently verify them.

For category c, component = mean of item values. A category is N/A only when the JD has no applicable requirement in it. Missing portfolio evidence is 0 only if the JD requires or prefers it; if the JD does not request portfolio evidence, portfolio is N/A. The same rule applies to preferred qualifications.

Overall = round(100 × sum(weight[c] × component[c]) / sum(applicable weight[c])). The backend calculates all arithmetic, not the LLM. Display original weights, effective weights after normalization and every contribution. N/A is excluded from the denominator, not set to 0.

Documented alignment bands: 80–100 strong, 50–79 moderate, 0–49 limited. These thresholds are product design choices. If there is no applicable JD criterion, or more than half the criteria are not documented/unclear, use insufficient information as the band. Keep any calculated score marked provisional and show evidence coverage. An explicit negative requirement is known evidence and is not counted as unclear.

Hard requirements: met / explicitly unmet / unclear. No inferred work authorization, licenses, languages or salary compatibility. An explicitly unmet or unclear hard requirement remains prominently visible even with a high score. Do not automatically reject the candidate or silently cap the score.

Use this sentence on each report: This score describes documented alignment with the supplied job requirements. It does not predict ATS passage, recruiter response, interview selection or hiring.

At least 90% of displayed requirement assessments must have valid source/evidence links in the synthetic test set, with all hard requirements accounted for and zero fabricated facts. A deterministic source-quote check validates provenance, not the semantic correctness of the assessment. Human review tests semantics.
