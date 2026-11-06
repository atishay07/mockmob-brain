# Motion choreography for the whole app (UI phase 2)

14 October 2026, about 19:00 IST. This is a read-only spec; the area fixers build it. The owner's 18:30 feedback is the authority (`design-2026-10-13/OWNER-FEEDBACK-1014-1830.md`): "what matters is, while using it, the animations, motion design... that's where the interactivity of the apps comes from", together with "balanced is the highest... over-gamified [is] at the same level as less". Below that come `OWNER-FEEDBACK-1110.md`, `BUILD-BRIEF.md` sections 2, 7 and 10, the HIGH, Revolut and FamApp teardowns, `flutter-feasibility.md` (M06 budget) and the owner's UI standards section 8. His MockMob direction overrides the standards' generic no-glass line.

The bottom bar has its own spec, `ui-phase2/DOCK.md`, which wins on the bar. Section 5 below adds only the cross-app rules the bar must share and one conflict to settle.

Sources read: `lib/core/motion/*` and `lib/core/mascot/*`, the shell, dock, morph and transitions, the Today, runner and practice code paths named below, every `ui-blitz/*.md`, the motion frame goldens (`dock_travel_*`, `quick_start_frames_*`, `motion_lock_in_*`, `motion_next_*`, `motion_repair_ending_*`, `finish_stamp_*`, `mobi_frames_*`, `skeleton_frames_*`), and `tmp/app-shots/now-1810.png`. Nothing here has been watched on a device or a screen recording. Section 7 says how to do that.

Status labels in this document:
- **[works]**: built and visible in goldens or tests. "Works" never means verified in use.
- **[wrong]**: built, but it fails the brief or the balance rule.
- **[missing]**: not built, or built in core but used nowhere.

---

## 0. Verdict

1. **A lot of motion exists in code.** Phase 1A wired 45 items: entrances, count-ups, skeleton light, Mobi acts, the liquid dock, page transitions. In use it still reads as the app of 25 hours ago, for four reasons:
   - Most of it is one small, early event. A 14 dp rise with 45 ms steps finishes before the eye arrives, and nothing after it answers the student.
   - The motions that make an app feel connected while you use it are missing or unused:
     - a card growing into the page it opens (`MmTransition.container` is built and used nowhere);
     - the bar stepping aside for a task;
     - direction in tab switches;
     - a designed pull to refresh (Today, Review, Insights, Saved and Learn use the stock Material spinner).
   - The bar's best idea, the bubble inking, fires the moment the tab changes, before the tile arrives. In `dock_travel_right_night.png` at 40 ms it is a 50%-alpha olive disc behind the Review icon while the tile is still on Today. That is the "finish" he asked for twice.
   - No one has judged any of it from a recording.
2. **Some places are over-gamified.**
   - The practice finish fires a stamp, two rings, 24 shards, a volt flash, a sweep, Mobi and a haptic together.
   - The repair ending fires per-bubble ticks, a burst, a bloom, a roll, Mobi, the thread and a sweep.
   - The runner flies a comet with a five-dot tail across the question text on every answer, up to 50 times in a timed mock (`motion_lock_in_mid.png`).
   - Onboarding gives a light impact and a burst on every answer.
   - The Celebrations setting (Full, Quiet, Off) is honoured only by the repair ending and the rhythm module, not by the practice finish, the result reveal or the seal.
3. **Phase 2 motion therefore means four things:**
   - **Connect:** transitions carry the object from where it was tapped.
   - **Respond:** every touch answers in the next frame, in both themes.
   - **Ration:** one lead moment per screen, and a celebration ladder with a cap on how many things happen at once.
   - **Prove it:** recordings, not stills.

---

## 1. Rules for every screen

### 1.1 The balance budget (his ranking: balanced, then crowded, then sparse and over-gamified)

- **Response.** Every tappable thing answers on the next frame:
  - press-in on `Springs.snappy`;
  - a highlight veil;
  - a haptic per 1.6.

  No control waits behind an animation. A tap during an entrance works.
- **One authored entrance per screen visit.**
  - The lead element comes first, then its meaning, then the action, then the rest in reading order.
  - It takes 800 ms or less in total.
  - It never replays on tab reselect, a data refresh or a return from a pushed page.
  - Content that loads later staggers once.
- **One light event per visit at most.** A light event is a sweep, burst, bloom or glow pulse. It is allowed only for a ladder T2 or T3 moment (1.2), never on an ordinary open.
  - Exception: Today's hero top-edge sweep (700 ms, once per app run, not per visit).
- **Three channels at most at once:**
  - a number landing;
  - one light event;
  - one Mobi act.

  A haptic goes with them and does not count. Text never animates while any of the three is running, except to engrave once.
- **Nothing loops on a resting screen.** Mobi's scheduled idle beats are the only idle life.
  - Indeterminate waits may loop: the submit sending band, Ask's pending bubbles and the pull-refresh reading arc. After 12 s each settles and says so in words ("Still sending. Your answers are safe on this phone.").
- **Durations:**

  | What | Duration |
  | --- | --- |
  | Press | 90 to 120 ms |
  | Small state change | 150 to 220 ms |
  | A result or state landing | 220 to 350 ms |
  | Entrances and transitions | 300 to 450 ms |
  | T2 moment | 1200 ms or less |
  | T3 moment | 2000 ms or less |

  Everything else that is over 450 ms today is trimmed in section 4. Springs are specified by duration and bounce; bounce stays at 0.12 or less except on the bar and on Mobi.
- **Never moves:**
  - question text;
  - options (except their own press);
  - the timer digits;
  - explanation bodies;
  - numbers after landing;
  - rows of a list while it scrolls. Lists never fade in on scroll; only charts draw in, and only once.
- **Robustness:**
  - Every animation is interruptible. A new target starts from the current value; springs keep their velocity.
  - Nothing queues: rapid Next, Next, Previous cancels each question entrance where it stands.
  - Every custom page transition must look right when Android 16 predictive back drives it partway and cancels.
  - Tickers stop when offscreen (`TickerMode` on branches and routes).
  - A failed load never leaves a half-played entrance; the error state takes over without replaying.

### 1.2 The celebration ladder (one source of truth)

| Tier | When | What plays | Max length | Haptic |
| --- | --- | --- | --- | --- |
| T0 response | any touch | press, veil | 120 ms | per 1.6 |
| T1 state | answer locked, chip chosen, step done, stage of a thread, count changed | ink or flip of the thing touched, or a number roll | 350 ms | selection |
| T2 done | practice set acknowledged, repair finished, mock received, week met | the number lands, then **one** light event (a ring **or** a sweep, not both), then Mobi cheers once the number has landed | 1200 ms | success, after the ack |
| T3 rare | plan sealed, first full mock, a milestone landed, a higher mock result | the number or object lands, a foil burst (14 to 24 particles, one painter), Mobi proud or celebrate. **No** extra sweep or flash. | 2000 ms | medium at the impact, success after the ack |

Rules:
- A lower or held result gets T1 only, calm (already the rule in result and practice).
- A first mock gets T2 at most, never a score celebration.
- Never two T3 in one session: a second one is downgraded to T2.
- **The Celebrations setting gates every T2 and T3 everywhere:**
  - Quiet: T1 plus the words;
  - Off: words only.

  Today only the repair ending and rhythm read `CelebrationMode`. Practice finish (`finish_ceremony.dart`), the result reveal, the onboarding seal and the submit receipt must read it too (build item P0-6).
- Tap anywhere skips a moment to its end state. A moment never hides its result (brief section 10).

### 1.3 Mobi's role (Duo-like presence, not a show)

- **One Mobi per screen.** A sheet over a screen may bring its own Mobi; the one underneath hushes and looks at the sheet.
- **He is present at human moments and absent from work:**
  - never in the runner, repair run, NTA, lists or settings rows;
  - on the submit page only after the server holds the sheet.
- **He speaks at most once per screen per app run.** Lines type at about 30 ms a character (`MobiTyping`). He never speaks while a moment's number is landing.
- **He acts after the state lands, never before it.** Cheer starts when the number has landed; he never cheers in anticipation.
- **Nudge (point at the action):**
  - only after 4 s with no touch and no scroll (today it is 1.2 s on Today's header, which reads as nagging);
  - once per screen per day.
- **Glancing at taps** (`watchTaps`): at most one glance every 2.5 s. On input-heavy screens (practice setup, onboarding pickers) pass `watchTaps: false`, and the screen glances on purpose at the thing that changed.
- **Night (11 PM to 5 AM):** sleepy or asleep entrance (exists). A tap wakes him (exists).
- **Reduced motion:** key poses only, no ticker (exists).

### 1.4 Daylight (his "light/dark inconsistencies")

Every light event needs a Daylight form, decided once, not per screen:
- **Sweeps:** a 14% volt band at the same speed. A lamp-amber or white sweep is invisible on paper `#F3EFE6` / raised `#FFFDF8`.
- **Glows and blooms:** none in Daylight. Use a 1 dp `#526700` edge instead.
- **Volt washes behind a chosen row or tile:** 9% on Night, 16% on Daylight. At 9% on paper the runner's chosen-row wash disappears.
- **Particles, shards, foil and ink:** volt fill with a 1 dp `#526700` rim on Daylight, so they read on paper.
- **Ink that sits on an icon or text** (the bar bubble, the onboarding bubble): opaque, never a translucent volt over grey. A translucent volt over an icon is what makes the olive mud in the bar frames.
- **Theme switch (Appearance):** today `MaterialApp` lerps the theme for 200 ms, so painters and cached pictures show muddy mid-states. Replace it with a deliberate cross-fade:
  - snapshot the frame;
  - swap the theme with `themeAnimationDuration: Duration.zero`;
  - fade the snapshot out over 250 ms on glide;
  - under reduced motion, make it instant.

Every motion golden is rendered in both themes. That is mostly true already; the runner `motion_*` goldens are Night only.

### 1.5 Reduced motion (system "Remove animations" or the in-app switch)

`Motion.reduced(context)` everywhere:
- movements become instant or a 120 ms fade;
- an unfold, flip or morph becomes a 200 ms cross-fade;
- numbers show their final value;
- particles, sweeps and flights are off;
- Mobi holds a still pose;
- haptics are unchanged.

The same information is always present in text. Each screen entry below states its fallback only where it differs from this.

A size animation is never given a zero duration: `AnimatedSize` with `Duration.zero` re-dirties its own layout and asserts in debug. Use `MmSizeEase` (`core/motion/size_ease.dart`), which is the child itself under reduced motion or a zero duration, and pass it the same `Motion.of(context, d)` duration.

### 1.6 Haptics (one map; the Touch feedback switch turns all of them off)

| Verb | Use |
| --- | --- |
| `selection` | tab change, scrub crossing, option, chip, length stop, accordion, recap card snap, drag thresholds, the first press of a tile that opens something |
| `light` | Start, a primary commit (Begin, Submit, Start now), the plan flip |
| `medium` | the seal landing, the unfold opening, the finish stamp |
| `success` | only after the server acknowledged: submission received, repair recorded, practice recorded, week met, milestone |

Changes to what exists:
- Onboarding's `light()` on every inked sheet bubble (`onboarding_flow.dart:212`) becomes `selection`. Seven light impacts in two minutes is a buzz on a budget motor.
- Sheet opening: the haptics doc maps it to `open()` (medium). Drop it: the tap that opened the sheet already ticked.
- The repair ending's per-ring selection ticks (up to 6) are capped at 3.
- Nothing ever fires on a wrong answer or an error. No sound anywhere: none exists in the app and none is added.

### 1.7 Budget phone (Galaxy M06, Mali-G57 MC2, 90 Hz, 11.1 ms frames; the emulator is the recording device)

- Animate transform and opacity, or a `CustomPainter` with a `repaint:` listenable, inside a `RepaintBoundary`. Nothing relayouts per frame.
- At most two live blurs on screen (the bar plus one sheet or the morph), all in the shell's one `BackdropGroup`. This exists: the dock drops to Lite under a modal.
- Particles: 24 at most, one painter, seeded once.
- One controller per widget family (the map owns all its bars; the deck owns all its rows).
- Cost tags in section 4:
  - **L:** a painter or transform only;
  - **M:** several layers, or a painter that runs for more than 1 s;
  - **H:** a live blur or a full-screen layer. H needs a profile measurement before it ships.

---

## 2. Token changes (`lib/core/motion/motion.dart`)

| Change | Why |
| --- | --- |
| Add `Motion.pressedScaleFor(double width) => 1 - min(0.04, 8 / width)`. `MmPressable` uses it when no `pressedScale` is passed. | A 340 dp hero at 0.96 sinks 14 dp and reads as a bounce. Large surfaces should sink at most about 8 dp; small keys keep 0.96. |
| Add `Motion.momentT2 = 1200 ms`, `Motion.momentT3 = 2000 ms`. | Caps for 1.2. Celebrations assert against them in tests. |
| Add `Motion.handOffOut = 180 ms` on `Motion.leave`, and `Motion.handOffIn = 300 ms` on glide. | The bar and a screen's chrome leaving for a focused task, and coming back. |
| Add `Motion.drawIn = 450 ms` on emphasized. | One duration for charts, roads, bars and threads drawing in. Today they range from 520 to 620 ms. |
| Add `Springs.celebrate` (520 ms, bounce 0.22). | Only for a T3 stamp and Mobi. Nothing else may use it. |
| Keep everything else. | The vocabulary is good. The problem is adoption and rationing, not tokens. |

Kit defaults (motion-kit packet, 15 Oct), in `lib/core/motion/**` and `lib/core/widgets/**`:
- **`MmOverlapSwitcher` is the default for any keyed content swap** (a message line, a figure, a label). The outgoing layer holds until the incoming is at 0.5, then fades over 90 ms; the summed opacity never drops below 0.7, so there is no blank frame. Under reduced motion it is a short fade. Use it instead of a bare `AnimatedSwitcher`. Tests: the old words stay until the new ones land, so pump about 400 ms before expecting them gone.
- **`MmDragCommit`** follows the finger 1:1 by default. `follow` below 1 moves the child less than the finger (the recap card leans at 0.35) while thresholds count the finger's travel; `commitShare` sets the commit distance as a share of the width; `onRelease` gives an `MmDragRelease` (side, offset at release, velocity) so the next content continues the finger's motion. For the runner, recap and saved-row swipes.
- **`MmSizeEase`** for any height change (see 1.5).

---

## 3. Connective motion (app-wide transitions)

| # | Transition | Status | Choreography | Mobi, haptic, reduced, cost |
| --- | --- | --- | --- | --- |
| C1 | Tab switch | [wrong]: fade-through 90/210 ms from 0.985 scale, with no direction | Outgoing: fade out over 90 ms on exit and drift 6 dp against the travel. Incoming: from 10 dp on the side of travel, fade in over 200 ms on glide. Direction comes from the bar lens (DOCK.md 5.4). Branches stay mounted; scroll positions are kept. | Selection on the bar. Reduced: 120 ms fade. L |
| C2 | Push (a step sideways) | [works]: shared axis, 28 dp, the page below recedes 0.22 with a 0.45 scrim | Keep. Check the predictive-back partial drive on device. | L |
| C3 | Rise (focus pages: result, recap, repair ending) | [works] | Keep. You moves into the bar as a tab (DOCK.md), so its rise route goes. | L |
| C4 | Container transform (card into page) | [missing]: built (`MmTransition.container`, `captureLaunch`), used nowhere | The tapped surface grows into the page over 420 ms on emphasized. Corners open from the card's radius to 0. The card's content fades out over the first 25%; the page content fades in from 35 to 80%; the page under it recedes. Falls back to rise without a rect (deep links). Adopt at:<br>1. Today hero, into the practice start screen (the "Getting your questions ready" ticket).<br>2. A Recent papers row, into the result.<br>3. Review's tonight hero, into the repair entry.<br>4. Practice suggestion hero and mode tiles, into the setup page.<br>5. The Milestones shelf in You, into Milestones.<br>6. A recap "Show me", into the evidence sheet: a sheet, so it rises from the row instead. | Tap: the card's own haptic. Reduced: 200 ms cross-fade. M: one clip plus one fade, no blur. |
| C5 | Hero element across one navigator | [missing] | The composer ticket (setup page, root) continues as the start screen's ticket (root, same navigator): a plain `Hero` flight of 420 ms on emphasized. The subject object and length number stay put while the rest of the page changes. That is Revolut's "the input becomes the result". | L |
| C6 | Bar leaving for full-screen work | [missing] | When a root page (runner, setup, result, repair, NTA, Ask, stream) pushes, the bar translates down 24 dp and fades over `handOffOut`, driven by the shell's `secondaryAnimation`. It returns over `handOffIn` on pop. Specified in DOCK.md 5.4; this table keeps the rule app-wide. | Reduced: instant. L |
| C7 | Sheets (`MmSheet`) | [works]: 420 ms emphasized rise, the body rides in, the handle reacts to drag, a tick at the close threshold | Keep. Drop the medium haptic on open (1.6). Drag release uses the finger's velocity on `Springs.settle`; check that a fast flick closes from anywhere. | L |
| C8 | Start morph into the Start sheet | [wrong]: frames 3 and 4 of `quick_start_frames_night.png` show the sheet's text laid out at full size and clipped by the growing glass ("air the next mistake", "about 10 minutes" cut at the shape edge). The content fades in from 12% of the morph, before the glass has any shape. | Content opacity runs from 0.38 to 0.78 of the morph, scaled from 0.94 anchored at the origin. The glass, its tint and the lamp rim carry the first third alone. The text must never be visible while the shape is under 80% of its final width. Closing reverses into the key over 280 ms. The row contract is in DOCK.md 6. | The live blur (sigma 14, under 90%) stays Full-only: H, measure it. Reduced: 200 ms fade. |
| C9 | Count changes anywhere | [works]: `MonumentalNumber` rolls from the previous digits; `MmCountUp` | Adopt `MmCountUp` for the recap tallies, Insights figures and the Review open count after a repair (today only the week sheet uses it). A refresh never rolls from 0. | Selection on landing only for the screen's lead number. L |
| C10 | Pull to refresh (Today, Review, Insights, Saved, Learn) | [missing]: stock `RefreshIndicator` | Build `MmPullRefresh` in `core/motion`. Content does not move (Android clamping physics). Under the status scrim, an answer-bubble ring draws its stroke as the pull grows from 0 to 72 dp, with a selection tick at the threshold. On release the ring becomes a reading arc (one 1.2 s rotation per turn, indeterminate, words after 12 s). When data returns, the ring inks volt over 160 ms and lifts away over 200 ms; changed numbers roll from their old values and the entrance does **not** replay. On failure the ring empties and the screen's InlineBanner shows. | Reduced: a static ring and the word "Refreshing". L |
| C11 | Skeleton to content | [works]: shimmer stops after 4 sweeps; Today waits 400 ms before showing a skeleton | Swap with one 200 ms cross-fade, and the content's own entrance rides that fade (no second fade-up). A cache hit shows content at once, with no skeleton flash. | L |
| C12 | Brand opening into the first screen | [works]: about 1.28 s; tickers under it are muted until the fade, so the first screen's entrance plays as it is revealed | Keep. Optional, ask the owner: the full unfold on the first cold start of the day, a 600 ms short form (the "mo" inks, the word fades) after that. | L |

---

## 4. Screen by screen

Each entry gives the status, then:
- **Moves:** what moves and why;
- **Order:** the choreography;
- **Mobi**, **Haptics**, **Reduced** (only where it differs from 1.5) and **Cost**.

### 4.1 Cold start opening
- **Status:** [works]. The "mo" holds, blinks and inks (0 to 500 ms), unfolds into "mockmob" (500 to 1000 ms) and hands off (1000 to 1280 ms). Tap to skip. It holds without a spinner on a slow start.
- **Moves:** the brand. It answers "the app is opening" and is the only place the logo moves.
- **Order:** unchanged. The first screen's entrance must start at the hand-off (it does: ticker muting).
- **Mobi:** blinks and glances at the word (exists).
- **Haptics:** a light tap at the ink (400 ms).
- **Reduced:** the "mo" fades to the word.
- **Hand-off rule (cold-start packet, 15 Oct):** the opening never waits for data. If the first screen is known when the word is composed, it hands off straight to it. If the session is still being read, the word holds for `OpeningTimeline.authGraceMs` (300 ms) more, then hands off to the router's launch screen, which is the same word with Mobi's idle blink, so nothing moves; the first screen replaces it when known. The app's services (`_AppServices` in `lib/app.dart`) start only through `BrandOpeningHost.afterOpening`. Target on the emulator: the unfold by 1.0 s of timeline after the "mo" is on the glass, the hand-off by about 1.3 s.
- **Cost:** L. (The old `_warmUp` method is gone.)

### 4.2 Onboarding steps and the plan seal
- **Status:**
  - [works]: the step switcher, the per-answer bubble ink with a burst, the word-rise headline, the lift stagger, the sheet flip (640 ms), print rows, the hold charge with ticks, the stamp, the warm-up pace line, Mobi cues.
  - [wrong]:
    - every step uses the word-by-word headline and a burst plus a light impact per answer: the same flourish nine times in two minutes;
    - Mobi points at every new bubble.
- **Moves:** the sheet building up. Each answer visibly fills the student's sheet (state), and the plan is the payoff.
- **Order:**
  - **Every step:**
    1. The old step leaves: 12 dp up (down when going back) and fades, 200 ms on exit.
    2. The headline lifts 14 dp and fades over 340 ms on glide.
    3. The support line follows at 120 ms.
    4. The answers at 180 ms, 45 ms apart.
    5. The key at 300 ms.
  - **Word-by-word rise:** only on Welcome and the plan headline ("Week one starts with Partnership.").
  - **Answer:**
    1. The tile presses (0.97).
    2. Its tick inks in 220 ms.
    3. The sheet's bubble inks in 260 ms; its burst ring (1x to 2.4x, 520 ms) plays only on the bubble that completes a row of the sheet (stage, course, subjects, plan). Elsewhere: ink only.
    4. Weeks and sessions roll over 500 ms (exists).
  - **Plan:**
    1. Flip: 640 ms emphasized, light at the halfway point. This is a T3-class moment, so the longer duration is allowed.
    2. Rows print 160 ms apart with one selection tick each, capped at 6 ticks.
    3. Hold: 1.2 s linear charge, with ticks at a third and two thirds. Letting go drains it in 220 ms.
    4. The seal stamps on `Springs.celebrate` (420 to 520 ms) with one ring wave, plus medium.
    5. Mobi celebrates **after** the stamp lands. No sweep.
  - **First move:** the hero lands, "Your first week" lifts after it (exists), and Mobi points at Start once.
- **Mobi:** 64 to 72 dp on the sheet's top edge.
  - He says one line on arrival at a step only where the step changes something (worry, warm-up, plan).
  - On the warm-up: right answer, `correct` (1.15 s); wrong answer, `encourage`. Never a frown.
  - Elsewhere he glances at the chosen tile and does not point.
- **Haptics:** selection per choice; light at the flip; medium at the stamp; success only when Save is acknowledged.
- **Reduced:** no rise, burst or flip (200 ms cross-fade); the stamp just appears; numbers land at their final value.
- **Cost:** L. One ticker per step entrance; the headline words come from one cached layout.

### 4.3 Today: open, scroll, pull
- **Status:**
  - [works]:
    - `TodayEnter`: header 0 ms, week 60, hero 120 (20 dp rise), sections 200 to 300; 760 ms total, once per page life;
    - `TodayReveal` draw-ins below the fold;
    - `MmParallax` on the hero art;
    - the week bubbles ink;
    - the hero number rolls;
    - the header Mobi points, then nudges.
  - [wrong]:
    - the hero object glides in from 24 dp right at 0.92 over 600 ms. That is over the UI ceiling, and it travels across the very corner the owner flagged ("calculator papers... stuck at the top... I don't know if it's an entry issue"). The art must arrive where it rests. The resting position itself is the spacing fixer's job: anchor the object to the subject-and-number block, not to the card's top corner.
    - The road draw-in takes 620 ms and the college picks 520 ms.
    - The nudge comes after 1.2 s.
    - The sticky move bar cross-fades in at 140 ms on `easeOut` as a second floating thing above the bar (see 5).
  - [missing]: pull to refresh (C10), and a press response on the hero card itself.
- **Moves:**
  - the hero (the one move tonight) leads, because it is the decision;
  - the week fills to show progress;
  - the road and colleges draw because they are quantities.
- **Order on open:**
  1. Header at 0 ms: the greeting and date fade over 200 ms, no rise.
  2. Week at 60 ms: the rail ink draws Monday to today (420 ms emphasized); counted bubbles ink 50 ms apart.
  3. Hero at 120 ms: rises 16 dp and fades (420 ms emphasized).
     - The object scales 0.94 to 1 about its own centre and rises 8 dp (420 ms, starting at 160 ms). No sideways travel.
     - The number rolls (500 ms, landing at about 640 ms) with a selection tick on landing.
     - The meaning, evidence and keys fade up 8 dp at 220 and 280 ms.
     - The top-edge light sweep (700 ms) runs once per app run, after the number lands.
  4. Sections at 220 and 280 ms (exists).
- **Below the fold:** each section draws once when its top edge is 72 dp into the viewport, over `Motion.drawIn` (450 ms):
  - Recent papers: the spine bars run in from the left;
  - the road: travelled ink to Now, the bracket to the next stop, the pill fades over the last 45%;
  - colleges: the spread inks, then the picks rise 8 dp, 45 ms apart.
- **Hero press:** sinks per `pressedScaleFor` (about 0.976 at 340 dp), with the veil.
  - On release the length chip and key behave as now.
  - Tapping the key: light haptic, then the container transform (C4) into the start screen.
- **Scroll:** the hero art parallaxes (factor 0.18, exists). Nothing else moves while scrolling. The bar collapses per DOCK.md.
- **Mobi:** the header Mobi is the only Mobi.
  - Entrance by time of day (sleepy at night).
  - He points at the hero key once it has landed.
  - Nudge per 1.3 (4 s, once a day).
  - He says his line once per app run.
  - Day one and returning states: the stage's own Mobi replaces the header one (one per screen).
- **Haptics:** selection on the number landing and on length chips; light on Start.
- **Reduced:** all in place on the first frame; sections drawn complete.
- **Cost:** L. One entrance controller; painters cache paths per size.

### 4.4 Quick start (the Start key and its sheet)
- **Status:**
  - [works]: the key press (0.9 disc) with the ink ring spread (380 ms); the deck (lead, pairs, wide, quiet); the route-driven row stagger (45 ms); the lead glyph's gesture once, 260 ms after landing; Mobi thinks, then points at the lead row.
  - [wrong]:
    - the morph text clipping (C8);
    - the breath (removed by DOCK.md);
    - Mobi plays two acts and a press-glance on a sheet that is open for about 2 s;
    - a choice's glyph gesture is 640 ms.
- **Moves:** the key becomes the sheet (where it came from), and the recommended row leads.
- **Order:**
  1. Press with the ink ring.
  2. Morph over 420 ms. The glass carries the first third alone; the content arrives over 0.38 to 0.78.
  3. Rows stagger 45 ms apart from 160 ms.
  4. The lead row's glyph plays once (420 ms, trimmed from 640) when the stagger reaches it.
  5. Mobi points at the lead row once it is laid out. He does not think first.
- **Choosing a row:**
  1. The tile presses (0.97), with selection.
  2. The sheet leaves downward over 200 ms on exit while the next page pushes. A choice that opens setup uses C4 from the tile.
- **Dismiss:** drag with velocity, scrim tap or back reverses the morph into the key (280 ms).
- **Mobi:** 64 dp, a point only. No line unless resuming ("23 of 50. Pick up where you left off." once).
- **Haptics:** light on the key; selection on a row.
- **Reduced:** 200 ms fade; no glyph gestures.
- **Cost:** H during the morph (one live blur that is gone by 90%). Measure it.

### 4.5 Practice setup (tab, composer, length dial, start screen)
- **Status:**
  - [works]:
    - subject tiles lift 4 dp with the object at 1.06;
    - the "Practising in" line cross-fades over 200 ms;
    - the mode deck with glyph gestures;
    - the ticket header with the rolling length;
    - the subject swap slide (300 ms);
    - the length dial thumb glides on emphasized, its bubbles ink 18 ms apart, scrub ticks;
    - the start screen ticket rises under Mobi.
  - [wrong]: glyph gestures run 640 ms on every press (decorative and long).
  - [missing]: the container transform from mode tiles (C4) and the ticket hero into the start screen (C5).
- **Moves:**
  - the chosen subject and length are seen, which answers his "it's just redirecting me to the accounting page";
  - the paper size of the chosen length is shown in bubbles.
- **Order:**
  - **Tab entrance (route stagger):** suggestion hero, then "Choose your own", then subject tiles (45 ms apart), then the mode deck.
  - **Choosing a subject:**
    1. The tile lifts 4 dp on `Springs.smooth` and its bubble inks (220 ms).
    2. The previous tile settles back.
    3. The subject line cross-fades.
    4. If a ticket is visible, its object slides out 12 dp and fades over 150 ms while the new one slides in over 300 ms on glide.
  - **Length:** the thumb glides (300 ms emphasized), bubbles ink 18 ms apart, the number rolls (300 ms), selection per stop.
  - **Mode press:** the glyph gesture runs 420 ms and only on the pressed tile.
  - **Start:** light haptic; the ticket flies (C5); the start screen's "Getting your questions ready" sits under the ticket with Mobi in `loading` until the session exists, then a 200 ms fade into the runner.
- **Mobi:** absent on the tab and the composer (work). On the start screen he is `loading`; after 8 s the words change ("Still fetching. This sometimes takes a moment on slow networks.").
- **Haptics:** selection on subject and stop; light on Start.
- **Reduced:** no lift or slide, values swap; no ticket flight.
- **Cost:** L. Emblems stay static here (`animate: false`).

### 4.6 Runner: answer select, next, palette
- **Status:**
  - [works]:
    - the lock-in: row press 0.985, the bubble inks from the touch point (260 ms), the volt wash bleeds across the row (320 ms), the other rows go to ink 2;
    - `LockFlight`;
    - the track ring glides (360 ms spring) and cells spark then cool;
    - marked notches;
    - the count flip (180 ms, direction-aware);
    - `QuestionEnter` (260 ms, options 35 ms apart from the side of travel);
    - the palette wave (12 ms per cell, capped at 420 ms);
    - the half and complete track sweeps;
    - the timer's five-minute bar.
  - [wrong]:
    - the flight's five-dot comet tail crosses the question text (`motion_lock_in_mid.png`), on every answer, in timed mocks too. That is the over-gamified end in the one place the student concentrates.
    - The wash at 9% vanishes in Daylight (1.4).
- **Moves:**
  - the chosen answer becoming a mark on the sheet (state);
  - the ring travelling the sheet (where you are);
  - nothing else.
- **Order:**
  - **Select:**
    1. Tap; the bubble inks over 260 ms.
    2. The wash reaches the far corner over 320 ms.
    3. In practice: a single 6 dp volt dot flies to the track cell over 240 ms on glide, with **no tail**, on a path kept left of the text column (bubble x, then up the gutter). The cell sparks and cools (220 + 420 ms).
    4. In a timed Full mock: **no flight**. The cell inks directly as the wash finishes.
  - **Next:**
    1. The count flips (180 ms).
    2. The ring glides on the 360 ms spring.
    3. The question text rises 10 dp and fades over 260 ms; options follow 35 ms apart from the side of travel.
    4. Scroll resets.
    5. Rapid taps cancel and restart from the current values; nothing queues.
  - **Mark:** the flag pops 0.8 to 1 on snappy; the track notch appears at once.
  - **Palette:** the sheet rises (C7) with the cell wave. "Go to question 9" is the only key with emphasis.
  - **Timer:** never moves. Under 5:00 the bar drains in real time; colour changes at 1:00. No pulse.
- **Mobi:** never here.
- **Haptics:** selection on select, jump, track tap and palette cell. Nothing on Next, Previous or mark.
- **Reduced:** instant; the track cell inks with no spark.
- **Cost:** L. Must hold 6 ms raster p90 (feasibility 12); no blur.

### 4.7 Submit and the finish moments
- **Status:**
  - [works]:
    - submit sending: the lamp band passes the bubbles, about 1.4 s a pass;
    - received: bubbles ink volt in order (900 ms), the success haptic at the ink's start, Mobi hops in a fixed slot, the receipt slides in, hand-off at 2.8 s or a tap;
    - practice finish: bubbles ink 40 ms apart, the figure counts, the stamp (1.14 to 1), a ring;
    - good set: shards, a sweep, Mobi;
    - Finish for now: the filed sheet, the check ring (420 ms), the receipt engraves, about 1.6 s.
  - [wrong]:
    - the good-set practice finish stacks a stamp, two rings, 24 shards, a volt flash, a sweep, Mobi and success: five channels, against a T2 cap of three;
    - none of it reads the Celebrations setting.
- **Moves:** the hand-in becoming the receipt (the sheet turns volt only when the server holds it), and the result arriving.
- **Order:**
  - **Submit received:** keep as is. It is the model T2: ink, Mobi hop, receipt.
  - **Practice finish, good or great (T2):**
    1. 0 to 200 ms: the sheet is in place.
    2. 200 to 1000 ms: bubbles ink 40 ms apart and the figure counts.
    3. At 1000 ms: the stamp (1.12 to 1, 420 ms emphasized) plus one ink ring, then medium.
    4. Shards: 14, 600 ms, from the figure. They replace the sweep and the flash; there is no second ring.
    5. At about 1200 ms: Mobi cheers. Then success (after the ack, already true on a fresh open).
  - **Mixed or low set:** the stamp only, no shards, Mobi `read` or `encourage` with one factual line.
  - **Finish for now:** keep.
- **Mobi:** one per screen, after the number lands.
- **Haptics:** medium at the stamp; success after the ack.
- **Reduced:** end state at once. Quiet: stamp only, no particles. Off: words.
- **Cost:** M (particles for 600 ms, one painter).

### 4.8 Result: recap cards
- **Status:**
  - [works]:
    - card 1: the arrival (28 dp rise, -1.5 to 0 degrees, 560 ms), the engraved headline, the drag unfold with threshold ticks, the reader line (900 ms) inking row by row, the tally counting what has inked, the figure roll, the marks meter, the sweep, Mobi reads, then cheers only for a higher result;
    - card 2: the flow (column 300 ms, ribbons 90 ms apart, 500 ms each);
    - card 3: Mobi thinks, then points;
    - between cards: rise 40 / sink 0.96, story bar fill, a selection tick on snap;
    - blocks within a card at a 55 ms stagger.
  - [wrong]:
    - the sweep plays after every reveal, not only higher results;
    - the meter takes 600 ms;
    - ribbons are 500 ms each (about 1060 ms for card 2);
    - the builder notes the reveal ink and tally are unverified on a device.
- **Moves:** the marking itself (the read is the OMR machine), then where the marks went. This is the app's signature moment and may be the longest.
- **Order, card 1:**
  1. Arrival (560 ms, a moment).
  2. Unfold by drag or tap.
  3. Read (900 ms).
  4. The figure rolls (500 ms) and the meter fills over 420 ms.
  5. If higher than the last comparable mock: the sweep (700 ms) and Mobi cheers. Otherwise Mobi stays reading.

  That is T2. The first full mock is a milestone and goes through the rhythm controller as a dated row, never a score celebration.
- **Order, card 2:** the column grows (300 ms), then ribbons draw at a 70 ms stagger, 420 ms each (about 700 ms in total), with labels rising 12 dp as each ribbon arrives.
- **Cards 3 and 4:** blocks at a 45 ms stagger. Card 3 has the cost figure roll and the strip tiles; Mobi points once.
- **Mobi:** one per card, at most one act per card.
- **Haptics:**
  - light on tap-open;
  - selection at the 25/50/75% drag thresholds;
  - medium when the sheet opens;
  - nothing during the read;
  - selection on each card snap.
- **Reduced:** the sheet is complete (200 ms fade) and figures are final.
- **Cost:** M. The read line repaints only its own layer.

### 4.9 Review and repair stages
- **Status:**
  - [works]:
    - the tonight hero art settles (420 ms) and the number rolls;
    - the map bars grow from the left (520 ms, 60 ms stagger);
    - the accordion opens over 320 ms emphasized and closes over 200 ms, with the chevron turning;
    - repair run: the run track fills over 420 ms with a light tick;
    - the stage thread: Found, a 160 ms delay, then the line draws to Repaired and the bubble inks (260 ms);
    - the repair ending choreography (`motion_repair_ending_t*`).
  - [wrong]:
    - the ending stacks rings with up to 6 ticks, two shock rings, 14 flecks, a bloom, a roll, Mobi cheering, the thread and a lamp sweep;
    - the bars run 520 ms.
- **Moves:**
  - the thread (Found, Repaired, Checked, Holds) is the one thing in the work layer that moves with weight, because a stage completing is the product's promise;
  - bars compare chapters;
  - the ending is a T2.
- **Order, Review tab (route stagger):**
  1. The tonight hero: the art settles (scale 0.94 to 1, rise 8 dp, 420 ms) and the number rolls.
  2. The map heading.
  3. Bars draw in over 420 ms at a 45 ms stagger, once.
  4. Accordion: one chapter open at a time. The opening chapter lifts onto `raised`, and its thread rows fade in at 30 ms apart. Selection haptic.
- **Repair entry:** C4 from the tonight hero. The number lands, then Begin is live at once.
- **Repair run:** the explanation lands. The thread draws Found to Repaired (160 ms delay plus 260 ms ink), a light tick when the server acknowledges the step, and the run track segment fills (420 ms). The explanation text never moves.
- **Repair ending (T2):**
  1. 0 ms: the handed-back sheet rises 12 dp (320 ms).
  2. 320 ms: rings draw on the repaired bubbles, 1100 ms in total, at most 3 ticks.
  3. Then the number rolls (500 ms), the burst plays (two rings and 14 flecks, 900 ms) **with no bloom and no sweep**, and the thread draws to Repaired (420 ms).
  4. Mobi cheers after the number lands.
  5. Success after the ack (already true).
  6. The keys and receipt are still from the first frame.
  7. A repair that holds a milestone goes through the rhythm controller as T3, without a second burst.
- **Mobi:**
  - the hero: points at Repair once, or sleepy at night;
  - the ending: cheers;
  - nothing in the run.
- **Haptics:** selection on the accordion; light on Begin; a light tick per acknowledged step; success at the end.
- **Reduced:** all at rest; no burst or ticks.
- **Cost:** L for the map; M for the ending (particles seeded once).

### 4.10 Ask Mobi
- **Status:**
  - [works]: the empty stage (Mobi `hello` at 132 dp, the line types in, eyebrows, tiles rise at a 60 ms stagger); the student bubble slides 10 dp over 240 ms; pending bubbles ink in sequence; the reply reveals word by word (18 ms a word, capped at 900 ms); the header Mobi thinks while pending, talks when the reply lands; the send disc scales in.
  - [wrong]:
    - follow-ups rise 200 ms apart (slow; it reads as lag);
    - pending loops with no 12 s fallback words;
    - the stage `hello` plays on every open.
- **Moves:** the conversation (state); Mobi as the one answering.
- **Order:**
  - **Empty stage:**
    1. Mobi `hello` on the first open of the day; idle after that.
    2. The line types in.
    3. Tiles at a 45 ms stagger from 380 ms.
  - **Send:**
    1. Light haptic.
    2. P2: the typed text morphs from the composer into the student bubble (Revolut: the input becomes the message) over 300 ms on emphasized. Until then, a 10 dp slide.
    3. Mobi goes to `loading`.
    4. The pending bubble appears at 120 ms.
    5. After 12 s: "Still thinking. Long questions take a little longer."
  - **Reply:**
    1. Word reveal.
    2. The source strip, actions and follow-ups rise at a 60 ms stagger.
    3. Mobi talks, then goes idle.
    4. Light haptic when a model reply lands.
- **Mobi:** the header Mobi; the stage Mobi on empty only.
- **Haptics:** selection on a prompt; light on send and on a model reply.
- **Reduced:** replies appear whole.
- **Cost:** L. The word reveal is a clip on one paragraph, not per-word widgets.

### 4.11 Insights (Your record) charts
- **Status:**
  - [works per spec, unverified]:
    - the hero ledger bubbles ink in reading order (700 ms);
    - the trend draws in (600 ms);
    - ranked bars grow at a 70 ms stagger;
    - the split and pace bars;
    - week rows.
  - [wrong]: every section fades up 16 dp as it is built. That is the identical fade-up on every section that the standards forbid (T-024), and it re-reads as motion while scrolling.
- **Moves:** the data drawing itself (the chart is the state); nothing decorative.
- **Order:**
  1. The hero ledger ink (700 ms). This is the screen's one entrance, a moment-layer hero.
  2. Below it, sections are simply there.
  3. Each **chart** draws once when 72 dp into the viewport, over `Motion.drawIn` (450 ms): the trend line draws left to right and the latest point's halo blooms over the last 30%; bars use a 45 ms stagger.
  4. Text and section headings never animate.
  5. Tap a point: selection, the note cross-fades over 150 ms, and the point's ring grows 1 to 1.3 over 150 ms.
- **Mobi:** none on the record. On the empty state only (`read`).
- **Haptics:** selection on a chart point or chip.
- **Reduced:** drawn complete.
- **Cost:** L. Painters per chart; `RefreshIndicator` becomes C10.

### 4.12 Rhythm and milestones
- **Status:** [works]:
  - WeekDial: a 160 ms lead, then 300 ms per segment, 110 ms apart. A met week gets a 700 ms sweep round the ring and a soft glow.
  - RunRibbon: capsules grow 40 ms apart over 360 ms.
  - Medal moment: settles from 0.92 with a light band over 500 ms, Mobi hops.
  - The milestone trail draws over 400 ms.
  - The celebration controller with L1 to L3 and CelebrationMode.

  This is the most complete area. It sets the pattern the others copy for gating.
- **Moves:** progress through the week (state) and milestones landing (T3, rare).
- **Order:**
  - Dial segments ink in order with no tick per segment. A met week is T2: the sweep only, then Mobi cheers beside the dial.
  - A milestone that landed since the last visit is T3, played once: the medal settles on `Springs.celebrate`, the light band crosses it, Mobi is `proud`, then success.
  - A milestone that landed more than 48 h ago is a quiet receipt row (exists).
- **Daylight:** the glow becomes the `#526700` edge, and the sweep a volt band (1.4).
- **Mobi:** at the ends only (exists).
- **Haptics:** selection on a day or ribbon week; success after the ack for the week met.
- **Reduced:** drawn settled.
- **Cost:** L.

### 4.13 You
- **Status:**
  - [works]: the `MmStagger` entrance (5 blocks, 60 ms); Mobi 120 waving; the week dial at 104 dp; row press veils.
  - [wrong]:
    - Mobi waves `hello` on every open;
    - You rises as a root page. It becomes the fourth tab (DOCK.md), so it arrives by C1 like the others.
  - [missing]:
    - the token shelf's newly landed token does not play its moment here (Milestones does);
    - the theme switch cross-fade (1.4).
- **Moves:** identity first (the student's sheet); settings are still.
- **Order:**
  1. The name and Mobi at 0 ms.
  2. The week pane at 60 ms, with the dial filling.
  3. The sheet block at 120 ms.
  4. The shelf at 180 ms.
  5. Settings at 240 ms.
  6. Rows below are simply there.
  - The Milestones shelf opens Milestones via C4.
- **Mobi:** `hello` only on the first open of the day, idle after that; a tap gives a boop (exists).
- **Haptics:** selection on rows; settle (light) on saving a goal; success only after the ack.
- **Reduced:** instant.
- **Cost:** L.

### 4.14 Sheets and dialogs
- **Status:** [works] (C7): the rise, body ride-in, handle widening 36 to 52 dp, threshold tick, scrim. The leave guard enters on emphasized.
- **Moves:** sheets rise over the content instead of replacing it (FamApp).
- **Order:** the glass first, then the body over the last two thirds. Rows inside a sheet stagger only if the sheet is a menu (Start, alternatives, evidence), at 45 ms apart.
- **Haptics:** none on open (1.6); selection at the drag threshold.
- **Cost:** H only for the morph; normal sheets are fake glass or a single grouped blur (as now).

### 4.15 Empty, loading, error, offline
- **Status:**
  - [works]: `StateView` (Mobi settles, then the title, message and action at 45 ms apart; Mobi looks at the action); skeleton shimmer (4 sweeps, then still); Today's 400 ms skeleton delay; Mobi `oops` on a setback.
  - [wrong]: Mobi plays `oops` again on every retry failure.
  - [missing]: the retry key's own loading state and the success hand-back.
- **Moves:** what is happening (loading, failed, offline) and the one way forward.
- **Order:**
  - **Loading:** nothing for 400 ms, then the skeleton with shimmer. After 8 s the skeleton stills and a line says what is slow.
  - **Error:**
    1. Mobi `oops` the first time only; after that, idle.
    2. The text and the Try again key.
    3. Retry: the key shows an inline reading arc (the C10 ring at 20 dp) and does not move the layout.
    4. On success: a 200 ms cross-fade to the content, whose entrance rides the fade (C11).
  - **Offline:** the banner slides down 8 dp and fades over 200 ms; it is not sticky motion.
- **Mobi:** one per state view: `rest` for all clear, `read` for empty, `oops` once on a failure, `sleep` at night.
- **Haptics:** none (nothing on errors).
- **Reduced:** static.
- **Cost:** L.

### 4.16 The bar
DOCK.md owns it. Its motion (lens travel with anticipation, ink at 70% of travel, icon departure, direction-aware content switch, collapse and expand, the capsule, the Start morph, leaving for pushed pages, the keyboard, badges) matches this spec's tokens and rules, and section 5 adds the cross-app points.

---

## 5. The bar: what this spec adds to DOCK.md

1. **One floating thing above the bar at a time.** Today has a `StickyMoveBar` (`move_keys.dart`, a 140 ms cross-fade) that floats "Start repair, 15 min" above the bar when the hero's key scrolls away. DOCK.md's live capsule sits in the same place, 8 dp above the bar. They will stack. Resolve it in one of two ways:
   - **Recommended:** retire `StickyMoveBar` and make "Tonight's move" the capsule's **lowest-priority** state, shown only on Today, only while the hero key is off-screen and no higher state applies.
     - Text: the move ("Accountancy repair, 15 min"). Action: "Start".
     - It enters with DOCK.md's "Capsule in" motion and leaves when the hero key returns to view.
     - One object, one motion vocabulary, and the bar visibly "knows tonight's move".
   - **Alternative:** keep the sticky bar but hide it whenever the capsule shows.
2. **The ink must be opaque and land with the lens.** DOCK.md 5.4 already says this (ink starts at 70% of travel, the bubble is built into the icon). The acceptance check is the 40 ms frame of the new `bar_travel_*` golden: no volt may show on the target icon before the lens's leading edge passes 70%.
3. **The bar's first appearance (DOCK.md: rise 16 dp, a 30 ms stagger, the Start pop) must not overlap the Today entrance.** Run the bar at hand-off and the Today header from 0 ms; both are under 450 ms and touch different regions, so they may run together. The rule is that the bar never pops while the hero number is landing (about 640 ms). Start the pop at 300 ms or earlier.
4. **Collapse and expand never fire from programmatic scrolls:** the tab reselect scroll-to-top and the accordion auto-scroll. They fire only on user-drag (`UserScrollNotification`), as now.

---

## 6. Prioritised build list

Each item gives its area, the files, and what "done" means. Every item's acceptance includes the recording check in section 7, in both themes.

### P0: what makes it feel different in use (do first)

| # | Item | Area and files | Done means |
| --- | --- | --- | --- |
| P0-1 | **The bar** per DOCK.md, with the section 5 additions (the capsule absorbs the sticky move) | foundation: `core/widgets/dock` to `bar`, `app_shell.dart`, `router.dart`; Today: `move_keys.dart`, `today_body.dart` | DOCK.md 9.3; one floating object above the bar at any time; the ink-timing frame check |
| P0-2 | **Container transform adopted** (C4) at the six places, plus **the ticket Hero** (C5) | Today `move_hero.dart` and `sheet_section.dart`; Review `tonight_card.dart`; Practice `suggestion_hero.dart`, `choice_deck.dart`, the setup and start screens; `router.dart` transitions for the targets | Recording: a card visibly grows into its page and back; the fallback without a rect is a rise; predictive back scrubs it |
| P0-3 | **Tab switch with direction** (C1) and **the bar leaving for full-screen work** (C6) | foundation: `transitions.dart` (`FadingBranchContainer`), the shell | Recording: content slides with the lens; the bar exits before the runner arrives and returns on pop |
| P0-4 | **`MmPullRefresh`** (C10) on Today, Review, Insights, Saved and Learn | foundation: new `core/motion/pull_refresh.dart`; features swap `RefreshIndicator` | No stock spinner anywhere (`grep RefreshIndicator lib` is empty); numbers roll from their old values; no entrance replay |
| P0-5 | **Ration the moments**: practice finish to T2 (14 shards, no sweep or flash, one ring); repair ending without bloom or sweep, ticks capped at 3; result sweep only for a higher result; onboarding burst only on row-completing bubbles, light to selection | Practice `finish_ceremony.dart`, `finish_stage.dart`; Review `repair_ending_screen.dart`; Result `sheet/*`; Onboarding `onboarding_flow.dart`, step widgets | A count of simultaneous channels is three or fewer in each `motion_*` frame sheet; tests assert `Motion.momentT2/T3` caps |
| P0-6 | **The Celebrations setting everywhere** (Full, Quiet, Off) | Practice, Result, Onboarding (seal), Runner (receipt); read `rhythmPrefsProvider` | Unit tests: Quiet gives no particles or sweeps, Off gives words only, for each moment |
| P0-7 | **Runner lock-in calmed**: no tail; flight in practice only, kept to the gutter; none in timed mocks; Daylight wash at 16% | Runner `lock_flight.dart`, `answer_option.dart`, `runner_layout.dart` | `motion_lock_in_mid` re-rendered in practice and mock, both themes; no pixel of the flight over the question text box |
| P0-8 | **Start morph content timing** (C8) | foundation: `morph_sheet_route.dart` | Re-render `quick_start_frames_*`: no text visible while the shape is under 80% of its width |
| P0-9 | **The Today hero arrives where it rests**: the object scales about its own centre (no 24 dp travel, 420 ms); the road and colleges draw at 450 ms; Mobi nudge at 4 s, once a day | Today `hero_stage.dart`, `today_reveal.dart`, `road_timeline.dart`, `college_ladder.dart`, `header_mobi.dart` | Frame sheet of the Today open at 0, 120, 300, 640 and 900 ms (new golden); the art never sits away from its rest position after 420 ms |

### P1: finish and consistency

| # | Item | Area | Done means |
| --- | --- | --- | --- |
| P1-1 | Daylight forms for every light event (1.4): sweeps as a volt band, no glows, rims on particles, opaque inks | all moment owners; a shared `MmLight.sweepColor(context)` etc. in `core/motion` | Day goldens for every `motion_*` sheet; the runner's `motion_*` gains `_day` |
| P1-2 | Theme switch cross-fade (1.4) | foundation `app.dart`, Appearance | Recording: Night to Day with no muddy mid-frames |
| P1-3 | `pressedScaleFor(width)` default in `MmPressable` | foundation `pressable.dart` | The hero sinks 8 dp or less; keys unchanged |
| P1-4 | Mobi discipline (1.3): one per screen, `hello` once a day (You, Ask), glance throttle of 2.5 s, `oops` once per failure run, no think-before-point on the Start sheet | mascot `mobi_character.dart` (throttle); features as listed | Unit tests on the throttle and the once-per-day gates |
| P1-5 | Insights: remove the per-section fade-ups; charts draw once at 450 ms; point tap ring | Insights widgets | Scrolling the record shows no text motion |
| P1-6 | Trims to `Motion.drawIn` and the stagger: Review bars 420/45, result meter 420, card 2 ribbons 420/70, Ask follow-ups 60 ms, practice glyph 420 ms on the pressed tile only | Review, Result, Ask, Practice | `grep` for durations above 450 ms outside moments; each remaining one is on the moment list |
| P1-7 | 12 s words on every indeterminate wait (submit sending, Ask pending, start screen, pull refresh, retry) | Runner, Ask, Practice, core | Fake-clock tests reach the words |
| P1-8 | `MmCountUp` for recap tallies, Review's open count after a repair, Insights figures | Result, Review, Insights | Values roll from old to new, never from 0 |
| P1-9 | Haptic map fixes (1.6): onboarding ink to selection, no medium on sheet open | Onboarding, foundation `haptics.dart` docs and `mm_sheet.dart` | Haptic counter tests updated |

### P2: delight, only after P0 and P1 are watched on a recording

| # | Item | Area |
| --- | --- | --- |
| P2-1 | Ask: the composer text morphs into the student bubble | Insights/Ask |
| P2-2 | A short brand opening after the first cold start of the day (C12). Ask the owner first: he has not complained about the opening. | foundation brand |
| P2-3 | Start press-and-slide (DOCK.md 5.2 P1) | foundation |
| P2-4 | A collapsing title on Practice and Review roots (`MmCollapsingTitle`, built and unused) | Practice, Review |
| P2-5 | Subject emblem idle (`animate: true`) only on the chosen subject tile in Practice, never in lists | Practice |

---

## 7. How to prove it (stills cannot)

1. **Recordings are the deliverable.** On the emulator (the owner's 13 Oct rule; keep its RAM at 2 to 3 GB), use a profile build and `adb shell screenrecord --bit-rate 8M` for each journey:
   - cold start to Today;
   - tab taps and a scrub;
   - the Today pull;
   - Start, the sheet and a choice;
   - the practice setup and start;
   - five runner answers with Next and Previous mashed;
   - submit and finish;
   - the result reveal and all four cards;
   - Review accordion, repair, ending;
   - Ask, one prompt;
   - Insights scroll;
   - You and the theme switch;
   - an error with a retry.

   Record each once in Night and once in Daylight, and once with Remove animations on. Watch them at 0.25x speed (extract frames with `ffmpeg -vf fps=30` into a contact sheet) and check against sections 1 and 4. **Send the owner the recordings, not stills**: that is what he asked to judge.
2. **Frame-sheet goldens** (`test/golden/core/frame_sequence.dart`) for every new choreography: the Today open, the bar travel, the morph, the pull, C4 per site, the practice finish T2, the repair ending, in both themes.
3. **Timing.** The emulator says nothing about M06 frame cost. When a phone is connected, use a profile build with DevTools or `TimelineSummary` on the H and M items (the morph, the bar blur with the capsule, the result read, the endings, scrolling Today). Targets: raster p90 at or under 8 ms (6 ms for the runner and repair), and missed frames at or under 5% in transitions. Say plainly which numbers came from the emulator and which from a phone.
4. **The done check against the owner's standards:**
   - every animation answers an action or shows a state;
   - one entrance per screen;
   - no loops on a resting screen;
   - reduced motion keeps the information;
   - the slop list (no scale-from-0, no ease-in on UI, no infinite loops on components, no confetti without a real outcome).
