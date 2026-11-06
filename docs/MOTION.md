# MockMob motion system (round 4, 3 October 2026)

Motion is decided by surface and frequency, never switched off wholesale. Three tiers:

| Tier | Where | Budget | Rule |
| --- | --- | --- | --- |
| Storytelling | Homepage, public pages | Longer, may have character | Pip, reveals, hero depth, demo clocks. Pause offscreen. |
| Selection | Arena pages outside the timed runner (Practice setup, Today, Review, Saved, Progress, Explore, Result…) | Entrances 380–460 ms, UI ≤ 200 ms | Every page opens the same way; choices give press/selection feedback; exam-day card keeps its tilt, blink and live clock. |
| Answering | `/test` runner (both skins) | Near zero | Shell fades 120 ms. No travel, no mascot, question-progress fill is instant (it moves on every Save & Next). |

## Tokens

Global (`src/app/globals.css :root`): `--ease-out` cubic-bezier(0.23, 1, 0.32, 1), `--ease-in-out`
cubic-bezier(0.77, 0, 0.175, 1), `--ease-drawer` cubic-bezier(0.32, 0.72, 0, 1), `--dur-press` 140 ms,
`--dur-ui` 200 ms, `--dur-enter` 420 ms. Existing surface tokens stay: `--a-ease` (Arena) and `--ease`
(landing) are cubic-bezier(0.16, 1, 0.3, 1). Never `ease-in` on UI, never `scale(0)`, never `transition: all`.

## Vocabulary

| Moment | Motion | Values | Notes |
| --- | --- | --- | --- |
| Arena entry (layout mount) | Shell fade, rail stagger | fade 220 ms; nav links 380 ms `--a-ease`, 22 ms stagger | Shell and page `.view` containers fade only: a transformed ancestor re-anchors fixed children (sidebar, phone dock, modals). |
| Page open | Head rise, stat stagger, step stagger | `.pr-head` 420 ms, `.pr-stats > div` +45 ms each, `.pr-steps` +60 ms each, 10 px rise | Shared by every page using `ArenaHead`. |
| Press | scale 0.94–0.97 | 120–160 ms `--ease-out` | Palette cells, buttons. |
| Hover | colour, small lift | ≤ 200 ms | Moving hovers only inside `(hover: hover) and (pointer: fine)`. |
| Exam-day card | idle tilt 1.2°, straighten on hover/choice; palette blink; live clock | 350 ms; blink 5 s loop paused offscreen; stepped 240 ms seconds tick | `NtaConsolePreview` sets `data-awake` only while on screen and the tab is visible. |
| Demo exam clock | counts down after first answer | 1 s steps, icon tick | Stops offscreen/hidden; resets with the preview. |
| Pip handoff (Round 5, refined Round 6) | continuous reserved desktop lane; local phone arrival | Exponential positional settling, 65 ms time constant; phone arrival at most 8 px; single-face opacity entry 140 ms; blink 190 ms | Ordered anchor midpoints + 32 px hysteresis. Small positional corrections under 18 px retain the station expression. Large travel uses attentive. Pointing faces inward. Phones track the document exactly. RAF stops when settled. |
| Pip reactions | hop, jump (peak, once), nod | 560 / 760 / 420 ms | Event-driven (`pip:react`), coalesced by station. Eureka waits for the visible next-move control and visible settled Pip; once per page view. No repeated nod during a held reaction. |
| Empty / error / loading state | Pip settles once | 420 ms | Then still. |
| Disclosure | native `<details>` | instant | Height animation was not worth the layout cost here. |

## Reduced motion

Fewer and gentler, not none. Arena entrances become a 160 ms fade; exam-day tilt, blink and clock
stop; Pip's guide does not mount, so every perch shows its static pose. The demo clock stays at 60:00.
Verified in real Chrome with `reducedMotion: 'reduce'` (see ROUND4-NOTES.md).

## Round 6 intent rules

Open-eyed attentive is the resting state during reading, setup, review, pricing and loading.
The closed-eyed idle and winking thinking assets remain in the library but are no longer used
as scroll/setup defaults. Greeting belongs at arrival/departure. Pointing needs a destination:
the right gutter points left, including the static reduced-motion fallback. Correct sample
answers retain a hop; an incorrect answer receives a short attentive nod, never shame or sleep.
Keyboard sample answers advance normally without triggering the decorative reaction. The Lab
next-move peak retains its once-per-page latch. Pip is absent from timed answering.
See `CLAUDE-PIP-PREPOS-HANDOFF-2026-10-03.md` for the current verification and source map.

## What was wrong (round 3) and the fix

- `arena-support.css` set `animation: none` on `.view`, removed the exam-day console transform and
  palette blink. Cause of the suppression was real (transformed shell vs fixed phone dock), the cure
  was too broad. Now containers fade, leaves rise.
- Seven `transition: all` rules in `globals.css` named their properties.
- Four ungated moving hovers gated to fine pointers.
- `pr-nta-blink` animated `box-shadow` per frame; now transform only.
