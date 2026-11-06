# MockMob: three design directions, final (brand and app)

Date: 13 October 2026. Written by the design director for the owner's decision. This is a proposal. Nothing in it is built, rendered or bought yet.

This file replaces `directions.md` as the version to decide from. `directions.md` stays in the folder as the first draft. The first draft was three paint jobs on one onboarding: the same 14 steps, the same questions and largely the same lines, with only the material, the font and the name of the identity object changed. It also copied several of HIGH's and Revolut's exact values while calling them original, and it collected onboarding answers that never paid off later. This version fixes that:

- The three directions now differ in **what happens**: the order of the first run, what the home screen is, how navigation works and what the student is building. The look follows from that.
- Every copied token is gone (listed in 0.4).
- Onboarding ends on the student's **real** marked result, and reminders are asked after it.
- The screens the owner actually complained about after onboarding are designed: day-one Today, Practice, the runner, the before-mock sheet, "Finish for now", repair and the fresh check, You, and a home-screen widget.
- Every image prompt is rewritten to production standard around objects a CUET Commerce student actually owns.
- Concept screens are built as prototypes with real type, not as AI renders with garbled copy.
- Section G asks the owner eight questions whose answers change what gets built.

Inputs, all read in full: `owner-materials.md`, `ref-high.md`, `ref-revolut.md`, `ref-fampay.md`, `onboarding-research.md`, `flutter-feasibility.md`, the owner's UI/UX standards (`AI OS/wiki/concepts/ui-ux-standards.md`), the first draft `directions.md` and the critique of it, `APP-DESIGN-SPEC.md` (sealed sheet A1, sections 5 to 8), the Galaxy M06 screenshots in `tmp/app-shots/m06`, and the data files `public/du/2026/index.json`, `public/du/2026/offerings/*.json`, `public/du/2026/rules.json` and `data/cuet_chapter_priorities.json`.

How to read it. Section 0 is what every direction shares: rules, the product contract and the engineering gates. Sections A, B and C are the three directions, each with the same eleven subsections, so they can be compared line by line. Section D compares them, E gives the recommendation, F lists decisions and next steps, and G holds the questions for the owner.

Numbers. DU figures were checked against the repo data on 13 October 2026: B.Com (Hons) ran at 55 colleges in CSAS 2026 (B.Com 44, B.A. (Hons) Economics 40, B.A. (Hons) Business Economics 10, BMS 9, BBA (FIA) 2). B.Com (Hons) Round 1 minimum allocation scores, UR: SRCC 924.3, Hindu 919.9, LSR 912.5, Hansraj 907.5, Kirori Mal 903.7, Ramjas 895.6, Sri Venkateswara 891.5. SRCC in other categories: OBC-NCL 849.1, EWS 887.9, SC 796.4, ST 723.6. Every other number in sample copy (mock scores, counts, times, names) is a sample value for prototypes.

---

## 0. The brief, and what every direction shares

### 0.1 What we are replacing, in one paragraph

The current app is a paper or charcoal ground with identical white keycap rows, a static Mobi sticker, a stock Material tab bar that covers content, and defensive copy at the foot of nearly every screen ("MockMob is not affiliated with NTA or Delhi University", "Sample questions. This is not a diagnosis.", "Practice, not proof", "Uses 10 credits. You have 100."). The onboarding is the website's five-question sample, the same for every paper, ending in a "4 of 5" and a dashed box that explains what the app cannot do. Today, Splash and the runner are route placeholders. The owner called it "really basic", "rudimentary" and "not interactive at all". He asked for "a really fancy UI: something premium, something which inspires people to use the app", with high.live, Revolut and Fampay as the vibe, and he is open to redesigning the whole brand.

### 0.2 The bar each direction is held to

- **A direction changes what happens, not only how it looks.** Each one has its own first-run order, its own home screen and its own navigation model. If two directions could share a storyboard, one of them is not a direction.
- **One central idea, visible in every screenshot and doing a job in each.** It must be a working object (it holds real state), not a theme.
- **Every answer the student gives pays off twice:** once visibly on the same screen, and again later in the plan, on the home screen or in the first recap (0.7).
- **Premium means it looks expensive and is fun to use.** It also means restraint: one loud move per screen, everything else quiet ("Reduce rather than decorate", "Maybe you have overdone the lighting").
- **Nothing borrowed at the value level.** Ideas from HIGH, Revolut and Fampay are allowed. Their hues, curves, durations, layouts and signature objects are not.
- **Smooth on the Galaxy M06** (Mali-G57 MC2, 3.5 GB, about 384 x 853 dp; 90 Hz to be confirmed by benchmark B1).

### 0.3 Integrity rules every direction keeps (behaviour, not footers)

1. Success, "Saved", haptic success and celebration fire only after the server acknowledges.
2. No invented numbers: no user counts, testimonials, percentiles, chances or "top 10%". Real DU figures use DU's own terms: "CSAS 2026, Round 1 minimum allocation score", always with the scale ("out of 1000"). Never "first list", which is pre-2022 language.
3. A short check is never projected to a CUET score, a rank or a college. "6 of 10" stays "6 of 10".
4. **One vocabulary for progress, used the same everywhere:**
   - **Found:** a mistake is recorded.
   - **Repaired:** a repair session on it is finished. This is the act, not proof.
   - **Checked:** the student passed a fresh check on questions they had not seen.
   - **Holds:** they passed it again on a later retained check.

   "Fixed" and "Fixes" are not used anywhere, because they claim an outcome before the evidence exists.
5. No recovered-marks, admission-chance or "mastered" claims.
6. Nothing decorative during a timed mock: no correctness, no Mobi, no motion beyond the timer and the save state.
7. **Celebration is proportional and specific.**
   - Finishing a mock is celebrated on its own ("Mock 1 is marked"). The score is celebrated only when it beats the student's own previous result in the same subject and mode.
   - A first mock gets no score celebration at all.
   - "Poor" means lower than the student's own last result, never a fixed threshold.
   - Never per question. Once per event id.
8. A reveal never withholds a result. Tap, the TalkBack action and "Open results directly" always work, and the ritual decays from the fourth sheet (spec 5.6). There is at most one press-and-hold ritual in the whole app, and it is on the result.
9. No punitive streaks, no variable or paid-random rewards, no guilt notifications. Weekly goals count real work ("2 of 3 repairs"), not sessions opened. Nothing earned dims, resets or is lost.
10. Badges and lists show what is **due today**, capped at 3, never the whole backlog. A pile of 47 is a guilt machine.
11. Glass carries text only at a tint that holds 4.5:1 over its worst backdrop. Targets are at least 48 dp, every control is named for TalkBack, and reduced motion keeps the same information.
12. No glow behind focal elements and no light as decoration. Edges and material do the work.
13. No build talk (route names, codes, service names) in any user-facing build.

### 0.4 What every direction removes

**Defensive and obvious lines.** The Welcome non-affiliation footer; every "sample, not a diagnosis" caption; "Example, not your plan yet"; "The five sample questions are the same for every paper"; "On this phone" on guest screens; every "Practice, not proof" tail; "This only decides your data settings"; source captions such as "Counts are DU's, from 2026 admissions" (the fact goes inside the line instead: "55 colleges ran B.Com (Hons) through CUET in 2026"). The non-affiliation statement and official sources live in You > Help and About and in the Play listing's full description, which is where every competitor puts it (`onboarding-research.md` 6.1).

**Cost-first rows.** The cost moves to the confirmation sheet, written as what you get: "10 questions, about 10 minutes. 10 credits."

**Slogans and filler from the first draft.** "Fill the sheet. Chase the seat.", "Your lost marks leave a trail.", "What keeps you up at 1 AM?", "Week one, sorted.", "Keep your pass.", "Don't lose page one.", "Evening, Aanya.", "Your plan, built from your answers.", "Received at 10:42 PM", and every "Fixed" or "banked".

**Copied tokens.**
- From HIGH: the subject hue set (lilac, bubblegum, cobalt, tangerine), the 168-degree three-stop band with a 74/8 radial highlight, the 7.2 s idle drift, the letter-rise curve, and the foil reward screen with share, see-it and next controls.
- From Revolut: the avatar, search pill and circle top row, the four circular actions, the "Recent" glass card, the pager with 85% scale, 60% opacity and 20 dp peeking neighbours, and its measured enter curve.
- From the first draft's own weak picks: the inflatable props, the smoked-glass slab, the fold mark, the struck-through wordmark, the glass Mobi, the pass, the notebook and washi kit, Unbounded, Instrument Serif and Caveat.

**The "sample data" caption in concept renders.** Concept screens are labelled in their file names and review notes, never inside the image.

### 0.5 Where the owner's new direction overrides the older standards, and where it does not

| Older rule (UXS, APP-DESIGN-SPEC) | Now | Still binding |
| --- | --- | --- |
| No glass or blur on content | Glass on floating parts (dock, sheets, overlays, controls over art); fake glass on hero cards over our own art | No glass under question text, options, explanations or result figures |
| No gradients or glow | Light and gradients allowed **inside art plates** and as scrims that make text legible over art | No gradient text, no halos on controls, no glow behind cards or focal elements, no copied gradient recipes |
| Dark ground must be neutral charcoal | Kept for dark themes | Yes |
| Mobi never speaks, poses only | Mobi may say one short factual line in onboarding, empty states and celebrations (owner decision, question G4) | Never during timed answering, never evaluative of the person, never guilt |
| No confetti, no particles | Restrained, real-milestone-only bursts drawn in one painter | Never after a poor result, never per question |
| Sentence case, no eyebrows, no emoji, no exclamation successes, no middle-dot strings, 12-hour time, tabular figures | Kept in all three | Yes |

### 0.6 Shared product structure

**Onboarding is a data-driven step deck, not hand-built screens.** Each step is a row in a versioned deck with:
- an id, a type (single, multi, ladder, rhythm, reveal, check, permission, account) and copy keys;
- a branch rule and the field it writes;
- a required "what visibly changes now" line and a required "where this pays off later" line. A test fails if either line is empty.

Courses, colleges, rules and cutoffs come from the DU 2026 index already in the repo. A new subject, exam or year changes data, not screens. That is the answer to "not even scalable". The five-question sample stays on the website, where it belongs.

**The onboarding contract.** Every direction keeps these eight rules, whatever its order.

1. **Say the time up front,** in the first screen's own words ("About 2 minutes to your plan. Skip anything.").
2. **Every step from goal to rhythm can be skipped,** and skipping falls back to a sensible default that is shown, not hidden.
3. **It ends on the real result.** The starting-point check (10 questions from the bank, server-scored) happens inside the first run, and the first run ends on its reveal. That reveal is the best moment in the product. It must not be left as homework after onboarding (Undertone lesson, V L109-114).
4. **Reminders are asked after that first reveal,** previewing a reminder built from the real result. If the student defers the check, the ask moves to the moment of deferral, framed as scheduling the check ("We'll nudge you at 8:00 PM").
5. **Age comes before the account,** held on the phone until sign-in. Usage-data consent for adults moves to after the first result.
6. **The account is asked when there is something to keep,** with Google first (Android Credential Manager), an email code second and "Not now" always visible. Where the server must score the check before the account exists, see question G2.
7. **The cold open plays on first launch only.** It is at most 1.0 s and tap skips it. Every later launch shows the Android 12 splash (a static mark) and paints the home screen from the last cached server payload, inside the 1.5 s cold-start budget, then refreshes.
8. **One press-and-hold ritual at most,** and it belongs to the result reveal, not to the plan.

**Learn.** A tab that says "Learning is not available right now" goes. Concepts open from the mistake they explain, and a Concepts shelf sits inside Practice until Learn has content of its own.

**Spine untouched.** The api, auth, repositories, storage, sync and session engine, routes and redirects, and all the providers stay. Theme, dock, keycap, sheet, splash, screens and copy are replaced (`flutter-feasibility.md` 14).

### 0.7 The payoff ledger: what each answer buys, now and later

| Input | Pays off now (same screen) | Pays off later |
| --- | --- | --- |
| Which CUET (stage) | Weeks to CUET, labelled expected until NTA publishes | Plan length; a lighter stretch during boards for Class 12 students (expected mid-February to early April 2027); the countdown on home and the widget |
| Course and colleges | The college ladder with real CSAS 2026 Round 1 scores and the scale | The ladder on home and in You; after save, it seeds the web Compass and cutoff tools |
| Category (optional, kept on the phone) | Ladder figures switch to that category | Same figures everywhere on this phone. The web asks separately |
| Subjects | The eligibility line ("keeps all three open") | Which subject the check uses; the plan's order |
| How solid each subject feels | Live reorder, weakest first | The "Your gut versus the check" card in the first recap. If that card is not built, the control is cut |
| Where the marks go (worry) | The first move visibly changes (table below) | The check's mode, the first week's mix and the target on home |
| Rhythm | "About 108 sessions before CUET" (sample, computed live, boards weeks counted at 2) | The week row on home, the widget time, the reminder time and quiet hours |
| Name (from Google, or one field) | Nothing. A name is never the headline | Used only where it helps, for example on a share card the student chooses to send |

**Worry mapping (the first move must really change).** Without this mapping the question does not ship.

| The student's words | The check | The first week | Home shows |
| --- | --- | --- | --- |
| "I knew it and still got it wrong" | Untimed, feedback after submit | Repair-first; each repair names the trap type | An accuracy target: "8 of 10 clean" |
| "The last 10 questions, no time left" | Timed, 12 minutes, time per question recorded | Two timed Quick 10s a week | "Your slowest: 2 min 40 s on Q4" |
| "Accounts numericals take me 4 minutes each" | Accountancy, numerical items first where the bank tags them | Numerical repairs first | Time per numerical, against your own last |
| "English passages" | English, one passage set | One passage set a week | Passage accuracy |
| "General Test reasoning" | Shown only when General Test is open | | |
| "No idea yet" | The balanced starting-point check | Chapter order from `cuet_chapter_priorities.json` | The next chapter by name |

`cuet_chapter_priorities.json` is an ordered list per subject (Accountancy: Partnership, Company Accounts, Financial Statements, Dissolution). It carries no frequency data, so copy names the chapter and never claims how often it appears.

### 0.8 The screens every direction must design (the contract)

The owner's complaint covered "the basic flow that I can see right now after onboarding", not only onboarding. Each direction designs all of these in its own model (subsection 7 of each).

- **Day-one home, two states:** the check deferred (nothing measured yet) and the check done (one result, a few mistakes, no week yet). Sample-data homes with "Mock 7" are not day one.
- **The usual home,** in this priority order (PB L253-255):
  1. a half-finished mock, which takes the hero slot;
  2. an unopened result;
  3. the next move;
  4. what is due today (at most 3);
  5. the week;
  6. the college ladder.
- **Practice:** one suggested session plus "Choose your own". Costs appear on the confirm sheet only.
- **The before-mock sheet:** the anxious moment, with the length, the time, how saving works and whether pausing is allowed.
- **The runner:** calm and solid. A tabular timer, a save glyph that fills only on server acknowledgment, a question palette, flag for review, and a leave guard.
- **Submit to marked:** "Sending" while pending, then "Marked" on acknowledgment, then the reveal.
- **The reveal and the recap cards, in this order:**
  1. where the marks went;
  2. the first thing to repair;
  3. your gut versus the check (first check only, when confidence was collected);
  4. against your last mock (from the second mock onwards; neutral wording when lower);
  5. what is recorded, plus the next ask.
- **Repair and the fresh check:** the trap, three to five targeted questions with feedback, "Repaired", a fresh check on unseen questions the next day ("Checked"), and a retained check about a week later ("Holds").
- **"Finish for now":** a real ending that says what was done and what is next, with no guilt.
- **Return after three or more days:** "Welcome back. How long have you got?" with 10, 20 and 30 minute choices. Nothing is lost.
- **You:** identity first (what the student has built), settings second.
- **The home-screen widget** (Android, via `home_widget` and Glance):
  - 2 x 2: the countdown plus tonight's move;
  - 4 x 2: adds the week;
  - one tap opens straight into the move;
  - quiet hours are respected.
- **Empty, offline and error states** that say what will appear, why it matters and how to start.

### 0.9 What gets connected ("many other things can be connected")

1. **Website hand-off (fast lane).** A deep link or the Play Install Referrer carries course, subjects and any website sample answers into the app. The first run opens with them already in place ("Picking up from mockmob.in") and skips to the first unanswered step.
2. **The dream list and subjects feed the web.** After save, they sync to the profile, so the web Compass and cutoff tools open with the same colleges. Category stays on the phone.
3. **The official NTA date lands on the countdown.** A server-config date with its source replaces "expected" automatically. The label changes from "May 2027, dates not out yet" to the real date, with no app release.
4. **The home-screen widget** is the cheapest premium return driver on Android, and neither reference app needs it.
5. **Notifications** carry the real next move ("Partnership, 12 minutes. 3 of your 10 went here"), only on chosen days and never after 11:00 PM.
6. **Share cards** (private by default, never showing marks) carry a deep link back into the app or the website.

### 0.10 Real dates and real feelings the copy may use

Dates, always labelled expected until official:
- Class 12 boards: mid-February to early April 2027.
- CUET registration: January to March 2027.
- The exam: May 2027.
- CSAS rounds: after results.

NTA's decision on the 2027 pattern is expected around 20 October 2026, so copy about paper length and subject caps stays generic until it is official.

Real feelings worth naming:
- a coaching test that came back at 142;
- boards and CUET squeezing the same months;
- knowing an answer and still marking the wrong bubble;
- a relative asking "DU mil jayega?" ("Will you get into DU?").

Example of copy that is specific and true: "Boards end in April. CUET is weeks later. The plan goes lighter in March."

### 0.11 Voice rules

- A sharp senior who got in and wants you in: short sentences, concrete nouns, dry humour.
- No slogans, rhymes or rule-of-three promise sentences.
- **Line lengths:** moment headlines two lines at most, written to fit the display face's measured characters per line. Body lines under about 90 characters.
- **Hinglish:** at most one caption-level phrase per screen, never in instructions, options or anything the student must act on. Example: "Aaj ka repair: 12 minutes, Partnership."
- **Never write:** "unlock", "supercharge", "level up", "your chances", "mastered", "join thousands", or any prediction of marks, percentile or rank.

### 0.12 Shared engineering gates (decided before visuals are final)

1. **Benchmarks first:** B2 (glass dock over a flung list of art), B6 (lens shader) and B7 (light and art under the dock) on the M06. **Lite glass is the default until B2 passes.** Appearance offers Full, Lite and Off.
2. **Display text** is clamped at 1.3x font scale (body text is never clamped). Line-break golden tests run at 1.0, 1.3 and 2.0.
3. **Dock scrubbing** starts only from a long-press on the active indicator, never from a plain horizontal swipe 10 dp above Android's gesture strip. It is tested with gesture navigation on.
4. **Nothing animates through a `ShaderMask`** (a `saveLayer` on Mali). Text reveals animate a `ClipRect` width per line. Moving shadows are pre-baked images.
5. **No parallax under fake glass** unless the pre-blurred slice is driven by the same scroll value.
6. **Daylight themes use an ink-filled active tab** (3:1 against its neighbours, WCAG 1.4.11).
7. **Images are decoded at display size** (`cacheWidth`). Pagers decode only the centre card and its two neighbours.
8. **Every tab root pads its bottom** by the dock height plus 16 dp.
9. **Haptics are tested on the M06's coarse motor** (B12) before the vocabulary is final.
10. **No stepped (12 fps) motion.** Hand-drawn strokes animate smoothly with a jittered path.
11. **Every display face is checked with fonttools** for `tnum` and `lnum` before adoption. Marks, timers and counts are never set in Hanken Grotesk, which has no tabular figures (`fonts.dart`). Gabarito, already bundled, has them and is every direction's fallback for numbers.

### 0.13 How concept screens and images are made

- **Concept screens are prototypes, not AI renders.** gpt-image misspells long UI copy and ignores hex codes. Each direction's four concept screens are built as HTML pages at 384 x 853 CSS px with the real fonts and the real tokens, exported at 3x, then shown on the M06. gpt-image makes only the art plates inside them.
- **File names carry the label**, for example `A-03-today_concept_sample-data.png`. Nothing is captioned inside the image.
- **Art pipeline:**
  1. Generate with gpt-image at quality high, in its native sizes (1024 x 1536 portrait, 1536 x 1024 landscape, 1024 x 1024 square). Use a transparent background for objects.
  2. Describe colours in words, never hex.
  3. Grade to the direction's palette afterwards with a fixed curves preset per direction.
  4. Convert with `cwebp -q 80 -m 6` (`-alpha_q 90` for cut-outs).
  5. Keep raster art under 3 MB in the first release.
- **House rules for every prompt:**
  - no legible text, letters, numbers or logos;
  - no crests, DU or college buildings, NTA marks or brand packaging;
  - no calculators (they are not allowed in CUET);
  - no real or realistic student faces;
  - no CGI gloss, inflatables, holographic foil, neon or lens flare.

  Sheets, bubbles, grids and charts are drawn in code, never generated.

---

## Direction A: "Your Sheet"

### A.1 The idea

**Core idea:** every student gets their own OMR answer sheet for the season, and the app is that sheet. Every onboarding answer, every question in a mock, every repair and every check is a bubble on it. It is the logo, the onboarding object, the dock indicator, the week row, the result reveal and the identity in You and on Today. It keeps filling with real evidence, so nothing on it is decoration.

**What happens differently:**
- **Goal first, then proof.** In about two minutes the student builds a plan whose bubbles fill as they answer. The same sheet then takes the real 10-question check, and the first run ends with that sheet being marked.
- **Home is the sheet.** It shows the live sheet and its week, not a dashboard.

**The ownable truth behind it.** Real OMR sheets are printed in a drop-out ink, a colour the scanner is built to ignore, so only the student's own marks count. MockMob uses that as its grammar. Each subject's sheet is printed in its own quiet form ink, and the only bright thing on any screen is the student's volt mark. In one line: "The grid is ours. The marks are yours."

**Mood:** precise, tactile, quietly premium and exam-native, with dark graphite and one volt ink.

**What it looks like in one screenshot:** a graphite screen, a crisp sheet card whose printed grid is in a muted form ink, volt-filled bubbles where real work happened, one large tabular number, a lamp-lit still life of an object from the student's own desk, and a frosted dock whose active tab sits in a liquid bubble.

**References, taken as ideas only:**
- From HIGH: the two-layer rule (loud moments, quiet work screens).
- From Revolut: "the input becomes the result" (an answer chip morphs into its bubble) and one big number with a small unit.
- From Fampay: open on the next move, and speed as proof (the measured repair time).

No values are borrowed: no gradient bands, no idle float, no letter-rise, no foil, no avatar-and-search top row, no circular action row, no peeking pager. Nobody in fintech or edtech owns the OMR sheet. It is the exam's own object, and in an Indian exam it is the most feared one.

### A.2 Brand

- **Wordmark:** `mockmob`, lowercase, Archivo ExtraBold at width 100, tracking -2.5%. Both o's are bubbles. The o in "mock" is a hollow ring in form ink. The o in "mob" is filled in volt by hand: the fill stops just short of the ring at one o'clock, as a real pencilled bubble does. That small sliver of paper is the brand's signature detail. In motion, the ring prints first and then the fill rises (A.8).
- **Mark: "the human fill".** A ring with an off-centre volt fill that leaves the one o'clock sliver.
  - App icon: the mark at 60% of the adaptive-icon safe zone on Graphite.
  - Monochrome themed icon: the ring plus the fill shape as one glyph.
  - At 16 dp the sliver is dropped and it becomes a plain filled bubble.
- **Name:** unchanged. Rename scope is question G6.
- **Palette.** Night is the default, and Day is a fully composed theme.

| Role | Night (default) | Day | Notes |
| --- | --- | --- | --- |
| Ground (Graphite) | `#111311` | `#F2F3EE` | Neutral, a hair of green to match mockmob.in |
| Raised | `#191C19` | `#FFFFFF` | Cards, rows, the sheet |
| Raised 2 | `#222622` | `#E6E8E0` | Inputs, tracks |
| Hairline | `#2C302B` | `#D4D7CC` | |
| Ink | `#F3F5EE` | `#121510` | |
| Ink 2 | `#B6BCB0` | `#3D4439` | |
| Ink 3 | `#878E82` | `#5B6356` | Captions, about 5.3:1 on each ground (to re-measure in the build) |
| Volt (the student's mark) | `#D2F000`, text on it `#0B1000` | Fill `#D2F000`; volt as text `#526700` | Filled bubbles, the primary action, the active tab. Nothing else |
| Correction | Ring `#FF7A66`, text `#FFB8AC` | `#B93225` | Always with a word or glyph |
| Form ink, Accountancy | `#E35D47` | `#B8402C` | Line only (see below) |
| Form ink, Business Studies | `#4C86E0` | `#2A5DB5` | |
| Form ink, Economics | `#3AAE7E` | `#1E7A55` | |
| Form ink, English | `#D9A23A` | `#8F6412` | |
| Form ink, General Test | `#8FA3B8` | `#4F6478` | |

**Form inks are line work only:** the printed grid at 35% opacity, the subject ring, a 3 dp edge on that subject's card, and a 24 dp chip. They are never a fill, a gradient or a background. Each screen shows at most one form ink plus volt.

- **Typography** (OFL, bundled variable files):

| Role | Family | Size / line / weight | Notes |
| --- | --- | --- | --- |
| Moment headline | Archivo | 34/38 sp, 800, width 100, -2.5% | About 18 characters a line at 352 dp, so moment lines are written to two lines of 18 or fewer |
| Hero number | Archivo | 72 to 104 sp, 700, width 112, `tnum` | The fonttools check is a gate (0.12); the fallback is Gabarito ExtraBold |
| Screen title | Archivo | 24/30 sp, 700, -1.5% | |
| Card title | Hanken Grotesk | 17/22 sp, 700 | |
| Body | Hanken Grotesk | 16/24 sp, 400 | Questions and explanations 17/26 |
| Label, button | Hanken Grotesk | 15/20 sp, 600 | |
| Caption | Hanken Grotesk | 13/18 sp, 500 | Smallest size in the app |
| Any figure in running text | Archivo `tnum` or Gabarito | Matches the text size | Never Hanken figures |

- **Mobi: keep the silhouette, upgrade the material.** The same lime folded-kite body, black visor with two white eyes, antenna and black limbs the app already has.
  - **Material:** a soft-touch matte polymer, like a well-made collectible. A single crisp crease runs down the body because Mobi is a folded sheet, and a faint embossed bubble grid sits on its back. The visor is satin black.
  - **Rig:** a code rig (body, visor, eyes, arms, antenna as WebP layers). The eyes are drawn in code, so blinks and looks cost nothing.
  - **Voice:** Mobi speaks one short factual line in onboarding, empty states and celebrations, never in the runner and never about the person.
  - **Why:** the owner's best-liked asset stays recognisable, and the new material reads as premium instead of clip art.

### A.3 Material system

| Material | Where | Recipe |
| --- | --- | --- |
| Liquid lens | The dock's active indicator only | 56 x 44 dp refraction shader (`ImageFilter.shader`) magnifying the icon under it 1.05x with a top-left specular. Only if B6 passes; otherwise a tint plus an edge light. Precompiled offscreen during the first frame's idle time on every launch |
| Frosted glass (live blur) | The dock, bottom sheets | `BackdropFilter` in one `BackdropGroup`, sigma 18 (dock) and 24 (sheets). Tint Raised at 0.70 (Night) or white at 0.78 (Day). A 1 dp edge light from white 16% at the top to 3% at the bottom. **Lite (fake glass) by default until B2 passes** |
| Smoked fake glass | The sheet card where it sits over an art plate (Welcome, plan reveal, milestone) | A pre-blurred quarter-resolution slice of the plate, white 8% plus black 18%, the same 1 dp edge light. No parallax |
| The sheet | Every sheet card | Raised surface, the form-ink grid drawn by one `CustomPainter` into a cached `Picture`, bubbles 18 to 28 dp |
| Solid | Runner, options, explanations, result detail, lists, settings | Raised tokens, no art behind, no texture |
| Art plates | Welcome, plan reveal, the reveal room, milestones, empty states | Lamp-lit still life (A.9), at most one per screen, never on a work screen |

Light: one direction for everything, a warm key from the upper left. Art plates are lit that way and UI edge lights follow it. Depth: one soft shadow under floating chrome (`0 16 32 -16`, black 40%). No glow anywhere.

### A.4 Signature motif

**The bubble, in seven states that always mean the same thing:**

| State | Look | Meaning |
| --- | --- | --- |
| Open | Form-ink ring | Not done yet |
| Pending | Ring with a thin volt arc running | Saving, waiting for the server |
| Filled | Volt fill with the one o'clock sliver | Done, and the server acknowledged it |
| Wrong | Correction ring with a small cross | A mistake, always with a word nearby |
| Rest or skipped | Dotted ring | A chosen rest day, or a skipped onboarding step on its default |
| Checked | Filled, with a fine ink tick inside | Passed a fresh check |
| Holds | Filled, with a second outer ring | Passed a retained check |

Every screen carries one bubble row that holds real state. In onboarding it is the plan being built, in a mock the questions, on Today the week's repairs, and in Repair the life of one mistake (Found, Repaired, Checked, Holds). Four bubbles and a volt sliver make any screenshot recognisable at thumbnail size.

### A.5 Navigation: the sheet dock

- **Destinations (4):**
  - **Today.**
  - **Practice.**
  - **Repair:** Review renamed, because repair is the act and the tab is the queue.
  - **You.**

  Learn folds into Repair (each mistake opens its concept card) and into a Concepts shelf in Practice.
- **Shape:** a floating pill 64 dp tall, inset 16 dp from the sides and 10 dp above the gesture inset, radius 32. Four equal slots, so the outer size never changes.
- **Indicator:** the liquid lens, a 56 x 44 dp bubble behind the active icon and label.
  - On a switch it travels on the Glide spring (340 ms, bounce 0.15). It stretches with velocity up to 1.18x wide and 0.88x tall, then settles.
  - **Scrubbing:** a long-press on the lens (300 ms, `lightImpact`) lets the finger drag it across tabs, with a `selectionClick` at each boundary. A plain horizontal swipe does nothing, so it never fights Android's gesture strip.
- **Icons:** a custom 24 dp set on a 2 dp grid, each built on a bubble.
  - Today: a bubble on a ruled line.
  - Practice: a pencil tip touching a bubble.
  - Repair: a bubble with a tick being drawn.
  - You: Mobi's visor.

  Inactive icons are a 1.75 dp outline in Ink 2; active ones are filled in Ink on the volt lens. Labels are always visible, 12 sp Hanken 600.
- **Press:** the slot scales to 0.96 in 120 ms and the lens brightens 6%.
- **Haptics:** `selectionClick` on a change; nothing on a re-tap (re-tap scrolls to the top).
- **Scroll:** down more than 24 dp scales the dock to 0.94 (transform only); it returns on scroll up or after 600 ms idle. It is never hidden on tab roots, and hidden in the runner, repair sessions and the reveal.
- **Badge:** Repair shows what is due today, capped at 3 ("3" means three or more).
- **TalkBack:** "Repair, tab 3 of 4, 2 due today."
- **Day theme:** the lens becomes an ink-filled pill with volt text and icon.

### A.6 Onboarding: "Fill your sheet"

The **sheet card** sits at the top of steps 2 to 7, 104 dp tall when collapsed. Its row of six bubbles is labelled CUET, Aim, Subjects, Marks, Pace and Check. Each answer fills its bubble with the Fill motion and prints a two-word summary under it. The sheet is the progress indicator, so there is no separate bar. Skip leaves a dotted ring and prints the default it used. The Check bubble stays open until step 9, the visible promise that this ends in a real result.

**1. Cold open (first launch only).**
- Graphite. A ring prints in form-ink grey (path trim, 240 ms), then a volt fill rises inside it (Fill, 320 ms) and stops at the sliver. The wordmark sets beside it (fade and a 4 dp rise, 200 ms). Total 1.0 s, and tap skips.
- Haptic: `lightImpact` as the fill lands.
- Reduced motion: the finished mark fades in over 200 ms.
- It also precaches the Welcome plate and the lens shader.
- Every later launch: the static splash, then Today painted from cache.

**2. Welcome.**
- Layout: the top 55% is plate A-1, a lamp-lit night desk seen from above with a pencil, eraser crumbs, a steel tumbler of chai and a metro token. An empty sheet card (code-drawn, form ink, all rings open) lies across the plate as if it were on the desk, with a baked contact shadow under it.
- Headline: "Every wrong bubble / has a reason."
- Support: "Take a mock. See which chapters cost you marks. Repair them 10 minutes at a time, then prove it on questions you haven't seen."
- Meta line (Ink 3): "About 2 minutes to your plan. Skip anything."
- Inputs: "Build my sheet" (volt) and "I already have an account" (text button).
- A quiet text link for students who would rather start with evidence: "Rather start with 10 questions?" It jumps straight to step 9 with the default plan, borrowing Direction B's order.
- Fast lane from mockmob.in: the headline becomes "Picking up from mockmob.in." The sheet arrives with Aim and Subjects already filled, and the flow skips to the first open bubble.

**3. Which CUET.**
- Headline: "Which CUET are you writing?"
- Inputs (four tiles): "May 2027, I'm in Class 12", "May 2027, taking a gap year", "I'm in Class 11", "Not sure".
- Pays off now: the CUET bubble fills and the countdown prints under the sheet: "About 30 weeks to CUET. May 2027, dates not out yet." It is computed from the device date and switches to the official date when NTA publishes (0.9). For Class 12 a second line prints: "Boards land mid-February to early April. Your plan will go lighter then."
- Class 11: "You're early. That helps." The plan starts lighter (two sessions a week) and Practice stays fully open.
- Pays off later: the plan's length, the board-season taper, the countdown on Today and the widget.

**4. Course and colleges (one evolving screen, three states).**

*State 1, the course.*
- Headline: "Which course, which colleges?"
- Inputs: course chips with real counts: "B.Com (Hons), 55 colleges", "B.Com, 44", "B.A. (Hons) Economics, 40", "B.A. (Hons) Business Economics, 10", "BMS, 9", "BBA (FIA), 2". Then "Another course or university", "Not sure yet", and a quiet "Not commerce?".

*State 2, the ladder.*
- Picking a course unfolds its college ladder in place (morph, 420 ms). It is a vertical ladder sorted by the CSAS 2026 Round 1 minimum allocation score: SRCC 924.3, Hindu 919.9, LSR 912.5, Hansraj 907.5, Kirori Mal 903.7, Ramjas 895.6, Sri Venkateswara 891.5, then "Show all 55".
- The headline changes to: "Which colleges would you say yes to tomorrow?"
- A chip at the top of the ladder reads "Showing UR". Tapping it opens a sheet of categories (UR, OBC-NCL, EWS, SC, ST and the rest), with the line "Stays on this phone." The figures re-roll for the chosen category.

*State 3, the picks and the bar.*
- Tapping a college fills its bubble on the ladder (up to three).
- The bar line prints under the ladder: "SRCC, B.Com (Hons): 924.3 out of 1000 in CSAS 2026, Round 1. That's about 231 of 250 in each of your four papers."
- The rule line: "B.Com (Hons) needs English (or another language), Maths or Accountancy, and two more of DU's listed subjects."
- "Open to any college" is always available.
- Pays off now: the Aim bubble fills with "B.Com (Hons), 3 picks".
- Pays off later: the ladder lives on Today and in You, and after save it seeds the web Compass.

**5. Subjects, and how solid each feels.**
- Headline: "Your subjects. How solid is each, honestly?"
- Inputs: rows pre-ticked from the rule, each with its form-ink ring, its name and a three-part control: Shaky, Okay, Strong. General Test, while it is closed: "Opening soon. We'll tell you the day it does."
- Pays off now: the rows reorder live, weakest first (Smooth spring), and a fit line prints with a volt tick: "English, Accountancy, Business Studies and Economics keeps SRCC, Hindu and Hansraj open."
- Promise line: "Your check will show where your gut was right."
- Pays off later: the check's subject, and the "Your gut versus the check" card in the first recap.

**6. Where the marks go.**
- Headline: "Where do your marks actually go?"
- Inputs (up to two): "I knew it and still got it wrong", "The last 10 questions, no time left", "Accounts numericals take me 4 minutes each", "English passages", "No idea yet". ("General Test reasoning" appears only when General Test is open.)
- Pays off now: the first-move line under the sheet visibly rewrites itself per the worry mapping (0.7). For example, "First: a timed 10-question check in Accountancy, 12 minutes."
- Mobi says one line. For "knew it": "Knew it and still lost it? That's a trap, not a gap. Traps are the quickest marks to win back." For time: "Then we'll train the clock, short and often."
- Pays off later: the check's mode, the first week's mix, and the target on Today.

**7. Pace.**
- Headline: "Pick a pace you can keep."
- Inputs:
  - minutes as three bubbles (10, 20, 30);
  - seven day bubbles, M to S, with four pre-filled;
  - a time window: Before school 6:00 AM, After school 5:00 PM, Evening 8:00 PM, Late 10:00 PM, or Custom.
- Pays off now, live: "Keep this and that's about 108 sessions before CUET." For Class 12 it adds: "Boards weeks count as two." Unchosen days show as dotted bubbles with the caption "Dotted days are rest days."
- Pays off later: the week row on Today, the widget, the reminder time and quiet hours.

**8. The plan.**
- Layout: the sheet card expands to full screen over plate A-2 (container transform, 420 ms) and prints four lines, 90 ms apart, each with its own bubble.
- Headline: "Week one starts with Partnership."
  - The chapter is the first in `cuet_chapter_priorities.json` for the weakest subject.
  - If the student chose "Not sure", the headline falls back to "Week one starts with a check."
- The lines:
  1. "First: a 10-question check in Accountancy, about 12 minutes. It decides what you repair."
  2. "Four evenings a week, 20 minutes, around 8:00 PM."
  3. "Mid-February to early April, the plan drops to two short sessions a week for boards." (Class 12 only. This is the line the student did not tell us.)
  4. "English, Accountancy, Business Studies and Economics keeps all three colleges open."
- Inputs: "Looks right" (volt, a plain tap with no hold ritual) and "Change something", which opens a sheet listing the steps.

**9. Save, then the check.**

*Save.*
- Headline: "Save your sheet. It follows you to mockmob.in."
- Age row first: "Quick one: are you 18 yet?" with "Yes", "Not yet" and "Rather not say", and one line: "Under 18, usage tracking stays off."
- Then "Continue with Google" (volt, Credential Manager), "Use an email code" and "Not now".
- States: "Saving your sheet" with a pending bubble. "Saved" only after acknowledgment, when the sheet's top bubble fills. On failure: "Couldn't save. Your sheet is still on this phone." with "Try again".
- "Not now": the plan stays on the phone, and the check asks for the account at its start, unless guest checks are chosen (question G2).

*The before-check sheet* (a bottom sheet over the plan):
- Title: "10 questions. Accountancy. About 12 minutes."
- Lines: "Answers save as you go. You can pause." The time-pressure worry instead gets: "Timed: 12 minutes. The clock starts when you tap Start."
- Inputs: "Start" (volt) and "Tonight at 8:00 PM".
- Choosing "Tonight" asks for the reminder here, as scheduling (0.6 rule 4), and lands on day-one Today, state 1 (A.7).

*The runner* is described in A.7. The Check bubble on the sheet shows the pending arc while it is answered.

**10. Marked, then the reveal.**
- On submit, "Sending" shows with a pending bubble.
- When the server acknowledges, "Marked" shows and the sealed sheet appears (A.7): "Your check, marked. Hold to open."
- First-check recap cards: "Where the marks went", "First thing to repair", "Your gut versus the check", then "What's recorded".
  - Gut versus check, for example: "You called Accountancy shaky. The check says 6 of 10: shaky on Partnership, solid on Company Accounts."
  - There is no score celebration, because it is a first result. The finish itself gets a quiet acknowledgment: "Check 1 is marked. Here's your map."

**11. Reminders (after value).**
- Headline: "Want a nudge at 8:00 PM?"
- Layout: the student's own notification, previewed on a frosted card: "8:00 PM. Partnership, 12 minutes. 3 of your 10 went here."
- Support: "Only on your days. Never after 11:00 PM."
- Inputs: "Remind me" and "Not now", at equal weight. "Remind me" opens the Android prompt.

**12. Landing.** The sheet card shrinks and flies into Today's hero (container transform). Today paints behind it from the real result (day-one Today, state 2).

Timing targets (to measure, not promise): the countdown in under 15 s, the college bar in under 40 s, the plan in under 2 minutes, the check about 12 minutes, and the reveal within a second of acknowledgment.

### A.7 Home, the work screens, result reveal, celebrations, streaks, return

**Day-one Today, state 1 (check deferred).**
- Top line: "Tuesday, 13 October" and a frosted chip: "~30 weeks to CUET".
- Hero: the sheet card with the plan's bubbles. The Check bubble pulses once on arrival, then stays still.
- Hero line: "Your check is set for 8:00 PM. 10 questions, Accountancy." Inputs: "Start now" (volt) and "Move it".
- Below: "Your ladder", the three picks with their Round 1 figures, and "This week" as seven bubbles, all open, with chosen rest days dotted.
- Nothing else. There are no empty cards and no "nothing here yet" boxes.

**Day-one Today, state 2 (check done).**
- Hero: "Partnership: 3 of your 10 went here. About 12 minutes to repair it." A large volt Start bubble.
- Then "Due today", at most 3 rows (each mistake pattern with its form-ink ring and a short trap name), "This week" (bubbles, with the goal: "0 of 3 repairs"), and "Your ladder".
- Caption, the one Hinglish line: "Aaj ka repair: 12 minutes, Partnership."

**Usual Today.**
- Top line: date plus the countdown chip.
- Hero, in priority order (0.8):
  - a half-finished mock: "Mock 8, Accountancy: 23 of 50 answered" plus its time rule, with "Resume";
  - an unopened result, as the sealed sheet;
  - the next move: "Partnership beat you 4 times in Mock 7. 12 minutes to repair it."
- "Due today" (at most 3), "This week" ("2 of 3 repairs", in bubbles), and "Your ladder" with "Open in Compass" (it opens mockmob.in).

**Practice.**
- Top: one suggested session on a sheet card: "Quick 10: Partnership and Dissolution. About 10 minutes." with "Start".
- "Choose your own": subject chips in form-ink rings, then mode rows that say what you get:
  - "Full mock: 50 questions, 60 minutes."
  - "Quick 10."
  - "One chapter."
  - "Exam-day layout", the NTA-style mode, named by what it is.
- The Concepts shelf: a horizontal row of concept cards opened from earlier mistakes.
- Tapping any mode opens the **confirm sheet**, the only place cost appears: "10 questions, about 10 minutes. 10 credits. You have 90." with "Start".

**Before-mock sheet (full mock).**
- "50 questions. 60 minutes."
- "Answers save as you go. The clock starts when you tap Start."
- A calm aside: "Water, pencil, rough sheet. Ready when you are."
- Inputs: "Start" and "Not now".

**The runner.**
- Solid graphite. No art, no Mobi, no glass except the palette sheet.
- Top bar: the subject, the timer (Archivo `tnum`, never moving) and the save glyph, a bubble that shows the pending arc while answers sync and fills when the server acknowledges. TalkBack reads "Saving" or "Saved".
- The question in Hanken 17/26. Options are A to D bubble keys laid out as an OMR row, so the student literally fills a bubble.
- Bottom bar:
  - "Flag" (the bubble gains a corner notch);
  - "Questions", which opens the palette sheet: 50 bubbles, filled for answered, rings for open, notched for flagged;
  - "Next".
- Leave guard: "Leave the mock? Your answers are saved." The session's time rule is stated as fact, followed by "Keep going" (primary) and "Leave".
- In practice and repair the practice skin applies (spec B13). In a mock there is never correctness.

**Result reveal: "The marking".** The score arrives with the submit response, so the sheet opens at once.
1. A sealed sheet on graphite over plate A-6: the student's sheet, all bubbles filled in volt as they answered, with a seal bubble at its head. Line: "Mock 7, marked. Hold to open." Alternatives: tap "Open", or the TalkBack action "Open without the reveal".
2. **The hold.** The seal's ring fills over 1.0 s, with a `selectionClick` at a third and at two thirds.
3. **The marking.** On release, the marking runs section by section (the Mark wave, 900 ms). Right bubbles keep their volt fill, wrong ones turn to correction rings with a cross, and skipped ones stay hollow. There is one `selectionClick` per section.
4. **The number.** The score rolls in, "183 of 250", then "38 right, 7 wrong, 5 left".
5. **The recap cards** follow (0.8): where the marks went (the sheet grouped by chapter), the first thing to repair, your gut versus the check (first check only), against your last mock ("183, up from 171. Partnership: 2 wrong, down from 5."), and what's recorded with "Repair it now, about 12 minutes".

Variants:
- **Lower than last time:** no hold, no wave; the sheet fades in already marked. The first card reads "Here's the first thing to repair." The compare card is neutral: "Down 12 from Mock 6. Most of it was Dissolution."
- **First mock:** the finish is acknowledged ("Mock 1 is marked. Here's your map.") and the score is not celebrated.
- **Decay:** from the fourth sheet, one tap and a 160 ms fade.

**Repair and the fresh check.**
- A row in Repair opens the mistake's thread page. At the top is the bubble life row: Found, Repaired, Checked, Holds.
- Then the trap in three lines with one worked example, then 3 to 5 targeted questions with feedback, then "Repaired in 9 min 40 s. Fresh check opens tomorrow." (after acknowledgment).
- The next day the fresh check runs: 4 unseen questions. The result reads "Partnership: 3 of 4 on the fresh check (was 0 of 4)." The Checked bubble fills with its tick.
- About a week later the retained check runs, and Holds gains its outer ring.
- "Finish for now" is always in the top bar. It ends on a real card: "Done for tonight. Partnership repaired. Dissolution is next, Thursday."

**Celebrations (server-acknowledged only).**
- **Tick:** a bubble fills, with `selectionClick`.
- **Milestone** (a repair acknowledged, the weekly repair goal met): the row's last bubble fills and the whole row brightens once in a single sweep (300 ms). Mobi gives one line, `successNotification` fires, and a fact line follows: "Repaired in 9 min 40 s. Fresh check opens tomorrow."
- **Big** (a chapter Checked, the first mock finished, a score beating the student's own last):
  - The sheet card rises full screen over plate A-6.
  - The completed row is stamped with the human-fill mark, and one sentence of fact follows.
  - One text button, "Share this", opens the system share sheet with a card that is private by default and shows no marks unless the student turns them on.
  - Never after a lower result.

**Streaks.** The weekly repair goal is chosen. Rest days are dotted, a missed day is just an open ring, and nothing earned is lost.

**Return** (three or more days away). The hero reads "Welcome back. How long have you got?" with 10, 20 and 30 bubbles. Mobi waves once.

**You (identity first).**
- Top: "Your sheet, CUET 2027", the whole season as a sheet with one row per week and one bubble per session, filled where real work happened. It scrolls horizontally through the weeks.
- Beneath, four counts drawn as bubble states: "Found 41, Repaired 18, Checked 9, Holds 4" (sample).
- Then the ladder, then personal bests: fastest clean Quick 10, best mock per subject, and the longest Holds.
- Then one group of settings rows: Plan and reminders, Appearance and feel (Glass: Full, Lite, Off; Reduce motion; Open results directly), Privacy, Account, and Help and About (non-affiliation and sources live here).

**Widget.**
- 2 x 2: graphite, "30 weeks" in Archivo, the line "Partnership, 12 min" and a volt Start bubble. One tap opens the repair.
- 4 x 2: adds the week's bubbles.
- It updates on sync, and its content never changes during quiet hours.

### A.8 Motion and haptic language

| Name | What | Curve and duration |
| --- | --- | --- |
| Print | A ring or grid line drawing (path trim) | `cubic-bezier(0.25, 0.8, 0.25, 1)`, 240 ms |
| Fill | Volt rising inside a bubble, stopping at the sliver | `cubic-bezier(0.2, 0.9, 0.3, 1)`, 320 ms |
| Mark | The marking wave across a sheet, section by section | 60 ms between rows, 900 ms in total |
| Glide | The dock lens, chips becoming bubbles | Spring 340 ms, bounce 0.15, velocity stretch up to 1.18x |
| Smooth | Reorders, cards, sheets | Spring 380 ms, bounce 0.05 |
| Morph | Container transforms (sheet to plan, sheet to Today, row to repair) | `cubic-bezier(0.16, 1, 0.3, 1)`, 420 ms |
| Press | Any tap target | Scale 0.96, 120 ms; release on Smooth |
| Roll | Digits | 40 ms per digit, 480 ms |
| Leave | Anything exiting | `cubic-bezier(0.5, 0, 0.75, 0)`, 180 ms |

- **No idle motion.** Nothing floats or breathes. Things move only when the student does something or the server answers. That is the "weight" the owner asked for, and it is cheaper on the M06.
- **Never moves:** question text, options, the timer, explanation body, a number once landed, and lists while being read.
- **Reduced motion:** Print and Fill appear complete, Mark becomes a 150 ms fade of the finished sheet, Glide jumps, Morph cross-fades in 150 ms, and Roll shows the final value. Every payoff keeps its text.
- **Haptics** (final vocabulary after B12):
  - `selectionClick`: tab, chip, option, palette, reveal sections;
  - `lightImpact`: an onboarding bubble filling, the lens long-press;
  - `mediumImpact`: the hold completing;
  - `successNotification`: an acknowledged submission, repair or milestone;
  - `warningNotification`: leaving a timed mock.

  None on wrong answers.

### A.9 Imagery plan

**Image bible for A: "the desk at night, still life".** Real objects from a Commerce student's desk, photographed as still life:
- **Camera:** overhead or a low three-quarter, 50 mm at f/4, shallow but not dreamy depth of field.
- **Light:** one warm practical desk-lamp key from the upper left, falling off to near-black graphite within a third of the frame, with a faint cool fill from a window on the right.
- **Texture:** natural surfaces (worn laminate, paper, steel, rubber) and fine 35 mm grain.
- **Colour:** no volt in any image. Volt belongs to the student's marks in the UI, so the art is always neutral-warm and the UI's marks are the only bright thing.
- **Grading:** a fixed curve that crushes blacks to Graphite and holds highlights warm-neutral.
- **Never:** text, logos, faces, calculators, CGI gloss.

**Better as code:** every sheet, bubble, grid, ring, tick, the wordmark animation, number rolls, the dock, the lens, the icons, the share card layout and confetti-free stamps.

**A-1. Welcome plate, the night desk.** Output: 1024 x 1536, cropped to the top 55%, about 110 KB WebP.
> Overhead photograph of a real study desk in a small Delhi bedroom at night. Worn pale-grey laminate desk surface with faint scratches. Arranged loosely around an empty clear rectangle in the centre of the frame (keep the middle 60 percent of the width and the middle third of the height completely empty desk surface): an HB pencil with a chewed end and a few pencil shavings at the upper left, a soft white eraser with grey crumbs beside it, a steel tumbler of milky chai with a thin skin on top at the right edge, a round blue plastic metro token near the bottom edge, and the corner of a ruled rough-work sheet with faint graphite scribbles (no legible writing) slipping in from the left. Lit only by a warm desk lamp out of frame at the upper left; light pools on the objects and falls off to deep charcoal shadow toward the bottom and right. Faint cool window light from the right. 50 mm lens, f/4, natural colour, fine 35 mm film grain, documentary still life, quiet and real. Avoid: any text, letters or numbers, logos, people, hands, calculators, phones, laptops, glossy CGI look, bokeh balls, lens flare, green or lime tones.

Post: grade to Graphite; add a soft contact-shadow zone where the sheet card sits (baked in a second layer, 20% black, 24 dp blur).

**A-2. Plan plate, the start of a season.** Output: 1024 x 1536, about 90 KB.
> Overhead photograph of the same kind of night study desk, slightly tidier: a desk calendar page lying flat at the upper right with one date circled in pencil (the calendar's printed numbers must be blank or illegible, abstract grey marks only), a steel geometry box half open showing a pencil and an eraser, and a small stack of three plain exercise notebooks with blank brown paper covers at the lower left. The centre of the frame is empty desk surface for an overlaid card. Warm desk lamp from the upper left, deep falloff to charcoal, faint cool window light from the right. 50 mm, f/4, fine grain, natural colour, calm and orderly mood. Avoid: legible text or numbers, logos, brand names on any object, people, hands, calculators, glossy CGI.

**A-3. Subject objects, five cut-outs for Practice, subject pages and Repair headers.** Output: 1024 x 1024, transparent background, about 30 to 45 KB each at 480 px.

Shared prompt frame:
> Studio still-life photograph of a single real object on a transparent background, shot from a low three-quarter angle with a 70 mm lens at f/5.6, lit by one warm soft key light from the upper left and a faint cool rim from the right, natural material textures, realistic small imperfections, crisp edges suitable for cut-out, no cast shadow on the ground (shadow added later), fine grain. Object: [OBJECT]. Avoid: any legible text, letters, numbers or logos, brand marks, hands, people, glossy CGI or plastic sheen, saturated colours, green or lime tones.

[OBJECT] per subject:
- **Accountancy:** "a worn carbon-copy receipt book held closed with a red rubber band, the top page half-filled with ruled columns of faint blank lines, a short pencil stub lying across it, slightly dog-eared corners."
- **Business Studies:** "a brass-handled rubber stamp standing upright beside an open tin ink pad with dark violet ink, and a small fanned stack of blank cream visiting cards."
- **Economics:** "a single red onion sitting on the pan of a small steel kitchen scale whose dial needle is caught mid-swing, the dial face blank with only tick marks."
- **English:** "a folded broadsheet newspaper open at the editorial page, its columns rendered as abstract grey bars with no letters, a yellow highlighter lying diagonally across it with its cap off."
- **General Test:** "a small desk calendar page with one date circled in pencil (printed numbers blurred and illegible) leaning against a round analogue table clock showing about 3:15 with plain tick marks and no numerals."

Post: grade per A's curve; generate two takes per object and keep the one with the cleanest silhouette; check every take at 100% for stray letters.

**A-4. Mobi, six poses (wave, point, think, cheer, rest, hold pencil).** Output: 1024 x 1024, transparent, layered later into the code rig, about 30 KB each at 512 px.
> Product photograph of a small collectible figure, about 8 cm tall, on a transparent background: a friendly robot whose body is a lime-yellow folded paper kite shape (a diamond folded down its vertical centre, with one crisp crease line), made of soft-touch matte polymer with a very faint embossed grid of tiny circles on its back. A satin black visor band crosses the upper body with two white rounded rectangular eyes. Thin black antenna with a small lime ball tip. Short black arms and legs with rounded black boots. Pose: [waving with the right hand raised, weight on one foot]. Warm soft key light from the upper left, faint cool rim from the right, realistic material, crisp edges, no ground shadow. Avoid: glossy plastic, inflatable look, glass, chrome, text, logos, extra limbs, a mouth.

Production note: gpt-image will not hold the exact character across six poses. Use it to explore the material on the existing `greeting.webp` silhouette. Then build one Blender model from the current Mobi (about a day of a 3D artist's time, or a Codex-assisted build) and render all poses from it. This is question G4.

**A-5. Empty states (nothing due, offline, all caught up this week).** Output: 1536 x 1024, about 40 KB each.
> Overhead night-desk still life, warm lamp from the upper left, charcoal falloff: [nothing due: the steel tumbler of chai now empty with a dried ring inside, a closed blank notebook, a pencil laid neatly parallel to it] [offline: a wired earphone cable coiled loosely beside a phone lying face down, its back plain and unbranded] [all caught up: a pencil sharpened to a fine point standing in a small steel cup next to a neat pile of eraser crumbs swept together]. Left 40 percent of the frame is empty dark desk for a line of text. 50 mm, f/4, fine grain. Avoid: text, logos, brand marks, people, hands, calculators, glossy CGI, lime or green tones.

**A-6. The reveal room and milestone ground.** Output: 1024 x 1536, about 70 KB.
> Overhead photograph of an almost empty dark study desk at night: a single pool of warm desk-lamp light in the upper-middle of the frame on worn grey laminate, everything else falling into deep charcoal. At the very edge of the light, a pencil and a few eraser crumbs. The lit area is empty, for a card placed on it later. 50 mm, f/4, fine grain, quiet and expectant mood. Avoid: text, logos, objects in the lit centre, people, glow effects, lens flare, coloured light.

### A.10 Concept screens (prototype briefs and art plates)

All four are built in HTML at 384 x 853 CSS px with Archivo, Hanken Grotesk and the A tokens, exported at 3x, and shown on the M06. File names: `A-01-welcome_concept_sample-data.png` and so on. Nothing is captioned inside the image.

1. **Welcome.** Plate A-1 fills the top 55%. The empty sheet card lies across the plate at -2 degrees: six open form-ink rings labelled CUET, Aim, Subjects, Marks, Pace and Check, with the wordmark at its head. Then:
   - the headline in Archivo 34/38, two lines: "Every wrong bubble / has a reason.";
   - the support line in Hanken 16/24, Ink 2;
   - the meta line in Ink 3, "About 2 minutes to your plan. Skip anything.";
   - a full-width volt pill, "Build my sheet";
   - a text button, "I already have an account";
   - a quiet link, "Rather start with 10 questions?".

   No footer.
2. **Course and colleges, state 3.**
   - The sheet card at the top, with CUET filled ("Class 12") and Aim filled ("B.Com (Hons), 3 picks").
   - The headline: "Which colleges would you say yes to tomorrow?"
   - The "Showing UR" chip.
   - The ladder of seven colleges with figures in Archivo `tnum`, right-aligned. SRCC, Hindu and Hansraj have filled volt bubbles; the rest have open rings.
   - Beneath: the bar line ("SRCC, B.Com (Hons): 924.3 out of 1000 in CSAS 2026, Round 1. That's about 231 of 250 in each of your four papers.") and the rule line.
   - "Continue" in volt.
3. **Today, state 2, with the dock.**
   - Date line and the "~30 weeks to CUET" chip.
   - Hero sheet card with an Accountancy form-ink edge: "Partnership: 3 of your 10 went here." and "About 12 minutes to repair it.", with a 64 dp volt Start bubble.
   - "Due today" with two rows ("Partnership, interest on capital trap", "Company Accounts, share forfeiture").
   - "This week" with seven bubbles (three open evenings, four dotted rest days) and "0 of 3 repairs".
   - "Your ladder."
   - The caption "Aaj ka repair: 12 minutes, Partnership."
   - The frosted dock over the scrolled list: Today active in the volt lens; Practice; Repair with "2"; You.
4. **The reveal, mid-marking.**
   - Plate A-6.
   - The student's sheet in the lamp pool, with the top three sections marked (volt fills, two correction rings with crosses, one hollow) and the bottom two still unmarked volt.
   - The score "183" rolling in Archivo 104 with "of 250" at 55% size.
   - The line "38 right, 7 wrong, 5 left".
   - The top of the first recap card rising from the bottom: "Where the marks went".

   No dock.

### A.11 Performance plan and biggest risk

- **Live blur:** the dock and at most one sheet, in one `BackdropGroup`, and only after B2 passes (Lite before that). The lens is optional (B6) and precompiled at launch.
- **Pre-rendered:** plates (decoded at display width), subject cut-outs (480 px), Mobi layers (512 px).
- **Code-drawn:** sheets and grids are one `CustomPainter` per sheet, cached as a `Picture`, so only the bubbles being filled repaint (one clip path at a time).
- **Animated budget:** no idle animation anywhere. The Mark wave repaints one section at a time.
- **Frame budget:** 11.1 ms at 90 Hz; raster p90 at or under 8 ms on Today while scrolling under the dock, and at or under 6 ms in the runner.
- **Biggest risk: it reads as a form.** A sheet and a grid can feel bureaucratic, not "crazy" in the high.live sense.
  - Mitigation: the moment layer (the lamp-lit plates, the liquid lens, the hold and the marking wave, the human-fill mark, Mobi's upgrade) carries the energy. Work screens stay quiet on purpose.
  - Test it on the M06 with the owner before building beyond onboarding.
- **Second risk:** still life could look like stock photography if the objects drift generic. The object list is fixed to CUET-true items, and each plate is reviewed at 100% for stray text.

---

## Direction B: "Cold Read"

### B.1 The idea

**Core idea: evidence first.** Students are asked to describe themselves everywhere: coaching forms, apps, relatives. MockMob asks them for nothing until it has seen them work. The first real act is a marked 10-question read. Every plan line, goal and home-screen sentence afterwards quotes that evidence, and every claim the app makes can be tapped open to the exact questions behind it.

**What happens differently:**
- **The order is reversed.** One choice (the paper), then the check, the reveal, and only then the goal questions, which are now framed by a real result.
- **There is no confidence question.** Evidence replaces self-report.
- **Navigation is a desk bar** whose centre is a Start control that opens into the core loop.

**The world:** the student's own desk in the evening, shot cinematically: warm practical lamp light, real objects, deep shadow. It is used only on moment screens. Everything the student works on sits on calm, solid surfaces. The desk changes with the real calendar (season plates), never with performance.

**Mood:** cinematic, quiet, serious and cool. Respect for a 17-year-old who wants the truth.

**What it looks like in one screenshot:** a full-bleed evening desk in warm lamp light with one sentence of evidence set large over the shadowed part ("Partnership beat you 4 times in Mock 7."), a small frosted tag under it that says where that came from, a volt Start pill, and a frosted desk bar at the foot.

**References, taken as ideas only:**
- From Revolut: the morph grammar, used where the Start control becomes the Start sheet.
- From Fampay: open on the next move, environment-lit ground.
- From HIGH: the two-layer rule.
- From Speak and Brilliant (onboarding research): learn by doing before being asked anything.

How it avoids the references:
- **Not Revolut's home:** no avatar, search and circle row, no circular action row, no peeking pager.
- **Not HIGH's console:** the ground is warm charcoal rather than cold black, headlines are not condensed caps, and lime appears only on the Start pill and the student's marks.
- **Not Fampay:** the warmth lives only inside the photographs. The UI never uses amber.

### B.2 Brand

- **Wordmark:** `mockmob`, lowercase, Mona Sans Bold at width 100, tracking -2%, with nothing struck through or drawn across it. Its signature is the space between "mock" and "mob", where a small diamond (the mark) sits at x-height in place of a letter space in the lockup.
- **Mark: "the crease".** A diamond, the outline of Mobi's folded body, with one vertical crease. The left half is volt and the right half is a deeper volt (the folded side). It is the folded answer sheet of the reveal and Mobi at once, so it is MockMob's own object rather than a generic document icon.
  - App icon: the mark on Warm charcoal.
  - Monochrome: the diamond outline and the crease.
- **Palette.** Night is the default; Daylight is a composed option.

| Role | Night (default) | Daylight | Notes |
| --- | --- | --- | --- |
| Ground (Warm charcoal) | `#141311` | `#F1EFEA` | A degree warmer than A, to sit with lamp-lit photographs |
| Raised | `#1C1B18` | `#FFFFFF` | |
| Raised 2 | `#262421` | `#E5E2DA` | |
| Hairline | `#302E2A` | `#D4D0C6` | |
| Ink | `#F4F1EA` | `#14120F` | |
| Ink 2 | `#BDB7AC` | `#423E37` | |
| Ink 3 | `#8E887D` | `#625D54` | About 5.2:1 on each ground (re-measure in build) |
| Volt | `#D2F000`, text on it `#0B1000` | Fill `#D2F000`; volt as text `#526700` | Start, the student's marks, the active tile's top edge |
| Wrong | `#2A1614` surface, `#7D3128` border, `#FFC9C2` text (the web's own trio) | `#FBE9E7` surface, `#B93225` text | |

There are no subject hues. Each subject is identified by its photographed object and its name, which keeps the ground calm and the photographs in charge.

- **Typography** (OFL, bundled; Mona Sans `tnum` is a gate):

| Role | Family | Size / line / weight | Notes |
| --- | --- | --- | --- |
| Evidence line (the big sentence over art) | Mona Sans | 30/34 sp, 700, width 100, -2% | Sentence case, two lines at most, about 22 characters a line |
| Hero number | Mona Sans | 88 to 112 sp, 800, width 87, `tnum` | Semi-condensed, not compressed caps |
| Screen title | Mona Sans | 24/30 sp, 700 | |
| Card title | Hanken Grotesk | 17/22 sp, 700 | |
| Body | Hanken Grotesk | 16/24 sp, 400 | Questions 17/26 |
| Label, button | Hanken Grotesk | 15/20 sp, 600 | |
| Caption, evidence tags | Hanken Grotesk | 13/18 sp, 500 | Figures inside tags use Gabarito `tnum` |

- **Mobi: present, but small and physical.**
  - **In the photographs** Mobi is a real painted resin figure about 7 cm tall, standing on the desk: lime enamel body, satin black visor, white eyes. Students meet Mobi as an object they would own.
  - **In the UI** Mobi is the code rig at 48 to 64 dp, only in empty states, the return screen and the first reveal's last card.
  - It never speaks in the work layer, and never in a mock or during the reveal.
  - Why: this direction is about evidence, so the mascot steps back, but the character survives intact.

### B.3 Material system

| Material | Where | Recipe |
| --- | --- | --- |
| Frosted acrylic (live blur) | The desk bar, bottom sheets | `BackdropFilter` grouped, sigma 20 (bar) and 26 (sheets); tint Raised at 0.72 (Night) or white at 0.80 (Daylight); a 1 dp polished top edge (white 18%), no glow. **Lite by default until B2 passes** |
| Fake acrylic | Evidence tags and the Start pill when they sit over a plate | A pre-blurred quarter-resolution slice of the same plate, tint black 30%; no parallax on any screen that has fake glass |
| Plates | Welcome, Desk hero (top 40%), the reveal room, the return screen, big milestones | Full-bleed photography (B.9) with a baked scrim and a baked progressive blur in the lower third so text sits on shadow, never on detail |
| Solid | Runner, options, explanations, Mistakes, Practice, You, settings | Raised tokens; no art behind, no texture |
| Sheet | The folded answer sheet in the reveal | Drawn in code (spec A1): three panels, one transform each, no `saveLayer` |

Light: there is none in the UI, only in the photographs, and they are always lit by a practical lamp in frame or just outside it. The B draft's volt glow, light shards and weekly room brightness are all gone.

### B.4 Signature motif

**"Show me" tags.** Under every claim the app makes there is a small frosted tag naming its source: "From Check 1: Q2, Q5, Q9" or "Mock 7: Q12, Q19, Q33, Q41". Tapping it opens those exact questions in a sheet, with the student's answer and the right one.

The tags appear wherever the app asserts something: the plan, the Desk hero, recap cards, Mistakes rows and even notifications (a long-press on the notification opens the questions). It is integrity as an interaction: the app never says something it cannot show. With the evening-desk photograph and the big evidence sentence, any screenshot reads as B.

### B.5 Navigation: the desk bar

- **Destinations:**
  - **Desk** (home).
  - **Mistakes** (Review renamed to the student's own word).
  - **You.**
  - **Start**, in the centre: not a destination but the way into the core loop. Practice lives inside it as "Choose your own".

  Learn folds into Mistakes (concepts open from the mistake) and into a Concepts shelf in "Choose your own".
- **Shape:** one floating frosted bar, 64 dp tall, inset 16 dp, 10 dp above the gesture inset, radius 24. Four slots: Desk, Start (a wider slot, 1.4x), Mistakes and You. The outer size never changes.
- **Start:** a volt pill inside the bar, labelled "Start" with a small upward chevron.
  - Opening it: a tap, or a drag up from the pill. Either morphs the pill into the Start sheet (Morph, 400 ms), which grows from the pill's own shape, and the drag follows the finger.
  - Contents of the sheet:
    - "Resume Mock 8, 23 of 50" (only when one exists);
    - "Suggested: Quick 10, Partnership and Dissolution";
    - "Repair next: Partnership, 12 min";
    - "Full mock";
    - "Choose your own".
  - Each tile shows a "Show me" tag where a reason exists.
- **Indicator:** for Desk, Mistakes and You, a frosted tile behind the active icon with a 1.5 dp volt top edge. It slides on Settle (360 ms, bounce 0.06) with no stretch, because this direction glides and lands. In Daylight the tile is ink-filled with volt text and icon (3:1).
- **Icons:** a custom 24 dp set with flat terminals.
  - Desk: a lamp head over a line.
  - Mistakes: a folded corner with a cross.
  - You: Mobi's diamond.

  Labels are always visible, 12 sp Hanken 600.
- **Haptics:** `selectionClick` on a tab change; `lightImpact` when Start opens; nothing on a re-tap.
- **Scroll:** the bar sinks 8 dp and scales to 0.95 on scroll down, and returns on scroll up or idle. It is hidden in the runner, repair sessions and the reveal.
- **Badge:** Mistakes shows due today, capped at 3.
- **TalkBack:** "Start, button, opens your next sessions"; "Mistakes, tab 2 of 3, 2 due today".

### B.6 Onboarding: "Cold read"

There is no sheet card building up and no questionnaire before the work. A slim four-part hairline at the top shows real phases: Check, Result, Aim and Plan.

**1. Cold open (first launch only).**
- Black for 150 ms. The lamp in the Welcome plate "switches on": the plate fades from 0 to 1 over 450 ms with a slight warm exposure lift, and the wordmark sets in the shadowed lower third. The haptic is a single `lightImpact`, the switch.
- 0.9 s in total; tap skips; reduced motion fades in over 200 ms.
- Later launches: the static splash, then the Desk painted from cache.

**2. Welcome.**
- Layout: plate B-1 full-bleed: a low three-quarter view across an evening desk with a rough sheet, a pencil, a steel tumbler and the small resin Mobi at the edge of the lamp's pool. The camera pushes in 3% over 900 ms once, only after the buttons are already usable.
- Headline (evidence-line style): "Your score is / the symptom."
- Support: "Let's find the cause. Ten real CUET questions, marked properly, then a plan built from what actually happened."
- Meta line: "About 12 minutes. Pause any time."
- Inputs: "Start with 10 questions" (volt), "Set my goal first" (secondary; it runs the Aim steps first, then the check), and "I already have an account".
- Fast lane from mockmob.in: the headline becomes "Picking up from mockmob.in." The paper is pre-chosen, and any website sample answers appear as "Your 5 from the website" on the first results card (shown as what they are, not as a score).

**3. Which paper first.**
- Headline: "Which paper first?"
- Inputs: four large tiles, each with its subject object photographed (B.9 B-3): Accountancy, Business Studies, Economics and English, plus "Another subject", which shows what is open and offers "Tell me when it opens".
- Pays off now: the tile morphs into the before-check sheet, titled with that paper.
- Pays off later: it is the first evidence, and the first repair's subject.

**4. Getting it marked** (one of two variants; question G2).
- **(a) Guest check, recommended if the API change is approved.** No screen at all. The check runs on an anonymous device session the server can score, and it is merged once into the account at sign-in.
- **(b) Account first.**
  - Headline: "We mark it properly, so it needs a home."
  - Age row first: "Quick one: are you 18 yet?" with "Yes", "Not yet", "Rather not say", and "Under 18, usage tracking stays off."
  - Then "Continue with Google", "Use an email code" and "Not now (look around first)".

**5. Before the check** (bottom sheet).
- Title: "10 questions. Accountancy. About 12 minutes."
- Lines: "Answers save as you go. You can pause."
- A switch: "Time me (12 minutes)". It is off by default, because the first read should measure what the student knows, not panic.
- Inputs: "Start" (volt) and "Tonight at 8:00 PM". "Tonight" asks for the reminder here, as scheduling, then lands on Desk, state 1.

**6. The check.** The runner (B.7). The hairline's first segment fills as questions are answered.

**7. Marked, and the fold.**
- On submit, "Sending" shows; on acknowledgment, "Marked".
- The folded sheet arrives in the reveal room (plate B-4) with the line "Check 1, marked. Swipe up to open." The fold is described in B.7.
- The number: "6 of 10" in Mona Sans 104, then "27 of 50 marks" and "6 right, 3 wrong, 1 left".
- Recap cards, each with a "Show me" tag:
  1. "Where the marks went": Partnership 1 of 4, Company Accounts 3 of 3, Financial Statements 2 of 3 (sample).
  2. "First thing to repair": "Partnership: 3 of your 4 wrong answers were here. The same trap twice: interest on capital."
  3. "Your fastest right answer: 41 seconds on Q3." This is speed as proof, a true fact about the student.
  4. "What's recorded": "Check 1 is saved to your account." with "Set my goal" (volt).
- No score celebration on a first result.

**8. Now aim it (the goal, asked after the evidence).**

Four quick steps, each skippable. The result chip stays pinned at the top ("Check 1: 6 of 10"), so the student aims with their evidence in view.
- **Which CUET:** "Which CUET are you writing?" with the same four options as A. The countdown prints as in A, with the boards line for Class 12.
- **Course and colleges:** the same evolving ladder screen as A, with the same real figures, scale line, category chip and rule line. The headline reads "Now, the target. Which colleges would you say yes to tomorrow?"
  - The only Hinglish caption: "For the next time someone asks 'DU mil jayega?'"
  - Nothing compares the 6 of 10 to the ladder. A short check is never projected (0.3 rule 3).
- **Subjects:** "Your four papers." Rows are pre-ticked from the rule, with the fit line ("keeps SRCC, Hindu and Hansraj open"). There is no Shaky, Okay, Strong control: in this direction, checks will tell us.
- **Pace:** the same controls as A, with the live session count.

**9. The plan.**
- Headline: "Week one, from your check."
- Lines, each with a "Show me" tag where it rests on evidence:
  1. "Repair Partnership first, 12 minutes." (Check 1: Q2, Q5, Q9)
  2. "Fresh check on Partnership on Thursday: 4 questions you haven't seen."
  3. "Economics check on Saturday, so the plan sees a second paper."
  4. "Four evenings a week, 20 minutes, around 8:00 PM."
  5. "Boards: two short sessions a week, mid-February to early April." (Class 12 only)
- Inputs: "Looks right" and "Change something".

**10. Save** (if variant (a) ran the check as a guest).
- Headline: "Save your check. It follows you to mockmob.in."
- The age row, then Google, email and "Not now". The same pending, acknowledged and failure states as A.

**11. Reminders.**
- Headline: "Want a nudge at 8:00 PM?"
- Preview: "8:00 PM. Partnership, 12 minutes. Same trap twice in your check."
- Support: "Only on your days. Never after 11:00 PM."
- Inputs: "Remind me" and "Not now", at equal weight.

**12. Landing.** The plan card morphs into the Desk hero. The Desk plate fades up behind it at the current season.

Timing targets: the first question on screen in under 20 s; the first marked result at about 12 minutes; the plan about 1 minute after that.

### B.7 Home, the work screens, result reveal, celebrations, streaks, return

**The Desk, usual state.**
- The hero, the top 40%, is the **season plate** (B-2) for the current calendar window:
  - October to November: an evening desk with the window open;
  - December to January: winter, with a folded shawl and a steaming steel tumbler;
  - February to April: boards, with a thick stack of revision papers held by a binder clip;
  - May: exam month, an early-summer evening with a clear exam pouch packed and ready.

  The plates change on dates, never on performance, and they never dim.
- Over the plate's shadowed lower part:
  - the evidence line: "Partnership beat you 4 times in Mock 7.";
  - "12 minutes to repair it.";
  - a volt "Start" pill;
  - the tag "Mock 7: Q12, Q19, Q33, Q41".
- Top right, small on the plate: "30 weeks to CUET".
- Below the plate, on solid ground:
  - "Due today" (at most 3 rows);
  - "This week": "2 of 3 repairs", three short segments;
  - "Last check: Accountancy, 6 of 10, Tuesday", with its tag;
  - "Your ladder", with "Open in Compass".
- A half-finished mock or an unopened result takes the evidence-line position: "Mock 8 is half done: 23 of 50." / "Mock 7, marked. Swipe to open."
- The one Hinglish caption, under the week: "Bas 12 minutes. Partnership."

**Desk, day one.**
- State 1, check deferred: the plate, plus "Your check is set for 8:00 PM. 10 questions, Accountancy." with "Start now" and "Move it". Below: "Set your target" if Aim was skipped, otherwise the ladder. Nothing else.
- State 2, check done: the plate, plus "Partnership: 3 of your 4 wrong answers. 12 minutes to repair it." with its tag, then "Due today" (two rows) and the empty week ("0 of 3 repairs").

**Mistakes.**
- Grouped by pattern, due today first.
- Each row carries the subject object's small cut-out, the trap name ("Interest on capital"), the source ("Mock 7, Q19 and 2 more") and a state chip with a glyph: Found, Repaired, Checked or Holds.
- A row opens the repair page.

**Practice ("Choose your own").**
- Subject tiles with their photographed objects, then modes with what you get: "Full mock: 50 questions, 60 minutes", "Quick 10", "One chapter", "Exam-day layout".
- The Concepts shelf.
- The confirm sheet carries the cost: "10 questions, about 10 minutes. 10 credits. You have 90."

**Before-mock sheet.** "50 questions. 60 minutes." "Answers save as you go. The clock starts when you tap Start." Aside: "Phone on silent. Rough sheet ready." Then "Start" and "Not now".

**The runner.**
- Warm charcoal, solid. Top bar: the paper, the timer (Mona Sans `tnum` 20 sp) and the save glyph, a small diamond outline that fills volt when the server acknowledges.
- Options are full-width solid rows with the letter in a square. A selected option gains a 2 dp volt left edge (no fills, no glass).
- Bottom: "Flag", "Questions" (the palette sheet: a 50-cell grid, answered cells filled, flagged ones with a corner fold) and "Next".
- Leave guard: "Leave the mock? Your answers are saved." The session's time rule is stated as fact, followed by "Keep going" and "Leave".

**Result reveal: "The fold"** (from spec A1).
1. The reveal room (plate B-4): a dark desk with one pool of lamp light. In it sits the sheet folded in thirds, drawn in code, sealed with a small volt diamond.
2. Line: "Mock 7, marked. Swipe up to open." Alternatives: tap "Open", or the TalkBack action "Open without the reveal".
3. **The unfold.** The drag follows the finger 1:1, and the panels unfold in perspective (one transform per panel, 120 ms stagger) with `selectionClick` at 25, 50 and 75%. Released under 60%, it springs back.
4. **The number.** "183" lands at 112 sp with "of 250" at 55% beside it, then "38 right, 7 wrong, 5 left". The 50-cell grid fills in by section.
5. **The cards**, each with its "Show me" tag: where the marks went, first thing to repair, against your last mock ("183, up from 171. Partnership: 2 wrong, down from 5."), and what's recorded with "Repair it now, about 12 minutes".

Variants:
- **Lower result:** no unfold; the sheet arrives open with a 200 ms fade. "Here's the first thing to repair." The compare card is neutral.
- **First mock:** "Mock 1 is marked. Here's your map." No score celebration.
- **Decay** from the fourth sheet: one tap and a 160 ms unfold.

**Repair and the fresh check.**
- The page header is the evidence line ("Interest on capital: 4 wrong in Mock 7") with its tag.
- Then the trap in three lines and a worked example, 3 to 5 targeted questions, and "Repaired in 9 min 40 s. Fresh check opens tomorrow."
- The fresh check: "Partnership: 3 of 4 on the fresh check (was 0 of 4)." becomes Checked. The retained check about a week later becomes Holds.
- "Finish for now" is in the top bar. It ends with: "Done for tonight. Partnership repaired. Dissolution is next, Thursday."

**Celebrations (server-acknowledged only).**
- **Small:** the state chip changes (Found to Repaired) with a 220 ms cross-fade, plus `selectionClick`.
- **Milestone:** the evidence line on the Desk rewrites itself in place with a line wipe ("Partnership: repaired in 9 min 40 s."), plus `successNotification`. There are no shards and no glow.
- **Big** (a chapter Holds, the first mock finished, a score beating the student's own last):
  - The current season plate full screen, with one line in Mona Sans 40 ("Partnership holds.") and one fact sentence with its tag.
  - "Share this" opens the system share sheet with a private-by-default card that shows no marks unless the student chooses.

**Streaks.** A weekly repair goal, chosen, with rest days; a missed day takes nothing. The season plates are the long arc, and they are about the calendar, so they cannot be lost.

**Return** (three or more days). The current plate, plus "Welcome back. How long have you got tonight?" with 10, 20 and 30 minute pills. The small code-rig Mobi stands at the plate's edge.

**You (identity first).**
- "Your evidence": a vertical timeline of every check and mock as small folded-sheet tiles with real numbers ("Check 1, Accountancy, 6 of 10", "Mock 7, 183 of 250"), each opening its recap.
- Then the counts (Found, Repaired, Checked, Holds), the ladder and personal bests.
- Then settings, grouped as in A.

**Widget.**
- 2 x 2: a crop of the current season plate darkened under the text, "Partnership, 12 min" and a volt Start.
- 4 x 2: adds "30 weeks to CUET" and the week's three segments.

### B.8 Motion and haptic language

| Name | What | Curve and duration |
| --- | --- | --- |
| Switch | The cold-open lamp | Fade 0 to 1, 450 ms, `cubic-bezier(0.3, 0, 0.2, 1)` |
| Push | A one-time camera push on the Welcome plate | Scale 1.0 to 1.03, 900 ms, `cubic-bezier(0.2, 0.7, 0.1, 1)`, after the buttons are live |
| Morph | Start pill to sheet, plan card to Desk hero, row to repair | `cubic-bezier(0.2, 0.9, 0.2, 1)`, 400 ms; it follows the finger when dragged |
| Unfold | Sheet panels | Follows the finger; on release, a spring of 420 ms with bounce 0 |
| Settle | Tiles, cards, sheets | Spring 360 ms, bounce at most 0.06 |
| Wipe | A line of text revealed or rewritten | `ClipRect` width per line, 260 ms, 70 ms stagger (no `ShaderMask`) |
| Roll | Digits | 40 ms per digit, 480 ms |
| Leave | Anything exiting | `cubic-bezier(0.5, 0, 0.75, 0)`, 180 ms |

- **Weight:** nothing bounces. Things glide, land and stay. There is no idle motion.
- **Never moves:** question text, options, the timer, explanation body, numbers once landed, list rows being read. The bar is absent in the runner.
- **Reduced motion:** Switch, Push and Unfold become fades; Wipe shows the text at once; Roll shows the final value.
- **Haptics:**
  - `selectionClick`: tab, option, unfold thresholds, tags;
  - `lightImpact`: Start opening, the cold-open switch;
  - `successNotification`: acknowledged submission, repair, milestone;
  - `warningNotification`: leaving a timed mock.

  None on wrong answers; final after B12.

### B.9 Imagery plan

**Image bible for B: "the evening desk, cinematic".** Generated photography of a real Indian student's desk:
- **Camera:** eye level or a low three-quarter angle across the desk (A shoots from above, so the two never look alike), 35 mm at f/2.8.
- **Light:** a practical lamp in frame or just outside it; deep, soft-edged shadow; a cool window as the only fill.
- **Grade:** tungsten corrected toward neutral-warm (never orange), blacks graded to Warm charcoal, fine 35 mm grain, no bloom.
- **People:** none. No faces and no hands, unless real-student photography is chosen (question G7).
- **Text:** none, anywhere. A sheet in a photograph shows only a plain grid of empty circles. If the model prints letters on it, the sheet is masked out and the code-drawn sheet is composited in post.

**Better as code:** the folded sheet and its panels, the grid, the diamond mark and wordmark, tags, the desk bar and icons, scrims, line wipes and number rolls.

**B-1. Welcome plate.** Output: 1024 x 1536, about 130 KB.
> Cinematic photograph, eye-level three-quarter view across a real student's study desk in a small Delhi bedroom at about 9 PM. A warm desk lamp at the left edge of the frame casts a soft pool of light across the near half of the desk. In the light: a single printed practice sheet with a plain grid of small empty circles and no printed letters or numbers, a few circles shaded in with pencil; an HB pencil; a soft white eraser with grey crumbs; a steel tumbler of chai with a thin skin. At the far edge of the light pool stands a small painted resin figure about 7 cm tall: a lime-yellow folded-kite-shaped robot with a satin black visor and two white eyes, thin antenna, black limbs. Behind, a window with soft out-of-focus night, no visible city lights. The upper 45 percent of the frame falls into deep warm-charcoal shadow, empty for text. 35 mm lens, f/2.8, shallow depth of field, fine 35 mm grain, natural colour, quiet and serious mood. Avoid: legible text, letters or numbers anywhere, logos, people, hands, calculators, laptops, phones lit up, bokeh balls, lens flare, neon, glossy CGI look, orange colour cast.

**B-2. Season plates, four** (shared frame plus four inserts). Output: 1024 x 1536, cropped to the top 40% for the Desk and full for big moments, about 120 KB each.
> Cinematic photograph, eye-level three-quarter view across the same kind of student desk in a small Delhi bedroom, warm desk lamp at the left edge, deep soft shadow, the lower-left third of the frame dark and empty for text. [INSERT]. 35 mm, f/2.8, fine grain, natural colour, calm mood. Avoid: legible text or numbers, logos, people, hands, calculators, bokeh balls, lens flare, glossy CGI, orange colour cast.

[INSERT] per season:
- **October to November:** "the window behind is open to a mild evening, a thin white curtain lifted slightly by the breeze, a closed exercise notebook with a plain brown cover and a pencil on the desk."
- **December to January:** "winter: a folded grey woollen shawl draped over the back of the chair at the edge of frame, a steel tumbler with a wisp of steam, the window fogged at its lower corner."
- **February to April:** "boards season: a thick stack of plain revision papers held together with a black binder clip, a highlighter beside it, a small steel water bottle."
- **May:** "exam month: early summer evening light still faintly blue in the window, a clear plastic zip pouch on the desk packed with two pencils, an eraser and a plain card with no printing, a folded handkerchief beside it."

**B-3. Subject objects in the lamp pool, five.** Output: 1024 x 1024; the object is centred so it can be cropped to a tile and to a 48 dp thumbnail; about 45 KB.
> Cinematic still-life photograph, low three-quarter angle, a single object in a pool of warm desk-lamp light on a worn grey laminate desk, the background falling into deep warm-charcoal shadow, 50 mm, f/2.8, fine grain, natural colour. Object: [OBJECT, as in A-3: the carbon-copy receipt book with a red rubber band and a pencil stub / the brass rubber stamp with a violet ink pad and blank visiting cards / the red onion on a small steel kitchen scale with the needle mid-swing / the folded editorial page with abstract grey columns and an uncapped yellow highlighter / the desk calendar with one date circled beside a round clock at about 3:15 with no numerals]. Avoid: legible text, letters or numbers, logos, hands, glossy CGI, bokeh balls, orange cast.

**B-4. The reveal room.** Output: 1024 x 1536, about 70 KB.
> Cinematic photograph looking slightly down at a dark study desk at night: one tight, soft pool of warm lamp light in the centre of the frame on worn grey laminate, completely empty, everything else falling away into warm-charcoal darkness, the lamp itself just out of frame at the upper left. A pencil lies at the very edge of the light. Quiet, expectant. 35 mm, f/2.8, fine grain. Avoid: objects in the lit area, text, logos, people, glow halos, lens flare, coloured light.

**B-5. Mobi as a desk figure, three poses** (standing, sitting on the edge of a notebook with legs dangling, leaning on a pencil). Output: 1024 x 1024 in-scene and a transparent cut-out version, about 40 KB.
> Macro photograph of a small painted resin collectible figure, about 7 cm tall, standing on a study desk in warm lamp light: a friendly robot whose body is a lime-yellow folded-kite shape with one crisp vertical crease, painted in smooth enamel with a soft satin finish, a satin black visor band with two white rounded rectangular eyes, a thin black antenna with a small lime ball, short black arms and legs with rounded boots. Pose: [sitting on the edge of a closed brown notebook, legs dangling]. 85 mm macro, f/4, fine grain, natural colour, collectible-photography quality. Avoid: glossy plastic, inflatable or glass look, text, logos, extra limbs, a mouth, orange cast.

Production note: as with A-4, lock the figure's design with one 3D model or one physical-reference render, then generate scene variants against it.

**B-6. Empty and offline states, three.** Output: 1536 x 1024, about 40 KB.
> Cinematic photograph across a dim study desk, warm lamp switched [on, low / off with only cool window light / on], the left half of the frame dark and empty for text. [nothing due: the steel tumbler empty, a pencil laid neatly on a closed notebook] [offline: the lamp off, only cool blue window light on a closed notebook, quiet] [all caught up: the small lime resin robot figure sitting on a closed notebook, legs dangling]. 35 mm, f/2.8, fine grain. Avoid: text, logos, people, hands, bokeh balls, glossy CGI.

### B.10 Concept screens (prototype briefs and art plates)

All four are built in HTML at 384 x 853 with Mona Sans, Hanken Grotesk and the B tokens, exported at 3x and shown on the M06. File names are like `B-01-welcome_concept_sample-data.png`.

1. **Welcome.**
   - Plate B-1 full-bleed, with the wordmark small at the top left in Ink.
   - In the shadowed upper half: "Your score is / the symptom." in Mona Sans 30/34.
   - Lower third over the baked scrim: the support line in Hanken 16/24, Ink 2, and the meta line "About 12 minutes. Pause any time." in Ink 3.
   - Buttons: a volt pill "Start with 10 questions", a frosted secondary "Set my goal first", and a text button "I already have an account".
2. **The fold, mid-unfold.**
   - Plate B-4.
   - The code-drawn sheet two-thirds unfolded in the lamp pool, its top panel tilted back about 40 degrees, the lower panels flat with the 50-cell grid partly filled.
   - Above it: "183" in Mona Sans 112 with "of 250", then "38 right, 7 wrong, 5 left".
   - At the top: "Mock 7, marked."
   - No bar.
3. **Now aim it.**
   - Solid ground, with the pinned result chip "Check 1: 6 of 10" and its tag "Q2, Q5, Q9" at the top.
   - The headline "Now, the target. Which colleges would you say yes to tomorrow?"
   - The "Showing UR" chip and the seven-college ladder with Mona Sans `tnum` figures, three picked with volt marks.
   - The bar line, the rule line, the caption "For the next time someone asks 'DU mil jayega?'", and "Continue".
4. **The Desk with the bar.**
   - The October plate in the top 40%.
   - The evidence line "Partnership beat you 4 times in Mock 7." and "12 minutes to repair it.", the volt Start pill and the tag "Mock 7: Q12, Q19, Q33, Q41", with "30 weeks to CUET" at the top right.
   - Below on solid: "Due today" (two rows), "This week: 2 of 3 repairs", and "Last check: Accountancy, 6 of 10, Tuesday".
   - The frosted desk bar: Desk active with the volt top edge, the volt Start pill, Mistakes with "2", and You.

### B.11 Performance plan and biggest risk

- **Live blur:** the bar plus at most one sheet, grouped, after B2 passes; Lite before that. Full-bleed plates under a live bar while scrolling is benchmark B2's worst case, so the Desk plate is not under the bar at rest. It scrolls away above the list, and the bar sits over solid ground.
- **Pre-rendered:** plates decoded at display width (`cacheWidth` 1080 for full-bleed, 384 for tiles, 144 for thumbnails); one plate per screen; the Push runs once.
- **The fold:** three images transformed, no `saveLayer`, as spec A1 already requires at 60 fps on a 720 x 1600 device.
- **Frame budget:** 11.1 ms at 90 Hz; raster p90 at or under 8 ms on the Desk while scrolling, at or under 6 ms in the runner.
- **Biggest risk: asking for a test before anything else.** Some students install to look around, and a 12-minute check as the first ask will lose some of them.
  - Mitigations: "Set my goal first" on Welcome, "Tonight at 8:00 PM", the guest check (no account wall), and the untimed default.
  - Measure install-to-first-marked-result against A in a Play experiment if both are built.
- **Second risk: dark and cinematic drifting toward generic dark fintech.** Mitigations: real Indian desk photography instead of renders, no glow or light in the UI, the warm ground, and evidence tags as the signature.
- **Third risk:** generated photographs of a "Delhi bedroom" can come out as stock. Fix the object list, reject any plate whose props are not CUET-true, and keep a tight grade.
- **Backend dependency:** a guest session the server can score and merge (variant (a)). Without it, the account comes before the check.

---

## Direction C: "Threads"

### C.1 The idea

**Core idea:** MockMob is a running conversation with Mobi, and every mistake is a thread you close. Fampay turned payments into conversations. C does the same for prep.
- **Home is an inbox.** Each mistake pattern is a thread holding the question, what you picked, the trap, the repair and the check.
- **A thread closes only when it is Checked,** and it slides into a Closed shelf that becomes the student's record.
- **Onboarding is the first chat.** Answers render as rich cards inside it, and the check and its marked sheet arrive as messages.
- **The "mob" in MockMob becomes real, with no social graph:** a closed trap can be sent to a friend as a card that opens that exact question.

**What happens differently:**
- **IA:** an inbox plus a contextual action shelf instead of tabs.
- **Presentation:** a conversation instead of screens.
- **Growth:** trap cards shared to friends.
- **Theme:** light-first with real liquid glass.
- **Mobi:** the lead character, not a garnish.

**Mood:** bright, quick, witty, warm and social, a friend who is good at this.

**What it looks like in one screenshot:** a daylight ground, a column of crisp messages (Mobi's in clear glass, the student's in volt), a solid question card inside the thread, a 3D Mobi peeking from the edge of a pinned card, and a floating liquid-glass shelf at the foot holding the two or three things you can do right now.

**References, taken as ideas only:**
- From Fampay: conversation as the organising model, and "open on the next move".
- From Revolut: "the input becomes the message" (a reply chip morphs into the student's bubble).
- From HIGH: a character-led reward layer kept separate from the data.

How it avoids the references:
- **Not Fam:** no amber, no paper tag, no DMs between people, no doodles, light-first.
- **Not HIGH:** no candy gradients and no stickers; Mobi is one consistent 3D character.
- **Not a chatbot:** Mobi's lines are scripted from real state, and nothing is typed out letter by letter to look alive.

### C.2 Brand

- **Wordmark:** `MockMob` in Gabarito ExtraBold (already bundled, with tabular figures), tracking -2%. The counter of the second "o" holds Mobi's visor, a black band with two white eyes, visible only at sizes above 32 sp.
- **Mark: "Mobi says".** A rounded volt speech bubble with its tail at the lower left. Across its upper half runs Mobi's black visor with two white eyes.
  - App icon: the mark on Daylight.
  - Monochrome: the bubble outline with the visor band.
- **Palette.** Day is the default; Night is a composed theme.

| Role | Day (default) | Night | Notes |
| --- | --- | --- | --- |
| Ground | `#F5F6F2` | `#121412` | Neutral daylight, not cream |
| Raised (cards, solid messages) | `#FFFFFF` | `#1B1E1B` | |
| Raised 2 | `#ECEEE7` | `#252925` | |
| Hairline | `#DADDD3` | `#2E322D` | |
| Ink | `#11140F` | `#F2F4ED` | |
| Ink 2 | `#3B4237` | `#B7BDB1` | |
| Ink 3 | `#5A6255` | `#8A9185` | 4.5:1 or better on each ground (re-measure) |
| Volt (the student's voice and the primary action) | Fill `#D2F000` with Ink text; volt as text `#4F6300` | Fill `#D2F000` with `#0B1000` text | The student's message bubbles, the primary shelf action, closed-thread ticks |
| Mobi's voice | Clear glass: white at 0.82 with a 1 dp edge light | `#1E221E` at 0.86 with the edge light | Fake glass in lists; real blur only on the shelf |
| Correction | Ring `#E0533D`, text `#B93225` | Ring `#FF7A66`, text `#FFB8AC` | Always with a word |

Subjects are identified by their miniature object (C.9), shown as the thread's avatar, not by a hue.

- **Typography:**

| Role | Family | Size / line / weight | Notes |
| --- | --- | --- | --- |
| Moment headline | Gabarito | 32/36 sp, 800, -2% | Two lines at most, about 20 characters a line |
| Hero number | Gabarito | 72 to 96 sp, 800, `tnum` | Verified in the bundled files (`fonts.dart`) |
| Screen title | Gabarito | 26/30 sp, 700 | |
| Message text | Hanken Grotesk | 16/23 sp, 400 | Mobi's and the student's |
| Card title | Hanken Grotesk | 17/22 sp, 700 | |
| Question and explanation | Hanken Grotesk | 17/26 sp, 400 | |
| Label, button | Hanken Grotesk | 15/20 sp, 600 | |
| Caption | Hanken Grotesk | 13/18 sp, 500 | |

- **Mobi: the lead.** The silhouette is kept exactly, rebuilt as one 3D model (Blender) and rendered in twelve poses: wave, point, think, cheer, sit, peek, read, hold pencil, shrug, sleep, thumbs up and stand.
  - **The visor is a screen,** with the eyes drawn in code over the render: blink, look left or right, happy arcs, squint and wide. Expression costs nothing and stays consistent.
  - **Mobi speaks in short lines.** One Hinglish caption-level line per screen at most.
  - **Limits:** never during a mock, never about the person ("you're bad at"), never guilt, never a fake typing delay.
  - **Optional:** "Ask why" on a mistake can call the existing student AI under its database budget guard (USD 25 per IST month). The answer is labelled by what it is (an explanation), not by technology.

### C.3 Material system

| Material | Where | Recipe |
| --- | --- | --- |
| Liquid glass (live blur) | The action shelf and bottom sheets | `BackdropFilter` grouped, sigma 20; tint white at 0.58 (Day) or `#1B1E1B` at 0.66 (Night); an inner top highlight 1 dp white 70%; shadow `0 12 28 -14` Ink at 18%. No saturation boost. **Lite by default until B2 passes** |
| Lens | The shelf's primary action | If B6 passes, a refraction lens 1.04x under the primary pill; otherwise the edge light only |
| Fake glass (messages) | Mobi's message bubbles in the thread | A flat translucent fill and edge light, no blur, so long threads scroll cheaply |
| Volt solid (messages) | The student's bubbles | Volt fill, Ink text, no shadow |
| Solid cards | Question cards, explanations, the plan, the ladder, recap cards | Raised, radius 20, a hairline border, no glass |
| 3D renders | Mobi, the moment plates | Pre-rendered WebP with alpha |
| Macro photographs | Subject avatars and the miniature scenes (C.9) | Pre-rendered WebP |

Depth: messages sit flat, cards rise 1 level, and the shelf floats. Light: soft daylight from the upper right in every render and photograph, mirrored by the UI's edge lights.

### C.4 Signature motif

**The thread closes.** Every thread carries a state dot at its avatar's corner:
- **Open (Found):** a hollow ring.
- **Repaired:** half filled.
- **Checked:** a volt tick. The thread closes.
- **Holds:** a tick with an outer ring.

Closing is the signature moment. The thread's row compresses into one line, its edge zips shut from left to right (300 ms), and it slides into Closed with a `successNotification` after the server acknowledges. A clean inbox with a volt tick sliding away is MockMob's screenshot.

### C.5 Navigation: the action shelf

- **There is no tab bar.** There are two places, the Inbox (home) and You, plus Practice as a full screen ("Choose your own"). The verbs live in a shelf.
- **The shelf** floats in liquid glass: 64 dp tall, inset 12 dp, 10 dp above the gesture inset, radius 32. It holds up to three labelled action pills for the current context, plus the student's avatar chip at the right end, which opens You.
  - On the Inbox: "Tonight: Partnership, 12 min" (volt), "Quick 10" and "Choose your own".
  - Inside a thread: "Repair this, 12 min" (volt), "Show the trap again" and "Close for now".
  - On a recap: "Repair the first one" (volt) and "Back to inbox".
- **Morphing:** when the context changes, the pills morph between sets (Morph, 320 ms) and the shelf's outer size never changes.
- **Inbox controls:** a segmented "Open | Closed" toggle sits under the title (swiping left on the Inbox does the same). Pulling down opens search ("Search chapters and questions"), and a visible search icon does the same.
- **Back** always returns toward the Inbox; predictive back is preserved.
- **Haptics:** `selectionClick` on a pill or toggle; `lightImpact` when a reply chip becomes a message.
- **Scroll:** the shelf sinks 6 dp on scroll down and returns on idle. It is hidden in the runner and the reveal.
- **TalkBack:** pills are named buttons; "Inbox, 2 due today"; "Open threads, Closed threads, tab".
- **The trade-off:** it is the most novel navigation of the three and the least conventional. A first-use hint (one line, once) explains it: "Your next moves live down here."

### C.6 Onboarding: "First chat"

A slim four-part bar in the header shows Aim, Subjects, Pace and Check. Mobi's messages appear immediately, staggered 80 ms, with no typing indicator. The student answers with reply chips. The chosen chip morphs into a volt message (Morph), and the payoff arrives as a card in the same thread.

**1. Cold open (first launch only).** The mark on Daylight. Mobi's eyes blink on inside the visor (two code frames), and the bubble settles with a small spring. 0.9 s; tap skips; `lightImpact` on the blink.

**2. Hello.**
- Layout: Mobi rendered full body (C-1), waving from the lower right, cropped at the knees. The first messages sit above.
- Headline: "Topper notes, / but about your mistakes."
- Mobi's first message: "I'm Mobi. I find where your CUET marks go and help you repair what's behind them."
- Second message, the time promise: "Two minutes of questions, then a real 10-question check. Skip anything."
- Chips: "Let's go" and "I already have an account".
- Fast lane from mockmob.in: Mobi says "Picking up from mockmob.in. You were on B.Com (Hons) and Accountancy." The thread starts with those answers already in it.

**3. Which CUET.**
- Mobi: "Which CUET are you writing?"
- Chips: "May 2027, Class 12", "May 2027, gap year", "Class 11" and "Not sure".
- Payoff card: "About 30 weeks. May 2027, dates not out yet." For Class 12, Mobi adds: "Boards come first, mid-February to early April. I'll go lighter on you then."

**4. Course and colleges.**
- Mobi: "Which course?" with course chips and their real counts.
- The payoff is the ladder card, a solid card in the thread holding the "Showing UR" chip and the seven-college ladder. The student taps up to three picks inside the card.
- Mobi: "SRCC took 924.3 out of 1000 in CSAS 2026, Round 1. That's about 231 of 250 a paper."
- Then, the screen's one Hinglish line: "Next time someone asks 'DU mil jayega?', you'll know exactly what it takes."
- The rule line sits at the foot of the card.

**5. Subjects, and how solid each feels.**
- Mobi: "Your subjects. How solid is each, honestly?"
- Payoff card: rows with Shaky, Okay and Strong, reordering live, and the fit line.
- Mobi: "I'll check your gut against the real thing."

**6. Where the marks go.**
- Mobi: "Where do your marks actually go?" with the same chips as A.
- The reply rewrites the pinned first move, per the 0.7 mapping.
- Mobi answers in one line. For "knew it": "Knew it, lost it anyway? That's a trap, not a gap. Those are the quickest to win back."

**7. Pace.**
- Mobi: "What pace can you keep?"
- The pace card (minutes, days, time) with the live count: "About 108 sessions before CUET."
- Mobi: "Dotted days are rest days. They count."

**8. The plan.**
- A pinned card rises to the top of the thread: "Your first week".
  1. "A 10-question check in Accountancy, about 12 minutes."
  2. "Then Partnership, if the check agrees."
  3. "Four evenings, 20 minutes, around 8:00 PM."
  4. "Lighter during boards." (Class 12 only)
- Mobi: "Look right?" with the chips "Looks right" and "Change something".

**9. Save.**
- Mobi: "Want to keep this chat? It follows you to mockmob.in."
- An inline card holds the age row ("Quick one: are you 18 yet?" with "Under 18, usage tracking stays off."), then "Continue with Google", "Use an email code" and "Not now".
- Pending, acknowledged and failure states as in A, written as Mobi lines: "Saving..." becomes "Saved." only after acknowledgment. On failure: "Couldn't save. It's all still on this phone." with "Try again".

**10. The check.**
- Mobi: "Now the real thing. 10 questions, Accountancy, about 12 minutes. I'll stay quiet till you finish."
- A card with "Start" and "Tonight at 8:00 PM". "Tonight" triggers the reminder ask as scheduling.
- The runner opens full screen (C.7).

**11. Marked, in the thread.**
- Back in the chat, the result arrives as a message: a sealed sheet card with a pull tab and the line "Check 1, marked."
- Pulling the tab (it follows the finger 1:1) or tapping "Open" expands the card to full screen (C.7). Closing it returns to the thread, where the recap arrives as messages and cards:
  - Card, "Where the marks went": the chapter rows.
  - Mobi: "Here's the first one to repair." Then the card: "Partnership: 3 of your 4 wrong answers. Same trap twice."
  - Mobi, gut versus check: "You called Accountancy shaky. 6 of 10. Shaky on Partnership, solid on Company Accounts. Your gut was half right."
  - Card, "What's recorded", with "Repair the first one" in the shelf.

**12. Reminders.**
- Mobi: "Want me to ping you at 8:00 PM on your days? Never after 11."
- The preview notification card: "Mobi: Partnership, 12 minutes. Same trap twice in your check."
- Chips: "Ping me" and "Not now".

**13. Landing.** The thread collapses into the pinned Mobi thread, and the Inbox assembles below it with one thread per mistake pattern from the check, each arriving with a 60 ms stagger.

Timing targets: the first payoff card in under 10 s, the plan in under 2 minutes, then the check.

### C.7 Home, the work screens, result reveal, celebrations, streaks, return

**Inbox, usual state.**
- Title "Inbox" (Gabarito 26) with a small "~30 weeks to CUET" chip, and the "Open | Closed" toggle.
- Pinned at the top, Mobi's thread "Tonight": the next move, with "This week: 2 of 3 repairs" as a small row.
- Then:
  1. a half-finished mock ("Mock 8: 23 of 50 answered" with "Resume");
  2. an unopened result (a sealed-sheet row);
  3. "Due today" threads, at most 3, each with its miniature avatar, the trap as its title ("Partnership: interest on capital"), its last line ("Found in Mock 7, Q19 and 2 more") and its state dot;
  4. a collapsed "More open threads" row with no count.
- Pinned at the foot: the ladder card.

**Inbox, day one.**
- State 1, check deferred: Mobi's pinned thread "Your check is set for 8:00 PM. 10 questions, Accountancy." with "Start now" in the shelf, plus the ladder card. Nothing else.
- State 2, check done: Mobi's pinned thread ("Partnership first. 12 minutes.") and the threads from the check.

**A thread** reads top to bottom:
- Mobi: "Mock 7, Q19. You picked B; the answer was D."
- The question card (solid) with both options marked.
- The trap in three lines, plus a worked example card.
- The shelf: "Repair this, 12 min".
- The repair runs inline as cards, with feedback per answer. Then: "Repaired in 9 min 40 s. Fresh check opens tomorrow."
- The next day Mobi posts: "Fresh check ready: 4 questions you haven't seen." The result reads "3 of 4 (was 0 of 4)." The thread closes (Checked) with the zip.
- About a week later: "Retained check ready." Passing it makes the thread Holds.
- **Share:** inside a closed thread, "Send this trap to a friend" makes a card showing the question and the trap's name. It carries no marks and no name unless the student adds one. Its deep link opens that question in the app, or on mockmob.in if the app is not installed. There is no contacts permission, no feed and no in-app social graph.

**Practice ("Choose your own").** A full screen with the subject miniatures, the modes with what you get, and the Concepts shelf. The confirm sheet carries the cost: "10 questions, about 10 minutes. 10 credits. You have 90."

**Before-mock card** (in the thread): Mobi says "50 questions, 60 minutes. Answers save as you go. I'll be quiet till you finish." The card holds "Start" and "Not now".

**The runner.**
- The shared contract in C's tokens: solid Raised ground in Day or Night, the timer in Gabarito `tnum`, and the save glyph (a small bubble outline that fills volt on acknowledgment).
- Options are solid rows with a volt left edge when selected.
- Bottom: "Flag", "Questions" (the palette sheet) and "Next". The leave guard is as in A.
- No Mobi and no chat chrome.

**Result reveal: "Pull to open".**
1. The sealed sheet card in the thread, "Mock 7, marked", with a tab at its top edge.
2. **The pull.** Pulling the tab down follows the finger, with `selectionClick` at 25, 50 and 75%. Released over 60%, the card expands to full screen (Morph). Tap "Open" and the TalkBack action always work.
3. **The marking.** The full-screen sheet shows the grid marking section by section (volt for right, correction rings for wrong, hollow for left). "183" rolls in Gabarito 96 with "of 250", then "38 right, 7 wrong, 5 left".
4. **The recap.** Closing returns to the thread with the recap as messages: where the marks went, first thing to repair, against your last mock (Mobi: "183, up from 171. Partnership: 2 wrong, down from 5."), and what's recorded.

Variants:
- **Lower result:** the card opens with a plain fade. Mobi: "Here's the first thing to repair." The compare line is neutral: "Down 12 from Mock 6. Most of it was Dissolution."
- **First mock:** "Mock 1 is marked. Here's your map." No score celebration.
- **Decay** from the fourth sheet: a tap opens it.

**"Finish for now":** "Close for now" in the shelf. Mobi: "Done for tonight. Partnership repaired. Dissolution is next, Thursday."

**Celebrations (server-acknowledged only).**
- **Small:** a reply lands with `selectionClick`.
- **Milestone:** a thread closes (the zip) and Mobi appears at 64 dp in the cheer pose for 1.2 s, then settles. `successNotification`, plus the fact line.
- **Big** (a chapter Holds, the first mock finished, a score beating the student's own last): a full-screen moment plate (C-4) with Mobi's matching pose, one line ("Partnership holds."), one fact sentence and "Share this".

**Streaks.** "This week: 2 of 3 repairs" in Mobi's pinned thread, as a chosen goal with rest days. A missed day is not mentioned.

**Return** (three or more days): Mobi says "Welcome back. How long have you got?" with chips for 10, 20 and 30 minutes. Mobi is in the peek pose.

**You (identity first).**
- "Your record": the Closed shelf as a grid of small closed-thread cards (trap name, subject miniature, Checked or Holds), then the counts, the ladder and personal bests.
- "Make Mobi yours": visor colours earned at real milestones (the first Holds, the first mock finished), predictable and never sold or random.
- Then settings.

**Widget.**
- 2 x 2: a Mobi bubble saying "8:00 PM: Partnership, 12 min", plus Start.
- 4 x 2: adds "2 due today" and the countdown.

### C.8 Motion and haptic language

| Name | What | Curve and duration |
| --- | --- | --- |
| Arrive | A message or card entering the thread | Rise 8 dp plus fade, 200 ms, `cubic-bezier(0.2, 0.8, 0.2, 1)`, 80 ms stagger; never a typing delay |
| Morph | A reply chip becoming the student's message; shelf pill sets; a sealed card to full screen | `cubic-bezier(0.18, 0.9, 0.2, 1)`, 320 ms (full screen 420 ms) |
| Zip | A thread closing | The edge draws shut 300 ms, then a 220 ms collapse, then a slide to Closed |
| Pull | The sealed card's tab | Follows the finger; release on a spring of 380 ms, bounce 0.1 |
| Blink | Mobi's visor eyes | Code frames: blink 120 ms, look 180 ms, happy arcs 240 ms |
| Pop | Mobi at a milestone | Scale 0.9 to 1.0 on a spring of 300 ms, bounce 0.2 |
| Roll | Digits | 40 ms per digit, 480 ms |
| Leave | Anything exiting | `cubic-bezier(0.5, 0, 0.75, 0)`, 180 ms |

- **Idle:** Mobi blinks every 6 to 9 s only while a Mobi render is on screen and the student is not reading a question. Nothing else idles.
- **Never moves:** question text, options, the timer, explanation body, numbers once landed, or the thread while the student is reading it. New messages arrive only in response to the student's action.
- **Reduced motion:** Arrive and Morph become 120 ms fades, Zip becomes an instant state change with the word "Closed", Pop is static and Blink stops.
- **Haptics:**
  - `selectionClick`: chips, pills, pull thresholds;
  - `lightImpact`: a reply becoming a message, the cold-open blink;
  - `successNotification`: acknowledged submission, a thread closing, a milestone;
  - `warningNotification`: leaving a timed mock.

  None on wrong answers.

### C.9 Imagery plan

**Image bible for C: "daylight miniatures and one character".**
- **Mobi** is one consistent 3D character, modelled once and rendered. gpt-image is used only to explore materials, never as the source of the final poses, because it cannot hold a character across a set.
- **Subjects and moments** are macro photographs of 1:12-scale miniatures: real-material small objects (paper, steel, clay, wood) on pale paper.
  - Light: soft window daylight from the upper right.
  - Camera: a 100 mm macro at f/5.6 with a gentle tilt-shift falloff.
  - Feel: crisp, bright, airy, collectible.
- **Grade:** daylight neutral with lifted shadows, never pastel candy.
- **Never:** text, logos, faces, calculators, inflatables, CGI gloss.

**Better as code:** the visor eyes and expressions, every chat bubble, cards, the shelf, state dots and the zip, the sheet and its marking, number rolls, the share card layout.

**C-1. Mobi turnaround and twelve poses (production through a 3D model).**
- **Brief for the 3D artist** (or a Codex-assisted Blender build): match `assets/mobi/greeting.webp` exactly in silhouette.
  - Body: a lime-yellow folded-kite diamond with one vertical crease, in a soft-touch matte polymer with a faint satin sheen on the crease ridge.
  - Visor: a flat satin black band, kept flat so code can draw the eyes.
  - Antenna: thin black, with a lime ball.
  - Limbs: short black arms and legs with rounded boots.
  - Rig the arms, legs and antenna. Render at 1024 px with alpha under one daylight key from the upper right and a soft white bounce, matching C's art.
- **gpt-image material exploration prompt:**

> Product photograph of a small collectible robot figure about 9 cm tall on a transparent background, bright soft window daylight from the upper right, white bounce fill, crisp edges. Its body is a lime-yellow diamond like a paper kite folded along its vertical centre, one crisp crease, made of soft-touch matte polymer with a faint satin sheen on the crease. A flat satin black visor band crosses the upper body with no eyes printed on it. A thin black antenna with a small lime ball. Short black arms and legs with rounded black boots. Pose: standing, waving with the right hand. Collectible-photography quality, true-to-life materials. Avoid: glossy plastic, inflatable look, glass, chrome, a mouth, printed eyes, text, logos, extra limbs.

**C-2. Subject miniatures, five** (thread avatars and Practice tiles). Output: 1024 x 1024, transparent, about 25 KB at 256 px.
> Macro photograph of a tiny handmade miniature, about 3 cm across, at 1:12 dollhouse scale, on a transparent background, lit by soft bright window daylight from the upper right with a white bounce, 100 mm macro lens at f/5.6, real materials with tiny handmade imperfections, crisp edges for cut-out, no ground shadow. Miniature: [Accountancy: a tiny carbon-copy receipt book with a red rubber band and a pencil stub the size of a grain of rice] [Business Studies: a tiny brass-handled rubber stamp beside a tin ink pad with violet ink] [Economics: a tiny red onion on a miniature steel kitchen scale with its needle mid-swing] [English: a tiny folded newspaper with abstract grey columns and a yellow highlighter] [General Test: a tiny desk calendar with one date circled beside a tiny round clock at about 3:15 with no numerals]. Avoid: legible text, letters or numbers, logos, hands, glossy CGI, plastic toy look, saturated candy colours.

**C-3. Welcome scene.** Output: 1024 x 1536, about 110 KB.
> Bright, airy photograph of the corner of a real student's desk by a window in the morning, soft daylight from the upper right, pale wood surface, a plain white wall. On the desk: a closed exercise notebook with a plain brown cover, a pencil, a steel tumbler, a small potted money plant at the far edge. Lower-right third left clear (a character is composited there later). The upper half is calm, pale and empty for text. 50 mm, f/4, lifted shadows, natural colour, fine grain. Avoid: text, logos, people, hands, calculators, phones, glossy CGI, pastel candy colours, lens flare.

**C-4. Moment plates, three** (first mock finished, first Holds, the weekly goal met), each with room for a composited Mobi pose. Output: 1024 x 1536, about 100 KB.
> Macro photograph of a 1:12 scale miniature scene on a pale paper surface in bright soft daylight from the upper right, 100 mm macro at f/5.6 with gentle tilt-shift falloff, real materials. [first mock finished: a tiny stack of three plain exercise notebooks with a pencil laid across the top, a tiny steel tumbler beside it] [first Holds: a tiny brass padlock, closed, resting on a tiny folded paper sheet] [weekly goal met: three tiny pencils standing in a tiny steel cup, all sharpened]. Clear space at the right for a figure added later, the top third empty for text. Avoid: text, letters or numbers, logos, hands, glossy CGI, confetti, candy colours.

**C-5. Empty and offline states, three** (Mobi poses composited over miniature props). Output: 1024 x 1024, about 35 KB.
> Macro photograph of a 1:12 scale miniature on pale paper in soft daylight from the upper right, 100 mm macro: [nothing due: a tiny hammock strung between two pencils stuck upright in an eraser] [offline: a tiny paper boat on a sheet of pale blue paper] [all caught up: a tiny closed notebook with a tiny pencil resting on it]. Space at the left for a figure added later. Avoid: text, logos, hands, glossy CGI, candy colours.

### C.10 Concept screens (prototype briefs and art plates)

All four are built in HTML at 384 x 853 with Gabarito, Hanken Grotesk and the C tokens, and C-1 renders composited in. They are exported at 3x and shown on the M06. File names are like `C-01-first-chat_concept_sample-data.png`.

1. **First chat, the ladder card.**
   - The four-part bar with Aim active.
   - Mobi's message "Which course?" and the student's volt reply "B.Com (Hons)".
   - The ladder card: the "Showing UR" chip and seven colleges with Gabarito `tnum` figures, SRCC, Hindu and Hansraj ticked in volt.
   - Mobi's message with the 924.3 line, then the "DU mil jayega?" line.
   - Mobi's head peeking from the right edge (the peek pose, 72 dp).
   - The shelf, holding "Continue".
2. **Inbox with the shelf.**
   - Title "Inbox", the "~30 weeks to CUET" chip and the Open | Closed toggle.
   - Mobi's pinned thread "Tonight: Partnership first. 12 minutes." with "This week: 2 of 3 repairs".
   - Two due-today threads with miniature avatars and state dots, and "More open threads".
   - The liquid-glass shelf: "Tonight: Partnership, 12 min" (volt), "Quick 10", "Choose your own" and the avatar chip.
3. **A thread, mid-repair.**
   - Mobi: "Mock 7, Q19. You picked B; the answer was D."
   - The solid question card, the trap card, two repair question cards (the first answered correctly with an ink check, the second waiting) and the Repaired-pending state dot.
   - The shelf: "Next question" and "Close for now".
4. **The sealed result pulling open.**
   - The thread, with the sealed sheet card "Mock 7, marked" half pulled down: its tab dragged, the card expanding, the marked grid beginning to show.
   - "183" partly rolled.
   - The shelf hidden.

### C.11 Performance plan and biggest risk

- **Live blur:** the shelf plus at most one sheet, after B2 passes; Lite before that. Messages are fake glass, so long threads scroll on the cheap path.
- **Lists:** threads are virtualised (`ListView.builder`), and messages are fixed-layout cards with no per-frame relayout. Renders are decoded at display size.
- **Mobi:** WebP poses at 512 px with code-drawn eyes, so there is no Rive or Lottie (B8 can still test Rive if the owner wants richer motion).
- **Frame budget:** 11.1 ms at 90 Hz; raster p90 at or under 7 ms in the Inbox and threads, and at or under 6 ms in the runner.
- **Biggest risk: it is the furthest from the owner's dark, cinematic taste,** and a chat can read young or slow.
  - Mitigations: Night as a fully composed theme, an instant tempo (no typing delays), short Mobi lines, the solid cards that carry all the facts, and the owner's call on question G3.
- **Second risk: the inbox becoming a to-do guilt pile.** Due-today capping and the collapsed, uncounted "More open threads" row are mandatory.
- **Third risk: the 3D character cost.** One model is needed before any pose ships, and consistency fails without it (question G4).
- **Backend dependencies:**
  - a thread model (mistake patterns with states) over the existing review data;
  - deep links for trap cards on app and web;
  - the guest-check option if chosen (question G2).

---

## D. The three side by side

| | A. Your Sheet | B. Cold Read | C. Threads |
| --- | --- | --- | --- |
| What MockMob is | Your own OMR sheet for the season | A desk where every claim shows its evidence | A conversation with Mobi in which mistakes are threads you close |
| What happens first | Goal, subjects and pace in about 2 minutes, then the check | One choice (the paper), then the check; the goal comes after the evidence | A 2-minute chat, then the check inside the chat |
| Time to the first marked result | About 14 minutes | About 12 minutes | About 14 minutes |
| Confidence question | Yes, repaid by "gut versus the check" | No; evidence replaces it | Yes, repaid in Mobi's recap line |
| Home | Today: the live sheet, the week, due today | Desk: a season photograph with one evidence sentence | Inbox: a pinned Mobi thread plus due-today threads |
| Navigation | A 4-tab dock with a liquid bubble lens (Today, Practice, Repair, You) | A desk bar: Desk, a Start pill that opens into the core loop, Mistakes, You | No tabs: a contextual action shelf, the Inbox and You |
| Default theme | Night (Day composed) | Night (Daylight composed) | Day (Night composed) |
| Glass | Frosted dock and sheets, a liquid lens, smoked fake glass on plates | Frosted acrylic bar and sheets, fake acrylic tags on plates | Liquid-glass shelf, fake-glass messages, a lens on the primary pill |
| Loud move | The marking wave across the student's own sheet | The full-bleed season photograph and the evidence sentence | The thread zipping closed, and Mobi |
| Signature motif | The bubble in seven states | "Show me" tags on every claim | The closing thread |
| Imagery | Overhead lamp-lit still life of real desk objects | Eye-level cinematic photography of an Indian evening desk, changing with the calendar | One 3D Mobi plus daylight macro miniatures |
| Type | Archivo plus Hanken Grotesk | Mona Sans plus Hanken Grotesk | Gabarito plus Hanken Grotesk |
| Mobi | Kept and upgraded in material; a code rig with one-line voice | A small physical resin figure in photos; rare in the UI | The lead: one 3D model, code-drawn eyes, many poses |
| Result reveal | Hold the seal, then the sheet is marked section by section | Drag to unfold the folded sheet | Pull the sealed card open inside the thread |
| Social | Share card (private, no marks) | Share card | Trap cards to friends that open the exact question |
| Closest reference, and the difference | HIGH's two-layer rule; nothing visual borrowed | Revolut's morph and Fampay's environment light, but photographic and evidence-led | Fampay's conversation model, but light, with no person-to-person DMs and a single character |
| Fit with the owner's taste (dark, cinematic, editorial, tactile, selective glass) | High | Highest on "cinematic" | Medium (light-first, playful) |
| Fit with "high.live is crazy" energy | Medium to high (moments) | Medium | High (character, pace) |
| Fit with Fampay's generation appeal | Medium | Medium | High |
| M06 cost | Low to medium | Medium (full-bleed plates) | Low to medium |
| Asset volume | About 20 images plus the Mobi model | About 20 images plus Mobi photos | About 15 images plus the Mobi 3D model (required) |
| Backend work beyond the current plan | Profile fields for onboarding answers | A guest session the server scores and merges (if chosen); evidence links on plan lines | A thread model over review data; trap-card deep links |
| Biggest risk | Reads as a form | Test-first loses browsers; dark drifts generic | Reads young or slow; furthest from the owner's dark taste |

## E. Recommendation: A, "Your Sheet", with B's evidence tags and C's threads

**Build Direction A as the world.** Then transplant two specific things and keep HIGH's two-layer rule on top: everyday screens are quiet, and the moments are loud.

### E.1 Why A is the base

1. **Its central idea is the strongest and the most ownable.** The OMR sheet is the exam's own object. No fintech or edtech brand owns it, and it scales from the logo to the dock indicator, the onboarding progress, the week row, the runner's options, the reveal and the identity in You. The drop-out-ink truth ("the grid is ours, the marks are yours") gives the brand a real story, not a theme.
2. **It answers the owner's onboarding complaint directly.** It is goal-first and scalable (data-driven), every answer visibly fills something, and the first run ends on the real marked sheet, which is the Undertone lesson the research said was missing.
3. **It fits the owner's taste:** dark, tactile, selective glass, weighty motion with no idle wobble, and the interactive dock (a liquid lens, long-press scrubbing, velocity stretch) he said was missing.
4. **It is the cheapest to make premium on the M06.** It is mostly code-drawn, has no full-bleed art under the dock, and uses one still-life plate per moment screen.
5. **It continues mockmob.in.** Volt is the student's mark and the ground is graphite, so the app and the site read as one brand, and a rebrand can start in the app and flow back.

### E.2 What to take from B: the evidence tags, and the evidence-first lane

- **"Show me" tags** under every claim the app makes (plan lines, the Today hero, recap cards, Repair rows, notifications), opening the exact questions behind it. They are drawn in A's language: a small frosted tag with a row of tiny bubbles that the student can tap open. This is integrity made interactive, and it costs almost nothing.
- **"Rather start with 10 questions?"** on Welcome is already in A.6. It is B's order as an optional lane for students who would rather prove than describe.

### E.3 What to take from C: threads inside Repair, and trap cards

- **Inside A's Repair tab, each mistake pattern is a thread** (the question, your pick, the trap, the repair, the fresh check) that closes into a Closed shelf when Checked. A's bubble states replace C's dots. The tab keeps its due-today cap.
- **Trap cards:** after a Checked thread, "Send this trap to a friend" shares a card with the question and the trap, carrying no marks and no name, with a deep link. This is the honest version of the "mob" and a free growth loop.
- **C's instant tempo rule:** no fake typing and no staged loading anywhere in the app.

### E.4 The two layers

- **The moment layer** gets the full treatment: the cold open, Welcome, the ladder, the plan, the marking, milestone screens, the widget and return. That means lamp-lit plates, the liquid lens, the hold and the marking wave, and Mobi's lines.
- **The work layer** (Practice, Repair, the runner, settings) is quiet: solid surfaces, Hanken text, no art behind reading, no idle motion.

This puts the excitement where it inspires, keeps the calm where students think, and is the best defence against "overdone the lighting" and "reduce rather than decorate".

### E.5 Why not B or C on their own

- **B alone** is the most cinematic and the most honest in spirit, but asking for a 12-minute test before anything else will lose students who came to look around. Its photography also makes it the heaviest on the M06 and the easiest to drift into generic dark fintech. Its best idea, the evidence tags, survives in the blend.
- **C alone** has the best character, the most Gen Z energy and the cleverest growth loop. But it is light-first and chat-shaped, the furthest from the owner's dark and cinematic briefs, and it depends on a 3D character pipeline before anything ships. Its threads and trap cards survive in the blend.

### E.6 What the blend's concept screens should be

Build A.10's four prototypes, with a "Show me" tag under the Today hero line and on the first recap card, and with Repair shown as threads in a fifth screen (`A-05-repair-threads_concept_sample-data.png`). If the owner wants to compare directions at their loudest, also build B.10 screens 1 and 4 and C.10 screens 1 and 2. That makes nine prototypes in all, each shown on the M06.

---

## F. Decisions for the owner, and the next steps

### F.1 Decisions

Section G asks the eight questions that change the build: direction or blend, account timing and the guest check, theme, glass strength, Mobi's future, brand scope, imagery, and tone. These decisions are already made in this document unless the owner overrides them:
- the onboarding contract in 0.6, including ending on the real reveal and asking for reminders after it;
- the progress vocabulary (Found, Repaired, Checked, Holds) and the celebration rules in 0.3;
- the removals in 0.4;
- the shared engineering gates in 0.12;
- the widget and the connections in 0.9.

Decisions still owed from the onboarding research, unchanged by this document:
- **D2:** the under-18 account approach before the DPDP child rules take effect around May 2027, with a counsel review.
- **D6:** the size and approval of the warm-up and check question pools.
- **D7:** the name of the NTA-style mode (proposed: "Exam-day layout") and the Play listing wording.
- **D8:** the owner's hands-on walkthrough of the Indian prep apps.

**Video.** No video is needed inside the app. Every motion here is code or a pre-rendered still, which is lighter and smoother on a 3.5 GB phone than video. Video is worth doing later for the Play Store promo and the website hero, using the same plates and prototypes.

**Image generation.** Plates and explorations are made with the owner's own ChatGPT or Codex image tools, not the MockMob API budgets. The Mobi 3D model needs either a 3D artist (about a day) or a Codex-assisted Blender build. Either is the owner's call, and nothing is spent before he says yes.

### F.2 Next steps once a direction is picked

1. **Reconnect the M06 and run benchmarks** B1 (refresh rate, renderer, cold start), B2 (glass dock over a flung list of art), B6 (lens shader), B7 (art under the dock) and B12 (haptics). These decide Full or Lite glass, the lens and the haptic vocabulary.
2. **Check every candidate display face with fonttools** for `tnum` and `lnum` (Archivo, Mona Sans). Gabarito is the fallback.
3. **Generate the chosen direction's art plates** in one batch, grade them to the palette, compress them, and review each at 100% for stray text.
4. **Build the concept prototypes** (A.10 plus E.6) in HTML with real fonts, and review them with the owner on the M06. No Flutter code is written before this review.
5. **Write the design spec** that replaces APP-DESIGN-SPEC's visual and copy sections: tokens, type roles, the bubble states, the dock, sheets, the motion and haptic tables, the copy deck, and the step-deck schema with its two required payoff lines.
6. **Build in the order the owner will see it:**
   1. cold open and Welcome;
   2. the onboarding deck;
   3. the check, the runner and the reveal;
   4. Today, day one and usual;
   5. Repair threads and the fresh check;
   6. Practice;
   7. You;
   8. the widget.

   Remove every route placeholder before any build reaches the owner's phone.
7. **Run an owner phone pass on the M06:** profile-mode frame timings, both themes, TalkBack, reduced motion, 1.3x and 2.0x font scale, gesture navigation, and every screen checked against the slop list.

---

## G. Questions for the owner

Eight questions, each one changing what gets built.

**G1. Which direction, or which blend?**
- (a) A with B's evidence tags and C's threads (recommended, E).
- (b) A on its own.
- (c) B, evidence first.
- (d) C, the Mobi conversation.

*What it changes:* the first-run order, the home screen, the navigation model and the whole asset list.

**G2. Before the student has an account, can the server mark their first check?**
- (a) Yes: build a guest session the server scores and merges into the account at sign-in. The account is asked after the reveal. This is a small API change.
- (b) No: ask for the account (one-tap Google) right before the check.
- (c) No: guests get the plan only, and the check waits for an account.

*What it changes:* where the account screen sits, whether "value before commitment" holds, and whether B is viable at all.

**G3. Themes?**
- (a) Dark only.
- (b) Dark by default, with a fully designed light theme.
- (c) Follow the phone, with both themes equal.
- (d) Light by default (C's choice).

*What it changes:* how many plate grades, tokens and screenshots we produce, and C's whole character.

**G4. What is Mobi's future?**
- (a) Keep the current Mobi, upgrade the material, and let it speak one short line at moments (A).
- (b) Make Mobi the lead character: one 3D model, many poses and expressions, talking in short lines (C).
- (c) Shrink Mobi to a small cameo: a physical figure in photos and a few empty states (B).
- (d) Retire Mobi from the app and keep the mark only.

*What it changes:* whether we commission a 3D model, how many poses we make, and how much Mobi says.

**G5. How strong should the glass be?**
- (a) Bold: live blur on the dock and sheets, plus the refraction lens, if the M06 benchmarks pass.
- (b) Selective: live blur on the dock only, with fake glass everywhere else.
- (c) Subtle: no live blur on the M06 at all; tinted fake glass and edge light only.

*What it changes:* the default quality setting, the benchmark bar, and how "liquid" the dock and sheets feel on budget phones.

**G6. How far does the brand change?**
- (a) A new wordmark, mark and app icon in the app now, with mockmob.in following in a later pass. The name stays MockMob.
- (b) The app, the website and the Play listing all move together in one release.
- (c) Keep the current wordmark and icon, and change only the app's visual system.
- (d) Open to a new name. If so, we pause the build for a naming round first.

*What it changes:* how much brand work happens before screens, and whether the website ships alongside.

**G7. What should the imagery be?**
- (a) Generated photographs of real objects from a student's desk: still life, no people (A and B).
- (b) A 3D character plus daylight miniatures (C).
- (c) Flat illustration.
- (d) Photography of real students, shot with their written consent; never generated people posing as real.

*What it changes:* the art pipeline, the cost and the timeline, and whether the app shows faces at all.

**G8. How playful against how serious?**
- (a) A sharp senior: dry, specific, rarely joking, at most one Hinglish caption per screen (the current proposal).
- (b) A Gen Z friend: more humour and more Hinglish in captions and empty states, never in instructions.
- (c) Calm and serious: almost no jokes, no Hinglish.

*What it changes:* every line of copy, how much Mobi speaks, and how loud the moment screens are.
