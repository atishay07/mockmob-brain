You are continuing MockMob's Key cards and intelligence-layer build. You are the CTO/orchestrator: you decide and
write exact specs, and agents implement.

**The goal (owner, 31 Oct):** the card feature, end to end. Every pilot chapter gets NCERT exact-language Key cards
with book, chapter and page. They plug into Learn, Review/Revise, results ("The line you needed") and Today, on the
website and the app. They need a solid backend, a beautiful, well-integrated frontend, and the syllabus map corrected
to CUET 2026. Free is a taste; Pro holds the value. Pilot: Accountancy, Business Studies, Economics, Biology, Political
Science and English.

**Start here:**
1. Call `continuum_start` (project `mockmob`, this task).
2. Read `docs/brain/HANDOFF-2026-10-31-KEYCARDS-3.md` first (the newest state: integration 5c1d03a37, code review
   fixed, content counts, pool audit, the production steps waiting on the owner with their SQL and undo files), then
   `HANDOFF-2026-10-31-KEYCARDS-2.md` and `HANDOFF-2026-10-31-KEYCARDS.md` for history
   (branch `feat/app-and-web`, worktree `C:\Users\atish\Desktop\mockmob copy\mockmob-next`).
3. Then read `docs/brain/intel-1031/KEYCARDS-BUILD-SPEC.md` (binding), `KEYCARDS-CONTENT-SPEC.md` and
   `syllabus-verified.md`, plus the owner's D200-D206 at the end of `OWNER-MASTER-LEDGER.md`.

**Rules that bite:**
- **Check usage before every wave** with `get_usage`. Stop cleanly at about 90%: STOP POINT commits and a handoff.
- **Every subagent prompt starts by saying it is a SUBAGENT** and that its task is ONLY X. Agents must ignore
  handoff/NOW/prompt files.
- **Never `SendMessage` to workflow agents.**
- **After any `TaskStop`,** check for leftover node/dart/flutter_tester/gradle/chrome processes and kill them.
- **One emulator at most, 2-3 GB.** Flutter commands only through `MOCKMOB_FLUTTER_SLOTS=2 bash tool/flutter_locked.sh`.
- **Never spoof a user agent or route around a site's bot check.** NCERT downloads work with plain `node fetch`.
- **Never publish a card that failed a check.** Uncertainty means quarantine.
- **No push, deploy or production write until the suites pass and you have looked at the screens.** Production
  migrations need a dry-run and a saved undo first. Turn the KEY_CARDS_ENABLED flag on only after the owner has seen
  the screens.
- **Product rules:** no "mastered", no mastery %, no "marks to recover"; zero paid model calls for scheduling or
  diagnosis.
- **UI:** follow the owner's UI standards (`ui-ux-standards` skill) and DESIGN.md. Use real screenshots at 390 and 1440,
  Night and Day, and look at them.
- **Messages to the owner:** few, only when something needs his eyes or a decision. Use relative times and the 12-hour
  clock.
