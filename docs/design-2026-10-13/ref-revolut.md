# Reference teardown: Revolut (app and revolut.com)

Researched 13 Oct 2026 for the MockMob redesign. Goal: understand what makes Revolut feel premium and how a complex product is made to feel simple and exciting, then translate it to a CUET prep app on a Galaxy M06.

## How to read the evidence labels

- **[LIVE]** measured by me from the running revolut.com (computed styles in the browser) on 13 Oct 2026.
- **[STORE]** read from Revolut's own Google Play listings (Revolut UK, Revolut India Beta, Revolut Kids and Teens India). These are marketing screenshots, so they show the intended UI, not a recording of the live app.
- **[DESIGNER]** Dribbble shots posted by Revolut's in-house product designer (Denis Kovalev, "for Revolut"). Close to the shipped UI, still a design file.
- **[SECOND]** third-party write-ups (Craft Innovations, Superside, Stratton Craig, Motion agency, Built for Mars, trade press). Treat as indicative.
- **[GAP]** I looked and could not verify it. Listed plainly in section 9.

Revolut's own 403-blocked pages (blog, some articles) were read through the browser where possible. Nothing was signed into, downloaded, submitted or installed. Cookies were declined.

---

## 1. What it is and who it is for

- Revolut is a UK-born "financial super app": current account, cards, FX, savings, stocks, crypto, P2P chat payments, subscriptions, an AI assistant. 80+ million customers worldwide per its own site [LIVE]. Play Store: 4.7 stars, 41.5 lakh ratings, 5 crore+ downloads [STORE].
- Audience: it started with young travellers and urban 20-somethings, and is now positioned as a primary bank for a broader adult base. The Oct 2023 "Revolut 10" redesign was framed as built for people who use Revolut as their main account [press release, revolut.com/news].
- India is live as a beta (Revolut Payments India, UPI, prepaid and forex cards). Per press coverage (TechCrunch, June 2026) it began onboarding a few thousand people from a roughly 450,000 waitlist [SECOND]. The India Play listing is aimed explicitly at "students, young professionals and frequent travellers" in one verified review [STORE], and a separate "Kids and Teens India" app exists for ages 6 to 17.
- Why it matters to MockMob: Revolut is the best-known example of a regulated, data-heavy product that feels like a lifestyle app. The same trick is needed for a mock-test and mistake-repair app: serious numbers, carried by expressive imagery and quick, confident interaction.

What changed recently (for the "2024-2026 redesign" question):

| Date | Change | Evidence |
|---|---|---|
| Oct 2023 | Revolut 10: biggest redesign. Simpler home, account switching, themes, per-account backgrounds, widgets, customisable navigation. Opt-in "new look preview" toggle during rollout. | Official blog and press release |
| 2024 to 2025 | Brand maturation under Head of Global Brand Design (Gareth Morgan, joined Jan 2024): photography to calmer portraits, 3D from cute toy-like to photoreal, type from shouty uppercase to calmer lowercase. Campaign "Money Possibilities" (Jan 2025, Anomaly London): abstract fabric/wool world, "more premium and emotional". | [SECOND] Superside, trade press |
| Oct 2025 | A Threads post (18 Oct 2025) says a TestFlight build adds Liquid Glass throughout the iOS app. | One secondhand post, no official statement. [GAP] |
| Jan 2026 | An X post calls the Android "liquid glass" navigation tacky. | Snippet only, page not readable. [GAP] |
| Apr 2026 | AIR (AI assistant) launches for UK customers. Opens by swiping down from the middle of the home screen, or via Profile, Chats. | Trade press |
| 2026 | FIFA World Cup 2026 themed splash/lock screen and 48 virtual cards, Pride theme, artist-collab theme (Alex Kuznetsov). | [DESIGNER] |
| 6 Oct 2026 | Play Store build notes are generic ("tweaks under the hood"). No announced redesign. | [STORE] |

Honest conclusion: there is no officially announced redesign after Revolut 10. What visibly moved since is the brand layer (premium photography, photoreal 3D, lowercase), motion polish, seasonal and artist themes, and the AI assistant.

---

## 2. Visual language, in concrete terms

### 2.1 Typefaces

- **Display and UI labels on the website: Aeonik Pro, weight 500** [LIVE]. Confirmed in `document.fonts` (Aeonik Pro 500 loaded; 700 and a Capitalised 900 declared but not used on the page). A paid commercial grotesque from Cotype Foundry. Do not use it (see section 8).
- **Fine print and micro labels: Inter** (12 and 14 px, 400 and 600) [LIVE]. In the app UI the numerals and labels in the designer shots look like Inter or an Inter-like grotesque; I could not confirm the in-app font file. [GAP]
- Type scale measured on the live site (desktop width 1024):

| Role | Size / line height | Weight | Tracking |
|---|---|---|---|
| Hero h1 | 80 / 80 (leading 1.0) | 500 | -2.08 px (about -0.026 em) |
| Section h2 | 48 / 48 | 500 | -0.6 px |
| Sub-head | 28 and 22 | 500 | n/a |
| Body | 18 | 400 | normal |
| Buttons | 16 | 500 | normal |
| Legal / footnote | 12 and 14 (Inter) | 400/600 | normal |

- Mobile website: the hero headline wraps to three lines at roughly 44 to 48 px; body about 18 px at 1.4 leading; everything left-aligned, no centre-aligned paragraphs on mobile [LIVE, 375 px emulation].
- Rules visible across the system: **one weight (500) for all display type**, never bold; tight negative tracking only at large sizes; headline line height at 1.0; sentence case (the move from uppercase to lowercase is a stated brand decision, [SECOND] Superside).
- Numbers: balances are set large with the minor units dropped to about 55 to 60 percent size and top-aligned (for example the whole part large, ".39" small) [DESIGNER, STORE]. Currency symbol sits at full size.

### 2.2 Colour

- Marketing surfaces alternate **pure white `#ffffff`** and **pure black `#000000`** [LIVE: the only two section backgrounds measured]. Text on white is `#1f1f1f`; secondary text `#717173`; on black, white plus `#c9c9cd` (28 elements used it for secondary text) [LIVE].
- Primary button: `#1f1f1f` fill, white text, fully round [LIVE]. Ghost/secondary on dark: `rgba(255,255,255,0.10)` fill with a 16 px backdrop blur [LIVE]. White solid pill on photos [LIVE].
- Brand accent: a violet-blue around `#494fdf` to `#4f55f1` (third-party design-system summaries list `#494fdf`; the purple icon tiles in the store screenshots match, [SECOND]/[STORE]). It is used sparingly: icon tiles for categories, cards, selected states. Everything else is monochrome and photographs carry the colour.
- Product UI palettes taken from the designer shots' own swatches [DESIGNER]: cool light grey `#E4E4E9`, near-black `#010101` to `#090909`, slate `#3C3E43`, mid-grey `#787E87`, with per-theme accents (indigo `#1221E2`, red `#C72D2E`, purple `#530E6C`, `#7B5F96`). The dark UI is **near-black with a cool blue tint, not warm charcoal**.
- Semantic: green for positive change (`+2.52%` type deltas), the rest neutral. Category colours are saturated flat tiles (green groceries, orange restaurants, pink shopping, blue travel, purple groceries) [STORE].

### 2.3 Materials

- **Photograph as ground.** Account heroes are full-bleed photos (living room for "House deposit", a woman from behind in a field for the main account, a couple for a Joint account, an abstract artist painting for a themed wallpaper). The photo fades to a dark gradient at the bottom, where the list begins [STORE, DESIGNER].
- **Frosted translucent pills and circles over the photo.** Balance sits directly on the photo. Below it: a small frosted "Accounts" pill; below that, four frosted circular action buttons (about 44 to 48 dp, white icon, label underneath in 12 to 13 sp white) [STORE, DESIGNER].
- **Dark glass list card.** Transaction rows sit on a rounded card (about 20 to 24 dp radius) that is a dark, slightly translucent grey over the wallpaper, with a "See all" row centred at the bottom. Rows: 36 dp round brand-logo avatar, merchant name 15 sp semibold white, "Today, 16:30" 13 sp grey, amount right-aligned [DESIGNER].
- **Website glass:** navigation bar has `backdrop-filter: blur(85px)` on `rgba(0,0,0,0.5)`. Ghost buttons use `blur(16px)` on `rgba(255,255,255,0.1)` [LIVE].
- **Flat everywhere else.** Third-party summaries report no shadows on web cards and depth coming from black/white banding and whitespace [SECOND]. I did not measure shadows. In the app, separation comes from translucency and tone, not shadow.
- **Borders:** hero frames on the site use a thin (about 2 px) translucent white stroke on a 40 px style radius around the phone-shaped photo [LIVE visual].
- **Dot-matrix and fluted textures** as brand "technical" textures: a particle-dot wave field behind the Security screen header (teal on black) [STORE]; dot-style QR code with rounded white dots on translucent dark [STORE]; fluted chrome and glass ribbon as the "360 degree view" illustration [STORE].
- **No visible grain.** Surfaces are clean; richness comes from photography, gradients and 3D.

### 2.4 Imagery

- **Lifestyle portraits**: warm, natural light, 3/4 crop, subject often looking off-camera or from behind; one balance number overlaid. Cropped inside tall rounded rectangles (the three-card row on the homepage: centre card larger, side cards peeking) [LIVE].
- **Photoreal 3D renders** (post-rebrand). Chrome and frosted-glass slabs with currency symbols stacked at an angle; a black glass phone with a glowing capsule (AIR); a brushed-metal shield with an R monogram (Security); metal and glass coins carrying company logos (investing); a tilted fan of physical cards with metal and gradient finishes (cards) [LIVE, STORE]. Lighting: dark studio, hard rim light, soft gradient floor.
- **Delivery is pre-rendered video, not real-time 3D.** The homepage has 5 `<video>` elements, 0 `<canvas>`. All muted, non-looping MP4s: three are 4320x2700 (4 s, 4 s, 16 s), one 900x1200 (3 s), one 2000x1000 (12 s with a poster image) [LIVE]. 26 images on the page.
- **Teen app imagery is looser and more playful** [STORE, Kids and Teens]: a still-life of three cards on a lilac plinth with a pebble, wood block and pencil; money-as-message cards with 3D boba tea or a pug in a party hat; chrome and glass pillars with a glowing yellow-to-cyan coin.
- **Illustration style shift:** from cute toy-like 3D to photoreal, a stated decision ("time to grow up") [SECOND].

### 2.5 Iconography

- Monoline, rounded caps, about 1.5 to 2 dp stroke, always inside a **filled circle or rounded square tile**: the four action buttons (plus, shuffle arrows, bank, ellipsis), tab icons, and category tiles (flat colour, white glyph) [DESIGNER, STORE].
- Merchants appear as their real round logos. Friends as round photos with a small badge (arrow or R).
- Status glyph discipline: a green check badge on the corner of an icon means "active" (Automations list) [STORE].

### 2.6 Layout and composition

- **Mobile app**: single column, 16 dp side margins, large vertical rhythm. Order on the home hero: top bar (avatar, Search pill, two circular icons) then account label, balance, "Accounts" pill, page dots, four circular actions, dark glass list card, "Products for you" card [DESIGNER].
- **Bento on analytics** (India): two side-by-side tiles under the list, "Spent this month" with a green down-arrow delta and a small sparkline, and "Total wealth" with overlapping icon bubbles [STORE].
- **Chart style** [STORE]: thick segmented **donut ring** (about 16 dp stroke) with rounded segment ends, visible gaps between segments, six saturated category colours, big total in the centre with a small label ("Spent" and month). A segmented control above (Expenses, Income, Budget; selected = lighter grey pill) and range chips below (1W, 1M, 6M, 1Y; selected = filled pill; a "..." chip at the end). On web: a horizontal segmented bar of 4 colours with a legend beneath a big total, inside a dark glass card overlapping a photo [LIVE].
- **Density**: low on the hero (one number, one photo), medium in lists (2 to 3 rows then "See all"). No dense tables on the home. Detail is pushed one tap deeper.
- **Website**: huge type, one idea per screen height, alternating black and white bands, a rounded-pill CTA on every band.

---

## 3. Motion and interaction

Documented values are from the live site; in-app motion is described by Revolut's own designer and by third parties. Where numbers are missing I say so.

### 3.1 Motion tokens [LIVE, website]

- Ease-out for most UI: `cubic-bezier(0.15, 0.5, 0.5, 1)` at 0.3 s (36 transitions measured), 0.35 s for a few.
- Ease-in for exits: `cubic-bezier(0.4, 0.3, 0.8, 0.6)` at 0.2 s.
- Hover and press colour changes: `0.15 s ease`. Longer opacity fades: `0.6 s ease`.
- Rule of thumb: hover and press 150 ms, enter 300 ms ease-out, exit 200 ms ease-in. Third-party design-system dumps list 150 and 240 ms with `cubic-bezier(0.22, 1, 0.36, 1)`; I trust the live-measured values over those. [SECOND]

### 3.2 Scroll behaviour [LIVE, website]

- Section headlines and body fade up from low-contrast grey into full contrast as they enter ("Life, meets savings" and "Ask, and AIR..." were grey mid-scroll and fully white once centred). Scroll-linked, not time-based.
- Full-bleed scene photo with **scene chips** (Adventure, Wedding, Moving) that swap the photo/goal. Card section has Physical, Virtual toggle pills (selected = white fill, others = outlined).
- 3D videos play once when the section is reached and rest on the last frame (non-looping).
- The three-photo hero row on the homepage is a horizontal pager with page dots; centre card scale larger.

### 3.3 In-app transitions and micro-interactions [DESIGNER unless noted]

- **Send money**: "the entire screen transforms into an input field and seamlessly transitions into a chat bubble" (designer's own description). P2P feels instant because the entry UI becomes the message.
- **Send message**: the input field morphs into the message bubble. Chat scroll has inertia.
- **Animated amount input**: new digit animation plus a placeholder for hundredths (the field shows the minor units greyed until typed).
- **Create account (reveal pattern)**: the new account "gradually appears and transitions seamlessly into the main screen" rather than a toast and a refresh.
- **Home appearance**: smooth entry animation for the main screen; a background was added to the 2FA screen so the lock and home share one atmosphere.
- **Freeze card**, **profile**: new bespoke animations (freeze uses a cool blue and violet palette per the shot swatches).
- **Card detail** [SECOND, Motion agency]: page controls blur out, the tab bar slides down and disappears, the card scales up and comes into focus, then the action sheet appears. "First the card, then the details."
- **Closing a pocket** [SECOND, Built for Mars]: the pocket dissolves into the screen. Used as a delight moment on a normally negative action.
- **Splash and lock**: playful animated ball and a personalised greeting for the World Cup 2026 easter egg ("Let's kick off", plus the user's name) [DESIGNER].
- **Status animations** during transfers and ID checks: processing, success, failed, each with its own state, and specific text such as "Checking image quality" rather than a generic spinner [SECOND].
- **AIR assistant**: swipe down from the middle of the home screen to open it [SECOND, trade press].
- **Pull to reveal search** on tab pages (added in version 8.0, 2021): the search bar appears only when you pull down; focus shows grouped suggestion cards [SECOND, Ergomania].

### 3.4 Haptics and sound

- No documented haptic or sound spec found. Any claim that Revolut vibrates on swipe or plays sound is unverified. [GAP]

---

## 4. Navigation: precise enough to rebuild the feeling

### 4.1 Bottom tab bar (Revolut 10 era) [DESIGNER]

- Five tabs: **Home** (R monogram), **Invest** (bars), **Payments** (two arrows), **Crypto** (bitcoin glyph), **RevPoints** (hexagon with plus). Labels about 11 sp under 22 dp icons.
- Active tab: white icon, bold white label. Inactive: grey (about `#8D9199`), regular weight. No pill or indicator.
- The bar is **docked, full width, flush with the screen bottom**, dark translucent (the wallpaper shows faintly through it), with the home-indicator area below. It is **not** a floating pill. Revolut users can hide some tabs (the crypto tab can be hidden) and customise the navigation [SECOND].
- Over a photo hero, the bar tint is dark enough to hold white text legibly; there is no hard divider line.
- Possible newer treatment: iOS 26 Liquid Glass reported in TestFlight (Oct 2025) and an Android glass bar criticised in Jan 2026. Unverified. [GAP] Even if real, it tells us the market moved to glass bars and some users found Android versions heavy-handed.

### 4.2 Top bar on home [DESIGNER]

- Left: round avatar (opens Profile). Centre-left: **Search pill** (frosted, magnifier plus label, about 36 dp high). Right: two circle icon buttons (analytics chart, cards). All three float over the wallpaper with the same frosted fill.

### 4.3 Account pager and sheets

- Accounts are a **horizontal pager of tall rounded cards**, each with its own background (photo, gradient, artist wallpaper). The neighbouring accounts peek in from the edges with a smaller, dimmed version of their balance. Page dots under the balance [STORE, DESIGNER]. The "Accounts" pill opens a switcher.
- **Customisation sheets** [DESIGNER]: a dark bottom sheet titled Theme (X at left), a carousel of phone-shaped previews, a swatch row of round chips (Lines, Alex K, Cyberpunk, Glass), a big white pill "Apply". A second sheet titled Background has chip tabs (Minimal, Alex Kuznetsov, Glass, Colours), a 3-column grid of tall rounded wallpapers (selected has a blue ring), and "Upload" in blue at top right.
- **Hub** (since 2021): one scrollable page of every product, with the ability to pin products to Home. Search lives at the top of main tabs [SECOND].
- **Modal depth**: card details and money flows are full-height pushes that hide the tab bar.

### 4.4 What to copy in feeling, not in form

- The nav is **quiet**: no logo-sized icons, no pill, no badges unless needed. Premium comes from what is behind it (photo) and how it transitions out of the way when a task starts.

---

## 5. Onboarding and first run, screen by screen

Source: the Craft Innovations analysis of the iOS flow captured on Mobbin (the Singapore variant), cross-checked with Raw.Studio, plus Play Store screenshots. The sequence varies by country and changes over time. Lazyweb lists the phone-signup flow as 11 screens and a legal-agreements flow as 3 screens, and 63 screens overall (gated; not viewed). [SECOND]

1. **Cold start**: logo on plain white, then a bold welcome screen with a playful question about changing how you "money" (the verb-ified noun is the brand line) and an animated coin flying through space. Large type, motion energy, no form.
2. **Story slides**: each benefit pairs a short line with a visual metaphor. Spending is shown with cards; investing is shown with coins and big-company logos ("from $1"). The coin or globe visual is documented by two sources (Craft: flying coin; Motion agency: a rotating globe with coins from different currencies sliding across for 30+ currencies).
3. **Phone number**: one task per screen. Searchable country-code picker. Before sending the code, a confirmation of the number.
4. **Code**: six digits, SMS autofill, visible countdown, "resend" appears automatically, direct error ("Incorrect code entered").
5. **Notifications priming**: explained as benefit ("instant payment notifications, your balance always up to date") with two buttons, Enable and Not now. Not a raw OS prompt first.
6. **Country of residence**: one decision. Privacy and consent links sit quietly at the bottom, not blocking.
7. **Name as on ID**: inline hint with an example ("Daniel, not Dan"), optional alias field.
8. **Fast-track ID (where available)**: a government e-ID option labelled "Faster" next to manual upload.
9. **Date of birth, address** with autocomplete; **email**; **passcode** then confirm; **Face ID** offered after.
10. **Document scan**: pick ID type, real-time blur detection, instant retake, status text "Checking image quality".
11. **Selfie video**: short prompts to keep the face in frame, with a plain instruction such as face forward, glasses are fine.
12. **"What do you want to use Revolut for?"**: multi-select emoji chips grouped under "Everyday needs" and "Global spending" (Transfers, Cashback, Airport lounge access, Crypto). Selected chips highlight instantly. The copy admits the dual purpose: it is needed for regulatory reasons, "and also, we're curious". A compliance question dressed as browsing features.
13. **Profile**: pick a handle (Revtag) with live availability feedback, optional photo, "Not now".
14. **"Useful ads only"**: a toggle framed as a benefit, with a line saying the choice can be changed on the next screen.
15. **Plan upsell**: plan cards with price, perks, free-trial option and partner perks. Then card colour preview, optional text or emoji on the card, PIN, delivery address with a fee heads-up, order summary, top-up with preset amounts, add to Apple Pay.
16. **Landing on Home** with a "your money's new home" message and clear actions (add money, explore).

Design takeaways (what is actually clever):

- The first 60 seconds sell the feeling; paperwork starts only after the user has seen the promise.
- One task per screen with immediate micro-feedback (number check, code error, handle available, image quality).
- Every required question is reframed as a choice, a toggle or a chip set, never a form.
- Every optional ask has a visible "Not now".
- The user arrives at Home with something personal done (handle, card colour), not just verified.
- **Teen variant** [STORE]: a very similar structure with a looser visual world: card customisation (text, stickers and "your own sketches"), the parent approves, and "Sign up for free in minutes" sits on a photo hero.

---

## 6. Copy voice

Formal substance, conversational delivery [SECOND, Stratton Craig]. The brand publishes its tone-of-voice thinking. Patterns I can see directly on the live site and store listings:

- **Verb-ify the noun.** The tagline treats "money" as a verb. The India listing repeats the move with "Change the way you money" and "Make your spend, well-spent".
- **"Your X, reimagined."** Section headlines on the live site follow a small set of templates: *Your [thing], reimagined*; *Elevate your spend*; *[Thing] got even more personal* (UPI section); *Take total control of your money*; *Your money's safe space*; *Teach your kids money independence*.
- **One short sentence, one benefit, one verb on the button.** Subtext is a single line. Buttons: Start earning, Get my card, Get started, Join today, Explore, Learn more, Move your salary.
- **Plain-English product labels:** Add money, Move, Details, More; Spent this month; Total wealth; Upcoming payment; Automations; Spare change; Sort your income.
- **Honesty with a wink.** The onboarding chips line admits the question is for regulators and also curiosity. Store copy: "No more awkward money chats", share a GIF "to diffuse any tension", "nip 'em in the bud".
- **Teen copy is looser:** money-message captions like "Thnx for the boba", "Happy bday", "Friday night". The cards carry these as styled message text with illustrations.
- **Personalised greetings** in moments of delight: a first-name line on splash and lock screens during the World Cup campaign.
- **Where the voice failed** [SECOND]: a casual takeaway-spending campaign read as patronising and used a headline statistic reported as fabricated. Lesson for MockMob: humour must never come at the student's expense, and numbers must be real.
- **Regulatory fine print is kept in a separate, quiet strip** (a thin band under each store screenshot, 12 px type on the web, below the CTA). It is not mixed into the headline, and it exists because Revolut is a regulated bank. MockMob is not, and the owner has said obvious disclaimers go.

Style note for MockMob (not a Revolut rule): Revolut speaks to adults who like to feel clever. For 17-year-olds, borrow the *structure* (short, benefit-first, verb button, a wink) and write in your own Hinglish-aware, exam-room voice.

---

## 7. The 10 most transferable ideas for MockMob

Constraints used below: Galaxy M06, Dimensity 6300 (Mali-G57), 720x1600 at 300 dpi (about 384 x 853 dp), 3.5 GB RAM, Flutter with Impeller. See `flutter-feasibility.md` in this folder: real backdrop blur only on floating chrome inside one `BackdropGroup`, fake glass from a cached pre-blurred copy of our own art everywhere else, transforms and springs over shaders, no glass stacked on glass, minimum tint 0.62 on dark and 0.72 on paper to keep text at 4.5:1. All numbers below are estimates for tuning on-device, not measurements from Revolut's app.

**1. A hero card with art, one number, one frosted pill (the home screen formula).**
Revolut: wallpaper, small label, large balance, "Accounts" pill. MockMob "Today": a full-width card (radius about 28 dp, margin 16 dp) whose background is a generated raster illustration for the current subject, fading to the dark ground at the bottom. Small label ("Accountancy, 12 days to CUET" using real dates), one big number that is genuinely the next thing to do (for example the count of mistakes waiting for repair, set at 44 to 48 sp Gabarito with the unit at 55 percent size), and a frosted pill that reads the next action. Art is pre-blurred and cached so the pill is fake glass, zero live blur. Do not show invented marks or readiness percentages.

**2. A subject pager with peeking neighbours.**
Revolut: account cards swipe with the neighbours visible at the edges. MockMob: Accountancy, Business Studies, Economics, English, General Test as a horizontal pager of hero cards, each with its own artwork and accent; the neighbours at 85 percent scale and 60 percent opacity peeking about 20 dp. Page dots under the number. Only the centre card runs any animation.

**3. A row of four frosted circular actions plus a glass list card.**
Revolut: Add money, Move, Details, More, then a dark glass list of recent items with "See all". MockMob: Practice, Full mock, Repair, Review as 52 dp circles with a monoline icon and a 12 sp label, then a dark glass card (24 dp radius) listing the last 2 or 3 items (for example "Repaired: Partnership dissolution, 2 of 3 right") with round icon tiles in the subject colour and a "See all" row. The list card is fake glass over the same art, so no stacked blur.

**4. A floating glass dock instead of a docked bar (a deliberate step beyond Revolut).**
Revolut's bar is docked and flat dark. The owner wants glassmorphism and more interactivity, so the floating pill is the better bet: 64 dp tall, inset 12 dp from the sides and 12 dp above the system bar, radius 32 dp, one live grouped backdrop (sigma about 18) with a 0.62 dark tint and a 1 dp edge-light stroke, five items with 24 dp icons and 11 sp labels, the active tab a lime-tinted pill that slides between items on a spring (about 260 ms). Quality fallback to opaque tint when frame time rises. Hide the dock on task screens (mock, repair) the way Revolut's card screen slides it away.

**5. Onboarding as a story, then choices, not a quiz.**
Revolut: promise first, one task per screen, compliance reframed as chips, "Not now" everywhere, personal setup before home. MockMob replacement for the five-question sample (the owner's point: it is not scalable and belongs on the website): (a) a 3 to 4 slide story with Mobi and one metaphor per slide (find the leak, repair it, watch it hold), pre-rendered art, 2 to 3 seconds each, skippable; (b) "Which subjects are you taking?" as emoji-free illustrated chips grouped by Commerce core and Languages; (c) "Which exam date and which colleges are you chasing?" as chips with a sensible default; (d) one honest line explaining why we ask ("so the first thing we show you is the right one"); (e) optional notification priming framed as the study reminder with "Not now"; (f) land on Today with the subject card already themed. A first-run "try one question" can stay as an optional card inside Practice, not as the gate.

**6. Theme and wallpaper choice as identity.**
Revolut: a Theme sheet with phone previews and an Apply pill, per-account backgrounds, artist collections. MockMob: a "Make it yours" sheet in You with 6 to 8 generated wallpapers (WebP, about 60 to 120 KB each, 720x1000), chips for collections (Calm, Neon, Paper, Mono), live preview of the Today card, and a white or lime Apply pill. Cheap to build (static art), high ownership feeling, and a natural place for seasonal drops (exam-day, results-week).

**7. A motion grammar of morphs, staging and number rolls.**
Revolut: the input becomes the bubble, the account reveals into home, first the card then the details, digits animate. MockMob: (a) answer chip expands into the explanation sheet (shared-element, 300 ms ease-out `cubic-bezier(0.15, 0.5, 0.5, 1)`); (b) result screen reveals in order: score number rolls up, answer-sheet squares fill left to right, then the "first thing to fix" card slides in; (c) repair completion collapses the mistake row into a check and shifts the list up (closing-a-pocket idea, 200 ms ease-in exit `cubic-bezier(0.4, 0.3, 0.8, 0.6)`); (d) press feedback 150 ms scale to 0.97. Transform and opacity only, springs from the shared token set, and everything snaps to instant when reduced motion is on.

**8. Pre-rendered "3D" objects for the few big moments.**
Revolut delivers chrome and glass objects as pre-rendered video, not live 3D (5 videos, 0 canvas on the homepage), and floats reward chips ("+100", "+250") off a rendered phone. MockMob: generate a small set of glass-and-chrome objects (a shield for streaks, a lens for "find the leak", stacked answer-sheet slabs, a lime orb for Pro) with image generation and ship them as WebP stills with a subtle parallax tilt from the gyroscope or scroll. At most one 3 second looping WebM or Lottie on the welcome slide, with a still fallback. Floating "+1 repaired" chips with a spring pop for rewards that are real counts.

**9. Learn as bite-sized, progress-led cards.**
Revolut Learn 2.0: filter chips (All, Crypto, Stocks, Fraud, Tips), a horizontal "Suggested" carousel of tall dark cards with a 3D object, a thin progress bar and the reward, an "In progress" row, and lessons broken into small chunks so users are not put off by walls of text (designer's stated aim). MockMob Learn: chips per subject, a "Suggested for your fix list" carousel of tall cards (art, chapter name, a 3 to 5 minute estimate, progress line), "In progress" below. No money rewards; the reward is the cleared mistake.

**10. Segmented ring plus bento tiles for honest evidence.**
Revolut Analytics: a thick segmented donut with gaps and a big centre total, range chips, then two bento tiles with a delta and a sparkline. MockMob Review: a ring of the last mock split by subject or by mistake type, the centre showing the real count of questions, range chips (This mock, 4 weeks), and two tiles ("Repaired this week" with a green delta, "Still open" with a sparkline). Draw the ring as a custom painter with one animation on first paint. Only observed values, never simulated marks.

---

## 8. What not to copy, and why

- **The brand itself.** The R monogram, the violet-blue accent used the same way, Aeonik Pro (a paid licence, and it would make MockMob look like a bank), and the tagline that turns "money" into a verb. Writing "Change the way you ..." anything is an obvious imitation of a trademarked line.
- **Lifestyle stock-style photography of adults.** It reads as finance and, if generated to look similar, as a copy. Use Mobi, exam-world objects and abstract art made for MockMob.
- **Toy-to-photoreal brand shift without thought.** Revolut moved from cute toy 3D to photoreal because its audience matured. MockMob's audience is 17 to 18 and Mobi is the one character asset. Keep Mobi, but give it richer material (soft 3D lighting, glass accessories) rather than replacing it with chrome.
- **Heavy media.** 4320x2700 videos of 4 to 16 seconds are fine on a marketing site, impossible on a 3.5 GB phone over Indian mobile data. Use stills and one tiny loop.
- **Live blur everywhere.** The website's `blur(85px)` nav and many 16 px glass buttons would drop frames on the Mali-G57 if translated to dozens of live `BackdropFilter`s. One grouped backdrop for the dock; fake glass for everything else.
- **A docked five-tab finance bar and a crowded home.** Revolut needs Home, Invest, Payments, Crypto and RevPoints because it sells many products. MockMob has one loop; five tabs is already the ceiling.
- **Upsell right after onboarding.** Revolut pushes plans, a trial and a card order before the home screen. MockMob's Pro is web-only and Rs 99; the app should not run a paywall funnel or imply purchase in-app.
- **Aggressive reward gamification** (points, cashback, "surprise" rewards). It fits a spending product. Here, rewards must be real evidence (a mistake repaired), not currency.
- **Fine print as a design element.** The thin legal strip under every Revolut screenshot is a regulatory need for a bank. The owner has said obvious disclaimers go. Keep only truths that are not obvious (for example the one place a result cannot be trusted yet), and phrase them as help, not defence.
- **Casual tone that mocks the customer, and borrowed claims.** Revolut's "You ok, hun?" campaign drew backlash and its statistic was reported as fabricated. No invented numbers, no fake social proof counters ("80 million"-style), no "join thousands" lines unless they are real.
- **Hidden customisation.** Reviewers noted Revolut's personalisation is tucked away. If MockMob offers themes, surface them in You and once in onboarding.
- **Assistant gesture collisions.** A swipe-down from the middle of Home opens AIR on Revolut. On MockMob that gesture belongs to pull-to-refresh and the Today scroll; do not hijack it.

---

## 9. What I could not verify (so do not build on it as fact)

- Any official Revolut redesign after Revolut 10 (Oct 2023). Searches found none.
- Liquid Glass in the Revolut app: one Threads post (Oct 2025) and a snippet of an X post (Jan 2026). Treat as rumour.
- Haptics and sound design.
- In-app font files, exact in-app durations and easing (only the website tokens were measured).
- The Mobbin and Lazyweb flows (login-gated). Onboarding detail comes from a secondary analysis of one country's flow.
- The in-app screens are known through store marketing images and a designer's Dribbble shots, not a hands-on session on a device.
- Pages that could not be opened: Revolut's own tone-of-voice blog post, the Revolut 10 microsite (404), Craft Innovations' AIR review body (lazy-loaded).

## 10. Sources used

- revolut.com home (UK and India) and Revolut 10 blog and press release (read in the browser).
- Google Play: Revolut (com.revolut.revolut), Revolut India Beta (com.revolut.retail.india), Revolut Kids and Teens India (com.revolut.junior.india): listing text and all 8, 8 and 7 screenshots.
- Dribbble "Revolut" profile by Denis Kovalev: Learn 2.0, Animated amount input, Home Appearance, Create account (Reveal pattern), Freeze card, Chat (send money and message), Profile, Analytics 2.0, Alex Kuznetsov Theme, Pride Theme, FIFA World Cup 2026 cards and splash.
- Craft Innovations banking onboarding analysis; Raw.Studio onboarding tactics; Superside (Gareth Morgan, Aug 2025); Stratton Craig (tone of voice); Motion agency (UI animation); Built for Mars (closing a pocket, metadata only); trade press on Revolut 10, AIR, Money Possibilities and Revolut India.
- Third-party design-system summaries (open-design.ai and similar) used only for the brand-blue hex and as a cross-check; where they disagreed with the live site I used the live measurement.
