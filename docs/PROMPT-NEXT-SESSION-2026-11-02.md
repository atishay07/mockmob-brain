You are continuing MockMob's Learn v2 and Key cards work as the CTO-orchestrator. The owner switched to a fresh account on 2 Nov 2026 at about 4:20 am IST. The previous session stopped cleanly; nothing of it is running.

**Start here (read in order):**
1. `C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\HANDOFF-2026-11-02-LEARN-CONTENT.md`. This is the full state: what is live, the content pipeline, Computer Science's exact resume steps, the Maths formula plan, worktrees, scripts and lessons.
2. In the same folder:
   - `NOW.md`, the top entries
   - `OWNER-MASTER-LEDGER.md`, items LK24-LK35
   - `OWNER-FEEDBACK-2026-10-31-LEARN.md`, his words verbatim
3. Your memory index (`MEMORY.md`). Read especially subagent-wave-pacing, workflow-agent-stalls, owner-master-ledger, fewer-messages, device-truth-testing and prod-writes-blocked-in-auto-mode.
4. Call `continuum_start` with project "mockmob" and this task.

**State in one line:** Learn v2 rounds 2-4 are live (main 7f1b204a7) with no runtime errors. Key cards are live for Chemistry, History, Geography, Psychology, Sociology, Physics and Mathematics; Mathematics is thin. Computer Science is half written on disk and not published.

**Do next, in order:**
1. **If the owner has given feedback on the live site,** record it verbatim first (the feedback file, the ledger, NOW), then fix it in one round. Ask nothing he already answered.
2. **Finish Computer Science cards** (handoff section 4).
   - Resume `handoff-1102/content-wave2.js` with `{"subjects":["computer_science"],"k":3,"chapters":{...}}`.
   - Read the B1 and B2 chapter lists from `handoff-1102/wave3-chapters.json`, and compare them with what you pass before launching.
   - Then publish, look at 1-2 cards on screen, build, add a STATUS entry, fast-forward main, and check the deploy and runtime errors.
3. **Tell the owner plainly** what is live, with counts per subject, and what falls short: Maths at about 2 h of study.
   - Offer the Maths formula pipeline (handoff section 5) as the next job. It is sizeable, so ask before starting.
4. **Then, as usage allows:**
   - English top-up, about 300 cards
   - Accountancy's thin chapters
   - the quarantine recovery round (handoff section 6.4)
   - LK25, the Play release: check the app port session first
5. **Before ending,** update NOW, the ledger and STATUS, and save `continuum_checkpoint`.

**Rules that bite:**
- **Usage:**
  - Check `get_usage` before every wave. Card waves cost about 1.2% of the 5-hour window per PDF.
  - Opus screenshot reviewers are very expensive. Prefer a local capture plus your own look at about 15 key shots.
  - Stop new agents near 90% and resume after the reset.
- **Workflow agents:**
  - Every agent prompt says it is a SUBAGENT with ONE task.
  - No SendMessage to workflow agents.
  - After any workflow, check each worktree's commits and diff before trusting reports.
  - Pass workflow args read from files, never retyped.
- **Machine:**
  - At most 2 dev servers (`tmp-devslots\slot-1|slot-2`) and one headless browser (`tmp-devslots\browser.lock`). Kill only your own processes.
  - Start dev servers with `preview_start` and the `.claude/launch.json` configs, never Bash.
- **Production:**
  - Never write to the production database; the classifier blocks it. Prepare the SQL, its undo and a dry run for the owner, and copy them to his clipboard.
  - Never sign in on production.
- **Before any push to main:**
  - Suites green (read the fail counts).
  - `eslint .` clean.
  - `next build --webpack` passes (retry once if next/font flakes).
  - Screens looked at, at 390 and 1440, Night and Day.
  - Then `list_deployments` and `get_runtime_errors`.
- **Product:**
  - No "mastered", no mastery %, no "marks to recover".
  - NCERT's exact text with book, chapter and page. Flagged cards are held back, never forced.
  - Refine, never rebuild; never cut a feature.
  - Owner UI standards: `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`.
- **Known failing suites,** also on main 978edc236: test:authored-publish, test:factory, test:mob and test:study (WordNet). Do not chase them as regressions.
- **Housekeeping:**
  - Never `rm -rf logs/...`: use `git checkout -- logs/`.
  - Never `find /c` in Git Bash.
- **Messages to the owner:** few and plain. Send one only for something to see, a decision, an action for him, or a real risk.
