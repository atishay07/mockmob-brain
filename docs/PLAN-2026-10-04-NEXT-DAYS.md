# Working plan for the next few days — set by the owner, 4 October 2026

This is the order of work. It narrows ROADMAP-2027.md and the 3–4 October differentiator decision;
evidence rules (no invented gains, uncertainty means quarantine, owner-approved production changes)
still bind. Budgets are owner-set and are the actual limits — agents must not invent stricter ones.

| Budget | Limit | Where enforced |
| --- | --- | --- |
| Student-facing AI (PrepOS replies, Score Recovery AI) | USD 25 per IST calendar month | `runtime_ai_budget.monthly_cap_usd` (production DB) |
| Question/content generation | USD 50 lifetime | `scripts/pipeline/lib/budgetLedger.mjs` (`CONTENT_LIFETIME_CEILING_USD`) |
| Student credits | 10 PrepOS credits/month free, 50 Pro | wallet RPCs (`mm_ai_reserve_credits` …) |

## Naming (decided 4 October)

- **Marketing name: "Score Recovery".** It says what students want: win back the marks they keep
  losing. Used in hero, ads, store listing and social: "Score Recovery for CUET".
- **Feature/place name: "Score Recovery Lab".** The in-app surface where diagnosis, repair and fresh
  practice live.
- **Action name in copy and buttons: "Mistake Repair".** Catchy, works everywhere a single wrong answer
  is fixed ("Repair this mistake").
- **Loop line:** "Find the marks you're losing. Repair the mistake. Prove it on fresh questions."
- "Repair that holds" stays an internal principle (delayed fresh checks), not public copy.
- Honesty guard: never print a number of "marks recovered" or a score promise. "Recover" names the
  method; proof is shown as fresh-question results with their sample size.

## Night 1 — 4 October: Score Recovery + AI (this session)

1. Unblock AI: budgets above, AI migrations on production (done, owner-approved), Anthropic provider
   added, routing to OpenAI tonight because the Anthropic key is invalid.
2. **Mistake Repair** (AI inside Score Recovery): on every wrong answer, the AI solves the question
   first; only if it matches the key does it explain why the pick was tempting, why it fails, the idea
   to keep and a 10-minute next step, then offers 5 fresh questions on the chapter. Disagreement →
   blind second opinion → question withheld for re-check, student not charged.
3. PrepOS model replies on (monthly credits); facts from the shared plan stay authoritative.
4. Keep the candidate recovery pathway and its validator; it releases after the learning migrations.

## Day 2 — 5 October: Trustworthy practice (error-free questions, AI-first)

Goal: every question a student sees is verified by AI evidence; uncertain ones are withheld.
- Audit the existing generator/pipeline (`scripts/pipeline/`) and the evidence gate
  (`data/evidence_registry.js`, `data/calibration_manifest.json`).
- Design: generate → independent blind solve (different model family) → key match → alternative-answer
  challenge → quarantine on any disagreement. Mistake Repair disputes already feed this queue.
- NTA mode on verified questions only.
- Open question for the owner: keep the $2 calibration stage before the $50 ceiling, or release it
  directly once the blind-solve gate is in place.

## Next — Google Play app (Android only)

- The brain's original mobile plan is in SPEC.md (Capacitor, email OTP, secure storage, free beta).
- Prerequisites the owner must provide: Google Play developer account, signing key, a test device.
- iOS is out of scope.

## Open owner items

- Replace the invalid `ANTHROPIC_API_KEY` (local and Vercel); then flip routing to Claude per
  AI-MODEL-REPORT-2026-10-04.md and re-run `scripts/learning/ai-live-smoke.mjs`.
- Set the `AI_*` routing env vars in Vercel production and deploy.
- AI purchases (top-up checkout, charged Rival battles) stay closed (`RELEASE_GATES.aiCommerce`)
  until a real captured top-up is verified.
- DPDP: under-18 consent and telemetry review before ~13 May 2027.
