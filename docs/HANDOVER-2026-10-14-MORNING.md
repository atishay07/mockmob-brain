# MockMob handover, 14 Oct 2026 morning (about 08:10 IST)

Session: Claude Code session `cc0bf1af` (Opus 5.5), on the default login (support@mockmob.in, Mockmob team). It ran from about 22:50 IST on 13 Oct to about 08:10 IST on 14 Oct. The owner (Atishay) stopped it and is continuing in another agent.

**Everything is stopped:**
- No agents or workflows are running. The last agent was stopped mid-task; see WIP 2209123 below.
- The emulator, Gradle daemons and every flutter/dart process are stopped, and the Flutter lock slots are cleared.
- The relay watcher (`AI OS/scripts/relay.py watch`, pid 35144) is stopped. **The "Continuum Relay Logon" scheduled task is still ENABLED**, so the watcher starts again at the next logon. Disable it if you don't want that.
- Nothing has been pushed or deployed. No production data was written.

---

## 1. Where this session started, and what it checked first

**Start point**
- The previous handover, `mockmob-next/docs/brain/HANDOVER-2026-10-13-NIGHT.md` (written 22:50 IST 13 Oct by relay fork 02ef8ecc), plus the continuum handoffs (newest 20261013T171526Z-43564e2c).
- `continuum_start` failed through MCP, so `brain.py start` was run by hand.

**Audit of every worktree before doing anything (13 Oct, 22:55 IST)**
- **mockmob-next** (`feat/app-and-web` at 7f14970):
  - 2 uncommitted edits in `src/app/privacy/page.js` and `src/app/account-deletion/page.js` (Android reminders are local, no push token; delete path You > Account > Delete account).
  - Traced to round-3 package pkg-02, whose brief said "edits the public web pages in source only and does not deploy them". There is no FCM in the app.
  - Committed as **6be644d**. Not deployed.
- **mockmob-hotfix** (`fix/nta-mode` at ad2023c): only pipeline log noise under `logs/` and untracked `tmp/`. Left alone.
- **mockmob-web2** (`fix/web-state-home` at 1dc44b9): clean apart from `tmp/` and `.next-staging/`.
- **mockmob-phone**: detached HEAD at 2e85f0f with about 170 uncommitted Flutter files from 12 to 13 Oct. Who made them could not be determined, so they were **left untouched**.
- **"mockmob copy/mockmob copy"** (main): 855 long-standing uncommitted changes. **Left untouched.**
- **mockmob-backend** (`release/app-backend` at 4bf41b8): clean. 4bf41b8 is on origin/main, so the app backend is live in production.

**Correction to the 13 Oct night handover**
- That handover said "round 3 built 10 packages". The workflow journals (782f4b0d, `wf_09e4d5a9`) show **only pkg-03 (Today) and pkg-05 (Result/Review) finished**.
- The other 8 builds, all 10 reviews and the integrate step stopped on "You've hit your session limit".
- The round-3 plan was recovered from the journal into `mockmob-next/tmp/round3-plan.json`.

**Relay at start**
- Usage read: default 100% (5-hour), and personal rate-limited. Starting the watcher would have forked this session onto a rate-limited account, so it was left off.
- Later the owner said to keep it off, and the "Continuum Relay Logon" task was disabled at about 00:50.
- At about 01:10 the owner asked for it ON ("shift to the other account in auto mode, don't stop"). The task was re-enabled and the watcher started (pid 35144).
- Defaults: threshold 98%, reset more than 30 min away, no config.json. Dry run: default 0%, skip. This session was never frozen.
- The owner warned at 01:25 that it must act only above 98%.
- Stopped now (see the top of this file).
- An old `relay_launch.py` for ticket 20261013T170815Z-f61bd4 (pid 2768) was left running from before.

---

## 2. Owner decisions given in this session (13 to 14 Oct)

- **NTA inactive grace:** 3 s for brief interruptions (notification shade, call overlay). Switching to another app counts a warning immediately. Three warnings stay. Owner's reason: "this is just a mock".
- **Screen-capture block (FLAG_SECURE):** NTA mode only, as built. The MockMob look of NTA mode is still secured.
- **"Nothing goes to ad or analytics companies":** remove it, along with all useless or filler lines ("I told previously also to not write useless stuff").
- **CSAS:** the owner disliked the CSAS/admission-portal piece and didn't know why it existed. Research found it was never an owner ask, so it was removed (below).
- **Registration window:** Feb to Mar 2027 for CUET 2027 is correct.
- **Recap back button:** researched. Never an owner ask; kept as is, so no owner decision is needed.
- **Notification pre-prompt:** may come back again and again, worded differently each time.
- **Study days:** saved on the phone only, which is fine.
- **Relay:** see section 1.
- **Testing:** emulator only. Manage RAM yourself; 3 GB AVD preferred, 2 GB acceptable. The app targets phones with 3 GB or more.
- **Overnight:** keep improving nonstop and never stop to ask. Saved as memory `overnight-autonomy-relay.md`; `emulator-ram-rule.md` was updated.

---

## 3. App: mockmob-next `feat/app-and-web`, all commits this session (oldest first)

None are pushed. The base was 7f14970.

| Commit | What |
|---|---|
| 6be644d | Web legal pages (pkg-02 source edit) |
| 53d676d | WIP: round-3 review fixes (packages 2, 3, 9, 10; unit failures; P1s) |
| 2be7a88 | WIP: packages 4, 5, 7, 8; router (learn summary, /load-failed); Mobi reduced-motion aim; NTA ended card held; deep links |
| 4d581a1 | Copy sweep (filler removed, incl. the privacy line); NTA grace 3 s; NTA intro "Mobi stays outside" removed |
| 5098239 | Road ends at the CUET window (no CSAS); plain college captions; home-screen widget; app shortcuts; share card; review prompt; in-app update; notification re-ask; warm-ups for all 15 subjects |
| b9f296d | C4 concept-checks playbook on the record page; PENDING list; Play listing draft |
| aa7ba69 | Account-deletion page names "MockMob: CUET UG Prep" (in.mockmob.app) |
| f269268 | STATUS.md: 14 Oct section |
| 54df049 | WEB-REDESIGN-PLAN-2026-10-14.md |
| 975f270 | 89 confirmed bugs fixed (first bug hunt) |
| 9028785 | Cross-area follow-ups |
| e0ecd97 | Goldens regenerated and reviewed |
| c204c83 | Visual-review fixes (108 findings) |
| 352f3f3 | Emulator walk-through fixes |
| a817371 | Stabilised: **full suite green, +2990, 0 failed; whole-project analyze clean** |
| 949cd2b | Play listing: permissions as merged |
| 8bf1bfb | Late-night rule, opaque quick-start title band, recap card 4 key |
| 846043f | 35 round-2 bugs fixed |
| **2209123** | **WIP, stopped mid-task, NOT tested** (see section 9) |

### 3.1 Round-3 close-out (53d676d, 2be7a88)

**Baseline test run on 5beb81c:** +2181 -219. About 200 golden pixel diffs plus 19 unit failures.

**Unit failures fixed**
- You/auth tests were outdated: the Security section pushed rows off-screen, the typed DELETE requirement, new receipt copy, and the `BrokenPrefs` fake.
- The runner bubble track now has 48x48 semantics nodes; the strip went from 44 to 48 dp.
- The quick-start a11y test now overrides `resumeDraftProvider`.
- The `nta_flow` test tap position.
- The result large-text overflow: `bubble_grid` (`numberHeightFor`/`heightFor`), `sheet_body`, `summary_section`.

**Haiku reviews of all 10 packages.** Findings are in `mockmob-next/tmp/round3-review-findings.md`. Fixes:
- **pkg-01 practice:**
  - The false "No <subject> paper yet" claim before attempts load.
  - FinishStage mounted on a reopened result before its rows arrived.
  - Composer controller disposal.
  - The difficulty picker clipped at 1.3x text; it now uses rows at 1.25x or more.
- **pkg-02 account:**
  - The load-failed screen (`/load-failed`) and its retry.
  - A catch-all on the delete request.
  - Recorded-state copy.
  - Google-in-browser feedback on the onboarding save step.
- **pkg-03 Today:** the Expected tag on road stops.
- **pkg-04 runner/NTA:**
  - An offline earlier submit no longer blocks a new start (it is archived and stays owed).
  - The save-retry target.
  - Focus-mode goldens.
  - New goldens: strikes 2, ended, leave, mockmob look.
  - Tests for RunnerBadPaper (49/51), FLAG_SECURE and the grace.
  - NTA-MODE-SPEC section 9.1.
- **pkg-05:** the repair celebration slot is mounted on the ending screen, so the moment is never spent unseen.
- **pkg-06 onboarding:** the stuck "Try again" key; `shownAnswer` removed.
- **pkg-07:**
  - The learn summary route is bound.
  - `mobi_loader` centred.
  - The quick-start resume title no longer reflows.
  - `MmColors.litTile`.
  - Mobi's point honours the aim under reduced motion.
- **pkg-08:**
  - goalSentence only mentions rest days when a plan exists.
  - One name per milestone.
- **pkg-09:** tooltip placement and Show me position.
- **pkg-10:**
  - Docs: BUILD-BRIEF registration Feb to Mar.
  - The WEB-PARITY index rebuilt from code, with rows H1 to H4.
  - REVIEW-ROUND1 superseded marks.
  - The overLimit copy.
- **Follow-ups:**
  - `StartPendingElsewhere` removed.
  - The NTA "Session ended" card is held until Continue, with a live submit status.
  - `zz_band_probe` test deleted.

**Manifest**
- pathPrefixes added for /test, /recovery, /progress, /study, /explore, /saved, /analytics.
- `flutter_deeplinking_enabled=false` set by me, because app_links plus ActionRouter handle links.

### 3.2 Owner-decision work (4d581a1, 5098239)

**Context research workflow** (four Sonnet agents):
- **CSAS road:** the CSAS stop and post-exam phase came from a round-3 finding with an invented end date of 30 Sep 2027. Never an owner ask.
- **Recap back button:** came from the design spec; never an owner ask.
- **Images and motion status:**
  - Mobi is a code-rigged vector with 12 acts.
  - About 31 Codex-generated webps ship.
  - The owner rejected the desk photo, and the welcome screen is now drawn in code.
  - Logo B is final, in `tmp/logo/final-B`.
  - Missing at that point: Play screenshots (now done), the website favicon (now done on web2) and a better feature graphic (v2 done).
- **Owner-ask ledger:** 67 asks; 29 done, 27 partial. It found that widget, shortcuts, share card and review prompt had never been built.

**Copy sweep** (four Haiku finders and four Sonnet fixers): about 50 filler lines removed across the you/auth, today/onboarding, practice/result/review and insights/learn/tools areas.

**NTA grace**
- `defaultInactiveGrace` is 3 s, with tests at 2 s, 4 s and re-arm.
- Spec and WEB-PARITY H1 updated.
- The NTA intro is now "Meet the exam before exam day."

**CSAS removal**
- The road ends at the CUET window; the card is hidden after 31 May 2027.
- The colleges caption reads "Last year's DU closing scores, unreserved". "UR" was later mapped to a word.
- CSAS text is kept only in tools/Compass, where it is the real data source.
- `CuetDates.counsellingStart/End` removed.

**Home-screen widget (A5)**
- Kotlin `TodayWidgetProvider` with RemoteViews; 4x2 and 2x2.
- Data comes from `lib/core/home_widget/` through home_widget.
- Tap opens deep links. It shows "Updated <time>".
- Later fixes: it redraws on alarms, fits large text, and writes the signed-out state immediately.

**Native touches (A9)**
- quick_actions shortcuts: Resume (only when a draft exists), 10-min repair, Practice 10. Icon drawables are in res/drawable and listed in keep.xml.
- A private share card (count and date only) on the repair ending and the met week.
- `in_app_review` after a held or improved result or a repair, at most once per 60 days, never in NTA.
- `in_app_update`, at most once a day; Play installs only.

**Notification re-ask**
- Cadence 2, 4 and 7 days, then every 10 days, never twice a day.
- Only after a result; never in a session, in NTA or on app open.
- Six rotating wordings.
- "Open settings" once Android has denied twice.
- The result recap reminder row follows the same policy and is no longer first-result only.

**Warm-ups**
- 30 questions picked from questions already verified locally in `mockmob-hotfix/tmp/nta-pass`.
- Each was blind-solved by 2 Haiku agents and kept only on a unanimous match.
- 3 per subject for 10 subjects; `kWarmupPoolVersion` = 2. All 15 subjects are now covered.

**ActionRouter**
- Carries the allowed query parameters (count, purpose, mode, subject, chapter...).
- The repair shortcut carries its count.
- The review prompt also fires after a held or improved result.

### 3.3 First bug hunt (975f270, 9028785)

- **Hunt:** 12 Sonnet finders, each finding checked by 2 Haiku skeptics. **89 confirmed**: 4 P0, 30 P1, 55 P2. List: `tmp/bughunt-2026-10-14.json`, grouped in `tmp/bughunt-groups.json`.
- **P0 fixes:**
  - Notification receivers (scheduled, boot, action) are now declared in the manifest. **Reminders previously never fired.**
  - Switching the NTA exam look no longer counts a warning.
  - The onboarding sheet no longer crosses accounts.
- **Follow-ups (9028785):**
  - `rhythmWatcherProvider` watched at app start.
  - `flushQuietly` used at sign-in.
  - Practice setup is a root route, so Back returns to Compass.
  - The before-you-start sheet offer is per student.
  - The TodayClock timer is released when unused; this fixed 15 to 17 router test failures.
  - The 10-min repair shortcut count.

### 3.4 Goldens and visual review (e0ecd97, c204c83)

- All goldens were regenerated: 306 changed and 8 new. The `today_road_csas` case was deleted.
- 15 Sonnet reviewers compared every image old against new. **108 issues**: 2 P1, 25 P2, 81 P3. List: `tmp/golden-review-issues.json`.
- Fixed:
  - Sign-in alignment.
  - Floating offline banners with no layout shift.
  - A drawn Google G mark.
  - Resend states.
  - The banner action pill.
  - Repair goldens now show their real states.
  - And more.
- **18 findings about the warm or brown night palette were left for the owner** (see section 8).

### 3.5 Emulator walk-through (352f3f3)

- Demo build on AVD `mockmob_budget`, x86_64, 2 GB (`-memory 2048`, because only about 3 GB was free).
- About 190 screenshots plus `tmp/app-shots/r3/WALKTHROUGH.md`.
- **No P0. 3 P1, 6 P2, 36 P3.**
- Fixed:
  - Today/Review open-mistake agreement.
  - A pinned start bar above the dock.
  - First paper named by subject.
  - Ask links carry the chapter.
  - **The opening unfolds properly on a slow start, with no ghost "mo".** The clock starts when Android reports the splash gone; 10 s safety net.
  - Opaque quick-start rows.
  - Collapsed not-attempted groups in Review and the full result.
  - Recap card 3 has a way forward.
  - And many P3s.
- Verified on the device:
  - NTA warnings: a look switch and a shade under 3 s count nothing; HOME counts "Warning 1 of 3" and locks the paper.
  - Back from Compass.
  - The road with no CSAS.
  - The share preview.
  - The widget in both sizes and themes.

### 3.6 Stabilise (a817371)

**Full suite +2990, all passed; analyze clean.** Changes:
- LearnBackScope uses `GoRouter.maybeOf`.
- Late-night lines per screen (Today "Still up? One short move, then sleep.", Practice "This one, then sleep", Review "Repair a little, then sleep.").
- Past results as "N of M".
- The brand_opening test updated.
- clock and fake_async added as dev dependencies.

### 3.7 Device re-check round 4 (`tmp/app-shots/r4`)

- All fixes passed on the device. The real release app opens to the welcome screen.
- The arm64-only release APK crashes on the x86_64 emulator unless installed with `--abi arm64-v8a`. It is fine on arm64 phones; Play uses the AAB.

### 3.8 Round 5 (8bf1bfb) and the second bug hunt (846043f)

**Round 5**
- One late-night definition, `isLateNight` in `lib/core/domain/next_move.dart` (11 PM to 5 AM), used by the greeting, Mobi and the repair length.
- `rhythm/logic/late_night.dart` still uses 11 PM to 7 AM, and onboarding uses 11 PM to 4 AM. **Not aligned yet.**
- The quick-start title band is opaque.
- Recap card 4's primary key names Today's next move.

**Second hunt** over tonight's new code (8 areas, 2 skeptics each)
- **35 confirmed**: 2 P0, 13 P1, 20 P2. List: `tmp/bughunt-r2.json`.
- All fixed in 846043f. The important ones:
  - **P0:** every reconnect retries a pending submit.
  - **P0:** a 2xx reply without an attempt id never deletes answers.
  - Archived drafts no longer outrank the live one.
  - No cross-account result writes.
  - An honest "not recorded" notification from the backup job.
  - An expired unsent draft is protected.
  - Profile reload races fixed.
  - The load-failed retry state (20 s limit).
  - **The onboarding sheet is tied to the account that started it.** I chose the owner-safe option: a sheet started while signed out is claimed by the first account that signs in, and is never written to a different account.
  - The opening honours the in-app Reduce motion setting.
  - Widget stamp and expiry fixes.
  - Shortcut and update edge cases.
  - The Today week re-samples after midnight.

---

## 4. Built artefacts (not committed; under mockmob-next/tmp/)

- **`tmp/apk/mockmob-real-release-arm64.apk`**, 30.6 MB, built 06:55 IST 14 Oct from a817371:
  - **REAL app** (`in.mockmob.app`), target SDK 36, versionCode 1.
  - Built with `dart_defines/prod.json`, which points at www.mockmob.in and the production Supabase public URL and publishable key. `GOOGLE_WEB_CLIENT_ID` is empty, so Google sign-in goes through the browser.
  - **Debug-signed**, because there is no `android/key.properties`. That is fine for sideloading; Play will reject it.
  - **It does NOT include 8bf1bfb, 846043f or 2209123. Rebuild before installing on the owner's phone.**
- `flutter_app/dart_defines/prod.json` was created this session. It is git-ignored and holds public values only, taken from `mockmob-hotfix/.env.local` NEXT_PUBLIC_*.
- `tmp/apk/demo-debug.apk`: the demo build (`in.mockmob.app.demo.debug`, sample student "Asha").
- **Merged permissions** (9 in total): INTERNET, ACCESS_NETWORK_STATE, POST_NOTIFICATIONS, RECEIVE_BOOT_COMPLETED, WAKE_LOCK, VIBRATE, FOREGROUND_SERVICE, FOREGROUND_SERVICE_SHORT_SERVICE, USE_BIOMETRIC.
  - VIBRATE comes from flutter_local_notifications.
  - The two FGS permissions come from workmanager.
  - USE_BIOMETRIC comes from androidx.biometric.
  - Documented in `docs/brain/PLAY-LISTING-2026-10-14.md`. RELEASE.md still lists 5 permissions and needs an update.
- **Play store screenshots:** `tmp/play/screens/final/01..08-*-store.png`, 1080x1920 and framed with captions. Raw captures are in `tmp/play/screens/raw/`; the script is `tmp/play/make_play_screens.py`.
- **Feature graphic v2:** `tmp/logo/final-B/play/feature-graphic-v2-1024x500.png`.
- **Docs written:**
  - `docs/brain/PLAY-LISTING-2026-10-14.md`: name "MockMob: CUET UG Prep", short and full descriptions, release notes, Data safety, content rating, screenshot plan.
  - `docs/brain/PENDING-2026-10-14.md`: every open task, grouped.
  - `docs/brain/WEB-REDESIGN-PLAN-2026-10-14.md`: owner decisions D1 to D19.
  - The STATUS.md 14 Oct section.
- **APK size audit:** `tmp/apk-size/AUDIT.md`. The Play per-ABI download is about 15.7 MB; the 29 to 30 MB figure is the arm64 APK with uncompressed native libraries.
  - A Tink keep-rule removal was tried, flagged by auto mode as security weakening, and **reverted**.
- **Owner-ask ledger and research results:** in the workflow output; summary in sections 2 and 3.2.

---

## 5. NTA (questions and engine)

**CUET-fit scoring**
- All **879 of 879** judge files exist in `mockmob-hotfix/tmp/nta-pass/fit/results/`, as `<batch>__h1|h2|h3.json`.
- The first run this session (wf_547f7cf8, 426 Haiku agents) found that **the rubric lives only on `wip/cuet-fit`**, not on `fix/nta-mode`.
  - 61 files were never written.
  - About 114 were made by judges who rebuilt the rubric from the validator.
- **161 were redone** against the real rubric (wf_2ced519e, 161 of 161 OK). Path: `mockmob-fit/docs/brain/NTA-CUET-FIT-RUBRIC.md`.
- The redo list is `tmp/nta-pass/fit/redo-pairs-2026-10-14.json`.

**New worktree: `mockmob copy/mockmob-fit`** on branch `wip/cuet-fit`
- 9471097: merge prep.
- 76cbf0d: full merge, `data/nta_fit_scores/*.json`, `scripts/nta-fit-merge.mjs`, `scripts/nta-fit-validate.mjs`.
- **Results:**
  - 2,529 quality-passed questions.
  - **2,221 pass the fit gate at 8; 684 pass at 9.**
  - 255 tens after the route rule.
  - Validation: 843 of 879 files fully valid; 63 problem rows, none unusable.
- `test:nta` 134 pass and `test:recovery` 40 pass. `test:nta-e2e` was skipped because it needs production fixtures.
- Not pushed.

**Read-only production engine run** from mockmob-fit
- Run by me in the main session. `.env.local` was copied in and deleted straight after.
- Output: `mockmob-fit/docs/brain/NTA-ENGINE-RUN-FIT.md` and `reports/NTA-ENGINE-RUN-FIT.json`, **uncommitted**. Auto mode blocked me from reading the report file because it contains production data.
- Printed summary:

| Subject | Result |
|---|---|
| Accountancy, Business Studies, Economics, Physics | 50 ("closest") |
| General Test | 45 to 46 |
| Biology | 45 to 46 |
| English | refused, 4 to 6 |
| Mathematics | 41 to 43 |
| Computer Science | 42 to 43 |
| Geography | 34 to 36 |
| Chemistry | 27 to 29 |
| Sociology | 27 to 29 |
| Political Science | 20 |
| Psychology | 20 |
| History | 17 |

- **NTA stays undeployed.** Short subjects need the question factory (paid; owner decision).

**mockmob-hotfix `fix/nta-mode`**
- 9dbf88f: `scripts/question-reorder.mjs`, `scripts/lib/listed-order-reorder.mjs`, tests (26 pass), and the `test:question-reorder` script.
- **Prepared, NOT run.** The runbook is `tmp/nta-review-cleanup/RUNBOOK-2026-10-14.md`, with lists in `tmp/nta-review-cleanup/lists/`.
  - 12 mainly-corruption holds.
  - 63 listed-order keys: 59 can be rewritten, 3 held, 1 no longer flagged.
  - Rewritten rows fall out of NTA until they are re-scored, which is paid work.

---

## 6. Other repos (all local, nothing pushed or deployed)

- **mockmob-backend** (worktree back on `release/app-backend` at 4bf41b8):
  - `feat/ai-reply-report` ff23016: `POST /api/ai/mentor/report`, a table migration and tests. The production SQL to run is `mockmob copy/PRODUCTION-ai-reply-report-2026-10-14.sql`.
  - `play-f4` 3faa82a: the account-deletion page names the app. A stray commit was removed from this branch. The backend's page is an older copy that still mentions push tokens.
  - `sec-tests` 7b2e20a: 18 auth behaviour tests, `test:auth` 68 of 68. Nothing crucial found.
- **mockmob-web2** `fix/web-state-home`:
  - 613235c: logo B wired in (favicon, icon.svg, apple-icon, manifest icons, OG/Twitter image, header SVGs).
  - **Checked in a browser at 375 and 1024 px** against staging: no horizontal overflow, logo B in place. Home page, signed out only.
  - Turbopack fails because web2's `node_modules` is a symlink to `mockmob-hotfix/node_modules`. It was run with webpack through a scratchpad launcher, `web2-staging-webpack.mjs`. A config "web2-staging" was added to `mockmob copy/.claude/launch.json`, alongside the old "mockmob-web-prod-check" config.

---

## 7. Machine state and gotchas

- **RAM:** 16 GB PC; only 0.5 to 4.6 GB free during the night.
  - I closed the ChatGPT desktop app (it partly relaunched) and stale find/flutter_tester processes. Wispr Flow was left running.
  - The emulator ran at 2 GB.
- **Flutter:** use `bash tool/flutter_locked.sh` (2 slots). **Run only one `flutter test` at a time.** Two at once can fail with "failed to delete build/native_assets/windows/sqlite3.dll".
- A hung test from 23:29 (`core_widgets_pkg07_test 50-question`) held a slot until the stabiliser killed it.
- Builds:
  - Demo: `bash tool/flutter_locked.sh build apk --debug -t test/device_demo/demo_main.dart`
  - Real: `bash tool/flutter_locked.sh build apk --release --target-platform android-arm64 --dart-define-from-file=dart_defines/prod.json`
  - Then: `cd android && ./gradlew --stop`
- The emulator cannot reach www.mockmob.in over HTTPS because of certificate interception on this PC.
- Agents never do a hosted sign-in. The owner signs in on the phone himself.
- **Auto mode blocks:** reading production report files ("Production Reads") and weakening security rules.

---

## 8. Owner decisions still pending

1. **Night palette:** keep the warm brown "Night Sheet" look, or move to neutral charcoal (the UI-standards rule)? 18 visual findings were left for this.
2. **Question factory** for the short NTA subjects (paid, within the USD 50 lifetime ledger).
3. **Start's "Repair the next mistake" row:** a 10-minute run (like the shortcut) or the whole chapter? It is currently the whole chapter.
4. **Onboarding sheet ownership:** confirm the chosen rule (section 3.8).
5. **Website redesign:** D1 to D19 in WEB-REDESIGN-PLAN-2026-10-14.md.
6. **NTA clean-up runbook:** approve and run (a production write).
7. **Run PRODUCTION-ai-reply-report-2026-10-14.sql;** earlier backend items: CRON_SECRET, ANDROID_CERT_SHA256.
8. **Owner-only steps:**
   - Upload key (`tool/make_upload_key.ps1`).
   - GOOGLE_WEB_CLIENT_ID.
   - Create the Play app and gather testers.
   - Fill in Data safety.
   - Deploy the web legal pages.
   - Connect the phone, install the rebuilt real APK and sign in.
9. **Earlier round-3 owner items:**
   - The "NTA mode, with Pro" label.
   - Sign-out deleting unsent drafts after a warning (copy is honest).
   - Pre-prompt policy (now: it re-asks).
   - Repair reminders' 7 PM fallback.

---

## 9. Exactly where it stopped, and what to do next

**WIP commit 2209123** was cut off mid-edit by the owner's stop. It is **untested**, the full suite was not run, and it may not even compile. It covers:
- An `ApiClient` expected-user guard: a write started for student A must not be sent with B's token. It touches `lib/core/api/*`, the repositories, `sheet_sync.dart`, `profile_editor.dart` and `study_length.dart`.
- The attempts list fetch time and Today's `_updatedLine` (`attempts_repository.dart`, `remote_state.dart`, `today_builder.dart`).
- `cancelAll()` after `signOutLocal()` in auth_controller sign-out and delete.
- A `StateAction` loading flag used by the load-failed screen.
- An `MmSheetPage` footer used by the reminders prompt sheet.
- The agent's last words were "Now the SheetSync test setup."

**First step for the next agent**
1. In mockmob-next/flutter_app, run `bash tool/flutter_locked.sh analyze`.
2. Run the affected test folders: `test/unit/core_data`, `test/unit/onboarding`, `test/unit/notifications`, `test/unit/core_auth`, `test/unit/today`, `test/unit/you`, `test/golden/notifications`.
3. Finish or fix the five items above.
4. Run the full suite one process at a time and get it green again. The last green run was a817371 at +2990.

**Then**
1. Rebuild the real release APK and the demo APK.
2. Quick emulator check (2 GB AVD).
3. Have the owner connect his phone, install the APK and sign in.

**Other open work**, also in PENDING-2026-10-14.md:
- Align the late-night windows in rhythm and onboarding.
- The remaining parity items: A9, A12 (server), F5 tour, E5 hubs, B5 AI lesson help (needs a server credit gate).
- APK size items 2 to 7 from the audit.
- Update RELEASE.md's permission row.
- Commit `mockmob-fit/docs/brain/NTA-ENGINE-RUN-FIT.md`.
- Merge `wip/cuet-fit` after review and an expert re-read.
- Website redesign after the owner's decisions.

**Continuum checkpoints from this session**, all in `AI OS/handoffs/mockmob/`, newest 20261014T023139Z-2872685b. Subagent handoffs from the same night: 20261014T012053Z (stabiliser), 20261013T232446Z (walk-through), 20261014T023041Z (auth) and 20261014T022012Z (sync).
