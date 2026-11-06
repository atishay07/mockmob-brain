# MockMob app onboarding: research and proposed structure

Date: 13 October 2026. Scope: structure and content of first-run onboarding for the Flutter app. Visual treatment (glass, motion, imagery, brand) is a separate pass and is not decided here. Nothing in this file has been built.

Companion files in this folder: `owner-materials.md` (what the owner has already told us, and the screen-by-screen gap analysis) and `flutter-feasibility.md`. This file does not repeat them.

## 0. How to read this

Evidence tags used throughout:

- [O] read first-hand in this session from a primary page: a live Play Store listing, official Google or government documentation, or MockMob's own repo and data.
- [R] read from a third-party screen-recording index (Page Flows, ScreensDesign, Lazyweb). Timestamps are the index's. These show one recording of one build; apps A/B test, and some recordings are old.
- [S] a secondary write-up, blog or news summary.
- [V] a vendor or company-reported statistic. Directional only.
- [I] my inference. Treated as a proposal, not a finding.

Numbers in square brackets such as [12] point to the source list in section 10.

Limits of this research, stated up front:

1. I could not install or screen-record any app. For Duolingo, Speak, Brilliant, Headway, Finch, Opal, Revolut, CRED and Snapchat the screen order comes from recordings made by others. The Revolut recording appears to be about six years old [11], so treat it as a pattern, not the current flow.
2. For Physics Wallah, Unacademy, Testbook, Embibe and Adda247, public pages do not document their in-app first-run screens. What is verified is listed in section 3.2. A hands-on walkthrough on the owner's phone is the way to close that gap (checklist in section 9, decision D8).
3. Fampay/FamApp: public sources describe the parent and teen flow, the card and later personalisation, but no screen-level onboarding data [13].
4. high.live: the page exposes one line only (a one-word headline, "Get in early", "Trade the culture"). `owner-materials.md` records that the site is canvas-rendered and its HTML shows nothing. I could not study its onboarding, and it is a visual reference rather than an onboarding one.
5. Legal material (Play policy, DPDP) is summarised for design purposes. It is not legal advice. DPDP in particular needs counsel before May 2027; the existing brain already says so (`DECISION-2026-10-03-DIFFERENTIATOR.md`, backlog item 7).

## 1. The owner's feedback, translated into structural requirements

| Owner said (13 Oct) | What the current flow does | Structural consequence |
| --- | --- | --- |
| The five-question approach is "not even scalable" and is what "the website requires", not the app [O13] | Welcome, subject, five bundled questions that are "the same for every paper", a result that says it cannot say where you stand, then sign-in, then age and usage consent [O, `copy.dart`, `APP-DESIGN-SPEC.md` 5.1] | My reading [I], to confirm in D1: the no-account sample is a web device for a visitor who has not committed. An app user has already installed. App onboarding should do what installed-app onboarding does in the best apps: goal and identity first, a personal reveal every two or three screens, a commitment, then save. The sample stays on the website. Five hand-authored questions cannot scale by subject, exam or year; the new flow must scale by data (course list, subject registry, DU index, question bank), not by hand-built screens. |
| "Really weak", "rudimentary", "not even close to a polished app" | The only personal input is a subject. The only payoff is a score out of five | Ask 6 to 8 things that each change something visible, and return a personal result after about every second or third answer. |
| Defensive bottom taglines are "obvious" | Non-affiliation footer on Welcome; "not a diagnosis" caption and footer on every sample question; "Sample, not a diagnosis" and "Example, not your plan yet" on the result; "This only decides your data settings" under the age question [O, `copy.dart`] | Delete them from the flow. Section 6.1 shows Google Play does not require them in the app. Where the non-affiliation statement must live is in section 6. |
| "If you had gone through the research I gave you" | Plan 3.4 followed the Undertone lesson (try the core idea in onboarding) literally, as five questions | Keep the lesson, change the carrier: one real question in the flow, then the real 10-question starting-point check as the first move. See step 8 and step 14. |
| Excitement, premium, Gen Z (Revolut, Fampay, high.live) | No brand moment, no aspiration, no identity | The aspiration here is a seat in a specific college. The product already holds real data for it (section 4). That is the exciting, specific thing a generic CUET app cannot offer. |

## 2. What the best apps do (evidence)

### 2.1 App by app

| App | What it asks, in order | Immediate payoff | Progress and commitment | Permission | Account | Speed | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Duolingo | Reason, goal (daily time), notification permission, path choice, first quiz question at about 0:49, lesson complete, streak, then account creation (profile, age, name, email, password) at about 2:46 to 3:10 [1] | A real question inside a minute; a streak starts before any form. A banner promises "7 quick questions" before the first lesson [2] | Progress bar on question screens [2]. Daily goal chosen at start; streak system backed by published tests (streak wager: Day 7 retention +14%; weekend amulet: +4% return) [3] | After goal, framed as reminders to meet the goal [1][S] | After the first lesson and streak. A reported A/B test of delaying sign-up gave about +20% daily active users [V, 4: not verified against a primary source] | Account at about 3 minutes; first interactive item inside a minute | [R] order; [O] blog tests; [V] 20% |
| Speak | Conversational set-up with an AI tutor (about 14 steps): native language, learning questions; summary cards show how answers shape the curriculum (about 1:43); a "preparing your curriculum" state; paywall (about 1:57 to 2:15) [5] | A visible link from each answer to the curriculum | 14 steps, conversational so it reads as a first lesson, not a form | Not described | Email sign-up exists; paywall follows the quiz | Under 3 minutes in the recording | [R] |
| Brilliant | Level check using real maths problems (about 0:30), a detailed quiz, account creation (a sign-up wall before the paywall), single annual plan with 7-day trial (about 1:04), then a personalised starting path (about 1:41) [6] | A recommended path that reflects answers | 12 steps | Not described | Before the paywall; Google, Apple or email [6] | About 1:45 in the recording | [R] |
| Headway | Quiz on goals, gender, age, focus areas, reading habits (1:08 to 2:45), "crafting your plan" screens, a "commitment pact" (2:49), soft paywall with trial (3:10) [7]. Questions alternate with reassurance and press or testimonial beats [7][S] | Plan framing and reassurance between questions | Commitment pact before any price | Not described | After the paywall | About 3 minutes | [R] and [S] |
| Finch | Hatch an egg, pick and name the pet and a trait (the pet reacts), a value line ("looking after yourself looks after your pet"), a quiz of large tappable cards (1:36 to 2:24), soft paywall with a trial timeline (2:35) [8]. A phone sign-up step offers Skip [8] | Attachment to a character before anything is asked | 18 to 36 steps depending on the index; one critique says too many customisation choices arrive at once [8][S] | Present in the flow; position not captured | Phone with Skip | Long | [R] and [S] |
| Opal | Activity-permission prompt, welcome, name, sign-in choice, priorities (focus, sleep, presence, mental health), 21 steps in the index [9]. A July 2026 episode describes a rebuild as a chat thread, with a three-beat reveal (about 91 days a year on the phone, then about 18 years of life, then "the rescue"), and a paywall that refers back to the chosen goal [9][S] | A personal number derived from the user's own answers | Chat format; the goal is echoed later | Early | Sign-in choice is asked as a chat question | Not captured | [R] and [S: episode notes only] |
| Revolut (recording about six years old) | Intro slides, phone, code, Face ID, country, address, name, date of birth, email, select goal (2:05), notification permission (2:11), add money, verify identity with ID and selfie, top up, select card, virtual card created (3:46), Apple Pay, home (3:54) [11] | A usable first card at the end | One action per screen, explicit status messages while verifying [11][S] | After goal, before the ID step | First, because it is a regulated product | About 3:54 including identity checks | [R] and [S] |
| CRED | Splash, phone (0:10), code (0:17), name (0:22), email (0:32), processing (0:47 to 0:59), notification permission (0:59), home (1:06) [10] | Entry itself is the status signal; a teardown argues the reward value only becomes clear late and that three trust-heavy asks come first [10][S] | None visible | Last | First | About 1:06 | [R] and [S] |
| Snapchat (Android) | Sign up, name, birthday (0:09), username, password, code (0:22), add and invite friends (0:31 to 0:35), create avatar (0:39 to 0:56) with photo permissions, home (1:01) [12] | An avatar made by the user | None | During avatar and friends | First | About 1 minute | [R] |
| FamApp / Fampay | Parent-first (parent KYC, then invites the teen) or teen-initiated with parental consent; teen KYC and parent KYC are separate [13][S]. Numberless card kept in the app; later a customisation space for QR theme, payment sounds, scanner, home page and app icon, with "more to brag about" copy [13][O, Play listing] | A card of your own; an app that can be made "yours" | Not documented | Not documented | Phone-based KYC | Not documented | [S] and [O] |

### 2.2 Patterns that recur, and what each means for MockMob

P1. Value or investment before the account. Learning apps (Duolingo, Speak, Brilliant, Headway) put a quiz, a plan or a first question before the account or paywall. Regulated or social products (Revolut, CRED, Snapchat) ask first because they must. MockMob is a learning product: the account comes after the plan reveal (step 12), not before.

P2. The goal question goes first. In a Lazyweb review of quiz-style onboarding, about one in five apps (24 of 119) ask a goal or objective question, and the review says it usually opens the quiz [15][R]. For MockMob the "goal" is concrete: a course and up to three colleges (steps 3 and 4).

P3. Every answer must visibly change something. The ScreensDesign guidance is explicit: ask only questions that change content, defaults or the starting path, say why, and then show how the answers shaped the setup [14]. The test used in section 4 is "can I say what changes on screen after this answer". Several apps fail it in public critiques; a goal captured and then ignored adds friction [14][15].

P4. Visible personalisation with an edit path. Plan or summary cards that reflect answers and let the user correct them (Speak, and Welling in the 2026 trends review) are the climax of the quiz [5][14]. MockMob has the data to make this concrete (section 4).

P5. Commitment devices before the ask. Duolingo's daily goal and streak; Headway's pact [3][7]. Two bodies of research support the mechanisms: implementation intentions (choosing when and where) have an average effect of about d = 0.65 across a 2006 meta-analysis [18][S]; the endowed-progress effect (a card with two of ten stamps already filled was finished by 34 percent of customers against 19 percent for a blank card) [18][S]. Both are secondary summaries; they support the design direction, not a forecast. Caution from MockMob's own rules: no punitive streaks, bounded weekly goals with rest days (`PLAN-2026-10-12`, rule 7). So the commitment is a weekly rhythm and a "when", never a daily chain.

P6. Prime permissions with the exact benefit, and ask once. The ScreensDesign guidance says to ask right before the feature needs it, preview the concrete moments, and keep the app useful if the user declines [14]. Examples in the 2026 review: a sample exam reminder with Skip or Remind me, and a pick-a-time step before the notification prompt [14]. Android 13 and later made notification permission a runtime prompt; vendor studies report opt-in falling from roughly 85 to 90 percent before Android 13 to somewhere between 56 and 75 percent depending on the vendor and category, with finance least affected [17][V]. No controlled study of primers was found, so the benefit of priming is [I]. An anti-pattern in the same review set: two permission prompts straight after a mandatory sign-up with no warm-up [14].

P7. Identity objects create attachment. Finch (pet), Snapchat (avatar), FamApp (card and personalisation space), Duolingo (character) all give the user something of their own early [1][8][12][13]. MockMob has Mobi. The risk named in a Finch critique is offering many customisations at once [8].

P8. Aspiration with a number the user cannot fake. Opal's years figure, CRED's membership gate, Revolut's first card, FamApp's "brag" framing [9][10][11][13]. MockMob's version is a college and the real cutoffs it had last year (section 4), plus a countdown.

P9. Fast means few blocking inputs, not few screens. Recorded flows run from about 1 minute (Snapchat sign-up, CRED) to about 4 minutes (Revolut with identity checks) [10][11][12]. ScreensDesign's own range is 10 to 51 screens and it says there is no universal number: use the fewest steps that resolve uncertainty blocking first value, count every tap from launch to first value, and remove steps that do not change the product [14]. Two further rules from that guidance: use step counts for fixed sequences or section labels for grouped questions, and never let progress stall, jump or hit 100 percent early [14].

P10. Paywall after the personalised reveal is the dominant subscription-app pattern, but it does not apply to MockMob. A Lazyweb study of 40 flows with paywalls reports most place the paywall late, after preferences and personalisation [15][S]. MockMob sells Pro only on the web (Rs 99 a month) and the app has no purchase flow (`PLAN-2026-10-12`, section 2.1), so onboarding has no paywall step. Industry data also suggests education is slow to convert: one benchmark reports 23.5 percent of education-app trials start 31 or more days after install, the highest late-start share in its dataset [16][V]. That supports not forcing a monetisation moment into first run.

P11. Social proof inside quizzes (press, testimonials, ratings) is common in Headway and Speak [5][7]. It is excluded for MockMob: the owner's rules forbid testimonials, headcounts and invented numbers. Real data beats are the substitute (section 4 and the copy directions).

P12. Conversational presentation. Speak (AI tutor) and Opal (chat thread) make question-and-answer feel like a first interaction, not a form [5][9]. This is a presentation option for the design pass: Mobi asks, the user taps replies. It does not change the structure below.

### 2.3 How account creation is done in India

- Verified: Adda247's own guide lists category, exam, language, then email or mobile sign-in with a one-time code, then notifications, then autostart [20]. Physics Wallah login/register is mobile number plus OTP (SMS, with WhatsApp OTP shown on a scraped copy) [20][S]. CRED is phone plus OTP [10]. Unacademy login is OTP-based [20][S].
- Vendor and Google case studies on conversion are directional only: a Google case study reports about 30 percent more sign-ups on mobile after adding Sign in with Google for a news publisher; one-tap phone login vendors report +8 percent (Meesho) and about 10 percent OTP-failure drop-off (Astrotalk) [21][V].
- Platform facts: Android's Credential Manager is the supported route for the Google sign-in bottom sheet, with the older One Tap client deprecated; SMS Retriever and the SMS User Consent API let an app read an OTP without the SMS permission [21][O].
- MockMob today: Google (pending OAuth set-up) and a no-password email code. Recommendation [I]: keep exactly those two, because every Android user has a Google account, Google fills the name, and an email code needs no SMS cost. Test a phone or WhatsApp OTP only if sign-up drop-off shows it is needed (D4).

## 3. Indian test-prep apps students already use

### 3.1 What a CUET aspirant sees today (Play Store audit, 13 October 2026) [19][O]

I fetched the live Play listings for the apps below and read the full descriptions.

| App (Play ID) | What the listing sells | Where the non-affiliation text sits |
| --- | --- | --- |
| Physics Wallah (`xyz.penpencil.physicswala`) | Live and recorded batches, tests, notes for JEE, NEET, NDA, boards 8 to 12 | A "Disclaimer" paragraph after the social links at the end of the full description: independent platform, not affiliated with or endorsed by any government body or exam authority, and no official services such as registration or admit cards |
| Testbook (`com.testbook.tbapp`) | One pass for mocks, PYQs, notes across government and competitive exams | One short line under "Support & Disclaimer" near the end, with a source link |
| Testbook CUET (`com.testbook.tbapp.cuet`) | Notes, PYQs, mocks, live classes; the listing is still titled for CUET 2022 | One line at the end plus the official source URL |
| Adda247 (`com.adda247.app`) | Government-job prep | A warning-sign "DISCLAIMER" block near the end, with a list of official source sites |
| CUET 2027 Exam Preparation (`cuet.com`) | Syllabus, PYQs, mock with All India Rank, notes, chapter MCQs | Bold disclaimer at the very top, naming NTA, any university or exam body, plus the NTA URL |
| EduRev CUET (`com.edurev.cuet`) | Notes, videos, mocks, test series | A line near the end with the NTA CUET page |
| CUETMOCK (`com.cuetmock`) | Subject and chapter tests, performance score, chapter suggestions | A line at the end |
| Achieve CUET (`com.cuet_achieve`) | 27K+ MCQs, daily free mocks, personalised chapter mocks, revision modes | A full paragraph in the description plus official resource links |
| Hitbullseye CUET (`com.cuet_bullseye`) | Stream-wise mocks, AI-based test analysis, national ranking | One line at the very end: not a government entity and does not provide government services |
| DUBuddy (`in.cyberflow.dubuddy`) | CUET PYQs and mocks | An "independent app" note in the opening paragraphs; information sourced from public material |

Install counts could not be extracted reliably from the page HTML, so none are quoted. The short description (the line under the app name) of all ten listings is a feature or benefit line; none carries a disclaimer.

What this tells us [I from the audit]:

1. Every CUET competitor I read is a catalogue: syllabus, PYQs, mocks, notes, rank. None advertises a plan built from the student's target college and course. That is the gap the onboarding in this file is built to exploit.
2. The non-affiliation text lives in the store listing description, nearly always near the end. Nothing in the listings suggests an in-app banner is needed to be competitive or compliant.
3. Hitbullseye advertises AI-based test analysis and Achieve personalised chapter mocks and revision modes; Embibe's App Store listing says it starts with exam selection, then a diagnostic test to find the level, then a personalised improvement plan, with a 7-day trial [20][O]. So a diagnostic-then-plan is already a known pattern in India. MockMob's difference has to be the honest evidence loop (find, repair, check) and the DU-specific data.
4. The official NTA Abhyas app is free and offers subject-wise mocks for all CUET subjects [S, search summary]; MockMob cannot win on "free mocks".

### 3.2 What is and is not verified about their first run

| App | Verified | Not verified |
| --- | --- | --- |
| Adda247 | Order from its own guide: category, exam, language (Hindi or English at registration, changeable later), email or mobile plus OTP, allow notifications, autostart [20] | Number of screens, visuals, whether a plan or diagnostic appears |
| Unacademy | Goal taxonomy page lists Class 6 to 12 by board, exams, and, under "Others", CUET UG (Domain) and CUET (Language and General Test) as separate goals [20][O]; OTP login [S] | Screen order and personalisation after the goal |
| Physics Wallah | Mobile number plus OTP for login or register [S]; Play listing audited above | Class, exam and language pickers, if any |
| Testbook | Exam category, language setting and a plan choice (Pass versus SuperCoaching) on a PC build described by a download site [S, low reliability] | Mobile flow |
| Embibe | Exam pick, then a simple diagnostic to find the level, then personalised plans, 7-day trial; no CUET in its App Store description [20][O] | Screens |

Takeaways [I]: Indian test-prep onboarding is exam-and-language selection plus phone OTP, then a catalogue. The consumer-app pattern of goal, personal reveal and commitment is largely absent. Phone OTP is the local norm, but a Class 12 student with an Android phone always has a Google account.

## 4. CUET UG 2027 personalisation: what MockMob can genuinely use

Facts that shape the questions:

- Dates are not announced. Expected window May to June 2027 (registration expected January to March 2027) [22][S]. MockMob's own `/cuet-2027` page already labels dates "expected". Do not ask the student for an exam date; show a derived countdown labelled expected, and update it when NTA publishes.
- The 2027 pattern is not settled. A draft reported by coaching and news sites would cut subjects from five to four, shorten papers (35 to 40 questions, 40 to 45 minutes) and hold all papers in one day. A decision was reported as due around 20 October 2026. Nothing is confirmed [22][S]. Do not hard-code "5 subjects" in copy; the API's client-side maximum is 5 for now.
- Syllabus for 2027 is reported expected late December 2026 [22][S].
- DU data already in the repo [23][O]: 73 programme groups in the 2026 index, 67 colleges, 1,393 college-programme offerings, three allocation rounds. Commerce and Economics groups: B.Com (Hons) in 55 colleges, B.Com in 44, B.A. (Hons) Economics in 40, B.A. (Hons) Business Economics in 10, BMS in 9, BBA (FIA) in 2. Eligibility for B.Com (Hons) in the 2026-27 Bulletin: one language plus Mathematics or Accountancy plus any two subjects from List B. Round I 2026 minimum allocation scores for the UR category in B.Com (Hons) start at 924.3 (SRCC), 919.9 (Hindu), 912.5 (LSR), 907.5 (Hansraj), 903.7 (Kirori Mal), 895.6 (Ramjas), 891.5 (Sri Venkateswara). St. Stephen's appears in this data for B.A. (Hons) Economics (891.97 Round I, UR) but not B.Com. Cutoffs describe 2026 and say nothing about 2027 (the existing Compass copy already says so). State the scale exactly as the web calculator does.
- Subjects: launch practice is English, Accountancy, Business Studies, Economics (`LAUNCH_SUBJECT_IDS`); 15 subjects are marked "supported" in the API; a free baseline (10 questions) and free full sample exist for the four launch subjects, and one free 10-question daily practice [23][O].
- Existing server levers that an answer can write to today: subjects (temporary `PATCH /api/users/{id}`), practice minutes 10, 20 or 30 (`/api/study/preferences`, `/api/learning/plan`), study days per week 1 to 7 (`/api/me/goal`), study window and quiet hours (`/api/me/notification-prefs`), age band (`/api/me/consent`). Anything else needs a new allowlisted profile endpoint [23][O].

Question audit. Verdict key: USE (feeds something real now), USE IF MAPPED (decorative unless the mapping is built), DEFER, SKIP.

| Candidate question | Real use | Verdict |
| --- | --- | --- |
| Where are you: Class 12 now, passed Class 12 (gap year), Class 11, not sure | Weeks to the expected window, plan length and weekly load. Class 11 gets an early-access path instead of a plan | USE (one tap) |
| Stream | Launch is Commerce. Assume Commerce; offer "Not commerce?" to capture interest and tell the student when it opens. Do not make every user answer | USE as an exit, not a step |
| Dream course (B.Com Hons, B.A. Hons Economics, B.Com, BMS, BBA FIA, other, not sure) | Drives eligibility (which subjects keep the door open) and the subject set; reuses the existing eligibility evaluator | USE |
| Dream colleges (up to three; list filtered to colleges offering the chosen course) | Gives the cutoff reference and the aspiration frame; reuses DU index | USE (optional, skippable) |
| Subjects: language, domain subjects, General Test | Practice availability, first move, plan ordering. Mark which are "practice ready" today | USE |
| Exam date | Single national window; student cannot change it | SKIP (derive and show) |
| Confidence per subject (Shaky, Okay, Strong) | Orders the plan; later "your gut versus your first check" comparison is a strong reveal. Decorative if that comparison is never built | USE IF MAPPED |
| Minutes per session (10, 20, 30), days per week, best time | Directly maps to plan minutes, weekly goal and study window | USE |
| Biggest worry (silly mistakes, running out of time, not knowing where to start, too much syllabus, forgetting what I studied, English or General Test) | Picks the first move: mistakes goes to repair; time goes to timed quick sets; start goes to the starting-point check; syllabus goes to chapter priorities (`cuet_chapter_priorities.json`); forgetting goes to recall cards. Decorative without that mapping | USE IF MAPPED |
| Prep status (not started, partly through, revising, in mock stage) | Starting mode. Mostly inferable from year and confidence | DEFER |
| Board (CBSE, ISC, State) and board exam dates | Boards fall before CUET and could shape February to March load. Nothing in the product uses it yet | DEFER (decorative today) |
| UI language (English or Hindi) | PW and Adda247 ask because their content is multilingual. MockMob content is English | DEFER until there is Hindi content |
| Reservation category (UR, OBC-NCL, EWS, SC, ST and others) | Needed only to show category-specific cutoffs. Sensitive | DEFER to an optional filter on the Compass screen, stored on device |
| Name | Mobi addresses the student by name. Google supplies it; otherwise one field | USE |
| Age: 18 or older | Required for data handling (section 6.2) | REQUIRED |
| City, state, school, gender, phone number, parents' details | No product use; data minimisation | SKIP |
| Coaching yes or no | Useful to the business for positioning, not to the student | SKIP in onboarding (survey later) |
| How did you hear about MockMob | Obtainable from the Play Install Referrer with no friction | SKIP |
| Contacts, friends | No social features shipped; contact permission is a trust and DPDP cost | SKIP |

## 5. Proposed onboarding: 14 steps

Principles for this flow, from sections 2 to 4:

1. Goal first, then facts, then calibration, then commitment, then save. Every step returns something visible.
2. Local until step 12. Nothing leaves the device before the account. The age check (step 11) comes before the account because the account is the first act of collecting a person's data.
3. Taps and chips, not typing. The only keyboard use is the email code, if chosen.
4. Honest time budget (a target to measure, not a promise): first real data reveal under 40 seconds, plan reveal under 2 minutes, finished with account and reminders in about 2.5 minutes. Every step from 3 to 10 has Skip, which falls back to defaults. Only step 12 is a commitment, and it also has "Not now".
5. Progress is real. A four-part segmented bar (Aim, Subjects, Rhythm, Save) that fills by actual step. No fake percentages. The reveal in step 10 is computed instantly; stage it visually in about a second, but do not show a fake "calculating" screen, because MockMob's rule is to show processing stages only when real.
6. Data-driven, not hand-built (the scalability answer). Each step is a row in a versioned step deck with: id, type (single, multi, chips, rhythm, reveal, permission, account), copy keys, branching rule, the field it writes, and a required one-line "what visibly changes" (a test fails if that line is empty). Courses, colleges and subjects come from the DU index and subject registry. New exams or subjects change data, not screens. The same deck can drive a web version and seed the app from a website deep link (fast lane below).
7. Presentation is open. The structure works as a Mobi-led chat with tappable replies or as full screens. That is a design decision.

At a glance:

| # | Step | Phase | Reveal or payoff | Needs account or server |
| --- | --- | --- | --- | --- |
| 1 | Welcome | Aim | Mobi plus one real fact | No |
| 2 | Where you are in the journey | Aim | Countdown to the expected window | No |
| 3 | Dream course | Aim | Colleges-per-course counts | No |
| 4 | Dream colleges | Aim | Dream-list card | No |
| 5 | What it takes | Aim | Subject rule and 2026 cutoff for the top pick | No |
| 6 | Subjects and how solid each feels | Subjects | Live reorder, first move previewed | No |
| 7 | Biggest worry | Subjects | First move changes | No |
| 8 | One real question | Subjects | Explanation and the ten-second fix | No |
| 9 | Rhythm | Rhythm | Sessions before the window, from their own choices | No |
| 10 | Your starter plan | Rhythm | The personalised reveal and the pact | No |
| 11 | Age check | Save | What changes for them, in one line | No (held on device) |
| 12 | Save your plan | Save | Plan follows them across devices | Yes |
| 13 | Reminders | Save | Preview of their own notification | Yes (device token) |
| 14 | First move | Save | The starting-point check, now or tonight | Yes (quote and scoring) |

### Step 1. Welcome

- Purpose: the promise and the first identity beat. One line, one action.
- Input: none. Buttons: "Get started"; "I already have an account".
- Payoff: Mobi's entrance and a real fact on screen from the data (for example the number of DU colleges that took B.Com (Hons) through CUET in 2026).
- Data use: none stored.
- States: offline works. If returning with a saved draft: "Pick up where you left off" resumes at the last step.

### Step 2. Where are you in the journey

- Purpose: set the timeline without asking for a date.
- Input: one tap. Class 12 now; Passed Class 12; Class 11; Not sure.
- Payoff: a countdown to the expected May 2027 window, in weeks, computed from the device date and labelled expected. It animates in.
- Data use: year and attempt stage select the plan length and weekly load. Class 11 routes to an early-access card instead of the plan. Stored as an enum on the profile after step 12.
- States: if the device date is wrong or after the window, show no countdown and say the dates are not out yet.

### Step 3. Dream course

- Purpose: capture the goal first (pattern P2).
- Input: chips from the DU index's Commerce and Economics programmes: B.Com (Hons), B.A. (Hons) Economics, B.Com, BMS, BBA (FIA), B.A. (Hons) Business Economics; plus "Another course or university" and "Not sure yet". Multi-select up to 3. "Not commerce?" sits as a quiet exit.
- Payoff: each chip shows how many colleges offered it through CUET in 2026 (real counts from the index).
- Data use: course ids feed the eligibility evaluator and the subject suggestion in step 5. "Another course" and "Not commerce" record an interest enum only.
- States: "Not sure yet" skips steps 4 and 5 and goes to step 6 with common Commerce subjects pre-ticked.

### Step 4. Dream colleges

- Purpose: aspiration and a reference point.
- Input: pick up to three from the colleges that offered the chosen course. Search by name. "Open to any" is allowed.
- Payoff: the chosen names appear on a "dream list" card that will persist on Today (plain typographic names, no crests or logos).
- Data use: college ids feed the cutoff reference in step 5 and the dream-list card. No cutoffs are shown here.
- States: if the DU data cannot load, skip to step 6. Names and data come from the published 2026 index (about 160 KB index plus 529 KB of offering files uncompressed), bundled or fetched once.

### Step 5. What it takes (first reveal)

- Purpose: the first personal, real payoff, well inside the first minute.
- Input: none. One button: "Build my subject set".
- Payoff: for the top pick, three facts: the subject rule the Bulletin sets (for example, one language plus Mathematics or Accountancy plus any two from List B for B.Com (Hons)), the 2026 first-list cutoff at that college in DU's own scale, and which of the student's likely subjects keep every dream-list course open. Uses the existing combination planner logic, which only checks eligibility and never claims chances.
- Data use: pre-selects step 6's subject set. Nothing stored beyond that.
- Copy rule: no "your chances" language and no promises. 2026 numbers are shown as last year's, in the same wording the web calculator uses.

### Step 6. Subjects, and how solid each feels

- Purpose: confirm what to practise and calibrate honestly.
- Input: a list pre-ticked from step 5. Each ticked subject has a three-state control: Shaky, Okay, Strong. "Practice ready" is marked on English, Accountancy, Business Studies, Economics (and any others the API reports as supported); subjects not yet available are shown honestly with "we will tell you when it opens". Soft cap from the API (currently 5); copy never states the 2027 cap.
- Payoff: the list reorders live, weakest first. A one-line preview of the first move appears ("Starting with Accountancy").
- Data use: subjects write to the profile (`subjects`). Confidence labels are stored as an enum per subject and are used to order the plan and, after the first check, for a "your gut versus the evidence" comparison. If that comparison is not built, drop the confidence control; it would be decorative.
- States: no subject selected is allowed only if "Not sure yet" was chosen; otherwise Continue is disabled with a reason.

### Step 7. Biggest worry

- Purpose: choose the first move and the tone of the plan.
- Input: single choice (optionally two): silly mistakes; running out of time; not knowing where to start; too much syllabus; forgetting what I studied; English or General Test.
- Payoff: Mobi reflects it back in one specific line, and the first-move preview changes.
- Data use: enum only. Maps to: silly mistakes goes to repair-first; running out of time goes to timed quick practice; not knowing where to start goes to the starting-point check; too much syllabus goes to chapter priorities; forgetting goes to recall cards. Without this mapping the question is decorative and should not ship.

### Step 8. One real question (the core loop in miniature)

- Purpose: let the student taste the core idea, and prove the explanations are good, inside the flow (the Undertone lesson, at a scale that fits an installed app).
- Input: one multiple-choice question in the weakest chosen subject, drawn from a small versioned warm-up pool per subject, bundled with the app (not the five fixed questions; pool size grows with content, not code). Skip available.
- Payoff: right: one line, and the next beat. Wrong: Mobi shows the specific trap and a ten-second fix, which previews the repair loop. No celebration for a wrong answer; no score.
- Data use: not stored beyond the device. It does not feed the plan; it is not a diagnosis, and it does not need to say so. The honest, scored measure is the starting-point check in step 14, which needs the account and the server's scoring.
- States: if no pool exists for the subject, skip this step. Warm-up questions must come from the approved bank, so no paid generation is needed.

### Step 9. Rhythm

- Purpose: commitment that is chosen, bounded and personal.
- Input: one screen with three compact controls: minutes per session (10, 20, 30); days per week (1 to 7, default 4); best time (evening chips, plus a custom window). Rest days are part of the plan.
- Payoff: live arithmetic from the countdown, labelled "if you keep this rhythm": sessions before the expected window. It is plain multiplication of the user's own choices and the weeks left, not a prediction.
- Data use: minutes go to the plan query and study preferences; days per week to `PUT /api/me/goal`; the window to `PUT /api/me/notification-prefs`. Default quiet hours stay 11 PM to 7 AM.
- Evidence for asking "when" as well as "how much": implementation intentions [18][S].

### Step 10. Your starter plan (the climax)

- Purpose: the personalised reveal, and the moment of commitment (patterns P4 and P5).
- Input: one primary action: "Lock it in" as a press-and-hold gesture with Mobi (the Headway pact idea, without loss framing). A secondary "Change something" opens the earlier step.
- Payoff: three staged cards: the first move ("Starting-point check, 10 questions, Accountancy, about 10 minutes"), the weekly rhythm, the dream list with the one subject combination that keeps every target open. The plan states its basis in the title ("Built from what you told us. It sharpens after your first check."), which is a statement of what the plan is, not a disclaimer.
- Data use: compiles the local answers into a draft profile. Nothing is sent yet.
- States: plan computed instantly; no fake loading. The pact is optional (a normal button works for TalkBack and reduced motion).

### Step 11. Age check

- Purpose: set the data rules before any account exists.
- Input: "Are you 18 or older?" Yes, No, Prefer not to say. One tap. A short reason line, for example "Under 18 is fine. We keep usage tracking off for you." The API behaviour behind it already exists: minor or unknown means analytics stay off.
- Payoff: immediate and plain: what changes for them.
- Data use: age band held on device until step 12, then `PUT /api/me/consent {ageBand, analyticsAllowed:false}`. "Prefer not to say" is treated like a minor. See section 6.2 for the DPDP consequences and the parent-approval step that may need to follow.
- Note: this moves the age question ahead of sign-in; the current design asks it after sign-in because the write needs an account. The answer is simply held locally.

### Step 12. Save your plan (account)

- Purpose: ask for the account only when there is something worth keeping (pattern P1, and the ScreensDesign "account timing" rule [14]).
- Input: "Continue with Google" (Android Credential Manager bottom sheet), "Use an email code", "Not now". No password.
- Payoff: the reason is concrete and short ("So your plan follows you to the website and your next phone"). On success the answers are written.
- Data use: after sign-in the client writes subjects, goal, notification prefs and consent, plus the new allowlisted profile fields (year, courses, colleges, confidence enums, worry enum). Never show "Saved" until the server acknowledges; show "Saving your plan" with a real state until then. A failed write keeps the local copy and offers retry.
- "Not now" continues as a guest with the plan visible on Today; the first action that needs the server (the check) asks to sign in at that moment.

### Step 13. Reminders

- Purpose: ask for the notification permission when it has a concrete, personal benefit and is easy to accept.
- Input: a preview of the exact notification in the student's chosen window ("Tonight, 8:00 PM. Ten minutes of Accountancy is ready."), with "Remind me" (triggers the Android 13 runtime prompt) and "Not now" with equal visual weight.
- Payoff: the preview is the student's own plan, not a generic benefit list.
- Data use: the OS result and, if allowed, the device token (`POST /api/me/devices`). Account is needed for the token, which is why this follows step 12. A refusal never blocks anything, and Settings has the path back.

### Step 14. First move

- Purpose: end on a real action, not a confirmation (ScreensDesign: finish on "a single useful first action" [14]).
- Input: two options: "Start my starting-point check now" (the 10-question baseline, free once per launch subject) or "Do it at 8:00 PM tonight" (schedules a reminder using the window from step 9). Plus an optional card, not a blocking step: "Make Mobi yours" (colour or look; decorative, kept to one screen).
- Payoff: the check's result opens as the recap reveal the design pass defines, and re-ranks the plan. This is the honest, measured counterpart to everything the student stated earlier.
- Data use: server-scored session; the allowance and cost come from the quote, as in the existing spec. Confidence versus result comparison is shown here if it was collected.

### Fast lanes and edge cases

- Website hand-off: a deep link or Play install referrer may carry course and subject; the flow starts at step 6 with those pre-filled, adding the sample answers when they exist. (The website's five-question sample stays on the website.)
- Returning user on a new phone: "I already have an account" signs in and skips to Today; onboarding answers come from the profile.
- Offline: steps 1 to 11 work fully offline (data bundled); step 12 needs a connection and says so once.
- Interrupted: state is saved after every step and the flow resumes.
- Reduced motion: staged reveals become fades; every payoff keeps its text.
- Under 18: see section 6.2; the structure holds, with the parent-approval step slotted between 11 and 12 when it exists.

## 6. Compliance that affects first run

### 6.1 Google Play: government-exam apps

What Google's policies say [24][O]:

- Apps that are not affiliated with a government but communicate government information (here: NTA exam facts, DU Bulletin rules and cutoffs) must show easy-to-see information sources in the app description and on the store listing page, and make clear the app does not represent a government or political entity. The page does not say the statement must be inside the app; it asks for the store listing and description.
- The app's privacy policy must be easy to find both in the app and on the store listing page.
- Impersonation policy: do not suggest a relationship or authorisation you do not have; do not use another entity's logo or official emblems in a way that suggests affiliation; do not claim to be "official" without rights. This covers descriptions and in-app elements, not just the title and icon.
- Government apps declaration on the Play Console App content page has been required since 31 January 2023. It asks whether the app is for government use; MockMob answers no (the help page does not spell out the unaffiliated case, so confirm the wording in the console).
- Target audience: Families policy applies once an age group includes children (under 13). The audience here is 16 to 19. Select 16 to 17 and 18 and over, and do not select under 13 [I]; confirm in the console.

What competitors do [19][O]: put a plain disclaimer in the Play full description, usually near the end, often with links to the official NTA pages. None of the ten listings I read puts it in the short description.

Recommendation [I]:

1. Play listing full description: a closing paragraph saying MockMob is independent, is not affiliated with NTA or the University of Delhi, and listing the official sources it draws on (the NTA CUET site and DU's Bulletin and admission portal; the existing DU data cites the DU Bulletin 2026-27 PDF and admission.uod.ac.in) [23]. Not in the short description or screenshots.
2. In the app: one quiet line in You, About, and the same sources list in Help. Nowhere on Welcome, onboarding, question or result screens. Not required by policy for the in-app experience, and the owner has asked for it to go.
3. Website: footer or About, which already carries the sources.
4. Avoid the things that actually trigger review: "Official" in the name or listing, NTA or DU logos, crests or emblems on onboarding cards or in screenshots, and a developer name that suggests an authority. The app's "NTA-style" practice mode reproduces the look of NTA's test interface. Name it by what it is (for example, an exam-day layout), do not use NTA marks, and consider this when writing the listing (decision D7).

### 6.2 India's DPDP Act and Rules: what changes at onboarding for under-18s

Facts [25]:

- The Digital Personal Data Protection Rules, 2025 were notified on 13 or 14 November 2025 (sources differ by a day). Most obligations, including the child-data rules (Rule 10), take effect after 18 months, on 13 or 14 May 2027 [25][S: DCOMPLY, law-firm summaries]. That is inside the CUET 2027 window. MeitY floated cutting the timeline to 12 months (to about 13 November 2026) in January 2026; reports in September 2026 found no amending notice [25][S]. Check the Gazette (G.S.R. 846(E)) before relying on either date.
- A child is a person under 18. The PIB explainer says verifiable consent from a parent or guardian is required for a child's personal data, unless the processing relates to essential services such as healthcare, education or real-time safety. Penalties for violations of obligations relating to children can reach Rs 200 crore [25][O].
- Outside exemptions the Act bars tracking, behavioural monitoring and targeted advertising aimed at children, even with consent. The "educational institution" exemption in the Fourth Schedule is limited to those institutions and to educational purposes or safety. Commentators read it as not clearly covering independent commercial edtech platforms; others note ambiguity. The brain already records this as unresolved (assumption A6) [25][S].
- Consequence for personalised learning: the law does not clearly separate adaptive learning from "behavioural monitoring", and the Board has issued no guidance [25][S].

What this means for the proposed flow [I]:

1. Ask age before the account (step 11). The first personal data MockMob stores is created at sign-in; the age band should be known by then.
2. Do not ask for more than the product uses. Section 4 already drops city, gender, school, phone and contacts. Reservation category stays on the device and optional. Answers are enums, not free text.
3. Personalisation uses what the student chose and what they did to get the service they asked for (their stated subjects, rhythm, and their own check results). It does not use engagement profiling, ad targeting, third-party SDKs or a public leaderboard of under-18 names. (The API contract already flags the leaderboard and `topContributors` exposure as a privacy decision.)
4. Analytics stay off for minors and unknown ages by server enforcement today. Recommend asking adults for the optional usage-data consent after their first result rather than in onboarding, so the ask follows value [I]; the existing sheet can move there. The owner's 12 October decision (no complicated parental flow just for optional analytics) concerns analytics only; it does not settle account-level consent.
5. The open decision is the account itself for under-18s from May 2027 (D2). Options: (a) keep a minimal-data account for minors and take the education-purpose argument to counsel; (b) add a parent-approval step between age and account (a parent's contact, a verification link, and a Rule 10 route such as an existing verified parent account or a DigiLocker token); (c) restrict minors to local-only use until approved. Decision needed before the Play launch is aimed at the CUET season.
6. A student who turns 18 during the cycle needs a way to update the band (You, Privacy). Self-declared age is weak evidence; do not present it as verification.
7. "Delete my account" in-app and on the web (Play requirement and DPDP) is already in the backlog (gap G2 in the API contract).

## 7. What to remove or move from the current flow

| Current string or element | Action |
| --- | --- |
| Welcome footer, "MockMob is not affiliated with NTA or Delhi University." | Delete from the app flow. Goes to the Play listing, You > About and the website |
| "Sample questions. This is not a diagnosis." above each question | Delete (the sample leaves the app flow) |
| "Five original sample questions. No signup. Not an official PYQ or a scored diagnostic." | Delete |
| "Sample, not a diagnosis. Five questions can show how MockMob explains things..." | Delete |
| "Example, not your plan yet" dashed card | Replaced by the real starter plan (step 10) |
| "The five sample questions are the same for every paper." | Delete; the question that admits the answer changes nothing goes away |
| "On this phone" pill on guest screens | Delete in onboarding; keep truthful save states elsewhere only where work is actually pending |
| "This only decides your data settings." | Replace with the useful line in step 11 |
| Five-question sample as onboarding spine | Stays on the website only; the app uses steps 1 to 14 |
| Account step after the sample result | Moves to step 12 after the plan |
| Age and usage-consent sheet after sign-in | Age moves to step 11; usage consent moves to after the first result |

## 8. Copy directions (exciting, specific, honest)

Voice: a sharp senior who got in and wants you in. Short sentences, concrete nouns, a little dry humour. Mobi speaks in one or two lines and never celebrates a wrong answer. Sentence case, no emoji, no exclamation marks on success, no middle-dot strings. The owner's integrity rules stay: no invented numbers, no social proof, no recovered-marks or admission-chance claims.

Directions, each with an example line to adapt:

1. Lead with the seat, not the software. "Which DU seat are you after?" Under it, a real fact: "55 colleges took B.Com (Hons) through CUET in 2026."
2. Let real data supply the thrill. "Hindu College's 2026 first-list cutoff for B.Com (Hons): 919.9 for UR. Here is which subjects keep that door open." (Check the figure and the scale wording against the web calculator before use; it is a minimum allocation score, last year's, not a target or a promise.)
3. Make time concrete without scaring. "About 30 weeks to the expected May window. That is about 210 evenings." Computed from the date; labelled expected.
4. Invite honesty, promise a payback. "Be harsh. We will show you where your gut was right after your first check."
5. Name the worry in the student's own words. "What keeps you up at 1 AM?" with answers such as "I keep losing marks on easy questions" and "I never finish on time".
6. Treat rhythm as freedom. "Pick a pace you can keep. Rest days are part of the plan."
7. Make the plan feel earned. "Week one, sorted." Three lines, each tied to an answer they gave.
8. Commitment without threat. "Hold to lock it in. No streak to lose. Miss a day and the plan bends."
9. Explain the account by what they keep. "Save your plan. It follows you to the website and your next phone."
10. Make the age question friendly and useful. "Quick one: are you 18 yet? Either answer works. Under 18, we keep usage tracking off for you."
11. Make the reminder preview a promise of a specific thing. "Tonight, 8:00 PM. Ten minutes of Accountancy is ready."
12. When a warm-up answer is wrong, name the trap. "Classic trap. Here is the ten-second fix."
13. The exit for non-commerce students is warm and useful. "Not commerce? Tell me what you are taking. I will tell you the day we open it."
14. A quiet trust line where it earns its place, not a disclaimer: "Everything so far stays on your phone until you save."

Never write: affiliation or "not a diagnosis" lines on onboarding screens; "unlock", "supercharge", "level up your prep"; "your chances of getting into [college]"; any prediction of marks, percentile or rank; testimonials, user counts or "join thousands".

## 9. Gaps, assets and decisions

Needed to build this [I]:

- A shared step-deck schema and a test that fails when a step has no "what visibly changes" line.
- The DU index as an app asset (course and college lists, eligibility rules, 2026 cutoffs). The web combination planner and Compass logic already exist and should be reused, not reimplemented differently.
- A new allowlisted profile endpoint for the enum fields in section 4 (year, courses, colleges, confidence, worry, Mobi look), covered by account deletion; the contract's planned `PATCH /api/me/profile` is the place.
- A bundled warm-up question pool per launch subject, drawn from approved questions.
- Mobi pose set for the flow (wave, think, hold-to-lock, quiet-reminder). Vector or Rive or Lottie is preferable to video on a 3.5 GB RAM phone. No video is needed for onboarding. If the owner later wants short Mobi clips, small looping assets are the better form on the Galaxy M06.
- Image needs are limited: no college crests or logos (trademark and Play impersonation risk). College names are typographic.

Decisions for the owner:

- D1. Confirm the reading in section 1: the five-question sample stays on the website only, and the app uses the goal-first flow above.
- D2. Under-18 account approach before 13 May 2027 (section 6.2 options a to c) and a counsel review.
- D3. Keep the dream-college step? High cutoffs could discourage some students; the alternative is to show eligibility and the cutoff only on request.
- D4. Account methods at launch: Google plus email code only, or add phone or WhatsApp OTP later after measuring drop-off.
- D5. Move the usage-data consent from onboarding to after the first result.
- D6. Warm-up pool size per subject and who approves the questions.
- D7. Naming of the "NTA-style" mode and the Play listing wording.
- D8. Hands-on walkthrough of the Indian apps. On the owner's phone, record fresh installs of Physics Wallah, Unacademy, Testbook (CUET app), Embibe, Adda247, NTA Abhyas and one CUET catalogue app. For each, note: number of screens before home, the questions asked, whether a goal or a diagnostic appears, when the account is requested, what the notification prompt says, and the first screen after onboarding. A 10-minute screen recording per app is enough.
- D9. Include "Make Mobi yours" at all (decorative, an identity beat) or defer.
- D10. Pattern uncertainty: the 2027 subject cap and paper format may change after NTA's decision; copy stays generic until it is official.

Measurement. Without consent, onboarding funnel analytics for minors and unknown ages is not available by design. For adults with the optional consent, the existing event allowlist has `goal_set` and `reminder_permission_result`; step-level onboarding events would need new allowlisted names. Other usable measures that are not personal profiling: Play Console install-to-account counts, and the share of new accounts that start the first check within 24 hours.

## 10. Sources

Onboarding exemplars

1. Page Flows, Duolingo onboarding recording (iOS): https://pageflows.com/post/ios/onboarding/duolingo/9595ed9e-7cf9-406a-b425-c069d0549a07/ [R]
2. ScreensDesign, Duolingo onboarding design: https://screensdesign.com/articles/duolingo-onboarding-design/ [R]
3. Duolingo blog, how streaks keep learners committed (streak wager, weekend amulet): https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/ [O]
4. Taplytics, Duolingo delayed sign-up test (summary retrieved by search; page not opened): https://taplytics.com/blog/duolingo-ab-test-onboarding ; Appcues: https://goodux.appcues.com/blog/duolingo-user-onboarding [S, V]
5. ScreensDesign, Speak: https://screensdesign.com/showcase/speak-learn-spanish-french [R]
6. ScreensDesign, Brilliant: https://screensdesign.com/showcase/brilliant-learn-by-doing ; Brilliant help (sign-in options): https://brilliant.org/help/using-brilliant/how-do-i-get-started-on-brilliant/ [R, O]
7. ScreensDesign, Headway: https://screensdesign.com/showcase/headway-daily-micro-learning ; Paddle, Fix That Funnel (Headway): https://www.paddle.com/studios/shows/fix-that-funnel/headway [R, S]
8. ScreensDesign, Finch: https://screensdesign.com/showcase/finch-self-care-pet ; Lazyweb Finch flow: https://lazyweb.com/canvas/flows/finch/onboarding ; Pratt IXD critique: https://ixd.prattsi.org/2025/09/design-critique-finch-ios-app-2/ [R, S]
9. Lazyweb, Opal flow: https://lazyweb.com/canvas/flows/opal/onboarding ; Price Power podcast, "Opal Killed the Quiz Funnel", 14 July 2026 (episode notes only; the written breakdown at retention.blog was not found); Opal help: https://opalapp.com/help/how-when-and-where-does-opal-report-your-screen-time [R, S]
10. Page Flows, CRED onboarding (iOS): https://pageflows.com/post/ios/onboarding/cred/ ; CRED teardown: https://lucky-risk-e12.notion.site/Summary-CRED-38adeea52e9d803dbc5ec2132424ddb6 [R, S]
11. Page Flows, Revolut onboarding (iOS, old): https://pageflows.com/post/ios/onboarding/revolut/ ; RAW.Studio: https://raw.studio/blog/how-revolut-uses-4-onboarding-ux-tactics/ [R, S]
12. Page Flows, Snapchat onboarding (Android): https://pageflows.com/post/android/onboarding/snapchat/ ; Snap teen privacy: https://values.snap.com/privacy/teens [R, O]
13. FamApp Play listing (fetched 13 Oct 2026): https://play.google.com/store/apps/details?id=com.fampay.in ; Outlook Business: https://www.outlookbusiness.com/big-idea/teens-often-disagree-with-their-parents-but-fampay-brings-them-on-the-same-page-6153 ; Decentro: https://decentro.tech/blog/strengthening-kyc-process-fampay/ [O, S]
14. ScreensDesign onboarding guide: https://screensdesign.com/guides/app-onboarding-screens/ ; 7 onboarding trends for 2026: https://screensdesign.com/articles/app-onboarding-trends-2026/ [S]
15. Lazyweb, goal-question research: https://www.lazyweb.com/research/how-many-apps-ask-goal-question-onboarding ; paywall placement: https://www.lazyweb.com/research/how-far-into-onboarding-do-apps-place-the-paywall [S]
16. RevenueCat 2026 benchmarks: https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026 ; Adapty education benchmarks: https://adapty.io/blog/markdown/education-app-subscription-benchmarks.md [V]
17. Pushwoosh, Android 13 opt-in rates: https://www.pushwoosh.com/blog/android-13-opt-in-rates-research/ ; Netcore: https://netcorecloud.com/?p=94067 [V]
18. Endowed progress (Nunes and Dreze, Journal of Consumer Research 32:504-512, 2006), as reported at https://siliconcanals.com/t-car-wash-loyalty-cards-endowed-progress/ ; implementation intentions (Gollwitzer and Sheeran, 2006) as reported at https://goalsandprogress.com/implementation-intentions-gollwitzer-how-to/ [S]

Indian test-prep and CUET

19. Play Store listings fetched 13 Oct 2026 (full descriptions read): https://play.google.com/store/apps/details?id=xyz.penpencil.physicswala ; ...com.testbook.tbapp ; ...com.testbook.tbapp.cuet ; ...com.adda247.app ; ...cuet.com ; ...com.edurev.cuet ; ...com.cuetmock ; ...com.cuet_achieve ; ...com.cuet_bullseye ; ...in.cyberflow.dubuddy [O]
20. Adda247 guide: https://www.adda247.com/teaching-jobs-exam/download-adda247-app/ ; Unacademy goals: https://unacademy.com/manage-goals ; Embibe App Store: https://apps.apple.com/in/app/embibe-learning-outcomes-app/id1522718120 ; PW App Store: https://apps.apple.com/app/id1641443555 [O, S]
21. Google case study (Jagran): https://developers.google.com/identity/sign-in/case-studies/jagran-new-media ; OTPless, Meesho: https://otpless.com/case-study/meesho ; Astrotalk: https://otpless.com/case-study/astrotalk ; Android Credential Manager: https://developer.android.com/identity/sign-in/credential-manager-siwg-implementation ; SMS Retriever: https://developers.google.com/identity/sms-retriever/overview [V, O]
22. PW, CUET 2027 changes (drafts, decision expected about 20 Oct 2026): https://www.pw.live/cuet/exams/cuet-2027-major-changes ; dates expected: https://collegedunia.com/exams/cuet/exam-dates and https://www.shiksha.com/science/cuet-exam-dates ; reforms: https://www.collegedekho.com/news/cuet-ug-2027-pattern-reforms-ugc-and-nta-explore-shorter-papers-and-reduced-subject-limits-80280/ [S]
23. MockMob repo (read 13 Oct 2026): `public/du/2026/index.json` and `offerings/*.json` (DU Bulletin 2026-27 at du.ac.in; cutoffs at admission.uod.ac.in); `data/capabilities.js`; `docs/brain/APP-API-CONTRACT.md`; `docs/brain/APP-DESIGN-SPEC.md` 5.1; `docs/brain/PLAN-2026-10-12-APP-AND-WEB-EXPERIENCE.md`; `docs/brain/DECISION-2026-10-03-DIFFERENTIATOR.md`; `flutter_app/lib/features/onboarding/copy.dart`; screenshots `tmp/app-shots/m06` [O]

Compliance

24. Google Play: apps that communicate government information: https://support.google.com/googleplay/android-developer/answer/9514050 ; impersonation and misleading claims: https://support.google.com/googleplay/android-developer/answer/9888374 ; target audience and content: https://support.google.com/googleplay/android-developer/answer/9867159 ; Families policy: https://support.google.com/googleplay/android-developer/answer/9893335 ; government badge: https://techcrunch.com/2024/05/02/google-will-now-show-labels-in-play-store-to-denote-official-government-apps [O, S]
25. PIB explainer on the DPDP Act and Rules (Nov 2025): https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf [O] ; commencement dates: https://dpdpa.dcomply.in/rules/ [S] ; S.S. Rana on schools, coaching centres and platforms: https://ssrana.in/articles/schools-coaching-centres-platforms-processing-childrens-data-are-you-compliant/ [S] ; Tsaaro on edtech and children's data: https://tsaaro.com/blogs/teaching-in-the-age-of-dpdpa-when-child-safety-becomes-edtech%E2%80%99s-competitive-advantage [S] ; 12-month proposal: https://chambers.com/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs [S]. The Gazette text (G.S.R. 846(E)) was not retrieved.
