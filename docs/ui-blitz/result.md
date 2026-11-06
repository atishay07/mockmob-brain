# UI blitz, result track: the marking and the recap

14 October 2026. Owner of this track: `lib/features/result/**`, `test/golden/result`, `test/unit/result`.
Authority: `docs/brain/design-2026-10-13/BUILD-BRIEF.md` (sections 7, 10, 12 "Result"), the owner's
11:10 feedback ("even after we finish it, there's no such animation"), and the references (HIGH:
reveals with weight and stagger; Revolut: "first the card, then the details", the input becomes
the result; FamApp: the success moment states a real fact).

## 1. What is wrong now (device shots `tmp/app-shots/r4`, `r3`)

- `r4/12-recap-1`: the open sheet is right, but the reveal is a uniform left-to-right ink with a
  diagonal sheen. Nothing reads the sheet; the counts under it are a plain legend that is simply
  there. The figure rolls, but nothing connects it to the bubbles.
- `r4/13-recap-2`: "Where the marks went" is a 20 dp stacked bar and four identical list rows. It
  is a spreadsheet. The arithmetic is right, the picture is not.
- `r4/14-recap-3`, `17-mock2-recap-card3`: a headline, a pill, a paragraph, then six identical grey
  boxes and an empty lower half. No figure, no sense of how much this chapter matters.
- `r4/15-recap-4`: Mobi, a nested panel, then nothing. No artefact to keep or share.
- Between cards: a 24 dp fade-rise. Every card arrives the same way; the story bar just swaps colours.
- Full result (`r3/40`): the figure is small, the breakdown is the same bar.

## 2. Target, per screen

Type: `moment` 36/38 for headlines, `figureHero`/`figure`/`figureCompact` condensed for numbers
with units at 55%, Hanken for everything read. Spacing on the 4 dp grid; 20 dp card gutter.
One volt focal element per card. All numbers come from `RecapModel` / `MarkBreakdown`.

### Card 1, the marking (sealed sheet, unfold, read, land)
- **Arrival.** The folded sheet is set down on the desk: 28 dp rise, -1.5 deg to 0 rotation,
  opacity 0 to 1, 560 ms emphasized. The headline engraves (clip left to right, 280 ms) after
  160 ms. The tab and "Open without the reveal" are live from the first frame.
- **Unfold.** Unchanged physics (drag 1:1 over 180 dp, ticks at 25/50/75%, open haptic).
- **The read.** After the flap lands, a reader line (1.5 dp volt hairline with a 40 dp warm trail
  above it) passes down the sheet like the OMR machine. As it crosses each row, that row inks left
  to right (about 130 ms per row). 900 ms for a 50-question sheet.
- **The tally.** Under the sheet, three counts (correct, wrong, not attempted), each led by its own
  bubble, count up with the bubbles that have actually inked. They end on the real counts.
- **The figure.** As the read finishes, the marks roll in on the flap (500 ms) and a 4 dp marks bar
  under it fills to marks / max (emphasized, 600 ms). Then one warm light sweep crosses the sheet.
- **Lower or held, reduced motion:** no read, no sweep, no roll: the sheet is simply complete
  (200 ms fade). Never celebrate a lower result.
- Haptics: light on tap-open, selection at drag thresholds, medium when the sheet opens. Nothing
  during the read (the read is not an interaction).

### Card 2, where the marks went (the flow)
- Headline and lead stay. The bar becomes a **flow**: on the left a column of all the paper's marks
  (`250`), and four ribbons fanning to the right into where they went: Scored (volt, solid), Taken
  off by wrong answers (coral, hatched), Not earned on wrong answers (coral outline), Not earned
  on blank answers (grey, dotted). Each destination carries its number big (`115` condensed 30
  with "marks" at 55%), its label and its "5 for each of 15" detail. Zero parts keep their row,
  drawn as a hairline, so the rows always add up to the whole.
- Proportional: ribbon widths are exact shares; each destination row is at least as tall as its
  label (measured with the student's text size), so nothing overlaps at 1.3x.
- Motion: the column grows down (300 ms), the ribbons draw left to right staggered 90 ms per part
  (500 ms each, emphasized), each label rises 12 dp and fades as its ribbon arrives. Reduced
  motion: drawn complete.
- "Show the arithmetic" stays.

### Card 3, the first thing to fix (editorial)
- Subject light pooled top right (environment only).
- Headline "Start with Admission of a partner", Show me.
- **The cost figure:** `34` condensed with "of the 135 marks you missed" beside it, and a 6 dp
  meter of the missed marks with this chapter's share lit (coral for wrong-led, grey for blanks).
  Both from the observed counts: wrong x 6 + blank x 5, the same rule as "Why this?".
- The four counts stay (questions, correct, wrong, not attempted).
- **The chapter strip:** this chapter's questions printed as a strip of the answer sheet (charcoal
  paper, question numbers above big bubbles), each bubble a 48 dp control opening that answer.
  Replaces the identical grey boxes.

### Card 4, the record and the next ask
- Headline, receipt line, Mobi (one per recap), the repair panel as before.
- **Your sheet, to keep:** a quiet "Share your sheet" key opens a preview of a share card: the
  student's answer sheet drawn as answered (volt) and left (hollow), the mock and the date, the
  wordmark. Private by default like the other share cards: no marks, no right or wrong, no chapters.

### Between cards
- Forward: the leaving card sinks (scale 0.96, fade, 200 ms exit curve) while the arriving card
  rises 40 dp and fades in (420 ms emphasized). Back reverses the direction.
- The story bar's active segment fills left to right over 420 ms when its card arrives (position,
  not a timer).

### Full result
- The figure at `figureHero`, the breakdown as the same flow (static), so the recap and the record
  agree visually.

## 3. Performance and accessibility
- Every animated piece is one CustomPainter or a transform/opacity inside a RepaintBoundary.
  The read line repaints only its own layer; the grid repaints through its existing listenable.
  No BackdropFilter added. No saveLayer in scrolling content. Paths cached per size.
- TalkBack hears the marks at once (existing announcement); the tally, the flow and the strip
  carry full-text semantics. 48 dp targets on every bubble control. Reduced motion shows final
  states. Text at 1.3x: flow rows grow to their measured labels.

## 4. States
Loading (skeleton), error and offline (StateView), held (no figure, card 2 skipped), keys
unavailable (banner), lower (calm), first mock (no score celebration), all correct (flow with one
part), all blank, finish ("in your record" line, then Today).

## 5. Build status (14 October, second builder)

Built and rendered (goldens in `flutter_app/test/golden/result/goldens`):
- Card 1: arrival, stamped seal, engraved headline, reader line with row-by-row ink, tally that
  counts what has inked, marks meter under the figure, light sweep. Calm path unchanged.
  Fix: the ink now completes on the last row where the reader ends (row span = bubble + 6 dp).
- Card 2: the marks flow (column, four ribbons, rows sized to their words). Draw starts at 260 ms,
  after the headline and lead have landed.
- Card 3: cost figure and meter; the chapter strip is now printed paper with a paper map on top
  (all questions as ticks, this chapter's answers to look at raised: wrong in coral, blank as an
  open dash) and six 72 dp tiles (32 dp bubbles, 4 dp apart, each at least 48 dp wide).
- Card 4: "Share your sheet" is a keepsake row (the student's sheet in miniature, answered inked,
  blanks open) that opens the share preview. Copy: "Your answers as a card. No marks on it."
- Between and within cards: the card stack transition (rise 40 / sink 0.96), plus every card's
  blocks arriving in reading order (16 dp rise, 55 ms stagger, 480 ms emphasized; spacers not
  animated; semantics always present; reduced motion shows all at once). Story bar fill per card,
  one selection tick when a card snaps in.
- Full result: figure at figureHero with the marks meter under it; the breakdown is the flow.
- Goldens now pump real frames in `_open` (2400 ms default), so typed and staggered motion is
  captured as it plays on a phone.

## 6. Design review round (14 October, third pass)

Applied after the review of 814a76a:
- Card 3: the cost figure is the hero (`figureHero`, 10 dp meter); the four counts are one line;
  "See the 6 questions" and "Why this?" share one row; the answer strip is printed paper nearly
  edge to edge (8 dp gutters) with a 44 dp paper map and 84 dp tiles over 40 dp bubbles; Mobi
  thinks, then points at the strip (`RecapMobi`, `lookAt`).
- "Show me" pill with dots removed everywhere in the result: `EvidenceLink`, a text action with
  an arrow that names what it opens. "Show the arithmetic" is the same kind of text action.
- Full result: one way back into the recap ("Continue recap" while unfinished, "Replay recap"
  in the bar once finished).
- Card 2 flow: outlined full-height source column with a 0 and total scale; one visual language
  (solid bands, lime / coral / grey, "not earned" lighter with a rim; no hatch or dots); a
  destination block is at least 12 dp tall, the column keeps the true share.
- Card 4: the repair panel is flat rows with one hairline, the lengths are one connected
  segmented row; the sheet keepsake is a 116 by 108 dp sheet; Mobi (120 dp) rests on the floor of
  the card above the keys with one plain line of text, no chat bubble. Cheers only for a higher
  result. Receipt: "Saved to your record at 10:44 PM."
- Card 1: the body of the sheet meets the flap along the crease with square corners (one sheet,
  no inner rounded panel); Mobi reads the sheet in the space above it (not after a lower or held
  result; one cheer after the figure lands for a higher one).
- `RecapCardPage.anchored` rests a block on the floor of a card; `RecapBleed` marks a block that
  runs nearly edge to edge.
- Goldens: 1.3x text for cards 2 and 3 added (`large13_card2_night`, `large13_card3_night`).

Not done: the reveal's ink and tally motion are unverified on a device (stills cannot show it).
