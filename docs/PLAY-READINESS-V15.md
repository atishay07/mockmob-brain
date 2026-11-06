# Play readiness for v15 (1.0.15): checklist

Written 18 Oct 2026 by a read-only audit. Docs only; nothing was built, pushed or changed in production.

**What was checked**
- App: `wt-v15` branch `ui/v15-1018`, head `76ee2e90` (v13 plus the four v14 branches; `pubspec.yaml` `1.0.15+3`). The three later v15 branches (Today, result and Review, polish) are NOT in this head, so the screenshots and the exact app that ships can still change.
- Website: origin/main `9578ee66` (release 4, live), read with `git show`.
- Sources: `V15-SPEC-2026-10-18.md` section 7, `PLAY-RELEASE.md` (13 Oct), `PLAY-RELEASE-2026-10-16.md` (it exists only in the `wt-v15` tree, not in this checkout), `PLAY-LISTING-2026-10-14.md`, `NOW.md`, `OWNER-MASTER-LEDGER.md`.
- Not re-run: a build, `aapt2`, `check_16kb.py`. No AAB exists (no signing key). Every "re-run on the AAB" below is therefore still open.

Legend: **[done]** verified in code or docs today. **[code]** needs a change (file and change given). **[owner]** needs the owner's account, key or decision.

---

## 0. The short version

Five things stand between v15 and a Play upload.

1. **[owner]** Upload key and Play Console. No key exists, so any release build today is debug-signed and Play would reject it.
2. **[code] The AI reply report is switched off in the app.** `aiReplyReportLive = false`, so Ask shows no "Report this reply" key. The server route and table are live on production, so the app can flip it now. Play's generative-AI policy needs this working before the closed test goes to review.
3. **[code] The privacy policy still says the app stores a push token** (it does not; there is no push or Firebase), and the paragraphs that describe the stream events and the report button are hidden behind `APP_STREAM_AND_REPORT_LIVE = false`. Play compares the policy, the Data safety form and the app.
4. **[code] New since the 16 Oct pack: the app sends first-party error reports** (`/api/app/errors`, only for adults who allowed usage data). The Data safety form, the policy and the in-app privacy text do not mention them, and the in-app text says the opposite ("This switch controls neither").
5. **[owner] Decision:** question-stream events (`seen`, `attempted`, `skip`) are sent for every signed-in user, minors included, not behind the usage-data switch. Declare them (recommended, already in the form below) or gate them.

---

## 1. App technical (wt-v15 head 76ee2e90)

| Item | Result |
|---|---|
| **[done]** applicationId / namespace | `in.mockmob.app` (`android/app/build.gradle.kts`). The demo build uses the suffix `.demo`; the release does not. |
| **[done]** targetSdk | 36, pinned: `maxOf(flutter.targetSdkVersion, 36)`. Play needs API 36 for new apps and updates from 31 Aug 2026 (an extension to 1 Nov 2026 was available). `build_release_aab.sh` refuses to build if the pin is changed. |
| **[done]** minSdk | 24, pinned. |
| **[done]** versionCode / versionName | From `pubspec.yaml` `1.0.15+3`: versionName 1.0.15, versionCode 3. Play only needs each upload to be higher than the last; this is the first upload, so 3 is fine. Upload the AAB, not `--split-per-abi` APKs (Flutter adds an offset to those codes). Every later upload: `bash tool/build_release_aab.sh --bump`. |
| **[done]** Cleartext, backup | Cleartext only in the debug manifest; `allowBackup="false"`. |
| **[done]** Permissions declared (main manifest) | INTERNET, ACCESS_NETWORK_STATE, POST_NOTIFICATIONS, RECEIVE_BOOT_COMPLETED, WAKE_LOCK. USE_BIOMETRIC and USE_FINGERPRINT are removed with `tools:node="remove"`. Exact-alarm permissions are absent on purpose. |
| **[done]** Permissions added by plugins | VIBRATE (flutter_local_notifications), FOREGROUND_SERVICE and FOREGROUND_SERVICE_SHORT_SERVICE (workmanager). I read the plugin manifests of the five plugins added since 16 Oct (home_widget 0.10.0, quick_actions_android, share_plus 13.3.1, in_app_review 2.0.12, in_app_update 5.0.0): none adds a permission (share_plus adds a FileProvider and an unexported receiver). Expected merged total stays 8 plus the app's own signature permission. |
| **[owner]** Re-verify on the real AAB | `aapt2 dump badging` (package, label, targetSdk 36, permission list) and `python -I tool/check_16kb.py <aab>`. The 16 KB check last passed on 13 and 16 Oct, before home_widget, quick_actions, share_plus, in_app_review and in_app_update were added. Hard deadline for 16 KB is 1 Feb 2027. `build_release_aab.sh` runs the 16 KB check itself. |
| **[done]** R8, symbols | On for release; keep rules in `android/app/proguard-rules.pro`; `SYMBOL_TABLE` native symbols; the script archives the R8 mapping and Dart symbols under `build/release-archive/<versionCode>/`. **[owner]** Keep that folder for every upload. |
| **[done]** Foreground-service declaration | If the Console asks: type is short service, used for sending queued answers (WorkManager). `FOREGROUND_SERVICE_DATA_SYNC` is not declared. If the Console demands a video, ask whether the permission can be dropped instead. |
| **[done]** Deep links | App Links for `https://www.mockmob.in` only, `autoVerify`; the sign-in callback `in.mockmob.app://login-callback`. Pricing and checkout paths are not listed. `/join` and `/mob` are listed for the Mob; harmless while the server switch is off. |
| **[done]** Mob is hidden when the server has it off | `mobDisabledError` treats any 404 on `/api/mob` as off and the You row then shows nothing. The Mob migration is NOT on production (NOW.md; the staging gate was NO-GO). So v15 ships with no Mob in practice. **If the Mob is switched on later**, redo: content rating ("users can interact": yes), Data safety (what other members see), the policy, and Play's user-generated-content rules (in-app report and block). |
| **[done]** Other new things | The home-screen widget and app shortcuts (quick_actions) work on the phone only and send nothing. `in_app_update` and `in_app_review` use Google Play's own services; nothing goes to MockMob. Share cards use the system share sheet, started by the student. |

## 2. Signing

| Item | Result |
|---|---|
| **[done]** Signing config | `build.gradle.kts` reads `android/key.properties` (git-ignored, confirmed with `git check-ignore`). With the file the release build uses the upload key. Without it the build silently falls back to the debug key. |
| **[done]** Guard | `tool/build_release_aab.sh` stops if `key.properties`, the keystore or `prod.json` is missing or still a template, if the signer prints `CN=Android Debug`, or if the SDK pins changed. |
| **[done]** Local files | `dart_defines/prod.json` exists locally and is git-ignored. It holds the production API URL (`https://www.mockmob.in`), the production Supabase URL and the public anon key. `GOOGLE_WEB_CLIENT_ID` is empty, so "Continue with Google" runs through the browser (PKCE), not the one-tap sheet. That works without an Android OAuth client. |
| **[owner]** Create the upload key | `powershell -ExecutionPolicy Bypass -File tool\make_upload_key.ps1` from `flutter_app`. Back up the `.jks` and the password in two places. Never send them to an agent or paste them in chat. **Still pending.** |
| **[owner]** Play App Signing | Accept the default. After the first upload copy the app-signing SHA-256 and SHA-1 (Test and release, App integrity). The SHA-256 goes into the Vercel variable `ANDROID_CERT_SHA256` (then redeploy; served at `/.well-known/assetlinks.json`). The SHA-1 goes into a Google Cloud Android OAuth client only if you add the web client id for one-tap sign-in. Until then links open in the browser and nothing breaks. |
| **[owner]** Optional: Google web client id | Fill `GOOGLE_WEB_CLIENT_ID` in `prod.json` for the one-tap sheet. Not needed for the closed test. If you do, the Google consent screen must be set to In production, or only listed test users can sign in. |
| **[code]** Docs drift | `flutter_app/docs/RELEASE.md` still shows `1.0.0+1` in its table and says the 14 days "do not count" per app. `PLAY-RELEASE.md` leaves that open. Make them agree after the owner checks the Dashboard (section 7). Low priority. |

## 3. AI reply report (Play generative-AI policy)

| Item | Result |
|---|---|
| **[done]** Server | `POST /api/ai/mentor/report` is on origin/main `9578ee66`: signed in, rate limited, reason from a fixed list, reply checked against the student's own conversation, write-only. The table migration `20261016140000_ai_reply_report` was applied to production on 17 Oct (HANDOFF-2026-10-17-NIGHT). Account deletion removes the reports. |
| **[done]** App UI exists | "Report this reply" key (`ask_messages.dart`), four reasons, offline outbox, and "Reported. It goes to a check." (`insights/copy.dart`). Ask also shows a one-time notice before the first AI send. |
| **[code]** Switch the key on | `flutter_app/lib/features/insights/data/ai_reply_report.dart` line 16: `const bool aiReplyReportLive = false;` to `true`. Until this is flipped, every v15 AI reply has no way to be reported, which is exactly what the policy asks for. Update any test that asserts the hidden state. |
| **[code]** Verify end to end before upload | One report from a signed-in test account against the staging rig (3101); then, on the closed-test build against production, one report from the owner's own account (agents must not write production data). Expect one row in `ai_reply_reports`, the key shows "Reported", and a second tap on the same reply does not create a second row. |
| **[code]** Web gate | `src/lib/appReleaseGates.mjs` in mockmob-next: `APP_STREAM_AND_REPORT_LIVE = false` to `true`, in the same website deploy as the AAB going to the closed track. It reveals the policy paragraphs "Question stream activity" and "Reporting an AI reply". Check `/privacy` shows both after the deploy. |
| **[owner]** Also on the form | Answer "Generative AI features: yes" in the content rating, and say replies can be reported in the app. Confirm the AI provider's terms bar training on API data; the "service provider, not shared" answer in Data safety depends on it. |

## 4. Privacy policy (`https://www.mockmob.in/privacy`)

The URL is live and loads. It must match the app and the form. Change `src/app/privacy/page.js` (mockmob-next, one website deploy):

| # | Change |
|---|---|
| **[code]** P1 | Section "Android app": remove "stores your push notification token so we can send reminders". The app has no push and no Firebase; reminders are scheduled on the phone. Say that, and that notification preferences and the study goal are stored with the account. |
| **[code]** P2 | Add the app's error reports: "If you are 18 or older and allow usage data, the Android app also sends error reports (what failed, which screen, app version, Android version, a coarse device class; no name, no email, no device id). Turning usage data off stops them." Check the wording against `error_scrubber.dart` and the `/api/app/errors` route before publishing. |
| **[code]** P3 | "Optional usage data" says "We never collect answers, marks, free text or contacts." Scope it to usage data ("Usage data never includes ...") so it does not contradict the stream-events paragraph, which says the stream sends the option picked and whether it was right. |
| **[code]** P4 | Name the Android screens as the app does: usage data is under You, then Usage data (the policy says "Profile"). Account deletion in the app is You, Account, Delete account. |
| **[code]** P5 | Several paragraphs describe the website ("uploaded questions", "moderate community questions"). Say which parts apply to the website only, so the policy does not suggest the app has user uploads. |
| **[code]** P6 | Update "Last updated" to the deploy date. |
| **[done]** | The account deletion page (`/account-deletion`) names "MockMob: CUET UG Prep" and `in.mockmob.app`, lists the two ways to ask, what is deleted and kept, and the 30-day period. |
| **[owner]** | Read the page once as the Play reviewer would. Legal review (DPDP, under-18 users) is still the owner's, as in `PLAY-RELEASE.md` section 4. |

## 5. Data safety answers (what the v15 app actually sends)

Method: "collected" = leaves the phone; "shared" = given to a third party other than a service provider acting for MockMob. All rows: collected yes, shared no, ephemeral no. Encrypted in transit: yes (HTTPS only). Deletion: yes, in the app and at `https://www.mockmob.in/account-deletion`. Account creation: email (code or password) and Google. Independent security review: no.

| Data type | Required or optional | Purposes | Status |
|---|---|---|---|
| Email address | Required | App functionality, account management, security | **[done]** same as the 16 Oct pack |
| Name | Optional | App functionality, account management | **[done]** Google sign-in, or typed in You |
| User IDs | Required | App functionality, account management | **[done]** |
| Other personal info (age band) | Optional | App functionality, security | **[done]** |
| App interactions | Required | App functionality, personalization, analytics (consented events only) | **[done]** answers, timing, results, stream seen/attempted/skip, lesson events, goal progress, how a paper ended |
| Other user-generated content | Optional | App functionality | **[done]** saves, votes, question and AI-reply reports (reason label, reply text) |
| Other actions | Optional | App functionality, personalization | **[done]** weekly goal, pause, reminder preferences, quiet hours, timezone |
| Other in-app messages | Optional | App functionality, personalization | **[done]** Ask Mobi text, processed for MockMob by the model provider |
| **Crash logs** | **Optional** | **App functionality, analytics** | **[owner] NEW since the 16 Oct pack.** The app's own error reports (`/api/app/errors`), adults who allowed usage data only. Tick it in the form. |
| **Diagnostics** | **Optional** | **App functionality, analytics** | **[owner] NEW.** Each report carries app version, build, Android version and a coarse device class. Tick it with crash logs. |

Not collected, leave unticked: location, financial info, health, photos and videos, audio, files, calendar, contacts, web browsing, installed apps, search history, device or other IDs (no advertising id, no push token), phone number (`PHONE_SIGN_IN` is off). Third parties: Supabase, Google (sign-in only), Resend (sign-in email), the AI model provider, Vercel, all acting for MockMob. Razorpay is website-only and not in the app. Play's own crash and vitals reporting is Google's, not the app's.

| Item | Status |
|---|---|
| **[owner]** Question-stream events (section 0, item 5) | Recommended: keep them as required "App interactions", declared above and in the policy once the gate is flipped. The alternative is to gate stream logging on the usage-data switch; that is a code change in `lib/features/insights/data/feed_api.dart` and the stream controller, and it would stop learning-progress updates for people who leave the switch off. |
| **[code]** In-app text must agree | `lib/features/you/copy.dart` `consentExplanation` (line 226) does not mention error reports. `operationalNote` (line 238) says Play reports crashes "and this switch controls neither", which is now false (the switch controls the app's error reports), and it does not name question views. Rewrite both so the in-app text, the form and the policy say the same thing. |
| **[owner]** After saving the form | Preview the Data safety card and read it against `/privacy`. |

## 6. Content rating, target audience, other declarations

| Item | Answer or state |
|---|---|
| **[done]** Content rating (IARC) | Category Reference, News or Educational. Violence, sexual content, profanity, drugs, gambling: none. Users communicate or share: **no while the Mob is off**. Location sharing: no. Digital purchases: no. Unrestricted internet: no (links open MockMob pages only; pricing and off-domain links are refused in `action_router.dart`). Collects personal info: yes. Generative AI: yes. Ads: no. Do not change answers to chase a rating. **[owner]** Enter them in the Console. |
| **[done]** Target audience | Tick 16-17 and 18 and over only. Not designed for children, not Designed for Families. No ads. The server refuses usage data for anyone who is not an adult. |
| **[owner]** Legal check | Whether 16 to 17 year olds count as children under India's DPDP Act (consent and monitoring rules from about May 2027) needs a lawyer before production. Not cleared by this document. |
| **[done]** Ads, advertising ID | None; no ad SDK, no AD_ID permission. Declare "does not use". |
| **[done]** Payments policy | The app no longer names a place to buy. The old "Plans are managed on mockmob.in" line is gone (`edit_copy.dart` now has only "Pro is active" and the unlimited-practice line; the plan card comment says "No price, no purchase"). No Play Billing, no checkout in the app. Do not tick "contains in-app purchases". One low risk left: the Ask wallet row "Purchased, never expire" (`insights/copy.dart` `walletPurchased`, used in `ask_wallet.dart` line 135). Consider "Extra credits, never expire" so no screen implies a purchase path. **[code]**, optional. |
| **[done]** Other declarations | Government apps: no. Financial features: none. News: no. Health: none. Foreground service: see section 1. |
| **[owner]** Trader status (EU) | Check Play's account page. Simplest: India only for the closed test. |
| **[owner]** App access for reviewers | Create a dedicated reviewer account on production by email code, set a password in You, Account, answer the age question Yes, leave usage data off, keep the account alive during review. Paste the steps from `PLAY-RELEASE.md` section 5. Labels verified in v15 code: "I already have an account", "Password", "Sign in with a password". **[code]** Re-check the bottom-bar tab names and "Quick practice" against the final v15 build before pasting (Today, Practice and Review exist as routes; the bar is still being reworked). |

## 7. Closed test

| Item | State |
|---|---|
| **[owner]** Developer account | Registered and verified? The type (personal or organisation) decides the rule. |
| **[owner]** The 12 testers, 14 days rule | Applies to personal accounts created after 13 Nov 2023. The owner said the 14 days were done on another app; Google's text does not say whether that carries over, and `RELEASE.md` says it does not. Open the new app's Dashboard: if "Apply for production" is available the gate is clear; if not, run 14 days with 20 to 25 testers (a Google Group), India only. Sample tester message and the production answers are in `PLAY-RELEASE.md` sections 7.3 to 7.7. |
| **[owner]** Release notes | The 16 Oct closed-test notes still fit; add "Report a wrong AI reply" once the key is switched on. |

## 8. Store listing

### 8.1 Text

| Field | Value | State |
|---|---|---|
| App name (30) | `MockMob: CUET UG Prep` (21). Fallback `MockMob: CUET UG Mocks` (22). Must contain "MockMob" so the deletion page matches. | **[done]** |
| Short description (80) | `Fresh CUET UG mocks each time. See where the marks went, then repair them.` (74 characters) | **[owner]** approve |
| Category, price, contact | Education, free, English (India), no ads, `support@mockmob.in`, `https://www.mockmob.in`, privacy `https://www.mockmob.in/privacy` | **[done]** |

**The USP, said truthfully.** The owner's line is "unlimited mocks from one central bank". In the app that is literally true only on Pro. Free spends Practice credits on each mock, and the app's own wording is "No fixed set of mocks" for Free and "Unlimited mocks" for Pro (`practice/copy.dart` `bankLine`). What is true on every plan: each paper is built fresh from the live question bank. The draft below says exactly that. It avoids "unlimited", competitor numbers ("10 to 30 mocks") and "never repeats" (the selector prefers unseen questions but does not guarantee them). **[owner] decision:** if you want the word "unlimited" in the listing it needs "on Pro", and a Pro mention in the listing raises the Play payments question again. Recommendation: keep Pro out of the listing.

### 8.2 Full description (2,724 of 4,000 characters)

Differences from the 16 Oct text: adds the fresh-paper section; removes NTA mode (Pro-gated), Concepts (the app may show it as paused), Admission Compass, Combo planner and the CUET 2027 guide (each needs a fresh check against the shipped v15 and the data behind it before it is named); says "Ask Mobi"; says AI replies can be reported in the app; names app error reports as optional. Add a removed bullet back only after the verify list below passes.

```
MockMob is a practice app for CUET UG 2027 students. A mock should show you where you lost marks and what to do about it, so the app works in three steps: practise, see where the marks went, repair the mistakes.

NOT A FIXED SET OF MOCKS
Every paper is built fresh from MockMob's live question bank, for the subject and chapters you choose. You are not working through a short list of ready-made mocks.

PRACTISE
- Quick practice of 5 to 20 questions, or pick up to 12 chapters and practise only those.
- A full mock, timed like the exam, with a question palette, mark for review and a clear submit step.
- Marking follows the CUET pattern: 5 marks for a right answer, minus 1 for a wrong one, 0 for a blank.
- If your connection drops during a mock, your answers stay on your phone and are sent when you are back online.

SEE WHERE THE MARKS WENT
- Each result breaks your marks down by chapter.
- Your record shows marks session by session and ranks chapters by the marks you left open.
- Ask Mobi a question about your record, such as which chapters cost you the most marks. Answers about your results come from your results. Other questions can get a reply written by AI, which can be wrong, so check it against the answer key and your textbook. You can report any AI reply from inside the app.

REPAIR
- Review groups your mistakes by chapter. Repair them one at a time and read the key explanation. Skipped questions are listed separately and are not counted as mistakes.
- Today suggests one next step from your own record and says why. Start it, or choose something else.

WEEKLY RHYTHM
- Set a goal of 1 to 7 study days a week. Pause it when life gets in the way; paused weeks do not break your run.
- Reminders are optional and are set on your phone. Choose which ones you want and your study time, and switch them off at any time.

SUBJECTS
MockMob starts with the CUET UG Commerce papers: English, Accountancy, Business Studies and Economics.

YOUR ACCOUNT AND YOUR DATA
- Sign in with a code sent to your email, with Google, or with a password you set yourself.
- There are no ads in the app.
- Usage data and app error reports are optional. They are off by default and can be turned on only by someone who says they are 18 or older. You can turn them off at any time.
- Delete your account from the app (You, Account, Delete account) or at www.mockmob.in/account-deletion.

NOT AFFILIATED
MockMob is an independent practice app. It is not affiliated with, endorsed by or sponsored by the National Testing Agency (NTA), the University of Delhi or any government body. CUET is an examination conducted by NTA. For official notices, dates and rules, use cuet.nta.nic.in.

Questions or feedback: support@mockmob.in
```

### 8.3 Verify each claim on the final v15 build before pasting

| Claim | Where it comes from | Confirm |
|---|---|---|
| Fresh paper from the live bank, no fixed set | `practice/copy.dart` `bankLine` ("true on every plan") | The Practice exam band shows the line on a Free account |
| Quick practice 5 to 20, up to 12 chapters | `practice/copy.dart` `quickLine`, `chapterLine` | Practice screen on the emulator |
| Full mock, palette, mark for review, submit | runner | Runner screenshots |
| +5, -1, 0 for blank | `lib/core/domain/marks.dart` | The result shows it the same way |
| Answers kept offline, sent later | outbox | Airplane-mode test on the emulator |
| Chapter breakdown, marks ranked by chapter | result and Insights | Result and record screens (the v15 result and Review branch is still open) |
| Skipped listed separately, not mistakes | Review | Review screen |
| Today next step with a reason | Today | Today screen (the Today design is still moving) |
| Ask Mobi answers from the record, AI replies, report key | `ask_controller.dart`, `ai_reply_report.dart` | **The report key shows only after `aiReplyReportLive` is true** |
| Goal 1 to 7 days, pause | Rhythm | You, Rhythm |
| Reminders local, optional, off any time | `notification_prefs`, quiet hours | You, Notifications |
| Four Commerce papers | `/api/subjects` | **The website now has a five-subject cap and the API listed 15 subjects in the 16 Oct pack. Check what the v15 app offers and name exactly that.** |
| Sign in by code, Google, password | `docs/AUTH.md` | Sign-in screen |
| Optional usage data and error reports, adults only | `consent`, `ErrorGate` | You, Usage data (after the in-app text fix) |
| Delete in the app | `delete_screen.dart` | You, Account, Delete account |

## 9. Graphics and screenshots

| Item | State |
|---|---|
| **[done]** App icon 512 x 512, 32-bit PNG with alpha | `mockmob-next/tmp/logo/final-B/play/icon-512.png` (untracked file, size and alpha checked). **[owner]** The logo is still "B, may switch to A"; confirm the icon matches the in-app adaptive icon before upload. |
| **[done]** Feature graphic 1024 x 500, no alpha | `feature-graphic-v3-1024x500.png` (24-bit, checked) and `.jpg`, same folder. v2 and v3 both exist; **[owner]** pick one. Keep Mobi small, never the hero (child-appeal risk for a 16+ audience). |
| **[owner]** Phone screenshots, 2 to 8 (use 8), portrait 1080 x 1920 | Real emulator captures with the reviewer account, Night theme, 12-hour clock, no edited numbers. Marketing waits until January per the owner (V15-SPEC section 7), but Play needs at least 2 for the listing, so capture these once v15 is final (after Today, result and Review land). Goldens (360 dp renders) are layout references only, never store images. |
| **[owner]** Tablet screenshots | Optional for a phone app; skip for the closed test. |

Screenshot list, in order (caption under 30 characters, sentence case, no rank or improvement claims):

1. Today with one next step and its reason. "One next step, and why". The old reference golden `today/goldens/today_ready_night.png` no longer exists; use the current `today` goldens.
2. Practice: Quick, By chapter, Full mock. "Pick how you practise". Reference `practice/goldens/exam_band_430_night.png`, `chapter_picker_night.png`.
3. The timed runner with the palette and a marked question. "Timed like the exam". Reference `runner/goldens/mock_answered_night.png` (`nta_answered_night.png` only if the account has NTA mode, which is Pro-gated).
4. Result: net marks and marks by chapter. "See where the marks went". Reference `result/goldens/full_answers_night.png`, `card2_night.png`. Wait for the v15 result branch.
5. Review: mistakes grouped by chapter. "Mistakes, grouped by chapter". Reference `review/goldens/review_mistakes_night.png`. Wait for the v15 Review branch.
6. Repair one mistake with the key explanation. "Repair one mistake at a time". Reference `review/goldens/repair_explained_night.png`.
7. Weekly goal and rhythm. "A weekly goal you choose". Reference `rhythm/goldens/rhythm_screen_top_night.png`.
8. Reminders and the usage-data choice (shows the privacy position in the app's own words). "You choose what is sent". Capture after the in-app text fix (section 5). It replaces the Admission Compass shot from the 16 Oct plan, because Compass is not named in the listing above. Alternate: Ask Mobi with the "Report this reply" key visible, once it is switched on, because it shows the AI policy in action.

Every reference golden above except the Today one was found in `wt-v15/flutter_app/test/golden`.

## 10. Order of work

1. **[code]** Flip `aiReplyReportLive`, rewrite the two in-app privacy texts, optionally the wallet label. One small app branch off `ui/v15-1018`; run tests and goldens for You and Ask.
2. **[code]** One website deploy: policy edits P1 to P6 and the `APP_STREAM_AND_REPORT_LIVE` flip, timed with the closed-test upload.
3. **[owner]** Run the upload key script; `prod.json` is already in place; build with `bash tool/build_release_aab.sh --bump`; confirm the printed signer is not "Android Debug"; re-run `aapt2` and the 16 KB check on the AAB.
4. **[owner]** Create the reviewer account; fill the Console sections (sections 4 to 8); upload to Closed testing, India only; add 20 to 25 testers.
5. **[owner]** After the first upload: copy the app-signing fingerprints to `ANDROID_CERT_SHA256` on Vercel, redeploy, and check `adb shell pm get-app-links in.mockmob.app`.
6. **[owner]** Capture the screenshots on the emulator once v15 is final; finish the listing.
7. Days 1 to 14: watch vitals and the AI reports table; ship fixes as new uploads on the same track; apply for production when the Dashboard allows it.
