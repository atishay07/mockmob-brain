# MockMob handoff: 17 Oct 2026, about 7:25 pm IST (session 604ced81, Claude Opus 5.5 as CEO/CTO)

**Read this whole file first.** It is the single source of truth for the next session and replaces every earlier stop note. It extends:
- `HANDOFF-2026-10-17-MORNING.md`
- `HANDOFF-2026-10-17-NIGHT.md`: rules, decisions, question rules, key facts. Still valid where not changed here.

Also read:
- **`WEB-OWNER-LEDGER-2026-10-17.md`:** the owner's 145 website and landing requests, from his own messages.
- `OWNER-FEEDBACK-2026-10-17.md` (F1-F18).
- `FEATURE-ADOPTION-2026-10-17.md`.
- The design decisions in `docs/design-decisions/pass-1017`: NAV, GLASS, RESULT, START, TODAY and LEARN-REVIEW.
- The memory index, especially owner-feedback-1017 and agent-swarm-resource-hygiene.

Newest owner words win. Verify every agent claim against git and production.

---

## 1. THE GOAL (owner's words today, in order of priority)

1. **Website, priority one:** "I for sure need the website redesign checked. This time, I don't want anything missed. Check everything that I said I wanted in the website. For the past 2 or 3 days, I have been giving that feedback, but in every new build and redesign, things are not implemented. Everything should be implemented."
   - The acceptance list is `WEB-OWNER-LEDGER-2026-10-17.md`: W-001 to W-100 (website) and L-001 to L-045 (landing).
2. **New landing page,** with priority one: ship only at a two-critic mean of 88+ with no high defect and NO truth defect, and every L item passing.
3. **Then, within 4-5 hours:**
   - **The Mob** (the group study feature) in the app and the website: "10/10 only if execution is 10/10".
   - **App v13** with all his 17 Oct changes, walked on the emulator, then the APK in his hands.
4. **Quality over speed:** "Speed doesn't mean we have to compromise with quality... we can parallelly run tests and ensure everything is operating properly."
5. **Later:**
   - Learn and Review F15 on web and app.
   - Higgsfield scenes.
   - **No new question or content generation unless he asks in his current message** (standing rule, memory content-generation-only-on-ask).

---

## 2. HONEST PROGRESS against what was promised this morning (about 12:45-1 pm)

**What was promised, in his words:** "the website with the new landing page and all the many things which I explicitly mentioned... within the next 1 to 2 hours. Then the mob feature in the app and website, along with this version 13... in the next 4 to 5 hours."

**The timeline:** it is now about 7:25 pm, about 6½ hours later. **Most of it is not done.**

| Promise | Promised by | State now | Honest % |
|---|---|---|---|
| Website redesign release (six 17 Oct redesigns, F17, 41 subjects retired) | about 2 pm | **DONE AND LIVE** at about 2 pm (f725a422) | 100% of that release |
| "Nothing missed": every website request he ever made | about 3 pm | Audit done: **of 100 items on the live site, 37 pass, 49 partial, 11 fail, 3 not testable.** Fixers: start/practice/runner (df7cf860) and pricing/help/copy (2ee6deea) are DONE on branches, not merged or live. Result/review, today/progress and nav/dock/design are partial (STOP commits). Integration, re-verification and push are not done. | about 45% |
| New landing at 88+ | about 3 pm | **Not shipped.** Score history: 74 (r10), 83 and 78 (r12), 80 and 83 (r13; critic B's rerun 79). Round 14 fixed one-gesture-one-slide (the regression to the live behaviour), the one-button dock, all truth items and Mobi/reveal issues. Round 14 has NOT been scored. Still open: the What's-inside heading tier (L-030), type scale, the desktop held-stage band, thumbnails, the reel frame, the Lab header orphan. | about 75% |
| The Mob, web and app | about 5-6 pm | Go/no-go at 1:25 pm: NO-GO 6/10. The web/server fixer did two rounds (wt-mobfix 1f5d2f4a): privacy section, entry points, join pages, rate limits on successes only, MOB_FULL, kill switch, sharing on by default, start-one-join-any. **Not re-checked; app side not updated; not walked; not on production.** | about 45% |
| App v13 APK | about 5-6 pm | **Not delivered.** Walk 1 plus critic said 6/10, "clearly better than v12, not yet premium". The 15 fixers were cut off mid-edit. The repair agent ran about 3 h and never committed. Its work (366 files, including 329 regenerated goldens) is saved as STOP POINT 42510757, unverified. Still to do: the remaining fixes, Mob app, integrate, walk 2, critic, final fixes, walk 3, APK. | about 50% |
| Learn and Review F15 (bonus, started this afternoon) | not promised today | Design revised to 7.6/10 (8ce5464b). Web build: shared P-LR0 done; P-LR1 Review partly built (5d1969c7); P-LR2 and P-LR3 not done. | about 25% |

### Why it slipped (honest)
1. **12:19 pm:** the previous session (25ef3d95, the other account) hit its usage limit mid-work. 15 v13 fixers were cut off, uncommitted, in one shared tree, and it didn't compile.
2. **About 2 pm:** the owner stopped the agents to upgrade the PC to 32 GB of RAM. Agents were killed mid-work.
3. **Usage burned fast:** 12% to 87% between 5:10 and 6:40 pm with about 16 agents, giving a safe stop at 6:40 pm. Resumed at 7:20 pm; stopped again at 7:25 pm at the owner's request (95%).
4. **Process mistakes (mine):**
   - A message to a running workflow agent resumed a DUPLICATE copy (two landing fixers editing one tree).
   - Shared dev servers bloated to 6-11 GB.
   - A landing critic killed another critic's captures.
   - Parallel fixers in one tree with no commits (the 12:19 pm loss) repeated a known risk.
5. **The audit itself was right:** it proved the owner's complaint. More than half of his website asks were only partly or not implemented on the live site.

---

## 3. Everything the owner said today (chronological, his words, for zero context loss)

Times are IST.

1. **About 2:20 am,** while the emulator was running: the "Detected ADB" popup kept appearing.
   - Fixed: the emulator's registry settings `HKCU\Software\Android Open Source Project\Emulator\set` now hold autoFindAdb=false, adbPath, showAdbWarning=false.
2. **About 2:45 am:** "I closed ChatGPT, keep going".
3. **About 3:30 am:** "I just was watching the app in the emulator while it was testing, and it's just very bad right now. The homepage UI looks weird, the navbar changes, and many other things that I wanted to be implemented are not implemented." This is v12. **v12 was dropped; v13 only.**
4. **About 3:35 am:** "Does V13 have all the things that I wanted?... Is all that in V3, or is there some context issue here?... What have you done in this 60%?" He was answered with a coverage table (HANDOFF-2026-10-17-MORNING section 4).
5. **About 3:55 am:** "prepare a detailed handoff along with a proper prompt" (MORNING handoff).
6. **About 12:20 pm** (new account, after session 25ef3d95 hit its limit): "check the status of that session and check everything. Know if it is possible to continue safely, and give an honest answer". Audited; safe to continue.
7. **About 12:40 pm:** "continue here and be focused on completing all the tasks. Give me an update on how much of everything... has not been done."
8. **About 12:50 pm:** "Is it possible that at least the website with the new landing page and all the many things which I explicitly mentioned... plus the app with the final build... and the mock [Mob] feature: can all that be shipped in the next 1 to 2 hours?" Answered honestly: web release about 1 h; landing maybe; Mob maybe about 2 h; v13 about 4 h.
9. **About 1 pm:** "I for sure need the website redesign checked. This time, I don't want anything missed... For the past 2 or 3 days, I have been giving that feedback, but in every new build and redesign, things are not implemented... the new landing page: both of these should be the priority to be done within the next one [hour]. Then the other two things are the mob feature in the app and website, along with this version 13... in the next 4 to 5 hours only, but run workflows and agents according to the pace. Speed doesn't mean we have to compromise with quality."
10. **About 2 pm:** he stopped the running agents (the Mob fixer, the v13 repair, the landing fixer) to upgrade the RAM.
11. **About 3:50 pm:** "I have updated my RAM to 32 GB... unlimited RAM, unlimited usage, because usage resets in 40 minutes... Now I want everything that we discussed to be done right now with maximum speed, efficiency, and quality."
12. **About 7:15 pm:** "im here keep going ill tell you when to stop but dont waste time".
13. **About 7:20 pm:** "you can start stopping things now usage is at 95%... compile everything into an extremely detailed handoff... include every small detail... give me an update... 3 or 4 things that you were supposed to complete in the morning within the next 1 to 2 hours..." (this file).

**Standing rule from session 25ef3d95, about 10:25 am (his words):** "make this a standing instruction that generating questions or content is to be done whenever I say only, not automatically running these with every prompt."

---

## 4. Live in production now

- **mockmob.in = main f725a422.**
  - Pushed about 2:05 pm. Vercel dpl_4rRdQev4JoQkzyBrH9tZqaVmSdUU: READY, 0 runtime errors.
  - Smoke checks:
    - These return 200: /, /pricing, /help, /login, /today, /leaderboard, /api/subjects (38 subjects, none of the 4 dropped), /api/stats.
    - /api/leaderboard returns 401 signed out.
    - /practice is 404 by design (Practice is /test).
  - **What f725a422 contains:**
    - The motion/UX pass (c3b1e215, shipped about 4:45 am by session 25ef3d95).
    - The six 17 Oct website redesigns:
      - the result screen in layers with one next move, Repair's value before paying, and no sleepy Mobi;
      - Start with pressable modes, bigger logos, and fine-tune above Start with grouped searchable chapters;
      - **the fine-tune scope enforced on the server**: CHAPTERS_NOT_ALLOWED and DIFFICULTY_NOT_ALLOWED return 422;
      - the runner pick shows one box;
      - the Start key holds steady on scroll;
      - Today as "Up next";
      - the phone dock (aligned at 320-768);
      - the Mob free/Pro split, OFF;
      - "41 subjects" retired and the 4 dropped subjects hidden.
    - **Review F17:** a repaired mistake opens its saved repair free and is never charged twice (503 "Nothing was charged" on a failed lookup); paper and 12-hour time on every mistake.
    - The live fixes:
      - the repair log goes to stdout;
      - the trap label is fixed;
      - the AGENTS.md cost line is current.
    - Content waves 3 and 4 score tables, so both waves are NTA-eligible.
  - The independent verifier PASSED f725a422 with these suites:

    | Suite | Pass |
    |---|---|
    | app | 498 |
    | recovery | 415 |
    | learning | 343 |
    | auth | 109 |
    | billing | 118 |
    | nta | 188 |
    | today | 28 |
    | mob | 45 |
    | subjects | 20 |
    | authored-publish | 155 |
    | dock | 74 (with a server) |
    | build | pass |

  - Its low notes:
    - the Practice bar sub-line is clipped for Pro at 390;
    - "Quick practice" is ellipsised at 360;
    - "Repair first" ordering versus the list order;
    - a repaired row reads "Check it held", not "Repaired";
    - the dock Start key plus the page's lime key make 2 lime keys at 390, which is the CTO's A1 decision.
- **Production DB:**
  - study_goals.exam_date and mock_target exist.
  - Wave 3 is published (153: chemistry 48, GAT 56, physics 49) and wave 4 is published (200: maths 51, chemistry 42, GAT 39, biology 35, physics 33).
  - 112 questions at 7-7.9 are HELD (55 from wave 3, 57 from wave 4); the owner may allow them for practice only.
  - The **Mob migration is NOT on production.**
- The account deletion function (`account_deletion_run`) skips missing tables via to_regclass, so the extra mob_* deletion steps are safe.

---

## 5. EXACT STOP POINT per track (7:25 pm; START HERE)

Everything was stopped on purpose at 95% usage. Every dirty worktree was committed as "STOP POINT 17 Oct ~8 pm" or "~6:40 pm". All dev servers, the emulator, the staging site and relay, Flutter, Gradle and headless Chrome were killed. **Nothing is half-applied in production.**

**Resuming in a new session:**
- Run ids work only inside session 604ced81.
- A new session relaunches from the scripts copied into **`docs/brain/workflows-1017b/`**:
  - `web-owner-audit-1017-v2.js`
  - `landing-1017c-wf_ca07ec62-a9e.js`
  - `app-mob-1017c-wf_8c482620-5e1.js`
  - `web-learn-review-1017-wf_844baba2-693.js`
- Skip the stages that are done. Add a RESUME note to each unfinished agent naming its STOP POINT commit; it must review that commit, keep what is right and finish.
- Saved agent results: **`mockmob-next/tmp/resume-1017d/`**, which includes **`web-ledger-verify-results.json`** (all 100 website items with pass, partial or fail, evidence and suggested fix), the critics, and the fixer reports.

### Track W: website release 2 (owner ledger fixes); TOP PRIORITY
- **Base:** live f725a422 (wt-ship17 on deploy/web-1017; integrate into a new branch deploy/web-1017b there).
- **Audit result on live** (`tmp/resume-1017d/web-ledger-verify-results.json`):

  | Area | Pass | Partial | Fail | Not testable |
  |---|---|---|---|---|
  | start-practice-runner | 14 | 8 | 2 | - |
  | result-review-repair | 6 | 9 | 1 | - |
  | today-progress-colleges-account | 8 | 9 | 5 | 2 |
  | nav-dock-global-design | 8 | 17 | 3 | - |
  | pricing-help-copy-misc | 1 | 6 | 0 | 1 |

  - **Examples of misses:**
    - W-038: a mistake doesn't carry its paper and time in the list.
    - W-032: no retry before the key.
    - W-035: the Lab USP has no visible name.
    - W-040: Learn/Review not refined (needs F15).
    - W-093: disclaimer lines.
    - W-094: the unlimited-mocks line in onboarding.
    - W-097: no monthly price shown.
    - **W-098: the per-user AI caps are NOT enforced on the rival start and submit, and a repo migration disagrees with the owner's Rs 5 decision. This is a real cost/security item; verify it first.**
    - W-099: repeated content.
- **Fixer branches:**

  | Branch | Worktree | Head | State |
  |---|---|---|---|
  | web/fix-start-1017 | wt-fx-start | **df7cf860** | DONE: all 9 items fixed, checked |
  | web/fix-pricing-1017 | wt-fx-pricing | **2ee6deea** | DONE: W-093 to W-099. Read its report for W-098 |
  | web/fix-result-1017 | wt-fx-result | cc2de720 | STOP: partial |
  | web/fix-today-1017 | wt-fx-today | 2345ee9e | STOP: partial |
  | web/fix-nav-1017 | wt-fx-nav | fb73dccd | STOP: partial |

- **Mob web fixes:** branch web/mob-fix-1017 (wt-mobfix, 1f5d2f4a, two rounds). Merge it into release 2 only behind MOB_ENABLED (off) unless the Mob gate passes.
- **Learn and Review web:** branch web/learn-review-1017 (wt-lr17, 5d1969c7).
- **Next:**
  1. Finish result, today and nav (Opus) from their STOP commits.
  2. Integrate all five fix branches (plus mob-fix behind its flag) into deploy/web-1017b.
  3. Run the suites and the build.
  4. Re-verify every partial and failed item against the ledger, then run an independent final verifier.
  5. The main session pushes.
  6. Then repeat the audit on the new live build until all 100 pass.

### Track L: landing
- **Where:** wt-land2, branch web/land2-1015, **head 9e3ceab7**. Lineage:
  - 8683c5e5 (r11);
  - bf098d46 (STOP);
  - a9f0ec8d (r12: all 11 truth defects fixed);
  - **f128642b** (r14: one gesture = one step in held stories, restoring the live site's paging; storyGesture.mjs and scrollMotion.test.mjs; 0 harness fails at 390, 1440 and reduced motion);
  - **9e3ceab7** (r14 truth and visual: one-button dock by state, "Save your answers" removed, answered count in the close, no "not affiliated" FAQ or footer, "commerce papers first", pricing credit line, focus to the first chip, Mobi eyes fade in with the body, reveals armed after mount, statement contrast).
- **Landing tests:** 85 of 85 pass.
- **Still open from r13 and r14:**
  - the L-030 What's inside heading tier;
  - the desktop held-stage band;
  - the type scale (15 sizes; target 12 or fewer);
  - college thumbnail placeholders;
  - the reel frame in Night;
  - the Lab header orphan "questions" at 390.
  - It has not merged main since f725a422.
- **Next:**
  1. A two-critic panel (Opus, phone-first and truth-first) also checking L-001 to L-045.
  2. Fixer and panel until a mean of 88+ with no high or truth defect and every L item passing.
  3. A ship verifier: merge origin/main, suites, build, smoke.
  4. The main session pushes.
- **Critic method lesson:** a dev server on 3122 shared by both critics, started with `NODE_OPTIONS=--max-old-space-size=4096`. Theme for Night is localStorage `mm:theme:v1` = 'dark' exactly. Each critic stops only processes it started.

### Track A: app v13 (the owner's biggest pain)
- **Where:** wt-v13, branch ui/v13-1017, **head 42510757**: a STOP POINT holding the repair agent's unverified work (366 files, 329 of them regenerated goldens).
- **Lineage:**
  - 29abcf75 (last known good: v13 integrated plus the Mob app side; analyzer clean; 5,230 unit tests and 1,314 goldens at 96f04d82);
  - 792fc271 (STOP: the 15 fixers' half-edits; did not compile);
  - 8d7e7eba (STOP: the first repair's partial);
  - 42510757 (STOP: the second repair, about 3 h).
- **Acceptance list:**
  - walk 1 (`mockmob-next/tmp/resume-1017c/wf_e62f61a8-c85-walk-1.json`): 94 items, 22 fail;
  - the critic (`wf_e62f61a8-c85-critic.json`): 6/10, 25 defects, 6 high:
    - the Night bar near-opaque;
    - a muddy Day rim light;
    - no bounce at the bottom of Today;
    - 2+ volt fills per tab;
    - Today missing See why, Change length, and the paper and date in the why line;
    - the Something else sheet doesn't add up.
- **Next:**
  1. Check 42510757 (analyze, unit tests, goldens; OPEN the regenerated goldens, since 329 masters changed). Keep, finish or revert per area. Fall back to 29abcf75 per area if needed.
  2. Remaining area fixes, each in its own worktree with commits (never parallel fixers in one tree without commits).
  3. The Mob app side to the new server (adopt changes_1017: error codes, sharing on by default, durationSec 600, invitesPaused, the chapters endpoint, entry points).
  4. Integrate, bumping to 1.0.13.
  5. The rig (section 9), then walk 2 with screenshots and motion clips: F1-F18, L01-L39, the design checks, the 22 plus 25 items, and the Mob with two members.
  6. An Opus critic.
  7. Final fixes.
  8. Walk 3.
  9. Release the APK.
  10. Send it to the owner with honest notes.

### Track M: the Mob (web and app)
- **Web/server:** wt-mobfix web/mob-fix-1017 **1f5d2f4a** (0c57718f round 1, plus round 2).
  - **The CTO decisions applied:**
    - Free STARTS one Mob and JOINS any by invite; Pro starts up to 3.
    - Sharing inside a Mob is ON by default with a per-member opt-out.
    - Free members of a Pro-made Mob may sit its extras.
  - **Fixed:**
    - a privacy Mob section;
    - entries on Today, Review and Practice;
    - the no-Mob and /join redesign;
    - rate limits count only successes;
    - MOB_FULL;
    - the MOB_INVITES_ENABLED kill switch;
    - the lows;
    - thin-bank chapter extras.
  - Migrations are on STAGING only.
- **Next:**
  1. A full go/no-go re-check on staging, with at least three members and crafted requests (the previous check is checkpoint `handoffs/mockmob/20261017T075524.870648Z-b72dfd38.md`).
  2. The app side and an emulator walk with two members.
  3. **Switch-on, only at 10/10:**
     - apply `20261017100000_mob.sql` plus the sharing-default migration on production under the grant (pre-check, apply, post-check, STATUS);
     - Vercel MOB_ENABLED=true, PERSISTENT_LIMITS_ENABLED=true (after checking take_rate_limit exists), and MOB_ID_SECRET;
     - redeploy;
     - name a moderator.
  4. **Rollback:** unset MOB_ENABLED.

### Track F: Learn and Review F15
- **Design:** `docs/design-decisions/pass-1017/LEARN-REVIEW-1017.md` (8ce5464b, self-score 7.6), with mocks in `tmp/design-1017/learn-review`.
  - Cross-doc flag: TODAY and RESULT still ask the Start key to go quiet, against NAV A1; resolve in favour of A1.
- **Web build:** wt-lr17, web/learn-review-1017, **5d1969c7**.
  - P-LR0 (shared) is done: review_input.mjs, the fixture, the parity test, GET /api/me/review, and the revise_cards.mode migration on staging.
  - P-LR1 (Review) is partial.
  - P-LR2 (Revise) and P-LR3 (Concepts) are not started.
- **Next:** finish the packets, then a critic and a fixer; then the app packets P-LR4 to P-LR6 on top of v13.

---

## 6. CTO decisions made today (do not re-ask)

- **TODAY-1017 section 13, Q1-Q4:** yes to all.
- **The first Repair stays paid.** That is the owner's pricing call; not built.
- **Publishing:** questions publish only when the two-judge mean is 8+ AND the fit median is 8+; 7-7.9 are held.
- **v12 is dropped; v13 is the only next APK.**
- **The Mob:** Free starts one and joins any; Pro starts up to 3; sharing is on by default with an opt-out; Free members may sit a Pro Mob's extras.
- **Nav A1:** the Start key never changes look with page state, and the dock key plus one page volt is accepted.
- **The landing dock** is one state-aware button (owner's 15 Oct words, L-008). Earlier rounds' two keys were wrong.

---

## 7. Pending owner items

1. **The Anthropic API key:** then switch runtime AI to Haiku 5.5 primary.
2. **Avast:** an exception for the Claude app, because the TLS failures killed agents twice (about 3 am).
3. **Held questions:** 112 at 7-7.9 (keep for practice?).
4. **Hindi:** needs a fluent reviewer.
5. **The free first Repair** (pricing).
6. **The Physics syllabus call:** 7 Electronic Devices questions were dropped in wave 3 on an unconfirmed syllabus reading.
7. **Later, his words "leave for now":** Razorpay, Play, Supabase backups, PERSISTENT_LIMITS_ENABLED, leaked-password protection.
8. **API credits:** bank re-validation or session-only.

---

## 8. Incidents and lessons today (all in memory agent-swarm-resource-hygiene)

1. **About 3 am:** every agent died at once with "SSL certificate verification failed (UNABLE_TO_VERIFY_LEAF_SIGNATURE)". The likely cause is Avast's HTTPS scanning.
2. **Usage:** four big workflows burned 37% in 35 minutes. At about 16 agents the burn is about 50% an hour. Stage waves; check usage every 15-20 minutes; stop cleanly at 87-90%.
3. **Memory:**
   - Webpack `next dev` servers grow to 6-11 GB over an hour of sweeps.
   - Start shared ones with NODE_OPTIONS=--max-old-space-size=4096 and restart them between waves.
   - The commit limit is about 64-69 GB even with 32 GB of RAM (the page file auto-grows).
4. **Never SendMessage a running workflow agent by its id:** it resumes a DUPLICATE copy. This happened twice: two landing fixers and a second critic B.
5. **Agents must stop only processes they started** (match their own temp profile). A critic killed another critic's captures.
6. **Never run the installed Chrome directly:** a helper ran `chrome --version`, which opened a visible window on the owner's default profile for under 2 minutes. The owner was told.
7. **Never let parallel fixers share one tree without committing:** that is the 12:19 pm loss of 15 fixers' work.
8. **Subagents cannot write report-named files;** save their results from the workflow journals.
9. **The emulator's "Detected ADB" popup** is fixed in its registry settings.

---

## 9. Key facts

- **Supabase:** production isrxrxzjocewrdureyhp, staging onwkqxmjqjrhfbjjdydu.
- **Vercel:** project prj_uSolddribHQDl1mM5AKxg3O9qCIu, team team_V5PhMz9hqV42vblUMcvhYqoN. The site is www.mockmob.in (apex redirects 307).
- **Local web:**
  - `npx next dev --webpack -p <port>` (dev dist `.next-dev`); `npx next build --webpack` (`.next`).
  - node_modules is a junction to mockmob-hotfix/node_modules.
  - .env.local comes from wt-batch2.
- **Flutter:** `MOCKMOB_FLUTTER_SLOTS=2|3 bash tool/flutter_locked.sh`; unit tests with `-j 1|2`.
- **The rig** (`mockmob-next/tmp/rig-1016e/RIG-READY.md`):
  - **Staging site on 3101:** `stagingLocalApp.start.mjs` builds and starts with MOB_ENABLED=true. Run it with cwd at the branch to serve (wt-mobfix for the Mob; copy .env.staging from wt-rig-site).
  - **Relay on 3102:** from wt-batch, `scripts/dev/supabase-usb-relay.mjs`.
  - **Emulator:** AVD mockmob_budget, -memory 3072.
  - **Builds:** PROFILE builds with dart_defines/phone-relay.json.
  - **Test accounts:** app-e2e-student@example.com, plus the mobtest-{a..h,pro,u1..u6}@example.com staging members.
- **Ports used today:** 3122 landing, 3263 audit, 3271-3275 fixers, 3280 gate, 3291-3296 Learn and Review, 3264 Mob.
- **Worktrees of today:** wt-ship17, wt-audit17 (detached at f725a422), wt-fx-{start,result,today,nav,pricing}, wt-land2, wt-v13, wt-mobfix, wt-lr17. The older wt-v13-* packet worktrees are merged into wt-v13.
- **Brain docs of today:**
  - STOP-POINT-2026-10-17-0350.md and STOP-POINT-2026-10-17-1840.md (superseded by this file)
  - HANDOFF-2026-10-17-MORNING.md
  - WEB-OWNER-LEDGER-2026-10-17.md
  - pass-1017/LEARN-REVIEW-1017.md
- **The owner's raw messages, 12-17 Oct:** `mockmob-next/tmp/owner-corpus/` (286 messages, one file per day). Use them when in doubt about what he asked.

---

## 10. Recommended order for the next session (time estimates for parallel agents)

1. **Track W:**
   - Finish the 3 fixers; integrate the 5 branches.
   - Re-verify every partial and failed item; run the final verifier; push.
   - Then re-audit all 100 items on live and loop until all pass.
   - **About 2-3 h.**
2. **Track L:** panel, then the fix loop to 88 with every L item, then ship. **About 1½-3 h,** in parallel with W. 88 is not guaranteed.
3. **Track A:** verify the repair, fixes plus the Mob app, integrate, walk 2 plus the critic, fixes, walk 3, APK. **About 4-5 h.**
4. **Track M:** go/no-go on staging; if 10/10, switch on (production migration, Vercel flags), with the app in v13. **About 2 h** after the app side.
5. **Track F:** finish the web packets, then the app packets on v13.

**Waves:**
- at most about 8 heavy agents;
- dev servers capped;
- check usage every 15-20 minutes;
- stop at 87-90% with STOP commits and a handoff.
