# Round 5 completion and approved follow-up — 3 October 2026

Continues `ASTRA-ROUND5-PROMPT-2026-10-03.md` and `ROUND5-NOTES.md`. The owner approved
implementing the remaining local work and restoring the local site. This record distinguishes
source implementation, fixture evidence and read-only live-account observations. Nothing was
deployed, migrated, purchased, generated as paid educational content or sent externally.

## Previous cutoff and delivered work

The continuation began with remaining acceptance work around visible autoplay, control
clearance, session handover and real milestones. The main seven-perch choreography and
prototype decision are recorded in `ROUND5-NOTES.md`. The later owner approval also covered
the proposed Tonight/replay/PWA work. The following local implementations now exist:

- **Tonight's plan:** Today uses the existing shared 10/20/30-minute server plan. Launch
  metadata travels through Practice setup into the server session snapshot. Only a current
  IST-day, server-scored recorded attempt produces the done state. A 30-minute plan contains
  20 practice questions and 10 minutes of review; recording practice does not claim that review
  is done. Real links retain ordinary new-tab and keyboard behavior.
- **Recorded milestones:** the first server-scored session and a passed fresh delayed check
  come from owner-scoped attempts and currently validated episodes. Blocked/invalidated
  evidence is excluded. No invented streaks, mastery or score-gain claims.
- **Mistake replay:** Result checks missed/skipped chapters read-only, and offers five unseen
  questions only where the launch subject, canonical chapter and current evidence pass. The
  API checks ownership, rate limits and all historical question/family exposures; launch
  rechecks content and access. Unavailable/unsupported records remain unavailable. The
  delayed-check pathway is separately labelled. No question bank mutation or generation.
- **PWA and patchy connection:** manifest/icons reuse existing brand art. The worker caches
  only the public offline page and two icons, never account HTML, APIs, RSC or answers. It is
  registered in production only. Install is offered when the browser provides a prompt;
  iOS receives explicit Safari instructions. An already-open runner preserves the original
  session identity, answers and deadline on the device. A full offline reopening needs a
  connection: the fallback says so explicitly. Logout removes only that user's study drafts.
- **Bounded submission:** failed network submissions freeze answers and remain pending.
  Reconnect retries within the existing two-minute server submission window; reload does not
  reset the timer or create a replacement session. The mobile palette closes on submission
  so the retry/error state remains visible. After expiry the server remains authoritative;
  late durable uploads include only server-acknowledged answers. There is no local scoring.
- **Monthly cancel:** the installed Razorpay SDK receives the correct boolean argument for
  end-of-cycle cancellation. A rejected request counts as confirmed only when a subsequent
  provider fetch identifies the same subscription as cancelled/completed. Otherwise the
  API returns an honest failure. Existing paid expiry and one-time buyer access remain intact.
  The monthly plan ID is absent, so monthly activation and provider acceptance remain gated.
- **Peak hardening:** actually seeing the Lab's next-move step latches the celebration request.
  It survives a retargeted flight/step change until Pip is settled and visible. A nod cannot
  overwrite it; the once-per-page peak survives reduced-motion toggling.

Source map: `data/study_progress.js`, `data/mistake_replay.js`, `data/session_draft.js`,
`src/components/{LearningNextAction,MistakeReplay,RecoveryOverview,InstallPractice}.jsx`,
`src/lib/server/{learning,practiceSessions,recoverySessions}.js`,
`src/app/api/recovery/replay/route.js`, `src/app/(app)/{dashboard,test}/`,
`src/components/AuthProvider.jsx`, `src/app/manifest.js`, `public/{sw.js,offline.html,pwa/}`,
`src/lib/payments/cancel.js`, `src/app/api/billing/cancel/route.js`, and the Lab/guide components.

## Local server recovery

Use `npm.cmd run dev -- --port 3010`; the user-facing site is `http://localhost:3010/`.
The final server runs Turbopack. Development output is isolated in `.next-dev`; production
builds use `.next`. Turbopack filesystem caching for development is disabled after repeated
cache/worker/chunk failures. `.gitignore`, ESLint ignores and the existing launch configuration
match that setup. No cache deletion, reset or bulk revert was performed.
The default bottom-left Next.js dev indicator intercepted the phone Today dock link in the
live browser. It is now disabled with the documented `devIndicators: false` option; runtime
and build errors still surface. This configuration affects development only.

Earlier sandboxed PostCSS worker IPC failed; a later persistent-cache error and transient
Webpack chunk errors are retained in logs. Separating output prevented build/dev contention,
and the final Turbopack setup passed the browser matrix and real signed-in navigation. It is
not claimed that one root cause explains every earlier failure. A separate production server
on 3011 was used for checks, not as the user-facing dev URL.

## Actual verification

Evidence: `artifacts/round5-completion/`, with final command logs under `logs/`.

- Final lint and production build passed. All data tests plus the recovery safety, evidence
  pipeline and source adapter suites passed: **172 tests, zero failures**. This includes the
  existing question/payment suites, two station tests and eight follow-up contract tests.
- Full route matrix passed **760 loads**: 38 routes × 10 sizes × two themes, using 380 public
  production cases and 380 explicitly labelled development fixtures. Zero root overflow,
  pageerrors, failed loads or broken loaded images. The earlier output-isolation failure
  remains archived separately; it is not included as passing evidence.
- New-state fixture coverage checks five widths, both themes, recorded Tonight state,
  available/unavailable replay and milestones. Offline fixtures submit through the real
  mobile palette, reconnect and reload with the same session ID, deadline and answers.
  These mocked API checks do not write to an account or prove live persistence.
- **37 acceptance checks** passed: real wheel travel forward/reverse across seven perches
  at 390/1280, visible control/focus-ring clearance, static reduced motion at both widths,
  six new fixture views at 200% text, and iPhone install-help/touch-target emulation.
  A first overlap assertion used the un-clipped rectangle of an off-track carousel card.
  The actual track ends at x=1100 and Pip starts at x=1106 at 1280; the card is clipped.
  The assertion now intersects ancestor scrollports and allows five pixels for focus rings.
  This was a harness correction, not a carousel product regression or CSS workaround.
- Final rebuilt homepage: **20 size/theme checks** passed, seven stations, no overflow or
  pageerrors, and the measured hero lead animation remains `none`.
- Production PWA check passed: manifest/icons, worker revalidation headers, exactly three
  public cache entries, account API failure offline and the honest navigation fallback.
- Earlier production performance, touch and quarter-interval journey evidence remains in
  `ROUND5-NOTES.md`; the new follow-ups did not change the measured homepage travel layout.
  These are laboratory/emulation results, not field Core Web Vitals or physical-device QA.

The final isolated rerun passed **43 checks**: two autoplay peaks (one per page, desktop and
phone), 40 new-state size/theme checks, and the offline submission/reconnect/reload contract.
An earlier run alongside other browser harnesses stayed at a paused replay bar and timed out;
the unchanged sequential rerun passed. That failure is preserved in
`logs/browser-final-first.log` and `failed-autoplay-first.png`. The timing/background cause
was not independently isolated, so the failed run is not silently discarded or presented as
passing. `logs/browser-final.log` records the successful final run.

## Live-account observation and remaining gates

The in-app browser already had the owner's authenticated session. Today loaded a real
20-minute plan and its link opened Practice with Quick Practice/count 20 selected. Account
showed fixed Pro expiry with no recurring subscription cancel control. Existing Result and
Review loaded; the inspected May attempt correctly identifies legacy browser scoring and
does not qualify for replay/recovery evidence. Seven existing attempts remained unchanged.
No session was started, no answer was submitted and no debit/score was added to this personal
account. This is read-only local UI evidence, not staging end-to-end submission evidence.
`artifacts/round5-completion/site-ready.png` is the actual signed-in Today view after restoring
navigation. The user-facing development server remains running; the temporary production
verification server was stopped after checks.

Opera/native-app access was not exposed. The existing sign-in made an OTP unnecessary;
Gmail was not opened and no authentication code or credentials were retrieved.

Outstanding external acceptance: approved staging target/test workflow, live server persistence
and resume, premium NTA submission with both skins, Razorpay sandbox subscription/cancel/
webhook reconciliation after the monthly plan ID exists, physical budget Android/iPhone,
and screen-reader acceptance. Current content evidence/calibration release gates remain
unchanged. No deployment or production migration has occurred.

## Skills and reversibility

The Round 5 skill matrix records Scroll Craft, Emil, Apple, prototype and frontend decisions.
This continuation applies mobile-native to install/resume feedback, break-ui to new-state
stress checks, Emil's quiet study surfaces to static milestones, and existing Apple/glass
tokens with opaque fallbacks. No extra UI dependency or replacement identity was introduced.
Original Pip assets remain sufficient; the previously generated GPT concept stays an archived
study. The exposed image tool cannot select an exact GPT Image 2.5 version. No email feature
was in this plan and no external messages were sent.

Rollback should be scoped to these new components/helpers, preserving surrounding owner
edits. If removing install support from an already served origin, unregister its worker and
delete only `mockmob-public-fallback-*` caches; removing registration alone leaves existing
workers installed. They contain public assets only. No migration rollback is needed for this
follow-up. Existing billing, scoring and atomic credit RPCs remain authoritative.
