# MockMob round 5: make Pip feel continuous, then carry it into the Arena

You are continuing MockMob in C:\Users\atish\Desktop\mockmob copy\mockmob copy. Act as a senior
product designer, motion designer and frontend engineer. You have full creative delegation:
explore, choose, implement and verify. Do not ask the owner to choose routine variants.

## Owner feedback on round 4 (verbatim intent)

"I really like some of the animations, but some only happen when scrolling up, and scrolling down
is a bit glitchy. Sometimes there is an animation in the Mistake Lab and sometimes there isn't.
Especially going down from the Mistake Lab to DU Compass there is no animation at all, unlike in the
scroller. In many places the mascot disappears or is really small, and it doesn't carry forward
anymore. Pip has to be integrated as the mascot in the Arena too, with PrepOS and everything, while
still keeping PrepOS's own identity [the owner said 'that wall of the PrepOS'; confirm in the code
whether this means the PrepOS orb/brand, its paid-reply pause wall, or both, and preserve both].
Both have to be integrated in a tasteful manner."

## Read first

AGENTS.md, PRODUCT.md, DESIGN.md, docs/brain/README.md, ROADMAP-2027.md, the latest STATUS.md
entry, docs/brain/ROUND4-NOTES.md, docs/brain/MOTION.md and
scrollcraft/builds/mockmob-round4/BRIEF.md. Read Scroll Craft in full
(C:\Users\atish\Desktop\mockmob copy\scroll-craft-main\plugins\nateherk-design\skills\scroll-craft\SKILL.md
plus hero-depth, feel, devices, uniqueness, approved-collection, taste, verify) and the Emil Kowalski
skills under .agents/skills (emil-design-eng, animate, improve-animations, review-animations,
find-animation-opportunities, animation-vocabulary, apple-design, mobile-native, break-ui,
prototype, pick-ui-library, ask-sonner). Read node_modules/next/dist/docs before framework code.
Use npm.cmd in PowerShell. Never reset, clean or bulk-revert; the tree holds extensive uncommitted
owner work.

Verification setup that matters: open the dev server at http://localhost:3000, not 127.0.0.1 (the
HMR origin check fails there and the page never hydrates). If you drive Chrome through DevTools,
bring the page to the front or rendering throttles to ~2 fps and all timing evidence is wrong.
In development, `window.__pipSlow = 8` slows Pip's flights for frame-by-frame capture. The page
uses smooth scrolling, so use `behavior: 'instant'` for jump tests and real wheel/touch input for
feel tests. Playwright-core with installed Chrome gives real reduced-motion and touch contexts.

## How round 4 works (so you fix causes, not symptoms)

- `src/components/brand/PipGuide.jsx`: one Pip. Perches are server-rendered `<MascotSeat station>`
  figures (hero, lab, compass, demo, close). The active station is whichever section crosses a thin
  band at the viewport middle (`IntersectionObserver`, rootMargin `-46% 0px -46% 0px`). On a change,
  Pip travels on a fixed flyer if the old perch is on screen, otherwise it "swoops" in from 120px
  above/below the new perch; phones drop in from 32px. Pip rests inside the perch via a portal.
  Reactions come from `pipReact(station, mood)` events and only play where Pip rests.
- `src/components/brand/PipActor.jsx`: poses, eyelid blink overlay. `src/app/brand-pip.css`: perch,
  flyer, motion keyframes, sizes.

Likely causes of the reported glitches. Verify each in the browser before changing anything:
1. The 8%-tall middle band is easy to skip: a fast wheel or flick crosses a section boundary
   between observer callbacks, or two zones register out of order, so a handoff never fires or
   fires backwards. Between the Mistake Lab and Compass there is also a full-width subject marquee
   that belongs to no zone.
2. The off-screen swoop and the very first dock are deliberately short or skipped (first dock
   before any scroll has no animation; the swoop is 120px). Scrolling down usually starts from an
   off-screen perch, so it gets the weak swoop. Scrolling up often has both perches near the
   screen, so it gets the full travel. That asymmetry is probably exactly what the owner sees.
3. The lab peak "eureka" plays once per page view, then only a nod. Whether the visitor sees it
   depends on where the lab's autoplay step happens to be when they arrive.
4. Pip is small: hero 68×78 (62×72 on phones), lab/compass 118×140, demo 64×74, close 90×102 —
   and the drill's own static Pips hide while the guide is on the hero perch.

## Priority 1: continuous, symmetric choreography

Rebuild station detection and handoff so that scrolling down and up feel equally intentional:

- Derive the active station from scroll position against ordered station anchors (with
  hysteresis), not from a thin observer band. Every boundary crossing must hand off, in order,
  including fast flicks, momentum scroll, keyboard Page Down, anchor links and reverse scroll.
  Coalesce rapid crossings into one retargeted flight from Pip's current on-screen position.
- Consider a scroll-linked "carry" between stations: while the visitor scrolls the gap from one
  perch to the next, Pip rides a soft lane in the gutter (scrubbed by scroll, eased, never over
  copy) and lands on the next perch, rather than vanishing off screen and swooping in. Prototype
  this against at least two alternatives (prototype skill, verbatim picker, dev-only route), pick
  one, delete the route afterwards, archive the sources, and record the decision with screenshots.
- Down and up must use the same grammar. Prove it with intermediate frames in both directions at
  every station pair, especially Mistake Lab → Compass, and with a cold feel-check (scroll the
  whole page once, write one word per section, diff it against the brief).
- Make the Mistake Lab peak deterministic: when the visitor arrives at the lab, Pip watches the
  replay, and the jump plays on the first "one next move" the visitor actually sees (queue it until
  the lab is in view and Pip is perched there). It must never depend on luck.
- Give phones their own good version: larger Pip, short local travel, never over the dock, no
  pinning. Respect reduced motion (static perches, no travel).

## Priority 2: presence and scale

- Re-art-direct perch sizes per breakpoint so Pip reads as a character, not an icon: roughly
  120–160px desktop and 88–110px phone at the main stations, bigger at the hero and close. Reserve
  space so nothing shifts. Never cover copy, controls, focus rings or the phone dock.
- Pip should not "disappear": define what Pip does between stations (stays visible in the gutter,
  or the authored silence is shortened). Audit DU eligibility, colleges, stats, pricing and FAQ for
  a natural extra perch only if it serves the story (for example pointing at the free calculator).
- Use the seven original poses well. Cross-fade pose changes inside a motion, keep the blink, add
  small purposeful accents (lean toward what Pip points at, a look toward the answer). No random
  perpetual floating and no stretched raster. Use the original PNG masters in
  artifacts/round3/mascot-high-resolution-png to export larger WebPs if the bigger sizes need them;
  do not regenerate or call paid image APIs.

## Priority 3: Pip in the Arena, alongside PrepOS

Make Pip the student's companion across the signed-in product without making study surfaces busy:

- Where Pip belongs: Today (greets with the one next action), Practice setup (reacts to the chosen
  mode, e.g. points at the exam-day card), session start and finish (Result already switches pose
  by outcome), Review and Saved empty states, onboarding, the first-run tour, loading and error
  states, streak-free milestones that are real (first session recorded, first fresh check passed).
- Where Pip never moves: the timed runner while answering, any data the student is reading.
- PrepOS keeps its own identity (orb, name, voice) and its paused paid-reply wall. Design the
  relationship tastefully: for example Pip hands the student over to PrepOS ("PrepOS has your
  record") and steps aside, or appears small beside the PrepOS launcher only on first visit. Pip
  must never speak as if it were the AI, never generate advice, and never imply paid replies are
  available while they are paused. Prototype two or three treatments, choose one, document why.
- All Pip copy uses real server-backed facts only: no invented streaks, mastery, ranks or gains.

## Priority 4: finish and harden

- Re-run the 38-route × 10-size × 2-theme sweep (the round-4 Playwright harness approach is in
  ROUND4-NOTES.md), plus intermediate and reverse scroll captures of the whole Pip journey on
  desktop and phone, reduced motion, 200% text and touch.
- Measure Pip's cost on the production build at 4× CPU / Slow 4G: frame pacing during handoffs
  with and without the guide, image bytes, no offscreen work. Investigate the lab LCP of 2.9–3.3s
  (text LCP, almost all render delay) and fix it if the cause is proven.
- Run lint, build, recovery, DU, learning, NTA, answer-integrity, payment and Explore/contribution
  tests. Record actual verification and gaps in STATUS.md and a ROUND5-NOTES.md with a skill
  matrix (skill → decision → evidence) and matched before/after frames.

## Next features to plan (after the above; propose, scope and only build what the owner approves)

1. Signed-in end-to-end check on staging: practice → result → review → next practice with a real
   test account, session resume, and the premium NTA submission with both skins.
2. "Tonight's plan" on Today: one 10/20/30-minute plan from the shared server plan, with Pip
   presenting it and a clear done state when the session is recorded.
3. Mistake replay drills: one tap from a Result chapter to a short set of the same chapter's missed
   concepts, with a fresh-question check later (only where content passes the evidence gates).
4. Monthly Pro (₹99/month) activation once the Razorpay plan ID is configured, and its Account
   cancel flow, with existing one-time buyers untouched.
5. PWA install and offline-tolerant session resume for budget Android on patchy 4G.
6. Real-device acceptance pass on a budget Android and an iPhone, plus a screen-reader pass.

## Boundaries (unchanged)

No deployment, production migration, bank mutation, external messages, paid model or image calls,
Razorpay plan creation or checkout. Preserve fonts, volt identity, both themes, campus
illustrations, server scoring, session resume, atomic credits, entitlements, AI-wallet reservations,
evidence quarantine, publicOffer(), truthful creator attribution, the empty testimonial list and the
NTA/DU independence disclaimer. Do not claim simulated or fixture results as live behaviour.
