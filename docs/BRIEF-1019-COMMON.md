# Common brief for every 19 Oct agent (part of your brief; read it fully before you start)

## Who it is for
The students are 16-17-year-olds preparing for CUET UG 2027. Many are new to mobile apps and to CBT. A fresh account must be complete, and nothing may be hidden (memory: audience-teens-new-to-cbt).

The owner's words for tonight are in `docs/brain/OWNER-FEEDBACK-2026-10-19.md`. The plan is `docs/brain/PLAN-1019.md`, and the forensics are in `tmp/feedback-1019/FORENSICS.md`. Read the parts that name your items.

## Bases and branches
- **App:**
  - Base: `ui/v15.2-1018` at **ab04b067**, the v15.2 build on his phone, 1.0.15+7.
  - Your worktree: `git -C "C:\Users\atish\Desktop\mockmob copy\wt-v15-2" worktree add -b <your branch> "C:\Users\atish\Desktop\mockmob copy\<your folder>" ab04b067`. If the folder already exists, reuse it.
  - Integration branch: `ui/v15.3-1019` in `wt-v15-3`. The main session merges your branch there. Never merge into it yourself.
- **Web:**
  - Base: main **23a7c090**, release 10, which is live.
  - Your worktree: `git -C "C:\Users\atish\Desktop\mockmob copy\wt-rel10" worktree add -b <your branch> "C:\Users\atish\Desktop\mockmob copy\<your folder>" 23a7c090`.
  - Integration branch: `deploy/web-1019-r11` in `wt-rel11`. The main session merges.

## Tools and limits
### Flutter
- Run it only through `MOCKMOB_FLUTTER_SLOTS=4 bash tool/flutter_locked.sh <args>`, from flutter_app.
- Unit tests run with `-j 3`.
- NEVER run `flutter test` and `flutter build` at the same moment in one worktree. The test run rewrites GeneratedPluginRegistrant, and the build fails.
- Run `./gradlew --stop` after builds.
- Copy `dart_defines/*.json` in from `mockmob-next\flutter_app\dart_defines`. Never commit them.

### Emulator
The emulator is SHARED, so only one agent uses it at a time.
- **Acquire:** `mkdir "C:\Users\atish\AppData\Local\Temp\mm-emu-lock"`. It fails while another agent holds the lock; retry every 30 s. Then write your name into `owner.txt` inside it.
- **Use:**
  - AVD `mockmob_budget` with `-memory 3072 -no-snapshot-save`;
  - `source tool/android_env.sh`, then `adb -e` only;
  - a PROFILE build with `dart_defines/phone-relay.json`.

  Keep each session under 15 minutes.
- **Release:** kill the emulator, then `rmdir /s /q` the lock folder.
- NEVER touch the device 10BF370PA6002XR (the owner's phone).
- **Rig:** see `mockmob-next\tmp\rig-1016e\RIG-READY.md`. Sign in with a staging OTP. Fresh accounts are NEW staging test students: create them through the staging OTP flow the rig documents. Never use the owner's account.
- **Staging sites:**
  - 3101 runs old rig code;
  - 3103 runs release 9 with the Mob ON;
  - point the app with `adb -e reverse tcp:3101 tcp:3103`, and restore it afterwards.

### Web
- node_modules is a junction to `mockmob-next\node_modules` (19 Oct 3:30 am: `mockmob-hotfix\node_modules` lost its scoped packages; never link there). Create it with PowerShell `New-Item -ItemType Junction`. Never run npm install.
- **Removing a worktree (19 Oct 12:48 pm: a removal followed the junction and wiped the shared node_modules for every web worktree and the staging rig):** stop your dev server and Chrome, then delete the junction FIRST with `cmd /c rmdir "<worktree>\node_modules"` (never Remove-Item -Recurse, rm -rf or git worktree remove while it exists), check that `mockmob-next\node_modules\next\package.json` still exists, then `git worktree remove --force`, then check again. The shared folder is now installed from release 11's lockfile (`npm ci` from wt-rel11's package-lock.json).
- `.env.local` comes from `wt-batch2` and points at PRODUCTION. Use the preview fixtures (`/preview/...`) only. Never sign in or write data with it.
- Run `NODE_OPTIONS=--max-old-space-size=4096 npx next dev --webpack -p <your port>`. Next refuses a second dev server in the same folder.
- Headless Chrome only, through playwright-core at `C:\Users\atish\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules\playwright-core`, with your own temp profile. Never chrome.exe directly, a visible browser or the chrome-devtools MCP.
- Night mode: localStorage `mm:theme:v1` = `dark`.

### Data and runtime
- Production database: SELECT-only.
- Only gpt-6-luna and Claude Haiku 5.5 run at runtime.

### Git and process hygiene
- COMMIT after each step. Commits end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Never git stash, never push, never write production.
- Use Python, not sed, for edits that contain backticks.
- Stop only your own processes. Never clean files outside your worktree.

## Finding the previous release, for R4
- **App:** ab04b067 (v15.2). Its release APK is `mockmob-next\tmp\apk\mockmob-v15.2-ab04b067.apk`.
- **Web:** live main 23a7c090. The restore shas are in FORENSICS.

## What you return
- **Per item:** DONE or NOT DONE, with the DONE WHEN proof: test names, screenshot or frame paths you opened, measurements.
- **Per screen you touched:** the R2 line, "What does a first-time student think this screen wants from them?", with your answer.
- **R4:** any lost polish you found or restored.
- **Your branch head.**
- **What you could not finish,** and exactly why.
