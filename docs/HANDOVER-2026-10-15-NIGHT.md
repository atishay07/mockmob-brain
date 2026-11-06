# MockMob handover, 15 Oct 2026, about 00:50 IST

This is the handover from session cc0bf1af (Opus 5.5, account support@mockmob.in).

## Shipped tonight (all live or delivered)

**App: release APK delivered to the owner.**
- File: `tmp/apk/MockMob-phase2-release.zip` (`.apk` inside; package in.mockmob.app, 31.6 MB, obfuscated).
- Built from ui/phase2 snapshot fcc2e672 in worktree `wt-release`, with `dart_defines/prod.json` copied in.
- Contents:
  - the new bar (Today, Practice, Start, Review, You) with the live capsule;
  - Material icon pairs (home, quiz, fact_check, avatar);
  - motion, spacing and Night/Day fixes;
  - robustness fixes;
  - the photo-real 3D subject objects restored (`SubjectEmblem.objectArt`);
  - the approved art set (welcome hero with live Mobi, plan seal, milestone, empty states);
  - round 2 fixes (except the audit+onboarding fixer).
- Full suite NOT run on it.

**Website (main = e1773d6a, deployed by push):**
- Mistake Repair reliability:
  - passage sent to the model;
  - NTA shuffle compare (it also fixed hidden keys on NTA result pages);
  - 90 s route budget with per-call timeouts;
  - credits never kept on a failure;
  - stuck-reservation release and a daily sweep in the cron;
  - honest error codes and a log line per failure;
  - narrowed word filter;
  - Haiku 5.5 fallback.
- Web repair client: fresh id after a charged-0 failure, 95 s abort, server messages, mojibake fixed.

**Root cause of repair failures since 5 Oct:** Vercel Production had no `OPENAI_API_KEY`. The owner added it at about 00:30 IST and a redeploy was pushed (6e4b64ed). Not yet verified with a live repair: check Vercel runtime logs (project prj_uSolddribHQDl1mM5AKxg3O9qCIu, team team_V5PhMz9hqV42vblUMcvhYqoN).

**Database (production isrxrxzjocewrdureyhp, via Supabase MCP; standing owner grant in the AI OS decisions log):**
- Migration 20261014183050 adds the claude-haiku-5-5 price row.
- Authored wave 2 published: 382 questions plus 1 case set, plan 73b63070.
- Restore file: `mockmob-hotfix/docs/brain/reports/authored-publish/authored-publish-restore-2026-10-14T18-48-05-150Z.json`.

**Disk:** C: had filled to 0 GB. 39.5 GB was cleared, and `flutter_locked.sh` now sweeps leftovers older than 6 h (memory `disk-hygiene.md`).

## Update 00:55 IST: round 2 complete, v2 APK delivered
- Round 2 (wf_113e84d6-978) finished. Analyze is clean, and unit tests pass: 487 + 743 + 1636. Not run: account_access, art, art_scenes, home_widget, platform, tools.
- ui/phase2 5a5e7852 was merged into feat/app-and-web as 156ab495.
- Release APK v2 built in mockmob-next (obfuscated) and delivered as tmp/apk/MockMob-v2-release.zip (apk MockMob-v2-156ab495.apk, sha1 f9fe1e2c).
- Still open after round 2:
  - the Practice goldens (practice_golden_test, practice_finish_golden_test) and possibly some core goldens are stale: regenerate them and look;
  - the 3.3 s cold-start hold (splash_screen.dart);
  - onboarding-05 (deep link lost on process death);
  - emblem size snapping;
  - the Mobi greeting bubble overlap (check the audit fixer's report in the journal);
  - an emulator check of fast Previous/Next.

## In flight or next

1. **Round 2:** workflow wf_113e84d6-978 (script `tmp/workflows/app-phase-2-round2.js`). Its last fixer (audit+onboarding: welcome overflow, clipped-icon audit, Mobi bubble covering the greeting, 3.3 s cold-start hold) and check-2 were still running.
   - When done: commit in wt-phase2, merge into feat/app-and-web (already merged up to fcc2e672 as ad4431f2), and build a new release APK. Rebuild in wt-release or mockmob-next. If CMake says "Permission denied" (antivirus), delete `build/.cxx` and retry.
2. **Full test suite** on feat/app-and-web (`bash tool/flutter_locked.sh test -j 1 -r failures-only`, 40 to 60 min). Goldens will need regenerating per area.
3. **Recording:** profile demo recording of the final build for the owner.
   - `tool/emu_rec.sh` and `tool/frame_sheet.py`: tap by label, record, contact sheets. ffmpeg comes from pip imageio-ffmpeg (`--use-feature=truststore`).
   - AVD mockmob_budget, -memory 2048. Stop the Gradle and Kotlin daemons first for RAM.
4. **Vercel housekeeping:** ask the owner.
   - Six projects named mockmob* exist (mockmob, -1uhb, -mmzs, -pf37, -nxud, -sjsj). If all of them build each push, that burns Hobby limits.
   - A `MOCK_AI` variable is set in Production; its value is unknown.
5. **Repair v2:** the richer paid repair, from `docs/brain/REPAIR-LAB-AUDIT-2026-10-14.md` section 5, built with web and app parity.
6. **Subject art:** regenerate 4 subject renders (Accountancy calculator plus balance sheet, Computer Science laptop with code, Business Studies briefcase, Languages book with Indian scripts) in the same lamp-lit style. Show old next to new, and ship only the owner's pick.
7. **Owner-only:** upload key, Google client ID, Play Console.

## Owner's latest direction (15 Oct)

- Speed: he wants hour-long tasks done in minutes. Fan out agents, and do not wait on full suites before building.
- No regressive changes, and preview before any taste change.
- Every feature is built the same on web and app.
- Fast mode was turned on for this session.
- Bypass permissions are on.
- The owner approved deploys of the repair fixes and the wave 2 publish.

## Update 01:10 IST: owner's "go all out" push, both runs in flight
- **Round 3 (wf_1fb2ccb3-a45, app, wt-phase2):** cold-start hold, Mobi bubble over the greeting, onboarding deep link, stale goldens, untested unit areas, then check-3.
- **"Alive and refined" (wf_ede58103-677):**
  - Plan: 25 ideation agents, then 1 planner, then about 16 build packets (11 app in wt-phase2, 5 web in worktree `wt-web-refine`, branch web/alive-1015 from origin/main), then app and web checks.
  - Goal: Mobi with a full emotional range everywhere it fits, motion and micro-interactions on every control, illustration and generated-art upgrades, refined features (including repair v2) on web and app.
  - Resume: Workflow({scriptPath: its session script, resumeFromRunId}). Scripts are in the session's workflows/scripts folder.
- **When both finish:**
  1. Commit wt-phase2 and merge into feat/app-and-web.
  2. Build release APK v3 in mockmob-next (obfuscated, zip it for the phone) and send it.
  3. Free RAM (stop the Gradle daemon), boot the emulator, then install the profile demo (`build apk --profile --target-platform android-x64 -t test/device_demo/demo_main.dart`). Record with tool/emu_rec.sh and send the clips.
  4. Web: review the web/alive-1015 commits and test lines. The owner has allowed deploys tonight, so push to main when green, and check Vercel.
- **Owner rule (01:05):** keep working until usage is at about 97%. Write a handover if a reset is more than 30 minutes away.

## Update 02:15 IST: final state of this session (usage at 85%, nothing new started)
- **Subject art:** Accountancy (calculator on a Debit/Credit ledger) and Computer Science (brushed-brass laptop) were regenerated at the old set's quality and are in wt-phase2 assets. object_art.dart has updated bounds; test/unit/art passes. **test/golden/art needs `--update-goldens`.** Business Studies and Languages keep the old renders (owner's choice). Old-file backups are in tmp/subject-art-v2/work2/old-backup.
- **Web (worktree wt-web-refine, branch web/alive-1015, 11 commits on origin/main e1773d6a, NOT pushed):** Mistake Repair v2 (trap name, explained another way, rule card, folded question, marks line, Mobi reacting), the MobiReact kit and motion kit, runner and result upgrades, review changes since the last look, Saved and Radar, Progress rhythm, Learn, nav and dock motion, Compass. The check:web agent runs the suites. **Push to main only after its suites pass** (the owner has allowed deploys tonight). Then check the Vercel deploy and the site.
- **App:** run wf_ede58103-677, 8 app build packets (today, practice, result, you-notifications, rhythm-onboarding, bar-tools, motion-kit, runner), then check:app (analyze plus 3 unit batches). Round 3 (wf_1fb2ccb3-a45): cold-start and goldens fixers, then check-3. Both write to wt-phase2 (ui/phase2), which is uncommitted since 5a5e7852.
- **The v2 recording found:**
  - finding 28: the demo resume card says "0 of 10 answered" while the capsule says 10;
  - finding 29: test scripts must tap "^Submit practice", not "^Submit".
