# MockMob CTO loop (living document; update after every wave)

Owner, 15 Oct 2026 about 21:45 IST: "act as a CTO ... Keep on a self-improvement loop of: adding features; making them useful (that's the most important); refining the UI/UX, the motion, motion graphics design; improving the quality, fluidity, and better-looking mascot."

Sources this consolidates (his words win; read them when in doubt):
- the 93 owner messages of session 604ced81, 12-15 Oct (`mockmob-next/tmp/resume-2110/OWNER-MESSAGES-604ced81.md`);
- `OWNER-VISION-2026-10-15-PM.md`, with his standing goal and its checklist;
- `APP-UX-AUDIT-2026-10-15.md`, with 25 ranked findings;
- `HANDOFF-2026-10-15-EVENING.md`;
- the memory files `cto-mode-standing-goal`, `platform-focus-mobile-first`, `web-restructure-rejected`, `features-over-retesting`, `mockmob-design-direction`, `quality-bar-and-stop-rule` and `subagent-model-choice`.

## 1. The loop (every wave)

1. **Pick** from the queue (section 4): usefulness first, then what he named, then polish.
2. **Route.** Every design-level agent (UI, motion, visual polish, critique) loads three skills with the Skill tool, in this order: ui-ux-standards (the owner's rules; section 10 is the AI-slop list and wins every conflict), then impeccable (critique and polish), then frontend-design (distinctive visual direction). Owner, 16 Oct 00:50. Design agents also read the owner's research brain (16 Oct 02:55): docs/research/premium-ux-ui-2026-10/AGENT_RULES.md plus the paper for their screen (summary: AI OS wiki/concepts/premium-ux-research-2026-10.md; merged into ui-ux-standards section 13; the research wins over older rules), and cite evidence IDs (T001-T009, S010-S018). Sonnet builds. Opus is used only for complex UI/UX, extreme motion graphics and polish. Haiku takes quick tasks under 5 minutes. Set effort explicitly on every agent. Planning stays in the main session.
3. **Build** on app and website together, on disjoint paths, continuing from the newest base. Never redo done work: check git log and the code first.
4. **Check once:**
   - analyze and the touched area's tests;
   - one web build;
   - goldens only where intended, opened and looked at.

   No emulator recordings unless he asks.
5. **Critique against his bar.** The main session asks for each change:
   - Is it useful? See the test below.
   - Is it richer than before, not plainer?
   - Is it balanced (not sparse, not over-gamified)?
   - Is it mobile-first on the landing?
   - Is it truthful?
   - Is it premium in motion?
6. **Quality gate, then ship (owner, 16 Oct 00:35: "not compromise quality for speed... every small new change, is actually tested and critiqued properly, then deployed").** Website: lint, the suites and a build, then a visual critique: a dev server, headless captures of every changed page at 390 and 1440 in Night and Day, looked at and clicked, with defects fixed. App: analyze, the tests, and the changed goldens opened. Nothing ships on tests alone. Design critics score with the research's 12-dimension 0/1/2 rubric and its 12-part anti-slop acceptance test (not a single /100 number), and every design packet leaves a short DESIGN_DECISIONS note (user task, alternatives, reason, evidence IDs, trade-offs, assumptions, before and after, verification) in docs/design-decisions/<branch>.md. Big visible changes (the landing) also get the owner's look on a local server before launch. Then:
   - the website: merge, deploy, check Vercel;
   - the app: APK, then install on his phone if it is connected, and send the zip.
7. **Update** this file's status column and the brain checkpoint. Then go back to step 1. Stop only at about 95% usage, with a handoff.

**Usefulness test (the most important).** A feature ships only if it changes what a student does next:
- it gives a clear next action, one tap away;
- every number is from their own data or a cited source, with its denominator;
- a Class 12 student understands it in 3 seconds.

"Confusing" means improve the UI and the words. Never cut the feature.

## 2. The vision, consolidated (status as of 15 Oct 21:45 IST)

| # | Vision item (his words, short) | Status |
|---|---|---|
| V1 | The app is distinctive: "not just a copy of the website ... something more and the best out there" | ongoing |
| V2 | Premium feel like HIGH, Revolut and Fampay: glass, rich motion, generated imagery, "nothing but perfection" | ongoing |
| V3 | Mobi everywhere with emotions and actions, Duolingo-level; a better-looking mascot | partial: emotion kit and parity done; quality pass queued (Q6) |
| V4 | Motion graphics, fluidity, finish; judged in use, not static | ongoing |
| V5 | Balanced (crowded beats sparse; over-gamified is as bad as sparse); one spacing system; Night/Day parity | ongoing |
| V6 | Memorable post-mock moments (Undertone-style recap), supportive streaks, celebrations without pressure | done in the app (recap, milestones); web parity partial |
| V7 | Exciting, plain copy; no defensive sub-remarks or "illustrative" lines | done on the landing; app copy pass queued (Q3) |
| V8 | Mistake Lab is the USP, "10 times more useful"; insights no one else can give; SWOT after each mock | slices 1-3 live (slice 3 deployed 15 Oct about 23:00, main 3fc0095b); slice 4 building (wave N+1) |
| V9 | The website takes the app's clarity without being cut: landing mobile-first; arena desktop-first and phone-ready | v2 live; one gesture moves one step, footer sign-up, explanatory illustrations and the speed pass (41% fewer landing bytes) deployed 15 Oct about 23:00; arena pass 3 building |
| V10 | State-aware website: signed-in users go straight to the arena; content fits free, paid, new or returning | check in Q9 |
| V11 | Sign-in that just works (Google, email code, password, maybe phone) and stays signed in | Google and email fixed today; 403 insurance queued (Q1) |
| V12 | NTA mode exam-faithful on web and app; CUET-fit questions; prefer the newest questions | done (r5 live) |
| V13 | CUET tools (Compass, Combo, guide) integrated into the flow with hierarchy, not hidden | resuming (app tools packet); Q4 for the shared colleges list |
| V14 | You and Profile as a real hub: a top-bar avatar, findable light/dark, account settings, credits | wave 4a resuming; Q5 for the full hub |
| V15 | Ask Mobi integrated with credits; two credit names everywhere | wave 4a resuming; Q2 for the credits page and history |
| V16 | Stay on free plans until launch: usage fixes, fix 5, backups | fixes 1-4 live 21:10; fix 5 queued (Q8) |
| V17 | Minimal first-party analytics with consent (off for minors and unknown ages); quiet hours 11 pm-7 am | consent switch done; funnel queued (Q10) |
| V18 | Play Store release (14-day test) | owner steps pending |

## 3. Running now (updated 16 Oct about 09:25 IST)

- **Production database, 16 Oct about 04:20:** trap_atlas, revise_cards, my_colleges, app_errors and funnel_daily applied under the standing grant; RLS on, service role only; STATUS.md 2a20d407 with undo paths.
- **Batch 1 pushed to main 16 Oct about 09:15 (09421b29):**
  - Mistake Lab slice 4 web (traps, Traps you meet, Revise, same mistakes later);
  - Mobi rig v2 web, My colleges, crash reports, names, Learn concept checks;
  - the arena de-slop A1-A3.

  Gate: four critics with the research rubric found 78 defects (1 blocker, 36 majors). An Opus fixer fixed them, and an independent verifier passed it: lint clean; test:app 328, test:recovery 231, test:learning 277, test:nta 169 all pass; `next build --webpack` passes. Check Vercel READY and runtime errors.
- **Batch 2 gate (wf_9bf4ba21-fa3, wt-batch2, deploy/batch-1016b):**
  - Repair v4: Check it held, Ask Mobi about Qn, the older-paper Lab line, marked-for-review in the SWOT, plus the follow-ups (e2d950ae);
  - web/ntaidx-1016: the practice-progress chunking fix; the index stays inert without the signing key;
  - web/pay-monthly-1016: inert until RAZORPAY_PLAN_ID_PRO_MONTHLY_99 is set; honest pricing copy bca252dc.
- **App:** APK v10 built at tmp/apk/mockmob-v10-9ccb7d0c.apk, with the zip sent to the owner. feat/app-and-web 9ccb7d0c holds ui/phase2 7501acf9 (phase2b merged) and a8252ca4 (Repair v4 in the app). Analyze clean; 4,715 unit tests and 1,063 goldens pass. Not installed: no phone was attached.
- **Landing (wf_3ee8e5c5-8e4, wt-land2):** critic scores 76, 82, 84, 87; fix-4 then critic 5. It needs the owner's look on a local server before launch.
- **Slice 5, cohort time (wt-slice5, web/slice5-1016):** being built. Migration on staging only; it rides on the inventory cron.
- **Open gaps after these land:**
  - Mobi at real moments everywhere (web and app);
  - Q13 landing calm-down;
  - the app half of slice 5;
  - live-database checks of `.is('receipt->check', null)` and `receipt->offered` claims after the deploy.

## 4. Queue (in order; skip anything the running wave finished)

| Q | What | Why (usefulness or his words) | Routing |
|---|---|---|---|
| Q1 | **Done 15 Oct 22:10** (24665cac on ui/phase2): edge-firewall 403 and HTML responses are now retryable "blocked", never a refusal. P0-2 and P1-14 were already done in 7be2e9ec. Left: show the "blocked" line on the runner's submit-pending screen (features owner), and a server analytics event | A paper or a queued write must never be lost | Sonnet high |
| Q8b | NTA index (A6) in production, **only once publishing rebuilds it automatically**: a stale index silently drops newly published questions from NTA papers, which breaks "prefer the newest questions". Make the authored-publish step (or a daily cron) run nta-index-build for the touched subjects, then apply per RUNBOOK-NTA-QUESTION-INDEX-2026-10-15.md. Also decide on chunking _userProgress (Accountancy history is ignored above about 700 ids) | Egress at scale; newest questions kept | Sonnet high |
| Q2 | Credits: two names only; one Credits page with both balances, the renew date and a history list (new GET /api/me/credits/history); every spend line names its pool and total (P1-12, 13) | Students must see what they spend | Sonnet high, web plus app |
| Q3 | Copy and naming pass: Ask Mobi everywhere, Quick practice (10 questions), the audit's jargon list (P2-18, 19) | Plain words | Sonnet medium |
| Q4 | One "My colleges" list on the server, shared by Today, Compass and You; Choose opens the chooser; Compass hierarchy and score prefill (P1-5 to 9), if the tools packet left them | Tools in the flow, not hidden | Sonnet high |
| Q5 | You as a real hub (audit section 3: profile, plan and credits, appearance, notifications, study days, colleges, progress, sign-in, privacy, help with FAQ) | "Doing a bit less" | Sonnet high |
| Q6 | **Mobi quality pass:** a better-looking rig, more actions and emotions, smoother motion, the same Mobi on web (I3 web half) | V3, his explicit ask | Opus high (rig and motion) plus Sonnet medium (web port) |
| Q7 | **Mistake Lab slice 4:** the trap atlas, "same mistakes later" (spaced re-check), the key-quality loop | V8, the USP | Sonnet high; Opus only for its signature visual |
| Q8 | **A5 deployed 15 Oct about 22:15** (main d9e290eb): a slim session start, with picks identical to before; per start, about 8.3 MB becomes 3.5 MB for Accountancy and 6-7 MB becomes about 1.8 MB for the others; kill switch PRACTICE_SLIM_READ=off. A6 is held (see Q8b). Weekly backup: owner steps in the Q8 report (Supabase CLI dump with the DB URL in a user environment variable). Agents testing on staging: still to do | V16; before more testers | Sonnet high |
| Q9 | Website arena on phones, pass 3: Today's dropdowns, Review details, the critic leftovers in tmp/web-v2-pass2/critic-2; state-aware entry for signed-in users | V9, V10 | Sonnet high; Opus for motion polish |
| Q10 | Analytics funnel (server-side, consent-respecting) and app crash reporting | Know what breaks | Sonnet medium |
| Q11 | Web halves of motion language, living objects and sharp scenes, where the website lacks them | Parity, fluidity | Sonnet high; Opus for the object flight |
| Q12 | Bar blur 24 sigma with lighter tints; the capsule never covers the hero; the week strip skeleton (P2-20, 22, 24) | Finish | Haiku low or Sonnet low |
| Q13 | Landing calm-down, with nothing removed (owner, 15 Oct 23:45: "we are bombarding them with too much information ... don't take any regressive actions"): one idea per screen, with details behind "See how"; tune with the Q10 funnel. Also a "Get the app" section and an Android-only smart banner, built behind a flag until the Play Store link exists. iOS: none for now (decision below) | Conversion | Opus for the hero and section rhythm, Sonnet for the rest |
| Q14 | **DEFERRED to January 2027 (owner, 15 Oct 23:59: "Right now, the entire focus is on product"). Commerce growth stack:** phone number with OTP sign-in (a WhatsApp OTP, plus Truecaller one-tap as an option); an explicit, unticked WhatsApp opt-in at sign-up and checkout; "get your sample result on WhatsApp" after the 5 questions; abandoned-checkout recovery (a retry screen, then one WhatsApp or email reminder, opted-in only); everything behind flags until the owner sets up a WhatsApp Business account through a provider. Season 2026 facts: 98 students paid, Rs 8,238; marketing spend was over Rs 15,000; 109 students started a checkout and never paid; about 30% of orders came through creator codes. Legal: India's data protection law (DPDP Act 2023): no data broker or visitor-identification vendors; many CUET students are under 18, so marketing needs parental consent, and minors get service messages only | Revenue; recover the checkout leak | Sonnet high; Opus for the checkout UX |

## 5. Owner items (ask only for these)

- Delete the 5 paused Vercel projects.
- Say whether students can reach Razorpay checkout today (this decides when to move to Vercel Pro).
- Play Store: the upload key, the Google client ID, Play Console.
- One Mistake Repair on the site, to verify the v3 cost.


**16 Oct 02:20 IST (owner):** the Vercel duplicates are deleted. He will do the Razorpay Rs 99 monthly plan (RAZORPAY_PLAN_ID_PRO_MONTHLY_99 in Vercel; the code switches to monthly automatically), the SUPABASE_DB_URL backup variable and the Play Console steps on the night of 16 Oct; a scheduled reminder is set for 16 Oct 21:00 IST (task mockmob-owner-production-steps-reminder). He will take one fresh mock on the site on the morning of 16 Oct: his own papers predate the slice 2 capture, so the Lab looked thin on his account. The live v3 repair at 02:16 worked (850 in / 524 out tokens, USD 0.00035, all v3 fields). His verdict: a paid repair that mostly explains the key is not enough. CEO decision: make the paid repair a learning loop (retry before the key, a fresh checked question on the same rule, the rule brought back on Revise, the personal trap pattern, ask a follow-up), reusing what slice 4 and the fresh-check code already built; scope it after the vision inventory (docs/brain/VISION-INVENTORY-2026-10-16.md).

## 6. CEO direction: the next horizon (set 15 Oct about 23:20 IST)

The owner, 15 Oct night: "Being the CEO of the company, also act as the CEO and take decisions... You have the direction and taste now." These are the bets every wave serves:

1. **Convert the visitor in the first 60 seconds.**
   - The path: a subject-aware sample, then their own result, then "Save your answers" (sign up).
   - Measure it with the privacy-safe aggregate funnel (Q10), then tune the hero and the dock from real numbers, never guesses.
2. **The Mistake Lab is the moat.**
   - It gets better with every student: cohort picks and times, the trap atlas, the key-quality loop.
   - Ship slices 4 and 5, then make the Lab the hero of the landing and of the app's result moment.
3. **Return every evening.**
   - Tonight's move, "same mistakes later" (1, 3, 7 and 21 days) and study-day reminders in the student's window.
   - A streak that never punishes.
   - Mobi as the companion who notices progress.
4. **Trust above all.**
   - Every number true, with its denominator.
   - NTA exam-faithful.
   - The newest, CUET-fit questions.
   - Sign-in that never fails.
5. **Growth loops.**
   - A shareable post-mock card (the app has sheet_share; bring it to the web).
   - Then a friend invite tied to credits: an owner decision before money is involved.
6. **Stay lean until launch.**
   - Free plans: usage fixes 1-5 and the self-maintaining NTA index.
   - Move to Pro at about 1,000 daily students.
   - Play Store release as soon as the owner's keys are in.

**iOS decision (owner and CEO, 15 Oct about 23:50):** no iOS app until there is evidence: paying students, or iPhone above about 10-15% of sign-ups, or repeated requests. iPhone users get the website, installable to the home screen. The Flutter code keeps an iOS port cheap later.
