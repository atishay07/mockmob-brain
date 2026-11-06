# MockMob app: spacing, layout and Night/Day parity system

14 October 2026, written for the phase 2 area fixers. Read with `SPACING-AUDIT.md` (every finding, by area, with image, file and exact fix), `DOCK.md` (the navbar) and `MOTION.md`.

All paths below are relative to `flutter_app/`. Numbers are dp (1 dp = 1 px in the 384 x 853 goldens). Existing tokens live in `lib/core/theme/tokens.dart` (`MmSpace`, `MmRadius`, `MmTarget`, `MmDock`) and `lib/core/widgets/surfaces/mm_surface.dart` (`MmRhythm`). This document keeps those names where it can and overrules their values only where the audit shows the value causes the drift the owner is seeing.

## 0. Why the app still looks uneven (what the audit measured)

The owner's complaint, "weird spacing, alignment, light/dark inconsistencies, looks the same as 25 hours ago", is real and has five measurable causes. The system below exists to remove each one.

1. **Two gutters and a +4 hack.** `MmSpace.gutter` is 16 and `MmSpace.cardGutter` is 20. Today, the Review hero, onboarding welcome, repair and the result cards use 20; Practice, You, Tools, Rhythm, Runner, Learn use 16; the You hub and the You sub-page titles use `gutter + 4`. Several screens mix them: on Review the hero text starts at x=20 and "Mistakes to repair" 90 dp lower starts at x=16; on the You hub the identity block starts at x=36 and "Milestones" at x=20.
2. **Visible gaps are not the coded gaps.** In `today_ready_night.png` the move card is coded 8 / 12 / 12 / 16 / 20, but the visible whitespace measured with a row scan is 10 (overline to title), 25, 29, 25, 25, 15. Two reasons: the figure styles carry large leading (`stageNumber` is 124 sp on a 104 dp line, so the "4" glyph is 82 dp tall inside a 104 dp box, 11 dp of air above and below), and every 32 dp-looking chip is a 48 dp hit box laid out as padding (`ShowMePill`, `MmSegmented`, quiet keys), so each adds about 8 dp of phantom gap.
3. **Art is placed by bleed, not by composition.** The Today hero art box is 212 x 212, bled 44 dp off the top and right, with a 168 dp emblem centred in it. The emblem is cropped by the card's top edge and ends 4 dp above the "to repair tonight" label, so the object looks glued to the top with air around it. The Review hero is a second, different implementation of the same card.
4. **Moments top-stack their content and pin the action.** Seven screens measured a dead band of 190 to 256 dp between the last content and the pinned button (repair entry 192, repair ending 232, result card 4 232, sealed sheet 240, onboarding save 224, question stream 224, weekly goal 256).
5. **Day is Night with the lights swapped, not a designed twin.** The Day surface ladder goes the wrong way (`raised2` is darker than the ground, so selected and "correct" states look disabled), the Day sheet scrim turns the page behind a sheet into taupe (#CBC3B5 on cream), and a handful of widgets paint `accentText` (olive #526700) where Night paints volt, so the same "today" bubble is volt on Night and olive on Day.

Measured first-screen fill (share of 8 dp rows that carry any ink or surface, Night, 384 x 853): Today 0.75 to 0.77, Practice 0.79 to 0.82, You hub 0.75, Rhythm 0.70 to 0.75, Onboarding steps 0.73 to 0.88. Those are healthy. The sparse ones are all moment screens: repair entry 0.57, repair ending 0.58, sealed sheet 0.59, result card 4 0.58, onboarding save 0.58, runner 0.58. The app is therefore not "sparse everywhere"; it is dense on roots and hollow on moments, which is why it feels unfinished.

## 1. The scale

One 4 dp grid. These are the only values allowed in `SizedBox`, `EdgeInsets`, `gap`, `spacing` and `Positioned` offsets, outside painters and art.

| Token | dp | Where it is used |
| --- | --- | --- |
| `s2` | 2 | Between a label and its sub-label when both are 14 sp or smaller; between a figure and its unit. Nothing else. |
| `s4` | 4 | Icon to label; overline to title; key to its quiet alternative; caption under a key. |
| `s8` | 8 | Items inside a control group (chip gap, wrap spacing, two stacked keys); meaning to evidence tag. |
| `s12` | 12 | Siblings: card to card, tile to tile, row padding vertical; title to figure; figure to meaning; section heading to its content; icon plate to text. |
| `s16` | 16 | Screen gutter; plain card padding; block to block inside a card; control to primary key; section rule to heading. |
| `s20` | 20 | Hero card padding; sheet side padding. |
| `s24` | 24 | Group gap (hero to the next block); moment gutter; art to headline in a moment. |
| `s32` | 32 | Section gap (with a hairline rule). Bottom air under the last row. |
| `s40` | 40 | Only the space above the very first section when the screen has no hero. |
| `s48` | 48 | Moment screens: top air under the header; the empty-state stack. |

`s6` stays for one use, the label/value "tight" pair (it is already `MmRhythm.tight`). Banned literals, all found in the code today (see audit G4): 3, 5, 7, 10, 14, 22, 28, 56 as gaps. Use the nearest token.

### 1.1 The three gutters, collapsed to two

- `MmSpace.gutter = 16`. Every screen that contains cards, lists, tiles or forms: all tab roots (Today, Practice, Review), every sub-page, runner, tools, you, rhythm, insights, learn, notifications, onboarding steps.
- `MmSpace.momentGutter = 24` (new; replaces `cardGutter = 20`). Only screens that are type and art with no cards: welcome, plan reveal title block, result recap cards, repair entry and ending, sealed sheet. A screen never mixes the two.
- Sheets and dialogs: 20 side padding (the 32 dp top radius needs the optical inset). Content cards inside a sheet are inset-tier (padding 16).
- Delete every `gutter + 4`, `youText` and `MmSpace.s4` outer padding on a screen. Titles and section labels sit on the gutter, exactly under the card edge.

At 360 dp this gives 328 dp of content on roots (the Today hero text column was 280; it becomes 288 with the padding below), which is what lets "to repair tonight" and unit labels sit beside the number instead of dropping under it.

### 1.2 The three text edges (the alignment grid)

Every left edge on a screen belongs to one of three lines. If a widget starts anywhere else it is wrong.

- **E0, the gutter (16).** Screen titles, section headings, captions, flat text, the edges of cards and art plates, week strips.
- **E1, card text.** Gutter plus the card tier's padding: inset 16 + 12 = 28, plain 16 + 16 = 32, hero 16 + 20 = 36.
- **E2, icon-row text.** E1 + 40 (plate) + 12 = E1 + 52. A row's divider starts at E2 (not at E1, not full width).

Right edges mirror: trailing values and chevrons sit on E1 from the right (so a "142 of 250" number and a chevron share one right edge).

Vertical: 4 dp grid for boxes; text is aligned by baseline, not by box, so a figure and its unit share a baseline (use `crossAxisAlignment.baseline` with the real font baselines; remove the `padding: bottom 14` hack in `number_block.dart`).

## 2. Surfaces, padding and radius (use `MmRhythm` and keep it small)

Three tiers only. Every card in the app is one of them.

| Tier | Padding | Radius | Fill (Night / Day) | Edge | Count per screen |
| --- | --- | --- | --- | --- | --- |
| Hero | 20 | 28 | raised blended 25% to ground plus lamp and subject light / `raised` plus the same light, lighter | edge light plus the one volt lit top edge | exactly 1 |
| Plain | 16 | 24 | `raised` / `raised` | hairline `line` plus edge light (Night) or card shadow (Day) | any |
| Inset | 12 | 18 | `sunken` (a well) / `sunken` | hairline only, no shadow, no edge light | any, inside Plain or Hero |

`MmRhythm.heroPad` changes from 24 to 20 and `plainPad` from 20 to 16 (the measured Today card at 20 already reads well; 24 and 20 steal 8 dp of width from every plain card). Radii: 28, 24, 18, 12 (controls), pill. Remove the loose radii found in the audit (14, 16, 20, 22).

## 3. Vertical rhythm

### 3.1 Between things on a screen

| Between | dp |
| --- | --- |
| Status inset to the header row | 8 (`MmRhythm.screenTop`) |
| Header row | 56 (avatar or back 44 inside a 48 target) |
| Header to the first block | 16 |
| Hero to the next block (group gap) | 24 |
| Card to card, tile to tile (item gap) | 12 |
| Section to section | 32, with a 1 dp hairline rule at the top of the new section, then 16, then the heading |
| Heading to its content | 12 |
| Last row to the dock clearance | 32 air, then the `MmBarInsets` clearance from `DOCK.md` section 3.4 |

Today's header currently takes 262 dp before the hero starts (hero top at y 283 of 853). Target: hero top at or above y 225 (see audit T3).

### 3.2 Inside a card (the move card is the model; every "hero" copies it)

Top to bottom, box values, with the visible whitespace they must produce after the leading fix in section 3.3:

| Step | Box gap | Visible whitespace |
| --- | --- | --- |
| Card top padding to the overline | 20 | 20 to cap height |
| Overline to title | 4 | about 8 |
| Title to the monumental number | 12 | about 16 |
| Number to its meaning line (when the label is under the number) | 8 | about 12 |
| Meaning to the evidence tag row | 8 | 12 |
| Evidence tag row to the control (segmented or chips) | 16 | 16 |
| Control to the primary key | 16 | 16 |
| Primary key to the quiet alternative | 4 | 8 |
| Quiet alternative or caption to the card bottom | 20 (equal to the top padding) | 20 |

The number's label sits beside the number, bottom-aligned to its baseline, when `numberWidth + 12 + labelWidth` fits the clear column; otherwise under it. It never floats on a third line.

### 3.3 Make the boxes tell the truth

- **Figures.** `hero`, `figure`, `figureCompact`, `stageNumber`, `countdownFigure` get a text-height behaviour with `applyHeightToFirstAscent: false` and `applyHeightToLastDescent: false`, and a line height equal to 0.9 of the font size, so the box is the ink plus about 2 dp. The 124 sp number then occupies about 86 dp, not 104. Compensate the card's gaps with the table above (the table already assumes this).
- **Hit targets are slop, not padding.** `ShowMePill` (32 visual, 48 box), the quiet key, `MmSegmented` rows, chips and avatar must paint at their visual size and extend the hit region outward with `hitTestBehavior` slop (a `MmHitSlop` wrapper: `Stack` + `Positioned.fill(left: -8, ...)` or `Listener` on an oversized transparent layer that does not take layout space). Visual size: chip 40, quiet key 40, show-me 32, segmented 44, avatar 44. The layout box then equals the visual box and the table in 3.2 holds.
- **Reserve async lines.** A line that appears after load or on connectivity change (Today's "Updated 7:30 PM. You are offline." adds 18 dp and pushes the whole page) reserves its height always, or overlays. No element moves after first paint except by the user's action.

## 4. Card composition rules

### 4.1 Subject emblem on a hero (the Today move card, the Review tonight card, the Practice suggestion, resume and ended heroes)

1. The emblem is a **prop belonging to the card's header band**, the band being overline + title + number. It is never anchored to the card corner.
2. Box 156 x 156 (heroArtWidth, heroArtHeight), emblem drawn at 136. Offset: top 8, right -10 (bleed only to the right, 10 dp). It is never cropped by the top edge. Replace the single `heroArtBleed = 44` with `heroArtBleedRight = 10` and `heroArtTop = 8`.
3. Its vertical centre is the vertical centre of the band (title top to number baseline), within 8 dp. Because the band is about 150 dp tall, a 136 emblem fits with 7 dp spare. If the title wraps to two lines the emblem keeps its position and the title wraps instead. The overline and title rows keep a right padding of `heroArtClear = 156 - 10 + 12 = 158`; the number row keeps it only while the number's label is beside the number.
4. Rows below the band (meaning, tag, control, key) are full width. The emblem never sits beside body copy.
5. 12 dp of clear air between the emblem's lowest ink and the first text row below the band; between the emblem's left edge and the title's right edge also 12 (use `_OneLine` scale-down, never overlap).
6. Parallax is 0.05 of the box height (about 8 dp), not 0.12. Entrance: glide in once (existing), then still. The emblem never changes size between themes.
7. A hero has either an object (emblem) or Mobi, never both. When the hero carries Mobi (day one, returning, late night, error), the header Mobi is hidden (already true on Today) and Mobi occupies the same band: 96 dp at the left of the band, speech bubble to its right, title and number below at full width.

### 4.2 Numbers

- A hero number is one per screen. Size: 124 sp for one or two digits, 112 for more; units at 55% of the number, top-aligned beside it ("183 of 250").
- Secondary figures (stat pairs like 3 and 6) are 40 sp with the label 4 dp under the figure, not 24 dp (rhythm "Your run" has a 24 dp hole between figure and label).
- The number's meaning is at most two short lines.

### 4.3 Rows and lists

- One-line row 48, two-line row 56, vertical padding 12, horizontal padding 16 inside a plain card.
- Leading plate 40 x 40, radius 12, gap 12 to the text (E2 = E1 + 52).
- Title Hanken 16/22 w600, sub-line 14/20 `ink2`, `s2` between them.
- Trailing value on the right edge E1, chevron 16 dp after an 8 dp gap, always the same chevron.
- Dividers 1 dp `line`, start at E2, end at E1 from the right.
- Selectable rows (options, choices): 56 minimum, radius 18, 2 px ink border when selected on both themes (see section 8), volt only for the state glyph.

### 4.4 Key stack (the bottom of cards, sheets and moments)

Primary key 56 tall, full width. Quiet key 40 visual, 4 dp below, centred. Caption 13/18 `ink3`, 4 dp below. Two equal-weight keys side by side: 8 dp gap. A key never touches a card edge: 20 dp from a hero's edge, 16 from a plain card's, 16 from the screen gutter.

### 4.5 Pinned action bar (sheets, runner, result, onboarding, Today when the key scrolls under the dock)

One component, `MmBottomBar`: 24 dp fade from transparent to ground above the bar, solid ground below; the scrolling content gets bottom padding equal to the bar height + 16 so the last row can scroll fully clear; content under the fade is dimmed, never half-visible chips or half rows. (Audit G10 lists seven places where a half-visible row or chip sits against a bar.)

## 5. The one-hero rule

Per screen:

- exactly one **hero tier** surface, and the one volt **lit top edge** is on it (no other card has a volt border, tint or edge; Compass currently has two);
- at most one **volt pill** in view at rest (the primary key); every other key is ghost (1 dp line, no fill) or quiet;
- at most one **object or character** (emblem or Mobi). The small header Mobi counts only when the hero has an emblem. Review currently shows an emblem plus a second Mobi beside the Start key;
- at most one **monumental number** (hero, figure) and one secondary figure row;
- at most three **badges or dots** (week bubbles and evidence bubbles count as one pattern each);
- sections under the hero are typeset (rule, heading, rows), not boxed; only Plain cards for lists and settings.

## 6. Density targets (balanced beats crowded beats sparse; over-gamified equals sparse)

Measure with the row scan in section 10. Targets at 384 x 853, first screen, Night and Day:

| Screen class | Fill (rows with ink) | Longest empty band | Notes |
| --- | --- | --- | --- |
| Tab root (Today, Practice, Review) | 0.72 to 0.85 | 40 | Hero top at or above y 225 on Today; hero plus at least one more block above the dock on a 640 dp phone (360 x 640). |
| List or settings page | 0.70 to 0.85 | 48 | |
| Moment (welcome, plan, result card, repair entry and ending, sealed sheet) | 0.68 to 0.82 | 96 between content and a pinned action band, 40 elsewhere | Content is vertically weighted (section 7), never top-stacked with a hole above the key. |
| Empty and error state | 0.40 to 0.60 | 264 allowed, but the stack is centred at 42% height | Mobi 140, title, one line, one key. |
| Runner question | 0.55 to 0.75 | 152 (options are pinned to the thumb zone by design) | Keep; verify at 360 x 640. |

Over-gamified guard: at most one celebratory element (burst, medal, Mobi) at a time; evidence bubbles must encode data (the Show me bubbles encode wrong answers); a decorative dot pattern that encodes nothing is removed; no more than three rows of dots or bubbles on one screen.

First-screen budget: one hero, at most three secondary blocks, at most 60 words outside the hero, between 3 and 9 tappables.

## 7. Moment scaffold (fix for the hollow screens)

One layout for every moment screen (`MomentScaffold`): `SafeArea > Column`: header (56) / `Spacer(flex: 2)` / content block / `Spacer(flex: 3)` / pinned action band (`MmBottomBar`). Content block is gutter-24, internal gaps from section 3, art no bigger than 176 (Mobi 140 to 176, emblem 136, sheet art up to 280 wide). When the content is taller than the space, it scrolls and the spacers collapse to 24. Optical centre at about 42% of the free height. Expected result: every moment's longest void at or under 96.

## 8. Night/Day parity (every surface, border, shadow, art plate and text colour needs a deliberate counterpart)

### 8.1 Surface roles (replace "raised2 means selected")

Night is monotone: sunken < ground < raised < raised2 (each step lighter). Day cannot go lighter than raised (#FFFDF8), so Day's `raised2` (#E9E4D8) is darker than the ground and reads as a hole. Semantic roles must be chosen by meaning, not by token name:

| Role | Night | Day |
| --- | --- | --- |
| Page | `ground` #12110E | `ground` #F3EFE6 |
| Card | `raised` #1B1A16 | `raised` #FFFDF8 |
| Well (inputs, tracks, inset cards, pressed) | `sunken` #0D0C0A | `sunken` #EAE5DA (keep; and stop using it for anything but wells) |
| Selected or active surface | `raised2` #25231E plus a 2 px ink border | `raised` plus a 2 px ink border (#17150F). Not `raised2`. |
| Correct and answer cards | card + 2 px ink border + volt glyph | same |
| Disabled | 40% opacity of the surface | 40% opacity of the surface |

Add `MmColors.selectedSurface` (Night = `raised2`, Day = `raised`) and replace the direct `raised2` reads on state surfaces (answer options in repair, learn answer card, segmented selected plate in Day is already white and is correct).

### 8.2 Edges and depth

- Night: depth is light. Every Plain and Hero card has the hairline `line` plus the `edgeTop` light on its top edge. Shadows are invisible on charcoal; do not rely on them.
- Day: depth is shadow plus hairline. Every Plain card has `cardShadow` and the hairline; ghost keys and white pills on the cream ground need a 1 dp `line` border (the white-on-cream pills on Usage data and Sign out have none).
- A shadow is always an analytic rounded rect with a blur at least 1.5 times its offset and never clipped by a parent `ClipRect` (the sealed sheet's Day shadow renders as a hard 8 dp strip).

### 8.3 Accent and text

- Volt is a **fill** in both themes with `voltInk` text. As **text or stroke on the ground** it is `accentText` (volt Night, #526700 Day). The rule "`isNight ? volt : accentText` for the filled mark" is wrong for fills: a filled dot, bubble or key is volt on both. Fix in `onboarding/widgets/week_ahead.dart:78`, `week_track.dart:27`; check the other `isNight ? colors.volt : colors.accentText` sites (listed in the audit).
- Text: body `ink`, secondary `ink2`, quiet `ink3`. `ink4` decorative only.
- Wrong: `wrongSurface`, `wrongBorder`, `wrongText`; wrong marks use `wrongMark`. Right marks use volt fill.
- Status text: Night uses the lighter `badText/warnText/goodText`; Day uses the darker ones. Never reuse a Night value in Day.

### 8.4 Scrims, light and art

- **Sheet scrim.** Night keeps `0x73080705`. Day changes from `0x425A4528` (26%, gives #CBC3B5 taupe over cream) to `0x2E4A3A20` at 18% (about #DDD6C8 over cream) plus the sheet's own shadow `0x1F2A2010`; the page behind stays cream, not grey.
- **Light fields.** `SubjectLight.night` / `.day` pairs already exist. Pool strength Night 1.15, Day 0.95; lamp alpha Night 0.20, Day 0.13. Keep. Subject art sits on its field on both themes and is never placed on bare ground.
- **Subject plate.** One widget, `SubjectPlate`, used for the Practice tiles, You subject tiles, Core subject grid and hero tiles: the field radial (centre 0.78, -0.78) over `raised`, the emblem unframed, label 12 w600 at the bottom-left on E1. Today the three screens use three different plates (white card with art, tinted gradient tile, dark field tile).
- **Raster art and Mobi** have transparent backgrounds and need no variant; their contact shadow is `black 24%` Night and `sepia 12%` Day, set once in `Mobi` / `SubjectEmblem`.
- **Raw colours.** `Color(0x...)` and `Colors.white/black` outside `core/art`, `core/mascot`, `core/theme` are parity debts. Files with the most: `practice/widgets/choice_glyphs.dart` (9), `today/widgets/today_tones.dart` (7), `rhythm/widgets/medal.dart` (7), `result/sheet/folded_sheet.dart` (5), `onboarding/widgets/welcome_scene.dart` (5), `core/widgets/bubbles/sheet_glyph.dart` (5). Each must read a role from `MmColors` or carry a comment naming its Day counterpart.
- **NTA exam look** is identical in both themes on purpose (it must match the real exam). Do not "fix" it.

### 8.5 Parity checklist for any widget

For each colour the widget paints, write the Night value and the Day value next to each other. If they are not both a `MmColors` role, it fails. For each border: Night edge light or hairline, Day shadow or hairline. For each emphasis: does the same state have the same visual weight in both themes (a selected row is the strongest thing on the page in both; it must not turn into a grey in one).

## 9. Headers and titles (one pattern)

- **Tab root:** avatar 44 + 12 + (overline 13/18 `ink2`, title `screenTitle` 26/30), row height 56. Existing `TabRootHeader`.
- **Sub-page:** one component, `MmPageHeader`: back key 44 (48 target) at the gutter, 12, title `screenTitle` 26/30 inline, optional trailing action, row height 56, caption under at E0. It replaces the stacked back-arrow-then-28/31 headline used on You, Tools and Rhythm pages and the five other bespoke bars (`PageHeader` review, `PracticeAppBar`, `_TopBar` in auth, result, mistake view). The stacked large title is reserved for moment screens.
- **Type tracking:** `headline` (28) tracking from -2% to -1%; `display` and `moment` (36) from -2.5% to -1.5%; add 0.5 dp word spacing. At the current values letters touch in "Appearance and feel", "Which CUET are you writing?", "Submit now?". Check on the 130% and 200% text-scale goldens.

## 10. Motion-safe layout (the owner's first priority)

- Layout never changes during an animation. Motion is transform and opacity only (already the brief). No `AnimatedSize` on cards that have siblings below them; where a height must change (segmented swaps task size), reserve the larger height or animate by clipping.
- Entrances use the same offsets as the scale: rise 8 or 12 or 20, stagger 60 ms, glide 300 ms. No 6, 10 or 14.
- A pinned bar, a sheet, the dock and the quick-start morph all read the same `MmBarInsets` so nothing the student is reading ever sits under them.
- Skeletons use the scale and the real component's measured heights so the page does not jump when data lands (today skeleton and hero should differ by at most 8 dp).

## 11. The check (run before reporting any screen done)

1. **Tokens.** `grep -rnE "SizedBox\((height|width): (3|5|7|10|14|22|28|56)\)|Radius.circular\((13|14|16|20|22)\)|gutter \+ 4|cardGutter" lib/features` returns nothing new.
2. **Edges.** Open the 384 x 853 Night golden; every left edge is E0, E1 or E2; every right edge mirrors.
3. **Row scan.** The band-measure script in `SPACING-AUDIT.md` appendix reports the visible gaps; compare to sections 3.1 and 3.2 (tolerance 4 dp), fill ratio per section 6, longest void per section 6.
4. **One-hero.** Count lit edges, volt pills, characters, big numbers.
5. **Pair.** Open the `_night` and `_day` goldens side by side; for every surface, border, shadow, art plate and text colour the counterpart is deliberate (section 8.5). Both goldens exist (22 result goldens are night-only today).
6. **Text scale.** 130% and 200% goldens for the roots keep E0 to E2, no clipped label, no unit dropped under a number without room.
7. **360 x 640.** The hero's primary key is visible without scrolling or the pinned bar is up with the fade.
