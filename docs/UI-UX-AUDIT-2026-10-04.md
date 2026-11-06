Method: dual-agent (A: /root/design_assessment · B: /root/technical_assessment)

# MockMob UI/UX audit — 4 October 2026

Owner follow-up: execution priorities are now defined in `UI-UX-IMPLEMENTATION-PLAN-2026-10-04.md`.
The owner retained official-key trust wording and selected phone performance, accessibility, error
prevention and student expectations as the implementation focus. The findings below remain the
historical audit; its wording-first execution order is superseded by that plan.

**Design health: 26/40 (65%, Acceptable). Technical health: 14/20 (70%, Good).** These are qualitative review scales, not conversion measurements, accessibility certification or a combined statistical score. MockMob has a recognizable visual identity and mostly sound responsive geometry. Its biggest opportunity is to make one useful student action arrive sooner, with fewer competing tools and more precise trust language.

Audit only: no product code changed, deployment performed, real account created, payment submitted or paid model called. Existing checkout edits were preserved. References to illustrative scores describe development fixtures, never student outcomes.

## Scope and evidence

Three surfaces were kept separate:

| Surface | What was inspected | Limits |
|---|---|---|
| Local checkout, localhost:3010 | Current public marketing/tools, both themes, interactive sample, new feature tour | Includes uncommitted work; does not prove deployment |
| Live MockMob, www.mockmob.in | Homepage at 390 and 1440; signup form at 390 and 1440 | Earlier landing composition; no completed authentication/payment/AI flow |
| Development Arena preview | 15 student views sampled; settled dashboard/result independently reviewed at 390 and 1440; timed runner/palette at 320; empty/error/long-name states | Synthetic context, wallets and attempts. Profile initial capture was a loading state. No production transaction proof |

Homepage viewport checks covered **320×740, 360×800, 390×844, 430×932, 768×1024, 1024×768, 1440×900 and 1920×1080**. All observed MockMob document widths fit the viewport. Absence of global overflow does not prove that every label, layer or focus state fits.

Public phone sweep: home, pricing, login, signup, cutoff calculator, subject-combination planner, features, English, CUET 2027 guide, contact and about. Local login/signup resolved to the current session shell, so the actual unauthenticated form was inspected on live signup instead. Desktop sweep at verified 1440×900: home, pricing, calculator, combination planner, features, English, contact, dashboard, result, Radar, PrepOS and Compass.

Student phone views sampled: dashboard, test, result, PrepOS, Radar, Compass, Today, Review, Progress, Saved, Rival, Profile, Onboarding, Explore and Ranks. Development banner height and its 12px View selector are excluded from production usability findings. Initial loading/count-up frames are excluded from stable visual-defect claims.

Rendered interaction checks included correct/wrong sample feedback and focus transfer; public and student menu opening/Escape dismissal; feature selection and ArrowRight behavior; timed question palette; malformed-email native validation without sending an email; and existing long-name, empty-record and connection-error fixtures. The error fixture displayed Try again; successful recovery from an actual network outage was not tested.

Evidence is under `artifacts/ui-ux-audit-2026-10-04/`: independent assessments, viewport measurements, contrast samples, keyboard observations, raw detector JSON and screenshots. Raw measurements labelled `desktop` actually contain width 390 because the initial viewport override affected a different tab. They are retained for provenance and excluded from desktop conclusions; `desktop-corrected` contains the verified 1440 sweep.

## Skills applied

| Skill | Contribution |
|---|---|
| Impeccable audit + critique | Independent visual/technical assessments, ten Nielsen heuristics, deterministic scan, severity and backlog |
| Emil design engineering | Purpose, frequency, input method, precise interaction recommendations |
| Review animations + standards | Marketing versus routine UI motion, reduced motion, layout-animation review |
| Mobile native | Thumb targets, editable font size, safe areas, keyboard/device limits |
| Frontend design | Authored identity, typography, visual hierarchy and restraint |
| Redesign existing projects | Diagnose existing composition while preserving brand and contracts |
| Break UI catalogue | Bounded empty/error/long-name/invalid-input stress checks using existing fixtures |

Generation, image-to-code, Swift/Expo and library-selection skills would not add audit evidence, so they were not invoked. Physical-device and screen-reader work remains a separate verification gate.

## Design specificity and overall impression

MockMob feels authored. Volt action keys, night grid, warm display type, Mobi and concrete CUET questions make it recognizable. Its strongest specificity is functional: original practice, +5/−1 accounting, recorded answer changes, chapter observations and dated admissions rules. Preserve this identity.

The weak point is sequencing. The page introduces eight branded tools, several separate admission demonstrations, analytics, AI and social proof before the student has a compact understanding of the recovery journey. Competitors also sell mocks, weak-topic diagnosis and AI help. MockMob's more defensible direction is a bounded mistake repair followed by a fresh unassisted check, with the evidence limitations visible. That direction is not yet equally clear across marketing, setup and result screens.

## Design health scale

Scale: 0 absent/broken, 1 major problems, 2 usable with significant friction, 3 good with specific gaps, 4 excellent within observed scope. All ten apply because the audit includes actual task interfaces as well as persuasion surfaces.

| # | Nielsen heuristic | /4 | Main evidence |
|---|---|---:|---|
| 1 | Visibility of system status | 3 | Sample verdict/continuation, loading states and result ledger are clear; backend availability not certified |
| 2 | Match with the real world | 2 | Subject/mode language works; branded destination names and official-key safety language need translation |
| 3 | User control and freedom | 3 | Navigation, filters, pause and disclosures exist; focus-driven autoplay remains a gap |
| 4 | Consistency and standards | 3 | Coherent theme/action system; tab/radio roles lack their expected keyboard conventions |
| 5 | Error prevention | 2 | Session cost/mode recap helps; overstated explanation safety creates an avoidable trust error |
| 6 | Recognition over recall | 3 | Numbered setup and named chapters help; eight features and overlapping review destinations add orientation work |
| 7 | Flexibility and efficiency | 3 | Optional fine-tuning and direct review links; phone setup delays the first controls |
| 8 | Aesthetic and minimalist design | 2 | Strong typography; long repeated demonstrations and result metric composition compete with the next action |
| 9 | Error recovery | 3 | Wrong-answer explanation and empty/error actions are constructive; real outage/auth/billing recovery unverified |
| 10 | Help and documentation | 2 | FAQ, guide and instructions exist; task-oriented help and capability distinctions could be clearer |
| | **Total** | **26/40** | **Acceptable — focused improvement needed** |

## Technical health scale

| Dimension | /4 | Assessment |
|---|---:|---|
| Accessibility | 2 | Labelled controls/focus feedback are widespread; custom roles, nested main and small targets need correction |
| Performance | 3 | Deferred media and visibility-gated Lab playback; avoidable width transitions and no device/field performance evidence |
| Theming | 3 | Working day/night roles and intentional separate NTA skin; full contrast/state coverage remains open |
| Responsive design | 3 | Tested global geometry holds; local result wrapping and secondary target/font exceptions remain |
| Implementation integrity | 3 | Product-specific interactions and honest ordinary-practice fallback; isolated semantics/copy issues |
| **Total** | **14/20** | **Good within sampled scope** |

## What works well

1. **Actual product proof before signup.** The sample gives a real question, a supportive wrong-answer explanation and a clear continuation. The observed focus handoff to Next question is useful. This is more persuasive than another feature claim.
2. **A coherent identity across day/night and student screens.** The type, restrained volt action color, companion and console structure belong together. The timed answering surface remains comparatively quiet. Do not flatten the NTA skin into marketing styling.
3. **Careful factual framing in several important places.** One-time access dates, original-practice disclaimers, historical DU rules, eligibility/admission caveats and ordinary-practice fallback are valuable. The empty Radar state suggests a ten-question set instead of inventing a diagnosis. These strengths should guide the remaining copy.

## Prioritized findings

**Ten consolidated groups: P0 0 · P1 1 · P2 8 · P3 1.** These are manually accepted groups, not automated alert counts. P1 means fix before promoting the affected experience; P2 means material usability refinement; P3 means polish/efficiency. No observed issue justifies declaring the whole website unusable.

### UI-01 · P1 · The explanation demo overstates what answer agreement proves

**Evidence:** local `src/app/page.js:67` calls the answer an official key. `src/components/landing/TourScreens.jsx:105` pairs “Matches the official key” with “So it is safe to explain.” The screen is labelled illustrative, but the causal safety claim remains. The product also describes original independent practice questions. Matching a stored key or two model answers does not establish truth.

**Impact:** a student can mistake a consistency check for authoritative correctness. This directly undermines the product's evidence contract.

**Recommendation:** say “matches this question's stored answer key” and describe withholding when checks disagree. Present source/calibration requirements separately. Explain the distinction between currently enabled single-answer Mistake Repair and the gated full fresh-check recovery workflow. Avoid claiming observed mark gains from examples.

**Acceptance:** every explanation claim names the actual evidence; ambiguous official/safe language is removed; held/disagreement states remain understandable and actionable. Suggested command: `$impeccable clarify`.

### UI-02 · P2 · The phone journey takes too long to reach one useful action

**Evidence:** at 390×844 the hero's first answer options are below the initial fold; the primary CTA leads with free-practice setup while the no-signup sample is secondary. Dashboard source places welcome, credit commentary, companion and four statistics before Subject. Its fixture banner adds approximately 140px and is not counted as product friction. The new tour repeats eight choices as dots, cards and full rows, followed by separate recovery/admissions demonstrations.

**Measured context:** local phone homepage approximately **16.9k px**, live approximately **22.5k px**, Preparoo approximately **7.2k px** at the recorded 390×844 snapshots. These are document-height observations, affected by content/state/fonts; shorter length is not proof of better conversion. The visible repetition supplies the actual critique.

**Impact:** newcomers must learn product vocabulary and scroll repeatedly; returning students must pass through framing before selecting their session. DU exploration distracts from the Commerce recovery direction when presented with equal early weight.

**Recommendation:** retain the conventional approved landing structure, but lead with one compact practise → mistake → next action demonstration. Test the no-signup question as the newcomer primary CTA. Group tools under three or four student tasks and disclose the rest. On the dashboard, put subject/default session setup before supplementary statistics while retaining the authoritative access/cost recap beside Start.

**Acceptance:** at 390px a newcomer reaches a solvable question with minimal scrolling; a returning student sees subject/session controls sooner; repeated eight-item selection is removed or progressively disclosed; no entitlement/scoring contract changes. Suggested commands: `$impeccable distill`, `$impeccable adapt`.

### UI-03 · P2 · Result metrics have two concrete composition defects

**Evidence:** settled `a-result-1440.jpg` shows Mobi extending into the Right tile and obscuring its label. Settled `a-result-390.jpg` breaks 33% into separate lines. `ResultPageClient.jsx:144–154` and `src/components/recovery/result.css:12–25,200–204` are the relevant composition. Initial count-up zeros were not treated as defects.

**Impact:** a sensitive score summary becomes harder to trust/read. Repeated “missed marks” framing also delays the achievable next action.

**Recommendation:** reserve the mascot's entire visual footprint in its grid cell; keep the number and percent sign together; put “of answered” below when necessary. Pair the summary with one neutral, concrete chapter action while preserving truthful +5/−1 accounting.

**Acceptance:** at 320, 390 and 1440, no metric label/number is covered; 0%, 33% and 100% remain intact; negative scores and long session labels fit. Suggested commands: `$impeccable layout`, `$impeccable typeset`.

### UI-04 · P2 · Secondary touch targets fall below MockMob's own floor

**Evidence:** rendered tour tabs **20×44px**, Pause **38×38px**; source finder clear **36×36px**. Result filters are 38px high and repair question chips 32px high. Locations: `feature-tour.css:57–60`, `du.css:267–275`, `result.css:103,150`.

**Impact:** dense adjacent dots invite wrong selections; small secondary controls are harder to use one-handed. Primary answers/start actions generally clear the floor.

**Recommendation:** preserve small visual marks inside actual 44×44px hit areas. Eight enlarged dots cannot simply be squeezed into 320px beside arrows; use fewer task groups, a counter plus labelled previous/next controls, or a scrollable selector.

**Standards nuance:** PRODUCT/DESIGN require 44px. WCAG 2.2 AA target size is 24px with exceptions, including an equivalent control. The large tool-list buttons may qualify for that exception, so this report does **not** declare a definitive WCAG failure for the tour dots. See [W3C target-size guidance](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

**Acceptance:** real pointer hit testing confirms 44px targets at 320/390 with no overlapping areas and visible focus. Suggested command: `$impeccable adapt`.

### UI-05 · P2 · The tour's announced tabs do not behave like tabs

**Evidence:** pressing ArrowRight on focused Practice left focus and selection unchanged; all eight tabs had tabIndex 0 and no aria-controls. `FeatureTour.jsx:109–114` has no arrow/Home/End handler or linked tabpanel. Source autoplay records touch/pointer/wheel interaction but does not pause on keyboard focus. Disappearing focused desktop CTA is a source-supported risk, not a reproduced runtime failure.

**Impact:** assistive technology promises a familiar interaction pattern that the component does not implement; reading and focus can compete with automatic advancement.

**Recommendation:** implement complete tabs with roving focus and panel association, or use ordinary labelled carousel-picker buttons. Pause automatic advance on focus/manual selection; restart explicitly. Review inactive slides' keyboard exposure. See [W3C tabs pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/).

**Acceptance:** keyboard-only users can reach every feature, see focus and read without automatic hiding. Arrow navigation works if tabs remain. No claim of an existing keyboard trap is made. Suggested command: `$impeccable harden`.

### UI-06 · P2 · Editable text falls below the documented mobile input size

**Evidence:** finder/combination search rendered at 15px; dashboard chapter search at 14px; Compass controls at approximately 13–15px; Explore selects at 13px; result reflection textarea at 15px. Exclude the development View selector. Live signup email correctly rendered at 16px.

**Impact:** potential focus zoom/recomposition on iOS and unnecessary input reading strain. Automatic Safari zoom was not tested on hardware.

**Recommendation:** set editable phone fields to at least 16px computed size across both marketing and app roots; keep supporting captions smaller. Do not disable user zoom. Start with `du.css:254`, `DashboardPageClient.jsx:443` and shared app field styles.

**Acceptance:** computed font size is at least 16px in both themes and nested tools; real Safari keyboard opening preserves input/caret and the reachable next action. Suggested command: `$impeccable adapt`.

### UI-07 · P2 · Student routes can expose nested primary landmarks

**Evidence:** `AppLayoutClient.jsx:319` owns a main; `TestPageClient.jsx:719` adds another inside it. `MockMobAIHub.jsx:106` also uses main inside the shared app route.

**Impact:** primary-landmark navigation becomes duplicated/nested. This is source-established composition, not a screen-reader certification.

**Recommendation:** retain the shared main, turn route-local wrappers into a div or labelled section, and preserve existing layout classes.

**Acceptance:** one active main per affected route; NVDA/VoiceOver landmark navigation reaches the intended primary content once. Suggested command: `$impeccable harden`.

### UI-08 · P2 · DU category radios lack their expected keyboard model

**Evidence:** `CutoffCalculator.jsx:473–479` provides radio-role buttons with aria-checked and onClick, but no arrow selection/roving tabindex. Buttons remain usable with Tab and Enter/Space.

**Impact:** keyboard users must discover a different convention for a familiar control.

**Recommendation:** use styled native radios or implement the complete radio-group model. Do not penalize the timed answers merely for using pressed buttons: their state names and numeric shortcuts exist.

**Acceptance:** arrow keys select the next category, focus/checked state agree and mouse/touch results remain identical. Suggested command: `$impeccable harden`.

### UI-09 · P2 · Reel statistics need clearer provenance and date handling

**Evidence:** `social.js:37–40` describes an owner-reported 100K+ floor and sets 5 October 2026. `CreatorReels.jsx:160` calls it a running total. This audit's supplied date is 4 October 2026. A reported floor should not sound like a continuously measured counter.

**Recommendation:** label the views as an owner-reported minimum with the actual observation date; retain audience-overlap and paid-partner disclosures. Check the timestamp at publication. Do not manufacture student outcomes or consented Wall of Love entries.

**Acceptance:** displayed date is not future relative to publication; source/provenance is understandable; loading failures never invent counts. Suggested command: `$impeccable clarify`.

### UI-10 · P3 · A few animations have avoidable rendering work

**Evidence:** active DU teaser changes width over 450ms (`du.css:1280`); tour dot indicator transitions width over 350ms (`feature-tour.css:60`). The unused DynamicCompassPreview width warning is excluded. Mobile reveal blur and layered backdrop blur are profiling candidates, not demonstrated jank. No low-end device frame times were measured.

**Recommendation:** use a full-width fill with scaleX for the bar; a stable dot box with transform/opacity for selection. Profile the glass/reveal composition before reducing deliberate marketing choreography. Keep timed answering quiet.

**Acceptance:** subject/feature feedback conveys the same state; layout properties no longer interpolate; reduced motion remains meaningful; verify frame time on the budget Android floor. Suggested command: `$impeccable optimize`.

## Motion and interaction review

| Before | After | Why |
|---|---|---|
| `du.css:1280`: width transition on stream indicator | Stable full-width fill, scaleX from left | Avoid layout interpolation without changing the numeric subject mix |
| `feature-tour.css:60`: width transition on active dot | Fixed hit area/indicator geometry, transform or opacity state | Preserve tactile feedback while avoiding layout animation |
| `FeatureTour.jsx:55–72`: advance may run during keyboard reading | Pause on focus/manual selection, explicit resume | Prevent automatic slide hiding while focus is in the content |
| `FeatureTour.jsx:89`: screen play excludes the tour's playing flag | Define whether Pause freezes advance only or the whole demonstration; make label/control behavior agree | Source shows slide advance can pause while its demonstration timers continue; full freeze was not runtime certified |
| Phone reveal blur/backdrop stack | Profile first, simplify only if it harms readability/frame time | Deliberate marketing motion is appropriate; performance cost is unmeasured |

**Verdict: Block approval of the two easy-to-replace layout animations until corrected.** This is the animation skill's narrow review decision, not a whole-site release verdict. No observed feel-breaking regression justifies removing the marketing motion system. Existing Lab readable-region/document-visibility gating, static reduced-motion alternatives and quiet exam skin are strengths. Actual reduced-motion preference, background-tab interruption and physical-device playback were not tested in this run.

## Competitive comparison

Public pages were inspected at 390 and 1440. These are observations about presentation and visible interaction, not verification of question quality, user counts, score outcomes or competitors' performance guarantees. Only settled screenshots support hierarchy judgments; Preparoo loading-frame captures are retained but excluded.

| Website | Strongest observed presentation | How MockMob holds up | Useful direction |
|---|---|---|---|
| [Preparoo](https://ug.preparoo.app/) | Large focused illustration, grouped product demos, compact feature families | MockMob has a more immediate playable question and a distinctive warm volt identity; it asks the phone visitor to absorb more tools and repeat more demos | Learn from task grouping and compact pacing; preserve MockMob's question-first evidence |
| [Testbook CUET](https://testbook.com/cuet/test-series) | Concrete test catalogue, subject selection, visible Free Test/Start Now cards | MockMob offers a calmer branded learning journey; catalogue/availability is less immediately scannable | Expose subject, mode, duration and availability at the decision point |
| [CUETMOCK](https://www.cuetmock.com/) | Very prominent registration and proof messaging | MockMob looks more restrained and offers product interaction before account creation; CUETMOCK's inspected phone page was considerably longer and busier | Keep proof close to the action with source/consent; avoid accumulating another wall of promotional claims |

Observed phone document heights: Preparoo ~7.2k, Testbook ~8.2k, CUETMOCK ~37.8k, local MockMob ~16.9k, live MockMob ~22.5k CSS px. Testbook's sampled phone document also extended about 132px beyond its viewport. These are contextual snapshots, not a full competitor audit or an accessibility ranking.

Preparoo already presents diagnosis, practice/retesting, analytics and AI assistance. Therefore weak-topic analytics and an AI copilot alone do not establish uniqueness. MockMob should foreground a trustworthy bounded repair with a later fresh check, subject to the actual release gates. A persuasive demo cannot substitute for academic validation.

## Cognitive load, personas and emotional journey

**Cognitive load: moderate.** Main task controls and numbered setup help. Three recurring weaknesses are excess simultaneous choice, delayed first decisions and incomplete progressive disclosure. Eight tour choices, six Study destinations and several review/analysis names require orientation. Four exam answers are intrinsic task choices and should not be treated as unnecessary overload.

| Persona | Observed friction | What helps |
|---|---|---|
| Casey, distracted phone user | First answers/setup below the initial fold; small tour targets; repeated tool introductions | Large primary answers, bottom study navigation, defaults and presets |
| Jordan, first-time visitor | Arena/Radar/PrepOS vocabulary; official-key safety implication; broad tool tour | No-signup sample, numbered setup, plain chapter names and next-step instructions |
| Sam, keyboard/assistive technology user | Tour ArrowRight convention fails; custom radio model and nested main | Descriptive labels, visible sample focus handoff, public/student Escape dismissal |

Arrival feels energetic and supportive. The wrong-answer sample is the emotional peak because it explains without shaming. The long middle tour is the valley. After a low result, repeated missed-mark framing and a compromised metric compete with reassurance. The memorable ending should be one completed, evidenced next action and a dated future check. The fixture's ordinary-practice fallback is honest and should remain visible whenever fresh proof is unavailable.

## Accessibility and responsiveness verification limits

Contrast was sampled from **1,473 repeated eligible rendered text checks** across nine route/theme passes. No eligible content-text failure was found in those samples. One 2.14:1 light-mode logo-dot result is decorative and excluded from text-conformance findings. Gradients/images, translucent or animating ancestors, some nested text and other unsupported compositions were skipped; low-sample dashboard/animated views are not certified. The method is recorded in `contrast.json`; it is not a whole-site WCAG audit.

Still required: physical iOS/Android keyboard and safe-area behavior; NVDA/VoiceOver full flow; 200% text zoom/reflow; hover/focus across all controls and themes; actual reduced-motion/transparency states; background interruptions; long test content; slow-network/assets and LCP/INP/CLS; authenticated attempt/result persistence; payment/webhook recovery; AI receipts and production release-gate verification. See [W3C text-resize guidance](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html). Viewport resizing does not substitute for text zoom or actual hardware.

The timed runner's beforeunload/exit dialog temporarily blocked browser automation. A fresh tab allowed unrelated checks to continue; later the synthetic tab was closed successfully. This is recorded as an automation limitation, not a proven website defect. Existing dev server was left untouched; temporary viewport overrides and audit tabs were cleaned up.

## Detector reconciliation and implementation integrity

Assessment B ran the prescribed CLI exactly once across 31 target-tree files. It produced **137 alerts: 135 advisory, 2 warning**; 77 in TestPageClient, 59 in DU CSS, one in unused DynamicCompassPreview. Rules: 60 color, 57 font-size, 18 radius, two width transitions. Exit 2 means findings, not a broken site.

Current theme-token fallbacks, print black, documented small labels and the intentionally conventional NTA skin account for many advisories. Do not bulk-normalize them into the marketing palette. Both independent reviews were completed before synthesis.

Two conclusions were deliberately corrected during synthesis:

- Assessment A's claim that top-up purchases are closed came from the older plan. Current `data/capabilities.js` has aiCommerce and runtimeAi enabled. No closed-top-up defect is accepted here. Current UI gates still do not prove environment configuration, production checkout or deployment.
- Assessment B's definitive target-size WCAG claim was narrowed because equivalent large selector controls may satisfy the exception. The 44px product-contract/usability finding remains.

No reliable browser overlay was injected: the available evaluation API is read-only and cannot perform the required mutable preflight. Saved CLI/source evidence plus independent rendered checks supplied the fallback. No detector live server was started. Ignore list absent; none added.

## Recommended sequence and acceptance

1. Correct trust language and statistic provenance, using the current capability map rather than stale status prose.
2. Fix result composition, targets, mobile editable text and semantic/keyboard contracts without changing scoring, entitlements or credit RPCs.
3. Shorten the phone journey around one student task; evaluate the no-signup primary CTA using actual funnel evidence rather than assuming conversion gains.
4. Replace the two layout animations; profile other visual effects before changing deliberate motion.
5. Re-audit on real devices and assistive technology, then verify the deployed version separately.

If behavior is subsequently changed, follow PRODUCT/DESIGN/brain contracts, read the installed Next.js guides relevant to the change, run the relevant recovery/question/payment suites and record actual results in STATUS. No such implementation tests were needed or claimed for this documentation-only audit.

Questions skipped: the actionable audit priorities are sufficiently concrete; no owner choice is required to complete the audit. Future implementation can start with the evidence-backed trust/alignment/control fixes, then test the proposed journey changes.

## Selected visual evidence

Settled result, 1440px: mascot overlaps the Right tile.

![Desktop result alignment](</C:/Users/atish/Desktop/mockmob copy/mockmob copy/artifacts/ui-ux-audit-2026-10-04/a-result-1440.jpg>)

Settled result, 390px: accuracy value splits its number and unit.

![Phone result wrapping](</C:/Users/atish/Desktop/mockmob copy/mockmob copy/artifacts/ui-ux-audit-2026-10-04/a-result-390.jpg>)

Feature tour at keyboard focus: small adjacent dots and a second full selector list.

![Phone feature-tour controls](</C:/Users/atish/Desktop/mockmob copy/mockmob copy/artifacts/ui-ux-audit-2026-10-04/tour-focus.jpg>)

Representative live desktop identity (separate deployed version).

![Live homepage](</C:/Users/atish/Desktop/mockmob copy/mockmob copy/artifacts/ui-ux-audit-2026-10-04/live-home-1440-dark.jpg>)
