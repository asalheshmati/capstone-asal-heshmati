# Strategic deployment and commercialization plan

## Buyer, user and differentiation
Buyer: TechTalk product/founder team. User: member targeting a coherent role family. Offer: a factual CV and job-fit workflow that applies TechTalk source rules and shows evidence. Differentiate from generic chat through linked requirements, consistent career facts, controlled scoring, editable outputs and measured quality. Validate differentiation against TechTalk's existing premium AI assistant before charging.

## Phases and gates
| Phase | Duration and owners | Activity | Gate |
|---|---|---|---|
| POC/capstone | 30 working hours, Asal + technical owner | Synthetic two-JD workflow, documents, LangSmith and recording | Seven actual cases; no fabricated claims; all hard requirements covered; core/error checks pass |
| Internal pilot readiness | Days 1–7 after capstone, product/privacy/technical owners | Confirm content rights, processors, intended purpose, data behavior and support | Real-data controls verified; evidence endpoint restricted; rollback available |
| Opt-in pilot | Days 8–21, 20–30 adults, coaches and product owner | Observe manual baseline vs assisted completion; collect usefulness, edits, defects and willingness to pay | ≥30% median time saving, ≥70% usefulness 4/5+, ≥90% evidence coverage, no critical factual/privacy issue |
| Paid pilot decision | Days 22–30, founders | Test $10/$15/$20 through stated willingness to pay or a separately authorized payment pilot | Actual pricing data, bounded support/API cost, privacy/legal sign-off and favorable unit economics |
| Controlled rollout | After pilot gate, not forced into capstone | Incremental member cohorts with monitored quota/support | Cohort retention, quality and incident thresholds sustained |

Do not expose real member data merely to reach a schedule date. Failing quality or privacy gates pauses expansion and returns the product to synthetic testing.

## Pricing hypotheses
Core: $15/month baseline, sensitivity at $10 and $20. Define a fair-use allowance provisionally at five full runs/month with retries bounded. Validate actual usage before publishing limits. Existing $50 membership, inclusion rights and user counts need client confirmation. Subscription entitlement, payment fees and billing implementation remain future tasks.

Future bundles: Core CV + fit $10–15; Career Plus with LinkedIn/learning guidance $20; interview practice module $5–10 add-on; discovery/tracking module $5–10 add-on. These are proposals, not live prices or verified demand. Avoid charging twice for an already included premium AI benefit without demonstrating added value.

## GTM
Pilot recruitment through TechTalk's existing community and workshop channel by its owner. Demo inside a CV workshop, show an evidence-based example, invite opt-in feedback, and use coach support during pilot. This plan does not send member outreach or publish promotional claims automatically.

## KPIs
POC: valid output rate, factual errors, requirement provenance, hard-condition recall, score consistency, recovery tests.
Pilot: median task time vs manual baseline, useful rating, factual correction rate, completion/drop-off, cost/full run, latency p50/p95, support tickets per active user, consent/deletion requests.
Commercial: eligible members reached, opt-in rate, actual payer conversion, gross/net monthly revenue, refund rate, monthly churn and contribution per payer. Do not mix total community users with reached eligible paid members.

## Communications and ownership
| Audience | Cadence | Owner/content |
|---|---|---|
| Founders | Weekly | Product owner: gate decisions, cost, adoption and risks |
| Coaches | Before pilot and weekly | Asal: teaching changes, factual-error cases and escalation |
| Technical owner | Each release | Commit/model/prompt versions, regressions and rollback |
| Privacy/legal owner | Before real data and each scope change | Data map, contracts, transfers and classification |
| Pilot users | Onboarding and feedback close | Explain AI use, evidence limits, edit/export and support |
| Instructors | Final submission | Repo, recorded/live demo, evaluation and honest audit |

## Rollback
Technical owner can disable generation, preserve the last verified model/prompt version and keep manual workshop/templates available. Critical unsupported qualifications or a cross-user data leak stops the pilot until repaired and retested. Publish recovery decisions internally with actual timestamps.
