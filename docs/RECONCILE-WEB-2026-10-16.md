# Website reconcile after the 16 Oct crash (written 16 Oct about 17:00 IST, read-only pass)

Live production is origin/main 4db57fc5. Nothing here was pushed, deployed, applied to a database, signed in to, or run in a browser. The only writes are this file and loose git objects from `git merge-tree`.

Sources read: HANDOFF-2026-10-16-DAY sections 2 and 8, the crashed session's checkpoint (20261016T091652), `tmp/wave-results/*.json`, the full wave outputs and the batch 3 workflow output in the crashed session's task folder, the last 400 lines of its transcript, `git for-each-ref refs/wip`, and `list_migrations` on production (read-only).

## 0. What stopped the crashed session

The session ended on the usage limit at 15:50 IST ("session limit, resets 6:40pm"), not on a code failure. Every agent still running died with it. Anything that says "completed" in those notifications finished earlier. Four web agents returned "no result" (repair-retry, plan-meta, a11y, break-ui), plus egress-practice and landing-perf. The app owner-ledger build returned nothing from all 8 area builders. This report covers the website only.

## 1. Answers to your specific questions

**Batch 3 (`deploy/batch-1016c`, worktree wt-polish).**
- Tip is `0b6d7d0e`. That is main 4db57fc5 merged into batch 3. Five conflicts were resolved. The refresh-inventory route keeps both nightly passes in the order inventory, NTA index, cohort stats. The NTA pass deadline was lowered from 250 s to 200 s.
- Suites on the merged tree, run by the merge agent: recovery 356, nta 180, answer-integrity 11, auth 52, app 344, du 19, learning 302, billing 87, and 37 of 38 in study. Lint was clean and `next build --webpack` passed.
- The one study failure is `study_content.test.mjs` line 103 (WordNet `LICENSE_UNAVAILABLE`). It fails identically on 4db57fc5 (the copy-pass agent proved this on the base), so it is not a batch 3 regression.
- Critics A and B finished at 390 and 1440, Night and Day. They found no high defect. They found three medium defects:
  - The replay block is clipped 4 px at the left edge on phones. `replay.css` line 258 assumes a number gutter that the Find step does not have. This is already live.
  - The pricing FAQ "What happens when I cancel?" talks about renewals for a one-payment plan. It also promises "a monthly plan is planned".
  - The Pro modal and the pricing footer stay dark in Day. The Pro modal also has a nested credits box.
  - The low items are: the "Edit" link is 25 px wide, "Welcome back" is said twice, the met week is told three times, the sticky repair header is tall, two lime Start keys sit near each other, and some labels are under 12 px.
- The fixer (Opus) did not finish. It died after 116 tool calls and never committed.
- The verifier never started (`fix: null, verify: null`).
- The fixer left 22 modified tracked files uncommitted in wt-polish (the working tree shows 23 entries; one is a whitespace-only file I did not diff). Their newest edit is 15:50. They do address the critics' list:
  - the pricing FAQ truth fix in `pricing/page.js`;
  - `replay.css`;
  - Day-theme rules in `globals.css`;
  - `RuleBook`, `RepairAsk`, `RunTrack`, `ReviseEntry` and `ScoreRecoveryLab`;
  - `result.css`, `repair-run.css` and `time-decisions.css`.
  Nothing checks them.
- **No ref protects these 22 files.** The 14:45 wip snapshots were taken before the fixer wrote them, and wt-polish has no snapshot. Snapshot them first (for example `git stash create` into a ref) before anyone runs git in wt-polish.
- Re-run on 16 Oct by me: `mobi_moments` and `cohort_time` (53 pass) and `revise` (24 pass) in wt-polish. `cohort_time` and `cohort_time_sql` (50 pass) in wt-slice5, which is a clean checkout at the slice 5 tip.
- **Visual gate: not passed.** Critics ran, the fixer did not finish and the verifier never ran.

**Landing (`web/land2-1015`, worktree wt-land2).**
- Tip is `a492e7f4` ("fixer round 7"). It is based on 09421b29 plus 30 commits and is 20 behind main.
- Last finished critic score is **85** (round 6, up from 76, 82, 84, 87, 88).
- Round 6 found 1 high and 5 medium defects plus 6 lows.
- Fixer r7 fixed 11 of those 12 critic-6 defects:
  - high: dead "Also on this page" links at 390;
  - medium: three different next moves for one student, chapter counts that disagree between the Lab and the tour, the changed-answer moment told three times, a flat desktop type scale, and the "Free to practise" overclaim.
  Its own checks passed: puppeteer at 390 and 1440 in Night and Day, link hit-tests, labStory tests 15 of 15, eslint, and `next build --webpack`.
- The one defect left open is the page-load weight (CSS merge). Two shelf images were re-encoded.
- **Critic round 7 never produced a verdict.** `tmp/landing-1016/critic-7/` holds raw captures up to 15:51 and no score. So the current score is unknown (85 last measured).
- The landing perf agent produced nothing. wt-land-perf (`web/land2-perf-1016`) is the same tip `a492e7f4`. It has one uncommitted experiment, `inlineCss: true` in `next.config.mjs`. That setting is global, not landing-only, and nobody measured it. Its wip snapshot holds only a `.next-staging` build folder, which is junk.
- Landing fails to merge with current main. Both main and batch 3 conflict in `src/components/MobileDock.jsx` (4 hunks) and `package.json`. The cause is main's 95d32d07, the checkout-aware dock, against the landing's round-5 "one dock rule". The landing also conflicts with `web/art-1016` on the binary `obj-business.v2-256.webp`.
- Landing tests I re-ran in wt-land2 (6 landing test files plus `sample_import`): 56 of 56 pass.

**NTA index fix `35a078e3` (`fix/nta-index-sig-1016`, wt-ntasig).**
- One commit on 4db57fc5. It changes `data/nta_engine.js` and `data/nta_index.js`, adds `nta_index_roundtrip.test.mjs`, and edits `package.json`.
- Cause: the builder signed `verified_at` as `...Z`, but PostgREST returns `+00:00` for the same instant. The fix normalises `verified_at` with `toISOString()` and rounds `score`, `luna` and `gemini` to 2 decimals on both the signing and checking sides.
- Proof, from the agent's report in the crashed session:
  - Staging held 535 index rows built with the old code. All 535 mismatched under the old signing and all 535 matched under the fix.
  - Every subject then read from the index on staging with 0 signature failures.
  - 5 new tests use rows shaped like real Postgres output, and they fail on the old code.
  - The NTA suite passed 185 of 185.
  - I re-ran the 5 round-trip tests: 5 of 5 pass.
- It merges cleanly with main, batch 3 and every other branch.
- **Production state (the checkpoint's "NTA index live" line is out of date):**
  - The index was applied and built at 14:00 (653 rows).
  - Every row failed `score_signature_invalid`.
  - The table was truncated at 14:55, and NTA is back on the full read.
  - The table exists with 0 rows. The STATUS entry for this lives only on `fix/security-1016`.
  - It goes back on only after this fix is deployed, the index is rebuilt (`scripts/nta-index-build.mjs --write --allow-production`), and `scripts/nta-engine-run.mjs` shows `poolSource index` with 0 signature failures.

**`fix/security-1016` (wt-w2c).**
- The database side is applied in production. `20261016141000_questions_private_to_browser_roles` appears in production's migration history, and the anon key now gets 401 on `questions`.
- **The code is not on main.** The branch has 5 commits (`86117f84` tip):
  - the migration `20261016141000_questions_private_to_browser_roles.sql` and its undo;
  - a `verify-payment/route.js` fix (a forged signature or mismatched payment no longer rewrites the student's own paid order);
  - `security_1016.test.mjs` (8 pass, re-run by me);
  - 2 STATUS entries, including the NTA rollback note.
- Main lacks the migration file, so the repo and production disagree until this merges. It merges cleanly.

**refs/wip snapshots whose work is not on a branch.**

| wip ref | Work | State |
|---|---|---|
| `wt-w3-plan-1445` | plan meta and untried chapters (`mock_swot`, `chapter_inventory`, `plan_link`; 17 files) | Only in the wip ref and the dirty wt-w3-plan. Branch `web/plan-meta-1016` still points at 4db57fc5. **A file in wt-w3-plan changed at 16:35**, after the crash, so an agent may still be writing there. |
| `wt-w3-retry-1445` | repair retry before the key (`/api/recovery/retry`, `RepairTry.jsx`, `repairRetry.js`; 24 files) | Only in the wip ref and wt-w3-retry (last edit 13:52). The branch is still at 4db57fc5. |
| `wt-w3-breakui-1445` | worst-case-data fixes (`previewWorst.js`, `firstName.js`, `Avatar`, `Glyph`) | Only in the wip ref and wt-w3-breakui. The worktree has about 8 lines newer than the snapshot. |
| `wt-w4-practice` | practice-start verdict index (`practice_verdicts.js`, `practice_source.js`, `practice-verdict-build.mjs`, a migration and its undo) | **Never snapshotted**, so it exists only in the dirty wt-w4-practice. It is incomplete, and its migration number `20261016160000` collides with credit-rpc. |
| `wt-land-perf-1445` | Only a `.next-staging` build folder | Junk. The real change is the `inlineCss` experiment in the worktree (see above). |
| `wt-w2h`, `wt-w3-faq`, `wt-w3-nudge`, `wt-w4-auth`, `wt-w4-compass`, `wt-w4-rpc`, `wt-w4-sec2` | The resumed agents finished these | All contained in their branches. Branch tips differ from the snapshot only by later refinements. |
| `wt-owner`, `wt-w2l`, `wt-w3-exam`, `wt-w3-fakes`, `wt-w3-font`, `wt-w3-record`, `wt-w4-hub`, `wt-w4-lesson` | App work (Flutter) | Out of scope here. |

Other dirty worktrees: wt-ntaidx has 10 tracked files modified since 02:59. Its branch is merged, so this is probably line-ending noise.

## 2. Branch inventory (website side)

`git branch --no-merged origin/main` lists 70 branches. App-only branches excluded: every `ui/*` (including `ui/art-1016`, `ui/owner-1016`, `ui/phase2*`), `app/play-prep-1016`, and `feat/app-and-web`. Details of that exclusion are at the end of this section.

"Gate" below means a visual pass at 390 and 1440, Night and Day, by an independent critic or the agent's own headless run. "Tests" are my re-runs with `node --test` of the branch's own touched test files at its tip. They are all clean checkouts.

### 2.1 Batch 3 (the unfinished gate)

| Branch / worktree | Tip | What it does | Finished? | Migrations (undo) | Env flags | Gate |
|---|---|---|---|---|---|---|
| `deploy/batch-1016c` (wt-polish) | `0b6d7d0e` | Slice 5 cohort-time lines (`web/slice5-1016` 3ec4c4b9 is inside it); Mobi moments on the web; arena pass 2 (Progress, Review, Radar); the nightly cohort-stats pass on `/api/internal/refresh-inventory`. | No. Suites passed at the merge. Critics A and B found 3 medium and about 12 low defects. The fixer's edits are uncommitted. The verifier never ran. | `20261016120000_question_option_stats` and `20261016130000_..._refresh_v2` (both undos exist). **Already applied in production** (13 s refresh, 461 questions). | None new. The cohort pass runs only in production and via the existing cron. `vercel.json` unchanged (2 crons). | Critics done. Fixer and verifier not. **Not passed.** |

### 2.2 Production-DB-linked hotfix lane

| Branch | Tip | What it does | Finished? | Migrations | Env flags | Conflicts | Gate |
|---|---|---|---|---|---|---|---|
| `fix/security-1016` (wt-w2c) | `86117f84` | Code and migration file for the questions lockdown. The `verify-payment` fix. | Yes. 8 tests pass. | `20261016141000_questions_private...` is **applied in production** (it is in the migration history). Undo exists. | None | Clean. The `package.json` test line conflicts with other branches (trivial). | No UI. Needs a verifier. |
| `fix/security-2-1016` (wt-w4-sec2) | `5a0cc8d2` | Retires `/api/billing/webhook` (answers 410; the real Razorpay hook is `/webhook`). Webhook in-flight lease. Constant-time secret check on moderation and internal routes. Persistent limiter on heavy recovery routes. Least-privilege grants for anon and authenticated. | Yes. 62 tests pass. Its own report says billing 110, auth 52, recovery 306, lint clean. | `20261016170000_browser_roles_least_privilege` and `20261016170100_webhook_event_lease` (both undos). **Not in production.** Staging: both applied, grants undone and re-applied, lease column dropped and re-added. | Reads `PERSISTENT_LIMITS_ENABLED`, `INTERNAL_API_SECRET`. No new required variable. | **Conflicts with `web/auth-cache-1016` in `data/db.js` (1 hunk) and with `web/egress-1016` in `recovery/route.js` (2 hunks).** Otherwise clean. | No UI. Needs a verifier. |
| `fix/nta-index-sig-1016` (wt-ntasig) | `35a078e3` | The index signature fix described above. | Yes. 5 tests pass. Staging proof as above. | None | None | Clean with everything. | No UI. |

### 2.3 Wave 2 to 4 website branches (all on 4db57fc5, one or two commits each)

| Branch (worktree) | Tip | What it does | Tests (my re-run) | Migrations (undo) and production state | Env flags | Conflicts | Gate |
|---|---|---|---|---|---|---|---|
| `web/ai-report-1016` (wt-w2a) | `245d99cc` | `POST /api/ai/mentor/report`: signed in, 10 per minute and 40 per day, 8000-character cap, fixed reason codes, owner-checked, one row per request. Privacy page names the question-stream events. Account deletion removes the reports. | 18 pass | `20261016140000_ai_reply_report` (undo exists). Staging: applied, undone, re-applied. **Not in production.** The route answers 503 until it is applied. | `PERSISTENT_LIMITS_ENABLED` makes the limits persistent | STATUS.md only, against batch 3. Trivial. | None. `/privacy` not looked at. The app's Report key stays hidden until `aiReplyReportLive` is set. |
| `web/weekdays-1016` (wt-w2j) | `2b79df03` | Study weekdays on the account. `/api/me/goal` carries a `weekdays` array. The Account goal editor picks days. | 31 pass | `20261016110000_study_weekdays` (undo exists). Staging: applied, undone, re-applied. **Not in production.** `study_goals` has 0 rows. A save with weekdays returns 503 until it is applied. | None | Clean | None |
| `web/revise-events-1016` (wt-w2g) | `db0cda5b` | `GET /api/me/badges` (16 badges), `run_weeks_3` and `first_hold` milestones in `/api/me/rhythm`. | 34 pass | None | None | Clean | None |
| `web/parity-you-1016` (wt-w2e) | `9a5620c0` | Progress page shows the app's 16 badges and personal bests. Uses `/api/me/badges` when present and falls back to the same rules over papers. | 32 pass | None | None | **Conflicts with batch 3: `RhythmCard.jsx` (3 hunks) and `progress.css` (1).** Batch 3 puts the week card first. This branch rebuilds the same card. | None |
| `web/college-search-1016` (wt-w2f) | `ce55ded0` | One shared matcher for college and programme search (BCOM, B.Com, b com, bcom hons all work). Keyboard-safe fields. | 12 pass | None | None | Clean | None |
| `web/compass-card-1016` (wt-w4-compass) | `19bb9b89` | One Admission Compass line on Today: programmes open to your subjects, one key, nearest college with its 2026 Round 1 cutoff. | 10 pass | None | None | Clean | None. The nearest college also appears in the My colleges card below it. |
| `web/timed-nudge-1016` (wt-w3-nudge) | `a085c1e8` | First timed mock: one honest line and one key on Today, on a practice result and in the Lab's empty block. | 15 pass | None | None | **Conflicts with batch 3 in `today/page.jsx` (2 hunks), `AnalyticsPageClient.jsx` (2) and `package.json`.** | The agent's own headless run at 390 and 1440, Night and Day. Lab: only 390 Night after the final wording change. |
| `web/help-faq-1016` (wt-w3-faq) | `6eace7ce` | `/help` page in the arena (six questions) and a Night / Daylight / Match device switch in the sidebar and More sheet. | 7 pass | None | None | Clean | The agent's own headless run at 390 and 1440, Night and Day |
| `web/copy-1016` (wt-w3-copy) | `2b84dbd9` | Copy pass in 22 files: arrows, ALL-CAPS labels, "Premium" to "Pro", raw error text. | No test files | None | None | **Conflicts with `web/rival-mobi-1016` in `AIRivalArena.jsx` (1 hunk).** | None. The rival arena, moderation and bulk upload need a look. |
| `web/rival-mobi-1016` (wt-w2h) | `c1ff52e9` | Rival result reveal: numbers first, then one Mobi act for the outcome. | 5 pass | None | None | See copy above. | **None.** RAM ran out. |
| `web/funnel-calls-1016` (wt-w3-funnel) | `72b2cadf` | Server-side funnel calls (first practice, first mock, first repair, pricing, checkout, payment), counted once per person. `/admin/funnel` gets an "After sign up" section. | 25 pass | `20261016120000_funnel_product_steps` (undo exists). Staging: applied. The undo ran on PGlite only. **Not in production.** **Its number collides with `20261016120000_question_option_stats`**, which is already live. The Supabase CLI keys migrations by this prefix, so rename it (for example `20261016120100`). | `FUNNEL_ENABLED=true` (off today) | Clean | None. The change is admin-only text. |
| `web/auth-cache-1016` (wt-w4-auth) | `524d9ccc` | Verifies access tokens locally (`getClaims` plus issuer and audience checks) and caches the identity row for 30 s. Columns are selected instead of `select(*)`. | 27 pass (the agent reports 79 for `test:auth`) | None | Reads `NEXT_PUBLIC_SUPABASE_URL` | **Conflicts with `fix/security-2-1016` in `data/db.js` (1 hunk).** | None. No UI. |
| `web/egress-1016` (wt-w4-egress) | `e3fbb7b9` | Narrower question reads on result, check and repair paths. The inventory cron reads 22 columns. Attempts reads take a column list. | 29 pass | None | Reads `CUET_EVIDENCE_SIGNING_KEY` (existing) | **Conflicts with `fix/security-2-1016` in `recovery/route.js` (2 hunks).** | None. No UI. The saving is about 11 MB a day, not the audited 33 to 36 MB. |
| `web/credit-rpc-1016` (wt-w4-rpc) | `bb37a57f` | Credit consume fast path, one-query leaderboard, and an optional destructive trim of factory job payloads. | 3 pass | `20261016160000_credit_consume_fast_path` and `20261016160100_leaderboard_group_by` (undos exist). The optional trim is in `supabase/optional/` and deletes about 30 MB of data. Staging: functions applied and checked inside rolled-back blocks. Staging had 0 wallets and 0 ledger rows. The undo was not run on staging. **Not in production.** | None | Clean | None |
| `web/art-1016` (wt-art-web) | `c69ab308` | Business Studies briefcase: 5 web image files. | n/a | None | None | **Binary conflict with the landing on `obj-business.v2-256.webp`.** | None. The agent's pick is D3 and its own note says the owner's OK is pending. |
| `fix/feed-keys-1016` (wt-w4-feed) | `8c89175a` | `/api/questions/feed` no longer returns the answer key. A signed ticket plus a new `POST /api/questions/[id]/answer`. | 28 pass | None | Optional `FEED_TICKET_SECRET`. It falls back to `NEXTAUTH_SECRET`. | Clean, except the `package.json` line. | None. `QuestionCard` is changed and was never seen. **Breaks installed app builds on Explore until the app is updated** (see section 6). |
| `play-f4` | `3faa82ab` | The account-deletion page names the app (`MockMob: CUET UG Prep`, `in.mockmob.app`). This is a copy-only change that Play wants. | n/a | None | None | Clean | None |
| `sec-tests` | `7b2e20aa` | `auth_security.test.mjs` (443 lines) and a bound on the local email-login bucket map. | **Not re-run.** The branch is 190 commits behind and I did not want to create a worktree. | None | None | `package.json` line only | None |

### 2.4 Unfinished work, not on a branch tip

| Branch | State | Needs |
|---|---|---|
| `web/repair-retry-1016` (wt-w3-retry) | At 4db57fc5. About 1,100 lines in the wip ref and the dirty worktree. | Finish, test, commit. |
| `web/plan-meta-1016` (wt-w3-plan) | At 4db57fc5. About 1,200 lines in the wip ref and the dirty worktree. A newer write at 16:35. | Check whether an agent is live, then finish and commit. |
| `web/breakui-1016` (wt-w3-breakui) | At 4db57fc5. About 280 lines in the wip ref and the dirty worktree. | Finish, test, commit. |
| `web/egress-practice-1016` (wt-w4-practice) | At 4db57fc5. About 224 lines changed in 5 tracked files, plus a migration. No snapshot. | Finish or drop. |
| `web/a11y-1016` (wt-w3-a11y) | At 4db57fc5, clean, no work at all | Re-run the agent or drop. |

### 2.5 Old lineages (drop)

- `feat/ai-reply-report` ff230163: superseded. `web/ai-report-1016` cherry-picked it.
- `fix/web-state-home` (4 commits, 192 behind): the older visitor-state home page. The owner rejected the restructure line on 15 Oct. The logo B switch it carries is already on main.
- `web/ia-1015`, `feat/web-redesign`, `feat/web-redesign-p2`, `web/W1.1` to `W1.5`, `web/W2.1` to `W2.4`: the rejected restructure lineage ("kept for salvage only"). Nothing from it is wanted.
- `codex/connected-study-suite`: one 5 Oct commit of deployment receipts (3 files). Irrelevant.
- `web/land2-perf-1016`: a duplicate of `web/land2-1015` at the same tip, carrying only the unmeasured global `inlineCss` experiment.

### 2.6 App-only exclusions, and web leftovers inside them

`feat/app-and-web` is 230 commits ahead and carries 9 migrations. All 9 are already identical on main. The rest of its non-Flutter work is on main by a different SHA.

Web files it has that main does not:
- the `/app` promotion page, the `AppBand`, `AppCta`, `AppNudge` and `HandoffQr` components, the QR encoder, and `DuShortlistSection`;
- `scripts/backup/weekly-db-dump.ps1`.

Hold the app promotion until Play is live. Take the backup script when the owner provides `SUPABASE_DB_URL`.

## 3. Conflict summary

Each branch merges cleanly into main. Against batch 3 these four do not:
- `web/parity-you-1016` and `web/timed-nudge-1016` (real conflicts);
- `web/ai-report-1016` (STATUS.md only);
- the landing.

Pairwise among the others, real (non-`package.json`) conflicts are only:
- `security-2` with `auth-cache` (`data/db.js`);
- `security-2` with `egress` (`recovery/route.js`);
- `rival-mobi` with `copy` (`AIRivalArena.jsx`).

Almost every pair also conflicts on the single `test:*` script line in `package.json`, because each branch appends its test file to the same line. Resolve by taking the union. Merge the branches one at a time and re-run the suites after each.

## 4. Proposed composition and order

### Batch 3 (the next deploy)

Contents: `deploy/batch-1016c` only (slice 5, Mobi moments, arena pass 2).
1. Snapshot the 22 uncommitted fixer files into a ref.
2. Review them against the critic list, add anything the fixer did not reach, and commit.
3. Run the suites and `npx next build --webpack`.
4. Run a visual re-check of the changed pages only (Result replay, Pro modal and pricing in Day, Progress, Today) at 390 and 1440, Night and Day.
5. Run an independent verifier.
6. Push, then check Vercel for runtime errors.

It is already in production's database. The slice 5 tables are applied, and no new migration or flag is involved. Do not add anything else to it, because `parity-you` and `timed-nudge` conflict with it. Merge them after it ships.

### Batch 3a (backend hotfix lane, independent of batch 3, can ship first)

Order:
1. `fix/security-1016` (repo catches up with production).
2. `fix/security-2-1016`.
3. `fix/nta-index-sig-1016`.

They touch no UI and merge cleanly with each other apart from the `package.json` line. They need suites and a verifier, but no visual critique. Before the deploy, apply `20261016170100_webhook_event_lease` to production. It matters before payments go live tonight, because a duplicate webhook delivery is otherwise not guarded. Apply `20261016170000_browser_roles_least_privilege` too. The agent's evidence says nothing in the site or the app reads those tables with the browser key, but run one signed-in smoke on the local staging site afterwards. After the deploy, rebuild the NTA index and run `scripts/nta-engine-run.mjs`.

### Batch 4 (features; rebase onto shipped batch 3 and 3a)

Merge in this order, with the suites after each.
1. `web/revise-events-1016`, then `web/parity-you-1016` (badges API, then the page that consumes it). Resolve `RhythmCard.jsx` against batch 3's week-first layout.
2. `web/weekdays-1016` (migration first).
3. `web/ai-report-1016` (migration first).
4. `web/college-search-1016`.
5. `web/compass-card-1016`.
6. `web/timed-nudge-1016`. Resolve `today/page.jsx` and `AnalyticsPageClient.jsx` against batch 3.
7. `web/help-faq-1016`.
8. `web/copy-1016`, then `web/rival-mobi-1016`. Resolve `AIRivalArena.jsx`.
9. `web/funnel-calls-1016`, after renaming the migration. Leave `FUNNEL_ENABLED` off.
10. `web/auth-cache-1016`. Rebase onto 3a first (the `data/db.js` conflict). Check the Supabase JWT signing key type first: with a legacy HS256 secret it quietly falls back to `auth/v1/user` and saves nothing.
11. `web/egress-1016`. Rebase onto 3a first.
12. `web/art-1016` and `play-f4`.

Visual gate: Today (colleges, Compass, nudge), Progress (badges), Account weekly goal, the Rival result, Help and the device switch, the cutoff checker and combination planner with the keyboard open, `/privacy`, and the Lab empty state. None of `rival-mobi`, `college-search`, `weekdays`, `compass-card` or `parity-you` has been looked at in a browser. If the gate is too wide, cut `rival-mobi`, `copy` and `art` to batch 5.

### Batch 5 and after

- The landing: merge main in first (`MobileDock.jsx` and `package.json` conflicts), settle the round-7 `inlineCss` question, run critic round 7 (the last score is 85, the target is 90 or more), then the owner's local look. Do `art-1016` before it so its image conflict is resolved once.
- `fix/feed-keys-1016`, together with the app change.
- Finish and gate `repair-retry`, `plan-meta`, `breakui`, `egress-practice` and `a11y`.
- `sec-tests`, once re-run.
- Everything app-side.

## 5. Production migrations to apply

Production holds, per its migration history and the STATUS entries: trap_atlas, revise_cards, my_colleges, app_errors, funnel_daily, question_option_stats and its refresh v2, `questions_private_to_browser_roles`, and `nta_question_index` (empty).

| Migration | Branch | Staging dry run | Apply when | Note |
|---|---|---|---|---|
| `20261016170100_webhook_event_lease` | security-2 | applied, column dropped and re-added, PGlite undo | before payments go live, and before or with 3a | Code falls back if the column is missing. |
| `20261016170000_browser_roles_least_privilege` | security-2 | applied, undone, re-applied, anon denied | with 3a, then a signed-in smoke | Wide grant change on 23 tables. |
| `20261016110000_study_weekdays` | weekdays | applied, undone, re-applied | before the batch 4 deploy | Additive. |
| `20261016140000_ai_reply_report` | ai-report | applied, undone, re-applied | before the batch 4 deploy | The route is 503 without it. |
| `20261016120000_funnel_product_steps` (rename to `...120100`) | funnel-calls | applied, PGlite undo only | any time before `FUNNEL_ENABLED=true` | Decide whether to pre-flag existing users. |
| `20261016160100_leaderboard_group_by` | credit-rpc | applied, EXPLAIN on 1 row | optional, with batch 4 | Code falls back if missing. |
| `20261016160000_credit_consume_fast_path` | credit-rpc | applied, semantics tested in a rolled-back block, no volume data, undo not run | **hold** | See "drop" below. |

Not on any list: the checkpoint says production lacks some older repo migrations (`submit_rival_battle`, `nta_paper_shortfalls`, the answer-correction tables). The code calls `submit_rival_battle` from `scoreRivalBattle.js`, so the Rival battle submit may fail on production today. Verify with a read-only check before any batch 4 deploy that touches the Rival screen.

## 6. Drop, hold, and what only you can decide

**Drop**
- `20261016160000_credit_consume_fast_path`. It rewrites the money path to save milliseconds. The audit's own numbers are 2,702 calls and 127 s in total since April. Staging had no wallets to prove it on. Keep the leaderboard function if you want it. The lesson from slice 5 (v1 looked fine on small data and timed out at production volume) applies.
- The optional factory-job payload trim. It is destructive and was not requested.
- The practice-verdict migration in wt-w4-practice until that work is finished. Its number collides with credit-rpc.
- The old lineages in section 2.5.

**Hold for the app**
- `fix/feed-keys-1016`. Installed app builds read the key from the feed. After it deploys, Explore shows "no usable answer key" until the app changes (five steps listed in its report).

**Yes or no questions you asked about**
- Shared rate limit: `PERSISTENT_LIMITS_ENABLED=true` in Vercel. Today each serverless instance keeps its own in-memory counter, so a limit of 10 per minute is really 10 per minute per instance, and the production table `persistent_rate_limits` has 0 rows. With the flag on, the count is shared across instances through the database function `take_rate_limit`. The cost is one extra database call per limited request, and if that call fails the request is refused. Money is not exposed either way (credits are reserved atomically in the database). The review recommended yes.
- Leaked-password protection: a Supabase Auth setting. When on, Supabase refuses a password that appears in the HaveIBeenPwned breach list when someone sets one. The review found it off and recommended yes. Your sign-in is mostly an email code, so it affects only the password path.
- Both are yours to change.

**Owner decisions waiting**
- OK on the Business Studies briefcase for the website copy.
- `new_best` badge rule (any same-format attempt, or only Full and NTA mocks).
- Accept the up-to-1-hour revocation window that local token verification brings.
- Whether to pre-flag existing users in the funnel.

## 7. Risks to check first on the next session

1. Snapshot the uncommitted files in wt-polish and wt-w4-practice. No ref holds them.
2. A write landed in wt-w3-plan at 16:35, after the crash. Check for a live agent before touching it.
3. The checkpoint says "NTA index live" and "NTA start drops to 0.4 MB". That is no longer true. The table is empty and NTA is on the full read.
4. Production's migration history does not list the older October migrations, so I could not confirm drift from it alone.
