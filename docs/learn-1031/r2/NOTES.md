# Round 2 notes (append only): requests across packets, deferred items, owner actions

## P1 Learn home and roadmap (web/1101-r2-home), 1 Nov 2026

Requests to other packets / the orchestrator (P1 did not edit these files):
- **P2 (learn.js end()):** pass `unseen: info.coverage.unseen` to `endOptions(...)` (around the `let opts = endOptions({` call). `data/learn/suggest.js` endOptions now takes `unseen`; with 3 or more the lead is `30 new cards left here` / key `Next 10 minutes here` and the next chapter follows as `Next chapter: <title>` (ruling 3). Without the field the old order stays, so nothing breaks before the merge.
- **P2 (run end):** a "Today's 10 minutes" run carries `start_state.today = { due }`; the end can say `Accountancy done for today.` from it (usefulness.md item 5).
- **P2 (end() level branch, usefulness.md item 11):** store the level pick as `start_state.levelPick = { subject, chapterKey, at }`; `data/learn/roadmap.js` already takes `levelPick` (the new student's position). P1 reads it once it is stored (one line in `subjectBody`: the newest ended level run's pick).
- **P3 or orchestrator:** `src/app/api/learn/covers/route.js` may pass `{ pure: true }` to `learnHttp` (a pure read: the rate limit then runs alongside, speed.md item 5a). Not done by P1 (Explore covers are P3's).
- **Dock badge (phone-clarity.md item 13, AppLayoutClient.jsx):** the badge already reads the shared `/api/learn/home` through `useLearnDue` (no change to AppLayoutClient was needed). Turning "8 due" into a dot is the shell's call (P3/P4).

Deferred / not done:
- **speed.md item 6a** (a `learn_question_index` table built by the 21:30 UTC cron) needs a migration: skipped per the packet. 6b is done (the pool pages are read in parallel once the count is known; the two managed-id columns together).
- **speed.md item 6c, owner action:** turn on Fluid compute for the Vercel project (instance reuse cuts cold starts). Not changed from an agent.
- **Final-weeks mode** (usefulness.md item 6): deferred by ruling 3 (CUET is in May 2027). Backlog.
- **Explore cover coverage line** (usefulness.md item 7, "12 of 53 cards seen" on each cover): P3's covers; the data is in `/api/learn/subject` rows (`progress`).
- `suggestions` stays in the /subject body for the app; Learn home no longer draws it (`home/Suggestions.jsx` removed).

## P2 (run, feed, ends), 1 Nov 2026 evening
- Touched outside the P2 list, one line each, for ruling 6 (a stopped run stays open to pick up today):
  - `src/components/learn2/api.js` `runEnd(id, { stop })` adds `?stop=1`.
  - `src/app/api/learn/runs/[id]/end/route.js` passes `stop` to `learn.end`.
  - `src/lib/server/learnPreview.js` line 193 passes `stop` in the preview router (P1 may add `/api/learn/home` next to it: merge by hand).
- `learn.end()` now returns `stopped`, `progress { of, seen, before }` (the chapter's cards seen, for the end's growing bar) and `chapter { key, title }`; Pro `options` is capped at 1 (an open mistake in this chapter first, "Fix 1 open mistake"). Free `options` unchanged.
- "Revise later" is the feed card's key. A question's key stays "Save": it bookmarks into Saved, not into Revise, so calling it "Revise later" would be untrue. Orchestrator: decide whether saved questions should join Revise (then rename), or keep Save.
- Deferred: the 1440 feed rail "Up next" stack (screens 19, last bullet); the two-part "Difference" line ordering (screens 6); the stem collapse to 2 lines (screens 6); the 40 px track lift after the first turn (screens 3; ruling 7 only asks for the peek and the chip).

## P3 (chapter page, Explore, tabs), 1 Nov 2026
- **Shared files P3 touched (merge with care):**
  - `src/lib/server/learn.js`: only `preview()` (adds `firstUp`, 5 lines before `return ok({`, and one field). No P1 or P2 function.
  - `src/lib/arenaNavigation.js`, `src/components/nav/PlaceTabs.jsx`, `src/app/(app)/nav-places.css`: the four-tab phone row.
  - `src/app/api/bookmarks/route.js`: a `?count=1` branch for Explore's "Saved 2".
  - `src/components/feed/QuestionCard.jsx`: a `closed` prop (stem first, "Answer it" opens the options).
  - `src/app/(app)/dashboard/DashboardPageClient.jsx`: Pro loses the "Included" tile badges and the head pill/sentence; the old
    lessons card (ConceptsPanel) is hidden while Learn v2 is on.
  - `src/app/(app)/saved/*`: "‹ Explore" back link, the one-time swipe cue in place of the swipe sentence.
  - Tests: `exploreModel.test.mjs` runs inside `test:learn` through an import at the end of `coverModel.test.mjs` (package.json
    left alone so three packets do not edit its one test line). The orchestrator may move it into `test:learn` directly.
- **Request to P1 (Learn home):** the old lessons card left Practice (a second Learn door). When a lesson is due, offer it as one
  of Learn's "Or" rows (for example "Revaluation of assets and liabilities, 7 min"). Until then lessons stay reachable from each
  chapter page's shelf ("Everything in this chapter").
- **Request to P1:** the chapter page shows only "Needs work" as a verdict (chapterModel `chapterVerdict`); the roadmap should
  use the same rule so the words agree.
- **Request to the orchestrator (dock badge, `AppLayoutClient.jsx`):** phone-clarity item 13 wants the dock's Practice badge
  ("8 due") as a dot too. P3 did not touch the dock (not in its list); the tab row's Papers count is now a dot.
- **Not done (left on purpose):** Fine-tune is drawn twice on Practice (the block and the strip above Start). phone-clarity 14
  says drop the strip, but the owner asked for it right above Start (F8), so it stays until he says otherwise.
- **Preview fixture (not P3's file):** `ArenaPreviewClient.jsx` answers GET `/api/bookmarks` with 2 saved questions for every
  student, so a brand-new student's Explore head reads "Saved 2" in the preview (90-explore-first-visit shots). Real accounts
  read their own count. A fix would return 0 for `student=new`.
- **Content call seen in "First up":** "What is partnership?" and "Define partnership." open the same run side by side (the
  near-duplicate pair still open in the owner's 1 Nov notes).
- **Shots:** `tmp/learn-1101/r2-after/p3/` (index.json lists each with its URL); script `scripts/design-audit/learn-1101-r2-p3-capture.mjs`.

## P4 Speed (web/1101-r2-speed), 1 Nov 2026

**Done:** speed.md items 1 (auth chain), 4 (`GET /api/today`), 7 (feed, part), 8 (CSS, part), 11 (`/api/stats`), 16 (summary user read in parallel), 17 (`published()` memo); ruling 12's Today check.

**Cross-packet edits (one line each; please keep on merge):**
- `src/app/page.js` (P5 owns the hero section): first line `import '@/app/marketing.css';`. The `.mm` system left `globals.css` and must load before `landing.css`.
- `src/app/preview/arena/ArenaPreviewClient.jsx` (P3 removes the `/api/learning/summary` fake there): adds a `/api/today` fixture and a brand-new-student Today fixture (`newOnToday`). `previewMob.js` also gets the new-student line.
- Any new public page or component that draws `.mm` or an `mm-*` class must `import '@/app/marketing.css'`. `data/tests/css_split.test.mjs` (in `test:app`) fails if one does not.

**Left for others or later:**
- Items 2 and 12 (`DiscoveryFeed.jsx`) belong to P3. Items 3, 5, 6 and 10 (`learn.js`, `learnHttp.js`, `learn2/api.js`) belong to P1.
- Item 7: `select('*')` stays. `readablePracticeQuestions` checks the signed `evidence` record of every row, so the wide columns are needed. A cheaper read needs a verdict index (`evidence_verdicts`), which is a separate packet.
- Item 8: app pages are now 400 to 516 KB of decoded CSS (from 468 to 557 KB), not 150 KB. What remains is Tailwind utilities from the whole tree (121 KB), `arena.css` (96 KB) and the page sheets. Getting lower needs a second Tailwind entry for the app, or splitting `arena.css` by page.
- Not started: item 9 (static app shell), item 13 (phone glass is a visual change and needs the owner's call), item 14 (lazy Mobi rig), item 15 (home main thread, with P5), item 18.
- Item 6c is an owner action: turn on Fluid compute in Vercel.

## P5 home hero (web/1101-r2-hero), 1 Nov 2026

Built hero.md items 1 to 16 except where noted. Shots: tmp/learn-1101/r2-after/hero/ (390 and 1440, Night and Day, first screen; 390 full page; taps 1, 4 and 6 at 390 Night and Day and 1440 Night; 360 x 640; 1024; answered sample at 390 and 1440; Reduce motion tap). The local dev server has no database, so /api/stats returns 503 and every shot shows the no-number fallback lines ("One live question bank. No cap on Pro.", "One big bank. A fresh mock every time."); locally the offer is the one-time plan, so the trust line is the long "No auto-renewal" variant and wraps to two lines at 390 (production's monthly line is one line).

Requests and open items for the orchestrator:
- The app twin: data/scene-anchors.json gained welcome.stars and welcome.sheetBubbles (the six measured bubble centres). The app's shared/scene-anchors.json should get the same bytes (the scene test compares them when wt-phase2 is present; it is not on this PC, so the test skipped).
- Not run: Lighthouse mobile on / and a `next build` chunk report (a production build in this worktree would have shared .next with the running dev server). Estimate: MobiReact and its rig modules minified and gzipped are about 28 KB including the 9.7 KB rig JSON (budget 35 KB). Band files: 780w avif 29 KB, 1170w 93 KB.
- Deviations: (1) the poster is Mobi's standing frame (act idle), not appear's first frame, because appear starts with his eyes shut and 10 units low; the appear rise is the poster's CSS entrance, and the rig takes over from the identical standing frame. (2) Celebrations Off follows MobiReact's shared rule (only the hop becomes the squash; hello, tilt and startle still play) instead of "only the squash"; vibration is off under Off. (3) 761 to 959 px (one column): the host's bubble is visually hidden (still the live region) because the stage's side margin has no room; the 900 px-tall hiding rule was not added. (4) Landscape phones are wider than 760 px, so they get the tablet host Mobi beside the stage, not a Mobi beside the H1. (5) Desktop column gap widened to 8.5 rem so Mobi and his 9 rem bubble live in the gutter and never touch the copy (the copy column is about 6% narrower; the proof row still ends at 843 px at 1440 x 900).
- Left in place: brand-pip.css still holds the old hero-seat rules (no element matches them now; landingMobi and release8 tests pin some of them); HeroMorph and HeroType still dispatch 'pip:glance', which nothing listens to now.
- Tests updated on purpose because they pinned the old hero: src/components/landing/heroScene.test.mjs (rewritten), src/components/landing/landingMobi.test.mjs (two tests replaced, one extended), src/components/scenes/sceneModel.test.mjs (file count +4), data/tests/release9_public_1018.test.mjs (the price line now reads heroTrustLine(priceLine(OFFER))).
