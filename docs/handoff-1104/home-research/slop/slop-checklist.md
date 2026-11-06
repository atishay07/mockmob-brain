# AI-slop checklist for the MockMob home page (Night first)

Built 4 Nov 2026, about 2:30 am IST, for LK67 to LK75. This is a judging aid for the home page (`src/app/page.js` and `src/components/landing/*`), not a design brief. Read-only research: no code was changed.

**Precedence.** The owner's own words come first (OWNER-FEEDBACK-2026-10-31-LEARN.md:202-231; OWNER-MASTER-LEDGER.md:699-711). His fixed landing checklist L-001 to L-045 comes next (WEB-OWNER-LEDGER-2026-10-17.md). This list comes after both. He has asked for two accent uses that this list would otherwise flag, so they stay: "CUET 2027." in the brand colour (L-017) and "MockMob" in green in the tour heading (L-030).

**Standing rules that every fix must keep.**
- Never remove a section, animation, showcase or scroll story (L-004, L-005).
- Refine, don't rebuild.
- Phone first: every section must be at least as strong on a phone (L-003).
- Night stays subtle.
- No disclaimers (L-024).
- Every claim must be true.

**Re-measure.**
1. Run `node capture.mjs` in this folder. It takes the browser lock and shoots production. Set `BASE=http://localhost:3452/` to shoot a local build instead.
2. Run `node summarize.mjs` to get the per-viewport counts.

The in-page detector is `audit()` in capture.mjs:46. The pixel maths is `pixelAudit()` in capture.mjs:148.

## Baseline: production, 4 Nov 2026, 2:26 to 2:30 am IST

The run sampled 17 viewports per pass at 1440x900 and 16 at 390x844 (scale 2): the hero, then each section anchor. The shots, `index.json` and `summary.json` are in `shots/`. The contact sheets are `shots/contact-{390,1440}-{night,day}.png`.

| per pass (sum over viewports) | 390 Night | 390 Day | 1440 Night | 1440 Day | linear.app 1440 | linear.app 390 |
|---|---|---|---|---|---|---|
| volt-coloured text runs | 21 | 9 | 26 | 7 | 0 | 1 |
| volt edges (borders, rings, outlines)* | 37 | 23 | 35 | 24 | 0 | 1 |
| coloured glows (volt shadow with blur) | 3 | 1 | 3 | 1 | 0 | 0 |
| volt washes (gradient fills) | 6 | 7 | 7 | 9 | 0 | 0 |
| content glass panels (not nav or dock) | 4 | 4 | 5 | 5 | 0 | 0 |
| lime-tint-on-dark pixels, mean (peak) | 3.70% (13.76%, combo) | 0.88% | 1.95% (10.27%, Compass Pro) | 0.79% | 0.27 to 0.94% | 0.01 to 0.09% |
| infinite loops in view | 19 | 19 | 55 | 55 | 1 | 1 |

\*The edge count includes the volt keycap's solid bottom edge (`0 4px 0 #9db400`, marketing.css:250), one for each primary key in view. That edge is owned depth, not a neon edge.

For the reference sites, the "volt" rows count any saturated accent, of any hue, and the tint row counts any saturated tint on dark.

What this shows:
- **Night carries much more lit text than Day.** It has 2.3 times as many volt text runs at 390 (21 against 9) and 3.7 times as many at 1440 (26 against 7).
- **Night carries 2.5 to 4.2 times as much olive-lime fog** (the lime-tint pixel share).
- **Mechanism.** The same tokens turn into olive ink on Day but into pure volt on Night. marketing-theme.css:8 sets `--accent-text: #d2f000` and `--accent-line: rgba(210,240,0,.5)` for Night. For Day it sets `#526700` and `#9caf5d` (marketing-theme.css:20).

## (a) The checklist: 40 tells

Each item gives:
- the tell;
- how to detect it in code, then on a screenshot;
- the pass bar for MockMob;
- what the live page does now;
- the sources.

### Colour and light (C1 to C12): the Night problems

**C1. Neon text: the accent used as a text colour on dark.**
- Code: an element with its own text has a computed `color` with its max channel above 200 and saturation above 0.6, on a dark body. pixelslop pattern 22 flags more than 3 per page.
- Screenshot: count the lime words per viewport.
- Pass: at most 1 per viewport, and only "CUET 2027." (L-017) and "MockMob" in the tour heading (L-030). Kickers, links, badges, numbers and timers use ink.
- Now: 21 distinct volt text items across the Night page.
  - Kickers ×4: home.css:43, used at page.js:269, 292, 307 and 372.
  - Compass Pro and Combo Planner badges: compass-ladder.css:58.
  - Statement words "where, tonight, shortlist": page.js:91 and hero-depth.css:97.
  - Links: "Free DU eligibility and cutoff calculator" and "Sign up free and pick yours" (hero-scene.css:35).
  - Numbers "780", "653" and "161K", and the monogram "GJ".
  - Timer "38:11", "Saved", "Pace 1:12" and "0:24 under".
  - At most 3 runs in one viewport (the 1440 hero).
- Sources: pixelslop #22; impeccable "AI color palette", "Dark mode with glowing accents"; Fountain Institute tell 1, "Neon color palette"; ui-ux-standards.md:79 (one soft accent); W-075 (one volt primary per viewport).

**C2. Neon edges: 1px accent outlines on containers, tabs, chips and rows.**
- Code: `border-color`, `outline` or `box-shadow: 0 0 0 Npx` in the accent at alpha 0.15 or more. A doubled edge is a border plus an inset ring.
- Screenshot: count lime-outlined boxes per viewport.
- Pass: 0 on containers. At most 1 per viewport, and only on the one selected control, preferably as a solid fill rather than an outline.
- Now:
  - The Night `--accent-line` composites to #6f8007, hsl(68,90%,26%). That is 4.35:1 against the ground. A neutral hairline (rgba(244,245,240,.09)) is 1.23:1, so the lime edge is 3.5 times louder than the page's own structure. Day's #9caf5d is only 34% saturated (2.2:1).
  - Uses: feature-tour.css:13 (active tab: border plus inset ring); compass-ladder.css:8, 30, 52 and 69; mistake-lab.css:34, 50, 58, 92 and 121; tour-screens.css:41, 54, 159, 166 and 191; social-proof.css:15-17 and 65; landing.css:1028, 1105 and 1136; du.css (about 20 rules, for example du.css:82, 208 and 532).
  - Example frames: shots/mm-390-night-05-tour.png (the active tab and the picked option) and mm-390-night-09-cpro.png (the whole card is lime-edged).
- Sources: impeccable "Dark mode with glowing accents", "wall of neon", "Lazy Cool: glass panels, neon edges"; impeccable new-work.md:65, which names this cluster outright: "near-black with one neon accent and glowing edges".

**C3. Coloured glows: accent box-shadows with blur, and zero-offset halos.**
- Code: a box-shadow, drop-shadow or text-shadow whose colour is the accent and whose blur is above 0. pixelslop #3 flags more than 2 glows on a dark body.
- Pass: 0.
- Now:
  - tour-screens.css:41: `0 0 20px -6px rgba(210,240,0,.45)` on the picked option.
  - tour-screens.css:14: a lime under-glow `0 18px 40px -24px rgba(210,240,0,.18)` on every tour screen. It is invisible on Day paper and glows on Night.
  - Halo rings: tour-screens.css:131 and 144, and lab-cinema.css:69 (`0 0 0 4px` accent wash on the scene dot).
- Sources: pixelslop #3; design-taste-frontend/SKILL.md:101 ("NO Neon/Outer Glows"); ui-ux-standards.md:82 and 84 (no glow or neon halos; no coloured zero-offset halos); L-019.

**C4. Glow blobs and spotlight washes: radial accent gradients behind content.**
- Code: `radial-gradient(` whose colour is the accent, on a ::before element or a background.
- Pass: 0. The only allowed light is the warm lamp light that the paintings already own (home.css:68).
- Now: four lime radial glows remain.
  - home-refinements.css:16 (alpha .085, behind the hero demo bay; .14 on Day at :36).
  - compass-ladder.css:53 (.16) and :70 (.14).
  - social-proof.css:37 (.22). Its own comment at social-proof.css:35 reads "Apple-style glass over a soft volt glow".
  - landing.css:221 says the hero "aurora" was removed as the L-019 glow. The same device survived in these four places.
  - On near-black these composite to olive fog, from #1c230d to #37410b. That produces the 10 to 14% lime-tint peaks in the Compass Pro and Combo Planner frames.
  - Day has its own versions (home-refinements.css:36 at .14, compass-ladder.css:65 at .24, social-proof.css:48 at .28). Remove them in both themes.
- Sources: impeccable "Radial-gradient background halo", "Soft spotlight behind content"; Fountain Institute tell 2, "Dark mode glow"; aismells "Gradient Fog"; Built In (Donska 2026), "generic gradient blobs"; L-019 ("no drifting glow blobs").

**C5. Lit edges and beams: an accent gradient hairline on a card's top edge, or light running round an edge.**
- Code: a 1 to 2px tall element or pseudo-element with `linear-gradient(90deg, transparent, <accent>, transparent)`, or an animated conic border.
- Pass: 0.
- Now:
  - home-refinements.css:32-35: the hero demo card's top edge is volt at 55%, compositing to #7e930a at 4.78:1. It is live: the audit found `div.mm-screen.mm-drill::before`.
  - The `.lp-stage__path` gradient hairline at home-refinements.css:49 is dead CSS: no JSX renders the class.
- Sources: L-019 ("no light running around an edge"); Magic UI "Border Beam" and "Shine Border"; impeccable "Lazy Cool".

**C6. Ambient tech patterns: a hairline grid, a dot matrix with a radial fade mask, and dots lit by the pointer.**
- Code: a background-image of 1px linear-gradient lines on a fixed `background-size`, or `radial-gradient(circle at 1px 1px …)`, or a layer that follows the pointer.
- Pass: 0 in the hero and the close band. A dot matrix that actually is MockMob's answer sheet (OMR bubbles) is owned. A generic dot pattern is not.
- Now:
  - HeroBackdrop.jsx, with landing.css:234-262: a 4.5rem grid, a 1.5rem dot matrix, and a 13rem volt dot spotlight under a fine pointer (shots/mm-1440-night-01-hero-pointer.png).
  - Close band: page.js:441-444.
  - Reel cards: social-proof.css:14 (a lime grid).
  - History: commit b6c40be4, "Hero v4: type first, nothing ambient" (16 Oct, 1:29 am), removed "the dot matrix and pointer-lit dots" and flagged "the close band's aurora, grid and dots". It exists only on web/land2-1015 and archive branches and never reached main (continuum handoff 20261015T200157-6ee68362).
- Sources: impeccable "Decorative grid-line background"; Magic UI "Grid Pattern", "Dot Pattern", "Interactive Grid Pattern"; Aceternity "Grid and Dot Backgrounds", "Spotlight".

**C7. Glassmorphism on content panels.**
- Code: `backdrop-filter` other than none on something that is not fixed chrome. pixelslop #2 calls 3 or more uses a pattern.
- Pass: 0. Allowed: the nav, the dock and the position band (owner W-071; ui-ux-standards.md:82).
- Now: 4 content glass panels.
  - .lp-proof: hero-depth.css:35-48, blur 24px, saturate 170%.
  - .lp-cpro: compass-ladder.css:52.
  - .lp-combo: compass-ladder.css:69.
  - .rl__summary: social-proof.css:36.
  - Each of the last three sits on a lime glow (C4), which is the "glass over glow" recipe.
- Sources: pixelslop #2; impeccable "Glassmorphism everywhere"; AGENT_RULES.md:26; ui-ux-standards.md:212 ("Glass, gradients and grids are slop when chosen by default").

**C8. Status dots and pings.**
- Code: a circle of 14px or less filled with the accent, with a ring or a `ping`/`pulse` keyframe.
- Pass: dots only for a real live state, with no rings and no pings.
- Now, rendered on the home page:
  - Dots with rings: `.lc-scene__take::before` (lab-cinema.css:69, a 4px ring) and `.ts__you` (tour-screens.css:144, a 3px ring).
  - Plain dots: `.lp-exam__live` (home-refinements.css:84, in the exam band) and `.lct__mark`.
- Now, still in the stylesheets but not rendered (no JSX uses them; delete so they cannot come back):
  - `.lp-pill__dot` with an infinite ping (landing.css:355-363).
  - `.lp-stage__live` pinging 3 times (home-refinements.css:41-42).
- Sources: Fountain Institute tell 7, "Status dots"; impeccable "Pulsing status dot"; L-020; commit b6c40be4 (it removed "the stage-heading pulsing dot").

**C9. One accent doing every job.**
- Code: grep the uses of the accent token and list the distinct roles.
- Pass: 3 roles or fewer:
  1. the brand marks (logo dot and Mobi);
  2. the one primary key, as a fill;
  3. the selected state, as a fill with dark ink.
  Correct and good use their own green; data and links use ink.
- Now: volt carries 12 or more roles. It is the brand, the CTA fill, kicker text, link text, a headline word, statement words, the selected chip, the correct answer (mistake-lab.css:58), a right count (:50), chart bars (mistake-lab.css:79, compass-ladder.css:40), the avatar fill (social-proof.css:90), the play button (social-proof.css:53), the focus ring (marketing-theme.css:7) and the "New" badge (NavBar.jsx:26).
- Sources: ui-ux-standards.md:78-79 ("Colour comes from meaning … exactly one soft accent, reserved for the primary action, the active state and the signature element"); Robinhood (2024), "purposeful pops of Robin Neon"; Nike: "limit the use of Volt to accents that do not cover a large amount of space".

**C10. A saturated accent at near-white brightness used as text or lines on dark.**
- Code: an accent with HSL saturation of 80% or more and relative luminance of 0.6 or more, used for text or strokes on a ground with luminance below 0.02.
- Pass: on Night, volt is a fill that carries dark ink, never text or a line. The system already says so: marketing.css:25, "Volt is a fill that carries dark ink, never a glow".
- Now: volt #d2f000 is hsl(68,100%,47%) with luminance 0.760. That is 85% of the body ink's 0.896, at 14.8:1. Every volt word is as bright as the white text and fully saturated, which is the highlighter effect.
- Sources: Android/Material dark theme ("Saturated colors also produce optical vibrations against a dark background, which can cause eye strain"; use desaturated, lighter tones); design-taste-frontend/SKILL.md:45 ("Saturation < 80%"); redesign-existing-projects/SKILL.md:34.

**C11. Night is not a designed theme: a tinted near-black, with edges doing the job of elevation.**
- Code: compare the ground and raised surface colours and the contrast between them.
- Pass:
  - 3 or more surface steps, each at least about 1.15:1 from the one below, neutral (under 10% saturation) or deliberately warm;
  - neutral borders at alpha 0.06 to 0.12;
  - product screens separated by surface steps, not by lime edges.
- Now:
  - The ground #0b100e is green-tinted (hue 156°, luminance 0.005). paper-raised #131a16 is only 1.08:1 above it.
  - The demo screen's gradient top #182117 is 1.16:1, falling to about 1.03:1 at its bottom. On Day the same dark screen is about 15:1 against the paper.
  - So every container in Night needs an edge, and the edges drift to lime.
  - For comparison: linear.app's body is #08090a with neutral borders at alpha 0.05 to 0.12 (median 0.08). The owner's standard is about #181818 ground and #212121 raised, neutral, "not blue- or indigo-tinted" (ui-ux-standards.md:83, §10 item 7).
- Sources: as above; RAXXO 2026 ("Spend contrast like currency").

**C12. Theme parity: Night louder than Day.**
- Code: run the capture and compare Night with Day per section.
- Pass: volt text runs and lime-tint pixel share in Night at most 1.2 times Day.
- Now: text is 2.3 times Day at 390 and 3.7 times at 1440. Lime tint is 4.2 times at 390 and 2.5 times at 1440. The owner scores Night 6/10 and the page overall 7/10.
- Sources: L-025 ("one design theme"); W-078 ("no theme-only bugs").

### Type (T1 to T6)

**T1. Overused AI fonts.**
- Code: `getComputedStyle(h1 | body).fontFamily`.
- Pass: no Inter, Geist Sans, Space Grotesk, Plus Jakarta Sans, Poppins, DM Sans, Roboto or Arial.
- Now: passes for display and body (Bricolage Grotesque, Hanken Grotesk, Literata, as LK73 says). One leftover: Geist Mono, the sibling of the "Geist" that impeccable lists as overused, sets figures and prices: `.mm-measure` (marketing.css:199-205; "₹0", "73", "924.3"), the tour counter (feature-tour.css:20) and the "GJ" monogram (social-proof.css:16). Hanken Grotesk with `tabular-nums` does the same job (ui-ux-standards.md:47, T-050).
- Sources: impeccable "Overused font: Inter and Geist"; prg.sh (Oct 2025); devtake (Jun 2026); the owner's list (OWNER-FEEDBACK-2026-10-31-LEARN.md:219-226).

**T2. A kicker or eyebrow label above every section heading, plus accent badges.**
- Code: a small `<p>` directly before an h2, or `.lp-kicker` / `.lp-cpro__badge`.
- Pass: no kicker. Where the name matters, it goes into the h2 itself or into the position band.
- Now:
  - 5 kickers in volt: page.js:269, 292, 307, 372 and 385. The 385 one renders only when the wall of love has voices; it is absent in production.
  - 2 badges: page.js:316 and 347.
  - Sentence case does not exempt them (ui-ux-standards.md:73: "No … kickers above headings").
- Sources: impeccable "Label above a heading"; T-062; W-076.

**T3. Highlighter words inside headlines and statements.**
- Code: a span inside an h1, h2 or statement that carries the accent colour.
- Pass: only the two the owner asked for (L-017, L-030).
- Now: the statement lights "where", "tonight" and "shortlist" in volt (page.js:91; hero-depth.css:97). That is on top of "CUET 2027." and "MockMob".
- Sources: ui-ux-standards.md:73 ("a single accented word in a headline"); commit b6c40be4 (it removed the "where." highlighter).

**T4. Numbered badges and monospace counters used as decoration.**
- Code: `padStart(2,'0')`, the patterns "01 / 10" or "01", or mono on labels.
- Pass: none. Show the step as words or as the progress bar alone.
- Now: FeatureTour.jsx:190 ("01 / 10" in mono, feature-tour.css:20); `span.ml__num` "01" in volt (Score Recovery Lab steps).
- Sources: ui-ux-standards.md:73 and 152; impeccable "Tiny numbered section labels"; pixelslop #12 "Monospace Tech Vibes".

**T5. Hero-metric typography: a big number with a small label in strips, and count-up tickers.**
- Code: font-size of 24px or more on text that is only digits and symbols (pixelslop #6 flags 2 or more), or a requestAnimationFrame count-up.
- Pass: at most one figure band on the page. Its numbers explain something ("5,765 questions in one bank"), not trivia, and none counts up.
- Now:
  - Hero proof strip: page.js:228-233 ("5 questions / 73 / 2 screens / 60 min", hero-depth.css:61-66).
  - LiveStatsBand count-up: LiveStatsBand.jsx:9-34.
  - Instagram strip "199K+ / 100K+ / 690+" in glass over a glow, and reel cards with "161K" in 2.6rem volt (social-proof.css `.rl__reach b`).
- Sources: impeccable "Hero metric layout: Used everywhere, trusted nowhere"; pixelslop #6; Magic UI "Number Ticker"; ui-ux-standards.md:63.

**T6. Middle-dot meta strings.**
- Code: `' · '` joins.
- Pass: none. Use two short lines or one sentence.
- Now: "Free to start · Pro ₹99 a month · Cancel anytime" (page.js:203; heroTaps.mjs:51).
- Sources: ui-ux-standards.md:109 (T-124).

### Layout and composition (L1 to L7)

**L1. On the phone's first screen, the mascot and decoration come before what MockMob is (LK70).**
- Code: `h1.getBoundingClientRect().top / innerHeight`, and the words above it.
- Pass:
  - The words "CUET", "mock" and the product promise sit in the top 40% of a 390x844 screen.
  - The mascot shares the screen with them; it does not stack above them.
- Now:
  - At 390x844 the nav plus the painted room take 0 to 381px: 45% of the screen. `--room-h: clamp(17rem, 38svh, 20rem)` is at hero-scene.css:165.
  - The only words in that band are "Hi, I'm Mobi. Tap me."
  - The h1 starts at 393px (47%).
  - With browser bars, the visible height is about 700 to 750px (an estimate), so the room is more than half of what shows.
  - Duolingo's phone hero puts its cast, the sentence saying what it is, and one key all in one screen (shots/ref-duolingo-390-00-top.png).
- Sources: LK70; ui-ux-standards.md:58; AGENT_RULES.md:27.

**L2. The phone and desktop heroes tell different stories (LK67).**
- Code: compare what is visible at 390 and at 1440.
- Pass: one hero idea on both, with the same Mobi role.
- Now:
  - Phone only: the room and a tap-cycling Mobi (hero-scene.css:150-246; `.lp-room` is display:none at 761px and up, :50-52 and :286).
  - Desktop only: a host Mobi beside the sample, plus the pointer spotlight (hero-scene.css:285-307; landing.css:272-276).
- Sources: LK67; L-003.

**L3. A stat or proof bar under the hero.**
- Code: a row of 3 to 4 cells, each with a big number and a label, directly after the hero.
- Pass: proof that shows the product working (the sample, a real screen), not trivia.
- Now: page.js:228-233, in glass (C7) with hero-metric type (T5). "2 screens" and "60 min" are facts, not proof.
- Sources: impeccable "Hero metric layout"; AGENT_RULES.md:27.

**L4. Nested cards and stacked frames (the "cardocalypse").**
- Code: an element with radius above 4px plus a border or shadow inside an ancestor with the same. pixelslop #9 flags more than 1.
- Pass: 2 levels at most (a section surface plus the product screen).
- Now:
  - The hero demo is 4 layers: the bay frame (`.lp-stage::before`), the card, `.mm-screen`, and two fake stacked cards under it (home-refinements.css:13-31).
  - The Compass Pro glass card holds a list of bordered cards (compass-ladder.css:52, 60).
  - The Lab frames show a card inside a bay with row cards inside.
- Sources: impeccable "Nested cards", "Cardocalypse"; Fountain Institute tell 5, "Cards on cards"; ui-ux-standards.md:62.

**L5. Rows of identical icon-plus-label tabs, and icon tiles above labels.**
- Code: 3 or more siblings that each carry an svg icon plus a short label.
- Pass: icons only where they speed up recognition. No icon-tile row.
- Now:
  - The tour rail has 10 tabs, each with a lucide icon (page.js:124-153).
  - The Lab steps (Time, Changes, Repair, SWOT) are icon squares above labels.
  - 14 lucide imports across the landing files.
- Sources: impeccable "Icon tile stacked above heading", "Identical card grids"; 925studios ("thin-line, interchangeable icons"); W-076 ("no icon grids").

**L6. The same section template stamped down the page.**
- Code: count the `lp-head` blocks with the same kicker, h2, sub and component order.
- Pass: vary composition by role (a statement band, a held story, a tool, proof), not one template.
- Now: 8 `lp-head` blocks (page.js:268-272, 280-283, 291-296, 306-311, 336-341, 371-375, 384-387 and 397-400), all left-aligned, with the same rhythm.
- Sources: impeccable "Copy-Paste Layouts", "Monotonous spacing"; pixelslop S11.

**L7. Product shots that are not the product, or that copy someone else's UI (LK72).**
- Code: product screens built in landing CSS rather than from the app's own components; third-party palettes.
- Pass: the screens shown are the real MockMob screens (or built from their components) and the copy matches. The NTA comparison shows MockMob's own better screen, not an NTA clone.
- Now:
  - TourScreens are "labelled illustrations" (page.js:120-122).
  - The exam band's NTA mode copies the NTA palette, including purple radial "review" bubbles (home-refinements.css:163).
  - The exam band is a hand-made `.lp-exam` (home-refinements.css:84-228).
- Sources: LK72; AGENT_RULES.md:27; zr37ibqXl1U case 1 [T007], "real product preview beats generic art".

### Imagery and mascot (I1 to I3)

**I1. Generic decorative geometry and placeholder art.**
- Code: decorative circles, orbits, dashed rings and monogram discs drawn in CSS.
- Pass: none. The owned illustrations stay: the painted rooms, the lamp-lit subject objects and the college photos.
- Now: reel cards with a volt circle and concentric halo rings, a dashed "orbit" and a mono "GJ" monogram (social-proof.css:14-17).
- Sources: impeccable "Placeholder-style illustrations"; Built In ("abstract shapes and floating figures").

**I2. A sparkles icon for anything AI.**
- Code: `Sparkles` or ✨.
- Pass: none.
- Now: page.js:6 and 139 (the "Ask Mobi" tab).
- Sources: NN/g, "The AI sparkles icon problem"; uxdesign.cc, "Nobody asked for the sparkle button".

**I3. The mascot as a toy or wallpaper rather than a character with a job (LK67, LK73).**
- Code: list each Mobi instance and its trigger.
- Pass: every appearance is tied to a moment in the student's task (pointing at the key, reacting to the sample answer, guiding the next step), with one render style and one light. No "tap me" toy on the hero. One Mobi in view (W-074).
- Now:
  - The hero bubble opens with "Hi, I'm Mobi. Tap me." (heroTaps.mjs:8) and cycles 6 tap lines.
  - Mobi stands in the room, hosts the sample, sits in 5 seats (page.js:297, 312, 335, 396, 446), rides the dock and the pip guide.
  - Desktop shows a floating Mobi in nearly every sampled viewport (contact-1440-night.png).
- Sources: Duolingo, "Building character" (Hartman, 2020): characters speak the exercise sentence and react after a correct answer; Duolingo, "Shape language" (Barker, 2020): "very few cleverly placed vector shapes", clear silhouettes; impeccable "Rough SVG illustrations: a crude hand-coded mascot".

### Motion (M1 to M7)

**M1. The same fade-up on every block.**
- Code: count the `<Reveal>` wrappers and the identical `opacity 0 → 1 + translateY` keyframes.
- Pass: one authored page-load moment. Sections enter through their own story, not one shared fade.
- Now: about 20 `<Reveal>` blocks in page.js, plus the `lp-rise` stagger on the hero (landing.css, `[data-hero]`).
- Sources: ui-ux-standards.md:115 ("Do not stack identical fade-ups"); pixelslop S8 (stock reveal libraries); prg.sh (Oct 2025), "generic animations such as fades".

**M2. Infinite decorative loops in view.**
- Code: `document.getAnimations()` where iterations is Infinity and the target is in the viewport.
- Pass: loops only on Mobi's idle (breathing, blinking), and at most one on screen.
- Now: at 1440 there are 55 infinite animations across 17 viewports (about 3.2 each).
  - Most are Mobi's idle loops (`pip-breathe`, `pip-eye-blink`, `pip-read`), because a floating Mobi is in nearly every desktop viewport.
  - The rest: the shelf's subject objects floating forever (home.css:129, subject-object.css:121) and the tour's typing dots and Mobi eyes (tour-screens.css:115, 132).
  - The wall-of-love drift (social-proof.css:78) runs only when voices are published; it is absent in production today.
  - The marquee (landing.css:553) and the pill ping (landing.css:362) are dead CSS.
- Sources: ui-ux-standards.md:115 and 150; impeccable "Lazy Impact: badges float".

**M3. Overshoot or bounce easing on UI chrome.**
- Code: a `cubic-bezier` with its second y value at 1.3 or more (pixelslop #13).
- Pass: overshoot only on the character (Mobi). Chrome uses ease-out.
- Now:
  - Theme toggle: marketing-theme.css:43 (1.56) and :50 (1.4).
  - Shelf settle: hero-depth.css:205 (1.3).
  - The Mobi appear at hero-scene.css:257 (1.4) is allowed.
- Sources: pixelslop #13; impeccable "Bounce or elastic easing".

**M4. Held scroll stories whose step depends on scroll speed and position (LK69).**
- Test: at 390 with touch, a fast flick (300px in 80ms) must advance exactly 1 step, and a slow drag (120px over 1.2s) must settle on a step, never between two.
- Pass: one gesture equals one step, every time (L-027, LK69).
- Now: ScrollStory.jsx:8-14 picks the step from an IntersectionObserver on "beats" crossing the middle of the window, and leaves wheel and touch to the browser "at the reader's own speed" (the LK47 fix of 2 Nov). So a flick crosses several beats and a slow drag can rest between them.
  - The non-pinned tour track already uses `scroll-snap-type: x mandatory` with `scroll-snap-stop: always` (feature-tour.css:30-31).
  - The pinned tour switches it off (feature-tour.css:126).
- Sources: L-027; LK69; LK47 (both must hold).

**M5. Stock component-library motion recipes, used as is.**
- Code: a word-by-word scroll reveal from about 0.2 opacity, count-up tickers, marquees, and pointer spotlights.
- Pass: use only the ones re-made in MockMob's own grammar. For example, a statement can fill like answer bubbles rather than fading grey words up.
- Now:
  - The statement words start at opacity 0.18 (hero-depth.css:98-109). The dim words are 1.64:1 on the ground, so they are unreadable until lit.
  - Count-up: LiveStatsBand.jsx:9-34.
  - Pointer spotlight: HeroBackdrop.jsx.
- Sources: Magic UI "Text Reveal", "Number Ticker", "Marquee"; Aceternity "Spotlight", "Text Generate Effect"; rectangle.substack, "The Linear effect" (Ginn, 2023), on imitators copying the surface: dark, blurred gradients, "animated glowing artefacts".

**M6. Typing and entry effects done badly (a risk for LK74).**
- Slop: a caret that blinks forever on static copy, one span per letter read out by screen readers, the line length jumping as words swap, the message held back, a loop that never ends, a 2 to 3 second splash on every visit.
- Pass:
  - The full sentence is in the DOM from the first paint.
  - The animated slot is `aria-hidden` and has a reserved width (CLS 0).
  - It types once, in about 1.5s or less, then rests with no blinking caret.
  - Reduced motion shows the whole line.
  - Any loading animation runs on the first visit only, takes about 0.8s or less, never covers the LCP text, and is skipped on repeat visits.
- Now: the h1 is static (heroLines.mjs:1-9, the R3 H1 ruling). It used to be typed, and commit b6c40be4 had a typed line behind a thin caret with a constant 212px slot. L-016 still asks for a typed line or a per-letter morph.
- Sources: cyishere.vercel.app, "a11y of typewriter animation"; mtgdev.netlify.app ("keep the text fully in the html from the start"); impeccable "Decorative blinking cursor"; ui-ux-standards.md:115 and 122 ("Never delay a usable control behind an animation"); L-016; L-043.

**M7. Pointer-only effects that make a parity gap.**
- Code: `(hover: hover) and (pointer: fine)` gates on visual effects.
- Pass: no essential or signature effect exists on one platform only (L-003).
- Now: the volt dot spotlight (HeroBackdrop.jsx:17-19; landing.css:272-276) and the hovered option's volt edge are desktop-only.
- Sources: L-003; ui-ux-standards.md:97.

### Copy and truth (W1 to W5)

**W1. Negative parallelism ("not just X", "Not X. Y.").**
- Code: grep `/not just|\. Not /i`.
- Pass: at most 1 on the page.
- Now: 3 instances:
  - "Fix why you got it wrong, not just the answer" and "Fix why you missed it. Not just the answer." (page.js:127);
  - "Repair the reason, not just the answer" (LabCinema.jsx:35).
- Sources: aismells "It's Not X — It's Y" (the most-flagged tell) and "Countdown Punch"; impeccable "Forced contrast".

**W2. Staccato fragment tricolons, as a density problem.**
- Code: 3 or more short sentence fragments in a row.
- Pass: at most 1 cluster on the page.
- Now:
  - h1 "CUET 2027. One mock. Know what to fix." (heroLines.mjs:11).
  - "Practise. Replay. Repair." (page.js:282).
  - "Take a timed mock. See exactly where every mark went. Fix the right chapter tonight." (page.js:195).
  - "Fix it once. Check it holds." (page.js:293).
  - "Five questions. Your move." (page.js:447).
- Sources: aismells "Always Three Things"; tropes.fyi; the Wikipedia "Signs of AI writing" guide, via aismells.

**W3. Text walls (LK71).**
- Code: count the words per viewport in each section.
- Pass:
  - each tour slide body at most about 25 words, plus 2 short points;
  - each section sub at most about 20 words;
  - nothing over about 60 words in view on a phone, except the FAQ.
- Now:
  - Tour bodies run 23 to 45 words, with 2 to 3 points and a chip (page.js:124-153). The Mob slide's body is 45 words.
  - One Ask Mobi point alone is 27 words (page.js:141).
  - The Lab sub is 27 words (page.js:271).
- Sources: LK71; impeccable "Redundant UX Writing", "Line length too long".

**W4. Pseudo-evidence by form.**
- Code: "+"-rounded counts, trivia in proof slots, a "Live demo" label on a scripted loop.
- Pass: every figure is sourced and is a figure a student cares about.
- Now: the numbers are real (read from the capability gates and the stats API). The form still reads as template: "199K+ / 100K+ / 690+" and "2 screens" (T5, L3).
- Sources: 12-part test item 9 (ai-slop-independent.md:50); AGENT_RULES.md:5-6 and 11.

**W5. Hype clichés, exclamation marks, generic CTA labels (a guard).**
- Code: grep for elevate, seamless, unleash, next-gen, supercharge, world-class, delve, "!", and "Get started" or "Learn more".
- Pass: none.
- Now: passes. There are 0 hits in page.js and the landing components, and the CTAs are specific ("Try Mistake Repair", "Plan my subjects").
- Sources: ui-ux-standards.md:107; impeccable "Generic marketing claims".

## (b) What premium, owned brands do in dark mode instead

These are measured where the page was reachable on 4 Nov 2026. Shots are in `shots/ref-*`.

**Linear** (linear.app; shots/ref-linear-1440-00-top.png)
- Body #08090a, a neutral near-black.
- Borders are neutral, alpha 0.05 to 0.12 (median 0.08).
- 0 to 1 accent-coloured text runs per viewport (one blue "@Linear" link), 0 glows, 0 patterns.
- The hero is white type plus the real product UI. Colour appears only in tiny functional icons (a star, a PR icon).
- Its 2024 redesign generated themes from 3 variables (base, accent, contrast) in LCH instead of 98. Its aims were to "reduce visual noise" and to "return to a more neutral and timeless appearance" by limiting coloured chrome (linear.app/now/how-we-redesigned-the-linear-ui, 28 Mar 2024).

**Raycast** (raycast.com; shots/ref-raycast-1440-00-top.png)
- Body #07080a.
- There is one huge, owned key-art: its own logo stripes, rendered as blurred red light. It is the only colour, and the headline and keys are white and neutral.
- Lesson: if anything glows, it is the brand's own mark, once, as art. It is not sprinkled on cards, edges and buttons.

**Arc** (arc.net, now a farewell page; shots/ref-arc-1440-00-top.png)
- #0b0b0b.
- Colour lives only in the logo. The headline is a serif display, and the key is a neutral grey pill.

**Robinhood** (Oct 2024 identity)
- Robin Neon #ccff00 is the same family as volt: hsl(72,100%,50%) against volt's hsl(68,100%,47%).
- Its palette is "rooted in black, white and neutrals, with purposeful pops of Robin Neon", under a "less is more" ethos (robinhood.com/us/en/newsroom/a-new-visual-identity).
- The approved pairing is black on neon (#000 on #ccff00). Effects such as gradients and shadows are banned on the mark (docs.robinhood.com/chain/brand-guidelines).

**Nike Volt**
- "Limit the use of Volt to accents that do not cover a large amount of space."
- The core palette is black, white and tonal greys (gps.standards.nike.com/Brand/color-theory).

**Duolingo** (light web, owned characters; shots/ref-duolingo-390-00-top.png)
- On a phone, the first screen holds the character cast, the sentence saying what it is, and one primary key.
- The key is a flat fill with a solid, darker 4 to 5px bottom edge: tactile depth with no glow. MockMob already owns this keycap (`--btn-edge`, marketing.css:250).
- Characters must resemble Duo and are built from simple geometric forms. They appear at task moments, speaking the sentence and celebrating a correct answer (blog.duolingo.com/building-character, 2020; blog.duolingo.com/shape-language-duolingos-art-style, 2020).

**Spotify** (third-party reconstructions, not official)
- #121212 base, with elevation by tonal steps (#181818, #1f1f1f).
- Green is kept for the primary play key and the CTA; secondary keys are white.

**Wise** (third-party reconstructions)
- The lime #9fe870 is a fill carrying forest green #163300 ink, never white text on the lime.

**Not measured**
- Revolut returned a Cloudflare human check, which was not bypassed. Its shots are invalid.
- HIGH (high.live), the owner's 13 Oct reference, was not captured in this run.

**What this means for MockMob Night** (an interpretation from the above)
- **The light source.** MockMob's own light is warm lamp light: the painted rooms, the lamp-lit subject objects and the shelf lamp (home.css:68). Where Night needs atmosphere, use that amber pool, never lime.
- **Volt.** Use it as fills with dark ink: the one key, the selected chip and Mobi.
- **Edges and surfaces.** Edges are neutral at alpha 0.06 to 0.12, and surfaces step up in neutral greys.
- **Hierarchy.** It comes from Bricolage type and the real product screens, not from lit outlines.

## (c) The traps of a lime or volt accent on near-black, with MockMob's numbers

1. **Brightness.** Volt's relative luminance is 0.760, which is 85% of the white ink. On #0b100e that is 14.8:1. Contrast passes WCAG easily, so it is never caught as an accessibility fault. But every lime word competes with the white headlines and, being 100% saturated, reads as a highlighter. On Day the same role is #526700 (5.81:1, dark olive), which is quiet.
2. **Edges.** A 50% volt line composites to #6f8007 (90% saturated, 4.35:1). A neutral hairline is 1.23:1. A 1px lime border is 3.5 times louder than the structure. Doubling it (a border plus an inset ring, feature-tour.css:13 and compass-ladder.css:8) makes it a neon tube.
3. **Olive fog.** Yellow-green at low alpha over near-black cannot make a clean tint. It turns muddy olive or khaki: 8.5% gives #1c230d, 16% gives #2b340c and 22% gives #37410b (hue 71 to 79°, 46 to 71% saturation). Lime washes read either dirty or as glow. This is the 10 to 14% tint peak in the Compass Pro and Combo Planner frames.
4. **Glow costs nothing on dark.** A lime shadow that is invisible on Day paper becomes visible light on Night (tour-screens.css:14 and 41). Every volt shadow, ring and wash written for Day turns into a glow at night.
5. **A tinted ground.** The green-tinted near-black (#0b100e, hue 156°) plus a yellow-green accent tips toward a night-vision, terminal or "cyber" monochrome. It also pulls the greys green (ink-3 #9aa795 is hue 103°). Neutral or warm charcoal keeps volt special.
6. **Flat surfaces force edges.** Raised #131a16 is only 1.08:1 above the ground, and the product screens are 1.03 to 1.16:1. Night therefore separates containers with borders, and the system's "active" border token is lime. Day separates the same screens by about 15:1 of surface contrast, which is why Day reads premium and Night reads neon.
7. **Meaning collisions.** Volt is the brand, "correct" (mistake-lab.css:58), "right" counts, selected, progress, links and kickers. Every lime word then reads as a "correct answer" signal. Right and wrong states must also carry an icon or a word, never colour alone (ui-ux-standards.md:80).
8. **The accent budget is already spent.** The logo dot, Mobi's body and the primary keycap are volt in every viewport. Any further volt dilutes them. The pass rule (W-075 plus C9) is: Mobi, the logo dot, one key fill and at most one selected fill per viewport.

## Sources

Owner and project:
- C:/Users/atish/Desktop/AI OS/wiki/concepts/ui-ux-standards.md: §4 :68-75, §5 :77-86, §7 :99-112, §8 :114-125, §10 :143-166, §13 :199-234.
- mockmob-next/docs/research/premium-ux-ui-2026-10/AGENT_RULES.md: :5-11, :26-27, :31, :40.
- mockmob-next/docs/research/premium-ux-ui-2026-10/papers/ai-slop-independent.md: the 12-part test :40-53 and the rubric :67-69.
- mockmob-next/docs/research/premium-ux-ui-2026-10/papers/uxpeak-zr37ibqXl1U.md [T007].
- WEB-OWNER-LEDGER-2026-10-17.md: L-003, L-004, L-016, L-017, L-019, L-020, L-025, L-027, L-030, W-071, W-074 to W-078.
- OWNER-MASTER-LEDGER.md:699-711.
- OWNER-FEEDBACK-2026-10-31-LEARN.md:202-231.
- Continuum handoff 20261015T200157-6ee68362 (Hero v4, commit b6c40be4).

Installed skills:
- ~/.claude/skills/impeccable/reference/new-work.md:65.
- ~/.claude/skills/design-taste-frontend/SKILL.md:45-46, :101-103.
- ~/.claude/skills/redesign-existing-projects/SKILL.md:33-38.

Web:
- [impeccable.style/slop](https://impeccable.style/slop) and the [anti-patterns](https://2cd2d50e.impeccable-2rv.pages.dev/anti-patterns) page.
- [pixelslop AI slop pattern catalog](https://cdn.jsdelivr.net/npm/pixelslop@0.3.8/dist/skill/resources/ai-slop-patterns.md), which gives detection thresholds.
- [Fountain Institute, 7 tells](https://pages.thefountaininstitute.com/posts/7-tells-that-a-ui-is-ai-generated).
- [aismells: Gradient Fog](https://aismells.pages.dev/gradient-fog.html) and the [aismells writing smells](https://aismells.pages.dev/llms.txt).
- [925studios (Nov 2026)](https://www.925studios.co/blog/ai-slop-design-tells).
- [prg.sh (Oct 2025)](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website).
- [devtake (Jun 2026)](https://devtake.pages.dev/article/ai-generated-frontend-slop).
- [Built In, Donska (Jun 2026)](https://builtin.com/articles/ai-design-slop-era).
- [RAXXO, dark mode that doesn't look AI](https://dev.to/raxxostudios/dark-mode-design-that-doesnt-look-ai-2cn3).
- [The Linear effect (Ginn, 2023)](https://rectangle.substack.com/p/the-linear-effect).
- [Linear redesign part II (2024)](https://linear.app/now/how-we-redesigned-the-linear-ui).
- [Android/Material dark theme colour](https://developer.android.com/design/ui/wear/guides/m2-5/styles/color).
- [Robinhood identity (2024)](https://robinhood.com/us/en/newsroom/a-new-visual-identity) and its [brand guidelines](https://docs.robinhood.com/chain/brand-guidelines/).
- [Nike colour theory](https://gps.standards.nike.com/Brand/color-theory).
- [Duolingo, Building character](https://blog.duolingo.com/building-character/) and [Duolingo, Shape language](https://blog.duolingo.com/shape-language-duolingos-art-style/).
- [NN/g, the AI sparkles icon problem](https://nngroup.com/articles/ai-sparkles-icon-problem/).
- [a11y of typewriter animation](https://cyishere.vercel.app/blog/a11y-of-typewriter-animation).
- [Aceternity components](https://ui.aceternity.com/components) and [Magic UI components](https://magicui.design/docs/components).
