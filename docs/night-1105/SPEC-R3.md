# Round 3, 5 Nov 2026 (owner LK99-LK114, his ~10 am look): the orchestrator's spec

His words are verbatim in docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md on branch feat/app-and-web, section "5 Nov 2026, about
10 am"; ledger rows LK99-LK114. Research behind every decision (read your packet's part): C:/Users/atish/Desktop/mockmob copy/
tmp-night/r3-research/ALL.md (preparoo, daygreen, prices, scrolltour, brandloss, pricingmap, content) and the folders beside it.
Standing rules: refine, never rebuild or cut; keep the logo and the fonts; no slop (no ALL-CAPS eyebrows, no middle-dot lists, no
text walls, no fake numbers, no arrows on buttons); honest money (no struck prices, no countdowns, never compare a monthly price
with a one-time price in one sentence; compare over the same period); every number from real data; 44 px targets; AA contrast;
Night and Day; reduced motion. Owner decisions here supersede older tests: update a pinned test to the new rule and say so.
Base: main 88ff026cc (what is live).

## R3-D1 Day palette (LK101)
Cause (daygreen DG1-DG8): the 4 Nov calm-Night change removed Day's olive layer and turned selected states into raw volt slabs
in Day; tonight's Day brand words went to a greyer #3F5200. Fix, Day only, Night unchanged:
- One Day text green #526700 (the app's accentText) for brand words, accents, numbers and the focus ring: --brand-word Day,
  the statement accent Day, the hero brand line Day, --focus-ring Day, motion-kit fallback.
- Volt #D2F000 stays the action fill with ink #0B1000; in Day its lip is #8BA000 plus an inset 1px rgba(82,103,0,.28) hairline.
- Day selected chips/segments/Compass groups/the Lab rail item: fill #FFFDF8, 1.5px #526700 rim, ink text, a small volt tick
  with a 1px rgba(82,103,0,.55) rim. Day hover/state wash rgba(210,240,0,.22). Never a raw volt slab on cream.
- Warm shadows rgba(27,25,20,x) replace the green-black ones (nav, dock, .ts, public-polish fallbacks).
- Record the Day palette in DESIGN.md and shared/tokens.css.

## R3-D2 Brand back, by role (LK108, LK102, LK114)
Cause (brandloss B1-B10): the colour, surface and texture layer was removed on 4 Nov. Bring brand back by role, never as decor:
- Brand words (volt in Night, #526700 in Day): product names, hero numbers (Compass score, creator reach, Recovery marks),
  progress and selected states (tab underline, story progress, the Lab pace line, the Recovery active step). The tour's and the
  Lab's product screens look like the app again (volt timer, selected answer, Saved, marks, Ask Mobi's own bubble), in both
  themes since those screens are dark.
- The statement: "MockMob" is a green word too (LK102); keep where/tonight/shortlist.
- Section brand stamps above h2s: the section's desk-object BrandIcon (24-28 px) + the product name in the brand word colour,
  sentence case, no caps, no dots: Mistake Lab, Score Recovery Lab, DU Compass, MockMob on Instagram, Wall of love (and Key cards).
  This replaces the 4 Nov "no kickers above an h2" rule for product names only.
- "Featured by CUET creators": restore the branded creator cards: volt reach numbers, the volt monogram with its dashed orbit
  (Bricolage, not mono), the volt play key with its volt-edge press, the volt heart and hover edge, volt Wall of love avatars;
  the summary as a raised strip with the three numbers in the brand word colour; texture from the brand's own answer-sheet
  (OMR) bubbles, never a generic grid or glow.
- Voice: "Fix it once. Check it holds.", "Practise. Replay. Repair.", "Fix why you missed it." where true.

## R3-D3 Hero (LK99, LK100)
Cleaner like Preparoo (fewer elements in the first screen, a 16-24 px rhythm, lead in 2 lines at 16-17 px) while keeping what
LK70 needs (say what MockMob is) and the approved CTAs (Sign up free; Try 5 questions first; Have an account? Log in). The two fact
lines become one line. The second beat (Five questions free, 73 DU programmes, Two exam screens, 60 minutes/50 questions) must be
shown properly: render two variants and let judges pick: (A) the beat as one rotating line inside the Mobi hero card with a label,
a 4-segment progress, 3 s dwell, 600 ms slide, pausing on hover/focus/touch and stopping after one full pass (WCAG 2.2.2),
stacked under reduced motion; (B) a branded strip under the hero with number weight (Bricolage 700 tabular in the brand word
colour) and a desk-object icon per fact, each a link to its section. Mobi's name back in the first bubble ("Hi, I'm Mobi." before
the sample line).

## R3-D4 The bottom of held stories, top and bottom shortcuts (LK103, LK104)
Phones (<900 px): the held card stops above a bottom band: --ss-band clamp(80px, 11svh, 104px) (64 px when max-height <= 700 px)
+ safe area; the 40 px top position band moves to the bottom. One page-level fixed bottom bar (extend SectionPosition), outside
.ss__stage, z-index under the nav: a progressive blur (4-5 backdrop layers 1.5/4/8/14 px, masked) over a paper tint (gradient
only under prefers-reduced-transparency or deviceMemory <= 4), and a row: a Top button (44x44), the section name, "n of N" over
an N-segment step bar (220 ms), and a Skip pill to the next section via the controller's LK89 anchor path. Shown while a story is
live, in the dock's slot. The logo on "/" scrolls to the top (<= 3 screens: 850 ms ease-in-out-cubic; further: a 120 ms veil,
instant jump, 240 ms rise) through the scroll bus so no story clamps it. A small "Pricing" pill in the phone nav jumps to
#pricing ("something for the bottom"). Fix the Lab's clipping at 360x640 (short-phone fit). Re-run runMatrix, runFast, runJump.

## R3-D5 The tour's glitch (LK105)
Cause (scrolltour P2-1..P2-5): a render-phase setState in TourScreens useSequence during a startTransition render plus the
inactive settle timer makes an incoming screen show its finished state, blank and rebuild; the outgoing screen pops to finished;
a symmetric crossfade overlaps two slides at ~50/50 for ~115 ms; rail icons lazy-load late; the chip row scrolls late.
Fix: an activation epoch (no render-phase setState; ScrollStory carries a step sequence; useSequence keeps {epoch, value} and
shows events[0] until its epoch matches); while held, inactive screens pause, never settle; sequenced change (out: opacity to 0
in 120 ms ease-in, no transform; in: 200 ms ease-out after 90 ms, rising 0.6rem); rail icons eager with fetchPriority low; the
chip row scrolls from cached offsets in the next frame. Gate: a MutationObserver shows data-ts-step non-decreasing from 0 on
every activation (390 touch, 1440 wheel, 1x and 4x CPU); overlap under 30 ms below 0.25 opacity.

## R3-D6 The exam screen on phones (LK106)
Keep the desktop monitor as is. Below 760 px a phone-native layout inside a phone device frame that matches the monitor's
material: question 18-20 px, options 16 px, nothing under 12 px, 44 px targets, the MockMob / NTA switch kept (answers and clock
survive), header and palette collapse into a drawer; NTA style stays faithful.

## R3-D7, D8, D9 Numbers band, pricing, value, comparison, final card (LK107, LK109, LK110, LK111)
- The numbers band section goes; its true counts (bank size from /api/stats, subjects) move into the plan card as grouped
  lines with a count-up.
- #pricing becomes the /pricing page's one plan ("One plan, everything in it"), extracted into shared components, with its art
  (the foil seal, the volt answer-sheet strip, the "MockMob Pro" chip), as a glass card over a big backdrop word (Pro); the Free
  plan as a quiet line with Start free. Value framing from the offer object, never typed: "₹99 a month is about ₹3.30 a day";
  a segmented control "Full mocks a week: 2 / 4 / 7 / 14" printing "about ₹X a mock" (99 / (n x 30/7), rounded up), with the
  maths shown. Branch on purchasable (monthly vs one-time) and newOfferReleased.
- Comparison (honest, same period, dated): MockMob Pro to May 2027 = 7 months x ₹99 = ₹693, cancel any month, unlimited full
  mocks; against real rows read on 5 Nov 2026 on each platform's own page (prices research P9/P10): an all-access CUET course
  ₹5,499 to May 2027; a science mock series ₹1,168 for 23 full mocks (9 months); per-subject mock packs ₹99 for 3 mocks each.
  Never claim "cheapest"; a "Prices as listed on each platform's page, 5 Nov 2026" note with the sources in a disclosure.
- The final card (close band): keep Sign up free / Log in; brand it (Mobi, the OMR motif); if referralsLive(), one line about
  invite codes from REFERRAL_COPY linking to /signup's invite field; never a code on a guest page.

## R3-D10 Key cards on the home page, and the loading kit (LK112)
A Key cards section (after the Recovery Lab): a real card from data/keycards decks with a 3D flip (600 ms
cubic-bezier(.4,0,.2,1), perspective 1000 px), a glass front over the brand art, a "1 / 5" progress bar, dots, and the rating
keys (Missed it / Got it / Easy with when each comes back) fading in after the flip; Sign up free to keep going. The loading kit:
count-up on true numbers once at 40% in view; shimmer/skeletons for async blocks; row stagger in demos. No splash (our first
paint is faster than Preparoo's).

## R3-D11 Accountancy Part B safety (content research C8)
NTA's 2025 paper asked no Computerised Accounting and a CAS pick drops Analysis of Financial Statements from practice and mocks.
Web now: the Accountancy option line says "The 2025 CUET paper asked Analysis of Financial Statements only." with AFS as the
default. The owner decides whether CAS stays a choice (asked in the report).

## Content lane (LK113, approved)
Computerised Accounting (NCERT leca1ps, leca101-104), Financial Markets (NCERT lebs202 2022, Wayback snapshot, verified digest),
English reading comprehension (~200 authored cards): the 2-3 Nov Key cards pipeline (Sonnet author + Sonnet reviewer per PDF,
review-merge, validate, tiers, gate), published as data/keycards files with the site (content research C1-C9).
