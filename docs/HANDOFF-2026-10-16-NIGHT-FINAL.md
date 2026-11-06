# MockMob handoff: 16 Oct 2026, about 11:50 pm IST (session 604ced81, Claude Opus 5.5 as CEO/CTO)

This is the single source of truth for the next session. Read all of it before acting. Older detail sits in HANDOFF-2026-10-16-DAY.md (sections 0-9), CTO-LOOP.md and the files listed in section 9 here. Newest owner words win. Agent-reported claims must be checked against git, production and the files before you act on them.

---

## 1. THE GOAL (one goal, pursue it continuously)

**Ship a visibly new, clearly better MockMob on both the website and the Android app, with every piece proven before the owner sees it.**

Concretely, finish and ship what is already built, in this order:
1. Website batch 4.
2. The website motion/UX pass and the social loop ("the Mob").
3. The new landing page.
4. App v12 (the owner's 39-item ledger, walked on the emulator) plus the app motion/UX pass and the Mob in the app.

Then start the Higgsfield landing and onboarding scenes through their idea, storyboard and approval loop.

"Done" means it is live (website) or an APK in the owner's hands (app), after its gate. Report honestly in percentages and relative times ("in the next 30 minutes"), 12-hour clock.

---

## 2. Owner rules (standing; these override defaults)

**Role and pace:**
- Act as CEO and CTO. Orchestrate many parallel agents (he expects 15-20 when usage and RAM allow).
- Keep the plan in the main session.
- Never stop to ask about routine work. Ask only for the owner decisions listed in section 6.

**Routing** (memory: subagent-model-choice):
- Sonnet does the heavy lifting.
- Opus only for complex UI/UX, motion and polish.
- Haiku for quick bounded tasks.
- Always set effort explicitly.

**Design:**
- Follow the owner's research brain: `docs/research/premium-ux-ui-2026-10/AGENT_RULES.md` (evidence IDs T001-T009, S010-S018), the 12-part anti-slop test, the 0/1/2 rubric, and a DESIGN_DECISIONS note per feature. Also the ui-ux-standards skill and `AI OS/wiki/concepts/ui-ux-standards.md`.
- Banned: eyebrow pills or dots, glow, gradient text, icon grids, nested cards, arrows on buttons, ALL-CAPS labels, hype copy, build talk.
- Mobi appears at most once per screen, only at real moments.
- Never simplify by cutting features; he calls that a regression.
- Real numbers with denominators. Night and Day parity. 48 dp / 44 px targets.

**The headline USP** (memory: usp-unlimited-mocks): **unlimited mocks from one central question bank** (rivals give 10-30 per subject). It must be visible everywhere, truthful and calm. The Mistake Lab and Repair are the depth story, not the headline.

**Website deploys:** tests plus a visual critique at 390 and 1440, Night and Day, plus an independent verifier. **Push the moment a verifier passes** (batch 3 sat ready for 45 minutes tonight).

**Landing:** he previously said he may deploy the landing when satisfied. The gate is critic score ≥ 85-90 plus a verifier. Show him if he asks.

**App** (memory: device-truth-testing): done only after an **emulator walk with screenshots** against the ledger, covering upgrade over the previous APK, keyboard open, scroll, and Night and Day. Goldens alone are never enough; that is how v5 issues survived to v10.

**Security and access:**
- Never drive his browser. Never sign in as him or create accounts.
- Agents use only the project test account `app-e2e-student@example.com` on STAGING through the local site.
- Never use the chrome-devtools MCP or a visible browser; headless Chrome only.
- Use his phone (adb 10BF370PA6002XR) only when he says it is connected.

**Production database:** allowed under his standing grant (14 Oct): save the migration, dry-run on staging (or in a rolled-back transaction when staging lacks the tables), keep an undo file, add a STATUS.md entry.

**Resource hygiene** (memory: agent-swarm-resource-hygiene):
- Reap leaked processes between waves: java GradleDaemon, chrome.exe with an AppData\Local\Temp profile, flutter_tester/dartaotruntime, orphan `next dev`.
- Put a RAM rule in every agent prompt.
- Check `get_usage` before each wave. Do not launch big waves above about 60% with more than an hour to the reset.
- WIP-commit right after any mass agent death.
- Tonight the 5-hour limit killed 28 agents (6:50 pm) and leaked processes crashed the app at 0.4 GB free.

**Product only:** marketing waits until January.

---

## 3. Live in production now

**mockmob.in = main 8a0141ba (batches 1-3).** Vercel READY, 0 runtime errors after deploy.

**Batch 1:**
- Mistake Lab slice 4: trap tags, Traps you meet, Revise / Same mistakes later.
- My colleges, Mobi rig v2 on the web, crash reports, names, Learn concept checks.
- The arena de-slop.

**Batch 2:**
- Mistake Repair v4: Check it held (a fresh never-seen question, server-marked, no extra credit, first answer counts), "Ask Mobi about Qn" (cost shown first), the Revise hand-off.
- The older-paper Lab line and marked-for-review in the SWOT.
- The practice-progress chunking fix (Accountancy above about 700 ids).
- The Rs 99 monthly switch, inert until `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set.
- Honest pricing copy.

**Batch 3:**
- Slice 5 cohort time (its lines stay hidden until enough timed students).
- Mobi moments on the website; better Progress, Review and Weak chapters.
- The NTA index signature fix.
- The homepage bank line ("Every mock is drawn fresh from one bank of 8,197 questions across 41 subjects...").

**Production DB, applied today** (STATUS entries on branch db/status-1016e and wt-polish):
- trap_atlas, revise_cards, my_colleges, app_errors, funnel_daily;
- question_option_stats with refresh v2 (461 questions);
- submit_rival_battle (was missing; dry-run proven);
- mm_leaderboard();
- least privilege for the browser roles (0 open RLS tables, 0 anon-executable server functions);
- pinned search_path;
- the payments policy in initplan form;
- the public question bank closed to the anon key (security fix by session cc0bf1af);
- **nta_question_index rebuilt: 653 rows, 0 signature failures**, verified with scripts/nta-engine-run.mjs.

**Known gaps live:**
- English NTA refuses a full paper (34 too few high-score questions): a content gap.
- The live homepage still says "Fresh questions, never repeats" (the new landing removes it).
- **Repair v4 has never been proven against the real DB.** The owner's own repair is the test.

---

## 4. In flight (workflows die with the session: check each by git and journal, WIP-commit partial work, then continue)

Journals are under `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\604ced81-3aa7-4deb-b42c-f324ca5f51e2\subagents\workflows\<run id>\journal.jsonl`. Scripts are in the session's workflows/scripts folders. Resume works only in the same session; otherwise relaunch only the missing agents.

| Track | Worktree / branch | State at handoff | Next action |
|---|---|---|---|
| **Website batch 4** | `wt-batch4b`, `deploy/batch-1016d` (merge e1b868ff; base main 8a0141ba) | Merged and built, all suites green. Contents: security-1016 and security-2 (payment verify fix and webhook_event_lease), db/status-1016e, fix/health-1016 (first-sign-in 500 fix, script guards, narrower reads), web/usp-mocks-1016 (unlimited mocks in Practice, result, pricing, onboarding), and the reconcile list (college search for BCOM, badges API and web badges, revise events, study weekdays, ai-report, compass card, timed nudge, help, copy, rival Mobi, funnel calls, auth cache, egress, art briefcase). Excludes feed-keys (held) and credit fast-path (dropped). The critic found **1 blocker: the weekday chips overflow on phones**. Fixer, then verifier, were running (wave-0935pm, wf_967ff020-5e0). | Finish the fix, then the verifier. Apply its NEW migrations to production in order (from the b4:merge result in the journal: webhook_event_lease 20261016170100, study_weekdays 20261016110000, ai_reply_report 20261016140000, funnel_product_steps renamed), each with pre/post checks and a STATUS entry. **Do not re-apply** 160100/170000/170200/170300/170400 (already live). Also merge the newest db/status-1016e commits (ea40b6ad: NTA index STATUS). Push, verify Vercel and runtime errors. |
| **Website motion/UX pass + the Mob (server + web)** | `wt-webux2`, `web/ux-social-1016` (from main 8a0141ba) | WP-B 1485a42e (touch, one primary action) and WP-C 3cf9c751 (Mistake Lab truth and hierarchy) done. WP-A (motion: page transitions were never wired; count-ups, entrances, loops) and the Mob server+web were running, then the gate. Plans: `docs/design-decisions/pass-1016e/WEB-PASS.md`, `SOCIAL-SPEC.md`, `SOCIAL-APP-CONTRACT.json`. | WIP-commit, finish WP-A and the Mob (no credits or money; minor-safe; no chat or DMs; migration staging-only until approved), gate (critic, fixer, verifier), merge onto batch 4's main, apply the social migration under the grant, push. Owner decisions D-S1 to D-S4 in SOCIAL-SPEC.md first. |
| **Landing** | `wt-land2`, `web/land2-1015` at 326a1c74 | Critic scores 76, 82, 84, 87, 88, 85, 84, **80 (round 9)**. Not shipped: below the live bar. Good now: unlimited mocks at heading level ("One question bank. As many mocks as you want with Pro."), no "never repeats", server-rendered counts. Round 9 defects are in the recover-0820pm journal (wf_432183b4-4cb, label land:critic-r9). | Fix the r9 defects (Opus), re-score to ≥ 85-90, rebase on the newest main, gate, ship. Then rebuild Lighthouse mobile (LCP was about 4.7 s). |
| **App v12** | `wt-owner`, `ui/owner-1016` at f5d848bf+ | All 8 areas built (shell/bar f9f3978a, colleges f7b8f40d, account 63853691, practice e5b1c683, today 50e8bdb9, review 18007846, you, onboarding c278997a; integration f5d848bf registered /review/again and fixed the tests). **APK v12 preview sent to the owner** (`mockmob-next/tmp/apk/mockmob-v12-preview-f5d848bf.zip`, debug-signed, NOT walked). The emulator walk of L01-L39 was running (wave-0935pm app:walk). | Reap processes, then restart the rig per `tmp/rig-1016e/RIG-READY.md`: staging site from wt-rig-site on 3101, Supabase relay on 3102 (Avast re-signs TLS), AVD mockmob_budget at -memory 3072, a PROFILE build with phone-relay.json (debug hangs on a CircularDependencyError). Then walk all 39 items with screenshots, fix, re-walk, release v12 (version bump, release command in HANDOFF-2026-10-15-FULL section 5), merge into ui/phase2 and feat/app-and-web, and send. |
| **App motion/UX pass + the Mob (app)** | `wt-appux2`, `ui/ux-social-1016` (from ui/owner-1016) | Workflow app-ux-social-now (wf_0fd124eb-6d5): AP-1 (core motion, Today motion) handover exists; AP-3 (truth, touch, hierarchy) handover exists; AP-2 (moments: clock turn, finish) and social:app were running. Plan: `pass-1016e/APP-PASS.md`. | WIP-commit, finish, integrate (analyze, units, goldens), then an emulator walk of the pass items (record motion clips), then merge into ui/owner-1016 after v12 and ship as v13 (or fold into v12 if both pass in time). NOTE: wave-0935pm's app tail duplicates this: skip it. |
| **Real-flow staging tests** | rig | Never completed (killed twice). | Run during the app walk: a quick practice, a short mock, the result + Lab, Mistake Repair + Check it held against the staging DB (reload: stored answer), Revise cards written, colleges search "BCOM". |

**Leftovers to know:**
- `wt-health` (fix/health-1016, verified, in batch 4).
- `wt-usp` (web/usp-mocks-1016, in batch 4).
- `wt-dbstatus` (db/status-1016e: STATUS entries).
- `wt-w4-practice` WIP a15bac4f (egress-practice, NOT adopted).
- `refs/wip/*-1445` snapshots from the crashed session.
- About 79 worktrees exist. Clean up only after everything ships.

---

## 5. Owner's own steps (tonight's 9 pm reminder fired; help him when he returns)

1. **Razorpay:**
   - create the Rs 99 monthly plan in TEST mode, then send the plan ID and save the test keys in `wt-batch2\.env.razorpay-test.local` (see OWNER-TONIGHT-2026-10-16.md);
   - the agent runs the TEST purchase per RUNBOOK-MONTHLY-BILLING-2026-10-16.md;
   - then LIVE: set `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` in Vercel, plus the webhook events;
   - decide about the 6 lapsed-premium accounts;
   - Vercel Pro is needed when payments go live.
2. **Backups:** `SUPABASE_DB_URL` (session pooler) plus PostgreSQL client 17 or later, for RUNBOOK-WEEKLY-BACKUP-2026-10-16.md.
3. **Play:** the developer account, then `tool\make_upload_key.ps1` with an agent, the Web client ID in prod.json, SHA-1 and SHA-256 after the first upload, and 12-20 testers (PLAY-RELEASE-2026-10-16.md on wt-play). The Play icon and feature graphic candidates are in mockmob-next/tmp/play-art-1016.
4. **Proof:** one fresh timed mock plus one repair, to prove Repair v4 live. Watch /api/recovery/check in the Vercel logs when he does.
5. **Optional hardening (his switches, recommended yes):** `PERSISTENT_LIMITS_ENABLED=true` in Vercel (shared rate limits through the DB function take_rate_limit, which exists); Supabase leaked-password protection.
6. **Local env:** 52 .env.local files point at production. Switching them to staging is his call (LOCAL-ENV-STAGING.md on fix/health-1016).

---

## 6. Decisions waiting on the owner

- **The Mob:** D-S1 to D-S4 in `pass-1016e/SOCIAL-SPEC.md`. No credits or money in social without his OK. A friend invite tied to credits is his decision.
- **Landing:** keep or drop the "41 subjects" figure (Hindi has 10 questions, Sanskrit 8).
- **App IA sign-off:** the 6-slot bar (Today, Practice, Start, Review, Colleges, You), the tab name "Colleges", study days only on You. Defaults were chosen.
- **Feed-keys fix** (the Explore answer key reaches the browser): held until the new app is installed widely, then ship.
- **Key-quality loop:** apply only the 5 questions with the 20-pick gap after an official key review (pending).
- **Mobbin:**
  - The owner is considering Pro at USD 20 with a student discount (quarterly, non-refundable, auto-renew).
  - Recommendation given: buy it, turn auto-renew off the same day, and use it for references and for a **blind A/B**. Three real screens (onboarding opening, the Mob main screen, the result after a mock), each built by an agent with our brief alone against our brief plus the Mobbin MCP, same model and prompt; the owner picks blind. If the MCP wins at least 2 of 3, adopt it in the design agents' toolkit.
  - The owner connects the MCP himself (a sign-in). iOS-only references are fine for taste; translate the Android conventions (back, permissions, share sheet, scroll feel).
  - Research: no fair before/after exists; several users say agents ignore its results; Android is likely unsupported in the MCP.

---

## 7. Higgsfield (AI video). The owner funded a USD 15 API budget. Include this in context whenever he asks.

**Files:**
- `docs/brain/HIGGSFIELD-IDEAS-2026-10-16.md` (direction, seed ideas I1-I6, rules, **the iteration loop**, the Opal reference);
- `HIGGSFIELD-PLAN-2026-10-16.md` (budget, models, ledger rules);
- `HIGGSFIELD-RESEARCH-2026-10-16.md` (verified prices and features, 41 sources).

**Owner direction:** use it on the **landing page (scroll storytelling) and app onboarding**, where "proper animation" beats SVG and code. Not subject-object animations.

**Reference bar:** Opal's onboarding (a glowing crystal breaking out of rock; Mobbin flow link in the ideas file).

**Verified facts:**
- The screenshot prices are 480p rates.
- Seedance 2.5 costs about USD 0.32/s at 720p and **0.80/s at 1080p** (never 1080p on this budget).
- **Wan 3.0 is primary:** last-frame control, 1:1, seed, arena rank 4, close to Seedance at 2. A/B it against Kling 3.0 Standard. Seedance only at 720p, for one shot the owner picks.
- Failed or moderated runs are free; rendered-but-rejected clips are charged. Call `/estimate/` before every call.
- Wan's 60% discount ends 31 Oct.

**Next step (not yet run):** round 1 of the idea loop. Spawn 5-7 Haiku and Sonnet idea agents with the lenses in the ideas file, then 1 synthesizer that ranks the top 8. Then free storyboard stills (the owner's GPT image account), then the owner picks, then Wan drafts. The ledger is `tmp/higgsfield/LEDGER.csv` with a hard cap of USD 15. The key (`HIGGSFIELD_API_KEY`) goes in a git-ignored env file only. The account is not connected yet.

---

## 8. Reference: key facts and pitfalls

- **Supabase:** production `isrxrxzjocewrdureyhp`, staging `onwkqxmjqjrhfbjjdydu`.
- **Vercel:** project `prj_uSolddribHQDl1mM5AKxg3O9qCIu`, team `team_V5PhMz9hqV42vblUMcvhYqoN`. Cron limit: 2 in use (refresh-inventory also runs the NTA index and cohort refresh).
- **Local web:** `npx next dev --webpack` and `npx next build --webpack` (Turbopack rejects the node_modules junction to mockmob-hotfix/node_modules). Vercel builds normally. A transient Google Fonts error on build: retry.
- **Flutter:** only via `MOCKMOB_FLUTTER_SLOTS=2 bash tool/flutter_locked.sh`, unit tests with `-j 1`.
- **The app plainBody fix (fd3fca29 / 3887e786):** dio returns decoded JSON even with ResponseType.plain. That emptied Today, Review and college search for every account in v10. Test fakes must mirror real content types.
- **Workflow scripts:** written from Python on Windows, they need LF line endings or the Workflow tool refuses them. Guard empty path lists in `git checkout <rev> -- $LIST`.
- **NTA index switch-off:** truncate public.nta_question_index (the runtime falls back to the full read).
- **Usage window:** the 5-hour limit resets around 12:30 am and 5:30 am IST cycles; check `get_usage`.
- **The owner's taste:** premium like HIGH, Revolut, Fampay; motion beyond Duolingo, judged in use; real proof, no fake dashboards.

## 9. Index of documents (all in mockmob-next/docs unless noted)

- `brain/HANDOFF-2026-10-16-DAY.md` (sections 0-9, the day's full history)
- `brain/CTO-LOOP.md`
- `brain/STATUS.md` (on the batch branches)
- `brain/APP-OWNER-LEDGER-2026-10-16.md` (39 app items with acceptance steps)
- `design-decisions/app-ia-1016.md` (IA, ownership map) and `app-today/practice-review/you/tools-1016.md`
- `design-decisions/pass-1016e/APP-PASS.md`, `WEB-PASS.md`, `SOCIAL-SPEC.md`, `SOCIAL-APP-CONTRACT.json`
- `brain/RECONCILE-WEB-2026-10-16.md`, `RECONCILE-APP-2026-10-16.md` (after the crash)
- `brain/PROD-HEALTH-2026-10-16.md`; `LOCAL-ENV-STAGING.md` (fix/health-1016)
- `brain/VISION-INVENTORY-2026-10-16.md`, `DESIGN-CRITIC-2026-10-16.md`
- `brain/HIGGSFIELD-IDEAS-2026-10-16.md`, `HIGGSFIELD-PLAN-2026-10-16.md`, `HIGGSFIELD-RESEARCH-2026-10-16.md`
- `research/premium-ux-ui-2026-10/` (the owner's research brain)
- Runbooks: monthly billing, weekly backup, Play release, NTA question index
- Memory: `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\memory\MEMORY.md` (read every entry; the newest are device-truth-testing, time-and-estimates-format, usp-unlimited-mocks, agent-swarm-resource-hygiene, higgsfield-video-plan)

## 10. First 15 minutes for the next session

1. `continuum_start` (project mockmob). If the brain search fails, read the files directly.
2. `get_usage`. Reap leaked processes (section 2).
3. For each worktree in section 4: `git status`. WIP-commit any partial edits with a clear message.
4. Read the journals of wave-0935pm (wf_967ff020-5e0) and app-ux-social-now (wf_0fd124eb-6d5) to see what finished.
5. Relaunch the unfinished tracks in priority order (batch 4, then web UX+social, then landing, then app walk and v12, then app UX+social), with RAM rules and staged waves.
6. Tell the owner, in a few lines, what is live, what ships next, and when.


---

## 11. EXACT STOP POINT (safe stop by the main session, 16 Oct about 11:55 pm, at 95% usage). START HERE.

All workflows were stopped deliberately. All agent processes (dev servers, headless Chrome, Gradle, emulator, staging site) were killed, leaving 6.7 GB free. Every interrupted worktree was committed as a "STOP POINT" commit. **Nothing is running. Nothing is half-applied in production.** This section overrides section 4 where they differ.

### Track A: Website batch 4. VERIFIED, READY TO SHIP (do this first)
- **Where:** `wt-batch4b`, branch `deploy/batch-1016d`, HEAD **965860e5**. The tree is clean. Independent verifier: **PASS** (lint, 8 suites, build).
- **Stopped at:** after the verifier, before the production migrations and the push.
- **Next, exactly:**
  1. Fetch. Confirm origin/main is still 8a0141ba and that 965860e5 contains it (fast-forward).
  2. Apply these migrations to production, in this order, each under the grant with a pre-check, apply, post-check and a STATUS entry. Each has an undo file in supabase/undo, and each was dry-run on staging per the merge report.
     - 20261016170100_webhook_event_lease (payments, needed before Razorpay goes live)
     - 20261016110000_study_weekdays
     - 20261016140000_ai_reply_report
     - 20261016120100_funnel_product_steps (renamed; collision fixed)

     Skip, because they are already live: 20261016141000_questions_private_to_browser_roles (closed by session cc0bf1af; verify that anon cannot select public.questions) and 20261016170200_server_only_functions_drift (already applied tonight). The full list of the 10 migrations not on main, and the dry-run evidence, are in the results labelled b4:merge and b4:verifier in journal wf_967ff020-5e0. Read them before applying.
  3. Merge db/status-1016e (HEAD ea40b6ad, STATUS entries for tonight's DB work) into deploy/batch-1016d. Push to main. Verify Vercel READY, runtime errors, and a smoke of /, /pricing, /progress, /profile, the colleges search.
  4. Non-blockers to note in STATUS:
     - /privacy hides the stream and AI-report sections until APP_STREAM_AND_REPORT_LIVE is set true in src/lib/appReleaseGates.mjs. Flip it in the same deploy as an app that has those features.
     - The app's college_search.dart may still have the old "bcom" behaviour; verify against ui/owner-1016.
     - Weekday chips look oval at 320 px.

### Track B: Website motion/UX pass + the Mob (server + web). Gate in progress
- **Where:** wt-webux2, branch web/ux-social-1016, HEAD **9abc71e5**. That is a STOP POINT commit holding the interrupted wux:fixer's partial edits (20 files), on top of:
  - 9d28148b (T0 token: count-up 720 to 420 ms);
  - dbb80d00 (WP-A motion);
  - 1485a42e (WP-B touch, one volt);
  - 3cf9c751 (WP-C Mistake Lab truth);
  - e49f347b (the Mob server + web, behind MOB_ENABLED, off).
- **Stopped at:** the fixer was mid-way through the gate critic's majors. The verifier never ran. The production build has not been run on this branch.
- **Open majors (label wux:critic in journal wf_967ff020-5e0):**
  1. Every Mob dialog opens at x=0, y=0 instead of centred.
  2. The Mob copy promises "never shows who didn't sit" while the member list does show it.
  3. No comparison or hand-back after both members finish a shared paper (ResultPageClient has no Mob reference).
  4. Two lime (volt) actions per viewport on /mob.
  5. The same double-volt on Practice, Review and Progress at 1440 (sidebar Start plus page Start).
- **Next, exactly:** an Opus fixer reviews 9abc71e5's partial edits against those 5 majors (keep the correct ones, finish the rest), runs lint, test:app, test:recovery, test:learning, npx next build --webpack, and commits. Then a Sonnet verifier on a dev server (390 and 1440, Night and Day). On a pass, merge onto main after Track A and push. The Mob stays OFF (MOB_ENABLED) until the owner answers D-S1 to D-S4 in pass-1016e/SOCIAL-SPEC.md. Its migration is applied on staging only; apply it to production only after the owner's OK.

### Track C: Landing. Needs a fix round
- **Where:** wt-land2, branch web/land2-1015, HEAD **a5f3710b** (a STOP POINT commit with 2 previously untracked files from round 9 tooling; check them and drop them if they are scripts or captures) over 326a1c74 (the round 9 fixes).
- **Stopped at:** round 9 was scored at **80/100** (below round 8's 84), so the page was not shipped. The defects are in journal wf_432183b4-4cb, label land:critic-r9.
- **Next, exactly:** an Opus fixer handles every r9 high and medium. Keep: unlimited mocks at heading level, no "never repeats", server-rendered counts. Then an Opus critic round 10, target 88 or more. Then rebase on the newest main, a gate, and ship. Show the owner first if he is around.

### Track D: App v12. Built, not walked
- **Where:** wt-owner, branch ui/owner-1016, HEAD **f5d848bf** (clean). APK v12 preview from this HEAD was sent to the owner (debug-signed).
- **Stopped at:** the emulator walk (label app:walk) was mid-run when stopped. **No walk results were recorded. Treat it as not started.** The emulator and the staging site are now stopped.
- **Next, exactly:**
  1. Restart the rig per tmp/rig-1016e/RIG-READY.md: the staging site from wt-rig-site on 3101, the Supabase relay on 3102, AVD mockmob_budget at -memory 3072, a profile build with dart_defines/phone-relay.json.
  2. Walk L01-L39 with screenshots, including the upgrade over v10.1 and the real-flow checks: a quick practice, a short mock, the Lab, Repair + Check it held against staging, Revise, colleges "BCOM".
  3. Fix by area, re-walk the failures, then release v12 (version bump and the release command in HANDOFF-2026-10-15-FULL section 5), and send it.

### Track E: App motion/UX pass + the Mob in the app. Integration in progress
- **Where:** wt-appux2, branch ui/ux-social-1016 (base 0d1ff6b6 from ui/owner-1016), HEAD **dfd705b9**. That is a STOP POINT commit with the interrupted aux:integrate partial edit (1 file), over:
  - AP-1 (4 commits, the last at 22:56: core motion, Today);
  - AP-2 (a5665a3b, 863cfa32, plus more: about 80%; AP2-03 not built);
  - AP-3 (a18fdd30: the 4 most visible items; the rest is outside its files);
  - the Mob app side (7 commits; 48 tests and 50 goldens pass).
- **Stopped at:** the integration (whole-app analyze, full unit tests, goldens) was mid-run. The You hub, Today and router suites were NOT re-run after the Mob added lines to them.
- **Next, exactly:** a Sonnet integrator runs flutter analyze, the full unit tests (-j 1) and goldens, fixes, and commits. Then an emulator walk of the APP-PASS items and the Mob flows, recording motion clips. Then merge into ui/owner-1016 after v12 ships, and release as v13, or fold it into v12 if both pass together. The Mob stays off until the owner answers D-S1 to D-S4.

### Not started (queued)
- **Higgsfield round 1 idea agents** (section 7; HIGGSFIELD-IDEAS-2026-10-16.md, "How to keep iterating" step 1).
- **The Mobbin blind A/B** (section 6), once the owner buys Pro and connects the MCP.
- **Real-flow staging tests:** folded into Track D's walk.

### Order for the next session
A (ship batch 4), then B and C in parallel (website), and D then E (app; D and E can build in parallel, but only one emulator walk at a time). Stage the waves, check get_usage before each, and reap processes between them.
