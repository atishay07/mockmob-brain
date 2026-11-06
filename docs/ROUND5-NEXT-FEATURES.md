# After Round 5: scoped follow-up work

The owner subsequently approved implementing the remaining work in this chat. Local
implementation is recorded in `ROUND5-COMPLETION.md`; existing server and billing contracts
remain authoritative. This table preserves the original scope and external release gates.

Current state: Tonight's plan, evidence-gated mistake replay, install support and bounded
offline submission/resume are implemented locally. Monthly cancellation was hardened, but
activation cannot proceed without the configured Razorpay monthly plan ID. Signed-in Today,
Practice setup, existing Result, Review and Account were inspected read-only in the owner's
existing browser session. This was not the staging submission/resume test in item 1. Physical
devices and screen-reader acceptance in item 6 remain outstanding.

| Order | Scope and acceptance | Dependency / release gate |
| --- | --- | --- |
| 1 | Staging account: Practice → Result → Review → next Practice; refresh/resume an unfinished session; submit premium NTA using both skins. Record server attempt IDs and verify one debit, one result. | An approved staging target and test account. Never substitute fixtures for persistence evidence. |
| 2 | Tonight's plan: present the existing 10/20/30-minute server plan on Today, with a completion state tied to its recorded session ID. Pip presents the action; no independent recommendation logic. | Verify step 1; define completion/idempotency before UI changes. |
| 3 | Mistake replay: Result chapter → short practice set with eligible unseen questions; delayed fresh check separately labelled. Show unavailable when sufficient evidence-qualified content is absent. | Source identity, calibration and quarantine gates; no automatic content publication or paid generation. |
| 4 | Monthly Pro ₹99: configure the real plan identifier, stage subscription/cancel/webhook reconciliation, preserve all one-time buyers. | Explicit billing activation approval and Razorpay sandbox evidence. Never create a live plan or run checkout implicitly. |
| 5 | Installable PWA: explicit offline/resume state, local draft answers reconciled to the existing server session. No local scoring or fabricated completion. | Threat model for shared phones, retention/expiry rules, offline write queue and conflict tests. |
| 6 | Device acceptance: budget Android + iPhone; VoiceOver/TalkBack/desktop screen reader; touch interruption, font scaling, keyboard, contrast and weak-network resume. | Physical devices and step 1. Emulation is supporting evidence only. |

Suggested delivery order: staging proof, Tonight's plan, eligible replay, independently gated
billing activation, offline resume, then physical-device release sign-off. Each is reversible
behind its existing capability gate; billing/data migrations require separate dry-run evidence.
