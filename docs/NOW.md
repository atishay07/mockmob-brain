# NOW: MockMob current state

**Before any UI work, read `UI-AUDIT-LOG.md` (this folder): what has already been looked at, what holds, what was fixed, what is open, and how to capture screens fast. Add your own findings to it. (Owner, 12 Nov 2026.)**

## 22 Nov 2026, about 6:30 am IST: hero walkthrough film v6 (LK368 task 2, the hero film side session). Files in wt-1110-convert, NOT committed, NOT live
- What: the hero film updated to today's product, 72.3 s (v5: 53 s), ten player chapters: Start 0 · Practise 10.567 · Mistake Lab 19.067 · Learn 26.233 · Key cards 30.783 · Ask Mobi 35.7 · Daily Five 43.617 · Benchmarks 49.917 · The Mob 54.117 · DU Compass 60.533 (the sign-up card plays inside the last). Every chapter is the real screen recorded from the dev server while the site's own demo cursor works it, in a window card with a camera that follows the cursor in; captions are the home page's own lines. Kept from v5: the open (night stage, college cards, wordmark, product set; the set's Key card, Ask Mobi and Learn screens now today's) and the end card (offer line fixed to "Pro ₹99 once, to 31 July 2027", data/capabilities.js CURRENT_OFFER; v5 said "a month").
- Voice: the owner's approved voice (Yash, eleven_v4, same settings) for the new lines; v5's approved open and close lines kept sample for sample. 1,920 ElevenLabs credits (logged in the film project's docs/ELEVENLABS-CREDITS.md). No Android app claim (the Play listing is not public).
- Sound: v5's approved bed and voice-first balance kept (voice 18 dB over the bed); a tactile tap on each real click, 19 dB or more under the voice; each chapter whoosh ends on its cut so a chapter jump starts clean; -16.1 LUFS, web -1.6 dBTP. Not checked by ear.
- Web tree (wt-1110-convert, uncommitted): public/video/hero-v6-{480,720,1080}.mp4 (4.72 / 8.29 / 13.40 MB; re-encoded 6:45 am with chapter 02 re-recorded from the rebuilt Lab), hero-v6-poster.webp (59 KB), hero-v6-poster-640.webp (18 KB); heroFilmConfig.mjs and HeroFilm.jsx point at v6; tests: data/tests/hero_film_r7.test.mjs (v6, v5 files kept), one line in data/tests/landing_checklist_1104.test.mjs (file-name pin made version-agnostic), src/components/landing/homeHero.test.mjs (ten segments). Hero tests 20/20, eslint clean, npm run -s test:app 1782 pass / 1 fail (coverage_public_1122, not the film) / 2 skipped. In-page check at 390 touch and 1440: plays v6, jump, pause, sound, no console errors, no shift.
- Rollback: the v5 files stay in public/video; restore the v5 FILM block in heroFilmConfig.mjs and PHONE_POSTER in HeroFilm.jsx (git).
- Film project (C:\Users\atish\Desktop\MockMob-promo-film, commit 1be0e89): master out/hero/hero-v6-master.mp4; plan, script and delivery notes docs/HERO-V6-PLAN.md; sheets out/hero/v6_sheet_*.png, v6_phone_*.png.

## 22 Nov 2026, about 6:10 am IST: Mistake Lab cards rebuilt (LK368, the Lab side session). Built and tested in wt-1110-convert, NOT committed, NOT live
His brief: keep the new stacked, self-playing look and its 7 s pace, but make the cards better by taking what the earlier screens did better; nothing cut on a phone.
- Each card now leads with ONE finding in the display face with one pen mark (the result page's own idiom), then ONE picture from the earlier screens at phone size, then the slot the cursor's tap fills. Chapters: "Partnership cost 18 of the 28 marks you missed.", bars cut into Q3 Q4 Q8, Fix first, -18, the three-mock columns. Time: "All 3 wrong answers ran over the 1:12 pace.", pace line, overrun hatched coral or amber. Changes: "= -6" counting up, each change as two picks and an arrow. Repair: the question, the pick struck, the key ticked, the record line, then the repair as a sheet. SWOT: the plan with Set up, four filled tiles.
- The line under each title follows the taps (LabBeats.mjs, one plain idea a beat, like Ask Mobi). On a phone the SWOT link shares that line's cell, which gave every device about 35 px back (part of his "cut on the bottom").
- Measured (Playwright, phone context): every card fits at full size at 360x640, 360x676, 390x844 and 1440x900, in light and dark; no text under 14 px (cards, card header, rail); nothing past the card; device 5 px each side, bottom at the band. Autoplay with CPU 6x: scenes hand off at about 7.0 to 7.9 s.
- Tests: lab_next_1121 11/11 (pins rewritten for the new cards, plus a new test for one finding, one pen mark and the beat lines), labStory + labTimePlays 15/15 (one stale pin from LK366 fixed), home_next_1120 24/24, landing_checklist_1104 43/43, test:app 1783 pass 0 fail; eslint clean.
- Not verified: a real phone. Design and sheets: wt-1110-convert/tmp/1122-lab/DESIGN.md (before: old-*, new-*; after: final-*).

## 21 Nov 2026, 3:05 pm IST: LIVE = main 459b9dd3d. THE NEW HOME IS LIVE ON / (owner: "Switch it live"); rollback = 467cd9540 (the old home on /)
- `/` = hero, colleges, Try five, one-place frame (6 rows, autoplay from its heading), Statement, Lab next look (plays itself), Daily and Sunday, Compass, pricing, creators (1,500+), FAQ (What do I get free?), close.
- /home-next 308 to /. Robots index/follow, canonical https://www.mockmob.in. Home tests moved to guard the new `/`; home-elements fixture recaptured.
- Live check (production, headless, 390x844 light, 360x676 dark, 1440x900 light): frame run starts at the heading; Lab plays 0 to 3 by itself; hero strip and deep links open the right rows; no sideways scroll; no errors.

## 21 Nov 2026, 1:42 pm IST: LIVE = main 467cd9540 (his LK364 notes); rollback = ca5c8f946
- The one-place frame starts when its heading reaches the top and plays all rows to the end. Cause of the misses: a swipe across a stage counted as a takeover; now only a real click or key does. 30 of 30 scroll trials start.
- Learn, Benchmarks and the Mob are rows 4-6 on the old deck's cards (TourScreens unchanged), with the deck's card slide between rows. Stages are 95% of a phone's width; the chips are one scrolling row.
- The Lab (next look) plays its five scenes by itself (useLabAutoplay.js, ScrollStory goTo) until a real touch, wheel or key. Two cursor taps a scene with eased reveals. The device is 94% of a phone's width.
- Out-of-suite tests that still fail and predate today: authored_w2 (13), du_teaser_r6 (1), marketing_theme_tokens_1104 (2), pricing_value_1105 (2). Not in any gate suite.

## 21 Nov 2026, 9:14 am IST: LIVE = main ca5c8f946 (the DU Compass tour waits while the page scrolls: phone Compass slow frames 9 to 1 on /home-next, 4 to 1 on /; the cause was the Lab still drawn one section above). Rollback = cf954f745

## 21 Nov 2026, 8:20 am IST: LIVE = main cf954f745 (/home-next, critic round 5 fixes); rollback = 216a21369. Morning report sent
- The phone exam pane stops on whole rows with a soft fade, the shorter phone rows are centred, and the frame and the Lab load in idle time after the opening. A Lab scene already on stage goes live as soon as its code arrives.
- Still open: on a phone, /home-next has more slow scroll frames per 1,000 px than `/` (about 3 against 1.9), mostly in the shared Compass section. lane-compass-jank is investigating, and will fix only if the fix is clean.
- Waiting for the owner: switching `/` to /home-next; showing the CUET 2026 coverage on the site; authoring the coverage gaps; his look at the phone Practise row, which is now the real phone exam (he liked the monitor picture in LK129; the monitor stays from 640 px); the hero film's green blocks seen on the emulator (check on his phone).

## 21 Nov 2026, 7:15 am IST: LIVE = main 216a21369 (/home-next after four critic rounds); rollback = 82cecc7a3, 3a7726dbe, 270b0a36a
- Critic scores (an independent Opus xhigh agent, using the live pages): /home-next 7.0, 8.0, 8.5, 8.7, then 9.0. The live `/` is 7.5 throughout.
- Phones: Practise plays the REAL phone exam inline: the MockMob runner, then NTA's phone screen. It is sized to the window with the key bar pinned. Every press is on screen at 390x844 down to 360x676 (Galaxy M06). Text is 16-19 px, and a swipe moves the page. Desktop keeps the monitor.
- The frame and the Lab load on approach (OnePlaceGate, LabNextGate), and only the shown stage is live. The bottom bar steps aside over the frame. The first-visit opening is quicker on /home-next, and the first visit's 709 ms reveal frame is gone.
- Speed versus `/` (critic, production, median of 3): worst scroll stall about half; the Chromebook blocks less (1.13 s against 1.48 s); layout shift lower. Still worse: slow frames per 1,000 px on a phone, 2.4 against 1.3, in sections both pages share. lane-hn-weight is moving the frame and Lab loading to idle time.
- 82cecc7a3 (the error page's sheets loaded lazily) made NO measurable change on live `/`: 664 KB of CSS before and after, because Turbopack chunks them differently. It is harmless, and its commit message overstates it.
- Running at 7:30 am: lane-oneplace (the pane's top edge on reveal, centring the phone rows) and lane-hn-weight (idle preload, Pricing's slow frames).

## 21 Nov 2026, 5:00 am IST: LIVE = main 270b0a36a (/home-next after two critic rounds; speed rounds 1 and 2; lighter film on weak phones); rollback = 807fdd35e, 2d2db4184
- The owner went to sleep at about 3 am with: "keep going until all the criteria have been satisfied and we have reached a level of everything which exceeds my expectations. I'll check everything in the morning."
- An independent critic (Opus xhigh) scored /home-next 7.0 against 7.5 for `/`. After the fixes it scored 8.0 against 7.5 (on the dev build). Round 3 on the live build is running.
- Frame: phone Practise zooms to the question (12 px or more), looks along the stem, and uses the palette chip for the next question. Touch takeover holds. Rows run 8 s or less, then one pass and rest. The proof lines are back (NTA exact copy, Key cards count, Bring a mistake credits). Tool chips never reach Log in. The desktop stage grows.
- Lab next look: pace label and key, the +6/-12/-6 totals, the full question, the SWOT heading, 0 layout shift, and 360x800 not trimmed.
- Speed: on `/`, 17 watched links instead of 79, and a touch scroll costs 7% less main-thread time. A GPU raster stall of 400-500 ms near scroll position 650 is not yet named.
- Hero film: a weak device (html[data-lite]) plays 480p (3.6 MB) instead of 720p (6.4 MB).
- Android emulator (mockmob_budget, real Chrome): /home-next opens every time, with no errors. Use -no-snapshot-load: its Quick Boot snapshot is corrupt. On the emulator it found heavier load than `/` (29 long tasks against 10), the bottom bar covering the demo, and green blocks in the film (probably the emulator's decoder: check on a real phone). lane-hn-weight is fixing the load, the bar, the flip, the preloads and the opening.
- `/` is unchanged apart from the speed fixes, which change nothing at rest. The switch to /home-next waits for his word.

## 21 Nov 2026, 1:30 am IST: LIVE = main 2d2db4184 (new /home-next on the live home; signed-in phone pass; 2026 coverage as data); rollback = e3d15ca10
- /home-next = the live home plus "Your whole CUET prep, in one place." (OnePlace.jsx: ExamStage, KeyCardsDemo, BringMistakeCard, each worked by `src/components/landing/demo/CursorDemo.jsx`), and the Lab with `look="next"` (LabNextScreens.jsx, lab-next.css). `/` is unchanged; its Lab is the default look.
- CUET 2026 coverage: `data/coverage/cuet2026/` (papers, ids, A and B checks, README). 100 of 149 covered. Not shown on any page; showing it waits for his word.
- Running: lane-speed (phone scroll and load on the home page); its uncommitted files are PipGuide, MobiReact, CollegeStrip, DesktopCursor, LoadingKit, TourDeck, PauseOffscreen, college-strip.css, r14-companion.css, home-sheets.css. They need a full gate before they ship.
- The local branch `wip/coverage-ui-1120` (the parked 2024 coverage section) must never be pushed.

## 20 Nov 2026, 11:55 pm IST: HIS VERDICT on /home-next (LK363): 6/10 against the live home's 8/10. LIVE = main e3d15ca10 (the real home is unchanged; /home-next is noindex). Building the next /home-next now
- **His verdict:** keep the live home as the base. Keep the idea of one frame for the whole prep, but each of its screens must be the product's ACTUAL screen, worked live by a cursor for 5 to 8 s (for example, the exam screen switching between MockMob and NTA style while questions are answered). The Lab goes back to the live Lab story, with its screens redone. No coverage section on the home page; the eventual goal is the CUET 2026 paper (LK362). Memories updated: web-restructure-rejected, final-redesign-pass.
- **In progress (two Opus lanes, dev server on port 3571):**
  - lane-oneplace: /home-next becomes the live page plus one section ("Your whole CUET prep, in one place."). It has three rows (Practise = the landing's real ExamScreen, Key cards = KeyCardsDemo, Ask Mobi = the BringMistakeBlock card), each worked by `src/components/landing/demo/CursorDemo.jsx`. The section replaces the tour deck, Key cards, Bring a mistake and the exam screen sections there.
  - lane-lab: LabCinema gets `look="next"`, with its five screens redone in the real result page's look and worked by the cursor. The default look stays as the live page has it. Review page: /preview/lab-next (dev only).
- **Coverage:** the CUET 2024 data is kept, not shown: `data/coverage/cuet-2024.json`, `scripts/coverage/merge-2024.mjs` (commit 725a08adc, not pushed). The coverage section built for the page is parked on the LOCAL branch `wip/coverage-ui-1120`; never push it. Figures: Business Studies 35 of 46, Economics 25 of 39, Accountancy 26 of 45; together 86 of 130.
- **Phone report:** he could not open /home-next on his phone. Not reproduced. In a slowed phone browser it loads in 2.4 s with no errors, and one scroll freeze of 745 ms was measured. The Android app's links only claim /today, /result, /review, /dashboard and /learn, so the app does not take over /home-next. What his phone showed is still unknown.

## 20 Nov 2026, 3:15 am IST: LIVE = main 46b3cc8b2 (speed pass, the snap on the key itself, Today levelled, Search by Shift twice, Ask Mobi as a bottom chat box); rollback chain = 6da135beb, 2e7430340. Nothing unpushed

- His feedback of about 2 am is in the ledger verbatim, LK352 to LK358. Standing: the speed yardstick is a cheap Chromebook or
  phone, measured with the processor slowed 6x (LK353); the landing is phone-first, desktop effort goes to the platform (LK358).
- Speed causes found and cured (tools in `wt-1110-convert/tmp/1120-speed/`: `chromebook.mjs`, `tracedesk.mjs`, `cpudesk.mjs`,
  `layers.mjs`; phone: `tmp/1119-phone/perf2.mjs`):
  - `HeroFilm.jsx` wrote `--p` on its whole chapters bar every animation frame while the film played (about 60 elements
    restyled 60 times a second at rest, on phones too). Now on the film's own time updates, on the one segment.
  - `PipGuide.jsx` (desktop) asked seats in undrawn sections for a box, for visibility and for animations: each lays the whole
    section out (a stall of about a second at 6x). Now judged from the section's own box (`farOff`).
  - `DesktopCursor.jsx`: four hit tests a frame became one about sixteen times a second; nothing read per frame.
  - `html[data-lite]` (inline script in `src/app/layout.js`; `mm:lite:v1` forces it): no blur, no pointer layer, no drift.
  - `AssetWarm.jsx`: lazy pictures fetched ahead in idle time. A blocking loading screen (LK354) was weighed and not built.
- Measured on live at 6x, before (2e7430340) and after: phone scroll 41.9 to 72.4 frames a second, frames over 50 ms 171 to
  41; first 6 s 22 to 43 frames a second; desktop pointer frames over 34 ms 22 of 218 to 0 of 434; desktop load blocked time
  2,452 to 1,753 ms (worst task 814 to 511 ms). Desktop scroll is NOT better (frames over 34 ms 199 of 756 to 185 of 783): the
  cost there is drawing each section the first time, still open.
- Signed-in: Today's greeting alone and columns level under one kind of heading (LK355); Search opens on Shift twice and is a
  glass bar with a top hit and Tab completion (LK356); Ask Mobi is a glass bar at the bottom right that opens a floating window
  and never narrows the page (LK357); the snap is the key's own outline (`data-snap`, LK352).
- NOT checked: Opera GX itself, a real Chromebook or phone, a real signed-in account on live (fixtures and a simulated
  session only), `html[data-lite]` on a real weak machine.
- Open: desktop scroll cost per section; old dock rules left in page CSS (harmless, can be deleted); the Ask Mobi window can
  sit over Practice's session card.

## 19 Nov 2026, 11:40 pm IST: LIVE = main 2e7430340 (his 10:15 pm feedback: home pointer, top bar and Mobi; Search and Ask Mobi; the streak line; signed-in pages on big screens); rollback chain = ea1bdfa68, ddecb3941. Nothing is waiting unpushed

- **His feedback of about 10:15 pm (a mouse, a 27 inch screen) is in the ledger verbatim, LK337 to LK351.** LK337 is a standing
  rule: a percent is counted from a written list (done and verified over asked), shown with the list; never a round figure.
- **Read `wt-1110-convert/tmp/1119-phone/STATE.md` (last section) first.** Two gated releases: 11:30 pm ea1bdfa68 (home page,
  the shell lane, the streak lane) and 11:40 pm 2e7430340 (the wide lane). Each: 24 suites fail 0, eslint empty, webpack and
  Turbopack builds 0.
- Home, mouse or trackpad only unless said:
  - LK338 Night's light is 420 px and about half as strong. LK339 the ring snaps onto a key from 12 px away and holds to 18 px
    (`.lp-snap`, `DesktopCursor.jsx`). LK340 on wide windows Mobi rides the head of the page's reading line and leans the way
    the page goes; a held story's rule stays plain (`NavReadLine.jsx`). LK341 tour screens say "Try it" beside the arrow.
  - LK342 a mark waits for a mouse reader (words above the lowest 38% of the window, page still for 130 ms); touch unchanged.
    The hero's price figure has its three flicks back (`accent="spark"`, that one figure only, pinned by a test).
  - LK343, a real fault: the desktop guide takes its stops from `[data-pip-station]` seats, and the Lab, the tour and Key
    cards had lost theirs, so he stood in one pose (the camera) for half the page and the Lab's own acts never played. Fixed
    with `WAYPOINTS` in `PipGuide.jsx` (a stop at the middle of a section, from the section's own box), eye boxes for the
    reading, camera and calendar poses (`mobiEyes.js`), a scroll look and a small lift with a resting mouse, and a lane that
    stays beside the page's column on very wide windows.
  - LK344 partly: the pricing backdrop word drifts behind its glass card. No other new scroll effect.
- Signed-in (seen only in the `/preview/arena` fixtures, plus a simulated session on live for the shell):
  - LK345 Search opens with Ctrl+Space on Windows and Linux (Ctrl+K and "/" still work, a Mac keeps Cmd+K); the first open
    says "One place to search everything." once. LK348 "/" stays on Learn and a plain letter typed on the page lands in Find.
  - LK350 Ask Mobi has a round key at the bottom right of a mouse window 1100 px or wider; from 1680 px its panel docks beside
    the page (`data-mobi-dock`, `--mobi-dock-w`), below that it covers. Hidden while the panel is open.
  - LK349 the streak is one volt highlighter line through the kept days (`StreakLine.jsx`), with "N questions answered in this
    streak", a pace line to the exam day (question counts, never marks), and one key that starts something the rule counts.
    Rules, numbers and routes unchanged. The top of Progress: the streak is a full-width first row, the weekly goal below.
  - LK346, LK347 pages are centred and their cap grows in steps to 1800 px at 2480; Today, Progress, Marks trend and You go to
    three columns from 1800; the Practice card's edge closes all round; Marks trend answers hover and focus.
- Verified on live after the first release: ring states (`reaim.mjs`), Mobi's stops and eyes down the page
  (`mobipause.mjs`), wheel walk 0 stuck 0 jumps, `sweep.mjs` at 1440 Day and Night 0 findings 0 errors, every site-bar link
  200, `authsim.mjs` passes, and `liveshell.mjs` (a simulated session, no real sign-in): the rail key reads Ctrl Space,
  Ctrl+Space opens Search with its first-use line, the Ask Mobi key is there and docks at 1920.
- NOT checked: a real mouse or trackpad, Safari, Firefox (no scroll-driven rider there: the fallback script draws it), a
  real phone, a real signed-in account on live (the streak, the wide layouts and Marks trend were seen in fixtures only),
  the result page's "Today counts" strip with a real just-finished set.
- Open, his to decide: more scroll effects on the home page (LK344 is only partly done); whether phones also get the
  subject rows' practice link on Marks trend; the pointer layer is still home-only.
- Housekeeping: a dev-only React key warning in `PlanValue` (old); `/preview/arena` is not on production, so signed-in
  screens cannot be looked at on live without a real sign-in.

## 19 Nov 2026, 8:31 pm IST: LIVE = main ddecb3941 (desktop: pointer layer, scroll depth, marks, sticky cards, Today at 1120 px, hover answers); rollback chain = 04ebba139, ce131e9b7, c22456209, 23432d0e7. Nothing is waiting unpushed. Waiting for HIS look with a real mouse

- **Read `wt-1110-convert/tmp/1119-phone/STATE.md` first** (the log of the day, the tools, what is next).
- Live for a mouse or trackpad only (nothing on touch, nothing with reduced motion): the ring closes to a volt dot and the
  action's name rides beside the arrow (Play or Pause on the film, Turn on the key card, Drag on the Compass slider, Watch on
  a reel, Open on a subject object); primary keys lean up to 7 px toward the arrow; the hero film and the exam monitor turn
  up to 4.5 degrees to face it; a faint light lies on the paper under it; the ring stretches along a scroll. Component
  `src/components/landing/DesktopCursor.jsx`; targets carry `data-cursor` and `data-tilt`.
- Desktop scroll depth: the picture of the Key cards, Ask Mobi and exam sections drifts 40 px against its words (CSS view
  timeline, no script). The wheel walk stays 0 stuck, 0 jumps.
- Marks at 1440: each photographed and measured (`tmp/1119-phone/marks.mjs`). Fixed: the statement's comma wrapped alone
  after the circled "where"; loops and the highlighter touched the next word. Every mark now measures 0 px into a neighbour.
- Checked in headless Chrome only (a scripted mouse). NOT checked with a real mouse, in Safari or Firefox (Firefox has no
  view timelines, so it gets no scroll depth; everything else works there in principle, unverified).
- Second batch, live 7:57 pm (main ce131e9b7): in Key cards and Ask Mobi the card is sticky in its column (from 1100 px wide
  and 780 px tall), so the blank paper under it is gone; signed-in Today takes 1120 px from 1360 px (it stopped at 960 and left
  about 210 px empty at 1440); the tour's and the exam screen's keys answer a hover; reel cards tilt.
- Measured on live after both: wheel walk 0 stuck, 0 jumps; every mark 0 px into a neighbour; a sweep of the page at 1440 in
  Day and Night found no console error, sideways overflow or clipped text (`tmp/1119-phone/sweep.mjs`); the pointer layer
  costs 1 frame over 20 ms in 600 while the mouse sweeps the hero (`ptrperf.mjs`).
- Third and fourth batches: 8:17 pm 04ebba139 (the torch goes out over films, photographs and screens; a looped word keeps
  room on phones too) and 8:31 pm ddecb3941 (the ring re-aims after the page scrolls under a resting mouse: it kept the state
  of what had scrolled away; a loop is 0.17 of the type size wider than its word, so it clears the word's own last letter).
  Verified on live at 8:35 pm: `reaim.mjs` correct, wheel 0 stuck 0 jumps, marks clear, sweep clean, 10 public pages 200.
- Decisions that are his: the torch (a faint light under the arrow) is a decorative glow, which his UI standards normally
  refuse; it is there because he asked for more on desktop, and one line removes it. The pointer layer is on the home page
  only; the other public pages have none yet (waiting for his look with a real mouse before spreading it).
- Still open on desktop: his own look with a real mouse; Safari and Firefox unchecked; the other signed-in pages at 1440.

## 19 Nov 2026, 5:08 pm IST: LIVE = main 23432d0e7 (desktop: wheel flows, circle mark, even gaps, cursor ring); rollback = ef915b1f9, then b941dc2dd, 64efe70d8. Nothing is waiting unpushed. The DESKTOP pass (LK333-LK336) has only begun

- 4:54 pm ef915b1f9 (the four widest desktop gaps 193-277 px brought to 142-157 px); 5:06 pm 23432d0e7 (`DesktopCursor.jsx`: a ring that trails a mouse pointer, opens over anything pressable, one ring out on a click; fine pointer only). Each passed the full gate. Live wheel walk at 1440: 0 stuck, 0 jumps.

- Today's releases: 3:18 pm e8a2d917d (phone pass LK317-LK328); 4:15 pm 64efe70d8 (the session store and the `> * + *` rules:
  the 0.6 s freeze after load is gone on live); 4:43 pm b941dc2dd (the mouse wheel scrolls the Mistake Lab and the tour
  natively: 0 stuck notches, 0 jumps, was 24 of 40 stuck; a step costs 0.62 beat on a mouse; circle marks clear the next word).
- His words at about 4:20 pm (ledger LK332-LK336): the pricing adds-up is what he likes; desktop "should be way more impressive
  than the mobile side, which it is not yet ... cursor animations, animating cursors, scrolls, and clicks"; desktop scroll
  "stuck or very jumpy"; treat phone and desktop as separate optimisations; marks overlap letters; too much white space on
  desktop; "keep going" until I call it perfect; stop only above 95% usage.
- NOT started for desktop: a cursor layer and click feedback (fine pointer only), a richer desktop hero and scroll effects, a
  check of every mark at 1440, the signed-in pages at 1440 (Today's two columns, the empty right side), the `:has()` cure on
  the signed-in site. Tools: `tmp/1119-phone/wheel.mjs`, `wheelsteps.mjs`, `gaps.mjs` (desktop), plus the phone ones.
- A rare flake, not ours: `billing_monthly_webhook.test.mjs` "payment.captured after subscription.charged ..." failed once in a
  gate (the test builds two entities from the clock a few ms apart); 29 solo runs pass, no billing code changed. For the CTO.

## 19 Nov 2026, 3:18 pm IST: the phone pass (LK317-LK328) is LIVE: main e8a2d917d (`dpl_APnzH2ATvD7jfccEWU1gJah5RdV1`); rollback = a5b4f08f8 (`dpl_Dp4t4tomaTauyWZopYA6CfYAmrEo`). A second smoothness fix is committed on `web/1118-prod` (f86083631), being measured: NOT gated, NOT live

- His words today (about 1:15 pm): GPT ran 10 to 15 minutes and stopped at its usage limit; "check how much it has done, what all
  is left, and go back to my first original prompt, achieving 100% completion and even beyond my expectations".
- **Read `wt-1110-convert/tmp/1119-phone/STATE.md` first**: what is done per ledger item, the measured frame numbers, the tools.
- Live since 3:18 pm (gate clean on e8a2d917d: every suite fail 0, eslint empty, webpack and Turbopack builds exit 0; 40 sitemap
  pages 200; no Vercel runtime errors): plain pen marks, slower and timed to reading position (LK317); the bottom story bar
  rides the scroll (LK318); the exam screen is the monitor again on phones, the phone runner only on "Try it full screen"
  (LK319); a first-visit "works best on a laptop or desktop" strip with a cross on phones (LK320); Daily Five without college
  names, "Five a day. Keep your streak." (LK321, switch `NEXT_PUBLIC_DAILY_COLLEGE_BOARD`); Compass plays one sweep by itself
  (LK322); the DU courses section is gone from home (LK323); pricing sits above Instagram (LK324); the usual-price sum opens
  from a key beside the figure (LK325); the opening is 1.75 s on a first visit and 1.1 s after (LK326); Practice is the
  version he preferred, c2f12abcd (LK328); You, Colleges and Marks trend lose blank space (LK327, part).
- **Frame numbers, lab phone profile (headless Chrome, 390x844, CPU x4), first six seconds of the home page:** before (main
  a5b4f08f8) 35 to 43 fps, worst frame 1.13 to 1.15 s; live now 76 to 78 fps, worst frame 0.62 to 0.65 s. Scrolling the whole
  page: frames over 25 ms 174 to 179 before, 77 to 108 now. Not checked on a physical phone or in Safari.
- **Found after the release, fixed in f86083631 (not live yet):**
  1. The session provider (`AuthProvider`, wraps every page) changed its context value from `loading` to `unauthenticated` right
     after load. A context change above Suspense boundaries that have not hydrated makes React hydrate ALL of them in one
     blocking task: 577 to 851 ms at CPU x4 on the live home page. The state now lives in a store (`useSyncExternalStore`); the
     context value never changes. `useAuth()` is unchanged for callers; `useAuthMaybe()` is the non-throwing form.
  2. Seven `> * + *` spacing rules in `marketing.css` (thirteen in all): a bare `*` left of a sibling combinator puts the rule in
     the browser's page-wide sibling set, so every element appended to `<body>` restyled the whole page (four times in the
     first three seconds, 118 to 176 ms each at CPU x4). Now `> :where(:not(:first-child))`. A test in `css_split.test.mjs`
     refuses both patterns.
- Earlier finding, live: **`:has()` with an attribute or pseudo-class inside, or a "no" answer on html/body, makes the browser
  rescan the page on every DOM change**. Fixed on the home page; the signed-in site still has many (`grep ':has(' src`).
- The session simulation `tmp/1119-phone/authsim.mjs` checks signed-out, signed-in and refused sessions with no real sign-in
  (a made-up cookie that never leaves the browser; `/api/auth/me` answered by the script). Run it after any change to the
  provider.
- Open, his to decide: the simpler Daily Five against the college version; the pricing card's own look ("can be better");
  Today's two columns at 1440; the items listed under "Owner decisions still open" in STATE.md.

## 18 Nov 2026, about 10:15 pm: HIS VERDICT on today's rebuild (LK317-LK330). Building here has STOPPED; the next session starts from `PROMPT-NEXT-SESSION-2026-11-18-B.md`

- **Read first:** ledger rows LK317 to LK330 (his words, verbatim, each with a reading) and `docs/PROMPT-NEXT-SESSION-2026-11-18-B.md`
  (the ten work items in order, the rollback commits to compare against, the rules).
- **In short, what he said:** the pencils and markers were "highly unprofessional" (removed, see below); the doodle marks stay but
  should be slower and better timed to the scroll; the first five seconds stutter and the site feels 40 to 50 fps, not 120; the
  bottom story progress bar is jumpy; the exam screen section and Practice read as regressions against their previous versions;
  he is unsure old or new is better for the pricing card and DU Compass; pricing goes above Instagram; the "usual way" figure
  needs its working beside it; DU Compass should autoplay then pause; "Which DU courses are open to you?" should go or be
  redone; Daily Five's college names worry him; he wants a first-visit "works best on desktop" note on phones; signed-in pages
  have blank space and "nothing really impressive".
- **Live:** main a5b4f08f8 since 10:22 pm (rollback = 0c9099f0e): the 9:42 pm release with the pencils, markers and sparks off
  everywhere (LK317, part), pinned by a test in `doodlePaths.test.mjs`. Gate on a5b4f08f8 clean (24 suites 0 failures, test:app 1,546,
  eslint clean, both builds 0). Live checks: the home page's HTML no longer carries a pen mark, 6 public pages 200, and the
  plain marks still draw at 390 on www with no pencil or spark element in the page.
- **Held on `web/1118-prod`, NOT live, NOT gated:** the rebuilt Colleges and Saved pages (merge 83fb1a8ed; the gate on it was
  stopped at eslint to gate the pencil removal first; its suites had passed, test:app 1,550) and the pencil removal as
  0a64a12a2 (the same patch as main's a5b4f08f8). Next session: `git merge main` into `web/1118-prod` first (the two pencil
  commits are the same change), look at Colleges and Saved against his blank-space remark, then gate. Known wart there: at
  360 px the four subject objects on Colleges wrap three and one.
- **Lesson (LK330, the session's own):** three rebuilds read to him as regressions and two as "not sure". Before replacing a
  section he has accepted, put old and new side by side (rollback commits: home sections 219551a16; Practice, Learn, You
  c2f12abcd) and keep the old where it wins.
- Not checked on anything today: a physical phone, Safari, any signed-in page on production.

## 18 Nov 2026, 9:42 pm: Features, About, the footer and the four guides are LIVE (main 0c9099f0e; rollback = 9c7b563f2, `dpl_RKhjzTB9jXmqihGZ3wJiTNW8p2tv`). One lane RUNNING from 9:50 pm (Colleges and Saved), not merged

- His words: LK316 ("keep going until you match the requirements of my first prompt").
- **LIVE (0c9099f0e), on top of the 9:12 pm release below:**
  - /features (lane pub-c): nine text cards became a catalogue in three groups (Practise, Fix what you missed, Free DU tools); six
    parts lead with the home tour's own product screen (Practice, mistake repair, Chapter review, Ask Mobi, DU cutoff calculator,
    Subject combination planner), three are compact rows with a desk object; long bodies keep their first sentence and fold the
    rest behind "More" on phones. Every word kept.
  - /about: the four principles are tiles; three lead with a live figure (15 CUET subjects, the bank's question count, 73 DU
    courses); unknown count shows no figure. The page refreshes at most hourly.
  - The footer folds on phones on every public page (was two screens of links; home was already folded).
  - The four guides (lane pub-d: /cuet-mock-test-free, /cuet-practice-tests-online, /cuet-previous-year-questions, /cuet-2027):
    a paper facts card (50 questions, 60 minutes, +5, -1, and the live bank line), "On this page" chips, numbered sections at a
    62-character measure, links as 56 px rows, a "Try five CUET questions" band after section 2, FAQ rows closed. No word of
    their text, headings or metadata changed; nothing is folded.
  - Main session: Progress's seven finished-week marks fit whole at 360 px; the Night highlight's turning copy is generated
    content (a heading holds its words once); the marker rides by transform (landing checklist L-040 had flagged a `left`
    keyframe: that test file is in no `test:*` script, so the gate does not run it; run
    `node --test data/tests/landing_checklist_1104.test.mjs` by hand before a gate).
  - Gate in `wt-1116-next` on 0c9099f0e: 24 suites 0 failures (test:app 1,545), eslint clean, webpack and Turbopack builds 0.
  - Live checks: the build answered on www at 9:42 pm; 16 public pages 200; /api/practice/quote 401 signed out; /features and
    /cuet-mock-test-free walked at 390 Day and /about at 390 Night on www (0 page errors); the whole home page walked at 360 on
    www (30 screens, 0 page errors); no Vercel runtime errors in the hour.
- **Decided by the lanes, his to overrule:** the guides' facts card is labelled "CUET UG 2026, every subject paper" (new words);
  "Your standing" has no screen on /features (the Benchmark screen shows a target score, not a rank); the DU calculator's part
  shows the Compass sample, whose line says "Your practice range".
- **Open, his to decide (unchanged):** Free per-chapter counts on Marks trend; two "day" rules side by side (Today, Progress);
  Pro's usage line inside the closed "Everything in Pro" on the home card on phones; "See everything in Pro" beside
  "Everything in Pro".
- **RUNNING:** `wt-1119-arena-c` (branch `web/1119-arena-c`, brief `wt-1110-convert/tmp/1118/briefs/arena-c.md`, Opus high): Colleges says its
  count once and draws each course's 2026 range as a bar; Saved as a shelf. Then: read its montages, merge, `npm run test:app` and
  the landing checklist, gate once, look, push.
- **Left from the first prompt:** signed-in Colleges and Saved (in the lane above); Mob, Result, Explore,
  Guide and /pricing were looked at and left; no generated art replaced the dropped 3D Mobi.
- Not checked: a physical phone, Safari, any signed-in page on production (fixtures only).
- Housekeeping: lane worktrees `wt-1118-*` and `wt-1119-*` are merged and can be removed (rmdir the `node_modules` junction first).

## 18 Nov 2026, late evening: Practice, Learn, You and the animated pen are LIVE, pushed 9:11 pm (main 9c7b563f2; rollback = c2f12abcd, `dpl_6ZZCxb7ANQr75M2CEZMwUZXy5iaz`). Two public-page lanes RUNNING, not merged

- His words: LK316 still (6:15 pm: "keep going until you match the requirements of my first prompt"); LK314 ("Doodles look good. Some
  can be more animated").
- **LIVE (9c7b563f2, Vercel `dpl_RKhjzTB9jXmqihGZ3wJiTNW8p2tv`):**
  - Practice (lane arena-b, reviewed by Opus xhigh, 2 fixes): the session is a "ticket" always in view. Desktop: the sticky card
    with the subject's desk object, the MODE as its heading (owner G26, restored by the main session after the lane had put the
    subject there; `startModel.test.mjs` caught it in the gate), then Subject, Questions, Time, Marking, Cost and the key
    "Start 10 questions in Accountancy". Phones: a bar pinned above the dock with the object, the subject, the time and the
    price, and the key "Start 10 questions". The bar never cuts its text at 360, 390 or 412 (`tmp/1118/tools/barfit.mjs`): the
    count is not said twice, the key drops its glyph under 430 px, the object shrinks under 400 and gives way under 380.
  - Learn's home: every chapter row shows its state (shape and word) with a thin bar; each part is a disclosure saying
    "n of m chapters started". You: the account card first (name, plan, credits, streak Mobi, subjects as desk objects), then
    the places as one list of 56 px rows with their live figures.
  - Doodles, more animated (main session): `Doodle` takes `pen` (a small volt pencil rides the stroke's head at a hand's pace
    and lifts away; a red pen on a mistake's mark; a marker on a highlight; with `followScroll` the reader's scroll moves it)
    and `accent="spark"` (three flicks after a circle). On: the hero's "One mock.", "five", the Lab's "a moment." (scroll),
    "wrong", "open to you?" (+ sparks), "unlimited mocks.", "first mock?"; sparks on the price hook's figure. Never loops;
    hidden under reduced motion and without CSS motion paths. Night: a highlighter's words now turn dark exactly where the
    swipe has reached (a clipped copy, `.dd__over`), not all at once.
  - Gate in `wt-1116-next` on 9c7b563f2: 24 suites 0 failures (test:app 1,537), eslint clean, webpack and Turbopack builds 0.
  - Live from 9:12 pm (the home page's HTML carried the pen marks on the fourth 10-second try after the push): 12 public pages 200; /api/practice/quote 401 signed out; the seven timed pen marks drew on www at 390 Day with the pencil at the stroke's head and all eight (with the scroll-held one) in Night, 0 page errors; no Vercel runtime errors in the hour. Signed-in pages (Practice, Learn, You) seen through fixtures only at 360, 390 and 1440, Day and Night.
- **Committed on `web/1118-prod`, NOT gated or live:** bdedd4781 (Progress at 360: seven finished-week marks fit whole).
- **RUNNING (Opus high, briefs in `wt-1110-convert/tmp/1118/briefs/`):** `wt-1119-pub-c` (`pub-c.md`: /features as a catalogue of
  the tour's real product screens, /about with the live figure behind each principle, the footer folded on phones on every
  public page) and `wt-1119-pub-d` (`pub-d.md`: the four long article pages made scannable, every word kept). Then: read their
  montages, merge, gate once with bdedd4781, look, push.
- **Open, his to decide (unchanged):** Free per-chapter counts on Marks trend; two "day" rules side by side (Today, Progress);
  Pro's usage line inside the closed "Everything in Pro" on the home card on phones; "See everything in Pro" beside
  "Everything in Pro".
- **Not done from the first prompt:** no generated art replaced the dropped 3D Mobi (nothing needed it yet); Mob, Explore, Saved,
  Result, Colleges, Guide and the pricing page were looked at tonight at 390 and left as they are (they read well; Colleges and
  Saved are the plainest).
- Not checked: a physical phone, Safari (the pen needs CSS motion paths: Safari 16+; older shows the mark without the pencil),
  any signed-in page on production (fixtures only).

## 18 Nov 2026, night: the section redesign is LIVE, about 7:42 pm (main c2f12abcd; rollback = 219551a16). One lane (Practice, Learn, You) RUNNING, not merged

- His words: LK316 (6:15 pm: "get this all done, keep going until you match the requirements of my first prompt").
- **LIVE (c2f12abcd), built by three Opus lanes to the main session's briefs (`wt-1110-convert/tmp/1118/briefs/R2-COMMON.md`,
  `home-a.md`, `home-b.md`, `arena-a.md`), each with before-and-after montages at 390:**
  - Home: the exam screen is a real readable question at phone scale (monitor kept on desktop); DU Compass is one card (score,
    slider, "n of m cleared" re-inking, a pen tick per cleared college; Compass Pro one line plus a disclosure); DU courses
    leads with the count and four quick-start keys (subject pickers behind a disclosure on phones); creators lead with the
    three counts and reel cards show the creator's figure; pricing is one card (price, six desk objects, picker, the comparison
    as one line, two disclosures) at 1,282 px on a 390 phone (was 2,442); FAQ rows 56 px, all closed; the closing card's Mobi
    160 px; the footer's link groups fold on phones (691 px, was 1,089). Home page at 390: 21,762 px (was 23,865).
  - Signed-in: Progress (streak Mobi, this week's bubbles, week marks, a four-figure record), Your standing (rank as the
    largest figure, one ladder with the student's row and the points gap), Your papers (one repair bar), Wallet (what the
    balance covers, as desk objects).
  - Reviews (Opus xhigh) before merge: arena-a 5 fixes (tied totals named a place nobody holds; own row could show another
    student's mocks; Wallet "covers" ignored set sizes; streak number shown twice; loading shift), home-b 3 fixes (disclosures
    unreachable without script on older Safari and Firefox; a resize closing an opened disclosure; a placeholder band) and its
    money words proved identical in 16 offer cases. home-a was reviewed by the main session from its montages only.
  - Gate in `wt-1116-next` on c2f12abcd: 24 suites 0 failures (test:app 1,525), eslint clean, webpack and Turbopack 442 pages.
    Live: 11 public pages 200; the whole page walked at 390 on www (28 screens, 0 page errors); nothing past the edge at 360;
    deck 0 errors; 31 marks drew in Night; no runtime errors in the hour.
- **RUNNING:** `wt-1119-arena-b` (brief `arena-b.md`): Practice as a ticket always in view, Learn's roadmap with chapter states,
  You as one identity card. Then: independent review (it touches Practice's start), merge, gate once, look, push.
- **Open, his to decide:** Progress shows the daily streak's Mobi beside study-day bubbles (two rules for "a day"; same question
  as Today's two week rows); Pro's included usage line sits inside the closed "Everything in Pro" on the home card on phones;
  Free per-chapter counts on Marks trend. At 360 the finished-weeks row on Progress scrolls sideways with the oldest half cut.
- Not checked: a physical phone, Safari, any signed-in page on production (fixtures only).

## 18 Nov 2026, evening: fourth batch LIVE about 6:27 pm (main 219551a16; rollback = 747d26f3e, `dpl_3tT838tk5xEQDuJnaFRLoMZFeo7W`). Round 2 redesign lanes RUNNING, not merged, not live

- His words: LK313-LK315 (2:55 pm: use the phone screen, larger mock-up screens, livelier doodles) and LK316 (6:15 pm: "get
  this all done, keep going until you match the requirements of my first prompt").
- **LIVE (219551a16):** the Codex session's work (7eb3388bc, 6ee99ef37, 04a5155fa), reviewed here in a browser: the tour's
  product screens fill the phone card (Practice screen 340 x 498 px at 390, fit 0.937, was 308 x 358 at 0.734); the Lab
  heading's pen follows the scroll; the Compass score and pricing total re-ink; small bars on Practice, Your papers, Wallet,
  Your standing. Plus one fix of mine: Learn showed "6 of 11 done" twice. The older sections still look almost as before.
  Gate in `wt-1116-next` on 219551a16: 24 suites 0 failures (test:app 1,508), eslint clean, webpack and Turbopack 442 pages.
  Live: 10 public pages 200; deck at 390 and 360 on www with 0 errors and no overflow; 20 marks drew; no runtime errors.
- **RUNNING (Opus high, briefs in `wt-1110-convert/tmp/1118/briefs/`: `R2-COMMON.md`, `home-a.md`, `home-b.md`, `arena-a.md`):**
  `wt-1119-home-a` (exam screen readable in place, DU Compass as one card, DU courses answer first), `wt-1119-home-b`
  (pricing in one card at half the height, creators, FAQ, close, footer), `wt-1119-arena-a` (Progress, Your standing as a
  ladder, Your papers summary, Wallet). Each must show a before-and-after montage at 390. Then: independent review for the
  money lane (home-b) and the data lane (arena-a), merge (union of `package.json` test:app and `HOME_SHEETS`), regenerate
  `home-sheets.css`, recapture `home-elements.json`, landing tests, full gate once, look, push.
- Still open after that: Practice, Learn, You; generated art; the two owner decisions (Free per-chapter counts on Marks trend;
  two week rows on Today).

## 18 Nov 2026, 12:45 to 2:45 pm IST: the premium rebuild. Three batches LIVE; live is main 747d26f3e (`dpl_3tT838tk5xEQDuJnaFRLoMZFeo7W`, about 2:43 pm; rollback `dpl_CxeSpRJtpzhppNL2KJPxX6RnwXR5` = fe0dfe8a7, before that `dpl_HxZKQinitYWbrxo6pxhnKK57AHyt` = 3ee7bca5e, `dpl_5x5GMJvvQhDD6rzvw5mEKUWaS9Yu` = 04004f2b2)

- **LIVE, third batch (747d26f3e, about 2:43 pm):** Marks trend as an analysis desk (Your chapters, Your pace for Pro, Where
  your marks go); the pen and the highlighter on 17 other public pages (placements in `src/lib/publicMarks.mjs`, rules in
  `tmp/1118/briefs/marks.md`); the pen's ink tone is the words' own colour. Gate on 747d26f3e: 24 suites 0 failures (test:app
  1,508), eslint clean, webpack and Turbopack 442 pages. Live: 12 public pages 200, `/api/analytics` 401 signed out, no
  runtime errors in the hour. Not looked at in a browser on production after this deploy.
- **Next session: `PROMPT-NEXT-SESSION-2026-11-18.md` (his 2:55 pm verdict LK313-LK315: use the phone screen, larger mock-up screens, livelier doodles).**
- **NOT DONE from his brief (told to him at 2:40 pm):** the older sections are not redesigned (home: exam screen, DU Compass,
  DU courses, creators, pricing, FAQ, footer; arena: Practice, Your papers, Learn, Wallet, You, Progress, Your standing); no
  3D or generated art in place of the dropped 3D Mobi; bars and icons beyond the streak; nobody has judged the "30 seconds".
  This is the next session's work. Nothing is running; all lane worktrees `wt-1118-*` are merged and can be removed (rmdir
  the node_modules junction first).
- His words whole: OWNER-MASTER-LEDGER LK302-LK312 (the 12:45 pm brief and his 2:05 pm note: tangible output, a doodle vibe on
  scroll, streak/bars/icons at Duolingo's level, notes in the brain, no subpar 3D, use the image generator instead). Why each
  thing is the way it is: `DESIGN-DECISIONS-2026-11-18.md`. What was looked at and the traps: UI-AUDIT-LOG section 2f.
- **LIVE, first batch (3ee7bca5e):** "More inside MockMob" is a deck the scroll deals on every pointer (`TourDeck.jsx`,
  `deckMotion.mjs`, `r18-tour-deck.css`; held by ScrollStory like the Lab). The pen and the highlighter
  (`src/components/doodle`: `Doodle`, `Marked`): "One mock." in the hero, the price figure, eleven section headings, the
  statement's three accent words. The sample card's verdicts are a pen tick and a red cross. Today's streak block: the logo's
  Mobi as the streak's mark (asleep or lit), the number, the week's seven bubbles, a bar for today's questions, one moment a day.
- **LIVE, second batch (fe0dfe8a7):**
  - Search (`src/components/search`, `src/lib/search`): Ctrl+K or `/` on desktop with a Search key in the rail; a Search field on
    You and in the Start sheet on phones; pages, start actions, every chapter (Enter opens Practice with it chosen), DU colleges
    and courses. Never opens on the test screen or over another sheet. Reviewed (Opus xhigh): 7 fixes. Open: a chapter of a
    subject the student has not picked opens Practice on its "not your subject" note; the row's Key cards and Learn links sit
    inside the listbox option (screen readers).
  - Test screen, MockMob style: keys (A-D or 1-4, arrows or N/P, M, X, ?), a `Keys` list on mouse devices, and a visible
    `Cross out` tool (kept through a reload in its own sessionStorage entry keyed by student and paper; never in the answer
    draft or the submit). NTA style has neither and keeps its old 1-4 and arrows. Reviewed (Opus xhigh): 3 fixes (keys dead
    while the list is open; cross-out marks kept per student; keys dead once a notice replaces the paper). Mine after review:
    no Keys list on an NTA-mode paper (full screen: Esc would count as a warning); the refusal line scrolls into view.
  - The pen inside three Lab screens, Mobi on the top-bar streak chip, a pen underline under the costliest chapter on the
    result page (names of 20 characters or fewer).
- Gates in `wt-1116-next`: on 3ee7bca5e and on fe0dfe8a7, each 24 suites 0 failures (test:app 1,405 then 1,477), eslint clean,
  webpack and Turbopack builds 442 pages each. Live after each deploy: `/` and nine public pages 200; `/api/analytics` and
  `/api/me/streak` 401 signed out; in headless Chrome at 390 Day on www the deck is held with five cards, real 380 px swipes
  move one card each, every mark draws (15, then 18), 0 page errors, nothing past the right edge; Vercel shows no runtime
  errors in the hour.
- Marks trend, detail (now live, see above): Marks trend as an analysis desk
  (`wt-1118-insight`, reviewed, 2 fixes): Your chapters (every chapter of the student's subjects as a tile with the product's
  own states and a detail panel), Your pace (Pro only), Where your marks go. Open and his: Free sees each chapter's
  right-of-answered count (Key cards treats that line as Pro); two figures can differ from Your papers' for the same chapter
  (different paper ranges); the page reads all of the student's answered rows on each visit.
- **Still building at 2:25 pm:** `wt-1118-marks` (the same pen marks on the other public pages, by the rules in
  `tmp/1118/briefs/marks.md`): 18 files changed, not committed, not reported.
- Next: when lane marks reports, look at its contact sheets, merge, run the full gate ONCE in `wt-1116-next` (tool background
  mode; check `Get-CimInstance Win32_Process` for `gate2.sh` first), push, live checks, update this section.
- Dropped: a hand-built real-time 3D Mobi (he saw the renders: "very bad"). Nothing from it shipped.
- Not checked on any batch: a physical phone, iPhone Safari, tablet widths, a screen reader, any signed-in flow on production
  (Search, the test screen and the streak block were seen only through the preview fixtures).
- His to do: delete the empty folders `C:\tmp\1118\mobi3d` (Blender wrote test renders there; a safety check stopped me removing them).

## 17 Nov 2026, 3:35 to 7:55 am IST: the B session — DONE: web live (main 04004f2b2), app version 22 built (Desktop/MockMob-build-22)

- Reviews done (Opus xhigh, one per lane) and merged into web/1117-prod (wt-1110-convert): daily d8cd51273 (7 fixes: Sunday
  board read in ordered 1,000-row pages, a refused college change never shown, shared phones, copy) plus mine 99ba4b013 (the
  day board's average shows from 10 players, to the nearest half: one more player can no longer give a score away); NTA
  6528d3dc6 (7 fixes: clock jump after the instructions page, a stalled second, unsaved choice cleared on every submit,
  reload after Start, accessibility) plus mine 6a11a06e1 ("Saved" / "Not saved yet" beside the question number, since the
  palette is folded away on phones); streak f4475c037 + c319a0c6d (the WIP kept; walk fixes found by a 20,000-history fuzz;
  pause-day practice; the top-bar chip now shows only from 640 px up: on phones the streak leads Today and You instead).
- Merged walk at 390 Day (37 real swipes, 0 page errors), tour deck by touch, opening frames (390 Day/Night, 1440 Day; LCP not
  delayed), companion 0 covering of 38 rests, shadow sweep 0 past-section at 360/390/1440 Day and 390 Night, no overflow at 360.
- **WEB LIVE about 4:12 am: main 65797fd17 (`dpl_4VGnGGjrHTSsAk8DX88jjjB4vEqT`; rollback `dpl_B6tTXUhhhHnV5s4fnisHLvfxAQMp`
  = 3511f1fb3).** Gate in wt-1116-next on af96050e8: 24 suites 0 failures, eslint clean, webpack and Turbopack builds 442 pages
  (the one later commit is CSS-only: pause days 44 px). Live checks: 12 public pages 200; /mentor signed out lands on
  /login?next=%2Fmentor (a redirect inside the page; curl sees 200); POST /api/ai/mentor/mistake, GET /api/me/streak, POST
  /api/me/streak/pause, GET /api/daily/me all 401 signed out; GET /api/daily/board 200, public, aggregate only; the opening on
  production frames (throttled phone: drawn at FCP 1.45 s, landed by 2.9 s, LCP not delayed); the deck by touch on production;
  no runtime errors.
- **Web hotfix LIVE 4:53 am: main 36e7f1050 (`dpl_7ugK8WDRJcrnStMetqgoBi35vFc3`)**: Ask Mobi's mistake ask never offers a
  fresh (chargeable) resend after a 5xx it cannot read; found by the app review. Suites run (recovery, learning, billing, app).
- App: ui/1117-final (wt-1117-app-final) = ask f193b3174 (review: 9 fixes incl. two double-charge paths) + daily 32b1644d4
  (with the college game) + nta b39197be5 (review: no answer-loss path; 2 fixes) + my 50cb21857 (away-banner copy) and the NTA
  strip fix; merged clean, whole-app analyze clean. Wave 2 merged: ui/1117-art eb8dd10de (the 3D Mobi stills, calendar on
  Daily Five and Sunday Mock, camera in the photo sheet, pointing on empty Colleges; +68 KB) and ui/1117-w2 da246cde6 (the one
  daily streak: Today, the sheet, You, the den; no top chip, it does not fit at 360 dp).
- **APP VERSION 22 BUILT (1.0.24+22), ui/1117-final 0a00993b6, local branch, not pushed.** Desktop/MockMob-build-22: signed AAB
  that sells (SHA-256 9ee587e9...), arm64 APK (173d6667...), symbols and mapping, README.txt, OWNER-STEPS.md (upload, release
  notes, the NEW Data safety step: Photos collected, not stored, not shared). Signer CN=MockMob 62:AC:58:08...EC:47 checked on both
  (keytool, apksigner); 16 KB alignment 10 libraries OK. Merged-branch tests: analyze clean; unit today/daily/social/you/
  insights/runner/mascot/core_ui/release 2,727 pass; golden social 575 pass after re-recording the den/sheet images for the
  streak's words (c228c3106, looked at); remaining golden failures are old drift that fails on 1.0.23 too: today_resume (2),
  tools (30: "last year" vs "2026 cutoff", date-dependent), explore_door (4), week_sheet (6). Emulator: the release build
  installed over 21 and opened; demo build: Today, Ask Mobi chat start, You, Practice, NTA mode end to end ("Not saved yet",
  Save & Next, "Saved"). Daily Five and the streak show their "did not load" states in the demo build (no stand-in server).
  Release worktree removed after deleting key.properties and prod.json (one empty locked folder wt-1117-app-releaselutter_app
  remains until a restart). Later commit 3c873193e: the release script's signer check no longer passes silently without keytool.
- **Web LIVE 7:28 am: main 04004f2b2 (`dpl_5x5GMJvvQhDD6rzvw5mEKUWaS9Yu`)**: the home daily block settles 1,600 px ahead, so a
  late board answer no longer moves the Sunday card (CLS 0.125 measured before, intermittent; 0.000/0.002/0.000 after).
- Open for later: the first swipe below the hero holds one long frame (~380 ms at 4x CPU, rendering, no script; not traced).
  Lane worktrees (wt-1117-*) are merged and can be removed (web ones: rmdir the node_modules junction first).
- Owner's open decisions unchanged: iOS app; an evening streak reminder; class leagues SQL; stale 6 Nov doc copies.

## 17 Nov 2026, about 3:25 am IST: STOPPED at the owner's usage limit; next session prompt is PROMPT-NEXT-SESSION-2026-11-17-B.md

Live is still main 3511f1fb3. Release branch web/1117-prod (wt-1110-convert) at 007f01059: six web lanes merged (tour deck,
opening, 3D Mobi, streak, NTA, daily college game) plus the calendar seat; 564 merged tests pass; not gated, not pushed.
Unfinished: reviews (daily, NTA; streak's review fix is WIP 28fa1045a on web/1117-streak, not merged), the gate and ship, both
app lanes (WIP 9769a2114 on ui/1117-ask and 26f90da01 on ui/1117-daily, untested), app wave 2, release 1.0.24+22. No Fable
agents (limit hit at 2:27 am). Everything is in the prompt file.

## 17 Nov 2026, from about 1:15 am IST: his third look (LK290-LK301) is being built (eight lanes; nothing new live yet)

- His words whole in OWNER-MASTER-LEDGER LK290-LK301. Research reports: `wt-1110-convert/tmp/1117/understand/<area>/FULL.md`.
- Web lanes (worktrees `wt-1117-<lane>`, branches `web/1117-<lane>` from 3511f1fb3; briefs `wt-1110-convert/tmp/1117/briefs/`):
  tour (phone tour as a tabbed card with a sideways swipe; soft shadows), opening ("Answer sheet rain" into the header logo),
  daily (Daily Five and Sunday Mock as a college game: "Playing for" a DU college, a private seat number, a board of colleges),
  art (the 3D Mobi on the home page with job poses), streak (the daily chain everywhere; the Daily Five counts), nta (exam-true
  saving, instructions page, submit summary, no counter). App lanes: `ui/1117-ask` (Ask Mobi chat with the photo key) and
  `ui/1117-daily` (Daily Five, Sunday Mock, weekend line, badges) from `ui/1112-final`.
- Then: merge, full gate, ship web; app wave 2 (art, streak, NTA, the daily team step); release 1.0.24+22 to
  Desktop/MockMob-build-22 after an emulator walk.

## 17 Nov 2026, about 1:05 am IST: his second phone verdict is LIVE (main 3511f1fb3, `dpl_B6tTXUhhhHnV5s4fnisHLvfxAQMp`; was 67146f994, rollback `dpl_6pnWZbgXceJvS9DKoqWgV8ymBUDM`)

The night's five lanes (tour, mistake, rhythm, price, chat) plus Mobi art, and this session's fixes. Ledger LK278-LK289 now say LIVE with outcomes (LK283 PART).
- Fixed this session: Ask Mobi's start at 390x844 (four tiles ended 4 px under the composer's fade; Mobi's box 64x82, gaps 12); landing test L-041 (the home page imported `bringMistake.mjs` and so its model prompt; prices moved to the prompt-free `src/services/mobi/mistakePrices.mjs`, the ban unchanged); the phone companion never covers words or controls (stands, shows his head, or steps aside at each rest; the hello only over a clear spot; 42-rest audit: live before 8 covering rests, live after 0); the DU calculator's head on the page's one left edge with Mobi at its right (was centred since 7 Nov; his 16 Nov phone rule wins); FLOW source pins follow the tour's free story; the home element fixture recaptured.
- Looked at, no change: section heads 60-70 px into a section are the brand stamp above them; the real gaps are even.
- Walk: the whole page at 390 Day with 38 real swipes; 390 Night, 360 Day, 1440 Day for the middle stretch; every new control tapped once by real touch. UI-AUDIT-LOG 2d and the section 3 note.
- Gate in `wt-1116-next` on 831dbde00: 24 suites 0 failures, lint clean, webpack and Turbopack 442 pages each; the last commit (a test pin) run on its own. Outside the gate's suites: 18 failing tests in `scripts/pipeline` and `authored_w2`, files unchanged since 67146f994 (old, not tonight's).
- Live: 12 public pages 200, `/mentor` signed out goes to `/login?next=%2Fmentor`, POST `/api/ai/mentor/mistake` 401 signed out, the new markup served, no runtime errors.
- NOT checked: a physical phone, iPhone Safari, a real phone keyboard over the chat's composer, any signed-in flow on production, a real model reply. The Android app's Ask screen still has the old layout and no photo key. The home page's Mobi (vector) got no new art or motion (LK283 part).
- Not mine to delete (permission declined): stale 6 Nov copies in `docs/_from-code-repo/mockmob-next/` (nothing in them to fold).

## 16 Nov 2026, night (10:25 pm to 11:58 pm IST): his second phone verdict; built and merged, NOT shipped (stopped at a usage limit)

Read `PROMPT-NEXT-SESSION-2026-11-17.md` (rewritten tonight): it is the whole state and the ordered list of what is left. Short form:
- His words: OWNER-MASTER-LEDGER LK278-LK289 (tour stack rejected, older held one preferred; mistake copy and the 5-of-10 card; the Daily and Sunday block too small; Mobi art; Ask Mobi "such bad UI", must be a real chat; no provider named; the refused-photo loophole; Free cap to Rs 3.50; Practice's Sunday line only on Saturday).
- LIVE is still main 67146f994. Release branch `web/1115-prod` (wt-1110-convert) is at f93e85149, local only: five lanes merged cleanly (tour, mistake, rhythm, price, chat) plus Mobi art. Not gated, not pushed.
- Done on production by the owner himself: `runtime_ai_budget.student_user_free` = 0.0398 (Rs 3.50), read back.
- Left: look at the chat follow-up screens (code done, unseen), fix test L-041, the merged home-page walk (never done; three known defects), the full gate, push, live checks, records.
- Sub-agent effort guide (his ask tonight): `AI OS/context/agent-model-routing.md`, top section; always pass effort.

## 16 Nov 2026, evening (from about 5:45 pm IST): the phone pass after his look at the live site

His words are whole in OWNER-MASTER-LEDGER.md (LK266-LK275): desktop looks good, the phone falls short; Daily Five and Sunday Mock too big and too high; "No. 2" means nothing; the bring-a-mistake block misplaced on phone and desktop, and does Ask Mobi really take a photo and what does it cost; the scrolling Mobi "needs to be interactive and overall fixed"; after the tour's Practice screen the page does "weird movements"; no pulsing dots, no walls of text, words lined up; "the codebase is yours ... don't ... keep asking me stuff".

- LIVE main 516bc9511 (about 7:35 pm, `dpl_9stbca5NZQSWBqam2qQbEzJBwKaQ`): the phone pass.
  - Daily Five and Sunday Mock: one section `#daily-and-sunday` after the exam screen, two short rows (`DailyFiveRow.jsx` HomeStrip, `dailyStripCopy.mjs`); 535 px at 390, from about 1,500 under the sample. The day's number is gone from the home page, Today's row and /daily; /daily's head says which papers the five come from.
  - Bring a mistake (`BringMistakeBlock.jsx`): one card walked through in three tabs (your question, Mobi's read on ink, a check), words on one left edge; 956 px at 390 from about 1,700. Price line built by `bringMistakeWords` from the app's numbers.
  - The tour (`web/1116-tour`): held only for `(hover: hover) and (pointer: fine)`; on touch a plain stack of the five tools (`r16-tour-stack.css`), and every screen answers a tap (`tourTaps.mjs`): Practice picks, Learn checks, Ask Mobi's two replies, Benchmarks' three targets, the Mob's Fix it together with the home sample's own Economics question. The timed carousel, the pulsing dot and the fake finger ripple are deleted.
  - Mobi the scroll companion (`MobiCompanion.jsx`, `companionModel.mjs`): only on the bottom bar, no lean, stretch or hop; a tap opens Ask Mobi with a question for the section in view (`SECTION_ASKS`). Mobi's seats arrive with a 260 ms fade on phones, not an 880 ms hop (`r16-phone.css`).
  - Compass: the score rests at 900 on touch (no self-running sweep); on touch a slider's track no longer takes a finger, only its knob (the Compass score once jumped to 236 under a scrolling thumb; same guard on the pricing pace); the head starts on the page's left edge on phones. Key cards: six subject chips and "and 8 more" on phones.
  - /sunday-mock "How a Sunday goes": the paper as three figures and the day as a five-step timeline, from the rule's constants (`sundayHow.mjs`).
  - Gate: in `wt-1116-next` (real Next 16.3.8 packages): 24 suites all pass, lint clean, webpack build and Turbopack build 442 pages each. On www after the deploy: 10 public pages 200, the new words served, the page walked at 390 (31 screens, 23,223 px), the slider guard tested with real touches, no runtime errors in the hour.
  - Not checked: a physical phone, iPhone Safari, a screen reader, Night at 768 and 1440 for the tour, landscape.
- LIVE main 67146f994 (about 7:55 pm, `dpl_6pnWZbgXceJvS9DKoqWgV8ymBUDM`): Ask Mobi reads a PHOTO of a question (`web/1116-photo`, his question: "uploading pictures of any other paper ... how many credits it would cost, pricing it properly").
  - What it is: in bring a mistake, "Add a photo of the question" (camera or gallery). The browser shrinks it to at most 1,600 px and 900 KB before sending; the server takes one JPEG of at most 1 MB, never stores or logs it, and saves only Mobi's reading ("Mobi read this from your photo", shown back so a misreading is seen at once). A typed ask is unchanged.
  - Price: typed 1 credit, photo 2 (`MISTAKE_PHOTO_CREDITS`), one reserve then commit or release. Worked out from the guard's price row: a photo ask costs 1.2 to 1.45 typed asks (worst case USD 0.00266 against 0.00219; expected about Rs 0.11 against Rs 0.08).
  - The tie into MockMob: Mobi names the chapter from MockMob's own list (kept only when the syllabus list AND the live list Practice reads both have it), and the next step is "Practise 10 <chapter> questions" on the existing Quick route.
  - One switch: `data/mistake_photo.mjs` `MISTAKE_PHOTO_ON` (true). Off: no photo key, the server refuses a photo, and the home page's block stops promising one (it reads the same switch and both prices).
  - Independent review, two passes: merge. No schema change. Privacy page gained the photo sentence (dated 16 November 2026); the line under the key reads "Your photo is sent to OpenAI to be read. MockMob does not save it. Leave your name and roll number out of the frame."
  - Gate: 24 suites, lint, webpack and Turbopack builds in `wt-1116-next`.
  - NOT PROVEN: no real model has read a photo (agents may not make paid calls or sign in). His to try once from his own account. Then read the newest row of `runtime_ai_requests` for mode `mistake`: its `usage.prompt_tokens` against the reservation. The reservation sizes the image at 2.5 x its 32 px patches (OpenAI documents 1.2 for the family, 2.46 at most; GPT-6 Luna has no row). If one call ever costs more than its reservation, `receipt_runtime_ai` PAUSES ALL STUDENT AI: a photo would need more than about 3.8 x to do that.
  - His pricing call: at expected costs a Free month's Rs 2.50 AI cap ends after about 31 typed or 22 photo asks, before the 50 credits are spent. Options: leave it; raise the Free cap; or price a typed ask at 2 credits and a photo at 3.
  - Known and left: a refused photo (unreadable, not a study question) is free in credits but its model call still counts against the student's monthly AI cap; the mobile app has no photo key yet; HEIC from some Android phones cannot be opened in Chrome (the panel says to take the photo again or type it).
- Rollback: `dpl_9stbca5NZQSWBqam2qQbEzJBwKaQ` (516bc9511, before photos), `dpl_CPWFfAdtzHHDNAwDMpQ2maVoCBQF` (79672593c, before the phone pass). Photos alone can also be turned off with the switch.
- Lessons: an element screenshot of a tall section comes out blank (content-visibility); walk it by viewport (`tmp/1116-final/walk.mjs`). A synthetic swipe that starts on a range input sets it: that is how the slider fault was found. The shared `node_modules` junction has eslint-config-next 16.2.4, so `npx eslint src` there shows five "rule not found" errors: lint and gate in `wt-1116-next`. `node --use-system-ca` breaks a Turbopack build's workers: run `npx next build`. After a page gains or loses markup, recapture `data/tests/fixtures/home-elements.json` (`scripts/capture-home-elements.mjs`) or the cascade test reads the old tree.

## 16 Nov 2026, from about 10:20 am IST — the pass continues (his words: "No need to stop for handover ... only stop when you think everything has been finalized")

- LIVE main 05510626d (about 11:10 am): "bring a mistake" on the home page after Key cards (`src/components/landing/BringMistakeBlock.jsx`, `bringMistakeCopy.mjs` with a test that works out the example's keys): a pasted question on a paper slip, Mobi's read on ink, one check answerable in place, three chips, one key to `/signup?next=/mentor`. Checked: real pointer at 360, 390 Day and Night, 1440; layout shift 0; app, billing, keycards-ui, du, dock suites, lint, build; live sections compared (only the new section added, 1,056 px at 390); no runtime errors. Same release: the remaining spinners and the two skeleton shimmers made one pattern (`web/1116-spin`, CSS only; none of the nine spinners could be seen in a browser, no fixture shows them).
- LIVE main f5f6774c5 (about 11:35 am): the Sunday Mock's public page wears the day band with a clock to next Sunday; a five finished signed out is carried to the account on the first signed-in visit and the result's door says so (`/signup?next=/daily`); the corrections log at `/corrections` (12 entries proven from the repository's records), UNLISTED until he reads it: `data/corrections_listed.mjs` (no footer, About or sitemap link, `noindex`; checked on www).
- LIVE main d40a6160b then b42dd5bb4 (about 12:35 pm): the first minute after sign-up (`web/1116-first`): a new account keeps the page it signed up for through onboarding (allowlist of app pages in `firstRunDestination`, one hour, re-checked on every read), the last onboarding key names it, an arrival line shows once; three sign-in links keep their page. Independent review: redirect logic sound, fixes applied. Then the race cases (`web/1116-race2`): a free durable start hands its free row to `start_learning_session`; optional guarded migration `20261116130000` UNAPPLIED. Reviewed: no change while the switch is off.
- LIVE main a6ab71edc (about 1:10 pm): Mob class leagues (`web/1116-league`) behind `CLASS_LEAGUES_ENABLED`, OFF: with it off nothing mounts, fetches or renders and `/api/class` answers 404 (checked on www). Migration `20261116150000_class_leagues.sql` and its undo UNAPPLIED. Independent review found seven things; all fixed (the switch-off leak, account deletion steps, a stored weekly figure, the name screen, persistent limits, the member cap, own marks). To turn on: apply the SQL, set `CLASS_LEAGUES_ENABLED=true`, redeploy.
- LIVE main 79672593c (about 1:50 pm, `dpl_CPWFfAdtzHHDNAwDMpQ2maVoCBQF`): Next.js 16.3.8 with chart.js and react-chartjs-2 removed (`web/1116-next`). Gated in `wt-1116-next`, which holds the real 16.3.8 packages: 24 suites, lint, a webpack build and a Turbopack build (442 pages). On www: the page reports Next 16.3.8, every home section equal to before at 390, 11 public pages 200, the security headers present, no console or runtime errors. The release worktree's `node_modules` junction still has 16.2.4: gate Next-sensitive work in `wt-1116-next` (check out the commit there) until the shared packages are reinstalled.
- THE LIST IS DONE. Nothing is running. What is left is his: the decisions below, the unapplied SQL (class leagues `20261116150000`; the race functions `20261116120000` and `20261116130000` for the CTO; the two late-paper migrations; the email migration), and a look on his phone.
- His to decide: list the corrections log publicly; class leagues on or off, and the floor (three throwaway accounts with blank papers plus one real student reach five sitters: the average then gives that student's marks away); the About page says "report it and we recheck it" while a question leaves practice after three reports; one Accountancy question (id 40d8ffd9...) likely has a wrong key and 384 disputed questions are kept out of NTA papers only (content track, not verified here).
- A brand-new student signing up from a `/class/<code>` link lands on Today with a one-tap Join, not on the class page (a two-statement addition to `firstRunDestination` would fix it; not made).
- The PC (his ask, 11:25 am): terminals flashing fixed at the source (six background spawn sites used DETACHED_PROCESS; now CREATE_NO_WINDOW; backups `*.bak-nowindow-20261116`; 12 visible windows before, 0 after in a test; running services keep the old flags until a sign-out). Disk 17.8 GB to 35 GB free (pip cache, old temp, old `.next*` folders). Waiting on him: `mockmob-next\tmp` (13 GB) and Claude session logs older than 14 days (16 GB).
- Lessons: read every line of the gate before pushing (I pushed f5f6774c5 with one Mob test failed; it passed on a rerun, a timeout under load); a shell here-document eats backslashes (it broke two test files; use the editor); source-pin tests must read past CRLF.

## 16 Nov 2026, about 2:05 am IST — first paint, the Daily Five as a calendar page, the week's two pages, a route bar and lighter loading, public Key card decks, bring a mistake: LIVE (main 329e257ba by 4:20 am)

- His words this sitting (16 Nov, about 1 am): the first Daily Five redesign (a thin ticket row) was "still not up to the mark"; he showed Prepium's weekly cards, said not to copy them, "think in a unique brand identity direction", "this space is a bit low", "not always taking the safest approach", "a highly converting website is very important", every feature thought through for how it is presented, how it works and its whole flow, and "make sure that it's very clearly depicted: what it is exactly and how we do it every time". He approved the second version ("Yes, that's what I want"). Ledger LK248-LK255.
- LIVE, each checked on www: first paint (acc95ac67; `/` identical to the baseline at 390 and 1440, 21 sheets from 28); the Daily Five block on the home page as a tear-off calendar page (date large on ink, a real clock to 12:00 am IST, chips that say how it runs, the board, a full-width volt key) and under it the Sunday Mock page with a clock to next Sunday 10:00 am; `/daily` rebuilt (ink day band joined to the card, board, run of seven days, result with the board arriving tile by tile, share, three run numbers); a 2 px route bar on every page and a reading line on the home bar; the opening 700 ms a session (was 1,280) and 1,200 ms on a first visit (was 1,600), the mark about half the size; the signed-in shell, Log in and Sign up waits redrawn; public Key card decks at `/key-cards` (183 chapters, 911 cards, 14 subjects, the Free taste of 5 a chapter, built static); "bring a mistake" in Ask Mobi (1 credit, inside the same credit and runtime budget reservations, independent review: no blocker, three fixes applied).
- About 2:55 am: badges LIVE (main 91f8f8aaf, `dpl_7ckikYsAgs2nrBvbeoTBaKVj5rRQ`): the 16 badges redrawn as one family of stamped marks (a shape for each path; earned, next with its count, not yet), the earning moment inside the result page and Today, a share picture, the collection in four rows. Full gate passed; live pages 200, `/api/me/badges` 401 signed out, no runtime errors. His to read: the new "what it needs" lines and the moment's words. Known: a repair badge can reach Today up to 5 minutes late (no `forgetBadges` after a repair; server code, not changed).
- About 3:20 am: the desktop lane LIVE (main e137d3575, `dpl_spJ7iRVRQnF6zMgpVd8MmVSXPfsK`): the result, Progress and the Wallet in two columns from 1100 px (the score, the marks lost and the one volt key stay in view on the left; the left column is sticky through `src/lib/stickySide.mjs`); phones and tablets unchanged (the lane compared layouts element by element at 390, 768, 1024, 1099); three reading widths from the tablet walk (Practice, Mob settings, Account). Full gate passed; merged result, Progress and Wallet captured at 1440 and the result at 390 with badges in; live pages 200, no runtime errors. Known minor: between about 1100 and 1180 px "/ 250 marks" drops under the score. Left from the tablet walk: `marks-ledger.css:127` (82 characters a line) and the 32 px marks bar segments (`marks-ledger.css:207`).
- About 3:45 am: LIVE main aecaf31c5: the home Key cards section has a "pick your subject" row, 14 links into `/key-cards` (app, keycards and dock suites, lint, build; the links and their anchors checked on www; no runtime errors).
- Handoff and the next prompt: `HANDOFF-2026-11-16.md`, `PROMPT-NEXT-SESSION-2026-11-17.md`. About 4:20 am: LIVE main 329e257ba (`dpl_236uTaRypn1V8DjtJYG2E7C4V9ak`): the free first Full mock's release race closed for durable sessions (`release_unstarted_allowance`, migration `20261116120000` and its undo, both UNAPPLIED, for the CTO; a fallback while the function is absent). Independent review: nothing blocking, no change while `LEARNING_SESSIONS_ENABLED` is off; two narrow cases stay open, written with lines and fixes in `wt-1110-convert/tmp/1116-race/CTO-NOTE.md`. Full gate (billing 554), live pages 200, no runtime errors. No lane is running. Not started: Mob class leagues, a public corrections log, the durable-sessions release race SQL for the CTO, Next 16.3.8 with chart.js removed.
- Checked: full gate on 001d211e6 and on 844e608fe (24 suites, lint, build 256+ pages); the Daily Five walked in headless Chrome with real pointer clicks at 360, 390 and 1440, Day and Night (start, five answers, result, the home block open and played, layout shift 0); live `/`, `/daily`, `/key-cards`, a chapter, a 404, `/login`, `/signup`, `/pricing`, `/cuet/accountancy`, `/sunday-mock` 200 or 404 as they should; the mistake route 401 signed out; no runtime errors.
- Not checked: a physical phone, iPhone Safari, any signed-in flow on production (bring a mistake has never made a real model call), a real Sunday sitting (first on 22 Nov), the route bar on production under a slow network.
- His to decide or do: the distress pre-check also fires on real exam text about suicide pasted into "bring a mistake" (a Durkheim question gets the support reply; kept as built, his rule); `/login` and `/signup` show a wait screen to signed-out visitors first (changing that is sign-in behaviour); apply the two late-paper migrations; the email migration, consent line and privacy page before `EMAILS_ENABLED=true`; the older list in `HANDOFF-2026-11-15-PRODUCTION-PASS.md`.

## 16 Nov 2026, about 12:15 am IST — more of the pass LIVE (main 6858ccef5): payment fixes, Sunday draw and small UI, late papers; first paint ready, not shipped

- LIVE and checked: 8817b82d6 (payments), fbdf9912b (Sunday draw, small UI), 6858ccef5 (late papers, durable start race). His next brief (Daily Five on the landing and its flow, a top progress bar, lighter loading) and the first-paint ship steps: `HANDOFF-2026-11-15-NIGHT.md`, last two sections.
- He tested "ask a parent to pay" for real: paid, Pro activated.

## 15 Nov 2026, about 10:50 pm IST — production pass, second half: Daily Five habit, Sunday Mock, DU cutoff pages LIVE (main 79ff0d94e; was 6472026f0)

- His brief (about 7:15 pm): build, not audit; decide small things; push live; keep one list of what waits on him.
- LIVE: small fixes (a3bad4078), the DU data check and 136 cutoff pages (12516f20f), the Daily Five as a habit, the Sunday Mock (first on 22 Nov), the welcome and day-2 emails built and OFF (79ff0d94e). Each release: suites, lint, build, an independent Opus review for money, sign-in or runner code, a merged visual check, and live checks.
- Built, NOT live: first paint (held: joined home sheet changed the cascade in the webpack build; Turbopack order unverified) and late upload plus the durable start race (held: a late paper must earn no badges, study day, chain or Mob hours first). Exact steps: `HANDOFF-2026-11-15-NIGHT.md`.
- His to do: the email migration, consent line and privacy page before `EMAILS_ENABLED=true`; the earlier list in `HANDOFF-2026-11-15-PRODUCTION-PASS.md` still stands.

## 15 Nov 2026, about 5:55 pm IST — production pass before marketing: the security release is LIVE (main e6b041acf, dpl_8hgVk5zUo8EqbVhSuP7xvnWQeX3k; was 38a09a4e7, rollback dpl_HVKC1RyErDXQVvTH5xS8BnewnNjb); the rest of the pass is built and gated, not deployed

- His brief (15 Nov, about 11:45 am): the final pass before marketing: features, flows, sign-in options, bugs, security, anything else for a 10/10 product; content is a separate track; orchestrate Opus and Sonnet agents. Plan, findings, his decisions and the owner-only list: `PRODUCTION-PASS-2026-11-15.md`. Refund runbook: `RUNBOOK-REFUNDS-2026-11-15.md`.
- LIVE now (security, shipped alone under his 12 Oct standing order): the question feed needs sign-in and keeps held questions' answers out (it gave the whole bank with answers to anyone); no Pro for ever by replaying an old payment check; account deletion cancels the website subscription; one checkout, one subscription; refunds end access; removed Mob members stay out and Mob reports email support; a fixed reply with Tele-MANAS 14416 and 112 for a student in distress, before any model call; sign-in email limits that hold across servers; security headers; a same-origin check on API writes; Rival off behind `RIVAL_ENABLED`; friend invite links stay on web sign-up until `PLAY_LISTING_PUBLIC=true`; Next.js 16.2.4 to 16.2.12.
- Verified: on the release branch all 24 suites (app 1,090, auth 165, billing 497, Mob 368 with its 7 old failures gone, learning 377, recovery 646; the only red is the Study line-ending test, fixed on the pass branch), eslint clean, `next build --webpack` 113/113; an independent Opus review (no blocker; its six findings fixed or checked); Vercel preview READY on Turbopack. On www after deploy: `/`, `/pricing`, `/signup`, `/login`, `/privacy`, `/cuet/accountancy` 200; the feed and `/api/today` 401 with no shared cache; `/coming-soon` 404; the headers served; an Android invite link goes to `/signup`; no runtime errors.
- Not checked: any signed-in flow on production, a real payment, refund or cancel, the distress reply through a real model turn, a physical phone.
- Built and gated, NOT deployed (branch `web/1115-prod` in `wt-1110-convert`, 36511c192; all suites, lint and a 115-page build pass): the test screen keeps answers through a reload at time-up, Back, a second tab and going offline, and a left paper can be resumed from Today and Practice; error pages everywhere; the result's report sheet, tomorrow line and install card; the first run ends on a question (one tap, was three and a scroll); fresh-account states; share images under 300 KB; the bubble texture he rejected is gone; the privacy page says what the code does. Waiting on a visual check of the merged branch and the sign-in lane (Open in Chrome inside Instagram, One Tap behind a switch).
- His to do first: Vercel Hobby and Supabase Free to Pro; check the Resend plan and set `AUTH_EMAIL_DAILY_CEILING` to fit it; tick `refund.processed` and `payment.dispute.*` in the Razorpay webhook; a DMARC record; the 20 Oct deletion request (due 19 Nov; the script now needs the Razorpay keys); one real Rs 99 purchase and cancel (the ten steps are in `RUNBOOK-REFUNDS-2026-11-15.md`'s companion list in the plan doc).

## 13 Nov 2026, about 1:35 am IST — round 14: real Ask Mobi for guests, Mobi as the phone scroll companion, the visual pass: web LIVE (main 38a09a4e7; was a218cb9a4, rollback dpl_A8w9FmNKKAMmeJnknspWD5LHjuFY)

- His words (LK237-LK241): round 13 read as "the entire landing page looks the same"; he ordered the full Ask Mobi for visitors without an account (real model calls; aim ₹0.5 a visitor, ₹1 at most), Ask Mobi at the front, Mobi as a scroll companion on phones, and a visual slop pass; two hours, build first, review once at the end at 8 of 10 or better.
- Ask Mobi for guests: `POST /api/mobi/guest` (`src/lib/server/guestMobi.js`). Three questions a visitor, real replies from the cheapest allowed model, one attempt, 220 output tokens at most. Guard: the runtime reservation without a user, plus three database limits (visitor 3 in 24 days by a signed cookie id, network 12 a day, whole site 1,000 a day or `GUEST_MOBI_DAILY_CALLS`). Worst case ₹0.042 a call, ₹0.13 a visitor, about ₹42 a day for the whole site. Kill switch: `GUEST_MOBI_ENABLED=false` on Vercel, then redeploy. Production has no `PERSISTENT_LIMITS_ENABLED`, so this route asks for the database limiter directly (`rateLimit.js`, option `persistent`); other routes are unchanged.
- Where he looks on his phone: the hero's feature list is two columns now and its "Ask Mobi" row opens the sheet; a small Mobi stands on the bottom bar from the college strip on, leans as he scrolls, and a tap opens the sheet; the sample's result key sends "What should I do tonight?" with the five answers. Boxes are gone from Compass, the exam note, Key cards, pricing and the tour; the sample, Mistake Lab and pricing headings are larger; Mobi's captions are plain text.
- Verified: test:app 1,065, landing files 280, dock 62, du 43, keycards-ui 40, auth 141, billing 455, subjects 62, today 146, learn 440, AI cap tests 26, all 0 failures; eslint clean; next build --webpack 115/115; Vercel preview dpl_5gDcuPH8MQ7DSzGMcJRwotiqmHvG READY before the first push to main (the two later small commits went to main after a local build only). On www at 390 Night: the sheet opened from the strip, a real question answered ("2 questions left"), the companion present at Key cards, 0 page errors, nothing past the right edge.
- Not checked: a physical phone and its keyboard over the sheet, iPhone Safari, a screen reader, tablet widths (640 to 959), whether the model's CUET facts are right beyond the few questions asked (it is told to defer to NTA when unsure, but it can still be wrong).
- Open and his: which "inaccurate depictions" he meant (asked, not answered); the companion's head can sit over a reel card or FAQ row edge when tucked; the site-wide daily ceiling of 1,000 guest calls is the agent's safeguard, his to change.

## 13 Nov 2026, about 12:20 am IST — round 13: the motion pass, Mobi on the scroll, Ask Mobi on the sample: web LIVE (main a218cb9a4, dpl_A8w9FmNKKAMmeJnknspWD5LHjuFY; was 766eb6da9, rollback dpl_CKT48CAQJP3fESpAJbLWEaPiu2KD)

- His brief (LK232-LK236, 12 Nov about 11:25 pm, dictated): a controlled pass on the landing's animations and UX: better animations and flows, less "ice block" (read as AI slop), Mobi integrated "using scroll graph" (read as scroll-craft, the skill in `mockmob copy/scroll-craft-main`), and maybe Mobi as a bot in the free trial without sign-up. Both readings are to confirm with him.
- Where he looks on his phone, in page order:
  1. "Try five CUET questions": as it scrolls in, the room settles back and Mobi comes forward. Answer the five: each tap dips, the answer lands without a hop, the next question rises in. On the result, tap "Ask Mobi what to do tonight", then the two follow-ups.
  2. The Mistake Lab and "More inside MockMob": the small Mobi on the bottom bar's step line hops with each swipe; one Lab scene leaves before the next arrives.
  3. Any section heading further down: it rises in quickly, with no blur.
  4. The menu (top right): the sign-up keys arrive sooner.
- Ask Mobi on the sample uses no AI model: the step is worked out in the browser from the five answers, and its last line says so. A Mobi that answers typed questions from guests needs his decision on a guest budget (LK236); not built.
- Verified before deploy: test:app 1,043, landing files 271, dock 62, du 43, keycards-ui 40, auth 141, billing 455, subjects 62, today 146, learn 440, all 0 failures; eslint clean; next build --webpack 115/115; Vercel preview dpl_7WUXyyZBz5gqCkUWXCjjsBG4fz9L READY before main. In headless Chrome on the dev build at 390 x 844 and 360 x 740 (Day and Night) and 1440 x 900: timed frames of the taps and the Lab change, the whole page top to bottom, Ask Mobi with 0, 3 and 5 misses, Reduce motion (15 reveals visible and still), 0 page errors, nothing past the right edge, real-pointer hit tests on the options, the ask key and Skip. Section heights match the live site except the sample's new line (24 px).
- Not checked: a physical phone, iPhone Safari (the desk's scroll depth needs a browser with CSS view timelines; others show the plain scene), how the new timings feel in the hand, a screen reader, tablet widths.
- Open and his: the guest AI budget for a typed Mobi (LK236); from the audit, the seats' hop-in timing and the Lab screens' 2.4 s draw (UI-AUDIT-LOG 2a). Earlier ones stand: Wallet selling, the account-level guide flag, past-paper labels.
- For other agents: the home page's motion is inventoried in `wt-1110-convert/tmp/1113-motion/AUDIT.md`; round 13's rules are all in `src/app/r13-motion.css`.

## 12 Nov 2026, about 9:20 pm IST — final pass: web LIVE (main 766eb6da9, dpl_CKT48CAQJP3fESpAJbLWEaPiu2KD; was 230de48e8), app 1.0.23+21 built for his upload

- His brief (LK225-LK230): one final pass on the hero, the home page, the signed-in product on desktop and the app; fix weak points only; deploy the site and build the app for Play.
- Web, live: the tour's last slide fits a phone (it ran 43 px past the edge); Learn and Key cards share the one left edge on desktop; the Mob's roster and settings sit side by side on desktop; no success toast before a practice set exists. The hero, the film and the rest of the home page were examined and left alone.
- App 1.0.23+21 (c79dac51c, branch ui/1112-final): the band under the bottom bar closes; one "Credits" label and no empty band in the account sheet; the opening screen's light runs to the top; the welcome screen has no black strip at the bottom; Privacy opens Privacy. Files: Desktop/MockMob-build-21 (AAB that sells, arm64 APK, symbols, OWNER-STEPS.md).
- Verified, web: landing gate 572 (548 pass, 0 fail), test:app 1,035, dock 63, du 43, keycards-ui 40, auth 141, billing 455, subjects 62, today 146, learn 440, test:mob 345 of 352 (the 7 old server-side failures); eslint clean; next build --webpack 115/115; Vercel preview READY before main; live: / /pricing /signup /login 200, the tour fix served, no tour slide past the edge at 390 on www. App: Checked: flutter analyze clean; unit folders account_sheet, core/router, core_ui, credits, a11y, you, today (1,460), test/widget (365) and the welcome tests (74) pass; 130 reference images re-recorded and their suites pass (324); the bundle and the APK carry the upload key (SHA-256 62:AC:58:08...EC:47) and pass the 16 KB check; on the emulator, the signed-in screens in the demo build (Night and Day) and the release build itself, installed over version 16: opening screen, welcome, the class, course and college steps.
- Not checked: a physical phone, iPhone Safari, signed-in pages on production, the test-taking screen on desktop. App: a physical phone; a sign-in in the release build; the first-run flow after the college step on a device; the whole unit and golden folders in one run (old drift remains in the credits, start sheet, art scenes, today_resume and share-card reference images; the credits ones fail without these changes too).
- For the CTO: a debug build of the real app stops on the opening screen (Riverpod's debug-only CircularDependencyError: AuthController listens to networkRestoredProvider, whose ConnectivityMonitor depends, through three providers, on AuthController; auth_controller.dart _watchForRecovery). Release builds do not run that check. Not changed in this pass.
- Open and his: Wallet selling (WALLET_COMMERCE_OPEN, after a test payment); an account-level guide flag; past-paper labels for sample questions; a portrait cut of the hero film for phones.

## 11 Nov 2026, about 1:29 am IST — the guide and web onboarding are LIVE (main 230de48e8; was 97192a222)

- All six items of his 10 Nov feedback have shipped. This sitting: the guide rebuilt with a once-only auto-start for a just-onboarded student (LK221) and web onboarding polish (LK216); the other session's four releases were reviewed on screen and hold.
- Verified: landing gate 572 tests (0 fail), test:app 1,035, dock 63, du 43, keycards-ui 40, auth 141, billing 455, subjects 62, today 146, guide and onboarding files 57; eslint clean; next build --webpack 115/115; Vercel preview READY before main. Seen in headless Chrome on the dev preview only.
- Not checked: a physical phone, iPhone Safari, a real new account's hand-off from onboarding into the guide, a screen reader, signed-in pages on production.
- Open and his: Wallet selling (WALLET_COMMERCE_OPEN, after a test payment); whether the guide should also start on a second device (needs an account-level flag, a schema change); past-paper labels for sample questions (needs verified data).

## 11 Nov 2026, 12:15 am IST — Guide design ready for review (LK221)

- The owner can try the three-stop Today guide in the design preview delivered in the Codex chat. The live guide is still manual. The current completion flag is browser-local.
- Chromium verified 18 placements at 360 × 672, 390 × 844 and 1440 × 900 in both themes, plus touch, keyboard, replay and dismissal. No physical phone or Safari check. LK216 follows after LK221.

## 11 Nov 2026, 12:09 am IST — Wallet history and states live (LK217)

- In Wallet, Recent activity lists the four latest entries and opens older activity on request. The states and 360 px layout were checked locally. Main 97192a222 serves www.mockmob.in.
- Checkout was exercised with a local stub. No payment, physical phone, iPhone Safari or signed-in production check. Selling is closed. Next is the guide design.

## 10 Nov 2026, 11:47 pm IST — Home sample loading and selection live (LK223)

- On the home sample, tap Not your subject? and choose a subject. The card shows what is loading and lets you change your mind. A previously loaded alternate set can open immediately.
- Main 4461487f5. The new build serves www.mockmob.in. The 30-question Accountancy window spans 12 chapters. No question in that checked window qualified for a past-paper label.
- Local Chromium covered 360, 390 and 1440 in both themes with delayed responses, cancellation, cache and failure states. A signed-out production check at 390 used intercepted responses. No physical phone, iPhone Safari or signed-in production check.
- Next is Wallet history and states, then the guide design and web onboarding.

## 10 Nov 2026, 11:19 pm IST — You and Mob profile live (LK219)

- Open You and scroll to the account card. The saved name and initial lead, the credit balance opens Wallet, and the subjects read in two columns. Edit Mob profile opens the existing name and colour dialog for the displayed Mob.
- Main 755dd31fe. Preview dpl_3zm4AwRiDpZLXFuxifVdWF81ccYo and production dpl_8Q2DatvUNcU9NukxFBm2kQCxHVX2 are READY. www.mockmob.in resolves to this production build.
- Local Chromium covered one to five subjects in Free and Pro at 390 and 360, both themes, and Day and Night at 1440. Mob identity, editing, loading, error, no Mob and feature-off states were checked using fixtures. A physical phone, iPhone Safari and signed-in production were not checked.
- Next is the home sample, then the remaining Wallet states, guide design and web onboarding.

## 10 Nov 2026, 10:55 pm IST — Pro sheet refinement live (LK218)

- In Practice, tap Smart practice, NTA mode or a locked difficulty. The sheet names the feature, shows a MockMob desk object and keeps the real price, terms and action together below the benefits.
- Main da4555622. Preview dpl_GyFKeaiqZQuTT2VN2jmcNdaWPG9F READY before production dpl_AZYV4RFeYUpTEZuyYN9RJ56bv8rX, which owns www.mockmob.in.
- Verified in local Chromium fixtures at 390 × 844, 360 × 740, 360 × 672 and 1440 × 900, in both themes. Physical phones, iPhone Safari and signed-in production were not checked.
- Next in order: You and Mob identity, home sample, Wallet, guide design, web onboarding.

## 10 Nov 2026, about 10:35 pm IST — the rest of his feedback is handed off (HANDOFF-2026-11-10-FEEDBACK-REST.md, PROMPT-2026-11-10-FEEDBACK-REST.md)

- He asked for a handoff and a detailed prompt for a smaller model in another window. Left, in order: the Pro pop-up graphic, the You card with even subjects and a Mob profile, the home sample (loading state, finest questions), the rest of the Wallet (selling stays closed until he tests and decides), the guide with auto-start, web onboarding polish. Nothing is half-built: main 7444fb291 is live and the working tree is clean.

## 10 Nov 2026, about 10:20 pm IST — his feedback on the app-refine pass, part done and LIVE (main 7444fb291); the rest waits for the next usage window

- His feedback (LK212-LK224 in the ledger). LIVE: the refund words (/pricing support line and /refunds), the Pro timeline graphic, a fourth "Also in Pro" tile, the Accountancy onboarding note (checked against the 2026 syllabus; all subjects re-read), the Night/Day switch beside the mark on phones, locked difficulty levels open the Pro sheet, the chosen practice tile's ring, the Wallet's first screen and pack cards.
- NOT done (the 5-hour usage window was nearly spent by about 10 pm, so two helpers were paused; it resets about 12:50 am): the Wallet's history and rarer states; the Pro pop-up graphic; the You card, even subjects and a Mob profile (helper `youcard`, paused); the home sample's loading state and finest questions (helper `sample`, paused); the guide redesign with auto-start; web onboarding polish. The two paused helpers resume by agent id with SendMessage; their briefs are in this session's transcript and the owner's words are in the ledger.
- Buying credits: closed by WALLET_COMMERCE_OPEN (Vercel Production). The path has never been run with a payment. His decision and a test-card run come first (tmp/1110-app/notes-wallet.md).
- Verified: test:app 1,034, dock 63, subjects 62, billing 453, landing gate 570 (0 fail), pricing/refunds/wallet/credit files 206; eslint clean; Vercel preview READY before main each time. Seen in headless Chrome at 390 (Night and Day) and 1440; not on a phone; signed-in pages only on the dev preview.

## 10 Nov 2026, about 9:10 pm IST — the app-refine pass is LIVE (main becb9055b; was ca0991ae8, rollback dpl_jgpwQVt4eiE6Cm3iAh9ZJgMf4nq4)

- His brief (PROMPT-2026-11-10-APP-REFINE.md, LK199-LK207): make the signed-in product on a phone feel finished and easy; a clear Day/Night choice in the app and on the home page; each feature one level deeper (the Mob first); Sign out twice, the theme transition, the landing texture; /pricing from 9 to 10; the hero pictures reordered. Outcomes per item are in OWNER-MASTER-LEDGER.md (LK199-LK211).
- Where he looks on his phone: after login, the top bar (the "mo" mark, Ask Mobi, the sun and moon switch, credits and the person); tap the switch; tap the person for the sheet with one Sign out. Then Mob, Colleges (from You), Review, You, Wallet. Signed out: the home page's first visit note under the switch (shows once per browser; a private tab shows it again), the faint grid and grain, the three pictures under the hero keys, /pricing under the plan cards.
- Verified before deploy: landing gate 570 tests (546 pass, 0 fail), test:app 1,034, dock 63, du 43, keycards-ui 40, auth 141, billing 453, today 146, subjects 62, recovery 642, learn 440, 27 new tests; eslint clean on every changed script file; next build --webpack 115/115; Vercel preview dpl_FPoMfyNN9FRNCWY9hqgyZ9g3k5dq READY before main; production dpl_9HAX3Y9Ta4P9YjeVwpoT5xdM8ohC. Signed-in screens were seen only through the dev preview route with fixture data, in headless Chrome at 390 x 844, 360 x 740, 360 x 672 and 1440 x 900, Night and Day.
- Not checked: a physical phone, iPhone Safari, signed-in pages on production, the Mob explainer/live/play screens after the change. Not in the gate and failing with or without this change: test:mob (7 server-side tests), test:study (1, the content gate).
- His to confirm on /pricing: the refund question on that page, "we reply within a day", and the items listed under LK205.
- Working files (not shipped): wt-1110-convert/tmp/1110-app (walk.mjs, tap.mjs, land.mjs, reveal.mjs, notes-*.md from each sub-agent, FINDINGS.md, shots/).

## 10 Nov 2026, about 3:15 pm IST — next task handed off, not started (LK199-LK207)

- The owner approved rounds 11 and 12, then asked for a pass on the signed-in phone UI (the arena), a clear Day/Night choice, each feature deeper (the Mob), named inconsistencies (Sign out twice, theme transition, landing texture), /pricing from 9 to 10, and the hero pictures reordered (Garima, Radhika, Rahul). This account is at 94% weekly, so he asked for a handoff and a prompt for a new account instead of the work: HANDOFF-2026-11-10-APP-REFINE.md and PROMPT-2026-11-10-APP-REFINE.md. Nothing of it is built.

## 10 Nov 2026, about 2:50 pm IST — round 12 LIVE: creators' real profiles, sixth Pro feature, film sound and full screen (main ca0991ae8; was 79b9c49cb)

- His words (10 Nov, after round 11): the Pro card's five icons "feel a bit out of place ... make it six"; the proof line's profiles were blank, "pick up their profiles from Instagram", add the other creators, "remove Prathna" from the featured ones but keep her in the Instagram section; the film's first sound-on "should play from the start"; a full-screen mode for the hero film. He approved the round 11 cuts after hearing the list.
- Done: creators re-read from Instagram on 10 Nov (du__club 208K, garima.again 28K, rahul.guides 12K, radhikagaur_055 8,814 new with reel DX11ggsyKFf, prathnajains23 180); profile pictures in public/brand/creators; featured = Garima, Radhika, Rahul (figure computes to 256K+); reel views from his screenshot (77.4K, 17.1K, 5,749, 1,364; matched to reels by the order of the reels tab); "NTA mode" is the sixth Pro feature; the first sound-on restarts the film; a full-screen key (in the picture's corner on phones, in the key row on wider screens).
- Gate: landing 570 tests, 545 pass, 1 old fail (LK141); eslint clean; Vercel preview dpl_9eS1YsaPdtdwud4x7PJ2B5SFhqKK READY, then main; the live page serves the figure, the pictures and the key. Not checked: a physical phone, iPhone Safari full screen, leaving full screen with Escape (headless Chrome ignores it). Garima's 695 likes are from 3 Oct.

## 10 Nov 2026, about 1:15 pm IST — round 11 LIVE: consistent phone scroll, one Lab, a five-tool tour (main 79b9c49cb; was 7c28f3ea7, rollback dpl_6cJqMnU6b1AwqjBNna1FX1KJTGdt)

- His words: LK191-LK198 (verbatim in ROUND-11-SPEC-2026-11-10.md). Later the same morning: "Don't worry about the weekly usage limit ... keep working until what you are doing is done" (weekly usage is no reason to stop or shrink scope).
- Phone scroll v2 (LK192): on a touch screen, in the Lab and the tour, the gesture chooses the step. A swipe released under 2.5 px/ms is exactly one step (shown once the page has gone 32 px under the finger; its momentum is held on that step's rest, unseen because the stage is sticky); a flick stays free (steps shown 120 ms late, never settling behind the step it showed); a swipe that brings a story on lands on the step at its door; no touch is taken, no lock. The statement stays position-driven. On browsers that are not Chromium nothing is put until the scroll rests. A step costs 0.85 of the mouse's hold (was 0.6). Knobs: storyGesture.mjs FLOW_FLICK_V, FLOW_COMMIT_PX; the 0.85 in scroll-story.css.
- One Lab (LK193): the Score Recovery section is off the page; the Mistake Lab has five scenes, a new first one Chapters ("Where your marks went", by chapter, from the same sample mock), then Time, Changes, Repair, SWOT (ends on "Sign up free and open yours"). "Score Recovery" is no longer named on the landing (strip, pricing features).
- Tour (LK196): "More inside MockMob.", five tools (Practice, Learn, Ask Mobi, Benchmarks, The Mob), no play/pause key in the held tour; Mobi's blink no longer loops for ever.
- Exam (LK195): "Warnings 0/3" removed; the rule in words from the runner's guard ("Leaving fullscreen or switching tabs counts as a warning. The third one submits your answers."); the section now sits before DU Compass.
- Marketing (LK194): hero proof line under the keys ("Featured by CUET creators with 199K+ followers", figure computed in src/lib/social, links to the creators section; two lines under 388 px); strip item "Exam-day screen"; DU section without the college chips, Combo Planner as one link line.
- Gate: landing 567 tests, 542 pass, 1 fail (LK141, old); app, dock, DU, Key cards UI, auth all pass; eslint clean; webpack build 115/115; Vercel preview dpl_DDrY2ZxSTWsjJHnq7FJLewH4ijKV READY, then main. Real Chrome at 390 on the dev build: flow tour 29/29 and Lab 29/29, landing 6/6, jump 8/8 (390) and 4/4 (1440), wheel 10/10 and 10/10. Flicks from the top to the plans: 30 at 1200 px/s, 19 at 2000, 10 at 3000, none stuck.
- Not checked: a physical phone, iPhone Safari, a screen reader. Reserved heights at 1024x768 touch are still about 324 px off (tablet landscape). The tour's reserved height is up to 94 px short on a 700 px tall laptop window.
- For him to look at on his phone: swipe through the Lab and "More inside MockMob" (one swipe, one slide; flick to run on); the Chapters scene; the hero proof line; the exam card's rule sentence.

## 10 Nov 2026, about 5:15 am IST — his phone look at round 10 (LK191-LK198); round 11 specified, scroll fix in progress

- His words (verbatim in ROUND-11-SPEC-2026-11-10.md): flow is the right direction but normal swipes are uneven ("skips too much or too little", worst in What's inside MockMob); flicks running on is fine; not held. Merge the Mistake Lab and the Score Recovery Lab (same feature, two sections). The "0/3 warnings" on the exam screen is not interactive. The tour's play/pause key has no autoplay behind it: remove it or bring back the story UI. More marketing thinking; the phone is the product (100% of conversions); he gives authority to add or remove anything on the landing page; he wants a finished product.
- Decided (the spec has the build detail): scroll v2 = a normal swipe is exactly one step, a flick is free, longer steps; one Lab of five scenes (Chapters, Time, Changes, Repair, Plan), the Recovery section and its three repeat tour slides go; the tour becomes "More inside MockMob" with five tools and no play key; the warnings pill goes; exam screen moves above the DU tools; hero key gets "No card needed"; a creators proof line under the hero keys.
- State: live is still round 10 (main 7c28f3ea7). Session 585e670b's context window was 92% full and weekly usage 87% when this was written, so the work continues from the spec (this session after compaction, or a new one with the spec as its brief). No large agent swarm at this usage.

## 10 Nov 2026, about 4:30 am IST — round 10 LIVE: landing taste refinement and the phone scroll decision (main 7c28f3ea7, dpl_6cJqMnU6b1AwqjBNna1FX1KJTGdt; was 5dbcea349, rollback dpl_F112hcu3ezRJratCkZem1eQMpYSm)

- His words (10 Nov, three messages; ledger LK185-LK190): a polish and conversion pass; then "take it deeper ... more as a UI/UX refinement and design taste refinement ... When you are satisfied ... commit the site and deploy it live" (no measuring wanted); then settle the phone scroll ("if we remove scroll, we aren't able to really show the features ... If we keep the scroll, then it feels very locked in"). Write-up: ROUND-10-LANDING-2026-11-10.md.
- Phone scroll is now FLOW (replaces "one gesture, one step" on touch screens; settles LK179): the stage still pins and shows every step, the scroll is always the browser's own, a gentle swipe moves one step, a flick passes several, a scroll at rest settles on the nearest step, and the first fling that brings the Mistake Lab, the tour or the Recovery Lab on lands once on its first step. A story costs 0.6 of the scroll it did. A mouse or trackpad is unchanged. Measured on the live site (real Chrome, real flings, 390x844): from the top to the plans, 31 ordinary flicks before, 19 now; 23 quick flicks before, 10 now; a gentle reader 41 before, 38 now. The phone page is 23,226 px (was 26,107).
- Visual refinement, five groups (hero; sample and statement; Mistake Lab and tour; Score Recovery, Key cards, Compass, DU, exam; creators, pricing, FAQ, close, footer, sign-up and log-in), each looked at before and after at 390 and 1440, Day and Night; nothing removed, no new claims. The first pass is in too: the sample's result opens /signup; no theme note over a phone's headline; the home page's funnel steps (the counter's switch stays off, not his ask).
- Gate: landing 554 tests, 529 pass, 1 fail (LK141 account pop-over, also fails on 5dbcea349), 12 skipped; app 1,030, dock 62, DU 42, Key cards UI 40, auth 141, all pass; eslint clean; webpack build 115/115; Vercel's build READY on the branch, then on main. Real Chrome on the merged build: flow 78/78 cells, landing 8/8, link jumps 10/10 at 390 and 5/5 at 1440, desktop wheel 30/30. Live: Vercel READY, no runtime errors in 30 min, live walks at 390 and 1440 with 0 page errors, landing 8/8 on www, the sample's 3 of 5 opens /signup.
- Not checked: a physical phone or iPhone Safari (flow was run in real desktop Chrome with touch emulation only), a screen reader, signed-in pages. At 4x CPU the cold scroll bench has 5 frames over 100 ms (the live site before had 3; the 394 ms one near the hero was there before).
- For him to look at on his phone: the scroll feel (one stop per story, then free); the sample on a laptop (Mobi's room now sits beside the card); Learn's tour title "Learn the idea. Then make it stick."; the Free panel in pricing. Each is easy to turn back.
- Left: proto/1109-share (full-screen film key, the laptop note) is still his separate decision; a day-old orphaned test-browser process (pid 42360, 19 MB) could not be ended.

## 9 Nov 2026, about 11 pm IST — sample result polish LIVE (main 5dbcea349, dpl_F112hcu3ezRJratCkZem1eQMpYSm; was 1184acb84)

- Brief (owner, 9 Nov night, pasted research prompt): make the homepage five-question sample's result explain itself (Packet A); fix demo arrival only if a phone reproduces the dock covering it (Packet B); local diff, release is a separate owner decision.
- Done (Packet A): heading "What you missed in these five" (was "After a full mock, chapter review would flag:"); each miss row leads with its question number (Q2, Q4), so two misses in one chapter stay distinct; an open miss shows "Your answer" and "Correct answer" with option texts, then the reason; its line says the real next step ("Sign up free, then choose chapters like this one in Practice."); "A full mock gives you a broader chapter review." above the one volt key (not on 5/5); a no-break worked sum wraps at 150% text instead of being clipped. Files: src/components/landing/DemoDrill.jsx, demo-subject.css only.
- Packet B: not reproduced at 360x640, 360x800, 390x844 (first jump, repeat jumps after progress, result, keyboard, fresh /#try-practice): the dock is never drawn there; head and first control always clear. No code change.
- Checks: before/after walks on two local servers (Day/Night, 390/1440/360, scores 0-5, fixture with repeated chapter and long texts, slow and failed subject with retry): 0 page errors. Landing suites 391/415 pass, the 1 failure also fails on 1184acb84 (0 new). eslint clean, webpack build passes. Lab perf (dev, 4x CPU, throttled): same 58 requests, +3 KB, result transition unchanged. Not checked: a physical phone, a screen reader by ear.
- Evidence: wt-1109-demo-result/tmp/1109-demo/report/index.html (paired images, recording, table).
- Deployed on the owner's "Yes, deploy it" (9 Nov ~11:30 pm): fast-forward 1184acb84..5dbcea349, Vercel READY, no runtime errors in 30 min. Live walk on www at 390: Night default five 3/5 (Q2, Q4, your/correct answers, 0 errors); Day live Accountancy set 1/5 with three misses in one chapter shown as Q1, Q2, Q5. Not checked live: a physical phone.

## 9 Nov 2026, about 5:50 am IST — hero walkthrough film r2 LIVE (main be44eafca, dpl_Vtz6tKbgL61KmefrF26DgLygcPKw; r1 was dd8c63a7a)

- Owner (9 Nov ~2:30 am): the main walkthrough video of the platform for the hero, reframed from the promo, highly converting; discretion on the player. Owner (~4 am): visitors already half-trust us; build trust, show we are the best and everything we offer, not first-time promotion (LK180, LK181).
- Film: Hero16 in Desktop/MockMob-promo-film (now a git repo; spec docs/HERO-FILM-SPEC.md, notes docs/HERO-NOTES.md). 66.967 s, muted-first, loops. Hook (Preparing for CUET 2027? / 142 / "But where did the other 108 go?") then the study loop: Mistake Repair, Learn (new), Ask Mobi, Key cards (new), unlimited mocks, exam-day screen, plan and colleges, the Mob, What you get (new: the site's subject claim and value card, ₹3,750 the usual way vs ₹99 a month), Sign up free. Every line holds long enough to read muted (lint: 0.6 s + 0.12 s a word). No Google Play claim (the old end card had one). Sound: paid-account audio only, -16.2 LUFS.
- Player (web/r9-hero-film): keys moved off the picture into a bar under it (pause, ten chapter segments that jump, sound), tap the picture to pause, 480/720/1080 by width x DPR. Tests 70/70, webpack build, 390/1440 Night/Day checked locally and live; no runtime errors.
- r2 (live): Mobi's 3D gestures re-timed to the hero's beats, "Mock after mock, and the score won't move." reads whole, larger Sign up free end card at phone width, Key card clear of the player's rounded corner, no strobe in the Mocks counter, two sound overlaps cleared; same 66.967 s and chapter times. Promo commit 0ddcf42; master out/hero/hero-r2-master.mp4.
- Next: owner judges the film and its sound (tap the speaker under the film) on his phone; open choice: Learn/Ask Mobi/Mob phones sit 28-50 px from the right edge by v8 design (left as is). Old teaser files public/video/hero-480/720/poster still in the repo (remove in a later cleanup). Owner should judge the sound by ear.

## 9 Nov 2026, about 1 am IST — phone scroll prototype (LK179), preview only, NOT live

- Owner (9 Nov): no forced scroll-through on phones ("They can see if they want to"); desktop may keep it. Reverses L-029/LK69/LK103 on phones.
- Prototype: branch proto/phone-free-scroll 27b8da7ac (from main a017c2555), Vercel preview dpl_5r5XHhqCH3X4Pov2o9MHA2dWkHcX (protected; a share link valid until about midnight 9-10 Nov IST was given to the owner in chat). ScrollStory holds only at (min-width: 960px) with hover and a fine pointer; phones and touch screens scroll freely; Mistake Lab = sideways row of 4 scene cards + tabs; statement scrubs; tour and Recovery Lab use their free modes.
- Checked: eslint clean, landing tests 231/231, headless touch walk at 390 (local and preview): one swipe moves the page about 1,300 px, a sideways swipe moves one Lab scene, tabs move the row, no sideways page scroll, 0 page errors; desktop 1440 still holds. Not checked: a real phone, signed-in pages.
- Next: owner looks on his phone; on his yes, merge to main and deploy; decide whether the tour keeps its autoplay on phones.

## 8 Nov 2026, evening IST — R8 + hero round 7 LIVE (main a017c2555, dpl_8ZMizFw6Cx4pGNiYQUDeoZqiD9mf); app 20 built

- Owner go (8 Nov evening): merge yesterday's hero (launch film, college strip) with R8, deploy, then the app. web/r7-hero merged into web/r8-craft cleanly; Arena's warm hairline grid restored (owner: the earlier texture looked better; warm palette kept). Pushed main 2f0d6b489..a017c2555.
- Gate: suites 0 new failures (baseline Mob 7, Study 1); hero/landing tests 317/317; eslint clean on hero files; Turbopack build passed. Live: Vercel READY, no runtime errors, www / /pricing /signup /learn /cuet/accountancy 200, film and logos served, 390/1440 no sideways scroll.
- Learn "gone" in the LAN preview: the preview hides Learn unless the link has &study=on; R8 did not touch Learn's nav or flags. Not checked signed-in on production.
- App 1.0.22+20 (ui/r8-app-craft 813eaa495, pushed as a branch): Desktop/MockMob-build-20 (sells AAB + arm64 APK, upload-key signer checked, 16 KB ok, OWNER-STEPS.md). Awaits the owner's Play upload. Not installed on a phone.
- Open: 22-swipe bench slightly heavier than pre-R8; owner decisions (keycap vs pill, Score Recovery on sale, Repair Q42 verb, Day samples, app swipe, APP-11/14/20).

## 8 Nov 2026, about 12:30 pm IST — R8 visible-craft pass finished locally (NOT deployed)

- Branches: web `web/r8-craft` (worktree wt-1108-craft, from main 2f0d6b489; 8 batches + 15 sweep commits); app `ui/r8-app-craft` (wt-1108-app). Nothing pushed.
- Visual report (before/after, done, not done): wt-1108-craft/tmp/r8-craft/report/R8-BEFORE-AFTER.html. Every change: tmp/r8-craft/RUNNING-LOG.md and tmp/r8-craft/changes/CHANGES-*.md.
- Checks: suites 0 new failures (baseline Mob 7, Study 1); eslint clean (180 files); webpack and Turbopack 115/115; touch 128/128, wheel 30/30; 70 home section shots looked at (Key cards on); app analyze clean + emulator walk.
- Open before release: 22-swipe bench R8 0-1 cold / 1-2 warm over 100 ms vs pre-R8 0 / 1-2 on the same PC (slightly heavier; profile first). Owner decisions in tmp/r8-craft/OWNER-DECISIONS.md and sweep/OWNER-FLAGS-raw.md.
- Local launcher fix: KEY_CARDS_ENABLED must be 'true' (not '1') or every Key cards surface is off in previews.

## 6 Nov 2026, about 8:40 pm IST — round 5 live (main d629a2939, dpl_DkxPwhLNPpNJSUH7v86zDTkGGRoF)

- Mobile scroll (LK161): reproduced on real Android Chrome (emulator, adb touch): quick swipes skipped 2-3 steps. Fixed with touch-action on the held story (pan only the way out), one fling stop per edge catch, and edge adoption. After: 0 multi-step jumps in 88 real swipes. Desktop: a spun mouse wheel no longer shakes at story edges (LK154).
- Hero: CUET 2027 by colour and size, no highlighter; 3D strip objects back and sharper; paper grain behind the hero.
- Pricing: /pricing on phones is Pro first with a Pro | Free switch; the home value card compares what students usually pay (₹500 + ₹250 a subject, typical) with ₹99 a month. Exam full screen stays upright on phones.
- Live checks: Vercel READY, no runtime errors, 375 px renders, no sideways scroll. Suites 0 failures; both bundlers built; touch 128/128; wheel 10/10.
- Not passed at the time: the 22-swipe speed bench (one long frame per edge catch, 100-170 ms at 4x CPU); LK169 is now fixed, see the 7 Nov update below. Preview links fall back to the one-time offer (monthly plan ID is production-only).
- 7 Nov 2026 update (Round 5 scroll fix, pushed to main c267858d1; commits e0f323057 + c267858d1 on top of bac4ae9ab; main was d629a2939). Vercel deploy is being verified separately.
  - Mobile multi-step skip, root cause: the edge catch required the previous scroll frame to be more than 1 px outside a story, so a fling frame landing exactly 1 px short (1735 for a top of 1736) and then crossing was never caught and flew through every step. Reproduced 4/4, fixed (strict outside check, also in the wheel look-ahead).
  - LK169 edge hitch, root cause: marking the held story (a class that changes the track's touch-action) restyles the whole story, about 90-100 ms at 4x CPU, and it was done inside the fling catch and inside a step's own frame. Now the catch only stops the fling; the mark is set at rest (settle, 150 ms after the page stops).
  - The fling-stop guard now resets on settle and on each touch (it never reset before, so a second fling into the same story ran on; live had that bug).
  - Speed bench (22 swipes at 4x CPU, cold and warm, quiet machine): 8-10 frames over 100 ms before, 0-3 after, none in the scroll code. Round 4 baseline on the same PC also ranges 0-6, so the strict "zero over 100 ms" gate is not met consistently on this machine.
  - Touch matrix 128/128 at 390x844 and 390x740 and wheel matrix at 1440 passed on the build with the 1 px fix (gate19). The final build's matrices were still running at push time; results to be added.
  - Not done: a real Android emulator swipe test on the final build (owner asked to ship within 10 minutes). The value card iteration remains open to the owner.
  - Machine note: the AI OS nightly (rag index --vectors, two embed-pending jobs, brain ingest) held the CPU at about 60-100% for over an hour on the night of 6-7 Nov and invalidated speed benches; two embed-pending ran at once (possible duplicate).

## 6 Nov 2026, about 1:05 pm IST — Round 4 live (main 068a7a061, dpl_34h9RLVRZwqfGwEZ62R93vu4kR7q)

- Round 4 (LK117-LK147, LK150) is on www.mockmob.in. Runtime is `06aed8557`; `068a7a061` adds only the corrected source assertion (outside touches checked in `onTouchStart`) and the STATUS gate note.
- Gate on the 06aed8557 build: landing suites 437 pass / 0 fail; eslint clean on all changed files; 22 swipes at 4x CPU over100 = 0 cold (max 97 ms) and warm (max 97 ms); matrix 128/128 at 390; all 72 section captures (390/1440, Night/Day) looked at. The 1440 Key cards shots caught the count-up mid-roll; it settles on 16,458.
- Live check: Vercel READY and the production alias points at the matching SHA; no private runtime errors in the 15 minutes after; www.mockmob.in at 375 px renders, no horizontal scroll, no console errors.
- Not exercised: signed-in use, production sample data, a physical phone, a screen reader. App 1.0.21+19 still awaits the owner's Play upload. Financial Markets Key cards still untouched.

## 6 Nov 2026, about 3:16 am IST — Round 4 integrated and paused at the owner's request

- Round 3 is live on `400d647a8`. Round 4 is committed locally on `web/r4-release` in `wt-1104-web-polish`, with runtime tip `06aed8557`. All six web packets are merged.
- Both final builds and the App suite passed. The last runtime revision still needs the source assertion updated, the full cold/warm and gesture runs, and the final visual sweep. Private Vercel access now works.
- Resume using [the detailed handoff](HANDOFF-2026-11-06-ROUND-4-RELEASE.md) and [next-session prompt](PROMPT-NEXT-SESSION-2026-11-06-ROUND-4-RELEASE.md). App build 19 awaits the owner's Play upload.

## 6 Nov 2026, about 12:40 am IST: stopped at ~90% weekly usage; round 4 saved on branches (not live); next session prompt written
- Live: main 400d647a8 (rounds 1-3). App 1.0.21+19 awaits his upload.
- Round 4 (LK117-LK147): branches web/r4-{demo,pricing} done; web/r4-{hero,learn,nav} fix stage unfinished (WIP commits);
  web/r4-sections build unfinished (WIP); ui/r4-app done. Backups: origin tags archive/r4-r4-*.
- Next: HANDOFF-2026-11-06.md and PROMPT-NEXT-SESSION-2026-11-06.md. The owner may run that prompt on another model as a
  temporary trial (experiments/MODEL-TRIAL-2026-11.md); that session leaves a branch, it does not ship.

## 5 Nov 2026, about 4:45 pm IST: round 3 live (main ce24dc682, dpl_AgxLoHQJ3uoLMdyeifYvm2qJnr9G); new Key cards for Computerised Accounting and English reading
- **Web:** Day palette fixed (#526700 text green, rimmed selected states, no volt slabs on cream), brand stamps and branded creator cards back, "MockMob" green in the statement, calmer hero with a branded fact strip, held stories stop above a bottom bar (Top, n of N, Skip), logo to top, Pricing pill, tour glitch fixed, phone exam screen, one-plan pricing with Rs-per-day/per-mock framing from the offer and a dated same-period comparison, Key cards flip section. Spec: docs/brain/night-1105/SPEC-R3.md.
- **Content:** Computerised Accounting 207 cards, English reading skills 231 cards (live with the site). Financial Markets blocked: Wayback lebs202 2022/2023 truncated; try the full 2021 capture.
- **Usage:** weekly at about 80% after round 3; keep to small fixes until the week resets (10 Nov 9:30 am IST).
- **Open:** real-phone look; count-up figures may read "0 5,765" to screen readers (check CountUp markup); app 1.0.21+19 awaits his upload; leftover empty folder wt-r3-bottom (locked).

## 5 Nov 2026, about 7:50 am IST: round 2 of the night refinement shipped (main 88ff026cc)
- **Web:** the app's motion on the web (the result score's digit roll at his 720 ms tempo, the finish stamp with one ring on a good set, the Start sheet growing out of its key); public pages with Sign up free / Log in everywhere (site bar, phone menu, a PublicDock), "CUET 2027" never split, even lines, nav links from 1120 px, phone footer in two columns; the logged-in web scanned at 25 views x 6 sizes x 2 themes and fixed (Learn feed bar overlap, Practice tiles at 1280, Your papers, wallet alignment, no decorative monospace, 44 px targets). Gate: suites 0 new failures, eslint clean, both builds, 22 swipes over100 = 0, matrix 128/128. Not measured: the Start sheet open at 4x CPU on a production build (dev build showed frames up to ~130 ms).
- **Earlier tonight (round 1, main 7b47b4c90):** LK81-LK97 live; app 1.0.21+19 in Desktop/MockMob-build-19 for his upload.

## 5 Nov 2026, about 5:50 am IST: the night refinement shipped (LK81-LK97); app 1.0.21+19 built for his upload
- **Web (main 7b47b4c90, deploy dpl_q2i33v9L2XTafEoR83f8k8B9LzFi):** slow-phone stutter fixed (idle predraw; 22 swipes at 4x CPU: 0 frames over 100 ms); Sign up free / Log in lead with "Try 5 questions first" second and a dock that never changes; "CUET 2027." and the tour's MockMob in the brand volt (one green); even lines; the statement's green words back; the opening waits for first paint, the typed line lands whole, Ask Mobi reads your record first; the exam screen in a desktop monitor with an address bar and a faithful NTA style, and the test runner's NTA style matching it; no demo-jump loop and a quiet arrival; fast swipes land on the right step; DU section there on arrival; the web account pop-over like the app's sheet; subject options at web onboarding and "Yours is ..." in Learn; Practice at 1024 px fixed; the numbers band never shows an empty slab. Spec: docs/brain/night-1105/SPEC.md on main; design notes docs/design-decisions/web-1105-*.md.
- **App:** Desktop/MockMob-build-19 (mockmob-1.0.21+19-sells.aab, upload key 62:AC:58:08...EC:47, 16 KB aligned; arm64 APK; OWNER-STEPS.md, README.txt). Branch ui/1105-app-19 (c34db6b69) pushed. New: subject options at onboarding and You > Subjects, Learn's chosen-option line, the card turn's lift and light. Suite 12,469 pass / 111 known old golden drift. His step: upload 19 (it replaces 18).
- **Not verified:** a real phone; signed-in hero states in a browser; app onboarding on the emulator (the demo is always signed in; goldens cover it).
- **Next (LK98, until morning):** more refinement passes on the web and the app; content only when everything else is done and he is away.

## 5 Nov 2026, about 3:45 am IST: night refinement under way (his 2:40 am live-site look, LK81-LK98); slow-phone fix done, seven build packets running
- **His words:** verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md ("5 Nov 2026, about 2:40 am"); ledger LK81-LK98. Keep refining the web and app until morning; then a Play build and the live site; when all of it is done and he is away, add content.
- **Done:** LK81 slow-phone stutter on branch web/1105-perf (0c21de817): held stories drawn while the page is idle (storyPredraw.mjs), the tour keeps its screens mounted, pausing restyles only what animates. 22-swipe bench at 4x CPU: frames over 100 ms 11 -> 0, worst 442 -> 91 ms, p95 24 -> 12 ms. Not live yet (ships with the night's merge).
- **Spec:** docs/brain/night-1105/SPEC.md on web/1105-perf (682712138): D1 CTAs Sign up free / Log in lead, "Try 5 questions first" second, a two-key dock that never changes; D2 the "CUET 2027." line; D3 even lines; D4 the statement's green words back; D5 opening/typing/PrepOS polish; D6 exam screen faithful NTA mode with the real URL inside a desktop mock-up; D7 the demo-jump loop (edge clamp on the landing frame), a quiet arrival, DU section without the reveal gap, fast-scroll hunt; D8 web account pop-over like the app's Account sheet; D9 subject options asked at onboarding (the options, table and Learn picker already exist); D10 card turn lift; app build 19.
- **Running:** workflow wf_8325864d-cee, packets P1 hero (wt-1105-hero), P2 brand (wt-1105-brand), P3 exam (wt-1105-exam), P4 scroll (wt-1105-scroll), P5 account (wt-1105-account), P6 options (wt-1105-options), P7 app (wt-1105-app, branch ui/1105-app-19).
- **Next:** review each packet's renders, merge into one branch, full gate (tests, lint, both builds, gesture matrix, perf, 390/1440 Night/Day critique), ship to main; app emulator walk and 1.0.21+19 AAB in Desktop/MockMob-build-19.

## 5 Nov 2026, about 12:35 am IST: Play build 1.0.20+18 ready for his upload; the new home page (Desk Light) shipped to www.mockmob.in
- **App:** Desktop/MockMob-build-18: mockmob-1.0.20+18-sells.aab (upload key, SHA-256 62:AC:58:08...EC:47, 16 KB aligned), arm64 APK, symbols, OWNER-STEPS.md with release notes. Branch ui/1103-app-18 at c93a34c95, pushed. Contains LK50-LK53, LK42, LK60, LK61, the card look, the bug-review fixes and the emulator-walk fixes. Full suite 12,438 pass, 114 = known old golden drift. His step: upload to Play closed testing (OWNER-STEPS.md).
- **Web:** main 09a5bbe39 (deploy dpl_4PEoVBRVjXEXg6kHvyMZi55K3fUF): the Desk Light home page (LK67-LK75: words-first hero with a typed line and Mobi handing the first question on phone and desktop, the "mo" opening, warm Night without neon, one gesture = one step, the real exam screen, shorter copy, one Mobi finish, a state-aware centred dock) and the Learn walk fixes. Gate: tests (only known failures), eslint, both builds, L-checklist 40 pass, gesture matrix all pass, LCP 0.9-1.2 s at 4x CPU. Left: a one-time first-draw hitch of the Lab and tour sections at 4x CPU (10-11 frames over 100 ms); no real-phone check yet; Instagram post cards without captions.
- **Owner words today:** LK77 (status, ETA), LK78 (backup push already done), LK79 (what is deployed), LK80 (speed up, deploy everything, as perfect as it can be).
- **Next:** his upload of 1.0.20+18 and his look at the live home page on his phone (Night and Day); then the Lab/tour first-draw performance follow-up; LK36 content gaps; Saved on phones; the app's switch labels.

## 4 Nov 2026, about 4:55 am IST: one session; web Learn fix live; app 1.0.20+18 fixed and settled, emulator walk running; home page spec written, build running
- **Live:** main ced6f747f (dpl_DP3B34H1NjgFudfSbiVWzxk3onaf READY, no runtime errors): the ratings coach line is true for every card ("Each key shows when this card comes back: Missed it soonest, Easy latest."), a feed checkpoint and its Stop here end show one count (no zero), the run's deck edges are whole cards.
- **App (ui/1103-app-18 at acd7be66d, not pushed yet):** WIP settle edits taken (b3c3507a7); all 5 medium and 5 of 6 low review findings fixed with tests (sync: 6e9d589f8 via ui/1104-app-sync; Learn: 65be52363, 42fa00a88); explore-learn-calm-3 left (needs a server field, not a regression). Goldens re-recorded and looked at; full suite 12,428 pass, 111 fail = the known old drift only. Emulator walk (Day, Night, text 1.3, Pro and Free) running; then bump to 1.0.20+18, signed AAB with --sell, Desktop/MockMob-build-18.
- **Home page (LK67-LK75):** audit, scroll forensics (real touch: a fling's speed decides how many steps it skips; a gesture-owned controller gave one step in 32 of 32 bench cases), brand inventory done; three designs with mock-ups, three judges (brand-first "Desk Light" best for owner fidelity 8.2 and anti-slop 8.0). The CTO's spec: docs/brain/handoff-1104/home-spec/SPEC-HOME-1104.md (19 decisions: words first with a one-pass typed line, Mobi hosting the first question on phone and desktop, the app's "mo" opening as a 1.3-1.6 s skippable loader, Night on the app's warm charcoal with volt only as fills, the real MockMob exam screen with an NTA-style switch, copy cut to about 2,000 words, one Mobi finish). Five build packets running on web/1104-polish, then integration and the full gate, then ship.

## 4 Nov 2026, about 3 am IST: stopped at his order (usage ~95%); web live, app 1.0.20+18 merged but not built; home page research started
- **Live:** main 5df0c1c72: Physics 1,403 cards; the new Key card look, top-bar capsule, Up next, Find's sets on Learn home, brand icons, English (web). No runtime errors.
- **App:** ui/1103-app-18 at 6079162d5 holds every app change (LK50-LK53, LK42, LK60, LK61, card look). A bug review found 5 medium and 6 low issues plus the version bump; none fixed yet. Not walked, not built. WIP of a stopped agent: wip/1104-app-settle-partial.
- **Home page (LK67-LK76):** his words recorded; Preparoo study and a 40-tell AI-slop checklist done (handoff-1104/home-research); audit, scroll forensics and brand inventory stopped part-way; no design or build yet.
- **Next session:** paste PROMPT-NEXT-SESSION-2026-11-04.md; full state in HANDOFF-2026-11-04-SINGLE-SESSION.md.

## 4 Nov 2026, about 12:05 am IST: new account, one session; Physics live; final Play build and live website in progress (LK63-LK66)
- **His words (3 Nov ~11:55 pm), verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md:** finish every lane, review the UI against his past feedback until satisfied, then NO prototype links or test builds: a final AAB he uploads to Play and the final web changes on www.mockmob.in; commit all uncommitted work for handover/onboarding. Ledger LK63-LK66. His message was cut off at "Everything then should be sent to" (asked).
- **Live:** main dadc12807 = Physics 1,090 to 1,403 cards (312 typeset; ~7.2 h), deployment dpl_HmnRzrJPoKdNYyjuxw3YSwHVhEze READY, no runtime errors.
- **Running (subagents of this one session):** app test fixes on ui/1103-app-18; a stronger Key card look on web/1103-webfull (merged with web/1103-icons at 867376462: Up next module, Find's sets, top-bar capsule, brand icons); English table, web half, on web/1104-english; top bar + brand icons ported to the app on ui/1104-app-look; WIP snapshot commits of old worktrees on their own branches (none pushed).
- **Next:** merge, gate, ship the web to main; app English + card look port, emulator walk, 1.0.20+18 AAB in Desktop/MockMob-build-18.

## 3 Nov 2026, about 9:15 pm IST: all work stopped for the move to a new account; one session from here on
- His words: stop everything; hand off to a new account where everything happens in a single session, with workflows or
  subagents for parallel work (no sub-sessions, no forks). Full state and next steps: HANDOFF-2026-11-03-SINGLE-SESSION.md;
  paste-ready prompt: PROMPT-NEW-ACCOUNT-2026-11-03.md.
- Live: main f0186302f. Unfinished: Physics formula cards (reviewed, not published), app 1.0.20+18 (branches, 4 new test
  failures), web prototypes awaiting his look, English rewrite table.

## 3 Nov 2026, about 3:15 pm IST: STOPPED by the owner; feedback LK55-LK62 recorded; he restarts the PC, then we continue
- His words verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md ("3 Nov 2026, about 3:15 pm"); ledger LK55-LK62. "Don't start doing anything right now. Just record everything that I said."
- Live: main f0186302f (Mathematics 548, fonts self-hosted, LK37 run choices). Nothing of the Key cards session is running.
- After the restart: dev servers and agents are gone; LAN preview address is the Wi-Fi one, 192.168.1.8 (not .15, the Ethernet address the firewall blocks).

## 3 Nov 2026, about 2:45 pm IST: Mathematics 548 live (all 13 NCERT chapters typeset); fonts self-hosted, so the Vercel font failure is gone
- **Live:** main 4006a7c04 (app port session's LK37 run choices, on top of 29b001d8e). 29b001d8e = Mathematics 349 to 548 (221 typeset cards; the other 10 chapters plus a fix round, each card through an Opus formula reviewer against the page image and a Sonnet content reviewer) and Bricolage, Gabarito, Hanken and Literata served from src/app/fonts. Both builds READY on the first try; no runtime errors; no Google Fonts requests.
- **Mathematics: about 2.9 hours** (data/learn/seconds.js), just under his 3-hour bar. NCERT's 2026-27 text supports about this much: Application of Integrals and Probability Distributions were cut by NCERT (coverage notes), and the four Applied Maths chapters have no NCERT book.
- **Queued:** rework of two Probability formulas written as fractions of long phrases (they scroll on a phone); ncert-books/pages to delete after it.
- **Needs his answer (running list):** the app port session's three questions (top bar live look at http://192.168.1.15:3463/preview/arena?view=dashboard&plan=pro, same Wi-Fi; Saved one tap or inside Explore; "Practise | Papers | Learn | Explore" in the app), LK36 gaps 1-3, Physics formula pipeline, Applied Maths source.

## 3 Nov 2026, about 1:45 pm IST: Maths formula cards pushed (Mathematics 349); 10 more chapters being written; app feedback LK50-LK53 with the app port session
- **His words (3 Nov ~1:30 pm), verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md:** the app looks good but the UI can be better in many places; a stuck "Sending your answers · Computer Science mock" strip on every screen of his main account (LK50); no Explore ("Flow") feed in the app (LK51); Learn still cluttered (LK52); stronger, more premium, in the direction of Duolingo (LK53). "Continue doing all that"; he answers questions when back in 30-40 minutes. His stop of 2 Nov ~11:20 am is lifted.
- **Pushed:** main 2152e0b74 = typeset Maths formulas on Key cards (KaTeX 0.19.0, server-drawn, readable plain text for the app), Mathematics 310 to 349 (Inverse Trigonometric Functions 21, Probability 29, Application of Integrals 11), Geist Mono self-hosted. Deploy check below in STATUS once READY.
- **Running:** workflow wf_87f52d2b-817 writes formula cards for the other 10 Maths chapters (Sonnet author, Opus formula reviewer against the page image, Sonnet content reviewer each). Then: check-drafts-mtex-1102.mjs, merge-mtex-reviews-1102.mjs, publish, look, push.
- **App (LK50-LK53):** handed to the app port session (local_3c5cb01e) with the diagnosis of the stuck strip (a stale local draft keeps pendingSubmission after its submit window, or after the token refresher gave up). Ends in 1.0.20+18 for him to upload.
- **Needs his answer (running list):**
  1. LK36 gaps: (1) English reading-comprehension cards (~200, authored like the vocabulary cards), (2) Financial Markets from NCERT's 2022 edition, (3) Computerised Accounting from NCERT's CAS book (a PDF download). Any of 1-3?
  2. Physics: the same formula pipeline could recover the ~400 Physics cards held for flattened notation. Start it?
  3. The four Applied Maths chapters have no NCERT book; leave them, or name a source?

## 2 Nov 2026, about 9:50 am IST: +668 Key cards live (15,469); Maths formula pipeline started on his yes; app 1.0.19+17 waiting for his upload
- **Live:** main a16fbd62e, deployment dpl_8XasSMKTRgwwiwN6CXtVc5UtuvkW (first build passed). /, /learn, /explore, /today, /pricing, /api/stats and a Computer Science cards page answer 200.
- **Recovery round 2:** 1,003 held cards (876 held as ambiguous, 127 Computer Science front wording) were fixed and re-reviewed independently; 668 passed. Computer Science 1,544, History 1,587, Geography 1,345, Sociology 1,190, Chemistry 1,411, Physics 1,090, Psychology 826, Mathematics 310, Accountancy 920. No published card removed or changed.
- **His words (2 Nov morning), verbatim:** "Yes, start it" (to: start the Maths formula card pipeline). Later: "Can you give me an update on what has been running over the past 24 hours? ... check the logs, check what all is done and what's left, and then give me a status update on everything that's left or something that has not even been done yet?" Answered in the session with the full list (58 open ledger rows untouched in two days; Today is the suggested next area).
- **Maths formula pipeline (LK34):** spec handoff-1102/MATHTEX-SPEC.md, author brief handoff-1102/MATHTEX-AUTHOR-BRIEF.md. A card may carry `tex` (LaTeX of its front/back), checked by machine (KaTeX parse; same letters and digits as the PDF-checked back) and by an independent reviewer against the page image; the server sends the app and search a readable Unicode version. Code on web/1102-mathtex (wt-1101-r2-home), pilot lemh102, then 12 chapters. Page images: ncert-books/pages (43 MB; delete after the wave). Backups: ncert-books/drafts-bak-mtex-1102, reviews-bak-mtex-1102.
- **LK25:** 1.0.19+17 is built and signed for him: C:/Users/atish/Desktop/MockMob-build-17/mockmob-1.0.19+17-sells.aab (steps in OWNER-STEPS.md there). His step: upload to Play closed testing, then check Learn on his phone.
- **Decisions waiting on him:** the app keeps its navigation (the web's four equal tabs, LK26, are not in the app); the stop sheet counts acted items ("3 of 18 done") while the end screen counts seen items ("9 of 18 done"). Self-hosting Geist Mono goes in the next release unless he says no.

## 2 Nov 2026, about 4:40 am IST: +911 Key cards (14,801): wording recovery, English to 650, Accountancy thin chapters (LK34)
- **Live:** main e120b004d, deployment dpl_4WjR4cqaxDCjgKuWZn8ct4f8Qcts (a redeploy: the first build of this commit failed on the Geist Mono font fetch, as one did at 4:15 am). No runtime errors; /, /learn, /explore, /today, /pricing, /api/stats and the English, Accountancy and History chapter pages answer 200. Rollback: dpl_9D1LG3MWRpJ6qB6DCWpBic8a4NLQ (main feb30935e).
- **What students get:**
  - 663 cards that were held back only for front wording are back, re-cut and checked by an independent reviewer: Chemistry +97, Geography +76, History +79, Mathematics +30, Physics +112, Psychology +52, Sociology +119.
  - English 350 to 650 (word meanings, idioms, one-word substitutions, confused words, grammar rules): about 3.2 h, above his 3-hour bar.
  - Accountancy 866 to 912: Change in Profit Sharing Ratio, Retirement & Death, Analysis of Financial Statements, Comparative & Common Size Statements.
  - No published card was removed or changed.
- **Per subject now:** Accountancy 912, Biology 1,394, Business Studies 901, Chemistry 1,354, Computer Science 1,350, Economics 1,195, English 650, Geography 1,238, History 1,497, Mathematics 290, Physics 1,044, Political Science 1,096, Psychology 778, Sociology 1,102.
- **Still short:** Mathematics (290 cards, about 2 h). The formula pipeline waits for his yes.
- **LK25:** the app port session was resumed at about 4:40 am with the web changes since 1 Nov (rounds 2-4, Key cards for every subject) and the plan: finish its walk, align with LK24-LK33, emulator walk, release AAB for him to upload.
- **Reliability:** 2 of 4 Vercel builds today failed fetching Geist Mono from Google Fonts. A redeploy passes. The lasting fix (self-host the font) is proposed, not done.
- **Next (scheduled in this session for 8:27 am, after the 8:20 am usage reset):** recovery round 2. 1,003 held cards: 876 held only as ambiguous, plus 127 Computer Science cards held only for front wording. They go through the same fix and independent re-review: handoff-1102/recovery2-1102.js, args in recovery2-args-1102.json, guards check-drafts-r2-1102.mjs and merge-reviews4-1102.mjs. If the session has ended, a new one runs it from those files.

## 2 Nov 2026, about 4:15 am IST: Computer Science Key cards live (LK34); a recovery round and the English top-up are being checked
- **Live:** main feb30935e, deployment dpl_9D1LG3MWRpJ6qB6DCWpBic8a4NLQ. No runtime errors; /, /learn, /explore, /today, /pricing and a Computer Science chapter page answer 200.
  - The first deploy of this commit (dpl_3mveaRtzPDRYTRTnZFSQGsy6bpaA) failed when the build could not fetch the Geist Mono font from Google Fonts; a redeploy of the same commit passed.
  - Rollback: dpl_8B5HtwbPkxUfDXTKa5UeBzyTdd8F (main 7f1b204a7).
- **Computer Science:** 1,350 cards across 18 chapters, from Computer Science XII Ch 1-12 and Informatics Practices XII Ch 1-7; 567 held back. Project Based Learning (CS Ch 13) is outside CUET Section B1, so it has no cards.
- **Blanks:** a comma or bracket that touches a blank now stays on its line (1,087 fronts had one; a line could start with ", and").
- **Every subject now has Key cards (13,890):** Accountancy 866, Biology 1,394, Business Studies 901, Chemistry 1,257, Computer Science 1,350, Economics 1,195, English 350, Geography 1,162, History 1,418, Mathematics 260, Physics 932, Political Science 1,096, Psychology 726, Sociology 983.
- **Short of his 3-hour bar:** Mathematics (about 2 h; needs the formula pipeline, offered to him) and English (about 1.7 h; the top-up below adds about 300).
- **In progress (next release):** workflow recovery-topup-1102 (handoff-1102/recovery-topup-1102.js).
  - 778 cards held back only for front wording (It/This openings, over-long fronts) are being fixed and re-reviewed by an independent reviewer.
  - English: 322 new cards written, 22 flagged. Accountancy thin chapters: 80 new, 34 flagged.
  - Then: handoff-1102/check-drafts-1102.mjs, merge-reviews3-1102.mjs, review-merge, validate per subject, tier, suites, a look, build, deploy.
- **LK25:** the app port session (Port Learn v2 and the Explore feed to the app) stopped on 1 Nov at about 3 pm at the old account's usage limit, before its emulator walk. It has not resumed.

## 2 Nov 2026, about 4 am IST: Physics and Mathematics Key cards live (LK34); Maths is thin
- **Live:** main 7f1b204a7, deployment dpl_8B5HtwbPkxUfDXTKa5UeBzyTdd8F. No runtime errors.
- **Physics:** 932 cards across 14 chapters.
- **Mathematics:** 260 cards across 14 chapters, about 2 hours of study. That is below his 3-hour bar.
  - Some chapters are very thin: Three Dimensional Geometry has 1 card; Inverse Trigonometric Functions and Vector Algebra have 5 each.
  - Why: the PDF text flattens formulas, so maths cards were limited to definitions and theorems in words.
  - The fix is a follow-up job: transcribe NCERT's formulas from the page images into LaTeX and draw them on the cards.
- **Still being written:** Computer Science.

## 2 Nov 2026, about 3:40 am IST: Geography, Psychology and Sociology Key cards are live too (LK34)
- **Live:** main 26e5f359a, deployment dpl_6hhcRyXQwLwtknmeVNiL1aDbyuqQ. No runtime errors.
- **New subjects:**
  - Geography: 1,162 cards, 17 chapters
  - Psychology: 726 cards, 7 chapters
  - Sociology: 983 cards, 14 chapters
- **With Chemistry and History, live since about 3 am:** 5 new subjects and 5,546 new cards.
- **Still being written:** Physics, Mathematics, Computer Science.

## 2 Nov 2026, about 3 am IST: Chemistry and History Key cards are live (LK34)
- **Live:** main 90679d8c0, deployment dpl_Bb2sB56bG5wADahBaBkiQvzAQEyh. No runtime errors; rollback is the previous deployment.
- **Chemistry:** 1,257 cards from 10 NCERT chapters.
  - Formulas are drawn as real chemistry (CH₃OH, [Co(NH₃)₆]³⁺, 3d⁸).
  - I looked at them on screen.
- **History:** 1,418 cards from 12 NCERT chapters.
- **Both subjects:** exact NCERT text with book, chapter and page. Each chapter was checked by an independent reviewer, and the cards it flagged are held back.
- **Being written now:**
  - Geography, Psychology and Sociology
  - Physics, Mathematics and Computer Science
  - Physics and Maths cards hold only text that reads right without formulas, because extraction flattens powers and fractions.

## 1 Nov 2026, about 11:55 pm IST: Learn v2 rounds 2 to 4 are live (his LK24-LK33)
- **Live:** main 668341aea, deployment dpl_kmM3Rym59riGDcmQ1MVgRzs9RbGa.
  - No runtime errors.
  - The pages answer 200.
  - /api/stats is served from the CDN cache.
  - Rollback: dpl_DoGHp6AAWaCKngaFxKAckyhq7vAy.
- **What he will see:**
  - **Learn:** opens with a start offer and no zeros, one subject picker on phones, Free rows show each chapter's real size, chapters are named "Chapter 5 of 14", and "Needs work · from your papers".
  - **Cards:** read like flashcards, with the next card peeking and a one-time swipe chip.
  - **Ends:** short, with the keys at the bottom. Free gets one true line: questions come back tomorrow, Key cards stay open.
  - **Today:** for a new student, no false history and no zeros, and the start key is above the dock.
  - **Home hero:** the headline stays still.
- **How it was checked:**
  - 3 rounds of fixes.
  - Round 3 was reviewed by 5 lenses, and every serious finding was checked by 1 to 3 skeptics (docs/brain/learn-1031/r4/R3-REVIEW-FINDINGS.md in the web repo).
  - The suites, lint and build passed.
  - 180 screenshots, which I looked at.
- **Not checked:** a real phone, a trackpad, or a screen reader. He should look on his phone.
- **Cards (LK34, subscription):**
  - Chemistry (1,257) and History (1,418) are published on branch web/1101-content. They are not live yet: the chemistry formulas need a look first.
  - Geography: 15 of 17 chapters are written.
  - Next: Physics, Mathematics, Psychology, Computer Science and Sociology, after the 1:50 am usage reset.
- **Open:**
  - LK25, the Play release, waits on the app port session's emulator walk.
  - The Day hero poster needs a repaint (an image job).
  - Practice may say 15 chapters on the live site if the chapters table holds Computerised Accounting.

## 1 Nov 2026, about 4:15 pm IST: his first live feedback on Learn v2 (LK24-LK35); round 2 starting
- **His words:** verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md (1 Nov, about 4:05 pm). Items LK24-LK35 are in the ledger.
- **What he asked for:**
  - the phone website is cluttered and slow
  - Learn leads with a real start offer, not zeros
  - first-time cues (the feed swipe)
  - less blank space and fewer walls of text on end screens
  - a home hero that is more branded, tighter and reacts to taps
  - content for every subject (3 hours or more each)
  - a fresh Play release when the app update is ready
  - keep going
- **Done since he went live:** the stop-sheet count fix, web/1031-learn-v2 584542985 (not pushed). Live: main 978edc236, with no runtime errors.

## 1 Nov 2026, about 1 pm IST: Learn v2 and the Explore feed are LIVE (switches on)
- Owner applied the migration (dry run OK, then apply); verified by read: both tables, both functions, flow_context learn, no anon read.
- LEARN2_ENABLED=true, NEXT_PUBLIC_LEARN2=on (Vercel production); main 978edc236 READY (dpl_DoGHp6AAWaCKngaFxKAckyhq7vAy).
  /api/learn/* now answers 401 signed out (on); /learn/c/<key> renders; no runtime errors. Off = set both off and redeploy.
- Next: the owner tests live and gives feedback (he saw bugs on the local server); fix round after his list.

## 1 Nov 2026, about 12:30 pm IST: Learn v2 code is LIVE with its switches off; the owner applies the migration next
- **Owner:** "Ship it", then: he wants it live to test everything properly; "mostly loved the direction"; refinement and fixes after
  deploy. He still has feedback from the local server (it was a bit buggy there).
- **Live:** main 106e53720 on mockmob.in (Vercel dpl_4KiFy8nhFkomrN5pgA3H1284MF5k, READY). Switches off: /api/learn/* answers 404
  LEARN_OFF, /learn/run, /explore/run and /learn/c/* serve the not-found page, the v1 Key cards API is unchanged, no runtime errors.
  The Learn v2 nav (Learn, Key cards first; the Start sheet's Learn a chapter) is gated too (cf552bac8), so the live nav is unchanged.
- **Blocked for agents:** the production migration (the auto-mode classifier denied even the rolled-back dry run). The owner runs
  wt-1031-learn-v2/supabase/dryrun/20261101150000_learn_runs.dryrun.sql, then supabase/migrations/20261101150000_learn_runs.sql in the
  Supabase SQL editor (project isrxrxzjocewrdureyhp). Read-only pre-checks passed; question_interactions is about 3,500 rows.
- **Then:** set LEARN2_ENABLED=true and NEXT_PUBLIC_LEARN2=on (Vercel, production) and redeploy; NOT before the migration (a redeploy
  with the switches on and no tables would break every Learn run). Then smoke test, his test, his feedback.
- **App port:** session local_3c5cb01e (Port Learn v2 and the Explore feed to the app) started by the owner.

## 1 Nov 2026, about 6:20 am IST: Learn v2 and the Explore feed built completely (LK20-LK23); waiting for his look
- **Branch web/1031-learn-v2 (wt-1031-learn-v2), not pushed or deployed.** Spec BUILD-1101.md; audits A1-A8, 00-critic, 09-final-critic in
  docs/brain/learn-1031/audit-1101/. Commits: 06d7b40f5 e61e5517e e8e6d3c0c 0cd13b463 978699f89 2e90b5be7 f684d507a eea222a3f ee3f61abe
  e36c92f4f 6bffc64c2 153f534e9 ea6543d7d d9afdf8e8 2be498715 1bfd86ee9 4bba8db6f.
- **What is built:** real pager (one wheel notch, swipe or key = one item; slow drag works; visible Previous and one named volt key),
  desktop session panel, cards that fit their words, the line in place, covers that show each chapter's own opening card, Learn home
  with search and shelves, chapter page, run on the same stage, stop sheet, ends with real numbers, watermarked v2 print sheet,
  production service + 11 /api/learn routes behind LEARN2_ENABLED, pages behind NEXT_PUBLIC_LEARN2, one Key cards world when on.
- **Verified:** final capture 182 stills at 1440/1366x650/1024/390/360, Night (Day at 1440/390), 0 console errors, 0 sideways scroll; wheel,
  trackpad, keys and touch measures pass; owner-eye critic M1-M10 fixed (1bfd86ee9). Not verified: real phone or trackpad, screen reader,
  real Ctrl+P margins; the two films predate the last fixes.
- **Owner links (LAN, this PC on):** http://192.168.1.15:3451/preview/arena?decks=real&study=on&view=learn2-feed&plan=pro&student=commerce&chapter=accountancy.admission-of-partner&min=10
  (also view=explore, view=learn2&subject=accountancy, view=learn2-chapter&chapter=accountancy.admission-of-partner). Owner set:
  wt-1031-learn-v2/tmp/learn-1101/for-owner/.
- **Needs him:** his look and verdict; confirm the CTO decisions (Keep = add to Revise; realistic seconds; LK15 claimed at the first answer,
  Free clamped to 10 min, second Free run cards only; no Must-know tag on feed/run cards; chapter page keeps the subject object); content
  calls (duplicate card "Define partnership." vs "What is partnership?"; the card "If this amount is paid..." reads oddly alone); to ship:
  run supabase/dryrun/20261101150000_learn_runs.dryrun.sql, then apply the migration, approve merge + deploy, set LEARN2_ENABLED=true and
  NEXT_PUBLIC_LEARN2=on; then the app port (A7, stale in places; the web is the source of truth).

## 1 Nov 2026, about 3:45 am IST: Learn v2 built for production behind flags; UI rebuild running
- **Branch web/1031-learn-v2 (wt-1031-learn-v2), not pushed or deployed.** Spec: docs/brain/learn-1031/BUILD-1101.md in that worktree
  (logic Part 1, production Part 2, UI Part B with B7 decisions); audits in docs/brain/learn-1031/audit-1101/ (A1-A8).
- **Done:** S2a service + 11 /api/learn routes behind LEARN2_ENABLED (06d7b40f5); S2b migration 20261101150000_learn_runs.sql with undo and
  PGlite test, saved only, never applied (e61e5517e); S1 engine rules: honest Keep, feed moves forward, resume, slot-first order, realistic
  seconds, LK15 claimed at the first answered question (e8e6d3c0c); P production pages behind NEXT_PUBLIC_LEARN2, no shell flash (0cd13b463).
  test:learn 133/133, test:keycards 81/81.
- **Running:** workflow learn-build-1101-ui: U1 feed (real pager: one swipe, wheel notch or key = one item; visible Previous and a named volt
  key; desktop session panel) and shared study parts; U2 covers (the opening card as the cover, no repeated object); U3 Learn home; U4 chapter
  page and run; S3 server fields. Then capture, critique and fix rounds, the owner's phone link.
- **Owner decisions taken by the CTO (he can override):** Keep = add to Revise (no fake rating); realistic seconds (about 12 cards and
  5 questions in 10 min); LK15 counts chapter runs and feeds, claimed at the first answer, Free clamped to 10 min with a line; a second
  Free run that day is Key cards only. Needs him later: apply the migration after the dry run; turn the two flags on; the app port.

## 1 Nov 2026, about 1:30 am IST: his look at the feed prototype (LK20-LK23); full build under way
- **His look (on a computer):** likes the feed direction, but on a PC there is no way to the next item and too much blank space (LK20); loves the
  Explore covers, but every Accountancy cover shows the same object (LK21); the chapter run is "quite good" but needs a lot of refinement (LK22).
- **His task (LK23):** build the feature completely now, test everything, fix every issue, refine the UI/UX and the logic, make it more useful; then tell
  him what is needed from him and his next steps.
- **Running:** workflow learn-map-1101 (logic audit, production wiring plan, Flutter app map) and learn-ui-audit-1101 (desktop and phone captures in
  wt-1031-learn-v2/tmp/learn-1101/audit, then audits A1-A4, A8 and a critic); reports go to wt-1031-learn-v2/docs/brain/learn-1031/audit-1101/.
  Then the main session writes the refinement spec, and build, capture, critique and fix rounds follow.

## 1 Nov 2026, about 12 am IST: nav v2 rejected; building the Explore feed v2 live prototype
- **Nav v2 rejected:** he says the current structure is cleaner, so it was reverted on web/1031-learn-v2 (60a7071e4, b54885382).
- **Building:** a phone-first Explore feed per learn-1031/FEED-2.md:
  - full-screen swipe-up items, cards that flip, Keep, the wrong-answer sheet, a checkpoint and an end screen;
  - Explore chapter covers;
  - Find as a search field in Learn.
- **Phone link:** he will open it on his phone over the LAN at http://192.168.1.15:3451. allowedDevOrigins was added in e723aaf4a.

## 31 Oct 2026, about 11:30 pm IST: the owner answered A9 and N1
- **A9 (LK15):** feed and Learn questions are free up to a limit. The rule is one free Learn session a day, up to 10 minutes. Not built yet.
- **N1 (LK16):** Learn becomes its own section, but the app bar cannot grow. NAV-2.md is on branch web/1031-learn-v2:
  - On the website, Learn is a place in the sidebar.
  - On phones, the Practice tab gets a Practice/Learn title switch.
  - An agent is rendering it as `&nav=n2`.
- **LK17:** he could not see any change because nothing is deployed. The local preview (port 3451) was opened in his browser pane.

## 31 Oct 2026, about 9:45 pm IST: Learn redesign renders sent to the owner
- **Sent:** 11 real renders and a run video (wt-1031-learn-v2/tmp/learn-1031/for-owner/), from branch web/1031-learn-v2
  (commits 5af8f8a2f slice, a47da5caf merge of the live release, b9bc5fe80 and the volt-quiet fix). Full set of 143 captures in
  tmp/learn-1031/final2; critique docs/brain/learn-1031/CRITIQUE-1.md (all four blockers fixed).
- **Must-know:** one overlay only, the live data/keycards/tiers.json (12 of 46 in Basic Concepts; 229 in Accountancy).
- **Checks:** test:learn 43/43, test:keycards 76/76, test:app 986 pass 2 fail (heroScene landing tests, also failing on main), lint clean.
- **Open:** E4 deck content (two near-duplicate opening definition cards, both Must-know; one Ch 1 card cites Ch 2), E6 Free
  "Your papers" fixture count, R9 Explore chapter label "Partnership Fundamentals", /learn/run as a focus route. Not wired
  to production yet (Supabase-backed /api/learn routes), no app parity yet.
- **Owner next:** his look at the renders; A9 (questions free inside Learn) and N1 (Learn as its own desktop sidebar place).

## 31 Oct 2026, about 6:55 pm IST: Learn feedback (LK1-LK14): fixes live, redesign in preview
- **Live (main b7e68f8e2):** Your part picker fixed (LK2); Study motion (LK5); MockMob watermark on every printed sheet (LK6);
  Must-know re-tiered to 25% via data/keycards/tiers.json (LK13). Suites, build and captures in STATUS.md.
- **Building (not live):** the Learn redesign as real screens in the dev preview: `wt-1031-learn-v2` (branch web/1031-learn-v2),
  spec `docs/brain/learn-1031/DESIGN-SPEC.md` (concept B "the chapter is the home" plus amendments A1-A12), data contract
  `API-CONTRACT.md`, workflow learn-v2-slice (engine, home, chapter page with piles, run player, cards view, Explore feed,
  then capture, Opus critique, fix). Dev server: .claude/launch.json "learn-v2-dev" on port 3451.
- **Owner next:** see the real renders when they land; decide whether questions inside Learn are free (A9) and whether
  Learn gets its own desktop sidebar place (N1). App version 17 can wait for the redesign.

## 31 Oct 2026, about 4:50 pm IST: 218 off-syllabus questions pulled
- **Owner:** "Pull them all". The 218 are off-syllabus, pending and frozen on production (dry-run, then applied; undo saved).
- **Bug fixed on the way:** the morning's 25 flawed-question pulls were still served (pending, but verified and active
  is still visible). They are frozen now. Visible questions 8,571 to 8,328.
- **Thin now:** Accountancy, Financial Statements of Company, 1 question; Political Science, Recent Issues and
  Challenges, 4.
- **Record:** STATUS.md on main 0149bf45b; `docs/brain/intel-1031/off-syllabus-2026-10-31/` on main.
- **Owner next:** app version 17 build; open /cards signed in once; say if Accountancy should get new questions.

## 31 Oct 2026, about 1:35 pm IST: Key cards ON for students
- **Flag:** the owner said "Turn it on". KEY_CARDS_ENABLED=true and redeployed (dpl_7dHWVGYYCxR753iJ8wW6Ppgaoyx4).
- **Smoke:** the routes answer 401 signed out; no errors. The signed-in flow on production is not yet seen by anyone.
- **Owner next:** decide on the 218 outside-syllabus questions; app version 17 build.

## 31 Oct 2026, about 1:20 pm IST: Key cards release LIVE with the flag off; syllabus v2 and Key cards migrations applied
- **Live:** main 5c1d03a37, dpl_jzeVzYF2yT6F8EwUQxM9EcnPvPau.
- **Database:** syllabus v2 plus its live-rows fix and the Key cards tables are applied; 561 re-tags; 59 flawed questions fixed.
- **Pools:** Biology 369, Chemistry 395, Political Science 252.
- **Record and undo:** STATUS.md on main.
- **Owner next:** see the screens, turn KEY_CARDS_ENABLED on, decide on the 218 outside-syllabus questions, build app version 17.

## 31 Oct 2026, about 1:00 pm IST: Key cards hardened, content grown, question pools audited; owner steps ready
- **Live production is unchanged** (main 0b7d6bc03). Nothing pushed, deployed or written to production. The session's
  permission check blocks production writes, so every production step is saved with its undo for the owner.
- **Web integration** `web/1031-keycards` 5c1d03a37. The merge to main is a fast-forward.
  - Code review fixed: 4 high, 6 medium, 12 low.
  - Screens polished against the real decks.
  - Content: 5,800 cards, 2,144 linked questions; 18 conflict cards and 49 duplicates held back.
  - Mocks: at most 2 copies of one template stem per paper.
- **App** `ui/1031-keycards`: walked on the emulator with real cards; fixes plus web display parity.
- **Pool audit** of 2,875 live questions: 515 wrong chapter (476 verified re-tags ready), 218 outside CUET 2026,
  50 flawed (59 fix-or-pull SQLs ready), and about 849 Accountancy template copies.
- Read `docs/brain/HANDOFF-2026-10-31-KEYCARDS-3.md`.

## 31 Oct 2026, about 6:00 am IST: Key cards built end to end on branches; waiting for the owner's look
- **Live production is unchanged** (main 0b7d6bc03). Nothing pushed, deployed or written to production.
- **Web integration** `web/1031-keycards` 90fddb40d: syllabus v2, Key cards server, web screens, 5,721 published NCERT
  cards in 6 subjects (137 quarantined), 1,632 question links, re-tag file. All suites green; webpack build passes.
- **App** `ui/1031-keycards` bb4da376b: done and tested; no device walk yet.
- **Owner decisions waiting:** see the screens; turn `KEY_CARDS_ENABLED` on; accept the pool shrink when syllabus v2
  retires 440 questions (Biology -18%, Chemistry -15%, Computer Science -14%).
- Read `docs/brain/HANDOFF-2026-10-31-KEYCARDS-2.md`. Next prompt: `docs/brain/PROMPT-NEXT-SESSION-2026-10-31.md`.

## 31 Oct 2026, about 3:45 am IST: Key cards build PAUSED at the owner's 93% usage
- **Live production is unchanged** since the version 16 web release (main 0b7d6bc03). Nothing from this work is pushed
  or deployed.
- **Work in progress:** Key cards (NCERT exact-quote flashcards), syllabus v2 (CUET-referenced) and chapter state.
  - Owner decisions: D200-D206.
  - Read `docs/brain/HANDOFF-2026-10-31-KEYCARDS.md`. Next prompt: `docs/brain/PROMPT-NEXT-SESSION-2026-10-31.md`.

(Older state below.)


**Last written:** 20 Oct 2026, about 3:20 am IST (updated from 2:35 am), by session 801f0d1a (Claude Opus 5.5, CEO/CTO). The owner is asleep with FULL AUTONOMY for this session (D156: decide independently, no mock-ups or results to show, deploy when tests pass). His words are verbatim in `docs/brain/OWNER-FEEDBACK-2026-10-19.md` (to D157 and I1-I16, J1-J6). Decisions: `OWNER-MASTER-LEDGER.md` (C-dec 3 and 3b at the end).

## 1. Vision (stable)
CUET UG 2027 prep for 16-17-year-olds. USP: unlimited mocks from one central bank. Score Recovery (find, fix, check the fix holds); Ask Mobi; the Mob. Premium, alive, smart. **The website is the main product** (D157); the app follows. Version 13 is the closed-test first impression for 14-15 testers starting 20 Oct (D155): no bugs, exceed expectations.

## 2. Rules in force
R1-R8 (PLAN-1019 section 0). D150 build-and-look loop (agents capture visuals while building). D156 autonomy for this session. D157: Pro does NOT make Mobi free; credits bought mostly by Pro students; depth over volume; keep AI margins wide. Never sign in from a staging build (C1: it reached production; guard now in ui/v17-bugs). Production writes allowed this session only for the Mob v3 go-live (D152) and what the owner named.

## 3. Live now
- **Web v13 + Mob v3 LIVE (3:13 am, D152):** main 65afa5d0, deployment dpl_4nA9juLKE9wFKjPHRAcdtfx7Ffha (rollback point dpl_F8qxHxpnXyZPqjCEAFrPrBbSnE9L). Mob v3 migrations core/games/chains/realtime applied on production (recorded as 20261019213134-213528), MOB_V3_ENABLED=true in Vercel Production, MOB_LIVE_ENABLED unset. Includes web Mob den/play, web Pro page + Wallet (J1/J3), /app/login email link page, assetlinks from ANDROID_CERT_SHA256 (unset: returns []), no email-prefix names. Smoke clean, 0 runtime errors.
- **Web:** main 58793f9c = Play subscriptions LIVE (PLAY_BILLING_ENABLED=true set by him; deploy dpl_F8qxHxpnXyZPqjCEAFrPrBbSnE9L; RTDN works). Production migration 20261019210000 applied 9:51 pm. Licence-tester purchase proven end to end (Pro, 4 renewals, 50-credit pack, refund+revoke). Stray test auth user chai-fresh@example.com deleted (D151).
- **Play Console:** listing uploaded (v11b text option A, feature graphic A, screenshot set 2 from Desktop\MockMob-store-listing\UPLOAD-THIS); internal testing has version 11 (link showed "Item not found": Google propagation; he used other routes); closed testing Alpha has version 11 IN REVIEW. Version 12 built (Desktop\MockMob-build-12) and SKIPPED by him (D154). Pro price shows Rs 150 (he set 150; D136 said 149; his call). Content rating (users interact: yes; purchases: yes) and Data safety (Purchase history) still need his update before Alpha review completes.

## 4. Version 13 in flight (all local, nothing pushed)
**App** base ui/v16-1020 2485e83e (= v12). Branches (each its own worktree wt-1020-*):
- done: ui/v17-bugs 6b659e43 (Ask Mobi ties, API origin guard C1, email App Link /app/login + verifyOTP, G13), ui/v17-mob-switch 449e8fde (MobRead v3Available/serverV3, MOB_V3_ENABLED default on), ui/v17-mob-art 9cc7e7dc (moments order, FINAL FOLDS art: idle/cheer/think, parcel, seal; shrug/wave fall back to idle), ui/v17-mob-den 6ea7f777 (H1/H2/H5/M1 etc.), ui/v17-mob-play e8a0d38e (H4 race, H6 podium, M2, M5), ui/v17-pro-page 6cb1c9d2 (full-screen Pro page /you/pro, owner J1/J2 applied).
- still working: ui/v17-wallet (owner J3: packs as Mobi answers/repairs), ui/v17-finish (SWOT-style paper read = Mobi's debrief + full-mock reveal), ui/v17-mobi + web/v13-mobi (Ask Mobi value per C-dec 3b: Where you stand, Fix it for good, doubt threads, mentor reads colleges).
- **Integrator** (Sonnet) building ui/v17-release in wt-1020-app-rel: merges bugs, mob-switch, mob-art, mob-den, mob-play, pro-page; full tests; demo-mode emulator walk; screenshots tmp/walk-1020/app-v13. Then wallet, finish, mobi to merge.
**Web** base web/1019pm-mob-v3 e2eb2462 (Mob v3 server + live main + v3Available). Branches: web/1020-fixes 55bcbad0 (app sign-in link page, assetlinks from ANDROID_CERT_SHA256, no email-prefix names), web/v13-mob-den 2e3cea79, web/v13-mob-play 8757518d, web/v13-money afea69dd (Pro page + Wallet, J1/J3). **Integrator** (Sonnet) building web/v13-release in wt-1020-web-rel (+ server folds.mjs colours); web/v13-mobi to merge after.

## 4b. In flight at 3:20 am
- App integrator: ui/v17-release (wt-1020-app-rel) has bugs, mob-switch, mob-art, mob-den, mob-play, pro-page merged (d915d22d); merging ui/v17-wallet 536de4b5, ui/v17-finish 6fdfff26, ui/v17-mobi (wt-1020-mobi); then full tests, demo walk, signed build 1.0.16+13 to Desktop\MockMob-build-13.
- Web Mobi deployer: merging web/v13-mobi (wt-1020-web-mobi) into wt-1020-web-rel at 65afa5d0, suites, push main, smoke, STATUS.
- Mobi owner finishing app tests on ui/v17-mobi.
- Handoff prompt for a fresh account: docs/brain/NEXT-PROMPT-1020-AM.md.

## 5. Next (in order, autonomous)
1. Finish merges (app ui/v17-release, web web/v13-release) incl. wallet, finish, mobi; full suites (app unit ~7k, web test:mob/billing/recovery/auth/app/subjects, next build --webpack).
2. Adversarial review per surface (Mob, money, finish, sign-in), fix wave.
3. GO LIVE (D152): pre-check prod; apply Mob v3 migrations 20261020100000 core, 100100 games, 100200 chains, 100300 realtime (files in wt-1019pm-mobsrv supabase/migrations, undo in supabase/undo); set MOB_V3_ENABLED=true in Vercel Production (MCP create_project_env; if blocked, note for owner); push web/v13-release to origin main (fast-forward from 58793f9c? it is a merge descendant: check `git merge-base --is-ancestor origin/main HEAD`); Vercel check; smoke (/, /mob, /pricing, /wallet, /api/mob 401). STATUS entry with undo.
4. Build version 13: bump to 1.0.16+13 (or 1.0.17+13), `bash tool/build_release_aab.sh --bump --sell` in the release worktree (copy MockMob-keys\key.properties to android\ if missing), APK too, emulator launch check, copy to Desktop\MockMob-build-13.
5. Folds shrug/wave: Codex account 2 resets 5:38 am (account 1 after 2:58 am); commands in tmp/design-1019pm/mob-v3/characters/final/FINAL-ART.md section 6; then `python tool/fold_manifest_final.py` in the app.
6. Morning summary to the owner: what is live, version 13 path, what he must do (upload v13 to closed testing, content rating + data safety, ANDROID_CERT_SHA256 = Play app-signing SHA-256 in Vercel for the email link).
7. Follow-ups: 150 vs 50 welcome credits (his decision); weekly Mob paper answer hold (C-dec 2 item 1); Mob live rooms (Phase B); Ask Mobi remaining capabilities (ASK-MOBI-VALUE.md); golden baseline drift (~110 stale goldens at base).

## 6. Commands and facts
Flutter: `MOCKMOB_FLUTTER_SLOTS=6 bash tool/flutter_locked.sh <args>` (slot max file %TEMP%\mockmob-flutter.lock.max = 6). Emulator lock %TEMP%\mm-emu-lock; AVD mockmob_budget -memory 3072; adb -e only; demo entry test/device_demo/demo_main.dart. Staging rig: 3104 (r11, shim 3114), 3105 (Mob v3 server, shim 3115), seed scripts/mob/seed-v3-staging.mjs (chai-* @example.com). Supabase prod isrxrxzjocewrdureyhp, staging onwkqxmjqjrhfbjjdydu. Vercel prj_uSolddribHQDl1mM5AKxg3O9qCIu / team_V5PhMz9hqV42vblUMcvhYqoN (env listing may be blocked by the permission classifier). Upload key fingerprint SHA-256 62:AC:58:08:...:EC:47. Codex images: account 2 signed in now.


## HANDOFF 20 Oct about 4:00 am (D159): every agent STOPPED; exact leftovers
- **Live (done):** main 48985a8d (deployment dpl_GNLLoKcKYZDo34nkpXbqMqnT5WSs): Play billing, web v13, Mob v3 (4 migrations on prod, MOB_V3_ENABLED on), Ask Mobi v13 web (credits buy jobs, Pro still pays, no migration). Rollback points: dpl_4nA9juLKE9wFKjPHRAcdtfx7Ffha (before Mobi), dpl_F8qxHxpnXyZPqjCEAFrPrBbSnE9L (before Mob v3).
- **App release ui/v17-release (wt-1020-app-rel) head 72af5155, clean:** merged bugs 6b659e43, mob-switch 449e8fde, mob-art 9cc7e7dc, mob-den 6ea7f777, mob-play e8a0d38e, pro-page 6cb1c9d2, wallet 536de4b5, finish 6fdfff26 (+ golden regenerations on the merged Folds art). pubspec still 1.0.16+12. NOT done: merge ui/v17-mobi; full unit run after the last three merges; demo emulator walk; version 13 build (Desktop\MockMob-build-13 does not exist yet).
- **ui/v17-mobi (wt-1020-mobi) head 096fa2db = STOP POINT** over 758b4547 (Where you stand, doubt thread, Fix it for good, goldens): its last 3 files were uncommitted work of a helper (App Ask Mobi v13 UI) stopped mid-way: review before merging.
- **Folds art:** idle, cheer, think for all 12 + parcel + seal are in the app (mob-art) and web (public/mob/folds); shrug, wave, Patang think redo NOT generated (FINAL-ART.md section 6; Codex account 2 resets 5:38 am).
- **Web leftovers (from the den/play owners):** D6 den room skeleton not wired; public /join/<code> page not v3-aware; sticker flights not live; podium first-place Fold head touches the lamp edge; signed-in walk of live Mobi flows not done (agents never sign in).
- **Owner steps:** upload v13 to Alpha; content rating + Data safety; ANDROID_CERT_SHA256; 150 vs 50 credits; Pro 149/150.
- **Next prompt:** docs/brain/NEXT-PROMPT-1020-AM.md (goal-first, 5-6 hour plan).

## PAUSE 20 Oct 5:30 am (session 604ced81, account usage 90%; window resets 9:00 am IST): every agent STOPPED, every dirty worktree has a STOP POINT commit
Blitz (D160/D161) results, all local branches, nothing pushed or deployed since main 48985a8d:
- **App v13 release** ui/v17-release (wt-1020-app-rel) 668df841 = STOP POINT over f345ebee (Ask Mobi v13 merged at e52a9490; uncommitted Wallet/Mob copy fixes were in progress: review; Wallet text still said "2 real CUET questions"/"Mobi job"). ui/v17-mobi finished at 361abc62. NOT done: full unit run on the final tree, demo walk completion (wt-1020-app-walk f345ebee has demo work), signed build 1.0.16+13, Desktop\MockMob-build-13.
- **Fix lists:** tmp/review-1020/FIX-WAVE-LENSES-1020.md (66 items; build blockers L-01..L-12, B-SUBMIT L-07b/L-08, live hotfixes L-09 blocking across Mobs, L-10 share-marks switch leak); per-surface reviews tmp/review-1020/*.md (FIX-WAVE-1020.md synthesis was stopped; merge the surface files).
- **Web branches ready to integrate (from 48985a8d, tested by their owners):** web/1020-web-practice-parity 6f4dde82, web/1020-web-goal-more eb37f6d5 (needs web/1020-goal-minutes fa635fc5 server + migration on prod), web/1020-web-subject-pages b2024553 (15 CUET pages; 9 subjects' copy needs one read), web/1020-web-onboarding-parity e22f7d34, web/1020-web-live-client fbbb8433 (behind live flag), web/1020-mob-polish 7bc2dd02, web/1020-join-v3 4a10d0f3, web/1020-set-password c3dfc2b4, web/1020-landing-health a68aba16, web/1020-paper-hold 54ff19a5 (+ app ui/1020-paper-hold 422811e1), web/1020-mob-live 6b0cf827 (Phase B server). Expect conflicts on Today (practice-parity strip vs onboarding name card) and subject pages vs landing.
- **App side branches:** ui/1020-small-fixes ba19dbbb, ui/1020-mob-live 99f5fde0 (STOP POINT). Marketing: mkt/1020-folds-kit 3d284a11. Analyses: check docs/brain/DECISION-WELCOME-CREDITS.md, OWNER-STEPS-1020.md, docs/design-decisions/pass-1020/MOBI-NEXT.md, Desktop\MockMob-store-listing\LISTING-v13.txt, tmp/walk-1020/GOLDEN-DRIFT.md (exist only if their agents finished).
- **Next after 9:00 am:** (1) one app owner: fix build blockers L-01..L-12 on ui/v17-release, full unit, demo walk, build v13 to Desktop\MockMob-build-13; (2) one web integrator: merge the web branches above into web/1020-release, suites, deploy (D156) with smoke + STATUS, plus L-08 legal pages and L-09/L-10 hotfixes; (3) Folds shrug/wave via Codex; (4) morning summary. Keep waves small: the blitz burnt about 80% of a window in 80 minutes.

## MORNING 20 Oct 11:05 am (session 604ced81): goal met
- **Version 13 ready:** C:\Users\atish\Desktop\MockMob-build-13 (mockmob-1.0.16+13-sells.aab SHA-256 cfc2dd9e..., mockmob-1.0.16+13-arm64.apk 50b459d6..., README, symbols, OWNER-STEPS.md). Built from ui/v17-release 19ac295b (head fe076156 adds goldens only). Signer = upload key 62:AC:58:08...EC:47. Blockers L-01..L-12 fixed; Folds shrug 12/12, wave 11/12 (Stamp wave missing, idle fallback); full unit+widget 7,337 pass; 454 intended goldens regenerated; 17 golden failures not from this release (4 Mob title cut at text 1.3 = real older bug B1; 13 noise/clock); demo walk ~75 shots (tmp/walk-1020/app-v13/r2, JUDGEMENTS.txt), 6 findings fixed; launch check on an x86_64 twin (emulator cannot run arm64).
- **Web live:** main 36492ed2 (dpl_8EU7duoJuwKFQuU8WEe5uPWyGhT9; rollback dpl_6uV9Z3cLWcFeHGcXcpBx85fJxn1M): hotfixes L-09, L-10, L-01 server, L-08 legal pages, L-07b from=app; 13 branches merged (practice/colleges parity, goal More + daily_minutes migration 20261020110000 on prod with undo, 15 CUET subject pages, onboarding parity, mob polish, join v3, set password, landing health, paper hold, live rooms code with MOB_LIVE_ENABLED off), Folds shrug/wave on web. Not applied: 20261020100400_mob_v3_live (live off until presence fix L-55). Today shows "Your colleges" twice (strip + older card), kept per his D126 "the block stays": revisit.
- **Docs for him:** docs/brain/DECISION-WELCOME-CREDITS.md (recommend 50: drop the one-time 100 signup grant), OWNER-STEPS-1020.md (= Desktop\MockMob-build-13\OWNER-STEPS.md), Desktop\MockMob-store-listing\LISTING-v13.txt, docs/design-decisions/pass-1020/MOBI-NEXT.md, docs/marketing/FOLDS-LAUNCH-KIT.md (branch mkt/1020-folds-kit).
- **Open:** Stamp wave pose; B1 Mob title at large text; Mob live rooms (presence fix L-55, migration 100400, Realtime public access off, his go); app live client ui/1020-mob-live STOP POINT 99f5fde0; ANDROID_CERT_SHA256 (his); remaining MEDIUM/LOW items in tmp/review-1020; welcome credits and Pro 149/150 (his decisions).

## 20 Oct ~12:30 pm: owner Play/Vercel steps DONE
Version 11 approved on the closed track; version 13 sent for review (he sent it before reading the steps; fine). Content rating redone (interact yes, digital purchases yes, no loot boxes, online/AI content yes, educational yes); Data safety Purchase history added. ANDROID_CERT_SHA256 set in Vercel Production and redeployed (dpl_13vbidun9MJtWKaNPub88Hj5NfSY): live assetlinks.json lists the Play app-signing key B2:45:68:DA:...:05:C9 and the upload key 62:AC:58:08:...:EC:47. Pro on Play stays Rs 149; welcome bonus 100 kept (150 total). Play "Automatic protection" (block unofficial installs) is ON: testers install from Play, not the APK. Next: his feedback on version 13; then the improvement list (real-device walk, Folds life, live rooms, remaining review items, smart layer).

## HANDOFF 20 Oct PM (session 604ced81, written ~3:45 pm at account usage 85%, context 86%)
His words today: OWNER-FEEDBACK-2026-10-19.md from "Owner, 20 Oct about 12:05 pm IST" (K1-K11, D165-D176).

**LIVE (production):**
- Website main bd9e03ea7 (code fb1e22e5, deployment dpl_2juF25MkVrVzCqrWFMXDwiGMHjBP; a docs-only build dpl_Fo9PLU76SS13bfLGP4sHbDXqKk1A was still BUILDING: confirm it reaches READY with FIRST_FULL_MOCK_ENABLED=false). Contains: the 11 am release (36492ed2), referral credits (2ffaf29d, REFERRALS_ENABLED=true; 50 welcome, +100 each after the friend's 5 answers; migration referrals applied, total credit_balance unchanged 112311/1545 users), web Mob explainer, Mob formats server + web client with MOB_FORMATS_ENABLED and MOB_LIVE_ENABLED UNSET; migrations 20261020095603 mob_v3_live and 20261020095712 mob_v3_formats applied (hashes match).
- D175: FIRST_FULL_MOCK_ENABLED=false (env aldFAoz9qJXBPpAQ): no free first full mock; /pricing line gone.
- ANDROID_CERT_SHA256 set (Play key B2:45:68:DA...05:C9 + upload key); assetlinks live.
- App version 13 (1.0.16+13) in closed-testing review (version 11 approved). Play Console: content rating redone, data safety Purchase history added.

**SUPABASE (URGENT, K11/D176):** org xnhuqcazqyqvnsodmqyf egress 14.42 GB of 5.5 GB (Free); grace until 22 Oct, then 402s on production AND staging until the quota refills at the next billing cycle (or an upgrade). Owner refuses $25 Pro during testing. Cause: staging (onwkqxmjqjrhfbjjdydu) is in the SAME org and agent walks, seeds and test runs hammered it; no weekly usage check. Done: agents told not to use staging. Waiting on him: billing-cycle end date (Billing > Upcoming invoice) and egress split per project (Usage > Egress). Next: move staging to its own free org (dashboard project transfer, he clicks); cut production egress (top queries, select only needed columns, caching); add a usage check to every session; never run agent walks against staging until the new cycle; if the cycle resets after ~22 Oct, tell him plainly the outage window and that Pro for one month (downgrade after reset, credited) is the only instant fix.

**APP BRANCHES (all from ui/v17-release fe076156 = version 13 source; none merged; nothing on a phone yet):**
- ui/1020-v14-polish 44073e9f (wt-1020-v14-polish): K1 Day mode, K3 You plan strip (credits + Upgrade to Pro), K4 Pro table, K6 Wallet; done, tests green. MUST change: remove "your first in each subject is free" copy (D175).
- ui/1020-finish-reveal 0942a34e (wt-1020-finish-reveal): K7 mark-sheet reveal on every paper; done, 7,138 tests. Remove any first-free wording.
- ui/1020-referrals ed2a8b93 (wt-1020-referrals-app): D165 app side; done.
- ui/1020-mob-explainer 1a7a622c (wt-1020-mob-explainer): D166/K9 explainer + one-question setup; builder STOPPED at 3:45 pm (usage 90%) just before its demo-mode emulator walk; code, tests and walk fixes 1-2 committed. Left: the demo walk of the explainer and setup, then merge.
- ui/1020-mob-formats d1d2c095 = STOP POINT (wt-1020-mob-formats-app; 12 files were uncommitted): race, Full mock together and the live client in the one Start a game sheet; stopped at 3:45 pm while writing the race goldens and frame strips. Review the STOP POINT diff, finish the goldens and frame strips, full unit, then merge.
- ui/1020-mob-live 99f5fde0 STOP POINT (merged into mob-formats as its live base); ui/1020-small-fixes ba19dbbb; ui/1020-paper-hold 422811e1.

**DECISIONS WAITING / OPEN:**
- Mob V4 (docs/design-decisions/pass-1020/MOB-MINIMAL.md "MOB-V4"; mock-ups tmp/design-1020/mob-minimal): APPROVED to build (D174), with Mob hours YES, a clear Pro call to action for Free members in Full mock together, both streaks visible, results as a short sequence plus celebration screens. NOT built yet.
- Full mock together rule: Pro starts; Free members pay 50 credits (no free first mock now, D175); Pro sits free. The SERVER currently lets everyone sit free: enforce the rule before MOB_FORMATS_ENABLED=true.
- Live rooms: owner must turn OFF Supabase Realtime "Allow public access"; app live client must ship; then MOB_LIVE_ENABLED=true.
- Stamp's wave pose and a desk-lamp image still to generate (Codex image route, FINAL-ART.md section 6).

**NEXT (in order):** (1) Supabase egress plan above. (2) Version 15: merge v14-polish, finish-reveal, referrals, explainer, mob-formats (+ small-fixes, paper-hold) into a v15 branch; remove first-free copy; build Mob V4; full analyze + unit + touched goldens; demo-mode walk only (NO staging); signed build to Desktop\MockMob-build-15. (3) Enforce the Full mock together pricing on the server, then MOB_FORMATS_ENABLED=true. (4) Live rooms after his Realtime click.
- **Supabase update (3:35 pm):** his Billing page shows the overage was in the PREVIOUS cycle and the last invoice is 21 Sep, so the cycle resets on the 21st: the quota refills 21 Oct, before the grace ends 22 Oct. Most likely no outage and no payment. BUT no second grace: the cycle 21 Oct-21 Nov must stay under 5 GB egress (~160 MB/day). He is confirming the "Upcoming invoice" date and sending the per-project egress split.

- **All agents STOPPED at 3:45 pm (usage 90%).** Leftover Dart processes and the emulator were killed; the emulator lock was removed. Web explainer branch web/1020-mob-explainer c4546a70 is already merged and live.

## SESSION b7e1b5da, 20 Oct from 4:06 pm (goal: version 15 to Play review tonight, D179/D180)
- **Supabase (parked, D178):** cycle 21 Sep-21 Oct confirmed (refills 21 Oct, grace ends 22 Oct); org egress 15.72 GB; spikes 7 Oct 3.8 GB and 18 Oct 3.3 GB were agent days. Staging transfer to org `mockmob-staging` is BLOCKED during grace: owner retries 22 Oct afternoon. Staging rig on 3104 killed 4:10 pm; no staging traffic since 5:30 am. D177 plan in OWNER-FEEDBACK. Egress cut: workflow on web/1020-egress (wt-1020-egress), first commit 2340ccb2d (inventory skip-if-unchanged), not deployed yet.
- **Live:** main 85c715756 = D175 hotfix (pricing comparison row no longer promises a free first mock), deployed and checked 5:17 pm.
- **Server:** web/1020-mob-fulltogether-price 185eaaf2b (wt-1020-fulltogether): Pro starts, Free sits for 50 credits, Pro free; contract APP-API-CONTRACT 2.12 (camelCase: v3.starts.mock, game.price, MOCK_PRO_REQUIRED 403, MOCK_CREDITS 402); test:mob 308, billing 448, build ok. Not merged/deployed.
- **App v15 base:** ui/1020-v15 (wt-1020-v15app), agent v15-integrator: merged small-fixes, paper-hold, referrals, v14-polish, finish-reveal, mob-explainer; D175 copy removal + full unit in progress.
- **Mob modes:** ui/1020-mob-formats (wt-1020-mob-formats-app), agent mob-formats-finisher: a5142e33f pricing client; aligning to the final camelCase contract.
- **Mob V4:** spec docs/design-decisions/pass-1020/MOB-V4-BUILD.md; branches ui/1020-v4-den (29283d0f1 part 1), ui/1020-v4-sheets, ui/1020-v4-results (all from a5142e33f), web/1020-mob-hours (Mob hours server at v3.hours). Workflows wf_0a2d44a4-ae6 (results track) and wf_6cde204f-70c (den, sheets, hours restart); coordination file tmp/v4-coord.md (agents never SendMessage each other: it wakes duplicates).
- **Owner feedback sweep:** workflow wf_4fa546de-309 writes tmp/review-1020/V15-OWNER-SWEEP.md (fix packages for after integration).
- **Next:** merge mob-formats + V4 branches into ui/1020-v15; sweep fix wave; full analyze/unit/goldens; demo-mode emulator walk Night+Day; signed build 1.0.17+15 to Desktop\MockMob-build-15; then web release (fulltogether price, Mob hours migration, V4 web, egress cut, MOB_FORMATS_ENABLED after price is live).

## PAUSE 20 Oct 6:28 pm (session b7e1b5da, account usage 91%): every agent STOPPED; exact stop points
Owner switches accounts; THIS session resumes (same session). Never SendMessage to workflow agents (wakes duplicates); coordination file tmp/v4-coord.md.
- **ui/1020-v15** (wt-1020-v15app) 18aa9341c: 6 merges + D175 copy removal (72906a94d) + goldens. Clean. Integrator was stopped before its final full unit report: re-run full analyze + unit.
- **ui/1020-mob-formats** (wt-1020-mob-formats-app) d97a2e167 DONE: races, Full mock together on the final camelCase contract (sit sheet, Pro CTA, MOCK_PRO_REQUIRED/MOCK_CREDITS), live client. Full suite 9,802 pass / 141 fail = 140 old non-Mob golden drift + 1 fixed motion guard.
- **ui/1020-v4-den** (wt-1020-v4-den) 70f9a64b0: den built + review fixes (two fixer runs). Clean. Needs: final look at goldens vs mock-ups, the friend-join/reaction/desk act calls (API from results track, see v4-coord.md), ResultsRun.showPending on den open.
- **ui/1020-v4-sheets** (wt-1020-v4-sheets) 4e61e9209: sheets built + review fixes. Clean.
- **ui/1020-v4-results** (wt-1020-v4-results) STOP POINT 8ac38ab9f over 5ded98382: reviewer fixes 1-3 committed (eyes without seams, X to den, rule box in view); fixes 4+ (Fix it together headline/one key, parallel reads + loading frame, podium your-place card + 3.5 s), A9 lobby For-you card, haptics, hours crown/ticks, 4.3 frame strips, acts API were IN PROGRESS: review the STOP POINT diff (tmp/review-1020/V4-RESULTS-REVIEW.json has the fix list).
- **ui/1020-v15-calm** (wt-1020-v15-calm) STOP POINT 2b78a0576: D181 first Pro ask waits, D183 usage data on for Rather not say, delete-account Play warning; was on onboarding save_step copy. Finish + tests.
- **ui/1020-v15-invite** (wt-1020-v15-invite) STOP POINT d51a71625: Play Install Referrer + "Have a friend's code?" row + live flag + D182 copy; was opening goldens. Finish + tests + debug apk compile check.
- **web/1020-referral-any** dabbf31d6 DONE: D182 migration 20261020150000_referral_any_practice (+undo, NOT applied), Android /r/<code> -> Play referrer; billing 440, auth 125, app 962, build ok.
- **web/1020-mob-fulltogether-price** 185eaaf2b DONE. **web/1020-mob-hours** 25940b5f6 (two fix rounds; RENAME its migration 20261020150000_mob_hours -> 20261020151000 at web integration: version clash with referral-any).
- **web/1020-egress** STOP POINT d8c35687e over 8e5d00430: F1 inventory skip-if-unchanged + many A/F cuts; the workflow was in its fix stage; verification not done.
- **Next after the switch:** (1) finish v4-results, v15-calm, v15-invite (3 agents); (2) one integrator merges mob-formats, v4-den, v4-sheets, v4-results, v15-calm, v15-invite into ui/1020-v15, fixes Mob explainer slide 3 (K9: real modes, no "Coming soon"), full analyze + unit + touched goldens; (3) demo-mode emulator walk Night + Day with screenshots (tmp/walk-1020/app-v15), fix what it shows; (4) signed build 1.0.17+15 to Desktop\MockMob-build-15; (5) web release: merge fulltogether, referral-any, mob-hours, egress, V4 web; apply the three migrations with pre/post checks; MOB_FORMATS_ENABLED=true after price is live.
- **Next prompt for any agent (Codex or Claude):** docs/brain/NEXT-PROMPT-1020-EVE.md.

## PAUSE 20 Oct 7:11 pm (session e5b2f75b, account usage 91%): every agent STOPPED; exact stop points
Owner rules this evening: D185 (Get Pro, never "See Pro plans"; no text bombardment, visual first), D186 (sheet and slide 3 approved; NO regressions; check the brain when unclear), D187 (record findings in Continuum as they happen). Next prompt: docs/brain/NEXT-PROMPT-1020-NIGHT.md.
- **ui/1020-v15** (wt-1020-v15app) 717aa3a89, clean: merged ui/1020-mob-formats, ui/1020-v4-den, ui/1020-v4-sheets, ui/1020-v4-results + integration (den plays achievements through ResultsRun.showPending; Week stitched reads v3.hours; all six V4 sheets wired; How the Mob works -> explainer replay; Your Mobs Start another -> explainer/setup; den header chip fix; own game rows "Your sprint"); explainer slide 3 "Ways to play" (K9: Sprint, Race 5/10, Your own round, Full mock together, Every week box: Mob paper + Mob hours; no Coming soon); Sit the full mock sheet redesigned (D185, approved D186). `flutter analyze` clean; Mob unit+widget 712/712 pass. Goldens NOT yet regenerated on the merged tree (Mob v3 goldens drift from merges; ~140 old non-Mob goldens are known drift).
- **ui/1020-v15-invite** (wt-1020-v15-invite) 3e9eb69e6, clean: agent finished review commits (referrer read exactly as the website sends it, hardened claim, Android Play Store query in the manifest, wallet row room + goldens, claimer can never fail the first build). Its final report never arrived: re-run analyze + referrals/wallet tests; debug/release APK compile not confirmed.
- **ui/1020-v15-calm** (wt-1020-v15-calm) STOP POINT 353a98fc9 over 2b78a0576: the review agent's uncommitted work (74 files incl. new onboarding goldens) committed unreviewed; it was running the touched-area unit tests. Review the diff, run analyze + onboarding/pro_nudge/you/core_data/billing tests.
- **Not wired (follow-up, not a blocker):** den join/reaction acts (DenActPlayer in widgets/fold_acts.dart) into den_stage (desk act and sticker flights already run); A9 MockLobbyBody (the sit sheet is the lobby). v3.fix (den Now card steps 2-3) has no server field yet: those steps never show.
- **Emulator:** AVD mockmob_budget was booted at 6:56 pm by this session; lock %TEMP%\mm-emu-lock (owner file says e5b2f75b). A new session may take the lock over (one emulator only).
- **Next:** merge ui/1020-v15-calm and ui/1020-v15-invite into ui/1020-v15; analyze; full unit/widget; regenerate Mob goldens on the merged tree and open the changed ones; demo-mode walk Night + Day (360 dp, text 1.0 and 1.3) with screenshots in tmp/walk-1020/app-v15 + JUDGEMENTS.txt; fix; signed 1.0.17+15 to C:\Users\atish\Desktop\MockMob-build-15; then web release.

## 20 Oct NIGHT (session 604ced81, 7:18 pm to ~10:30 pm): version 15 finished in one window (owner D189, D190)
- **App, ui/1020-v15 9e6ad500f built (+ goldens-only commit after), version 1.0.17+15, signed AAB + arm64 APK in C:SERSTISHDESKTOPMOCKMOB-BUILD-15 (AAB SHA256 4BCA8F3C..., UPLOAD KEY 62:AC:58...). FULL SUITE 10,491 PASS, 117 FAIL = KNOWN GOLDEN DRIFT + 2 FLAKY; RELEASE X64 LAUNCH CHECK OK; FINAL DEMO WALK DEN/START/SIT/YOU/WALLET NIGHT+DAY OK.** Merged tonight on top of 717aa3a89: ui/1020-v15-invite (Have a friend's code row, Play install referrer), ui/1020-v15-calm reviewed by 20 agents then fixed (555d8e45f, 31bf4bb80: consent never promotes an age band, D181 first result per attempt id, returns to Today counted by the router, privacy unanswered key), ui/1020-v15-calm-ui (first-session Pro sheet visual first with renewal stated, save step age note one line; 6e1b5a239, 02a286aaa), ui/1020-den-acts (d58d15862: a friend who joined hops in, a sticker makes the Mob cheer), ui/1020-mob-polish (7 commits: chain chip beside the gear, Your Mob never cut (B1), Week stitched pennant hero, sit sheet price row flush, short Free start row with Pro starts it tag, Mob copy without "last", This week sheet), my copy fixes 8cc4c9add (Get Pro on Wallet and inline links, Rather not say everywhere, short Mob Pro ledes), motion guard 94623c2a9 (shared curves in Fold acts). Mob goldens regenerated 06dbe24a0 and judged against the mock-ups (tmp/v15-night/golden-judge.json).
- **Website, LIVE: main 7f7e3f19f** (release 2c71cb810 + STATUS): Full mock together price enforced on the server, referral after any one practice (D182), Mob hours, egress cuts (19 commits reviewed), v3.fix for the den Now card steps 2-3 (APP-API-CONTRACT 2.14), D183 consent on server + Profile + privacy policy (updated 20 Oct, parent route, crash reports disclosed). 7 migrations applied on production 9:00-9:15 pm (list and checks in STATUS.md). MOB_FORMATS_ENABLED=true (env xJZ4QrcRIdcShmYI). Rollback deployment dpl_4bn4VVutv4Lyxf2JE1yLyCMrTQVG.
- **Known drift (not regressions, proven on the base):** ~117 old golden images (onboarding ladder/rhythm/taste/balance, credits, tools, account sheet, rhythm, art scenes, etc.): tmp/v15-night/known-drift.txt. Flaky: run_r5_flag/run_r6_done (Kabir's eye 0.08%), billing_sub_renewal_off.
- **Follow-ups for the next session:** copy sweep of "lost"/"last" outside the Mob (Today "Repair your last paper", "You lost 99 marks in Goodwill", result "You lost N marks", ask doors); the den's studying chip timing in den_stage (StudyDesk, goldens only); web Mob V4 (MOB-MINIMAL W1-W7) and the web den fix card; MOB_LIVE_ENABLED after the owner turns off Supabase Realtime "Allow public access"; staging moves to its own org on 22 Oct; the stopped 4-build walk left 298 screenshots of build A in tmp/walk-1020/app-v15/A-formats-free (contact sheets in ../contact).

## HANDOFF 20 Oct 11:25 pm (session 604ced81, usage ~91%): version 15 closed, version 16 next
- Version 15 (1.0.17+15) is in Desktop\MockMob-build-15; the owner tested it on his phone (feedback 11:20 pm, D191). It is NOT being sent to review: version 16 (1.0.18+16) is the final closed-testing build, tonight.
- Owner findings on v15: the Mob explainer never plays automatically on a fresh account (it is wired only to Start/Join/See how it works); the invite card in credits shows at the wrong time; no welcome-credits + invite pop-up after sign-up; Live hidden (MOB_LIVE_ENABLED unset, waits for his Supabase Realtime switch); delete only records a request, so a "deleted" account kept working and showed odd credits (a fresh account showed 50 -> 39, correct).
- Website feedback (phone first): pricing revamp, "Get access for 99" like the app, hero like the app, subjects first with commerce preselected, scroll story bigger on phone with better copy, Mistake Lab timer animation frozen, bot screens need depth in dark mode, Razorpay monthly setup guidance.
- Next prompt: docs/brain/NEXT-PROMPT-1020-V16.md (copy on Desktop as NEXT-PROMPT-V16.md). The v15 verify prompt is withdrawn.

## 21 Oct 12:58 am (session b7e1b5da, Fable 5.1): version 16 in flight
- **Owner tonight:** D192 (Fable orchestrates), D193 (web ₹99), D194 (hero line stays), D195 (Realtime public access OFF; Razorpay plan id set as RAZORPAY_PLAN_ID_PRO_MONTHLY_99 on Vercel; MOB_LIVE_ENABLED=true set; webhook URL fixed to www). Plan: docs/brain/V16-PLAN.md.
- **App ui/1020-v16 (wt-1020-v16) eff27472d:** merged ui/1020-v16-nudges 879068666 (A4: rules by Fable + Opus card/sheet/facts; demo MOCKMOB_DEMO_NUDGE=<kind>), ui/1020-v16-welcome 4dad2e850 (A1 welcome-credits sheet + warmer invite copy; demo DEMO_WELCOME_CREDITS=true), ui/1020-v16-mobwelcome b93276a66 (A3 welcome room then explainer on the first Mob tab visit; demo MOB_V3_SCENARIO=fresh). Analyze clean. STILL RUNNING: ui/1020-v16-sweep (A2 invites/deletion clarity, A6 copy sweep, studying chip). Then: full unit suite, demo walks Night/Day, signed 1.0.18+16 to Desktop\MockMob-build-16.
- **Web web/1020-v16 (wt-1020-web16) dabf26d1c:** merged onboard c9ee1b5fe (W4), landing 864f7816d (W5/W6/W7), pricing ef5837ecb (W1/W2), hero 9156786a8 (W3), invite copy 7e410cc06, deletionRequestedAt in /api/auth/me 53c2022b7. Suites on the tree before hero: app 980, billing 453, mob 351, auth 125, recovery 637, landing 73, all green. Next: npm ci restore of mockmob-next/node_modules (my worktree removal followed junctions and emptied it, 12:42 am), then suites + eslint + build, browser check 390/1440 Night/Day, push main, smoke (monthly ₹99 + live rooms go live with it), STATUS entry.
- **Disk:** 1 GB free at 12:20 am -> 107 GB after deleting build output and 197 finished worktrees. scripts/sweep_build_output.sh (before builds, end of waves) and scripts/remove_worktree.sh (junction-safe). 21 dirty worktrees kept.
- **Open:** web hero phrase "See the lost marks." (approved rotation; width-pinned by tests) left for the owner's call like D194; web Wallet "opens the invite section" lands at the Wallet top; nudges and welcome need the emulator walk.

## 21 Oct 2:28 am: version 16 app at the test and walk stage
- **Website release 16 LIVE:** main 832e88031 + STATUS 0b7d6bc03 (deployment dpl_G17kKZkn2bw24a5SGL8xNaXHxv95, rollback dpl_HsKRboUQsi1oUdC8ffrWV9QsnHpT). Monthly ₹99 (RAZORPAY_PLAN_ID_PRO_MONTHLY_99) and live rooms (MOB_LIVE_ENABLED) on. Owner fixed the Razorpay webhook URL to www.
- **App ui/1020-v16 (wt-1020-v16):** 0fd6f644a merge of ui/1020-v16-sweep (A2 invites, deletion note, A6 copy sweep, studying tag) + referral goldens commit; analyze clean; full suite 10,638 pass / 118 fail (expected = known drift 111 + flaky; the rerun capturing failure names runs now: tmp/v16-unit-fails.txt). Signing inputs staged in wt-1020-v16/flutter_app (key.properties, prod.json; git-ignored).
- **Walk:** agent v16-walk in wt-1020-v16walk (ui/1020-v16-walk = 0fd6f644a): demo x64 builds (fresh + DEMO_WELCOME_CREDITS + MOB_V3_SCENARIO=fresh; MOCKMOB_DEMO_NUDGE kinds), Night and Day, screenshots to tmp/walk-1021/app-v16, JUDGEMENTS.txt.
- **Promo kit (D196/D197):** Desktop\MockMob-promo-kit (PROMPT.md price ₹99 only); another session (7a597d) is building the teaser in Claude Motion.
- **Next:** classify the 118 failures (regenerate only intended goldens; any real failure fixed), fix walk findings, bump to 1.0.18+16 with `bash tool/build_release_aab.sh --bump --name 1.0.18 --sell` (+ arm64 APK as in 20 Oct NIGHT), launch-check an x64 release APK, copy AAB/APK/README/symbols/OWNER-STEPS to Desktop\MockMob-build-16.
- Time-sense "last" ("since your last look", "in each of your last 3 mocks") stays: v13-approved and test-pinned; the rule is applied to "lost"/"behind"/"last place" senses.

## 21 Oct 3:52 am: VERSION 16 DONE (session b7e1b5da, Fable 5.1)
- **App 1.0.18+16 signed:** C:\Users\atish\Desktop\MockMob-build-16 (mockmob-1.0.18+16-sells.aab SHA-256 da7d67a7..., arm64 APK, symbols and mapping, README.txt, OWNER-STEPS.md). Built from ui/1020-v16 f72207c27 (tree dcd87253f + version bump). Owner uploads to Alpha (sent 3:52 am). x64 release launch check on the emulator: MainActivity up, no fatal exception (tmp/walk-1021/v16-release-launch.png).
- **Website release 16 live** (main 832e88031; STATUS entry 0b7d6bc03): see the STATUS entry; monthly ₹99 and live rooms on.
- **Evidence:** analyze clean; full suite 10,639 pass / 117 fail = known drift (tmp/v15-night/known-drift.txt) + start_v13_following_picked stale; demo walk 140 shots (tmp/walk-1021/app-v16, JUDGEMENTS.txt), no blockers, 3 high fixed; web suites green, build ok, browser QA no blockers.
- **Next session (owner's words tomorrow first):** the three medium walk items (explainer slides 3-6 text density; Today date at text 1.3; repairOpen note next to the repair hero); the web hero rotation phrase "See the lost marks." (owner's call, like D194); Day theme product cards on the website; dense /cuet pages; nudges and welcome sheet on a real account; Supabase staging transfer on 22 Oct afternoon (grace ends); Mob hours on the web; promo video (Desktop\MockMob-promo-kit, another session is cutting the teaser in Claude Motion).
- **Branches merged into ui/1020-v16:** nudges, welcome, mobwelcome, sweep, fixa (Wallet deep link), walk (Mob clips). Worktrees kept: wt-1020-v16 (app, final), wt-1020-web16 (web, = main), wt-1020-v15app/walk, wt-v15-3; the v16 side worktrees can be removed with scripts/remove_worktree.sh.
- **Disk:** 1 GB -> ~120 GB free; rules in scripts/sweep_build_output.sh and remove_worktree.sh (junction-safe). Owner's own: Documents\Wondershare 119 GB.


## 21 Nov 2026, 8:10 pm IST (orchestrator, Claude Fable 5.2): the owner's notes on the live home (LK365), round started

LIVE is still main 459b9dd3d (the new home, since 3:05 pm). Nothing from this round is committed yet.

His 12 items (ledger LK365): one-place rows too fast and unexplained; Ask Mobi as a film of the real flow (photograph the
paper, Mobi reads it, the read, the check, the practice); Learn, Benchmarks and the Mob shown working, not as paragraphs;
the Mistake Lab moves on the moment a scene ends and stacks like cards; the Daily Five rethought or removed; the streak
worth using; DU Compass never pauses by itself; pricing's subject picker (end numbers); an Android-only app nudge.

Decisions taken (orchestrator):
- Rows become captioned stories. `CursorDemo` steps now take `say` (the beat's line, reported through `onSay`) and `focus`
  (the stressed element carries `data-demo-focus`). Story contract and the round's rules: `wt-1110-convert/tmp/1121-stories/COMMON.md`.
  New story files go under `src/components/landing/stories/` with a dev-only harness (`StoryPreview.jsx`, pages
  `/preview/story-<id>`).
- Daily Five rethink = "Your five": a signed-in student's five are built from their own record (2 missed, 2 from weak
  chapters, 1 from their subjects), wrong picks feed their mistakes, the shared five stays for guests and the Android app.
  New route `GET /api/daily/mine`, no migration, kill switch `DAILY_MINE_ENABLED`, fail-soft to the shared five. Spec:
  `wt-1110-convert/tmp/1121-stories/DAILY-SPEC.md`; the server's shapes: `tmp/1121-stories/daily/CONTRACT.md`.
- Android nudge: the Play listing of in.mockmob.app answers 404 today (checked), so the nudge is built OFF behind the
  existing `PLAY_LISTING_PUBLIC` switch. It turns on when the owner sets that env value after the listing is public.
- Streak rewards with money value (credits, free mocks) are NOT built: proposals for the owner only.

Running: workflow `home-lk365` (run wf_5bacbd5a-f61), all agents Opus: four story lanes, frame, Android nudge, Lab,
Compass and picker, Daily server then review, page and home section, streak; then integrate, assemble (24 suites), three
critics, fixers, a final check. After it: the orchestrator's own look, the full gate in wt-1116-next, a fast-forward push.

## 22 Nov 2026, 12:48 AM IST (Codex orchestrator) — LK365 release 10ef17bf0

Production main 10ef17bf0814e95289a07dcc0af75f85269693e5 reached READY on Vercel (dpl_DHkEgAr4a281NV8gejZqH6kjTjgB) at 22 Nov 2026, 12:42 AM IST. Previous live deployment dpl_F3ukC8JMzgxQLNzsU1W8aXwCBfao at 459b9dd3d is the rollback target.

The release gate in wt-1116-next/tmp/gate2.log passed all 24 suites, ESLint, Webpack and Turbopack. The separate landing checklist passed 43 with 12 existing TODOs. Production Chrome smoke at 390×844 light, 360×676 dark and 1440×900 light confirmed Daily CTA hit testing, Compass autoplay and Pause, pricing edge taps and the hidden Android nudge. The live short-phone film reached all six rows in 12.6–14.5 seconds each with 26 of 26 cursor presses in the viewport and on the right controls. Its console had CSS preload warnings only. Compass on live Chrome at 390×844 with 6× CPU slowdown measured six frames over 50 ms out of 172 playing, versus zero out of 288 paused. Signed-out GET /api/daily/mine returned 401. Vercel had no [daily-mine] events and no /api/daily/mine error or fatal entries in the first 5 minutes 19 seconds after READY.

Your Five has no migration. The guest and Android shared five still use the existing routes. The college day average and Mob strip can aggregate personal and shared results across students. A shared answer from an older Android client receives its own grade after a personal run starts on web, with the account retaining the personal run. No signed-in production walkthrough was performed. Kill switch DAILY_MINE_ENABLED=false. The Android web nudge stays off while Play returns 404. Monetary streak rewards remain proposals only. No owner device or iPhone was checked.

### LK365 status board for the next feedback prompt

| Area | Status |
| --- | --- |
| **Done** | 12 of 12 implemented and checked. Six captioned home demos, auto-advancing stacked Mistake Lab, Your Five, phone streak chip, Compass autoplay, pricing edge taps and the Android nudge. |
| **Live** | `10ef17bf0` is READY on www.mockmob.in. All 24 suites, the landing checklist, ESLint and both builds passed. Chrome smoke checks passed at all three requested sizes. |
| **Left from LK365** | No implementation work remains. The Android nudge stays off while Google Play returns 404. A signed-in production Your Five run, the owner's phone and iPhone hardware remain unchecked. Cash-value streak rewards are proposals. |
| **Brain** | The LK365 ledger, NOW, UI audit and Continuum checkpoint agree. Ready for the next feedback prompt. |


## 22 Nov 2026, 1:25 am IST (orchestrator, Claude Fable 5.2): LK366, the owner's verdict on release 10ef17bf0, round in progress

LIVE is main 10ef17bf0 (LK365). Nothing from this round is committed yet. His words are in the ledger, row LK366.

What he likes (approved taste, keep): the captioned story direction of the one-place rows, the Ask Mobi film, the Mob story,
Benchmarks, the Lab's stacked cards with the automatic hand-off, the Compass tour that never pauses by itself.

What I measured before changing anything (phone 390x844, CPU 6x, films in `wt-1110-convert/tmp/1122-lk366/`):
- Practise and Key cards rows: hard olive outline boxes round whole groups with the rest dimmed to 0.4, 12 to 14 s a row.
- Mistake Lab: all five scenes over in 11 s (scene changes at about 2.0, 5.0, 9.0, 10.6 s). Device content clipped on a phone.
- Daily Five section: five layers of words, a card in a card, beats of about 3 s, the demo cut by the window's bottom.
- Compass bars: stepping in 10-point jumps with no transition (the 21 Nov jank fix removed it).

Decisions (orchestrator):
- Practise and Key cards: no stress boxes and no dimming on the two real screens; three beats each, about 10 s; the Key cards
  third line is now shown (the rated card is filed: "This card is back in 3 days." with a time line, `KeyCardsDemo.jsx`
  FILE_MS 1500). `ROW_MIN_MS` 8500; the four row stories keep 11 to 13 s.
- Ask Mobi first line: "Photograph a school or coaching question you got wrong." Learn lines 3 and 4: "Then a quick card
  checks you remember it." and "Miss one and that card comes back sooner."
- Android nudge: `/?appnudge=1` now previews it on an Android phone on the live site too (always drawn hidden; a note says
  the listing is not public). Without the query it still needs `PLAY_LISTING_PUBLIC=true`.
- Benchmarks checked: it is the real `/rival` screen (levels, timed run, result against the target) plus the Ranks standing.
- Three Opus lanes running: Lab pace (6.5 to 7.5 s a scene, nothing clipped on a phone), Daily Five (one surface, a plain
  sub line, four beats of 3.2 s or more, the demo always in view, no boxes), Compass (bars glide by transform again).
  Lane rules: `wt-1110-convert/tmp/1122-lk366/COMMON.md`.


## 22 Nov 2026, 2:23 AM IST (orchestrator, Claude Fable 5.2): LK366 released, main aa15bc996

LIVE = main aa15bc996 (fast-forward from 10ef17bf0, which is the rollback target). Gate in `wt-1116-next/tmp/gate2.log`: 24
suites at fail 0, eslint empty, webpack and turbopack build exit 0, DONE. Landing checklist by hand: 43 pass, 12 todo.
The outcome per item is in the ledger (row "LK366 outcome"). Evidence: `wt-1110-convert/tmp/1122-lk366/` (films before and
after, lane reports' sheets, `suites/`).

Things the next agent should know:
- Stress boxes are gone from the two real screens of the one-place frame (Practise, Key cards). The four row stories keep
  their own stress. `ROW_MIN_MS` is 8500. Do not bring boxes back: he called them wrong (LK366).
- The Lab's pace lives in `LAB_PACE` (`LabNextScreens.jsx`), pinned by `data/tests/lab_next_1121.test.mjs`. He found 11 s
  for five scenes unreadable and the 21 Nov afternoon pace (5.4 s a scene, 3 s of dead time) a bit slow; it is now about 7 s
  a scene with no dead time. The Lab also glides to its resting place when a reader stops with its heading in the top half
  of the window (LabCinema `held`): new, not yet judged by him.
- Compass bars: `makeGlide` in `CompassLadder.jsx` (Web Animations, transform only). A tour step writes words only.
- `/?appnudge=1` previews the Android nudge on the live site (Android phone browsers only).
- Open, his to decide: the Lab's glide (above); the college board and Mob strip mix personal and shared fives; money-value
  streak rewards; showing the CUET 2026 coverage; authoring the coverage gaps.
- Known, not fixed: under reduced motion ScrollStory's `fitAll` can measure before the display font loads and fit the
  Repair smaller at 360x676 (text smaller, not cut); a Compass row's words can lag its tick for a moment on a slow phone.


## 22 Nov 2026, 3:33 AM IST (orchestrator, Claude Fable 5.2): LK367 released, main 6ad2c7f63

LIVE = main 6ad2c7f63 (rollback aa15bc996). Outcome and open points: ledger row "LK367 outcome". Evidence: `wt-1110-convert/tmp/1122-lk366/` (films, cov-both.jpg, lab-nudge.jpg), gate log in `wt-1116-next/tmp/gate2.log`. Open with the owner: which earlier Lab screens to roll back to; Daily Five for a newcomer; the "most advanced" wording; NCERT line references inside the product. He has an overnight task to brief next. Working rule: small passes in the main session, agents only when they speed things up.


## 22 Nov 2026, 3:51 AM IST (orchestrator, Claude Fable 5.2): LK368 overnight run started

LIVE = main 6ad2c7f63. The owner's overnight brief is ledger row LK368 (he is asleep; decide and keep going; report by morning).
Orchestrator's limits told to him: no invented coverage numbers; no "highest in the market" line without proof.

Running, all in the shared checkout `wt-1110-convert` (only the orchestrator commits, gates and deploys):
- Session `hero-film` (Fable): update the hero walkthrough film for today's product, better sound; delivers
  `public/video/hero-v6-*` and the player config; v5 files stay for roll-back.
- Session `lab-redesign` (Fable): the Mistake Lab's cards and motion, old and new looks combined; Lab files only.
- Agent `cov-ui` (Opus): the coverage pages `/cuet-2026-coverage` and `/cuet-2026-coverage/[subject]`, the build script
  `scripts/coverage/build-public.mjs`, and the home teaser moved lower. Design: `tmp/1122-coverage/UI-SPEC.md`.
- Agent `cov-scout` (Opus): read-only map of the papers, the content pipelines and the gaps: `tmp/1122-coverage/SCOUT.md`.
- Next, from the orchestrator: a multi-agent run that (a) checks more subjects' real CUET 2026 papers question by question,
  (b) authors the missing content (Key cards for theory gaps ship with a deploy; bank questions need a production publish),
  (c) re-checks, so each shown subject reaches 80% or more for real.

Design decisions (orchestrator): four statuses per question (same question, same with new numbers, taught, not yet), a
syllabus-level figure computed from data, every question shown beside its MockMob match. Competitor's published figures seen
22 Nov: 73% overall; Economics 79, Business Studies 74, Accountancy 73, Mathematics 53 (their own method).

### 4:15 AM update (orchestrator)
- Usage: the two Fable sessions burned the 5-hour limit fast (36% to 54% in 13 minutes), so both sessions now run on Opus 5.5
  (session ids local_a01f33a5-babf-4240-8975-caef7be1efea hero-film, local_c4062e0d-cf4c-430c-8147-856f2845fe26 lab-redesign).
  The limit resets about 5:40 AM. The orchestrator keeps its own calls few.
- Coverage content runs (rules: `wt-1110-convert/tmp/1122-coverage/COMMON.md`, map: `SCOUT.md`):
  workflow `coverage-tier1` run wf_4f3b1eb9-780 (Accountancy, Business Studies, Economics: dossier, author, audit, then a
  wave 5 publish plan in `tmp/1122-coverage/PUBLISH.md`; the apply is the orchestrator's step and may need the owner);
  workflow `coverage-new-subjects` run wf_23b06b13-8b6 (Political Science, History, Sociology, Psychology: paper, check A,
  check B, Key cards, audit). Each subject ends in `data/coverage/cuet2026/<id>-final.json`.
- After they finish: run `scripts/coverage/build-public.mjs` (agent cov-ui is writing it), look at the pages, recapture the
  home fixture, gate in wt-1116-next, deploy.

## 22 Nov 2026, 6:40 AM IST (orchestrator, Claude Fable 5.2): LK368 overnight, state for whoever continues

LIVE = main f33bd5018 since 6:21 AM (rollback 6ad2c7f63): /cuet-2026-coverage and its subject pages, audited Key cards.
In the release gate now: aae55e759 (adds Sociology and History, the redesigned Mistake Lab). Deploy when wt-1116-next/tmp/gate2.log
shows 24 "fail 0", empty eslint, both builds 0, DONE.

Coverage, true numbers (data/coverage/cuet2026/public/summary.json; build: scripts/coverage/build-public.mjs with
`--snapshot-dir tmp/1122-coverage/snap/<id>/` for each subject, or `--fetch`): Business Studies 41/49 (84%), Economics 39/45 (87%),
History 39/42 (93%), Political Science 39/41 (95%), Psychology 48/50 (96%), Sociology 35/41 (85%); total 241/268 (90%).
Accountancy 41/55 (75%) is HELD (the build shows a subject only with its final check done and at 80% or more).
Running: workflow coverage-geo-bio run wf_695d580e-c0e (Geography, Biology: paper, checks A and B, Key cards, audit).

Bank questions (wave 5): 44 authored, the wave gate (5 blind solvers, 2 quality judges, 3 fit judges) kept 32
(accountancy 21, business studies 3, economics 8) and held 12. Dry run clean. The APPLY WAS DENIED to the orchestrator by the
auto-mode safety check (a production write), so the owner must run it:
  in wt-1110-convert: node --use-system-ca scripts/question-publish-authored.mjs --mode=apply
  --plan=docs/brain/reports/authored-publish/authored-publish-plan-2026-11-22T00-56-38-375Z.json
  --reason="CUET 2026 coverage wave 5: 32 scored commerce questions (accountancy 21, business studies 3, economics 8)"
  --expect-project=isrxrxzjocewrdureyhp
(restore command and details: wt-1110-convert/tmp/1122-coverage/PUBLISH.md). After the apply: in the three commerce
`<id>-final.json` files set `needs` to [] on the questions PUBLISH.md lists, run build-public with `--fetch`, tests, commit,
gate, deploy. Expected then: Accountancy 54/55, Business Studies 44/49, Economics 43/45.
NOT yet committed (stage 3): scripts/authored-w2-accept.mjs, scripts/lib/authored-wave.mjs, scripts/authored-w5-scoring-layout.mjs,
data/nta_agent_scores and data/nta_fit_scores (32 kept rows), docs/brain/reports/authored-w5 and authored-publish plans, and the
hero film v6 files (public/video/hero-v6-*, HeroFilm.jsx, heroFilmConfig.mjs, hero tests; v5 files stay for roll-back).

Hero film v6: delivered by session hero-film at about 6:25 AM (72.3 s, ten chapters, real screens, the approved voice; it
used 1,920 ElevenLabs credits). The orchestrator asked it at 6:35 AM to re-check the Mistake Lab chapter against the
redesigned Lab and re-record if stale; release v6 after it answers. Sound not checked by ear.
Mistake Lab redesign: done by session lab-redesign (notes in its own section above), included in aae55e759.
Not done from the owner's list: the Daily Five's clarity for a newcomer; more subjects (Maths and the sciences need
numerical bank questions, so they need the publish route); "highest in the market" is not claimed anywhere.


## 22 Nov 2026, 7:35 AM IST (orchestrator, Claude Fable 5.2): LK368 overnight run released, main fb7f3bbcc

LIVE = main fb7f3bbcc (rollbacks: aae55e759, f33bd5018, 6ad2c7f63). Outcome: ledger row "LK368 outcome". Gate log: wt-1116-next/tmp/gate2.log.
WAITING ON THE OWNER: the wave 5 publish (32 gated bank questions). Command, from wt-1110-convert:
`node --use-system-ca scripts/question-publish-authored.mjs --mode=apply --plan=docs/brain/reports/authored-publish/authored-publish-plan-2026-11-22T00-56-38-375Z.json --reason="CUET 2026 coverage wave 5: 32 scored commerce questions (accountancy 21, business studies 3, economics 8)" --expect-project=isrxrxzjocewrdureyhp`
Then: set `needs` to [] on the questions PUBLISH.md lists in the three commerce final files, `node scripts/coverage/build-public.mjs --fetch`, tests, commit, gate, deploy. Accountancy then shows at 54/55.
To add a subject: the workflow scripts under the session's workflows/scripts (coverage-new-subjects, coverage-geo-bio) run paper, check A, check B, Key cards, audit; rules in wt-1110-convert/tmp/1122-coverage/COMMON.md, map in SCOUT.md. A subject shows only with `<id>-final.json` and 80% or more (scripts/coverage/build-public.mjs SHOW_MIN_PCT).
Open with the owner: his ear on the film's sound; the Lab on his phone; the Daily Five for a newcomer; whether to keep sub-80 subjects hidden; the 12 held bank questions (rewrite or drop); Maths and the sciences.

### 7:55 AM update (orchestrator): LIVE = main 7d0e31d87
The Daily Five's sub line now speaks to a newcomer first (LK367). Gate clean on 7d0e31d87 (24 suites, eslint, both builds).
Everything else as in the 7:35 AM section above; the owner's publish step for the 32 bank questions is still open.


## 22 Nov 2026, 12:43 pm IST (orchestrator, Claude Fable 5.2): wave 5 PUBLISHED, Accountancy shown, main 8c74cca7c

LIVE = main 8c74cca7c (rollbacks: 7d0e31d87, fb7f3bbcc, aae55e759, f33bd5018). Outcome: ledger rows LK369 and "LK369 outcome".
The owner's publish step is DONE (he asked the orchestrator in chat to run it; 12:17 pm; 32 inserted). Nothing waits on him for coverage.
Coverage now: nine subjects shown, total 382/416 (92%); Accountancy 54/55, Business Studies 44/49, Economics 43/45; held list empty.
Undo of the publish (hides the 32 rows): `node --use-system-ca scripts/question-publish-authored.mjs --mode=restore --restore=docs/brain/reports/authored-publish/authored-publish-restore-2026-11-22T06-47-45-879Z.json --expect-project=isrxrxzjocewrdureyhp` from wt-1110-convert; after it, set the 20 questions of tmp/1122-coverage/PUBLISH.md section 2g back to not_covered and rebuild.
Never apply the old 44-row plan (authored-publish-plan-2026-11-22T00-16-56-474Z.json, untracked).
Open with the owner: his ear on the film's sound; the Lab, coverage pages and film on his phone; Maths and the other sciences (numerical bank questions through the same publish route); the 12 held bank questions (rewrite or drop); NCERT line references in the product; his promised feedback on "the whole CUET prep thing".


## 22 Nov 2026, 12:55 pm IST (orchestrator, Claude Fable 5.2): hero film v6 ROLLED BACK, v7 rebuild in progress

LIVE = main 8c74cca7c (12:43 pm): the hero plays v5 again (heroFilmConfig.mjs, HeroFilm.jsx and the hero tests are the pre-v6 versions); coverage shows nine subjects (382/416). Rollbacks: 7d0e31d87 (v6 film), fb7f3bbcc.
Owner's verdict on v6 and his brief for the rebuild: ledger row LK370. Rule saved (memory hero-film-fable-only): film work is the main session's, never a side session; update the old film's scenes, never recordings in a window; watch it through before release.
v7 state: Desktop/MockMob-promo-film, docs/HERO-V7-PLAN.md (structure, the time warp, order of work, status). Files: src/hero/v7/{kit7,KeyCards7,AskMobi7,Daily7,Rival7,Compass7,Hero7}.tsx, spec7.ts, scripts/hero7.mjs, scripts/hero7-bundle.sh, scripts/hero-sound/build_hero_v7_mix.py; mix public/music/hero-v7-mix.wav (-16 LUFS, -1.8 dBTP by the project's meter). Master render out/hero/hero-v7-master.mp4 started about 12:55 pm.
NEXT: review the master's sheets through its whole length beside v5's; send him the film as a FILE (not a deploy); on his yes: `node scripts/hero7.mjs --master out/hero/hero-v7-master.mp4 --web v7`, copy out/hero/web-v7/* to wt-1110-convert/public/video, point heroFilmConfig.mjs and HeroFilm.jsx at hero-v7 with the ten chapters of out/hero/v7/chapters.json (the v6 commit fb7f3bbcc shows the exact edits and test changes), tests, gate, deploy.

### 1:02 pm update (orchestrator): hero film v7, first full cut SENT to the owner as a file, NOT live
Master MockMob-promo-film/out/hero/hero-v7-master.mp4 (1920x1080, 60 fps, 72.3 s, crf 16); web files out/hero/web-v7/hero-v7-{1080,720,480}.mp4 (13.34 / 8.26 / 4.72 MB) and posters; film project commit 02af892 (plan docs/HERO-V7-PLAN.md).
Looked at: the whole length at 2 frames a second at phone size (out/hero/v7_phone_01..05.png) and three rounds of 3 fps frames of chapters 01 to 09. Sound: built with the project's mixer (-16 LUFS, -1.8 dBTP, 74 quiet effects); NOT heard by ear.
The site still plays v5 (main 8c74cca7c). On his yes: copy out/hero/web-v7/* to wt-1110-convert/public/video, point heroFilmConfig.mjs and HeroFilm.jsx at hero-v7 with the ten chapters of out/hero/v7/chapters.json (web commit fb7f3bbcc shows the same edits for v6, including the three hero tests), tests, gate in wt-1116-next, deploy. On his notes: change the scene in src/hero/v7, re-bundle (scripts/hero7-bundle.sh), re-render (about 5 minutes at 1080p, concurrency 8).


### 1:06 pm update (orchestrator): new references and the Higgsfield trial (ledger LK371)
Owner's two reference launch films: https://youtu.be/SgmuplXU2iY (Zelios, LangEase launch ad, 1:29) and https://youtu.be/k3d_xeVxEOE (OpenAI, "Refreshed.", 1:50); "mostly silent" (music and effects, no voice). NOT yet studied: the browser pane could not give reliable frames. WAITING ON THE OWNER for the two files in Desktop/MockMob-promo-film/refmedia; then: frames at 4 a second into contact sheets, the sound measured from the files (tempo, hit and silence times, levels), a written study in docs/, and the film raised to that bar.
Higgsfield trial: unlimited to 25 Nov 2026, one image and one video at a time; his card is charged USD 93.22 on 25 Nov unless he cancels (tell him again on 24 Nov). This session's Higgsfield connector has no generate tool (7 read tools); ask him to allow the connector's generation tools for Claude Code, or run generations in the Claude chat app from prompts written here and read the results with show_generations.
Hero film v7 first cut is with him as a file (wt-1110-convert/tmp/1122-film/mockmob-hero-film-v7-draft.mp4); the site plays v5.


### 1:15 pm update (orchestrator): references studied; direction from LK372
Both reference films watched frame by frame (MockMob-promo-film/docs/ref/lk371/le_01..06.jpg at 4 fps, rf_01..09.jpg at 2 fps) and their sound measured (tools/ref_sound_lk371.py). LangEase (33 s): 117.5 BPM, a steady bed from second 4, about 3.3 sound events a second, NOT ONE hard cut: every change is a morph or a camera move, each big move on a bar; words 2 to 4 at a time; one UI detail at a time, large, in soft 3D. OpenAI Refreshed (110 s): 95.7 BPM, built from one dot, opens on isolated dry clicks with real silence between them, music enters around second 10, a breakdown with silences at 48 to 55 s, cuts in rhythmic bursts (one every 0.23 s at 28 to 30 s).
Owner (LK372): these are a craft bar, not a style to copy; keep building on the existing film; top-tier motion, animation and design. So: NO new-style film. Next pass on Hero16v7 (MockMob-promo-film docs/HERO-V7-PLAN.md): designed transitions at every chapter cut instead of bare hard cuts, captions that arrive word by word, cards and devices that keep a slow 3D drift so nothing sits still, stronger entrances; then re-render, watch through, send as a file.


### 1:23 pm update (orchestrator): the 72 s cut is dropped; Hero16v8 = v5's voice and flow with better pictures (ledger LK373)
Owner: v5's script, voice and flow were "almost perfect"; only add and improve the graphics; v7's longer lines and the spelled-out N-C-E-R-T were wrong. Now building Hero16v8 (MockMob-promo-film src/hero/v8/{spec8.ts,Hero8.tsx}, scripts/hero8.mjs, hero8-bundle.sh, scripts/hero-sound/build_hero_v8_mix.py; mix public/music/hero-v8-mix.wav). v7 (src/hero/v7, 72 s) stays in the repo as the source of the scene components v8 reuses (KeyCards7, AskMobi7, Compass7, kit7); it is not a deliverable any more.
NEXT: review the v8 master's sheets through its whole length (out/hero/v8_phone_*.png), send him the film as a FILE; on his yes: copy out/hero/web-v8/* to wt-1110-convert/public/video, point heroFilmConfig.mjs and HeroFilm.jsx at hero-v8 (nine chapters as v5, chapter 02 named Mistake Lab; times in out/hero/v8/chapters.json are v5's), update the three hero tests, gate, deploy.

### 1:27 pm update (orchestrator): Hero16v8 (53 s) SENT to the owner as a file, NOT live
Master MockMob-promo-film/out/hero/hero-v8-master.mp4 (1080p, 60 fps, 53.033 s); web files out/hero/web-v8/hero-v8-{1080,720,480}.mp4 (9.79 / 6.08 / 3.47 MB) and posters; film project commit follows 02af892 (docs/HERO-V8-PLAN.md has the table of what changed and the commands).
Looked at: the whole length at 2 frames a second at phone size (out/hero/v8_phone_01..04.png); check frames of chapters 04 to 06 at 4 a second. Sound: v5's mix figures reproduced exactly; NOT heard by ear.
Waiting on the owner's verdict on v8. The site plays v5. Higgsfield: still 7 read-only tools in this session, nothing generated.


### 2:22 pm update (orchestrator): hero v8 accepted as fine; new work = a silent LAUNCH film (ledger LK374)
Two films: (1) hero walkthrough: v8 ready in MockMob-promo-film/out/hero/web-v8, NOT live (no explicit yes yet; the site plays v5); (2) a new launch film, purely launch-focused, NO sound: composition Launch16 in MockMob-promo-film (plan docs/LAUNCH-FILM-PLAN.md). Spine = the site's own words: hero sentence "CUET 2027. One mock. Know what to fix." (web heroLines.mjs, owner-approved) and the end card's "Find it. Fix it. Check it held."; seed element = the volt dot (the o of the wordmark, Mobi). Craft bar: docs/REF-STUDY-LK371.md (continuous morphs, one idea at a time, big type, UI details large in soft 3D), never a copied style. Process: a finished opening slice goes to him first as a real render, then the rest.

### 2:30 pm update (orchestrator): launch film opening slice SENT; films gathered on the Desktop (ledger LK374, LK375)
Launch film: MockMob-promo-film src/launch/Launch16.tsx, plan and scene table docs/LAUNCH-FILM-PLAN.md (A to C built, D to G to build). Slice out/launch/launch-slice-01.mp4 (13 s, 1080p60, silent) sent to the owner as a direction check. WAITING on his verdict before D to G.
Owner also asked (LK375, about 2:25 pm): "can you place the films that we have created in one folder ... They are cluttered on the PC ... add all that to a folder on the desktop." DONE: Desktop\MockMob Films (copies; 4 numbered folders: promo 16x9, portrait 9x16 with cut-downs and Instagram files, hero film v5 live / v8 not live / rejected v6 and v7, launch film in progress; a plain READ ME lists them). Originals untouched in MockMob-promo-film\out. Add each new cut there.
Hero film v8: he called it "fine already"; NOT live, no explicit yes to switch. Higgsfield: still 7 read-only tools here, empty history.


### 2:37 pm update (orchestrator): launch slice REJECTED (ledger LK376); new storyline and look
The 13 s slice (cream ground, type and flat cards, no audio) is rejected as "so basic". Rules now: no voice-over but full music and sound design; a real storyline; fast, upbeat; creative fonts; glass and liquid glass; cinematic depth. Third reference studied: MockMob-promo-film/refmedia/lk371/lovio.mp4 (53 s, 136 BPM, 5.6 sound events a second, 11 hard cuts; sheets docs/ref/lk371/lv_01..04.jpg): a story ("I have an idea" -> a typed prompt -> generating -> results -> "Beautifully designed" -> "ready to launch" -> "in any direction" -> "What starts as an idea"), glass pills and panels over cinematic plates and aurora gradients, big zooms into UI, words with objects set between them. The new plan is MockMob-promo-film/docs/LAUNCH-FILM-PLAN.md section "V2" (storyline, look, music grid). src/launch/Launch16.tsx (the rejected slice) stays only as a source of parts (the dot, the palette, the chapter rows).
