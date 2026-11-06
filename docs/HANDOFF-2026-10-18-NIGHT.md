# MockMob handoff: 17-18 Oct 2026, about midnight IST (session 604ced81, Claude Opus 5.5 as CEO/CTO)

> **SUPERSEDED 18 Oct about 2 am.** The current state is in `NOW.md` and the open owner asks are in `OWNER-MASTER-LEDGER.md`. This file is history.

**Read this whole file first.** It replaces the stop points of HANDOFF-2026-10-17-LATE and -EVENING (read those for history, rules and key facts).

**THE GOAL for this session:** **v15 ready to publish on the Play Store by about 7-8 am, 18 Oct.** In parallel, the website release train continues.

Read, in this order:
1. `V15-SPEC-2026-10-18.md`: the v15 design and plan, written by the main session.
2. `OWNER-FEEDBACK-2026-10-17-NIGHT.md`: N1-N19, his newest words.
3. `WEB-OWNER-LEDGER-2026-10-17.md`.
4. `OWNER-FEEDBACK-2026-10-17.md` (F1-F18).
5. The memory index, especially:
   - orchestrator-thinks-agents-do
   - landing-checklist-gate
   - owner-feedback-1017
   - agent-swarm-resource-hygiene
   - content-generation-only-on-ask

## 1. The owner's words and decisions tonight (in order)

1. **About 9:50 pm:**
   - Resume from the LATE handoff.
   - "focus on keeping on launching the next versions of the apps every 1 to 2 hours... rather than trying to just be stuck in a loop of trying to improve one single version".
   - "We had made about 90% progress in the 2 days, and we have been stuck on the final versions... agents are getting lost doing unnecessary things."
2. **About 10:15 pm** (landing, after 15 rounds): "There is for sure some issue with some part of it." He chose **the fixed checklist gate**: ship the landing when all his L items pass, with zero truth and zero high defects, each fix locked by a test. The 88/100 score is advisory only. (Memory landing-checklist-gate.)
3. **About 10:50 pm:** he signed in to GitHub when the push prompt appeared (Git Credential Manager). He asked for an honest update; it was given (section 3).
4. **About 11 pm:** detailed feedback on the live website (desktop). All of it is in **OWNER-FEEDBACK-2026-10-17-NIGHT.md, N1-N19**. The key points:
   - **N1:** Today is still confusing. Replace the calendar strip and the mock slider, on web AND app.
   - **N12:** the result/Review redesign is "not acceptable at all". Restore the mascot and the full analysis.
   - Also: the blur is too strong, the fine-tune copy, the sliding-indicator animation, the CS/IP overflow, the NTA bar animation and timer, the Ask Mobi orb, the guide, and checking the CUET 2027 maximum number of subjects.
   - He loves the Start sheet.
   - He will review mobile next.
5. **About 11:15 pm, the orchestrator principle (memory orchestrator-thinks-agents-do):**
   - The main session does the thinking: design taste, decisions, exact specs.
   - Agents are doers: mostly Sonnet, Opus only where the doing needs taste.
   - "This is not to save costs."
6. **About 11:20 pm:**
   - **Skip v14 as a separate release:** merge its fixes into v15.
   - **v15 is the final version before the Play Store.**
   - "finish V13 in the next 1 hour".
   - Compile the v13 findings and the v15 fixes into the next session so that "by 7 am or 8 am we are completely ready for publishing it on the Play Store".

## 2. Live now
- **mockmob.in = main 12997f5a: website release 2.**
  - **What it contains:**
    - security rounds 1 and 2;
    - the per-user AI cap on rival battles (W-098);
    - the owner-ledger fixes for Start/Practice/runner and pricing/help/copy.
  - **Status:** Vercel dpl_C7KUvYzEbxjuwvkorugsdMPtciR6, READY, 0 runtime errors.
  - **Smoke:** /, /pricing, /help, /login, /today, /test and /leaderboard return 200; /api/leaderboard returns 401.
- **Production DB, applied tonight by the main session under the grant** (staging dry-run first; pre-checks and post-checks verified):
  - `create_pending_payout_lock`
  - `account_deletion_runtime_ai_scrub`
  - `default_privileges_server_only` (0 browser sequence grants; default ACLs postgres and service_role only)
  - STATUS entry in 12997f5a.
- **Before tonight:** waves 3 and 4 are published (353 questions); study_goals.exam_date and mock_target exist; the Mob migration is NOT on production.

## 3. Release train state at the stop (each in its own worktree; check every workflow's journal or result)

| Track | Workflow | Where | State |
|---|---|---|---|
| **App v13** | wf_2f859569-6ab "v13-fast" | wt-v13 ui/v13-1017 **e0939ad2** | The release APK build and a 45-minute emulator walk were running in parallel at about 11:30 pm. The APK goes to tmp/apk/mockmob-v13-<sha>.apk. **The walk findings feed v15 section 5.** v13 contents: A1 nav, glass, bounce, the 17 Oct Today and result (which the owner has since rejected, N1 and N12), the Start sheet, Review F17, the Mob app side (off), the ledger fixes. |
| **v14 fixes, now v15 inputs** | wf_d91a84bd-0f9 (done) | ui/v14-glass 7dd0ac52, ui/v14-today e55fee7f, ui/v14-result f221554f, ui/v14-practice (wt-v14-practice) | All committed with tests green; not walked |
| **Website release 3** | wf_f592d7f5-c7e "web-r3b-train" | wt-rel3 deploy/web-1017c | Live main plus web/fix-today-1017 f69f8a86 and web/fix-nav-1017 49dc3426, **excluding** web/fix-result-1017 (rejected direction; saved as branch deploy/web-1017c-withresult). Integrating, then the verifier. **The main session pushes on a pass** (GitHub may prompt the owner to sign in). |
| **Website release 4** | wf_b4ce44ef-8f8 "web-r4-owner-night" | wt-r4-today, wt-r4-result, wt-r4-practice, wt-r4-mobi, wt-r4-subjects; integrate into deploy/web-1017d in wt-rel3 | 5 builders running: Today N1, result restore N12, practice polish N2/N3/N5/N7/N8/N11, Mobi orb and guide N9/N17, CUET subject count N6. Then integrate and verify. **Before shipping, the main session reviews Today and result/Review itself against N1 and N12.** |
| **Landing** | wf_b167ffb5-960 "landing-checklist" | wt-land2 (from 9e3ceab7) | Checklist 1 done, fixer 1 done, checklist 2 running. It ships on the checklist gate; the main session pushes. |
| **The Mob** | none | wt-mobfix web/mob-fix-1017 c33d7f03; app side in v13 | The gate on staging has never run. Switch on only at 10/10 (HANDOFF-2026-10-17-EVENING Track M lists the steps). |

## 4. The next session, in order (with the chains)
1. **Collect:** the v13 APK and walk result (send the APK to the owner with honest notes if not already sent); the R3, R4 and landing results.
2. **Push:** R3, then R4 (after the main-session design review), then the landing (when its checklist passes).
3. **v15**, per V15-SPEC section 6:
   - merge v14 (about 45 min);
   - Today, result/Review and polish packets in parallel, Sonnet (about 1½ h);
   - integrate (about 45 min);
   - walk plus one Opus critique (about 1½ h);
   - fix (about 1 h);
   - confirm walk (about 45 min);
   - APK 1.0.15 (about 30 min).
   - **About 6-7 h total.**
4. **Play Store readiness** (V15-SPEC section 7): upload key and Console (owner), signing, privacy, data safety, target SDK, AI report route.
5. **The Mob gate,** then F15 Learn and Review, then Higgsfield, only after v15.

## 5. Rules in force (unchanged plus tonight's)
- **Ship every 1-2 hours;** never loop on one version.
- **Gates:** fixed checklists, never a fresh critic's score.
- **The main session writes the specs.** Agents implement: Sonnet by default, Opus only where taste is in the doing.
- **No content generation** unless he asks.
- **CPU limit:** at most about 12 heavy agents.
- **Dev servers:** NODE_OPTIONS=--max-old-space-size=4096.
- **Never message a running workflow agent.**
- **Processes:** agents stop only their own.
- **Never run chrome.exe directly;** never use a visible browser.
- **Pushes:** the main session pushes.
- **Usage:** check every 15-20 minutes; stop at 87-90% with STOP POINT commits.
- **Reporting:** honest percentages with the chain written out; 12-hour clock.
- **Production DB under the grant:** save, dry-run on staging, undo, STATUS.

## 6. Owner items pending
- **Play Console account and upload key** (now blocking for publishing).
- **Anthropic API key** (then Haiku 5.5 becomes the primary runtime model).
- **Avast exception** for the Claude app.
- **Held questions:** 112 at 7-7.9.
- **Hindi** reviewer.
- **Free first Repair** (his pricing call).
- **The Mob card on Today:** keep it or move it (the v14 Today fixer asked).
- **Mobile review** of the website (he said he will send it).
