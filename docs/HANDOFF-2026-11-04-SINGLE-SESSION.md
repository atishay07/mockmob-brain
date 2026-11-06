# Handoff, 4 Nov 2026, about 3 am IST: stopped at the owner's order (usage about 95%); the next session continues in ONE session

**His order (4 Nov ~2:55 am, verbatim):** "Usage is at 95% right now, so start stopping everything and then prepare handoff along with the prompt for the next session. Make sure that no work is lost anywhere, everything is recorded, and stop at a safe checkpoint with all the understandings and the findings that you have got until now and the work that you have done."

**Rules still in force:** one session only (parallel work through Workflow or Agent subagents, never other sessions); record his new words verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md before acting; NOW, ledger and STATUS updated at every stop. Newest decisions:
- **LK64 (3 Nov ~11:55 pm):** no prototype links or test builds for him. Ship the final web to www.mockmob.in after the full gate, and hand him one AAB he uploads straight to Play.
- **LK65:** commit everything.
- **LK66:** push to GitHub ("Push branches to GitHub").
- **LK67-LK76 (4 Nov ~2:05 am):** the home page hero and brand.

## 1. Live now: www.mockmob.in = main 5df0c1c72 (READY, no runtime errors)

- **Physics formula cards (dadc12807):** 1,090 to 1,403 cards (312 typeset), all 14 NCERT chapters, about 7.2 h. One card (superposition of forces) is set as two aligned rows (v3), so every one of the 312 lines fits 360 and 390 px phones (measured inside a real card back).
- **Web ship (55a1d2f63, then the STATUS time fix 5df0c1c72)**, branch web/1104-english:
  - the new Key card look (LK39/43/58): warm paper, a family-coloured header band, a ruled back, Night without a rim, a stack in runs, a bigger desktop stage (LK41)
  - the top-bar capsule (LK42)
  - the Up next module (LK59)
  - Find's four sets on Learn home (LK62/LK48)
  - brand desk-object icons (LK60)
  - the English rewrite on the web (LK61; table docs/brain/learn-1031/r7/E-ENGLISH.md, applied list E-APPLIED-WEB.md)
- **Gate:** 4,402 web tests, 23 failing, all pre-existing on main (authored_w2 13, mob_v3* 7, study_content 1, round5_completion 1, inventory_fingerprint 1); eslint clean; both builds pass. Turbopack must be built in wt-1101-content: it panics on a junctioned node_modules.
- **Known web follow-ups (not done):** row 89 ("Holding") needs a server label change; contractions in about 400 more lines outside Learn (Mob, payments, Today, profile).

## 2. App 1.0.20+18: release branch ui/1103-app-18 at 6079162d5 (worktree wt-1103-app-rel). NOT built, NOT walked

**What it contains, on top of 1.0.19+17 (06b65ff46, what he has):**
- ffe92518b, the stale "Sending your answers" fix (LK50)
- round 5 plus Explore as Practice's fourth door (LK51)
- the calmer Learn (LK52/53)
- ef7eb742b, tests tapping what a finger reaches
- d573644f7, the Learn goldens
- ui/1104-app-look: You's plan strip as one capsule (LK42) and BrandIcon desk objects (LK60)
- ui/1104-app-english: the English rewrite mirrored from the web (E-APPLIED-APP.md)
- ui/1104-app-cards: the web's Key card look

**Verified only per branch:** analyze clean; each branch's full suite showed only old golden drift (111-113: tools, onboarding, credits, account_sheet, rhythm, art_scenes, today, result, start_v13, a flaky billing pair, social v3 run R5/R6 which reads today's date). After the final merges, the learn2 golden conflicts were resolved by taking one side, so those goldens must be re-recorded and looked at.

**WIP branch wip/1104-app-settle-partial (cfa811f8b):** the settle agent was stopped mid-run. It holds partial golden re-records plus 3 small edits (learn2 run_parts.dart, stage_frame.dart, stage_paper.dart). Unverified: diff and judge before taking any of it.

**Bug review of the whole diff, done.** Six areas: sending strip, cards, English, top bar/icons, Explore/calm Learn, release safety. Twelve findings were traced as real by an independent tracer; none critical or high. Full traces and fix hints are in handoff-1104/WORKFLOW-PARTIAL-RESULTS-2026-11-04.md.
- release-safety-1: pubspec is still 1.0.19+17. Bump to 1.0.20+18 (`python -I tool/bump_version.py --name 1.0.20` or `build_release_aab.sh --bump --name 1.0.20`).
- MEDIUM, fix before the build:
  - english-parity-1: the coach line "Got it, in a few days" contradicts a Got it key that says "back in 3 weeks". Fix both web WORDS.coachRatings and app LearnWords.coachRatings so the line is true for every card, and redeploy the web.
  - explore-learn-calm-1: the Explore door stays on the first linked subject for the whole session. Treat the link as a one-shot (explore_screen.dart:114).
  - explore-learn-calm-2: a feed checkpoint says "8 of 16 done" but its Stop here end says "1 of 16". Use one count (feed_screen.dart:695).
  - sending-strip-1: when the settler settles a paper, the pinned "Sending Mock N" notification is never cleared (stale_submit_settler.dart:127).
  - cards-stage-run-2: the run's deck edges are 48 dp slabs that show behind the card on every flip. Draw whole sheets (run_parts.dart:582).
- LOW, fix if cheap:
  - english-parity-2: the Missed it sub-line is cut at 360 dp, text 1.3. Set _subLines from 3 to 4.
  - english-parity-3: the Last look end key says "Study again". It should say "Look again".
  - explore-learn-calm-3: after a resume, the stop sheet undercounts. Needs the server to send `reached`.
  - sending-strip-2: a past-window paper is closed on the phone's clock alone.
  - sending-strip-3: settling a stale draft hides a newer Resume.
  - cards-stage-run-1: a card front can't scroll and the band pushes prompts under the fade.

**Next steps, in order:**
1. Decide on the WIP branch.
2. Fix the 5 mediums and the cheap lows, each with a test, plus the web coachRatings line.
3. Re-record the merged learn2/practice/you goldens and open them.
4. Run the full suite against the known drift list.
5. Emulator walk:
   - AVD mockmob_budget, 2 GB
   - `source flutter_app/tool/walk_learn2.sh`: `l2_build pro returning`, `l2_prep`, `l2_theme`, `l2_font`, then `l2_build free new`
   - the demo reads Learn from the web preview on port 3452 (launch config app-walk-web)
   - walk Day and Night, and text 1.3 on the main screens
   - clean up afterwards: `adb emu kill`, `gradlew --stop`
6. Build the AAB:
   - `bash tool/build_release_aab.sh --bump --name 1.0.20 --sell`
   - copy key.properties from C:/Users/atish/MockMob-keys (never print or commit it) and dart_defines/prod.json from wt-1020-v16; remove both after the build
   - package in C:/Users/atish/Desktop/MockMob-build-18 with OWNER-STEPS.md and release notes, like MockMob-build-17
7. Push ui/1103-app-18 to GitHub.

The stopped workflow's script, with all 6 review prompts, the walk prompt and the fix prompts, can be reused:
C:/Users/atish/.claude/projects/C--Users-atish-Desktop-mockmob-copy/c5a8da45-5c74-46ba-abca-73f6160b75cd/workflows/scripts/app-1020-release-verify-wf_24f47ca0-fd6.js
Resume does not work across sessions. Write a fresh remaining-steps script: drop the review/verify phase (it is done) and keep settle, fix, walk and walk fix.

## 3. Home page (LK67-LK76): investigation partly done, nothing designed or built

His words are verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "4 Nov 2026, about 2:05 am". In short:
- the hero is not the same idea on phone and desktop: Mobi's tap and bubble feel weird on the phone, and desktop has no Mobi
- the Night hero has neon edges
- phone scroll: one gesture must be exactly one step at any speed, and the page lags
- the phone hero has no word of CUET or exams
- text walls
- the exam screen is too tall and must show the real MockMob screen, not NTA's
- a stronger brand: illustrations, typography hierarchy, consistent Mobi; keep the fonts and logo
- a Preparoo-level loader and typing line

His scores: 7/10 vs AI slop overall, Night 6/10.

**Done (saved in git under docs/brain/handoff-1104/home-research):**
- **ug.preparoo.app study** (preparoo/index.json is the map; source/splash.txt, typing.txt, scroll.txt; screenshots stay in wt-1104-web-polish/tmp/home-1104/preparoo):
  - their loader is a black panel painted at first paint
  - the wordmark and mascot lockup then zooms in: scale 0.85 to 1, opacity 0 to 1, 800 ms, cubic-bezier(0.16,1,0.3,1), waiting for the font and logo with a 300 ms fallback
  - the panel then lifts away (100vh to 0, translateY -20vh, 750 ms in-out-cubic) over a static hero
  - it shows 0.78 to 2.47 s on a cold phone load and 0.32 to 1.90 s on a warm visit
  - typing details are in source/typing.txt
- **The AI-slop checklist:** slop/slop-checklist.md, 40 checkable tells (colour C1-C12, type T1-T6, layout L1-L7, imagery I1-I3, motion M1-M7, copy W1-W5). Each has a code check, a screenshot check and the live page's current state with file:line, sources cited; also what owned brands do in dark mode, and the traps of lime on near-black. Live page shots (66 viewports) are in wt-1104-web-polish/tmp/home-1104/slop.

**Stopped mid-work (partial data saved):**
- **Live audit:** audit-partial/ holds the Night/Day neon inventories at 390 and 1440 (neon-*.json, neon-390-compare.txt), page and crop measures, gesture-390.json and herotime.json. Shots are in tmp/home-1104/audit.
- **Scroll forensics:** scroll-tools/ holds probe.mjs, summarize.mjs, prototype-one-gesture.html and v1-results-main.md. Its synthetic touch flicks never moved the held Lab section, so it is inconclusive: the probe may not drive the page's own handler. Re-check with real touch events.
- **Brand inventory:** partial shots only, in tmp/home-1104/brand.

**Not started:** three designs (brand-first, clarity-first, feel-first), three judges (owner fidelity, anti-slop and brand, feasibility and regression), the spec, the build. The script with all prompts:
C:/Users/atish/.claude/projects/C--Users-atish-Desktop-mockmob-copy/c5a8da45-5c74-46ba-abca-73f6160b75cd/workflows/scripts/home-hero-understand-design-wf_5f4c151f-e76.js
Rerun only audit, scroll and brand, feeding in the finished Preparoo and slop results, then design and judge.

**Building it:**
- Where: wt-1104-web-polish, branch web/1104-polish from main 5df0c1c72; launch config web-polish on port 3467.
- Gate: all web tests, eslint, both builds, a look at 390 and 1440 Night and Day, his L-001..L-045 checklist (WEB-OWNER-LEDGER-2026-10-17.md) with tests, and one gesture = one step locked by tests.
- Then push main and check the deploy.
- Never cut a section, animation or showcase. Mobile first. No glow, sheen, gradient text or blobs. Night subtle. Keep the fonts and logo B. Every claim true.

## 4. GitHub (LK66)

- **Pushed:** feat/app-and-web (this docs hub), web/1101-content, web/1031-learn-v2, codex/question-factory-release, and 437 `archive/<branch>` tags (every local branch that was not on GitHub). Tags start no Vercel build.
- **At this stop:** ui/1103-app-18 goes up as a branch, and the 1104 work branches (web/1104-english, web/1104-polish, ui/1104-app-look, ui/1104-app-english, ui/1104-app-cards, wip/1104-app-settle-partial) as archive tags.
- **Vercel is on Hobby:** 100 deployments a day, one build at a time. Never push hundreds of branches.
- **Not on GitHub:** archive/uncommitted-1104-main (610 MB snapshot of the old main checkout). The safety classifier blocked my push. His command (from any folder):
  `git -C "C:\Users\atish\Desktop\mockmob copy\mockmob-next" push origin archive/uncommitted-1104-main:refs/archive/uncommitted-1104-main`
- **Snapshot commits of 22 old worktrees exist locally** (and in the tags). Do not switch branches in the old main checkout ("mockmob copy/mockmob copy"), mockmob-phone, wt-rev-apptests, wt-rig-r11 or wt-rig-site: their files now live on the archive branches. Left out of the snapshots on purpose:
  - 61 raw OpenAI response JSONs with key-shaped strings
  - 66 generated files over 5 MB
  - offline batch logs
  - the nested repo artifacts/keyreview-release

## 5. Machine state at the stop

- No dev servers, no emulator, no workflows, no subagents running. tmp-devslots is empty (stale locks removed).
- **Possibly still alive:** the classifier blocked killing orphans. The home audit's probe (node probe.mjs, pid 600) and its puppeteer headless Chrome may still run until they finish; close them if they linger.
- **New worktrees tonight:** wt-1104-english-web, wt-1104-web-polish (both with a node_modules junction to wt-1103-web-cards: rmdir the junction before removing a worktree), wt-1104-app-look, wt-1104-app-english, wt-1104-app-cards.
- **Launch configs added:** ship-look (3466), app-walk-web (3452), web-polish (3467).

## 6. Waiting on the owner

1. Upload 1.0.20+18 once it is built (section 2).
2. Optional: run the 610 MB push command above.
3. Open from before:
   - LK36 content gaps (English reading-comprehension cards, Financial Markets 2022, Computerised Accounting)
   - Saved on phones (one tap, or inside Explore)
   - the app's switch labels "Practise | Papers | Learn | Explore"
   - Under LK64 the CTO may decide the last two himself.
