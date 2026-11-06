## id

clarity

## title

Clarity-first home page: "CUET 2027 mock tests for [subject]", with Mobi handing you the first question on every screen size

## thesis

On a phone, a student should understand the offer in one glance, before any decoration. Today the painted room and the bar fill 45% of the screen before the H1 starts (audit, LK70), and no sentence says what MockMob is. In this proposal the first screen reads, top to bottom:
1. What it is: "CUET 2027 mock tests for Accountancy", with the subject typed in.
2. Why us, in one true sentence: every mock is fresh from one bank of 5,765 questions, then MockMob shows where each mark went and why.
3. What to tap: "Try five questions".
4. Mobi standing on the live first question, which he hands you.

That stage (the painted room cropped to a 212 px band, Mobi with his feet on the top edge of the sample card, a task-tied bubble) is the same idea at 390 and at 1440. This closes the parity gap in LK67 without cutting the room, Mobi or the sample.

The rest of the page keeps every section, story and animation (L-004, L-005). It is refined in five ways:
- Night moves to the app's warm charcoal. Volt becomes a fill only, and the lime edges, washes and glass go (LK68).
- The held stories get the one-gesture controller that was proven on the bench. All 32 of its flick cells advanced exactly one step. The page's scroll listeners are merged into one reader (LK69).
- Copy is cut to the line that matters in each block, about 3,050 words down to 2,000 or fewer (LK71).
- The exam section becomes a picture of the real MockMob runner that fits in one screen, with NTA style kept as a rehearsal switch (LK72).
- One brand system: warm tokens, a type ladder with real weight steps, Literata for questions, owned desk-object icons instead of Lucide, and one job for Mobi everywhere (LK73).

Entry gets a 1.3 s first-visit loader: the app's own "mo unfolds into mockmob" opening, which then lands in the site bar (LK74).

## hero

{
 "phone": "Layout at 390x844, measured on the mock-up:\n- Site bar: 60 px.\n- H1: 82 to 213 (top at 9.7% of the screen).\n- Lead: 229 to 304.\n- Two keys side by side: 326 to 378.\n- Trust sentence: 392 to 412.\n- Stage: room band 438 to 650. Mobi (128 px) stands at 491 to 619 with his feet on the card's top edge. The sample card starts at 620 and the question stem at 680.\nSo the student sees what MockMob is, why it is different, the primary key, Mobi and the real question on the first screen. Today the H1 starts at y 393.\n\nAt 360x640 the H1, lead and keys still fit (the keys end at about 380), and Mobi's head shows at the fold.\n\nType at 390:\n- H1: Bricolage 800, clamp(2.5rem, 11.4vw, 4.6rem) (about 44 px), line-height 0.98, tracking -0.038em. Three lines: \"CUET 2027\" in --accent-text, \"mock tests for\", then the typed subject. The slot is a CSS-grid stack with an invisible sizer holding \"Business Studies\", so the line never changes size (CLS 0).\n- Lead: Hanken 400, 17/25, max 36ch, --ink-2. The bank count is Hanken 700 tabular-nums in --ink.\n- Keys: a two-column grid with a 10 px gap. Each key is 52 px with the existing 4 px keycap edge: primary volt, secondary paper-raised with a 1 px line.\n- Trust: Hanken 500, 14/20, --ink-3, one sentence with no middle dots.\n- Hero links (\"Free DU eligibility and cutoff calculator\", \"See the real exam screen\") move below the stage on phones. They are kept, not cut.\n\nStage:\n- The room band (HeroRoom) is 212 px tall, radius 20 at the top. The image is 106% wide at -3% and bottom -22 px, so the answer-sheet poster's lower rows and the lamp's floor pool show. A 46 px paper-coloured scrim fades it into the card.\n- Mobi stands right of centre (right: 20%) with his feet 31 px above the room's foot, on the card edge.\n- The bubble sits at the top left (left 14, top 26, max 168 px), with its tail pointing at him.\n- The card overlaps the room by 30 px.",
 "desktop": "At 1440x900 the hero is a two-column grid: copy (1fr) and a 500 px stage, gap 72, max width 1240, padding 64/32, vertically centred.\n\nCopy column:\n- H1: Bricolage 800, 76/74, three lines, 208 to 431.\n- Lead: 19/28, max 38ch.\n- Keys: inline, 54 px tall, 24 px side padding.\n- Trust: 15 px.\n- Hero links: one row, ink with a --line-strong underline.\n\nStage column: the same stage as the phone.\n- Room band 262 px; the image is 108% wide at bottom -70 px, Day 132% at bottom -96.\n- Mobi is 168 px, right: 22%, standing on the card edge.\n- The bubble is at left 24, top 44, max 250 px, on one line.\n- The card overlaps by 34 px. The question stem is Literata 21 px.\n\nBelow the hero is the facts row, which replaces the glass lp-proof. It is four plain links with a 1 px --line top border and a 24 px gap: value first in Hanken 700 17 px, the label in Hanken 500 14 px --ink-3. The cells are \"5 questions / Free to try, no signup\", \"73 DU programmes / Matched to your subjects\", \"2 exam screens / Ours, and NTA style for rehearsal\" and \"60 minutes / 50 questions on the CUET clock\". On a phone it is a 2x2 grid.\n\nThe pointer spotlight, the hairline grid and the dot matrix (HeroBackdrop) are retired from the hero. They were desktop-only (slop items M7 and C6, and the L-003 parity rule), and the painted room now gives desktop its owned scene.",
 "mobi": "Mobi has one role on both widths: he is the host who hands you the first question.\n\nComponents:\n- HeroMobi merges the 'room' and 'host' variants into one variant, 'stage'. It is the same rigged vector MobiReact with its poster first frame.\n- HeroRoom renders at every width (the display:none at 761 px and up is removed).\n\nBubble lines, tied to the task and driven by demoSignal, never by taps. No exclamation marks.\n- On load: \"Your first question. No signup.\"\n- After a correct answer: \"That's the one. Read the why, then the next.\"\n- After a wrong answer: \"Close. The why shows the trap.\"\n- After question 5: \"That's five. Sign up to keep your score.\"\n\nMotion:\n- Each bubble change is a cross-fade: 180 ms opacity plus a 4 px rise, var(--ease-out), with the size held by a sizer, so it never jumps.\n- Mobi's acts follow the sample: correct plays cheer, wrong plays encourage, the next question plays point at the card.\n\nTap: one small act (hello, hop or tilt, never the same twice), at most once per 1.2 s.\n- Gone: the bubble change, the 8 ms buzz and the key lift.\n- The site-bar Mobi's wink on the first tap stays.\n- The tap animation is refined, not removed.\n\nThe Night painted answer sheet now fills one empty bubble per answered sample question, five in all. This reuses the HeroRoom BUBBLES overlay: 220 ms scale from 0.6 to 1 and opacity, var(--ease-out), 120 ms after the answer. The Day sheet is already full, so Day shows progress through the card's 5-segment bar only.\n\nIdle: the rig is capped at 30 fps and paused when the stage is off screen or the tab is hidden.\n\nThe six heroTaps.mjs pitch lines are retired. Their content now lives in text everyone reads: the bank and the fresh mock are in the lead, free and no signup in the trust sentence and the bubble, and \"try five\" in the key.\n\nOne Mobi in view (W-074) still holds. The section seats keep the baked poses (see the brand system).",
 "words": "H1 (one sentence for screen readers and search, in a visually hidden span; the visible runs are aria-hidden): \"CUET 2027 mock tests for Accountancy, Economics, Business Studies and English.\"\n\nVisible H1:\n- Line 1, in --accent-text: \"CUET 2027\".\n- Line 2: \"mock tests for\".\n- Line 3, typed: Accountancy, then Economics, then Business Studies, then English, then a rest on Accountancy. This is the commerce-first order of L-023. Every word must be in CUET_PUBLIC_ALLOWED_SUBJECTS, and a test holds that.\n\nLead: \"MockMob builds every mock fresh from one bank of 5,765 questions, then shows where each mark went and why.\" The count is live from bankStats or QuestionBankLine. Without a count: \"MockMob builds every mock fresh from one live question bank, then shows where each mark went and why.\"\n\nPrimary key: \"Try five questions\" (to #try-practice, no prefetch). Secondary key: \"Start free practice\" (to /signup). The signed-in states of L-006 and L-007 are unchanged.\n\nTrust sentence:\n- Monthly offer: \"Free to start. Pro is ₹99 a month, with no cap on mocks.\"\n- One-time offer: \"Free to start. Pro is ₹{oneTime} once, through {expires}, with no cap on mocks.\"\nThis carries the unlimited-mocks USP truthfully and quietly, as L-041 asks: the cap is lifted only on Pro.\n\nMobi's bubble on load: \"Your first question. No signup.\"\n\nThe card foot: \"Each answer shows the why. Taking other subjects? Pick yours free\" (links to /signup).\n\nHero links: \"Free DU eligibility and cutoff calculator\" and \"See the real exam screen\".\n\nThe recoveryReleased() branch keeps its own H1 and lead unchanged.\n\nHero word count: about 75, down from 121."
}

## loader

A first-visit loader built from the app's own opening (brand_opening.dart, OpeningTimeline). It is not a generic splash. It ends by landing in the site bar.

New files:
- BrandOpening.jsx and brand-opening.css.
- A tiny inline script at the top of page.js sets html[data-opening] before first paint. It reads localStorage 'mm:opened-v1' inside try/catch, and is skipped for:
  - repeat visitors;
  - signed-in users;
  - URLs with a hash;
  - prefers-reduced-motion and data-motion=reduced;
  - noscript.

Ground and letters:
- Ground: Night #12110E, Day #F3EFE6 (the app's grounds).
- Letters: per-letter paths split from logo B's merged path at letterX = [0, 865, 1445, 1968, 2549, 3423.22, 3987.35] (logo_geometry.g.dart:132-265). A one-off generator, scripts/brand/build-logo-letters.mjs, writes src/components/brand/logoLetters.generated.js.

Timeline in ms:
- 0: "mo" (the m plus Mobi as the second o) centred at min(28vw, 132 px) high.
- 140 to 300: Mobi blinks.
- 300 to 480: the empty right eye inks, scale from 0 to 1, 180 ms ease-out.
- 480 to 880: the letters unfold on paper hinges. "mock" rotates leftwards from the m and "b" rightwards from Mobi, rotateY(-90deg) to 0 at the shared edge, nearest letter first, 40 ms stagger, 280 ms each, cubic-bezier(0.23, 1, 0.32, 1). At the same time the camera pulls back, scale 1.5 to 1 on cubic-bezier(0.5, 0, 0.15, 1). The volt dot pops in at 820 over 160 ms.
- 880 to 1000: the word holds. This is the frame shown in the mock-up shots.
- 1000 to 1300: a FLIP flight to the site-bar logo's rect, translate plus scale over 300 ms on var(--ease-drawer) cubic-bezier(0.32, 0.72, 0, 1). From 1060 the ground fades from 1 to 0 over 240 ms ease-out.
- From 1080: the hero lines rise (opacity 0 to 1, translateY 12 px to 0, 360 ms, var(--ease-out), 60 ms stagger). The typing starts at 1400.

Total: 1.3 s.

Fail-safes:
- Pure CSS keyframes, so if JS never runs, the ground still reaches opacity 0 and pointer-events: none at 1.4 s.
- The H1 is in the DOM from first paint.
- Reduced motion: no loader.

L-043 needs reconciling. Its "about 3 s" wording was for the app; this is the web's 1.3 s first-visit version (see risks).

## typing

New file: HeroTyped.jsx, a client component inside the static H1.

Server render: "Accountancy" is in the slot, so the H1 paints whole at first render and LCP is not held back by JS.

Sequence:
- Starts 900 ms after hydration on repeat visits, or 1400 ms on a first visit (after the loader).
- Select and retype, the owner-approved HeroType grammar recovered from git (f61de0206^): the current word gets a selection highlight for 220 ms, then the next word types at 52 ms a letter.
- The selection highlight is --sel: #e4e9c2 on Day and rgba(244, 240, 230, .16) on Night. It is neutral on Night, never a volt wash.
- Each word holds 1800 ms. The order is Accountancy, Economics, Business Studies, English, then back to Accountancy, where it rests. A full pass is about 9.5 s.

Caret: a 0.075em by 0.78em bar in --ink with a 1 px radius. It is solid while typing. At rest it blinks twice (530 ms on, 530 ms off), then fades out over 180 ms, so nothing blinks forever (slop item M6).

Pausing and replays:
- It pauses on visibilitychange and when the hero leaves the viewport (IntersectionObserver), and resumes on the current word.
- At most 2 passes per visit.
- Reduced motion: a static "Accountancy", no caret.

Accessibility:
- The full sentence is in a visually hidden span.
- The visible runs are aria-hidden, so a screen reader never hears letter-by-letter changes.

Layout: the slot is a grid stack with a hidden sizer holding "Business Studies", so CLS is 0. Each line is display:block, so the wrap is fixed at every width.

Why this is more refined than Preparoo (study source/typing.txt): Preparoo deletes at 100 ms a character and types at 150 ms with an endless 0.7 s blinking caret. Here selection replaces deletion, it types three times faster, the loop is finite and the caret retires.

The heroLines.test.mjs H1 rule changes from "static headline" to these rules:
- the typed slot is aria-hidden;
- the sentence is present;
- the sizer holds the widest word;
- the caret retires;
- at most 2 passes.
L-016 is satisfied ("a visibly changing word, typed line, no glass, no glow").

## night

Night moves to the app's warm charcoal (mm_colors.dart:117-133 and the logoB charcoal) and volt goes back to being a fill.

Token changes in marketing-theme.css:3-8, html[data-theme='dark'] .mm:
- --paper: #12110e
- --paper-raised: #211f1a (the app's #1b1a16 is only 1.08:1 above the ground; #211f1a gives about 1.15:1, the C11 floor; the nav and the dock keep #1b1a16)
- --paper-sunken: #0e0d0b
- --ink: #f4f0e6
- --ink-2: #cfc8ba
- --ink-3: #a39c8f
- --line: rgba(244, 240, 230, .09)
- --line-strong: rgba(244, 240, 230, .17)
- --accent-line: var(--line-strong)
- --accent-wash: transparent
- --accent-text: #cddd5a. This is lamp-lit volt, hsl(66, 66%, 61%), under the 80% saturation threshold of slop item C10. It is used only by .lp-title__brand ("CUET 2027", L-017) and the tour heading's "MockMob" (L-030).
- A new token, --link: var(--ink). Links, kickers, numbers and timers use ink, not volt.
- --good-text: #bcd486.
- --volt-soft: #2b2d18, for selected-state fills only.
- The body background rule at marketing-theme.css:28 becomes #12110e.

Day matches the app's cream in marketing.css .mm (L-025, "one design theme matching the app"):
- --paper: #f3efe6
- --paper-raised: #fffdf8
- --paper-sunken: #eae5d9
- --ink: #17150f
- --ink-2: #45413b
- --ink-3: #6a655c
- --line: #e0dacb
- --line-strong: #c9c2b0

Volt keeps three roles (slop item C9):
1. The brand marks: the logo dot and Mobi.
2. The one primary key fill, with the existing 4 px #9db400 keycap edge.
3. The selected or progress fill, with dark ink.

Removals (file:line from the audit and slop studies):
- home-refinements.css:13-20 and :36: the lp-stage::before volt radial.
- :32-35: the 1 px volt top line on mm-drill.
- :41-42 and :49: dead ping and path CSS.
- hero-depth.css:35-66: the lp-proof glass and hero-metric type, which becomes the plain facts row.
- marketing-theme.css:47-61: the theme toggle thumb's glow box-shadows (keep the sun and moon and the travel). The 1.56 and 1.4 overshoot easings become var(--ease-out); the thumb keeps a 1.2 overshoot as Mobi-adjacent character, inside slop item M3's 1.3 limit.
- landing.css:234-276: the hero and close-band grid, dots and pointer spotlight.
- du.css:338-374: du-chip volt borders become --line, with --volt-soft fill and ink when pressed.
- feature-tour.css:11-13: the active tab's lime border and inset ring become a 2 px ink underline and weight 700.
- compass-ladder.css:6-8, 30, 52-53 and 69-70: lime edges, radial glows and glass become paper-raised with a 1 px line.
- tour-screens.css:6, 14, 41, 131, 144 and 191: lime under-glow, option glow and halo rings removed; the picked option is a --volt-soft fill.
- social-proof.css:14-17 and 35-37: the lime grid, orbit, rings, monogram and "glass over volt glow".
- lab-cinema.css:69, 91-95, 188-202 and 289-294: the scene-dot ring, bezel rings, chip and head edges, plan number and go button in volt text.
- mistake-lab.css:34, 50, 58, 92 and 121: lime edges, with right and correct in --good-text.
- home.css:43: the kicker in volt (kickers are folded into the h2s; see copy).
- hero-depth.css:97: the statement accent words go from volt to weight contrast (800 against 600).
- MarketingFooter and NavBar 'New' badge: volt text becomes an ink chip with a --line border.

The Night room painting keeps its own amber lamp. It is owned art, the one permitted light.

Acceptance:
- slop capture.mjs on Night: volt text runs at most 1 per viewport.
- Volt edges on containers: 0.
- Coloured glows: 0. Volt washes: 0. Content glass: 0.
- Lime-tint pixel share at most 1.2 times Day (slop item C12).
- Infinite loops in view: at most 1, Mobi's idle only.

## scroll

One gesture is one step in every held story and the statement, on touch, wheel and keys. This is the mechanism proven on the scroll bench (tmp/home-1104/scroll/prototype-one-gesture-v2.html, results2-p2-clamp.json): all 32 flick cells gave exactly +1 step, and wheel bursts of 1, 5 and 30 notches gave +1 each.

Implementation in ScrollStory.jsx plus a new pure module, scrollGesture.mjs.

Touch:
- A window-level, non-passive touchmove is registered only while a story track is within one screen (IntersectionObserver, rootMargin 100%).
- It owns a vertical-dominant gesture that starts inside a hold, after a 6 px slop.
- The step commits at touchend, from net travel of 40 px or more, or 12 px or more at 0.3 px/ms or more. The result is always +1, -1 or 0, never more.
- A 420 ms lock (120 ms under reduced motion) swallows gestures that start inside it.

Wheel and keys:
- A wheel burst ends after 160 ms of quiet and is one step.
- PageDown, Space and ArrowDown are one step each.

Commit and edges:
- On commit: scrollTo(rest[i], instant) under the sticky stage. The stage's content changes with its own 320 ms var(--ease-out) transition, so the page never glides (the LK47 cause of 2 Nov).
- At the first and last step, an outward gesture goes back to native scroll; the edges stay free.
- A fling entering from outside is clamped at the first rest, so step 0 is always shown.
- A native scroll that ends inside a hold (scrollend, or a 150 ms fallback) settles on the nearest rest, so there are no half states.
- Programmatic jumps (goTo, HashSettle, DemoJump, nav and position-band links) dispatch 'mm:jump' with their target, so the controller does not hold them at the first rest.

Step-driven visuals: fills, the Lab object tilt and the step progress become CSS transitions on [data-step], not scroll-linked:
- scroll-story.css:55-71;
- lab-cinema.css:511-512;
- hero-depth.css:98-190 for the statement.
React stays out of the per-step path: the stage gets data-step by attribute, and the scene components read it in CSS.

The statement becomes a 3-step held story on both widths. Its three phrases light in turn, by weight (600 to 800) and ink from --ink-3 to --ink over 220 ms. No word starts at 0.18 opacity any more, which fixes slop item M5's unreadable dim words.

Geometry: landing.css:1435 reserves #your-prep at 680svh on phones (100 + 10 x 58), and the desktop value stays at 570svh. Each held section's contain-intrinsic-size comes from calc(100svh + var(--steps) * var(--beat)), so fling targets and hash jumps stop drifting by about 950 px.

Tests:
- scrollStorySpeed.test.mjs is replaced by scrollGesture.test.mjs. It unit-tests decideStep({dy, dt, vEnd, locked, atEdge}) for every bench row.
- A real-Chrome CDP gate, scripts/design-audit/one-gesture-gate.mjs, reuses probe2.mjs. It cannot use chrome-headless-shell, which never scrolls on synthetic input.
- Acceptance:
  - 32 of 32 flick cells (4 distances x 4 speeds x Lab and tour) are +1 step and end at 0 px off a rest;
  - slow drags of 40, 120, 150 and 300 px are +1;
  - a 20 px drag is 0;
  - 100 px forward then 100 px back is 0;
  - two flicks 150 ms apart are 1 step, 700 ms apart are 2;
  - an entering fling of 600 px at 6000 px/s rests on step 0;
  - a wheel burst of 1, 5 or 30 notches, or a 60-event trackpad tail, is +1.
- These lock L-027, L-028 and L-029, which have no test today.
- The owner's own phone look, plus a real iPhone and a real Android check, are required before shipping (risk R1).

## examScreen

The section rebuilds ExamComparator.jsx (same export, so page.js is untouched) as a picture of the real MockMob runner (TestPageClient.jsx:1213-1470). It is theme-aware, not always dark.

Heading (no kicker):
- h2: "Practise on our screen. Rehearse on NTA's."
- Sub (19 words): "The same mock, timer and answers in either screen. With Pro, switch to NTA style any time."

Switch: a segmented control, "MockMob screen" or "NTA style". The selected segment is a --volt-soft fill with ink.
- NTA style shows the existing NTA rehearsal skin, deliberately faithful to NTA because rehearsal is its job.
- The default is ours.
- Switching keeps the selected answer and the timer, as the real runner does.

Console, from top to bottom (all real runner strings):
- Offline strip: "Saved on this device. Stay online to submit." in Hanken 500 13 px, --ink-3, on --paper-sunken.
- Header: an exit [x], "Full mock" over "Accountancy" (Bricolage 700 20 px), and a timer pill "38:12" (Hanken 700 tabular-nums with a clock icon). Under them, "Question 14 of 50" and "13 answered", and a 4 px progress bar with a volt fill.
- Question card:
  - chips "Admission of partner" and "Medium" (--line border, ink);
  - a status pill;
  - Mark and Clear;
  - the stem in Literata 600 19/21 px: "Goodwill brought in by an incoming partner is shared by old partners in:";
  - options A to D: B is selected (letter chip in a volt fill with dark ink), C is struck out by press-and-hold (a line-through and ink-3, with a 1 px ink strike line drawn left to right over 240 ms);
  - the hint "Press and hold an option to cross it out.".
- Bottom bar: Prev, Palette and Next (the volt key).

Palette:
- Phone: tapping Palette in the demo opens a sheet. It rises 280 ms on var(--ease-drawer), and the demo is live: the options, strike-out, Mark and Palette work locally, but Next stays inert.
- Desktop: the palette shows as a 300 px side panel.
- Contents: counters "13 Answered", "2 Marked", "1 Pending" and "34 Not visited" (Hanken 700 tabular-nums), then chips 1 to 50 outlined by state (answered is an ink fill, marked an ink ring with a corner tick, current a volt fill), and a Submit key.

Below the console, one line links to the fullscreen gate: "Full mocks open in your exam space, fullscreen, with warnings counted out of 3."

Heights:
- 390: section 980 px or less (was 1,644), console 700 or less (was 1,005).
- 1440: section 760 or less (was 1,363), with the console and palette side by side.

Files and drift:
- New exam-preview.css. The .lp-exam rules in home-refinements.css:84-228 are deleted.
- A parity test, examPreviewParity.test.mjs, asserts that every runner string the preview shows exists in TestPageClient.jsx: "Saved on this device", "Press and hold an option to cross it out", Mark, Clear, Prev, Palette, Next, Answered, Marked, Pending, Not visited. So the home screen cannot drift from the product (AGENT_RULES 27: real product preview over art, T007).
- Mobi stays out of the exam screen (no distraction in a paper).

## copy

The rule: never cut a section, step or showcase. Cut each block to the line that matters, and move numbers into the mock screens' visuals.

Caps (slop item W3):
- Every section sub is 20 words or fewer.
- Every tour body is 25 words or fewer, plus at most 2 points of 12 words or fewer.
- Each Lab step is a title plus 18 words or fewer.
- No phone viewport shows more than 60 words, except the FAQ.
- The page total at 390 is 2,000 visible words or fewer (from about 3,050).
- FAQ answers are 45 words or fewer.

Kickers (slop item T2): the section name folds into the h2, and the position band keeps the names.
- Lab: "The Mistake Lab traces every mark to a moment."
- Tour: "What's inside MockMob." (L-030 keeps "MockMob" in --accent-text).
- Recovery: "Fix a mistake once, then check it holds."
- Compass: "Hold your DU shortlist up to real cutoffs."
- Instagram: "Featured by CUET creators on Instagram."
- Compass Pro and Combo badges become h3 text.

Exact rewrites:
- Lab sub (27 words): "The Lab replays your mock: time, changed answers, the reason for each miss, and a plan."
- Tour sub, "Practise. Replay. Repair." (slop item W2): "Practise, replay and repair, then one plan for tonight."
- Practice body: "A short drill for a free evening, or a full 50-question, 60-minute mock for the weekend, on the same timer."
- Repair line (slop item W1, "not just"): "Fix the reason behind a wrong answer".
- Repair title: "Fix the reason you missed it."
- Repair body: "See why your pick was tempting and where it breaks, written from the official key. If the AI can't match the key, you pay nothing."
- LabCinema.jsx:35 "Repair the reason, not just the answer": "Repair the reason behind the miss".
- Ask Mobi point (27 words): "One credit buys one Mobi job. Every plan gets 50 free credits a month."
- Mob body (45 words): "Share a code and race your friends on the same five questions for 24 hours. Then Fix it together gives each of you a fresh one."
- DU sub: "Tick your subjects to see every DU programme they open under the 2026 rules. Free, no signup."
- Compass Pro body: "Your practice as a paper-by-paper range, set against your DU shortlist."
- Compass Pro list items: 10 words or fewer each.
- Instagram sub: "DU seniors and admissions creators have shown MockMob to their followers. Watch a reel here."
- FAQ "What is MockMob built for?" (58 words): "Timed CUET UG practice, a clear read of every mistake, and one next step for tonight. It covers the 15 subjects behind 19 of every 20 CUET papers, and every mock is built fresh from one live bank, with no cap on Pro." (45 words)

Other text changes:
- The tour counter "01 / 10" in Geist Mono (slop item T4) becomes the progress bar alone, with the step name.
- Middle-dot strings (slop item T6) become sentences.

What stays: the close "Five questions. Your move." (the one allowed fragment cluster), the pricing truth lines, the FAQ questions and L-024 (no disclaimers anywhere).

Every number is read from its existing source: bankStats, DU_FACTS, OFFER and SUBJECT_CLAIM.

## brandSystem

Palette: the app's cream (Day) and warm charcoal (Night) tokens, as in the Night section. Volt has three roles: brand marks, the one primary key, and the selected or progress fill. Correct answers use --good-text. Lamp amber is light in paintings only, never a control. This follows the swatch sheet's own rule.

Type ladder: the fonts are kept (Bricolage display, Hanken body, Literata reading), and the steps are made real with weight and size. Today all four display levels are 800 within a 1.2x range (brand study).
- Display XL (hero H1): Bricolage 800, 44 px at 390 and 76 px at 1440, line-height 0.98, -0.038em.
- Statement: Bricolage 600, 34/56, line-height 1.08, -0.03em. The lit phrase steps to 800.
- Section h2: Bricolage 700, 30/48, line-height 1.05, -0.03em, max 20ch.
- Close h2: Bricolage 800, 40/72.
- h3: Hanken 700, 20/22.
- Lead: Hanken 400, 17/19, line-height 1.48.
- Body: Hanken 400, 16, line-height 1.5.
- Small: Hanken 500, 14.
- Figures: Hanken 700 tabular-nums. Geist Mono is retired on the landing (.mm-measure, the tour counter and the GJ monogram), per slop item T1's leftover and T-050.
- Reading: Literata 600, 19 to 21 px, for every question stem in the hero sample, the exam preview and the Lab mock screens.
- That is six display and text sizes by role (R-029).

Mobi: one finish per job, and one Mobi in view (W-074).
- The rigged vector Mobi is the live host wherever something reacts: the hero stage.
- The baked poses (public/brand/mascot/*.webp) are section seats. Every seat is the same size (112 px phone, 140 px desktop), sits right of its h2, and speaks through the hero's bubble component in Hanken 600 14 px with the same tail and border. The 11 to 13 px captions go.
- Each seat line is 6 words or fewer and tied to the section's task. Examples: Lab "Let's find the lost marks.", Compass "Got a dream college? Let's look.", pricing "Free stays free.".
- PipGuide's flights stay.

Owned illustration replaces generic icons (slop items L5 and I2). FeatureTour maps slide id to the existing desk-object icons in public/art/icons/*-96.webp, drawn at 24 px in the rail and 40 px on the slide:
- practice: papers
- repair: mistakes
- learn: lesson
- replay: revise
- radar: questions
- prepos: keycards (no Sparkles)
- compass: compass
- combo: print
- rival: today
- mob: mob

Also:
- The reel cards' CSS orbit, rings and monogram are replaced by the reel's own cover frame.
- The logo B wordmark and its volt dot are untouched.
- The painted room now appears at both widths as the hero stage. It is the brand's scene.

Motion grammar:
- One authored load moment (the loader).
- Sections enter through their own stories. The roughly 20 identical Reveal fade-ups become a single 240 ms opacity fade on the h2 only (slop item M1).
- No infinite loops in view except Mobi's idle.
- Chrome uses var(--ease-out). Overshoot is for Mobi only.

## perItem

[
 {
  "item": "LK67: one hero idea, parity between phone and desktop",
  "change": "HeroMobi gets one 'stage' variant, and HeroRoom renders at every width. Mobi stands on the sample card's top edge as the host on both widths (128 px phone, 168 px desktop). The bubble is task-tied (load, correct, wrong, done), never tap-cycled. A tap gives one small act only: no bubble change, no buzz, no key lift. The Night answer sheet fills one bubble per answered sample question. The six tap lines are retired into the lead, trust sentence, bubble and key.",
  "acceptance": "Shots at 390x844 and 1440x900 show the same stage (room band, Mobi on the card edge, bubble, sample card) in Day and Night.\n\nA Playwright test asserts, at both widths:\n- .lp-room is visible;\n- one .mobi-react is in the hero;\n- Mobi's bottom is within 4 px of .card's top;\n- the bubble text is 'Your first question. No signup.';\n- after a real CDP tap, the bubble text is unchanged and one act ran;\n- after the first sample answer, the bubble text changes and, at Night, one sheet bubble fills.\n\nheroTaps.test.mjs is replaced by heroHost.test.mjs.",
  "files": [
   "src/components/landing/HeroMobi.jsx",
   "src/components/landing/HeroRoom.jsx",
   "src/components/landing/heroTaps.mjs",
   "src/components/landing/heroTaps.test.mjs",
   "src/components/landing/heroScene.test.mjs",
   "src/app/hero-scene.css",
   "src/app/page.js"
  ]
 },
 {
  "item": "LK68: Night de-neon",
  "change": "Night moves to warm charcoal tokens. Volt is a fill with three roles. The listed volt edges, radials, glass, halo rings, top-edge lines, volt text and toggle glow are removed or neutralised. The hero backdrop grid, dots and pointer spotlight are retired. Statement accents and kickers use weight and ink, not volt.",
  "acceptance": "The slop capture (capture.mjs plus summarize.mjs) on Night shows:\n- volt text runs at most 1 per viewport;\n- 0 volt edges on containers;\n- 0 coloured glows, 0 volt washes and 0 content glass;\n- lime-tint pixel share at most 1.2 times Day;\n- volt text runs at most 1.2 times Day;\n- at most 1 infinite loop in view.\n\nA static test, landing_slop_gate.test.mjs, also checks the landing CSS for:\n- radial-gradient with a volt colour;\n- backdrop-filter outside .mm-nav, .mm-dock and .sp-band;\n- box-shadow with a volt colour and a blur;\n- --accent-text used outside .lp-title__brand and .ft-title em.",
  "files": [
   "src/app/marketing-theme.css",
   "src/app/marketing.css",
   "src/app/home.css",
   "src/app/du.css",
   "src/app/feature-tour.css",
   "src/app/compass-ladder.css",
   "src/app/tour-screens.css",
   "src/app/social-proof.css",
   "src/app/lab-cinema.css",
   "src/app/mistake-lab.css",
   "src/app/landing.css",
   "src/components/landing/HeroBackdrop.jsx"
  ]
 },
 {
  "item": "LK69: one gesture, one step; no lag",
  "change": "ScrollStory gets the bench-proven one-gesture controller in a new pure module, scrollGesture.mjs:\n- a non-passive touchmove only near a story, 6 px slop, commit at touchend from net travel;\n- a 420 ms lock;\n- a 160 ms wheel burst;\n- a clamp on entering;\n- settle on the nearest rest;\n- programmatic jumps declare 'mm:jump'.\nVisuals become step-driven, and the statement becomes a 3-step story. Intrinsic sizes are fixed (#your-prep at 680svh on phones).\n\nPerf: one shared scroll reader, scrollBus.js, replaces the ObjectLife, PipGuide, SectionPosition and ScrollStory loops. There are no per-frame querySelectorAll, checkVisibility or getBoundingClientRect calls; rects are cached on resize. The ResizeObserver fit is write-only. The Mobi rig runs at 30 fps or less and pauses off screen.",
  "acceptance": "scrollGesture.test.mjs (unit tests for every bench row) replaces scrollStorySpeed.test.mjs.\n\nThe real-Chrome CDP gate, one-gesture-gate.mjs, shows:\n- 32 of 32 flick cells are +1 step with 0 px off a rest;\n- slow drags of 40, 120, 150 and 300 px are +1, a 20 px drag is 0, and 100 forward then 100 back is 0;\n- two flicks 150 ms apart are 1 step, 700 ms apart are 2;\n- an entering fling rests on step 0;\n- wheel bursts of 1, 5 and 30 notches, and a trackpad tail, are +1 each.\n\nPage height fresh equals warm, within 20 px.\n\nAt 4x CPU in real Chrome over 22 swipes:\n- p95 frame at most 20 ms;\n- frames over 50 ms at most 4;\n- worst frame at most 150 ms;\n- style recalcs on an idle hero at most 15/s, from 73;\n- TBT at most 300 ms;\n- CLS 0.\n\nThe owner looks on his own phone. A real iPhone and a real Android phone are checked.",
  "files": [
   "src/components/landing/ScrollStory.jsx",
   "src/app/scroll-story.css",
   "src/components/landing/scrollGesture.mjs",
   "src/components/landing/scrollBus.js",
   "src/components/landing/SectionPosition.jsx",
   "src/components/brand/ObjectLife.jsx",
   "src/components/brand/PipGuide.jsx",
   "src/components/brand/MobiReact.jsx",
   "src/components/landing/HashSettle.jsx",
   "src/components/landing/DemoJump.jsx",
   "src/components/landing/scrollStorySpeed.test.mjs"
  ]
 },
 {
  "item": "LK70: the phone hero says what we are",
  "change": "Text comes first:\n- H1 'CUET 2027 / mock tests for / [typed subject]';\n- the lead names MockMob, the 5,765-question bank and 'where each mark went and why';\n- the keys, then the trust sentence with 'no cap on mocks' on Pro.\nThe room shrinks from 320 px above the H1 to a 212 px band below the keys, with Mobi in it.",
  "acceptance": "At 390x844:\n- h1.top is 90 px or less (mock-up: 82);\n- the lead's bottom is 320 or less (304);\n- the primary key's bottom is 400 or less (378);\n- 'CUET', 'mock' and 'MockMob builds' are all above y 340, the top 40%;\n- Mobi's figure is fully visible (bottom 619 or less);\n- the question stem top is 700 or less (680).\n\nAt 360x640 the keys' bottom is 600 or less.\n\nAll of these are measured by getBoundingClientRect in a hero geometry test at 390x844, 412x915, 375x667 and 360x640, in Day and Night.",
  "files": [
   "src/app/page.js",
   "src/app/hero-scene.css",
   "src/components/landing/heroLines.mjs",
   "src/components/landing/heroLines.test.mjs"
  ]
 },
 {
  "item": "LK71: no AI-slop tells, no text walls",
  "change": "The copy caps and exact rewrites in the copy field. Kickers fold into the h2s. The 'not just' lines and the 'Practise. Replay. Repair.' cluster go. Middle dots become sentences. The '01 / 10' mono counter goes. The LiveStatsBand count-up becomes static figures. Lucide icons and Sparkles become owned desk icons. The roughly 20 Reveal fade-ups become one h2 fade.",
  "acceptance": "landingCopy.test.mjs is extended to check:\n- each tour body is 25 words or fewer and each point 12 or fewer;\n- each lp-sub is 20 words or fewer;\n- 0 matches for /not just|\\. Not /i, middle dots, padStart(2, '0'), Sparkles or .lp-kicker in page.js and the landing files;\n- FAQ answers are 45 words or fewer.\n\nA Playwright word count at 390 shows 2,000 visible words or fewer and no viewport over 60 words outside #faq.\n\nThe slop capture shows the T2, T4, T6, W1 and W2 counts at the pass bar.",
  "files": [
   "src/app/page.js",
   "src/components/landing/LabCinema.jsx",
   "src/components/landing/FeatureTour.jsx",
   "src/components/landing/TourScreens.jsx",
   "src/components/landing/MistakeLab.jsx",
   "src/components/landing/CompassLadder.jsx",
   "src/components/landing/CreatorReels.jsx",
   "src/components/landing/LiveStatsBand.jsx",
   "src/components/landing/Reveal.jsx",
   "src/components/landing/landingCopy.test.mjs"
  ]
 },
 {
  "item": "LK72: the exam screen is the real MockMob runner, shorter",
  "change": "ExamComparator.jsx is rebuilt from the runner's own parts:\n- the offline strip, header, timer pill and progress;\n- the question card with chips, Mark and Clear, the Literata stem, a selected option, a press-and-hold strike-out and the hint;\n- the Prev, Palette and Next bar;\n- a palette sheet or panel with the Answered, Marked, Pending and Not visited counters.\nIt is theme-aware. The 'MockMob screen / NTA style' switch keeps the answer and timer. NTA style is kept as Pro rehearsal. The .lp-exam CSS is deleted.",
  "acceptance": "Section height at most 980 px at 390 (was 1,644) and at most 760 px at 1440 (was 1,363). The console is at most 700 px at 390.\n\nIn Day the console background equals --paper-raised (it is not rgb(16, 24, 15)).\n\nThe default view contains no 'Mark for Review & Next', 'Save & Next' or 'Clear response'. Those strings appear only after switching to NTA style.\n\nexamPreviewParity.test.mjs: every runner string in the preview exists in TestPageClient.jsx.\n\nA CDP press-and-hold of 500 ms on option C strikes it out. A tap on Palette opens the sheet with the four counters. Switching to NTA style keeps option B selected and the timer value.",
  "files": [
   "src/components/landing/ExamComparator.jsx",
   "src/app/exam-preview.css",
   "src/app/home-refinements.css"
  ]
 },
 {
  "item": "LK73: a stronger brand identity of our own",
  "change": "Six parts:\n- the warm app palette in both themes;\n- a type ladder with real weight steps (800, 700 and 600);\n- Literata for questions;\n- Hanken tabular figures, with Geist Mono retired on the landing;\n- one Mobi role per finish, with same-size seats speaking through the hero bubble;\n- owned desk-object icons in the tour, and the painted room at both widths.\nThe fonts and logo B with its volt dot are kept as they are.",
  "acceptance": "Computed styles at 390 and 1440 check:\n- the H1, statement and h2 font-weights are 800, 600 and 700;\n- the H1 to h2 size ratio is 1.45 or more at 390 and 1.55 or more at 1440;\n- the question stems use Literata;\n- no Geist Mono inside .lp;\n- every .ft__tab has an img from /art/icons/;\n- every MascotSeat is 112 or 140 px and uses .bubble.\n\nThe 12-part anti-slop test, item 1 (identity with the logo hidden), passes in the judges' shots: the room, Mobi, the OMR sheet and the keycap are all owned.",
  "files": [
   "src/app/marketing.css",
   "src/app/marketing-theme.css",
   "src/app/home.css",
   "src/components/brand/Mascot.jsx",
   "src/components/landing/FeatureTour.jsx",
   "src/app/feature-tour.css",
   "src/app/layout.js"
  ]
 },
 {
  "item": "LK74: a refined loader and a refined typing line",
  "change": "Loader: BrandOpening, the app's 'mo unfolds into mockmob' opening. It takes 1.3 s on a first visit only, lands in the site bar by FLIP, has CSS fail-safes, and never shows to repeat visitors, signed-in users, hash links or reduced motion.\n\nTyping: HeroTyped, select and retype at 52 ms a letter. It holds 1800 ms, goes through the four commerce subjects, rests on Accountancy, and the caret retires. It pauses when hidden, makes at most 2 passes, the slot is aria-hidden with a reserved width, and reduced motion is static.",
  "acceptance": "A test on a fresh context checks the loader:\n- html[data-opening] is present;\n- .bo is gone and pointer-events are none by 1,400 ms;\n- the logo flight ends within 4 px of the .mm-nav logo rect.\nOn a second load in the same profile there is no loader. Under reduced motion there is no loader.\n\nTyping: the h1's accessible name is the whole sentence. The slot width is constant across a full pass (ResizeObserver delta 0). At rest (12 s) there is no element with an infinite animation in the h1. CLS is 0.\n\nThe lab LCP at 4x CPU is 2.5 s or less on repeat visits. First-visit LCP is reported separately.\n\nThe filmstrip at 100 ms steps (the Preparoo study's method) is attached for the owner.",
  "files": [
   "src/components/landing/BrandOpening.jsx",
   "src/app/brand-opening.css",
   "src/components/landing/HeroTyped.jsx",
   "scripts/brand/build-logo-letters.mjs",
   "src/components/brand/logoLetters.generated.js",
   "src/components/landing/heroLines.test.mjs"
  ]
 },
 {
  "item": "LK75: refine it ourselves, thought through",
  "change": "Every change refines something that exists. No section, story, showcase or animation is cut. The room, Mobi, the sample, the statement, the three held stories, the tour, Compass, DU, the exam screen, Instagram, pricing, FAQ and close all stay.\n\nThe conflicting locks are reconciled on purpose, not silently:\n- heroLines.test H1 becomes the typed rules;\n- scrollStorySpeed.test becomes scrollGesture.test;\n- the release9 hero grid and dots assertion becomes the room-stage assertion;\n- the L-016 and L-043 rows are updated in WEB-OWNER-LEDGER with today's words.",
  "acceptance": "Every section id present before is present after; the section-inventory test diffs against main. Each L-001 to L-045 row has a test id or a named screenshot check in landing_L_checklist.test.mjs, where 4 of 45 have one today. The full gate passes at 390 and 1440 in Day and Night.",
  "files": [
   "data/tests/release9_public_1018.test.mjs",
   "data/tests/landing_L_checklist.test.mjs",
   "mockmob-next/docs/brain/WEB-OWNER-LEDGER-2026-10-17.md"
  ]
 }
]

## mockup

{
 "html": "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-clarity/hero.html (built by build.mjs from hero.src.html in the same folder; shoot.mjs takes the shots under the browser lock). Open it with ?theme=night|day, ?still=1 (frozen mid-word) and ?frame=loader. Without ?still it plays the real select-and-retype line. It uses the real self-hosted Bricolage, Hanken and Literata files, the real logo B SVGs with the volt dot, the real Mobi poster SVG with mobi-figure.css, and the real painted rooms (scene-welcome-band-night, scene-empty-allclear-day), all copied into design-clarity/assets.",
 "shots": [
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-clarity/shots/final-390-day.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-clarity/shots/final-390-night.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-clarity/shots/final-1440-day.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-clarity/shots/final-1440-night.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-clarity/shots/final-390-night-loader.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-clarity/shots/final-1440-day-loader.png"
 ],
 "selfCritique": "I opened every shot. The mock-up went through four rounds (v1, v2, v3 and final, all in the shots folder).\n\nv1 had four defects:\n- the bar's Start free key leaked onto the phone, which caused 22 px of horizontal scroll (scrollWidth 412);\n- Mobi was positioned against the whole stage and fell below the card;\n- the room crop showed only the plant and bookshelf;\n- the logo had lost its volt dot.\nv2 fixed them: specificity, a scene wrapper, a re-cropped room, and the dot added at Logo.jsx's geometry.\n\nv3 had two defects:\n- the card covered Mobi's boots;\n- the desktop bubble broke as 'No / signup.'.\nI fixed them by standing him on the card edge (bottom = overlap + 1) and adding text-wrap: balance with a wider bubble. I also centred the desktop columns vertically.\n\nThe final round changed one line: 'then finds the mistake behind each lost mark' overstated what we do for skipped questions, so it now reads 'then shows where each mark went and why'.\n\nAgainst the slop checklist on the final shots:\n- C1: one volt text run per viewport ('CUET 2027', lamp-lit #cddd5a at Night) plus the key fill, the progress fill and the logo. Pass.\n- C2 to C8: no lime edges, glows, radials, lit edges, grid or dots, content glass or pings. Pass.\n- C9: volt has three roles. Pass.\n- C10: the Night accent is at 66% saturation. Pass.\n- C11: the mock-up card is #1b1a16, only 1.08:1 above the ground. The spec raises cards to #211f1a so they pass 1.15.\n- C12: Night has the same element count as Day. Pass.\n- T1, T2, T3 and T6 pass. T5: the facts row uses 17 px body type, not hero-metric type, but it is still a 4-cell row (a residual risk under L3).\n- L1: the H1 is at 9.7% and the pitch sentence ends at 36%. Pass.\n- L2: one idea on both widths. Pass. L4: two levels. Pass.\n- I3: Mobi has a job. Pass.\n- M6: the sentence is in the DOM, the slot is reserved, the line is finite and the caret retires. Pass.\n- W1, W2 and W5: none in the hero. Pass.\n\nThe owner's 12-part test:\n- Identity with the logo hidden: yes (the painted room, Mobi, the OMR poster, the keycap).\n- One primary action: yes.\n- True content: yes (bank count, ₹99, 73 programmes, subjects within the 15).\n- Hierarchy: yes. Composition: yes.\n- Type by role: Bricolage for display, Hanken for body, Literata for the stem.\n- States, motion and a11y: specified, not yet shown in a still.\n- No pseudo-evidence: yes.\n- What would be better without this: the facts row is the weakest element.\n\nRemaining weaknesses:\n- On desktop there are about 170 px of air under the hero links at 900 px tall.\n- The Night room is warm and busy behind the bubble.\n- The 'mock tests for' line is plain by design, which leaves the brand line to carry it.\n- The mock-up shows the poster frame, not the rig.\n- The toggle is simplified.\n- It is a static composition, so nothing about real-device motion or performance is proven."
}

## keepsAndNeverCuts

Kept and refined, never cut (L-004, L-005, L-042):
- the painted room, now on desktop too;
- the rigged Mobi and his tap animation (refined to one act);
- the five-question sample with no signup (T003);
- the hero links;
- the facts nav, restyled;
- the statement and its shelf of lamp-lit subject objects (a 3-step held story now);
- the Mistake Lab cinema;
- the 10-slide feature tour;
- the Score Recovery Lab;
- Compass ladder and Compass Pro;
- the DU eligibility teaser, Combo Planner and college destinations;
- the exam section, with NTA style kept as rehearsal;
- the live stats band (static figures);
- Instagram reels;
- the wall of love (still voice-gated);
- pricing, FAQ, close and footer;
- PipGuide flights, section Mobi seats, the position band and the state-aware dock (L-008 to L-011).

Fonts and logo B with its volt dot are unchanged. The keycap buttons are unchanged.

Truth sources stay wired: bankStats/QuestionBankLine, DU_FACTS, OFFER/priceLine, SUBJECT_CLAIM, CAPABILITIES, MOB_LIVE and STUDY_LIVE.

Standing rules respected:
- mobile-first: every section is composed for 390 first, and the hero stage is identical at both widths;
- no glow, sheen, light running round edges, drifting blobs or gradient text (the only gradient is a functional image scrim);
- Night subtle;
- no defensive sub-remarks (L-024);
- unlimited mocks said truthfully ('no cap on mocks' on Pro) and quietly (L-041);
- a typed line for the changing headline (L-016);
- one gesture = one slide, locked by tests (L-027 to L-029).

Retired as code, with the same job done better, so these need the owner's eye:
- the six tap-only bubble lines;
- the desktop-only pointer spotlight, hairline grid and dot matrix (C6, M7).

## risks

R1, scroll on real devices. The one-gesture controller was proven only in Chromium 151 with CDP touch. Still open:
- iOS Safari's handling of a non-passive window touchmove, and whether scrollTo stops momentum;
- the scrollend fallback;
- visualViewport re-measure.
LK47 (2 Nov, 'it races') and LK69 pull in opposite directions. The new controller never glides, but the owner must judge it on his phone before it ships. Fallback: settle-only, with no gesture capture.

R2, the hero headline. The headline is static under his 1 Nov ruling, R3 H1. LK74 and L-016 ask for typing. This proposal types the subject inside a true sentence; the decision is his. 'Ace the CUET' at Preparoo uses a typed slot too. Ours differs (subjects, not exams; select and retype; finite; the caret retires), but R-054, don't copy, should be checked by the judges.

R3, the loader length. L-043 says 'about 3 s' (most likely an app ask). The web version is 1.3 s on a first visit only. It covers the H1 for about 1 s on that visit, which may move first-visit LCP by about 1 s. Measure first-visit and repeat LCP separately. If field LCP goes above 2.5 s, drop to a 0.9 s variant played in the bar.

R4, the warm palette. Day #f3efe6 and Night #12110e are .mm tokens, so every public page shifts (pricing, the /cuet pages, signup, the DU tools). It needs screenshots of each before shipping. It could be scoped to .lp first, but that would break 'one theme'.

R5, retiring things. The HeroBackdrop grid, dots and pointer spotlight, and the tap-cycled lines, are removed effects. They stand against 'never remove an animation'. The argument: they were desktop-only or toy-like (L-003, I3), and the painted room and task-tied Mobi replace them. They need his explicit OK. Fallback: keep a static Day-only grid at 0.06 opacity.

R6, the exam preview. It duplicates runner markup, so the parity test must stay green. NTA style is Pro, so the sub says 'With Pro' as a fact. Never add a disclaimer.

R7, the typed subjects. They must stay within CUET_PUBLIC_ALLOWED_SUBJECTS. They are commerce-first by design (L-023). A science student sees 'Pick yours free' and the 15-subject claim in the shelf and FAQ (L-015).

R8, the Night raised surface. At #211f1a it departs slightly from the app's #1b1a16 so it passes C11.

R9, perf numbers. The perf numbers come from headless or 4x lab runs and are a diagnosis only. GPU cost of the room image, now on desktop too, is unmeasured (+40 KB AVIF, lazy).

R10, page.js ownership. page.js is owned by packet P1 alone, so P4 and P5 must not edit it. Tour icons map inside FeatureTour, and the exam heading lives inside ExamComparator.

## buildPackets

[
 "P1 Hero, loader, typing and page.js copy. Owns these files:\n- src/app/page.js (hero JSX, the statement as a 3-step story, the facts row, the TOUR/faq/sub/h2 string rewrites from the copy spec, kickers removed);\n- HeroMobi.jsx and HeroRoom.jsx ('stage' variant at all widths, sheet fills on sample answers);\n- heroLines.mjs and heroTaps.mjs, which becomes heroHost.mjs;\n- new HeroTyped.jsx, BrandOpening.jsx and brand-opening.css;\n- hero-scene.css and hero-depth.css (proof glass to facts row, statement weight accents, step-driven statement);\n- HeroBackdrop.jsx (retired from the hero and the close band);\n- scripts/brand/build-logo-letters.mjs and logoLetters.generated.js.\nTests: heroLines.test, heroHost.test, heroScene.test, brandOpening.test, the landingCopy.test caps, and release9_public_1018.test (hero assertion).\nUses P3's ScrollStory API unchanged (steps, data-step).\nDone when: the geometry, typing and loader acceptance in LK67, LK70 and LK74 pass in Day and Night at 390, 412, 375, 360 and 1440.",
 "P2 Night/Day tokens and de-neon, CSS only. Owns:\n- marketing-theme.css and marketing.css (.mm tokens, toggle glow, Day cream);\n- home.css, du.css, feature-tour.css, compass-ladder.css, tour-screens.css, social-proof.css, lab-cinema.css and mistake-lab.css;\n- landing.css (grid, dots and spotlight rules removed, plus the #your-prep intrinsic size fixed to 680svh on phones and calc(100svh + steps x beat) for each held section).\nNew static test: data/tests/landing_slop_gate.test.mjs.\nDone when: slop capture on Night shows C1 at most 1 per viewport; C2, C3, C4 and C7 at 0; C12 at most 1.2x Day; and the other public pages are screenshotted in both themes with no unreadable text.",
 "P3 One gesture, one step, and the scroll and perf fixes. Owns:\n- ScrollStory.jsx and scroll-story.css;\n- new scrollGesture.mjs (pure decideStep) and new scrollBus.js (one passive scroll reader plus rAF, cached rects);\n- SectionPosition.jsx, sectionPositionPhase.mjs, HashSettle.jsx and DemoJump.jsx ('mm:jump' targets);\n- brand/ObjectLife.jsx, brand/PipGuide.jsx (no per-frame queries or checkVisibility, IntersectionObserver instead);\n- brand/MobiReact.jsx (30 fps idle cap, pause off screen or hidden).\nReplaces scrollStorySpeed.test.mjs with scrollGesture.test.mjs, and adds scripts/design-audit/one-gesture-gate.mjs (real Chrome CDP, from tmp/home-1104/scroll/probe2.mjs).\nKeeps the ScrollStory props and the data-step contract stable for P1.\nDone when: the 32/32 flick matrix, the slow drag, reverse and wheel rows, fresh-equals-warm geometry within 20 px, and the 4x-CPU frame targets pass.",
 "P4 The exam screen as the real runner. Owns:\n- ExamComparator.jsx (rebuilt in place as the runner preview, heading inside it);\n- new exam-preview.css;\n- home-refinements.css (deletes .lp-exam 84-228, plus the hero radial 13-20/36, the drill top line 32-35 and the dead ping/path rules 41-49, exactly as listed).\nNew tests: examPreviewParity.test.mjs, and a Playwright check for the section height (980 px or less at 390, 760 or less at 1440), Day theming, strike-out, the palette sheet and the switch keeping the answer and timer.",
 "P5 Brand system in components. Owns:\n- FeatureTour.jsx (maps slide id to /art/icons desk objects, drops the '01 / 10' mono counter);\n- TourScreens.jsx, LabCinema.jsx and MistakeLab.jsx (component-owned copy cuts: Lab steps 18 words or fewer, 'Repair the reason behind the miss', numbers moved into the screens, Literata stems);\n- CompassLadder.jsx, CreatorReels.jsx (reel cover frame replaces the orbit and monogram) and LiveStatsBand.jsx (no count-up);\n- Reveal.jsx (one h2 fade);\n- brand/Mascot.jsx (seat sizes 112/140, hero bubble component, lines of 6 words or fewer);\n- src/app/layout.js (Literata loaded for .lp stems).\nDone when: the LK73 computed-style checks and the LK71 component word caps pass.",
 "P6 Gate and ledger (new files and docs only, built in parallel and run last). Owns:\n- data/tests/landing_L_checklist.test.mjs (one test id or named screenshot per L-001 to L-045);\n- scripts/design-audit/home-1104-gate.mjs (shots at 390x844, 412x915, 375x667, 360x640 and 1440x900 in Day and Night; slop capture and summary; word counts; the one-gesture gate; the 4x-CPU perf in real Chrome; section inventory diffed against main);\n- the WEB-OWNER-LEDGER rows L-016 and L-043, updated with the owner's 4 Nov words (verbatim quotes, no new authority);\n- the DESIGN_DECISIONS note for this change (AGENT_RULES 39).\nDone when: the gate runs end to end on localhost and production, and every packet's acceptance is a named check in it."
]

## evidenceIds

[
 "T003",
 "T006",
 "T007",
 "T009",
 "S014",
 "S016",
 "R-023",
 "R-029",
 "R-054",
 "R-093",
 "R-101",
 "R-153",
 "R-155",
 "R-203",
 "T-005",
 "T-010",
 "T-024",
 "T-031",
 "T-050",
 "T-062",
 "T-072",
 "T-080",
 "T-103",
 "T-112",
 "T-124",
 "A-001",
 "A-009",
 "A-012",
 "C1",
 "C2",
 "C3",
 "C4",
 "C5",
 "C6",
 "C7",
 "C9",
 "C10",
 "C11",
 "C12",
 "T1",
 "T2",
 "T4",
 "T5",
 "T6",
 "L1",
 "L2",
 "L3",
 "L4",
 "L5",
 "L7",
 "I2",
 "I3",
 "M1",
 "M2",
 "M3",
 "M4",
 "M5",
 "M6",
 "M7",
 "W1",
 "W2",
 "W3",
 "L-003",
 "L-004",
 "L-005",
 "L-015",
 "L-016",
 "L-017",
 "L-019",
 "L-023",
 "L-024",
 "L-025",
 "L-027",
 "L-028",
 "L-029",
 "L-030",
 "L-041",
 "L-043",
 "W-074",
 "LK47"
]

## performance

Baseline from the audit (real Chrome, 4x CPU, 22 swipes):
- p95 frame 24 ms;
- 23 frames over 50 ms;
- worst frame 474 ms;
- style recalcs: 3,978 recalcs taking 7.8 s;
- idle hero: 73 recalcs per second;
- TBT 536 ms;
- LCP 2,944 ms (the lazy room AVIF);
- CLS 0.

Levers, in order of measured cost:
1. One scroll reader, scrollBus.js: a single passive listener and one rAF publishing scrollY and the viewport. ObjectLife lean (the 3.3 s self-time hot spot), PipGuide gaze, SectionPosition and ScrollStory subscribe to it. Element rects are cached on ResizeObserver or resize, so no per-frame layout reads.
2. PipGuide: cache the station nodes at mount and on change. IntersectionObserver replaces per-frame querySelectorAll and checkVisibility (about 4.1 s together), and the 260 ms timeout goes.
3. ScrollStory fit: the ResizeObserver callback becomes write-only, with reads batched in one rAF. This removes the 118-158 ms forced layout frames. Step changes set data-step by attribute, with no React re-render of the whole stage (the 108-116 ms frames).
4. Scroll-linked view-timeline animations in the stories (52 of them) become step-driven CSS transitions.
5. MobiReact idle is capped at 30 fps and paused when off screen or the tab is hidden. Target: idle hero recalcs of 15/s or fewer.
6. Correct contain-intrinsic-size per section, so there is no 906 px geometry drift and no section-draw spikes on fling targets.
7. Hero: the room image moves below the keys. It is lazy with fetchpriority low, so LCP becomes the H1 text on repeat visits. The loader is CSS-first and adds no long task.
8. Next link prefetch is off for in-page jumps (already done on the hero key).

Targets at 4x CPU in real Chrome:
- p95 frame 20 ms or less;
- frames over 50 ms: 4 or fewer;
- worst frame 150 ms or less;
- TBT 300 ms or less;
- LCP 2.5 s or less on repeat visits (first visit reported separately);
- CLS 0;
- page height fresh equals warm, within 20 px.

These are lab numbers and only a diagnosis (R-101, R-203). Field INP and LCP must be read after deploy.

