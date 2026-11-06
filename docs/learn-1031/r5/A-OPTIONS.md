# R5 Packet A: options in a stable shuffled order (LK44)

2 Nov 2026. Branch `web/1102-shuffle` (off origin/main a16fbd62e). Nothing pushed, merged, deployed or written to a database.
No migration.

The owner saw "every answer is A" in Explore and Learn. The production key distribution confirms it: Accountancy's verified
keys were A 1,206 / B 96 / C 62 / D 41 on 2 Nov. NTA papers already shuffle per session. Every other surface served the stored
order. The fix: one permutation per question, seeded from the question id alone, applied when a question is served. Grading goes
back through the same mapping, and what is stored keeps naming the stored option.

## The design

- **One helper**, `data/option_order.js`. `servedRow(row)` calls the NTA engine's own `ntaServedRow` (data/nta_item_checks.js)
  with a fixed seed (`mockmob-options:stable-1`). The order therefore depends only on the question id, and it is the same for
  every student and every surface.
  - **Kept-order items.** The engine's `shuffleBlockers` keep the stored order for these:
    - options that name other options ("All of the above", "Both A and B", "None of these", "option 2");
    - single-label options;
    - a conventional last option ("No error");
    - a stem that names an option;
    - an explanation that names an option in a way that cannot be rewritten;
    - a key that does not resolve.
  - **What moves with the order.** Served letters A-D are given in served order. The key (`correct_index`, `correct_answer`)
    and the explanation's letter references ("Option B is correct") move with their options. Stored self-letter prefixes
    ("A. ...") are removed.
  - **The order array.** `order[i]` is the stored index served at position i, the NTA engine's `nta_option_order` convention.
  - **Other entry points.** `servedOut` and `outOrder` do the same for questionOut-shaped questions (data/db.js). The mapping
    helpers are `storedIndexOf`, `servedIndexOf`, `storedKeyAt`, `storedLetterOfServed` and `servedLetterOfStored`.
  - **The rule for callers.** Stability needs the same inputs on every surface: options, stem, key and explanation. Every
    caller reads all four. That is why the Learn content read and the Revise item read now include the key and explanation;
    neither is sent to the client.
- **What is persisted.** Option identity: the stored index or the stored option's own letter, never a served letter. Old rows
  (served in stored order) and new rows therefore mean the same thing. A paper snapshot keeps what the student saw, plus
  `optionOrder`, as NTA snapshots already do.
- **In flight across the change.**
  - **Learn run items.** These carry `ov: 'stable-1'`. A run started before the change (no `ov`) is served and graded in the
    stored order until it ends (48 hours).
  - **Rival battles.** These carry `metadata.optionOrder`, and a battle without it is graded as before.
  - **Mob papers and games.** A paper or game of a week starting before **9 Nov 2026** (`STABLE_ORDER_FROM_WEEK` in
    src/lib/mob/model.mjs) keeps the stored order. No frozen paper changes order while its Mob is sitting it, and an old
    week's side-by-side shows the letters its members saw. **If this ships after 9 Nov, move that date to the first Monday
    after the deploy.**

## Surfaces

### Before the change

| Surface | Shuffled before | What was persisted | Who reads it later |
|---|---|---|---|
| NTA papers (`data/db.js getNtaPaper`) | yes, per session (`ntaServedRow`, key = generation key) | attempt snapshot with `optionOrder`, `details[].givenIndex` (served index) | result, review, mistakes; identity readers (option_compare, cohort_picks, trap_atlas) |
| Practice papers: quick, full, other modes (`getQuestions` → `questionOut`) | no | snapshot (stored order), `givenIndex`, progress `last_selected_key` = letter at that index | result, review, mistake lab, repair, cohort, trap atlas, paper trace |
| Recovery sessions (`recoverySessions.js`) | no (NTA mode: yes) | as practice, plus `recovery_sessions.events` (served index) | as practice |
| Learn v2 runs (`learn.js`, index in `learnHttp.js`) | no | event `choice` + body `{key, choice}`, progress `selected_key`, interaction `selected_key` (letters) | Learn replay, Revise seeding (flag only), progress |
| Explore feed (`/api/questions/feed`) and Saved (`/api/bookmarks`) | no; key and explanation sent, graded on the client | `/interact`: interaction `metadata.selected_key`, progress `last_selected_key` / `last_correct` (letter) | Revise seeding (flag only), progress |
| `/api/questions/explore` (public, no key) | no | nothing; no caller in src or the app | n/a |
| Revise (`/api/me/revise`) | no | `revise_cards` only (box, day, key_hash of the key text) | Revise |
| Mob weekly, extra and Full mock together papers (`mob/deps.js loadQuestions`) | no ("quick papers never shuffle options") | snapshot, `givenIndex` → `mob_sittings.picks`, `mob_game_runs.answers` | compare (letters), trap, together, mark sheets |
| Mob race and round (`games.js`, `publicQuestion`) | no | `mob_game_runs.answers.pick` (index), `correct` | review, podium, Fix it together, settle trap |
| Mob Fix it together (`fixStart` / `fixAnswer`) | no | `mob_fix` result (`correct` only) | den |
| Rival (`createAIRivalBattle` / `scoreRivalBattle`) | no | `selected_answer` (index), `is_correct` | nothing found |
| Repair check, Mobi thread check (`repair_check.js`) | no, deliberately (explanations cite letters) | offer `optionHashes` (display order), pick, progress via stored letter | check replay, Revise cards (key_hash) |
| Session check (`/api/sessions/[id]/check`) | follows the snapshot | `session_check_log.answer` (served index) | snapshot readers |
| Result review, attempts/[id], mobile/attempts | follows the snapshot | n/a | n/a |
| Study runs (study_content items) | not bank questions; out of scope | | |
| Key cards option choice | not question options (the part picker) | | |

### After the change

| Surface | Now | Grading | Persisted (identity) |
|---|---|---|---|
| NTA papers | unchanged (own per-session shuffle) | snapshot | progress `last_selected_key` is now the stored letter through `optionOrder` |
| Practice papers and recovery sessions | stable order (`servedQuestionOut`); snapshot carries `optionOrder` | snapshot, unchanged | snapshot as served + `optionOrder`; progress = stored letter |
| Learn v2 | stable order (index, content fallback, answer read) | served letter → stored option | event `choice`, progress, interaction `selected_key` = stored letter; interaction `served_key`; the event body keeps what was seen plus `order` |
| Explore and Saved | stable order; served `correct_answer` and remapped explanation; `option_order: 'stable-1'` | client: served key; `/interact`: served letter → stored | interaction `selected_key` = stored, `served_key` = served; progress = stored letter |
| Revise | stable order | served index → stored, then compared with the stored key; `keyIndex` returned as served; explanation remapped | `revise_cards` unchanged |
| Mob papers (weeks from 9 Nov) | stable order, one for every member; orders kept on `selection_meta.mobPaper.optionOrders` | snapshot | `picksFromAttempt` maps through the orders → stored indices |
| Mob race, round, Fix it together (weeks from 9 Nov) | stable order | served pick → stored, then compared with the stored key | `answers.pick` = stored index; review shows `yourPick` and `correctIndex` as served |
| Mob compare and trap letters (weeks from 9 Nov) | letters as served | n/a | picks unchanged (stored) |
| Rival | stable order (`metadata.optionOrder`) | served index → stored | `selected_answer` = stored index |
| Repair check, Mobi thread check | offered in stable order (`offeredHashes`); explanation letters rewritten | hashes → stored (unchanged machinery) | unchanged |

### The app (wt-1101-learn-app/flutter_app, read only)

No change is needed. The app renders the options each route sends and posts back what it was served:

- **Learn:** `POST /api/learn/runs/:id/answer {choice}`, the served letter.
- **Revise and repair check:** the served index.
- **Practice, Mob and Mob v3:** the served index.
- **Explore stream:** `selected_key` is the served letter, with `is_correct` computed against the served `correct_answer`.
  `/interact` reads every posted letter as served, so no `option_order` is needed from the app.

The app keeps its own copy of `contract_later_v1.json`. The web copy was rebuilt: same shape, but the answers' `keyIndex` is
now a served index. Re-sync the app copy only together with its Revise golden.

## Key distribution

Script: `node scripts/option-order-distribution.mjs <exportDir> [--all]`. It is offline and read-only. It serves every
verified live question through the shared order and checks that Learn (`learnServed`), Explore and Saved (`feedServed`),
practice and Mob papers (`servedOut`), the Mob race (`publicQuestion`), Revise (`reviseItem`) and the repair check
(`offeredHashes`) all serve the same order and key.

The data is the read-only production export of 13 Oct 2026 (`mockmob-hotfix/tmp/nta-fixtures`, `scripts/nta-fixture-export.mjs`).
It is older than the 2 Nov numbers above: its Accountancy has 1,246 A keys where production now has 1,206 (verified).
Production was not read.

| Subject | Verified rows | Before A / B / C / D | After A / B / C / D | Kept in order |
|---|---:|---|---|---:|
| Accountancy | 1,487 | 84 / 9 / 5 / 3 % | 27 / 24 / 25 / 24 % | 38 |
| Biology | 379 | 68 / 16 / 12 / 4 | 26 / 26 / 25 / 23 | 10 |
| Business Studies | 435 | 40 / 22 / 25 / 12 | 28 / 27 / 22 / 23 | 9 |
| Chemistry | 300 | 64 / 22 / 9 / 4 | 28 / 21 / 25 / 26 | 0 |
| Computer Science | 331 | 66 / 21 / 8 / 5 | 29 / 27 / 22 / 23 | 11 |
| Economics | 483 | 55 / 20 / 14 / 11 | 26 / 27 / 22 / 24 | 19 |
| English | 277 | 39 / 24 / 19 / 18 | 30 / 24 / 23 / 23 | 10 |
| General Test | 154 | 74 / 19 / 6 / 1 | 18 / 32 / 27 / 23 | 1 |
| Geography | 182 | 81 / 9 / 8 / 2 | 31 / 26 / 21 / 22 | 10 |
| History | 197 | 75 / 17 / 7 / 2 | 32 / 20 / 23 / 24 | 8 |
| Mathematics | 282 | 75 / 15 / 7 / 2 | 27 / 26 / 22 / 26 | 5 |
| Physics | 320 | 75 / 16 / 7 / 2 | 25 / 26 / 26 / 23 | 3 |
| Political Science | 198 | 72 / 20 / 7 / 2 | 31 / 22 / 28 / 19 | 10 |
| Psychology | 87 | 47 / 24 / 23 / 6 | 17 / 33 / 21 / 29 | 1 |
| Sociology | 212 | 60 / 21 / 15 / 4 | 25 / 23 / 30 / 22 | 3 |
| **All** | **5,324** | **68 / 16 / 10 / 5** (3,636 / 863 / 545 / 280) | **27 / 25 / 24 / 24** (1,446 / 1,334 / 1,290 / 1,254) | **138 (3%)** |

The 138 kept items, by reason:

| Reason | Items |
|---|---:|
| The option refers to other options | 98 |
| The explanation names an option | 20 |
| A conventional last option ("No error") | 19 |
| The stem names an option | 1 |

Unresolved keys: 0. Surfaces disagreeing with the shared order: 0. Small subjects (Psychology 87, General Test 154) vary more
around 25% by chance.

## Tests and suites

New tests:

- **`data/tests/option_order.test.mjs`** (7 tests, also in `test:learn` and `test:option-order`):
  - stability across calls and surfaces;
  - every permutation appearing, with about 25% per key over 2,000 all-A ids;
  - grading round trips;
  - kept-order items, and explanation rewriting;
  - stored letters and object options;
  - old rows: Mob picks without orders, weeks before 9 Nov, compare and trap letters with and without an order;
  - repair checks offered in the stable order and marked by the option picked.
- **`learn_routes`** gains two tests:
  - an answer persists the stored letter (event, progress, interaction) and returns the served key;
  - a run started before the change keeps the stored order to its end.

Updated tests choose answers by meaning, not by letter: learn_routes, learn_preview, revise, repair_check_flow,
repair_check_followups. egress_misc now allows the Revise item read to include the explanation. Mob tests are unchanged: their
weeks are before 9 Nov.

Each suite was run on this branch and on a clean a16fbd62e worktree:

| Suite | This branch | a16fbd62e |
|---|---|---|
| test:learn | 389 / 0 | 381 / 0 |
| test:recovery | 637 / 0 | 637 / 0 |
| test:mob | 344 / 7 | 344 / 7 |
| test:billing | 453 / 0 | 453 / 0 |
| test:nta | 229 / 0 | 229 / 0 |
| test:egress | 101 / 0 | 101 / 0 |
| test:answer-integrity | 11 / 0 | 11 / 0 |
| test:attempt-reads | 12 / 0 | 12 / 0 |
| test:learning | 357 / 0 | 357 / 0 |
| test:app | 984 / 0 | 984 / 0 |
| test:keycards | 82 / 0 | 81 / 0 |
| test:keycards-ui | 40 / 0 | 40 / 0 |
| test:today | 146 / 0 | 146 / 0 |
| test:health-egress | 56 / 0 | 56 / 0 |
| test:study | 61 / 1 | 61 / 1 |
| test:question-reorder | 25 / 0 | 25 / 0 |
| test:auth | 141 / 0 | 141 / 0 |
| test:subjects | 62 / 0 | 62 / 0 |

The failures on this branch are the same tests that fail on the base:

- **test:mob (7).** These are date-bound v3 tests: SV-1, SV-5 to 9, SV-10/11, SV-15, SV-17, L-55, and the room ticket on
  leave.
- **test:study (1).** The content gate's quarantine test.

ESLint is clean on every changed file.

## Not covered, and risks

- **The deploy window.**
  - A page or app screen loaded before the deploy and answered after it posts a letter from the old order:
    - Explore and Saved: `/interact` reads it as served, which affects only that progress row and interaction.
    - Revise: an item fetched before is graded through the new order.
  - Learn runs, Rival battles, Mob papers and games, and practice papers are safe: they carry their order or a marker, or they
    are graded from their snapshot.
- **The Mob date.** `STABLE_ORDER_FROM_WEEK = '2026-11-09'` must move if this ships after 9 Nov. Weeks before it keep the
  stored order.
- **Content edits after serving.**
  - Explore and Saved, Revise, the Mob race and Rival recompute the order from the live row at answer time. An edit between
    serve and answer that flips a kept-order verdict (an option or explanation newly naming another option) would change the
    order for that one question.
  - Snapshot surfaces and Learn's `order` are not affected. Mob papers keep their orders on the attempt.
- **Kept items are still mostly A.** The 138 kept-order items (3%) keep their stored keys, mostly A. Rebalancing them needs a
  content change, not a serve-time order.
- **Not changed:**
  - `/api/questions/explore`: no caller, and no key is sent.
  - Study runs: not bank questions.
- **Not looked at in a browser.** No screen layout changed; only the option order and letters changed. The web and app
  screens were not visually checked in this packet.
