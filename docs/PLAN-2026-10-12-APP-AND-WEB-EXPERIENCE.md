# MockMob Android app + website experience plan

Status: **PROPOSED, 12 October 2026.** Prepared by Claude at the owner's request ("inspect everything and
make a plan which we can work upon"). The owner answered four direction questions the same day (§9: Flutter
app, no in-app purchase in v1, homepage restructured around the loop, personal Play account). Nothing is
implemented yet. Each phase starts when the owner authorizes it. Where this plan and a newer owner decision
conflict, the owner decision wins.

Inputs read for this plan (all of them, line by line where they are research):

- `docs/brain/PRODUCT-EXPERIENCE-RESEARCH-2026-10-12.md`: §§1–16, Appendix A (the 19-section product
  brain and the 201-line emotional-design/gamification transcript), Appendix B (the 164-line dashboard +
  Undertone transcript), Appendix C (owner notes). The PDF `MarkMob_Product_Research_and_UX_Specification`
  was checked page by page against the product brain. It adds the six reference screens on pages 15–20
  (mobile home, result→repair, card anatomy, "Why this?", honest card states, evidence-before-wording).
  The other pages only differ in typesetting.
- `PRODUCT.md`, `DESIGN.md`, `AGENTS.md`, `docs/brain/SPEC.md`, `PLAN-2026-10-04-NEXT-DAYS.md`, STATUS
  (newest entries), the AI OS decision log (12 Oct: **₹99 a month**; a staging project exists).
- The live homepage at phone width (12 Oct), the `mobile/` Capacitor scaffold, and the website's routes, auth
  and APIs (agent inventories).

---

## 1. Honest baseline (12 Oct 2026)

| Area | Where it actually is |
| --- | --- |
| Website | Live on Vercel (`origin/main` 4476a5a, deployed 7 Oct). Night Arena landing with a 9-chapter feature tour, no-signup 5-question sample, Arena app shell (Today, Practice, Learn, Review + More), result page with Score Recovery Lab (Find → Repair → Prove), AI Mistake Repair, Learn + FSRS recall, PrepOS, DU Compass, Combo Planner, NTA-style console, PWA with an offline fallback page only. Light theme is the default since 5 Oct. |
| Android app | `mobile/`: a 101-line React/Vite/Capacitor 8 spike (5 tabs, 5-question quick session, email OTP, secure storage, one local reminder). **Never built or run on a device**; built `dist` has no env so it shows "beta is being prepared"; default Capacitor splash/legacy icons; no deep links, no Google sign-in, no signing. Roughly 10–15% of a store app. The server side it uses (`/api/mobile/*`, bearer-token `auth()`, `mobileCors.js`) is real and reusable. |
| Shared contract | `shared/recoveryContract.js` (launch subjects, API wrapper) and `shared/tokens.css` (5 variables) are used by both. Scoring and sessions are server-authoritative (`/api/sessions`). **But the beta app starts sessions without `experience:'practice'` and submits without `sessionTicket`, so it hits the strict recovery path (evidence-certified content, currently empty). The web runner (`test/TestPageClient.jsx`) uses the practice protocol.** Inferred from code, not tested. |
| API reach for a native client | `auth(request)` accepts `Authorization: Bearer` on sessions, attempts, practice quote, recovery, learning plan, study, PrepOS chat/insights, compass pro and analytics. **Cookie-only** (unusable from an app until changed): bookmarks, all `/api/questions/*`, `ai/credits*`, `ai/mentor/{history,local,session/new}`, `ai/rival/*`, `ai/usage`, `ai/context`, `learning/summary`, `users/[id]`, `billing/cancel`, and every payment route. |
| Website code health | Three CSS dialects (`.mm` marketing, `.app-shell` Arena, legacy dark Tailwind utilities in 19 files), about 11,000 lines of CSS, three icon systems, and many orphaned components. `test/TestPageClient.jsx` is 1,508 lines, about 640 of them inline CSS. Security items to fix during the overhaul: <ul><li>vestigial next-auth routes with a "Demo Login" credentials provider;</li><li>`GET /api/questions/pending` has no auth;</li><li>the billing webhook secret is compared with `!==`;</li><li>no security headers;</li><li>`middleware.js` guards only four route groups.</li></ul> |
| Core loop truth | "Repair that holds" (fresh delayed checks) is **not live**: `RELEASE_GATES.content=false`, no v7 content released, recovery pathway `blocked_content`. What is live: result Lab, single-answer Mistake Repair, chapter practice labelled "not proof". **Fresh-question supply is the hard dependency for every "Prove/fresh check" feature in this plan.** |
| Measurement | No analytics of any kind (no SDK, no event table). No push notifications. No weekly goals. |
| Pricing | Owner (12 Oct): **₹99 a month**. Live site still sells and says "₹99 once, through 31 July 2027 · No auto-renewal" because `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is not confirmed set. `PRODUCT.md` carries both. |
| Repo | Local `main` is 30 commits behind `origin/main` with ~850 uncommitted/untracked entries (mostly data/logs/docs). Any build work must start from a clean worktree off `origin/main`; the dirty tree is preserved, not reset. |

Homepage observation (phone, 12 Oct): one long page carrying hero + sample + stats + a 9-tool autoplay
tour + Mistake Lab + interactive DU cutoffs + subject eligibility + Combo Planner + campus cards + NTA
skin switcher + bank counters + Instagram creators + pricing + FAQ. Everything is honest and labelled, but
the page reads as a catalogue. The research's central point is that it should read as one loop.

---

## 2. What we are building: one product, two surfaces

**Promise (owner-approved line):** *Find the marks you're losing. Repair the mistake. Prove it on fresh
questions.* The emotional job, from the research: replace an intimidating score or a feature catalogue with
**calm agency**: "I can see what happened, I know the next step, and my work is safe."

**The loop both surfaces serve:**
Discover → try 5 questions → save → mock/practice → result → one supported pattern → repair → fresh
check (when content allows) → come back later → finish the chosen work.

### 2.1 Division of roles

| | Website (mockmob.in) | Android app | Shared (one source of truth) |
| --- | --- | --- | --- |
| Main job | Discovery, SEO, persuasion, the no-signup sample, checkout, desktop mocks, DU research tools | The daily study companion: tonight's next move, short repairs, mocks in focus mode, reminders tied to real tasks, offline review on patchy 4G | Account, entitlements, sessions and scoring, next-move plan, repair/check records, evidence states, copy vocabulary, design tokens, event contract |
| Owns | Landing, subject hubs, pricing/Razorpay, Compass/Combo Planner, account billing | Widget, push, notification-driven returns, offline packs, haptics, shortcuts, native share | `/api/*` services, `shared/` package, Supabase |
| Must never | Diverge from app copy/states | Compute its own score, progress or plan; sell Pro before Play policy is settled | Have two versions of the truth |

### 2.2 The rules we build by (research distilled into MockMob decisions)

1. **One dominant useful action per screen**, with agency: shorten, choose another, decline, "Why this?".
   (Research §2.5, §4.3, §9; figs 15–17.)
2. **Value before commitment.** The 5-question sample is onboarding on web *and* app; the result and the
   shape of the next move are shown before signup; guest answers carry into the new account. (§2.2, §4.2.)
3. **Truthful states are features.** Every data surface ships its states: cold start, thin evidence, ready,
   in progress, check due, stale, unavailable, no content, entitlement-blocked, error. Saving shows *local
   pending → sent → server accepted*. Never show success before acknowledgment. (§5.6, §9.6, fig 19.)
4. **Data drives form.** Denominators always ("6 of 15 answered"), unanswered ≠ wrong, tabular numerals,
   timelines for chronological records, colour only for an actionable state, no fake precision. (§4.)
5. **Emotional fit over celebration.** A poor result leads with "Here's the first thing to work on", never
   a red wall; celebration is proportional; no confetti after distress; Mobi is contextual and **never in
   timed answering**. (§2.2, §6.1–6.3 of the brain.)
6. **Design the natural-return moment.** Opening the result after a mock is MockMob's Undertone moment.
   Hold the thread while it processes, notify when ready, make it worth opening, let the student reveal it
   optionally, pay off on two channels proportionally, frame what was recorded, and put the next useful ask
   inside the ending. (§6, §9.)
7. **Bounded goals, not punishment.** A chosen, editable weekly goal with rest days; the ring's denominator
   is real work (repair cycles), never XP; nothing earned is lost for a missed day. No variable-ratio or paid
   random rewards; predictable access to learning. (§8.)
8. **Competence feedback over points.** Show comparable fresh performance ("7 of 10 fresh, earlier 4 of
   10") and keep practised / fresh check completed / retained distinct. (§8.6, §13 of the brain.)
9. **Deterministic first, AI for expression.** Next moves come from versioned rules over real history; AI may
   rephrase validated facts only; the deterministic card survives AI failure or budget exhaustion. (§11–12.)
10. **Craft is trust on a budget Android.** 44px targets, 16px inputs, reduced-motion parity, opacity/
    transform-only motion, no heavy blur, measured LCP/INP/CLS. (§5.7, §14.4.)
11. **Owner standing preferences stay binding:** category-standard structure at full craft; volt `#D2F000`
    as action fill; Gabarito / Hanken Grotesk / Geist Mono roles; NTA skin exceptions; no testimonials or
    headcounts; illustrative screens labelled; market every feature and do not delete features just to
    shorten a page; demos autoplay with a visible pause; change only what a task names.
12. **Measure learning, not taps.** North Star = weekly students completing a valid learning cycle
    (observed need → repair → eligible fresh check). Taps, opens and XP are not success. (§15 of the brain.)

---

## 3. The Android app: more than the website

### 3.1 Stack decision (owner input, 12 Oct)

The owner said to ignore the old Capacitor app. React Native is acceptable if it makes syncing with website
accounts easier. The owner knows Flutter and values its feel: animation quality, and haptics on bottom-nav
switches.

**Decision proposed: Flutter (Android only), a new project at `app/` (or a sibling repo, decided in
Phase 0).** The 101-line Capacitor client is retired. Its server work (bearer `auth()`,
`/api/mobile/*`) is reused.

Why Flutter rather than React Native, now:
- **Account sync is identical either way.** Both clients talk to the same Supabase auth and the same
  `/api/*` server. The Flutter side uses `supabase_flutter`, with native Google sign-in exchanged through
  Supabase ID-token sign-in. So account sync is not a reason to pick React Native.
- **The owner's quality bar is the feel, and Flutter draws every pixel itself.** That gives consistent
  animation and press feedback even on budget Android. Haptics (`HapticFeedback.selectionClick` on tab
  change), custom bottom navigation, Rive/Lottie and implicit animations are first-class.
- **The toolchain and the publishing path are already proven on this machine.** The Flutter SDK is at
  `C:\flutter` (an upgrade is available). The Android SDK, NDK and emulator are in `%LOCALAPPDATA%\Android\Sdk`.
  CampusOS already produced a signed AAB that was uploaded to Play. The owner can run and judge builds
  directly.
- The package ecosystem covers every signature experience:
  - `firebase_messaging` (push), `home_widget` (widget), `app_links`, `flutter_secure_storage`;
  - `drift`/`sqflite` (offline), `wakelock_plus`, `in_app_update`, `in_app_review`, `share_plus`;
  - the Dart `fsrs` port for offline recall.
  
  Confirm current versions through Context7 or pub.dev at setup.

What React Native would have offered, and how the plan compensates:
- **Same-language sharing with the website.** To compensate, `shared/` becomes language-neutral:
  - `tokens.json` generates both the web CSS variables and a Dart theme;
  - JSON Schema for API payloads and state enums generates both TS/JS and Dart models;
  - `copy.json` holds the student vocabulary.
  
  Server contract tests keep both clients honest.
- **Over-the-air JS updates.** Flutter ships through Play releases. Code push for Flutter (for example
  Shorebird) is optional and not in v1.

For the record:
- React Native can also do premium feel (Reanimated, haptics on tab press), and large polished apps ship on
  it (Shopify, Coinbase, Discord).
- Publishing works the same way in both: a signed `.aab` uploaded to the Play Console.
- The choice here rests on the owner's priority (feel) and proven familiarity, not on capability.
- TWA (the website inside Chrome) was rejected because it is the website.

### 3.2 App information architecture

Bottom tabs, labelled, with names identical to the web Arena so students never relearn the product:
**Today · Practice · Review · Learn · You.** The research's *Practice / Improve / My Goal* is run later as an
experiment on both surfaces (§8, Phase 6), not adopted on name appeal. You = weekly goal, progress, DU goal
(links to web tools), account, Pro status, notifications, data and deletion.

### 3.3 Signature experiences (what the website cannot do as well)

Each one is tied to a real student job, a research mechanism and an honesty boundary.

| # | Experience | Student job | Research mechanism | Boundary |
| --- | --- | --- | --- | --- |
| A1 | **Tonight** (Today): one next-move card with a 10/20/30-min chooser and a "Why this?" sheet showing real counts and source mocks; resume and due-check slots above it when valid | "What do I do with the 20 minutes I have?" | Next best move contract, 12 states (brain §9; figs 15, 17–19) | Comes from `/api/learning/plan`; never a fabricated history; cold start = labelled diagnostic |
| A2 | **Result recap moment**: submission is held in an ongoing notification ("Submitted · saved on server · result ready", real stages only). A push arrives when ready. The recap card is worth opening, with an optional first-time reveal that can be skipped and turned off. Haptic and visual payoff are proportional to the outcome. It is framed as "Mock 7 added to your record · 3 mistakes ready to repair". It ends with the next ask: "Start 10-min repair / Remind me for a fresh check / Finish for now" | "How did I do, and what now?" | Undertone's 7 interventions (§6.6), peak-end as a lens (§6.7) | Direct result access always; no reveal ritual forced on repeat; no confetti after a poor mock; no simulated percentages |
| A3 | **Repair record**: a personal, growing record of mistakes found → repaired → checked (the "vinyl sleeve" equivalent: an observation becomes work, then evidence) | "Is my work adding up?" | Distinctive ending from the product itself (§6.8); competence feedback (§8.6) | Status words only: practised / fresh check completed / retained on later check; never "mastered" or recovered marks |
| A4 | **Reminders tied to real tasks**: result-ready, fresh-check-due, chosen study window, weekly plan; asked for only after the first result; quiet hours; cancelled when the task is done, invalid or dismissed | "Remind me when it actually matters" | Reminders contract (brain §7.3), external cadence (§6.3) | Inexact scheduling (no `SCHEDULE_EXACT_ALARM`); refusing never blocks study; no guilt copy |
| A5 | **Home-screen widget**: next move + weekly cycles ring + days to CUET; tap opens straight into the task | "Keep my plan in sight without opening anything" | Hold the thread / presence without opening (§6.5) | Shows last server-confirmed state with its time; no invented urgency |
| A6 | **Focus mode for mocks/NTA**: immersive, keep-awake, back-button guard, interruption-safe resume, server-anchored timer, explicit saved/syncing state per answer | "Rehearse the real exam on my phone without losing answers" | Mock flow (brain §4.4); trust through details | Correctness hidden during exam-equivalent mocks; Mobi absent; no offline scored attempts unless reconciliation is proven |
| A7 | **Offline study packs**: Learn cards (FSRS reviews offline, synced later), saved mistakes and their explanations, downloaded for the bus or a weak signal | "Study on patchy 4G" | Device floor; the app-launch logic (brain §8.2) | Downloaded review is not a scored attempt; offline is advertised only after it is proven on a device |
| A8 | **Weekly goal**: the student picks, for example, 3 repair cycles (with a smaller option), with rest days and a friendly restart; the ring fills only with real cycles | "A finish line I can actually reach this week" | Completion drive with a real denominator (§8.6); streak trap (§8.4) | Nothing earned is lost; partial stages are labelled partial; the week is in the student's timezone |
| A9 | **Native touches**: haptic vocabulary (select, saved, finished); app shortcuts (Resume, 10-min repair, Fresh check); App Links; a private-by-default share card for a finished repair or week, with a preview | "It feels made for my phone" | Emotional design (visceral/behavioural layers) | Respect system haptics; share never exposes marks or weak areas by default |
| A10 | **Mobi, native**: small, cheap reactions at defined moments (first repair, saved, check passed), static under reduced motion | "Someone in my corner, but not in my way" | Duolingo character feedback (§7.1), Mobi contract | Never in timed answering; never claims feelings or unseen history |

### 3.4 First run (the Undertone fix applied: the core idea is tried inside onboarding)

1. Welcome (one line of the promise) → pick subjects (with the reason given: "to serve the right questions").
2. Five sample questions (labelled "sample, not a diagnosis").
3. A sample result with explanations, and *what your next move would look like* for real history.
4. Create the account to keep this (Google or email code). The sample answers carry over.
5. Offer to turn on reminders, explaining exactly what they send. Saying no is fine.
6. Land on Today with a real next move or a labelled diagnostic.

### 3.5 Non-functional bar (app)

- Budget Android, patchy 4G. Measure cold start and first useful screen on one real low-end device (owner
  supplies one). Keep animations cheap: avoid stacked blur, opacity and `saveLayer` effects. Check UI and
  raster frame times in Flutter DevTools on that device in profile mode. The app bundle gets a size budget.
- Session reliability: delta sync of answers with server ACKs, safe final-answer flush at the deadline,
  idempotent start/submit (this also fixes the web, see §7).
- Accessibility: TalkBack names, 200% font scale, focus order, colour never the only signal.
- Security: tokens in Keystore-backed storage; no service keys in the client; deep links validated.
- Crash/ANR visibility: Play Console vitals at minimum (optional crash SDK is an owner decision).

---

## 4. Interlinking the website and the app

1. **One identity.** The same Supabase account. The app signs in with email OTP (existing) and native Google
   sign-in (Credential Manager → Supabase ID-token sign-in), which matches the website's Google login. A
   student never has two accounts.
2. **One record.** Sessions, scoring, next move, repair records and entitlements live only on the server.
   The app reads `/api/mobile/me` for Pro status. Something bought on the web works in the app.
3. **Links that open the right surface.** `https://www.mockmob.in/.well-known/assetlinks.json` plus
   `autoVerify` App Links for `/today`, `/result/*`, `/review`, `/dashboard` (Practice), `/learn/*`. They
   open the app when installed and stay on the web otherwise. Production serves www; the apex redirects
   (307). Verification is not expected to follow redirects, so declare only the www host, or serve the file
   on the apex without a redirect. Verify this on a device. Pages the app doesn't own (Compass, Combo Planner) open
   in a Custom Tab. A short-lived, server-exchanged handoff code keeps the student signed in. The handoff
   needs a security review before shipping. In v1 the app does not link to pricing or checkout, because
   of the Play Payments policy.
4. **Cross-device continuity.** A desktop result page shows "Continue on your phone" (a QR into that exact
   result or repair). Practice and repair sessions resume on either device, with "which session is active"
   made explicit. Timed-mock handoff follows the integrity rules.
5. **One notification brain.** The same server events (result ready, check due, weekly plan) drive app push,
   an in-app inbox, and optional email. Cancellation rules are shared.
6. **One language-neutral contract.** `shared/` becomes the source both clients generate from:
   - `tokens.json` generates web CSS variables and a Dart `ThemeExtension`;
   - JSON Schema for session, next-move, repair-record and entitlement payloads and state enums generates
     JS (web) and Dart (app) models;
   - `copy.json` holds the student vocabulary (mock, repair, fresh check, progress, goal) and the
     state-matrix copy.
   
   Server-side contract tests validate real responses against the schemas, so neither client can drift.
7. **One event contract** (if approved, §9). The same event names on both surfaces, with `platform` as a
   property.

---

## 5. Promoting the app (website and beyond)

- **`/app` page** (SEO: "MockMob app", "CUET mock test app"):
  - what the app adds (Tonight, reminders tied to real tasks, widget, offline review, focus mode);
  - real screenshots, labelled where illustrative;
  - Play badge, a QR code for desktop, and privacy notes.
- **Contextual prompts at value moments, not on arrival:**
  - after the sample result ("Get your next step on your phone");
  - after a mock result;
  - on Today.
  
  Show them only on Android browsers. Remember dismissals. Never use a full-screen interstitial (it is also
  a mobile-SEO penalty). Desktop shows the QR. iPhone shows nothing pushy, because the web is their app.
- **Persistent but quiet entries:** nav/footer "Get the app", Account → "Connect your phone", the mobile
  dock variant on Android.
- **PWA coordination:** add `related_applications` to `src/app/manifest.js`. Chrome on Android then offers
  the Play app instead of a second install. Keep the PWA for iPhone and desktop.
- **Play listing:**
  - name, short description, and screenshots from the real app;
  - feature graphic;
  - Data safety form, content rating, target audience (students under 18 are likely, so the minors rules
    apply);
  - privacy policy URL and an account-deletion URL.
- **Launch distribution:**
  - existing creator partners: the dated reel strip already exists, and paid partnerships stay marked;
  - an email to existing accounts;
  - a "repair card" share (private by default);
  - referral codes stay as they are (tracked; they never change the price).
- **Growth is measured by activated students and completed cycles**, not by installs (brain §8.3).

---

## 6. Website UI upgrade

Scope rule: restructure and re-craft, keep every feature reachable and marketed (owner preference). Start
with the screens on the core loop, then the legacy screens.

1. **Landing: from catalogue to loop.** The existing modules stay, reordered and grouped as below. The
   target is a shorter scroll on phones (Preparoo is the owner's mobile reference: one feature carousel,
   product mocks, sticky CTA).

   | Order | Section | Notes |
   | --- | --- | --- |
   | 1 | Hero + "Try 5 questions" | Outcome-led; keep the kinetic headline moment |
   | 2 | The sample | Ends in a sample result + "your next move would look like this" + save-to-account (guest merge) |
   | 3 | The loop: Find → Repair → Prove | The Mistake Lab, as the mechanism section |
   | 4 | Feature tour, grouped by job | Practise (Practice, NTA) · Fix (Mistake Repair, Replay, Radar) · Plan (PrepOS, Compass, Combo, Benchmarks) · Learn; still autoplay with a visible pause |
   | 5 | One "Plan your DU shortlist" section | Merges today's two large interactive DU blocks into one tabbed block |
   | 6 | App band | New |
   | 7 | Truthful counters | |
   | 8 | Creators | |
   | 9 | Pricing | From `publicOffer()`: ₹99/month once the plan is live |
   | 10 | FAQ, footer | |
2. **Today (web Arena home).** Keep the existing `LearningNextAction` card as the one dominant action,
   brought to the 12-state contract with "Why this?". Resume and check-due slots go above it. The weekly goal
   sits below. The tool catalogue moves under "More tools".
3. **Result page ending.** Keep the 4 Oct structure. Add the honest grading/correction states, the
   proportional ending, the next ask inside the ending, and "Continue on your phone".
4. **One design system.**
   - Collapse DESIGN.md's three layers (daylight paper, Night Arena, Arena) into one current spec.
   - Generate tokens from the shared JSON.
   - Retire the third dialect: move the screens still on legacy classes and dark Tailwind utilities
     (`/features`, Chart.js Radar, Moderation, Upload, parts of Saved/Explore, `pricing/prepos`) to Arena
     components.
   - Keep one icon system (the lucide `Glyph` wrappers).
   - Delete orphaned components once they are confirmed unused.
   - Split `TestPageClient.jsx` (runner logic, palette, skins, CSS) without changing its behaviour.
   - Give marketing pages a shared layout. The legal pages repeat theirs three times.
   - Write the full state contract (button, input, save, recommendation, repair, submission, payment) as
     reusable components.
5. **Data presentation pass.** Denominators, tabular numerals, unanswered vs wrong, timelines for
   attempt/repair history, a table equivalent for every chart.
6. **Truth fixes:**
   - Price copy everywhere follows `publicOffer()` once the monthly plan ID is set. `PRODUCT.md` and
     `STATUS.md` are updated to ₹99/month.
   - Fix the stale DESIGN.md frontmatter. Use the Mobi name in `MOTION.md`.
7. **Performance and accessibility proof:**
   - a real budget Android test and a TalkBack pass;
   - a 200% zoom check;
   - field Web Vitals, if the owner approves a minimal first-party measurement (§9).
8. **Small truthful fixes found in the inventory:**
   - The PWA manifest `theme_color` (dark) disagrees with the light viewport colour. Add a maskable icon.
   - Register the service worker beyond `/today`, or state that offline is Today-only.
   - Leaderboard synthetic "practice rival" rows: keep them clearly labelled, or move them to a separate
     benchmark view.
   - `/rival` is unreachable from the nav. Decide whether it stays.
   - The in-app guide never auto-starts. Decide whether it should, once, after signup.

---

## 7. Shared backend work (both surfaces depend on it)

| Item | Why | Notes |
| --- | --- | --- |
| Next-move contract | Today card, widget, push and app all show the same next move | Extend `/api/learning/plan` to the 12 states + evidence payload ("Why this?"); deterministic; AI phrasing optional with fallback. No parallel `/v1/next-move` routes |
| App on the practice protocol | The beta starts sessions on the strict recovery path, which fails without certified content | The app uses the same `experience:'practice'` + `sessionTicket` protocol as the web runner; one documented session contract in `shared/` |
| Bearer auth on cookie-only routes | The app needs bookmarks, questions/explore, PrepOS history, credits/wallet read, learning summary, profile update, billing status | Switch those handlers to `auth(request)`; payment create/verify stay web-only |
| Trust & security hygiene | Both surfaces sit on the same API | Remove the vestigial next-auth Demo/Credentials providers; add auth to `/api/questions/pending`; timing-safe webhook secret compare; security headers; review `middleware.js` coverage against Next 16's `proxy` convention (read `node_modules/next/dist/docs/` first) |
| Session reliability | The app makes interrupted sessions common | Replace the 1.5 s full event-log re-upload with delta + ACK; make the final flush safe at the deadline; make start/submit idempotent (Cloudflare audit findings) |
| Push infrastructure | Result-ready, check-due, weekly plan | FCM project; `device_tokens` and `notification_prefs` tables; scheduler (Supabase cron or Vercel cron); send + cancel rules; per-user frequency cap; quiet hours |
| Native Google sign-in | Same account as web | Supabase ID-token sign-in from Credential Manager |
| App Links + handoff | Interlinking | `assetlinks.json` (needs the release signing fingerprint), route map, and a short-lived handoff-code exchange (with security review) |
| Guest merge | Value before commitment | Sample answers become the new account's record exactly once (idempotent) |
| Account deletion | Play requirement; DPDP | In-app and web deletion with clear effects on records |
| Event contract | North Star and experiments | Minimal first-party events table, no third-party SDK, consent-aware; **owner + DPDP decision first** |
| Entitlements for app | Pro bought on web works in app | Already exposed via `/api/mobile/me`; Play Billing only after the policy decision |
| Fresh-content supply | Every "Prove/fresh check" promise | Owned by the generator programme; the app and web label practice as practice until `RELEASE_GATES.content` opens |

---

## 8. Phased roadmap (ordered by dependency, not dated)

No dates are promised before Phase 0 measures the real work. Each phase ends only on its exit evidence.

| Phase | Work | Exit evidence |
| --- | --- | --- |
| **0. Foundations & decisions** | Owner answers §9. Clean worktree from `origin/main`. Plan for reconciling the dirty tree (nothing reset). Flutter toolchain check (`flutter doctor`; upgrade the SDK at `C:\flutter`; Android Studio JBR as the JDK; the existing SDK/NDK/emulator) and one real budget phone. Create the Flutter project and its package id. Map the current web journey on a phone in both themes: sample → signup → Today → practice → result → repair → prove, including failure states (research §13 step 1). Shared token JSON + contract skeleton. Pricing/doc truth fixes. | Journey map with screenshots and found defects; toolchain builds a debug app; decisions recorded in the decision log |
| **1. Shared backend** | Documented session contract (practice protocol) in `shared/`; bearer auth on the cookie-only routes the app needs; trust/security hygiene (§7); next-move states + evidence; session delta sync and deadline safety; push infrastructure; Google ID-token sign-in; App Links file; guest merge; account deletion; event table (if approved) | Existing suites pass (`test:recovery`, payments, NTA, answer-integrity, learning) plus new contract tests for states, idempotency, ownership and cancellation |
| **2. Website experience pass** (parallel with Phase 3 once Phase 1 contracts exist) | Landing restructure + app band; Today; result ending; state components; legacy-screen migration; data presentation; truth fixes | Rendered walkthrough at 360px and desktop in both themes; reduced motion; long labels; LCP/INP/CLS measured; owner review in the real UI |
| **3. App MVP** (Play internal testing, then closed testing as early as it is stable so the 14-day clock runs in parallel with Phase 4) | Flutter app: theme from `tokens.json`; custom bottom nav with haptics; first-run (§3.4); auth (OTP + Google); Today (A1); Practice + focus mode (A6); result recap (A2); Review + Mistake Repair; Learn; You (account, Pro status, settings, deletion); push for result-ready/check-due (A4); App Links | Signed internal build on the owner's real budget phone; the research §12 scenarios that apply (background, kill, network loss, notification refusal, account switch, long text, TalkBack) |
| **4. App differentiators** | Widget (A5), ongoing submission notification, weekly goal (A8), repair record (A3), offline packs (A7), shortcuts/share/haptics (A9), Mobi native (A10), in-app update; review prompt only after a good moment | Each one checked on a device, with the cancellation and failure paths exercised; offline claims proven before they are advertised |
| **5. Interlink & launch** | `/app` page, contextual prompts, QR handoff, PWA `related_applications`, Play listing + Data safety + target audience, closed testing (personal account: 12 testers × 14 days, to verify in the Console; an organisation account is exempt), staged production rollout, launch comms | Play production access; the live listing; web→app and app→web links working on real devices |
| **6. Measure & iterate** | North Star + activation dashboard; experiments from research §10.4 (sample → next step; result ending; optional reveal; weekly goal vs streak; "Why this?" vs generic copy; Practice/Improve/My Goal IA). Negative results are kept | Pre-registered hypotheses and guardrails; decisions logged |

Parallelism: Phase 2 (web) and Phase 3 (app) can run side by side in separate worktrees once the Phase 1
contracts they share exist. Two writers never touch the same files.

---

## 9. Decisions

Answered by the owner, 12 Oct 2026:

1. **App stack:** ignore the old Capacitor app. Flutter is the owner's known, preferred feel; React Native
   was acceptable only if it made account sync easier. It does not (§3.1). → **Flutter.** The owner can
   still choose React Native; nothing has been built yet.
2. **Selling Pro in the app (v1):** **no.** Pro bought on mockmob.in is honoured in the app. The app
   shows no prices or purchase links until the Play Payments policy route is chosen. Later options are
   Play Billing with UPI Autopay subscriptions, India's alternative billing, or consumption-only. Verify
   the current policy first.
3. **Homepage:** **restructure around the loop, keeping every feature** (§6.1).
4. **Play account:** **a personal account exists.** If it was created after 13 Nov 2023, expect a closed
   test with 12 opted-in testers for 14 consecutive days before production access. This is per
   third-party guides; verify the exact rule in the Play Console. Recruit testers early (existing users,
   creator partners' audiences, friends) and start the closed track as soon as the MVP is stable.

Still open:

1. **Play details:** app name and package. Proposal: "MockMob", `in.mockmob.app`; the beta id was a
   placeholder. Play App Signing plus who holds the upload key. One real budget Android test phone.
2. **Measurement.**
   - Approve a minimal first-party event table (no third-party SDK), with consent wording.
   - DPDP under-18 handling is needed before ~13 May 2027.
   - Crash reporting: Play vitals only, or add an SDK.
3. **Monthly ₹99.** When the Razorpay monthly plan ID goes live, so the copy can switch everywhere at once.
4. **Notification defaults.** Ask after the first result. Proposed quiet hours 23:00–07:00 IST, editable.
   Weekly frequency cap.

---

## 10. Risks

| Risk | Handling |
| --- | --- |
| No fresh-question supply → "Prove" stays thin | Every fresh-check surface has a truthful "practice, not proof" state; the plan never markets checks the content can't serve |
| Dirty repo, 30 commits behind | Build only in clean worktrees off `origin/main`; reconcile the dirty tree as its own task |
| Play policy (billing, minors, Data safety, exact alarms, closed testing) | v1 sells nothing; inexact alarms; deletion + privacy shipped before submission; verify the current Console rules at Phase 5 |
| Budget Android performance | Real-device measurement in every app phase; transform/opacity-only motion; size budget |
| Feature overload (the research's S-curve warning) | Each new mechanic states its behaviour, distortion risk, exit and the metric that would remove it |
| Two truths (score/progress) | Server-only scoring and plans; a shared contract package; contract tests |
| Notifications becoming pressure | Opt-in after value, quiet hours, cancellation, opt-out tracking as a guardrail |
| Session sync load at scale | Delta sync in Phase 1, before the app adds traffic |

---

## 11. How each slice gets built (definition of done)

1. **Before code:** fill the research §11.2 experience brief: job, journey, evidence basis, primary action,
   states, emotional intent, persistence/cost, web/app adaptation, ending, acceptance evidence.
2. **While building:** reuse tokens, components and contracts. Implement states together with the
   operation. Keep Mobi out of timed answering. No paid model call outside its budget guard (USD 50
   lifetime content; USD 25/IST month student AI).
3. **Before calling it done:**
   - Exercise the rendered flow on a small phone and on desktop/tablet, in both themes, with long labels,
     keyboard/TalkBack and reduced motion.
   - Exercise its failure and interruption paths.
   - Run the relevant suites.
   - Label evidence precisely (a fixture is not a student, an emulator is not a device).
4. **After:** record what was verified and what remains open in STATUS, save a Continuum checkpoint, and
   get the owner's review in the real UI.

---

## Appendix: research → plan traceability

| Research source | Plan items |
| --- | --- |
| §2 coherent experience, emotional arc; brain §3.8 | §2 promise and rules 1, 5; A2 copy by outcome |
| §3 orchestration (7 questions per feature) | §11 brief; §7 states |
| §4 data → form, denominators, truncation, timelines, colour, disclosure | Rule 4; §6.5; "Why this?" sheet |
| §5 hierarchy, grids, type, colour ramps, icons/buttons, state contracts, overlays/motion cost | §6.4 design system; rule 10; §3.5 |
| §6 Undertone: diagnosis, core test in onboarding, cadence, brand first, processing visibility, 7 interventions, peak–end, distinctive ending | §3.4 first run; A2; A3; A4; A5; Phase 0 tokens first |
| §7 Duolingo/Phantom/Revolut; hidden assumption; economics | A9, A10; rule 2 (low-commitment start); §2.1 roles; cost per useful cycle in Phase 6 |
| §8 PBL, local competition, richness, streaks, variable reward, completion, competence, addictive architectures, community | Rules 7–8; A8; risk "feature overload"; community deferred until a moderated purpose exists |
| §9 recap blueprint, copy, navigation, sharing, app continuity | A2, A3, A9; §3.2 IA test; §4 continuity |
| §10 recommendation contract, learning proof, retention events, experiments | §7 next-move contract; event contract; Phase 6 |
| §§11–12 agent workflow, rubric, 16 + 24 acceptance scenarios | §11; phase exit evidence |
| §13 opportunity order | Phase order 0 → 6 |
| Brain §8.1 landing structure; §8.2 app launch logic; §8.3 growth; §8.4 pricing trust | §6.1; §3; §5; §6.6 truth fixes |
| Brain §§9–14 next move, data model, policy, API, verification, failures/privacy/a11y | §7; §3.5; §9.4 |
| Brain §15 North Star, events, metrics | Rule 12; Phase 6 |
| Dashboard transcript (C001–C058) | §6.4–6.5; rules 3–4 |
| Emotional-design / gamification transcripts (L001–L201) | Rules 5–8; A8–A10; §5 growth |
| Figures 15–20 (PDF pp. 15–20) | A1 Today layout; result-to-repair ending; card anatomy; "Why this?"; honest states; deterministic pipeline |
