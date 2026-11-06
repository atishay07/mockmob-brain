---
name: mockmob-pricing-and-prepos-decisions-oct-2026
description: "Owner's finalised pricing (Rs 99/month Pro) and PrepOS model-reply direction, plus the switches that keep them honest"
metadata:
  node_type: memory
  type: project
  originSessionId: 7a6c47d2-9abe-4974-b429-a709d65a8e56
  modified: 2026-10-02T15:47:36.341Z
---

Owner decisions on 2 Oct 2026:
- Pro is Rs 99 per month, auto-renewing (Razorpay subscription), cancellable in Account. Chosen over a one-time 30-day pass.
- PrepOS: reintroduce model replies on a small monthly allowance (10 free / 50 Pro credits), but only behind the staging gates.
- Wants one design language per concept everywhere (icons, credit marks); no emoji or text glyphs as UI. Wants deep research; the 300-400 site target was not achievable and the shortfall was reported.

**Why:** the owner is the business decision-maker, but handover rules still bind: nothing is advertised that cannot be bought, no migrations or paid model calls happen implicitly, runtime AI funding is not authorised by the $2/$10 content budget.

**How to apply:** pricing copy must come from `publicOffer()` (src/lib/payments/offer.js); monthly sells only when `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set, otherwise the Rs 99 one-time access stays the honest offer. Model replies stay off until `RELEASE_GATES.runtimeAi` flips after the checklist in docs/brain/LEARNING-DEPLOYMENT.md. See [[mockmob-owner-audit-jul-2026]] and [[mockmob-redesign-aug-2026]] for earlier design decisions.
