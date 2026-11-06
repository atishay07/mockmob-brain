# Runbook: nta_question_index (usage fix A6)

15 Oct 2026. Source: `docs/brain/USAGE-LIMITS-DIAGNOSIS-2026-10-15.md` row A6. Allowed under the owner's
standing database grant (14 Oct). Production is `isrxrxzjocewrdureyhp`; staging is `onwkqxmjqjrhfbjjdydu`.

## What it does

NTA papers read one subject's pool through `nta_question_index`: signed slim rows (score, judges, content
hash, family, objective tag) plus the questions without their `evidence` column, instead of every column of
the subject. About 0.27-0.36 MB a start instead of 5.3-6.6 MB (`docs/brain/NTA-ENGINE-RUN.md`). The runtime
re-checks each row's HMAC signature (`CUET_EVIDENCE_SIGNING_KEY`) and that the question's content hash is
unchanged, so the index cannot admit a question the full read would refuse. The score bar (`NTA_MIN_SCORE`)
is applied at runtime; moving it needs no rebuild. The engine itself (`data/nta_engine.js`) is unchanged.

## Files

- Migration (create): `supabase/migrations/20261013190000_nta_question_index.sql`
- Undo (drop): `supabase/undo/20261013190000_nta_question_index.undo.sql` (outside `migrations/` on purpose)
- Index builder: `scripts/nta-index-build.mjs` (dry run by default; `--write` upserts; production also needs `--allow-production`)

## Safe order

1. Apply the migration. It adds an empty table: no behaviour change, because `loadNtaPoolFromIndex` returns null
   for a missing OR empty subject and the full read runs as before.
2. Build the index for each subject (reads the questions with their evidence, select only; writes only
   `nta_question_index`). From this moment NTA starts read the slim path.
3. Rebuild after any change to a question's content or evidence (a stale row is refused at runtime by the
   content-hash check and the question simply falls out of the pool until rebuilt) and after the signing key
   rotates. The build removes a subject's rows that no longer verify.

## Keeping the index current (Q8b, 15-16 Oct 2026)

The index no longer needs a manual rebuild after a publish. Three layers, each safe on its own:

1. **Pool fallback (always on, no deploy step).** `loadNtaPoolFromIndex` compares the subject's newest index
   `verified_at` with the newest `created_at` or `live_at` of its live, undeleted questions (two one-row selects,
   once per subject per 5-minute pool cache). If a question is newer, the subject is read in full for that start
   (`timings.poolSource = full`, `timings.indexStale = true`, one `[nta-index] stale index` log line), so a question
   published after the last build is never missing from a paper. A failed check also reads in full.
2. **Every publish path rebuilds the subjects it touched** (`data/nta_index.js`):
   - `scripts/question-publish-authored.mjs --mode=apply`: right after its read-back is clean (`ntaIndex` in its output).
   - `scripts/question-republish.mjs --mode=apply`, `scripts/question-hold.mjs --mode=restore`,
     `scripts/question-reorder.mjs` (`--keep-live` apply, restore, release): after the database change (`ntaIndex` in the output).
   - The factory and the worker publish one question or one passage group at a time (`publishFactoryQuestion`,
     `publishFactoryGroup`, `publishQuestion`). They note the subject in a queue that rebuilds it at most once per
     30 minutes per subject (`createNtaIndexTouchQueue`), and the batch ends (`factory.mjs` worker, `publishProductionCohort.mjs`,
     the offline import) flush it at once.
   - All of them need `CUET_EVIDENCE_SIGNING_KEY` in the environment or `.env.local`, skip quietly when the key or the table
     is missing, never fail the publish, and can be switched off (`--no-index-rebuild`, or `NTA_INDEX_REBUILD=off` for the
     queue). Two rebuilds of the same subject in one process never run at once: the second waits and runs once more, so it
     sees what was published in between.
   - The website's routes publish nothing the index can hold: the moderation pass and user uploads work on questions without
     signed evidence and never set `status: live`, and `/api/admin/question-factory` only changes pause and phase flags.
     A test fails if one of them starts writing `status: 'live'`.
3. **Daily safety rebuild, on the existing cron.** `vercel.json` is at its limit, so there is no cron entry of its own:
   `/api/internal/refresh-inventory` (21:30 UTC, 03:00 IST) runs it right after the inventory refresh, within the same 300 s
   (it stops starting subjects 250 s after the request began and leaves the rest for the next day). It goes subject by
   subject, oldest index first, and rebuilds a subject only when one of three things is true:
   `newer_questions` (a live question is newer than the index), `content_changed` (an indexed question no longer hashes to its
   row: an edited stem or key; a slim read, about 0.3 MB, no evidence column) or `max_age` (the index is older than 7 days:
   re-verifies expired evidence and drops rows that no longer verify). Otherwise it costs a few small selects and writes
   nothing, so a repeat run, or a second run in a day, changes nothing. A subject with no index rows is left alone (the first
   build stays the owner's step). It runs only on Vercel production (`data/full_bank_guard.js`), uses the same secrets as the
   inventory route, and never changes that route's status code: the outcome is in the response under `ntaIndex` and in one
   log line, `[nta-index] daily refresh ok in 1840 ms: rebuilt 1 (chemistry newer_questions 41 rows), fresh 9, never built 3`
   (`console.error` with `FAILED` when a subject failed). The route `/api/internal/rebuild-nta-index` stays, outside
   `vercel.json`, for a manual run: `?subject=<id>` for one subject, `?force=1` to rebuild every built subject whether it is
   stale or not (safe to repeat; one full read per subject).

`verified_at` is stamped per subject at or after that subject's newest live question, so a clock difference between
the builder and the database cannot leave a fresh build looking stale. No migration change.

What none of this can see: a question the index lost because it was held and later shown again by SQL run by hand (nothing
in `created_at`, `live_at` or its hash moves). The weekly `max_age` rebuild brings it back; for a change you made by hand,
call `/api/internal/rebuild-nta-index?subject=<id>&force=1`.

## Switching it on (owner steps, in order)

1. Apply the migration `20261013190000_nta_question_index.sql` (standing database grant; section below). Until this
   step everything above is inert: the table is missing, every rebuild skips, and NTA mode reads the full pool as before.
2. Set `CUET_EVIDENCE_SIGNING_KEY` in the Vercel production environment (the same value `.env.local` uses for the factory),
   then redeploy. Without it the daily pass logs `skipped: no_signing_key`.
3. Build the first index of every subject once (`scripts/nta-index-build.mjs --write --allow-production`, below). From then
   on the publish paths and the daily pass keep it current.
4. Check the next morning's log for `[nta-index] daily refresh ok` (Vercel logs, route `/api/internal/refresh-inventory`).

## Apply and verify (production)

Use the Supabase MCP `apply_migration` with name `nta_question_index` and the SQL of the migration file, or
`supabase db push` if the CLI is linked to production. Then verify with `execute_sql`:

```sql
select c.relrowsecurity as rls,
       (select count(*) from pg_indexes where tablename = 'nta_question_index') as indexes,
       (select string_agg(grantee || ':' || privilege_type, ',' order by grantee, privilege_type)
          from information_schema.role_table_grants
         where table_schema = 'public' and table_name = 'nta_question_index'
           and grantee in ('anon', 'authenticated', 'public')) as non_service_grants,
       (select count(*) from public.nta_question_index) as rows
from pg_class c where c.oid = 'public.nta_question_index'::regclass;
```

Expected: `rls = true`, `indexes = 2`, `non_service_grants = null`, `rows = 0`.

Build the rows from a machine that has the production service-role key and `CUET_EVIDENCE_SIGNING_KEY` in its
environment (never paste either into chat or a file). Dry run first, then write:

```
node --use-system-ca scripts/nta-index-build.mjs --env .env.local --out tmp/nta-index-prod-dry-run.json
node --use-system-ca scripts/nta-index-build.mjs --env .env.local --write --allow-production
```

The dry run prints, per subject, `loaded`, `indexed`, the full and slim byte counts and the reasons rows were
rejected. Expect `indexed` to match the number of questions whose evidence passes the NTA score checks, and
the slim bytes to be under about 0.4 MB. The write reads every NTA subject's full pool once (about 20-40 MB of
egress, one time).

Verify the write:

```sql
select subject, count(*) as rows, min(score) as min_score, max(verified_at) as built_at
from public.nta_question_index group by subject order by subject;
```

then start one NTA paper per subject from a test account and check the server log line `[nta-engine]`: its
`timings.poolSource` should read `index` (not `full`), and `pool.loaded` should equal the subject's index rows plus agent-scored
rows.

## Undo

Run `supabase/undo/20261013190000_nta_question_index.undo.sql` (`drop table if exists public.nta_question_index;`).
NTA mode returns to the full read at once (Postgres 42P01 or PostgREST PGRST205 means "no index"). Nothing else
depends on the table. To keep the table but turn the slim read off, `truncate public.nta_question_index;`.
