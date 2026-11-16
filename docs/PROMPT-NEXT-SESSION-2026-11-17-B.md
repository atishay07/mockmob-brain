# Prompt for the next session (written 17 Nov 2026, about 3:25 am IST, Opus orchestrator; the owner is asleep for 5-6 hours)

Paste everything below the line into a new session.

---

Continue the MockMob pass from where the 17 Nov night session stopped at the owner's usage limit. You have 5-6 hours while
the owner sleeps: keep building, testing and shipping until the list is done; do not stop to ask; ship when it passes.

**First:** call continuum_start with project "mockmob". Then read, in this order: this file
(C:\Users\atish\mockmob-brain\docs\PROMPT-NEXT-SESSION-2026-11-17-B.md); NOW.md's top section; OWNER-MASTER-LEDGER.md
LK290-LK301 (his words whole, below too); UI-AUDIT-LOG.md sections 1, 2c, 2d; and the research reports in
`C:\Users\atish\Desktop\mockmob copy\wt-1110-convert\tmp\1117\understand\<tour|daily|streak-nta|opening|app>\FULL.md`.

**Rules for this run (owner's, 17 Nov):**
- NO Fable agents (the Fable limit was hit at 2:27 am; resets 9:30 am IST, but do not use Fable in this run). Opus agents are
  allowed when they are truly useful; otherwise do the work in your own context. Always pass `effort` explicitly
  (`C:\Users\atish\Desktop\AI OS\context\agent-model-routing.md`): Opus xhigh for reviews, money, data, NTA saving; Opus high
  for well-specified builds. Keep to about 2-3 agents at once; one session only (never start_session).
- Check usage before every wave; stop cleanly with a handover before a limit, never mid-change.
- Production database writes are blocked for agents: any SQL goes to the owner as a file plus an exact undo.
- RAM rule: at most one dev server and one headless Chrome per agent; emulator at most 2-3 GB; reap processes after.
- The owner judges on his phone. Walk with real touch swipes at 390x844 (Day and Night), 360, and 1440.

## His words tonight, whole (17 Nov ~1:15 am; ledger LK290-LK301)

> I'll tell you right now what works and what doesn't.
> * Coming onto the morning side [More inside MockMob], that section is still not good. From the ones that you have made, I would say that the previous version, in which you had just spread everything vertically, was the first. That old one was better than this. Though that was not perfect in any sense or good, it was better than this. You have to think about how you can better implement all this. I am just leaving it hanging.
> * Overall, in the above card of this, there's a weird shadow that got off, so just make it soft and diffused. Keep a focus on the overall visual hierarchy of everything and how the flow is working.
> * This Asmobi thing [bring-a-mistake block], I would say you have depicted all this quite perfectly. This daily 5 and Sunday mock is also depicted quite well. I would just say, if we could do something different, like what Prepium is doing, because this is exactly their version copied. If you see that they don't do it this way. What they do is they have all this in a daily challenges section, and they have stuff like English daily 017 number. If you see the website and try to attempt it, what they have done is identify yourself and choose your team to appear on the leaderboard. There are some athletes' names, jersey numbers, and all this. This is just gamification of stuff. I don't know if this is good or not, but it could be something useful in general. I'm thinking in that direction and building something unique from them. What I'm saying is, what works and what's good is the UI and how you have made it look and be understandable: that part is good.
> And there were many new generations of Mobi and 3D assets and image generations in the last session but I don't see any changes to that. I don't know if it hasn't been committed or if there is some other issue.
> The working is good now. Overall, I like the look better. Dot canceling too, but it's good. It's directing the credit also as it should. You have added, I think, some kind of soft blur to the page, which I also really like and which feels good. [Ask Mobi chat]
> Also after this, what you have to focus on is improvising the streak system and refining [our] NTA mode and stuff like that. Overall making the website just feel very fluid and smooth is also very important. It's pretty good right now but still just make it as good as we can.
> Just one thing: the loading animation while opening the website is still not good at all and needs to be improvised. It should be grand in the phase, with even some animation falling through it after loading the page. Once the page is loaded and the animation has gone up, you can merge it into the MockMob logo at the top and animate the logo a little bit, of some sort. Just think about it.
> Finally, coming onto the app: build everything in the app and send me the final version. Whatever you build, it should be up to date with all the progress that we have made and the most complete product possible. This is our final build for the app also.
> Just confirm one thing for me: if the web app feature is available on iOS, is it just an extension of the website that saves the information? Or is it a full-fledged, proper app experience, like the haptics and multiple other things that can be done only in the app? Does it do all of those things? If yes, we'll build that also.

Already answered to him (do not redo): the Mobi art was never lost (`wt-1110-convert/tmp/1116-art`); the iPhone Home Screen
web app is the website in its own window (full screen, offline, push only once on the Home Screen; no haptics: Safari never
shipped the Vibration API and the switch trick reportedly broke in iOS 26.5; no App Store, widgets or background work); a
full iPhone app means compiling the Flutter app for iOS (Apple Developer account USD 99/yr, a Mac or a paid cloud Mac build
service, Apple in-app purchase for Pro). That is HIS decision; do not start iOS. The site already has a standalone manifest
and an Apple touch icon (installs to /today).

## State at the stop (17 Nov ~3:25 am)

LIVE: www.mockmob.in = main **3511f1fb3** (`dpl_B6tTXUhhhHnV5s4fnisHLvfxAQMp`). Nothing from tonight is live.

**Web release branch `web/1117-prod`** in `C:\Users\atish\Desktop\mockmob copy\wt-1110-convert`, head **007f01059**, local only,
NOT gated, NOT pushed. It holds all six web lanes merged cleanly plus the calendar Mobi on the daily head; 564 merged tests
passed (landing, daily, streak, NTA saving). The lanes (each `wt-1117-<lane>`, branch `web/1117-<lane>`, from 3511f1fb3):
1. **tour** (36a1ba841, mine): on touch the tour is a deck: five still tabs over cards the browser scrolls sideways (one card
   a swipe, next card peeking), never held; 969 px at 390 (was 2,839); desktop unchanged. Soft shadows: the Lab's last screen
   (was clipped by content-visibility), tour screens, sample card; a sweep finds no shadow past its section. Tests rewritten.
2. **opening** (945ae3d67, mine): "answer sheet rain": wordmark min(88vw,960px) on the page's own ground (no dark flash),
   bubbles/rows/tiles falling at three depths, a bubble inks Mobi's eye, curtain rises while the word FLIPs onto the bar logo
   (lands within 4 px), then the logo settles (dot drops, Mobi hops and blinks). First visit lands 1,200 ms, still by 1,500;
   session 800/1,100. Keys v2. Tests rewritten (opening.test.mjs, L-043 to LK299). Seen on the dev server at 390 Day and Night;
   desktop mid-flight not captured (dev server released late); check the timings on production frames.
3. **art** (2db3e8e2d, mine on Fable's partial): one 3D Mobi finish everywhere (the vector pose sprite left the page; the desk's
   live rig stays): magnifier (Lab), camera (bring-a-mistake, new pose), reading (exam), pointing (Compass, DU), attentive
   (pricing), wave with six real frames (close), calendar (daily, added at merge). Companion 3D at 56 px, never covers words.
4. **streak** (Opus): one humane daily streak everywhere (Today block, top-bar OMR bubble, You, sheet with 7 days, passes,
   milestones, pause); Daily Five and repairs count (JS merge, no SQL); GET /api/me/streak + POST/DELETE /api/me/streak/pause;
   bug 6 fixed; streakDays removed. Its independent review ran and a fix pass was MID-WORK when stopped: the partial fix is
   WIP commit **28fa1045a** on web/1117-streak (16 files, unreviewed) and is NOT in web/1117-prod yet.
5. **nta** (Opus): instructions page before the clock, exam-true saving (only Save & Next / Mark for Review & Next save),
   one question at a time in NTA style, NTA Exam Summary, opens in NTA style by default, no warnings counter, mirror shapes,
   steady clock; 16 saving tests. Its review was running; no findings received.
6. **daily** (Opus): Daily Five as a college game: "Playing for" a DU college (sheet: My colleges first, search all 67, or none;
   first pick and first change free, then once a week), seat number on an admit-card style card (signed in), college board
   (today by players, week by days, Sunday by average marks; floors; honest empty state), yesterday's trap, edition names
   ("Tuesday's five, 17 Nov"), share "Playing for ...". No new SQL (the college rides on the Daily Five rows); GET
   /api/daily/board public, cached, aggregate; /api/daily/me adds team and seat. Its review never started.

**App lanes** (Flutter, `wt-1108-app` repo, from `ui/1112-final` c79dac51c = 1.0.23+21):
- `wt-1117-app-ask` / `ui/1117-ask`: Ask Mobi as a chat with the Photo key; WIP commit **9769a2114** (122 files, unfinished,
  unreviewed, untested).
- `wt-1117-app-daily` / `ui/1117-daily`: Daily Five, Sunday Mock, Practice's weekend line, badges; WIP **26f90da01** (121 files,
  unfinished, unreviewed, untested).
- App wave 2 brief is written, not started: `wt-1110-convert/tmp/1117/briefs/app-wave2.md` (3D art, the one streak, NTA twin).

Briefs: `wt-1110-convert/tmp/1117/briefs/*.md`; lane rules `tmp/1117/LANE-COMMON.md`, `APP-COMMON.md`; lane script
`tmp/1117/mk-lanes.ps1`. Capture tools: `wt-1110-convert/tmp/1116-final/` (swipe.mjs, walk.mjs, sec.mjs, mc-audit.mjs, taps.mjs)
and `wt-1117-tour/tmp/lane-tools/deck.mjs` (sideways deck test), `wt-1117-opening/tmp/cap.mjs` + `sheet.py` (opening frames).
Shadow sweep: copy the logic described in UI-AUDIT-LOG 2d (an element's box-shadow reaching past its section's bottom).
Dev server: `preview_start {name:"convert-1110"}` (port 3571, wt-1110-convert). In Git Bash, `MSYS_NO_PATHCONV=1` before a lone
`/` argument; write file content with Write/Edit, not heredocs with apostrophes.

## What to do, in order (5-6 hours)

1. **Finish the reviews (Opus xhigh, independent, one per lane; or do them yourself):** daily (privacy for 16-17 year olds,
   cheating, floors, the team-change rule, the board API, Bearer auth), NTA (every path an answer could be lost or saved twice,
   drafts/offline/resume, the timer), streak (look at WIP 28fa1045a: finish or drop each change; IST boundaries, the pass cap,
   no-Mob students), and a quick independent look at tour/opening/art (mine, unreviewed). Fix what is right; merge the fixes
   into web/1117-prod.
2. **Merged walk** of web/1117-prod at 390x844 Day with real swipes (whole page), Night, 360, 1440: the deck (sideways and
   vertical swipes, tab taps), every 3D seat, the daily game (pick a college, play, board states via fixtures), Today's streak
   block and the top-bar bubble (preview arena fixtures), NTA mode in the runner (instructions, saving, summary), the opening
   frame by frame (first and session, Day and Night; cap.mjs). Companion audit 0 covering; shadow sweep none; no overflow.
3. **Fluid and smooth (LK298):** after the merges, on a QUIET machine (no other agents, no builds), bench the home page scroll
   and the runner at 4x CPU; fix long frames and layout shift you find; verify the opening never delays LCP.
4. **Gate** in `C:\Users\atish\Desktop\mockmob copy\wt-1116-next` (real Next 16.3.8): recapture
   `data/tests/fixtures/home-elements.json` first (`scripts/capture-home-elements.mjs` with PLAYWRIGHT_CORE and CHROME set;
   its opening key is now v2), `git checkout --detach <sha>`, `bash tmp/gate2.sh`, read every line of tmp/gate2.log (24
   suites, eslint, webpack and Turbopack builds), and also run the touched tests outside the gate (landing, daily, streak,
   NTA, opening). Then `git push origin web/1117-prod web/1117-prod:main` (fast-forward from 3511f1fb3), wait for the Vercel
   production build (project prj_uSolddribHQDl1mM5AKxg3O9qCIu, team team_V5PhMz9hqV42vblUMcvhYqoN), check live: 12 public
   pages 200, /mentor signed out to login, POST /api/ai/mentor/mistake 401, /api/daily/board 200 and aggregate only,
   /api/me/streak 401 signed out, the opening on production frames (first and session), the deck by touch, runtime errors.
5. **The app, final build (LK300):** finish ui/1117-ask and ui/1117-daily from their WIP (build, test folders, goldens looked
   at), review each (Opus xhigh), merge both into `ui/1117-final`, then run app wave 2 (art, streak, NTA; brief above) and add
   the daily college game (GET /api/daily/board, team and seat from /api/daily/me) to the app's Daily Five. Version
   **1.0.24+22**. Release build in a CLEAN detached worktree (memory: release-build-own-worktree): key.properties from
   C:\Users\atish\MockMob-keys and prod.json in, deleted after; `bash tool/build_release_aab.sh --bump --sell`; the arm64 APK
   separately; signer SHA-256 62:AC:58:08...EC:47; `python -I tool/check_16kb.py`; emulator walk on `mockmob_budget` (2-3 GB,
   release build for first run; demo build for signed-in screens) with screenshots of every new screen against his words;
   outputs to `C:\Users\atish\Desktop\MockMob-build-22` (AAB, APK, symbols, README.txt, OWNER-STEPS.md incl. the Play Data
   safety form: Photos used, not stored). Never print or commit secrets. Send him the folder path (SendUserFile for the APK
   only if it fits).
6. **Records:** NOW.md, ledger LK290-LK301 statuses, UI-AUDIT-LOG (a 2e for this pass), PRODUCTION-PASS row and rollback
   point, a continuum checkpoint. Remove merged lane worktrees only after `cmd /c rmdir` on each node_modules junction.
7. **Tell him plainly**, against each of LK290-LK301: what is live, what the app build contains, what was not checked (a real
   phone, iPhone Safari, signed-in production flows, a real model reply), and the open decisions below.

## Open decisions that stay his (do not decide)
- iOS app (account, Mac or cloud builds, Apple in-app purchase).
- An evening streak reminder in the app (the notification copy rule forbids streak nudges today).
- Class leagues SQL (20261116150000_class_leagues.sql) and the earlier open SQL in NOW.md's 16 Nov morning section.
- Stale 6 Nov doc copies in mockmob-brain/docs/_from-code-repo/mockmob-next/ (deletion was blocked for the agent).

## The longer vision (use the hours well, after the list above is shipped)
MockMob is CUET practice for 16-17 year olds, many new to apps and computer-based tests; the owner judges on his phone and
wants it to feel premium (HIGH, Revolut, Fampay level), calm, alive, and MockMob's own, never a rival's look. His standing
direction: features over audits, visible change over timing tweaks, bold branded blocks over safe thin ones, nothing that
moves by itself, honest numbers only, one left edge, soft shadows, plain words. When the list is done and time remains:
- Make the daily college game feel alive day after day: the trap of the day once the crowd floor is met, a weekly "most
  consistent campus" moment, a share card in MockMob's own admit-card style.
- Take the 3D Mobi further where it helps: one-shot sprite reactions (camera snap, magnifier sweep, calendar page turn) only
  if frames match the character sheet exactly; Mobi in the app's empty and success states.
- Fluidity everywhere a student spends time: the runner, Today, Learn, the Mob; zero layout shift, no long frames.
- Fresh-account truth: a brand-new student must find every feature without being told (audience rule).
- Keep the records current as you go; checkpoint before any limit.
