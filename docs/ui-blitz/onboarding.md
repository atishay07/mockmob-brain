# UI blitz: onboarding ("Your sheet")

14 October 2026. Track owner: the onboarding builder (branch `ui/onboarding`). Scope: `flutter_app/lib/features/onboarding/**` and its tests. Authority: BUILD-BRIEF section 11 and directions-final A.6 and A.8, with the owner's 11:10 feedback (onboarding at most 60 percent; Mobi alive like Duo; no pasted pictures) and his references (HIGH, Revolut, FamApp). Palette, fonts and core widgets are unchanged; every data path, validation and saved field stays as it is.

## 1. What is wrong now

Evidence: the committed goldens (`test/golden/onboarding/goldens/*_night.png`, 384 x 853) and the device shots in `tmp/app-shots/r4` (`33-real-welcome-night.png`).

1. **Every step is the same list of rounded boxes.** Stage (`stage_class12_night`) and worry (`worry_night`) are four and six identical 56 dp rows with A/B/C letters, the generic "form" look the owner called basic. Nothing about the answer is shown in the answer: the stage rows do not say what each choice means for the student (the weeks), the worry rows have no picture of the worry.
2. **No choreography.** A step change is a 16 dp sideways slide and fade of the whole body (`_StepSwitcher`). Headline, support, answers and the key arrive as one block; nothing builds. The sheet above does ink its bubble, but silently (no haptic, no light), so progress does not feel like filling a sheet.
3. **The sheet card reads as another card.** A dark rounded box with seven circles. No OMR detail (timing marks, printed rows), so it does not read as the student's answer sheet.
4. **Course and ladder are rows, not a ladder.** `course_ladder_night`: selected colleges are boxed rows with a 6 dp dot; the pick order is invisible, there is no rail, and the scores carry no visual weight.
5. **Subjects stack nested boxes.** `subjects_night`: each subject is a bordered card containing a bordered segmented control (a card in a card).
6. **The warm-up question has no moment.** A right answer prints one line of text; the measured time, which is the payoff, is body text.
7. **Pace is a form.** `rhythm_night`: a segmented control, a row of bubbles, a number, then four text chips. The time of day has no picture.
8. **The plan reveal is a text box.** `plan_night`: a long card of numbered body lines, then "Hold to seal" and "Seal it" as two equal grey pills. The climax of the flow looks like a terms page; holding gives a thin trace and a fill, no build-up, no stamp.
9. **Mobi is small and stays in the corner.** 64 dp in the top bar; he points at the sheet, but he does not react to the student's taps.

## 2. Principles for this pass

- **The sheet builds up.** One object across the flow: each answer inks a bubble on the sheet with a lit burst and a light tap, and Mobi points at it. The step body enters in a fixed order: headline, support, answers, key. Leaving is quick and goes up; a back step goes down.
- **The answer shows its meaning.** A choice tile carries the fact the choice changes: weeks to CUET on the stage tiles, the college count and the shape of the ladder on the course tiles, the pick order on the ladder, minutes as big figures.
- **One dominant action per step.** The key at the foot stays the only volt surface besides inked bubbles. The plan step's dominant action is the hold.
- **Mobi reacts.** He glances at every tile the student touches, says one line on arrival, points at each new bubble, cheers a right answer, shrugs at a trap, celebrates the seal.
- **Weight, not bounce.** Glide, emphasized and a near-critical spring for presses; one overshoot curve, used only for headline words and the seal stamp.
- **Budget phones.** Transform and opacity only; one ticker per step entrance; headline words drawn from one cached layout; no BackdropFilter added; reduced motion shows every end state at once.

## 3. Motion vocabulary (onboarding)

| Name | What | Curve and duration |
| --- | --- | --- |
| Rise | Headline words rise 0.45 em, turned 6 degrees, into place | `Cubic(0.3, 1.35, 0.46, 1)`, 520 ms, 30 ms per word, start 40 ms |
| Lift | Support line, each answer, the key: 14 dp up, 0.97 to 1 scale, fade | glide `Cubic(0.15, 0.5, 0.5, 1)`, 340 ms; support at 160 ms, answers from 220 ms, 45 ms apart (capped at 8), key at 300 ms |
| Leave | The outgoing step: 12 dp up (down when going back) and fade | exit `Cubic(0.4, 0.3, 0.8, 0.6)`, 200 ms |
| Ink | A bubble fills from the touch point | glide, 260 ms (core Bubble) |
| Burst | A volt ring around a newly inked sheet bubble: 1x to 2.4x, fades out | `Motion.out`, 520 ms, once |
| Press | Any tile: 0.97 on a near-critical spring | core MmPressable |
| Roll | Weeks, sessions, measured seconds | core MonumentalNumber, 500 ms |
| Flip | The sheet turns over to the plan | emphasized, 640 ms; light tap at the halfway point |
| Print | Plan rows: the row bubble inks, then the line engraves | 160 ms apart; a selection tick per row |
| Charge | Hold to seal: the seal ring fills, the sheet sinks to 0.985, the edge light traces | linear 1.2 s; selection ticks at one third and two thirds; medium impact on completion |
| Stamp | The foil seal lands: 1.35x to 1 with a ring wave, sheet rebounds | `Cubic(0.3, 1.35, 0.46, 1)`, 420 ms |

Haptics: `selectionClick` on every choice; `lightImpact` when a sheet bubble inks and at the flip; `mediumImpact` when the seal lands. Nothing on a wrong answer. Reduced motion: no rise, lift, burst or flip (cross-fade 200 ms); the stamp appears; numbers show their final value; every text payoff stays.

## 4. Per screen

### Welcome
- Layout unchanged (the owner did not object to it): the code-drawn lamp-lit desk, Mobi waving on the desk with his line, the moment headline, support, the volt key, "I already have an account".
- New: the entrance is choreographed. The headline rises word by word at 200 ms (after Mobi's wave starts), support lifts at 420 ms, the key lifts at 520 ms. The return state keeps its bubble row and line.

### Step frame (every deck step)
- Top bar: back (48 dp), Mobi 72 dp standing on the sheet's top edge with his bubble beside him, skip on the right when allowed.
- The answer sheet: smoked glass with OMR timing marks (short ink bars) down the left edge, "Your sheet" and "n of 7", the bubble track with labels, the weeks (stage step) and the newest engraved line. A newly inked bubble bursts once (volt ring) and taps lightly.
- The body: headline in the headline role (28 sp Bricolage), support in ink 2, then the answers, then the key pinned at the foot with a 32 dp fade above it. Entrance as section 3.

### Stage: "Which CUET are you writing?"
- A two by two grid of tall tiles (min 128 dp). Each tile leads with the real number of weeks to that student's CUET window in condensed figures (29 for the 2027 choices, 81 for Class 11, "29?" style is avoided: "Not sure" shows the 2027 count with "probably" in the caption), the unit "weeks" at 55 percent, and the choice in label type beneath. An answer bubble sits in the corner and inks on choice; the chosen tile takes the paper rim and lit top edge; the others stay at full contrast (no dimming of readable text).
- Payoff: the sheet's weeks roll (existing), Mobi points at the CUET bubble.

### Course: "Which seat are you after?"
- Course tiles keep the real college count, and add a code-drawn ladder glyph: the course's top seven closing scores as seven hairline rungs whose length follows the score between 800 and 1000, so a steep, crowded course reads differently from a short one. Selected: inked bubble and rim.
- "Not sure yet" stays as a quiet full-width row under the grid.

### Colleges: "Which colleges would you say yes to tomorrow?"
- A real ladder: a vertical rail runs through the bubbles, each college is a rung with its score in condensed figures at the right. A pick inks its bubble with the pick number (1, 2, 3) in voltInk, so the order is visible. Picked rungs take the raised fill; others are flat on the ground, with no box. The category chip and "Any college is fine" stay above; the bar line stays below and engraves when it changes. Second pass: a picked rung no longer takes the tile's edge light (three lit rungs in a row read as a stack of boxes); the raised fill and the numbered bubble carry the pick.

### Subjects: "Your subjects. How solid is each, honestly?"
- The eligibility line stays on top. Included subjects are one surface each (no inner box): the subject object on its lamp light, the name, and a three-bubble confidence row (Shaky, Okay, Strong) drawn like an OMR question: three labelled bubbles, the chosen one inked. 48 dp targets; TalkBack reads "How solid is Accountancy, Shaky, selected". Rows still reorder weakest first on the spring (FlipItem).
- Common picks below as flat rows with a hollow bubble; "Add a subject" keeps the picker.

### Worry: "Where do your marks actually go?"
- A two-column grid of tiles. Each worry has a glyph in a lamp-lit medallion (knew it: a crossed bubble, drawn in code; time: timer; numericals: calculator; passages: open book; syllabus: layers; no idea: question circle), the worry in the student's words below. The chosen tile inks its bubble and takes the rim; Mobi thinks, then says the short line and points at the Marks bubble (existing cue).

### The warm-up question
- Calm work layer: no lamp scene, no art. A small live clock beside the subject and chapter shows the measured seconds (its own repaint boundary; it stops on answer).
- Right: the right option inks with the lit edge; under the options, a result row: the measured seconds as a monumental number that rolls, "seconds. Right." beside it. Mobi cheers. Second pass: under it, a pace line from nothing to two minutes with a tick at exam pace ("Exam pace, about a minute", the same figure the first-move framing already uses); the volt mark travels out to the student's time on the glide in 500 ms (the number roll's length) and inks the line behind it. TalkBack reads "Right, in 41 seconds. Inside exam pace, about a minute a question." Reduced motion draws it landed.
- Wrong: the wrong option shows the wrong surface and crossed bubble, the right one inks; "That's the trap. The ten-second fix" with the fix on a solid panel. Mobi shrugs. No haptic.

### Pace: "Pick a pace you can keep."
- Minutes: three large bubbles (64 dp) with 10, 20, 30 in condensed figures inside; the chosen one is inked volt with the figure in voltInk. "min" under the row.
- Days: the seven bubbles (existing), "Dotted days are rest days."
- Sessions: the monumental number rolls on every change, with the explanation beside it.
- Time of day: a two by two grid of tiles with a sky glyph (sunrise, sun, moon, moon and stars), the label and the time.

### The plan (the big moment)
- The sheet flips over (640 ms, a light tap at the halfway point) and its back is the plan. On the back: the overline, the headline in the moment role ("Week one starts with Partnership."), the start date, then the rows. Each row prints in turn: its row bubble inks, then its line engraves, 160 ms apart, a selection tick per row. The lamp pools behind the card.
- The foot: the hold. A wide volt-rimmed pill, "Hold to seal", with the foil seal medallion at its left end. While held: the pill fills with volt from the left, the label switches to "Keep holding", the light traces the sheet's edge, the sheet sinks to 0.985, and selection ticks land at one third and two thirds. Letting go drains it in 220 ms. On completion: medium impact, the seal stamps into the sheet's corner with a ring wave, the sheet rebounds, Mobi celebrates and says "Sealed. It's yours." "Seal it" sits beside the hold in the same row (the plain alternative, a full target), and "Change something" under them.

### Save: "Keep your sheet."
- The sealed sheet with its seal; the age question as three answer chips; the account keys appear after age, as now. Entrance as section 3. Saved is only said after the server acknowledges (unchanged).

### First move
- Mobi at 120 dp says his line and points at the start key (existing). The hero card keeps the monumental 10. Entrance as section 3.
- New (second pass): the lower half of the screen was an empty void (`first_move_night`). Under the hero, flat on the ground (no card), "Your first week": the next seven days from today read off the student's own pace, a ring per study day, the rest mark per rest day, today ringed and labelled, with "20 min, around 8:00 PM" beside the title. Nothing is inked because nothing is done yet. It lifts in after the hero. TalkBack reads it as one sentence ("Your first week: Wednesday, Thursday and Saturday, 20 minutes around 8:00 PM.").

## 5. States kept

Loading (the welcome key waits for the stored sheet), unreadable or newer sheet (notice and Try again), offline on save, Google in the browser, the skip dotted bubble, the three-college cap line, the five-subject cap line, no seats for a category, the not-offered subjects in the picker, the practice-only first move, small (360 x 640) and large text (1.3x). All existing tests' contracts stay: the texts they find, the hold behaviour (1.2 s, early release drains), "Seal it" in the same row at 48 dp or more.

## 6. How it meets the references

- HIGH: monumental condensed numbers inside choices, the word-by-word headline rise with a small overshoot, a foil moment for the seal, the dark lamp-lit room.
- Revolut: one task per screen with immediate micro-feedback (the weeks, the ladder, the sessions, the measured seconds); the entry UI becomes the result (the sheet flips into the plan).
- FamApp: personality spent on choices that make the plan feel owned (the sheet, the seal, Mobi), a single illustration and claim per screen, no tutorial carousel.

## 6.1 Second pass (14 October, after the usage-limit cut)

The first builder's WIP compiled and analyzed clean; the goldens in that commit were partly stale (worry, rhythm and others rendered before the code changed). This pass re-rendered every golden, looked at each, and fixed what showed:
- Figures and pick numbers on an inked (volt) bubble were drawn in the Daylight ground colour on Daylight (the 20 in the minutes bubble, plan row numbers, ladder pick numbers): near-invisible on volt. Volt ink is the same in both themes, so they are voltInk in both.
- Course tiles: the skyline mapped scores 750 to 1000, so every course's bars looked the same height. It now maps 800 to 1000 with wider, taller bars, so a steep course and a short one read differently.
- First move: "Your first week" fills the empty lower half with the student's own week (section 4).
- Warm-up: the pace line (section 4).

## 6.2 Third pass (14 October, after the design review)

Done: the welcome is Mobi first (about half the room, the desk reduced to one row of inking bubbles, no paper sheet); choice tiles lose the rim and the empty radio, a chosen tile takes a flat lamp wash and an inked tick; the stage step gains a drawn road (one tick per week, May 2027 and May 2028 marked, the chosen window lit); subjects are bare rows with hairlines and a lamp wash only when on the sheet; the college ladder has no filled rungs, only the rail, hairlines and inked numbered bubbles; the plan sheet is ruled like a form with a 36 px headline; first-week rest days are a short bar, study days volt rings, today a filled disc; the pace step has 32 dp between sections and 44 dp time medallions; below 680 dp the sheet drops its weeks and engraved line (TalkBack still reads it).

Not done, with reasons: the resting breath and blink already exist in `MobiSim` (the goldens are stills, so they cannot show it) and that code is outside this track; the sheet-into-Today handoff needs the shell and Today; splitting the pace step into two needs a deck change; the top-bar Mobi stays 64 dp because the bar is 56 dp.

## 7. Acceptance

Goldens for every step in both themes at 384 x 853, 360 x 780, 360 x 640 and 1.3x text, opened and compared with the previous ones; the onboarding unit tests; `flutter analyze` on the feature.
