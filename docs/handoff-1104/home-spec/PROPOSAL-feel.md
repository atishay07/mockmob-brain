## id

feel

## title

Feel-first home: one room, one typed line, one gesture per step, Night without neon

## thesis

The home page should feel calm and exact before it tries to look impressive. The phone hero opens on the sentence that says what we are, "CUET 2027 mocks that find your [weak chapter.]". The last two words are typed in our own rhythm. Below it sits the key, then one stage that is the same on phone and desktop: Mobi's painted room, with the real first question on his desk and Mobi standing under the answer sheet, turned toward it.

The entry is the app's own "mo" unfold, about 1.28 s and on the first visit only. It hands the wordmark into the site bar.

Every held story moves exactly one step per touch, wheel burst or key. One scroll reader and cached geometry keep a mid-range Android under budget.

Night becomes the app's warm charcoal, and volt is held to its few real jobs: the logo and Mobi, "CUET 2027", the primary key, and the selected state. Edges become neutral hairlines, and every glow, wash and content glass panel goes.

Nothing is cut. The tap pitch, the room, the grid's pointer effect, the statement scrub and the NTA view are each refined into a calmer form that does the same job. Evidence: T003 (value before signup: the playable question is on the first screen), T007/T009 (real product preview, not decoration), T002/S015 (no fake progress in the loader), S014 (progressive disclosure for the pitch lines), S016 (WCAG 2.2: reduced motion, the screen-reader sentence, focus), S017/S018 (slop is missing intent).

## hero

{
 "phone": "390x844, measured on the mock-up. Site bar 0-64 px: logo B with the volt dot (the Day dot is #9DB400), the calm theme switch and the 44 px menu button.\n\nCopy block (20 px side gutter):\n- H1 top at y 88 (10.4% of the screen). Bricolage 800, 41/1.02, -0.038em, three lines: 'CUET 2027 mocks' / 'that find your' / [typed slot]. Only 'CUET 2027' uses --accent-text, which is volt on Night and #526700 on Day (L-017).\n- Lead at y 229-306: Hanken 17/1.5, --ink-2, three lines.\n- Primary key at y 328-384: 'Try five questions', full width, 56 px tall, radius 16, volt fill with --volt-ink, plus the owned 4 px #9DB400 bottom edge. No glow.\n- Secondary text button, 48 px: 'Start free practice' (LandingActions).\n- Facts line at y 446-489: 15 px --ink-3, two short sentences.\n\nStage at y 517: a 358x268 room panel, radius 24. Night uses scene-welcome-band-night, object-fit cover at 64% 40%. Day uses scene-empty-allclear-day at 66% 40%, scaled 1.1 to crop the feathered edge.\n- Mobi is the rigged vector Mobi, 134 px tall. He stands at the right under the answer-sheet poster, facing left, feet resting on the card's top edge.\n- The live DemoDrill card is full width minus 10 px. It overlaps the room by 44 px and runs past the fold, so the question invites the scroll. Its header reads 'English' and 'Question 1 of 5', left-aligned, in ink.\n\nFirst-screen shares: copy 64-489 px (50%), room plus card top 517-844 (39%). Mobi starts at y 619, after the headline, lead and key.\n\nThe hero links ('Free DU eligibility and cutoff calculator', 'Try the exam-day screen') move under the card on phones. The proof row stays under the stage.",
 "desktop": "1440x900, measured. Bar 72 px with a 1200 px container: logo, five links (the volt 'New' badge on Cutoff calculator becomes nothing; the page that matters is linked), switch, 'Log in', and 'Start free' as a secondary key.\n\nTwo columns, 1fr and 520 px, gap 64, centred.\n- Left column:\n  - The same H1 at 66/1.0, -0.04em, top at y 174.\n  - Lead at 19/1.5, max 36ch.\n  - Key (58 px) and secondary side by side.\n  - Facts on one line.\n  - Two underlined ink links: 'Free DU eligibility and cutoff calculator' and 'Try the exam-day screen'.\n- Right column: the same room panel, 520x600, radius 28. The same Mobi at 196 px stands under the answer sheet at the right, facing left. The same DemoDrill card (330 px, all four options and 'No signup. Each answer comes with the why.') sits bottom-left on the desk.\n\nUnder the hero, the proof row is calm: no glass, a hairline top border, Hanken 700 20 px tabular figures, one 14 px --ink-3 line each. It reads '5 questions' (Free to try, no signup), '73 DU programmes' (Matched to your subjects, from DU_FACTS), '2 exam screens' (MockMob, and NTA style) and '60 minutes' (50 questions on the full clock).\n\nThe phone and desktop show the same idea, the same Mobi role and the same card. Only the scale and the column change (LK67, L-003).",
 "mobi": "One role on both sizes: Mobi is the host of your first question, standing in his room under the answer sheet and turned toward the card. He never stacks above the headline.\n\nWhat stays:\n- His tap: the MobiReact act cycle, hop and wink.\n- On Night, the painted answer sheet fills one bubble per tap, 120 ms after the tap. The bubbles now fill in pencil graphite #2B2A26 instead of volt.\n- The 8 ms buzz and the 3.5 s look-down at the key if untouched.\n\nWhat changes:\n- No speech bubble on load, and no 'Hi, I'm Mobi. Tap me.' The six tap-only pitch lines go into the lead, the facts line and the typed phrases, so every student reads them (S014).\n- His bubble appears only when he reacts to something the student did. After the first answer, the existing host reaction to the demo shows in a fixed-size 240x56 bubble anchored above his head. It enters with opacity 0 to 1 and translateY 6 to 0 over 240 ms, cubic-bezier(.22,1,.36,1), and holds 2.6 s. Its size never changes.\n- When each typed phrase completes, he glances at the headline: eyes shift 2 px over 140 ms out and 160 ms back (event 'mm:hero-typed').\n- The pointer spotlight from HeroBackdrop becomes his gaze, following the pointer on desktop and the last touch on phones. It is the same effect on both sizes (M7 parity).\n\nPerformance rule: the rig's frame loop runs only during an act or glance. At rest he is the static poster SVG plus one CSS breath on a transform (4 s, paused off-screen). That is 0 rAF per second idle, down from 52.",
 "words": "H1, with the full sentence in the DOM for screen readers and search: 'CUET 2027 mocks that find your weak chapter, your lost minutes and your second guesses.'\n\nVisible lines: 'CUET 2027 mocks' / 'that find your' / typed slot.\n\nTyped phrases, in order, one round:\n1. 'weak chapter.' Chapter review names the chapter to fix first, free after every mock.\n2. 'lost minutes.' The Lab's time on each question.\n3. 'second guesses.' Every answer you changed, from the Lab and Replay.\n\nThe round ends back on 'weak chapter.' Each phrase is 13 to 15 characters, so it fits one line at 41 px on a 350 px column.\n\nLead (19 words): 'Every mock is fresh from one bank of 5,765 questions, timed like the real paper. Then see where each mark went.' The count is live from bankStats (/api/stats bankSize). Without it: 'Every mock is fresh from one live question bank, timed like the real paper. Then see where each mark went.'\n\nPrimary key: 'Try five questions' (scrolls to #try-practice). Secondary: 'Start free practice'.\n\nFacts, two sentences and no middle dots: 'Free to start.' / 'Pro is ₹99 a month, with no cap on mocks.' This is built from priceLine(OFFER). On the one-time offer it reads 'Pro is ₹X once, through <date>, with no cap on mocks.'\n\nThat facts line states the USP (unlimited mocks from one central bank) truthfully and quietly (L-041).\n\nIf recoveryReleased(), the H1 keeps its own static line, 'Find the mistake behind the marks.', and the typed slot is off."
}

## loader

BrandOpening.jsx is the app's opening (brand_opening.dart OpeningTimeline), ported. It runs on the first visit only and lasts 1,280 ms.

How it renders and runs:
- It is rendered first inside the home page, as server-rendered markup with inline critical CSS (2.5 KB at most), so it paints at first paint, as Preparoo's preloader-fix does.
- A 1.2 KB inline script runs before the overlay in the document. It adds html.mm-open-skip, which hides the overlay before paint, in five cases: localStorage 'mm.opened' is less than 30 days old (try/catch), reduced motion is set (OS or data-motion), the URL has a hash, the referrer is our own origin, or the page is a bot or prerender.
- No fonts or images are needed. The letters are inline SVG paths split from the app's logo_geometry.g.dart into src/components/brand/logoLetters.generated.js by a one-off script, so nothing waits on font loading. Preparoo has to gate on its font.

Timeline, from first paint:
- 0 ms: a full-screen curtain in var(--paper) (#F3EFE6 Day, #12110E Night). 'm' plus Mobi as the 'o' sit centred at scale 2.4.
- 0-150: Mobi blinks (eye scaleY 1 to 0.1 to 1).
- 320-520: the right eye's detail inks in (opacity).
- 500-1000: the camera pulls back, scale 2.4 to 1, cubic-bezier(.5,0,.15,1).
- From 520: 'mock' unfolds leftward (k, c, o, m, 40 ms stagger) and 'b' unfolds rightward.
  - Each letter turns rotateY(-90deg) to 0 on its inner edge, a paper hinge, over 280 ms, cubic-bezier(.22,1,.36,1).
  - Opacity goes 0 to 1 over the first 120 ms. There is no overshoot.
- 860: Mobi glances (2 px, 140 ms out, 160 ms back).
- 940: the volt dot appears (scale .6 to 1 and opacity, 160 ms).
- 1000: the word is composed. This is the mock-up's loader frame.
- 1000-1280: hand-off.
  - The composed wordmark moves into the site bar logo's rect (FLIP translate and scale, read once at 0 ms) over 280 ms, cubic-bezier(.65,0,.35,1).
  - The curtain fades 1 to 0 from 1040 ms over 240 ms, ease-out.
  - The nav logo, kept visibility:hidden until then, shows at 1280. The overlay is display:none at 1300.

Rules:
- Any pointerdown, touchstart, wheel or keydown jumps straight to the hand-off (a 160 ms fade). It never delays a control.
- No JS needed: the CSS animation alone ends it, so a no-JS user is never trapped.
- aria-hidden, no focus trap, and the hero is fully in the DOM underneath.
- No progress bubbles or bars, because nothing real is being counted (T002).
- The typed line starts 600 ms after the hand-off.

Tests and acceptance:
- A Playwright filmstrip at 100 ms steps: frame 0 shows 'mo'; frames 600-800 show a partial unfold; frame 1000 matches the mock-up loader frame; frame 1300 shows no overlay and the nav logo in its final rect.
- A second load shows no overlay. Reduced motion shows no overlay.
- CLS is 0.
- LCP is no more than 150 ms worse than with ?open=off (lab, CPU 4x).
- document.elementFromPoint returns hero content at 1300 ms.

L-043 asks about 3 s, flagged in the risks. 1.28 s matches the app's warm open and Preparoo's roughly 1.35-1.6 s.

## typing

HeroTypeLine.jsx, a client island inside the H1.

Markup:
- span.sr holds the full sentence.
- The visible part is aria-hidden.
- The slot is an inline-grid stack: each phrase sits in the same grid cell with visibility:hidden, so the slot is exactly as wide as 'second guesses.' and CLS is 0. On phones the slot is its own third line.
- The server renders 'weak chapter.' as the live text, so it shows at first paint and works with no JS.

Start: 600 ms after the loader hand-off, or 900 ms after first paint when the loader is skipped. It also waits until document.fonts.ready and the hero is intersecting.

One round only:
1. Hold 'weak chapter.' for 2,400 ms.
2. Erase: backspace at 26 ms per character (the first two characters at 40 ms).
3. 160 ms empty.
4. Type 'lost minutes.' at 58 ms per character plus a deterministic ±14 ms jitter seeded from the character code, adding 90 ms after a space.
   - Each new letter enters with opacity 0 to 1 and translateY(.08em) to 0 over 120 ms, cubic-bezier(.22,1,.36,1). It is crisp, never blurred.
5. Hold 2,400 ms. Then 'second guesses.' the same way, then back to 'weak chapter.'.

The round takes about 12.5 s, then the line rests for good. There is no loop. Preparoo loops forever at 150/100 ms per character with a 2,000 ms pause; we keep its patience and drop the endless loop (slop M6).

Caret:
- 3 px wide by .78em, var(--caret), which is ink and never volt. Radius 1.
- Solid while erasing and typing.
- During each hold it blinks twice (530 ms period, step timing), then fades out over 160 ms. It comes back when the next erase starts.
- After the round it is gone.

Other behaviour:
- When each phrase completes, the component dispatches 'mm:hero-typed', and Mobi glances.
- It pauses mid-character when the hero leaves the viewport or the document is hidden, and resumes from the same character.
- Reduced motion: static 'weak chapter.' and no caret.
- It uses no setInterval: one timer chain with requestAnimationFrame for letter entry. Under 1.5 KB.

Tests:
- heroLines.test.mjs replaces the R3 'static H1' assertion with:
  - the phrase list and the sentence;
  - each phrase is at most 15 characters;
  - the slot is aria-hidden and the sizer holds every phrase;
  - the round count is 1;
  - reduced motion is static.
- Playwright at 390 and 1440:
  - CLS is 0 over 14 s;
  - a screenshot at t of about 9.1 s shows 'second gu' plus the caret (the mock-up frame);
  - after 14 s, 'weak chapter.' shows with no caret element visible.

## night

Night becomes the app's warm charcoal, from mm_colors.dart dark.

Night token block (marketing-theme.css:2-11):
- --paper #12110E, --paper-raised #1B1A16, --paper-raised-2 #25231E, --paper-sunken #0D0C0A.
- --ink #F4F0E6, --ink-2 #BDB6A6, --ink-3 #A09989 (6.4:1 on the ground).
- --line #312E27, --line-strong #4A453B.
- --accent-line #4A453B: neutral, so every rule that used it loses its lime edge in one change.
- --accent-wash rgba(244,240,230,.04).
- --surface-hover #22201B, --edge-light rgba(255,246,228,.14).
- --good-text #C6E86E, --warn-text #EDB75A, --bad-text #FFA396.
- --accent-text stays #D2F000, but it is used only for 'CUET 2027' (L-017) and 'MockMob' in the tour heading (L-030).
- html and body background #12110E.
- .mm-screen product stills take the same warm values, with slate #1B1A16.

Day moves to the app's warm paper:
- --paper #F3EFE6, --paper-raised #FFFDF8, --paper-sunken #EAE5DA.
- --ink #17150F, --ink-2 #454036, --ink-3 #655F53.
- --line #D8D1C2, --line-strong #BDB4A2.
- --accent-text #526700 (kept).
- --accent-line #BDB4A2.

Volt keeps exactly three jobs (C9):
1. Brand marks: the logo dot and Mobi.
2. The primary key fill, with --volt-ink.
3. The selected state as a volt fill with --volt-ink. Never an outline or an inset ring.

Correct and good use --good-text. Links, kickers, numbers and timers use ink. Focus rings stay functional.

Replacements, file by file from the audit's top 15 (both themes unless noted):

| What | Where | Change |
|---|---|---|
| du-chip ×19 | du.css:338-374 and about 20 rules | 1 px --line-strong; selected = volt fill |
| ft__row active tab | feature-tour.css:11-13 | No border plus inset ring; active = --paper-raised-2 plus an ink 2 px left tick? No: active = volt fill on the tab's small marker only, with an ink label |
| cl__group buttons | compass-ladder.css:6-8 | Neutral hairline |
| lp-cpro, lp-combo volt radials and glass | compass-ladder.css:52-53, 69-70 | Opaque --paper-raised, 1 px --line, no backdrop-filter, no radial |
| Tour screen under-glow 0/18/40/-24 | tour-screens.css:6, :14 | var(--sh-card) neutral |
| Picked-option glow | tour-screens.css:41 | Volt fill |
| Halo rings | tour-screens.css:131, 144; lab-cinema.css:69 | Plain 8 px ink dot, no ring, no ping |
| ts__ladder li[data-mark=you] | tour-screens.css:191 | Volt fill chip |
| rl__cover-mark and orbit | social-proof.css:14-17 | Removed decoration; monogram in Hanken 700 ink |
| rl__summary glass over glow | social-proof.css:36-37 | Opaque raised surface |
| lcd__frame bezel rings | lab-cinema.css:91-95 | One 1 px --line-strong |
| lcc__chip, lcc__head | lab-cinema.css:188-202 | Neutral |
| lcp-plan__n, __go | lab-cinema.css:289-294 | Ink |
| Theme switch thumb | marketing-theme.css:47-61 | Halo shadows removed; travel easing (.34,1.4,.5,1) becomes cubic-bezier(.22,1,.36,1) at 420 ms; stars and sky kept |
| lp-proof glass and rim | hero-depth.css:35-47 | Hairline row (hero mock-up) |
| lp-stage::before volt radial | home-refinements.css:13-20 | Removed |
| mm-drill card's 1 px volt top line | home-refinements.css:32-35 | Removed |
| Hero and close-band grid, dot matrix, pointer spotlight | HeroBackdrop.jsx, landing.css:234-276 | Removed from the hero; the pointer effect becomes Mobi's gaze; the close band's lp-bg grid and dots become plain --paper-sunken |
| Night-only answer-sheet overlay | HeroRoom.jsx | Fills in graphite #2B2A26, not volt |
| Dead CSS | landing.css:355-363, 553; home-refinements.css:41-42, 49 | Deleted so it cannot return |

The Night room painting's amber lamp is owned art and stays.

Acceptance:
- Re-run slop/capture.mjs and summarize.mjs (390 and 1440, Night and Day) and audit/neon capture:
  - volt text runs in Night at most 1.2 times Day;
  - volt edges on containers 0, with Night volt edges at 390 at most 15 (from 123);
  - coloured glows 0, radial washes 0, content glass panels 0;
  - Night lime-tint mean at 390 at most 1.0% (from 3.70%);
  - animated elements in Night at most Day plus 2 (from 55 against 5).
- The mock-up's Night shots are the visual bar.

## scroll

One gesture is one step, using the bench-proven mechanism from tmp/home-1104/scroll/RESULTS.md §6 (32 of 32 flick cells gave one step at 0 px offset). It goes into ScrollStory.jsx as a small controller with cached geometry. Each rule:

1. Geometry is cached per story: top, hold, steps, and rest(k) = top + round(hold*k/(steps-1)). It is re-measured on ResizeObserver, on visualViewport resize and on contentvisibilityautostatechange, never in the gesture path.
2. Touch: one passive touchstart, passive touchend and touchcancel, and one window touchmove with {passive:false}.
   - It is registered only while a story is within one screen (the existing IntersectionObserver, ScrollStory.jsx:153-156).
   - It calls preventDefault only for an owned gesture: one that started inside a hold, is vertical after 6 px of slop, has a step in its direction, and did not start inside the lock.
   - While owned, the content leans 25% of the finger's travel, capped at 28 px, with a single translate3d.
3. The step commits at touchend from net travel only: 40 px or more, or a 12 px flick at 0.3 px/ms or faster over the last 80 ms. It is never more than one step, and speed never counts beyond that 12 px rule.
4. Lock: 420 ms after a commit (120 ms under reduced motion). Gestures that start inside it are swallowed, not queued.
5. Wheel and trackpad: one non-passive wheel listener. A burst ends after 160 ms of quiet or on a change of direction, and gives at most one step after 12 px. Arrow keys, Page Up/Down and Space step once per press. ctrlKey is ignored.
6. After a step: scrollTo(rest(next), {behavior:'instant'}). The stage is sticky, so the jump is invisible. There is never a glide, so LK47's cause does not come back.
7. Entry and exit clamp: a fling that crosses a story's first rest from above, or its last from below, is held there. Leaving past the last step stays native.
8. Settle: a native scroll that ends inside a hold (scrollend, or a 150 ms fallback) moves to the nearest rest.
9. Visuals are driven by the step: data-step on the story root, with time transitions on transform and opacity only.
   - The outgoing step goes opacity 1 to 0 over 160 ms, ease-out.
   - The incoming step goes opacity 0 to 1 and translateY 12 px to 0 over 320 ms, cubic-bezier(.22,1,.36,1), starting 60 ms later.
   - Progress fills and the Lab object tilt transition over 320 ms on the same curve and are no longer tied to the scroll timeline.
   - React stays out of the per-step path: the stage children are memoised and only the attribute changes.
10. The statement becomes StatementStory, a 3-step held story on phone and desktop. One step per clause, same words:
    - 'Your marks slipped somewhere. MockMob shows you where,'
    - 'picks the chapter for tonight,'
    - 'and keeps your DU shortlist in sight.'
    The active clause is --ink and the others --ink-3, which reads at 4.5:1 or better, never 0.18 opacity. The shelf objects land on step 3 with their existing depth and tilt, now timed (480 ms, cubic-bezier(.22,1,.36,1)).
11. Programmatic jumps (goTo, HashSettle, DemoJump, nav links) call story.arrive(y) first, so they are not clamped.
12. content-visibility reserved sizes are fixed: landing.css:1435 #your-prep 580svh becomes 680svh on phones, and every held section's contain-intrinsic-size is set to its real track. Fresh and warm page height must differ by less than 30 px.

Tests:
- scrollStorySpeed.test.mjs is replaced (rule 14a): only touchmove and wheel are non-passive, preventDefault appears only behind the ownership check, and no overflow:hidden or touch-action:none.
- New scripts/design-audit/one-gesture-gate.mjs runs in real Chrome with CDP Input.dispatchTouchEvent and wheel, against next start, at 390x844 and 1440x900, on all four stories. It covers:
  - the 32 flick cells (4 distances x 4 speeds);
  - slow drags of 40, 120, 150 and 300 px;
  - reversals 100/100 and 300/200;
  - a 20 px nudge;
  - two flicks 150 ms apart and 700 ms apart;
  - an enter flick of 600 px at 6000 px/s from 500 px above;
  - exit flicks in both directions;
  - wheel bursts of 1, 5 and 30 notches and a 60-event tail;
  - reduced motion.
  Each row asserts the exact step and offPx === 0.
- That gate is the L-027, L-028, L-029 and LK69 lock. The owner still sees it live on his phone, and it is checked on one real iPhone and one real Android before shipping.

## examScreen

ExamComparator.jsx is rewritten under the same export and the same #exam-experience id, so page.js does not change for it. It now shows our runner, not an NTA clone.

Head:
- h2: 'The exam screen you'll practise on.'
- Sub (14 words): 'The CUET timer, palette and marking, laid out so nothing gets in your way.'

The preview is built presentationally from the real runner's markup and classes (TestPageClient.jsx:1213-1470) and fixture data. It has no runner logic and is theme-aware: --paper-raised in Day and #1B1A16 at Night, never the always-dark rgb(16,24,15).

Phone (390), one screen, console at most 640 px:
- Header: an exit button, 'Full mock' and 'Accountancy', and the timer pill '47:12' in ink.
- 'Question 12 of 50' and '11 answered', with the progress bar.
- The runner's own offline line: 'Saved on this device. Stay online to submit.'
- The question card, with the chapter chip 'Admission of a partner' and the difficulty chip 'Medium', then the status pill.
- 'Mark' and 'Clear'.
- Four options, one of them struck out. The press-and-hold strike draws over 240 ms when the section enters, once, with the runner's hint 'Press and hold an option to cross it out.'
- Bottom bar: 'Prev', 'Palette', and 'Next', which is volt as the primary.

A segmented switch with two tabs sits above it, 'Question' and 'Review':
- Review shows the runner's Review sheet: Answered 11, Marked 2, Pending 3, Not visited 34, the state-outlined chips and 'Submit'.

Desktop (1440): the question pane and the Review palette side by side, as the runner lays them out. The section is at most 860 px.

The second switch, 'MockMob view / NTA view', is our runner's real interface switch, which keeps the answers and the timer. NTA view is our runner's NTA skin and is labelled 'with Pro' (Smart practice and NTA mode are Pro). The NTA rehearsal stays; it is just not the default and not the section's picture.

Copy check: none of 'Mark for Review & Next', 'Save & Next', 'Clear response' or the NTA five-state legend text appears in MockMob view.

Acceptance:
- Section height at most 1,000 px at 390 (from 1,644) and at most 860 px at 1440 (from 1,363).
- A text search proves those strings are absent in the default view.
- Day background equals var(--paper-raised).
- 0 volt edges.
- Screenshots in Day and Night sit beside audit/shots/runner/390-quick-accountancy-day.png and 1440-nta-mockmob-night.png for a parity check.
- The old .lp-exam rules (home-refinements.css:84-228) are deleted.

## copy

Budgets, locked in landingCopy.test.mjs:
- Every section sub at most 20 words.
- Every tour slide body at most 25 words, with at most 2 points of at most 12 words each.
- No 390 viewport, at any story step, over 60 visible words except the FAQ (counted by a capture script).
- Whole phone page at most 2,100 visible words (from about 3,050).
- W1 'not just' at most 1. W2 staccato clusters at most 1. T6 middle-dot strings 0. T2 kickers 0.

Exact rewrites:
- Hero: see the hero words above. The middle-dot trust line becomes two sentences.
- Lab sub (27 words): 'Your score says how it went. The Lab shows why, minute by minute.'
- Remove the kickers 'Mistake Lab', 'Score Recovery Lab', 'DU Compass' and 'MockMob on Instagram' (page.js:269, 292, 307, 372). The position band still names the held stories.
- Tour sub: 'Everything you get around a mock, one slide at a time.' (This replaces the 'Practise. Replay. Repair.' cluster.)
- Tour Practice body: 'A short drill for a free evening, or a full 50-question, 60-minute mock. Same timer, same palette, same pressure.'
- Tour Repair:
  - title: 'Fix the reason you missed it.'
  - line: 'Fix the reasoning behind a wrong answer'
  - body: 'See why your pick was tempting and where it breaks, written from the official key. If the AI can't match the key, you pay nothing.'
  - points: 'A 10-minute next step', 'Then 5 fresh questions to test the fix'
- Tour Ask Mobi:
  - The second point becomes 'One credit buys a whole Mobi job. Every plan gets 50 free credits a month.'
  - The Sparkles icon is replaced by the owned desk bell (public/brand/mascot/ask-deskbell.webp).
- Tour Mob body: 'Start a Mob, share its code and race your friends on the same five questions for 24 hours. Then fix the one that caught you, together.'
- The tour's '01 / 10' mono counter (FeatureTour.jsx:190) is removed. The progress bar plus the slide name carry position.
- Close h2: 'Try your first five questions.' with sub 'Answer five now. Sign up when you're ready to keep score.' 'Fix it once. Check it holds.' stays as the page's one cluster.
- Lab step bodies: trim to at most 30 words each by moving numbers into the mock screens (labStory.mjs).
- Statement: unchanged words, now in 3 steps.

Every claim is read from CAPABILITIES, OFFER, DU_FACTS or bankStats. No 'illustrative', 'not affiliated' or other sub-remarks (L-024).

## brandSystem

Logo: logo B unchanged, 'mockmob' with Mobi as the second o, plus the volt dot (Logo.jsx: r 90, gap 58). The dot is #9DB400 on Day paper and #D2F000 at Night.

Fonts kept:
- Bricolage Grotesque variable for display.
- Hanken Grotesk for body and all figures, with tabular-nums. Geist Mono leaves the home page: .mm-measure prices, the tour counter and the monogram (T1).
- Literata stays for reading surfaces (Learn) and is not loaded on home.

Type ladder by role, phone / desktop:
| Role | Phone | Desktop | Weight, tracking |
|---|---|---|---|
| display-1 (hero) | 41/1.02 | 66/1.0 | 800, -0.038 to -0.04em |
| display-2 (statement, close) | 34/1.08 | 54/1.04 | 750 |
| h2 | 28/1.12 | 44/1.08 | 700, -0.025em |
| h3 | 20/1.25 | 20/1.25 | 650, -0.015em |
| lead | 17/1.5 | 19/1.5 | Hanken 400, --ink-2 |
| body | 16/1.55 | 16/1.55 | |
| small | 14/1.45 | 14/1.45 | --ink-3 |
| data | | | Hanken 600-700 tabular |

The hero-to-h2 step becomes 1.46x on phones and 1.5x on desktop, against today's 1.2x and 1.04x (all 800).

Colour: the app palette, warm paper and warm charcoal, with volt's three jobs as in the Night section.

Mobi, one finish per surface:
- The rigged vector Mobi in the hero.
- The 5 section seats move from the 7 baked photo-real webp poses to static vector poses generated by scripts/brand/build-mobi-poster.mjs (attentive, pointing, greeting). One render style and one light.
- One Mobi in view (W-074). Each seat points at that section's action.

Illustration: the owned desk-object icons in public/art/icons replace the 14 lucide icons in the tour rail:
- Practice: papers. Mistake Repair: mistakes. Learn: lesson. Replay: revise. Chapter review: questions.
- Ask Mobi: the desk bell. DU Compass: compass. Combo Planner: keycards. Benchmarks: today. The Mob: mob.
- They are drawn at 40 px in a 44 px target, with no tile behind them (L5, I2).
- Controls keep plain ink glyphs.

Motion grammar:
- Ease-out cubic-bezier(.22,1,.36,1) for UI.
- 120 ms press, 200 ms small state, 320 ms step, 480 ms milestone.
- Overshoot only on Mobi.
- No infinite loops except Mobi's breath, one in view.
- Reduced motion: instant changes.

Surfaces: at most 2 nesting levels (section plus product screen). Hairlines are 1 px --line. Shadows use --sh-card, neutral.

## perItem

[
 {
  "item": "LK67 One hero idea on both sizes (Mobi parity)",
  "change": "Both heroes become the same stage: the painted room panel, Mobi standing under the answer sheet turned toward the card, and the live DemoDrill card on his desk. On phones the stage sits below the copy; on desktop it is the right column. HeroMobi gets one variant ('stage') in place of 'room' (phones) and 'host' (desktop). The room is drawn at every width (today it is hidden at 761 px and up). The tap still plays the act cycle and the graphite bubble fill. The 'Tap me' bubble and the six tap-only pitch lines are retired into the lead, facts and typed phrases. Mobi reacts to answers with a fixed-size bubble and glances at the typed line. The pointer spotlight becomes his gaze, the same on touch and pointer.",
  "acceptance": "Playwright at 390 and 1440, Day and Night:\n- .lp-room and .mobi-react are visible at both widths.\n- Mobi's rect sits inside the room rect, and his facing is 'left' at both.\n- Mobi's area is at least 2.5% of the first screen on both (today 7.5% and 1.3%).\n- No element with text 'Tap me' exists.\n- Tapping Mobi changes data-act and fills one .lp-room__dot with graphite #2B2A26.\n- Answering demo question 1 shows one bubble of constant size, 240x56.\n- The screenshots match mock-up v6 composition.\n- The heroScene.test and landingMobi.test assertions are updated to the 'stage' variant.",
  "files": [
   "src/components/landing/HomeHero.jsx (new)",
   "src/components/landing/HeroMobi.jsx",
   "src/components/landing/HeroRoom.jsx",
   "src/components/landing/HeroBackdrop.jsx",
   "src/components/landing/heroTaps.mjs",
   "src/components/landing/heroTaps.test.mjs",
   "src/components/landing/heroScene.test.mjs",
   "src/components/landing/landingMobi.test.mjs",
   "src/app/hero-scene.css",
   "src/app/home-refinements.css"
  ]
 },
 {
  "item": "LK68 Night hero reads as AI slop (neon)",
  "change": "Night tokens move to the app's warm charcoal, and --accent-line becomes neutral. Volt keeps three jobs plus the two headline words the owner asked for. Removed: the hero card's volt top line, the stage's volt radial, the proof glass, the toggle halo, the hero grid, dots and spotlight, and the volt answer-sheet overlay (now graphite). The rest of the page's top 15 offenders are fixed file by file (Night section table).",
  "acceptance": "Run slop/capture.mjs and summarize.mjs on localhost and then production:\n- Night 390 hero viewport: volt text runs 1 ('CUET 2027'), volt container edges 0, glows 0, radial washes 0, content glass 0.\n- Whole Night page: volt text runs at most 1.2 times Day; lime-tint mean at most 1.0%.\n- Audit neon-390-night volt edges at most 15; Night animated elements at most Day plus 2.\n- marketing-theme.test asserts the token values (#12110E, #1B1A16, #F4F0E6, --accent-line #4A453B).",
  "files": [
   "src/app/marketing-theme.css",
   "src/app/marketing.css",
   "src/app/du.css",
   "src/app/feature-tour.css",
   "src/app/compass-ladder.css",
   "src/app/tour-screens.css",
   "src/app/social-proof.css",
   "src/app/lab-cinema.css",
   "src/app/mistake-lab.css",
   "src/app/home-refinements.css",
   "src/app/hero-depth.css"
  ]
 },
 {
  "item": "LK69 Laggy page; one gesture must be one step",
  "change": "ScrollStory gets the bench controller: an owned non-passive touchmove only near a story, a commit at touchend from net travel, a 420 ms lock, wheel bursts, instant scrollTo to the rest, entry and exit clamps, settle, and visuals driven by step. The statement becomes a 3-step StatementStory. Content-visibility reserved sizes are fixed.\n\nPerformance:\n- One scrollBus (a single passive scroll listener plus one rAF, reading only scrollY and cached geometry) replaces ObjectLife's document capture listener and lean loop, PipGuide's per-frame querySelectorAll, checkVisibility and getBoundingClientRect, and SectionPosition's per-frame getComputedStyle.\n- ScrollStory's fitAll moves out of rAF into a batched ResizeObserver callback (reads before writes).\n- React stays out of the per-step path.\n- The MobiReact rig runs only during acts.\n- prefetch={false} on links below the fold.\n- PipGuide hydrates on idle after the first interaction.",
  "acceptance": "The one-gesture-gate.mjs table passes 100% at 390x844 and 1440x900 on all 4 stories, with offPx === 0 on every row. The new source test replaces scrollStorySpeed.test.mjs. Fresh and warm document height differ by less than 30 px.\n\nThe performance budget holds on the audit's lean run (real Chrome, CPU 4x, 22 real-touch swipes to y 9,422):\n- p95 frame at most 20 ms; at most 3 frames over 50 ms; 0 over 100 ms; scroll long tasks at most 4 and at most 400 ms in total.\n- At most 1,200 style recalcs during the run (from 3,978).\n- 8 s idle on the hero: at most 0.6 s task time, at most 5 recalcs/s, 0 rAF callbacks/s after 4 s.\n- TBT at most 250 ms; LCP at most 2.2 s; CLS 0.\n\nThe owner's phone check, plus one real iPhone and one real Android, before shipping.",
  "files": [
   "src/components/landing/ScrollStory.jsx",
   "src/app/scroll-story.css",
   "src/components/landing/scrollBus.mjs (new)",
   "src/components/landing/StatementStory.jsx (new)",
   "src/components/landing/SectionPosition.jsx",
   "src/components/landing/HashSettle.jsx",
   "src/components/landing/DemoJump.jsx",
   "src/components/brand/ObjectLife.jsx",
   "src/components/brand/PipGuide.jsx",
   "src/components/brand/MobiReact.jsx",
   "src/app/landing.css",
   "src/app/hero-depth.css",
   "src/components/landing/scrollStorySpeed.test.mjs (replaced by oneGesture.test.mjs)",
   "scripts/design-audit/one-gesture-gate.mjs (new)"
  ]
 },
 {
  "item": "LK70 The phone first screen must say what MockMob is",
  "change": "The copy now comes first, and the room moves below it at 268 px tall (it was 320 px above the H1). The H1 is a sentence that names the product and the exam: 'CUET 2027 mocks that find your weak chapter.' The lead says how: a fresh bank, the real timer, where each mark went. The key comes before any decoration.",
  "acceptance": "At 390x844, 375x667, 360x640 and 412x915:\n- The H1 top is at or below 12% of innerHeight.\n- The words 'CUET', 'mocks' and the lead's first sentence end inside the top 40%.\n- The primary key's bottom is at or below 50% (390x844: H1 at y 88 and key bottom at 384, measured on the mock-up).\n- No decorative element starts above the key.\n- Mobi is still on the first screen at 390x844 (top at y 619 or less).",
  "files": [
   "src/components/landing/HomeHero.jsx (new)",
   "src/components/landing/heroLines.mjs",
   "src/app/hero-scene.css"
  ]
 },
 {
  "item": "LK71 AI-slop traits and text walls; page too long",
  "change": "Apply the copy budgets and rewrites: kickers 0, middle dots 0, at most 1 'not just', at most 1 staccato cluster, no mono counter, tour bodies of at most 25 words, Lab bodies of at most 30. Numbers move into the mock screens. The exam section shrinks by about 640 px on phones. No section, story or animation is removed.",
  "acceptance": "landingCopy.test.mjs enforces every budget against page.js, the labStory and TOUR data. A capture script counts visible words per 390 viewport at each story step: none over 60 outside the FAQ, and at most 2,100 in total. Run slop capture: T2 0, T4 0, T6 0, W1 at most 1, W2 at most 1. The section list matches production (L-004).",
  "files": [
   "src/app/page.js",
   "src/components/landing/labStory.mjs",
   "src/components/landing/LabCinema.jsx",
   "src/components/landing/MistakeLab.jsx",
   "src/components/landing/FeatureTour.jsx",
   "src/components/landing/landingCopy.test.mjs"
  ]
 },
 {
  "item": "LK72 The exam section is too tall and an NTA copy",
  "change": "ExamComparator becomes a theme-aware picture of our runner, built from TestPageClient's own pieces:\n- the header, the offline line, the chapter and difficulty chips, Mark and Clear, the press-and-hold strike-out, and Prev, Palette and Next;\n- the Review tab with its four counters;\n- the real interface switch, with NTA view labelled 'with Pro'.",
  "acceptance": "Section height at most 1,000 px at 390 and at most 860 px at 1440. No 'Save & Next', 'Mark for Review & Next', 'Clear response' or NTA legend text in the default view. Day background equals var(--paper-raised). 0 volt edges. Day and Night screenshots are checked against the audit's runner shots. The .lp-exam CSS is deleted.",
  "files": [
   "src/components/landing/ExamComparator.jsx",
   "src/app/exam-screen.css (new)",
   "src/components/landing/examScreen.test.mjs (new)"
  ]
 },
 {
  "item": "LK73 Own brand identity (illustration, type hierarchy, consistent Mobi); keep fonts and logo",
  "change": "The app palette and the type ladder by role. Geist Mono is off home. One Mobi finish (vector) with one role per seat. Owned desk-object icons replace lucide in the tour rail, and Sparkles goes. Logo B plus the volt dot are unchanged. The motion grammar is written down once.",
  "acceptance": "Run getComputedStyle checks: h1/h2 size ratio at least 1.4 at both widths, and no element on home uses Geist Mono. No lucide or Sparkles import in page.js. The 5 MascotSeat elements render the vector poster (img of brand/mascot/*.webp count 0 on home). The logo SVG has the dot circle. Identity with the logo hidden: the room, Mobi, the answer sheet and the CUET wording are present in the first screen (12-part test item 1).",
  "files": [
   "src/app/marketing.css",
   "src/components/brand/Mascot.jsx",
   "scripts/brand/build-mobi-poster.mjs",
   "src/app/page.js (TOUR icons)",
   "src/components/landing/FeatureTour.jsx"
  ]
 },
 {
  "item": "LK74 Preparoo-level loader and typing",
  "change": "BrandOpening: the app's 'mo' unfold, 1,280 ms, first visit only, any input skips it, and the wordmark hands off into the site bar. HeroTypeLine: one typed round of three true phrases, with a reserved width, a crisp letter entry, a caret that blinks twice per hold and then hides, a pause off-screen, and reduced motion static.",
  "acceptance": "The loader filmstrip assertions and the typing assertions (CLS 0 over 14 s, the mid-word frame, at rest after one round), as in those sections. heroLines.test is updated so L-016 holds and the old static-H1 lock is replaced. brandOpening.test asserts the skip rules (repeat visit, reduced motion, hash, same-origin referrer) and an inline weight of at most 4 KB.",
  "files": [
   "src/components/landing/BrandOpening.jsx (new)",
   "src/app/brand-opening.css (new)",
   "src/components/brand/logoLetters.generated.js (new)",
   "scripts/brand/build-logo-letters.mjs (new)",
   "src/components/NavBar.jsx",
   "src/components/landing/HeroTypeLine.jsx (new)",
   "src/components/landing/heroLines.mjs",
   "src/components/landing/heroLines.test.mjs",
   "src/components/landing/brandOpening.test.mjs (new)"
  ]
 },
 {
  "item": "LK75 Refine it ourselves, thought through",
  "change": "Every move above is a refinement of something that exists (the room, Mobi, the taps, the scrub, the NTA view, the proof row), with numbers from the three investigations. No new art and no video. The L-001..L-045 gate runs with tests named per L item.",
  "acceptance": "The full gate passes, with each L item named in a test or a capture check: L-016 typing, L-017 'CUET 2027' colour, L-019 glow counts, L-027 to L-029 the gesture gate, L-031 eye line, L-040 performance budget, L-043 loader. The anti-slop 12-part test scores 2 on items 1-5, 9, 10 and 12. Screenshots at 390 and 1440, Day and Night, are reviewed before deploy.",
  "files": [
   "data/tests/release9_public_1018.test.mjs",
   "scripts/design-audit/one-gesture-gate.mjs (new)"
  ]
 }
]

## mockup

{
 "html": "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/hero.html (built from hero.src.html by build-and-shoot.mjs. It inlines the real logo B (public/brand/logo-header-*.svg) plus the volt dot, and the real Mobi poster SVG (mobiPoster.generated.js) with mobi-figure.css. It uses the self-hosted Bricolage and Hanken woff2 and the real room paintings, scene-welcome-band-night and scene-empty-allclear-day. Open it with ?t=day|night and &s=hero|loader.)",
 "shots": [
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/shots/v6-390-day-hero.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/shots/v6-390-night-hero.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/shots/v6-1440-day-hero.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/shots/v6-1440-night-hero.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/shots/v6-390-day-loader.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/shots/v6-390-night-loader.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/shots/v6-1440-night-loader.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-feel/shots/v1-390-night-hero.png"
 ],
 "selfCritique": "I built and looked at six versions; v1 and v6 are kept for comparison. The browser lock was taken and released for each burst.\n\nFixes:\n- v1: Mobi fell below the fold on the phone, which fails LK70's 'keep Mobi'. The lead was 4 lines with an orphan word. The logo had lost its volt dot, and the loader frame had no dot either. On desktop, Mobi stood half outside the room.\n- v2: Mobi moved into the room. The copy was tightened to a 3-line lead. The dot was restored from Logo.jsx geometry. But the desktop card covered the answer sheet, and the balanced facts line split as '₹99 a / month'.\n- v3: Mobi moved under the answer sheet, facing the card. The card moved to the left of the desk. The facts became two sentences on two lines.\n- v4: The desktop secondary key was aligned with the primary. The two hero links were added under the facts on desktop, so they are kept, not cut. The dot clipped at the viewBox edge, fixed in v5.\n- v6: The phone card became full width, with Mobi's feet on its top edge, so the real options get the full 350 px.\n\nSlop checklist on v6:\n\n| Tell | Count |\n|---|---|\n| C1 volt text | 1 ('CUET 2027') |\n| C2 container edges | 0 |\n| C3 glows | 0 (Mobi's own screen halo is his signature) |\n| C4 radials | 0 |\n| C5 lit edges | 0 |\n| C6 grid or dots | 0 |\n| C7 content glass | 0 |\n| C8 status dots | 0 |\n| T2 kickers | 0 |\n| T5 hero-metric type | 0 (20 px proof labels, no count-up) |\n| T6 middle dots | 0 |\n| W2 staccato | 0 in the hero |\n\nL1 passes: the H1 is at 10.4% and the key ends at 45%. L2 passes: the same idea on both sizes.\n\nStill imperfect:\n- At Night, Mobi's antenna bulb sits over a painted volt bubble on the sheet. Hero volt count: logo dot, 'CUET 2027', key, plus the owned painted bubbles and Mobi.\n- The painting's own volt bubbles add accent on Night. They are owned art, so I kept them.\n- The desktop left column has about 70 px of air under the links.\n- The mock-up shows only Mobi's still poster pose, not his acts, and a simplified theme switch. Production keeps the sky switch minus the halo.\n- The loader shots show the composed frame at 1000 ms only, not the unfold.\n- '₹99', '5,765' and '73' are hard-coded here; production reads OFFER, bankStats and DU_FACTS.\n- The proof row is still a 4-cell row under the hero (L3 tell). I kept it because each cell is a link to its section. A judge could fairly ask to fold it into the links row."
}

## keepsAndNeverCuts

Nothing below is cut. It is refined or kept as it is.

Sections and stories:
- All 14 sections plus the footer, in the same order.
- The three held stories: the Lab (4 steps), the tour (10) and the Recovery Lab (4).
- The statement, now 3 steps with the same words.

Animations and art:
- The shelf objects landing.
- The hero room painting (Day and Night), now on desktop too.
- Mobi's taps and act cycle, and the Night bubble fill (now graphite).
- The 3.5 s look-down and the buzz.
- Mobi seats in 5 sections (now one vector finish).
- The theme switch's sun, moon and stars (minus the halo).
- SceneLife's one breath.
- The LiveStatsBand.
- The creator reels.
- The DU tools and the Combo Planner.
- The Compass Pro and Combo asides (now opaque).

Exam and pricing:
- The NTA view in the exam section (now behind our runner's real switch).
- The pricing cards and the FAQ.

Hero:
- The proof row (now calm).
- The hero links.
- The dock gate and MobileDock with state-aware labels (L-006 to L-010).

Converted, not removed:
- The pointer spotlight becomes Mobi's gaze.
- The six tap lines move into the lead, facts and typed phrases.
- The speech bubble becomes a fixed-size reaction after the first answer.

Brand and rules:
- Fonts kept: Bricolage, Hanken, Literata.
- Logo B and the volt dot kept.
- The approved copy kept where it is within budget: 'Every mark, traced back to a moment.', 'Fix it once. Check it holds.', 'What's inside MockMob' with MockMob in green.
- Mobile-first: every hero element is measured at 390 first.
- No glow, sheen, light running round edges, drifting blobs or gradient text. The only gradient anywhere is none (the mock-up's phone scrim was removed in v2).
- No sub-remarks or disclaimers.
- Truth comes from the capability gates.
- The USP sits in the lead and the facts, not as a banner.

## risks

1. Rulings that changed:
   - L-043 asks that a logo opening last about 3 s. I propose 1.28 s (the app's warm open; the 3 s is the app's first install). The owner should choose. The duration is one token, --open-total.
   - heroLines.mjs records a 1 Nov 'R3 H1' ruling that the headline is static. LK74 (4 Nov) asks for refined typing like Preparoo, and L-016 asks for a visibly changing word. Newer words win, but this reverses a ruling: record his verbatim agreement or show it to him live.
2. Scroll on real devices:
   - LK47 (2 Nov, 'it raced') against LK69 and L-027 (one gesture, one step). The controller never glides, but he must feel it on his phone.
   - iOS Safari and a real Android are untested (bench R1 to R3). A non-passive touchmove can lag on a janky main thread, so the performance packet should land first or together with it.
3. LCP: the room painting is now on the first screen at every width and is larger than the H1, so it becomes the LCP element. It must load eagerly with fetchpriority high and stay at most 40 KB AVIF for the active theme only. A full-screen loader over the H1 could also shift LCP; measure it with ?open=off.
4. Things that could read as cuts or changes to approved work:
   - Moving the statement from a scrub to 3 steps, and dropping the hero grid, dots and pointer spotlight, could read to him as 'removed animations' (L-005). Each is converted, and the change log must say so.
   - Moving the 5 Mobi seats from photo-real poses to vector poses changes art he called good ('Mobi is good'). It can be gated behind a flag and shown first.
5. Palette reach: the Day and Night token change is scoped to .mm, so it repaints every public page (pricing, DU tools, sign-in). Those pages need a Day and Night screenshot pass before deploy.
6. Truth: check 'second guesses' against the capability gates. Changed answers are free in the Lab and Replay, but the 'Full chapter review' pace and changed-answer detail is Pro. If Free does not show changed answers after a mock, swap that phrase for 'slow questions.'
7. Tests that must be rewritten on purpose, not deleted:
   - release9_public_1018.test (hero grid and dots must stay);
   - heroLines.test (static H1);
   - scrollStorySpeed.test (no preventDefault).
8. Merge order: the six packets avoid shared files, but page.js assembly (packet 5) depends on the HomeHero, BrandOpening, StatementStory and exam exports landing first. Merge order: tokens, then the hero, loader, exam and scroll packets, then assembly.
9. Two hero CTAs (key plus text button) stay as today, which slightly dilutes one primary action. The secondary is text-only to keep the hierarchy clear.

## buildPackets

[
 "P1 Hero stage and typed line (Opus for taste, Sonnet if this spec is followed exactly). Files:\n- new src/components/landing/HomeHero.jsx (the hero section, lifted from page.js:172-245, with props offer, duFacts, bankLine);\n- new src/components/landing/HeroTypeLine.jsx;\n- src/components/landing/heroLines.mjs and heroLines.test.mjs;\n- src/components/landing/heroTaps.mjs and heroTaps.test.mjs;\n- src/components/landing/HeroMobi.jsx ('stage' variant, glance and gaze, fixed bubble, rig only during acts at the hero level);\n- src/components/landing/HeroRoom.jsx (all widths, graphite fill);\n- src/components/landing/HeroBackdrop.jsx (retired from the hero);\n- src/app/hero-scene.css;\n- src/app/home-refinements.css (delete the stage radial, the card top line, the dead CSS, and the .lp-exam rules at 84-228);\n- heroScene.test.mjs, landingMobi.test.mjs, and the hero assertions in data/tests/release9_public_1018.test.mjs.\nDone when: the v6 mock-up composition is reproduced at 390 and 1440 in Day and Night, and the LK67, LK70 and typing acceptance checks pass.",
 "P2 Entry loader (Sonnet). Files:\n- new src/components/landing/BrandOpening.jsx, with its inline pre-paint skip script;\n- new src/app/brand-opening.css;\n- new scripts/brand/build-logo-letters.mjs and src/components/brand/logoLetters.generated.js (per-letter paths from the app's logo_geometry.g.dart);\n- src/components/NavBar.jsx (data-open-target on the logo, visibility handshake);\n- new src/components/landing/brandOpening.test.mjs;\n- new scripts/design-audit/opening-filmstrip.mjs.\nDone when: the filmstrip at 0, 600, 1000 and 1300 ms matches the spec, repeat visits, reduced motion, hash and same-origin referrer skip it, CLS is 0, and the LCP delta is at most 150 ms.",
 "P3 Night de-neon and brand tokens (Sonnet). Files:\n- src/app/marketing-theme.css (Night and Day tokens, toggle halo and easing);\n- src/app/marketing.css (tokens, and .mm-measure moves to Hanken tabular);\n- colour rules only in: src/app/du.css, feature-tour.css (active tab, mono counter style), compass-ladder.css, tour-screens.css, social-proof.css, lab-cinema.css (91-95, 188-202, 289-294, 69), mistake-lab.css;\n- hero-depth.css's lp-proof block (35-66) only;\n- a new marketing-theme.test.mjs that pins the tokens.\nDo not touch scroll-timeline rules. Done when: the slop and neon capture targets in the Night section pass at 390 and 1440, and contrast is at least 4.5:1 for every ink role on each ground.",
 "P4 One gesture, one step, plus scroll performance (Opus: the hardest correctness work). Files:\n- src/components/landing/ScrollStory.jsx and src/app/scroll-story.css (the bench controller, rules 1-13);\n- new src/components/landing/scrollBus.mjs;\n- new src/components/landing/StatementStory.jsx (the 3 steps), with hero-depth.css statement rules (lines 90-210);\n- src/components/landing/SectionPosition.jsx and sectionPositionPhase.mjs;\n- HashSettle.jsx and DemoJump.jsx (story.arrive);\n- src/components/brand/ObjectLife.jsx, PipGuide.jsx and MobiReact.jsx (rig frame loop only during acts);\n- src/app/landing.css (contain-intrinsic-size fixes, and deleting dead lp-pill, marquee and lp-bg grid/dots CSS);\n- replace scrollStorySpeed.test.mjs with oneGesture.test.mjs;\n- new scripts/design-audit/one-gesture-gate.mjs (CDP touch and wheel table) and perf-gate.mjs (the audit's lean run).\nDone when: the gate passes 100% at 390 and 1440, the performance budget holds at 4x CPU, fresh and warm height differ by under 30 px, and it has been tried on a real Android plus an iPhone.",
 "P5 Copy, page assembly and brand icons (Sonnet). Files:\n- src/app/page.js: swap in HomeHero, BrandOpening and StatementStory; import the new CSS; copy rewrites; kickers removed; TOUR icons become owned desk objects; Sparkles removed; close h2; close band lp-bg markup removed;\n- src/components/landing/labStory.mjs, LabCinema.jsx and MistakeLab.jsx (body trims);\n- src/components/landing/FeatureTour.jsx (no '01 / 10', icon images);\n- src/components/brand/Mascot.jsx and scripts/brand/build-mobi-poster.mjs (vector seat poses, behind a flag);\n- src/components/landing/landingCopy.test.mjs (budgets);\n- new scripts/design-audit/words-per-viewport.mjs.\nLands last. Done when: the copy budgets pass, the section list equals production, and slop T2, T4, T6, W1 and W2 pass.",
 "P6 Real exam screen (Sonnet, with the runner open beside it). Files:\n- src/components/landing/ExamComparator.jsx (same export and id; a presentational runner preview with fixture data, Question and Review tabs, and the MockMob/NTA switch);\n- new src/app/exam-screen.css;\n- new src/components/landing/examScreen.test.mjs.\nRead-only reference: src/app/test/TestPageClient.jsx:1213-1470. Done when: the section is at most 1,000 px at 390 and at most 860 px at 1440, there is no NTA button vocabulary in the default view, it is theme-aware, and the screenshots are checked against audit/shots/runner/*."
]

## evidenceIds

[
 "T002",
 "T003",
 "T005",
 "T007",
 "T008",
 "T009",
 "S014",
 "S015",
 "S016",
 "S017",
 "S018"
]

## performance

Budget for a mid-range Android, using the audit's lean run as the lab proxy: real Chrome, CPU 4x, 390x844, 22 real-touch swipes to y 9,422.

| Measure | Today | Target |
|---|---|---|
| FCP | 888 ms | 1.0 s or less |
| LCP (the room AVIF, now eager and high priority) | 2,944 ms | 2.2 s or less |
| TBT | 536 ms | 250 ms or less |
| CLS | 0 | 0 |
| Scripts | 327.9 KB | 290 KB or less (drop 14 lucide icons and HeroBackdrop; PipGuide on idle; prefetch off below the fold) |
| DOM nodes | 3,566 | 3,000 or fewer |
| Scroll p95 frame | 24 ms | 20 ms or less |
| Frames over 50 ms | 23 | 3 or fewer |
| Frames over 100 ms | 12 | 0 |
| Scroll long tasks | 2.6 s | 400 ms or less, 4 tasks at most |
| Style recalcs during the run | 3,978 | 1,200 or fewer |
| Idle hero, 8 s: task time | 5.5 s | 0.6 s or less |
| Idle hero: recalcs | 73/s | 5/s or fewer |
| Idle hero: rAF after 4 s | 52/s | 0 |

The style-recalc cut comes from step-driven visuals in place of scroll timelines and from the rig at rest. Mobi idle becomes a static poster plus one compositor-only CSS breath, paused off-screen.

Levers, in order of the audit's cost ranking:
1. One scrollBus in place of ObjectLife's capture listener and lean rAF (3.3 s self).
2. PipGuide: IntersectionObserver plus cached rects in place of per-frame querySelectorAll, checkVisibility and getBoundingClientRect (about 4.1 s).
3. ScrollStory fitAll moves out of rAF into a batched ResizeObserver (118-158 ms frames), and SectionPosition stops calling getComputedStyle per frame.
4. React out of the per-step path (108-116 ms renders).
5. Link prefetch off below the fold (280 ms LoAF).
6. 52 scroll and view-timeline animations replaced by data-step transitions.

The loader and the typed line cost only transform and opacity, under 3 KB inline.

Verify with scripts/design-audit/perf-gate.mjs, a copy of audit/data/perf3-lean, on localhost and then production. A real-device trace on the owner's phone decides whether it ships (L-040).

