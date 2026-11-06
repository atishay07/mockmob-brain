# Brief: A5 app range estimate (model opus), launched 2026-10-18T20:31:46.733Z

You are owner A5 of the MockMob app (Flutter) for the 19 Oct fix: "TYPE YOUR OWN RANGE" AND "I DON'T KNOW MY RANGE". First read C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\BRIEF-1019-COMMON.md completely (bases, tools, emulator lock, what to return); it is part of this brief. Branch ui/1019-a5-range, folder wt-1019-a5 (from ab04b067).

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

**G18 "Type your own range".**
- SPEC:
  - Fix the parser: accept any lo-hi within 0-1000 (for example 900-920, "900 to 920", "900–920").
  - Normalise: swap when lo > hi; reject a gap over 200 with a plain message.
  - The goal check and "Within your range" must read the same parsed value.
  - Find why 900-920 gives "0 of 4 clear" (likely the range compared against single cutoffs, or the parse falling back to 0).
- DONE WHEN: unit tests cover 900-920, 910-920, "900 to 920", 920-900 and a gap of 250, and the onboarding screen and Today agree.
(FORENSICS: estimate_sheet.dart has two numeric fields From and To (lines 534-535), _typed lines 187-192; the disagreement is the verdicts: estimate.dart:47-52 verdictFor says "clears" when the LOW end reaches the cutoff and "within" when only the HIGH end does; the headline counts only clears (estimate_sheet.dart:646-664, 692; colleges_copy.dart:108 "Your colleges: $n of $of clear") while rows show "Within your range" (estimate.dart:66). FIX (PLAN section 4): one rule: a college is "in reach" when the range's HIGH end clears it and "safe" when the LOW end does. The headline and the rows use the same words ("2 safe, 2 in reach of 4").)

**G19 + D109: "I don't know my range".**
- SPEC:
  - A choice "I don't know my range yet" on the range step and in You > Plan.
  - Until one full mock per subject of the student's set is scored (for example 5 subjects means 5 mocks), Today shows a progress card: "Sit one full mock in each subject and we'll estimate your range: English done, Accountancy done, Economics next."
  - After the last one, show the estimated range (the summed subject estimate ± its spread, on 1000 or the NTA scale used elsewhere) with the colleges it reaches; the student can accept it as their range or keep going.
  - The estimate is never presented as certain ("estimate from your 5 mocks").
- DONE WHEN: the flow works on a fresh account with fixtures, and the copy is honest.
(Build on EstimateSource.mocks, which already exists. The owner's words: "Your first direction is fine for estimating after 5 full mocks, but it should show 1 mock for each subject like that." The progress card's "Sit one" key starts that subject's full mock. Never claim precision the data does not have: show the spread.)

FILE OWNERSHIP: lib/features/tools/estimate/**, the range step's widget in onboarding ONLY for the "I don't know my range yet" choice (coordinate by keeping the change small; owner A2a owns the rest of onboarding), You > Plan's range row, and ONE insertion of your progress card into Today (today_body.dart is owned by A2b: add a single line that mounts your card widget from your folder; nothing else in Today).

CHECKS before you return: flutter analyze clean; unit tests for every parse case and both verdict words, the progress logic (1, 3 and 5 subjects; partial progress; done), the estimate copy; goldens (open old and new; 360 and 412; Night and Day; 1.3x). Then, holding the emulator lock, a FRESH staging account: choose "I don't know my range yet", see the Today progress card; type 900-920 and confirm the headline and rows agree; then a heavy account with mocks. R2 line per screen; R4 against v15.2. Commit as you go. Return as the common brief says.
