Work in this existing TechTalk AI Career Copilot project. Read the five attached resource files first. Preserve working features and existing source history.

Use OpenAI API as the only inference provider. Replace any application Anthropic/Claude client, API endpoint, provider configuration and environment references with OpenAI equivalents. Do not alter unrelated builder tools. Do not print or expose existing secret values.

Inspect the actual repository and report its frontend, backend, dependency manifest, deployment method, secure backend secret mechanism, file parser and current output schema. Check each capability in code or runtime rather than assuming CTO.new supports it. Give the exact secure place for me to set OPENAI_API_KEY. Keep OPENAI_MODEL configurable, provisionally gpt-4.1-mini, and verify model access with a real server-side request after the key is configured.

Use OpenAI Responses API with structured outputs supported by this project's current SDK. Set store=false and validate parsed results. All paid API calls and keys stay on the backend. Handle missing key, invalid input, timeout, 429/5xx, refusal, incomplete response and schema failures. No silent provider fallback.

Inspect before editing. If the existing two-JD workflow works, retain it. If it is absent, implement only the first two input stages: pasted CV plus optional current role, location and projects; then Target Role A, Target Role B and two pasted full job descriptions. File upload is optional until its parser is confirmed. Provide loading and validation states.

Keep the final workflow to evidence extraction, candidate correction/confirmation, two explainable fit reports, one master CV and two tailored CVs, then edit/copy/text download. No billing, scraping, accounts, job applications or extra agents.

Implement only what is needed for the provider connection and input foundation now. Report changed files, checks actually run, what works, what needs the key and the next acceptance test. Never claim live success from a mock or a prompt.
