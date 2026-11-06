# UI/UX implementation plan — 4 October 2026

Status: core scoped UI changes implemented and locally verified on 4 October 2026. See `UI-UX-IMPLEMENTATION-RESULTS-2026-10-04.md` for actual evidence and remaining gates. Physical-device accessibility and controlled/field performance acceptance remain open; no deployment performed.

Owner direction: prioritize phone performance, accessibility, error prevention, clear student expectations and useful actions. Preserve the existing brand, product mechanisms and owner-approved trust wording. This is a scoped execution plan beneath `PLAN-2026-10-04-NEXT-DAYS.md`, not a replacement product roadmap.

## Outcome

A student on a budget Android connection can reach the first useful action quickly, operate the interface comfortably, understand the current state and recover from an error without losing context or accidentally repeating a charge. Desktop retains its current identity and capabilities. Improvements are demonstrated by before/after behavior and measurements, not a higher subjective audit score alone.

## What matters and what does not belong in this sprint

| Audit item | Decision | Reason |
|---|---|---|
| Phone loading, interaction delay, scrolling and animation work | Measure first, then optimize early | Highest product/device priority; the audit did not establish actual low-end frame time or field Core Web Vitals |
| Result mascot overlap and split percentage | Fix directly | Confirmed obstruction of useful information |
| Small touch targets, small editable text, keyboard/focus issues | Fix directly | Concrete access and input friction |
| Held/failed repair versus completed repair, pending actions and retries | Inspect and harden | Students must know what happened and what they can do next |
| Delayed sample/setup controls, repeated tour navigation | Refine the flow | Extra orientation work before the student can act |
| Nested main landmarks and custom DU radio behavior | Fix with the accessibility pass | Small scoped changes with functional value |
| Official-key versus stored-key marketing terminology | Exclude | Owner retained the trust wording and explains that the key is based on official material. Do not rewrite it as part of this UI/UX sprint |
| Statistical provenance/date wording | Defer to normal content maintenance | Not a reason to delay phone/accessibility improvements |
| 137 detector alerts, palette literals, tiny documented labels and NTA skin exceptions | Do not bulk-fix | Most were contextual advisories, not confirmed user-facing defects |
| Cleaning unused demo components | Defer | No effect on the rendered journey unless bundle evidence establishes otherwise |
| Matching a competitor's page height | Reject as a target | Shorter pages do not establish better usability or conversion |
| Removing all glass, motion, Mobi or DU features | Reject as an approach | Preserve useful identity/capabilities; change expensive or repetitive presentation only where evidence supports it |
| Renaming Arena/Radar/PrepOS or changing prices/access | Out of scope | Improve task guidance while retaining product vocabulary and existing authoritative contracts |

The original audit remains a historical record. This owner-selected plan supersedes its execution order and wording priority. Retaining marketing wording does not change runtime evidence checks, disagreement handling or release flags.

## Working rules

- Inspect the current rendered state and dirty tree before editing; the checkout may have evolved since the screenshots. Reproduce each defect first and skip anything already fixed.
- Read PRODUCT.md, DESIGN.md, brain README and the owner working plan. Use the current capability/offer functions for runtime availability and prices; older prose is not a reason to flip flags.
- Keep scoring, quotes, entitlements, wallet reservations, idempotency and question verification authoritative on the server. This sprint changes presentation and client interaction, not those contracts.
- Preserve Mobi, volt identity, both themes, the no-signup sample, sourced DU tools and the quiet timed-answering surface.
- Make focused, reviewable changes in the batches below. Compare each batch with its baseline before continuing. Do not broadly reset the checkout to undo unrelated work.
- Existing behavior that already works should be tested and retained, not reimplemented. Read relevant installed Next.js guides before framework changes.
- No production migrations, paid-model benchmarking, price changes, real checkout submissions or automatic deployment are needed for this UI/UX implementation. Fixture states cover interaction work; real service gates are recorded separately.

## Batch 0 — Establish the baseline and reproduce the defects

**Dependency:** none. **Deliverable:** compact route/state matrix, screenshots and performance baseline with commit/dirty-tree provenance.

1. Pin the current local version and live version separately. Use production builds for loading/bundle measurements; development preview fixtures remain layout/state evidence. Do not enable development preview routes in production to make a benchmark work.
2. Core routes: homepage, Practice setup, timed runner, Result, PrepOS. Secondary routes: pricing/signup, calculator, combination planner and Explore.
3. Reproduce overlap/wrapping, tour keyboard behavior, small targets and editable font sizes at 320/390/1440. Include both themes, settled content and sticky controls. Exclude fixture banners from production layout conclusions.
4. For performance, record initial JavaScript transfer, main-thread tasks, LCP/CLS, controlled input-to-feedback timing, scroll frame-time distribution and offscreen/background timer work. Identify the actual bottlenecks before choosing optimizations.
5. On the same production build, device/browser and network/CPU settings, take at least five comparable cold-load samples per core measured route and summarize median plus spread. Use a separate warm interaction trace. Save settings, raw results and exact version; avoid mixing development and production numbers.
6. Use supported browser/DevTools diagnostics. If CPU/network throttling, tracing or hardware access is unavailable, record it as an open gate rather than substitute unverified numbers. Existing design-audit scripts are references and require checking against the active tooling and current routes before reuse.

**Completion:** each planned direct fix has a current reproduction or is marked already fixed; performance bottlenecks have trace evidence or an explicit measurement limitation. No invented baseline or claim that emulator results represent physical phones.

## Batch 1 — Phone performance and stable composition

**Dependency:** Batch 0. **Primary files:** `src/components/landing/FeatureTour.jsx`, `TourScreens.jsx`, `src/app/feature-tour.css`, `home-refinements.css`, `src/components/recovery/result.css`, `src/app/(app)/result/[id]/ResultPageClient.jsx`, shared app field styles.

### Direct fixes

- Reserve the full mascot footprint in Result. Keep score/accuracy number and unit together; allow the descriptive label to wrap beneath. Test 0%, 33%, 100%, negative scores and long subject/session labels.
- Reserve dimensions for screenshots, cards, images and loading placeholders so asynchronous content does not move the student's target. Loading/skeleton states must not leave the essential action permanently invisible.
- Set phone editable inputs, textareas and selects to at least 16px computed text size, accounting for the different app/marketing roots. Preserve user zoom.
- Replace the active tour/DU width animations with stable geometry and transform/opacity where straightforward. These are small efficiency improvements, not by themselves proof that the phone is fast.

### Trace-driven optimization

- Stop inactive/offscreen demo timers and unnecessary renders; pause document-hidden playback without catch-up. Show a useful settled state for reduced motion.
- Give Pause a clear operational contract: pause slide advancement and the active scripted demonstration. Resuming must not jump through missed stages. Keyboard focus/manual selection should stop automatic movement until explicit resume.
- Defer below-fold interactive demo code only if bundle/trace evidence shows it matters. Preserve server-rendered explanatory content and reserved-height fallbacks. Load before the student reaches the interaction; avoid replacing eager work with a visible blank or interaction-time waterfall.
- Review layered blur, mobile reveal filters and animated shadows. Simplify the largest measured cost while retaining glass/motion where it performs well. Do not hide required content until an animation or IntersectionObserver runs.
- Optimize the actual LCP asset/font path identified by measurement. Do not lazy-load the LCP element or preload every image/font. Keep third-party embeds interaction-triggered.

**Framework references:** installed `node_modules/next/dist/docs/01-app/02-guides/production-checklist.md` and `lazy-loading.md`, plus the current image/font guides if touched. The installed lazy-loading guide warns that importing Client Components dynamically from a Server Component does not currently provide automatic client code splitting; do not assume wrapping everything in dynamic imports solves the payload.

**Completion:** no result overlap/split unit at 320/390/1440; essential content survives motion-disabled/failed-script states; no hidden-demo timer work in measured cases; before/after traces show the targeted improvement without a new input delay, blank demo or layout shift. Retain expensive-looking effects if they are not the actual bottleneck.

## Batch 2 — Accessibility and reliable control behavior

**Dependency:** stable composition in Batch 1. **Primary files:** FeatureTour/CSS, `src/components/du/SubjectPicker.jsx`, `CutoffCalculator.jsx`, `du.css`, result controls, `AppLayoutClient.jsx`, `TestPageClient.jsx`, `src/components/ai/MockMobAIHub.jsx`.

1. Bring action hit areas to at least 44×44px. Include tour controls, clear buttons, result filters, question chips and retry controls. Keep small visible icons inside larger hit areas. At 320px, use previous/next plus a counter or a scrollable selector instead of squeezing eight enlarged dots into the same rail.
2. Treat the tour as a carousel with labelled previous/next, slide position and Play/Pause. Avoid duplicating the same eight-item selector on phones. If tabs are retained, implement roving focus, arrow/Home/End behavior and linked panels fully; do not leave partial tab semantics.
3. Make offscreen/inactive content's keyboard exposure intentional. Programmatic inactive state must not trap focus or hide an element that currently owns focus. Manual selection preserves an understandable focus position.
4. Use native styled radios or a complete radio-group keyboard model for DU categories. Preserve click/touch behavior.
5. Keep one active main landmark in student routes. Change nested wrappers to a div or labelled section without changing their visual layout.
6. Verify visible focus, Escape dismissal/focus return, dialog focus containment where appropriate, and focused content clearance from sticky headers/docks. Avoid noisy automatic announcements from demo timers.
7. Test 200% zoom/text enlargement, reduced motion, both themes and relevant contrast states. Fix failures that affect readable content/control states, not decorative logo-dot contrast.

The [W3C carousel pattern](https://www.w3.org/WAI/ARIA/apg/patterns/carousel/) supports stopping rotation when focus enters the carousel and resuming through explicit user action.

**Completion:** homepage/sample and setup/review navigation can be operated by keyboard with visible focus; controls meet the product target floor; no focused control is obscured; DU category navigation is conventional; affected routes expose one main. Screen-reader and physical keyboard/device results are recorded separately when available.

## Batch 3 — Student expectations, error prevention and recovery

**Dependency:** Batches 1–2. **Primary files:** `DashboardPageClient.jsx`, `ResultPageClient.jsx`, `src/components/recovery/MistakeRepair.jsx`, `MockMobAIHub.jsx`, `src/components/ui/SignupCard.jsx`, existing shared error/loading components.

### Practice setup

- Move subject and default session setup ahead of supplementary statistics/companion commentary. Keep a compact access/credit indicator rather than hiding cost or entitlement information.
- Show subject, mode, question count, expected duration and server-quoted cost near Start. If access is still checking, say so and prevent launch; if unavailable, explain the reason and offer the appropriate next action.
- Preserve existing quote matching, expiry revalidation and launch idempotency. The source already has these guards; verify them after moving the UI.
- Keep selected subject/mode/count on recoverable failures. Start responds visibly once and cannot be accidentally submitted twice.

### Repair and result states

- Treat pending, explained, stored, held for re-check, not explained, insufficient credit and uncertain request outcome as distinct states.
- Current source at `ResultPageClient.jsx:92–93` adds held/not-explained outcomes to the same `repaired` set as successful outcomes, and the answer row displays Repaired from that set. Reproduce via existing fixtures, then separate outcome display from whether a request has already been handled. A held question must remain visibly held and must not be immediately re-requested as a new paid action.
- Preserve server responses and accounting. Do not infer refund/payment success from client state. An uncertain reply outcome uses the existing same-request retry behavior where supported.
- After a score, offer one concrete recommended next action. Keep all answer review and chapter detail accessible below it; do not claim the repair was learned merely because an explanation was displayed.

### General recovery

- An error communicates what failed, what state was retained and one useful action. Avoid full-page reload for a local failure where a scoped retry safely preserves context.
- Keep form values on validation/service failures; move/announce errors appropriately. Check existing signup pending and alert/status behavior before adding new controls.
- Empty states suggest the next available task. Unavailable inventory/access does not look like a broken page or a completed task.

**State acceptance matrix**

| Situation | Required student experience |
|---|---|
| Quote loading/error/expired | Clear status; safe disabled/recheck Start; current choices retained |
| Rapid Start taps | One launch intent; visible pending state; existing idempotency retained |
| No record/no eligible questions | Useful ordinary-practice/setup next action; no fabricated diagnosis |
| Repair explained/stored | Explanation/retrieved explanation visible; appropriate continuation |
| Repair held/not explained | Distinct status and safe alternative; no Repaired badge |
| Credit balance unknown/insufficient | No guessed allowance; authoritative reason/options |
| Request outcome uncertain | Existing request can be retried safely; no client claim of an unverified charge/refund |
| Result/auth load failure | Retry path and retained context/values; no silent loss or endless spinner |

**Completion:** each state has a deterministic fixture/browser reproduction; rapid taps and delayed responses do not produce duplicate intent; outcome labels match the response; no scoring, wallet, price or model changes were introduced.

## Batch 4 — Shorter, clearer activation journey

**Dependency:** reliable controls/states first. **Primary files:** `src/app/page.js`, landing layout CSS, FeatureTour, dashboard/result composition.

1. Make the no-signup question easy to find and operate. Reduce mobile hero preamble/spacing enough that the question and first answers arrive promptly; keep the price/trust information readable.
2. Use the no-signup sample as the prominent first-time action and free practice as the account/setup action. Preserve logged-in destinations. Evaluate existing funnel evidence where available; this is a design proposal, not an established conversion lift.
3. Present feature discovery through student tasks: take a set, review/repair a mistake, choose the next set, explore DU options. Keep existing feature names/capabilities inside those groups.
4. On phones, use one tour selector. Consolidate repeated explanatory sections where they repeat the same proof. Keep DU tools accessible and preserve the source disclosures; do not delete the tools to shorten the page.
5. Keep an obvious next action across Result, Review, Radar and PrepOS using the existing shared plan. Do not build a second client recommendation engine.

**Completion:** at 390×844, the first question and initial answer choices are reachable after at most one short scroll (roughly half a viewport), with no sticky obstruction; at 320px content remains readable without forced clipping. Returning students reach subject/session controls sooner than the baseline. A newcomer can identify the first action and post-result next action without learning all eight tools. Page height and conversion remain observations, not arbitrary pass/fail thresholds.

## Batch 5 — Verification and release evidence

**Dependency:** completed batches and a production-build remeasurement after composition changes.

### Responsive/interaction matrix

- Layout: 320/360/390/430 phones, 768 tablet, 1024/1440/1920 desktop. Run the core interaction matrix at 390 and 1440 in both themes; run boundary controls at 320.
- States: settled/loading/error/empty/long text; free/Pro/expired/unknown balance; repair explained/held/not explained/insufficient/failed/uncertain; quote loading/blocked/expired.
- Input: real pointer hit testing, touch where supported, keyboard, focus/Escape, 200% zoom, reduced motion. Record physical Android/Safari and NVDA/VoiceOver checks as completed only if actually performed.
- Timed answering remains quiet. Test long question/palette layout and sticky action clearance without using fixture scores as student evidence.

### Performance acceptance

The standard field objectives are **LCP ≤2.5s, INP ≤200ms and CLS ≤0.1 at the 75th percentile**, segmented by mobile/desktop. [Google Web Vitals guidance](https://web.dev/articles/vitals).

Before release, repeat the controlled production-build baseline and interaction traces on the same settings. Show improvement in the actual bottlenecks and investigate any regression. Lighthouse/TBT is not field INP; five lab loads are not a 75th-percentile user population. If available field data cannot establish the objectives, report the gap. Do not add a telemetry system or collect student answers/PII just to complete this UI sprint.

### Existing checks after relevant edits

Use `npm.cmd` in Windows PowerShell when the npm script shim is blocked:

```text
npm.cmd run lint
npm.cmd run build
npm.cmd run test:recovery
npm.cmd run test:answer-integrity
npm.cmd run test:nta
node --test data/tests/payment_entitlements.test.mjs data/tests/monthly_billing.test.mjs
```

Also run `npm.cmd run test:learning` when repair/setup/PrepOS state work touches their client/service contracts, and `npm.cmd run test:du` for DU control changes. Add only focused behavior tests for materially changed outcome/keyboard/retry behavior; do not write tests that merely mirror CSS values. Report existing baseline failures separately from regressions caused by the work.

### Delivery

- Save before/after screenshots, performance settings/results, changed files, actual checks and remaining gates in a new implementation artifact folder and STATUS.md.
- Keep each batch reviewable and independently reversible. Revert only the batch's own edits if it causes a regression; do not reset other user work.
- A passing source build is not production publication. After a separately authorized deployment, verify the exact live version's layout and key actions; physical hardware/auth/payment/model gates remain explicit if unresolved.

## Order to execute

**Baseline → phone performance/composition → accessibility → student state/error handling → activation flow → final measurement and release evidence.**

Use scoped Impeccable adapt/harden/layout/distill work, Emil interaction guidance, animation review and mobile-native guidance as appropriate. Spend effort on the student outcomes and measured bottlenecks, not accumulating skill invocations or detector-cleanup totals.
