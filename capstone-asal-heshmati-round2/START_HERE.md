# Your next CTO.new steps

## 1. Use your existing project
Open the CTO.new project that produced your TechTalk Career Copilot. Keep its current working screens. This package improves that project rather than asking you to rebuild it.

## 2. Give CTO five resource files
Attach these files from the ZIP to the project's context/resource control if it offers one:
1. `resources/01_product_scope.md`
2. `resources/02_techtalk_rules.md`
3. `resources/03_scoring_policy.md`
4. `resources/04_security_and_privacy.md`
5. `resources/05_output_contract.md`

Do not attach the entire compliance pack to every model request. The curated resources are the build context. CTO must also include the relevant rules in actual server-side inference prompts.

If you cannot see an attachment control, open each Markdown file, copy its text and paste it into the CTO builder chat in that order. Say: “Save this as [exact path] in the project and use it as the current specification.” The interface and secure secret control must be identified by CTO from this project, so this guide does not invent button names.

## 3. Paste the first prompt
Open `prompts/01_inspect_and_connect_openai.md`. Copy all of it. Paste it into the CTO.new builder chat for the existing project. Wait for its inspection and implementation report.

## 4. Configure the API privately
When CTO identifies its real backend secret control, set `OPENAI_API_KEY` there. Use `OPENAI_MODEL=gpt-4.1-mini` provisionally, subject to account access and test results. A ChatGPT subscription does not configure this application's API key. Do not paste the key into this guide or the builder's ordinary conversation.

The application should make a small server-side request. If it fails, ask CTO to report a redacted error category and fix that connection before expanding the app.

## 5. Proceed one prompt at a time
Use prompts 02, 03, 04 and 05 in sequence. After each, check the acceptance test written at its end. You should see factual profile confirmation, two evidence-based reports, three CVs and working copy/edit/download.

## 6. Test and collect evidence
Attach `evaluation/synthetic_cases.json`. Use prompt 06. Then add the LangSmith secret privately and use prompt 07. If CTO cannot run Python, it can adapt the same dataset/evaluators to its actual backend language, or you can run the protected endpoint adapter locally. Keep experiment output tied to the app's actual code.

## 7. Finish the submission
Use prompt 08. Save real screenshots, a 2–5-minute demo recording, source repository and LangSmith evidence. Fill the evidence fields in the POC/MVP docs. Keep your original Round 1 work. Use the deck as a complete presentation draft and update its evaluation/status slides with measured results before delivery.

## The five deliverables you should see on screen
Job fit A → Job fit B → Master CV → Tailored CV A → Tailored CV B.

Stop adding features until all five outputs and the required evaluation/evidence work. The full plan and fallback for each hour are in `execution_plan_30_hours.md`.
