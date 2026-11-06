# UI/UX implementation results — 4 October 2026

Core UI implementation is complete locally. This is not a production release or a declaration of whole-site accessibility/performance compliance.

Owner-approved official-key wording remains unchanged. Mobi, volt, both themes, admissions tools, the timed exam, scoring, prices, paid entitlements, atomic credit operations and model/budget routing are preserved. The checkout was already dirty at HEAD `678229d30e9970571f050b747a8174ead358b8eb`; existing author edits and the previously untracked tour were refined without reset, staging or commit.

## Implemented behavior

| Area | Before | After |
|---|---|---|
| Practice loading | Subjects/setup waited for optional statistics and other panels in one Promise.all | Setup waits for subjects/record; optional panels resolve independently. Pending counts say Checking, unavailable counts are labelled; launch still requires the matching server quote |
| Practice hierarchy | Companion and four statistics preceded Subject | Subject/session setup precedes supplementary commentary/statistics. Phone summary shows subject, mode, count, time, marking and quoted cost near Start |
| Practice recovery | Dashboard error retried through a full reload | Scoped data retry preserves valid subject/mode/count; quote matching, expiry check and idempotency remain. A synchronous launch-key guard prevents duplicate launch intent |
| Guest activation | Signup-led primary hero CTA; longer lead pushed sample lower | Guest primary opens the no-signup sample; authenticated destination is preserved. Compact phone composition and lead make the first question and two options visible at 390×844 |
| Result layout | Mascot box inherited a short fixed height; percentage could split as anonymous flex text | Mascot reserves intrinsic height, entrance movement stays within the row gap, metric values do not split and captions wrap |
| Repair outcomes | Held/not-explained outcomes shared Repaired badge/progress with successful explanations | Outcome labels distinguish Explanation ready, Held for review and No explanation. Progress counts explanations; handled questions leave the automatic queue without being counted as repaired |
| Repair continuity | Collapse/filter could unmount the repair, discard state and repeat an automatic request | Only visited answer bodies are populated; they remain mounted while hidden/filtering. Pending/completed/held state and request identity survive those interactions |
| Retry identity | A generic 5xx cleared the request ID; released/in-progress 409 could leave no continuation | Uncertain reply keeps ID; explicit operation_released permits a new retry; in_progress offers Check again using the same ID. In-flight guard prevents overlapping calls; incomplete replies never show a success panel |
| Feature tour | Eight dots plus eight rows on phones; partial tab semantics; Pause did not govern demo timers | Phone previous/next/counter and native picker; desktop selector retained. Complete carousel labels, inactive slides inert, 44px controls, visible focus, focus/manual pause with explicit resume |
| Demo activity | Timelines restarted/settled on pause; countdown could keep ticking; background slide advancement | Bounded elapsed-time scheduler freezes stages/countdown/typewriting while paused/offscreen/hidden, resumes without catch-up, and cancels on unmount. Reduced-motion screens settle. Demo CSS animation follows playback; video follows visibility/playback |
| DU inputs | Small editable type/clear target; category radios lacked keyboard navigation | Phone/tablet editable fields compute to 16px, clear target is 44px and returns focus, category arrows/Home/End use one tab stop. Teaser bar animates transform instead of width |
| Landmarks | Nested main in timed runner/PrepOS | One main, visually identical inner div wrappers |

The result's recommended next repair still uses the existing recorded session analysis. Available explanations are not labelled as learned concepts or observed score gains. Ordinary-practice fallback remains when verified fresh questions are unavailable.

## Actual verification

Evidence directory: `artifacts/ui-ux-implementation-2026-10-04/`.

- Baseline and final production builds passed. Final `npm.cmd run lint` passed.
- 179 automated tests passed: 35 recovery, 80 learning/wallet/monthly-budget/practice-quote, 59 combined payment-entitlement/answer-integrity/NTA/DU, and 5 new playback/outcome/retry-policy tests. Logs are `recovery-tests.log`, `learning-tests.log`, `contracts-tests.log`, `ui-state-tests.log`.
- Final light matrix: home, practice, result, DU at 320/390/768/1440. Final dark matrix: those routes at 320/390/1440. Zero horizontal overflow; result mascot did not overlap metrics; each route exposed one main. Product editable fields at phone/tablet sizes compute to 16px. Development preview's external 12px View selector is excluded from product field conclusions.
- Final matrix JSON: `responsive-final.json`, `responsive-final-dark.json`. Images `*-final-*.jpg` and `*-final-dark-*.jpg` correspond to these checks. Earlier `responsive-night.json` is pre-correction evidence and includes the transient overlap subsequently fixed; use final files for acceptance.
- At 390×844, production homepage question begins around y459; first two option bottoms are around y672/y738, above the phone dock. Guest primary sample CTA and wrong-answer feedback were checked in local development. Production sample correct feedback transferred focus to Next question. Logged-in production-preview CTA retained `/dashboard`.
- Production build served locally on port 3020; public home checked at 390 and desktop, both themes. Existing session caused `/signup` to redirect to the real dashboard; it loaded with authoritative Pro access/quote. No session launched, credit spent, repair model called or account state changed. Current-run native email validation was therefore not repeated; earlier audit evidence is not claimed as a fresh test.
- Browser fixture outcomes: explained/default, stored, held, not explained, insufficient credits, unusable reply, malformed reply, in_progress and released. Held/not-explained showed zero explanations; stored showed one. A held panel stayed held after collapse/filter/reopen and had no repair-start button. Fixtures are illustrative software evidence, never student proof or billing receipts.
- Pause retained exactly the observed practice demo step and clock across subsequent work. Pure scheduler tests additionally cover a 60-second hidden interval without catch-up, bounded completion, repeated resume and cancellation.
- Final keyboard check: Play was focused and playback running; pressing Tab moved focus to the feature picker and stopped playback. Final tour lint and production rebuild passed after this correction; the owned production preview was restarted for the final build.
- DU ArrowRight moved selection/focus UR→OBC-NCL with one tab stop; End moved to EWS. Clear search emptied the field and returned focus. App menu Escape closed it and returned focus to its trigger.
- PrepOS at 390 and timed runner at 320/390 had one main and zero horizontal overflow. Timed runner verification used development fixtures and did not submit an attempt.
- Pending-inventory fixture `?view=dashboard&stats=loading` rendered complete setup and a launchable authoritative quote despite the never-resolving statistics request. This verifies removal of the setup dependency; it is not a measured device speedup.
- Development server logs recorded several inventory requests taking 7.5–11 seconds; production preview also recorded a roughly 9-second inventory read. These are local server request durations, not LCP/INP or real-phone observations. Inventory backend optimization is outside this UI change.
- `git diff --check` found an existing blank line at EOF in owner-edited `ProductScreens.jsx`; no new targeted whitespace defect was reported. The unrelated owner edit was retained.

## Remaining release gates

1. Controlled production-build traces with CPU/network throttling: transferred JavaScript, long tasks, LCP/CLS, controlled input-to-feedback, scroll frame distribution and five comparable samples. Available browser capabilities expose viewport/interaction but no trace/throttling/field-metrics API. No main-thread/INP/frame or before/after performance gain is claimed. Blur, font/image preload and lazy-loading changes were intentionally deferred until measurements identify a cost.
2. Field Core Web Vitals and actual budget Android/iPhone use: touch swipes, keyboard opening, safe areas, background interruption and long-session behavior. Screenshots at phone widths do not replace hardware.
3. Actual 200% text/browser zoom, screen-reader flow, browser-emulated reduced motion and full hover/focus/contrast matrix. Native zoom shortcut did not change the supplied viewport. Current evidence covers responsive reflow, keyboard checks and reduced-motion source/scheduler behavior; it does not claim these missing checks passed.
4. Authenticated persistence/real rapid launch/lost-reply/payment/paid AI receipts in an appropriate controlled environment. Server contract suites passed, but fixture responses do not prove deployed accounting or model behavior. Existing authenticated setup was read-only.
5. Production deployment and live smoke. No deploy or data migration was requested or performed.

No paid model calls, real attempts, outbound messages, signup completion, payment, production migration, pricing/entitlement/budget changes or deployment were performed. The host-side local server/build permission was approved; initial restricted-server/build runs were not used as performance evidence.

## Review and rollback

Review the scoped diff and the current untracked tour/helper/test files. Do not reset this checkout or revert all of `page.js`, `public-polish.css`, `home-refinements.css` or the tour: they contain earlier owner work. Roll back only the implementation-specific hunks in the files described above, including the optional-request split and outcome/retained-body changes. The pure helpers are `data/demo_playback.mjs` and `data/repair_presentation.mjs`; meaningful state tests are `data/tests/ui_ux_state.test.mjs`.

Local preview processes created for this work: development 3010 and production 3020; PID/log files are in the evidence directory. They are local previews, not publications.

## Authorized publication follow-up

Owner subsequently requested publication. UI source and preflight documentation were pushed as
`f70e385909ff454f10bf83e60d96a6883bb31c17`; Vercel production deployment
`6VA6xyZTYuXB87urHXQLAgeusbAx` completed successfully at `2026-10-04T12:50:34Z`.
The exact isolated UI release passed production build, lint and all 179 tests before the push.
Unrelated local model-routing, commerce enablement, pricing/payment and backend-test edits were excluded.

Live `www.mockmob.in` serves the new UI with 200; apex redirects once to www with no loop.
Home light/dark 320/390/1440px smoke found no horizontal overflow and one main. Sample feedback,
native tour feature selection/pause, one active/seven inert slides, 44px tour controls and live
DU arrow navigation/search-clear focus/16px input passed. Captured error logs were empty.
Release evidence is in `artifacts/ui-ux-release-2026-10-04/`. This receipt remains a local record
after publication; earlier no-deploy statements describe the implementation pass before authorization.
Physical-device/CWV/screen-reader/actual-zoom and real accounting gates remain open.
