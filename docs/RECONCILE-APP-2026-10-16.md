# Reconcile: the app (ui/owner-1016), 16 Oct 2026 evening

Read-only pass. Nothing was pushed, deployed, applied to a database, signed in or run on a device. The only writes are this file and scratch copies under the session scratchpad.

## 0. What was run, and when (read this first)

- **Tree reconciled:** `C:\Users\atish\Desktop\mockmob copy\wt-owner`, branch `ui/owner-1016`, HEAD `ab89f591`, plus the uncommitted working tree.
  - Commits since `fd0da7d3`: `3a8bf5ba` (WIP, 115 files from the 8 stopped builders), `91a0268e` (study sections compile fix), `23efeade` (You badges, bests, badge sheet), `ab89f591` (Business Studies briefcase art).
  - **Uncommitted:** 111 files have real content changes (about 150 more show only CRLF noise), 13 new non-image files, 58 new golden PNGs (onboarding 20, review 16, rhythm 14, you 8) and 40 modified golden PNGs.
  - **The resumed builders' work is this uncommitted tree.** The crashed session relaunched 8 builders at 14:44. They died at the usage limit about 15:50 with no final reports ("agent returned nothing" in `wf_63ecb0f5-ce2`), so what they finished is only visible as files.
  - `refs/wip/wt-owner-1445` (`f4adb6b4`, 14:41) is fully contained in the current tree: no file in it is missing on disk.
- **Commands** (from `wt-owner\flutter_app`, `MOCKMOB_FLUTTER_SLOTS=2 bash tool/flutter_locked.sh`, one at a time):
  1. `analyze`, 16:42.
  2. `test -j 1 test/unit`, 16:42 to 17:26: 377 files, 4,762 tests, 32 failures.
  3. A scratch copy (junctions to `lib` and `assets`, copied `test`, two test-only compile errors patched in the copy) to run the 17 test files that could not load: 253 tests, 6 failures.
- **Not run:** `test/golden/**` and `test/widget_test.dart`. No emulator walk. Nothing here is device-verified, so "built" below never means "walked on the emulator".
- **Caveat: builders are active in wt-owner again.** From about 17:37 a resumed workflow is editing wt-owner and running analyze and tests there (processes for you/rhythm, today, onboarding, tools, review, account_sheet and core_ui were live at 17:57). Files changed after my runs ended at 17:26 include `account_sheet_test.dart`, `credits_test.dart`, `colleges_screen_test.dart`, `core_widgets_pkg07_test.dart`, `credits_data.dart`, `account_sheet.dart`, the onboarding `copy.dart`, `bank_size.dart` and `save_step.dart`, and the rhythm and `you_hub_screen.dart` files. Several of the failures below may already be fixed. Re-run before acting on any of them. I did not touch the tree.

## 1. Analyzer: 23 issues (16 errors, 6 warnings, 1 info), no error in `lib/`

| Owning area | File and line | Issue |
|---|---|---|
| Colleges | `test/unit/tools/colleges_screen_test.dart:112` | 14 errors from one cause: an apostrophe inside a single-quoted test name ("the student's course") ends the string and breaks the rest of the test. The test body below it is unfinished (it taps "B.Com. (Hons.) · Change"). |
| You (test support) | `test/unit/you/you_test_support.dart:11, 361, 401, 403` | `NetworkStatusNotifier` is imported from `connectivity.dart`, which does not export it (it lives in `connectivity_providers.dart`). 2 errors, 2 warnings. This one file stops **17 test files from loading** (section 2). |
| You | `test/unit/you/hub_test.dart:6, 8, 15` | 3 unused imports. |
| Today | `lib/features/today/widgets/road_rail.dart:533` | Warning: `debugResetMobi` is never used. |
| Today | `lib/features/today/widgets/road_section.dart:19` | Info: unnecessary import of `mascot.dart`. |

## 2. Unit tests: 4,762 run, 32 failures (as run at 17:26)

**A. 17 files fail to load (compile), so their tests never ran:**
- Cause 1, `you_test_support.dart`, 16 files:
  - `account_sheet/account_sheet_test.dart`
  - `credits/credits_test.dart`
  - `you/`: `account`, `across_on_you`, `appearance_help`, `bughunt_fixes`, `category_sheet`, `editors`, `goal`, `hub_chips`, `hub_sections`, `hub`, `motion_pieces`, `privacy`, `robustness`, `sign_out_data`.
- Cause 2: `tools/colleges_screen_test.dart` (the apostrophe above).
- With only those two compile errors patched in a scratch copy, these 17 files ran 253 tests with 6 failures (the 6 are in section B, marked "after fix").

**B. Real failures, with the owning area:**

| Area | Test | What it says |
|---|---|---|
| Shell/bar | `core_ui/core_widgets_pkg07_test.dart` "bar compact state ... compact from the first frame" | Start's word scale expected 0.933 (14/15), got 1.0. The shell builder changed `start_key.dart` (glow removed, one word size) and the old test was not updated, or the compact word-size rule is not met. |
| Shell/bar | `motion/motion_guard_test.dart` "no new Curves.ease*" | `mm_bar.dart` uses `Curves.easeOutBack` (line 881). |
| Colleges | same guard | `my_colleges_sheet.dart` uses `Curves.ease*` twice. |
| Colleges | `tools/banned_copy_test.dart` | The banned phrase "your CUET score" is in `estimate/estimate.dart`. |
| Colleges | `tools/compass_flow_test.dart` "Combo shows the website best fit..." | "Option 2" is not found: the Combo rework (progress header, step modes) changed the flow and the test was not updated, or it broke. |
| Colleges | `tools/tools_design_test.dart` "a programme the subjects open shows its cutoffs at once, with the category as a 48 dp rail" | The rail is 40 dp, not 48. |
| Colleges | `tools/colleges_screen_test.dart` "a college typed in the course search ..." (after fix) | The unfinished test cannot find "B.Com. (Hons.) · Change". |
| Today | `motion_guard` "no new bare AnimatedSwitcher" | `road_section.dart` has 5. |
| Colleges | same guard | `college_rung.dart` 1, `compass/stream_fold.dart` 1, `my_colleges_sheet.dart` 2. |
| Practice | same guard | `choice_deck.dart` 1, `suggestion_hero.dart` 1. |
| Account | same guard | `notifications/widgets/notifications_invite.dart` 2. |
| Practice | `practice/practice_order_test.dart` "at 360 by 800 ..." | The layout asserts pass (strip 128-268, card 284-504, first mode ends at 688, bar top 724). It fails only on "exactly one KeyButton": a second `KeyButton` sits in a `SectionHeading` row. The test still has `DBGKEY` and `DBGRECT` debug prints, so the builder was mid-debug. |
| Practice | `practice/tab_dock_clearance_test.dart` "quick pair starts above the bar ... 360 by 780" | The Quick practice block ends at y 704, the limit is 656. On a 780 dp phone the first mode is under the bar. |
| Review/Result | `result/full_result_test.dart` "order: summary, the Lab, Time and decisions, the first fix, After this mock, the answers" | `full_result_screen.dart` now puts "After this mock" (SWOT) right under the marks, which contradicts the Lab v4 spec 3 order the test holds. One of the two must give. |
| Review (Mobi) | `mascot/mobi_moments_one_per_screen_test.dart`, 4 Revise tests | `MissingPluginException(getTemporaryDirectory ... path_provider)`. `revise_screen.dart:901` now watches `reviewAgainCountProvider`, which opens the real drift database in a widget test. The harness needs an override. |
| Onboarding | `onboarding/step_end_of_scroll_test.dart` "with the keyboard up on the college search ..." | `rungs in view: []`: with the keyboard up no college rung is visible. This is the L30 keyboard fix not working yet (`keyboard_watch.dart` is new and untracked). |
| Art | `art/object_art_test.dart` "files on disk are exactly the renders, at the sizes declared" | `obj-business.webp` is now 685 x 582 (the new briefcase, `ab89f591`) but `core/art/object_art.dart:95` still declares `SubjectRender business ... 685, 769` with the old foot and ground metrics. The size and foot measures must be re-measured, not just the number changed. |
| You (after fix) | `you/hub_chips_test.dart`, 2 tests | A chip no longer scrolls its section to just under the row. The section keys changed with the new order. |
| You (after fix) | `you/hub_sections_test.dart` "Study days planned weekdays are named and drawn, 28 dp marks" | Fails (stack not readable in the log; the database warning is printed first). |
| You (after fix) | `you/hub_test.dart`, 2 tests | "Colleges" and "B.Com (Hons)" are not found in the hub: the courses and colleges section moved or was renamed. |

Everything else passes, including all of `test/unit/today` (new: `move_builder_partial`, `road_rail_gesture`, `road_weeks`, `colleges_card`), `rhythm` (new `badge_study_test`), `review`, `notifications`, `tools/estimate_verdict_test`, `core_ui/bar_test.dart` (alignment, six slots, scrub, semantics order) and `router_widget_test`.

## 3. The 8 areas of app-ia-1016 section 10

| Area | State | Evidence (paths under `flutter_app/`) | Missing against its brief |
|---|---|---|---|
| **Shell and bar** | Built, 2 tests failing | Six equal slots with Start third (`lib/core/widgets/bar/bar_tabs.dart`: `kBarSlots = 6`, `slotToBranch`). Colleges is branch 3 (`router.dart:286`, `routes.dart:27, 127`). `/tools` redirects to `/colleges` (`router.dart:192`). `BarIconKind.colleges` and a person icon for You. Start loses its glow. Predictive-back fix with `_onNavigation` (L04). `bar_test.dart` covers geometry, alignment, 1.3x text, scrub and semantics order, and passes. | `bar_six_*` goldens are coded (`bar_golden_test.dart:225`) but no PNG exists. Emulator ruler check not done. Compact Start word rule fails. `Curves.easeOutBack` in `mm_bar.dart`. **`/review/again` is not registered** (section 5). |
| **Colleges** | Built, mostly; 5 tests failing or unloadable | `features/tools/colleges/{colleges_screen,college_rung,colleges_copy}.dart`, `my_colleges/college_search.dart` (normaliser), keyboard-safe `my_colleges_sheet.dart`, `estimate/estimate_sheet.dart` (658 lines, the cutoff checker at `/colleges/cutoff`), `compass/stream_fold.dart`, `combo/combo_progress.dart`. "CSAS dashboard" is gone from user copy. | `my_colleges/aim_ladder.dart` (brief 2.4) was never created. The unfinished `colleges_screen_test`. Banned copy, 48 dp rail, Combo flow test, two guard violations. No Colleges tab golden. No Mobi count check. |
| **Today** | Built, mostly; guard failure only | `widgets/road_rail.dart` (815 lines: weeks as columns, draggable exam flag), `road_tuners.dart` (`PaceStrip`, `MockRuler`), `road_section.dart` rebuilt, `colleges_card.dart` replaces `college_ladder.dart`, `logic/road_weeks.dart`, `logic/plan_adjust.dart`, failure ladder (`lastTriedAt`, `refreshFailed`), auto-retry on resume. `ToolsQuietLink` removed from Today. | `plan_adjust_test`, `retry_status_test`, `hero_spacing_test` do not exist. `road_readout.dart` does not exist. The hero spacing edits of brief section 5 (`hero_stage.dart`, `number_block.dart`) are unchanged since `fd0da7d3`. Old `road_timeline.dart` is kept for the "window open" state instead of deleted. `RoadBoardGrid` still in `road_board.dart`. Road goldens (`today_road_rail` and the like) were never generated (only the old `today_road_*` PNGs). |
| **Practice and Start** | Partly; 2 tests failing | Order is now subject strip, one compact "Up next" card, "Ways to practise" deck (quick pair, Smart, Exam band), More, Concepts (`practice_screen.dart` 300-440). `default_subject.dart`, `suggestion.dart`, `suggestion_hero.dart` (compact), `more_rows.dart` (Review again row, Compass pushed straight). `subject_state_test` passes. | The first screen on a 780 dp phone fails the clearance test. A second `KeyButton` appears. `tab_order_*` goldens not generated. `quick_start.dart` NTA note edit is 4 lines. |
| **Review** | Built, mostly; 2 integration defects | `again/` (5 files), `widgets/retry_first.dart` wired into `mistake_view.dart`, `repair_api.dart` `retry_pick`, `next_from_mock.dart` on History, `review_load_failure.dart`, empty state only on a known-empty read. 24 unit test files pass. Goldens: `repair_try_*`, `repair_verdict_*`, `review_again_*`, `review_tab_rows`. | **`/review/again` has no route**, so the "Review again" row (`review_again_entry.dart:51` pushes `ReviewAgainCopy.path`) lands on the error page. `widgets/try_first.dart` (shared controller) not created. No `review_again_end` golden. Fresh check on 2 new questions (A.9) not in the app. Revise tests break on the new DB read. Result order test conflict. |
| **You (+ rhythm)** | Built; 5 tests failing (plus 14 files that did not load) | Order is study first (`you_hub_screen.dart`): this week, notifications invite, badges, bests, across your mocks, subjects, then plan and credits. `rhythm/logic/derived_badges.dart` (5 phone-derived badges), `badge_record.dart`, `fastest_answer.dart`, `screens/bests_screen.dart`, badge sheet, `goal_editor.dart` ring now shows words. New `badge_study_test` passes. 8 You and 14 rhythm golden PNGs exist. | Weekdays still phone-only (`PhoneOnlyStudyDays`, `study_days.dart:78`). The hub tests were not updated to the new order. I did not count the badges against the brief's 14 to 16. |
| **Account** | Built; 1 guard failure | `account_sheet/account_sheet.dart` (credit status line, "Saved 9:14 PM", Try again), `notifications_row.dart` ("Off" with a Turn on pill), `notifications/widgets/notifications_invite.dart` (the strip on You). With the compile error patched, `account_sheet_test` and `credits_test` pass. | Two bare `AnimatedSwitcher` in `notifications_invite.dart`. The two test files were being edited after my run. |
| **Onboarding** | Partly; 1 test failing | `college_ladder.dart` (up to 8, `kMaxColleges = MyColleges.maxColleges`), `college_match.dart` using the shared `duMatchRank`, `keyboard_watch.dart` (new), `step_layout.dart`, 20 new golden PNGs (course ladder, keyboard, eight, plan sealed). | The keyboard-up college search shows no rungs. The shared `AimLadder` from the Colleges brief was not built. `bank_size.dart`, `save_step.dart` and `copy.dart` were being edited after my run. |

## 4. The 39 ledger items

Key: **Built+pass** = code on the branch answers the item and its area's tests pass in the 17:26 run. **Partly** = built in part, or built with a failing test or a missing piece (named). **Not started** = nothing on `ui/owner-1016`. No item is device-verified.

Counts: **19 built and passing, 19 partly, 1 not started** (L39, which exists only on separate branches).

| Id | Status | Evidence and gap |
|---|---|---|
| L01 Today card | Built+pass | `move_builder.dart` (`recordUnavailable` with attempts gives a move), `today_builder.dart` (`refreshFailed`), `move_builder_partial_test.dart` passes; the dio plainBody root cause is fixed in `3887e786`. No `retry_status_test`. Not verified on a device. |
| L02 Today spacing and art | Partly | Hero edits of brief section 5 not made: `hero_stage.dart` and `number_block.dart` unchanged since `fd0da7d3`; `hero_spacing_test.dart` missing. Earlier spacing system (MmRhythm) stays. |
| L03 Section after load | Partly | `today_skeleton.dart` (+87 lines in WIP) and `week_ledger_skeleton.dart`; no test or golden for "nothing arrives late". |
| L04 Back exits app | Built+pass | `app_shell.dart` `_onNavigation` and `_backLeavesApp` (predictive-back fix); `router_widget_test.dart` passes. |
| L05 Road adjustable | Built+pass | `road_rail.dart` (horizontal drag on the flag, `onFlagEnd`), `road_tuners.dart` (`PaceStrip`, `MockRuler`), jump chips; `road_rail_gesture_test.dart` (156 lines) passes. Rail goldens not generated. |
| L06 Study-day ring | Partly | `goal_editor.dart` now uses the default `showWords: true` and `PaceStrip` edits days on the road; but `hub_sections_test` "planned weekdays ... 28 dp marks" fails and weekdays are still phone-only. |
| L07 Road lead-in | Built+pass | The "Your road to May" pill is unchanged and its tests pass. |
| L08 Practice order | Partly | Order built (subject, Up next, ways, exam band). `tab_dock_clearance_test` fails on 360x780 (first mode ends at 704, bar limit 656); `practice_order_test` fails on a second KeyButton; `tab_order_*` goldens missing. |
| L09 NTA tile overflow | Built+pass | `choice_glyphs.dart` panel sized from its grid; unchanged by this round; tests pass. |
| L10 Start moments | Built+pass | `composer_ticket.dart` clock turn; unchanged; passes. |
| L11 Quick practice | Built+pass | `pick_and_start_test.dart` passes; unchanged. |
| L12 Review record and empty state | Built+pass | `review_screen.dart` shows the empty state only for a known-empty read, `review_load_failure.dart` names the cause; review tests pass. |
| L13 Repair is more than the key | Partly | Retry-before-key built: `retry_first.dart` in `mistake_view.dart`, `retry_pick` in `repair_api.dart`, `repair_try_step_test`, goldens `repair_try_*` and `repair_verdict_*`. Missing: `try_first.dart` shared controller, the fresh check on 2 new questions (A.9), repair record across devices (separate branch, section 5). |
| L14 Review again | Partly | The page, data, entry row, tests and goldens are built, but **`/review/again` is not registered in `core/router`** (no match in `routes.dart` or `router.dart`), so the row opens the error page. No end-state golden. |
| L15 SWOT after each mock | Partly | `full_result_screen.dart` moved "After this mock" under the marks, `next_from_mock.dart` on Review History; `full_result_test` order test fails (Lab v4 order). The recap card's top-2 SWOT items are not in the diff. |
| L16 Profile sheet | Built+pass | `account_sheet.dart` with the credit status line; passes once the test support compiles. |
| L17 You as a study hub | Partly | Order built (study first, plan and credits last); 5 You tests fail against it (`hub_chips` 2, `hub_sections` 1, `hub` 2). |
| L18 Badges, milestones, bests | Built+pass | `derived_badges.dart`, `badge_record.dart`, `fastest_answer.dart`, `bests_screen.dart`, `badge_study_test.dart` passes, 14 rhythm and 8 You goldens. Badge count (14 to 16) not checked; two new server ids show only when the server sends them. |
| L19 Notifications invite | Partly | `NotificationsInvite` strip on You and the sheet's Off row with Turn on exist; `motion_guard` fails on 2 bare `AnimatedSwitcher` in `notifications_invite.dart`. |
| L20 Light/dark switch | Built+pass | In the account sheet and the Appearance card; passes. |
| L21 Edit subjects | Built+pass | `you/subjects/subjects_screen.dart`; passes. |
| L22 Tools not hidden | Built+pass | Colleges is tab 4 of 6 (`bar_tabs.dart`), `/tools` redirects, Practice More pushes `/tools/compass`, Compass in 2 taps from Colleges; `collegesScreen` tests pass except the unfinished one. |
| L23 Compass hierarchy | Partly | Rework plus `stream_fold.dart` built; `tools_design_test` fails (category rail 40 dp, needs 48). |
| L24 Search and keyboard | Built+pass | `college_search.dart` normalises "bcom", "b.com", "b com", "bcom hons"; `my_colleges_sheet.dart` pads by `viewInsets` and keeps 3 results above the keys; `college_search_test` and the keyboard test pass (patched run). |
| L25 Choose and Start | Built+pass | `my_colleges_actions.dart`, Today's colleges card; `colleges_card_test` passes. |
| L26 Score the student lacks | Partly | `estimate_sheet.dart` and `estimate.dart` built, `estimate_verdict_test` passes, "CSAS dashboard" removed; `banned_copy_test` fails ("your CUET score" in `estimate.dart`). |
| L27 Combo planner | Partly | Progress header and step or result modes (`combo_progress.dart`, `combo_screen.dart` +141 lines); `compass_flow_test` Combo case fails; no new Combo test; the "why not drop English" reason copy was not found. |
| L28 Onboarding polish | Partly | Mostly earlier work; the new college ladder fails its keyboard test; builders were still editing at 17:49. |
| L29 Sign-in | Built+pass | Unchanged; the auth tests pass. |
| L30 Add colleges in onboarding | Partly | Ladder up to 8, shared search, `keyboard_watch.dart`; keyboard test fails; the shared `AimLadder` was not built. |
| L31 Bar alignment | Partly | Geometry and alignment tests pass; the compact Start word test fails; `bar_six_*` goldens not generated; no emulator ruler. |
| L32 Bar 5 to 6 things | Built+pass | Six slots, Colleges tab, semantics order test passes. |
| L33 Bar blur | Built+pass | Earlier work, `glass_quality_test` passes. |
| L34 Motion | Partly | 16 new bare `AnimatedSwitcher` (13) or `Curves.ease*` (3) uses fail `motion_guard` across five areas. |
| L35 Mobi everywhere | Partly | 4 Revise Mobi tests fail (database in a widget test). The "Mobi look" rework exists only in `refs/wip/wt-w2l-1445` (7 files in `lib/core/mascot`); the live `wt-w2l` no longer has those edits. |
| L36 Spacing and parity | Partly | No new spacing test (`hero_spacing_test` missing); new screens not checked at 1.3x; nothing device-verified. |
| L37 Subject art | Partly | Briefcase committed (`ab89f591`), but `object_art_test` fails: the file is 685x582 and `object_art.dart:95` declares 685x769. |
| L38 Ask Mobi with credits | Built+pass | Unchanged apart from "AI credits" wording in `result/copy.dart`; passes. |
| L39 Other website features | Not started here | None of the missing list is on this branch. Parts exist elsewhere (section 5). Weekdays are still phone-only. |

## 5. App work outside ui/owner-1016

All of it is **uncommitted** in its own worktree, branched from `91a0268e` (contains the owner branch up to the You commit). Each is also snapshotted in `refs/wip/<wt>-1445`, but the snapshots are older than the current files (14:45), so merge from the worktree, not the ref.

| Worktree, branch | Content | State | Merge advice |
|---|---|---|---|
| `wt-w3-exam`, `ui/exam-preview-1016` | `lib/features/exam_preview/` (6 files), unit tests, golden test | `flutter analyze` on its files: **no issues**. Died at the limit; tests and goldens not run by me. | Merge after the owner branch settles. Needs a route and a link from Practice (`/exam/nta` per IA 11). |
| `wt-w4-hub`, `ui/subject-hub-1016` | `lib/features/subject_hub/` (7 files), tests, golden | Analyze: **1 error** (`practiseChapter` getter missing on `SubjectHubCopy`, `subject_hub_widgets.dart:145`), 2 warnings. Mid-edit. | Finish the copy getter, then merge. |
| `wt-w4-lesson`, `ui/lesson-ai-1016` | `learn/lesson_help/` (controller, copy, sheet), edit to `run_step.dart`, tests | Not analyzed (flutter slots were full). | Analyze and test first. |
| `wt-w3-record`, `ui/repair-record-1016` | `core/models/repair_record.dart`, `repair_record_repository.dart`, a 425-line test | Data layer only, no screen. Not analyzed. Needs the web repair-record endpoint. | Merge with the Review area once wired. |
| `wt-w3-fakes`, `ui/fakes-1016` | Test fakes that mirror real content types (`api_plain_body_test`, `fakes.dart`) | Test-only. | Merge, low risk. |
| `wt-w3-font`, `ui/font-audit-1016` | `test/golden/font_audit/` | Test-only, never rendered ("queued for a Flutter slot"). | Optional. |
| `wt-w2l`, `ui/mobi-look-1016` | Only tests and a probe file are live now | The Mobi look edits (`mobi_details`, `mobi_parts`, `mobi_painter`, palette, sim: 260 lines) exist only in `refs/wip/wt-w2l-1445` (fc9f3352). `zz_probe_test.dart` is a throwaway file. | Decide whether to restore from the ref. |
| `ui/phase2` (`20ed7a4d`) | `test/widget_test.dart`: the welcome smoke test uses an in-memory rhythm store | One test commit not in the owner branch. | **Cherry-pick into ui/owner-1016.** |
| `feat/app-and-web` (`fd3fca29`) | The plainBody fix | The same fix is already in the owner branch as `3887e786`. | Nothing to merge. |
| `ui/art-1016` (`15aeadde`, `61dd6d4e`) | Business Studies briefcase | The same image is already in the owner branch as `ab89f591`. | Nothing to merge. |
| `app/play-prep-1016` (`59681adb`) | Doc-only change to the Play release guide | Not app code. | Optional. |

## 6. What to do next (in this order)

1. **Let the resumed builders finish, then re-run** analyze and `test/unit`. The failures that look like leftovers (test support import, the unfinished colleges test, stale test expectations) are already being edited.
2. **Shell:** register `/review/again` in `router.dart` and `routes.dart` (this alone makes L14 reachable); decide the compact Start word rule and update or fix `core_widgets_pkg07_test`; replace `Curves.easeOutBack`; generate the `bar_six_*` goldens.
3. **Practice:** fix the 780 dp clearance and the extra KeyButton; remove the `DBG` prints.
4. **Colleges:** finish `colleges_screen_test`; fix "your CUET score"; make the programme category rail 48 dp; repair or update the Combo flow test; build or drop `AimLadder`.
5. **Result and Review:** settle the SWOT order (L15) against the Lab v4 test; override the review-again database in the Revise harness.
6. **Art:** re-measure `SubjectRender.business` for the 685x582 briefcase (size, foot, ground).
7. **Motion:** replace the 16 bare `AnimatedSwitcher` and `Curves.ease*` uses with the `core/motion` helpers.
8. **You and Onboarding:** update `hub_test`, `hub_chips_test`, `hub_sections_test` to the new order (or fix the real defects); fix the keyboard-up ladder.
9. Cherry-pick `20ed7a4d`. Then commit the tree (the 111 changed files and the new goldens are not on any branch yet; only `refs/wip` holds a 14:41 copy).
10. Only then run the golden suites, regenerate and open the new PNGs, and do the emulator walk of L01 to L39 against this file.
