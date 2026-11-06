# Mobile refinement audit and next steps — 4 October 2026

**Implementation update:** the owner approved implementation and the name **Mobi**.
The local refinement pass is implemented; see `MOBILE-REFINEMENT-IMPLEMENTATION-2026-10-04.md`
for changes, browser evidence and remaining release gates. The audit below preserves the
pre-change findings. No production publication is included in this pass.

Owner brief: the published desktop experience is satisfying; phones are not. Improve mobile animation timing, mascot behaviour, preview composition, Arena navigation and both themes. Use UG Preparoo's mobile craft as a reference. Preserve MockMob's identity and existing working product contracts.

This is an audit and implementation plan, not a shipped UI change. No application behaviour, deployment, migration, account record, payment or paid-model request changed. Working branch is `main`; checkout HEAD and locally recorded `origin/main` both equal `050661022bf839c5bfe1f6dd47c056fc0b9e01a9`. Remote tracking was not refreshed, and browser inspection does not establish the exact production commit.

## Evidence and limits

- Public production inspected at `https://www.mockmob.in/`: 390×844 and 1280×844, dark and light. Sampled hero, Lab, exam demo, Compass and pricing. Additional 390px light reduced-motion check.
- Public reference inspected at `https://ug.preparoo.app/`: 390×844 and 1280×844; sequential wheel scrolling, first feature and assistant sections, screenshots, rendered image URLs and computed backdrop filters.
- Current Arena inspected through development-only `/preview/arena`: Practice setup, branded quick-practice runner and Result at 320, 390 and 430px, both themes. All 18 final captures waited for hydrated content; zero document overflow and zero page exceptions in these captures.
- Navigation menu opened with a tap and closed with Escape at 320 and 390px. This establishes those two interactions only, not focus trapping, screen-reader usability or physical touch behaviour.
- Evidence: `artifacts/mobile-audit-2026-10-04/report.json`, `preparoo.json`, `details.json`, and adjacent PNGs. Scripts: `scripts/design-audit/mobile-current-state-2026-10-04.mjs`, `preparoo-reference-2026-10-04.mjs`, `mobile-detail-2026-10-04.mjs`.
- Initial Arena captures showed loading states and a missing-subject error. They were not accepted as UI verification. The final run supplies a subject and waits for `.pr-head`, `.nta-option` or `.rp-hero` before capturing.
- Local loopback setup initially failed; `127.0.0.1` subsequently served HTML but Next blocked its HMR origin, leaving the fixture unhydrated. Restarting the preview with network access and using the configured `localhost` origin restored hydrated fixtures. No Next config change or cache deletion. Diagnostic script retained.
- Chrome mobile emulation is not a physical phone. No live authenticated attempt, AI repair, premium NTA submission, payment, field performance, Safari, keyboard/safe-area or screen-reader acceptance was performed. Existing tests were not rerun because only audit scripts and documentation changed.

## Confirmed findings

| Before | Proposed after | Why |
| --- | --- | --- |
| Landing Lab autoplay observes the entire `.ml` at threshold zero. At 390px, 40px of the navigation enters the usable viewport while the stage starts at y=1118px. After 6.8 seconds the step has advanced to Find, all ten replay tiles have revealed, and the stage still has **zero visible pixels**. Reproduced in both themes. | Observe a stable replay-content region, accounting for the header and dock. Start at Replay only when that content is readable. Pause all progression when it is not readable or the document is hidden. | The first visible playback must be the beginning. Increasing a whole-section threshold alone is fragile because phone section heights vary. |
| Four vertically stacked navigation rows, caption and pause control occupy 376px before the 632px stage at 390px. The entire Lab is 1036px before its heading. | Compact phone step selection adjacent to the stage; one active explanation, meaningful panel padding and a reachable pause/replay control. Retain complete labels through accessible controls. | Playback and its explanation should be seen together; shrinking type would lose meaning. |
| Desktop Lab also advances with only about 40px of its stage visible. | Apply the readable-content playback rule on desktop too while preserving its side-by-side composition. | The trigger defect exists on both layouts, with a much greater impact on mobile. |
| Pip uses a fixed body portal for phones as well as desktop. Mobile local movement is only 8px, but the static art is hidden whenever the guide is enabled, and visibility requires the entire perch to clear fixed 72/100px bands. | Keep desktop travel. On phones, use a local in-flow actor in a reserved art box, calm entry, and one relevant reaction while its preview is readable. Make handoffs and reverse scroll interruption explicit. | The existing code provides a plausible disappearance/handoff mechanism; a repeatable physical-device glitch has not yet been isolated. Preserve useful character rather than adding more travel. |
| The Practice cost summary at 320px compresses “Included with access” into near-letter-by-letter wrapping beside a 200px Start button; measured summary height is 390px versus 102px at 390px width. | Give cost/reason text its own usable line and a full-width launch action where the two-column summary cannot fit. | A root-overflow check passes while the component is still visibly broken. This is a priority functional layout defect. |
| In the Result fixture, the Find step alone is 1247px at 390px and 1490px at 320px; observations account for 944/1084px. Repair follows all four explanations. | Prioritise the leading chapter and one strongest factual observation; retain the rest in an accessible expandable explanation. Keep a visible route to Repair and then Prove. | The action needs to arrive before several screens of analysis. This is content density, not a claim that the data is wrong. |
| Light Result option letters B and C fail the computed audit at approximately 2.75:1 and 2.82:1. | Correct foreground/background role pairs for correct and wrong option states in light mode; check selected, disabled and expanded states separately. | Status states must remain readable. Ratios are diagnostic readings, not a complete accessibility certification. |
| The sampled public light page has one computed text flag: the decorative logo period, 2.14:1. Dark sampled text has none. Gradients are skipped by this audit. | Treat body text and meaningful controls as contrast gates. Assess the decorative mark appropriately; improve light surface separation and shadows visually rather than claiming broad text failure. | “Light mode feels weak” is broader than contrast. The Lab retains a very heavy dark shadow and substantial unused panel space against paper. |

**Motion review verdict: Block mobile craft acceptance.** First-view playback timing is a confirmed feel-breaking defect. Reduce and retime motion before adding polish. Existing reduced motion shows a complete static replay and removes the floating guide; preserve that path.

## What the Preparoo reference actually shows

The useful reference is phone composition, not a particular image format:

- At 390px the hero uses a dedicated phone illustration, `images/v2_dark_bg_mobile.webp`, rendered about 366×620px from a 1536px-wide raster source. PNG character art and an SVG resource were also observed. JPEG is a raster format; there is no basis for calling these vector JPEGs.
- The compact header leaves the canvas to the content. Large short headings introduce one idea, followed by a highlighted feature explanation immediately above its preview. The flashcard and assistant examples provide a clear sense of what to read and try.
- The captured assistant preview fits into a contained phone-width browser frame. Its small embedded text is not a typography target for MockMob; adapt the information hierarchy, keeping meaningful text readable.
- Computed styles confirm backdrop filters, including layered progressive blur. There are many blur elements, some outside the current viewport; the inventory does not prove all are painted at once or that performance is good on a budget phone.
- A floating free-mock prompt overlays preview content in the captured phone view. Do not inherit that collision. MockMob's own dock must remain outside the preview's active reading/interaction region.
- Neither screenshots nor resource inspection prove how their animation code is authored or establish device frame-rate superiority. No proprietary art or implementation was copied.

Use controlled glass for the navigation/dock or a single illustrative frame where it clarifies layering, with an opaque fallback and reduced-transparency handling. Keep question text and studying surfaces stable and legible. Compare an opaque baseline under CPU throttling before retaining blur; do not add stacked animated blur panels merely to match the reference.

## Implementation order

### Pass 1 — Fix missed playback and broken layouts

1. Lab: separate reveal visibility, playback readability and mascot reaction visibility. The replay's observer must not be the entire tall parent. Account for actual fixed chrome. Preserve elapsed progress across a brief offscreen pause, start the first visit at Replay, and reset only on an explicit replay action. Pause on document hidden; manual step selection remains authoritative. Every timed effect, including tile reveals, must share the gate.
2. Phone Lab: place compact step controls, explanation and stage together. Prefer one active title with previous/next or four usable short step controls; avoid a long horizontal overflow dependency. Size to supported content without clipping longer descriptions or 200% text. Desktop rail remains.
3. Practice: repair summary grid constraints before visual styling. Verify long subject names, free credit costs, Pro inclusion, unavailable inventory and launch-disabled reasons at 320/360/390px.
4. Result: reduce the distance to Repair through ordered disclosure; correct light option state contrast. Keep observations available and separate facts from inferred suggestions.

Files: `src/components/landing/MistakeLab.jsx`, `src/app/mistake-lab.css`, `src/app/(app)/arena.css`, `src/app/(app)/dashboard/DashboardPageClient.jsx`, `src/components/ScoreRecoveryLab.jsx`, `src/components/recovery/result.css`.

### Pass 2 — Phone-specific composition and mascot

1. Audit hero/drill, exam comparator, Compass, campus illustrations, subject links and pricing as phone compositions. Full-size reading text, one dominant action, a contained useful preview and consistent section spacing come first. Reserve illustrative image dimensions before loading.
2. Keep Pip's original artwork and successful desktop travel. Build a phone-local model with stable reserved geometry, no fixed actor tracking document scroll, deliberate limited reactions and reliable static fallback. Reaction must coincide with the explanatory content, not an earlier heading.
3. Naming: **Mobi** was approved by the owner during implementation. Update accessible names and student-facing copy consistently; internal Pip identifiers may stay until a coordinated rename is worthwhile. Avoid mixing two public names.
4. Make public and Arena navigation serve different tasks. Public: exploration, theme, account and one main action. Arena: Today/Practice/Explore/Review plus More, with other destinations clearly grouped. Keep existing destinations; improve menu height/scroll behaviour and focus handling. The timed runner owns its palette and navigation, without a mascot or general app dock competing with answering.

Files: landing components, `landing.css`, `home-refinements.css`, `hero-depth.css`, `brand-pip.css`, `PipGuide.jsx`, `Mascot.jsx`, `AppLayoutClient.jsx`, `arenaNavigation.js` and runner styles only where necessary.

### Pass 3 — Coherent daylight and restrained depth

1. Establish clear ground, raised surface, inset, divider, secondary text, selected, warning, success and focus roles across public and app themes. Keep volt as an action fill; accent text on paper uses the darker accessible role.
2. Refine Lab elevation, inactive states, cards and preview borders. Preserve dark exam-style islands where intentional; tune their transitions to daylight instead of repainting every screen white.
3. Trial a restrained glass navigation/dock treatment in light and dark. Retain only if text, focus and scrolling remain stable at the device floor.
4. Check theme change mid-scroll and mid-preview, persistence after reload, touch active states, desktop hover/focus and reduced motion. Use capability queries for hover; keep zoom available.

### Pass 4 — Acceptance and release

Render and interact at widths 320, 360, 390, 430, 768, 1024 and 1440, portrait and short landscape, both themes. Include 200% text and reduced motion. Verify meaningful layouts, not only no overflow.

- Normal/slow/fast forward scroll, reverse scroll, stop just before the Lab, dwell over its heading, leave mid-step, return, pause/resume, manual selection, explicit replay and background-tab resume. **No progress before the replay is readable.** No reset on each small crossing, no race between two clocks.
- Phone guide: no disappearance of the local fallback, no duplicate faces, no delayed celebration after its explanation has passed, no collision with text, controls, focus rings or dock. Desktop journey must stay intact.
- Arena: cost summary, subject/mode/count choices, disabled launch reasons, menu tap/back/Escape/focus, branded and NTA palette sheets, long questions, answer/clear/mark/next and submission confirmation. Use development fixtures first; separately record real authenticated staging acceptance.
- Performance: production build measurements with a slow network and 4× CPU at minimum. Set a 2.5s LCP / 0.1 CLS target; collect measurements rather than infer them from emulation screenshots. Profile scrolling and blur, including the first visit with unloaded assets.
- Hardware: Android Chrome is the primary floor; also Safari if available. Test browser chrome, safe areas, touch fling, keyboard and long-page return. USB Android remote debugging via Chrome's `chrome://inspect` can help if the user enables it; this session has not established an attached device or an ADB executable. A same-Wi-Fi phone can open the development server by LAN address after connectivity is confirmed. Do not call emulation hardware proof.
- After relevant product edits: `npm.cmd run lint`, `npm.cmd run build`, `npm.cmd run test:recovery`, `npm.cmd run test:learning`, `npm.cmd run test:nta`, `npm.cmd run test:answer-integrity` and the existing payment suite (`node --test data/tests/payment_entitlements.test.mjs`, verify the actual file before running). Keep logs and exact unresolved gates in STATUS.

No new library, paid AI call, production data migration or payment change is needed for these refinements. Paid entitlements, authoritative scoring, atomic credits, AI budget guards, question gates and truthful illustrative labels must remain intact. Release after the mobile acceptance pass and an explicit deployment decision; source/build passing alone does not establish the phone experience.

## Immediate next task

Implement Pass 1 and show paired phone/desktop before-and-after captures, plus recorded playback timing. Then develop the phone-local mascot and preview composition in Pass 2. Do not begin with a blanket cosmetic redesign: the reproduced timing and summary defects are the first acceptance gates.
