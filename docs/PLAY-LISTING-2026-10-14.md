# MockMob on Google Play: listing, Data safety, rating and screenshots

Written 14 Oct 2026 for package `in.mockmob.app`, closed test. This re-derives the text from the code as it stands today (`flutter_app/lib`, `src/app`) and supersedes the listing and Data safety parts of `PLAY-RELEASE.md` (13 Oct) where they differ. The rest of that pack (testers, reviewer access, technical rules, owner checklist) still stands. Items not confirmed from code are marked **[CONFIRM]**. This is not legal advice.

Copy rules used: plain sentence case, no hype, no superlatives, no exclamation marks, no emoji, no em dashes, 12-hour time, nothing the build cannot do today.

---

## 0. What changed since PLAY-RELEASE.md, and what is still open

Checked on 14 Oct against the working tree.

| # | Item | State on 14 Oct | What to do |
|---|---|---|---|
| 1 | "Plans are managed on mockmob.in" line (old F1) | Gone. `edit_copy.dart` now says only "Pro is active." or "Pro is active until {date}." | Nothing. The Pro-gated rows in Practice still say "Comes with Pro" with no place to buy, which is fine |
| 2 | Report control on AI replies (old F2) | The control exists in the app (`ask_messages.dart`, "Report this reply"), but the server route `/api/ai/mentor/report` does **not** exist (`src/app/api/ai/mentor` has only chat, history, local, session). The app keeps the report in its outbox, gets a 404 and tells the student it did not reach us (`ai_reply_report.dart`) | **Blocker for any build where the AI mentor can reply.** Add the endpoint, or keep the mentor off for the Play build. Play's generative AI policy needs a working in-app report |
| 3 | Privacy page push-token sentence (old F3) | Fixed. It now says reminders are local notifications and no push token is stored. It mentions optional AI and practice events | Add "seen, attempted and skipped per question in the question stream" to the practice events paragraph (see item 5) |
| 4 | Deletion page names the app exactly as on Play (old F4) | Not done. `src/app/account-deletion/page.js` says only "MockMob" | Add "MockMob: CUET UG Prep (`in.mockmob.app`)" to the page before submission |
| 5 | Question stream events not behind the usage-data switch (old F5) | Unchanged. `stream_controller.dart:178` logs `seen` and `:194` logs `skip`, and answers log `attempted`, for every signed-in user, and `operationalNote` in `you/copy.dart` does not name them | Declared below as required "App interactions". Owner decision still open: name them in the policy and the app, or gate them on consent |
| 6 | `flutter_app/docs/RELEASE.md` disagrees with this pack | It says target audience "18 and over only", Data safety includes "crash and diagnostics if enabled", and lists five permissions | Follow this file. The app has no crash SDK (Play vitals only), the age question allows "No" and "Prefer not to say", so 16 to 17 year olds can use the app, and the merged release manifest has 9 permissions (list in 2.1). Edit RELEASE.md section 5 to match |
| 7 | New since 13 Oct: CUET tools, Concepts, question stream, saved questions, home-screen widget | Included in the text below | Verify on the submitted build (section 1.5) |
| 8 | Listing names NTA mode and it is gated | NTA mode and Smart practice are Pro-gated in the app ("Comes with Pro", `practice/copy.dart`) | The listing names NTA mode as the owner asked, without saying who can open it. If you would rather not list a gated feature, delete the one NTA bullet |

---

## 1. Store listing

### 1.1 Fields

| Field | Limit | Value |
|---|---|---|
| App name | 30 | `MockMob: CUET UG Prep` (21) |
| Fallback name if refused | 30 | `MockMob: CUET UG Mocks` (22) |
| Short description | 80 | see 1.2 |
| Full description | 4000 | see 1.3 |
| Default language | | English (India), `en-IN` |
| App or game | | App |
| Free or paid | | Free |
| Category | | Education |
| Tags | up to 5 | Education, Exam preparation, Test prep, Study, Quiz (choose what the Console offers; if it offers fewer, keep the first two) |
| Contact email | public | `support@mockmob.in` |
| Website | | `https://www.mockmob.in` |
| Privacy policy | | `https://www.mockmob.in/privacy` |

### 1.2 Short description

```
CUET UG practice with timed mocks, mistake repair and a weekly rhythm.
```

(70 characters. Plain, names the exam and the three things the app does.)

### 1.3 Full description

```
MockMob is a practice app for CUET UG 2027 students. A mock should show you where you lost marks and what to do about it, so the app works in three steps: practise, see where the marks went, repair the mistakes.

Practise
- Quick practice of 5 to 20 questions, or pick up to 12 chapters and practise only those.
- A full mock, timed like the exam, with a question palette, mark for review and a clear submit step.
- NTA mode: an exam-day screen with 50 questions in 60 minutes, modelled on the computer-based test, so the layout is familiar on the day.
- Marking follows the CUET pattern: 5 marks for a right answer, minus 1 for a wrong one, 0 for a blank.
- A question stream for untimed practice: answer, then see why.
- If your connection drops during a mock, your answers stay on your phone and are sent when you are back online.

See where the marks went
- Each result breaks your marks down by chapter.
- Your record shows marks session by session and ranks chapters by the marks you left open.
- Ask your record a question, such as which chapters cost you the most marks. Answers about your results come from your results. An optional AI mentor can also reply, and its replies can be wrong, so check them against the answer key and your textbook.

Repair
- Review groups your mistakes by chapter. Repair them one at a time and read the key explanation. Skipped questions are listed separately and are not counted as mistakes.
- Today suggests one next step from your own record and says why. Start it, or choose something else.
- Concepts has short lessons and recall cards from the chapters you practise.

Weekly rhythm
- Set a goal of 1 to 7 study days a week. A study day is a day you finish a practice, a mock or a repair. Pause the goal when life gets in the way; paused weeks do not break your run.
- Reminders are optional and are set on your phone. Choose which ones you want and your study time, and switch them off at any time.
- Mobi, the MockMob mascot, adds a short line on Today and after a session.

CUET tools
- Admission Compass shows which Delhi University programmes your subjects open under the UG Bulletin 2026-27, with college cutoffs by category and round from the 2026 CSAS lists.
- Combo planner works out which papers open the courses you want.
- The CUET 2027 guide has expected dates and a month-by-month plan.

Subjects
MockMob starts with the CUET UG Commerce papers: English, Accountancy, Business Studies and Economics.

Your account and your data
- Sign in with a code sent to your email, with Google, or with a password you set yourself.
- There are no ads in the app.
- Usage data is optional. It is off by default and can be turned on only by someone who says they are 18 or older. You can turn it off at any time.
- Delete your account from the app (You, Account, Delete account) or at www.mockmob.in/account-deletion.

Not affiliated
MockMob is an independent practice app. It is not affiliated with, endorsed by or sponsored by the National Testing Agency (NTA), the University of Delhi or any government body. CUET is an examination conducted by NTA. For official notices, dates and rules, use cuet.nta.nic.in.

Questions or feedback: support@mockmob.in
```

Length is checked in section 1.6. What was left out on purpose: price, any mention of Pro or where plans are sold, rank or improvement claims, the other subjects (the app lists 15 but only the four above are launch subjects), fresh-question checks (gated off), "official", and any student count.

### 1.4 Release notes for the closed test (limit 500 characters)

```
First closed test build. Please try: sign in, take a Quick practice, open the result and the chapter breakdown, repair one mistake in Review, set a weekly goal under You, and choose your reminders in Notifications. Sit a full mock with Wi-Fi off, then switch it back on and check that your answers are sent. Tell us what looks wrong at support@mockmob.in with a screenshot. This build has no ads and no purchases.
```

### 1.5 Check every claim on the submitted build

| Claim | Where it comes from | What to confirm |
|---|---|---|
| Quick practice 5 to 20 questions; by chapter up to 12 | `practice/copy.dart` (`quickLine`, `chapterLine`) | Practice setup screens |
| Full mock timed, palette, mark for review, submit step | `runner/copy.dart` (`paletteTitle`, `mark`, `reviewAndSubmit`, `submitTitle`) | Runner and submit screens |
| NTA mode 50 questions, 60 minutes | `runner/nta/nta_copy.dart` (`NtaRules`) | Open it on an account that has it |
| +5, -1, 0 | `insights/copy.dart` (`ledgerNote`), `NtaRules` | Result screen |
| Question stream, untimed | `insights/copy.dart` (`streamEntryNote`) | Review tab, Question stream |
| Answers kept on the phone offline | `runner/copy.dart` (`awayOnPhone`, `pendingBody`) | Airplane-mode test on the emulator |
| Result by chapter; record by session; chapters ranked | `insights/copy.dart` (`trendHeading`, `chaptersHeading`) | Record page after two sessions |
| Ask your record; optional AI mentor | `insights/data/ask_controller.dart` | Ask screen; **AI report endpoint missing (section 0, item 2)** |
| Mistakes by chapter, skipped listed separately | `review/copy.dart` (`emptyMessage`, `notAttemptedNote`) | Review tab |
| Today: one next step with a reason | `today/copy.dart`, `today/screens/why_sheet.dart` | Today |
| Concepts: lessons and recall cards | `learn/copy.dart` | **[CONFIRM]** the server has Concepts on; the app shows "Concepts are paused right now" when it does not. If paused, delete that bullet |
| Goal 1 to 7 days; study day definition; pause | `you/copy.dart` (`goalCounts`, `goalRejected`, `pausedKeepsRun` in `rhythm/copy.dart`) | You, Weekly goal and rhythm |
| Reminders optional, local, study time | `notifications/*`, `AndroidManifest.xml` (no push) | You, Notifications |
| Mobi lines on Today | `today/copy.dart` (`mobiIdle` and others) | Today |
| Compass, Combo planner, CUET 2027 guide | `tools/copy.dart` | You, CUET tools |
| Sign in by code, Google, password | `core/auth/*`, `docs/AUTH.md` | Sign-in screen; Google needs the Play App Signing SHA-1 added to the Android OAuth client |
| No ads | `pubspec.yaml` has no ad SDK, no AD_ID permission | Re-run `aapt2 dump badging` on the upload |
| Delete path | `you/copy.dart` (`rowAccount`, `deleteRow`), `account/delete_screen.dart` | You, Account, Delete account |

### 1.6 Lengths

Counted by script on 14 Oct 2026, from the blocks above: app name 21, short description 70, full description 3,200, release notes 413. Recount after any edit (the check is in the last section).

### 1.7 Graphics

| Asset | File | Notes |
|---|---|---|
| App icon 512 x 512 | `tmp/logo/final-B/play/icon-512.png` | Existing, final-B `mo` icon. Confirm it has alpha and is under 1024 KB at upload |
| Feature graphic 1024 x 500 | `tmp/logo/final-B/play/feature-graphic-v2-1024x500.png` | New. 24-bit RGB PNG, no alpha. Warm charcoal ground `#12110E`, the final-B wordmark with Mobi as the second o (volt only inside the mark), one line "Find where you lose marks, then repair them." in warm grey `#BDB6A6`, and a quiet answer-sheet grid on the right in the app's line colours with a faint lamp-amber glow in the corner. Text sits inside a 72 px side and 56 px vertical margin. Built by `tmp/play/make_feature_graphic.py` |
| Phone screenshots | 8, see section 5 | |

The old `feature-graphic-1024x500.png` (wordmark only, centred) stays on disk and is not used. Mobi is small and part of the wordmark, never the hero, so the graphic does not read as child-directed (PLAY-RELEASE section 1.3 warning).

---

## 2. Data safety form

Rules used, from Play's guidance: "collected" means sent off the device; data kept only on the device is not collected. "Shared" means a transfer to a third party, except to service providers that process data only for MockMob. Mark "Optional" only when a user can decline and still use the app.

### 2.1 What the build sends, from the code

| Area | Leaves the phone | Source |
|---|---|---|
| Sign-in | Email address for code and password sign-in. For Google sign-in, the Google ID token; the server then holds name, email and a profile picture link | `core/auth/*` |
| Account | Reads only: user id, subjects, role, credit balance, Pro status | `core/models/auth_me.dart` |
| Age and usage-data choice | `ageBand` (adult, minor, unknown) and the usage-data switch | `PUT /api/me/consent` |
| Profile edits | Display name (1 to 80 characters), up to 5 subjects | `PATCH /api/users/{id}` in `you/data/profile_editor.dart`, `onboarding/state/sheet_sync.dart` |
| First-run sheet | Study days a week and study time are sent. Course, colleges, category, confidence, worry and minutes stay on the phone (`sheet_sync.dart` header) | `PUT /api/me/goal`, `PUT /api/me/notification-prefs` |
| Practice and mocks | Subject, chapters, answers, answer changes, visits and time per question, submit time, marks, per-question results | `/api/sessions`, `/api/attempts`, `/api/recovery/*` |
| Question stream | Per question: `seen`, `attempted` (option, correct or not, time), `skip`; save (`/api/bookmarks`), vote, and report with a reason label | `insights/data/stream_controller.dart:178,194`, `feed_api.dart` |
| Concepts | Lesson and recall-card events for a run | `learn/data/study_api.dart` (`/api/study/runs/{id}/events`), study length preference |
| Goal and reminders | Goal days, pause date, timezone, quiet hours, channels on, weekly cap, study window | `/api/me/goal`, `/api/me/notification-prefs` |
| AI mentor | The typed message and a session id; the server adds a compact study summary and sends both to the model provider. A reply report (reason) if the endpoint exists | `/api/ai/mentor/chat`, `ai_reply_report.dart` |
| Usage data (adults only, optional, off by default) | Event name, time, app version, at most a few labels. Allowlist of 19 events and 10 prop keys; the server rejects anything else. Kept 180 days, deleted on withdrawal | `core/analytics/event_allowlist.dart`, `POST /api/events` |
| Delete request | A deletion request, source `android` | `POST /api/me/delete` |
| CUET tools | Public DU data is only fetched (`GET /api/compass/pro` and the DU source). Compass subjects, category, score, Combo targets and shortlist stay in on-device preferences | `tools/data/tools_store.dart` |
| Not sent | Contacts, location, photos, files, microphone, camera, advertising ID, Android ID, push token (no Firebase), phone number (`PHONE_SIGN_IN` is off), crash reports (no crash SDK; Play vitals are Google's own) | `pubspec.yaml`, manifest |

Release permissions: INTERNET, ACCESS_NETWORK_STATE, POST_NOTIFICATIONS, RECEIVE_BOOT_COMPLETED, WAKE_LOCK, VIBRATE, FOREGROUND_SERVICE, FOREGROUND_SERVICE_SHORT_SERVICE, USE_BIOMETRIC, USE_FINGERPRINT (13 Oct build; the manifest declares the first five, plugins add the rest). Re-run `aapt2 dump badging` on the exact AAB you upload.

Third parties that touch data, all acting for MockMob: Supabase (auth and database), Google (Google sign-in only), Resend (sign-in email), the AI model provider (mentor text), Vercel (hosting). **[CONFIRM]** the AI provider's terms bar training on API data; "service provider" only holds if they do.

### 2.2 Answers

**Overview**

| Question | Answer |
|---|---|
| Does the app collect or share any required user data types? | Yes, collects. Shares: No |
| Is all collected data encrypted in transit? | Yes. API base `https://www.mockmob.in`, Supabase over HTTPS, no cleartext permission in the release manifest (cleartext is in the debug manifest only) |
| Can users request that their data is deleted? | Yes |
| Account creation methods | Email (code or password) and Google |
| Deletion in the app | You, Account, Delete account |
| Deletion web page | `https://www.mockmob.in/account-deletion` (add the exact app name first, section 0 item 4) |
| Delete some data without deleting the account | Yes: turning usage data off (You, Privacy) stops collection and deletes earlier usage data |
| Retention shown in the form | Account and study records are deleted within 30 days of a request; payment records required by law are kept; usage data is kept 180 days |
| Independent security review | No |
| Committed to Play Families policy | No (the app is not designed for children) |

**Data types.** Collected: Yes for every row. Shared: No for every row (service-provider exemption). Ephemeral: No.

| Type | Required or optional | Purposes | Basis |
|---|---|---|---|
| Personal info: Email address | Required | App functionality, Account management, Fraud prevention, security and compliance | Sign-in and account matching |
| Personal info: Name | Optional | App functionality, Account management | Arrives with Google sign-in or when the student types a name; code and password sign-in do not send one |
| Personal info: User IDs | Required | App functionality, Account management, Analytics (consented events only) | MockMob and Supabase ids link every record |
| Personal info: Other info (age band) | Optional | App functionality, Fraud prevention, security and compliance | "No" and "Prefer not to say" are accepted; it decides whether the usage-data switch can exist |
| App activity: App interactions | Required | App functionality, Personalization, Analytics (consented events only) | Answers, timing, submit, results, stream views and attempts, lesson events, goal progress, optional usage events |
| App activity: Other user-generated content | Optional | App functionality | Saves, votes, question reports with a reason label. No free text goes to other students |
| App activity: Other actions | Optional | App functionality, Personalization | Weekly goal, pause date, reminder preferences, timezone, quiet hours, subjects, study time |
| Messages: Other in-app messages | Optional | App functionality, Personalization | AI mentor messages sent to the model provider on MockMob's behalf. Optional because the app works without them |

**Not collected, leave unticked:** Location, Financial info (the app reads Pro status but sends no payment or purchase record), Health and fitness, Photos and videos (the Google profile picture is a link stored on the server, not an upload; tick Photos, optional, account management, if you want zero risk), Audio, Files and docs, Calendar, Contacts, Web browsing, Installed apps, In-app search history, Crash logs, Diagnostics, Device or other IDs, Phone number.

Judgement calls the owner can overrule: question-stream events are declared inside "App interactions: Required" (section 0, item 5); the connecting IP is hashed into a rate-limit bucket and is not a Play data type; if Firebase push is added, add Device or other IDs first; if `PHONE_SIGN_IN` is turned on, add Phone number and update the policy first.

After saving, preview the Data safety card and read it against the privacy page.

---

## 3. Content rating questionnaire (IARC)

Category: Reference, News or Educational. Contact: `support@mockmob.in`. Answer what the app does; do not adjust answers to chase a rating.

| Topic | Answer | Basis |
|---|---|---|
| Violence, blood, fear | None | CUET Commerce questions only |
| Sexual content or nudity | None | |
| Profanity or crude humour | None | |
| Drugs, alcohol, tobacco | None | |
| Gambling, simulated gambling, contests with prizes | No | No prizes, no loot or variable-reward mechanics |
| Users can communicate or exchange content | No | No chat or posting between students. Votes and reports go to MockMob only |
| Shares location | No | No location permission |
| Collects personal information | Yes | Email, optional name, age band, study records (section 2) |
| Digital purchases in the app | No | No Play Billing, no checkout |
| Unrestricted internet or browser | No | Links open MockMob pages only; pricing and off-domain links are refused (`action_router.dart`) |
| Generative AI features | Yes | Optional text mentor for study help; users can report a reply (after the endpoint exists) |
| Ads | No | |
| User-generated content that could be mature | None | Only the platform's own question bank |

Expected result: an all-ages rating. The AI answer may raise it in some regions. The rating does not set the target audience.

**Target audience (same section of the Console):** tick `16-17` and `18 and over`. Not designed for children, not for Designed for Families, no 18+ restriction. The age question in the app allows "Prefer not to say", so minors may use the app; the server only allows usage data for an adult (`PUT /api/me/consent`, `POST /api/events`). Whether 16 to 17 year olds count as children under India's DPDP rules (from about 13 May 2027) needs a lawyer before production.

---

## 4. Other declarations

| Declaration | Answer |
|---|---|
| Ads | No ads |
| Advertising ID | Not used |
| App access | Reviewer email and password (PLAY-RELEASE section 5). Update the step wording to the final screen labels |
| Government app | No |
| Financial features | None |
| Health | None |
| News | No |
| In-app purchases | None. Do not tick "contains in-app purchases" |
| Foreground service | If asked: `shortService`, from the background sync library used to send queued answers **[CONFIRM]** |
| Countries | India only for the closed test |

---

## 5. The 8 phone screenshots

Capture on the emulator (main test device), portrait 1080 x 1920, Night theme, the reviewer account with a few real sessions so numbers are genuine. Do not edit numbers in the images. Set the phone clock to 12-hour time. Captions are overlay text, under 30 characters, sentence case, no claims about rank or improvement. Mobi stays small and incidental.

| # | Screen and state | Route | Caption | Length |
|---|---|---|---|---|
| 1 | Today with one next step: the hero move, its reason line and "Start now, about 10 minutes". Mobi small in the header | `/today` | One next step, and why | 22 |
| 2 | Practice tab showing Quick practice, By chapter, Full mock and NTA mode | `/practice` | Pick how you practise | 21 |
| 3 | NTA mode in progress: palette open, one option chosen, a question marked for review | `/run/{id}` | The exam-day screen | 19 |
| 4 | Full result: net marks and the "Where the marks went" ledger by chapter | `/result/{id}` | See where the marks went | 25 |
| 5 | Review: mistakes grouped by chapter, with the skipped note | `/review/mistakes` | Mistakes, grouped by chapter | 28 |
| 6 | Repair of one mistake: the question, the key explanation, "Next mistake" | `/review/repair/{id}/{q}` | Repair one mistake at a time | 28 |
| 7 | Weekly goal and rhythm: study days with Counted, Planned and Rest marked | `/you/rhythm` | A weekly goal you choose | 24 |
| 8 | Admission Compass with subjects ticked and the programmes they open | `/tools/compass` | Which DU courses open | 21 |

Alternates if one fails review: submit sheet (answered, marked, not answered) for 3, and reminders with the usage-data switch off (You, Notifications and Privacy) for 8. Reminders and usage data are worth showing before production because they state the privacy position in the app's own words.

Capture notes: screens 3 and 8 need an account that has NTA mode and Compass open. If the reviewer account is not Pro, capture 3 as a Full mock runner instead and rename the caption "Timed like the exam" (19).

---

## 6. Length check

Counted by script on 14 Oct 2026 (Python `len` on each fenced block of section 1): short description 70 of 80, full description 3,200 of 4,000, release notes 413 of 500, app name 21 of 30. Screenshot captions are 19 to 28 characters. The text has no em dashes and no exclamation marks. Recount after any edit.

## Permissions in the actual release build (checked 14 Oct 2026, 07:05 IST, aapt2 on the arm64 release APK)
The merged manifest has 9 permissions, not the 5 in RELEASE.md. The four extra come from plugins:
- VIBRATE: flutter_local_notifications (reminder vibration).
- FOREGROUND_SERVICE and FOREGROUND_SERVICE_SHORT_SERVICE: workmanager / androidx.work (expedited background work runs as a short-service FGS). Short service is not a Play "special type" (no declaration video), but the Play Console foreground-service declaration should say the app uses it for short background sync of answers. FOREGROUND_SERVICE_DATA_SYNC is not declared.
- USE_BIOMETRIC: from a plugin dependency (see the merger report); the app never asks for biometrics.
Update RELEASE.md's permission row and the Data safety notes before the first upload.
