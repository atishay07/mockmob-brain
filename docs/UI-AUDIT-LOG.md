# UI audit log: what has already been looked at, and what was found

Living file. Started 12 Nov 2026 (about 9:45 pm IST) after the owner's words: "most of your time went to looking ... no other agent has to spend this kind of time looking and already finding the things which you have already found or which you think don't need to be changed ... Log all of this in the brain, keep it updated."

**Rule for every agent doing UI work on MockMob:** read this file before capturing or reading any screen. Do not re-walk a surface marked "seen, holds" unless code under it changed after the date shown (check `git log` for the files named). When you look at something, add what you found here, with the date, the commit and the sizes you looked at. A finding without those three is not a finding.

State this log describes: web `main a218cb9a4` (live, 13 Nov 2026; sections 2 and 3 were walked on 766eb6da9, section 2a on a218cb9a4), app `ui/1112-final c79dac51c` (version 1.0.23+21).

---

## 1. How to look, fast (do not rediscover this)

Web worktree: `C:/Users/atish/Desktop/mockmob copy/wt-1110-convert`. Tools: `tmp/1110-app/` (not shipped). Dev server: `preview_start {name: "convert-1110"}`, port 3571. Delete `.next` and `.next-dev` after a session.

| Need | Command (from `tmp/1110-app`, Git Bash; prefix `MSYS_NO_PATHCONV=1` when an argument is a lone `/`) |
|---|---|
| Whole public page as a reader scrolls it | `node strip.mjs <label> / 390x844 dark 760` then `python grid.py shots/<label> 390-dark 300 8 1` (contact sheets; about 2,200 tokens a sheet) |
| A page at given scroll positions after waits | `node at.mjs <label> / 390x844 dark 5320,6080 700,2500` |
| First visit, timed frames | `node first.mjs <label> 390x844 dark` |
| Signed-in pages (fixtures, no sign-in) | `node walk.mjs --label x --w 1440 --h 900 --theme dark --data ready --views today,dashboard,... --max 2` (a real desktop browser at 700 px and wider). Views: today, dashboard, mob, profile, review, learn2, learn2-chapter, cards, explore, saved, ranks, wallet, result, progress, radar, compass, prepos, revise, help, onboarding. Extra query with `--q`. |
| Where each page's title starts on desktop | `node edges.mjs 1440 today,mob,learn2,...` |
| Anything running past the right edge | `node probe.mjs 390x844 <y1,y2,...>` (local) or `probe-live.mjs ... x https://www.mockmob.in/` |
| Film frames | `node film-frames.mjs <label> /video/hero-v5-720.mp4 1.9` then `grid.py` |
| Side-by-side images | `python montage.py out.jpg <width> a.jpg b.jpg` |

Traps that cost time on 12 Nov:
- **Lab and tour scenes fill in over about 2 s.** A shot taken 0.7 s after a jump shows half-empty cards. That is not a defect. Wait 2.5 s before judging.
- **Count-up numbers** (questions, Key cards, subjects) differ between shots because they animate once. Not a truth problem.
- **The roaming Mobi** on the home page is in transit between sections after a jump; it has `pointer-events: none` and cannot block a tap.
- **Local price wording differs from production.** Locally the offer is "₹99 once, to 31 July 2027" (no `RAZORPAY_PLAN_ID_PRO_MONTHLY` locally); production says "₹99 a month". The film's "Pro ₹99 a month" matches production.
- **Production runs the newer Mob (the den, `MOB_V3_ENABLED` on).** The preview shows the older ring page unless the link has `&mob=den`. Judge the den.
- **The preview cannot open the test-taking screen** (`view=test` says the paper link expired; a launch from Practice does not complete). Not seen on desktop in this pass.
- **A first visit gets the Day theme**, whatever the phone's setting. Judge Day at least as carefully as Night.
- The time: run `date`. On 12 Nov my sense of elapsed time was an hour off.

App: `C:/Users/atish/Desktop/mockmob copy/wt-1108-app/flutter_app`. Method and tap coordinates: `wt-1108-app/tmp/1112-final/walk/WALK.md` (720x1600 emulator `mockmob_budget`: tabs at y 1465, Today x 101, Practice 225, Start 360, Mob 494, You 617; avatar 72,208; Ask Mobi 575,208). Shots: `tmp/1112-final/walk/` (117, demo build, Night and Day) and `tmp/1112-final/check/` (after shots; release build first run).
- **Debug builds of the real app stop on the opening screen** (Riverpod's debug-only `CircularDependencyError`: `AuthController._watchForRecovery` listens to `networkRestoredProvider`, whose `ConnectivityMonitor` depends through three providers on `AuthController`). Do not spend time on it in a walk. For the first-run flow use a **release** build signed with the upload key: it installs over the `in.mockmob.app` already on the emulator (same key) and opens at the welcome screen.
- The demo build (`test/device_demo/demo_main.dart`) is the way to see signed-in screens. Learn, Explore and Colleges show "didn't load" there (no local servers); the Mob shows "opens soon". Both are demo limits.
- Flutter tests run at about 8 a minute on this PC. Never plan to run the whole unit or golden folder; run the folders that cover the change.
- Onboarding reference renders exist for every step at four sizes and both themes: `test/golden/onboarding/goldens` (322 files). They are faithful; read them before asking for a device walk.

---

## 2. Home page (www.mockmob.in)

Looked at on 12 Nov 2026, commit 230de48e8 then 766eb6da9: 390x844 Night (28 screens), 360x740 Day (31), 1440x900 Night (25) and Day (24), a timed first visit at 390, /signup at 390 and 1440 in both themes, an overflow scan of the whole page at 390, and the live site's tour region at 390.

| Section | Verdict | Notes |
|---|---|---|
| Header (phone and desktop) | Seen, holds | At 360 the Pricing pill is hidden by design. |
| Hero copy, two keys, log-in line, creators line | Seen, holds. **Not changed** | First paint about 0.6 s on the local build; no splash delay. The owner removed a fact line from the hero (LK121), so do not add "Free. No card needed." there. The third headline line types and rotates by design. |
| Hero film player | Seen, holds. **Not changed** | Plays about 3 s after load. The "Sound on" key on the picture stays: the film is narrated (owner, round 12). **Weak point, open:** on a phone the film is about 350x197 px, so the phones and laptops inside it are hard to read; only its headlines carry. |
| Hero film content (r5, 53 s) | Seen frame by frame, truthful | "Pro ₹99 a month", "15 subjects, 19 of every 20 CUET papers", "Race up to four friends", "Unlimited with Pro" all match production. Its screens still match the product. Edits to the film are done by the main session only (owner, 12 Nov). |
| Feature strip under the film | Seen, holds | **Possible gain, open:** six stacked rows plus the price hook on a phone (about 600 px) push the "Try five CUET questions" sample to about 1,900 px down. |
| College strip | Seen, holds | |
| Sample ("Try five CUET questions") | Seen, holds | Subject switch and loading were redone 10 Nov (LK223). |
| Statement ("Your marks slipped somewhere") | Seen, holds | Scroll-scrubbed; the dim words are mid-scrub. |
| Mistake Lab, five scenes | Seen, holds | Every scene fills its card within about 2 s on phone and desktop. |
| Tour "More inside MockMob" | **Fixed 12 Nov** | The last slide (the Mob) ran 43 px past a 390 px screen: `.ft` had an implicit auto column. Now `grid-template-columns: minmax(0, 1fr)`; "Up next" reads the next section's `data-section-name` ("Key cards"). |
| Key cards, exam screen, DU Compass, DU courses, creators, pricing, FAQ, close, footer | Seen, holds | The creator cards' empty middle is where a reel preview loads. |
| /signup | Seen, holds (phone and desktop, both themes) | |
| /pricing, /refunds | Not re-walked 12 Nov | Reworked 10 Nov (LK212-LK214); only checked that they answer 200. |

Not looked at: tablet widths (768 to 1024), iPhone Safari, a physical phone, a screen reader.

### 2a. Home page motion (round 13, 13 Nov 2026, commit a218cb9a4; owner LK232-LK236)

**Every animation on the home page is inventoried in `wt-1110-convert/tmp/1113-motion/AUDIT.md`** (curves and durations in use, each section's animations with trigger, timing and file:line, 26 findings, the list of loops, and exactly what Mobi does on phones and desktop). Read that before touching any motion here; do not re-derive it.

Round 13's own rules are in one file, `src/app/r13-motion.css`, loaded last by `page.js`. Each block's comment says what it replaced.

| Thing | State after round 13 | Notes |
|---|---|---|
| Section reveals (`Reveal.jsx`, `.rv`) | **Changed** | Heads: 10 px rise, 320 ms, no blur (was a 6 px blur over 800 ms from 24 px). Blocks: 12 px, 300 ms. `threshold` 0 (was 0.12, which left a blank band under tall blocks on a flick). |
| Mistake Lab scene change | **Changed** | Out 120 ms, in 90 ms later over 220 ms (was a 420/550 ms crossfade with two scenes showing). The screens inside still take about 2 s to draw their rows (audit F19, owner's call, untouched). |
| Sample card taps | **Changed** | Press dips to 0.985; right answer swells 1.5 %, wrong shakes 3 px; no 3 px hop; the next question's stem and options rise 6 px in sequence. Mobi's bubble: old line out in 100 ms, new one in after 110 ms. |
| Sample result: "Ask Mobi what to do tonight" | **New** | `askMobiSample.mjs` (pure, tested). One step from the five answers, two follow-ups. No model, no network. Checked at 390 and 360, Day and Night, with 0, 3 and 5 misses. |
| Held stories' bottom bar (phones) | **New** | The logo's Mobi (18 px) on the current step, a hop per step (`SectionPosition.jsx` `.lp-bar__mobi`). |
| Desk scene in "Try five CUET questions" | **New** | Scroll-driven depth (CSS `animation-timeline`): room 1.08 to 1, Mobi 0.92 to 1, bubble last. Done at `contain 30%` on phones, at `entry 100%` from 1024 px. |
| Press states | **Added** | Tour chips, pricing subject steps, Compass keys, FAQ rows, shelf links, Wall pause, hero DU link. |
| Sticky hover on touch | **Fixed** | A tap no longer freezes the college rows or leaves the Compass demo key hovered. |
| Key card flip | **Changed** | 480 ms on the drawer curve (was 600 ms on a slow-start curve). |
| Phone menu | **Changed (site-wide, `nav-motion.css`)** | 260 ms an item, 25 ms apart: the sign-up keys land by 410 ms (were 640 ms). |
| Compass sweep | **Changed** | Renders in steps of 5 points (was a render nearly every frame). |
| Night phone dock | **Changed** | Blur 14 px, saturation 1.2 (was 20 px, 1.6). |
| Desktop lane Mobi | **Changed** | Fades over 160 ms when he hides or shows (was one frame). |
| Held stories' step and gesture logic, the hero film, the college marquees, seat hop-ins | **Untouched** | Owner-tuned; the audit lists facts only. |

Traps found:
- **A timed frame taken with Playwright is 50 to 100 ms later than its label** (the screenshot itself takes that long). Judge a 100 ms transition from several frames, not one.
- **A scroll-driven animation shows a half state in a still shot** taken while the stage is entering. Compare against where a reader rests, not mid-entry.
- The page's height differs between local and live by about 70 px in pricing (the local one-time offer wording). Section heights otherwise match; `tmp/1113-motion/heights.mjs <base>` prints them.

Tools added (`wt-1110-convert/tmp/1113-motion`, Git Bash): `node check.mjs <label> 390x844 light` (timed frames of a wrong pick, Next, a right pick and a Lab scene change, plus page errors, right-edge overflow and real-pointer hit tests); `node ask.mjs <label> 390x844 light 0,1,0,0,1` (plays the sample with those picks, opens Ask Mobi, taps each follow-up); `node reduced.mjs` (Reduce motion: every reveal visible and unmoved, the desk finished).

Open, from the audit, his call: seats appear at 55 % visible with an 880 ms hop (F18); Lab screens take about 2.4 s to draw (F19); the film's progress bar restyles every frame (F21, not measured).

### 2b. Home page, round 14 (13 Nov 2026, commit 38a09a4e7; owner LK237-LK241)

His verdict on round 13: "the entire landing page looks the same". Timing changes do not count as visible change for him. Round 14 is the visible one.

| Thing | State | Notes |
|---|---|---|
| Hero feature strip (phones) | **Changed** | Two unboxed columns under one hairline (was six stacked rows in a bordered card, about 455 px; now about 334 px at 390). Its "Ask Mobi" row reads "Ask a question. No sign-up." and opens the sheet. |
| Boxes | **Removed** | Hero DU link tray, Compass Pro aside, Compass score box, exam NTA note, Key cards bank line, pricing's six tiles and "usual way" panel, Instagram numbers, the tour's "Up next" box, the FAQ band's gradient. All in `src/app/r14-look.css`, each block commented. Left by the owner's earlier word: college chips, the "Or start on Free" panel, the Pro glass card. |
| Mobi's seat captions | **Changed** | Plain ink-2 text, no pill or tail (DU, pricing, close). |
| Headings on phones | **Changed** | The sample, Mistake Lab and pricing h2 are 34 px with 48 px above; the rest stay 28 px. |
| Phone scroll companion | **New** | `MobiCompanion.jsx`, `r14-companion.css`, `companionModel.mjs` (tested). Below 900 px: 56 px Mobi on the dock's top edge, leans with scroll speed, pose by section, steps out when the desk Mobi, a seat, the film or a held story's bar is on screen, tucks to a 26 px head when a control is under him. A tap opens Ask Mobi. One 3 s hello bubble a session. Known: tucked, his head can sit over a reel card's or FAQ row's top edge; he reaches a rising dock about 120 ms before it. |
| Ask Mobi sheet | **New** | `AskMobiSheet.jsx`, `ask-sheet.css`, opened by the window event `mm:ask-mobi` (strip row, companion, sample result). Real replies from `POST /api/mobi/guest`; three questions a visitor; falls back to the local plan (`askMobiSample.mjs`) for the result's question if the server cannot answer. Checked at 390 and 360 Night and Day and 1440 (Day, 360 and 1440 with mocked replies). |

Capture tools added: `tmp/1114-ask/sheet.mjs`, `tmp/1114-companion/walk.mjs`, `tmp/1114-look/` (before/after montages), `tmp/1113-motion/live14.mjs` (the live sheet and companion; spends one real guest call).

Traps: running captures and `next build` together crashed a build worker once (exit 3221226505); build alone. Production does not set `PERSISTENT_LIMITS_ENABLED`: a route that must have the database limiter passes `persistent: true`.

### 2c. Home page, round 16 (16 Nov 2026 evening, main 516bc9511; owner LK266-LK275)

His verdict on the live page: good on desktop, short on the phone. Looked at: www and the local build at 390x844 Day (whole page, 31 screens, twice), real finger swipes from the Mistake Lab to pricing, 360 and 768 touch for the tour, 390 Night for the new blocks, 1440 Day for the new blocks and the held tour.

| Thing | State | Notes |
|---|---|---|
| Daily Five and Sunday Mock on the home page | **Moved and rebuilt** | `#daily-and-sunday` after the exam screen: two rows, 535 px at 390. The full calendar pages live only on /daily and /sunday-mock now. No day number anywhere. |
| "Got one wrong in another test?" | **Rebuilt** | One card, three tabs (reader-driven, never timed), 956 px at 390. Desktop: words left on one edge, card right, centred. |
| "More inside MockMob" on touch | **Rebuilt** | A plain stack, no hold, no chip row, no bottom band. Every screen answers taps. Mouse and trackpad keep the held tour. The Mistake Lab stays held on every device. |
| Phone scroll companion | **Calmed** | On the bottom bar only; no lean, stretch, hop. Still tucks to a head over a control. Tap asks about the section in view. |
| Mobi's seats on phones | **Calmed** | 260 ms fade and 8 px rise (was an 880 ms hop). The close keeps its one wave. |
| Compass | **Fixed** | No self-running score on touch (rests at 900: five clear, five short); head on the left edge; Mobi at the head's right. |
| Range inputs on touch | **Fixed** | Track ignores the finger, knob takes it, vertical drags scroll (`r16-phone.css` block 3). Compass and pricing. |
| Key cards subjects | **Trimmed on phones** | Six chips and a count chip; all fourteen from 720 px. |
| /sunday-mock "How it works" | **Rebuilt** | Three figures and a timeline. /daily's head explains the five. |
| Hero, colleges, sample, statement, Mistake Lab, exam screen, DU tool, creators, pricing, FAQ, close | Seen, hold. **Not changed** | He called the page "competent" up to the tour's first screen. Pricing is 2,442 px at 390: long, his approved design, left. |

Traps: an element screenshot of a tall section is blank (content-visibility): use `tmp/1116-final/walk.mjs <label> "#a,#b" 390x844 light` (viewport steps, joined). `tmp/1116-final/swipe.mjs <label> "#start" <swipes> <px>` makes real finger drags; a drag that starts on a slider sets it. `tmp/1116-final/slider.mjs [base]` tests the slider guard. `sec.mjs` taps through a block's steps and reports whether each control was reachable. In Git Bash a `/path` argument needs `MSYS_NO_PATHCONV=1`.

Open, his call: the pricing section's length on a phone; whether the companion should show at all while a tour screen is under him (he stands over its right corner); Learn's "Then: practise Vocabulary questions" line inside the tour screen.

### 2d. Home page, the merged night lanes (17 Nov 2026, web/1115-prod 3511f1fb3; owner LK278-LK289)

Looked at: the whole page at 390x844 Day with 38 real finger swipes (420 px drags, CDP touch; top to footer, 22,875 px), then 390 Night, 360x740 Day and 1440x900 Day for the stretch from "Got one wrong in another test?" to the DU calculator; a 42-rest companion audit (after each swipe settles, a script reads whether his visible figure or his hello covers a word or a control) on the local build and on live main 67146f994; one real touch tap on each new control. Tools: `wt-1110-convert/tmp/1116-final/` `swipe.mjs`, `walk.mjs`, `mc-audit.mjs`, `taps.mjs`, `taps2.mjs`; shots under `tmp/1116-final/shots/` (`w17day`, `st390n`, `st360`, `st1440`, `mc-new`, `mc-live`, `taps-390`).

| Thing | State | Notes |
|---|---|---|
| Tour on phones (LK278) | **Seen, holds** | One held stage again, five still tabs, the browser's own scroll (`free`). In the 390 walk each ordinary swipe moved one tool (Practice, Learn, Ask Mobi, Benchmarks, Mob). All five tabs and a screen choice answer a tap. |
| "Got one wrong in another test?" (LK280, LK281) | **Seen, holds** | Four steps (Question, Read, Check, Practise), the older concrete copy, "What you leave with". 1,135 px at 390. Every step, "See Mobi's read", an answer (verdict shows), "Then practise" tapped for real; nothing over any of them. |
| Daily Five and Sunday Mock (LK282) | **Seen, holds** | Stamp, big head, week rail, today's card on ink with its clock and key, the Sunday card. 811 px at 390. "Play today's five" goes to /daily, "See how Sunday works" to /sunday-mock. |
| Phone companion | **Fixed** | He used to duck only for controls, so he stood over words, and his once-a-session hello could land on a sentence (live: over a word or control at 8 of 42 rests, including the hello over the shelf line and a link, tour keys, the Daily row). Now at each rest he looks for words too: clear, he stands; only his body over something, he shows his head; his head band too, he steps aside until a clear rest. The hello shows only where its own box covers nothing. Local: 0 of 42. He shows less often (6 rests against 12). `MobiCompanion.jsx`, `restSpot` in `companionModel.mjs`. |
| DU calculator head | **Fixed** | Was centred (7 Nov) over a left-aligned tool: its h2 started 27 px in. Now the Compass's form: head on the left edge, Mobi at its right; the Combo line under the tool is left-aligned. Owner's 16 Nov rule: one left edge per block. |
| Section heads "60-70 px into the section" | **Looked, no change** | The extra 32-40 px is the brand stamp above those heads (Key cards, Ask Mobi, the week, the Compass, Instagram). From one block's last words to the next block's first element the gap is even, about 55-60 px. |
| Everything else on the page | Seen, holds | No sideways overflow at 360, 390, 1440; no page errors. |

Not looked at: a physical phone, iPhone Safari, tablet widths, a screen reader, Night at 1440 for this stretch.

### 2e. Home page and runner, the 17 Nov lanes (web/1117-prod, merged head af96050e8 / 65797fd17; owner LK290-LK301)

Looked at (17 Nov, about 3:45-4:10 am, local webpack dev server on the merged branch): the whole home page at 390x844 Day with
37 real finger swipes (420 px; 21,131 px page, 0 page errors); the tour deck by real touch (`wt-1117-tour/tmp/lane-tools/deck.mjs`:
four sideways swipes one card each, a swipe back, a vertical swipe over the deck scrolls the page, three tab taps, a tap inside);
the opening frame by frame (`wt-1117-opening/tmp/cap.mjs`, first visit at 390 Day, 390 Night, 1440 Day); the companion audit (38
rests); a new shadow sweep (`wt-1110-convert/tmp/1116-final/shadow-sweep.mjs`: any box-shadow reaching past its section's bottom,
and hard shadows) at 390 Day, 390 Night, 360 Day, 1440 Day; sideways overflow at 360 on /, /daily, /sunday-mock
(`overflow-check.mjs`); the daily block at 360; Today and You with streak fixtures (`?streak=day3|makeup|day30`) at 390 Day and
Night; NTA mode in the runner fixture (`wt-1117-nta/tmp/lane-tools/nta-walk.mjs`, 390 Day). Shots: `tmp/1116-final/shots/p17day`,
`d360`; `wt-1117-tour/tmp/lane-tools/shots/m390`; `wt-1117-opening/tmp/shots/m390d`, `m390n`, `m1440`; `tmp/1110-app/shots/st-*`;
`wt-1117-nta/tmp/lane-tools/shots/m390`.

| Thing | State | Notes |
|---|---|---|
| Tour on phones (LK290) | **Rebuilt, seen** | A deck: five still tabs over cards the browser scrolls sideways, next card peeking; one card a swipe; never held. 969 px at 390. Desktop keeps the held tour. |
| Shadows (LK291) | **Fixed, swept** | 0 shadows past their section at four sizes. The only "hard" hits are the brand's solid 4 px key lips and ring borders (intended). |
| Opening (LK299) | **Rebuilt, seen** | Answer sheet rain on the page's own ground (no dark flash in Day), the word rises onto the bar logo and lands (desktop: lands by about 1.1 s after release, links fade in by 1.4 s). LCP is page content at first paint (820 ms local), not delayed. |
| 3D Mobi seats (LK294) | **Seen, hold** | Magnifier, camera, reading, pointing, attentive, calendar, wave; companion at 4 of 38 rests, covering words at 0. |
| Daily Five block (LK293) | **Rebuilt, seen** | "Five a day. Play for your college.", admit-card Daily Five card with "Playing for", the college board with an honest empty state, the Sunday card. 1,141 px at 360. Board average from 10 players, to the nearest half (privacy). |
| Streak (LK296) | **Built, seen** | Today's block (days in a row, the milestone line, what today needs, rest passes), You. The top-bar chip shows only from 640 px up (on phones it squeezed Ask Mobi). Pause days 44 px tall. |
| NTA mode (LK297) | **Built, seen** | Instructions before the clock, saving only by Save & Next / Mark for Review & Next, "Saved" / "Not saved yet" beside the question number, Save & Next on the last question saves and stays, NTA's Exam Summary. |

Not looked at: a physical phone, iPhone Safari, Night at 1440 for the new blocks, the daily board with many players on screen
(fixture states tested in code only), a screen reader.

### 2f. Home page and arena, the 18 Nov rebuild (web/1118-prod; owner LK302-LK312)

Looked at (18 Nov, about 12:50 to 2:10 pm, local webpack dev server): the whole home page at 390x844 Day and 1440x900 Day before
any change (contact sheets `wt-1110-convert/tmp/1110-app/shots/r18a/sheets`), every signed-in view at 390 Day and 1440 Day
(`shots/r18arena`). Then each change as it was built. Tools added in `wt-1110-convert/tmp/1118/tools` (Git Bash, from that
folder): `deck.mjs <label> <WxH> <theme>` (the tour deck at each rest and two mid-deal frames), `marks.mjs <label> <WxH> <theme>`
(scrolls like a reader and shoots every pen mark once drawn), `drill.mjs` (answers the sample card), `lab.mjs` (three Lab scenes
after the pen has marked them), `streak.mjs <label> <WxH> <theme> [states]` (Today's streak block cropped, per fixture state),
`sheet_any.py <dir> <thumb w> <per row>` (contact sheets of any folder).

| Thing | State | Notes |
|---|---|---|
| "More inside MockMob" (LK304) | **Rebuilt, seen** | One deck the scroll deals, on every pointer (`TourDeck.jsx`, `deckMotion.mjs`, `r18-tour-deck.css`): held by ScrollStory like the Lab; five still tabs whose mark slides with the scroll; the card on show on top, passed tools as edges above it, the next card rising from the pile's foot as the page scrolls; each tool's demo plays once as its card comes on. Eight real 380 px finger swipes moved exactly one card each (scrollY 7574, 8219, 8865, 9511, 10156), 0 page errors. Seen at 390 Day, 1440 Day. `FeatureTour.jsx` and `r16-tour-stack.css` are no longer rendered (kept in the repository; tests now pin `TourDeck`). |
| The pen and the highlighter (LK308) | **New, seen** | `src/components/doodle` (`Doodle.jsx`, `doodlePaths.mjs`, `doodle.css`; `Marked` wraps a phrase of a copy string). Every mark is generated for its words' own box (never a stretched template), seeded by the words, drawn once when the words are 20% clear of the screen's foot. On the home page: "One mock." (highlighter, `HeroMark`, after the opening), the price figure (circle), 11 section headings (one mark each), the statement's three accent words, the sample card's verdicts (tick, red cross), three Lab screens (the worst chapter's marks, the net effect, the first plan line). On the result page: an underline under the costliest chapter when its name is 20 characters or fewer. Seen at 390 Day and Night, 1440 Day. A marked phrase never wraps (`white-space: nowrap`): keep marked phrases to three words. |
| Today's streak block (LK309) | **Rebuilt, seen** | `StreakMobi` (the logo's Mobi: an outline with shut eyes until today counts, volt with open eyes once it does), the number beside him, `WeekStrip` (the seven bubbles, moved up from the sheet), a segmented bar of today's answers (`todayProgress`, the server's own figures; the make-up's 10 when a day is open), then the status line, the passes and the door to the sheet. One moment a day when today first shows counted (Mobi wakes, the number rolls, today's bubble lands); none under Celebrations Off or Reduce motion. Six fixture states at 390 Day, two at 1440 Night. The top-bar chip (640 px and up) wears the same Mobi. The block is about 100 px taller than before (393 to 501 px at 390). |
| Everything else on the home page and in the arena | Seen, not changed | The arena's content column, rail and pages as section 3 says. |

Traps found:
- **Two files in one folder that differ only by case or by extension stem resolve wrongly on Windows** (`TourDeck.jsx` beside
  `tourDeck.mjs`: the import of the component got the module). The dev server also keeps the wrong answer until `.next-dev` is
  deleted and the server restarted.
- **A Blender render path that is relative lands in `C:\tmp`**, not the working folder: pass an absolute path.
- **A gate started with `( ... & )` inside a Bash tool call keeps running after the call returns** even though `ps` in Git Bash
  does not list it; starting a second one runs two builds in one folder. Start the gate once, with the tool's own background
  mode, and check `Get-CimInstance Win32_Process` for `gate2.sh` before starting another.
- Landing tests outside the gate's named suites pin `page.js` lines (`landing_checklist_1104`, `homeHero`, `hero_film_r7`,
  `du_teaser_r6`, `brand_r3_1105`, `pricing_value_1105`, `landingPosition`, `tourTaps`): run
  `node --test src/components/landing/*.test.mjs data/tests/landing_checklist_1104.test.mjs` after changing a heading's markup.

Not looked at: a physical phone, iPhone Safari, tablet widths, a screen reader, the deck under a slow phone CPU, Night at 1440
for the deck.

Tried and dropped: a real-time 3D Mobi (a Blender script to a compact mesh for a hand-written WebGL renderer). The owner saw
the working renders and called them "very bad" against the generated Mobi art already on the site (LK311). Nothing shipped;
the script is in `wt-1110-convert/tmp/1118/mobi3d/src` only. Mobi art comes from the existing stills or the image generator.

---

### 2g. Round 2 and 3 of 18 Nov (evening; main c2f12abcd then 9c7b563f2; owner LK313-LK316)

- **What was rebuilt:** home (exam screen, DU Compass, DU courses, creators, pricing, FAQ, close, footer), arena (Progress, Your
  standing, Your papers, Wallet, Practice, Learn's home, You). Briefs: `wt-1110-convert/tmp/1118/briefs/` (`R2-COMMON.md` holds the
  method: the graphic is 70% of the section's first phone screen, one left edge, detail behind a real disclosure, before/after
  montage or it is not done).
- **The pen in view** (`src/components/doodle`): `pen` and `accent="spark"` on `Doodle`/`Marked`. Look with
  `node tmp/1118/tools/pen2.mjs <label> 390x844 light` then `python tmp/1118/tools/pen.py <label> 390-light`: it pauses each
  mark's own animations at fixed times, so the pencil and the stroke head can be compared exactly (timed screenshots cannot).
  `pen.mjs` shoots real-time frames, including the scroll-held pencil on the Lab's heading.
- **Traps found tonight:**
  - An `<svg>` with width or height 0 paints nothing, even with `overflow: visible`: the pencil was invisible until its svg was 1 x 1.
  - A lane runs only the suites its brief names. arena-b moved Practice's heading from the mode to the subject and no test it ran
    said so; `src/components/start/__tests__/startModel.test.mjs` (owner G26) caught it only in the full gate. Before a gate, run
    `npm run test:app` once in the release worktree (about a minute) so a pin failure does not cost a 15-minute gate.
  - Practice's phone bar: a key that names the set ("Start 10 questions") is 170 to 190 px wide; measure the text beside it
    (`tmp/1118/tools/barfit.mjs` prints clientWidth against scrollWidth per width and mode) instead of trusting a screenshot.
  - Night highlighter: turning the words dark all at once leaves the words ahead of a slower swipe dark on the dark page; the
    clipped copy (`.dd__over`) fixes it.
  - Git Bash turns a lone `/` argument into `C:/Program Files/Git/`: `MSYS_NO_PATHCONV=1 node strip.mjs label / 390x844 light`.
  - The Lab's phone screens look half empty in a scroll strip because they are caught mid-animation; `tmp/1118/tools/lab.mjs`
    shoots all five at rest (they are full).
- **Round 3 (9:42 pm, main 0c9099f0e):** /features, /about, the footer on every public page, the four guides (briefs `pub-c.md`,
  `pub-d.md`). Look at public pages with `MSYS_NO_PATHCONV=1 node strip.mjs <label> /<path> 390x844 light 780 [base]` from
  `wt-1110-convert/tmp/1110-app`, then `python grid.py shots/<label> 390-light 260 11`. `data/tests/landing_checklist_1104.test.mjs`
  is in no `test:*` script: run it by hand (it caught a keyframe animating `left`).
- **Looked at and left (390 Day, fixtures):** Mob, Result, Your papers, Revise, Explore, Guide read well. Plainest: Colleges
  (signed-in Compass: a long list of text rows) and Saved. Public: /pricing is rich; /features was nine text cards and the four
  article pages were walls of text (both in lanes pub-c and pub-d).

## 3. Signed-in website (the arena)

**17 Nov 2026: Ask Mobi (`/mentor`) is a chat now** (web/1116n-chat, owner LK286): a pinned composer with a labelled Photo key, the thread, History (a side column on wide screens, a sheet on phones), Your record as its own tab; the docked panel shares the chat. The 1-credit rule for an ask Mobi reads but cannot use shows beside the price before sending; Mobi waves once on the start (six-frame sprite) and reads (stills) while waiting. Seen at 390 Day and Night and 1440 Day (`wt-1110-convert/tmp/1116-final/shots/chat-fu`). Fixed 17 Nov: at 390x844 the four start tiles ended 4 px under the composer's fade (Mobi's box 64x82 on phones, gaps 12). Not seen: a real phone keyboard over the composer, a real model reply.

Phone (390, 360): walked in depth on 10 and 11 Nov (LK199-LK224). On 12 Nov only an overflow scan at 360 Day across every view: clean (only decorative SVG parts of Mobi pass the edge, clipped by their own box).

Desktop, looked at on 12 Nov at 1440x900 (all views), 1366x768 and 1920x1080 (six views):

| Page | Verdict | Notes |
|---|---|---|
| Shell | Seen, holds | Content column is 960 px, left-aligned beside the 250 px rail by decision (R8 TOOLS-18, "one left edge"); at 1920 the column sits centred. Do not centre individual pages. |
| Today | Seen, holds | Two columns. Right column is narrow (about 270 px) at 1440. |
| Practice | Seen, holds | Two columns with a sticky summary. **Fixed:** the success toast at launch is gone. |
| Your papers, You, Marks trend, Colleges, Ask Mobi, Explore, Saved, Your standing, Revise | Seen, hold | Two columns where it makes sense. |
| Learn, Key cards | **Fixed 12 Nov** | Were centred (titles at x 317 and 352 against 252 everywhere else); now `margin-inline: 0 auto`. |
| Mob (the den) | **Fixed 12 Nov** | Members and settings side by side from 1100 px (`mob.css`, `:has`). The den scene itself uses the width well. |
| Wallet, Progress, practice result | **Two columns from 1100 px, 16 Nov** (e137d3575) | Left column sticky (score and the next step; the balance; the weeks), right column scrolls; one column while Ask Mobi is docked. Seen at 1440 Day and Night, 1366, 1100. Captures: `wt-1116-desk/tmp/1116-shots/desk/final`. Minor: 1100 to 1180 px, "/ 250 marks" wraps under the score. |
| Guide, Pro sheet, account pop-over | Not re-walked 12 Nov | Checked at 1440 on 10 and 11 Nov. |
| Test-taking screen | **Not seen** | See the trap above. The landing's exam section shows the same component. |

### 3a. Fresh-account states (15 Nov 2026)

Audit `wt-1110-convert/tmp/1115-prod/ux-fresh.md` (on 38a09a4e7: 390 Day and Night, 1440 Day; 196 shots in its `shots/ux-fresh/`). Fixes on branch `web/1115-w2-c` (0578850e4 to fcddb3986), walked again at the same sizes; shots in `wt-1115-w2-c/tmp/1115-shots/w2-c/`.

**Fresh-account recipe:** `/preview/arena?view=<v>&plan=free&data=empty&student=new&decks=real&study=on&mob=none`. `data=empty` answers every account read empty (now traps and Revise too; the Explore bank feed stays, `feed=empty` empties it). `student=new` gives the fresh Key cards and Review. The wallet is fresh by default under either (`wallet=fresh`: 50 free, nothing held, no history, this month's refill date). `referrals=fresh|some|cap|paused|invited|off|down` (default fresh: a code, nobody joined). `mob=none` is now the den's start as production (`none-v2` the old page). `paper=practice5&rules=new` is a first result with no rule. `firstmock=free`, `ai=live`, `guide=auto` as before; `data=error` and `data=loading` for failed and loading.

| Seen and holds (do not re-walk) | Changed 15 Nov |
|---|---|
| Today fresh (hero "Start now", week, road), Start sheet, account sheet, top bar and dock targets, Practice fresh, Learn, a chapter, Explore, Revise empty, Your standing, Colleges, Ask Mobi page and sheet, the den (no Mob, a Mob of one), the guide's six stops, all loading states, Day contrast | U2: one label "Start 10 questions" (`src/lib/firstSet.mjs`) to Practice with the set chosen: Today's first-week practice, Your papers, Revise, Progress, Marks trend, Your standing (empty), Colleges projection, Ask Mobi page and sheet |
| Fresh Wallet (50, "Refills on 1 December", Kept 0) and the "Bring a friend" card: first seen 15 Nov, both hold | U3: the scene failed-load Try again, Saved's keys and Revise's empty key carry `data-page-primary` (dock and sidebar Start go quiet) |
| | U5: Marks trend says "No sessions yet.", the empty record has the volt first-set key, "Your rules (n)" waits for a first rule, "...first Full or NTA mock. Your account keeps its record." |
| | U6: "...is chosen in Your rules." stays one sentence at 360 (inline link, 44 px from padding) |
| | U7: the run row reads "Day 1 / Your first week at your goal" with no session, "Not yet" after; a new Mob's pennant says "New"; badges untouched |
| | U8: Your papers empty and failed: room left, words right from 1024 px. U9: Saved's room is 225 px wide on a phone, key above the dock |
| | U10: Key cards, nothing due and nothing added: names the first chapter, outlined "Open the chapter" to its deck |
| | U11: every Today read failed: one card, one Try again that reads everything again; a part failing alone keeps its own retry |

**Open, and whose:** U1 first-session Pro sheet timing (result lane, owner's call); U4 "Keep the momentum" after a blank paper (result lane); U12 two colleges offers on Today (owner, R3); U13 "Did your rule hold" on a first paper (result lane; `rules=new` now shows it); U18 Guide vs Show me around (owner's copy). The app's `ask_doors.dart` still says "Practise 10 questions first"; `denCopy.mjs` `pennantLabel(0)` still reads "0 weeks in a row" aloud. Today's day-one hero keeps "Start now" (judged sound); Your standing's ranked state keeps "Start a practice session" (not a first step).

**Traps:** the preview answers in the page, so Playwright's request log stays empty after a retry: judge by the screen. Headless mobile can lay the Marks trend key under the dock at load; scroll before clicking. In a column flex parent a scene room's 372 px flex-basis becomes its height (the Saved bug): give it `flex: none`. Tests pin preview and Today source lines (`today_r3`, `today_bundle`, `learn_integration`, `my_colleges`, `practice_parity_1020`): change those lines with their test.

---

### 3b. New surfaces, 15 Nov 2026 night (merged branch 41710cfc4, webpack dev; 390 Day, 390 Night, 1440 Day)

Seen and hold: `/daily` (start, a guest run to the score), `/du-cutoffs`, `/du-cutoffs/b-com-hons`,
`/du-cutoffs/colleges/hindu-college`, `/sunday-mock`, `/signup` (Open in Chrome line in Android in-app browsers), the public
bar with Daily Five (desktop and the phone menu), Today with all 17 Sunday card states, the den with the Daily Five strip and
the 5 Sunday block states, Practice (Sunday chip, Average score), the result (open and held Sunday). Captures:
`wt-1115-look/tmp/look/` (the worktree may be removed; copies in `wt-1110-convert/tmp/1115-prod/lane-shots/`).

Open: the `/sunday` page has no top-bar title (1440); `/daily` loading placeholder taller than the card (CLS 0.05-0.08, also
live); the first-paint join (`web/1115-paint`, reverted from the release) put `home-sheets.css` before `scroll-story.css`,
`section-position.css` and `du.css` in the webpack build: tour hold +502 px at 390, Lab cinema -144 px, the DU teaser card
fill wrong in both themes. Trap: local webpack builds already differ from live Turbopack in sheet order (the local home page
is 359 px taller at 390 than live, 21,244 against 20,885), so compare cascade questions against production, not local.

### 3c. 16 Nov 2026 (main 15286120f; 360, 390 Day and Night, 1440 Day; headless Chrome, real pointer clicks)

Seen and hold: the home page's two calendar pages under the sample card (`.dfh`, DailyFiveRow.jsx: Daily Five open, begun,
played; the Sunday Mock page), as wide as the desk at 360 to 1920 (tmp/1116-daily/widths.mjs), nothing covering them;
`/daily` start, playing, result, the played return, signed in with an account record, the failed load; `/key-cards`, a
chapter, its end state, a 404; the reading line on the home bar; the shell's loading skeleton; the Log in wait. Captures:
`wt-1110-convert/tmp/1116-daily/shots` and `merged`, and each lane's `tmp/1116-shots/<lane>/`.
Tools added: `tmp/1116-daily/shots.mjs <WxH> <theme>` (the Daily Five walk with a hit-test before every click, layout shift
reported), `widths.mjs`, `pages.mjs`, `merged.mjs`. Fixture: `/preview/daily?daily=none|played|error&auth=out&fresh=1`.
Traps: the home page's sections measure differently before they are scrolled near (content-visibility), so compare section
heights on production in the same browser, before and after; the in-app browser pane does not run timers or observers until
a frame is drawn, so a clock can look empty in its first screenshot; a first visit's block shows the open state for one
frame before this device's record is read. Badges (16 Nov, 91f8f8aaf): one family of stamped marks, three states, the earning moment in the result page and Today; dev sheet of every mark at `/preview/badges`; captures `wt-1116-badges/tmp/1116-shots/badges`. Tablet walk (768x1024, 1024x768, Day, 20 views): nothing past the edge or under the dock.
16 Nov, later (main 79672593c): seen and hold: the home page's bring-a-mistake block (360, 390 Day and Night, 1440; real pointer on the check; `tmp/1116-daily/bmk.mjs`), the Sunday Mock page's day band, `/corrections` (390 Day and Night, 1440), onboarding's last key with and without a promised page and the arrival lines (`wt-1116-first/tmp/1116-shots/first`), class leagues' states through fixtures (`wt-1116-league/tmp/1116-shots/league`; the feature is OFF in production). Traps: in Git Bash a lone `/` argument becomes a Windows path (`MSYS_NO_PATHCONV=1`); a stamped `.lp-head--left` goes two-up on desktop (make it a column when a block stands beside it).
Open: the other loading states listed in lane load's report (nine button
spinners, two skeleton shimmers, the sign-in wait shown to signed-out visitors); the Sunday page's key is quiet by choice.

## 4. Android app (1.0.23+21)

Looked at on 12 Nov: 117 emulator shots of the demo build (Today to the bottom, Start sheet, Practice with its four sub-tabs, a Quick practice from setup to result, the repair flow, Mob, You, the account sheet and every row, Wallet, Ask Mobi, Colleges; Day for the main ones), the onboarding reference renders, and the release build's first run through the college step.

Holds, do not re-examine without a reason: Today, the Start sheet, Practice setup, the runner, the palette, the result, the repair flow, Papers, You, Wallet, Notifications, Theme and appearance, and every onboarding step.

Fixed 12 Nov (commits 1a7349291, c79dac51c):
- The band under the bottom bar closes (`BarScrim`: `underBar` 0.92, `underShare` 0.25, `atScreenBottom` 0.96). The see-through of the bar itself is unchanged (0.12 and 0.22): the owner likes the glass and content must show through it.
- Account sheet: "Credits" once, the balance lined up under it, no reserved empty line.
- Opening screen: a clear status tint, so the lamp light runs to the top.
- Welcome screen: clear system bars. `SystemUiOverlayStyle.light` and `.dark` carry an opaque black navigation bar; never use those presets in this app.
- The Privacy row opens a page titled Privacy.

Seen and left, with the reason:
- Practice result at rest: the "50% / 2" tally row is half hidden behind the fixed foot. It is the finish stage's own trade-off (a 24 dp fade exists); changing it needs a layout decision.
- Repair ending at rest: one line of the explainer is cut by the foot. Same cause.
- The submit page's back key is a round arrow while other pages use a "Back" pill: a pill would put two labels on one action ("Keep working").
- Back on a page opened from the account sheet closes the page and the sheet together. By design.
- Demo-only mismatches (Wallet 46 against 45 elsewhere, "54 mistakes" after a repair, "in Mock 1"): fixture limits listed in `flutter_app/docs/DEMO-BUILD.md`.

Old reference-image drift, not caused by this pass and not re-recorded: `credits` (10; they fail without the 12 Nov changes too), `core/start_v13 following_picked`, `art_scenes welcome` and `plan_seal_struck`, `today_resume` (date-dependent), `result card4_share`.

Not checked: a physical phone; a sign-in in the release build; the first-run flow after the college step on a device; the Mob, Learn and Key cards on a device (they need servers the demo does not have).

### 4a. Android app 1.0.24+22 (17 Nov 2026, ui/1117-final 0a00993b6; owner LK300)

Looked at on the emulator (mockmob_budget, 720x1600; shots in `wt-1117-app-final/tmp/1117-walk/`): the release build installed
over 21 and opened (the "mo" opening, the welcome); the demo build: Today (top to the road, the new "Daily streak" block and
"This week's goal"), Ask Mobi's chat start (Mobi, the record line, four priced starters, the composer with the labelled Photo
key, the credit line), You, Practice, and NTA mode end to end (instructions with the tick, Start at 00:59:57, a chosen option
says "Not saved yet" with 0 answered, Save & Next counts it, back shows "Saved" and Answered). Reference images looked at by
the lanes and by me: Daily Five admit card with seat and "Playing for" and the calendar Mobi, the college board, the NTA held
state, the den's "Your daily streak" sheet and the week sheet's streak link.

Demo limits (not defects): the Daily Five page shows "Today's five did not load" and the streak block "Your streak did not
load" in the demo build (no stand-in server for the new APIs); both read production in the real build.

Old drift confirmed on the 1.0.23 base (fail there too): `explore_door` (4), `week_sheet_*` (6), `today_resume` (2). The Mob
den and sheet images were re-recorded on purpose (the streak's words) and looked at.

---

## 5. Open candidates for visible change (owner's to pick; none started)

1. A portrait cut of the hero film for phones. Owner, 12 Nov: "Not now". Do not raise it again unless he does.
2. The hero's first screen on a phone: mostly words and two keys, with the film cut off at the fold. A rework that shows the product above the fold.
3. The feature strip under the film on phones: tighten it so the sample comes up sooner.
4. Desktop layouts for Wallet, Progress and the practice result.
5. The app's result and repair-ending feet (the half-hidden row at rest).

Owner constraints that bound all of this: refine, do not rebuild (rejected restructures on 15, 17 and 18 Oct); nothing hidden or cut from the signed-in product without a reason told to him; one accent (volt) for the primary action; no facts or claims the code does not back; he judges on his phone.

---

## 5a. Smoothness: how to measure it and what has been found (19 Nov 2026)

Tools in `wt-1110-convert/tmp/1119-phone/` (not shipped). All use a production build (or the live site), headless Chrome not
marked as driven so the opening really runs, 390x844, CPU x4. Run on a quiet machine. Prefix `MSYS_NO_PATHCONV=1` when an
argument is a lone `/`.

| Need | Command |
|---|---|
| Frame pacing, first 6 s and a full scroll | `node tmp/1119-phone/perf2.mjs <label> <base> short 4` (`first` for a first visit) |
| Who starts each long script (event, timer, script tag) | `node tmp/1119-phone/loaf.mjs <base> short 4 7000` |
| The longest tasks opened up: trace events and sampled JavaScript | `node tmp/1119-phone/task.mjs <base> short 7000 4 2` |
| Style recalculations with what invalidated them | `node tmp/1119-phone/style.mjs <label> <base> load 4 25` (`scroll` for scrolling) |
| What the GPU and raster threads do in the longest scroll stall | `node tmp/1119-phone/rast.mjs <base> 5 4`, then `rast_read.mjs` |
| Universal sibling selectors in what a page really loads | `node tmp/1119-phone/owl_built.mjs <base> /` (source: `python tmp/1119-phone/owl.py`) |
| The session provider's three first answers, no real sign-in | `node tmp/1119-phone/authsim.mjs <dev base>` |

Found, with the cure (each is pinned by a test):
- **`:has()` with an attribute or pseudo-class inside, or anchored on html/body with a descendant inside**: the browser rescans
  the page on every DOM insert or remove (3.2 ms per change on a fast PC on the home page; 0.003 ms without). Cure: the owning
  component mirrors the state onto an ancestor as a plain attribute; page-kind rules are child-only
  (`html:has(> :where(body) > .mm)`). Done for the home page. **Not done for the signed-in site** (30 rules in `arena.css`
  alone).
- **A context value that changes above parts of the page not yet hydrated** (the session provider, around every page): React
  hydrates every Suspense boundary in one blocking task (577 to 851 ms at CPU x4 on the live home page). Cure: state in a
  store read with `useSyncExternalStore`, a context value that never changes. Any new page-wide provider must follow this.
- **A bare `*` on the left of `+` or `~`** (`> * + *`): every element added or removed under a parent restyles that parent's
  whole subtree; a script appended to `<body>` restyled the whole page. Cure: `> :where(:not(:first-child))`.
- **Selectors ending in `*` keyed on an `<html>` attribute, custom properties written on `<html>`, `CSS.registerProperty` at
  load**: each restyles the whole page once. Cure in the opening: a variable on the layer, a one-rule `<style>`, `@property`.
- **One 0.4 s stall on the second swipe of a scroll, in the old and the new build:** not the page. The trace shows a single GPU
  raster flush with shader compilation, which a fresh headless profile does on first use and a phone caches. Do not chase it
  in the lab; it needs a physical phone.
- Still open: the first frame itself (parse, style and layout of the page, 230 to 450 ms at CPU x4 before anything shows); the
  Mistake Lab's step swaps (about 450 elements restyled a step); the first drawing of skipped sections while scrolling.

## 6. Change log of this file

- 12 Nov 2026: created from the final pass (LK225-LK230).
- 13 Nov 2026: section 2a added (round 13, the home page's motion; LK232-LK236).
- 15 Nov 2026: section 3a added (fresh-account states, ux-fresh audit and lane W2-C fixes).
- 16 Nov 2026: section 3c added (the Daily Five pages, the week's pages, the merged wave).
- 16 Nov 2026, evening: section 2c (round 16, the phone pass after the owner's look at the live site).
- 17 Nov 2026: section 2d (the merged night lanes, the companion and DU head fixes) and the Ask Mobi chat note in section 3.
- 18 Nov 2026: section 2f (the rebuild: the tour as a deck the scroll deals, the pen and the highlighter, Today's streak block; the dropped 3D Mobi; four traps).
- 19 Nov 2026: section 5a added (smoothness: the tools, three page-wide causes and their cures, the shader stall that is not ours). Home page of this log's section 2 changed on 19 Nov (main e8a2d917d): marks, bottom bar, exam screen, desktop note, Daily Five head, Compass autoplay, DU courses removed, pricing above Instagram.
- 19 Nov 2026, 7:45 pm: desktop home (main c22456209): a pointer layer for fine pointers (`DesktopCursor.jsx`: named cursor via `data-cursor`, leaning primary keys, `data-tilt` pictures, a torch on the paper, ring stretch on scroll), scroll depth on three section pictures, marks spaced from their neighbours from 960 px. Tools: `tmp/1119-phone/marks.mjs` (every mark photographed and measured), `fx.mjs` (the pointer layer photographed), `depth.mjs`. Before judging desktop, run `marks.mjs` and `wheel.mjs` at 1440.
- 19 Nov 2026, 8:31 pm: desktop home (main ddecb3941): sticky cards in Key cards and Ask Mobi (from 1100x780), signed-in Today at 1120 px from 1360, the ring re-aims after a scroll, the torch is out over pictures, loop marks 0.17 of the type size wider than the word with 0.16em (desktop) and 0.13em (phone) of room. Tools added in `tmp/1119-phone/`: `sweep.mjs` (errors, overflow, clipped text), `hover.mjs` (hover census; first instance of each kind only), `ptrperf.mjs`, `reaim.mjs`, `motion.mjs`, `sticky.mjs`, `under.mjs`.
- 19 Nov 2026, 11:40 pm: after the owner's look with a mouse on a 27 inch screen (main ea1bdfa68, then 2e7430340; ledger LK337 to LK351). Home: the ring snaps onto keys (`.lp-snap`), Mobi rides the page line on wide windows, marks wait for the page to stop under a mouse, guide `WAYPOINTS` (the Lab, the tour and Key cards had no seat, so he stood in one pose for half the page), eyes in the reading, camera and calendar poses. Signed-in: Ctrl+Space and the first-use line in Search, the Ask Mobi key and dock, the streak as one highlighter line (`StreakLine.jsx`), pages centred and stepped to 2560 px, the Practice card's edge, Marks trend hover. Tools added in `wt-1110-convert/tmp/1119-phone/`: `app.mjs` (any signed-in fixture at any size and theme, full page), `snap.mjs`, `bar.mjs`, `mobi.mjs`, `mobipause.mjs`, `mobiposes.mjs`, `phoneseats.mjs`, `liveshell.mjs` (the shell on a deployed site with a simulated session). Traps: `/preview/arena` is 404 on production; full-page shots never scroll, so anything that inks in on view (the answer sheet on Marks trend) looks empty in them.
- 20 Nov 2026, 3:15 am: speed pass and signed-in refinements (main 46b3cc8b2; ledger LK352 to LK358). Measure with the processor slowed 6x: `tmp/1120-speed/chromebook.mjs` (desktop, a Chromebook's window), `tmp/1119-phone/perf2.mjs` (phone), `tracedesk.mjs` (what the main thread does at rest, on pointer, on scroll). Lessons: a custom property written per frame on a parent restyles its whole subtree; getBoundingClientRect, checkVisibility and getAnimations on a node inside an undrawn section each lay that section out; judge from the section's own box.

## 22 Nov 2026, 12:48 AM IST — LK365 release 10ef17bf0

Candidate main 10ef17bf0814e95289a07dcc0af75f85269693e5. Chrome viewports 390×844 light and Android touch, 360×676 dark and Android touch, and 1440×900 light with mouse and wheel. Evidence under wt-1110-convert/tmp/1121-stories/.

| Area | Evidence |
|---|---|
| OnePlace | Reviewed all six rows at all three sizes. At 1440×900 the first film found six presses below the viewport. The fixed trigger waits for actual controls to fit, and the second desktop film recorded 26 of 26 presses in the viewport on their controls. Both phone films recorded 26 of 26. |
| Mistake Lab | All five scenes advanced in the gesture-arrival film at each viewport. Inspected stacked panels and their reveals. A small existing native touch settle overshoot in the shared scroll controller remains. |
| Daily | Inspected the homepage demo, confirmed the dock clears its primary key and played all five personal fixture questions. Checked resumed, finished, shared, signed-out and fail-soft fixture states. The personal ending counted actual feedback responses and offered Revise. Fresh-device retry, day-mode concurrency, held questions and side-write failures covered by fakes. |
| Streak | Tested the new phone-header chip and sheet at the two phone sizes. Controls measured at least 44 px high. Checked makeup, counted, new and the tick-up fixture, plus desktop Today. |
| Compass and pricing | Checked score movement during scroll, explicit Pause and Play, and the end corners of the pricing picker at all three sizes. |
| Android nudge | Visible with the development query and Android browser profile at both phone sizes. Hidden in the desktop profile. Play returned 404. The production nudge stays off. |

The release gate in wt-1116-next/tmp/gate2.log passed all 24 suites, ESLint, Webpack and Turbopack. The separate landing checklist passed 43 with 12 existing TODOs. Production Chrome smoke at 390×844 light, 360×676 dark and 1440×900 light confirmed Daily CTA hit testing, Compass autoplay and Pause, pricing edge taps and the hidden Android nudge. The live short-phone film reached all six rows in 12.6–14.5 seconds each with 26 of 26 cursor presses in the viewport and on the right controls. Its console had CSS preload warnings only. Compass on live Chrome at 390×844 with 6× CPU slowdown measured six frames over 50 ms out of 172 playing, versus zero out of 288 paused. Signed-out GET /api/daily/mine returned 401. Vercel had no [daily-mine] events and no /api/daily/mine error or fatal entries in the first 5 minutes 19 seconds after READY.

No personal five was tried signed in on production. No owner device or iPhone hardware was tested.


## 22 Nov 2026, 2:23 AM IST: LK366 release aa15bc996 (orchestrator's own look)

Looked at with Chrome, phone context (touch, Android user agent, CPU 6x) at 390x844 light and 360x676 dark, and 1440x900
light with a mouse wheel. Films and contact sheets: `wt-1110-convert/tmp/1122-lk366/`.

| Area | Before (release 10ef17bf0) | After |
|---|---|---|
| One place, Practise | Olive outline boxes round groups, the rest at 0.4; 12.3 s scripted | No box, nothing dimmed; three beats, 10.7 s scripted. `film-390x844-light/sheet-practise-1.jpg`, `film-360x676-dark/` |
| One place, Key cards | Card dimmed while rating, box round the keys, third line with nothing shown; 11.5 s | No box; the rated card is filed with a time line ("This card is back in 3 days."); 10.1 s. `kc-both.jpg` |
| One place, desktop | n/a | Plays with no boxes once the working screen's foot is in the window. `orchdesk-1440x900-light/sheet-1.jpg` |
| Mistake Lab | Five scenes over in 11 s (`lab2-390x844-light/`); device cut by the band before the pin | About 7 s a scene, 35 s in all; content whole at both phone sizes; glides in and plays from the approach. `orchlab-390x844-light/sheet-1.jpg` |
| Daily Five | Five layers of words, a card in a card, 3 s beats, demo cut by the window (`daily-390x844-light/`) | One surface, plain captions, 3.6 s or more a beat, always in view. `daily-card-390x844-light/sheet-1.jpg` |
| Compass | Bars jump 3 px a step, no easing | Glide: median movement 0.14 px a frame (lane measurement) |
| Android nudge | Not reachable on the live site | `/?appnudge=1`: `nudge-390x844-light/f001.jpg` |

Not looked at: a real phone, an iPhone, the Daily block's signed-in states, the Lab's 10-arrival test at 360x676.

22 Nov 2026, about 6:10 am IST (LK368, Mistake Lab cards): earlier look vs new look filmed at 360x640, 360x676, 390x844, 1440x900 (wt-1110-convert/tmp/1122-lab old-*, new-*). Earlier screens won on pictures (chapter bars by question, pace line with hatched overrun, picks and arrows, the struck pick); new look won on real UI, cursor and stack but its cards were settings lists with empty reserved room. Combined cards built: one finding with one pen mark, one picture, the slot; all fit at full size at the four sizes in both themes, nothing under 14 px (after: final-*/sheet-1.jpg). Open: a real phone look; desktop cards keep 100 to 180 px empty under their content.


## 22 Nov 2026, 7:35 AM IST: LK368 release fb7f3bbcc (orchestrator's own look)

| Area | What was looked at |
|---|---|
| Coverage pages | Builder's sheets at 360 dark, 390 light, 1440 light (wt-1110-convert/tmp/1122-coverage/look/); live addresses answer 200; the index shows the built total. Not looked at on a phone. |
| Mistake Lab | Session's final films at 360x640, 390x844, 1440 (tmp/1122-lab/final-*); live film at 360x640 after release aae55e759 (tmp/1122-lk366/livelab2-360x640-light/sheet-1.jpg): scenes about 7 s, cards whole. |
| Hero film v6 | One frame per chapter (MockMob-promo-film/out/hero/v6_sheet_*.png, tiled in tmp/1122-coverage/film-grid.jpg); the session's page check at 390 and 1440. Sound not heard. |


## 22 Nov 2026, 12:43 pm IST: release 8c74cca7c (coverage after the wave 5 publish; orchestrator's own look)

| Area | What was looked at |
|---|---|
| Coverage index | Dev server at 390 wide: 92% of 416, 84 same and 21 new numbers, 114 of 114 chapters, nine subject tiles with Accountancy first; no sideways scroll. Live address checked after the deploy. Not looked at on a phone. |
| Accountancy page | Dev server at 390 wide: 98%, 54 of 55, four status rows, the Q3 card shows NTA's question beside the new MockMob question; check date 22 November. |
| Home teaser | Text only (the section mounts late): 92%, six rows led by Accountancy. No layout change was made. |


## 22 Nov 2026, 12:55 pm IST: hero film (orchestrator's own look)

| Area | What was looked at |
|---|---|
| v5 against v6 | One frame every 2.5 s of both films, side by side (scratchpad film-v5-sheet-*, film-v6-sheet-*): v5 = staged scenes in devices, Mobi, big fact cards; v6 = small flat recordings in one window, type too small, no devices, no Mobi. The owner's verdict matches. |
| Hero after the roll-back | Live page serves hero-v5 posters (curl of www.mockmob.in at 12:43 pm). Not looked at on a phone. |
| v7 scenes | Three rounds of 3 fps half-size frames of chapters 01 to 09 (MockMob-promo-film/out/hero/v7/seq1, seq2, seq3 sheets): kept v5 scenes land on the new words; new scenes fixed for size, overflow and overlap. Full master not yet reviewed; sound not heard. |


## 23 Nov 2026, about 2:00 pm IST: website pass LK427 (orchestrator's own look, before release)

Looked at with headless Chrome in a phone context (touch, Android user agent) at 390x844 Day and Night and 360x640 Night, and at
1440x900 Day and Night. Tools and pictures: `wt-1110-convert/tmp/1123/` (`shot.mjs` one part of a page, `film.mjs` a self-playing
demo with a log of where the demo cursor rests, `cov-walk.mjs` real taps through the CUET 2026 section, `lab-end.mjs`,
`hash-land.mjs`, `compass-watch.mjs`; pictures in `tmp/1123/out/`). The pane browser's screenshots were cropped after a scripted
scroll, so every picture is from the scripts.

| Area | Before | After |
|---|---|---|
| CUET 2026 on the home page | A teaser: 92%, six of nine subjects as bars, no streams, no question level. | Question by question: stream tabs, subject chips with percent, a strip of every question by status, NTA's question beside the MockMob question or Key card. Tabs to the end of the pair = 1.42 screens at 390x844 (2.0 at 360x640). Real taps checked: Q3 new numbers, Q23 not yet, a reading-skill item, the Science note, a match-list table with "Show all". `cov2-390x844-light.jpg`, `cov4-sheet.jpg`, `walk-sheet-a.jpg`, `walk-sheet-b.jpg`. |
| CUET 2026, Night | n/a | The "Same question" ring was lost on the dark ground; it is now a dark ring inside a volt edge (both themes). |
| Daily Five | A six-line paragraph, a faint "Example" chip, the demo cursor parked on row 5 for the whole first beat. | One short line and three small pictures (get one wrong, it comes back, the streak grows); a solid "Example" mark; the cursor shows only while it taps. `daily1-390x844-light.jpg`, `dfilm-sheet-390x844-light.jpg`. |
| Demo cursor (one-place rows, Lab, Daily) | Rested on the words of the screen between taps. | Shows only while it moves and presses; logged at 1.5 s steps over all six rows: 3 resting samples before the last fix (all pointing moves), 0 in the Lab and the Daily Five after it. `opfilm-sheet-390x844-light.jpg`, `labfilm-sheet-390x844-light.jpg`. |
| Mistake Lab bottom bar | Stayed on until the Lab was half off the screen, over the next section's first line (measured: bar on while the next heading rose from 849 to 509 px). | Leaves as soon as the next section shows (bar off at 749 px). |
| DU Compass tour | Swept 600 to 960 on every list: "0 of 10 cleared" for half of each round on the first list. | Sweeps the list's own cutoffs: 800 to 950 on the first list, 1 of 10 cleared at its lowest, 10 of 10 at its highest (logged over one round). Still card starts at 860. |
| Deep links on a phone | /#compass stayed at the top of the page; /#pricing stopped 980 px short. | /#cuet-2026, /#compass, /#pricing, /#daily-and-sunday land with the section at the top. |
| Desktop guide (Mobi) | Stood on the CUET section's last lines while the pricing seat was below the window. | Waits in his lane at the right. `cov5-small.jpg`. |

Looked at and left: the six one-place rows play in 10.5 to 15 s each with nothing cut at 390x844; the Lab's five scenes take about
33 s and fit; the Lab's desktop cards keep reserved room for lines that arrive on a tap (a centring change was tried and undone:
not proven better). Not changed: the Lab's scroll length on a phone (the tuned flow model); the four generated subject objects
under the Statement (the owner's checklist L-038 says keep the shelf; his LK367 words call that art family "AI slop": his call).

Not looked at: a real phone, an iPhone, Safari, Firefox, the page at 360 wide in Day, any signed-in page.
