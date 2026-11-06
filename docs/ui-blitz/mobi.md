# Mobi, alive everywhere (UI blitz, track "mobi", 14 Oct 2026)

Owner ask: Mobi animated everywhere like Duolingo's Duo, premium not gamified (HIGH, Revolut,
FamApp). Code-drawn only. Scope: `lib/core/mascot/**`, `test/golden/mascot`, `test/unit/mascot`.

## What is wrong now

- Device shots `tmp/app-shots/r4/33-real-welcome-night.png`, `02-today-top-night.png`,
  `23-ask-record-night.png`: Mobi is present but reads as a sticker. Between acts it only breathes
  and blinks on a fixed rhythm; the eyes stare dead ahead; nothing in the room affects it.
- The act set covers the onboarding beats but not the moments the screens now need: a correct
  answer in practice, a wrong one, waiting on the server or the AI, a proud milestone, listening
  while the student types a question (Ask is mostly empty), sleeping late at night.
- Acts lack anticipation and follow-through: the wave starts cold and the arm drops dead; appear
  is a plain rise; the eyes never blink on a big glance (people and Duo do).
- Expression range is narrow: open ovals, happy arcs or a flat lid. No warm "smiling eyes"
  (raised lower lid), so encouragement and pride cannot read without becoming cartoon joy.
- Taps on Mobi alternate cheer and hello; no feel of touching something physical, no haptic.
- Small sizes (Ask header, cards, list rows) pay full-detail paint cost (three strokes per limb,
  gradient hands) for detail that is sub-pixel at 48 dp. There is no head-only avatar for rows.

## Target

### Idle life (every Mobi, every screen)
- Breath: 3.0 to 3.6 s cosine breath, squash 1.4 %, rises 0.9 du; deeper and slower asleep.
- Blinks: 2 to 6 s apart with a skewed distribution, fast close (55 ms), 30 ms hold, slower open
  (110 ms); 20 % doubles; a blink also fires on any glance wider than 0.6 (saccade blink).
- Glances: every 4 to 9 s with no target, the eyes flick (stiff spring, 120 ms) to a random
  point, hold 0.6 to 1.4 s, return; sometimes a small weight shift (tilt 0.02 rad) with it.
- Fidgets (standing at ease only): every 12 to 22 s one small beat of personality, 1.3 s: a smile
  at the student (eyes come to the middle and warm, a small nod), a weight shift with a toe tap,
  or an antenna flick (a dip, the bulb flashes, a look up at it). Own random stream, scheduled.
- Attention: an on-screen tap anywhere makes Mobi glance at it for 1.1 s (global pointer route,
  no rebuilds, opt out with `watchTaps: false`). `MobiController.glance` does the same for
  content (a new row, the next button).
- All idle beats are scheduled, so the ticker still sleeps between beats (budget phones, tests).

### New acts (additions to `MobiAct`, existing values and indices unchanged)
| Act | Moment | Shape | Duration |
| --- | --- | --- | --- |
| `correct` | a right answer in practice, a repair step that held | 80 ms crouch, small hop (12 du), nod at the top, smiling eyes, one volt answer bubble inks beside the head and pops | 1.1 s |
| `encourage` | after a wrong answer, a lower result | lean in, chin-up nod, right mitten pumps once, warm smiling eyes, never a frown | 1.4 s |
| `loading` | waiting on the server or the AI (held) | mitten to chin, eyes scanning left-right, antenna bulb pulses with light, gentle sway; after 12 s it settles into `think` beats | held |
| `sleep` | 1 AM to 5 AM, dormant states (held) | slumps seated, eyes closed lines, slow deep breath, z's; a tap wakes it with a startle | held |
| `nudge` | pointing at the primary action | point stance, then two short jabs with overshoot and a lean toward the target | 1.0 s, then holds the point |
| `proud` | milestone, weekly goal met, first full mock | stretches tall (anticipation dip), mittens on hips, chin up, smiling eyes, three glints sparkle around the head | 2.2 s |
| `listen` | Ask while the student types, any input field (held) | leans 0.06 rad toward the speaker, head tilt, slightly wider eyes, a slow nod every few seconds | held |
| `wake` | a tap on a sleeping or sleepy Mobi; first open of the morning | eyes snap open wide (70 ms), a startled 9 du hop with mittens flung out and the bulb flashing, landing squash, a quick look left and right, a happy blink | 1.2 s |

### Upgrades to existing acts
- `appear`: eyes blink on (closed for 160 ms, then open), rises with stretch and lands with a
  squash, antenna whips by spring.
- `hello`: 120 ms anticipation dip and counter-lean, overshooting arm raise (easeOutBack), wave
  with body sway, follow-through on the drop (arm bounces past rest and settles).
- `celebrate`: visor glint sweep at the top of the jump, landing squash with boot spread.
- Tap: a "boop" (squash toward the touch, eyes look at the finger, happy blink) plus a light
  haptic; the third quick tap plays `cheer`; tapping a sleeping Mobi plays `wake`.
- `think` and `loading`: the mitten now really sits under the visor (hand to chin), not on the belly.

### Expression and material
- Shut eyes (asleep, the peak of a blink, before the eyes blink on) draw a soft lid line curving
  down, never a slit. Warm eyes (`smile`) are a round dome with a lower lid curving up into it and
  blunt, rounded horns: a smile with volume, distinct from the thin `happy` arc.
- `MobiEye.smile` (raised lower lid, 0 to 1) for warm looks; `MobiRig.glow` (antenna bulb light),
  `glint` (visor light sweep), `sparkle` (proud glints), `bubble` (the inked answer bubble).
- Lite paint at heights under 72 dp: one stroke per limb, cached shaders, no rim detail.
- `MobiFace`: the head only (diamond, visor, eyes, antenna) for avatars and list rows, 24 to 56 dp;
  blinks and glances, sleeps its ticker between beats.

### Motion rules
Anticipation 80 to 160 ms, action on `easeOutBack` or ballistic arcs, follow-through 150 to 300 ms;
squash never beyond 12 % (the paper body must not look rubbery). Reduced motion: every act has a
still key pose and nothing ticks; the quick per-answer reactions (`correct`, `encourage`, `wake`)
show their key pose for the act's length and then return to the stance (a timer, no frames), the
bigger moments hold their pose until the next act as before. One RepaintBoundary per Mobi; no rebuilds per frame.

### Haptics
Mobi itself only fires `selectionClick` on a tap (honours the Touch feedback switch). Moment
haptics (success after acknowledgement) stay with the screens.

## How this meets the references
- Duo: a character that reacts to what you do (right, wrong, waiting, milestones) and watches you.
- HIGH: physical, lit, playful motion with weight; the volt bubble and glints are the brand's own.
- Revolut / FamApp: restraint; reactions are short, proportional, and the work stays in front.

## For the merge (where each act goes)

All additions are in `lib/core/mascot`; nothing outside it changed. `MobiMoments.act(event)`
maps a `MobiEvent` (rightAnswer, wrongAnswer, waiting, typing, milestone, sessionDone,
showAction, allClear, setback, arrive) to its act so screens stay consistent. The enum is
`MobiEvent`, not `MobiMoment`: that name is already the Today widget
(`features/today/widgets/mobi_moment.dart`) and the clash broke `move_hero.dart`.

| Where | What to call |
| --- | --- |
| Practice question, right answer (practice only, never a timed mock) | `controller.play(MobiAct.correct)` on a small Mobi or `MobiFace` beside the feedback |
| Practice question, wrong answer; lower result on the recap | `controller.play(MobiAct.encourage)` with a factual line |
| Ask screen while the AI answers; any "Saving..." or loading Mobi state | `play(MobiAct.loading)`; then `play(MobiAct.idle)` or the answer's act when it lands |
| Ask screen while the student types (focus on the field) | `play(MobiAct.listen)`; `controller.glanceAtWidget(fieldKey)` on each new suggestion chip |
| Ask thread: Mobi's lines | `MobiFace(size: 32 to 40)` as the avatar; `MobiFace(entrance: MobiAct.correct)` etc. per line |
| Today hero / empty states pointing at the one action | `controller.pointAtWidget(ctaKey)` then `play(MobiAct.nudge)` once after 1.2 s of no input |
| Milestones: repair held, weekly goal met, first full mock (after server ack) | `play(MobiAct.proud)` with the success haptic from the screen |
| Session finished (after ack) | `MobiAct.cheer`; full result above the last one: `MobiAct.celebrate` |
| Welcome, return after a gap | `MobiAct.hello` (now with anticipation and follow-through) |
| Any entrance at night | `entrance: MobiMoments.entranceAt(DateTime.now())` (sleepy from 11 PM, asleep 1 to 5 AM; a tap wakes it) |
| Morning: first open after a sleeping Mobi was shown, or a tap on it | `play(MobiAct.wake)` (taps do this by themselves on an `interactive` Mobi) |
| Lists, small headers, rows | `MobiFace` (head only, lite) or `MobiCharacter(lite: true)` / `Mobi` at under 72 dp |

Notes:
- `MobiCharacter.watchTaps` (default true) makes every on-screen Mobi glance at taps. Pass
  `false` where Mobi sits in a scrolling list of many items.
- `MobiAct.loading` ticks continuously for up to 12 s, then settles. Tests that `pumpAndSettle`
  with a loading Mobi on screen take 12 s of fake time; that is expected.
- `widgets/mobi.dart` (not owned here) may add `MobiPose.proud/encourage/listen` mapping to the
  new acts and pass `lite: size < 72`; the `Mobi` wrapper still compiles unchanged.
- `core/widgets/lab/lab_mobi.dart` lists `MobiAct.values` as chips, so the lab golden
  (`test/golden/core/mobi_states_golden_test.dart`: `mobi_*`, `state_error_*`) gains eight chips
  and shifts; regenerate it at the merge. Its tests otherwise pass.
- Goldens elsewhere that show a think Mobi now show the mitten under the visor.
- Goldens elsewhere that show a hello, cheer, think or celebrate Mobi will shift slightly (glow
  on the bulb when thinking or cheering, new eye transitions); regenerate them at the merge.

## Status (14 Oct, ui/mobi)

Done and verified: every act above, fidgets, attention, boop and wake, `MobiFace`, lite paint,
`MobiEvent`/`MobiMoments`. `flutter analyze lib` clean; `test/unit/mascot` and
`test/golden/mascot` pass (77 tests); the Mobi-using unit tests elsewhere (core_ui, onboarding,
practice, review) pass. Contact sheets: `test/golden/mascot/goldens/mobi_new_acts_*`,
`mobi_close_ups_*`, `mobi_expressions_*`, `mobi_faces_*`, `mobi_frames_*` (correct, encourage,
proud, nudge then loading then sleep, wake, appear then hello, fidgets).

Not mine, seen while verifying: `flutter analyze test` reports errors in tests from the earlier
round-2 WIP commit (`api_client_test.dart`, `sheet_sync_test.dart`, fakes missing the new
`expectUserId` parameter in notifications, rhythm and you tests).
