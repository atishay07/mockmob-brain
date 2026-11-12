# UI audit log: what has already been looked at, and what was found

Living file. Started 12 Nov 2026 (about 9:45 pm IST) after the owner's words: "most of your time went to looking ... no other agent has to spend this kind of time looking and already finding the things which you have already found or which you think don't need to be changed ... Log all of this in the brain, keep it updated."

**Rule for every agent doing UI work on MockMob:** read this file before capturing or reading any screen. Do not re-walk a surface marked "seen, holds" unless code under it changed after the date shown (check `git log` for the files named). When you look at something, add what you found here, with the date, the commit and the sizes you looked at. A finding without those three is not a finding.

State this log describes: web `main a218cb9a4` (live, 13 Nov 2026; sections 2 and 3 were walked on 766eb6da9, section 2a on a218cb9a4), app `ui/1112-final c79dac51c` (version 1.0.23+21).

---

## 1. How to look, fast (do not rediscover this)

Web worktree: `C:/Users/atish/Desktop/mockmob copy/wt-1110-convert`. Tools: `tmp/1110-app/` (not shipped). Dev server: `preview_start {name: "convert-1110"}`, port 3571. Delete `.next` and `.next-dev` after a session.

| Need | Command (from `tmp/1110-app`, Git Bash; prefix `MSYS_NO_PATHCONV=1` when an argument is a lone `/`) |
|---|---|
| Whole public page as a reader scrolls it | `node strip.mjs <label> / 390x844 dark 760` then `python grid.py shots/<label> 390-dark 300 8 1` (contact sheets; about 2,200 tokens a sheet) |
| A page at given scroll positions after waits | `node at.mjs <label> / 390x844 dark 5320,6080 700,2500` |
| First visit, timed frames | `node first.mjs <label> 390x844 dark` |
| Signed-in pages (fixtures, no sign-in) | `node walk.mjs --label x --w 1440 --h 900 --theme dark --data ready --views today,dashboard,... --max 2` (a real desktop browser at 700 px and wider). Views: today, dashboard, mob, profile, review, learn2, learn2-chapter, cards, explore, saved, ranks, wallet, result, progress, radar, compass, prepos, revise, help, onboarding. Extra query with `--q`. |
| Where each page's title starts on desktop | `node edges.mjs 1440 today,mob,learn2,...` |
| Anything running past the right edge | `node probe.mjs 390x844 <y1,y2,...>` (local) or `probe-live.mjs ... x https://www.mockmob.in/` |
| Film frames | `node film-frames.mjs <label> /video/hero-v5-720.mp4 1.9` then `grid.py` |
| Side-by-side images | `python montage.py out.jpg <width> a.jpg b.jpg` |

Traps that cost time on 12 Nov:
- **Lab and tour scenes fill in over about 2 s.** A shot taken 0.7 s after a jump shows half-empty cards. That is not a defect. Wait 2.5 s before judging.
- **Count-up numbers** (questions, Key cards, subjects) differ between shots because they animate once. Not a truth problem.
- **The roaming Mobi** on the home page is in transit between sections after a jump; it has `pointer-events: none` and cannot block a tap.
- **Local price wording differs from production.** Locally the offer is "₹99 once, to 31 July 2027" (no `RAZORPAY_PLAN_ID_PRO_MONTHLY` locally); production says "₹99 a month". The film's "Pro ₹99 a month" matches production.
- **Production runs the newer Mob (the den, `MOB_V3_ENABLED` on).** The preview shows the older ring page unless the link has `&mob=den`. Judge the den.
- **The preview cannot open the test-taking screen** (`view=test` says the paper link expired; a launch from Practice does not complete). Not seen on desktop in this pass.
- **A first visit gets the Day theme**, whatever the phone's setting. Judge Day at least as carefully as Night.
- The time: run `date`. On 12 Nov my sense of elapsed time was an hour off.

App: `C:/Users/atish/Desktop/mockmob copy/wt-1108-app/flutter_app`. Method and tap coordinates: `wt-1108-app/tmp/1112-final/walk/WALK.md` (720x1600 emulator `mockmob_budget`: tabs at y 1465, Today x 101, Practice 225, Start 360, Mob 494, You 617; avatar 72,208; Ask Mobi 575,208). Shots: `tmp/1112-final/walk/` (117, demo build, Night and Day) and `tmp/1112-final/check/` (after shots; release build first run).
- **Debug builds of the real app stop on the opening screen** (Riverpod's debug-only `CircularDependencyError`: `AuthController._watchForRecovery` listens to `networkRestoredProvider`, whose `ConnectivityMonitor` depends through three providers on `AuthController`). Do not spend time on it in a walk. For the first-run flow use a **release** build signed with the upload key: it installs over the `in.mockmob.app` already on the emulator (same key) and opens at the welcome screen.
- The demo build (`test/device_demo/demo_main.dart`) is the way to see signed-in screens. Learn, Explore and Colleges show "didn't load" there (no local servers); the Mob shows "opens soon". Both are demo limits.
- Flutter tests run at about 8 a minute on this PC. Never plan to run the whole unit or golden folder; run the folders that cover the change.
- Onboarding reference renders exist for every step at four sizes and both themes: `test/golden/onboarding/goldens` (322 files). They are faithful; read them before asking for a device walk.

---

## 2. Home page (www.mockmob.in)

Looked at on 12 Nov 2026, commit 230de48e8 then 766eb6da9: 390x844 Night (28 screens), 360x740 Day (31), 1440x900 Night (25) and Day (24), a timed first visit at 390, /signup at 390 and 1440 in both themes, an overflow scan of the whole page at 390, and the live site's tour region at 390.

| Section | Verdict | Notes |
|---|---|---|
| Header (phone and desktop) | Seen, holds | At 360 the Pricing pill is hidden by design. |
| Hero copy, two keys, log-in line, creators line | Seen, holds. **Not changed** | First paint about 0.6 s on the local build; no splash delay. The owner removed a fact line from the hero (LK121), so do not add "Free. No card needed." there. The third headline line types and rotates by design. |
| Hero film player | Seen, holds. **Not changed** | Plays about 3 s after load. The "Sound on" key on the picture stays: the film is narrated (owner, round 12). **Weak point, open:** on a phone the film is about 350x197 px, so the phones and laptops inside it are hard to read; only its headlines carry. |
| Hero film content (r5, 53 s) | Seen frame by frame, truthful | "Pro ₹99 a month", "15 subjects, 19 of every 20 CUET papers", "Race up to four friends", "Unlimited with Pro" all match production. Its screens still match the product. Edits to the film are done by the main session only (owner, 12 Nov). |
| Feature strip under the film | Seen, holds | **Possible gain, open:** six stacked rows plus the price hook on a phone (about 600 px) push the "Try five CUET questions" sample to about 1,900 px down. |
| College strip | Seen, holds | |
| Sample ("Try five CUET questions") | Seen, holds | Subject switch and loading were redone 10 Nov (LK223). |
| Statement ("Your marks slipped somewhere") | Seen, holds | Scroll-scrubbed; the dim words are mid-scrub. |
| Mistake Lab, five scenes | Seen, holds | Every scene fills its card within about 2 s on phone and desktop. |
| Tour "More inside MockMob" | **Fixed 12 Nov** | The last slide (the Mob) ran 43 px past a 390 px screen: `.ft` had an implicit auto column. Now `grid-template-columns: minmax(0, 1fr)`; "Up next" reads the next section's `data-section-name` ("Key cards"). |
| Key cards, exam screen, DU Compass, DU courses, creators, pricing, FAQ, close, footer | Seen, holds | The creator cards' empty middle is where a reel preview loads. |
| /signup | Seen, holds (phone and desktop, both themes) | |
| /pricing, /refunds | Not re-walked 12 Nov | Reworked 10 Nov (LK212-LK214); only checked that they answer 200. |

Not looked at: tablet widths (768 to 1024), iPhone Safari, a physical phone, a screen reader.

### 2a. Home page motion (round 13, 13 Nov 2026, commit a218cb9a4; owner LK232-LK236)

**Every animation on the home page is inventoried in `wt-1110-convert/tmp/1113-motion/AUDIT.md`** (curves and durations in use, each section's animations with trigger, timing and file:line, 26 findings, the list of loops, and exactly what Mobi does on phones and desktop). Read that before touching any motion here; do not re-derive it.

Round 13's own rules are in one file, `src/app/r13-motion.css`, loaded last by `page.js`. Each block's comment says what it replaced.

| Thing | State after round 13 | Notes |
|---|---|---|
| Section reveals (`Reveal.jsx`, `.rv`) | **Changed** | Heads: 10 px rise, 320 ms, no blur (was a 6 px blur over 800 ms from 24 px). Blocks: 12 px, 300 ms. `threshold` 0 (was 0.12, which left a blank band under tall blocks on a flick). |
| Mistake Lab scene change | **Changed** | Out 120 ms, in 90 ms later over 220 ms (was a 420/550 ms crossfade with two scenes showing). The screens inside still take about 2 s to draw their rows (audit F19, owner's call, untouched). |
| Sample card taps | **Changed** | Press dips to 0.985; right answer swells 1.5 %, wrong shakes 3 px; no 3 px hop; the next question's stem and options rise 6 px in sequence. Mobi's bubble: old line out in 100 ms, new one in after 110 ms. |
| Sample result: "Ask Mobi what to do tonight" | **New** | `askMobiSample.mjs` (pure, tested). One step from the five answers, two follow-ups. No model, no network. Checked at 390 and 360, Day and Night, with 0, 3 and 5 misses. |
| Held stories' bottom bar (phones) | **New** | The logo's Mobi (18 px) on the current step, a hop per step (`SectionPosition.jsx` `.lp-bar__mobi`). |
| Desk scene in "Try five CUET questions" | **New** | Scroll-driven depth (CSS `animation-timeline`): room 1.08 to 1, Mobi 0.92 to 1, bubble last. Done at `contain 30%` on phones, at `entry 100%` from 1024 px. |
| Press states | **Added** | Tour chips, pricing subject steps, Compass keys, FAQ rows, shelf links, Wall pause, hero DU link. |
| Sticky hover on touch | **Fixed** | A tap no longer freezes the college rows or leaves the Compass demo key hovered. |
| Key card flip | **Changed** | 480 ms on the drawer curve (was 600 ms on a slow-start curve). |
| Phone menu | **Changed (site-wide, `nav-motion.css`)** | 260 ms an item, 25 ms apart: the sign-up keys land by 410 ms (were 640 ms). |
| Compass sweep | **Changed** | Renders in steps of 5 points (was a render nearly every frame). |
| Night phone dock | **Changed** | Blur 14 px, saturation 1.2 (was 20 px, 1.6). |
| Desktop lane Mobi | **Changed** | Fades over 160 ms when he hides or shows (was one frame). |
| Held stories' step and gesture logic, the hero film, the college marquees, seat hop-ins | **Untouched** | Owner-tuned; the audit lists facts only. |

Traps found:
- **A timed frame taken with Playwright is 50 to 100 ms later than its label** (the screenshot itself takes that long). Judge a 100 ms transition from several frames, not one.
- **A scroll-driven animation shows a half state in a still shot** taken while the stage is entering. Compare against where a reader rests, not mid-entry.
- The page's height differs between local and live by about 70 px in pricing (the local one-time offer wording). Section heights otherwise match; `tmp/1113-motion/heights.mjs <base>` prints them.

Tools added (`wt-1110-convert/tmp/1113-motion`, Git Bash): `node check.mjs <label> 390x844 light` (timed frames of a wrong pick, Next, a right pick and a Lab scene change, plus page errors, right-edge overflow and real-pointer hit tests); `node ask.mjs <label> 390x844 light 0,1,0,0,1` (plays the sample with those picks, opens Ask Mobi, taps each follow-up); `node reduced.mjs` (Reduce motion: every reveal visible and unmoved, the desk finished).

Open, from the audit, his call: seats appear at 55 % visible with an 880 ms hop (F18); Lab screens take about 2.4 s to draw (F19); the film's progress bar restyles every frame (F21, not measured).

---

## 3. Signed-in website (the arena)

Phone (390, 360): walked in depth on 10 and 11 Nov (LK199-LK224). On 12 Nov only an overflow scan at 360 Day across every view: clean (only decorative SVG parts of Mobi pass the edge, clipped by their own box).

Desktop, looked at on 12 Nov at 1440x900 (all views), 1366x768 and 1920x1080 (six views):

| Page | Verdict | Notes |
|---|---|---|
| Shell | Seen, holds | Content column is 960 px, left-aligned beside the 250 px rail by decision (R8 TOOLS-18, "one left edge"); at 1920 the column sits centred. Do not centre individual pages. |
| Today | Seen, holds | Two columns. Right column is narrow (about 270 px) at 1440. |
| Practice | Seen, holds | Two columns with a sticky summary. **Fixed:** the success toast at launch is gone. |
| Your papers, You, Marks trend, Colleges, Ask Mobi, Explore, Saved, Your standing, Revise | Seen, hold | Two columns where it makes sense. |
| Learn, Key cards | **Fixed 12 Nov** | Were centred (titles at x 317 and 352 against 252 everywhere else); now `margin-inline: 0 auto`. |
| Mob (the den) | **Fixed 12 Nov** | Members and settings side by side from 1100 px (`mob.css`, `:has`). The den scene itself uses the width well. |
| Wallet, Progress, practice result | Seen, acceptable. **Open candidates** | One 960 px column each. Not broken; a two-column desktop layout would be a real gain if desktop work is wanted. |
| Guide, Pro sheet, account pop-over | Not re-walked 12 Nov | Checked at 1440 on 10 and 11 Nov. |
| Test-taking screen | **Not seen** | See the trap above. The landing's exam section shows the same component. |

---

## 4. Android app (1.0.23+21)

Looked at on 12 Nov: 117 emulator shots of the demo build (Today to the bottom, Start sheet, Practice with its four sub-tabs, a Quick practice from setup to result, the repair flow, Mob, You, the account sheet and every row, Wallet, Ask Mobi, Colleges; Day for the main ones), the onboarding reference renders, and the release build's first run through the college step.

Holds, do not re-examine without a reason: Today, the Start sheet, Practice setup, the runner, the palette, the result, the repair flow, Papers, You, Wallet, Notifications, Theme and appearance, and every onboarding step.

Fixed 12 Nov (commits 1a7349291, c79dac51c):
- The band under the bottom bar closes (`BarScrim`: `underBar` 0.92, `underShare` 0.25, `atScreenBottom` 0.96). The see-through of the bar itself is unchanged (0.12 and 0.22): the owner likes the glass and content must show through it.
- Account sheet: "Credits" once, the balance lined up under it, no reserved empty line.
- Opening screen: a clear status tint, so the lamp light runs to the top.
- Welcome screen: clear system bars. `SystemUiOverlayStyle.light` and `.dark` carry an opaque black navigation bar; never use those presets in this app.
- The Privacy row opens a page titled Privacy.

Seen and left, with the reason:
- Practice result at rest: the "50% / 2" tally row is half hidden behind the fixed foot. It is the finish stage's own trade-off (a 24 dp fade exists); changing it needs a layout decision.
- Repair ending at rest: one line of the explainer is cut by the foot. Same cause.
- The submit page's back key is a round arrow while other pages use a "Back" pill: a pill would put two labels on one action ("Keep working").
- Back on a page opened from the account sheet closes the page and the sheet together. By design.
- Demo-only mismatches (Wallet 46 against 45 elsewhere, "54 mistakes" after a repair, "in Mock 1"): fixture limits listed in `flutter_app/docs/DEMO-BUILD.md`.

Old reference-image drift, not caused by this pass and not re-recorded: `credits` (10; they fail without the 12 Nov changes too), `core/start_v13 following_picked`, `art_scenes welcome` and `plan_seal_struck`, `today_resume` (date-dependent), `result card4_share`.

Not checked: a physical phone; a sign-in in the release build; the first-run flow after the college step on a device; the Mob, Learn and Key cards on a device (they need servers the demo does not have).

---

## 5. Open candidates for visible change (owner's to pick; none started)

1. A portrait cut of the hero film for phones. Owner, 12 Nov: "Not now". Do not raise it again unless he does.
2. The hero's first screen on a phone: mostly words and two keys, with the film cut off at the fold. A rework that shows the product above the fold.
3. The feature strip under the film on phones: tighten it so the sample comes up sooner.
4. Desktop layouts for Wallet, Progress and the practice result.
5. The app's result and repair-ending feet (the half-hidden row at rest).

Owner constraints that bound all of this: refine, do not rebuild (rejected restructures on 15, 17 and 18 Oct); nothing hidden or cut from the signed-in product without a reason told to him; one accent (volt) for the primary action; no facts or claims the code does not back; he judges on his phone.

---

## 6. Change log of this file

- 12 Nov 2026: created from the final pass (LK225-LK230).
- 13 Nov 2026: section 2a added (round 13, the home page's motion; LK232-LK236).
