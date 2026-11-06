# Production health audit, 16 Oct 2026

Read-only. Taken about 4:55 PM IST (11:25 UTC) on 16 Oct 2026. Nothing was applied, changed, paused or deployed. Only SELECTs, advisor reads and log reads were run against Supabase `isrxrxzjocewrdureyhp` (mockmob, ap-southeast-1) and Vercel `prj_uSolddribHQDl1mM5AKxg3O9qCIu`.

Builds on `USAGE-LIMITS-DIAGNOSIS-2026-10-15.md`. That file's fixes A1 to A4 are checked against live state in finding 1.

## What I could not measure

- **Vercel usage meters.** The observability query tool rejected the request and then timed out. Hobby also does not expose usage to these tools. Vercel egress, CPU hours and invocations for today are not measured here. Read them under Vercel, Settings, Usage.
- **Vercel logs older than one hour.** Hobby keeps 1 hour of runtime logs. The 24 hour picture for Vercel comes from the pre-aggregated error clusters only.
- **Supabase response bytes.** The gateway logs carry no `content_length` for most responses (chunked), so egress below is computed from row sizes times request counts. It is raw JSON size, before any compression.
- **Plan and billing cycle.** `get_organization` is denied to this account. The diagnosis of 15 Oct states the Supabase organisation is on the Free plan (5 GB egress, 500 MB database). I treat that as given.
- **Counter windows.** `pg_stat_statements` and `pg_stat_user_tables` have been counting since 21 Apr 2026 (about six months). Counts from them are lifetime, not today. Edge-log numbers are the last 24 hours.

## Headline

- Real students are barely visible in the data. Of about 5,640 Supabase API requests in 24 hours, 4,194 (74%) came from the owner's home connection (Bharti Telenet, Delhi) using the service key, and 5,372 (95%) used the service key from a Node client. Only 261 used the publishable key from Node, and those are all auth calls.
- No application errors reached students in the last 24 hours. Vercel shows one logged line, no exceptions. Supabase edge shows 3 responses at 400 or above out of 5,676, all from our own scripts.
- The thing most likely to hurt students is self-inflicted: whole-bank downloads still run about 49 times a day and push the free Supabase egress quota toward a restriction.

---

## Findings ranked by student impact

### 1. Whole-bank downloads still burn the free egress allowance (risk: API restriction for every student)

**Evidence**

- Edge logs, last 24 h: 489 requests to `/rest/v1/questions?select=*&is_deleted=eq.false&order=id.asc&offset=N&limit=1000`. That is the exact call in `src/lib/server/inventory.js:17`.
- 449 of 489 came from the owner's Bharti connection (2 IPs), 17 from Amazon Northern Virginia, 4 from Singapore, 9 from Japan, 10 from other US ranges.
- One full copy is 10 pages and 41 MB of JSON (9,697 live rows, average 4,419 bytes as JSON; `evidence` alone is 8.2 MB even compressed in storage). 489 pages is about 49 copies, about 2.0 GB raw per day. On 15 Oct the diagnosis counted 26 copies and 1.1 GB, so this is worse today, not better.
- `pg_stat_statements`: the `questions.*` paging statement has 10,126 calls, 236 ms mean, 6.9 s worst, 2,388 s of total database time. That is the single biggest consumer of database time since April.
- `public_inventory_snapshot` was read 499 times in 24 h (539 ms average) and `/api/stats` is polled about every 100 s by a "script" client from Delhi (Vercel log, last 50 min).
- Checked against fixes from the diagnosis: A3 (region) is live. The deployed production build runs in `sin1`. A1 and A4 are not in the working tree: `src/lib/server/inventorySnapshot.js` still sets `SNAPSHOT_FRESH_MS = 15 * 60 * 1000` and `inventory.js` has no `VERCEL_ENV` guard. The STATUS commit for `web/usage-fixes` says "local, not deployed".
- Supabase still answers (project `ACTIVE_HEALTHY`, no 402s in the edge log), so either the grace period is running or the meter has not tripped. Unknown from here.

**Why students feel it.** If Supabase restricts the organisation, every API call can return 402 or the database can go read-only. That takes down sign-in, practice and mocks together.

**Fix (code, deploy needs the owner's OK).**

1. `src/lib/server/inventory.js`, stop refreshing from anywhere except the daily cron and never from a developer machine:

```js
// scheduleRefresh(): only the production cron may recompute the whole bank.
function scheduleRefresh() {
  if (process.env.VERCEL_ENV !== 'production') return;   // local dev and previews serve the stored snapshot
  if (refreshing) return;
  ...
}
// refreshInventorySnapshot(): same guard, except when called by the cron route.
export async function refreshInventorySnapshot({ fromCron = false } = {}) {
  if (!fromCron && process.env.VERCEL_ENV !== 'production') throw new Error('INVENTORY_REFRESH_PRODUCTION_ONLY');
  ...
}
```

   and in `src/lib/server/inventorySnapshot.js` change `snapshotDecision` so a snapshot younger than 24 h never asks for a refresh (`refresh: false`); `/api/internal/refresh-inventory` calls `refreshInventorySnapshot({ fromCron: true })`.
2. Stop reading `evidence` and `provenance` for counts. Add a Postgres function that returns only per-subject counts for the eligibility test that does not need evidence, or select the light columns and fetch evidence only for rows whose eligibility needs it. Saves about 55% of each copy (23.5 MB of 41 MB per the 15 Oct sizing).
3. Point the eight `.env.local` files at staging `onwkqxmjqjrhfbjjdydu` (owner decision, per the 15 Oct diagnosis section B.2). Without it, 92% of whole-bank copies today still come from local machines.

**Undo.** Revert the commit. No data changes.

---

### 2. Starting a practice session downloads the whole subject, with the heaviest column

**Evidence**

- `data/db.js` `getQuestions` (lines 1118 to 1152): `select('*')` of the subject, 1,000 rows a page, `order created_at desc`, evidence included.
- Student-side latency from the edge log, excluding the owner's network: `/rest/v1/questions` 56 requests, average 965 ms, p95 2,210 ms, max 2,418 ms. Every other student route averages 180 to 390 ms.
- Per-subject read sizes from the 15 Oct diagnosis: Accountancy about 8.0 MB, Business Studies 7.1 MB, Economics 6.9 MB, English 6.0 MB per session start. A fresh 5 GB month is about 700 Commerce session starts.
- Database-side, the matching PostgREST statements show a long tail: max 5.5 to 6.9 s, 1,435 calls at 308 ms mean.

**Why students feel it.** A mock or practice start takes about a second longer than any other action and uses 6 to 8 MB of mobile-irrelevant server bandwidth. At launch it multiplies with finding 1.

**Fix (code, `data/db.js`, medium risk, run `test:recovery`, `test:nta`, `test:learning` and the question suites).** Select the light columns for ranking and picking (`id, subject, chapter, difficulty, status, created_at, score, passage_group_id, order_index, content_hash`), then fetch full rows with `.in('id', pickedIds)` for the 10 to 50 chosen questions. Compare picks before and after on a fixed seed.

**Undo.** Revert the commit.

---

### 3. A student's first sign-in can fail with a 500

**Evidence**

- Vercel runtime error cluster, 11 Oct 2026, `/api/auth/me`: `duplicate key value violates unique constraint "users_pkey"`, status 500 after 2,337 ms, desktop browser. Earlier occurrence 17 Jun 2026 (same code 23505).
- `data/db.js` `createUser` does a plain `insert(row).select('*').single()` and throws on any error. Two near-simultaneous first requests (web app loads `/api/auth/me` and another route) both try to create the same user.
- Related, one-off and now resolved: `/api/auth/email-login` logged `clearing an unconfirmed password failed: PGRST202` twice on 15 Oct 03:30 UTC. `public.auth_clear_unconfirmed_password(p_email text)` now exists (secdef, search_path empty, service role only) and nothing has repeated since, so the migration landed after those two calls. Confirm once that the schema cache is current (see undo note).

**Fix (code, `data/db.js` `createUser`).** Make creation idempotent so the loser of the race reads the winner's row:

```js
const { data, error } = await supabaseAdmin().from('users')
  .upsert(row, { onConflict: 'id', ignoreDuplicates: true }).select('*').maybeSingle();
if (error) throw error;
const out = data || (await supabaseAdmin().from('users').select('*').eq('id', row.id).single()).data;
return userOut(out);
```

Keep `credit_balance: 100` only on first insert (`ignoreDuplicates` guarantees that).

**Undo.** Revert the commit. If PGRST202 returns, run `NOTIFY pgrst, 'reload schema';` once.

---

### 4. Leaderboard and dashboard read far more than they show (fine today, slower every week)

**Evidence**

- `data/db.js:1702` `getLeaderboard` pages through every attempt (`select user_id, score` with no filter) on each call. `pg_stat_statements`: 11,424 calls, 42 ms mean, 2.6 s worst, 483 s total. Edge log: 148 unscoped `attempts` reads in 24 h. `attempts` has 1,815 rows and 11,559 sequential scans (7.6 M tuples read since April).
- `data/db.js:1584` `getAttempts(userId)` is `select('*')`. Each attempt averages 10 kB (8.7 kB is `questions_snapshot`). A student with 100 mocks returns 1 MB to open a list that `listAttemptSummaries` (`src/lib/server/attemptSummary.js`) already serves in a few kB.
- `attempts` is 21 MB on disk for 1,815 rows and 18 MB of that is out-of-line (TOAST) data. Reading a few columns is cheap, reading `*` is not.
- The right index exists: `attempts_user_completed_idx (user_id, completed_at desc)` has 32,941 scans. `user_question_progress` has `(user_id, updated_at desc)` and `(user_id, subject, updated_at desc)`, 18,222 and 144 scans. `revise_cards` and `recovery_sessions` indexes cover their lookups (`recovery_sessions_owner_state` 521 scans). No hot-path index is missing for those four tables.

**Fix (migration plus code).** Add a grouped function and call it from `getLeaderboard`; point web dashboard reads at `listAttemptSummaries`.

```sql
-- up
create or replace function public.leaderboard_totals()
returns table (user_id text, tests integer, total_score bigint)
language sql stable
set search_path = public, pg_temp
as $$ select a.user_id, count(*)::int, coalesce(sum(a.score), 0)::bigint from public.attempts a group by a.user_id $$;
revoke execute on function public.leaderboard_totals() from public, anon, authenticated;
grant execute on function public.leaderboard_totals() to service_role;
-- undo
drop function if exists public.leaderboard_totals();
```

In `getLeaderboard`: `const { data, error } = await supabaseAdmin().rpc('leaderboard_totals');` then keep the existing user lookup. Check the sort and tie-break against the current output before shipping.

---

### 5. Database access is protected only by "RLS on, no policy" (no leak found, one slip would open it)

**Evidence**

- Security advisor: 69 tables in `public` have RLS enabled and no policies. Every table in `public` has RLS on (no table without it).
- The same tables still carry full table grants to the `anon` and `authenticated` roles. Checked: `users`, `attempts`, `credit_transactions`, `ai_credit_wallets` and 20 others give both roles SELECT, INSERT, UPDATE and DELETE. Today RLS with no policy denies everything, so there is no leak. One `CREATE POLICY ... USING (true)` or one `ALTER TABLE ... DISABLE ROW LEVEL SECURITY` in a future migration would expose users and balances to anyone holding the public key.
- Good: `questions` has no grants at all for `anon` or `authenticated`, so the live-question policy is dead and answers are not reachable through the public key. `payments` is SELECT-only for `authenticated`, and its policy is user-scoped.
- Client use of the public key is auth only: in 24 h the publishable key made 217 `/auth/v1/user`, 31 JWKS, 10 token, 4 logout, 1 verify, and one `GET /rest/v1/questions` that returned 401. No student client reads tables directly, so revoking table grants will not break the app (checked also: no `.channel(` or realtime use in `src` or `data`).
- Functions: 10 `public` functions are executable by `anon` and `authenticated`: `apply_question_vote` (two overloads), `claim_moderation_job`, `count_distinct_mock_sessions`, `create_pending_payout(p_creator_id, p_actor_id)`, `enforce_admin_role`, `link_user_to_creator`, `recover_stale_moderation_jobs`, `set_updated_at`, `sync_question_scores_metadata`. They are SECURITY INVOKER, so RLS blocks their table writes today. `create_pending_payout` inserts a `paid` payout and stamps payments, so it must never become reachable by a public caller.
- Advisor warns: 16 functions with a mutable `search_path`, and Auth leaked-password protection is off.
- Advisor also flags `payments` policy "Users can read their own payments": `auth.uid()` is re-evaluated per row.

**Fix.** Four small migrations. Test each on staging first. Apply one at a time.

```sql
-- 5a up: take table grants away from the public roles on every RLS table that has no policy
do $$ declare r record; begin
  for r in select c.oid::regclass as t from pg_class c join pg_namespace n on n.oid=c.relnamespace
           where n.nspname='public' and c.relkind='r' and c.relrowsecurity
             and not exists (select 1 from pg_policy p where p.polrelid=c.oid)
  loop execute format('revoke all on %s from anon, authenticated', r.t); end loop;
end $$;
-- 5a undo (restores Supabase's default grants on those tables)
do $$ declare r record; begin
  for r in select c.oid::regclass as t from pg_class c join pg_namespace n on n.oid=c.relnamespace
           where n.nspname='public' and c.relkind='r' and c.relrowsecurity
             and not exists (select 1 from pg_policy p where p.polrelid=c.oid)
  loop execute format('grant all on %s to anon, authenticated', r.t); end loop;
end $$;
```

```sql
-- 5b up: functions meant only for the server
revoke execute on function
  public.apply_question_vote(uuid, uuid, text),
  public.apply_question_vote(text, text, question_vote_type),
  public.claim_moderation_job(text),
  public.count_distinct_mock_sessions(text, timestamptz),
  public.create_pending_payout(text, text),
  public.recover_stale_moderation_jobs(integer)
from public, anon, authenticated;
grant execute on function
  public.apply_question_vote(uuid, uuid, text),
  public.apply_question_vote(text, text, question_vote_type),
  public.claim_moderation_job(text),
  public.count_distinct_mock_sessions(text, timestamptz),
  public.create_pending_payout(text, text),
  public.recover_stale_moderation_jobs(integer)
to service_role;
-- 5b undo
grant execute on function
  public.apply_question_vote(uuid, uuid, text),
  public.apply_question_vote(text, text, question_vote_type),
  public.claim_moderation_job(text),
  public.count_distinct_mock_sessions(text, timestamptz),
  public.create_pending_payout(text, text),
  public.recover_stale_moderation_jobs(integer)
to public, anon, authenticated;
```

The trigger functions (`enforce_admin_role`, `link_user_to_creator`, `set_updated_at`, `sync_question_scores_metadata`) keep working without EXECUTE rights for triggers, so they can be revoked the same way after a staging test.

```sql
-- 5c up: pin search_path on the 16 flagged functions (staging test first: any function that
-- uses an unqualified name outside public or pg_temp will fail)
do $$ declare r record; begin
  for r in select p.oid::regprocedure as f from pg_proc p join pg_namespace n on n.oid=p.pronamespace
           where n.nspname='public' and p.prokind='f' and p.proconfig is null
             and p.proname in ('claim_moderation_job','count_distinct_mock_sessions','recover_stale_moderation_jobs',
               'sync_question_scores_metadata','apply_question_vote','enforce_admin_role','link_user_to_creator',
               'create_pending_payout','set_updated_at','grant_contribution_credits','moderate_question_with_credit',
               'grant_daily_login_credits','grant_attempt_answer_credits','spend_credits','save_sample_import')
  loop execute format('alter function %s set search_path = public, pg_temp', r.f); end loop;
end $$;
-- 5c undo
do $$ declare r record; begin
  for r in select p.oid::regprocedure as f from pg_proc p join pg_namespace n on n.oid=p.pronamespace
           where n.nspname='public' and p.proconfig @> array['search_path=public, pg_temp']
  loop execute format('alter function %s reset search_path', r.f); end loop;
end $$;
```

```sql
-- 5d up: evaluate auth.uid() once per query
drop policy "Users can read their own payments" on public.payments;
create policy "Users can read their own payments" on public.payments
  for select to authenticated using (user_id = (select auth.uid())::text);
-- 5d undo
drop policy "Users can read their own payments" on public.payments;
create policy "Users can read their own payments" on public.payments
  for select to authenticated using (user_id = (auth.uid())::text);
```

Owner dashboard action: Supabase Auth, Providers, Email, turn on "Prevent use of leaked passwords". Undo is the same toggle.

---

### 6. The database is slow to answer simple lookups, and local analysis scripts run heavy statements on it

**Evidence**

- Student-side calls (edge logs, owner's network excluded): `/rest/v1/users` 383 calls, 268 ms average, p95 857 ms. `/rest/v1/attempts` 177 calls, 293 ms, p95 1,086 ms. Database execution time for these is under 1 ms (primary-key lookups, `users_pkey` 202,808 scans). The remaining 250 ms or more is round trip, pooling and gateway time, so the number of sequential calls per page is what students feel.
- Authenticated session check `/auth/v1/user` runs 366 times a day (211 from non-owner traffic). The JWKS path (`/auth/v1/.well-known/jwks.json`, 31) shows the app can verify tokens locally. Using local verification for every API route would remove most of the 211.
- Heavy statements on production, from our own analysis scripts: a 5.2 to 7.4 s query over `attempts.details` and `questions` (6 calls, 131,002 buffer blocks each), `public.refresh_question_option_stats()` 13.0 s (1 call, no caller in `src` or `data`), five 2.8 to 4.4 s JSON-size scans over `questions`. One `canceling statement due to statement timeout` is in the Postgres log. Several more recorded errors are the same family of ad hoc queries (`column ... does not exist`, `operator is not unique`).
- PostgREST log: 548 lines of `Warp server error: Thread killed by timeout manager` in 24 h (about 570 with multi-line entries), on a day with 5,676 requests. This is PostgREST closing a slow or abandoned connection. It lines up with the large paged reads (finding 1), not with a student route, but I could not tie each line to a request.
- Autovacuum and analyze are stale on a few small tables: last analyze 18 May for `attempts` (1,815 rows), 26 Jul for `users`. Harmless at this size, but the planner is working from old row counts.
- Database size 157 MB of 500 MB (31%). `question_factory_jobs` is 46 MB (almost all TOAST, 898 rows), `questions` 28 MB, `attempts` 21 MB, `user_question_progress` 12 MB.

**Fix.**

1. Run ad hoc analysis against staging or a branch, not production. If it must run on production, wrap it in `set local statement_timeout = '5s'` and `set transaction read only`.
2. Verify the session JWT locally in the API route helpers (use the published JWKS), and only call `/auth/v1/user` when freshness matters (sign-out, password change).
3. One-off statistics refresh (safe, writes statistics only):

```sql
-- up
analyze public.attempts; analyze public.users; analyze public.user_question_progress; analyze public.questions;
-- undo: none needed
```

---

### 7. Ten foreign keys have no covering index (matters for deletes, not for reads today)

**Evidence.** Performance advisor, `unindexed_foreign_keys`:

| Table.column | Why it matters |
|---|---|
| `learning_observations.user_id`, `study_events.user_id` | Account deletion (`src/lib/server/accountDeletion.js` deletes by user) scans the whole table |
| `recovery_playbook.attempt_id`, `recovery_review_queue.attempt_id` | Deleting an attempt scans both (the deletion processor deletes attempts) |
| `revise_cards.question_id`, `user_question_progress.question_id`, `user_question_answer_credits.question_id`, `question_concepts.question_id`, `question_content_disputes.question_id` | Deleting or merging a question scans each |
| `study_cards (unit_id, unit_version)` | Unit version change |

All of these tables are small now (largest: `user_question_progress` 33,920 rows), so no read is slow today. Index creation is cheap and the write cost is negligible.

**Fix.** Build outside a transaction (`CREATE INDEX CONCURRENTLY` cannot run in one):

```sql
-- up
create index concurrently if not exists learning_observations_user_id_idx on public.learning_observations (user_id);
create index concurrently if not exists study_events_user_id_idx on public.study_events (user_id);
create index concurrently if not exists recovery_playbook_attempt_id_idx on public.recovery_playbook (attempt_id);
create index concurrently if not exists recovery_review_queue_attempt_id_idx on public.recovery_review_queue (attempt_id);
create index concurrently if not exists revise_cards_question_id_idx on public.revise_cards (question_id);
create index concurrently if not exists user_question_progress_question_id_idx on public.user_question_progress (question_id);
create index concurrently if not exists question_content_disputes_question_id_idx on public.question_content_disputes (question_id);
-- undo
drop index concurrently if exists public.learning_observations_user_id_idx;
drop index concurrently if exists public.study_events_user_id_idx;
drop index concurrently if exists public.recovery_playbook_attempt_id_idx;
drop index concurrently if exists public.recovery_review_queue_attempt_id_idx;
drop index concurrently if exists public.revise_cards_question_id_idx;
drop index concurrently if exists public.user_question_progress_question_id_idx;
drop index concurrently if exists public.question_content_disputes_question_id_idx;
```

Do not drop the 28 "unused" indexes yet. Most sit on tables for features with almost no traffic (payments, rival battles, revise cards, usage events). Their idle status says nothing at 8 attempts in three weeks. Revisit once real traffic exists. `users_name_lower_idx` is unused because the only call that would use it (`getUserByName` in `data/db.js:317`) has no caller and uses `ilike`, which a `lower(name)` index does not serve.

---

### 8. Vercel side: no active errors, one noisy log line, the old timeout cluster is closed

**Evidence**

- `get_runtime_errors`, 24 h: one group, `{"route":"repair","stage":"interpret","kind":"explained","dropped":[]}` on `/api/recovery/repair`, count 1, 15 Oct 8:46 PM IST (20:46 UTC). That is a normal diagnostic line written at error level, not an exception.
- `get_runtime_errors`, 7 d: 52 timeouts "Task timed out after 300 seconds" on `/api/practice/quote` and `/api/stats`, 20 users, 7 Oct 5:36 UTC to 13 Oct 4:50 UTC, last deployment `dpl_BRnd6uWft...`. None since 13 Oct. The fix for that is in production.
- Other 7 d groups, all single events: `/api/questions/pending` returns "Bad Request" (last 12 Oct, first seen 24 Jun), the `/api/auth/me` duplicate key (finding 3), the PGRST202 pair (finding 3).
- Live now: production deployment `dpl_DWnHXg8zQ...` (commit `4db57fc5`) is READY with `regions: ["sin1"]`. Last 50 minutes: 4 requests, all `/api/stats`, 200, 0 to 761 ms, from a Delhi script client. The last 8 production deployments: 7 READY, 1 ERROR (`dpl_BHchzehMX...`, 15 Oct, Mistake Lab merge, superseded by a redeploy within about 2 hours).
- Slow routes and 4xx/5xx spikes: Vercel's per-route latency and status counts are not available on Hobby here. From the Supabase side nothing spiked: 5,644 of 5,676 edge responses were 200, 19 were 302 (auth redirects), 4 were 204, 3 were 201, 3 were 206. The only three failures were a 401, a 404 and a 555 (see below), all from our own node client.
- The 555 was a full-bank page that ran 10,004 ms at the database on 15 Oct 4:07 PM UTC and was cut off. Same cause as finding 1.

**Fix.** None needed for runtime errors. Two small items: log the `repair/interpret` line at `info` (find the `console.error` for `stage: 'interpret'` in `src/app/api/recovery/repair`), and read `/api/questions/pending` once to see why a 400 comes back.

---

### 9. Edge and egress picture against the free-plan limits

| Meter | Free limit | Measured | Verdict |
|---|---|---|---|
| Supabase egress | 5 GB per month, shared by prod and staging | About 2.0 GB raw per day from whole-bank copies alone (about 49 copies). Compression is unknown, so billed bytes are lower. 7 Oct already at 2.28 GB (diagnosis) | Over pace. Likely already tripped or in grace. Confirm on the Supabase billing page |
| Supabase database size | 500 MB | 157 MB | Fine |
| Supabase file storage | 1 GB | 0 files (diagnosis) | Fine |
| Supabase monthly active users | 50,000 | 9 signed in over 30 days; 1,639 accounts (diagnosis); 1,641 user inserts in `pg_stat_statements` | Fine |
| Supabase auth and API request count | no hard cap on Free | 5,676 requests in 24 h, 1,043,313 PostgREST `set_config` calls since April (about 6,000 a day) | Fine |
| Vercel Active CPU | 4 hours per month | Not readable. The 52 to 59 timeouts of 7 to 13 Oct (up to 4.9 CPU hours) are the likely cause of the earlier overage. None since | Check Vercel, Settings, Usage |
| Vercel function invocations, data transfer | 1,000,000 and 100 GB | Last 50 minutes: 4 requests. Traffic is tiny | Fine |
| Vercel commercial use | Hobby is non-commercial | MockMob takes payments (Razorpay) | Owner decision, unchanged since 15 Oct |

Hourly Supabase API request counts: 3 to 6 hours of the day carry the load. The peak was 08:00 to 09:00 UTC on 16 Oct (2,005 and 735 requests), which is owner-network traffic during local testing. Overnight and early morning IST hours show 6 to 12 requests an hour.

---

## Recommended order

1. Finding 1 code guard plus staging `.env.local` switch (stops about 92% of egress today). Needs the owner's OK to deploy, since it touches production behaviour.
2. Finding 3 `createUser` idempotent insert (a student-facing 500).
3. Finding 2 light-column session start (the only change with a visible speedup for students).
4. Finding 5a to 5d and the Auth toggle (hardening, no user-visible change, stage first).
5. Finding 4 leaderboard function, finding 7 indexes, finding 6 JWT local verify.

## Sources for each number

- Vercel: `get_runtime_errors` (24 h and 7 d), `get_runtime_logs` (50 min, grouped), `list_deployments`, `get_deployment`.
- Supabase: `get_advisors` (security and performance), `pg_stat_statements`, `pg_stat_user_tables`, `pg_stat_user_indexes`, `pg_indexes`, `pg_policy` and `pg_policies`, `information_schema.column_privileges`, `has_table_privilege`, `has_function_privilege`, and edge, Postgres, PostgREST and Auth logs for the last 24 h via `query_logs`.
- Repo files read: `src/lib/server/inventory.js`, `src/lib/server/inventorySnapshot.js`, `src/lib/server/attemptSummary.js`, `data/db.js` (lines 304 to 358, 1088 to 1152, 1305 to 1330, 1575 to 1730), `docs/brain/USAGE-LIMITS-DIAGNOSIS-2026-10-15.md`, `vercel.json`.
