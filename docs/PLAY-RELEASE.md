# MockMob on Google Play: closed test pack

Written 13 Oct 2026 for package `in.mockmob.app` (Flutter app in `flutter_app/`, branch `feat/app-and-web`). Everything below is what to type or tick in Play Console for a closed test, grounded in the code as it stands today. Items that could not be confirmed are marked **[CONFIRM]**. This is not legal advice.

Sources for Play rules are numbered [S1] to [S12] at the end. Code facts name the file they come from.

Standing decisions this pack relies on (from the owner, not re-opened here): no in-app purchase (a Pro plan bought on the web is honoured), minimal first-party usage data only for consenting adults, data deletion at `https://www.mockmob.in/account-deletion`, support email `support@mockmob.in`, the app is not affiliated with NTA, DU or any government body.

---

## 0. The five things most likely to get this rejected or flagged

Read these first. Each one is also in section 9 as a fix with an owner.

1. **Payments policy, steering.** The app says "Plans are managed on mockmob.in. Pro bought there works here." (`lib/features/you/edit_copy.dart:113`). Play's Payments policy says apps "may not lead users to a payment method other than Google Play's billing system", and lists in-app promotions, buttons, links and account flows [S8]. The code already refuses to open pricing, checkout and subscribe links (`lib/core/router/action_router.dart`), which is right. The sentence that names the website as the place to buy is the risk. Recommend: say only "Pro is active" or "Pro is not active on this account", with no mention of where plans are bought. Keep Pro out of the store listing too. The design spec already lists "Play policy review of the no-price rule and of any mention of Pro" as an open item (APP-DESIGN-SPEC.md, section 13, item 7). Whether Play accepts honouring web purchases in a non-reader app is not settled by the policy text [S8]; treat it as a known risk.
2. **Generative AI content policy.** The app has an AI mentor chat (`POST /api/ai/mentor/chat`, `lib/features/insights/data/ask_controller.dart`). Play requires apps that generate content from user prompts to let users report or flag offensive output inside the app without leaving it [S9]. Question screens have a report control (`question_actions.dart`, `report_key.dart`). The AI reply bubbles do not appear to have one. Add a "Report this reply" control, wired to a server endpoint that stores the report, before the closed test goes to production. **[CONFIRM]** against the final build.
3. **Privacy policy does not match the app.** `src/app/privacy/page.js` says the Android app stores a push notification token. v1 has no push and no Firebase (`push_transport.dart`, design spec A3); reminders are local. It also does not mention the AI mentor text or the per-question view and answer events (item 5). Play compares the form, the policy and the app. Fix the policy text (section 9).
4. **Accounts and the deletion page name.** Play wants the deletion web page to "reference the app or developer name as it appears on Google Play" [S6]. `src/app/account-deletion/page.js` only says MockMob. Use the exact listing name "MockMob: CUET UG Prep" on that page.
5. **Question view events are not behind the usage-data switch.** The app logs `seen`, `attempted` and `skip` (with time spent) per question in the explore stream to `POST /api/questions/{id}/interact` (`stream_controller.dart:178-194`, `feed_api.dart`), for every signed-in user including minors. The in-app text says the usage-data switch is the only optional data and lists "sessions, scores, notification settings and plan" as operational (`lib/features/you/copy.dart`, `operationalNote`). Question views are not named there. This pack declares them honestly in the Data safety form (section 2) as required app functionality. The owner and the integrator should decide: either name them in the policy and in the app, or gate the explore-stream logging on the same consent. PRODUCT.md already notes that under-18 consent and monitoring rules under DPDP apply from about 13 May 2027 and need legal review.

---

## 1. Store listing

### 1.1 Text

| Field | Limit | Value |
|---|---|---|
| App name | 30 | `MockMob: CUET UG Prep` (21 characters) |
| Short description | 80 | `Timed CUET UG mocks that show where you lost marks, then help you repair them.` (78 characters) |
| Default language | | English (India) `en-IN` |
| App or game | | App |
| Free or paid | | Free (cannot be changed to paid later) |
| Category | | Education |
| Tags | up to 5 | Education, Exam preparation, Test prep, Study, Quiz (pick what the Console offers) |
| Developer contact email | public | `support@mockmob.in` |
| Website | | `https://www.mockmob.in` |
| Phone | not public on listing for personal accounts, used for verification | the owner's number, own entry **[CONFIRM]** |
| Privacy policy URL | | `https://www.mockmob.in/privacy` (after the fixes in section 9) |

Name rules to respect: no emoji, no "free", "best", "#1", no store-performance words, no repeated keywords. The name must contain "MockMob" so the deletion page can match it. A second name option if the first is refused: `MockMob: CUET UG Mocks` (22).

### 1.2 Full description (2410 of 4000 characters)

Plain, specific, no numbers that are not in the code, the non-affiliation statement near the end. Do not add price, a Pro mention, "official", rank or marks-improvement promises. Before pasting, check every line against the build you submit (the verify list is in 1.4).

```
MockMob is a practice app for students preparing for CUET UG 2027. It is built around one idea: a mock test should show you where you lost marks and what to do about it, not only hand you a score.

TAKE A TIMED MOCK
- Sit a timed mock on an exam-style screen with a question palette, mark for review and a clear submit step.
- Marking follows the CUET pattern: 5 marks for a correct answer, minus 1 for a wrong one.
- If your connection drops, your answers stay on your phone and are sent when you are back online.

SEE WHERE THE MARKS WENT
- Each result breaks your marks down by chapter, so a weak chapter shows up as a pattern instead of a vague feeling.
- Go back through every question you got wrong, with the correct answer, and a separate list for the ones you skipped.

REPAIR, THEN MOVE ON
- Today suggests one small next step from your own record and tells you why it was suggested. Start it, or leave it for another day.
- Short chapter practice and study lessons let you work on one weak chapter at a time.
- Set a weekly goal that fits your week, and pause it when life gets in the way.
- Reminders are optional and run on your phone. You choose which ones you want and your quiet hours, and you can switch them off at any time.

BUILT FIRST FOR COMMERCE
MockMob starts with the CUET UG Commerce papers: English, Accountancy, Business Studies and Economics.

ASK ABOUT YOUR RECORD
Ask a question about your own results, such as which chapters cost you the most marks. Answers about your record come from your record. An optional AI mentor can also reply. AI replies can be wrong, so check them against your answer key and your textbook.

YOUR ACCOUNT AND YOUR DATA
- Sign in with a code sent to your email, with Google, or with a password you set yourself.
- There are no ads in the app.
- Usage data is optional. It is off by default and can only be turned on by someone who says they are 18 or older. You can turn it off at any time.
- You can delete your account from inside the app, or at www.mockmob.in/account-deletion.

NOT AFFILIATED
MockMob is an independent practice app. It is not affiliated with, endorsed by or sponsored by the National Testing Agency (NTA), the University of Delhi or any government body. CUET is the name of an examination conducted by NTA. For official exam notices, dates and rules, use the NTA website, cuet.nta.nic.in.

Questions or feedback: support@mockmob.in
```

The non-affiliation sentence matches the in-app copy (`lib/features/you/copy.dart`, `helpNonAffiliation`) and the Welcome footer in the design spec. The paragraph "BUILT FIRST FOR COMMERCE" names only the four launch subjects (PRODUCT.md, SPEC). The app exposes 15 supported subjects through `/api/subjects`; whether the other 11 are good enough to name is an open content question (APP-DESIGN-SPEC 5.1.2), so they are left out. The sentence about fresh-question checks ("prove it") is left out on purpose: that feature is gated off (`FRESH_CHECKS_LIVE=false`).

### 1.3 Graphics

Sizes and limits, checked on Play's page [S3]:

| Asset | Requirement | Plan |
|---|---|---|
| App icon | 512 x 512 px, 32-bit PNG with alpha, at most 1024 KB | Export from the brand source. The repo has `public/pwa/icon-512.png` (web) and the Android launcher set (`tool/make_icons.py` builds it). Confirm the 512 master matches the in-app adaptive icon (volt background, dark mark). |
| Feature graphic | 1024 x 500 px, JPEG or 24-bit PNG, no alpha | One image: the MockMob wordmark, one line ("Find the marks you lose. Repair the mistake."), and a cropped real screen (the result ledger). No Mobi as the hero (see the warning below). No store badges, no "free", no "#1". |
| Phone screenshots | 2 to 8 required, 320 to 3840 px per side, longest side at most 2x the shortest, JPEG or 24-bit PNG no alpha. 9:16 portrait recommended. For the promo-eligible tier, at least 4 at 1080 px minimum | Take 8, portrait, 1080 x 1920 (9:16) from the emulator (the owner's main test device) with the reviewer-style test account. |
| 7 inch and 10 inch tablet, Chromebook | Optional for a phone app. If added: at least 4, 1080 to 7680 px, 16:9 or 9:16 | Skip for the closed test. Revisit before production. |
| Promo video | YouTube URL, public or unlisted, no ads | Skip. |

The eight phone screens, in order. Each is a real screenshot of the shipping UI, no mock-ups, no invented marks or student counts:

1. Today with one next step and its reason.
2. The timed runner with the answer sheet and palette.
3. The submit sheet (answered, marked for review, not answered).
4. The result: marks ledger and chapter breakdown.
5. Review: mistakes grouped by chapter, with the skipped list.
6. A repair card for one mistake.
7. Weekly goal and rhythm.
8. Reminders and the usage-data choice (shows the privacy stance).

Caption text on screenshots, if any, stays factual ("Find the chapter that costs you marks"). No rank, percentile or improvement claims. Use the emulator capture the integrator produces; do not edit numbers in the images.

**Warning on the mascot.** Play can reject an app that picks an adult age group when its marketing "suggest[s] children are the audience, such as youthful animation or young characters in graphic assets" [S5]. Mobi is a character. Keep Mobi small and incidental in screenshots (it appears on empty states), never the hero of the feature graphic or icon.

### 1.4 Verify list before pasting the description

Each claim, where it comes from, and what to confirm on the submitted build:

| Claim | Basis | Confirm |
|---|---|---|
| Timed mock, palette, mark for review, submit step | design spec 5.5, runner feature | Runner screenshot shows them |
| +5 / -1 marking | ARCHITECTURE.md, `lib/core/domain/marks.dart` | Result screen shows marks the same way |
| Answers kept on phone when offline | `lib/core/sync/*`, outbox, spec "Your work is still on this phone" | Test with airplane mode on the emulator |
| Chapter breakdown, skipped list | design spec 5.6 and 5.8 | Result and Review screenshots |
| Today next step with reason | design spec 5.3 (`next_move`) | Today screenshot |
| Weekly goal with pause | `PUT /api/me/goal` (pausedUntil) | Rhythm screenshot |
| Reminders optional, quiet hours | `notification_prefs`, `quiet_hours.dart` | You, Notifications screen |
| Answers about your record come from the record; optional AI mentor | `ask_controller.dart` (local answer first, then `/api/ai/mentor/chat`) | Ask screen; AI report control present (section 0, item 2) |
| Sign in with email code, Google, password | `docs/AUTH.md` | Sign-in screen; Google needs the Supabase redirect URL and OAuth setup (section 10) |
| No ads | pubspec has no ad SDK; no AD_ID permission in the built APK | n/a |
| Delete account in the app | `lib/features/you/account/delete_screen.dart` | You, Account, Delete |

---

## 2. Data safety form

Rules used, from Play's own guidance [S4]: "collect" means data transmitted off the device, including by SDKs; data processed only on the device is not collected. "Share" means transfer to a third party, except to **service providers that process data only on your behalf**, user-initiated transfers the user expects, legal transfers and fully anonymised data. Answer "encrypted in transit" yes only if everything the app and its SDKs send is. Mark a type optional only if every user can decline it and still use the app.

### 2.1 What the app actually sends (the evidence)

| Where | What goes off the phone | Source |
|---|---|---|
| Sign-in | Email address (code sign-in, password sign-in); for Google, an ID token from Google, after which the server holds name, email and a profile picture link from Google | `lib/core/auth/*`, `src/lib/auth.ts` (name, email, `avatar_url` stored on the MockMob user) |
| Account | MockMob user id, Supabase user id, subjects, role, practice credit balance, Pro status and end date (the app only reads these) | `lib/core/models/auth_me.dart` |
| Age question | `ageBand`: adult, minor or unknown, and the usage-data choice | `PUT /api/me/consent` |
| Practice and mocks | Chosen subject and chapter, answers, answer changes, visits and time on each question, submit time, resulting marks and per-question result | `POST/PATCH/PUT /api/sessions`, `src/lib/server/recoverySessions.js` (`recordEvents`, `finishSession`) |
| Question stream | Per question: seen, attempted (selected option, correct or not, time spent), skip; save, vote, report (with a reason label) | `stream_controller.dart`, `feed_api.dart`, `src/app/api/questions/[id]/interact` |
| Goal and reminders | Weekly goal days, pause date, timezone, quiet hours, which reminder channels are on, weekly cap, study window | `/api/me/goal`, `/api/me/notification-prefs` |
| Repair and rhythm | Repair acknowledgements; reads of rhythm and bests | `/api/me/repair-record`, `/api/me/rhythm`, `/api/me/bests` |
| First sample answers | The five guest sample answers, imported once after sign-in | `/api/me/sample-import` |
| AI mentor | The student's typed message and a session id; the server adds a compact study summary and sends it to the model provider | `/api/ai/mentor/chat`, `src/app/privacy/page.js` ("Optional AI") |
| Usage data (adults only, optional, off by default) | Event name, time, app version and at most a few labels (subject, mode, state, screen, count, minutes). Names and keys are a fixed allowlist of 19 events and 10 props; the server rejects anything else. Kept 180 days, deleted on withdrawal | `lib/core/analytics/event_allowlist.dart`, `src/lib/server/usage.js`, `POST /api/events` |
| Delete request | A deletion request row (source `android`) | `POST /api/me/delete` |
| Not sent | Contacts, location, photos or files, microphone, camera, advertising id, Android id, push token (no Firebase in v1), phone number (phone sign-in is off: `PHONE_SIGN_IN=false`), crash reports (no crash SDK; Play collects vitals itself) | pubspec.yaml, built-APK permission list |

Permissions in the release APK (checked with `aapt2 dump badging` on `build/app/outputs/flutter-apk/app-arm64-v8a-release.apk`, built 13 Oct 10:50): INTERNET, ACCESS_NETWORK_STATE, POST_NOTIFICATIONS, RECEIVE_BOOT_COMPLETED, WAKE_LOCK, VIBRATE, FOREGROUND_SERVICE, FOREGROUND_SERVICE_SHORT_SERVICE, USE_BIOMETRIC, USE_FINGERPRINT. No AD_ID, no location, no contacts, no storage. Re-run this on the exact AAB you upload.

Third parties that touch data: Supabase (auth and database, the service provider), Google (only for Google sign-in), Resend (sends the sign-in email), the AI model provider (receives the mentor text), Vercel (hosts the API). Razorpay is website-only and not in the app. All are processors acting for MockMob. The server also sees the connecting IP address for abuse limits; it is hashed into a rate-limit bucket (`src/lib/server/rateLimit.js`) and is not a Play data type, so it is not declared. **[CONFIRM]** that the AI provider's terms bar training on API data; "service provider" only holds if so.

### 2.2 Answers to the form

**Section: data collection and security**

| Question | Answer |
|---|---|
| Does your app collect or share any of the required user data types? | Yes |
| Is all of the user data collected by your app encrypted in transit? | Yes. API base is `https://www.mockmob.in`, Supabase is HTTPS, no cleartext permission in any manifest. |
| Do you provide a way for users to request that their data is deleted? | Yes. In app: You, Account, Delete account. Web: `https://www.mockmob.in/account-deletion`. |
| Account creation methods | Email (code or password) and Google |
| Deletion URL | `https://www.mockmob.in/account-deletion` |
| Independent security review ("Independent security review" badge) | No |

**Data types.** Every row is "Collected". Shared is **No** for all rows, on the service-provider exemption [S4]. "Ephemeral" is **No** except where noted.

| Category and type | Required or optional | Purposes | Why |
|---|---|---|---|
| Personal info: Email address | Required | App functionality, Account management, Fraud prevention, security and compliance | Sign-in and account matching |
| Personal info: Name | Optional | App functionality, Account management | Only arrives when signing in with Google; code and password sign-in never send it. Used for the greeting |
| Personal info: User IDs | Required | App functionality, Account management, Analytics (only for adults who opted in) | MockMob id and Supabase id link all records and consented events |
| Personal info: Other info (age band: adult, minor, unknown) | Optional | App functionality, Fraud prevention, security and compliance | "Rather not say" is allowed. Decides whether the usage-data switch can exist |
| App activity: App interactions | Required | App functionality, Personalization, Analytics (the consented events only) | Answers, timing, submit, results, question views and attempts, goal progress. Core to mocks, repair and Today |
| App activity: Other user-generated content | Optional | App functionality | Saves, votes and question reports (reason label). The app has no way to post questions or free text to other students |
| App activity: Other actions | Optional | App functionality, Personalization | Weekly goal, pause date, reminder preferences, timezone, quiet hours |
| Messages: Other in-app messages | Optional | App functionality, Personalization | The text of AI mentor messages, sent to the model provider on MockMob's behalf. Optional because the app works without it |

**Not collected, do not tick:** Location, Financial info (the app reads Pro status but never sends a payment or purchase record; Razorpay is on the web), Health and fitness, Photos and videos, Audio, Files and docs, Calendar, Contacts, Web browsing, Installed apps, In-app search history, Crash logs, Diagnostics, Device or other IDs, Phone number.

Judgement calls to record, so the owner can overrule them:

- **Profile picture.** The server stores the Google avatar link (`image`). It is a link, not an image the app uploads, so "Photos" is not ticked. Tick "Photos and videos: Photos" (optional, account management) if you want zero risk.
- **Diagnostics.** The app version rides only on consented usage events. Play vitals come from Google, not from the app. Not ticked, and the in-app text already says so (`operationalNote`).
- **Question views (section 0, item 5).** Declared above inside "App interactions: Required". If you gate them on consent later, App interactions stays Required because mocks still need it.
- **Phone number.** If you ever switch `PHONE_SIGN_IN` on, add Personal info: Phone number (required for that path) and update the policy first.
- **Push tokens.** If Firebase is added, add Device or other IDs, and update the form before that release.

After you save, preview the "Data safety" card and read it against the privacy page. Anything the page does not say, add to the page.

---

## 3. Content rating questionnaire

Category to choose in the questionnaire: **Reference, News or Educational** (an exam-preparation app). The IARC wording changes; match by topic. Email for IARC correspondence: `support@mockmob.in`. Accuracy matters: wrong answers can get an app removed [S7].

| Topic | Answer | Basis |
|---|---|---|
| Violence, blood, fear | None | Question content is CUET Commerce papers |
| Sexual content or nudity | None | |
| Profanity or crude humour | None | |
| Controlled substances (drugs, alcohol, tobacco) | None, not depicted or promoted | |
| Gambling, simulated gambling, contests with prizes | No | No gambling mechanic, no prizes. The design spec bans loot-style and variable-reward mechanics (section 6) |
| Users can communicate with or exchange content with each other | No | No chat, comments or posting between students. Votes and reports go to MockMob only |
| Shares the user's location with others | No | No location permission |
| Collects or shares personal information | Yes: account email, name, age band, study records (as in section 2). Not shared with third parties beyond service providers | |
| Digital purchases in the app | No | No Play Billing and no checkout in the app |
| Unrestricted internet access or a web browser | No | Links open only MockMob pages in a Custom Tab; pricing and off-domain links are refused (`action_router.dart`) |
| Generative AI features | Yes if asked: text replies from an optional AI mentor, for study help | `/api/ai/mentor/chat`. If the form asks, say AI replies are limited to study topics and users can report them (after the section 0 fix) |
| Ads | No | |
| Mature or unrated user-generated content | None. The app shows only the platform's own question bank | |

Expected result: an "all ages" style rating (IARC 3+, PEGI 3, ESRB Everyone) is likely, but regional authorities can adjust and the AI answer may raise one. Accept what the summary shows; do not change answers to chase a rating. The rating does not decide the target audience in section 4.

---

## 4. Target audience and content

**Age groups to tick:** `16-17` and `18 and over`. Do not tick 13-15, 9-12, 6-8 or 5 and under. CUET UG students are in Class 11 and 12 or are drop-year repeaters (PRODUCT.md), so almost everyone is 16 or older.

**Questions on the page:**

| Question | Answer |
|---|---|
| Does the app appeal to children (under 13)? | No |
| Is the app designed for children? | No |
| Do you want it in "Designed for Families"? | No, do not opt in |
| Restrict Minor Access (18+ only option) | Not used. The audience includes 16 to 17 year olds. |
| Ads in the app | None. Select "No ads" in the Ads declaration |

**What this implies [S5]:**

- Selecting 13-17 groups makes Play consider whether those users count as children under local law. Play says apps aimed at anyone under 21 "must consider whether those users would count as children under local law" and, if so, Families policy applies [S5]. Families policy is mandatory for apps that include children under 13 (we do not target that). For 16 to 17 the page leaves the consequence open. India's DPDP definition of a child is under 18, and PRODUCT.md already flags that its consent and monitoring rules start about 13 May 2027 and need legal review. **[CONFIRM] with a lawyer before production**; do not treat this pack as clearing it.
- So build to the stricter reading now, and the app mostly already does: no ads, no advertising id, no third-party analytics or tracking SDK, usage data off by default and only for someone who says they are 18 or older. The server enforces it, it does not rely on the app: `PUT /api/me/consent` refuses `analyticsAllowed: true` unless `ageBand` is `adult`; `POST /api/events` returns `collecting:false` and stores nothing unless the consent row says adult, allowed and not withdrawn (`src/app/api/events/route.js`, `src/lib/server/usage.js`); withdrawing deletes stored events. The client queues nothing unless the gate is open and clears its queue on sign-out and withdrawal (`analytics_client.dart`).
- The age answer is a self-declaration with "Not yet" and "Rather not say" choices. That is a neutral, non-leading screen for this purpose: no birth date is preset and nothing says an age is required [S5].
- The listing and graphics must not look child-directed (see the mascot warning in 1.3).
- Teen-facing safeguards in the app: no leaderboard shown to students, no streak-loss notifications, reminders capped (default 3 a week) with quiet hours 11 pm to 7 am (design spec, sections 6.10 and 8).
- Remaining gaps for minors to close before production: question view events (section 0, item 5) and the DPDP review.

---

## 5. App access for reviewers

The app needs sign-in for mocks, so Play needs credentials [S10]. Email code sign-in is not usable for a reviewer (the code goes to an inbox they cannot open), so use **email and password**, which the app now supports (`docs/AUTH.md`; no password sign-up in the app, so the owner creates the account first).

**Create it (owner, once, on production):**

1. On `https://www.mockmob.in`, sign in with an email code using a dedicated address you control, for example `playreview@mockmob.in` or a new Gmail used only for this. Not your own account. **[CONFIRM]** the address can receive the code.
2. In the app, You, Account, "Set a password". Choose a long random password and store it in your password manager.
3. Answer "Are you 18 or older?" with Yes on this account, so reviewers can see the usage-data switch. Leave the switch off.
4. Complete the first-mock steps once so reviewers land on a populated Today, or leave it clean; either works.
5. If you want reviewers to see Pro-gated screens, grant that account Pro yourself with your admin tool. An agent must not touch production data. Not required for approval.
6. Keep the account alive. Do not delete or rename it while review is open. Change its password after approval.

**Paste into Play Console, App content, Sign-in details, "Add new instructions":**

```
Name: Reviewer account
Username: [the dedicated email address]
Password: [the password]

Instructions:
1. Open the app. On the welcome screen tap "I already have an account".
2. Choose the "Password" sign-in method (not the email code option, which needs inbox access). The screen is titled "Sign in with a password".
3. Enter the email and password above and tap Sign in.
4. After signing in you land on Today. The bottom bar switches between the main areas (Today, Practice, Review and more).
5. To try a timed mock: Practice, choose a subject (English, Accountancy, Business Studies or Economics), choose Quick, start, answer a few questions, tap Submit, open the result.
6. Account deletion is under You, Account, Delete account. Do not complete it on this account.
7. No two-factor step, no one-time code and no location or membership restriction applies. The app works in India and outside it. Sign-in with Google is also offered but is not needed for review.

The app is a CUET UG practice tool. It is not affiliated with NTA, the University of Delhi or any government body.
```

**[CONFIRM]** the labels "I already have an account", "Password", "Quick" and the tab names (the tab set is being rebuilt by other agents) against the shipped build and edit the text to the exact words on screen; Play reviewers follow it literally.

If the Pro mode needs a credit or a plan the account lacks, the app shows a "comes with Pro" line and a free alternative. That is expected, not a bug, and is why step 5 above is optional.

---

## 6. Other declarations in App content

| Declaration | Answer | Notes |
|---|---|---|
| Privacy policy | `https://www.mockmob.in/privacy` | Required for every app. Must be on a live URL and match the form |
| Ads | No, the app does not contain ads | No ad SDK in pubspec; no `AD_ID` permission in the built APK |
| Advertising ID | The app does not use it | Targeting Android 13+ requires the question to be answered; no ad id is read |
| App access | Instructions in section 5 | |
| Content rating | Section 3 | |
| Target audience and content | Section 4 | |
| Data safety | Section 2 | |
| Government apps | **No, this is not a government app.** Not developed by or on behalf of a government. | Add the same disclaimer used in the listing and in the app (You, About). The listing shows "not affiliated with NTA, the University of Delhi or any government body" |
| Financial features | My app does not provide any financial features | No loans, wallet, payments, banking or crypto in the app. Razorpay is on the website only |
| News apps | No, not a news app | |
| Health apps | No health features | Select the "none" option |
| Social features, COVID-19, gambling | None | |
| Foreground service permissions | If Play shows the declaration, the type is `shortService`, from the background sync library (WorkManager), used to send queued answers | The two permissions come from plugins, not from the manifest (`FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_SHORT_SERVICE`). **[CONFIRM]** whether the Console asks; if it asks for a video, ask the integrator whether the permission can be removed instead |
| Data deletion | Section 2.2 | The in-app path and the web page both exist |
| Payments (no Play Billing) | Do not tick "contains in-app purchases" | Section 0, item 1. The app has no purchase |
| Trader status (EU) | **[CONFIRM]** in Account details | If you distribute in the EU you must declare trader or not. The simplest path for the test and for launch is India only. Selling a plan on the website probably makes you a trader. Check Play's Account page before adding countries |

---

## 7. Closed test setup

### 7.1 The rule

Play requires personal developer accounts created after 13 Nov 2023 to run a closed test "with a minimum of 12 testers who have been opted in continuously for at least 14 days" before applying for production access. A tester who opts out before 14 days does not count; opting out and in again needs the 14 days to be consecutive. Production is locked until the criteria are met. After the 14 days you click "Apply for production" on the Dashboard and answer questions about the test, the app and readiness. Review usually takes seven days or less. Play can ask you to keep testing if there are fewer than 12 opted-in testers or "insufficient tester engagement" [S1].

**Your earlier app.** The owner said the 14 days were already done on this account, for another app. Google's text frames the requirement as "for their app" and does not say whether a second app on the same account must repeat it [S1]. Community reports disagree. Do not assume either way: open the new app's Dashboard in Play Console. If "Apply for production" is already available, the gate does not apply and the closed test is a normal pre-launch test. If Production is greyed out, run the 14 days with this app. The same 12 people can be the testers.

### 7.2 Track and release

| Item | Value |
|---|---|
| Track | Testing, Closed testing. Use the default track (named "Alpha") or create one named `mockmob-closed` |
| First upload | A signed release AAB (`flutter build appbundle --release --dart-define-from-file=dart_defines/prod.json --build-number N`, see `flutter_app/docs/RELEASE.md` when it lands, and `dart_defines/README.md`). Must be signed with the owner's upload key, never the debug key. `build.gradle.kts` silently debug-signs when `android/key.properties` is missing, and Play rejects that |
| Version | `versionCode` must go up with every upload. Start with a small number above 0 and add 1 each time; never reuse one |
| Countries | India only |
| Release name and notes | `1.0.0 (closed test 1)`; notes in plain English, what to test (below) |
| App signing | Accept Play App Signing (the default for a new app). The owner keeps the upload key (`tool/make_upload_key.ps1`, run by the owner; the key and passwords never go to an agent or the repo) |

### 7.3 Testers

Use **a Google Group**; it is the easiest way to add and remove people without editing the Console list:

1. Create a group at groups.google.com, for example `mockmob-testers@googlegroups.com`. Set it so only managers can add members (or members join by invite), and set "Who can view members" to members only.
2. Add testers by their Google account emails (the same account their Play Store uses). Aim for **20 to 25**, not 12. People drop out, and one drop under 12 can set the count back [S1, S11].
3. In Play Console: Closed testing, Testers, Create email list or select "Google Groups", enter the group address, save.
4. Set a feedback email: `support@mockmob.in`.
5. Copy the **opt-in URL** (Testers tab, "How testers join"). Send it to everyone, with the instructions below.

Rules for who counts as a tester: a real person with an Android phone, a Google account, the Play Store, and Android 7.0 or newer (the app's minSdk is 24, `build.gradle.kts`). Friends, classmates, students you teach, family. Do not buy testers from a "tester service": the Play review looks at engagement, and the testing is meant to be genuine [S1]. Under-13 accounts cannot be used.

### 7.4 What each tester must do to count

Send this text with the link:

```
Help me test MockMob (a CUET UG practice app) on Google Play.
1. Use the Google account that is in the testers group, on an Android phone.
2. Open this link on that phone and tap "Become a tester": [opt-in URL]
3. Tap the Google Play link on that page and install MockMob.
4. Do NOT leave the test for 14 days. Leaving the test, even for a day, can stop you counting.
5. Open the app a few times a week. Sign in, take a short practice, open a result.
6. If something looks wrong, email support@mockmob.in with a screenshot.
Thank you.
```

What Play counts: the tester stays opted in for 14 consecutive days and the tester group stays at 12 or more. Uninstalling the app is not leaving the test, but engagement matters too, so ask people to keep it installed and use it. Track who joined and when in a sheet; if anyone leaves, replace them straight away from the buffer.

### 7.5 Timeline

- **Day 0:** upload the AAB, add the group, send the link. The first release goes through review (hours to a few days). Testers cannot install until the release is approved and live on the track. The 14-day clock is by tester opt-in, so get 12 opt-ins as close to the same day as possible.
- **Days 1 to 13:** watch crashes and ANRs in Play Console vitals, answer feedback, fix.
- **Day 14 or later:** when the Dashboard shows the criteria met, "Apply for production". Suggested answers are in 7.7.

### 7.6 Updates during the test

- Upload a new AAB (higher `versionCode`) to the same closed track as a new release. It goes through a short review, then rolls out to testers by normal Play auto-update. No re-opt-in, the group stays the same.
- Updating the build does not appear in Google's wording as resetting the 14 days; the requirement is about testers staying opted in [S1]. That is my reading, not a quote. To be safe, do not delete the track, do not recreate the tester list, and do not remove people from the group.
- Ship fixes freely, but keep each build to what the testers can try. Put the change in the release notes.
- A build you want in production later is promoted from the closed track (Promote release) rather than rebuilt, so what ran in the test is what ships.
- Do not skip signing or change the application id: a new id is a new app and restarts everything.

### 7.7 Draft answers for "Apply for production"

Edit to match what really happened. Keep them factual.

- About your closed test: how many testers, how recruited (classmates and students known to the owner), how long, what they were asked to do (sign in, take a practice, open a result, report problems), how feedback was collected (email, a form), the number of issues found and fixed.
- About your app: a CUET UG practice app for Class 11 and 12 and drop-year students; timed mocks, result by chapter, mistake review, short practice, weekly goal, local reminders; free, no ads, no in-app purchase; the audience is 16 and over.
- Production readiness: all App content sections complete; Data safety matches the privacy policy; account deletion in app and on the web; reviewer sign-in provided; target API 36 and 16 KB page-size checks passed (section 8); crash and ANR rates reviewed in vitals; support at `support@mockmob.in`.

---

## 8. Current Play technical rules (checked 13 Oct 2026)

| Rule | What it says | Status for `in.mockmob.app` |
|---|---|---|
| Target API level | From 31 Aug 2026 new apps and updates must target Android 16 (API 36) or higher. An extension to 1 Nov 2026 was available by request [S2] | `targetSdk = maxOf(flutter.targetSdkVersion, 36)` in `build.gradle.kts` (Flutter's own value is 36 in the installed SDK, `C:\flutter\...\FlutterExtension.kt`); `aapt2 dump badging` on the 13 Oct release APK shows `targetSdkVersion:'36'`, `compileSdkVersion='36'` |
| 16 KB page size | Apps targeting API 35 or higher must support 16 KB memory pages on 64-bit devices; from **1 Feb 2027** updates that do not will be blocked. Only apps with native code need work [S12] | The release APK has five native libraries, all with LOAD segments aligned to at least 0x4000 (libapp and libflutter 0x10000; libsqlite3, libdartjni, libdatastore_shared_counter 0x4000), and `zipalign -c -P 16 -v 4` printed "Verification successful" (SDK build-tools 37.0.0). Re-run `python -I tool/check_16kb.py <aab>` on the exact AAB you upload, as plugins or Flutter updates can change this |
| New app format | Android App Bundle (AAB) | Build with `flutter build appbundle` |
| Closed test | 12 testers, 14 consecutive days, personal accounts after 13 Nov 2023 [S1] | Section 7 |
| Account deletion | In-app path and a web link that loads without errors, names the app, and shows the request path. Disclose it in the Data safety form [S6] | In app: `delete_screen.dart`. Web: `/account-deletion`. Fix the name (section 0, item 4) |
| Generative AI | In-app report or flag for AI output [S9] | Missing for the mentor replies (section 0, item 2) |
| Payments | No steering to other payment methods [S8] | See section 0, item 1 |
| Target audience | Section 4 [S5] | |

Not checked by me: whether this app is a "large screen" app Play will rate as unoptimised; whether Play pre-launch reports raise issues. Look at the pre-launch report after the first upload.

---

## 9. Fixes before submission (not made by this task)

This task wrote documents only. The integrator or a web agent owns these edits. None of them needs a database change.

| # | Where | Change |
|---|---|---|
| F1 | `flutter_app/lib/features/you/edit_copy.dart:113` | Replace "Plans are managed on mockmob.in. Pro bought there works here." with copy that does not name a place to buy. Review the "comes with Pro" lines in `practice/copy.dart` and `insights/copy.dart` for any wording that points off-app |
| F2 | AI mentor reply bubble (`insights/widgets/ask_messages.dart`) and a server endpoint | A "Report this reply" control that sends a report without leaving the app |
| F3 | `src/app/privacy/page.js` | Remove or correct the push-token sentence for v1; say reminders are scheduled on the phone; say the AI mentor text and a compact study summary go to the model provider; list question view and answer events (seen, attempted, skip) as operational data; name the age question; keep the 180 days and 30 days statements |
| F4 | `src/app/account-deletion/page.js` | Name the app exactly as on Play ("MockMob: CUET UG Prep", `in.mockmob.app`); keep the two ways to ask, the lists of what is deleted and kept, and the 30-day statement |
| F5 | `lib/features/you/copy.dart` (`operationalNote`) | Name question views in the list of data the usage-data switch does not cover, or gate the explore-stream logging on consent |
| F6 | `flutter_app/docs/RELEASE.md` (the build and signing agent) | Confirm the build command, `prod.json` contents and key steps the checklist in section 10 refers to |

---

## 10. Owner action checklist, in order

Do these in this order. Steps marked (owner) use secrets or accounts only you hold. Do not paste keystore passwords, `key.properties` or service keys into chat or into the repo.

1. (owner) Open Play Console and the new app's Dashboard. Note whether "Apply for production" is already available (section 7.1). This decides if the 14 days apply.
2. (owner) Create the app: name `MockMob: CUET UG Prep`, default language English (India), App, Free, accept the declarations. Complete Account details (developer name, contact email, phone, trader status if asked).
3. (owner) Run `powershell -ExecutionPolicy Bypass -File tool\make_upload_key.ps1` from `flutter_app`. Back the keystore up in two places. Never send it to anyone.
4. (owner) Create `flutter_app/dart_defines/prod.json` with the production Supabase URL and anon key, `API_BASE_URL=https://www.mockmob.in` and, once set up, `GOOGLE_WEB_CLIENT_ID` (see `dart_defines/README.md`, `docs/AUTH.md`). Public values only. Add the Supabase redirect `in.mockmob.app://login-callback` for Google (AUTH.md step S1).
5. Have the integrator land fixes F1 to F6, then build: `flutter build appbundle --release --dart-define-from-file=dart_defines/prod.json --build-number N`, run `python -I tool/check_16kb.py` on the AAB, and run `aapt2 dump badging` on the matching APK to confirm permissions and target 36.
6. (owner) Create the reviewer account on production (section 5).
7. (owner) Fill App content: privacy policy URL, Ads, App access (section 5 text), Content rating (section 3), Target audience (section 4), Data safety (section 2), Government apps, Financial features, News, Health, Advertising ID (section 6).
8. (owner) Fill the Store listing: name, short and full description (section 1), icon, feature graphic, 8 phone screenshots. Category Education, contact email, website.
9. (owner) Create the Google Group and add 20 to 25 testers (section 7.3). Create the closed track, add the group, set the feedback email, India only, upload the AAB, send for review.
10. (owner) Once the first upload exists, open Play Console, Setup, App signing (App integrity), copy the **SHA-256** and **SHA-1** of the app signing certificate. Put the SHA-256 into the server environment variable `ANDROID_CERT_SHA256` on Vercel so App Links verify (`src/app/api/assetlinks/route.js`), and add the SHA-1 to the Android OAuth client in Google Cloud if you use the one-tap Google sheet. Builds installed from Play are signed with this key, not your upload key, so Google sign-in and App Links will not work for testers until this is done. Google sign-in through the browser works without it.
11. When the release is live on the track, send the opt-in link and the tester message (section 7.4). Record who joined and when.
12. Days 1 to 13: watch vitals and feedback, ship fixes as new releases on the same track (section 7.6).
13. Day 14 or later: check the Dashboard shows the criteria met, then "Apply for production" with the answers in 7.7.
14. After approval: promote the tested build to Production (India), rotate the reviewer password, and add other countries only after the trader and legal checks.

---

## Sources

- [S1] Play Console Help, "Testing requirements for new personal developer accounts": https://support.google.com/googleplay/android-developer/answer/14151465 (read 13 Oct 2026)
- [S2] Android Developers, "Target API level requirements for Google Play apps": https://developer.android.com/google/play/requirements/target-sdk (page updated 1 Oct 2026)
- [S3] Play Console Help, "Add preview assets to showcase your app": https://support.google.com/googleplay/android-developer/answer/9866151
- [S4] Play Console Help, "Provide information for Google Play's Data safety section": https://support.google.com/googleplay/android-developer/answer/10787469
- [S5] Play Console Help, "Target Audience and App Content settings": https://support.google.com/googleplay/android-developer/answer/9867159
- [S6] Play Console Help, "Understand Google Play's app account deletion requirements": https://support.google.com/googleplay/android-developer/answer/13327111
- [S7] Play Console Help, "Content ratings": https://support.google.com/googleplay/android-developer/answer/9859655
- [S8] Play Console Help, "Payments policy": https://support.google.com/googleplay/android-developer/answer/9858738
- [S9] Play Console Help, "AI-Generated Content policy": https://support.google.com/googleplay/android-developer/answer/13985936 (requirement read through search summaries of this page; open the page to confirm current wording)
- [S10] Play Console Help, "Provide information for App content" (Sign-in details section): https://support.google.com/googleplay/android-developer/answer/9859455
- [S11] Third-party guides on the 12-tester rule, used only for the advice to recruit a buffer (not Google's text): https://levelup.gitconnected.com/the-12-tester-tax-google-plays-closed-testing-rule-is-quietly-killing-solo-devs-2cea83c2e338
- [S12] Android Developers, "Support 16 KB page sizes": https://developer.android.com/guide/practices/page-sizes
