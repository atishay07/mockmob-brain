# MockMob brand inventory for the home page (LK67-LK75)

Read-only research, 4 Nov 2026 (IST, small hours). Nothing in the repo was changed. Everything below was read from the files named, or measured on
the local dev server (http://localhost:3452 = the live main) and production. All paths are absolute under
`C:/Users/atish/Desktop/mockmob copy/` unless they start with `Desktop/`.
Output folder: `wt-1104-web-polish/tmp/home-1104/brand/` (called `B/` below).

Contents: 0 top findings, 1 Mobi, 2 promo film, 3 illustrations, 4 typography, 5 the changing headline, 6 checklist L-001..L-045,
7 gaps the designs must close, 8 phone hero geometry (LK70), 9 file index.

## 0. Top findings (the ones that change a design)

1. **Mobi exists in four different renderings and the home page mixes two of them.** (a) the rigged vector Mobi (`MobiReact`, 32 acts x 7 moods) in the hero only;
   (b) 8 baked photo-real poses (`public/brand/mascot/*.webp`) in the 5 section seats (`MascotSeat`); (c) 21 more 3D-render poses from the promo film
   (`MockMob-promo-film/public/art/gen/mobi-*.png`, `public/art/mobi/*`) that the site does not use; (d) a Blender GLB (`MockMob-promo-film/blender/mobi/mobi.glb`, 10.3 MB). Contact
   sheet: `B/sheet-ALL-MOBI.png`. In the 1440 Day Lab-section shot (`B/shots/home-1440-day-lab-head.png`) the seat Mobi is a large glossy baked pose at the page edge, while the 1440 hero Mobi (`B/shots/home-1440-night-hero.png`) is a small 140 px vector figure: same character, two finishes, two scales.
2. **The web palette is not the app palette.** App Night ground is warm charcoal `#12110E` (raised `#1B1A16`, ink `#F4F0E6`, lamp amber `#F2A93B`, `mm_colors.dart:117-133`; the logo's own charcoal is `#12110E` and warm white `#F3EFE4`, `logoB.js` last line). Web Night is a green-black: paper `#0b100e`, raised `#131a16`, ink `#f2f4ec`, lines `#283329` (`src/app/marketing-theme.css:3-8`). Web Day is `#f4f5f0` (app Day `#F3EFE6`). The painted room (warm amber lamp) sits on top of a green-black page in `B/shots/home-390-night-hero.png`. This mismatch is the quiet cause of Night reading as "neon on green-black": volt `#d2f000` has no warm ground to sit on. Fixing it is a token change, not a rebuild.
3. **The web display type is not the app's cut.** The app sets headlines in static Bricolage cuts at weight 600 (semi-condensed "Headline" 36/38, -1.5 %) and numbers in a condensed 700 cut (`flutter_app/lib/core/theme/mm_type.dart:145-162`). The web loads one wght-only variable file (`src/app/fonts/BricolageGrotesque-Variable.woff2`, 41 KB) and sets every display level at weight 800 (measured, section 4). The app's cuts exist as TTFs on the web side (`public/brand/fonts/BricolageHeadline-SemiBold.ttf`, used only by the OG image) and in `Desktop/MockMob-promo-kit/fonts/`.
4. **The home hierarchy is flat.** At 390: hero h1 38.5 px, statement 35.1, section h2 32, close h2 38.4 (a 1.2x range across four levels, all weight 800, all about -0.04 em). At 1440: h1 60.0, statement 59.2, h2 57.6, close 80. Display never changes weight or width, so "what is the page's main idea" is carried by nothing.
5. **The one entry animation MockMob owns is the app's "mo" opening** (`brand_opening.dart`): the "mo" sits on the glass, Mobi blinks, the empty right eye inks, the camera pulls back while "mock" unfolds leftwards and "b" rightwards on paper hinges, 1.0 s to the composed word, hand-off at 1.28 s (3.0 s on first install). The website has no entry loader at all (L-043 is N/A today). Everything needed to port it is on the web side already except per-letter outlines (section 1.5).
6. **The exam section copies the NTA information architecture in MockMob colours; it is not the app's own screen.** Measured: 1644 px tall at 390 (1.95 screens), 1363 px at 1440 (1.51 screens). It shows `Save & Next`, `Mark for Review & Next`, `Clear response`, `Question Palette` with an NTA legend, on a dark card (`B/shots/home-390-day-exam-console.png`). The app's own question screen (promo kit `screens/15`, `16`) has a different layout: a "1 of 5" pill, a Questions button, a Saved tick, five progress dots, a "Mark for review" chip, A/B/C option rows with letter chips, "Clear my answer", Previous and a volt Next key (sheet `B/sheet-app-exam-screens.png`). That screen is the unique, real MockMob screen LK72 asks for.
7. **The tests currently forbid parts of what LK67-LK75 ask for.** `heroLines.test.mjs` (H1) forbids a changing or typed headline and deletes the old components by name; `scrollStorySpeed.test.mjs` forbids `preventDefault` and non-passive listeners in `ScrollStory.jsx`, so a "one gesture = one step" implementation that catches the wheel or touch must rewrite that lock (and LK47 of 2 Nov asked for the opposite: the page was gliding a whole step per notch and the owner said the speed felt like a lot); `release9_public_1018.test.mjs` requires the hero grid and dots to stay while the slop checklist (C6) wants them gone. Section 6 lists every lock.
8. **L-016 (the hero headline has a visibly changing word) is in direct conflict with the owner's 1 Nov ruling H1** (static headline; `heroLines.mjs` header). LK74 (a refined typing animation) re-opens it. The new design has to decide which wins and update both the checklist row and the test.
9. **Page weight of copy**: 1,705 words across the 13 sections at 390 (sum of `capture-results.json` `sections[].words`), page height 27,017 px = 32 screens at 390 and 23,321 px = 25.9 screens at 1440. The three tallest: Your-prep tour 5,943 px (7.0 screens), Lab cinema 3,569 px, Mistake Lab 3,463 px. These are held (pinned) stories, so most of that height is scroll distance, not reading length; the text walls are in the Lab (487 words) and Compass (214) and Eligibility (193).
10. **13 brand desk-object icons, the foil/stamp/parcel/token art, the painted scenes and the Fold characters are not on the home page** (grep of `src/app/page.js` and `src/components/landing/*.jsx`: no `BrandIcon`; folds appear only as 20 px heads in `TourScreens.jsx:329`). They are owned, approved assets the designs can reuse to replace generic Lucide line icons.

## 1. Mobi

### 1.1 Every Mobi asset (with where it lives)

| Family | Files | Poses / expressions | Used on home today | Used in the app |
|---|---|---|---|---|
| Rigged vector Mobi (web twin of the app's painter) | `src/components/brand/MobiReact.jsx`, `MobiFigure.jsx` (305 lines), `mobiPaint.js`, `mobiRig.js`, `mobiSim.js`, `mobiActs.js`, `mobiDom.js`, `mobi-figure.css`; poster `src/components/landing/MobiPoster.jsx` + `mobiPoster.generated.js` (static SVG first frame) | 31 acts (`mobiActs.js:15-20`: appear hello talk cheer celebrate think point sleepy oops rest read correct encourage loading sleep nudge proud listen wake nod tilt wave startle brace relief walk hop curious focus sympathy idea) + idle; 7 moods (calm happy proud curious sleepy concerned focused); 6 eye shapes (open smile happy content wide focus). Design box 140x168 (`mobiPaint.js` GEO). Contact: `B/shots/preview-mobi-acts-1440-day.png` (dev route `/preview/mobi-acts`), `B/sheet-promo-kit-brand.png` (moods and eyes) | Hero only: `HeroMobi.jsx` variant `room` 178 px (phone), variant `host` 140 px (761+); `HeroDockGate.jsx` | `flutter_app/lib/core/mascot/*` (mobi_rig, mobi_sim, mobi_painter, mobi_acts, mobi_tap_cycle ...): the same rig table |
| Baked pose set (photo-real render) | `public/brand/mascot/{greeting,idle,attentive,thinking,pointing,encouraging,celebrating}.webp` (409x560 ... 472x560, 30-33 KB each), `character-sheet.webp` (864x1107, 119 KB), `og-pointing.png`, `ask-deskbell.webp` (a brass desk bell, not Mobi), `manifest.json`; `public/mob/explainer/mobi-{greet,think}.webp`; `public/art/pro/mobi-read.webp` | 7 poses + sheet. Contact: `B/sheet-site-mobi.png` | Five seats via `MascotSeat` (`Mascot.jsx:48`): Lab `attentive` (page.js:297), Compass `pointing` (312), Eligibility `pointing` (335), Pricing `attentive` (396), Close `greeting` (446); `Mascot` also inside `DemoDrill.jsx` | `flutter_app/assets/art/mobi-{greet,point,think,cheer,rest,sleepy,read}.webp` (7, `mm_art.dart:13-19`) and `assets/mobi/` (7 older flat files, `mobi.dart:55` legacy) |
| Promo-film 2D render poses (same character, richer acting + props) | `Desktop/MockMob-promo-film/public/art/gen/mobi-*.png` (21: cards, highlighter, jump, laptop, ledge, peek, phone, point-left, present, pull, stamp, strip, surprised, think-up, wave, wink ...) and `public/art/mobi/mobi-{cheer,greet,point,read,think}.png`; kit copies in `Desktop/MockMob-promo-kit/visuals/mobi/` (character sheet, every-mood, eyes). Upscaled with Real-ESRGAN (`docs/ASSET-LICENSES.md`) | Contact: `B/sheet-promo-mobi.png` (21 poses) | Not on the site | Not in the app |
| Promo-film 3D Mobi (Blender) | `MockMob-promo-film/blender/mobi/mobi.glb` 10.3 MB, `mobi.blend`, `poses.py`, rig with squash/stretch, face controls (blink, squint, look_x/y); frame sequences `public/mobi3d/*` (e.g. `everything-r8c4` 838 PNGs, 268 MB; `open` and `logo` are 400 MB trees) | `B/sheet-promo-mobi3d.png` (frame samples; transparent PNGs show mostly black on the sheet) | Not on the site | n/a |
| Folds (the Mob's 12 paper-folded companions) | `public/mob/folds/` 119 files: crane, cutting, dart, dogear, hexa, hop, kandil, naav, patang, stamp, sticky, tally x poses idle, idle-blink, cheer, wave, think, shrug, head (128/256/512 px webp). Contact `B/sheet-folds.png` | Same visor face as Mobi, a different folded body each | 20 px heads in the tour's Mob screen (`TourScreens.jsx:329`) | `flutter_app/assets/folds` (96 files) |
| Logo-B Mobi (as the second o) | `src/components/brand/logoB.js` (`LOGO_B_MOBI` full / small / micro), `src/components/Logo.jsx` (`logoDetail`: micro < 14 px, full >= 64 px), `public/brand/logo-header-{dark,light}.svg`, promo kit `visuals/brand/logo-*` | Detail masters: full (flap cut, inked left eye, empty bubble right eye), small (both eyes), micro (visor only) | Site bar wordmark | App launch + icons; `logo_geometry.g.dart` |

### 1.2 Expressions and poses at a glance

* Baked set (7): greeting (wave), idle (eyes closed, sitting), attentive (hands down), thinking (hand on chin), pointing (right arm out), encouraging (open hands, one raised brow), celebrating (arms up, closed-smile eyes). All with a lime folded-paper diamond body, black visor, two tall cream eyes, antenna with a lime ball, black rubber-hose limbs and boots.
* Rig (see 1.1): the app's table, `data/mobi_rig.v2.json`, evaluated in `mobiRig.js` + `mobiSim.js`; tap cycle hello, tilt, hop, startle (never the same twice, reset after 8 s, six a visit, then a squash) in `HeroMobi.jsx` header; Celebrations "Quiet" and "Off" and Reduce motion rules in `MobiReact.jsx` header.
* The hero's six tap lines (`heroTaps.mjs`): load "Hi, I'm Mobi. Tap me.", then "I find where your marks slip.", "One timed mock shows me the chapter.", "{bank} questions. A fresh mock every time.", "Okay, okay. Try five questions?", "Free to start. These five need no signup.", "That's all my tips. Go on, try one."

### 1.3 How Mobi is used on the home page today (and the parity gap, LK67)

* Phone (up to 760 px): inside `HeroRoom` (the painted Night room band `scene-welcome-band-night` or the Day room `scene-empty-allclear-day`), rigged Mobi 178 px, a speech bubble over the window (tap line), Night's pinned answer sheet fills one volt bubble per tap 120 ms after the tap (`heroScene.test.mjs:70`). After 3.5 s untapped he looks down at the key once (curious). Shot: `B/shots/home-390-night-hero.png`.
* Desktop (761 px up): no room. Mobi is the sample's "host", 140 px, in the gutter at the stage's lower left, points (nudge) at the card, reacts to the sample's answers (correct / encourage). Shot: `B/shots/home-1440-night-hero.png`. So the two heroes have different scene, size, role and interaction: one rigged Mobi, two ideas.
* Sections: five baked-pose seats (above), each with a caption at 11 px / 13 px 700 (`Mobi seat caption` row in section 4). `PipGuide` (flying Mobi that lands on stations; `src/components/brand/PipGuide.jsx`, 367 lines) is also mounted (page.js:45). `landingMobi.test.mjs:65` locks "one Mobi in view (W-074)".
* The phone dock carries no Mobi (page.js:459 comment).

### 1.4 The app's launch animation: "mo" expands into "mockmob"

Source (read-only): `Desktop/mockmob copy/wt-1103-app-rel/flutter_app/lib/core/widgets/brand/brand_opening.dart` (908 lines), `first_launch_opening.dart`, `core/router/splash_screen.dart` (104 lines: the still last frame + Mobi blink every 2.8 s while the session loads), geometry in `brand/logo_geometry.g.dart` (422 lines). Frames: `B/app-opening-goldens.png` (mo, ink, unfold), launch splash `B/sheet-promo-kit-brand.png` (third tile).

Timeline in ms from "mo on the glass" (`OpeningTimeline`, `brand_opening.dart:55-110`):
* 0-500 the "mo" holds exactly where the Android splash drew it (288 dp square); Mobi blinks at 150 (160 ms blink); the empty answer-bubble right eye inks from its centre 320-520 (200 ms) with a light haptic at 400.
* 500-1000 the camera pulls back (`pullBack` cubic 0.5,0,0.15,1, 500 ms, scale interpolated on a log scale because a front-loaded curve read as a cut) to the whole word while the other letters unfold out of the "mo" like a folded paper strip: "mock" leftwards from the m, "b" rightwards from Mobi; each letter on a hinge at the edge it shares with its neighbour, nearest first, first letter at 520, stagger 40 ms, carried by a spring (`Springs.settle`); a letter stays invisible until 12 % open and is fully visible at 45 % open. The lamp (`LightField.lamp`) comes up with the camera. Mobi glances toward the word at 860 (120 ms).
* 1000 composed word (final em = min(48 dp, 60 % of width)); 850 the first screen starts painting under the opaque opening.
* 1000-1280 hand-off: the word fades out in 120 ms, then the ground lifts (80-280). Short opening total about 1.28 s. First launch after install: 3.0 s (`fullMs`), the word holds with a 3 % breath swell, Mobi glances back and blinks. Reduced motion: "mo" fades out in 200 ms, the word fades in over 160 ms, no unfolding.
* Ground: charcoal `#12110E` in both themes plus the amber lamp; letters warm white `#F3EFE4`; Mobi volt `#D2F000`.

What a web port would reuse: `logoB.js` already holds Mobi's three detail masters and the letters as one merged outline; the per-letter outlines with their pen positions (`letterX = [0, 865, 1445, 1968, 2549, 3423.22, 3987.35]`, Mobi index 5, `wordBounds` 40,-670 to 4544.35,32.11, `adaptiveIconCrop` 1985.64,-1514.05 size 2585.81) are in `logo_geometry.g.dart:132-265`, generated from `mockmob-next/tmp/logo/final-B/make_dart.py` (that folder also holds `svg/` and `web/` exports). The promo film also has pre-cut per-letter PNGs of the wordmark (`MockMob-promo-film/public/art/brand/wm-{dark,paper}-{0m,1o,2c,3k,4m,b,mobi,mockm}.png`). The web currently has no loader; the Preparoo splash study (`mockmob-next/docs/brain/handoff-1104/home-research/preparoo/source/splash.txt`) is the reference the owner named.

### 1.5 Contact sheets (all in `B/`)

* `sheet-ALL-MOBI.png` (1680x1998): the master. Row 1-2 the web baked poses + deskbell + explainer + read; rows 3-6 the 21 promo-film poses; bottom the app's `assets/art` Mobi poses on dark, hero desk, compass, three foil tokens.
* `sheet-site-mobi.png`, `sheet-promo-mobi.png`, `sheet-app-only-art.png`, `sheet-promo-mobi3d.png`, `sheet-folds.png` (24 fold poses), `shots/preview-mobi-acts-1440-day.png` (the rig's moods and 32 acts), `sheet-promo-kit-brand.png` (logo board, Play feature graphic, launch splash, colour swatches, every mood, eyes).

## 2. Promo film assets (the 21-24 Oct work)

Project: `Desktop/MockMob-promo-film` (Remotion 4, 60 fps; `docs/HANDOFF-2026-10-24-1530.md`, `docs/OWNER-LEDGER.md`). Kit for Claude Motion: `Desktop/MockMob-promo-kit` (60 app screens, fonts, `data/motion-tokens.json`, `data/folds.json`, INDEX.md). Store art: `Desktop/MockMob-store-listing` (feature graphic 1024x500, icon, 8 captioned screenshots).

| Item | Where | State | Usable on the site |
|---|---|---|---|
| Teaser16 (16:9 v8, 77.8 s, approved, byte-frozen) | `out/teaser-v8.mp4` 130 MB (master `teaser-v8-master.mp4` 130 MB, `teaser-v8-phone.mp4` 27 MB); sheets `out/teaser-v8_sheet_01..20.png` | Approved | Stills (see `B/promo-teaser-v8-frames.png`: "Preparing for CUET 2027?", 142 of 250 marks, "13 wrong", the exam-day laptop, Ask Mobi phone, the mockmob end card with the five Folds). Video: heavy; L-044 says no video scene unless he approves its storyboard |
| 9:16 Reel (68.57 s) | `out/reel916/final/` (approved 24 Oct about 6:10 pm per ledger line 10), `out/reel916/cand/cand4.mp4` 41.8 MB, phone copy `out/reel916/owner/reel-v2-cand4-phone.mp4` 17 MB, captions `out/reel916/mockmob-reel916.srt/.vtt`; keyframes `B/promo-reel916-keyframes.png` | ~85 % at last handoff, sound pass pending | Stills; the 9:16 framing suits a phone hero |
| Film stills pulled for this run | `B/film-stills/teaser-{01,13,25,33,45,77}.png`, `reel-{01,13,16,49,58,67}.png` (1920x1080 / 1080x1920) | extracted | Direct use as stills; they carry film typography (below) |
| Sound | `public/sfx/*.wav` (38 files: bell_brass, click_switch, clock_tick, paper_flick/rustle/slide, pop_soft/bright, seal_pop, ding_success, logo_hit ...), `public/music*`, voices `public/vo/el_himanshu_reel_p9`; licences `docs/AUDIO-LICENSES.md` | The owner's tactile UI sound layer is a film rule (memory: "tactile UI sound layer (SaaS feel) is required" for the film) | The site has no sound; none was asked for on the home page |
| Wordmark letters | `public/art/brand/wm-*.png` | cut for the logo unfold in the film | A ready reference for the per-letter unfold |
| Desk and plates | `public/deskshot/plate.jpg`, `plate2.jpg` (+ depth maps), `public/art/scenes`, `out/3d/` | generated plates (laptop, chai, lamp, window city bokeh) | `B/sheet-desk-plates.png` |
| Props (3D look) | `public/art/gen/prop-*.png`: bubble-token, clock, college, highlighter, laptop, ledge-strip, mock-deck, paper-chain, pencil, phone, price-tag, speech-bubble, tex-paper | cream/charcoal/volt matte felt look | `B/sheet-promo-props.png` |
| Typography in the film | Bricolage display + Hanken + **Instrument Serif Italic** accent words ("exact screen", "held", "else", "go?") (`docs/ASSET-LICENSES.md`; frames in `B/promo-teaser-v8-frames.png`) | Film only | The italic serif is NOT in the owner's keep-list (Bricolage, Hanken, Literata); do not import it to the site without asking |
| Rules the film followed | `docs/V8-ACCEPTANCE.md` (owner words): nothing childish or toy-like, UI realistic and rebuilt in code (no AI-generated UI text), never art above native resolution, Mobi friendly in every frame (no squint/half-lid), no defensive text, Rs 99 never next to Google Play, unlimited mocks the headline USP, no bank-size numbers | | Same sensibility as the site rules |

## 3. Illustrations and their style rules

Contact sheets: `B/sheet-subject-objects.png` (29 subject objects, 2 repeats), `B/sheet-brand-icons.png` (13 desk icons + foil seal + hybrids + parcels + stamp), `B/sheet-scenes.png` (18 painted scenes + campus sprite), `B/sheet-desk-plates.png`, `B/sheet-promo-props.png`, `B/sheet-folds.png`.

* **Subject objects** (29; `public/art/subjects/obj-<id>.v2{,-256,-512}.webp`, 114 files; `data/subject_art.mjs`; `SubjectObject.jsx`, `ObjectLife.jsx` float on a 7.2 s breath, lean to pointer/finger/scroll, `ObjectLifeModel.mjs` = the app's springs): photo-real, lamp-lit 3D desk objects on cream (accountancy calculator and ledger, agriculture wheat and trowel, anthropology skull, biology microscope, business briefcase, chemistry flask, computer science laptop, economics scale with onion, engineering graphics compasses, english newspaper and pen, entrepreneurship coin box, environmental studies tree-slice, fine arts palette, general test Rubik's cube and compass, geography globe, history seal, home science sewing machine, knowledge tradition book, language journal, legal studies scales, mass media microphone, mathematics compass, performing arts tabla, physical education cones and whistle, physics Newton's cradle, political science gavel, psychology brain, sociology figures, teaching aptitude blackboard). Rule (`SubjectObject.jsx` header): square box laid out before decode, never cropped, stands on the app's two-ellipse contact shadow, below 32 px swap to a line icon, decorative.
* **Desk-object brand icons** (13; `data/brand_icons.mjs`, `BrandIcon.jsx`, `public/art/icons/<name>-{96,192}.webp`): keycards, questions, mistakes, lesson, print, revise, feeds, saved, papers, compass, today, mob, you. Style (`BrandIcon.jsx` header): one desk object per meaning, "brass, cream paper, kraft, charcoal and one lime felt or foil accent", centred on one optical box, 32 px floor, controls (chevrons, close, check, search) are never brand icons. Locked by `data/tests/brand_icons_1103.test.mjs`. **None is on the home page.**
* **Pro art** (`public/art/pro/`): foil seal (lime foil sticker, 27 KB), group desk (the five Folds under the lamp), hybrid metronome, mobi-read. Also `public/mob/art/`: stamp-seal, parcel sealed/pop/open, hybrid deskbell/stopwatch, foil-seal, scene-empty-nothing day/night.
* **Painted scenes** (`public/art/scenes/`, 96 files = 18 scenes x widths 768/1280/1536 x avif+webp): the app's rooms, Night and Day pairs: welcome hero (1296x1620), welcome band, plan seal, milestone check (volt tick made of OMR bubbles), empty states all-clear / nothing / no-results / offline / saved / unreachable. Common language: a warm amber lamp pool on a floor ellipse, an arched window (moon and city at Night, daylight and hills at Day), a plant, shelves, a pinned answer-sheet poster whose bubbles are volt. Home uses `welcomeBand` (Night) and `allClear` (Day) in `HeroRoom.jsx`.
* **Campus tiles** (`public/images/campus/{hansraj,hindu,srcc,stephens}-{300,450,600}`, `campus-illustrations.webp`): painted red-brick college facades; used in `CollegeDestinations.jsx` and `PublicHeroArt.jsx`.
* **Folds**: see 1.1.
* **Style rules found in the repo** (to cite, not to invent): swatch sheet caption "Volt is the only accent. Night = charcoal, Day = cream. Lamp amber is light, never a button." (`B/sheet-promo-kit-brand.png`, `brand-colour-swatches.png`); no glowing keys, sheens, drifting blobs, gradient text (L-019, `ui-ux-standards.md`); lamp light only as painted light (slop checklist C4: "the only allowed light is the warm lamp light that the paintings already own", `home.css:68`); the film's "never above native resolution" and "UI realistic, built in code"; the icon set's "controls are never brand icons".
* Palette tokens in the app: `mm_colors.dart:117-200` (volt `#D2F000`, volt ink `#0B1000`, volt edge `#9DB400`, lamp `#F2A93B`, Day accent text `#526700`; Night ground/raised/raised2/line `#12110E #1B1A16 #25231E #312E27`; Day ground/raised `#F3EFE6 #FFFDF8`; Fold paper colours in the swatch sheet).

## 4. Typography on the home page today

Measured with `getComputedStyle` on the local main at 390x844 (DPR 2) and 1440x900, Day (Night is identical in size; only colour differs). Raw data: `B/capture-results.json` (`runs[*].levels.named`), script `B/brand-capture.mjs`.

Families (`src/app/layout.js:19-61`; `--font-display` Bricolage Grotesque, `--font-body` Hanken Grotesk, `--font-mono` Geist Mono; Gabarito is declared but unused; **Literata is not loaded on the home page**, it ships only in `src/components/keycards/` for Learn).
Bricolage here is the Fontsource "variable latin wght" file (`layout.js:14-19`, 41 KB), i.e. the weight axis only; no width or optical-size axis is shipped. The app's four static cuts are condensed 700, headline 650 at width 87, title 600, wordmark.

| Level | 390 px | 1440 px |
|---|---|---|
| Hero h1 "CUET 2027. One mock. Know what to fix." | Bricolage 38.5 / 38.1, w800, -1.54 px (-0.04 em) | 60.0 / 59.4, w800, -2.40 |
| Hero lead | Hanken 16 / 23.2, w400 | 20 / 31, w400 |
| Primary key | Bricolage 16 / 24.8, w800, -0.16 | same |
| Second key | Hanken 15 / 23.25, w650 | Bricolage 16, w800 (a different face at the two widths) |
| Trust line, bank line | Hanken 13 / 17.55, w400 | same |
| Mobi bubble | Hanken 13 / 18.2, w600 | same |
| Sample card heading / tag | Hanken 12 / 18.6 w600 / w400 | same |
| Sample question | Bricolage 18 / 24.3, w700 | 24 / 32.4, w700 |
| Sample option, option letter | Hanken 16 w600; Geist Mono 13 w600 | same |
| Sample note, other-subjects line | Hanken 11 / 16.5; 12 / 18 | same |
| Proof band number / label | Bricolage 21.6 / 22.7 w800; Hanken 13 | 28 / 29.4; 13 |
| Statement ("Your marks slipped somewhere...") | Bricolage 35.1 / 36.5, w800, -1.40 | 59.2 / 61.6, w800, -2.37 |
| Shelf subject name / note | Hanken 16 w700; 13 | Hanken 14 w700; 14 / 21.7 |
| Section kicker | Hanken 14 / 16.8 w700 (volt) | same |
| Section h2 | Bricolage 32 / 32.6, w800, -1.15 | 57.6 / 58.8, w800, -2.07 |
| Section sub | Hanken 16 / 25.3, w400 | 18 / 28.4 |
| h3 | Bricolage 20 / 22 w800 | 26 / 28.6 |
| h4 plan name | Bricolage 18 / 21.6 w700 | same |
| Mobi seat caption | Hanken 11 / 16.5 w700 | 13 / 19.5 w700 |
| Tour slide title / lede / counter | Bricolage 20.3 w800; Hanken 15 / 21.75; Geist Mono 10.7 w600 | 40 / 43.2 w800; Hanken 16 / 24; Geist Mono 10.7 |
| Exam h2 / question / option / action | Bricolage 32 w800; Bricolage 18 / 25.2 w600; Hanken 14; Hanken 11 w600 | 57.6; 24 / 33.6; 14; 12 |
| Stats number / label | Bricolage 32 w800; Bricolage 15 w700 | 44 w800; 15 |
| Plan price | **Geist Mono** 40 / 38 w700 | 60 / 57 |
| FAQ question | Bricolage 17 / 22.1 w700 | same |
| Close h2 | Bricolage 38.4 / 39.2 w800 | 80 / 81.6 w800 |
| Footer blurb / links | Hanken 15 / 24; 16 | same |
| Dock line | Hanken 12 / 15.6 | n/a |

Where the hierarchy is muddled (numbers above):
1. **Four display levels inside 32-38 px at 390** (h2 32, statement 35.1, hero 38.5, close 38.4): the hero is 1.2x the section titles. At 1440 the hero (60.0), statement (59.2) and h2 (57.6) are within 4 %; only the close (80) breaks out, and it is the last thing on the page.
2. **One weight for everything**: every Bricolage display level is w800 with a tracking of about -0.04 em (-0.036 em on 20 px). No light/regular display, no condensed figures; the app uses 600 headlines and condensed 700 numbers (`mm_type.dart`). The proof numbers (21.6-28), stats number (32-44) and plan price (Geist Mono 40-60) are three different number styles.
3. **Three number faces**: Bricolage (proof, stats), Geist Mono (plan price, option letters, tour counter, "GJ" monogram) and Hanken (the rest). Geist Mono is the sibling of the overused "Geist" (slop checklist T1); Hanken with `tabular-nums` or Bricolage tabular figures (the app asks for them: `mm_type.dart:114`) would do the job.
4. **Small text**: 11 px (sample note, Mobi seat caption at 390, exam action at 390), 12 px (sample heading, other-subjects line, dock line), 13 px (trust line, bank line, bubble, proof label). The first-screen facts the owner cares about (price, "No auto-renewal", "No cap on Pro") are all 13 px.
5. **Second key changes face and weight between phone and desktop** (Hanken 15 w650 vs Bricolage 16 w800), so the same action has two voices.
6. **Kickers** (Hanken 14 w700 volt) above h2 on five sections (page.js:269, 292, 307, 372, 385); the owner's ledger L-020 forbids eyebrow labels with dots; a kicker without a dot is a grey area the slop checklist calls T2.
7. **Line-height**: lead 1.45, section sub 1.58, tour lede 1.45, footer 1.6, sample option 1.35: five body rhythms.
8. **Weight loss on the exam card**: question w600 vs the sample card's w700 for the same kind of text.

## 5. The changing headline: today and in history

**Today** (`src/components/landing/heroLines.mjs`, 13 lines, owner ruling H1, 1 Nov 2026, commit `f61de0206`): `HERO_LINES = ['CUET 2027.', 'One mock.', 'Know what to fix.']`, one static sentence. `page.js:184` renders the three runs inline with `<br />`; "CUET 2027." takes `.lp-title__brand` (`color: var(--accent-text)`, L-017). The only motion is one entrance rise: `animation: lp-scene-rise 420ms cubic-bezier(0.23, 1, 0.32, 1) 240ms backwards` (`hero-scene.css`, locked by `heroLines.test.mjs:47`). Mobi's six tap lines (`heroTaps.mjs`) carry the reactions instead. "Know what to fix." is claimed true (chapter review names the chapter; the free SWOT gives sets to do next, `data/mock_swot.js`).

**History** (`git log -S"morphing-text"`: `f87041359` 23 Apr, `3c88f925c` 4 Oct, `bafdda0b1` 19 Oct, `f61de0206` 1 Nov):
1. **April 2026, `src/components/ui/morphing-text.jsx`** (140 lines, deleted 18 Oct in `02d2558d8`, last readable at `3c88f925c`): two stacked absolutely-positioned layers; a requestAnimationFrame loop with morphTime 1.5 s and cooldown 0.5 s; the incoming layer goes from `blur(min(8/f - 8, 100)px)` and opacity f^0.4 to sharp while the outgoing mirrors it; text swapped in each frame. A "melt". Used with `MorphWord.jsx` (present at `3c88f925c`, 4 Oct): a CSS cross-fade of words in one grid cell, `interval 2800 ms`, only opacity, blur and a small transform, paused off-screen/hidden/reduced-motion. This is the "morphing text" the owner remembers ("glassmorphism/morphing hero text", ledger line 188).
2. **18 Oct, option "per-letter morph" (`HeroMorph.jsx`, L-016)**: the changing third line `No more guessing. / Every mark traced. / Know what to fix. / Fresh every time.`; letters rise 0.35 em and fade out in 240 ms while new letters rise in (IN_DELAY 120, IN 360, CHANGE 480, stagger 20 ms/letter, ease `cubic-bezier(0.23,1,0.32,1)`), each phrase holds 2600 ms, first change after 3600 ms; transform + opacity only; a phrase at rest is plain kerned text; one shared grid cell with invisible size-holder copies (CLS 0); screen readers read one stable sentence; reduced motion shows one still line.
3. **19 Oct, option C "select and type" (`HeroType.jsx`, HERO-MOTION-1019.md, D112/D115)**: old line selected from its end back over 220 ms with a 100 ms beat, then the new phrase typed per letter (30 ms + jitter, +24 ms after a space, +70 ms before the full stop, letters fade in 60 ms) behind a solid brand-colour caret (caret in 100 ms, blinks twice after the last letter, leaves in 160 ms), starts only after the first screen settles (fonts ready, entrance done, no scroll for 1.2 s), pauses on scroll, one lap then rests on "No more guessing."; flag `HERO_MOTION_V2`.
4. **19 Oct `HeroMelt.jsx` (`?hero=v3`, D119)**: last year's melt on today's headline over `HERO_PHRASES_V2`: 1.0 s melt, 1.2 s hold, new phrase every 2.2 s, rAF only during the melt, blur scaled to today's type; preview-only.
5. **1 Nov**: all five (HeroLine, HeroMelt, HeroMorph, HeroType, heroPhrases) and `hero-motion.css` (153 lines) deleted; `heroLines.test.mjs` H1 asserts they stay gone. Source of the typed/melt timings is in git: `git show f61de0206^:src/components/landing/heroPhrases.mjs`, `HeroType.jsx`, `HeroMelt.jsx`.

Reference for the new typing animation (LK74): Preparoo's typing and demo typing are in `mockmob-next/docs/brain/handoff-1104/home-research/preparoo/source/typing.txt` and `demo-typing.txt`.

## 6. Landing checklist L-001..L-045 (`mockmob-next/docs/brain/WEB-OWNER-LEDGER-2026-10-17.md:12-56`)

**Finding on the locks**: only L-013, L-014, L-019 and L-033 are named in a test; the other 41 rows carry no test id. "Locked by" below is the nearest test that asserts the same behaviour, found by reading test titles; "none found" means no test asserts it. Tags: **HERO** constrains the hero, **NIGHT** constrains Night/slop, **SCROLL** constrains scroll paging, **EXAM** constrains the exam screen, **COPY** constrains copy length/content, **KEEP** = a never-remove/never-regress rule.

| ID | One line | Locked by | Tags |
|---|---|---|---|
| L-001 | New landing is what www.mockmob.in serves; every L item passes on the live URL, no preview link | none found (process) | KEEP |
| L-002 | Ship only at critic score 88+ and no truth defects | none found (process; the owner's own checklist is the gate, the 88 is advisory) | |
| L-003 | At 390 px every section is composed for the phone first and at least as impressive as 1440 | none found | HERO, KEEP |
| L-004 | Full feature showcase, tour, scroll animations, flying Mobi (about 12 sections) stay; nothing cut for a plain list | none found (`landingPosition.test.mjs:28` locks that every position-band name is a real section) | KEEP |
| L-005 | Every earlier scroll animation and behaviour still exists and runs more fluidly | none found | SCROLL, KEEP |
| L-006 | Signed in: no guest CTA, a "Welcome back" state with an obvious Enter the Arena button | none found | HERO |
| L-007 | Hero CTA, nav and bottom bar differ for first-time, signed-out, signed-in free and paid; no upsell to paid | none found | HERO |
| L-008 | Bottom bar is ONE real button whose label follows state (guest "Try a CUET question", signed in "Welcome back", finished sample "Sign up") | `release9_public_1018.test.mjs:158-196` (demo signal: the hero key steps down after an answer, first answer announces once) partly | HERO |
| L-009 | After the 5 sample questions the dock and later CTAs say Sign up | same tests as L-008, partly | HERO |
| L-010 | Bottom/footer "Try a CUET question" works; Sign up reachable from the bottom | none found | |
| L-011 | At 390 the Start/bottom button is centred, inside the layout, not floating | none found | HERO |
| L-012 | Logo scrolls to top; every top-bar link works; a clear state-based conversion CTA in the bar | none found (`landingPosition.test.mjs:21-55` locks the band under the bar) | HERO |
| L-013 | A guest reaches a sample, sign-up and the Arena in at most 2 taps from the hero, dock and footer; no dead CTA | `release8_fixes_1018.test.mjs:183` (hero buttons show 761-899 px), `release9_public_1018.test.mjs:224` (footer Help) | HERO |
| L-014 | Hero redesigned with clean spacing, message at first glance without bombarding; every other section still present | `release8_fixes_1018.test.mjs:150` (desktop hero seat does not paint before PipGuide marks the root) | HERO, KEEP |
| L-015 | Visitors whose subject is not in the 5 samples get a clear path (subject choice or sign-up) | `heroLines.test.mjs:102` (the sample's other-subjects line survives); `heroScene.test.mjs:107` | HERO |
| L-016 | Hero headline has a visibly changing word (typed line or crisp per-letter morph), no glass, no glow | **contradicted** by `heroLines.test.mjs:34` (nothing types or cycles); superseded by ruling H1 of 1 Nov; LK74 re-opens it | HERO |
| L-017 | "CUET 2027" in the hero is brand-coloured, not plain | `heroLines.test.mjs:26` (`.lp-title__brand` uses `--accent-text`) | HERO, NIGHT |
| L-018 | "CUET 2027" is not a button that only scrolls | `heroLines.test.mjs:30` (not an a/button/Link) | HERO |
| L-019 | No glow around buttons, no sheen sweep, no light running round an edge, no drifting blobs, no gradient text | `release8_fixes_1018.test.mjs:177` (Lab Cinema glow), `release9_public_1018.test.mjs:209` (aurora gone; **but "grid and dots stay"**), `web_fixb_1019.test.mjs:50`, `landingPosition.test.mjs:55` (band never glows). The slop checklist finds 4 lime radial glows and a lit card edge still live | NIGHT, HERO |
| L-020 | No eyebrow pill/label with a dot anywhere, no decorative four-icon row; hierarchy by type and layout, not cards, pills or badges | `heroScene.test.mjs:99` (hero details band has no eyebrow, no stacked checks); kickers still present in 5 sections | NIGHT, HERO, COPY |
| L-021 | Hard-reload 5 times at 390 and 1440: hero copy and Mobi render fully every time | none found | HERO |
| L-022 | No floating subtext "Built first for commerce", "CUET commerce", "English" | none found | HERO, COPY |
| L-023 | Commerce-first positioning stays clear, via hierarchy not subtext | none found | HERO, COPY |
| L-024 | Zero defensive fine print ("illustrative", "not a prediction", "not affiliated") on any public page | `landingCopy.test.mjs:17` (no retired claim, hype word or guarantee), `pricing_copy_1017.test.mjs` | COPY |
| L-025 | All English reads correctly; one design theme matching the app; passes the 12-part anti-slop test | none found | NIGHT, COPY |
| L-026 | At 390 the "Every mark, traced back to a moment" showcase pins and steps like desktop, not stacked | none found | SCROLL |
| L-027 | With a fast wheel flick and a fast swipe each gesture advances exactly ONE slide | **no test** and **reversed by LK47 (2 Nov)**: `scrollStorySpeed.test.mjs` now forbids `preventDefault` and non-passive listeners; LK69 (4 Nov) asks for one gesture = one step again | SCROLL |
| L-028 | "What's inside MockMob" advances much slower (one slide per gesture, readable dwell) | none found (the tour is `FeatureTour.jsx`, a held `ScrollStory`) | SCROLL |
| L-029 | "What and Why MockMob" and "see where your marks went" hold the screen and step so one flick cannot skip them | `landingPosition.test.mjs` / `sectionPositionPhase.test.mjs` (held stories, the band's phases) but not "cannot skip" | SCROLL |
| L-030 | "What's inside MockMob" heading smaller, "MockMob" in green, heading and subtext animate together | none found | COPY, NIGHT |
| L-031 | At 390 every screen fills the viewport, no dead space at the bottom, key content above the eye line | none found | HERO, EXAM |
| L-032 | Repair and SWOT scene text readable on a phone (body 14-16 px, short per scene) | `labStory.test.mjs` locks the story data, not sizes | COPY |
| L-033 | No demo question time above about 3 minutes anywhere | `labStory.test.mjs:49` (named L-033) | |
| L-034 | Time scene bars differ: some under, some over the pace line, matching feedback | `labStory.test.mjs:72` | |
| L-035 | Changes scene: B green with a check, path to D crossed, D red | `labStory.test.mjs:102` (carries both verdicts) partly | |
| L-036 | Smart analysis and Replay scenes self-explanatory, nothing broken | `labStory.test.mjs:11-29` (same session and ledger) partly | |
| L-037 | The 3D calculator behind the accountancy mock behaves the same at 1440 and 390 | none found | |
| L-038 | At 390 the subject object scroller is aligned, objects large enough, gentle easing | `brand_assets.test.mjs:40-83` (objects at every width, inside tile, shadow) partly | |
| L-039 | Mobi present on the landing, homepage motion visibly better than the 15 Oct version | `landingMobi.test.mjs:17-65` | HERO |
| L-040 | Fast flick top to bottom: no glitch, flicker, jank or missed reveals; page weight and animation cost reduced | none found (`web_landing_health_1020.test.mjs:47-61` locks LCP only) | SCROLL |
| L-041 | Says plainly that every paper is fresh from one live central bank with no mock cap (rivals 10-30); not in the face; never "never repeats" | `landingCopy.test.mjs:22-48`, `heroTaps.test.mjs:51-59` (bank line, real count), `web_landing_health_1020.test.mjs:40` (share card USP) | HERO, COPY |
| L-042 | What he approved stays: Mobi, the time section, good copy, logo animations | none found | KEEP |
| L-043 | If the landing has a logo opening it uses logo B and lasts about 3 s, else N/A | none found; the site has no opening today (N/A). LK74 now asks for one | HERO |
| L-044 | No video scene live unless the owner approved its storyboard | `heroScene.test.mjs:142` (no video, GIF or frame sequence in the hero) | HERO |
| L-045 | App promoted only where a real link exists; no placeholder badges | none found | |

Other tests that constrain the new hero, Night, scroll or exam work (read their titles): `heroScene.test.mjs` (room is the app's painted file; only the shown theme's file is fetched; phones only; entrance plays once and nothing loops; reduce-motion fades only; one key, second action a quiet text link with a 44 px target), `heroTaps.test.mjs` (six lines word for word, 44-character limit, no hype), `landingMobi.test.mjs` (rigged Mobi loads on idle, first frame drawn on the server, eyes follow a mouse by under 3 px, one Mobi in view), `landingPosition.test.mjs` and `sectionPositionPhase.test.mjs` (the position band), `labTimePlays.test.mjs`, `web_landing_health_1020.test.mjs` (LCP: the headline's lines share one box), `release9_public_1018.test.mjs:121-138` (price framing "Rs 99 once, through 31 July 2027" flips to "a month" together on three surfaces).

## 7. Gaps the three designs must close (facts, not advice)

* A real, unified token set: web Night/Day vs app Night/Day (finding 2) and the volt roles (slop checklist C9: 12+ roles).
* One Mobi look per surface (finding 1) and one idea for both heroes (LK67): the hero room exists only below 761 px, the host only above.
* Hero first screen: the measured geometry is in section 8 (the headline starts at 47-52 % of the viewport).
* An entry loader the web does not have (1.4) and a typed/morphed line the tests currently forbid (5, 6).
* A real MockMob exam screen (finding 6) in well under 1.5-1.95 screens.
* Unused owned art: 13 desk icons, foil seal, stamp seal, parcels, 12 Folds, scenes other than the hero room, campus tiles are the only illustration besides subject objects.

## 8. Phone hero geometry, measured (LK70)

Local main, headless Chrome, DPR 2, touch, Night and Day identical in layout. Script `B/hero-geometry.mjs`, data `B/hero-geometry.json`, shot `B/shots/hero-375x667-night.png`, `B/shots/home-390-night-hero.png`. Numbers are CSS px from the top of the viewport; the site bar is 0-61.

| Viewport | Room (painting + Mobi + bubble) | Mobi | h1 top-bottom | Primary key | Room share of viewport (bar + room) | h1 starts at |
|---|---|---|---|---|---|---|
| 390x844 | 61-381 (320) | 182-361 (Night 179 tall; his bubble 77-116) | 393-507 | 582-636 | 381/844 = 45 % | 47 % |
| 375x667 | 61-333 (272) | 151-313 | 345-454 | 529-583 | 333/667 = 50 % | 52 % |
| 360x740 | 61-342 (281) | 161-322 | 354-459 | 533-587 | 342/740 = 46 % | 48 % |
| 412x915 | 61-381 (320) | 172-362 | 393-515 | 589-643 | 381/915 = 42 % | 43 % |

Facts: the room is 272-320 px tall whatever the phone, so on short phones (375x667) it takes half the first screen and the headline (which holds "CUET 2027.") begins at 52 %; the first words a student reads are the bubble's "Hi, I'm Mobi. Tap me." (Night shot) and the answer-sheet poster, not what MockMob is. The headline, lead and key do fit the first screen at every size (key bottoms 583-643). Below the key come the trust line, bank line and the sample card (stage 723-784 down 518 px tall, so the whole hero is 1,456-1,570 px, 1.8-2.2 screens). The hero's primary key is volt on charcoal with a 4 px solid lip (`marketing.css:250`), the bubble is a charcoal pill, the poster dots are volt.

## 9. File index

In `B/` (= `wt-1104-web-polish/tmp/home-1104/brand/`):
* Notes: `BRAND.md` (this file).
* Mobi: `sheet-ALL-MOBI.png` (master), `sheet-site-mobi.png`, `sheet-promo-mobi.png`, `sheet-promo-mobi3d.png`, `sheet-app-only-art.png`, `sheet-folds.png`, `shots/preview-mobi-acts-1440-day{,-top,-mid}.png` (rig moods + acts), `sheet-promo-kit-brand.png` (logo board B, Play feature graphic, launch splash, swatches, moods, eyes), `app-opening-goldens.png` (the "mo" opening: mo, ink, unfold), `make-mobi-master-sheet.mjs`.
* Illustrations: `sheet-subject-objects.png`, `sheet-brand-icons.png`, `sheet-scenes.png`, `sheet-desk-plates.png`, `sheet-promo-props.png`.
* Promo film: `promo-teaser-v8-frames.png`, `promo-reel916-keyframes.png`, `promo-reel916-final-r2-frames.png`, `film-stills/` (12 full-size frames).
* App exam screens: `sheet-app-exam-screens.png` (confirm, question Night, question Day, NTA console, palette).
* Home page, current: `shots/home-{390,1440}-{day,night}-*.png` (hero, statement, lab, tour, compass, eligibility, exam, exam-console, recovery, pricing, close), `og-home.png`.
* Measurements: `capture-results.json` (every type level at 390/1440 Day+Night, section heights, word counts), `hero-geometry.json`, scripts `brand-capture.mjs`, `runner-capture.mjs` (stopped run's runner walk; its result `shots/runner-error-no-subject-390-day.png` is an error frame, not used), `hero-geometry.mjs`.
