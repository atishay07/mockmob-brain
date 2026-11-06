# FamApp (Fampay) design teardown for MockMob

Date: 13 October 2026. Purpose: the owner named Fampay as the closest audience match (Indian teenagers and Gen Z) and asked for "something premium, something which inspires people to use the app". This is a reference study, not a spec. It changes no code.

## 0. How to read this: evidence and limits

Every claim carries one of these tags.

| Tag | Meaning |
| --- | --- |
| [seen] | I looked at the image or page myself (Play Store screenshots, famapp.in, archived Play listing) |
| [css] | Measured from the live famapp.in stylesheet and computed styles |
| [px] | Colour sampled from the pixels of an official Play Store screenshot |
| [listing] | Official store or site text (Play Store, App Store mirror, famapp.in, Fam FAQ and blog) |
| [third] | Third-party or vendor write-up, treated as a claim |
| [inferred] | My reading of what the evidence implies. Not confirmed |

What I could look at: 8 screenshots of the current Play listing (updated 8 Oct 2026, the post-rebuild UI), 8 screenshots of the July 2025 listing (via the Internet Archive, the previous UI), famapp.in at desktop and phone width with computed CSS, the current and archived Play listing text, the App Store text, Fam's engineering blog (3 posts), the Fam FAQ and About page, a WebEngage case study, and a Media Infoline item.

What I could not do, so do not treat these as known:
- Nobody can see a first-run or signed-in screen without an account, and I was told not to sign in. The onboarding in section 5 is therefore reconstructed from the FAQ, store listings and marketing art, and says so.
- No live motion, easing, duration or haptic data. The Play screenshots are official marketing composites (tilted phones, floating layers), not raw captures. Motion in section 3 is split into documented and inferred.
- APKMirror release notes sit behind a Cloudflare check. I did not bypass it.
- There is no public Medium, Behance or Dribbble case study from Fam's design team (searched). The only first-party design statements are job posts, which say design is central and that the brand is for Gen Z. Everything below comes from the product's own surfaces.
- Fam's Instagram and YouTube could not be read.

Name check: fampay.in and famcard.me both redirect to famapp.in. The product is now "FamApp by Trio (formerly FamPay)", company Tri O Tech Solutions Pvt Ltd, Bengaluru [listing].

---

## 1. What it is and who it is for

**Product.** A spending account for under-18s that grew into a general UPI and card app. FamX is the account: a wallet with a numberless RuPay prepaid card (issued by Trio, card face personalised with line-art doodles) plus a UPI ID on the @fam handle [listing]. Around it: bank linking (UPI 2.0, aimed at 18+), recharge and bills, gift cards with cashback, gaming codes (BGMI, Valorant, Steam), Keeper (an auto-save "digital piggy bank"), DigiGold from Rs 10, FamCoins, spinners and giveaways, and, as of the October 2026 update, Flex (a premium subscription with guaranteed cashback) and FamStudio (change your QR theme, payment sounds, scanner, home page and app icon) [listing].

**Audience.** The 2025 Play art says "for everyone above 11" [seen]. The website hero rotates the word teens, adults, everyone [seen]. So the brand is aging up on purpose: from a teen pocket-money tool to a Gen Z payment app that adults also use. The current design is correspondingly darker, warmer and less cartoonish than the 2021 doodle-led look [inferred].

**Scale and trust claims differ by surface.** Play: 50M+ downloads, 4.5 stars from about 32.6 lakh reviews, "trusted by 1 crore+ users". The App Store text says 5 crore+. The website says 10 million+ registered. These do not agree, so treat all of them as marketing [listing]. Reviews on Play are heavily about support failures (an AutoPay charged three times, accounts locked for weeks, only a chatbot) [listing]. Great surface, weak service: a warning for the "do not copy" list.

**How it is built** (matters for what MockMob can imitate) [listing, Fam engineering blog]:
- Android: native Kotlin/Java moving to Jetpack Compose. iOS: SwiftUI. Flutter modules power the whole KYC flow and the home-screen tabs, with several Flutter engines. A React PWA runs inside web views so screens ship without a release. Kotlin Multiplatform shares the core.
- The home screen is a server-driven feed (internally "Homelander"): the backend decides each card's content, layout and eligibility from user attributes, grouped into sections such as "For you" and "Quick actions". They cut p95 load from 2-4 s to a target under 50 ms with ETag caching, change-data-capture invalidation and a Go service. The product team changes cards without an app release.
- App icons are swapped at runtime with Android activity-aliases without closing the app, as a "delight feature". Customising the icon and QR theme is paid; the FAQ says the entry point is a star icon at the top right of the payment page [listing].
- The App Store lists the iOS build at about 425 MB [listing]. Heavy.

**The October 2026 rebuild.** The Play text from September 2026 says the app was rebuilt from scratch around one idea, speed: the camera is ready the instant you launch, swipe down to search and pay anyone, swipe left for DMs where you chat, pay and add notes, the homepage learns who you pay, and everything runs through gestures [listing, reported by search mirror of the listing and APK pages, [third]]. The current Play screenshots show exactly that UI. This is the design to study.

---

## 2. Visual language in concrete terms

### 2.1 Typefaces

- **Website: Metropolis** (weights 400, 500, 600, 700), the only text family loaded for body and headings [css]. Metropolis is a geometric sans in the Montserrat family tree. The app marketing artwork matches it: double-storey a, round bowls, Bold for headlines, Light for sublines [seen, inferred it is the app face too].
- **Hand-lettered accent.** The website also loads two handwriting-style faces, "Chilldranety" and "WaitingForTheSunrise" [css]. Chilldranety is used at 3.75 rem for date stamps on the careers page [css]. In the Play art, one word per headline ("UPI") is set in an amber hand-drawn, marker-like face while the rest is Metropolis Bold [seen]. That is the Fam typographic signature: one word of hand lettering in the accent colour inside a clean geometric headline [inferred it is the same family].
- **Logo.** Lowercase "fam" in a heavy geometric sans with an orange F-glyph that reads as a wing or arrow; "famX" with a diagonal amber X, "by trio" small beneath it [seen].
- **Type scale** (website, desktop) [css]: H1 53 px / 700 / line-height 1.0 (tight, zero extra leading); section H1 45.6 px / 700 / 1.17; list items 21 px / 500; body 18 px / 400 / 1.5; buttons 18-23 px / 600; letter-spacing normal everywhere. Three weights only (400/500/700, with 600 on buttons).
- **Marketing art in the app** (estimates from the screenshots, width 675 px) [seen]: headline about 8% of the image width, so on a 384 dp phone roughly 30-34 sp bold, two lines, centred, white. Subline about 5% (roughly 20 sp) in weight 300-400. Numbers in the UI (amount entry) are large and amber with a small superscript rupee sign (roughly 40 sp, with the symbol at 60% size).
- **2025 headline treatment.** Headlines were a champagne-gold gradient (about #E6B577 to #F2CA99) with a white light-weight subline [px]. The 2026 art dropped the gold gradient for plain white headlines with one amber word or a paper tag.

### 2.2 Colour (hex measured or estimated)

| Role | Hex | Evidence |
| --- | --- | --- |
| Ground, app art | #0C0908 (warm near-black, covers 60-80% of every screenshot) | [px] |
| Ground, website | #121212 | [css] |
| Raised surfaces, lists, trays | #1A1B1C, #191A1A, #121212 (cards on ground); #2A2B2A, #2E2E2E (trays and search pill) | [px] |
| Warm ambient tint | #2A180C, #2D0F00, #342518 (scanner, home), #3B2822 (chips) | [px] |
| Primary accent: amber | #FBA730 (Pay button, app art); #FBAF03 (website CTA, text on it #1C1C1C); #F9AE04 (Keeper CTA) | [px] [css] |
| Amber for text accents | #F5A623 | [css] |
| Paper tag amber | mottled #DC9328 to #ECA233 | [px] |
| Money-positive green | #0BC878 fill, #2DE89A glow text on success; #74D394 or #68BA84 for "10% back" and "Buy for" labels | [px] |
| Primary text | #FAFAFA | [px] |
| Secondary text | #A1A1A1 and #B9B9B9 | [css] [px] |
| Environment accents | indigo #0F0D2A (recharge), wine and maroon (savings, Zomato tile), purple (Myntra tile), orange #F38847 to #FFB666 (Keeper safe) | [px] |

Logic: one chromatic accent (amber) for actions and emphasis, green only when money is good (success, cashback), and all other colour comes from content (brand logos, 3D objects, the screen's ambient light). Dark only. I saw no light theme.

### 2.3 Materials

- **Warm black plus environmental light, not flat fills.** Each marketing screen has a blurred photographic or 3D environment behind it that tints the whole screen: sunset-orange low-poly architecture for scanning, a macro of a Rs 500 note, a wooden table with a receipt for the card, a pile of game controllers for gaming codes, an indigo network globe for recharge, a wine-red vignette with floating notes for savings [seen]. In the UI itself, the scanner screen keeps this: the live viewfinder is a rounded card over an orange ambient backdrop [seen].
- **Dark translucent pills and trays.** Search pill, quick-action buttons and the DM favourites tray are neutral dark (#2A2B2A range) with a hairline lighter rim and about 24-32 dp radii. Translucency is mild. This is not iOS liquid glass; the depth comes from lighting, layering and tilt [seen, inferred].
- **Die-cut stickers.** Bank, UPI-app and brand logos orbit the phones as stickers with a thick off-white border, soft shadow and 8-15 degrees of rotation. Avatars are squircle cut-outs where faces are sometimes replaced or covered by hand-drawn sticker doodles (a starburst, a flame, a crown, an arrow) [seen].
- **Crumpled-paper tags.** The caption layer is an amber crumpled-paper rectangle, tilted by 1-2 degrees, carrying a sentence-case bold line ("swipe down for quick actions" is the pattern). A grey-white paper tag with a paper-clip graphic does the same in the DM art [seen]. This is Fam's most recognisable device.
- **Halftone dots** behind the pay amount; a faint dotted field fading out toward the numpad [seen].
- **Gradients are light, not paint.** Radial glows behind phones and a diagonal gold X on the card. Controls are flat colour [seen].
- **Edge glow on tiles.** The Cashback Store tiles have 1 px brand-tinted borders with a soft outer glow (blue for Amazon, red for McDonald's, purple for Myntra), notched at the bottom like a gift-card or ticket [seen, 2025 art].
- **Shadows:** large, soft, only under floating objects (trays, sheets). Cards inside lists have none [seen].

### 2.4 Imagery

- **Rendered 3D objects on near-black** are the hero language for money: stacked gold bars stamped 24K, a glass jar of notes and coins with a target sticker and a handwritten "Savings" tag, game controllers. Cropped fully, floating, lit from above with a vignette [seen].
- **Flat vector illustration** for explainers: the Keeper safe in orange with green cash and orange ripple rings; the website's feature icons are a phone on a navy tile with a green leaf and sparkles, a QR tile, a rupee phone [seen]. Soft gradients, thick shapes, no outlines.
- **Meme and pop culture as content.** QR themes shown: a close-up cat, a hand-and-wallet meme with an "insert money here" caption, a pixel-art neon bedroom with Japanese lettering [seen]. Users pick their identity from jokes.
- **Line-art doodles** on the black card: camera, ghost, game controller, cheese wedge, cap, a dove, in white outlines [seen]. 200+ doodles was the 2021 claim [third].
- **People photography** is cropped to squircles and mixed with sticker overlays. Real teen faces are partly masked by doodles [seen]. I think this also acts as a minors-privacy device [inferred].
- **Brand logos as colour.** Gaming, telecom and shopping logos supply most of the saturated colour on otherwise neutral screens [seen].

### 2.5 Iconography

- Thin outline icons (about 1.5-2 dp stroke, white or amber) inside circles or pills: scanner frame, person with an arrow (pay self), bank columns, phone with a bolt (recharge), clock with a back arrow (history), paper clip, eye (hide or show balance), bell, send arrow [seen].
- In the 2025 build, primary shortcuts used small 3D objects on pedestal discs (App Store card, phone with a bolt, Google Play, a voucher) with a caption and a reward chip beneath [seen]. The 2026 build moves to outline icons in pill buttons, which is faster to draw and cheaper to render.
- Tab bar icons are outline, icon-only, amber when active with a small amber dot beneath [seen, 2025 Keeper screen].

### 2.6 Layout and density (current UI) [seen]

- **Home** top to bottom: a top row (squircle avatar at left, a wide search pill, a circular send/DM button with a red count badge); a rounded live camera viewfinder as the hero with a floating torch and gallery mini-pill on its lower edge; a horizontally scrolling row of shortcuts (QR Codes, Check Balance, Add Money, Vouchers, GPRC, App Store) where the last item is clipped at the screen edge to signal scroll; then "Pay to recents" as a row of circular avatars with a UPI-app badge on each. Medium density, but every element has generous radius and breathing room.
- **Search / Pay anyone:** a back arrow and search field, an 8-up grid of recent contacts (4 by 2) in a rounded tray, keyboard open, and a shelf of five quick actions floating above the keyboard (Scan QR, Pay self, Pay bank, Recharge, History).
- **Pay:** amount in large amber at the top, recipient avatar, a plain large numpad with no key outlines, then a raised sheet to choose the funding source (rows with a check or radio: bank account, FamX wallet), and a full-width amber pill CTA with dark text.
- **DMs:** a favourites strip ("Clip") of squircle avatars, then rows that read like messages (sender, a status such as "requested" or "received" with age, a send arrow at the far right), with real chat snippets mixed in.
- **Recharge:** plan cards with 1 px coloured outlines (indigo, green, amber) and a swipeable offer banner with a 1/3 pager; filter chips where the active one is amber-outlined text.
- **Density rule of thumb:** one dominant object per screen (the camera, the amount, the tray), everything else subordinate and dark.

### 2.7 Geometry estimates, useful for rebuilding the feel

From screenshots, not specs [seen, inferred]: CTA pill height about 56 dp, fully rounded. Search pill about 48-52 dp. Trays and sheets 24-32 dp radius. Avatars squircle (superellipse), not circle, at about 56-64 dp in trays, circle for recents. Sticker border 3-4 px off-white. Paper tag rotation -2 to +2 degrees. Phones in marketing art are tilted 6-10 degrees with floating parts pushed 20-40 px out toward the viewer.

---

## 3. Motion and interaction

| What | Evidence | Notes |
| --- | --- | --- |
| The camera is live the instant the app opens | [listing] | The launch screen is the scanner. First paint is the primary task |
| Swipe down from home opens search and pay-anyone; a floating action shelf sits above the keyboard | [listing] [seen caption "swipe down for quick actions"] | The gesture is advertised in the screenshot caption, so discovery is by marketing, not by UI |
| Swipe left opens DMs: chat, pay, notes, clipped favourites, history search | [listing] | Payment history is modelled as conversations |
| Home feed returns in under 50 ms (target) with about 1 s staleness allowed | [listing, engineering blog] | Perceived speed is a headline feature, not an engineering footnote |
| Payment success: green check in a filled circle, concentric rings, small confetti shards, and a line stating how long it took (0.21 s in the art) | [seen, 2025] | Speed is bragged about. Money-positive green appears only here and on cashback |
| Hide or show balance with an eye toggle. In the 2025 build the hidden balance displays money-face emoji instead of dots | [seen, 2025] | Humour inside a privacy control |
| Carousel offer banner with "1/3" and dots; horizontally scrolling chips and shortcut rows with a clipped last item | [seen] | Scroll affordance by clipping, no arrows |
| Active tab: amber glyph plus a small amber dot | [seen, 2025] | Minimal indicator |
| Payment sounds and QR theme are customisable; app icon changes without a restart | [listing, blog] | Sound exists as an opt-in personalisation, not a default |
| Website: the hero word rotates teens, adults, everyone; sections stay blank until scrolled, then reveal | [seen] | Standard scroll reveal; nothing special |
| Haptics, spring curves, durations, shared-element transitions | not documented | Cannot be known from public material. An owner screen recording would settle it |

Marketing-only motion language, which I would not expect in the app but which shapes the brand feel [inferred]: phones tilted in 3D, UI trays and sticker logos pushed out of the device plane, light blooms. This is a composite look. The in-app equivalent is the floating shelf above the keyboard and the raised funding-source sheet over the numpad.

---

## 4. Navigation, described so the feeling can be rebuilt

**2025 build [seen].** A bottom bar of four to five icon-only outline glyphs on the near-black ground with a hairline top border: bank/account, the X (FamX), scan, safe (Keeper); earlier versions also had home, a trophy for Rewards and a gamepad for Games [seen on the website phone image]. Active tab: amber glyph and a small amber dot under it. No text labels, no pill, no raised bar.

**2026 build [listing, seen].** Navigation moves into gestures and the top bar:
1. **Home is the camera.** The scanner is the first thing seen. Over it: a top row with avatar (left), a long search pill with the action in plain words (centre), and a circular send/inbox button with a count badge (right).
2. **Pull down = search and pay.** Search sits above everything: contacts, UPI IDs, phone numbers, recharges, transfers. A five-item shelf (scan, pay self, pay bank, recharge, history) floats above the keyboard as a slightly tilted tray with a lighter rim.
3. **Swipe left = DMs.** A message-style list of people and merchants with amounts as status lines, a favourites strip of squircles with a paper-clip "Clip" slot at the start, a send arrow on each row.
4. **Quick actions at the top of home**, driven by the server feed (recharge and bills for those who recharge, App Store codes for iOS users, Google Play codes for Android users) [listing].
5. **Bottom sheets** for confirmation choices (which account to pay from) rather than new screens.
6. **FamStudio** (new, October 2026) opens a customisation space: scanner, home page, QR theme, sounds, app icon [listing].

**What to rebuild:** the sense that you are always one gesture from the main task, the top row that is the same on every screen (avatar, action pill, inbox circle), floating trays instead of a fixed bottom bar, and sheets that rise over the content instead of replacing it.

---

## 5. Onboarding and first run

Be clear about the limit: I could not see the signed-in first run. What exists in public material:

**Compliance onboarding (the part that is documented)** [listing, FAQ]:
1. Aadhaar is mandatory, in the user's own name; a parent's Aadhaar cannot be used. The phone number linked to Aadhaar must receive an OTP.
2. Aadhaar verification through DigiLocker.
3. Selfie verification: allow the camera, keep the face fully inside a circle.
4. Names must match Aadhaar and PAN exactly (PAN needed above Rs 50,000 a year).
5. A guardian's mobile number is collected for minors and cannot be changed.
6. KYC attempts are limited. Video KYC carries a fee. Verified details cannot be edited later.
7. Card: tap Order Card on the FamX page; the physical card costs Rs 249 and arrives in 7-10 business days; a virtual card is activated with a code and the last six digits.
In 2020 the flow was parent-first with the teen invited, or teen-first with parental consent [third]. A vendor case study claims the onboarding funnel doubled after push, SMS and WhatsApp campaigns, and teen transactions rose 22% in six months [third, WebEngage]. These are the vendor's own numbers.

**Where the personality arrives: identity moments after the compliance gate** [seen, 2025 art]:
- **Pick your UPI ID.** The art shows toast-style cards "Name created handle@fam" with funny handles. You choose a name for your money identity and it can be a joke.
- **Pick a QR theme.** Memes, pixel art, photos.
- **Design your card** from doodles.
- **First feature intro (Keeper),** the only explainer screen visible: a dark green radial-lit screen with a vector illustration of an orange safe full of cash, a small caps eyebrow ("What is Keeper?"), a two-line bold headline (the digital piggy bank, but cooler), one grey line, a single amber pill CTA ("Start saving now"), and the icon-only tab bar still visible beneath. One illustration, one claim, one button. No slides.
- **First payment:** the success screen described in section 3.

**What the pattern teaches** [inferred]: Fam does not try to make KYC fun. It gets the unavoidable gate done as plainly as possible, then spends its personality on choices that make the account feel owned. The marketing sequence (store listing, then identity customisation, then first payment) is the emotional onboarding. There is no tutorial carousel anywhere in the material.

---

## 6. Copy voice (Indian Gen Z English)

Patterns, with my own MockMob-flavoured equivalents so nothing is copied.

1. **Direct verb-first, plain.** Labels name the thing: pay, scan, recharge, clip. No feature jargon. Equivalent: "Repair this mistake", "Start 10 minutes".
2. **Captions as an aside on a paper tag.** Lowercase-sounding sentence-case lines that tell you what to do or what is special, one per screen. Equivalents: "swipe left for your mistakes", "10 minutes, one topic".
3. **Release notes with a wink.** The 2025 notes are written as a friend: a nickname for the people it concerns (the 18+ gang), a joke about growing up (the update is called "adulting"), a stretched word for excitement, and a throwaway admission that bugs were fixed. Emoji all through [listing]. Equivalent: "Mock analysis is faster now. Also fixed a few things we broke. Sorry."
4. **Self-owning identity humour.** Sample handles in the art make jokes about being broke or rich [seen]. Equivalent: a study card with a handle like "lastminute.legend" (user chosen).
5. **Hinglish where it is natural.** A sample DM line is in Hinglish (asking a friend to send money), and the site's featured testimonial opens in Hinglish with a goat emoji [seen]. Equivalent: sparing Hinglish in captions and empty states ("Aaj ka target pura?"), never in instructions that need precision.
6. **Plain superlatives.** "Most exciting", "most rewarding". Tolerated on a marketing page; I would not carry them into the product.
7. **Speed as proof.** A concrete measured time on the success screen (0.21 s). This one is worth copying because it is a fact about the user's action.

One direct line for tone reference only: the Keeper intro calls itself a digital piggy bank "but cooler" [seen]. That is the register: deflate the grown-up idea, then the benefit.

Emoji are used heavily in store text, release notes and blog titles, not in the core pay screens [listing, seen]. Exclamation marks are frequent in marketing, scarce in the pay flow.

---

## 7. The 10 most transferable ideas for MockMob

Context for every item: Galaxy M06, Dimensity 6300, 3.5 GB RAM, 720 x 1600 at 300 dpi, which is about 384 x 853 dp. Pre-rendered bitmaps are cheap; live blur, shaders and large layers are not. Integrity rules from section 5 of owner-materials.md stay in force.

**1. Open on the next move, from a cached server-driven feed.**
Fam: the camera is live on launch; the home feed is a server-driven card list with sub-50 ms cache hits.
MockMob: Today paints in under 100 ms from the last known server payload (cached, with ETag), then updates. The top card is the one thing to do now: resume a half-done mock, a due fresh check, or a 10-minute repair. Product can reorder cards without a release. Splash under 600 ms.
On the M06: one list of cards, no splash video, cached JSON in local storage, skeleton only if there is no cache.

**2. A gesture grammar with visible fallbacks.**
Fam: swipe down for search, swipe left for DMs.
MockMob: swipe down on Today opens search over topics, chapters and PYQ themes; swipe left opens the Mistake inbox, where each wrong answer is a thread: the question, what you chose, the fix, "repair this". Both gestures also have a labelled button, and TalkBack gets named actions.
On the M06: a drag-driven sheet with a fixed-size layer, nothing re-laid-out per frame.

**3. One pill search plus a floating shelf of five actions.**
Fam: avatar, a wide search pill and an inbox circle on top; a tilted shelf of five actions above the keyboard.
MockMob: the same top row on every tab (avatar, pill that says what it does, mistake inbox with a real count). A shelf of Mock, Practice, Repair, PYQ, Notes floats above the keyboard in search. This is also the owner's "compact floating dock" answer for when a bottom bar is needed.
On the M06: solid translucent fill (about 80% charcoal) with a 1 px lighter rim and one soft shadow. No BackdropFilter inside scrolling content; at most one blurred layer behind the dock.

**4. A warm-black, environment-lit ground instead of flat paper or flat charcoal.**
Fam: near-black with a blurred, tinted environment that changes per screen.
MockMob: Night world as the hero identity: charcoal ground with one soft light field per section (volt-green aurora for Practice, warm amber for Review, cool indigo for Learn). Pre-rendered 360 x 640 WebP backdrops of 20-40 KB, upscaled, no per-frame work. Light theme stays as a composed option.
Caution: keep it restrained. The owner has also said he dislikes over-lighting.

**5. Rendered 3D objects as subject identity.**
Fam: gold bars, a jar of money, controllers.
MockMob: each Commerce subject gets one generated 3D object: a ledger and calculator for Accountancy, a briefcase for Business Studies, a coin and graph for Economics, a book and quill for English, a compass for General Test. ChatGPT or Codex generates them on transparent backgrounds. Used large on the subject picker and in the subject's hero, at 400 px WebP, 25-40 KB each. Replaces the identical white keycap rows in the subject list.
On the M06: bitmaps with a Hero transition and a slow float (transform only, 4 px, 6 s loop). Off under reduced motion.

**6. Die-cut stickers and paper-tag captions instead of footers.**
Fam: die-cut logo stickers, doodle overlays on avatars, a crumpled amber caption tag.
MockMob: Mobi in seven poses as die-cut stickers (white border, soft shadow, slight tilt). One caption tag per screen in lime paper or masking-tape style carrying the exciting line ("Your first mock is a map of where the marks went"), at the top of the hero rather than a disclaimer at the bottom. The tag is a small PNG with a subtle texture (under 20 KB). Do not copy the exact crumple-and-amber look; pick a different material.
On the M06: static images, rotation applied once at build time.

**7. "Build your CUET card" onboarding, replacing the five-question sample.**
Fam: the identity moments (UPI ID, QR theme, doodle card) are where it delights.
MockMob: onboarding assembles a card the student will recognise as theirs, one decision per screen, each answer visibly changes the card instantly:
1. Cold open: dark, Mobi greeting, one line, one button.
2. Target: course and college group; the card header changes.
3. Subjects: tap your five; each arrives as a sticker on the card.
4. Rhythm: time per day and how ready you feel; the card shows a weekly goal ring.
5. Handle and sticker: a name for your card (the joke moment).
6. A short real diagnostic from the subject bank, ending in the sealed-sheet recap reveal; the account is requested here, after value, with work carried over.
Skippable, with a step count. It scales across subjects because the card is data, not a bundled quiz. Needs the owner's confirmation on length and where sign-up sits (see owner-materials.md conflict 2). No exam date is shown unless it is an official, sourced date.
On the M06: one persistent card widget animating transform and opacity only, 60 fps.

**8. A measured-time success moment, after the server confirms.**
Fam: the payment success line states how long it took, with a green check, rings and confetti shards.
MockMob: when a repair is acknowledged by the server, show the real measured time and the real next step: a check in a volt circle, two rings, a short shard burst (under 1 s), a haptic tick, and "Repaired in 4 min 12 s. Fresh check unlocks tomorrow." Never before acknowledgment, never after a poor result, once per event id.
On the M06: 12-16 drawn shards on a single canvas, no particle library, 700 ms.

**9. Point-of-action progress chips, predictable not random.**
Fam: coin multiplier and cashback chips beside each action (1x coins, win 2X, rupees back).
MockMob: each practice tile carries a small chip that states what completing it changes, with a real denominator: "2 of 3 repairs this week", "Unlocks a fresh check". No random rewards, no spinners. The chip is a 24 dp pill, tonal fill, tabular numerals.
On the M06: text and fill only, no animation beyond a 150 ms count-up when it changes after server acknowledgment.

**10. A voice with a personality, written as a friend.**
Fam: release notes and captions that joke about growing up, address a group by nickname and admit bugs.
MockMob: captions, empty states and release notes written as a slightly teasing senior who passed CUET, specific to the exam and Delhi University, light Hinglish in captions, no invented numbers and no claims of recovered marks. Replaces the defensive footers. Non-affiliation lives in About and the Play listing.
On the M06: zero cost. Biggest effect per rupee on this list.

---

## 8. What not to copy, and why

- **Amber and black as the palette.** It is Fam's brand. MockMob's lime (volt) accent is the distinguishing asset. If the brand is redesigned, do not drift into gold on black.
- **The crumpled-amber paper tag, the doodle card, the X glyph, the F glyph, the "Fam" naming, the "Clip" favourites and the "DMs" label.** These are recognisable Fam signatures. Take the idea (a caption layer, identity customisation, payments as conversation) and give it MockMob's own material and names. Copying the look is an off-brand risk and a legal one.
- **Metropolis as the exact type pairing.** The font is free, but using it with an amber accent would read as Fam. Keep the Gabarito and Hanken pairing, or choose a distinct family if the brand changes.
- **The coin, spinner and giveaway economy, and sold cosmetics.** Fam runs FamCoins, spinners, giveaways, cashback multipliers, and charges for QR themes and app icons. MockMob's rules forbid random and paid-random rewards and punitive loops (owner-materials.md section 5, items 9 and 10), and Pro is bought on the web only, so in-app cosmetics sales are out. Earned cosmetics, such as stickers unlocked by completed repairs, are acceptable.
- **Real teen photographs and invented social proof.** Fam shows real faces with sticker masks and sample feeds ("X created Y@fam"). MockMob must not show invented students or peer activity. Use generated illustration and real, dated, sourced counts only.
- **Inconsistent trust numbers** (1 crore, 5 crore, 10 million on different surfaces). No invented or mismatched numbers.
- **Weight.** A 425 MB iOS build, several Flutter engines, full-bleed blurred 3D environments on every screen, tilted multi-layer phone composites. None of this fits 3.5 GB RAM. Pre-render the look; do not compute it live.
- **Gesture-only discovery.** Fam teaches swipes through marketing captions. Keep a visible control and a TalkBack action for every gesture, and show a one-time hint.
- **All-caps eyebrows, emoji in product chrome, exclamation-mark successes.** Fam uses a small caps eyebrow on the Keeper screen and emoji widely. The owner's standards ban eyebrows and emoji in the product, and TalkBack reads emoji aloud. Keep personality in the sentence, not the glyph.
- **Marketing composites mistaken for UI.** Tilted phones and floating parts are advertising. Build the in-app version (a floating shelf, a raised sheet), not the poster.
- **Support that fails.** The most visible weakness in Fam's reviews is unreachable support. A premium surface with a bot-only help path hurts trust more than anything the UI gains.
- **Dark-only.** Fam appears to have no light theme. MockMob keeps both.

---

## 9. Three other Indian apps that add something Fam does not

**CRED (NeoPOP).** CRED's fourth-generation system is named after the Neo-Pop art movement. Its stated aim is that every screen should feel like a made object, and its principles are isometric drawing of objects on flat planes, linear motion and "pseudo-morphism" where objects transform into fluid displays [third]. The component library is reported to render floating 3D buttons with GPU drawing, and to ship motion guidelines [third]. Reports about the headline typeface and the exact shadow style conflict across sources, so I do not rely on them. What it adds: tactile, physical controls and one dominant, art-directed object per screen. MockMob already has a keycap button, so the take-away is to make the screen's single hero object (the answer sheet, the repair card) the art-directed element.

**Jupiter.** Jupiter's design team says its redesign made numbers the focal point through type, colour and position, whether a balance or a monthly spend, and claims a 4% lift in day-zero onboarding and funding [third; the page itself blocked direct reading, so this comes from the search summary]. What it adds: the data point is the hero. For MockMob this means the repair count, the mock score or the weekly goal ring is the largest type on its screen, in tabular numerals, before any illustration.

**Seekho.** Seekho's Play listing (100M+ downloads, number 5 free in education, updated 8 Oct 2026) describes a Hindi-first "edutainment" platform with short video courses taught by creators called Gurus [listing]. Its screenshots [seen] pair a heavy Hinglish all-caps headline in white and orange with a tilted phone framed by an orange-to-violet gradient rim and large gradient circles, and a "Recommended" rail of poster-style creator thumbnails with bold typographic covers and category chips. What it adds: content as posters, and Hinglish at full volume. For MockMob's Learn tab, topics can be generated posters with a bold two-line title rather than text rows. Weight caution: all-caps is the owner's rejected style for eyebrows, so keep the poster idea and drop the capitals.

---

## 10. What a real-device pass would add

If the owner screen-records the real FamApp on his phone (first launch, swipe down, swipe left, a payment, opening FamStudio), the gaps in this report close: haptics, easing and duration, the actual first-run screens, the empty states, and how the shelf and sheet animate. That is the one thing public material cannot supply.

## Sources

- famapp.in (home, about, careers CSS and assets): https://www.famapp.in/
- Play Store listing, current: https://play.google.com/store/apps/details?id=com.fampay.in
- Play Store listing, July 2025 snapshot (Internet Archive): https://web.archive.org/web/20250716080611/https://play.google.com/store/apps/details?id=com.fampay.in&hl=en_IN
- App Store listing (older text): https://apps.apple.com/in/app/famapp-by-trio-upi-card/id1499806454
- Fam engineering blog: https://blog.famapp.in/ (tech stack, 50 ms home feed parts 1 and 2, dynamic app icon)
- Fam FAQ: https://www.triotech.co.in/faqs/
- Fam Insider (Media Infoline, 17 Sep 2026): https://www.mediainfoline.com/tag/famapp-fam-insider
- WebEngage case study: https://webengage.com/resource/case-study/fampay-witnesses-increase-in-transactions/
- CRED NeoPOP (Homegrown): https://homegrown.co.in/homegrown-voices/cred-s-new-design-philosophy-channels-the-unbridled-creative-spirit-of-the-neo-pop-art-movemen
- Jupiter design principles (summary only; direct read blocked): https://life.jupiter.money/design-principles-at-jupiter-f783457c976d
- Seekho Play listing: https://play.google.com/store/apps/details?id=com.seekho.android
