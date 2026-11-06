# Runner (practice and Full mock) - UI blitz spec

Branch `ui/runner`. Owns `flutter_app/lib/features/runner/**` except `nta/**`. NTA mode keeps its exam skin untouched. Logic, session engine, routes, saving and submit calls are untouched: this is a presentation and interaction upgrade.

## 1. What is wrong now (device shots `tmp/app-shots/r4/09, 10, 11`, goldens `practice_q19_360_night`, `submit_ready_night`, `submit_received_night`)

1. **Nothing is alive.** Moving to the next question swaps the whole body in one frame. The count "19 of 20" changes by a hard cut. The progress strip is a row of ten-dp dots that never move; the current ring teleports. Choosing an answer inks one bubble and nothing else on the screen reacts.
2. **Four identical dark boxes.** The options are four equal rounded rectangles with a small ring on the left. The selected one is distinguished by a 1.5 dp lighter border and a bubble. There is no weight, no hierarchy between the chosen answer and the three others, and no sense of marking a sheet.
3. **The question is small.** 17 sp in a column of 328 dp with a large empty lower third. The screen reads like a form, not an exam paper you are concentrating on.
4. **The track is information-poor.** Marked questions do not show on it, and it cannot say "you have answered 14 of 20".
5. **The palette sheet is a wall of 50 identical bubbles** with a legend that repeats the counts. It does not help the one decision the student makes there: where do I go next.
6. **The submit page is a status report, then dead air.** "Submit now?" over a card, 220 dp of black, a plain button. On receive the only change is a check and a lit warm patch: no moment, no Mobi, nothing that tells the student that the thing they just did mattered. It also offers no way to go straight to the questions that are still empty (the one thing someone about to submit wants).
7. **The timer is just digits.** Under five minutes only the colour changes.

## 2. Principles

- The runner is still the **work layer**: solid surfaces, no art behind anything read, nothing moves under the student's eyes while they think (question text, options and the timer never reflow). All new motion is transform or opacity inside a RepaintBoundary and answers an action or shows a state.
- The **moment layer** starts where the work ends: the submit page and the handoff to the result.
- One volt light per resting screen: the primary key. Volt also appears for a moment (the lock-in spark) and cools into ink.
- No correctness while answering. The session payload has no answer key (marking is server-side after submit), so per-question correct and incorrect moments cannot exist here, and must not be faked. What this track upgrades instead is everything the student actually feels in the runner: locking in an answer, moving, progress, the palette, the hand-in and the receipt. Correct and incorrect reveal belongs to the result screens (other track).
- Reduced motion: no flights, no glides, no sweeps, no stagger; states change instantly (or a 120 ms fade where an element appears).
- Haptics: `selectionClick` on lock-in (existing), jump and track taps; nothing on Next, Previous or marks (inside a timed paper only the tick speaks); `success` only after the server acknowledges the submit (existing); nothing on wrong answers (none exist here).
- Budget phones: no BackdropFilter added; one small CustomPaint per moving thing; the lock-in flight is a single 6 dp dot on a short bezier inside its own RepaintBoundary overlay; the track repaints only on its own controller.

## 3. Screen: the question (`RunnerLayout`)

```
 [x]   19 of 20                          [ 2x2  Questions ]      top bar 60 dp (unchanged geometry)
 Accountancy, Admission of a partner            (ok) Saved       meta line, 2 lines reserved
 o o o o o o o o o o o o o o o o o o (o) o                       track 48 dp: glides, inks, notches
                                              [flag Mark]        mark toggle row
 A and B share profits in the ratio 3:2. C ...   20/29 w600      the question, bigger
 [ A  5:3:2                                  ]                   options 60 dp
 [ B  3:2:1                                  ]
 ...
 [ Previous ]  [          Next            ]                       bottom bar
```

### 3.1 Count and timer (top bar)
- The count "19 of 20" stays Bricolage condensed 30 sp. On a change the old number slides up 10 dp and fades while the new one rises in from below (180 ms, glide curve; direction follows travel: forward rises, back drops). Never a roll from zero. Reduced motion: instant.
- Timer (mock): same digits, never moves. Under 5:00 the digits take the warning colour (as now) and a 3 dp bar appears under them, full at 5:00 and draining over exactly those five minutes (the only span whose length is known; built as an underline, not a ring, so nothing is added beside the digits and nothing shifts). Under 1:00 the bar and digits turn the strong warning ink. No pulsing.

### 3.2 Progress track (`TimingTrack`)
- Bubbles (short papers) and timing marks (long papers) keep their geometry, hit boxes and TalkBack cells exactly.
- **The current ring glides.** It travels from the old cell to the new on the dock's 360 ms spring (bounce 0.12), stretching 1.25x along its path at speed, so moving through questions reads as one ring travelling a sheet.
- **Answered cells ink.** A newly answered cell is flooded by a volt spark (radius 0 to the bubble over 220 ms from the centre) that cools to paper ink over 420 ms; the final resting state is solid paper ink: **one answered state across the runner** (track, palette and submit sheet all draw the same solid ink disc, number in the ground colour on the palette). Volt is only the lock-in moment and the received sheet.
- **Marked cells notch.** A marked-for-review question shows a small ink pennant (6.8 dp wide) above its bubble (reviewable in `practice_marked_360_*`) (and a taller timing mark with a cap on long papers). Fixes the old gap where marks were invisible on the track.
- **Bubbles scale with the room**: 15 dp on a short practice, about 12 dp on twenty on a 360 dp phone, never under 10 (the pitch is capped at 24 dp). Cells on this phone only keep their palette treatment: a hollow ink dot (never orange), named in the palette legend as "On this phone N" while any exist. A flag is only ever a mark for review.
- **Milestone sweep.** When the answered count first reaches half the paper, and again when every question is answered, one soft light band crosses the track (700 ms, sweep curve, once per threshold per visit). No haptic, no sound.

### 3.3 The lock-in (`AnswerOption`, `LockFlight`)
- A press sinks the row to 0.985 on the snappy spring (transform only; layout never changes) and darkens the fill to raised 2.
- On selection: the lettered bubble inks volt from the touch point (existing, 260 ms), the option is a row of the OMR sheet, not a box: no border and no fill, hairline rules between rows, bubble column on the left, unchosen rows keep full ink text (nothing dims). The chosen row is the only lit thing: a flat volt wash at 9% bleeds out of the bubble across the row (clipped circle growing from the bubble centre to the far corner, 320 ms, emphasized curve; no gradient). Text goes to weight 600.
- The three other rows go to ink 2 text (still above 4.5:1) so the chosen row is the only one at full ink.
- A 6 dp volt dot lifts off the bubble and flies to the track cell of this question on a short curve (280 ms, glide), leaving a fading 14 dp tail; on landing the cell sparks (3.2). The dot never blocks input. Changing an answer flies again; clearing an answer does not.
- Haptic: one `selectionClick` at the tap (existing behaviour, host-owned).

### 3.4 Question to question (`QuestionEnter`)
- The new question enters over 260 ms: the question text rises 10 dp and fades in with a 0 ms delay, each option follows 35 ms later than the one above (transform and opacity only), travelling from the side it came from (forward from the right by 14 dp, back from the left). The scroll position resets as it does now. Selecting an answer on the same question never replays it. Reduced motion: no motion, content is there at once.
- Passage questions: the passage well enters with the question text.

### 3.5 Question typography and the mark toggle
- Question text 19/28, weight 600 Hanken (was 17/26 w500): the screen's hero. Body of a question (when present) stays 16/24. Options 16/24 at w500.
- Mark for review stays a labelled toggle; on mark the flag pops (scale 0.8 to 1 on the snappy spring) and the track notches at once.

### 3.6 Bottom bar
- Previous (glass pill) and Next (volt) stay; the label switches Next to Review and submit with a 160 ms cross-fade. When every question is answered the primary key carries the lit glow beneath it, the one resting emphasis on the screen.

## 4. Screen: the answer sheet palette (`PaletteSheet`)
- The question sits at the top and the options rest at the foot of the region (next to the thumb), so a short question leaves air between them, not a dead lower third. "Clear my answer" is a 48 dp secondary key under the options.
- Header: monumental "14 of 50 answered" (Bricolage condensed 40 sp, unit at 55%) in place of a legend of four counts; below it a one-line legend of the four mark shapes (answered, not answered, not visited, marked) with counts, as chips kept for TalkBack parity.
- A **jump row**: "Go to first not answered, question 9" as a secondary key (only when one exists), and "Review and submit" stays pinned in the footer. This is the decision the student is making.
- Cells pop in as a wave on open (scale 0.84 to 1 and fade, 12 ms stagger per cell, 260 ms each, capped at 420 ms total); the current question's ring draws. Reduced motion: none.
- Bubble geometry, semantics, 52 dp rows unchanged.

## 5. Screen: submit (`SubmitPage`, practice and Full mock only)
- Title "Submit now?" (or "Time is up." as now). Under it the sheet card: monumental "45 of 50 answered", then **the sheet**: the answered bubbles drawn in the one answered ink (calm), not-answered as dashed rings, marked as ringed dots, numbered. Marked and not-answered counts below as a ledger: each count is a 32 sp numeral with its words, and the whole row (64 dp tall, chevron) is the key that takes the student back to the first such question and closes the page ("5 not answered" over "Go to question 9"). A count of zero is not shown.
- Primary key "Submit mock" or "Submit practice". The line "You cannot change answers after you submit." sits above the key, quiet, so the confirm reads as one decision.
- **Sending** (the real call): a band of lamp light travels the sheet continuously (1.4 s per pass, indeterminate by design, never a percentage). The light lives in the marks, not in a panel over them: each answered bubble warms and swells 0.8 dp as the band passes it (smooth bell, 70 dp wide), with a soft halo; no hard-edged rectangle. Button shows loading. Mobi is not shown.
- **Received** (only on the server's 200, as now): the bubbles ink volt in question order across 900 ms with the lit edge on the card (the truth is the metaphor: the sheet is paper ink until the server holds it, volt once it does); the existing `success` haptic fires at the start of the ink; the warm lamp comes up behind (existing); Mobi waits in a fixed 160 dp slot under the sheet (so nothing shifts) and hops in as the ink finishes (the living vector Mobi, 104 dp); the receipt line slides in 120 ms after the ink finishes. The hand-off to the result is unchanged (2.8 s, or the tap).
- Pending, window closed, rejected: no light, no Mobi, sheet card unlit (existing logic), unchanged copy.

## 6. Leave guard
Unchanged geometry and copy; the sheet enters on the shared emphasized curve (existing).

## 7. Hierarchy and states checklist
| State | Treatment |
| --- | --- |
| First question, nothing answered | Practice note under the track ("Marks come after you submit."), Previous disabled |
| Answered / changed | Lock-in per 3.3; clear answer removes the wash and the track ink |
| Marked | Flag toggled, track notch |
| Answers held by network / not saved | Meta line states as now |
| Away (returned after a gap) | Glass strip over the meta line as now |
| 5 and 1 minute warnings | Warning words on the meta line as now, ring on the timer per 3.1 |
| Passage question | Passage well enters with the question |
| Large text 1.5x to 2x | All new motion is transform only; the track and top bar clamp as now; options grow |
| Reduced motion | Everything instant per section 2 |
| Day theme | All washes and sparks use token colours; volt-as-text rule respected (volt is fill only) |

## 8. How it meets the references
- **HIGH**: heavy condensed numerals as the anchor of the screen; one lit light; motion that has weight and direction (the ring travelling, the dot flying to the sheet) instead of fades.
- **Revolut**: the input becomes the object (the option's bubble becomes the mark on the sheet), digits that slide, a hand-in that turns into a receipt.
- **FamApp / Fampay**: tactile, physical keys; the sheet as the central object; playful but not gamified.
- **Duolingo's Duo** (via Mobi): Mobi appears only at the human moment (hand-in received) and cheers; absent while the student works.

## 9. Verification plan
Goldens (360x780 and 384x853, night and day) for: first question, answered with a marked cell, the selected-option lock-in at rest, practice 19 of 20, large text, passage, offline, warning, palette, submit idle, submit sending, submit received (after the ink), leave guard. Unit tests cover: the track painter (settled state), count flip and enter widgets under reduced motion, the lock-in flight overlay lifecycle (appears and is removed), palette jump row, submit jump-to-first-unanswered, and that nothing new appears in NTA.


## 10. Findings kept for the merge (checked, not assumed)
- The session payload carries no answer key (`SessionQuestion`: "Answer keys are never in this view"), so a per-question correct or incorrect moment cannot be real. The owner's request for practice feedback moments is met where the truth exists: the lock-in, the track, the palette, the hand-in and the receipt. Correct and incorrect reveals belong to the practice result screens (not this track).
- BUILD-BRIEF section 2: Mobi is never in the runner. He appears on the submit page only once the server holds the sheet (moment layer).
- Motion frames are goldens (`goldens/motion_*.png`, fake clock) so the choreography is reviewable, not only the rest states.
