# LK69: why phone scrolling on the home page is inconsistent, measured with real touch events

Built 4 Nov 2026, 3:00 to 4:20 am IST. Read-only on the code. Production (https://www.mockmob.in, the live main build) at 390x844, DPR 2, isMobile, hasTouch, Chrome 151 headless, dark theme. Step numbers everywhere are the story's own 0-based `data-step` (0 = first scene; "step 1 rest" = the second scene's resting place). Everything below came from `Input.dispatchTouchEvent` / `Input.dispatchMouseEvent` sequences, not from `Input.synthesizeScrollGesture` (which moved the page 0 px, as the stopped run found).

## 0. The answer in ten lines

1. The held stories are plain native scroll. `ScrollStory.jsx` (lines 3-22, 144-152) takes the step from where the page happens to be (an IntersectionObserver on invisible "beats" crossing the window's middle) and, since LK47 (commit a52264827, 2 Nov), catches no wheel, swipe or key at all. Speed therefore decides everything, which is exactly the owner's "it detects speed".
2. How far a flick carries the page depends on the finger's release speed, not on how far the finger moved: 60 px at 3000 px/s moved the page 1756 px, 600 px at 3000 px/s moved it 2298 px, 60 px at 400 px/s moved it 77 px. A step is 544 px (tour), 788 px (Mistake Lab, recovery) or 855 px (Lab), so a normal flick skips 2 to 5 steps. Two quick flicks 150 ms apart on the 10-step bench (today's behaviour) carried the page through all 8 remaining steps (1 to 9) in about a second.
3. A slow or short drag stops wherever the finger left it: 15 of the 18 slow, short or reversing drags run inside the stories on production ended 85 to 358 px away from the nearest step's resting place (the other 3 moved about 15 px); only 4 of the 18 changed the step at all, and the tour flashed step 2 and back to 1 on a drag that reversed. The stage then shows one step while its progress fill, its object tilt and (for the statement) its word-by-word light are scroll-linked and sit part way (screenshots below).
4. Nothing stops a fling at a story's edge: a flick from the statement at 6000 px/s lands inside the Lab on its step 1 or 2 (step 0 never shown), and on the 10-step bench a flick from 500 px above the story landed on step 5 (steps 0 to 4 never shown).
5. The one-gesture-one-step rule exists in the owner's checklist as L-027 ("each gesture advances exactly ONE slide") and was built and checked once (commit f42b898c6, 15 Oct, 266 headless checks), then removed on 2 Nov for LK47 (the page "seemed to race" into the first story). Today's only scroll test, `scrollStorySpeed.test.mjs`, forbids the mechanism L-027 needs (no `preventDefault`, no `passive:false`). No test locks one gesture = one step today.
6. Mechanism proven on a bench that reproduces production's numbers exactly (the "today" column matches production row for row): a gesture controller (touch, wheel burst, keys) that commits one step from the gesture's net travel, plus an edge clamp for flings that arrive from outside, plus a settle on the nearest rest, plus step-driven (not scroll-driven) fills. All 32 flick rows (4 distances x 4 speeds x 2 stories) gave exactly one step and landed on a resting place (off 0). Slow drags, reversing drags, tiny nudges, two quick flicks, wheel bursts of 1 to 30 notches and a 60-event trackpad tail all behave (section 6).
7. Lag is real but not mostly scroll handlers: at 4x CPU the longest frames were 210 to 250 ms. Attributed: a forced layout in ScrollStory's resize callback (118 to 158 ms), a React render of the whole stage when a step changes (108 to 116 ms), a frame with no script (layout of a section as it is drawn), plus two always-on per-scroll animation loops (the object "lean" loop and Pip's gaze) that cost about 4% and 3% of the main thread. Blur on the nav and dock made no measurable difference in headless Chrome (negative result, section 7).
8. Geometry is also unstable: the page is 27,000 px tall when fresh and 27,906 px after content-visibility has drawn everything (+906 px); the tour section is reserved at 5,007 px and is really 5,977 px (landing.css:1435 reserves 580svh for a story that is 680svh tall plus its header). That moves every later story and in-page link by about 950 px and makes a fling land in a different place than expected.
9. Entry clamp via CSS scroll-snap was tested and rejected: it stops flings (yes) but also makes a 300 px slow drag from outside the story spring back (+0 px) and truncates a flick leaving the story to one screen (844 px instead of 2001 px).
10. The one thing this bench cannot prove is iOS Safari and a real Android phone (section 8).

## 1. Delivery proof (the events reached the page's own listeners)

`prove.mjs` installed capture-phase listeners (`addInitScript`) for touchstart/touchmove/touchend/touchcancel, pointer*, wheel, scroll, scrollend and logged them with scrollY and `cancelable`. Production, from the Lab's step-1 resting place (y 4181). Raw: `results-prove-delivery.json`; screenshots `proof-*.png` (all opened).

| gesture | touchstart | touchmove | touchend | pointerdown / pointercancel | scroll events | scrollend | page moved |
|---|---|---|---|---|---|---|---|
| flick 150 px @1200 px/s | 1 | 9 | 1 | 1 / 1 | 66 | 1 | +412 |
| flick 60 px @3000 px/s | 1 | 3 | 1 | 1 / 1 | 134 | 2 | +1756 (Lab steps 2 then 3 shown, then the page left the Lab) |
| slow drag 150 px (2 px / 25 ms) | 1 | 42 | 1 | 1 / 1 | 68 | 1 | +135 |
| drag 300 forward then 200 back | 1 | 142 | 1 | 1 / 1 | 243 | 1 | +85 |
| drag 100 forward then 100 back | 1 | 55 | 1 | 1 / 1 | 93 | 1 | -15 |

Notes: every touch event in the production log has `cancelable: 0`, because the page registers only passive listeners and Chrome then sends touch events to it non-blocking (nothing on the page could cancel them). The bench's non-passive `touchmove` receives cancelable events and cancelling them held the page in every owned gesture. `pointercancel` fires once per gesture as soon as the browser takes the scroll, so pointer-based logic (FeatureTour.jsx:203-205) sees only the first move; touch events carry the whole gesture.

## 2. What is on the page that scrolls or pages (code, with line numbers)

All files under `wt-1104-web-polish/src`. "Native" = the browser scrolls; nothing in the page cancels it.

| # | What | Where | Events listened to | What decides the next state | Lock / guard |
|---|---|---|---|---|---|
| 1 | Hero (1491 px tall on a phone, ordinary flow) | `components/landing/HeroMobi.jsx:175` (Mobi), `HeroBackdrop.jsx:41` | pointerdown/up/cancel/click on Mobi only; pointermove (passive) on the backdrop host | none: no scroll behaviour of its own | n/a |
| 2 | Statement + shelf. On phones a 180svh track, its grid `position: sticky` | `app/hero-depth.css:88` (view-timeline `--lp-statement`), 98-107 (word opacity 0.18 to 1 by scroll), 120-190 (phone pin, shelf lifts by scroll range) | none (CSS scroll-driven animations only) | scroll position, continuously (words and the four objects scrub) | none: any stop between two values stays half lit (screenshot `statement-slowdrag-300.png`) |
| 3 | Held story primitive `ScrollStory` (Lab, tour, Mistake Lab) | `components/landing/ScrollStory.jsx`; geometry `app/scroll-story.css:23-31` (track = 100svh + steps x beat; stage `position: sticky; top: 0; height: 100svh`) and 46-48 (beats) | `scroll` (passive, only within 100% of the story, one rAF read, line 141); IntersectionObserver on beats, `rootMargin: -50% 0 -50% 0` (144-152); `wheel`/`touchstart` (passive) and `keydown` only to stop a programmatic glide (222-224) | step = the beat that crosses the window's middle (distance from the nearest resting place), so position alone. `go()` (201-220) glides to a step only for taps on chips/arrows (440 ms) | `steering` flag during that glide only. No lock for user scroll |
| 4 | Lab (4 scenes, beat 76svh = 855 px per step) | `LabCinema.jsx:351` `<ScrollStory steps={SCENES.length}>`, `app/lab-cinema.css:33` | via ScrollStory | via ScrollStory; object tilt scroll-linked: `lab-cinema.css:511-512` (`animation-timeline: --ss-track`) | none |
| 5 | Tour (10 slides, beat 58svh = 544 px per step) | `FeatureTour.jsx:240`, `app/feature-tour.css:123` | via ScrollStory; its own handlers `onPointerDown/Move/Up/Cancel`, `onTouchStart`, `onWheel` (203-207) set only "interacting"/"programmatic" flags | via ScrollStory. Unpinned fallback is a real horizontal pager (`feature-tour.css:30-31`: `scroll-snap-type: x mandatory`, `scroll-snap-stop: always`), switched off when pinned (line 126) | none |
| 6 | Mistake Lab (4 steps, beat 70svh = 788 px) | `MistakeLab.jsx:338`, `app/mistake-lab.css:177` | via ScrollStory | via ScrollStory | none |
| 7 | Progress fills inside the stories | `app/scroll-story.css:55-71` (`.ss-fill`, `animation-timeline: --ss-track`, range by step) | none | scroll position: the fill of the next step grows while you drag, so a stop part way shows a half bar (see `lab-r1-slowdrag-513.png`, `tour-r1-slowdrag-300.png`) | none |
| 8 | Chip and card rails | `app/marketing.css:718` (`.mm-rail`, `scroll-snap-type: x proximity`), `app/social-proof.css:9` (reels, `x proximity`), `CreatorReels.jsx:139-145` (`scrollBy`) | native horizontal scroll | native, proximity snap | none (these are horizontal, they do not fight the vertical story) |
| 9 | Programmatic jumps | `DemoJump.jsx:74-100` (`scrollTo` instant then smooth), `HashSettle.jsx:12,28` (`wheel`, `touchstart`, `keydown`, `pointerdown` stop it), `html { scroll-behavior: smooth }` at `app/globals.css:58` | wheel / touchstart / keydown / pointerdown (passive) | link clicks and hashes | stop on user input |
| 10 | Section position band, dock gate, reveals | `SectionPosition.jsx:73-78` (passive scroll + rAF read), `HeroDockGate.jsx`, `Reveal.jsx`, `ArenaPreview.jsx:76` | scroll (passive), IntersectionObserver | position | n/a |
| 11 | Per-scroll animation loops outside the stories | object "lean" physics (chunk `17pwiblfjlk0w.js`, a scroll listener feeding a rAF loop: `L.scrollDelta`, `L.lean`), Pip's gaze (chunk `0ssi8vcg7qkb0.js`, `window.addEventListener("scroll", h, {passive:true})`) | scroll (passive) | scroll velocity | none |
| 12 | Section rendering | `app/landing.css:1433-1444` (`content-visibility: auto` + `contain-intrinsic-size` per section) | n/a | n/a | n/a |

`scroll-craft-main` is not used by the home page (no import in `page.js` or `components/landing`). No scroll library (Lenis, GSAP ScrollTrigger) is used. No `scroll-snap-type` exists on the document, `html` or `body`. No `touch-action` rule exists on the stories (only `manipulation` on buttons). The only non-passive-capable listeners are none: every listener the stories add is passive (test-locked).

## 3. Production results: the gesture table

Source: `results-main.json` (run 4 Nov 3:00 am by `probe.mjs`, live production, flick rows are CDP touch sequences with exact timestamps, lifted while moving so Chrome flings). Start: each story's step-1 resting place. Geometry at that run: Lab top 3326, 4 steps, 855.3 px apart; tour top 6957, 10 steps, 543.9 px apart; recovery top 12928, 4 steps, 787.7 px apart; statement top 1552.

Fling distance is set by release speed (rows) almost independent of how far the finger moved (columns). "out" = left the story.

### Production flick tables

**lab**: cell = step change / page moved px / where it stopped (off = px from the nearest rest; out = left the story)

| release speed  drag | 60 px | 150 px | 300 px | 600 px |
|---|---|---|---|---|
| 400 px/s | +0 / +77 / off +77 | +0 / +168 / off +168 | +0 / +318 / off +318 | +1 / +619 / off -237 |
| 1200 px/s | +0 / +322 / off +322 | +0 / +412 / off +412 | +1 / +561 / off -295 | +1 / +863 / off +7 |
| 3000 px/s | +2 / +1756 / out | +2 / +1848 / out | +2 / +2002 / out | +2 / +2298 / out |
| 6000 px/s | +2 / +2586 / out | +2 / +2691 / out | +2 / +2841 / off +65 | +2 / +3139 / off -181 |

**tour**: cell = step change / page moved px / where it stopped (off = px from the nearest rest; out = left the story)

| release speed  drag | 60 px | 150 px | 300 px | 600 px |
|---|---|---|---|---|
| 400 px/s | +0 / +77 / off +77 | +0 / +33 / off +33 | +0 / +33 / off +33 | +0 / +38 / off +38 |
| 1200 px/s | +1 / +277 / off -267 | +1 / +277 / off -267 | +1 / +275 / off -269 | +1 / +277 / off -267 |
| 3000 px/s | +3 / +1705 / off +73 | +3 / +1711 / off +79 | +3 / +1713 / off +81 | +3 / +1710 / off +78 |
| 6000 px/s | +5 / +2586 / off -133 | +5 / +2566 / off -153 | +5 / +2641 / off -78 | +5 / +2563 / off -156 |

**recovery**: cell = step change / page moved px / where it stopped (off = px from the nearest rest; out = left the story)

| release speed  drag | 60 px | 150 px | 300 px | 600 px |
|---|---|---|---|---|
| 400 px/s | +0 / +76 / off +76 | +0 / +169 / off +169 | +0 / +318 / off +318 | +1 / +619 / off -168 |
| 1200 px/s | +0 / +322 / off +322 | +1 / +412 / off -375 | +1 / +561 / off -226 | +1 / +863 / off +76 |
| 3000 px/s | +2 / +1755 / out | +2 / +1848 / out | +2 / +2002 / out | +2 / +2298 / out |
| 6000 px/s | +2 / +2586 / out | +2 / +2691 / out | +2 / +2842 / out | +2 / +3139 / out |


Reading the matrices: with a 60 px flick the step changes by 0 at 400 px/s and by 2 to 5 at 3000 to 6000 px/s (the tour at 6000 px/s: 1 to 6, five steps in 3.2 s). At 1200 px/s a 150 px flick on the Lab changes nothing and leaves the page 412 px past the rest, while a 300 px flick changes the step but stops 295 px before the new step's rest. The same distance, different speed, different result: that is LK69 in numbers. A flick lifted at 400 px/s moves the page only the finger's own distance plus 0 to 20 px, so it is a drag, not a flick.

Other gestures on production (steps are 0-based; "rest k" is step k's resting place; screenshots opened):

| gesture (from the step-1 rest unless noted) | story | page moved | step before to after (steps shown) | stopped | progress fill after | shot |
|---|---|---|---|---|---|---|
| slow touch drag ~80px/s, held, lifted, 150 px | lab | +135 | 1 to 1 (1) | held, +135 px from rest 1 | x1 |  |
| slow touch drag ~80px/s, held, lifted, 300 px | lab | +285 | 1 to 1 (1) | held, +285 px from rest 1 | x1 | lab-r1-slowdrag-300.png |
| slow touch drag ~80px/s, held, lifted, 513 px (0.6 of a step gap) | lab | +498 | 1 to 2 (1,2) | held, -358 px from rest 2 | x0.582 | lab-r1-slowdrag-513.png |
| slow touch drag ~80px/s, held, lifted, 150 px | tour | +135 | 1 to 1 (1) | held, +135 px from rest 1 | x1 |  |
| slow touch drag ~80px/s, held, lifted, 300 px | tour | +285 | 1 to 2 (1,2) | held, -259 px from rest 2 | x0.524 | tour-r1-slowdrag-300.png |
| slow touch drag ~80px/s, held, lifted, 326 px (0.6 of a step gap) | tour | +311 | 1 to 2 (1,2) | held, -233 px from rest 2 | x0.572 |  |
| slow touch drag ~80px/s, held, lifted, 150 px | recovery | +135 | 1 to 1 (1) | held, +135 px from rest 1 | x1 |  |
| slow touch drag ~80px/s, held, lifted, 300 px | recovery | +285 | 1 to 1 (1) | held, +285 px from rest 1 | x1 | recovery-r1-slowdrag-300.png |
| slow touch drag ~80px/s, held, lifted, 473 px (0.6 of a step gap) | recovery | +458 | 1 to 2 (1,2) | held, -329 px from rest 2 | x0.581 |  |
| slow touch drag ~80px/s, held, lifted, 300 px | lab | +285 | 0 to 0 (0) | entering, 629 px of stage shown | x0.749 | lab-enter-slowdrag-300.png |
| slow touch drag ~80px/s, held, lifted, 300 px | tour | +285 | 0 to 0 (0) | entering, 629 px of stage shown | x0.605 |  |
| slow touch drag ~80px/s, held, lifted, 300 px | recovery | +285 | 0 to 0 (0) | entering, 629 px of stage shown | x0.727 | recovery-enter-slowdrag-300.png |
| very slow drag 2px/16ms, held, lifted, 120 px | lab | +105 | 1 to 1 (1) | held, +105 px from rest 1 | x1 |  |
| drag 300 forward then 200 back, held, lifted, 300 px (reverses) | lab | +85 | 1 to 1 (1) | held, +85 px from rest 1 | x1 |  |
| drag 100 forward then 100 back, held, lifted, 100 px (reverses to start) | lab | -15 | 1 to 1 (1) | held, -15 px from rest 1 | x0.982 |  |
| very slow drag 2px/16ms, held, lifted, 120 px | tour | +105 | 1 to 1 (1) | held, +105 px from rest 1 | x1 |  |
| drag 300 forward then 200 back, held, lifted, 300 px (reverses) | tour | +85 | 1 to 1 (1,2,1) | held, +85 px from rest 1 | x1 |  |
| drag 100 forward then 100 back, held, lifted, 100 px (reverses to start) | tour | -15 | 1 to 1 (1) | held, -15 px from rest 1 | x0.973 |  |
| very slow drag 2px/16ms, held, lifted, 120 px | recovery | +105 | 1 to 1 (1) | held, +105 px from rest 1 | x1 |  |
| drag 300 forward then 200 back, held, lifted, 300 px (reverses) | recovery | +85 | 1 to 1 (1) | held, +85 px from rest 1 | x1 |  |
| drag 100 forward then 100 back, held, lifted, 100 px (reverses to start) | recovery | -15 | 1 to 1 (1) | held, -15 px from rest 1 | x0.981 |  |

Statement (phone scrub, no steps) and flings that arrive from the statement:

| gesture | page moved | lands | words lit (of 20) before to after |
|---|---|---|---|
| flick, fling on, 60 px @1200 | +322 | statement, statement progress 0.48 | 0+0p/20 to 10+2p/20 |
| flick, fling on, 150 px @1200 | +412 | statement, statement progress 0.61 | 0+0p/20 to 13+2p/20 |
| flick, fling on, 300 px @1200 | +561 | statement, statement progress 0.83 | 0+0p/20 to 18+2p/20 |
| flick, fling on, 600 px @1200 | +863 | statement | 0+0p/20 to 20+0p/20 |
| flick, fling on, 60 px @6000 | +2586 | Lab held, phase 0.95, -43 px from rest 1 (Lab steps shown: 1) | 0+0p/20 to 20+0p/20 |
| flick, fling on, 150 px @6000 | +2691 | Lab held, phase 1.07, +62 px from rest 1 (Lab steps shown: 1) | 0+0p/20 to 20+0p/20 |
| flick, fling on, 300 px @6000 | +2841 | Lab held, phase 1.25, +212 px from rest 1 (Lab steps shown: 1) | 0+0p/20 to 20+0p/20 |
| flick, fling on, 600 px @6000 | +3139 | Lab held, phase 1.6, -346 px from rest 2 (Lab steps shown: 1,2) | 0+0p/20 to 20+0p/20 |
| slow touch drag ~80px/s, held, lifted, 300 px | +285 | statement, statement progress 0.42 (Lab steps shown: 0) | 0+0p/20 to 9+1p/20 |

What the half states look like (screenshots in this folder, all opened):

- `lab-r1-slowdrag-513.png`: the Lab on "Repair" with Repair's own underline filled 58% (x0.582) and the page 358 px before that step's resting place: a half slide.
- `tour-r1-slowdrag-300.png`: the tour on "Learn" (03 / 10) with the third progress segment partly filled.
- `statement-slowdrag-300.png`: the phone statement after a 300 px drag: 9 words lit, 1 half lit, the shelf objects half risen. The statement is a pure scrub (no steps), so every stop is a half state.
- `proof-flick-60-3000.png`: a 60 px flick from the Lab's second scene ended on its last scene (SWOT) with the stage already leaving: Repair was never shown.

## 4. Tests that exist today

- `src/components/landing/scrollStorySpeed.test.mjs` (3 tests, pass): reads `ScrollStory.jsx` as text and asserts (a) no `preventDefault(`, no `passive: false`, no `overflow = 'hidden'`; (b) `wheel` and `touchstart` listeners with `{ passive: true }` that only stop a picked-step glide; (c) `go()` jumps instantly under reduced motion. It was added by the LK47 fix (a52264827). It locks the opposite of L-027 and has to be rewritten, not just extended.
- `labStory.test.mjs`, `landingPosition.test.mjs`, `sectionPositionPhase.test.mjs`, `heroScene.test.mjs`, `heroTaps.test.mjs`, `landingMobi.test.mjs`: scene copy, the position band and Mobi. None touches gestures.
- Grep for `gesture`, `one slide`, `L-027`, `L-028` in `data/tests`, `src` (excluding the unrelated learn pager, `usePager`, `swipeRelease`, `dragPolicy`): no landing test. L-027 ("each gesture advances exactly ONE slide", WEB-OWNER-LEDGER-2026-10-17.md:38) and L-028 (one slide per gesture, readable dwell, :39) have no test. The checks that proved G1 (266 headless runs, commit f42b898c6 message) are not in the repo.
- History: `f42b898c6` (15 Oct) built the controller (wheel, touch, keys, escape, edge catches: about 260 lines in ScrollStory.jsx); `a52264827` (2 Nov, LK47) deleted it because "one 100 px notch moved the page 864 px at 1440x900. The first held story sits right after the hero, so the page seemed to race there." That complaint was about how it carried the page into the first story, not about the stage swapping once the story was held. The mechanism below keeps the stage still, never glides the page, and moves the scroll position by at most the rest offset while the stage is sticky (invisible).

## 5. Root causes (file:line)

1. **Step state follows scroll position, and the scroll is the browser's.** `ScrollStory.jsx:144-152` (IntersectionObserver on beats at the window's middle), `:222-224` (listeners only stop a glide), `scroll-story.css:23-31, 46-48`. The test at `scrollStorySpeed.test.mjs:12-15` forbids anything else. Result: the number of steps a gesture moves is (fling distance) / (step gap), and fling distance follows release speed (table in section 3).
2. **No stop at a story's edge.** Nothing in `ScrollStory.jsx` limits momentum at the first or last resting place. A fling from the statement or the previous story runs through the next one (production: statement flick 300 px @6000 lands at Lab phase 1.25, step 0 never shown; bench: enter flick 600 @6000 lands on step 5 of 10).
3. **Visuals are scroll-linked, so they are half done whenever the finger stops.** Progress fills `scroll-story.css:55-71` (`animation-timeline: --ss-track`), the Lab object tilt `lab-cinema.css:511-512`, the statement words and shelf `hero-depth.css:98-107, 120-190`. The statement has no step at all.
4. **Beats are only half a step wide and the scroll rests anywhere.** A drag that ends 40% of the way to the next step leaves the page there (no settle) while the content is the previous step's; at 50% the content flips mid drag and flips back if the drag reverses (production: tour `reverse-300-back-200` shows steps 1, 2, 1).
5. **Geometry drifts while scrolling.** `landing.css:1433-1444`: sections are `content-visibility: auto` with a reserved `contain-intrinsic-size`, and `#your-prep` is reserved at 580svh (`:1435`; 570svh at desktop `:1447`) while its track is `100svh + 10 x 58svh = 680svh` (`scroll-story.css:25`, `feature-tour.css:123`). Measured (fresh load, then after one top to bottom walk): page 27,000 to 27,906 px; tour section 5,007 to 5,977 px; Mistake Lab section top 11,804 to 12,752; pricing 23,099 to 23,992. Every position after the tour moves by about 950 px the first time the tour is drawn. Any step table, hash jump (`HashSettle.jsx`, `DemoJump.jsx`) or fling target computed before that is wrong.
6. **Main-thread stalls inside gestures** (section 7): a forced layout in a resize callback (`ScrollStory.jsx:164-184`, `fitAll` 44-66 reads and writes style per marked node, up to 3 passes), a React render of the whole stage on every `setStep` / `setLive` (`ScrollStory.jsx:147-148`, `api` memo at 250 changes with `step`), and two per-scroll animation loops.
7. **Contradictory standing rules, never reconciled.** L-027/L-028/LK69 want one gesture = one step; LK47 (and its test) forbid catching the gesture. The gesture was removed rather than fixed.

## 6. Proposed mechanism: "one touch (or one wheel burst) = at most one step"

Rules, each backed by a bench row below. Geometry and DOM stay as they are (sticky stage in a tall track, beats, scrollbar, find-in-page, hash links, keyboard focus all keep working); only how a step is chosen changes.

1. **Cached geometry.** Per story: `top` and `hold` (track height minus stage height), re-measured on ResizeObserver and when a content-visibility section is drawn (`contentvisibilityautostatechange`), never in the gesture path. `rest(k) = top + round(hold * k / (steps - 1))`. Hot paths read only `scrollY`.
2. **Touch.** One window-level `touchstart` (passive), `touchend`/`touchcancel` (passive) and one `touchmove` with `{ passive: false }` that calls `preventDefault` only for a gesture it owns. A gesture is owned if it started while the page is inside a story's hold, moves vertically more than sideways after 6 px of slop (sideways = chips, reels, tour list stay native), the story has a step in the net direction (first/last step in the way out = native, so the page leaves normally), and it did not start inside the lock. Moves under the slop are cancelled (the page waits). While owned, the content leans 25% of the finger's travel, at most 28 px (one transform write per frame, `translate3d`, no layout).
3. **Commit at touchend, from the net travel only, speed never.** Step in the direction of the net travel if `|dy| >= 40 px`, or if it is a short flick (`|dy| >= 12 px` and the last 80 ms at `>= 0.3 px/ms` in the same direction). A drag that reverses to under 40 px commits nothing; a reversal past the start steps the other way (implemented, not in the table). No step is ever more than one, whatever the finger did.
4. **Lock.** After a commit, any gesture that starts within 420 ms (120 ms under reduced motion) is swallowed whole (never queued, never skipped ahead).
5. **Wheel and trackpad.** One `wheel` listener (`passive: false`, `preventDefault` only while owned). A burst starts after 160 ms of quiet or on a direction change and fires at most one step (after 12 px of travel), however many notches or inertia events follow; the whole tail is swallowed. Keys (arrows, PageUp/Down, Space) step once per press, not per repeat. `ctrlKey` (pinch zoom) is ignored.
6. **After a step, the page position follows.** `scrollTo(rest(next), { behavior: 'instant' })`: invisible because the stage is sticky, and it keeps scrollbar, anchors and the beats agreeing with the step. Never a glide.
7. **Entry and exit clamp (the part CSS snap could not do).** From a passive `scroll` listener (one rAF, `scrollY` only), with no finger down: if the page crosses a story's first rest from above (or its last from below) while not owned by a gesture, hold it at that rest (`keepY`) until the next `touchstart`/`wheel`/key or until scrolling has been quiet for 150 ms. Re-assert each frame, instant. Because the stage only becomes sticky at that very position, the clamp is invisible: the page just stops where the story takes the screen. A native touch that ends with the page inside a hold holds the nearest rest the same way.
8. **Settle.** When a native scroll ends inside a hold (`scrollend`, or 150 ms without scroll events where unsupported), move to the nearest rest and show that step. This removes every half state for the scrollbar, keyboard `Home`/`End`, find-in-page and any gesture the controller did not own.
9. **Visuals are step-driven.** Fills and the Lab object tilt change by `data-step` with time transitions (transform/opacity only), not `animation-timeline: --ss-track`. Set the step by writing `data-step`/class on the story root and let CSS react; keep React out of the per-step path (memoise the stage's children, or move `setStep` behind `startTransition`) so a step costs a style change, not a stage re-render.
10. **Statement on phones.** It has no steps, so no controller can make it consistent: either turn its 180svh hold into a 4 to 5 step `ScrollStory` (one step per phrase: words and shelf object lift on the step, timed, same content) or keep the scrub and add rule 8 (settle to the nearest of the five landmarks). The first keeps "one gesture, one step" literally true everywhere.
11. **Programmatic jumps declare themselves.** `goTo`, `HashSettle`, `DemoJump` and nav links must tell the controller the target (`story.arrive(y)` sets the "last y" before they scroll), otherwise a jump from outside is read as an entry and held at the first rest. (The bench shows this: a plain `scrollTo` to rest 1 from far above was held at rest 0 until a second jump from inside.)
12. **Reduced motion.** Steps still change by gesture, instantly (transitions 1 ms, lock 120 ms, no finger lean); the clamp and settle stay (they are not motion).
13. **Smoothness.** Everything per frame is a transform or opacity change or one `scrollY` read; geometry is cached; only `touchmove` (and `wheel`) are non-passive and they return immediately when not owned; no `overflow: hidden`, no `touch-action: none` (the way out stays native).
14. **Tests it needs** (to replace `scrollStorySpeed.test.mjs`): (a) source-level: only touchmove and wheel are non-passive, `preventDefault` appears only behind an ownership check, no `overflow = 'hidden'`; (b) a Playwright/CDP table at 390x844 and 1440x900 run against `next start`: the 32 flick rows (4 distances x 4 speeds), 3 slow drags, 2 reversing drags, tiny nudge, two flicks 150 ms and 700 ms apart, enter flick 600 @6000 from 500 px above, exit flicks both ways, wheel 1, 5, 30 notches and a 60-event tail, reduced motion; each asserts the exact step and that the page rests on the resting place (`offPx === 0`); (c) the fresh-vs-warm geometry check (document height difference under 30 px).

### Bench: the same gesture table on the prototype

`prototype-one-gesture-v2.html` (this folder) reproduces the production story geometry (protoA = Lab: 4 steps, 855 px; protoB = tour: 10 steps, 544 px) and switches each part with a query (`ctrl=0` = today's free scroll, `entry=snap|clamp|none`, `settle=0`, `commit=move`). The "native (today)" column below matches production row for row (same page-moved numbers, e.g. 60 px @3000 = +1756 px, 600 px @6000 = +3140 px), so the bench is a fair stand-in. Runs: `probe2.mjs` (`results2-p2-*.json`, `results2-p2-*.md`, logs `run2-*.log`), one browser at a time under the shared lock.

Flick table, today's behaviour on the bench (copy of the production result, protoA and protoB):


**Today (free scroll) on the bench: protoA (Lab geometry) and protoB (tour geometry).**

**protoA**: cell = step change / page moved px / where it stopped (off = px from the nearest rest; out = left the story)

| release speed  drag | 60 px | 150 px | 300 px | 600 px |
|---|---|---|---|---|
| 400 px/s | +0 / +77 / off +77 | +0 / +168 / off +168 | +0 / +318 / off +318 | +1 / +619 / off -237 |
| 1200 px/s | +0 / +322 / off +322 | +0 / +412 / off +412 | +1 / +561 / off -295 | +1 / +863 / off +7 |
| 3000 px/s | +2 / +1756 / out | +2 / +1848 / out | +2 / +2002 / out | +2 / +2298 / out |
| 6000 px/s | +2 / +2586 / out | +2 / +2692 / out | +2 / +2841 / out | +2 / +3140 / out |

**protoB**: cell = step change / page moved px / where it stopped (off = px from the nearest rest; out = left the story)

| release speed  drag | 60 px | 150 px | 300 px | 600 px |
|---|---|---|---|---|
| 400 px/s | +0 / +77 / off +77 | +0 / +168 / off +168 | +1 / +318 / off -226 | +1 / +619 / off +75 |
| 1200 px/s | +1 / +322 / off -222 | +1 / +412 / off -132 | +1 / +561 / off +17 | +2 / +863 / off -225 |
| 3000 px/s | +3 / +1756 / off +124 | +3 / +1848 / off +216 | +4 / +2002 / off -173 | +4 / +2298 / off +123 |
| 6000 px/s | +5 / +2586 / off -133 | +5 / +2692 / off -27 | +5 / +2841 / off +122 | +6 / +3140 / off -123 |


Same table with the proposed mechanism (controller + clamp + settle, commit at release): every one of the 32 cells is exactly one step, 544 or 855 px, resting on the resting place (off 0):


**protoA**: cell = step change / page moved px / where it stopped (off = px from the nearest rest; out = left the story)

| release speed  drag | 60 px | 150 px | 300 px | 600 px |
|---|---|---|---|---|
| 400 px/s | +1 / +856 / off +0 | +1 / +856 / off +0 | +1 / +856 / off +0 | +1 / +856 / off +0 |
| 1200 px/s | +1 / +856 / off +0 | +1 / +856 / off +0 | +1 / +856 / off +0 | +1 / +856 / off +0 |
| 3000 px/s | +1 / +856 / off +0 | +1 / +856 / off +0 | +1 / +856 / off +0 | +1 / +856 / off +0 |
| 6000 px/s | +1 / +856 / off +0 | +1 / +856 / off +0 | +1 / +856 / off +0 | +1 / +856 / off +0 |

**protoB**: cell = step change / page moved px / where it stopped (off = px from the nearest rest; out = left the story)

| release speed  drag | 60 px | 150 px | 300 px | 600 px |
|---|---|---|---|---|
| 400 px/s | +1 / +544 / off +0 | +1 / +544 / off +0 | +1 / +544 / off +0 | +1 / +544 / off +0 |
| 1200 px/s | +1 / +544 / off +0 | +1 / +544 / off +0 | +1 / +544 / off +0 | +1 / +544 / off +0 |
| 3000 px/s | +1 / +544 / off +0 | +1 / +544 / off +0 | +1 / +544 / off +0 | +1 / +544 / off +0 |
| 6000 px/s | +1 / +544 / off +0 | +1 / +544 / off +0 | +1 / +544 / off +0 | +1 / +544 / off +0 |


### Bench: the other gestures, and which parts are needed

Six variants, same gestures (`compare.md` is the same table; raw rows in `results2-p2-*.json`). Columns: today's free scroll; CSS scroll-snap only (`html { scroll-snap-type: y mandatory }`, every section a snap area, a 1 px stop with `scroll-snap-stop: always` at each rest); the controller without any entry control; the controller plus that CSS snap; the controller firing as soon as 32 px is passed (my first version); and the proposed mechanism (commit at release, edge clamp, settle). Steps are 0-based; "lands on step k" = the story is held and shows step k.


**protoA** (4 steps, 855 px per step); cell = steps moved / page moved / where it settled (off = px from the nearest rest)

| gesture | native (today) | CSS snap only (no controller) | controller, no entry control | controller + CSS snap | controller, fires on move | controller + clamp + settle (proposed) |
|---|---|---|---|---|---|---|
| very slow drag 120 px (2 px / 16 ms) | +0 step / +105 px / off +105 | +0 step / +0 px / off +0 | not run | +1 step / +856 px / off +0 | +1 step / +856 px / off +0 | +1 step / +856 px / off +0 |
| slow drag 150 px | +0 step / +135 px / off +135 | +0 step / +0 px / off +0 | not run | +1 step / +856 px / off +0 | +1 step / +856 px / off +0 | +1 step / +856 px / off +0 |
| slow drag 300 px | +0 step / +285 px / off +285 | +0 step / +0 px / off +0 | not run | +1 step / +856 px / off +0 | +1 step / +856 px / off +0 | +1 step / +856 px / off +0 |
| tiny nudge 20 px | +0 step / +5 px / off +5 | +0 step / +0 px / off +0 | not run | +0 step / +0 px / off +0 | +0 step / +0 px / off +0 | +0 step / +0 px / off +0 |
| drag 300 forward, 200 back, lift | +0 step / +85 px / off +85 | +0 step / +0 px / off +0 | not run | +1 step / +856 px / off +0 | +1 step / +856 px / off +0 | +1 step / +856 px / off +0 |
| drag 100 forward, 100 back, lift | +0 step / -15 px / off -15 | +0 step / +0 px / off +0 | not run | +0 step / +0 px / off +0 | +1 step / +856 px / off +0 | +0 step / +0 px / off +0 |
| two 300 px @3000 flicks, 150 ms apart | +2 step / +6143 px / off +12 / steps flashed 1,2,3 | +2 step / +1711 px / off +0 / steps flashed 1,2,3 | not run | +1 step / +856 px / off +0 | +2 step / +1711 px / off +0 / steps flashed 1,2,3 | +1 step / +856 px / off +0 |
| two 300 px @3000 flicks, 700 ms apart | +2 step / +7052 px / off -166 / steps flashed 1,2,3 | +2 step / +1711 px / off +0 / steps flashed 1,2,3 | not run | +2 step / +1711 px / off +0 / steps flashed 1,2,3 | +2 step / +1711 px / off +0 / steps flashed 1,2,3 | +2 step / +1711 px / off +0 / steps flashed 1,2,3 |
| flick 600 px @6000 arriving from 500 px above the story | ends outside the story / +3140 px / steps flashed 3,0,1,2,3 | lands on step 0, off 0 / +844 px | ends outside the story / +3139 px / steps flashed 3,0,1,2,3 | lands on step 0, off 0 / +844 px | lands on step 0, off 1 / +501 px | lands on step 0, off 0 / +500 px |
| flick 300 px @1200 arriving from 500 px above | lands on step 0, off 61 / +561 px | lands on step 0, off 0 / +844 px | lands on step 0, off 0 / +500 px | lands on step 0, off 0 / +844 px | lands on step 0, off 1 / +501 px | lands on step 0, off 0 / +500 px |
| slow drag 300 px arriving from 500 px above | ends outside the story / +285 px | ends outside the story / +0 px | not run | ends outside the story / +0 px | ends outside the story / +285 px | ends outside the story / +285 px |
| flick 300 @3000 from the last step (leaving) | ends outside the story / +2002 px | ends outside the story / +844 px | not run | ends outside the story / +844 px | ends outside the story / +2001 px | ends outside the story / +2001 px |
| flick 300 @3000 up from the first step (leaving) | ends outside the story / -1400 px | ends outside the story / -844 px | not run | ends outside the story / -844 px | ends outside the story / -1400 px | ends outside the story / -1400 px |

**protoB** (10 steps, 544 px per step); cell = steps moved / page moved / where it settled (off = px from the nearest rest)

| gesture | native (today) | CSS snap only (no controller) | controller, no entry control | controller + CSS snap | controller, fires on move | controller + clamp + settle (proposed) |
|---|---|---|---|---|---|---|
| very slow drag 120 px (2 px / 16 ms) | +0 step / +105 px / off +105 | +0 step / +0 px / off +0 | not run | +1 step / +544 px / off +0 | +1 step / +544 px / off +0 | +1 step / +544 px / off +0 |
| slow drag 150 px | +0 step / +135 px / off +135 | +0 step / +0 px / off +0 | not run | +1 step / +544 px / off +0 | +1 step / +544 px / off +0 | +1 step / +544 px / off +0 |
| slow drag 300 px | +1 step / +285 px / off -259 | +1 step / +544 px / off +0 | not run | +1 step / +544 px / off +0 | +1 step / +544 px / off +0 | +1 step / +544 px / off +0 |
| tiny nudge 20 px | +0 step / +5 px / off +5 | +0 step / +0 px / off +0 | not run | +0 step / +0 px / off +0 | +0 step / +0 px / off +0 | +0 step / +0 px / off +0 |
| drag 300 forward, 200 back, lift | +0 step / +85 px / off +85 / steps flashed 1,2,1 | +0 step / +0 px / off +0 / steps flashed 1,2,1 | not run | +1 step / +544 px / off +0 | +1 step / +544 px / off +0 | +1 step / +544 px / off +0 |
| drag 100 forward, 100 back, lift | +0 step / -15 px / off -15 | +0 step / +0 px / off +0 | not run | +0 step / +0 px / off +0 | +1 step / +544 px / off +0 | +0 step / +0 px / off +0 |
| two 300 px @3000 flicks, 150 ms apart | +8 step / +6115 px / outside / steps flashed 1,2,3,4,5,6,7,8,9 | +2 step / +1087 px / off -1 / steps flashed 1,2,3 | not run | +1 step / +544 px / off +0 | +2 step / +1088 px / off +0 / steps flashed 1,2,3 | +1 step / +544 px / off +0 |
| two 300 px @3000 flicks, 700 ms apart | +8 step / +7056 px / outside / steps flashed 1,2,3,4,5,6,7,8,9 | +2 step / +1087 px / off -1 / steps flashed 1,2,3 | not run | +2 step / +1087 px / off -1 / steps flashed 1,2,3 | +2 step / +1088 px / off +0 / steps flashed 1,2,3 | +2 step / +1088 px / off +0 / steps flashed 1,2,3 |
| flick 600 px @6000 arriving from 500 px above the story | lands on step 5, off -79 / +3140 px / steps flashed 9,0,1,2,3,4,5 | lands on step 0, off 0 / +844 px | lands on step 5, off 0 / +3219 px / steps flashed 9,0,1,2,3,4,5 | lands on step 0, off 0 / +844 px | lands on step 0, off 0 / +500 px | lands on step 0, off 1 / +501 px |
| flick 300 px @1200 arriving from 500 px above | lands on step 0, off 61 / +561 px | lands on step 0, off 0 / +844 px | lands on step 0, off 0 / +500 px | lands on step 0, off 0 / +844 px | lands on step 0, off 1 / +501 px | lands on step 0, off 1 / +501 px |
| slow drag 300 px arriving from 500 px above | ends outside the story / +285 px | ends outside the story / +0 px | not run | ends outside the story / +0 px | ends outside the story / +285 px | ends outside the story / +285 px |
| flick 300 @3000 from the last step (leaving) | ends outside the story / +2002 px | ends outside the story / +844 px | not run | ends outside the story / +844 px | ends outside the story / +2001 px | ends outside the story / +2002 px |
| flick 300 @3000 up from the first step (leaving) | ends outside the story / -2002 px | ends outside the story / -1400 px | not run | ends outside the story / -844 px | ends outside the story / -2001 px | ends outside the story / -2002 px |

What the comparison says:

- **Today (native)**: no gesture is deterministic. Slow drags settle 105 to 285 px off a rest; two quick flicks 150 ms apart carry the page through all 8 remaining steps of the 10-step story (+6115 px); a flick from 500 px above the story runs through the 4-step story (steps flashed 3,0,1,2,3) or lands on step 5 of 10.
- **CSS snap only** fixes flings (every flick is one step, enter flicks stop at the first rest) but: a 120 to 300 px slow drag returns to where it started (+0, the page will not move for a short deliberate drag, in the story and also at a section boundary: "slow drag 300 px arriving from 500 px above" stays at +0), a flick leaving the story is cut to one screen (+844 px instead of +2001 px), a finger drag longer than a step on the 544 px story still skips (600 px drags = 2 steps), and mandatory snapping is page-wide (every section becomes a snap area). Rejected as the mechanism. It is also not needed: the clamp does the one thing it was good at.
- **Controller without entry control** gives exactly one step for every gesture that starts inside the story, but a fling that arrives from outside still runs through (protoA: flashes 3,0,1,2,3 and leaves; protoB: lands on step 5 after flashing steps 0 to 4).
- **Fire on move** (first version) fires at 32 px and cannot take it back, so "drag 100 forward, 100 back" still stepped. Commit at release (default now) gives 0 steps for that drag and 1 step for "300 forward, 200 back" (net 100 forward).
- **Proposed**: all rows land on a resting place, one step, whatever the speed; the enter flick stops at rest 0 (+500 px from 500 px above, steps shown 3 to 0 only because the bench's previous row left it on step 3); the exit flick is free (+2001 px); the slow drag arriving from above is free (+285 px); the second flick 150 ms after the first is swallowed by the 420 ms lock (1 step, +856 px) and 700 ms later it counts (2 steps). If that lock feels slow in use, it can be shortened; the swallow rule is what keeps "two flicks, 150 ms apart" from skipping.

### Wheel and trackpad (desktop 1440x900, same bench, `results-prove-wheel2.json`)

Start at the second step's rest; one gesture each. Step moved / page moved:

| gesture | today (free scroll) | proposed, controller on | proposed, reduced motion |
|---|---|---|---|
| one notch (100 px) | 0 / +100 px (half step) | +1 / +912 px | +1 / +912 px |
| 5 notches, 40 ms apart | +1 / +500 px | +1 / +912 px | +1 / +912 px |
| 30 notches, 10 ms apart | +2 / +3000 px | +1 / +912 px | +1 / +912 px |
| trackpad swipe: 60 events decaying over 900 ms | +1 / +857 px | +1 / +912 px | +1 / +912 px |
| two notches, 700 ms apart | 0 / +200 px | +2 / +1824 px | +2 / +1824 px |
| one notch up (-100) | 0 / -100 px | -1 / -912 px | -1 / -912 px |

(+912 px is the bench's step gap at 900 px tall windows.) A first wheel run started from a plain `scrollTo`; the page was held at rest 0 as an "entry" and the numbers were off by one step, which is how the programmatic-jump rule (rule 11) was found; the table above is the second run with the start made from inside the hold.

## 7. Lag: what is actually slow (production, 4x CPU throttle, 6 constant drags of 700 px)

Frames while dragging from the top through the statement into the Lab (`results-prove-lag.json`, profile `profile-lag.json` summarised by `profsum.mjs`):

- At 1x CPU (probe perf run): p50 6.1 ms, p95 12.1 ms, max 42 ms, 2 frames over 25 ms: fine on a desktop. At 4x (a mid-range phone is 4 to 6x slower): p50 15.9 ms, p95 24 ms, p99 32 ms, max 221 ms, 26 frames over 25 ms, 6 over 50 ms in about 23 s.
- The long frames, from the Long Animation Frames API: one of 210 ms with no script (style/layout/render: a section being drawn), one of 118 to 158 ms whose script is a `FrameRequestCallback` in chunk `01~804s7l7.6y.js` at offset 50,934, which is ScrollStory's `fitAll` + `measureSlack` callback (`ScrollStory.jsx:164-184`: `removeProperty`, then `getBoundingClientRect` / `getComputedStyle` / `offsetHeight`, up to 3 passes per marked node, forced layout each time a story's section is drawn or fonts load), and one of 108 to 116 ms that is `MessagePort.onmessage` in chunk `15euem4lyi_on.js`, which contains React's scheduler (`MessageChannel`): a React render, i.e. `setStep` / `setLive` re-rendering the whole stage (`ScrollStory.jsx:147-148`).
- CPU profile (23.2 s sampled at 4x): 54% `(program)` (browser style, layout, paint, raster: not attributed to script), 32% idle, 4.2% the object "lean" scroll handler (`17pwiblfjlk0w.js:24147`, writes `scrollDelta` and wakes a rAF loop every scroll event), 3.0% Pip's gaze callback (`0ssi8vcg7qkb0.js:4391`, a rAF per scroll event that calls `querySelectorAll` and sets `data-pip-looking`), 1.4% `querySelectorAll` (called by those two), 0.7% self time in the ScrollStory fit callback (its forced layout is booked under `(program)`).
- Negative result: removing every `backdrop-filter` (nav 18 px, nav fade 10 px, dock 20 px; `feature-tour.css:101-104`) and the `.rv` reveal blur (`filter: blur(6px)`, `feature-tour.css:105`) changed nothing measurable in headless Chrome (p95 24, 24, 24, 24 ms; max 221, 238, 254, 219 ms; over-25-ms frames 26, 24, 20, 26). Headless uses software raster, so this does not clear them on a real GPU; it only says they are not the cause here.

So the lag is a handful of 100 to 250 ms frames at the moments a story arrives or a step changes (forced layout in `fitAll`, a stage re-render, section draw), plus two always-on per-scroll loops. The controller above removes the step changes from the scroll path (no beats flipping during a fling, rule 9) but the `fitAll` forced layout and the content-visibility draw need their own fixes: run `fitAll` only on a width change (read all rects first, write after), reserve the right intrinsic size (`#your-prep` 680svh + its header, then re-measure the others), and make the lean and Pip loops sleep while a held story is on screen.

## 8. Risks, and what this bench cannot show

- **R1 iOS Safari (not tested).** No device and no WebKit here. Things to confirm on a real iPhone: a non-passive `touchmove` listener on `window` is honoured (it must be registered with `{ passive: false }` explicitly); preventDefault must happen before Safari commits to scrolling, about the first 10 px, so the slop is 6 px and the sub-slop moves are cancelled (but that also cancels the first moves of a gesture that turns out to be "the way out", so the exit may feel a hair stiff: test it); `scrollTo` during momentum stops the momentum on iOS (the clamp relies on it and on `scroll` events firing every frame during momentum, which should be true on current iOS); `scrollend` may be missing on the Safari in use (the bench already falls back to a 150 ms quiet timer); the dynamic toolbar changes the viewport height (`svh` stays stable, but the cached `top`/`hold` must be re-measured on `visualViewport` resize).
- **R2 Android Chrome (engine tested, device not).** The bench is Chrome 151 with CDP touch input; Android's fling curve differs (distance per release speed), but the mechanism does not depend on it: it ignores speed except for the 12 px short-flick rule.
- **R3 cost of a non-passive touchmove.** Once a non-passive `touchmove` exists Chrome waits for the main thread to answer the first move before it starts scrolling, so on a janky main thread (the 100 to 250 ms frames above) the finger moves first and the page follows late; Chrome also marks `touchmove` non-cancelable once scrolling has begun or after a long stall, in which case an owned gesture scrolls natively by the finger distance. The page then self-heals (the commit calls `scrollTo(rest(next))`, an uncommitted drag is settled back by rule 8) but a visible jiggle is possible. Mitigations: register the non-passive `touchmove` only while the page is within one screen of a story (ScrollStory already has that observer, `ScrollStory.jsx:153-156`), keep the handler a few lines, and fix the stalls first.
- **R4 content-visibility.** Cached `top`/`hold` are wrong until a section has been drawn once (section 5.5). Fix the reserved sizes and re-measure on `contentvisibilityautostatechange`, otherwise the clamp positions are off by up to 950 px for stories after the tour.
- **R5 accessibility.** Keyboard users keep native scrolling for `Home`/`End`/`Tab`/mouse-wheel-free paths (settle then rests them); arrow keys and Space step once per press; focus into an off-stage step still brings it on (`ScrollStory.jsx:243-248`); every step stays in the DOM. Screen readers and find-in-page still move by position and settle.
- **R6 inner scrollers and sideways gestures.** Any element inside the stage that scrolls vertically (none today) needs the old `scrollsInside` check (present in `f42b898c6^:ScrollStory.jsx`); horizontal rails (chips, reels) are left native by the `|dx| > |dy|` rule.
- **R7 the owner's two rules.** LK47 ("do not catch the scroll, it raced") and L-027/LK69 ("one gesture, one step") pull opposite ways in his own words. This mechanism satisfies LK69 without LK47's cause (no glide, no visible jump: the stage only swaps, and the clamp holds the page exactly where the stage becomes sticky). He should still get to see it live on his phone, and the old test has to be replaced as in rule 14.
- Not tested: iOS, a real Android phone, desktop Safari, Firefox, real 120 Hz devices, and the statement as a step story (not built; rule 10 is a design decision).

## 9. Files (this folder: `C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/scroll`)

- `RESULTS.md` (this file); `compare.md` (variant table), `prod-special.md`, `matrix-prod.md`, `matrix-native.md`, `matrix-clamp.md` (matrices).
- Probes: `probe.mjs` (production table, from the stopped run, unchanged), `probe2.mjs` (adds reversing and 120 px / 16 ms drags, the six bench variants, and `prodrev`), `prove.mjs` (delivery proof, lag A/B, wheel), `prove-wheel.mjs` (wheel run with a second jump), `prof.mjs` + `profsum.mjs` (CPU profile), `matrix.mjs`, `compare.mjs`, `queue.sh`.
- Bench: `prototype-one-gesture-v2.html` (the proposed mechanism, about 150 lines of script); `prototype-one-gesture.html` is the stopped run's v1 (its scroll-snap "latch" did nothing: proximity snapping does not reach a far stop).
- Raw: `results-main.json/.md` (production table), `results2-prodrev.json`, `results2-p2-{clamp,clampmove,native,snaponly,snapctrl,noentry}.json/.md`, `results-prove-delivery.json`, `results-prove-lag.json`, `results-prove-wheel2.json` (and the polluted first run `results-prove-wheel.json`), `profile-lag.json`, logs `run*.log`.
- Screenshots (all opened): `proof-*.png` (delivery runs), `lab-r1-slowdrag-513.png`, `lab-r1-slowdrag-300.png`, `tour-r1-slowdrag-300.png`, `statement-slowdrag-300.png`, `proof-flick-60-3000.png`, plus the stopped run's `v1-*.png`.
