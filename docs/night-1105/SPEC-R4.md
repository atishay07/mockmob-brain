# Round 4, 5-6 Nov 2026 (owner LK117-LK147, his ~11:40 pm full feedback): the orchestrator's spec

His words: docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md on branch feat/app-and-web, section "5 Nov 2026, about 11:40 pm";
ledger LK117-LK147 in OWNER-MASTER-LEDGER.md there. Earlier research: C:/Users/atish/Desktop/mockmob copy/tmp-night/
r3-research/ALL.md (Preparoo measurements, Day green, brand loss, prices). Base: main ce24dc682 (round 3 live).
Effort split (LK145): 80% website at every size (phone 360-412, tablet 768-1024, laptop 1280-1440, desktop 1920), 20% app.
Standing: refine, never cut what he approved; no slop; honest money; real data; 44 px; AA; Night and Day; reduced motion.
Owner decisions here supersede older tests: update pinned tests to the new rule and say so.

## Home page
- H1 Desktop fills the screen (LK117, LK119): Preparoo-scale. Fluid container with small side gutters (about 3-4vw, max ~1680px),
  headline sized to the viewport (about 7-8vw at 1440, never tiny), the Mobi desk card large in the right half, the hero filling
  the first screen; every section re-laid for 1280/1440/1920 (bigger H2 ~72px desktop, wider grids, no empty bands). A brand
  texture behind the hero and key sections in both themes (answer-sheet/OMR bubble field, desk-light falloff; subtle; strongest
  need in Night): the owner asked for texture "like we had previously" - brand-owned, not a generic grid/glow.
- H2 Hero copy (LK120-LK124): CUET highlighted (a volt marker/tag treatment on "CUET 2027." or the typed slot; owner liked how
  Preparoo types the exam name). Find why the typed line is "sometimes there, sometimes gone" (HeroTyped / opening gate /
  sessionStorage / headless checks) and make it reliable on every visit. Remove the fact line under the CTAs; keep only
  "Have an account? Log in". Rewrite the demo card copy from a marketing angle (Mobi's bubble and the card's label: a clear,
  confident invite to try a real CUET question, no "Go."). Replace the fact strip: either the main features (Unlimited fresh
  mocks, Mistake Lab review, Score Recovery, DU Compass, Ask Mobi, Key cards) with icons, each a link, or remove it; add the
  honest price hook "as low as ₹X a mock" computed from the offer at the slider's top value.
- H3 "Not your subject?" (LK123): on the demo card, a tasteful control to pick another CUET subject; then 5 random live
  questions from that subject (a public, cached, rate-limited server route returning only what the demo shows, with the
  explanation; no answer leaks beyond the demo's own reveal; respect egress tests). English stays the default.
- H4 Statement (LK125): "MockMob" is green from the start (always the brand word), the other accent words keep lighting up.
- H5 Phones (LK126-LK128): Lab Repair and SWOT scenes less dense; less white space between items and sections everywhere
  (measure gaps; target a calm 48-64 px section rhythm on phones); Key cards section refined and tighter.
- H6 Exam section (LK129): revert the phone layout to the round-2 version (the monitor scaled, which he liked) and, on phones,
  add a "Try it full screen" key that opens the exam screen in a full-screen overlay at a readable scale (landscape-friendly),
  same MockMob/NTA switch. Desktop monitor unchanged.
- H7 Pricing (LK130-LK132): the plan card sits lower so more of the big "Pro" word shows; in Day the word gets enough contrast.
  The slider: "Full mocks a week: 5 / 7 / 14 / 21" (5 = one a week per CUET paper; say so honestly), showing about ₹X a mock
  (5/week is under ₹5) and the catch "under 10 paise a question" (questions = mocks x 50), all computed from the offer. Remove
  the competitor comparison block and its sources entirely (legal risk). Cleaner UI for the section.
- H8 Dock (LK135): the phone bottom bar re-made: spacing, alignment, a stronger primary CTA (true to the offer, e.g. "Start
  free" with a short true line), Log in secondary; consistent with PublicDock.
- H9 Nav (LK133): the Pricing pill goes to /pricing.

## /pricing (LK134)
The bottom plan card refined to match the home page's card; the last section as a clear "Free or Pro" choice.

## Logged-in web (Arena)
- A1 Learn (LK136, LK139, LK140): cross-check Accountancy Part 1/Part 2 (AFS vs CAS affects only Part B chapters; Part A common;
  three Class 12 books) against data/cuet_syllabus.js and the CUET syllabus PDF, report; fix Learn search (a chapter search
  returns chapters; cards results separate and secondary; the Show answer toggle works and reads clearly); de-clutter Learn.
- A2 Key cards swipe (LK137): in the web Learn run/feed and Key cards study, drag/swipe a turned card: right = Got it, left =
  Missed it, down = Easy, with a visible hint while dragging, keys kept, reduced motion = keys only.
- A3 Navigation (LK141, LK146): phones: the dock's You opens the You page; the top profile avatar opens the account sheet/pop-over
  (quick toggles). Desktop: avatar = pop-over (as now), sidebar You = You page. Sidebar UI refined (spacing, grouping, active
  state, no cut-off items at 1366x768).
- A4 Ask Mobi back (LK143): find where Ask Mobi went (routes /mentor, the sidebar card, the dock); make it a first-class door:
  in the top bar/sidebar on desktop, a clear entry on phones, a card on Today, and "Ask Mobi about this" on results and question
  reviews where it already exists in code. Report the plan in the design note.
- A5 Today and Practice (LK142): make the main jobs one tap and obvious; refine without cutting.

## App (20%, LK144)
Haptics in the Mob tutorial and other missing places; a little more brand green in the Explore and Learn feeds. Build only if
asked; the owner uploads builds himself.

## Usage (LK147)
Keep going; when the weekly meter nears about 95%, stop, commit everything, and write a handoff + a paste-ready prompt so he can
continue on another account.
