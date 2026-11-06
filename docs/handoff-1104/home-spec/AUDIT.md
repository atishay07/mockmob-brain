# Live home page audit, 4 Nov 2026 (LK67 to LK75)

Subject: https://www.mockmob.in/ as a student sees it (read-only; no sign-in, no DB, no repo edits). Code read: `wt-1104-web-polish/src/app/page.js`, `src/components/landing/*`, the CSS files named below. Local dev server http://localhost:3452 used only for the real exam runner preview.

Times: the first capture burst ran 2:24 to 2:48 am IST; part 2 (real runner, CPU-4x perf, exam measures) ran 3:30 to 3:50 am IST. All paths are under `C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/audit/` unless absolute.

## 0. What to trust, and what was wrong in the stopped run

| earlier file | verdict |
|---|---|
| `data/gesture-390.json`, the "scroll" block of `data/perf-390-cpu4x.json` | INVALID. Taken in `chrome-headless-shell`, where touch and wheel input never scrolled the page (`ys` is 0 in every row, `stepsMoved` 0 in every row). The CPU-4x load numbers in that file (LCP 2392, TBT 190) were taken with the headless shell and are lower than the real-Chrome numbers below. Use `perf3-lean-390-cpu4x.json`. |
| `data/runner.json` | INVALID. The preview needs a `generationKey` of 12 or more characters (`TestPageClient.jsx:332`); the old run used a short one and every shot is the "This did not load / Missing generation key" error. Replaced by `data/runner2.json` and `shots/runner/*`. |
| `data/hover*`, `shots/hover` | the hover job failed (CDP mouse error). Not needed: phones have no hover. |
| `data/page-*.json`, `crops-*.json`, `neon-*.json`, `herotime.json`, `shots/390-*`, `shots/1440-*` | re-checked against screenshots; good. |
| `data/perf2-390-cpu4x.json` | real Chrome WITH my instrumentation (rAF/setTimeout wrappers that capture a stack, and the sampling profiler). It inflates cost (the wrapper alone cost 1.4 s). Use it only for WHO is expensive, not for how much. |
| `data/perf3-lean-390-cpu4x.json` | real Chrome, no wrappers, no profiler: the honest numbers (section 5). |
| `data/exam-measure.json` | heights of the home exam section parts (section 4). |

Scripts: `scripts/home-audit.mjs` (part 1), `scripts/home-audit2.mjs` (runner, perf; `LEAN=1` for the lean run), `scripts/exam-measure.mjs`. The other agent's real-touch scroll work is in `wt-1104-web-polish/tmp/home-1104/scroll/` (`results-perf.json`: 11 frames over 25 ms at CPU 4x versus 2 at 1x, through the lab). Not repeated here.

## 1. The hero, phone versus desktop

### 1.1 Components and files

Hero markup: `src/app/page.js:176-235`. Phone (up to 760 px) and desktop (761 px up) are one section with two Mobi variants; CSS switches them (`src/app/hero-scene.css:19` and `:26`).

| piece | file | phone 390 | desktop 1440 |
|---|---|---|---|
| painted room (Play app welcome room, AVIF, lazy) | `landing/HeroRoom.jsx` (box `.lp-hero__greeting`, `hero-scene.css:163-190`) | drawn: 320 px tall at 844 (`--room-h: clamp(17rem, 38svh, 20rem)`, `hero-scene.css:165`) | `display:none` |
| Mobi rig + speech bubble | `landing/HeroMobi.jsx` `variant="room"` (178 px size const, `HeroMobi.jsx:31`) | figure 143x172 at (132,192), bubble 147x39 | `variant="host"` (140): 117x140 at (627,564), bubble 144x58, in the gutter at the lower left of the demo card |
| six tap lines | `landing/heroTaps.mjs:12-27` | yes | the same six lines |
| headline (static, three runs) | `page.js:187-193`, words in `landing/heroLines.mjs:12` | 114 px tall at y 393 | 178 px tall at y 180 |
| lead, CTA, trust lines | `page.js:195-209`, `LandingActions` | lead y 519, CTA y 586-688 | lead y 379, CTA y 461-515 |
| demo drill card ("Your first question. Go.") | `page.js:219-229`, `landing/DemoDrill.jsx` | below the fold: starts y 759 at 844 | right column, 453x548 at (773,133), fully in view |
| proof dock (4 facts) | `page.js:231-235`, `hero-depth.css:35-47` | below the fold | y 740-843, in view |
| backdrop (hairline grid, dots, pointer spot) | `landing/HeroBackdrop.jsx` | grid and dots on a `scroll(root)` timeline | same; pointer spot only for a fine pointer |

### 1.2 What fills the first screen (measured, `data/page-*.json` `hero.boxes`, `data/herotime.json`)

| viewport | site bar | room (Mobi + bubble + painting) | headline starts at | words in the first screen | CTA bottom | demo card |
|---|---|---|---|---|---|---|
| 390x844 | 61 px (7.2 %) | 320 px (37.9 %) | y 393 (46.6 %) | about 55, text covers 20.0 % of the area | y 688 (81 %) | starts y 759, cut off |
| 412x780 (Pixel, URL bar) | 61 (7.8 %) | 296 (38.0 %) | y 369 (47.3 %) | text 21.6 % | y 671 (86 %) | below |
| 390x664 (iPhone Safari with bars) | 61 (9.2 %) | 272 (41.0 %) | y 345 (52.0 %) | text 21.9 % | y 640 (96 %) | below |
| 360x640 (small Android) | 61 (9.5 %) | 272 (42.5 %) | y 345 (53.9 %) | text 21.2 % | y 630 (98 %) | below |
| 1440x900 | 61 (6.8 %) | none | y 180 | text 14.8 % | y 515 | in view, right column |

So on a phone the room plus the site bar is 45 to 52 % of the height before a single word of the headline, and the Mobi figure itself is only 7.5 % of the area: the rest of that band is painted room (window, lamp, shelf, answer sheet). Screens: `shots/390-day/00-first-screen.png`, `shots/390-night/00-first-screen.png`, `shots/herotime/390x664-day.png`, `shots/herotime/360x640-night.png`, `shots/1440-day/00-first-screen.png`, `shots/1440-night/00-first-screen.png`.

Does anything say CUET, exam, mocks or what MockMob is? (text-node scan of the first screen, `hero.mentions`):
- Phone: "CUET" yes (headline "CUET 2027."), "mock" yes ("One mock.", lead, bank line), "exam" NO. The headline is on screen at every size tested (it is not pushed off the fold), but nowhere does a sentence say what MockMob is (a CUET mock-test and mistake-analysis site). The word "MockMob" appears only in the logo. The only words in the top 45 % of the phone screen are the bubble "Hi, I'm Mobi. Tap me." and the site bar's "Light or dark? Your call" tooltip.
- Desktop: CUET, exam ("Try the exam-day screen"), mock all present; the nav adds "Free mock test", "Cutoff calculator".
- Page title (tab): "CUET Mock Tests & Practice Questions | MockMob" (`data/page-390-day.json` `theme.title`).
- The headline has no motion: at 500 ms it is already opacity 1 (`data/herotime.json` rows 0 to 9). Only the bubble fades in, at about 1.6 s. There is no entrance sequence and no typing on either hero (the comment at `heroLines.mjs:1-10` records that the owner ruled it static on 1 Nov).

### 1.3 Mobi on the phone: taps (shots: `shots/390-day/M1a..M4b-*.png`, `shots/390-night/M1a..M4b-*.png`; rig state in `data/page-390-*.json` `mobi.taps`)

Before any tap: bubble "Hi, I'm Mobi. Tap me.", act `curious` (looks down at the key once at 3.5 s if untouched, `HeroMobi.jsx:130-134`).

| tap | bubble line | what else changes |
|---|---|---|
| 1 | "I find where your marks slip." | MobiReact `hello` act; the site-bar Mobi winks (`HeroMobi.jsx:160`, `wink()` at :194); Night: the first volt circle fills on the painted answer sheet 120 ms later (`HeroRoom.jsx:57-65`); Android buzz 8 ms (`HeroMobi.jsx:169`) |
| 2 | "One timed mock shows me the chapter." | next act of MobiReact's cycle (hello, tilt, hop, startle; never the same twice); next sheet circle (Night) |
| 3 | "5,765 questions. A fresh mock every time." (live bank count from /api/stats) | same |
| 4 | "Okay, okay. Try five questions?" | the "Try five questions" key lifts 2 px once (`HeroMobi.jsx:161`, `liftKey()` :201) |
| 5 | "Free to start. These five need no signup." | |
| 6+ | "That's all my tips. Go on, try one." stays; later taps only squash | |

Observations from the shots: the bubble grows from 1 line to 2 lines on tap 1 and sits over the window/lamp of the painting; Mobi moves (tilt, hop) inside a fixed painted room; nothing on the rest of the screen reacts except the Night answer sheet. The sequence teaches the page's pitch in six taps ("where marks slip", "timed mock", "5,765 questions", "try five") but only a student who taps ever reads it; a non-tapper sees "Tap me." and nothing else. This is the LK67 "weird" part: a toy interaction that carries the product pitch, in a spot (the top 38 %) where the real pitch should be.

### 1.4 Desktop: does it have Mobi? Yes, but small and detached

Desktop shows the same Mobi as the sample's host (`HeroMobi variant="host"`), 117x140 (1.3 % of the first screen, 1.9 % with its bubble), standing in the gutter at the lower left of the demo card, default act `nudge` (pointing at the card), reacting to the sample's answers (`pip:react` for the hero, `HeroMobi.jsx:137-149`). He answers the same six taps, with the same lines (`shots/1440-day/M1..M4-host-click*.png`; acts after tap: hello, then `nudge`). There is no room, no painted light, no site-bar wink coupling beyond the same code path, no key-lift visible. Parity gap summary:

| | phone | desktop |
|---|---|---|
| Mobi size | 143x172 + painted room 390x320 | 117x140, no room |
| hero's top band | Mobi and decoration | the headline and the live demo |
| tap pitch lines | prominent, over the room | small bubble beside the card |
| answers the demo | no (the demo is below the fold) | yes (correct, encourage) |
| first-screen words that say what MockMob is | none | none, but the nav and the "exam-day" link carry exam words |
| LCP element | the room painting (AVIF, 124,800 px) at 2.9 to 3.3 s at CPU 4x | not measured on desktop |

One hero idea on both would have to decide whether Mobi is the stage (phone) or the host of the live question (desktop). Also note a phone-only runtime cost: the rig loads on idle and then updates SVG attributes every frame (section 5.4).

## 2. Night neon: top 15 offenders

Source: `data/neon-390-night.json` (95 selector groups, 320 elements) and `neon-1440-night.json` (102 groups, 336 elements); `data/neon-390-compare.txt` (Night versus Day side by side). Classifier in `scripts/home-audit.mjs` (`classify`).

Page totals, Night versus Day at 390: volt edges (borders, rings) 123 vs 69; volt text runs 83 vs 45; volt fills 78 vs 79; lit/bright hairlines 37 + 20 vs 11; animated elements 55 vs 5; volt/colour box-shadow glows 2 (both are the toggle thumb and the Tour screen card); volt radial glows 3; glass panels 7. So Night is not glow-heavy; it is edge-heavy: volt used as an outline colour on 123 elements, and 55 things animate. At 1440 Night: volt edges 125, volt text 86.

What the Night hero section carries (390 and 1440; the demo card and proof dock are below the fold on a phone): one soft glow (the toggle thumb, `marketing-theme.css:47-61`), a volt top hairline on the demo card, a volt radial spot behind the demo stage, a lit hairline on the proof dock, a volt headline line, volt key, volt dots on the painted board, an amber lamp cone painted into the room. No element in the hero has a volt border or a drop-glow beyond those. The "extreme AI slop" read is therefore the combination (volt on near-black, spot cone, top-edge line, painted dots) plus the 123 edges as he scrolls, not one rogue glow. Calm replacement rule for every row: a 1 px neutral hairline (`rgb(244 245 240 / .12)`), no coloured shadow, no radial wash; keep volt only for the primary key, the headline accent, the active dot and the logo.

Ranked by visual weight (count x area x colour weight). "Hero" marks the ones in the first two screens.

| # | selector (count) | what it does in Night | file:line | calm replacement | in hero |
|---|---|---|---|---|---|
| 1 | `button.du-chip` + `.du-chip__tick` (19 + 19) | volt border + 10 % volt fill + volt tick when on | `components/du/du.css:338-374`; `app/marketing-theme.css:80` | neutral hairline; tick only is volt | no |
| 2 | `button.ft__row` (10) | volt inset ring + volt border + volt wash on the active tour row | `app/feature-tour.css:11-13` | neutral border, volt 2 px dot or text for "on" | no |
| 3 | `.cl__group button` (14) | volt inset rim + volt border on pressed | `app/compass-ladder.css:6-8` | neutral border, bold ink for pressed | no |
| 4 | `figure.ts` (tour screens) | the page's only large soft volt glow: `0 18px 40px -24px rgb(210 240 0 / .18)` | `app/tour-screens.css:6` (Night), `:16` (Day) | `0 24px 48px -28px rgb(0 0 0 / .5)` | no |
| 5 | `span.mm-theme-toggle__thumb` (+ `__sky`, `::after`) | pale-lime 0/0/10/1 glow, inset rim, gradient sky | `app/marketing-theme.css:47-61` | flat disc, no glow | yes (site bar) |
| 6 | `aside.lp-cpro` (+ `::before`) | volt radial glow 16 %, volt border, glass blur(22px) | `app/compass-ladder.css:52-53` | solid raised panel, neutral hairline, no radial | no |
| 7 | `aside.lp-combo` (+ `::before`) | same as 6 (14 %) | `app/compass-ladder.css:69-70` | same | no |
| 8 | `span.rl__cover-mark` + `__cover-orbit` (6 + 6) | volt ring, dashed volt orbit on each reel cover | `app/social-proof.css:16-17` | drop the orbit; mark in neutral | no |
| 9 | `.lcd__frame` | bezel `0 0 0 4px` + `0 0 0 5px` rings plus inset rim and bright hairline | `app/lab-cinema.css:91-95` | one 1 px hairline; bezel as a flat darker fill | no |
| 10 | `.lcc__chip`, `.lcc__head` (6 + 3) | volt-green edges on verdict chips and arrows | `app/lab-cinema.css:188-202` | verdict by fill tone, border neutral | no |
| 11 | `.lcp-plan__n`, `.lcp-plan__go` (2 + 2) | volt fill/border + bright hairline | `app/lab-cinema.css:289-294` | volt fill only on the first; others neutral | no |
| 12 | `.ts__ladder li[data-mark=you]` | volt border + 12 % volt fill | `app/tour-screens.css:191` | neutral border, bold ink | no |
| 13 | `nav.lp-proof` (+ 4 links) | glass blur(24px) saturate(170 %), lit inset rim, bright hairline | `app/hero-depth.css:35-47` | solid panel, one neutral hairline | yes (second beat) |
| 14 | `.lp-stage::before` | volt radial spot 8.5 % behind the demo card + lit inset rim + frame border | `app/home-refinements.css:13-20` | remove the radial; keep the frame hairline | yes |
| 15 | `.mm-drill` card `::before` + hairline | the 1 px volt line along the top edge of the demo card (shot `shots/390-night/01-hero-2.png`), bright 20 % hairline, lit inset rim | `app/home-refinements.css:27-35` | delete the volt line; hairline 12 % | yes |

Next in line (not in the 15): `.lc__rail-ico` active volt fill (`lab-cinema.css:80-84`), `.cl__tag` volt pill (`compass-ladder.css:30`), `.ml__steps li` volt borders (`mistake-lab.css`), `.lp-plan--pro` volt border (`landing.css:1135`), footer `.mm-new` (`marketing.css`), `.lp-bg__spot` volt radial on desktop (`landing.css:251`), hero grid/dots (`landing.css:234-267`, `hero-depth.css:14-23`, scroll-driven).

The painted Night room (`HeroRoom.jsx`, file `scene-welcome-band-night`) carries its own amber lamp cone; that is an image, not CSS, and would need a different crop or a re-paint if the cone is the offender.

## 3. Text walls

Method: visible text nodes only (not `opacity:0`, not closed `<details>`), 390x844, Day (`data/page-390-day.json`; Night identical). Pinned stories are counted over all their steps (the student reads one step at a time). "Body" excludes headings and button text; "lines" = rendered lines at 390.

| # | section | all visible words | body words | longest body paragraph | lines |
|---|---|---|---|---|---|
| 1 | Hero | 121 | 56 | lead, 15 words | 2 |
| 2 | Statement (scrubbed) | 39 | 34 | the statement, 20 words | 7 (display size) |
| 3 | Mistake Lab (head + 4 steps) | 36 + 553 = 589 | 29 + 490 | head sub 27 words; step text 25 words | 4 / 3 |
| 4 | Feature tour (head + 10 steps) | 14 + 1,022 = 1,036 | 11 + 629 | 21 words | 3 |
| 5 | Score Recovery Lab (head + 4 steps) | 23 + 288 = 311 | 17 + 187 | 19 words | 3 |
| 6 | DU Compass | 209 | 140 | 22 words | 3 |
| 7 | DU eligibility + combo + colleges | 186 | 92 | 24 words | 4 |
| 8 | Exam section | 122 | 66 | 20 words | 3 |
| 9 | Proof band | 48 | 35 | 19 words | 2 |
| 10 | Instagram reels | 145 | 41 | 21 words | 3 |
| 11 | Pricing | 94 | 81 | 14 words | 2 |
| 12 | FAQ (closed) | 29 | 25 | 7 | 1 (answers when opened: 21, 58, 68, 44, 23 words) |
| 13 | Close | 34 | 23 | 11 | 2 |
| 14 | Footer | 84 | 33 | 25 | 3 |
| | total | about 3,050 | | | |

Findings: there is no long paragraph; the longest is 27 words (4 lines at 390). The "text wall" feeling is the volume spread across 18 pinned steps (about 1,900 words in the three stories, which are 47 % of the phone page height) and the repeated small UI-copy inside the mock screens (a Lab step is 85 to 174 words including the screen's own numbers). Per-step totals: Lab 125/85/174/169, Tour 100/124/107/101/93/111/99/89/90/108, Recovery 66/101/77/44. Wall of love is built but not shown (`WALL_VOICES` empty, `page.js:381`).

## 4. The exam screen section

### 4.1 What it is
`src/components/landing/ExamComparator.jsx` (111 lines), rendered at `page.js:357`; CSS `lp-exam*` classes (landing CSS). Heading "Practise calm. Rehearse exam day.", a MockMob / NTA-style switch (NTA marked Pro), then an interactive console with five live questions (`QUESTIONS`, lines 9-15), a clock that starts on first action, a 50-cell palette (five live, 45 decorative), a legend, a notice line, "Reset preview", then Mobi's seat and a "See Pro" / "Set up an NTA mock" button. Shots: `shots/390-day/08-exam-*.png`, `shots/1440-day/08-exam-*.png`.

### 4.2 Height (`data/exam-measure.json`)

| | 390 (phone) | 1440 |
|---|---|---|
| whole section | 1,644 px (1.95 screens) | 1,363 px (1.5 screens) |
| intro (heading + sub) | 245 | 190 |
| MockMob/NTA switch | 56 | 56 |
| console | 1,005 (1.2 screens: bar 48, paper 540, palette 304, foot 111) | 681 (paper 560, palette 560 beside it) |
| bottom row (Mobi seat, line, button) | 224 | 210 |

On the phone the console alone is 1.2 screens tall because the palette stacks under the question, and the page it sits in is 27,000 px. The section scrolls normally (no sticky, no scroll timeline).

### 4.3 Is it a faithful picture of our runner? No.

Real runner: `src/app/(app)/test/TestPageClient.jsx` (2,188 lines; `.nta-runner` at :1255, interface switch :1281, palette :1213-1250, mobile palette sheet :1448-1470). Shots (all new, `shots/runner/`): `390-quick-accountancy-day.png`, `390-quick-accountancy-night-palette.png`, `390-nta-mockmob-day.png`, `390-nta-classic-day-palette.png`, `1440-quick-accountancy-day.png`, `1440-nta-mockmob-night.png`, `1440-nta-classic-day.png` (each with -full / -palette variants at 390). Data: `data/runner2.json`.

| | home page "MockMob" screen (`lp-exam`) | real MockMob runner (default mode) |
|---|---|---|
| surface in Day | always a dark panel (`rgb(16,24,15)`) even in Day | light, follows the theme |
| header | one bar: dot + "MockMob Practice, English", "Try it here", clock | bar with exit X, "Quick practice / Accountancy", "Question 1 of 10" with a progress bar, "0 answered", timer pill, and a "Saved on this device. Stay online to submit." banner |
| question card | "Question 1 of 5" + stem + A to D | "MockMob CUET Test Console" label, "Question 1" title, chapter chip ("Admission Of Partner"), difficulty chip ("Medium"), a status pill ("Not Answered"), Mark (flag) and Clear |
| actions | "Mark for Review & Next", "Clear response", "Save & Next" (NTA's own words) | Mark, Clear, Previous, Next; mobile bottom bar Prev / Palette / Next |
| palette | 50 numbered cells with the NTA legend text ("Not visited", "Not answered", "Answered", "Marked for review", "Answered & marked for review") | Review panel: four counters (Answered, Marked, Pending, Not visited), numbered chips with state outlines, legend with live counts (monospace), "Submit test" key; on phones a sheet "Review palette 0/10 answered" |
| unique behaviours | none shown | press-and-hold an option to cross it out (hint under the options), offline save notice, fullscreen exam-space gate with "Warnings 0/3" (NTA mode), MockMob/NTA interface switch kept live with answers and timer ("Switch anytime. Your answers and timer stay."), chapter-aware chips |

So the home screen is an NTA-vocabulary clone drawn in MockMob's dark skin: it is not a picture of the runner a student gets, and its button and legend words are NTA's. It also stays dark in Day, which the runner does not.

### 4.4 How close is the real runner to the NTA CBT interface?
From the real runner's own "NTA style" skin (Pro; `shots/runner/1440-nta-classic-day.png`, `390-nta-classic-day-palette.png`): navy header band with subject and timer, orange pentagon "Not answered" chips, green "Answered", purple circles for marked, purple "Mark for review & next", "Clear response", green "Save & next", numbered palette. Against the public NTA CBT screen as I know it from memory (not re-verified against a live NTA page in this audit): header with candidate name and photo, subject/section tabs, "Time Left", question palette with the five-state legend and counts, "Mark for Review & Next", "Clear Response", "Save & Next", "Submit". The NTA skin copies the colour legend and the three action buttons; it has no candidate-details header (there is no candidate on a practice paper). The default MockMob skin is deliberately different: only the timer and numbered palette resemble NTA.

### 4.5 What is better and unique in our runner (candidates to show instead)
1. The Review panel: Answered / Marked / Pending / Not visited counters plus state-outlined chips, one glance versus NTA's legend-only palette (`1440-quick-accountancy-day.png`).
2. Press-and-hold to strike an option out (hint shown under the options).
3. Question context chips: chapter and difficulty, and a plain status pill.
4. "Saved on this device. Stay online to submit." offline-safe note.
5. The one-tap interface switch between MockMob and NTA styles that keeps answers and timer, and the "Enter your exam space" integrity gate with a three-warning meter (`1440-nta-mockmob-night.png`): the rehearsal story, true to the product.
6. The phone sheet palette (`390-quick-accountancy-night-palette.png`), with a thumb-reachable Prev / Palette / Next bar.
All six are real behaviours in `TestPageClient.jsx`; none appears on the home screen today. At 390 the runner is one screen (document height 876 at 844) against the home section's 1,644.

## 5. Phone performance, CPU throttled 4x

Setup: live site, 390x844, DPR 2, isMobile + touch, Android UA, empty cache, Day, `Emulation.setCPUThrottlingRate 4`, network not throttled (this PC), real Chrome 151 headless. Scroll: real CDP touch events with timestamps, 450 px at 900 px/s with fling, 600 ms apart, 22 swipes from the top to y 9,422 (hero, statement, whole Mistake Lab story, the first Tour steps).

### 5.1 Load (lean run `data/perf3-lean-390-cpu4x.json`; the instrumented run `perf2` gave LCP 3,324 and TBT 260)
| metric | value |
|---|---|
| TTFB / DCL / load | 89 / 1,380 / 1,398 ms |
| FCP | 888 ms (the H1) |
| LCP | 2,944 ms: `IMG.lp-room__file--day`, the room painting `scene-empty-allclear-day-1280.v2.avif` (39.8 KB). The H1 painted at 888 ms; the room image, `loading="lazy"` (`HeroRoom.jsx:46`), is the later and larger paint |
| TBT (FCP to 10 s) | 536 ms; 7 long tasks at load: 90, 229, 226, 68, 132, 87, 94 ms (926 ms) |
| CLS | 0 (load and scroll) |
| Document | 53.6 KB, 3,566 DOM nodes, 27,000 px tall |
| bytes after scroll | scripts 327.9 KB over 18 files (largest: React DOM chunk `15euem4lyi_on.js` 71.1, Next router `0h9bqs8w8u3qm.js` 39.1, ScrollStory + SectionPosition `01~804s7l7.6y.js` 37.6, MobiReact rig `0ijs-ew9qzq_6.js` 28.0, `0jif3~bk8e-c-.js` 23.5, `14tozbuglj_1w.js` 22.1, `0010y4~bum_ea.js` 19.4, ObjectLife `17pwiblfjlk0w.js` 17.1); CSS 125.5 KB over 21 files; fonts 144.6 KB (3); images 187 KB (8); 42 `fetch` calls 71.8 KB (most likely Next link prefetch) |
| biggest load tasks (LoAF) | 458 ms with no script attribution (style/layout), 365 ms React `MessagePort.onmessage` + a `FrameRequestCallback` in the ScrollStory chunk; 284 ms |

### 5.2 Idle on the hero (8 s, no input, CPU 4x, lean)
Main-thread task time 5.5 s of 8 s, script 0.73 s, 581 style recalculations (73 per second), 524 layouts. Nothing visible is happening except Mobi's rig. 52 animations are "running" at the top of the page (`data/perf2-390-cpu4x.json` `animations`), but they are scroll- or view-timeline animations (progress tied to scroll, not to time), so they cost on scroll, not at idle: `lp-depth-grid`, `lp-depth-mid` (hero grid and dots on `scroll(root)`), 20 `lp-word` (statement words on a view timeline), 4 x (rise, out) x (float, occluder, contact) shelf-object animations, shelf names and lamp.

### 5.3 Scroll (lean, 63.9 s)
| metric | value |
|---|---|
| frames | 4,876; p50 8.1 ms, p95 24.1, p99 39.5, worst 474 ms |
| frames over 25 / 50 / 100 ms | 180 / 23 / 12 |
| long tasks | 16, total 2.6 s (blocking time over 50 ms: 1.8 s): 464, 346, 300, 265, 165, 149, 137, 132, 131, 128, 111, 81, 56, 53, 51, 50 ms |
| main-thread work | task 39.6 s, script 4.3 s, style recalculation 7.8 s (3,978 recalcs), layout 0.86 s (295) |
| nature | style recalculation costs about twice the script time: the cost is the number of animated and scroll-linked things, not one heavy function |

### 5.4 Who costs (instrumented profile `perf2`, relative only)
Scroll window (sampling, 72 s): native rendering "(program)" 36.4 s (style, layout, paint, composite), then:

| rank | script / component | evidence | file |
|---|---|---|---|
| 1 | SubjectObject scroll physics ("lean"): a `document` capture-phase `scroll` listener (`N`) that reads `scrollY` per event and runs a rAF loop that updates every living object | 3.3 s self in the profile; 144 ms in one `#document.onscroll` LoAF script; 4,614 rAF calls | `src/components/brand/ObjectLife.jsx:134` (listener), chunk `17pwiblfjlk0w.js:24148`; the living objects are the SubjectObject instances (the statement's shelf and the Lab prop) |
| 2 | PipGuide (the global mascot flyer): a window `scroll` handler that on every frame does `querySelectorAll` over `.pip-seat` and `.pip-drill-*`, `getBoundingClientRect` per seat, `checkVisibility`, sets `data-pip-looking`, and a 260 ms `setTimeout` | 1.9 s self + `querySelectorAll` 1.3 s + `checkVisibility` 0.9 s + `matchMedia` 0.4 s; 1,258 rAF and 1,258 setTimeout calls | `src/components/brand/PipGuide.jsx:101`, `:148`, `:360`; chunk `0ssi8vcg7qkb0.js` |
| 3 | ScrollStory / SectionPosition: rAF callbacks on scroll that `getBoundingClientRect` and `getComputedStyle` the stage; a `FrameRequestCallback` here was 456 ms in one frame (LoAF) | 0.86 s self; LoAFs up to 541 ms, one holding a 456 ms ScrollStory callback | `src/components/landing/ScrollStory.jsx:141`, `SectionPosition.jsx:78`; chunk `01~804s7l7.6y.js:50901` |
| 4 | React work from state updates driven by those scroll hooks | 0.9 s; LoAF `MessagePort.onmessage` 85 to 580 ms | React DOM chunk |
| 5 | Next router prefetch (link prefetch streams) | LoAF 280 ms includes `eStreamDefaultReader.read` | `0h9bqs8w8u3qm.js` |
| 6 | scroll-linked CSS animations (view and scroll timelines) | style recalcs 3,978; 52 running at rest | `hero-depth.css:14-23`, statement CSS, `home.css` |

Idle (hero, no input): the MobiReact rig. 416 rAF calls in 8 s (52 per second) from chunk `0ijs-ew9qzq_6.js:81005`, and `setAttribute` (220 ms), `e$`/`ev`/`i.px` (the `__mb` attribute cache writes, `0ijs-ew9qzq_6.js:50136-50401`): the SVG rig is redrawn every frame while on screen (it stops when out of view: 130 rAF calls during the scroll). The rig code is `src/components/brand/MobiReact.jsx` (250 lines) and its rig chunk loads on idle (`HeroMobi.jsx:95`). This is inference from the profile, not proved by disabling the rig.

Load: the rig chunk 0.6 s, React 0.5 s, Turbopack runtime 0.24 s, ScrollStory 0.2 s of sampled script; the rest is native rendering.

Heaviest animations: the 20 per-word statement scrubs plus 24 shelf-object timelines (view timeline) and the rig's per-frame SVG updates. Not measured separately: GPU/compositor cost (headless).

## 6. Section list (390 / 1440 heights from `data/page-*.json`; sticky and timeline columns from computed styles)

Section order, as `main#main-content > section`. Heights vary by about 5 percent between runs because of `content-visibility:auto`.

| # | section | component / file | h at 390 | h at 1440 | pinned / scroll-driven |
|---|---|---|---|---|---|
| 1 | Hero | `page.js:176-235`: HeroBackdrop, HeroRoom, HeroMobi, LandingActions, DemoDrill, proof dock | 1,491 | 869 | no pin; ambient `scroll(root)` timelines on grid, dots, demo card (`hero-depth.css`) |
| 2 | Statement + shelf | `page.js:238-262`: scrubbed words, four SubjectObjects, `ObjectLife` | 1,519 | 736 | sticky text (`mm-wrap`, top 61 px, grid 699 px); 20 words and the shelf objects on view timeline `--lp-statement` |
| 3 | Mistake Lab | `page.js:264-275`: `LabCinema` inside `ScrollStory` | 3,704 | 4,143 | pinned story, 4 steps; hold 2,566 px (390) at 855 px per step (beat `76svh`; 2,808 and 936 at 1440, beat 78svh); view timelines `--ss-track` |
| 4 | Feature tour "What's inside MockMob" | `page.js:278-286`: `FeatureTour`, 10 slides (`TOUR`, `page.js:123-`; Learn and Mob slides appear only when switched on) | 5,977 | 6,422 | pinned story, 10 steps; hold 4,895 at 544 per step (beat `58svh`; 5,220 and 580 at 1440) |
| 5 | Score Recovery Lab | `page.js:289-300`: `MistakeLab` + MascotSeat | 3,396 | 3,604 | pinned story, 4 steps; hold 2,363 at 788 per step (beat `70svh`; 2,520 and 840 at 1440) |
| 6 | DU Compass | `page.js:304-331`: `CompassLadder`, Compass Pro panel | 2,263 | 1,449 | no |
| 7 | DU eligibility + combo + colleges | `page.js:333-355`: `EligibilityTeaser`, `CollegeDestinations` | 2,472 | 1,552 | no |
| 8 | Exam experience | `ExamComparator.jsx` (`page.js:357`) | 1,644 | 1,363 | no (interactive) |
| 9 | Proof band | `LiveStatsBand` (`page.js:360-366`) | 455 | 268 | no |
| 10 | Instagram creators | `CreatorReels` (`page.js:369-378`) | 1,009 | 1,159 | no (horizontal reel) |
| 11 | Pricing | `page.js:394-423` | 1,229 | 950 | no |
| 12 | FAQ | `page.js:425-438` | 485 | 623 | no |
| 13 | Close | `page.js:440-455`: `CloseActions`, `DemoJump`, `HashSettle` | 630 | 832 | no |
| 14 | Footer | `MarketingFooter` | 1,493 | 514 | no |
| - | Wall of love | `WallOfLove`, `page.js:381-391` | not rendered live | not rendered live | no (no published voices) |

Global layers: `SectionPosition` (the position band under the site bar during the three stories), `PipGuide` (mascot flyer, `page.js:458`), `HeroDockGate` + `MobileDock` (phone bar, `page.js:461`), `NavBar`.

Totals: section heights sum to 27,767 px at 390 and 24,484 px at 1440. The three pinned stories are 13,077 px (47 percent) at 390 and 14,169 px (58 percent) at 1440. At 390 the stories hold 9,824 px of scroll for 18 steps; one step is 544 to 855 px of finger travel, which is more than a screen for the Lab (855 px versus an 844 px screen). Because a step is a function of distance travelled and a flick travels as far as its speed carries it, the step count a flick skips depends on speed, which is what LK69 reports (not re-measured here; see the `scroll` folder).

## 7. Screenshot index
- First screens: `shots/390-day/00-first-screen.png`, `shots/390-night/00-first-screen.png`, `shots/1440-day/00-first-screen.png`, `shots/1440-night/00-first-screen.png`
- Short phones: `shots/herotime/{390x664,360x640,412x780}-{day,night}.png`; hero over time: `shots/herotime/390-{day,night}-t*.png`
- Mobi taps: `shots/390-{day,night}/M{1..4}{a,b}-*.png`; desktop host: `shots/{1440-day,1440-night}/M{1..4}-host-click*.png`
- Sections: `shots/{390,1440}-{day,night}/NN-*.png`; contact sheets: `sheets/`
- Real runner: `shots/runner/*`
- Neon crops: `shots/crops-390/`, `shots/crops-1440/`
