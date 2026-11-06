# Reference teardown: HIGH (high.live), website and app

Researched 13 Oct 2026 for the MockMob redesign. Everything below was observed directly unless it is marked "estimate" or "inferred". I did not sign in, submit a form, download or install anything. The owner's note on HIGH was that the app is "just crazy"; this is what is actually there.

## 0. Evidence and limits (read first)

- **Observed live:** the full high.live landing page (desktop 1440x900 and a 390x844 phone emulation), the login page (/auth/login), the first onboarding screen (/onboarding/mobile), the page's own CSS, its fonts and image assets, and the compiled JS strings of the web app.
- **Observed as images:** six App Store screenshots and six Google Play screenshots (same set), plus the three phone-screen stills the landing page uses (home, "1st TRADE" badge, "Today's Hot Movers" story).
- **Read as text:** the App Store and Google Play listings, version history, "What's new", and the public reviews and developer replies on both.
- **Not observed:** the native app itself (no install allowed), any hover states in a real pointer session (read from CSS instead), haptics, or any in-app onboarding screens. The in-app onboarding below is assembled from the web onboarding, the store text and the reviews. Where I infer, I say so.
- **No public design write-ups exist.** I searched for case studies, agency credits, press and interviews (Dribbble, Behance, Medium, trade press, Instagram, YouTube). I found none. The product is about six weeks old (iOS 1.0 listed 28 Aug 2026, 1.0.4 on 1 Oct), so this is first-hand inspection only.
- **Treat HIGH as a style reference, not a UX-quality reference.** Ratings are 3.1 on Google Play (42 reviews, 5K+ installs) and 3.5 on the App Store (13 ratings). The loudest complaint is a 15-minute signup. Section 8 uses that.

## 1. What it is and who it is for

- **Product:** HIGH is a stock, F&O, ETF, IPO, commodity and digital-gold trading app for young India. Tagline on the site: "A trading app for a new generation". Browser title: "Get in early. Trade the culture." The store pitch is "built for investing, not gambling". Instagram bio, paraphrased: your future called, it said download HIGH.
- **Who is behind it:** Play developer is TrueStock; the App Store developer is Truestock Universe Private Limited. The SEBI-registered broker named in the footer is Choice Equity Broking Private Limited. Support: care@high.live. Handles: Instagram @high.rebels (about 7.3K followers), X @GetHighApp, YouTube @GetHighClub.
- **Audience:** 18+ (a demat account is required), first-time and early traders who grew up on Instagram, memes and streetwear. The site says it is built for how "young India actually trades".
- **Business context on the page:** waitlist counter 69,656 of 75,000 seats claimed; 1,000 "founder" seats already gone; flat Rs 10 per order; Rs 0 to open. The "cut the line" referral ladder is a growth mechanic, not a design pattern to copy (section 8).
- **Why it matters for MockMob:** it is the clearest local example of a serious, regulated, number-heavy product that dresses like a youth brand and still keeps its data screens readable. The brand layer (stickers, hues, type) and the data layer (dark, tight, tabular) are deliberately separate. That separation is the main lesson.

## 2. Visual language in concrete terms

### 2.1 Two systems, one brand

HIGH runs two visual systems that share a logo and a voice.

| Layer | Where | Look |
|---|---|---|
| **Candy layer** | Marketing site, store art, reward moments | Saturated violet / indigo / pink / coral chapters, 3D baked objects, die-cut stickers, monumental condensed caps, photo flat-lays. |
| **Tool layer** | The app's data screens, the web console, login and KYC | Near-black grounds, one lime accent, green/red for up/down, small tight Manrope-style text. |

The app screens in the store art (Titan chart, BUY pad, watchlist) are all dark. The candy layer wraps them: it frames the phone in the art, it does not run through every row of the UI. The web login and KYC use black plus lime and are visually much plainer than the landing page.

### 2.2 Typefaces (identified from the page's own font loads)

- **Display: Roc Grotesk Compressed** (ExtraBold 800 and Bold 700, self-hosted OTF; commercial, by Typofactur). Fallback stack: Big Shoulders Display, then Manrope. Used uppercase for the wordmark, chapter headlines and numerals.
- **Condensed fallback in the web console: Anton** (OFL). The onboarding tracker title and the login headline use it.
- **Text and UI: Manrope** (weights 200 to 800, Google Fonts), mostly 600 to 800. The web console and KYC form use **Space Grotesk**.
- **Handwriting accent: Permanent Marker** is loaded; I did not see it on screen.
- **Mono: system monospace**, 22px bold, +2.5px tracking, for the curved market ticker that wraps above the phone.

### 2.3 Type scale and weights (desktop CSS, measured)

| Role | Spec |
|---|---|
| Hero wordmark "HIGH" | Roc Grotesk Compressed 700 to 800, uppercase, `clamp(52px, 12.5vw, 210px)` times a scale var, line-height 0.82, tracking about -0.004em. On a 1440x900 screen the cap height is about 36 percent of viewport height and the word is about 480 px wide. On a 390-wide phone it is about 255 px wide and 175 px tall. |
| Chapter headlines | Roc Grotesk Compressed 800, uppercase, `clamp(3.6rem, 13.5vh, 9.5rem)` (58 to 152 px), line-height 0.9, tracking +0.004em, balanced wrap. Two tones per headline: line one in deep ink, line two in white. |
| Chapter sub | Manrope 600, `clamp(16.5px, 1.6vw, 23px)`, line-height 1.55, max 46ch, balanced. |
| Section headline on white sheets | Manrope 800, about 46 px with -0.03em tracking (38 px with -0.025em in a narrower case). One word swaps to a violet-to-magenta gradient fill. |
| Eyebrow / tagline | Manrope 600, 13.8 px, uppercase, +3.6 px tracking. |
| Marquee strip | Manrope 800, 14 px, +3.4 px tracking, white on violet. |
| Tab labels | Manrope 800, 11.5 px, uppercase, +0.09em. |
| FAQ question | Manrope 700, 18.5 px; numerals 01 to 06 in small violet. |
| App headings (from store art) | Condensed display, sentence case for editorial titles ("IT turns weak"), all caps for badges and tabs (BUY, SELL, "YOU ARE SUPER"). |
| App meta text | Manrope-like 11 to 13 px, light weight, grey on black (small and low-contrast; see section 8). |

Rule of thumb they follow: display type is huge or it is absent. There is almost no middle size.

### 2.4 Colour (exact where read from CSS, estimate otherwise)

- **Landing ground:** `#08080C`. The page is a set of rounded "frames" on this near-black, 14 px in from the edge, radius 34 px.
- **Hero (estimate):** pale lavender, about `#E9E1F7` in the centre to `#C9B8EC` at the edges, over a soft pixel-mosaic and film grain. The CSS fallback is a deep gradient from `#2A2476` through `#6A49BD` to `#ECB0E2`.
- **Phone section:** a WebGL speed-line burst in green (about `#1FA64F` with lime `#A8D820` and white streaks).
- **Four chapter hues (exact):**
  - Trade: `#8B5CF6`, gradient `#A87DFF` to `#8B5CF6` to `#6D3BE0`
  - Live: `#4F6DF5`, gradient `#7D93FF` to `#4F6DF5` to `#3743CF`
  - Discover: `#EE4F9E`, gradient `#FA7FC3` to `#EE4F9E` to `#C22A78`
  - Collect: `#FF6157`, gradient `#FF8F7D` to `#FF6157` to `#E03B44`
  - Each is a 168 degree linear gradient plus a radial white highlight at 74 percent / 8 percent, alpha 0.30 to 0.32. Headline ink per chapter is the same hue family in a deep shade: `#2A1168` for Trade (exact), a navy for Live, a wine for Discover, `#5F1310` for Collect (the last two are estimates).
- **Tool-layer tokens (exact, from the web CSS):** bg `#050506`, bg-2 `#0C0D10`, card `#111317`, card-2 `#16181D`, line `rgba(255,255,255,.08)`, ink `#F4F5F7`, ink-soft `#B7BCC6`, ink-mute `#6F7682`, bull `#2EDF6A`, bear `#FF3B4E`, accent lime `#BFFD03` with ink `#131F00`, violet `#8B3DFF`, magenta `#E11FD0`, gold `#F5B23D`, teal `#2FD9C4`, blue `#5B7CFF`, radius 22 px.
- **Note for MockMob:** MockMob's volt is `#D2F000`. HIGH's console lime `#BFFD03` is a close neighbour. If we move toward black grounds, a lime button and a condensed headline, we would look like HIGH's login page. Keep volt as the action colour, but let chapter hues and our own mascot carry identity.
- **Reward-moment palette:** a purple capsule (about `#5B2A86` to `#2A1044`) with gold foil (about `#E8CF8E`) on pure black.
- **Story-card palette:** warm gouache (marigold, tomato red, teal, navy) dissolving into one flat maroon (about `#6B2B33`) block for the text.

### 2.5 Materials

- **Glass is mostly frosted, not see-through.** The nav is `rgba(233,231,233,.86)` with `blur(24px) saturate(1.5)`, a 1 px `rgba(255,255,255,.5)` border and a soft long shadow (`0 10px 30px -18px rgba(20,16,40,.3)`), radius 20, height 58. At 86 percent opacity the blur is barely visible; the look is "frosted paper". Saturation boost (1.35 to 1.8 on the other glass pieces) is a large part of why it feels juicy.
- **Glass recipes found on the page:**
  - **Tab tray:** white 24 percent, 1 px white 44 percent border, `blur(18px) saturate(1.35)`, radius 18, a 1 px inner top highlight at 45 percent white, a tinted drop shadow (`0 24px 48px -22px` in a dark hue-matched colour).
  - **Store buttons:** white 97 to 93 percent gradient, `blur(18px) saturate(1.6)`, pill radius, shadows `0 28px 56px -20px rgba(34,12,84,.55)` plus `0 8px 20px -12px rgba(34,12,84,.34)`, an inner 1 px white top edge and a faint violet inner ring.
  - **Dark chips:** `rgba(7..10,..,.58..78)`, `blur(8..12px)`, 1 px white 12 to 14 percent border, inner top highlight 10 percent.
  - **Coloured glass chips:** gradient fill (purple `#4A1596` with a pink radial; or green `#178A52` to `#0A3D28` with a mint radial), coloured glow shadow (`rgba(150,20,200,.68) 0 22px 50px -18px`), inner top highlight 22 to 35 percent, inner bottom shade 55 percent.
  - **Pricing sheet:** `blur(28px) saturate(1.8) brightness(1.12)` over art, top radius 30, double inner white highlights (95 and 55 percent), a drag-handle bar, and a scalloped "receipt" bottom edge.
- **Gradients:** every chapter is a three-stop diagonal plus one soft radial highlight. No mesh gradients, no noise on the chapters themselves.
- **Grain:** the hero has an SVG fractal-noise layer at 45 percent soft-light (140 px tile) and a 58 px faint grid masked to the edges. The story illustrations carry real risograph-style grain.
- **Shadows:** long, low-opacity and hue-tinted (never neutral grey) on light grounds; heavy black on dark.
- **Glow:** lime text-glow on the HIGH word in the tool layer; green glow behind the BUY header. Used sparingly.

### 2.6 Imagery

This is where HIGH spends its taste. Five kinds, all cut out or art-directed, never stock.

1. **Baked 3D objects with alpha:** a silver "THE HIGH CLUB" coin, a chrome bell, a glossy pink flame heart, a veined green-iris eyeball, red octopus tentacles, an engine, a gold coin, an airplane on clouds. They look 3D but ship as flat WebP files ("baked" in the folder name).
2. **Die-cut stickers:** pink lips with a rainbow-drip tongue, pixel "deal with it" shades, a mint skull with gold teeth, "NOCAP" and "GOAT" tags, "CRAZY" graffiti, "awesome" handwritten pill, "INVEST BY VIBE" neon pill, a pixel heart, a pixel hand cursor. All have a white keyline and a soft drop shadow. Some are real meme photos (a screaming child, a troll face).
3. **Collectible cards:** portrait art cards named like sectors (a truck-art "strong order book", neon-chrome "AUTO GEARS", a pastel "SNACK" table, a red-telephone "TELECO"), rotated about 6 to 10 degrees. They are the Collect tab.
4. **Editorial illustration:** the "Today's Hot Movers" story: a flat gouache scene of two men in a red pickup with a white scribble road, full-bleed to the top, fading to flat maroon where the title sits.
5. **Photo and video:** a greyscale flat-lay (Instax camera, headphones, stickers, washi tape, a phone on a grid mat) that zooms in and turns purple; an art-directed pink y2k "tile bathroom" scene with a disco ball, neon wings, a bow-wearing skull and a nail-art hand holding a phone with a stacked-card watchlist; four portrait posters (a highway sign reading "the stock market has enough apps, it needs culture", a neon-lit portrait, a sky poster).

**Cropping and composition rules:** objects bleed off the frame edges at the corners; the centre is left empty for the headline; four to six props per scene, each at a different rotation; props overlap the text zone only at the edges. Phones are shown in 3D perspective with a slow sway, or held by a hand with long decorated nails (store art).

**Asset weights (cheap):** the 24 sticker and object files total about 1.18 MB (1 to 120 KB each, 200 to 760 px wide, WebP with alpha). The three in-phone screens are 26 to 73 KB. The hero poster is 179 KB.

### 2.7 Iconography

- **In-app tab icons are puffy and filled:** house, a chart on a screen, a ringed planet, a wallet, binoculars. They have a soft metallic gradient and rounded geometry, almost clay. Active is bright white; inactive is mid-grey. No labels in the landing phone (Play screenshots show labelled variants such as Watchlist, Explore, Portfolio, Profile).
- **Utility icons are thin line icons** inside glass or pearl circles (search, star, SIP, gear, back arrow, share).
- **Two circle-button materials:** dark glass (search, back, settings) and pearl white (the grid button, the binoculars action). Pearl signals "primary utility", dark glass "secondary".
- **Emoji and glyphs** are used as punctuation in the Play copy and in a few chips (fire next to a hot stock).
- **Logo:** a four-glyph stack, "HI" over "*H", italic heavy, white fill with a black outline, drawn like a sticker. The app icon is that mark on black.

### 2.8 Layout, composition, density

- **Marketing:** one idea per screen height. Centred type, huge margins, objects at the corners. The pinned phone section is a full-viewport stage.
- **Frames:** content sits in rounded sheets that stack over each other as you scroll (radius 30 to 34, 14 px gutters), like cards in a deck.
- **App:** tight. Rows about 64 to 72 px, 11 to 13 px meta text, small coloured pills for percent change (solid green with dark text for up, solid red for down), and big condensed numerals for the single number that matters (price, multiplier, balance).
- **Density is zoned:** loud art at the top of a screen, quiet dense rows below, one hero card in the middle ("What's cookin'", a gradient card with tags and a tilted polaroid photo).
- **Section dividers** are tiny: a hairline with a diamond terminal on each side around a small uppercase label.

## 3. Motion and interaction

Everything here was read from the page CSS and JS (so values are exact) and confirmed on screen where possible.

### 3.1 Choreography (marketing)

- **Smooth scroll:** Lenis (inertial). The hero is a card that shrinks from an edge-to-edge frame into a smaller rounded card on black as you scroll.
- **Pinned phone stage (about 1,800 px of scroll):** a WebGL fragment-shader backdrop of green speed lines with sparkle (`speed 1.3, density 12.5, zoom 1.75, vignette 0.41, sparkle 1.43, warp 1.3`). It has a "cursor lens" that bulges and swirls near the pointer (desktop only). It requests the low-power GPU, no alpha, no antialias, and checks reduced-motion.
- **Phone pose loop:** `perspective(1500px)`, rotateY from -12 deg to +10.5 deg and back to 0, rotateX about +/-2 to 3 deg, 1 to 2 deg of roll, a few px of lift, scale 1.014. The screen inside swaps between home, the first-trade badge and a story with a crossfade.
- **Ticker halo:** index prices (NIFTY, SENSEX and so on) set in per-character spans on a curved arc above the phone, with green and red arrows.
- **Stacking sheets:** the next section rises over the pinned stage as a rounded white sheet.
- **Scroll-scrubbed image sequence** (not a video file): about 61 WebP frames of the flat-lay, drawn to a canvas as you scroll. A zoom toward the phone, a purple wash, and the headline building word by word on both sides. The final pink y2k scene is another scroll-driven media element (a `video` tag with a canvas class); I did not capture its source.
- **Chapter slider (400vh track):** four chapters (Trade, Live, Discover, Collect). A glass tab tray 15 percent from the bottom shows where you are; scrolling advances it and tapping jumps. Background crossfades in 0.4 s.
- **Card fan:** four to five portrait creatives on a rotated arc (a "trail" keyframe exists in the CSS; I saw the arrangement, not the movement).
- **Footer:** a "JOIN THE WAITLIST" marquee, a ghosted giant "HIGH CLUB" wordmark that fades into the ground, legal text collapsed under a small label.

### 3.2 Micro-interactions (exact values)

| What | Spec |
|---|---|
| Headline letters in | per letter: from `translateY(.48em) rotate(7deg)`, origin bottom, to rest; `.62s cubic-bezier(.3,1.62,.46,1)`; delay `index * 26ms + .12s`; opacity `.22s`. |
| Headline letters out | to `translateY(-.4em) rotate(-5deg)`; `.24s cubic-bezier(.55,0,.8,.4)`; stagger 9 ms. |
| Chapter sub copy | in: `translateY(18px)` to 0 plus fade, `.45s cubic-bezier(.22,.61,.36,1)`; out: -18 px. |
| Sticker idle float | `translateY 0` to `-9px` to 0 with -1.2 deg rotate, 7.2 s loop (`ftFloat`); another set bobs -7 px at a fixed 9 deg tilt; a third uses `translate: 0 -10px`. Props never move together. |
| CTA hover | `translateY(-2px)`, shadow grows, `.18s`. Store buttons use `.32s cubic-bezier(.34,1.35,.5,1)`; the store icon pops with `.38s cubic-bezier(.34,1.56,.64,1)`. |
| Active tab | white tile with a lifted tinted shadow; a short underline bar under the label. Colour change `.25s`. |
| Founder chip | a sheen (a light band sweeping left to right) that runs in the first 14 percent of its cycle then rests. |
| Seats counter | number "pops" when it changes, a small "+" rises, a live dot blinks, the green glow breathes. |
| Price cell (web console) | background flashes a soft lime or red then clears (`ltpFlashUp`). |
| Route change (console) | `routeRise`: 12 px up and fade. Toast: from -10 px and scale 0.97. |
| Success | a confetti keyframe (pieces fall about 78vh with random drift and rotation). |
| FAQ | native `<details>`; the open row gets a faint violet gradient wash on its left; +/- icon swap. |
| Glow text | a looping pulse of a lime text-shadow (blur grows from 12/26 px to 20/54/80 px) on the HIGH word (tool layer); duration not read. |
| Reduced motion | handled in both CSS (`prefers-reduced-motion`) and JS (the shader checks it). |
| Haptics | none documented on the web. The native app's haptics are unknown. |

### 3.3 What moves and what does not

Motion is saved for three things: reveals (letters, sheets), idle life (floating props, sheen, glow), and feedback (hover lift, counter pop, price flash). Rows, lists and form fields do not animate decoratively.

## 4. Navigation

### 4.1 Website

- **Top strip (28 px):** a violet gradient marquee, "HIGH WAITLIST IS LIVE" with a four-point star between repeats, uppercase wide-tracked.
- **Nav pill:** floating, centred, 560 px wide (max 720), 58 px tall, 14 px under the strip. Three columns: logo left, X and Instagram centred, a "Get High" button with a tiny app-tile icon right. On a phone it drops the button and keeps the logo and the two social icons. It stays on screen in every section and sits over everything.
- **Bottom dock (always on):** two coloured glass chips side by side, 62 to 65 px tall: a purple one ("1,000 founders") and a green one ("69,656 joined of 75,000 seats"). They float 16 px above the bottom edge and do not move. This is the persistent call to action; the page has no sticky button bar.
- **Chapter tray:** a glass segmented control with four icon-plus-label tabs (Trade, Live, Discover, Collect). 7 px inside padding, 5 px gaps, each tab at least 44 px tall, active tab a white tile.

### 4.2 App (from the store art and the landing phone stills)

- **Tab bar (landing phone):** five icon-only tabs, no container. Filled puffy glyphs sit over the content; the rows beneath the icons fade and blur out toward the bottom edge, so the list seems to dissolve under the dock. Active glyph bright white; others muted grey. To rebuild the feeling: no bar background, a bottom gradient plus blur mask on the scroll view, icons about 26 to 28 dp, generous gaps.
- **Home header:** a round avatar chip at the top left, a dark-glass search circle and a pearl-white grid circle at the top right. Below, a full-bleed index strip with a green glow at the left end and a red glow at the right end.
- **Screen sections:** a small uppercase label with hairline dividers ("WHATS COOKIN'"), then one hero card, then a one-line news ticker with a flame icon and a violet sparkle separator, then "HEAT CHECK", a gold label on a striped bar.
- **Detail screens:** a back arrow in a glass circle, search / star / SIP in glass circles at the top right, a large price in condensed type, a green change line, and a row of period chips (1D, 1W, 1M, 1Y, 5Y, ALL) where the active chip is a white pill.
- **Order pad:** a full-height sheet. A big X in a glass circle at the top left, BUY and SELL as condensed words on a green curved glow header, a segmented control (`5x Delivery`, `4x Intraday`, `3x MTF`) with the multiplier in condensed numerals, then Market / Limit, then the quantity and price fields in large type.
- **Portfolio:** a Positions / Holdings segmented glass toggle at the top; then three summary numbers (1D return, total return, balance in large condensed digits) and a stack of fanned coloured cards, one per holding in the company's brand colour, each showing a short name and the percent in a strip.
- **Watchlist:** the user can name it (one demo is named with slang and a skull sticker), the header number is lime with a glow, rows have a logo circle, a name, price, and a solid green or red percent pill; dividend chips sit on small rows.

## 5. Onboarding and first run, screen by screen

What follows mixes observed web screens (marked O), strings read from the web app bundle (S), store text (T) and reviews (R). The native in-app first run was not visible.

1. **Before install (O).** The hero: giant HIGH wordmark, the tagline, two white pill store buttons, then "Founders are in. You're next." over two glow chips. Props frame the type at the corners.
2. **Store page (O, T).** Six portrait posters read as a story: "Break the default", "Your market crush list", "Can't choose?", "Blink and you've traded", "Where the heat at?". Each pairs two to three words of condensed headline with one phone and two to four stickers. The art does the persuading; the text lists are secondary.
3. **Signup entry /onboarding/mobile (O).** A dark card on black with a lime glow behind the logo: a condensed uppercase title ("Open a free demat account"), a two-line sub, a phone field with a "IN +91" prefix and a 9876543210 placeholder, a lime link "Have a referral code?", two pre-ticked lime checkboxes (terms and consent; WhatsApp updates), and a full-width lime button "Send OTP" that renders dimmed olive (so, inferred: disabled until the number is valid). A grey regulatory block at the foot. This screen carries none of the candy layer.
4. **Login /auth/login (O).** A dark-lime gradient header with a two-line condensed title whose last word is lime and glowing, a one-line sub, a "Welcome to HIGH" card with a Mobile number / QR code segmented control (lime pill active), a trust line with three lime initial avatars, a phone field, a lime "Continue", and "New here? Sign up". The trust line claims a very large trader count that does not match the waitlist counter (section 8).
5. **KYC wizard (S, O for the tracker CSS).** Four phase titles ("Let's Get Started!", "Personalize Your Experience!", "Secure Your Account!", "Unlock Your Investment Power!") and seven steps: verify email, confirm PAN, personal details, trading segments, bank verification, nominee details, selfie verification. A tracker shows an uppercase condensed title, "Step n of 7" and a 6 px progress bar. On desktop a sticky left card repeats the brand line and a short trust list. Further flows add Aadhaar-based authentication with a live selfie, e-sign, income proof for derivatives, and a derivatives risk acknowledgement. The copy here is generic and exclamatory; it is not the marketing voice.
6. **Review reality (R).** A Play review from 15 Sep: signup took about 15 minutes, approval was slow, login failed, and "a turn off for a new gen way of trading". The developer replied on 29 Sep that it is "working on reducing friction across onboarding, approval, and login". The 1.0.x notes say "quicker signup, smoother sign in". iOS reviews praise the interface and call the AI "non-gimmicky", and complain of a non-skippable optional email field and a broken "cut the line" feature.
7. **First moments after approval (O from the landing stills, T).** Home with "What's cookin'" and "Heat check". A simulated watchlist lets you "test your ideas without putting money on the line" (T). The first real trade fires a full-screen reward: black ground, a purple capsule with a gold-foil "1ST TRADE", a huge condensed "YOU ARE SUPER!!", one grey sentence, and three controls (a dark share circle, a pearl binoculars circle, a white pill "LET'S GO!"). Badges and "drops" continue the loop (T).
8. **The takeaway.** HIGH's brand reaches the user before install and at the first reward. The middle (KYC) is plain and long. For MockMob, which has no KYC, the brand can run through the whole first run.

## 6. Copy voice

- **Pattern:** a plain statement, a beat, then a punch. Short imperatives for headlines (two to four words, full stop). Slang is rationed to about one phrase per surface; labels stay plain (Delivery, Intraday, Limit).
- **Headlines:** "Turn boring into High". "Your entire trading desk." "The market, live." "Find what moves you." "Welcome to the club." Store art: "Can't choose?", "Blink and you've traded".
- **Humour handles constraints.** The referral FAQ says it cannot pay for signups because of the regulator, and adds that it likes its licence. A discovery line ends with "not tips". Leverage copy says the limits stay visible and the decision stays yours. Compliance becomes character instead of a footer apology.
- **Questions in the user's mouth:** "What even is HIGH?" "Founders are full. Am I cooked?" "How do I climb?"
- **Testimonials are lowercase and raw,** attributed "via Instagram", so they read as found, not written.
- **Product lines are concrete:** "Flat Rs 10 an order. That's the whole menu." Charges that apply are listed once, small, directly under the price card.
- **Play description structure:** emoji-led section heads (MARKET PULSE, WATCHLISTS, IPO DROPS, STOCK SIP), each two or three lines, each ending on a wry sentence. A comparison to a "2008 government website" is the sort of specific joke that lands.
- **Legal copy:** tiny, grey, collapsed, at the foot of every page (marketing, login, KYC), never between the user and the next action.

## 7. The 10 most transferable ideas for MockMob

Each one says how it would look in a CUET prep app on a Galaxy M06 (Dimensity 6300, 3.5 GB, 720x1600). "Budget" means: transforms, pre-rendered art and gradients, with at most one live backdrop blur per screen (per the glass rules in `flutter-feasibility.md`).

### 1. Chapter hues: every subject owns a colour

- **HIGH:** four chapters, each with a three-stop 168 degree gradient, a soft top-right highlight and a deep matching ink; the background crossfades in 0.4 s as you move.
- **MockMob:** Accountancy, Business Studies, Economics, English and General Test each get a signature hue (for example violet, indigo, pink, coral, teal). The top band of Today, the subject cards and the chip fills use the hue; the reading surface stays paper or charcoal. Switching subject crossfades the band over 400 ms.
- **Looks like:** a 220 dp gradient header with a headline in two tones, and the question or list below on a calm ground.
- **Budget:** one gradient fill and one radial highlight; no blur. Cheap on Mali-G57. Check contrast of ink on each hue.

### 2. A baked sticker and 3D kit, made once

- **HIGH:** 24 objects, about 1.2 MB total, WebP with alpha, 200 to 760 px, idle bob only.
- **MockMob:** 24 to 30 pieces generated with image tools and cleaned up: a chrome calculator, a silver coin with the rupee sign, a flame, a ledger, a stack of notes, a pencil, a die-cut "no cap" style tag, pixel hearts, plus Mobi in six more poses as stickers with a white keyline. Used as props on onboarding, empty states, reward screens and the result screen.
- **Looks like:** three or four props per screen at corners, tilted 6 to 12 degrees, a long soft shadow, one idle float (about 8 dp up, plus or minus 1.2 degrees, 7 s). Props pause off-screen and when reduced motion is on.
- **Budget:** under 120 KB each at 512 px, decoded at display size. All art is original; no real memes or real faces (section 8).

### 3. The foil milestone screen

- **HIGH:** a pure black screen, a gold-foil capsule badge, a huge condensed line, one sentence, three controls.
- **MockMob:** "First mock banked", "First repair closed", "Re-check passed". Black or deep-charcoal ground, a foil capsule with the subject hue inside, a monumental headline, one line that states what actually happened, and three controls: a dark share circle, a pearl "see it" circle, a primary pill.
- **Truth rule:** it fires only after the server acknowledges, and it states a fact ("3 of the 4 questions you repaired were right on the re-check"). No invented percentile, which is the one thing not to copy from HIGH's own "top 10 percent" line.
- **Budget:** a static foil WebP plus a one-shot scale-and-settle spring; confetti limited to about 20 pieces, skipped under reduced motion.

### 4. Story cards for concepts and the intro

- **HIGH:** full-bleed grainy flat illustration that dissolves into one solid colour where a condensed title and two lines of sub sit.
- **MockMob:** "Concept stories" (a five-card swipe with a segmented progress bar) for a ledger rule, a demand curve or a grammar trap; also the first-run intro. Each card is one illustration, one title, two lines.
- **Looks like:** top 60 percent art with visible grain, then a flat block in the subject hue for text, so text never sits on the image.
- **Budget:** 50 to 75 KB WebP at 720 px wide per card; tap-to-advance; no video.

### 5. A floating icon dock that content dissolves under, plus a glass tab tray

- **HIGH:** no bar container, puffy filled icons, active bright, a fade under the dock; separately, a frosted tray with a white active tile.
- **MockMob:** the five tabs (Today, Practice, Review, Learn, You) become chunky filled glyphs floating over the list, a bottom gradient mask under them, and the active tab gets a bright glyph, a label that fades in beside it, and a spring settle on press. In-screen sub-tabs use the glass tray: 7 dp padding, 18 dp radius, 44 dp tabs, a white active tile with a tinted shadow.
- **Accessibility:** keep real labels for TalkBack on every tab even when only the active one shows text; 44 dp minimum targets.
- **Budget:** one `BackdropFilter` for the dock, grouped and clipped (tint about 0.62 on dark, 0.72 on paper); the "dissolve" is a gradient mask, not a second blur. Provide a no-blur fallback with a higher tint.

### 6. Glass status chips with glow, sheen and a pop

- **HIGH:** two pill chips on a persistent dock, a coloured gradient fill, a coloured glow shadow, an inner top highlight, an occasional sheen sweep, a pop when a number changes.
- **MockMob:** at most two chips on Today: "Repair 2 of 5" in the subject hue and the next scheduled mock (only real dates). On update the number pops once and the sheen runs once; the sheen then rests for about 8 s.
- **Truth rule:** values come from the server; no chip claims progress that has not been acknowledged.
- **Budget:** gradient plus a translated highlight; no live blur. The glow is a pre-rendered soft shadow.

### 7. Monumental condensed type with a spring letter reveal

- **HIGH:** headlines at 13.5 percent of viewport height, line-height 0.9, two tones, letters rising with overshoot at 26 ms steps.
- **MockMob:** use it only for "moments": the welcome line, reward screens, the big result number, and empty-state headlines. Everything else stays in Hanken Grotesk and Gabarito.
- **Font:** Roc Grotesk is commercial. Open-licence options already close in feel are Anton, Bebas Neue, Big Shoulders Display (which HIGH itself lists as a fallback), or Barlow Condensed. This is a brand decision for the owner; Gabarito at its heaviest weight may be enough if the brand stays rounder than HIGH.
- **Budget:** cap the spring at about 20 characters, otherwise fade the line in as one block. Reduced motion: a plain 200 ms fade.

### 8. Tinted ranked rows and a wallet-card stack

- **HIGH:** the "Heat check" rows are tinted by rank (gold, silver, graphite) with an outlined condensed numeral at the right; Holdings are fanned coloured cards.
- **MockMob:** the Review repair queue becomes ranked rows (72 dp): the top row gold-tinted, the next silver, the rest graphite, a subject glyph in a circle at the left, and a big outlined condensed numeral at the right, the count of questions to fix. The "You" or Review tab gets a subjects deck: five stacked chapter-hue cards showing the subject name and the re-check accuracy; tap lifts a card to open the subject.
- **Budget:** plain gradients and transforms; a stack of five `Transform` layers, no blur.

### 9. First run in taps, not typing: choose, land, get the first repair, celebrate

- **HIGH's lesson:** the brand is strong before install and at the first reward, but a seven-step KYC drew a 15-minute complaint and a 3.1 rating. The activation moment (first trade) is celebrated; the try-before-you-commit surface (a simulated watchlist) is separate from the paid-risk action.
- **MockMob:** no five-question diagnostic in the app (that belongs on the website). Suggested path: (a) one monumental welcome with Mobi and one button; (b) a sticker-tile choice, "What are you cracking?", multi-select over the five subjects in their hues; (c) a second tile choice, "Where are you in prep?" with three big tiles; (d) land on Today with a first repair already built from those two taps; (e) the foil moment after the first completed repair; (f) sign-in deferred to the first time it is needed, as a glass bottom sheet ("Save your progress").
- **Looks like:** two taps from open to Today; nothing to type; every screen is one hue and one prop.
- **Budget:** static art per screen, one spring transition between tiles, no per-screen network wait. The diagnostic stays available as an optional "Find my gaps" card in Practice.

### 10. Voice with attitude, honesty by behaviour, legal at the foot

- **HIGH:** punchy lines, a joke that turns a rule into character, regulatory text tiny and collapsed at the end of a page.
- **MockMob:** remove the obvious footers from the flows (no "not affiliated with Delhi University" under a screen, no "this is just a diagnostic" under a result). If a sentence is legally required, it goes in Settings > About and the store listing. Integrity is delivered by behaviour: nothing shows as done until the server says so, numbers come from data, and a practice result is never called proof.
- **Sample lines that stay inside the truth rules:**
  - Today empty: "Nothing broken yet. Take a mock and we'll find the leaks."
  - Repair queue: "Four questions keep beating you. Let's end that."
  - After a re-check: "Fixed. Three of four now land."
  - Streak miss: "Missed yesterday. Today's repair is eight minutes."
  - Practice header: "Pick a chapter. Pick a fight."
  - Welcome: "CUET, but make it winnable." (the second half is a hope, not a promise; keep it as a tone line, not a claim)
  - Offline: "No signal. Your last repair is saved."
  - Sign-in sheet: "Save your progress. We'll keep it safe."
- **Budget:** copy is free; the cost is discipline. Keep slang to one phrase per screen and keep labels plain.

## 8. What not to copy, and why

- **Invented or unverifiable social proof and scarcity.** The login page says "Join 2M+ traders" with initial avatars while the waitlist counter on the same site reads about 69.7K; the reward screen tells the user they are in the "top 10%" of investors in India; the waitlist runs a "founders are full" ladder. None of this can be backed up on screen, and it breaks MockMob's rule of no invented numbers and no fake social proof. Reviewers also report the "cut the line" feature not working.
- **Gambling-adjacent mechanics.** "Heat check", flame badges, a 5x leverage chip and a "buzz" counter use arousal as the hook, even though the pitch is "investing, not gambling". MockMob's users are 17 to 18. No loss-chasing, no streak guilt, no variable-reward drops, no "heat".
- **Real meme photos and real faces as stickers** (a screaming child, a troll face, a portrait). This is a licensing and likeness risk, and unkind to the people in the images. MockMob stickers are all original (Mobi and objects).
- **Third-party marks as decoration.** HIGH puts company logos on cards because those are the securities. MockMob must not use Delhi University, NTA or other institution logos or their lookalikes as decoration. With the disclaimers gone, imagery must not imply affiliation either.
- **Roc Grotesk Compressed.** It is a commercial typeface. Do not ship it without a licence; use an open-licence condensed face if we go condensed.
- **The weight of the marketing site.** On a 390-wide phone emulation, reaching the flat-lay section pulls about 15 MB (61 WebP frames, about 10.9 MB, drawn to a canvas), on top of a WebGL shader hero with a cursor lens, 3D perspective phone loops and dozens of backdrop filters. That will not run well on 3.5 GB of RAM and a Mali-G57. Copy the look (baked art, gradients, springs), not the machinery (frame sequences, full-screen shaders, live refraction).
- **Candy backgrounds on every screen.** HIGH keeps its tool screens dark and uses colour as a frame. Full-bleed saturated backgrounds behind reading and question content hurt legibility and fatigue the eyes. Use the hue on headers, chips and cards.
- **Icon-only tabs with no text.** They look clean and hurt discoverability and TalkBack. Keep labels and semantics.
- **Tiny, low-contrast meta text.** Light grey 11 to 13 px on black appears all over HIGH's app art. Keep MockMob's body at 14 sp or larger and check 4.5:1.
- **A long, form-first signup.** Seven KYC steps are regulatory for them. We have no such excuse; see idea 9.
- **Animated neon text glow and endless idle loops.** A pulsing text-shadow and several simultaneous idle animations cost battery and fill rate. Allow one idle motion per screen, pause it off-screen, stop it for reduced motion.
- **Looking like their console.** Black ground, a lime button and a condensed headline is exactly HIGH's login page. Keep volt `#D2F000` as an action colour but let chapter hues, Mobi and the sticker kit carry identity.

## Appendix: where to look

- Landing: https://high.live (assets under /waitlist/v3/, for example /ft-trade, /ft-live, /ft-discover, /ft-collect, /screens, /baked)
- Login: https://high.live/auth/login. Signup entry: https://high.live/onboarding/mobile
- App Store: https://apps.apple.com/in/app/high-by-truestock/id6793021999
- Google Play: https://play.google.com/store/apps/details?id=com.choiceequity.high
- Instagram @high.rebels, X @GetHighApp, YouTube @GetHighClub
- Related MockMob notes: `flutter-feasibility.md` (glass budget, Mali-G57), `onboarding-research.md`, `owner-materials.md`
