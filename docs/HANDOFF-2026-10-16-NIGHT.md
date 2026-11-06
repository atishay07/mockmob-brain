# MockMob handoff, 16 Oct 2026, about 02:05 IST

From session cc0bf1af (Opus 5.5). Stopped safely at the owner's 99% usage. All agents are stopped, dev servers and builds are killed, and every worktree is committed. Read `docs/brain/CTO-LOOP.md` first: the vision V1-V18, the loop, the usefulness test, the quality gate, the CEO direction and the queue.

## 1. Owner rules set tonight (all in memory and CTO-LOOP)

- **Act as CEO and CTO.** Decide from his recorded taste, and keep the loop running with parallel agents.
- **Quality gate before every deploy.** Lint, the suites and a build, then a visual critique: a dev server, headless captures of every changed page at 390 and 1440 in Night and Day, clicked with a real pointer, defects fixed. Nothing ships on tests alone.
- **Model routing.** Sonnet does the heavy lifting. Haiku takes quick tasks. Opus subagents only for complex UI/UX, extreme motion and polish. Set effort explicitly. Planning stays in the main session.
- **Design skills.** Every design agent loads ui-ux-standards first (section 10, the AI-slop list, wins every conflict), then impeccable, then frontend-design, plus his skills: emil-design-eng, high-end-visual-design, redesign-existing-projects, design-taste-frontend and minimalist-ui. **30 of his skills were installed tonight** into `~/.claude/skills`. They had been in the repo's `.claude/skills` and AI OS, where this session never read them.
- **Slop, his definition:**
  - glowing keys, sheen and edge lights;
  - drifting glow blobs and gradient text;
  - **eyebrow pills with a pulsing dot above a heading**;
  - icon-in-a-rounded-square grids, card rows, nested cards.

  He wants real typographic hierarchy, like professional sites. He rated the landing 50-60; the target is 90.
- **Product focus only.** Marketing, WhatsApp and phone sign-in, abandoned checkout and the share card wait until January (CTO-LOOP Q14).
- **iOS:** none until there is evidence. iPhone is about 7.6% of sign-ups.

## 2. Live now (www.mockmob.in)

- `3be06112`: usage fixes 1-4. `d9e290eb`: fix 5 slim practice start. `3fc0095b`: landing round 1 plus Mistake Lab slice 3.
- **`77713336` was pushed at about 01:58 and was still BUILDING when the session stopped. Verify it first** with the Vercel MCP list_deployments, get_runtime_errors and curl on /, /pricing and /api/stats. If it failed with a cron-limit error (vercel.json now has 3 crons), remove the rebuild-nta-index cron entry and redeploy.
- What it contains:
  - arena on phones pass 3;
  - the credits page with history;
  - the self-maintaining NTA index code (inert until the table exists);
  - the conversion funnel (off until FUNNEL_ENABLED=true);
  - website motion parity;
  - 6 fixes from the visual critique.
- **Not applied to production yet:**
  - the funnel_daily migration (`supabase/migrations/20261015233000_funnel_daily.sql`, with its undo, dry-run on staging);
  - the nta_question_index migration plus the index build (`docs/brain/RUNBOOK-NTA-QUESTION-INDEX-2026-10-15.md`; needs CUET_EVIDENCE_SIGNING_KEY in Vercel production).

## 3. Not live: branch by branch

| Worktree, branch | State | Next |
|---|---|---|
| wt-land2, web/land2-1015 | Landing from his notes: hero v4 (b6c40be4, de-slopped, typed line), fast-scroll fix, no empty band, sample with a subject picker, state-aware dock, English pass, Start key centred, plus group 1-3 de-slop rebuild partial (WIP d9c3c52f) | Finish the de-slop rebuild from `mockmob-next/tmp/landing-1015-night/SLOP-AUDIT.md` (groups system, lab and rest; read the group handovers in the brain), the hero follow-up (live count must be one stable true number, Mobi placement on desktop, the sample card's dots), the cleanup, then the critic with a score out of 100. Show the owner on a local server before deploy. |
| wt-lab4, web/lab4-1015 | Mistake Lab slice 4 web, truth reviewed (f2d12263) | Its web check found 2 merge conflicts (handover 01:09: merge order arena3, mobi, lab4, you; arena3 and you are already live). Apply its 2 migrations to production (standing DB grant; save, dry-run, undo, STATUS.md). Decide the owner readings it flags (retirement reading; key-quality 13 flagged vs 5 with a 20 gap). Run the visual gate, then deploy server first. |
| wt-mobi, web/mobi-1015 | Mobi rig v2 on the web (5b2038f2) | Visual gate on /preview/mobi (mid-motion never seen), merge, deploy. |
| wt-colleges, wt-crash, wt-names, wt-learn | One My colleges list (server and web), self-hosted crash reports (server; the app half is on ui/phase2), one name per concept on the arena, concept checks with life on the web | Each has passed its own tests. Merge into one deploy batch from origin/main, run the gate, apply the colleges and app_errors migrations, deploy. |
| wt-phase2, ui/phase2 (app) | Mobi rig v2, lab4 app, You hub, credits page, Q12 finish items, M4 learn feedback, evening loop, critic kit L, critic packets A, B, C, F, H, J, K and G cut mid-work (WIP cfc81867) | Make analyze clean and run the unit tests, then finish the cut critic packets from `docs/brain/DESIGN-CRITIC-2026-10-16.md`, then open the goldens, merge into mockmob-next feat/app-and-web, and build APK v10 (send it; install over adb if the phone is connected). |

## 4. Next after that (CTO-LOOP queue)

- **Arena de-slop pass.** The same audit method as the landing: the arena still has dot eyebrows ("Friday, 16 October", "Account"), appended arrows and subject tile grids.
- **Critic packets D and E:** recap and result; Review, repair and the rules statistics in plain words.
- **Q13 landing calm-down,** after the de-slop pass.
- **Mobi everywhere at real moments.**
- **Q4 app half** of My colleges.
- **Play Store prep** (owner keys).

## 5. Facts learned tonight

- 1,639 accounts. 93% signed up in May 2026. 9 signed in during the last 30 days.
- 98 students ever paid, Rs 8,238 in total (62 season pass, 36 monthly). 109 more started a checkout and never paid. Season 2026 marketing spend was over Rs 15,000.
- Sign-up platforms (auth sessions): Android web 52.8%, desktop 20.4%, iPhone 7.6%, unknown 19%.

## 6. Owner items

- Delete the 5 paused Vercel projects.
- Razorpay reachability, which decides when to move to Vercel Pro.
- Play Store keys.
- One live repair, to verify the v3 cost.
- The weekly backup setup (the Supabase CLI dump; the DB URL in a user environment variable).
