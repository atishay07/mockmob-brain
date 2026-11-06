# Web D (round 6, 3 Nov 2026): cards worth looking at, a desktop that uses its space, a subtle Night (LK39, LK41, LK43)

Branch web/1103-cards (off origin/main 2152e0b74). Spec: R6-SPEC.md "Web D". Owner's words: OWNER-FEEDBACK-2026-10-31-LEARN.md, 2 Nov.
He: the cards are "very boring" in Light and Dark; "everything is very scaled down ... so much white space ... on the desktop";
Night has "neon light around every card ... a bit too much ... less of a very extreme neon AI slop look". Refine, don't rebuild;
never cut; Night stays subtle; he judges it live (dev-server config `r6-cards`, port 3463).

## What the before shots show (tmp/learn-1103/r6-d/before, 390 and 1440, Night and Day)

- **A card is a grey rectangle with words in it.** The kind ("Definition") is 13 px grey text in the corner, the same weight as the
  source line at the foot; nothing tells one kind of card from another, and nothing says "this is a card you hold". On the back the
  NCERT line floats in the middle of a big empty face. Feed (CardFace) and run (CardItem) cards look the same; the covers and the
  Cards view rows use the same flat grey label.
- **Night's rim.** Every surface (stage card, peek, covers, single-question cards, options, rail keys) carries a 1 px
  `--a-line-strong` (#384736) border, lighter than both the card (#131a16) and the ground (#0b100e). Repeated on every box, the
  light green-grey outline reads as a glow ring: his "neon light around every card".
- **Desktop is a phone layout centred.** At 1440 x 900 the feed's stage is a 680 px column with a 360 px card and 32-40 px words;
  the run is 240 | 640 | 72 with the card's words at 32-40 px; questions are 23 px stems and 17 px options; the covers are four
  ~270 px tiles with a 22 px hook. 300-400 px of the width and a third of the height are empty.

## Direction, in plain words

**A Key card is an index card with a coloured tab.** The kind hangs from the card's top edge as a small tab in one of four
colours the app already has, by what the card is for:

| family | kinds | colour (Night / Day) |
| --- | --- | --- |
| Meaning | Definition, Term, Word, One word, Idiom, Usage | volt text / dark lime (`--a-accent-text`) |
| Rule | Formula, Rule, Entry / Journal entry | lilac / plum (`--a-purple-text`) |
| Parts | List, Steps, Types, Difference | amber / brown (`--a-warn-text`) |
| Fact | Fact, Key line, Quote, Example | the cool blue Key cards already had (W-013) |

The tab is words on a tinted wash (never colour alone), sentence case, hung like DESIGN.md's flag tabs (corners rounded only at
the bottom). The card's top hairline takes a trace of the same colour, so the tab reads as part of the card. Under it: the prompt
in confident display type (unchanged on phones, bigger on a computer), and the source as a quiet footer under a hairline, like the
foot of a printed card. The back keeps the asked line small at the top and NCERT's own words in the reading face with the book rule.
The grain stays (DESIGN.md allows texture inside the card; no gradient, no glow).

**Night keeps one soft edge.** The full light rim goes: cards, covers and options in Night take the quiet `--a-line` hairline with
a faint top light (an inset 1 px highlight) and the existing dark drop shadow. Day keeps its borders (they read as paper edges).

**A computer gets a bigger stage.** From 1360 px wide: the feed's stage column 680 -> 800 px (panel 240 -> 264), the run's
640 -> 800 px (panel 240 -> 264), cards at least 420-460 px tall where the height allows, the words up a step (front 40/32/26 ->
48/38/30, question stem 23 -> 26, options 17 -> 18.5, the back's NCERT line 20 -> 22). From 1600 px a little more. Explore's covers
show three larger covers and a peek per row from 1040 px of row (was four), with a bigger hook. The Cards view's column 680 -> 780
with the front at 18 px. Phones keep their layout; only the tab, the footer rule and Night's edge change there.

## What this is not

No new kinds of decoration: no illustrations, no gradients, no glow, no coloured side bars (the owner's standards ban coloured
borders over 1 px), no new motion. Nothing removed: every label, key, count and line stays. The kind words are the same words.

## Plan (each step its own design commit on web/1103-cards)

1. `kindFamily(kind)` in `src/components/keycards/kinds.js` (tested) and the family colours as tokens in keycards.css
   (`[data-family]` sets `--kc-fam`), Night and Day.
2. Feed card (`stage/CardFace.jsx`, `stage.css`): `data-family` on the card box, the tab, the top hairline, the footer rule;
   the peek cap edge follows. CardFace Front's `card?.texHtml?.front` path untouched.
3. Run card (`run/RunParts.jsx` CardItem, `run.css`): the same tab, edge and footer.
4. Night's soft edge on stage and run cards, the peek, the options and the covers.
5. Desktop scale-up: stage.css and run.css from 1360 and 1600; the question type with it.
6. Explore covers (`feed/coverModel.js` passes the hook's kind; `ExploreCovers.jsx`, `covers.css`): the hook's tab, three
   bigger covers per row on a computer, Night edge.
7. Cards view (`cards/CardList.jsx`, `cards.css`): the row's kind as the same family tab (inline), the wider column.
8. After shots with the same script (`scripts/design-audit/learn-r6-d-cards-capture.mjs`), look at every one, fix, re-shoot;
   `npm run test:learn`, `test:keycards-ui`, `test:app`.

## Result (3 Nov 2026, built on web/1103-cards, not pushed, not deployed)

Shots: before `tmp/learn-1103/r6-d/before/`, after `tmp/learn-1103/r6-d/after/` (32 each: d01-d08 at 390 and 1440, Night and
Day; INDEX.md and console-errors.txt beside them). Made with `scripts/design-audit/learn-r6-d-cards-capture.mjs` against
`next dev` on 3463 with the preview decks (decks=real), never production.

- Feed card (CardFace) and run card (CardItem): the kind tab in its family colour, the coloured top hairline, the source footer
  under a hairline; Night's light rim replaced by the quiet hairline and one top light; from 1360 px the stage is 256 | 800 | 72
  (feed) and 256 | 800 | 72 (run), cards at least 440-460 px, front 48/38/30 px, NCERT line 22 px. CardFace's
  `card?.texHtml?.front` path is unchanged (the Front component and the `html` prop untouched); the run's typeset Formula card
  checked in the browser (Mathematics, Probability), the Cards view's five typeset fronts too.
- The feed's peek edge takes the next card's family colour on its top hairline.
- Questions (feed and run): from 1360 px stem 26 px, options 18.5 px at 64 px; Night options take the quiet hairline.
- Explore covers: the hook card's kind tab (the server already sends the hook's kind; coverModel passes it as `cardKind`), the
  family top hairline, Night's soft edge, three bigger covers per row from 1040 px of row (four from 1400), hook 31/27/23 px.
- Cards view: each row's kind as its family tag; Night's open row without the light rim; from 1360 px a 780 px column, 18 px fronts.
- Tests: `npm run test:learn` 404/404, `test:keycards-ui` 40/40, `test:keycards` 124/124, `test:app` 987 pass 0 fail
  (2 skipped), `keycards_tex` 42/42; new test in coverModel.test.mjs (the hook's kind, every kind's family).

Seen, not in this packet's scope (reported, not changed):
- Some Assertion-Reason questions show their stored letter inside the option text after the option shuffle ("A  D Assertion false
  but Reason true", Admission of a Partner, feed item 5): the options' own "A/B/C/D" prefixes survived into the text.
- Explore's single-question cards and its selects still carry Night's light rim (they are DiscoveryFeed's, not the covers).
