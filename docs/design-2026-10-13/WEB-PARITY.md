# Web parity: every student-facing website feature, and the plan to bring each into the app

13 October 2026. Research pass, read-only (no code changed). Authority: OWNER-FEEDBACK-1110.md wins, then BUILD-BRIEF.md, DEVICE-FINDINGS.md, REVIEW-ROUND1.md. Where APP-DESIGN-SPEC.md says "no Mobi, no celebration after practice" or "NTA-style uses the same runner skin", the owner's 11:10 feedback overrides it (section 11, decisions 1 and 2).

Read for this document: every page under `src/app/(app)` (dashboard, today, test, result, review, recovery, progress, analytics, rival, leaderboard, mentor, saved, explore, study, learn, profile, admission-compass, upload, my-uploads, moderation) with their components, the public tools (`cuet-cutoff-calculator`, `cuet-subject-combination`, `cuet-previous-year-questions`, `cuet-2027`, `cuet/[subject]`, `cuet-mock-test-free`, `cuet-practice-tests-online`, `features`), all 85 route handlers under `src/app/api`, the DU data under `public/du/2026`, `APP-API-CONTRACT.md`, and `flutter_app/lib` (474 Dart files, 11 features).

Legend. Status: Done, Partial, Missing (checked against `flutter_app/lib`). Pri: **P0** ships in this pass, **P1** next pass, **P2** link out or deliberately not built. Size is for one builder: S about half a day, M about a day, L two days or more.

---

## 1. Verdict in twelve lines

1. The app has the loop (Today, Practice, Runner, Result, Review, Repair, Learn, You, rhythm, reminders) and a better spine than the site (offline journal, durable sync, server-acknowledged states). It has almost none of the site's reading and planning surfaces.
2. Missing outright: Explore (untimed question stream), Saved questions, Radar and the PrepOS record (where marks go), Compass (DU eligibility and cutoffs, in-app), Combo Planner (in-app), Progress (playbook), chapter summaries, weekly study plan, edit subjects, edit name, plan card. Today the "CUET tools" rows in You open two Custom Tabs to the site.
3. NTA mode is wired to the API (`mode=nta`, quote, 50 questions, 3600 s) but opens the ordinary mock runner. None of the website's NTA features exist: two skins, the NTA palette with five states, "Mark for Review and Next", "Clear Response", passage sets as one block, the integrity warnings (3 strikes), the preparing screen, the free exam-screen preview. Section 5 specifies all of it.
4. Practice setup lacks what the site offers: multi-chapter selection with search (up to 12), difficulty (Pro), Smart practice (Pro), live question counts per subject, the summary (time, marking, cost), stale-subject handling, and `chapters`/`difficulty` in deep links (`ActionRouter._setup` drops them).
5. Result lacks the site's analysis depth: the marks-gap bar (scored, lost to wrong, left on blanks), observations (changed answers, rushed picks, one weak chapter, blanks), per-answer time and answer changes, filters, report-a-problem, the "5 fresh questions" Prove step, the decision note (playbook), and the whole-record view.
6. Every P0 feature has a Bearer-ready route today (`auth(request)`): feed, explore, vote, interact, bookmarks, prepos/insights, compass/pro, recovery/replay, recovery (GET and POST), me/repair-record, sessions/{id}/check, attempts/summary, ai/mentor/chat, users/{id} PATCH (now allowlisted: name and subjects only). The contract's section 4 is partly stale; section 8 here lists what changed.
7. Cookie-only and therefore P2 for now: ai/rival/start and submit, ai/mentor/local and session/new, ai/context, ai/actions/execute, questions upload, mine, moderate, billing cancel, credit orders, creator/me, admin/*.
8. Do not port: `/api/analytics` `advanced` block (readiness, focus score, momentum, "rank readiness": conflicts with the product's no-rank-prediction rule, contract G12), `topContributors`, the public leaderboard (names and ids of every user plus 12 invented "practice rivals", contract G7, and APP-DESIGN-SPEC 6.10 bans leaderboards), invented counts.
9. Information architecture stays three tabs plus Start and You. Everything new lands inside Practice (Explore, subjects), Review (Insights, Saved) and a "CUET tools" screen behind You. No new tab, no "More" tab. Section 2.
10. The Today, Start sheet and dock work the owner praised stays untouched. New screens use the existing foundation (GlassSurface, KeyButton, Bubble system, sheets, TabRootHeader, MmArt, Mobi).
11. A decorative dot or bubble must be either a state the student can act on (palette cell, week day, answer in the strip) or a link to the questions behind a claim ("Show me"). Section 6 audits the existing motifs against that rule.
12. P0 total is about 11 work packages (section 9). They are independent enough for parallel builders: only A2/A3 (practice setup, router) and A5 (NTA) share the runner and `SessionDraft` key.

---

## 2. Information architecture (proposed)

### 2.1 Surfaces

| Surface | What it holds | Website pages it absorbs |
|---|---|---|
| Dock tab Today | Tonight's move (time chips 10/20/30, why sheet, resume, sealed result), week, sheet, road to May, **study sequence** (P1), **one finding from the record with Show me** (P0, from `/api/prepos/insights` findings[0]) | /today, RecordGlimpse |
| Dock tab Practice | Recommended start; Choose your own (Quick, One chapter, Full mock, **NTA mode**, **Smart practice**, Pro tags from the quote); **Your subjects** (tiles with question counts, "Edit subjects"); **Question stream** row (Explore); Concepts shelf | /dashboard, /explore, /learn entry |
| Dock tab Review | Tonight's repair, mistakes by chapter, **Where your marks go** card (Insights), **Saved questions** row, record preview, past sessions, due recall cards line | /review, /progress (playbook), /analytics (Radar), /saved, /recovery |
| Start (glass circle) | Resume, Quick 10 in the first subject, Full mock, **NTA mode** (Pro tag), Repair the next mistake (max five rows) | quick start |
| You (avatar) | Sheet (course, colleges, subjects with **Edit**, week), **Plan and credits**, Progress group (rhythm, repair record, milestones, bests), Settings group, **CUET tools** group | /profile |
| CUET tools (`/tools`, pushed from You and from a quiet link under Today's road) | Compass (eligibility and cutoffs), Combo Planner, Compass Pro (Pro), CUET 2027 guide, Ask your record (opens the Ask sheet), Subject guides and Previous-year guide (Custom Tab) | /admission-compass, /cuet-cutoff-calculator, /cuet-subject-combination, /cuet-2027, /cuet/[subject], /cuet-previous-year-questions, /mentor |
| Ask sheet (`/ask`, sheet) | "Your record" (free, computed on the phone) and optional model reply (1 PrepOS credit) | /mentor, AssistantDrawer |

### 2.2 New routes (add to `AppRoutes`, `router.dart`, `templates`)

| Route | Screen | Replaces web |
|---|---|---|
| `/practice/stream` | Explore stream (query `subject`, `chapter`, `difficulty`) | /explore |
| `/review/saved` | Saved questions | /saved |
| `/review/insights` | Insights: ledger, findings, chapters, changed answers, pace, week, trend, by subject | /analytics, mentor "Your record" |
| `/you/subjects` | Edit subjects (max 5) | /onboarding?edit=true |
| `/you/plan` | Plan and credits (read-only; no selling, binding rule 13) | PlanCard |
| `/tools`, `/tools/compass`, `/tools/compass/:groupId`, `/tools/combo`, `/tools/guide-2027` | CUET tools | DU pages, /cuet-2027 |
| `/learn/summary/:subject/:chapter` | Chapter summary reader (P1) | /learn/summary |
| `/ask` (sheet) | Ask your record | /mentor |
| `/practice/setup/:mode?chapters=a&chapters=b&difficulty=hard` | existing route, extended | /dashboard?... |
| `/run/:sessionId` | existing; NTA skin chosen by `mode == nta` | /test?mode=nta |
| `/practice/exam-preview` | Free exam-screen preview (P1) | landing #exam-experience |

### 2.3 `ActionRouter` mapping to add (web hrefs the API still returns)

`/explore` to `/practice/stream`; `/saved` to `/review/saved`; `/analytics` to `/review/insights`; `/mentor` (and `?tab=record`) to `/review/insights`, `?tab=ask` to `/ask`; `/admission-compass`, `/cuet-cutoff-calculator` to `/tools/compass`; `/cuet-subject-combination` to `/tools/combo`; `/cuet-2027` to `/tools/guide-2027`; `/learn/summary?subject&chapter` to `/learn/summary/...`; `/profile` to `/you`; `/onboarding?edit=true` to `/you/subjects`. `_setup` must also carry `chapters` (repeat param), `difficulty` and `interface`. `/leaderboard`, `/rival`, `/upload`, `/my-uploads`, `/moderation`, `/creator`, `/admin` stay Custom Tab or unsupported. `/pricing` stays refused (commerce prefix).

---

## 3. Master index

Status below was re-derived from `flutter_app/lib` on 13 October 2026 (evening). The section 1 verdict and the "App:" lines in section 4 are the original research and are older than this table; where they differ, this table wins. H1 to H4 were added after the first index.

| ID | Feature | Status | Home | Pri | Size | Evidence in `flutter_app/lib` |
|---|---|---|---|---|---|---|
| A1 | Today next step, time chips, study sequence, tonight recorded | Partial | Today | P1 sequence | S | Record finding card, minutes chips, resume, sealed hero, why, alternatives, week and road are built (`features/today`, `InsightsCard` in `today_routes.dart`). `LearningPlan.sequence` is parsed (`core/models/learning_plan.dart`) but not rendered; Today's minutes chip is not saved to `study/preferences` (You > study length saves it) |
| A2 | Practice setup: subject, mode, count, chapters, difficulty, summary, cost | Done | Practice, setup | none | none | `practice_setup_screen.dart`, `chapter_picker.dart` (search, units, up to 12, one chapter when a name has a comma), difficulty in `practice_selection.dart`, counts from `/api/stats` in `practice_catalog.dart`, Smart and NTA modes, `stale_subjects_banner.dart` |
| A3 | Deep links and Start sheet honour subject, mode, count, chapters | Partial | router, Start | P1 | S | `practice_link.dart` and `action_router.dart` carry subject, count, chapter, chapters, difficulty, purpose, `recoveryFrom`; `StartPendingElsewhere` is handled in `launch_flow.dart`. `tonightKey` and `tonightMinutes` are not carried (no match in `lib`) |
| A4 | Runner parity for Quick, Smart, Full | Done | Runner | none | none | Smart is not a mock (`runner_session.dart` `isMock` is full and NTA only), so it uses the practice skin with the server's deadline. Votes are deliberately absent from timed runs; the flag action is on the result (`report_key.dart`) |
| A5 | **NTA mode console** (two skins, palette, strikes, preparing, preview) | Done | Runner, Practice | none | none | `features/runner/nta/**` (skins, palette, `nta_integrity.dart` strikes, `nta_instructions_screen.dart`, preparing, submit summary), NTA-only `FLAG_SECURE` (`status_tint.dart`, `MainActivity.kt`). The free exam-screen preview (`/practice/exam-preview`) is not built |
| A6 | Submit, sync, offline, resume, auto-submit, grace window | Done | Runner | none | none | `core/sync/session/**`, `features/runner/**` |
| A7 | Result: summary, gap bar, observations, answer by answer, filters, timing, changes, report, corrections | Done | Result | none | none | `features/practice/model/session_analysis.dart`, `observations_panel.dart`, `result_list.dart`, `marks_bar.dart`, `report_key.dart`, `KeyState.held` for non-corrected reviews in `practice_result_model.dart` |
| A8 | Prove: 5 fresh questions (`recovery/replay`) | Done | Result | none | none | `prove_card.dart`, `result_actions.dart` (`/api/recovery/replay`), `recoveryFrom` in `practice_link.dart` and `practice_starter.dart` |
| A9 | Decision note to the playbook (`POST /api/recovery`) | Missing | Result, Review | P1 | S | No call to `/api/recovery` itself in `lib` (only `/api/recovery/repair` and `/replay`) |
| A10 | Mistake Repair (+ key review notices) | Done | Review | none | none | `features/review/**`, `repair_api.dart` |
| A11 | Review hub: sessions, mistakes, due cards, links to Insights and Saved | Done | Review | none | none | `review_screen.dart` mounts `ReviewInsightsRows` (Where your marks go, Saved with count) next to sessions, mistakes and the tonight card |
| A12 | Repair record across devices (`/api/me/repair-record`) | Missing (local only) | Review record | P1 | S | No `repair-record` call in `lib`; `repair_local_repository.dart` keeps repairs on the phone |
| A13 | Practice finish moment (animated) | Done | Practice result | none | none | `finish_stage.dart`, `model/finish_reaction.dart` |
| B1 | Learn library, lesson, run, recall | Done | Learn | none | none | `features/learn/**` |
| B2 | Chapter summary reader (`/api/study/summary`) | Done | Learn | none | none | `summary_screen.dart`, `summary_loader.dart`, `study_api.dart` are built. `LearnPaths.summary()` opens it and `router.dart` now binds `learnSummaryScreen` (checked 14 October 2026), so the reader is reachable from Learn and from a unit. Share as text is built |
| B3 | Study preferences (subjects, minutes) `PUT /api/study/preferences` | Done | You, Today | none | none | `you/data/study_length.dart` (GET and PUT with `expectedRevision`), `profile_editor.dart`; subjects are edited at `/you/subjects` |
| B4 | Weekly plan, 7 days, Pro | Partial | You, Today week sheet | P1 | M | The weekdays the student plans are chosen and shown (`rhythm/logic/plan_week.dart`, `week_sheet.dart`, `you/sheet/week_editor.dart`) but kept on the phone (`study_days.dart` `PhoneOnlyStudyDays`). The Pro `weeklyPlan` field of `study/preferences` (a subject and minutes per weekday) is not read or written. See H3 |
| B5 | Lesson help with AI (1 PrepOS credit) | Missing | Learn | P2 | S | No lesson-level `mentor/chat` call (Ask uses it for record questions only) |
| C1 | Insights (the record): ledger, findings, chapters, changes, pace, week | Done | Review | none | none | `features/insights/screens/insights_screen.dart`, `record_sections.dart`, `ledger_hero.dart`; Pro rows via `ProRow` |
| C2 | Score trend and by-subject | Done | Review | none | none | `widgets/trend_chart.dart`, `data/trend.dart` (`trendSeries`, `subjectLines`; one format per line) |
| C3 | Ask your record (free, local) and model reply | Done | Ask sheet | none | none | `data/ask_controller.dart` (local answers, then `POST /api/ai/mentor/chat`), `screens/ask_screen.dart` |
| C4 | Progress: concept checks (blocked state) and playbook list | Done | Review record | none | none | `insights/data/recovery_record.dart` (`GET /api/recovery`, read once when the record opens or is pulled, parsed off the main isolate, only checks and playbook kept and cached), `insights/widgets/recovery_sections.dart` mounted at the end of `insights_screen.dart`. Placeholder while loading, one plain row with Try again on failure or offline, empty lines for no checks and an empty playbook, "unavailable" kept apart from "empty", a playbook row opens its session. Milestones are not rendered (the rhythm milestones already cover them). Saving a note (A9) is still missing, so the empty playbook line points to the website |
| D1 | Explore stream with instant feedback | Done | Practice | none | none | `insights/screens/stream_screen.dart`, `data/feed_api.dart` (`/api/questions/feed`) |
| D2 | Vote, report, explanation opened | Done | Stream, Result | none | none | `feed_api.dart` (`/vote`), `widgets/question_actions.dart`, `report_key.dart` |
| D3 | Saved questions (bookmarks) | Done | Review | none | none | `insights/screens/saved_screen.dart`, `data/saved_repository.dart` (`/api/bookmarks`) |
| E1 | Compass: DU eligibility, cutoffs by category and round | Done | Tools | none | none | `features/tools/compass/**`, `domain/du_eligibility.dart`, `data/du_repository.dart` |
| E2 | Combo Planner | Done | Tools | none | none | `features/tools/combo/**`, `domain/du_combos.dart` |
| E3 | Compass Pro: projection, shortlist, paper to work on | Done | Tools | none | none | `tools/pro/**`; see H4 |
| E4 | CUET 2027 guide | Done | Tools | none | none | `tools/guide/guide_2027_screen.dart`, `/tools/guide-2027` |
| E5 | Subject hubs, PYQ guide, free-mock pages | Missing | Custom Tab | P2 | none | Not built; opens on the website only |
| F1 | Edit subjects | Done | You | none | none | `you/subjects/subjects_screen.dart`, `profile_editor.dart` (`PATCH /api/users/{id}`) |
| F2 | Edit display name | Done | You, Account | none | none | `you/account/name_sheet.dart` |
| F3 | Plan and credits card (read-only) | Done | You | none | none | `you/account/plan_card.dart` |
| F4 | Usage data consent, delete account, notifications, appearance | Done | You | none | none | `features/you/privacy`, `account`, `appearance`, `features/notifications` |
| F5 | Guided first-run tour with Mobi | Missing | Today | P1 | M | No spotlight or tour widget in `lib` |
| G1 | Leaderboard | not built | none | P2 | none | Deliberately not built (section 10) |
| G2 | Rival benchmark | Missing | none | P2 | none | Not built (section 10) |
| G3 | Upload, My uploads, Moderation, Creator, Admin | Missing | Custom Tab | P2 | none | Not built (section 10) |
| H1 | NTA inactive grace: another window may cover the exam for 3 s before a warning counts (3 s, owner decision 14 Oct 2026) | Done | Runner | none | none | `runner/nta/nta_integrity.dart` Xours, not the website's, so the owner confirms it. (The code comment cites it as decision 4 of section 11, but that list's item 4 is about Compass; the NTA rule is 5.3 item 4) |
| H2 | Subject monogram: a subject with no art shows its initials, never another subject's object | Done | Everywhere subjects show | none | none | `core/widgets/art/subject_glyph.dart` `subjectMonogram`, `learn/widgets/subject_mark.dart`, `insights/widgets/insights_bits.dart` (also logs the missing id). Section 11 item 9 |
| H3 | Per-weekday study plan: which weekdays the student plans, with rest days | Partial | You, Today week | P1 | M | Chosen in onboarding and `you/sheet/week_editor.dart`, shown by `plan_week_strip.dart` and `week_sheet.dart`; stored on the phone only (`study_days.dart`) because no endpoint holds weekdays. Done when the server gains a field or maps onto Pro `weeklyPlan` (B4) |
| H4 | Compass Pro: practice projection per paper, paper to work on, shortlist against 2026 cutoffs (Pro only) | Done | Tools | none | none | `tools/pro/compass_pro_section.dart`, `compass_pro_repository.dart` (`GET /api/compass/pro`); the section is absent for an account the server locks (`pro.locked`), no lock or pitch |

---

## 4. Detailed specs

### A1 Today

- Web: `/today` greets by first name, shows one primary step (`GET /api/learning/plan?minutes=10|20|30`), the time choice persisted through `PUT /api/study/preferences {minutes, expectedRevision, weeklyPlan?}` (409 `REVISION_CONFLICT`: refetch and retry), "why" facts (basis `record` or `rule`), `alternatives[0..2]`, a study `sequence[]` (lesson, recall, practice steps with hrefs, "Skip to the next step", "Take a mock"), a "tonight is recorded" banner when `plan.tonight.state == recorded` (link to `/result/{sessionId}`), and a one-line RecordGlimpse (`findings[0]` headline and detail, link "See your full record"). When launching `ordinary_practice` with no sequence the site adds `tonightKey` (12 to 100 chars) and `tonightMinutes` to the session start.
- App: move hero, minutes chips, resume, sealed hero, why sheet, alternatives, week, road: Done. `sequence` is parsed (`LearningPlan.sequence`) but not rendered. Minutes are not persisted. No record finding.
- Do now (P0): one finding line under the hero from `GET /api/prepos/insights` `findings[0]` (headline, detail) with a "Show me" pill opening `/review/insights` scrolled to that finding (`f.action.href` mapped through ActionRouter). Hidden when `insights.state != ready` or the call fails. Never a second plan.
- P1: render `sequence` as a numbered "Your study session" list (3 steps max, each opens its route); persist minutes via `PUT /api/study/preferences` and pass `tonightKey`/`tonightMinutes` for the quick-10 and quick-20 starts so "tonight recorded" works.
- Acceptance: the finding appears only with `sessions >= 1`; tapping Show me lands on the evidence; no number on the line is computed on the phone; airplane mode hides it silently.

### A2 Practice setup (website "Practice" page)

What the site does for the student, in order: (1) pick a subject from their saved subjects that have `practice == supported`, each tile shows the CUET code and how many usable questions exist (`GET /api/stats` `subjectCounts[internalId]`, public, 30 s cache), plus "Edit subjects"; stale saved subjects (practice not supported) are listed with `practiceReason` and a way to edit. (2) pick a mode: Quick (5/10/15/20, 60 s each), Full (50, 60 min), Smart (Pro, 10/15/20, adaptive 45/60/90 s per easy/medium/hard, weights chapters missed), NTA (Pro, 50, 60 min). Badge per mode: Included (Pro), Needs access, or N credits. (3) Fine-tune: difficulty Balanced/Easy/Medium/Hard (Pro only, quick and full only, never smart or nta) and chapters (search box, multi-select, up to 12, "All chapters", grouped by unit for unit subjects such as Mathematics and Chemistry via `units[].chapters`). (4) Summary panel: Subject, Mode, Questions, Time (`quote.durationSec`, "About" when `durationEstimated`), Marking "+5 / -1", Cost ("Free: today's included set" when `creditCost == 0`, "Included with access", or "N credits"), `quote.reason`, and for blocked quotes an upgrade pointer (never a purchase in the app). (5) Wallet strip: practice credits, "Quick costs 10, Full costs 50", unlimited with Pro. (6) Launch: the quote's `idempotencyToken` becomes the `generationKey`; a quote older than `expiresAt` (60 s) is re-fetched first; `tonightKey`/`tonightMinutes` pass through.

- API: `GET /api/practice/quote?subject&mode&count&purpose` (never charges; HTTP 200 even when blocked; branch on `state`, `launchable`, `reasonCode`); `GET /api/chapters?subject=` (`{grouped, units:[{id,name,chapters:[{id,name}]}]}` or `{grouped:false, chapters}`); `GET /api/stats`; `POST /api/sessions {generationKey, subject, mode, count, chapter|chapters, difficulty, experience:"practice", purpose?, tonightKey?, tonightMinutes?}`.
- App today: subject tiles, mode list (Quick, One chapter, Full, NTA row gated by quote), confirm sheet with cost line, chapter picker (single), count 5/10/15/20, "More subjects" sheet. Missing: multi-chapter with search and unit grouping, difficulty, Smart, per-subject question counts, the summary with time and marking, stale-subject banner, Edit subjects link.
- Rules the builder must follow: the API takes chapter NAMES. `chapters` is a comma-joined string and the server splits on commas (`practiceSessions.js:31`), so a name such as "Alcohols, Phenols and Ethers" breaks a multi-select. Until the server accepts an array (request this one-line change, section 8), the picker must disable multi-select for any subject that has a comma in a chapter name and fall back to one chapter via the single `chapter` field. Difficulty and multi-chapter must be added to `SessionDraft.keyFor` (the web key includes difficulty and chapters; the app key does not), otherwise a resumed draft can start the wrong selection.
- Acceptance: (a) start Business Studies, 15 questions, one chapter: the runner shows Business Studies, 15 questions, that chapter; repeat for every subject the account has (15 supported ids). (b) A free account sees Smart and difficulty with a "Pro" tag and the quote's reason, never a purchase button. (c) The summary time and cost come from the quote only. (d) A subject with `practice != supported` appears in a "cannot start practice" banner with `practiceReason` and an Edit subjects key. (e) Goldens: setup in both themes with 1 chapter, 3 chapters, difficulty on, quote blocked, quote loading, offline.

### A3 Deep links and Start sheet

- Web `/dashboard?subject=&mode=&count=&chapter=&chapters=&difficulty=&tonightKey=&tonightMinutes=&interface=nta` prefills the setup; a `subject` the student does not have shows "The lesson's subject is not in your available practice subjects" with Edit subjects.
- App: `_setup` keeps subject, chapter, count only.
- Acceptance: the Start sheet, Today's hero, the Concepts shelf and every notification payload that names a subject start that subject; a stored draft for another subject never silently replaces the chosen one (`StartPendingElsewhere` must name the subject and offer Resume or Start new); the 5-question quick practice shows the real runner (not a loading score) and the result opens after the server acknowledges the submit.

### A4 Runner parity (Quick, Smart, Full)

- Web: exit with confirm (progress saved, resume from the same session), progress bar and "N answered", timer with `role=timer`, sync line (offline, pending submission, saved), palette, mark, clear, keyboard 1 to 4 and arrows, passage block that groups all its questions, per-question vote controls (Quick and Full only), "insufficient pool" alert (`meta.insufficientHighQualityPool`, `meta.message`), pre-start preparing screen.
- App: Done except votes and the preparing steps. P0: Smart mode launches with the Quick skin (practice, no exam clock: Smart uses adaptive per-difficulty time, `expiresAt` from the server is the only deadline). P1: a quiet "Flag this question" action after submit only (section D2); no vote controls during a timed mock (integrity: nothing decorative and no feedback loops during a mock).
- Acceptance: all of the above rendered from `meta`/`expiresAt`; never compute the deadline locally.

### A5 NTA mode: see section 5.

### A7 Result depth

What the site shows, in order: hero (Mobi pose by pass at score >= 40, count-up marks "N / max marks", verdict line: all right; wrong answers cost X of the Y marks missed; or blanks left X), stats (Right +5 each, Wrong -1 each, Blank 0, Accuracy of answered), a strip of numbered question buttons coloured by verdict with "answer changed" marker (tap jumps and opens), then the Score Recovery Lab: the bar (scored, lost to wrong, left on blanks) and "Each wrong answer costs 6: the 5 you did not get, plus the 1 penalty"; step Find (chapters ranked by marks lost, each with wrong/blank counts of n and a proportional track; up to 4, expandable), observations (see below); step Repair (queue of wrong questions, progress "N of M explanations ready", cost "1 credit per repair, reopening is free, no charge if held"); step Prove (A8); a collapsible "every answer you changed" list with time, before to after letters and mark effect, and the one-line note (A9); key review log; correction notice ("We corrected N answer keys. We are sorry." original result preserved); then "Answer by answer" with filters All / Wrong / Blank / Right, each row collapsible: question text, verdict "Right +5 / Wrong -1 / Blank 0", chapter, time on question, "Answer changed", repair label, options with your pick and key (key shown only with no review or a `corrected` review), book explanation, Mistake Repair, key-review or correction notice, "Report a problem with this question". Footer links: full record, all mistakes, Radar, back to practice.

- Observations (client-side from `selectionMeta.recovery`, `data/session_recovery.js`): Changed answers (helped or hurt marks), Rushed picks (half or more of timed wrong answers quick), One weak chapter (one chapter holds 40% or more of the wrong answers, with 2+ wrong and 3+ wrong overall), Blanks. Timing exists only when `selectionMeta.recovery.telemetry == self_reported`; for `inconsistent` or `invalid` say so and hide timings. Device-scored attempts (no `scoringVersion`) show no changes or timings.
- API: `GET /api/attempts/{id}` returns `answerReviews` and `answerReviewState`; `POST /api/questions/{id}/interact {interaction_type:"report", flow_context:"review", session_id, metadata:{source:"result_analysis", attempt_id, subject, verdict, note, given_index, correct_index}}`.
- App today: recap cards, full result with answers grouped Wrong/Blank/Right, explanations, changed-answer note, first-fix card, key rules for reviews. Missing: gap bar and the 6-mark rule line, observations, per-answer time, the changed-answers list, filter chips, report a problem, the fresh-5 step, note, the "all saved mistakes" and "Insights" links.
- Port to Dart (pure, from `data/session_recovery.js`): `analyseSession` (marks, accuracy, per-question verdict, dwell from timeline, chapter breakdown, observations) and `formatDuration`. Never compute scores for authority: the attempt's `correct/wrong/unattempted` is the truth.
- Acceptance: for a 10-question paper with 7 right, 2 wrong and 1 blank the result shows 33 of 50 marks, "2 wrong answers cost 12 of the 17 marks you missed" arithmetic exactly as the site does (right 35, wrong -2: 33; gap 17; gapWrong 12, gapBlank 5); filters work; the report note posts and the row reads "Reported. Thank you."; a corrected key shows the correction notice and never the old key as current.

### A8 Prove: five fresh questions

- Web: after a result, `GET /api/recovery/replay?attemptId=` (30/min, one call per result view). `state:"unsupported"` outside the four launch subjects (english, accountancy, business_studies, economics); else `chapters:[{chapter, state:available|unavailable, href}]`. Available: "Try 5 fresh questions" starts `POST /api/sessions {subject, mode:"quick", count:"5", chapter, recoveryFrom:attemptId, experience:"recovery", generationKey}` (free, 300 s). Failure `INSUFFICIENT_VERIFIED_CONTENT`. Otherwise a regular 10-question set on the top chapter.
- App: Missing. Home: the first-fix card and the repair ending screen.
- Acceptance: the key never appears before the fresh set is submitted; copy says "A day or two later is how you know a repair stuck"; unsupported subjects show the ordinary-practice fallback and no promise of fresh questions.

### A9 Decision note (playbook)

- `POST /api/recovery {attemptId, strategy:"two_pass"|"concept_repair"|"timed_practice", reflection<=1000}` returns `{saved:true, evidenceState:"more_evidence_needed"}`; needs a server-scored attempt (422 otherwise). The site picks `concept_repair` when the attempt has mistakes else `two_pass`. `GET /api/recovery` returns `playbook[]` for the Progress list. Home: result detail (collapsed) and Review > Record. Say "Saved" only after the 200.

### A11 and A12 Review and repair record

- Web Review lists every session (`GET /api/recovery` `ordinaryReview[]`: id, subject, completedAt, correct, total, mistakes) with a to-review badge, summary stats (sessions saved, questions to review, right %, last session), the shared next step and the study due-cards line (`GET /api/study/catalog`).
- App Review is richer (chapters, repair, record). Add: rows "Where your marks go" (to `/review/insights`) and "Saved questions" with the count (to `/review/saved`), and wire `GET /api/me/repair-record?limit=50` (rows `{attemptId, questionId, chapter, subject, foundAt, repairedAt, checkedState: not_available|pending|passed|not_passed, retriedAt}`) so the record survives a new phone. Merge by `(attemptId, questionId)` with local records; server wins on `repairedAt`.
- Acceptance: sign in on a second device and the repair record shows the same repairs; `not_available` renders as "Check not available yet", never "Checked".

### A13 Practice finish moment (owner feedback)

- Today quick practice goes straight to a quiet result. Owner wants a real moment. Spec (proportional, no confetti, nothing during the run): submit stages come only from real calls (Sending, then Received at the 200); the result opens with the N-bubble strip inking in order (40 ms stagger, 800 ms cap, mask reveal), the figure "8 of 10" rolls (500 ms), and Mobi appears with a pose chosen from the outcome: `cheer` at 70% or better or better than the last practice in that subject, `point` toward the first wrong answer when there are mistakes, `read` when most are blank, `rest` for a very short or very poor set (calm, no sweep). Receipt line "Practice finished. Recorded at 11:51 PM." after the 200. Reduced motion: final state at once. Keys: Review N wrong answers, Try the blanks, Practise another chapter, Finish for now. Lower results get no celebration.
- Acceptance: golden frames at 0, 400, 900 ms; the moment never precedes server acknowledgment; skippable by tap.

### B2 to B5 Study extras

- B2 `GET /api/study/summary?subject&chapter` returns `{units:[{id,title,version,sourceRefs,blocks:[{id,title,...}]}]}`: published lessons of a chapter in one scroll. Print is web only; the app offers Share as text (P1). Entry: the chapter row in Learn ("Read the chapter summary").
- B3 preferences: `GET/PUT /api/study/preferences {subjects, minutes:10|20|30, expectedRevision}`; `newCardsPerDay` is forced to 5. Entry: You > Study preferences (subjects and usual time).
- B4 weekly plan (Pro): `weeklyPlan:[7 x {subject, minutes}]`, Pro only (422 `PREMIUM_REQUIRED`). This is the natural data behind the "weekly rhythm needs more thought" feedback: goal days per week (`/api/me/goal`) says how many days; the weekly plan says what each weekday is for. Show it in the week sheet; free accounts see the shape with a plain "Pro" note.
- B5 `POST /api/ai/mentor/chat {message, mode:"revision", studyRunId, studyRevision:int, studyItemId, requestId}` costs 1 PrepOS credit; reuse `requestId` on retry; P2.

### C1 and C2 Insights (the record)

- Web: Radar page and PrepOS "Your record": `GET /api/prepos/insights` (60/min, no model, no credits, last 60 sessions) returns `{ok, insights:{state, sessions, questions, window:{first,last}, ledger:{gained, penalty, openSkipped, net}, accuracy:{pct, low, high, n}, chapters:{ranked[], thin[]}, changes:{count, gains, losses, marksGained, marksLost, net, sessionsWithTelemetry}, pace:{usable, medianSec, p90Sec, medianRightSec, medianWrongSec, shareOnWrong, slowest[], questionsTimed, sessionsTimed}, week:{thisWeek, lastWeek, activeDaysLast14}}, findings:[{id, kind: good|leak|info, headline, detail, n, action:{label, href}}], basis}`.
- Sections to render, each with its sample size: Net marks ledger (+5 per right, -1 per wrong), What stands out (findings with "Based on n questions" and an action), Chapters by marks left open (right/wrong/blank stack, open marks, n; `MIN_CHAPTER_SAMPLE = 4`; thin chapters in a separate collapsed list), Changed answers (helped, hurt, net: "shows what happened, not why"), Pace (typical, slowest 10%, right vs wrong, time on wrong; needs 8 timed questions), This week and last, Active days of the last 14. The site gates changed answers, pace and chapters beyond 3 to Pro (`ProLock`); in the app show the same gating as a quiet "Pro" row, never a sales screen.
- Trend and by subject: use `GET /api/attempts/summary?limit=50` (slim: `{id, subject, mode, correct, wrong, unattempted, total, marks, maxMarks, completedAt, formatId}`) for a score-by-session line (marks over max, same subject and format only; the site's chart mixes formats, the app must not) and per-subject sessions and accuracy. Do not call `/api/analytics` (heavy, returns readiness and focus scores).
- Honesty rules: every figure shows its n; no cause, no prediction, no "marks you could recover", no percentile.
- Acceptance: with 0 sessions the empty state offers a Quick 10; with 1 session the trend line says "One more session and the trend line appears"; a failed call shows "Your record could not be read just now. Nothing was charged." with Retry; goldens in both themes for empty, thin, rich.

### C3 Ask your record

- Free path: port `answerFromInsights(text, insights, {pro})` from `data/prepos_insights.js` to Dart (pure, deterministic: marks, chapters, timing questions). Suggestion chips: "Where am I losing marks?", "Which chapter should I practise?", "Am I spending too long on wrong answers?". Origin label "From your record. No credits."
- Model path (P2): `POST /api/ai/mentor/chat {message<=1500, mode, replyKind:"record"|"model", requestId, sessionId}` 20/min; `replyKind:"record"` can never fall through to a billed model. Reuse `requestId` after an unknown outcome. Wallet from `GET /api/ai/credits` (`known:false` must never render as zero). History: `GET /api/ai/mentor/history`. Session create and local logging are cookie-only (skip logging).

### C4 Progress

- `GET /api/recovery` heavy (all attempts): `progress[]` (concept checks, `{concept, state, sampleSize, evidenceLabel}`), `playbook[]`, `dueReviews`, `milestones[]` (`{kind,title,detail,href}`), `note`. While `RELEASE_GATES.content` is false the concept checks are empty by design: show "No completed recovery checks yet. Ordinary practice is ready while sources and calibration are prepared." Fetch once on opening Review > Record, never on the home screens.

### D1 to D3 Explore and Saved

- Web Explore: untimed practice, one question at a time with instant feedback, separate from mock scores. Filters Subject (all non-merged subjects, default Accountancy), Chapter (grouped), Difficulty (All, Easy, Medium, Hard). `GET /api/questions/feed?subject&chapter&difficulty&limit=12&offset=` returns `{questions:[{id, subject, chapter, difficulty, body, options:[{key,text}], passage_text, passage_group_id, order_index, correct_answer (a key letter), explanation, tags, verification_state, source_refs, upvotes, downvotes, score, userVote, saved}], nextOffset, hasMore}`. Advance by `nextOffset` (raw rows are consumed before quarantine, so a page can be short or empty while `hasMore` is true: keep paging, show "No ready questions on this page"). De-dupe by id.
- Card behaviour: the question is "seen" at 40% visibility (`POST /api/questions/{id}/interact {interaction_type:"seen", flow_context:"explore", session_id}`); picking an option reveals correct or incorrect with the explanation ("Correct. Keep the reasoning." / "The answer is X.") and posts `attempted` with `dwell_ms` and `metadata.selected_key`; a skip posts `skip` (requires `dwell_ms`); a question with no usable key is disabled with "This question has no usable answer key. Try the next one." Save: `POST /api/bookmarks {questionId, saved, source:"explore"}` returns `{saved, count, limit}`; free limit 25 (402 "Free bookmark limit reached": say "Your 25 free save slots are full. Remove a saved question to make room.", no selling). Vote: `POST /api/questions/{id}/vote {vote_type:"up"|"down"|null}` returns `{score, upvotes, downvotes, userVote}`. Report: `interact {interaction_type:"report", ...}`.
- Aside: "Answer first. Then ask why." plus links to Saved and Review; "N questions solved in your recorded untimed practice" from `GET /api/learning/summary?subject=` `progress.solvedTotal` (render only that one field; the response also carries `topContributors`, which exposes other users and must never be rendered).
- App design: `/practice/stream`. A vertical pager (one question per page, swipe up for next; the Quick skin: solid, calm, no art), filter chips at the top (subject, chapter sheet, difficulty), option keys that fill like a bubble and then show ink check or the wrong trio plus the explanation rising 220 ms, Save and the quality vote as quiet icon keys, "Flag a problem" in the overflow. Offline: show the loaded page and "Connect to load more". Haptics: `selectionClick` on pick, `lightImpact` on save.
- Saved: `GET /api/bookmarks` returns `{questionIds, questions:[{id, subject, chapter, difficulty, body, options, correct_answer, explanation, tags, upvotes, downvotes, score, saved:true}], count}`; only items that pass the readable-content filter come back (ids can outnumber questions). Same card, answers already revealable; remove with a tap (`saved:false`). Cache the last list for offline review.
- Acceptance: answering shows the key only for explore and saved (these are practice surfaces), never inside a timed mock; the save count matches the server; every answer is recorded as `attempted` with dwell; goldens in both themes for question, revealed correct, revealed wrong, end of feed, empty filter, offline.

### E1 Compass: DU eligibility and cutoffs

- What it does for the student: pick CUET subjects (presets Commerce, Commerce + Maths, Science PCM, Science PCB, Humanities, or tick from 14 languages, 22 domain subjects and the General Aptitude Test; the profile subjects are pre-ticked, `general_test` maps to `gat`), see every one of 73 DU programme groups they are eligible for under the 2026-27 Bulletin, with which combination matched and, when not eligible, the nearest combination and the gap ("Mathematics or Applied Maths", "a language from List A"), "considered only if seats remain after Combinations I and II" for secondary combinations, `suggestUnlocks` (the subjects that would open the most more programmes), then open a programme to see college by college minimum allocation scores for Round I, II, III for the chosen category (11 categories: UR, OBC-NCL, SC, ST, EWS, SIKH, PwBD, KM, SGC, ORPHAN-FEMALE, ORPHAN-MALE; main vs other list), the effective cutoff being the lower of the UR and category cutoff (UR badge "Cleared on the Unreserved cutoff, which is lower"), an optional score (0 to 1000) or what-if that labels each college row "Clears Round I", "Clears Round II", "Clears Round III", "Below last year" or "No allocation recorded", search by college or programme, sort by fit or highest, 25 per page.
- Data: static JSON served from `/du/2026/index.json` (157 KB: `meta`, `languages`, `domains`, `groups` with `eligibility.combinations[].slots[{type:lang|domain|free, any|subject|count}]`), `/du/2026/rules.json` (65 KB), `/du/2026/offerings/{groupId}.json` (68 files; `rows:[[college, programme, r1[11], r2[11], r3[11]]]`, index by `meta.categories`, null for no seat). No API, no auth, no cost. Fetch from `https://www.mockmob.in/du/2026/...` with an on-disk ETag cache; bundle `index.json` as an asset for offline first run (ask the orchestrator to add the asset to `pubspec.yaml`: builders cannot edit it). The onboarding already bundles six Commerce courses (`du_2026_data.dart`, generated): Compass must use the full files, not that subset, and the generated onboarding data may later be derived from the same source.
- Port to Dart: `lib/du/eligibility.js` (178 lines: `evaluateGroup`, `evaluateAll`, `suggestUnlocks`, `describeGap`, `effectiveCutoff`, `seatStatus`, `explainCombinations`) and `lib/du/client.js` helpers. Keep the labels verbatim.
- Honesty: every number is "CSAS 2026, Round N" on a scale out of 1000. Copy: "Cutoffs are last year's. They are not a prediction and not an admission chance." Practice marks are never turned into a CUET score. 2027 rules are provisional until DU publishes its next Bulletin.
- App design: `/tools/compass` (subjects chips with a 5-subject limit, category chip, optional score key) then a list of eligible programmes grouped by stream; `/tools/compass/:groupId` shows rules (check and cross rows) then colleges. A "Practise" bridge: the weakest ranked chapter's subject from the insights opens setup for that subject (the site's `PracticeBridge`). Sources list (`lib/du/sources.js`) behind "Official source documents" opening in a Custom Tab.
- Acceptance: pick English, Accountancy, Business Studies, Economics, UR, score 650: B.Com (Hons) shows eligible and each college row shows a status from the dataset; remove Accountancy and Mathematics and B.Com (Hons) shows not eligible with the exact missing rule; works offline after one load; no figure is invented; TalkBack reads status and round.

### E2 Combo Planner

- Does: the student lists target DU programmes (up to 6; quick picks B.Com (Hons.), Economics, English, Political Science, Psychology, B.A. Programme) and the subjects they could take (pool up to 12), a paper limit 3, 4 or 5 (default 5, provisional for 2027); the planner tries every subset up to the limit against the same evaluator, ranks combinations by targets unlocked, total programmes unlocked, fewest papers, and shows which targets each combination misses and why. No scores, no chances. Choices stay on the device.
- Port `lib/du/combos.js` (84 lines, depends on E1's evaluator). Cap compute with an isolate or `compute` (12 choose 5 is 792 subsets times 73 groups: fine, but keep it off the UI thread).
- Acceptance: with targets B.Com (Hons.) and Economics and a pool of English, Accountancy, Business Studies, Economics, Mathematics, General Test the top result matches the website's top result for the same input (use the site as the oracle in a test with a fixed fixture).

### E3 Compass Pro (Pro)

- `GET /api/compass/pro` returns `{ok:true, locked:true}` for free accounts, else `{ok, locked:false, projection, sessions}`: a practice projection from server-scored marks with a Wilson range per paper (`needed` more questions when thin), shortlist (up to 8, stored on device per user) compared with published 2026 cutoffs, and the one paper to work on. Labelled "a projection from your own practice, not a prediction or a normalised CUET score". P1.

### E4 CUET 2027 guide and E5 hubs

- `/cuet-2027` is a static guide (timeline: registration expected February to March 2027, exam May 2027, results late June or early July, then CSAS; the latest completed cycle is only a reference; month-by-month plan; FAQs). App: one native screen with the same facts and "expected" wording, links to Combo and Compass. Subject hubs (`/cuet/[subject]`, six subjects), the PYQ guide (the site says it does not claim a verified historical inventory) and the free-mock pages are SEO text: open in a Custom Tab (P2).

### F1 Edit subjects

- Web: `/onboarding?edit=true` lists subjects with `practice == supported` (15), pick up to 5, saved subjects without practice shown with Remove, `PATCH /api/users/{id} {subjects:[public ids]}`. The server's `profilePatch` accepts only `name` and `subjects`, at most 5 unique ids from the registry (400 with a message otherwise), then `GET /api/auth/me` to refresh. The app already calls this in `sheet_sync.dart` for onboarding.
- App: `/you/subjects`, reached from You > Subjects (the sheet card row), the Practice subject tiles ("Edit"), the stale-subject banner and the deep link `/onboarding?edit=true`. Subject rows use the shared art for all 15 (owner: subject art for every subject; map in section 7). On save: only after the 200, refresh `auth/me`, then Practice, Today and the quote re-read. Removing the subject used by a stored draft keeps the draft resumable but marks it "Not in your subjects".
- Acceptance: choose 5, a sixth is refused inline; saving with no change is disabled; a failed save keeps choices and says so; goldens both themes.

### F2 and F3 Name and plan

- F2: `PATCH /api/users/{id} {name}` (1 to 80 chars, trimmed), then refresh. Inline edit on You > Account.
- F3: show Free or Pro badge, practice credit balance (`creditBalance`, or "unlimited" for Pro), `premiumUntil`, `razorpaySubscriptionId` presence (renews monthly vs fixed access date) as text, and "Manage your plan on mockmob.in" as plain text, not a link (the app never sells; cancel renewal is cookie-only `POST /api/billing/cancel`). The quote's `reason` explains any block.

### F5 Guided tour

- Web: a four-step spotlight tour (Today, Practice, Review, Progress) with Pip at each step, shown once per user (`mockmob_app_tour_seen_{userId}`), replayable from "Guide". App: a three-step spotlight on Today, Practice, Review plus Start, with Mobi pointing, shown once per account after the first result, replayable from You > Help. P1; depends on the Mobi animation package.

### G Community and the rest (all P2, reasons in section 10)

---

## 5. NTA mode: complete spec (P0, the owner's explicit ask)

The website's NTA mode is the same runner (`TestPageClient.jsx`) with `mode=nta`: 50 questions, 3600 s, `difficulty` mix 30/45/25, original practice content, Pro only (`quote.reasonCode == access_required` for free). It is the most complete exam simulation in the product. Every behaviour below exists on the site and must exist in the app. Source of truth: `TestPageClient.jsx`, `nta-classic.css`, `ExamIntegrityGuard.jsx`, `data/exam_integrity.mjs`, `NtaConsolePreview.jsx`, `ExamComparator.jsx`.

### 5.1 Behaviour table

| # | Website behaviour | Native implementation | App today |
|---|---|---|---|
| N1 | Practice card "Closest to exam day": 50 Q, 60 min, palette, mark for review, original questions, not official papers; live mini-console preview; Pro badge | Practice row "NTA mode" with the same four facts; no animated preview (decoration); the tag comes from the quote | Row exists (gated) |
| N2 | Exam screen choice before start: "MockMob style" or "NTA style" (Pro), switchable inside the test without losing answers or time; also `?interface=nta` | Segmented key on the pre-start sheet; remembered per device in prefs; a toggle in the runner overflow; state is presentation only | Missing |
| N3 | Preparing screen: "Building your verified {subject} mock", 3 steps (Checking available evidence, Selecting your question mix, Creating your session), "This can take up to 30 seconds" | Pre-start stage view with the same three steps driven by real phases (quote, start request, draft write); failure maps `INSUFFICIENT_*` to the exact messages; this also fixes the owner's "just loading the score" complaint for practice | Partial (spinner) |
| N4 | Start refused unless the server returns exactly 50 questions: "The database returned N usable NTA questions for this subject; 50 are required." | Same rule; show `meta.message` when `insufficientHighQualityPool` | Missing |
| N5 | Entry overlay "Enter your exam space": explains fullscreen, the three rules, timer already running | Pre-start sheet lists the rules; entering the runner sets sticky immersive (exists) and wakelock (exists) | Partial |
| N6 | Header: title stack "NTA Mode / {Subject}", "Question i of N", "{answered} answered", progress bar, countdown (red under 60 s, `role=timer`), warnings pill "Warnings n/3" | Same in both skins. In NTA style the bar is NTA blue `#32688F` with white text; MockMob style uses the runner's own top bar plus the pill | Partial (timer, count) |
| N7 | Passage sets: the passage (title, text) shown once with all its questions stacked as one block; Next and Previous move by block (`startIdx`, `endIdx`), visiting a block marks every question in it visited | Passage well on top (max 40% height, own scroll) and questions stacked beneath; navigation by block; "Questions 3 to 6 use this passage" line | Partial (well and range exist; block navigation to confirm) |
| N8 | Per question: number, state chip (Answered, Marked, Visited, Not visited, Answered + marked), Mark/Unmark, Clear, options A to D (E), selected state | Same; chip text uses words, not colour alone | Partial (mark, clear exist) |
| N9 | Navigation, MockMob style: Previous, Next (last block: Submit Test) | Bottom bar: Previous, Palette, Next / Review and submit | Done |
| N10 | Navigation, NTA style: **Mark for Review and Next** (purple), **Clear Response**, Previous, **Save and Next** (green; last block: Submit Test) | Two-row action area on phone: row 1 Mark for Review and Next, Clear Response; row 2 Previous, Save and Next | Missing |
| N11 | Review panel: summary grid Answered / Marked / Pending / Not visited, palette of 50 numbered chips in 5 states, current chip ringed, legend with the 5 states, Submit test | Palette bottom sheet on phone (opened by Palette); a permanent right panel (292 dp) at 840 dp width or landscape; summary grid and legend identical | Partial (sheet, counts) |
| N12 | Palette chip states and NTA style shapes: answered green pentagon-ish, not answered orange-red, not visited light grey, marked purple circle, answered and marked purple circle with a green dot | NTA skin draws those exact shapes with `CustomPainter`; MockMob skin uses the answer-sheet bubbles (filled ink, outline, sunken, flag, flag with fill); both carry the number and a semantic label ("Question 4, answered and marked for review") | Partial (MockMob only) |
| N13 | Submit confirm: "You have N unanswered questions and M marked for review. Submit anyway?" | Sheet "Submit now?" with the same counts (exists) | Done |
| N14 | Auto-submit at zero; offline pending submission retried on reconnect within the 120 s window; messages for expired window | Exists in the engine | Done |
| N15 | Integrity: fullscreen exit, tab hidden, window blur are warnings; third warning submits current answers; strikes persist across reload (`localStorage`); answering blocked while the overlay shows; copy, paste, cut, context menu blocked; fine print "not server-verified proctoring" | Android: leaving the app (`AppLifecycleState.paused` or `hidden`) is a warning; `inactive` for more than 3 s is a warning (split screen, overlay); each away period counts once until return; strikes persist by `sessionId` in prefs; overlay on return "Warning n of 3" with the rules and a Continue key; 3rd warning flushes the journal and submits; answers blocked while the overlay shows; no selectable text in the runner; `FLAG_SECURE` on the window in NTA mode only (blocks screenshots and recents thumbnails); fine print kept | Missing |
| N16 | No exit (X) in NTA mode; the vote controls are hidden | Android back opens "Leave this mock?" (exists); no vote anywhere in a timed mock | Partial |
| N17 | Keyboard: 1 to 4 pick, arrows move | Hardware keys on tablets and keyboards: same | Missing, S |
| N18 | Result: same attempt, same result page | Sealed sheet and recap for `mode == nta` (exists) | Done |
| N19 | Free "Meet the exam before exam day" preview: 5 sample questions, both screens, switchable, demo clock, no account | `/practice/exam-preview` from the Practice NTA row when the quote says Pro is required: bundled five questions (the warm-up pool exists in onboarding), both skins, local only, no scoring, no network, no records | Missing (P1) |
| N20 | Disabled controls: options disabled while pending submission, time up or submitting | Same | Done |

### 5.2 Layout and states

- Phone portrait 360 to 420 dp: header 56 dp, sub-row with warnings pill and save state, content scrolls, bottom action area 72 dp (MockMob style) or 120 dp (NTA style, two rows). Tablet and landscape at 840 dp or more: two panes (paper on the left, review panel 292 dp on the right) exactly as the site's `.nta-grid`.
- NTA skin pins its own light palette in both app themes (as the site does: `color-scheme: light`, Arial, white panels, blue header, green and purple buttons). MockMob skin follows the app theme. Contrast 4.5:1 on every text.
- Haptics: `selectionClick` on pick and palette tap, `lightImpact` on Save and Next, `mediumImpact` on a warning. No sound, no flash, no red pulsing; the low-time state is the timer colour plus the existing 5 and 1 minute banners.
- States to design: preparing, entry sheet, running, warning overlay (1, 2), final warning submitting, offline, pending submission, time up, sent, not recorded.

### 5.3 Policy decisions made (no owner question needed)

1. Warnings apply to NTA mode only, not to Full mock; the Full mock keeps the calm "timer keeps running" model (APP-DESIGN-SPEC 5.5).
2. Copy is plain and unshaming: "You left the exam. Warning 1 of 3." The fine print states this is a practice safeguard on the phone, not server-verified proctoring (verbatim from the site).
3. Strikes are not sent to the server and do not change the score; the third strike submits like the site.
4. A phone call or the notification shade does not count (they produce `inactive` for less than 3 s or no change); an incoming call that backgrounds the app does count once, same as switching tabs on the site, and the overlay explains it.
5. `FLAG_SECURE` is NTA-only; if the platform channel is not available the rest still ships.

### 5.4 Acceptance (NTA)

Device-gated: start NTA on an account with Pro; switch skins mid-test and answers, marks and time persist; background the app: warning 1 shows on return and answering is blocked until Continue; do it three times: the answers submit and the sealed sheet opens; kill the process after warning 2 and reopen: still warning 2; a passage set shows its passage once with all its questions and Next jumps past the block; Mark for Review and Next marks and moves; Clear Response clears; the palette shows five distinct states (also in grayscale: shapes and words differ); 50 of 50 required; goldens at 384 x 853 DPR 2 for both skins, both themes, states running, palette open, warning overlay, final submit, and a two-pane tablet frame.

---

## 6. Website polish the app lacks (beyond whole features)

Practice setup: live question counts per subject (`/api/stats` `subjectCounts`, "Count unavailable" when absent); "About N minutes" from `durationSec`; chapter search; mode badge text (Included, Needs access, N credits) taken from the quote not constants; the summary dl (Subject, Mode, Questions, Time, Marking +5/-1, Cost); the wallet strip; recent sessions with score tone (70 and over good, 40 and over mid) and a Review mistakes link; "Usable questions" and sessions and average; launch toast; quote re-check at expiry; post-mock "credits left" line for free accounts (the site pops a modal after a mock; the app shows one quiet line on the receipt).

Runner: sync line in words (offline, pending, saved); `meta.message` shown for an insufficient pool; passage grouping; exit confirm text "Your progress is saved and you can resume".

Result: the gap bar and its 6-mark rule; observations; time per answer; answer-change markers on the strip; filter chips; per-answer report; correction and key-review notices (exist for review states); links to Insights; "Continue on your phone" QR is web-only (skip).

Review: due-card line; Saved and Insights rows; session cards show the to-review badge or "All correct".

Today: tonight recorded; sequence; record finding.

Learn: chapter summary; subject tabs show lesson counts; "untaught chapters" list ("practice available, lessons later") with Practise keys and the provisional-2027-syllabus note; the Learn to Lock in to Apply three-step explainer; study record line.

Account: Plan card text; edit name; edit subjects; usage-data text matches the site's wording ("Allow usage data to improve MockMob").

Empty, error and loading states: the site pairs each with the Mobi companion poses (attentive, encouraging, celebrating, greeting); the app should use the animated Mobi for the same states (separate package).

Dots and bubbles audit (owner: "how useful are they"): keep where the dot is a state or a link: runner palette bubbles (answered, marked, not visited, unsynced), result strip (verdict per question, tap opens it), week bubbles on Today (study days, tap opens the week), sheet rows with Show me (evidence). Remove or convert where it is only decoration: the dot beside a label with no action, repeated bubble rows that repeat a number already on screen, bubbles under mode rows that carry no state. New rule for builders: if a bubble cannot be tapped and does not encode a state, delete it.

Subject art: the site's `SubjectIcon` covers every subject id. The app has five lamp objects (accountancy, business, economics, english, general test). Needed for all 15 supported subjects: mathematics, physics, chemistry, biology, history, political science, geography, psychology, sociology, computer science. Proposal (code-drawn objects in the same warm lamp style, no new generated images): mathematics a drafting compass over graph paper; physics a pendulum or prism; chemistry a flask; biology a leaf over a cell; history a scroll with a seal; political science a ballot box; geography a globe on a brass stand; psychology a head silhouette with a bubble; sociology three linked figures; computer science a terminal prompt block; general test a clock and sheet (exists). Map by public subject id and always fall back to a monogram tile with the subject's initials, never a wrong object.

Weekly rhythm and milestones (owner: "needs more thought"): data the server already gives and the app does not use: `GET /api/me/rhythm` `milestones[]` ids (first_scored_session, first_full_mock, first_repair, repairs_5/10/25, sessions_10, first_week_met, weeks_met_4) with `achievedAt`; `GET /api/learning/plan` `milestones[]`; the weekly plan (B4); `GET /api/me/bests`. Tie milestones to something the student does next (each token links to the record behind it) and show the next unearned one with its exact condition (for example "5 repairs: 2 to go").

---

## 7. Subject coverage (15 supported ids from `GET /api/subjects`, `practice == supported`)

english, general_test, accountancy, business_studies, economics, mathematics, physics, chemistry, biology, history, political_science, geography, psychology, sociology, computer_science. `applied_mathematics` is merged into mathematics: never offer it. The session API and the quote take the public id; `attempt.subject` and snapshots use `internalId` (general_test is `gat`). Free first-use allowances (`baseline`, `full_sample`) and fresh-question replay exist for the four launch subjects only. `GET /api/chapters` returns units for unit subjects: render unit headers.

---

## 8. API notes builders must know

Changed since `APP-API-CONTRACT.md` (read the route handlers, not only the contract):

- Now Bearer-ready: `/api/questions/feed`, `/explore`, `[id]/vote`, `[id]/interact`, `/pending`, `/api/bookmarks`, `/api/learning/summary`, `/api/ai/credits`, `/usage`, `/api/ai/mentor/chat`, `/history`, `/api/compass/pro`, `/api/prepos/insights`, `/api/users/[id]` GET and PATCH.
- `PATCH /api/users/[id]` is allowlisted (`profilePatch`): only `name` (1 to 80) and `subjects` (up to 5, registry ids). The privilege-escalation note in the contract no longer applies to this route.
- New routes: `GET /api/me/bests`, `GET /api/me/repair-record?limit=`, `POST /api/me/sample-import`, `GET /api/attempts/summary?cursor=&limit=` (the slim list; use it instead of `GET /api/attempts` everywhere you can), `POST /api/sessions/{id}/check {qid, answer, sessionTicket?}`.
- `POST /api/sessions/{id}/check` exists but answers 403 `check_not_available` unless `SESSION_CHECK_ENABLED=1` on the server, and only for `quick` and `smart` ordinary practice; a checked answer is final. Use it for per-answer feedback in the Quick skin when it answers 200 and fall back to feedback-after-finish on 403. Never call it in Full or NTA.
- `GET /api/stats` is public and cached 30 s: `subjectCounts` keyed by `internalId`.
- Explore and Saved return `correct_answer` and `explanation` to the client by design. They are untimed practice surfaces; never use them for exam-style modes.
- `/api/leaderboard` is public, unpaginated, includes 12 synthetic "practice rivals" and every user's name: do not call it.
- `/api/learning/summary` `topContributors` exposes other users: never render it.
- `chapters` is comma-joined (comma-in-name bug). Request `Array.isArray(input.chapters)` support in `practiceSessions.js:31` (one line); until then single chapter for such subjects.
- Rate limits to respect: mentor chat 20/min, prepos insights 60/min, learning routes share 60/min, sessions 60/min, replay 30/min, repair 12/min.
- Cookie-only (P2): ai/rival/start, ai/rival/submit, ai/mentor/local, ai/mentor/session/new, ai/context, ai/actions/execute, ai/credits/order and verify, billing/cancel, questions upload, mine, moderate, questions (POST), creator/me, admin/*.
- DU data is static and public: `https://www.mockmob.in/du/2026/index.json`, `rules.json`, `offerings/{id}.json`.

Pro gating the app must render from the server, not from constants: Smart and NTA (mode capability `access`), `difficulty` for every mode, `weeklyPlan`, unlimited bookmarks, Compass Pro, Insights depth (chapters beyond 3, changed answers, pace). Free practice: Quick 10 credits, Full 50 credits, plus the `daily_practice`, `baseline:*` and `full_sample:*` allowances from the quote.

---

## 9. Work packages for this pass (parallel builders)

| WP | Scope (IDs) | Owns | Depends on | Size |
|---|---|---|---|---|
| WP1 | NTA console (A5): skins, palette shapes, strikes, preparing stage, two-pane, free preview (P1 part last) | `features/runner/**` (NTA skin files new), `features/practice/widgets/mode_list.dart` row | `SessionDraft` key from WP2 | L |
| WP2 | Practice setup parity and deep links (A2, A3, A4 Smart): chapters multi-select, difficulty, summary, counts, stale subjects, router mapping, draft key | `features/practice/**`, `core/router/action_router.dart`, `core/models/session_draft.dart` key | none | M |
| WP3 | Result depth and Prove (A7, A8, A9 part, A13): gap bar, observations port, filters, timing, changes, report, fresh-5, practice finish moment | `features/result/**`, `features/practice/practice_result_screen.dart`, domain port `core/domain/session_analysis.dart` | none | L |
| WP4 | Insights and Ask your record (C1, C2, C3 local, Today finding, Review rows, A11, A12) | new `features/insights/**`, `features/review/**` rows, `features/today` finding | none | M |
| WP5 | Explore stream and Saved (D1, D2, D3) | new `features/explore/**` | none | M |
| WP6 | Compass and Combo (E1, E2) with DU data layer and eligibility port; tools hub | new `features/tools/**`, `core/domain/du/**` | asset request | L |
| WP7 | Account: edit subjects, name, plan card, study preferences (F1, F2, F3, B3) | `features/you/**` | none | S to M |
| WP8 | Subject art for all 15 subjects (section 6) | `core/widgets/art/**` | none | M |
| WP9 | P1 queue: Compass Pro, chapter summary, weekly plan, study sequence on Today, guided tour, CUET 2027 guide, playbook list | various | WP4, WP6, Mobi package | M to L |

Shared files to serialise: `routes.dart`, `router.dart`, `screens.dart` (each package adds its own `*_routes.dart` export, as the existing code intends), `copy` files per feature. `pubspec.yaml` asset additions: `assets/du/index.json` and `assets/du/rules.json` (request through the orchestrator).

---

## 10. P2 and deliberately not built

| Feature | Why | What the student gets |
|---|---|---|
| Leaderboard (`/leaderboard`) | APP-DESIGN-SPEC 6.10 bans leaderboards; the endpoint lists every user's name and 12 invented rivals (G7); minors | Personal bests and rhythm instead (already in You) |
| Rival benchmark (`/rival`) | Cookie-only routes; paid battles paused (`aiCommerce:false`); opponents are simulated profiles | Nothing; revisit after a privacy decision |
| Upload, My uploads (`/upload`, `/my-uploads`), earning credits for approved questions | Cookie-only; moderation workflow; creator tool | Custom Tab link from You > Help to mockmob.in |
| Moderation, Creator dashboard, Admin | Role-gated, not student | none |
| Pricing, checkout, cancel renewal | The app never sells (binding rule 13; `ActionRouter` refuses commerce prefixes) | Read-only plan state (F3) |
| Handoff QR, PWA install, AppNudge, landing, SEO hubs, PYQ guide, free-mock pages | Web-only marketing | Custom Tab where useful |
| AI lesson help (B5), model replies in Ask (C3 model path) | Credits and an unfinished commerce state | Free record answers (C3 local) |
| `/api/analytics` advanced scores | Rank-readiness conflicts with the no-prediction rule | Insights (C1) |

---

## 11. Decisions made (no owner question was asked)

1. Practice gets a real animated finish (A13) even though APP-DESIGN-SPEC 5.4.1 said none; owner feedback 1110 wins. Mocks keep the sealed-sheet ritual.
2. NTA mode gets its own console with two skins and warnings (A5), overriding the spec's "same runner skin"; Full mock stays calm.
3. Explore, Saved and Insights live inside Practice and Review, not new tabs (the dock the owner praised is unchanged).
4. Compass and Combo are native, from the public static DU files, not Custom Tabs.
5. No call to `/api/analytics`, `/api/leaderboard`, or `topContributors`.
6. Trend and by-subject come from `/api/attempts/summary`, compared by `formatId`, never mixing formats.
7. Pro-only features show a "Pro" tag and the server's reason; no purchase path in the app.
8. The first record finding on Today is evidence-first (Show me) or absent.
9. Subject art for the ten missing subjects is code-drawn in the existing lamp style with a monogram fallback.
10. Multi-chapter selection is limited to subjects without commas in chapter names until the server accepts an array.
