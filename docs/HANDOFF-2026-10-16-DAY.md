# Handoff, 16 Oct 2026 about 12:30 IST (session 604ced81, Claude Opus 5.5 as CEO/CTO)

Read this whole file first, then CTO-LOOP.md, APP-OWNER-LEDGER-2026-10-16.md, and the memory index. Newest owner words win. Nothing here authorizes a push the gates below do not allow.

## 0. The owner's standing rules (his words and decisions, still in force)

**Role, pace and honesty:**
- Act as CEO and CTO. Keep looping with many parallel agents. He measures pace and expects 15-20 agents in parallel when usage allows.
- Give honest percentages. Never repeat an estimate without new evidence.
- Stop at about 95% usage with a handoff like this one.

**Routing** (memory subagent-model-choice):
- Sonnet does the heavy lifting.
- Opus only for complex UI/UX, motion and polish.
- Haiku only for quick, bounded tasks.
- Always set effort explicitly.

**Design:**
- Design agents load these skills: ui-ux-standards, impeccable, frontend-design, emil-design-eng, high-end-visual-design, redesign-existing-projects and design-taste-frontend.
- They follow his research brain: `docs/research/premium-ux-ui-2026-10/AGENT_RULES.md`. Cite evidence IDs, run the 12-part anti-slop test and the 0/1/2 rubric, and write a DESIGN_DECISIONS note per feature.
- Banned: eyebrow pills or dots, glow, gradient text, icon grids, nested cards, arrows on buttons, ALL-CAPS labels, hype copy.
- Mobi appears at most once per screen, and only at a real moment.
- Never simplify by cutting features; he calls that a regression.

**Deploy gates:**
- **Website:** every deploy needs the suites plus a visual critique at 390 and 1440, Night and Day, and an independent verifier pass.
- **Landing:** needs the owner's own look on a local server before launch.
- **App:** NEW RULE from today (memory device-truth-testing). App work is done only after an emulator walk with screenshots against the owner ledger: the upgrade path, keyboard open, scrolling, Night and Day. Goldens alone are never enough. This failure is why his v5/v6 issues survived to v10.

**Security and access:**
- Never drive his browser. Never sign in as him. Never create accounts.
- Use his phone (adb serial 10BF370PA6002XR) only when he says it is connected.
- The emulator gets at most 3 GB RAM. Agents use the project test account `app-e2e-student@example.com` on the local staging site only.

**Database:**
- Production DB work is allowed under his standing grant (14 Oct): save the migration, dry-run on staging, keep an undo file, add a STATUS.md entry.
- He gave a standing OK to hotfix crucial security issues.

**Focus:**
- Product only; marketing waits until January.
- Landing is mobile-first. The arena is desktop-first but must work on phones. The app is mobile only.

## 1. What is live in production now

- **mockmob.in = main 4db57fc5:**
  - Vercel READY, 0 runtime errors after deploy (dpl_DWnHXg8zQArzfPeEK533NjPiQMrT).
  - Batch 1 (09421b29):
    - Mistake Lab slice 4 web: trap tags, Traps you meet, Revise / Same mistakes later;
    - My colleges, Mobi rig v2 web, crash reports, names, Learn concept checks;
    - the arena de-slop;
    - fixes for 78 gate defects.
  - Batch 2 (4db57fc5):
    - Mistake Repair v4: Check it held (a fresh never-seen question, server-marked, no extra credit, first answer counts), "Ask Mobi about Qn" with its cost shown first, the Revise hand-off;
    - the older-paper Lab line, marked-for-review in the SWOT and plan;
    - the practice-progress chunking fix (Accountancy history above about 700 ids was silently ignored);
    - nta_question_index upkeep code, inert without the key and table;
    - the Rs 99 monthly switch, inert until `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set, with honest pricing copy ("one payment of ₹99, not a subscription");
    - the Pro modal moved above the app chrome.
  - vercel.json now has 2 crons. The nightly index rebuild rides on /api/internal/refresh-inventory.
- **Production DB isrxrxzjocewrdureyhp, applied today under the grant, logged in STATUS.md with undo files:**
  - trap_atlas, revise_cards, my_colleges, app_errors, funnel_daily: all RLS on, service role only.
  - question_option_stats with refresh_question_option_stats v2 (slice 5). The v1 refresh timed out; v2 rebuilt the table in 13 s: 461 questions, 13,877 first answers, 0 timed answers so far, so every cohort-time line stays hidden by design. The nightly pass that keeps it fresh ships with batch 3.
- **NOT verified live:** Check it held, the receipt->check and receipt->offered PostgREST claims. Agents cannot sign in. The owner will take a fresh timed mock and do one repair. Watch Vercel runtime errors on /api/recovery/check after he does.

## 2. Work in flight at handoff (workflows die with this session; check each)

| What | Where (worktree, branch) | State at handoff | How to continue |
|---|---|---|---|
| **App owner-ledger build** (the main job) | `wt-owner`, `ui/owner-1016` (from ui/phase2 fd0da7d3) | Workflow wf_bdae83cd-a43: 8 builders were running in parallel (shell/bar plus 7 areas). Next stages: integrate, then emulator walk of L01-L39, then fix, then re-walk, then the release v12 APK | Check `git -C wt-owner log` and `status`; see which areas committed. The script is `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy-wt-owner\604ced81-3aa7-4deb-b42c-f324ca5f51e2\workflows\scripts\app-owner-build-1016-wf_14d6c73f-9d4.js` (keep LF line endings or the Workflow tool refuses it). Re-run only the missing area builders (each prompt is in the script), then the Integrate, Walk, Fix and Release stages |
| **Website batch 3 gate** | `wt-polish`, `deploy/batch-1016c` (main 09421b29 plus slice 5 b9aea401, refresh v2 e1c6ec1a, W1 Mobi moments web, W2 arena pass 2 d8f8d50a, STATUS 7a4fe44e/9b52448d) | Workflow wf_39d20212-193 web half: critics were running, then fixer-c (Opus), then verifier-c | Batch 3 branched from 09421b29, but main is now 4db57fc5. **Merge origin/main into deploy/batch-1016c first.** Known conflict: `src/app/api/internal/refresh-inventory/route.js`; keep both passes, NTA index first, then cohort stats. Then suites, `npx next build --webpack` and the visual gate (or the verifier's verdict if it finished), then push to main and verify Vercel |
| **APK v11** (intermediate) | `wt-phase2` ui/phase2 → `mockmob-next` feat/app-and-web | A4 agent in wf_39d20212-193: full tests, version bump, merge, release build to `mockmob-next/tmp/apk/mockmob-v11-*.apk` | If built, send it to the owner as "intermediate". v12 is the real target |
| **Landing** | `wt-land2`, `web/land2-1015` (HEAD ccf285c3 plus round-7 fixes) | Scores went 76, 82, 84, 87, 88, then 85 (round 6 found new truth defects). Workflow wf_33a37b2f-35b: fixer, then critic, up to rounds 7 and 8 | Read the last critic. If 90 or more, open http://localhost:3122 for the owner (dev server PID 33504, or `npx next dev --webpack -p 3122` in wt-land2) and **deploy only after his OK**: merge into main through a gate |

## 3. The app: what the owner wants (the ledger is the acceptance list)

- **Ledger:** `docs/brain/APP-OWNER-LEDGER-2026-10-16.md`. It has 39 items (L01-L39), 19 of them raised more than once and 10 not built when written. Each has emulator acceptance steps.
- **Design:** `docs/design-decisions/app-ia-1016.md` (IA; the ownership map is section 10), plus `app-today-1016.md`, `app-practice-review-1016.md`, `app-you-1016.md` and `app-tools-1016.md`.
- **Decisions in force (owner sign-off pending; defaults chosen):**
  1. **Bar:** 6 equal slots: Today, Practice, Start (third, lit pill), Review, Colleges, You. All icons, labels and the Start pill share one line.
  2. **Colleges tab:** My colleges, Admission Compass, the cutoff checker sheet, the Combo planner and the guides. Every tool is reachable in 2 taps or fewer. `/tools` redirects to `/colleges`.
  3. **You tab = the student's study:** the week as "3 of 4", 16 badges, personal bests, across your mocks, subjects. Plan and credits shrink to one row at the bottom.
  4. **Avatar sheet = the account:** name, email, plan, both credit balances, theme, notifications showing "Off" with Turn on, privacy, help, sign out.
  5. **Road to May:** a sideways strip of weeks you edit in place. The study-days ring says what it counts.
  6. **Practice:** subjects first, one "Up next" card, then Quick practice, By chapter, Smart practice, then Exam conditions (Full mock, NTA mode).
  7. **Colleges search:** normalises "BCOM", "B.Com", "b com" and "bcom hons", and stays keyboard-safe.
  8. **Onboarding:** includes adding colleges.
  9. **Notifications invite:** returns until notifications are on, and never appears inside a paper.
- **Owner answers today:** "Review again" meant the Review tab saying "We could not load your mistakes" (now fixed, see below). "Interview mode" = NTA mode.
- **Root-cause fix today (device-proven with a diagnostic build on his phone):** dio returns decoded JSON even with ResponseType.plain, so every `plainBody` call got an empty text. That broke the Today card ("Could not reach MockMob") for every account, the Review tab, and the DU college catalogue behind My colleges search.
  - Fixed in `core/api/api_client.dart` with test `test/unit/core_data/api_plain_body_test.dart`: fd3fca29 on feat/app-and-web, 3887e786 on ui/phase2.
  - v10.1 (v10 plus the fix) was sent to the owner: `tmp/apk/mockmob-v10.1-fd3fca29.zip`. Not device-verified after the fix; the phone was unplugged.
- **Also in the app since v10:**
  - 7501acf9: phase2b, My colleges, critic packets D and E;
  - a8252ca4: Repair v4 in the app;
  - 35d9fa49: slice 5 in the app;
  - dd5a1500: honest attempts failure states;
  - fd0da7d3: Mobi at real moments, one per screen;
  - 3a8968a1: the play-prep merge.
- **Emulator walk rig** (written in the build script):
  1. Wait for 4 GB of free RAM, then start the AVD with at most 3 GB (`-memory 3072`).
  2. Run the local staging site from `wt-batch` with `node scripts/pipeline/tools/stagingLocalApp.mjs` (port 3101), then `adb -e reverse tcp:3101 tcp:3101`.
  3. Build the debug APK with `--dart-define-from-file=dart_defines/phone.json` (package in.mockmob.app.debug).
  4. Sign in with the test-account code from `node --use-system-ca scripts/dev/staging-otp.mjs app-e2e-student@example.com`.
  5. Upgrade test: install a fd0da7d3 build first, then the new one with `install -r`.
  6. Downscale screenshots to 540 px and open every one.
- **Release command** (HANDOFF-2026-10-15-FULL section 5): in mockmob-next/flutter_app, `MOCKMOB_FLUTTER_SLOTS=3 bash tool/flutter_locked.sh build apk --release --target-platform android-arm64 --obfuscate --split-debug-info=build/symbols --dart-define-from-file=dart_defines/prod.json`. Version bump script from play-prep: versionCode is still 1.

## 4. Owner items (tonight; reminder scheduled for 21:00 IST)

1. **Razorpay:** create the Rs 99 monthly plan in TEST mode first, then set `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` in Vercel.
   - Webhook events: subscription.authenticated, activated, charged, pending, halted, paused, resumed, cancelled, completed, payment.captured, payment.failed.
   - Runbook: RUNBOOK-MONTHLY-BILLING-2026-10-16.md.
   - Decide the 6 lapsed-premium accounts.
   - Vercel Pro is needed when payments go live.
2. **Backup:** set `SUPABASE_DB_URL` (session pooler string) and install PostgreSQL client tools 17 or later. Runbook: RUNBOOK-WEEKLY-BACKUP-2026-10-16.md.
3. **Play:**
   - Create the developer account and run `tool\make_upload_key.ps1` with an agent.
   - Put the Web client ID in prod.json; add SHA-1 and SHA-256 after the first upload.
   - Recruit 12-20 testers.
   - Guide: PLAY-RELEASE-2026-10-16.md on wt-play.
4. **NTA index:** `CUET_EVIDENCE_SIGNING_KEY` in Vercel. After that, apply `20261013190000_nta_question_index.sql` under the grant and run `scripts/nta-index-build.mjs --write --allow-production` once.
5. **Funnel:** decide on `FUNNEL_ENABLED=true`.
6. **Testing he will do:**
   - a fresh timed mock plus one repair, which verifies Repair v4 live and fills the Lab;
   - his look at the landing on a local server;
   - the bar, tab-name and study-days sign-off questions (section 3).

## 5. Next steps, in order

1. Check the four in-flight items (section 2) and finish each.
2. **App:** finish the build, then integrate, then walk all 39 items on the emulator, then fix, then re-walk, then release v12.
   - Send v12 with a per-item list: item, pass or fail, screenshot path.
   - Install on his phone only when he says it is connected.
3. **Website batch 3:** merge main in first, then gate, then push.
4. **Landing:** reach 90 or more, then his local look, then a gated merge into main.
5. **Owner production steps** (section 4) once he has done his parts. Run the Razorpay TEST purchase per the runbook.
6. **Doubling down on the strengths:**
   - Get every tester through one timed mock. The Lab and the cohort time need volume; only 8 timed papers exist.
   - Make Repair v4 the hero of the landing and of the app's first run.
   - Keep honest numbers everywhere.
7. **Still open from the vision** (VISION-INVENTORY-2026-10-16.md):
   - anchor questions in NTA papers (owner decision, deferred);
   - landing calm-down Q13 (partly done by the de-slop rounds);
   - the Revise "It held" and "3 weeks in a row" badges need server events;
   - the website Rival result reveal has no Mobi yet;
   - the key-quality loop: apply only the 5 questions with the 20-pick gap after official key review (needs his decision).

## 6. Honest progress (16 Oct about 12:30)

- **Website:** about 85% live. Batch 3 and the landing remain.
- **Mistake Lab v4:** slices 1-4 and Repair v4 are live, and slice 5 has data but its code is in batch 3. About 90%.
- **App:** about 60% of what the owner expects. The core screens work after today's network fix, but the 39-item ledger (bar, Colleges tab, You, Road to May, Practice order, Compass) is mid-build and not device-verified.
- **Overall:** about 75% built, about 65% live.

## 7. Pitfalls learned today

- **Local builds:** run `npx next build --webpack` and `next dev --webpack`. Turbopack rejects the node_modules junction. Vercel builds normally.
- **Workflow scripts:** writing them with Python on Windows adds CRLF, and the Workflow tool then refuses the script ("control characters"). Write with newline='' or convert to LF.
- **Empty path lists:** `git checkout <rev> -- $EMPTY` with an empty list checks out the commit (detached HEAD). Guard path lists.
- **Crons:** Vercel allows 3 crons; batch 2 uses 2. Ride new nightly work on refresh-inventory.
- **Cohort SQL:** must be checked at production volume (1,815 attempts, 35k answers). v1 looked fine on tiny staging data and timed out on production.
- **Test fakes:** must mirror real content types. The plainBody bug hid because test fakes returned plain strings.
- **App walk:** test the upgrade path from the previous APK, not only fresh installs.

## 8. State at the stop (16 Oct about 12:45 IST; all workflows stopped at the owner's request, 96% usage)

**Every agent was killed mid-work. Nothing below is verified.**

| Worktree | State |
|---|---|
| **wt-owner** (`ui/owner-1016`) | WIP commit **3a8bf5ba** holds the partial owner-ledger app build, 115 files, none checked. **Not analyzed, not tested.** |
| **wt-polish** (`deploy/batch-1016c`) | Clean at **1217aeb6**: W1 Mobi moments web plus W2 arena pass 2, slice 5 and refresh v2. **The batch 3 gate did not finish** (critics, fixer and verifier never completed). |
| **wt-land2** (`web/land2-1015`) | WIP commit **a7a63e8d** holds the partial round-7 fixes for the critic-6 findings. Last finished score: **85** (round 6). |
| **wt-phase2** (`ui/phase2`) | fd0da7d3 plus one uncommitted test file (`flutter_test/widget_test.dart`) from the stopped v11 agent; review or discard it. **APK v11 was not built.** Skip it and build v12 after the owner-ledger work. |
| **mockmob-next** (`feat/app-and-web`) | This handoff, the ledger and the design briefs, all committed. |

**What the stop changes in the plan:**
- **wt-owner WIP:** the shell/bar and every area left partial edits. They include:
  - router and app_shell, bar files;
  - practice, today `road_weeks`, the you hub `study_sections`, rhythm badges;
  - tools `college_search` and `estimate`, review `again/` and `retry_first`;
  - onboarding colleges, the notifications invite.
- **Next session, app:**
  1. Run `flutter analyze` and the unit tests on wt-owner first.
  2. List, per area, what is complete against its brief.
  3. Relaunch builders only for the gaps, each told to continue from the WIP.
  4. Then integrate, walk on the emulator, fix and release.
- **Next session, batch 3:** merge origin/main (4db57fc5) into deploy/batch-1016c, then run the full gate.
- **Next session, landing:** check the WIP against the critic-6 list (dead phone links in the tour, one consistent sample student, the repeated changed-answer moment, the desktop type scale, honest Free pricing copy, product names), then run a critic round.
- **Dev servers** may still hold RAM: ports 3122 (landing), 3180 (polish) and others. Stop the ones you do not need.

## 9. Evening update (16 Oct about 11:20 pm, session 604ced81, after the crashed session cc0bf1af and two restarts)

### Live now
- **mockmob.in = main 8a0141ba (batches 1-3).** Vercel READY, 0 runtime errors.
  - Batch 3 adds: slice 5 cohort time (its lines stay hidden until enough timed students exist), Mobi moments on the website, Progress, Review and Weak chapters improved, the NTA index signature fix, and the homepage bank line.
- **Production DB, applied tonight under the standing grant** (STATUS entries on branch db/status-1016e: 4a7c204c, 63bfd822, ea40b6ad):
  - submit_rival_battle (was missing; dry-run proven in a rolled-back transaction);
  - mm_leaderboard();
  - least privilege for the browser roles;
  - pinned search_path on 17 functions;
  - the payments policy in initplan form;
  - the NTA index rebuilt (653 rows, **0 signature failures**, verified with scripts/nta-engine-run.mjs).
- **English NTA** refuses a full paper (34 too few high-score questions). That is a content gap, unchanged since 13 Oct.

### In flight at handoff (check each with its journal; resume with Workflow({scriptPath, resumeFromRunId}) in the same session, otherwise relaunch the missing agents)
- **wave-0935pm (wf_967ff020-5e0)**, script in the session's workflows/scripts:
  - **Batch 4** on wt-batch4b, deploy/batch-1016d (merge e1b868ff passed all suites and the build). The critic found 1 blocker: the weekday chips overflow on phones. The fixer, then the verifier, were running. After a pass: apply its production migrations from the merge report (webhook_event_lease, study_weekdays, ai_reply_report, funnel_product_steps, renamed), then push.
  - **Web motion/UX + social** on wt-webux2, web/ux-social-1016. WP-B 1485a42e and WP-C 3cf9c751 are done. WP-A (motion) and the Mob server and website were running, then the wux gate.
  - **App v12 walk on the emulator rig** (tmp/rig-1016e/RIG-READY.md), then fixes, the re-walk and the v12 release. NOTE: this script also runs app UX + social packets after the release, which duplicates app-ux-social-now. Skip or stop that tail.
- **app-ux-social-now (wf_0fd124eb-6d5)** on wt-appux2, ui/ux-social-1016 (from ui/owner-1016). AP-1, AP-2 and AP-3 Opus packets plus the Mob app side, then integrate. AP-1 and AP-3 handovers exist in the brain.
- **APK v12 preview** (sent to the owner): mockmob-next/tmp/apk/mockmob-v12-preview-f5d848bf.zip, from ui/owner-1016 f5d848bf. Debug-signed (no key.properties), and **not yet walked**.
- **Landing**, wt-land2 web/land2-1015 at 326a1c74: **round 9 scored 80**, below round 8's 84, so it is NOT shipped.
  - The good part: the unlimited-mocks message is at heading level, there is no "never repeats", and the counts are server-rendered.
  - Next: read the critic r9 defects in the recover-0820pm journal (wf_432183b4-4cb), fix, re-score to 85 or more, then ship through a gate.

### Owner decisions pending
- **The Mob social spec** (design-decisions/pass-1016e/SOCIAL-SPEC.md): decisions D-S1 to D-S4. No credits or money in social without his OK.
- **Landing 41-subjects figure:** Hindi has 10 questions and Sanskrit 8. Consider dropping the subject count.
- **Feed-keys fix:** held until the new app ships.
- **Credit fast-path rewrite:** dropped.
- **Optional hardening, his to switch:** PERSISTENT_LIMITS_ENABLED=true in Vercel; Supabase leaked-password protection.
- **Local env files:** 52 .env.local files point at production; switching them to staging is his call (docs/brain/LOCAL-ENV-STAGING.md on fix/health-1016).
- **His steps tonight (21:00 reminder):** the Razorpay TEST plan ID and keys, SUPABASE_DB_URL plus pg tools, the Play account and upload key, and one fresh mock plus one repair to prove Repair v4 live.

### Higgsfield (AI video), owner-funded USD 15. Include this in context whenever he asks
- **Read:** HIGGSFIELD-IDEAS-2026-10-16.md (the direction and the iteration loop), HIGGSFIELD-PLAN-2026-10-16.md (budget, models, rules), HIGGSFIELD-RESEARCH-2026-10-16.md (verified prices: the screenshot's "from" prices are 480p; Seedance 2.5 1080p is about USD 0.80/s; Wan 3.0 is primary; failed or moderated runs are free, rejected renders are charged; call /estimate first).
- **Owner direction:** use it for the **landing page (scroll storytelling) and app onboarding**, where "proper animation" beats SVG and code. Not for subject objects.
- **Round 1 of idea agents is PENDING** (5-7 Haiku and Sonnet agents with the lenses listed in the ideas file, then one synthesizer). It was not run at 11:15 pm because usage was at 87%. Run it after the reset.
- **Spend gate:** free storyboard stills first (GPT image account), the owner picks, then Wan drafts. Ledger in tmp/higgsfield/LEDGER.csv. The key goes in env only.

### Lessons tonight (memory: agent-swarm-resource-hygiene, time-and-estimates-format, usp-unlimited-mocks)
- The 5-hour limit killed 28 agents at about 6:50 pm. Leaked Gradle daemons and headless Chrome later crashed the app (0.4 GB free). Reap leftovers, put a RAM rule in every prompt, and check usage before each wave.
- **Push the moment a verifier passes.** Batch 3 sat ready for 45 minutes.
- Give relative times and size them for parallel agents. Never repeat an estimate without new evidence.
