# MockMob app redesign: build brief ("Night Sheet")

13 October 2026, 03:40 IST. The owner rejected the first build ("really basic", "rudimentary", "not even close to an onboarding flow of a polished app", "a good navbar wouldn't look like this") and asked for "a really fancy UI, something premium, something which inspires people", with HIGH (high.live), Revolut and Fampay as the vibe. He then went to sleep and said: "don't ask me for anything... Keep on making the app better... bring it to 90 by morning." So the decisions below were made by the orchestrator on his behalf, from the research in this folder. **This brief wins over every other document on conflicts.** For detail, read `directions-final.md` (or `directions.md` if final is missing), section B "Afterhours" and section E, then `ref-*.md`, `owner-materials.md`, `onboarding-research.md` and `flutter-feasibility.md` in this folder.

Concept renders to match in spirit (open them): `tmp/design-concepts/afterhours/concept-1.png` (welcome), `concept-2.png` (onboarding step), `concept-3.png` (Today: use its art and materials, NOT its Revolut layout), `concept-4.png` (result reveal). Generated art for the app: `tmp/design-concepts/assets/*.png` (see section 9).

## 1. The decision

**Direction: "Night Sheet".** Afterhours' world (a dark, cinematic room; smoked glass on floating parts; one volt light per screen; monumental condensed numbers; weighty glide) built around one central object the student owns: **their OMR answer sheet**. The bubble sheet is the logo, the onboarding object (a bubble fills per answer), the dock indicator, the week row, the progress of every task, and the result reveal (a folded black answer sheet sealed with lime foil that unfolds and inks its bubbles). Two layers, as HIGH does: the **moment layer** (cold open, welcome, plan reveal, result fold, milestones) gets art, light sweeps and monumental type; the **work layer** (runner, lists, repair, settings) is calm and solid.

### 1.1 Warm, not ice cold (the owner's last note before sleeping)

He looked at the first concept renders and said: "It has some taste and all but it's very ice cold. I hope you'll work on refining this and not just copy-paste this completely. The direction that you are now taking is really good." So the room is a **late-night study desk, not a cold studio**:
- Light: every moment scene has a warm tungsten desk-lamp key light (honey amber, about 2700 K) pooling from the upper left, with volt as the single accent light. The renders in `tmp/design-concepts/afterhours` are cold references for layout and material only; the shipped art in `tmp/design-concepts/assets` (warm batch) is the colour truth.
- Colour: warm the neutrals (section 3). Volt stays the only interactive accent; amber "lamp light" exists only as environment (glows, light fields, art), never as a button or text colour.
- People: greet by first name; time-aware lines (after 11 PM: "Late one tonight. Ten minutes, then sleep." with sleepy Mobi); acknowledge real feelings (boards and CUET in the same months, a coaching test that came back low, "DU mil jayega?" from relatives) without drama; celebrate effort as well as scores ("Mock 7 done. That's your third full paper this month."), always truthfully.
- Mobi is a companion with personality (seven warm poses), present at the human moments, absent while the student works.
- Texture: warm film grain and soft paper on the moment layer; type stays crisp.
- Do not copy any render literally; refine.

## 2. Brand

- Wordmark: `mockmob` lowercase, Bricolage Grotesque condensed (wdth 75 to 87, wght 700), with a 1.5 dp volt hairline through the x-height (see concept-1). In motion the hairline draws left to right in 500 ms.
- Mark and app icon: a rounded-square dark tile (`#101210`) with a 2 by 2 grid of answer bubbles; one bubble is filled volt, the other three are hollow hairline rings; a 1 dp volt edge light along the top. Draw it in code (CustomPainter) and export the launcher icons from the same geometry (Python PIL is fine). Adaptive icon foreground plus `#101210` background; monochrome themed icon as outlines with the filled bubble solid.
- Mobi: keep the existing character exactly (lime folded-paper diamond body, black visor with white eyes, antenna with a lime ball, black arms and boots), re-rendered in high resolution with warm light (`mobi-greet|point|think|cheer|rest|sleepy|read`). Used at the human moments: welcome, onboarding guide moments, empty states, return after a gap, late night, celebrations. Never in the runner, never on the sealed sheet. Mobi may say one short line in a glass bubble, never evaluative of the person. Give it life with transforms only (a 420 ms settle, a hop, a small tilt toward what it points at), never an idle loop.

## 3. Colour (Night is the default; Daylight is an option in Appearance)

| Role | Night | Daylight |
| --- | --- | --- |
| Ground | `#12110E` (warm charcoal) | `#F3EFE6` (warm paper) |
| Raised | `#1B1A16` | `#FFFDF8` |
| Raised 2 | `#25231E` | `#E9E4D8` |
| Hairline | `#312E27` | `#D8D1C2` |
| Ink | `#F4F0E6` (paper white) | `#17150F` |
| Ink 2 | `#BDB6A6` | `#454036` |
| Ink 3 | `#8E877A` | `#655F53` (check 4.5:1 on each ground) |
| Lamp (environment light only) | `#F2A93B` at 10 to 22% in glows and fields | `#F2A93B` at 14% |
| Volt (action, the light) | `#D2F000`, text on volt `#0B1000` | fill `#D2F000`, volt as text `#526700` |
| Wrong | surface `#2A1614`, border `#7D3128`, text `#FFC9C2` | `#FBE9E7` / `#B93225` |
| Subject light fields (radial, behind art only) | Accountancy amber `#3B2A10`, Business Studies indigo `#14213F`, Economics teal `#0F3330`, English rose `#3A1626`, General Test moss `#22300F` | pale versions |

One accent. Gradients only as environment (light fields, scrims). No gradient text, no glow behind text, no neon on ordinary cards.

## 4. Type

- Bricolage Grotesque (bundled; the variable file is at `C:\Users\atish\AppData\Local\Temp\claude\C--Users-atish-Desktop-mockmob-copy\604ced81-3aa7-4deb-b42c-f324ca5f51e2\scratchpad\fonts\bricolage-var.ttf`, OFL licence beside it). Cut **static instances** with fontTools (`python -m pip install fonttools` if needed; `fontTools.varLib.instancer`) rather than relying on runtime variable axes: `BricolageCondensed-Bold` (wdth 75, wght 700, opsz 96) for hero numbers; `BricolageHeadline` (wdth 87, wght 650, opsz 48) for moment headlines; `BricolageTitle` (wdth 100, wght 600, opsz 24) for screen titles. Check tabular figures with fontTools; if `tnum` is missing, roll digits in fixed-width slots.
- Hanken Grotesk (already bundled) for everything you read: body 16/24, questions 17/26, labels 15/20 w600, captions 13/18 w500.
- Units beside big numbers at 55% of the number, top-aligned ("183 of 250").
- Retire Gabarito from the UI.

## 5. Material, light and the glass setting

- Live glass (BackdropFilter, grouped): the dock, the Start button, sheets and dialogs. Sigma 20 to 28, tint `#181B18` at 0.62 (Night) or white at 0.72 (Daylight), a 1 dp edge light (white 14% at the top fading to 3%), soft shadow.
- Fake glass (no live blur): cards over art use a pre-blurred slice of the art or a tinted translucent fill plus edge light and a static noise tile.
- Solid: the runner, options, explanations, lists, settings. No art behind anything a student reads.
- The lit edge: exactly one focal element per screen has a thin volt top edge (and optionally a 14% volt glow beneath, never behind text).
- **Glass quality setting** in Appearance: Full, Lite (tint plus edge, no live blur) and Off (solid). Default Full, with an automatic downgrade to Lite when frame timings (`SchedulerBinding.addTimingsCallback`) show p90 raster over 12 ms for two seconds of scrolling. This keeps the M06 smooth until the morning benchmark.

## 6. Navigation

- A split glass dock floating 10 dp above the gesture inset: a pill with three labelled tabs (**Today, Practice, Review**), and a separate 60 dp glass circle, **Start**, to its right.
- The active tab sits on a "lit tile" (white 12% fill, volt top edge) that slides on a spring (360 ms, bounce 0.18, stretches up to 1.15x with velocity). As it lands, the tab's small answer bubble fills with volt ink from the touch point. Icons are 24 dp outlines that swap to filled on activation; labels are always visible. Haptic `selectionClick` on change.
- Start morphs (container transform, 420 ms, emphasized curve) into a glass quick-start sheet: "Resume [subject] mock, 23 of 50" when one exists, "Quick 10", "Full mock", "Repair the next mistake". `lightImpact` on press.
- The avatar at the top left of each tab root opens **You**. Learn is no longer a tab: concepts appear as a "Concepts" shelf in Practice and open from the mistake they explain; while study content is switched off, the shelf is hidden (never a whole screen saying "not available").
- On scroll down the dock eases down 8 dp and scales to 0.94; it never hides on tab roots and is absent on the runner, repair and the result.

## 7. Motion and haptics

Glide (enter) `cubic-bezier(0.15, 0.5, 0.5, 1)` 300 ms; exit `cubic-bezier(0.4, 0.3, 0.8, 0.6)` 200 ms; emphasized `cubic-bezier(0.16, 1, 0.3, 1)` 420 ms; springs nearly critical (bounce at most 0.12) except the dock tile (0.18); light sweep 700 ms once; engrave (mask reveal) 280 ms; number roll 500 ms. Never moves: question text, options, the timer, explanation body, numbers after landing. Reduced motion: sweeps and dollies off, unfold becomes a 200 ms cross-fade, rolls show the final value. Haptics: `selectionClick` (tab, option, thresholds), `lightImpact` (Start, flips), `mediumImpact` (seal), success pattern only after the server acknowledges. Nothing on a wrong answer. Everything animated is transform or opacity, inside a RepaintBoundary; no saveLayer in scrolling content.

## 8. Copy

- Remove every defensive footer and caption: "MockMob is not affiliated...", "Sample questions. This is not a diagnosis.", "Practice, not proof", "Example, not your plan yet", "On this phone" on guest screens, "This only decides your data settings", cost-first headlines. The non-affiliation statement lives in You > Help > About and the Play listing.
- Voice: a sharp senior who has been through CUET. Short, specific, a little dry, in the student's words. Real dates (boards mid-February to early April 2027; CUET registration February to March 2027; the exam in May 2027; CSAS rounds after results). At most one Hinglish caption per screen, never in an instruction ("Aaj ka repair: 10 minutes, Partnership.").
- Vocabulary for mistakes: **Found, Repaired, Checked, Holds** ("Holds" only after a fresh check passes). Never "mastered" or "fixed forever".
- Sentence case, no emoji, no exclamation marks, no arrows in buttons, 12-hour time, tabular figures in data.
- Costs live on the confirm sheet, written as what you get: "10 questions, about 10 minutes. 10 credits."

## 9. Generated art (copy what you use into `flutter_app/assets/art/` as WebP)

`hero-desk` (welcome scene: a lamp-lit study desk at night with the glowing glass answer sheet and cutting chai, portrait), `mobi-greet|point|think|cheer|rest|sleepy|read` (transparent), `obj-accountancy|business|economics|english|generaltest` (subject objects in warm lamp light, transparent), `paper-tile` (charcoal embossed paper, tileable), `foil-seal` (lime and gold foil, transparent), `token-first-mock|first-repair|held` (brass milestone tokens, transparent), `empty-allclear|offline` (landscape vignettes with Mobi). If a file is missing or looks wrong, use code-drawn art and note it. Convert with Python PIL to WebP (quality 82; objects 512 px, Mobi 512 px, hero 768 x 1152 or so, paper 512 px), and keep raster art under 3 MB total. Light fields, sheets, bubbles, grids, rings, scrims, noise, the wordmark and the mark are code.

## 10. Integrity (unchanged, enforced in review)

Success, "Saved", success haptics and celebrations fire only after the server acknowledges. No invented numbers: DU figures are real CSAS 2026 data from `public/du/2026` (label "CSAS 2026, Round 1" and show the scale out of 1000 where relevant). Practice, repair, fresh check and held stay distinct states. No recovered-marks, admission-chance or "mastered" claims. Nothing decorative during a timed mock. Celebrations are proportional and never after a lower or held result. A reveal never withholds a result (tap, TalkBack action, "Open results directly", decay from the fourth sheet). No punitive streaks or random rewards. 48 dp targets, TalkBack labels, reduced motion, 4.5:1 text contrast over its worst backdrop.

## 11. Onboarding ("Your sheet", data-driven step deck, about 2 minutes)

A smoked-glass answer-sheet card at the top gathers the student's answers: each answer fills a bubble and engraves a line. Steps (each must visibly change something):
1. Cold open (first launch only): the hairline draws, the bubble mark inks, the wordmark rises. 1.4 s, tap to skip.
2. Welcome: `hero-slab` art with Mobi; headline "Every lost mark has a pattern."; support "MockMob finds yours, helps you repair it, and checks the repair holds. Two minutes to set up."; "Build my plan" (volt) and "I already have an account".
3. Stage: Class 12 writing in 2027 / passed Class 12 / Class 11 / not sure. Payoff: the weeks to the May 2027 window roll onto the sheet.
4. Course and colleges (one evolving screen): pick the course (commerce programmes from `public/du/2026`), then a ladder of colleges for it with real CSAS 2026 Round 1 minimum scores (category chip, default UR, stored on the phone), pick up to three. Payoff: the picks engrave onto the sheet.
5. Subjects and confidence: Shaky / Okay / Strong per subject, with the eligibility rule for the chosen course from `rules.json` ("This set keeps all three open"). Rows reorder weakest first.
6. Biggest worry (six options in the student's words). Payoff: the first move changes, and Mobi says one line.
7. One real question in the weakest subject (bundled pool), with the measured time on a right answer and a ten-second fix on a wrong one.
8. Rhythm: minutes (10, 20, 30), days as seven bubbles, a time window. Payoff: "That's about 120 sessions before May."
9. The plan reveal: the sheet flips; its back is the plan, revealed line by line, including one insight the student did not enter (the weakest subject's top chapter by weight from `data/cuet_chapter_priorities.json`, and "Boards end in early April. The plan goes lighter from mid-February."). "Hold to seal" with a plain "Seal it" alternative.
10. Save: "Are you 18 yet?" then "Continue with Google" (when configured), "Use an email code", "Not now". Saved state only after acknowledgment.
11. First move: the sheet flies into Today; "10 questions to your starting point" with "Start now, about 10 minutes" and "Tonight at 8:00 PM". Reminders are asked after the first check (preview of the student's own reminder, equal-weight buttons).
Answers save on the phone first and sync where the API supports them (`/api/profile`, `/api/me/goal`, `/api/me/rhythm`); fields without an endpoint stay local in a versioned store. The five-question sample stays on the website only.

## 12. The other screens

- **Today** (not a Revolut clone): top row with the avatar, the date and the week as seven bubbles; a hero "Tonight's move" with the subject's light field and object, one monumental number and its meaning, a volt pill and the lit edge; "Your sheet": the last mocks as compact bubble rows; the countdown and dream ladder; an unopened result takes over the hero as the sealed sheet; return after three or more days shows Mobi and "How long have you got tonight?" with 10, 20, 30 minute chips; a designed day-one state.
- **Runner**: calm, solid, no art. Top bar with count and timer (own RepaintBoundary), save glyph with three states, palette sheet of bubbles, 56 dp options that fill like a bubble when chosen (no correctness during a mock), leave guard ("Leave this mock?") on Android back, submit stages from real calls only.
- **Result**: concept-4. The sealed folded sheet (paper-tile, foil-seal), drag or tap to unfold with threshold haptics, bubbles ink in order, the number lands, then recap cards with a story bar: where the marks went, first thing to repair, compare with the last comparable mock, what's recorded and the next ask. Lower result: calm, no sweep. Decay and skip rules from spec 5.6.
- **Practice**: one recommended default up top (art, lit edge) plus "Choose your own" (subject, mode, length); costs on the confirm sheet; the Concepts shelf when content exists.
- **Review**: mistakes grouped by chapter with Found, Repaired, Checked, Holds; the repair flow (calm panel, worked explanation, optional 5-question retry) and its ending (bubbles inking, receipt from the acknowledgment, one Mobi hop); the repair record timeline.
- **You**: identity first (the student's sheet: target course and colleges, subjects, rhythm, the milestone token shelf), settings second (notifications, appearance with theme and glass quality, privacy, account, help and about).

## 12.1 Additions from `directions-final.md` (adopt these)

- **"Show me" tags (evidence first).** Under every claim the app makes about the student ("Accountancy first", "6 mistakes ready", "Partnership is your trap", a recap insight), a small quiet tag "Show me" opens the exact questions or attempts behind it. A claim without evidence is not shown.
- **Repair as threads.** In Review, each mistake (or repeated trap) reads as a short thread: Found (the attempt), Repaired (the repair session), Checked (the fresh check), Holds. The thread closes, with a quiet ink stroke, only when Checked; Holds appears after a later check passes.
- **Gut versus the check.** The first recap after onboarding includes a card comparing the onboarding confidence (Shaky, Okay, Strong) with what the check found, kindly and truthfully.
- **Onboarding ends on the real check.** The first move is the 10-question starting-point check; its marked result (in the result reveal) ends the first run, and reminders are asked after that result.
- **Badges:** only what is due today, at most three on screen.
- **Trap cards** (optional share): a card showing a trap question pattern and the ten-second fix, never the student's marks.
- **Calendar truth:** "expected May 2027 window" until NTA publishes dates; boards mid-February to early April.

## 13. Engineering rules for every builder

- Spine untouched: api, auth, repositories, storage, sync, the session engine, routes and providers. Replace the presentation layer.
- Each builder owns `lib/features/<feature>/**` and its tests. Core visual code (`lib/core/theme`, `lib/core/ui` or widgets, the shell and dock) is owned by the foundation step; feature builders use it and list any core change they needed.
- Memory on this PC is tight: run Flutter tests through `bash tool/flutter_locked.sh test -j 1 <paths>` and analysis through `bash tool/flutter_locked.sh analyze <paths>` (a lock so only one heavy Flutter process runs at a time). Never start an emulator; the orchestrator owns the device.
- Goldens at 360 x 780 (and 384 x 853), both themes, opened and looked at.
- Done means: analyze clean, your tests pass, your goldens viewed, and every state (loading, empty, error, offline, success, return) designed.
