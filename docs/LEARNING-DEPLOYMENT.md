# Connected learning: staging and rollback procedure

Source work is not deployment. No SQL in this run was applied to Supabase.
The Supabase CLI was unavailable; migration files were saved manually and tested
in isolated PGlite, without installing tools or touching production.

## Staging order

1. Back up staging and inventory its columns, constraints, owner types and existing
   migration history. The older foundation migration and mode-aware atomic credit
   RPC, question_interactions and 0028 bookmark/progress tables must already be
   applied. Existing AI overlay tables live under db/migrations;
   do not assume supabase/migrations contains all installed history.
2. Review/apply saved connected_learning migration in staging. Exercise free daily,
   baseline and full-sample allowances; owner/CAS/retry/resume/deadline behavior.
   Turn LEARNING_SESSIONS_ENABLED=true only after these checks. Current ordinary
   ticket completions continue through finishPractice during transition.
3. Review/apply runtime_ai_guard. Its initial funded balance is zero and its model
   price register is empty. This grants no spending permission. Keep optional AI
   sales paused. PERSISTENT_LIMITS_ENABLED=true only after checking the RPC under
   actual service-role credentials on auth/session/learning/mentor routes. Failure
   is closed after activation. Schedule cleanup of expired rate buckets with a
   reviewed retention policy; do not delete payment/usage receipts.
4. Rival atomic submission requires both existing AI-overlay rival tables and
   20261002122000_rival_atomic_submission.sql before deploying the new submit
   service. Validate concurrent completion, rollback on detail errors and old
   pending battles. Its source guard rejects duplicate and unauthorized IDs.
5. Answer correction history requires the foundation and connected-learning
   migration. Its queue does not certify a changed key. A worker must use current
   publication evidence and deriveCorrectedScore before inserting an immutable
   revision. Automatic disputed-report re-evaluation remains paused with the
   evidence worker; uncertain questions remain withheld. Do not auto-approve.
   Changed stems, passages or reordered/edited options are not comparable with
   original selected indexes; keep the original score and exclude the comparison.
6. Register sources with permission/version/locator and independent calibration.
   Write eight complete pathways to recovery_pathways.json only when valid. Each
   pathway needs state=released, version/sourceVersion/ruleVersion, approved
   explanation/worked contrast, hypothesis matrix, probes/repair/checks and item
   question IDs/families/content hashes. Numeric steps require an independent
   solver input and matching answer. Checks are multiple choice. Four checks allow
   maintenance; additional families are needed for failure/re-repair sequences.
   Register the canonical sorted-key SHA256 of the complete pathway at
   source_registry.pathways[id], with matching versions and calibrationState
   released. Referenced questions must ALSO pass authenticated evidence/calibration
   and family-hold checks. Development fixtures are never release evidence.
7. Enable RECOVERY_PATHWAYS_ENABLED only after reservation/exposure audits and
   authenticated end-to-end testing. Verify assisted work, repeats, missing
   inventory, corrections and both delayed checks with a controllable staging
   clock. Do not manipulate production timestamps to simulate learning outcomes.
8. Record real Razorpay staging authentication, captured payment, old pending
   ₹99 orders, new versioned plan, signature/ownership/webhook replay, refund and
   reconciliation checks. Explicitly map referrals per plan; V2 inherits no offers.
9. Runtime funding/price receipts and wallet reservations, optional AI sales,
   season economics ≥70% contribution margin, eight pathways, Android/accessibility
   and payment checks are still gates. Update the central capability/release
   registry only with evidence. ₹299 cutover is a separate coordinated release.

## Rollback

Disable RECOVERY_PATHWAYS_ENABLED for new starts and turn off the new sales gate.
Already-started episodes can still advance when their current evidence is valid;
no new subscription or credits are required for their delayed checks. Preserve
LEARNING_SESSIONS_ENABLED for safe durable completion/resume; switching it off
only routes new starts to legacy tickets, existing durable finish remains readable.
Keep all history, exposures, allowances, observations, version rows and receipts.
Never drop history tables or replace old plan amounts. Do not redeploy the prior
Rival submit service while transactions are in flight. Preserve old plan records
and pending-order verification. Restore flags only after the incident is understood.

## Unfinished release criteria

The content registry is empty and calibration paused. No academic pathways or
observed student gains have been established. No authenticated staging browser,
real checkout/refund, Android, assistive-technology or field-performance evidence
was supplied. Payment reconciliation, correction-worker deployment, season cost
receipts, optional wallet reservations and an opted-in cohort are unfinished.
Use reports/learning-preflight.json and STATUS.md as the actual handoff.

## 2 October 2026 — monthly Pro billing and PrepOS replies (switch-on checklists)

Both features are built, tested locally and OFF. Nothing below was run against staging or production.

### A. ₹99/month Pro (auto-renewing)
Code: `pro_monthly_99` in `src/lib/payments/plans.js`, `/create-monthly-subscription`, `/api/billing/cancel`,
checkout in `RazorpayPaymentButton` (`billing="monthly"`), verification through the existing subscription
path in `/verify-payment` and `/webhook` (signature, captured payment, amount, owner, refund revocation).
1. In the Razorpay dashboard create a Plan: ₹99, period monthly, interval 1. (Test mode first.)
2. Set `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` to that plan ID in staging. Nothing else is needed.
3. Staging checks: start checkout, pay with a Razorpay test card, confirm `/verify-payment` marks Pro
   active; send a `subscription.charged` test webhook for month two and confirm `premium_until` extends;
   cancel from Account and confirm Pro continues to the paid-through date; send `subscription.cancelled`;
   replay a webhook (must be ignored); refund a test payment (must revoke).
4. When the variable is set in production, `publicOffer()` flips: the pricing page, landing page, Arena
   upsell and SEO title show ₹99/month, and NEW one-time ₹99 checkouts close. Existing one-time buyers
   keep their term (31 July 2027). Unsetting the variable restores one-time sales. No migration needed.
Known limits: a subscription is created with 24 billing cycles; after that the student must resubscribe.
After "Cancel renewal" the Account card does not yet remember that cancellation was requested across reloads
(a repeat press is harmless). Referral codes are tracked on monthly orders but never change the price.

### B. PrepOS model replies and monthly credits
Code: `supabase/migrations/20261002130000_prepos_credit_reservations.sql` (NOT applied),
`src/services/prepos/modelReply.js`, `replyDeps.js`, `/api/ai/mentor/chat`. Gate: `RELEASE_GATES.runtimeAi`
in `data/capabilities.js` (false) plus the emergency off switch `PREPOS_MODEL_REPLIES_DISABLED=true`.
All of these must be true before flipping the gate (also opens PrepOS top-ups):
1. Apply the reservation migration on staging (after `db/migrations/2026_05_02_ai_overlay_credits_fix.sql`
   and `20261002121000_runtime_ai_guard.sql`). Rollback: drop the table and four functions; balances unaffected.
2. Verified model prices in `runtime_ai_prices` (fresh within 30 days) and a funded `runtime_ai_budget`.
   Runtime funding is NOT authorised by the content budget ($2/$10) and was not set up here.
   **Superseded 4 Oct 2026:** runtime guard, reservations and monthly cap (USD 25) applied to
   production with owner approval; see reports/ai-migrations-dry-run-2026-10-04.json.
3. Schedule `select public.mm_ai_release_expired(100)` every few minutes (returns held credits for crashed replies).
4. Run `node scripts/learning/wallet-reconciliation.mjs --remote-read` on staging and review mismatches.
5. A real multi-session concurrency test against staging Postgres, a provider timeout test, and a
   signed-in browser pass of `/mentor`.
Then change `runtimeAi: true` in code, deploy, and watch `ai_credit_reservations` for rows stuck in
`executing`. Rollback: set `PREPOS_MODEL_REPLIES_DISABLED=true` (replies stop, record analysis keeps working).
