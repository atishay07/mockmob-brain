# UI blitz, art track: the subject emblem set

14 October 2026. Branch `ui/art`. Owner ask: "subject art for every subject", no pasted AI pictures, HIGH, Revolut and FamApp as the bar.

## What is wrong now

- Subjects are shown two ways that do not belong together. Large: the lamp-lit raster objects (`assets/art/obj-*.webp`, see `tmp/app-shots/r3/09-practice-tab-night.png`: a red book for Accountancy, a rubber stamp for Business Studies, a kitchen scale with an onion for Economics). Small: stock Lucide line icons (`lib/core/widgets/art/subject_glyph.dart`). The renders read as pasted pictures, several do not say their subject (the owner: "around C it makes a bit of sense; I don't know if everyone makes as much sense"), and they turn to mud under 56 dp. The Lucide row reads as a generic template.
- Nothing ties a subject to the app's own idea, the answer sheet. Every subject card is a dark box with a photo in it (`r3/02-today-top-night.png`, the Today move card shows Mobi but no subject identity at all).
- No subject art moves. Nothing reacts when a student picks a subject.

## The system: "form ink"

Real OMR sheets are printed in a drop-out ink the scanner ignores, so only the student's marks count. Each emblem is a small piece of that sheet:

1. **The tile.** A continuous-corner square (radius 30% of size) in the subject's light field (brief section 3), lit like the desk: a 168 degree two-stop body, a lamp-amber pool at the upper left, a 1 dp edge light along the top, a soft contact shadow. Optional (`framed: false`) when the emblem sits on its own art.
2. **The printed grid.** Answer bubbles, row numbers and the OMR timing track printed in the subject's form ink at 16 to 26%, fading toward the object. Only at 40 dp and up.
3. **The object.** One folded-paper object per subject in three tones (lit paper, shade, deep form ink), lit from the upper left, every main plane split by a crease like Mobi's folded body and the result's folded sheet. No outlines, no gradients on the object beyond the fold, no clip-art strokes.
4. **The mark.** Exactly one volt bubble per emblem, placed where it means something: the equilibrium point on the supply and demand cross, the nucleus, the rising bubble in the flask, the ballot's filled choice, the missing cell of the reasoning grid, the summit on the map, the inked total in the ledger. Volt stays the only bright thing.

Level of detail (optical sizes, as type families do): **glyph** under 40 dp (silhouette, the mark, nothing else), **tile** 40 to 95 dp (grid, fold, main details), **plate** 96 dp and up (timing track, hairline highlights, fine rules).

| Subject | Object | The volt mark |
| --- | --- | --- |
| Accountancy | A ledger sheet with a T account behind a calculator | The equals key |
| Business Studies | A briefcase with a folded plan in the lid | The clasp |
| Economics | Supply and demand curves on graph paper | The equilibrium point |
| English | An open book with a fountain pen nib | The ink at the nib |
| General Test | A three by three pattern grid | The missing answer |
| Mathematics | A protractor with a set square | The compass point at the centre |
| Physics | An atom, three orbits | The nucleus, with an electron travelling |
| Chemistry | A conical flask, liquid in form ink | The rising bubble |
| Biology | A leaf folded on its midrib | A cell on the leaf |
| History | A columned hall with a pediment | The medallion |
| Political Science | A ballot box with the paper going in | The filled choice on the ballot |
| Geography | A map folded in three panels, contour lines | The summit |
| Psychology | A head in profile with a spiral of thought | The centre of the spiral |
| Sociology | Three people whose heads are a row of bubbles | One head, inked |
| Computer Science | A code window with brackets | The first title-bar bubble, a blinking cursor |

Form inks (line work only, never a button or text colour), each paired with its existing light field: amber, indigo, teal, rose, moss, steel, violet, sea green, leaf, terracotta, brick, ocean, plum, ochre, green, sepia for languages.

## Motion

- **Idle** (`animate: true`, off by default): the object floats 0 to -1.6% and rotates within 1.2 degrees over 7.2 s on a sine (HIGH's sticker drift), the contact shadow tightens as it rises, and one subject detail lives (the electron travels its orbit, the flask bubble rises and resets, the cursor blinks at 1.06 s, the summit pin bobs, the heads nod in sequence, the spiral turns). Emblems in a row are phase-shifted by subject so they never move together.
- **Marking** (`marked`): unmarked shows the volt bubble as a form-ink ring; marking inks it from the centre in 260 ms (Motion.ink, emphasized curve) with a 1.25x overshoot ring that fades. This is the subject picker's selection feedback; the caller adds `HapticFeedback.selectionClick`.
- **Reduced motion** (system or in-app): no idle ticker at all, marking snaps.
- Cost: the tile and the object are recorded once per subject, theme, detail level and mark state into a cached `ui.Picture`; each frame draws two pictures and a few shapes under a transform, inside a RepaintBoundary. One ticker per animated emblem, only while animating. No BackdropFilter, no saveLayer, no per-frame layout.

## States

Marked, unmarked, marking (animated), unknown subject (initials on the subject's tile, never a wrong object), language papers (speech bubbles), Night and Daylight, text scale independent (emblems are decorative and excluded from semantics unless a label is given).

## API

```dart
SubjectEmblem(subject: 'accountancy', size: 56, animate: false, marked: true, framed: true, semanticLabel: null)
SubjectIdentity.of('business_studies') // name, short name, formInk(brightness), field(brightness), hasEmblem
```

## Where to wire it (for the merge)

Import `package:mockmob/core/art/art.dart`. The emblem replaces both the raster `MmArt.subjectObject` renders and the Lucide `SubjectGlyphTile`; one helper per call site is enough.

| Screen | Call site today | Emblem |
| --- | --- | --- |
| Today, Tonight's move | `features/today/logic/move_builder.dart:163` (`HeroArt.object(MmArt.subjectObject(...))`), `features/today/widgets/resume_hero.dart:23` | 88 to 96 dp, `animate: true`, `framed: false` on the hero's light field |
| Practice, Choose your own | `features/practice/widgets/subject_tiles.dart:183`, `suggestion_card.dart:50` | 112 dp, `marked` follows selection, caller fires `HapticFeedback.selectionClick` |
| Practice, other subjects sheet | `features/practice/widgets/other_subjects_sheet.dart:52` | 40 dp (gives the six identical rows a subject each) |
| Review chapters, mistake threads | `features/review/widgets/chapter_group_card.dart:77`, `review_rows.dart:283`, `review_bits.dart:57` | 32 to 40 dp glyph |
| Onboarding subjects step | `features/onboarding/widgets/subject_row.dart:150` | 56 dp, `marked` follows the pick |
| Result header | result header widget (owned by the result track) | 120 to 160 dp plate, `animate: true` |
| You, subjects and sheets | `features/you/widgets/subject_art.dart` (make `SubjectArt` delegate to `SubjectEmblem`), `subject_rows.dart:35/95`, `hub/sheet_fields.dart:125`, `sheet/choice_sheets.dart:252` | 26 to 40 dp |
| Insights, Learn | `features/insights/widgets/insights_bits.dart:358-361`, `features/learn/widgets/subject_mark.dart` | 32 to 56 dp |

Notes:
- `SubjectIdentity.of(id)` accepts every spelling the app uses (`business`, `bst`, `gat`, `maths`, language papers) so no `canonicalSubject` is needed first; it keeps each subject's existing `SubjectLight`.
- `formInk(brightness)` is the subject's identity tint: line work only (a 3 dp edge, a chip ring, a progress hairline), never a button, a fill behind text or a text colour. Volt stays the only accent.
- Once wired, `assets/art/obj-*.webp` and `core/widgets/art/subject_glyph.dart` can be retired (saves the raster weight); leave them until every call site moves.
- Only one or two emblems per screen should `animate` (the hero and the result header). Rows stay still.

## Verification (14 Oct)

- Goldens in `flutter_app/test/golden/art/goldens/`: `emblem_gallery_{night,day}` (all 15 at 112, 56 and 24 dp), `emblem_states_{night,day}` (160 dp, unmarked and marked, unframed, language and unknown subject), `emblem_idle_frames_{night,day}` (five moments of the idle cycle for the six live subjects).
- Unit: `test/unit/art` (identity mapping, ink contrast on field, every subject at every detail level in both themes, picture cache bounded, idle only when asked, reduced motion system and in-app, marking timing, semantics, size).

## Review round (14 Oct, after the design review)

Changes to the emblem set, all inside `lib/core/art`:

- `marked` now defaults to false. A picker passes `marked` with the selection and `selectable: true` with a `semanticLabel`, so the semantics node reports selected. Pair the pick with a visible check or ring on the card: the ink alone is colour.
- Rows and cards use `framed: false`. An unframed emblem stands on a soft pool of the subject's field (cached, no blur), so there is no box inside the card. Use the tile only where the emblem is the object of the screen (a picker tile, a result header).
- The tile is now a piece of an answer sheet with one folded corner, not a squircle app icon.
- The volt mark has eight forms: bubble (Physics, Chemistry, General Test, History, Political Science, Psychology, Sociology, Geography with its pin), key (Accountancy), pill (Business Studies clasp, Computer Science run button), ink drop at the nib (English), reticle (Economics), swept angle (Mathematics), ring with open middle (Biology cell), and a reply row of three dots (language papers). General Test is a filled bubble in its grid cell. Still exactly one mark per emblem.
- Folds: Accountancy, Business Studies and Economics sheets are folded and shaded on one side. Biology has a honeycomb of cells on the lit half and stronger leaf inks.
- At 24 dp the idle drift and the live details (Geography pin, Sociology nods) move about twice as far in design space, so they read.
- Cache keys use the subject id, not its kind.
- Daylight: stronger tile at 24 dp, stronger pool, darker Physics orbit.
