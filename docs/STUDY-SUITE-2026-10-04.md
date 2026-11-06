# Connected preparation suite — first release

## Released scope

Mocks retain their existing session builder, eligibility checks, credit quote and payment entitlements. The study layer adds Learn, scheduled Recall, durable study runs, shared Today recommendations, separate reading/recall progress, Free preferences and Pro weekly planning/custom mixed revision. Mobile navigation is Today, Practice, Learn and Review, with the existing destinations in More. New study screens advance only after student actions.

The current content release is **21 lessons and 86 cards**, with partial lesson coverage in **15 of 54 mapped chapters**. The initial two-unit release grew to fourteen through Learn v2, then seven source-linked packets added Planning, Staffing, Directing, Money & Banking, Government Budget, Share Capital and Accounting Ratios. The four-subject syllabus map keeps publication gaps visible; 2027 specifications remain provisional. This release does not claim full four-subject coverage or comparative learning superiority. Maintenance workflow: `STUDY-CONTENT-WORKFLOW.md`.

## Content and integrity

- `data/study/pilot.json`, `sources/registry.json` and `release.json` bind versioned units/cards to permitted references and canonical hashes. WordNet 3.0 excerpts retain their complete license. NCERT factual formulas are referenced; teaching prose and examples are authored separately.
- Run `node scripts/learning/study-ratio-source-check.mjs`, `validate-study-pilot.mjs`, `build-study-import.mjs`, `study-current-project-smoke.mjs`, then `study-schema-dry-run.mjs` from the checkout. The ratio check needs the ignored source PDF at `data/study/sources/ncert-retirement.pdf`; its URL and digest are in the source registry. These checks make no provider calls. They verify source reconciliation, arithmetic, contracts, hash bindings and database behavior; they do not constitute independent academic calibration or exam-fit evidence.
- Same-version content imports are insert-only and reject hash differences. Corrections invalidate affected study claims. Append-only events retain original retry results; event, run revision and scheduling commit together.
- `ts-fsrs@5.4.2` runs on the server with default parameters and 0.90 desired retention. This is a scheduler target, not an outcome promise. Default five new cards per IST day; over twenty overdue current cards pauses new introductions. Withdrawn/superseded cards do not create an invisible backlog. Three lapses recommend a lesson without diagnosing a reasoning error.
- Teaching/card families are recorded as exposures and excluded from reserved fresh assessment families. Reading and self-ratings do not certify mastery, repair or score recovery. The separate formal source registry/pathway gates remain closed where evidence is absent.
- No paid AI was called during implementation. Existing Free/Pro prices, 10/50 monthly AI allowances, $50 lifetime generation ceiling, $25 IST-month runtime ceiling and atomic credit RPCs are unchanged.

## Database and deployment

The owner explicitly selected the current project `isrxrxzjocewrdureyhp`, containing existing data, instead of a separate staging project. Saved migrations and local dry-run reports preceded SQL-editor application. The initial three-migration transaction checked that questions, attempts, credits, entitlements and credit receipts remained unchanged. A fourth migration scopes the overdue guard to current published versions. All six study tables use RLS and explicit service-role grants; browser roles cannot read them directly. Application routes authenticate the owner on the server.

Applied files:

1. `20261001105920_score_recovery_foundations.sql`
2. `20261002120000_connected_learning.sql`
3. `20261004154217_connected_study_suite.sql`
4. `20261004172214_study_review_backlog.sql`

The signed-in SQL editor was used because the available service key is not a migration connection. **Supabase CLI migration history has not been reconciled.** Check actual schema and these receipts before any later `db push`; do not blindly apply the old pending files again.

Production rollout is controlled independently by `STUDY_CONTENT_ENABLED`, `STUDY_RECALL_ENABLED` and `STUDY_GUIDED_PLAN_ENABLED`. All three were saved as `true` for the verified Vercel `mockmob` project serving `www.mockmob.in`. They take effect on a new deployment. Rollback sets the flags to `false` and redeploys; retain the tables/events and existing learning/credit infrastructure. Content withdrawal can independently quarantine a unit. Runtime app rendering uses the installed Next.js 16 `connection()` API.

The isolated release checkout at `artifacts/study-suite/release` contains the preparation change without the owner's unfinished provider, pricing, payment-script, landing or AI-evaluation edits. Local `.env.local`, reference downloads and credentials remain ignored. Do not reset or merge over the original dirty checkout.

## Verification and remaining gates

The clean release passed lint, production build, 35 recovery tests, 80 learning tests, six answer-integrity tests, 22 NTA selector tests, 12 payment-entitlement tests and 11 study tests: **166 distinct tests**. Additional repeated wallet/billing checks also passed. The final plan change passed the study suite again. PGlite exercised the complete four-migration transaction, idempotent two-unit/23-card import and service-role run transactions. Current-project smoke verified start/retry, exact recorded event retries, scheduling and stale revisions inside a transaction that rolled back all verification writes. Anonymous study-table access returned 401; canonical released hashes matched.

Authenticated browser checks saved an English lesson, resumed its second step after reload and completed its unscored knowledge check. Saved time preferences survived reload and were restored to the original twenty minutes. Recall reveal/grading, resumed scheduling and final responsive checks are recorded in the release receipt as they complete. These owner QA actions are not student outcome evidence.

Earlier fixture checks covered keyboard reveal/grading, heading focus, spelling-answer withholding and explicit feedback. Browser viewport checks at 320, 390, 768, 1024 and 1440 pixels plus short landscape found no root overflow and no study buttons below 44px in the inspected light/dark states. Dev fixtures are labelled illustrative and blocked in production.

Still required: real budget Android with keyboard open, physical assistive technology, actual 200% browser text/zoom and OS reduced-motion checks, controlled performance lab/field CWV, unseen-question learning outcomes with adequate samples, formal source/calibration expansion and CLI history reconciliation. Online interruption recovery is included; downloadable offline packs follow only after online correctness. Content expansion to the remaining concepts/chapters must pass the same versioned source/content gates. Existing consent/privacy and recovery pilot sample thresholds remain authoritative.

Local evidence is in `artifacts/study-suite/`: migration/content receipts, rollback smoke, schema dry run, release build/lint/test logs, responsive results and screenshots. Production deployment status and actual live smoke belong in `STATUS.md`; a local build is not proof of publication.

## Content v2 and the connected loop (5 October 2026)

Learn is now organised around one loop per concept: Learn → Lock it in → Apply. Authored sources live in
`data/study/authored/*.mjs`; `node scripts/learning/build-study-content.mjs` writes `pilot.json` and WordNet
excerpts; `node scripts/learning/validate-study-content.mjs --write --strict` writes `release.json` (needs the
git-ignored NCERT PDFs and `data/study/sources/dict`; without them NCERT/vocabulary units quarantine);
`node scripts/learning/study-content-v2-import.mjs` writes and dry-runs the two-phase SQL; production uses
`apply-study-content-v2.mjs insert|supersede|verify` against the authorised project only. Coverage, verification
and rollback: STATUS.md, 5 October entry.

## Source-linked expansion and clearer recall (5 October 2026)

- New students finish a current lesson before its new cards enter the queue. Existing current-version reviews keep their schedules. A corrected run returns safe replacement navigation instead of an unrecoverable error.
- Recall uses a contained card surface, explicit answer/reveal controls and two large assistance choices. Selected subject tiles retain semantic keyboard-operable inputs. Next buttons name the next reading activity or quick check. Reduced-motion CSS disables the reveal transition.
- Pro mixed revision opens the returned run directly, selects learned concepts and respects the 20-concept limit. Results expose all matching lessons. Reading, recall and exam marks remain separate.
- Published chapter summaries contain teaching blocks only and record exposure without completing lessons. They offer browser printing/PDF saving. Print layout is implemented; actual printed output is a separate verification gate.
- Optional help uses the current owner-bound run/step, validated before reservation. It sees current published teaching or revealed feedback, not future answers or unrelated student history. One existing PrepOS credit buys an explanation; a saved same-step reply can be replayed without another call/charge. Free static learning and recall remain usable when AI is unavailable.
- A single source-linked packet compiles teaching, checks, recall variants and summaries. `npm run study:prepare` validates and produces digest-bound SQL/dry-run receipts. Skipping PDF checks cannot publish. Source changes and same-version content changes are refused. The seven new units used zero paid content-generation calls; one guarded owner tutor QA call cost $0.00032835 and committed one credit.
- Existing Android/offline work is preserved. This change does not rebuild it or claim new real-device/offline evidence. Remaining coverage and device/performance/outcome gates are recorded in STATUS.md.
