# MockMob Android: design and build spec

Status: definitive spec for implementing agents, 12 October 2026. Flutter, Android only. App name MockMob, package `in.mockmob.app`. Nothing here is built. Every performance figure is a target until it is measured on the real budget phone, which is still pending; an emulator is not evidence.

Authorities, in precedence order: owner chat instruction, then the MockMob live design system (DESIGN.md, Arena tokens, Gabarito and Hanken Grotesk roles, volt `#D2F000` as the action fill), then `AI OS/wiki/concepts/ui-ux-standards.md`, then generic skills. Research: PRODUCT-EXPERIENCE-RESEARCH-2026-10-12.md. Plan: PLAN-2026-10-12-APP-AND-WEB-EXPERIENCE.md. API: APP-API-CONTRACT.md (cited as `[API §n]`).

Tags: `[NEW-API]` means the endpoint does not exist yet and a backend module builds it (section 12.2). `[CONFIRM]` means an owner or engineering decision is needed before it ships. Until a `[NEW-API]` endpoint ships, the screen uses the stated fallback or hides the feature.

---

## Amendments by the orchestrator (12 October 2026, override the sections they name)

A1. **Signature reveal: the sheet arrives folded.** Mobi is drawn as a folded sheet of volt paper, so MockMob's own version of a wrapped recap is a handed-back answer sheet folded in half. In 5.6.2 the sealed sheet is drawn folded along a horizontal crease at about 45% height. The lower half is the visible front: "Mock 7, Accountancy", submit time, "Saved on the server." and the tab. The upper half is the folded-over flap, a plain `raised2` surface with a 1 dp crease line and a small folded-corner notch echoing Mobi's body. Swiping the tab up unfolds the flap. It rotates about the crease from 180° to 0° with `Matrix4.identity()..setEntry(3, 2, 0.0012)..rotateX(angle)`, one transform layer and no `saveLayer`, following the finger 1:1 over 180 dp. The question strip and counts appear as the flap opens. Tick haptics fire at 25, 50 and 75%, and the open haptic on completion. All the other 5.6 rules still apply: release under 60% springs back, "Open without the reveal" and the TalkBack action always work, ritual decay from the fourth sheet is a 160 ms cross-fade unfold, and reduced motion is an instant unfold. The fold is drawn with plain shapes (no images) and must hold 60 fps on a 720 by 1600 device.

A2. **No code generation outside core.** Do not use `freezed`, `json_serializable`, `riverpod_generator` or `riverpod_annotation`. Models are hand-written Dart classes with `fromJson`. Riverpod 3 (`flutter_riverpod`) is used without codegen. Drift code generation (`build_runner`) runs only for the core database, owned by Module 0. No other module adds drift tables or runs `build_runner`.

A3. **No Firebase in v1.** No `firebase_core` or `firebase_messaging`: the server sender (B5) and the owner's Firebase project do not exist yet. Notifications are local only (`flutter_local_notifications` with inexact scheduling). A `PushTransport` interface in `core/notifications` stays unimplemented until FCM is added. Remove the Firebase meta-data and service items from Module 0's manifest list.

A4. **`flutter_timezone` was removed** (its build script pulls an old Android Gradle plugin). The student's timezone comes from `GET /api/me/notification-prefs` (`timezone`, default `Asia/Kolkata`). Local scheduling uses the `timezone` package with that IANA name.

A5. **B1 is done differently.** `PATCH /api/users/{id}` now accepts only `name` (1 to 80 characters) and `subjects` (up to 5 known subject ids) and rejects everything else (commit f6411b2). The app uses that route. No `/api/me/profile` is needed.

A6. **Defaults taken for the open items in section 13,** each reversible by the owner:
- The analytics switch starts off. An adult turns it on explicitly.
- The goal unit is study days.
- The welcome line has no "Prove it" clause until checks are live.
- Subjects: the Commerce four, plus an "Other subjects" row for the remaining supported subjects.
- Push cap: 3 a week, set client-side, until the server sender exists.
- Recap tone: default variant only until B8 ships.

A7. **The dependency list is fixed.** It lives in `flutter_app/pubspec.yaml` (committed, resolved and building). Modules must not edit `pubspec.yaml`. If a package is truly missing, stop and report it.

A8. **Build environment on the owner's PC.** Run `source flutter_app/tool/android_env.sh` before any `flutter` command. The emulator AVD is `mockmob_budget` (Android 14, 720 by 1600, 280 dpi, 3 GB).

A9. **Assets prepared by the orchestrator:**
- `assets/fonts/` holds static Gabarito 400-800 and Hanken Grotesk 400-700 instances with their OFL files.
- `assets/mobi/*.webp` holds seven poses, 288 px tall, about 14 KB each: greeting, attentive, celebrating, encouraging, idle, pointing, thinking. Use `idle` where this spec says "neutral". The "hop" is a transform on a pose, not extra frames.
- The five sample questions come from `src/components/landing/DemoDrill.jsx` lines 12-58. Module 2 copies them verbatim into `assets/sample/sample_questions.json` with the disclaimer.

A10. **Golden tests:**
- Load the bundled fonts with a shared test helper (`test/helpers/fonts.dart`, owned by Module 0), so goldens show real type, not the Ahem test font.
- Render at 360 by 780 logical px, device pixel ratio 2.
- Each module renders its goldens, then looks at every PNG it produced before reporting done.

---

## 0. Binding rules (read before any screen)

1. Sentence-case labels. No ALL-CAPS eyebrows or kickers. No numbered badges.
2. Tabular numerals on every number (`FontFeature.tabularFigures()`). No monospace font ships.
3. No middle-dot meta strings. Write "8 questions, about 10 minutes".
4. 12-hour times ("11:42 PM"). Dates as "12 October".
5. No decorative gradient, glow, glass or blur. No emoji. No arrow or chevron appended to button text. No exclamation-mark successes.
6. No fake progress. No success state before server acknowledgment. Local pending work is never called saved or safe: it is "On this phone" (for example "9 answers are on this phone. Not sent yet."). The word "saved" always means server-acknowledged.
7. 44 dp minimum touch targets (48 dp for tabs and palette cells, 54 dp primary keys, 56 dp answer options). Reduced motion respected everywhere.
8. Truth. Never print a recovered-marks number, percentile, admission chance or the word "mastered". Practice is not proof. Fresh-question checks are content-gated (`RELEASE_GATES.content=false`, `pathwayState:'blocked_content'`, [API §6]); every surface that touches a fresh check shows an unavailable or "practice, not proof" state, and the Checked stage always reads "not available yet". No testimonials, no headcounts, no leaderboard.
9. Mobi never appears during timed answering, never speaks (pose and motion only, no text), never reacts to inactivity, never shows a sad pose.
10. No correctness is shown during an exam-equivalent mock (Full and NTA-style). Practice, repair and sample show correctness.
11. Scoring, answer keys, plans, credits, Pro status and deadlines are server-only. The app renders what the server returns. Marks shown are `correct*5 - wrong` out of `n*5` from server counts (a display derivation, [API §2.8]); the app never decides authority.
12. Volt is an action fill (primary keys) and the active-tab pill only. Done, selected and progress states use ink, a check glyph and fill weight, never volt. On paper, volt is never text; use `accentText`.
13. No prices, no purchase links, no "upgrade" buttons anywhere. A Pro-gated state says what the account includes and offers a free alternative.

---

## 1. Experience principles and emotional arc

### 1.1 Principles
1. **The student's own work is the star.** The one recurring object is the answer sheet (the question strip of right, wrong, blank, changed cells already on the web result page). The recap, repair and Review all use it.
2. **One dominant action per screen.** Everything else is quieter.
3. **Concentrate during, understand after, restart gently on return.** Motion and personality scale to the moment: zero while answering, one designed peak after a mock, almost nothing on return.
4. **Proportion.** Feedback matches the real outcome. No celebration for a poor result, none for tapping the app open.
5. **Rhythm, not a chain.** Rest is part of the design. Nothing earned is ever lost or reset on screen.
6. **Every ending is designed.** A score with no next step, or a failure with no recovery, is the bug to prevent.
7. **Honest state words.** "On this phone", "Sending", "Saved on the server" mean exactly that.

### 1.2 Emotional arc

| Phase | Student feels | App does |
|---|---|---|
| First launch | Sceptical, short on time | A real question within seconds, no account |
| Before a task | Tired, wants it sized to the time | One next move, honest duration, 10/20/30 chooser |
| During a timed mock | Concentrating, anxious | Disappears: no Mobi, no correctness, near-zero motion, visible save state |
| Submitting | Afraid of losing answers | Proves arrival first, then says anything else |
| Opening the result | Vulnerable | Sealed sheet they open themselves, true numbers, calm tone |
| After a repair | Wants the work counted, no more | Mark on the sheet, stated limit, permission to stop |
| Returning after 1 or 10 days | Possibly guilty | Remembered context, smaller restart, "Nothing was lost" |
| End of week | Wants an honest ending | Bounded summary, no verdict |

Peak: the sheet opening. End: each session type has a named ending (section 5). Late-night is the real condition, so care is text only and never blocks.

---

## 2. Visual system (Flutter tokens)

### 2.1 Colour roles
Implement as `ThemeExtension<MmColors>`; derive `ColorScheme` only for framework widgets. Every wash is pre-flattened to an opaque colour (no alpha-over-alpha, no `saveLayer`).

| Role | Dark (night) | Light (paper) |
|---|---|---|
| ground | #0B100E | #F4F5F0 |
| raised | #131A16 | #FFFFFF |
| raised2 | #18211B | #F8F9F4 |
| sunken | #0F1512 | #EEF0E8 |
| line | #253026 | #DCE1D4 |
| lineStrong | #384736 | #BCC5B0 |
| ink | #F2F4EC | #172016 |
| ink2 | #BCC5B9 | #3D4A39 |
| ink3 | #93A08F | #56624F |
| ink4 (decorative only) | #7F8B7B | #646F5D |
| volt (action fill) | #D2F000 | #D2F000 |
| voltInk (on volt) | #0B1000 | #0B1000 |
| voltEdge (key lip) | #9DB400 | #9DB400 |
| accentText | #D2F000 | #4F6400 |
| focusRing | #D2F000 | #4F6400 |
| badText | #FF9D92 | #B0291F |
| warnText | #E0B93F | #845400 |
| goodText | #B6E36E | #3D6600 |
| wrongSurface / wrongBorder / wrongText | #2A1614 / #7D3128 / #FFC9C2 | #FBE9E7 / #B93225 / #B0291F |
| scrim | #000000 at 40% | #000000 at 40% |

Rules: theme setting is Match phone (default), Light, Dark; no time-of-day switching; fall back to light when the system reports none. The wrong trio appears only in practice, repair and sample feedback, never in a mock. State is never colour alone: pair with a word, glyph or shape.

### 2.2 Type roles
Bundle Gabarito 600/700/800 and Hanken Grotesk 400/500/700, subset to Latin plus U+2212 and the rupee sign if present; all files at most 350 KB. Verify `tnum` in both fonts at setup; if Gabarito lacks it, numerals in timers and tables use Hanken with tabular figures. Devanagari falls back to the system font. Honour `MediaQuery.boldText`.

| Role | Font | Size sp / height | Weight | Letter spacing |
|---|---|---|---|---|
| figureHero (recap card 1 only) | Gabarito | 96 / 1.0 | 800 | -3.5% |
| display | Gabarito | 36 / 1.05 | 800 | -3.5% |
| headline | Gabarito | 28 / 1.1 | 800 | -3% |
| title | Gabarito | 22 / 1.2 | 700 | -2% |
| subhead | Gabarito | 17 / 1.3 | 700 | -1% |
| figure | Gabarito | 40 to 56 / 1.0 | 800 | -3.5% |
| timer | Gabarito | 20 / 1.0 | 700 | 0 |
| button | Gabarito | 17 / 1.0 | 700 | 0 |
| label | Gabarito | 13 / 1.3 | 600 | 0 |
| lead | Hanken | 18 / 1.45 | 400 | 0 |
| question | Hanken | 18 / 1.5 | 500 | 0 |
| body | Hanken | 16 / 1.55 | 400 | 0 |
| small | Hanken | 14 / 1.5 | 400 | 0 |

Text scales to 200%. Only bottom-nav labels clamp, to 1.3x (full name stays in semantics). `figureHero` clamps to 1.3x at large scales. Question and option text never ellipsise. Names, costs and disclosures never truncate.

### 2.3 Spacing, radii, elevation
- Spacing scale: 4, 8, 12, 16, 20, 24, 32, 48. Gutter 16 dp (20 dp on Today cards). Gap between independent groups 32 dp. Card padding 20 dp.
- Radii: 10 small controls, 14 keys, fields, options, 20 panels and sheet inner cards, 28 sheet tops, pill chips.
- Elevation is tonal: ground, raised, raised2, 1 dp `line` hairline. Light cards may carry one precomputed `const BoxShadow` (0,1,2 at 6% plus 0,12,32,-18 at 18%). Dark has no shadow. Never nest cards.
- Content max width 600 dp, centred on larger screens. Portrait only on phones.
- No ripple: `NoSplash.splashFactory`. Pressed fills replace ripples. Every pressable has rest, pressed, focus, disabled and loading states.

### 2.4 The touch keycap (signature)
`KeyButton` is a custom widget.
- Geometry: flat edge `DecoratedBox` (voltEdge, 4 dp, offset down) under a face (volt, 14 dp radius, min height 54 dp, 56 dp in runner). Rest: face 4 dp up.
- Press: on pointer-down the face translates down 4 dp in 80 ms (easeOut); the edge stays. Release returns in 140 ms; the tap commits on up with the `press` haptic.
- Disabled: face down and flush at 45% opacity, with a one-line reason below when it matters.
- Loading: label stays, 18 dp spinner inside, width unchanged.
- Secondary: raised fill with `lineStrong` lip. Quiet: transparent, 44 dp, no lift. Answer options on night use a 3 dp lip `#0A0D09`.
- A chosen answer option stays pressed flush (selected state is flush face plus 2 dp ink border plus check glyph, not volt and not green).
- Each key sits in a `RepaintBoundary`. Cost: one translate and two flat boxes.

### 2.5 Iconography
Lucide-style line icons via `lucide_icons_flutter`: 24 dp, 1.75 dp stroke, round caps, one style only. Visible size is not the hit area (hit area at least 44 dp). Tab icons switch outline to filled glyph. Icons never replace labels in navigation.

### 2.6 Illustration and Mobi
Mobi ships as pre-sized WebP poses (each at most 12 KB): greeting, attentive, neutral, hop frames. No Rive or Lottie. Motion is transform-only (settle 420 ms, hop 400 to 560 ms). Mobi appears only at: Welcome (96 dp greeting), sample explanation panel (40 dp), Today new-user and 10-day return (greeting once), recap card 3 (48 dp attentive, beside no text) and card 4 (neutral), repair finished (one hop), weekly goal met (one hop), and empty or error states (settle once). Absent: splash, timed runner, submit and wait, sealed sheet, recap cards 1 and 2 on a lower result, repair question feedback. Reduced motion: static pose. Section 6.3 holds the full matrix.

---

## 3. Motion and haptics

### 3.1 Tokens (one file `lib/core/motion/motion.dart`)
```dart
class Motion {
  static const press = Duration(milliseconds: 100);
  static const release = Duration(milliseconds: 140);
  static const ui = Duration(milliseconds: 200);
  static const card = Duration(milliseconds: 240);
  static const result = Duration(milliseconds: 320);
  static const figureRoll = Duration(milliseconds: 420);
  static const milestone = Duration(milliseconds: 500); // ceiling, optional
  static const out = Cubic(0.23, 1, 0.32, 1);
  static const arena = Cubic(0.16, 1, 0.3, 1);
  static const drawer = Cubic(0.32, 0.72, 0, 1);
  static const inOut = Cubic(0.77, 0, 0.175, 1); // position change only
  static Duration of(BuildContext c, Duration d) => reduced(c) ? Duration.zero : d;
  static bool reduced(BuildContext c) =>
      MediaQuery.disableAnimationsOf(c) || ReducedMotionSetting.of(c);
}
```
Only opacity and transform animate. Never ease-in on UI, never scale(0) (start at 0.95 with opacity 0), never page-level `Opacity` over large trees (use `FadeTransition`), no `BackdropFilter`.

### 3.2 Tiers
| Tier | Where | Budget |
|---|---|---|
| Answering | Timed mock, NTA-style | 120 ms fade into screen, instant option selection, no travel |
| Selection | Today, Practice, Review, Learn, You, repair, sample | Press 100 to 140 ms, UI 200 ms, entrance up to 420 ms |
| Recap | Sealed sheet and cards | Open 220 ms, card change 240 ms, bar 320 ms, figure roll 420 ms |
| Milestone | First repair ever, week goal met | At most 500 ms, once per event id |

Page transitions: tab switch 140 ms fade, no travel. Push 220 ms fade plus 12 dp slide from trailing edge (pop 180 ms). Modal sheet slides up 280 ms on `drawer` (exit 200 ms). Runner 120 ms fade both ways. Predictive back enabled (`android:enableOnBackInvokedCallback`); exam and sheets use `PopScope` explicitly.

### 3.3 Haptic vocabulary (`Haptics` wrapper)
Three verbs plus a guard. All skipped if the system touch feedback or the in-app "Touch feedback" switch is off.

| Verb | Flutter call | Used for |
|---|---|---|
| tick | `selectionClick` | Tab change, option select, time chooser, palette cell, recap card snap, sheet drag thresholds (25, 50, 75%) |
| settle | `lightImpact` | Key commit on release (except in exam), a repair step acknowledged by the server, correct repair retry, result ready in foreground, 5-minute and 1-minute warning (one each) |
| open | `mediumImpact` | Sheet opened, submission acknowledged by the server, repair finished, weekly goal met |
| warn | `lightImpact` twice, 80 ms apart | Destructive confirms (leave mock, delete account) |

Errors and wrong answers have no haptic. In the exam only tick fires (option select, mark for review). If a budget motor makes `selectionClick` imperceptible on the real phone, substitute `lightImpact` for tick. No sound ships in v1.

### 3.4 Reduced-motion fallbacks
Triggered by system "Remove animations" or the in-app Reduce motion override. Movement becomes an instant change or a 120 ms fade; the figure roll is skipped; the stacked bar appears complete; Mobi is static; the sheet opens by a 120 ms cross-fade; the first-sheet nudge is skipped; haptics still fire if enabled (they are not motion). Every fallback keeps the same information as text.

---

## 4. Information architecture and navigation

### 4.1 Tabs
Five labelled bottom tabs, same names as the web Arena: **Today, Practice, Review, Learn, You**. 64 dp plus bottom inset, `raised` fill, 1 dp top hairline, tab target 72 by 64 dp, icon 24 dp, label 12 sp Gabarito 600 sentence case. Active tab: 56 by 32 volt pill behind the icon with `voltInk` icon (pill scales X from 0.5 to 1 and fades over 200 ms; icon dips 2 dp for 160 ms). Haptic tick on a different tab; re-tap scrolls to top, second re-tap pops to the root. One 8 dp dot on Review while a locally recorded received result has not been opened (`pending_result`, section 10); no numeric badges. Semantics: "Practice, tab 2 of 5, selected". `StatefulShellRoute` keeps branch state.

### 4.2 Routes (go_router)
```
/splash
/welcome                      first run
/onboarding/subject
/onboarding/sample/:i         i = 1..5
/onboarding/sample/result
/sign-in                      email, google
/sign-in/code?email=
/before-you-start             age + usage-data choice (sheet route)
/today                        (shell branch 0)
/today/why/:actionId          sheet
/practice                     (branch 1)
/practice/setup/:mode
/practice/start               start/resume transition
/run/:sessionId               exam or practice runner, fullscreen
/run/:sessionId/submit
/result/:attemptId/sealed
/result/:attemptId/recap/:card
/result/:attemptId            full result
/review                       (branch 2)
/review/mistakes
/review/record
/review/repair/:attemptId/:questionId
/learn                        (branch 3)
/learn/:unitId
/learn/run/:runId
/you                          (branch 4)
/you/goal
/you/rhythm
/you/notifications
/you/privacy
/you/account
/you/delete
/you/milestones
/you/bests
/you/appearance
/you/help
/today/week                   sheet
/today/alternatives           sheet
/today/weekly-ending          dismissible card route
/permissions/notifications    pre-prompt sheet
/practice/result/:attemptId   practice ending (5.4.1)
/review/repair/:attemptId/ending
/learn/run/:runId/done        run ending (5.9)
/dashboard                    alias to /today
```
`/dashboard` and any unknown path open the matching tab or a Custom Tab on `www.mockmob.in`.

### 4.3 Deep links
App Links `autoVerify` on `https://www.mockmob.in` only (apex redirects; verification does not follow redirects). Paths: `/today`, `/result/:id`, `/review`, `/dashboard`, `/learn`, `/learn/*`. Needs the Play App Signing SHA-256 in `ANDROID_CERT_SHA256` [API §1.1]; until set, links open in the browser. Signed-out link: go to sign-in, then continue to the intended route. Result belonging to another account (404): "This result belongs to another account. Sign in with the right one." No pricing or checkout links are handled. Emit `app_link_opened` (consented only).

### 4.4 Back behaviour
Tab root back goes to Today, then exits. Runner back opens the leave guard (never discards). Recap back goes to the full result, never exits the screen. Sheets dismiss by drag, scrim or back without resetting the parent. Sign-in back from code goes to the email field with the email kept.

---

## 5. Screen-by-screen specification

Format per screen: purpose, layout, components, states with exact copy, interactions, analytics (only when consented; names from the server allowlist [API §2.2], props limited to `subject,mode,state,action_type,outcome,source,screen,variant` strings and `minutes,count` numbers), acceptance.

### 5.1 First run

**5.1.1 Cold start and Welcome.** Purpose: put a real question in front of the student within seconds, no account. Splash: Android 12 splash API, ground colour, static wordmark, no Mobi; first Flutter frame at most 1.5 s (target). Welcome layout: Mobi greeting 96 dp (one 420 ms settle, then still), headline "Find the marks you're losing. Repair the mistake." (display 34), line "Start with five real CUET questions. No account needed." (lead), primary key **Try 5 questions** (full width), quiet **I already have an account** (44 dp), footer small "MockMob is not affiliated with NTA or Delhi University." The third clause "Prove it on fresh questions" is added only when the content gate is open (build flag `freshChecksLive`). Interaction: Try 5 goes to subject. Analytics: none before consent is known (the student is a guest and has no consent record). Acceptance: no network call is needed to render; works offline; golden at 360 by 780 light and dark.

**5.1.2 Subject.** One decision: "Which paper first?" Four 56 dp rows: English, Accountancy, Business Studies, Economics. These are the Commerce launch subjects, the ones with a free first diagnostic, a free first Full mock and fresh-practice replay; confirm against `/api/subjects` `practice==='supported'` when online, bundled list otherwise. Below them a quiet row **Other subjects** opens the rest of the supported list (the API marks 15 subjects supported, so 11 more); those subjects work but have no free allowances (`baseline` and `full_sample` cover only the four) [CONFIRM: show the other 11 in v1, or keep Commerce only until their content is ready]. Reason: "We use this to set up your first mock. You can change this later in You." The five sample questions that follow are the same for every paper and the screen says so: "The five sample questions are the same for every paper." One tap advances after a 140 ms pressed state. Multi-subject setup lives in You.

**5.1.3 The five questions.** Source: bundled JSON of the five landing questions with the disclaimer "Five original sample questions. No signup. Not an official PYQ or a scored diagnostic." [API §2.11]. Layout: five position pips (position, not reward) and "Question 2 of 5"; caption "Sample questions. This is not a diagnosis."; question (question role, 20 sp Gabarito per DESIGN); four 56 dp option keys. Resolution sequence (practice skin): 0 ms chosen key settles flush, 90 ms others recede, 180 ms reason panel rises (220 ms), 260 ms the next key fades in. Correct: ink check glyph, `settle` haptic. Wrong: wrong-trio panel, no haptic, explanation shown. Mobi 40 dp only inside the explanation panel after the choice (hop for correct, attentive nod for wrong); never before the choice. Keys: **Next question**; last one **See my result**. Back loses nothing. Answers persist locally, marked "On this phone" until an account exists. Sample feedback shows correctness because this is practice, not a mock.

**5.1.4 Sample result and what the next move would look like.** Figure "4 of 5 correct" (figure 56). Line: "Sample, not a diagnosis. Five questions can show how MockMob explains things. They cannot say where you stand." Dashed-outline card labelled "Example, not your plan yet": "After your first full mock, your first thing to fix appears here, with the evidence behind it." Primary **Save this and continue**, quiet **Try another subject**.

**5.1.5 Guest carry-over.** Account step: "Create a free account to keep your five answers and start a mock." Keys **Continue with Google** and **Use an email code** (section 5.2). After sign-in the app calls `POST /api/me/sample-import` `[NEW-API]` with `{importKey, sampleVersion, subject, answers:[{sampleQuestionId, optionKey}]}`; idempotent on `importKey` so it merges exactly once. States: pending "Saving"; accepted "Saved to your account" (only after the server acknowledges); failure "We could not save yet. Your answers are still on this phone. Try again." Fallback until the endpoint ships: keep the sample on the phone only and skip the "Saved to your account" line (never claim saved).

**5.1.6 Before you start (one skippable sheet, shown after sign-in because the writes need an account).** Step 1: "Are you 18 or older?" three equal rows: **Yes**, **No**, **Prefer not to say**; beneath: "This only decides your data settings." Writes `PUT /api/me/consent {ageBand, analyticsAllowed:false}` (`yes` to `adult`, `no` to `minor`, `prefer not to say` to `unknown`). Step 2 only for adults: the usage-data card exactly as specified in 5.12.3, which is a switch labelled exactly **Allow usage data to improve MockMob** (starting off), the explanation text, the "See every event we collect" link and a single key **Done**. Turning the switch on writes `PUT /api/me/consent {ageBand:'adult', analyticsAllowed:true}` and the switch shows on only after the server acknowledges; Done with the switch off changes nothing. For minor or unknown the card is not shown, analytics stays off, and no parental flow exists. Skip leaves `ageBand:'unknown'`. Notification permission is not asked here.

**5.1.7 Landing on Today, new user.** Mobi greeting once; "Let's find a useful starting point." Primary **Start a full mock** ("50 questions, 60 minutes"; the first one in the chosen subject is free when the quote's `full_sample` allowance is available), secondary **Try a 10-minute diagnostic** (a Quick practice of 10 questions with `purpose=baseline`; its cost comes from the quote) labelled "A first signal, not a full picture."

Acceptance (5.1): the whole flow works with airplane mode until the account step; every option 56 dp; TalkBack reads "Question 2 of 5"; no Mobi before an answer is chosen.

### 5.2 Sign-in
Purpose: get the student in, preserving work.
- **Email code.** Field 52 dp, `AutofillHints.email`. Key **Send code** calls `POST /api/auth/email-login` [API §2.1]. Code screen: "Enter the 8-digit code we emailed to asha@example.com" (use the real address), field with `AutofillHints.oneTimeCode`, tabular "Resend code in 0:30" (60 s cooldown). Verify with Supabase `verifyOTP` type `email`, retry `magiclink` on failure (UNVERIFIED which succeeds), then `GET /api/auth/me` with the documented 429/5xx backoff.
- **Google.** `signInWithIdToken` (google_sign_in plus supabase_flutter). Needs external config [API Q3].
- States: sending ("Sending a code", key loading); wrong code "That code did not work. Check the latest email or send a new code."; rate limit "Please wait a minute before asking for another code."; offline "You are offline. Connect to sign in."; Google cancelled returns silently to the screen. Work is preserved on every error.
- Analytics: none until consent loaded (consent GET after sign-in).
- Acceptance: never display a raw 422 or JSON; a 401 later refreshes once then signs out with "Please sign in again. Your work is still on this phone."

### 5.3 Today
Purpose: "What do I do with the time I have?" Data: `GET /api/learning/plan?minutes=` (fetch on open and after a session, never on a timer; cache last), `GET /api/me/rhythm`, `GET /api/auth/me`, `GET /api/practice/quote` for the one practice action the card is about to offer (no side effects), `GET /api/ai/credits` (read-only, for the repair wallet line), the cached attempts list (for the observed chapter breakdown and repair candidates, 5.6.3), and local records: the session draft, `pending_result`, `repair_local`, `rhythm_seen`, `dismissals` (section 10).

Layout, one scroll, 360 dp:
1. Title "Today" (headline) and date "Monday, 12 October". No exam countdown until an official date is confirmed in config.
2. **Resume or ended slot** (only when a valid local or server session exists):
   - In progress (`endsAt` in the future): "Mock 7, 31 of 50 answered. Time left 22:10." Line "Saved on the server at 10:03 PM" only when the last ack time is known, else "Answers are on this phone." Primary **Continue**. Sits above the next-move card.
   - Ended while away (`endsAt` has passed). The copy is chosen from real state, in this order (see 5.5.1 for the mechanics):
     - the attempt exists on the server (auto-finalised at expiry, or submitted by the background job): "Mock 7 ended at 10:42 PM. Your 31 answers sent before then were recorded." Key **Open result**. The 31 is the number of answered questions covered by `acknowledgedSequence`, counted from the local journal.
     - no attempt yet, submit window still open (`now <= expiresAt + 120 s`): "Mock 7 ended at 10:42 PM. Your answers are on this phone and are being sent." Key **Try again**.
     - no attempt and the window closed (`SESSION_EXPIRED`, then a `GET /api/attempts/{id}` that returns 404): "The submission window for Mock 7 has ended, so it could not be recorded. 31 answers were sent before 10:42 PM." Key **Choose something else**. Never a promise that anything counts.
3. **Result slot:** while a `pending_result` record has no `openedAt` (a result that was received but not opened, including after process death): "Mock 7 was received. Your result is ready." Key **Open result**. The same record drives the dot on the Review tab. Clears when the sealed sheet opens.
4. **Due-check slot:** while `pathwayState==='blocked_content'`: one quiet line "Fresh-question checks are not available yet. Repairs are practice, not proof." When content opens it becomes the due-check card.
5. **Next-move card** (raised, 20 dp radius): title; evidence line (from `primary.evidence`, or from the observed chapter breakdown when the client built the card); duration chooser (segmented keys, 44 dp, tick on change, card height stable); restated task "3 mistakes, about 10 minutes"; basis line "Based on Mock 7 on 2 October. Early signal from one mock."; primary **Start repair** (or the action's verb); quiet **Why this?** and **Choose something else**. Web `href` values are mapped to native routes by `ActionRouter` (never opened blindly) [API §2.4].
   - **Where the card comes from today.** While recovery is gated the plan's `primary` is realistically `resume_session` or `ordinary_practice` [API §2.4], so the central loop (mock, first thing to fix, repair) has no plan source. Until B10 adds structured `repair` and `investigate` actions to the plan, the client builds the Ready card itself: the latest full or NTA-style attempt within 14 days that has at least one repair candidate (5.6.3) gives "Repair 3 mistakes from Mock 7" (the chapter is named when one chapter holds most of them), the evidence from the observed chapter breakdown, and the task line from the candidate count. The plan's `primary` and `alternatives` then feed **Choose something else**. When the server later returns `repair` or `investigate`, the plan's action wins and the client-built card is retired.
   - **Cost lines.** The practice action shows its cost from the quote ("Free today", "Uses 10 credits. You have 8."). A repair task shows the explanation wallet when the balance is below the task: "This repair needs 3 explanation credits. You have 2. Start with 2 mistakes, or read the key explanations in Review." An unknown balance (`known:false`) shows nothing, never 0. The same lines appear on recap card 4.
6. **The week** (section 6.1): one compact row.
7. **Practise something else:** list rows (not cards): Full mock, Quick practice, Chapter practice.

**Choose something else** opens an alternatives sheet. Rows: the plan's `alternatives` (up to 2), the plan's `primary` when the client built the card, then Full mock, Quick practice, Chapter practice, Review your mistakes (free) and Learn (free), each with its cost from the quote or the word "Free". Tapping a row starts that setup. A quiet key **Not today** records a local dismissal in `dismissals`, keyed by (kind, subject, chapter, source attempt id): it hides only this suggestion on Today until 4:00 AM the next local day or until a new attempt is submitted, whichever comes first, promotes the next-ranked alternative, and shows one quiet line under the card, "Hidden until tomorrow. Your mistakes are still in Review." A dismissal never deletes, hides or edits anything in Review, the repair record, any attempt or the plan inputs, so history is never rewritten. A dismissed suggestion is not re-shown inside its expiry even if the plan returns it. `next_move_dismissed` is sent on **Not today** only.

**State precedence.** The first match decides the next-move card. The resume or ended slot and the result slot are independent and always sit above the card. Returning and late night change defaults only, never the state.

1. History unavailable
2. New user
3. Subject changed
4. Stale
5. No eligible content
6. Thin history
7. Ready
8. Repaired, check not due
9. No strong weakness

Verification due is never rendered while the gate is closed. Entitlement blocked replaces only the action it blocks. **Default duration:** Returning (3 or more days) 5 minutes, otherwise late night (11 PM to 7 AM) 10 minutes, otherwise the plan's own `minutes`. The plan honours only 10, 20 and 30, so chips 10, 20 and 30 re-request it. The **5-minute** chip is client-side and shown only when the task can shrink: a client-built repair becomes "up to 2 mistakes, about 5 minutes", a practice action becomes a Quick practice of 5 questions (60 seconds each, validated by the quote). If neither applies, the chip is not shown.

States (copy exact):

| State | Condition | Copy and action |
|---|---|---|
| History unavailable | `recordState==='unavailable'` or load error | "Your earlier results are still there. We could not load a new suggestion." **Try again**, **Choose practice** |
| New user | no attempts | "Let's find a useful starting point." Keys **Start a full mock** (the free first mock for that subject when the quote's `full_sample` allowance is available), **Try a 10-minute diagnostic** |
| Subject changed | subjects edited and no attempt in the new set | "You changed your subjects. Earlier results stay under the old ones." The new-user keys; the old history stays in Review under the old subject |
| Stale | basis older than 14 days | "Based on a mock from 21 September. A new practice set will update this." **Practise to refresh** |
| No eligible content | no content for repair | "We do not have enough reviewed questions for this repair yet. Try the related review." **Review these mistakes** |
| Thin history | evidence under threshold | "Early signal from 6 questions. Let's check it." **Check this skill** |
| Ready | client-built or plan `repair` or `investigate` | as layout. **Start repair** |
| Repaired, check not due | repair done | "You repaired 3 mistakes on Monday. Fresh checks are not available yet." **Practise another skill** |
| No strong weakness | none stands out | "Nothing stands out right now. Mixed practice keeps things fresh." **Start mixed practice** |
| In progress | `resume_session` or a local draft | Resume slot; the card keeps the next move below |
| Verification due | `fresh_check` | Never rendered while the gate is closed |
| Entitlement blocked | quote `access_required` | "NTA-style mode is part of Pro. You can run a Full mock now." **Start a Full mock** |

**Diagnostic and skill check mapping.** "Try a 10-minute diagnostic" is a Quick practice of 10 questions with `purpose=baseline` in the chosen subject. Its cost is whatever the quote says: free once per launch subject (allowance `baseline:<subject>`), then the quote's `creditCost` (10 credits), and the card says which. "Check this skill" is a Quick practice of 10 questions with the chapter set and an ordinary purpose, free when the quote shows the `daily_practice` allowance as available, otherwise the quote's credits. Neither is labelled as measuring ability.

Loading: static skeleton at the card's real height (no shimmer), appearing after 400 ms; Retry shows at 8 s; the cached card shows with "Updated 9:40 PM" while refreshing; a tie never reshuffles the top action. Offline: cached plan with its time; actions that need the network say "Connect to start."

**Why this sheet:** source attempt, counts ("6 wrong, 3 correct, 0 not attempted"), window, "Early signal" explained, link to the student's own answers, the alternatives that ranked lower (`alternatives`). Return after a gap (3 days or more, `returning`): section 6.7. Late night: section 6.8.

Analytics: `next_move_impression` (state, screen), `next_move_reason_opened`, `next_move_started` (action_type, minutes), `next_move_dismissed`, `app_opened`.
Acceptance: golden for each state in light and dark; layout does not jump between skeleton and loaded; the primary key is the only volt element besides the active tab; with the content gate closed, no fresh-check wording appears except the unavailable line; the precedence list is covered by a table-driven unit test; a dismissal expires at 4:00 AM and leaves Review unchanged; the ended-mock slot renders all three copies from fixtures.

### 5.4 Practice setup
Purpose: start a session with honest cost. Data: `GET /api/practice/quote` (re-quote after `expiresAt`, 60 s), `GET /api/subjects`, `/api/chapters`.
- Mode list (rows, not identical cards): **Full mock** "50 questions, 60 minutes", **Quick practice** "5 to 20 questions", **Chapter practice** "Practice, not proof" (this is Quick practice with one chapter chosen: the same mode and the same cost), **NTA-style mode** shown only if the quote returns it; Pro-gated rows show a lock icon and "Part of Pro" with a free alternative, never a price. A "10-minute diagnostic" is not a separate mode: it is Quick practice of 10 questions with `purpose=baseline`, reached from Today and onboarding (5.3).
- **Costs and free paths come only from the quote** (`creditCost`, `creditBalance`, `allowance`), never from constants in the app. Row lines: "Free today" when `daily_practice` is available (one free 10-question Quick practice per IST day for accounts not on Pro), "Free, your first one in Accountancy" for `baseline:<subject>` or `full_sample:<subject>`, otherwise "Uses 50 credits. You have 120." (nothing for Pro).
- **Credits, stated plainly.** New accounts start with 100 practice credits. Quick practice (chapter practice included) costs 10 and a Full mock costs 50, so a free student has two Full mocks or ten Quick practices, and the app has no way to buy or earn more. The code read shows no scheduled refill, so the app never says credits return or renew [CONFIRM: owner decision on a monthly refill, because 100 credits is only two Full mocks]. Mistake Repair draws on a separate explanation wallet (10 a month on a free account, 50 on Pro, renewing on `wallet.resetAt`), not on practice credits.
- Setup: subject chips (44 dp, wrapping), count stepper for quick (5, 10, 15, 20 only), chapter picker (single `chapter` field; never the comma-joined `chapters` parameter [API §2.5]).
- States: loading skeleton; credits low "You have 8 credits. A Quick practice costs 10, and chapter practice costs the same." followed by a list headed "Free right now" naming only paths that are really free: the daily 10-question practice (only when the quote's `allowance.state` is `available`), Learn, Review of your answers and keys (key explanations included) and the five-question sample. Never "Chapter practice is still open" (it is the same cost). Not launchable shows the quote `reason` text only; offline "Connect to start. Your downloaded reviews still work."; error "We could not start the session. Nothing was charged. Try again."; `INSUFFICIENT_PRACTICE_CONTENT` "We do not have enough questions for this yet. Nothing was charged."
- Start: persist `generationKey` locally before sending `POST /api/sessions` with `experience:'practice'` [API §3].
- Mock numbering: "Mock 7" is the number of the student's full or NTA-style attempts in that subject (completed attempts counted by `completedAt`, using `selectionMeta.mode`) plus one for the session being started. Quick practice never takes a number.
- Pre-start sheet for mocks (one sheet, not a wizard): "Mock 7, Accountancy. 50 questions, 60 minutes. 5 marks for each correct answer, minus 1 for each wrong answer. The timer keeps running if you leave the app. Submit ends the mock." In ticket mode (`meta.sessionTicket` present) one more line: "If you leave, open MockMob again before 11:42 PM so your answers can be sent." Quiet line: "For fewer interruptions, turn on Do Not Disturb from Quick Settings." Primary **Start mock**. We do not change system settings.
Analytics: `session_started` (mode, subject, minutes via count).
Acceptance: double-tap Start creates one session (same key); a 402 shows the code-mapped copy, not raw text; the low-credit state lists only free paths the quote or the catalog confirms.

### 5.4.1 Endings for Quick practice and chapter practice
After submit (the same Sending and Received sequence as 5.5; no line says recorded before `POST /api/attempts` returns 200) the student lands on a plain practice result, not the recap: figure "8 of 10 correct" (figure 40), "1 wrong, 1 not attempted", the question strip, per-question rows showing correctness and the key rule of 5.7 (this is where correctness first appears while B13 is not live), and the receipt "Practice finished. Recorded at 11:51 PM. This is practice, not proof." Primary key **Review 1 wrong answer** (wrong answers only; blank ones are listed separately with **Try it again**), or **Practise another chapter** when there are none. Quiet **Finish for now** ends with "Practice recorded at 11:51 PM." and nothing else. No Mobi and no celebration; the week row changing quietly on Today is the only acknowledgment (L0). Chapter practice adds the line "Chapter: Admission of a partner."

### 5.5 Exam focus runner (Full and NTA-style)

Purpose: concentration and trust. Everything needed is visible without a tap.

Layout (360 by 800 dp portrait):
- Top bar 56 dp: "Question 12 of 50" left, timer centre-right (Gabarito 20 tabular; "47:12", "1:02:18" at an hour or more; accessible name "Time left, 47 minutes 12 seconds"), **Questions** key (44 dp) right.
- Save pill row under the bar: left subject and chapter (small ink3), right the save state.
- Progress track 4 dp (answered count of total, instant, ink on sunken, not volt).
- Question region scrolls; long passages scroll within it. Options: 56 dp keys with letter chip; selected is flush plus 2 dp ink border plus check glyph. No correct or wrong colour anywhere.
- Bottom bar 72 dp above the gesture inset: **Previous** (quiet), **Mark for review** (secondary), **Save and next** (primary volt; last question: **Review and submit**).
- System UI: sticky immersive, edge-to-edge, `wakelock_plus` while foregrounded. No Mobi, no feedback, no celebration.

**Save-state truth model** (three states per answer):
1. On this phone: written to the local journal (drift, WAL) synchronously, in under 5 ms, before the UI shows it selected.
2. Sending: cumulative events `PUT /api/sessions` (durable mode), debounced about 400 ms and only when events changed (60/min bucket). Ticket mode skips PUT and holds the ticket locally [API §3].
3. Accepted: `acknowledgedSequence` covers the answer.
Pill copy: "Saved" with check (all accepted), "Saving" with spinner, "3 answers on this phone, waiting for network" (warn, polite live region, announced once). "Saved" is never shown for local-only. Retry back-off 1, 2, 4, 8, 16, then 30 s while the runner is open. Palette cells with unsynced answers carry a hollow dot. In ticket mode the pill reads "On this phone" until submit, because the server holds nothing.

**Clock:** anchor on receipt: `startedRef = receivedAt - max(0, serverNow - startedAt)`, `endsAt = receivedAt + (expiresAt - serverNow)` on a monotonic clock (`SystemClock.elapsedRealtime`); event `at` is integer ms from the monotonic clock, non-decreasing [API §3.4]. Re-sync on resume and every 60 s. Timer is a `ValueListenable<Duration>` in its own `RepaintBoundary`, repainting one Text per second. Warnings at 5 and 1 minutes only: a one-line banner for 3 seconds ("5 minutes left"), one `settle` haptic, a TalkBack announcement, `warnText` plus the words; no pulsing, red flash or sound. At zero the app stops answering, flushes and submits once.

**Palette sheet:** 5 columns of 48 dp cells. Answered: filled ink with number in `ground`; not answered: outlined; not visited: sunken; marked: flag glyph top-right; unsynced: hollow dot bottom-right; current: 2 dp ink ring. Legend with counts: "38 answered, 5 not answered, 7 marked for review, of 50". Submit key at the foot.

**Interruptions:** back opens "Leave this mock?" body "The clock keeps running. Your answers stay in the mock and you can continue until 11:42 PM." Keys **Keep going** (primary) and **Leave the mock** (secondary), warn haptic; never discards. App switch or call: timer keeps running; on return a non-blocking banner "You were away for 2 minutes 10 seconds. The timer kept running." plus either "All answers are saved on the server." (only if all accepted) or "Your answers are on this phone and will be sent when you are online." Process death: the journal restores the same question and selections; Today shows **Continue** with real time left. On `AppLifecycleState.paused` flush unacknowledged answers immediately. Network loss never stops answering. Offline at the deadline: "Time is up. Your answers are on this phone. We will try to send them." and never a promise that they count; the server accepts submit until `expiresAt + 120 s` and in that grace window only acknowledged answers count [API §2.7]; after that "The submission window has ended, so this mock could not be recorded."

**5.5.1 Unattended deadline and the submission window.** Nothing on the phone can be guaranteed to run at `endsAt`: the app may be backgrounded or killed, and Android Doze and WorkManager delay can hold work back. If the student leaves and never returns, nothing submits by itself, and after `expiresAt + 120 s` the server refuses a submit and only acknowledged answers could ever count. So:
1. **Server auto-finalise (B11, a blocker for shipping Full and NTA-style mocks, no longer a [CONFIRM]).** For durable sessions the server finalises the session at `expiresAt` from the acknowledged events and creates the attempt. Without it the app does not ship mocks.
2. **Client flush and submit job.** Flush on pause (above). Schedule a WorkManager one-time job for about 90 seconds before `endsAt` that flushes events and submits (expedited work cannot be delayed, so this is a normal job with an initial delay; Android may run it late, so it narrows the gap and is never the only safeguard). Re-queue it on reconnect until `expiresAt + 120 s`.
3. **Token refresh in the background isolate.** The job runs headless, so it refreshes the Supabase session itself: read the stored session from secure storage, call the Supabase token refresh endpoint with dio, write the new session back under one cross-isolate lock (a lock file in the app's no-backup directory) so the foreground and background isolates never spend the same refresh token twice, retry the request once, then stop and keep `pendingSubmission`.
4. **Ticket mode** (no server copy, so no server finalise): only an app that opens before `expiresAt + 120 s` can send, which is why the pre-start sheet carries the extra line (5.4).
5. **What the student sees.** Today's ended-mock slot (5.3) and a Review row show the three states: recorded ("Mock 7 ended at 10:42 PM. Your 31 answers sent before then were recorded."), being sent, and window closed ("The submission window for Mock 7 has ended, so it could not be recorded. 31 answers were sent before 10:42 PM."). On `SESSION_EXPIRED` the client first reads `GET /api/attempts/{id}`; a 200 means the server finalised it and the result opens, a 404 means the window closed.

**Practice skin (Quick practice, chapter practice and repair retries; no exam timer):** same layout without the timer. Per-answer feedback needs `[NEW-API]` B13, `POST /api/sessions/{id}/check {qid, answer}`, which returns `{correct, keyIndex, explanation}` for practice and recovery experiences only and which the server refuses (403 `check_not_available`) for `full` and `nta`, decided from the session's mode, never from a client flag. A checked answer is final for that question [CONFIRM]. With B13 live: correct shows an ink check and a short reason rising in 220 ms with `settle`; wrong shows the wrong-trio panel with the explanation, no haptic, no shake beyond a 3 px knock. **Until B13 ships (the v1 fallback):** the API gives the app no key or explanation before submit (session views carry no keys, `PUT /api/sessions` returns only `acknowledgedSequence`, and correctness exists only in `GET /api/attempts/{id}`), so Quick practice, chapter practice and repair retries show no correctness while answering, use the same neutral selected state as a mock, say once at the start "Feedback comes after you finish.", and show per-question feedback on the practice result after submit (5.4.1) from the attempt detail and the key rule of 5.7. Only the bundled sample (5.1.3) may show per-question feedback today. No fullscreen reward per question. Mobi appears only on completion states.

**Submit:** last-question key opens the sheet "Submit now? 38 answered, 7 marked for review, 5 not answered. You cannot change answers after you submit." Keys **Submit mock** and **Keep working**. The stages come only from real calls: **Sending** from the tap until `POST /api/attempts` returns 200 (key loading, "Sending your answers"); **Received** the moment it returns 200: "Answers received. Saved on the server at 10:42 PM." (idempotent; retry safe). The 200 body is the scored attempt, so the result is openable at once: the sealed sheet (5.6.2) appears immediately, and `GET /api/attempts/{id}` is only a read for `answerReviews` (5.6.4 covers a failed or `unavailable` read). There is no marking stage, no marking bar and no disabled tab, because the server scores synchronously. Failure or no network: "Your answers are on this phone. We will send them when you are online." with **Try again** and the state "Not on the server yet"; submit retries (`pendingSubmission`) until `endsAt + 120 s`. A silent ongoing notification "Mock 7 in progress" runs while a mock is open and the app is in the background; its states are only in progress, then sending while a background submit is pending. A result-ready notification (section 8) is posted only for a submit that was acknowledged later in the background: "Mock 7 was received. Your result is ready." The attempt id of every received but unopened result is stored locally in `pending_result`, so Today and the Review dot still know it exists after process death.

Analytics: `session_submitted` (mode, subject, count, outcome: submitted or timed_out).
Acceptance (device-gated): leave the app through `endsAt` and confirm Today shows the right ended-mock copy and that the background job refreshes the token; no dropped frame in a 220 ms question change on the real phone; kill the process mid-mock and restore the same question; airplane mode through the deadline shows the exact copy above; golden for each save state; a TalkBack pass reads option, selected state and timer name.

### 5.6 Result: recap reveal ("Open your sheet")

This is the signature moment. It applies to **Full and NTA-style mocks** only. A Quick practice of 5 to 20 questions goes to the practice result (5.4.1) with one summary line. Data: the attempt returned by `POST /api/attempts` (marks derived from `correct`, `wrong`, `unattempted`, `total`), `GET /api/attempts/{id}` for `answerReviews` and `answerReviewState`, `GET /api/me/rhythm`, `GET /api/learning/plan`, the cached attempts list, and the `recap` block `[NEW-API]` (B8: `{tone, previousComparable:{marks,max,attemptId}|null, timingReliable:boolean, formatId}`) on attempt detail.

**Derived values, each defined once in `core/domain` (pure functions with unit tests):**
- **Mock ordinal.** "Mock 7" is the count of the student's attempts in the same subject whose `selectionMeta.mode` is `full` or `nta`, ordered by `completedAt`, up to and including this one. Quick practice attempts never take a number (their title is "Quick practice, Accountancy"). `first_mock` is ordinal 1, not `attempts.length===1`, because the attempts list also holds Quick practice.
- **Comparability.** `attemptOut` has no `formatId`, so the comparison line is hidden until `recap.previousComparable` exists (B8). Full and NTA-style mocks are never compared with each other without it.
- **Mark breakdown (one function, `markBreakdown(correct, wrong, unattempted)`).** `scored = correct*5 - wrong`; `takenOff = wrong`; `notEarnedOnWrong = wrong*5`; `notEarnedOnBlank = unattempted*5`; `lost = takenOff + notEarnedOnWrong + notEarnedOnBlank`. The four parts always sum to `n*5` (scored + lost = 5c - w + 6w + 5u = 5n). Fixture (26 correct, 15 wrong, 9 not attempted): 115 + 15 + 75 + 45 = 250, and lost = 15 + 75 + 45 = 135.
- **Observed chapter breakdown** (client-side, ported from `data/session_recovery.js`): for each chapter in `questionsSnapshot`, with `details`: questions, correct, wrong, not attempted, `marksLost = wrong*6 + unattempted*5` (the same derivation). Sort by `marksLost` descending, then wrong descending, then chapter name, so a tie never reshuffles. A chapter with fewer than 3 questions is never named as the chapter that cost the most; if every chapter is under 3, card 3 lists the wrong answers by question number instead.
- **Repair candidates:** wrong answers (`details[].isCorrect===false`) of the attempt, excluding questions whose review state is `withdrawn`, `under_review`, `content_changed` or `key_changed_unverified`, questions already repaired (local `repair_local` acknowledgments, later B7), and ids the server answered with `not_a_mistake` (hidden quietly and recounted, never shown as an error). Not attempted questions are never candidates: `POST /api/recovery/repair` can return 422 `not_a_mistake` for ineligible items and whether it accepts blanks is UNVERIFIED, so the client never sends one. A blank is a skipped question, not a conceptual error, so it never appears in "mistakes".
- **Repair time estimate:** 3 minutes per mistake, rounded up to the nearest 5 and always written "about" ("3 mistakes, about 10 minutes"). The 3 is a stated assumption [CONFIRM: replace with a measured figure after the pilot]; with zero candidates no time is shown.

**5.6.1 Ritual and decay**
- The student's first three sealed sheets (counted locally as `sheetsOpened`): full swipe-up open with a nudge hint on the first only.
- From the fourth: the sheet is still sealed but opens with one tap (160 ms fade, no travel). Cards remain.
- Always available: **Open without the reveal** on the sheet, **Skip to full result** on every card, You, Feel "Open results directly". After the third open a quiet line appears once on the last card: "Prefer to skip the reveal? Change it in You." Never repeated. **Replay recap** is always on the full result page.

**5.6.2 Sealed sheet** (no Mobi, no waiting state: the sheet is openable from the moment it appears, because `POST /api/attempts` already returned the scored attempt)
- Full-height card, 16 dp margins, 20 dp radius, `raised`, hairline. Top: "Mock 7, Accountancy" (headline); "50 questions, 60 minutes. Submitted at 10:42 PM." and "Saved on the server." (the attempt exists, so this is always acknowledged).
- Middle: the question strip (50 cells, 10 columns) dimmed under the fold; cells uncoloured so nothing leaks before opening.
- Bottom: the **tab**, a volt pill 56 by 200 dp with two grip lines and the label "Open your result", placed 96 dp above the bottom edge, clear of the system gesture bar (read `MediaQuery.systemGestureInsets`) and away from the left and right edges (predictive back). Under it, quiet text **Open without the reveal**.
- **Gesture rule: swipe up always means continue.** The drag follows the finger 1:1 over 180 dp; the top flap lifts with it. `tick` at 25, 50 and 75%. Release at 60% or more completes in 220 ms with one `open` haptic; below 60% springs back in 200 ms with no haptic. Tap on the tab opens with a scripted 220 ms lift and the same haptic. TalkBack: "Mock 7 result, sealed. Button: Open your result", plus a custom action "Open without the reveal".
- First-ever sheet: 1.2 s after settling the tab nudges up 12 dp over 400 ms once (skipped under reduced motion).
- Opening marks the `pending_result` record opened.

**5.6.3 Card sequence.** Vertical stack. Swipe up next, swipe down back (240 ms, transform and opacity; leaving card rises 24 dp and fades, arriving card rises from 24 dp below). Each card has a visible primary key naming what comes next (no arrows) and a **Skip to full result** text button top-right (44 dp). System back goes to the full result. Top: segmented position marker (one segment per card, position not progress to a reward) and "Card 2 of 4" for TalkBack. Each card is a `RepaintBoundary`.

- **Card 1, the marks.** The answer sheet is the anchor, not a hero number alone. Layout at 360 dp: left column "Mock 7, Accountancy, 50 questions" (small), the figure (figureHero 96) "115" and "out of 250 marks"; right column the 50-cell question strip as 5 columns by 10 rows (16 dp cells, 3 dp gaps), each cell carrying a glyph so state is never colour alone (check for correct, cross for wrong, empty for not attempted). At large text scale the strip drops under the figure as 10 columns. Under both, the three count pairs are the strip's legend, each led by its cell glyph: "26 correct", "15 wrong", "9 not attempted", caption "26 + 15 + 9 = 50 questions." Line "5 marks for each correct answer, minus 1 for each wrong answer." If `recap.previousComparable` exists: "Mock 6, same format: 92 out of 250." Never a percentile or "above average". On open the cells fill in question order over 240 ms and the figure rolls 0 to value in 420 ms; TalkBack reads the final value at once; both are skipped under reduced motion and on the lower variant. Key **Where the marks went**.
- **Card 2, where the marks went.** Title "Where the other 135 marks went". A 16 dp stacked bar of four segments totalling 250 (every number from `markBreakdown`), growing 320 ms with 60 ms stagger: scored 115, taken off by wrong answers 15, not earned on wrong answers 75, not earned on blank answers 45. Segments differ by fill pattern (solid, hatched, outlined, dotted), not colour alone. Rows aligned right, tabular: "Scored: 115 marks", "Taken off by wrong answers: 15 marks (1 for each of 15)", "Not earned on wrong answers: 75 marks (5 for each of 15)", "Not earned on blank answers: 45 marks (5 for each of 9)". Caption "Of 250 marks: 115 scored, 15 taken off, 75 not earned on wrong answers, 45 not earned on blanks. 15 + 75 + 45 = 135." Tap "Show the arithmetic" reveals the formula line `26 x 5 - 15 = 115`. Key **The first thing to fix**. Observed loss only, never a forecast. Implementations take every number from server counts through `markBreakdown`, never from the fixture. Unit test: the four parts sum to `n*5`, and the rows sum to 135 on the fixture.
- **Card 3, the first thing to fix.** One pattern, one chapter, from the observed chapter breakdown (not from the plan, which has no source for it while recovery is gated). Title "Start with partnership accounts: admission of a partner". Evidence "This chapter cost the most marks in this mock. 9 questions: 3 correct, 4 wrong, 2 not attempted." Wrong and not attempted are always shown separately, here and everywhere. Question tiles (44 dp) tap through to those answers. "Early signal from one mock." Optional single observation only when supported (for example "3 answers were changed from right to wrong"). Quiet **Why this?**. Mobi 48 dp attentive beside the primary key only (no text). Key **Choose how to fix it**. When the leading chapter has no wrong answers, only blanks: title "Start with the questions you left blank in admission of a partner", evidence "You did not attempt 5 of 9 questions here. Blank answers are not mistakes to repair.", key **Practise this chapter** (Quick practice with the chapter set). When the plan later returns `repair` or `investigate` (B10) it may replace the title; the evidence stays observed.
- **Card 4, what was recorded and the next ask.** Title "Mock 7 is in your record." "Saved on the server at 10:44 PM." (always, since the attempt exists). Rows: "3 wrong answers ready to repair, about 10 minutes." and, when present, "2 not attempted. They are in Review." "Fresh check: not available yet. Repairs are practice, not proof." When the explanation wallet is below the task: "This repair needs 3 explanation credits. You have 2. Start with 2 mistakes, or read the key explanations in Review." Duration chips (5, 10, 20 minutes) set how many mistakes the repair holds (about 2, 3 and 6), capped by the candidates; chips that exceed the candidates are not shown, and with 2 or fewer none are shown. Primary **Start 10-minute repair** (the minutes follow the chip), secondary **Choose something else** (the alternatives sheet of 5.3), tertiary **Finish for now**. Finish ends with "Mock 7 is in your record. Your 3 mistakes are waiting in Review." and nothing else. First-result extra (once, inline, not a system dialog): row "Want a reminder when your repair is due? You choose the time." with **Set a reminder** and **Not now**, which calls the `PermissionRequester` interface in core (implemented by Module 11); only the first triggers the Android permission dialog; a refusal is final until changed in You and never blocks study. Third-reveal line as in 5.6.1. Mobi neutral pose, static.
- **Dropped in v1:** the "How the hour went" timing card (revisit when `recap.timingReliable` exists), the paper sound, the volt underline sweep.

**5.6.4 Outcome variants** (the server decides; the app never decides what is poor). Held is defined only from real states: `answerReviews` entries and `answerReviewState`; there is no "grading pending" state in the API.

| Variant | When | Behaviour |
|---|---|---|
| default | no tone or neutral | Standard sequence |
| first_mock | mock ordinal is 1 | Greeting Mobi on card 1; "No earlier mock to compare."; card 3 "Early signal from one mock."; no celebration |
| held | any `answerReviews` entry whose state is `withdrawn`, `under_review`, `content_changed` or `key_changed_unverified` | Sheet opens; card 1 shows "Marks held": "2 questions are being checked. Your marks will update here, and we will tell you." No figure; card 2 hidden; card 3 only from questions that are not under review; `settle` only |
| keys unavailable | `answerReviewState==='unavailable'` | Treated as no keys shown: the figure and counts (from the attempt) still show with the line "We could not check for answer-key updates just now. Your marks may change." and **Try again** on card 4; no key or explanation anywhere until the read succeeds |
| lower `[NEW-API]` | `recap.tone==='lower'` | Figure in `ink`, no roll, no Mobi on cards 1 and 2; line "Your result is ready. Start with one repeated pattern."; extra quiet key **Show me the first thing to fix** (jumps to card 3, can return); card 3 leads with more space; `open` haptic only, no ticks. Thresholds are an owner decision [CONFIRM]; until `recap.tone` exists the app renders default |
| higher `[NEW-API]` | `recap.tone==='higher'` | Comparison "Mock 6: 92 out of 250. Mock 7: 115 out of 250."; one Mobi hop on card 1 after the figure settles; no underline, no confetti; card 2 still shows where marks went |

Gated-check line on card 4 appears in every variant. When a held result resolves and marks change, the full result says "Your marks changed from 112 to 117 after two answer keys were corrected" (annotation, never silent rewrite) and the recap is re-offered once.

**5.6.5 Result-ready notification:** only for a submit that was acknowledged later in the background ("Mock 7 was received. Your result is ready."); posts silently inside quiet hours (section 8). In the foreground nothing is announced: the sealed sheet is already there, because there is no marking stage.

**5.6.6 Repeat visits:** reopening an old result goes to the full result, never the seal. A top-bar text button **Replay recap** replays the cards without the tear. If the student left before card 4, a chip "Continue recap, card 3 of 4" shows; completing card 4 clears it.

Analytics: `result_opened` (mode, variant), `recap_opened`, `recap_skipped` (screen: card number), `finish_for_now`.
Acceptance: the sheet never withholds the result (button, TalkBack action and skip all work); poor variant golden has no volt figure and no Mobi on 1 and 2; the `markBreakdown` unit test passes (parts sum to `n*5`, rows sum to 135 on the fixture); card 1 shows the strip beside the figure and wrong and not attempted are never merged on any card; reduced-motion run shows every figure at once; the tab is reachable with one thumb at 360 by 640.

### 5.7 Full result
Purpose: complete, readable result without the ritual. Order (Lab order): summary (figure, counts with denominators, arithmetic from `markBreakdown`), Score Recovery Lab (where marks went, first fix from the observed chapter breakdown), answer by answer (collapsed rows, first wrong opens, wrong answers lead with Mistake Repair; not attempted questions are listed separately and have no repair key). Key rule: mark the correct option only when there is no review or `review.state==='corrected'` and `currentIndex===j`; any non-corrected review shows no key and no explanation, and `answerReviewState==='unavailable'` means no keys or explanations at all [API §2.8]. Dwell times only when `telemetry==='self_reported'` and `scoringVersion` is server. Question strip with right, wrong, blank, changed cells; repaired cells carry the repair mark (section 6.4). States: loading skeleton, held (5.6.4), corrected (annotated), error "We could not load this result. Your result was recorded. Try again.", offline from cache with "Showing what was last loaded at 10:44 PM."

### 5.8 Review list and Mistake Repair
Three sections: **Mistakes to repair** (wrong answers grouped by chapter; row shows question number, chapter and when found; a separate quiet group "Not attempted (2)" lists skipped questions with **See the answer** and **Try it again**, never a repair key), **Your record** (repair timeline), **Past results** (each with Replay recap). A result that was received but not opened shows as the first row with "Mock 7 was received. Your result is ready." Data: cached attempts list plus `GET /api/recovery/repair` results; `[NEW-API]` `GET /api/me/repair-record` for the cross-device record (fallback: derive from attempts and locally stored repair acknowledgments in `repair_local`, labelled "On this phone" when not server-backed). Candidate rules are in 5.6 (repair candidates).

**Repair record (timeline, not a binder):** each mistake is a row on a vertical 2 dp thread with three square nodes in words: Found, Repaired, Checked on fresh questions. Row: "Q11, admission of a partner. Found on 12 October, 10:42 PM. Repaired on 12 October, 11:08 PM. Checked on fresh questions: not available yet." Nodes fill with ink and a check glyph, not volt. The third node stays hidden-as-text until the gate opens; header line "Fresh checks are not available yet. Repairs are practice, not proof." No pile, no totals line, no filing animation. Status words only: "practised", "fresh check completed", "retained on a later check". When checks go live: "7 of 10 on fresh questions. Earlier check: 4 of 10" with date and sample size, shown only with at least 8 items. A pattern seen again is annotated ("Seen again on 14 October"), history never rewritten.

**Repair flow** (`POST /api/recovery/repair {attemptId, questionId, requestId}`; reuse `requestId` on retry; costs 1 explanation-wallet credit per mistake, so the entry screen says "Uses 1 explanation credit for each mistake. You have 9." from `/api/ai/credits`, and when the balance is below the number of mistakes: "This repair needs 3 explanation credits. You have 2. Start with 2 mistakes, or read the key explanations."):
1. Entry (plain screen): "3 mistakes from Mock 7, about 10 minutes. You can stop after any one." Key **Begin**.
2. Per mistake: the original question, the student's answer and the correct answer in a calm panel (`chosenIndex`, `keyIndex` from the repair response); "What happened here" (observed pattern in one or two sentences, from `why_tempting`, `why_wrong`; never a statement about ability); worked explanation (`key_idea`, `next_step`). Then an optional retry (see below).
3. Keys **Next mistake** or **Finish for now** at any point. Progress "1 of 3 mistakes" (real work). A mistake the server answers with `not_a_mistake` is removed from the list without an error and the count updates.
- **The retry.** `practiceHref` is mapped to a native practice start. Sessions have a server minimum of 5 questions, so the retry is a Quick practice of 5 questions in the same chapter, a separate practice session with its own quote and cost (10 practice credits, or free when the quote shows an allowance) and its own receipt, "Practice finished. Recorded at 11:40 PM." Because B13 (`POST /api/sessions/{id}/check`) may not exist, the retry follows the practice skin fallback of 5.5: no feedback while answering and correctness on the practice result after submit. When practice credits are below the cost, the retry key is replaced by **Finish without a retry**. A retry is optional and is not needed for the mistake to count as repaired. Right or wrong in the retry never changes the repair record; a wrong retry only appears as a note in the result.
- **No-AI fallback.** When the wallet is empty (402 `insufficient_ai_credits`), the repair is paused (503 `paused`) or the explanation cannot be made, the screen shows "Answer review" built from the attempt detail: the student's answer, the correct answer, and the key explanation from `questionsSnapshot`, only when the key rule of 5.7 allows a key, labelled "Key explanation. No explanation credit used." It is not counted as a repair and the mistake keeps its place; the row is marked "Reviewed" and "On this phone". With the wallet reset date known: "Explanation credits renew on 1 November."
- Outcomes: `explained`, `stored` (free reopen), `held_for_recheck` ("We are checking this question's answer key. It is set aside for now and you were not charged."), `not_explained` ("We could not explain this one. You were not charged. Try another."). Errors map by code: 402 "You have used this month's explanation credits." followed by the no-AI fallback above and the renewal date when known; 409 states per code; 422 `not_a_mistake` hides the item; 429 "Please wait a minute."; 502 and 503 "The explanation could not be made. Try again."
- **What counts toward the week (read from `rhythm.js` and `appPrefs.js`, not decided by the client).** The server counts a repair activity for each `ai_credit_reservations` row that is committed with a stored repair, which is each acknowledged `explained` response. A `stored` reopen, `held_for_recheck` and `not_explained` add nothing. The retry session counts like any server-scored session when its `POST /api/attempts` returns 200 (any mode, including Quick practice; the 5-answer floor is B2 and does not exist yet). No endpoint marks a whole repair finished: the per-mistake `POST /api/recovery/repair` acknowledgments are the only records of the repair, and `POST /api/attempts` records the retry.
- **Ending** (one screen, 320 ms entrance): the question strip at the top; repaired cells gain a small ink corner mark over 240 ms (the signature mark, not volt); headline "3 mistakes repaired."; line "This was practice. Fresh-question checks are not available yet, so this does not show that it holds."; receipt line "Repair finished. Recorded at 11:51 PM." where the time is the acknowledgment time of the last acknowledged `POST /api/recovery/repair` (only after the server acknowledges; before that "On this phone. Not recorded yet."); keys **Repair 3 more mistakes** (only if more exist, with count and time) and quiet **Finish for tonight**; `open` haptic once; Mobi one 400 ms hop (500 ms for the first repair ever with the line "This is your first repair."). The headline counts only mistakes whose repair call was acknowledged as `explained` or `stored`. If a retry was wrong: "3 mistakes worked through. Two retries were still wrong. They are in Review for another go." The ending makes no claim about the week; the week row on Today updates from `GET /api/me/rhythm`.
- Share card (optional, after a finished repair or met goal): private preview first, text only "I finished 3 repairs this week on MockMob." No marks, wrong answers, weak chapters or counts of other students.

Analytics: `repair_started`, `repair_completed` (count).
Acceptance: eligibility errors never lose the student's place and `not_a_mistake` hides the item silently; a `held_for_recheck` outcome never counts as repaired; Checked node reads "not available yet" in every golden; the empty-wallet state shows the no-AI fallback and the renewal date; the receipt time equals the last repair acknowledgment.

### 5.9 Learn
Purpose: short recall cards and chapter study. Data: `GET /api/study/catalog`, `/api/study/runs`, `/api/study/units/{id}` (GET records exposure, do not prefetch), preferences.
- Due summary: "12 cards due." (a count from `queue.dueCount`; the catalog gives no minutes or due dates, so neither is claimed). Empty: "Nothing is due right now." No streak. A due date or "about N minutes" returns only if a `[NEW-API]` field (for example `queue.nextDueAt` and a per-card time) is added.
- Lessons: unit list with `status` words: new "New", in_progress "In progress", lock_in "In progress", due "Due", learned "Done for now"; never "mastered".
- Recall card: tap to reveal (200 ms fade and 8 dp rise, no 3D flip); auto-graded types answer inline; self-rated cards show four keys **Forgot**, **Hard**, **Got it**, **Easy** (ratings 1 to 4). One pending event per run is persisted across app kills with its `requestKey` and `expectedRevision`; a second offline step waits ("Reviewed offline, sending when online") until acknowledged. Offline packs: per-subject **Keep for offline** toggle with the size ("4.2 MB"); lesson content cached by `id + version + contentHash` and dropped on change. Offline review is never a scored attempt.
- **Run ending.** When the run `state` is `complete` and the last event is acknowledged: "Run finished. 8 cards reviewed. Recorded at 6:12 PM." (only after the server acknowledges; before that "On this phone. Not recorded yet."). The student sees how many cards are still due from a fresh catalog read ("4 cards are still due"), or nothing if none. Primary **Back to Learn**; quiet **Finish for now**. No Mobi, no celebration, no streak; an `invalidated` or `set_aside` run ends with its own plain line instead. Route: `/learn/run/:runId/done`.
- States: disabled (`state:'disabled'`) "Learning is not available right now."; `DAILY_NEW_LIMIT_REACHED` "You have done today's new cards. Review is still open."; `NOTHING_DUE` as empty; `STUDY_CONTENT_CHANGED` replaces the run with "This lesson was updated. Opening the new version."; conflicts retry silently once.
Analytics: none beyond `app_opened`.
Acceptance: kill the app mid-run and resume with no double event; offline pack opens in airplane mode; the due summary shows no minutes or dates; every `UnitView.status` value maps to a word.

### 5.10 You (hub)
Rows (list, not cards): Weekly goal and rhythm, Repair record, Milestones, Personal bests, Notifications, Appearance and feel, Privacy, Account, Help. "CUET tools" (Compass, Combo Planner) open in a Custom Tab.

### 5.11 You: rhythm, goal, record, milestones, personal bests
See section 6 for rules. Layout: the week strip (36 dp marks), rows "Weeks in rhythm: 3", "Best run: 6 weeks", "Goal: 4 days a week" with **Edit goal**, **Pause rhythm** (presets "This week", "2 weeks", "Until I turn it on", maps to `pausedUntil`), a quiet **Turn off rhythm** (hides the strip everywhere; records stay). Closed weeks as hairline rows "Week of 5 October, 4 of 4 days." (read from the B2 `history` array; hidden until it ships) Milestones as dated rows. Personal bests row, hidden when the server does not return a format id.

### 5.12 You: notifications, usage data, account

**5.12.1 Notifications** (section 8 for rules). Rows: Allow notifications (system state), channels (Result ready, Study window, Weekly plan, Check due hidden until gate opens), study window, Quiet hours (start and end, 12-hour pickers, default 11:00 PM to 7:00 AM, editable), weekly cap, "Mute for 7 days". A study window inside quiet hours shows inline "Your 11:30 PM reminder falls inside quiet hours. Move one of them." and is never overridden silently. Data: `GET/PUT /api/me/notification-prefs` (24-hour strings on the wire).

**5.12.2 Appearance and feel:** Theme (Match phone, Light, Dark), Reduce motion (follows system), Touch feedback (on), Open results directly (off), Late-night lines (on).

**5.12.3 Privacy: usage data (exact).**
- Visible to everyone as a row; the switch is available only to a self-declared adult.
- Adult row: switch label exactly **Allow usage data to improve MockMob**. Explanation: "We count which parts of the app are used, such as starting a mock or finishing a repair, along with the app version. We do not collect your answers, marks, questions, contacts, location or an advertising ID. Nothing goes to ad or analytics companies. You can turn this off any time here and collection stops straight away." Link **See every event we collect** lists the allowlisted event names in plain words. Turning on: `PUT /api/me/consent {ageBand:'adult', analyticsAllowed:true}`. Turning off: `analyticsAllowed:false`, then the confirmation "Usage data is off. We stopped collecting it. Earlier usage data was deleted." shown only after the PUT returns and `deletedEvents` is reported; on 503 "Your choice was saved, but deleting earlier data failed. Try again." Withdrawal clears the local event queue before the call.
- Minor or unknown: row reads "Off for your account." with no switch and no prompt. Changing the age answer: **Change my answer** re-asks "Are you 18 or older?"; choosing No or Prefer not to say writes `analyticsAllowed:false`.
- The same switch card (the switch with the exact label, off, plus a single **Done** key) is shown after the first completed result as an inline dismissible row and, for adults, in the optional "Before you start" sheet (5.1.6); Done with the switch off changes nothing and is final until the student opens You. Operational data (sessions, scores, notification tokens, entitlements) is described separately in the privacy text; Play Console vitals are not controlled by this switch and the text says so. FCM tokens are declared in the Play Data safety form [CONFIRM owner and legal review of the wording and the 30-day deletion statement].
- **Queue and account edges:** every queued event is stored with the user id it was created under; on sign-out and on account switch the queue is deleted, and a flush sends only events whose user id equals the signed-in user, so an adult's events can never post under a minor's account. If the consent GET fails or has not loaded, analytics is treated as off (nothing is queued or sent). Besides the allowlisted props the event schema accepts only `platform` and `app_version` [API §2.2], so the copy says "app version" and the client sends no OS version; adding the Android version would first need the server allowlist to change. Firebase: Module 0's manifest sets `firebase_analytics_collection_enabled` and `google_analytics_adid_collection_enabled` to false, so only Messaging is initialised, after the first frame.
- Default ON for consenting adults is interpreted as: on only after the adult confirms by an explicit action (the switch is off until they choose Allow). [CONFIRM]

**5.12.4 Account:** email, "Pro is active until 31 July 2027" or "Not on Pro" read from `/api/auth/me` (`isPremium`, `premiumUntil`), with no price or purchase link and "Pro bought on mockmob.in is honoured here." **Sign out**: confirm, clears tokens and local drafts after warning if answers are unsent ("3 answers are on this phone and not sent. Sign out anyway?"). **Delete account**: screen "Delete your MockMob account" with consequences "We delete your account and study records within 30 days. Payment records required by law are kept. You will be signed out." Key **Request deletion** (destructive, warn haptic); `POST /api/me/delete {source:'android'}`; show the returned message; sign out locally only after success (idempotent on repeat: "Your request is already with us."). **Help:** support@mockmob.in, "MockMob is not affiliated with NTA or Delhi University", version.

Acceptance (5.10 to 5.12): withdrawal stops event posting before the network call returns; golden for consent adult, minor and unknown; the exact switch label appears once and unaltered.

---

## 6. Gamification rules

Attention budget per surface: Today one element (the week row); practice setup zero; timed answering zero; recap at most one celebration level plus the receipt; Review's content is the record; You is the only dense surface. A new mechanic may be added only by retiring one or after an experiment.

### 6.1 Weekly rhythm and the supportive streak
- **Source of truth:** `GET /api/me/rhythm` and `GET/PUT /api/me/goal` [API §2.3]. The goal unit is **study days per week** (`daysPerWeek` 1 to 7, default 4), because that is what the server supports today; the judges' preference for counting repairs is recorded as `[CONFIRM]` and needs a backend change (B2).
- **What counts (read from `rhythm.js` and `appPrefs.js`, 12 October 2026):** a local calendar day in the student's timezone on which the server recorded either (a) a server-scored attempt (any mode, including Quick practice, as long as its `scoringVersion` is a server version), or (b) a repair, which is a committed `score_recovery_repair` reservation holding a stored repair, one per acknowledged `explained` response. Backend module B2 adds a floor of 5 answered questions for a scored session so one tap cannot count; until B2 ships the app does not claim the floor in copy.
- **Data the endpoint does not return today:** `GET /api/me/rhythm` returns only the current week's `studyDayDates`, plus `weeksMetStreak`, `bestRun` and `milestones[]`. So the app cannot read closed-week rows, past-week counts, a week-just-closed event, the previous streak value, repairs or mocks this week, or a stable id for a repair-finished or week-closed celebration. **`[NEW-API]` B2 extension** adds to the rhythm response: `history` (array of `{weekStart, studyDays, goal, met}` for the last 12 weeks, so past weeks keep the goal they were held to), `repairsThisWeek`, `mocksThisWeek`, and `lastClosedWeek` (`{id: weekStart, studyDays, goal, met}`, a stable id). **Until it ships** the app hides closed-week rows and the weekly summary counts ("2 mocks, 7 mistakes repaired", "2 repairs finished"), and keeps two local records in `rhythm_seen`, stated as best effort: `lastSeenWeek` (`weekStart`, `studyDays`, `daysGoal`, `metThisWeek`, `weeksMetStreak`, written after every successful rhythm read) and `lastCelebratedWeekStart`. A week is treated as just closed when the current `weekStart` differs from `lastSeenWeek.weekStart` by exactly one week; it closed as met when `lastSeenWeek.metThisWeek` was true; a run ended when `weeksMetStreak` is lower than `lastSeenWeek.weeksMetStreak`. If the app was not opened in that week's final state, the app shows nothing rather than guess. Celebration ids: milestones use `milestones[].id`; a repair finished uses the local id `repair:<attemptId>:<first acknowledged requestId of the run>`; a closed week uses `week:<weekStart>` (the server's `lastClosedWeek.id` once B2 ships), checked against `lastCelebratedWeekStart`.
- **Week boundary:** Monday to Sunday in the student's timezone (`timeZone` from notification prefs, default Asia/Kolkata, IST). The client never computes week boundaries; it renders `weekStart`, `studyDayDates`.
- **Rest days:** every non-study day is a rest day; no marking needed. Copy in the editor: "The other days are rest days."
- **Pause:** `pausedUntil`; paused weeks do not break the run. Copy "Rhythm is paused until 26 October." Strip shows words, not colour alone.
- **Weekly strip on Today** (one compact row, 44 dp tall): seven 28 dp circles with weekday initials; a study day is an ink-filled circle with a 2 dp check, today has a 2 dp ink outline, other days are hairline circles; left text "2 of 4 study days"; met: "4 of 4 study days. This week is done."; extra days "5 days this week". No flame, no numeric badge, no volt. Tap opens the week sheet. Stale: "As of 9:15 PM". Unavailable: "We could not load this week." with **Try again**; no count shown. The painter is owned by Module 0 (core); the rhythm module only composes it.
- **Streak language:** the number shown is "Weeks in rhythm: 3" (`weeksMetStreak`), never days. Best run is kept (`bestRun`). When a run ends (detected as above): "A new run starts this week. Your best is still 6 weeks." never "0", never "you lost". No consecutive-day counter, no flame, no repair or freeze of a streak.
- **Restart copy (returning is true):** "Welcome back. Pick up with a small next step." (section 6.7).
- **Close-week forgiveness** (a week at goal minus 1 carries the run) needs an owner-approved server change; not v1.
- Metric to retire it: pause or turn-off above 25% within 4 weeks, or no lift in completed repairs per active week.

### 6.2 Celebration scale
Each celebration is triggered by a server fact with a stable id and fires once (id remembered locally and checked against `milestones[].achievedAt`). Repair finished and week closed have no server id today and use the local ids of 6.1 until B2 ships.

| Level | Moment | Response |
|---|---|---|
| L0 | Any answer recorded, any step | Text only |
| L1 | Repair finished, a week closed as met | Repair mark on the sheet, one `open` haptic (repair) or a 500 ms ring sweep (week), receipt line |
| L2 | First repair ever, first full mock submitted, first week met | L1 plus one Mobi hop (400 to 500 ms) and one plain sentence; the first full mock appears as a text milestone row only, never tied to the score |
| L3 | First fresh check completed, 4 weeks met | A dated row fades into the milestone timeline; fresh-check milestone stays hidden while the gate is closed |

Suppression: no celebration on a first mock, a lower result, a held result or after a failed repair. At most one celebration per session end. No confetti, no particles, no sound anywhere in v1. Settings: Celebrations Full, Quiet (L0 and L1 as text) or Off.

### 6.3 Mobi matrix
| Moment | Mobi |
|---|---|
| Splash, sample choosing, timed mock, submit and wait, sealed sheet, repair feedback | Absent |
| Welcome | Greeting 96 dp, one 420 ms settle |
| Sample explanation | 40 dp hop (correct) or nod (wrong) |
| Today new user, return after 10 days | Greeting once |
| Recap card 1 | first_mock greeting; higher variant one hop; absent on lower |
| Recap card 3 | Attentive 48 dp, static |
| Recap card 4 | Neutral, static |
| Repair finished, weekly goal met | One hop, 400 ms (500 ms for firsts) |
| Empty and error states | Settles once |
Reduced motion: static pose.

### 6.4 Repair record
Defined in 5.8: a timeline of Found, Repaired, Checked, with Checked reading "not available yet". The mark on the sheet cell is ink with a corner notch, never volt.

### 6.5 Milestones (dated rows, not a badge wall)
From `milestones[]` [API §2.3]: first scored session, first full mock, first repair, 5 repairs, 10 repairs, 25 repairs, 10 sessions, first week met, 4 weeks met. Shown as plain rows "First repair finished on 9 October" with a small check. No milestone depends on question counts, none appears for a poor outcome, none unlocks anything. `[NEW-API]` additions later: "first fresh check completed" (hidden until the gate opens) and "first repair after a break" (only when `returning` was true).

### 6.6 Personal bests
Shown only when the server supplies a comparable `formatId` (same template, subject, duration, count and scoring version, first unassisted exposure) `[NEW-API: recap.formatId and GET /api/me/bests]`. Copy: one attempt "First full mock saved. A second one will show your change."; two or more "Best on this mock type: 142 of 250 marks. Latest: 131 of 250 marks." Observed marks with denominators; no percentile; an L1 text acknowledgment only; hidden by a You setting. Retakes of seen papers never count.

### 6.7 Returning
- After 1 day: no fanfare. A quiet line "Last night: 3 mistakes repaired. 3 are waiting." (from repair acknowledgments on this phone until B7 exists) One notification at most, inside the study window, only if the task is still valid; cancelled if the repair is done first.
- After 3 or more days (`returning`): Mobi greets once; "Welcome back. Pick up with a small next step."; duration chips default to 5 minutes ("You have 5 minutes" is a legitimate restart); "Your last mock was Mock 7 on 2 October. Your 3 mistakes from it are still here."; the week strip shows past weeks with real counts only when the B2 `history` array exists (otherwise just "Nothing was lost."); the next move is marked stale with an offer of short mixed practice. No guilt countdown, no escalating notifications, no "we miss you".

### 6.8 Late-night lines
Between 11 PM and 7 AM (the quiet-hours default), duration chips default to 10 minutes and after a finished session the ending adds "That is a good place to stop for tonight." Once per night, dismissible, off in settings. Never blocks anything and never repeats. The 1 AM to 5 AM clock line is not shipped.

### 6.9 Weekly ending
First open after the week closes (Monday) shows one dismissible Today card; an optional push on Sunday at the student's study window. Met: "You finished 4 study days this week. Fresh checks are not available yet." (the counts "2 mocks, 7 mistakes repaired" are added only when B2 returns `mocksThisWeek` and `repairsThisWeek`) Keys **Keep 4**, **Try 5**, **Take a lighter week**. Not met: "You finished 2 of 4 study days. Nothing is lost. Your record is as you left it." Keys **Keep 4**, **Make it 2**, **Take a rest week**. A rest week suspends the goal with no message next Sunday. Bounded summary, no verdict, no comparison with other students.

### 6.10 Anti-patterns we will not ship
XP, gems, coins, levels, hearts or lives, daily-streak counters with flames or freezes (earned or paid), variable-ratio or random rewards, daily login bonus, leaderboards and leagues, "mastered" badges, a fullscreen reward per question, loss-framed notifications ("your streak ends tonight"), public weakness display or default marks sharing, confetti, badge walls, collectible pile of repair cards with totals, hoarding mechanics, celebration after a poor result, pressure copy about the exam date, and any mechanic added without retiring one.

---

## 7. Receipt line (cross-cutting motif)
Every finished task ends with one plain line stating what was recorded and when, shown only after server acknowledgment: "Mock 7 saved on the server at 11:42 PM.", "Repair finished. Recorded at 11:51 PM.", "Practice finished. 8 answered. This is practice, not proof." Before acknowledgment the line reads "On this phone. Not recorded yet."

---

## 8. Notifications

- **Permission timing:** after the first result is opened and closed, via the inline recap row (5.6) or a pre-prompt sheet "Remind me when it matters" listing the channels with an example each; then the Android 13+ system dialog. **Not now** is a full-width quiet key; the sheet returns after 14 days at most once. Refusal never blocks study.
- **Channels** (created at first value, not install): Mock in progress (low, silent, ongoing; states are only in progress and sending), Results ready (default; only for a submit that was acknowledged later in the background), Study reminders (default; the student's study window), Weekly plan (low; off by default), Fresh checks (created only when the content gate opens), Account and safety (default). Prefs map: `result_ready`, `study_window`, `weekly_plan`, `check_due`.
- **Copy:** "Mock 7 was received. Your result is ready." "Your repair is ready: 3 mistakes, about 10 minutes." "Your week is ready to look at." (future) "Your inference check is ready: 5 fresh questions, about 6 minutes." Actions: **Start**, **Not tonight**, **Mute for 7 days**. No streak, guilt, pet or admission wording.
- **Quiet hours:** default 11:00 PM to 7:00 AM, editable (12-hour pickers; wire format 24-hour). Reminders that are not a response to the student's own action wait until 7:00 AM and are dropped if stale. A result-ready post for the student's own submit arrives silently (no sound, vibration or heads-up) [CONFIRM]. The ongoing silent status is unaffected. Quiet hours govern notifications only, never studying.
- **Frequency cap:** one push a day, 3 a week by default (server `weeklyCap`, API default 5 [API §2.3]; confirm), one push per due item ever, none escalating. After 3 ignored in a row a category stops and the app says once "Want fewer reminders? You can turn this one off." After 7 days of silence at most one message in the study window, then nothing until return.
- **Cancellation:** cancelled when the task is done, invalid, dismissed or past validity (fresh check 7 days).
- **Mechanics:** local notifications first (`flutter_local_notifications` + `timezone`, inexact scheduling only, no `SCHEDULE_EXACT_ALARM`); FCM push once the server sender exists (G4, B5). Token upload via `POST /api/me/devices` after permission is granted and the first frame has rendered; `DELETE` on sign-out.

---

## 9. Widget and app shortcuts (Phase 4, after the recap works)
- **Widget:** native `AppWidgetProvider` with RemoteViews via `home_widget`; data in SharedPreferences written after each server-confirmed sync plus a 6-hourly WorkManager refresh. 4 by 2: "Next step", the title, "8 questions, about 10 minutes", the week "2 of 4 study days", age "Updated 8:05 PM"; tap opens the task via App Link. 2 by 2: ring and title. No exam countdown unless a confirmed date exists. Signed out "Sign in to see your next step." Offline shows the last confirmed state with its time. Day and night resources, system corner radius, no gradient, no animation.
- **Shortcuts** (`quick_actions`, max four): **Resume mock** (only while one is in progress), **10-minute repair**, **Saved mistakes**, **Fresh check** (only when the gate is open).
- Adaptive icon: volt `#D2F000` background, mark `#0B1000` inside the 66 dp safe zone, monochrome layer for themed icons. Notification small icon: flat white silhouette; accent voltEdge.

---

## 10. Offline and sync semantics

State words used everywhere: **On this phone** (local pending), **Sending**, **Saved on the server** (accepted). Local pending is never called saved.

| Surface | Offline behaviour |
|---|---|
| Today | Last plan with "Updated 9:40 PM"; never presented as fresh |
| Review and results | Cached read-only with a cache-time banner "Offline. Showing what was last loaded." (32 dp strip under the status bar, never covering controls) |
| In-progress mock | Continues; answers on this phone, re-sent on reconnect; submit waits for network and is allowed until `expiresAt + 120 s` |
| Start practice or mock | Not offline: "Connect to start. Your downloaded reviews still work." |
| Learn | Downloaded lessons and recall work; one queued event per run |
| Sign-in, account changes, delete | Not offline |
| Analytics | Queued only while consent allows, tagged with the user id; deleted on withdrawal, sign-out and account switch; stop when the server returns `collecting:false`; off when the consent read fails |

Implementation: SQLite via drift (tables `answer_journal`, `outbox`, `session_draft`, `cached_plan`, `cached_attempts`, `learn_cache`, `review_log`, `analytics_queue` with a `user_id` on every row, `pending_result` {attemptId, receivedAt, openedAt}, `repair_local` {attemptId, questionId, requestId, status, ackedAt}, `rhythm_seen`, `dismissals`). Every write carries an idempotency key (`generationKey`, `requestKey`, `requestId`, `event_id`) reused across retries. WorkManager flushes the outbox on reconnect and an expedited job covers a backgrounded submit. Connectivity is not trusted from the radio flag alone: a failed request plus a light ping only while work is pending drives the offline state. Never claim offline capability in product copy until proven on the real device.

**Focus-mode resilience:** journal write before UI selection; flush on `paused`; restore after process death; monotonic clock; back guard; wakelock; immersive mode; the leave guard never discards; Do Not Disturb is suggested, never changed.

---

## 11. Accessibility and performance budgets

Accessibility:
- TalkBack: every control named; headings correct; reading order logical; swipe gestures always paired with a button and a custom action. Options form a mutually exclusive group ("Option B, text, selected"). Timer is not a live region; announcements at 5 and 1 minutes through `SemanticsService.announce`. Save pill is a polite live region announcing changes only. Palette cells read "Question 12, answered, marked for review, on this phone". Charts have a table equivalent.
- 200% font scale: only minimums, no fixed heights; layouts scroll with the primary action pinned; sheets become full pages at scale 1.5 or more with a visible Close; test at 1.0, 1.3, 2.0 on 360 by 640. Long chapter names never truncate.
- AA contrast at final size; focus ring 2 dp; state never by colour alone; reduced motion honoured; display size and bold text honoured; haptics, sound and motion never the only carrier of information.

Performance targets (validate in profile mode on the real phone once confirmed):
| Metric | Target |
|---|---|
| Cold start to first Flutter frame | at most 1.5 s |
| Cold start to usable Today skeleton | at most 2.0 s typical, 3.0 s worst |
| Warm start | at most 0.7 s |
| Frames (60 Hz) | build and raster p90 at most 12 ms; under 2% over 16.6 ms in tab switches and scrolling |
| Exam question change | build at most 8 ms, no dropped frame in 220 ms |
| Memory | at most 180 MB PSS on Today, 250 MB peak |
| Download (arm64 split from AAB) | at most 15 MB; installed at most 45 MB |
| Fonts | at most 350 KB |
| Timer | one Text repaint per second, nothing else rebuilds |
Techniques: R8, `--split-debug-info`, `--tree-shake-icons`, ABI splits (keep arm64-v8a and armeabi-v7a), min SDK 24 target, no `BackdropFilter`, `RepaintBoundary` on timer, keys, tabs and recap cards, `const` constructors, `ListView.builder`, static skeletons, defer Firebase and database open until after the first frame, parse payloads over about 50 KB in an isolate, Riverpod `select`. Measure Impeller against Skia in profile mode and ship the lower-jank one. `GET /api/attempts` is an unpaginated dump: fetch once after sign-in and after submit, cache in drift, parse in an isolate (B4 adds a slim paged list).

---

## 12. Build breakdown

### 12.1 Flutter package structure
```
android/                       package in.mockmob.app, flavors none (debug/release)
  app/src/main/AndroidManifest.xml     Module 0 only (all permissions, App Links filters, widget receiver, FCM service, shortcuts meta-data pre-declared)
  app/src/main/kotlin/in/mockmob/app/platform/        Module 12 files (widget provider, shortcuts glue)
  app/src/main/kotlin/in/mockmob/app/notifications/   Module 11 files (FCM service, channels glue)
  app/src/main/res/xml/                                widget info and shortcuts: Module 12 files
lib/
  main.dart
  app.dart                     MaterialApp.router, theme, locale
  core/
    theme/        tokens, colors, typography, theme extension, key_button, widgets
    motion/       motion.dart, reduced_motion.dart
    haptics/      haptics.dart
    router/       routes.dart (every route, 4.2), router.dart, action_router.dart (web href to native)
    api/          dio client, bearer interceptor, refresh-once, error parsers per family, models
    auth/         session store, supabase wrapper, auth state, background-isolate token refresh with lock
    storage/      drift database, secure storage, prefs
    repositories/ consent, notification_prefs, goal, session_draft, pending_result, rhythm_seen, dismissal, repair_local (interfaces and implementations; features only consume them)
    permissions/  PermissionRequester interface (Module 11 provides the implementation)
    domain/       marks.dart (markBreakdown), mock_ordinal.dart, chapter_breakdown.dart, repair_candidates.dart (ported from session_recovery.js; pure, unit tested)
    analytics/    consent-gated client, queue tagged by user id, event allowlist
    notifications/ service, channels, scheduler, quiet hours
    connectivity/ pending-work aware connectivity
    sync/         outbox, idempotency keys, workmanager entry and callback dispatcher
    widgets/      skeleton, state views, sheets, banners, week_strip painter, question_strip painter, mobi
    copy/         shared strings only (state words, formatters for time, date, marks)
  features/                    each feature owns its own copy.dart
    auth/ onboarding/ rhythm/ today/ practice/ runner/ result/ review/ learn/ you/ notifications/ platform/
assets/ fonts/ mobi/ sample/ (five questions json)
test/ unit/<module>/ golden/<module>/ golden/_support/ integration_test/
```

### 12.2 Dependencies (pub names; pin exact versions at setup, verify current versions with Context7 or pub.dev)
`flutter_riverpod`, `riverpod_annotation`, `go_router`, `dio`, `supabase_flutter`, `google_sign_in`, `drift`, `drift_flutter` (or `sqlite3_flutter_libs`), `flutter_secure_storage`, `shared_preferences`, `workmanager`, `wakelock_plus`, `connectivity_plus`, `flutter_local_notifications`, `timezone`, `flutter_timezone`, `firebase_core`, `firebase_messaging` (analytics collection disabled; init deferred), `home_widget`, `quick_actions`, `url_launcher` (Custom Tabs), `package_info_plus`, `share_plus`, `lucide_icons_flutter`, `intl`, `uuid`, `freezed`, `freezed_annotation`, `json_serializable`, `json_annotation`, `build_runner`, `drift_dev`, `riverpod_generator`, dev: `flutter_test`, `integration_test`, `mocktail`, `alchemist` (golden tests), `flutter_lints`. Not used: any ad or third-party analytics SDK, `lottie`, `rive`, `google_fonts` at runtime (fonts are bundled), `BackdropFilter`-based packages.

### 12.3 Modules
Ownership is by file and is disjoint. Every module imports `core/*` only through its public barrel and may not edit another module's files. Rules that remove the shared hot files:
- **Copy.** Each feature owns `features/<feature>/copy.dart` for its exact strings. `core/copy` holds only shared strings (state words such as "On this phone", formatters) and is owned by Module 0. Module 13's lint scans every `copy.dart` and `core/copy`, not one file.
- **Painters.** The week strip painter and the question strip painter live in `core/widgets` (Module 0). Module 3 and others only compose them.
- **Android.** Module 0 pre-creates the whole manifest (permissions `INTERNET`, `ACCESS_NETWORK_STATE`, `POST_NOTIFICATIONS`, `WAKE_LOCK`; the App Links intent filters for `www.mockmob.in`; the widget receiver; the FCM service; the shortcuts meta-data; and the two Firebase meta-data flags `firebase_analytics_collection_enabled` false and `google_analytics_adid_collection_enabled` false), the Gradle files, and empty-but-compiling Kotlin stubs in the `platform` and `notifications` packages. Module 11 then owns only files under `notifications/`, and Module 12 only files under `platform/` and `res/xml/`. The runner needs no native edit (`wakelock_plus` is a plugin). A module that needs a manifest change asks the Module 0 owner.
- **Routes.** Module 0 defines every route up front (4.2), each with a placeholder, so no module adds a route.
- **Shared repositories.** `ConsentRepository` (`GET/PUT /api/me/consent`), `NotificationPrefsRepository` (`GET/PUT /api/me/notification-prefs`), `GoalRepository` (`GET/PUT /api/me/goal`), `SessionDraftRepository`, `PendingResultRepository`, `RhythmSeenRepository`, `DismissalRepository`, `RepairLocalRepository` and the `PermissionRequester` interface are implemented once in `core` by Module 0. Modules 1, 2, 3, 4, 6, 7, 8, 10 and 11 consume them and implement no endpoint of these families themselves.
- **Tests.** Each module owns `test/unit/<module>/` and `test/golden/<module>/` for its own screens. Module 13 owns only `test/golden/_support/`, `integration_test/` and CI.

**Module 0: core.** Owns `lib/core/**`, `lib/main.dart`, `lib/app.dart`, `android/**` (manifest, Gradle, stubs), `assets/fonts`, `assets/mobi`, pubspec. Contents: theme and tokens (section 2), `KeyButton`, motion tokens, haptics, router with every route in 4.2 and a placeholder for every screen, API client (Bearer, refresh once on 401 then sign out, per-family error parsers, 429 back-off, no raw messages), auth store and background-isolate refresh with the lock, drift schema (section 10), secure storage, the shared repositories and `PermissionRequester` above, the domain functions (`markBreakdown`, mock ordinal, observed chapter breakdown, repair candidates) with unit tests, consent-gated analytics client and queue (tagged by user id), notification service skeleton with channels and quiet-hours logic, connectivity, sync outbox, shared widgets (skeleton, state views, sheet, banner, week strip painter, question strip painter, Mobi). Depends on: none. Endpoints: `GET /api/auth/me`, `GET/PUT /api/me/consent`, `GET/PUT /api/me/notification-prefs`, `GET/PUT /api/me/goal`, `POST /api/events`. Acceptance: app launches to `/splash` then `/welcome`; theme golden in both modes; `KeyButton` rest, pressed, disabled, loading goldens; unit tests prove no event is sent when consent is off or when the consent GET fails, the queue is cleared on withdrawal, sign-out and account switch, and a flush never sends events tagged with another user id; `markBreakdown` parts sum to `n*5`; 401 triggers one refresh then sign-out; fonts at most 350 KB. Goldens (`test/golden/core/`): key states, tab bar, skeleton, banner, question strip (right, wrong, blank, changed, repaired), week strip, state view.

**Module 1: auth.** Owns `features/auth/**`. Depends on 0. Endpoints: `POST /api/auth/email-login`, Supabase `verifyOTP`, `signInWithIdToken`, `GET /api/auth/me` (consent through `ConsentRepository`). Screens: sign-in, code. Acceptance: all error copy of 5.2; resend cooldown 60 s; the OTP double-try; Google flow behind config. Goldens: sign-in, code, error, loading.

**Module 2: onboarding.** Owns `features/onboarding/**`, `assets/sample/**`. Depends on 0, 1. Endpoints: `GET /api/subjects`, `PATCH /api/users/{id}` with only `{subjects}` (temporary until B1 ships `PATCH /api/me/profile`), `POST /api/me/sample-import` `[NEW-API]` (B9); consent through `ConsentRepository`. Screens: welcome, subject, five questions, sample result, account step, before you start. Acceptance: works offline until the account step; guest merge idempotent; no Mobi before choosing; the subject reason reads "We use this to set up your first mock." Goldens: welcome, subject, question (unanswered, correct, wrong), sample result, before you start (adult with the exact switch label, minor).

**Module 3: rhythm and celebration domain.** Owns `features/rhythm/**` (providers, week sheet, milestone rows, celebration controller, goal editor logic, `rhythm_seen` logic). It composes the core week strip painter and does not own it. Depends on 0. Endpoints: `GET /api/me/rhythm` (goal through `GoalRepository`). Acceptance: celebration ids fire once; suppression rules of 6.2; strip states of 6.1; streak never shown as 0; run-ended and week-closed detection from `rhythm_seen` with the best-effort rule of 6.1. Goldens: strip states (empty, partial, met, paused, stale, unavailable), milestone list.

**Module 4: today.** Owns `features/today/**`. Depends on 0, 3; reads the session draft through the core `SessionDraftRepository` written by Module 6, and the cached attempts and `pending_result` through core repositories. Endpoints: `GET /api/learning/plan`, `GET /api/me/rhythm`, `GET /api/auth/me`, `GET /api/practice/quote`, `GET /api/ai/credits`. Acceptance: states and precedence of 5.3, alternatives sheet, dismissal, why sheet, resume, ended and result slots, late-night line, return flow. Goldens: all states light and dark, skeleton, resume, ended-mock (three copies), return.

**Module 5: practice setup.** Owns `features/practice/**` (setup and the practice ending, 5.4.1). Depends on 0. Endpoints: `GET /api/practice/quote`, `GET /api/subjects`, `GET /api/chapters`, `POST /api/sessions` (start), `GET /api/ai/credits` (read-only, balance). Acceptance: quote then start with persisted `generationKey`; copy for 402, 422 and unavailable; no prices; credits-low state lists only confirmed free paths. Goldens: mode list, setup, blocked, credits low, offline, pre-start sheet (with and without the ticket line), practice result.

**Module 6: runner.** Owns `features/runner/**` including the background submit job (registered in core `sync/`). Depends on 0, 5. Endpoints: `POST /api/sessions` (resume), `PUT /api/sessions`, `POST /api/attempts`, `GET /api/attempts/{id}`, `POST /api/sessions/{id}/check` `[NEW-API]` (B13). Acceptance: three-state save model; monotonic clock anchoring; journal restore after process kill; back guard; palette; submit stages only from real calls (Sending, Received); offline and deadline copy; unattended-deadline job and background token refresh (5.5.1); no correctness in a mock; the practice skin shows no correctness until B13. Goldens: runner (each save state), palette, leave guard, submit sheet, failed submit, practice skin (with B13: correct and wrong).

**Module 7: result and recap.** Owns `features/result/**`. Depends on 0, 3, 6 (shared attempt model from core); calls the core `PermissionRequester` interface for the first-result reminder row (implementation is Module 11's, no build-time dependency). Endpoints: `GET /api/attempts/{id}`, `GET /api/attempts`, `GET /api/me/rhythm`, `GET /api/learning/plan`, `GET /api/ai/credits`, `GET /api/recovery/replay` (gated copy only). Acceptance: 5.6 and 5.7 completely, including card 1 with the strip, card 2 arithmetic, card 3 from the observed chapter breakdown, ritual decay, variants default, first_mock, held, keys unavailable (lower and higher when `recap.tone` exists). Goldens: sealed sheet, cards 1 to 4 (default, first_mock, held, lower, higher), full result, corrected annotation.

**Module 8: review and repair.** Owns `features/review/**`. Depends on 0, 3, 6 (the repair retry reuses the runner's practice skin and the practice start), 7. Endpoints: `GET /api/attempts`, `POST /api/recovery/repair`, `GET /api/ai/credits`, `GET /api/me/repair-record` `[NEW-API]` (B7, fallback `repair_local`), `POST /api/recovery` optional decision log. Acceptance: record timeline with Checked "not available yet"; repair outcomes and error mapping of 5.8; no-AI fallback; blanks never offered for repair and `not_a_mistake` hides the item; ending with receipt from the last repair acknowledgment. Goldens: review empty, sparse, list, record timeline, repair entry, explanation, no-AI fallback, ending, held_for_recheck.

**Module 9: learn.** Owns `features/learn/**`. Depends on 0. Endpoints: `GET /api/study/catalog`, `GET/PUT /api/study/preferences`, `POST /api/study/runs`, `GET /api/study/runs/{id}`, `POST /api/study/runs/{id}/events`, `GET /api/study/units/{id}`. Acceptance: pending-event persistence, offline pack, conflict handling, run ending, status mapping including `lock_in`. Goldens: due summary, empty, card front and revealed, run ending, offline pack, disabled.

**Module 10: you.** Owns `features/you/**`. Depends on 0, 3. Endpoints: `POST /api/me/delete`, `GET /api/auth/me`, `GET /api/me/rhythm` (consent, goal and notification prefs through the core repositories; the notification engine is Module 11). Acceptance: usage-data row exact label and states, withdrawal confirmation after save, delete flow, sign-out warning for unsent answers and queue clearing, appearance settings, Pro status text. Goldens: you hub, goal editor, privacy (adult on, adult off, minor, unknown), delete, account.

**Module 11: notifications.** Owns `features/notifications/**`, `android/app/src/main/kotlin/in/mockmob/app/notifications/**`; the notification service interface inside `core/notifications` is Module 0's. This module owns schedulers, channel setup, copy, quiet-hours and cap logic, token upload, and the `PermissionRequester` implementation. Depends on 0, 10. Endpoints: `POST/DELETE /api/me/devices` (prefs through `NotificationPrefsRepository`). Acceptance: permission after first value only; quiet hours defer to 7:00 AM; cap and stop-after-3-ignored; cancellation; ongoing silent mock status uses real states; result-ready only for a background-acknowledged submit; inexact scheduling only. Goldens: pre-prompt sheet, quiet-hours editor with conflict message, notification previews.

**Module 12: platform surfaces.** Owns `features/platform/**`, `android/app/src/main/kotlin/in/mockmob/app/platform/**`, `android/app/src/main/res/xml/*widget*` and widget layouts. Depends on 0, 4. Endpoints: reads cached plan and rhythm. Acceptance: App Links verified on www only, signed-out continue-after-login, widget states, shortcuts. Goldens: widget 4x2 and 2x2 (ready, signed out, offline), shortcut list.

**Module 13: quality harness.** Owns `integration_test/**`, `test/golden/_support/**`, CI config. Depends on all. Contents: the standards slop-list lint over every `copy.dart` and `core/copy` (uppercase eyebrows, middle dots, emoji, trailing arrows, exclamation successes, and the words "saved" or "safe" within 40 characters of "phone", which must read "On this phone"), accessibility tests at 1.0, 1.3, 2.0 scale, interruption scenarios (background, process kill, airplane mid-mock, call, account switch, leaving through the deadline), profile-mode timeline summaries for tab switch, question change and recap, a checklist that every fresh-check surface shows the unavailable state while the gate flag is false. Acceptance: all pass on the real phone when confirmed; reports state only what was exercised.

Dependency order: 0, then 1 and 3 and 9 in parallel, then 2, 4, 5, 10, then 6, then 7, 8, 11, 12 in parallel (7 and 8 need 6; 11 needs 10; 12 needs 4), then 13.

### 12.4 Backend modules and migrations (for `mockmob-next`)
| ID | Work | Endpoint or change | Migration name |
|---|---|---|---|
| B1 | Security: allowlisted profile route; strip `role`, `subscriptionStatus`, `isPremium`, `premiumUntil`, `razorpaySubscriptionId`, `email` from `PATCH /api/users/[id]`; validate subject ids and maximum 5 | `PATCH /api/me/profile` | none |
| B2 | Study-day floor of 5 answered questions; goal history so past weeks keep their goal; pause start date; rhythm response gains `history` (last 12 weeks of `{weekStart, studyDays, goal, met}`), `repairsThisWeek`, `mocksThisWeek` and `lastClosedWeek` with a stable id `[NEW-API]` | change `rhythm.js`, `GET /api/me/rhythm`, `GET/PUT /api/me/goal` | `20261013_study_goal_history` |
| B3 | Apply saved migrations from `5fac96f` (consent, usage events, notification prefs, push devices, study goals, deletion requests, `insert_usage_events`) after dry-run | none | existing |
| B4 | Slim paged attempts list | `GET /api/attempts/summary?cursor=` (id, subject, mode, marks, max, completedAt, formatId) | none |
| B5 | Notification sender: scheduler, quiet-hours and cap enforcement, FCM send, cancellation | server job | `20261013_notification_outbox` |
| B6 | Deletion processor and web deletion page (Play requirement) | operator script, web URL | `20261013_deletion_processor` |
| B7 | Repair record: found, repaired, checked-state per question | `GET /api/me/repair-record` | `20261013_repair_record_view` |
| B8 | Recap block: `tone`, `previousComparable`, `formatId`, `timingReliable` on attempt detail, with `mode` and `formatId` also on `attemptOut` and the B4 summary; owner-tuned thresholds | extend `GET /api/attempts/[id]`; `GET /api/me/bests` | `20261013_attempt_format_id` |
| B9 | Guest sample import, idempotent | `POST /api/me/sample-import` | `20261013_sample_imports` |
| B10 | Structured action fields (type, subject, chapter, mode) beside web `href` values in plan, replay, repair, quote | extend responses | none |
| B11 | **Blocker for Full and NTA-style mocks.** Server auto-finalises durable sessions at `expiresAt` from the acknowledged events and creates the attempt; expose the durable or ticket capability to the client | server job and contract | none |
| B12 | Set `ANDROID_CERT_SHA256` (release and Play App Signing); Supabase Google provider config | env and config | none |
| B13 | Practice feedback check, refused for `full` and `nta` `[NEW-API]` | `POST /api/sessions/{id}/check {qid, answer}` returning `{correct, keyIndex, explanation}` | `20261013_session_check_log` |

---

## 13. Items to confirm
1. Analytics reading: explicit adult opt-in (switch starts off) versus pre-ticked for adults.
2. Goal unit: study days (supported today) versus repairs; whether to build B2 now.
3. Result tone thresholds and the silent result-ready push inside quiet hours.
4. Welcome line without the "Prove it" clause until checks are live.
5. Weekly push cap (3 a week here, API default 5).
6. Mocks depend on B11 (server auto-finalise at expiry); what remains to confirm is whether the 120 s grace stays and what ticket mode does.
7. Play policy review of the no-price rule and of any mention of Pro in the app.
8. Mobi pose count and sizes confirmed against the web assets.
9. Real phone: every budget in section 11 is unmeasured until it is confirmed.
10. Practice credits: whether they refill (for example monthly), because 100 credits is two Full mocks and the app has no way to buy or earn more.
11. Subject list: Commerce four only, or all 15 supported subjects (5.1.2).
12. Repair time of 3 minutes per mistake (a stated assumption) and the B13 rule that a checked answer is final.
