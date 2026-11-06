# Landing funnel: integration note and runbook (15 Oct 2026, Q10)

Branch web/q11-1015. Not pushed, not deployed, migration NOT applied to production.

## What exists

| Piece | File |
| --- | --- |
| Table `funnel_daily(day, step, platform, count)` and atomic `funnel_increment(p_step, p_platform)` | `supabase/migrations/20261015233000_funnel_daily.sql` |
| Undo (outside migrations, the CLI never applies it) | `supabase/undo/20261015233000_funnel_daily.undo.sql` |
| `POST /api/funnel` | `src/app/api/funnel/route.js` |
| Rules (whitelist, bots, origin, kill switch, summary maths) | `src/lib/server/funnel.js`, `src/lib/funnelSteps.js` |
| Database access | `src/lib/server/funnelStore.js` |
| Client helper | `src/lib/funnel.js` |
| Admin summary, last 14 days | `/admin/funnel` (`src/app/admin/funnel/page.jsx`, `src/components/admin/FunnelSummary.jsx`), linked from the admin header |
| Tests | `data/tests/funnel.test.mjs` |

## Privacy, as built

- Stored: a day (India calendar day, set by the database), one of seven step names, one of five platform categories, a count. Nothing else.
- Platform (added 15 Oct, Q11): derived on the server from the User-Agent at request time into `desktop`, `android_web`, `ios_web` (iPhone and iPad), `android_app` (a MockMob token, Dart or okhttp as the first token) or `other`. Only the category is kept; the User-Agent is read, mapped and dropped. The category never comes from the request body.
- Not stored, not logged, not read: cookies, user id, session id, IP, user agent. The IP feeds only the in-memory rate limit (40 a minute); the persistent limiter is deliberately not used because it writes a hashed IP to the database. The user agent is read once for the bot check, then dropped. Only a database error code is ever logged.
- Ignored: obvious bots and scripts, an empty or very short user agent, requests that are not same-origin, bodies over 200 characters, any step not on the whitelist, and visitors who send Do Not Track or Global Privacy Control (the client helper also skips them).
- Every outcome except a rate limit answers an empty 204, so the filter cannot be probed.
- Kill switch: counting runs only when `FUNNEL_ENABLED` is exactly `true`. Unset or anything else means off, and the route answers 204 before doing any work.

## Client helper

```js
import { trackFunnel } from '@/lib/funnel';
trackFunnel('sample_started'); // returns true if sent; once per step per page load; never throws
```

It sends `navigator.sendBeacon('/api/funnel', {"step": "..."})`. Call it from a client component, from an event handler or a `useEffect`. A server render is a safe no-op.

## Where each step should be called (landing components are not edited here)

The landing is being rebuilt, so anchor on the behaviour. Today's code is named so the builder can find it.

1. `landing_view`: once when the landing page mounts, a `useEffect(() => { trackFunnel('landing_view'); }, [])` in a client component rendered by `src/app/page.js` (for example a tiny `FunnelLandingView` sibling of `HeroDockGate`). Do not put it in `NavBar` or the layout, which would count every route.
2. `sample_subject_chosen`: in the click handler of the sample's subject choice. In the rebuilt sample this is the control that picks the subject. In the current page the subject cards in `src/components/landing/SubjectGrid.jsx` are links to `/cuet/[slug]` (a navigation, not a sample), so only count them if the owner treats that as the sample choice; otherwise it belongs on the rebuilt sample's chooser.
3. `sample_started`: when the first sample question is shown or answered. In today's `src/components/landing/DemoDrill.jsx` that is the first call of `pick(...)` (where `setPicked` runs), guarded by the helper's once-per-load rule.
4. `sample_done`: when the sample's result screen appears. In `DemoDrill.jsx` that is the `setDone(true)` line inside `next(...)`. A replay (`restart`) does not count again in the same page load.
5. `signup_click`: on every sign-up link or button the visitor can press on the landing, in its `onClick` (the beacon survives the navigation): `LandingActions.jsx` (both buttons, whichever points at `signupHref`), `CloseActions.jsx` ("Sign up free", and the dock's sign-up link further down that file), `DemoDrill.jsx` result link (`<Link href="/signup">`), `FooterStart.jsx` ("Sign up free"), `NavBar.jsx` (desktop `mm-nav__cta` and the mobile menu entry), and `src/app/page.js` ("Start free", near line 372). Count only when the visitor is signed out (`!isAuthenticated`).
6. `signup_complete`: NOT a client call (the beacon refuses it). The server counts it, once, where the account row is first created: `ensureDbUser` in `src/lib/server/cookieSession.js` runs an optional `onCreated` hook only for the request whose insert created the row (not for the loser of a first-login race, not for a returning student or an older row found by email). `src/lib/auth.ts` passes a hook that calls `countSignup(headers)` in `funnelStore.js`, which counts under the platform of that request (the Android app's bearer requests included). The definition is therefore "account created for a confirmed email", earlier than finishing onboarding. It honours the kill switch and Do Not Track / Global Privacy Control, never throws, and never changes the sign-in result.
7. `login_click`: the log in links: `NavBar.jsx` (the `mm-nav__login` link and the mobile menu link at line 181) and `FooterStart.jsx` ("Log in"). Signed-out visitors only.

The admin page also shows a By platform section: each platform's share of landing views and of finished sign ups (always with its numerator and the all-platform denominator, small samples flagged) and the 14-day funnel per platform. The Android app does not open the landing page, so it shows sign ups only. A sign up is counted on the device that made the account, which can differ from the platform of the landing view that led to it.

Because each beacon is a separate daily total, the admin page compares totals, not the same people. It says so on the page and flags rates over 100% and rates on fewer than 30.

## Production steps (the orchestrator or owner, in order)

1. Review the migration. Nothing was run against production. Staging (onwkqxmjqjrhfbjjdydu) was dry run on 15 Oct, and again after the platform column was added (the earlier staging copy was removed first, then the new file applied): applied, RLS on, anon and authenticated have no table or function access, service_role does; two increments for the same platform gave 2 and another platform got its own row, an unknown step and an unknown platform each raised a check violation, a rolled-back test left 0 rows; the undo (which also drops the old one-argument function) dropped the function and table; the migration was then put back on staging.
2. Apply `supabase/migrations/20261015233000_funnel_daily.sql` to production (isrxrxzjocewrdureyhp), for example with the Supabase MCP `apply_migration`. The file already contains the platform column; production has no earlier copy, so apply it once, as is.
3. Verify on production:
   ```sql
   select to_regclass('public.funnel_daily') is not null as table_ok,
          (select relrowsecurity from pg_class where oid = 'public.funnel_daily'::regclass) as rls,
          has_table_privilege('anon', 'public.funnel_daily', 'select') as anon_select,       -- expect false
          has_function_privilege('anon', 'public.funnel_increment(text, text)', 'execute') as anon_exec, -- expect false
          has_function_privilege('service_role', 'public.funnel_increment(text, text)', 'execute') as service_exec, -- expect true
          (select string_agg(column_name, ',' order by ordinal_position) from information_schema.columns where table_schema = 'public' and table_name = 'funnel_daily') as cols; -- expect day,step,platform,count
   ```
4. Deploy this branch. The route answers 204 and counts nothing until the flag is set.
5. Set `FUNNEL_ENABLED=true` in Vercel (production), redeploy, then send one beacon (open the landing once with the helper wired in) and check `select * from public.funnel_daily;` shows a row for today with the right platform. A new sign up adds a `signup_complete` row. Open `/admin/funnel` as the admin to see it.
6. Kill switch: set `FUNNEL_ENABLED` to anything but `true` and redeploy. Full removal: run `supabase/undo/20261015233000_funnel_daily.undo.sql`; the route then still answers 204 and the admin page shows that the table does not exist.

Until the landing agent wires the calls in (section above), `/admin/funnel` shows "Nothing counted".
