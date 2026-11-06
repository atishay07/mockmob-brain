# Website sign-in reliability, 13 Oct 2026

Owner feedback (2025-26 students): signing up worked, but students had to log in again and again,
especially with Google and the email code, and the whole account flow felt unreliable.
This pass finds the causes in the website code, fixes them, and lists the dashboard settings
only the owner can change. Branch `feat/app-and-web`. Nothing is committed by this pass.

## Root causes (line numbers are from HEAD before this change)

1. **No session refresh ever ran on the server: the proxy file was in the wrong place.**
   `middleware.js` sat at the repository root (moved there from `src/proxy.js` on 23 Apr 2026,
   commit 063ce7a). The app lives in `src/app`, and Next only compiles a proxy or middleware file
   that sits next to `app` (`src/`). The root file was silently ignored: the last build's
   `.next/server/functions-config-manifest.json` had no `/_middleware` entry and the compiled
   server contained none of its code. Its matcher (`middleware.js:209`) also covered only four paths.
   Consequence: Server Components that read the session (`/pricing`, `/pricing/prepos`, `/admin`
   via `auth()` in `src/lib/auth.ts`) refreshed an expired access token themselves. Server
   Components cannot write cookies, so the write was swallowed (`src/lib/auth.ts:91`). Supabase
   had already rotated the refresh token, the browser kept the spent one, and its next refresh
   was treated as token reuse: Supabase revoked the session and the student was signed out.
   This is the failure the @supabase/ssr proxy pattern exists to prevent.

2. **Every tab focus and every hourly token refresh reloaded the whole app.**
   `src/components/AuthProvider.jsx:194-208`: `onAuthStateChange` called
   `refreshSession({ silent: false })` for every event. supabase-js emits `SIGNED_IN` whenever a
   tab becomes visible again and `TOKEN_REFRESHED` about every hour. Each one set the status to
   `loading`, which made `src/app/(app)/AppLayoutClient.jsx:160` replace the whole app (a test in
   progress included) with "Loading your session...". If the follow-up `/api/auth/me` failed at
   that moment, the status became `unauthenticated` and line 92 sent the student to **/signup**.
   On a phone this happened every time a student switched to the mail app to read the code.

3. **Transient failures were treated as "signed out".**
   - `AuthProvider.jsx:15`: a 2.5 s timeout on `getSession()`. When the token needs a refresh on
     a slow mobile connection, the timeout threw and the student was marked unauthenticated.
   - `src/lib/auth.ts:101` and `:141`: any `getUser()` error (Supabase unreachable, 5xx, rate
     limit) returned null, so `/api/auth/me` answered **401** (`route.js:37`), which the web and the
     Android app read as "signed out".
   - `AuthProvider.jsx:160-161`: any `AuthApiError` triggered `supabase.auth.signOut()`.

4. **Sign-out was global.** `AuthProvider.jsx:161` and `:268` called `signOut()` with the default
   scope, which is `global`: it revokes every session of that account. Signing out on one laptop,
   or the error path above, signed the student out of every other device (and will sign them out
   of the Android app).

5. **Returning students were sent to Sign up, and lost their place.** `AppLayoutClient.jsx:92`
   redirected to `/signup`; the callback (`AuthCallbackPageClient.jsx:123`) and the login page
   always went to `/dashboard`.

6. **Email code flow rough edges.** No resend control and no way to change the email after a
   code was sent (`SignupCard.jsx`); a 429 said only "Please wait" with no time; raw Supabase
   errors ("Token has expired or is invalid") were shown; the email always said "8-digit" even
   though the length is a dashboard setting. The callback displayed `error_description` from the
   URL verbatim (`AuthCallbackPageClient.jsx:62`), which an attacker can craft.

7. **Google inside in-app browsers.** Students opening MockMob from Instagram or WhatsApp land in
   an embedded browser, where Google refuses OAuth. Nothing told them to switch browser or use the
   email code.

8. **Dead NextAuth code.** `src/lib/auth.ts:18-75` built a next-auth handler (Google provider,
   JWT sessions, its own user creation) exposed at `/api/auth/[...nextauth]`. Nothing used it,
   but with `GOOGLE_CLIENT_ID/SECRET` set it was a second, unmonitored way to create accounts.

## Fixes

| Area | Change |
| --- | --- |
| Session refresh | New `src/proxy.js` (Next 16 Proxy, Node runtime) calling `refreshSupabaseSession` in `src/lib/server/sessionProxy.js`: the documented @supabase/ssr pattern (`getAll` / `setAll` writing to the request and the response, `NextResponse.next({ request })`, the library's no-store headers, nothing between `createServerClient` and `getClaims()`). Anonymous visitors (no `sb-*-auth-token` cookie) skip Supabase entirely. A 5 s budget stops a hung Supabase call from stalling pages; transient failures leave cookies untouched. Never redirects. Matcher skips `/api/`, `_next`, `.well-known`, `sw.js`, metadata files and static assets. Build output now lists "Proxy (Middleware)". Root `middleware.js` deleted; its referral-cookie capture on `/pricing` moved into the proxy. |
| Server reads | `src/lib/auth.ts`: next-auth removed; new `authWithStatus(request)` returns `{ session, transient }`; `auth()` unchanged for the 60+ callers. Cookie reads keep `getUser()` (authoritative: a deleted or banned account is refused at once, which matters because a valid identity can create the MockMob user row). Bearer reads (Android app) unchanged apart from error classification. |
| `/api/auth/me` | Answers **503** with `Retry-After: 2` on a transient auth failure instead of 401. The web and the Android app (`auth_me_loader.dart` retries 503) keep the student signed in. |
| Browser state | `AuthProvider.jsx`: ignores `INITIAL_SESSION`, and `SIGNED_IN`/`TOKEN_REFRESHED` for the same signed-in student; never swaps a loaded app for the loading screen; new `unavailable` status ("You are still signed in... Try again", retried on `online` and tab focus) instead of signing out; one forced refresh-and-retry before believing a 401; local-only sign-out (`scope: 'local'`) everywhere; dead refresh tokens (`isDeadSessionError`) are the only automatic sign-out. Shared rules in `src/lib/supabase-auth-errors.js`. |
| Return path | `src/lib/auth-redirect.js`: the gate sends to `/login?next=<page>`; the page is stored in localStorage for 30 minutes and re-validated on read (same-site path only; no `//`, backslashes, control characters, schemes, or auth/API pages). The OAuth redirect URL stays exactly `/auth/callback`, so the Supabase allow list can stay exact. |
| Callback | `src/lib/auth-callback.js` + `AuthCallbackPageClient.jsx`: accepts only a PKCE `code` (UUID shape) or `token_hash` with an allow-listed type (`email`, `magiclink`, `signup`, `invite`, `email_change`; no `recovery`); shows fixed copy per error code, never URL text; removes the code from the address bar before any network call; runs once per page load (safe under React Strict Mode); explains the "different browser" PKCE failure; honours onboarding, then the saved page. |
| Google | `flowType: 'pkce'` is now explicit in `src/lib/supabase-browser.js`. In-app browsers get a notice to open Chrome or use the email code. |
| Email code | `SignupCard.jsx`: "Send a new code" with a countdown that follows the server's `retryAfterSeconds`, "Use a different email", focus moves to the code field, 6-10 digits accepted, clear messages for wrong/expired code, rate limit and offline. Verification tries type `email` first (covers both new-account and existing-account codes) then `magiclink`, and stops on network errors. `/api/auth/email-login` returns `{ code: 'rate_limited', retryAfterSeconds }` with a `Retry-After` header (contract unchanged for the app: still 429), and the email names the real code length. |

## Auth review fixes (same day)

An independent review of this pass (13 Oct 2026) found one confirmed sign-out bug and one
plausible takeover path. Applied:

| Finding | Change |
| --- | --- |
| H1: a Supabase 429 or 500 on a token refresh still deleted the session. `@supabase/auth-js` 2.104 only keeps the session for network errors, 502-504 and 52x; on anything else it removes it and emits SIGNED_OUT before our rules run. Production refreshes from Vercel, so all students share a few outgoing addresses and Supabase's per-address "Token refreshes" limit. | `createAuthSafeFetch` in `src/lib/supabase-auth-errors.js` turns a 429 or 5xx answer to a **refresh-token grant only** into a 503 (other grants and `/verify` keep their real status, so "too many tries" still shows). Passed as `global.fetch` to the proxy client (`sessionProxy.js`, merged with test options), the server client (`src/lib/server/cookieSession.js`, used by `auth.ts`) and the browser client (`supabase-browser.js`). Second guard: the proxy and server reads now hold cookie writes until the outcome is known; new tokens are always written, deletions only when Supabase definitively ended the session (`mayWriteAuthCookies`). |
| H2: anyone can call Supabase's public sign-up with a student's email and a password. | `authWithStatus` refuses identities without `email_confirmed_at` (not `confirmed_at`: a confirmed phone would set that) and looks the MockMob user up by Supabase id first, then email. Migration `supabase/migrations/20261013150000_auth_unconfirmed_passwords.sql`: service-role-only `auth_clear_unconfirmed_password(email)` (called by `/api/auth/email-login` before `generateLink`) and a trigger that removes any password in the same update that first confirms the email, which closes the window between sending the code and entering it. Owner: "Confirm email" ON. |
| M1: the email-code route limited per email only. | Three persistent limits (`src/lib/server/emailLoginPolicy.js`): per address 20/hour, per address and email 5/hour, per email from any address 15/hour. Owner: `PERSISTENT_LIMITS_ENABLED=true` on Vercel. Turnstile after three requests from one address is a later step. |
| M2: the email link was spent on page load (mail scanners use it up, together with the code in the same email; a link someone else sent signed this browser into their account). | `AuthCallbackPageClient.jsx` reads and clears the link, then asks: "Continue to MockMob", or, when already signed in, "You're signed in as ... Switch to the account in this email?" with "Stay signed in". `verifyOtp` runs only on the tap. Owner: Resend click tracking off. |
| M3: no way to end other sessions. | "Sign out of other devices" on the web account page (`/profile`, `SignOutOtherDevicesSection`, `signOut({ scope: 'others' })` via `AuthProvider.signOutOtherDevices`) and in the app (`SignOutOtherDevicesCard`); the app's Forgot password ends other sessions after the new password is saved. Owner: "Secure password change" ON. |
| M4: after a proxy timeout or transient failure, `auth()` in Server Components (`/pricing`, `/pricing/prepos`, `/admin`) could still spend the refresh token without being able to save it. | The proxy always strips an incoming `x-mm-auth-stale` header and sets it on the forwarded request after a `transient` or `timeout` outcome; `readCookieUser` then answers "transient" without calling Supabase. Server reads also have a 5 s budget (the library retries a failed refresh for up to 30 s), so `/api/auth/me` answers 503 in time. |
| L3: the email link fell back to the request's own origin. | In production the link origin is `NEXT_PUBLIC_SITE_URL` only if it is `https://www.mockmob.in` or `https://mockmob.in`, else `https://www.mockmob.in`. |
| L5: two first logins at once could collide on the users insert. | `ensureDbUser` catches the unique violation (23505) and reads the winner's row. |
| L7: every signed-in page view calls Supabase while the project uses the shared JWT secret. | Dashboard step 3 is now **recommended**. The proxy matcher deliberately still runs on prefetches: skipping them would let a prefetched Server Component refresh without the stale guard. |
| L8: the email's button opens the website even on a phone with the app. | The email says "Using the MockMob app? Type this code in the app." |
| L9: leftover NextAuth. | `next-auth` uninstalled (`package.json`, `package-lock.json`). |
| L1, L4 | Reuse interval 30 s on both projects (app doc corrected); localhost removed from the production redirect list (step 4). |

## Verification (actual)

- After the review fixes: `npm run test:auth` passes in full (see the final report for counts),
  including 429 and 500 cases for the proxy, the `/api/auth/me` read path and the real
  `@supabase/ssr` browser client (no SIGNED_OUT, cookie kept), a control test proving the
  unwrapped library does sign out on a 429, held cookie writes, the stale marker, the
  confirmed-email rule, the first-login race, the email-login policy and the tap-to-continue
  callback.
- First pass: `npm run test:auth` (new script): 33 pass. New `data/tests/auth_reliability.test.mjs` drives the real
  `@supabase/ssr` server client and a real `NextRequest` against a fake Supabase Auth server:
  expired token refreshed with new cookies on both request and response (long-lived Max-Age,
  no-store header); valid session untouched; network failure and 503 keep cookies; revoked refresh
  token clears them; hung call cut off; anonymous requests never reach Supabase; matcher run/skip
  lists; no next-auth imports; open-redirect cases; callback parsing; error classification.
- `npm run test:recovery` 39 pass; `npm run test:learning` 91 pass; payment, account deletion and
  UI state suites 28 pass. (There is no `npm test` script in this repo.)
- `npx next build` succeeds (Turbopack), output lists `ƒ Proxy (Middleware)`;
  `functions-config-manifest.json` now has `/_middleware`. ESLint clean on every changed file.
- Local staging app (`http://localhost:3101`, dev server already running from this checkout):
  a request carrying a bogus expired session cookie came back with `Set-Cookie: ...; Max-Age=0`,
  proving the proxy runs and clears a dead session; `/review?tab=mistakes` while signed out went
  to `/login?next=%2Freview%3Ftab%3Dmistakes` and stored the path; the code step showed the
  countdown and change-email control; a wrong code showed the new message; two quick code
  requests gave 200 then 429 `Retry-After: 60`; callback error, invalid-type and empty cases
  showed fixed copy and a clean URL; 375 px width has no horizontal scroll.
- Not exercised: a completed Google sign-in or a real inbox code (agents must not complete
  sign-in through a hosted identity provider); a session surviving past the 1-hour token expiry
  on production. Check both on the owner's phone after deploy.

## Residual risks

- If Supabase answers slower than 5 s in the proxy, the page renders without a refreshed cookie
  and server reads in that request are marked stale (they do not refresh). The library may still
  finish the refresh in the background and its new token is then lost; the browser refreshes
  within seconds, inside the 30 s reuse interval, so this does not sign anyone out.
- During a Supabase 429 the library retries a refresh with backoff for up to 30 s. Students keep
  their session but may see "unavailable" until the limit resets; raise the limit (step 5b).
- With the legacy shared JWT secret, `getClaims()` in the proxy falls back to a network
  `getUser()` call on each signed-in page view (about 100-300 ms). Asymmetric signing keys make it
  local (dashboard step 3).
- The persistent email rate limiter (`src/lib/server/rateLimit.js:13`) fails closed: if its
  database RPC errors, every code request returns 429. Kept on purpose (stops email bombing);
  watch for 429 spikes in logs.
- Sign-out is local to the device; "Sign out of other devices" on the account page ends the rest.
- The unconfirmed-password migration is saved, not applied. Until it is, the email-login route
  logs `clearing an unconfirmed password failed` once per request and carries on.
- Protected pages are still gated in the browser (`AppLayoutClient`), as before; the proxy only
  refreshes. Server routes and Server Functions must keep checking `auth()` themselves.

## Owner dashboard steps

Production project ref starts with `isrx` (staging is `onwkqxmjqjrhfbjjdydu`). Do 1, 2, 4, 5 and
9 on both projects (staging first).

1. **Supabase > Authentication > Sessions** (Sessions settings)
   - Detect and revoke potentially compromised refresh tokens: **On** (keep).
   - Refresh token reuse interval: **30** seconds (default 10), on both projects. The proxy, the
     browser and the app can refresh at nearly the same moment on slow phone networks.
   - Enforce single session per user: **Off** (on would sign the website out whenever the app signs in).
   - Time-box user sessions: **0 / never**. Inactivity timeout: **0 / never**.
2. **Access token (JWT) expiry**: keep **3600** seconds. In the current dashboard it is under
   Project Settings > JWT Keys (older dashboards: Project Settings > API > JWT Settings > JWT expiry
   limit). Do not set it below 600.
3. **Recommended: asymmetric signing keys.** Project Settings > JWT Keys > "Migrate JWT
   secret", then create a standby **ECC (P-256)** key and click "Rotate keys". The repo has no code
   that verifies tokens with the legacy secret (searched for `JWT_SECRET`, `jwtVerify`,
   `jsonwebtoken`), and tokens already issued stay valid. This makes the proxy's check local
   instead of one Supabase call per signed-in page view and link prefetch.
4. **Supabase > Authentication > URL Configuration**
   - Site URL: `https://www.mockmob.in`
   - Redirect URLs on **production** (exact, one per line):
     - `https://www.mockmob.in/auth/callback`
     - `https://mockmob.in/auth/callback`
     - `in.mockmob.app://login-callback`
   - Remove `http://localhost:3000/auth/callback` from production if it is there.
   - Redirect URLs on **staging** only: the three above plus `http://localhost:3000/auth/callback`
     and `http://localhost:3101/auth/callback`.
   - Remove any broad wildcard such as `https://*.vercel.app/**` unless previews need it.
5. **Supabase > Authentication > Sign In / Providers**
   a. **Email**: Enabled. **Confirm email: ON** (stops a stranger signing up with a student's
      email and a password). **Secure password change: ON** (a stolen session cannot set a
      password; the app already explains the extra code step). Minimum password length **8**.
      Email OTP length **8** (the web, the email and the app all expect 8 today); Email OTP
      expiration **3600** seconds.
   b. **Rate Limits** (Authentication > Rate Limits): raise "Token refreshes" well above the
      default, for example **1800 per 5 minutes**, and "Sign-ups and sign-ins" to about **300 per
      5 minutes**. Website refreshes come from a few Vercel addresses shared by every student.
   c. **Google**: Enabled. Client IDs: the **Web** OAuth client ID first, then the Android client
      ID(s), comma-separated (the app's native Google sign-in sends ID tokens for these). Client
      Secret: the Web client's secret. Leave "Skip nonce checks" off.
6. **Google Cloud Console > APIs & Services > Credentials > OAuth 2.0 Client IDs > Web client**
   - Authorized JavaScript origins: `https://www.mockmob.in`, `https://mockmob.in`
   - Authorized redirect URIs: `https://<production-project-ref>.supabase.co/auth/v1/callback`
     (and the staging one on its own client). This is Supabase's callback, not the site's.
7. **Google Cloud Console > Google Auth Platform (OAuth consent screen)**: Publishing status
   **In production** (in Testing only listed test users can sign in). Branding: app name MockMob,
   support email, authorised domain `mockmob.in`, home `https://www.mockmob.in`, privacy
   `https://www.mockmob.in/privacy`, terms `https://www.mockmob.in/terms`. Scopes: `openid`,
   `email`, `profile` only (many students are 17; keep data to the minimum).
8. **Vercel > Project > Settings > Environment Variables (Production)**
   - `NEXT_PUBLIC_SITE_URL=https://www.mockmob.in` (the login email's link uses it; any other
     value now falls back to `https://www.mockmob.in` in production).
   - `PERSISTENT_LIMITS_ENABLED=true` (without it the email-code limits are per server instance
     and barely limit anything).
   - Delete `NEXTAUTH_URL`, `AUTH_SECRET`, `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` (no
     code in this repo reads them now). **`NEXTAUTH_SECRET` is still read** by
     `src/app/api/coming-soon/unlock/route.js` as a fallback when `COMING_SOON_COOKIE_SECRET` is
     unset, and after that it falls back to a fixed public string. Set
     `COMING_SOON_COOKIE_SECRET` to a new random value first (for example the output of
     `openssl rand -base64 32`), then delete `NEXTAUTH_SECRET`.
   - Redeploy after changing any of these.
9. **Supabase > SQL** (or `supabase db push`): apply
   `supabase/migrations/20261013150000_auth_unconfirmed_passwords.sql`, staging first. Then on
   staging: sign up through the Auth API with a password for a new test email, complete the code
   sign-in on the website, and check that the password no longer works; repeat with Google on
   another test email. If Supabase refuses the trigger on `auth.users`, apply the function part
   alone and report it.
10. **Resend > Domains > mockmob.in**: turn **Click tracking off** (and open tracking off). With it
    on, the one-time login token passes through Resend's link redirector.

## Phone or password login (owner asked)

Update the same day: the Android app now has password sign-in (after a code or Google sign-in)
and a phone flow that is built but switched off; see `flutter_app/docs/AUTH.md`. Before phone is
ever switched on, add Turnstile, a "Before User Created" hook that rejects users without an
email, a "Send SMS" hook that allows only +91 numbers, and a low SMS rate limit (app doc, steps
P1-P4). Many CUET students are 17: keep phone off, Google scopes minimal, tokens and emails out
of analytics, and plan one age and guardian-consent checkbox at sign-up before the DPDP Rules'
obligations start (about mid-2027). This is not legal advice.

The original assessment from the first pass:


Not added in this pass. The repeated logins came from the session bugs above, not from the sign-in
methods. Phone OTP in India needs an SMS provider with DLT registration (sender ID and template
approval) and costs per message; worth it only if email codes still fail after this fix.
Passwords add reset emails and leaked-password risk for a student audience; Supabase supports
them if wanted later. Revisit after a week of production data on `/api/auth/me` 401 and 503 rates.
