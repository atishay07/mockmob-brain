# Round 4: restored craft, Pip as a guide, motion system, study loop, sweep (3 October 2026)

Local source only. No deployment, migration, bank mutation, paid model/image call, external
message, Razorpay plan or checkout. `publicOffer()`, creator attribution, the empty testimonial
list and the NTA/DU independence disclaimer are untouched. Evidence: `artifacts/round4/`.

## 1. Regressions: cause, fix, evidence

| Owner report | Root cause (measured) | Fix | Evidence |
| --- | --- | --- | --- |
| Comparator boxes behave strangely | `brand-pip.css` forced `min-width: 44px` on live palette buttons inside `repeat(8, 1fr)`; tracks resolved to `44 44 44 44 44 15 15 15`px, cells 6–8 crushed, palette overflowed 52px. At ≤420px a 5-column override plus `span 2` left holes and a 437px palette. Placeholders lost the NTA grey-gradient cell. NTA `clip-path` shapes clipped the focus/current ring. | One cell geometry for live and decorative cells, `minmax(0, 1fr)` tracks, button = transparent hit target with a 6–10px slop to the gap midline, inner `.lp-exam__cell` carries the shape (rings never clipped). Phones/touch keep 44px live cells spanning two columns. Body reserves the taller skin (560px): switching skins no longer reflows. | `before/comparator-*`, `after/comparator-*` (matched). Tracks now 26.75px ×8, overflow 0; phone palette 214px, no holes; skin switch: body 560 → 560, top 140 → 140. Hit-tested: 33×48 (MockMob) / 32×45 (NTA) on fine pointers. |
| Arena entry animation missing | `arena-support.css` set `.view { animation: none }`. The real hazard: `.view` sits on the shell root and `fadeIn` animated `transform`, which re-anchors `position: fixed` children (sidebar, round-3 phone dock, modals) for 250ms. | Containers fade only; leaves rise (`.pr-head`, `.pr-stats`, `.pr-steps`), sidebar rail staggers once (22ms). Timed runner gets a 120ms fade only. | Live: `arena-fade` ×2, `arena-nav-in` ×17, `arena-rise` ×10 running. |
| Practice lost motion / exam-day clock | Same file forced the NTA console `transform: none`, killed the palette blink. The clock was a static `58:12` (never ticked in any committed or snapshot source). | Restored tilt and pointer-straighten (now gated to fine pointers), straightens when chosen; blink keyframes lose per-frame `box-shadow`; new `NtaConsolePreview`: real countdown with a stepped seconds tick, echoes the chosen subject, pauses offscreen and in hidden tabs. | `after/practice-nta-card-*.png`; measured 58:12 → 58:10 on screen, frozen at 57:49 offscreen, blink `paused`. |
| (found by sweep) Practice lower panels cut off | `.pr-lower`/`.pr-panel`/`.pr-subs` grids used implicit `auto` tracks; one no-wrap title set a 548px width from 320 to 1440px. Root overflow was 0 (body clips), so earlier checks missed it. | `minmax(0, 1fr)` tracks. | Sweep 20/20 clean after. |

The demo exam clock on the homepage now starts at the visitor's first answer, runs only on screen, and resets.

## 2. Pip as a Scroll Craft guide

Brief (self-authored under delegation): `scrollcraft/builds/mockmob-round4/BRIEF.md`. Feeling curve:
welcome (hero greeting, reacts to the drill) → curiosity then relief (Mistake Lab thinking, jumps once
when the leak becomes one next move: the engineered peak) → orientation (Compass, Pip on the leading
side pointing at the headline) → delight (exam preview, cheers the visitor's answers) → resolve
(close, encouraging). Signature move: the perch handoff.

Prototype comparison (prototype skill, verbatim picker, dev-only route, archived to
`artifacts/round4/prototypes/pip-journey`):

| Direction | Axis | Observed | Verdict |
| --- | --- | --- | --- |
| Lane | Continuous presence, fixed side lane scrubbed by scroll | At 1280 there is no gutter: Pip overlapped the heading edge (1158–1254 vs 1185) and pointed off-page; impossible on phones; per-scroll-frame layout reads + state | Rejected |
| Perches | One Pip per station, arrival animation | Two Pips on screen at once on tall viewports; re-animates on every reverse scroll; read as stickers sliding in (the owner's exact complaint) | Rejected |
| Handoff | One Pip travels between perches, event reactions | Single identity, zero per-frame work while resting, local phone adaptation | **Chosen** |

Implementation: `PipGuide` (client island, marketing only), `PipActor` (eyelids drawn in the visor
colour from measured eye boxes; raster never stretched), `pipEvents`. Perches stay server-rendered
static poses (no-JS / reduced-motion fallback). Rules learned while verifying: off-screen handoffs
swoop in locally (a long crossing passed over a caption); first appearance before any scroll docks
without ceremony; reactions to actions taken while the perch is offscreen are queued ≤10s; one Pip
in view (the drill's own static Pips step aside while the guide is visible); flyer sits under the
nav (60) and dock (70).

Evidence (`artifacts/round4/pip/`): hero celebrate on a real drill click, lab thinking → peak jump on
a real "Get one next move" click, Compass pointing, exam preview cheer after five real answers,
close, mid-flight frames forward and reverse (40× slow motion, numeric path samples: reverse swoop
299 → 196px onto a 197px target), long smooth glide across all stations ends docked at hero, phone
drop-in at 390.

Feel-check diff: intended = welcome / relief / orientation / delight / resolve. Felt cold: welcome,
relief (the jump lands), orientation, *nothing* at the exam preview (the cheer fired while the
perch was below the fold at 1280×860), resolve. Changed the page, not the brief: queued reactions.

Elsewhere: first-run Arena tour shows Pip per step (greeting, encouraging, thinking, celebrating)
with a nod and blink; onboarding greets once; loading/empty/error state Pips settle once; Result
Pip follows the outcome (celebrating ≥40%, encouraging below). No Pip motion in the timed runner.

## 3. Motion system

`docs/brain/MOTION.md`: three tiers (storytelling, selection, answering), shared tokens, vocabulary,
reduced-motion policy. Seven `transition: all` rules named; four ungated moving hovers gated.

## 4. Study loop

Result now ends with one next step from the same pure engine as the on-page readout and PrepOS
(`computePrepOSInsights`): it names a chapter only when the engine ranks one (≥4 answered), otherwise
"Practise another set" in the same subject, plus Review mistakes, Saved, Radar and Back to Practice.
A first draft contradicted the readout (named a chapter from 1 wrong answer); caught in the browser
and replaced. Saved gains "Choose practice" beside Explore. Review already loops via the shared next
action and session cards. Real-touch flows (Playwright `tap`): More sheet opens and a link closes it;
Explore answers by keyboard Enter with focus moving to feedback; onboarding toggles and saves with
the preview notice; a failed contribution keeps the draft, options and chosen key.

## 5. Responsive, accessibility, performance

Route checklist (source-derived): 19 public routes; 19 Arena views via the dev fixture (Today,
Practice, Explore, Review, Progress, Saved, Radar, Compass, PrepOS, Ranks, Account, Contribute, My
uploads, Result, Rival, Recovery, Onboarding, runner MockMob and NTA). Excluded: `/admin`, `/creator`,
`/moderation` (staff), `/auth/callback`, other preview routes.

Sweep (`artifacts/round4/sweep/sweep.json`, 760 loads = 38 routes × 10 sizes × 2 themes, touch on
≤1024, phones mobile-emulated): root overflow 0, load failures 0, console errors 0. Real defects
found and fixed: Practice panel escape (above), 36–40px targets (`pr-link`, chapter chips, Today
minutes, runner interface switch, Recovery link). Reruns of the affected routes: clean. Accepted:
homepage palette cells on fine pointers (hit slop, see table); dev-fixture-only "Preview assistant
drawer" chip. Three "occluded" flags were false positives (empty `<p>` boxes / no dock; checked by
screenshot and last visible text). 200% text (root and body font doubled) on six key routes at 390
and 1280: no overflow; only visually-hidden screen-reader text and an intentional 4-line reel clamp.
Reduced motion in real Chrome: guide off, five static perches, Arena 160ms fade, console still, demo
clock still.

Performance (production build, `next start`, 390px, 4× CPU, Slow 4G, lab): LCP 2.93–3.29s across two
runs (text LCP, ~all render delay), CLS 0.00. Hero entrance not proven to be the cause (an override
test did not apply on reload); not changed on a hypothesis. Pip cost: two ~30KB images on the phone
homepage, greeting reused by the guide (no duplicate request); no per-frame work while resting;
frame intervals during a jump-and-handoff p50 18–25ms, p95 ~50ms (upper bound, includes painting the
new section).

## Skill matrix

| Skill | Applied decision | Evidence |
| --- | --- | --- |
| Scroll Craft (SKILL + hero-depth, feel, devices, uniqueness, approved-collection, taste, verify) | Self-authored brief, feeling curve before devices, one peak, signature move, peak moved out of the act stack, intermediate and reverse positions verified, feel-check diff acted on, fingerprint row appended | BRIEF.md, FINGERPRINTS.md, `pip/` frames |
| emil-design-eng | Frequency-based gate (no motion while answering; delight only at rare moments), asymmetric short UI timings | MOTION.md tiers |
| animate (+ RECIPES) | Exact curves solved per frame, transform/opacity only, reduced motion shipped with each change | PipGuide bezier, keyframes in brand-pip.css |
| improve-animations | Recon sweeps before changes (transition: all, ease-in, scale(0), ungated hover via postcss) | 7 + 4 fixes, globals.css diff |
| review-animations | Self-review: blink box-shadow paint removed, interruption via presentation value, no keyframes on rapid toggles | NtaConsolePreview, flight retarget test |
| find-animation-opportunities | Added: demo clock on first answer, tour Pip, Result outcome pose. Rejected: animating the runner progress fill, Pip in the answering surface | MOTION.md |
| animation-vocabulary | Named: perch handoff (shared element travel), swoop, stepped tick, hop/jump/nod, settle | BRIEF.md, MOTION.md |
| apple-design | Interruptible flights from the presentation value, independent X/Y curves, spatial consistency on reverse | numeric path samples |
| mobile-native | Hover gated to fine pointers, tap highlight off on palette, 44px touch cells, flyer under dock, phone drop-in | sweep, hit tests |
| break-ui | Long chapter titles in Practice exposed the 548px panel; long subjects on the console bar truncate | sweep fix |
| prototype + picker | Three structural directions, verbatim picker, chose and deleted the surface | archived sources, screenshots |
| pick-ui-library | No new runtime: existing CSS + small client island; Motion not needed | package.json unchanged |
| ask-sonner | Reviewed toast needs: existing ToastProvider kept, no second toaster | no change |

## Remaining gaps (honest)

- No physical Android or iPhone run; touch was Playwright/CDP emulation. No screen-reader pass.
- Authenticated persistence, session resume, real premium NTA submission and payments were not
  exercised (fixture blocks writes). The Result "Practise this chapter" link relies on the existing
  single-chapter launch; its server entitlement path was not traced end to end.
- LCP 2.9–3.3s in the throttled lab is above the 2.5s p75 target; cause not isolated.
- Desktop palette hit areas are 32–33px wide (fine pointer only) to keep the NTA grid exact.
- Contrast was measured on the new surfaces only (Pip captions, demo clock, palette cells, Result next
  step, exam-day console, Practice links), both themes: lowest 5.98:1. Other routes were not re-audited.
