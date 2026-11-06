Continue MockMob as CEO/CTO in a FRESH session (any agent: Claude Code or Codex). Goal tonight: app VERSION 15, signed, walked in demo mode on the emulator in Night and Day, free of known bugs, in C:\Users\atish\Desktop\MockMob-build-15, so the owner can send it to Play closed-testing review tonight (D179). Website release after the app.

START
1. Shared brain: continuum_start with project "mockmob" (if missing: read C:\Users\atish\Desktop\AI OS\AGENTS.md and run python "C:\Users\atish\Desktop\AI OS\scripts\brain.py" start mockmob --task "version 15 finish"). Run `date` (IST, 12-hour times; record the owner's words with the REAL clock time from `date`, never a guess).
2. Repo C:\Users\atish\Desktop\mockmob copy\mockmob-next (branch feat/app-and-web holds the docs). Read, in order:
   - docs/brain/NOW.md, the LAST section "PAUSE 20 Oct 7:11 pm": every branch, worktree and exact stop point.
   - docs/brain/OWNER-FEEDBACK-2026-10-19.md from "Owner, 20 Oct 4:06 pm" to the end (D177-D187).
   - docs/brain/NEXT-PROMPT-1020-EVE.md: the vision, commands, facts and hard rules still apply (this prompt replaces only its STATE and DO sections).
   - docs/design-decisions/pass-1020/MOB-V4-BUILD.md and MOB-MINIMAL.md (Mob V4, approved); mock-ups tmp/design-1020/mob-minimal/*.png.

OWNER RULES ADDED TONIGHT (verbatim in OWNER-FEEDBACK)
- D185 (6:51 pm): the Pro key says "Get Pro" (one plan; never "See Pro plans"). No text bombardment on any screen: visual first, one short line per idea, no text boxes inside cards, no mix of big/small/bold paragraphs.
- D186 (6:57 pm): the redesigned Full mock sit sheet and explainer slide 3 are approved. "Don't make any regressive changes anywhere ... check the previous context (Continuum) ... don't break things."
- D187 (6:59 pm): record findings (breaks, fixes in progress) in Continuum checkpoints as they happen; the 95% handoff lists everything.

STATE AT 7:11 PM (SHAs in NOW.md)
- ui/1020-v15 (wt-1020-v15app) 717aa3a89: ALL Mob branches merged (mob-formats, v4-den, v4-sheets, v4-results) + integration + slide 3 + sit sheet. analyze clean; Mob unit+widget 712/712. Goldens not regenerated on the merged tree.
- ui/1020-v15-invite 3e9eb69e6: review done (4 commits), final report lost: re-run its tests and a release compile.
- ui/1020-v15-calm STOP POINT 353a98fc9: unreviewed agent work committed: review the diff (D181 first Pro ask waits for a real limit, D183 usage data on for 18+ and Rather not say, delete-account Play warning, Ask Mobi pending question forgotten on sign-out/delete), then tests.

DO, IN ORDER
1. Review ui/1020-v15-calm (git show 353a98fc9 and 2b78a0576) and finish it; analyze + onboarding/pro_nudge/you/core_data/billing tests; open its new onboarding goldens.
2. Merge ui/1020-v15-calm and ui/1020-v15-invite into ui/1020-v15 (wt-1020-v15app). analyze; full unit + widget suite (whole app); regenerate the Mob v3 goldens and any goldens the merges touched; OPEN the changed Mob ones (results run, den, sheets, start sheet) against the mock-ups; list the ~140 old non-Mob drift goldens without chasing them.
3. Demo-mode walk on the emulator (owner rule, the real check): build `-t test/device_demo/demo_main.dart` (profile or debug), install with `adb -e`, Night AND Day, 360 dp, text 1.0 and 1.3: Today, Practice + finish reveal, You + plan strip + Pro page + Wallet + invites (Have a friend's code? row), the Mob (explainer incl. slide 3, den, Start a game with every format, Full mock sit sheet, a race, the results run with celebrations, This week / Your chain / Shelf / Mob settings sheets, Mob hours), sign-in screens. Look for text bombardment (D185) and anything basic-looking. Screenshots to tmp/walk-1020/app-v15 with JUDGEMENTS.txt. Fix, re-walk fixed screens.
4. Signed build 1.0.17+15 (versionCode above 13): in flutter_app `bash tool/build_release_aab.sh --bump --sell`, APK too; key.properties from C:\Users\atish\MockMob-keys if missing (NEVER print or commit keys); launch check; copy AAB + APK + README with SHA-256s + symbols + OWNER-STEPS.md (how to upload to closed testing) to C:\Users\atish\Desktop\MockMob-build-15.
5. Website: as NEXT-PROMPT-1020-EVE.md step 5 (merge web/1020-mob-fulltogether-price, web/1020-referral-any, web/1020-mob-hours with its migration RENAMED to 20261020151000, web/1020-egress after verifying its STOP POINT; suites; next build --webpack; deploy by pushing main; migrations on production with pre/post checks and undo; smoke; STATUS.md; MOB_FORMATS_ENABLED=true only after price enforcement is live and smoked).

KNOWN FOLLOW-UPS (not blockers; say so in the release notes for the owner): den join/reaction acts not wired (widgets/fold_acts.dart ready); v3.fix (den Now card steps 2-3) has no server field.

HARD RULES (unchanged): no walks, seeds or tests against Supabase staging or production (demo mode and local tests only; production only for the web deploy, its migrations and a smoke). Flutter only via `MOCKMOB_FLUTTER_SLOTS=6 bash tool/flutter_locked.sh <args>` in flutter_app. One emulator (AVD mockmob_budget, -memory 3072, lock %TEMP%\mm-emu-lock; this session booted it at 6:56 pm, take the lock over). Kill only processes you started, by PID; never taskkill dart.exe by name while another agent runs Flutter. Subagents: few, one writer per worktree, never SendMessage a workflow agent; check usage every 10 minutes (on a Pro account two Sonnet agents plus the main session used about 45% an hour); at 95% stop everything, STOP POINT commits, NOW.md, next prompt, Continuum checkpoint. Copy rules: plain, warm, no exclamation marks, emoji, arrows or hype; never "lost", "behind", "last"; numbers with units; 12-hour times; 44 dp targets; reduced motion; Night and Day first-class. Commit messages end with a Co-Authored-By line for your model. End every update to the owner with "Things needed from you right now:" or "Nothing needed from your side".
