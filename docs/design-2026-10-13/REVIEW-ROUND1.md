# Review round 1 findings (13 Oct 2026, three lenses)

## review1:taste-warmth

# Night Sheet review, round 1: taste, warmth and brand

**Verdict:** this is a real step up from the first build. The welcome scene, the answer-sheet reveal, the runner's palette, the identity card in You and the late-night states all look authored and warm. What still makes it feel half-done is mostly about how the screens are put together:

- All three tab roots use the same hero card: a red book at the top right, one big number and a volt button.
- Content shows through the bottom of the dock on every tab root.
- Selected items are styled four different ways.
- The lamp light is a flat brown wash instead of a pool of light from one side.
- Several lines of copy are untrue or contradict the screen they sit on.

I looked at all 79 screenshots in `tmp/app-shots/v2`, the four concept renders, the warm art, and about 36 goldens (Today, onboarding, Review, Practice, result, core, You and rhythm, night and day). I also checked the strings in `lib/`. I did not edit any code.

---

## P0: copy that is untrue or contradicts itself (integrity, brief section 10)

1. **Today hero numbers contradict each other, and "holds" is used in the wrong sense.** Seen in `today_late_night`, `today_returning` and `30_today_demo`.
   - The hero says "3 mistakes from Mock 7", then "Partnership fundamentals holds 4 of the 6 waiting" or "Its 6 mistakes are still here".
   - "Holds" is a reserved state word: it means a fresh check passed.
   - Fix in `features/today/copy.dart:42-44` and `mistakesLabel`:
     - The big number is tonight's batch. Set the unit to "mistakes tonight", and the support line to "3 of the 6 from Mock 7. 4 of the 6 are in Partnership fundamentals."
     - Replace `'$chapter holds $count of them.'` with `'$count of them are in $chapter.'`
   - Never use "hold" or "holds" for anything except the Holds state.

2. **"Ten real CUET questions" (`today/copy.dart:33-34`) and "One real question." (`onboarding/copy.dart:71`, `sheet_lines.dart:34`) are false.**
   - `warmup_pool.dart` says these are original questions written for the pool in CUET style. "Real CUET questions" means past papers to a student.
   - Change to:
     - "Ten CUET-style questions in $subject."
     - Question step headline: "One question from $subject."
     - Sheet line: "Warm-up: right in 41 s" or "Warm-up: one trap found".

3. **"Weakest first: Accountancy, then Business Studies" is shown when every subject is still "Okay".** Seen in 09, 20, 21 and 21b; source is `sheet_lines.dart:25`.
   - Give the order only when the ratings differ.
   - On a tie, say: "Accountancy and Business Studies, both Okay. Your check sorts them."

4. **"Board weeks count as two." (`onboarding/copy.dart:84`) says the opposite of the maths.**
   - `calendar.dart` caps board weeks at `boardWeekSessions`.
   - Replace with "During boards we count two a week."

5. **Two empty states claim different things.**
   - `core/state_empty` says "Every mistake you found is checked."
   - Review's all-clear says "repaired".
   - Unless a fresh check really passed, use "Every mistake you've found is repaired. A Quick 10 finds the next one."

6. **Time-of-day words are wrong in the morning.** "Tonight's repair" shows at 7:27 AM (63) and "all 3 repaired tonight" at 7:34 AM (68).
   - Add one helper and use it in `review/copy.dart:9`, `:147-148`, `ending_sheet.dart:72`, Today's "Tonight's move" and "How long have you got tonight?":
     - 5:00 AM to 3:59 PM: "today"
     - 4:00 PM to 4:59 AM: "tonight"

---

## P1: warmth and brand (what makes it look templated or cold)

7. **The three tab heroes are one template, and the red book is overused.**
   - Today (30), Practice (34) and Review (63) are the same card: overline, red book at the top right, big number, volt pill.
   - The book also appears on first move (24), card 3 (60), Review rows and the setup tiles: about 8 places.
   - This sameness is the biggest thing that reads as AI-made. Fix:
     - **Today keeps the art hero.** It should show the subject object for that day's subject, not always the book.
     - **Practice** leads with "Choose your own" subject tiles at 132×148 dp (that art is good). Shrink the recommendation to a 96 dp row: object 56 dp on the left, "Partnership fundamentals · 10 questions" and a volt pill on the right.
     - **Review** leads with the sheet itself: a 5-column row of rose X bubbles (22 dp) for tonight's mistakes, then the Found → Repaired → Checked → Holds thread line, which today only shows on the repair entry page. No object art in the Review hero.
     - On first move and card 3, use the subject light field and Mobi-point instead of the book.

8. **The lamp light is a flat wash, not a pool.**
   - I sampled the result scenes (55, 60): roughly #2A2010 everywhere, and *brighter* bottom right (#3A2D19). There is no falloff to the ground colour #12110E, so the scene reads as muddy brown rather than a lamp-lit desk.
   - Fix in `light_field.dart` for moment scenes:
     - One radial gradient centred at (-0.65, -0.95) in Alignment space, radius 1.1 × width.
     - #F2A93B at 18% at the centre, 6% at 0.55, 0% at 1.0.
     - Then a bottom vignette over the lower 35%: ground at 0% to 85%.
     - Remove the second field at the bottom right.
   - Work screens (runner, submit, settings) get no lamp at all, which is already true on the runner.

9. **Content shows through the bottom of the dock on every tab root, in both themes.** Seen in 30, 34, 44, 63, 75 and 76.
   - Text sits between the pill and Start, and under the pill.
   - Add a non-interactive ground scrim behind the dock:
     - Height: dock height + 10 dp + bottom inset + 48 dp.
     - Vertical gradient: ground at 0% at the top, 88% at 40% of the height, 100% at the bottom.
     - Paint it in its own `RepaintBoundary`, not as a `saveLayer`.
   - Give tab-root scroll views bottom padding of 60 + 10 + inset + 24 dp so the last row can scroll clear.

10. **Selected items are styled four different ways.**
    - Volt-border card (stage, worry), cream-filled pill (course chip, time window, age, repair minutes), raised dark segment (minutes, glass), white-border tile (subjects).
    - The cream fill (#F4F0E6 at 100%) is the loudest object on those screens and off-brand.
    - Use one OMR language everywhere:
      - Selected = Raised2 #25231E fill, a 1.5 dp border in ink #F4F0E6 at 70%, and a leading 10 dp bubble filled volt.
      - Unselected = a hollow bubble with a 1 dp hairline ring in Ink3.
    - Segmented controls keep the raised tile but add that 10 dp bubble before the label.

11. **Onboarding answers are a generic radio list.** Seen in 03, 04, 10 and 11.
    - Use answer-sheet rows instead:
      - 56 dp height, a leading 28 dp letter bubble (A, B, C, D with a Hanken 13 w600 letter) that fills volt with a 280 ms ink.
      - No trailing radio.
      - Label in Hanken 16/24.
    - That puts the OMR idea on every step, as the warm-up question (12) already does.

12. **The plan reveal (16 to 19) is a card, not a moment.**
    - The brief calls for the sheet flipping to show the plan on its back.
    - At present it is six volt dots, a volt border and a volt "Hold to seal" outline, with a small orphan caption floating 90 dp above.
    - Fix:
      - Number the lines like OMR rows: "01" to "06" in BricolageCondensed 13, Ink3, 28 dp gutter. Drop the volt dots.
      - Add timing marks: 3×10 dp bars every 24 dp down the left edge, Ink3 at 40%.
      - Move "Your plan, built from your answers." inside the card as its overline.
      - Put the lamp pool behind the card.
      - On seal, stamp the foil at the card's centre-right, 88 dp, with a 1.0 → 0.92 → 1.0 scale over 280 ms and `mediumImpact`.
      - Volt then appears only on the newest engraved line and the seal.

13. **The foil seal is clipped by the card and the screen edge** on the save step (20, 21, 21b, 25) and sits half off the card in 19.
    - Place it inside the card at right 20 dp, bottom 20 dp, size 64 dp, rotated -8°.
    - Add a soft drop shadow: black 40%, blur 12, y 4.

14. **The onboarding sheet card reads as a stepper, not an answer sheet.**
    - Labels "CUET, Aim, Subjects, Marks…" at 11 sp under 20 dp rings look like any progress stepper.
    - Fix:
      - Put the column numbers "1" to "7" above the bubbles in Hanken 11 Ink3, OMR-style.
      - Make the bubbles 22 dp with a 1.5 dp ring.
      - Labels in all caps at 10 sp with +0.8 letter-spacing.
      - Double the timing marks along the right edge to 2×8 dp at 50% Ink3.
      - Rename "Marks" (the worry step) to "Worry".
      - Replace the placeholder "Weeks to CUET print here" plus grey bar (03, `answer_sheet_card.dart:186`) with Ink3 text: "Your weeks to May land here."

15. **The week bubbles on Today are about 8 dp and squeezed into the header's right corner.** Seen in 30 and all Today goldens.
    - This is the brief's signature week row, and today you can't read it.
    - Give it its own row under the greeting:
      - Seven 18 dp bubbles, 10 dp apart, day initials in Hanken 11 Ink3 underneath.
      - Study days that are done: volt fill. Today: a 2 dp paper-white ring. Rest days: dashed.
      - Left-aligned with the greeting text at the 16 dp gutter.

16. **The amber "lamp catch" on solid cards looks like a glitch.** The orange sliver on the top-left corner shows on 71 Weekly goal, 72 Reduce motion and 77 notification cards.
    - Either spread it along the straight top edge as a 1 dp line, #F2A93B at 30% at x=0 fading to 0 by 45% of the width, never on the corner arc;
    - or keep it only on glass (dock, sheets, heroes) and remove it from solid work-layer cards. I recommend this one.

17. **The milestone shelf has a hard-edged rectangular glow band behind the empty sockets** (71).
    - Replace it with a 2 dp shelf line (Hairline #312E27) under the tokens.
    - Each socket gets its own radial pool: #F2A93B at 10% → 0 at 56 dp radius.
    - Make the sockets 64 dp and show the token art at 25% opacity, desaturated, as a "not yet" ghost instead of a black hole.

18. **Mobi looks pasted on in the result recap.**
    - Card 3 (60) has a 40 dp Mobi squeezed left of the CTA. Card 4 (61) has a 52 dp sticker at the top right.
    - Show one Mobi per recap, on card 4 only:
      - 112 dp mobi-cheer, or mobi-point when the result is lower.
      - Left-aligned above the repair panel, with the 420 ms settle and one hop.
      - A single glass bubble line, for example "Third full paper this month."
    - Remove Mobi from card 3.

19. **The quick-start sheet (36, `quick_start.dart`) is a generic icon, title and chevron list.** The icons are a lightning bolt, a document and a wrench.
    - Use bubble glyphs in 40 dp tiles:
      - Quick 10: ten 5 dp bubbles in two rows.
      - Full mock: a 5×5 micro-grid of 3 dp bubbles.
      - Repair: one 16 dp rose X bubble with a volt ring.
    - Title: "What's it going to be tonight?" (time-aware), or "Pick today's work" in the daytime.
    - The Resume row, when present, gets the lit edge.

20. **The Start button looks like a media-player play button**: a volt ring around a play triangle.
    - Fill it as the concept does: a 60 dp volt disc (#D2F000) with a #0B1000 glyph, 2 dp outer glass ring, and a 14% volt glow *below* it.
    - Then lower the hero CTA on tab roots to the volt outline style so volt stays a single light. If the owner prefers it the other way, keep it glass and say why.

---

## P2: layout and polish

21. **Practice and mock confirm pages show the dock, and it covers Start (50).** These are pushed routes.
    - Hide the dock on all `/practice/setup/*` pages, matching the runner, repair and result.
    - Pin the CTA at the bottom: 16 dp gutter, 16 dp + inset from the bottom, sitting on the same ground scrim.

22. **The mock confirm's 50-bubble grid fills only about 60% of the width (50).**
    - Lay it out 10 columns across the full content width (352 dp, so 35.2 dp per column) with 14 dp bubbles centred in each cell.
    - Or show five rows of ten numbered bubbles, as the received screen (54) does well.

23. **The 50-question palette needs a scroll to reach "Review and submit" (53).**
    - Pin a sheet footer: 16 dp top padding, a hairline above, the button inside it.
    - Open the sheet at 0.88 of the screen height.
    - Keep the 5-column grid of 48 dp targets scrolling above it.

24. **The runner's progress strip uses dashes and ticks, not bubbles** (39 and 51).
    - Practice (10): 10 dp bubbles, 8 dp gap. Answered = ink at 55%, current = a 1.5 dp paper ring, unvisited = hairline ring.
    - Mock (50): keep the tick marks, which read as OMR timing marks, but make the current tick 3×12 dp in paper white.

25. **Card 3's chapter tiles leave an orphan (60):** "44" wraps alone onto a second row.
    - Use six tiles per row: (352 − 5×8) / 6 = 52 dp wide, 60 dp tall.
    - Or show them as one row of numbered bubbles like the sheet.
    - The book art at the top right leaves an empty block of about 180 dp at the top left. Drop the art and start the headline 24 dp under the story bar.

26. **College ladder (06, 07):**
    - The list runs under Continue with no fade. Add a 32 dp ground fade above the CTA.
    - Drop "(W)" from "Lady Shri Ram College for Women"; the name already says it, and the row then fits on one line.
    - "Open to any college" reads as a filter. Label it "Any college is fine".
    - The course chip with a pencil should be a plain text button: "B.Com (Hons) · change".

27. **Course tiles repeat "colleges took it in 2026" six times (05).**
    - Say it once in the subtitle, which already does.
    - In each tile, set "55" and then "colleges" at 55% size, top-aligned.
    - Course name in Hanken 15/20 w600.

28. **Subject rows say "Starting point ready" on every subject (08, 09, `onboarding/copy.dart:63`).** The line means nothing there.
    - Remove it, or replace it with that subject's question count: "12 chapters".
    - Also remove the volt bubble in front of each subject, so volt stays for actions.

29. **First move (24):**
    - The bottom third is empty.
    - The server line shows before the student has done anything.
    - Fix: put mobi-point (120 dp) bottom-left pointing at Start, with the bubble line "Ten minutes. I'll be here after."
    - Show the "needs your account" line only after a guest taps Start.

30. **The sealed sheet's "Open your result" button has a stray "=" glyph (55).** Remove the icon.
    - "Saved on the server." and "Marked on the server. Open it when you are ready." say the same thing twice. Keep "Marked on the server."

31. **The trap-fix heading (13_try_wrong) is in wrong-answer rose with a trailing colon, and the panel covers option D.**
    - Heading in ink: "That's the trap. The ten-second fix".
    - Push the panel below option D, or collapse the unchosen wrong options to 40 dp.

32. **The unfold flap goes wider than the screen at about 80% open (`sealed_unfold80`, 56).** The header text skews off-screen.
    - Clamp the perspective to 0.0012 and the maximum rotateX to 88°.
    - Clip the flap to the sheet's width.

33. **Practice's "Show me" is an underlined link, while Today and Review use a pill.** Use the pill everywhere: 32 dp tall, three 6 dp evidence bubbles, then "Show me" in Hanken 13 w600.

34. **Review headline wraps to three lines (63).**
    - Set the hero chapter title in BricolageTitle 24/28, maximum two lines, and drop the subject prefix ("Partnership:") when the overline already names the subject.
    - Reconcile "3 mistakes" in the hero with "5 mistakes to repair" for the same chapter in the list: label the hero "3 from Mock 2 · 5 in all".

---

## P3: remaining copy, in the brief's voice

| Where | Now | Better |
|---|---|---|
| Plan line, `plan.dart:85` | "Partnership is first in MockMob's chapter order for Accountancy." | "Accountancy starts at Partnership. Admission, retirement and dissolution all build on it." |
| `plan.dart:65` | "first in our chapter order" | "the first chapter on your plan" |
| Save footer, `copy.dart:108` (brief section 8 removes "on this phone") | "Everything so far is on this phone until you save." | Delete it. "Not now" already says enough. |
| Return welcome, `copy.dart:23` | "Your sheet is on this phone, right where you left it." | "Your sheet is where you left it. 3 of 7 filled." |
| Today returning | "Evening, Asha" + "Welcome back, Asha." (name twice) | Hero: "Four days off. How long have you got tonight?" |
| Quick-start title | "Start something" | "What's it going to be tonight?" or "Pick today's work" |
| Not found, `review/copy.dart:132` | "This mistake is no longer on your account." / button "Mistakes" | "We can't find this mistake any more. It may already be repaired." / "Back to Review" |
| Recap card 1 | "26 + 15 + 9 = 50 questions." | Delete it. The full result keeps the arithmetic. |
| Recap card 2 | Paragraph "Of 250 marks: … 15 + 75 + 45 = 135." | Delete it. "Show the arithmetic" covers it. Lead line: "75 went on answers you got wrong." |
| Card 4 and sealed screen | "Mock 7 done. That's your third full paper this month." on both | Say it once, on card 4. |
| `card4_first` | "Your first full paper this month." | "Your first full paper." |
| Card 4, `result/copy.dart:139` | "Fresh check: not available yet." | Delete it, or "Fresh check opens on 16 October." if the date is known. |
| `rhythm/copy.dart:51` | "Weeks in rhythm: 3" | "3 weeks in rhythm" |
| Submit page | "0 marked for review" | Hide the line when it is 0. |
| Today resume | "Continue" | "Resume Mock 8" |
| Practice tile | "Business studies" | "Business Studies" (proper name) |
| Repair ending | "Checked needs fresh questions you haven't seen. Those open later." | "Checked comes later, on questions you haven't seen. That's how we know it holds." |

---

## Keep these (don't regress them)

- **Welcome:** the lamp-lit desk art, the headline, and the volt dot in the wordmark (a better OMR read than the brief's hairline; record it as a decision).
- **Late-night states:** "Up late, Asha", sleepy Mobi, "Late one tonight. Ten minutes, then sleep."
- **Result reveal:** the answer grid inking with the "115 of 250" numbers.
- **Runner:** the numbered palette bubbles.
- **Received screen:** "Your sheet is in." with the 5×10 sheet.
- **You:** the identity card with embossed bubbles and timing marks.
- **Practice resume:** the Economics teal light field.
- **Appearance:** the theme previews.
- **Daylight:** the paper theme.
- **Mock confirm:** "Water, pencil, rough sheet. Ready when you are."
- **Hinglish caption:** "Aaj ka repair: 10 minutes, Partnership."

## Limits of this review

- Screenshots 36, 43 and 53 were taken before the sheet tint went to 0.86. In the newer `leave_guard` and `quick_start` goldens the bleed-through is gone, so I did not count it.
- 32, 14 and 21 show the old "778.4" and "0 s" values, which the report says are fixed.
- Blur quality on the M06 is still unseen.

## review1:integrity-flow

**Round 1 review: truth, integrity and flow (Night Sheet build)**

I read the code paths and opened every `_s` screenshot. I made no code changes.

**High**

1. **The Start sheet promises a fresh check that doesn't exist.** `lib/core/router/quick_start.dart:100-104`
   - Problem: the note on "Repair the next mistake" says "A worked explanation, then a fresh check." Review's own copy says fresh checks are not available yet. The row also opens the mistakes list, not the next mistake, and it shows even when there is nothing to repair.
   - Fix:
     - Change the note to "A worked explanation for your next mistake."
     - Send it to `AppRoutes.reviewRepair(tonight.attemptId, tonight.items.first.questionId)`, using `reviewIndexProvider.tonight`.
     - Hide the row when `tonight == null`.

2. **Practice has a deadline the student never sees.** Runner, practice skin (`widgets/runner_layout.dart:62`, `runner/copy.dart:103`)
   - Problem: the practice skin hides the timer, but the session still ends at `endsAt` (Quick 10 ran from 7:17 to 7:27). The leave sheet then says "The clock keeps running…", about a clock that was never on screen.
   - Fix:
     - In practice, show a static "Open until 7:27 AM" in `runner_meta_row.dart`. Static text only; no ticking timer.
     - Add the same time to the "Feedback comes after you finish." line.
     - Practice leave copy: "This practice stays open until 7:27 AM. Your answers stay in it."
     - Keep "The clock keeps running" for mocks only.

3. **The mock confirm page's Start key is under the dock** (`50_setup_full`). The main action can't be seen until you scroll.
   - Fix: on `/practice/setup/*`, either hide the dock (as on the runner) or add bottom padding of dock height + 10 dp + `viewPadding.bottom` to the setup scroll view. Re-take 50 at 384x853.

**Medium**

4. **"This is your first repair." can be false.** `review/data/repair_run.dart:55`
   - Problem: it is decided from local repair records only. After a reinstall, a new phone or `pm clear`, someone with past repairs is told it is their first.
   - Fix: take it from `/api/me/rhythm` `milestones` (`first_repair.achievedAt == null` before this run). With no rhythm data, show no line.

5. **Result card 4 says "9 not attempted. They are in Review." even when they are not.** `result/recap/record_parts.dart:87`, `review/data/mistake_index.dart:239`
   - Problem: Review only keeps the blanks of the newest attempt that has blanks. For any older result (Replay recap, a deep link), the line is false.
   - Fix: say "in Review" only when `index.blanks?.attemptId == m.attemptId`. Otherwise just say "9 not attempted."

6. **Today misuses "Holds".** `today/copy.dart:43-44`
   - Problem: "Partnership fundamentals holds 4 of them" uses the word reserved for a passed fresh check.
   - Fix: "4 of them are in Partnership fundamentals." and "4 of the 6 waiting are in X."

7. **Today and Review give two different "tonight" repairs.**
   - Problem: Today uses every candidate of the latest basis attempt (6 mistakes, about 20 minutes, `today/logic/move_builder.dart`). Review uses the largest open chapter of the newest attempt with open mistakes (3 mistakes, `mistake_index.dart:255`). On the same evening the student sees two different "tonight's repair" claims.
   - Fix: move one `TonightPick` builder into `core/domain`. Feed it to the Today hero, the Review hero and the Start sheet, and test that they agree.

8. **Blocked notifications leave a dead end.** Notifications (`notifications/widgets/settings_sections.dart`)
   - Problem: the toggles still show On, and there is no way to fix it from the screen, only typed instructions.
   - Fix:
     - When permission is denied or unavailable, dim the toggles and add the caption "Saved. Nothing arrives until Android allows it."
     - Add an "Open Android settings" key through a MethodChannel to `Settings.ACTION_APP_NOTIFICATION_SETTINGS` in `MainActivity`. This needs no pubspec change.

9. **The plan says "built from your answers" while skipped steps use silent defaults.** `onboarding/model/plan.dart` (`FirstMove.of`, `rhythmLine`)
   - Problem: skipped steps fall back to Accountancy and "4 evenings, 20 minutes, 8:00 PM", presented as the student's own choices.
   - Fix: when the step is in `answers.skipped`, mark that line "(our default, change it any time)", or change the intro to "Built from your answers and a few defaults."

10. **The demo data can't prove numbers agree across screens.**
    - Problem, all in the demo screenshots:
      - The submit page says 6 of 10 answered; the result says 7 right, 2 wrong, 1 blank.
      - Today says Mock 7 was 204; the reveal says 115.
      - You shows every milestone unlit for a student with 7 mocks.
    - Fix:
      - Build `demo_main.dart` from one attempts list that feeds Today, the result, Review and rhythm.
      - Add tests that check:
        - submit counts equal result counts;
        - the Today mistake count equals the result candidates for the same attempt;
        - the token shelf matches the milestones.
    - Signed-in flows have still never touched the real API; that sign-in is still owed.

**Low to medium**

11. **DU labels are imprecise.**
    - Problem:
      - The course tiles say "colleges took it in 2026". Colleges don't take a course; the number is colleges with Round 1 allocations.
      - Today says "Round 1 closing scores". They are minimum allocation scores, and later rounds go lower. Onboarding already says "lowest score that got a seat".
    - Fix:
      - Tiles: unit "colleges", with the support line "Seats offered in CSAS 2026, Round 1" (`onboarding/copy.dart:40-42`).
      - Today caption: "CSAS 2026, Round 1 minimum scores, UR, out of 1000" (`today/copy.dart:132`).

12. **The pace step says "Board weeks count as two."** It reads as if board weeks count double; the code means two sessions a week. Fix: "Two a week during boards."

13. **Onboarding warm-up, wrong answer** (`13_try_wrong`).
    - Problem: option D is hidden under the fix panel, and the right option is marked by its volt fill alone, with no words.
    - Fix: add a "Correct answer" caption as the repair panel does, and make the step scroll so all four options stay reachable.

14. **The effort line ignores the app's own rule.**
    - Problem: "Mock 7 done. That's your third full paper this month." shows on the sealed sheet and again on card 4, and on lower and held results too. `recap_variant.allowsTokens` documents that effort tokens never show after a lower or held result.
    - Fix: show it once, on card 4 only. For lower and held results, either drop it, or keep it as a plain line and correct the doc comment.

15. **Banned copy and dead code are still in the codebase.**
    - `core/copy/state_words.dart`: `practiceRecorded` and `practiceFinished` contain "This is practice, not proof." Both are unused, but `test/unit/core_ui/formatters_test.dart:109-122` still asserts them.
    - `core/router/placeholder_screen.dart` is unused.
    - Fix: delete the two receipts, their tests, and the placeholder file.

16. **The runner shows "Saved" on question 1 before any answer** (39, 51). Fix: show the save pill only after the first answer has been acknowledged.

17. **The first move page is crowded at the bottom and empty in the middle.**
    - Problem: the "The check is marked on our server…" footnote repeats the save-step banner, and the lower third is empty (24).
    - Fix: drop the footnote, since the save banner already says it. Give the space to the plan's next three days, or centre the card.

18. **The question step offers two skip controls:** "Skip" at the top and "Skip this one" at the bottom. Keep one.

19. **Some screenshots are stale.** 14, 20 and 21 still show "right in 0 s" from before the fix. Re-take them so the evidence matches the code.

**Checks that passed**
- The repair ending only counts repairs the server acknowledged.
- The submit stages use only real calls, and the success haptic and lamp come only after "Received".
- No art, Mobi or lamp appears in the runner.
- The reveal never withholds:
  - "Open without the reveal" is offered, including as a TalkBack action;
  - "Skip to full result" is available;
  - after three sheets a tap opens the reveal, and the "Open results directly" setting works.
- Mobi stays off a lower result's cards 1 and 2.
- Sessions-before-May and weeks-to-May are plain arithmetic on the student's own choices.
- Chapter order is worded as "first in MockMob's chapter order", with no frequency claim.
- The DU aim line carries its source, category and scale.
- The age question defaults to usage data off.
- Back is guarded on onboarding, the submit page and the repair ending.
- The non-affiliation statement appears only in Help > About.

## review1:perf-a11y

# Round 1 review: performance and accessibility on the 3.5 GB MediaTek phone

Four things need fixing before the morning check: the glass auto-downgrade, the dock labels, the faint grey text colour (`ink3`) in Night, and the onboarding back button for TalkBack. I changed no code. The proposed fixes below are untested.

All paths are under `C:\Users\atish\Desktop\mockmob copy\mockmob-next\flutter_app\`. Contrast figures come from a WCAG calculation on the theme colours. Two findings were also seen in device screenshots: the bleed-through behind the dock and the tiny sheet labels.

## High

**1. The automatic switch to Lite gets saved as if the student chose it, and it can fire for the wrong reasons.**
- **Where:** `lib/core/theme/glass_quality.dart`, `downgrade()`, `GlassPerformanceWatch` and `RasterBudgetMonitor.add`.
- **Problem:** `downgrade()` calls `choose(lite)`, which saves Lite for good. Appearance never says it was automatic.
- The watch counts any 2 s of continuous rendering: cold open, onboarding engraving, hold-to-seal, the unfold. Some of those screens have no live blur at all, so dropping to Lite gains nothing there and still sticks.
- It also runs in debug builds, whose engine is slower. The emulator already saved Lite this way. If the owner benchmarks the M06 on the debug APK, he will probably be judging Lite without knowing it.
- **Fix:**
  - Only start the watch when `kReleaseMode || kProfileMode`.
  - Only feed frames while a user scroll is active (pass `UserScrollNotification` start and end from `AppShell`) and while at least one Full `GlassSurface` is mounted (a static counter in a tiny stateful wrapper).
  - Save the downgrade under its own key (`glassAutoLite`) instead of the user's choice. Show "Switched to Lite to keep scrolling smooth" in Appearance, and let picking Full clear it.
  - Before the benchmark, clear the emulator's saved Lite: `pm clear` or pick Full in Appearance.

**2. The downgrade can never fire on the slowest phones.**
- **Where:** `RasterBudgetMonitor` (`minFrames = 60`, 250 ms idle gap).
- **Problem:** 60 frames in a 2 s window needs at least 30 fps. Once raster p90 is above about 33 ms (the phones that most need Lite), it never fires. Above 250 ms per frame, every frame counts as an idle gap and resets the window.
- **Fix:**
  - Set `minFrames` to 20 and drop the `span >= 0.9 × window` requirement when there are 20 or more frames.
  - Treat a gap as idle only if it is longer than `max(250 ms, 3 × the median raster time)`.
  - Base the threshold on the refresh rate (`min(12 ms, 0.9 × the vsync period)`).
  - Add tests at 25 fps with 40 ms frames and at 4 fps with 300 ms frames (`test/unit/core_ui/glass_quality_test.dart`).

**3. Inactive dock labels and icons fail 4.5:1 over real content.**
- **Where:** `lib/core/widgets/dock/dock_pill.dart`, `_DockTab`, which uses `ink3`.
- **Problem:** at Night tint 0.62, `ink3` drops to 1.5–2.1:1 over a volt key, white text or lamp art scrolling under the dock. In Daylight at 0.72 it is 3.1–3.3:1 over dark content.
- The device shot `31_today_scrolled.png` shows this: "Deshbandhu College" and "763" read clearly through "Practice" and "Review".
- **Fix:** use `ink2` for inactive labels and icons. That gives 5.3:1 at Night 0.62 with half bright coverage after blur, 6.4:1 in Lite, and 5.1:1 in Daylight over black. Keep `ink` for the active tab.

**4. Night `ink3` is below 4.5:1 on its own surfaces.**
- **Where:** `lib/core/theme/mm_colors.dart`, Night `ink3 #8E877A`.
- **Problem:**
  - 4.41:1 on `raised2`.
  - 3.8–4.3:1 over the lamp field (Today's offline caption at the top left, and onboarding captions with lamp strength 0.85).
  - 3.84–4.47:1 on the amber, teal, moss, indigo and rose subject fields.
- **Fix:** Night `ink3` becomes `#A09989`. That gives 5.54:1 on `raised2`, 4.78:1 at lamp 18% and at least 4.8:1 on every subject field, and it stays clearly below `ink2`.

**5. The onboarding back button probably does nothing when double-tapped in TalkBack.**
- **Where:** `lib/features/onboarding/screens/onboarding_flow.dart:255`, `_TopBar`.
- **Problem:** the outer `Semantics(button, label, excludeSemantics: true)` has no `onTap`, so it hides `MmPressable`'s tap action. Every onboarding step is affected. Android's system back still works.
- **Fix:** delete the outer `Semantics` and pass `semanticsLabel: OnboardingCopy.back` to `MmPressable`.

## Medium

**6. The status-bar fade changes the tree shape above the whole app.**
- **Where:** `lib/app.dart`, `_StatusBarScrim`.
- **Problem:** `if (top <= 0) return child;` versus `Stack(...)`. When the top inset reaches 0 (the runner's `immersiveSticky` on phones without a notch), the `Router` is recreated and the navigators are re-parented. That means a rebuild of the whole app at mock start and exit, a route re-parse, and lost state above the navigators.
- **Fix:** always return `Stack(children: [Positioned.fill(child: child), if (top > 0) Positioned(...)])`.

**7. Targets under 48 dp.**
- **Where:**
  - `lib/features/runner/widgets/runner_controls.dart`: `RoundIconKey` (leave) and `SheetKey` (Questions) are 44×44. These are the runner's two main controls.
  - `lib/features/onboarding/widgets/day_picker.dart`: each day is 44 wide.
- **Fix:**
  - For the runner keys, wrap the 44 dp face in `SizedBox.square(48)` inside `_SolidKey`, so the hit-tested box is 48.
  - For the day picker, set `width: 48`. Seven 48 dp days fit in 344 dp.

**8. The welcome art pops in late.**
- **Where:** `lib/core/widgets/art/mm_art.dart` (`heroSlab('hero-slab')` has no file) and `lib/features/onboarding/screens/welcome_view.dart`.
- **Problem:** every welcome first fails to load the missing asset, then falls back to `hero-desk` and decodes it. There is no precache during the 1.4 s cold open.
- **Fix:**
  - Change `heroSlab` to `'hero-desk'`, or remove it.
  - In `ColdOpen.didChangeDependencies`, add `precacheImage(ResizeImage(AssetImage(MmArt.heroDesk.asset), width: (size.width*dpr).round()), context)`, plus `mobi-greet`.

**9. Sheets pay for a full blur that barely shows.**
- **Where:** `lib/core/widgets/materials/glass_surface.dart` (sheet tint 0.86 and 0.88 with sigma 28).
- **Problem:** this is the largest blur area in the app, and at 86% tint the blur contributes about 14% of what you see. While a sheet is open, the dock's two panes also keep blurring under the scrim, so there are 3 backdrop passes per frame of the sheet animation.
- **Fix:**
  - Choose one: either sheets skip the `BackdropFilter` at these tints (draw as Lite), or go back to about 0.70 with blur and check it on the M06.
  - In `AppShell`, while `ModalRoute.of(context)?.isCurrent == false`, pass `quality: GlassQuality.lite` to the dock.

**10. The answer-sheet step labels are too small and never grow.**
- **Where:** `lib/features/onboarding/widgets/answer_sheet_card.dart:139-160`.
- **Problem:** the labels are 10 sp, use `TextScaler.noScaling`, and are mostly `ink3` over fake glass. The 1.3x golden shows them unreadable.
- **Fix:** 11.5–12 sp, `ink2`, `textScaler: clamp(maxScaleFactor: 1.3)` with `FittedBox(scaleDown)` on each label.

**11. Accessibility verification gaps.**
- **Problem:**
  - There is no `meetsGuideline` test anywhere.
  - There are no 1.3x goldens for Today, Practice, Review, You, the dock or the quick-start sheet.
  - 250 goldens are 384×853 pixels, so they render at DPR 1, not the required DPR 2. Decode sizes and hairlines are therefore not checked.
- **Fix:**
  - Add `androidTapTargetGuideline`, `labeledTapTargetGuideline` and `textContrastGuideline` checks for each tab root, the quick-start sheet, the runner and the sealed result.
  - Add 1.3x goldens in both themes.
  - Set `tester.view.devicePixelRatio = 2` in the feature harnesses.

## Low

- **12. See-through art drawn with an `Opacity` widget inside scrolling content.** This happens in `lib/features/today/widgets/sealed_hero.dart:82` (0.9 over a repeated tile) and `lib/features/practice/widgets/subject_tiles.dart:118` (0.86 on each unselected tile). These only avoid an off-screen pass if an engine shortcut applies, and Impeller has no raster cache.
  - Fix: use `Image.asset(opacity: AlwaysStoppedAnimation(x))` or `DecorationImage(opacity:)`, as `paper.dart` already does.
  - `sealed_hero` also repeats `paper-tile`, while `paper.dart` notes the tile has a visible seam. Use `fit: cover` instead.
- **13. Art decoded at full size.** `ArtImage` is used without a width or height in `subject_tiles`, `suggestion_card` (176 dp box), `hero_stage`, `ending_sheet` and `welcome_view`, so 512 px objects are decoded for tiles of about 100 dp.
  - Fix: pass the known box sizes, or have `ArtImage` use a `LayoutBuilder` to set `cacheWidth` from its constraints when no size is given.
- **14. The unfold rebuilds the sheet body every frame.** In `lib/features/result/recap/sheet_stage.dart`, `_sheet()` wraps `SheetBody` (50 cells) in an `AnimatedBuilder` on `open`, but nothing in it reads `open.value`. Fix: remove the `AnimatedBuilder`.
- **15. The loading row rebuilds every frame.** In `lib/features/practice/widgets/inking_sheet.dart`, `BubbleRow` is rebuilt on every vsync for 10 state changes per 2.4 s. Fix: track `inked` in a `ValueNotifier` updated from a controller listener only when it changes, and use a `ValueListenableBuilder`.
- **16. Every pressable gets its own layer.** `lib/core/widgets/pressable.dart` wraps each surface in a `RepaintBoundary`: 50 layers in the palette, plus every settings row. Fix: make it opt-in (`isolate: true`).
- **17. Layout reads that rebuild too often.** `lib/features/today/screens/today_body.dart:88` and `lib/core/router/app_shell.dart:106` use `MediaQuery.of`. Fix: use `paddingOf` in `today_body`. In `AppShell`, build the copied `MediaQuery` with `MediaQuery.removeViewInsets` so keyboard insets don't change the branches' MediaQuery and rebuild Today on every keyboard frame.
- **18. The dock is not on its own layer.** Fix: wrap `SplitDock` in `AppShell` in a `RepaintBoundary`, so the lit tile's spring and the scroll drift don't redraw the shell's stack.
- **19. Mobi's line always uses `liveRegion: true`** (`lib/core/widgets/mobi.dart:187`), so TalkBack announces it every time a screen opens. Fix: make it live only when the line changes after a student action (for example the worry step).
- **20. Practice's "Show me" is announced as just "Show me"** (`lib/features/practice/widgets/suggestion_card.dart:150`). Fix: give it context, as Today's does: "Show me, the attempt behind this".
- **21. Review's `AnimatedSize`** (`chapter_group_card.dart`, `question_panel.dart`) animates layout inside a scrolling list, against the brief's rule that only transform and opacity animate. Fix: snap the size and fade the content.
- **22. Glass flips after the first frame.** `GlassQualitySetting` loads its saved value after the first frame, so a saved Lite or Off rebuilds the whole tree from Full. Fix: read the preference before `runApp` and pass it in as an override.
- **23. Leftover files.**
  - Old golden `failures/` folders (07:37–07:43, before the final passing run) are still in `test/golden/*/`. Delete them.
  - Unbundled Gabarito TTFs are still in `assets/fonts/`. Delete them.

## What already holds
- **Runner timer:** it is one `Text` inside its own `RepaintBoundary`, driven by a `ValueListenableBuilder`. The session engine does not notify every second, and the figures are tabular.
- **Reduced motion:** every `AnimationController` file checks `Motion.reduced`, and the implicit animations use `Motion.of`.
- **Result reveal:** it has an "Open results directly" TalkBack custom action and an immediate announcement.
- **Live blur:** only the dock, the Start button, the morph route and `MmSheet` use it, never scrolling content. The blur is clipped to its shape, and the dock's panes share one `BackdropGroup`.
- **Art budget:** 716 KB of art on disk, under the 3 MB budget.

## Not measured
- The Full blur cost and frame timing on the M06. This needs a profile APK (not debug), with glass forced to Full and the auto-downgrade off. Scroll Today, Practice and Review for 10 s each, open the quick-start sheet over Today, and record raster p90 in DevTools.

## Screenshot evidence after the round 1 fixes

The `r1-*` screenshots in `tmp/app-shots/pass2` were taken after the round 1 fixes, at commit `49f4100`. They replace the earlier pass 2 shots of the same screens, which no longer match the code.

- **Superseded:** pass 2 screenshots 23 to 27 (`23-demo-today` to `27-demo-today-insights`) are superseded by `r1-23-demo-today`, `r1-24-demo-today-scroll` and `r1-25-demo-today-road` (and the variants `r1-25b-demo-today-colleges`, `r1-25b-demo-today-compass-row` and `r1-26-demo-alternatives-length`). Use the `r1-*` files as evidence.

| Screenshot | Commit |
|---|---|
| `r1-01-welcome.png` | `49f4100` |
| `r1-03-onb-stage.png` | `49f4100` |
| `r1-05-onb-course.png` | `49f4100` |
| `r1-107-stream.png` | `49f4100` |
| `r1-110-rhythm.png` | `49f4100` |
| `r1-111-milestones.png` | `49f4100` |
| `r1-111b-milestones-repairs.png` | `49f4100` |
| `r1-23-demo-today.png` | `49f4100` |
| `r1-24-demo-today-scroll.png` | `49f4100` |
| `r1-25-demo-today-road.png` | `49f4100` |
| `r1-25b-demo-today-colleges.png` | `49f4100` |
| `r1-25b-demo-today-compass-row.png` | `49f4100` |
| `r1-26-demo-alternatives-length.png` | `49f4100` |
| `r1-28-demo-start-sheet.png` | `49f4100` |
| `r1-29-demo-practice.png` | `49f4100` |
| `r1-32-demo-quick-confirm-5.png` | `49f4100` |
| `r1-33-demo-runner-q1.png` | `49f4100` |
| `r1-35-demo-runner-last.png` | `49f4100` |
| `r1-36-demo-submit.png` | `49f4100` |
| `r1-37-demo-sending.png` | `49f4100` |
| `r1-38-demo-finish-0.png` | `49f4100` |
| `r1-38-demo-finish-typing.png` | `49f4100` |
| `r1-39-demo-finish-1.png` | `49f4100` |
| `r1-40-demo-finish.png` | `49f4100` |
| `r1-44-practice-modes.png` | `49f4100` |
| `r1-45-day-nta-instructions.png` | `49f4100` |
| `r1-45-nta-instructions-top.png` | `49f4100` |
| `r1-45b-nta-look-back.png` | `49f4100` |
| `r1-46-nta-instructions-mockmob-look.png` | `49f4100` |
| `r1-47-nta-instructions-end.png` | `49f4100` |
| `r1-48-nta-preparing.png` | `49f4100` |
| `r1-49-nta-q1.png` | `49f4100` |
| `r1-50-nta-q1-answered.png` | `49f4100` |
| `r1-52-nta-palette.png` | `49f4100` |
| `r1-57-nta-submit-summary.png` | `49f4100` |
| `r1-58-nta-sending.png` | `49f4100` |
| `r1-59-nta-after-submit.png` | `49f4100` |
| `r1-61-mock8-result.png` | `49f4100` |
| `r1-64-review.png` | `49f4100` |
| `r1-64b-review-chapters.png` | `49f4100` |
| `r1-65-review-past.png` | `49f4100` |
| `r1-66-record.png` | `49f4100` |
| `r1-67-record-2.png` | `49f4100` |
| `r1-68-saved.png` | `49f4100` |
| `r1-71-repair.png` | `49f4100` |
| `r1-71b-repair-question.png` | `49f4100` |
| `r1-73-repair-ending.png` | `49f4100` |
| `r1-74-you.png` | `49f4100` |
| `r1-81-edit-subjects.png` | `49f4100` |
| `r1-85-edit-subjects-sixth-refused.png` | `49f4100` |
| `r1-90-appearance-auto-lite.png` | `49f4100` |
| `r1-91-day-today.png` | `49f4100` |
| `r1-91-today-after-practice.png` | `49f4100` |
| `r1-92-review-after-repair.png` | `49f4100` |
| `r1-93-day-practice.png` | `49f4100` |
| `r1-94-day-review.png` | `49f4100` |
