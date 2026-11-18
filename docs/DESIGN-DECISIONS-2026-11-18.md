# Design decisions, 18 Nov 2026: the premium rebuild (owner LK302-LK312)

Written by the main session as the work went, so a later session can see why each thing is the way it is. Evidence tags:
O = the owner's words (ledger id), V = seen in a real browser, I = my interpretation.

## 1. "More inside MockMob" is a deck the scroll deals (LK304)
- **Task.** Show five tools in about one screen each, with no gesture a student has to discover.
- **What he had rejected, in order.** A held stage with self-playing demos and a moving chip row ("weird movements", 16 Nov);
  a vertical stack ("wastage of vertical space"); a held stage with still screens ("still not good", 17 Nov); a sideways row
  of cards ("no animation ... no one will ... understand that they have to touch it", 18 Nov) [O LK266-LK304].
- **What he pointed to.** The Mistake Lab: "animated cards and scroll animation on them" [O LK304].
- **Decision.** One held story on every pointer, built on the Lab's own ScrollStory, but where the Lab swaps scenes at a beat,
  the deck's cards follow the scroll itself: the next card rises from the pile's foot over the one on show, the passed ones
  show as edges above. The finger is always moving something, so the hold never feels like a stuck page [I]. Demos play once
  as a card comes on; taps still work but nothing depends on them.
- **Alternatives not taken.** CSS scroll-driven animations alone (no Firefox, Safari only from 26; a script fallback would be
  needed anyway); a page-level scroll snap (fights the other held stories' controller).
- **Trade-off.** The section costs about four screens of scroll on a phone, like the Lab. The tabs and the bottom bar's Skip
  are the ways past it.
- **Verified.** [V] 390 Day: eight real 380 px swipes, one card each, 0 page errors; 1440 Day. Not on a physical phone.

## 2. The pen and the highlighter (LK308)
- **Task.** Make the page feel made by hand without making it childish; give a reader's scroll something to watch.
- **Decision.** One component, `Doodle`: marks generated for the exact box of the words (a circle round "on time." and one
  round "open to you?" are the same hand at the same pen width), seeded by the words, drawn once when the words clear the
  screen's foot. It suits the product's own world (paper, ink, a marked answer sheet) better than any borrowed effect [I].
- **Rules that keep it professional.** One mark per heading; one to three words; the highlighter for what MockMob gives that
  others do not; a circle for a figure; an underline for the sentence's object; the red pen only for words about a mistake;
  never on legal lines, buttons or forms. Written into `tmp/1118/briefs/marks.md` for the public pages.
- **Where it answers an action.** The sample card's verdict (tick, red cross) and the result page's costliest chapter: the
  pen there is feedback, not decoration.
- **Alternatives not taken.** Stretched SVG templates (the wobble distorts and a dash draw breaks with non-scaling strokes);
  a hand-writing font for margin notes (a second voice on the page, and font weight; not needed).
- **Trade-off.** A marked phrase cannot wrap, so marked phrases stay short. Without script the words are simply unmarked.
- **Verified.** [V] 15 marks on the home page at 390 Day and Night and 1440 Day.

## 3. Today's streak block (LK309)
- **Task.** A student reads their streak in one look, as in Duolingo, in MockMob's own identity.
- **Decision.** The streak's mark is Mobi as he stands in the logo: asleep as an outline until today counts, lit in volt once
  it does (a real state, like Duolingo's lit and unlit flame, but ours) [I]. The number beside him; the week's seven OMR
  bubbles moved up from the sheet; a segmented bar of today's answers from the server's own figures. One small moment a day
  when today first shows as counted.
- **Kept from 17 Nov.** No guilt words, no countdown, rest passes, the whole surface opens the sheet, never a zero as a lead.
- **Trade-off.** The block is about 100 px taller on a phone.
- **Open.** Today now shows two week rows near each other (the streak's last seven days, and "This week's goal" for the
  calendar week). Merging them is a product decision; not made.
- **Verified.** [V] six fixture states at 390 Day, two at 1440 Night; `streak_1117` 27 tests and the new `todayProgress` tests.

## 4. Dropped: a real-time 3D Mobi (LK311, LK312)
- **What was tried.** Mobi modelled by script in Blender and exported to a compact mesh for a hand-written WebGL renderer, to
  stand at the sample desk and react to answers.
- **Why it stopped.** The owner saw the reference renders and called them "very bad" beside the generated Mobi art already
  on the site. A hand-built model was not going to match that art in one day [I]. Rule now: no subpar output; where 3D
  cannot be made perfect, use the image generator.
- **Kept.** Nothing in the product. The script is in `wt-1110-convert/tmp/1118/mobi3d/src` if a later session wants it.
