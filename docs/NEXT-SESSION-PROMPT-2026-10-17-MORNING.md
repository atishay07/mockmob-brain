Continue MockMob as CEO/CTO from session 604ced81 (stopped 17 Oct 2026 about 4 am IST, a usage safe stop at 87%).

Call continuum_start with project "mockmob". Then read mockmob-next/docs/brain/HANDOFF-2026-10-17-MORNING.md completely. It extends HANDOFF-2026-10-17-NIGHT.md: read that one fully too (rules, decisions and live state). Also read:
- OWNER-FEEDBACK-2026-10-17.md (F1-F18, my words);
- FEATURE-ADOPTION-2026-10-17.md;
- the five design decisions in docs/design-decisions/pass-1017 (NAV, GLASS, RESULT, START, TODAY);
- the memory index, especially owner-feedback-1017 and agent-swarm-resource-hygiene.

Then start at section 5, "EXACT STOP POINT", which gives every track's worktree, commit and next step. The workflow scripts to copy are in mockmob-next/docs/brain/workflows-1017.

THE GOAL: ship a visibly new, clearly better MockMob on the website and the Android app, built from my 17 Oct feedback and decisions, with every piece proven before I see it. A student must know what to do next, use the features, and feel the value of what they pay for. I watched v12 on the emulator and it is very bad: the homepage looks weird, the navbar is wrong, and what I asked for is missing. v12 is dropped. v13 must look and feel like a new, premium app, with every 17 Oct decision visibly in it.

Next 5-10 hours, in this order, with parallel agents in staged waves:
1. Website:
   - Ship the motion/UX pass (Track A; its checks were never finished).
   - Finish the result, Start and fine-tune, Today, dock and Mob packets. Review F17, the subject claim and the live fixes are already done.
   - Integrate, gate and push.
   - Ship the landing only at 88+ with no truth defects.
2. App v13 (my top priority):
   - Integrate the UX pass.
   - Finish the six v13 packets: nav A1 with the bubble refined, liquid glass and bounce, the result screen, Today "Up next", Start and the fine-tune rules, and Review F17 with adoption. Add the app subject claim.
   - Integrate, then the Mob app side.
   - Walk the emulator against F1-F18 and L01-L39 with screenshots and motion clips, plus an Opus visual critic.
   - Fix, walk again, then send me the v13 APK with honest notes.
3. Content wave 3:
   - Re-solve the repaired rows and the reworded rows.
   - Run the final acceptance; merge, check and dry run.
   - Publish only questions scoring 8+ (two-judge mean and fit median), under the grant. Keep Hindi off.
   - Confirm the Physics syllabus call before dropping the 7 Electronic Devices questions.
   - Then keep adding depth to GAT, Physics, Chemistry, Maths and Biology the same way.
4. Weave in the adoption research everywhere:
   - the Find, Fix, Keep loop;
   - one next move per screen;
   - Repair on the mistake;
   - receipts;
   - a first-week path;
   - features introduced at the right moment.
5. After that:
   - Learn and Review (F15);
   - then the Higgsfield landing and onboarding scenes through their idea, storyboard and approval loop.

Rules:
- Act as CEO and CTO. Decide from my recorded taste; don't re-ask decided things. Never spend walks or releases on a build that lacks my newest decisions.
- Models and effort:
  - Sonnet does the heavy lifting.
  - Opus only for complex UI, motion, polish and visual critique.
  - Haiku for quick tasks and as question solvers.
  - Set effort explicitly.
- Website gate: tests, a visual critique at 390 and 1440 in Night and Day, and an independent verifier. Push the moment it passes.
- App: done only after an emulator walk and a visual critique; never trust goldens alone.
- Never cut features. Never use the chrome-devtools MCP or a visible browser. Never drive my browser or sign in as me.
- Only gpt-6-luna and Claude Haiku 5.5 run in the app or website.
- Production DB under my standing grant: save, dry-run on staging, undo, STATUS.
- Usage and RAM:
  - Stage waves of about 8 heavy agents and check usage every 15-20 minutes.
  - Stop cleanly at about 87-90% with STOP POINT commits, and resume after the reset.
  - Run at most 4 Next dev servers at once and one emulator walk at a time.
  - Reap leaked processes between waves.
- If every agent dies with an SSL certificate error, it is Avast's HTTPS scanning: save the work, wait, and resume.
- Give honest percentages and relative times.
- Before the session ends, write a full handoff and a prompt like this one.
