## id

brand

## title

Desk Light: one MockMob hero built around Mobi's lamp-lit desk (brand-first proposal for LK67-LK75)

## thesis

The page reads as AI slop because its brand pieces (Mobi, the painted room, the volt, the fonts) appear as separate effects instead of one system. On phones the painted room is a toy stage above the pitch. On desktop Mobi is a 117x140 host stuck in a gutter. Night lights every edge in volt on a green-black that no MockMob product uses. Desk Light turns them into one system. Every surface is the app's own warm charcoal or cream. The only light is the painted lamp. Volt is a fill (the key, Mobi, the logo dot) plus the one brand word "CUET 2027." Mobi is one character with one finish (the rigged vector figure the app paints) and six poses, each with a job.

The hero is the same idea at both widths: the words first, then Mobi standing in his lamp-lit room and handing you the real first question. The pitch moves out of tap-only bubbles and into a typed headline plus one plain sentence saying what MockMob is. Phone and desktop differ only in arrangement (stacked versus two columns), never in story. Around this:
- the app's "mo" opening becomes the site's entry loader;
- the headline types once, Preparoo-level crisp, and rests;
- one gesture is one step in every held story;
- the exam section becomes a picture of our real runner instead of an NTA clone;
- copy is cut to budgets, with numbers moved into the mock screens.

Nothing is removed: every section, story, showcase, animation and Mobi seat stays. Where a decoration goes, the reason is named (for example the hero grid and the pointer spotlight: slop C6 and M7, LK68).

## hero

{
 "phone": "One column, 20 px side gutter. Numbers are measured on the mock-up at 390x844, with document width 390 (no sideways scroll).\n\n- **Site bar**, 0-60. The logo B wordmark is 26 px tall. Theme toggle and menu sit on the right. No volt key in the bar while the hero key is in view (W-075: one volt primary per viewport).\n- **h1**, 82-211. It starts at 9.7 % of the screen, so \"CUET 2027.\" is on the first tenth.\n  - Bricolage 800, 44/0.98, -0.035 em, 3 lines.\n  - Line 1 \"CUET 2027.\" uses the new --brand-word token (#D2F000 Night, #526700 Day; L-017).\n  - Line 2 is static. Line 3 is the typed slot.\n- **Lead (the pitch sentence, LK70)**, 227-301, ending at 35.7 %. Hanken 17/1.45, colour ink-2, max 34ch. The first clause is in ink at weight 650.\n- **Primary key**, 319-375. Full width, 56 px, radius 16. Volt fill, volt-ink text, Bricolage 750 17. Owned keycap edge 0 4px 0 #9DB400, no glow.\n- **Quiet text link** \"Start free practice\": a 44 px target, underlined in line-strong.\n- **Two fact lines**, Hanken 14/1.5, ink-3, no middle dots (T6).\n- **The desk**, from 499:\n  - The room is 358x212 (`--desk-h: clamp(10.5rem, 25svh, 13.25rem)`), radius 22 22 0 0. Night uses scene-welcome-band-night at object-position 62% 92%. Day uses scene-empty-allclear-day overscanned to 118 % so its feathered edges never show.\n  - Mobi is 112x134 standing in the lamp pool at the left, at room bottom +10.\n  - His bubble (Hanken 600 14, raised paper, 1 px line-strong, radius 16 16 16 4, nowrap) sits on the floor to his right: \"Your first question. Go.\"\n  - The real sample card (DemoDrill) attaches to the room's bottom edge at 710 and shows its head row and stem on the first screen.\n\nResult: the text block is 0-56 %, Mobi and the room 59-84 %, the card from 84 %. Today the room takes 45 % before the h1. On 360x640, CUET is at 13 % and the lead and key are fully on screen; Mobi falls just below the fold there, and the room clamp shrinks it to 168 px.",
 "desktop": "Container max 1200, padding 32. Grid `minmax(0,1fr) 520px`, gap 72, align-items center. Measured at 1440x900:\n\n- **Left column:**\n  - h1 207-447: Bricolage 800, 84/0.95, -0.04 em. The hero is now 1.46x the section h2 (57.6), not 1.04x as today.\n  - Lead 473-563: 20/1.5, max 33ch.\n  - CTA row at 591: the key is 58 px tall with 28 px padding, then the text link.\n  - Facts: 15 px.\n- **Right column, the same desk as the phone:**\n  - Room 520x318, radius 28 28 0 0, y 108-426.\n  - Mobi 150x180, standing in the lamp pool at x 846.\n  - Bubble 16 px on the floor to his right, \"Your first question. Go.\".\n  - The sample card is attached below, y 425-839. Its stem is set in Literata 600 23/1.32 (the printed-paper voice); options are Hanken 600 16 with tabular letter chips (no Geist Mono).\n- **Second beat** (lp-proof), just below the fold. A 1 px hairline row of four sentence links (bold Bricolage 700 17 title plus a Hanken 15 line), with no glass, no tiles and no big numbers (slop C7, T5, L3). The four facts are unchanged: five free questions, 73 DU programmes, two exam screens, 60 min / 50 questions.\n- **Site bar:** the \"Start free\" key becomes a raised-paper secondary while the hero key is visible, and turns volt only after the hero key leaves the viewport (one volt key per viewport).\n- **Removed from the hero:** the HeroBackdrop grid, the dot matrix and the pointer-lit volt spotlight. They are generic tech patterns that exist only on desktop (C6, M7) and are part of the Night neon read (LK68).",
 "mobi": "**One character, one finish, one role in the hero.**\n\n- **Finish.** The rigged vector Mobi (MobiReact and MobiFigure, the web twin of the app's painter) is used everywhere on the home page.\n  - Live in the hero only.\n  - Everywhere else as static SVG poses generated from the same rig. A copy of scripts/brand/build-mobi-poster.mjs with live:false and settledPose(act) already produces them; see tmp/home-1104/design-brand/poses/*.svg and shot-poses.png.\n  - The 7 baked photo-real webp poses leave the home page (they stay in public/ for OG images and the app). This ends the two-finish, two-scale mix the brand audit found.\n- **Six poses with jobs** (pose names are the rig's acts):\n  - hello: opening hand-off and hero load.\n  - point: when the sample card enters view, he points at its first option.\n  - think: Mistake Lab seat.\n  - read: holds the OMR answer sheet. Used for the tour and the exam section, and is the brand signature pose.\n  - encourage: Score Recovery seat, and the sample's wrong answer.\n  - cheer: after the 5th sample answer and in the close band.\n- **Hero behaviour, the same at both widths:**\n  - Load: the hello act runs once at the opening hand-off, then idle.\n  - Card in view: one nudge or point.\n  - Sample answered: correct plays the correct act, a miss plays encourage.\n  - Five answered: cheer.\n  - Tap or click: one reaction act (hop, then tilt, then startle, never the same twice; the existing cycle). The bubble does NOT change on taps.\n  - Bubble lines come only from the sample's state, each at most 44 characters:\n    - load: \"Your first question. Go.\"\n    - right: \"Right. The why is under it.\"\n    - miss: \"Close one. Read the why.\"\n    - after five: \"That's five. Pick your subject next.\"\n  - The six pitch lines retire. Their facts now live in the lead, the typed line and the bank line.\n  - Night's painted answer sheet fills one volt bubble per sample answer, not per tap, so the room's mechanic now means something.\n- **Scale rule.** In the hero, Mobi's height is 1.0 to 1.05x the h1's line-3 height times 3: 134 px on phones, 180 px on desktop. Seats are 96 px on phones and 120 px on desktop.\n- **Other rules kept:** one Mobi in view (W-074); his speech is sentence case, never a price, never hype.\n- **Logo link.** The logo's Mobi (the second o) is the same character. When the hero Mobi waves at the hand-off, the bar logo's Mobi blinks once (the existing 160 ms blink).\n- **Perf.** The rig runs requestAnimationFrame only during an act. Idle becomes a CSS breathe (transform scale 1 to 1.012, 3.6 s, on the compositor) and a CSS blink every 4.2 s. This removes the measured 52 rAF/s and 73 style recalcs/s at idle.",
 "words": "**Exact hero copy.**\n\nThe h1 DOM sentence (visually hidden span, read by screen readers and search; the LCP text is the same server HTML) is \"CUET 2027. One mock. Know what to fix.\" It is unchanged, HERO_SENTENCE in heroLines.mjs.\n\nVisual lines:\n1. \"CUET 2027.\" in the brand word colour.\n2. \"One mock.\"\n3. The typed slot, aria-hidden. It is server-rendered as \"Know what to fix.\", then types the phrases once:\n   1. \"Fresh every time.\": every mock is built fresh from one live bank, which is the USP said quietly.\n   2. \"Every mark traced.\": the Lab review.\n   3. Rests on \"Know what to fix.\"\n\nEach phrase is at most 18 characters, so it fits 358 px at 44 px.\n\n**Lead (new, LK70):** \"MockMob is CUET UG mock tests with a review that finds the chapter behind every mark you lose.\" That is 18 words, with \"MockMob is CUET UG mock tests\" in ink at weight 650.\n\n**Primary key:** \"Try five questions\" (unchanged; L-008 state labels still apply). **Second action:** \"Start free practice\" (unchanged, text link).\n\n**Facts:**\n- Line 1: \"Free to start. Pro ₹99 a month, cancel anytime.\" Built from heroTrustSegments(priceLine(OFFER)) joined as a sentence, not with middle dots. The one-time variant reads \"...no auto-renewal.\"\n- Line 2: heroBankLine: \"One bank of 5,765 questions. No cap on Pro.\" (live count).\n\n**Desk bubble:** \"Your first question. Go.\"\n\n**Card:**\n- Head: \"English\" and \"1 of 5\" as two spans with a 10 px gap (no middle dot).\n- Note: \"No signup for these five. Other subjects? Pick yours free\", where the last three words link to /signup. This merges the two old notes and keeps the L-015 path.\n\nThe recoveryReleased() branch keeps its own words and gets the same layout."
}

## loader

**The site's opening is the app's own \"mo\" opening** (brand_opening.dart:55-110; BRAND.md 1.4). It is not a new invention and not a Preparoo copy. Preparoo's is a black splash with an 800 ms zoom-in (cubic-bezier .16,1,.3,1) and a 750 ms lift (inOutCubic) after 600 ms.

**Component.** New `src/components/landing/OpeningMo.jsx`, a server component.

- **Markup:** a fixed layer `.mo-open` (z-index 90, inset 0, background #12110E in both themes, the app's opening ground) holding one inline SVG wordmark built from per-letter paths.
- **Per-letter paths:** a new generated `src/components/brand/logoLetters.mjs`. It is split from logoB.js using the pen positions `letterX = [0, 865, 1445, 1968, 2549, 3423.22, 3987.35]` and Mobi index 5 from logo_geometry.g.dart:132-265, by a new script, scripts/brand/split-logo-letters.mjs.
- **Run gate:** a 0.3 KB inline script placed before the layer sets `html[data-opening]`:
  - 'first' when localStorage mm-opened is absent;
  - 'short' on a new session (sessionStorage absent);
  - 'skip' otherwise, on reduced motion (device setting or the student's own data-motion switch), and on hash or deep entries.
  - Every storage access is wrapped in try/catch; on a storage error it falls back to 'short'.
- **Animation:** pure CSS keyframes on transform and opacity only, so it runs without hydration. It ends on `visibility:hidden` with fill-mode forwards, so it can never become a stuck invisible layer (slop list item 17). React removes the node at 1400 ms.

**Timeline, ms from first paint ('short'):**

| Time (ms) | What happens |
|---|---|
| 0 | \"mo\" (the m plus Mobi) centred at 2.2x the final size. The other letters sit at scaleX 0 on their shared-edge hinges. |
| 150 | Mobi blinks: eyes scaleY 1 to 0.1 to 1, 160 ms. |
| 320-520 | The empty answer-bubble right eye inks from its centre (scale 0 to 1, 200 ms, cubic-bezier .23,1,.32,1). |
| 500-1000 | Camera pull-back: the group scales 2.2 to 1 on cubic-bezier .5,0,.15,1, interpolated on a log scale as in the app. |
| from 520 | The letters unfold, nearest first, 40 ms stagger, each 300 ms on cubic-bezier .34,1.36,.64,1. This spring overshoot is allowed because it belongs to the logo character, not to chrome (M3). Each letter is hidden until 12 % open. |
| 1000 | Word composed. This is the last frame, see the mock-up shots. |
| 1000-1280 | Hand-off: the word FLIPs to the site-bar logo's rect (translate plus scale, 280 ms, cubic-bezier .23,1,.32,1). Meanwhile the ground fades out with a 4vh lift between 1080 and 1280, revealing the hero, which has been painted underneath since 0 (LCP is the server h1). |
| 1280 | The hero Mobi plays hello and the typed line starts. |

**Variants:**
- 'first': holds the composed word for 320 ms with a 3 % breath and one Mobi glance. Total 1,600 ms.
- 'skip': no layer.
- Reduced motion: no layer. The page fades in over 160 ms.

**L-043** says \"about 3 s\". The app's first install runs 3.0 s, but on the web that would hold the LCP and the key behind a curtain for every new visitor. The proposal is 1.6 s first ever and 1.28 s per new session. This must be reconciled with him (see risks); OPENING_FIRST_MS is one constant.

**Acceptance (tests plus shots):**
- The layer is present in the server HTML; computed visibility is hidden after 1.4 s.
- `elementFromPoint` at the key's centre returns the key at 1.5 s.
- No opening on a second load in the same session, and none under reduced motion.
- A filmstrip at 100 ms steps at 390 and 1440 (Night and Day) shows the mo, ink, unfold, composed and lift frames.
- LCP ≤ 2.5 s at 4x CPU, and CLS 0.

## typing

**Component.** New `src/components/landing/HeroTyped.jsx` (client) replaces the static third run in page.js. heroLines.mjs gains `HERO_TYPED = ['Fresh every time.', 'Every mark traced.']` and keeps HERO_LINES and HERO_SENTENCE.

**DOM:**
- The h1 holds a visually hidden span with HERO_SENTENCE, plus the visual lines marked aria-hidden.
- Line 3 is a CSS grid cell. Every phrase is stacked in it with visibility hidden, as a sizer, so the box is always the widest phrase (CLS 0). The live text sits over it.
- The server renders \"Know what to fix.\", so no-JS, crawlers and LCP see the approved sentence.

**Sequence**, starting at the opening hand-off (1,280 ms) or 600 ms after paint when the opening is skipped:
1. Select-back: a wash of `color-mix(in srgb, var(--ink) 14%, transparent)` grows from the line's end to its start over 220 ms, followed by a 100 ms beat.
2. Clear.
3. Type \"Fresh every time.\": 34 ms per letter, +24 ms after a space, +70 ms before the full stop. Each letter fades in from opacity 0 and translateY .06em over 60 ms (cubic-bezier .23,1,.32,1).
4. Hold 2,200 ms.
5. Select-back and clear, then type \"Every mark traced.\". This is the mock-up's mid-word frame, \"Every mark tra|\".
6. Hold 2,200 ms.
7. Select-back and clear, then type \"Know what to fix.\" and rest for good.

**Caret:**
- A solid ink bar, 0.075 em wide and 0.78 em tall, never volt.
- Appears in 100 ms when typing starts.
- After the final letter it blinks twice (530 ms on, 530 ms off) and leaves in 160 ms.
- It never blinks while text is static (slop M6).

**One pass per page view, about 9 s in all.** It never loops, unlike Preparoo's 150/100/2000 ms loop with a forever-blinking caret.

**Pauses:**
- Pauses when the h1 leaves the viewport (IntersectionObserver) or the tab is hidden, and resumes where it stopped.
- Reduced motion: no timers, final line only.
- Signed-in or recovery variants: no typing.

Only opacity and transform animate. The wash is a background on a span with a transform-scaled pseudo element.

**Tests replace heroLines.test.mjs H1:**
- The sentence is in the server HTML.
- The slot is aria-hidden with a sizer.
- Every phrase is ≤ 18 characters and at most the container width at 360 px (Playwright measure).
- The final rest text equals HERO_LINES[2].
- No setTimeout is scheduled under reduced motion.
- No infinite animation on the caret.
- The L-016 row is updated to \"typed line, one pass\".

## night

**De-neon Night by changing the ground, not by adding effects.** Owner score: Night 6/10. The audit measured 123 volt edges against 69 in Day, and the slop baseline 21 volt text runs against 9.

**Packet 1 rewrites the tokens.**

marketing-theme.css, html[data-theme='dark'] .mm, takes the app's warm charcoal (mm_colors.dart:117-133; logoB charcoal #12110E):

| Token | Value |
|---|---|
| --paper | #12110E |
| --paper-raised | #1B1A16 |
| --paper-sunken | #0E0D0B |
| --paper-raised-2 (new) | #25231E |
| --ink | #F4F0E6 |
| --ink-2 | #CFC8B9 |
| --ink-3 | #A29B8C (6.4:1 on #12110E) |
| --line | rgba(244,240,230,.09) |
| --line-strong | rgba(244,240,230,.16) |
| --accent-line | var(--line-strong) (neutral, was rgba(210,240,0,.5)) |
| --accent-text | var(--ink) (links and kickers go to ink with an underline) |
| --brand-word (new) | #D2F000. Used ONLY by .lp-title__brand (L-017) and the tour's \"MockMob\" (L-030). |
| --accent-wash | transparent |
| --surface-hover | #211F1A |
| --focus-ring | #D2F000 (a focus ring is functional) |
| body background (both :has rules) | #12110E |

Day takes cream to match the app:

| Token | Value |
|---|---|
| --paper | #F3EFE6 |
| --paper-raised | #FFFDF8 |
| --paper-sunken | #EAE4D8 |
| --ink | #1B1914 |
| --ink-2 | #4A453B |
| --ink-3 | #6B6457 |
| --line | rgba(27,25,20,.10) |
| --brand-word | #526700 |
| --accent-text | stays #526700 |

Volt (#D2F000 fill, #0B1000 ink, #9DB400 keycap edge) keeps exactly three roles (C9):
1. the brand (logo dot, Mobi);
2. the one primary key as a fill;
3. the selected state as a fill carrying dark ink.

Correct answers use --good-text. Chart bars use ink-2.

**Offenders fixed, by file:line from the audit and slop C1-C11:**

- **Hero:**
  - home-refinements.css:13-20: lp-stage::before volt radial deleted.
  - home-refinements.css:32-35: mm-drill::before volt top line deleted.
  - home-refinements.css:41-49: dead .lp-stage__live, .lp-stage__path deleted.
  - hero-depth.css:35-47: lp-proof glass becomes a hairline row (C7).
  - marketing-theme.css:47-61: toggle thumb glows `0 0 0 3px` and `0 0 12px` removed (the motion stays, as the owner restored it D10); stars keep opacity only.
  - HeroBackdrop.jsx and landing.css:234-276: grid, dot matrix and pointer spotlight removed (C6, M7).
- **Rest of the page:**
  - du.css:338-374: du-chip x19; selected becomes a fill, rest becomes a line-strong hairline.
  - feature-tour.css:11-13: ft__row active becomes a raised-2 fill, no ring.
  - compass-ladder.css:6-8, 30, 52-53, 69-70: buttons hairline; lp-cpro/lp-combo radial plus glass become a raised surface.
  - tour-screens.css:6, 14, 41, 131, 144, 191: under-glow, option halo, dot rings and ladder volt edge removed.
  - social-proof.css:14-17, 35-37: lime grid, orbit and ring monogram become an owned desk icon; glass over glow becomes raised.
  - lab-cinema.css:69, 91-95, 188-202, 289-294: halo ring, bezel rings and chip edges become hairlines.
  - mistake-lab.css:34-121 volt edges become hairlines.
  - Kickers (home.css:43): volt becomes ink-3.
  - Statement highlighter words (page.js:91, hero-depth.css:97): accent becomes ink weight 800 (T3).
  - Also: shelf objects' infinite float limited to the lit one, overshoot easing removed from chrome (M2, M3).

**Acceptance.** Re-run tmp/home-1104/slop capture.mjs on the branch preview, plus a new data/tests/night_calm_1104.test.mjs that greps the CSS:
- volt text runs per Night pass ≤ 1.2x Day, with 1 per viewport at most outside L-017 and L-030;
- volt edges on containers 0;
- coloured glows 0;
- volt radial washes 0;
- content glass panels 0;
- lime-tint pixel mean in Night ≤ 1.2x Day;
- infinite animations in any viewport ≤ 1.

Then Night and Day screenshots at 390 and 1440 for every section anchor, opened and compared side by side.

## scroll

**Packet 4 adopts the mechanism the scroll forensics proved on the bench** (RESULTS.md: 32 of 32 flick cells gave +1 step; wheel bursts of 1, 5 and 30 notches gave +1).

**Change in ScrollStory.jsx.**

- **Gesture capture:**
  - A window-level non-passive touchmove is registered only while a held story is within one screen of the viewport.
  - It owns a vertical gesture that starts inside a hold after a 6 px slop. Sideways gestures and inner scrollers stay native (the scrollsInside check).
  - The step commits at touchend from net travel: 40 px, or a 12 px flick at ≥ 0.3 px/ms. Speed never multiplies steps.
  - A 420 ms lock (120 ms under reduced motion) swallows gestures that start inside it.
  - A wheel burst ends after 160 ms of quiet and moves one step. Keyboard PageDown and Space move one step.
- **Edge stops:**
  - Flings crossing a story's first or last rest from outside are clamped at that rest.
  - A native scroll that ends inside a hold settles on the nearest rest, using scrollTo with behavior instant, wrapped in a 180 ms CSS translate on the stage so it does not read as a jump.
  - Exits stay free.
- **Step-driven visuals.** Progress fills, the Lab object tilt and the statement's words are driven by `data-step`, not by scroll position, so a half state cannot exist. React leaves the per-step path: steps toggle attributes, with no stage re-render.
- **Declared jumps.** goTo, HashSettle, DemoJump and nav links declare their target through scrollBus.jump(target), so a jump from outside is not held at rest 0.
- **Statement on phones.** It becomes a 4-step held story, one clause per step, with the shelf objects arriving on step 4. On desktop it stays a scrub plus a settle. Nothing is removed.
- **Geometry.** landing.css:1435 reserves 680svh for #your-prep on phones (it was 580svh). Every content-visibility contain-intrinsic-size matches the measured track, so the page height is stable fresh or warm (today 27,000 versus 27,906).
- **Lag (LK69):**
  - One shared scroll reader, new src/components/landing/scrollBus.mjs: one passive listener and one rAF per frame reading scrollY and the viewport once.
  - ObjectLife.jsx:134, PipGuide.jsx:101/148/360 and SectionPosition.jsx:78 subscribe to it instead of each running their own listener and loop.
  - PipGuide caches its stations on resize and drops its per-frame querySelectorAll, checkVisibility and getBoundingClientRect.
  - ScrollStory's ResizeObserver fitAll runs once per resize in rAF, never inside a scroll frame.
  - The Mobi rig idles in CSS.
- **Tests.** scrollStorySpeed.test.mjs is replaced by oneGesture.test.mjs, which locks L-027, L-028, L-029 and LK69. It runs in real Chrome (not chrome-headless-shell, which never scrolls) with timestamped CDP touch and wheel events, over the bench's matrix:
  - 4 distances x 4 speeds on each story give exactly +1 step at offset 0;
  - slow drags of 40/120/150/300 px give +1;
  - 20 px gives 0;
  - forward 100 then back 100 gives 0;
  - two flicks 150 ms apart give 1 step; 700 ms apart give 2;
  - an entry flick stops on step 0;
  - an exit flick leaves freely;
  - every stop is within 2 px of a rest.
  
  It also asserts that no non-passive listener is registered while no story is near (protecting LK47's \"no glide\").

**Before shipping:** a real iPhone and a real Android walk, plus his own phone look.

## examScreen

**Rebuild the home exam section (LK72) from the real runner's anatomy.** ExamComparator.jsx becomes `ExamScreen.jsx` with a new `exam-screen.css`; the old .lp-exam rules at home-refinements.css:84-228 are deleted. Our own screen is the default; the NTA rehearsal is a switch inside it. The NTA skin is no longer the section's picture.

**One theme-aware frame** (it follows Day and Night, unlike today's always-dark panel), copying TestPageClient.jsx:1213-1250, 1255, 1281 and 1448-1470:
- **Header:** exit, \"Accountancy quick mock\", a progress bar, \"6 of 15 answered\" (tabular), timer pill \"38:11\" (ink on raised-2, not volt).
- **Saved note:** a quiet one-line \"Saved on this device\". It is the real offline-save behaviour, as a line, not a banner.
- **Question card:**
  - chips for the chapter (\"Admission of a partner\") and the difficulty;
  - the stem in Literata 600, 18 px phone and 22 px desktop;
  - four options with tabular letter chips;
  - option C shown struck through, with a one-time caption under the options: \"Press and hold an option to strike it out.\"
- **Actions:** Mark and Clear as text buttons.
- **Phone bottom bar:** Prev, Palette, Next (Next is the one volt fill).
- **Review panel**, opened by Palette on phones and a right column on desktop:
  - counters for Answered, Marked, Pending and Not visited, each with a word plus an outlined chip, never colour alone;
  - a 15-chip grid;
  - a Submit key.
- **Interface switch**, at the top right of the frame: a segmented control, \"MockMob\" or \"NTA style\". It keeps the answers and the timer, as the runner really does.
  - NTA style reskins to the three NTA action words and the five-state legend, so the rehearsal still exists.
  - It is labelled as a rehearsal in the section h2 copy, not as a disclaimer.
- **Below the frame:** the \"Enter your exam space\" fullscreen gate, shown as a small, real line: \"Full screen, with Warnings 0 of 3.\"

**Mobi** takes the read pose (holding the answer sheet) beside the section head at 96/120 px, never inside the paper (no distractions in an exam, R-overlay).

**Size:**
- Section at most 1.1 screens at 390 (at most 930 px, from 1,644) and at most 760 px at 1440 (from 1,363).
- The console fits one phone screen (at most 760 px), as the real runner is 876 px document height.
- Copy at most 60 words in view.

**Acceptance:**
- examScreen.test.mjs asserts:
  - no \"Save & Next\", \"Mark for Review & Next\" or \"Clear response\" string in the MockMob mode;
  - the NTA words exist only in the NTA-style branch;
  - the theme follows data-theme;
  - the counters are labelled with words.
- A Playwright measure at 390 and 1440 for both themes and both modes checks the section height against the budgets above.
- A side-by-side shot with tmp/home-1104/audit/shots/runner/390-quick-accountancy-day.png shows the same anatomy.

## copy

**Text walls (LK71).** About 3,050 visible words at 390 today, 1,860 of them in the three held stories. Target: at most 2,000, with no section or step cut. Budgets, locked in landingCopy.test.mjs:
- section sub ≤ 20 words;
- tour slide body ≤ 25 words plus at most 2 points of ≤ 10 words each;
- Lab or Recovery step text ≤ 45 words, with the step's numbers living inside its mock screen, not in body text;
- FAQ answers ≤ 45 words;
- nothing over 60 words in one phone viewport except an opened FAQ.

Packet 5 moves the arrays out of page.js into a new src/components/landing/homeCopy.mjs so the budgets are testable.

**Concrete rewrites:**
- Mob slide body (45 words) becomes: \"Start a Mob, share its code, and race your friends on the same five questions for 24 hours. Fix it together sends you back to the one that caught you.\" (28 words; the points carry the rest).
- Lab sub (27 words) becomes: \"Every mock opens in the Lab: time, changed answers and the reason behind each miss.\" (15 words).
- Kickers above h2 (page.js:269, 292, 307, 372, 385) are removed. Their names already live in the position band (T2). The h2 stays.
- \"not just the answer\" x3 (page.js:127, LabCinema.jsx:35) become \"Fix the reason you missed it.\" and \"Repair the reason, then check it on fresh questions.\" (W1).
- Staccato clusters (W2): only the hero keeps its fragments. \"Practise. Replay. Repair.\" becomes \"Practise it, replay it, repair it.\"; \"Fix it once. Check it holds.\" becomes \"Fix it once and check it holds.\"
- Middle dots go everywhere (T6).
- The Ask Mobi point (27 words) is cut to 14.
- The Sparkles icon is replaced by the brand desk bell (I2).

**Truth:**
- Every number stays sourced from the capability gates and /api/stats.
- \"Fresh every time\" rests on the one-bank generator; \"no cap on Pro\" on the plan gate.
- No new claims. No disclaimers (L-024).

## brandSystem

**1. Colour.** The app's palette, with exactly three volt roles: brand, one primary fill, selected fill. Lamp amber #F2A93B appears only as painted light, never as CSS (swatch sheet rule: \"Volt is the only accent. Night = charcoal, Day = cream. Lamp amber is light, never a button.\"). There are no coloured shadows, no radial washes, and no glass on content.

**2. Mobi.** See hero.mobi: one finish, six poses with jobs, one in view, the same scale rule and the same behaviour on phone and desktop. The Fold characters appear only where the Mob is shown (tour Mob slide, at 48 px rather than 20 px heads).

**3. Owned illustration language: \"the lamp-lit desk\".**
- Painted scenes carry atmosphere: the hero room, and the existing scenes for empty and close states.
- Desk objects carry meaning:
  - the 13 BrandIcon webp objects replace the lucide icons in the tour rail (keycards, questions, mistakes, lesson, papers, revise, compass, today, mob, you; Ask Mobi uses the brass desk bell);
  - the 29 subject objects stay on the shelf;
  - foil and stamp seals mark Pro moments only.
- Controls stay plain icons (chevrons, close, check), per the BrandIcon header rule. No generic geometry, orbits or monogram discs (I1).

**4. Typography ladder.** It keeps Bricolage, Hanken and Literata and fixes the flat 1.2x range.

| Role | Face and setting | 390 | 1440 |
|---|---|---|---|
| Display XL (hero h1 only) | Bricolage 800, -0.035 to -0.04 em | 44/0.98 | 84/0.95 |
| Statement | Bricolage 650 (weight contrast) | 30/1.12 | 52/1.08 |
| Section h2 | Bricolage 750 | 30/1.04 | 52/1.0 |
| h3 | Bricolage 700 | 20/1.15 | 26/1.15 |
| Close h2 | Bricolage 800 | 40 | 72 |
| Question stems everywhere (sample, exam, Lab mock screens) | Literata 600, the printed-paper voice | 20/1.32 | 23/1.32 |
| Body | Hanken 400 (one rhythm) | 16/1.5 | 18/1.55 |
| UI and bubbles | Hanken 600 | 14-16 | 14-16 |
| Small (floor 14 on the home page) | Hanken | 14 | 14 |

- Literata ships as the existing 52 KB variable file, preloaded only on /.
- Numbers use Bricolage 700 with tabular-nums. Geist Mono leaves the home page (price, option letters, tour counter), and \"01 / 10\" counters become the progress bar alone (T1, T4).
- Every line-height is one of 0.95, 1.04, 1.15, 1.32 or 1.5.
- Sentence case everywhere.

**5. Motion grammar.** One authored load moment: the opening, then the typed line and Mobi's hello.
- Sections enter through their own story; the shared Reveal fade becomes a 180 ms opacity-only entrance on the first child only (M1).
- Overshoot only on Mobi and the logo.
- Chrome uses cubic-bezier(.23,1,.32,1) at 150-220 ms; a press is 100 ms (R-153, T-103).
- Reduced motion: instant or 160 ms fades with the same text.

**6. Theme parity.** Night may not be louder than Day (C12). The same tokens drive both, and every Night/Day shot pair is reviewed together.

## perItem

[
 {
  "item": "LK67 hero parity",
  "change": "Phone and desktop get one hero idea: the words, then Mobi in his lamp-lit room handing over the real first question. Today the phone has a room-only Mobi and desktop has a host-only Mobi in the gutter. The bubble lines move from tap-cycling to sample-state reactions. Taps give the same reaction act on both widths. `HeroMobi variant` collapses to one `desk` variant, and HeroRoom renders at every width.",
  "acceptance": "heroScene.test.mjs (rewritten):\n- .lp-desk__room and .lp-desk__mobi are visible at 390, 768 and 1440;\n- no media query hides either;\n- the bubble text never changes on a pointer tap (dispatch 6 real CDP taps; the text stays \"Your first question. Go.\");\n- answering the sample changes it to the right or miss line.\n\nScreenshots at 390x844 and 1440x900, Day and Night, show the same composition. Mobi measures ≥ 130 px tall on the phone and ≥ 170 px on desktop.",
  "files": [
   "src/app/page.js",
   "src/components/landing/HeroMobi.jsx",
   "src/components/landing/HeroRoom.jsx",
   "src/app/hero-scene.css",
   "src/components/landing/heroTaps.mjs",
   "src/components/landing/heroScene.test.mjs",
   "src/components/landing/heroTaps.test.mjs"
  ]
 },
 {
  "item": "LK68 Night de-neon",
  "change": "Web Night moves to the app's warm charcoal tokens. Volt is restricted to 3 roles plus the two owner-asked brand words. Every audited volt edge, radial, glow, halo and content-glass rule is removed (night field lists file:line). The hero grid, dots and pointer spotlight go.",
  "acceptance": "Slop capture re-run on the branch preview:\n- volt text runs Night ≤ 1.2x Day;\n- container volt edges 0;\n- coloured glows 0;\n- volt radials 0;\n- content glass 0;\n- lime-tint pixel mean ≤ 1.2x Day;\n- infinite animations ≤ 1 per viewport.\n\nnight_calm_1104.test.mjs greps the landing CSS for rgba(210,240,0 and #d2f000 outside the allowed selectors. release9_public_1018.test.mjs:209-221 is updated from \"grid and dots stay\" to \"hero has no ambient pattern\".",
  "files": [
   "src/app/marketing-theme.css",
   "src/app/marketing.css",
   "src/app/landing.css",
   "src/components/landing/HeroBackdrop.jsx",
   "src/app/du.css",
   "src/app/feature-tour.css",
   "src/app/tour-screens.css",
   "src/app/compass-ladder.css",
   "src/app/social-proof.css",
   "src/app/lab-cinema.css",
   "src/app/mistake-lab.css",
   "data/tests/night_calm_1104.test.mjs"
  ]
 },
 {
  "item": "LK69 one gesture, one step, and lag",
  "change": "The bench-proven gesture controller goes into ScrollStory.jsx: commit at touchend from net travel, a 420 ms lock, a 160 ms wheel burst, edge clamps, settle on the nearest rest, step-driven fills and declared programmatic jumps. The statement becomes a 4-step story on phones. Intrinsic sizes are fixed. One shared scroll reader (scrollBus.mjs) replaces 4+ listeners. PipGuide stops querying the DOM per frame. The Mobi rig idles in CSS.",
  "acceptance": "oneGesture.test.mjs, in real Chrome with CDP touch and wheel:\n- all 32 flick cells give +1 step;\n- slow drags give +1;\n- 20 px gives 0;\n- reversal gives 0;\n- entry stops at step 0;\n- every stop is within 2 px of a rest.\n\nPage height fresh equals warm, ±2 px. At 4x CPU over 22 swipes: p95 frame ≤ 20 ms (from 24), 0 frames over 100 ms (from 12), style recalcs during an 8 s idle hero ≤ 5/s (from 73). After that, a real iPhone and Android walk.",
  "files": [
   "src/components/landing/ScrollStory.jsx",
   "src/app/scroll-story.css",
   "src/components/landing/scrollBus.mjs",
   "src/components/landing/ObjectLife.jsx",
   "src/components/brand/PipGuide.jsx",
   "src/components/landing/SectionPosition.jsx",
   "src/components/landing/HashSettle.jsx",
   "src/components/landing/DemoJump.jsx",
   "src/app/hero-depth.css",
   "src/components/landing/oneGesture.test.mjs"
  ]
 },
 {
  "item": "LK70 hero tells what we are",
  "change": "Words come first on the phone. The h1 starts at 82 px (9.7 %), and a new lead sentence names the product: \"MockMob is CUET UG mock tests with a review that finds the chapter behind every mark you lose.\" The room shrinks from 320 to clamp(168, 25svh, 212) px and moves below the key.",
  "acceptance": "A Playwright measure at 390x844, 375x667, 360x640 and 412x915:\n- h1 top ≤ 12 % of the viewport;\n- the lead's bottom (containing \"MockMob is CUET UG mock tests\") ≤ 40 % at 390x844 (mock-up: 301/844 = 35.7 %) and ≤ 48 % at 360x640;\n- the key's bottom ≤ 46 % at 390x844;\n- the word \"exam\" or \"mock tests\" is in the first-screen text.\n\nThe test asserts the lead string via homeCopy.mjs.",
  "files": [
   "src/app/page.js",
   "src/app/hero-scene.css",
   "src/components/landing/homeCopy.mjs"
  ]
 },
 {
  "item": "LK71 slop traits and text walls",
  "change": "Word budgets are applied per section, sub, step and slide, and the copy moves to homeCopy.mjs. Kickers, the 'not just' contrasts, middle dots and staccato clusters go. Numbers move into the mock screens. The template rhythm is broken by role (statement band, held story, tool, proof).",
  "acceptance": "landingCopy.test.mjs asserts every budget, 0 middle dots, at most 1 'not just', and 0 kickers before an h2. The brand-capture word count at 390 is ≤ 2,000 visible words (from about 3,050). Every section anchor and every scroll story still exists (landingPosition.test.mjs unchanged).",
  "files": [
   "src/components/landing/homeCopy.mjs",
   "src/app/page.js",
   "src/components/landing/LabCinema.jsx",
   "src/components/landing/FeatureTour.jsx",
   "src/components/landing/landingCopy.test.mjs"
  ]
 },
 {
  "item": "LK72 exam screen: real, unique, shorter",
  "change": "ExamComparator becomes ExamScreen, built from the real runner's anatomy:\n- header with progress, answered count and timer;\n- the saved note;\n- chapter and difficulty chips;\n- strike-out;\n- Mark and Clear;\n- Prev, Palette and Next;\n- review counters;\n- the MockMob or NTA-style switch that keeps answers and timer;\n- the exam-space gate line.\n\nIt follows the theme, and NTA vocabulary appears only in the rehearsal mode.",
  "acceptance": "examScreen.test.mjs checks the vocabulary and theme rules. Section height ≤ 930 px at 390 and ≤ 760 at 1440, measured in both modes and themes. The screenshot sits side by side with the real runner shot.",
  "files": [
   "src/components/landing/ExamScreen.jsx",
   "src/app/exam-screen.css",
   "src/components/landing/ExamComparator.jsx",
   "src/components/landing/examScreen.test.mjs"
  ]
 },
 {
  "item": "LK73 stronger brand of our own",
  "change": "One Mobi finish (the rig) with six job poses as generated SVGs in every seat. Desk-object BrandIcons replace lucide in the tour rail. Literata is the question voice. A real type ladder (hero 1.46x h2, weight contrast). Warm app palette. Fonts and logo B are unchanged.",
  "acceptance": "landingMobi.test.mjs:\n- no /brand/mascot/*.webp on the home page;\n- every seat renders a generated pose;\n- one Mobi in view;\n- Mobi height ≥ 130 px in the hero.\n\nbrand_icons test: the tour rail uses BrandIcon, and there is no lucide import in FeatureTour. A type audit confirms the ladder values and 0 Geist Mono on the home page. The 12-part anti-slop test, item 1 (identity with the logo hidden), is judged on a logo-masked screenshot.",
  "files": [
   "src/components/brand/Mascot.jsx",
   "scripts/brand/build-mobi-poses.mjs",
   "src/components/brand/mobiPoses.generated.js",
   "src/components/landing/FeatureTour.jsx",
   "src/app/layout.js",
   "src/app/globals.css",
   "src/components/landing/landingMobi.test.mjs"
  ]
 },
 {
  "item": "LK74 refined loader and typing",
  "change": "OpeningMo is the app's \"mo\" opening in CSS: 1,280 ms per new session and 1,600 ms on a first-ever visit, then a FLIP into the bar logo. HeroTyped is a one-pass select-and-type with a sizer box, a solid ink caret that leaves after two blinks, pause off-screen, and nothing under reduced motion.",
  "acceptance": "A filmstrip every 100 ms at 390 and 1440 shows the mo, ink, unfold, composed and lift frames. The layer is hidden at 1.4 s, and elementFromPoint at the key is the key at 1.5 s. There is no layer on a same-session reload or under reduced motion. LCP ≤ 2.5 s at 4x CPU and CLS 0.\n\nTyping:\n- server text = HERO_SENTENCE;\n- phrases ≤ 18 characters and fit at 360 px;\n- the final text equals \"Know what to fix.\";\n- no infinite caret animation.\n\nheroLines.test H1 and checklist rows L-016 and L-043 are updated.",
  "files": [
   "src/components/landing/OpeningMo.jsx",
   "src/app/opening.css",
   "src/components/brand/logoLetters.mjs",
   "scripts/brand/split-logo-letters.mjs",
   "src/components/landing/HeroTyped.jsx",
   "src/components/landing/heroLines.mjs",
   "src/components/landing/heroLines.test.mjs"
  ]
 },
 {
  "item": "LK75 refine it ourselves",
  "change": "Every change is a refinement of existing components and assets: the room, the rig, the scenes, the icons, the app's opening and tokens. The full gate runs: the L-001..L-045 table with a test per fixed row, the slop capture, the 12-part test, and Night/Day pairs at 390 and 1440 for every anchor.",
  "acceptance": "A new data/tests/landing_checklist_1104.test.mjs maps each L row to an assertion where one is checkable (today 4 of 45; target ≥ 30). The orchestrator's live check on www.mockmob.in after deploy comes with opened screenshots.",
  "files": [
   "data/tests/landing_checklist_1104.test.mjs"
  ]
 }
]

## mockup

{
 "html": "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/hero.html",
 "shots": [
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/final-390-night.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/final-390-day.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/final-1440-night.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/final-1440-day.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/final-390-loader-lastframe.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/final-1440-loader-lastframe.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/final-360x640-night.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/design-brand/shot-poses.png"
 ],
 "selfCritique": "I built, shot and opened four rounds: v1, v2, v3 and final, all in tmp/home-1104/design-brand. The mock-up uses the real self-hosted Bricolage, Hanken and Literata, the real logo-header SVGs, the real painted rooms and the real rig Mobi, rendered as static SVG by a copy of build-mobi-poster.mjs.\n\n**Round fixes:**\n- **v1.** Mobi was positioned against the card, not the room: invisible on the phone and covering options C and D on desktop. Fixed with a stage wrapper.\n- **v1.** An OMR-ring backdrop I had added as an \"owned\" pattern read as a busy tech texture behind the h1 in Night (slop C6). I applied \"what would be better without this\" and removed it.\n- **v2.** The Day painting's feathered edges showed as a white halo inside the frame, so I overscanned it to 118 %.\n- **v2.** The bubble wrapped \"right / here.\" and covered the painted answer sheet. I shortened it to the approved \"Your first question. Go.\" and moved it onto the floor beside Mobi.\n- **v3.** Two volt keys were in one desktop viewport (bar \"Start free\" plus the hero key). The bar key became a raised secondary.\n- **v3.** A middle dot in the card head, \"English · 1 of 5\", violated T6. I split it into two spans.\n\n**Final checks against the slop list:**\n- C1: 1 volt text run per viewport, the owner's \"CUET 2027.\"\n- C2-C5: no volt edges, no coloured glows, no radial washes, no lit card edge.\n- C6: no grid, dots or spotlight. C7: no glass on content.\n- C9: volt only on the key, Mobi and the logo. C11: warm charcoal with neutral 9 % and 16 % hairlines.\n- T1: no Geist Mono. T2: no kicker. T6: no middle dots.\n- L1: CUET at 9.7 % and the pitch done by 35.7 % of 844.\n- L2: the same composition at both widths. L4: two levels only (the room-and-card desk on the page).\n- I3: Mobi has a job (handing the question).\n- M6: the caret is ink, not volt, and the full sentence stays in the DOM.\n\n**12-part test:**\n1. Identity with the logo hidden: the lamp-lit room, Mobi and the answer-sheet poster are unmistakable. Pass.\n2. One primary action. Pass.\n3. True content: real sample question, real price and bank line. Pass.\n4. Hierarchy at first scan: h1 at 84 is 1.46x the section h2. Pass.\n5. Intentional composition. Pass.\n6. Typography by role: Literata reserved for question stems. Pass.\n7. Every state: partial. Right, miss and after-five bubbles, signed-in and reduced motion are specified, not drawn.\n8. Accessible interaction: specified (sr-only sentence, aria-hidden slot, 44 px targets); not tested in the mock-up.\n9. No pseudo-evidence: the hero-metric strip becomes sentence links. Pass.\n10. Motion with a reason: one load moment, Mobi acts tied to answers. Pass by spec; not filmed.\n11. One leading metric plus one guardrail, proposed: sample start rate from the hero, guarded by LCP ≤ 2.5 s and bounce.\n12. What would be better without this: the ring field went.\n\n**Remaining weaknesses I can see:**\n- On desktop the left column has about 180 px of calm space under the facts. Acceptable, but a judge may want the proof row raised.\n- On 360x640 Mobi sits just below the fold. The room clamp to 168 px is in the spec but not drawn.\n- The hello pose has closed smiling eyes. If the film's 'no squint' rule applies to the site, the wave pose with open eyes is the swap (shot-poses.png).\n- The loader is shown only at its last frame; the unfold itself is not animated in the mock-up.\n- Lighthouse, real-device scroll and the typed animation were not exercised. The mock-up is a static picture, not a build."
}

## keepsAndNeverCuts

Kept, per L-004, L-005, L-039, L-042 and LK73:
- **Sections and stories:** all 14 sections and the footer; the three held stories (Mistake Lab, Feature tour, Score Recovery Lab) and the statement; the shelf of lamp-lit subject objects; the DU calculator; the Compass; Instagram reels; pricing; FAQ; the close band; the dock.
- **Characters and motion:**
  - PipGuide (the flying Mobi), made cheaper but kept.
  - The theme toggle's sun-to-moon motion (owner D10), with only its glow removed.
  - The hero room painting and its Night answer-sheet fill.
  - Mobi's tap reactions (now on both widths).
  - The volt keycap edge.
  - Every Mobi seat, re-skinned to the one finish.
- **Brand:** fonts Bricolage Grotesque, Hanken Grotesk and Literata; logo B with Mobi as the second o and the small volt dot.
- **Copy and truth:** the approved hero sentence \"CUET 2027. One mock. Know what to fix.\" as the h1's text and resting state; \"CUET 2027.\" brand-coloured (L-017) and not a link (L-018); \"MockMob\" green in the tour heading (L-030).
- **Hero behaviour:** the sample with its other-subjects path (L-015); state-based CTAs (L-006 to L-009); no video (L-044).
- **USP:** said once in the bank line (\"One bank of 5,765 questions. No cap on Pro.\") and once in the typed \"Fresh every time.\" Never \"never repeats\" (L-041).

Removed, each with its reason:
- the hero grid, dot matrix and desktop-only pointer spotlight (C6, M7, LK68);
- the decorative glows, edges and glass listed under night;
- section kickers (T2);
- the six tap-only pitch lines, whose facts moved into the lead, the typed line and the bank line (LK67);
- the baked photo-real poses from home-page seats, replaced by the same character in one finish.

None of these is a section, scroll story, showcase or character.

## risks

1. **L-043 says the logo opening lasts about 3 s.** This proposes 1.6 s first-ever and 1.28 s per session, to protect LCP and first taps. That is a decision for the owner; OPENING_FIRST_MS is one constant. A full-screen opening also risks his \"slow site\" read on cold 4G. Its CSS ends hidden even if JS fails, and it never runs twice in a session.
2. **Ruling H1 of 1 Nov (static headline) against L-016 and LK74.** The design keeps the approved sentence as the DOM and resting text but types two phrases first. heroLines.test H1 must be rewritten deliberately; it is not a regression.
3. **LK47 (2 Nov: stop gliding) against LK69 (one gesture, one step).** The controller never glides: commits are instant and the clamp sits only at story edges. But it is the most regression-prone area, as fixers broke it before. It needs a real iPhone (Safari non-passive touchmove, momentum stop, scrollend fallback) and a real Android before it ships. Headless shell cannot test it.
4. **Retiring the baked photo-real Mobi poses from the seats** changes approved art. If he prefers them, the fallback is to keep the baked poses but match their scale and light. The one-finish rule is the brand argument.
5. **Changing web Night from green-black to the app's warm charcoal** shifts every section's look at once. Expect a few contrast regressions in hand-tuned Night overrides (du.css has about 20). Every section anchor must get Night/Day shots.
6. **release9_public_1018.test.mjs locks \"grid and dots stay\".** Removing them contradicts an 18 Oct lock whose owner source I did not find. Check NOW and the ledger before deleting.
7. **Literata on the home page** adds a 52 KB font. Preload it only on /, and subset to latin if LCP suffers.
8. **The hello pose's closed smiling eyes** may trip the film rule \"no squint or half-lid\". The wave pose is the swap.
9. **Not verified:** the mock-up is static, so the typing, the opening, real-device scroll, performance numbers and the accessibility tree were not exercised. The perf targets in the per-item acceptance are goals, not measurements.
10. **Packet boundaries:** page.js is owned by packet 2 only. Packets 3 and 5 deliver components and homeCopy.mjs that packet 2 wires in, so packet 2 lands last or rebases.

## buildPackets

[
 "P1 Tokens and Night calm (owns src/app/marketing-theme.css, marketing.css, landing.css, globals.css, du.css, feature-tour.css, tour-screens.css, compass-ladder.css, social-proof.css, lab-cinema.css, mistake-lab.css, src/app/layout.js, src/components/landing/HeroBackdrop.jsx, data/tests/night_calm_1104.test.mjs, and the grid/dots lines of data/tests/release9_public_1018.test.mjs).\n\nWork:\n- Warm app tokens for Night and Day. The new --brand-word and --paper-raised-2.\n- Volt limited to three roles.\n- Remove every edge, radial, glow and halo listed in the night field.\n- HeroBackdrop renders nothing in the hero.\n- Type ladder tokens.\n- Literata preloaded on / in layout.js.\n- Geist Mono off the home page.\n- The content-visibility intrinsic sizes at landing.css:1435/1447, using the numbers from P4's spec (680svh phone).\n\nAccept: the slop capture numbers and the Night/Day anchor shots at 390 and 1440.",
 "P2 Hero desk and Mobi in the hero (owns src/app/page.js, src/app/hero-scene.css, src/app/home-refinements.css, src/components/landing/HeroMobi.jsx, HeroRoom.jsx, heroTaps.mjs, DemoDrill.jsx, demoSignal.mjs, heroScene.test.mjs, heroTaps.test.mjs).\n\nWork:\n- Hero layout per the hero field: words first, the desk stage with the room at every width, Mobi 134/180, sample-state bubble lines, taps give reaction acts only, the Night sheet fills per sample answer.\n- lp-proof becomes sentence links. The bar CTA is secondary while the hero key is in view.\n- Delete the old hero lines 13-49 and the exam block 84-228 from home-refinements.css.\n- Integration owner: wires OpeningMo and HeroTyped (P3), ExamScreen and homeCopy.mjs (P5) into page.js. Lands last.\n\nAccept: the LK67 and LK70 measures, and the four hero shots matching the mock-up.",
 "P3 Opening and typed headline (owns new src/components/landing/OpeningMo.jsx, src/app/opening.css, src/components/brand/logoLetters.mjs, scripts/brand/split-logo-letters.mjs, src/components/landing/HeroTyped.jsx, heroLines.mjs, heroLines.test.mjs).\n\nWork:\n- Generate per-letter logo paths from logo_geometry.g.dart letterX.\n- CSS-only \"mo\" opening on the timeline in the loader field, with the inline run gate (first, short, skip; storage in try/catch), the FLIP to the bar logo and the hidden end state.\n- One-pass typed line with sizer, select wash, ink caret, pause off-screen and reduced motion.\n- Update the L-016 and L-043 wording with the orchestrator.\n\nAccept: the filmstrips, the elementFromPoint check, LCP and CLS, and the typing tests.",
 "P4 One gesture, one step, and scroll performance (owns src/components/landing/ScrollStory.jsx, src/app/scroll-story.css, new src/components/landing/scrollBus.mjs, ObjectLife.jsx, src/components/brand/PipGuide.jsx, SectionPosition.jsx, HashSettle.jsx, DemoJump.jsx, src/app/hero-depth.css (statement as a 4-step phone story), src/components/brand/MobiReact.jsx plus mobi-figure.css (idle in CSS), and the replacement of scrollStorySpeed.test.mjs with oneGesture.test.mjs).\n\nPort the bench controller from tmp/home-1104/scroll/prototype-one-gesture-v2.html.\n\nAccept: the full gesture matrix in real Chrome, the 4x CPU frame targets, then real iPhone and Android.",
 "P5 Exam screen, copy budgets and section brand (owns new src/components/landing/ExamScreen.jsx, src/app/exam-screen.css, ExamComparator.jsx (retire), examScreen.test.mjs, new src/components/landing/homeCopy.mjs, LabCinema.jsx, MistakeLab.jsx copy, FeatureTour.jsx (BrandIcon rail, Fold heads at 48 px), TourScreens.jsx, src/components/brand/Mascot.jsx (seats use generated poses), new scripts/brand/build-mobi-poses.mjs, src/components/brand/mobiPoses.generated.js, landingCopy.test.mjs, landingMobi.test.mjs).\n\nWork:\n- Real-runner exam screen with the MockMob/NTA switch.\n- Word budgets and the listed rewrites.\n- Six job poses generated from the rig (the script already proven in tmp/home-1104/design-brand/poses.mjs).\n- The desk bell for Ask Mobi.\n\nAccept: exam height and vocabulary tests, the word count at most 2,000, and one Mobi finish on the page."
]

## performance

**Measured today at 4x CPU (audit):**
- FCP 888 ms, LCP 2,944 ms (the lazy room AVIF), TBT 536 ms.
- Scroll p95 24 ms, 12 frames over 100 ms.
- 3,978 style recalcs. The idle hero does 73 recalcs/s while the Mobi rig runs 52 rAF/s.

**Levers in this proposal:**
1. **LCP moves to the h1.** It is server text painted under the opening. The room drops to 212 px and below the key, and is lazy with fixed dimensions, so the image is never the LCP on phones.
2. **The Mobi rig idles in CSS.** rAF runs only during an act, which removes about 5 s of task time per 8 s of idle.
3. **One scroll reader** replaces the ObjectLife, PipGuide, ScrollStory and SectionPosition listeners. PipGuide's per-frame DOM queries are cached.
4. **No layout reads in scroll frames.** ScrollStory's fitAll runs on resize only, and steps toggle attributes without React re-renders.
5. **Intrinsic sizes match the tracks,** so there is no 906 px geometry drift.
6. **Fewer animations:** the 55 Night animations and the infinite shelf floats drop to the lit object only, and the hero grid layers are gone.
7. **The opening is CSS-only** (about 2 KB inline plus about 6 KB of letter paths) and never runs twice in a session.

**Costs added:** Literata (52 KB, preloaded on / only) and the HeroTyped and OpeningMo JS (about 3 KB gzip).

**Targets, to be verified, not claimed:**
- LCP ≤ 2.5 s at 4x CPU, TBT ≤ 300 ms, CLS 0;
- scroll p95 ≤ 20 ms with 0 frames over 100 ms;
- idle hero ≤ 5 recalcs/s;
- field INP ≤ 200 ms.

## evidenceIds

[
 "AGENT_RULES 7 (one primary action)",
 "AGENT_RULES 26 (distinct art direction, no default glass/gradient)",
 "AGENT_RULES 27 / T007 / T009 (real product screen over generic art: sample card and real runner)",
 "AGENT_RULES 31 (motion with purpose, reduced motion)",
 "AGENT_RULES 33 (cards only for meaningful groups)",
 "T003 (value before account wall: five questions, no signup)",
 "T004 (carry guest work; no artificial sunk cost)",
 "S014 (progressive disclosure for secondary: review panel behind Palette on phone)",
 "S016 (accessible labels, selected state, keyboard)",
 "ui-ux T-005 / T-069 (neutral or warm charcoal dark theme, not tinted near-black)",
 "ui-ux T-031 / T-072 (exactly one soft accent)",
 "ui-ux T-080 / T-082 (no glow, no glass on content)",
 "ui-ux T-062 / T-064 (no kickers, no single accented word beyond the owner's two)",
 "ui-ux T-124 (no middle-dot strings)",
 "ui-ux T-050 (tabular numerals, not mono labels)",
 "ui-ux R-153 / T-103 (durations by role, ease-out)",
 "ui-ux T-024 / T-112 (one authored page-load moment)",
 "ui-ux A-001 (floating UI never covers content: bubble and Mobi kept off options)",
 "slop C1-C12, T1-T6, L1-L7, I1-I3, M1-M7, W1-W5 (slop-checklist.md)",
 "audit AUDIT.md sections 0-3 (geometry 45%, neon counts, perf profile, exam 1,644 px)",
 "scroll RESULTS.md (bench: 32/32 flick cells +1 step)",
 "BRAND.md 1.4 (app opening timeline), 4 (type levels), 8 (phone geometry)",
 "Preparoo source splash.txt a-60 (800 ms zoom, 750 ms lift), typing.txt (150/100/2000 ms loop, forever caret, deliberately not copied)"
]

