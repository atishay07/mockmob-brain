# MockMob handoff: 17 Oct 2026, about 4:00 am IST (session 604ced81, Claude Opus 5.5 as CEO/CTO)

**Read this whole file before acting.** It is the single source of truth for the next session, and it extends `HANDOFF-2026-10-17-NIGHT.md`. Read that one fully too: its sections 1, 2, 3, 5, 6, 7, 8, 9 and 10 (goal, owner rules, live state, design decisions, incidents, question rules, owner items, key facts, document index) still hold. **This file replaces its sections 4 and 13** (in flight, stop point).

Also read:
- `OWNER-FEEDBACK-2026-10-17.md` (F1-F18, his words);
- `FEATURE-ADOPTION-2026-10-17.md`;
- the five design decisions in `docs/design-decisions/pass-1017` (NAV, GLASS, RESULT, START, TODAY);
- `STOP-POINT-2026-10-17-0350.md` (the short form of section 5 below);
- the memory index `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\memory\MEMORY.md`, especially owner-feedback-1017 and agent-swarm-resource-hygiene.

Newest owner words win. Check every agent claim against git, production and the files before acting on it.

---

## 1. THE GOAL (unchanged, sharpened by the owner tonight)

**Ship a visibly new, clearly better MockMob on the website and the Android app, built from the owner's 17 Oct feedback and decisions, with every piece proven before he sees it.** A student must know what to do next, use the features, and feel the value of what they pay for.

**The app is the owner's biggest pain.**
- At about 2 am he told the previous session that the emulator testing "feels like the old app".
- At about 3:30 am he watched the v12 walk on the emulator and wrote: "it's just very bad right now. The homepage UI looks weird, the navbar changes, and many other things that I wanted to be implemented are not implemented."
- **v12 is dropped. v13, built from the 17 Oct designs, is the next and only APK.** It must look and feel new and premium (his references: HIGH, Revolut, Fampay; Apple's Liquid Glass).

**Done means:**
- **Website:** live after its gate.
- **App:** an APK in his hands after an emulator walk and a visual critique.
- **Reporting:** honest percentages and relative times, 12-hour clock.

---

## 2. What the owner said this session (his words, then what was done)

1. **About 2:40 am:** the emulator's "Detected ADB" warning kept popping up.
   - **Fixed:** the emulator's own settings, in `HKCU\Software\Android Open Source Project\Emulator\set`, now hold autoFindAdb = false, adbPath = `C:/Users/atish/AppData/Local/Android/Sdk/platform-tools/adb.exe` and showAdbWarning = false.
   - The emulator window still opens during walks; he may watch it.
2. **About 2:45 am:** "I closed ChatGPT, keep going". This freed RAM.
3. **About 3:30 am:** v12 is "very bad" (quoted above).
   - v12 walk 1B and the v12 release were cancelled.
   - v13 packets launched immediately.
4. **About 3:35 am:** "Does V13 have all the things that I wanted? ... Is all that in V13, or is there some context issue? ... What have you done in this 60%?"
   - **Answer given:** his 14 messages to session cc0bf1af (16 Oct 6 pm to 17 Oct 2 am IST) were checked against the ledger and the build plans; nothing was lost in the handover. The coverage table is section 4.
   - **One gap was found:** retiring "41 subjects" and hiding the 4 dropped subjects in the APP. Only the website had it; it is now in the v13 plan.
   - **One mistake was owned:** the main session followed the prompt's "finish v12 first" for about 50 minutes even though his 2 am remark already said v12 looked old.
5. **About 3:55 am:** "prepare a detailed handoff along with a proper prompt" (this file).

---

## 3. Incidents and lessons this session (new; add to the NIGHT handoff's section 6)

1. **API TLS failure at about 3:00 am.**
   - Every running agent (48) died at the same moment with "SSL certificate verification failed (UNABLE_TO_VERIFY_LEAF_SIGNATURE)" on the Claude API. The main session also needed "Try again" three times.
   - **Likely cause:** Avast's HTTPS scanning. `tmp/rig-1016e/RIG-READY.md` already records Avast re-signing Supabase's certificate on this PC.
   - **Told the owner:** an Avast Web Shield exception for the Claude app (or api.anthropic.com) should prevent it. That is his security setting; do not change it.
   - **Recovery:**
     - commit every worktree's partial work as a STOP POINT;
     - reap processes;
     - resume the workflows from cache with a RESUME note added only to the unfinished agents.
2. **Usage burst.**
   - 37% of the 5-hour window went in the first 35 minutes.
   - **Cause:** four workflows at once, including 130 Haiku scoring agents (about 14 M subagent tokens) and 8 website packets (4 Opus).
   - **The window lasted about 1 h 40 min of real work.**
   - **Rule:**
     - stage waves;
     - at most about 8 heavy agents (Opus or Sonnet high) at once;
     - check get_usage every 15-20 minutes;
     - stop cleanly at about 87-90%, and never let 100% kill agents.
3. **Memory commit.**
   - 8 Next dev servers (webpack dev uses 2-4 GB of commit each) plus the emulator rig pushed commit to 56 of 64 GB (the page file is capped at 48 GB).
   - **Rule:** at most 4 Next dev servers at once (the web script carries a DEV SERVER CAP note).
   - A watcher script is at `C:\Users\atish\AppData\Local\Temp\claude\...\604ced81...\scratchpad\ramwatch.ps1`. It alerts above 88% commit, below 15 GB free on C:, and on any visible chrome-devtools-mcp Chrome.
4. **The landing was paused** for RAM and usage (it is Opus-heavy: one fixer and two critics per round).
5. **Subagents still cannot write report-named files.** Saved agent results from this session are in `mockmob-next/tmp/resume-1017b/*.json`.

---

## 4. Does v13 contain everything the owner asked for? (coverage, checked against his messages)

| His ask | Where it is built |
|---|---|
| Nav A1: a glass capsule of 5 tabs plus a 64 dp round lime Start key; the Practice bubble must never cut into an icon | v13-nav (partial: 27 files) |
| Liquid glass at the app level; bounce instead of stretch | v13-nav (G1 bounce, G3 lens) and v13-glass (G2 material, G4 sheets, G5 floating controls, G6 accessibility) |
| Practice keeps its blue light and textured cards | A hard rule in every v13 prompt |
| Result screen: three layers, no sleepy Mobi, Repair's value before paying, submission shown once | v13-result (partial: 13 files) and website web/result-1017 (partial: 31 files) |
| Today: one "Up next"; not cluttered | v13-today (partial: 3 files) and website web/today-1017 (07d822c3 plus partial) |
| Fine-tune scope (Quick: chapters and difficulty; Full mock: difficulty; NTA and Smart: none) | v13-start (partial: 10 files); website web/start-1017, where the server enforces it on the session routes (6ffa128c plus partial) |
| F17: a repaired mistake opens its saved repair, never a paid one again; each mistake shows its paper, date and time | **Website DONE** (web/review-f17-1017 4298f1ff; the server never charges twice; 503 "Nothing was charged" on a failed lookup); app: v13-review (partial: 27 files) |
| Adoption (F18): one next move, receipts, first-week path, empty states that teach, features at their moment | Today, result and review packets (web and app) |
| The Mob: open to everyone (no age gate); Free vs Pro per SOCIAL-SPEC section 15; first week free sample; off until 10/10 | Website web/mob-split-1017 (partial); app: a Mob stage after v13 integration |
| Website Start menu (F4-F8, F10, F12) and dock (F13) | web/start-1017, web/dock-1017 (partial) |
| Retire "41 subjects"; hide the 4 dropped subjects | **Website DONE** (web/subjects-claim-1017 533e32cc, reviewed: `data/subject_claim.js`, `/api/subjects` hides them, profile save refuses them, explore and feed return 422). **App: NOT yet; add it to v13.** The landing owns its own lines. |
| AI at most Rs 5 per paid user; only gpt-6-luna and claude-haiku-5-5 | Live since 16 Oct night |
| Questions follow every wave 1-2 rule; publish only 8+; Hindi off | Wave 3: see section 5, track G |
| Learn and Review refinement (F15) | Not started (after the website and v13) |
| Higgsfield landing and onboarding scenes | Not started (after F15) |
| Switch runtime AI to Haiku 5.5 when he adds the Anthropic key | Waiting on him |
| Session-based question farm; bank re-validation with API credits | His decision, open |

---

## 5. EXACT STOP POINT (17 Oct about 3:50 am IST; START HERE)

All workflows were stopped on purpose at **87%** usage; the window resets at about 6:50 am IST. Every dev server, the emulator rig, the Flutter testers, Gradle and headless Chrome were killed (7 GB free after). Every worktree's partial work is committed as a "STOP POINT" commit. **Production is still main e192c59e. Nothing new is live. Nothing is half-applied in production.**

The workflow scripts of this session are copied into **`mockmob-next/docs/brain/workflows-1017/`**:
- `web-1017b.js`
- `landing-1017.js`
- `app-v13-1017.js`
- `content-w3-1017.js`

**Resume by run id works only inside session 604ced81.** A new session must relaunch them as new workflows: copy the prompts and add a RESUME note to each unfinished agent saying which STOP POINT commits hold its earlier partial work, and that it must review them, keep what is right, finish, and verify everything.

### Track A: ship the website motion/UX pass
- **Where:** wt-ship17, branch deploy/ux-1017, HEAD **7e26abc3**.
- **History:**
  - 42b0d75b merges web/ux-social-1016 (verifier PASS on its own base) onto main e192c59e;
  - e5c4952e removes the stray log and ignores *.log;
  - 5e41b296: the moderation Mob reports list makes no request while MOB_ENABLED is unset;
  - 7e26abc3 is a STOP POINT (1 file).
- **Stopped at:** the ship verifier was killed twice before it finished its checks.
- **Next:**
  1. Run lint, test:app, test:recovery, test:learning, test:auth, test:billing and `npx next build --webpack`.
  2. Prove that no page queries mob tables while MOB_ENABLED is off (the Mob migration is NOT on production).
  3. Smoke Today, Practice, a result, Review, Progress, /leaderboard ("Your standing"), Pricing and Help at 390 and 1440, Night and Day.
  4. Push with the PUSH protocol in `web-1017b.js`, then verify Vercel READY and the runtime errors.

### Track B: the website redesign packets (all from base 42b0d75b)

| Packet | Branch, worktree | State |
|---|---|---|
| live fixes | web/live-fixes-1017, wt-p-fixes | **DONE** da626be6: the repair diagnostic goes to stdout, the trap label is fixed, the AGENTS.md cost line is current |
| review F17 | web/review-f17-1017, wt-p-review | **DONE** 4298f1ff (self-verified; details in `tmp/resume-1017b/wf_38d2793c-f36-build_review17.json`) |
| subject claim | web/subjects-claim-1017, wt-p-copy41 | **DONE** 533e32cc (reviewed by the resumed agent, no change needed; report in `tmp/resume-1017b/wf_38d2793c-f36-build_copy41.json`) |
| result | web/result-1017, wt-p-result | Partial, 4190b065 (31 files, fixtures for weak, avg, strong, all_repaired, held, late_night, zero_credits) |
| start | web/start-1017, wt-p-start | 6ffa128c (fine-tune scope on the session routes) plus STOP POINTs 58e05acb and 951666a4 |
| today | web/today-1017, wt-p-today | 07d822c3 (Up next, This week, road strip, two rows, the road on the account, P0) plus STOP POINTs b3657e99 and cab8161a |
| dock | web/dock-1017, wt-p-dock | dfd0c121 (the More sheet opens Learn, Practice gets a Concepts panel) and 088ff733 (the session dock shares widths; clearance and pointer tests pending) |
| mob split | web/mob-split-1017, wt-p-mob | Partial, STOP POINTs 6beb8d4d and b0322f75 |

**Next:**
1. Finish result, start, today, dock and mob (Opus for result, start, today, dock; Sonnet for mob), each reviewing its STOP POINTs first.
2. Integrate all 8 into deploy/web-1017 on top of the shipped Track A head.
3. Run the gate: an Opus critic, an Opus fixer, then a Sonnet verifier, twice if needed.
4. Push. The Today migration (exam date and mock target) may be applied under the grant if it was dry-run on staging and has an undo. **Never the Mob migration.**

### Track C: Landing
- **Where:** wt-land2, branch web/land2-1015, HEAD **94b4081e**. That is a STOP POINT with the round-11 fixer's second partial pass (16 files), over d483939d (the first partial) over d6e1ad65 (round 10).
- **Score history:** 76, 82, 84, 87, 88, 85, 84, 80, 74. It oscillates, because fixers break other sections.
- **The r10 defects:** `tmp/resume-1017/C_critic-r10.json`, including the truth defect (Score Recovery and delayed fresh checks shown as live while `data/capabilities.js` blocks them).
- **Next:** relaunch `landing-1017.js`:
  - a fixer reviews 94b4081e against the r10 defects, retires "41 subjects" and fixes the truth defect;
  - then the two-critic panel (one leads with the 390 phone, one with truth plus 1440 and motion);
  - ship only at a mean of 88+ with no high or truth defect;
  - up to 3 rounds, then a verifier and a push.
- Run it when usage and RAM allow (it is Opus-heavy).

### Track D: App v13 (the owner's top priority)
- **Packets,** each in its own worktree from **f5d848bf** (v12's last good commit; later STOP POINT commits on ui/owner-1016 are superseded):

  | Packet | Worktree, branch | STOP POINT |
  |---|---|---|
  | nav | wt-v13-nav, ui/v13-nav | 070d5df3 (27 files) |
  | glass | wt-v13-glass, ui/v13-glass | aae2d834 (6 files) |
  | result | wt-v13-result, ui/v13-result | 68f63c11 (13 files) |
  | today | wt-v13-today, ui/v13-today | 244b3271 (3 files) |
  | start | wt-v13-start, ui/v13-start | d0b7334b (10 files) |
  | review | wt-v13-review, ui/v13-review | 0494d417 (27 files) |

  All are partial and unchecked.
- **The UX-pass integrator** (wt-appux2, ui/ux-social-1016 at 2787be0a, a STOP POINT with about 100 files of an older integrator's unchecked edits) was started three times and never got far enough to commit. **It must run first or alongside**, because the v13 integrator builds on ui/ux-social-1016.
- **Next (script `app-v13-1017.js`):**
  1. The UX-pass integrator: analyze, the full unit tests (-j 1) and goldens on wt-appux2. In parallel, the six packets resume from their STOP POINTs.
  2. **Add the app subject claim to the start or integrate brief:** retire "41 subjects" in app copy and hide entrepreneurship, teaching_aptitude, legal_studies and engineering_graphics in app pickers (the server already hides them once the website ships).
  3. The v13 integrator: create wt-v13 on ui/v13-1017 from ui/ux-social-1016, merge f5d848bf, then each packet. Where the UX pass and a packet touch the same screen, the 17 Oct packet's structure and look win; keep the motion helpers and the Mob. Bump to 1.0.13.
  4. The Mob app side (SOCIAL-SPEC section 15).
  5. Walk 1 on the emulator: F1-F18, L01-L39, the design acceptance checks, motion clips, Night and Day, 1.3 font. The site on 3101 must run the newest main for the Today fields; apply the Today migration on STAGING only.
  6. **An Opus visual critic** judges the screenshots against the mocks in `tmp/design-1017` and the owner's taste. It scores "feels new" out of 10.
  7. Fixers by area (Opus for nav, glass, today, result, practice, mobi).
  8. Walk 2.
  9. Release v13: merge into ui/phase2 and feat/app-and-web, the release build per HANDOFF-2026-10-15-FULL section 5, and save `tmp/apk/mockmob-v13-<sha>.apk` plus a zip.
  10. **Send it to the owner only after the walk and the critic, with honest notes on anything still failing.**

### Track E: Content wave 3 (GAT, Physics, Chemistry; Hindi off)
- **Where:** wt-wave3, branch content/wave3-1017, HEAD **2babd2a2**.
- **Done:**
  - **Scoring layout:** 5705cabc, wave-2 layout in `wt-wave3/tmp/authored-w3s`, 13 batches.
  - **Scoring:** 245 questions with 5 blind Haiku solvers, 2 rubric judges and 3 fit judges each (130 role files).
  - **Acceptance:** 57bc1baa. `scripts/authored-w2-accept.mjs --wave=w3`, plus 16 new tests in `data/tests/authored_w3_accept.test.mjs`. **219 of 245 accepted; 211 pass the engine's content gates.**
  - **Expert passes:**

    | Subject | Commit | Reviewed | Ready | Repaired | Dropped |
    |---|---|---|---|---|---|
    | GAT | 2babd2a2 | 83 | 53 | 30 | 0 |
    | Physics | 7b81787a | 67 | 42 | 17 | 8 |
    | Chemistry | 602f5381 | 69 | 24 | 42 | 3 |

    - **Physics:** 4 repairs changed solver-visible text; 7 drops are Electronic Devices items (Zener, solar cell, logic gates, filter ripple, LED) judged outside the 2026 syllabus. **That syllabus call is NOT confirmed against the NTA PDF: check it before dropping.**
  - Reports are in `tmp/resume-1017b/wf_acdb5b99-5e4-*.json`.
- **Known test note:** `test:authored-publish` has 1 failure ("merging wave 2 again reproduces the committed tables byte for byte"). The agent says it fails on untouched code too, from CRLF line endings in this Windows checkout. Verify.
- **Next:**
  1. Build the re-solve set: every expert-repaired row whose solver-visible text changed. Run 3 blind Haiku re-solvers (2 of 3 on the key, else hold the row back).
  2. Reword the engine-refused non-Hindi rows and give them a full fresh pass: 5 solvers, 2 judges, 3 fit judges.
  3. The final acceptance (the wave-2 final mode generalised for w3).
  4. **The owner's rule:** publish only rows with a two-judge mean of 8 or more AND a fit median of 8 or more; list 7-7.9 rows as held.
  5. Run `authored-scores-merge.mjs --mode=merge`, then `--mode=check`, then the suites.
  6. A publish dry run against production (select-only, `--expect-project=isrxrxzjocewrdureyhp`).
  7. Then the main session applies the 8+ set under the grant (the owner already said yes for 8+) and adds a STATUS entry.

### Not started
- Learn and Review F15 (design pass, then build).
- The Higgsfield idea loop (`HIGGSFIELD-IDEAS-2026-10-16.md`, "How to keep iterating").
- Hindi (waits for a fluent human reviewer).

---

## 6. Recommended order and staging for the next session (usage-aware)

**Check get_usage first.** With a fresh window, about 100% lasts roughly 1.5-2 hours at full burn with about 15 agents. Plan in waves.

**Wave 1** (about 8 heavy agents):
- Track A ship verify (Sonnet);
- the 5 unfinished website packets (4 Opus, 1 Sonnet);
- the UX-pass integrator (Sonnet);
- the content continuation (Sonnet coordinator plus a few Haiku re-solvers).

**Wave 2** (as wave 1 agents finish):
- the six v13 packets (4 Opus, 2 Sonnet);
- the website integrate and gate.

**Wave 3:**
- the v13 integrate, Mob, walk, critic, fixes, walk 2, release;
- the landing when there is room;
- apply wave 3.

**Stops:** at about 87-90% usage, stop everything cleanly (STOP POINT commits, reap processes, a checkpoint), then resume after the reset.

**RAM:**
- at most 4 Next dev servers;
- one emulator walk at a time;
- Flutter through the lock with 2 slots;
- reap between waves;
- the RAM rule in every prompt;
- never the chrome-devtools MCP or a visible browser.

---

## 7. Owner items pending (unchanged unless noted)

1. **The Anthropic API key:** he will add it. Then switch runtime AI to Haiku 5.5 primary with Luna fallback.
2. **Avast:** an exception for the Claude app, so the TLS failure does not recur (new; his setting).
3. **Hindi:** a fluent reviewer, and whether the 2026 Hindi paper is only reading comprehension and verbal ability.
4. **Free first Repair:** a pricing call; not built.
5. **Later, his words "leave for now":** Razorpay, Play, Supabase backups (SUPABASE_DB_URL, PostgreSQL 17), PERSISTENT_LIMITS_ENABLED, leaked-password protection.
6. **API credits:** whether to spend them on bank re-validation or keep everything session-based.
