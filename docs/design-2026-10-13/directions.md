# MockMob: three design directions (brand and app)

Date: 13 October 2026. Written by the design director for the owner's decision. This is a proposal, and nothing in it is built yet.

Inputs, all read in full: `owner-materials.md`, `ref-high.md`, `ref-revolut.md`, `ref-fampay.md`, `onboarding-research.md`, `flutter-feasibility.md`, the owner's UI/UX standards (`AI OS/wiki/concepts/ui-ux-standards.md`), `DESIGN.md` (web tokens, Night Arena), `APP-DESIGN-SPEC.md` (sealed sheet A1, 5.6, 6.x), and the Galaxy M06 screenshots in `tmp/app-shots/m06` (01 Welcome, 03 sample question, 12 sample result, 20 You, 28 Appearance dark, 31 Practice dark, among others).

How to read it. Section 0 covers what every direction shares. Sections A, B and C are the three directions, each with the same eleven subsections, so they can be compared line by line. Section D compares them, E gives the recommendation, and F lists the owner decisions and the next steps. All numbers in sample copy are either real 2026 DU data (marked "2026") or sample values for concept renders (marked "sample").

---

## 0. The brief, and what every direction shares

### 0.1 What we are replacing, in one paragraph

The current app is a paper or charcoal ground with identical white keycap rows, a static Mobi sticker, a stock Material tab bar that covers content, and defensive copy at the foot of nearly every screen ("MockMob is not affiliated with NTA or Delhi University", "Sample questions. This is not a diagnosis.", "Practice, not proof", "Uses 10 credits. You have 100."). The onboarding peak, the sample result, is a "4 of 5" and a dashed box that explains what the app cannot do. Today, Splash and the runner are route placeholders. The owner called it "really basic", "rudimentary" and "not interactive at all", and asked for "a really fancy UI: something premium, something which inspires people to use the app", with high.live, Revolut and Fampay as the vibe.

### 0.2 The bar each direction is held to

- **Authored, not assembled.** One central idea per direction, visible in every screenshot, in the owner's words "built around its own central idea".
- **Premium means it looks expensive and is fun to use.** Fun and useful go together for this owner ("a really nice UI, which makes it really fun to use. It is also useful").
- **Fewer, stronger ideas.** The owner also punishes excess ("Reduce rather than decorate", "Maybe you have overdone the lighting"). Each direction names its single loud move and keeps everything around it quiet.
- **Smooth on the M06** (Mali-G57 MC2, 3.5 GB, about 384 x 853 dp, 90 Hz to be confirmed): at most two live blurs on screen, fake glass from cached art everywhere else, transform-and-spring motion, WebP art at 2.0x.

### 0.3 Integrity rules every direction keeps (behaviour, not footers)

1. Success, "Saved", haptic success and celebration fire only after the server acknowledges.
2. No invented numbers: no user counts, testimonials, percentiles, chances, or "top 10%". Real 2026 DU figures are labelled as 2026.
3. Practice, repair, fresh check and retained check stay distinct states in data and UI, shown by structure (Found, Fixed, Checked), never by a "practice, not proof" tagline.
4. No recovered-marks, admission-chance or "mastered" claims.
5. Nothing decorative during a timed mock: no correctness, no Mobi, no motion beyond the timer and save state.
6. Celebration is proportional: never after a poor or held result, never per question, once per event id.
7. A reveal never withholds a result: tap, TalkBack action and "Open results directly" always work, and the ritual decays from the fourth sheet (spec 5.6).
8. No punitive streaks, no variable or paid-random rewards, no guilt notifications.
9. Glass carries text only at a tint that holds 4.5:1 over its worst backdrop. Targets are at least 48 dp, every control is named for TalkBack, and reduced motion keeps the same information.
10. No build talk (route names, codes, service names) in any user-facing build.

### 0.4 What every direction removes

The Welcome non-affiliation footer, every "sample, not a diagnosis" caption, "Example, not your plan yet", "The five sample questions are the same for every paper", "On this phone" on guest screens, every "Practice, not proof" tail, "This only decides your data settings", and the cost-first lines as the headline of a row (the cost moves to the confirmation sheet, written as what you get: "10 questions, about 10 minutes. 10 credits."). The non-affiliation statement and official sources live in You > About and in the Play listing's full description, which is where every competitor puts it (`onboarding-research.md` 6.1).

### 0.5 Where the owner's new direction overrides the older standards, and where it does not

| Older rule (UXS, APP-DESIGN-SPEC) | Now | Still binding |
| --- | --- | --- |
| No glass or blur on content | Glass on floating parts (dock, sheets, overlays, controls over art); fake glass on hero cards over our own art | No glass under question text, options, explanations or result figures |
| No gradients or glow | Gradients allowed as environment (subject light fields, chapter bands, scrims), one functional light per screen | No gradient text, no neon halos on controls, no glow on ordinary cards |
| Dark ground must be neutral charcoal | Kept (all three grounds stay near-neutral) | Yes |
| Mobi never speaks, poses only | Mobi may say one short factual line in onboarding, empty states and celebrations (owner decision F.1 item 4) | Never during timed answering, never evaluative of the person, never guilt |
| No confetti, no particles | Restrained, real-milestone-only bursts drawn in one painter | Never after a poor result, never per question |
| Sentence case, no eyebrows, no emoji, no exclamation successes, no middle-dot strings, 12-hour time, tabular figures | Kept in all three | Yes |

### 0.6 Shared product structure

- **Onboarding is a data-driven step deck, not hand-built screens.** All three directions present the same 14-step backbone from `onboarding-research.md` section 5 (welcome, stage, course, colleges, what it takes, subjects and confidence, worry, one real question, rhythm, plan and pact, age plus save, reminders, first move), dressed in each direction's own metaphor. Each step is a row in a versioned deck (id, type, copy keys, branch rule, field written, and a required "what visibly changes" line). Courses, colleges and cutoffs come from the DU 2026 index already in the repo; the warm-up question comes from an approved per-subject pool. This is the answer to "not even scalable": a new subject, exam or year changes data, not screens. The five-question sample stays on the website.
- **Account timing.** After the plan reveal, never before. The age check sits on the same screen, before the account buttons. "Continue with Google" (Android Credential Manager bottom sheet, one tap when a Google account is on the phone) is the first and largest option, "Use an email code" second, "Not now" always visible. Everything before that stays on the phone.
- **Permission priming.** Notifications are asked after the account, with a preview of the student's own reminder, and "Remind me" and "Not now" at equal weight. Usage-data consent for adults moves to after the first result (D5 in the onboarding research).
- **Learn.** A whole tab that says "Learning is not available right now" goes. Each direction folds Learn into the mistake loop (concepts open from the mistake they explain) until Learn has content of its own.
- **Spine untouched.** api, auth, repositories, storage, sync and the session engine, routes and redirects, and all the providers stay. Theme, dock, keycap, sheet, splash, screens and copy are replaced (`flutter-feasibility.md` 14).

---

## Direction A: "Bubble"

### A.1 The idea

**Core idea:** MockMob turns the OMR answer sheet, the most feared object in Indian exams, into a toy you want to fill. The filled bubble is the logo, the dock lens, Mobi's head, the progress grammar and the reveal.

**Mood:** juicy, liquid, tactile, bright, playful but sharp.

**What it looks like in one screenshot:** a deep chapter-hue band at the top with a glossy inflatable object floating in it, a big volt bubble you want to press, and a row of bubbles telling you exactly where you are.

**References and how it stays original:**
- From HIGH: one hue per chapter (here, per subject), baked glossy 3D props with an idle float, the spring letter reveal for big moments, the foil milestone screen.
- From Revolut: one big number per hero, digits that roll, an input that morphs into its result.
- From Fampay: an identity object built during onboarding, the friend voice.
- Original because: the bubble is exam-native, and no fintech or edtech app owns it. Liquid glass becomes literal (a drop of ink filling a bubble) instead of decoration. The type is wide and round (Unbounded), not condensed, so it never reads as HIGH's black, lime and compressed-caps console. The hues are MockMob's own, not HIGH's violet, indigo, pink and coral.

### A.2 Brand

- **Wordmark:** `mockmob`, lowercase, Unbounded 700, tracking -2%. The o in "mock" is a hollow ring and the o in "mob" is a filled volt bubble with a small specular highlight at 10 o'clock: one question open, one answered. In motion the second o fills from the bottom like ink (320 ms, the Fill curve).
- **Mark:** "the filled bubble". A volt circle with a soft top-left highlight shaped like a short tick stroke. App icon: the bubble at 62% of the adaptive-icon safe zone on Ink `#141414`. The monochrome themed icon is a ring with a tick.
- **Palette.** Dark ("Ink") is the default; light ("Paper") is a full theme, not an afterthought.

| Role | Dark (Ink) | Light (Paper) | Notes |
| --- | --- | --- | --- |
| Ground | `#141414` | `#F4F5F0` | Neutral, per the owner's dark-mode rule |
| Raised | `#1E1E1F` | `#FFFFFF` | Cards, rows |
| Raised 2 | `#29292B` | `#EAECE3` | Inputs, segmented tracks |
| Hairline | `#2E2F31` | `#D9DCD0` | |
| Ink (text) | `#F6F6F2` | `#10140E` | |
| Ink 2 | `#BDBEB7` | `#3E453B` | |
| Ink 3 | `#8C8D86` | `#5C6357` | Min for captions, 4.5:1 checked on ground |
| Volt (action, done) | `#D2F000`, text on it `#0B1000` | Fill `#D2F000`; volt as text `#526700` | Only for the primary action, filled bubbles and the active tab |
| Wrong | `#FF6B5B` ring, text `#FFB4AA` | `#C2361F` | Always with a word or glyph |
| Accountancy (Tangerine) | `#FF8A3D` | `#C85A12` | Chapter band gradient `#FFB070` to `#FF8A3D` to `#E0661A` |
| Business Studies (Cobalt) | `#3D6BFF` | `#2346C7` | `#7C97FF` to `#3D6BFF` to `#2A4FD6` |
| Economics (Bubblegum) | `#FF5FA2` | `#C42E72` | `#FF92C2` to `#FF5FA2` to `#DD3E83` |
| English (Lilac) | `#A98BFF` | `#6B4FD1` | `#C9B5FF` to `#A98BFF` to `#8A69F0` |
| General Test (Aqua) | `#22C7C7` | `#0E8A8A` | `#6EE0DF` to `#22C7C7` to `#11A3A6` |

Subject hues appear only in their subject's region (chapter band, subject card, subject chip). A screen never shows more than one subject hue plus volt.

- **Typography** (all OFL, bundled, variable files):

| Role | Family | Size / line / weight | Notes |
| --- | --- | --- | --- |
| Moment headline (welcome, reveals, milestones) | Unbounded | 32/36 sp, 700, -2% | Wide face: about 14 characters per line at 352 dp, so moment lines are written short |
| Hero number | Unbounded | 72 to 96 sp, 800 | Tabular figures to be verified with fonttools; fallback numerals Gabarito ExtraBold (has `tnum`) |
| Screen title | Unbounded | 24/30 sp, 600 | |
| Card title | Figtree | 18/24 sp, 700 | |
| Body | Figtree | 16/24 sp, 400 | Questions and explanations 17/26 |
| Label, button | Figtree | 15/20 sp, 650 | |
| Caption | Figtree | 13/18 sp, 500 | Smallest size in the app |

- **Mobi: restyle.** Mobi becomes a living bubble: a spherical volt head with a black glossy visor band and two white pill eyes, a short soft body, stubby arms, in the finish of a soft-vinyl designer toy. It is rebuilt as a code rig (head, visor, eyes, antenna, body, arms as separate WebP layers of 5 to 15 KB each) so it can blink, look at the last touch, squash on tap and fill its head with ink on a success. Why: the mascot becomes the system's atom, and a toy-grade finish reads as premium collectible rather than clip art.

### A.3 Material system

| Material | Where | Recipe |
| --- | --- | --- |
| Liquid glass with refraction | One place only: the dock's volt lens | 56 x 44 dp lens shader (`ImageFilter.shader`) magnifying the icon under it 1.06x with a top-left specular, only if benchmark B6 passes; otherwise tint plus edge light |
| Frosted glass (live blur) | Dock body, bottom sheets | `BackdropFilter.grouped`, sigma 20 (dock) and 24 (sheets); tint `#1E1E1F` at 0.66 dark, `#FFFFFF` at 0.76 light; 1 dp edge light (white 18% at the top to 4% at the bottom) |
| Tinted fake glass | Onboarding "Your sheet" card, Today hero card over the chapter band, recap cards | Pre-blurred slice of the chapter band (quarter resolution), tint white 14% (dark) or 60% (light), edge light |
| Solid | Question runner, options, explanations, result figures, lists, settings | Raised tokens, no texture |
| Full-bleed colour | Chapter bands (top 240 to 280 dp of Today, a subject's Practice page, the recap) | Code-drawn 168 degree three-stop gradient plus a white radial highlight at 74% / 8% (alpha 0.28), 2% grain tile at 4% opacity to stop LCD banding |
| Props | Chapter bands, onboarding, empty states, milestones | WebP with alpha, at most one per screen |

Light: a single soft specular on bubbles and props from the top left. Depth: hue-tinted soft shadows under props and the hero card (`0 16 32 -18` in the subject hue at 35%). No glow on cards, ever.

### A.4 Signature motif

**The bubble row.** Every screen carries one row of bubbles that holds real state: questions in a mock, days in the week, steps in onboarding, mistakes in a fix. Filled volt means done, a half-filled liquid bubble with a wavy surface means in progress, a ring means open, a dotted ring means a rest day. A volt bubble with a highlight, and a row of bubbles under it, makes any screenshot recognisable.

### A.5 Navigation: the bubble dock

- **Destinations (4):** Today, Practice, Fixes, You. Review is renamed **Fixes** because the tab is the repair queue and "fix" is the product's verb. Learn folds into Fixes (each mistake opens its concept card) and into a "Concepts" shelf inside Practice. It returns as a tab only when it has content of its own.
- **Shape:** a floating pill, 64 dp tall, inset 16 dp from the sides and 10 dp above the gesture inset, radius 32. Four equal 84 dp slots, so the outer size never changes during animation.
- **Material:** frosted glass (A.3), edge light, a soft shadow `0 18 36 -20` black at 45%.
- **Indicator:** the volt lens, a 56 x 44 dp liquid bubble behind the active icon and label. On a switch it travels on `Springs.smooth` (380 ms, bounce 0.18) and stretches with velocity, up to 1.22x wide and 0.86x tall, like a droplet sliding on glass. On arrival it settles with one small overshoot.
- **Icons:** a custom 24 dp set on a 2 dp grid with round terminals, each built on a circle. Today is a bubble with a rising arc, Practice a pencil tip touching a bubble, Fixes a bubble with a tick being drawn, You is Mobi's head. Inactive: 1.75 dp outline in Ink 2. Active: filled, Ink on volt. Labels are always visible: 12 sp Figtree 650.
- **Press:** the slot scales to 0.94 on `Springs.snappy` (240 ms), and the lens brightens 6%.
- **Drag:** sliding a finger along the dock scrubs the lens across tabs, with a `selectionClick` at every boundary.
- **Haptics:** `selectionClick` on a tab change and each drag crossing. Nothing on a re-tap (re-tap scrolls to the top).
- **Scroll:** scrolling down by more than 24 dp scales the dock to 0.92 (transform only), and it returns on scroll up or after 600 ms idle. It is never hidden on tab roots, and it is hidden on the runner, repair and result screens.
- **Badge:** Fixes carries a small number bubble with the real count of mistakes waiting.
- **TalkBack:** "Fixes, tab 3 of 4, 6 waiting."

### A.6 Onboarding: "Fill your sheet" (14 screens)

A persistent **Your sheet** card (fake glass, 112 dp collapsed) sits at the top of steps 3 to 10. It has six labelled bubbles: Stage, Course, Colleges, Subjects, Worry, Rhythm. Each answer fills its bubble with the Fill animation and writes the short answer under it. The sheet is the progress indicator, so there is no separate bar. Skip fills a bubble with a dotted "default" ring.

**1. Cold open.** Purpose: the first brand moment. Layout: Ink ground; one volt bubble drops into the centre on `Springs.bouncy`, fills with ink from the bottom, and the wordmark types out around it (letters rise with overshoot, 26 ms stagger). 1.6 s. Haptic: `lightImpact` when the bubble fills. Tap skips. Reduced motion: the wordmark fades in over 200 ms. This screen also precaches the art and the lens shader.

**2. Welcome.** Purpose: promise and first identity beat. Layout: the top 55% is the baked hero (A-3): a tilted answer sheet spilling glossy bubbles in volt and the five subject hues, with Mobi sitting on the highest bubble and waving (the rig waves; the cascade drifts 6 dp). Below:
- Headline: "Fill the sheet. Chase the seat."
- Support: "MockMob finds where your CUET marks leak, helps you fix each leak, then checks the fix held."
- Inputs: "Build my plan" (volt), "I already have an account" (text button).
- Payoff: the promise, in under three seconds, with no footer.

**3. Stage.** Purpose: the timeline without asking for a date.
- Headline: "Where are you right now?"
- Support: "This decides how many weeks we plan for."
- Inputs: four large bubble tiles: "Class 12, writing CUET 2027", "Passed Class 12, writing CUET 2027", "In Class 11", "Not sure yet".
- Payoff: the Stage bubble fills, and a countdown rolls in under the sheet: "About 30 weeks to the expected May 2027 window." (computed from the device date, labelled expected, hidden if the date is past). Class 11 branches to an early-access card.

**4. Course.** Purpose: the goal first.
- Headline: "Which course are you after?"
- Support: "Pick up to three. Counts are from DU's 2026 admissions."
- Inputs: two-line chips: "B.Com (Hons)" over "55 colleges in 2026"; "B.Com" over "44 colleges"; "B.A. (Hons) Economics" over "40 colleges"; "B.A. (Hons) Business Economics" over "10 colleges"; "BMS" over "9 colleges"; "BBA (FIA)" over "2 colleges"; "Another course or university"; "Not sure yet". A quiet link: "Not commerce?"
- Payoff: each selected chip's count pops (scale 1.0 to 1.12 to 1.0) and the Course bubble fills.

**5. Dream colleges.** Purpose: aspiration and a reference point.
- Headline: "Name your dream list."
- Support: "Up to three. Only colleges that offered your course in 2026."
- Inputs: a search field and college rows with a bubble selector; "Open to any college".
- Payoff: the names stack onto the sheet in Figtree 700, plain type, no crests.

**6. What it takes (first reveal).** Purpose: the first personal, real payoff, inside the first minute.
- Layout: the chapter band turns Tangerine; the number rolls digit by digit (600 ms) in Unbounded 88.
- Headline: "This is the bar at SRCC."
- Hero number: "924.3", with the label "B.Com (Hons), 2026 first list, UR".
- Supporting rows for the other picks: "Hindu College 919.9", "Hansraj College 907.5".
- Rule line: "B.Com (Hons) takes one language, Mathematics or Accountancy, and any two more from List B."
- Fit line: "English, Accountancy, Business Studies and Economics keeps all three open."
- Input: "Build my subjects".

**7. Subjects and how solid each feels.**
- Headline: "Your subjects, weakest first."
- Support: "Be honest. After your first check we'll show you where your gut was right."
- Inputs: each subject is a row with its hue bubble, name and a three-part control (Shaky, Okay, Strong). The four launch subjects carry "Practice ready"; General Test reads "Opening soon. We'll tell you the day it opens."
- Payoff: rows reorder live on `Springs.smooth`, and the line at the foot changes: "First up: Accountancy."

**8. Biggest worry.**
- Headline: "What keeps you up at 1 AM?"
- Inputs (pick one or two): "I lose marks on easy questions", "I never finish on time", "I don't know where to start", "The syllabus feels endless", "I forget what I studied", "English and GT scare me".
- Payoff: Mobi answers in one line, specific to the choice. For easy questions: "Easy marks first, then. That's where we start." For time: "Then we practise against the clock, short and often." The first-move preview on the sheet changes.

**9. One real question.**
- Layout: solid surface, no glass. A small title: "One question. Accountancy." The question is drawn from the approved warm-up pool for the weakest subject; options are A to D bubble keys.
- Correct: the chosen key fills volt, `selectionClick`, and the line "Clean. In 14 seconds." (the real measured time).
- Wrong: the chosen key gets a coral ring and the line "Classic trap. Here's the ten-second fix:" with a two-line explanation and the right key filled. No haptic on wrong.
- Inputs: "Next"; "Skip this one".

**10. Rhythm.**
- Headline: "Pick a pace you can keep."
- Inputs: minutes per session as three bubbles (10, 20, 30); seven day bubbles (M to S, four pre-filled); a time window (Before school, 6:00 AM; After school, 5:00 PM; Evening, 8:00 PM; Late, 10:00 PM).
- Payoff, live: "That's about 120 sessions before the expected window." (weeks left times days chosen). Rest days show as dotted bubbles with "Rest days are part of the plan."

**11. Your starter plan (the climax).**
- Layout: the sheet card expands to full screen (container transform, 420 ms) and prints three cards line by line, 90 ms apart.
- Headline: "Week one, sorted."
- Cards: "First move: starting-point check. 10 questions, Accountancy, about 10 minutes." "Rhythm: four evenings a week, 20 minutes, 8:00 PM." "Dream list: SRCC, Hindu, Hansraj. English, Accountancy, Business Studies and Economics keeps all three open."
- Line: "Built from your answers. Your first check sharpens it."
- Inputs: a press-and-hold volt bubble, "Hold to lock it in" (a ring fills over 1.2 s, `selectionClick` at a third and two thirds, `mediumImpact` on completion, Mobi's head fills with ink). A normal tap target "Lock it in" serves TalkBack and reduced motion. Secondary: "Change something".

**12. Save (age first, then the account).**
- Headline: "Keep your plan."
- Support: "It follows you to mockmob.in and your next phone."
- Age row first: "Quick one: are you 18 yet?" with "Yes", "Not yet", "Rather not say", and one line: "Under 18, usage tracking stays off."
- Then: "Continue with Google" (volt, Credential Manager sheet), "Use an email code", "Not now".
- States: "Saving your plan" while pending; "Saved to your account." only after the server acknowledges; on failure "Couldn't save. Your plan is still on this phone." with "Try again".

**13. Reminders.**
- Headline: "Want a nudge at 8:00 PM?"
- Layout: a glass notification preview: title "Tonight, 8:00 PM", body "Ten minutes of Accountancy is ready."
- Support: "Only on the days you picked. Never after 11:00 PM."
- Inputs: "Remind me" and "Not now", equal weight. "Remind me" opens the Android permission prompt.

**14. First move (the personalised reveal).**
- Layout: the sheet card shrinks and flies into Today's hero bubble (container transform); Today paints behind it, already built from the answers: chapter band in Tangerine, the countdown chip, the dream list, the week's bubbles.
- Headline on the hero: "Your first bubble."
- Inputs: the big volt bubble "Start the check" and the text button "Tonight at 8:00 PM".
- Payoff: they land in an app that already knows them.

### A.7 Today, result reveal, celebrations, streaks, return

**Today.**
- Top row: "Evening, Aanya." (sample name) and a glass chip "30 weeks to the expected window".
- Chapter band (260 dp) in the hue of the next move's subject, with that subject's inflatable object floating at the right (7.2 s bob).
- Hero card (fake glass on the band): "Fix 6 Partnership questions", "About 12 minutes", and a 64 dp volt bubble with a play glyph. For a new student: "Starting-point check. 10 questions."
- "This week": seven bubbles (filled on done days, dotted on rest days) and "3 of 4 sessions done".
- "Waiting to fix": the top three ranked rows, each with a subject bubble and a big outlined count.
- "Dream list": three names with their 2026 first-list figures in small type.
- If a received mock is unopened, its sealed bubble takes the hero slot (spec 5.3 result slot).

**Result reveal: "Pop the seal".** The server scores synchronously, so the sheet is openable at once.
1. A dark sheet with a 50-bubble grid, uncoloured, and one large volt seal bubble in the centre. "Hold to open" (or tap "Open").
2. Holding fills the seal; at full it pops (scale 1.0 to 1.08, then it splits into 10 droplets) and the droplets fly to the grid, filling bubbles in waves by section over 900 ms: volt for right, coral ring for wrong, hollow for skipped.
3. The score rolls in Unbounded 96: "183", "of 250", with the line "38 right, 7 wrong, 5 left" (sample).
4. Recap cards swipe up one at a time: "Where the marks went" (the grid grouped by chapter), "First thing to fix" ("Partnership: 4 wrong, the same trap each time"), "What's recorded" with "Fix it now, about 12 minutes".
- Lower or held result: no pop and no droplets; the grid fades in and the first card is "Here's the first thing to fix."
- Decay: from the fourth sheet, one tap opens it with a 160 ms fade. "Open results directly" in Appearance skips the seal entirely.

**Celebrations (three tiers, server-acknowledged only):**
- Tick: a bubble fills, `selectionClick`.
- Milestone (repair finished, weekly goal met): the bubble fills, Mobi's head fills, 16 bubble droplets burst once, `successNotification`, and a fact line: "Fixed in 4 min 12 s. Fresh check opens tomorrow."
- Big (first mock banked, fresh check passed): a full-screen foil bubble medallion (A-4) drops in, a fact line, and three controls (share circle, see-it circle, "Next" pill). Never after a poor result.

**Streaks:** a weekly bubble row with a chosen goal. Rest days are dotted bubbles, a missed day is just an open ring, and nothing earned is lost.

**Return:** after three or more days away, Today's hero reads "Welcome back. Pick the time you have." with 10, 20 and 30 bubbles, and Mobi waves once.

### A.8 Motion and haptic language

| Name | What | Curve and duration |
| --- | --- | --- |
| Fill | Liquid rising in a bubble with a sine-wave surface (two cycles) | `cubic-bezier(0.2, 0.9, 0.3, 1)`, 320 ms |
| Pop | Seal or bubble bursting into droplets | Scale 1.0 to 1.08 in 120 ms, then droplets on `Springs.bouncy`, 360 ms |
| Stretch | Dock lens and droplets travelling | `Springs.smooth` 380 ms, bounce 0.18, velocity-stretched |
| Squish | Press feedback | `Springs.snappy` 240 ms to 0.94, release with bounce 0.2 |
| Rise | Moment headlines, letter by letter | `cubic-bezier(0.3, 1.62, 0.46, 1)`, 620 ms, 26 ms stagger, capped at 20 characters |
| Roll | Digits | 40 ms stagger per digit, 500 ms |
| Drift | Idle prop float, 8 dp, plus or minus 1.2 degrees | 7.2 s loop, one per screen, paused off-screen |
| Exit | Anything leaving | `cubic-bezier(0.4, 0.3, 0.8, 0.6)`, 200 ms |

- **Never moves:** question text, options, the timer, explanation body, a number once landed, and lists while being read.
- **Reduced motion:** Fill becomes an instant colour change, Pop a 150 ms fade, Stretch a jump, Rise a block fade, Roll shows the final number, Drift stops. Every payoff keeps its text.
- **Haptics:** `selectionClick` (tab, chip, option), `lightImpact` (an onboarding bubble filling), `mediumImpact` (hold-to-lock complete), `successNotification` (server-acknowledged submission, repair or milestone), `warningNotification` (leaving a timed mock). None on wrong answers.

### A.9 Imagery plan

**Image bible for A:** glossy soft-vinyl and inflatable 3D objects; one large softbox key light from the top left plus a white rim from the right; saturated MockMob hues plus volt `#D2F000`; no text, letters, numbers or logos in any image; transparent background for objects; 2% grain on backdrops. Generate with gpt-image (`background: transparent`, PNG), then convert to WebP (`cwebp -q 80 -m 6 -alpha_q 90`).

| Id | Asset | Size and budget | gpt-image prompt |
| --- | --- | --- | --- |
| A-1 | Mobi, six poses (wave, think, cheer, point, hold pencil, asleep on a bubble) as separate layer sheets | 512 px, about 30 KB each | "A small friendly robot mascot designed as a premium soft-vinyl designer toy, three-quarter view. Its head is a perfect sphere in electric lime (#D2F000) with a satin glossy finish and a single soft specular highlight at the top left, crossed by a wide black glossy visor band with two white rounded-pill eyes. A short rounded charcoal (#1E1E1F) body, stubby arms, small rounded feet, a thin antenna ending in a tiny lime ball. Pose: [waving with the right arm raised]. Studio lighting: large softbox key from the top left, subtle white rim light from the right, soft contact shadow only. Clean toy-photography look, crisp edges, no text, no logo. Transparent background, centred, full body in frame with 8% padding." |
| A-2 | Subject inflatables (5) | 480 px, 30 to 50 KB | "A single glossy inflatable object, like a high-end inflatable pool toy with visible soft seams and a satin sheen: [Accountancy: a chunky calculator with rounded buttons] [Business Studies: a briefcase] [Economics: a coin with a rising arrow fused to it] [English: an open book with a ribbon bookmark] [General Test: a puzzle cube]. Colour: [tangerine #FF8A3D] with lighter highlights and deeper shadow tones of the same hue, small volt (#D2F000) accent detail. Three-quarter view, tilted 8 degrees, softbox key from the top left, white rim from the right, no ground shadow. No text, numbers or symbols on any surface. Transparent background." |
| A-3 | Welcome hero: answer-sheet cascade | 768 x 900, 120 KB max | "Art-directed 3D still life on a deep charcoal (#141414) background: a white exam answer sheet, its grid of circular answer bubbles visible but with no letters, numbers or printed text, tilted 20 degrees and floating, with a cascade of glossy spheres pouring off its lower edge and bouncing, in electric lime #D2F000, tangerine #FF8A3D, cobalt #3D6BFF, bubblegum #FF5FA2, lilac #A98BFF and aqua #22C7C7. Spheres have a satin vinyl finish and one soft highlight each. The top 40 percent of the frame is empty dark space for a headline. Soft studio light from the top left, gentle depth of field on the farthest spheres, 2 percent film grain. No text anywhere." |
| A-4 | Foil medallions (3: first mock banked, first fix, fresh check passed) | 512 px, 40 KB | "A round collectible medallion shaped like a filled exam answer bubble, made of holographic lime and silver foil with a fine embossed concentric ripple, a raised [tick / bandage cross / circular loop arrow] symbol in the centre, thick rounded rim, lying at a 15 degree angle, studio light producing an iridescent sheen across the foil, soft shadow. No text or numbers. Transparent background." |
| A-5 | Sticker sheet (12 die-cut stickers: volt bubble, pencil, eraser with crumbs, tick, calculator, cutting-chai glass, desk lamp, alarm clock, paper plane, highlighter, stack of books, a tiny Mobi head) | 256 px each, 12 to 25 KB | "A single die-cut sticker of [a cutting-chai glass of tea], glossy vinyl illustration style with soft 3D shading, colours from lime #D2F000, tangerine, cobalt and charcoal, a thick 6 px white border following the outline, a soft drop shadow, slightly rotated. No text. Transparent background." |
| A-6 | Empty states (4: nothing to fix, all caught up this week, offline, concept coming soon) | 480 px, 40 KB | "Mobi the lime soft-vinyl bubble-head robot [lying back on a pile of filled lime bubbles, relaxed, eyes as happy arcs], small scene, glossy toy photography, softbox from the top left, transparent background, no text." |

**Better as SVG or code:** every bubble, ring, dotted ring and bubble grid; the chapter-band gradients and their highlight; the dock, lens and icons; droplets and confetti (one CustomPainter); the wordmark animation; number rolls; the progress sheet; grain (a 256 px noise tile generated once).

### A.10 Concept render prompts (gpt-image, portrait 9:19.5)

Shared preamble for all four: "High-fidelity mobile app UI design, a single Android phone screen shown flat and front-on at 1080 x 2340 (9:19.5), no hand, a thin black device bezel with small rounded corners, Android status bar at the top showing 8:41 PM, signal and battery, a slim gesture handle at the bottom. The phone sits centred on a plain #0A0A0A canvas, and below the phone is a tiny grey caption: 'MockMob concept, sample data'. Typography: headlines in a wide, round, geometric display typeface similar to Unbounded, body text in a clean friendly sans similar to Figtree, sentence case throughout, no emoji, no exclamation marks. Crisp, legible text, premium Gen Z app quality, generous spacing, 16 dp side margins."

1. **Onboarding hero (Welcome).** "[Preamble]. Dark charcoal background #141414. The top 55 percent is a glossy 3D still life: a white exam answer sheet with a grid of empty circular answer bubbles, tilted 20 degrees, with satin spheres in lime #D2F000, tangerine, cobalt blue, bubblegum pink, lilac and aqua pouring off its lower edge. A small robot mascot with a lime spherical head, black glossy visor and white pill eyes sits on the highest sphere and waves. At the top left above the art, the wordmark 'mockmob' in lowercase wide rounded type where the last 'o' is a filled lime circle. Below the art, a two-line headline in large white wide rounded type: 'Fill the sheet. Chase the seat.' Under it, in light grey 16 sp text: 'MockMob finds where your CUET marks leak, helps you fix each leak, then checks the fix held.' At the bottom, a full-width lime #D2F000 pill button with near-black text 'Build my plan', and below it a white text button 'I already have an account'. Nothing else on screen, no footer text."
2. **Mid-onboarding personalisation (What it takes).** "[Preamble]. Dark background. At the top, a frosted glass card 'Your sheet' showing six small labelled circles in a row: Stage, Course, Colleges filled lime with small white text under them ('Class 12', 'B.Com (Hons)', 'SRCC +2'), and Subjects, Worry, Rhythm as empty rings. Below, a tangerine band (gradient #FFB070 to #E0661A) fills the middle of the screen with a glossy inflatable tangerine calculator floating at the right edge. On the band, white text 'This is the bar at SRCC.' and a huge number '924.3' in wide rounded bold type, with a small label under it 'B.Com (Hons), 2026 first list, UR'. Under the band, two plain rows on charcoal: 'Hindu College' with '919.9' right-aligned and 'Hansraj College' with '907.5' right-aligned. Then one line: 'English, Accountancy, Business Studies and Economics keeps all three open.' A full-width lime pill button at the bottom: 'Build my subjects'."
3. **Today with the navigation visible.** "[Preamble]. Dark background #141414. Top left small text 'Evening, Aanya.' and at the right a small frosted pill '30 weeks to the expected window'. A tangerine gradient band about 40 percent of the screen tall, a glossy inflatable tangerine calculator floating at its right. Overlapping the band's lower edge, a frosted glass card with white text 'Fix 6 Partnership questions' and grey 'About 12 minutes', and a large glossy lime circle button with a black play triangle on its right side. Below: a row titled 'This week' with seven circles, three filled lime, one dotted ring, three empty rings, and the text '3 of 4 sessions done'. Then 'Waiting to fix' with two rows: a small cobalt circle and 'Business Studies, Delegation' with a big outlined numeral '3'; a small pink circle and 'Economics, Elasticity' with an outlined '2'. At the bottom, floating 16 dp above the edge, a frosted dark glass pill navigation bar with four items, each with an icon and a label: 'Today' (active, sitting inside a glossy lime liquid bubble lens, black icon and label), 'Practice', 'Fixes' with a tiny lime badge '6', and 'You'. The list content is faintly visible blurred behind the glass bar."
4. **Result reveal moment.** "[Preamble]. Dark background. Mid-animation moment: a grid of 50 circles in 5 rows of 10 in the upper half, most filled lime, a few with coral #FF6B5B rings, a few hollow; small lime droplets are flying from the centre toward the last unfilled circles, with a faint motion trail. Below the grid, a huge number '183' in wide rounded extra-bold white type, with 'of 250' smaller beside it, and one line in grey: '38 right, 7 wrong, 5 left'. Under that, the top edge of a card peeking up from the bottom of the screen: 'First thing to fix' in white and 'Partnership: 4 wrong, the same trap each time' in grey, with a small handle bar. A soft lime light falls on the grid from the top. No navigation bar on this screen."

### A.11 Performance plan and biggest risk

- **Live blur:** the dock and at most one sheet, in one `BackdropGroup`. The lens shader is optional (B6). No blur inside scrolling content.
- **Pre-rendered:** props and Mobi layers (WebP, 2.0x, `cacheWidth` set), the welcome cascade, the medallions. Chapter bands are code gradients with a grain tile, which is cheap.
- **Animated budget:** one idle Drift per screen; droplets and confetti at most 16 particles in a single painter for under 1 s; Fill uses a clip path on one bubble at a time.
- **Frame budget:** 11.1 ms at 90 Hz; raster p90 at or under 8 ms on Today, at or under 6 ms on the runner (no glass there).
- **Biggest risk: the "toy" read.** Candy hues and vinyl props could feel younger than a 17-year-old aiming at SRCC wants, and less premium than Revolut. Mitigation: dark-first, one hue per screen, props at small counts, adult copy. Technical risk: Unbounded's width makes long headlines wrap badly on 384 dp, so moment lines must stay under about 28 characters.

---
## Direction B: "Afterhours"

### B.1 The idea

**Core idea:** CUET prep happens at night, so MockMob is the premium after-hours room for it: dark, cinematic and quiet, where the only light in each scene comes from the thing that matters (your next move, your result) and the folded answer sheet is the object everything is built around.

**Mood:** cinematic, nocturnal, calm-intense, expensive, editorial.

**What it looks like in one screenshot:** a near-black room with one smoked-glass slab catching a thin volt edge of light, a monumental condensed number, frosted controls floating over a softly lit render, and a small glass dock.

**References and how it stays original:**
- From Revolut: the home formula (art-backed hero, one big number with small units, a frosted pill, four frosted circular actions, a dark glass list card), the subject pager with peeking neighbours, the morph grammar ("first the card, then the details"), a calm lowercase brand.
- From HIGH: the dark tool layer for data, monumental type only at moments, the foil milestone, a floating dock.
- From Fampay: the environment-lit near-black ground that changes per section, one rendered 3D object per subject, speed as proof (the real measured time on a success).
- Original because: the light model ("one light per screen, and it comes from the focal element") and the folded answer sheet belong to MockMob (Mobi is already drawn as a folded volt sheet, spec A1). There are no stickers, no candy chapters and no compressed caps, so it is not HIGH. There are no lifestyle photos and no violet, so it is not Revolut. There is no amber and no paper tag, so it is not Fam. It also extends the website's Night Arena, so the app and mockmob.in become one brand.

### B.2 Brand

- **Wordmark:** `mockmob`, lowercase, Bricolage Grotesque at width 87, weight 700, tracking -3%. A single volt hairline (1.5 dp at app size) runs through the x-height from the second m to the end, like light escaping through a fold. In motion the hairline draws left to right (500 ms) and the letters brighten as it passes.
- **Mark:** "the fold". A rounded square of smoked glass with its top-right corner folded down; the folded triangle is volt, and a 1 dp edge light runs along the crease. It echoes Mobi's folded-sheet body. App icon: the mark on `#101210`. Monochrome themed icon: an outline square with a filled corner.
- **Palette.** Dark ("Night") is the default identity. Light ("Daylight") is a composed option for daytime and accessibility.

| Role | Night (default) | Daylight | Notes |
| --- | --- | --- | --- |
| Ground | `#101210` | `#EEF0E8` | Neutral charcoal with the faintest green, matching the web's `#0b100e` family |
| Raised | `#181B18` | `#FFFFFF` | |
| Raised 2 | `#222622` | `#E3E6DC` | |
| Hairline | `#2B302B` | `#D3D7CA` | |
| Ink | `#F2F4EC` | `#111410` | |
| Ink 2 | `#B4BBAE` | `#3E453B` | |
| Ink 3 | `#848C7F` | `#5C6357` | 4.5:1 checked on each ground |
| Volt (action, the light) | `#D2F000`, text on it `#0B1000`; edge light `#D2F000` at 85% | Fill `#D2F000`; volt text `#526700` | Volt is used as light: edges, the active state, the primary button |
| Volt glow | `#D2F000` at 14 to 18% | `#D2F000` at 22% | Only behind the focal element, never behind text |
| Wrong | `#2A1614` surface, `#7D3128` border, `#FFC9C2` text (the web's own trio) | `#FBE9E7` surface, `#B93225` text | |
| Accountancy light field | `#3B2A10` fading to `#101210` (warm amber) | `#F6E8CF` | Fields are low-saturation and radial, behind art only |
| Business Studies field | `#14213F` (indigo) | `#DCE3F7` | |
| Economics field | `#0F3330` (deep teal) | `#D3EEEA` | |
| English field | `#3A1626` (rose) | `#F4DDE6` | |
| General Test field | `#22300F` (moss) | `#E2EDCF` | |

- **Typography** (OFL, bundled variable files):

| Role | Family and axes | Size / line / weight | Notes |
| --- | --- | --- | --- |
| Hero number | Bricolage Grotesque, wdth 75, opsz 96 | 88 to 112 sp / 0.9, 700 | Condensed by the width axis, not a commercial compressed face. `tnum` to verify; fallback numerals Gabarito ExtraBold |
| Moment headline | Bricolage Grotesque, wdth 87, opsz 72 | 36/38 sp, 650, -2.5% | Two lines maximum |
| Screen title | Bricolage Grotesque, wdth 100 | 26/30 sp, 600, -1.5% | |
| Card title | Hanken Grotesk | 17/22 sp, 700 | |
| Body | Hanken Grotesk | 16/24 sp, 400 | Questions 17/26 |
| Label, button | Hanken Grotesk | 15/20 sp, 600 | |
| Caption | Hanken Grotesk | 13/18 sp, 500 | |
| Units beside big numbers | Bricolage Grotesque | 55% of the number, top-aligned | Revolut's "pence set small" move, for "of 250" and decimals |

- **Mobi: restyle, used less.** Mobi becomes a small robot of frosted glass and brushed graphite whose visor is a volt light: the visor is literally a light source in the scene. Its body keeps the folded-sheet silhouette. It appears at onboarding as a small guide, on return after a gap, at celebrations and in empty states, and never during a mock or on a sealed sheet. In the app it is a code rig (layers plus springs); on the welcome and milestone screens it appears as a 3D render. Why: the audience wants to be taken seriously, and Revolut's lesson (toy to photoreal as the audience matures) applies without losing the character.

### B.3 Material system

| Material | Where | Recipe |
| --- | --- | --- |
| Frosted glass (live blur) | Dock, the Start button, sheets, one collapsing header (only if B3 passes) | `BackdropFilter.grouped`, sigma 22 (dock) and 28 (sheets); tint `#181B18` at 0.64 Night, `#FFFFFF` at 0.74 Daylight; 1 dp edge light (white 14% at the top to 3%); shadow `0 20 40 -22` black at 50% |
| Liquid lens | The dock's active tile | 64 x 44 dp refraction shader (B6) with a volt hairline on its top edge; fallback tint plus edge light |
| Smoked fake glass | Hero cards, the circular actions, recap cards, the onboarding pass | Pre-blurred slice of the scene art, tint white 8% plus black 20%; a 1.5 dp volt top edge only on the one focal card per screen |
| Solid | Runner, options, explanations, result detail, lists, settings | Raised tokens; no art behind, no light |
| Full-bleed imagery | Today hero (top 52%), onboarding backgrounds, the result room, milestone screens | Subject light field plus a rendered object, faded into the ground by a baked scrim and a baked progressive blur in the lower third |
| Light | Exactly one light per screen | A soft volt glow (14 to 18%) behind the focal element and a thin volt edge on it; nothing else glows |
| Grain | All art | 2.5% film grain baked in, plus a static 3% noise tile on the ground |

Depth comes from three planes: the room (art, parallax at 0.2x the scroll), glass (cards) and chrome (dock and sheets). **The room responds to the week:** the light field's opacity rises from 0.35 to 0.6 as the student's real sessions this week approach their goal, so the room is brighter in a good week. It never dims below the starting level, and a rest day does not dim it.

### B.4 Signature motif

**The lit edge.** Every focal object (the hero slab, the sealed sheet, the active dock tile, the onboarding pass) has one thin volt edge of light along its top, and nothing else on the screen has it. With the monumental condensed number beside it, any screenshot is recognisable at thumbnail size. Secondary motif: the fold. Corners fold, sheets unfold, the logo is a fold.

### B.5 Navigation: split glass dock

- **Destinations:** three tabs in the dock (Today, Practice, Review), one floating **Start** button beside it, and You behind the avatar at the top left of Today (Revolut's pattern). Learn folds into Practice as a "Concepts" shelf and opens from any mistake in Review. The research asked for a three-destination test (PB L234); this is it, with labelled tabs.
- **Shape:** the dock is a pill 60 dp tall and about 288 dp wide (three 88 dp slots plus padding), anchored 16 dp from the left and 10 dp above the gesture inset. The Start button is a 60 dp glass circle 12 dp to its right. Outer sizes never change.
- **Indicator:** a "lit tile", white 12% fill with a 1.5 dp volt top edge, slides on `Springs.smooth` (360 ms, bounce 0.12) and stretches up to 1.15x with velocity. If B6 passes, it is a liquid lens that refracts the icon under it.
- **Icons:** 24 dp, 1.75 dp outline in Ink 3 when inactive; the active tab swaps to its filled variant in Ink with a 200 ms cross-fade and a 0.92 to 1.0 spring scale. Labels always visible, 12 sp Hanken 600.
- **Start:** a volt ring with a play glyph. A press morphs the circle into a sheet (container transform, 420 ms, Emphasized) with the tiles "Resume Accountancy mock, 23 of 50" (when one exists), "Quick 10", "Full mock" and "Fix the next mistake". It is the one-tap way into the core loop from anywhere.
- **Press:** 0.95 scale on `Springs.snappy`; the edge light brightens.
- **Haptics:** `selectionClick` on a tab change and each drag crossing, `lightImpact` on Start, nothing on a re-tap.
- **Scroll:** on scroll down both pieces drift down 8 dp and scale to 0.94, returning on scroll up or idle. Never hidden on tab roots; hidden on the runner, repair and result.
- **TalkBack:** "Review, tab 3 of 3, 6 mistakes waiting"; "Start, opens quick start".

### B.6 Onboarding: "Your pass" (14 screens)

The identity object is a **pass**: a smoked-glass card with a lit edge that gathers the student's answers line by line, each with a light sweep, like an engraving. Stage, course, dream list, subjects and rhythm are engraved on it as they are chosen. At the climax it flips to show the plan on its back and is sealed by holding. At the end it flies into Today, and it lives in You afterwards. A four-segment hairline at the top (Aim, Subjects, Rhythm, Save) shows real progress.

**1. Cold open.** A black room. A volt hairline draws across the middle (500 ms), light spills down from it and reveals the fold mark, and the wordmark fades up beneath. 1.4 s, tap to skip; precaches art and shaders. Haptic: one `lightImpact` as the line completes. Reduced motion: a 200 ms fade to the wordmark.

**2. Welcome.**
- Layout: full-bleed render (B-1): a smoked-glass answer-sheet slab floating in a dark room, a volt light along its top edge, a soft reflection below, the small glass Mobi sitting on its corner. The camera dollies in 4% over 6 s, then rests.
- Headline: "Your lost marks leave a trail."
- Support: "MockMob follows it, helps you fix what's behind it, and checks that the fix held."
- Inputs: "Start my plan" (volt), "I already have an account".

**3. Stage.**
- Layout: the room dims; the empty pass slides up and rests in the top third.
- Headline: "Where are you on the road to CUET 2027?"
- Inputs: four glass rows: "Class 12, writing in 2027", "Passed Class 12, writing in 2027", "In Class 11", "Not sure yet".
- Payoff: "30" rolls onto the pass in condensed type with "weeks to the expected May window" beside it.

**4. Course.**
- Headline: "Which seat are you after?"
- Support: "Counts are DU's, from 2026 admissions."
- Inputs: a two-column grid of fake-glass tiles, each with a big condensed count over a small label: "55" over "B.Com (Hons)", "44" over "B.Com", "40" over "B.A. (Hons) Economics", "10" over "B.A. (Hons) Business Economics", "9" over "BMS", "2" over "BBA (FIA)", plus "Another course" and "Not sure yet". Up to three.
- Payoff: the chosen course engraves onto the pass with a light sweep.

**5. Dream colleges.**
- Headline: "Pick your dream list."
- Support: "Up to three. Change it whenever you like."
- Inputs: search plus a list; "Open to any college".
- Payoff: the names engrave onto the pass, and the room's light field warms slightly.

**6. The bar (first reveal).**
- Layout: a full-screen moment. The pass recedes, the room goes dark, and one number rises from below in condensed Bricolage at 104 sp.
- Number: "924.3"; label: "SRCC, B.Com (Hons), 2026 first list, UR".
- Then two rows slide in: "Hindu College 919.9", "Hansraj College 907.5".
- Rule: "B.Com (Hons) takes one language, Mathematics or Accountancy, and any two more."
- Fit: "English, Accountancy, Business Studies and Economics keeps all three open."
- Input: "Set my subjects".

**7. Subjects and how solid each feels.**
- Headline: "How solid is each one, honestly?"
- Support: "Your first check will show whether your gut was right."
- Inputs: each subject is a slab row with a small swatch of its light field, its name, "Practice ready" where true, and a segmented Shaky, Okay, Strong. General Test: "Opening soon. We'll tell you."
- Payoff: rows reorder live, weakest first, and "Starting with Accountancy" engraves onto the pass.

**8. Biggest worry.**
- Headline: "What costs you the most marks?"
- Inputs: six glass rows (the same six worries as Direction A, in the student's words).
- Payoff: Mobi, small at the edge, says one line in a glass bubble, for example "Easy-question leaks. That's where we start." The first move on the pass updates.

**9. One real question.**
- Layout: solid raised surface, no art behind it, Hanken 17 sp.
- Correct: a volt edge runs once around the chosen option (400 ms), with "Right, in 14 seconds." (measured).
- Wrong: the chosen option takes the wrong trio, the right one gets the lit edge, and "That's a trap. Here's the ten-second fix:" with the explanation.
- Inputs: "Next", "Skip this one".

**10. Rhythm.**
- Headline: "When do you study best?"
- Inputs: minutes (10, 20, 30) as a segmented control; days per week as seven glass dots, four pre-lit; a time window (6:00 AM, 5:00 PM, 8:00 PM, 10:00 PM, or custom).
- Payoff, live: "Keep this and that's about 120 sessions before the expected window." Rest days are unlit dots: "Rest days are part of the plan."

**11. The plan (the climax).**
- Layout: the pass moves to the centre, scales up and flips on its Y axis (600 ms, `lightImpact` at 90 degrees). The back is the plan, revealed line by line with the sweep.
- Headline above it: "Your plan, built from your answers."
- On the back: "Week one." Then "First move: starting-point check, 10 questions, Accountancy, about 10 minutes." "Four evenings a week, 20 minutes, 8:00 PM." "Dream list: SRCC, Hindu, Hansraj."
- Line: "It sharpens after your first check."
- Input: "Hold to seal it": a volt edge runs around the whole pass over 1.2 s, `mediumImpact` on completion, and Mobi's visor brightens. A plain "Seal it" target serves TalkBack and reduced motion. Secondary: "Change something".

**12. Save (age first, then the account).**
- Headline: "Keep your pass."
- Support: "Sign in and your plan follows you to mockmob.in and any phone."
- Age row: "Quick one: are you 18 yet?" with "Yes", "Not yet", "Rather not say", and "Under 18, usage tracking stays off."
- Inputs: "Continue with Google" (volt, Credential Manager), "Use an email code", "Not now".
- States: "Saving your pass" while pending; "Saved to your account." after acknowledgment; on failure "Couldn't save. Your pass is still on this phone." with "Try again".

**13. Reminders.**
- Headline: "One nudge, at your time."
- Layout: a glass notification preview floating in the room: "Tonight, 8:00 PM" over "Ten minutes of Accountancy is ready."
- Support: "Only on your days. Never after 11:00 PM."
- Inputs: "Remind me", "Not now", equal weight.

**14. First move (the personalised reveal).**
- Layout: the pass shrinks and flies into Today's hero slab while the camera dollies into the room; Today assembles around it with the student's subject light field, countdown, dream list and week.
- Hero: "10" in condensed type, "questions to your starting point", and a frosted pill "Start now, about 10 minutes".
- Secondary: "Tonight at 8:00 PM".

### B.7 Today, result reveal, celebrations, streaks, return

**Today (the Revolut formula, made for an exam):**
- Top bar over the art: avatar (opens You), a search pill "Find a chapter", and a 36 dp circle holding this week's ring (opens rhythm).
- Hero (top 52%): the next move's subject light field and its rendered object. Label "Accountancy". Monumental "6" with "mistakes ready to fix" small beside it. Frosted pill: "Fix them, about 12 min". The hero is a pager: swipe to the next subject; neighbours peek 20 dp at 85% scale and 60% opacity; only the centre one has the lit edge.
- Four frosted circular actions (52 dp, labels under): "Full mock", "Quick 10", "Fix", "Concepts".
- A dark glass list card, "Recent": "Fixed: Partnership, 3 of 4 right on the fresh check" (sample), "Mock 7, Accountancy, 183 of 250" (sample), "See all".
- A two-tile bento: "Dream list" (SRCC 924.3, Hindu 919.9, Hansraj 907.5, labelled "2026 first list") and "This week" (a ring with "3 of 4 sessions").
- An unopened result takes over the hero with its sealed sheet (spec 5.3).

**Result reveal: "The fold".** The scored attempt arrives with the submit response, so the sheet is ready at once.
1. A dark room. A matte-black answer sheet folded in thirds rests in the centre, sealed with a volt foil seal (B-5). On the visible panel: "Mock 7, Accountancy" and "Received at 10:42 PM". "Swipe up to open", or tap "Open".
2. The drag follows the finger 1:1; the panels unfold in perspective (`rotateX`, one transform per panel, 120 ms stagger), with `selectionClick` at 25, 50 and 75%. A light sweep crosses the sheet as it flattens.
3. The number lands: "183" at 112 sp, "of 250" small and top-aligned, then "38 right, 7 wrong, 5 left". The 50-cell grid under it colours in by section.
4. Recap story cards with a segmented progress bar at the top (tap to advance): "Where the marks went" (a segmented ring by chapter with real counts), "First thing to fix" (the chapter, the count and the repeated trap), "What's recorded" with "Fix it now, about 12 minutes".
- Lower or held: no sweep, no glow; the sheet opens with a calm fade, and the first card is "Here's the first thing to fix."
- Decay and skip as in spec 5.6: from the fourth sheet a single tap and a 160 ms unfold; "Open results directly" in Appearance; the TalkBack action "Open without the reveal".

**Celebrations (server-acknowledged only):**
- Small: the lit edge runs once around the item, `selectionClick`.
- Milestone: a brushed-chrome token (B-6) rises into the light, 12 thin volt light shards streak outward once (700 ms, one painter), `successNotification`, and a fact line with the measured time: "Fixed in 4 min 12 s. Fresh check opens tomorrow."
- Big (first mock banked, fresh check passed): a full-screen dark room with the token, a monumental line ("First mock, banked."), one fact sentence, and three controls (share circle, see-it circle, "Next" pill). Never after a poor result.

**Streaks:** the week ring and the room's light. The goal is weekly and chosen; rest days keep the light; a missed day takes nothing that was earned.

**Return:** after three or more days away, the glass Mobi sits at the hero's edge and the hero reads "Welcome back, Aanya. How long have you got tonight?" with 10, 20 and 30 minute pills.

### B.8 Motion and haptic language

| Name | What | Curve and duration |
| --- | --- | --- |
| Glide | Default enter | `cubic-bezier(0.15, 0.5, 0.5, 1)`, 300 ms (Revolut-measured) |
| Exit | Default exit | `cubic-bezier(0.4, 0.3, 0.8, 0.6)`, 200 ms |
| Emphasized | Container transforms (Start to sheet, pass to Today, card to detail) | `cubic-bezier(0.16, 1, 0.3, 1)`, 420 to 450 ms |
| Smooth spring | Dock tile, cards, sheets with velocity | 360 ms, bounce 0.12 |
| Dolly | Camera push into a scene (art scale 1.0 to 1.04 plus 12 dp parallax) | Emphasized, 900 ms, once |
| Sweep | A soft light band crossing a surface | `cubic-bezier(0.45, 0, 0.55, 1)`, 700 ms, once |
| Engrave | Text revealed left to right by a mask | 280 ms, Glide |
| Unfold | Sheet panels | Follows the finger; release on a 420 ms spring, bounce 0 |
| Roll | Digits | 40 ms per digit, 500 ms |

- **Weight:** springs are nearly critically damped (bounce at most 0.12). Things glide and land; they do not bounce. This is the owner's "Everything glides. Every interaction has weight."
- **Never moves:** question text, options, the timer, explanation body, numbers after landing, list rows while being read. The dock is absent during a mock.
- **Reduced motion:** Dolly and Sweep off; Unfold becomes a 200 ms cross-fade; Engrave shows text at once; Roll shows the final value; the lit edge stays as a static line.
- **Haptics:** `selectionClick` (tab, option, unfold thresholds), `lightImpact` (Start, the pass flip at 90 degrees, the cold open), `mediumImpact` (seal complete), `successNotification` (acknowledged submission, repair, milestone), `warningNotification` (leaving a timed mock). None on wrong answers.

### B.9 Imagery plan

**Image bible for B:** photoreal product renders in a dark studio "room" with a charcoal floor fading to black; materials are smoked glass, frosted glass, brushed graphite, brushed chrome and matte black paper; a neutral soft key light from the top left and one thin lime (`#D2F000`) rim or edge light per image, never more; 2.5% film grain; no text, numerals, logos or crests anywhere; objects on transparent backgrounds, scenes full-bleed. Generate with gpt-image (`background: transparent` for objects), convert to WebP.

| Id | Asset | Size and budget | gpt-image prompt |
| --- | --- | --- | --- |
| B-1 | Welcome hero: the answer-sheet slab in the room | 768 x 1706, 140 KB max | "Cinematic photoreal 3D render, portrait 9:19.5. A single thin slab of smoked glass shaped like an exam answer sheet, with a faint etched grid of small circles and no text, floating at a 12 degree tilt in the lower middle of a dark studio room. A thin electric lime (#D2F000) light glows along its top edge only, as if light escapes from inside the glass, and casts a faint lime reflection on a glossy charcoal floor below. A soft neutral key light from the top left; the rest of the room falls off to near-black (#101210). The top 45 percent of the frame is empty dark space for a headline. Shallow depth of field, 2.5 percent film grain, premium product-launch mood, no text, no logos." |
| B-2 | Subject objects (5) | 520 px, 40 to 60 KB | "Photoreal 3D product render of a single object: [Accountancy: a closed ledger book of frosted glass with brushed graphite corners and a graphite ribbon] [Business Studies: a slim smoked-glass briefcase with a brushed chrome handle] [Economics: a short stack of brushed-chrome coins beside three frosted-glass bars of rising height] [English: a brushed graphite fountain-pen nib resting on a single frosted glass page] [General Test: a frosted glass prism inside a graphite compass ring]. Dark studio, neutral soft key light from the top left, one thin lime (#D2F000) rim light along the top edge, subtle reflections. Three-quarter view, centred, 10 percent padding. No text, numbers or symbols on any surface. Transparent background." |
| B-3 | Subject light fields (5) plus a neutral one | Rendered at 768 x 1706, decoded at 180 px wide, 20 to 40 KB | "Abstract low-frequency light field for a phone background, portrait 9:19.5: a soft out-of-focus glow of [warm amber] light pooling in the upper-right third and fading smoothly into near-black charcoal (#101210) across the rest of the frame, like light from an unseen lamp on a dark wall. Extremely soft, no shapes, no bokeh circles, no objects, 2.5 percent fine film grain to prevent banding. No text." (Swap the colour: deep indigo, deep teal, muted rose, moss green, neutral warm grey.) |
| B-4 | Glass Mobi, five poses (greet, point, think, nod, rest) | 512 px, 40 KB | "Photoreal 3D render of a small friendly robot mascot about the size of a coffee mug. Its body is a folded-sheet shape, like a square of paper folded diagonally, made of frosted glass with brushed graphite joints; short graphite arms and feet; its head carries a horizontal visor glowing soft electric lime (#D2F000) from within, with two rounded white eye shapes in it. Pose: [raising one hand in greeting]. Dark studio, neutral key from the top left, the lime visor casting a faint glow on its own body, gentle reflections. No text. Transparent background, full body, centred." |
| B-5 | Sealed-sheet layers: a matte black paper panel with an embossed bubble grid (tileable), and the volt foil seal | Panel tile 512 px, 30 KB; seal 256 px, 20 KB | Panel: "Top-down macro texture of matte black heavyweight paper with a subtle blind-embossed grid of small circles, even soft lighting, seamless and tileable, no text." Seal: "A round foil seal sticker in iridescent electric lime and silver foil with a fine radial brushed texture and a crisp folded-corner symbol embossed in the centre, slight curl at one edge, soft studio light, top-down, transparent background, no text." |
| B-6 | Milestone tokens (3: first mock banked, first fix, fresh check passed) | 512 px, 45 KB | "Photoreal 3D render of a thick round token of brushed chrome with a frosted glass inlay in its centre; the inlay holds a raised [folded-corner sheet / check mark / looped arrow] shape that glows faint lime (#D2F000) from within. The token floats tilted 20 degrees in darkness with one thin lime rim light along its top edge and soft reflections. No text or numbers. Transparent background." |
| B-7 | Empty-state scenes (3: nothing to fix, offline, concepts coming) | 600 x 400, 40 KB | "Photoreal 3D vignette in a dark studio room: [the small frosted-glass robot with a lime visor sitting on a closed frosted-glass ledger, legs dangling, relaxed]. One soft key light, a faint lime rim on the robot, the floor fading to near-black, wide crop with empty space at the left for a line of text. No text." |

**Better as SVG or code:** the fold mark and wordmark, lit edges and light sweeps (gradients on small rects), rings and segmented rings, the dock and icons, light shards (one painter), scrims and the noise tile, the pass card (live text on fake glass), number rolls, and the unfold geometry (transforms on three panel images).

### B.10 Concept render prompts (gpt-image, portrait 9:19.5)

Shared preamble: "High-fidelity mobile app UI design, a single Android phone screen shown flat and front-on at 1080 x 2340 (9:19.5), no hand, a thin black bezel with small rounded corners, Android status bar showing 8:41 PM, signal and battery, a slim gesture handle at the bottom. The phone is centred on a plain #050505 canvas, with a tiny grey caption under the phone: 'MockMob concept, sample data'. Typography: big numbers and headlines in a modern grotesque with a condensed width, like Bricolage Grotesque condensed; body in a clean neutral grotesque like Hanken Grotesk; sentence case, no emoji, no exclamation marks. Cinematic dark UI on a near-black neutral charcoal ground #101210, one electric lime #D2F000 accent used as light. Crisp legible text, premium fintech-grade polish, 16 dp margins."

1. **Onboarding hero (Welcome).** "[Preamble]. Full-bleed photoreal scene: a thin smoked-glass slab shaped like an exam answer sheet, with a faint etched grid of circles, floats tilted in a dark studio room; a thin lime light glows along its top edge and reflects on a glossy charcoal floor. A tiny frosted-glass robot with a glowing lime visor sits on the slab's corner. At the top left, the lowercase wordmark 'mockmob' in off-white with a thin lime line running through the letters. In the lower third over a dark fade: a two-line headline in large off-white condensed grotesque, 'Your lost marks leave a trail.' Under it in grey 16 sp: 'MockMob follows it, helps you fix what's behind it, and checks that the fix held.' A full-width lime pill button with near-black text 'Start my plan', and an off-white text button 'I already have an account' below it. No footer."
2. **Mid-onboarding personalisation (course pick with the pass).** "[Preamble]. Dark room background with a faint warm amber glow at the upper right. At the top, a thin four-segment progress line with the first segment lime. Below it, a smoked-glass card with a thin lime light along its top edge, labelled 'Your pass', showing engraved off-white lines: '30 weeks to the expected May window' with the 30 large and condensed, and 'Class 12, writing in 2027'. Under the card, the headline 'Which seat are you after?' and grey text 'Counts are DU's, from 2026 admissions.' Then a two-column grid of six dark frosted tiles, each with a large condensed number over a small label: '55' 'B.Com (Hons)' (selected, with a lime edge and a small lime check), '44' 'B.Com', '40' 'B.A. (Hons) Economics', '10' 'B.A. (Hons) Business Economics', '9' 'BMS', '2' 'BBA (FIA)'. A lime pill button 'Continue' at the bottom."
3. **Today with the navigation visible.** "[Preamble]. The top half is a dark scene with a soft warm amber glow and a photoreal frosted-glass ledger book with graphite corners floating at the right, lit by a thin lime rim. Over it: a small round avatar at the top left, a frosted search pill 'Find a chapter', and a small circle with a partial lime ring at the top right. Left-aligned on the scene: the small label 'Accountancy', a huge condensed number '6' with 'mistakes ready to fix' small beside it, and a frosted pill 'Fix them, about 12 min'. The edge of the next subject card peeks in, dimmer, at the right edge. Below: four frosted circular buttons with icons and labels 'Full mock', 'Quick 10', 'Fix', 'Concepts'. Then a dark glass card 'Recent' with two rows, 'Fixed: Partnership, 3 of 4 right on the fresh check' and 'Mock 7, Accountancy, 183 of 250', and 'See all'. At the bottom, floating: a frosted dark glass pill with three labelled tabs, 'Today' (active, on a lighter frosted tile with a thin lime top edge), 'Practice', and 'Review' with a small count '6', and to its right a separate frosted glass circle with a lime play icon. The list is softly blurred behind the glass."
4. **Result reveal moment.** "[Preamble]. A dark room. Mid-reveal: a matte black answer sheet folded in thirds is three-quarters unfolded in the centre, its panels in perspective, a soft band of light sweeping across it, a lime foil seal peeled back at the top edge. On the flattened panel, a grid of 50 small cells in 5 rows of 10, mostly lime, a few muted red, a few empty. Above the sheet, a huge condensed off-white number '183' with 'of 250' small and top-aligned beside it, and below it in grey '38 right, 7 wrong, 5 left'. At the very top, small text 'Mock 7, Accountancy, received at 10:42 PM'. At the bottom, the edge of a dark glass card 'First thing to fix' rising into view. No navigation bar."

### B.11 Performance plan and biggest risk

- **Live blur:** the dock and the Start circle (two small clipped shapes in one group, under 8% of the screen), plus one sheet when open. A blurred collapsing header only if B3 passes; otherwise an opaque header that fades in.
- **Pre-rendered:** the hero scene is two layers: the light field decoded at quarter resolution (`cacheWidth: 180`, 288 KB in memory) and the object at 2.0x. Fake glass draws from the pre-blurred field. The progressive blur at the foot of the hero is baked into the art.
- **Animated budget:** at most one full-screen animated layer (the Dolly) per screen, and it runs once. Parallax is paint-only (`Flow` repainting on the scroll position). The unfold is three transformed images with no `saveLayer`.
- **Frame budget:** 11.1 ms at 90 Hz; raster p90 at or under 8 ms on Today while scrolling under the dock; the runner at or under 6 ms.
- **Biggest risk: over-lighting and generic dark fintech.** The owner has already said "Maybe you have overdone the lighting", and a dark room with lime light can drift toward every other dark app. Mitigation: the one-light rule enforced as a review check (one focal edge per screen), the room-brightness range capped at 0.6, and real exam-world objects in every hero. Technical risk: full-bleed art under a live dock while scrolling is the heaviest case on the Mali-G57, which is exactly benchmark B2.

---

## Direction C: "Margin Notes"

### C.1 The idea

**Core idea:** MockMob is the senior's notebook every aspirant wishes they had: every trap circled, every fix taped in, and notes in the margin written just for you. Finding and fixing mistakes is literally what a marker does, so the marker becomes the interface.

**Mood:** handmade, witty, warm, collectible, loud in places, honest.

**What it looks like in one screenshot:** warm ruled paper, one volt marker circle drawn around the thing that matters, a taped card, a die-cut Mobi sticker holding a red pen, a short handwritten margin note, and paper index tabs standing up from a tinted acetate tray.

**References and how it stays original:**
- From Fampay: die-cut stickers, a caption layer instead of footers, identity built through playful choices, the friend voice.
- From HIGH: a baked sticker kit, grainy gouache and riso story illustration, a voice with attitude, the foil moment (here a rubber stamp).
- From Revolut: the theme sheet becomes "notebook covers" in You, and the morph grammar becomes page turns.
- Seekho: concepts as posters.
- Original because: red-pen correction is the core act of MockMob (find the mistake, fix it, check it), so annotation as UI is the product's own metaphor, not a borrowed style. The material is ruled paper, graph paper, acetate film and washi tape, not Fam's crumpled amber tag or HIGH's candy chapters; there is no amber, no condensed caps and no meme imagery.

### C.2 Brand

- **Wordmark:** `MockMob` in Gabarito ExtraBold (the face the app already ships), tracking -2%, with a hand-drawn volt marker underline under the whole word that ends in a tick. The underline draws once, stop-motion style (400 ms), on the cold open.
- **Mark:** "the circled tick". A hand-drawn marker circle, open at the top right where the pen lifted, with a tick inside, cut out as a sticker with a 3 dp white border and a soft shadow. App icon: the volt sticker on warm paper `#F3EFE6`; in Night, on `#161512`. Monochrome: the circle and tick as strokes.
- **Palette.** Light ("Notebook") is the default; dark ("Night notebook") is a full theme.

| Role | Notebook (default) | Night notebook | Notes |
| --- | --- | --- | --- |
| Ground (paper) | `#F3EFE6` | `#161512` | Warm paper; rule lines drawn in code at 3% |
| Raised (card paper) | `#FFFDF8` | `#201E1A` | |
| Raised 2 | `#E9E3D6` | `#2A2823` | |
| Rule line, hairline | `#D8D0BF` | `#33302A` | |
| Ink | `#17150F` | `#F4F0E6` | |
| Ink 2 | `#4A453A` | `#C2BBAA` | |
| Ink 3 | `#6B6558` | `#918A7A` | 4.5:1 checked |
| Volt (highlighter, primary action) | `#D2F000` fill with Ink text; as text `#526700` | `#D2F000` | The circle around the focal thing and the primary button |
| Correction red (wrong, what to fix) | `#D93A2B` | `#FF7A68` | Always with a word |
| Your-pen blue (the student's own answers) | `#2F55D4` | `#8FA8FF` | Echoes of what the student told us |
| Tape colours | `#F5C6D6`, `#BFE3D0`, `#C9D3F7`, `#F7E0A3` | Same at 80% | Decoration only, one strip per hero card |
| Subject covers | Accountancy `#2F6B4F`, Business Studies `#2B3F8C`, Economics `#B5462E`, English `#6B3E8E`, General Test `#1E7A86` | Same, lifted 12% | Tabs and covers only, white text on them |

- **Typography** (OFL, bundled):

| Role | Family | Size / line / weight | Notes |
| --- | --- | --- | --- |
| Moment headline | Instrument Serif | 40/42 sp, regular; italic for one-line moments | Editorial, unlike any test-prep app |
| Screen title | Instrument Serif | 30/34 sp | |
| Big numbers, buttons, chips | Gabarito | Numbers 72 to 96 sp ExtraBold with `tnum`; buttons 16 sp 700 | Already in the app |
| Body | Hanken Grotesk | 16/24 sp, 400; questions 17/26 | |
| Label | Hanken Grotesk | 14/20 sp, 600 | |
| Caption | Hanken Grotesk | 13/18 sp, 500 | |
| Margin note | Caveat | 20/24 sp, 600 | At most one per screen; never instructions, numbers you must read, or anything needed to act |

- **Mobi: keep and amplify.** Mobi stays the lime folded-sheet robot the app already has, redrawn as a flat sticker character with a confident marker outline and a die-cut white border, in twelve poses (holding a red pen, taping a note, stamping, asleep on books, pointing, peeking over a page edge). Why: it is the cheapest, most consistent character to scale across a sticker world, and it is already the brand's most liked asset.

### C.3 Material system

| Material | Where | Recipe |
| --- | --- | --- |
| Acetate glass (live blur) | The tab tray and sheets | `BackdropFilter.grouped`, sigma 18; tint white 40% plus the active tab's colour at 35% (Notebook), `#201E1A` at 0.6 plus colour at 25% (Night); a printed halftone dot pattern at 6%; a bright 1 dp cut edge. Labels sit on paper tabs, never directly on acetate |
| Highlighter (fake acetate) | Behind the one key line of a card, the selected chip | Volt at 55% multiplied over paper, slightly ragged ends (a 9-slice image) |
| Paper (solid) | Grounds and cards | Ruled lines on Today and onboarding, graph grid on Practice, both in code; a 256 px paper-fibre tile at 2% |
| Clean paper | Question runner, options, explanations | Plain raised paper; rules and fibre switch off under text you read |
| Stickers | Mobi, earned collectibles, empty states | Die-cut WebP with alpha, at most two per screen |
| Tape | Holding the hero card | One washi strip, rotated 4 to 8 degrees |
| Full-bleed illustration | Welcome, milestone pages, concept posters | Riso and gouache style with visible grain, 2 to 3 inks per image |

Depth: short paper shadows (`0 1 0` black 6% plus `0 8 16 -8` black 18%), stickers lifted further. Taped or stuck things sit at -1.5 to 1.5 degrees; text blocks you read are never rotated.

### C.4 Signature motif

**The marker circle.** On every screen one hand-drawn volt circle draws itself around the one thing that matters (the next move, the score, the wrong option's fix), and at most one margin note in Caveat with a little arrow says something human about it. A circled number on ruled paper, with a sticker in the corner, is unmistakably MockMob.

### C.5 Navigation: index tabs on acetate

- **Destinations (4):** Today, Practice, Mistakes, Me. Review is renamed **Mistakes** because that is what the student calls them. Learn folds into Mistakes (each mistake opens its concept page) and a shelf of concept posters in Practice.
- **Shape:** a floating acetate tray, 68 dp tall, inset 12 dp from the sides and 8 dp above the gesture inset, radius 24. Inside, four paper index tabs of equal width with 12 dp rounded tops stand up from the tray.
- **Indicator:** the active tab is 8 dp taller, in its own paper colour (Today volt, Practice periwinkle `#C9D3F7`, Mistakes pink `#F5C6D6`, Me butter `#F7E0A3`), with Ink text. Inactive tabs are cream paper at 85% with Ink 2 text. On a switch, the old tab drops and the new one rises on a paper-snap spring (300 ms, bounce 0.25) with a -1.5 to 0 degree settle, a marker underline draws under its label (180 ms), and the tray's tint shifts to the new colour (200 ms).
- **Icons:** a custom 24 dp hand-drawn set with an uneven 2 dp marker stroke: Today is a sun over a ruled line, Practice a pencil, Mistakes a circled question mark, Me is Mobi's face. Labels always visible, 12 sp Hanken 600.
- **Press:** the tab presses 2 dp into the tray (100 ms).
- **Haptics:** `selectionClick` on a change; nothing on a re-tap.
- **Scroll:** scrolling down tucks the tray 18 dp lower so only the tab tops with their labels show; it returns on scroll up or idle. Hidden on the runner, repair and result.
- **Badge:** Mistakes shows the real count on a small pink sticky dot.
- **TalkBack:** "Mistakes, tab 3 of 4, 6 to fix."

### C.6 Onboarding: "Mobi's notebook" (14 screens)

The flow is a conversation on a notebook page. Mobi's lines are printed (Hanken 17 sp) beside a small Mobi sticker; the student answers by tapping paper chips; each choice is written into the page in your-pen blue (short Caveat echoes) and may earn one margin note. Four paper tabs at the top edge (Aim, Subjects, Rhythm, Save) fill in as each part is done.

**1. Cold open.** Warm paper. A volt marker circle draws itself in stop-motion (12 fps, 420 ms), a tick draws inside it, the sticker lifts (its shadow grows), and the wordmark's underline draws. 1.3 s, tap to skip. Haptic: `lightImpact` as the tick lands. Reduced motion: the finished mark fades in over 200 ms.

**2. Welcome.**
- Layout: the top half is a riso illustration (C-1): Mobi on a stack of notebooks holding a red pen, a desk lamp, a few sticky notes. Below it on ruled paper:
- Headline (Instrument Serif 40): "The best notebooks have every trap circled."
- Support: "Start yours. MockMob circles the traps in your CUET prep, helps you fix them, and checks the fix stuck."
- Inputs: "Open my notebook" (volt), "I already have an account".

**3. Stage.**
- Mobi: "First things first. Where are you right now?"
- Chips: "Class 12, CUET 2027", "Passed Class 12, CUET 2027", "Class 11", "Not sure yet".
- Echo in blue: "Class 12, CUET 2027".
- Mobi: "About 30 weeks to the expected May window. Enough, if we spend them well."
- Margin note: "30 wks" with a circle.

**4. Course.**
- Mobi: "Which course are you chasing?"
- Chips, two lines each: "B.Com (Hons)" over "55 colleges in 2026", "B.Com" over "44", "B.A. (Hons) Economics" over "40", "B.A. (Hons) Business Economics" over "10", "BMS" over "9", "BBA (FIA)" over "2", "Something else", "Not sure yet". Quiet link: "Not commerce?"
- Mobi: "B.Com (Hons). 55 colleges offered it in 2026. Let's narrow that down."

**5. Dream colleges.**
- Mobi: "Dream list. Up to three, no judgement."
- Input: "Pick colleges" opens an acetate sheet with search and a list; "Open to any".
- Payoff: Mobi tapes a sticky note onto the page with the three names in blue.

**6. What it takes (first reveal).**
- Layout: the page turns to a full note. A big Gabarito "924.3" with a volt marker circle drawing around it.
- Headline: "Last year's bar at SRCC."
- Label: "B.Com (Hons), 2026 first list, UR."
- Rows: "Hindu College 919.9", "Hansraj College 907.5".
- Rule: "B.Com (Hons) takes one language, Mathematics or Accountancy, and any two more."
- Fit, with a blue tick: "English, Accountancy, Business Studies and Economics keeps all three open."
- Margin note: "your list, in one line".
- Input: "Got it. Subjects next."

**7. Subjects and how solid each feels.**
- Mobi: "Now be honest. How solid is each one?"
- Layout: a graph-paper card; each subject has its cover-colour tab, its name, "Practice ready" where true, and a segmented Shaky, Okay, Strong. General Test: "Opening soon. I'll tell you."
- Payoff: rows reorder live, weakest first, and a margin arrow labelled "start here" points at the top row.
- Support line: "After your first check I'll show you where your gut was right."

**8. Biggest worry.**
- Mobi: "What eats your marks?"
- Chips: the same six worries as A and B.
- Payoff: Mobi answers one line per choice, for example "Silly ones. We'll hunt those first." The first move on the page updates.

**9. One real question.**
- Mobi: "One quick one. Accountancy."
- Layout: clean paper card, no rules under the text.
- Correct: a volt tick draws beside the option in stop-motion and the line reads "Clean. 14 seconds."
- Wrong: a red circle draws around the chosen option, the right one gets a volt tick, and "Classic trap. Here's the ten-second fix:" with the explanation. No haptic on wrong.
- Inputs: "Next", "Skip this one".

**10. Rhythm.**
- Mobi: "Pick a pace you'll actually keep."
- Inputs: a timetable strip M to S with tick boxes (four ticked), minutes chips (10, 20, 30), time chips (6:00 AM, 5:00 PM, 8:00 PM, 10:00 PM). Unticked days read "rest" in Caveat.
- Payoff, live: "About 120 sessions before the expected window. Rest days included."

**11. Page one (the climax).**
- Layout: the chat slides up and away; a fresh page slides in from the right with three taped cards, each taped on with a short stretch.
- Headline (Instrument Serif italic): "Page one. Week one."
- Cards: "First move: starting-point check. 10 questions, Accountancy, about 10 minutes." "Rhythm: four evenings, 20 minutes, 8:00 PM." "Dream list: SRCC, Hindu, Hansraj."
- Line: "Written from your answers. Your first check sharpens it."
- Input: "Hold to sign it": a signature scribble draws along the foot of the page while the finger is down (1.2 s), Mobi stamps a small circled-tick beside it, `mediumImpact`. A plain "Sign it" target serves TalkBack and reduced motion. Secondary: "Change something".

**12. Save (age first, then the account).**
- Headline: "Don't lose page one."
- Support: "Sign in and your notebook follows you to mockmob.in and your next phone."
- Age row: "Quick one: are you 18 yet?" "Yes", "Not yet", "Rather not say". "Under 18, usage tracking stays off."
- Inputs: "Continue with Google" (volt), "Use an email code", "Not now".
- States: "Saving page one" while pending; "Saved to your account." after acknowledgment; on failure "Couldn't save. Page one is still on this phone." with "Try again".

**13. Reminders.**
- Headline: "Want a sticky note at 8:00 PM?"
- Layout: a butter sticky note preview: "Tonight, 8:00 PM" over "Ten minutes of Accountancy is ready."
- Support: "Only on your days. Never after 11:00 PM."
- Inputs: "Remind me", "Not now", equal weight.

**14. First move (the personalised reveal).**
- Layout: the page curls over to reveal Today's page, already written from the answers, with the starting-point check taped at the top and circled in volt.
- Headline: "Today's page."
- Inputs: "Start the check" (volt), "Tonight at 8:00 PM".

### C.7 Today, result reveal, celebrations, streaks, return

**Today:**
- Header: "Tuesday, 13 October" in Instrument Serif, with "30 weeks to the expected window" small beneath.
- Next-move card, taped with washi: "Fix 6 Partnership questions", a big Gabarito "6" circled in volt, "About 12 minutes", and a volt "Start" button.
- One margin note from Mobi, only when the data backs it: "same trap, 4 times. let's end it."
- "Mistakes caught": a row of pink sticky notes, one per chapter, with real counts.
- "This week": the timetable row with ticks, rest days marked "rest", and "3 of 4 sessions".
- "Dream list": three paper labels with their 2026 first-list figures.
- An unopened result takes the top slot as a face-down sheet with a paper clip.

**Result reveal: "Marked".**
1. The answer sheet arrives face down with a paper clip. "Flip it" (tap or swipe).
2. It flips (500 ms). The marks animate section by section in stop-motion at 12 fps over 900 ms: volt ticks for right, red circles for wrong, nothing for left, `selectionClick` per section.
3. The score: Gabarito 96 "183" with "/250", and a volt marker circle draws around it like a teacher's mark; "38 right, 7 wrong, 5 left".
4. Recap sticky notes (swipe): "Where the marks went" (a bar chart with exact bar lengths and a marker texture), "First thing to fix" (the chapter circled in red pen), "What's recorded" with "Fix it now, about 12 minutes".
- Lower or held: no stop-motion flourish; the marks fade in plainly, and the first note is "Here's the first thing to fix."
- Decay and skip as in spec 5.6.

**Celebrations (server-acknowledged only):**
- Small: a tick draws, `selectionClick`.
- Milestone: a rubber stamp (code-drawn frame with live text "Fixed", "Banked" or "Checked" and an ink-spread mask) slams onto the card, `successNotification`, with the fact line "Fixed in 4 min 12 s. Fresh check opens tomorrow."
- Big (first mock banked, fresh check passed): a full-page riso illustration (C-5), the stamp, one fact sentence, and three controls (share, see it, next). The student earns a collectible Mobi sticker for real milestones only; stickers live in a sticker book in Me and are never sold or randomised.

**Streaks:** the weekly timetable with ticks and "rest" days; the sticker book never loses anything.

**Return:** a Mobi sticker holding a sticky note: "Welcome back. How long have you got?" with 10, 20 and 30 minute chips.

### C.8 Motion and haptic language

| Name | What | Curve and duration |
| --- | --- | --- |
| Snap | Tabs and stickers settling | Spring 300 ms, bounce 0.25 |
| Slap | A sticker placed: scale 1.15 to 1.0, rotate +4 degrees to its final angle, shadow grows | Snap, 260 ms |
| Draw | Marker strokes (path trim) | `cubic-bezier(0.2, 0.8, 0.2, 1)`, 400 ms |
| Stop-motion | Ticks, squiggles and circles in reveals | Stepped at 12 fps |
| Flip | A sheet or card turning over | `cubic-bezier(0.16, 1, 0.3, 1)`, 500 ms |
| Curl | Page turn (rotateY plus skew plus a moving shadow) | Same curve, 520 ms |
| Tape | A washi strip stretching on | Ease-out, 180 ms |
| Stamp | Celebration | Scale 1.25 to 1.0 in 200 ms, 80 ms settle, ink spread 300 ms |
| Exit | Anything leaving | `cubic-bezier(0.4, 0.3, 0.8, 0.6)`, 200 ms |

- **Never moves:** question text, options, the timer, explanation body, numbers once landed. Text you read is never rotated.
- **Reduced motion:** strokes appear complete, the stamp fades in, flips and curls cross-fade, tape is static, stickers appear in place.
- **Haptics:** `selectionClick` (tab, chip, option, each reveal section), `lightImpact` (a sticker slap, a page turn), `mediumImpact` (signature complete), `successNotification` (acknowledged submission, repair, milestone), `warningNotification` (leaving a timed mock). None on wrong answers.

### C.9 Imagery plan

**Image bible for C:** risograph and gouache illustration with two or three inks per image (volt `#D2F000`, a deep ink `#17150F`, plus one of the tape or cover colours), visible riso grain and slight misregistration, flat shapes with soft texture, no gradients; Mobi always the lime folded-sheet robot with a black visor; no text, letters or numbers in any image; no real people's faces, no institution buildings or crests. Stickers on transparent backgrounds with a white die-cut border.

| Id | Asset | Size and budget | gpt-image prompt |
| --- | --- | --- | --- |
| C-1 | Welcome illustration | 768 x 900, 120 KB | "Risograph illustration in three inks (electric lime #D2F000, deep ink #17150F, soft periwinkle #C9D3F7) on warm cream paper (#F3EFE6), visible riso grain and slight misregistration. A small friendly robot mascot shaped like a lime folded sheet of paper with a black visor and two white eyes sits on top of a tall stack of notebooks, holding a red pen like a sword, a desk lamp casting a cone of light from the left, three sticky notes stuck to the stack. Night-study mood, warm and witty. Generous empty cream space in the lower third. No text, letters or numbers anywhere." |
| C-2 | Mobi sticker set, 12 poses | 384 px, 15 to 30 KB | "Flat sticker illustration of a small friendly robot mascot shaped like a lime (#D2F000) folded sheet of paper, black visor with two white rounded eyes, short black arms and legs, confident hand-drawn black marker outline of uneven thickness, subtle riso grain inside the fills. Pose: [holding a red pen and pointing at something off-frame]. Die-cut with a thick 8 px white border following the outline and a soft drop shadow. No text. Transparent background." |
| C-3 | Paper tiles (Notebook and Night) | 256 px tiles, 15 KB each | "Seamless tileable macro texture of [warm cream #F3EFE6 / dark charcoal #161512] uncoated paper with very subtle fibres, flat even lighting, no lines, no stains, no text." |
| C-4 | Craft kit: four washi strips, three sticky notes, a paper clip | 200 to 400 px, 5 to 15 KB each | "A single strip of [pink #F5C6D6] Japanese washi tape with torn ends and a faint printed dot pattern, slightly translucent, top-down, soft shadow, transparent background, no text." (Variants: mint, periwinkle, butter; a square butter sticky note with a slight curl; a silver paper clip.) |
| C-5 | Milestone pages (3: first mock banked, first fix, fresh check passed) | 768 x 1000, 120 KB | "Risograph illustration in three inks on cream paper: [the lime folded-sheet robot mascot standing on a giant open answer sheet, stamping it with a huge rubber stamp, ink splatter around]. Joyful but not childish, strong composition, riso grain, empty space at the top for a headline. No text, letters or numbers." |
| C-6 | Concept posters (5, one per subject) | 600 x 800, 80 KB | "Risograph poster illustration in [ledger green #2F6B4F] and electric lime on cream paper: [Accountancy: a balance scale made of stacked ledger books with coins on each pan]. Bold flat shapes, riso grain, a large empty band at the bottom for a title. No text." (Business Studies: an org chart made of paper cups and string; Economics: a demand curve drawn as a road with a tiny scooter; English: an open book whose pages turn into paper planes; General Test: a puzzle of interlocking pencils.) |
| C-7 | Empty states (3: nothing to fix, offline, all caught up) | 480 px, 30 KB | "Risograph spot illustration, two inks (lime and deep ink) on transparent background: [the lime folded-sheet robot asleep on a closed notebook with a tiny 'z' shape drawn as a squiggle, not a letter]. Riso grain, no text." |

**Better as SVG or code:** six hand-drawn marker circle variants, ticks, arrows, underlines and the signature scribble (drawn once by hand as SVG paths so they can animate by path trim); the hand-drawn icon set; rule lines and graph grids; stamp frames with live text; highlighter strips (9-slice); bar charts with a marker texture mask; the index tabs and tray.

### C.10 Concept render prompts (gpt-image, portrait 9:19.5)

Shared preamble: "High-fidelity mobile app UI design, a single Android phone screen shown flat and front-on at 1080 x 2340 (9:19.5), no hand, a thin black bezel with small rounded corners, Android status bar showing 8:41 PM, signal and battery, a slim gesture handle at the bottom. The phone is centred on a plain warm grey #E9E3D6 canvas, with a tiny grey caption under the phone: 'MockMob concept, sample data'. Typography: headlines in an elegant high-contrast serif like Instrument Serif; big numbers and buttons in a rounded bold grotesque like Gabarito; body text in a clean grotesque like Hanken Grotesk; very short handwritten margin notes in a casual marker script like Caveat. Ground is warm cream paper #F3EFE6 with faint ruled lines. Sentence case, no emoji, no exclamation marks. Crisp legible text, premium editorial-collage quality, 16 dp margins, uncluttered."

1. **Onboarding hero (Welcome).** "[Preamble]. The top half is a risograph illustration in lime, deep ink and periwinkle with visible grain: a small lime robot shaped like a folded sheet of paper, with a black visor, sits on a stack of notebooks holding a red pen, a desk lamp shining from the left, sticky notes on the stack. Top left over the illustration: the wordmark 'MockMob' in bold rounded type with a hand-drawn lime marker underline ending in a tick. Below on ruled cream paper: a two-line serif headline in near-black, 'The best notebooks have every trap circled.' Under it in dark grey 16 sp: 'Start yours. MockMob circles the traps in your CUET prep, helps you fix them, and checks the fix stuck.' A full-width lime pill button with near-black text 'Open my notebook', and a text button 'I already have an account'. No footer."
2. **Mid-onboarding personalisation (subjects).** "[Preamble]. At the top, four small paper tabs 'Aim' (filled lime), 'Subjects' (active), 'Rhythm', 'Save'. A small die-cut sticker of the lime folded-sheet robot at the left beside a printed line: 'Now be honest. How solid is each one?' Below, a graph-paper card with four rows, each with a small coloured paper tab at the left (dark green, navy, brick red, plum), the subject name, and a three-part segmented control 'Shaky', 'Okay', 'Strong': 'Accountancy' set to Shaky, 'Economics' set to Okay, 'Business Studies' set to Okay, 'English' set to Strong. A small grey label 'Practice ready' under each name. A hand-drawn lime arrow in the margin points to the Accountancy row with the handwritten note 'start here'. Under the card, a line in blue handwriting-style text 'Class 12, B.Com (Hons), SRCC +2'. A lime pill button 'Continue' at the bottom."
3. **Today with the navigation visible.** "[Preamble]. Top: serif date 'Tuesday, 13 October' and small grey text '30 weeks to the expected window'. A white paper card held at its top corner by a strip of pink washi tape, slightly rotated 1 degree: title 'Fix 6 Partnership questions', a huge bold rounded numeral '6' with a hand-drawn lime marker circle around it, grey 'About 12 minutes', and a lime pill button 'Start'. In the right margin, a tiny handwritten note 'same trap, 4 times. let's end it.' with a little arrow. Below: 'Mistakes caught' with three pink sticky notes in a row reading 'Partnership 6', 'Delegation 3', 'Elasticity 2'. Then 'This week' with a timetable row of seven boxes, three ticked, one marked 'rest' in handwriting, and '3 of 4 sessions'. At the bottom, floating: a translucent tinted acetate tray with a faint halftone dot pattern and blur, with four paper index tabs standing up from it: 'Today' (active, taller, lime paper, near-black label with a marker underline), 'Practice', 'Mistakes' with a small pink dot '6', and 'Me', each with a small hand-drawn icon."
4. **Result reveal moment.** "[Preamble]. Mid-reveal: a white answer sheet lies on the paper ground, just flipped face up, a silver paper clip at its top. A grid of 50 small answer circles in 5 rows of 10: most have lime hand-drawn ticks, a few have red hand-drawn circles, a few are empty; the last row's ticks are half drawn, with a small motion blur. At the top of the sheet, a huge bold rounded number '183' with '/250' beside it, and a hand-drawn lime marker circle being drawn around it, the stroke three-quarters complete. Under it, grey text '38 right, 7 wrong, 5 left'. At the bottom edge, a butter sticky note peeking up reading 'First thing to fix'. A small sticker of the lime robot holding a red pen in the lower left corner. No navigation bar."

### C.11 Performance plan and biggest risk

- **Live blur:** the acetate tray and at most one sheet, grouped. Nothing else.
- **Pre-rendered:** stickers, illustrations, paper tiles and tape (WebP, small). Rule lines and grids are drawn in code once per page into a `RepaintBoundary`.
- **Animated budget:** marker strokes are path-trim animations over precomputed `PathMetrics` (cheap); stop-motion runs at 12 fps, so most frames have nothing to repaint; at most two stickers and one illustration per screen to keep alpha overdraw low.
- **Frame budget:** 11.1 ms at 90 Hz; raster p90 at or under 7 ms on Today (paper is cheap); the runner at or under 6 ms with textures off.
- **Biggest risk: clutter and the "cute scrapbook" read.** It is the direction most likely to break the owner's "Reduce rather than decorate", and the least like the dark, cinematic taste in his CampusOS briefs and the Revolut and high.live references. It also needs the largest illustration set, which must stay consistent across dozens of assets. Secondary risk: Caveat and textured paper can look smudgy on a 300 dpi LCD.

---

## D. The three side by side

| | A. Bubble | B. Afterhours | C. Margin Notes |
| --- | --- | --- | --- |
| What MockMob is | A toy made of the exam's own answer sheet | A premium night room where your evidence is the light | The senior's annotated notebook |
| Default ground | Ink `#141414` (Paper as a full theme) | Night `#101210` (Daylight as an option) | Notebook paper `#F3EFE6` (Night notebook as a theme) |
| Loud move | Subject chapter bands plus glossy props | Monumental condensed numbers in a lit dark scene | The self-drawing marker circle |
| Glass | Frosted dock with a liquid volt lens, fake glass on bands | Frosted dock plus Start circle, smoked fake glass on art, liquid lens | Tinted acetate tray, highlighter film |
| Imagery | Glossy vinyl and inflatable 3D | Photoreal glass, graphite and chrome renders, light fields | Riso and gouache illustration, stickers, paper |
| Type | Unbounded and Figtree | Bricolage Grotesque (variable width) and Hanken Grotesk | Instrument Serif, Gabarito, Hanken Grotesk, Caveat |
| Mobi | Restyled as a vinyl bubble-head toy | Restyled as a small glass robot with a light visor, used less | Kept, amplified as a sticker character |
| Navigation | 4 tabs: Today, Practice, Fixes, You | 3 tabs plus a Start button; You behind the avatar | 4 index tabs: Today, Practice, Mistakes, Me |
| Onboarding object | Your sheet (bubbles fill) | Your pass (lines engrave, card flips and seals) | Page one (a chat that becomes a signed page) |
| Result reveal | Pop the seal; droplets fill the grid | The fold: drag-to-unfold sheet with a light sweep | Marked: ticks and circles draw on, the score is circled |
| Motion character | Squishy, liquid, bouncy | Weighty glide, near-critical springs | Snappy paper, stop-motion marker |
| Closest reference | HIGH's candy layer | Revolut's home and HIGH's tool layer, Fampay's lighting | Fampay's stickers and voice, HIGH's story cards |
| Fit with the owner's taste ("dark, cinematic, editorial, tactile, selective glass") | Medium: tactile and glassy, less cinematic | High | Low to medium: editorial and tactile, not cinematic |
| Fit with "something premium" | Medium (toy risk) | High | Medium (scrapbook risk) |
| Fit with "high.live is crazy" energy | High | Medium on its own | Medium to high |
| M06 cost | Low to medium | Medium (art under a live dock) | Low |
| Asset volume | About 30 images | About 25 images | About 45 images |
| Continuity with mockmob.in (Night Arena, volt) | Medium | High | Low |
| Biggest risk | Reads young | Over-lit, generic dark | Cluttered, cute |

---

## E. Recommendation: Afterhours, with the Bubble's pulse and the Notebook's voice

**Build Direction B, "Afterhours", as the world, and transplant three specific things from A and C.** Then run HIGH's two-layer rule on top of it: everyday screens are quiet and dark; the moments are loud.

### E.1 Why B is the base

1. **It matches the owner's own taste profile more closely than anything else.** His CampusOS briefs ask for "dark, cinematic, youthful, intelligent, tactile... editorial, expressive", "selective physical glass", "Everything glides. Every interaction has weight", and "This looks expensive". B is built from exactly those words: one light per screen, smoked glass on floating parts, near-critical springs, monumental type.
2. **It answers "a good navbar wouldn't look like this... this is not interactive at all" with the most interactive piece in any of the three:** a split glass dock with a lit, velocity-stretched, drag-scrubbable tab and a Start button that morphs into a quick-start sheet. That morph is the Revolut "the input becomes the message" grammar, applied to the core loop.
3. **It is the closest to Revolut and Fampay where they are strongest,** without copying either: Revolut's art-backed hero with one big number, frosted actions and a glass list card; Fampay's environment-lit near-black and one rendered object per subject; Fampay's "speed as proof" in the measured repair time.
4. **It extends the brand that already exists.** mockmob.in already runs the Night Arena (dark ground, volt as the only accent). B makes the app and the website one brand, which matters if the owner does redesign "the entire brand": the redesign can start in the app and flow back to the web without a second identity.
5. **Its signature moments come from MockMob's own objects.** The folded answer sheet is already Mobi's body and the spec's A1 reveal. B turns it into the logo, the result ritual and the onboarding pass. That is the "built around its own central idea" the owner's standards ask for.
6. **It is the most honest frame for a serious exam.** The audience is 17 and aiming at SRCC and Hindu. A calm room where the numbers are big and true reads as respect, which is what the research means by "calm agency".

### E.2 What to take from A (the pulse)

- **The bubble as the unit of progress.** Inside B, every row of progress (the week's sessions, the 50-cell grid on a sheet, the onboarding segments) is drawn as OMR bubbles that fill with ink, not as generic dots. This is exam-native and gives B a second ownable motif at almost no cost.
- **The juicier dock spring.** B's springs everywhere stay weighty (bounce at most 0.12), except the dock's lit tile, which uses A's bounce 0.18 and velocity stretch. The one control the owner touches most should feel alive.
- **Subject identity through colour, made premium.** A's idea that each subject owns a hue survives as B's subject light fields (amber, indigo, teal, rose, moss), so the five subjects are still recognisable at a glance, without candy.

### E.3 What to take from C (the voice)

- **The senior's voice:** short, specific, a little dry, in the student's words ("What keeps you up at 1 AM?", "Same trap, 4 times. Let's end it."), with Mobi allowed one factual line in onboarding, empty states and celebrations.
- **Earned collectibles:** the milestone tokens (B-6) collect on a shelf in You, one per real milestone, never sold or randomised. That is C's sticker book in B's material.

### E.4 The HIGH lesson: two layers

HIGH keeps a candy layer for reward moments and a dark, tight layer for data. In the blend, the **moment layer** (cold open, welcome, the bar reveal, the plan flip and seal, the result fold, milestone screens) gets the full treatment: rendered art, the dolly, light sweeps, monumental numbers, shards. The **work layer** (Practice lists, Review, the runner, repair, settings) is quiet: solid surfaces, Hanken text, no art behind reading, no idle motion. That keeps the "crazy" where it inspires and the calm where students have to think, and it is the best defence against the owner's "overdone the lighting" and "reduce rather than decorate".

### E.5 Why not A or C on their own

- **A alone** is the most fun and the most original motif, but the vinyl-toy finish and candy bands risk reading younger than the student and less premium than Revolut. Its best ideas survive in the blend.
- **C alone** has the best voice and the strongest product metaphor for repair, but it is the busiest, the furthest from the owner's dark and cinematic taste, the most expensive to illustrate consistently, and the most likely to be called cluttered. Its voice survives in the blend.

### E.6 What the recommended blend's four concept renders should be

Use B.10's four prompts with two changes: in render 3 (Today), draw the "This week" ring as seven small bubbles inside the top-bar circle and the four filled ones in lime ink; in render 4 (result), draw the 50 cells as filled and hollow answer bubbles. If the owner wants to compare, render A.10's prompts 1 and 3 and C.10's prompts 1 and 4 as well (eight images in total), so he can see each idea at its loudest.

---

## F. Decisions for the owner, and the next steps

### F.1 Decisions

1. **Direction:** B with the A and C transplants (recommended), or A, or C, or a different blend.
2. **Night as the default theme**, with Daylight as a composed option in Appearance.
3. **Navigation:** three tabs plus Start, with You behind the avatar (recommended), or four tabs (Today, Practice, Review, You) plus Start.
4. **Mobi:** restyle to the glass robot with a light visor (recommended for B), and allow one short factual line in onboarding, empty states and celebrations. No Rive; a code rig.
5. **Type:** adopt Bricolage Grotesque for display and numbers, keep Hanken Grotesk for text. Retire Gabarito except as the numeral fallback if Bricolage's tabular figures fail the check.
6. **Brand scope:** new wordmark, mark and app icon now in the app, with mockmob.in following in a later pass, or app-only for now.
7. **Onboarding:** 14 screens with the account after the plan reveal and Google first (recommended), and whether the dream-college step stays (onboarding research D3).
8. **Celebrations:** light shards and tokens instead of confetti; sound stays off.
9. **Renders:** generate the four B renders (plus the optional four from A and C) with gpt-image in ChatGPT or Codex. These are the owner's own tools, not the MockMob API budgets; confirm before anyone spends.
10. **Video:** not needed inside the app (pre-rendered art and code motion cover it). Worth considering later for the Play Store promo and the website hero.

### F.2 Next steps once a direction is picked

1. Render the concept images and review them with the owner (no code yet).
2. Reconnect the M06 and run benchmarks B1 (refresh rate, renderer, cold start), B2 (glass dock over a fast-scrolling list of art cards) and B6 (the lens shader), then B7 (light fields under the dock). These decide sigma, the lens, and Full or Lite glass on the M06.
3. Write the design spec that replaces APP-DESIGN-SPEC's visual and copy sections: tokens (colour roles with translucency, light, edge), type roles, the motion and haptic tables above, the dock, the sheet, the pass and the fold.
4. Generate the image set against the chosen image bible, in one batch, then compress (`cwebp`) and check the asset budget (under 3 MB of raster art in the first release).
5. Build in the order the owner will see it: cold open, onboarding (as a step deck), Today, the result fold, then Practice, Review and You. Remove the route placeholders before any build reaches the owner's phone.
6. Owner phone pass on the M06 with profile-mode frame timings, both themes, TalkBack, reduced motion, and a check of every screen against the slop list.
