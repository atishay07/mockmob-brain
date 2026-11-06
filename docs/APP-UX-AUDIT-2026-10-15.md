# App UX audit, 15 Oct 2026 (after the owner's APK v8 test)

Auditor key: "audit". Read-only pass over the Flutter app in `wt-phase2/flutter_app` (branch ui/phase2, head 00b875eb), its goldens, and the production server routes in `wt-usage` (production main, head 48309076). Nothing was edited, built or run on a device. Production was only read: two `SELECT`s on Supabase (`auth.flow_state`, `information_schema`, `pg_proc`) and the Vercel runtime-error clusters for the last 24 hours.

Paths below are relative to `wt-phase2/flutter_app` unless they start with `src/` (server, `wt-usage`). "Verdict" is CONFIRMED when code and an artefact (golden, database row) agree, PLAUSIBLE when the code makes it likely but no device run proved it.

Areas owned by another agent right now (Mistake Lab slice 3): `lib/features/result/**`, `lib/features/review/**`, `lib/features/you/**`, `lib/core/models/**` and the NTA pre-paper instructions screen. Findings that land there are marked **[other owner]**. Hand them over; do not edit them in a parallel wave.

## 1. The owner's v8 report: root causes

| What he saw | Root cause | Evidence | Verdict |
|---|---|---|---|
| Google sign-in "doesn't redirect me to the app" | Supabase does not allow the app's return address, so it sends the code to the website instead. One-tap is also off. | `auth.flow_state` today: the Google flows at 14:32, 14:33, 14:41 and 14:55 UTC (his test) have `referrer = https://www.mockmob.in`, three of them with a code issued. The app asks for `in.mockmob.app://login-callback` (`lib/core/auth/auth_service.dart:430-436`, `lib/core/auth/auth_links.dart`). `mockmob-next/flutter_app/dart_defines/prod.json` has `GOOGLE_WEB_CLIENT_ID` empty, so only the browser flow runs. Owner step S1 in `docs/AUTH.md:230-234` was never done. | CONFIRMED |
| "Couldn't load" card at the top of Today; Try again does nothing | The server reads failed, and Today's error card cannot say why, or that a retry also failed. Per the orchestrator, the Vercel checkpoint that blocked the app is now off. That fixes the cause but not the card. | `lib/features/today/logic/move_builder.dart:181-191` (historyUnavailable card: "Your earlier results are still there." / "Could not load a suggestion." / Try again). `lib/features/today/screens/today_screen.dart:82-90`: a fast refusal flashes the key's spinner and the identical card comes back. Golden `test/golden/today/goldens/today_error_night.png`. | CONFIRMED (copy and flow); cause per orchestrator |
| Back "is just exiting the app" | Back from the Today tab closes the app at once. There is no second-press guard. | `lib/core/router/app_shell.dart:394-399` (`canPop: shell.currentIndex == 0`) | CONFIRMED |
| NTA mode tile "boxes and checkboxes going out of the area" (Practice and Start) | The NTA glyph's bottom row of cells is drawn below its panel. | `lib/features/practice/widgets/choice_glyphs.dart:419-460`: the cells start at y 7.1 and end at 7.1 + 3×4.4 + 2×1.5 = 23.3 units, but the panel ends at 2.4 + 19.6 = 22.0. The same glyph is used on the Practice tab (`practice_screen.dart:403-411`) and in the Start sheet. Golden `test/golden/practice/goldens/quick_start_deck_night.png` shows the grey row hanging out. | CONFIRMED |
| "Your colleges": tapping Choose shows "Could not load a suggestion"; then Start does nothing | Choose pushes the You tab root from inside the shell. It never opens a college picker. | `lib/features/today/screens/today_screen.dart:140` `context.push(AppRoutes.you)`. `lib/core/router/router.dart:200-203` notes that pushing a route inside the shell can build the shell a second time. Even when it works, You has no direct college picker (see finding 5). | Push target CONFIRMED; the duplicate shell PLAUSIBLE |
| Home "added another section ... 1 of 4" | The week strip appears only after the rhythm read succeeds, with no reserved space, so it pops in later. | `lib/features/today/data/today_providers.dart` (`week` is null until `rhythmSnapshotProvider` has data); goldens `today_error_*` show the strip above the card | PLAUSIBLE |
| Compass "why is it asking for my score?" | The second block of Compass asks for a "programme-specific CUET score" from the "CSAS dashboard", which a Class 12 student does not have in October. | `lib/features/tools/copy.dart:50-60`, `lib/features/tools/compass/compass_screen.dart:142`; goldens `compass_full_night.png`, `compass_category_sheet_day.png` | CONFIRMED |
| "Where's the option to do light or dark mode?" | The theme is only under You > Settings > "Appearance and feel", about 1,500 dp down the You page. It says "Night/Daylight", never "dark/light". | `lib/features/you/hub/hub_sections.dart:83-91`; golden `test/golden/you/goldens/hub_full_page_night.png` (Settings starts about 1,500 dp down) | CONFIRMED |

## 2. Top 25 findings, ranked by impact

P0 = blocks use or risks a student's work. P1 = the owner will hit it this week. P2 = polish he already named, or will.

### P0

**1. Google sign-in never returns to the app.**
Evidence: see table row 1. In Supabase, the Google flows started by the app today all have the website as their referrer.
Fix: (a) Owner step, two minutes: Supabase > Authentication > URL Configuration > Redirect URLs, add exactly `in.mockmob.app://login-callback` (AUTH.md S1). (b) Fill `GOOGLE_WEB_CLIENT_ID` in `dart_defines/prod.json` and create the Android OAuth clients (AUTH.md G1-G3), so the native account sheet is used and the browser is not needed. (c) App: when the app resumes in the "finish in your browser" wait with no callback within about 5 s, say "Google sent you to the website, not the app. Use an email code for now." and focus the email field (`lib/features/auth/sign_in_controller.dart:146-148`).

**2. Today's error card stays the same after Try again and says something untrue to new students.**
Evidence: `move_builder.dart:181-191`; `today_screen.dart:82-90`; `today_error_night.png`. "Your earlier results are still there." is shown even to an account that has no results. A failed retry gives the same card back, so the key looks dead.
Fix: keep a retry count in `TodayScreen`. After a failed retry, the line changes to "Still not loading. MockMob did not answer the app. Anything you did is safe on this phone.", with "Tried at 8:41 PM". Make "Practise anyway" the primary key once a retry has failed. With no cached attempts, use "Your first move shows here once MockMob answers." Today copy lives in `lib/features/today/copy.dart:117-120`.

**3. A 403 from an edge firewall is treated as the server refusing the work, which can end a submitted paper and drop queued writes.**
Evidence: `lib/core/api/api_error.dart:128-142` and `:269` (any 403 is `forbidden`, which counts as a definitive refusal); `lib/core/sync/session/session_submitter.dart:145-148` marks the draft `rejected`; `lib/core/sync/outbox_repository.dart:216-224` removes the item. Nothing in `lib/core/api` looks for `x-vercel-mitigated` or an HTML body (grep found no "vercel", "challenge" or "text/html"). The checkpoint the owner hit today is the same kind of event.
Fix: in the API client, classify a non-JSON body, or any response carrying `x-vercel-mitigated`/`x-vercel-challenge-token`, as a new retryable `ApiErrorKind.blocked`. It is never definitive. Give it one plain line ("MockMob's server is not letting the app in just now. Your work is kept.") and an analytics event, so the next checkpoint is noticed within minutes. Verdict: PLAUSIBLE (it depends on the status Vercel returns), but cheap and important insurance.

### P1

**4. NTA mode glyph overflows its panel (Practice tab and Start sheet).**
Evidence: table row 4. Fix in `choice_glyphs.dart` `_nta`: `cell = 4.0`, `gap = 1.3`, `originY = 6.9`, so the cells end at 21.5, inside the 22.0 panel. Or grow the panel to `Rect.fromLTWH(2.2, 2.4, 19.6, 21.2)` and re-centre. Regenerate and open the practice goldens (`quick_start_deck_*`, `tab_*`, `subject_art_all_*`). While there, top-align the two pair tiles: in `quick_start_deck_night.png`, the Full mock title sits about 36 dp lower than NTA mode's because the notes differ in length.

**5. "Choose your colleges" leads nowhere useful.** (Today is free to change; the You side is **[other owner]**.)
Evidence: `today_screen.dart:140` pushes `/you`, a tab root. On You, the Course and Colleges rows look like list rows but cannot be tapped. Only Subjects has `onEdit` (`lib/features/you/hub/sheet_card.dart:253-254`). Colleges are changed only through the "Edit" pill, then the sheet editor, then the colleges sheet, and a course must be chosen first.
Fix: Choose opens the colleges chooser directly, as a sheet over Today: the sheet editor's colleges sheet, or Compass's programme page with an "Add to my colleges" key. Never `push` a tab root; use `go` when a tab is really meant. Make the You Course and Colleges rows tappable.

**6. Two college lists that never meet.**
Evidence: Today's "Your colleges" ladder (up to 3, from the student's sheet, `lib/features/you/data/student_target.dart`) and Compass Pro's "Your DU shortlist" (up to 8, stored only on the phone, `lib/features/tools/data/tools_store.dart:103-124`; golden `compass_pro_night.png`). A college added in Compass never appears on Today, and the reverse.
Fix: one list, "My colleges", saved on the server. Add to it from Compass college rows, from Today's ladder and from You. Today shows the first 3 and a count of the rest.

**7. Compass asks for a score students do not have, and ignores the projection it already computes.**
Evidence: `tools/copy.dart:50-60`; `compass_full_night.png` puts "Category and score, Unreserved. No score yet" as the second block. `compass_pro_night.png` shows "Practice projection 640 of 1000" lower down, while the score row above still says "No score yet".
Fix: split the block into "Your category" (a chip row, kept near the top) and "Try a target score (optional)", which moves below the programme list. Prefill the score with the practice projection when there is one ("Use my practice estimate, 640"). Drop "From your CSAS dashboard" and use "Round 1" instead of "Round I".

**8. Compass programme list has no hierarchy and no pull to open.**
Evidence: `compass_full_night.png`. Every row reads the same: title, "55 colleges", "Round I, unreserved: 645.3 to 924.3". A B.Voc row with 1 college carries as much weight as B.Com (Hons) with 55. "Unreserved" repeats on every row although the header already says it.
Fix: lead with "Best fits for your subjects", the top 3 programmes as cards that name 3 real colleges and mark "My colleges". Fold programmes with fewer than 5 colleges into a collapsed "Smaller programmes (9)" row. Each row says "Cutoffs 645 to 924" plus a "See 55 colleges" chevron. Show one decimal only in the college table. Files: `lib/features/tools/compass/compass_screen.dart`, `programme_rows.dart`.

**9. CUET tools are hidden in three quiet places.**
Evidence: the You hub's last section (`hub_full_page_night.png`, about 1,900 dp down); the "quiet link" under Today's road (`lib/features/today/today_routes.dart:17`, `ToolsQuietLink`); and Practice "More" (`lib/features/practice/widgets/more_rows.dart:29-31`). The owner: "it has to be integrated, not hidden below something."
Fix: give colleges their own tab (section 4). Until then, put a Compass summary card ("35 of 73 DU programmes open to your subjects") inside Today's road section, above "Your colleges".

**10. The light or dark switch cannot be found.** **[other owner: you/appearance]**
Evidence: table row 8. It is called "Appearance and feel", and its tiles say Night, Daylight and Match phone (`appearance_day.png`).
Fix: a one-tap theme toggle in the new profile sheet (finding 11). Rename the row "Theme and appearance" and the tiles "Night (dark)" and "Day (light)", keeping the warm names as subtitles.

**11. No profile or account button at the top of any screen.**
Evidence: the tab root header is built with "no avatar" on purpose (`lib/features/you/you_hub_screen.dart:117-119`). Today's header shows Mobi, not the student. The owner expects the usual app pattern, a top-bar avatar.
Fix: an initials avatar (48 dp target) at the top right of every tab root (`TabRootHeader`, `lib/features/today/widgets/today_header.dart`). It opens Profile and settings (section 3). Mobi stays in the hero, not in the header.

**12. Credits have three names, and You shows only one balance.** **[mostly other owner]**
Evidence:
- Account: "40 practice credits" (`lib/features/you/edit_copy.dart:117-126`, `account_free_night.png`).
- Ask: "Other questions use 1 AI credit. You have 18." (`lib/features/insights/copy.dart:169-177`, `ask_start_night.png`).
- Repair: "Uses 1 credit per mistake. You have 9." and "explanation credits" (`lib/features/review/copy.dart:168, 179-180`, `repair_entry_night.png`).
- Practice says "Your credits show in You" (`lib/features/practice/copy.dart:217`), but You shows practice credits only.

The server keeps two ledgers (`src/app/api/ai/credits/route.js:44-46`: `practiceCredits` versus the AI `wallet`). No screen and no endpoint shows a history.
Fix:
- Two names only: "Practice credits" (mocks and practice) and "AI credits" (Ask Mobi and repair explanations). Every spend line names its pool: "Uses 3 AI credits, 1 per mistake. You have 9."
- One Credits page under Profile showing both balances, the renew date and a history list.
- A new read-only `GET /api/me/credits/history` over `ai_credit_ledger` and the practice ledger.

**13. Repair costs are stated per mistake but never as a total, and the two quick ways in show no cost at all.** **[other owner for the entry screen]**
Evidence: `repair_entry_night.png` says "3 mistakes" and "Uses 1 credit per mistake", but never "3 credits". The Start sheet row "Repair the next mistake" (`lib/core/router/quick_start.dart:520`) and Today's "Start repair, 10 min" key show no cost.
Fix: the entry screen says "This repair uses 3 AI credits. You have 9.". Add a quiet "AI credits" fact chip on the Start row and under Today's repair key.

**14. Back closes the app from Today.**
Evidence: `app_shell.dart:394-399`.
Fix: in `onPopInvokedWithResult` on branch 0, the first back shows a snackbar ("Press back again to close MockMob", 2 s) and the second exits. Back on any other tab still goes to Today first.

### P2

**15. The Road to May is below the fold with nothing pointing to it.**
Evidence: Today's order (`lib/features/today/screens/today_body.dart:440-455`) is header and week, hero, also slots, insights, weekly ending, Recent papers, then the road. In `today_day_one_full_night.png` the road starts about 775 dp down, under the bar.
Fix: a "28 weeks to CUET" chip in Today's header row that scrolls to the road with `Motion` tokens. Also add a soft down-chevron cue under the hero that fades after the first scroll. For students with fewer than 3 papers, put the road above Recent papers.

**16. The road cannot be changed or explored.**
Evidence: the only tap target is the walker (`lib/features/today/widgets/road_timeline.dart:293`). The owner wants "the board", interactive and editable.
Fix:
- Tap "Class 12 boards" to choose your board (CBSE, ISC, a state board); the bar shows that board's dates.
- Tap a month to open its plan from the CUET 2027 guide, which already exists in tools.
- "Remind me" on CUET registration (a local notification).
- Study days per week editable inline (the rhythm goal).
- The colleges ladder marks the student's practice projection against the cutoffs.

**17. You is thin when things load, and mostly error boxes when they do not.** **[other owner]**
Evidence: `hub_failed_night.png` shows "This week did not load" and "Your milestones did not load" stacked. Full hub: sheet, milestones, three progress rows, five settings rows, tools. There is no plan, credits, study days or notification status at a glance. Proposal in section 3.

**18. "Ask Mobi" and "Ask your record" are the same feature with two names.**
Evidence: the Start sheet row says "Ask your record" (`quick_start_deck_night.png`; `lib/features/practice/widgets/quick_start_deck.dart`). Review's pill and the Ask page say "Ask Mobi" (`insights/copy.dart:129`, `review/copy.dart:14`).
Fix: "Ask Mobi" everywhere, with "About your marks" as the subtitle, and the same on the website.

**19. Jargon and internal metaphors in on-screen copy.**
Evidence and fixes:
- "Your sheet, CUET UG 2027" and "Finish your sheet" (you/copy.dart:12-18): use "Your plan" or "Your CUET plan".
- "Rhythm" and "Weekly goal and rhythm": "Study days" and "Weekly goal".
- "Open results directly: Skips the sealed sheet" (you/copy.dart:109): "Show results straight away".
- The week legend "Counted, Planned, Rest": "Studied, Planned, Day off".
- "Milestones, 3 of 9 landed": "3 of 9 earned".
- Compass: "Combination I", "Any one Language from List A", "Round I/II/III", "CSAS 2026", "programme-specific CUET score" become "Option 1", a plain sentence naming the student's own subjects, "Round 1", "DU admissions 2026" and "Target score".
- Combo: "Papers on your form": "Subjects you will write".
- NTA tile note "palette, Mark for Review": "Looks and times like the real exam screen".

**20. The live capsule covers hero text at 360 dp with 1.3x text.**
Evidence: `today_ready_text130_short_night.png`. The "Accountancy repair, Start" capsule sits on top of the hero's "11 Oct." line.
Fix: show the capsule only once the whole hero card has scrolled out, not just its key (`today_body.dart:322`), or add the capsule's height to the hero's bottom padding while it shows.

**21. The Full mock and NTA mode starts have no moment of their own.**
Evidence: `lib/features/practice/practice_start_screen.dart` runs one shared stage flow for every mode. The owner asked for "the clock doing a 360".
Fix: on Start of a Full mock, the stopwatch glyph's hand sweeps 360 and the crown clicks (one haptic), then the runner fades in. For NTA mode, the palette fills cell by cell into the exam header. Use shared tokens from `lib/core/motion/**`; reduced motion gets a still frame. The NTA pre-paper screen is **[other owner]**.

**22. The bar's blur reads weak.**
Evidence: `lib/core/widgets/bar/bar_glass.dart:15,34` (20 sigma) under a 72% Night and 80% Day tint; sheets 14 sigma (`lib/core/theme/tokens.dart:84-86`). The thick tint hides most of the blur. Phones that drop to auto-lite get none (`lib/core/theme/glass_quality.dart:82-84`).
Fix: tint to about 60% Night and 68% Day, sigma 24, keep the 1.15 saturation. Raise `sigmaSheet` to 18. Re-check `glass_*` goldens in both themes.

**23. The Combo planner is three tasks on one long page.**
Evidence: `combo_full_night.png`. It asks where you want to go, then which subjects you could take, then how many papers, then shows combinations, and leaves a large empty tail. "Do not drop: English, Mathematics" names Mathematics, which the student never listed, with no reason given.
Fix: steps 1-2-3 with a small sticky progress header and the result card first once set. Explain the must-keep line: "Mathematics opens B.Com (Hons) Option 1 at 41 more programmes."

**24. Today's week strip pops in late.**
Evidence: table row 6. The You hub has `week_skeleton.dart`; Today has no placeholder.
Fix: reserve the strip's height with a skeleton while `rhythmSnapshotProvider` is loading, so Today does not jump and the student does not see "a new section".

**25. No large-text or 360 dp goldens for Compass, Combo, the tools hub or You.**
Evidence: `test/golden/tools/goldens` and `test/golden/you/goldens` have no `text130` files. Today, Review and Insights do. The Compass search field and "Most colleges" sort pill share one row and will truncate at 1.3x.
Fix: add `text130` 360 dp goldens for `compass_full`, `programme_bcom`, `combo_full`, `hub` and You `hub_full_page`; stack the sort pill under search below 380 dp at large text.

## 2a. Further findings (lower impact)

- **Stale goldens.** 13 golden folders hold `failures/` images (onboarding welcome, core state_error/offline, notifications settings_error, tools compass_error/offline, rhythm, learn, runner motion_next_mid, review tab and repair ending, result replay). The masters no longer match the code, so reviewers are looking at old pictures.
- **The You hub golden is not the production You.** `hub_full_page_*` renders the fallback `ToolsPanel` (external-link rows) because `YouHubScreen.tools` is null in the test. Production passes `ToolsShelf` (`lib/features/you/you_routes.dart:28`). **[other owner]**
- **Help has no answers.** It has no FAQ on credits, NTA mode, what counts as a study day, or what to do when Google sign-in fails (`lib/features/you/copy.dart:235-255`). **[other owner]**
- **Account layout.** The "Not now" text key under "Set a password" floats inside the list (`account_free_night.png`). The "40 practice credits" title is set in a grey display face, so it outweighs the plan pill. **[other owner]**
- **Review empty state.** "Your mistakes gather here" with a Start practice key is fine. The owner's line "we could include your mistakes" may mean showing a sample repair, or mistakes from website papers. Check with him. **[other owner]**
- **Name of the first tab.** It is "Today", the owner calls it "Home", and the website calls it "Dashboard". Keep "Today", but use it everywhere (notifications, widgets).
- **Quick 10 versus Quick practice.** The Start sheet says "Quick 10" and the Practice tab says "Quick practice". The website uses both. Pick one, "Quick practice, 10 questions".

## 3. What Profile (today's You) should contain

Open it from an avatar at the top right of every tab root (finding 11). Order follows how often a student needs each part:

1. **Profile header.** Initials avatar, name, email, course and target year (CUET UG 2027), and an Edit key. Tapping the name, course or subjects edits them in place.
2. **Plan and credits.** Plan (Free or Pro, "until 12 Jan"). Two balances: "Practice credits 40, for mocks and practice" and "AI credits 18, for Ask Mobi and repair explanations, renew on 1 Nov". "See history" opens the ledger list: date, what, credits, balance after. No price and no purchase (binding rule 13); a Pro student sees what Pro includes.
3. **Appearance.** An inline three-way toggle (Night, Day, Match phone), then glass, touch feedback and celebrations behind "More".
4. **Notifications.** On or off with the reminder time shown on the row; quiet hours; a link to the phone's settings when blocked.
5. **Study days.** The weekly goal (3, 4 or 5 days), planned weekday chips inline, pause until a date. This replaces "Rhythm".
6. **My subjects and My colleges.** The one shared college list (finding 6), editable here, on Today and in Compass.
7. **Progress.** Milestones shelf, personal bests, repair record: what the old hub's "Progress" held, now one tap down.
8. **Account and sign-in.** Sign-in methods (Google, email code, password, phone), sign out of other devices, sign out, delete account.
9. **Privacy.** Usage data on or off.
10. **Help.** An FAQ (credits, NTA mode, study days, sign-in trouble), "Write to us", policies, version.

## 4. The bottom bar: five slots, each earning its place

Width check: five slots of 72 dp fit a 360 dp phone with the thumb reaching every one.

| Slot | Contents | Why it is on the bar |
|---|---|---|
| Today | Tonight's move, the week, the road (with a board picker), your colleges ladder | Opened daily. It answers "what do I do with the time I have". |
| Practice | Subjects, quick practice, by chapter, Smart practice, Full mock, NTA mode, concepts | The main way to make marks; the owner likes it as it is. |
| Start (centre action) | The quick start sheet | One tap to begin from anywhere. It is an action, not a page. |
| Review | Mistakes, repair, Mistake Lab, Ask Mobi, saved questions, record | Where marks are won back after every paper. |
| Colleges (new; replaces You) | My colleges, Admission Compass, Combo planner, CUET 2027 guide, practice projection against cutoffs | Commerce students choose MockMob for admission outcomes. This turns the hidden tools into a destination the owner asked to be "integrated properly". |

You becomes the avatar page in section 3, which matches the usual app pattern the owner described. A sixth slot is not recommended: at 360 dp six slots drop under 60 dp each and Start's centre position is lost.

## 5. App and website names

| Thing | App now | Website now | Use |
|---|---|---|---|
| Ask about your record | "Ask Mobi" (Review, Ask page); "Ask your record" (Start sheet) | "Ask your record" (1 place) | Ask Mobi |
| Compass | "Admission Compass" (tools), "Compass" (You fallback rows) | Admission Compass | Admission Compass |
| Combo | "Combo planner" (tools hub), "Combo Planner" (You copy) | Combo Planner, "subject combination planner" | Combo planner |
| Colleges list | "Your colleges" (Today, 3), "Your DU shortlist" (Compass Pro, 8), "Colleges" (You) | n/a | My colleges |
| Credits | practice credits, AI credit, explanation credits, credits | "Practice credits (Quick Practice and Full Mock)", PrepOS wallet | Practice credits; AI credits |
| Theme | Night, Daylight, Match phone | n/a | Night (dark), Day (light), Match phone |
| Quick mode | Quick 10, Quick practice | both | Quick practice, 10 questions |
| Repair | Repair the next mistake, Mistake Lab, repair record | Mistake Lab, Mistake repair | Mistake Lab (the place), repair (the act) |

## 6. Owner steps found by this audit

1. Supabase > Authentication > URL Configuration > Redirect URLs: add `in.mockmob.app://login-callback` (fixes Google, finding 1).
2. Google Cloud: the Web client ID into `dart_defines/prod.json` `GOOGLE_WEB_CLIENT_ID`, and Android OAuth clients for the release and upload keys (AUTH.md G1-G3), for one-tap sign-in.
3. Keep Vercel's checkpoint and bot challenge off for `/api/*` from the app, or add a bypass rule for the app's user agent and bearer-authenticated requests. The app cannot get past a browser challenge.

## 7. Server routes checked

Every path the app calls exists in production main, except `POST /api/ai/mentor/report`. The "Report this reply" key is behind a flag that is off (`lib/features/insights/data/ai_reply_report.dart:12-14`), so it is not a dead tap today. Runtime errors in the last 24 hours: one cluster, `/api/auth/email-login` PGRST202 at 03:30 UTC. The RPC `auth_clear_unconfirmed_password` exists now, so that cluster is from before the migration.
