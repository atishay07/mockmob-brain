# Home hero, round 2 (LK32): the proposal and its ranked fixes

1 Nov 2026. Lens: the home page hero. He "loves the direction" but wants about 10 to 20% less space spent on the details, a more branded look than "this vague SVG and PNG integration", and a hero that reacts when he taps something, Mobi for example, using the animation and promo-film assets we already have (OWNER-FEEDBACK-2026-10-31-LEARN.md, 4:05 pm, LK32; also LK24 clutter, LK28 speed, LK29 first-time cues, LK30 blank space).

Evidence (live production, signed out): `tmp/learn-1101/r2-before/live-home/home-first-screen-390-night.png`, `-390-day.png`, `-1440-night.png`, `-1440-day.png`, `home-full-390-night.png` (crop y 750 to 1700 css px), `home-full-1440-night.png` (top 1300 px).

## What is on screen today (measured from the 390 x 844 shots, CSS px)

| Band | Today (y) | Height |
| --- | --- | --- |
| Site bar | 0 to 62 | 62 |
| SVG room (`HeroScene.jsx`), the PNG Mobi (`greeting.webp` through `MascotSeat`), bubble "Hi, I'm Mobi. Let's find yours." | 62 to 430 | about 370 (`--scene-h: clamp(17rem, 44svh, 26rem)`) |
| "For CUET UG 2027" | 442 | 40 |
| H1, 3 lines | 470 to 585 | 115 |
| Lead, 2 lines | 598 to 640 | 42 |
| "Try five questions" + "Start free practice" | 659 to 760 | 100 |
| Three stacked reassurances | 778 to 845 | 70 (+ gaps, about 90) |
| Bank sentence, 3 lines | 860 to 915 | 55 to 70 |
| Demo stage | 927 to 1663 | 736 |

The first screen ends in the middle of the reassurances; the stage, the thing a first-timer can actually use, starts 83 px below the fold. At 1440 (`home-first-screen-1440-night.png`) the proof row starts at 940, below the 900 px screen, the left column has an empty band between the reassurances (711) and "Try the exam-day screen" (816), and Mobi stands outside the grid at x 1280 to 1410 with a caption ("Mobi's on your side. Even at 11pm."), cut by the right edge in the full-page shot.

## Brand assets inventory (what exists, what the hero uses)

| Asset | Where | Size | Used in the hero? |
| --- | --- | --- | --- |
| The app's painted welcome room, Night (the same file the Play app's welcome screen draws) | `public/art/scenes/scene-welcome-hero-night-1080.v2.avif` / `-1296` (+ webp); master in the app `flutter_app/assets/art/scene-welcome-hero-night.webp` | 144 KB / 197 KB avif, 1296 x 1620 | **Yes**, as a new cropped band file (item 1) |
| The app's Day room (the app's Day welcome uses it: `WelcomeHeroLayout.day`) | `public/art/scenes/scene-empty-allclear-day-768.v2.avif` / `-1280` / `-1536` | 24 KB / 40 KB / 39 KB avif | **Yes** (Day) |
| Room anchors (feet, ellipse, lamp, sheet) shared with the app | `data/scene-anchors.json` (`welcome`, `vignette.scenes.allClear`); app constants in `flutter_app/lib/features/onboarding/widgets/welcome_scene.dart` (footX 0.504, footY 0.857, mobiWidthShare 0.5185; day footX 0.514, footY 0.796, dayGrow 1.5) | data | **Yes** |
| Room life (lamp breath, dust motes, stars; by Day the floor pool) | `src/components/scenes/SceneLife.jsx`, `sceneModel.mjs lifeLayers()` | code | **Yes**, one breath |
| Mobi, the rigged character (web twin of the app's MobiFigure; 31 acts, moods, blink, tap cycle, eye follow) | `src/components/brand/MobiReact.jsx`, `MobiFigure.jsx`, `mobiSim/Rig/Paint/Dom.js`, `data/mobi_rig.v2.json`; tap cycle `src/lib/mobiMoments.js` `TAP_CYCLE = { acts: hello, tilt, hop, startle; resetAfterMs 8000; cap 6 }`, `FOLLOW` | about 44 KB gzip as source, rig JSON 6.8 KB gzip | **Yes**, replaces the PNG |
| Mobi PNG poses (what the hero shows now) | `public/brand/mascot/*.webp` (greeting 31 KB) + `PipGuide`/`PipActor` CSS hops | 30 KB each | No longer in the hero (still used by PipGuide's other seats) |
| Logo B (Mobi as the second "o"; full master has an answer-bubble eye) | `src/components/brand/logoB.js` | paths | Yes, a 1-frame wink tie-in (item 14) |
| 3D Mobi frame sequences from the promo film (Blender, 60 fps, alpha PNG) | `C:\Users\atish\Desktop\MockMob-promo-film\public\mobi3d\` : `logo/r8c-f2` (212 frames, 1988 x 1118, the logo landing), `open/r8c-f3` (399), `End/r8c` (34, 302 x 688), `everything-r8c4` (837), `unlimited-host-r8c-f3` (418, 500 x 450), `findfix-host-r8c-f4` (354), `examday-r8c-c` (323), `mob-r8c4` (324) | 3 MB to 400 MB per sequence, 0.2 to 1 MB per frame | **No** (see "Rejected"); `End/r8c` (34 frames, 3 MB) is the only one small enough to ever become a sprite |
| Promo film stills | `MockMob-promo-film\public\art\mobi\mobi-{cheer,greet,point,read,think}.png` (about 600 KB each), `art\brand\wm-*` (wordmark letters), `art\folds\`, `art\open916\` | large PNG | No |
| Promo film sound (UI layer the film used) | `MockMob-promo-film\public\sfx\` : pop_soft, pop_bright, paper_flick, paper_slide, tick_soft, tick_ui, chime_up, ding_success, seal_pop, swish_card, logo_hit ... (37 wav) plus ElevenLabs sets `sfx-el\`, `sfx-el-paid\` | 6 MB wav | **No** on the web for now (item 19) |
| Rendered reels | `MockMob-promo-film\out\reel916\final-cuts\mockmob-reel916-cut15-phone.mp4` (4.5 MB), `cut30-phone.mp4` (7.2 MB), `final-r2\mockmob-reel916-phone.mp4` (25.8 MB) | MB | **No** in the hero; the 15 s cut belongs to the reels band (`CreatorReels.jsx`) or the close band, `preload="none"`, poster only |
| Folds (the Mob's paper characters: crane, cutting, dart, dogear, hexa, hop, kandil, naav, patang, stamp, sticky, tally) | `public/mob/folds/*.webp` | 256/512 webp | No: one character per hero (W-074) |
| App welcome screenshots (the reference for the twin) | `C:\Users\atish\Desktop\MockMob-promo-kit\screens\01-welcome-night.png`, `02-welcome-day.png` | | Reference |
| Motion tokens | `shared/motion-tokens.json` (press 100, release 140, fadeThroughOut 90, fadeThroughIn 210, reducedFade 120, enter 360, gelSquash 100) | | Yes |

## The one hero to build

**The website's first screen becomes the twin of the Play app's welcome**: the app's own painted room (not a redrawn SVG), the real rigged Mobi standing in its light (not a PNG), and Mobi answers taps with a short line in his bubble. The details under it shrink by about 20%, and the try-it stage starts on the first screen.

**390 x 844, Night and Day (after):**

| Band | y (css px) | Height | Change |
| --- | --- | --- | --- |
| Site bar | 0 to 62 | 62 | same |
| Room: painted room, Mobi (MobiReact, 178 px tall), bubble | 62 to 382 | 320 | was 370 (-14%) |
| H1 (3 lines, unchanged words and motion) | 394 to 509 | 115 | "For CUET UG 2027" removed (-40) |
| Lead (2 lines, unchanged) | 521 to 563 | 42 | same |
| Key "Try five questions" + text link "Start free practice" | 583 to 683 | 100 | same |
| Two quiet lines: reassurances on one line, bank on one line | 695 to 741 | 46 | was about 160 (-114) |
| Demo stage begins ("Your first question. Go.") | 761 | | was 927; its heading and the card's top edge are on the first screen |

Details band (eyebrow to bank line): 473 px today, 347 px after (-27%); whole hero above the stage: 853 px to 699 px (-18%). That is inside his 10 to 20%.

**1440 x 900 (after):** two columns stay (copy 1.06fr, stage 1fr). Left column loses the eyebrow, the bank paragraph becomes one line, the two tool links share one row; the stage loses its duplicate lines; Mobi leaves the right margin and stands as the stage's host in the gutter. The hero ends (proof row bottom) at about 860, inside the 900 px screen (today 1040).

**Mobi on tap:** see items 2 and 3 (acts, ms, lines, reduce motion, no sound).

**Budget:** see item 9 (room band 50 KB avif eager-lazy, 0 KB of Mobi image, MobiReact chunk under 35 KB gzip after idle, no video anywhere in the hero).

## Ranked items

### 1. Room: replace the drawn SVG room with the app's painted room
- **Surface:** phone hero room (max-width 760 px), Night and Day.
- **Wrong:** `home-first-screen-390-night.png` and `-390-day.png`: the room is a flat hand-coded SVG (`HeroScene.jsx`: rect books, a polygon city, a 5 x 7 dot sheet) that imitates the app's painted room and loses to it; next to the 3D-looking Mobi it reads as the "vague SVG" he named. The Play app's welcome (`MockMob-promo-kit\screens\01-welcome-night.png`) shows the same idea done well.
- **Why:** LK32 "more branded". A student who installs the app after the site sees the same room twice: one brand, not two drawings.
- **Fix:**
  - Night: `scene-welcome-hero-night` cropped to a band. Build `public/art/scenes/scene-welcome-band-night-780.v2.avif` and `-1170.v2.avif` (+ webp) from the 1296 x 1620 master, crop y 0.20 to 0.95 of the painting (1296 x 1215), same grain/ground pipeline as `src/components/scenes/tools/build-scene-files.mjs` (add an entry; never edit outputs by hand). Targets: 780w avif at most 55 KB, 1170w at most 95 KB.
  - Day: the app's Day welcome file, `scene-empty-allclear-day` (768/1280 already exist, 24/40 KB), drawn 1.5 x the screen width, centred, its feathered sides running off-screen (the app's `dayGrow 1.5`).
  - Placement at width W (390): Night painting drawn W wide (full painting height 1.25 W); position it so the floor ellipse centre (cy 0.853) sits 28 px above the room's bottom: `top = 320 - 28 - 0.853 x 1.25 W` (at 390: -124 px; visible painting y 0.25 to 0.91: the lamp's cone enters from the top, window left, sheet right, floor pool). Day: painting 1.5 W wide, height 1.0 W; ellipse cy 0.785 sits 28 px above the bottom (at 390: top -14 px).
  - The room meets the site bar with the existing top fade (mask 0 to 7%) and the page at the floor (84 to 100%). In Day the Day room's own feathering does that.
  - Room height `--room-h: clamp(17rem, 38svh, 20rem)` (320 px on 844-tall phones; 272 on 640-tall phones).
  - Delete `HeroScene.jsx` and the room half of `hero-scene.css` (lines 14 to 72 and the SVG rules); keep the bubble and the entrance rules.
- **Files:** `src/components/landing/HeroScene.jsx` (replace with `HeroRoom.jsx`), `src/app/hero-scene.css`, `src/app/page.js` (line 182), `src/components/scenes/sceneModel.mjs` (add `kind: 'welcomeBand'`), `src/components/scenes/tools/build-scene-files.mjs`, `public/art/scenes/`, `src/components/landing/heroScene.test.mjs`.

### 2. Mobi: the rigged Mobi (MobiReact) in the light, answering taps
- **Surface:** the Mobi in the phone room; the Mobi in the 1440 hero.
- **Wrong:** `home-first-screen-390-night.png`: Mobi is `greeting.webp`, a still PNG with CSS transforms (`MascotSeat` + PipGuide's `pip-wave`); tapping him does nothing. At 1440 he is a separate PNG in the margin.
- **Why:** LK32 "reactive on tapping ... the mobi". The real Mobi already exists on the web (`MobiReact`: the app's rig, 31 acts, blink, moods, a tap cycle and pointer follow). A 16-year-old pokes a character first; the poke should pay off and point at the next step.
- **Fix:**
  - Render `<MobiReact act="appear" interactive follow />` (follow is pointer-only, so desktop) inside a `<button type="button" class="lp-mobi" aria-label="Mobi. Tap for a tip.">`, 44 x 44 px minimum hit area (it is far bigger), focus ring `2px solid var(--focus-ring)` offset 4 px, Enter and Space act like a tap.
  - Size: height = `min(0.46 W, room - 120px)` (178 px at 390, 166 at 360, 198 at 430). Feet: Night at (0.504, 0.857) of the painting, Day at (0.514, 0.796), converted with the item 1 offsets; his contact shadow is the painting's pool, so no CSS shadow.
  - Tap: press `scale(0.97, 0.94)` from the feet, 100 ms (`press`), release 140 ms (`release`); then the next `TAP_CYCLE` act: hello 1850 ms, tilt 1100 ms, hop 800 ms, startle 950 ms; never the same twice; cycle resets after 8 s without a tap; after 6 acts a visit, only the squash (all as `MobiReact` already does). Taps during an act restart the cycle step, never stack.
  - Android: `navigator.vibrate?.(8)` on each tap that plays an act, not under Reduce motion and not when Celebrations is Off. iOS has no API; nothing.
  - The one-Mobi rule (W-074): PipGuide must no longer use `station="hero"`; it starts at the next seat. The PNG `MascotSeat` leaves the hero.
  - Drop PipGuide's "glance at the headline when it changes" for the hero (PipGuide.jsx line 269): with a line every 2.3 s (D120) it would fight the tap acts.
- **Files:** `src/app/page.js` (line 182), new `src/components/landing/HeroMobi.jsx` (client island), `src/components/brand/PipGuide.jsx`, `src/components/brand/pipJourney.js`, `src/app/hero-scene.css`, `src/components/landing/landingMobi.test.mjs`.

### 3. The bubble: one first-time cue, then a line per tap (copy word for word)
- **Surface:** the bubble over the window, top left of the room.
- **Wrong:** `home-first-screen-390-night.png`: "Hi, I'm Mobi. Let's find yours." Yours what? It never changes and never says he can be tapped.
- **Why:** LK29 (first-time cues: show how a thing works), LK32 (reactive), LK24 (the facts move out of the details band into something he chose to tap).
- **Fix:** bubble `max-width: min(11rem, 46%)`, 16 px from the room's top and the gutter; tail points down-right at Mobi.
  - On load: **"Hi, I'm Mobi. Tap me."**
  - Tap 1 (hello): **"I find where your marks slip."**
  - Tap 2 (tilt): **"One timed mock shows me the chapter."**
  - Tap 3 (hop): **"5,765 questions. A fresh mock every time."** (the live count from `/api/stats`, as `QuestionBankLine`; without it: **"One big bank. A fresh mock every time."**)
  - Tap 4 (startle): **"Okay, okay. Try five questions?"** and the "Try five questions" key does one 2 px lift and settle (240 ms, transform only, no glow).
  - Tap 5: **"Free to start. These five need no signup."**
  - Tap 6: **"That's all my tips. Go on, try one."** (stays; later taps only squash).
  - Swap motion: old line fades out 90 ms; new line fades in 210 ms from `translateY(4px) scale(0.96)`, origin at the tail (`fadeThroughOut`/`fadeThroughIn`). The bubble is an `aria-live="polite"` region.
- **Files:** `HeroMobi.jsx`, new `src/components/landing/heroTaps.mjs` (the six lines, pure, tested), `src/app/hero-scene.css`, `src/components/landing/landingCopy.test.mjs`.

### 4. Cut the details band by about 27% on the phone
- **Surface:** phone hero copy under the room.
- **Wrong:** `home-first-screen-390-night.png`: an eyebrow that repeats the H1 ("For CUET UG 2027" over "CUET 2027."), three stacked check lines (778 to 845), and a three-line bank sentence (`home-full-390-night.png` crop, 860 to 915): the first screen ends mid-list and the stage is below the fold.
- **Why:** LK32 "consume a bit less of the details space ... 10%, 20%", LK24 clutter, LK31 walls of text.
- **Fix:**
  - Remove `<p className="lp-hero__for">` at every width (the H1 carries "CUET 2027.").
  - Reassurances on one line, 0.8125 rem, `--ink-2`, middle dots, no check icons on phones: **"Free to start · Pro ₹99 a month · Cancel anytime"** (keep `priceLine(OFFER)` and the No-auto-renewal variant).
  - Bank on one line under it, same style: **"One bank of 5,765 questions. No cap on Pro."** (count from `/api/stats`; without it **"One live question bank. No cap on Pro."**). The long sentence (subject claim) stays on desktop and in the FAQ.
  - Spacing: H1 12 px under the room; 12 px H1 to lead; 20 px lead to key; 12 px key block to the two lines; 4 px between them; 20 px to the stage.
- **Files:** `src/app/page.js` (lines 182 to 209), `src/components/landing/QuestionBankLine.jsx` (add `variant="short"`), `src/app/hero-scene.css`, `src/app/home-refinements.css`.

### 5. Desktop 1440: Mobi becomes the demo's host; the column and stage shrink
- **Surface:** 1440 hero.
- **Wrong:** `home-first-screen-1440-night.png`, `-1440-day.png`: Mobi floats in the right margin (x 1280 to 1410) with a two-line caption, detached from everything; the left column has an empty 100 px band (y 711 to 816); the proof row starts at 940, below the screen.
- **Why:** LK30 blank space, LK32 reactive and branded. On desktop the demo is the hero's working part; Mobi belongs to it.
- **Fix:**
  - Mobi (MobiReact, 140 px tall, `follow` on) stands in the column gutter at the stage's lower left, feet on the stage's bottom edge line, overlapping the stage's border by 36 px, facing the card. No caption. On load: `appear` (750 ms) then `nudge` (1050 ms, held point at the card). When the demo is answered: right answer `correct` (1150 ms), wrong `encourage` (1450 ms), via the existing demo signal (`demoSignal.mjs`). Tap: item 2's cycle; bubble above his head, item 3's lines.
  - Left column: no eyebrow; bank paragraph to one line (item 4 copy); "Free DU eligibility and cutoff calculator" and "Try the exam-day screen" on one row, 24 px apart, 16 px under the reassurances.
  - Target: proof row bottom at 860 or less at 1440 x 900.
- **Files:** `src/app/page.js`, `src/components/brand/Mascot.jsx` (hero seat removed), `src/app/landing.css`, `src/app/home.css`, `src/app/hero-depth.css`, `HeroMobi.jsx`.

### 6. The demo stage: cut its repeated lines (phone and desktop)
- **Surface:** "Your first question. Go." stage inside the hero.
- **Wrong:** `home-full-390-night.png` (crop y 927 to 1663) and `home-first-screen-1440-night.png`: "No signup" (header) and "Tap an answer. No signup needed." say the same thing; a dashed "The reasoning shows up here" skeleton fills 100 px before anything is answered; "Answer — Read why it's right" and "Five original CUET-style questions. Every answer comes with the why." say the same thing again. The stage is 736 px tall on a phone.
- **Why:** LK30, LK31 (too many lines), LK24.
- **Fix:** keep the header pair; remove "Tap an answer. No signup needed."; the reasoning panel is not rendered until an answer is chosen, then it opens (height 0 to auto by `grid-template-rows: 0fr` to `1fr`, 240 ms `card`); remove the "Answer — Read why it's right" path row; keep one line under the card: **"Five CUET-style questions, each with the why."** and "Taking other subjects? Sign up free and pick yours". Target stage height before an answer: 560 px or less at 390.
- **Files:** `src/app/page.js` (lines 212 to 220), `src/components/landing/DemoDrill.jsx`, `src/app/landing.css`.

### 7. Each tap fills one answer bubble on the wall sheet (Night)
- **Surface:** the pinned answer sheet in the Night room.
- **Wrong:** today's sheet is decoration that never responds (`home-first-screen-390-night.png`).
- **Why:** LK32 reactive; it ties his tap to the product's idea (marks found, one at a time) without a word.
- **Fix:** an SVG overlay inside the room box, same coordinate frame as the painting (`viewBox="0 0 1296 1620"`, positioned like the image). Six empty bubbles are filled in order, one per act-playing tap: (row 2, col 3), (3, 2), (4, 4), (2, 6), (6, 1), (5, 5) (1-based, the painting's 6 x 6 grid; centres measured from the 1296 master and stored in `data/scene-anchors.json` under `welcome.sheetBubbles`, never guessed in CSS). Fill: volt `#D2F000` circle, radius equal to the painted ring's inner radius, `scale(0 to 1)` 180 ms `cubic-bezier(0.23, 1, 0.32, 1)`, 120 ms after the tap (lands on the hop's apex). Reset when the page reloads only. Day: no overlay (the Day sheet is already full; "all clear").
- **Files:** `HeroRoom.jsx`, `data/scene-anchors.json` (+ the app's `shared/scene-anchors.json` twin, which the scene test compares), `src/app/hero-scene.css`.

### 8. Entrance: once, short, in this order
- **Surface:** phone and desktop hero, first load.
- **Wrong:** today the light, the PNG rise and a 1300 ms `pip-wave` play, then PipGuide may fly him; nothing hints at tapping.
- **Fix (no-preference motion):** room image fades in 200 ms once decoded (SceneImage's rule); Mobi `appear` (750 ms) starting at 150 ms; H1 rise 420 ms at 240 ms (unchanged); key at 330 ms; bubble 260 ms at 900 ms ("Hi, I'm Mobi. Tap me."). Room life: `SceneLife` with one breath (8 s: lamp glow, motes, stars; Day: the floor pool), then it removes itself; add a `breaths` prop (default 3, hero passes 1). If he has not been tapped after 3.5 s on a phone, one `curious` (1400 ms) looking down at the key, never repeated.
- **Files:** `src/app/hero-scene.css`, `HeroMobi.jsx`, `src/components/scenes/SceneLife.jsx`.

### 9. Performance budget (LK28)
- **Surface:** home, phone first.
- **Wrong:** the hero ships an eager 31 KB PNG Mobi, about 9 KB of inline room SVG and 229 lines of room CSS, and the PipGuide chunk wakes for the hero seat.
- **Fix, hard limits:**
  - Room: one file per theme, only the shown theme fetched (both `<img>` in the markup with `loading="lazy" decoding="async"`, the other theme's `display: none`, which browsers do not fetch); width/height attributes and `aspect-ratio` so CLS stays 0. Night 780w avif at most 55 KB (1170w at most 95 KB for 3x phones); Day 768/1280 avif 24/40 KB. `sizes="100vw"` (Night) / `"150vw"` (Day).
  - Mobi: 0 image bytes. The first frame is a generated static SVG string (a build script runs `virtualPaint` on the `appear` first frame and writes `src/components/landing/mobiPoster.generated.js`), rendered by a server component, about 5 KB of HTML. `MobiReact` loads with `dynamic(() => import(...), { ssr: false })` on `requestIdleCallback` (timeout 2000 ms) or on the first `pointerdown`/`keydown` on the button, whichever comes first, and replaces the poster in the same frame (identical first frame, no jump). A tap before it loads shows the line at once and plays the act when ready. Chunk at most 35 KB gzip (check with `next build` output; today's source is about 44 KB gzip before minifying).
  - No video, GIF or frame sequence anywhere in the hero, phone or desktop.
  - Targets on a mid-range phone, 4G, cold: LCP 2.0 s or less (the H1 or the room), CLS 0, TBT 150 ms or less; Lighthouse mobile performance 90 or more on `/`.
- **Files:** `HeroRoom.jsx`, `HeroMobi.jsx`, new `scripts/brand/build-mobi-poster.mjs`, `src/components/brand/PipGuideLazy.jsx`.

### 10. Reduce motion, Celebrations and accessibility
- **Fix:** under Reduce motion (device or the student's switch): no acts; Mobi holds his still pose; a tap swaps the bubble line by a 120 ms fade (`reducedFade`) and fills the sheet bubble by a 120 ms fade (no scale); no SceneLife; no vibration. Celebrations Quiet: hop becomes nod (MobiReact rule); Off: only the squash, lines still change. The button's label stays "Mobi. Tap for a tip."; the bubble is the live region; the room images are `alt=""`.
- **Files:** `HeroMobi.jsx`, `src/app/hero-scene.css`.

### 11. Day theme: the bright room, not a dark box on cream
- **Wrong:** `home-first-screen-390-day.png`: the Day SVG room is pale beige shapes with a sun shaft; little reads at a glance.
- **Fix:** the app's Day room (`scene-empty-allclear-day`, item 1): window with hills, floor lamp, full volt sheet, sunlit pool; Mobi 0.44 W tall at (0.514, 0.796); bubble white `#fff`, ink `--ink`, 1 px `rgba(23,32,22,0.08)` border (the current Day bubble tokens). Matches `MockMob-promo-kit\screens\02-welcome-day.png`.
- **Files:** `HeroRoom.jsx`, `src/app/hero-scene.css`.

### 12. Short and wide phones
- **Fix:** height under 700 px (360 x 640): `--room-h` 272 px, Mobi `min(0.46 W, room - 110px)`, bubble one line ("Hi, I'm Mobi. Tap me." fits 11 rem at 0.8125 rem). 430 wide: the painting grows with W, Mobi 198 px; the bubble's right edge never passes Mobi's antenna (max-width 46%). Landscape phones (max-height 500 px): the room is not drawn (as today's two-column rule), Mobi sits beside the H1 at 120 px.
- **Files:** `src/app/hero-scene.css`.

### 13. Tablets 761 to 1100 px
- **Wrong:** the room never draws above 760 px and the margin Mobi crowds the stage at 1024.
- **Fix:** 761 to 1100: no room; item 5's host Mobi at 120 px; hide him under 900 px tall if the stage would push the proof row past the fold.
- **Files:** `src/app/hero-depth.css`.

### 14. Logo tie-in: the nav's Mobi-o winks on the first tap
- **Surface:** the wordmark in the site bar (Logo B, Mobi as the second "o").
- **Fix:** on the first act-playing tap only, the wordmark's Mobi eyes close and open once: `scaleY(1 to 0.1 to 1)` 160 ms, eyes only. Nothing under Reduce motion. One frame of brand continuity between the bar and the room; no other logo motion.
- **Files:** `src/components/NavBar.jsx` (or its logo component), `src/components/brand/logoB.js` (eye paths as separate elements), `HeroMobi.jsx` (dispatches a `mm:mobi-tap` event once).

### 15. H1 and lead stay; the third line keeps its D120 motion
- **Note:** he loves the direction and chose the typing line (D120). Do not touch the words or the morph; only its spacing (item 4). The `lp-title__brand` volt/olive colour stays.

### 16. Tests and checks to land with it
- `heroScene.test.mjs`: the room is the painted file (no `<svg className="lp-scene__art">`), only one theme file fetched, the box has width/height.
- `landingMobi.test.mjs`: hero Mobi is `MobiReact interactive`; PipGuide has no `hero` station; one Mobi in view at 1440 (W-074).
- New `heroTaps.test.mjs`: six lines, sentence case, none over 44 characters, no "mastered", no percentages, line 3 has a fallback without a number.
- Capture `tmp/learn-1101/r2-after/hero/` at 390 and 1440, Night and Day: load, after tap 1, tap 4 (key lift), tap 6; and 360 x 640. Lighthouse mobile on `/` with the numbers in item 9.

## Rejected (and why)

- **3D Mobi frame sequences as the hero Mobi** (`mobi3d/*`): 0.2 to 1 MB per frame; a 1-second act at 30 fps is 2 to 4 MB even as animated WebP. Fails LK28. The rig gives 31 acts for 0 image bytes.
- **The 15 s reel in the hero** (`mockmob-reel916-cut15-phone.mp4`, 4.5 MB): no video in the hero. If wanted, a "Watch the 15-second film" row in the reels or close band with a 30 KB poster and `preload="none"`.
- **Sound on tap** (promo-film `sfx/pop_soft.wav` and the rest): the website has no sound setting and a student opens it in class; an unasked sound breaks trust. Revisit only with a site-wide Sound switch, default off.
- **Tapping the lamp to switch Night and Day:** a hidden control that changes the whole page is a surprise, not a cue; the theme switch stays in the bar.
- **A Fold character next to Mobi:** two characters in one view breaks W-074 and adds clutter (LK24).
