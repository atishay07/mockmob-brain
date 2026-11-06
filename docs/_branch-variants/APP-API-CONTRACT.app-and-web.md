# MockMob App API Contract (Flutter Android client)

Status: authoritative for the `in.mockmob.app` client as of 2026-10-12. Derived from reading `mockmob-next` at commit `5fac96f` ("App backend foundations: bearer access, consent-gated usage data, prefs, rhythm, deletion"). Nothing here was exercised against production. Live env flag values are UNVERIFIED and marked as such.

Update 15 Oct 2026: sections 2.8 and 2.9 gain two additive contracts from the Mistake Repair v3 and post-mock SWOT build: the repair v3 payload with `pattern` (under `POST /api/recovery/repair`), and `mistakeInsights` and `swot` on `GET /api/attempts/[id]`. Both are additive; an older app that ignores them keeps working. They follow the build spec `mockmob-next/tmp/repair-v3/SPEC.md` (sections A, B, C.1, C.2) and should be reconciled with the shipped server at integration.

Citations are `file:line` relative to the `mockmob-next` root. "Verified" means I re-read the source while composing this; other facts come from the reader notes and carry their original citations.

Corrections made while composing (earlier reader notes were written against an older tree):
- `/api/learning/summary`, `/api/bookmarks`, `/api/ai/credits`, `/api/ai/usage`, `/api/ai/mentor/history`, `/api/questions/{feed,explore,[id]/vote,[id]/interact,pending}` and `GET/PATCH /api/users/[id]` now call `auth(request)` and accept Bearer (`src/app/api/learning/summary/route.js:85`, `bookmarks/route.js:22,77`, `ai/credits/route.js:21`, `users/[id]/route.js:7,26`; commit message of `5fac96f`).
- `GET /api/users/[id]` is now owner-only (`users/[id]/route.js:7-11`). It no longer leaks other users.
- `PATCH /api/users/[id]` still passes the raw body to `Database.updateUser`, which accepts `role`, `subscriptionStatus`, `isPremium`, `premiumUntil`, `email` (`users/[id]/route.js:33`, `data/db.js:346-356`). A signed-in user can still self-grant Pro. The app must NOT use it (use `/api/me/*` and the gap list in section 7).
- New first-party app routes exist: `/api/me/{consent,notification-prefs,devices,goal,rhythm,delete}`, `/api/events`, `/.well-known/assetlinks.json`.

---

## 1. Base URL, hosts, auth, errors, rate limits

### 1.1 Base URL and hosts
- Production base: `https://www.mockmob.in`. The apex redirects to `www` at the Vercel domain layer. The repo explicitly forbids adding a www-to-apex redirect (`next.config.mjs:27-29`, "production outage, 4 Oct 2026"). Use `www` directly so no redirect is followed. A client that sends `Authorization` across a redirect may lose the header, so never rely on following the apex redirect.
- The existing Capacitor pilot used `https://mockmob.in` (`mobile/.env.example:1`). Do not copy it.
- Android App Links: `/.well-known/assetlinks.json` is rewritten to `/api/assetlinks` (`next.config.mjs:38`). It lists package `in.mockmob.app` with fingerprints from env `ANDROID_CERT_SHA256`. If the env is empty it returns `[]`, so App Links will not verify until the owner sets the release (and Play App Signing) SHA-256 fingerprints. Verified `src/app/api/assetlinks/route.js`.
- All JSON, `Content-Type: application/json`. Native HTTP sends no `Origin`, so CORS is irrelevant. CORS exists only for Capacitor origins on `/api/sessions` and `/api/mobile/*` (`src/lib/server/mobileCors.js`).

### 1.2 Authentication
The server accepts any valid Supabase access JWT as a Bearer token. Nothing is Capacitor-specific.
- Header: `Authorization: Bearer <supabase access_token>`. If an `Authorization` header exists but does not start with `Bearer `, the user is null and the route returns 401 (`src/lib/auth.ts:125-133`). Validation: `supabaseAdmin().auth.getUser(token)`.
- With no header, auth falls back to Supabase cookies (`auth.ts:134`). A native client always sends Bearer.
- The Supabase user must have an email. Phone-only accounts get 401.
- The first authenticated call lazily creates `public.users` with `subjects: []` (`auth.ts:98-111`). If a row with that email already exists (possibly legacy id `usr_...`), that row is used. Therefore the app user id is `user.id` from `GET /api/auth/me`, NOT the Supabase UUID.
- Routes that call `auth()` with no request argument read cookies only and cannot be called with Bearer (section 4).
- Token refresh is the Supabase Flutter SDK's job. On a 401 from any route, refresh the session once and retry, then sign out.

#### Email OTP (sign-in)
1. `POST /api/auth/email-login` (alias `POST /api/mobile/login`), body `{ "email": string }`. Server emails a button link AND an 8-digit code. The link is a web URL (`/auth/callback?token_hash=...&type=...`), not an app link, so rely on the code.
2. Client verifies directly against Supabase: `verifyOTP(email, token, type: OtpType.email)`, and on failure retry with `OtpType.magiclink`. The web does exactly this double try (`src/lib/supabase-browser.js:52-64`). Which type succeeds for new vs existing users is UNVERIFIED.
3. Then `GET /api/auth/me` (retry on 429/500/502/503/504 with backoff 0, 250, 600, 1000, 1600, 2400, 3200 ms, mirroring `AuthProvider.jsx:13-17`).
- The 8-digit length is a Supabase project setting (UNVERIFIED in repo; web enforces 8 digits, `SignupCard.jsx:68,115,121`).

#### Native Google
Supabase `signInWithIdToken(provider: google, idToken, accessToken)` from the Flutter app. No MockMob backend change is needed because `auth()` is provider-agnostic (`auth.ts:140-142` reads `full_name|name` and `avatar_url`). Required external config, all UNVERIFIED (not in repo): Supabase Google provider with the Web client ID plus the Android client ID in "Authorized Client IDs"; Android OAuth client with package `in.mockmob.app` and SHA-1 for debug and Play App Signing keys; `serverClientId` set to the Web client ID; nonce handling matched to the Supabase "Skip nonce check" setting.

### 1.3 Error envelope (inconsistent by route; parse per route)
| Family | Shape | Used by |
|---|---|---|
| Machine code | `{ "error": "SESSION_EXPIRED" }` | `/api/sessions`, `/api/attempts` POST |
| Learning | `{ "error": CODE, "message": string }` | `learningHttp` routes (`/api/learning/plan`, `/api/study/*`, `/api/recovery/episodes*`) |
| Repair | `{ "ok": false, "error": code, "message": string }` | `/api/recovery/repair` |
| Quote | `{ "state", "reasonCode", "reason" }` | `/api/practice/quote` |
| Human string | `{ "error": "Attempt not found" }` | `/api/attempts*`, `/api/recovery` POST, `/api/users/[id]` |
| App prefs | `{ "error": "invalid_request", "message" }` (422), `{ "error": "unavailable" }` (503), `{ "error": "Unauthorized" }` (401) | `/api/me/*` |
| Login | `{ "ok": false, "message" }` | `/api/auth/email-login` |

Rules: branch on the code or status, never on human `message` text. 401 casing varies (`Unauthorized` vs `unauthorized`). A `JSON.parse` failure on `/api/sessions` or a learningHttp write returns 422 with the raw parser message; do not display it. All `/api/sessions`, `learningHttp`, `/api/me/*` and `/api/events` responses carry `Cache-Control: no-store`; several others (`/api/analytics`, `/api/leaderboard`, `/api/stats` public cache) do not, so do not depend on cache headers.

`/api/sessions` status mapping, applied to the thrown message in order (`src/app/api/sessions/route.js:25-27`, verified): `NOT_FOUND` gives 404; `MIGRATION|FAILED` gives 503; `CREDITS|PREMIUM` gives 402; else 422. Body over 600,000 chars gives 413 `{error:'Payload too large'}` (after auth and rate limit).

`learningHttp` mapping (`src/lib/server/learningHttp.js`): `NOT_FOUND` gives 404; `UNAVAILABLE|FAILED|AWAITING|CHANGED` gives 503; `CONFLICT` gives 409; else 422. So `STUDY_CONTENT_CHANGED` is 503, `REVISION_CONFLICT`/`STEP_CONFLICT`/`IDEMPOTENCY_CONFLICT` are 409. Writes over 8,000 chars give 413.

### 1.4 Rate limits (keys are route + IP + user id unless noted; no route sends `Retry-After` except where stated)
| Route | Limit | Limiter |
|---|---|---|
| `/api/practice/quote` | 120/min | persistent flag (`quote/route.js:20`, verified) |
| `/api/sessions` POST/PUT/PATCH and `/api/attempts` POST | 60/min | persistent flag (`sessions/route.js:19`, verified) |
| `/api/recovery/replay` | 30/min | persistent flag |
| `/api/recovery/repair` | 12/min | in-memory only |
| `/api/recovery` POST | 20/min | in-memory |
| learningHttp routes (all share one bucket `/api/learning`) | 60/min | persistent flag (`learningHttp.js`, verified) |
| `/api/learning/summary` | 120/min per IP | in-memory; sends `Retry-After` and `X-RateLimit-*` |
| `/api/auth/me` | 300/min per IP | in-memory; sends `Retry-After` |
| `/api/prepos/insights` | 60/min | |
| `/api/auth/email-login` | 5/hour per email, 60 s spacing | in-memory plus persistent |
| `/api/stats` | 120/min per IP | persistent flag; sends `Retry-After` |
| none | `/api/subjects`, `/api/chapters`, `/api/attempts` GET, `/api/analytics`, `/api/leaderboard`, `/api/bookmarks`, `/api/me/*`, `/api/events` | |

"Persistent" means Supabase RPC `take_rate_limit` only when env `PERSISTENT_LIMITS_ENABLED==='true'` (UNVERIFIED); otherwise per-serverless-instance memory. If persistent is on and the RPC errors, it fails closed with 429. Client policy: back off about 60 s on any 429, never poll learning routes, send session events only when changed and batched (the web PUT-syncs every 1.5 s, about 40/min, from the 60/min bucket, `TestPageClient.jsx:348`).

---

## 2. Endpoints the app uses

Conventions: "Auth today" is `Bearer` (works with a Supabase JWT) or `Cookie-only` (cannot be called natively). `auth(request)` routes accept both cookie and Bearer.

### 2.1 Account and identity

#### POST /api/auth/email-login (alias POST /api/mobile/login)
- Auth: none. Request `{ "email": string }` (trimmed, lowercased, must match `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`). `redirectTo` is ignored.
- Response 200 `{ "ok": true }`.
- Errors (`{ok:false,message}`): 400 invalid email; 429 "Please wait before requesting another login code." (no `Retry-After`); 500 not configured / could not create code / provider rejected key / could not send.
- Side effects: Supabase `generateLink(magiclink)` (may create the auth user, UNVERIFIED), email via Resend from `MockMob <support@mockmob.in>`. Not idempotent; each call issues a new code. Client: 60 s resend cooldown.

#### GET /api/auth/me (alias GET /api/mobile/me)
- Auth: Bearer. Response 200:
```json
{"user":{"id":"usr_...","name":"Asha","email":"asha@example.com","image":null,"subjects":["english","general_test"],"role":"student","creditBalance":100,"subscriptionStatus":"free","isPremium":false,"premiumUntil":null,"razorpaySubscriptionId":null},"needsOnboarding":false}
```
- `role` is `student|moderator|creator|admin`. `creditBalance` is the practice-credit ledger (100 on creation), not the PrepOS wallet. `subjects` maps `GAT` to `general_test` and de-duplicates. `isPremium` is computed (`subscription_status==='active'` OR `premium_until>now` OR legacy flag). `needsOnboarding = subjects.length===0`.
- Errors: 401 `{user:null,needsOnboarding:false}`; 404 same shape; 429 `{error:'Too many requests'}`; 500 `{error:'Failed to resolve auth session'}`.
- Not returned: createdAt, age, goal, consent, notification prefs (use `/api/me/*`).

#### GET /api/users/[id] (owner only)
- Auth: Bearer, and `id` must equal the caller's id, else 401 (`users/[id]/route.js:7-11`, verified). Returns full `userOut`. Prefer `/api/auth/me`.

#### PATCH /api/users/[id] (do not use for entitlements)
- Auth: Bearer, owner only. Used by onboarding web as `{ "subjects": ["english","accountancy"] }` (`OnboardingPageClient.jsx:71-75`). Response 200 full `userOut`; errors 401, 404 `User not found`, 500.
- DEFECT: body is unfiltered (`users/[id]/route.js:33`; `data/db.js:346-356`). The app may send only `{subjects}` and must treat this as a temporary route until an allowlisted profile route exists (section 7). Max 5 subjects and valid ids are enforced client-side only; ids come from `/api/subjects` where `practice==='supported'`.

#### POST /api/me/delete
- Auth: Bearer. Body optional `{ "source": "android" | "web" }` (default `android`).
- Response 200 `{ "status":"pending", "requestedAt": ISO, "message": "We delete your account and study records within 30 days. Payment records required by law are kept." }`.
- Errors: 401; 503 `{error:'unavailable'}`.
- Side effects: inserts one pending row in `account_deletion_requests` (partial unique index). It does NOT delete anything; an operator must process it (`me/delete/route.js:7-10`, `appPrefs.js:97-112`). Idempotent: a repeat returns the existing pending request. The app must show the 30-day message honestly and sign the user out locally only after it succeeds.

### 2.2 Consent and usage data

#### GET /api/me/consent and PUT /api/me/consent
- Auth: Bearer.
- GET 200: `{ ageBand: 'adult'|'minor'|'unknown', analyticsAllowed: boolean, policyVersion: '2026-10-12', decidedAt: ISO|null, withdrawnAt: ISO|null }`. Defaults to `unknown`/false when no row. 503 `{error}` on read failure.
- PUT body `{ "ageBand": "adult"|"minor"|"unknown", "analyticsAllowed": boolean }`, both required. `analyticsAllowed:true` with a non-adult band gives 400 "Usage data can only be turned on for adults (18 or older)."; invalid body 400.
- PUT 200: the GET shape plus `deletedEvents: number`. Whenever `analyticsAllowed` is false (withdrawal, minor, unknown), all stored `usage_events` for the user are deleted in the same call; failure of that delete returns 503 "Your choice was saved, but deleting earlier data failed. Please try again." Retry safely; PUT is idempotent.
- The age band is self-declared. The label to show is "Allow usage data to improve MockMob" (`src/lib/server/usage.js:3`). Default must be off.

#### POST /api/events (optional analytics)
- Auth: Bearer. Body `{ "events": Event[] }`, at most 50 events, whole body at most 100,000 chars (413), invalid JSON 400.
- `Event`: `{ event_id: string(<=64), name, platform: 'android'|'web', app_version?: string(<=32), occurred_at: ISO or epoch ms, props?: {...} }`. `occurred_at` must be within 7 days past and 5 minutes future. Allowed names (`usage.js:6`): `session_started, session_submitted, result_opened, recap_opened, recap_skipped, next_move_impression, next_move_reason_opened, next_move_started, next_move_dismissed, repair_started, repair_completed, fresh_check_completed, reminder_permission_result, notification_opened, goal_set, weekly_goal_met, finish_for_now, app_link_opened, app_opened`. Allowed prop keys with types: `subject,mode,state,action_type,outcome,source,screen,variant` strings (<=64), `minutes,count` numbers; any other key drops the whole event; props under 1 KB.
- Response 202 `{ accepted, dropped, collecting }`. If consent is not `adult` + allowed + not withdrawn, the server returns 202 `{accepted:0,dropped:n,collecting:false}`: the client must stop queueing when `collecting:false` and when consent is off, and must not send at all unless consent says allowed.
- The event may carry only `platform` and `app_version` besides `props`; there is no OS-version field, so user-facing copy may say "the app version" and not "the Android version". The client must tag its queue by user id and delete it on sign-out and account switch, because the server attributes events to the bearer of the request.
- Idempotent by `event_id` (client dedupes within a batch; DB insert is consent-checked atomically via RPC `insert_usage_events`). 503 `{error:'Temporarily unavailable.'}` retry with the same ids.

### 2.3 Notification preferences, devices, goal, rhythm

#### GET and PUT /api/me/notification-prefs
- Auth: Bearer. GET 200 (`appPrefs.js:15-23`):
```json
{"timezone":"Asia/Kolkata","quietStart":"23:00","quietEnd":"07:00","channels":{"check_due":true,"weekly_plan":true,"study_window":false,"result_ready":true},"studyWindow":null,"weeklyCap":5}
```
- PUT accepts any subset of `timezone` (must be in the allowlist: Asia/Kolkata, Asia/Dubai, Asia/Singapore, Asia/Kathmandu, Asia/Dhaka, Asia/Colombo, Asia/Karachi, Europe/London, America/New_York, America/Los_Angeles, Australia/Sydney, UTC), `quietStart`/`quietEnd` (`HH:MM` 24 h), `weeklyCap` (integer 0-14), `channels` (object of booleans over `check_due, weekly_plan, study_window, result_ready`, merged with current), `studyWindow` (`{start,end}` HH:MM, or `null` to clear). Empty patch gives 422 "Nothing to update." Other errors 422 `{error:'invalid_request',message}`, 401, 503 `{error:'unavailable'}`. Returns the full new prefs. Defaults are 23:00 to 07:00 IST, matching the owner's quiet-hours decision. Idempotent.

#### POST and DELETE /api/me/devices
- Auth: Bearer. Body `{ "token": string(20-4096 chars, no whitespace), "appVersion"?: string(<=32) }`; invalid gives 422 `{error:'invalid_request',message:'A device token is required.'}`.
- POST upserts by token (a token seen on another account moves to this one, `revoked_at` cleared), platform fixed `android`. Response `{ok:true}`. DELETE `{token}` sets `revoked_at`. Both idempotent; 503 `{error:'unavailable'}`.
- This route only stores the token. No server-side push sender is present in the routes read; whether pushes are actually sent is UNVERIFIED (section 7).

#### GET and PUT /api/me/goal
- Auth: Bearer. GET 200 `{ daysPerWeek: 1-7 (default 4), timezone, pausedUntil: 'YYYY-MM-DD'|null }`.
- PUT `{ "daysPerWeek": int 1-7 (required), "pausedUntil"?: 'YYYY-MM-DD'|null }`. A pause may be at most 100 days ahead and must be a real calendar date. 422 messages are friendly strings. Pausing never removes history. Idempotent.

#### GET /api/me/rhythm
- Auth: Bearer. Response 200 (`rhythm.js:128-142`):
```json
{"timeZone":"Asia/Kolkata","weekStart":"2026-10-12","studyDays":2,"studyDayDates":["2026-10-12","2026-10-13"],"daysGoal":4,"metThisWeek":false,"paused":false,"weeksMetStreak":3,"bestRun":5,"lastActivityAt":"2026-10-13T11:02:00.000Z","daysSinceLastActivity":0,"returning":false,"milestones":[{"id":"first_scored_session","achievedAt":"2026-09-01T10:00:00.000Z"}]}
```
- Meaning: a study day is a local day (timezone from `notification_prefs`, default IST) with at least one server-scored session or a completed Mistake Repair. Weeks are Monday to Sunday. The streak is consecutive weeks meeting the goal; the current week counts only once met; paused weeks do not break it. `returning` is true after 3 or more days away. Milestone ids: `first_scored_session, first_full_mock, first_repair, repairs_5, repairs_10, repairs_25, sessions_10, first_week_met, weeks_met_4` (`achievedAt` null when not earned). Known limits (documented in `rhythm.js:1-12`): the current goal is applied to all past weeks; no fresh-check milestones. Reads up to 26 weeks of activity.
- Exactly what counts (verified in `src/lib/server/appPrefs.js` `loadActivity` and `rhythm.js`, 12 October 2026): any attempt with a server `scoringVersion`, in any mode including Quick practice, with no minimum answer count yet, and one repair per `ai_credit_reservations` row that is committed with a stored repair (so one per acknowledged `explained` response of `POST /api/recovery/repair`; `stored`, `held_for_recheck` and `not_explained` add nothing). The retry session of a repair counts only as an ordinary attempt. No endpoint marks a whole repair finished.
- NOT returned today (the app cannot read them): closed-week rows, past-week counts, a week-just-closed signal, the previous streak value, repairs or mocks this week, and a stable id for a repair-finished or week-closed event (`milestones[]` covers only the nine listed ids). `[NEW-API]` B2 extension: `history` (last 12 weeks of `{weekStart, studyDays, goal, met}`), `repairsThisWeek`, `mocksThisWeek`, `lastClosedWeek` (`{id, studyDays, goal, met}`). Until then the client keeps best-effort local records (design spec 6.1).
- 503 `{error:'unavailable'}`. This is the supported source for streaks and celebrations; do not use `streakDays` in `/api/learning/summary` (UTC, today-only, ignores repairs).

### 2.4 Learning plan and summary

#### GET /api/learning/plan
- Auth: Bearer (learningHttp, shared 60/min). Query optional `subject`, `minutes` (10|20|30 honoured).
- Response (`learning.js:46-89`): `{ primary: Action, alternatives: Action[0..2], minutes, sequence?: Step[], study?: {dueCards, lessonsRead, preferences, weekday}, studyState?: 'unavailable', episodes: Episode[], pathwayState: 'available'|'blocked_content', supportedConcepts: [], recordState: 'ready'|'unavailable', ordinaryAttemptCount, tonight: {state:'ready'} | {state:'recorded', sessionId, minutes, completedAt:number, reviewMinutes}, milestones: [...] }`.
- `Action` = `{ kind, title, href, reason, duration, availability:'available', evidence:string[], facts:[{basis:'record'|'rule', text}] }`. Kinds in precedence: `resume_session, fresh_check, repair, investigate, baseline, ordinary_practice`. Today only `resume_session` or `ordinary_practice` are realistic because recovery is gated (section 6).
- `href` values are WEB paths (`/test?...&sessionId=`, `/dashboard?mode=quick&count=N[&subject&chapter]`, `/recovery?...`, `/review`, `/learn?recall=due`, `/learn/{unitId}`, `/study/{runId}`, `/result/{id}`, `/progress`). The client maps them to native routes and must not open them blindly.
- Expensive: loads all attempts, episodes and study record. Fetch on open and after a session, not on a timer.
- To make "tonight recorded" work, the practice start request must include `tonightKey` (12-100 chars of the key charset) and `tonightMinutes` (10/20/30) with quick mode and count 10 (for 10) or 20 (for 20/30). The web adds these only when there is no `sequence` and primary is `ordinary_practice` (`LearningNextAction.jsx`).

#### GET /api/learning/summary
- Auth: Bearer now (`route.js:85`, verified). Optional `subject`. 429 `{error:'Too many requests'}` with `Retry-After`; 401; 500.
- Response `{ plan:{status,isPremium,label}, progress:{solvedTotal,solvedThisWeek,weeklyGoal(30|80),weeklyPercent,accuracy,mockAvg,testsCompleted,totalMockQuestions,feedAttempts,skipped,streakDays,avgDwellMs}, bookmarks:{count,limit,remaining,questionIds}, premium:{...}, activity:[7 x {day,label,solved}], topContributors:[{id,name,count}] }`.
- Caveats: `streakDays` is UTC-based, counts from today only (0 if no activity today UTC), ignores study and repair, and can shrink retroactively. `weeklyGoal` week is server-local (UTC on Vercel). `topContributors` exposes other users' ids and names; the app must not render it. No `Cache-Control: no-store` header. Heavy (loads all attempts and progress rows). Prefer `/api/me/rhythm` for streak and week.

### 2.5 Subjects and chapters

#### GET /api/subjects
- Auth: none. Returns array of 42 `SUBJECTS` entries: `{ id (public; gat becomes general_test), internalId, name, short, glyph, chapters: string[], units?: [{unit_name,chapters}], officialCode, officialName, practice: 'supported'|'not_offered'|'retired'|'merged'|'unknown', practiceReason, mergedInto, registryVersion: 'nta-cuet-ug-2026@2026-09-02' }`.
- Not filtered. The client shows only `practice==='supported'` (15: english, general_test, accountancy, business_studies, economics, mathematics, physics, chemistry, biology, history, political_science, geography, psychology, sociology, computer_science, `data/cuet_controls.js:9-25`). `applied_mathematics` is `merged` into `mathematics`; do not offer it. Cacheable.
- Use `internalId` when comparing to `attempt.subject` and `questionsSnapshot[].internalSubject`.

#### GET /api/chapters?subject=<id>
- Auth: none. Response `{ grouped:true, units:[{id,name,sortOrder,chapters:[{id,name,sortOrder}]}] }` or `{ grouped:false, chapters:[...] }`. Errors: 400 `{error:'subject is required'}` or `SUBJECT_REQUIRED`; 422 `SUBJECT_NOT_SUPPORTED`; 500.
- The session API takes chapter NAMES, never ids. Names can contain commas (for example "Alcohols, Phenols & Ethers"), which breaks the comma-joined `chapters` parameter. Send the single `chapter` field for one chapter; use `chapters` only when no name contains a comma (`practiceSessions.js:30`, verified).

### 2.6 Practice quote

#### GET /api/practice/quote?subject=&mode=&count=&purpose=
- Auth: Bearer. Query `subject`, `mode` (default quick), `count`, `purpose` (`baseline|full_sample|` ordinary). No side effects; never charges or reserves.
- HTTP 200 even when blocked: the outcome is in the body. Non-200: 401 `reasonCode:'unauthenticated'`; 429 `rate_limited`; 503 `user_unavailable`.
- Body fields: `quotedAt, expiresAt` (TTL 60 s, `practice_quote.js:8`), `idempotencyToken` (UUID when launchable, else null), `subject:{storedId,id,code,name}`, `mode:{id,label,capabilityId,capabilityVersion}`, `count`, `durationSec`, `durationEstimated`, `entitlement:{kind:'free'|'access',expiresAt}`, `inventory:{policy,state:'sufficient_count'|'insufficient'|'empty'|'unknown',ordinaryCount,checkedAt,note}`, `allowance:{kind,state:'available'|'used'|'unknown'}|null`, `creditCost`, `creditBalance` (null for Pro), `upgradeHref` (web path; map to the native paywall), `state:'available'|'blocked'|'unavailable'`, `launchable`, `reasonCode`, `reason`, `offer:{monthly:{planId,rupees,interval,autoRenews,ready},oneTime:{planId,rupees,expires,onSale},purchasable:'monthly'|'one_time'}`.
- `reasonCode`: `ok, unauthenticated, rate_limited, user_unavailable, subject_not_offered|subject_retired|subject_unknown, mode_unknown, mode_unavailable, access_required (blocked), inventory_unknown, inventory_insufficient|inventory_empty (unavailable), insufficient_credits (blocked)`.
- The token is not server-validated or stored. It is a convenient `generationKey`. The quote is advisory; launch can still fail. Re-quote after `expiresAt`. The quote does not model `difficulty`.
- Free allowances (durable mode only): `daily_practice` (quick, count 10, once per IST day), `baseline:<subject>` and `full_sample:<subject>` (4 launch subjects). If durable mode is off, quote and launch charge credits.

### 2.7 Sessions (practice, mock) and attempts

Detailed in section 3. Endpoints: `POST /api/sessions` (start or resume), `PUT /api/sessions` (event sync), `PATCH /api/sessions` or `POST /api/attempts` (submit), `GET /api/attempts` (list), `GET /api/attempts/[id]` (result). All Bearer.

#### POST /api/sessions: start
Request body (the web sends every value as a string; numbers are also accepted):
| field | rule |
|---|---|
| `generationKey` | required unless resuming; `/^[a-zA-Z0-9_-]{12,100}$/` else 422 `INVALID_GENERATION_KEY` |
| `subject` | supported subject else 422 `SUBJECT_NOT_SUPPORTED` |
| `mode` | `quick|smart|full|nta`, default quick; else 422 `INVALID_MODE` |
| `count` | `max(5,min(50,Number(count)||10))` then mode resolution; fixed 50 for full and nta; unlisted counts fall back to the default (7 becomes 10) |
| `chapter` or `chapters` | up to 12, each validated against the syllabus else 422 `INVALID_CHAPTER` |
| `difficulty` | `easy|medium|hard`, Pro only, and mode must allow it (not smart/nta) |
| `experience` | `'practice'` for ordinary practice and mocks; `'recovery'` plus `recoveryFrom` for fresh-question replay |
| `purpose` | `baseline|full_sample` (allowances only) |
| `tonightKey`, `tonightMinutes` | see 2.4 |
| `sessionId` | resume (durable mode only) |
Routing (`sessions/route.js:30-32`, verified): `sessionId` truthy goes to `startPractice` (resume); `episodeId` goes to `startSession`; `experience==='practice' && !recoveryFrom` goes to `startPractice`; else `startSession`. The app must set `experience:'practice'` for ordinary practice.

Response: the public session view (`shared/recoveryContract.js:5-16`):
```json
{"id":"att_practice_3f9c...","startedAt":"2026-10-12T05:00:00.412+00:00","expiresAt":"2026-10-12T05:10:00.412+00:00","serverNow":1791781200530,"state":"active",
 "questions":[{"id":"q_9a1","subject":"english","chapter":"Vocabulary","question":"...","body":"...","options":[{"key":"A","text":"Frank"}],"passageText":null,"passageGroupId":null,"difficulty":"easy"}],
 "meta":{"sessionId":"att_practice_...","mode":"quick","requestedCount":10,"learningPurpose":"ordinary_practice","contentEvidence":"legacy_bank"}}
```
Answer keys are never sent. `startedAt` may be `...Z` (ticket mode) or Postgres `+00:00` (durable); parse both. Two modes exist and the production setting (`LEARNING_SESSIONS_ENABLED`) is UNVERIFIED, so support both:
- Durable: no `sessionTicket`; `state:'active'`; the server holds the session. Same `generationKey` returns the existing session (plus top-level `events`) without a new charge. A replay of an expired or submitted session gives 422 `SESSION_EXPIRED`.
- Ticket: `meta.sessionTicket` (`p2.<iv>.<ct>.<tag>`, up to 500,000 chars) and `meta.storage:'device'`; no `state`. The server keeps no copy: store the ticket with the questions; losing it loses the session. Same key and selection rebuilds the same id; if the attempt exists it returns 422 `SESSION_ALREADY_SUBMITTED`. No server resume (404 `SESSION_NOT_FOUND`).

Errors: 402 `INSUFFICIENT_CREDITS`, 402 `PREMIUM_REQUIRED` (premium modes and any `difficulty` for non-Pro), 422 `DIFFICULTY_NOT_ALLOWED`, 422 `INSUFFICIENT_PRACTICE_CONTENT` (no charge), 422 `INSUFFICIENT_VERIFIED_CONTENT` (recovery path), 503 `LEARNING_MIGRATION_REQUIRED|RECOVERY_MIGRATION_REQUIRED|SESSION_CREATE_FAILED`, 422 `PRACTICE_SNAPSHOT_TOO_LARGE|invalid_server_snapshot`. The web's `upgrade` field handler is dead code; the server never sends `upgrade`, so branch on `error` strings.
Side effects and idempotency: durable mode runs RPC `start_learning_session` in one transaction (spend credits or consume allowance, insert session and exposure rows), idempotent on `(user, generationKey)`. Ticket mode charges non-Pro after sealing with a deterministic reference, so a retry is free. Questions are fetched before any spend, so a failed build is not charged. Costs: quick 10, full 50; smart and nta 0 but Pro-only.

Modes (`data/test_modes.js`): `quick` (count 5/10/15/20, 60 s per question, free to try), `smart` (Pro, counts 10/15/20, adaptive 45/60/90 s per easy/medium/hard), `full` (fixed 50, 3600 s), `nta` (Pro, fixed 50, 3600 s, exam-style, original practice content). Always use the returned `expiresAt`; never compute the deadline locally.

Not provided today: per-answer correctness or an explanation before submit. Session views carry no keys, `PUT /api/sessions` returns only `acknowledgedSequence`, and correctness exists only in `GET /api/attempts/{id}` after submit. `[NEW-API]` B13: `POST /api/sessions/{id}/check {qid, answer}` returning `{correct, keyIndex, explanation}` for practice and recovery experiences only, refused (403 `check_not_available`) when the session's mode is `full` or `nta`, with the check recorded so the answer is final. Until it ships, Quick practice, chapter practice and repair retries show feedback only after submit. Also not provided: any server action at `expires_at` for an unattended session. `[NEW-API]` B11: the server finalises durable sessions at expiry from acknowledged events and creates the attempt (design spec 5.5.1). `POST /api/attempts` scores synchronously, so there is no asynchronous marking state.

#### PUT /api/sessions: sync events (durable sessions only)
- Body `{ "sessionId": string, "events": Event[] }`, cumulative. `Event = {seq:int, qid:string, type:'visit'|'answer', at:int, answer?:int|null}`; `answer` required for type answer; `null` means cleared.
- Response 200 `{ "acknowledgedSequence": number }`.
- `seq` starts at 1, +1 each, no gaps, maximum 5,000. `at` is integer ms since the SERVER `startedAt`, non-decreasing, and at most elapsed plus 2 s. Already-sent events must be byte-identical on resend. Errors (all 422): `invalid_event_sequence`, `invalid_event_answer`, `invalid_events`, `unknown_question`, `EVENT_CONFLICT`, `SESSION_EXPIRED`. A ticket session gets 404 `SESSION_NOT_FOUND` (skip PUT when `meta.sessionTicket` exists, as the web does, `TestPageClient.jsx:336`).
- Idempotent for identical prefixes. Never rewrite or round sent events.

#### PATCH /api/sessions or POST /api/attempts: submit
- Body `{ "sessionId": string, "sessionTicket"?: string, "answers": { [qid]: int }, "events": Event[] }`. `POST /api/attempts` is literally the PATCH handler (`attempts/route.js:18`) with the same limits. The web uses `POST /api/attempts` with `sessionId`, `sessionTicket` from `selectionMeta`, `answers`, `events` filtered to `at <= duration` (`TestPageClient.jsx:392-397`).
- Response 200: the attempt object (`attemptOut`, section 2.8) without `answerReviews`. The client then calls `GET /api/attempts/[id]` for the result.
- Accepted until `expires_at + 120,000 ms`; after that 422 `SESSION_EXPIRED`. Submit is idempotent: an existing attempt id returns the saved attempt.
- Ticket path: ticket must open and belong to the user (422 `INVALID_PRACTICE_SESSION`, 404 `SESSION_NOT_FOUND`); answers scored as given. The server cannot tell if answers were produced after the deadline, so the client must stop answering at `expiresAt`. Events failing validation are dropped (`recovery.telemetry:'invalid'`), but bad answers give 422 `invalid_answer|unknown_question`.
- Durable path: before the deadline `input.answers` are used for ordinary sessions; in the grace window only stored acknowledged answers count. Recovery-path sessions ignore `input.answers` entirely and score only the acknowledged event log (`recoverySessions.js:129`), so events must be PUT or sent in the PATCH.
- Scoring: +5 correct, -1 wrong, 0 blank. `score = max(0, round((correct*5-wrong)/(n*5)*100))`, a percentage 0-100, not marks. Marks are `correct*5 - wrong` out of `n*5`.
- Side effects: insert `attempts` row with `id == sessionId`; upsert `user_question_progress`; durable path queues `recovery_review_queue` rows due in 1 day for non-correct questions; no additional charge. 413 is possible only in the worst case where the echoed ticket plus 5,000 events exceeds 600,000 chars. 503 `SESSION_SUBMIT_FAILED` on RPC failure.

### 2.8 Attempts and results

#### GET /api/attempts
- Auth: Bearer. Bare JSON array of ALL the user's attempts, newest first, each with full `questionsSnapshot` (including keys and explanations) and `details`. Unpaginated and heavy; there is no slim list. Call once after sign-in or after a submit and cache locally. 500 `{error:'Failed to load attempts'}`.
- `attemptOut`: `{ id, userId, subject (internal id), score (percent), correct, wrong, unattempted, total, details:[{qid,givenIndex:int|null,isCorrect:true|false|null}], questionsSnapshot:[...], selectionMeta:{...}, completedAt: epoch ms }`.

#### GET /api/attempts/[id]
- Auth: Bearer. Response `{...attemptOut, answerReviews: {[qid]: review}, answerReviewState: 'ready'|'unavailable'}`; `Cache-Control: no-store`. 404 `{error:'Attempt not found'}` also for another user's attempt; 401; 500. No rate limit.
- `selectionMeta.scoringVersion` is `server_practice_v1|server_snapshot_v1` for server-scored attempts; anything else means legacy device scoring and the web shows no changes or timings. `selectionMeta.recovery` (`telemetry: 'self_reported'|'inconsistent'|'invalid'`, `observed.answerChanges`, `timeline`, `recommendation`) carries timing data; only `self_reported` is usable.
- `answerReviews` states: `withdrawn`, `under_review`, `content_changed`, `key_changed_unverified`, `corrected` (with `currentIndex`, `explanation`, `source`, `chosenIndex`, `originalMarks`, `correctedMarks`, `adjustment`). No entry means the key is unchanged.
- Key-display rule (replicate): mark the correct option only with no review, or when `review.state==='corrected'` and `review.currentIndex===j`. With any non-corrected review show no key and no explanation. Options may be strings or `{key,text}`; handle both.
- Client-side derivations to port from `data/session_recovery.js`: marks, accuracy, per-question verdict, dwell time from `timeline` (only when `telemetry==='self_reported'`), chapter breakdown, observations, `formatDuration`. Never compute scores or keys for authority.

#### GET /api/attempts/[id]: `mistakeInsights` and `swot` (additive, 15 Oct 2026)
- Two new top-level fields beside `recap` and `missedBefore`. Both are built on the server from the user's stored attempts (the route already reads them), cost no model call and no credit, and arrive as finished sentences with their denominators, so the web and the app say exactly the same thing. The app only lays them out: it never rewords a line, recomputes a number or adds a cause.
- Each is computed in its own try/catch. When the history read fails the route still returns 200 with `swot: null` and `mistakeInsights: {}`. The env value `SWOT_ENABLED=off` omits `swot`. A client treats absent, `null`, a non-object and an unknown `state` as "nothing to show". A `null` never renders as 0 or as a placeholder.
- `mistakeInsights`: `{ [qid]: { lines: [{ kind, text }], evidence } }` for every answer with `isCorrect === false`; `{}` while `answerReviewState` is not `ready`, as the SWOT then says `checks_pending`. `lines` are in display order and each exists only when its gate passed. `kind` is `change`, `time`, `repeat_same` or `chapter`; an unknown kind is still shown. `evidence` is `{ firstIndex, finalIndex, seconds, medianSeconds, timed, chapter: { right, answered, papers } }` with `null` for unknown values; it is for tests and is not shown. The app shows `lines[].text` under "From your record" in a mistake's repair view, then the repair response's `pattern.line`.
- `swot`: `{ version: 1, state, message, basis, quadrants, plan }`.
  - `state` is `ready`, `checks_pending`, `too_few` or `not_available`. `not_available` is a practice attempt, a mode other than `full` or `nta`, or a paper not scored on the server.
  - Outside `ready`: `basis` is null, `quadrants` is `[]` and `plan` is `[]`. `message` is set for `checks_pending` ("This read appears once the answer checks load.") and `too_few` ("Answer at least 10 questions for a read of this paper."), and the client shows only that line. Nothing is drawn for `not_available`.
  - `basis`: `{ line, heldLine, counted, total, held, earlierPapers, earlierAnswers, timing }`. `line` reads "From 49 of 50 questions in this paper and 212 earlier answers in Accountancy across 6 papers." `heldLine` is null unless questions under re-check or corrected were left out. `timing` is `recorded` or `not_recorded`.
  - `quadrants` always has 4 entries in the fixed order `strength`, `weakness`, `opportunity`, `threat`, each `{ id, label, empty, items }`. A quadrant has either `items` or one quiet `empty` line. `label` is the heading word ("Strengths", "Weaknesses", "Opportunities", "Threats") and is always written, never replaced by colour alone.
  - `items[]`: `{ id, kind, title, detail, chapter, questions, planId, evidence }`. `questions` are 1-based question numbers of this paper in snapshot order (the same numbers as the result's answer rows), used for the "See" buttons; `planId` names the plan row that practises the item, or is null. Kinds: strengths `strong_chapter`, `accurate`, `changes_helped`; weaknesses `weak_chapter`, `weak_chapter_paper`, `changes_hurt`, `quick_wrong`; opportunities `close_chapter`, `blanks`, `untried`; threats `repeat_loss`, `chapter_slipped`, `not_opened`, `repeat_misses`. A chapter is named at most once. Caps per quadrant: 2, 3, 2, 2.
  - `plan[]`: up to 3 rows `{ id, label, reason, practice: { subject, mode: 'quick', count, chapter|null }, href, later }`. `href` is the web link (`/dashboard?subject=..&mode=quick&count=..[&chapter=..]`). The app ignores `href` and builds its own link from `practice`: `/dashboard?subject=<public subject id>&mode=<chapter if a chapter is set, else quick>&count=<n>[&chapter=<name>]`, resolved by `ActionRouter.resolve` to `/practice/setup/chapter` or `/practice/setup/quick` and pushed. That opens the setup screen with its own credit quote, so nothing starts and nothing is charged before the second tap. `later` is null or `{ at: <epoch ms>, right, of, line }`, the earliest later quick set wholly in that chapter ("A set on this chapter on 16 Oct: 7 right of 10."). It says what happened; it never claims the plan was followed.
- Truth rules the client relies on: every number comes from stored records with its denominator; nothing about the student comes from a model; no forecasts, rank or percentile; an NTA paper gets the same output as a full mock and Mobi stays hidden on NTA attempts, as before. Strings are sentence case with no exclamation mark, no em dash and no middle dot.
- Client rules: render only what is present, ignore unknown fields, keep the server's order, and show "After this mock" on the full result only (after the hero and before "Where the marks went"). A first-view entrance plays once per attempt per app run; reduced motion shows everything at rest. Dart models: `Swot`, `SwotBasis`, `SwotQuadrant`, `SwotItem`, `SwotPlanItem`, `SwotPractice`, `SwotLater` (`lib/core/models/swot.dart`) and `MistakeInsights`, `InsightLine` (`lib/core/models/mistake_insights.dart`); `AttemptDetail.mistakeInsights` is an empty map and `AttemptDetail.swot` is null when absent. The contract fixture is `flutter_app/test/fixtures/swot_contract_v1.json`, a byte copy of the website's `data/tests/fixtures/swot/contract_v1.json` (built by the server code, copied at integration on 15 Oct 2026; the models parsed it with no change). The hand-written stand-in kept beside it, `swot_contract_stand_in.json`, carries unknown fields at three levels and the specific values the unit tests assert.

### 2.9 Recovery (Find, Repair, Prove)

#### GET /api/recovery/replay?attemptId=
- Auth: Bearer; 30/min. 200 `{chapters:[], state:'unsupported'}` when the subject is outside the 4 launch subjects (english, accountancy, business_studies, economics), else `{chapters:[{chapter,state:'available'|'unavailable',href?}], state:'ready', delayedCheckHref:'/recovery'}`. Errors 401, 422 `Invalid attempt`, 404 `Attempt not found`, 503 `Fresh practice could not be checked. Your result is still available.`
- `href` is a web path; parse its query to build the start: `POST /api/sessions {subject, mode:'quick', count:'5', chapter, recoveryFrom:<attemptId>, experience:'recovery', generationKey}`. The launch can still fail with 422 `INSUFFICIENT_VERIFIED_CONTENT`. Quick 5 on this path is free and lasts 300 s. One call per result view; it scans pools for up to 12 chapters.

#### POST /api/recovery/repair
- Auth: Bearer; 12/min in-memory. Body `{attemptId, questionId, requestId}`, `requestId` matching `/^[A-Za-z0-9_-]{16,64}$/`. Reuse the same `requestId` on retries; mint a new one only after `operation_released`.
- Costs 1 PrepOS (AI wallet) credit, separate from practice credits. Free wallet 10 per IST month, Pro 50 (`aiCreditWallet.js:16-17`).
- 200 outcomes: `explained` (`repair:{why_tempting,why_wrong,key_idea,next_step,model,generatedAt}, charged, wallet, practiceHref, chosenIndex, keyIndex`), `stored` (free reopen), `held_for_recheck` (AI disagreed with the key; question is globally withheld pending review, charged 0), `not_explained` (charged 0). Client must accept only these four `status` values and require `repair.key_idea` for explained and stored (v3 keeps `key_idea` as an alias of `rule`; see "POST /api/recovery/repair: v3 payload" below).
- Error HTTP codes: 400 `request_id_required`; 401; 402 `insufficient_ai_credits` (with `balance`); 404 `not_found|user_not_found`; 409 `question_withdrawn|question_under_review|key_changed|operation_released|in_progress`; 422 `invalid_request|not_a_mistake|snapshot_invalid`; 429 `rate_limited`; 502 `provider_error|unusable_output`; 503 `question_unavailable|paused|could_not_start|quarantine_not_confirmed`. Eligibility failures may include `{review}`, which takes priority over the error code. Retry allowed after `operation_released` (new id) and `in_progress`; otherwise only when status is not 401/402/404/409/422.
- Text limits: `why_tempting, why_wrong, key_idea` up to 320 chars; `next_step` up to 220. `practiceHref` is a web path to convert to a recovery start as above.

#### POST /api/recovery/repair: v3 payload and `pattern` (additive, 15 Oct 2026)
- The request, the four `status` values, the error codes and the credit rules are unchanged: 1 AI credit and one model call per fresh repair, free reopen, every failure releases the credit. Only the `explained` and `stored` bodies grow.
- Shape of `explained` (a `stored` body has the same shape with `charged: 0` and no `wallet`): `{ ok, status, repair: { version: 3, trap_type, trap, why_wrong, why_right, contrast, others: [{ index, why }], rule, memory_hook, another_way, why_tempting, key_idea, model, generatedAt }, pattern: { line, scope, k, n, trapType } | null, charged, wallet: { total, state }, practiceHref, practiceAction, chosenIndex, keyIndex }`.
- Fields: `trap_type` is one of `partly_true`, `reversed`, `look_alike_term`, `missed_not_except`, `not_in_passage`, `calculation_slip`, `wrong_rule`, `one_step_short`, `extreme_word`, `assertion_reason_link`, `other` (the server turns an unknown value into `other`; the app should too). `trap` is why the chosen option looks right, about the option and not the student. `why_wrong` is the exact point where it fails. `why_right` is why the key is right. `contrast` is one worked contrast ("If the question said X, B would fit. It says Y, so D."). `others` holds one line per option that is neither chosen nor the key, indexes 0-based in the served option order, all or nothing. `rule` is the "Keep this" instruction. `memory_hook` is a contrast pair, an example or a mnemonic, never a repeat of the rule. `another_way` is the same idea explained more simply, in the same response: revealing it makes no call and costs no credit.
- Optional: `contrast`, `memory_hook` and `another_way` may be absent. `others` may be `[]` or absent. `pattern` may be null (it is read free from the user's stored repairs, under a 1.5 s stop, and any failure gives null). A client renders only what is present and shows no empty heading. Invalid `others` entries (non-integer or duplicate index, an index equal to the chosen option or the key, empty text) are ignored.
- Versions: version 3 when `why_right` is present; version 2 when only `rule` is present; otherwise version 1. Stored v1 and v2 repairs come back as stored (no `version`) and keep their old layout. `why_tempting` (equal to `trap`) and `key_idea` (equal to `rule`) are aliases present on every v3 response for older app builds; they are never stored. A client reads `key_idea ?? rule` and `why_tempting ?? trap`.
- Server caps per field (characters): `trap` 260, `why_wrong` 280, `why_right` 280, `contrast` 280, each `others[].why` 150, `rule` 130, `memory_hook` 100, `another_way` 460. The model's `next_step` sentence is gone: "Do this next" is the real practice action (`practiceAction`, or `practiceHref` as before).
- `pattern.line` is a finished sentence, for example "Since 9 Oct, 2 of your 3 repairs in Correct Word Usage had this trap." It is dated (India time) from the earliest repair it counts, so it is the whole count for that period. `scope` is `chapter` or `subject`. `k` of `n` count the user's repairs that carry a trap type (v1 and v2 repairs count in neither), this one included; `since` (ms) is the date the line starts from. The app shows the line under "From your record", after the `mistakeInsights` lines. It does not compute or reword it.
- Screen order, identical on web and app: the folded question line; the trap heading with the chip "Explained from the answer key (D)." (the word "Checked" is no longer used: the call is told the key before it explains); "Why B looked right"; "Where it breaks"; "Why D is right" with `contrast` under it; the "The other options" disclosure, closed by default; "Keep this" with Copy, then "To remember it: ..."; "Explain it another way"; "From your record"; the marks line; "Do this next"; and the fine print "1 credit used. 43 left." or "Saved repair. No credit used." The app reads `response.charged` and `response.wallet.total` for the fine print.
- Loading lines, on real elapsed time and never a fake stage: "Writing the repair for Q7." then, after 8 s, "Still writing. You are charged only if it arrives." then, after 45 s, "Taking longer than usual. Still trying."
- Free versus credit: free are the key, the book explanation, the marks line, every "From your record" line, the pattern line, reopening a saved repair, and the SWOT and its plan. The credit covers the trap, why it tempted, where it breaks, why the key is right, the other options, the contrast, the rule and hook, and "Explain it another way".
- Rollback: the env value `REPAIR_PROMPT_VERSION=1` switches the server back to the v1 prompt and payload, so a client must keep parsing v1 and v2.

#### POST /api/recovery (decision log)
- Auth: Bearer; 20/min. Body `{attemptId, strategy: 'two_pass'|'concept_repair'|'timed_practice', reflection: string(<=1000)}`. 200 `{saved:true, evidenceState:'more_evidence_needed'}`. Errors 401, 429, 422 (`Invalid reflection` or `A new server-scored session is needed` for legacy attempts), 404, 503. Upsert on `(user, attempt, strategy)`; idempotent, overwrites.
- `GET /api/recovery` is heavy (all attempts, evidence checks, raw rows). Not for the home screen.

#### /api/recovery/episodes and /responses
Behind the recovery release gate (section 6). `POST /api/recovery/episodes {conceptId, requestKey}` fails with 503 `PATHWAY_AWAITING_SOURCES_AND_CALIBRATION` today. Do not build UI beyond the blocked state.

### 2.10 Study suite (all learningHttp, Bearer, shared 60/min)
- `GET /api/study/catalog?subject=`: `{ state:'ready'|'disabled', subjects, units:[UnitView], queue:{dueCount,overdueCount,newAllowance,availableCount,newCount,pausedNew}, active, nextUnit, preferences, recallEnabled, newCardsPerDay:5, introducedToday, progress }`. `UnitView.status` is `new|in_progress|lock_in|due|learned`.
- `GET/PUT /api/study/preferences`: GET `{subjects, minutes:10|20|30, newCardsPerDay:5, weeklyPlan:null|[7], revision, premium, state}`. PUT `{expectedRevision:int (required), subjects?, minutes?, weeklyPlan?}`; stale revision gives 409 `REVISION_CONFLICT` (refetch and retry); `weeklyPlan` is Pro-only (422 `PREMIUM_REQUIRED`); `newCardsPerDay` is forced to 5. State `disabled` gives 503 `STUDY_STORAGE_UNAVAILABLE`.
- `POST /api/study/runs {requestKey, mode:'learn'|'recall', unitId?, mixed?, unitIds?}`: starts or resumes a run; returns `publicRun`. `requestKey` is `/^[a-zA-Z0-9_-]{12,100}$/`. Starting recall consumes the day's new-card allowance immediately. Errors 422 `LESSON_NOT_READ|DAILY_NEW_LIMIT_REACHED|NOTHING_DUE|PREMIUM_REQUIRED|INVALID_*`, 503 `STUDY_RECALL_UNAVAILABLE|STUDY_CONTENT_*`, 404 `UNIT_NOT_FOUND`. Idempotent on `requestKey`; a different shape gives 409 `IDEMPOTENCY_CONFLICT`. At most 10 cards per run.
- `GET /api/study/runs/{id}`: `publicRun` with `state:'active'|'complete'|'set_aside'|'invalidated'`, `cursor`, `revision`, `revealed`, `feedback`, `item`, `total`. Answers, explanations and cues are withheld until revealed or answered. `invalidated` returns 200 with `units` to route to the replacement lesson.
- `POST /api/study/runs/{id}/events {requestKey, expectedRevision, itemId, type:'answer'|'reveal'|'rate'|'continue', value?, rating?, assisted?}`: server grades; ratings 1 Again, 2 Hard, 3 Good, 4 Easy (auto-graded recall: wrong 1, correct and assisted 2, correct 3; self-rated reveal cards send 1-4). Stale revision gives 409 `REVISION_CONFLICT`; wrong item gives 409 `STEP_CONFLICT`. Replay with the same key returns the stored original result. Persist one pending request per run across app kills and reuse its key.
- `GET /api/study/units/{id}`: lesson content. This GET records a study exposure (a write); do not prefetch lessons through it.
- `GET /api/study/summary?subject=&chapter=` exists (`study/summary/route.js`); its response shape was not read (see section 7).

### 2.11 Other reads the app may use
- `GET /api/ai/credits` (Bearer now): PrepOS wallet. Shape `{ok,userId,state:'available|empty|paused|schema_unavailable|error',message,wallet:{state,spendable,paid,known,includedMonthlyCredits,includedUsed,includedRemaining,bonusCredits,total,resetAt,periodStart,...},isPaid,tier,creditCosts,practiceCredits:{balance,label},checkout:{open,reason},buyPacks:[...]}`. Never render `known:false` (null balances) as zero. 401 `{error:'unauthorized'}`; 503 `{error:'user_unavailable'}`. Checkout is closed (`aiCommerce:false`); packs are `paused`.
- `GET /api/prepos/insights` (Bearer; 60/min): `{ok,userId,insights,findings,basis}`; empty state `{state:'empty',...}`; findings carry web-path `action.href` values to map.
- `GET /api/analytics` (Bearer): radar data. Uses internal subject ids; returns Pro-style `advanced` fields to everyone (no server gating). Decide which parts to show; rank-readiness heuristics conflict with the product's own no-rank-prediction principle.
- `GET /api/compass/pro` (Bearer; 60/min): `{ok:true,locked:true}` for non-Pro, else `{ok,locked:false,projection,sessions}`.
- `GET/POST /api/bookmarks` (Bearer now): GET `{questionIds, questions:[snake_case rows], count}`; POST `{questionId, saved:boolean, source?}` returns `{saved,count,limit}` (limit 25 free, null Pro); 402 `Free bookmark limit reached`.
- `GET /api/stats` (public, cached 30 s), `GET /api/leaderboard` (public, unpaginated, lists names and ids of every ranked user plus 12 synthetic rivals). Do not show the leaderboard to students without a privacy decision (gap G7).
- Landing sample drill: five hard-coded questions in `src/components/landing/DemoDrill.jsx:12-58`, no API. Bundle a JSON copy with the disclaimer "Five original sample questions. No signup. Not an official PYQ or a scored diagnostic."

---

## 3. Practice-session protocol (exactly as the web runner does it)

Reference: `src/app/(app)/test/TestPageClient.jsx` (start `:247-256`, restore `:212-238`, timing `:273-283`, event capture `:188-194`, sync `:336-348`, submit `:392-416`).

1. **Load context.** `GET /api/auth/me` (credits, Pro), `GET /api/subjects` (filter supported), optionally `GET /api/chapters`.
2. **Quote.** `GET /api/practice/quote?subject=&mode=&count=&purpose=`. If `launchable:false`, show `reason`; for `access_required` or `insufficient_credits` map `upgradeHref` to the native paywall (the app does not sell in v1, so show the reason only). If the quote is older than `expiresAt` or the selection changed, re-quote before launch.
3. **Start.** `POST /api/sessions` with `generationKey` = the quote's `idempotencyToken` (or a fresh `[A-Za-z0-9_-]{12,100}` string), `subject`, `mode`, `count`, `chapter`, `experience:'practice'`, optional `difficulty` (Pro), optional `tonightKey/tonightMinutes`. Persist the `generationKey` locally before sending so a double tap or crash retries the same key and is idempotent.
4. **Anchor the clock.** On receipt: `receivedAt = monotonicNow()`; `serverElapsed = max(0, serverNow - Date.parse(startedAt))`; `startedRef = receivedAt - serverElapsed`; `endsAt = receivedAt + max(0, Date.parse(expiresAt) - serverNow)`. Use a monotonic clock for the countdown and for event `at` (`at = max(prior.at, monotonicNow() - startedRef)`, integer ms). Do not use the wall clock for `at`; the server rejects events later than server elapsed plus 2 s.
5. **Persist a local draft** keyed `mm:test:<userId>:<subject>:<chapters|chapter|*>:<count>:<difficulty|auto>:<mode>`: questions, answers, visited, marked (local only), `selectionMeta` (including `sessionTicket` in ticket mode), `generationKey`, events, `startedAt`, `endsAt`, `idx`, `pendingSubmission`. Resume rules (`data/session_draft.js`): needs `selectionMeta.sessionId`, 1-50 questions, finite `endsAt`, matching `sessionId` or `generationKey`, and `endsAt > now` or (`pendingSubmission` and `endsAt + 120000 > now`).
6. **Resume.** Durable: `POST /api/sessions {sessionId}` returns the view plus `events`; restore answers from `events`, reset index to 0, and append one `visit` for question 1. Ticket mode: restore from the local draft only.
7. **Events.** `seq` counter from 1, first event is `visit` on question 1, `gotoQuestion` records `visit` for the target question only, an answer records `{type:'answer', answer:int}`, clearing records `answer:null` and removes the key from `answers`. Cap 5,000. Block answering when submitted, submitting, pending submission, or past `endsAt`.
8. **Sync (durable only, skipped when `selectionMeta.sessionTicket` exists).** `PUT /api/sessions {sessionId, events}` with the full cumulative array. The web does it every 1.5 s and on reconnect; the app should send only when events changed, and batch. On `EVENT_CONFLICT` refetch via resume and rebuild; on `SESSION_EXPIRED` stop.
9. **Submit.** At zero time left (once) or on user tap: `POST /api/attempts {sessionId, sessionTicket?, answers, events}` where `events` are filtered to `at <= endsAt - startedRef`. On a network error set `pendingSubmission:true` and retry on reconnect while `now <= endsAt + 120000`. On `SESSION_EXPIRED` show that the server's submission window has ended and the session cannot be recorded. Submit is idempotent, so retrying is safe.
10. **Result.** Clear drafts; `GET /api/auth/me` to refresh credits; `GET /api/attempts/{sessionId}` for the result (`answerReviews` included). Then optionally `GET /api/recovery/replay?attemptId=` once, and `GET /api/me/rhythm` for the week and celebration state.

---

## 4. Cookie-only routes the app needs, and the change required

Verified by grep for `auth()` with no request argument in `src/app/api`. Items 1-4 were cookie-only before commit `5fac96f` and are now fixed; they are listed so the client team does not carry stale assumptions.

| Route | State now | Change required for the app |
|---|---|---|
| `/api/learning/summary`, `/api/bookmarks`, `/api/ai/credits`, `/api/ai/usage`, `/api/ai/mentor/history`, `/api/users/[id]` | Bearer works (fixed in `5fac96f`) | None. Add an app test that sends only a Bearer header. |
| `PATCH /api/users/[id]` | Bearer works but body is unfiltered | Add allowlisted `PATCH /api/me/profile` (name, subjects with server-side validation: supported ids only, maximum 5). Strip `role, subscriptionStatus, isPremium, premiumUntil, razorpaySubscriptionId, email` from `PATCH /api/users/[id]`. Security fix before launch. |
| `/api/billing/cancel`, `/api/ai/credits/order`, `/api/ai/credits/verify` | Cookie-only on purpose ("the app does not sell in v1", `ai/credits/order/route.js`) | None for v1. Any later in-app purchase must go through Google Play Billing, not these Razorpay routes. |
| `/api/ai/context`, `/api/ai/actions/execute`, `/api/ai/mentor/local`, `/api/ai/mentor/session/new`, `/api/ai/rival/start`, `/api/ai/rival/submit` | Cookie-only | Only if the app ships PrepOS mentor or rival features: switch to `auth(request)` and add a rate limit and idempotency review. Out of scope for the v1 contract. |
| `GET/POST /api/questions`, `/api/questions/{mine,moderate,upload}` | Cookie-only | Not needed by students in v1 (contributor and moderator tools). Leave web-only. |
| `/api/creator/me` | Uses `requireCreator()` (cookie guard) | Web-only. |
| `GET /api/learning/plan`, `/api/study/*`, `/api/recovery/*`, `/api/practice/quote`, `/api/sessions`, `/api/attempts*`, `/api/me/*`, `/api/events`, `/api/compass/pro`, `/api/prepos/insights`, `/api/analytics` | Bearer works | None. |

Not Bearer-dependent: `/api/subjects`, `/api/chapters`, `/api/stats`, `/api/leaderboard` are public.

---

## 5. Offline: cacheable vs server-authoritative

Cache for display, revalidate on foreground, label with "as of" when stale:
- `/api/subjects` and `/api/chapters` (syllabus; key by `registryVersion`).
- Study catalog titles, summaries and objectives; lesson content after the student has opened it once, keyed by `id + version + contentHash` and discarded on any change.
- Last results: `GET /api/attempts` list (or per-id detail) after a successful fetch, for offline review of past results.
- Last `/api/me/rhythm`, `/api/learning/plan`, `/api/learning/summary` (display only), `/api/me/notification-prefs`, `/api/me/goal`, `/api/me/consent`.
- The five-question landing drill as a bundled asset.
- In-progress session draft (questions, answers, events, ticket, generationKey, pendingSubmission) so a session survives app kill and offline; ticket mode makes this mandatory.
- A queued (not yet sent) analytics batch, but only while consent is allowed; drop the queue and stop on withdrawal.

Must stay server-authoritative (never compute or trust locally):
- Scoring, answer keys, explanations, cues, answer corrections (`answerReviews`), study-answer grading.
- Credits, allowances, Pro status, premium gating, quote `launchable`.
- Session deadlines (`expiresAt`), the submit grace window, event validation.
- FSRS scheduling, `due` times, daily new-card allowance and backlog pause, run `cursor/revision`.
- Streak, weeks-met, milestones, "tonight recorded", weekly counts.
- Whether content is current (hash validation per event).

Offline behaviour: a session already started can be answered offline and submitted on reconnect within `expiresAt + 120 s`; after that it cannot be recorded. Starting a session needs the network (quote and start). Study runs allow one queued event per run (same `requestKey` and `expectedRevision`); a second offline step cannot target a revision that does not exist yet. Preference PUTs are revision-guarded where applicable (`/api/study/preferences`); notification prefs, goal and consent are last-write-wins.

---

## 6. Feature flags and release gates that change client behaviour

There is no HTTP capabilities endpoint (`data/capabilities.js` is compile-time). Infer state from responses or ship a build-time copy.

| Gate | Value in repo | Client effect |
|---|---|---|
| `LEARNING_SESSIONS_ENABLED` env | UNVERIFIED (docs say enable only after audits) | Chooses durable vs ticket mode; enables allowance quota. Support both; detect by `meta.sessionTicket` presence. |
| `RECOVERY_PATHWAYS_ENABLED` env and `data/recovery_pathways.json` | manifest `state:'blocked_sources'`, `pathways:[]` | `pathwayState:'blocked_content'`; episode starts fail with 503 `PATHWAY_AWAITING_SOURCES_AND_CALIBRATION`. Recovery capability is `blocked_content`. Show the blocked copy; the replay "Prove" step over `/api/sessions` with `recoveryFrom` is a separate path and works for the 4 launch subjects. |
| `STUDY_CONTENT_ENABLED`, `STUDY_RECALL_ENABLED`, `STUDY_GUIDED_PLAN_ENABLED` env | docs state saved `true` on 4 Oct 2026 (UNVERIFIED live) | Off means study `state:'disabled'`, no recall, no `sequence`/`study` in plan. Detect via `state` and `recallEnabled`. |
| `RELEASE_GATES.runtimeAi` | true | PrepOS replies and Mistake Repair available; budget capped (USD 25 per IST month). |
| `RELEASE_GATES.aiCommerce` | false | PrepOS top-ups and paid rival battles paused (`checkout.open:false`). |
| `RELEASE_GATES.content`, `authenticatedJourney` | false | Recovery blocked (`recoveryReleased()` false). |
| `RELEASE_GATES.stagingPayments`, `economics` | false | New offer not released; current offer is `pro_cuet_2027` at 99 rupees until 31 July 2027. |
| `PERSISTENT_LIMITS_ENABLED` env | UNVERIFIED | Rate limits are per instance when off; closed on RPC error when on. |
| `ANDROID_CERT_SHA256` env | UNVERIFIED | Empty makes `assetlinks.json` return `[]`; App Links will not verify. |
| Mode capabilities | quick/full: credits or access; smart/nta: Pro | Show Pro gating from quote `reasonCode:'access_required'`; `difficulty` is Pro for every mode. |
| Consent policy | `POLICY_VERSION='2026-10-12'` | Analytics collected only for `ageBand:'adult'`, allowed, not withdrawn. Minor and unknown stay off by server enforcement. |
| NTA integrity (fullscreen/tab strikes) | web-only (`TestPageClient.jsx:419-420`) | Not a server rule; the app decides its own policy. |

---

## 7. Gaps and open questions

Backend work needed before or soon after launch:
- G1. Privilege escalation: `PATCH /api/users/[id]` lets any signed-in user set `isPremium`, `subscriptionStatus`, `premiumUntil`, `role` (non-admin). Add an allowlist (`name`, `subjects`) and validate subject ids and count server-side.
- G2. Account deletion only records a request (`/api/me/delete`); no in-repo processor deletes data. Google Play requires in-app deletion plus a web URL for the same flow; an operator script and a web deletion page are needed, and the 30-day promise must be operationally real.
- G3. No profile or age fields in `public.users`. Age band lives only in `usage_consent` (self-declared). Product decision needed on age gating beyond analytics.
- G4. Push delivery: `/api/me/devices` stores tokens, but no sender, scheduler, quiet-hours enforcement or weekly-cap enforcement was found in the routes read. UNVERIFIED whether any exists. Local (on-device) notifications may be needed first.
- G5. Applying the migrations: commit `5fac96f` says migrations are saved only, not applied. If `usage_consent`, `usage_events`, `notification_prefs`, `push_devices`, `study_goals`, `account_deletion_requests` or the `insert_usage_events` RPC are not applied, the `/api/me/*` and `/api/events` routes will return 503. UNVERIFIED.
- G6. `/api/attempts` is an unpaginated, answer-bearing dump (everything per call). Add a slim list (id, subject, score, completedAt, mode) with paging.
- G7. `/api/leaderboard` publicly returns names, images and ids and scans all attempts per call; `/api/learning/summary` returns `topContributors` with other users' ids and names. Needs a privacy decision before showing either to students (under-18 audience).
- G8. `/api/learning/summary` streak is UTC and today-only; use `/api/me/rhythm` instead. Consider removing `streakDays` or aligning to IST.
- G9. `chapters` multi-select breaks for chapter names containing commas; accept an array or an id list.
- G10. Web paths in responses (`href`, `practiceHref`, `upgradeHref`, `delayedCheckHref`, insight `action.href`) are not a stable API. Either add structured fields (type, subject, chapter, mode) or freeze the parse rules in this contract.
- G11. Error envelope inconsistency; the client needs a per-route parser. A unified `{error:{code,message}}` would help.
- G12. `/api/analytics` returns `advanced` and `premiumMoves` to everyone (no Pro gate) and includes rank-readiness heuristics.
- G13. `/api/study/summary` response shape and the questions routes (feed, explore, vote, interact, pending) were not read in detail here; read before using them.
- G14. No per-answer feedback endpoint for practice (B13) and no server finalise at expiry for durable sessions (B11, blocker for mocks): see 2.7.
- G15. The rhythm response lacks closed-week history, repairs and mocks this week, and a stable last-closed-week id (B2 extension): see 2.3.
- G16. `attemptOut` has no `formatId`, and the mock ordinal and first-mock logic must use `selectionMeta.mode` (full or nta) because the attempts list includes Quick practice (B8).
- G17. Practice credits (100 on creation, Quick 10, Full 50) have no scheduled refill in the code read; whether they should refill is an owner decision. The only free paths are the quote allowances (`daily_practice`, `baseline:<subject>`, `full_sample:<subject>`).

Verification and decisions pending (UNVERIFIED):
- Q1. Is `LEARNING_SESSIONS_ENABLED` on in production (durable vs ticket)? Changes resume, sync and loss behaviour.
- Q2. Supabase email OTP length (8) and which `verifyOTP` type succeeds for new vs existing users; whether requesting a new code invalidates the earlier one.
- Q3. Google native sign-in configuration (Web and Android client IDs, nonce setting, SHA-1/SHA-256 for debug and Play App Signing keys).
- Q4. Are `PERSISTENT_LIMITS_ENABLED` and `ANDROID_CERT_SHA256` set in production?
- Q5. Real DB chapter names vs `data/canonical_syllabus.js`; the static fallback equals canonical for the 15 supported subjects, but DB contents are not visible.
- Q6. The app does not sell in v1; the Pro offer and 99-rupee plan can only be displayed informationally unless Play Billing is added.
- Q7. Whether the owner wants the app to enforce NTA exam integrity or leave it web-only.
- Q8. Android App Link intent filters for the emailed web link (currently the code is the only reliable path).

Client-side pitfalls to remember: send integer `at` with monotonic time; reuse `generationKey`, `requestKey` and `requestId` across retries; never display raw 422 parser messages; branch on `error` codes not messages; stop analytics the moment consent is off.
