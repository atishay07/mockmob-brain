# Question factory execution

The default worker now runs usable coverage → focused cached excerpts → GPT-6 Luna authoring → blind Luna solution and independent Gemini challenge → explanation audit → automatic inspection → atomic publication → refreshed coverage. Original practice does not require a PYQ anchor. Authentic PYQ labels still require authenticated, immutable paper/key provenance.

The official 2026 baseline is provisional for 2027: 50 questions, 60 minutes, +5/−1/0 and raw maximum 250. English stimuli are capped at 300 words. Accountancy campaigns choose the financial-analysis or computerized alternative branch and retain the common units.

On 7 October the original 100-candidate batch finished with 50 approved and 50 withheld, gross batch cost $0.515798. All 50 are published in staging and the production database. Production student retrieval still requires the deployed current registry and the existing signing secret in Vercel Production. These counts do not include pending continuation cohorts.

The owner-authorized continuation uses fixed cohorts of 100 (25 per subject), actual usable staging inventory, source-section and lexical-target avoidance, exact quote selection for new authoring, and the unchanged independent academic gates. Four cohorts may process concurrently under one exclusive scheduler. Every request uses the same persistent $50 lifetime ledger. Completed cohorts with unresolved bounded receipt holds do not occupy provider-processing slots, but cannot be reported as settled or completed delivery.

```powershell
node --use-system-ca scripts/pipeline/tools/continueCoverageCohorts.mjs --staging --approved-production
node --use-system-ca scripts/pipeline/tools/acceptedBatchStatus.mjs
node --use-system-ca scripts/pipeline/tools/exportContinuation.mjs --staging
node --use-system-ca scripts/pipeline/tools/checkContinuationRetrieval.mjs --staging --minimum 500
```

Resume the scheduler using the retained ledger and `artifacts/question-factory/continuation-500/state.json`; do not prepare or regenerate an existing campaign. The actual source captures, source cache, artifacts and private ledger must be retained together. Accepted provider IDs are collected after restart. A failed OpenAI batch row is collected from its error file: typed pre-inference rejections have provider-backed zero inference cost, failed responses with usage are charged, and unknown server failures retain their full conservative maximum.

The continuation export contains every registered candidate, complete/pending status, answers, explanations, exact supporting excerpts, validation results, reasons, item costs and deduplicated request receipts. Its cost comparison uses all completed cohorts under the current author contract, rather than selecting the best yield. Partial approvals do not establish final unit costs. Provider usage receipts are distinct from invoices.

Add `--realtime-checks` to the scheduler to use real-time Luna for unsent blind checks, repairs and explanation audits while keeping authoring and Gemini on native batch pricing. This is the Luna checking mode used in the frozen benchmark. Already accepted IDs retain their original execution mode and are collected, never replaced. The more expensive checking rates are included in each actual item receipt and gross cohort comparison.

The explicit `--approved-production` scheduler flag publishes completed, inspected subsets to the pinned production database under the owner's 7 October authorization. Application deployment and signing configuration are separate and must be verified before calling them available to students. A terminal failed call on a quarantined candidate can retain a proven maximum hold while unaffected approved items publish; all pending calls, uncertain checks on approved items, unknown acceptance and unbounded holds still block. Costs with any holds remain unsettled.

For an explicitly owner-approved production subset, after a complete cohort, current inspection and bounded terminal accounting:

```powershell
node --use-system-ca scripts/pipeline/tools/publishProductionCohort.mjs artifacts/question-factory/COHORT --approved-production
node --use-system-ca scripts/pipeline/tools/checkContinuationRetrieval.mjs --approved-production --base https://YOUR-VERIFIED-PRODUCTION-DOMAIN --minimum 500
```

The production publisher pins the production project identity, reuses the existing admin, retains idempotent publication receipts, and leaves production generation paused. It never applies staging bootstrap migrations. The retrieval command checks existing identities without emails or new roles; it fails if published questions are unavailable to the deployed application.

The 19 criteria are defined in `data/question_factory_criteria.mjs`. Sixteen mandatory gates cannot be offset by craft scores. Both independent judgments must give overall craft 7–10 after mandatory success. Individual clarity, distractor and difficulty scores remain visible. A candidate receives at most one targeted repair; its changed content starts validation again. An unresolved defect is quarantined. No routine human approval is required.

The local SQLite ledger is the only content budget authority. Back up `data/pipeline-budget.sqlite` and its runtime files securely outside Git. It retains settled usage, reasoning-inclusive output, failed calls, accepted provider IDs, repairs and conservative maximum holds under the $50 lifetime cap. An unknown call is never assumed free or reposted. Only a proven bounded hold permits unrelated continuation; an unbounded hold still blocks. Student AI remains a separate $25 per IST month database contract.

Run these commands from the repository root in PowerShell:

```powershell
npm.cmd run factory:staging-app
```

That app uses ignored `.env.staging`, isolates its Next.js build at `.next-staging`, serves port 3101 and disables paid student/payment/email provider keys. It refuses the production Supabase identity. The original app process is separate.

```powershell
npm.cmd run factory:focused -- reconcile
npm.cmd run factory:focused -- generate
npm.cmd run factory:focused -- validate --realtime-luna
npm.cmd run factory:focused -- report
npm.cmd run factory:focused -- inspect
npm.cmd run factory:focused -- publish --staging
```

These resume the existing preregistration. A pending accepted ID is collected, never submitted again. `--realtime-luna` uses real-time Luna validation, audit and bounded completion/repair while keeping Gemini's native batch pricing. The initial 100-candidate authoring request was explicitly submitted through native OpenAI batch pricing. Prices and every execution mode are saved per receipt.

```powershell
npm.cmd run autonomous -- --staging --realtime-luna
```

The worker reads signed-in admin pause/resume controls, collects receipts while paused, synchronizes progress, validates only the registered campaign, and automatically inspects a completed cohort. Publication additionally requires staging publication to be enabled. It retains a permanent host/ledger identity and a process lease. A second process cannot claim a live lease; a dead process is recoverable without duplicating requests. Pending provider status snapshots expire so the worker can observe completion.

For a later separately authorized campaign, prepare actual staging coverage without overwriting this run:

```powershell
node --use-system-ca scripts/pipeline/tools/prepareCoverageCampaign.mjs next-campaign-name --staging
node --use-system-ca scripts/pipeline/tools/focusedFactory.mjs worker --staging --realtime-luna --campaign-dir artifacts/question-factory/next-campaign-name
```

Add `--computerized` to the preparation command to choose that Accountancy branch. New campaigns reuse a dated completed benchmark only while the source and verification contracts still match; reuse is never called fresh reliability evidence. Official topic gaps remain open when the two validated topic tags cannot be assigned unambiguously. Local document ranking helps retrieval and never proves answer support.

The current artifacts are in `artifacts/question-factory/execution-2026-10-07`: full 100-item JSON/CSV, approved questions and full approved records, rejected records, exact excerpts, validation checks, receipts, batch economics, inspection, coverage and staging proof. `validation-summary.json` separates fresh benchmark cost from all failed/preparation attempts and states the small-sample limitation. Provider response usage is distinct from invoices; open holds stay explicit.

The completed cohort contains 50 approved questions and 50 withheld questions. All 50 are published and retrievable in separate staging; production has zero new publications. Gross cohort cost is $0.515798, or $0.01031596 per approved question. The conditional 10,000-question marginal cost is $103.159600 and lifetime forecast is $109.766661. This does not fit $50–70. The final report records live model misses caught by free inspection; the compact benchmark is not a perfection claim.

Evidence signing uses canonical JSON object ordering so PostgreSQL JSONB round trips preserve trust. Array order and all evidence gates remain binding, legacy signatures remain verifiable, and the serializer is part of the frozen contract. Historical receipts are retained. Worker progress writes use 25-row chunks; finished publications are not repeated on every tick. A new authorized campaign still needs supported sources for its actual gaps.

```powershell
npm.cmd run test:factory
npm.cmd run test:recovery
npm.cmd run test:learning
node --test data/tests/payment_entitlements.test.mjs data/tests/mock_question_selector.test.mjs data/tests/nta_question_selector.test.mjs data/tests/answer_integrity.test.mjs data/tests/practice_quote.test.mjs
npm.cmd run build
node --use-system-ca scripts/pipeline/tools/checkPublishedStaging.mjs
```

The final command requires the completed, published live cohort. It checks actual signed-in student retrieval and temporarily withholds one unchanged approved row to test dispute filtering, then restores its unchanged publication state and retains the explicitly labelled staging-test dispute receipt. Software storage fixtures are separately labelled and excluded from academic yield.

Production remains separate. `production/factory-migration.sql` is an additive transaction with no seeds, promotions, balance edits or receipt deletions. The read-only production preflight confirms prerequisites; apply/deploy/publish only after owner approval. Never apply the empty-staging bootstrap to production.
