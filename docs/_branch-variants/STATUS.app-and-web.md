## 6 Nov 2026, about 3:16 am IST — Round 4 release candidate paused

- Production is Round 3, main `400d647a8`, Vercel `dpl_F74Lgyeyodb5YPh2kiK5HTxfiAmT` READY.
- All six Round 4 packets are integrated locally on `web/r4-release` with runtime tip `06aed8557`. Both production builds passed. The final source assertion, browser performance, gesture and visual gates are pending. Private Vercel errors and deployment listing are accessible after the owner's approval.
- The owner stopped the session at 5% usage (LK152). The [release handoff](HANDOFF-2026-11-06-ROUND-4-RELEASE.md) records the exact failures, test and screenshot evidence, worktree state and next steps.

## 14 October 2026, 02:03 IST — current state since 7 October (git logs and handoffs; newer than every section below)

Sources: git logs read on 14 Oct 02:03 IST in mockmob-next, mockmob-hotfix, mockmob-fit, mockmob-backend and mockmob-web2; docs/brain/PENDING-2026-10-14.md; the AI OS handoffs in handoffs/mockmob from 20261013T195956 back to 20261012T174318. Nothing was run, deployed or read from production to write this section. "Live" below rests on a handoff or a push record, not on a fresh probe. The 7 October sections below cover the question factory and the web study suite only; they say nothing about the app, NTA mode or the 12-13 Oct releases.

### Live in production (owner-pushed or owner-approved)

- Security hotfix f31f7ba (12 Oct 22:19): students can no longer grant themselves Pro or read other accounts. Pushed to origin/main by the owner. Handoff 20261012T174318 records the probes afterwards: /api/questions/pending 401, /api/users/x GET and PATCH 401, apex 307 to www, www 200.
- Inventory snapshot for practice quotes and homepage counts e2a9dab (12 Oct 22:44), daily inventory cron cd755e2 (12 Oct 23:01, pushed 13 Oct 01:02 IST), evidence registry read once per pass 52de7fe (13 Oct 01:29, pushed 10:17 IST).
- Sign-in reliability 5f7d53e (13 Oct 13:49): session refresh proxy, cookie-safe server reads, hardened callback and email codes. Deployed by the owner at about 14:00 IST (push 14:02). The owner reported website sign-in "working fine" afterwards (handoff 20261013T083532).
- App backend release 04e99cf and 4bf41b8 (13 Oct 14:36 and 15:01): server routes, modules and migrations for the Android app, plus the per-student finaliser pass. The local reflog of origin/main shows 4bf41b8 pushed 13 Oct 15:08 IST, so it is the origin/main tip. Not verified for this section: that the Vercel deployment is Ready, that PRODUCTION-app-backend-2026-10-13.sql was run, or that CRON_SECRET and ANDROID_CERT_SHA256 are set in Vercel. The handoff left those as owner steps.
- Production question data, owner-approved 13 Oct (HANDOVER-2026-10-13-NIGHT): 325 questions withheld from practice (c1fc654: 279 suspect-key recheck, 34 "only" to "mainly", 15 demo seed rows) and 76 repaired questions put back (96ff500: new key, explanation and wording, 4 of 5 blind solvers agreed, both judges 7 or more). 249 remain withheld: 25 repaired but below 7, 13 unrepairable, 211 others. Restore files are in mockmob-hotfix docs/brain/reports/question-holds/. These were data writes; the code commits c1fc654 and 96ff500 exist only on the local branch fix/nta-mode, not on origin/main.
- Not in production: the Flutter app, NTA mode, the CUET-fit work, the AI reply report endpoint, the web state-aware home and the logo B web icons.

### Local only (not pushed, not deployed)

mockmob-next, branch feat/app-and-web, head b9f296d. Commits since 49f4100 (pass 2 after owner feedback, 13 Oct 19:42), newest first:
- b9f296d (14 Oct 02:00): concept-checks playbook on the record page, PENDING-2026-10-14.md, Play listing and data-safety draft (docs/brain/PLAY-LISTING-2026-10-14.md). 26 files.
- 5098239 (01:25): road ends at the CUET window with no CSAS and plain college captions; home-screen widget, app shortcuts, private share card, review prompt, in-app update; notification re-ask with rotating asks and Open settings; warm-ups for all 15 subjects (handoff: blind-solve verified). 76 files.
- 4d581a1 (00:44): copy sweep with filler lines removed, including "Nothing goes to ad or analytics companies"; NTA inactive grace 3 s (owner decision 14 Oct); NTA intro line. 15 files.
- 2be7a88 (00:27): round 3 fixes for packages 4, 5, 7, 8; router (learn summary, load-failed), Mobi reduced-motion aim, NTA ended card held until Continue, deep links. 128 files.
- 53d676d (13 Oct 23:51): round 3 review fixes for packages 1, 2, 3, 6, 9, 10 and the unit-suite baseline failures. 114 files.
- 6be644d (22:54): web legal pages say Android reminders are local and give the delete path You > Account (src/app/privacy, src/app/account-deletion). Source only.
- 7f14970 (22:45): HANDOVER-2026-10-13-NIGHT.md.
- 5beb81c (22:44): WIP, app round 3 builds and logo B device fixes. 538 files.

Test state of the app: the last full Flutter suite, run on 5beb81c, gave 2181 pass and 219 fail (about 200 golden pixel diffs plus 19 unit failures). The unit failures were fixed in 53d676d. Since then there has been no full-suite run, no golden regeneration, no emulator walk-through of round 3 and no release APK. The origin/feat/app-and-web tracking ref sits at 03eab8a (13 Oct 01:01); the branch is 22 commits ahead of it. The working tree carries other agents' uncommitted edits in flutter_app (launch_flow.dart, practice_start_screen.dart, result_providers.dart, recap_screens.dart) and untracked tmp/; none of that is in the commits above.

mockmob-hotfix, branch fix/nta-mode, head ad2023c (13 Oct 21:50), 15 commits ahead of origin/main as last fetched: NTA paper engine from 053d2a0, agent score merge, key disputes, end-to-end tests for 15 subjects, c1fc654 and 96ff500 (the production data changes above), a404f09 (mark for review saved with the session, device-ticket clock kept, option layout stored), 2c6e5a1 engine r4, ad2023c engine r4.1. The handover records tests passing on this branch; they were not re-run for this section. The last production engine run (e1dbfe8, before r4 and the fit gate) showed 6 of 15 subjects able to build a paper, and the expert verdict was not ready. NTA stays undeployed until the fit merge is done and an expert re-reads the papers. The working tree has modified logs/audit/route_* files.

mockmob-fit, branch wip/cuet-fit, head 9471097 (14 Oct 01:37), on 7848577 (13 Oct 22:44, partial gate) on ad2023c: CUET-fit merge into the engine (fit gate, stored type first, recency so a newer 8 beats an older 9, fixtures with three fit judges per row, new nta_fit_gate tests added to test:nta). The commit message says the tables were re-merged from the 676 judge files present, so scoring is partial. The 14 Oct missing-pairs list holds 383 entries (mockmob-hotfix tmp/nta-pass/fit/missing-pairs-2026-10-14.json); the results folder held 790 files at 02:03 IST with workflow wf_547f7cf8 still running. The commit message reports no test result and none was run for this section.

mockmob-backend, branch feat/ai-reply-report, head ff23016 (14 Oct 01:29): POST /api/ai/mentor/report (bearer-authenticated, rate limited, validated, write-only), migration 20261014090000_ai_reply_reports.sql (ai_reply_reports table, RLS on, per-student dedupe), test data/tests/ai_reply_report.test.mjs. The migration is not applied anywhere, so the app's "Report this reply" key gets a 404 until the route is deployed. The same worktree also has branch sec-tests at 4bf41b8, equal to origin/main.

mockmob-web2, branch fix/web-state-home, head 613235c (14 Oct 01:30), 4 commits ahead of origin/main as last fetched: 5d79433, 6e68228, 1dc44b9 (state-aware home page and test-screen notices, with the owner's decisions) and 613235c (favicon, icons, header logo and share image switched to logo B). Never checked in a browser at 375 px or 1024 px. Untracked .next-staging/ and tmp/ present.

### Owner decisions on record (14 Oct)

From handoff 20261013T185818 and PENDING-2026-10-14.md: NTA inactive grace 3 s for brief interruptions such as the shade or a call overlay; switching to another app counts at once; three warnings stay; FLAG_SECURE in NTA mode only; study days kept on the phone; the notification pre-prompt may return with different wording; filler lines such as "Nothing goes to ad or analytics companies" removed. Relay: the 13 Oct 22:50 handover says it stays off; the newer handoff 20261013T195636 says the owner wanted it on, with a watcher started (pid 35144) and a 98% threshold. The newer record wins.

### Still open (full list in PENDING-2026-10-14.md)

- App round 3 close-out: full suite folder by folder, golden regeneration and viewing, remaining P2/P3 test gaps, emulator walk-through, release build with dart_defines/prod.json (GOOGLE_WEB_CLIENT_ID is empty; no upload keystore exists in the repo).
- Owner decisions: recap back target, CSAS end date for the road and registration window, the label "NTA mode, with Pro", sign-out deleting unsent drafts, question-view event policy, logo A or B, relay overnight, NTA clean-up holds (12 corrupted-connective questions and 63 listed-order keys, tmp/nta-review-cleanup/CLEANUP-2026-10-13.md), short papers, Razorpay Rs 99 monthly plan, crash reporting, quiet hours, fate of the 249 withheld questions.
- Owner-only: Play Console app and forms, upload key, Vercel and Supabase dashboard steps, every deploy and production SQL, the production NTA engine run, and the evidence expiry between 5 Nov 2026 22:41 UTC and 6 Nov 2026 14:57 UTC for the 662 scored factory questions.
- Budget (unchanged): content generation USD 50 lifetime, student AI USD 25 per IST month. The last ledger figure is USD 13.10 committed on 7 Oct and has not been reconciled since. This section authorizes no paid call.

## 7 October 2026, 14:22 UTC — 575 verified production retrievals and current accounting

Owner-corrected signing configuration redeployed as GnJ42mkLjHXgbwUs4SvPY6oSWgpD (c235606), Ready/Latest in 77 seconds. The actual production student check passed at 14:12:38: 575/575 unique new approved questions retrieved, ten complete passage groups, zero rejected IDs, unchanged USD 25 student-AI monthly cap. The authenticated rendered dashboard confirms 575 usable / 579 historical publication records, four withheld, and after a metadata-only accounting refresh shows USD 12.82 settled + USD 0.28 held and a USD 92.76 conditional lifetime forecast. That refresh preserves paused=true, phase=1000 and publication_enabled=false, and changes no questions, payments or student budgets; its receipts are in production-accounting-sync.json/.jsonl. Export refreshes now maintain this snapshot when production publication was explicitly authorized.

The retained ledger at 14:22:16 is USD 12.824160 settled + USD 0.276446 held = USD 13.100606 committed, 7,146 requests. Sixteen accepted candidates remain submitted; five historical/terminal-failure requests remain unresolved and retain their USD 0.090248 maximum holds. Provider invoices remain unavailable. Eight completed cohorts retain 800 candidates, 575 usable approvals and USD 4.860017 gross; the current author contract's three complete cohorts retain 300 candidates, 250 approvals and USD 2.108597 gross. Current overall craft distribution remains 233 seven, 341 eight, one nine, zero ten; this is a mixed bank, not a uniformly premium or perfect bank.

Stricter craft-filter scenarios retain all 800 completed candidates and their USD 4.860017 gross costs. Overall scores of at least eight select 342 questions, USD 0.014211 per selected question and a conditional lifetime 10,000 cost of USD 150.346349. Requiring an overall score of at least eight plus every individual craft subscore of at least seven selects 160, USD 0.030375 per selected question and USD 311.991652 conditional lifetime cost. These are observed rating filters, not accuracy or premium-quality proof. The mixed-bank USD 92.762624 forecast cannot substantiate a uniformly premium bank under USD 100. The automated report includes these distinctions and preserves all rejected and failed-call costs.

Staging repeated statement timeouts (57014) on large status upserts and snapshot reads. Sync writes now use byte-bounded chunks while preserving every evidence byte; full snapshot reads keep their usual pagination and retry a timed-out evidence-heavy page once at 100 rows with the same offset. Metadata errors and further failures still fail closed. Four targeted byte/boundary/error tests pass; full factory/snapshot tests 335, recovery 39, question/payment/wallet/ticket 65 pass, with the earlier application-learning 84 retained as dated evidence. Controller 59386 resumed the same accepted campaigns; no new cohort or paid evaluation was registered. Paid IDs, reservations and evidence gates remain intact. Production availability is established; the combined 1,000-candidate campaign is still incomplete while the last 16 provider candidates finish.

## 7 October 2026, 13:31 UTC — production signing key and request-scoped evidence checks

The owner saved CUET_EVIDENCE_SIGNING_KEY as a Vercel Production Secret. Redeployment 2S7jeLumVt3bf59yBrJ5JTUmmUXs of e9e1ffb is Ready (53 seconds). Public endpoints return 200; anonymous admin returns 401. The authenticated overview timed out at 30 and 90 seconds and remains unverified. It was reparsing approximately 4.85 MB of registry/calibration JSON per inventory row (9,821 production rows). The overview now binds one fresh registry/calibration snapshot per request; item signatures, content hashes, source versions, expiry, disputes and release predicates are still independently evaluated, with no cached item verdict. Real 575 approved records remain eligible in 0.297 seconds locally; sampled existing-path verdicts match. Factory plus snapshot safety tests pass 331, recovery 39, question/payment/wallet/ticket 65; the release build passes. Production retrieval is to be rerun after this optimization deploys. Native provider IDs, remaining 19 candidates, all costs/holds and the running controller remain intact. No new paid evaluations, production migrations or payment changes.

## 7 October 2026, 12:52 UTC — native Gemini failure receipts preserve holds without publication deadlock

The accepted 64-item Gemini validation batch succeeded at the provider level; 60 usage receipts settled and four item records reported native code 14, service unavailable, with no usage. The four $0.019788 reservations remain fully committed ($0.079152 total), and all four corresponding candidates are quarantined. The transport now retains each exact native metadata key, batch identity, terminal state and error record. Cohort accounting recognizes only matching terminal failures on quarantined items as bounded receipt holds, so unrelated approved questions can publish once their pending work finishes. A failed call with reported usage is charged for its candidate plus reasoning tokens; no service failure is assumed free. Missing/duplicate identities, a running batch, missing failure evidence, invalid bounds or an approved failed item still block publication.

The fix passed 28 targeted receipt/restart/identity/budget/publication tests, all 328 factory tests and the full release build. It was applied atomically after preserving the old files; the existing controller and active paid calls were left running. Actual SQLite proof at 12:51:38 UTC verifies all four native keys, terminal errors, unchanged full holds and quarantined item states. The academic generation/validation contract is unchanged; no repeated paid evaluation or accepted-ID resubmission was introduced. Two OpenAI batches and later repair-validation work remain pending; the controller must finish them before the combined campaign is called complete. Production signing-key entry and the historical 503 receipt remain external dependencies.

## 7 October 2026, 12:22 UTC — 575 actual staging retrievals and deployed currency correction

The signed-in staging student check at 12:15:53 UTC retrieved all 575 current approved questions: English 149, Accountancy 123, Business Studies 159 and Economics 144. Ten passage groups were complete; no rejected item was retrieved. The authenticated admin overview distinguishes 579 retained publication records from 575 currently usable factory items. Funded checkpoint replay, the unfunded 10,000 checkpoint rejection and the existing $25 student-AI monthly cap passed. This is actual API evidence; it does not replace a current rendered dashboard inspection.

The serving guard now preserves the sign in grouped rupee amounts, including Indian grouping, while rejecting mathematically equal options such as ₹3,00,000 and ₹300000. This corrected a false positive on one independently validated Economics item without changing its key, explanation or academic evidence. Fractional signed scalars are also covered. Question/selector/payment/wallet/ticket checks pass 65, factory 324, recovery 39 and the release build passes. Vercel shows production commit 4a9c002e7ce957d78715c409f0ec45f7d5ce3cca Ready/Latest, deployment Fr8c2aHmfwxtzqjXF1inXovKTdSm, 57 seconds. The frozen academic contract remains byte-identical to the release checkout: d80135b0271f350a1864c9d107b078f07fbefa54419c4615a8891aa096308399.

The existing controller was restarted only after two independent child-empty checks to reload the guard. Restart evidence retains all 7,047 prior ledger requests and 2,438 stored accepted provider IDs, with zero missing IDs and no replay calls. The resumed controller reports 575 usable items and 83 pending candidates in the two already registered later cohorts; no further cohort was registered. Eight complete fixed cohorts preserve their entire 800-candidate denominator, 575 approvals and $4.860017 gross cost. At the dated 12:15:30 snapshot, lifetime settled usage is $12.521966, holds $1.378190, committed $13.900156; the conditional lifetime 10,000 forecast is $93.562174 across all completed cohorts and $93.394263 for all completed current-author-contract cohorts. Neither a uniformly premium bank nor a $50–70 forecast is established. These are usage receipts and conservative holds, not provider invoices.

Additional application/learning verification completed at 12:32 UTC: 84/84 existing tests pass. They exercise the production-shaped monthly AI budget migrations, conservative missing-usage accounting, duplicate dispatch suppression, credit reserve/commit/refund lifecycle and historical payment-plan resolution. These are local database and application checks, not a captured production payment or live student-provider claim. The report retains exact commands, test counts and log hashes in continuation-500/local-verification.json and includes them automatically in future exports.

Production student availability remains unverified while the owner-controlled CUET_EVIDENCE_SIGNING_KEY form awaits entry and submission; storage receipts and a Ready deployment do not establish availability. The browser credential rule requires the owner to complete that step. The historical OpenAI 503 request remains conservatively held at $0.011096; the read-only billing lookup encountered an authentication failure, and no zero-cost assumption or resubmission was made. The accepted native batches remain under the persistent controller for completion, export and final retrieval checks.

## 7 October 2026, 10:15 UTC — current usable admin counts and lifetime forecast

The actual staging check at 10:12:30 UTC passes 491/491 current approved questions, ten complete passage groups, and zero rejected items retrieved. The authenticated overview now separates 495 retained publication records from 491 currently usable factory questions. All four withheld historical publications remain stored and unavailable. The admin headline, subject counters and checkpoint gates use the intersection of current usable coverage with new factory publication IDs; unrelated legacy inventory cannot fill these checkpoints. The lifetime forecast includes existing committed spending and conservative holds once, rather than showing only marginal cost for 10k.

Four targeted count/forecast tests cover retained withholding, legacy exclusion, an insufficient 999-usable/1000-historical checkpoint, and absent cost evidence. Factory passes 324; the full release build passes. Recovery 39 and scoped question/payment/wallet/ticket 64 remain passing. At the dated aggregate snapshot 10:06:44 UTC, seven completed cohorts retain all 700 candidates, with 491 usable approvals and $4.128471 gross. Lifetime settled is $11.398041 and conservative reservations $0.782782, committed $12.180823. Conditional lifetime 10k is $92.135264 across all completed cohorts; uniform premium quality and a $50–70 fit are not established.

The accepted native batches are still processing (99/100, 98/100 and 0/7 in the latest direct read). Their output files are not available yet, so partial provider counters cannot be collected as completed questions or settled receipts. All accepted IDs remain retained; no paid regeneration or accepted-request resubmission was introduced. Production signing-key entry and the historical 503 billing receipt remain precise external dependencies.

## 7 October 2026, 10:04 UTC — unsupported antonym explanation withheld

The actual supplied dictionary span does not entail the generated rule that an antonym 'must oppose both qualities'. Both independent model checks and the explanation audit passed that unsupported claim. The publication inspection now rejects it automatically, and the already published item abb793b3de99185acb169170f420b335 has been withheld in both authorized environments with content, provider costs and prior publication history retained. This is an observed validator miss and dated regression evidence; it is not a fresh benchmark success or proof of general accuracy. The three duplicate passage children remain withheld. Cohort 007 now has 78 approvals and 22 rejections, preserving its full 100-candidate denominator and $0.681212 settled gross cost.

Inspection contract evidence-content-idea-inspection-v3 binds publication reuse to these current guards and unchanged content. The frozen academic model contract remains d80135b0271f350a1864c9d107b078f07fbefa54419c4615a8891aa096308399. Factory passes 320 tests; recovery 39 and scoped answer/selector/payment/wallet/ticket checks 64 remain passing. Actual staging retrieval passed 492/492 at 09:55 before this additional withholding, so that proof is dated; the updated usable count must exclude this item. Remaining native requests are retained, and no fresh paid benchmark or uncontrolled regeneration was run.

## 7 October 2026, 09:50 UTC — actual novelty withholding and serving guard corrections

Vercel reports production 224e63a1ad3928f592f945d88be1b3ae351a7510 Ready (53 seconds). The retained seven completed cohorts originally approved 495 candidates. A new automatic passage-fact check found three children of the same passage group asking the same factual condition, despite differing concept labels. All three are now withheld in staging and approved production through retained dispute receipts; no content, publication receipt or spending record was erased. The local cohort retains the former publication history and now reports 79 approvals and 21 rejections. The strengthened prepublication check also withholds every sibling if a duplicate child fails. Numeric quantities, negations, different passages and genuinely distinct facts remain distinct in regression tests.

Two serving false positives were found from actual inventory: the guard collapsed +3.75 and -3.75, and treated vocabulary definitions containing 'true' as answer verdicts. Signed scalars now preserve value/sign, equivalent scalar options still collide, and truth assertions require an actual verdict. Independent key, support and explanation validation remain unchanged. The frozen academic contract is unaffected; no fresh paid benchmark was purchased.

Factory passes 319, recovery 39, and the scoped answer/selector/payment/wallet/ticket checks pass 64. The controller was stopped only after two child-empty checks, preserving accepted provider jobs; it resumed with the same persistent ledger. Remaining accepted cohorts 008–010 are still processing. The current count and lifetime figures are in artifacts/question-factory/continuation-500/REPORT.md; neither pending work nor historical duplicate publications count as delivery. Production student availability still needs the owner to save the prepared signing secret; OpenAI billing login returned an authentication error, and its historical 503 maximum reservation remains fully counted.

## 7 October 2026, 09:05 UTC — content-bound retrieval and automatic final evidence

The stronger real staging check passes 413/413 approved items across all four subjects, verifies actual passage-group IDs and nine complete groups, and finds no rejected questions in retrieval or storage. Its proof binds the complete exported content/evidence hash and the unchanged academic validation contract d80135b0271f350a1864c9d107b078f07fbefa54419c4615a8891aa096308399. Anonymous/student admin denial, cross-origin rejection, funded checkpoint replay, unfunded 10k denial and the preserved $25 monthly student AI cap also pass. No paid model calls, emails or production data writes occur in these checks.

The final export now refreshes REPORT.md automatically. Once every registered candidate and accepted provider processing stage is terminal and the actual usable bank reaches 500, it runs one real staging retrieval and, under the existing production authorization, one real production retrieval. Attempts are persisted before dispatch; content, evidence, academic verification contract and retrieval-script content bind reuse. Interrupted/failed checks remain explicit rather than being presented as completion. After an external configuration fix, --refresh-final-evidence rechecks without generation or paid evaluations. This lets the persistent worker finish reviewable evidence if chat usage ends while native results are still pending.

The factory suite passes 317 tests. Recovery passes 39 and question/payment/ticket checks pass 67. Production submission fix 2e50d71 remains Ready; new production factory retrieval still needs owner submission of the prepared signing key. The fixed 1000-candidate campaign remains incomplete and its pending native requests are retained, not resubmitted or counted as delivered.

## 7 October 2026, 08:38 UTC — deployed submission fix and safe campaign restart

Production 2e50d719cf86e83dc6fc8fbab5fcfaef5f45f8a8 is Ready/Latest (50-second cloud build), verified on its exact Vercel overview. The expanded recovery command passes 39 tests. Actual full mocks for all four subjects and English quick practice pass the separate-staging launch/submission/replay check; every selected item is in the new approved bank.

The controller was restarted only after two inspections confirmed no active worker child. Its old process ended; no worker child or provider job was terminated. Actual restart evidence retains all 293 previous accepted provider IDs, zero missing IDs and all 6079 ledger requests. The resumed controller reports the current 413 usable questions rather than the old module's conservative undercount of 410. Accepted request IDs were not resubmitted.

Pending-capacity scheduling now waits for already accepted candidates or settled approvals that can fill the target before buying another cohort. This potential is an upper bound, not promised yield. Terminal receipt-only holds contribute no fictitious delivery capacity and remain fully committed; bounded unrelated work remains permitted. The new scheduling cases and existing budget/concurrency/recovery checks pass (17 targeted tests). The export report binds its coverage snapshot to its own inventory measurement so an older running controller cannot overwrite the report's count or topic contract.

The live campaign remains unfinished: six completed fixed cohorts, 600 candidates, 413 unique published questions; cohort 007 has 78 approvals, 17 rejected and five accepted requests pending, and cohorts 008–010 still await accepted authoring results. At 08:25:58 UTC, lifetime receipt-settled usage is $10.680328 and conservative holds $1.139486, committed $11.819814 under $50. Production student retrieval still requires owner entry/submission of the prepared signing key; provider invoices and the historical 503 usage remain unresolved. None of the queued work is counted as completed delivery.

## 7 October 2026, 08:20 UTC — actual full-paper submission repaired and verified

Production commit 66aef5f is Ready (50-second cloud build), including source families through fixed cohort 010. This does not establish new factory student retrieval: owner submission of the prepared Production CUET_EVIDENCE_SIGNING_KEY remains pending.

Actual separate-staging API launches exposed a real issue: 50 selected factory questions carried sufficient verification records to make the encrypted device-held session ticket exceed the 600k submission limit. New p2 tickets compress the complete server snapshot before AES-GCM encryption, retain an 8 MiB decompression bound and the existing 500k ticket ceiling, and keep valid p1 tickets readable. No academic evidence, keys, source records or historical receipts were dropped. Sealing still precedes charging; oversized sets fail before spend.

The corrected live staging check passed English quick practice and all four 50-question/60-minute full mocks, actual approved-question selection, four options, passage delivery, hidden timed-session keys, free replay and idempotent submissions. Synthetic unanswered attempts score zero; these are test records, not learner-gain or fresh academic reliability evidence. Failed initial checks remain in practice-launch-checks.json. The existing disposable student received a separately recorded 160-credit non-monetary staging fixture; production balances, entitlements, payment receipts and AI budgets remain untouched.

Verification: 35 existing recovery checks and 67 question/payment/ticket checks passed; the four new ticket checks cover exact large-snapshot recovery, legacy readability, authentication/tampering/ownership/expiry, and decompression limits. The complete release build passes. The new ticket suite is now included in test:recovery. Accepted generation requests continue under their original IDs; the 500 delivery target and final accounting remain unfinished.

# Implementation status — latest update: 7 October 2026

## 7 October 2026 — owner-approved production release and cost optimization (ongoing)

- Update 07:57 UTC: six completed fixed cohorts retain all 600 candidates: 413 approved, 187 withheld, gross cohort cost $3.447259. Actual signed-in staging retrieval at 07:51 verifies all 413 exact records (English 111, Accountancy 86, Business Studies 111, Economics 105), nine complete passage groups and zero rejected items. All 413 have production atomic storage receipts; new production student retrieval still needs the owner signing-key entry. The original fixed 100 remains 50 approved/50 rejected/$0.515798, not substituted by continuation yields.
- Release 9085d02849756710323abf3e702c633b4608dfcf is visibly Ready/Latest on www.mockmob.in after a same-commit clean rebuild (70 seconds). Initial Vercel restored-cache build failed in Turbopack Google-font module resolution; the uncached rebuild passed. Actual production feed preserves existing library access in all four subjects. Factory 315/315, recovery 35/35, question/payment 63/63 and production build pass; frozen academic contract remains d80135b0271f350a1864c9d107b078f07fbefa54419c4615a8891aa096308399.
- A repeated authenticated staging check hit the 30-second request timeout because controls downloaded/classified the full bank twice. Controls now retain the first inventory's explicit counts_snapshot_at, apply the same funding/evidence gates, then re-read actual database controls without a second whole-bank download. Live authenticated release/replay and all-413 retrieval pass, as do the subsequent build and recovery checks. No correctness gate or paid-model stage was removed.
- The local helper's IPv4-only binding did not match this host's localhost (::1) resolution. Helpers now bind only to localhost and the direct localhost health check returns 200. Existing browser error pages are additionally blocked by Browser Use's data-URL policy; no raw browser/security workaround was used. Current rendered admin recapture needs that browser page restored; earlier actual admin/student screenshots remain dated evidence.
- Cohorts 007–010 retain accepted IDs and fixed 100-candidate denominators. Pending authoring and independent batch checks are provider work, not completed questions. The live exclusive guarded controller continues; the $50 content cap and $25/IST-month student cap remain intact. Current exports and dated lifetime reservations/forecasts are in continuation-500/REPORT.md; no global settled-cost or invoice claim while the saved historical 503 remains held.

- Update 07:40 UTC: original fixed 100 and continuation cohorts 002–006 are academically complete (600 candidates; 413 approved, 187 withheld), with completed-cohort gross cost $3.447259. Publication of cohort 003 is still progressing; dated actual counts and receipts are in `artifacts/question-factory/continuation-500/REPORT.md`. Cohorts 007–009 retain their fixed denominators and accepted provider IDs; queued candidates are not counted as usable delivery.
- Actual signed-in staging retrieval at 07:27 verifies all then-published 253 exact keys/options/explanations, six complete passage groups and zero rejected items. Monthly student AI cap remains $25. Latest deployed commit fc060f2 is visibly Ready/Latest in Production (43-second Vercel build). New factory production student availability still requires the owner signing-key entry and current family registry deployment.
- Fixed a deterministic answer-guard false positive: the ordinary dictionary definition “understood in more than one way” was wrongly treated as a combined-answer choice. Combined-answer options remain withheld; two regressions pass. Independently validated academic content and keys were unchanged. Recovery 35/35 and question/payment 63/63 pass after this correction.
- English coverage now separates exact numbered/lettered official syllabus phrases instead of treating the whole PDF as a single unfillable topic; independent tag disagreement remains unclassified. Five official-topic regression checks pass. Aggregate exports now disclose all completed cohort economics alongside the predeclared current-author-contract subset and lower independent craft ratings; no partial or favorable-cohort selection.
- The first v3 authoring cohort completed 88/100 approvals for $0.695839, with overall scores 28 at 7 and 60 at 8. These are sound-to-ordinary practice ratings, not uniform premium or accuracy guarantees. Actual committed lifetime snapshots include all outstanding reservations and the historical $0.011096 OpenAI 503 hold; no provider invoice or globally settled-cost claim.

- Update 06:00 UTC: two fixed 100-candidate cohorts are complete. Original: 50 approved/50 rejected/$0.515798; native cohort 002: 53 approved/47 rejected/$0.482092. All **103** newly approved items are published in staging and production database. Signed-in staging student retrieval verifies all 103 exact keys/options/explanations and two complete passage groups; no rejected item retrieved. Production student availability of new factory items still requires the pending owner signing-key entry; it is not counted as verified delivery.
- Production compatibility release **9bf60d0cf6e4faaf62ef12dfeae048d7fa90e6c7** is Ready (49-second Vercel build). Its actual public feed again returns existing library questions in all four subjects. Fixed a regression requiring screening receipts on every pre-existing row; existing holds and any failed/stale receipt still withhold a row, and modern factory evidence/provenance cannot use legacy compatibility. 313 factory, 35 recovery and 61 question/payment checks pass; production build passes.
- Atomic publication caught three individually approved children with differing chapter classifications in one registered passage. The publisher stopped correctly. Prepublication inspection now uses that same unchanged group contract and quarantines the entire affected group before RPCs. Three additional removals reduced native cohort 002 from 56 to 53; no forced repair, rewritten answer or score inflation.
- Cohort 004 authoring finished with 87 responses and 13 provider-confirmed invalid-schema failures: strict quote enums cannot contain newline characters. Failed requests remain in its denominator. New author contract v3 uses exact contiguous source spans without control characters. Existing accepted v2 bodies and idempotency keys are preserved byte for byte; no accepted ID is replaced. Regression tests cover both.
- At 05:59 UTC the actual lifetime ledger was $9.230111 committed, including pending validations and conservative holds. This is a dated snapshot, not a final cost or provider invoice. Cohorts 003–005 are still in progress. **500 registered candidates is not 500 approved questions.** The guarded worker continues toward 500 new usable publications; current-author-contract forecast remains unmeasured until complete cohorts exist. Content cap stays $50; student cap stays $25/IST month.


## Earlier release record (retained)

# Implementation status — latest update: 5 October 2026

## 5 October 2026 — Source-linked study expansion and journey fixes

Implemented in the isolated `artifacts/study-suite/release` checkout; the original dirty
checkout and its unfinished owner edits are preserved. Existing Android/offline work is
retained. See `STUDY-CONTENT-WORKFLOW.md` for inexpensive expansion and correction rules.

- Current manifest: 21 lessons / 86 cards / 221 task variants; partial lesson coverage
  in 15 of 54 chapters, up from 8. Seven new concept packets cover Planning, Staffing,
  Directing, Money & Banking, Government Budget, Share Capital and Accounting Ratios.
  The preceding 14 lessons and 65 cards retain their exact canonical content hashes.
- Source-linked authoring compiles teaching, contrasts, concept maps, original checks,
  recall and printable material once. Strict PDF/digest reconciliation, independent
  arithmetic and packet/key checks passed with no quarantine. Skipping PDF checks cannot
  publish; same-version mutations fail. No paid content generation ran.
- Saved SQL and PGlite receipts preceded current-project inserts. Read-only live plan
  matched all 79 preceding rows; insert verification matches all 107 current unit/card
  rows. Share-capital title narrowed to the three stages actually taught through an
  immutable v2 correction, not an overwrite. Superseded v1 withdrawal follows deployment.
  No question-bank, attempt, entitlement or balance changes were made by the importer.
- Recall introduces new cards only after teaching. Corrected sessions link to current
  lessons. Mixed revision navigates directly and lists learned concepts within the
  20-concept limit. Results show all matched lessons. Student controls use large selection
  tiles, explicit assistance choices, specific next actions and reduced-motion-safe reveals.
- Session validation reads only its bound lesson IDs, with current publication and canonical
  hash checks retained. Catalog growth no longer increases records transferred on every
  Continue/answer request. No latency or field-CWV improvement is claimed without measurement.
- Owner-authorised chapter summaries return reading blocks only, record teaching
  exposure and do not certify completion. Browser print/PDF action and print CSS included.
- Optional one-credit tutor uses only the current published lesson or already revealed
  feedback, validated against owner, version, revision and item before credit reservation.
  Existing $25/IST-month runtime guard and 10/50 Free/Pro allowances retained. One owner QA
  explanation completed: one credit committed, provider receipt $0.00032835. Content
  generation spend remains $0. Same-step saved explanations can replay without a second
  charge. Removed the obsolete Demo Login provider; server-validated Supabase auth retained.
- Fresh verification: recovery 35, learning 80, study 22, payment/answer-integrity/NTA/UI
  45 — 182 distinct tests, all passed without skips. Lint and production build passed.
  Sandbox build stalled; the normal-filesystem build completed, with no config workaround.
  Canonical source/content validation and isolated import/correction dry runs passed.
- Browser preview completed a new Planning lesson, two keyboard checks and the transition
  into three recall cards. Real signed-in run saved and resumed step 2 after reload;
  the tutor returned a correct policy/procedure/rule explanation. Server-backed chapter
  summary loaded in both themes. Comparison/summary at 320/390/768/1024/1440 and short
  landscape: no document overflow; inspected controls at least 44px. These are owner QA
  and viewport-emulation checks, not student outcomes or physical-device performance.

Evidence: `artifacts/study-suite/v3/` and `artifacts/study-suite/coverage.json`.
Published as `86accc3` on `origin/main`. Vercel production deployment
`63WAusDST9US1pFBq9ZEhMMb4W42` is Ready (39s build), created 5 October at 02:06:43 IST.
Live public/auth checks passed: home/Learn/summary shell 200, anonymous catalog/summary
API 401, dev preview 404, Google-only auth providers and apex-to-www 307. Signed-in live
Learn showed 21 lessons and the new chapter entries; Pro mixed revision opened its saved
five-card run directly. The owner's corrected old run now links to the current vocabulary
lesson. The new Planning run resumes across localhost/production with the same saved step.
Share-capital v1 was quarantined after deployment; all 107 current hashes still match.
Rollback keeps records: revert the release commit or disable the existing independent
study flags and redeploy; no deletes.
New rows are ignored by the preceding release manifest. Remaining: 39 chapters without
lessons, deeper coverage within the 15 touched chapters, real-device/offline-pack checks,
screen reader/200% zoom/OS reduced motion, actual print output, field CWV, delayed unseen
question outcomes and Supabase CLI migration-history reconciliation. No full-coverage,
mastery or superiority claim is authorized by this source/self-study gate.

## 4 October 2026 — Mobile refinement publication authorized (Codex)

The owner explicitly requested committing these changes to the live website. Publishing
the verified mobile refinement through `main` and the existing Git deployment integration.
Physical-device/background-tab acceptance and the inconsistent throttled LCP result remain
documented limitations, not completed checks. No database or environment changes are part
of this publication. Deployment completion is to be checked against the live domain.

## 4 October 2026 — Mobile refinement implemented locally (Codex)

Owner approved implementation and the public companion name **Mobi**. Detailed changes,
measurements and limits: `MOBILE-REFINEMENT-IMPLEMENTATION-2026-10-04.md`.

- Lab starts only when its content is readable. One clock pauses offscreen/hidden;
  manual steps pause and explicit Replay restarts. Compact phone controls and natural
  panel sizing; Mobi uses contained local reactions, preserving desktop travel.
- Phone hero/exam palette refined. Practice summary repaired at 320px (390px → 166px).
  Result Find shortened through disclosure (1247px → 399px at 390px). Light answer-state
  contrast corrected; navigation glass has opaque accessibility fallbacks.
- Arena header now sticks correctly. More opens without page jumps, scrolls between
  measured header/dock bounds, and restores opener focus on Escape. Final checks at
  320px, 390px with 200% text, and 844×390 landscape reached the last account action.
- Responsive matrix: 56 homepage/Practice/Result/quick-runner configurations across seven
  widths and both themes; no root overflow or page exceptions. Timing, reduced motion,
  text zoom, Mobi fallback, both NTA skins' answer/palette flows, public demo, theme
  persistence and free/error states verified in development fixtures. Result contrast
  scans had no flagged text. Evidence: `artifacts/mobile-refinement-2026-10-04/`.
- Lint/build passed. Recovery 35, learning 80, NTA/answer-integrity/payment 40: all 155
  tests passed without skips. Diff whitespace check passed. Build EPERM was resolved by
  approved filesystem access, with no cache deletion or configuration workaround.
- Isolated Slow 4G/4× CPU production samples: CLS 0; LCP 1.604–3.532s, so the 2.5s
  target is not consistently met. Physical Android/Safari, actual background-tab resume,
  assistive technology and real signed-in acceptance remain open. Local emulation does
  not establish hardware or production readiness. No paid model, migration or deploy.
- Preview: localhost:3010. Temporary production server 3011 stopped. Existing edits/
  untracked artifacts preserved. No commit or push; publication awaits device/performance
  acceptance and an explicit deployment decision.

## 4 October 2026 — Published mobile audit and Preparoo reference study (Codex)

Audit and plan only; no product behaviour or production changes. Plan:
`MOBILE-REFINEMENT-PLAN-2026-10-04.md`. Evidence: `artifacts/mobile-audit-2026-10-04/`.

- Live homepage: 390/1280px, both themes; Lab autoplay advances to Find while the replay
  has zero visible pixels on phones. The phone rail occupies 376px before the replay.
- Preparoo public reference: 390/1280px, wheel-scroll samples, phone illustration and
  backdrop-filter inventory. Observed mobile hero asset is WebP, plus PNG/SVG assets.
  Phone feature/explanation/preview hierarchy is the useful reference; no assets copied.
- Hydrated Arena fixtures: Practice, branded quick runner, Result at 320/390/430px,
  both themes, 18 captures. Zero document overflow/page exceptions. Narrow Practice
  cost text wraps nearly letter by letter; Result Find occupies 1247px at 390px.
  Light Result option letters produce two contrast flags (~2.75/2.82:1).
- Menu taps and Escape close verified at 320/390px. Public reduced motion shows a
  complete static replay and removes the floating guide. Initial unhydrated captures
  were rejected; localhost-origin retry restored fixture hydration without config edits.
- Next: playback readability gate + compact Lab + Practice summary + Result density/
  contrast, then phone-local mascot, previews/navigation and daylight depth. Mobi is
  a suggested name only, not an approved or implemented rename.
- Browser emulation is not physical-device proof. Real Android/Safari, screen reader,
  throttled production performance, both premium NTA skins and live signed-in workflows
  remain acceptance gates. No attempt, model call, checkout, migration or deploy ran.
  Only audit scripts/docs changed; product suites/build were not rerun. Local preview
  is running on port 3010. Existing untracked evidence directories were preserved.

## 5 October 2026 — Mistake Repair on GPT-6 Luna (Claude)

Owner chose GPT-6 Luna (USD 0.10 in / 0.50 out per 1M) for Mistake Repair: reasoning effort `low` for
the repair, `high` for the blind second opinion (`REPAIR_ROUTE`/`REPAIR_EFFORT` in
`src/services/recovery/mistakeRepair.js`; `AI_REPAIR_MODEL` overrides). `providers.js` now sends
`max_completion_tokens` + `reasoning_effort` (no temperature) to GPT-5/6/o-series and reserves budget
for hidden reasoning tokens. gpt-4o-mini remains the fallback. Price row inserted in production
`runtime_ai_prices` (owner instruction to ship now; file `20261005090000_runtime_ai_price_gpt6_luna.sql`).
Not verified: a live GPT-6 Luna call (the live eval run was blocked by the local permission
classifier). If Luna rejects a parameter, repairs fall back to gpt-4o-mini rather than failing.
Open: key disputes ("No repair for this one") still are not logged as evidence about the key; the
dispute flow designed on 5 October (soft flags, proposed key, student-was-right signal) is next.

## 4 October 2026 (late night) — Result page + Score Recovery Lab redesign after owner test (Claude)

Owner tried a 10-question quick practice (3 right, 7 wrong) and rated the Lab 5/10: no meaningful use,
weird "replay your decisions" slider, page too tall; wanted summary + Pip first, then the Lab, then
each answer with Mistake Repair. Done (see DESIGN.md "Score Recovery Lab"):
- `data/session_recovery.js` (new, pure): marks gap (6 per wrong, 5 per blank), chapters ranked by
  marks lost, per-question time from device events, factual observations. Tests:
  `data/tests/session_recovery.test.mjs` (added to `test:recovery`).
- `ResultPageClient.jsx` rewritten: summary hero with question strip → Lab → accordion answers.
  Removed from this page: ArenaHead, MistakeReplay, SessionReadout, the separate next-step block and
  the compact LearningNextAction (all duplicated the Lab). Components still exist for other pages.
- `ScoreRecoveryLab.jsx` rewritten as Find / Repair / Prove; slider replaced by a folded decision log.
- `MistakeRepair.jsx`: staged loading, two-card trap/why-wrong layout, "matched the key" check,
  auto-run when launched from the Lab queue, "Next mistake: Qn" chaining.
- `/preview/arena?view=result` fixture is now a realistic 10-question session scored by the real
  engine; `/preview/recovery` redirects there.
Verified: recovery 35, learning 80, nta 22, answer-integrity 6, du 19, payment/questions/PrepOS/repair
81 pass; lint clean; `next build` 62/62. Browser: desktop, 375px (no horizontal scroll), light theme,
Start repairing → Q2 repaired → Next mistake Q3 → Q4. Page height on the fixture fell from ~5.8k to ~3.6k px.
Second pass (owner: UI 9/10, clarity 7/10, "too much AI framing"): repair copy no longer narrates
the AI ("Why option C felt right", "Where it breaks", "Checked against the answer key"); server
held/not-explained messages rewritten the same way; sparkle icon replaced by a wrench; observations
are now tag + fact + consequence + one tip; step headers say what each step is for; mono uppercase
labels replaced with sentence case; motion added (score count-up, Pip entrance, strip stagger, bars
and chapter tracks grow when the Lab scrolls into view, repair cards stagger in; all off under reduced
motion). Owner approved commit and push to main.

## 4 October 2026 (night) — Score Recovery + AI unblocked and live in production DB (Claude)

Owner decisions in chat: names (marketing "Score Recovery", feature "Score Recovery Lab", action
"Mistake Repair"); student AI USD 25 per IST month; content generation USD 50 lifetime; AI migrations to
production "with my OK" (then explicit yes on the dry-run report); provider "whichever is best, make a
report" (AI-MODEL-REPORT-2026-10-04.md); OpenAI tonight because the Anthropic key is invalid.
Plan of record: PLAN-2026-10-04-NEXT-DAYS.md.

**Production database changes (owner-approved, applied via Supabase MCP):**
`runtime_ai_guard`, `prepos_credit_reservations`, `runtime_ai_monthly_cap` (new file
20261004120000). Dry run: reports/ai-migrations-dry-run-2026-10-04.json (PGlite rehearsal + production
precondition checks: no collisions, 879 wallets / 108 ledger rows untouched). Found and fixed before
applying: the ledger `reason` check would have rejected every reserve/release (all paid replies would
have failed); a single missing-usage response paused all student AI; prices expired after 30 days.
Verified after apply: cap 25, prices for claude-haiku-4-5, claude-sonnet-5-5, gpt-4.1-mini, gpt-4o-mini
(gpt-4o-mini added by SQL insert), all functions present, readiness script all green.

**Code:**
- `RELEASE_GATES.runtimeAi = true` (PrepOS replies + Mistake Repair); new `aiCommerce = false` keeps
  top-up checkout and charged Rival battles closed (order route, packs, pricing page, Rival).
- Anthropic provider in `src/services/ai/providers.js` (SDK retries off, per-model params: Sonnet 5.5
  without custom temperature / thinking off). `.env.local` routing: OpenAI gpt-4.1-mini fast+smart,
  gpt-4o-mini fallback (Claude routing documented for when the key is fixed).
- **Mistake Repair**: `data/mistake_repair.js` (eligibility, solve-then-explain prompt, blind second
  opinion, output validation incl. banned score/rank promises), `src/services/recovery/mistakeRepair.js`
  (1 PrepOS credit via reserve/commit/release; finished repair stored on the committed reservation and
  reopened free; dispute → blind check → question withheld exactly like a student report, credit
  released), `POST /api/recovery/repair`, `src/components/recovery/MistakeRepair.jsx` on result-page
  wrong answers with "Prove it: 5 fresh questions on this chapter".
- Budgets: AGENTS.md rewritten (limits are owner-set; do not invent stricter ones);
  `CONTENT_LIFETIME_CEILING_USD = 50` in budgetLedger.mjs; COST-POLICY, QUALITY, ROADMAP, README,
  PRODUCT, DECISION, IMPLEMENTATION, BACKLOG, LEARNING-DEPLOYMENT reconciled.

**Verification actually run** (logs: artifacts/ai-night-2026-10-04/):
- Live smoke through the production guard: gpt-4.1-mini ×2, gpt-4o-mini ×1 valid JSON, receipted
  (~$0.00007 each). Anthropic: 401 invalid key (booked conservatively, no pause).
- Live Mistake Repair eval on 10 real published bank questions: 10/10 solved = key, explained,
  $0.0038 total. Sample was all Accountancy (selection by ID order) — not representative.
- Tests: recovery 30/30, learning 80/80 (+5 Mistake Repair, +1 production-migration PGlite), nta 22/22,
  answer-integrity 6/6, du 19/19, payment 12/12, questions 9/9, recovery:validate; lint clean; build 62/62.
- Browser (preview fixture, localhost:3010): repair explained / withheld / out of credits / failure
  states, light theme; result page renders the panel only under wrong answers.
- Month-to-date runtime spend after all tests: ≈ $0.008 of $25.

**Deployed (owner chose "commit and push to main"):** `3c88f92` (all source/docs in the tree, incl.
the owner's and earlier agents' uncommitted work; untracked `artifacts/` 121 MB deliberately not committed).
**Incident:** that tree contained an earlier agent's www→apex redirect in next.config.mjs while Vercel
redirects apex→www, so production looped (50 redirects) for ~15–20 minutes. Hotfix `499475a` removed the
rule; site verified 200 at 01:03 IST on /, /pricing, /cuet-subject-combination, /api/stats; new
/api/recovery/repair and /api/ai/mentor/chat answer 401 signed out. Lesson: before pushing a dirty tree,
diff next.config/middleware against the deployed commit and probe redirects right after deploy. To make
the apex canonical, change Vercel's domain redirect first, then add the rule.
**Not done / gates:** Vercel `AI_*` env vars (code defaults to OpenAI gpt-4o-mini/gpt-4.1-mini, both
priced, so replies work if Vercel has OPENAI_API_KEY — unverified); signed-in production
check of a real PrepOS reply and repair; Anthropic key; learning/recovery migrations (triggers on live
`questions`) still unapplied; homepage/store copy not yet renamed to "Score Recovery"; AI purchases
closed; AI dispute quarantine relies on one model family tonight (both opinions from OpenAI).

Rollback: `update runtime_ai_budget set monthly_cap_usd=0` stops all student AI instantly; or set
`RELEASE_GATES.runtimeAi=false` / `PREPOS_MODEL_REPLIES_DISABLED=true`. Remove the repair route and
component to withdraw Mistake Repair. Wallets and ledger history are never rewritten.

## 4 October 2026 — Differentiator decision and first validation slice (Claude)

Decision: [DECISION-2026-10-03-DIFFERENTIATOR.md](DECISION-2026-10-03-DIFFERENTIATOR.md). Primary bet
"repair that holds", proven on one pathway before eight; trustworthy practice and goal-aware DU tools
support it. Rename to "Mistake Repair" proposed, **not applied** (owner decision). Brain reconciled:
README, PRODUCT.md, ROADMAP-2027 (amendment), IMPLEMENTATION-2027 (Stage 2), BACKLOG (ordered next).

Implemented (local source only; nothing deployed, migrated, seeded, purchased or sent to a model):
- Candidate pathway `data/recovery_candidates/sacrificing_gaining.{source,pathway}.json`: original
  wording, CUET UG 2026 Accountancy (301) Unit II locator with PDF SHA-256, 3 probes / 5 repair /
  6 checks, 14 families, hypotheses secure / direction_reversed / old_ratio_default / new_ratio_used,
  boundary checks (old ratio correct; unaffected partner). State `candidate`; manifest still
  `blocked_sources` with `pathways: []`. `source_registry.json` deliberately untouched (the paid
  worker treats an empty registry as a pause signal).
- Validator `data/pathway_validation.js` + `npm run recovery:validate`: exact-fraction recomputation of
  every key, matrix cell, derived ratio, unique key, option-text/claim binding, family disjointness,
  isomorphic scenarios, sources. 97/97. Corruption tests prove it fails on 13 seeded defects; it caught
  one real weakness during this work (swapped partner attribution passed), now fixed.
- Engine: no-gap diagnosis label; clearer feedback when repair ends; shared plan `primary.facts`
  (record vs rule) incl. immediate-check and upcoming-check states. Server digest now reuses
  `pathwayDigest` from the validator (same algorithm, one implementation).
- PrepOS: "Why this step" facts in the plan panel; free record reply appends the facts; model prompt
  states facts are authoritative (paid replies remain paused).
- Metrics `data/recovery_metrics.js` + read-only `scripts/learning/recovery-metrics.mjs`: completion,
  immediate/delayed/maintenance pass rates (Wilson, n), overdue and stalled attrition, defects,
  diagnosis counts, probe concordance, cost; groups < 5 suppressed; no decision < 30 episodes.
- Capability registry: `EVIDENCE_LEVELS`, `DIFFERENTIATORS`, `differentiatorClaimable()` (false for all).
- Dev-only fixture `/preview/arena?view=recovery&recovery=candidate[&net=lose-once][&clock=h]`: real
  recovery UI on the real engine, idempotent by request key; pathway read server-side in development
  only. Production build contains no candidate item IDs (grep of .next/static and .next/server: 0).

Verification actually run (logs in `artifacts/differentiator-2026-10-04/`):
- `npm.cmd run test:recovery` 30/30 (was 17; +13 candidate tests incl. PGlite storage),
  `test:learning` 74/74, `test:nta` 22/22, `test:answer-integrity` 6/6, `test:du` 19/19,
  payment_entitlements 12/12, mock selector + explore feed 9/9, `recovery:validate` passed.
- Candidate tests cover: per-hypothesis diagnosis/routing/timing (24h, 72h), secure path, conflicting
  probes → general repair, repeat exposure (seen family/question, failed checks consume families,
  exhaustion → blocked_content), interruption (stale submit rejected, expired check reopens repair),
  no key/matrix/claim leakage, concurrent start retries → one episode and one weekly allowance, refused
  start consumes nothing, second concept same week refused, idempotent response retry, answer
  correction → episode invalidated → counted as a defect.
- `npm.cmd run lint` clean; `npm.cmd run build` 61/61 pages.
- Browser (in-app pane, existing dev server on localhost:3010): start → probe 1 with response lost
  after commit → retry returned the committed state, 1 commit → probe 2 → supported old-ratio
  diagnosis, explanation, contrast → routed repair → hand-off to unassisted fresh check (4 commits for
  4 answers); conflicting probes → general explanation; PrepOS shows "Take your first fresh check"
  with record/rule facts; 320px: no overflow, 76px option targets; PrepOS facts contrast ≥ 9:1.
- Read-only metrics against the configured database: `learning_episodes` absent (PGRST205) → n = 0.
  The connected-learning migration is not applied there. Fixture report is labelled simulated.

Not done / gates: academic validation (independent Accountancy reviewer; one definition item flagged
for review); backend-signed evidence for the 14 items; staging migration + seeding + digest
registration; opted-in pilot flag (not built); scored fresh check through `/test` with real
sessions; real devices and screen readers; DPDP legal review (under-18 consent and telemetry before
~13 May 2027); owner decision on the rename; Testbook research (pages unavailable on 3 Oct).

Rollback: delete `data/recovery_candidates/`, `data/pathway_validation.js`, `data/recovery_metrics.js`,
`data/tests/recovery_pathway_candidate.test.mjs`, `data/tests/recoveryCohortFixture.mjs`,
`scripts/learning/{validate-pathway,recovery-metrics}.mjs`, the `candidates` key in
`data/recovery_pathways.json`, and the `recovery:validate`/test-list additions in package.json; revert the
small edits in learning_engine.js, capabilities.js, server/learning.js, MockMobAIHub.jsx, prepos.css,
mentor chat route, systemPrompt.js and the preview files. No data, credit, entitlement or payment path changed.


## 3 October 2026 — Owner round 2: motion, social proof, hero, Arena, Compass Pro, Combo Planner (Claude)

Owner decisions taken in chat this round: demos autoplay by default with an explicit pause; creators shown
with real follower numbers, ordered by reach; Compass gets Pro features (projection, college mapping); a new
USP feature; ₹99/month to be executed; live-site testimonials described by the owner as authenticated.

Implemented (local source only; nothing deployed, migrated, purchased or sent to a model):
- **Mistake Lab** no longer pauses under a passing cursor, a tap or the 35% visibility threshold; it pauses only
  fully offscreen, on keyboard focus, or by its button. Step descriptions share one fixed-height slot, removing the
  6-second layout shift that moved everything below on phones. Verified: steps advance while scrolling, rail
  height constant (376px at 390 wide).
- **Compass ladder** autoplays again by default as an eased, time-based rAF sweep (600–960, 11s); Pause/Play
  resumes from the visitor's score; filters no longer stop it; drag or quick score takes control.
- **Creators section** reframed "Trusted by CUET creators with 199K+ followers": counts read from public profiles on
  3 Oct 2026 (Garima Jain 25.2K + runs @du__club 161K; Rahul Thapa 13K; Prathna Jain 188), bios paraphrased from
  their own profiles, reel likes/comments where Instagram exposed them, sorted by reach, glass summary panel.
  Rahul's reel is marked Partner (his bio offers paid collaborations and the caption carries a discount code).
- **Hero**: CSS scroll-driven depth on the existing planes (aurora/grid/dots lag; drill card lifts on desktop
  only), a glass proof dock (199K+ creator reach, 73 DU programmes, 2 exam screens, 50 in 60), and a
  scroll-scrubbed statement. Progressive enhancement; reduced motion and unsupported browsers get the static page.
- **Compass Pro** (`data/compass_projection.js`, `/api/compass/pro`, `CompassPro.jsx`): per-paper practice
  projection out of 250 (attempt share × +5/−1 accuracy, Wilson range, ≥30 questions), four-paper total (one
  language + three strongest domain), personal DU shortlist (≤8 eligible programme+college targets, Rounds I–III
  in the chosen category, band position), next move (paper with most marks open + weakest ranked chapter).
  Pro enforced server-side; free sees a locked explainer. Labelled a projection, never a prediction or chance.
  No paid model call (runtime AI gate stays off). Advertised on landing, pricing and FAQ.
- **New USP: CUET Subject Combo Planner** (`/cuet-subject-combination`, `src/lib/du/combos.js`): targets + candidate
  subjects → every combination up to the paper limit checked with DU's own eligibility evaluator, ranked by targets
  met, programmes unlocked, fewer papers; "do not drop" subjects computed over all qualifying combinations; deep
  links into the calculator. Free, no signup. Promoted on landing, footer, CUET 2027 guide, sitemap.
- **Arena**: shared `ArenaHead`/`ArenaStats` (Practice's header and ruled stat strip); Today, Review, Progress
  rebuilt from a light "recovery-lab" slab into Arena pages; shared next-step card (full and compact); Radar's
  stray next-step moved under its header; Saved header; shared Empty/Error states restyled (no "// Error").

Not done, needs the owner:
- **₹99/month**: code is complete; creating the live Razorpay plan was blocked by the session's permission
  classifier. Create Plan (₹99, monthly, interval 1) in the Razorpay dashboard, set
  `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` in `.env.local` and Vercel production, redeploy. `publicOffer()` then flips
  every price surface. Run the LEARNING-DEPLOYMENT.md §A staging checks first.
- **Wall of Love**: not published. The July 2026 audit records the live-site quotes as fabricated and removed,
  and one is attributed to the owner. Publish only with written consent per quote; a founder quote must be
  labelled as such (ASCI/CCPA disclosure).

Verification: lint clean; build 56/56 (Edge Runtime warning unchanged); recovery 17/17, du 19/19 (+3 combos),
learning 74/74 (+5 compass projection), nta 22/22, answer-integrity 6/6, payment 12/12. Headless Chrome (CDP,
real input events): Mistake Lab and Compass autoplay timings; creators section 1280 dark / 390 light; hero
depth transforms at 400px scroll; statement word scrub; Compass Pro Pro/free/dark/light/390 with shortlist adds
and verdicts, contrast audit 0 failures; Today/Review/Progress/Radar/Saved fixtures; planner flow at 1280/390,
no overflow. Fixture APIs are stubs; real signed-in data, Instagram embeds on phones, real devices unverified.

Rollback: revert the files above; delete `src/app/cuet-subject-combination/`, `src/app/api/compass/pro/`,
`src/components/du/CompassPro.jsx`, `src/components/du/ComboPlanner.jsx`, `src/lib/du/combos.js`,
`data/compass_projection.js`, `src/components/arena/`, `src/app/hero-depth.css` and the two new tests.
No data, credit, entitlement or payment path changed.

## 3 October 2026 — Astra UI continuation: verification pass and confirmed fixes (Claude)

Local source only. No deployment, migration, checkout, paid generation, bank mutation or external message.
The PrepOS reservation migration remains unapplied. No image generated (none warranted).

Method: the in-app browser pane could not paint while occluded, so interaction checks ran in headless
Chrome driven over the DevTools protocol (scratch script, not committed) with real `Input.dispatch*`
mouse, touch and key events, `Emulation.setEmulatedMedia` for `prefers-reduced-motion` and colour
scheme, and touch emulation (`pointer: coarse`) below 900px. This is lab emulation, not real hardware.

Confirmed defects, each reproduced before fixing and re-checked after:
- **Signed-in Admission Compass, dark theme (high):** `du.css` reads marketing tokens defined only on
  `.mm`; inside the app shell they fell back to light ink (`#0a0a0a` on `#0b100e`, ~1.1:1 headings,
  buttons, notes), unset radii/shadows/`--volt-ink`. Bridged to `--a-*` tokens on `.app-shell .cmp`
  (`arena.css`). Light theme's active "All" chip was also unreadable; fixed by the same bridge.
- **Calculator sticky summary, light theme:** fixed night fill under theme ink (~1.1–1.6:1), public and
  signed-in, below 1100px. Now follows `--paper-raised`.
- **Calculator results at 320px:** implicit auto grid tracks (`.du-main`, `.du-list`) grew to card
  min-content, pushing cards 23–41px past the column. Pinned to `minmax(0, 1fr)`.
- **Wall of Love, 4 entries:** each lane held 2 cards, narrower than the lane, leaving an empty stretch
  every loop. Lanes now repeat hidden copies to at least 4 cards; duration scales per card (~16px/s).
  Accessible tree still lists each quote once. Removed `aria-pressed` beside a state-changing label.
- **Keyboard focus loss to `<body>`:** carousel arrow reaching its end (now `aria-disabled`, focus kept);
  activating an Instagram card (focus moves to "Open original"); demo drill after answering, Next and
  finish (focus moves to Next, first option, readout); Escape from the mobile nav sheet (returns to the
  menu button). Arrow group gained `role="group"` so its label is exposed. Nav `aria-controls` now set
  only while the sheet exists.
- **Mistake Lab, reduced motion:** tapping a question always snapped back to Q4 (effect re-ran on
  `picked`). Fixed. Score live region is quiet while the tour auto-plays.
- **Compass ladder:** UR/SC chips were 42x40 (now ≥44x44); "0 of 0 colleges" when a round/category has
  no published cutoff now says no cutoff was published for that cycle.
- **Narrow/zoomed phones:** below ~300px CSS width (≥125% zoom on a 360px phone) the menu button left the
  screen; hero title and dock CTA clipped at 200% text. Wordmark is visually hidden under 300px (still
  named), theme switch moves into the sheet under 240px, rotating hero phrase may wrap, phone title floor
  1.5rem, dock note yields under a 17rem container, dock spacer grows with text size and safe area.
  320px and wider are unchanged (measured).
- Touch tablets (761–1023px, `pointer: coarse`): NTA comparator's live palette cells 22x36 -> 49x44.
  Breadcrumb and stale-subject links raised to 44px targets.

Not changed after testing: MobileDock clearance at 320x640/740x360 (last footer line 41px above dock);
phone carousel arrows were already visible (44px) at 375/390, so code and notes agree.

Browser coverage actually exercised: homepage at 320, 390, 768, 1024, 1440, 1920 in dark and light
(no document overflow, no console errors, no broken images); 195px and 240/288px nav; 200% root font on
`/`, `/pricing`, calculator, `/cuet/english`; short landscape 740x360 and 568x320; full five-question demo
by touch and by keyboard only; comparator answer/review/switch preservation; Compass programme, category,
round, quick score, range keys and missing rows; Mistake Lab pause, step and tile selection in normal and
reduced motion; Wall fixtures 0/4/many incl. reduced motion at 320; Instagram arrows to both ends and
card activation (a real reel rendered); calculator alias search (BST, Accounts), score, share link,
reload persistence, Edit subjects; 20 public routes at 320 dark and 1280 light; `/preview/arena`
fixture views (free, Pro, inventory down, stale subjects, test, PrepOS plan/record/wallet, Compass,
Radar, Saved) at 320 and 1280. Computed-contrast audit (text vs nearest opaque surface) on home,
calculator, pricing and fixture views, both themes: remaining flags are the logotype dot (exempt) and
two probe false positives (gradient avatar, oklab launcher fill).

Verification: `npm.cmd run lint` clean; `npm.cmd run build` 55/55 pages, existing Edge Runtime warning;
`test:recovery` 17/17, `test:du` 16/16, `test:learning` 69/69, `test:nta` 22/22,
`test:answer-integrity` 6/6, `payment_entitlements` 12/12. `git diff --check` clean on edited files.

Still unverified: real phones (sticky hover, safe-area values, keyboard, 60fps), true browser page zoom
(root-font scaling and narrow viewports were used as proxies), screen readers, Instagram login walls,
signed-in persistence/entitlements/billing (`/preview/arena` is a stubbed fixture), creator permission
for the curated reels. Wall of Love stays hidden: no consented quotes exist.

Rollback boundary: revert the edits in `WallOfLove.jsx`, `CreatorReels.jsx`, `CompassLadder.jsx`,
`DemoDrill.jsx`, `MistakeLab.jsx`, `NavBar.jsx`, `Logo.jsx`, `social-proof.css`, `compass-ladder.css`,
`home-refinements.css`, `landing.css`, `globals.css` (crumbs, dock, nav-narrow, drill result),
`(app)/arena.css` (`.cmp` bridge, `.pr-alert a`) and `du/du.css` (`.du-sum`, `.du-main`, `.du-list`).
CSS/markup/focus only: no data, scoring, credit, entitlement or payment path changed.

## 3 October 2026 — Astra UI continuation handover (Codex)

The previous UI-refinement agent reached the usage limit during the final browser pass. A complete continuation prompt is saved at `docs/brain/CLAUDE-ASTRA-UI-CONTINUATION-2026-10-03.md`. This pass completed focused homepage, Compass, Mistake Lab, reveal, morph and historical-copy refinements, plus integrated social, authenticated-page and public-page work documented in the three `ASTRA-*-UI-NOTES.md` files. No image asset was generated because existing campus artwork and code-native product surfaces cover the meaningful visual needs.

Fresh verification: `npm.cmd run lint` passed with 0 errors and 0 warnings; `npm.cmd run build` passed with 55 generated pages and the existing Edge Runtime warning; `npm.cmd run test:recovery` 17/17; `npm.cmd run test:learning` 69/69; `npm.cmd run test:nta` 22/22; `npm.cmd run test:answer-integrity` 6/6; `npm.cmd run test:du` 16/16; `node --test data/tests/payment_entitlements.test.mjs` 12/12. Browser evidence covers homepage light/dark at 1440, homepage at 390 and compact 320 opening, Compass filters/keyboard/demo/missing-data state, Mistake Lab manual replay, and one real deferred Instagram embed. Wall fixtures, reduced motion, all route states, 200% zoom and real-device behavior remain unverified.

Open UI follow-ups: verify/fix phone carousel arrow visibility versus `ASTRA-SOCIAL-UI-NOTES.md`; inspect Wall fixtures and reduced motion; verify closed NavBar `aria-controls` target and MobileDock height at narrow/landscape sizes; complete route/theme/keyboard browser pass; preserve the honest empty public Wall. No production data, migration, checkout, deployment, paid generation or external communication was performed.

## 3 October 2026 — Astra UI handoff preparation (Codex)

Saved `ASTRA-UI-HANDOVER-2026-10-03.md`: current-source continuation prompt for
homepage refinement and remaining student-facing UI, Scroll Craft plus all 14
Emil Kowalski skill applicability, built-in image generation, and acceptance checks.
Read current contracts and Stage R/R2 notes; inspected the local homepage at phone
and desktop sizes, Compass, dark Instagram strip, and development-only Wall preview.
Confirmed the curated social strip is already present and public testimonials remain
hidden because the consented quote list is empty. No embeds activated in this pass.

No application code changed, no test/build suites rerun, no generation, migration,
checkout or deployment performed. This is prompt preparation, not UI completion.
Signed-in routes, all motion states and real-device behavior remain unverified here.
Rollback: remove the new handoff document and this entry; application source is unchanged.

## 2 October 2026 — Stage R2: original-site comparison, Compass, Radar, NTA, creators (Claude)

Local source only. Nothing deployed, migrated, purchased or sent to a model.

Compared with the live mockmob.in (read in the in-app browser): it had a Compass showcase with a cycling score card
and college labels, a Wall of love, a PrepOS section and a college marquee. Its Compass card showed "Reach / Moderate /
High" chances and a "score band predictor"; those claims are NOT reproduced (AGENTS.md: no admission probability, no
mock-to-CUET conversion). The three quotes on that site were not carried over.

Implemented:
- **Landing Compass ladder** (`CompassLadder.jsx`, `src/lib/du/showcase.js`): a score sweeps (or is dragged) across last
  year's real published Round I-III minimum allocation scores for 10 colleges in 4 programmes and 4 categories, from
  `public/du/2026`. About 10 KB shipped. It states a gap to a past cutoff only and links to the free eligibility tool.
- **Instagram strip** (`CreatorReels.jsx`, `src/lib/social.js`): 9:16 horizontal cards for the 3 creator reels and 3
  MockMob posts found on the public profile. Instagram's own embed loads only when a card is pressed. Edit the list in
  `src/lib/social.js` to add reels. Instagram's login wall blocks reading the feed, so entries are curated, not synced.
- **Wall of love** (`WallOfLove.jsx`, `src/lib/voices.js`): two opposing drifting rows (a grid under 4 voices), hidden when
  empty, only entries with `consent: true`. Dev-only prototype with labelled placeholders at `/preview/wall`. No
  testimonial is published.
- **Practice**: NTA Mode is a featured row (mini exam-console preview, chips, "Closest to exam day") with an exam-screen
  choice (MockMob / NTA style) for Pro and a free preview link for others. The grid is Quick, Full, Smart.
- **Admission Compass page** rebuilt as a product page: opens already ticked from the student's profile subjects
  (link, then saved choice, then profile), a three-step explainer, an honesty note, a bridge from the practice record
  ("Your practice says: ..."), and the sources. Calculator logic is unchanged apart from the seed prop.
- **Radar** rebuilt on the PrepOS record engine plus a theme-aware score trend (Chart.js reads Arena tokens and re-reads on
  theme change). Removed the invented composites ("Rank readiness", "Focus score"), the 1-4 axis radar chart, the
  non-functional "Ask Radar" box and the blurred paywall over made-up metrics.
- **Free vs Pro for the record**: free = marks ledger, top 3 chapters, findings, weekly summary; Pro = every ranked
  chapter, thin-chapter list, changed-answer and pace detail. Enforced in the record view and in Ask (server and client),
  and stated in the pricing page, landing page and PrepOS wallet copy.

Verification actually run: lint clean; `test:learning` 69/69 (adds landing_content 4: real-file cutoff match, embed
format, consent filter, Pro gating of Ask); recovery 17/17, du 16/16, nta 22/22, answer-integrity 6/6; build 55/55.
Browser: landing Compass ladder, reels (the embed loaded a real reel), Wall prototype, Practice with the NTA tile, Compass
page, Radar, at 1280 and 375 widths in light; no horizontal overflow.

Not verified: no signed-in session, so Radar/Compass/Practice used the dev preview with stubbed account APIs (real engines,
real DU data). Saved, Explore, Ranks, Contribute and My uploads were not touched this round. A dark-mode pass of the new
sections was not repeated. Creator names and handles come from the public profile page; the owner should confirm permission.

## 2 October 2026 — Stage R: Arena design language, PrepOS record and wallet, ₹99/month, landing (Claude)

Local source only. Nothing deployed, migrated, purchased, or sent to a model; no real wallet or ledger row was
read or written. Owner decisions taken this round: Pro is **₹99/month auto-renewing**; PrepOS model replies for a
small monthly allowance are **built but switched off** until the gates in LEARNING-DEPLOYMENT.md pass.

Implemented:
- **One icon language.** `src/components/ui/Glyph.jsx`: one lucide family at one stroke weight (`AppIcon`,
  `StatusIcon`, `SubjectIcon` for all 42 subject ids, `ModeIcon`) and two distinct credit coins (`CreditMark`:
  bolt = practice credits, orbit = PrepOS). Replaced the mixed nav icons, the star + "∞" credit pill, the
  38 decorative subject characters, and emoji/text glyphs (✅ ❌ 💡 🌵 ⚡ ★ ▲ ▼ ↻ ✓ ✗ ⚠) in Arena, uploads, feed
  cards, onboarding and votes. Remaining hits in `scripts/design-audit/glyph-audit.mjs` are the now-unused
  `glyph` data fields, a comment and a seed question.
- **Credit display fixed everywhere.** Pro now reads "Unlimited" (coin + word, not "∞" or "no credits") in the
  top bar, Practice, Account and the modal; free reads the number. A second chip shows the PrepOS wallet
  (unknown wallets show "—", never a number). Practice credits and PrepOS credits are always labelled apart.
- **Practice screen rebuilt** (`DashboardPageClient.jsx` + `.pr-*` in `arena.css`): two-column layout with a
  sticky session summary (a pinned launch bar on phones), subject and mode tiles with icons, official subject
  codes and entitlement badges, segmented controls, a Fine-tune disclosure, ruled stat strip, recent sessions
  with subject icons, status badges with icons. No inline `<style>`. Launcher no longer covers the Start button.
- **₹99/month.** `pro_monthly_99` plan, `/create-monthly-subscription`, `/api/billing/cancel`, checkout in
  `RazorpayPaymentButton`, `PlanCard` on Account (renewal date, two-step cancel). `publicOffer()` is the single
  source for pricing page, landing page, Arena upsell, modal, SEO title and mobile dock. Closed until
  `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set; until then the existing ₹99 one-time access stays the honest offer
  and copy says monthly "opens soon". When set, new one-time checkouts close; old orders keep verifying.
- **PrepOS record engine** (`data/prepos_insights.js`, free, no model): marks ledger (+5/−1, blanks), accuracy with a
  Wilson range, chapters ranked by marks left open only with ≥4 answered questions (thin chapters listed apart),
  difficulty split, pace from device events, answer changes counted both directions with the net, last-7-days vs
  previous week. Surfaces: PrepOS "Your record" tab, "Ask" answers record questions instantly and free, Today
  shows the top finding, the Result page shows "Where your marks went" for that session.
- **PrepOS wallet clarity.** Monthly meter ("38 of 50 left", reset date, no carry-over), purchased credits shown
  apart, plain list of what is always free and what costs 1 credit.
- **Model replies, gated.** Migration `20261002130000_prepos_credit_reservations.sql` (saved, NOT applied) adds the
  reserved→executing→committed|released lifecycle; `runModelReply` wraps the existing provider/runtime-budget
  guard; chat route answers record questions free, explains the plan while paused, and runs the lifecycle only
  when `RELEASE_GATES.runtimeAi` is true. Client keeps one request id per action and reuses it only after an
  unknown outcome.
- **Landing.** The section after the hero is now the interactive "Mistake lab" (`MistakeLab.jsx`, `mistake-lab.css`):
  four auto-advancing, tappable, pausable steps (replay → leak → one next move → fresh check later) on one
  labelled illustrative session, reduced-motion and keyboard safe; the recovery step shows its real release state.
  Sharper hero and section copy; offer-aware trust row, pricing block, FAQ and stats cell. NTA/MockMob comparison,
  scroll reveals and the rest were left untouched.

Verification actually run:
- `npm.cmd run lint` clean. `npm.cmd run build` 54/54 pages, new routes present.
- `test:learning` **65/65** (adds `monthly_billing` 5, `prepos_insights` 8, `prepos_reservations` 9 in real Postgres
  via PGlite, `prepos_model_reply` 9, plus the earlier quote/wallet suites). `test:recovery` 17/17, `test:nta` 22/22,
  `test:answer-integrity` 6/6, `test:du` 16/16, `payment_entitlements` 12/12, selection/offline 16/16.
- Reservation SQL cases proven: retry same key charges once; over-reserve refused; release restores included then
  bonus exactly and is idempotent; released key cannot be reused; commit final both ways; month rollover returns
  expired included credits as bonus; expiry sweep; ledger explains balance; service-role only. PGlite is one
  connection, so these prove arithmetic and idempotency, NOT multi-session lock contention.
- Browser (dev-only `/preview/arena`, stubbed account APIs built from the real pure engines, plus the real `/`
  and `/pricing`): Practice, PrepOS record/ask/wallet and landing at 320–1366 widths in light and dark; computed
  contrast audit (full text coverage) clean on Practice, PrepOS record and wallet (light), Practice (dark; one
  false positive: black on a volt gradient avatar), landing and pricing. No horizontal overflow. Unauthenticated
  boundary: new endpoints return 401.
- Lab auto-advance, pause, step taps, tile inspector exercised in the browser.

Not verified / known gaps:
- No real signed-in session: Account PlanCard, Result-page readout and Today glimpse are lint/build verified and use
  the same components as the verified previews, but were not rendered with live data. No real Razorpay checkout
  (test or live), no webhook replay, no model call, no real Android or screen-reader run.
- Research: 20 pages requested, 16 usable; far below the 300–400 requested. See DESIGN-REFERENCES.md.
- The Chart.js screens (Radar), Moderation, Saved and Explore were not re-skinned in this round.
- Account plan card forgets a requested cancellation across reloads; subscription is created with 24 cycles.

Next incomplete criteria: staging for the reservation migration + Razorpay test plan (LEARNING-DEPLOYMENT.md A/B);
signed-in two-theme pass of the remaining app routes; then Stage C (durable sessions) and Stage D (bank audit).

## 2 October 2026 — Claude handover execution, Stage A (Arena capability/theme truth)

Local source only. No deployment, migration, checkout, paid model call or content
generation. Existing user edits preserved. Checklist: `CLAUDE-WORKLOG.md`.

Implemented:
- `data/subject_registry.js`: versioned subject registry with official codes verified
  against the NTA CUET(UG)-2026 subject list (cuet.nta.nic.in, "Last Updated Sep 02,
  2026", checked 2 Oct 2026; provisional for 2027). Crosswalk keeps old IDs
  (`gat`→501, `applied_mathematics`→319; Engineering Graphics, Entrepreneurship, Legal
  Studies, Teaching Aptitude are not in the 2026 list → `retired`). Stored choices are
  never deleted; unsupported ones show a reason and cannot launch.
- `data/capabilities.js`: capability IDs/versions, inventory purposes (ordinary,
  recovery-eligible, original sample, verified historical — none claimed), and per-mode
  capabilities with entitlement copy that never ranks question quality.
- `data/practice_quote.js` + `GET /api/practice/quote`: read-only server launch quote
  (entitlement + expiry, allowance, credit cost, duration, inventory policy/count,
  reason, 60-second staleness, server-minted idempotency token). Unknown inventory or
  an unreadable allowance is unavailable, never free. Dashboard renders only this; the
  launch button is disabled unless the quote for the exact selection is launchable,
  re-checks a stale quote, and reuses the server token across retries.
- Dashboard copy: removed "Fast lane active", "highest-quality selection layer",
  "Upgrade for premium question quality", "Most Popular" badge and "unlock more premium
  mocks"; counts say "usable questions in the ordinary library" with unavailable state.
  Onboarding lists only practice-supported subjects and lets stale saved ones be removed.
- Today: the 10/20/30 choice now sets the session (`/dashboard?mode=quick&count=10|20`,
  30 min = 20 questions + 10 minutes review) and states the duration/charging contract.
- Arena theme: semantic `--a-*` tokens for dark (Night Arena, unchanged values) and an
  intentional light palette, scoped to `html:has(.app-shell)` so portals/toasts follow.
  Tailwind's variable-backed palette is remapped in light mode; volt-as-text becomes
  `--a-accent-text`. Theme switch added to the app top bar (≥640px) and mobile sheet,
  using the existing `mm:theme:v1` preference (set pre-paint by the root script). The
  pre-shell auth screen has a light variant. The NTA-style console pins its previous
  token values so it renders exactly as before in either Arena theme. PrepOS launcher
  stays a deliberate dark island.

Verification actually run:
- `npm.cmd run test:learning` 12/12 before adding the new file; new
  `data/tests/practice_quote.test.mjs` 10/10 (final suite totals are in Stage B below) (registry codes, stale/retired/unknown
  subjects, premium block, unknown/short/empty inventory, zero credits, included/used/
  unknown allowance, expiry, no quality ranking, minutes→session). `test:recovery` 17/17.
- `npm.cmd run lint`: clean. `npm.cmd run build`: first attempt failed fetching the Geist
  Mono Google Font (network); immediate retry compiled and generated 54/54 pages.
- Browser, dev-only `/preview/arena` (mock user, stubbed account APIs, quote built by the
  real `buildPracticeQuote`) on the owner's running dev server: computed-contrast audit of
  every visible text node (`scripts/design-audit/contrast-audit.js`) and overflow check.
  Dashboard light: 0 failures at 320/375/768/1024/1280/1920 after fixes; dark at 320 and
  1280: 0 (one false positive: black on volt-gradient avatar). Branded runner light 375:
  0; answer selection causes no layout shift (paper 598px before/after); selected border
  #6f8700 ≈3.9:1. NTA console in both Arena themes: unchanged conventional skin (only its
  existing orange "visited" chip, 4.4:1, which predates this change). Exercised states:
  stale saved subjects, inventory outage, insufficient inventory (15 > 12), Pro included
  with expiry, theme toggle click + persistence. No horizontal overflow at any width.

Not verified / remaining for Stage A:
- Signed-in routes other than the dashboard/runner harness (Today, Review, Progress,
  Radar, Account, Saved, Compass, PrepOS, Explore, Ranks, Upload, Result) were not
  rendered: no session in the built-in browser and no credentials may be entered. They
  inherit the token remap, but charts (Chart.js colours), page-specific inline styles
  (TestPageClient result states, MyUploads, Moderation, Upload, Analytics) still need a
  signed-in two-theme pass. Keyboard-only and screen-reader passes not done.
- Recovery-launch quotes (`purpose=baseline/full_sample`) are computed but not exposed in UI.
- Lead, not fixed: the root font is 15px, so Tailwind `min-h-11` renders 41.25px (17 uses
  outside PrepOS). New PrepOS controls use explicit 44px.

## 2 October 2026 — Stage B (PrepOS wallet safety and explanation layer)

Local source only. Paid PrepOS stays paused (`CAPABILITIES.optionalAi.state = 'paused'`).
No wallet balance, ledger row, payment or migration was changed; no model was called.

Implemented:
- `src/services/credits/aiWalletState.js` (pure): explicit wallet states `available`,
  `empty`, `paused`, `schema_unavailable`, `error`, with a safe message. An unreadable
  wallet has `known:false` and null balances — never a synthetic allowance or a spendable
  zero. Paused wallets still show real stored balances, not spendable. Central
  `isPaidUser` uses `effectivePremiumFromRow` (status / paid-through / legacy flag) at call
  time, so expired access stops counting.
- `aiCreditWallet.js`: `readAIWallet` is one select; it never inserts, resets or syncs
  (the monthly reset/allowance sync is projected and applied only inside the atomic RPC).
  `consumeDirectly`/`grantDirectly` and the swallowed ledger insert are deleted. Spend is
  RPC-only, requires a caller-stable operation key, and returns `prepos_paused` before any
  RPC while paused; a missing RPC fails closed (503). Grants for captured purchases still
  use the atomic grant RPC (historical orders and webhook/verify paths unchanged).
  Narrowed missing-function detection so real RPC errors are not treated as "missing".
- `consumeAIAllowance`: refuses while paused before reading or charging; uses the caller's
  operation key (Rival: `rival:<battleId>:<action>`), never `Date.now()`. Rival refuses a
  paid benchmark before creating a battle row while paused. Usage snapshot accepts a
  pre-read wallet and refuses charges unless the wallet is spendable.
- `GET /api/ai/credits`: one wallet read, `state`/`message`, practice credits labelled as a
  separate ledger, `checkout.open`, packs carry `status: 'paused'`.
- PrepOS hub rewritten as an explanation layer: "Next step" renders `/api/learning/plan`
  with the same 10/20/30 choices as Today; "Ask" answers product/credit/DU questions
  deterministically and sends plan questions to the existing no-charge server route;
  "Tools and wallet" shows the wallet state read-only with no pack buttons. Removed local
  missions/day plans/setup planner (20/45/60/90), benchmark entitlements, "GPT-4.1 mini"
  and "college and course direction" copy. DU wording now: published 2026 eligibility
  rules and Round I–III minimum allocation scores by category, historical only, no
  admission prediction or mock→CUET score conversion. Hub remounts per account.
- Retired unreferenced legacy `MockMobAssistant.jsx`, `AIAssistantDrawer.jsx`,
  `AIAssistantLauncher.jsx` (no importers; tracked in git) and a dead charge helper in
  `/api/ai/actions/execute`. `/pricing/prepos` shows the paused message, "—" for unknown
  figures and lists packs only when checkout is open. Rival shows "—" for unknown wallets.
- `scripts/learning/wallet-reconciliation.mjs`: read-only wallet↔ledger reconciliation
  (grants − bonus spends vs stored bonus; included spends this period vs stored usage;
  orphan ledgers). Offline `--fixture` or explicit `--remote-read`; never writes.
- PRODUCT.md lines promising fast lane, score-band estimate, college recommendations,
  peer review and live AI packs are marked superseded.

Verification actually run (all exit 0):
- `test:learning` **33/33** (includes `practice_quote` 10 and new `prepos_wallet` 11:
  expired/legacy entitlement, missing schema, read error, paused, stale period projection,
  unmaterialised wallet, client mapping of failed/legacy responses, narrow missing-function
  detection, source guards against direct writes/time-based keys, real
  `mm_ai_consume_credits` in PGlite: two consumes over balance → one succeeds, same-key
  retry charges once, ledger insert failure rolls back the balance; grant idempotency;
  reconciliation flags drift). PGlite runs on one connection, so "concurrent" consumes are
  serialised — this proves arithmetic/idempotency, not multi-session lock contention.
- `test:recovery` 17/17, `test:nta` 22/22, `test:answer-integrity` 6/6, `test:du` 16/16,
  `payment_entitlements` 12/12; payment + mock selector + practice filtering + offline
  batch (schema/dedup/alignment/generation/import) 24/24. `npm.cmd run lint` clean.
  `npm.cmd run build` 54/54 pages.
- Unauthenticated dev-server checks: `/api/practice/quote` 401 with unavailable state,
  `/api/ai/credits` 401, `/api/learning/plan` 401, `/api/subjects` 200.
- Browser (`/preview/arena?view=prepos`, stubbed APIs built from the real pure functions):
  plan at 375 light; paused wallet shows 68 / 38/50 / 30 with the required message and no
  pack buttons; `wallet=down` shows only "could not be read… Nothing has been charged";
  Ask answers for credits, DU chances and "what next" at 320 dark; keyboard focus ring on
  section tabs. Contrast audit was corrected mid-run (it had skipped oklch/oklab colours)
  and every Stage A/B view was re-run with full coverage: 0 failures except the known
  avatar false positive.

Remaining gates before any paid PrepOS reactivation (unchanged: stays paused):
1. Student-ledger reservation lifecycle (`reserved → executing → committed/released`)
   does not exist yet; only provider-side runtime reservations/receipts
   (`20261002121000_runtime_ai_guard.sql`). Provider timeout, unusable output and
   deterministic-fallback reversal tests cannot be written until that path exists.
2. Staging verification of `ai_credit_wallets`/`ai_credit_ledger` and both RPCs, then a
   `--remote-read` reconciliation run reviewed by the owner (not run; production data was
   not read).
3. Real multi-session concurrency test against staging Postgres.
4. Signed-in browser pass of `/mentor`, `/rival`, `/pricing/prepos` and account switching.

Next incomplete acceptance criterion: Stage A signed-in two-theme pass of the remaining
app routes, then Stage C (durable sessions/recovery integration) and Stage D (read-only bank
audit against the subject registry). Stage 1 explicit staging schema remains the release gate.

## Approved roadmap execution — source implementation, launch still gated

The complete product is **not released or definition-of-done complete**. Existing
user edits were preserved. No production/staging migration, quarantine application,
deployment, real checkout/refund or paid generation was performed in this run.
The content ceiling remains $2 calibration within $10 lifetime; runtime AI funding
has not been authorized. Current offer remains ₹99 through 31 July 2027.

Implemented local behavior:

- Central capability/release truth, versioned ₹299 plan and coordinated future copy;
  old ₹99 orders, access and offer amounts are retained. New sales remain gated.
- Bounded diagnosis, selected/general reasoning repair, independent numeric solvers,
  choice/numeric/evidence-span responses, fresh-family reservation and two delayed
  checks. Wrong/unanswered/expired checks reopen repair; repeats and assistance
  cannot certify understanding. No hidden keys/matrices/future questions in plans.
- Saved service-only owner/allowance/episode/observation/exposure transactions,
  durable sessions behind a switch, legacy ticket compatibility, revision/idempotency
  checks, account ownership and changed/held-content invalidation.
- Shared next action for Today/Radar/results/PrepOS; ordinary mistake Review and
  episode-based Progress; functional recovery forms/check launch in the existing shell.
  Decision replay distinguishes event effects and net changes. Experiments deferred.
- Compass now uses sourced DU rules/cutoffs; fictional chance/score predictor removed.
- Persistent request reservations/usage receipts and rate limiting saved in Postgres
  migrations. Unknown costs/funding block physical AI dispatch. Core plans/repairs
  have no paid model dependency. New AI top-ups/replies paused; wallets preserved.
- Rival duplicate/ownership guard and atomic completion SQL. Answer changes archive
  history and queue recomputation; comparable revalidated score derivation keeps
  original attempts intact. Edited/reordered answers cannot reinterpret old indexes.
- Shared practice eligibility for inventory, truthful zero/unavailable counts, public
  aggregate caching; current copy/legal/theme refinements and optional shorter guide.
  Open test-email sending is disabled by default and admin/rate limited if enabled.
- Roadmap authority, implementation checklist, local preflight and deployment/rollback
  instructions saved in the brain. Earlier pilot/count/store order is superseded.

Verification actually performed:

- `npm.cmd run test:recovery`: 17/17 passed.
- `npm.cmd run test:learning`: 12/12 passed. Includes isolated PGlite transactions
  for allowance concurrency, owner restrictions, response retries/CAS, original
  snapshot preservation, answer correction queues and family-hold invalidation;
  zero-funding/unknown-price/reservation/receipt/rate-limit behavior; Rival atomicity.
- Combined `node --test data/tests/*.test.mjs` plus recoverySafety, evidencePipeline,
  sourceAdapters, practiceModeFiltering and offlineBatchSchema/Dedup/Alignment/
  Generation/Import: **101/101 passed**. Includes NTA, answer integrity, mock selection,
  payment/entitlement, DU and offline import gates. Fixtures are software-only.
- `npm.cmd run lint` and `npm.cmd run build`: passed before the final HTTP boundary
  follow-up; final repeat results and HTTP checks are recorded below.
- `node scripts/learning/preflight.mjs`: sources 0, academic calibration paused,
  pathways 0, current price ₹99, ₹299 disabled. See reports/learning-preflight.json.
- Browser (local development server): homepage at 320px in both themes, keyboard
  Space theme toggle, pricing at 320px, honest count failure display and unreleased
  recovery notice. No horizontal overflow on inspected home/pricing. Recovery rendered
  its unavailable state with ordinary Practice/Review links; existing session resolved
  and GET /api/learning/plan returned 200. No new study attempt or payment initiated.
  One navigation timed out before its rendered state resolved; it was not treated
  as a completed flow until the DOM showed the actual unavailable state.
- Initial local production boundary pass: 8/9 expected statuses. Empty anonymous
  mentor payload returned 400 before authentication; auth/rate limiting moved before
  parsing/context work, with a bounded payload. Final repeat recorded below.
- No screen-reader, real Android, constrained-network, Lighthouse or field CWV
  result. Theme/320px inspection does not establish accessibility or device readiness.

Release gates and remaining implementation:

1. Explicit staging schema verification/application of saved migrations, including
   older interactions, bookmarks/progress, atomic credits and recovery foundations.
   Rival additionally requires the older db/migrations AI-overlay tables before its
   new submit service deploys. No source deployment should bypass this dependency.
2. Eight permitted/versioned, independently calibrated concept pathways with complete
   fresh inventory. Sources and academic benchmarks are empty; no academic accuracy,
   student learning gain or source-backed coverage is established by these tests.
3. Real authenticated baseline → investigation → repair → immediate → two delayed
   checks, resume/account-switch/concurrency/expiry/invalidation/exhaustion tests in
   staging. Audit legacy device-ticket wall-clock limitations; its telemetry cannot
   prove answer timing. Durable server checks enforce deadlines without grace answers.
4. Correction-queue worker, report-triggered evidence re-evaluation, payment
   reconciliation and cohort/cost/support reporting remain unfinished. Uncertain
   content stays withheld. Fresh timed decision experiments wait for the core loop.
5. Real staging captured checkout, old pending orders, new V2, signature/owner/amount,
   webhook retries and refund/revocation. Optional runtime wallet reservation/reversal
   and price/funding receipts remain gates; paid AI stays paused.
6. Android/accessibility/performance, season receipts and ≥70% contribution margin;
   opted-in cohort before public recovery/₹299. Do not sell planned features as live.

Next incomplete acceptance criterion: **Stage 1 explicit staging schema and real
authenticated session/owner flow**. Stage 2 cannot release until academic source and
calibration gates pass. See IMPLEMENTATION-2027.md for the dependency checklist and
LEARNING-DEPLOYMENT.md for switches, migration order and non-destructive rollback.

Final follow-up results:

- Final `npm.cmd run build`: exit 0; optimized Next 16.2.4 build completed. Existing
  edge-runtime/static-generation warning remains informational.
- Final standalone `npm.cmd run lint`: exit 0, no diagnostics. One preceding
  overlapping lint invocation ended exit 1 without diagnostic output; this was
  not called a pass. The separate repeat completed successfully.
- `node scripts/learning/http-check.mjs`: exit 0, **9/9** expected production-build
  authentication/unavailable statuses. Saved reports/learning-http-checks.json.
  Includes the corrected anonymous mentor 401, disabled email 404 and production
  preview 404s. No cookies, credentials, provider dispatch or payment was used.
- Temporary development and production inspection servers were stopped, browser
  viewport restored and temporary inspection tab closed. No deployment made.

## 2 October 2026 — roadmap gap audit and Claude handoff

This follow-up was documentation-only. No product source, database, migration,
entitlement, wallet balance, payment, content record or deployment was changed.
The existing user-owned development server was left running. The companion audit
`ROADMAP-GAP-AUDIT-2026-10-02.md` records the evidence; the copy-ready execution
contract is `CLAUDE-MASTER-HANDOVER.md`.

Confirmed current issues include the Arena app shell staying dark while the
marketing theme reports light, no Arena theme control, stale Fast lane and mixed
availability copy, inconsistent subject catalogs, PrepOS local planner/time
choices, and wallet degraded/fallback paths that can expose synthetic balances or
non-atomic direct consumption. These findings are release blockers or staging
work; they were not patched in this audit.

The Impeccable detector returned 95 heuristic advisories across Arena/dashboard/
PrepOS files (49 font-size, 28 color, 15 radius, plus grid/transition/easing).
They are retained as review leads in `reports/claude-handover-static-audit.json`,
not counted as confirmed defects. A read-only local browser check observed the
Arena computed dark shell under `data-theme="light"` and the 320px Today fallback.
No new mock, purchase, paid model call, migration or content generation occurred.

Next incomplete acceptance criterion remains the explicit staging schema and real
authenticated session/owner flow. The next Claude run must fix Arena/capability
truth and PrepOS wallet safety before enabling paid AI, then begin the authoritative
CUET syllabus registry and read-only question-bank audit. Existing prior test/build
numbers remain prior-run evidence and were not rerun in this documentation pass.
- `git diff --check` identified three trailing-space lines introduced while editing
  pricing; they were removed. Other existing user changes remain intact.

## Historical status — October 1 2026

This is a locally implemented foundation and redesigned recovery pilot journey,
NOT a completed production launch. No production migration, bank mutation, deploy,
paid content request, APK signing, store submission or real-device test was made.

| Milestone | Completion evidence | Remaining gate |
|---|---|---|
| Project brain | AGENTS, PRODUCT, DESIGN and brain specifications/architecture/quality/cost/benchmark/backlog | Keep updating actual results |
| Read-only inventory | 9,342 records; saved per-item report and 59-row quarantine dry run | Independent semantic checks, schema deployment before applying quarantine |
| Historical failure classification | Ten zero-candidate/zero-validator routes classified unknown | Request-level receipts needed to reconstruct old bills |
| Durable cost controls | Shared SQLite reservations, usage receipts, crash/concurrency/zero-yield/repair/cache tests | Verified prices, durable worker deployment; distributed ledger not implemented |
| Evidence publication | Signed hashes, source/family/version checks, blind solving, alternative challenges, route calibration; worker/offline importer integrated | Source registry/academic fixtures empty; source-backed model adapter configured but not executed; numerical family solvers not supplied |
| Practice/recovery backend | Server scoring, event replay, idempotency, ownership, credits, playbook/review queue, changed-evidence progress exclusion | Saved SQL needs staging/production setup; correction recomputation and fuller timing/review behavior pending |
| Web pilot UI | Immediate illustrative replay, separate pilot signup, observed/inferred results, four launch subjects; public reference notes | Remaining legacy screens, live authenticated content flow |
| Mobile beta source | Bundled React/Vite/Capacitor assets/fonts, OTP/bearer, native secure storage, cached reviews/drafts, reminders; Android project generated | Public environment config, signing, JDK/SDK, macOS/iOS, real-device QA and store review |

## Verification

- npm run test:recovery: 15 focused software regressions, including local Postgres
  transaction/owner/credit/idempotency/quarantine/passage rollback tests.
- Existing answer integrity, NTA selection, mock selection, payment/entitlement and
  offline batch suites: 52 tests. Academic fixture release remains unverified.
- Production web and mobile asset builds compile. Targeted edited React lint is clean.
- Production-mode HTTP checks reject unauthenticated/forged-token attempt, analytics,
  recovery, session and mobile reads/submissions with 401. The illustrative preview
  returns 404 in production. Saved results: artifacts/recovery/http-checks.json.
- Desktop/390px captures in artifacts/recovery; no horizontal overflow in inspected
  home/lab. Replay control is 44px. Public catalog references include >1,000 designs;
  no claim that 1,000 screens were individually inspected.
- Fresh Impeccable design review: initial disposition fix; all six material fixes
  resolved in one batch; final disposition ship. DESIGN and sidecar reconciled.

Artifacts are local evidence, not live app success. Lab screenshots contain clearly
labelled development-only illustrative data. Existing user edits/payment changes
were preserved. No independent academic accuracy or model-versus-human result exists.

## Next agent

Read brain README, BANK-AUDIT and BACKLOG. Verify live setup before claiming anything
deployed. Start with authenticated source/key extraction and development/held-out
fixtures; do not open paid generation on missing prices or empty references. Keep
the $2 calibration hold and $10 ceiling. Never reset the ledger or publish the old
Economics sample based on its heuristic grade. Follow BACKLOG in order.

## 2026-10-01 stabilisation and landing rebuild (Claude)

Done and verified locally (dev server, port 3100):
- Homepage was unstyled: ChatGPT's last pass shipped about 20 `cuet-*` classes with no CSS.
  `src/app/page.js` rebuilt on the existing `.mm` system plus `src/app/landing.css`
  (`.lp-*`): hero with playable five-question drill, subject keys, live stats band,
  Arena/Radar/Compass screens (static, labelled illustrative), steps, Score Recovery
  Lab replay, free vs Pro (₹99 once) comparison, FAQ, close. On phones the drill
  follows the lead directly; subject keys follow the drill.
- `/api/leaderboard` returned 500: `Database.getLeaderboard` put 512 user ids in one
  `.in()` filter (20 KB URL, HeadersOverflowError) and silently read only the first
  1000 of 1807 attempts. Now pages attempts and chunks user lookups by 100
  (`data/db.js`). Synthetic practice rivals remain labelled.
- `LiveStatsBand` fallback claimed "10,000+" questions; live bank is 6,963
  (`/api/stats`). Fallbacks are now "6,900+" and "40". Bank note reworded to
  "automated schema, duplicate and answer-key checks".
- `/login` and `/signup` still used legacy dark utility classes inside the paper
  world. Rebuilt with `AuthShell`, `auth.css` and a restyled `SignupCard` (auth
  logic unchanged: Google, email link, 8-digit OTP).
- Testimonials: no invented student quotes were added. `src/lib/voices.js` is an empty
  list; the landing section renders only when real, consented quotes are added.

Verification: `npm run lint` clean; `npm run build` passes, all routes; test:recovery
15/15, test:nta 22/22, test:answer-integrity 6/6, payment_entitlements 11/11.
Public routes and `/api/stats|subjects|leaderboard` return 200 locally; 390px and
1440px landing/auth captures show no horizontal overflow.

Not verified: any signed-in screen (dashboard, test, result, saved, profile, Compass,
PrepOS) was NOT visually checked this pass (no test credentials used); Quick Practice
submit/resume/idempotency from the handover; Razorpay checkout end to end; production.
Remaining legacy dark-style screens inside `(app)` still need the same audit.

## 2026-10-02 landing redesign round 2 (Claude)

Owner rejected the paper homepage as less polished than mockmob.in, prepium.in and
ug.preparoo.app. Rebuilt `/` as "Night Arena" (see DESIGN.md): layered grid/dot-matrix
backdrop with pointer-lit dots, hero stage (playable drill + Example chips), subject
marquee, live stats, wide/pair/wide/trio bento (Arena, Radar, PrepOS, Compass, three
small tiles), animated three-step section, Score Recovery Lab replay, live per-subject
counts, free vs Pro, FAQ, closing band. Restored FAQ + breadcrumb JSON-LD from the old page.

Root cause of the hover "shake": `DecodeWord` re-scrambled on hover and glyph widths
differ. Deleted; replaced by width-reserving `MorphWord`. Verified by measuring every
hero element's box before/after hovering the primary CTA: no movement (only the
decorative chips on their own loop). Drill height is constant before/after answering.

Verified in the browser at 320, 390, 820x1180, 1024x768, 1280x720, 1440x900,
3440x1440 and 844x390 landscape: no horizontal overflow at any size; hero balanced;
mobile nav works on dark. `npm run lint` clean; `npm run build` passes; test:recovery 15/15;
payment_entitlements 11/11.

Not verified: real-device performance on a budget Android (backdrop uses static CSS layers;
pointer layer is disabled on touch); reduced-motion behaviour was reviewed in CSS, not
exercised in a browser; Lighthouse not run; no screen-reader pass beyond the a11y tree.
`DynamicCompassPreview.jsx`, `ArenaPreview.jsx`, `RadarField.jsx` are now unused by `/`.

## 2026-10-02 free DU eligibility and cutoff calculator (Claude)

New public tool at `/cuet-cutoff-calculator` plus a landing-page teaser (`#du-eligibility`),
nav and footer links, a hero link, a Compass-tile link, a Radar-page link that pre-fills the
student's practised subjects, and a pointer from the Admission Compass page.

Data (all from four public DU documents, user-approved download of five PDFs, ~9.7 MB):
UG Bulletin of Information 2026-27, and the Round I, II, III minimum-allocation-score lists.
Pipeline in `scripts/du-csas/` (geometry-based PDF parsing, hard failure on ambiguity);
output is static JSON in `public/du/2026/` (no serverless function runs for the tool).

Verified:
- Cutoffs: S.NO contiguous (1,393 / 1,393 / 956), identical seat lists across Rounds I and II,
  Round III a subset, and the multiset of every parsed score equals the numbers printed in the
  PDFs: 17,316 cells (two whole-number cells in Round I located individually). One displayed
  value (Dyal Singh B.Com. (Hons.) Round I OBC-NCL 695.3) traced to the raw PDF coordinates.
- Eligibility: 73 Bulletin programmes, 149 combinations all parsed into typed slots, every
  combination satisfiable. Engine tested (`npm run test:du`, 12 tests) including language
  specific rules, GAT combinations, the "considered only if seats remain" combinations III/IV,
  and the UR-merit rule for reserved categories.
- `npm run lint` clean; `npm run build` passes (route prerendered static); test:recovery 15/15,
  test:nta 22/22, test:answer-integrity 6/6, payment_entitlements 11/11.
- Browser: desktop 1440/1024 and mobile 390 on the calculator and the landing teaser; no
  horizontal overflow; selection, URL sharing, expand-to-cutoffs, score status all exercised.

Also fixed: `html, body { overflow-x: hidden }` in globals.css made `<body>` a scroll container,
so `position: sticky` (including the site's own nav) never stuck. On marketing-system pages
(`.mm.lp`) it is now `overflow-x: clip`.

Not done / limits:
- Seat counts (Prepium shows them): the seat-matrix PDF is organised differently and was not
  parsed. Not shown rather than guessed.
- 5 Bulletin programmes (3 music, B.F.A., B.Sc. PE) have test-based merit and no CUET cutoff
  list; shown for eligibility only.
- 2026 data only. Add a 2025 cycle by adding a second dataset folder; the UI reads `meta`.
- No Lighthouse or real-device run. No screen-reader pass beyond the a11y tree and aria states.
- `src/lib/admissionCompass.js` (existing, untouched) still uses invented per-college "target"
  scores and category adjustments. It is clearly labelled as an estimate, but it should not be
  presented as cutoffs. The calculator is the source of real published numbers.

## 2026-10-02 calculator rework after owner feedback (Claude)

Owner reported the cutoff calculator "not updating live", no way to recheck, clunky UX, and that
subject mapping did not show that IP/Computer Science (and similar) are one CUET subject.

What I could and could not reproduce: scripted clicks always updated state, so I found no
single hard failure. I did demonstrate real defects that make live updates invisible or
unreliable for a person: a floating "N programmes unlocked" bar sat over the chip grid (scripted
`.click()` bypasses overlays, a finger does not), the results were far below a very long picker,
and the address bar was rewritten on every change. All three are removed.

Changes: two-pane layout from 1100px (sticky subjects pane, results beside it, live); below that a
sticky summary bar with the live count and Edit / View buttons; removable selected-subject tray;
full official subject names on chips plus a finder that maps aliases (IP, Informatics Practices,
Biotech, Book Keeping, Applied Maths...) to the one subject DU/NTA count; every programme card shows
the Bulletin's exact combinations with met / missing marks, and "Not eligible yet" rows open to the
same rules. The URL is read once on load and then cleaned; edits persist in localStorage; Share
builds the link on demand.

Accuracy check: B.Sc. (Hons.) Computer Science has two Bulletin combinations and BOTH require
Mathematics/Applied Mathematics, so a commerce student with only IP is not eligible. Tests added
(16 total in `npm run test:du`): that case, the Computer Science / IP equivalence, rule
explanations, alias search. Verified in the browser with a real click: adding Mathematics took
35 -> 41 programmes and made B.Sc. CS Honours and Economics Honours appear.

Note: Prepium lists Sanskrit under List B; the 2026 Bulletin's List B (22 subjects) does not,
so the tool follows the Bulletin. Lint, build, test:du 16/16, recovery 15/15, nta 22/22,
answer-integrity 6/6, payments 11/11. No real-device or screen-reader run.

## October 2, 2026 — homepage refinement and exam-interface comparison

Preserved the existing homepage and added a refined hero practice frame, persistent
animated light/dark switch, four original campus illustration cards, and an
interactive MockMob/NTA-style comparison. Premium NTA sessions now offer a
presentation switch on the same runner; the existing scoring, timing, entitlement
and credit logic is unchanged. College cards hand off a validated programme filter
to the existing DU calculator.

Verification: production build and ESLint pass; NTA 22/22, DU 16/16, recovery 15/15,
answer integrity 6/6, payment entitlements 11/11. Browser checks at desktop and
390px/320px confirm theme persistence, mobile menu, no horizontal document overflow,
preview answer/review/clear/reset state, and Commerce preset 35/73. Premium setup
link selects NTA Mode with 50 questions / 60 minutes without starting the mock.
New browser tab reported no console errors. Generated campus asset is 276 KB WebP.

No production deployment, migration, checkout or scored exam submission performed.
The real premium exam submission path with the classic skin remains a release check.
NTA style is a reference-based practice console, not a guarantee about the official
2027 UI. Source changes and their rollback boundary, reference survey, image prompt
and evidence are in HOMEPAGE-REFINEMENT-2026-10-02.md and artifacts/homepage/.

## October 2, 2026 (second pass) — repair, theme, Arena alignment (Claude)

Local source only. Nothing deployed, migrated, purchased or generated. Screenshots:
`artifacts/refinement-2026-10-02b/`.

Confirmed defects fixed (cause → fix):
- Radar/analytics was empty for every student: `/api/analytics` kept only `server_snapshot_v1`
  attempts (Score Recovery pilot, not launched) while practice writes `server_practice_v1`.
  Now counts the owner's practice; pre-server browser-scored attempts are included and labelled
  (owner decision). Recovery/progress evidence rules are unchanged. `data/attempt_scoring.js`.
- Submission could be rejected by clock skew: runner timed events as client `Date.now()` minus
  server `startedAt`; server rejects events later than its elapsed time + 2 s. Runner now times
  from receipt using only the server duration; `finishPractice` scores answers without the
  (discarded) event log if the log is malformed (`scorePracticeSubmission`). Answers still fully
  validated. Recovery-pilot `finishSession` is unchanged.
- Result page called every new practice attempt "historical… not scored from a server-held
  snapshot". Copy now distinguishes server-scored practice from older browser-scored attempts.
- Nav dropped Radar, Saved, Compass, PrepOS, Explore, Ranks, Contribute, My uploads (pages still
  existed; several are sold as Pro). Restored as a "Tools" group (owner decision). App tour pointed
  at nine missing nav targets; rewritten for the current nav.
- Light mode: subject-card hover was `#121712` behind `#172016` text (1.08:1); landing secondary
  button hover `#151a14` (1.05:1); dark mode on paper sub-pages: shared `.mm-btn--secondary:hover`
  was `#fff` behind near-white text (1.11:1); calculator/teaser lime, amber and pink text on paper
  (1.2–2:1). Cause: night-only literals in `landing.css`/`du.css`/`globals.css`. Fixed with theme
  roles (`--accent-text`, `--accent-line`, `--accent-wash`, `--tint`, `--surface-hover`,
  `--warn/bad/good-text`) defined per theme in `marketing-theme.css`; per-selector light patches removed.
- 900–1023 px: marketing nav labels wrapped onto two lines after the toggle was added. Text links
  now move into the menu below 1024 px; CTA and Log in stay. NTA-style "Mark for Review & Next" and
  "Clear response" were hidden at 761–1023 px; now visible below 1024 px.

Refinements: theme switch redesigned (sun/moon thumb, inset-shadow crescent, stars, spring travel,
press squash, circular View Transition reveal from the switch; instant under reduced motion or
without support). Hero practice bay restored (framed bay, lit slate card, deep shadow, skeleton
explanation) plus a two-card stack; status row and purpose rail kept. Campus cards pair as
landscape cards at 761–1023 px. Arena: scoped `src/app/(app)/arena.css` re-skins shell, dashboard,
shared app primitives and the branded runner; NTA-style console untouched apart from the
breakpoint fix. Dashboard copy and numbered setup steps; no logic change.

Verified locally:
- Tests: recovery 17/17 (2 new), NTA 22/22, DU 16/16, answer integrity 6/6, payments 11/11,
  mock selector + practice filtering + offline batch (pure) 13/13. Paid-model pipeline tests not run.
- `npm run lint` clean; `npm run build` passes. Production server: `/preview/arena` and
  `/preview/recovery` 404; unauthenticated `/api/analytics`, `/api/attempts`, PATCH `/api/sessions` 401.
- Browser: computed-state contrast audit of every hover/focus/pressed/selected/disabled rule on
  `/`, `/pricing`, `/cuet-cutoff-calculator`, `/login`, `/about`, `/cuet-2027`, `/features` in both
  themes; light homepage clean; calculator text (542 nodes) passes in light with results open.
  Real-pointer hovers checked in both themes. Toggle: click, Space, Enter, focus ring, aria-checked,
  persistence, reveal animation from the switch. No document overflow at 15 widths 320–1440.
  Drill answer causes no layout shift (stage 718 px before and after).
- Arena via `/preview/arena` (development-only, mock user, stubbed account APIs, no production
  writes): dashboard subject/mode/count selection, 50-credit gate disabled with top-up hint, launch
  URL; branded runner answer, mark, clear, navigate, submit; captured payload scored by the real
  `scorePracticeSubmission`; NTA-style console at 1366 and 900 px; mobile menu at 375 px.

Not verified / release checks:
- A real signed-in Quick Practice (start → submit → result → Radar) was approved by the owner but
  not run: the browser pane had no session and credentials cannot be entered for the owner.
- Live premium NTA submission with either interface; Razorpay checkout; production deploy.
- Reduced-motion paths reviewed in code, not emulated. No real-device, Lighthouse or screen-reader run.
- `/api/bookmarks` hides saved questions that fail the current quality gate, but the free-tier
  25-save limit still counts them (not changed).
- Other app pages (Compass, Radar, Saved, Profile…) inherit the re-skinned primitives but their
  page-specific layouts were not redesigned.

## 3 October 2026 — Round 4: restored craft, Pip guide, motion system, study loop (Claude)

Local source only. Nothing deployed, migrated, purchased, generated or sent. Full record:
`docs/brain/ROUND4-NOTES.md`; motion rules: `docs/brain/MOTION.md`; brief:
`scrollcraft/builds/mockmob-round4/BRIEF.md`; evidence: `artifacts/round4/`.

- Regressions fixed at their measured causes: comparator palette (44px min-width in 1fr tracks,
  5-column phone override with span-2 holes, lost NTA placeholder skin, clipped focus rings);
  Arena entry and exam-day card (round-3 blanket overrides; containers now fade, leaves rise, so the
  fixed phone dock is never re-anchored); exam-day clock now really counts down, offscreen-paused.
- Pip: one guide that hands off between five perches and reacts to page events (drill answer, Mistake
  Lab next move, exam preview answers). Chosen over two other built prototypes (archived). Static
  perches remain the no-JS/reduced-motion experience. No mascot motion in the timed runner.
- Study loop: Result ends with one next step from the PrepOS insights engine (no chapter named
  below its 4-answer ranking rule), plus Review, Saved, Radar, Back to Practice. Saved links back to
  Practice.
- Sweep: 760 loads (38 routes × 10 sizes × 2 themes): root overflow 0, console errors 0. Found and
  fixed a Practice panel cut off from 320–1440px (grid `auto` tracks) and six sub-44px controls.
- Verified: `npm run lint` clean; `npm run build` passes; recovery 17, DU 19, learning 74, NTA 22,
  answer-integrity 6, payments 12, Explore/contribution 8 = 158/158 pass (logs in
  `artifacts/round4/logs`). Reduced motion, 200% text, real-touch flows, light theme and contrast on
  new surfaces checked in Chrome. Lab perf (prod build, 390px, 4× CPU, Slow 4G): LCP 2.9–3.3s, CLS 0.
- Not verified / release checks: physical phones, screen reader, authenticated persistence and
  resume, live premium NTA submission, payments; LCP above target with cause not isolated.

## 3 October 2026 — Round 5: continuous Pip journey and Arena handover

Local implementation. Full evidence and limits: `docs/brain/ROUND5-NOTES.md`; scoped future
work: `docs/brain/ROUND5-NEXT-FEATURES.md`; artifacts: `artifacts/round5/`.

- Seven ordered perches with hysteresis replace the narrow observer band. One desktop actor
  carries through a reserved gutter; phone motion stays local and follows document scrolling.
  Reverse/fast crossings coalesce. Larger original art, pose fades and static reduced motion.
- Lab celebration waits for the visible next-move control and settled visible Pip. One peak
  per view. Today, Practice, Review and Saved gain calm companion states; recorded-session
  acknowledgment uses server data. PrepOS keeps its orb, voice and capability/credit wall.
- Three travel/PrepOS studies archived; temporary Round 5 route removed. One requested image
  concept generated; original six pose assets remain in product. Exact GPT Image 2.5 selection
  is unavailable through the tool, so no such model-version claim is made.
- Lint and production build pass. Recovery/DU/learning/NTA/answer-integrity/payment/Explore
  suites: 158 passed, plus two station-selection tests. 760 verified layout loads: 380 public
  production + 380 development fixtures; zero root overflow, pageerrors or failed loads.
  Reduced motion, quarter-interval reverse journeys and six 200%-text fixture views checked.
- Hero-animation ablation reproduced lower text LCP (phone 1.60–1.94s versus guide baseline
  2.27–3.64s). Removed only the measured lead paragraph's entrance animation; other entrances
  remain. Final production measurements and methodological limits are in ROUND5-NOTES.md.
- No deployment, production migration, bank writes, paid-content generation, outgoing email
  or checkout. Live authenticated persistence/resume, premium NTA submission, payments,
  physical devices and screen-reader acceptance remain release gates. Fixture counts and
  laboratory performance are not live account evidence or field Core Web Vitals.

## 3 October 2026 — owner-approved Round 5 follow-up and local-server recovery

Local implementation; full source map, evidence and limits: `docs/brain/ROUND5-COMPLETION.md`.
The owner subsequently approved implementing the remaining plan and restoring the site.

- Tonight's plan now uses the shared server plan and ties its recorded state to a current-day
  server-scored attempt. First-session/fresh-check milestones use real validated records.
  Thirty minutes includes ten minutes of review, which is not automatically marked done.
- Result offers evidence-gated, unseen-family five-question replay only when inventory permits;
  ownership/rate limits and launch checks remain authoritative. No generation or bank writes.
- Install/PWA support caches only three public fallback assets. Open-runner drafts preserve
  session identity, answers and deadline. Network submission freezes answers and supports
  bounded reconnect/reload without a new timer, debit or local score. Logout purges own drafts.
- Monthly cancellation now uses the installed Razorpay SDK's boolean argument and confirms
  rejected requests only through a matching terminal provider state. No provider operation ran;
  monthly activation remains gated because the plan ID is absent. One-time Pro access remains.
- Local dev restored at `http://localhost:3010/` with separate `.next-dev` output and disabled
  Turbopack development filesystem cache. The phone-blocking Next dev indicator is disabled.
  No reset/cache deletion/bulk revert. Earlier worker/cache/chunk failure logs are retained.
- Final build and lint passed; 172 automated tests passed, including question/payment/recovery
  contracts. 760 route/size/theme loads passed. New feature suite: 43 checks passed. Acceptance:
  37 forward/reverse wheel, clipped control/focus clearance, reduced-motion, 200%-text and iOS
  help checks passed. Rebuilt homepage: 20 size/theme checks passed; production PWA check passed.
  A concurrent autoplay timing run paused and failed; unchanged sequential rerun passed, both
  retained. Fixtures, browser touch and device emulation are not live persistence/hardware proof.
- Existing signed-in browser session inspected read-only: Today 20-minute plan → Practice setup,
  fixed-expiry Account, existing legacy Result and Review. No new attempt, score or debit.
  Opera/native-app access was unavailable; Gmail/OTP access was unnecessary and not performed.
- Remaining release gates: authenticated staging submission/resume and premium NTA with both
  skins, configured monthly plan plus sandbox billing/webhook evidence, physical Android/iPhone
  and screen reader. No deploy, migration, paid content generation, checkout or external message.

## 3 October 2026 — Pip intent and PrepOS refinement (Round 6)

Owner asked to preserve the good motion, make mascot actions contextual, reduce generic hero
details, strengthen PrepOS with its existing API/wallet and prepare next steps. Full handoff and
paste-ready Claude prompt: `CLAUDE-PIP-PREPOS-HANDOFF-2026-10-03.md`.

- Added one GPT-generated attentive pose with open eyes and relaxed arms. Removed sleep/wink
  defaults from scroll reading, pricing, comparison, Arena setup and loading. Original art stays.
- Pip points inward, including its static reduced-motion fallback. Single-face 140 ms entry
  replaces the overlapping-visors dissolve. Small scroll corrections retain the expression.
  Correct sample answers keep their hop; wrong answers receive an attentive nod. Keyboard
  answers trigger no mascot reaction. The Lab peak and mascot-free timed answering remain.
- Hero now states one fixed practice promise and leads with the actual five-question sample.
  PrepOS connects its next step with the record observation and an inspect/ask handoff.
- PrepOS Ask explicitly separates free record facts from optional one-credit model guidance.
  Source labels, receipts, wallet refresh, unknown-balance handling and same-ID retry are visible.
  Unresolved requests/conversations survive PrepOS section changes; late history cannot replace
  a new conversation. Effective paid expiry is recomputed using the shared entitlement rule.
  Explicit free requests cannot fall through to a paid model; new saved replies carry their source.
- Final build and lint passed. **172 existing automated tests passed** across recovery, question,
  payment, wallet, reservation, model lifecycle and other contracts. A final focused PrepOS rerun
  also passed all 26 tests. **147 browser report entries passed** at four widths and both themes:
  forward/reverse stations, inward pointing, one face, reduced motion, free/paid/unknown wallet
  states, lost-after-commit idempotent retry, keyboard/mouse reactions, wheel reversal and quiet
  companions with doubled root font size. Browser AI responses are labelled fixtures, not live
  model calls. Evidence and earlier failed test assumptions are retained in `artifacts/round6/`.
- Read-only configured Supabase check: wallet, ledger, reservation, runtime request and price
  tables answered. Funding table unavailable through the Data API (`PGRST205`); configured
  model prices not verified; available funding not established. Paid AI remains release-gated.
  Table readability does not establish RPC correctness or applied migration history. No migration
  was executed and no model/credit/budget call was made during this check.
- Public live PrepOS still shows its earlier public-guide/missions interface. That observation
  does not establish deployment of this checkout's guarded contracts. No outgoing email, paid
  educational generation, attempt/score fabrication, checkout or deploy. Port 3010 dev is left
  running; the temporary port 3011 production verification server is stopped.
- Next gates: resolve funding-table availability, verify actual schema/RPCs against saved SQL
  without blindly reapplying migrations, establish authorized runtime funding/current prices,
  reconcile wallets and run real staging concurrency/retry/release. Then consider activation.
  Durable client retry after reload/drawer closure, physical phones, screen reader and prior
  authenticated staging/payment acceptance remain unverified. This refinement preserves the
  retry ID across section changes only; it does not claim paid-request reload recovery.

## 5 October 2026 — Luna-only routing, shorter mobile home, light default, AI purchases

Source changes (not yet deployed; deploy needs `AI_LUNA_MODEL` optional and the Razorpay env below):
- **Model routing:** `src/services/ai/providers.js` now runs GPT-6 Luna only. `fast` tier = no reasoning, `smart` tier =
  low effort; callers that solve/generate questions pass `reasoningEffort` explicitly (medium+). Fallback is Luna, no
  reasoning. Question moderation (`src/lib/moderation/ai.js`) moved from a direct Claude call to the budget-guarded
  router, Luna at medium effort. `AI_FAST_MODEL`/`AI_SMART_MODEL`/`AI_FALLBACK_*` no longer route anywhere.
- **Homepage:** removed Subjects, Marquee, How-it-works, Proof band, mini tiles, Compass Pro box, college destinations;
  Instagram moved up under the statement; stats are now combined followers, reel views (owner-stated 100K+ floor,
  `REEL_VIEWS_FLOOR`) and recorded likes+comments. Product screens hidden under 700px. Mobile page 20.2k → 15.1k px.
- **Theme:** light is the default (`layout.js`); first-visit hint on the switch (`ThemeToggle hint`), shown once.
- **Payments:** `RELEASE_GATES.aiCommerce = true` (owner, 5 Oct); PrepOS top-up packs (₹10/50, ₹20/150, ₹50/400) now sell
  on `/pricing`. Monthly Pro ₹99 opens when `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set; create it with
  `scripts/payments/create-razorpay-plan.mjs`. Pro keeps 50 PrepOS credits/month, Free 10.
- Verification: `test:learning` 80/80, `test:recovery` 35/35, payment + landing tests 16/16; browser checks on 375px.
- **Unresolved gates:** Razorpay keys + plan ID + webhook secret are empty in `.env.local`; no real captured top-up or
  subscription charge has been verified; Vercel env not updated.

### 5 October 2026 (later) — landing page restructure, feature tour
- Reverted the over-trimmed homepage: Compass Pro box, college destinations, stats band restored. Removed only the Subjects
  block (owner), the subject marquee and the three-step "how it works". Instagram stays where Subjects was.
- New `FeatureTour` (`src/components/landing/FeatureTour.jsx`, `src/app/feature-tour.css`): eight tools, one idea per slide,
  swipe on phones (scroll-snap), list + stage on desktop, autoplay with pause, only while on screen. Replaces the bento.
  Slides accept `video: '/demos/<id>.mp4'`; no recordings exist yet, so the animated screens play.
- Phone polish: glass header with progressive blur, floating glass dock, blur-in reveals (`.lp .rv`, reduced-motion safe).
- Reference studied: ug.preparoo.app (Webflow + GSAP; 7.1k px on mobile; one feature carousel, product mocks, sticky CTA).
- Tour v2 (same day): desktop is tool pills + a split stage (copy left, screen right); phones get equal-height cropped glass cards.
  Copy rewritten; Rival slide now says what it is (a fixed accuracy-and-pace target, not other students).
  `LiveStatsBand` drops a figure that fails to load instead of printing "Unavailable". Cause of the "unavailable" the owner saw:
  the preview dev server lacked `--use-system-ca` (TLS to Supabase failed); `.claude/launch.json` now uses it. Production unaffected.
- Tour v3 (same day): slides now use `TourScreens.jsx` + `tour-screens.css`, compact demo screens that play a scripted
  sequence each time their slide becomes active while the tour is on screen (timer ticks, options tapped, rows arriving,
  typing, bars filling), then hold the finished state; reduced motion shows the finished state. Nothing is cropped on phones.
  Verified frame by frame in a foreground Chrome (chrome-devtools) at 390x844 mobile and 1440x900: all 8 demos play and settle.
  Note: the desktop app's Browser pane throttles timers when hidden, so it is not reliable for checking motion.

## 4 October 2026 — UI/UX audit (audit-session date)

- Documentation-only audit saved to `docs/brain/UI-UX-AUDIT-2026-10-04.md`; raw evidence and screenshots in
  `artifacts/ui-ux-audit-2026-10-04/`. Independent visual and implementation reviewers completed before synthesis.
- Design health 26/40; technical health 14/20. Ten accepted groups: P0 0, P1 1, P2 8, P3 1. Highest priority:
  illustrative key agreement must not imply official correctness or explanation safety. Other priorities:
  phone journey/feature repetition, result mascot overlap and split percentage, touch/keyboard semantics.
- Homepage checked at widths 320/360/390/430/768/1024/1440/1920; all observed MockMob global widths fit.
  Public pages, 15 student fixture views, both themes, live home/signup and three live competitors sampled.
  Initial profile/test loading frames are not full-state verification. Incorrectly labelled initial desktop rows
  are retained as provenance and excluded; corrected 1440 measurements are the desktop evidence.
- Sampled answer feedback/focus, menu Escape, tour ArrowRight, timed palette, malformed email without sending,
  and long-name/empty/error fixtures. Contrast sampling had no eligible content-text failures within its limited
  coverage; gradients/animation and other unsupported cases were skipped. No whole-site WCAG certification.
- Detector ran once: 137 raw alerts, largely contextual advisories; no bulk theme/runner normalization warranted.
  Current aiCommerce=true supersedes the older closed-top-up assessment; target-size equivalent-control exception
  prevents declaring a definitive WCAG failure from dots alone. Both reconciliations are explicit in the report.
- No UI code changes, tests/builds, paid model calls, real attempts, migrations, auth completion, emails, payments or
  deploys performed. Existing dirty tree/dev server preserved. Audit tabs and temporary viewport overrides cleaned up.
- Open gates: real phone keyboards/safe areas, screen reader, 200% text zoom, full hover/focus/reduced-motion matrix,
  background interruption and budget-device/slow-network performance; authenticated persistence/payments/AI receipts.
  Live landing differs from local; this audit does not establish deployment of the new feature tour or configured AI.

### 4 October 2026 — owner-selected UI/UX implementation plan

- Saved `UI-UX-IMPLEMENTATION-PLAN-2026-10-04.md` and linked it from the brain README/audit.
  Owner retains official-key trust wording; wording-first audit priority is superseded for this sprint.
- Order: reproducible baseline → phone performance/composition → accessibility → student/error states
  → activation flow → final measurement and release evidence. Cosmetic detector cleanup, unused demos,
  arbitrary competitor page-height targets and blanket motion/feature removal are excluded/deferred.
- Current source review found held/not-explained repair outcomes enter the Result `repaired` set, which
  drives a Repaired badge. Plan requires fixture reproduction and separate handled/outcome states;
  no runtime reproduction or fix is claimed in this planning pass.
- Planning only: no UI edits, performance runs, tests, paid calls, migration or deployment performed.
  Performance acceptance separates controlled production-build traces from real-user Core Web Vitals.

### 4 October 2026 — UI/UX plan implementation

- Implemented phone hero/sample composition; tour carousel controls, inert slides, focus/manual pause,
  bounded pausable demo timelines, hidden/offscreen gating and 44px controls; official-key wording retained.
- Practice setup now precedes supplementary commentary/statistics and no longer waits for optional panel
  reads. Pending/unavailable counts are explicit; matching/expiry/idempotent server quote guards remain.
  Scoped load retry retains choices; phone summary exposes subject, mode, count, time, marking and cost.
- Result mascot height/entrance and metric units fixed; distinct explanation/held/unexplained outcomes,
  handled queue vs explanation progress, retained visited answer state across collapse/filter, and safe
  same-ID retry/in-progress/released handling. No scoring, wallet, model, budget or entitlement changes.
- DU category arrows/Home/End and clear focus fixed; editable phone/tablet fields 16px; key targets 44px;
  transform progress bars; one main in timed runner and PrepOS.
- Baseline/final production builds and final lint passed; 179 tests passed (35 recovery, 80 learning,
  59 payment/question/NTA/DU, 5 new UI state tests). Final key-route light 320/390/768/1440 and dark
  320/390/1440 matrices have zero horizontal overflow and no result mascot/metric overlap.
  Fixtures cover distinct repair outcomes, pending/error states and retained held panels. Browser
  checked DU keyboard, menu Escape focus return, sample feedback, tour freeze and one-main wrappers.
- Local production preview on 3020 checked public home, themes and sample; existing authenticated
  setup was read-only. Signup redirected to setup, so current-run native email validation is unverified.
  No new real session/paid repair/payment/signup completion, data migration or deploy performed.
- Several local inventory reads took 7.5-11s and had blocked setup; dependency removed and tested with
  never-resolving-statistics fixture. No device speedup, Core Web Vitals or field gains claimed.
- Full evidence/open gates: UI-UX-IMPLEMENTATION-RESULTS-2026-10-04.md and
  artifacts/ui-ux-implementation-2026-10-04/. Physical phone, screen reader, actual 200% zoom,
  reduced-motion browser/full contrast matrix, controlled throttled traces/field CWV, real transaction
  receipts and production deployment remain open. Measurements cannot be replaced with screenshots.
- Existing checkout changes retained. Diff check only reported the pre-existing ProductScreens.jsx EOF
  blank line. Do not bulk-reset/revert these files; review the scoped implementation hunks.

### 4 October 2026 — authorized UI production release preflight

- Owner requested publication of the UI changes. The staged release includes the reviewed landing/tour,
  mobile/accessibility, dashboard, result/repair presentation and DU refinements with their source dependencies.
- Existing AI-routing/moderation, aiCommerce enablement, pricing, payment scripts and corresponding
  backend-test edits are excluded and retained locally. This release does not activate new commerce,
  change model routing, migrate data or call a paid model.
- Exact staged source tree `7cfe2abf1d958767fb32f5bcd270560900cddd58` was exported independently:
  production build and lint passed, with 179/179 recovery/learning/payment/question/NTA/DU/UI-state tests.
  Evidence: `artifacts/ui-ux-release-2026-10-04/`. Shared dependency junction was rejected by Turbopack;
  the successful build used a real dependency copy. No application workaround was introduced.
- Push/Vercel readiness and live-domain/mobile/desktop smoke are pending at this preflight entry.
  Hardware, screen-reader, measured throttled performance/CWV and real transaction gates remain open.

### 4 October 2026 — UI release live verification

- Pushed `f70e385909ff454f10bf83e60d96a6883bb31c17` to `origin/main`. `Vercel – mockmob`
  reached success at `2026-10-04T12:50:34Z`; deployment:
  https://vercel.com/atishay07s-projects/mockmob/6VA6xyZTYuXB87urHXQLAgeusbAx.
- `https://www.mockmob.in/` serves the new tour, short hero lead and sample CTA with HTTP 200.
  Apex redirects once (307) to www, then 200. Calculator returns 200; no redirect loop.
- Live home light/dark checks at 320/390/1440px: no horizontal overflow, one main.
  Sample CANDID/Frank feedback works; selecting Mistake Repair pauses the tour with one active,
  seven inert slides and 44x44px controls. Live calculator at 390px: category ArrowRight selects
  and focuses OBC-NCL with one tab stop; clear empties search, restores focus, and input is 16px.
  No captured browser error logs in this smoke. Phone and desktop screenshots saved.
- Evidence: `artifacts/ui-ux-release-2026-10-04/{github-status.json,live-http.json,live-ui.json}`
  and build/test/lint logs. This post-deployment receipt is a local status update; deployed source
  and preflight documentation are in the release commit above.
- Existing unrelated AI/commerce/payment edits remain local. No production migration, paid model
  call, real attempt, purchase or signup completion was performed. Physical devices, screen reader,
  actual zoom, controlled performance/field CWV and real accounting receipts remain unresolved.

### 4 October 2026 — guided tour follow-up

- Owner rejected the phone dropdown and easily interrupted/slow feature playback after the UI
  publication. Rebuilt the tour as an automatic 4.8-second chapter sequence with shared progress,
  explicit Pause, a chapter strip and an Up next nudge. Normal vertical browsing no longer turns
  rotation off. Pointer navigation resumes its cycle; horizontal input holds briefly while settling.
- Preserved keyboard reading holds, explicit resume, reduced motion, inactive-slide isolation and
  hidden/offscreen suspension. Phone product panels fit without overhang; the sample dock steps
  aside during the tour. Nearby Mistake Lab stages also use 4.8 seconds. Official-key copy retained.
- Final isolated application source build and lint passed; nine relevant tests passed. Both-theme
  320/390/768/1024/1440 matrices have zero root overflow, no screen overhang and 44px controls.
  Browser observed auto progression/loopback, scrolling/navigation without sticky pause, explicit
  pause, and keyboard hold/resume. No measured wall-clock/FPS/device performance claim.
- See `TOUR-REFINEMENT-2026-10-04.md` and `artifacts/tour-refinement-2026-10-04/` for details.
  Production readiness/live smoke pending at this entry. Physical phones, screen reader and CWV
  gates remain open. Unrelated AI/commerce/payment edits retained locally; no migration/paid call.

### 4 October 2026 — connected preparation suite verified for rollout

- Implemented shared Today sequence, Learn, server-scheduled Recall, durable versioned runs/events,
  separate study progress, selected subjects/time, Pro weekly plans and custom mixed recall.
  Mobile Today/Practice/Learn/Review retains the other destinations through More. Active sessions
  and due checks replace their plan blocks; a persistent full-mock shortcut retains the existing
  quote/eligibility/credit path. Teaching/card exposure excludes those families from fresh checks.
- Owner explicitly authorized current Supabase project `isrxrxzjocewrdureyhp` with existing data.
  Saved migrations and isolated dry runs preceded SQL-editor application of score-recovery,
  connected-learning and study foundations; the published-version backlog follow-up also applied.
  The original transaction verified existing questions/attempts/credits/entitlements/credit receipts
  unchanged. Current service-role retry/scheduling/stale-revision smoke passed and rolled back all
  verification writes. CLI migration history remains unreconciled; do not blindly reapply pending SQL.
- Published two units and 23 cards: English twenty-word deck and sacrificing/gaining ratios.
  Canonical hashes and anonymous table denial verified against the current project. WordNet license
  preserved; NCERT formula/source reconciliation and exact arithmetic passed. This does not release
  formal recovery pathways or certify academic calibration, exam fit, mastery or score gains.
  Remaining four-subject coverage is visibly pending; offline packs and curriculum expansion remain.
- Clean isolated release excludes owner's unfinished pricing/provider/AI-evaluation/payment-script/
  landing edits. Lint and production build passed. 166 distinct tests passed: recovery 35, learning
  80, answer integrity 6, NTA 22, payment entitlements 12, study 11. Final plan changes passed study
  tests again; final mock/lesson links passed targeted lint and production rebuild. Complete local
  four-migration/import/retry/runtime dry run passed. Authenticated browser saved/resumed/completed
  the English lesson, persisted/reloaded a recall rating and saved/restored time preferences.
- No paid model calls. Existing Free/Pro prices, entitlements, atomic credit RPCs and AI allowances/
  persistent $50 generation and $25 monthly runtime guards unchanged. Only three independent study
  flags were saved as true in production on the domain-verified Vercel `mockmob` project.
  Publication/live verification pending at this entry; local build is not proof of deployment.
- See `STUDY-SUITE-2026-10-04.md` and local `artifacts/study-suite/` receipts. Real Android/keyboard,
  screen reader, actual 200% text/zoom/reduced-motion settings, field CWV and delayed unseen-question
  outcomes remain unverified. Rollback disables study flags and retains learning records.

### 4 October 2026 — preparation suite published

- Commit `a6a61cc276d9df36b43e4760c08df0dfe83802a3` is on `origin/main`.
  Domain-verified Vercel project `mockmob` deployment is Ready:
  https://vercel.com/atishay07s-projects/mockmob/FeimHt2rAGpA3qG4Eepoqfa43PNJ.
  Vercel showed 49 seconds and 23:21:17 IST on 4 October. Production flags are enabled.
- Live HTTP smoke passed: apex 307 once to www then 200; www and Learn 200; anonymous
  study catalog 401; dev-only study preview 404. Public Learn redirects signed-out users
  through existing authentication. Live signed-in browser check awaits owner Google sign-in;
  the Google chooser shows the existing account signed out. No credential was generated,
  transferred from localhost or changed to bypass login.
- Authenticated current-project readback passed: English lesson complete, recall cursor one
  after the first card, answer hidden on the next card, one persisted FSRS review whose due
  date matches the run receipt, and original twenty-minute preference restored. Actual
  owner QA records remain resumable; they are not student outcome evidence.
- Final authenticated release library and recall checks across 320/390/768/1024/1440 plus
  short landscape showed zero root overflow and no study buttons/links below 44px. Dark
  phone library also had no overflow. Full-mock shortcut selected the existing Full Mock
  and displayed its access quote without starting or charging a practice session.
- Evidence: `artifacts/study-suite/{production-release-receipt.json,production-deployed.png,
  live-http.json,authenticated-study-receipt.json,responsive-release-library.json,
  responsive-release-recall.json,phone-library-dark.png}`. This post-release receipt remains
  local; application source and pre-release verification status are already published.
- Original dirty checkout and unrelated owner edits remain intact; release checkout/branch is
  `artifacts/study-suite/release` / `codex/connected-study-suite`. Original local main still
  points at its prior commit; reconcile intentionally before later publishing owner edits.
  Full curriculum/offline packs, formal calibration, CLI migration-history reconciliation,
  physical-device/assistive-technology/200%-zoom and field performance/outcome gates remain open.


### 4 October 2026 — signed-in preparation-suite production smoke passed

- Owner completed normal Google sign-in. Live library rendered both English and Accountancy
  units, existing Pro access, the completed lesson and recall progress. The existing recall run
  resumed at card two. A live reveal was saved and survived page reload; its answer, optional
  pronunciation, linked lesson and four rating controls rendered correctly. No scored session,
  practice-credit charge, purchased-entitlement change or paid AI call was made.
- Actual live library viewport checks passed at 320/390/768/1024/1440 and short landscape.
  Revealed recall passed at 320/390/1440 and short landscape. Each measurement asserted actual
  width/height, zero root overflow and no study buttons/links below 44px. No error logs were
  captured in the final live test tab. Earlier viewport results that targeted the build-queue
  tab were discarded and replaced with these measurements; they are not release evidence.
- Evidence: `live-responsive-library.json`, `live-responsive-recall.json`, `live-phone-library.png`,
  `live-phone-recall.png` and updated `production-release-receipt.json` in `artifacts/study-suite/`.
  Physical-device, assistive-technology, actual zoom/reduced-motion, field performance and
  curriculum/calibration/offline/history-reconciliation gates listed above remain open.


- Final signed-in live Today showed the same resumable study run, twenty-minute preference and
  the 4/6/10-minute sequence plus full-mock shortcut. Temporary viewport overrides were reset.


### 5 October 2026 — Learn rebuilt as one connected loop; content v2 across four subjects

Owner feedback: "Even I cannot understand what Learn actually does." Diagnosis from the live/local walk-through:
Learn opened on "Start recall" before anything was taught; the English "lesson" taught the recall method and no
words; cards were bare dictionary definitions; lesson completion did not lead to recall or practice; starting a
second lesson silently resumed the first (the database resumes any active run of the same mode).

What changed (branch `codex/connected-study-suite`, on top of a6a61cc):
- One loop per concept, stated everywhere: **Learn (5–7 min) → Lock it in (2–3 min recall) → Apply (chapter
  practice with marks)**. Learn home gives one next action (continue / due review / recommended lesson, subjects
  rotated by fewest lessons read or by recent practice mistakes), then subject → chapter → concept with status,
  "practice available, lessons later" for untaught chapters, study record and mock shortcut.
- Lesson overview: objectives ("You'll be able to"), "How CUET asks this", three-step status, contents, sources.
- Lessons: idea, formula, method, worked example tables, common-mistake callouts, word sets with WordNet examples,
  numbered practice passages; quick checks with per-option "why that is wrong" feedback. Completion screen offers
  Lock it in (that lesson's cards), then Practise <chapter> (`/dashboard?subject&chapter&mode=quick&count=10`).
- Recall: one card = one memory with rotating task variants (meaning in context, gap fill/spelling, synonym or
  opposite; numeric/ratio calculations; scenario classification). Answers checked exactly (equivalent fractions,
  ratios in lowest terms, ₹/commas, British/US spelling from the source). After each card: when it returns.
  Summary lists remembered/forgot with next review, reread links and the Apply step.
- Server: `set_aside` transition closes an older active session (history kept, nothing introduced) when a
  different lesson or focused recall starts; same request resumes. Per-unit memory status, lock-in availability,
  explicit `DAILY_NEW_LIMIT_REACHED` / `NOTHING_DUE`. Unchanged: 5 new cards per IST day, >20 overdue pauses new
  cards, FSRS 5.4.2 defaults at 0.90, append-only events, revision checks, DB-enforced daily limit, RLS/grants.
- Today steps carry purpose, minutes and what "done" means; practice step links the recommended chapter.
  Result page Repair step links every mistaken chapter that has a lesson (count + minutes). Review/Progress
  study card reworded. Homepage tour gains a flag-gated Learn slide; its counts come from `release.json`.

Content v2 (released 14 units / 65 cards / 179 task variants; zero paid model calls):
| Subject | Units | Chapters with lessons |
| --- | --- | --- |
| English | 6 vocabulary sets (30 WordNet words; 10 new) + main idea + stated/inferred | Vocabulary, Factual Passage, Narrative Passage (3 of 7) |
| Accountancy | sacrificing/gaining ratios (v2), revaluation | Change in Profit Sharing Ratio, Admission of Partner (2 of 16) |
| Business Studies | delegation/decentralisation, planning/controlling | Organising, Controlling (2 of 13) |
| Economics | what GDP counts (final goods, value added, GVA/NVA, non-monetary), nominal/real/deflator | National Income & Related Aggregates (1 of 18) |
All eight concept blueprints now have teaching units. This is **not** full syllabus coverage and does not release
formal recovery pathways or assessment families.

Validation (`scripts/learning/validate-study-content.mjs --write --strict`): every number recomputed
independently; WordNet meanings/examples/synonyms/antonyms re-derived from hashed source lines (licence kept);
NCERT reconciliation phrases found on cited PDF pages (leac102 p.3,5,6,30,31; leac103 p.3; leec102 p.3,10,21,23;
lebs105 p.20,26; lebs108 p.5,6,8; PDFs downloaded with owner approval, sha256 in registry, git-ignored);
original reading passages checked for evidence/not-stated/key structure; family IDs disjoint from recovery
pathways. Tamper tests prove changed arithmetic, definitions, relations, reading keys and answer keys quarantine.

Production data (owner-authorised project isrxrxzjocewrdureyhp): phase 1 insert-only applied 5 Oct via
`scripts/learning/apply-study-content-v2.mjs insert` after the PGlite dry run
(`artifacts/study-suite/content-v2-import-dry-run-report.json`: idempotent, invisible to old code, changed
same-version content refused, supersede quarantines not deletes, stale run invalidated with event, unrelated
data unchanged). Receipt: 14/14 units, 65/65 cards present and hash-matched. Phase 2 (`supersede`, retires
english-vocabulary-01@1 and accountancy-sacrificing-gaining@1) runs only after the v2 deploy is live.

Verification (local, release checkout): tests recovery 35, learning 80, study 19, answer-integrity 6, NTA 22,
payment entitlements 12, landing/UI 9 — all pass; full lint clean; production build passes. Fixture walk-through
(dev-only `/preview/study`, real engine and scheduler) and **owner-signed-in walk-through on production data**
on localhost: revaluation lesson resumed at step 3 after reload; triple click advanced one step; stale second-tab
event returned 409 with server state unchanged; wrong choice explained; "₹3,000" accepted; completion → Lock in 5
cards → summary with next review times → reread link → practice opened with Accountancy / Admission of Partner
preselected and "Included" (nothing started or charged); different lesson set the earlier one aside, same lesson
resumed; Today led with the unfinished lesson. 320 px library/overview/lesson: zero overflow, no study targets
<44 px; wide comparison tables stack on phones. Both themes checked. These are owner QA records, not student
outcome evidence.

Still open: real budget Android with keyboard, physical screen reader, actual 200% zoom/OS reduced motion, field
Core Web Vitals, delayed unseen-question outcomes, comprehension testing with real students, offline packs
(print summary only), remaining chapters, CLI migration-history reconciliation. Device TTS pronunciation is
labelled as device voice; no licensed pronunciation source is bundled.

Rollback: set STUDY_CONTENT_ENABLED/STUDY_RECALL_ENABLED/STUDY_GUIDED_PLAN_ENABLED to false and redeploy (records
kept), or `git revert` the release commit and redeploy. If phase 2 has run and the old code is restored, set the
two v1 units back to `published` (no deletes are needed; v2 rows are ignored by the old release proof).

### 5 October 2026 — Learn v2 published

- Commit `78a627f` pushed to `origin/main`; www.mockmob.in served it about 80 s later. Live HTTP: home 200 with
  the flag-gated Learn tour slide, `/learn` 200, anonymous study catalog 401, dev preview 404.
- Content phase 2 applied after the deploy: english-vocabulary-01@1 and accountancy-sacrificing-gaining@1
  quarantined (v2 published); the correction trigger invalidated the 5 owner QA runs on v1, one event each; no
  deletes. Receipts: `artifacts/study-suite/v2/apply-{insert,supersede}-receipt.json`, `live-receipt.json`.
- Signed-in live check (owner Pro account, 375px): Learn led with the unfinished lesson and due cards; the
  lesson completed with check feedback and the daily new-card limit message; Organising practice linked.
- Local `main` in the original checkout still points at 6c5e05b with the owner's uncommitted work; it is now
  three commits behind `origin/main`. Reconcile deliberately before publishing those edits.

## 5 Oct 2026: Key Review + NTA integrity guard + Luna routing
- Key Review: when Mistake Repair's solve and blind second check both disagree with the key, the student sees an
  acknowledgement ("We may have got this one wrong") with who picked what, plus a result-page log of held keys.
  A reload shows the same panel via `question_under_review`. Marks are NOT changed automatically; copy says so.
  No migration, no extra model calls.
- NTA integrity guard: leaving the tab/window = strike; warnings 1-2 show an animated modal, strike 3 submits the
  session. Strikes persist across reload (`<session key>:integrity`); copy/paste/context menu blocked. Browser-side
  deterrent only: strikes are NOT sent to the server (attempt events accept only answer/visit), so there is no
  server-verified proctoring record.
- Also shipped: GPT-6 Luna-only model routing (providers.js, moderation/ai.js, live-eval scripts).
- Deliberately NOT shipped: AI top-up opening (RELEASE_GATES.aiCommerce, pricing pages) from the local tree; needs an explicit owner go-ahead and Razorpay keys.
- Verified: unit tests and eslint (see commit); preview walkthrough of both flows. Not verified: real multi-window/mobile
  app-switch behaviour, signed-in NTA run, live Luna calls.

## 6 Oct 2026: Key Review / NTA release verification
- Prepared an isolated normal checkout from 82d3341 (base origin/main 23ac1dd), preserving the owner's dirty main checkout.
- The handoff commit omitted seven new component/data/test files plus package.json and this status entry. Recovered these exact files from the handoff worktree; no AI commerce, pricing, artifacts, study-suite edits or migration included.
- Removed a duplicate question_under_review response handler; corrected the illustrative held-response fixture so both checks actually disagree with its key.
- Actual checks: npm run build passed with physical node_modules (Next.js 16.2.4 / Turbopack); eslint passed; test:learning 84/84, test:recovery 35/35, answer-integrity plus payment-entitlements 18/18 passed. No paid-model invocation or production-data migration performed.
- Earlier preview interaction evidence is from the handoff, not repeated in this release check. Browser-only strikes are not a server proctoring record. After reload, Key Review is returned on a repair request for the already-held question; the result-page log is rebuilt from those responses.
- Deployment is pending the non-forced main push and Vercel verification. Live Luna compatibility, signed-in NTA, real mobile/multi-window focus behaviour and captured AI top-up checkout remain unverified. AI top-up purchasing remains closed.
- Rollback: revert the feature commit and release-completion commit; no database rollback is needed.
### Production publication evidence (6 Oct 2026)
- Published 82d3341 plus completion commit d2e3f2b to GitHub main by non-forced fast-forward from 23ac1dd.
- GitHub check `Vercel – mockmob` succeeded for d2e3f2b. Production deployment 6868841235 succeeded at https://mockmob-9stt6no29-atishay07s-projects.vercel.app (Vercel dashboard: https://vercel.com/atishay07s-projects/mockmob/BXoio53KjaFuPBdUUJ49fc4Sqnxc).
- Post-deploy live checks: apex https://mockmob.in redirects to https://www.mockmob.in/ with final HTTP 200; www homepage and /pricing return 200; unsigned /test redirects to /signup with final 200. No redirect loop observed.
- These checks confirm production publication and public entry routes; they do not prove authenticated Key Review/NTA interactions, physical-device focus handling, live model compatibility or payment capture. Those gates remain as recorded above. Other duplicate Vercel projects attached to the repo are outside this live-domain release verification.

## 6 Oct 2026: corrective NTA fullscreen and answer-change audit
- Owner reported that fullscreen rehearsal and confirmed-key correction UX were incomplete. Audit and source-backed question findings: docs/brain/reports/KEY-REVIEW-NTA-CORRECTIVE-AUDIT-2026-10-06.md.
- NTA now requests actual fullscreen, requires re-entry after warnings, counts one absence once, persists strikes per session, submits on warning 3, removes the in-app Exit shortcut, locks answering behind native themed dialogs and exposes failed-submission retry. Browser/OS exits remain possible; unsupported browsers disclose a focus-only fallback. Timer deadlines are unchanged.
- Results now hydrate changed/held questions from current server records on reload. Confirmed corrections show an apology, corrected answer/explanation/source and separate marks adjustment; unverified changes do not claim correctness. Old snapshots/account/leaderboard scores remain intact. No paid model calls on reading corrections.
- Exact screenshot question is already D in production (dea6e298-269e-4b18-afd4-53c0b3be7cf5). Source-backed matching display receipt confirms D; pick B stays wrong, adjustment 0. No production data update or migration performed. The historical A-to-D change has no returned version-history receipt, so its timing/provenance is not claimed.
- Verified: learning 91/91, recovery 35/35, answer-integrity/payment-entitlements 18/18, eslint and production build. Isolated Chrome exercised real fullscreen entry/exits, warning progression, reload persistence, auto-submit, failure/retry, denial, and Quick Practice. Desktop/390px mobile compositions inspected; controlled visibility/blur events reached the real hook. JSON/screenshots retained locally in artifacts/corrective-checks/.
- Remaining: corrective deployment verification, signed-in production result/NTA, real OS/tab/window switching, physical phones, screen readers and live Luna. A real headless tab switch did not expose focus change; synthetic events are not hardware proof. Strikes remain browser-only. AI commerce stays closed; entitlements and atomic RPCs untouched.
- Rollback: revert the corrective code commit. No database rollback needed.

### 2026-10-19 — Play reviewer account given Pro (production, owner request D131/D133)
- Account review.mockmob@gmail.com (users.id 1cbee7ed-f731-4d33-b568-6b48a9fa758b), created and password set by the owner, used in Play Console "Sign-in details" for Google's reviewers.
- Before: is_premium false, subscription_status 'free', premium_until null. After: true, 'active', 2027-07-31T18:29:59.999Z (the Pro CUET 2027 end).
- Undo: `update public.users set is_premium=false, subscription_status='free', premium_until=null where id='1cbee7ed-f731-4d33-b568-6b48a9fa758b';`
- Also confirmed today (read-only): migration 20261018190832 play_purchases is on production since 18 Oct (RLS on, no policies, service-role only, 0 rows; function bodies identical to staging).
