# Why MockMob went over the Vercel and Supabase free limits

15 Oct 2026, about 20:15 IST. This was a read-only check: nothing was changed, paused, deleted or deployed.

## The short answer

Real students did not cause this. Only 8 practice attempts were completed in the last three weeks, and only 9 accounts signed in during the last 30 days.

The usage came from our own code and our own machines:

1. **The question-count feature copies the whole question bank.** It shows "how many questions per subject" on the home page, dashboard and practice screen. Each time it refreshes, it downloads all 9,697 questions with every column, about 41 MB. In the last 24 hours that happened 26 times, about 1.1 GB.
2. **The same feature burned Vercel's compute allowance.** From 4 to 13 Oct it also re-read two large files (4.9 MB) once for *every question*. Each request ran until Vercel killed it at 300 seconds. Vercel logged 59 of those kills between 7 and 13 Oct. That adds up to as much as 4.9 hours of compute, against a monthly Hobby allowance of 4 hours. This was fixed on 13 Oct for the counts. The same slow pattern still exists in 5 other places.
3. **Our own computers test against the live database.** Agents and local dev servers in 8 worktrees use the production database. About 3,000 of the 3,700 database requests in the last 24 hours came from this PC's internet connection (Airtel), not from students.

The free plans can last through testing once these are fixed (section 4). One thing they cannot cover is commercial use: Vercel's free plan is for non-commercial projects only, and MockMob takes payments.

Terms used below:

- **Egress:** data sent *out* of Supabase to whoever asked for it.
- **Function:** a piece of our server code that Vercel runs for one request.
- **Active CPU:** time Vercel's servers spend actually computing, not waiting.

---

## 1. Which limits were exceeded, with the numbers

### Supabase (Free plan, organisation "mockmob")

| Meter | Free allowance | What I measured | Over? |
|---|---|---|---|
| **Egress** (shared by production *and* staging) | 5 GB per billing month | 2.28 GB already used on 7 Oct (dashboard capture); about 1.1 GB per day now (26 whole-bank copies of about 41 MB each in the last 24 h) | **Yes. This is the limit you hit.** |
| Database size | 500 MB per project | Production 157 MB, staging 92 MB | No |
| File storage | 1 GB | 0 files in production | No |
| Monthly active users | 50,000 | 9 signed in during the last 30 days; 1,639 accounts in total | No |

The timeline fits your "5 or 6 days ago":

- 2.28 GB had been used by 7 Oct.
- Before 13 Oct, the count refreshed on almost every request, and failed requests were never remembered, so they retried.
- That pace passes 5 GB around 8-10 Oct.

What happens next, from Supabase's billing FAQ:

- **Grace period.** You first get a grace period.
- **Restrictions.** After it, Supabase can restrict every project in the organisation. That can mean API requests answered with error 402, the database switched to read-only, or projects paused. It applies to staging too.
- **Already counted.** Usage already counted this month stays counted, even after a fix.
- **Restrictions lift** when the billing month resets, or immediately if you upgrade.
- **No second grace period.** Once a grace period has ended, the next overage is restricted immediately with no new grace period.

So the fixes must be live before the next billing month starts. The reset date is on the Supabase Billing page under "Upcoming invoice". I could not read it with the tools I have.

### Vercel (Hobby plan, team "atishay07's projects")

Vercel does not let these tools read Hobby usage numbers. Its usage and metrics API needs the paid "Observability Plus", and billing data returned "not found" for a Hobby team. So the meter below is my **best-evidence conclusion, not a reading from the Usage page**. Please confirm it on Vercel under Settings, then Usage.

| Meter (Hobby allowance, per 30 days) | Evidence | Verdict |
|---|---|---|
| **Active CPU: 4 CPU-hours** | Vercel's error log shows **59 requests killed at 300 seconds** ("Task timed out after 300 seconds"), from **26 different users**, on `/api/practice/quote` and `/api/stats`, from 7 Oct 11:06 IST to 13 Oct 10:20 IST. The work was CPU-bound file parsing, so this is up to 59 × 300 s ≈ **4.9 CPU-hours**. That is more than the whole monthly allowance, from one bug. (It is "up to" because requests sharing one server share its CPU.) | **Almost certainly the one you hit** |
| Provisioned memory: 360 GB-hours | The same 59 requests come to about 10-20 GB-hours | Probably fine |
| Function invocations: 1,000,000 | Traffic is tiny | Probably fine |
| Fast Data Transfer: 100 GB; CDN requests: 1,000,000 | Traffic is tiny; the whole `public/` folder is 14 MB | Probably fine |
| Image transformations: 5,000 | Only 2 components use Next's image optimiser, on about 24 small images | Fine |

What Vercel says happens on Hobby:

- **Waiting period.** After you exceed a limit, "you will have to wait until 30 days have passed before you can use the feature again".
- **Pausing.** The account "may be paused".
- **Current state.** At 20:00 IST today the site was still answering: `/api/stats` returned 200 in 0.5-1.6 s. So nothing is paused yet.

---

## 2. The causes, ranked

### Cause 1. The question-count feature downloads the whole bank (Supabase egress, and Vercel CPU)

- **Where it happens.** `src/lib/server/inventory.js` line 17 reads every non-deleted question with all columns (`select('*')`), 1,000 at a time.
- **What it was before.** Until the 13 Oct deploy, it ran inline on every request to `/api/stats` and `/api/practice/quote`, with only a 60-second memory per server.
- **What it does now.** It serves a stored snapshot, but it starts a full refresh in the background whenever the snapshot is more than 15 minutes old (`inventorySnapshot.js` line 3). Any visit at least 15 minutes after the last refresh therefore costs a full copy.
- **Who calls it.**
  - The home page (`LiveStatsBand.jsx` line 82).
  - The dashboard (`DashboardPageClient.jsx` line 118), and the practice quote, which refires on every subject, mode or count change (line 211).
  - The app's Practice tab: 3-4 quotes and 1 stats call.
  - The daily cron.
- **Size of one copy.** 9,697 rows ≈ **41 MB** as JSON. Of that, 23.5 MB (55%) is the `evidence` column, carried by only 666 questions at about 35 KB each.
- **Last 24 hours (Supabase gateway logs).** **26 full copies, about 1.1 GB.**
  - 14 came from this PC's Airtel connection (local dev servers refreshing every 15-20 minutes while agents worked on website v2, 10:10-14:05 UTC).
  - 12 came from Vercel's servers in Virginia. That includes one after each deploy, when Vercel's own check bot loads the new home page.
- **Since April.** The database's own counters show 7,297 whole-table pages read, which is about **730 full copies of the bank** (roughly 25-30 GB before compression). The code that does this went live on 4 Oct.
- **Compression caveat.** Supabase may compress responses, so billed bytes could be 3-6 times smaller than these raw sizes. Even then, 26 copies a day is more than 5 GB a month.

### Cause 2. The evidence check re-reads 4.9 MB of files for every question (Vercel Active CPU)

`publicationEligibility()` in `data/evidence_registry.js` reads and parses `calibration_manifest.json` (2 MB) and `source_registry.json` (2.9 MB) every time it is called, unless the caller passes a snapshot. Measured on staging, that is about 37 ms per question. For roughly 9,000 questions it comes to about 330 s, which is past Vercel's 300 s limit. That produced the 59 timeouts.

- **Fixed for the counts.** The 13 Oct deploy (commit 52de7fe5) fixed it for the counts only. On 535 questions, time went from 19,650 ms to 83 ms, with identical verdicts.
- **Still slow in 5 places**, each doing it once per question:
  - `src/services/recovery/answerReviews.js:16`: every result page (`GET /api/attempts/[id]`). The Android app also calls this route on resume, as an existence check.
  - `src/services/recovery/mistakeRepair.js:48`: Mistake Repair.
  - `src/lib/server/learning.js:43`: the learning plan.
  - `src/app/api/sessions/[id]/check/route.js:39`.
  - `data/db.js:1539`.

A 50-question NTA result therefore parses about 245 MB of JSON, which is seconds of CPU per view.

### Cause 3. Our own computers use the production database

Eight local worktrees point at production in `.env.local`:

- `mockmob copy`
- `mockmob-backend`
- `mockmob-hotfix`
- `mockmob-next`
- `mockmob-web2`
- `wt-repair`
- `wt-web-refine`
- `wt-web-v2`

Every local dev server, test run and agent browser check therefore spends the production allowance.

- **Last 24 hours.** About **3,000 of the roughly 3,700 Supabase requests (80%)** came from the Airtel connection, and 14 of the 26 whole-bank copies.
- **Right now.** At the time of the check, two local Next.js servers were running: port 3110 from `mockmob-hotfix`, and port 3143.
- **Live site too.** Vercel's logs for the last hour show `/api/stats` on the live site being called every 30-60 seconds from one Airtel address range, which is very likely agents checking pages.

### Cause 4. Starting a practice session downloads the whole subject (small today, the biggest risk at launch)

`data/db.js` lines 1122-1150 (`getQuestions`) page through **every** matching question in the subject, with all columns including `evidence`. That happens for each session start. The `poolSize` it computes is never used.

The Commerce subjects are the heaviest:

| Subject | Visible questions | One session start downloads | Without the evidence column |
|---|---|---|---|
| Accountancy | 1,405 | ~8.0 MB | ~2.6 MB |
| Business Studies | 422 | ~7.1 MB | ~0.9 MB |
| Economics | 466 | ~6.9 MB | ~1.0 MB |
| English | 384 | ~6.0 MB | ~0.9 MB |

- **Today.** There were only 5 such reads in the last 24 hours.
- **At launch.** 5 GB is about **700 Commerce session starts a month**. Twenty testers doing two sessions a day would exceed it from this alone.
- **NTA papers.** These have a slim path, but it needs the `nta_question_index` table, which **is not in production**. NTA papers therefore take the full-column read too.

### Cause 5. Vercel runs our server code in the USA while the database is in Singapore

- **Where each runs.** The live deployment runs functions in `iad1` (Washington DC; deployment `regions: ["iad1"]`). Supabase is in `ap-southeast-1` (Singapore). Supabase's logs confirm the calls arrive from "Amazon Data Services Northern Virginia".
- **The cost.** Every database call crosses the planet, roughly 200-250 ms each way and back. A page that makes 10 calls waits 2-3 seconds. That waiting is billed as memory-time, and it makes the site slow for students in India.
- **Why.** `iad1` is Vercel's default. Hobby allows choosing any one region.

### Cause 6. Five duplicate Vercel projects built every push (until 14 Oct)

- **What happened.** `mockmob-1uhb`, `-mmzs`, `-nxud`, `-pf37` and `-sjsj` are connected to the same GitHub repo. On 13-14 Oct each of them built every push to `main`: **50 extra builds in two days**, and each production copy also had the two daily crons.
- **Now.** They were paused on 14 Oct and show "BLOCKED" on every push since. They cost little now, but they are still connected.

### Cause 7. Smaller multipliers (each modest, together worth fixing)

- **`/api/stats` is never cached by Vercel's CDN.** Its header has `max-age` but no `s-maxage`, so every call runs the function. It is also marked force-dynamic, and writes a rate-limit row when that feature is on.
- **The web test page sends the whole event log every 1.5 seconds** (`TestPageClient.jsx:504`), even when nothing changed. That is about 40 server calls a minute per running test when server sessions are on.
- **About 24 MB of NTA score JSON loads into almost every server route.** `data/db.js` imports `nta_pool`, which imports `nta_agent_scores`. The two 5 MB registry files are also bundled into every function (`next.config.mjs` `outputFileTracingIncludes '/*'`). The result is extra CPU and memory each time a server starts.
- **The Android app re-downloads all attempts after every submit** (`refresh(force: true)`), and the web dashboard does a full attempts dump. Per-user sizes are small today (under 1 MB).
- **`robots.txt` does not block private app pages** (`/today`, `/progress`, `/review`, and others), so a crawler visit triggers a full server render.
- **One-off scripts read the whole bank from production:** `nta-data-audit`, `nta-engine-run`, `nta-sample`, and the factory and audit npm scripts. On 7 Oct, a factory run also wrote 900 rows (46 MB) into production `question_factory_jobs`. That is now the largest table, 29% of the database, but the database is still well under its limit.

---

## 3. Fixes, ranked by savings and risk

### A. Safe: an agent can do these (code or config). Deploying needs your usual OK.

| # | Fix | What it saves | Risk |
|---|---|---|---|
| A1 | **Counts refresh only once a day.** Remove the "refresh after 15 minutes" step in `src/lib/server/inventory.js` (`scheduleRefresh` / `after()`). Serve the stored snapshot; let only the daily cron refresh it; never refresh outside Vercel production (`VERCEL_ENV !== 'production'`). | About 25 of 26 whole-bank copies a day: **about 1 GB a day, roughly 90% of current Supabase egress**. It also removes the CPU spike for good. | Low. Counts can be up to a day old, which is fine for "N questions" labels. |
| A2 | **Read the two evidence files once per server, not once per question.** Cache the parsed files in memory (they ship with the deployment and cannot change while it runs) and use that in the 5 places listed in cause 2. | Seconds of CPU per result page, repair, plan and check become milliseconds. This protects the 4 CPU-hour allowance. | Low. It is the same change already proven on 13 Oct, with identical verdicts on all 666 evidence rows. |
| A3 | **Move Vercel functions next to the database.** Add `"regions": ["sin1"]` (Singapore) to `vercel.json`. | Each database call drops from about 220 ms to a few ms. Pages get faster for Indian students, and less memory-time is billed. | Low. It is one config line. Watch the first deploy. |
| A4 | **No whole-bank reads from non-production machines.** Add a code guard: refresh and full-bank reads refuse to run when the server is not Vercel production. | It stops local dev servers burning production egress even if an `.env.local` still points at production. | Low. |
| A5 | **Lighter session start.** Read the light columns for the whole subject to rank and pick, then fetch full rows (with `evidence`) only for the 10-50 chosen questions. Optionally, keep each subject's pool in server memory for 5-10 minutes. | One Commerce session start goes from about 7 MB to well under 1 MB, roughly **10 times more sessions per GB**. This is the fix that matters most at launch. | Medium. It touches question selection. Run `test:recovery`, `test:nta`, `test:learning` and the question suites, and compare picks before and after. |
| A6 | **Apply the existing `nta_question_index` migration in production.** It is allowed under your 14 Oct database grant; follow its runbook. | NTA papers read slim columns instead of every column of the subject. | Low to medium. |
| A7 | **Let Vercel's CDN cache `/api/stats`.** Change the header to `public, s-maxage=300, stale-while-revalidate=3600` and skip the rate-limit write for it. | Most `/api/stats` function runs, from the home page, dashboard and app. | Low. |
| A8 | **Test-page sync sends only when something changed.** Send only events newer than the last saved one, and at most every 5 s (`TestPageClient.jsx:490-504`). | Up to about 90% of `PUT /api/sessions` calls during a test. | Low to medium. Re-run the session and resume tests. |
| A9 | **Load the 24 MB of NTA scores only on the NTA path.** Use a lazy import, and bundle the 5 MB registry files only into the routes that use them. | CPU and memory on every server start for every route. | Low to medium. |
| A10 | **Small clean-ups:** block private app pages in `robots.txt`; the app uses `/api/attempts/summary` instead of full re-downloads; the app's resume check uses a light call instead of the result route. | Small but steady savings. | Low. |

**Suggested order:** A1, A2, A3 and A4 first. They are small, low-risk and remove almost all of today's waste. Then A5 and A6, before inviting more testers.

### B. Owner actions (dashboard clicks and decisions)

1. **Confirm the exact meters, and the Supabase reset date.**
   - Vercel: Settings, then Usage.
   - Supabase: organisation Usage, and Billing under "Upcoming invoice".
   - I could not read these with the tools available. Alternatively, an agent can install the Vercel CLI and run `vercel usage` after you sign it in.
2. **Agree that local development and agent testing use staging (or a local database), not production.** That means switching the 8 `.env.local` files listed in cause 3 to staging `onwkqxmjqjrhfbjjdydu`. An agent can do the edit, but it changes how testing works, so it is your call. It removes about 80% of today's database requests.
3. **Delete the five paused duplicate Vercel projects**: `mockmob-1uhb`, `mockmob-mmzs`, `mockmob-nxud`, `mockmob-pf37` and `mockmob-sjsj`. At minimum, disconnect them from GitHub. Deleting is permanent, so it is your click.
4. **Give your OK to deploy A1-A4.** Deploys sit outside the 14 Oct database grant.
5. **Decide on the Vercel plan (section 4).**
6. Optional:
   - Move the staging Supabase project into its own free organisation, so factory runs on staging stop spending production's 5 GB. Egress allowance is per organisation.
   - Archive the 900 `question_factory_jobs` rows from 7 Oct in production (46 MB). This is not urgent, because the database is at 157 of 500 MB.

---

## 4. Can the free plans last through testing?

**Yes, once A1-A4 are live and agents stop testing against production.** Here is a rough monthly picture after the fixes, at testing scale:

| Item | Before | After |
|---|---|---|
| Question counts | ~26 copies/day ≈ 30+ GB a month (raw) | 1 copy/day ≈ 1.2 GB a month. Near zero later if each question's evidence verdict is stored once at publish time and counted in SQL. |
| Local dev and agent traffic | 80% of requests, 14 copies a day | 0 (moved to staging) |
| Session starts (say 20 a day) | ~4 GB a month | ~0.5 GB a month after A5 |
| Sign-in, profile, attempts, everything else | small | under 0.5 GB a month |
| **Supabase egress total** | **well over 5 GB** | **about 1-2 GB a month** |
| **Vercel Active CPU** | up to ~4.9 h from the timeouts alone | Normal requests use 10-100 ms of CPU. 4 CPU-hours then covers roughly 150,000 to 1.4 million requests a month, far above testing traffic. |

Two honest caveats:

- **Vercel Hobby is for non-commercial use only** (Vercel fair-use guidelines). MockMob takes payments; the payments table holds about 475 records. Vercel can pause a Hobby project for commercial use regardless of usage. Once paid plans are live for students, **Vercel Pro ($20 a month, one seat, includes $20 of usage credit)** is the compliant choice. It also gives 1-day logs and real usage numbers.
- **This month's Supabase usage is already counted.** The fixes stop new waste, but the current overage stays until the billing month resets. If restrictions start before then, the fastest unblock is Supabase Pro ($25 a month, with 250 GB egress, 8 GB database, daily backups and no pausing). It can be downgraded later.

### Cheapest path

1. **Now, $0:** ship A1-A4, move testing to staging, and delete the duplicates. Wait for the Supabase reset if no restriction hits first.
2. **Before more testers:** ship A5 and A6.
3. **At public launch with payments:** Vercel Pro, $20 a month. Stay on Supabase Free while egress stays under about 3 GB a month. Move to Supabase Pro, $25 a month, when you need backups and headroom, or when daily active students reach the hundreds.

### Alternatives, with honest trade-offs

- **Cloudflare Workers (paid plan, about $5 a month) using the OpenNext adapter for Next.js.**
  - **Cheaper and generous on requests.** But it is not a drop-in move for this app.
  - **Files and bundle size.** Our server code reads JSON files from disk at runtime (`readFileSync`) and bundles about 24 MB of JSON. Workers have no normal disk and cap the compressed code size at about 10 MB on the paid plan, so the data would first have to move into the database or Cloudflare storage.
  - **Compatibility.** Next 16, the sign-in proxy and some Node APIs would need checking.
  - **Verdict.** Expect days of migration and a new class of bugs. Not worth it while Vercel Pro is $20.
- **Self-hosting Supabase on a small server (about $5-10 a month).**
  - **What you take on.** Backups, upgrades, security patches, uptime and sign-in email delivery all become your job.
  - **Verdict.** Not recommended for a one-person team during testing.
- **Shrinking the database.** It is not the problem: 157 of 500 MB. Archiving the 7 Oct factory jobs would free 46 MB if it is ever needed.

---

## Appendix: how this was measured (all read-only)

- **Vercel (MCP):**
  - Project list: 6 projects (1 live, 5 paused duplicates).
  - Deployment history since 13 Oct: 96 deployments across the team.
  - Latest production deployment, `dpl_D2rXNuzQP8wRvMJD5br5Kp6kATwF`, `regions: ["iad1"]`.
  - Runtime error groups for 7 days: the 59-timeout group, first seen 2026-10-07 05:36 UTC, last seen 2026-10-13 04:50 UTC.
  - Runtime logs for the last hour: `/api/stats` was the only route logging.
  - Usage metrics and billing returned "Observability Plus required" and "costs not found" on Hobby, so no direct usage numbers.
- **Supabase (MCP):**
  - `pg_database_size`, table sizes, column-level JSON sizes of `questions`, and per-subject pool sizes.
  - `pg_stat_statements`, counting since 21 Apr: 7,297 whole-table pages, 1,315 + 5,217 + 765 calls across three query shapes.
  - `pg_stat_user_tables`: `questions` has had 169 million rows read by full scans.
  - Gateway logs for the last 24 hours: requests by path, by network owner and by 5-minute bucket.
  - Storage objects (none), auth counts, and the performance advisors (only minor index notes, none tied to usage).
- **Documentation used:**
  - Supabase billing FAQ and "Manage egress usage", for limits, grace period and restrictions.
  - Vercel Hobby plan, functions pricing and cron docs, via Context7: Hobby includes 4 CPU-hours Active CPU, 360 GB-hours memory, 1M invocations, 100 GB Fast Data Transfer and 5,000 image transformations; a 30-day wait after exceeding; crons at most daily; any single function region.
- **Not verifiable with these tools:**
  - The exact numbers on both Usage pages, and the Supabase reset date.
  - Whether Supabase bills compressed or raw bytes.
  - Usage before 7 Oct on Vercel, because error history stops at 7 days.
- **Earlier evidence:** a 7 Oct dashboard capture showing "Egress 2.28 / 5 GB, Database size 120 / 500 MB, Monthly active users 4 / 50,000".
- **Code evidence:** paths are in the live worktree `wt-deploy` (branch `web/lab-s3`, deployed commit 48309076) and the app in `wt-phase2/flutter_app`.
