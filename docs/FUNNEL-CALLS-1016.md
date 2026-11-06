# Funnel calls (16 Oct 2026, branch web/funnel-calls-1016)

Not pushed, not deployed. Migration 20261016120100 (renamed from 20261016120000 to keep timestamps unique) is NOT applied to production; it was applied to STAGING (onwkqxmjqjrhfbjjdydu) and probed in a rolled-back transaction (first call true, second false, count 1, anon cannot execute, service_role can). Builds on `FUNNEL-INTEGRATION-2026-10-15.md`.

## What now calls the funnel (server side)

| Step | Where | Notes |
| --- | --- | --- |
| `signup_complete` | `ensureDbUser` onCreated (already there) | unchanged |
| `first_practice_started` | `src/app/api/sessions/route.js`, POST, after the start succeeds | not a resume (`sessionId`), not the delayed check (`episodeId`) |
| `first_practice_finished` | same file, PATCH finish (also reached by `/api/attempts` POST) | delayed checks excluded |
| `first_mock_finished` | same finish, when the attempt's mode is `full` or `nta` | both steps are claimed on a first mock |
| `first_repair` | `src/app/api/recovery/repair/route.js`, status `explained` or `stored` | not for refusals or held repairs |
| `pricing_viewed` | `src/app/pricing/page.js`, signed-in students only | signed-out visitors are not counted (no person to count once) |
| `checkout_opened` | `create-subscription` (one-time, also `create-order`) and `create-monthly-subscription`, after the order or subscription exists | |
| `payment_captured` | `verify-payment` (both kinds) and `webhook` (one-time order, subscription charge) | first captured Pro payment; renewals do not count again. A webhook is Razorpay's request, so if it lands before the student's verify call it counts under platform `other` |

App versus web is the existing platform column: the server reads the User-Agent of the request (Android app token, Dart or okhttp = `android_app`; browsers = `android_web`, `ios_web`, `desktop`) and keeps only that category. Nothing new is read.

## How it works

- `countStepOnce(userId, steps, headers)` in `src/lib/server/funnelOnceStore.js`. Fire and forget: returns nothing, is never awaited, runs through `after()` (falls back to running directly), swallows every error, logs only a database error code. It does nothing unless `FUNNEL_ENABLED` is exactly `true`, and nothing for Do Not Track or Global Privacy Control.
- Once per person: `funnel_count_once(user_id, step, platform)` sets the step in `users.funnel_seen` (the person's own row) and, only if it was not set, adds 1 to `funnel_daily`, in one transaction. `funnel_daily` still has only day, step, platform, count. The id never reaches `funnelStore.js` or the landing route; the privacy test still bans ids there.
- The browser beacon refuses all seven new steps (server only).
- Admin `/admin/funnel` gains an "After sign up" section: each step against finished sign ups.
- Flags are only set while `FUNNEL_ENABLED=true`, so turning it on later counts everyone from that day. Existing students will reach "first" steps once after enabling, so the first days read high against sign ups (the page says rates can pass 100%). Optional, not run: to avoid that, the owner can pre-flag existing users before enabling, for example `update users set funnel_seen = array['first_practice_started','first_practice_finished'] where id in (select distinct user_id from attempts);` and similar for the other steps. Decide before applying; it edits production data.

## Production steps

1. Review and apply `supabase/migrations/20261016120100_funnel_product_steps.sql` to production (after `20261015233000_funnel_daily.sql`). Undo: `supabase/undo/20261016120100_funnel_product_steps.undo.sql`.
2. Verify: `select has_function_privilege('anon','public.funnel_count_once(text,text,text)','execute')` is false, service_role true, `users.funnel_seen` exists.
3. Deploy, then set `FUNNEL_ENABLED=true`.
4. Until the migration is applied, calls fail quietly (one warning code per call) and nothing else changes.

## Lines for the landing (not applied here; src/app/page.js and landing components are on another branch)

The landing needs none of the new steps. Its calls are the ones in `FUNNEL-INTEGRATION-2026-10-15.md`. Exact lines, unchanged:

```js
import { trackFunnel } from '@/lib/funnel';
// in a client component rendered by src/app/page.js, once on mount:
useEffect(() => { trackFunnel('landing_view'); }, []);
// sample subject chooser click:          trackFunnel('sample_subject_chosen');
// first sample question shown/answered:   trackFunnel('sample_started');
// sample result screen appears:           trackFunnel('sample_done');
// onClick of every signed-out sign-up link/button (hero, close, dock, footer, nav, mobile menu):
//                                         trackFunnel('signup_click');
// onClick of every log-in link (nav, mobile menu, footer), signed-out only:
//                                         trackFunnel('login_click');
```

`pricing_viewed` must not be added to the landing or to a Pricing link: it is counted on the server when a signed-in student opens `/pricing`. `trackFunnel('first_repair')` and the other new names are refused by the route on purpose.

## Checks run

`node --test data/tests/funnel.test.mjs data/tests/funnel_calls.test.mjs` (25 pass, includes PGlite migration and undo), `npm run test:billing` (87), `test:auth` (52), `test:app` (335), `test:learning` (302), `test:recovery` (306), eslint on changed files clean. One bug found by the billing suite and fixed: the verify-payment helpers had no `request` in scope, now `requestHeaders` is passed in.
