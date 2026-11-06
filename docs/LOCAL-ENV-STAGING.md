# Local env files point at staging, never production

16 Oct 2026. Finding 1 of `PROD-HEALTH-2026-10-16.md`. Names only in this file: no key, secret or URL value is copied here, and no `.env` file was edited.

## The rule

A dev server, a script, an agent test or a preview must not read the production database. Production (`isrxrxzjocewrdureyhp`) is for Vercel production and for deliberate owner operations. Everything else uses staging (`onwkqxmjqjrhfbjjdydu`).

Why: on 16 Oct, 489 whole-bank pages (about 49 copies of 41 MB, about 2 GB raw) were read in 24 hours, and 92% of them came from local machines. The free plan allows 5 GB of egress a month, shared by production and staging, so a laptop that pages the question bank spends the students' allowance.

## What the code now enforces (branch `fix/health-1016`)

| Guard | Where | Effect outside Vercel production |
|---|---|---|
| Whole-bank refresh | `src/lib/server/inventory.js` calls `assertFullBankRead` (`data/full_bank_guard.js`, `VERCEL_ENV === "production"`) | Throws `FullBankReadBlocked` before any read; the cron route answers 409. Already in the base, now covered by a test that only the cron route and `inventory.js` mention `refreshInventorySnapshot`. |
| Cohort table, NTA index rebuild, `Database.getAllQuestions` | same guard | Same. Already in the base. |
| Stats and counts requests | `src/lib/server/inventorySnapshot.js` | Never recompute. They serve the stored row or an "unavailable" fallback. There is no 15 minute refresh path any more (`SNAPSHOT_FRESH_MS` is gone); a test fails if it comes back. |
| Whole-bank scripts | `assertScriptFullBankRead` in `nta-data-audit`, `nta-pass-export`, `nta-fixture-export`, `nta-diagnose`, `nta-sample` and `pipeline/tools/auditBank --database` | Refuse when the Supabase URL is the production project, unless the command line has `--allow-production` (the flag `nta-index-build` already uses). Staging passes. |
| Dev server pointed at production | `src/lib/supabase.js` calls `warnIfProductionFromOutside` (`data/db_target.js`) | One warning line per process. It does not block: the owner may do this on purpose. |

The daily count itself now reads the 22 columns it uses of the visible rows only (`data/inventory_count.js`, taken from `web/egress-1016` commit `e3fbb7b9`). The signed `evidence` and `provenance` records cannot be dropped from it: whether a row of the four evidence-managed subjects counts depends on its signed record, so they are read for those rows (about 23.6 MB of 32.7 MB). That read happens once a day on production.

Staging is not blocked, and staging egress counts against the same organisation. The 15 Oct diagnosis (section B) listed moving staging into its own free organisation as an owner option.

## Which checkouts point at production today

Run it yourself, it prints names only and exits 1 while any `.env.local` points at production:

```
node scripts/dev/env-targets.mjs "C:\Users\atish\Desktop\mockmob copy"
```

Result on 16 Oct 2026 (about 19:00 IST): 84 env files, **52 `.env.local` files point at production**, in the variables `NEXT_PUBLIC_SUPABASE_URL` and `SUPABASE_URL`. The 15 Oct diagnosis counted 8.

Folders whose `.env.local` points at production:

`mockmob copy` (the main checkout), `mockmob-backend`, `mockmob-hotfix`, `mockmob-next`, `mockmob-web2`, `wt-arena3`, `wt-batch`, `wt-batch2`, `wt-colleges`, `wt-crash`, `wt-deploy2`, `wt-fix5`, `wt-lab4`, `wt-land-perf`, `wt-land2`, `wt-learn`, `wt-merge`, `wt-mobi`, `wt-names`, `wt-ntasig`, `wt-polish`, `wt-q11`, `wt-q11b`, `wt-q8b`, `wt-repair`, `wt-rig-site`, `wt-w2a`, `wt-w2b`, `wt-w2c`, `wt-w2e`, `wt-w2f`, `wt-w2g`, `wt-w2h`, `wt-w2j`, `wt-w3-a11y`, `wt-w3-breakui`, `wt-w3-copy`, `wt-w3-faq`, `wt-w3-funnel`, `wt-w3-nudge`, `wt-w3-plan`, `wt-w3-retry`, `wt-w4-auth`, `wt-w4-compass`, `wt-w4-egress`, `wt-w4-feed`, `wt-w4-practice`, `wt-w4-rpc`, `wt-w4-sec2`, `wt-web-refine`, `wt-web-v2`, `wt-you`.

32 of them also have a `.env.staging` (variable `STAGING_SUPABASE_URL` holds the staging URL). `wt-health` has no env file.

Scripts that read `.env.local` by default, so they run against production unless given another file:

- npm scripts with `--env-file=.env.local`: `autonomous`, `validate:sample`, `validate:dry-run`, `validate:apply`, `answer-integrity:dry-run`, `answer-integrity:apply`, `answer-integrity:semantic-dry-run`, `answer-integrity:semantic-apply`, `audit:bank`.
- Scripts that load `.env.local` themselves: `scripts/apply-supabase-auth-template.mjs`, `nta-data-audit`, `nta-diagnose`, `nta-engine-run`, `nta-fixture-export`, `nta-index-build`, `nta-pass-export`, `nta-sample`, `seed`, `question-hold`, `question-publish-authored`, `question-reorder`, `question-republish`, `ops/process-account-deletions`, `learning/recovery-metrics`, `learning/apply-study-content-v2`, and about 30 files under `scripts/pipeline/` (factory, worker, publish tools).
- Of these, the whole-bank readers are now guarded (table above). The paged scans in `answer-integrity-*` and `validate-existing` read narrow columns of live rows and have write modes, so they were left alone: they are the owner's deliberate production operations.

## How to point a checkout at staging (owner or an agent with your OK)

1. Fastest, no file edit: `npm run factory:staging-app` (`scripts/pipeline/tools/stagingLocalApp.mjs`). It loads `.env.local` and then `.env.staging`, overrides `NEXT_PUBLIC_SUPABASE_URL`, `SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY` and `SUPABASE_SERVICE_ROLE_KEY` with the `STAGING_*` values, blanks the paid provider, payment and email keys, and starts `next dev` on port 3101. Port 3101 is fixed in that file, so two checkouts cannot run it at once, and 3101 to 3190 are used by the parallel workflows. A `--port` option is a small follow-up.
2. Permanent: in each checkout's `.env.local` set the same four variables to the values held in `.env.staging` (`STAGING_SUPABASE_URL` to the first two, `STAGING_SUPABASE_ANON_KEY` to the anon key, `STAGING_SUPABASE_SERVICE_ROLE_KEY` to the service role key). Keep every other line. A `.env.staging` file only holds those three `STAGING_*` names, so `NEXTAUTH_SECRET`, `CUET_EVIDENCE_SIGNING_KEY`, the AI and payment variables stay in `.env.local`.
3. Check with `node scripts/dev/env-targets.mjs "C:\Users\atish\Desktop\mockmob copy"`. Start a dev server and confirm the log has no `[db-target]` line.

Things to know when working on staging:

- Staging has its own Auth users and its own rows. Sign-in needs a staging account (`scripts/dev/staging-otp.mjs` exists for that). Agents do not sign in to hosted accounts.
- Evidence records are signed with `CUET_EVIDENCE_SIGNING_KEY`. The NTA index fix (`35a078e3`) was proved on staging rows, so the same key is in use there; if a staging read reports `signature_invalid`, check that variable first.
- Staging data lags production. A question added only to production will not show up locally.
- `scripts/dev/dry-run-migrations.mjs`, `check-staging-app-schema.mjs` and `staging-app-api-check.mjs` are the existing staging checks.

## What is not done, and needs the owner

- Switching the 52 `.env.local` files. Nothing here edits an env file.
- Vercel production variables are untouched; the guard needs `VERCEL_ENV` which Vercel sets itself.
- Deploying this branch. The guard itself (commit `c4a51cd2`) is already in live production, `origin/main` 4db57fc5. The audit of 16 Oct read `mockmob-next`, which is on `feat/app-and-web` (f3a6b483) and predates the guard, which is why it looked as if A1 and A4 were missing. Dev servers started from `mockmob-next` or any other checkout that predates `c4a51cd2` still run the old `select('*')` refresh with a 15 minute trigger, and with a production `.env.local` they copy the bank. Moving those checkouts to staging, or rebasing them, stops that; this branch adds the script guards and the warning for everything newer.
