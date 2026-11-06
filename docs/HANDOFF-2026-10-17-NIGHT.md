# MockMob handoff: 17 Oct 2026, about 3:40 am IST (session cc0bf1af, Claude Opus 5.5 as CEO/CTO)

**Read this whole file before acting.** It is the single source of truth for the next session. Newest owner words win. Check every agent claim against git, production and the files before acting on it. Older context:
- `HANDOFF-2026-10-16-NIGHT-FINAL.md` (16 Oct, sections 1-11)
- `HANDOFF-2026-10-16-DAY.md`
- `CTO-LOOP.md`
- the memory index: `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\memory\MEMORY.md`. Read every entry. The newest is **owner-feedback-1017.md**.

---

## 1. THE GOAL

**Ship a visibly new, clearly better MockMob on the website and the Android app, built from the owner's 17 Oct feedback and decisions, with every piece proven before he sees it.**

The test is simple: a student opening the app or the site knows what to do next, uses the features, and feels the value of what they pay for.

**Vision for the next 5-10 hours, in order:**

1. **Website (first 1-2 h):**
   - Ship the verified motion/UX pass.
   - Finish and ship the six 17 Oct website redesigns:
     - the result screen in three layers;
     - Start, fine-tune, the runner fix and the Start button state;
     - Today as "Up next";
     - the phone dock;
     - the Mob free/Pro split (still OFF until it is 10/10);
     - retiring "41 subjects".
   - Ship the landing only when the critic gives it 88 or more with no truth defects.
2. **App (hours 1-5):**
   - Finish the v12 walk and fixes, then release v12.
   - Build **v13 from the 17 Oct designs**: nav option A1 (with the active-tab bubble refined), the liquid-glass material and bounce, the new result screen, Today "Up next", the Start sheet and fine-tune rules, the Mob app side, and the app UX pass.
   - Walk v13 on the emulator against the F1-F18 ledger and the 16 Oct ledger, with screenshots and motion clips.
   - Release v13. **The owner's biggest complaint tonight: the app still feels like the old app. v13 must look and feel new.**
3. **Content (in parallel, session-based):**
   - Run the full wave 1-2 scoring on the 294 wave-3 drafts (GAT, Physics, Chemistry): 5 blind solvers, 2 rubric judges, 3 CUET-fit judges, the acceptance rule, an expert pass, and a re-solve of repaired rows.
   - Publish only questions scoring 8+ (8+ is NTA-eligible; well-scored 5-7 may be kept for practice only).
   - Hindi stays off.
   - Then start session-based depth waves: GAT, Physics, Chemistry, Maths, Biology, toward about 600 verified questions each.
4. **Feature adoption (woven into 1 and 2):** apply `FEATURE-ADOPTION-2026-10-17.md`:
   - the Find, Fix, Keep loop;
   - one next move per screen;
   - Repair on the mistake row, with its value stated before paying;
   - receipts;
   - a first-week path;
   - features introduced at the moment they are useful;
   - empty states that teach.
5. **After that:** Learn and Review refinement (F15), then the Higgsfield landing and onboarding scenes through their idea, storyboard and approval loop (`HIGGSFIELD-IDEAS-2026-10-16.md`).

**"Done" means:**
- **Website:** live after its gate.
- **App:** an APK in the owner's hands after an emulator walk.
- **Reporting:** honest percentages and relative times, 12-hour clock.

---

## 2. Owner rules (standing; newest first; these override defaults)

### New tonight (17 Oct), all in memory owner-feedback-1017.md

- **Feedback ledger F1-F18** (`docs/brain/OWNER-FEEDBACK-2026-10-17.md`, his words verbatim). This is the acceptance list next to `APP-OWNER-LEDGER-2026-10-16.md` (L01-L39).
  - **Nav:**
    - **A1 chosen**: option A, a glass capsule of 5 tabs (Today, Practice, Review, Colleges, You) plus a separate round Start key with a **lime fill**.
    - Refine the active-tab bubble: over Practice it "cuts into" the icon and "feels weird".
    - B1 (Start in the exact centre, You in the avatar) was also liked, but its alignment was off.
  - **Practice screen:** **never lose its blue light and textured cards.** The nav mock only drew a stand-in behind the bar.
  - **Liquid glass (F3):** carry Apple's Liquid Glass taste into the app UI (not the Android system UI). Bounce instead of Android's stretch where the app owns scrolling. Plan: `docs/design-decisions/pass-1017/GLASS-1017.md`.
  - **Result screen (F11):** "too cluttered... even for me".
    - Remove the sleeping Mobi (a sleepy-at-night rule: reaction.js on the web, recap_variant.dart in the app).
    - Repair's value must be clear before paying.
    - The submission is shown 3-4 times; show it once.
    - SWOT, analysis and repair are stacked; fold them into sections.
    - Check it held is fine.
    - Plan: `RESULT-1017.md`.
  - **Website Start menu (F4-F8, F10, F12):**
    - Mode rows must feel like pressable buttons.
    - Bigger subject logos, with the card's name following the selected subject.
    - Stronger blur on the other subject chips.
    - Fine-tune sits above Start, with chapters grouped and searchable.
    - Fix the Start button's scroll flicker.
    - Fix the runner's double box when an option is picked.
    - Plan: `START-1017.md`.
  - **Fine-tune scope (F9), a hard rule, enforced on the server:**

    | Mode | Fine-tune |
    |---|---|
    | Quick practice | chapters and difficulty |
    | Full mock | difficulty only |
    | NTA mode, Smart practice | none ("we pick for you") |

  - **Today (F14):** "never really liked: very cluttered, very confusing". Plan: `TODAY-1017.md`.
  - **Learn and Review (F15):** need refinement.
  - **Review (F17):** a mistake already repaired must open its saved repair (never offer a paid repair again), and each mistake shows which mock it came from, with date and time.
  - **Adoption (F18):** students didn't use 90% of features last year; learn from top edtech (`FEATURE-ADOPTION-2026-10-17.md`).
  - **Dock (F13):** the Start placement looks weird, and his earlier dock feedback was not applied.
- **"Act with it as the CTO. Define it."** Decide and execute from his recorded taste. Don't re-ask decided things.
- **The Mob** (spec `docs/design-decisions/pass-1016e/SOCIAL-SPEC.md` **section 15**):
  - **D-S1: open to everyone, final.** No age gate, no consent flow; he accepts the risk.
  - **D-S2: neither all free nor Pro-only:**
    - **Free:** start 1 Mob and join any; the weekly 10-question Mob paper with no credits; the shared ring; your own result; a one-line teaser of where the Mob split.
    - **Pro:** the full side-by-side per question; history; extra papers on a chosen chapter; up to 3 Mobs.
    - **The hook:** the first Mob week shows the full side-by-side once, free.
  - **His bar:** "10/10 only if execution is 10/10." It stays behind MOB_ENABLED until gate plus walk show it polished.
  - **Hosting cost:** about zero (no AI, a few rows per member per week).
- **AI money** (`docs/brain/AI-COST-PER-USER-2026-10-17.md`):

  | Setting | Value |
  |---|---|
  | Pro credits | 50 AI credits a month |
  | Free credits | 10 AI credits a month |
  | Per-user cap, paid | **Rs 5 a month** (`runtime_ai_budget` student_user_paid 0.0568) |
  | Per-user cap, free | **Rs 1 a month** (student_user_free 0.0114) |
  | Global USD 25 ceiling | **removed** by the owner (student_ai monthly_cap_usd = 1000000) |

  - **Only two models anywhere in the app or website:** gpt-6-luna (openai) and claude-haiku-5-5 (anthropic). This is enforced in code (providerCore) and in `reserve_runtime_ai`.
  - Typical cost is about Rs 2 a month per heavy user.
  - The owner set his own billing alerts.
  - AGENTS.md still says "USD 25 per IST month": update it in the next web deploy.
- **Funding:**
  - Claude startup grant: this Team plan plus **USD 1,000 Anthropic API credits** that expire in the first week of April 2027. Possibly USD 500 a month more across his 5 team accounts.
  - Students arrive from mid-April, so the credits will mostly go unused by students.
  - **When he adds the Anthropic key, switch all runtime AI to Haiku 5.5 as primary (Luna fallback).** He will say when.
  - He is leaning toward **session-based question generation** (agents, not the paid pipeline), possibly a dedicated account farming questions 24/7. He has not decided on spending API credits on bank re-validation.
- **Questions:**
  - Generated questions must follow every wave 1-2 rule (see section 7).
  - Publish only questions scoring 8+ (8+ is NTA-eligible).
  - Well-scored 5-7 questions may be kept for practice only.
  - "Top quality is our main priority."
  - **Hindi:** the owner can't read it, so it stays off until a fluent human checks a sample (he may find someone).
  - **Open syllabus question:** the repo's 2026 Hindi PDF lists only Reading Comprehension and Verbal Ability.
- **Subject claim** (`docs/brain/SUBJECT-COVERAGE-2026-10-17.md`):
  - **Retire "41 subjects".** Truthful claim: "Full NTA-pattern mocks for the 15 subjects behind 19 of every 20 CUET papers (2026 NTA data)".
  - Hide the 4 subjects CUET dropped in 2025 (entrepreneurship, teaching_aptitude, legal_studies, engineering_graphics) from pickers.
  - Depth first: GAT, Physics, Chemistry, Maths, Biology. Then Hindi, then Physical Education verification, then Agriculture.
- **Business Studies art:** the open briefcase (in the app ui/owner-1016 and web/art-1016). Every other subject's art stays. Don't regenerate art unasked.
- **Razorpay, Play, Supabase backups and Vercel switches:** "leave for now / later".

### Standing from before (still in force)

- **Role and pace:**
  - CEO and CTO; many parallel agents (15-20 when usage and RAM allow).
  - Never stop to ask about routine work.
  - Honest percentages.
  - Stop at about 95% usage with a handoff.
- **Routing (subagent-model-choice):**
  - Sonnet does the heavy lifting.
  - Opus only for complex UI/UX, motion and polish.
  - Haiku for quick bounded tasks and question authoring and solving.
  - Set effort explicitly.
  - Planning stays in the main session.
- **Design:**
  - Research brain `docs/research/premium-ux-ui-2026-10/AGENT_RULES.md`, the ui-ux-standards skill, impeccable and the other design skills.
  - Banned: eyebrow pills or dots, glow, gradient text, icon grids, nested cards, arrows on buttons, ALL-CAPS labels, hype, build talk.
  - One volt (lime) primary per viewport.
  - Mobi at most once per screen, only at real moments.
  - **Never simplify by cutting features.** Real numbers with denominators. Night and Day parity. 44 px web and 48 dp app targets.
  - Headline USP: **unlimited mocks from one central bank**, calm and truthful.
- **Gates:**
  - **Website:** suites, a visual critique at 390 and 1440 in Night and Day, and an independent verifier. **Push the moment the verifier passes.**
  - **Landing:** critic 88 or more plus a verifier.
  - **App:** an emulator walk with screenshots (upgrade, keyboard, scroll, Night and Day). Goldens alone never count.
- **Security and access:**
  - Never drive his browser or sign in as him. Never use the chrome-devtools MCP or a visible browser (tonight an agent did; the main session had to kill it).
  - Use only the project test account `app-e2e-student@example.com` on staging.
  - Use his phone only when he says it is connected.
  - Standing OK to hotfix crucial security issues.
- **Production DB:** standing grant. Save the migration, dry-run on staging, keep an undo, add a STATUS entry.
- **Resource hygiene:**
  - Reap leaked processes between waves.
  - Put a RAM rule in every agent prompt.
  - Check get_usage before waves.
  - Take a WIP snapshot after any mass agent death.
- **Product only.** Marketing waits until January.

---

## 3. Live in production now

**mockmob.in = main e192c59e** (Vercel dpl_DshEL7as2kR8RE5GDuM9NuBPG48A READY, 0 runtime errors after deploy):

- **Batches 1-3:** as in the 16 Oct handoff.
- **Batch 4 (bc099c53):**
  - college search for BCOM;
  - badges and personal bests (GET /api/me/badges);
  - study weekdays on the account;
  - the AI-report route (POST /api/ai/mentor/report, Play blocker);
  - the Compass row on Today;
  - the timed-mock nudge;
  - Help (/help);
  - the copy pass;
  - the Rival reveal with Mobi;
  - funnel calls (FUNNEL_ENABLED off);
  - auth cache, egress cuts and security-2 (webhook lease);
  - unlimited-mocks copy;
  - the art briefcase (web).
- **a2fe34b4, leaderboard privacy hotfix:**
  - GET /api/leaderboard was public and returned **794 real students' names, user ids and 608 photos plus 12 fake "Practice rival" students**.
  - It now requires sign-in and returns only `{you:{rank,of,tests,average}, window:'all time'}`.
  - /leaderboard is "Your standing".
  - topContributors returns counts only.
- **e192c59e, per-user AI cap plus two-model allowlist:**
  - at most 2 physical calls per action;
  - reasoning headroom 1,000 tokens;
  - Ask Mobi context capped at 12 KB;
  - account deletion nulls runtime_ai_requests.user_id.

**Production DB, applied tonight with pre and post checks:**

| Migration or change | Effect |
|---|---|
| `20261016170100_webhook_event_lease` | webhook_events.claimed_at |
| `20261016110000_study_weekdays` | study_goals.weekday_mask, with a 1-127 check |
| `20261016140000_ai_reply_report` | ai_reply_reports, RLS on, service role only |
| `20261016120100_funnel_product_steps` | users.funnel_seen, funnel_count_once |
| `20261017120000_runtime_ai_user_cap` | runtime_ai_requests.user_id; 7-argument reserve_runtime_ai with the allowlist |
| `runtime_ai_budget` updates | student_user_paid 0.0568, student_user_free 0.0114, student_ai 1000000 |
| Earlier on 16 Oct (session cc0bf1af) | public.questions closed to the anon key |
| Earlier on 16 Oct (session 604ced81) | NTA index rebuilt (653 rows, 0 signature failures) |

**Not applied (staging only):** the Mob migration, the funnel ENABLED flag, and Today's possible exam_date / mock_target migration.

**Proven live tonight (the owner's own account):**
- Mistake Repair v4: 3 repairs on 3 different chapters (Admission of Partner, Cash Flow Statement, Share Capital). Each was charged 1 credit once, on gpt-6-luna with no fallback, about 815 input and 387 output tokens, about Rs 0.03 each.
- **Check it held** recorded both a right and a wrong answer.
- No double charge.

**Known live issues to fix:**
- The repair route logs a harmless diagnostic to stderr on every repair (`{"route":"repair","stage":"interpret",...}`), so it shows as a Vercel "error". Move it to info.
- One Accountancy repair got trap_type "not_in_passage" (a reading trap label). Check the trap labelling for non-passage subjects.
- `src/lib/motion-tokens.test.mjs` has 1 failing test on main (motion-kit.css token): pre-existing.
- English NTA can't build a full paper (too few high-score questions).
- The Luna price row must be re-verified before about 1 Jan 2027 (the guard rejects rows older than 90 days).

---

## 4. In flight at the stop (workflows die with the session; check each by git and journal)

Journals are under `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\cc0bf1af-4c1f-4097-81a5-97ba84470f41\subagents\workflows\<run id>\journal.jsonl`. Section 13 records the exact heads at the stop.

### Workflow wf_608e70c8-074 "web-build-1017"

It was at **ship:merge**. The stages:
1. **ship:merge:** create `wt-ship17` on branch `deploy/ux-1017` from origin/main e192c59e and merge **web/ux-social-1016 (94c172e6, verifier PASS on its own base)**. Keep the leaderboard privacy shape and the AI cap. Then suites, build and smoke. **Push it the moment it passes.**
2. **Six parallel packets,** each in its own worktree from that head:

   | Branch | Worktree | Content |
   |---|---|---|
   | web/result-1017 | wt-p-result | RESULT-1017 website half |
   | web/start-1017 | wt-p-start | START-1017, fine-tune scope enforced server-side, F12, F10 |
   | web/today-1017 | wt-p-today | TODAY-1017 website |
   | web/dock-1017 | wt-p-dock | NAV W1 phone dock: capsule Today, Practice, Review, Colleges, More, plus the Start key |
   | web/mob-split-1017 | wt-p-mob | Mob free/Pro split; remove the age gate; still OFF |
   | web/subjects-claim-1017 | wt-p-copy41 | Retire "41 subjects"; hide the 4 dropped subjects |

3. **Integrate** into `deploy/web-1017`.
4. **Gate:** an Opus critic, an Opus fixer, then a Sonnet verifier. Push on pass.

Resume it, or relaunch only the missing stages, from the script at `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\cc0bf1af-4c1f-4097-81a5-97ba84470f41\workflows\scripts\web-build-1017-wf_608e70c8-074.js`. Resume only works in the same session; otherwise hand-author the continuation.

### Workflow wf_a59c8a05-169 "resume-1017"

**B: website UX pass.** Fixer 94c172e6, then **verifier PASS**. Its notes, none blocking:
- a 0.5 s double volt during a slow dev load;
- 2 other minor notes in the journal.

It ships through web-build-1017's ship:merge.

**C: landing** (wt-land2, web/land2-1015):
- Round 10 fixer, then critic **74/100**, down from 80.
- **Truth defect:** the Score Recovery Lab and the statement present delayed fresh checks as a live feature, but `data/capabilities.js` has recovery 'blocked_content' and /recovery says the steps are not live. More defects are in `mockmob-next/tmp/resume-1017/C_critic-r10.json`.
- Fixer r11 was running.
- Rule: no shipping below 88.
- **Landing keeps:** unlimited mocks at heading level, no "never repeats", server-rendered counts.
- **Remove "41 subjects" (owner decision).**

**D: app v12 walk** (rig up: staging site 3101, relay 3102, emulator-5554 with the **v12 profile build f5d848bf installed over the fd0da7d3 baseline**; upgrade test PASSED):
- **walk-1A: 14 pass, 5 fail** (full result `mockmob-next/tmp/resume-1017/D_walk-1A.json`, shots `tmp/app-walk-1017/1A`):

  | Item | Failure |
  |---|---|
  | L01 | offline wording missing |
  | L03 | page jumps after load |
  | L09 | mode titles not on one line |
  | L13 | the repair screen lacks the cost statement before the call |
  | L33 | the bar reads as an opaque tint, not frosted |

- walk-1B was starting.
- Then: area fixers, walk-2, then release v12 (version bump to 1.0.12; release command in HANDOFF-2026-10-15-FULL section 5) to `mockmob-next/tmp/apk/mockmob-v12-<sha>`.
- Test-account credits on staging were topped to 160 by a staging-only service-role update.

**E: app UX pass integration** (wt-appux2, ui/ux-social-1016):
- The integrator was running the unit tests.
- Its emulator walk follows v12's.
- Plan: merge into ui/owner-1016 after v12, then **v13**.

### Content wave 3 (`wt-wave3`, branch content/wave3-1017 at **725c0e65**; drafts in `mockmob-next/tmp/authored-w3`)

- **Authoring:** 300 written by Haiku to the blueprints (units, chapters, type quotas, difficulty mix, key spread). One Haiku blind check passed 294.
- **Sonnet audit of a 45-row sample:**
  - 0 wrong keys in 107 rows checked;
  - **defect rate 15.6%**, mostly Hindi: wrong chapter names on 24 rows, one grammar slip, one wrong explanation, and 3 listed-order giveaways;
  - 28 rows repaired (text only);
  - 8 engine-refused rows need rewording;
  - advisories: the key skew is A 76, B 90, C 78, D 50, and the longest option is the key in 41% of Hindi rows.
- **Dry run against production (select-only):** 294 rows would insert (chemistry 74, general_test 97, hindi 49, physics 74). **Blocker:** none has agent or fit scores yet.
- **Hindi work:** a blueprint `data/nta_blueprints/hindi.json` (pending subject), Hindi passage-set storage in authored-wave.mjs, and two Latin-only engine checks fixed for Devanagari.
- **Hindi syllabus question:** the 2026 PDF lists only Reading Comprehension and Verbal Ability.
- **Reports:**
  - `docs/brain/reports/authored-w3/wave3-audit-2026-10-17.json`
  - `wave3-candidates-2026-10-17.json`
  - `wave3-dryrun-2026-10-17.json`
- **What wave 3 still needs, identical to waves 1 and 2:**
  - 5 blind Haiku solvers per question (4 of 5 must match the key);
  - 2 agent-rubric quality judges (j1, j2): each 7 or more, no blocking flag; they also give the difficulty check, objective tag and blind answer;
  - 3 CUET-fit judges (h1-h3): median 8 or more, fewer than 2 flags;
  - the acceptance rule;
  - a Sonnet expert pass setting `_verdict` ready or repaired;
  - a 3-solver blind re-solve of the repaired rows;
  - rewording of the 8 refused rows with a fresh pass;
  - then `node scripts/authored-scores-merge.mjs --mode=merge ...`, then `--mode=check`, then the dry run again, then `--mode=apply --plan=... --expect-project=isrxrxzjocewrdureyhp` after the owner OK (he already said yes for 8+ scored rows).
- **Scripts to generalise:** `scripts/authored-w2-accept.mjs` and `scripts/lib/authored-scores.mjs` (wave 3 source, batch naming). Calibrated Haiku threshold 7 exists for physics, chemistry and general_test.
- **Hindi stays out** (no fluent reviewer, no Hindi score tables, too few verbal-ability items).

### Not started

- **App v13 build** from NAV (A1), GLASS, RESULT, TODAY, START (app parts), APP-PASS and the Mob app side.
- **Learn and Review pass (F15)**, and **Review F17** (saved repair plus the mock date and time on each mistake).
- **Higgsfield.**
- **Mobbin A/B** (optional; the owner may buy Pro).
- **Fixes:** the repair diagnostic log and the trap label.
- **AGENTS.md wording:** the USD 25 line.

---

## 5. Design decisions made tonight (`mockmob-next/docs/design-decisions/pass-1017/`, committed on feat/app-and-web)

- **NAV-1017.md:**
  - **A1**: the capsule of 5 tabs plus a 64 dp round Start key with a lime fill, on one measured row.
  - Colleges stays a tab; Learn moves (web) to the More sheet and Practice.
  - The web phone dock mirrors it.
  - Glass taste: lens lift and magnify, spring release, saturated blur, scroll-minimise, bounce. True refraction is excluded as too heavy for budget phones; revisit with a FragmentProgram if performance allows.
  - Owner questions Q1-Q5 are answered: A1, the bubble needs refining, B1 was liked but not aligned.
  - Mocks: `tmp/design-1017/nav/out`.
- **RESULT-1017.md:** one order for practice and mocks:
  1. **What happened:** a receipt line, the score with its denominator, a 3-part marks bar, and the costliest chapter.
  2. **One next move by rules:** nothing missed means a harder paper; under 40% right means practise the costliest chapter; a repairable mistake with credits means repair the first in repair order; everything repaired means "Check Qn held"; otherwise practise.
  3. **Repair's value in one line** with the cost and balance.
  4. **The mistakes list** in repair order, with Repair and Check it held inline.
  5. **Everything else folded** into named sections.

  Remove the night-time sleepy Mobi. Show the submission once. The site's result page was 13,528 px tall at 390, with 2 volt repair keys and up to 3 Mobis.
- **START-1017.md:** mode rows as pressable buttons; logos; blur; fine-tune placement and scope; chapter search and grouping; the F12 and F10 causes and fixes.
- **TODAY-1017.md:** one "Up next" with a reason, the week, Road to May; other blocks move to their homes (a move table is in the doc). It needs a server migration for the exam date and mock target (staging only until applied). Build packets: P3 homes, P0 server, P1 web, P2 app. Owner sign-off questions are in its section 13.
- **GLASS-1017.md:** the glass material system for the bar, sheets, Start key and floating controls (never on reading surfaces): lensing and highlights, touch and scroll response, a performance budget, the low-quality fallback, legibility, and reduced motion and transparency.

**Research:**
- **FEATURE-ADOPTION-2026-10-17.md:** the ranked changes and the stop list.
- **SUBJECT-COVERAGE-2026-10-17.md:** the 15 subjects cover 94.9% of 2026 CUET paper registrations and about 80% of candidates fully (76-83%). Hindi adds 8.7 points.
- **AI-COST-PER-USER-2026-10-17.md.**

---

## 6. Incidents and lessons tonight

1. **A session crash (about 2:30 pm 16 Oct) killed every agent.**
   - Recovery: 35 orphan processes were reaped; dirty worktrees were snapshotted with a temporary index (`refs/wip/<wt>-1445`) without touching the real index; workflows were resumed with a "RESUMED AFTER A CRASH" note added only to the unfinished agents (finished ones stayed cached).
   - **Don't use `git add -N` for snapshots:** it leaves intent-to-add entries.
2. **The NTA index signature mismatch:**
   - verified_at was signed as `...Z` but PostgREST returns `+00:00`, so every index row was rejected.
   - The index was truncated within an hour. 0 attempts happened in the window.
   - The fix 35a078e3 shipped with batch 3, and the index was rebuilt (653 rows, 0 failures).
   - **Lesson: test fakes must return the exact shapes Postgres and PostgREST return.** It is the same class of bug as the app's plainBody.
3. **Security:**
   - The public anon key could read the whole question bank: fixed by revoking it on production.
   - /api/leaderboard leaked students' names, ids and photos: hotfixed and live.
4. **The chrome-devtools MCP opened a visible Chrome** (the landing-perf agent). It was killed. **Every prompt must forbid it,** and the main session reaps `chrome-devtools-mcp` Chrome processes.
5. **Subagents cannot write report files** (the Write tool refuses "report" files for subagents). Ask for results in the returned text and save them from the journal (`mockmob-next/tmp/wave-results`, `tmp/resume-1017`).
6. **Usage limit hits kill whole workflows.** Check get_usage before waves; the 5-hour window resets about every 5 hours. Tonight's window resets at 4 am IST (22:30 UTC).
7. **The Flutter lock:**
   - a machine-wide override file `C:\Users\atish\AppData\Local\Temp\mockmob-flutter.lock.max` (number of slots) was added to `tool/flutter_locked.sh` in the app worktrees (uncommitted in some);
   - it is currently set to 2;
   - more slots thrash RAM.
8. **RAM** dipped to about 0 GB with an emulator, dev servers, Gradle and about 25 agents. Keep about 15 agents when the emulator runs.
9. **The Vercel Hobby plan keeps runtime logs for only 1 hour.** Check logs right after the owner tests.

---

## 7. How question work is done (the rules the owner insists on)

**Rules files:**
- `docs/brain/QUALITY.md`: the CUET-fit contract.
- `docs/brain/NTA-AGENT-RUBRIC.md`: 0-10 scores, blocking flags with caps, a difficulty check, a learning-objective tag, calibration.
- `data/nta_blueprints/*.json`: units, chapters, type quotas.
- the exemplar packs.
- `data/nta_agent_scores`, `data/nta_fit_scores`.
- `scripts/lib/authored-wave.mjs` and the publish scripts.

**NTA bar:** a mean of 2 judges of 8 or more (`NTA_MIN_SCORE = 8`), each judge at or above the calibrated 7. Any blocking flag, or both judges disagreeing with the key, excludes the question.

**Session-based pipeline (the owner likes it; it may become the default):**
1. a planner (SQL coverage against the blueprints);
2. authors in parallel;
3. 5 independent blind solvers;
4. 2 rubric judges and 3 fit judges;
5. the deterministic acceptance rule;
6. an expert pass and a re-solve of repaired rows;
7. the publish script (dry run, then apply).

He suggests stronger authors (Sonnet or Opus). Keep Haiku for the independent solvers.

**Bank re-validation (about 8,196 live questions):**
- Possible in sessions: 2 Sonnet judges per question, Opus on the roughly 15% of disputes, about 700 agent runs over 2-3 sessions.
- Or unattended with API credits via the Anthropic Batch API (roughly USD 50-100 a Sonnet pass). That needs his key, his OK for that content job, and a raised content budget guard.
- **Not decided. Don't start without his word.**

---

## 8. Owner items pending

1. **Hindi:** nothing needed now. If he finds a fluent reviewer, prepare a 20-question sample. Also open: is the 2026 CUET Hindi paper only reading comprehension and verbal ability?
2. **The Anthropic API key:** he will add it. Then switch runtime AI to Haiku 5.5 primary.
3. **Later (he said leave for now):** Razorpay TEST then LIVE; the Play account and upload key; SUPABASE_DB_URL plus PostgreSQL 17 for backups; PERSISTENT_LIMITS_ENABLED=true; Supabase leaked-password protection.
4. **Decisions not yet made:**
   - API credits for bank re-validation, or keep everything session-based;
   - the free first Repair (the adoption research suggests it; it is a pricing call, not built);
   - Today's sign-off questions (TODAY-1017 section 13).

---

## 9. Key facts

- **Supabase:** production `isrxrxzjocewrdureyhp`, staging `onwkqxmjqjrhfbjjdydu`.
- **Vercel:** project `prj_uSolddribHQDl1mM5AKxg3O9qCIu`, team `team_V5PhMz9hqV42vblUMcvhYqoN`.
- **Local web:** `npx next dev --webpack` and `npx next build --webpack`. node_modules is a junction to `mockmob-hotfix/node_modules`. Copy `.env.local` from `wt-batch2` into new worktrees (wt-batch4b has none).
- **Flutter:** `MOCKMOB_FLUTTER_SLOTS=2 bash tool/flutter_locked.sh`, unit tests with `-j 1`.
- **Rig:** `mockmob-next/tmp/rig-1016e/RIG-READY.md`. Use profile builds with `phone-relay.json` (debug hangs on a CircularDependencyError).
- **App walk screenshots:** `mockmob-next/tmp/app-walk-1017`.
- **Stall watcher:** `scratchpad/stallwatch.py` (WF_IDS env, `--once`).
- **Saved agent results:** `mockmob-next/tmp/wave-results/*.json`, `tmp/resume-1017/*.json`.
- **Worktrees:** about 100 exist. Clean up only after everything ships.

## 10. Document index

All paths are in `mockmob-next/docs`.

| Folder | Files |
|---|---|
| brain | HANDOFF-2026-10-17-NIGHT.md (this), NEXT-SESSION-PROMPT-2026-10-17.md |
| brain | OWNER-FEEDBACK-2026-10-17.md, FEATURE-ADOPTION-2026-10-17.md, SUBJECT-COVERAGE-2026-10-17.md, AI-COST-PER-USER-2026-10-17.md |
| brain | APP-OWNER-LEDGER-2026-10-16.md, HANDOFF-2026-10-16-NIGHT-FINAL.md, CTO-LOOP.md, HIGGSFIELD-IDEAS/PLAN/RESEARCH-2026-10-16.md |
| design-decisions/pass-1017 | NAV, RESULT, START, TODAY, GLASS |
| design-decisions/pass-1016e | APP-PASS.md, WEB-PASS.md, SOCIAL-SPEC.md (section 15 decisions), SOCIAL-APP-CONTRACT.json |
| design-decisions | app-ia-1016.md and the area briefs |
| research | premium-ux-ui-2026-10 |

---

## 13. EXACT STOP POINT (filled in at the safe stop)

(See below, appended by the main session at the stop.)

### Section 13, written at the stop (17 Oct about 3:55 am IST, usage at 96%)

All workflows were stopped on purpose. The emulator, the staging site and relay, the dev servers, headless Chrome, Gradle and Flutter testers were all killed (6.3 GB free after). Every interrupted worktree was committed as a "STOP POINT" commit. **Nothing is half-applied in production.** Live main is still **e192c59e**.

| Track | Worktree, branch | Head at the stop | Next, exactly |
|---|---|---|---|
| **A. Ship the website UX pass** | wt-ship17, deploy/ux-1017 | **42b0d75b** merges web/ux-social-1016 (94c172e6, verifier PASS) onto main e192c59e. On top sits 079e8338, a STOP POINT that only adds a stray `dev3250.log`: delete it in a commit. | The merge agent never finished its checks. Rerun lint, test:app/recovery/learning/auth/billing and `npx next build --webpack`, then smoke Today, Practice, a result, Review, Progress, /leaderboard ("Your standing" must survive) and Pricing at 390 and 1440, Night and Day. Then **push to main** and verify Vercel. |
| **B. Six website redesign packets** | none created yet (wt-p-* do not exist) | n/a | Launch them from deploy/ux-1017 **after A ships**, exactly as in section 4: result, start (with the server-side fine-tune scope, F12, F10), today, dock, mob split, retire 41 subjects. Then integrate, an Opus critic, an Opus fixer, a Sonnet verifier, push. Script to copy: `web-build-1017-wf_608e70c8-074.js` (path in section 4). |
| **C. Landing** | wt-land2, web/land2-1015 | **d483939d**, a STOP POINT holding the round-11 fixer's partial edits (21 files) over d6e1ad65 (round-10 fixes) | Critic r10 scored **74** (`mockmob-next/tmp/resume-1017/C_critic-r10.json`), with a truth defect: delayed fresh checks and the Score Recovery Lab are presented as live while `data/capabilities.js` blocks recovery. An Opus fixer reviews d483939d against the r10 defects, finishes, and removes "41 subjects". Then an Opus critic round 12; ship only at 88+. |
| **D. App v12** | wt-owner, ui/owner-1016 | **f5d848bf** (clean; includes the Business Studies briefcase) | Walk 1A done: 14 pass, 5 fail (L01, L03, L09, L13, L33; `tmp/resume-1017/D_walk-1A.json`, shots `tmp/app-walk-1017/1A`). Walk 1B never ran. Restart the rig (RIG-READY.md; the v12 profile build is already installed on the AVD), walk L16-L28, L30, L34-L39, fix all failures by area, re-walk, release v12. |
| **E. App UX pass integration** | wt-appux2, ui/ux-social-1016 | **2787be0a**, a STOP POINT with the integrator's partial edits (about 100 files) over dfd705b9 | A Sonnet integrator reviews the partial edits, then analyze, the full unit tests (-j 1) and goldens. Merge into ui/owner-1016 after v12, as the base for **v13**. |
| **F. App v13** (the owner's priority: "the app feels like the old app") | branch from ui/owner-1016 after D and E | n/a | Build from NAV A1 (refine the active-tab bubble), GLASS, RESULT, TODAY, START (app parts) and the Mob app side (SOCIAL-SPEC section 15). Keep the Practice cards' blue light and texture. Emulator walk against F1-F18 and L01-L39, then release. |
| **G. Content wave 3** | wt-wave3, content/wave3-1017 | **725c0e65** (clean) | Run the missing scoring steps listed in section 4 with session agents (Haiku solvers and judges; Sonnet expert pass), merge the scores, dry run, then apply the 8+ rows (owner already said yes for 8+). Keep Hindi off. |

**Also open:**
- the repair diagnostic log level and the "not_in_passage" trap label;
- the AGENTS.md USD 25 line;
- Review F17 (the saved repair plus the mock date on each mistake).
