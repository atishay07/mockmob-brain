# Google Play billing, server side (18 Oct 2026)

Owner decisions (18 Oct 2026; D78 at 6:50 pm: ONE credits balance for everything): the Android app sells Pro and credit packs through Google Play Billing. Prices live in Play Console, never in code. **Pro is Rs 150 on Google Play (final, 6:38 pm), Rs 99 on the web.** The app never mentions the web price and never links to web checkout (Google's anti-steering rule). A purchase in the app grants exactly what the same web purchase grants, in the same tables, so web and app share one Pro status and one balance.

Branch `web/play-billing-1018` (from live main 00328e54 = release 8). Local, not pushed, not deployed. Nothing applied to any database (staging dry-run only, rolled back).

## What was built

| Piece | File |
|---|---|
| Product map | `src/lib/payments/playProducts.js` |
| Google auth + API (service account JWT, RS256, node:crypto + fetch, no new dependency) | `src/lib/payments/playGoogle.js` |
| Verify, grant, finish; RTDN handling (no Next imports, tested) | `src/lib/payments/playBilling.js` |
| Pub/Sub push authentication (token + optional Google OIDC) | `src/lib/payments/playRtdn.js` |
| Route handlers | `src/lib/server/playBillingHttp.js`, wiring `playBillingDeps.js` |
| Routes | `POST /api/billing/play/verify`, `POST /api/billing/play/rtdn` |
| Migration + undo | `supabase/migrations/20261018190000_play_purchases.sql`, `supabase/undo/20261018190000_play_purchases.undo.sql` |
| Tests (in `test:billing`) | `data/tests/play_billing.test.mjs` (45) |
| Other edits | `data/db.js` (a Play Pro purchase counts as other paid access), `accountDeletion.js` (play_purchases kept, raw payload scrubbed) |

Both routes answer 404 for every method unless `PLAY_BILLING_ENABLED` is exactly `true`.

## Product map (Play product id -> grant)

| Play product id | Grants | Finished with | Web equivalent | Proposed Play price (owner to confirm) |
|---|---|---|---|---|
| `pro_cuet_2027` | Pro until 31 July 2027 (2027-07-31T18:29:59.999Z, read from the web plan) | acknowledge (never consumed) | `pro_cuet_2027`, Rs 99 | **Rs 150 (final, set in Console)** |
| `credits_10_50` | 50 credits | consume | Rs 10 | Rs 15 |
| `credits_29_150` | 150 credits | consume | Rs 29 | Rs 45 |
| `credits_49_300` | 300 credits | consume | Rs 49 | Rs 75 |
| `ai_credits_prepos_10_50`, `_20_150`, `_50_400` | 50 / 150 / 400 credits | consume | the earlier AI top-up packs (Rs 10 / 20 / 50) | not sold: kept accepted for safety only; do not create them in Console |

There is ONE credits balance. Every credit pack lands in the held credits as **bonus credits** through the existing AI credit purchase grant (`mm_ai_grant_bonus_credits`, reason `pack_purchase`, idempotency key `play:<purchase token>`). There are no separate Practice credit products (they were in an earlier draft and are gone). The proposed pack prices are about 1.5x the web, for the owner to confirm. The server never reads a price from a client or from Play: the product id decides the grant.

The three `credits_*` ids and amounts are the website catalogue's (`src/services/credits/creditPacks.mjs`, built on `web/credits-core-1018`; a copy is also in `wt-wallet-web`). That file is not in this branch, so the Play map defines the same ids itself: **the integrator should point `playProducts.js` at that catalogue** (and add a test that the two agree).

**Gaps (not mapped):** `pro_monthly_99` (the web's auto-renewing Razorpay plan: a Play subscription needs `purchases.subscriptionsv2` plus renewal and cancel handling, add it when wanted), `pro_cuet_2027_v2` (not released), `pro_cuet_2026` (legacy). Web credit-pack checkout may be paused by a release gate; a Play purchase is always granted (the money is already taken), so **only activate the credit pack products in Play Console when the web packs are on sale**, and the app should show them only when the credits endpoint says checkout is open.

## How a purchase flows (the contract for the Android app)

1. Before buying, the app sets `BillingFlowParams.setObfuscatedAccountId(hex)` where `hex` = lowercase hex SHA-256 of the signed-in user's id (UTF-8), 64 characters. Test vector: SHA-256 of `abc` is `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`. The server will not grant a purchase that does not carry the caller's hash.
2. After Play reports `PURCHASED`, the app calls `POST /api/billing/play/verify` with its bearer token and `{ productId, purchaseToken, orderId?, obfuscatedExternalAccountId?, packageName? }`. Nothing else is read (a price, credit count or plan in the body is ignored).
3. **The app must not acknowledge or consume the purchase itself.** The server does it after the grant (Pro: acknowledge; packs: consume). On app start the app should call `queryPurchasesAsync` and send any unfinished purchase to verify (replay-safe), so a crash after paying is healed.
4. Answers: `200 { ok, idempotent, productId, kind, finished, pro:{isPremium,premiumUntil,duplicate} | credits:{granted,balance} }`. Errors carry `{ ok:false, error, code }`: 400 `unknown_product`, `bad_token`, `wrong_package`, `order_mismatch`; 401; 403 `account_mismatch`; 404 `purchase_not_found`; 409 `purchase_already_used`, `purchase_voided`, `purchase_canceled`, `product_mismatch`, `unsupported_quantity`, `product_expired`; 202 `purchase_pending` (wait, do not retry in a loop); 429; 503 `play_unavailable`, `grant_unavailable`, `play_not_configured` (safe to retry, nothing was granted). `finished:false` means the grant stands and Google's acknowledge/consume failed; calling verify again finishes it.
5. A purchase that is never verified is refunded by Google after 3 days (unacknowledged); that is the safety net for a purchase the server refused (wrong account, wrong quantity).
6. Keep "multi-quantity purchases" off in Play Console (quantity other than 1 is refused).

## Rules enforced

- Google decides: `purchases.products.get` must say purchaseState 0 (pending answers 202, cancelled 409), for `PLAY_PACKAGE_NAME` (default `in.mockmob.app`), quantity 1, and `obfuscatedExternalAccountId` equal to the caller's hash.
- Grant and `play_purchases` row are one database transaction (`mm_play_grant_purchase`, security definer, service_role only). Unique on `purchase_token`: a replay returns the same result and grants nothing twice; another account presenting the token gets `purchase_already_used`.
- Pro writes the same user columns as the web one-time verify (`is_premium`, `subscription_status`, `premium_until`, never shortened). A Pro bought on Play by someone already Pro past that date is still recorded and acknowledged and flagged `duplicatePro: true` in `play_purchases.granted`, so the owner can refund it in Play Console. The app should hide the Buy button when `/api/me` says Pro.
- Credit packs use the existing atomic `mm_ai_grant_bonus_credits` (idempotency key `play:<token>`), into the one credits balance.
- RTDN (`/api/billing/play/rtdn?token=...`): a voided purchase (refund, chargeback) revokes: Pro off unless the user has other paid evidence (a captured Razorpay payment or another Play Pro in force, the same rule as the web refund path); credit packs are clawed back down to zero and never below, with the shortfall recorded in `play_purchases.revoked`; a void that arrives before verify leaves a tombstone so a late verify is refused. Test notifications are logged. Each Pub/Sub message is processed once (`webhook_events`, provider `google_play`); a database failure answers 5xx so Pub/Sub retries.
- A Play Pro purchase in force counts as paid access in `getOtherPaidAccess` / `hasOtherPaidSubscriptionEvidence`, so a Razorpay cancel or refund can never switch it off.
- Money-route limit: 15 per 10 minutes per user, persistent, fails closed.

## Environment variables (Vercel, Production)

| Variable | Value |
|---|---|
| `PLAY_BILLING_ENABLED` | `true` only at the last deploy step (anything else = off, both routes 404) |
| `GOOGLE_PLAY_SERVICE_ACCOUNT_JSON` | the service account JSON key (raw, or base64 of it) |
| `PLAY_PACKAGE_NAME` | optional, default `in.mockmob.app` |
| `PLAY_RTDN_TOKEN` | long random string; the same value goes in the push URL. Unset = the endpoint stays closed (401) |
| `PLAY_RTDN_OIDC_AUDIENCE` | optional but recommended: the audience set on the Pub/Sub push subscription (e.g. the full push URL without the query). When set, the Google OIDC token is required too |
| `PLAY_RTDN_OIDC_EMAIL` | optional: the push service account's email, pinned |

## What the owner must do (Play Console and Google Cloud)

1. Play Console: set up the **payments profile** (merchant account) and tax details.
2. Enrol in the **15% service fee tier** (Play Console > Settings > Developer account > Payments profile, "Reduced service fee" / the Play Media Experience Program or the 15% tier for the first USD 1M; whichever your account shows).
3. Create the **in-app products** (Monetize > Products > In-app products) with exactly these ids, as one-time products, multi-quantity off: `pro_cuet_2027` at **Rs 150**; `credits_10_50`, `credits_29_150`, `credits_49_300` at the prices you confirm (proposed Rs 15 / 45 / 75), activated when the web packs are on sale. Do not create the old `ai_credits_prepos_*` ids.
4. Google Cloud: create a **service account** (any project linked to Play Console), enable the "Google Play Android Developer API", create a JSON key. In Play Console > Users and permissions > Invite new users, add the service account email and grant "View financial data" and "Manage orders and subscriptions" for the app. Access can take up to a few hours to apply.
5. Google Cloud Pub/Sub: create a **topic** (e.g. `play-rtdn`), grant `google-play-developer-notifications@system.gserviceaccount.com` the Publisher role on it, create a **push subscription** to `https://www.mockmob.in/api/billing/play/rtdn?token=<PLAY_RTDN_TOKEN>` (optionally enable authentication with a service account and set its audience). In Play Console > Monetize > Monetization setup > Real-time developer notifications, enter the topic name and use "Send test notification"; the endpoint answers 200 and logs "test notification received".
6. Add **licence testers** (Play Console > Settings > License testing) with the Google accounts used for test purchases (they pay nothing).
7. Upload a build to an **Internal testing track** and buy from a tester account before going to production. Check on the first real test purchase that `purchaseState` comes back as `0` (the server refuses a response without it).

## Deploy order

1. Take the production pre-checks (below).
2. Apply migration `20261018190000_play_purchases` on production (backward compatible: nothing reads it until the flag is on; `data/db.js` tolerates the table being absent).
3. Set the env vars on Vercel (flag still off), deploy the code. Both routes answer 404.
4. Send the RTDN test notification once the push subscription exists (it gets 404 until the flag is on; so do this after step 5 or briefly flip the flag on a Preview deploy).
5. Set `PLAY_BILLING_ENABLED=true`, redeploy. Run a licence-tester purchase from the internal track; confirm one `play_purchases` row, Pro on, the purchase acknowledged in Play Console.
6. Ship the app build that sells.

Note: this migration does not touch the `credit_transaction_type` enum or `users.credit_balance` (an earlier draft had Practice packs; dropped under D78). It needs `mm_ai_grant_bonus_credits` (migration 0038, already on production).

## Production checks

Pre (read-only SELECTs only):
```sql
select to_regclass('public.play_purchases') as table_absent_is_null,
       (select count(*) from pg_proc where proname in ('mm_play_grant_purchase','mm_play_revoke_purchase')) as fns_should_be_0,
       (select count(*) from pg_proc where proname='mm_ai_grant_bonus_credits') as ai_grant_fn_should_be_1;
```
Post:
```sql
select relrowsecurity from pg_class where relname='play_purchases';                       -- true
select count(*) from pg_policies where tablename='play_purchases';                        -- 0
select has_table_privilege('anon','public.play_purchases','select'),                      -- false
       has_table_privilege('authenticated','public.play_purchases','select'),             -- false
       has_function_privilege('anon','public.mm_play_grant_purchase(text,text,text,text,text,integer,timestamptz,jsonb)','execute'),   -- false
       has_function_privilege('authenticated','public.mm_play_revoke_purchase(text,text,text,jsonb)','execute'),                      -- false
       has_function_privilege('service_role','public.mm_play_grant_purchase(text,text,text,text,text,integer,timestamptz,jsonb)','execute'); -- true
select count(*) from public.play_purchases;                                               -- 0 before the first test purchase
```

## Staging dry-run (18 Oct 2026, project onwkqxmjqjrhfbjjdydu, rolled back)

The migration was run in a `DO` block that ends in `RAISE EXCEPTION`, so nothing stayed (re-checked: no table, no function, no test users). Results: Pro grant (premium on, until 2027-07-31), replay idempotent, other account `purchase_already_used`; credit pack grant (+50, balance 60), replay no double credit (bonus 50), revoke claws back 50; Pro revoke switches Pro off, second revoke idempotent, late verify of the voided token `purchase_voided`; anon and authenticated cannot execute the functions or read the table, service_role can. The final migration differs from the dry-run text only in a comment (a Practice pack branch that was dry-run on the way was removed under D78). The same flows run on PGlite with the real migrations in the test file.

## Rollback

1. `PLAY_BILLING_ENABLED` unset or not `true` and redeploy (or flip it in Vercel): both routes answer 404 at once. The app then cannot verify; unfinished purchases are refunded by Google after 3 days, and anyone already granted keeps what they got.
2. Code rollback to the previous deploy is safe at any time (the table is unused by old code).
3. DB: `supabase/undo/20261018190000_play_purchases.undo.sql` drops the two functions and the table only if it is empty; with real purchases recorded it keeps the table and says so.
4. To take back a single grant by hand: `select public.mm_play_revoke_purchase('<purchase_token>', 'manual', null, '{}'::jsonb);` (service role).

## Notes and limits

- Not verified against the live Google API (no credentials, no network calls were made): the response shapes follow Google's documented `purchases.products` resource. The internal-track test purchase is the real check, especially that `purchaseState` is present as `0` and `obfuscatedExternalAccountId` comes back.
- RTDN voids are trusted once the push is authenticated (token, plus OIDC when configured); the server does not re-ask Google. Enable the OIDC audience.
- A purchase made before the server hears about it is granted only through verify (RTDN purchased messages are logged, not granted, because only verify can bind a purchase to an account).
- Account deletion keeps `play_purchases` rows (legal/financial), with the stored Google response cut to non-personal fields.
