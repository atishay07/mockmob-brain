---
name: conversion-baseline-and-funnel-switch
description: "10 Nov 2026 — MockMob has no visitor data; the aggregate funnel exists but FUNNEL_ENABLED is the owner's open switch; known rates are after sign-up only"
metadata:
  node_type: memory
  type: project
  originSessionId: 585e670b-982c-44d4-b5f2-1ceca346163e
  modified: 2026-11-09T20:55:30.769Z
---

As of 10 Nov 2026 the website records no visitors: Vercel Web Analytics is not enabled (the API answers
`web_analytics_not_enabled`) and `funnel_daily` holds 0 rows. The first-party aggregate funnel (15-16 Oct: `/api/funnel`,
`src/lib/funnel.js`, `/admin/funnel`, both migrations applied on production) counts only while `FUNNEL_ENABLED=true`,
which the owner has not set since 16 Oct. The home page only sends its steps from branch `web/1110-conversion`
(a0745a808, built 10 Nov, not live when written).

Rates that do exist (production, read 10 Nov): 1,493 sign-ups in Apr-May 2026, 61 from June to 9 Nov (about 12 a
month, some are test accounts); a first set finished within 24 h of sign-up by 48% last season and 36% since June;
6.7% of May sign-ups paid.

**Why:** the owner's ambition is "10x conversion and a 50%+ rate" (LK186). Without the switch there is no baseline, and
at about 12 sign-ups a month no controlled test can read out.

**How to apply:** before claiming or planning any conversion lift, check whether `funnel_daily` has rows; define event
(`signup_complete`), audience (`landing_view`, signed-out home page loads) and window first; call every lift a
hypothesis. Details: `mockmob-brain/docs/CONVERSION-PASS-2026-11-10.md`. See [[prod-writes-blocked-in-auto-mode]] for
why agents only read production.
