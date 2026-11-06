Continue MockMob as CEO/CTO from session 604ced81 (stopped 17 Oct 2026 about 7:25 pm IST, an owner-requested safe stop at 95% usage).

Call continuum_start with project "mockmob". Then read mockmob-next/docs/brain/HANDOFF-2026-10-17-EVENING.md completely. It is the single source of truth and holds every detail of 17 Oct: my words, the decisions, honest progress, live state, incidents and lessons. Also read:
- WEB-OWNER-LEDGER-2026-10-17.md: my 145 website and landing requests, from my own messages;
- OWNER-FEEDBACK-2026-10-17.md (F1-F18);
- the design decisions in docs/design-decisions/pass-1017 (NAV, GLASS, RESULT, START, TODAY, LEARN-REVIEW);
- the memory index, especially owner-feedback-1017, agent-swarm-resource-hygiene and content-generation-only-on-ask.

Then start at section 5, "EXACT STOP POINT". It gives every track's worktree, commit and next step. The workflow scripts to copy are in docs/brain/workflows-1017b, and the saved results are in tmp/resume-1017d (web-ledger-verify-results.json lists all 100 website items with pass, partial or fail).

THE GOAL: everything I have asked for on the website and the landing, actually implemented and live, with nothing missed. For 2-3 days my feedback kept getting lost in new builds. The audit proved it: only 37 of my 100 website items fully pass on the live site. Then the Mob in the app and the website at 10/10 execution, and app v13 that looks and feels new and premium (v12 was "very bad"), walked on the emulator and in my hands. Quality over speed: run things in parallel, test properly, prove every piece before I see it.

In this order, with parallel agents in staged waves:
1. Website release 2 (top priority):
   - Finish the result, today and nav fixers; start and pricing are already done.
   - Check W-098 (the per-user AI cap on rival start and submit) first.
   - Integrate all five fix branches; re-verify every partial and failed ledger item; run the independent final verifier; push.
   - Re-audit all 100 items on the live build and loop until every one passes.
2. Landing:
   - A two-critic panel on round 14 (9e3ceab7), also checking L-001 to L-045.
   - Fix and re-score until the mean is 88+ with no high or truth defect and every L item passing.
   - Then a ship check and push.
3. App v13:
   - Verify the repair's work (STOP 42510757, with 329 regenerated goldens to open and judge) or fall back to 29abcf75 per area.
   - Finish the 22 walk failures and the 25 critic defects, each fixer in its own worktree with commits.
   - Bring the Mob app side in line with the new server.
   - Integrate; walk 2 on the emulator (F1-F18, L01-L39, the Mob with two members, motion clips); an Opus critic; fixes; walk 3.
   - Send me the APK with honest notes.
4. The Mob:
   - Run the go/no-go on staging.
   - Only at 10/10: apply its migrations on production under my grant, set MOB_ENABLED (plus PERSISTENT_LIMITS_ENABLED and MOB_ID_SECRET) on Vercel, and ship with v13.
5. Then Learn and Review F15: finish the web packets in wt-lr17, then the app packets on v13. Then Higgsfield.

Rules:
- Act as CEO and CTO. Decide from my recorded taste; don't re-ask decided things. My newest words win.
- No question or content generation unless I ask in my current message.
- Models and effort:
  - Sonnet does the heavy lifting.
  - Opus for complex UI, motion, polish and visual critique.
  - Haiku for quick tasks.
  - Set effort explicitly.
- Website gate: tests, a visual check at 390 and 1440 in Night and Day, and an independent verifier. The main session pushes.
- App: done only after an emulator walk and a visual critique; never trust goldens alone.
- Never cut features.
- Never use the chrome-devtools MCP or any visible browser. Never run the installed Chrome directly. Never drive my browser or sign in as me.
- Only gpt-6-luna and Claude Haiku 5.5 run in the app or website.
- Production DB under my standing grant: save, dry-run on staging, undo, STATUS.
- Lessons from 17 Oct:
  - Never SendMessage a running workflow agent (it starts a duplicate).
  - Agents stop only their own processes.
  - Cap shared dev servers with NODE_OPTIONS=--max-old-space-size=4096 and restart them between waves.
  - Never let parallel fixers share one tree without committing.
  - Stage waves of about 8 heavy agents.
  - Check usage every 15-20 minutes; stop cleanly at 87-90% with STOP POINT commits.
- If every agent dies with an SSL certificate error, it is Avast's HTTPS scanning: save the work and resume.
- Give honest percentages and relative times on a 12-hour clock.
- Before the session ends, write a full handoff and a prompt like this one.
