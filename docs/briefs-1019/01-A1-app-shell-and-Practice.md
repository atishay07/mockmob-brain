# Brief: A1 app shell and Practice (model opus), launched 2026-10-18T20:30:29.196Z

You are owner A1 of the MockMob app (Flutter) for the 19 Oct fix: APP SHELL AND PRACTICE. First read C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\BRIEF-1019-COMMON.md completely (bases, tools, emulator lock, what to return); it is part of this brief. Branch ui/1019-a1-shell, folder wt-1019-a1 (from ab04b067).

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

**G11 Today pill.**
- SPEC: The selected-tab pill in the bottom bar must be a perfect stadium (radius = height/2, equal insets on both sides, centred on its icon and label). Check at 360 and 412 dp and at 1.0, 1.3 and 1.6 text.
- DONE WHEN: a zoomed screenshot shows even ends.

**G15 Practice modes (D101).**
- SPEC:
  - Practice always lists every mode: Quick practice, Smart practice (the real name; there was never a "Smart mock", see FORENSICS), Full mock and NTA mode.
  - Pro-only modes stay visible with a quiet "Pro" tag. With PLAY_BILLING off, a tap opens a calm sheet: "NTA mode is part of Pro. Pro opens in the app soon." No price, no web link (anti-steering).
  - With PLAY_BILLING on, a tap opens the Upgrade sheet. A Pro student sees and uses them.
  - Revert the hiding from e3ca76be for these tiles.
- DONE WHEN: on a fresh Free account, Practice shows all the modes.

**G17 + D105: the Mob tab.**
- SPEC:
  - The app bar becomes Today, Practice, Start, Mob, You. Start stays the centre key.
  - Review moves inside Practice as "Your papers" (G20).
  - The Mob tab opens the Mob home: your Mob, this week's paper and the invite, or for a student with no Mob, a clear "Start a Mob / Join with a code" screen.
  - Remove the Mob row from You.
  - Keep the Today Mob card only while the student has no Mob.
- DONE WHEN: the bar shows the five, and the Mob is one tap away on a fresh account.

**G20 (structure only):** move Review inside Practice as "Your papers": the Practice tab gets a clear "Your papers" entry/section that opens the Review screen at its new route; every old route to Review (deep links, result "See this paper", notifications) still lands on it. Owner A3 rebuilds the CONTENT of that screen (D106: stats strip, subject filter, papers newest first, mistakes by chapter) in another branch: do NOT edit lib/features/review/** content or the result screens.

FORENSICS for you: e3ca76be (10-18 22:54) hid Smart and NTA tiles in practice_screen.dart:211-220 (showNta/showSmart with proOnSale), alternatives_sheet.dart, quick_start.dart, nta_instructions_screen.dart; take the tiles back from e3ca76be^ and show them locked (copy planGateTitle / ntaGatedPlain exists). The Mob page is /you/mob (mob_routes.dart:17; /mob redirects at router.dart:374); MobHubRow is you_hub_screen.dart:373; MobTodayBlock today_body.dart:807 (keep only while no Mob); mob_entry.dart.

FILE OWNERSHIP (to avoid merge conflicts): you own lib/core/widgets/bar/**, the router and route files for the tabs, lib/features/practice/screens/practice_screen.dart and the mode tiles/sheets, the Start sheet's mode list, alternatives_sheet.dart, quick_start.dart, nta_instructions_screen.dart, lib/features/you/** (the Mob row only), lib/features/social/** entry and the Mob tab home, mob_entry.dart. Other owners: A2a onboarding and colleges, A2b Today and the deck (today_body.dart is theirs except the one Mob-card condition, which you may change in mob_entry.dart), A3 result and Review content, A5 the range estimate.

CHECKS before you return: flutter analyze clean; unit tests for the five-tab bar, the pill geometry, every mode visible and locked/unlocked by plan and flag, the Mob tab empty state, route redirects; goldens for what you change (open old and new; 360 and 412, Night and Day, 1.3x). Then, holding the emulator lock, a FRESH staging account walk: the bar, the pill zoomed, Practice with all four modes and the locked sheet, the Mob tab, Practice > Your papers; then a quick heavy-account look. R2 line per screen; R4 side-by-side with v15.2 (install the v15.2 APK first to capture the before shots, or use the round walk screenshots in mockmob-next\tmp\app-walk-1018g). Commit as you go. Return as BRIEF-1019-COMMON.md says.
