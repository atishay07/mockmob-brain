# Brief: A2a onboarding and colleges (model opus), launched 2026-10-18T20:30:49.596Z

You are owner A2a of the MockMob app (Flutter) for the 19 Oct fix: ONBOARDING AND COLLEGES. First read C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\BRIEF-1019-COMMON.md completely (bases, tools, emulator lock, what to return); it is part of this brief. Branch ui/1019-a2a-onboard, folder wt-1019-a2a (from ab04b067).

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

**G1 First-open copy.**
- SPEC: Read the actual first-open Mobi line and sub-line in `lib/features/onboarding` (the welcome or intro screen). Rewrite both as full, grammatical, persuasive sentences.
  - Direction for the headline: "Find the marks you are losing. Win them back before CUET."
  - Direction for the sub-line: "MockMob finds where your marks slip, helps you fix each mistake, and checks the fix holds."
  - Keep his pattern (the Mobi speech).
- DONE WHEN: no fragment or telegram English appears on any onboarding screen. A copy test bans dropped articles in these strings (list them).

**G3 College search keyboard.**
- SPEC:
  - Reproduce on the emulator: type in the college search on the college step. Expected bug: the keyboard dismisses or the field scrolls under it.
  - Fix: a TextField with `scrollPadding`, the sheet resizing with `MediaQuery.viewInsets`, no rebuild that drops focus, and results filtering as you type.
- DONE WHEN: on the emulator at 360 dp, typing "hans" keeps the keyboard up and shows Hansraj. A widget test asserts the field keeps focus across rebuilds.

**G4 Course list order.**
- SPEC: Lead with the courses DU commerce aspirants target most: B.Com (Hons), BA (Hons) Economics, B.Com, BMS, BBA (FIA), then BA (Hons) Business Economics and the rest. Never label a course "top". Order by aspirant demand, not alphabetically.
- DONE WHEN: the list shows that order, and a test pins the order.

**G5 Multiple target courses.** DECISION: not now. (Nothing to build; make sure the course step and You > Plan say plainly that the course can be changed any time.)

**G6 College order (D103).**
- SPEC:
  - First, re-check the data source for last year's DU CSAS Round 1 closing marks per course and category (find it in data/ or lib/).
  - Order the picked colleges by those marks for the student's course and category.
  - Show the number beside each, for example "Hansraj · 912.5 last year".
  - If the data puts LSR above Hansraj for that course, say so with the numbers in the reply to him.
- DONE WHEN: the order matches the data, and every row shows its number.
(Note on G6: the owner believes SRCC, then Hindu, then Hansraj, then LSR for commerce. Report the real numbers per course/category that you find, with their source file and its provenance; never invent a number; if a college has no number for that course/category, say "no 2025 number" plainly and order it last. Use a plain separator in the row copy instead of a middle dot if the app's copy rules ban middle dots.)

**G9 Subject intelligence up front.**
- SPEC: On the subjects step, before any pick, show the course's rule as one line ("B.Com (Hons) needs a language, usually English, plus 3 subjects such as Accountancy, Business Studies and Economics or Maths") with the course's common sets as one-tap chips.
- KEEP the common sets and picks (he praised them).
- DONE WHEN: the line shows before the first pick.

KEEP: the first onboarding screen (G2), the common sets and picks, the D47 slider, the bigger base and its animation (G10). Never cut a step.

FILE OWNERSHIP: you own lib/features/onboarding/** and the college ordering in lib/core/models/my_colleges.dart and the colleges data it reads. Owner A2b owns Today (colleges_card.dart on Today shows "Your top 3 of N" and reads YOUR order: keep the model API stable, add a sort, do not change the card). A5 owns lib/features/tools/estimate/**. A1 owns the bar, Practice and the Mob tab.

CHECKS before you return: flutter analyze clean; unit and widget tests for each item (copy test, focus test, course order, college order with numbers, rule line before first pick); goldens for changed screens (open old and new; 360 and 412; Night and Day; 1.3x). Then, holding the emulator lock, a FRESH staging account through the whole onboarding at 360 dp (screenshots opened), including typing "hans" in the college search; R2 line per screen; R4 side-by-side against v15.2 (mockmob-next\tmp\apk\mockmob-v15.2-ab04b067.apk or the walk shots in mockmob-next\tmp\app-walk-1018g). Commit as you go. Return as the common brief says, including the college numbers you found for B.Com (Hons) general category (SRCC, Hindu, Hansraj, LSR, Kirori Mal, Ramjas and any others picked often).
