# App owner feedback ledger, 16 Oct 2026 (about 11:30 IST)

One list of everything the owner has said about the Flutter app, with where it lives in the code, whether the code on `ui/phase2` answers it, and the check a tester runs on the emulator. Nothing here has been verified on a device. "Built" means code exists; it does not mean it works.

## How to read this

- **Owner words** are his voice-typed messages, shortened. Where voice typing garbled a word, the line says what it most likely meant ("Use section" is "You"; "Interview mode" is most likely NTA mode; "Review Again" is unclear, see L14). Newest words win where items conflict.
- **Dates** are IST. His messages in the session logs are stamped in UTC; these were converted (+5:30). A date is listed for every message where he raised the item.
- **Repeated** means he raised the same item on two or more different days.
- **Versions.** No owner message is tied to "v5" or "v6" by name. The dated app feedback on record is: 13 Oct 11:10 (Vivo, demo build), 14 Oct about 18:30, 15 Oct about 20:20 (APK v8), 16 Oct about 10:32 (APK v10, sent about 08:30). APK v5 went out 15 Oct afternoon. His 16 Oct sentence "the same issues as V5 or V6" is therefore read as "the items from 13 to 15 Oct".
- **Code evidence** is read from `wt-phase2/flutter_app` on `ui/phase2` at dd5a1500 (16 Oct 10:35) plus the uncommitted edits another agent had in the tree (onboarding, review/revise, saved screen, learn feedback Mobi). APK v10 is `feat/app-and-web` 9ccb7d0c; dd5a1500 and 35d9fa49 are newer than v10 and in no APK.
- **Status words:** "Built, plausibly working" (code answers the ask and nothing contradicts it); "Built, likely broken" (code exists but the code or the owner's report points at a defect); "Not built" (the ask is not met by anything on the branch; pieces that exist are named).
- **Sources read.** The owner's messages in the session logs (`604ced81`, `cc0bf1af`), `tmp/resume-2110/OWNER-MESSAGES-604ced81.md`, `tmp/resume-1015/OWNER-WORDS-1014.md`, `tmp/landing-1015-night/OWNER-NOTES.md`, `docs/brain/design-2026-10-13/OWNER-FEEDBACK-1110.md` and `-1014-1830.md`, `OWNER-VISION-2026-10-15-PM.md`, `APP-UX-AUDIT-2026-10-15.md`, `CTO-LOOP.md`, `VISION-INVENTORY-2026-10-16.md`, `HANDOFF-2026-10-15-EVENING.md`, `HANDOFF-2026-10-16-NIGHT.md`, `ui-phase2/DOCK.md`, `WEB-PARITY.md`, the owner memory files, and the app code. The Continuum search tools returned an error in this session (their `brain.py` call failed), so the AI OS files and transcripts were read directly.

## Test setup for every acceptance check

- Emulator `mockmob_budget`, 2 GB RAM (check free RAM first). Run `bash tool/flutter_locked.sh build apk --debug --dart-define-from-file=dart_defines/phone.json` from `wt-phase2/flutter_app` (staging site on port 3101, `adb reverse tcp:3101 tcp:3101`), or install the newest release APK.
- Two test accounts, never the owner's: **A** with at least 2 finished mocks, open mistakes and a name; **B** fresh, no papers. The staging sign-in code comes from `node --use-system-ca scripts/dev/staging-otp.mjs <email>`.
- Run each check in Night and Day, at 360x800 and 412x915, and once at 1.3x font size. Take a screenshot at the end of each check.

## Index

| Id | Item | Group | Raised on | Repeated | Status |
|---|---|---|---|---|---|
| L01 | Today card: "Could not reach MockMob just now" | Today | 2 days | yes | Built, likely broken |
| L02 | Today spacing and art alignment | Today | 2 days | yes | Built, plausibly working |
| L03 | Today gains a section after load | Today | 1 day | no | Built, plausibly working |
| L04 | Back button exits the app | Today | 1 day | no | Built, plausibly working |
| L05 | Road to May: clunky, timeline should be adjustable by scrolling | Road to May | 3 days | yes | Not built |
| L06 | Study days sheet: ring still shows 3 after choosing 4 | Road to May | 1 day | no | Built, likely broken |
| L07 | Road to May sits too low, needs a lead-in | Road to May | 1 day | no | Built, plausibly working |
| L08 | Practice tab order is wrong | Practice | 1 day | no | Not built |
| L09 | NTA tile overflows its panel (Practice and Start sheet) | Practice | 1 day | no | Built, plausibly working |
| L10 | Start moments: full mock clock turn, NTA moment | Practice | 1 day | no | Built, plausibly working |
| L11 | Quick practice honours subject and length; finishing has a moment | Practice | 1 day | no | Built, plausibly working |
| L12 | Review page: record not reached, odd empty state | Review | 2 days | yes | Built, likely broken |
| L13 | Mistake repair must be more than the key | Review | 3 days | yes | Not built |
| L14 | "Review again" does not work | Review | 1 day | no | Built, likely broken |
| L15 | SWOT after each mock | Review | 1 day | no | Built, plausibly working |
| L16 | Profile sheet from the avatar | You and profile | 2 days | yes | Built, plausibly working |
| L17 | You tab as a study hub, plan items lower | You and profile | 3 days | yes | Not built |
| L18 | More badges, milestones, personal bests | You and profile | 2 days | yes | Not built |
| L19 | Keep inviting people to notifications until on | You and profile | 2 days | yes | Not built |
| L20 | Light/dark switch and account settings easy to find | You and profile | 1 day | no | Built, plausibly working |
| L21 | Edit subjects | You and profile | 1 day | no | Built, plausibly working |
| L22 | CUET tools and Admission Compass not hidden in a corner | Tools and Compass | 2 days | yes | Not built |
| L23 | Admission Compass rethought, hierarchy | Tools and Compass | 2 days | yes | Built, plausibly working |
| L24 | My colleges search: "BCOM" finds nothing, keyboard hides results | Tools and Compass | 1 day | no | Built, likely broken |
| L25 | "Your colleges": Choose and Start do nothing | Tools and Compass | 1 day | no | Built, plausibly working |
| L26 | Compass asks for a score the student does not have | Tools and Compass | 1 day | no | Built, likely broken |
| L27 | Combo planner confusing | Tools and Compass | 1 day | no | Not built |
| L28 | Onboarding: polished, no sample, no pasted pictures, no filler lines | Onboarding | 3 days | yes | Built, plausibly working |
| L29 | Sign-in works and stays signed in | Onboarding | 3 days | yes | Built, plausibly working |
| L30 | Add colleges in onboarding | Onboarding | 1 day | no | Built, plausibly working |
| L31 | Bottom bar aligned with the Start bubble; labels aligned; rethink | Navigation | 6 days | yes | Built, likely broken |
| L32 | Bar holds 5 to 6 useful things | Navigation | 1 day | no | Not built |
| L33 | Bar blur stronger | Navigation | 1 day | no | Built, plausibly working |
| L34 | Motion graphics, judged in use | Mobi and motion | 6 days | yes | Built, plausibly working |
| L35 | Mobi in every scene, tastefully, better looking | Mobi and motion | 4 days | yes | Built, plausibly working |
| L36 | One spacing system, balance, light/dark parity | Mobi and motion | 2 days | yes | Built, plausibly working |
| L37 | Subject art that says its subject | Mobi and motion | 1 day | no | Built, plausibly working |
| L38 | Ask Mobi with credits | Website parity | 2 days | yes | Built, plausibly working |
| L39 | Other website features missing in the app | Website parity | 3 days | yes | Not built |

Counts: 39 items; 19 repeated; 10 not built; 7 built but likely broken; 22 built and plausibly working.

## Today

### L01 Today card: "Could not reach MockMob just now" (repeated)
- **Owner words.** 15 Oct 20:20: "Couldn't load is the thing coming on top of the page. Even when I click Try again, nothing is happening." 16 Oct 10:32: "The homepage is still not working, at least for my account. I'll try another account." Later: "I couldn't reach my record" on the second account, while "Your record" itself loads.
- **Raised.** 15 Oct 20:20, 16 Oct 10:32.
- **Area and files.** Today. `features/today/logic/move_builder.dart` (the `historyUnavailable` card, line 181), `features/today/copy.dart` (`unavailableFor`, line 142), `features/today/screens/today_screen.dart` (`_retry`, `_sayIfStillFailing`), `core/repositories/attempts_repository.dart`, `core/repositories/plan_repository.dart`, `core/auth/load_problem.dart`.
- **Status: Built, likely broken.** The card says this when `plan.recordUnavailable` is true or the attempts read failed with nothing cached (`move_builder.dart:105`). v10 used one general line for every cause. Try again now keeps its spinner for 900 ms and then says why it is still failing in a snackbar (built before v8 testing ended). Commit dd5a1500 (16 Oct 10:35, after v10, in no APK) is the first response to this exact report: a body that is not a list is now "unreadable" instead of "no record", one bad row no longer drops the others, and the card names the cause. It was written from code and tests, not from a device or a production log, so the real cause on his two accounts is not confirmed. "Your record" loads from a different route, so it proves little. Until a build with dd5a1500 shows a named cause or a working card on an account that fails today, treat this as open.
- **Acceptance check.** Install the newest build. Sign in as account A, cold start, open Today. The first card must show a subject name, a number of questions and a Start key within 5 seconds, not "Could not reach MockMob" or "Your earlier results are still there". Sign in as B: the card must say it is a day-one move (starting point, 10 questions), not an error. Then turn on airplane mode on A, force-stop and reopen: the card must say "You are offline" and cached results still show in Review. Tap Try again: the key shows a spinner for about 1 second, then a snackbar "Still not loading." names the cause. Turn the network on and tap Try again: the card becomes a real move. If any account shows an error card with the network on, capture `adb logcat` and the response of the attempts and plan reads; that account is the reproduction this item still needs.

### L02 Today spacing and art alignment (repeated)
- **Owner words.** 13 Oct 11:10: "Some spacing, like on the first page only: 2 days, move accountancy, 3 mistakes. There is a book there, but the spacing overall can be improved." 14 Oct 18:30: "the calculator papers should be lower. There is too much space ... Then it's stuck at the top."
- **Raised.** 13 Oct 11:10, 14 Oct about 18:30.
- **Area and files.** Today hero. `features/today/widgets/move_hero.dart`, `hero_stage.dart`, `today_body.dart`; specs `docs/brain/ui-phase2/SPACING.md` and `SPACING-AUDIT.md`.
- **Status: Built, plausibly working.** A spacing system (`MmRhythm`) and a hero redesign landed 14 to 16 Oct (commits 5f5a2d40, 7f685790, critic packet A f5e8da16). No owner message after 14 Oct 18:30 mentions this spacing again, and no device run has confirmed it. The goldens were opened by the builders, not by him.
- **Acceptance check.** On account A open Today in Night, then Day, at both sizes. The subject object must sit beside or above the "N to repair" text with no empty band taller than one line of text, must not touch the top edge, and must not be clipped. Repeat at 1.3x font size: no overlap, nothing cut. Repeat with a Mobi hero (account B): the same.

### L03 Today gains a section after load
- **Owner words.** 15 Oct 20:20: "when I come to Home again, it has added another section like last week ... 1 of 4."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `features/today/screens/today_screen.dart` (the `AnimatedSize` around the weekly ending), `features/today/widgets/week_ledger_skeleton.dart`, `today_inputs.dart` (`weekLoading`).
- **Status: Built, plausibly working.** The week strip reserves a skeleton while the rhythm read loads, and the weekly ending card opens into place with an animated size change. Not seen on a device.
- **Acceptance check.** On account A with slow network (emulator network speed "gprs"), cold start Today. The week area must show a placeholder from the first frame; when data arrives the page must not jump, and no new block may appear under the hero after the first second. Start a mock, finish it, return to Today: no section may appear without an animated opening.

### L04 Back button exits the app
- **Owner words.** 15 Oct 20:20: "When I click this back button, it's just exiting the app. That should not be the case."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `core/router/app_shell.dart` (`pressBackAgain`, line 96; the pop handler near line 437).
- **Status: Built, plausibly working.** A two-press guard exists; not run on a device.
- **Acceptance check.** On Today press Back once: a snackbar "Press back again to close" appears and the app stays. Press Back again within 2 seconds: the app closes. Open Practice, press Back: the app goes to Today, not out. With a sheet open, Back closes the sheet first.

## Road to May

### L05 Road to May: clunky, timeline should be adjustable by scrolling (repeated)
- **Owner words.** 13 Oct 11:10: "The road to May ... can also be improved a bit." 15 Oct 20:20: "the UI can be improved by showing the board, making it more interactive, editable or changeable." 16 Oct 10:32: "some parts of it are still quite clunky ... make it intuitive in the way that this timeline is somehow intuitive ... maybe some adjustments can be put directly into the scrolling or something in the timeline."
- **Raised.** 13 Oct 11:10, 15 Oct 20:20, 16 Oct 10:32.
- **Area and files.** Today. `features/today/widgets/road_timeline.dart` (1,125 lines), `road_board.dart`, `road_section.dart`, `logic/road_board.dart`, `data/road_plan.dart`.
- **Status: Not built.** What the 15 Oct ask produced is built: a board of four tiles (exam date, mocks against a target, study days left, this week), each opening a sheet that edits the value, kept on the phone except the study-day goal (`road_board.dart`). The timeline itself is a read-only painter: the only gesture is a long-press scrub that shows a date readout (`road_timeline.dart:59-209`); nothing on it moves a date, a target or a study day. His 16 Oct ask (adjust by scrolling the timeline) has no code.
- **Acceptance check.** On account A scroll Today to the road. Drag or scroll along the timeline: a marker for the exam date (or for the weekly plan) must move with the finger, a live readout must show the new date and the weeks and study days left, and releasing must save it. The date tile and the study-days tile in the board must show the same new numbers. Force-stop and reopen: the value is kept. Scroll the page itself over the timeline: the page still scrolls (the timeline must not trap vertical scroll). Reduced motion: no animation, the same result.

### L06 Study days sheet: ring still shows 3 after choosing 4
- **Owner words.** 16 Oct 10:32: "when I change the study days, it's just showing 3 only to me. The thing that you have made to change ... is not up to the mark: the UI built around this." (Related earlier: 13 Oct 11:10 "Weekly, some things require a bit more thinking over"; 14 Oct 00:23 "Study days can be saved on the phone".)
- **Raised.** 16 Oct 10:32 (related asks 13 Oct, 14 Oct).
- **Area and files.** `features/rhythm/widgets/goal_editor.dart`, `week_dial.dart`, `features/today/widgets/road_board.dart` (`_StudyDaysSheet`, line 447), `rhythm/data/rhythm_providers.dart` (`saveStudyDays`).
- **Status: Built, likely broken.** `WeekDial` draws exactly `goal` segments but the number in the middle is `done`, this week's counted study days (`week_dial.dart` header). The editor passes `done` and sets `showWords: false`, so a student who has studied 3 days this week sees a ring with 4 segments and a big "3", with no words saying "of 4". That matches his report and is the most likely reading, but it is not proven: he did not say which ring. Other weak points seen in the code: the Today sheet closes and a second sheet opens on top of the same flow (`road_board.dart:471-474`), the save is three steps (server goal, server weekdays where an endpoint exists, then the phone) with a refresh after, and the weekdays still live on the phone only (`PhoneOnlyStudyDays`), so a second device never sees them.
- **Acceptance check.** On account A with 3 days studied this week: Today, road board, "Study days left", "Change study days". Pick Mon, Tue, Thu, Sat. The ring must show 4 segments and the words "of 4 study days" with the studied count visible as a count of the 4, not as the goal. Save. Today's road tile must say "At 4 study days a week" and the This week tile "3 of 4". Open You: Study days shows 4. Force-stop and reopen: still 4. Repeat in airplane mode: an error line appears and the old 3 stays everywhere.

### L07 Road to May sits too low, needs a lead-in
- **Owner words.** 15 Oct 20:20: "This Road to May is a bit too at the bottom, so something in the UI should be leading them below, maybe a down arrow."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `features/today/screens/today_body.dart` (the "Your road to May" pill with a down chevron, line 720).
- **Status: Built, plausibly working.** Not seen on a device.
- **Acceptance check.** Account A, Today: under the hero a pill "Your road to May" with a chevron must show while the road is below the first screen. Tap it: the page glides to the road. After the road scrolls into view, the pill is gone. At 1.3x font size it must not cover the hero text.

## Practice

### L08 Practice tab order is wrong
- **Owner words.** 16 Oct 10:32: "The issue is the placement of things, like first in the top English subject, then a few modes, then subject selection, and then ... it's not exactly ideal." (He listed Quick Practice, By Chapter, Smart Practice, Exam Condition, Full Mock, "Interview Mode".) On 15 Oct 20:20 he praised the subject selection animation and Smart Practice, so the pieces stay and the order changes.
- **Raised.** 16 Oct 10:32 only.
- **Area and files.** `features/practice/practice_screen.dart` (list order lines 219-431), `data/default_subject.dart` (why English is first for some accounts), `widgets/choice_deck.dart`, `subject_tiles.dart`, `mode_list.dart`.
- **Status: Not built.** The order in code matches his complaint: header, suggestion hero, a subject line (the default subject, English for his account), the quick pair (Quick practice, By chapter), then "Choose your own" with the subject tiles, then Smart practice, then the exam band (Full mock, NTA mode), then More, then Concepts. That order was set on purpose on 15 Oct 19:37 (775bb896) before his 16 Oct note and has not changed since. "Interview mode" does not exist in the app; it is most likely NTA mode.
- **Acceptance check.** Practice tab on account A. Reading top to bottom the order must be one the owner confirms; the proposal to test: choose the subject first (the subject strip at the top of the page), then the modes for that subject, shortest to longest (Quick practice, By chapter, Smart practice, Full mock, NTA mode), then More. Changing the subject must keep the modes in place and change only their notes. No mode may appear above the control that chooses its subject. The first screen at 360x800 must show the subject choice and the first mode.

### L09 NTA tile overflows its panel (Practice and Start sheet)
- **Owner words.** 15 Oct 20:20: "NTA mode is a bit broken. Some boxes and checkboxes are going out of the area." And again in the Start section.
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `features/practice/widgets/choice_glyphs.dart` (`ntaPanel`, `ntaCellRect`, line 420), `quick_start_deck.dart`.
- **Status: Built, plausibly working.** The panel is now sized from the grid it holds, so cells cannot leave it by construction. Not seen on a device.
- **Acceptance check.** Practice tab and the Start sheet, Night and Day, 360 and 412 wide, 1.3x font: the NTA tile's three rows of coloured cells sit fully inside the pale panel; the tile's title and note do not overlap the art; the Full mock tile's title and the NTA tile's title sit on the same line.

### L10 Start moments: full mock clock turn, NTA moment
- **Owner words.** 15 Oct 20:20: "when clicking on the Start button, the full mock can have some animation of its own, like the clock doing a 360, or NTA mode can have something."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `features/practice/widgets/composer_ticket.dart` (line 52, the clock turn), `practice_start_screen.dart`, `exam_sheet_start.dart`.
- **Status: Built, plausibly working.** Wave 3 added the clock turn and an NTA moment inside the hold the start already has. Not seen on a device.
- **Acceptance check.** Start a full mock: after the server confirms, the stopwatch art sweeps one full turn before the runner opens, without delaying the paper's clock. Start an NTA paper: a different, exam-style moment plays, then the instructions page. Reduced motion (Android "remove animations"): a still frame, no sweep. Nothing animates inside the timed paper.

### L11 Quick practice honours subject and length; finishing has a moment
- **Owner words.** 13 Oct 11:10: "Whenever I am trying to start a quick practice of 5 questions ... Even after we finish it, there's no such animation ... Even when I'm starting from business studies ... it's just redirecting me to the accounting page."
- **Raised.** 13 Oct 11:10 only (he has not repeated it since the next builds).
- **Area and files.** `practice/data/practice_starter.dart`, `launch_flow.dart`, `widgets/finish_stage.dart`, `model/finish_reaction.dart`; tests `test/unit/practice/pick_and_start_test.dart`.
- **Status: Built, plausibly working.** Tests cover subject and count being honoured; a finish ceremony exists. No owner message since 13 Oct reports it again.
- **Acceptance check.** On Practice choose Business Studies, Quick practice, 5 questions, Start. The runner header must name Business Studies and the question count must be 5. Finish: a finish moment with Mobi plays, then the result shows the 5 answers. Repeat with another subject and By chapter: the chapter and subject are the ones chosen.

## Review

### L12 Review page: record not reached, odd empty state (repeated)
- **Owner words.** 15 Oct 20:20: "Review is also showing me that we could include your mistakes." 16 Oct 10:32: "Especially the home page and review page: the issues with them. Even if I'm signing into another account, I couldn't reach my record."
- **Raised.** 15 Oct 20:20, 16 Oct 10:32.
- **Area and files.** `features/review/screens/review_screen.dart`, `review/copy.dart` (`emptyTitle` "Your mistakes gather here", line 147), `core/repositories/attempts_repository.dart`.
- **Status: Built, likely broken.** The phrase he heard is most likely the empty state, "Your mistakes gather here. Every wrong answer lands here". An account that has papers should never see it. The dd5a1500 commit says the attempts read treated a body that was not a list as an empty record, "a student with a record was told they had none", which would produce exactly this on Review and an error card on Today. This is the best current explanation, not a confirmed one. It stays "likely broken" until a build with that fix shows his own mistakes.
- **Acceptance check.** Account A (papers with mistakes): Review tab must show "To repair" with tonight's repair and the chapter list, and a History side with past results, never the empty state. Account B: the empty state with a "Start practice" key is correct. Airplane mode on A after a first load: cached mistakes still show with a note that they are saved on the phone.

### L13 Mistake repair must be more than showing the key (repeated)
- **Owner words.** 14 Oct 22:14: "we show the correct or wrong answers for free. We are charging for the mistake repair ... make that feature more useful." 15 Oct 08:49: "It's working, but it should be a bit more useful, like giving more insights." 16 Oct 02:19: "we just can't show mainly your correct answer ... We can't ask them to pay extra to just see the right answer."
- **Raised.** 14 Oct 22:14, 15 Oct 08:49, 16 Oct 02:19.
- **Area and files.** `features/review/screens/repair_screen.dart`, `repair_ending_screen.dart`, `widgets/repair_check_section.dart`, `data/repair_check_*.dart`; the server `src/app/api/recovery/repair`.
- **Status: Not built.** Built so far: Repair v3 (trap label, key quality chip), the SWOT after a mock, "Check it held" and "Ask Mobi about Qn" (a8252ca4, after v10 started). The CEO decision of 16 Oct 02:20 (retry before the key, a fresh checked question on the same rule, the rule back on Revise, the personal trap pattern, a follow-up into Ask Mobi) is only partly there: the fresh check on 2 new questions (spec A.9) and retry-before-key are missing on web and app (`VISION-INVENTORY-2026-10-16.md`), and Revise is built but not live.
- **Acceptance check.** Account A, Review, repair one mistake. The screen must ask the student to try again before the key shows, then explain the reason (not only the key), name the trap pattern, offer a fresh question on the same rule that is free and says "Checked", and offer "Ask Mobi about this". Before the call the screen states the cost ("Uses 1 AI credit. You have N."); after it the balance in the Account sheet is lower by exactly that amount; a failed repair charges nothing.

### L14 "Review again" does not work
- **Owner words.** 16 Oct 10:32: "and Review Again is not working for you." (Said while describing Practice.)
- **Raised.** 16 Oct 10:32 only.
- **Area and files.** Candidates, since no control is labelled "Review again": "Try it again" in Review (`review/widgets/review_rows.dart:153`, opens the answer sheet), "Try it again" on a result card (`practice/widgets/result_question_card.dart:257`), "Try the same mistakes again" (`review/screens/repair_ending_screen.dart:247`), the Revise page (`review/revise/revise_screen.dart`).
- **Status: Built, likely broken.** The label is ambiguous and the question to the owner is open (see "Open questions"). Every candidate reads the attempts or an attempt detail first, so while L01 and L12 are open they fail the same way. No separate defect was found by reading.
- **Acceptance check.** Account A: Review, a mistake row, "Try it again" must open the question with the options and no key showing; answer it: the app shows right or wrong and the key. Result screen: a skipped question's "Try it again" works. End of a repair: "Try the same mistakes again" opens the same questions. Each must work offline for a cached question or say so plainly.

### L15 SWOT after each mock
- **Owner words.** 15 Oct 08:49: "after each mock, add a SWOT analysis. According to that, we will recommend the next specific topic mocks."
- **Raised.** 15 Oct 08:49 only.
- **Area and files.** `features/result/**`, `features/review/data/ending_model.dart`; server SWOT in the repair route.
- **Status: Built, plausibly working.** In the app since APK v5 (Repair v3 and the SWOT); the app recap card does not yet show the top 2 SWOT items (`VISION-INVENTORY` D.5-2).
- **Acceptance check.** Finish a full mock on account A: the result shows strengths, weaknesses, opportunities and threats built from that mock, and each recommendation opens a practice start for that topic with the subject and chapter filled in.

## You and profile

### L16 Profile sheet from the avatar (repeated)
- **Owner words.** 15 Oct 20:20: "Maybe Profile can be opened by a button, like how it's usually in the apps, by the top bar." 16 Oct 10:32: "one you click on in the profile ... profile, name, email ... practice credits, AI credits quickly ... plan-related tasks".
- **Raised.** 15 Oct 20:20, 16 Oct 10:32.
- **Area and files.** `features/account_sheet/account_sheet.dart`, `core/widgets/account/account_avatar.dart`, `core/widgets/tab_root_header.dart`.
- **Status: Built, plausibly working.** The avatar sits on the tab-root header and opens a sheet with initials avatar, name, email, a Free or Pro tag, both credit balances (tiles that open the Credits page and its history), the Night/Day/Match-phone switch, rows for Name sign-in and plan, Notifications, Study days, Privacy, Help and Write to us, and Sign out. It was in v9 and v10, but his 16 Oct note describes this sheet as the right idea, so what remains open is the You tab (L17), not this sheet.
- **Acceptance check.** On each of the four tab roots tap the avatar. The sheet must show the same name and email as the account, the plan tag, "Practice credits N" and "AI credits N" (both numbers, each tile opens a Credits page with a history list), the theme switch (tapping Night or Day recolours the app at once), the six rows (each opens its screen and Back returns to the same tab), and Sign out (asks to confirm, returns to sign-in).

### L17 You tab as a study hub, plan items lower (repeated)
- **Owner words.** 15 Oct 20:20: "The You section shows not much. Would be a bit more." 16 Oct 10:32: "In the You section, there is stuff like study days, badges, and milestones ... personal bests ... improve the UI and functionality of all these kinds of things related to study ... These can be put lower down. Plan-related tasks are already visible in the other section."
- **Raised.** 13 Oct 11:10 (milestones and weekly "need a bit more thinking"), 15 Oct 20:20, 16 Oct 10:32.
- **Area and files.** `features/you/you_hub_screen.dart` (section order lines 276-346), `you/hub/hub_cards.dart`, `hub_sections.dart`, `features/rhythm/**`.
- **Status: Not built.** The hub is built, with 11 sections, but in the wrong order for his ask: Plan and credits first, Appearance second, then Study days, Notifications, My subjects and colleges, the milestones shelf, Progress, Across your mocks, Account and privacy, CUET tools, Help. Plan, credits and the theme switch also sit in the avatar sheet, so they appear twice and above the study content he wants first.
- **Acceptance check.** You tab on account A. The first screen (360x800) must show study content: the week ring with study days, then milestones and badges, then personal bests; Plan and credits, Appearance and Account must be below those and must not duplicate the avatar sheet's credit tiles. Every section opens its detail screen and returns to the same scroll position. With no data, every section shows a plain empty state, not an error.

### L18 More badges, milestones, personal bests (repeated)
- **Owner words.** 13 Oct 11:10: "milestones ... That thing should be improved." 16 Oct 10:32: "You can add more badges to it and make it more intuitive ... personal bests."
- **Raised.** 13 Oct 11:10, 16 Oct 10:32.
- **Area and files.** `features/rhythm/logic/tokens.dart` (3 tokens), `milestone_tracks.dart`, `screens/milestones_screen.dart`, `bests_screen.dart`.
- **Status: Not built.** There are exactly three badge tokens (first mock, first repair, first week met), plus a milestones page and a personal bests page. No new badges were added after his ask.
- **Acceptance check.** You tab, the milestones shelf: a student with account A sees at least 8 distinct badges (for example first mock, first repair, 7 study days, first full mock, 3 chapters repaired), each with a clear locked state that says what earns it and an earned state with its date. Opening a badge explains it. Personal bests show best mock score, longest run of study days and fastest pace, each with its date. Earning a badge in the runner shows a celebration once.

### L19 Keep inviting people to notifications until on (repeated)
- **Owner words.** 14 Oct 00:23: "Notification prompt can be sent again and again with some unique way of asking." 16 Oct 10:32: "people pages of notifications, unless and until they have turned it on."
- **Raised.** 14 Oct 00:23, 16 Oct 10:32.
- **Area and files.** `features/notifications/logic/pre_prompt_policy.dart`, `screens/reminders_prompt_sheet.dart`, `you/hub/hub_cards.dart` (`NotificationsPanel`).
- **Status: Not built (partly).** A reminders sheet comes back after "Not now": 2 days after the first ask, then 4, 7, then every 10, never more than once a day, and only right after a finished result. It never shows when the student is just opening the app, and nothing on the You tab, Today or the avatar sheet keeps inviting them while reminders are off; the You row just says "Off".
- **Acceptance check.** Account A with notifications off: the avatar sheet row "Notifications" and the You tab show an invitation (plain words, a key that turns them on) for as long as they are off. Tapping the key asks Android's permission; allow it: the invitation disappears and the row says "On" with the next reminder time. Deny it twice: the key then opens Android settings. After finishing a practice, the reminders sheet appears at most once a day and never during a paper.

### L20 Light/dark switch and account settings easy to find
- **Owner words.** 15 Oct 20:20: "Where's the option to do light or dark mode? ... There should be a proper account setting option easily accessible."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `features/you/appearance/theme_switch.dart`, `account_sheet.dart`.
- **Status: Built, plausibly working.** One switch in the avatar sheet and an Appearance card on You.
- **Acceptance check.** From any tab: avatar, Night/Day/Match phone is visible without scrolling and changes the whole app immediately, including the bar and sheets. Kill and reopen: the choice is kept.

### L21 Edit subjects
- **Owner words.** 13 Oct 11:10: "there is no option to edit subject, I think."
- **Raised.** 13 Oct 11:10 only.
- **Area and files.** `features/you/subjects/subjects_screen.dart`, `practice/widgets/other_subjects_sheet.dart` ("Edit subjects" on Practice).
- **Status: Built, plausibly working.** Reachable from You (My subjects) and from Practice.
- **Acceptance check.** Practice, "Edit subjects": remove one, add one (limit 5), save. Practice tiles, Today and You show the new set; the default subject on Practice is one of them.

## Tools and Compass

### L22 CUET tools and Admission Compass not hidden in a corner (repeated)
- **Owner words.** 15 Oct 20:20: "it has to be integrated, not hidden below something ... CUET tools' entire section and Combo Planner." 16 Oct 10:32: "The CUET tools are not tucked inside a corner, hidden ... Mainly, it's the Admission Compass only, and it's a quite important feature."
- **Raised.** 15 Oct 20:20, 16 Oct 10:32.
- **Area and files.** `features/tools/hub/tools_shelf.dart` (`ToolsShelf`, `ToolsQuietLink`), `you/you_hub_screen.dart` (tools section is index 10 of 11), `practice/widgets/more_rows.dart`, `core/widgets/bar/bar_tabs.dart`.
- **Status: Not built.** The tools are reachable from three quiet places: the end of the You page, a quiet link under Today's road, and the Practice "More" list. There is no tab and no card in the main flow. The audit's recommendation (a Colleges tab, `APP-UX-AUDIT` section 4, and a Compass summary card inside Today's road) is not built (`VISION-INVENTORY` P1-9: missing).
- **Acceptance check.** From a cold start on account A, Admission Compass must be reachable in one tap from the bottom bar or from a visible card on Today (for example "35 of 73 DU programmes open to your subjects"), and from Practice. Opening it from either lands on the same screen, and Back returns to where the student was. A student who has never opened it sees it named on Today.

### L23 Admission Compass rethought, hierarchy (repeated)
- **Owner words.** 15 Oct 20:20: "This lacks visual hierarchy. In B Com when you are showing 55 colleges, maybe that section can be cleaned where there are very few colleges ... something nudging people to open it." 16 Oct 10:32: "this entire thing honestly needs to be thought through: how to build the Admission Compass better."
- **Raised.** 15 Oct 20:20, 16 Oct 10:32.
- **Area and files.** `features/tools/compass/compass_screen.dart`, `compass_hero.dart`, `programme_rows.dart`, `cutoff_bar.dart`, `programme_screen.dart`.
- **Status: Built, plausibly working.** Commit 610bab23 (16 Oct 01:45) reworked it: one primary move under the hero, best options as a cutoff bar with the score pinned, stream and unlock chips, small programmes folded under "Other programmes". Not in front of the owner yet (v10 may have it; he did not comment on it in his 16 Oct list beyond asking for a rethink).
- **Acceptance check.** Open Compass on account A. Within the first screen: the student's category and what their subjects open, the best-fit programmes first (each with a cutoff range and the number of colleges), small programmes folded; tapping a programme opens its colleges with cutoffs; "Add to my colleges" on a college row adds it (check My colleges). No row looks identical to every other row.

### L24 My colleges search: "BCOM" finds nothing, keyboard hides the results
- **Owner words.** 16 Oct 10:32: "when I am searching BCOM, there is nothing, and it's going to the bottom, and everything is getting hidden ... If I write b., it's then showing, but still it is going down, and my keyboard isn't automatically adapting to it."
- **Raised.** 16 Oct 10:32 only.
- **Area and files.** `features/tools/my_colleges/my_colleges_sheet.dart` (`_programmeList`, line 165: `g.name.toLowerCase().contains(q)`; `_collegeList`, line 201), `core/widgets/mm_sheet.dart`, `features/tools/widgets/tools_page.dart` (`ToolsSearchField`).
- **Status: Built, likely broken.** Both defects are visible in the code. Search is a plain substring match on the programme name, so "bcom" cannot match "B.Com (Hons)" while "b." can (his exact symptom); no punctuation, space or abbreviation handling. The chooser is a modal sheet whose body is a scroll view with no keyboard avoidance: `mm_sheet.dart` has no `viewInsets` handling and only five files in the app use `viewInsets` (none is the sheet or the colleges chooser), so the results sit under the keyboard.
- **Acceptance check.** Today, "Your colleges", Choose (or You, My subjects and colleges). In the chooser type "bcom": B.Com (Hons) and B.Com programmes must be listed. Type "b.com", "B Com", "bcom hons", "eco": each finds the matching programmes. With the keyboard open the field and at least three results must stay visible above it; scrolling the list works with the keyboard open; closing the keyboard leaves the list in place. The college search inside a programme behaves the same. Add a college: the row shows a tick and the list count rises; the limit is 8.

### L25 "Your colleges": Choose and Start do nothing
- **Owner words.** 15 Oct 20:20: "When I'm clicking to choose, it's showing 'Could not load a suggestion.' Then I'm clicking Start, nothing is happening."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `features/today/screens/today_screen.dart` (`onChooseColleges`, line 191), `features/tools/data/my_colleges_actions.dart`, `my_colleges_repository.dart`; server list in `web/colleges-1016`.
- **Status: Built, plausibly working.** Choose now opens the My colleges sheet over Today (straight to the chooser when the list is empty), replacing the push to the You tab root. One server-backed list (up to 8) is shared by Today, Compass and You; older lists are moved into it. The server routes shipped in the 16 Oct batch (production migrations applied 16 Oct 04:20). The "Could not load a suggestion" line is gone, but L24 still breaks the search inside this sheet.
- **Acceptance check.** Account B: Today's "Your colleges" with Choose opens a sheet, never the You tab. Add 3 colleges: Today's ladder shows them in order, with their cutoffs. Reopen Choose: the three are ticked. Offline: the sheet says it could not save and keeps the list. Add one in Compass: it shows on Today.

### L26 Compass asks for a score the student does not have
- **Owner words.** 15 Oct 20:20: "When I am opening this Admission Compass, why is it asking for my score?"
- **Raised.** 15 Oct 20:20 only (related: 14 Oct 00:23, "I didn't like the CSAS admission portal, so I don't know what you are trying to do with it").
- **Area and files.** `features/tools/copy.dart` (line 66 `scoreHelp`: "Use the score on your CSAS dashboard"; lines 29 and 163 name "CSAS"), `compass/category_score.dart`, `score_sources.dart`.
- **Status: Built, likely broken.** The 16 Oct rework puts "add your expected score" as the first move; the "CSAS dashboard" wording and the round and CSAS jargon from the audit (`APP-UX-AUDIT` finding 7 and 19) are still in `copy.dart`. A Class 12 student in October has no such score, so the first question is still one they cannot answer, though the screen may now offer the practice estimate.
- **Acceptance check.** Open Compass as account B (no papers): the screen must be useful with no score, and must never say "CSAS dashboard". With account A (papers): the score field offers "Use my practice estimate" with the number. Category is a chip row near the top; the score is optional and below the programmes.

### L27 Combo planner confusing
- **Owner words.** 15 Oct 20:20: "the CUET tools' entire section and Combo Planner. All this is a bit confusing. Again, remember, confusing doesn't mean get off."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `features/tools/combo/**` (last touched 15 Oct 21:03), audit finding 23.
- **Status: Not built.** The three tasks on one long page (where do you want to go, which subjects could you take, how many papers) with a long empty tail, and "Do not drop: English, Mathematics" without a reason, have no commit after the audit.
- **Acceptance check.** Open Combo planner: three steps with a small progress header; the result (combinations that open the chosen programme) shows first once set; any "do not drop" line says why ("Mathematics opens B.Com (Hons) Option 1 at 41 more programmes"). No empty tail at 360x800.

## Onboarding

### L28 Onboarding: polished, no sample, no pasted pictures, no filler lines (repeated)
- **Owner words.** 13 Oct 02:30: "onboarding flow is really weak ... the 5-question approach ... is not correct for the app ... weird bottom taglines ... are obvious and don't need to be written." 13 Oct 11:10: "onboarding looks fine ... not more than 60% ... on the first page there's an AI-generated picture that doesn't look good." 14 Oct 00:23: "Remove that privacy line ... not to write useless stuff."
- **Raised.** 13 Oct 02:30, 13 Oct 11:10, 14 Oct 00:23.
- **Area and files.** `features/onboarding/**` (`welcome_view.dart`, `welcome_scene.dart`, `model/deck.dart`), `onboarding_routes.dart`.
- **Status: Built, plausibly working.** The five-question sample is gone from the app (old paths open the onboarding), the welcome opens with Mobi, a sheet deck replaced the sample, and a search of the app for the filler lines ("not affiliated", "not a prediction", "ad or analytics companies") finds none. The owner has said it "looks fine"; later feedback does not return to it. Another agent is editing onboarding files now (uncommitted).
- **Acceptance check.** Fresh install, no account: the first screen is Mobi greeting, no stock or AI picture; the steps (stage, course and colleges, subjects, worry, question, study days, plan, save) can each be skipped except the last; no screen carries a disclaimer line; ending shows the sealed plan and the first move.

### L29 Sign-in works and stays signed in (repeated)
- **Owner words.** 13 Oct 11:25: "there were a lot of issues with signing in and keeping the account logged in, especially with Google and the email code." 15 Oct 20:04: "Continue with Google is not working. Big bug ... Send code is also not working." 15 Oct 20:28: "Google login is working now."
- **Raised.** 13 Oct 11:25, 15 Oct 20:04, 15 Oct 20:21; he confirmed Google working on 15 Oct 20:28.
- **Area and files.** `core/auth/**`, `features/auth/**`, `core/api/api_error.dart` (blocked classification).
- **Status: Built, plausibly working.** Google returns to the app since the Supabase Redirect URL was added by the owner; the email-code path works after Vercel Attack Challenge Mode was turned off; edge-firewall 403s are now retryable. "Stays signed in" has not been re-confirmed by him.
- **Acceptance check.** Account A: sign in with Google (returns to the app), sign in with an email code, sign out, sign in again. Force-stop and reopen after 24 hours of the emulator clock: still signed in. A second sign-in on the same device for B does not show A's data.

### L30 Add colleges in onboarding
- **Owner words.** 16 Oct 10:32: "This Add the Colleges needs to be incorporated into the onboarding section only. I'll see if you have done that or not."
- **Raised.** 16 Oct 10:32 only.
- **Area and files.** `features/onboarding/steps/course_step.dart`, `widgets/college_ladder.dart`, `model/answers.dart`, `features/tools/data/my_colleges_actions.dart` (`_legacy`, `_migrate`).
- **Status: Built, plausibly working.** Onboarding step 2 is "course and colleges": a ladder of up to 3 DU colleges with 2026 Round 1 scores, or "Any college is fine"; after sign-in those colleges are moved into the server My colleges list. Two limits: it is not the My colleges chooser (no programme search, 3 not 8), and an existing account never sees onboarding again, so he cannot see it unless he signs up with a new account. The sheet's own line says course and colleges "stay on this phone for now" (`copy.dart:231`).
- **Acceptance check.** Fresh install, account B: on the course step choose a course and 3 colleges (or "Any college is fine"), finish, sign in. Open Today's "Your colleges" and My colleges: the 3 colleges are there. Skip the step: My colleges is empty and Today shows the Choose key.

## Navigation

### L31 Bottom bar aligned with the Start bubble; labels aligned; rethink (repeated)
- **Owner words.** 13 Oct 02:30: "a good navbar wouldn't look like this ... not interactive at all." 13 Oct 11:10: "very fluent and snappy ... require a lot of finish." 14 Oct 18:30: "rethink the design and overall structure." 14 Oct 20:51: "the icons on the bottom half bar also look extremely weird." 15 Oct 20:20: "5 to 6 things." 16 Oct 10:32: "I need the bottom nav bar to be perfectly aligned with the bubble and how it's showing things, especially the text that is showing."
- **Raised.** 13 Oct 02:30, 13 Oct 11:10, 14 Oct 18:30, 14 Oct 20:51, 15 Oct 20:20, 16 Oct 10:32.
- **Area and files.** `core/widgets/bar/mm_bar.dart`, `bar_tabs.dart`, `bar_lens.dart`, `start_key.dart`, `bar_icons.dart`, `bar_glass.dart`; spec `docs/brain/ui-phase2/DOCK.md`.
- **Status: Built, likely broken.** The structure he asked to rethink is built (Today, Practice, Start key, Review, You, with a lens that moves under the active tab, Material icon pairs since 14 Oct 22:00, a live capsule). The last bar commit is 305a7be2 (16 Oct 00:07, glass); nothing was changed after his 16 Oct alignment note, and no device or screenshot check of icon, label and lens centres is on record. His note is specific and recent, so treat it as still true.
- **Acceptance check.** At 360x800 and 412x915, Night and Day: with a ruler overlay on a screenshot, the four tab icons share one baseline and the four labels share one baseline; the Start key's centre is on the same horizontal axis as the tab icons' centres (or its offset is deliberate and the same in both themes); the lens sits centred on the active tab's icon and label; moving between tabs slides the lens and the labels do not jump; at 1.3x font no label clips; with the live capsule showing, the bar stays aligned; the Start key's "Start" text is centred in the key.

### L32 Bar holds 5 to 6 useful things
- **Owner words.** 15 Oct 20:20: "The 5-to-6-things concept is getting fulfilled, but everything being useful is not."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `bar_tabs.dart`; audit `APP-UX-AUDIT` section 4 (Colleges as a fifth tab replacing You).
- **Status: Not built.** The bar has four places and Start; no Colleges destination exists (`VISION-INVENTORY` P1-9 missing). It is an open decision, not a defect.
- **Acceptance check.** Whatever the final five are, each must open a place a student uses weekly, and Compass and My colleges must be one tap from the bar (see L22).

### L33 Bar blur stronger
- **Owner words.** 15 Oct 20:20: "You have added a general blur, that's good, and it can be made a bit stronger."
- **Raised.** 15 Oct 20:20 only.
- **Area and files.** `core/widgets/bar/bar_glass.dart` (sigma 24, tint 60 and 68 percent), sheets sigma 18.
- **Status: Built, plausibly working.** Done in 305a7be2 (16 Oct 00:07), so it is in v10.
- **Acceptance check.** Scroll Today under the bar in Night and Day: content shows frosted and blurred through the bar and labels stay readable. A phone on the low-quality glass setting shows a flat tint instead; that is expected.

## Mobi and motion

### L34 Motion graphics, judged in use (repeated)
- **Owner words.** 13 Oct 02:30: "not interactive at all." 14 Oct 14:01: "not very good or premium, like a Duolingo level." 14 Oct 18:30: "what matters is, while using it, the animations, motion design, graphics, motion graphics." 15 Oct 02:53: "the motion graphics, animations, fluidity, finish I'm looking for." 15 Oct 21:15: "refining the UI/UX, the motion, motion graphics design." 16 Oct 10:45: "motion graphics design".
- **Raised.** 13 Oct, 14 Oct (twice), 15 Oct (twice), 16 Oct.
- **Area and files.** `core/motion/**` (tokens), `core/widgets/mm_stagger*`, `docs/brain/ui-phase2/MOTION.md`, per-feature motion in `features/**`.
- **Status: Built, plausibly working.** A motion language, entrances, springs, parallax, the finish ceremony, the clock turn, and a reduced-motion path exist. He judged builds v8 to v10 as "pretty similar" on 14 Oct and has not signed off since; the quality gate (critic with the 12-dimension rubric) was passed by the builders, not by him.
- **Acceptance check.** Record 60 seconds on the emulator (`adb shell screenrecord`) of: cold start, a tab switch each way, opening and dragging a sheet, starting a quick practice, answering, finishing, the result, the repair end. Every transition must be continuous (no snap, no blank frame, no frame that jumps), `adb shell dumpsys gfxinfo in.mockmob.app` shows janky frames under 5 percent, nothing animates inside a timed paper, and with "Remove animations" on every screen is still usable.

### L35 Mobi in every scene, tastefully, better looking (repeated)
- **Owner words.** 13 Oct 11:10: "the mascot also should be there in the app clearly, and it should have the animation ... like the Duo mascot of Duolingo." 14 Oct 14:01: "Duolingo level." 15 Oct 21:15: "better-looking mascot." 16 Oct 10:45: "Mobi integrated tastefully in every scene."
- **Raised.** 13 Oct 11:10, 14 Oct 14:01, 15 Oct 21:15, 16 Oct about 10:45.
- **Area and files.** `core/mascot/**`, `core/widgets/**` (`MobiCharacter`), per-feature Mobi widgets (Today 9 files, You 11, Runner 8, Insights 7, Practice 6, Onboarding 5, Review 5; Account sheet 0, Rule book 0, Tools 1); uncommitted `docs/design-decisions/app-mobi-moments-1016.md` and `test/unit/mascot/mobi_moments_one_per_screen_test.dart`.
- **Status: Built, plausibly working.** Rig v2 (31 acts) is built; Mobi appears in most features. A packet in progress right now applies "one Mobi per screen, at a real moment" (Saved, Revise). Mobi is absent from the Account sheet, the Rule book and mostly from Tools. Rig v2 is in APK v10 only if it was merged (it was merged into feat/app-and-web before 9ccb7d0c).
- **Acceptance check.** Walk every screen on account A: Today, Practice, a start, the result, Review, a repair, Ask, Saved, Learn, You, the avatar sheet, Compass, Rule book, and each empty or error state. At most one Mobi per screen, none inside a timed paper, each reacting to something real (greets, thinks while loading, cheers after a finish, oops on a failed load). Compare the look against the owner's reference once for taste.

### L36 One spacing system, balance, light/dark parity (repeated)
- **Owner words.** 13 Oct 11:10: "spacing overall can be improved." 14 Oct 18:30: "many spacing inconsistencies and light/dark mode inconsistencies ... Balanced is the highest favorability. Crowded is better than less, then over-gamified at the same level as less."
- **Raised.** 13 Oct 11:10, 14 Oct about 18:30.
- **Area and files.** `core/theme/**` (`MmSpace`, `MmRhythm`), `docs/brain/ui-phase2/SPACING.md`, `SPACING-AUDIT.md`, `ROBUSTNESS.json`.
- **Status: Built, plausibly working.** The system and its audit exist; 30 critic findings were worked in packets A to K. Not confirmed by the owner.
- **Acceptance check.** Every tab root and sheet in Night and Day: the same gutter, the same group gap, no screen sparse (one idea floating in empty space) or over-gamified (badges and counters competing). Day must have no low-contrast text and no dark leftovers from Night.

### L37 Subject art that says its subject
- **Owner words.** 14 Oct 20:51: "all the graphics ... basic and very childish compared to the extremely cool 3D graphics you generated previously." 14 Oct 22:15: the restored objects look "really premium"; weak ones are Accountancy, Computer Science, Business Studies and Languages.
- **Raised.** 14 Oct 20:51, 22:01, 22:15 (one evening).
- **Area and files.** `core/art/**` (`SubjectEmblem`, `obj-*.webp`), `core/widgets/art/subject_glyph.dart`.
- **Status: Built, plausibly working.** The photo-real 3D objects were restored (a48b8171, 14 Oct 21:48) and "every subject object" shipped in app wave 1 (45ac3513). The agreed plan to regenerate only the four weak ones, shown old next to new, has no commit I could find, so those four may be unchanged.
- **Acceptance check.** Practice subject strip and Today hero for Accountancy, Computer Science, Business Studies and English: each object reads as its subject at 40 dp and larger, none cropped, and a subject without art shows its initials, never another subject's object.

## Website parity

### L38 Ask Mobi with credits (repeated)
- **Owner words.** 15 Oct 20:20: "This Ask Mobi thing has really good UI ... whether it is integrated properly with the credit UI and the entire system that we have built is the question." 16 Oct 10:45: "Mobi as a bot assistant (Ask Mobi), credits (done)."
- **Raised.** 15 Oct 20:20, 16 Oct 10:45.
- **Area and files.** `features/insights/screens/ask_screen.dart`, `data/ask_controller.dart`, `ask_wallet.dart`, `widgets/ask_wallet.dart`, `features/credits/**`, `features/account_sheet/**`.
- **Status: Built, plausibly working.** Ask answers record questions for free on the phone, other questions use 1 AI credit with the cost and balance shown first; two credit names everywhere (practice credits, AI credits); a Credits page with history; Ask Mobi is the one name (the Start sheet's old "Ask your record" is gone from user text). He called credits done on 16 Oct.
- **Acceptance check.** Account A: Review, Ask Mobi. Ask "Which chapter loses me the most marks?": answer from the record, no credit spent, the wallet pill unchanged. Ask "Explain income statement": the screen says "Uses 1 of your N AI credits" before sending; after the answer N is lower by 1 in the Account sheet and on the Credits page history. Airplane mode: a plain message and no charge. Zero credits: the message says when they renew, and record questions still work.

### L39 Other website features missing in the app (repeated)
- **Owner words.** 12 Oct 18:20: "not just a copy of the website. It should be something more." 13 Oct 11:10: "We wanted this to be an extension of the website, having more than it. It doesn't even have all those things." 16 Oct 10:45: "other website features missing in the app."
- **Raised.** 12 Oct 18:20, 13 Oct 11:10, 16 Oct about 10:45.
- **Area and files.** `docs/brain/design-2026-10-13/WEB-PARITY.md` (master index), `VISION-INVENTORY-2026-10-16.md`.
- **Status: Not built.** Most of the website's student features exist in the app (practice setup, NTA mode, result analysis, Mistake Repair, Insights, Saved, Explore stream, Compass, Combo, 2027 guide). Checked against `lib` today and still missing: the repair record across devices (no `repair-record` call), the free exam-screen preview, a guided first-run tour with Mobi, lesson help with AI, a decision note to the playbook, the fresh check on 2 new questions (A.9), cohort time lines (slice 5, missing on both), weekdays stored on the account (they stay on the phone), subject hubs and previous-year guides (only as web links). Leaderboard, rival and upload are deliberately not built.
- **Acceptance check.** For each website student page, open its app equivalent from a cold start in at most 2 taps from a tab, with the same data (a paper done on the website is in the app's Review within one refresh, and the reverse). Build the missing list above in priority order the owner sets.

## Keep list (the owner liked these; do not regress)

- Subject selection animation and Smart practice (15 Oct 20:20), the Start sheet, the 3D subject objects after restore (14 Oct 22:15), logo B (13 Oct), the sealed-sheet onboarding as "fine" (13 Oct 11:10), NTA mode as done (14 Oct 19:17), Google sign-in working (15 Oct 20:28), the app as "a solid app, no major issues" apart from his account (16 Oct 10:32).
- His rules for any fix: never simplify by cutting ("confusing doesn't mean get off", 15 Oct); balanced beats sparse and over-gamified (14 Oct); no filler or defensive lines (13 Oct); judged in use, not in stills (14 Oct); every new feature for the app and the website together (14 Oct).

## Open questions for the owner

1. "Review Again is not working" (L14): which control did you tap, and on which screen?
2. "Interview mode" in the Practice list (L08): is that NTA mode? The app has no interview mode.
3. Which ring showed 3 after you chose 4 study days (L06): the ring inside the sheet, the This week tile on the road, or the ring on You?
4. Which two accounts failed on Today (L01), and does each have papers on the website?
5. Is the proposed Practice order (subject choice first, then modes, short to long) what you meant (L08)?
