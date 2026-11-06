# Mob v3 server, Phase A (R7)

Branch `web/1019pm-mob-v3` in `wt-1019pm-mobsrv` (from 4af47969). Spec: `docs/design-decisions/pass-1019pm/mob-v3/MOB-BUILD-SPEC-V3.md`, with D127-D133 and C-dec 2. Nothing was pushed or deployed, and production was not touched.

## What was built
**Migrations** (each with `supabase/undo/<name>.undo.sql`):
1. `20261020100000_mob_v3_core.sql`
   - 6-character codes beside the 8-character ones.
   - `mobs.name_key` and `show_podium`.
   - `mob_profiles`, `fold_unlocks`, `mob_reactions`, `mob_seen`, `mob_step_outs`.
   - Functions: create_named, settings_set, profile_set, fold_grant, sticker, step_out, seen_mark.
   - `mob_state` and `mob_invite_lookup` replaced, keeping all their old keys.
2. `20261020100100_mob_v3_games.sql`
   - Tables: games, runs, answers, start_claims, mics, quest_ticks (no user id), weeks, traps, fix_checks.
   - Functions: open, run_start, answer, run_finish, game_json, picks_closed, settle, quest_week and quest_tick, mic_give, start_status, fix_issue and fix_answer, trap_get, weeks_list.
   - `mob_record_sitting` and `mob_extra_record` replaced (same signatures); they now tick the quest.
3. `20261020100200_mob_v3_chains.sql`
   - Tables: chain_prefs, chain_pauses, mob_chain_best.
   - Functions: chain_daily, chain_fixes_held, chain_state, pause set and clear, prefs_set, the two best bumps, mob_unlock_facts.
4. `20261020100300_mob_v3_realtime.sql`
   - The schema only, for Phase B: tickets, `mob_room_ok` (the only security definer), the two realtime.messages policies, revoke-on-leave and revoke-on-block triggers, and room ticket, start and cancel.

Every new table has RLS on, no anon or authenticated policy, and service_role only.

**Pure rules:**
- `src/lib/mob/`: `names.mjs`, `folds.mjs`, `starts.mjs`, `games.mjs` (places, ties, moments, trap, Wednesday window, ghosts, ghost pace, public question), `quest.mjs`, `mobChain.mjs`.
- `src/lib/chain/chain.mjs`.
- `model.mjs`: `CODE_RE` takes 6 or 8 characters, plus `codeFromBytes(bytes, 6)`, `displayCode` and the 32 new error sentences.

**Server:**
- `src/lib/server/mob/games.js`: the v3 service, including `checkUnlocks`.
- `src/lib/server/chain.js` and `src/lib/server/mob/memberId.js`.
- `service.js` (view.v3, create and join take `fold` and `nameKey`, 6-character invites, lookup name, paper start without the free claim), all behind `MOB_V3_ENABLED`.
- `http.js`: 20 v3 actions and 9 limits from spec 2.5.
- `deps.js`: `MOB_V3_ENABLED`, `MOB_LIVE_ENABLED`, `PLAY_BILLING_ENABLED`.
- `accountDeletion.js`: 14 new steps.

**Routes:** `PATCH /api/mob/settings`, `PUT /profile`, `GET /shelf`, `POST /sticker`, `/mic`, `/step-out`, `/seen`, `POST /game`, `GET /game/[id]`, `POST /game/[id]/run|answer|finish`, `GET /game/[id]/podium|review`, `POST /fix/start|answer`, `GET|PATCH /api/me/chain`, `POST|DELETE /api/me/chain/pause`.
- `MOB_V3_ENABLED` not `true` gives 404 `MOB_DISABLED`.
- Old routes keep their shape. GET adds only `mob.v3`; with v3 off, the bytes are unchanged (tested).

## Tests (in `npm run test:mob`)
- `data/tests/mob_v3.test.mjs` (30 tests) covers:
  - start rules and the billing flag;
  - free-start and mic races, and leave-and-rejoin;
  - marks, places and ties, private marks and the podium switch;
  - the F1 leak scan;
  - ghosts, moments and the trap;
  - quest and step-out;
  - unlocks and the shelf;
  - Fix it together and the Wednesday check;
  - RLS denial for anon and authenticated;
  - Realtime payload keys and room auth on stubs;
  - account deletion;
  - copy lint;
  - migrations: apply twice, undo twice, and the schema returns byte for byte.
- `data/tests/mob_v3_chain.test.mjs` (37 tests, more than 90 cases): IST boundary, skips, passes, the cap, make-up, open, pause, held fixes, hidden, best, Cutting, and the SQL.
- `data/tests/mob_v3_contract.test.mjs` (2 tests): 30 fixtures from real responses in `data/tests/fixtures/mob_v3/*.json`, compared byte for byte with ids normalised.

Suite results:
- test:mob 147/147;
- test:recovery 610 pass, 0 fail;
- test:auth 110/110;
- test:app 841 pass, 0 fail;
- test:billing: 1 false positive fixed (see the last section).

Lint is clean. `next build --webpack` passes. Plain `next build` (Turbopack) panics on the node_modules junction ("Symlink points out of the filesystem root"); that is environmental, and every web worktree has it.

## Staging dry run (onwkqxmjqjrhfbjjdydu only)
1. Took a pre-v3 snapshot hash over every mob, chain and fold function, column, constraint, trigger and policy, plus the realtime policies: `024b5d35...` (269 objects).
2. Applied the four migrations (`mob_v3_*_staging`).
   - The first smoke test failed: staging's 8-character check is named `mob_invites_code_check1`, because the parked v1 table kept the plain name.
   - Fixed in the migration: the check is now found by its definition and recorded in `mob_data_moves`, and the undo puts it back under that name. A PGlite test covers this.
3. Smoke test in one rolled-back transaction, using 4 staging test users:
   - a 6-character invite and its lookup;
   - free start ok, second `start_used`;
   - marks 20, 19, 19, 13; a retry returned `exists` with marks unchanged;
   - picks are null before close and 4 rows after;
   - `game_json` runs carry no picks;
   - settle, then `already`;
   - check `not_yet` before Wednesday; two right checks give `fixed_now`;
   - quest 19 of 60;
   - past pause refused;
   - anon and authenticated denied tables and functions;
   - a ticket gives `room_ok` true, and leaving makes it false.
4. Undo of all four (`mob_v3_undo_all_staging`): the snapshot hash went back to exactly `024b5d35...` (269).
5. Re-applied all four (`*_staging_reapply`). The 47 v3 function bodies on staging hash to `e0207bcf...`, identical to the repo files applied on PGlite.
   - Staging is now ON v3: 18 tables with RLS, 2 realtime policies.
   - Security advisor: only the expected notice that `mob_room_ok` (security definer) is executable by authenticated, by design (spec 2.4).

## Production apply order (owner's yes first)
1. Deploy the code with `MOB_V3_ENABLED` unset. It is safe before the migrations: everything new is gated.
2. Apply `20261020100000_mob_v3_core` → `..100100_mob_v3_games` → `..100200_mob_v3_chains` → `..100300_mob_v3_realtime`. Before that, read-only check the mob_invites check name; the core handles any name.
3. Set `MOB_V3_ENABLED=true`. Leave `MOB_LIVE_ENABLED` unset (Phase B). The Realtime "Allow public access" switch is Phase B's owner step.
4. **Undo:**
   - `MOB_V3_ENABLED` off first;
   - then the undo files in reverse: realtime, chains, games, core.
   - Undo loses v3 data (games, quests, Folds, chains settings).

## Where the routes differ from spec section 3 (for the app)
- **Question indexes:** `q` is 0-based everywhere (answers, review, trap, fix). Traps and moments add `number` (1-based) for the copy "Question 4".
- **Moment fields:**
  - `fastest_right` gives `{q, number, seconds}`;
  - `quickest_finish` gives `{count, seconds}`;
  - `three_in_a_row` gives `{from, to}` (1-based);
  - `all_right` and `finished_all` give `{count}`.
  - "Fastest" and "quickest" are true only for the one run that holds them.
- **Moment keys:**
  - `quest_done:<mobId>:<week>` and `stitch:<mobId>:<week>` carry the Mob id, because seen-keys are per student;
  - `reveal:<fold>` and `chain:<n>` are as the spec has them.
- **The chain's day-14 pass:** day 14 gives a pass (the 2.3 algorithm and C1 copy: "one every 7 days"). The 0.4 milestone table said 14 gives none; `milestones[].reward` for 14 is `rest_pass`.
- **Tally:** needs `right_n > 0`, so three all-skip games do not earn it.
- **Fix it together:**
  - `fix/start` `question` also has `answered`;
  - `trap` also has `number`;
  - an unknown `q` gives `Q_INVALID`.
- **Review:** `trap.fix.check` also has `state` (`not_yet|open|closed|done`). `trap.fix.now` is `open|done`.
- **Errors:**
  - `RUN_EXPIRED` puts `{run:{finished, marks, answered, count}}` in `error.detail`;
  - `FOLD_LOCKED` is 409, as in the 3.2 table (3.1's create text said 422).
- **Lookup (v3):** keeps the old keys (`valid`, `code`, `expiresAt`) and adds `status` and `name`. Invite adds `display`.
- **starts:**
  - adds `micFrom: {memberId, name}` when a mic is held;
  - a Free member with an unused start AND a mic gets `via: free_weekly` with `mics: 1`, because the free start is used first.
- **v3 extras:** `mobChain` adds `restarted`; den `games[]` adds `title`; `reactions[]` adds `game` when set.
- **Quest labels:** "This week's Mob paper", "Riya's sprint", "Extra paper on X", "Fix it together". They are ordered by most answered.
- **Fixtures** are in `data/tests/fixtures/mob_v3/` (30 files, ids normalised to `uuid-N` and `member-N`).

## Left, or risky
- **The weekly paper holding its answers until Sunday (C-dec 2 item 1): NOT DONE.**
  - Why: answers for a Mob paper leave through the shared practice runner (instant checks), the result page, `/api/attempts/[id]` and review. That is a cross-cutting change to non-Mob code paths that build 9 depends on.
  - Plan: behind `MOB_V3_ENABLED`, strip `correctIndex` and `explanation` from attempts tagged `selection_meta.mobPaper` until `closesAt(week)` (extras: `closes_at`), and run Mob papers without instant checks. This needs its own spec slice and an app change.
- **Phase B is not built:** room routes (ticket, start, cancel), the `LIVE_BUSY` cap (`MOB_LIVE_MAX_ROOMS`) and `auth()` exposing `authUid`. The SQL for them is in migration 4 and is tested.
- **Not built:**
  - `/admin/funnel` v3 metrics;
  - `scripts/mob/seed-v3-staging.mjs`;
  - the web UI (spec: later).
- **Product caps:** 3 open games and 1 room per Mob are enforced. The 30-room global cap is Phase B.
- **Mob chain week passes** are computed and not written back to `mob_weeks.pass_used`.
- **One test outside the Mob changed:** `data/tests/first_full_mock_1019.test.mjs` failed because the v3 core migration contains the string `first_full_mock` (Naav's earn source). Its scan now skips `_mob_v3_` files.
- **Exposed function:** `mob_room_ok` is callable through PostgREST by signed-in users. It only answers whether the caller holds a live ticket for a topic.
