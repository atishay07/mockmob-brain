# Vision inventory, 16 Oct 2026 (read-only audit, about 03:00 IST)

Scope: every vision item and spec item, web and app separately. Nothing was edited, committed, pushed or written to a database. Evidence is git (one shared store), the Vercel MCP (read-only), two read-only SELECTs on production Supabase, and three GETs and one empty POST on www.mockmob.in.

Status words: **LIVE** (on origin/main 77713336, which Vercel shows as the READY production deployment; file cited), **BUILT** (finished on a branch, not live; branch and commit), **PARTIAL**, **MISSING**. "v9" is the newest APK sent (tmp/apk/MockMob-v9-ef0d1128.apk, built from feat/app-and-web ef0d1128).

## 0. Summary

1. **Mistake Lab v4 is mostly built and mostly live.** Slices 1, 2 and 3 are on main on the web (merged: slice 2 as f83d4dcb, whose own Vercel build failed and shipped with the 48309076 redeploy; slice 3 as 3fc0095b) and in the app (v9). Slice 4 (trap tag, Traps you meet, Same mistakes later, Revise, key-quality loop) is built on web/lab4-1015 (f2d12263) and in the app on ui/phase2 (27f90c1b), **not live on either**, and needs two production migrations first. Slice 5 (cohort time) is **missing**. The owner's memory that "v4 had already been built" is right.
2. **Repair v3 and the post-mock SWOT are live on web and app.** A live repair on 16 Oct 02:16 cost USD 0.00035 with all v3 fields (CTO-LOOP). The fresh check on 2 new questions (spec A.9) was never built. FRESH_CHECKS_LIVE is not a web flag at all; in the app it only opens a notification channel.
3. **No regression was found on the live site.** Between 11e30ec3 (before website v2), 48309076, 3fc0095b and 77713336 no file was deleted, and the only larger removals are intentional replacements (old Lab bar by the ledger, "1 credit" lines by the two-pool spend line, NTA row by the app-style deck). Section 6 lists the evidence and the few things that look like loss to a visitor.
4. **Why the live site still feels like a regression** (causes, in order of weight):
   - A lot of the last session's work is built but not live: the landing de-slop and hero (web/land2-1015), Lab slice 4, Mobi rig v2, My colleges, one name per concept, concept checks, crash reports (all but land2 are already merged into deploy/batch-1016, 16 commits ahead of main, not pushed). In the app, v9 lacks the whole of ui/phase2 (16 commits of finish work, You hub, credits, Mobi v2, slice 4, crash reports).
   - **The Lab has almost no data to show.** Production has 1,815 attempts, **8 with a usable timeline (3 accounts)**, 9 attempts in the last 30 days, newest 15 Oct 02:05 UTC. The owner's own papers predate the slice 2 capture, so every old paper renders the `basic` ledger and none of Replay, trace lines or Across your mocks. One fresh timed mock fixes his account (he plans it for the morning of 16 Oct).
   - The live hero is the old hero: static "CUET 2027. One mock. A clearer next step." The `lp-title__morph` span has no CSS and `MorphWord.jsx` is orphaned (not rendered anywhere), so the "moving morphic design" and coloured "CUET 2027" he noticed missing really are absent from live. The branch version that restored them (8fb2b670) was then replaced by hero v4 "nothing ambient" (b6c40be4). That contradiction needs his decision (Section 5, item G1).
5. **Production database is behind the code**: tables trap_atlas, revise_cards, funnel_daily, nta_question_index and app_errors do not exist; no my-colleges table either. Confirmed by a read-only query. Code that needs them is inert (funnel, NTA index) or not deployed (slice 4, colleges, crash).

## 1. Mistake Lab v4 (tmp/mistake-lab-v4/SPEC.md), one row per item

Web file paths are on origin/main unless a branch is named. App paths are under flutter_app/lib on ef0d1128 (v9) unless ui/phase2 is named.

### Slice 1: marks ledger, re-mark, how others answered

| Item | Web | App | Notes |
|---|---|---|---|
| Marks ledger, 7 groups adding to the gap, fixed bands (2 min, 20 s) | LIVE `data/mistake_lab.js`, `src/components/result/MarksLedger.jsx`, `data/mistake_lab.copy.json` | LIVE `features/result/full/lab_ledger_section.dart`, `core/models/mistake_lab.dart` | `ready`, `basic`, `none` states; old bar is the fallback when `lab` is missing |
| Headline gate (12 marks or 15%), do lines, legend disclosure, Q chips | LIVE same files | LIVE | |
| Bar split motion, played once per attempt | LIVE `marks-ledger.css` | LIVE (CustomPainter) | |
| First-pick re-mark ("Your first picks, re-marked") and "See every change" | LIVE `mistake_lab.js`, copy `remark` | LIVE | |
| How others answered, per-option counts and 2 px bars | LIVE `src/components/result/OthersAnswered.jsx`, wired in `ResultPageClient.jsx:380` | LIVE `answer_row.dart` | |
| "Most others got it right" ledger line (n 20+, Wilson) | LIVE `data/cohort_picks.js`, `lab_mistake` cohort items | LIVE | |
| Cohort snapshot data | LIVE `data/cohort/question_picks.v1.json`: 461 questions, 21 Apr to 15 Oct 2026, built 15 Oct 02:05 UTC | reads server lines | Spec said about 545; 461 pass the n 10 gate. Static; refresh by hand (`scripts/cohort/build-question-picks.mjs`) |
| Time and decisions (pace, median, time split, every change) kept | LIVE `data/time_decisions.js`, `result/TimeDecisions.jsx` | LIVE (server lines) | |
| SWOT stops repeating the paper's behaviour items | LIVE `data/mock_swot.js` (`ledgerGroups`, `ledgerCovers`) | LIVE (server) | |
| Old observation cards retired when the ledger shows | LIVE `ScoreRecoveryLab.jsx:110` | LIVE | |
| Lab above "After this mock", renamed "Mistake Lab" | LIVE `ResultPageClient.jsx:314,317` | LIVE `full_result_screen.dart` | |
| Preview with real builder on sample data | LIVE `/preview/arena?view=result&mock=full` (`previewMock.js`) | n/a | |

### Slice 2: capture, one time rule, Replay

| Item | Web | App | Notes |
|---|---|---|---|
| Server accepts end, away, back, strike, via, marks, client meta | LIVE `data/recovery.js` (`END_REASONS`, `VISIT_VIA`, 5,000-event cap) | n/a | Server first, as specified |
| Runner capture: end event, away/back, strike-outs, via, marks kept, attempt meta | LIVE `src/lib/runnerCapture.js` (RUNNER_CAPTURE 2), `test/TestPageClient.jsx` | LIVE `core/sync/session/session_engine.dart`, `session_journal.dart` (recordPresence, recordStrike, recordMark, recordEnd, via), `session_submitter.dart` (`client`) | On by default in the app (`kRichSessionEvents`, define MOCKMOB_CAPTURE_V2). Cohort table (capture row 7) is slice 5 |
| One time rule (away subtracted, last question to the end event) | LIVE `data/paper_trace.js`; `prepos_insights.js` and `session_recovery.js` now call it | LIVE `core/domain/paper_trace.dart` | Retires the three disagreeing rules |
| Replay: 10-minute rows, bars by result, picks, changes, flags, away gaps | LIVE `src/components/result/Replay.jsx`, `data/replay.js`, `mistake_replay.js` | LIVE `features/result/full/replay_section.dart` | |
| Row ends ("By 20:00: 14 answered. Even pace: 16"), three facts under the grid | LIVE copy `replay` | LIVE | |
| Filter chips in the ledger's words; "See it in the replay" from each ledger row | LIVE `Replay.jsx` (`focus`) | LIVE | |
| Play in 15 s, range input, arrow and Shift-arrow stepping; reduced motion Previous/Next | LIVE `Replay.jsx` header comment and code | PARTIAL: drag scrub; haptic at question boundaries not verified | |
| Tap a bar opens that answer with its trace | LIVE | LIVE | |
| Trace lines: later visit vs without leaving, marked for review, away not counted, crossed out the key, last question "until you submitted", "Time ran out" | LIVE copy `trace` (5, 5, 2, 7, 3 hits), `paper_trace.js` | LIVE (server lines) | |
| "Crossed out the key" ledger group | LIVE `mistake_lab.js`, `lab-cinema`-free; Lab copy | LIVE `lab_ledger_section.dart:337` | Needs a paper taken after the capture shipped |
| Passage sets and submit sheet counted correctly (rules 5 and 6) | LIVE `runnerCapture.js` | LIVE | |

### Slice 3: the record, Rule book, the loop

| Item | Web | App | Notes |
|---|---|---|---|
| Across your mocks (second thoughts, when changes help, never opened, long stays, last 10 minutes), gated | LIVE `data/across_mocks.js`, `result/AcrossMocks.jsx`; same component on Analytics `analytics/AnalyticsPageClient.jsx` | LIVE `features/rules/widgets/across_mocks_view.dart` | Spec also named the app's You page; not verified there |
| Rule book: repair rules plus four paper habits with Wilson band and 3-mock gate | LIVE `data/rule_book.js`, `src/components/rules/RuleBook.jsx`, `/review/rules` | LIVE `features/rules/screens/rule_book_screen.dart` | |
| "Use in my next mock" (writes recovery_playbook) | LIVE `src/lib/server/ruleBook.js`, `/api/me/rules` | LIVE `rules_data.dart` | Table exists in production |
| Start sheet line ("Your rule for this mock") | LIVE `src/app/(app)/dashboard/StartRule.jsx` | LIVE `features/rules/widgets/start_sheet_line.dart` | |
| Rule check in Prove after the next mock | LIVE `result/RuleCheck.jsx`, `data/rule_book.js` | LIVE `rule_check_view.dart` | |
| Repair order by cohort ("Repair Q12 first", hero key) | LIVE `data/repair_order.js`, `result/labLoop.js` | LIVE `core/domain/repair_candidates.dart`, `models/lab_loop.dart` | |
| PrepOS reads pace and change numbers from paper_trace | LIVE `data/prepos_insights.js` | n/a | |

### Slice 4: traps and spaced return

| Item | Web | App | Notes |
|---|---|---|---|
| Trap atlas table and fill from committed v3 repairs, format rules (assertion-reason, match, sequence) | BUILT web/lab4-1015 4997a913 (`data/trap_atlas.js`, `option_hash.js`, `src/lib/server/trapAtlas.js`); in deploy/batch-1016 (0474b36b) | BUILT ui/phase2 ff002b4c (contract), 27f90c1b | **Needs migration `20261015210000_trap_atlas.sql`**, not applied (table absent). The atlas fills only as paid repairs commit (6 existed at audit time), so format rules carry the first weeks |
| Trap tag under the wrong option | BUILT df6352c0 `result/TrapTag.jsx` | BUILT 27f90c1b `features/result/widgets/trap_tag.dart` | |
| Traps you meet, "Falling" / "Still catching you" | BUILT df6352c0 `TrapsMeet.jsx`, `/api/me/traps` | BUILT 27f90c1b `traps_meet_view.dart` | |
| Same mistakes later (1, 3, 7, 21 days, cap 10 a day, no credits) | BUILT `SameMistakesLater.jsx`, `data/revise.js` | BUILT `same_mistakes_later_view.dart` | **Needs `20261015210100_revise_cards.sql`**. Truth review f2d12263 made it promise only what Revise holds |
| Revise page (F1 folded in) | BUILT `src/app/(app)/review/revise/page.jsx`, `/api/me/revise` | BUILT `features/review/revise/*` (ui/phase2) | |
| Key-quality loop (wrong option picked by 20+ and more than the key goes to re-check) | BUILT `scripts/cohort/key-quality-loop.mjs`, `src/lib/server/keyQuality.js`; dry run by default | n/a | A script, not automatic. Owner readings flagged in handoff: retirement reading; 13 flagged vs 5 with a 20 gap |

### Slice 5 and the rest

| Item | Web | App | Notes |
|---|---|---|---|
| Nightly `question_option_stats` table and refresh | MISSING | MISSING | Table does not exist in production |
| Cohort time lines ("Students who got this right took a median of 51s"), changed-here, crossed-out-key-here, "twice as long" ledger finding | MISSING | MISSING | Gates (30 and 20 students) cannot pass today; no timed cohort |
| Shared anchor questions in NTA papers | MISSING | MISSING | Owner decision 5, deferred |
| Folded: F4 "never opened across mocks", F5 Rule book, F1 Revise | LIVE (F4, F5); BUILT (F1) | LIVE (F4, F5); BUILT (F1) | |
| Cut: self-tagged reasons, Your chapters, Paper formats, Week in review | cut (not found in main) | K0 removed the screens (per handoff) | Matches spec |

## 2. Repair v3 and SWOT (tmp/repair-v3/SPEC.md)

| Item | Web | App | Notes |
|---|---|---|---|
| A.1 screen order, trap-label heading, "Explained from the answer key (D)" chip | LIVE `src/components/recovery/MistakeRepair.jsx`, `data/repair_presentation.mjs` | LIVE (Repair v3 merge 34046de9, v5 APK) `features/review/*` | |
| A.2 schema v3 (trap, why_wrong, why_right, contrast, others, rule, hook, another_way), maxTokens 1,400, aliases, `REPAIR_PROMPT_VERSION` rollback | LIVE `data/mistake_repair.js` | reads fields | Default 3; `1` rolls back |
| A.3 what the model is sent (subject, topic, type, reference explanation) | LIVE `mistake_repair.js` | n/a | |
| A.4 validation (fitSentence, claimsAboutStudent, contradictsKey, others coverage) | LIVE `mistake_repair.js`, `repair_failures.js` | n/a | |
| A.5 cost | LIVE; measured 850 in, 524 out, USD 0.00035 (16 Oct 02:16) | | One live repair done by the owner's account |
| A.6 "From your record" lines | LIVE `data/mistake_insights.js`, `attempt_ledger.js` | LIVE (server lines) | |
| A.7 trap pattern line | LIVE `data/repair_pattern.js` | LIVE | Counts only v3 receipts |
| A.8 honest loading line (8 s, 45 s), arrival stagger, Mobi states | LIVE `repair_presentation.mjs` `REPAIR_LOADING` | LIVE | |
| A.9 **fresh check on 2 new questions** (GET/POST `/api/recovery/repair/check`, signed ticket, free, "Checked" = 2 of 2) | **MISSING** (no route, no view) | **MISSING** | The only fresh check live is Prove's "5 fresh questions" (`/api/recovery/replay`). Older episode-based fresh checks exist but are behind `RELEASE_GATES.content` (Section 4) |
| A.10 free vs credit, two-pool spend line | LIVE `src/lib/creditCopy.mjs`; `RepairCost` in `MistakeRepair.jsx` | PARTIAL: credits page and total-cost line are in ui/phase2, not v9 | |
| B SWOT (states, ledger L, items, caps, basis line, Do these next, plan links, motion) | LIVE `data/mock_swot.js`, `src/components/result/SwotPanel.jsx`, `SWOT_ENABLED` kill switch | LIVE `features/result/full/swot_section.dart` | |
| B.4 plan follow-through ("A set on this chapter on 16 Oct: 7 right of 10") | LIVE (`later` line) | LIVE | Not tied to the exact plan item (D.5-4) |
| D.5-2 app recap card 2 shows top 2 SWOT items and plan[0] | n/a | MISSING (no SWOT in the recap code) | |
| D.5-3 marked for review used by the SWOT | MISSING (marks are stored and drive Rule book habit 4 and trace lines, not the SWOT) | MISSING | |
| D.5-4 plan item id in selection_meta, dashboard takes several chapters | MISSING | MISSING | |
| D.5-5 inventory-aware `untried` | MISSING | MISSING | |
| CEO decision 16 Oct 02:20: paid repair becomes a learning loop (retry before the key, fresh checked question on the same rule, rule back on Revise, personal trap pattern, ask a follow-up) | PARTIAL: trap pattern LIVE; Revise BUILT (batch); retry-before-key MISSING; fresh question MISSING (A.9); follow-up to Ask Mobi MISSING | PARTIAL: same | Scope next, after this inventory |

## 3. Owner vision V1 to V18 and queue Q1 to Q14 (docs/brain/CTO-LOOP.md)

| Item | Web | App | Notes |
|---|---|---|---|
| V1 distinctive app, not a copy of the site | n/a | PARTIAL (ongoing) | |
| V2 premium glass and motion (HIGH, Revolut, Fampay) | PARTIAL: Q11 motion language, haptics, number memory, full-size objects LIVE (merged q11, q11b) | PARTIAL: v9; finish work in ui/phase2 | |
| V3 Mobi everywhere, better rig | PARTIAL: emotion kit LIVE (`MobiReact`); rig v2 as SVG BUILT web/mobi-1015 5b2038f2 (`/preview/mobi`, mid-motion never viewed) | PARTIAL: rig v1 in v9; rig v2 BUILT ui/phase2 0fab673d (`mobi_rig_data.dart`) | Q6 |
| V4 motion judged in use | PARTIAL | PARTIAL | no recordings by owner rule |
| V5 balanced, one spacing system, Night/Day parity | PARTIAL | PARTIAL (30 critic findings, Section 5) | |
| V6 memorable post-mock moments, supportive streaks | PARTIAL: recap not on web; Lab replay LIVE | LIVE recap and milestones | Share card deferred to January |
| V7 plain exciting copy, no defensive sub-remarks | PARTIAL: landing copy LIVE (G2/G3); English pass BUILT web/land2-1015 (36975c6c, 45f4d838); names BUILT web/names-1016 457550cb | PARTIAL: copy pass Q3 not found as a separate commit; fixtures in critic still show fine print (finding 8) | |
| V8 Mistake Lab as the USP | LIVE slices 1-3; BUILT slice 4; MISSING slice 5 | same (app slice 4 in ui/phase2) | Section 1 |
| V9 website takes the app's clarity, mobile-first landing, arena desktop-first | LIVE v2 (8b845719, f42b898c one gesture one step, footer sign-up, explanatory illustrations, speed pass); arena pass 3 LIVE (9bb41032); landing de-slop BUILT, partly cut: land2 685ecfae with WIP d9c3c52f unchecked | n/a | |
| V10 state-aware website | LIVE signed-in front page opens Today or onboarding (`ArenaEntry.jsx`, 9bb41032); landing dock that follows visitor state BUILT land2 ee755002 | n/a | |
| V11 sign-in that just works | LIVE Google and email fixed; email-login RPC guard applied | LIVE (owner added the redirect; Google working 15 Oct 14:58); 403 insurance LIVE in v9 (24665cac) | PARTIAL: `GOOGLE_WEB_CLIENT_ID` empty so no native one-tap; phone sign-in off |
| V12 NTA exam-faithful, CUET-fit, newest questions | LIVE (r5, `data/nta_pool.js`) | LIVE | Index table not built, see flags |
| V13 CUET tools in the flow | PARTIAL: My colleges BUILT web/colleges-1016 35e8a7e9 (not live) | PARTIAL: Compass hierarchy and first move BUILT ui/phase2 610bab23; tools packet in v9; colleges tab (audit section 4) MISSING | |
| V14 You and Profile as a hub | PARTIAL: account page with credits LIVE | BUILT ui/phase2 c3a6fe7a (hub, one-tap theme, study days); avatar sheet LIVE in v9 | |
| V15 Ask Mobi with credits, two names | LIVE two pools and history (`/api/me/credits`, `profile/CreditsSection.jsx`, 08dd50e8) | PARTIAL: Ask with credits in v9; credits page BUILT ui/phase2 (5e95a34c contract) | |
| V16 stay on free plans (fixes 1-5, backups) | LIVE fixes 1-4 (3be06112) and 5 (d9e290eb, kill switch PRACTICE_SLIM_READ=off); A6 index code LIVE but table absent; backup is an owner step | n/a | |
| V17 consent-first analytics, funnel | LIVE code (`/api/funnel`, `src/lib/server/funnel.js`, admin view), **off and table absent** | LIVE consent switch (`core/analytics`) | Funnel needs a migration and a flag |
| V18 Play Store release | owner steps | owner steps | key, Google client ID, Console |
| Q1 403 as retryable | n/a | LIVE v9 (24665cac); the "blocked" line on the runner's submit-pending screen and a server event still open | |
| Q2 credits page and history | LIVE | BUILT ui/phase2 | |
| Q3 copy and naming pass | BUILT web/names-1016 | PARTIAL | |
| Q4 one My colleges list | BUILT web/colleges-1016 (server, web, migration `20261016090000_my_colleges.sql` not applied) | PARTIAL: contract fixture abc0635c only | |
| Q5 You as hub | PARTIAL | BUILT ui/phase2 | |
| Q6 Mobi quality pass | BUILT web/mobi-1015 | BUILT ui/phase2 | |
| Q7 Lab slice 4 | BUILT | BUILT | |
| Q8 / Q8b usage fixes and self-maintaining NTA index | LIVE code; production table and key MISSING | n/a | |
| Q9 arena on phones pass 3, critic leftovers | LIVE pass 3; leftovers PARTIAL | n/a | |
| Q10 funnel, crash reporting | LIVE funnel code, off; crash server BUILT web/crash-1016 a0dbf9dd (`app_errors`, not applied) | BUILT ui/phase2 2ee85a16 | |
| Q11 web motion language and living objects | LIVE | n/a | |
| Q12 app finish items (bar blur 24, capsule, week skeleton) | n/a | BUILT ui/phase2 305a7be2 | |
| Q13 landing calm-down, "Get the app" banner | MISSING (after de-slop) | n/a | |
| Q14 commerce growth stack | deferred to January | deferred | |

## 4. Owner's landing notes (OWNER-VISION 15 Oct PM checklist and OWNER-NOTES 23:10)

| Ask | Status |
|---|---|
| Checklist items 1-9, 12 (mobile-first, held stories on phones, shelf, Mobi motion, calculator glitch, English, bigger practice objects, Start sheet scroll) | LIVE (f652aba0, per checklist; 10 is "first pass deployed, more queued") |
| One scroll = one slide on held stories | LIVE f42b898c; momentum hush and fast-scroll reveals BUILT land2 9a6f12f3 |
| Footer sign-up, working "Try a CUET question" | LIVE 1147259e (G2); keys without arrows BUILT land2 685ecfae |
| Hero rebuilt: no pulsing dot, no AI-looking buttons, hierarchy, not-confusing for no subject match (15-subject sample chooser) | BUILT land2 b6c40be4 and 8fb2b670; live hero unchanged (pill with dot, "Try five questions") |
| Coloured CUET 2027 and the moving morph line | **MISSING live** (see Section 0.4); hero v4 removes the morph; owner decision needed |
| Realistic Lab numbers ("no one spends 10 minutes") | PARTIAL: live max 3:18, changes up to 10:35 later; realistic set BUILT land2 85d0f4cf |
| Wasted bottom space; dock that follows state ("Welcome back / Go to Arena / Sign up"); sample-aware | BUILT land2 ee755002, b6713562 |
| Heavy-scroll glitching; Mockmob button to top | BUILT land2 9a6f12f3 (stress harness); not live |
| Repair text unreadable on phones, SWOT readability | PARTIAL: LabCinema scenes BUILT land2 28025792 (type scale); live not changed |
| De-slop rebuild (SLOP-AUDIT groups 1-3, rest group) | BUILT, partly unchecked: land2 685ecfae; removes ProductScreens, RadarField, DynamicCompassPreview, MorphWord, ChapterReadout, RecoveryPreview (about 570 lines). Check against the owner's "never simplify by cutting" before merging |
| Bottom state button for the 5-questions-done visitor | BUILT land2 ee755002 |

## 5. App UX audit (25 findings) and design critic (30 findings, packets A to L)

Audit, status in v9 or ui/phase2 (grep-checked unless noted):

| Finding | v9 | ui/phase2 |
|---|---|---|
| P0-1 Google returns to app | owner step done; native client ID still empty | same |
| P0-2 Today error card after retry | LIVE | LIVE |
| P0-3 403 = blocked, retryable | LIVE | LIVE |
| P1-4 NTA glyph overflow | claimed in merge 649c973c; not grep-verified | not grep-verified |
| P1-5 Choose colleges opens chooser | LIVE | LIVE |
| P1-6 one college list on the server | MISSING | server BUILT web/colleges-1016; app PARTIAL |
| P1-7, P1-8 Compass score and hierarchy | PARTIAL (tools hierarchy in 649c973c) | BUILT 610bab23 |
| P1-9 tools in the flow; colleges tab | MISSING (no colleges tab in either) | MISSING |
| P1-10 light/dark toggle | MISSING | BUILT (`theme_switch.dart`) |
| P1-11 avatar | LIVE (account sheet) | LIVE |
| P1-12 / 13 credits names, total cost | PARTIAL | BUILT credits screen; cost line not found |
| P1-14 back guard | LIVE | LIVE |
| P2-15, 16 road chip, board picker | LIVE | LIVE |
| P2-21 start moments | claimed in 649c973c | |
| P2-22 blur 24 | MISSING | BUILT 305a7be2 |
| P2-24 week skeleton | MISSING | BUILT |
| Help FAQ | MISSING | BUILT (`faq.dart`) |

Critic packets (docs/brain/DESIGN-CRITIC-2026-10-16.md): L kit BUILT (2a8d59d2); A Today, B Practice, C Runner, F Insights, H Tools, J Onboarding, K Rhythm: partial edits in WIP cfc81867 and c199eff1, **unchecked, analyze not run**; G You cut mid-work; D recap and result and E Review/rules/Revise: not started; I Learn: concept checks BUILT c51c996c, rest not started.

## 6. Regressions

Compared: 11e30ec3 (production before website v2), 48309076, 3fc0095b, f652aba0-era landing, against origin/main 77713336.

- **File level:** `git diff --name-status` between each of those and 77713336 shows **zero deleted or renamed files** under src/ and data/. The Lab, result page, landing components and SWOT all still exist.
- **3fc0095b to 77713336:** only 4 non-binary files with 15+ deleted lines: `scripts/nta-index-build.mjs` (49, moved to shared builder, intentional), `DashboardPageClient.jsx` (42, NTA row replaced by the app-style deck; "NTA style / MockMob style" switch, palette and mark-for-review chips are kept at lines 476-505), `subject_art.mjs`, `MockMobAIHub.jsx`. `ScoreRecoveryLab.jsx` and `MistakeRepair.jsx` only gain the two-pool credit lines.
- **48309076 to 77713336:** `lab-cinema.css`, `LabCinema.jsx`, `landing/MistakeLab.jsx` grew (235, 168 lines added); `data/db.js` is the slim practice read (A5).
- **Landing:** `src/app/page.js` and landing components are unchanged between 3fc0095b and main. Versus 11e30ec3 the landing gained the shelf, LabCinema held stories, dock and sample links; the only removed strings are the superseded hedged lines ("Illustrative demos", "not a prediction"), which the owner asked to remove.
- **Two small weaker spots, not regressions in the strict sense:**
  1. Live hero morph: `components/landing/MorphWord.jsx` is orphaned and `.lp-title__morph` has no rule, so the hero text is static. This was lost long before 48309076 (MorphWord is not used by any `page.js` from 11e30ec3 on). Owner decision G1.
  2. Slice 2's own Vercel deploy (f83d4dcb, 15 Oct about 17:30) ended in ERROR; production kept serving the previous build until the 48309076 redeploy (Google Fonts fetch retry). So slice 2 went live later than the commit log suggests.
- **Regression risks sitting on branches (would regress live if merged unreviewed):** web/land2-1015 deletes the six landing components above and the hero morph; `deploy/batch-1016` has an uncommitted line-ending change to `next.config.mjs` in wt-batch (git shows only LF to CRLF); web/ia-1015 (rejected restructure, 12 commits) must stay unmerged.

## 7. Hidden behind flags or gates

| Flag | Where | State | Turning it on needs |
|---|---|---|---|
| `FUNNEL_ENABLED` | Vercel env; `src/lib/server/funnel.js`, `/api/funnel`, admin view `/admin/funnel` | off (POST returned 204 with an empty body; production value not read) | apply `20261015233000_funnel_daily.sql` (with undo, dry run on staging), set env `true`, redeploy, send one beacon (`docs/brain/FUNNEL-INTEGRATION-2026-10-15.md`) |
| NTA question index | `data/nta_pool.js`, cron `/api/internal/rebuild-nta-index` (vercel.json, 3 crons) | code live, inert: table absent, falls back to the full read | apply `20261013190000_nta_question_index.sql`, set `CUET_EVIDENCE_SIGNING_KEY` in Vercel, run `node scripts/nta-index-build.mjs --write --allow-production` (RUNBOOK-NTA-QUESTION-INDEX-2026-10-15.md) |
| `SWOT_ENABLED`, `PRACTICE_SLIM_READ`, `REPAIR_PROMPT_VERSION` | `/api/attempts/[id]`, `data/db.js`, `mistake_repair.js` | defaults are on (3 for repair); these are kill switches | set `off` / `1` to roll back |
| `STUDY_CONTENT_ENABLED`, `STUDY_RECALL_ENABLED` | `src/app/page.js`, `src/lib/server/study.js` | on in production (the live landing shows "lessons across ... subjects") | already on |
| `STUDY_GUIDED_PLAN_ENABLED`, `LEARNING_SESSIONS_ENABLED`, `RECOVERY_PATHWAYS_ENABLED`, `SESSION_CHECK_ENABLED`, `PERSISTENT_LIMITS_ENABLED` | `src/lib/server/learning.js`, sessions check route, rate limit | production values not verified (Vercel env not read) | read them with the Vercel MCP before relying on them |
| `RELEASE_GATES.content` and `authenticatedJourney` | `data/capabilities.js` (code constants, both false) | off: gate the older episode-based Recovery pathways, delayed fresh checks and the alternate hero copy; `/recovery` still returns 200 | academic and release evidence, then a code edit and deploy |
| Razorpay Rs 99 monthly plan | `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` | owner will set (CTO-LOOP 16 Oct 02:20) | the env var; code switches automatically |
| `FRESH_CHECKS_LIVE` | **app only**: `core/config/app_config.dart`, `dart_defines/prod.json` = false | off; opens only the fresh-check notification channel and its settings row. It is not a web flag and gates no fresh-check screen | a build define plus a fresh-check feature to notify about (A.9 is missing) |
| `PHONE_SIGN_IN` | app | off | SMS provider (deferred, Q14) |
| `GOOGLE_WEB_CLIENT_ID` | app define, empty | native one-tap off; browser flow works | Google Cloud Android clients and the Web client ID (docs/AUTH.md G1-G3) |
| `MOCKMOB_CAPTURE_V2` | app | default true | already on |
| `aiReplyReportLive` | app const, false | "Report this reply" hidden | route `POST /api/ai/mentor/report` (branch feat/ai-reply-report) and the const |
| `MOBI_RASTER` | app | off | debug fallback only |
| Migrations not applied to production | batch: `20261015210000_trap_atlas`, `20261015210100_revise_cards`, `20261016090000_my_colleges`, `20261016100000_app_errors`; plus funnel and NTA index above | confirmed absent | standing DB grant: save, dry run, undo, STATUS.md entry; apply before the code that reads them |

## 8. Deploy order that would close most of the gap

1. Apply the four batch migrations (trap_atlas, revise_cards, my_colleges, app_errors) after a staging dry run.
2. Finish the batch gate (lint, suites, build, 390 and 1440 captures in Night and Day), push deploy/batch-1016: ships slice 4 web, Mobi v2 web, My colleges, crash reports, names, concept checks. Server code first.
3. Land web/land2-1015 after the de-slop check and the owner's hero decision (G1). It is 18 commits behind main and must be rebased.
4. App: make ui/phase2 analyze clean, run unit tests, open goldens, merge into feat/app-and-web, build APK v10.

## 9. Top 10 real gaps, ranked by usefulness to a student

1. **The paid repair does not yet teach.** No retry-before-the-key, no fresh checked question on the same rule (A.9 is unbuilt on both surfaces), no follow-up into Ask Mobi, and the Revise page that would bring the rule back is built but not live. The owner's verdict on the live v3 repair: explaining the key is not enough. Built-not-live: Revise (web batch, app ui/phase2); MISSING: the rest.
2. **Students cannot see the Lab on their own papers.** Only 8 timed papers from 3 accounts exist; everything older renders the plain ledger without Replay or trace lines, and nothing on the result page says "take one new timed mock to unlock this". A one-line in-product explanation and getting every tester through one fresh mock matter more than any new slice.
3. **Same mistakes later (spaced return, 1, 3, 7, 21 days) is not live.** It is the one thing that brings a student back and checks memory. Blocked only by the revise_cards migration and a deploy.
4. **Trap tag and Traps you meet are not live, and the atlas starts nearly empty** (6 committed repairs). The three format-rule tags (assertion-reason, match, sequence) work without repairs and should be what a student sees first.
5. **"How others answered" rests on a static, mostly May 2026 snapshot of 461 questions**; slice 5's nightly table and cohort time ("students who got this right took 51 s") do not exist, and no timed cohort exists to feed them.
6. **The phone app is behind the website.** v9 lacks slice 4, the You hub with a findable Night/Day switch, the credits page and history, Mobi rig v2, the evening return loop and the crash reporter. 16 unchecked commits in ui/phase2 (WIP cfc81867, c199eff1) stand between today and APK v10; critic packets D and E (recap, Review) are not started.
7. **One "My colleges" list and a colleges destination.** Built on the server and web (not live); the app has only the contract fixture; no colleges tab exists. Commerce students pick the app for admission outcomes, and Compass still asks for a score before it gives a first move (fix BUILT in ui/phase2 610bab23).
8. **Marked-for-review is stored but not used where it matters**: the SWOT, the plan and the app recap card 2 ignore it (spec D.5-2, D.5-3, and the plan-item follow-through D.5-4).
9. **The landing is the old one for a signed-out visitor**: static hero with the pulsing-dot pill, no state-aware dock, unrealistic Lab numbers, fast-scroll glitches. All fixed in web/land2-1015 but unmerged and partly unchecked; Q13 calm-down is not started. Conversion cannot be tuned because the funnel is off and its table is missing.
10. **Mobi is a mascot only at some moments.** Rig v2 (better-looking, 31 acts) is built for web and app but live nowhere; "Mobi at real moments everywhere" (CTO queue) and Learn's missing character (critic 21) are open.

## 10. Method limits

- Production environment variables were deliberately not read (they hold secrets); flag states marked "not verified" can be read with the Vercel MCP if wanted.
- App status comes from grep and git ancestry on ef0d1128 and ui/phase2, not from running the app. Items marked "claimed in merge message" were not independently checked.
- The Lab's behaviour on real data was not run; the production check was two SELECTs (counts of attempts, existence of tables). No rows were read or written.
- Branch heads move (other agents were committing while this ran): feat/app-and-web showed 6ea8772a, then eb9e0f46.
