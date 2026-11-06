# Round 5 — Pip journey and Arena companion

3 October 2026. Local source and browser evidence. No deployment, migration, bank mutation,
checkout, Razorpay plan creation or outgoing email. Existing user edits were retained.
Image generation was explicitly requested in the live instruction; one concept board was
generated, but the shipped identity uses the original images. The tool exposes no model
selector, so GPT Image 2.5 is not claimed.

## Result and decisions

- Replaced the thin IntersectionObserver station band and asynchronous flight lifecycle
  with cached ordered anchors, midpoint selection, 32px hysteresis and one scheduled frame.
  Fast crossings resolve to the final station; the visible desktop actor retargets from its
  current position. Reverse uses the same rules. Timers clear held reactions; no rest RAF loop.
- Desktop reserves a 180px outer lane at 1100px and above. Pip remains visible through gaps,
  then leaves at the end of main. Phones use 88–110px art and a short local arrival; viewport
  position follows document scrolling exactly, avoiding a trailing overlay on controls.
  Static reduced-motion perches remain. Raster aspect ratios and measured blink boxes match.
  Final matched-frame review also removed the hero perch's unused in-column height on desktop:
  its space is already reserved by the gutter, so the headline and primary actions stay higher.
- Seven stations: hero, lab, compass, demo, eligibility, pricing, close. Eligibility and pricing
  have a useful decision to point at. Colleges, stats and FAQ retain quiet reading space.
- Lab eureka is coalesced until the next-move control is at least half visible and Pip is visible
  and settled. It plays once per view; keyboard-driven step changes do not produce a jump.
  Pose changes fade over 180ms. Repeated nod events cannot restart a held celebration.
- Today loading/error/next action, Practice mode selection, Review loading/error/empty/recorded
  sessions, and Saved error state now use a quiet companion. Existing Result outcome poses,
  onboarding and first-run tour remain. The timed answering surface was not given mascot motion.
  Recorded-session copy reads server data; no claims of first-ever activity, mastery or passed
  fresh checks are inferred from a partial record. Fresh-check celebration remains gated by
  unavailable evidence, not fabricated for the design.
- PrepOS uses the handover treatment: Pip introduces the record-led workspace, while the
  existing orb, name, replies and capability/billing wall retain their roles. Header glass has
  opaque fallback and reduced-transparency/high-contrast treatment. No second AI persona.

## Exploration and evidence

`scrollcraft/builds/mockmob-round5/BRIEF.md` defines the feeling curve and acceptance.
Three interactive alternatives used the prototype skill's HTML/CSS/JS picker blocks:
Gutter (continuous reserved lane), Relay (local perches), Rail (inline column). The same
exploration compared PrepOS paired banner, handover and orb-only treatment.
Sources are archived in `artifacts/round5/prototypes/picker.html`; generator in
`scripts/design-audit/round5-prototypes.mjs`. Opening/handover screenshots exist for all three;
picker ArrowRight changed selection in all three. The first prototype run exposed an inline
quote error, which was fixed before screenshots were accepted. `/preview/round5` was removed.

Chosen: Gutter on wide screens, Relay on phones, PrepOS handover. Rail squeezed the study
canvas; a permanently paired banner competes with the record. These were small structural
studies, not three fully polished product builds. Round 4's page structure/fingerprint is
intentionally retained; this is not a claim of a new-site uniqueness pass.

Matched frames: `artifacts/round5/before/{1280,390}-2-lab.png` against
`artifacts/round5/after/{1280,390}-lab.png`. The before JSON records missed demo/close handoffs.
`journey/` contains quarter-interval frames for all six station pairs in both directions at
1280 and 390, plus lab peak and reverse wheel captures. Later final frames use the corrected
phone document tracking. `arena/` contains six fixture views and their 200% text versions.

Visual feel review: hero **welcome**, lab **curiosity**, compass **orientation**, demo **confidence**,
eligibility **clarity**, pricing **choice**, close **resolve**. Compared with the brief, the lab
still needs its explicit next-move interaction to produce relief; the deterministic peak now
supports that moment. Phone gaps intentionally contain silence rather than pinned reading
content. These words are a design review, not user-study findings.

## Verification

- Lint and production build passed. A subsequent font-bundling rebuild failed with Turbopack's
  internal next/font query error; unchanged retry passed. Failure log retained.
- Recovery 17, DU 19, learning 74, NTA 22, answer-integrity 6, payments/Explore/contribution 20:
  158 passed. Two new station-selection tests cover rapid forward/reverse crossings and
  hysteresis: 160 total. Logs in `artifacts/round5/logs/`.
- 38 routes × 10 sizes × 2 themes = 760 verified loads. 380 public cases on production;
  380 existing Arena fixture cases on development. `sweep/verified.json`: no root overflow,
  pageerror, broken loaded image or failed response. These checks do not certify every control's
  hit area, every offscreen lazy image or live account state.
- The initial sweep's document-start theme script accessed a not-yet-created root element.
  Corrected to the real `mm:theme:v1` storage key and reran. The production-only run correctly
  returned 404 for 380 development fixture URLs; those were separately rerun in development.
  Both intermediate results are retained; neither is represented as the verified set.
- Final interaction check: lab `jump-1` at both 1280 and 390; reduced motion mounts zero guide
  actors and seven static perches; six Arena fixture views at 200% text have zero root overflow.
  Wheel reversal, PageDown and intermediate instant anchor positions were exercised. Browser
  touch emulation is not physical-device evidence.

## Production performance and final touch

Chrome, local `next start`, 4× CPU, 150ms network latency / 1.6Mbps down / 750Kbps up,
cache disabled, two runs per width/mode. Same reserved layout with guide enabled versus
`data-pip-static` before hydration (static fallback, no guide effect). This is a small laboratory
sample, not field p75 or a statistically powered benchmark.

| Final build | Text LCP (two runs) | CLS | Handoff frame p95 |
| --- | --- | --- | --- |
| Phone 390, guide | 1.928s / 1.704s | 0 / 0 | 24.3ms / 24.3ms |
| Phone 390, static | 1.628s / 1.496s | 0 / 0 | 24.2ms / 24.3ms |
| Desktop 1280, guide | 1.912s / 1.540s | 0 / 0 | 24.3ms / 30.3ms |
| Desktop 1280, static | 1.576s / 1.616s | 0 / 0 | 30.2ms / 30.3ms |

The LCP element was the hero lead paragraph. Before the fix, guide-on phone LCP was
2.272s / 3.636s and desktop 2.348s / 2.264s. A document-start CSS ablation (computed animation
verified `none`, network unchanged) reduced phone to 1.936s / 1.604s and desktop to
1.764s / 1.604s. Final source removes only `.lp-lead[data-hero]` animation; surrounding hero
entrances remain. Final values above verify that narrower fix. Earlier route-intercepted CSS
experiments altered network delivery and are excluded from this causal comparison.

Initial mascot encoded bytes: 12,290 phone / 30,498 desktop, identical with and without guide;
the greeting image is reused, not downloaded twice. Counts are initial viewport requests,
not the full library or the full page journey. No image re-export was needed at these sizes.

The desktop figures above were rerun after the final hero spacing correction and are saved
in `performance-desktop-spacing.json`; phone figures are in `performance.json` (phone CSS
was unchanged by that correction). All eight corresponding final idle windows counted zero
RAF callbacks. One earlier desktop window counted 216 whole-page callbacks, so universal
whole-page inactivity is not claimed. A separate guide-callback probe (`scVerifyState` in
the callback, 2.2s windows) recorded one event-driven frame at the hero and zero at the footer.
The guide timer/RAF cleanup is separate from other page animations. Full CPU profiling of all
page effects remains outside this small comparison.

CDP touch forward and reverse changed scroll position 0 → 634 → 0; tapping next move produced
`jump-1`, its center hit the intended button, no page errors and no horizontal overflow.
`touch.json` and touch screenshots record this emulation. Final homepage checks rerun the
20 size/theme combinations after the LCP and desktop-spacing changes; all pass, including
seven stations and computed lead animation `none`. Final matched after frames are production.

## Skill → decision → evidence

| Skill | Decision | Evidence |
| --- | --- | --- |
| Scroll Craft | Authored feeling curve, one peak, deliberate silence, wide/phone grammar | brief, journey frames, feel review above |
| prototype | Three alternatives and original picker; archive and remove route | prototypes directory and generator |
| emil-design-eng | No continuous study motion; rare visible celebration; short transitions | ArenaCompanion, 180ms pose fade |
| animate / animation-vocabulary | Retargeted carry, local arrival, blink, hop/jump/nod vocabulary | PipGuide, MOTION.md |
| improve-animations | Read-only motion audit exposed stale flight callbacks and phone interruption issues | replacement lifecycle; no further subagents after cost instruction |
| review-animations | No stale hide callback, no repeating rapid nod, keyboard frequency gate | event queue and interaction checks |
| find-animation-opportunities | Add calm loading/setup/recorded-session states; keep answering still | Today, Practice, Review, Saved |
| apple-design | Presentation-position interruption, spatially consistent reverse; bounded glass | guide and PrepOS header fallback |
| mobile-native | Document-aligned phone frame, dock clearance, static reduced motion | phone frames and reduced checks |
| frontend-design | Larger character hierarchy while retaining original fonts, volt and authored content | matched frames |
| break-ui | Wide/phone/tablet matrix, text enlargement and loading/error fixtures | sweep and arena screenshots |
| pick-ui-library | Existing React/CSS and one small guide; no added runtime dependency | source implementation |
| ask-sonner | Existing notification system retained; no toast for decorative motion | no new toaster |
| imagegen | Original-reference concept study; original assets shipped | IMAGE-PROMPT.md and concept PNG |
| email | Reviewed integration guidance; this plan contains no email feature or sending authorization | no email changes or sends |

## Remaining release gates

No authenticated staging persistence/resume/premium NTA submission, live payment, physical
Android/iPhone or screen-reader pass. Fixture states are not live product evidence. The owner
later approved local follow-up implementation; the resulting work and subsequent verification
are recorded in `ROUND5-COMPLETION.md`. `ROUND5-NEXT-FEATURES.md` retains the original scope
and remaining external gates.
