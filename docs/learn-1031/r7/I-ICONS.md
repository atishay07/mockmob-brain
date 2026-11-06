# R7 packet I: branded icons instead of vague ones (LK60)

Owner, 3 Nov 2026, about 3:15 pm: "Don't use these vague icons and stuff like this either. Make them into a proper branded icon,
a generated image, or something else."

Branch `web/1103-icons` (worktree wt-1103-icons, from web/1103-proto). The app swap follows after his look.

## 1. Inventory (3 Nov, phone 375 x 812, dev preview port 3466, plus source)

Two kinds of icon live on these screens:

- **Controls** (a chevron that opens, an X that closes, a check, a search glass, a plus/minus stepper, a spinner, the pager
  arrows). They are verbs of the interface, not stand-ins for a meaning. They stay as they are (Lucide, one stroke).
- **Meaning icons**: a generic line drawing standing in for a MockMob thing (a timer for Practice, a people outline for Mob,
  a printer for the print sheet). These are what he called vague. They are the list below.

### Web (src/)

| # | Where | Today | Means |
|---|---|---|---|
| W1 | Phone dock (AppLayoutClient) | CalendarCheck | Today |
| W2 | Phone dock | Timer | Practice |
| W3 | Phone dock | Users | Mob |
| W4 | Phone dock | UserRound | You |
| W5 | Desktop sidebar places (Glyph APP_ICONS) | BookOpenText, Telescope, NotebookText, Bookmark, Compass, Sparkles, Wallet, Trophy ... | Learn, Explore, Papers, Saved, Colleges, Ask Mobi, Wallet, Ranks |
| W6 | Practice, Your papers door | NotebookText in a tinted tile (an icon tile, which DESIGN.md already forbids) | Your papers |
| W7 | Practice, repair panel title | Wrench | Questions to repair (your mistakes) |
| W8 | Practice, repair panel key | MessageCircle | Ask Mobi |
| W9 | Practice, ticket and bar | SlidersHorizontal, Target | Fine-tune, the paper's rule |
| W10 | Learn chapter page, shelf rows | none on Key cards, Questions only, Your mistakes, Lesson; Printer as the Print sheet's end mark; Lock on a locked line | the chapter's shelf |
| W11 | Learn run and stage, source line | BookOpen | "from the NCERT chapter" |
| W12 | Learn run, a mistake card's head | History | a card from your mistakes |
| W13 | Explore head, Saved chip; feed rail Save key; Discovery feed | Bookmark | Saved |
| W14 | Explore feed rail, Chapter key | BookOpen | the chapter page |
| W15 | Learn home Or rows (Revise due cards, Fix open mistakes) | chevron only | Revise, Mistakes |

Count: 15 places on the web, 22 distinct meaning glyphs (W5 alone holds 8). Controls on the same screens: 14 Lucide control
glyphs (ChevronLeft/Right/Up/Down, X, Check, CheckCheck, Search, Plus, Minus, LoaderCircle, MoreHorizontal, RotateCcw, Play).

### App (flutter_app/lib, read only)

| # | Where | Today | Means |
|---|---|---|---|
| A1 | Bar (core/widgets/bar/bar_icons.dart) | calendarCheck, timer, usersRound, userRound | Today, Practise, Mob, You |
| A2 | Practise, More ways in (practice/widgets/more_rows.dart) | rotateCcw | Review again / Revise |
| A3 | More ways in | usersRound | This week's Mob paper |
| A4 | More ways in (learn2/learn2_door.dart) | galleryVerticalEnd | Chapter feeds |
| A5 | More ways in (insights entry_points.dart) | layers | Untimed questions |
| A6 | More ways in | compass | Admission Compass |
| A7 | Learn chapter shelf (learn2/chapter/chapter_shelf.dart) | lock, chevron | the chapter's shelf |
| A8 | Feed and run (feed_screen, run_screen, card_face) | bookOpen, bookmark, history | chapter source, Saved, from your mistakes |
| A9 | Practise rules (composer_parts.dart) | timer, circleCheck, bellOff | the paper's rules |

Count: 9 places in the app, 13 distinct meaning glyphs.

**Total: 24 places, 35 meaning glyphs (web 22, app 13), drawn from about 20 distinct meanings.**

## 2. What MockMob already looks like (the visual language to reuse)

The product already has a strong, owned picture language, and the vague icons sit next to it:

- **Subject objects**: photo-real, lamp-lit miniatures (a brass calculator on a ledger for Accountancy), on transparent
  ground with a soft contact shadow (`public/art/subjects/obj-*.webp`, `SubjectObject`, the app's `assets/art/obj-*`).
- **Hybrid props**: a brass stopwatch, a brass desk bell (`public/mob/art/hybrid-*.webp`), the Start sheet's Full mock.
- **Volt craft**: lime (#D2F000) felt and foil pieces: the foil seal, the felt check stamp, a kraft parcel with a lime seal.
- **Mobi**: the lime folded-paper diamond with the charcoal visor (`public/brand/mascot/*`), already used for Ask Mobi.

Rule already in the code (SubjectObject): below 32 px a photo-real object turns to mush, so small marks keep the line icon.

## 3. Direction: "desk objects", one small set

Every meaning becomes **one small desk object** from the same study desk the subject objects sit on: warm aged brass, cream
paper and card stock, kraft, charcoal, and exactly one lime (#D2F000) felt or foil accent per object, lit by the same warm
lamp from the upper left, transparent ground, no text. They read as MockMob at a glance because they are the same world as
the subject art and Mobi, not a new style.

| Object | Picture | Replaces |
|---|---|---|
| keycards | a short stack of index cards, the top card with a lime felt tab | Key cards (W10, A7) |
| questions | an exam answer sheet with filled bubbles and a pencil | Questions only, Untimed questions (W10, A5) |
| mistakes | a paper strip torn and mended with lime tape | Your mistakes, repair (W7, W10, W15, A2) |
| lesson | a small open hardback with a lime ribbon marker | Lesson, the chapter source (W10, W11, W14, A8) |
| print | a printed sheet with a lime binder clip | Print sheet (W10) |
| revise | index cards held by a lime rubber band | Revise due cards (W15, A2) |
| feeds | a fanned deck of tall portrait cards | Chapter feeds, Explore (A4) |
| saved | a lime felt bookmark ribbon tucked in a book corner | Saved (W13) |
| papers | a sheaf of answer papers held by a brass bulldog clip | Your papers (W6) |
| compass | a brass pocket compass with a lime needle | Admission Compass, Colleges (W5, A6) |
| today | a tear-off day calendar block with a lime top | Today (W1, A1) |
| mob | three felt game pawns, one lime, one cream, one charcoal | Mob (W3, A1, A3) |
| you | a spiral notebook with a lime elastic band | You (W4, A1) |

Practice keeps the existing brass stopwatch and Ask Mobi keeps Mobi (both already branded).

Where they go (at 32 px and up only, per the existing rule):

1. **Learn chapter page shelf**: each row leads with its object at 40 px (Key cards, Questions only, Your mistakes, Lesson,
   Print sheet). The Print sheet row ends with the chevron like the others, the printer glyph goes.
2. **Learn home Or rows**: Revise and Fix mistakes lead with revise / mistakes at 36 px.
3. **Practice**: Your papers loses its icon tile for the papers object; the repair panel's wrench becomes the mistakes object;
   the Ask Mobi key carries a small Mobi instead of a speech bubble.
4. **Explore**: its icons are controls (the Saved chip's 16 px bookmark, Play, the pager arrows) and stay; the feeds object
   leads the Learn home's "as a feed" row instead (section 4 says why the Explore head was left alone).
5. **Dock** (today, practice, mob, you at 28 px): shown on the showcase page as a proposal only, beside today's line icons.
   The dock is 24 px; objects that small are at their limit, so the owner judges it live before it is swapped.

Controls (chevrons, X, check, search, steppers, spinners, the 13 px lock, the 16 px bookmark) stay Lucide: they are the
interface's verbs, and making them pictures would add noise, not brand.

## 4. What was built (3 Nov, evening)

- Generation: two sheets, one try each (sheet A: keycards, questions, mistakes, lesson, print, revise; sheet B: feeds,
  saved, papers, compass, today, mob, you), Codex image_gen on the lean `.codex-alt` home, GPT-6-Luna high. Sheet A's agent
  made one extra call by mistake (its alpha was broken; unused). Both kept sheets have true alpha. Sources and prompts:
  `docs/brain/learn-1031/r7/icons-src/`.
- Assets: `public/art/icons/<name>-96.webp` and `-192.webp`, 13 icons, square, transparent, 3.5 to 10 KB each (212 KB all).
- Code: `data/brand_icons.mjs` (names, files), `src/components/brand/BrandIcon.jsx` (`BrandIcon`, the 32 px floor with a
  line fallback, and `MobiMark`, Mobi's face drawn at text size), `brand-icon.css`.
- Swapped on the web: chapter shelf rows (5 objects at 40 px, the printer glyph gone), Learn home Or rows (36 px by row kind),
  Practice's Your papers (44 px object, the icon tile gone), the repair panel (mistakes at 32 px instead of the wrench) and
  its Ask Mobi key (Mobi's face instead of a speech bubble).
- Not swapped, on purpose: Explore's head (the phone row already holds the title and the length control; an object would
  crowd it), the Saved chip and feed rail keys (16 to 22 px controls), the dock (shown as a proposal on the showcase), the
  desktop sidebar (18 px). Next after his look: the dock if he likes it, the Saved and Colleges page heads, the app's
  More ways in rows (rotateCcw, usersRound, galleryVerticalEnd, layers, compass) and chapter shelf.
- Showcase: `/preview/arena?decks=real&study=on&plan=pro&student=commerce&view=icons`.
- Test: `data/tests/brand_icons_1103.test.mjs` (in `test:app`): files, sizes, alpha, weight, the floor, the swaps.

## 5. Assets and process (plan as written before generating)

- Generated with `codex exec` image_gen, GPT-6-Luna high, lean `CODEX_HOME=C:\Users\atish\.codex-alt`, as two sheets of
  objects in one light so the set matches; references: the accountancy object, the stopwatch, the felt stamp, the parcel.
  At most a few tries per sheet.
- Cut, trimmed and saved as `public/art/icons/<name>.webp` at 192 px (sharp at 3x for 64 px) plus a 96 px file.
- One React component, `BrandIcon` (`src/components/brand/BrandIcon.jsx`): `<BrandIcon name="keycards" size={40} />`,
  decorative by default, a fixed square box (no layout shift), the line icon below 32 px.
- Showcase: `/preview/arena?view=icons` (dev preview only).
