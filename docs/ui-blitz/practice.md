# UI blitz: practice track (14 Oct 2026)

Owner: practice track agent, branch `ui/practice`. Scope: `flutter_app/lib/features/practice/**`, its goldens and unit tests. The quick-start sheet lives in `lib/core/router/quick_start.dart` (core, not this track): this track builds the new chooser as a self-contained widget in `features/practice/widgets/choice_deck.dart` and the merge step points the sheet at it (see "For the merge").

Authority: `design-2026-10-13/BUILD-BRIEF.md`, owner feedback 1110 ("Even after we finish it, there's no such animation", "starting from business studies ... redirecting me to the accounting page"), ref-high / ref-revolut / ref-fampay, and the owner's UI standards (his MockMob direction overrides the generic no-glow and no-gradient lines). Palette unchanged: volt is the only accent, lamp amber is environment only, subject light fields behind art only.

## 1. What is wrong now (device shots r3 / r4)

- `r4/04-quickstart-night.png`: "Pick today's work" is five identical 68 dp boxes, each a 40 dp icon tile, a title and a grey sentence. The lit edge on the first row is the only hint of a recommendation; Quick 10 and "Ask your record" carry the same weight. No motion beyond Mobi settling.
- `r3/09-practice-tab-night.png`, `r3/10-practice-scroll-night.png`: after the suggestion and the subject tiles, five modes sit as equal rows on one panel (icon, title, line, chevron). Full mock and NTA mode (the serious, exam-shaped choices) look exactly like Quick practice. The page reads as a settings list.
- `r3/11-practice-setup-night.png`, `r3/13-practice-setup-bst-night.png`: the confirm sheet names the subject in a 24 sp title and the length on a generic segmented control. Nothing on the sheet shows which subject's paper this is beyond one word, and the length is four numbers on a track. The owner's "it starts in Accountancy when I picked Business Studies" bug was fixed in logic, but nothing makes the choice visibly honoured.
- `r3/20-practice-finish-sheet-night.png`, `r3/21-practice-result-night.png`: the finish moment is bubbles inking and Mobi typing. The number counts up but never lands; there is no beat where the paper is "in". The owner asked twice for a finishing animation.
- "Finish for now" ends on one receipt line on an empty screen for 1.6 s.

## 2. Target design

Shared vocabulary for this track:

| Token | Value |
| --- | --- |
| Enter | glide `Cubic(0.15, 0.5, 0.5, 1)`, 300 ms, rise 12 dp plus fade, stagger 40 ms per tile |
| Landing | emphasized `Cubic(0.16, 1, 0.3, 1)`, 420 ms |
| Press | `MmPressable` spring to 0.97 (tiles) / 0.96 (chips), no tap delay |
| Glyph gesture | 640 ms, `Curves.easeInOutCubic`, plays on press and once on entrance for the leading choice; ends where it began so a skipped frame never leaves a glyph half drawn |
| Haptics | `selection` on choosing a subject, a length stop (and each stop crossed while dragging); `light` on committing a choice; `medium` when the finish number stamps down; `success` only for a good or great set, and only on the fresh open after the server's acknowledgement |
| Reduced motion | no rise, no stagger, no glyph gestures, no burst or sweep; numbers show final values; the stamp is an instant change |
| Performance | transforms and opacity only; every glyph and the burst are one `CustomPainter` each inside a `RepaintBoundary`; paths built once per size; no `BackdropFilter` added; no `saveLayer` in scrolling content |

### 2.1 Animated choice glyphs (`widgets/choice_glyphs.dart`)

Code-drawn vector glyphs replacing the Lucide icons and the 40 dp boxes, each with one gesture:

- Quick: a lightning bolt; on press it flashes volt and throws three spark ticks.
- By chapter: an open book; the right page turns over and settles.
- Smart: three rings closing in on a wrong bubble, the outer ring drawing in volt.
- Full mock: a stopwatch; the crown dips and the hand sweeps a full turn.
- NTA mode: the exam's 3 by 3 palette in its own colours; the cells fill one by one.
- Repair: a wrong bubble; a volt ring draws around it.
- Ask: a speech bubble whose three dots hop in turn.
- Resume: five bubbles; the next hollow one inks.

Drawn on a soft disc (raised 2 with a hairline) at 44 dp in tiles, 56 dp in the leading choice where the disc carries a volt rim.

### 2.2 Choice deck (`widgets/choice_deck.dart`), used by the tab and the quick-start sheet

Rows of three kinds, so hierarchy comes from shape and size, not colour:

- **Lead** (the recommended choice, quick-start only): full width, min 136 dp, raised surface with the lit edge and its glow, a lamp pool behind the 56 dp glyph, title in Bricolage headline 26/29, note in body ink 2, facts as quiet chips, and a 52 dp volt go disc bottom right (play glyph, `voltInk`). Its glyph plays once 260 ms after the sheet lands.
- **Pair**: two tiles side by side, equal height (intrinsic), min 128 dp: glyph top left, title (Hanken 16 w700) and a two-line note at the bottom. Tags ("Pro") sit beside the title.
- **Wide**: one tile across, glyph left, title and note right, facts chips below (NTA: 50 questions, 60 minutes, Question palette, Mark for review).
- **Quiet**: the tertiary choice (Ask your record): no fill, hairline only, 60 dp.

States: rest, pressed (scale 0.97, fill brightens 4%, glyph plays), focused (focus ring from `MmPressable`), disabled (not used: a Pro-gated mode stays tappable and says so on the confirm sheet), loading (rows are drawn from data the screen already has; nothing waits).

### 2.3 Practice tab

1. Header (unchanged), offline and stale-subject banners (unchanged).
2. Suggestion hero (the one lit element, unchanged logic).
3. "Choose your own" with Edit subjects.
4. Subject tiles, upgraded: the chosen tile lifts 4 dp, its object scales to 1.06 on the settle spring, its light field brightens, and an identity bar in the subject's accent (a lighter tone of its own light field) runs under the name. On press the object dips to 0.94. Identity accents never act as buttons or text colours on their own; the volt bubble still marks the choice.
5. A subject line that honours the choice: the subject's glyph chip and "Practising in Business Studies", cross-fading (200 ms) when the subject changes.
6. The modes as a deck: Pair (Quick practice, By chapter), Wide (Smart practice), then an "Exam conditions" band: Pair (Full mock, NTA mode with its facts) on a sunken band with a hairline. No lead on this screen: the suggestion is already the lead.
7. Explore and plan, Concepts shelf (unchanged).

### 2.4 Confirm sheet and setup page (the composer)

- **Ticket header**: the subject's object (64 dp) in its light, the mode as eyebrow, the subject as the title; on the right the length as a monumental number ("10" with "questions" beneath) that rolls when the length changes. Mocks show 50 and the minutes. Changing subject swaps the object with a 300 ms slide and fade, so the choice is seen, not just read.
- **Subject chips** (setup page only, which can change subject): a horizontal strip of chips, each the subject's line glyph on its light tile, the name, and on the chosen chip an accent underline plus the volt bubble. 48 dp tall, `selection` haptic.
- **Length dial** replacing the segmented control: four stops across a sunken track. Each stop is its number (Bricolage 22) over a small sheet of bubbles sized to the length (5 = one row of five, 20 = four rows), so the control shows how much paper you are taking. The chosen stop sits on a raised thumb that glides on the emphasized curve and its bubbles ink volt with a 18 ms stagger; drag across the track to scrub, with a `selection` tick at each stop. Each stop is a 64 dp button with selected semantics.
- Difficulty, what-you-get panel, mock lines and keys: unchanged logic; the panel keeps its numbers from the quote.

### 2.5 The finish moment (fresh open after the server acknowledged)

| t (ms) | Beat |
| --- | --- |
| 0 to 200 | The sheet card is in place with hollow bubbles numbered 1 to n under them (painted). The figure reads 0. |
| 200 to 1000 | Bubbles ink in order (40 ms apart, 800 ms cap). The figure counts up with each right bubble. |
| 1000 to 1420 | **Stamp**: the figure scales from 1.14 to 1 on the emphasized curve while an ink ring expands from behind it and fades; `medium` haptic. |
| 1000 to 1700 | Good or great only: 14 volt shards burst from the figure (one painter, 700 ms) and a light band sweeps the sheet once; `success` haptic. Mixed, blank and low sets get the stamp only, calm. |
| 1260 | Mobi reacts (cheer, celebrate, point at the first wrong bubble, read or think), says one line. |

Tap anywhere skips to the end. Reopened results and reduced motion show the end state at once. The figure text is the only text node with the count (tests rely on it).

### 2.6 Finish for now

Instead of a lone receipt line: Mobi waves (hello act) above a filed-sheet card; a volt check draws itself in a ring (420 ms), then the receipt line ("Practice recorded at 11:51 PM.") engraves in. Today takes over after the same 1.6 s.

## 3. How this meets the references

- HIGH: display type is huge or absent (the ticket number, the finish figure); loud art at the top, quiet rows below; reward moments get a capsule-and-foil ceremony, here the stamp and the burst, rationed to real good results.
- Revolut: first the object, then the details (subject object leads the ticket, then the controls); digits animate when a value changes; enter 300 ms ease-out, exit 200 ms.
- FamPay: point-of-action facts as chips with real numbers; success moment with rings and shards under one second, only after the server confirms; subject objects as identity instead of identical rows.
- Owner standards: one dominant action per screen (the suggestion on the tab, Start on the sheet, Repair on the result), no nested cards (the exam band is a background change, not a card around cards), 48 dp targets, every state named, reduced motion honoured.

## 4. Verification plan

Goldens at 384 x 853 night and day for the tab, the confirm sheet, the setup page, the finish frames and a new chooser golden; unit tests for the dial's semantics and the deck's ordering; `flutter analyze` on `lib/features/practice` and the tests.

## 5. Build status (14 Oct, second builder)

Built and verified with goldens (384 x 853, night and day) and unit tests:

- Choice deck with code-drawn glyphs and press gestures; quick-start deck (lead, pairs, wide, quiet). Goldens `quick_start_deck_*`, `quick_start_deck_resume_*`, `quick_start_deck_pressed_*`.
- Practice tab: subject tiles lift with identity bars, the "In <subject>" line, the mode deck, and the exam band as a ground change only (its outline was removed so it no longer reads as a card around cards).
- Composer (confirm sheet and setup page): ticket header, subject chips, length dial. The dial's height now follows the text size (it overflowed by 0.9 dp at 1.3x text).
- Start screen ("Getting your questions ready"): the same ticket rises in under Mobi once the selection is known, so the subject and length chosen are seen while the questions come. Golden `start_ready_*`.
- Finish moment: stamp, ring, burst and sweep. New goldens `finish_stamp_mixed_*` (ring only, 1150 ms) and `finish_stamp_great_*` (burst, 1250 ms).
- Finish for now (2.6): `ResultClosing` files the student's own sheet under a volt seal (ring and check draw in), Mobi waves, the receipt line engraves in; 900 ms inside the existing 1.6 s. Goldens `closing_350ms_*`, `closing_1000ms_*`.
- Tests: `test/unit/practice/choice_and_dial_test.dart` (deck arrangement, a glyph per id, tap haptic, reduced motion, dial semantics, tap and drag ticks, 1.3x text fit, closing). Four existing tests now find the length stops inside `LengthDial` instead of `MmSegmented<int>` (intended: the control was replaced; every assertion is unchanged).

## 5b. Design review pass (14 Oct, third pass)

Applied from the review of the second build; goldens re-rendered and opened (night and day).

- Glyphs are now objects, not line icons (`choice_glyphs.dart`): a solid bolt, an answer sheet part inked, an open book with a ribbon, a target with a wrong bubble at its heart, a stopwatch with a dark face, the NTA palette on its panel, a wrong bubble with a volt ring, a speech bubble. Lit top left to shaded bottom right, a soft drop, drawn in a 24-unit box so one vector serves 40 dp rows and the 104 dp lead. The ghost watermarks are gone (they ran under the copy).
- Deck roles are visibly different (`choice_deck.dart`): the lead is a hero (104 dp lit object, its own lamp pool and a volt wash, 30 sp title, go disc); pairs are borderless tonal tiles with a 72 dp object; a wide row is a ruled list row with a chevron and no card; quiet stays an outline. `solid` is removed; `ChoiceDeck.onSheet` steps tiles to the sunken tone on the quick-start sheet so they hold on Daylight.
- The exam band is a full-bleed sunken ground ruled top and bottom (`ChoiceDeck.bleed` takes the page gutter), no rounded container; the tiles inside are borderless.
- Ticket (`composer_ticket.dart`): a real ticket shape (`TicketBorder`, one path from the card minus two notches), dashed perforation, the subject object at 96 dp (72 dp from 1.2x text) in its own light, the length rolling on the stub. The subject name wraps between words and steps down rather than being cut. The start screen uses the ticket as its own card. On a mock the Difficulty control follows "What you get" instead of sitting under the ticket.
- Length dial: stops are taller with 28 sp numbers, empty bubbles are full-strength ink 3 rings (3:1 or better), bubbles are larger.
- Subject chips fade out where more chips wait past an edge.
- Finish: the figure has clearance above and below, "of 10" sits clear of the digit, and a good set bursts with 24 larger shards, dark-cored bubbles, two rings and a volt flash.
- Finish for now: the filed sheet is a real card (score, numbered bubbles) under a seal centred on its top edge, with the counts line and the receipt below; `NumberedSheet` is shared with the finish moment.
- Not done here: the quick-start sheet is still wired in `lib/core/router/quick_start.dart` (core), so the device shows the old list until the merge in section 6. No emulator run yet.

## 6. For the merge

- `lib/core/router/quick_start.dart` (core, not this track): replace the Column of `QuickStartRow`s with `QuickStartDeck(options: [...])` from `features/practice/widgets/quick_start_deck.dart`, building `ChoiceOption(id:, glyph: QuickStartDeck.glyphFor(id), title:, note:, onTap:)` in the same order and under the same conditions. Ids: `resume`, `quick`, `mock`, `nta`, `repair`, `ask` (Ask is drawn quiet; the deck is drawn `onSheet`). Pass `noteLines: 2` for the resume option (its count arrives late). The first option leads, so the `lit:` logic goes. Tests in core that look up `QuickStartRow` or the key `quick-start-resume` need the deck's keys (`choice-<id>`).
- `test/golden/core/sheets_golden_test.dart` and `buttons_golden_test.dart` render the quick-start sheet; their goldens change once the sheet uses the deck.
- No files outside `lib/features/practice/**`, `test/golden/practice`, `test/unit/practice` and this doc were edited.
