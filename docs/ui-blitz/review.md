# Review and repair: UI blitz spec (14 October 2026)

Track: `lib/features/review/**`. Authority: BUILD-BRIEF.md (Night Sheet), the owner's 13 October feedback, ref-high / ref-revolut / ref-fampay. Owner direction overrides the generic "no glass, gradient, glow" lines of the UI standards; everything else applies (one dominant action, real data only, every state, 48 dp targets, reduced motion).

## 1. What is wrong now (device shots r3/r4 and the old goldens)

- Review tab (`review_tab_full_night.png`): every block is a rounded dark box. Tonight's card is a box holding text, a strip of bubbles and a thread; below it three near-identical chapter boxes each holding a glyph tile, text, a second row of five pink dots and a chevron; then another box for skipped questions. Hierarchy is flat: nothing says "this is the thing to do" louder than "this is a list".
- The dots in the chapter cards are decoration: ten equal dots tell you nothing about where marks go. No scale, no comparison between chapters.
- Nested cards: chapter card > stage chip pills; repair entry > solid panel > life row; first repair card inside the ending; notice panel; retry card and concept row boxed inside the explanation.
- Chapters open with a snap (a fade, no size motion). Repair progress is a row of 12 dp dots. The life thread (Found, Repaired, Checked, Holds) is static: when a repair completes nothing travels along it.
- The ending has a handed-back sheet, a number and a hop, but no moment: no light, no ink travelling along the thread, no haptic cadence.
- Everything is the same size: no monumental number on the hero, art with no weight.

## 2. Target

One idea for the whole track: **the thread**. Every mistake walks Found, Repaired, Checked, Holds. The thread is drawn the same way on every screen (hairline between bubbles; when a stage completes the line draws in volt from the previous bubble and the next bubble inks). Stage completion is the only thing that moves with weight in the work layer.

Two layers, as in the brief: the **moment layer** (the tonight hero, repair entry, repair ending) carries art, light and a monumental number; the **work layer** (the map, the mistake panel, the record) is calm, flat, ruled by hairlines, no boxes inside boxes.

### 2.1 Review tab, top to bottom (384 px frame)

1. Header (shared `TabRootHeader`), lamp field behind the first 360 dp.
2. Unopened result: kept (fake glass row with the folded sheet).
3. **Tonight hero** (the one lit element: `LitEdge` with the volt top edge and glow). One surface, no inner boxes:
   - subject light field (code, `LightField.subject`) pooled upper right, the subject's object art 132 dp bleeding off the top right, settling in (420 ms emphasized, rises 8 dp, scale 0.94 to 1);
   - overline "Tonight's repair, Accountancy" (caption), chapter in 28/31 Bricolage, two lines max (three at large text), width held clear of the art;
   - the monumental number: tonight's mistake count (`MonumentalNumber`, 64 sp condensed, unit "mistakes", rolls 500 ms) with the source line beside it ("from Mock 2. 1 more in this chapter from earlier papers.");
   - the questions as an inline row of wrong bubbles with numbers ("Q1  Q11  Q31"), no box;
   - the stage thread (Found lit, others dashed), labels beneath;
   - the volt key (full width, 56 dp), then the "Show me" tag with Mobi pointing at the key. Late night: sleepy Mobi with the one line.
   - Motion: art settles (420), number rolls (500), Reduced motion: all at rest.
4. **Mistake map** replacing the three chapter boxes (heading "Mistakes to repair", caption "7 mistakes across 4 chapters"):
   - an open list on the ground, hairlines between chapters, no card per chapter;
   - each chapter row: subject glyph tile 40 dp, chapter (cardTitle, two lines), subject and stage words (caption), on the right the open count as a condensed figure with "to repair" under it (the repaired count in volt when nothing is open); the chevron sits at the end of the bar line;
   - under the text, a **segmented bar**: one segment per mistake, coral for open, volt for repaired, dashed ring for set aside, left aligned and **drawn at one scale for the whole map** (the width of one mistake is fixed by the chapter with the most, capped at 36 dp a segment), so bar length compares chapters honestly. Bars grow in from the left on first show (520 ms emphasized, 60 ms stagger per row), reduced motion shows them whole;
   - no separate legend: the "1 of 8 repaired" line above the map carries a bar drawn in the same segments (volt repaired, coral open, ring set aside), so it teaches the encoding;
   - tapping a chapter expands it (accordion: one open at a time) with a size and fade animation (320 ms emphasized open, 200 ms close), a selection haptic, the chevron turning, the open chapter lifting onto a `raised` fill. Inside: the mistakes as a vertical thread (rail, bubble per stage, "Question 11, found in Mock 2 on 12 October", the stage word in its own tone, no pills) and a repair key per paper.
   - "See all N chapters" quiet key stays when there are more than three.
5. Skipped questions: a flat row of the same family (hairline, count, chevron) with the same collapsible.
6. Insights rows (owned by `insights`; untouched).
7. Repair record preview: the vertical thread.
8. Past results: rows with a hairline marks bar (marks over max, real data) next to the chevron.

### 2.2 Mistakes screen
Same map, full list, first open chapter expanded. Repaired and set-aside sections use the same rows.

### 2.3 Repair entry
Moment layer: lamp field, subject light field and object art (upper right, bleeding), chapter in the moment cut, the **number** of mistakes as a monumental figure with "mistakes", then "3 mistakes, about 10 minutes. You can stop after any one." as the lead, the questions as an inline wrong-bubble row, the thread drawn flat on the ground (no panel), the credit line, Begin pinned. 

### 2.4 Repair run (work layer)
- Top bar: "1 of 3 mistakes" and Finish for now; under it a **run track**: one segment per mistake, 4 dp high, 6 dp gaps. A completed mistake fills volt left to right (420 ms emphasized) with a light haptic tick; the current segment is brighter; key-reviewed segments are ringed ink, set-aside dashed. Never colour alone: the bar sits under the live-region count.
- When the explanation lands, the **stage thread** appears above it (Found, Repaired, Checked, Holds): Found sits lit, then 160 ms later the line draws to Repaired and the bubble inks (260 ms). This is "a stage completes" made visible. Checked and Holds stay dashed (fresh checks are not available).
- The explanation, retry and concept rows lose their boxes: ruled by hairlines, the retry offer is a flat block with a secondary key.

### 2.5 Repair ending (the celebration, premium)
Choreography (full celebration mode, motion on):
- 0 ms: lamp scene up; the handed-back sheet rises 12 dp (320 ms).
- 320 ms: the rings draw on tonight's repaired bubbles one by one (1100 ms total), each with a selection tick (capped at 6).
- when the rings finish: a **foil burst** behind the number: two thin shock rings (volt, then lamp amber) and 14 small foil flecks ease out over 900 ms and fade, once. No confetti, no loop. A soft volt bloom (environment light, never behind text) rises under the number; the number rolls (500 ms); Mobi cheers (existing act); the thread draws Found to Repaired (volt, 420 ms); success haptic only after the server acknowledged (unchanged).
- the receipt and keys are already in place and stay still. A soft sweep of lamp light crosses the handed-back sheet while the last ring closes.
Off / text-only celebration and reduced motion: everything at rest, no burst, no ticks. A run with nothing repaired is calm: no burst, no number (unchanged). Nothing claims the repair holds.

### 2.6 Record screen
The vertical thread with a volt-inked rail for repaired nodes; entries keep their dated lines and life row.

## 3. Type, spacing, colour
Hero number 64 condensed, chapter 28/31 (title cut), card title 17/22 in the map, per-chapter count 28 condensed, captions 13/18. Section gap 32, row padding 16 by 14, bars 8 dp high. Colour: coral = `wrongMark`, volt = `volt` (Night) / `volt` with `voltEdge` outline (Day), set aside = `ink3` dashed ring. Volt only on: the key, repaired segments and rings, the lit edge, the burst.

## 4. Performance (budget phones)
All animation is transform, opacity or a CustomPainter repaint through an `Animation` listenable inside a `RepaintBoundary`. No BackdropFilter added. One controller per widget family (the map owns one for all bars; the burst owns one). The burst's particles are computed once in `initState` from a seeded random. Collapsibles lay their child out once and clip with `heightFactor`.

## 5. Accessibility
48 dp rows (64 on the map), `Semantics` on every row with the full spoken line, bars and the burst excluded from semantics, the run track under a live-region count, stage words never colour alone, text at 1.3x tested.

## 6. How it meets the references
HIGH: one monumental figure and object per moment, one soft light event, the work layer stays quiet. Revolut: a ruled list instead of cards, a bar per row that carries real comparison, numbers as the heroes. FamApp: a celebratory ending with a short physical foil burst and a character, restrained.
