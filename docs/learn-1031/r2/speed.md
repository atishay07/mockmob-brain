# Speed audit, round 2 (LK28: "the phone website and the website are slow")

1 Nov 2026, branch web/1031-learn-v2. Read-only audit: no code changed, nothing deployed, no database touched.

## What was measured

| Measure | How | Result |
|---|---|---|
| Live floor per API call | `curl` from this PC (India) to www.mockmob.in, 3 runs each, signed out | Route `bom1::sin1` (edge Mumbai, function Singapore). An empty 401 from `/api/auth/me` or `/api/learning/summary` takes **0.20 to 0.25 s** warm. That is the cost of *one* call before any database work. |
| Cold start | same | `/api/learn/covers` 401: **1.41 s** first call, 0.29 s and 0.20 s after. A signed-out `/api/questions/feed?subject=accountancy&limit=10`: **1.19 s** cold, 0.60 s, 0.41 s warm. |
| `/api/stats` caching | `curl -I` | `Cache-Control: public, max-age=30`, `X-Vercel-Cache: MISS`, `Age: 0`: the CDN does not keep it; every visit runs the function and the persistent rate-limit RPC. |
| `/learn` HTML | `curl` | 39 KB, TTFB **0.22 to 0.37 s** every time: server-rendered on demand, although the page is a client shell. |
| Home on a phone | DevTools performance trace, 390 px, 4x CPU, Fast 4G, cold cache (trace: `tmp/speed/home-mobile-trace.json.gz`) | LCP 1,060 ms (TTFB 31 ms, render delay 1,029 ms). **14 render-blocking CSS files**, the slowest done at 640 ms. 17 CSS files = 531 KB decoded (121 KB on the wire); 15 JS files = 867 KB decoded (271 KB). HTML 311 KB decoded. DOM 2,926 elements; one layout pass 217 ms; style recalc 79 ms. |
| Lighthouse | chrome-devtools `lighthouse_audit` | This tool's Lighthouse **excludes the performance category**, so the trace above stands in for it. |
| Client bundles | `next build --webpack` (Next 16 prints no First Load table any more; measured by reading each route's HTML on `next start` and gzipping the referenced chunks; `.next` left in place) | JS (gzip, incl. 39 KB `nomodule` polyfills that modern phones skip): `/today` **400 KB** (29 files), `/learn` **366 KB** (27), `/explore` 316 KB (22), `/learn/run` and `/explore/run` 251 KB (16), `/` 286 KB (17). CSS: 94 to 115 KB gzip, **460 to 560 KB decoded**, 18 to 26 files, on every app page. |
| Production regions | `vercel.json`, STATUS 15 Oct | Functions `sin1`; Supabase `isrxrxzjocewrdureyhp` is ap-southeast-1. Co-located (right). The phone pays Mumbai to Singapore on **every** call, so the lever is fewer calls and fewer sequential database trips, not a region move. |

The production logs' numbers (`/api/learning/summary` about 906 ms, `/api/questions/feed` about 967 ms from bom1) match: 0.2 s floor + several sequential Supabase trips + wide rows, worse when cold.

## The shape of the problem in one line

A signed-in hard load of Learn is a five-step waterfall: HTML (0.3 s, dynamic) -> 366 KB JS -> the Supabase client chunk is fetched and awaited -> `/api/auth/me` (four sequential database reads) -> then the page's own reads, three of which rebuild the same per-subject snapshot. The whole shell shows "Loading your session..." until step four ends. On a Rs 12,000 phone on 4G that is 2.5 to 4 s before the student sees anything they can tap.

## Ranked fixes (biggest expected gain first)

### 1. The whole app waits for `/api/auth/me` behind a lazy chunk. Gain: 400 to 900 ms on every hard load of every app page

- **Surface:** every signed-in page (Today, Practice, Learn, Explore, runs). The screens in `tmp/learn-1101/r2-before` (for example `30-home-top-390-night.png`, `01-explore-covers-390-night.png`) are what a student sees only after this wait; before it, `AppLayoutClient.jsx:340-343` draws "Loading your session...".
- **What is wrong:** `AuthProvider.jsx:188-201` does, in sequence: dynamic `import('@/lib/supabase-browser')` (chunk `7839`, 155 KB raw / 43 KB gzip, fetched only after hydration) -> `readSession` (may refresh the token against Supabase Auth, another Singapore round trip) -> `fetchMe()`. The server cookie is already enough for `/api/auth/me`; nothing needs the browser client first. Then `/api/auth/me` itself (`src/app/api/auth/me/route.js`) runs `authWithStatus` -> `getUserById` -> `getUnifiedWallet` -> `getPlaySubscription` -> `pendingDeletionAt`, each awaited one after another.
- **Why it matters:** LK28 directly. A first-timer reads "Loading your session..." as "this app is slow" before seeing a single card.
- **Fix:**
  1. In `checkSession`, when `hasSessionCookie()` is true, start `fetchMe()` at once and load the Supabase client in parallel (`Promise.all([fetchMe(), getSupabaseBrowserClient().then(readSession)])`); only the 401 branch needs the client (refresh then retry).
  2. Keep the last good `me` in `localStorage` under `mm:me:v1` as `{ id, at, me }` (try/catch, dropped on sign-out and on a different cookie user). On boot with a session cookie and a cached `me` less than 7 days old, set `status = 'authenticated'` with it immediately and revalidate in the background; a 401 then signs out as today. Credits and plan refresh from the live answer within a second.
  3. In `/api/auth/me`, run `getUnifiedWallet(dbUser)`, `getPlaySubscription(dbUser.id)` and `pendingDeletionAt(...)` in one `Promise.all` (they only need `dbUser`).
- **Files:** `src/components/AuthProvider.jsx`, `src/app/api/auth/me/route.js`, `src/app/(app)/AppLayoutClient.jsx` (no change to the gate, it just opens sooner).

### 2. Explore pays the slowest route in the logs (`/api/learning/summary`, ~906 ms) for a line it never shows. Gain: one 0.9 s call and its egress removed from every Explore visit

- **Surface:** Explore (`01-explore-covers-390-night.png`: covers, then Questions).
- **What is wrong:** `src/components/feed/DiscoveryFeed.jsx:132` calls `/api/learning/summary?subject=` and line 143 reads `summary.data?.solvedTotal`. The live route returns it nested, `progress.solvedTotal` (`src/app/api/learning/summary/route.js:184`), so `solved` is always `undefined` and the "N questions solved in your recorded untimed practice" line (lines 219, 253) never renders on the live site. The preview hides the bug: its fake answers a flat `{ solvedTotal: 7 }` (`ArenaPreviewClient.jsx:714`). Meanwhile the route reads every attempt with its `details` array, every `user_question_progress` row, every bookmark and a 500-row contributors sample (memoised), behind `auth` -> `getUserById` in sequence.
- **Why it matters:** LK28; also LK24 and LK31 (less text): the line is a sentence nobody needs on Explore.
- **Fix:** delete the summary read and the `ex-record` line from Explore (lines 126-138, 143, 219, 253). If the owner wants the count back later, it belongs on Progress, which already has it.
- **Files:** `src/components/feed/DiscoveryFeed.jsx`, `src/app/preview/arena/ArenaPreviewClient.jsx` (drop the fake so preview equals live).

### 3. Learn home builds the same heavy snapshot three times. Gain: 2 function calls and about 40 database queries fewer per visit; home complete 300 to 600 ms sooner

- **Surface:** Learn home (`30-home-top-390-night.png`: subject strip with "9 due / 6 due", the three counts 9 / 6 / 26, the Pick up card).
- **What is wrong:** on `/learn` three calls run: the shell's badge `useLearnDue` -> `/api/learn/shelves` (no subject, `AppLayoutClient.jsx:104`, `api.js:152`), and the home's `/api/learn/subject` plus `/api/learn/shelves?subject=` (`LearnHome.jsx:161,165`). Each passes the persistent rate-limit RPC, `who()` (a fresh `users` read) and `snapshot()` (`learn.js:169`): 11 parallel reads, then `shownCards` and `mistakePlaces` in sequence. `shelves` adds `kc.dueCount` (`keycards.js:534`: `who`, `loadStates`, `published`, `loadOptions` again) and one `store.states` per other subject.
- **Fix:** one `GET /api/learn/home?subject=` that returns `{ ...subject body, shelves }` from a single `snapshot`, with `due.all` computed as the sum of `bySubject` (no second `dueCount`). The shell badge reads the same answer through a tiny module cache (`learnHomeCache: Map<subject, { at, promise }>`, 30 s), so on `/learn` and `/explore` it costs nothing extra; elsewhere it still calls once. Keep `/subject` and `/shelves` for the app.
- **Files:** `src/lib/server/learn.js` (new `home()`), `src/app/api/learn/home/route.js` (new, `learnHttp`), `src/components/learn2/api.js`, `src/components/learn2/home/LearnHome.jsx`, `src/app/(app)/AppLayoutClient.jsx`; contract line in `docs/brain/learn-1031/API-CONTRACT.md`.

### 4. Today makes about 13 separate function calls and lands "in one piece", so it waits for the slowest. Gain: first paint of Today from ~1.5 to 2.5 s to ~0.6 to 0.9 s after auth

- **Surface:** Today.
- **What is wrong:** `useToday.js:78-86` fires plan, papers, rhythm, goal, road, revise, timed-mock, repair-record; plus `useInsights` (`/api/prepos/insights`), `useMob` (`/api/mob`), the Revise badge (`/api/me/review`), the daily set and first-mock reads, plus `/api/auth/me`. Every one re-runs `auth()` and most re-read `users`. Each pays the 0.2 s floor, and ten at once on a cold deployment wake several cold instances (1.4 s each). The page header says it "lands in one piece (W-042)", so the slowest call sets the time.
- **Fix:** `GET /api/today` that authenticates once, reads the user once and runs the eight reads in one `Promise.all`, returning the same eight shapes (`{ plan, papers, rhythm, goal, road, revise, facts, record }`); `useToday` keeps its per-key `refresh` by calling the old routes. Insights and Mob stay separate and render into their own slots when they land (they are below the fold).
- **Files:** `src/app/api/today/route.js` (new), `src/components/today/useToday.js`, `src/app/(app)/today/page.jsx`.

### 5. Every Learn call has 3 to 4 needless sequential steps. Gain: 60 to 150 ms per Learn call (covers, subject, shelves, cards, search, preview, start)

- **What is wrong:** `learnHttp.js:122` awaits the persistent rate limit (a Supabase RPC) before any work; `who()` (`learn.js:147`) is awaited before `snapshot()` starts; inside `snapshot()` `shownCards` (line 207) and `mistakePlaces` (line 210) run one after the other after the 11-way `Promise.all`; `covers()` then reads each open feed's run and events (line 1194).
- **Fix:** (a) for GETs, run `checkPersistentRateLimit` in parallel with the handler and return 429 if it refuses (reads have no side effects); keep it first for POSTs. (b) Start `getUser(userId)` inside the same `Promise.all` as the snapshot reads (`snapshot` only needs `me` after the reads). (c) Run `shownCards` and `mistakePlaces` together in one `Promise.all`.
- **Files:** `src/lib/server/learnHttp.js`, `src/lib/server/learn.js`.

### 6. Cold Learn instances read a whole subject's question pool page by page before answering. Gain: cold Learn calls from ~1.5 to 3 s to ~0.5 s

- **What is wrong:** `learnService()` (`learnHttp.js:83`) on a new instance: `keycardsService`, the syllabus, `loadDecks` (6.2 MB of JSON, 5,806 cards, `readFileSync` + `JSON.parse`: 30 ms on this PC, ~80 ms on a function) and then, per subject, `buildIndex` -> `loadLightPool` (`data/practice_source.js:80`): a count, the light pool in 1,000-row pages **one after another**, and the managed ids for two columns, also paged one after another, then `readable()`. Cached 5 minutes per instance only, so each new instance and each idle gap pays it again. The 1.41 s cold 401 shows the cold cost even before this.
- **Fix:** (a) build each subject's Learn question index once a day in the existing 21:30 UTC inventory cron and store it (one row per subject in a new `learn_question_index` table, or a JSON file in Storage), read with one query; fall back to today's path when missing. (b) Until then, fetch the pool pages in parallel once the count is known (`Promise.all` over `ceil(count/1000)` ranges). (c) Owner action: turn on Fluid compute for the project in Vercel (instance reuse cuts cold starts); say so in the handover, do not change settings from an agent.
- **Files:** `src/lib/server/learnHttp.js`, `data/practice_source.js`, `src/app/api/internal/refresh-inventory/route.js`, a migration plus undo under `supabase/` (dry-run first, per AGENTS.md).

### 7. `/api/questions/feed` reads wide rows and authenticates after the query. Gain: 150 to 300 ms per page of Explore questions

- **Surface:** Explore's Questions list (bottom of `01-explore-covers-390-night.png`).
- **What is wrong:** `select('*')` on `questions` (every column, including the evidence and provenance JSON), then `attachBankPassages`, then `readablePracticeQuestions`, then `auth(request)` (line 107), then `getUserVotes`, then the bookmarks read: six steps in a row.
- **Fix:** start `auth(request).catch(() => null)` at the top as a promise; select only the columns the response maps plus what `readablePracticeQuestions` needs to judge readability (list them once as `FEED_COLUMNS`); run votes and bookmarks in one `Promise.all`. For signed-out readers add `CDN-Cache-Control: public, s-maxage=300` (no per-user fields then).
- **Files:** `src/app/api/questions/feed/route.js`, `data/practice_library.js` (confirm the columns it reads).

### 8. 460 to 560 KB of CSS blocks the first paint of every page. Gain: 150 to 400 ms first paint on a mid phone

- **What is wrong:** the root layout imports `globals.css` (110 KB), `marketing-theme.css`, `brand-pip.css` (32 KB), `brand.css`, `app-view.css` for every page; the home adds 12 more files (`lab-cinema.css` 47 KB, `motion-kit.css` 38 KB, `landing.css` 36 KB and so on); the app shell adds 8. The home trace shows 14 render-blocking CSS requests, the slowest finishing at 640 ms on Fast 4G; app pages carry 18 to 26 CSS files.
- **Fix:** move `marketing-theme.css` and `brand-pip.css` out of `src/app/layout.js` into the home page and the marketing pages that use them; split `globals.css` into tokens + base (root) and the rest into the pages that use it. Target: an app page at or under 150 KB of CSS decoded, under 10 files. Check with the same HTML script (`tmp/speed/` notes) after the move.
- **Files:** `src/app/layout.js`, `src/app/globals.css`, `src/app/page.js`, the marketing pages.

### 9. App pages are server-rendered on every request though they are client shells. Gain: 200 to 300 ms TTFB on every hard load

- **What is wrong:** `src/app/(app)/layout.js` calls `await connection()` only to read four env flags at request time; `/learn` also awaits `searchParams` on the server. Measured TTFB of `/learn` 0.22 to 0.37 s; a CDN-served page answers in ~0.03 to 0.05 s (home: 31 ms in the trace).
- **Fix:** read the flags at build time (`NEXT_PUBLIC_STUDY_ENABLED`, `NEXT_PUBLIC_MOB_ENABLED` and so on, set in Vercel; a change takes a redeploy, as `FIRST_FULL_MOCK_ENABLED` already does) and drop `connection()`; read `?subject`, `?find`, `?recall` with `useSearchParams` inside the existing `Suspense`. Read `node_modules/next/dist/docs` on static rendering in Next 16.2 before changing it.
- **Files:** `src/app/(app)/layout.js`, `src/app/(app)/learn/page.jsx`, `src/app/(app)/learn/params.js`, `next.config.mjs` (`env`).

### 10. No client cache: going back to Learn or Explore reloads everything. Gain: return visits show content at once instead of after 300 to 900 ms

- **What is wrong:** `components/learn2/api.js` `call()` uses `cache: 'no-store'` and `useLearnRead` starts from `{ status: 'loading', data: null }` on every mount. Coming back from a run to the home or Explore draws the skeleton again.
- **Fix:** a module-level `Map<url, { at, data }>` in `api.js`; `useLearnRead` starts from the kept data (status `refreshing`) when it is under 5 minutes old and revalidates; writes (start, answer, rate, end) clear the keys for that subject. Same for Explore's covers.
- **Files:** `src/components/learn2/api.js`, `src/components/learn2/feed/ExploreCovers.jsx`.

### 11. `/api/stats` is not cached at the edge. Gain: 100 to 200 ms on the home's numbers, plus one function and one RPC per visitor

- **What is wrong:** `Cache-Control: public, max-age=30` is answered `X-Vercel-Cache: MISS`, `Age: 0`; Vercel's CDN needs `s-maxage` (or `CDN-Cache-Control`). The counts change once a day (21:30 UTC cron).
- **Fix:** add `CDN-Cache-Control: public, s-maxage=3600, stale-while-revalidate=86400` to the 200 answer; keep `no-store` on the 503.
- **Files:** `src/app/api/stats/route.js`.

### 12. Explore starts with a needless `/api/subjects` step. Gain: 150 to 250 ms to the first cover

- **What is wrong:** `DiscoveryFeed.jsx:57-84` reads `/api/subjects`, and only then the chapters, the questions and the covers start. The student's subjects are already in `useAuth().user.subjects`.
- **Fix:** pick the first of `user.subjects` (or the remembered one) at once and start covers and questions; let `/api/subjects` only correct the list when it lands.
- **Files:** `src/components/feed/DiscoveryFeed.jsx`.

### 13. Two blurred fixed layers repaint on every scroll frame on phones. Gain: smooth 60 fps scrolling on low-end Android (no ms on load)

- **Surface:** the top bar and the floating dock on every app screen (`30-home-top-390-night.png`, `01-explore-covers-390-night.png`, the "Today / Practice / Start / Mob / You" dock).
- **What is wrong:** `arena.css:314-315` gives the top bar `backdrop-filter: blur(18px) saturate(1.2)`; `arena.css:1689-1690` gives the dock `blur(32px) saturate(1.5)`. Both are `position: fixed` over scrolling content, so each scroll frame re-samples and blurs two regions. On Mali/Adreno 5xx-class GPUs this drops frames; the owner's "a bit slow" on the phone can be this as much as the network.
- **Fix:** below 768 px and on `(hover: none)`, use the solid tokens (`background: var(--dock-solid)`, `backdrop-filter: none`) with the existing 1 px top line; keep the glass from 768 px up. It already exists as a fallback at `arena.css:1669` and `1746`; make it the phone default.
- **Files:** `src/app/(app)/arena.css`.

### 14. Mobi's rig ships in every app page's first load. Gain: ~28 KB gzip and 100 to 200 ms of parse at 4x CPU

- **What is wrong:** chunk `7222` (91 KB raw, 28 KB gzip: `mobiRig.js`, `mobiSim.js`, `mobiPaint.js`, with the pose tables "bump, tilt, squash, stance") is in the first load of `/learn`, `/today`, `/explore` and `/`.
- **Fix:** draw Mobi's still image first and load the rig with `next/dynamic(..., { ssr: false })` after `requestIdleCallback` (fallback `setTimeout(…, 1200)`); a tap on Mobi before it loads triggers the import and plays once loaded.
- **Files:** `src/components/brand/Mascot.jsx`, `src/components/brand/MobiReact.jsx`, wherever the shell mounts Mobi.

### 15. The home page is heavy on the main thread. Gain: 150 to 250 ms of main-thread time on a mid phone

- **What is wrong (trace):** DOM 2,926 elements; one layout of 217 ms; 311 KB of HTML; `ExamComparator.jsx:97` renders 50 number cells (`.lp-exam__numbers`, 50 children).
- **Fix:** `content-visibility: auto; contain-intrinsic-size: auto 900px` on each home section below the hero; render the exam comparator's 50 cells as 10 visible plus a CSS background pattern for the rest. Coordinate with the LK32 hero work (less space, more brand) so the hero stays light.
- **Files:** `src/app/home-refinements.css`, `src/components/landing/ExamComparator.jsx`, `src/app/landing.css`.

### 16. `/api/learning/summary` (still used by Dashboard) reads every attempt's answers. Gain: 200 to 400 ms on Dashboard

- **What is wrong:** `getAttempts(..., { columns: [..., 'details', ...] })` with no limit, every progress row, auth then `getUserById` then the reads.
- **Fix:** run `getUserById` inside the `Promise.all`; compute answered/correct per attempt in SQL (a `slim` read through `data/attempt_reads.js`, which already supports `'summary'`; check whether it carries answer counts and extend it if not, migration plus undo first) instead of shipping `details`.
- **Files:** `src/app/api/learning/summary/route.js`, `data/attempt_reads.js`.

### 17. `published()` copies 5,806 cards into a new Map on every call. Gain: 5 to 20 ms CPU per Learn request (small, cheap)

- **What is wrong:** `keycards.js:144` builds `new Map([...decks.byId].filter(...))` each call; Learn calls it from `snapshot`, `dueCount`, `contentOf`, `hydrateAnswer`, so two to four times per request; `taste()` then walks all cards.
- **Fix:** memoise the result by the suspended set (already cached `REPORT_TTL_MS`, 5 minutes): rebuild only when that set changes.
- **Files:** `src/lib/server/keycards.js`.

### 18. Motion details in Learn that touch layout. Gain: no load time; removes small hitches on low-end phones

- `cards.css:48` animates the chips indicator's `width` for 240 ms: use `transform: scaleX()` with `transform-origin: left` and a fixed width.
- `stage.css:209` `.st-lineopen` animates `grid-template-rows` (layout) 240 ms after 180 ms: fine once per wrong answer, but keep it the only layout animation in the stage.
- Checked and fine: the pager moves one track with `translate3d` and `will-change: transform` (`usePager.js:30-31`, `stage.css:29`), the card turn is a transform, no blur inside Learn, the 671 KB chunk `5420` is the preview's fixtures only (not in production pages), and the Key card decks never reach a production client bundle.

## What not to do

- Do not move functions to `bom1` alone: the database stays in Singapore and every query would then cross the sea (5 to 15 trips per request). Fewer calls (items 1, 3, 4) is the real cure for the Mumbai to Singapore hop.
- Do not add a service worker or prefetch-everything: the waste is in the waterfall and repeated snapshots, not in caching static files (they are already `immutable`).

## Proof each fix worked (for the builder)

- Hard load of `/learn` on a 390 px phone profile (4x CPU, Fast 4G) signed in: time to the first subject row, before and after items 1, 3, 9 (target under 1.5 s).
- Count of `/api/*` requests on `/today` and `/learn` (DevTools network): target 3 or fewer on each.
- `curl -I https://www.mockmob.in/api/stats` twice: the second answers `X-Vercel-Cache: HIT`.
- Vercel logs: `/api/learn/*` p50 under 300 ms, `/api/questions/feed` under 400 ms; no `/api/learning/summary` calls from Explore.
