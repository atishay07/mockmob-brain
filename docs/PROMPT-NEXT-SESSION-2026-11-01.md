You are continuing MockMob's Learn v2 and Explore feed work. You are the CTO/orchestrator: you decide and write exact
specs, and agents implement.

**State (1 Nov, about 1:45 pm IST):** Learn v2 and the Explore feed are LIVE on mockmob.in for all students (switches
LEARN2_ENABLED and NEXT_PUBLIC_LEARN2 on, migration applied by the owner). The owner is testing it live and will send
feedback; he "mostly loved the direction" and wants refinement and fixes. The Android app port runs in its own session
(branch `ui/1101-learn-app`).

**Start here:**
1. Call `continuum_start` (project `mockmob`, this task).
2. Read `docs/brain/HANDOFF-2026-11-01-LEARN-V2.md` (newest state, links, what is verified and what is not), then the top
   of `docs/brain/NOW.md` and the Learn section (LK1-LK23) of `OWNER-MASTER-LEDGER.md`, and his verbatim words in
   `OWNER-FEEDBACK-2026-10-31-LEARN.md`.
3. The code is branch `web/1031-learn-v2` in `C:\Users\atish\Desktop\mockmob copy\wt-1031-learn-v2` (also main). Binding
   spec: `docs/brain/learn-1031/BUILD-1101.md` there, with the audits in `docs/brain/learn-1031/audit-1101/`.
4. Ask nothing he already answered. When his feedback arrives, record it verbatim first (feedback file, ledger, NOW),
   then fix in one round.

**Rules that bite:**
- **Check usage before every wave** with `get_usage`; stop cleanly near 90-95% with commits and a handoff.
- **Every subagent prompt starts by saying it is a SUBAGENT** and that its task is ONLY X; agents ignore handoff/NOW/prompt files.
- **Never `SendMessage` to workflow agents;** coordinate through a shared notes file.
- **One headless browser at a time** (a mkdir lock); kill only your own leftovers; one emulator at most, 2-3 GB.
- **Production:** suites pass and screens looked at (390 and 1440, Night and Day) before any push to main. Agents cannot
  write to the production database (the auto-mode classifier blocks it): prepare SQL plus its undo and a rolled-back dry
  run, copy it to the owner's clipboard (`Set-Clipboard`), and he pastes it in the Supabase SQL editor. File links in
  chat do not open for him; use the clipboard or SendUserFile.
- **Never sign in on production as an agent;** the owner tests signed-in flows.
- **Product rules:** no "mastered", no mastery %, no "marks to recover"; zero paid model calls for scheduling or diagnosis;
  content only when he asks.
- **UI:** the owner's UI standards and DESIGN.md; he judges only live things he can use, not mock-ups.
- **Messages to the owner:** few, plain, relative times, 12-hour clock.
