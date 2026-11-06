# Brief: A2b app Today and the deck (model opus), launched 2026-10-18T20:31:10.477Z

You are owner A2b of the MockMob app (Flutter) for the 19 Oct fix: TODAY AND THE SUGGESTED DECK. First read C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\BRIEF-1019-COMMON.md completely (bases, tools, emulator lock, what to return); it is part of this brief. Branch ui/1019-a2b-today, folder wt-1019-a2b (from ab04b067).

THE RULES (verbatim from PLAN-1019 section 0; obey every one):
- **R1. Fresh-account first.** Every app and web check starts on a brand-new account (onboarding to Today to Practice to a paper to the result to Review to the Mob), then on the seeded heavy account. Both at 360 dp, plus 390 and 1440 for web, Night and Day.
- **R2. The 17-year-old test (G23).** For every screen, write one line: "What does a first-time student think this screen wants from them?" If the answer is not obvious in 3 seconds, it is a finding.
- **R3. Never hide to fix.** Removing or hiding any visible feature needs his explicit say-so. With billing off, Pro-only features are visible but locked (D101).
- **R4. Regression diff.** Before any release, screenshot the same screens on the previous release and the candidate, side by side. Any lost gradient, texture, motion or feature is a HIGH unless he asked for it.
- **R5. Motion is part of done.** Every result, accept and reveal animation is checked as a frame sequence on device (the emulator is fine), compared with the approved version's durations and curves.
- **R6. Copy in his voice (D84).** Persuasive, plain, grammatical English. No clipped fragments, no dropped articles, no telegram style. Read every new line aloud. If it would not appear in a good consumer app, rewrite it.
- **R7. One owner per surface.** Fewer, larger branches. Each has a single owner who knows the whole surface. The main session merges early, not at the end.
- **R8. Mock-up first** for anything that changes a layout (D107, D110, and his standing rule): 2-3 options as images, he picks, then the build.

YOUR ITEMS (SPEC and DONE WHEN verbatim from PLAN-1019 section 1):

**G7 Colleges on Today (D104).**
- SPEC:
  - Today shows the 3 hardest-to-reach picked colleges, labelled "Your top 3 of N".
  - A "See all N" row opens a sheet listing every picked college with the marks it needs and the gap.
  - Nothing silently disappears.
- DONE WHEN: with 5 colleges, Today shows 3 plus "See all 5", and the sheet lists 5.
(Order and numbers come from owner A2a's college ordering in my_colleges.dart, D103: read the hardest-to-reach by last year's closing marks; if A2a's sort is not in your base, sort locally by the existing cutoff data the model already exposes and leave a clear TODO-free seam. FORENSICS: MyColleges.ladderSize = 3, colleges_card.dart header "the first three of My colleges", colleges_copy.dart:14, 71.)

**G12 Suggested deck on a fresh account (R1).**
- SPEC: A fresh account with subjects always gets at least 4 real cards, built from the subjects it has (no history needed):
  1. A quick 10 in the subject the student rated weakest in onboarding.
  2. A full mock in their first domain subject.
  3. An English quick 10 (or their language).
  4. The Mob ("Sit the same paper as your friends").
  5. A 5th card, when there is room: another subject.
- Copy fixes:
  - Replace "You passed this one / it waits" and the bad "[go through them] again" line with true, plain English. For example, after a pass: "Moved to the back. You will see it again after the others." At the end: "You've seen all 4. Go through them again, or see every way to practise."
  - Remove the odd clock animation on the card, or make it a calm static icon.
- DONE WHEN: a fresh account's deck has at least 4 cards, every line is grammatical, and a test builds the deck from an empty history.
(FORENSICS: cards come from buildChoices in glance_builder.dart:108-150 with limit 4; repair, revise and weakest need papers; mock only if none in 14 days; other via otherSubjectFor move_builder.dart:846; end card copy_suggested.dart:23 and :82; the clock is SuggestedArt.stopwatch. Keep swipe v2 exactly as approved (D94: Up next / Not now, buttons under the deck, first-time demo, undo). Pro-only cards (Smart, NTA) are allowed only as visible-locked per D101, never hidden, never a price.)

**G13 The "Do this next" accept animation.**
- SPEC: Refine it: the accepted card lifts (scale 1.0 to 1.03, shadow up), travels to the lead slot with one spring (no overshoot over 4%, 350-450 ms), and the lead card settles. Reduced motion: a crossfade. Compare against the approved MOTION.md values.
- DONE WHEN: the frame sequence shows a single continuous move.

**G14 Today: KEEP** (he likes it). Do not restyle Today beyond your items.

FILE OWNERSHIP: you own lib/features/today/** (today_body.dart, colleges_card.dart on Today, the deck, glance_builder, move_builder choices, copy_suggested, the accept animation). Owner A5 adds ONE progress card ("I don't know my range") to Today from lib/features/tools/estimate/; if you see its insertion in your base later, keep it. A1 owns the bar, Practice and the Mob tab (and the Today Mob card's show-only-without-a-Mob condition in mob_entry.dart). A2a owns onboarding and the college ORDER in my_colleges.dart. A3 owns results and Review.

CHECKS before you return: flutter analyze clean; unit tests (deck from an empty history has at least 4 cards for 1, 3 and 5 subjects; top 3 of N with 2, 3, 5 and 8 colleges; the See all sheet lists all; deck copy); goldens for changed Today states (open old and new; 360 and 412; Night and Day; 1.3x). Then, holding the emulator lock, a FRESH staging account after onboarding: the deck (all cards, a pass, the end card), the accept animation as a FRAME SEQUENCE (screenrecord or rapid screencaps; open the frames; compare with the approved durations in MOTION.md or the motion tokens), Today with 5 colleges and the See all sheet; then a heavy account. R2 line per screen; R4 side-by-side against v15.2 (the walk shots in mockmob-next\tmp\app-walk-1018g or the v15.2 APK). Commit as you go. Return as the common brief says.
