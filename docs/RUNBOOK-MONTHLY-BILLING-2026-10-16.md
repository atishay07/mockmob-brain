# Runbook: switching MockMob Pro to Rs 99 a month (16 Oct 2026)

Branch `web/pay-monthly-1016` (from main 77713336). The code already switches to monthly by itself when
`RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set (`isMonthlyBillingReady` in `src/lib/payments/plans.js`). This branch
makes that switch safe. Part 1 is the owner's steps. Part 2 is what the main session checks locally in Razorpay
TEST mode before the owner flips the live variable. Part 3 is the go-live and rollback. Part 4 lists the known limits.

## What changed in the code, and why

| Gap found | Fix |
| --- | --- |
| A one-time Pro holder (for example the 2026 pass to 31 Dec 2026, or a 2027 pass to 31 July 2027) lost the date when any monthly subscription event ran: `payment.failed`, `subscription.cancelled` and the rest overwrote `premium_until` with null or a shorter date | `settleUserEntitlement` (`src/lib/payments/settle.js`) reads the user's other paid access first and never shortens it. Pure rule: `resolveUserEntitlement` |
| An old subscription ending could overwrite the user's newer subscription id and status | The subscription id and status are only taken over when this subscription is the one that runs longest |
| `subscription.pending`, `subscription.paused` and `subscription.resumed` were not handled | Pending and paused keep Pro to the paid date and show `past_due`. Resumed records the subscription |
| A `subscription.charged` event whose payment was not captured, or had the wrong amount, wiped the paid evidence of a subscriber who had already paid and took Pro away mid month | Such an event is logged and changes nothing for a record that already paid |
| A `payment.failed` that arrived late, after the subscription had recovered, flipped the account to `past_due` | Ignored when the fetched subscription is `active` |
| A late `subscription.charged` for a subscription the student already cancelled switched renewals back on in Account | The `cancelled` status is kept for that subscription |
| `effectivePremiumFromRow` treated `subscription_status = 'active'` as Pro forever, whatever the date. A missed cancel webhook, or a one-time pass past its end date, kept Pro on for good | An `active` status now ends 2 days after `premium_until` (the grace covers a late renewal webhook). No date at all still means Pro, as before |
| Cancel at cycle end left Account showing "renews every month" until the cycle ended, and a second tap hit Razorpay again | The cancel route marks the account `cancelled` at once (Pro stays to the paid date) and is safe to call twice |
| Account only knew "renews" or "fixed date" | `PlanCard` now has four states: renewing, renewal off, last payment failed (with Pro still on, or off with a cancel option), fixed date |
| The first-payment check in `/verify-payment` marked a payment that was only authorised (not captured yet) as failed and told the student it did not match | It answers 202 "being confirmed" and writes nothing. The webhook grants Pro once Razorpay captures it |
| `/verify-payment` with a bad signature, or a mismatch, overwrote a subscription that had already paid | Paid records are never rewritten by a failed verify |
| A student with a monthly plan still being retried by Razorpay could start a second one and be charged twice | `/create-monthly-subscription` refuses while the earlier one is `active`, `pending` or `authenticated` at Razorpay |
| Checkout error text said "Nothing has been charged" even after the payment window had taken money, and used an em dash and a middle dot | After a payment the text says not to pay again. Dash and dot removed |
| The refund page still described monthly as "historical" and told people to cancel at Razorpay | Rewritten: monthly Pro, how to cancel in Account, no refund for a charged month, failed renewals, the one-time pass keeps its term |
| Pricing had no answer for "I paid once, what happens?" or "what if a renewal fails?" | Two FAQ entries, shown when monthly is on sale |

Tests: `npm run test:billing` (76 tests). `data/tests/billing_monthly_webhook.test.mjs` sends every event
(authenticated, activated, charged, pending, halted, paused, resumed, cancelled, completed, payment.captured,
payment.failed) as signed fake payloads to the real route, with no network.
`data/tests/billing_monthly_routes.test.mjs` covers create, verify and cancel. The helper is `data/tests/billing_harness.mjs`.

## Part 1. The owner's steps (Razorpay dashboard and Vercel)

Do these in order. Razorpay keeps TEST and LIVE separate: a plan made in one mode does not exist in the other.
So you create the plan twice, once in Test mode (for the main session's local check) and once in Live mode.

1. Open the Razorpay Dashboard and switch the toggle at the top to **Test mode**.
2. Go to **Subscriptions** in the left menu, then **Plans**, then **Create Plan**. If Subscriptions is missing from the menu,
   your account does not have it activated yet: open the Subscriptions page in the dashboard and use its request or activation
   button, or write to Razorpay support. Live subscriptions can need Razorpay's approval, so do this first.
3. Fill the form:
   - Plan name: `MockMob Pro monthly`
   - Billing frequency: **Monthly**, every **1** month
   - Amount: **99** (Rs 99.00), currency INR
   - Description: `MockMob Pro, billed monthly`
4. Save. Copy the **Plan ID** (it starts with `plan_`). Send the TEST plan ID to the main session (a plan ID is not a secret).
5. Switch the toggle to **Live mode** and repeat steps 2 to 4. Keep the LIVE plan ID for step 8.
6. Check the webhook (Live mode, then Test mode if you use one): **Account and Settings**, then **Webhooks**. The existing webhook
   must point at the live site's `/webhook` route (the same host the site is served from) and use the secret that is in Vercel as
   `RAZORPAY_WEBHOOK_SECRET`. Tick these events, in addition to what is already ticked:
   `subscription.authenticated`, `subscription.activated`, `subscription.charged`, `subscription.pending`, `subscription.halted`,
   `subscription.paused`, `subscription.resumed`, `subscription.cancelled`, `subscription.completed`, `payment.captured`, `payment.failed`.
7. Decide about the six accounts below (the main session will have read the list before you flip anything).
8. In **Vercel**, project settings, Environment Variables, add for **Production**:
   `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` = the LIVE `plan_...` ID. Then redeploy (an environment variable only applies to a new deployment).
   Leave `BILLING_WEBHOOK_SECRET` unset (and do not add it): it belonged to an older generic webhook that wrote plan status without dates. That route (`/api/billing/webhook`) is now retired and answers 410 whatever is set.
9. Open `/pricing` on the live site. It must say Pro is Rs 99 a month and show a "Start Pro for Rs 99/month" button. Until then, one-time access is still on sale.

Tonight's order that is safe: steps 1 to 4 and 6 first, so the main session can run Part 2. Do steps 5, 8 and 9 only after Part 2 has passed.

### The six accounts to decide about (read-only count on 16 Oct 2026)

Before this change, an account with `subscription_status = 'active'` stayed Pro whatever its date. On 16 Oct, 6 accounts are
`active` with a `premium_until` already in the past, so they are Pro today only because of that. After this change they move to Free,
which matches the date they paid for. The 62 captured 2026 passes end 31 Dec 2026 by their date, and without this change they would
have stayed Pro after that day too. To list the six (read-only):

```sql
select id, email, subscription_status, premium_until, razorpay_subscription_id
from users
where subscription_status = 'active' and premium_until is not null and premium_until < now() - interval '2 days';
```

If you want any of them to keep Pro, either set their `premium_until` to a future date by hand, or tell the main session to hold this
change until you decide. Nothing is written to the database by the deploy itself.

## Part 2. How the main session verifies the whole flow locally in Razorpay TEST mode

Rules: test keys only (`rzp_test_...`), never live keys. Local dev server on port 3101 only. The database is the staging Supabase
project (`onwkqxmjqjrhfbjjdydu`), never production. Staging has the needed tables and columns (`payments.access_until`,
`payments.subscription_id`, `users.premium_until`, `users.razorpay_subscription_id`, `webhook_events`; checked read-only on 16 Oct).
Headless browser only.

Note that `scripts/pipeline/tools/stagingLocalApp.mjs` blanks every `RAZORPAY*KEY*` variable on purpose, so it cannot be used for this.
Start the server by hand with the staging Supabase values and the test Razorpay values in one process environment (values live in
git-ignored `.env*` files, and are never printed or committed).

### Setup

1. Test values needed: `RAZORPAY_KEY_ID` (`rzp_test_...`), `RAZORPAY_KEY_SECRET`, `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` (the TEST plan from Part 1),
   and `RAZORPAY_WEBHOOK_SECRET` (any long random string, used only locally: the simulator signs with it).
2. Staging values from `.env.staging`: `STAGING_SUPABASE_URL`, `STAGING_SUPABASE_ANON_KEY`, `STAGING_SUPABASE_SERVICE_ROLE_KEY`. Map them to
   `NEXT_PUBLIC_SUPABASE_URL`, `SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY` as the launcher does, but keep the Razorpay test values.
3. Check the key before starting: the id must start with `rzp_test_`. Start `node --use-system-ca node_modules/next/dist/bin/next dev --port 3101`
   in the background, and stop it when done.
4. Make a throwaway test student on the local app (a test account on localhost against staging; see `AUTH-RELIABILITY-2026-10-13.md` for the sign-in paths).
   Record the test email in the checkpoint, not in chat.

### Run order, and what must be true after each step

Check `users`, `payments` and `webhook_events` with read-only SELECTs on the staging project after each step.

| # | Action | Expected |
| --- | --- | --- |
| 1 | Open `/pricing` signed out, headless, 390 and 1440 | Says Rs 99 a month, cancel anytime, the FAQ entries about a failed renewal and a one-time payment are present |
| 2 | Unset the plan ID, restart, open `/pricing` | One-time offer shown, no monthly button. Set it again |
| 3 | Signed in as the test student, tap Start Pro. Razorpay Test checkout opens. Pay with Razorpay's published test card (4111 1111 1111 1111, any future expiry, any CVV, any OTP on the bank page) or the test UPI id `success@razorpay` | The handler calls `/verify-payment`, the page says Pro is active and renews monthly. `payments` has one row for the subscription, `status = captured`, `amount_paid = 9900`, `access_until` about one month ahead. `users`: `subscription_status = active`, `is_premium` true, `premium_until` = same date, `razorpay_subscription_id` set |
| 4 | Account page | "Pro renews every month. Paid through <date>." and a Cancel renewal button |
| 5 | Simulate the webhooks (below) for `subscription.authenticated`, `subscription.activated`, `subscription.charged` using the real test subscription | Each answers HTTP 200. A repeat with the same `--event-id` answers `deduped`. State unchanged |
| 6 | Simulate `subscription.pending`, then `subscription.halted` (file mode) | `past_due`, Pro still on to `premium_until`. Account says the last payment did not go through |
| 7 | Simulate `subscription.charged` again with a later `current_end` (file mode) | Back to `active`, date moved forward, still one `payments` row |
| 8 | Tap Cancel renewal, confirm | Razorpay test subscription shows a scheduled cancel. Account says renewal is off and Pro stays to the date. `subscription_status = cancelled`, `is_premium` unchanged. Tap it again by API: 200 `alreadyCancelled`, no second Razorpay call |
| 9 | Simulate `subscription.cancelled` (file mode, `current_end` in the past), then check the row | `is_premium` false, `premium_until` null, status `cancelled`, payment row still `captured` |
| 10 | Edit the test student to hold a fake one-time pass (`premium_until = 2027-07-31T18:29:59.999Z`, matching captured `pro_cuet_2027` payment row), then simulate `payment.failed` and `subscription.cancelled` for another subscription id | The pass date and status are untouched |
| 11 | Try a second Start Pro while the first subscription is `active` in Razorpay | 409 `already_active` for a Pro student. For a past-due student with an open plan, 409 `subscription_open` |
| 12 | Bad signature (`curl` with a wrong header) to `/webhook` | 401, nothing written |
| 13 | Clean up: delete the staging test rows you created, stop the dev server, delete temp files | Port 3101 free |

Simulating webhooks. Razorpay cannot call localhost, so use the script. It refuses live keys and any host except `127.0.0.1`:

```
# real test-mode entities for a real test subscription
node scripts/billing/simulate-razorpay-webhook.mjs --event subscription.charged --subscription sub_XXXX --port 3101
# a fully fake event, no Razorpay call: states that test mode cannot produce on demand (pending, halted, paused, cancelled)
node scripts/billing/simulate-razorpay-webhook.mjs --file fake-event.json --port 3101
# the same event id twice, to see idempotency
node scripts/billing/simulate-razorpay-webhook.mjs --file fake-event.json --event-id evt_same
```

`RAZORPAY_WEBHOOK_SECRET`, `RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET` are read from the environment. A fake event file has the shape
`{ "event": "subscription.halted", "payload": { "subscription": { "entity": { "id": "sub_XXXX", "status": "halted", "current_end": <unix seconds>, "notes": { "userId": "...", "planId": "pro_monthly_99" } } } } }`.
The signed fake payloads in `billing_harness.mjs` (`subscriptionEntity`, `paymentEntity`, `webhookEvent`) show every field the route reads.

Razorpay cannot be made to renew early in test mode, which is why steps 6, 7 and 9 use the simulator. The automated suite
(`npm run test:billing`) covers the same events with no setup, and should be green first.

Also run before reporting: `npm run test:auth`, `npm run test:app`, `npm run test:learning`, `npm run test:billing`, `npx eslint` on the touched files,
and one `npm run build`. Then the visual critique the CTO loop requires for Account (the four Plan states) and `/refunds` and `/pricing`, at 390 and 1440, Night and Day.
The Plan states are text changes inside the existing card, but they have not been looked at in a browser yet.

## Part 3. Go live, check, roll back

After Part 1 steps 5, 8 and 9:

1. Look at `/pricing` on the live site. Do not buy anything on the owner's behalf. If the owner wants to prove it end to end, he pays Rs 99 himself with his own card,
   checks Account, and cancels renewal in Account. A charged month is not refunded by policy, so he may prefer to do this with a friend's agreement or accept the Rs 99.
2. Watch Razorpay's webhook delivery log: every event should show HTTP 200. A 401 means the secret differs from `RAZORPAY_WEBHOOK_SECRET`. A 503 means the variable is missing.
3. In the Vercel runtime logs, search for `[webhook] failed`. Razorpay retries a failed delivery for a day, and the route reprocesses a retried event.

Rollback: remove `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` in Vercel and redeploy. The one-time offer returns, nobody can start new monthly plans, and existing subscribers keep working:
the webhook, verify and cancel routes do not depend on the variable. Their renewals are Razorpay's, so cancel them in the Razorpay dashboard if the plan is being retired.

## Part 4. Known limits (not changed here)

- **Revenue totals under-count renewals.** There is one `payments` row per subscription (`subscription_id` and `payment_id` are unique), and it holds the latest charge.
  `amount_paid` summed over rows (admin and creator dashboards) counts a subscriber once. The real number of charges is Razorpay's `paid_count` (stored in `raw_subscription`)
  times Rs 99. A per-charge ledger needs a migration, so it was not made implicitly.
- **Creator earnings are per subscription, not per renewal.** `payout_per_sale` is recorded once on the subscription's row.
- **Monthly plans run for 24 cycles** (`totalCount: 24`), which ends in October 2028, long after CUET 2027. That is the existing product choice.
- **The Flutter app only displays the plan** ("Pro is active until <date>", from `premiumUntil` of `/api/auth/me`). It never sells and has no cancel. For a renewing subscriber the date is the paid-through date and moves forward each month. No app change was needed.
- **Cancelling while Razorpay holds the subscription in `pending`** can be refused by Razorpay for cycle-end cancel. The route returns a clear error and changes nothing; this is the existing, tested behaviour of `cancelMonthlyRenewal`.
- **Two deliveries of the same event at the same instant**: the first claims the event with a lease (`webhook_events.claimed_at`, 120 s). A duplicate that arrives while the first is still working gets a 503 so Razorpay retries it later; once the first finishes, a retry is answered as a duplicate (200). If the first crashed, the retry after the lease runs the event. Needs migration `20261016170100_webhook_event_lease.sql`; until it is applied the code falls back to the old claim (handlers are idempotent, so the result is the same).
- **The generic `/api/billing/webhook`** is retired (16 Oct 2026 security follow-up): it returns 410 and writes nothing. Before this it let a holder of `BILLING_WEBHOOK_SECRET` set `subscription_status` and `is_premium` for any user id or email, with no paid-through date and no Razorpay evidence. Nothing in the repository called it. The old code is in git history (the commit "Retire the legacy billing webhook").
