# Handoff: Key cards, 31 Oct afternoon session (about 1:00 pm IST)

**Session:** 16f96fa8, Claude Opus 5.5 (orchestrator). It continues `HANDOFF-2026-10-31-KEYCARDS-2.md`.

**Owner's words at the start:** "keep going keep building and perfecting more and more things and if you feel like
everything is done then lmk".

**State in one line:** the feature is built, reviewed, hardened and walked on a device. The content is larger and
cleaner. The question pools are audited, with every fix prepared. Nothing is pushed, deployed or written to production.

## UPDATE, about 4:50 pm IST: 218 off-syllabus questions pulled (owner: "Pull them all")
- **Production:** the 218 are `is_cuet_syllabus = false`, `pending`, `frozen`. The morning's 25 pull-outs are frozen too:
  `pending` alone left them served, because a verified, active row is visible. Dry-run then apply; undo saved.
- **Files:** `docs/brain/intel-1031/off-syllabus-2026-10-31/` (README, list.json, pull.sql, undo.sql), main 0149bf45b.
- **Thin chapters:** Accountancy, Financial Statements of Company, 1; Political Science, Recent Issues and Challenges, 4.
- **Lesson for any future pull:** set `exploration_state = 'frozen'` with `status = 'pending'`.

## UPDATE, about 1:35 pm IST: Key cards ON
- **Flag:** owner: "Turn it on". KEY_CARDS_ENABLED=true in Vercel Production, redeployed as dpl_7dHWVGYYCxR753iJ8wW6Ppgaoyx4.
- **Smoke:** the routes answer 401 signed out (they were 404 off), all pages 200, no errors.
- **Decks:** traced into the function bundles (checked with a local build).
- **Watch next:** the first signed-in student requests in the runtime logs (`[keycards]` warnings would mean a deck failed to load).

## UPDATE, about 1:20 pm IST: production steps DONE (owner: "Yes, run them")
- **Deployed:** main is 5c1d03a37, plus STATUS f3ebd6b9c. Live as dpl_jzeVzYF2yT6F8EwUQxM9EcnPvPau with KEY_CARDS_ENABLED off. **Rollback point:** dpl_5QtNxZUkLvxXBWxJfJLDL6tLxaXE.
- **Migrations applied after rolled-back production dry runs:**
  - syllabus_v2
  - syllabus_v2_fix_live_rows: 8 live chapters had no row because of an id collision; there are now 199
  - key_cards
- **Re-tags:** 85 and 476, all moved.
- **Flawed questions:** 59 fixed (3 keys, 31 rewords, 25 pending).
- **Smoke:** clean. No runtime errors.
- **Full record and undo order:** docs/brain/STATUS.md (top entry on main).
- **Still the owner's:**
  1. Look at the screens, then turn KEY_CARDS_ENABLED on (Vercel env, then a redeploy).
  2. Decide on the 218 outside-syllabus questions.
  3. App version 17 build.

## Where everything is (under `C:\Users\atish\Desktop\mockmob copy\`)

| Part | Branch / place | State |
|---|---|---|
| **Web integration** | `web/1031-keycards` at 5c1d03a37 (`wt-1031-keycards-web`), 36 commits since 90fddb40d | Everything below is merged. origin/main has not moved (0b7d6bc03), so the merge to main is a fast-forward. |
| **App** | `ui/1031-keycards` at 98c41a73e (`wt-1031-keycards-app`) | Device walk plus fixes; the web's display rules ported and checked against 383 real cards; the Must-know taste; new cards by chapter; offline and first-visit lines. analyze clean; keycards, learn and review unit and golden folders pass (779). |
| **Content pipeline** | `ncert-books/` (not in git) | Drafts, reviews, round-2 fix lists (`fixlists2/`), gap links (`links/gap-*.json`), audit (`audit/`), and the briefs (GAP, CONFLICT, FIT-AUDIT, dated 2026-10-31). |

## What changed this session

1. **Code review and fixes.** All 22 findings are fixed with tests. Write-up: `docs/brain/intel-1031/CODE-REVIEW-2026-10-31.md`.
   - **The four high findings:**
     - state reads capped at 1,000 rows
     - an older offline replay crashing the scheduler after a Free review was charged
     - lapsed-Pro queues the student cannot play
     - the validator quarantining 40% of cards on its next run
   - **Review RPC:** reviews now go through one transactional RPC (`key_card_review`, `client_key` replay key).
   - **Late reviews:** an older replay is logged as `late` and not rescheduled.
   - **Paging:** every list read is paged.
   - **Free:** sees only taste cards in its queues.
   - **Re-tagged questions:** they keep their evidence.
   - **UI:**
     - one timestamp per card on retry
     - the "unknown" chapter state
     - per-reason Free copy (`keycard_new`, `keycards`)
2. **Real decks on the web screens.**
   - **Preview mode:** a dev-only real-deck preview (`/preview/arena?...&decks=real`). It is off in production, with a test pinning that.
   - **Polish from real content:**
     - book names normalised
     - journal entries laid out as entries
     - lists, formulas and multi-line backs
     - rounds of 20 in Study
     - English cards
     - home headings
   - **Shots:** `wt-1031-kc-realdeck/tmp/walk-1031/realdeck/` (Night full, Day subset).
   - **Printed quotes:** NCERT's printed single quotes are restored where the text extraction had a backtick (36 cards).
3. **App on a device.** The emulator walk (demo mode, six real NCERT chapters, Pro and Free, Night and Day, font scale 2.0) found and fixed:
   - rating keys below the fold
   - run-together lists and entries
   - a 157 ms frame on a 165-card deck, now 5 ms
   - middle dots
   - no source on English cards
   - squeezed chapter rows
   - "the line you needed" missing on practice results
   - Revise and home counts disagreeing
   - two demo blockers

   Shots: `wt-1031-keycards-app/tmp/walk-1031/app/`.
4. **Content.**
   - **Published:** 5,800 cards (was 5,721).

     | Subject | Cards |
     |---|---|
     | Accountancy | 868 |
     | Business Studies | 900 |
     | Economics | 1,193 |
     | Biology | 1,394 |
     | Political Science | 1,096 |
     | English | 349 |

     **Held back:** 143, each with its reason, including 49 duplicates.
   - **Gap pass:** for every unlinked live question, either link the card a first pass missed, or write a new card for the NCERT line that decides it.
     - **Links:** 2,144 (was 1,632). Accountancy 1,072, Economics 296, Business Studies 267, Biology 235, English 155 (the first English links), Political Science 119.
     - **New cards:** 60, each through an independent review, which flagged about half and kept them out.
   - **Conflict sweep:** 18 cards held back where NCERT says two things that cannot both be true. Examples:
     - Kargil dates
     - North-East reorganisation
     - discount on issue of debentures: "during the life time" on p. 81 against "in the year of issue" on p. 106
     - Shareholders' Funds
     - the agriculture share
     - RBI and coins
     - BPM6
     - frame-shift
     - the species-area slope

     Files: `docs/brain/intel-1031/conflicts-2026-10-31/`.
   - **Fix round 2:** 88 held-back cards recovered after a fix and a re-review.
   - **Duplicate sweep:** 49 cards that repeated another card's fact held back. Their links point to the kept card.
     File: `conflicts-2026-10-31/duplicates-resolved.json`.
5. **Live question pools audited.** Read-only, 2,875 questions in the five NCERT subjects. Write-up: `docs/brain/intel-1031/POOL-AUDIT-2026-10-31.md`.

   | Finding | Count |
   |---|---|
   | OK | 69% |
   | Wrong chapter | 515 |
   | Outside CUET 2026 | 218 |
   | Not decidable from NCERT | 95 (Political Science 52 of 251) |
   | Flawed | 50 |

   - **Accountancy is mostly templates:** about 849 of 1,405 live questions are a handful of templates repeated.
   - **Fix in code (no data change):** the practice and mock picker now takes at most 2 copies of one template stem per paper, filling with more only when nothing else is left (eb70694c5).
   - **Live re-tag ready:** 476 verified chapter moves. Every non-template move was read in full by a second agent.
     - File: `data/syllabus/retag-live-2026-10-31.json`.
     - SQL: `docs/brain/intel-1031/retag-live-2026-10-31.sql` plus its own undo.
     - Applied through the syllabus v2 hook after that migration.
     - The moved questions keep their evidence; inventory logic is now version 4.
   - **Flawed questions ready:** 59 questions, each batch with `fix.sql` and an exact `undo.sql` (`docs/brain/intel-1031/answer-keys-2026-10-31/README.md`).
     - 3 key fixes
     - 31 rewords
     - 25 out of the pool
   - **Why not applied:** the session's permission check blocked the production write, so these wait for the owner.

## Verification (integration 5c1d03a37)

| Suite | Result |
|---|---|
| keycards | 67 |
| keycards-ui | 23 |
| syllabus | 24 |
| nta | 229 |
| subjects | 61 |
| learning | 357 |
| today | 120 |
| egress | 101 |
| recovery | 637 (3 known todo) |
| health-egress | 56 |
| mock selector | 5 |
| practice parity | 8 |

**Known failures, not code regressions:**
- **study 61/62:** the WordNet licence test fails on base too.
- **test:app 985/987:** two landing CSS regex tests fail on this checkout's CRLF line endings. Base, with LF, passes all 987.

**Build and lint:** `next build --webpack` and lint passed at cc3e9d6f0. The last commit after that is deck data only.

## What waits on the owner (in order)

1. **Look at the screens.**
   - Web: `wt-1031-kc-realdeck/tmp/walk-1031/realdeck/`.
   - App: `wt-1031-keycards-app/tmp/walk-1031/app/`.
2. **Production database** (each step: dry-run, then apply, with the undo saved).
   1. `20261031130000_syllabus_v2.sql` with the 85-question re-tag. This is the pool shrink: Biology -18%, Chemistry -15%, Computer Science -14%.
   2. `20261031140000_key_cards.sql`.
   3. The live re-tag, 476 moves.
   4. The flawed-question batches, 59.
   5. A decision on the 218 outside-syllabus questions.
3. **Deploy.** Merge `web/1031-keycards` to main (a fast-forward), deploy with `KEY_CARDS_ENABLED` off, then turn it on.
4. **App version 17.** Bump the version and build from `ui/1031-keycards` once the web is live. With the flag off, the app hides Key cards.

## Not done, worth doing next
- **Re-flagged cards:** about 16 from round 2.
- **English:** only Vocabulary, Correct Word Usage and Match have links. Passage questions have no cards by design.
- **Distinct Accountancy questions:** the cure for the template-heavy pool. Write them only when the owner asks.
