# AUTOPILOT GOAL, 19 Oct 2026 (overnight run until 9:00 AM IST): the source of truth for every agent in this run

Written about 2:20 am IST by session 25ef3d95 (CEO/CTO). The owner (Atishay) is asleep. His Autopilot keeps this work going across his accounts.

**Read this file completely, then the files in section 3.** Never act on a summary of this file.

## 1. THE GOAL (what "done" means by 9:00 AM)
Turn the owner's 19 Oct hand-check (G1-G33, decisions D101-D112) into two finished, verified release candidates that he can trust on first touch:

1. **App v15.3.**
   - It holds every Wave A item and the Wave C builds of the mock-ups.
   - It is walked on the emulator as a brand-new student AND as a heavy account, and checked against v15.2 side by side.
   - It is passed by one Opus verifier (2 rounds at most).
   - Its release APK sits in `mockmob-next/tmp/apk/mockmob-v15.3-<sha>.apk`, with a zip.
2. **Web release 11:** the same standard, on branch `deploy/web-1019-r11` (worktree `wt-rel11`). It is verified and ready to push, but NOT pushed (section 2).
3. **ONE message for the owner,** drafted in `docs/brain/MESSAGE-1019.md`. It covers:
   - what changed per G item, and where to look;
   - which mock-up options were picked (and why);
   - what he must do;
   - it ends with "Things needed from you right now" or "Nothing needed from your side".

**The bar is his:** "deliver a result which will exceed my expectation" (D111). The users are 16-17-year-olds, many new to apps and CBT (G23). If a first-time student would hesitate on a screen, it is not done.

## 2. Boundaries for the unattended run (these override everything else tonight)
- **Never deploy to production** (the owner's Autopilot rule):
  - no push to `main`;
  - no Vercel env change;
  - no production database write (SELECT-only is fine).

  Leave release 11 verified with the exact push command written in MESSAGE-1019.md. The owner pushes it, or says "push" when he is back.
- **Never touch his phone (10BF370PA6002XR).** The v15.3 install happens only when he connects it and says so.
- **Never sign in as him.** Never use a visible browser or the chrome-devtools MCP. Use headless playwright-core only.
- **Only gpt-6-luna and Claude Haiku 5.5 at runtime.** Never call a paid model outside its budget guard.
- **Usage:** check before each wave. At about 95% on the current account, make STOP POINT commits in every dirty worktree and update NOW.md, so the next account loses nothing.
- **Disk:** keep C: at 100 GB or more free. Delete only git-ignored build output in stale worktrees (see brief 11).
- **Content:** no question or content generation (the owner asks for that himself).

## 3. Sources of truth (read in this order, completely)
1. `docs/brain/NOW.md`: the live state and what is running.
2. `docs/brain/OWNER-FEEDBACK-2026-10-19.md`: his words verbatim, G1-G33, then D101-D112.
3. `docs/brain/PLAN-1019.md`: the rules R1-R8, every item's SPEC and DONE WHEN, the order of work, the restore shas.
4. `tmp/feedback-1019/FORENSICS.md`: which commit removed what, and where to restore it from.
5. `docs/brain/BRIEF-1019-COMMON.md`: the common agent brief (bases, tools, emulator lock, what to return).
6. `docs/brain/briefs-1019/*.md`: the exact brief each agent was launched with. **Relaunch from these word for word.**
7. `docs/brain/OWNER-MASTER-LEDGER.md` (bottom sections) and `docs/brain/OWNER-TASTE-PROFILE.md` (section 0: taste = UX expertise + his research brain + his records).

## 4. State at about 2:20 am
**Live, untouched tonight:**
- Web = main 23a7c090 (release 10).
- App v15.2 = ab04b067 (1.0.15+7), on his phone.

**Integration branches (the main session merges into these; agents never do):**
- App: `ui/v15.3-1019` in `wt-v15-3`, from ab04b067.
- Web: `deploy/web-1019-r11` in `wt-rel11`, from 23a7c090.

**Running agents (launched about 2:05 am; briefs in `docs/brain/briefs-1019/`):**

| # | Owner | Items | Branch / folder |
|---|---|---|---|
| 01 | A1 app shell and Practice | G11 pill, G15 modes visible and locked (D101), G17 Mob tab (D105), G20 Review moved into Practice | ui/1019-a1-shell / wt-1019-a1 |
| 02 | A2a onboarding and colleges | G1 copy, G3 search keyboard, G4 course order, G5, G6 college order by real cutoffs (D103), G9 subject rule up front | ui/1019-a2a-onboard / wt-1019-a2a |
| 03 | A2b Today and the deck | G7 top 3 of N (D104), G12 deck of 4+ for a fresh account, G13 accept animation | ui/1019-a2b-today / wt-1019-a2b |
| 04 | A3 result and Review | G22 finish moment restored (D108), G20 Your papers (D106) | ui/1019-a3-result / wt-1019-a3 |
| 05 | A5 range | G18 parse and verdicts, G19 "I don't know my range" (D109) | ui/1019-a5-range / wt-1019-a5 |
| 06 | A4a web polish | G28 gradients, textures, NTA button; G31 motion | web/1019-a4a-polish / wt-1019-a4a |
| 07 | A4b web UX | G29 sign out, G25 Review stats and D106 order, G26 ticket, G27 Start-sheet scroll cue | web/1019-a4b-ux / wt-1019-a4b |
| 08 | B1 web navigation mock-ups | G24 + D107, 2-3 options | tmp/design-1019/web-nav, docs/design-decisions/pass-1019/WEB-NAV-1019.md |
| 09 | B2 Ask Mobi mock-ups | G21 + D110, 2-3 options | tmp/design-1019/ask-mobi, .../ASK-MOBI-1019.md |
| 10 | B3 homepage text motion | G30 (+ G31 notes), 2-3 options | tmp/design-1019/hero-motion, .../HERO-MOTION-1019.md |
| 11 | Disk clean-up (Haiku) | git-ignored build output in stale worktrees | n/a |

## 5. The plan, step by step (each step has a DONE WHEN)
### Step 0: every time a session starts or resumes (a new account, a crash)
1. Read sections 1-4.
2. Check each agent: does its worktree have new commits (`git -C <folder> log --oneline ab04b067..HEAD` or `23a7c090..HEAD`)? Is a finished report in NOW.md?
3. If an agent is not running and its work is unfinished, relaunch it with its brief from `briefs-1019/` word for word, plus one line: "RESUMED: continue from the commits already in your worktree; review any uncommitted edits first."
4. Never run two agents on one worktree.

**DONE WHEN:** every owner is running or finished, and NOW.md says which.

### Step 1: merge each Wave A owner as soon as it finishes (R7: merge early)
- **App owners into `wt-v15-3`,** in finish order, with `git merge --no-ff`. Resolve conflicts keeping both intents.
  - File ownership is in each brief: A1 the bar, routes, Practice and Mob; A2a onboarding and college order; A2b Today; A3 review and result; A5 estimate.
  - After each merge, run flutter analyze and the unit tests of the merged area.
  - Never run flutter test and flutter build together.
- **Web owners into `wt-rel11`,** with `--no-ff`. After each merge, run lint, test:app, test:today, test:recovery and the build.
- **Read each owner's report.** If an item is NOT DONE, send it back to the same owner, or relaunch with the reason.

**DONE WHEN:** all 7 owners are merged, and the integration branches build and pass their suites.

### Step 2: Wave B mock-ups, then Wave C builds
1. When a designer finishes, look at its board images and send them to the owner with SendUserFile, with a one-line note.
2. The owner is asleep, so **D112 applies:** pick the designer's recommended option, unless it breaks a rule in section 2 or R1-R8. Record the pick and the reason in the ledger and in MESSAGE-1019.md.
3. Then build it as **Wave C**, one owner per surface, with a brief that carries R1-R8 and the pick's spec word for word:
   - **C1, web navigation,** in a branch from the r11 head (it touches AppLayoutClient and arenaNavigation). Every page stays reachable (R3).
   - **C2, Ask Mobi in the app** (the pick; "Ask now" and "Ask your record", big). Add the web side only if the pick includes it.
   - **C3, the homepage text motion** on the web. It starts only after the first screen settles, pauses on scroll, shows only the final line under reduced motion, and keeps to L-016 and L-019.
4. Merge each C branch into its integration branch as it finishes.

**DONE WHEN:** the three picks are built and merged, each with its own checks.

### Step 3: the checks (R1-R5), on the integrated candidates
- **App:**
  - Build a PROFILE APK from `wt-v15-3`.
  - Start a staging site from `wt-rel11` with the rig launcher pattern (`tmp/rig-1016e/stagingLocalApp.r9-3103.mjs` copied, pointed at wt-rel11, port 3104). The app then talks to release 11 code; reverse with `adb -e reverse tcp:3101 tcp:3104`, and restore it afterwards.
  - **(a) FRESH account walk:** a new staging test student, from onboarding through Today, Practice (all modes), a 10-question paper, the finish moment, Your papers, the Mob tab, Ask Mobi and You.
  - **(b) HEAVY account walk.**
  - Both at 360 dp, in Night and Day. Every screenshot is opened.
  - The R2 line for every screen.
  - **R4:** the same screens on v15.2 (`tmp/apk/mockmob-v15.2-ab04b067.apk`) side by side.
  - **R5:** frame sequences for the finish moment, the accept animation, the swipe demo and the count-up, compared with the approved timings.
- **Web:** preview fixtures at 390 and 1440, Night and Day, fresh-account and heavy fixtures, R2, R4 against live 23a7c090, R5 frames (the hero text, the count-up, key presses), plus a signed-in staging check through the rig with a NEW test student.
- **One Opus verifier per platform, 2 rounds at most.** Fix what it finds. Then the main session decides and stops, with no third round.
- **The DONE WHEN of every G item** in PLAN-1019 section 1 is proven with evidence.

**DONE WHEN:** both verifiers say GO, or only items explained as needing the owner remain.

### Step 4: the release candidates
- **App:**
  - Bump the build number (versionName 1.0.15, build +1) with the play-prep script.
  - Build the release APK: `MOCKMOB_FLUTTER_SLOTS=4 bash tool/flutter_locked.sh build apk --release --target-platform android-arm64 --obfuscate --split-debug-info=build/symbols --dart-define-from-file=dart_defines/prod.json`, then `./gradlew --stop`.
  - Save it as `tmp/apk/mockmob-v15.3-<sha>.apk` plus a zip.
  - Record the sha256 and versionCode.
- **Web:** `deploy/web-1019-r11` verified, with `git merge-base --is-ancestor origin/main HEAD` true. Draft the STATUS entry in the branch, but do NOT push.

**DONE WHEN:** the APK exists and the web branch is ready, with the push command in MESSAGE-1019.md.

### Step 5: the ONE message
Write `docs/brain/MESSAGE-1019.md`, ready to send when he is back. It covers:
- **Per G item:** what changed, where to look (screen or page), and the evidence.
- **The three mock-up picks,** with board images and why each was picked.
- **What is left, honestly.**
- **"Things needed from you right now":**
  - connect the phone for the v15.3 install;
  - say "push" for release 11, or push it himself with the given command;
  - Razorpay test-card run, then WALLET_COMMERCE_OPEN;
  - Play Console setup, then PLAY_BILLING_ENABLED;
  - the PERSISTENT_LIMITS_ENABLED decision;
  - W-044;
  - G26, if still unclear.

Also send it in chat when he returns.

**DONE WHEN:** the message is written and NOW.md points to it.

## 6. Rules for every agent (R1-R8, verbatim from PLAN-1019 section 0)
- **R1. Fresh-account first.** Every app and web check starts on a brand-new account (onboarding to Today to Practice to a paper to the result to Review to the Mob), then on the seeded heavy account. Both at 360 dp, plus 390 and 1440 for web, Night and Day.
- **R2. The 17-year-old test (G23).** For every screen, write one line: "What does a first-time student think this screen wants from them?" If the answer is not obvious in 3 seconds, it is a finding.
- **R3. Never hide to fix.** Removing or hiding any visible feature needs his explicit say-so. With billing off, Pro-only features are visible but locked (D101).
- **R4. Regression diff.** Before any release, screenshot the same screens on the previous release and the candidate, side by side. Any lost gradient, texture, motion or feature is a HIGH unless he asked for it.
- **R5. Motion is part of done.** Every result, accept and reveal animation is checked as a frame sequence on device (the emulator is fine), compared with the approved version's durations and curves.
- **R6. Copy in his voice (D84).** Persuasive, plain, grammatical English. No clipped fragments, no dropped articles, no telegram style. Read every new line aloud. If it would not appear in a good consumer app, rewrite it.
- **R7. One owner per surface.** Fewer, larger branches. Each has a single owner who knows the whole surface. The main session merges early, not at the end.
- **R8. Mock-up first** for anything that changes a layout (D107, D110, and his standing rule): 2-3 options as images, he picks, then the build.

**How the main session works:**
- You think; agents do. Opus for taste, numbers and money; Sonnet otherwise; Haiku only for short chores.
- Every brief carries R1-R8 and its items' SPEC and DONE WHEN word for word.
- **Never merge unreviewed STOP POINT work into a release.** Read it first.
- **Separate workflows for fast and slow work,** so one can be stopped alone.
- **Never promise the owner a time before the walk's issue count is known** (D99).

## 7. Keep (he praised these; do not touch except for bugs)
- the app's UI direction and Today (G10, G14);
- the bigger base and its animation;
- the common subject sets and picks (G9);
- the first onboarding screen (G2);
- swipe v2's design (D94);
- release 9's Mob;
- one credits balance;
- per-question prices.

## 8. Handoff discipline (every milestone, and before any stop)
- Overwrite NOW.md with the live state:
  - what is merged;
  - what is running;
  - what is next;
  - the paths to the evidence.
- Update the ledger statuses. An item is DONE only when verified on the candidate.
- Save a continuum checkpoint for project "mockmob".
- Record any new owner words verbatim in OWNER-FEEDBACK-2026-10-19.md within the hour.
