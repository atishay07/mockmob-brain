## 13 Nov 2026 (about 1:35 am IST) — round 14: guest Ask Mobi (real model calls), the phone companion, the visual pass: web live

- Live: main 38a09a4e7 (was a218cb9a4; rollback dpl_A8w9FmNKKAMmeJnknspWD5LHjuFY). New public route `POST /api/mobi/guest`, a paid model behind the runtime reservation (no user) and three database limits; worst case ₹0.13 a visitor, about ₹42 a day site-wide. Kill switch `GUEST_MOBI_ENABLED=false`.
- Verified: test:app 1,065, landing files 280, dock 62, du 43, keycards-ui 40, auth 141, billing 455, subjects 62, today 146, learn 440, AI cap tests 26 (0 failures each); eslint clean; next build --webpack 115/115; Vercel preview READY before the first push to main. On www: a real guest question answered by curl and in the sheet at 390; the fourth-question limit was exercised on the dev server, not on production.
- Unresolved: no physical phone, iPhone Safari or screen reader; the last two small commits (limiter option, Escape) reached main after a local build only; `ai_cap_route_coverage` now lists the guest route as a declared user-less caller (the CTO should know); guest replies can state CUET facts wrongly.

## 13 Nov 2026 (about 12:15 am IST) — round 13: the home page's motion, Mobi on the scroll, Ask Mobi on the sample: web live

- Live: main a218cb9a4 (dpl_A8w9FmNKKAMmeJnknspWD5LHjuFY READY, aliased to www.mockmob.in); was 766eb6da9 (rollback dpl_CKT48CAQJP3fESpAJbLWEaPiu2KD). The app is unchanged (1.0.23+21).
- Verified: test:app 1,043, landing files 271, dock 62, du 43, keycards-ui 40, auth 141, billing 455, subjects 62, today 146, learn 440 (0 failures each); eslint clean on page.js, components/landing and NavBar; next build --webpack 115/115; Vercel preview dpl_7WUXyyZBz5gqCkUWXCjjsBG4fz9L READY before main. On www after the deploy, headless Chrome at 390 x 844: a wrong pick, Next, a right pick and a Lab scene change with 0 page errors, nothing past the right edge, real-pointer hits on an option and Skip; Ask Mobi opened and both follow-ups answered; / /pricing /signup /login answer 200; no runtime errors in the hour.
- Unresolved: no physical phone, no iPhone Safari (the desk's scroll depth needs CSS view timelines; other browsers show the plain scene), no screen reader, no tablet width. test:mob and test:study were not run (their old failures are unrelated). A typed Mobi for guests is not built: it needs the owner's decision on a guest AI budget (LK236).

## 12 Nov 2026 (about 9:20 pm IST) — final pass: web live, app 1.0.23+21 built

- Live: main 766eb6da9 (dpl_CKT48CAQJP3fESpAJbLWEaPiu2KD); was 230de48e8. App: 1.0.23+21, c79dac51c on ui/1112-final, Desktop/MockMob-build-21.
- Verified: web suites and build as in NOW.md (0 new failures; test:mob keeps its 7 old server-side failures); live checks on www. App: Checked: flutter analyze clean; unit folders account_sheet, core/router, core_ui, credits, a11y, you, today (1,460), test/widget (365) and the welcome tests (74) pass; 130 reference images re-recorded and their suites pass (324); the bundle and the APK carry the upload key (SHA-256 62:AC:58:08...EC:47) and pass the 16 KB check; on the emulator, the signed-in screens in the demo build (Night and Day) and the release build itself, installed over version 16: opening screen, welcome, the class, course and college steps.
- Unresolved: no physical phone, no iPhone Safari, no signed-in production pages; the desktop test-taking screen not seen in this pass. App: a physical phone; a sign-in in the release build; the first-run flow after the college step on a device; the whole unit and golden folders in one run (old drift remains in the credits, start sheet, art scenes, today_resume and share-card reference images; the credits ones fail without these changes too). Debug builds of the real app stop on the opening screen (provider cycle caught by a debug-only check; release unaffected).

## 11 Nov 2026 (about 1:29 am IST) — the guide and web onboarding live

- Live: main 230de48e8 (was 97192a222). Verified: landing gate 572 (0 fail), app 1,035, dock 63, du 43, keycards-ui 40, auth 141, billing 455, subjects 62, today 146, guide and onboarding 57; eslint clean; next build --webpack 115/115; preview READY before main.
- Unresolved: no physical phone, iPhone Safari or signed-in production check; the auto-start is per device; Wallet selling closed.

## 11 Nov 2026, 12:15 am IST — Guide design ready for review (LK221)

- Design only. Production remains on 97192a222. No product files changed for LK221.
- Prototype uses the local first-day Today fixture. All 18 target and card placements are disjoint. Back, Next, Done, Skip, Escape and focus return passed. Owner design review and a durable account-scoped first-visit claim are open. Web onboarding is queued after the guide.

## 11 Nov 2026, 12:09 am IST — Wallet history and states live (LK217)

- Main 97192a222. Preview dpl_C3TRpKniUKHWaptWRRaHbvdj9Re1 was READY before production dpl_F82HMuFKG2eyZKrAhANwQjSHaWDz, which owns www.mockmob.in.
- Billing 455/455, targeted 78/78, release gate and ESLint clean, webpack 115/115. Local Chromium verified Wallet states and a stubbed confirmed purchase with one activity entry and balance refresh retry.
- Selling is closed. A Razorpay Test Mode purchase on an isolated preview and the owner’s decision are pending. Pack refund clawback remains open.

## 10 Nov 2026, 11:47 pm IST — Home sample loading and selection live (LK223)

- Main 4461487f5. Preview dpl_J2A4f3UubAH8qqpgMQtonzZxq9Jx was READY before the production push. Production dpl_59Cqzg4r6E3GeTYmWsMQrG85zqvH is READY and owns www.mockmob.in.
- Existing publication and answer checks stay in place. The selection prefers stored quality, coverage across chapters and authenticated provenance. The read-only Accountancy check returned 30 eligible questions from 12 chapters with zero signed past-paper labels. No question content was edited.
- Landing 548/572 (12 skipped, 12 todo), app 1033/1035 (2 skipped), dock 62/63 (1 skipped), DU 43/43, Key cards UI 40/40, auth 141/141, billing 453/453, subjects 62/62. Zero release-gate failures, ESLint clean, webpack 115/115.
- Local Chromium verified 360, 390 and 1440 in Night and Day. Signed-out production Chromium at 390 verified the sample with intercepted requests. The 15-minute Vercel check found no runtime errors on the selected routes.
- LK217 remaining Wallet states, LK221 guide design and LK216 onboarding are open.

## 10 Nov 2026, 11:19 pm IST — You and Mob profile live (LK219)

- Main 755dd31fe. Vercel preview dpl_3zm4AwRiDpZLXFuxifVdWF81ccYo was READY before the production push. Production dpl_8Q2DatvUNcU9NukxFBm2kQCxHVX2 is READY and owns www.mockmob.in.
- The card leads with the account name and initial. Add a subject is beside Edit subjects. Monthly credit breakdown remains in Wallet and Credits. The current Mob's identity is read from the existing GET action in read-only mode. Saving uses the existing PATCH.
- Landing 546/570 (12 skipped, 12 todo), app 1033/1035 (2 skipped), dock 62/63 (1 skipped), DU 43/43, Key cards UI 40/40, auth 141/141, billing 453/453, subjects 62/62. Zero failures in the release gate. ESLint clean, webpack 115/115. Mob suite 345/352 with the same seven documented server failures.
- Verified in local Chromium at 390 × 844 and 360 × 740 with one through five subjects, Free and Pro, Night and Day, and at 1440 × 900 in both themes. Mob edits were tested against fixtures, including validation, save and focus return. No physical phone, iPhone Safari or signed-in production check.
- LK223, the remaining LK217 Wallet states, LK221 guide design and LK216 onboarding are open.

## 10 Nov 2026, 10:55 pm IST — Pro sheet refinement live (LK218)

- Main da4555622. Preview dpl_GyFKeaiqZQuTT2VN2jmcNdaWPG9F READY; production dpl_AZYV4RFeYUpTEZuyYN9RJ56bv8rX READY and www.mockmob.in resolved to it.
- The triggered feature and a desk object lead the sheet. The existing benefits, pricing and terms remain. Get Pro and Not now stay in view while details can scroll.
- Gate: targeted 71/71, landing 546/570 (12 skipped, 12 todo), app 1032/1034 (2 skipped), dock 62/63 (1 skipped), DU 43/43, Key cards UI 40/40, auth 141/141, billing 453/453, subjects 62/62. Zero failures, ESLint clean, webpack 115/115.
- Eight local Chromium cases and screenshots passed. Verified pointer taps, pricing navigation, Escape and focus return, reduced motion on the shortest viewport. No physical phone, iPhone Safari or signed-in production check.
- Unresolved: LK219, LK223, LK217 remaining states, LK221, LK216.

## 10 Nov 2026 (about 10:20 pm IST) — owner feedback, first part live: refund words, Pro timeline, fourth tile, Accountancy note, switch place, locked levels, Wallet first screen

- Live: main 7444fb291 (commits a3f239194 and 7444fb291; was becb9055b).
- Verified: test:app 1,034 (0 fail), dock 63, subjects 62, billing 453, landing gate 570 (0 fail), pricing/refunds/wallet/credit files 206, eslint clean; Vercel previews READY before main. No local production build this time (Vercel built both commits).
- Unresolved: LK216, LK218, LK219, LK221, LK223 not done; Wallet selling closed by WALLET_COMMERCE_OPEN and never tested with a payment; no physical phone, no iPhone Safari, no signed-in production pages.

## 10 Nov 2026 (about 9:10 pm IST) — the app-refine pass live: signed-in phone screens, Night/Day switch, one Sign out, texture, /pricing

- Live: main becb9055b (was ca0991ae8; rollback dpl_jgpwQVt4eiE6Cm3iAh9ZJgMf4nq4). Vercel preview dpl_FPoMfyNN9FRNCWY9hqgyZ9g3k5dq READY first, production dpl_9HAX3Y9Ta4P9YjeVwpoT5xdM8ohC.
- Verified: landing gate 570 tests, 546 pass, 0 fail (the old LK141 failure is fixed); test:app 1,034 (1,032 pass, 2 skipped), dock 63, du 43, keycards-ui 40, auth 141, billing 453, today 146, subjects 62, recovery 642 (639 pass, 3 todo), learn 440; new tests 27; eslint clean; next build --webpack 115/115; live public pages checked after deploy (home, /pricing).
- Unresolved: not run on a physical phone or iPhone Safari; signed-in pages checked only on the dev preview with fixtures; test:mob 7 server-side failures and test:study 1 (content gate) exist with or without this change; owner confirmations on /pricing (LK205).

## 10 Nov 2026 (about 2:50 pm) — round 12 live: creators, sixth Pro feature, film sound and full screen

- Live: main ca0991ae8 (was 79b9c49cb). Landing gate 570 tests, 545 pass, 1 old fail (LK141); eslint clean; Vercel preview READY before main; live page checked for the new figure, pictures and key. Not run: webpack build locally, a physical phone, iPhone Safari.

## 10 Nov 2026 (about 1:15 pm) — round 11 live: phone scroll v2, one Lab, five-tool tour

- Live: main 79b9c49cb (commits 49b5d9ca1 scroll v2, 79b9c49cb the page); was 7c28f3ea7, rollback dpl_6cJqMnU6b1AwqjBNna1FX1KJTGdt.
- Verified: landing gate 567 tests, 542 pass, 1 old fail (LK141); test:app, test:dock, test:du, test:keycards-ui, test:auth pass; eslint clean; next build --webpack 115/115; Vercel preview READY before main. Real-Chrome bench at 390x844 (dev build): flow 58/58, landing 6/6, jump 12/12, wheel 20/20; journey 30 / 19 / 10 flicks at 1200 / 2000 / 3000 px/s.
- Unresolved: not run on a physical phone or iPhone Safari; reserved heights off by about 324 px at 1024x768 touch; details in NOW.md.

## 10 Nov 2026 (about 4:30 am) — round 10 live: landing refinement, phone scroll flow

- Production: main 7c28f3ea7 (Vercel dpl_6cJqMnU6b1AwqjBNna1FX1KJTGdt READY, aliases www.mockmob.in and mockmob.in; fast-forward 5dbcea349..7c28f3ea7, six commits: a0745a808 first pass, 1d81f27eb round 10 visuals, 100427445 phone scroll flow, 6aff554e1 merge, 857d2193f reserved heights and the Compass fill variable, 7c28f3ea7 subgrid guard). Rollback: dpl_F112hcu3ezRJratCkZem1eQMpYSm (5dbcea349). The branch's preview build (dpl_A1eAn8qbcUbAJAVzwCr3Pzqb5kAF) was READY first, so Vercel's own bundler had built this commit before main moved.
- Phone scroll (owner LK190): FLOW on touch screens (`(hover: none), (pointer: coarse)`): no touch owned, no track locked, the stage shows the step under the window's middle, a scroll at rest settles on the nearest rest, one landing per story on its first fling from above (not the statement), hold 0.6 of the mouse's (`--ss-run`). Files: storyGesture.mjs, storyController.mjs, ScrollStory.jsx, scroll-story.css; bench modes flow, landing, journey in oneGestureBench.mjs. A mouse or trackpad is unchanged.
- Verification before deploy (local, branch tip): tests landing gate 554 / 529 pass / 1 fail (LK141 account pop-over: fails on 5dbcea349 too) / 12 skipped; test:app 1,030 pass; dock 62; du 42; keycards-ui 40; auth 141; eslint clean on every changed script file; next build --webpack 115/115. Real Chrome with real touch and wheel input on the merged dev build: flow 78/78 (tour 20, Lab 19, Recovery 19, statement 20), landing 8/8, link jumps 10/10 at 390 and 5/5 at 1440, wheel/trackpad/keys at 1440 30/30, 0 page errors. On the local production build: flow 39/39 (Lab, tour), landing 8/8; page height before and after everything is drawn within 44 px at 390x844 and 19 px at 1440x900 (reserved heights re-measured in landing.css; it was 1,281 and 874). Simulated-browser tests for the flow and the landing: oneGestureJump.test.mjs (11 new).
- Verification after deploy (www.mockmob.in): deployment READY; get_runtime_errors 30 min: none; page walks at 390x844 (first visit, Day) and 1440x900 (Night): 0 page errors; the sample's 3 of 5 opens /signup as "You got 3 of 5. Keep going."; no theme note over the phone headline; landing 8/8 in real Chrome; journey by 300 px flicks from the top to the plans: 19 at 2000 px/s (31 on 5dbcea349), 10 at 3000 px/s (23), page 22,956-23,226 px tall at 390 (27,173).
- Performance, local production build, 22 swipes at 4x CPU: cold p95 22.9 ms, 5 frames over 100 ms (max 394 ms at y 873, also present on 5dbcea349 live: 403 ms at y 866); warm p95 16.3 ms, 2 over 100 ms. Live 5dbcea349 cold for comparison: p95 16 ms, 3 over 100 ms. The old strict gate (p95 20 ms, none over 100 ms) is not met cold; it was not met consistently before either.
- Not verified: a physical Android phone, iPhone Safari (no directional touch-action there: the landing relies on putting the page back each frame, as the held clamp did), an in-app browser, a screen reader, signed-in pages. The flow was run only in desktop Chrome 151 with touch emulation.
- Unresolved: FUNNEL_ENABLED stays off (the owner said on 10 Nov he does not want measurement); the home page now sends its funnel steps, which the route answers with an empty 204 while the switch is off. LK141's test still fails (signed-in account pop-over, not touched). Orphaned headless Chrome utility process pid 42360 from 9 Nov could not be ended (19 MB).
- Production reads this session (read-only): users by month, attempts against sign-up time, payments by month and status, funnel objects. No production writes.

## 10 Nov 2026 (about 2:30 am) — conversion pass built locally, not deployed (superseded by the entry above)

- Branch web/1110-conversion a0745a808 (worktree wt-1110-convert, from main 5dbcea349). Not pushed. Production unchanged: main 5dbcea349.
- Changes: the home page sample's result is carried to /signup in the browser (sampleCarry.mjs; headline and sentence from the score and missed chapters, one day, never sent, cleared on sign-in); the first-visit theme note is not drawn below 960 px (marketing-theme.css); the home page sends its aggregate funnel steps (FunnelBeacon.jsx, DemoDrill.jsx). Write-up and definitions: CONVERSION-PASS-2026-11-10.md.
- Verification: local dev build, headless Chrome with touch at 390x844, 360x640 and 1440x900, Day and Night: sample to sign-up for scores 1, 3 and 5, 0 page errors, no sideways scroll; funnel beacons intercepted: landing_view, sample_started, sample_done, login_click, signup_click once each across a restart, two back navigations and a second press, body is the step name only, no cookie, none sent under Global Privacy Control; live /api/funnel answers 204. Tests: sampleCarry 6/6; landing + funnel + sign-up suites 311 tests, 300 pass, 0 fail, 11 skipped; test:app 1,032 tests, 1,030 pass, 0 fail; eslint clean on the changed files; next build --webpack 115/115.
- Not verified: a Turbopack build (the worktree's node_modules is a junction; Vercel builds with Turbopack, so the deploy is the first Turbopack build of this commit), a physical phone, a screen reader, the signed-in first run after sign-up (agents do not sign in on production).
- Deployment gates still open: the owner's go to deploy; FUNNEL_ENABLED=true (owner-gated since 16 Oct; both funnel migrations are applied on production, checked read-only 10 Nov: funnel_increment, funnel_count_once, users.funnel_seen, 14 steps in the check; funnel_daily holds 0 rows).
- Production reads this session (read-only): users by month, attempts against sign-up time, payments by month and status, funnel objects. No writes.

## 9 Nov 2026 (afternoon) — hero film r5 live: the owner's notes on r4

- Production: main 1184acb84 (Vercel dpl_GBHvgoKK9gESDaVQzXfzvLdzdtz6). Hero16 r5, 53.0 s, same voice (Yash) and the same nine chapter times. Promo commits 60a47b0, f7ac0b7, d112f9a, 595ef7d, 8a1df31. Changes from his r4 notes (LK183): 0-5 s is the richer older open again with a new exit (3D Mobi, college cards on three depths, the volt CUET UG 2027 chip, "Preparing for CUET 2027?", the cards spiral into the wordmark's o and an iris opens on cream); 5-10 s is a staged product tour of whole devices (exam laptop push and press, Road to CUET, then the set recedes under "Everything for CUET 2027. In one place."); features 02-07 show whole devices (no cropped laptops or phones); 01 Mocks rebuilt; the colleges row says "Not yet" (was "Below last year"); the previous end card (Mob shelf, Mobi in the o, Find it. Fix it. Check it held., Sign up free, Pro ₹99 a month) and the sound ends on one pop at 51.43 s, silent by 52.9 s. The film ends on the end card (no whip back to the open).
- Verification: two independent critic rounds (owner notes, picture craft, sound) and two fix rounds; my own review of the sheets, phone sheets and full-size frames; master -16.0 LUFS, -1.8 dBTP, sync check passes; Teaser16 and Reel916 unchanged; hero tests 70/70. Not verified: the sound by ear, a physical phone.
- Known, left as is: the product screens show the demo app's "27 weeks to CUET UG" (captured late Oct); the Ask Mobi query reads "Where am I losing marks?" (owner's call); the exam laptop shot appears in the tour and again in 01 Mocks.

## 9 Nov 2026 (midday) — hero film r4 live: 52 s narrated walkthrough

- Production: main 89b9b4d01 (player 52e267a71: "Sound on" key in the picture corner until first unmute; first unmute rewinds to the chapter start). Hero16 r4 (promo commits 35c925f, 1bbea5b, 7124faa): voice Yash A Malhotra (owner's pick from 5 auditions), one continuous take on the paid ElevenLabs account; straight opening + product montage, 01 Mocks .. 07 The Mob numbered features after klayprep's grammar, close on 15 subjects and Sign up free. Nine player chapters. r3 (101 s, Himanshu) was live 10:05 am - 12:10 pm and is replaced.
- Verification: hero tests 70/70; sheets and phone sheets reviewed; live homepage serves hero-v4 (sizes match), no runtime errors. Not verified: sound by ear, a physical phone.

## 9 Nov 2026 (early morning) — hero walkthrough film live (r2)

- Production: main be44eafca (Vercel dpl_Vtz6tKbgL61KmefrF26DgLygcPKw READY, no runtime errors; live file sizes match the r2 encodes). r1 went live first at dd8c63a7a. The hero film is the new 67 s walkthrough (Hero16 r2) with a ten-chapter bar under the picture.
- Verification: hero tests 70/70 (83 incl. todo/skip), eslint clean, local webpack production build, Vercel Turbopack build, live smoke at 390 (Night) and local 1440 Day/Night; chapter jump and tap-to-pause checked live. Not verified: a physical phone; the sound by ear.

## 8 Nov 2026 (evening) — R8 visible-craft pass and hero round 7 live

- Production: main a017c2555 (Vercel dpl_8ZMizFw6Cx4pGNiYQUDeoZqiD9mf READY, no runtime errors in the first 15 min). Contents: R8 web pass (160-finding audit, 8 batches, 34-fix sweep), hero round 7 (launch film, college strip, sample desk in #try), Arena warm hairline grid back.
- Verification: test suites (only baseline Mob 7 / Study 1 fail), landing 317/317, Turbopack build, live smoke at 390/1440. Not verified: signed-in production flows, a physical phone.
- App 1.0.22+20 built and signed (Desktop/MockMob-build-20); upload is the owner's step.

## 7 Nov 2026 — Pricing marketing pass live (owner's four changes)

- main f30bb1059, Vercel dpl_AUjRSddvYHZWeaX8ByuJ5pXPcqSJ READY, no runtime errors, live text checked.
- Hero hook: About ₹1 a mock on Pro at 3 full mocks a day (nearest rupee from ₹1 up; was ₹1.10).
- Pro card (home and /pricing): Practise, Fix (Mistake Lab; Mistake Repair and Ask Mobi, 50 credits a month all for Mobi), Revise (every Key card, saved questions), Plan. Compare table adds Mistake Lab, Mistake Repair and Ask Mobi, Key cards.
- Value card: mock series says 10 to 30 papers a subject; the repeated totals line under the bars removed.
- Note: Pro gets 50 credits a month (AI_PRO_INCLUDED_MONTHLY_CREDITS), the same as Free; the owner thought 100.
- Checks: landing/pricing tests 335, billing 453, app 1021, keycards 125, all pass; 390 Day and 1440 Night looked at.

## 8 Nov 2026 — R8 visible-craft pass, local only (not deployed)

- Web web/r8-craft (wt-1108-craft): 160-finding audit; 8 batches (tokens, recovery chain, practice/run, hero demo, home sections, Arena tools, Learn, pricing/public) each built, critiqued in a real browser, revised; merged with no conflicts; merged-site sweep fixed 34 more (focus, labels, spacing, counts).
- App ui/r8-app-craft (wt-1108-app): 19 findings + 5 from an emulator walk (Night/Day, 1.3x, reduced motion).
- Verified: all npm suites (only baseline Mob 7 / Study 1 fail), eslint 180 files clean, webpack 115/115, Turbopack 115/115 (wt-1101-content detached, restored), touch 128/128, wheel 30/30, 70 section shots, 88 before/after shots, flutter analyze clean.
- Not met: strict 22-swipe bench (R8 0-1 cold, 1-2 warm over 100 ms; pre-R8 0 / 1-2 on the same PC). Not exercised: physical phone, screen reader, signed-in production use.
- Deployment gate: owner decisions pending (key shape, Score Recovery on sale, paid key verb, Day samples, app swipe, APP-11/14/20); then the normal release gate.

## 7 Nov 2026 — Round 5 scroll fix pushed to main

- Pushed to main `c267858d1` (commits `e0f323057` + `c267858d1` on top of `bac4ae9ab`; main was `d629a2939`). The Vercel deploy is being verified separately.
- Mobile multi-step skip, root cause: the edge catch required the previous scroll frame to be more than 1 px outside a story, so a fling frame landing exactly 1 px short (1735 for a top of 1736) and then crossing was never caught and flew through every step. Reproduced 4/4, fixed (strict outside check, also in the wheel look-ahead).
- LK169 edge hitch, root cause: marking the held story (a class that changes the track's touch-action) restyles the whole story, about 90-100 ms at 4x CPU, and it ran inside the fling catch and inside a step's own frame. Now the catch only stops the fling; the mark is set at rest (settle, 150 ms after the page stops).
- The fling-stop guard now resets on settle and on each touch (it never reset before, so a second fling into the same story ran on; live had that bug).
- Speed bench (22 swipes at 4x CPU, cold and warm, quiet machine): 8-10 frames over 100 ms before, 0-3 after, none in the scroll code. The Round 4 baseline on the same PC also ranges 0-6, so the strict "zero over 100 ms" gate is not met consistently on this machine.
- Touch matrix 128/128 at 390x844 and 390x740 and wheel matrix at 1440 passed on the build with the 1 px fix (gate19). The final build's matrices were still running at push time; results to be added.
- Not done: a real Android emulator swipe test on the final build (owner asked to ship within 10 minutes). The value card iteration remains open to the owner.
- Machine note: the AI OS nightly (rag index --vectors, two embed-pending jobs, brain ingest) held the CPU at about 60-100% for over an hour on the night of 6-7 Nov and invalidated speed benches; two embed-pending ran at once (possible duplicate).

## 6 Nov 2026, about 1:00 pm IST — Round 4 release gate passed; pushed to main

- Runtime unchanged from `06aed8557` (the webpack build of 03:14 am served on 127.0.0.1:3518). The only code change is the source assertion in `data/tests/one_gesture_source_1104.test.mjs`: outside touches are now checked as `native` in `onTouchStart`; the preventDefault and behaviour assertions are unchanged.
- Landing suites (`src/components/landing/*.test.mjs`, `*_1104`, `*_1105`, `web_landing_health_1020`): 437 pass, 0 fail, 11 skipped, 12 todo. ESLint on every JS file changed since `400d647a8`: clean.
- 22-swipe bench at 4x CPU: cold over100 0 (max 97 ms, LoAF max 84), warm over100 0 (max 97 ms, LoAF max 89). Gesture matrix at 390: 128/128 (four stories 32/32) plus jump checks, no page errors.
- Visual: all 72 section captures (390 and 1440, Night and Day) reviewed. The 1440 Key cards shots caught the count-up mid-roll (16,371); a follow-up check shows it settles on the real 16,458 at 1440 and 390, rolling digits aria-hidden.
- Evidence (local, ignored): `tmp/r4-release-gate/{landing-gate2,eslint-gate2,swipes-gate2,matrix-gate2,sections-gate2,keycards-settle}.log`, `release-shots/`.
- Not exercised: production sample data, signed-in use, a physical phone, a screen reader.

## 6 Nov 2026, about 3:16 am IST — Round 4 candidate paused locally

- All six web packets are integrated on `web/r4-release` with runtime tip `06aed8557`. Round 3 is live at main `400d647a8`, Vercel `dpl_F74Lgyeyodb5YPh2kiK5HTxfiAmT` READY.
- Both builds passed and App passed 1,020 tests with two skips. The landing suite has one source assertion that still expects outside-touch classification in the old handler. The new behavior tests pass. A prior build passed 128/128, then a later build exposed one fast entry skip and one 103 ms warm frame. The current build still needs the full performance, gesture and final visual gates.
- The owner paused the session at 5% usage. Private Vercel access works after team approval. See `mockmob-next/docs/brain/HANDOFF-2026-11-06-ROUND-4-RELEASE.md` for evidence and the exact resumption steps.

## 5 Nov 2026, about 4:30 pm IST: round 3 to production (owner LK99-LK115) and new Key cards (Computerised Accounting, English reading)

Shipped (main from web/r3; spec docs/brain/night-1105/SPEC-R3.md; notes docs/design-decisions/web-r3-*.md):
- Day palette (LK101): one Day text green #526700 (the app's), Day key lip #8BA000 + hairline, Day selected states as rimmed raised paper with a volt tick (no volt slabs on cream), warm shadows; "MockMob" green in the statement (LK102).
- Brand back by role (LK108): brand stamps (desk object + product name) above the Lab, Recovery Lab, DU Compass, Instagram, Wall of love and Key cards; volt in the product screens again; branded creator cards with an answer-sheet texture; the punchy voice lines.
- Hero (LK99/LK100): calmer first screen (2-line lead, one fact line, "Hi, I'm Mobi."), the four facts as a branded number strip (judged over a rotating line).
- Held stories (LK103/LK104): cards stop above a bottom band on phones; a bottom bar with Top, the section name, n of N and Skip; the logo goes to the top; a Pricing pill in the phone nav.
- Tour (LK105): activation epoch (no finished-state flash), sequenced change instead of a crossfade, eager rail icons.
- Exam (LK106): a phone-native exam screen below 761 px in a phone frame; the desktop monitor unchanged.
- Pricing (LK107-LK111): the numbers band folded into the one plan card (glass over "Pro"), value from the offer object (about Rs X a day / a mock at 2/4/7/14 full mocks a week), a same-period comparison with three dated rival rows (5 Nov 2026, sources in a disclosure; never "cheapest"), the close band with an invite line only while invites are live.
- Key cards section (LK112): five real cards with a 3D flip, a glass front, progress and the rating keys; the loading kit (count-up on true numbers).
- Accountancy (LK115): both Part B choices stay; the AFS line notes the 2025 paper asked AFS only.
- Content (LK113): Computerised Accounting 207 cards (NCERT leca101-104, Reprint 2026-27) and English reading skills 231 authored cards; 22 held by the content lead; Financial Markets not done (the Wayback copies of lebs202 2022/2023 are truncated at 1 MiB; the full 2021 capture is the fallback).

Verified: test:app 1018, learn 434, keycards 125, keycards-ui 40, subjects 62, nta 234, recovery 637, billing 453, auth 141, dock 63, du 42, learning 357, today 146, landing and round tests 407 all 0 fail (mob 7, study 1, egress 1 pre-existing); eslint clean; webpack and Turbopack builds pass; on the production build 22 swipes at 4x CPU over100 = 0 cold and warm (p95 16 ms); one-gesture matrix 128/128 at 390; every home section looked at at 390 and 1440, Night and Day.
Not verified: a real phone; signed-in states in a browser; the per-packet independent reviews ran only for the Key cards packet (the usage limit stopped the others).

## 5 Nov 2026, about 7:45 am IST: night refinement round 2 to production (owner LK95, LK98: the app's motion on the web, public and app pages refined)

Shipped (main from web/1105-round2; design notes docs/design-decisions/web-1105-motion.md, web-1105-public.md, web-1105-appweb.md):
- The app's motion on the web (LK95): the result score's digits roll into their slots (the app's MonumentalNumber, at the owner's 720 ms result tempo, G31) and the figure is stamped as the last digit lands, with one ink ring on a good set (Celebrations Full, never in NTA mode; no shards); the Start sheet grows out of the key that opened it and goes back into it (420/280 ms, the app's grow curve; reduced motion a 120 ms fade). Fixed on the way: the result score's inner spans shrunk to 18 px by a descendant rule; focus dropping to body 125 ms after the Start sheet opened (also on main before).
- Public pages: "Sign up free" / "Log in" everywhere (site bar key, phone menu, /login, guide, /about, calculator, 404), a PublicDock with the same two keys on the public pages, "CUET 2027" and other name-number pairs never split (keepTogether.mjs), text-wrap pretty/balance (single-word last lines 188 -> 10 over 104 renders), site bar links from 1120 px (the key no longer runs past the gutter at 1024), phone footer in two columns, pricing tiles and gaps, 404 spacing.
- Logged-in web: Learn feed bar no longer overlaps (Turn over sat 33 px over Chapter from 768 to 1359 px), Practice tiles at 1280-1439 px, Your papers saved repairs at 1024-1365 px, wallet packs aligned, no monospace as decoration (credits, the MockMob runner), Marks trend and Progress alignment, 44 px top-bar targets, Key card chip contrast in Day, app-wide even lines. An automated scan of 25 views x 6 sizes x 2 themes ends with zero overlaps, spills, covered lines or sideways scroll.

Verified: test:app 1018, learn 434, keycards 125, keycards-ui 40, subjects 62, nta 234, recovery 637, billing 453, auth 141, dock 63, du 42, learning 357, today 146, landing and new tests 282 all 0 fail; mob 7, study 1, egress 1 = pre-existing (identical on base). eslint clean. Both builds pass (webpack; Turbopack in wt-1101-content). Home on the production build: 22 swipes at 4x CPU over100 = 0 cold and warm (p95 16 ms); one-gesture matrix 128/128; the demo jump lands from below every story.
Not verified: the Start sheet's open on a production build at 4x CPU (the preview harness is dev-only; on the dev build at 4x it showed main-thread frames up to about 130 ms from its clip-path; a compositor-only shape is the fix if he sees a stutter); real phones; signed-in states in a browser.

## 5 Nov 2026, about 5:40 am IST: the night refinement to production (owner LK81-LK97, his 2:40 am live-site look), and app 1.0.21+19 built

Shipped (main from web/1105-night; spec docs/brain/night-1105/SPEC.md; design notes docs/design-decisions/web-1105-*.md):
- LK81 slow-phone stutter: held stories drawn while the page is idle (storyPredraw.mjs, also the DU section), the tour keeps its screens mounted, pausing restyles only what animates. 22 swipes at 4x CPU on the production build: frames over 100 ms 11 -> 0 cold (after the hero) and warm, worst 442 -> 96 ms, p95 24 -> 16 ms.
- LK83/LK88 CTAs: Sign up free leads, Try 5 questions first second, "Have an account? Log in"; the phone dock is Log in / Sign up free from hero to footer and never changes; the close band is Sign up free / Log in. LK82 "CUET 2027." in the brand volt (#D2F000 Night, #3F5200 Day) with tabular figures; --brand-word follows, one green on the page. LK84 text-wrap pretty/balance across the landing.
- LK86 the statement's green words back (they light up as each clause arrives). LK87 the opening waits for first paint, the typed line lands whole with a resting caret, Ask Mobi "Reading your record for tonight".
- LK91/LK92 the exam screen in a CSS desktop monitor with an address bar (mockmob.in/test?...), NTA style faithful to NTA's CBT guidelines; the test runner's NTA style matches it (header, palette symbols, NTA's capitals, a section summary before submit, Question Paper).
- LK89 no demo-jump loop (the edge clamp fired on the jump's landing frame), the card lands centred with a quiet shell lift (no white ring); LK90 a fast swipe into a story lands on its edge step, geometry re-measured from the body; LK93 the DU calculator is there on arrival (no reveal gap).
- LK97 web account pop-over like the app's Account sheet (plan, credits, Appearance, links, sign out); LK95 Upgrade sheet words follow the app; the Key card turn lifts; LK94 subject options asked at onboarding (web) and Learn says "Yours is ..."; Practice at 1024-1279 px no longer collides; the numbers band lays out only the figures it has.

Verified: node suites test:app 1009, learn 434, keycards 125, keycards-ui 40, subjects 62, nta 234, recovery 637, billing 453, auth 141, dock 55, du 42, learning 357, today 146, landing 270 all 0 fail; mob 7, study 1, egress 1, health-egress 1 failing = identical on the base branch (pre-existing). eslint clean on every changed file. Both builds (webpack here, Turbopack in wt-1101-content) pass. One-gesture matrix 128/128 at 390 (four stories), wheel 27/27 at 1440, the demo jump lands from below every story at 390 and 1440. Visual pass: every home section at 390 and 1440, Night and Day.
Not verified: a real phone; signed-in hero/dock states in a browser (source tests only); onboarding options on a live account.

App: 1.0.21+19 (branch ui/1105-app-19, c34db6b69, pushed): subject options at onboarding and You > Subjects, Learn says the chosen option, the card turn lifts and catches the light (kept inside its slot after the emulator walk). Desktop/MockMob-build-19 (sells AAB, arm64 APK, symbols, OWNER-STEPS.md). Suite 12,469 pass, 111 = known old golden drift. His step: upload 19 (it replaces 18).

## 5 Nov 2026, about 12:30 am IST: the new home page "Desk Light" to production (owner LK67-LK75; his 4 Nov ~7 pm "speed up... deploy everything... as perfect as they can be"), plus tonight's Learn fixes

**What shipped (branch web/1104-polish, spec docs/brain/handoff-1104/home-spec/SPEC-HOME-1104.md on feat/app-and-web):**
- **Hero (LK67, LK70):** words first: "CUET 2027." (brand colour), "One mock.", a typed third line (Fresh every time. / Every mark traced. / rests on Know what to fix.), then "MockMob is CUET UG mock tests with a review that finds the chapter behind every mark you lose." One key. Below (phone) or beside (desktop): Mobi standing in his lamp-lit room handing over the real first question; the same idea at every width. Bubble lines follow the sample (load, right, miss, five), never taps.
- **Opening (LK74, L-043):** the app's "mo" opening on the site: about 1.3 s per new session, 1.6 s on a first visit, skipped by any tap, reduced motion, signed in or coming back from inside the site; ends hidden even without JS.
- **Night without neon (LK68):** the app's warm charcoal and cream tokens; volt only for the key, Mobi, the logo dot and selected fills; no glows, washes, glass or volt edges on containers (slop capture: glows 0, washes 0, glass 0; lime-tint pixels at 390 Night 3.70% to 0.71%). The frosted bar is now a calm near-opaque bar.
- **One gesture, one step (LK69, L-027..L-029):** the held stories (Lab, tour, Score Recovery, and the statement as a 4-step phone story) take one step per touch gesture or wheel burst at any speed; native scrolling elsewhere; jumps land on their target.
- **The exam screen (LK72):** the real MockMob runner's anatomy, theme-aware, with an "NTA style" switch that keeps answers and timer; 920 px at 390 (was 1,644).
- **Copy and brand (LK71, LK73):** about 2,300-2,470 visible words at 390 (was about 3,050), no kickers or middle dots, one Mobi finish (the rig's poses in every seat), desk-object icons in the tour, Literata for question stems.
- **Way in (L-006, L-008, L-009, L-011):** one centred dock button whose label follows the visitor (Try a CUET question / Sign up free after all five / Go to Practice signed in); the hero key never offers a signed-in student "Start free practice".
- **Learn (web half of the app's 1.0.20+18 fixes):** the Revise line says "the first back ..." when returns differ; a feed counts a turned card as done (checkpoint, stop sheet and end agree); the stopped end's Continue minutes match the checkpoint; the Options below cue is a band, never over words.

**Verified (production builds, real Chrome):**
- Every web test file: about 4,892 tests, 4,798 pass; the 28 failures are all pre-existing (authored_w2 13, mob_v3* 7, inventory_fingerprint, round5_completion, study_content, 5 scripts/pipeline, next_move_parity known gaps).
- eslint clean; `next build --webpack` and Turbopack `next build` (in wt-1101-content) exit 0 at the ship commit.
- Owner checklist L-001..L-045: 40 pass, 2 not met (L-011 fixed after the gate and checked; L-040 below), 3 need the live site.
- One-gesture matrix on the production build: every touch, wheel and key cell passes; page height fresh = warm.
- At 4x CPU, cache off: LCP 0.9-1.2 s at 390 (was 2.9 s) and 1.2 s at 1440 (was 3.7 s); CLS 0.0005; idle hero 4-5 restyles a second (was 73-165).
- Looked at: first screen at 390, 360 and 1440, Night and Day; all 14 anchors at 390 Night; the nav with the key under it; the dock mid-page and at the footer.

**Not met / left:**
- At 4x CPU, the first draw of #inside-the-lab and #your-prep still takes about 358 ms each (10-11 frames over 100 ms in 22 swipes, p95 24 ms); at 1x there is no lag. Follow-up: smaller first draws (content-visibility per scene). TBT at 4x is 0.9-2.7 s.
- Not checked on a real iPhone or Android phone; the Android emulator's Chrome stopped on its first-run terms screen (not accepted without the owner).
- The Instagram row's "MockMob post" cards have no captions in the data.

## 4 Nov 2026, about 1 am IST: Learn and Explore refinements to production (owner LK39, LK41-LK43, LK48, LK56-LK62; his 3 Nov ~11:55 pm "deploy the final changes to the website")

**What shipped (branch web/1104-english = web/1103-proto + cards + icons + webfull + R8 cards + the English pass):**
- **Key cards look like cards (LK39, LK43, LK58):** warm paper (Day) and neutral charcoal (Night), a header band in the card's family colour with its kind word, faint ruled lines on the back that the NCERT words sit on, the source as a footer; Night has one quiet hairline and no light rim. The run card sits on a two-card stack; the feed's peek is the next card's band. Meaning family is now a calm green (lime is the primary key's alone). Bigger stage and type on a computer from 1360 px (LK41).
- **Top bar (LK42):** the account as one calm capsule (credits with its word, then the avatar and plan); every destination kept.
- **Up next (LK59):** Learn home recommends in one module with Today's anatomy: one move on the card, the other moves as swap cells, the server's pick marked Suggested; roadmap rows say state ("Needs work"), not advice.
- **The phone website as the full product (LK62, LK48):** Find's four sets (Due today, Missed lately, In Revise, Must-know lines) are on Learn home under the field; before, three of them had no way in.
- **Brand icons (LK60):** desk objects instead of vague line icons on the chapter shelf and Practice's doors (R7 I-ICONS.md).
- **English (LK61):** the E-ENGLISH table on the web (rows in E-APPLIED-WEB.md): one name per action (Turn over; Missed it, Got it, Easy with what each does), contractions, no middle dot except before a length, no idioms.

**Verified:**
- Every web test file (4,402): 4,334 pass, 23 fail, all pre-existing on live main: authored_w2 13, mob_v3* 7, study_content 1, round5_completion 1 and inventory_fingerprint 1 (the last two checked on an origin/main checkout).
- `eslint .` clean; `next build --webpack` exits 0; `next build` (Turbopack) exits 0 at the ship commit in a worktree with a real node_modules (Turbopack refuses a junctioned node_modules).
- Looked at: Learn home 390 Day and Night, 1440; Explore 390 Night; Key cards front and back at 390 and 1440, Day and Night, in the feed, the run and a typeset Maths card (tmp/learn-1103/r8-cards/after, made by scripts/design-audit/learn-r8-cards-capture.mjs). No console errors.

## 3 Nov 2026, about 11:59 pm IST: Physics formula cards (owner LK34): Physics 1,090 to 1,403 cards, about 5.5 to 7.2 hours

**What shipped:**
- **Physics: 1,090 to 1,403 cards** (312 with typeset formulas), all 14 NCERT chapters (leph101-108, leph201-206). Each new or reworked card passed an Opus formula reviewer against the page image and a Sonnet content reviewer (handoff-1102/ptex-wave-1103.js, 42 agents; fix round ptex-fix-wave-1103.js, 15 agents; merged with merge-ptex-reviews-1103.mjs). Hours (handoff-1102/deck-hours-1103.mjs): 7.23 h.
- **The tex check** reads Greek as the Symbol-font letter the PDF prints (958f2b8c3), so inline Physics formulas such as 1/4pe0 match their typeset line.
- **One layout fix:** the superposition-of-forces card (Electric Charges and Fields, p. 12) set its long display formula as two aligned rows (v3), because at 60% fit it still scrolled on a phone. Same symbols, same line count; its review verdict carried over.
- **Safety:** no published card removed or changed (deck comparison with HEAD: 0 removed, 0 changed); check-drafts-ptex-1103.mjs OK for both rounds.

**Verified:**
- Suites: keycards 125, keycards-ui 40, learn 417 pass. `eslint .` clean; `next build` and `next build --webpack` both exit 0 (before the one-card layout fix, a data-only change; keycards suites re-run after it).
- Width: every one of the 312 typeset lines measured inside a real card back at 360 and 390 px phone widths with the card's own fit rule: none scrolls, none spills. Looked at a turned formula card at 390 Night.

## 3 Nov 2026, about 2:35 pm IST: Mathematics 349 to 548 formula cards (owner LK34); every Google font self-hosted (production builds no longer fail on the font fetch)

**What shipped:**
- **Mathematics: 349 to 548 cards** (221 with typeset formulas), from the other 10 NCERT chapters (handoff-1102/mtex-wave-1102.js, 30 agents) and a fix round on cards held only for a formula point or only as ambiguous (handoff-1102/mtex-fix-wave-1103.js, 12 agents). Each new or changed card passed an Opus formula reviewer comparing every symbol with the page image and a Sonnet content reviewer. Per chapter: Integrals 82, Matrices 58, Continuity & Differentiability 57, Vector Algebra 56, Determinants 47, Three Dimensional Geometry 41, Application of Derivatives 37, Relations & Functions 35, Differential Equations 30, Probability 29, Linear Programming 26, Inverse Trigonometric Functions 21, Application of Integrals 11 and Probability Distributions 1 (both with coverage notes: NCERT 2026-27 shortened or removed them). About 2.9 hours by data/learn/seconds.js, just under the 3-hour bar; NCERT's text supports about this much.
- **Fonts:** Bricolage Grotesque, Gabarito, Hanken Grotesk and Literata (the NCERT reading face) are now served from src/app/fonts (Fontsource 5.3.0, OFL), as Geist Mono already was. Vercel runs `next build` (Turbopack), whose Google-font loader failed intermittently (2152e0b74's first build: "next/font/google queries have exactly one entry", Gabarito); with no next/font/google left it cannot recur. Production and local home pages compared at 390 Night and 1440 Day: same faces, weights and line breaks.
- **Formula fit:** a display formula is fitted again when its glyph runs change size, so the fit holds on a first visit while KaTeX's fonts load (measured in fresh browsers: Matrices, Determinants, Vector Algebra and Integrals fit every wide formula; two Probability formulas with worded fractions stay at the 60% floor and scroll inside their line; their rework is queued).
- **Safety:** no published card was removed or changed (deck comparison with HEAD; check-drafts-mtex-1102.mjs OK for both rounds after the 5 pilot cards were confirmed identical to their live versions).

**Verified:**
- Suites: keycards 124, keycards-ui 40, learn 403, option-order 7, today 146, app 987, learning 357, syllabus 24 pass.
- `eslint .` is clean; `next build` (Turbopack) and `next build --webpack` both exit 0; no KaTeX JS and no Google Fonts reference in the build output.
- Looked at: the home page (production vs local fonts), formula cards in Determinants (feed, 390 Night), and the Read view of Matrices, Determinants, Vector Algebra, Integrals and Probability (390 Night) in fresh browsers; no page errors.
- 2152e0b74 went live through a redeploy (dpl_9v6kS4VjVk9k5pArAts6kbpkFS2A) after its first build failed on the Turbopack font loader; no runtime errors.

**Rollback:** the previous production deployment.

## 2 Nov 2026, about 11:20 am IST: Maths formula cards to production (owner LK34, his "Yes, start it"): typeset formulas on Key cards; Mathematics 310 to 349; Geist Mono self-hosted

**What shipped:**
- **Typeset formulas on Key cards** (handoff-1102/MATHTEX-SPEC.md). A mathematics or physics card may carry `tex`, the LaTeX of its front and back, transcribed from the NCERT page image.
  - The server draws it with KaTeX 0.19.0 (pinned; MIT) into `texHtml`, with prose escaped, trust off and a forbidden-command check. Only KaTeX's CSS and fonts reach the browser, never its JS (`grep "KaTeX parse error" .next/static`: none).
  - Every plain client (the app, search, screen-reader lines) gets a readable Unicode form instead of the PDF text ("tan⁻¹((x + y)/(1 − xy))", "A⁻¹ = (1/|A|) adj A", "[x + 1, 2; 3, y − 1]").
  - New checks in scripts/keycards/lib.mjs (shape:tex_*): KaTeX parses in strict mode; each tex line has the same letters and digits as the PDF-checked back line (so a wrong digit or a missing term fails); the prose is NCERT's; no long inline math; no capitalised function name opening a front.
  - Drawing: Prompt, NcertText, the feed's CardFace and the Cards list. A display formula wider than its line is set smaller (down to 60%) and then scrolls inside its own line; the card never widens.
- **Mathematics: 310 to 349 cards.** Inverse Trigonometric Functions 7 to 21, Probability 9 to 29, Application of Integrals 6 to 11. Every new or reworked card passed two independent reviewers: an Opus formula reviewer comparing each symbol with the page image, and a Sonnet content reviewer. Coverage notes: Application of Integrals (NCERT 2026-27 keeps 8 pages) and Probability Distributions (NCERT 2026-27 removed it; one paragraph remains).
- **Geist Mono is served from the repo** (src/app/fonts, OFL, from geist 1.8.1), so production builds no longer fetch it from Google Fonts (2 of 4 builds failed on that fetch on 2 Nov).
- **Safety:** no published card was removed or changed (deck comparison with HEAD; handoff-1102/check-drafts-mtex-1102.mjs OK).

**Verified:**
- Suites on the merged tree (with main dc6e45561, Learn v2 round 5): keycards 124, keycards-ui 40, learn 403, option-order 7, today 146, app 987, learning 357, recovery 637, egress 101, dock 55 pass. Before the merge also syllabus, subjects, billing, auth, du, community, nta and the rest pass; the known failures (authored-publish 13, factory 5, mob 7, study 1) are unchanged.
- `eslint .` is clean, and `next build --webpack` exits 0.
- Looked at in the local preview: formula cards in the feed (390 Night and Day, 1440 Night and Day), the Cards list, and the Read view at 1440 Night; the wide conditional-probability formula fits its line; journal entries and lists unchanged (no card back overflows).

**Next:** the other 10 Maths chapters after the 1:20 pm usage reset (handoff-1102/mtex-wave-1102.js, mtex-args-b-1102.json).

**Rollback:** the previous production deployment (main dc6e45561).

## 2 Nov 2026, about 11 am IST: Learn v2 round 5, first wave (owner LK38, LK40, LK44-LK47): every answer was A; the three keys say what they do

**Owner, ~10 am** (verbatim in mockmob-next docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md, "2 Nov 2026, about 10 am"): every answer in the Explore feed seems to be A; nobody can tell what Missed it / Got it / Easy do; a scroll over the question does not scroll the page; do fixes 2, 3 and 4; tabs Practice, Papers, Learn, Explore; the landing's first section scrolls too fast.

**What shipped (web/1102-r5 = web/1102-shuffle + web/1102-stage-r5 + three web/1102-chrome commits; spec docs/brain/learn-1031/r5/R5-SPEC.md):**
- **LK44 options:** verified keys were 68% A (Accountancy 84%). One stable order per question (`data/option_order.js`, the NTA engine's own blockers, seeded by the id) on every non-NTA surface: Learn, Explore and Saved, practice and recovery papers, Revise, Rival, repair and Mobi checks; the stored letter is what is saved; runs started before keep the stored order; Mob papers switch from the week of 9 Nov (`STABLE_ORDER_FROM_WEEK`). After: 27/25/24/24 (`docs/brain/learn-1031/r5/A-OPTIONS.md`). No database write, no migration.
- **LK38 keys:** each key says when the card returns ("Got it / back in 3 days"), the stamp after a rating says where it went, a once-per-student line explains the three, and In Revise counts all three ratings.
- **LK45 fixes 2 and 4:** the stop sheet and the end count done the same way; a run over several chapters is headed Revise. (Fix 3 is the app's.)
- **LK40:** the run's item area and card face no longer trap the wheel.
- **LK46:** Practice's tabs read Practice, Papers, Learn, Explore. **LK47:** the landing's held stories no longer catch the wheel (one notch moved 864 px; now 100).
- **Held for his live look:** the top bar capsule (web/1102-chrome 53b500e62, LK42).

**Verified before the push:** test:learn 403, option-order 7, app 987, keycards 82, keycards-ui 40, recovery 637, billing 453, nta 229, learning 357, dock 55, egress 101, today 146, auth 141, all 0 failures; mob 344/7 and study 61/1 fail the same on a16fbd62e (not this change). `next build` compiled. Stage looked at 390 and 1440, Night and Day, with real wheel events (agent B1); landing and tabs likewise (agent C1). The option order was not looked at in a browser before the push.
**Risk:** a page loaded before the deploy and answered after it can be mis-graded once (Explore progress, Revise).

## 2 Nov 2026, about 9:45 am IST: Key cards +668 to production (owner LK34): recovery round 2 (cards held as ambiguous, and Computer Science front wording)

**What shipped (15,469 cards, from 14,801):**
- **Recovery round 2:** 1,003 held cards went through a fixer and an independent re-reviewer (handoff-1102/recovery2-1102.js, 56 groups, 112 Sonnet agents, 0 errors). 876 had passed review on exact and important but were held as not unambiguous; 127 Computer Science cards were held only for front wording. A fixer either gave the front the context that leaves one right answer, changed the blank or the kind, or dropped the card when no honest fix existed.
- **Published gain:** Computer Science +194 (1,544), History +90, Sociology +88, Geography +107, Chemistry +57, Psychology +48, Physics +46, Mathematics +20 (310), Accountancy +8 (920), Economics +5, Biology +2, Political Science +2, Business Studies +1. English unchanged (650).
- **Safety:** no published card was removed or changed (deck-by-deck comparison with HEAD). handoff-1102/check-drafts-r2-1102.mjs confirmed the fixers touched only their fix-list cards. One fixer (lebs108) reported edits that never reached the draft; its two cards stay held, and the reviewer's verdict for the missing id is ignored by review-merge.
- **Tiers:** 3,803 of 15,469 cards are Must-know (25%). learn_preview now pins Accountancy at 920 cards and 236 Must-know.

**Verified:**
- Suites: keycards 82, keycards-ui 40, learn 381, syllabus 24, subjects 62, today 146, recovery 637, billing 453, auth 141, app 984, du 42, dock 55, community 11, learning 357, nta 229, question-reorder 25, goal-minutes 23, attempt-reads 12, health-auth-board 10, least-privilege 12, egress 101, answer-integrity 11, health-egress 56: all pass. Known failures, also on main 978edc236: authored-publish 13, factory 5, mob 7, study 1.
- `eslint .` is clean, and `next build --webpack` exits 0.
- Looked at in the local preview: feed cards in Computer Networks, Mass Media and Communications, Vijayanagara and Attitude and Social Cognition (390 Night, face and back), Amines and Planning and Sustainable Development (1440 Day), and the Computer Networks card list (390 Day, 84 cards). No page errors.

**Rollback:** the previous production deployment (main 31af5f9dc, dpl_CxXNLxRhN454H9K32NJJpqVL8xFb).

## 2 Nov 2026, about 4:35 am IST: Key cards +911 to production (owner LK34): wording recovery, English top-up, Accountancy thin chapters

**What shipped (14,801 cards, from 13,890):**
- **Recovery round:** 778 cards were held back only for front wording (a front opening with It/This/These, a front over 140 characters, a back that is not the quote). Fixers re-cut them under ncert-books/FIX-BRIEF-2026-10-31.md, and an independent reviewer judged every edited or new card. Published gain: Chemistry +97, Geography +76, History +79, Mathematics +30, Physics +112, Psychology +52, Sociology +119.
- **English:** 350 to 650. 322 new authored cards (word, idiom, one-word substitution, commonly confused words, grammar rules); 300 passed review.
- **Accountancy:** 866 to 912. 80 new NCERT cards for Change in Profit Sharing Ratio, Retirement & Death, Analysis of Financial Statements and Comparative & Common Size Statements; 46 passed.
- **Safety:** no published card was removed or changed (deck-by-deck comparison with HEAD). handoff-1102/check-drafts-1102.mjs confirmed that the fixers touched only their fix-list cards. merge-reviews3-1102.mjs removes the old verdict of any card edited in place without a fresh one; there were none.
- **Tiers:** 3,659 of 14,801 cards are Must-know. learn_preview now pins Accountancy at 912 cards and 235 Must-know.

**Verified:**
- Suites: keycards 82, learn 381, keycards-ui 40, today 146, app 984, learning 357, recovery 637, subjects 62, syllabus 24, auth 141, egress 101, health-egress 56, dock 55, billing 453, du 42, community 11. All pass, with 0 failures.
- `eslint .` is clean, and `next build --webpack` exits 0.
- Looked at in the local preview: recovered History, Physics and Sociology cards (390 Night); English word and usage cards and the new Accountancy definition (390 Day); the Change in Profit Sharing Ratio card list (11 cards, new ones in their sections); English Vocabulary (523 cards, new idioms in place). No console errors.

**Rollback:** the previous production deployment (main feb30935e).

## 2 Nov 2026, about 4:15 am IST: Key cards for Computer Science to production (owner LK34); a blank keeps its punctuation on its line

**What shipped:**
- **Computer Science:** 1,350 cards across 18 chapters, from 19 NCERT PDFs (Computer Science XII Ch 1-12, Informatics Practices XII Ch 1-7). 567 are held back with reasons.
  - Project Based Learning (Computer Science Ch 13) is outside CUET Section B1, so it has no cards. The Informatics Practices chapter of the same name gave 10.
  - Only the Computer Science reviews were merged (KEYCARDS_REVIEWS_DIR), so no other subject's verdicts changed while the recovery round runs.
- **Tiers:** 3,500 of 13,890 cards are Must-know.
- **Blanks:** a comma, stop or closing bracket after a blank (or an opening one before it) now stays on the blank's line. 1,087 published fronts have one, and before this a line could start with ", and". `blankRuns` and `gapClass` are in kinds.js, used by the stage, the chemistry stage, KeyCard and the card list.

**Verified:**
- Suites: learn 381, keycards 82, keycards-ui 40, today 146, app 984, auth 141, egress 101, health-egress 56, dock 55, recovery 637, billing 453, subjects 62, syllabus 24, learning 357, du 42, community 11. All pass, with 0 failures.
- `eslint .` is clean, and `next build --webpack` exits 0.
- Looked at these cards in the local preview: SQL front and back, Stack, and Pandas, at 390 Night. The SQL blank card also at 390 Day and 1440 Night and Day, and a Chemistry blank card at 390 Day. The preview showed no console errors.

**Rollback:** the previous production deployment (main 7f1b204a7).

## 2 Nov 2026, about 4 am IST: Key cards for Physics and Mathematics to production (owner LK34)

**What shipped:**
- **Physics:** 932 cards from 14 NCERT chapters, 397 held back.
- **Mathematics:** 260 cards from 14 chapters, 234 held back.
- Both were written under the plain-text notation rule. pdftotext flattens powers, subscripts and fractions, so a card carries no formula whose meaning depends on them, and the reviewers flagged any flattened notation. A scan of both decks found none.
- **Mathematics is thin.** Three Dimensional Geometry has 1 card; Inverse Trigonometric Functions and Vector Algebra have 5 each. Its formulas need a typeset pipeline: transcribe NCERT pages to LaTeX and render them on cards.
- **Tiers:** 3,165 of 12,540 cards are Must-know.

**Verified:**
- test:keycards 82, test:learn 381.
- `next build --webpack` exit 0.
- Looked at: a Physics card (Alternating Current) and a Maths card (Application of Derivatives), at 390 Night.

**A note on the preview:** the 4-card feeds are the backlog rule, "Revise first: 42 due", for the seeded preview student. This is not a bug.

**Rollback:** the previous production deployment (main 26e5f359a).

## 2 Nov 2026, about 3:30 am IST: Key cards for Geography, Psychology and Sociology to production (owner LK34)

**What shipped:**
- **Geography:** 1,162 cards from 17 NCERT chapters, 444 held back.
- **Psychology:** 726 cards from 7 chapters, 150 held back.
- **Sociology:** 983 cards from 14 chapters, 441 held back.
- All are exact NCERT Reprint 2026-27 text with book, chapter and page. Each chapter was written by a subscription author and checked by an independent reviewer. The held-back cards and their reasons are in `data/keycards/quarantine/`.
- **Tiers:** 2,840 of 11,348 cards are Must-know.
- **Thin chapters:** Sociology's Structural Change (8 cards) and Cultural Change (32) are short in NCERT too.

**Verified:**
- test:keycards 82, test:learn 381, test:keycards-ui 40.
- `next build --webpack` exit 0.
- Looked at: one feed card per subject, at 390 Night (Geography term card, Psychology difference card, Sociology definition card).

**Not changed:** no migration, no env var.

**Rollback:** Vercel instant rollback to the previous production deployment (main 90679d8c0), or revert this fast-forward.

## 2 Nov 2026, about 3 am IST: Key cards for Chemistry and History to production (owner LK34)

**What shipped:**
- **Chemistry:** 1,257 cards from 10 NCERT chapters.
- **History:** 1,418 cards from 12 NCERT chapters.
- Both are NCERT Reprint 2026-27 exact text with book, chapter and page. Each chapter was written by a subscription author and checked by an independent reviewer. 298 and 337 cards are held back, with reasons, in `data/keycards/quarantine/`.
- **Review rule:** importanceRight is advice only (scripts/keycards/review-merge.mjs), because tiers.json decides Must-know. This publishes 4 cards in Business Studies, Economics and English that had been held only for their label.
- **Accountancy chapter 1** defines partnership by Section 4 of the Partnership Act (Ch 1, p. 2). The Ch 2 restatement is held as its duplicate.
- **Tiers:** 2,105 of 8,477 cards are Must-know.
- **Science notation (chemistry cards):** formulas, complex-ion charges, NCERT's en-dash minus, electron configurations and monatomic ions. Checked over all 1,257 cards and on screen.

**Verified:**
- Suites:
  - test:learn 381
  - keycards 82
  - keycards-ui 40
  - today 146
  - app 984
  - auth 141
  - egress 101
  - health-egress 56
  - dock 55
  - recovery 637
  - billing 453
  - subjects 62
  - syllabus 24
  - learning 357
- `eslint .` exit 0.
- `next build --webpack` exit 0 on the second try. The first try failed in next/font while fetching the Google Fonts CSS, a transient network failure; the retry passed unchanged.
- Looked at: the feed cards for Coordination Compounds, d- and f-Block, Alcohols and Harappa, front and back, at 390 Night.

**Not changed:** no migration, no env var. The decks are bundled JSON, and the manifest sha256 is checked at load.

**Rollback:** Vercel instant rollback to the previous production deployment (main 668341aea), or revert this fast-forward.

## 1 Nov 2026, about 11:55 pm IST: Learn v2 rounds 2 to 4 (owner LK24-LK35) to production

**Owner, 4:05 pm** (verbatim in mockmob-next docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md):
- the phone web is cluttered and slow
- Learn should lead with a start offer, never zeros
- first-time cues
- less blank space, no walls of text
- a tighter, branded hero that reacts to taps
- keep going

**What shipped:** web/1031-learn-v2, fast-forwarded into main, 48 commits.
- **Round 2:**
  - start offer and roadmap
  - one end screen and the stop sheet
  - feed cues and the chapter page
  - four phone tabs
  - speed: combined `/api/today` and `/api/learn/home`, auth chain, CSS split
  - the painted hero with Mobi taps
- **Round 3** (`docs/brain/learn-1031/r3/R3-SPEC.md`, the critics' findings):
  - one word per thing (`data/learn/words.js`)
  - one true Free rule
  - no zero leads
  - flashcard layout and the next card's peek
  - static H1
  - one due count
  - Today without false history
- **Round 4** (`docs/brain/learn-1031/r4/R4-SPEC.md`, findings verified by 1-3 skeptics each in `R3-REVIEW-FINDINGS.md`):
  - Free rows show the real chapter size
  - chapters named by roadmap place ("Chapter 5 of 14")
  - Free never offered a key the server refuses
  - due counts respect the part option
  - the address follows the run
  - science notation for chemistry cards
- **Not changed:** no migration, no new env var (NEXT_PUBLIC_LEARN2 and LEARN2_ENABLED stay on).

**Verified before the push** (HEAD 689617ed8):
- Suites:
  - test:learn 380
  - keycards 81
  - today 146
  - app 984
  - auth 141
  - egress 101
  - dock 55
  - keycards-ui 40
  - subjects 62
  - syllabus 24
  - learning 357
  - recovery 637
  - billing 453
  - nta 229
  - health-egress 56
  - and 8 more, all 0 fail
- `eslint .` exit 0; `next build --webpack` exit 0.
- **Captures:** 180 shots at 390, 360x640, 1440 and 1920, Night and Day (`tmp/learn-1101/r4-merged/INDEX.md`): 0 failures and 0 console errors. Each round's shots were looked at.

**Known failures, also on main 978edc236, not from this work:**
- test:authored-publish: 13
- test:factory: 5
- test:mob: 7 (SV-1, SV-5..9, SV-10/11, SV-17, SV-15, L-55, room ticket)
- test:study: 1 (the WordNet licence check)

**Not verified:**
- a real phone or trackpad
- a screen reader
- the live Practice chapter count: `/api/chapters` reads the chapters table and may say 15 where Learn says 14, if a Computerised Accounting row exists there

**Rollback:** Vercel instant rollback to dpl_DoGHp6AAWaCKngaFxKAckyhq7vAy (main 978edc236), or revert the fast-forward range 978edc236..689617ed8.

## 31 October 2026, about 6:50 pm IST: Key cards fixes from the owner's first live look (LK2, LK5, LK6, LK13)

**Owner, 5:20 pm** (verbatim in mockmob-next docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md): Your part "glitches sometimes and shuffles it"; Study is "exactly what we wanted" but needs motion; the print sheet needs "our watermark all over the place"; too many cards say "must know". The wider Learn redesign (LK1, LK3, LK4, LK7-LK12) is being built as a preview for his OK first.

- **LK2, Your part picker** (KeycardsHome.jsx, api.js, optionChoice.js): the tapped part stays selected through the save and the re-read; taps are ignored while in flight (one PUT); the old list dims instead of jumping; only new rows fade in; a failed re-read keeps the page with "Saved. The chapter list did not refresh." and Try again. Proven with a dev-only 1,500 ms delay (&kclag), 390 and 1440, Night and Day.
- **LK5, Study motion** (KeyCard.jsx, ChapterDeck.jsx, studyMotion.js, keycards.css, shared liftGhost in studyFeel.js): the answer opens in 220 ms with the quote rising 8 px; a badge on the rating key (check, double check, or a grey come-back arrow); the card leaves only after the server accepts the rating (Got it right and up, Easy higher, Missed drops back); the next card rises in 240 ms; reduced motion cross-fades. Frames reviewed at 390 and 1440, Night and Day.
- **LK6, watermark** (src/components/print/PrintMark.jsx, printSheet.css): the logo B tiled at -28 degrees, 7% black, on every printed page of the Key cards chapter sheet, a lesson's summary and the chapter summary; footer "Printed for <first name> from mockmob.in on <date>." Checked in A4 PDFs page by page.
- **LK13, Must-know re-tier** (scripts/keycards/tier.mjs, data/keycards/tiers.json applied in loadDecks; decks, manifest and hashes untouched): top quarter of each chapter by question links, card kind and NCERT summary sections, 6 to 40 per chapter: 3,916 (68%) became 1,439 (25%). The app reads it through the same API with no release. Free's 5 taste cards change in 71 of 73 chapters; only one account had used Key cards (10 card states), so no student loses cards.
- **Checks:** test:keycards 76/76, test:keycards-ui 40/40, test:recovery 637/637, test:study 61/62 (the known WordNet licence check, also failing on main), study_feel and vercel_config 18/18, eslint clean on changed files, `next build --webpack` passes and traces tiers.json into /api/keycards, /deck and /api/me/revise.
- **Rollback:** delete data/keycards/tiers.json (author marks return, with one [keycards] warning) or revert the merge.

## 1 Nov 2026: Learn v2 and the Explore feed ON (owner "Ship it")
- Code: web/1031-learn-v2 fast-forwarded into main (106e53720), deployed first with the switches off and smoke-tested.
- Migration 20261101150000_learn_runs.sql: dry run then apply by the owner in the SQL editor; verified (both tables, both
  security-definer functions, flow_context accepts learn, no anon read). Undo: supabase/undo/20261101150000_learn_runs.undo.sql.
- Switches: LEARN2_ENABLED=true and NEXT_PUBLIC_LEARN2=on (production). Off = set them off and redeploy.
- Verified before deploy: test:learn 244, keycards 81, auth 137, recovery 637/640 (0 fail), billing 453, egress 101, today 120, dock 55;
  test:app 986/990 (2 landing hero tests that also fail on main). Not verified: real phone, trackpad, screen reader.

## 31 October 2026, about 4:50 pm IST: 218 off-syllabus questions pulled; 25 earlier pulls actually frozen

**Owner:** "Pull them all" (the 218 questions the pool audit found outside the CUET 2026 syllabus).

- **Applied on production** (`docs/brain/intel-1031/off-syllabus-2026-10-31/`, pull.sql and an exact undo.sql):
  - The 218 are now `is_cuet_syllabus = false`, `pending` and `frozen`.
  - The 25 answer-key pull-outs from the morning are frozen too. They had been set to `pending` only, but a verified,
    active row is still served (VISIBLE_QUESTION_FILTER), so they were still reaching students until now.
- **Dry run** (rolled back): 218 pulled, 25 frozen, 0 learning episodes invalidated. **Check after:** visible
  questions 8,571 to 8,328, matching.
- **Thin chapters now:** Accountancy, Financial Statements of Company, 1 question left; Political Science, Recent
  Issues and Challenges, 4 left. New questions only on the owner's ask.
- **No deploy needed:** data only. Practice caches follow `updated_at`; the inventory recounts at the next cron.
- **Not touched:** 22 older pending, verified and active rows (Mathematics, Hindi, English, from April), outside the
  pilot.

## 31 October 2026, about 1:35 pm IST: Key cards ON for students (KEY_CARDS_ENABLED=true)

**Owner, after seeing the screens:** "Turn it on".

- **Flag:** KEY_CARDS_ENABLED=true in Vercel Production (plain, env id upxHGi3akyKdAkvi). Redeployed from dpl_D6QMYXQCyFwVGTHNz3gfcfHfagG4 as dpl_7dHWVGYYCxR753iJ8wW6Ppgaoyx4 (main f3ebd6b9c), aliased to www.mockmob.in.
- **Smoke (no sign-in):**
  - /api/keycards, /api/keycards/deck, /api/keycards/line, /api/me/chapters and /api/me/revise answer 401 Unauthorized signed out (were 404 KEY_CARDS_OFF).
  - Pages /, /cards, /learn, /pricing and /dashboard all 200.
  - get_runtime_errors: none.
- **Decks are bundled:** a local `next build --webpack` of the same commit traces the 7 deck files, the 7 link files and manifest.json into /api/keycards, /deck, /line and /api/me/revise (outputFileTracingIncludes).
- **Not verified:** the signed-in flow on production. No agent signs in there, so the first student request is the first real one.
- **Off:** set KEY_CARDS_ENABLED to anything but true (or delete it), then redeploy. The tables and data can stay.

## 31 October 2026, about 1:20 pm IST: Key cards release DEPLOYED with the flag off (main 5c1d03a37, then this STATUS commit); syllabus v2 and Key cards migrations applied; 561 re-tags; 59 flawed questions fixed

**Owner's go-ahead (31 Oct):** "Yes, run them".

- **Deploy:**
  - `git push origin HEAD:main` 0b7d6bc03..5c1d03a37 (fast-forward; main had not moved).
  - Vercel dpl_jzeVzYF2yT6F8EwUQxM9EcnPvPau READY, aliased to www.mockmob.in and mockmob.in.
  - **Rollback point for the code:** dpl_5QtNxZUkLvxXBWxJfJLDL6tLxaXE (0b7d6bc03).
- **Smoke (no sign-in):**
  - Pages: /, /pricing, /login, /signup, /cuet, /cuet/accountancy, /privacy, /help, /cards and /learn all 200.
  - /api/keycards, /api/keycards/deck and /api/me/chapters: 404 KEY_CARDS_OFF.
  - /api/me/revise and /api/me/review: 401 signed out.
  - /preview/arena/realdeck: 404.
  - get_runtime_errors: none in the 40 minutes after READY.
- **Production dry runs, each in one transaction ended by a raised error, so everything rolled back:**
  - syllabus v2: 567 questions retired, 59 renamed, 191 live chapters, none without a unit.
  - key_cards: key_card_review() on a real user answered ok, then replay, then conflict, with 2 allowances claimed.
  - After each rollback, no column, table or flag was left behind.
- **Applied with the Supabase MCP (recorded in schema_migrations), in order:**
  1. syllabus_v2 (20261031130000).
  2. syllabus_v2_fix_live_rows (20261031150000). Eight live chapters got no row in step 1, because their generated id was held by the old-named row (for example business_studies__financial_management = "Business Finance"). This adds them; there are now 199 live chapters, all with units.
  3. key_cards (20261031140000).
- **Re-tags through public.apply_syllabus_retag:**
  - data/syllabus/retag-2026-10-31.json: 85 of 85 moved. 80 moved at first; 5 moved after step 2.
  - data/syllabus/retag-live-2026-10-31.json: 476 of 476 moved.
- **Pools after (live, in syllabus):**

  | Subject | Before | After |
  |---|---|---|
  | Biology | 451 | 369 |
  | Chemistry | 466 | 395 |
  | Computer Science | 387 | 347 |
  | Political Science | 281 | 252 |
  | Business Studies | 422 | 417 |
  | Economics | 466 | 454 |
  | History | 273 | 259 |
  | Geography | 223 | 214 |
  | Physics | 383 | 373 |
  | Psychology | 161 | 145 |

  Accountancy, English, Mathematics, Sociology and GAT are unchanged.
  - **Not yet in a live chapter:** 16 in Computer Science "Data Structures" and 2 in Geography "Resources & Development" wait for a split re-tag. 15 in Computer Science "Communication Technologies" are resolved by code aliases.
- **Flawed questions:** 59 fixed, from docs/brain/intel-1031/answer-keys-2026-10-31.
  - 3 keys corrected, 31 reworded (the key kept), 25 set to pending.
  - Every guard was checked before applying, and every batch was checked after.
  - The learning_evidence_change trigger invalidates learning episodes built on a changed question. This is intended.
- **Flag:** KEY_CARDS_ENABLED is unset (off). **To turn it on:** set KEY_CARDS_ENABLED=true in Vercel Production and redeploy, after the owner has seen the screens.
- **Undo, in order:**
  1. Keep the flag off.
  2. Run each answer-keys batch's undo.sql.
  3. Run docs/brain/intel-1031/retag-live-2026-10-31.undo.sql.
  4. Run supabase/undo/20261031140000_key_cards.undo.sql.
  5. Run supabase/undo/20261031130000_syllabus_v2.undo.sql. It also reverses the 85 re-tags and removes the fix rows.
  6. For the code, promote dpl_5QtNxZUkLvxXBWxJfJLDL6tLxaXE.
- **Open:**
  - The inventory recounts in full at the next cron (logic version 4).
  - The 218 outside-syllabus questions wait for the owner (docs/brain/intel-1031/POOL-AUDIT-2026-10-31.md).
  - The syllabus v2 SQL generator should not skip a live chapter whose id is held by another name. The fix migration covers production.

## 20 October 2026, 9:25 pm IST: website release 15 DEPLOYED (main 2c71cb810, then this STATUS commit); 7 migrations applied on production; MOB_FORMATS_ENABLED=true
- **Migrations applied on production (isrxrxzjocewrdureyhp) with the Supabase MCP, in order:** 20261020150000_attempts_lean_fn, 20261020150100_attempt_question_ids_fn, 20261020150200_referral_any_practice, 20261020152000_mob_den_fix, 20261020160100_inventory_content_digest_fn, 20261020160000_usage_consent_d183, 20261020151000_mob_hours (recorded under their names in schema_migrations). Undo files: supabase/undo/<same name>.undo.sql. Staging dry runs were NOT done (staging is off-limits while the egress quota is fragile, D177/D178); each file was applied twice and undone twice on PGlite against the real migration chain in its tests.
- **Pre/post checks:** mob_members 1 -> 1 (sharing 0), usage_consent 4 rows -> 4 (4 on), checks usage_consent_adult_only -> usage_consent_minor_off, all 9 functions present after.
- **Deploy:** Vercel dpl_HmtsjmbMPDWK7u2RfZS3S21fyHZu READY on www.mockmob.in. Smoke: /, /privacy (shows "Optional usage data (updated 20 October 2026)" and Rather not say), /pricing, /account-deletion 200; /api/mob and /api/me/consent 401 signed out; no runtime errors in 30 minutes. Rollback: dpl_4bn4VVutv4Lyxf2JE1yLyCMrTQVG (main 85c715756).
- **Flag:** MOB_FORMATS_ENABLED=true (production, env id xJZ4QrcRIdcShmYI) after the Full mock together price enforcement went live; this commit's deploy picks it up. Off = set false and redeploy. MOB_LIVE_ENABLED stays unset until the owner turns off Supabase Realtime "Allow public access".

## 20 October 2026, night IST: website release 15 integrated on web/1020-v15-release (cut from main 85c71575): full mock together price, referral any practice, Mob hours, production egress cuts, and v3.fix. NOT deployed, no migration applied
- **Merged (each --no-ff, in this order):** web/1020-mob-fulltogether-price 185eaaf2b (merge 557adccf0, no conflict), web/1020-referral-any dabbf31d6 (merge a433f610b, no conflict), web/1020-mob-hours 25940b5f6 (merge e4f6c38b8; conflicts: docs/brain/APP-API-CONTRACT.md add/add, resolved by keeping the full contract and adding the hours stub as section 2.13, and package.json test:mob, both new test files kept), web/1020-egress in two merges: up to 8e5d00430 (3ad24989d; conflict package.json test:mob, all kept) and its STOP POINT d8c35687e (e7a25c437). web/1020-consent-d183 e4aae0fe9 (D183 review fixes, on top of 571041531) was first skipped because its worktree had uncommitted edits; once the writer committed and the worktree was clean it was merged last (merge 2c71cb810, no conflict; ProfilePageClient.jsx merged cleanly; its migration 20261020160000_usage_consent_d183 and undo came with it, not applied).
- **Egress review (the last workflow stopped in its fix stage):** all 18 commits before the STOP POINT pass their suites unchanged and were kept. The STOP POINT commit was merged separately and reviewed: its own review test file (egress_review.test.mjs, in no script) failed 4 of 20: one real gap (attemptMemoKeyFor looked only at listed supersets, so a limited read after a whole read of the same profile hit the database again; fixed in data/attempt_reads.js), two test faults (a reference read counted in the call log it asserted on; Array.sort on a frozen array) and one over-tight size bar (insights against history 0.6, 0.63 measured on short fixture stems, now 0.75; the one-tenth-of-a-row and half-of-summary bars stay). Now 20 of 20, including the real SQL on PGlite, and the file is in test:egress. egress_lean.test.mjs still expected the old summary profile on six routes and now expects insights. Nothing was dropped: the verdict cache, the insights, record and insights_strict profiles, the exposures reads, the byte-bounded row cache and the inventory digest all have passing parity or byte tests; every new database function falls back to the old read when it is missing.
- **Migrations in apply order (none applied; each has an undo in supabase/undo):** 20261020150000_attempts_lean_fn (egress), 20261020150100_attempt_question_ids_fn (egress), 20261020150200_referral_any_practice (renamed from 150000, which attempts_lean_fn holds), 20261020151000_mob_hours (renamed from 150000), 20261020152000_mob_den_fix (new, for v3.fix), 20261020160100_inventory_content_digest_fn (renamed from 160000 so the D183 migration 20261020160000_usage_consent_d183 keeps its version). The D183 migration 20261020160000_usage_consent_d183 (undo supabase/undo/20261020160000_usage_consent_d183.undo.sql, apply it before or with the route that accepts Rather not say with usage data on) is also merged and sorts before the digest (160100); none of these migrations depends on another. Seven new migrations, none applied, no staging or production dry run. Pre-existing and untouched: 20261013170000 is used by two files on main (app_service_role_grants, nta_paper_shortfalls).
- **v3.fix (APP-API-CONTRACT 2.14):** den `v3.fix = { gameId, question (1-based), state ready|check, checkOpensAt }` from the Mob's real traps, absent when nothing is left for the member. One small read per den (public.mob_den_fix), after the settle loop that makes the traps, no call for a Mob of one; absent migration or a failed read leaves the key out. `check` is sent only inside the trap's own Wednesday window (the server really has the check: mob_traps.check_opens_at and check_closes_at, mob_fix_checks stage check). The card is read from the traps, not from the den's games[] (7 days), because a window lasts up to 14.
- **Review fixes (23b198625):** (1) a den function whose migration is not applied (mob_den_fix, mob_hours_head, mob_hours_rows) answers not found once and is then not asked again for 5 minutes by that server process (src/lib/server/mob/missing.js, the rule attempt_reads.js uses), so a den read before 151000 and 152000 no longer makes calls that always fail; once a migration is applied a running server notices within 5 minutes. (2) attempt_question_ids (150100) takes a question's family from familyId or, when missing or empty, evidence.record.family_id, as the old recovery and replay read did; new PGlite test. (3) mob_den_fix (152000) filters on the member's own answers before its limit of 5, so five newer finished traps never hide an older open one; new test with 7 traps. (4) The MOCK_PRO_REQUIRED and MOCK_CREDITS sentences (server and web den) are built from MOCK_SIT_CREDITS; a test ties all four to it. (5) The consent merge, above.
- **Checks on the head after the review fixes and the consent merge:** test:mob 351/351, test:billing 453/453, test:app 979 tests (978 pass, 1 skipped; includes usage_consent), test:auth 125/125, test:recovery 640 (637 pass, 3 todo), test:egress 101/101, test:health-egress 56/56, test:attempt-reads 12/12, test:nta 229, test:learning 357, test:today 120, test:subjects 38, test:dock 56 (55 pass, 1 skipped), test:community 11, test:du 42, test:least-privilege 12, test:health-auth-board 10, test:answer-integrity 11, test:goal-minutes 23, test:question-reorder 26 (25 pass, 1 skipped), test:authored-publish 159 (155 pass, 4 skipped), test:factory 332/332; test:study 62 tests, 61 pass, 1 FAIL (study_content.test.mjs, the content gate reports wordnet LICENSE_UNAVAILABLE): the same single failure on a clean origin/main 85c715756, so it is pre-existing. next build --webpack exit 0, no warnings. No network call was made to Supabase.
- **Open:** the web den does not draw the fix card (the app does); the fix routes (where the app's card leads) still load the full question rows through the stamp cache, not the light columns; staging and production dry runs of the seven new migrations are not done; den steps 2 and 3 (v3.fix) and Mob hours are live only after 20261020152000 and 20261020151000 are applied (then within 5 minutes per server); the attempt_question_ids family rule should be compared on staging with the old read for a few real students before 150100 is applied.

## 20 October 2026, evening IST: Full mock together price enforced on the web server (owner D174, D175) on web/1020-mob-fulltogether-price. NOT deployed, no migration
- **Rule as built:** only a Pro member starts a Full mock together, with PLAY_BILLING_ENABLED on or off (src/lib/mob/starts.mjs startRight, code MOCK_PRO_REQUIRED, 403, detail with the price). A Free member pays 50 credits to sit it, charged when the sitting starts (POST /api/mob/paper/start { mob, game }), never on joining or opening the card; Pro sits free; no free first full mock (a Mob paper never takes it). Too few credits: MOCK_CREDITS (402) with { costCredits, sitCredits, proSitsFree }.
- **Charge path (no new ledger):** the Mob service passes mobPaper.creditAction 'attempt_full' for a Free sitter (service.js startMock); practiceCharge charges it exactly as a solo Full mock (data/practice_charge.js), so the existing spend_credits / start_learning_session charge it under practice_<id> / recovery:<id>. The session id comes from a key fixed per game and member, so a retry or resume is never charged twice. Every refusal runs before the charge; a durable start charges in the same transaction as the session, so a failed start takes nothing (there is no separate practice refund path, and none was added).
- **Payload:** den starts.mock { costCredits, sitCredits, proRequiredToStart, canStart, proSitsFree }; every mock game's price { costCredits, sitCredits, proSitsFree }. Contract: docs/brain/APP-API-CONTRACT.md section 2.12 (file taken from feat/app-and-web, where it lives, plus the new section: expect an add/add merge with only that section different).
- **Web:** Start a game sheet shows the locked Full mock together row with the 50-credit line and a Get Pro link (/pricing); a Pro host sees who pays what; the game card shows the price, "Sit the full mock for 50 credits" and "Sit free with Pro"; the runner answers MOCK_CREDITS with Add credits (/wallet), Get Pro, Back to your Mob. Not rendered in a browser (no dev server by rule): wiring checked by tests and the build only.
- **Behaviour change to note:** with billing OFF a Free member can no longer start a Full mock together (before: anyone could). Everything else under billing off is unchanged.
- **Checks:** new data/tests/mob_full_together_1020.test.mjs 8/8 (Mob service on the real Mob migrations plus the real credits ledger on PGlite) and data/tests/full_together_charge_1020.test.mjs 5/5 (practiceCharge, spend_credits, start_learning_session); test:mob 308/308, test:billing 448/448, test:app 962 pass 1 skipped, test:auth 125/125, test:recovery 636 pass 3 todo; eslint clean on the touched files; next build --webpack exit 0 (placeholder env, build command only). Contract fixtures regenerated (mob errors_v1, mob_v3 errors_v3, starts_*, den_get*, game_*mock*, paper_start_mock).

## 20 October 2026, about 3:30 pm IST: web release 3 is LIVE on production (main fb1e22e5): Mob explainer and setup (D166), Mob formats server and web client (D167) with MOB_FORMATS_ENABLED and MOB_LIVE_ENABLED both OFF, free first full mock off (D175), two Mob migrations applied with undo
- **What is live (web):** the Mob explainer (7 slides, replay row, the invite page leads with Join <Mob name>) and the one-question-per-screen setup (web/1020-mob-explainer c4546a70, D166/D168/D169); the Start a game sheet code with the race and Full mock together rows, and live presence through the server (web/1020-mob-formats-web 35c32bf8 and web/1020-mob-formats 757c5fdd, D167). The new formats and live rooms sit behind their switches, so students see the same four ways to play as before; the formats code is dormant until the flag is on. D175 (owner, 3:25 pm): the free first full mock per subject is OFF (FIRST_FULL_MOCK_ENABLED=false, Vercel Production env aldFAoz9qJXBPpAQ).
- **Merged (each --no-ff into web/1020-release3 from main 024a889a):** mob-explainer c4546a70, mob-formats 757c5fdd, mob-formats-web 35c32bf8. One conflict: package.json test:mob (kept both new test files, mob_v3_formats and mob_explainer_1020). denCopy.mjs overlapped without a conflict (both sides kept). One merge fixup (fb1e22e5): the explainer truth-table test matched the old rematch source text; the claim still holds (a sprint or round rematch keeps length and chapter, a race keeps its minutes), so the regex now matches the merged code.
- **Flags (the safe state):** MOB_FORMATS_ENABLED UNSET and MOB_LIVE_ENABLED UNSET in Vercel Production (checked in the env list before the push). **MOB_FORMATS_ENABLED stays off until the Full mock together pricing rule is decided and the server enforces it** (main session, 3:15 pm): as built, every Mob member can sit Full mock together for free, so one Pro friend could hand the whole Mob a free full mock every day, a credits loophole the owner has not ruled on. Do not set the flag before that. MOB_LIVE_ENABLED also stays off: the owner turns OFF Supabase Realtime "Allow public access" (Dashboard > Realtime > Settings) first, and the app client has to ship.
- **Checks on fb1e22e5:** lint exit 0; next build --webpack exit 0; test:mob 300/300 (the F-10 contract test "the client reads the server's race and mock bodies" runs against the server fixtures and passes), test:app 962 pass 1 skipped, test:billing 435/435, test:auth 125/125, test:recovery 636 pass 3 todo.
- **Visual check (dev build, headless, 390 and 1440, Night and Day; screenshots opened and judged):** the explainer (all 7 slides, the setup name step, D0), the Start a game sheet (Pro member: all four rows open; Free member: Full mock together carries the Pro tag, the Live tab is gated with its sentence), and /preview/mob-live (lobby and the live race). No horizontal overflow and no page errors in any of the 56 captures. One note, not a blocker (live is off): at 390 the live race ruler's first runner label ("Kabir") is clipped at the left edge at the start line; a small polish item for the live client.
- **Deploy:** `git push origin HEAD:main` 024a889a..fb1e22e5 (fast-forward; main had not moved). First build dpl_5vaeYem2qMmmB6FvXwxN58iQ7Zdb READY (it started before D175's env var, so it still showed the free first full mock). Redeploy from the same commit with the env var: **dpl_2juF25MkVrVzCqrWFMXDwiGMHjBP READY about 3:24 pm IST, aliased to www.mockmob.in and mockmob.in**. **Rollback point:** dpl_E72LNC2t28hENMADCZrDBSpFL1ub (024a889a, referrals live) via Vercel promote or request_rollback; the migrations can stay (see Rollback).
- **Migrations (owner's standing grant), applied on isrxrxzjocewrdureyhp with the Supabase MCP, in order:** (1) supabase/migrations/20261020100400_mob_v3_live.sql as `mob_v3_live` (recorded 20261020095603), the SQL from the first statement on (header comment left out); undo supabase/undo/20261020100400_mob_v3_live.undo.sql. (2) supabase/migrations/20261020140000_mob_v3_formats.sql as `mob_v3_formats` (recorded 20261020095712), the same way; undo supabase/undo/20261020140000_mob_v3_formats.undo.sql (run it BEFORE the live undo). Both were dry-run on staging onwkqxmjqjrhfbjjdydu by the builders (see the 3:15 pm entry below).
- **Production pre-check (SELECT only, before the apply):** neither migration in list_migrations (the last was 20261020083309); no mob_live_open, mob_room_tidy, mob_room_roster, mob_room_presence or mob_game_open_v2; no mob_private schema; none of the five new columns; mob_games, mob_game_runs and mob_game_answers had 0 rows; the old checks mob_games_format_check, mob_games_question_ids_check and mob_game_answers_q_check present; the Realtime policies mob_room_presence (INSERT) and mob_room_receive (SELECT, public.mob_room_ok) present; helpers mob_room_send, mob_room_maybe_done, mob_quest_tick, mob_ist_week and the table mob_data_moves present.
- **Production post-check:** all 18 function bodies match the files (md5 of prosrc equals md5 of the body between the dollar quotes in the two migration files: mob_room_tidy 6ff91659, mob_live_open 85bd3413, mob_room_ticket 6aa71b35, mob_room_start 50848d89 (the formats version), mob_room_cancel 5ccfbf84, mob_game_secs f316e841, mob_run_seal 1e6511c4, mob_game_open_v2 7096ca62, mob_live_open_v2 807523d0, mob_run_start 5a04af73, mob_game_answer aa94dd91, mob_mock_begin e16d9321, mob_mock_record 51bbe4d2, mob_game_json afd1263b, mob_game_settle de10455e, mob_room_roster 96943794, mob_room_presence 02149728, mob_private.mob_room_ok d6880435); every public function holds EXECUTE for postgres and service_role only (public.mob_room_ok lost authenticated; mob_private.mob_room_ok keeps authenticated because the Realtime policy runs as that role); RLS on for mob_games, mob_game_runs, mob_game_answers and mob_room_tickets, table grants only postgres and service_role, no policies on them; Realtime now has only mob_room_receive (SELECT, mob_private.mob_room_ok) and the client presence INSERT policy is gone; constraints mob_games_format_v2, mob_games_ids_v2, mob_games_shape_v2, mob_game_answers_q_v2 and mob_room_tickets_presence_v2 present and the three old checks dropped with their names recorded in mob_data_moves (formats_check:format, :ids, :q) for the undo; columns minutes, sheet, session_id, presence and seen_at present; index mob_games_room_live_idx present; games, runs and answers still 0 rows (no data was touched).
- **Smoke, no sign-in, after the first build and again after the redeploy:** curl 200 on /, /mob, /pricing, /wallet, /join/TEST, /cuet, /privacy, /login, /signup, /cuet/accountancy and /help; signed-out Mob APIs 401 (GET /api/mob, /shelf, /history, /game/<id>, /game/<id>/podium; POST /api/mob, /game, /paper/start, /game/<id>/answer, /room/ticket, /room/start, /room/presence), 405 on GET to the POST-only /invite, /seen and /me, and /api/mob/live is 404; get_runtime_errors empty over 20 and 15 minutes.
- **D175, free first full mock off (confirmed on the live site):** /pricing no longer lists "Your first full mock in every subject is free" (3 matches in the first build, 0 on the live redeploy); no public page says a first full mock is free (/, /pricing, /wallet, /help, /features, /cuet and /mob checked). With the switch off the quote route reads nothing and the quote carries no rule field, so no freeReason is sent, and the start route charges every Full mock (data/first_full_mock.js, src/app/api/practice/quote/route.js; the Wallet and in-app lines read FIRST_FULL_MOCK_ON). The signed-in quote itself was not called (no sign-in on production). **Rollback of D175:** delete FIRST_FULL_MOCK_ENABLED in Vercel Production (or set it to anything but false) and redeploy, because next.config.mjs puts it into the builds.
- **Rollback, in order:** (1) nothing needs switching: both format and live switches are unset, so students cannot reach a race, a Full mock together or a live room. (2) Code back: Vercel promote dpl_E72LNC2t28hENMADCZrDBSpFL1ub (or request_rollback); the old code should run on the new schema (same function names and signatures, returns only gain keys, mob_game_open and public.mob_room_ok still exist; not tried against the old build). (3) Schema back, only if needed: run supabase/undo/20261020140000_mob_v3_formats.undo.sql, then supabase/undo/20261020100400_mob_v3_live.undo.sql (it restores the 20261020100300 bodies and the presence insert policy). Games, runs and answers were empty at the apply, so no data needs moving.
- **Owner steps still open:** (a) decide the Full mock together pricing rule (who can start it, and what a Mob member who is not Pro pays or gets); the server must enforce it before MOB_FORMATS_ENABLED=true. (b) For live: Supabase Dashboard > Realtime > Settings > turn OFF "Allow public access", then the app client ships, then MOB_LIVE_ENABLED. (c) Nothing else is required for this release.

## 20 October 2026, about 3:15 pm IST: Mob formats server (D167) built on web/1020-mob-formats: timed races, Full mock together, live-room fixes (L-55). NOT deployed; staging only
- **Race (format race, 5 or 10 minutes):** one frozen pool (6 a minute, at least 4) the same for everyone in the same order, served ONE question at a time (an answer must be for the next question; the next comes back with the answer); the clock is the server's (starts at /run, a live race at the room's Go; an answer counts until the end + 2 s; time never passes the minutes); unserved questions are not skips; CUET marks; ghosts from per-answer server times; ties share a place; moments most_answered and raced.
- **Full mock together (format mock):** one 50-question CUET paper (full-mock selector), open 24 hours, sat in the practice runner through POST /api/mob/paper/start { mob, game } (mode full, 60 minutes, no credits, never the free first full mock), answers held until the game closes (mobPaper.gameId + holdUntil, held kind "mock"); the hand-in is recorded on the game (finish hook, or the next read for the durable path); the podium adds full mark sheets (marks of 250, right, wrong, skipped, accuracy, server time, syllabus-unit sections; private members hidden); after close Fix it together takes the most-missed question; it ticks the quest. Pro starts it with billing on (starts.locked); a passed mic never opens it.
- **Every game (web-security 20 Oct #1, #2):** a run never ends after the close, an answer at the close is refused, open runs are sealed before the review; a new game never draws a question of an open game, the held weekly paper or an open extra (nor, when the bank allows, one closed in the last 7 days), and a review withholds a key that sits in another open game or held paper.
- **Live (L-55, web-security #7, L-60):** the client presence insert policy is dropped (clients write nothing on a room channel); POST /api/mob/game/[id]/room/presence { st: here|ready|left } with a 20 s heartbeat, server broadcast presence { m, st }, roster [{ memberId, st }] on the ticket and the game view (45 s); the Realtime check is mob_private.mob_room_ok (public.mob_room_ok no longer callable by authenticated; the advisor finding is gone on staging); live refusal sentences say "to play any time in the next 24 hours".
- **Migration:** supabase/migrations/20261020140000_mob_v3_formats.sql (needs 20261020100400 first), undo supabase/undo/20261020140000_mob_v3_formats.undo.sql. Staging onwkqxmjqjrhfbjjdydu: pre-snapshot 704b029d (460 objects: mob functions with ACLs, checks, columns, Realtime policies); applied; smoke in a rolled-back transaction found a check that let a race with no minutes through (null passes a CHECK), fixed with coalesce plus a test; undo gave back 704b029d exactly; re-applied (mob_v3_formats_20261020140000_staging_reapply): the 14 functions hash dda5ecae and the v2 checks b23f19b1, both equal to the repo files on PGlite; second smoke all as expected. Staging stays ON the migration.
- **Checks (head of the branch):** data/tests/mob_v3_formats.test.mjs 25/25 (in test:mob); lint exit 0; test:mob 275/275, test:app 962 pass 1 skipped, test:billing 435/435, test:recovery 636 pass 3 todo; next build --webpack exit 0. Contract: data/tests/fixtures/mob_v3 (57 files, 23 new, older ones regenerated with additive keys).
- **Production read-only check (3:05 pm):** mob_games_format_check, mob_games_question_ids_check, mob_game_answers_q_check (standard names, found by definition anyway); 20261020100400 not applied; the 100300 presence insert policy is still there (harmless while no ticket is issued). Supabase org plan: free (200 Realtime connections; MOB_LIVE_MAX_ROOMS 30 = 150).
- **Order for production (owner's grant; main session):** (1) deploy the code with MOB_FORMATS_ENABLED and MOB_LIVE_ENABLED unset (safe before the migrations: question games fall back to mob_game_open); (2) apply 20261020100400_mob_v3_live, then 20261020140000_mob_v3_formats; (3) MOB_FORMATS_ENABLED=true and redeploy; (4) live: the owner turns OFF Realtime "Allow public access" (Dashboard > mockmob > Realtime > Settings), the web and app clients that use the presence route (never channel.track()) ship, then MOB_LIVE_ENABLED=true. Undo: flags off, then the 140000 undo, then the 100400 undo (loses race and mock games).

## 20 October 2026, about 2:10 pm IST: referral credits and the 50-credit welcome (D165) are LIVE on production (main 2ffaf29d, REFERRALS_ENABLED=true; D156 and the standing migration grant)
- **What is live:** a new account starts with this month's 50 free credits only (users.credit_balance default 0); a friend who signs up through a friend's /r/<code> link, a typed code or a Mob invite link, and answers at least 5 questions (a finished practice or Mob game), earns +100 for the friend and +100 for the inviter, once, at most 10 friends per inviter per IST month, with the same-device, reused-device and same-network holds. Existing balances were not touched.
- **Deploy:** `git push origin HEAD:main` 36492ed2..2ffaf29d (fast-forward; main had not moved, so no merge and no rerun of the builder's suites: test file 26/26, billing 435, auth 125, mob 250, app 962, recovery 636, webpack build). Code first with the flag unset: dpl_Dxotnw4QbbratpnGpZbBycgL4dga READY about 2:01 pm IST. Flag on: REFERRALS_ENABLED=true set in Vercel Production (plain, env id yLb9Qkm9dvrNjm6s), then redeployed: dpl_GmV6rjynAJPULhWSU7yeZ1qu5jZv READY about 2:05 pm IST, aliased to www.mockmob.in and mockmob.in. **Rollback point for the code:** dpl_13vbidun9MJtWKaNPub88Hj5NfSY (main 36492ed2, before referrals).
- **Migration (standing grant):** supabase/migrations/20261020130000_referrals.sql applied on isrxrxzjocewrdureyhp with the Supabase MCP as `referrals_welcome_credits` (recorded 20261020083309, about 2:03 pm IST), SQL from the first statement on (the header comment block was left out). Staging dry run (onwkqxmjqjrhfbjjdydu, rolled back) was done by the builder, see the entry below. **Undo file:** supabase/undo/20261020130000_referrals.undo.sql (not applied).
- **Production pre-check (SELECT only, 1:59 pm IST):** users.credit_balance default 100; sum(credit_balance) 112311 over 1545 users, no null, no negative; no referral table, function or trigger; mob_game_runs present; credit_transactions has no check on action, a unique index on reference, type enum earn/spend/bonus; last migration 20261020044306.
- **Production post-check (2:06 pm IST):** default 0; sum(credit_balance) 112311 and 1545 users, unchanged (no credit_transactions rows and no new users in between, so the equality is exact); referral_program row reward 100, monthly_cap 10, grants_paused false; referrals 0 rows, referral_codes 0 rows; RLS on for the three tables, 0 policies, only postgres and service_role hold table grants (none for anon, authenticated or PUBLIC); 11 mm_referral_* functions, anon and authenticated cannot execute any, service_role can; triggers mm_referral_after_attempt (attempts) and mm_referral_after_mob_run (mob_game_runs) present; md5 of every function body in the database equals the md5 of its body in the migration file (11 of 11).
- **Smoke, no sign-in (flag off, then flag on):** / , /pricing, /wallet, /signup, /login, /mob, /privacy 200; /join/TEST 200 (invalid-code page); /r/TEST 307 to /signup with no cookie (TEST is not a valid code length); /api/referrals 401 and POST /api/referrals/claim 401 signed out. Flag on: /r/ABC2DEF 307 to /signup?invite=1 and sets mm_invite plus an HttpOnly mm_dev cookie (cookies only, no database write); /pricing carries "Invite a friend and you both get 100 credits once they finish a practice." get_runtime_errors: none in the 30 minutes after each deploy. No account was created and nobody signed in on the live site; the signed-in paths (claim, a real grant) are covered by the 26 PGlite tests and the staging dry run only, so the first real grant happens when a real friend qualifies.
- **Rollback, in order:** (1) pause payouts at once without a deploy: `update public.referral_program set grants_paused = true;` (qualified rows wait; `select public.mm_referral_grant_due();` pays them after); (2) flag off: delete REFERRALS_ENABLED in Vercel Production (or set it to anything but true) and redeploy, which stops capture, claims and every invite line; (3) code back, only if the code itself misbehaves: promote dpl_13vbidun9MJtWKaNPub88Hj5NfSY (main 36492ed2; its ensureUser writes credit_balance 100 explicitly, so new accounts get 150 again whatever the column default is; the referral tables and functions can stay); (4) database: run the undo file (drops the two triggers and the mm_referral_* functions, default back to 100, keeps every credit already paid and keeps the three tables once any referral was paid). Credits already paid are never taken back.
- **Owner:** nothing is required. Worth knowing: new accounts now see 50 credits, not 150; the app (ui/1020-referrals) is a separate track and claims only after sign-in with this API; the pricing line says "finish a practice" while the database rule is at least 5 answers.

## 20 October 2026, afternoon IST: referral credits and the 50-credit welcome (D165) built on web/1020-referrals (now LIVE: see the entry above)
- **Rules (owner D165):** a new account starts with this month's 50 free credits only (users.credit_balance DEFAULT 100 -> 0; data/db.js no longer writes 100; existing balances untouched). A referral pays BOTH the inviter and the friend +100 once the friend signs up and finishes one practice (>= 5 answers: an attempts row or a finished Mob game). The Mob invite link (/join/<code>) is also the referral link; a friend's own link is /r/<7-character code>, ?ref=<code> on any page but /pricing (creator codes), or a code typed at sign-up.
- **Migration:** supabase/migrations/20261020130000_referrals.sql (referral_program with reward 100, monthly_cap 10, grants_paused; referral_codes; referrals unique per referee, not self; mm_referral_attach/grant/qualify/status/grant_due; triggers on attempts and mob_game_runs; RLS on, service_role only). Credits go to users.credit_balance with credit_transactions references 'referral:<id>:friend|inviter' (idempotent), NOT bonus_credits, which count as bought and would lift the per-student AI cap. Holds: same device as the inviter, a device already paid on another account, a 4th friend from one network in a month. Undo: supabase/undo/20261020130000_referrals.undo.sql (default back to 100; paid credits stay).
- **Staging dry run (onwkqxmjqjrhfbjjdydu, one transaction raised to ROLL BACK):** the exact file, then the rules: new account 0, self refused, attach + replay idempotent, 3 answers no, 5 answers +100 each, grant replay idempotent, 2 ledger rows, an existing account refused, same device held, Mob invite attach and a finished Mob game paid, status counts only, no browser-role access, 46 existing users and 4,873 credits unchanged; all 11 function bodies' md5 equal the file's. After: no referral tables or functions, default still 100.
- **Checks:** data/tests/referrals_1020.test.mjs 26/26 (PGlite: every rule, the undo); lint exit 0; test:billing 435/435, test:auth 125/125, test:mob 250/250, test:app 962 pass 1 skipped, test:recovery 636 pass 3 todo; next build --webpack exit 0.
- **Switch:** REFERRALS_ENABLED=true (Vercel env, then redeploy). Off: no capture, no claim, GET /api/referrals answers live:false, no invite line anywhere. Kill switch for grants without a deploy: `update public.referral_program set grants_paused = true` (qualified rows wait; `select public.mm_referral_grant_due()` pays them after).
- **Order for production:** deploy the code with the switch off; apply the migration (standing grant); smoke; set REFERRALS_ENABLED=true and redeploy. App: ui/1020-referrals (claims after sign-in, /r/ App Link).

## 20 October 2026, about 11:00 am IST: web release 20 Oct (web/1020-release) is LIVE on production (main 5819163a), plus the daily-minutes migration (D156, standing grant)
- **Merged (each --no-ff into web/1020-release from 48985a8d, then live main b5199afe merged in):** goal-minutes fa635fc5 (30122258), web-goal-more eb37f6d5 (cd11144f), set-password c3dfc2b4 (274f0235), landing-health a68aba16 (e61eba1b), web-practice-parity 6f4dde82 (4c1ea372), web-onboarding-parity e22f7d34 (1f1b3d82), mob-polish 7bc2dd02 (e66726ac), join-v3 4a10d0f3 (65f45307), paper-hold 54ff19a5 (113db3d8), mob-live 6b0cf827 (843f30c2), web-live-client fbbb8433 (44c11f56), web-subject-pages 42e92940 (0dda9b0d; b2024553 plus one truth commit: the 9 new subjects read against NTA's CUET UG 2026 bulletin and syllabus PDFs, unsupported claims softened), live hotfixes web/1020-hotfix (e0acbac9) and main b5199afe (75ead0dd).
- **Conflicts kept both intents:** goal-minutes vs web-goal-more (shared DailyMinutes picker + server rules), package.json (union of test files in every script), OnboardingPageClient and getStudentAIContext imports, den CSS (.join-v3), /cuet/[subject] keeps its own share card, games.js imports (live.mjs + togetherLine), layout.js (theme + den skeleton script and the app-view script). Today order as both branches' tests lock it: greeting, the "Your colleges" strip inside the header, then the name card. Fix commits: 976f5cdf (goal test follows the merged card), 3c8be362 (least-privilege allows exactly liveChannel.js, with a guard), 332abb8f (comment).
- **Added in the release:** ba3444aa Folds shrug (12) and wave (11) stills in public/mob/folds from tmp/design-1019pm/mob-v3/characters/final/poses (same @256 webp export as idle/cheer/think; Stamp's wave hit the image limit and falls back to idle via FOLD_POSES_MISSING; a wrong answer in a game run now shows the shrug). 5819163a L-02 on the web: "2 real CUET questions" is now "2 new CUET-style questions" on /pricing (ONE_CREDIT_LINE), Help, wallet, Ask Mobi, subject pages, thread server lines and the model prompt; guard test in mobi_copy_1020.
- **Flags:** MOB_LIVE_ENABLED stays unset: the only reader is deps.js `=== 'true'`; the three room routes answer 409 LIVE_OFF before any RPC; /api/mob/live is 404 on production.
- **Checks on 5819163a:** lint exit 0; next build --webpack exit 0 (/, /privacy, /terms static; /cuet static 1h; /cuet/[subject] SSG 15 paths); test:app 962, test:mob 250, test:auth 125, test:recovery 636, test:subjects 38, test:goal-minutes 23, test:today 120, test:learning 357, test:factory 332, test:nta 188, test:du 42, test:dock 55, test:community 11 and the egress/least-privilege/answer-integrity/attempt-reads/health/question-reorder/authored-publish suites, all 0 fail. test:billing 408/409 once: billing_monthly_webhook "payment.captured after subscription.charged" differed by premiumUntil (a clock-second flake; 29/29 on three reruns, file untouched by this release). test:study 61/62: study_content LICENSE_UNAVAILABLE because WORDNET-LICENSE.txt is CRLF in Windows checkouts (fails on main too; passes with LF).
- **Visual check (dev build, headless, 390 and 1440, Night and Day; tmp/walk-1020/web-release2):** /, /pricing, /cuet, /cuet/physics, Today, Profile, Mob (arena preview and the v3 den preview), Wallet, the in-app join, /join/<code> (invalid-code state, MOB_ENABLED on): no horizontal overflow, no page errors; opened and judged. Notes, not blockers: Today shows the colleges strip at the top and the older "Your colleges" card lower down (some repetition); the app-view /pricing notice is plain.
- **Migration (owner's standing grant):** supabase/migrations/20261020110000_study_goal_daily_minutes.sql (one nullable smallint study_goals.daily_minutes + check 5 to 999). Dry run on STAGING onwkqxmjqjrhfbjjdydu at about 10:30 am, one transaction that raised to ROLL BACK: migration twice, 12 rows before and after, 12 null, 1 check, 4 and 1000 refused, 999 accepted, undo twice, 8 columns back. Production pre-check: 7 rows, 8 columns, no column, no check. Applied to PRODUCTION isrxrxzjocewrdureyhp after the code was live, recorded as 20261020044306 study_goal_daily_minutes; after: 7 rows, all null, 9 columns, the check present. **Undo:** supabase/undo/20261020110000_study_goal_daily_minutes.undo.sql (drops the check and the column; the code feature-detects it and falls back). NOT applied: 20261020100400_mob_v3_live.sql (only live-room routes use it; apply in the change that turns MOB_LIVE_ENABLED on, after the presence fix L-55).
- **Deploy:** `git push origin HEAD:main` b5199afe..5819163a (fast-forward). Vercel dpl_2DmM3U2em5PRcipjCJNdpq7mPSf2 READY, aliased to www.mockmob.in and mockmob.in. **Rollback point:** dpl_6uV9Z3cLWcFeHGcXcpBx85fJxn1M (b5199afe, hotfixes live) via Vercel promote or request_rollback; the migration can stay (additive) or be undone with the file above.
- **Production smoke (no sign-in):** curl 200 on /, /pricing, /privacy, /terms, /refunds, /mob, /wallet, /login, /signup, /help, /features, /cuet, /cuet/accountancy, /cuet/physics, /cuet/mathematics, /cuet/general-test, /cuet/english, /cuet-previous-year-questions, /join/K7P2M9, /dashboard, /profile, /account-deletion and the new shrug/wave stills; /api/mob, /api/mobi/standing, /api/me/goal and POST /api/ai/mentor/chat 401. Headless Chrome on live (390 and 1440 Night): no page errors on those pages (the join page's one 404 is the invalid code's lookup). get_runtime_errors: none.
- **For the app owner (not web):** L-07a add `from=app` to every Custom Tab URL; L-02 the app still says "2 real CUET questions" (copy.dart, ask_doors.dart, doubt_thread.dart, WalletCopy); copy_v3.dart shareMarksNote still says "The collective line still counts your answers" (untrue since L-10); L-01 app half can adopt `response.thread` from the server replay.

## 20 October 2026, about 10:20 am IST: live hotfixes L-08 (legal pages) and L-07b (no pricing in pages opened from the app) are LIVE (main 166129c1; D156)
- **L-08** web/1020-hf-legal 40502c2b: APP_STREAM_AND_REPORT_LIVE = true (the app version 13 stream events and Report this reply are now on /privacy; two details corrected to match the interact route). /privacy: the push-token claim is gone (the app has no push; reminders are scheduled on the phone), also removed from /account-deletion; Payments now names Razorpay on the website and Google Play Billing in the Android app (what is stored, Google holds the payment method, renewal cancelled before deletion, what deletion keeps); "Mobi job" replaced by plain words; dated 20 October 2026. MobLegal rewritten for Mob v3 from the code (games, CUET marks, podium and the owner's switch, ghosts as pace only, the share switch with the L-10 behaviour, trap, Fix it together, weekly paper, nudges, 8 fixed stickers kept 30 days, quest/chain/Folds, the mic, Leave and block with the L-09 behaviour, reports 180 days, deletion list); live rooms are not described (MOB_LIVE_ENABLED off: add them in the change that turns them on). /refunds and /terms cover Google Play billing (monthly Pro cancelled in Play, Play refunds follow Google's policy, a refunded Play purchase is taken back, deleting the account cancels renewal without refunding the month). No Play price printed.
- **L-07b** web/1020-hf-appview 71ec833e: a page opened with `?from=app` stores `sessionStorage['mm:appView']='1'` (per tab, never a cookie: Custom Tabs share Chrome's cookie jar) and sets `data-app-view` on `<html>` before paint; CSS then hides every link to /pricing, /upgrade, /checkout, /wallet, the Razorpay and credit-pack buttons and the home pricing section; /pricing, /pricing/ai-credits and /wallet show only "Plans and payments for the app are in the MockMob app." Normal visitors see no change; no route changed rendering mode (/, /privacy, /terms, /account-deletion still static). **App contract (L-07a, app owner):** add `from=app` to the first URL of every Custom Tab (e.g. https://www.mockmob.in/privacy?from=app); later pages in that tab need nothing.
- **Copy fix 166129c1:** the den's share switch note no longer says "The collective line still counts your answers" (untrue after L-10); the podium switch is the Mob owner's. **The app has the same untrue line** (flutter_app copy_v3.dart shareMarksNote): the app owner must change it before version 13 ships.
- **Tests:** legal_play_1020 (test:billing), mob_legal_v3_1020 (test:mob), app_view_1020 (test:app), 7 each. On 166129c1: lint exit 0; test:mob 184/184; test:billing 408/408; test:app 891 pass 0 fail; test:recovery 636/636; test:auth 114/114; test:subjects 30/30; next build --webpack exit 0. Headless screenshots (390/1440, Night/Day) in tmp/walk-1020/hf-appview, opened: no Pricing in app view, normal view unchanged.
- **No migration, no env change.**
- **Deploy:** `git push origin HEAD:main` d1d26132..166129c1 (fast-forward). Vercel dpl_Gr98Qz8QqReXbxNgMZ3TMnfjUT2r READY, aliased to www.mockmob.in. Smoke (curl, no sign-in): every public page 200, signed-out APIs 401; live /privacy, /refunds and /terms name Google Play, carry no push-token claim and no "never ranked", /privacy has the stream section and the v3 Mob section; /privacy?from=app carries the app-view script. get_runtime_errors: none in the 30 minutes after READY.
- **Owner, in Play Console (unchanged):** Data safety > Purchase history; content rating (digital purchases yes, users interact yes).
- **Undo:** redeploy dpl_DM5M9PoC6WUT1cVdQ2gprUj6Mhcm (d1d26132, wave 1 live) with Vercel promote or request_rollback. No database step.

## 20 October 2026, about 10:00 am IST: live hotfixes L-09, L-10 and L-01 (server) are LIVE on production (main 792c8c61; D156)
- **What went live (each on its own branch from 48985a8d, merged as web/1020-hotfix):**
  - **L-09** web/1020-hf-block 174ef9b8: Leave and block (and a report with block) now separates the two students in EVERY Mob they share, in the same request. In a Mob the blocker owns the blocked member is removed (the owner keeps the Mob); in any other the blocker leaves. mob_join already refuses a block either way, so they never share a Mob again. The response adds `separatedMobs` when above 0. No migration (uses mob_state, mob_remove, mob_leave).
  - **L-10** web/1020-hf-share 19a48c9e: "Share my marks" off no longer leaks results in Mob games. A private run (not the viewer's own) gets only the "finished" moment (no All N right, No minus, fastest, three in a row), is left out of the "together" line (togetherLine: `of` counts only the runs summed, so the sum cannot be subtracted to get a private count), and is never a ghost for others. The member's own view is unchanged.
  - **L-01 server** web/1020-hf-doubt 42ee2844: a paid doubt whose reply was lost is replayed on retry with the same requestId (threadStore.findOpened by the persisted reply's charge reference, else metadata.thread.openKey; always scoped to the student): the reply, the thread as it stands, its 2 questions and any answers, as a 200 with `replayed: true`, runtimeState 'replayed'. No second charge, no second model call, nothing stored again. A duplicate reserve (retry racing the first write) replays too. Also web-mobi #1: a later free ask in the same panel no longer wipes the thread's metadata (chat persist and /api/ai/mentor/local keep metadata.thread). App note: the app's retry now gets the thread back; the app half (L-01 _recover/_adoptThread) can adopt `response.thread`.
- **Tests:** new L-09 test and two L-10 tests in mob_v3.test.mjs (the L-09 and the L-10 service tests fail on 48985a8d), four L-01 tests in mobi_doubt_thread.test.mjs. On 792c8c61: lint exit 0; test:mob 177/177; test:recovery 636/636; test:app 884 pass 0 fail; test:billing 401/401; test:auth 114/114; test:subjects 30/30; next build --webpack exit 0 (one earlier attempt failed fetching Google Fonts, a network blip; the retry passed).
- **No migration, no env change.**
- **Deploy:** `git push origin HEAD:main` 48985a8d..792c8c61 (fast-forward). Vercel dpl_5YWmq8gsTaMy27EW7V2w62GL5ws8 READY, aliased to www.mockmob.in and mockmob.in.
- **Production smoke (curl, no sign-in):** /, /pricing, /privacy, /terms, /refunds, /mob, /wallet, /login, /signup, /help, /features, /cuet/accountancy, /cuet-previous-year-questions, /join/K7P2M9, /dashboard, /profile, /account-deletion all 200; /api/mob, /api/mobi/standing, /api/me/goal and POST /api/ai/mentor/chat 401. get_runtime_errors: none in the 20 minutes after READY.
- **Not done here:** L-08 legal pages and L-07b (app view without pricing) follow in their own deploy; the app half of L-01 is the app owner's.
- **Undo:** redeploy dpl_KN3JmVqupBfxFYWABbjEQGDQe8Tj (48985a8d) with Vercel promote or request_rollback. No database step.

## 20 October 2026, about 3:25 am IST: Ask Mobi v13 value is LIVE on production (main e789ffcc; owner D157, D156)
- **What went live:** web/v13-mobi (3e380817, 5 commits on 55bcbad0) merged into web/v13-release as d9891541, plus e789ffcc. Mobi charges for finished jobs, never for talking: Where you stand (GET /api/mobi/standing) and "What should I revise tonight?" are free and make no model call; a doubt thread is 1 credit (answer, 1 follow-up, 2 verified unseen bank questions via /api/mobi/thread); Fix it for good is 1 credit (second fresh check, held, the student's own trap history); Mobi's context now reads My colleges and their 2026 Round 1 cutoffs. The 3-credit "deeper analysis" is gone from pricing, privacy, Help, the assistant, the wallet and CREDIT_COSTS.
- **Merge notes:** conflicts only in package.json (test:billing keeps money_v13_1020 and mobi_copy_1020; test:recovery and test:app auto-merged with every test file) and STATUS.md (all entries kept). One semantic break the merge hid: main's wallet price list (money_v13_1020) still had a "Deeper analysis, 3 credits" row and imported DEEP_AI_CREDITS, which the Mobi side had removed from creditCopy.mjs. e789ffcc removes the row and the import, updates the money test, and mobi_copy_1020 now fails on any import of a name creditCopy does not export.
- **Rules verified in code and tests (D157, C-dec 3b):** Pro does not make Mobi free (no plan branch in the thread, standing, tonight or thread-store code; the reserve is the same wallet for everyone; test added); every Mobi job is 1 credit on every plan (THREAD_CREDIT_COST 1, repair 1, CREDIT_COSTS 1); things read from the record are free (standing, tonight, the follow-up and checks take no wallet); no charge on failure (a failed opening releases the credit and closes the thread, a failed follow-up gives its slot back, an unreadable bank offers nothing and charges nothing extra); budget caps untouched (no change to runtime_ai_budget, the per-student cap or providers; the follow-up still runs under the runtime guard and the per-student cap); only gpt-6-luna and claude-haiku-5-5 (no Mobi file names a model; test added).
- **Checks at e789ffcc:** eslint on 59 changed files exit 0; test:mob 174/174; test:billing 401/401; test:recovery 635 (632 pass, 3 todo, 0 fail); test:auth 114/114; test:app 885 (884 pass, 1 skipped, 0 fail); test:subjects 30/30; test:learning 357/357 (the AI cap, provider and repair suites); test:today 120/120; test:du 42/42; test:dock 56 (55 pass, 1 skipped); next build --webpack exit 0 (.next removed). No test calls a real model.
- **No migration:** no file under supabase/migrations differs from origin/main (checked before the push); nothing applied to production; no env change.
- **Deploy:** `git push origin HEAD:main` 65afa5d0..e789ffcc (fast-forward). Vercel dpl_GNLLoKcKYZDo34nkpXbqMqnT5WSs READY at about 3:25 am IST, aliased to www.mockmob.in and mockmob.in. Rollback point: dpl_4nA9juLKE9wFKjPHRAcdtfx7Ffha (65afa5d0, web v13 + Mob v3).
- **Production smoke (curl, no sign-in):** / , /mentor, /pricing, /wallet, /mob, /today, /api/stats all 200; /api/mobi/standing, /api/mobi/thread (GET and POST), POST /api/ai/mentor/chat, /api/recovery/check and POST /api/recovery/repair answer 401; /pricing carries the new one-credit line. get_runtime_errors: none in the 5 minutes after READY (and none in the 30 minutes before the final check).
- **Not done:** no signed-in walk of the live Mobi flows (no sign-in by agents; the paid doubt-thread and Fix it for good paths are tested with fakes only, so the first real model call happens when a student uses them); the app side of Mobi v13 is a separate track.
- **Undo:** redeploy dpl_4nA9juLKE9wFKjPHRAcdtfx7Ffha (Vercel promote or request_rollback). No database step to undo.

## 20 October 2026, about 3:10 am IST: website v13 and the Mob v3 database are LIVE on production (main 9936793c; owner D152, D156)
- **His words (D152):** "yes ... for both": the 4 Mob v3 production migrations and deploying the website with the Mob v3 switch on. D156: decide independently.
- **Re-verified before the push:** wt-1020-web-rel clean at 9936793c; origin/main still 58793f9c and an ancestor (fast-forward, 29 commits); test:mob 174/174, test:billing 396/396.
- **Production pre-check (isrxrxzjocewrdureyhp, SELECT only):** 15 mob tables (RLS on), 24 mob functions; mob_invites 8-character check named `mob_invites_code_check` (plus max_uses and uses checks); mobs 0, mob_members 0, mob_invites 0; no v3 table; no realtime.messages policy; last migration play_subscriptions.
- **Migrations applied in order with the Supabase MCP (exact file SQL):** mob_v3_core (recorded 20261019213134), mob_v3_games (20261019213350), mob_v3_chains (20261019213446), mob_v3_realtime (20261019213528). Post-checks after each:
  - core: 5 tables RLS on; `mob_invites_code_check` dropped and recorded in mob_data_moves (`v3_code_check:mob_invites_code_check`); `mob_invites_code_len` takes 6 or 8 characters; mobs.name_key and show_podium added; 9 functions security invoker, not executable by anon or authenticated.
  - games: 9 tables RLS on; 23 functions present; no anon or authenticated grant or policy.
  - chains: 3 tables RLS on; 9 functions present; none executable by anon or authenticated.
  - realtime: mob_room_tickets RLS on; realtime.messages policies mob_room_receive (SELECT) and mob_room_presence (INSERT), both for authenticated; mob_room_ok security definer with search_path "" (the only one; anon false, authenticated true, by design); triggers mob_room_revoke (mob_members) and mob_room_revoke_block (mob_blocks).
  - Totals: 18 v3 tables RLS on; 0 policies on any public mob, chain or fold table; no public mob/chain/fold function executable by anon.
  - Exactness: the 47 v3 function definitions (md5 37f0318c...), the v3 table constraints (b4991962...) and the two realtime policies (8ceb10c7...) hash identically on production and staging.
- **Security advisor:** nothing new. INFO rls_enabled_no_policy (by design, now including the 18 v3 tables); WARN mob_room_ok executable by authenticated (expected, spec 2.4); WARN leaked password protection (an older Auth setting, not this change).
- **Vercel:** MOB_V3_ENABLED=true added (plain, Production only). MOB_LIVE_ENABLED stays unset (Phase B); the Realtime "Allow public access" switch is still the owner's Phase B step. No other env var changed.
- **Deploy:** `git push origin HEAD:main` 58793f9c..9936793c (fast-forward). Vercel dpl_6jwcAvFQxtZGSWmnUoL1FV6R7RBu READY at about 3:08 am IST, aliased to www.mockmob.in and mockmob.in. Rollback point: dpl_F8qxHxpnXyZPqjCEAFrPrBbSnE9L (58793f9c).
- **Production smoke (curl, no sign-in):** / 200, /pricing 200, /wallet 200, /mob 200, /api/stats 200, /api/mob 401 (UNAUTHENTICATED), POST /api/billing/play/verify 401, /.well-known/assetlinks.json 200. Runtime errors since the push: none; the new deployment's logs show info only. Read-only DB: mobs 0, mob_members 0, mob_invites 0, mob_games 0 (no Mob had been made on production yet, so no existing Mob data to break).
- **Open item, not a v13 change:** assetlinks.json answers `[]` because ANDROID_CERT_SHA256 is not set in Vercel. App Links stay off until the owner pastes the Play app-signing SHA-256 there and redeploys.
- **Undo:** first MOB_V3_ENABLED off (delete it or set it to anything but "true") and redeploy (or roll back to dpl_F8qxHxpnXyZPqjCEAFrPrBbSnE9L); then the undo files in reverse order: `supabase/undo/20261020100300_mob_v3_realtime.undo.sql`, `..100200_mob_v3_chains.undo.sql`, `..100100_mob_v3_games.undo.sql`, `..100000_mob_v3_core.undo.sql`. The undo loses all v3 data (games, quests, Folds, chain settings); core puts the 8-character check back under the name recorded in mob_data_moves.

## 20 October 2026, IST: Ask Mobi v13 value (C-dec 3 + 3b, D157) built on web/v13-mobi (local, not pushed, not deployed, nothing applied to production)
- **Rule:** Mobi charges for finished jobs, never for talking; 1 credit a job on every plan (Pro does not make Mobi free, C-dec 3b); what is read from the record is free.
- **Free, no model:** GET /api/mobi/standing (range vs My colleges' 2026 Round 1 closing marks, gap, 2-3 chapters that close it; was Compass Pro); "What should I revise tonight?" (rules from repairs, traps, due Revise cards, costliest chapters).
- **Doubt thread (1 credit):** POST /api/ai/mentor/chat opens a thread (mentor_sessions.metadata.thread): answer + 1 follow-up (free, 500-token cap, still under the runtime guard and the per-student cap) + 2 verified unseen bank questions on the chapter, marked by /api/mobi/thread. Nothing charged on any failure.
- **Fix it for good (1 credit):** repair response carries `mobi` (your pick, key, trap, the student's own trap history); /api/recovery/check slot 2 = a second fresh question (receipt.offered2/check2); held = every check right.
- **Context:** getStudentAIContext reads My colleges + cutoffs (targetColleges, collegeStanding); the 12 KB cap drops lower-value parts first; the old chance-label Compass summary is left out when the standing exists.
- **Copy:** the 3-credit "deeper analysis" is gone (pricing, privacy, Help, assistant, ONE_CREDIT_LINE, CREDIT_COSTS).
- **Cost per job (luna $0.10/M in, $0.50/M out; production measurement 17 Oct):** Fix it for good about Rs 0.027 (max Rs 0.042); doubt thread about Rs 0.05 (worst about Rs 0.08 with its follow-up); standing, tonight and the check questions Rs 0. One credit = Rs 0.163 (web 300 pack) or Rs 0.25 (Play).
- **No migration needed.** next.config traces public/du/2026/offerings into /api/mobi/standing and /api/ai/mentor/chat.

## 20 October 2026, early hours IST: website release v13 integrated on web/v13-release (local; NOT deployed yet; nothing applied to production)
- **What is in it (git merge --no-ff, in this order, on web/1019pm-mob-v3 e2eb2462 = Mob v3 server + live main 58793f9c + the v3Available flag):** web/1020-fixes (app sign-in link page /app/login, assetlinks from ANDROID_CERT_SHA256, no email prefix as a name); web/v13-mob-den (the web den, start, join, sheets, chains, shelf, moments, public/mob art); web/v13-mob-play (playing a game, podium, moments, Fix it together); web/v13-money afea69dd (Pro page outcome moments, wallet packs as Mobi answers and mistake repairs); then the Fold catalog colours from the final art.
- **Integration decisions:** one v3Available implementation (the server's, which also covers the with-Mob case); one game-URL contract (gameHref in playModel.mjs, re-exported by MobGame.jsx; den Play key goes to /mob/game/<id>?play=1, podium ?view=podium, fix ?view=fix, back to /mob; a live-room card and the start-a-game redirect go to the card without starting the clock); one Fold art set (the den's fold-<key>-<pose>@<size>.webp; the play owner's unsized duplicates removed; a test fails on any /mob/folds/ name that is not a file); the game page reads GAME_VIEWS from the pure module (a server page cannot read a plain value from a client component); src/lib/mob/folds.mjs colours = fold_catalog.dart (fixture folds.json refreshed).
- **Previews:** /preview/mob-den opens its game links in /preview/mob-play (and back), /preview/mob-den?view=join added.
- **Checks:** lint 0; test:mob 174/174; test:billing 396/396; test:recovery 610 pass, 3 todo (known gaps), 0 fail; test:auth 114/114; test:app 841 pass, 1 skipped, 0 fail; test:subjects 30/30; next build --webpack exit 0 (.next removed). Headless preview walk (390 and 1440, Night and Day): den in 14 states, den to game to podium and back, game ready/run/done, podium so far/final/table, moments, fix, wallet free and Pro, /pricing: no broken images, no horizontal overflow, no page errors; every screenshot opened (tmp/walk-1020/web-v13).
- **Not deployed yet.** No push, no deploy, no production write. Mob v3 stays behind MOB_ENABLED and MOB_V3_ENABLED.

## 19 October 2026, about 9:51 pm IST: Play Pro monthly subscription: production migration APPLIED; web deploy with PLAY_BILLING_ENABLED next (owner D141)
- **His words (D141):** "Yes: once the web fixes pass every test and you've shown me the results, apply the production migration 20261019210000 and deploy the website with billing on. I'll set PLAY_BILLING_ENABLED=true in Vercel when you tell me."
- **Migration:** `20261019210000_play_subscriptions` applied to production isrxrxzjocewrdureyhp with the Supabase MCP (name play_subscriptions; same statements as the file, comments left out). Pre-check: play_purchases present, 0 rows, no sync function, kind check (pro, ai_credits). Post-check: 8 new columns; kind check (pro, ai_credits, pro_sub); mm_play_sync_subscription security definer, search_path public, pg_temp, execute for service_role only (anon and authenticated false); mm_play_revoke_purchase anon false; RLS on, 0 policies; 0 rows.
- **Undo:** PLAY_BILLING_ENABLED off (both Play routes 404) or a code rollback first, then `supabase/undo/20261019210000_play_subscriptions.undo.sql` (keeps the columns if any subscription row exists).
- **Branch:** web/1019pm-play-subs 9a62dbf4 (review fixes: refunded Razorpay date no longer keeps Pro after a subscription ends; account deletion cancels a Play renewal first; PlanCard keeps the Razorpay cancel key beside a Play subscription). Checks at 9a62dbf4: test:billing 387/387, recovery 610 (3 todo), auth 110/110, app 841 (1 skipped), eslint clean, next build --webpack exit 0; staging dry-run clean.

## 19 October 2026, about 2:50 pm IST: homepage motion option C is ON for everyone (main 9fd48201; D119, D120)
- **His words:** at 1:50 pm "a bit too slow ... every 2-3 seconds, it should be doing something new" (D119); at 2:30 pm "I like the V2, the one with the typing animation ... You can publish it" (D120).
- **What changed:** option C is faster and loops (first change 1.6 s after first paint, then a new line every 2.3 s; it pauses on scroll, off screen and in a hidden tab; Reduce motion shows "No more guessing."). HERO_MOTION_V2_DEFAULT = true, so everyone gets it with no env change; HERO_MOTION_V2=0 in Vercel (plus a redeploy) brings back the old line. ?hero=v3 (last year's April melt on today's line, D119) stays as a preview only.
- **Checks:** heroPhrases 31/31, lint 0, test:app 842, test:today 120, next build --webpack OK; a local next start showed all four lines cycling with 0 errors; production dpl_8uKmkJG7VLmfjCCTZp71UsfRS6qK READY, and the live homepage cycled all four lines in 10 s with 0 console errors.
- **Note:** the line now loops with no rest (his ask); it still stops on scroll, off screen, in a hidden tab and under Reduce motion.

## 19 October 2026, about 1:45 pm IST: website release 11 SHIPPED (main a0eb6abe, fast-forward from 23a7c090 = release 10); the homepage motion stays OFF behind HERO_MOTION_V2
- **Deploy:** Vercel dpl_7uPzhxDNpCbXMuX6J4iEmRx9HXmC READY at about 1:44 pm, aliased to www.mockmob.in. Runtime errors since the push: none (30 min window). Rollback point: dpl_4EH82tptRMfagc6npWiwBSFeLbQh (23a7c090, release 10).
- **No migration, no env change.** FIRST_FULL_MOCK_ENABLED is ON when unset ("false" turns it off and hides every free line; needs a redeploy). HERO_MOTION_V2 unset = release 10's hero for everyone, with the preview `https://www.mockmob.in/?hero=v2` working. The free first mock writes `learning_allowances` rows (table already on production; server-only inserts; the primary key is the one-per-subject lock). WALLET_COMMERCE_OPEN, PLAY_BILLING_ENABLED and PERSISTENT_LIMITS_ENABLED unchanged.
- **What is in it (PLAN-1019):** A4a G28/G31 (lit polish back: keycap volt key, card edge lights and washes, NTA mode button-card; one motion token file shared with the app, count-up 720 ms); A4b G29 (Sign out in the first screen of Account, one confirm everywhere), G25/D106 (Your papers: stats strip, subject chips, papers newest first, then Mistakes to repair), G26 (the Start sheet leads with the mode), G27 (scroll cue: peek, one nudge, chevron that never takes a tap); C1 G24/D114 web navigation A (Today, Practice, Start, Mob, You; Mobi's door at the foot of the sidebar); C3 G30/D114 hero option C behind the flag; W5 C-dec 1 (the first full mock in each subject is free, one per subject, ever); C2-web G21/D114 Ask Mobi B (/mentor with two doors: Ask now and Ask your record; the docked panel stays for asks about one question or mock); the copy pass (D114, R6); fixers A, B, C and D (verifier and walk findings).
- **Verification:** Opus verifier round 1 GO (2 MEDIUM, 10 LOW, all fixed); browser acceptance walk (390 and 1440, Night and Day; 5 blocks NOT DONE, all fixed by fixer B and C2-web); Opus verifier round 2: part A GO at 3ae564a6 (no HIGH, no MEDIUM; tmp/walk-1019/verify2/VERDICT-R2-partA.md), part B NO-GO at 37e86203 for 1 HIGH (the "8 to revise" badge wrapped the sidebar row and covered the Start key at 390) and 1 MEDIUM (a Free record ask could be charged 1 credit when the panel's second record read failed); both fixed in web/1019-fixd (badge back to "8 due", measured clear of the Start key; the panel never sends a Free ask as a paid reply). Main session: restored release 10's credit tick in the docked panel (a0eb6abe) and caught that the first restore shadowed creditCount() (would have crashed the "1 credit" labels); render-checked in a dev server, no page errors. Decision: GO (2 verifier rounds used).
- **Checks at a0eb6abe:** lint 0; test:app 835 (0 fail, 1 skipped); today 120; recovery 613 (3 todo); billing 349; dock 56 (1 skipped); learning 357; mob 78; auth 110; subjects 30; du 42; community 11; attempt-reads 12; answer-integrity 11; `next build --webpack` OK. Known, not a release 11 change: test:study's content-gate test fails on a clean install ("wordnet LICENSE_UNAVAILABLE": the wordnet licence file is not in release 10's or 11's lockfile install; a content-pipeline check, not runtime).
- **Production smoke (headless, no sign-in):** / , /?hero=v2, /pricing, /features, /login, /dashboard, /explore, /review, /mob, /mentor, /today, /wallet, /profile all 200; the plain hero reads release 10's line; ?hero=v2 types "See the lost marks." (tmp/walk-1019/prod-r11).
- **Known LOWs shipped:** with LEARNING_SESSIONS_ENABLED=true (OFF in production) a start quoted free that loses the race is charged 50 without a warning (fix before durable sessions go on); the old app v15.2 says "Free today" for the free first mock (fixed in v15.3); Colleges has two lit cards back to back near the foot; "An AI service writes Mobi's replies" sits under the Ask now field (owner's call).
- **Incident:** at 12:48 pm the shared mockmob-next/node_modules was emptied by a worktree removal that followed its junction (third time). Restored in 26 s with `npm ci --prefer-offline` from release 11's lockfile; the rule is now in docs/brain/BRIEF-1019-COMMON.md.

## 19 October 2026, IST - Release 10 verifier findings fixed (deploy/web-1018-r10; local, not pushed, not deployed; NOTHING applied to production)
- **Copy (tests in data/tests/release10_verifier_1019.test.mjs, in test:billing):** H1 Ask Mobi says "138 credits left · 38 free, back to 50 on 1 Nov", not "resets"; H2 "Your free credits go back to 50 on 1 November."; M3 one line everywhere (creditCopy ONE_CREDIT_LINE): "1 credit is 1 practice question or 1 chat reply; a full mock is 50 and deeper analysis is 3. The cost shows before you start."; M5 the wallet's out-of-credits line offers a top-up only when commerce.open, and never tells a Pro student to top up for practice; the Mob "Get credits" key is now "See your credits" to /wallet; buy_credits (actionPolicy and the execute route) follows walletCommerceOpen(); M7 /pricing/ai-credits rows (free this month + held credits) add up to the balance, and the open/paused words follow walletCommerceOpen(); L1 holds (no AI_PACKS); L5 "No credits needed for practice", a true wallet lede, a wallet description without "how to top up", "3 credits".
- **M6:** the attempts summary falls back to the table only for PGRST202 / 42883; a timeout (57014) or any other error makes GET /api/attempts?view=summary answer 503 with a retry message.
- **M1 (SQL edited in place, not on production):** mm_play_revoke_purchase and both data/db.js readers count only Pro plan payments (plan_id 'pro_...') as paid evidence; a credit-pack payment no longer keeps Pro after a Play Pro refund. Applied to STAGING (play_purchases_20261018190000_pro_evidence); a rolled-back check: credit-pack payer lost Pro, Pro payer kept it. Staging md5 d3e2356d167289e5a5704c2eef8d84c8.
- **M4 (SQL edited, staging only):** reserve_runtime_ai lifts the cap only while the student has an open (reserved/executing, unexpired) credit reservation with a bonus part, that is a reply paid from bought credits now; leftover headroom never pays for held-credit replies. Charge-first AI (mm_ai_consume_credits) gets no lift, the same as production today. Applied to STAGING (one_credits_balance_cap_lift_fix); a rolled-back check: bought-credit reply at the cap edge dispatched; held-credit reply after 20 bought credits were spent was refused. Staging md5 c09163e925f8a677456457565a0d06b6. The undo is unchanged and still restores production's bodies (spend_credits 911105fd, mm_ai_consume_credits c1ce92df, mm_ai_reserve_credits 499b44d1, mm_ai_release_credits 9c1d744b, reserve_runtime_ai f6026ff6).
- **Attempts function:** 20261018230100_attempts_list_summary_fn applied to STAGING (exact file); service_role only (anon and authenticated cannot execute), security invoker, filters by p_user_id. EXPLAIN ANALYZE for the heaviest staging user (26 attempts): 786 ms cold, 157 ms warm, about 0.8 MB sorted instead of about 29 MB shipped. Not on production.
- **Not now:** L2 Razorpay credit-pack refund clawback, L3, L4, L7.

## 19 October 2026, about 12:30 am IST - Website release 10 integrated (deploy/web-1018-r10, from live main 9b3661e8 = release 9; local, not pushed, not deployed; NOTHING applied to production)
- **Merged (git merge --no-ff, in order):** web/credits-core-1018 4eb36198, web/wallet-1018 d491ba22, web/pro-nudge-1018 5216dee0, web/play-billing-1018 9b6cd30b, web/r10-taste 18f791be, web/r10-attempts 5b8be747. Each merge commit lists its conflicts and how both intents were kept.
- **Decisions in the merge:** one chip (the unified total, to /wallet); the core's catalogue and unified wallet win; the release 9 Mob layout and rules win over the nudge track's older copy (the mob_limit sheet was false against release 9 and is fixed); the Play product map reads the one catalogue; the release 10 Today cue (glass circle above the dock) replaces release 9's in-flow cue, with release 9's no-cover / no-blink intents kept in tests; GET /api/wallet history reads like /api/me/credits (no balance stated before the month's free-credit reset).
- **Visual-check fixes (9567ef8a):** preview fixtures model one balance (chip, Practice header, Upgrade sheet and Wallet all 108); history lines say "Free credits for the month" / "Credits added"; /pricing lost a dead list with the old 50/150/400 packs; /pricing/ai-credits shows packs only when WALLET_COMMERCE_OPEN is also true.
- **Checks:** lint exit 0; test:billing 315/315; test:app 756 pass, 1 skipped; test:learning 357/357; test:recovery 604 pass, 3 todo; test:mob 78/78; test:today 120/120; play_billing + wallet + pro_nudge + attempt_list_summary + today_release10 126/126; next build --webpack exit 0. Headless screenshots (390 and 1440, Night and Day, preview fixtures, production endpoints severed in the dev server env) in mockmob-next/tmp/rel10-shots.
- **Migrations on this branch not on production (read-only check of schema_migrations):** 20261018190000_play_purchases, 20261018210000_one_credits_balance, 20261018230100_attempts_list_summary_fn (optional; the route falls back without it). Code and the one-balance migration ship together (see the core entry below).

## 18 October 2026, about 10:20 pm IST: website release 9 SHIPPED (main 2e45a92c), and the Mob is ON in production
- **Deploy:** main moved eb5185ef to 2e45a92c as a fast-forward. Vercel dpl_B8RemZJBcEvuc9CER6var7dFqr6Q is READY, aliased to www.mockmob.in, with 0 runtime errors in its first 20 minutes.
- **Vercel env:** MOB_ENABLED=true (Production) was set at about 10:15 pm, before the push. PERSISTENT_LIMITS_ENABLED was left unset on purpose; it is the owner's decision.
- **Smoke test (live):** /, /pricing, /today, /review, /mob, /join/<code> and /api/stats all return 200. /api/mob signed out returns 401 UNAUTHENTICATED (not the disabled error). /pricing says "1 credit a question".
- **Contents:**
  - Per-question practice credits (D65/C2): 5/10/15/20 questions cost 5/10/15/20 credits; a full mock costs 50; free allowances are unchanged; old builds keep attempt=10 and attempt_full=50.
  - The audit-fix packets: Today, Review/Result, nav and public.
  - The Mob (D66/C3).
- **Verification:** an independent Opus verifier ran 3 rounds with 2 fix rounds. Its final verdict: no HIGH, and 2 MEDIUM.
  - The join form showed a placeholder name and failed on the first Join tap. FIXED in 2e45a92c with tests.
  - W-044 (the Today cue is barely seen while scrolling at 390x844) is NOT claimed. The cue now sits in the page flow and never covers a control. W-044 stays OPEN for a decision.
  - Also fixed: the false line "You sat it in your other Mob".
- **Suites at 2e45a92c:** lint clean; test:mob 78/78; test:app 720/720; and at a14de0db: today 99, recovery 604 (+3 todo), learning 357, billing 215, auth 110, dock 31 (+1 skip), subjects 30. `next build --webpack` passes.
- **Production database: migrations applied today under the owner's standing grant.** Each had a pre-check, a post-check and a rolled-back dry run, and each has an undo file in supabase/undo.
  1. **20261018130000_free_ai_wallet_50**, about 3:47 pm.
     - The two AI wallet functions hash as the file; student_user_free reads 0.0284.
  2. **20261018170000_practice_credit_per_question**, about 6:22 pm.
     - spend_credits md5 went from 7decd1ff... (1535 chars) to 911105fd... (1666 chars); EXECUTE is granted only to postgres and service_role.
     - A rolled-back dry spend of 5+15+20+10+50 came to exactly 100, a replay was free, and 0 rows were left.
  3. **20261017100000_mob + 20261017190000_mob_fix_1017**, about 6:29 pm.
     - 26 functions have md5s equal to staging; 15 mob tables, all with RLS on; server roles only.
     - Undo runs in reverse order: the fix first, then the base.
- **Known open items (LOW):**
  - /mob?mob=<id> ignores the deep link to a second Mob.
  - "You both got the same question right" does not name the question.
  - W-044, described above.

## 18 October 2026 - ONE credits balance core (web/credits-core-1018; local, not pushed, not deployed; NOTHING applied to production; the migration IS applied on STAGING)

**Review fixes after the checker's round 1 (18 Oct, about 11:20 pm; commits 4431e42a and cdf2dcef over STOP POINT 6c23b11c, which was reviewed and kept).** The migration file changed, so the md5s in steps 4-6 below are superseded by the ones here.
- **(b) code and database ship together, guarded in code:** `oneBalanceLive()` (src/services/credits/aiWalletState.js) probes `public.mm_wallet_window` once (yes cached for the process, no cached one minute, any other error = old behaviour for that request). On a database without the migration the web keeps the OLD figures exactly (practice quote and /api/auth/me creditBalance = users.credit_balance, what the old spend_credits takes; AI wallet = free + bonus, what the old AI functions take). So the web may ship before the migration; the migration may NOT be undone while this code runs (undo order: code first).
- **(a) fields the live app reads, documented in src/services/credits/unifiedWallet.js:** one-balance database: /api/auth/me creditBalance and /api/ai/credits wallet.total = the one total, the amount any spend can take; old database: unchanged. /api/ai/context normalCreditBalance now stays users.credit_balance on both (the stop point had made it 0 on the old database). Ask Mobi's model gets one total with its parts and no second balance (creditsForModel.js).
- **(c) the per-user AI cap, decided:** only BOUGHT credits (ai_credit_wallets.bonus_credits; every Razorpay and Play pack is granted there) lift the owner's per-user cap, USD 0.02 per bought AI credit (`mm_bought_ai_credits_spent`, budget row `student_bought_credit`; the drafts' `mm_held_ai_credits_spent` / `student_held_credit` are dropped by the file). users.credit_balance credits are NOT bought: production holds 111,961 of them over 1,541 users (column default 100 = the signup grant, plus community rewards; no purchase ever went there). Under D78 they pay for AI like any credit, but under the owner's Rs 2.50 / Rs 5 cap, unchanged. Margin: production runtime_ai_requests (read-only): largest luna reservation USD 0.00237 (p99 0.00236, 9 rows), largest ever 0.002536, largest actual 0.00048; the largest the code can reserve is about 0.0045 a call, 2 calls a reply (MAX_PHYSICAL_CALLS), so 0.009. 0.02 covers that twice: a reply at the cap edge dispatches both calls, and so does the next one after a failed reply there (PGlite tests prove 0.005 and 0.01 fail those cases). Bought credits are spent before held ones, so a buyer is never refused by the cap while bought credits last.
- **Fixed in the stop point and kept:** mm_ai_reserve_credits records the wallet's synced period (a clock behind at a month edge can no longer turn free credits into bonus on release).
- **Checks (wt-credits-core at cdf2dcef):** eslint clean; test:billing 238/238 (now includes one_credits_balance 19 and one_balance_ship_together 4); test:learning 357/357; test:app 692 pass, 1 skipped, 0 fail; test:recovery 604 pass, 3 todo (known gaps), 0 fail.
- **Staging (onwkqxmjqjrhfbjjdydu), final file:** dry-run of the changed bodies in a DO block that raised (rolled back), then applied with apply_migration (`one_credits_balance_20261018210000_final`, then `one_credits_balance_20261018210000_bought_cap` = every statement of the final file, header comments trimmed; idempotent on an applied database). md5(prosrc) now EQUAL the file: spend_credits a2d71600fffe756b05443f4f4ca72967, mm_ai_consume_credits f43c5c1e8b3c2ef6acd93cc264c5e5d2, mm_ai_reserve_credits 01e87c89d18754a99d2b843ef23cad1d, mm_ai_release_credits 8313e28a7c5f1de0cde72b0772d450f8, reserve_runtime_ai 14e38c076490cc8f25f00570acd68786, mm_wallet_take ca977c2458db54d823908dc120ada860, mm_wallet_window c16763e69a3853d2a1a7d7853ae173f4, mm_bought_ai_credits_spent c728032bb35720b5c368518388e257e0; ACL postgres + service_role on all eight; runtime_ai_budget student_bought_credit 0.02, no student_held_credit row, no mm_held_ai_credits_spent.
- **Spend matrix on the final staging (rolled-back DO block, users dry1018c_*):** free 10 / bought 8 / held 20: a 5-set takes 5 free; a 10-set takes 5 free + 5 bought, parts {5,5,0}; its replay returns true with one row and no second debit; an AI reserve of 2 takes bought (bonusSpent 2), its replay is idempotent; a 5-set takes bought 1 + held 4; a full mock with 16 left returns false with nothing taken and no row; an AI reserve of 17 is refused, nothing taken; AI consume 1 from held, replay charges once (15 held left); bought AI credits this month = 2; at the cap: the student with bought spends dispatches two USD 0.0045 calls, a student with nothing is refused, a student with 100 held (signup) credits is refused by the cap and gets the reserved credit back (100). "MATRIX OK".
- **Undo dry-run on the final staging (the updated undo file, guard inline, DO block that raised):** the five bodies back to production exactly (consume c1ce92df, release 9c1d744b, reserve 499b44d1, reserve_runtime_ai f6026ff6, spend_credits 911105fd), ACL postgres + service_role, new functions left 0, budget rows left 0. Afterwards staging still holds the final migration (reserve_runtime_ai 14e38c07, 3 new functions, no dry rows).
- **Production (read-only, 11 pm):** the five functions still at the "before" md5s; mm_wallet_take / mm_wallet_window / mm_bought_ai_credits_spent absent; no parts / from_balance columns; no student_bought_credit row; 0 open AI reservations. Exact production steps: in the main session's notes for release 10.

**Owner (D78, 18 Oct 6:50 pm):** one credits balance for everything. Spend order: this month's free 50, then bought (ai_credit_wallets.bonus_credits), then held (users.credit_balance). 1 credit = 1 question or 1 Ask Mobi reply; a full mock 50. Database core in 5c553d3a (public.mm_wallet_take used by spend_credits and the AI reserve/consume; refunds per part; held credits raise the per-user AI cap; `src/services/credits/creditPacks.mjs`; PGlite tests `data/tests/one_credits_balance.test.mjs` 16/16; migration `supabase/migrations/20261018210000_one_credits_balance.sql`, undo `supabase/undo/20261018210000_one_credits_balance.undo.sql`).

**Web reads (11d0ef56, finishing STOP POINT 72d8550e, which was kept):** every balance read goes through `getUnifiedWallet` / `readAIWallet` (both read the wallet row and users.credit_balance together; either failing = unknown, never 0).
- `/api/auth/me` creditBalance = the one total (+ `credits` parts); `/api/practice/quote` prices against the one total; `/api/ai/credits` adds `credits`; `/api/me/review` aiCredits = practiceCredits = the one total.
- `/api/me/credits` adds `total {balance, freeLeft, freeAllowance, held, renewsOn, label}` (additive; practice.balance + ai.balance = total.balance, never counted twice) and each history line states the ONE balance after it, counted back across both ledgers; a line older than this IST month has no number (the free credits come back with no ledger row). The app contract fixture `contract_credits_v1.json` is unchanged.
- Account: one tile, one figure ("9 of your 50 free credits left this month; 50 more on 1 November. They are used first."), filters by kind (Practice / Ask Mobi and repairs). Top bar: ONE credits chip, opening the credits page. Ask Mobi's wallet line shows the total once anything is held.
- One name, "credits", in every student-facing line; sentences that claimed two separate balances rewritten (help answer, /pricing rows and Ask Mobi section, /pricing/ai-credits intro, /features, assistant knowledge). `PRACTICE_PRICE_LINE` = "1 credit a question. A 10-question set is 10, a full mock 50." The server contract labels in `src/lib/server/credits.js` stay ("Practice credits"/"AI credits", app parity).
- Fixtures regenerated: `data/tests/fixtures/review/expected.json` and `data/tests/fixtures/result_next_move/*.json` ("1 credit", "credits"). **The app copies under flutter_app/test/fixtures/{review,result_next_move} must be synced when the app takes the one balance.**
- `ai_cap_route_coverage`: a later migration may READ student_user_paid (reserve_runtime_ai); only an insert or update is a write. (This test failed at 5c553d3a.)

**Checks (worktree wt-credits-core):** eslint clean; test:billing 215/215; test:app 692/692; test:learning 357/357; test:recovery 604 pass, 3 todo, 0 fail; PGlite one_credits_balance 16/16; `next build --webpack` ok. Baseline at 5c553d3a: billing 215/215, app 686/686, learning 356 + 1 fail (the cap-coverage test above), recovery 604.

**Staging (onwkqxmjqjrhfbjjdydu), in order:**
1. **Compared with production (read-only pg_proc md5(prosrc)):** spend_credits equal (911105fda93f7c1dcd687b08dd7c1059). Staging DIFFERED on mm_ai_consume_credits c0b401769a58a563ccb7ee1879607a79 (no mid-month allowance sync; EXECUTE also granted to PUBLIC, anon, authenticated), mm_ai_reserve_credits 75c8ea15510925ca223c3f1061a82f96 (default allowance 10), mm_ai_release_credits 57047a2b5395072ec20c2e359f693a3c (CRLF + comments), reserve_runtime_ai 3df970caa84b7ec89a0344735cb52b29 (comments).
2. **Brought staging to production's bodies** (staging migration `staging_baseline_one_credits_prod_bodies`, bodies from the undo file, whose md5s equal production's) and production's grants on consume (service_role only). After: consume c1ce92df1577794e2e49a54d82a0fd42, reserve 499b44d19273c8901b11d65f0874e9fc, release 9c1d744b969d7e52c74d06e5537110f5, reserve_runtime_ai f6026ff6dde4b329e6f021dae3b51b7a, spend_credits 911105fd = production; ACL postgres + service_role on all five.
3. **Dry-run** (the whole migration plus the spend matrix inside one DO block that raises at the end): "DRYRUN OK (rolled back)". Afterwards mm_wallet_take/window/held absent, no parts column, no test users, spend_credits back to 911105fd.
4. **Applied for real** (staging migration `one_credits_balance_20261018210000`, the file body unchanged). md5(prosrc) now equal the repo file: spend_credits a2d71600fffe756b05443f4f4ca72967, mm_ai_consume_credits f43c5c1e8b3c2ef6acd93cc264c5e5d2, mm_ai_reserve_credits 0921e34189052ee6cd6ec6a3ab55f8e7, mm_ai_release_credits 8313e28a7c5f1de0cde72b0772d450f8, reserve_runtime_ai 69e3d0c2f4e48f3bce157df66aef3966, mm_wallet_take ca977c2458db54d823908dc120ada860, mm_wallet_window c16763e69a3853d2a1a7d7853ae173f4, mm_held_ai_credits_spent 15a785e33797d37c3202a37fb7620551; runtime_ai_budget student_held_credit 0.005; every function service_role only.
5. **Spend matrix on the applied staging** (test users dry1018_*, in a DO block that raises at the end, so they are rolled back). Free/bonus/held, u1 starting 50/30/100: a full mock 50 -> 0/30/100 parts {included 50}; an Ask Mobi reply (reserve 1) -> 0/29/100 (bonus); a 20-set -> 0/9/100; a 15-set -> 0/0/94 parts {bonus 9, balance 6}; AI consume 3 -> 0/0/91 (repeat idempotent); reserve 2 from held -> 0/0/89, release -> 0/0/91 (back to held), release the bonus reply -> 0/1/91 (back to bonus), repeat release idempotent; a repeated practice reference charges nothing; a full mock 50 across bonus 1 + held 49 -> 0/0/42; a student with no wallet row and nothing held: the free 50 pay one full mock, then a 5-set is refused with no row written, and a reply is refused; held AI credits spent this month = 3 (released ones excluded); per-user cap (staging student_user_free 0.0114): a student at the cap with no held spend is refused ("runtime user limit reached"), the one with 3 held credits spent dispatches; a new IST month: the free credits reset before the take -> 45/0/42. Result: "MATRIX OK".
6. **Undo dry-run** (the undo file, guard inline, in a DO block that raises at the end): md5s back to production exactly (consume c1ce92df, release 9c1d744b, reserve 499b44d1, reserve_runtime_ai f6026ff6, spend_credits 911105fd), new functions left 0, held row left 0, ACL postgres + service_role. Rolled back: staging still holds the applied migration (checked after).

**Not touched on staging (drift noted):** runtime_ai_budget caps (staging student_ai 25, student_user_free 0.0114, student_user_paid 0.1136 vs production 1000000 / 0.0284 / 0.0568), mm_ai_commit_credits, mm_ai_grant_bonus_credits, mm_ai_release_expired (bodies differ from production), runtime_ai_month_start (CRLF only), ai_credit_wallets column defaults (absent on staging).

**For the production step (release 10, not done here; superseded by the review-fixes block at the top of this entry for md5s and ship order):** pre-check the five md5s above equal production's "before" values; apply the migration; post-check the eight md5s; the undo is proven on staging. Code and database ship together (old code shows two numbers; new code on the old database shows the one total but AI cannot spend users.credit_balance). `public.mm_spend_credits_amount` (security definer, spends users.credit_balance only) has no caller (`src/services/credits/checkAndConsumeCredits.js` is unused); leave it or drop it in a later cleanup. For the D/E lanes: /pricing pack cards and PrepOSCreditPurchaseButton still describe the old 50/150/400 packs (renamed to "credits", prices unchanged); creditPacks.mjs is the catalog to point them at.
## 18 October 2026 - Credits wallet, web (branch web/wallet-1018, from release 9 part A 5d9116f0; local, not pushed, not deployed; NOTHING applied to any database; this branch adds no migration)

**Owner, D76, D78, D82, D84:** ONE credits balance for everything (this month's free 50, then bought, then held; 1 credit = 1 question or 1 Ask Mobi reply; a full mock 50); packs `credits_10_50` Rs 10, `credits_29_150` Rs 29, `credits_49_300` Rs 49 (featured); persuasive but true copy; Razorpay is wired by the owner today.

- **Page `/wallet`:** one balance figure with what a credit buys, the free credits left and their reset date, the credits held ("They do not expire"); the three packs with their price, what they buy ("6 full mocks, or 300 questions") and the per-credit price, "Best value" on the 300 pack only (it is the lowest per credit); a Pro line for Free students ("Get unlimited mocks: with Pro, practice never uses a credit. Rs 99 through 31 July 2027."); the last 20 lines of activity with one running balance. Closed top-ups say "Top-ups open soon" on every key and the note "Your free credits keep working until then". No exclamation marks, no countdowns, no scarcity words (the copy test now also bans hurry, last chance, ends soon, only today, selling fast, countdown); every number is read from the practice price list and the pack catalog.
- **API:** `GET /api/wallet` (cookie or bearer; the exact JSON is in `docs/brain/WALLET-RAZORPAY.md` section 5, including the new `packs[].fullMocks`); `POST /api/wallet/order` and `POST /api/wallet/verify` behind `WALLET_COMMERCE_OPEN` (closed = 503 `WALLET_COMMERCE_CLOSED`, no order, no payment row, no Razorpay call; verify is never gated, so a payment already taken always settles).
- **Compat with the credits core (wt-credits-core 5c553d3a):** `src/services/credits/creditPacks.mjs` is now a byte copy of the core's catalog and `unifiedWallet.js` returns the core's shape (`known`, `wallet` added); the wallet imports only `CREDIT_PACKS`, `LEGACY_AI_PACKS`, `PLAY_PRODUCT_IDS`, `findCreditPack` and `findBuyableCreditPack`, and names a pack by `key`. Test `compat with the credits core` fails on anything else. On the release 10 merge take the core's `creditPacks.mjs`, `unifiedWallet.js`, `aiCreditWallet.js` and `aiWalletState.js` whole; the wallet needs no other change. The app never reads `proOffer`, `packs` or `commerce` (anti-steering, D72; Play prices D82).
- **Checks:** eslint src and data/tests/wallet_1018.test.mjs clean; wallet_1018 28/28; test:billing 230/230; test:app 687 (686 pass, 1 skipped by design); test:auth 110/110; test:today 99/99; test:mob 45/45; test:dock 32 (31 pass, 1 skipped by design); test:subjects 30/30; test:learning 357/357; test:recovery 607 (604 pass, 3 todo, 0 fail); `next build --webpack` passes (one first attempt failed on a transient Google Fonts fetch, the retry passed) and lists /wallet, /api/wallet, /api/wallet/order, /api/wallet/verify.
- **Visual:** headless playwright-core (own temp profile) against a dev server on 3421 with the preview fixture (`/preview/arena?view=wallet`, also `&commerce=open`, `&wallet=zero`, `&plan=pro`); captures opened at 390 and 1440, Night and Day: no horizontal overflow (scrollWidth equals clientWidth in all of them), one lime key on the page (the shell's Start), the packs stack with price and key on one row at 390, the Pro and zero states read correctly. The 390 full-page captures show the fixed dock over the pack list: a capture artefact, not layout.
- **Not done here (owner or release 10):** Razorpay keys and webhook and `WALLET_COMMERCE_OPEN=true` (owner; steps in WALLET-RAZORPAY.md); the `one_credits_balance` migration and the unified spend order (credits core, not applied anywhere); a Razorpay test-card purchase on a preview deployment.

## 18 October 2026 - Web release 9 integrated (part A) (deploy/web-1018-r9, from live main 00328e54 = release 8; local, not pushed, not deployed; nothing applied to any database; the Mob packet web/r9-mob-1018 is NOT merged yet)

**Merged, --no-ff, in order:** web/r9-perq-1018 (dfc33d17), web/r9-today-1018 (106c8fb5), web/r9-review-1018 (0f5df84d), web/r9-nav-1018 (d88e7c5b), web/r9-public-1018 (77da5a35). Each STATUS section below is kept, newest packet on top of the older ones.

**Conflicts:** (1) `docs/brain/STATUS.md` in the today, review, nav and public merges: every section from every side kept. (2) public: `package.json` test:billing, test:auth and test:app lists: every test file from every side kept (practice_credit_per_question in test:billing, release9_nav and release9_public in test:app). /pricing and the landing merged without a conflict: perq's credit wording (`PRACTICE_PRICE_LINE`, "1 a question in Quick practice, 50 a Full mock") and public's one price framing ("Pro is ₹99 once, through 31 July 2027", "Your standing") both stand. (3) Semantic, not textual: release9_nav's plan-card test still asserted the old "Quick practice costs 10 practice credits" sentence; it now asserts perq's one price sentence.

**Leftovers fixed (test `data/tests/release9_integrate_1018.test.mjs`, in test:app):**
- Result's last link said "Open weak chapters" but opens /analytics, which is "Marks trend": it now says "See your marks trend".
- Practice at 1440 x 900: the session card's Start key sat at y=892 to 944 of 900 on first load and the price was stated about four times in the first fold. Now the price sits once on the mode tiles ("1 a question", "50 credits") plus the card's own Cost line; the line under the lede (`PRACTICE_PRICE_TAIL`), the card's "Your practice credits" row (the chip under the lede and the top bar already show it) and the amount in the "charged only after a complete set is built" note (`data/practice_quote.js`, now "You are charged only after a complete set is built.") are gone. Start is at y=810 to 862. No amount changed.
- Result said the key re-check three times: the notice under the score stays (with its jump); the "Answer keys we are re-checking" list (`KeyReviewLog`, no longer mounted) is gone from the Marks part; the ledger group "Under re-check or corrected" is now "Not sorted" (copy in `data/mistake_lab.copy.json`, fixtures contract_ready_v1 and contract_replay_v1 rebuilt, mistake_lab and result_parts tests updated). The marks arithmetic is unchanged. Still there, by design: each row's chip and the per-question notice, and the "(1 question under re-check left out of both)" footnote in Time and changes.
- Footer blurb: "tonight.The 15 subjects" had no space; fixed.

**Checks:** eslint src and data/tests clean; test:app 687 (686 pass, 1 skipped by design); test:today 99/99; test:recovery 607 (604 pass, 3 todo, 0 fail); test:learning 357/357; test:billing 202/202; test:auth 110/110; test:dock 32 (31 pass, 1 skipped by design, needs DOCK_BASE_URL); test:subjects 30/30; test:mob 45/45; `next build --webpack` ok (.next deleted). Visual: headless playwright-core on a dev server on 3250 (preview fixtures and public pages only, every non-GET aborted, stopped afterwards): Today, result, Review, Practice, the More sheet (390), /pricing, the landing (hero, Your standing plan, footer) at 390 and 1440, Night and Day; every screenshot opened: `mockmob-next/tmp/r9-integrate/`.

**Verifier fixes (after the first verify of part A; tests in practice_credit_per_question, release9_public, today_release8/9; no database touched, nothing pushed or deployed):**
- **MEDIUM, a free included set priced at "10 credits" (every surface now reads the allowance the way the quote does):** new pure `src/lib/dailySet.mjs` (states 'free' | 'priced' | 'unknown', `dailySetFromQuote`, `countHint`) and one shared, read-only, minute-cached read of `GET /api/practice/quote` for a Quick 10 (`src/lib/useDailySet.js`, `src/components/useMyDailySet.js`; forgotten when a set is launched). 'free' prints "Free: today's included set." (short "Free today") and no number or balance; 'unknown' (not read yet, read failed, quote blocked) prints no number ("Practice shows the price before it starts."); 'priced' (allowance off, or today's set used) prints the price as before. Surfaces: Practice count option for 10 (own Quick 10 quote first, else the shared read; unread shows no hint), Today's lead price line (moved to pure `src/lib/today/priceLine.mjs`; the lead also holds for the read, same 1.5 s cap), the Start sheet (`costLine`, hero and the Quick and By chapter rows), the result next move and Review (`nextMove`, `practiceCostLine`, new `chapterPracticeClause`, `reviewInput({dailySet})`), Review's empty state, Revise's empty state, Review's chapter row. 15, 20, a full mock and Pro never change; a caller that passes nothing keeps the shared fixture words ('priced'), so the app port and fixtures are unchanged. The Today reel builds the same move but renders no price, so it reads nothing. Production note: the allowance is off there today (0 rows in learning_allowances), so the quote says priced and "This set uses 10 practice credits" is still the true line until LEARNING_SESSIONS_ENABLED is on; with it on, every line says free. Seen (headless, preview fixtures, `?allowance=on`): Practice 390 Night and 1440 Day/Night ("Free today" under 10, Cost "Free: today's included set"), Today first week 1 and 3, the Start sheet at 390 Day and Night (hero and By chapter), the result (1440 Day, 390 Night), Review chapter row (1440 Night) and the empty Review (390, 1440), `inventory=down` (no number); without the flag they still say "10 credits" and "uses 10 practice credits". Screenshots: `tmp/r9-fixes/fixes2/`.
- **MEDIUM, /pricing FAQ said "Pro is ₹99 a month":** the non-monthly answer is now "Not yet. Today Pro is one payment of ₹99 for access through 31 July 2027, with no auto-renewal. A ₹99 monthly plan opens soon, and whoever pays now keeps the full term." (the FAQ JSON-LD reads the same string). Test: no "Pro is ₹N a month" outside a monthly branch.
- **LOW, credits modal:** a balance buys whole 5s (`quickQuestionsFor`: 37 credits = 35 questions); under 5 it says "Not enough for a 5-question set" with the title "Not enough practice credits" (0 stays "out of"); the label/value rows wrap instead of squeezing the label (390). Preview gained `?balance=N` for the free fixture user.
- **LOW, restart after the deploy:** `spendWithLegacyFallback` (data/practice_charge.js, used by the device-held start): on exactly "credit reference already used" for `attempt_5/10/15/20` it asks once with the legacy `attempt`; the reference then exists, so that call is recognised as the same spend (true) or refused again, never a second charge. Proved on PGlite with the real migration. The database function and its md5 are unchanged (the app-side option), so the deploy plan's md5s stand.
- **LOW, migration md5 on Windows checkouts:** `.gitattributes` now has `supabase/**/*.sql text eol=lf`; both files re-checked out as LF on disk: migration body md5 911105fda93f7c1dcd687b08dd7c1059 / 1666, undo 7decd1ff44f4456ed2552a9e19ed1157 / 1535 (test reads raw bytes). Other checkouts: `git checkout` the two files once after pulling the attribute, or apply from `git show HEAD:<path>`.
- **LOW, landing at 390:** the hero key steps down to secondary after the first sample answer at every width (was 960 px and up only); `DEMO_QUIET_QUERY` and the matchMedia gate are gone. Seen at 390 Day and Night after a real pointer tap on "Frank": Try five questions is secondary; the chosen chip and Next question are the lime in view.
- **Checks:** eslint src and data/tests clean; test:app 688 (687 pass, 1 skipped by design); test:billing 215/215; test:recovery 607 (604 pass, 3 todo, 0 fail); test:today 99/99; test:learning 357/357; test:auth 110/110; test:dock 32 (31 pass, 1 skipped by design); test:subjects 30/30; test:mob 45/45; `next build --webpack` ok (.next deleted). Dev server on 3261 (preview fixtures and public pages only, every non-GET aborted, 0 blocked), stopped afterwards.

## 18 October 2026 - Practice credits per question (branch web/r9-perq-1018, from live main 00328e54 = release 8; local, not pushed, not deployed; NOTHING applied to production, the migration IS applied on staging)

**Owner, 18 Oct about 4 pm (D65):** "5, 10, 15, 20, like as many questions, that many credits." On Free, Quick practice costs 1 practice credit a question: 5 = 5, 10 = 10, 15 = 15, 20 = 20. A full mock stays 50. Unchanged: Pro pays nothing; today's included 10-question set, the first set per subject (baseline), the full sample, the free 5-question recovery set, Mob papers; the starting 100; AI credits.

- **One helper** (`data/test_modes.js`): `practiceCreditCost(modeId, count)` and `practiceCreditAction(modeId, count)` (quick -> `attempt_<n>` for 5/10/15/20, full -> `attempt_full`, Pro modes 0/null, any other count null; the start paths already resolve a stray count to the 10-question default). Quick has `creditPerQuestion: 1` and no flat `creditCost`. Used by the quote (`practice_quote.js`), the charge (`practiceSessions.js`), recovery (`recoverySessions.js`), `db.spendCredits` whitelist, the dashboard, Today's price line, the Start model (`costLine(mode, {count})`), the credits modal, the result page's next move.
- **Database (the only place a spend is priced):** `public.spend_credits` maps `attempt_5/10/15/20` to 5/10/15/20; `attempt` stays 10, `attempt_full` 50, `generate` 10. `start_learning_session` and `start_recovery_session` only pass the action through, untouched. No refund or cancel path exists for practice spends (read the repo and production), so nothing needs to refund a different amount.
- **Migration (NOT applied on production):** `supabase/migrations/20261018170000_practice_credit_per_question.sql`, undo `supabase/undo/20261018170000_practice_credit_per_question.undo.sql`. Production before (read-only, 18 Oct): md5(prosrc) 7decd1ff44f4456ed2552a9e19ed1157, length 1535. After: 911105fda93f7c1dcd687b08dd7c1059, length 1666, proconfig search_path=public, pg_temp. The undo restores production's exact body (proved on PGlite: md5 and length equal).
- **Staging (onwkqxmjqjrhfbjjdydu):** dry run in a DO block that raised (rolled back; balance 390 afterwards, no leftover rows): spends 5, 10, 15, 20, full 50, old attempt 10, generate 10; attempt_7 refused; a retry charged once; a different action on one reference refused. Then applied for real; md5 911105fd..., length 1666. Staging's function differed from production before (md5 8ac89ba7..., no search_path, CRLF); it now equals what production will have after.
- **Copy:** one sentence from `src/lib/creditCopy.mjs` (`PRACTICE_PRICE_LINE`): "Practice credits: 1 a question. A 10-question set is 10, a full mock 50." Used in /pricing notes, plan terms and the comparison row ("1 credit a question"), Account > Plan, the help answer, the pricing FAQ; the dashboard header line and the Quick tile ("1 a question"); each count option shows its own cost (5, 10, 15, 20 credits; none on Pro); the credits modal ("1 practice credit a question", "N questions" left). The landing, /features and /pricing/ai-credits state no practice price, so they are unchanged.
- **Tests:** new `data/tests/practice_credit_per_question.test.mjs` (22, in test:billing; PGlite with the real migrations 0036 and later, the migration, the undo). Updated paper_copy and startModel tests. lint clean; test:app 653; test:today 87; test:recovery 586 pass, 3 todo; test:learning 357; test:billing 183; test:auth 110; test:subjects 30; test:mob 45; `next build --webpack` ok (.next deleted).
- **Visual:** headless playwright-core on a staging-keyed dev server on 3230 (stopped afterwards), preview fixtures; opened and checked dashboard 390 Night, 1440 Day and Night (count options with costs, cost line "15 practice credits", bar "15 min, 15 credits"), /pricing 1440 Day and 390 Night; text of /pricing and Help read at 390 and 1440, Night and Day. The Start sheet does not open in the preview, so its rows are covered by tests only; Today's preview shows the Revise lead (Free, no credits), so its set line is covered by tests only.
- **Known, not changed (fixed afterwards, see the release 9 verifier fixes):** Today and the Start sheet name a 10-question set as "uses 10 practice credits" even when today's included set is free (same as before). Old app builds keep sending `attempt` (10), which still works.
- **Deploy order:** apply the migration on production first (backward compatible: old code still sends `attempt`/`attempt_full`), then the code. Roll back = code first, then the undo.

## 18 October 2026 - Web release 9, Today packet (web/r9-today-1018, from live main 00328e54 = release 8; local, not pushed, not deployed; no data written)

Refinements only; nothing cut. Proof screenshots (headless playwright-core, own temp profile, dev preview fixtures on localhost:3241, every one opened): `mockmob-next/tmp/r9-fixes/today/`.

- **D28 (MEDIUM, greeting flash):** the hour and the date come only from the client (`useSyncExternalStore(..., () => null)`); new `greetingAt()` returns null for an unknown hour; both head lines keep their height and fade in (180 ms). The SSR HTML of `/preview/arena?view=today` holds no greeting (`ssr-preview-today.html`: h1 has only a screen-reader "Today"). At a fixed 2:41 am IST it reads "Hello" (`g-241am-m-dark.png`). Test: today_release9 D28 x2.
- **W-042 (lead before the glance column):** the lead also holds for the rhythm, road, goal and insights reads, under the same 1.5 s cap (`holdForPage`); skeleton heights now match the landed blocks (lead 600/540, week 255, road readout 240). Measured, polled every 30 ms: lead, This week, Road and Weak chapters land on the same tick at 390 and 1440 (was 240-400 ms apart). Test: today_release9 W-042.
- **W-044 (cue behind the dock):** the cue is a sticky pill 8 px above the dock's safe area (`bottom: calc(84px + env(safe-area-inset-bottom))`, 16 px from 1024 px). Without the fixture bar at scroll 0: 390x844 cue 716-760 vs dock 768-832; 390x932 cue 796-840 vs dock 856-920. Real pointer tap scrolls the week to the top and the cue fades (`cue-nobar-m-*.png`, `cue-nobar-m2-dark.png`, `cue-after-tap-m-dark.png`). Test: the cue offset equals dock bottom + height + 8 read from arena.css.
- **D27 nits:** Road's selected stop is a 2 px ink underline, no raised tile (`today-d-dark-full.png`); "Today already counts toward your week" is only in This week, Road says what is left ("Left: 5 Revise questions."); Road's This week prints This week's own count via `weekDays()` ("4 of 4 study days", the mock on its own line "and 1 of 1 full mock"; `fw7-m-dark-full.png`); the returning card's link is now "See all 6 mistakes" in the footer beside More ways to practise, "Why this?" alone in the reason (`returning-d-light.png`). Tests: today_release9 D27 x4.
- **F18 (path not readable, check day mislabelled):** the rail has day numbers under the marks and one line naming today's step and the next ("Tomorrow: A second subject.", "The last step of your first week."); the overline says "Day N of your first week" only when the card shows the day's step (`pathLeads`), else "Up next" with "Day 3 of 7: Weak chapters next." (`fw3-d-light.png`, `fw3check-m-light.png`, `fw7-d-light.png`). Tests: today_release9 F18 x2.
- **LOW (Why this? restated the card, counts disagreed with the chip):** `todayContext({ move, revise })` sends the reason, the move's chapter and which mistakes come back (Revise chapters, only when they add up to the card's count); the plan's fact lines are no longer sent. `todayAnswer()` builds the opening from the panel's own insights read (same as the "Your record" chip): wrong and blank of N over S sessions, the last miss date, the marks at stake of the record's open marks. Real pointer click (`whythis-d-dark.png`, `whythis-m-dark-fw3.png`). Tests: today_release9 x2, ask_mobi_entries and ask_mobi_panel updated.

**Files:** `src/app/(app)/today/page.jsx`; `src/components/today/{TodayMove,TodayRoad,TodayWeek,useToday}.jsx|js`, `today.css`; `src/lib/today/{firstWeek,greeting,move,week}.mjs`; `src/components/ai/askContexts.mjs` (Today part) and `src/components/ai/askSuggestions.mjs` (the today branch of `openingFor` only, outside the packet's list); `package.json` (test:today adds today_release9); tests: new `data/tests/today_release9.test.mjs`, updated wiring asserts in today_1017, today_release7, today_release8, ask_mobi_entries, ask_mobi_panel.

**Checks:** eslint src and data/tests clean; test:today 99/99; test:app 653/653; test:recovery 586 pass, 3 todo (known gaps, unchanged), 0 fail; test:learning 357/357; `next build --webpack` ok (.next deleted). Not measured: real-account timing on production (needs a signed-in production walk).

## 18 October 2026 - Web release 9, packet "review": result, Review and the reel (branch web/r9-review-1018, from live main 00328e54 = release 8; local, not pushed, not deployed; nothing written to any database)

**Items and proof** (screenshots in mockmob-next/tmp/r9-fixes/review/, 390 x 844 and 1440 x 900, Night and Day, real pointer clicks, 0 non-GET /api requests on every click):
- **D18 / LOST-X-OF-Y (HIGH):** `chapterRows()` never prints "lost X of Y" with X > Y. Every question wrong now reads "Lost 35 marks, 6 questions in Mock 3 and Mock 2. 5 wrong, 1 left blank." and the bar is full (share clamped to 1); lost == offer keeps "of N"; offer unknown says the marks alone. Test: release9_review_1018 (every-wrong, lost == offer, lost < offer, offer unknown, and a sweep of every wrong/blank mix to 8 questions). Seen: review-allwrong-1440-night.png, review-allwrong-390-day.png, review-allwrong-390-night.png, review-allwrong-1440-day.png (preview ?review=allwrong).
- **D15 counts that agree (HIGH):** the finding under the score is scoped to its chapter: "In Share Capital: 4 wrong and 1 left blank of its 6 questions." (and "In X: 1 right of its 10 questions, 6 wrong and 3 left blank."). Same sentence in the reel (it reads finding.detail) and Today's reel. "After this mock" prints once: the in-part SwotPanel no longer carries a second (screen-reader-only) title. The shared fixtures data/tests/fixtures/result_next_move/*.json carry the new sentence, so the app port must take the same words. Seen: result-hero-1440-day.png, hero-idle-390-night.png, reel-chapter-390-light.png.
- **F11 nothing shown twice (MEDIUM):** an opened Review mistake shows its stem once (the sheet leaves it out when the row prints the same words; a cut-short row stem keeps the full question in the sheet) and one Repair entry: the row's Repair goes while its sheet is open, the sheet's own "Repair Q42, 1 AI credit" stays (the audit's suggestion to hide the inner key would have left no paid path under W-032). ".:" join removed (cleanStem). Seen: review-open-390-light.png, review-open-390-dark.png, review-open-1440-dark.png, review-open-1440-light.png, review-answer-1440-dark.png.
- **LOW ledger:** "Where your marks went" no longer waits on a 14 px bar at threshold 1. IntersectionObserver cannot see a jump past the bar (no threshold crossed), so the panel asks on mount, scroll and resize: any part in view plays the split, a bar already above the viewport shows the final state, a closed part waits. Walked: jump past the bar gives data-split still and opacity 1 (was armed, opacity 0). Seen: ledger-past-bar-1440-dark.png, ledger-past-bar-390-light.png, ledger-scrolled-in-390-dark.png.
- **LOW reel:** the sheet lights without pauses, then the moments play by the clock (33:54, 48:56, 51:01; was 48:56, 51:01, 33:54); a ring is only on a listed moment; the chapter rings (Q12, 17, 22, 42, 47) carry "Ringed: 5 questions in Share Capital that lost marks." Seen: reel-moment-390-light.png, reel-chapter-1440-dark.png, reel-end-390-dark.png.
- **LOW hero Mobi:** rest renders as the wide-eyed idle on the web hero (src/components/result/heroAct.mjs); proud (happy eyes, sparkles) and encouraging render. Preview gained ?tone=first_mock|higher|lower|held. Seen: mobi-idle-zoom.png, mobi-first_mock-act.png, mobi-lower-act.png (before: hero-rest-390-night.png).
- **LOW fixtures:** previewReview saved repair says key B everywhere (was B then option C); previewFixtures fixtureAttempt completedAt is 25 minutes before now, so ?view=result&earned=one shows the Badge earned row (verified).

**Files outside the packet list (smallest change):** data/replay.js (reelScript order), data/result_next_move.mjs (costliestLine sentence), data/tests/fixtures/result_next_move/*.json, data/tests/replay_reel.test.mjs, data/tests/result_next_move.test.mjs and retry_first.test.mjs (one assertion each updated for the new code), src/app/preview/arena/ArenaPreviewClient.jsx (?tone= and saved-repair dates relative to the paper), package.json (release9 test wired into test:recovery).
**For the app port:** review_chapters.dart (lost > offer wording), the costliest sentence and the reel order should take the same words from the shared fixtures.

## 18 October 2026 - Website release 9, fix packet "nav" (branch web/r9-nav-1018, from live main 00328e54 = release 8; local, not pushed, not deployed; nothing applied to any database)

**Scope:** navigation, Practice, the runner, Colleges, Progress and the global chrome, from the read-only audit of release 8 (tmp/ledger-audit-1018/results.json) and the CEO decisions. Practice credit amounts and credit copy are untouched (the per-question agent owns them) and the Mob entry is not added here (the Mob agent does). Screenshots (390 x 844 and 1440 x 900, Night and Day, real pointer clicks where interaction is the fix): tmp/r9-fixes/nav/.

| Item | What changed | Proof |
|---|---|---|
| D11 + N17 | "Help" is "Guide" as a nav label (sidebar Account group, phone More sheet) and the page is "Guide and questions" (route stays /help; tab title and top bar follow). "Show me around" (the tour) is the first row of the More sheet card and a row under the sidebar Account group; both start the tour. The tour's last stop is named Guide. | more-390-night/day.png, sidebar-1440-night.png, guide-page-1440-night.png, tour-from-more-390-night.png, tour-from-sidebar-1440-night.png; release9_nav_1018 tests |
| Marks trend | /analytics nav label "Weak chapters" is "Marks trend" (sidebar, More sheet, assistant feature guide, the Colleges bridge link now says "See the chapters to work on in Review" and goes to /review). One line in the sheet column at 390 (row 48 px high, label 22.5 px). | more-390-night.png |
| D6 | The More-sheet Ask Mobi row is above the theme control (its own row under the account card, like Learn's row below it); Planning no longer lists it again; the sidebar keeps it in Planning. | more-390-night/day.png |
| W-075 / new MEDIUM | Colleges: signed in, "Go to Practice" is outlined (and "Open my chapter review" is quiet text, now pointing at /review); signed out the sticky "View courses" steps back while the page's closing lime key is on screen. The scan (data/tests/helpers/voltScan.mjs) found 2 keys on release 8 at 390 and 1440 and finds at most 1 now at every 100 px of scroll, 390 and 1440, Night and Day. | colleges-bottom-390-night.png, colleges-bottom-1440-day.png, scan-volt.mjs output; browser test in release9_nav_1018 (MM_PREVIEW_BASE) |
| New LOW (Practice bar + dock key) | pagePrimary.mjs: the dock key goes quiet at once when any of the page key shows (SHOW_AT 0.05, HIDE_AT 0.02; no settle on the way in), and a second thin observer watches the strip of page under the dock capsule, where a key rising from the bottom edge first peeks out. Only the return to lime waits the settle time. 20 px wheel steps through 480 to 960 px and back at 390: 0 frames with two lime keys in Night and Day (release 8: 2). | scan-practice-band.mjs; dock_primary_quiet tests (24) |
| W-079 | 44 px: Practice "Edit fine-tune" (54 x 44), chapter picker "Whole unit" (68 x 44), runner legend buttons (262 x 44), "Go to question" and Undo, Start sheet arrows (the hidden arrow no longer sits at 0.82 scale = 36 px; the disc is 44). | measured in shots3/4/5 scripts |
| New LOW | Runner notice reads "Saved on this device. Stay online to submit." ("Bank in review" is gone). | runner-1440-night.png, runner-390-day.png |
| N6 | The subject-cap note: "That is the CUET UG 2026 limit: five papers in all (a language or the General Test counts as one)." One sentence, built from CUET_RULE_CYCLE. | onboarding-subjects-390-night.png |
| D8 / New LOW | Ask Mobi row and the AI-credit chip: Orbit (read as a "not allowed" sign) is replaced by a sparkle, the Lucide Sparkles for the row and the same four-point sparkle inside the coin for the chip. | icons-topbar-night.png (3x), icons-sidebar-planning-day.png (3x) |
| New LOW | PlanCard: the "Free" / "Pro" pill is quiet meta text (there is one pill in PlanCard, not two; the other pr-badge is the Contribute submissions list on Practice, off while Contribute is off, outside this packet). | account-plan-1440-night.png |
| New LOW | Progress at 1440: earned badges appear in the shelf only; the four path lists keep next, locked and unknown rows and the header counts ("3 of 5"); a path with every badge earned says "All N earned". The phone's All badges sheet still lists everything. | progress-badges-1440-night/day.png (earned rows in lists: 0, shelf 6) |
| D7 | Night: an earned medal is a charcoal disc with a thin lime ring and a lime glyph (wash and line tokens, no fill, no glow); medal art unchanged; Day keeps the solid medal. | progress-badges-390-night.png, progress-badges-1440-night.png |

**Not changed on purpose (outside the packet):** the result page's "Open weak chapters" link still goes to /analytics under that old name (result files); the public footer still says Help; Account's "Help" section heading; Today's "Weak chapters" heading and the first-week step name; the Practice card's Start key at y=884 on a 1440 x 900 first load (audit LOW, not in this packet).

**Checks:** lint clean on every changed file; test:app 668 (667 pass, 1 skipped by design: the browser walk needs MM_PREVIEW_BASE); test:dock 32 (31 pass, 1 skipped by design); test:today 87; test:subjects 30; test:du 42; test:recovery 589 (586 pass, 3 todo); test:learning 357; test:billing 161; test:auth 110; test:nta 188; release9_nav_1018 run against a preview server (MM_PREVIEW_BASE=http://localhost:3243): 15 of 15 pass, including the one-lime scan at every 150 px of scroll on Colleges and Practice (390 and 1440, Night and Day). The scan found 2 lime keys on release 8's CutoffCalculator and finds 1 now. `next build --webpack` passes (exit 0; .next deleted after).

## 18 October 2026 - Website release 9, packet "public" (web/r9-public-1018, from live main 00328e54 = release 8; local, not pushed, not deployed; no database step)

Commits 706b1fe9, 164d26e3. Proof: data/tests/release9_public_1018.test.mjs (16 tests, in test:app and test:billing) and the headless walk in mockmob-next/tmp/r9-fixes/public (390 x 844 first, then 1440 x 900, Night and Day, reduced motion; real pointer on the sample answer and the footer Help; walk-*.json hold the read values).

- **MEDIUM truth, /pricing/ai-credits:** the closed branch now says "New top-ups are paused for now. Your monthly credits work, and credits you bought are kept." Replies are tied to runtimeAi, top-ups to aiCommerce (aiCreditsCopy.mjs); rules checked, none said replies. Proof: test "never says written replies are paused"; ai-credits-390-day.png, walk-pages.json pausedReplies false at 390/1440 Night/Day.
- **MEDIUM truth, onboarding step 1:** "...one live question bank: no cap on Pro, and on Free each one uses practice credits." Proof: test; onboarding-390-day-subjects-v2.png.
- **M-006, bolder onboarding:** "Your papers. Your mocks." / "Your papers, your call." / "How many days a week can you give?" / "Which colleges are you chasing?" with matching leads, all facts unchanged (5 subjects, 8 colleges, Skip = 4 days). Copy lives in paperCopy ONBOARDING_STEPS. Proof: test; onboarding-*-v2.png, onboarding-*-days.png, onboarding-*-colleges.png.
- **MEDIUM, landing "leaderboard" x3:** now "Your standing", "Benchmarks and your standing", "...toward your standing", "See your standing" (route /leaderboard unchanged). **LOW:** "The mob speaks." -> "Students, in their own words."; ArenaPreview "Students solved it in". Proof: tests.
- **MEDIUM (CEO decision), price framing:** checkout today charges pro_cuet_2027, Rs 99 once, access to 31 July 2027, no renewal (create-order + plans.js; monthly opens only with RAZORPAY_PLAN_ID_PRO_MONTHLY_99, unset). The /pricing H1 ("Pro is Rs 99 once, through 31 July 2027."), the Pro tag ("Rs 99 once"), the page title and the landing trust row now read priceHeadline / priceTag / priceLine (src/lib/payments/offer.js), so they switch together to "a month" when monthly opens. No price or plan changed. Proof: tests; pricing-390-night.png, pricing-1440-day-plans.png.
- **LOW, two lime keys after a sample answer:** at 960 px and up the hero key steps down to secondary after the first answer (demoSignal.mjs; phones keep it). Proof: walk-landing.json limeAfter = answer chip + "Next question" only; landing-1440-night-after-answer.png, landing-1440-day-after-answer.png.
- **LOW, tour chips clipped at 1440:** from 900 px the row wraps with no mask and tighter chips (all 9 in one row at 1440, none clipped); below 900 it snaps and fades 48 px. Proof: walk-landing.json tourChips clipped []; landing-1440-night-tour.png, landing-390-day-tour.png.
- **LOW, aurora wash (L-019):** .lp-bg__aurora removed from the hero and the close, with its rules and parallax; grid and dots kept. Proof: test; close-1440-night.png, close-390-day.png.
- **LOW (L-013), footer Help:** guests go to /#faq (the landing's public questions, scroll margin + HashSettle so it lands from any page), signed-in students to /help (FooterHelpLink). Proof: walk-help.json (8 real clicks, URL /#faq, heading under the nav); help-night-390-from_pricing.png.
- **LOW, auth repeats:** login card says how you get in ("Use Google, or get a one-time code by email. No password to remember."); signup card "Free to start. No card needed."; "stay signed in" once per page. Proof: test; login-1440-night.png, signup-390-day.png.

**Files outside the packet list (smallest change):** src/lib/payments/offer.js (two new helpers), src/components/ui/SignupCard.jsx (the auth card copy), src/components/LandingActions.jsx, src/app/home-refinements.css and src/app/marketing-theme.css (aurora rules), data/tests/billing_pay_gate_copy.test.mjs and pricing_copy_1017.test.mjs (old assertions for "a month" H1 and the old onboarding lead), package.json (test wiring).

**Checks:** lint clean; test:app 669; test:billing 177; test:subjects 30; test:auth 110; test:learning 357; test:today 87; test:recovery 586 pass, 3 todo; `next build --webpack` ok (.next deleted).

## 18 October 2026 - The Mob merged onto release 8 and gated on staging 10/10 (branch web/r9-mob-1018, from live main 00328e54; local, not pushed, not deployed; NOTHING applied to production)

**Merge:** web/mob-fix-1017 (e89d4a35: Mob web code, gate fixes 1 to 5, migration 20261017190000_mob_fix_1017 + undo) into release 8. Conflicts resolved by intent, every release 3-8 change and every Mob fix kept: package.json (test:app, test:mob list all six Mob suites: mob, mob_plans, mob_ui, mob_fix_1017, mob_render_size, mob_gate_1018), mob.css (both blocks), Practice (the release 8 PracticeMobChip stays; the old MobEntry row is dropped, it would have doubled it), Today (the release 8 TodayMob row stays; MobEntry stays only as the one-time invitation for a student in no Mob, with a new inviteOnly prop, so a member sees one Mob row, not two), Progress (MobTodayCard stays), Review (the Review page was rebuilt, so the Mob row now sits under Also in Review in ReviewChapters as a matching row). The nav item, the tour step and the page title now say Mob (not Your Mob). mob_fix_1017.test.mjs asserts the new wiring and that inviteOnly stays quiet for a member (a first draft of that guard had silently not applied; the gate caught the double row on Today and it is fixed and locked by the test).

**Staging database:** compared, not guessed. All 26 Mob and rate-limit functions have the same md5 of their body as the two repo migrations; all Mob tables have RLS on and no anon or authenticated grant; mobs.created_by, mob_members.share_moved_1017, show_score default true, mob_departures, mob_data_moves all there. Nothing needed applying. Staging Mob data and persistent_rate_limits were truncated before the run (test data only).

**The gate, on staging (Supabase onwkqxmjqjrhfbjjdydu), local server from this worktree through the staging launcher on port 3231 with MOB_ENABLED=true and PERSISTENT_LIMITS_ENABLED=true, test accounts mobtest-* only, headless playwright-core, two separate browser contexts:**
1. Plans and caps: Free starts one (MOB_LIMIT), Pro starts 3 and the 4th is MOB_LIMIT_PRO before the weekly create wait, four failed starts never use the weekly limit, the 4th start in a week is 429 with the real date in the sentence.
2. Invite, join, full, rejoin: 5 members, a 6th is MOB_FULL (join and lookup), eleven wrong codes still leave a real join through, leave, a spent link says expired and a new link fills the seat, rejoin.
3. The weekly paper: same 10 questions in the same order and options in both runners, clock 10:00, no credits charged (balances equal before, during, after, also after leave and rejoin), a second start is PAPER_ALREADY_SAT, the free claim outlives the membership across Mobs.
4. Side-by-side: free teaser, one free sample, trap only after the sample or Pro, sharing on by default and the opt-out hides score and picks, Pro full, extras (3 a week, free members sit them), history.
5. Nudges, reports, blocks, owner handover, remove (only the owner), removal is not a block.
6. Rate limits: create and join count successes only, invites 5 a day, reports 10 a day, reads 120 in 10 minutes, each 429 with Retry-After and the real wait.
7. Crafted requests: signed out 401, 4 KB body cap, non-boolean flag, no price in a body, no user id or email in any view, comparison or public lookup, PostgREST direct reads and rpc refused.
8. Screens at 390 x 844 and 1440 x 900, Night and Day: no Mob, start, create-limit error, invite dialog, join page (signed out, signed in, bad, full, paused), one member, waiting, all sat, shared and opted out, the trap, free sample, Pro full, extras dialog, member menu, report, remove, block, name, leave dialogs, error, loading, the two-context end to end (18 UI checks).
9. Entry points: sidebar and More sheet say Mob, Today row, Practice chip, Review row, Progress card, result row, privacy section.
10. Flag off and kill switch: with MOB_ENABLED unset every /mob and /join page and every /api/mob route is a real 404, no Mob link or word on Today, Practice, Review or Progress at 390 and 1440 in both themes, no request to /api/mob (33 checks); with MOB_INVITES_ENABLED=false invites and joins answer 503, members keep their Mob.
Counts: API gate 98 of 98, end to end 18 of 18, flag-off 33 of 33, kill switch 7 of 7 (one of them re-run with a fresh account because a daily invite limit had been used up on the first). Screenshots (opened): tmp/mob-gate-1018b (not committed).

**Suites:** lint clean; test:mob 71; test:app 679; test:today 87; test:recovery 586 pass, 3 todo; test:learning 357; test:auth 110; test:billing 161; next build --webpack ok (.next removed).

**App (wt-v15, read only):** every route, method, body and reply field in mob_repository.dart, mob_paper.dart and mob_models.dart matches the merged web API; the 9 JSON fixtures are byte-identical to data/tests/fixtures/mob; all 48 server error codes are known to the app. Only ALREADY_IN_MOB is unused (the server answers a view for a link to a Mob you are in).

**Findings (none blocks switch-on):** timer is re-issued from now when a started paper is reopened before submitting (same as ordinary practice); the runner heading for a Mob paper says Quick practice; a link has as many uses as seats when it was made, so after a leave it is spent and the owner makes a new one; the leave dialog says sittings leave with you, true at that moment, but a rejoin credits the saved result again (so no second paper); the web page ignores ?mob= (the switcher is not in the URL); the no-Mob line on the result page from SOCIAL-SPEC section 9 is not built; the Today invitation is covered by tests, not walked in a browser.

**Production plan (main session applies):** migrations 20261017100000_mob.sql then 20261017190000_mob_fix_1017.sql (production has no mob tables, persistent_rate_limits and take_rate_limit exist, users.id is text); env MOB_ENABLED=true, PERSISTENT_LIMITS_ENABLED=true (production has neither; without it the weekly create limit is per instance), optionally MOB_ID_SECRET; then redeploy. Undo: unset MOB_ENABLED and redeploy; schema undo files are in supabase/undo.

## 18 October 2026, about 4:05 pm IST - Website release 8 shipped (main 00328e54) and production migration 20261018130000_free_ai_wallet_50 applied (owner: "Ship it", about 3:55 pm)

**Order:** the migration first, under the owner's standing production grant, then the code (the code is backward compatible with the old database; "50 on Free" is true only with both).

**Migration on production (isrxrxzjocewrdureyhp), about 3:57 pm:**
- **Pre-check:** `runtime_ai_budget.student_user_free` = 0.0114; `md5(prosrc)` of `mm_ai_consume_credits` c0b40176... and `mm_ai_reserve_credits` 75c8ea15... equal the bodies in `supabase/undo/20261018130000_free_ai_wallet_50.undo.sql` (LF endings).
- **Applied:** `apply_migration free_ai_wallet_50`, the file's SQL unchanged.
- **Post-check:** the two bodies hash c1ce92df... and 499b44d1..., equal to the migration file's; `student_user_free` = 0.0284; the global `student_ai` row is untouched (1000000).
- **Dry spend (in a DO block that raises, so everything rolled back):** a real Free wallet stored at 10 (4 used, a May period) read 50 left at amount 0, then 49 after consuming 1, then 47 after reserving 2. Afterwards: 0 ledger rows and 0 reservations with the dry-run keys; 811 wallets still store 10 and sync to 50 on their next spend.
- **Undo:** `supabase/undo/20261018130000_free_ai_wallet_50.undo.sql` (roll the code back first).

**Code:** `git push origin 00328e54:refs/heads/main`, a fast-forward from fc9e1f6b (release 7). Contents are in the "Web release 8 integrated" entry below: W-078, W-075, W-079, W-093, W-089, W-064 (first-week path, repair receipt), W-032 (sealed mistake rows, Try it again before the key), the D38 landing hero, D53 (the quiet AI line), D54 (Free AI wallet 50), plus the post-verify fixes (desktop hero Mobi flash, Review Repair through the sealed sheet, Lab Cinema glow removed L-019, hero buttons at 761-899 px L-013). The independent re-verify said GO; the owner had the live preview from about 2:30 pm.

**Deploy:** Vercel dpl_3THyGFBktbdxcAuwhfN2sLNsHmrT READY at about 4 pm, aliased to www.mockmob.in. Runtime errors in the 20 minutes after: none. Smoke: /, /pricing, /pricing/ai-credits, /features, /today, /review, /help, /api/stats 200; an unknown path 404 (themed). Live /pricing reads "50 a month on Free"; no "10 AI credits" left.

## 18 October 2026, about 1:10 pm IST - Website release 7 shipped (main fc9e1f6b): the new Today, Road to CUET, the Change plan receipt fixes

**What:** deploy/web-1018-r7 (contents and conflict notes in "Web release 7 integrated" below), plus the verifier fix round for H1 (the Change plan receipt seeded a stale mock target), M1-M3, M5-M7, L4 and L5. The owner approved the new Today at 8:40 am ("the today page is better now").

**Checks:** independent verifier GO after the fix round. Vercel dpl_FYgR76nTTSeX5uV4ShJed1u1Rq5A READY, 0 runtime errors at 1:20 pm. Nothing was applied to any database.
## 18 October 2026 - Google Play billing, server side (branch web/play-billing-1018, from live main 00328e54 = release 8; local, not pushed, not deployed; NOTHING applied to production)

**Owner (18 Oct, 6:25 and 6:38 pm):** the Android app sells Pro and credit packs through Google Play Billing at the Play Console price (Pro Rs 150 final; web Rs 99); same entitlement, same tables as the web. Plan, owner steps, env vars, deploy order, rollback: `docs/brain/PLAY-BILLING-PLAN-1018.md`.

- **Built (behind `PLAY_BILLING_ENABLED=true`, both routes 404 otherwise):** `POST /api/billing/play/verify` (signed in, bearer or cookie, persistent money limiter 15/10 min, Google `purchases.products.get`, package + purchaseState + quantity + obfuscated account hash checks, atomic idempotent grant, then acknowledge Pro / consume packs) and `POST /api/billing/play/rtdn` (Pub/Sub push, token + optional Google OIDC, once per message via webhook_events, voided purchase revokes). Google auth is the service-account JWT flow on node:crypto + fetch, no new dependency, token cached until a minute before expiry.
- **Product map (D78, one credits balance, 6:50 pm):** `pro_cuet_2027` (Pro to 31 Jul 2027), `credits_10_50` / `credits_29_150` / `credits_49_300` (50 / 150 / 300 credits as bonus credits through `mm_ai_grant_bonus_credits`, idempotent on the token), plus the earlier `ai_credits_prepos_*` ids kept accepted. No separate practice products. Proposed Play prices Rs 15 / 45 / 75; Pro Rs 150. The `credits_*` ids are defined in the Play map because `src/services/credits/creditPacks.mjs` is not in this branch: the integrator points the map at that catalogue. Gaps: `pro_monthly_99` (Play subscription not built), v2 and 2026 passes.
- **Migration (NOT applied):** `20261018190000_play_purchases` + undo. `play_purchases` (unique token, RLS, server only), `mm_play_grant_purchase` and `mm_play_revoke_purchase` (security definer, service_role only). No enum or users change (an earlier Practice-pack draft was removed under D78).
- **Also touched:** `data/db.js` (a Play Pro purchase in force counts as other paid access, so Razorpay cancel/refund cannot switch it off), account deletion plan (play_purchases kept, Google payload scrubbed).
- **Staging dry-run (onwkqxmjqjrhfbjjdydu), rolled back, nothing left:** grants, replays, other-account refusal, voids for Pro and a credit pack, privileges (the final migration differs from the dry-run text only in a comment).
- **Checks:** `play_billing.test.mjs` 45/45 (JWT, mocked Google, wrong package, pending, other-account token, replay, ack vs consume, void revoke, flag off 404, no client price, OIDC, the SQL on PGlite with the real migrations); test:billing 207, test:auth 110, test:app 653, test:recovery 586 pass + 3 todo, lint clean, `next build --webpack` ok.
- **Not verified:** the live Google API (no credentials). The internal-testing purchase is the real check.

## 18 October 2026 - Web release 8 integrated (deploy/web-1018-r8, from live main fc9e1f6b = release 7; local, not pushed, not deployed; nothing applied to any database)

**Merged, --no-ff, in order:** web/r8-fixes-1018 (cb672f6b), web/r8-adopt-1018 (dfc6797e), web/r8-retry-1018 (f9fa1d82), web/land3-1018 (42b51dd3), web/credits50-1018 (d8bc38d8). Every R7 fix is kept.

**Conflicts:** (1) adopt: `package.json` test:today lists both the R7 fixes test and the first-week tests; `today/page.jsx` imports keep R7 keepLength and readLength and add firstWeek. (2) retry: `package.json` test:recovery lists repair_receipt and retry_first; `ResultPageClient.jsx` reset effect keeps adopt's repair-record read for the receipt and adds setRetried. (3) credits50: `docs/brain/STATUS.md`, both sections kept. fixes and land3 merged clean.

**Also:** `test:app` now runs the landing hero, copy, Mobi and position tests (land3 added them but wired none).

**Checks:** lint clean; test:app 647; test:today 87; test:recovery 586 pass, 3 todo; test:learning 357; test:auth 110; test:billing 161; test:dock 28 pass, 1 skipped by design (needs DOCK_BASE_URL); `next build --webpack` ok.

**Gate before deploy:** the D54 migration `20261018130000_free_ai_wallet_50` must be applied on production first (code is backward compatible), then the code. Not applied here.

## 18 October 2026 - Free AI wallet 10 -> 50 a month (branch web/credits50-1018; local, not pushed, not deployed; NOTHING applied to production)

**Owner, 12:15 and 12:30 pm (D54):** free users get 50 AI credits a month (Pro stays 50 included); the server, the app and the website change together.

- **Code:** `AI_FREE_MONTHLY_CREDITS = 50`; `AI_FREE_BUDGET_INR_CAP = 2.5` (it said 5 but production enforced Rs 1; it now mirrors the database row). Every reader (api/ai/credits, getDailyUsage, wallet projection, the Ask Mobi composer line, the AI credits page) takes the constant, so they move together.
- **Copy:** /pricing (plan terms, free notes, Ask Mobi section), /features, landing Ask Mobi card, askSuggestions fallback. /pricing/ai-credits reads the constant. No text elsewhere (help, FAQ, terms, refunds, emails, data/*.json) stated the Free number.
- **Migration (NOT applied on production):** `supabase/migrations/20261018130000_free_ai_wallet_50.sql`, undo `supabase/undo/20261018130000_free_ai_wallet_50.undo.sql`. (1) `mm_ai_consume_credits` now syncs a wallet row's stored allowance to the one the server sends mid-month (mm_ai_reserve_credits already did), so a student who used 4 of 10 has 46 of 50 left with no one-time grant; before this, the app would have shown 46 while Ask Mobi chat still enforced the stored 10. (2) `mm_ai_reserve_credits` null-allowance fallback 10 -> 50. (3) `runtime_ai_budget.student_user_free` USD 0.0114 (Rs 1) -> 0.0284 (Rs 2.50). Pro 0.0568 and the global row untouched.
- **Cap evidence (production, SELECT-only, 18 Oct):** a reply settles at about USD 0.00029 (gpt-6-luna 9 requests avg 0.000299, max 0.000479; the 4 requests carrying a user id avg 0.000289) and each request is checked as spent + a reservation of about 0.00155. The old Rs 1 cap stops a free student after about 33-34 typical replies; 50 need about 0.0165; 50 at the observed maximum need about 0.0255; Rs 2.50 = 0.0284 covers both and a failed attempt or two.
- **Staging dry-run (onwkqxmjqjrhfbjjdydu):** migration applied by SQL, then in rolled-back blocks: stored 10 with 4 used + server 50 -> consume leaves 45 left, reserve 44; a new Free user spends exactly 50, the 51st is refused (insufficient_ai_credits); null allowance falls back to 50; a stale previous-month row resets to 49 left with 5 bonus kept; reserve_runtime_ai with the free tier: 34 typical replies before the old cap stopped, 80+ (loop limit) under the new cap, 57 at the highest cost seen. Then the undo was run: both function hashes equal production's pre-change hashes (cbd55d39..., bf56e49a...) and the free cap is back at 0.0114. Staging's two functions had drifted from production before (older consume body, anon/authenticated could execute it); they now hold production's bodies. No test rows left.
- **Deploy order:** apply the migration first (it is backward compatible with the old code: old code still sends 10, the new consume then syncs a row down to 10), then deploy the code. Roll back = code first, then the undo.
- **Global student-AI ceiling:** the task brief said USD 25 stays; production's `student_ai` row reads 1000000 (the owner removed the ceiling on 17 Oct, AGENTS.md). This work does not touch that row either way.
- **Practice credits (unchanged):** a new account starts with 100 practice credits (users.credit_balance default 100); Quick practice costs 10 (5 to 20 questions), Full mock 50; the daily login grant is switched off (grant_daily_login_credits returns false); +15 per approved contribution; no monthly refill. So a free student's 100 buys 10 Quick sessions, or 2 Full mocks, or a mix. Mob papers, Revise, Learn and the five-question baseline use no credits.
- **Checks:** test:billing 161/161 (includes the new data/tests/free_ai_wallet_50.test.mjs, 8 tests: constants, copy, wallet projection, the migration and its undo on PGlite); test:learning 357/357; test:recovery 556 tests, 0 fail (3 known-gap warnings); test:app 595/596, the one failure (release6_fixes_1018 'Review at 0 AI credits...') is a CRLF-checkout artefact in this worktree (its regex needs LF line endings; it passes in wt-rel7), not from this change; lint clean; `next build --webpack` ok; /pricing and /pricing/ai-credits at 390 and 1440, Night and Day: no horizontal overflow, the page text states 50 and nowhere 10.

## 18 October 2026 - Web release 8 adoption pieces: the chained first-week path and the after-the-mock repair receipt (web/r8-adopt-1018, from release 7 c46d1dcd; local, not pushed, not deployed; nothing applied to any database)

**Owner items:** W-064 and F18 (students did not use 90% of features because nothing led them); FEATURE-ADOPTION-2026-10-17 items 5 and 7.

**1. The first-week path** (`src/lib/today/firstWeek.mjs`, pure; wired in `page.jsx`, `TodayMove.jsx`):
- Seven steps, one a day, the doc's order: day 1 Find and fix (the 10-question starting set, then a Repair), 2 Revise, 3 practice aimed at the weakest chapter (smart practice on Pro), 4 a first set in a second subject, 5 the first full mock, 6 repair what that mock found, 7 Change plan.
- Clock: the first scored session (rhythm `first_scored_session`; the account start date is not among Today's reads, so it is not used). Nothing saved is day 1. After day 7, or when every step that applies is done, the path is gone.
- Done is read from data the page already holds: a saved session plus a Repair (or nothing left to repair); Revise used (asked today, or an active card above box 1); a second session; papers in two subjects; a saved full or NTA mock; a Repair on the newest mock; a date, mock target or study days saved. Unknown reads never tick and never lead.
- Today's step replaces the lead only while it is undone and the product can do it now. It never replaces a session waiting, a check, "Done for tonight" or a failed read. The regular move waits among the two choices; "More ways to practise" stays. A step passed stays a quiet open mark and is never nagged.
- The lead's overline says "Day 3 of your first week"; under it a rail of seven marks (done = ink disc with a tick, today = ink ring, passed = quiet ring, ahead = dot, not applicable = dash). No volt, no checklist, no labels; a screen reader hears one sentence. The day 7 key is a button that opens Change plan.
- The lead holds as loading, 1.5 s at most, while the reads that decide today's step are in flight, so it lands once.

**2. The receipt** (`data/repair_receipt.mjs`, pure; the result's summary card, and one line under Last paper on Today):
- Counts the student's saved repairs made before the paper (repair record, one per question). If a repaired question came up again on the paper: "Of the 6 mistakes you repaired, 2 came up again on this paper. You got both right." (nothing is said if none was right, and the chapter is never swapped in). Otherwise, repaired mistakes in chapters this paper asked about, answered at least twice (one lucky answer is not evidence of a chapter) and got none wrong: "Of the 6 mistakes you repaired, 4 are in chapters where you got nothing wrong on this paper." No line when there is no repair before the paper, the record did not load, nothing matches, or there is no good news. No cause and no marks claimed.
- The result page reads the repair record in parallel with the paper (the same read Today makes) and waits for it 0.5 s at most so the line is in the first paint.

**Preview fixtures (dev only):** `/preview/arena?view=today&firstweek=1..7` (a student on that day who followed the path to yesterday; real rhythm engine and scorer); `&receipt=chapter|question|none`; `?view=result&firstweek=6&attempt=fw-p5` opens the first full mock with the receipt.

**Tests:** `first_week_path.test.mjs` (16) and `today_release8.test.mjs` (6) in `test:today`; `repair_receipt.test.mjs` (11) in `test:recovery`.

**Checks:** today 75 pass; recovery 564 pass, 3 todo, 0 fail (was 553); learning 357; app 595 pass and 1 fail that is there before this work too (`release6_fixes_1018`, "Review at 0 AI credits", a CRLF-sensitive regex in a Windows checkout). eslint clean on every changed file. `npx next build --webpack` exit 0; `.next` deleted. Headless Chrome (playwright-core, own temp profile, own dev server on :3217, preview fixtures only, stopped): days 1 to 7 and the receipt in Night and Day at 390 and 1440, each capture looked at, a real pointer click opening Change plan from the day 7 key and swapping the lead on day 3, no horizontal overflow, no console errors; the rail fits at 320 and under reduced motion shows its ticks with no animation. Captures: `tmp/adopt/`.

**Known limits:** the day 3 step is "done" by a second saved session (the summary does not say which chapter a set was aimed at); Check it held is not used as a step because the repair record's `checkedState` is `not_available` on this codebase; the receipt's chapter rule is a proxy and says so in its own words (a chapter counts as clean only on two or more answers). Not measured: production timing and a real account's history.

## 18 October 2026 - Web release 7 integrated (deploy/web-1018-r7, from live main 70c4598c = release 6; local, not pushed, not deployed; nothing applied to any database)

**What it is:** the new Today (TODAY-1018, branch web/today-1018 at d0486c12; the owner at 8:40 am: "the today page is better now") merged onto release 6. Today files are the 1018 design; every R5 and R6 change in the shared files is kept (Help and FAQ with no Help door, "Learn", community hidden, the Ask Mobi panel and nav row, badges, not-found pages, the docked-panel rule that stacks Today's columns at 1280 to 1439).

**Conflicts and how they were resolved (by intent):**
- `src/app/(app)/today/page.jsx` and `src/components/today/TodayMove.jsx`: the 1018 versions won. R6's "Why this?" was re-attached to the new lead card (below).
- Auto-merged and checked: `package.json` (R6's suite lists plus `test:today` now with `today_release7.test.mjs`), `ArenaPreviewClient.jsx` (R6's preview routes kept, two fixture states added), `today.css` (R6's 44 px sentence-link rule kept).

**Owner items on the new Today:**
- **D36, "Why this?"**: AskMobiLink (ASK-MOBI-1018) is in the lead card's reason paragraph, right after the reason text, 68 x 45 px (hit-tested at the top, centre and bottom). It opens the Ask Mobi panel with the lead's reason answered free, and it follows the lead: a swapped card (tap a choice) asks about the swapped move. It takes the place of the "See why" link to the record page, so the card never has two ways to ask why.
- **D15 wording**: "mistakes to repair first" is now "mistakes to repair" (priority is order, never a label); in Weak chapters each mistake's one action is `actionLabel` from `data/repair_presentation.mjs`: Repair, Check it held, See repair, Try it again (`src/lib/today/mistakeAction.mjs`). The lead's key still reads "Start repair" with its minutes: it starts a run of several, not one question.
- **D29, "Play your paper back, 20 s"**: after a fresh submission (newest paper saved within 3 hours) Today shows a card once in the lead's place (`TodayReel.jsx`, `src/lib/today/paperReel.mjs`). It builds the reel with the result's own engine (`reelScript.mjs`, shared with the result page: same analysis, time read, costliest chapter and next move) from the cached attempt read that Last paper already makes. One volt key plays it in the result's own `PaperReel`; "Not now" is one tap. The card is marked seen once it has been on screen (last 20 attempt ids in localStorage `mm:today-reel:v1`), and Up next returns. A paper that cannot be read or has nothing answered hands the lead back at once. The seconds in the title come from the script (5, 10, 15, 20...).
- **D28, greeting**: Hello from midnight to 5 AM survives (the 1018 greeting.mjs, tested).

**Preview fixtures (dev only):** `/preview/arena?view=today&reel=fresh` (a new attempt every load, so the card shows every time) and `&reel=stable` (one attempt id: shows once, a reload brings Up next back); `&repaired=chapter` (weak chapter with one Check it held, one See repair, one Repair).

**Tests changed because the owner replaced the behaviour:** `today_1017.test.mjs` (two asserts: the label "mistakes to repair first" is now "mistakes to repair", D15); `ask_mobi_entries.test.mjs` (the page wiring regex now reads `todayContext({ move: lead, ... })`: the 1018 lead is named `lead`, not `move`; the entry, its label and its context are unchanged). New: `data/tests/today_release7.test.mjs` (9 tests).

**Checks (after the merge, in this worktree):**

| Suite | Result |
|---|---|
| recovery | 553 pass, 3 todo (known gaps), 0 fail |
| app | 596 |
| learning | 357 |
| auth | 110 |
| billing | 153 |
| nta | 188 |
| today | 53 (was 32; 9 new in today_release7) |
| mob | 45 |
| subjects | 30 |
| du | 42 |
| dock | 7 pass, 1 todo |
| community | 11 |
| study | 37 pass, 1 fail: the known wordnet LICENSE_UNAVAILABLE |

- eslint is clean on every changed file. `npx next build --webpack` exits 0; `.next` deleted.
- Headless Chrome (playwright-core, own dev server on :3117, preview fixtures only, stopped): "Why this?" hit-tested at 390 and 1440; its click opens the docked panel with the reason answered; docked at 1280, 1440 and 1920 with no horizontal overflow; the reel card at 390 and 1440 in both themes, the reel plays and closes and Up next returns, "Not now" returns Up next, `reel=stable` shows once and a reload brings Up next back; Weak chapters shows Check it held, See repair and Repair.

**Result page `?q=N` (coordinator decision, after the merge):** Today's "Repair this leak", the Weak chapters links and the reel's last key send `/result/{id}?q=N`. The result page now reads it once the paper is loaded and runs `jumpTo(N)`, the same path as a press on that question's bubble: Your mistakes (or the part that owns the row) opens, the row expands and scrolls into view with its Repair button, and focus lands on the row. It never passes `{ repair: true }`, so it never sets `autoRepair`: no paid repair can start from a URL (checked in the preview: no POST was made). A missing, non-numeric or out-of-range N does nothing. `src/components/result/questionParam.mjs`; `data/tests/result_question_param.test.mjs` (2 tests, in test:recovery) pins the parse and that the effect never reaches `setAutoRepair`. recovery is now 553 pass, 3 todo.

**Known gaps found while merging:**
- The working tree of this worktree has CRLF line endings (core.autocrlf), which breaks one regex in `release6_fixes_1018.test.mjs` (`practiseLine` match on `
`); the index is LF and the test passes on an LF checkout.


## 18 October 2026, about 7:25 am IST - Website release 6 shipped (deploy/web-1018-r6): Review and result 1018, Ask Mobi 1018, community and Learn, badges

**What shipped, by owner item (OWNER-FEEDBACK-2026-10-18-DAWN.md):**
- **Review and result:**
  - Review leads with weak chapters (D18).
  - One action label per mistake, and the counts agree (D15).
  - The analysis index is calm, with one part open at a time (D16).
  - The replay is sized to the paper; a paper with nothing to replay says so (D17).
  - "Play your paper back" reel (D29).
  - A saved repair opens free (F17).
- **Ask Mobi** is one panel opened in context, with no tabs, nothing under the theme switch, a real Day panel, and the cost shown before a paid ask (D6/D12).
- **Contribution features** are hidden behind CONTRIBUTE_ENABLED: /upload and /my-uploads show the calm paused page. Your standing is under Progress, and Learn is in the Study group (COMMUNITY-1018, D20).
- **Badges:** "Badges, n of 16" on Progress, tap to explain, and a one-time "Badge earned" row on the result (D19). `forgetBadges` runs after an attempt is saved.
- **Unknown URLs** get a themed not-found page.

**Merges onto R5 (58bc53f6):** web/r6-community-1018 (f9f28fba), web/r6-review-1018 (0b7ae8a4), web/r6-askmobi-1018 (d5287d3d), web/badges-1018 (9f897ef8).

**Checks:**
- Suites:

  | Suite | Result |
  |---|---|
  | recovery | 551 pass, 3 todo |
  | app | 596 |
  | learning | 357 |
  | today | 32 |
  | community | 11 |
  | auth | 110 |
  | billing | 153 |
  | nta | 188 |
  | mob | 45 |
  | subjects | 30 |
  | du | 42 |
  | dock | 7 (1 skipped) |
  | study | 37 of 38 (the known wordnet LICENSE_UNAVAILABLE) |

- eslint clean; next build --webpack exit 0.
- **Visual check:** an independent verifier (210 captures, 390/1440, Night and Day, real pointer clicks) gave NO-GO on 1 HIGH: the docked Ask Mobi broke the result at 1280-1366. A fix round (10 commits) fixed it and 8 MEDIUM/LOW items:
  - the layouts now use container queries;
  - the root not-found page;
  - the Time part says what the paper holds;
  - Progress CLS went from 0.198 to 0.006;
  - 44 px targets;
  - the Ask panel without lime;
  - the reel moments in clock order;
  - focus after Esc;
  - no duplicated heading.

  The fix round re-checked with ~50 captures at 1280/1366/1440 docked, Night and Day, with 0 mid-word breaks. The main session looked at the docked result and Review captures.
- **Practice zero-credit line:** left honest. Practice credits do not renew, so no renewal date is shown there.

**Approval:** the owner at about 4 am: "Push everything that passes".

## 18 October 2026, about 4:50 am IST - Production migration 20261017160000_revise_cards_mode applied (owner's standing grant)

- **Applied by:** the main session, through the migration tool as "revise_cards_mode", right after website release 5 (58bc53f6) was pushed. The code feature-detects the column.
- **Before:** staging dry run and apply on 17 Oct (evidence in the migration file). Undo at supabase/undo/20261017160000_revise_cards_mode.undo.sql.
- **Production pre-check:**
  - 27 rows; no mode column; no check constraint;
  - RLS on; 0 policies.
- **Production post-check:**
  - 27 rows, all with mode 'question'; 1 mode column;
  - the check is (mode = ANY (ARRAY['question','again']));
  - RLS on; 0 policies (service role only).

## 18 October 2026 - Web release 6 integrated (deploy/web-1018-r6, from live main 58bc53f6 = release 5; local, not pushed, not deployed; nothing applied to any database)

- Merged in order, each with the suites and eslint run after it: web/r6-community-1018 (CONTRIBUTE_ENABLED, no Community header, Your standing under Progress, Learn in the Study group, phone More marks), web/r6-review-1018 (D15, D16, D17, D18, D29, F17), web/r6-askmobi-1018 (one Ask Mobi panel and its entry points, ASK-MOBI-1018), then web/badges-1018 (BADGES-REFINE-1018: Badges as their own section of Progress after the record, a tap-to-explain sheet or popover, the earned row on the result).
- Badges: Progress keeps the record, then the study record, then "Badges, n of 16" and Personal bests (out of the week card), then the closing Your standing row. On the result the EarnedBadges row sits once, right after the summary and above the reel row and the analysis, on the review branch's structure. One server addition the badges branch left for the merge: the server keeps a student's badge list for 5 minutes, so forgetBadges(userId) now runs after an attempt is saved (PATCH /api/sessions on a finish, which /api/attempts POST re-exports, and the two GET routes that turn an expired session into a result when they finalised one); the earned row asks /api/me/badges with cache no-cache so the browser's own one-minute copy cannot hide the new badge. New test data/tests/badges_forget_1018.test.mjs (real badgesStore and real /api/sessions route over stubbed edges) is in test:app with badges_refine_1018.
- Conflicts were settled by intent, not by taking a side. The nav label stays "Learn" (D20). Release 5's Review badge on the dock and sidebar stays beside the community branch's tour filter and its More mark (data-within, which covers Learn, Explore, Saved, Progress, Account and Help). Release 5's removal of the Help door (D11) stands: the sidebar foot is the appearance row alone, Help and FAQ is its own page, and nothing about Mobi sits under the theme switch; the Help tour step no longer promises Ask Mobi there. The Help page keeps its "Help and FAQ" title and drops its Ask Mobi row.
- Practice has ONE Ask Mobi entry. Release 5's Repairs line under the subject shelf (D5) stays with its "Review and repair" key; its Ask Mobi key is now the Ask Mobi branch's AskMobiLink "Ask Mobi what to practise", with the weakest-chapter record line under it, and the separate row that branch drew (PracticeAskRow) is gone. The saved-repair hand-off the line used before is not used for the entry any more (repairsLine.mjs still computes it).
- The result keeps the review branch's D15/D16/D17/D18/D29 structure. Ask Mobi's two entries sit where they fit it: "Ask Mobi about this mock" under the ledger in Where your marks went, and "Ask Mobi about Q7" inside an opened mistake in Your mistakes, under the repair; once the repair holds its own ask the line is not drawn twice. Ask Mobi's retirement of the four-tab hub and AIMentorTerminal stands, and the four tests that read the old hub now read the panel.
- Tests: the union of all three sides. Contradictions settled for the newer approved design: mobi_help_door (no Help door, no orb, from release 5 and Ask Mobi), pricing_copy_1017 (Review is its own page from release 5; the finding is not repeated in the panel or the record page from Ask Mobi) and practice_repairs plus ask_mobi_entries (one Practice entry). test:app gains ask_mobi_panel and ask_mobi_entries; practice_repairs.test.mjs is not in any suite list (as in release 5) and passes when run on its own.

## 18 October 2026 - Web release 6, Review and result (REVIEW-RESULT-1018, owner D15, D17, D18, D29) finished on web/r6-review-1018 (local, not pushed, not deployed; nothing applied to any database)

- Built on the approved mock-up (docs/design-decisions/pass-1018/REVIEW-RESULT-1018.md). The front of the result (hero, next move, answer map) is untouched; the Review and the depth layer are the packets P-RR0 to P-RR3 plus what was missing:
  - D18: Review leads with where you lose marks (chapters priced as "Lost 35 of the 80 marks on offer"), the open chapter carries the one lime key "Practise 10 on this chapter" and its mistakes, each with one action; Saved repairs, Your papers, Revise and Also under it. A chapter named in the URL scrolls into view. /analytics keeps its trend and links to Review for chapters.
  - D15: actionLabel() in data/repair_presentation.mjs is the one source of Repair, Check it held, See repair and Try it again (Review's rows and the result's chips both ask it). The result's list now leads with the mistake the next move names (leadMistake(), read once at load, one line says why), so "Repair Q6" and the first row are the same question; a mistake that is already repaired opens its saved repair free (F17) and each mistake shows its paper and a 12-hour weekday stamp.
  - D17: the replay is one slot per question sized to the paper (10 questions draw 10 wide slots, 50 draw two rows of 25), with Play over the real events, Previous and Next, a detail line, Collapse remembered per device, and no replay at all on a paper with under 2 minutes or under 3 answer events (the 58-second case says so in one sentence). The per-answer strip is now the replay in miniature (this question's slot lit). Captions, detail words and the cut link come from data/mistake_lab.copy.json so the app can port them.
  - D16: Your full analysis is one index of six named parts, each with what it found, exactly one open, in the URL (?part=); the lit fill is one marker that slides to the open row.
  - D29: "Play your paper back, N s" (N from the script's own length, 20 for a mock): reelScript() in data/replay.js, the same engine as the replay, builds one timeline from the attempt record (sheet lights question by question as the score counts to the paper's own score, pauses on real moments such as "Q31: you changed a right answer to wrong. It cost 6 marks.", lands on the costliest chapter, ends on the one next move). The web opener is a quiet row under the front; Skip is one tap, Escape leaves, reduced motion opens settled with Next moment. Not wired into Today (another branch): mount ReelEntry/PaperReel there with autoplay and the same script.
- Tests: new replay_reel.test.mjs (12) and result_parts_1018.test.mjs (13: one label from one function, no "Repair first", "Repair in N" or "Check it here" on any result or Review surface, the six parts in order with every R4 block in its part, the front's props, the review states, saved repairs free, the key and the list lead agree), both in test:recovery. Results: recovery 554 (551 pass, 3 todo known gaps, 0 fail), learning 357, app 502, today 32, mob 45, auth 110, billing 153, study 37 of 38 (the same wordnet LICENSE_UNAVAILABLE failure as before, not from this work). eslint clean on all 26 changed files. No existing test was changed or weakened.
- Headless checks (playwright-core, temp profile, 390x844 and 1440x900, Night and Day, every image opened; /preview/arena fixtures, no sign-in, no production data): Review (student, other chapter, one paper, all repaired, zero credits, empty, down, loading, lower sections), Radar row, result (front, six parts, replay of 50, 10 and the 58-second cut), the reel (row, frames at 0.9 to 21.5 s, end card, reduced motion). Real-pointer walks: every index row, Next:, All six parts, Play, Pause, Next, Previous, a slot, Collapse, an answer-map bubble for a wrong and a right answer, a chapter, a mistake row (free sheet), a saved repair (no paid Repair offered), the reel's Skip and Play again, with hit-tests that nothing covers a control; one lime fill in the content at every step; no console errors. Captures: tmp/r6review/shots.
- Limits: Today's "mistakes to repair first" (src/lib/today/move.mjs) still says "first" and belongs to the Today branch; the cut replay's link says "Practise 10 more, no time limit" (a fresh set, not the same questions again, so "Take these 10 again" would be untrue); the app ports (review_chapters.dart, replay_model.dart, the reel) are not built.

## 18 October 2026 - Web release 6, sidebar items: community side hidden (COMMUNITY-1018) and Learn's place (D20) on web/r6-community-1018 (from web/r5-nav-1018; local, not pushed, not deployed; nothing applied to any database)

- CONTRIBUTE_ENABLED (default off; only the exact string true turns it on) hides Contribute and My uploads (sidebar group and Account rows), the Practice "Add a question" panel (and its /api/questions/mine read), the vote arrows (Explore cards and the runner) and the Explore footnote about votes. Routes, tables, files and the creator programme stay. /upload and /my-uploads answer the calm paused page while the flag is off, never a 404, as COMMUNITY-1018 says (ContributionsPaused, inside the app shell; the coordinator corrected an earlier brief that said not-found); a new src/app/(app)/not-found.js, which keeps the sidebar and dock, serves genuinely unknown routes; POST /api/questions/upload and GET /api/questions/mine answer 403 {code: contributions_paused} before any auth or database work. The vote API is left as it is (the app's vote arrows still call it). The flag reaches the browser through ContributeFlagProvider, as MobFlag does. The preview takes ?contribute=on.
- Sidebar: the Community header is gone. Your standing is a sub-link indented under Progress, listed beside Progress in the phone sheet; Account's group is headed Progress and keeps the Your standing row; Progress ends with a "Your standing" row. Your Mob (flag off by default) follows it in Study. With the flag on a Contribute group returns.
- No contribution promise left: Pricing's free-plan note no longer says an uploaded question adds 15 credits; the Terms description (page and seo.js) says practice questions, not community questions; seoPages.js says timed practice from one large CUET question bank. Terms and Privacy keep their community clauses while the upload API exists.
- Practice: with Add a question hidden, Concepts and Pro take the right column beside Recent sessions at 1024 px and up (CSS only), so the lower area stays two balanced columns.
- D20 Learn: the dock stays Today, Practice, Review, Colleges, More (a sixth slot is under 44 px at 375 px and Colleges was the owner's own call). Learn leads the More sheet in its own row (name and one line), is not listed twice, and has its own Guide stop. NEW this pass: (1) a lesson or recall run at /study/<id> keeps Learn as the current place (sidebar, header title), so a run reached from Progress no longer shows no place; (2) on a phone More is marked, with the lens under it, whenever the current place lives under More (Learn, Explore, Saved, Progress, Account, Help), so the dock never shows a screen with nothing current; (3) Progress's study record now leads to the Learn page itself ("Open Learn", with "N cards are due for review in Learn") instead of dropping into a card run; Review keeps its direct "Review due cards" button, Today's plan card is untouched. Learn stays in the desktop Study group between Practice and Review and shows only while STUDY_CONTENT_ENABLED is on. Not done (other owners' pages): Practice's Concepts panel is still at the bottom of the page, and Learn's own page refinement (F15).
- Preview fixtures (dev only): ?study=on carries through the preview's links and opens /preview/study for Learn, serves a study catalog for Progress's study record (?due=0 for none due), and view=not-found shows the not-found page, view=paused and view=paused-uploads show the paused page.
- Landing lines that say "leaderboard", for the landing track (NOT edited): src/app/page.js line 53 (the free plan list item "Leaderboard"), line 124 (kicker "Benchmarks and leaderboard"), line 126 (point "Every mock earns points for accuracy and speed on the leaderboard" and the button "See the leaderboard", href /leaderboard). In-app copy that still says leaderboard (not landing): the result page correction note and AnswerCorrectionNotice.
- Checks: eslint clean (whole repo); test:community 11, test:app 513, dock 7 pass 1 skipped (the DOM measurement launches chrome.exe directly, not run), subjects 30, today 32, mob 45, auth 110, learning 357, recovery 415 all pass. test:study has 1 failure, "the content gate quarantines changed arithmetic, unsourced vocabulary and unsupported reading keys" (WordNet LICENSE_UNAVAILABLE): its inputs (data/study, scripts/learning) are unchanged by this branch, so it is not from this work; not investigated further.
- Headless captures (playwright-core, 390x844 and 1440x900, Night and Day, all opened) in tmp/community/shots: Practice off and on (bottom), Explore off and on (0 and 12 vote rows, footnote 0 and 1), Account group off and on, Your standing with the sub-link current, Progress (study record, closing row), Learn with Learn current and More marked, the More sheet with the Learn row, the paused page (both titles) and the not-found page. Real pointer clicks: More opens the sheet, the Learn row and the Your standing links navigate and become current in the sidebar and (phone) under More; no horizontal scroll at 390, no console error.

## 18 October 2026, about 4:45 am IST - Website release 5 shipped (deploy/web-1018-r5, 09a620fa): the owner's dawn fixes

**Contents (owner items in OWNER-FEEDBACK-2026-10-18-DAWN.md):**
- Night mode is subtle again (D7/D12).
- The light/dark switcher animation is restored (D10).
- Help has moved to its own page, and the phone nav pulse is fixed (D11/D13).
- Practice has Repairs and Ask Mobi entry points (D5).
- The result uses one action label per mistake, and the answer bar is sized to the mock (D15/D17).
- Learn and Review: F15 Revise and Concepts.

**Checks:** recovery 509 pass / 3 todo / 0 fail, app 502, learning 357, auth 110, billing 153, nta 188, today 32, mob 45, subjects 30, du 42, dock 7 (1 skipped: it launches chrome.exe); eslint clean on the 66 changed files; next build --webpack exit 0. Independent visual check with before/after pictures at 390 and 1440, Night and Day: docs/brain/R5-WHERE-TO-LOOK.md. The main session renamed the nav item and page title from Concepts back to Learn (D20) and re-ran app 502, learning 357, dock 7 and eslint. The migration 20261017160000_revise_cards_mode stays on staging only for this push (the code feature-detects the column).

**Approval:** the owner said "Push everything that passes" at about 4 am.

**Nothing was applied to any database.**

## 18 October 2026, about 1:20 am IST - Website release 4 shipped (deploy/web-1017d, main 9578ee66): the owner's night feedback N1-N13

**Contents:**
- The Today redesign (N1). The owner later called it "a huge regression" (D1); the new Today is TODAY-1018.
- The result and Review restore (N12).
- Practice polish (N2/N3/N5/N7/N8/N11).
- The Mobi orb and guide (N9/N17). Later rejected (D6); the redesign is ASK-MOBI-1018.
- The five-subject cap (N6).

**Checks (independent verifier PASS):**

| Suite | Passed |
|---|---|
| app | 502 |
| recovery | 415 |
| learning | 357 |
| auth | 110 |
| billing | 153 |
| nta | 188 |
| today | 32 |
| mob | 45 |
| subjects | 30 |
| du | 42 |
| dock | 74 |

Vercel dpl_APxT7dGMgtBCc6CehsWmXSwuJ7cn was READY with 0 runtime errors in the hour after the push.

**Nothing was applied to any database.**

## 17 October 2026, about 11:55 pm IST - Website release 3 shipped (deploy/web-1017c, main 5d0c46f2): Today and nav fixes

**Contents:**
- Merged onto release 2 (12997f5a): web/fix-today-1017 (f69f8a86) and web/fix-nav-1017 (49dc3426).
- web/fix-result-1017 was left out, because its direction was rejected. It is kept as branch deploy/web-1017c-withresult.

**Checks:** independent verifier PASS. Vercel dpl_6qnQMMAKko4y82Ak65SbL3dqRdGg READY.

**Nothing was applied to any database.**

## 18 October 2026 - Web release 5 (deploy/web-1018-r5): checked and made reviewable (local, not pushed, not deployed; nothing applied to any database)

- Suites on the merged head (9dce83f9): test:recovery 512 tests, 509 pass, 0 fail, 3 todo (the next_move_parity known gaps); test:app 502/502; test:learning 357/357; test:auth 110/110; test:billing 153/153; test:nta 188/188; test:today 32/32; test:mob 45/45; test:subjects 30/30; test:du 42/42; test:dock 8 (7 pass, 1 skipped: the DOM measurement needs DOCK_BASE_URL). eslint clean on the 66 files changed since main 9578ee66. next build --webpack passes. No test was changed and no code was changed in this pass.
- Evidence for the owner's "seems the same" (D33): docs/brain/R5-WHERE-TO-LOOK.md, with 168 pictures in docs/brain/r5-where-to-look/ (390 x 844 and 1440 x 900, Day and Night; before = release 4 main 9578ee66 on a spare port, live www.mockmob.in for the landing; after = the branch on port 3205) and pixel-diff.json. Verdicts: D5, D10, D17 and F15 are clearly visible; D15 and D13 are small; D11 is partly visible (the Help page itself already existed in release 4); D7 is visible on Ask Mobi only (the Night colours elsewhere are the same as release 4); the 50-question summary bar is identical by design. Release 5 contains nothing for Today (D1 to D3), the Ask Mobi redesign (D6), icons (D8) or badges (D19).
- Notes: the sidebar and page now say Concepts where they said Learn (F15). The dev server on 3205 uses the production .env.local: do not sign in on it; the preview routes need no sign-in.

## 18 October 2026 - Web release 5, item lr: Learn and Review packets merged on web/r5-lr-1018 (from main 9578ee66; local, not pushed, not deployed; nothing applied to any database)

- Merged web/lr2-1017 (Revise queue, Review page P-LR1, Concepts base) and web/lr3-1017 (Concepts polish). Conflicts: AppLayoutClient (main's tour and Mobi gating kept, plus the Review badge and the More current on Concepts), RecoveryOverview (the Review view is now review/ReviewPage; main's small Review tweaks are superseded), STATUS.md (all entries kept).
- Checks: eslint clean; test:app 502, test:recovery 509 pass / 3 todo / 0 fail, test:learning 357, test:today 32, test:dock 5 (1 skipped), test:study 37 of 38 (the wordnet LICENSE_UNAVAILABLE failure, which also fails on the older main-line commit 12997f5a); next build --webpack passes.
- Headless captures (390x844 and 1440x900, Night and Day, every image opened): Review (Mistakes, an opened chapter, Papers, empty, down), Revise (ready, cards, empty, a full run played with real pointer clicks, end), Concepts (full, first visit, lesson, lesson opened from Q42), Practice's Concepts panel, the More sheet. No horizontal scroll, no console error from this work (the one 401 is /api/ai/credits, which the study preview does not stub).
- D20 status: see the return of this task. Concepts sits in the desktop sidebar (Study group) and in the phone More sheet only; its Practice panel is at the bottom of the page; the migration 20261017160000_revise_cards_mode is on staging only (code feature-detects the column).

## 17 October 2026, about 11:05 pm IST - Website release 2 shipped (deploy/web-1017b): security rounds 1 and 2, per-user AI cap on rival battles, owner-ledger fixes for Start/Practice/runner and pricing/help/copy

- Merged onto live f725a422: fix/security-1017d (creator API cut-down sale, exact creator-code match, a single report never unlists a question), fix/security-2-1017d (explore returns public fields only, upload is no longer an answer oracle, payout serialisation, server-only default privileges, mentor /local never stores client text as the assistant, deletion scrubs runtime_ai_requests, votes only on live questions), web/fix-aicap-1017 (W-098: rival start and submit reserve through the per-user cap), web/fix-start-1017 (owner ledger W-002, 003, 005, 008, 012, 013, 014, 017, 018, 023), web/fix-pricing-1017 (W-093 to W-099).
- Checks (independent verifier PASS): lint clean; app 498, recovery 415, learning 357, auth 109, billing 153, nta 188, today 28, mob 45, subjects 26; next build --webpack; headless smoke at 390 and 1440 in Night and Day with zero console errors and zero overflow.
- Production migrations applied by the main session under the owner's standing grant, each dry-run on staging first, with pre- and post-checks: 20261017200000_create_pending_payout_lock (advisory lock present), 20261017205000_account_deletion_runtime_ai_scrub (prefix match and {hash} present; applied before this code), 20261017210000_default_privileges_server_only (0 sequence grants to anon or authenticated; public default ACLs postgres and service_role only; supabase_admin step skipped on hosted Supabase). Undo files in supabase/undo. Not applied: 20261017100000_mob.sql (the Mob stays off).
- Open: 12-13 Oct migrations (app_preferences, session_finalisations, inventory_snapshots, nta_paper_shortfalls) are not on production under their own names; their callers must degrade safely (not traced). New functions meant for browser roles now need an explicit GRANT EXECUTE.

## 18 October 2026 - Learn and Review P-LR2 (web Revise queue) verified on web/lr2-1017 (local, not pushed, not deployed; nothing applied to production)

- Reviewed the P-LR2 commits against LEARN-REVIEW-1017 5.8 and acceptance 9 and 12: one run over four sources (questions, repaired mistakes as Review again, Check it held, concept cards), one card per question per day (the merge keeps the repaired mode, and the server's guarded card update answers a second try with not_due), the cap of 5 or 10 on questions only, checks always in, cards at most 5; the dock hidden on the whole /review/revise route (loading, empty, failed and end states too); the Review badge counts down only on the server's acknowledgement; /learn?recall=due and /review/again land on Revise filtered. No code change was needed in this pass.
- Visual check through /preview/arena?view=revise on port 3341 (headless Chrome, temp profile deleted, dev server stopped, .next-dev removed): ready, dedupe, cards, sparse, legacy, empty, done and down at 390x844 and 1440x900 in Night and Day. A full run was played with real pointer clicks: 8 due, 5 questions back, 1 Check it held, 2 concept cards; the sidebar count went 8 to 4 after four answers; the dock computes to display none at 390; no horizontal scroll; the 5 or 10 a day switch is hit-testable and remembered; the end reads "5 recalled" with the slipped check and the cards named. One lime fill in the content at every step (Next question, Start 10 questions, Back to Review); the sidebar Start key is the owner's accepted second fill.
- Checks: eslint clean (whole repo); test:recovery 509 pass, 0 fail, 3 todo (the next_move_parity known gaps); test:app 498, test:today 28, test:dock 5 pass 0 fail; test:study 37 of 38 (the wordnet LICENSE_UNAVAILABLE failure in study_content.test.mjs, not from this work). next build --webpack passes only with NODE_PATH pointing at mockmob-next/node_modules: the shared node_modules junction lacks @img/colour, so sharp cannot load for the webp blur images (an environment gap, not code); Turbopack refuses the node_modules junction.
- Limits: Revise minutes come from minutesFor (8 due is about 10 minutes; the design mock says 7). The Revise run keeps the web top bar (logo, credits, avatar), as the mock does; the spec line about the app bar stepping away is for the Flutter app. Changing the cap restarts the run on purpose, so the schedule fold closes. Review pages (P-LR1) are on hold and untouched.

## 17 October 2026 - Learn and Review P-LR0 (shared input, fixture, storage) on web/learn-review-1017 (from deploy/web-1017 f725a422; local, not pushed, not deployed)

- Built: data/review_input.mjs (Review's input to the one shared nextMove(), plus chapterRows, receipt, reviseDue, reviewBody), the design student and variants in data/tests/fixtures/review/ (student.json is the unchanged copy; scripts/gen_review_fixtures.mjs writes the variants and expected.json), GET /api/me/review (read-only, src/lib/server/review.js), data/study/lesson_map.mjs, migration 20261017160000_revise_cards_mode.sql with its undo.
- Staging only (onwkqxmjqjrhfbjjdydu): dry run rolled back clean, then applied; revise_cards 105 rows all 'question'. Production NOT migrated; the code feature-detects the column.
- Tests added to test:recovery: review_input, next_move_parity, review_api, lesson_map. Recovery 461 pass, 3 todo (below), 0 fail; today 28, egress 29, app 498 pass; lint clean. test:study has one failure that is not from this change (wordnet LICENSE_UNAVAILABLE in study_content.test.mjs).
- KNOWN GAPS (recorded as todo tests in next_move_parity.test.mjs, not faked): Today's repair key is a batch ("Start repair", the paper's result page, count of the newest paper), not "Repair Q42"; so Today cannot name Review's first target until the TODAY owner changes its wording (LEARN-REVIEW-1017 12 flag 2). Kind and the paper the key opens do agree.
- Other limits: the API has no cohort repair order, so its first repair is the lowest open number in the newest paper (Q38 in the design student, not the fixture's Q42) until a repairOrder is sent; Review prices open items while the result page prices all of a paper's wrong answers (same on one paper without repairs); the Revise minutes use data/revise.js minutesFor (8 due = about 10 minutes), the design mock says 7; the Review-again answer endpoint and the merged due list belong to P-LR2.

## 17 October 2026 - deploy/web-1017: wave 4 merged and the critic's defects fixed (local, not pushed, not deployed; nothing applied to any database)

- Merged content/wave4-1017 (the wave 4 rows in data/nta_agent_scores and data/nta_fit_scores, so the 200 live questions become NTA-eligible on deploy).
- Fixed all 17 critic defects (5 medium, 12 low). Also from the main session: the Practice session bar is opaque now, and the phone dock is denser (Night 0.94, Day 0.93), so no text behind either one is readable. CTO calls: the dock's Start key is unchanged (A1), and the bar's key says what it starts (Start 10 questions, Start full mock, Start NTA paper). The Start lamp is now a neutral warm light at 0.08. The preview takes ?study=on to show Learn in the More sheet; no production flag was changed.
- Checks: lint clean; app 498, recovery 415, learning 343, auth 109, billing 118, nta 188, today 28, mob 45, subjects 20, authored-publish 159 (155 pass, 4 skipped, 0 fail); next build --webpack passes. Headless captures at 390x844 and 1440x900, in Night and Day, with elementFromPoint hit tests before every click. Pages: Practice, Start sheet, Result (perfect, zero credits, an opened row, the repair strip), Review, Today (returning, the road, the dock), Mob (complete, two, pro) and the More sheet.
- Open: at 360 px the bar's mode name is cut short ("Quick pr…"), though the price still shows. STUDY_CONTENT_ENABLED in Vercel production was not checked; Learn has no phone entry while it is off.

## 17 October 2026, about 10:20 am IST - Authored wave 4 published on production (200 questions; mathematics 51, chemistry 42, general_test 39, biology 35, physics 33)

- Applied by Claude (session 25ef3d95) under the owner's standing database grant and his publish rule: only questions whose two quality judges average 8 or more AND whose fit median is 8 or more, after the full wave 1-2 process (coverage plan from select-only production SQL against the blueprints, Sonnet authors, a Sonnet audit per subject, 5 blind Haiku solvers with 4 of 5 on the key, 2 rubric judges, 3 fit judges, the acceptance rule, a Sonnet expert pass, a 3-solver blind re-solve of the one repair that changed solver-visible text). Hindi stays out.
- Plan `docs/brain/reports/authored-w4/plans/wave4-publish-plan-production-2026-10-17.json` (hash 813c724a6554f82a, 200 rows, 2 passage groups, no blockers); select-only dry runs on staging and production first. The main session re-checked all 200 rows against the final score entries before applying (0 failures).
- Inserted 200. Live after: biology 451, chemistry 466, gat 322, mathematics 383, physics 383. Restore file `docs/brain/reports/authored-publish/authored-publish-restore-2026-10-17T04-46-59-355Z.json` (undo: `--mode=restore --restore=<that file> --expect-project=isrxrxzjocewrdureyhp`); also `supabase/undo/20261017130000_authored_wave4_publish.undo.sql`.
- Held: 57 rows at 7-7.9; out: 22 (first-pass rule 20, including 8 general_test Current Affairs items the fit judges rated 6; one unaudited physics draft job never laid out).
- NTA mode: the rows show in practice now; they become NTA-eligible once the code carrying the merged score tables (this branch) is deployed.

## 17 October 2026 - Website release branch deploy/web-1017 assembled (from live main c3b1e215; local, not pushed, not deployed; nothing applied to any database)

- Merged with --no-ff, in order: web/live-fixes-1017, web/review-f17-1017, web/subjects-claim-1017, web/result-1017, web/start-1017, web/today-1017, web/dock-1017, web/mob-split-1017, content/wave3-1017. Conflicts: result (both branches had built the F17 saved repair: kept the lab.repaired ids and the savedRepairs map with the paper line), start and dock (package.json scripts; the phone dock key stays lime and fixed, the sidebar key follows the route through data-start-quiet, the Practice start bar rides --dock-h), mob split (MOB_ENABLED gate kept with the mobId lookup), wave 3 (STATUS only).
- Marketing: the Leaderboard feature is now Your standing on pricing and features (own rank among MockMob students, no other student's name). The landing page is another branch's.
- Tests: lint clean; app 498, recovery 415, learning 343, auth 109, billing 118, nta 188, du 42, subjects 20, today 28, mob 45, authored-publish 128 (123 pass, 4 skipped, 1 fails only on this Windows checkout: CRLF changes the bytes of tmp/authored-w3s raw files, whose manifest sha256 matches the committed LF blobs), dock 6 (5 pass, 1 skipped: needs a running server). next build --webpack passes.
- Migrations vs main: new 20261017150000_study_road_fields.sql (TODAY-1017 P0: exam_date and mock_target; undo file; dry-run on staging still to do); 20261017100000_mob.sql changed (Mob; must not reach production while Mob is off). Not applied anywhere.

## 17 October 2026, about 4:45 am IST - Website motion/UX pass shipped (deploy/ux-1017 onto main e192c59e)

- Ships web/ux-social-1016 (independent verifier PASS on its own base, 94c172e6) merged onto main e192c59e (42b0d75b), plus: stray log removed and *.log ignored (e5c4952e), the moderation Mob reports list and the result page's Mob row send no request while MOB_ENABLED is unset (5e41b296, 1240a925), data-page-primary on the two /leaderboard CTAs (7e26abc3).
- Ship verifier (session 25ef3d95): leaderboard privacy shape intact (401 signed out; only {you:{rank,of,tests,average}, window}), "Your standing" copy intact, providerCore allowlist is only gpt-6-luna and claude-haiku-5-5, reserve_runtime_ai called with 7 arguments. The Mob is off by code: every /api/mob route returns 404 MOB_DISABLED before auth or any DB call, /mob and /join call notFound(), no page or server component queries a mob table while the flag is unset.
- Checks: lint clean; test:app 474, recovery 374, learning 323, auth 109, billing 118 pass; motion tests 27 pass; next build --webpack passes. Headless smoke at 390x844 and 1440x900, Night and Day (Today, Practice, a result, Review, Progress, /leaderboard, Help, Pricing; 32 captures opened): 0 console or page errors, no horizontal scroll, 0 covered tap targets, one volt action per viewport.
- Migrations: none applied. The only new migration, 20261017100000_mob.sql, stays off production (Mob off).
- Open: marketing copy still lists "Leaderboard" as a feature (pricing, landing, features); the result page has 18 px of invisible overflow from an opacity-0 tooltip (html overflow hidden, cannot scroll).

## 17 October 2026 - Per-user AI cap, two-model allowlist, two-call ladder (branch fix/ai-user-cap-1017 from a2fe34b4; local, not pushed, not deployed; nothing applied to production)

- Migration `20261017120000_runtime_ai_user_cap.sql` (undo in supabase/undo): runtime_ai_requests.user_id and index; cap rows student_user_paid 0.1136 and student_user_free 0.0114 in runtime_ai_budget (USD per IST month, change with one UPDATE); reserve_runtime_ai takes p_user_id and p_user_tier, refuses with 'runtime user limit reached', and refuses any model but openai gpt-6-luna and anthropic claude-haiku-5-5 ('runtime model not allowed'). The global USD 25 check is untouched. Dry run on STAGING (onwkqxmjqjrhfbjjdydu): apply, proof in a rolled-back transaction, undo, apply again; staging is left migrated.
- Deploy order: apply the migration to production BEFORE the code (the old function has no p_user_id).
- Code: providerCore allowlist (an env override such as AI_LUNA_MODEL to another model is refused, logged, nothing called), at most 2 physical calls per action (the third Luna fallback after a failed JSON retry is gone), 'low' reasoning headroom 2,500 to 1,000, user_budget kind and the limit message, Ask Mobi context capped at 12 KB (src/services/ai/contextBudget.js), account deletion unlinks runtime_ai_requests.user_id.
- Tests: data/tests/ai_user_cap.test.mjs (in test:learning). Recovery 352, app 343, auth 109, billing 118, learning 323 pass.

## 17 October 2026, about 4:35 am IST - Authored wave 3 published on production (153 questions; chemistry 48, general_test 56, physics 49)

- Applied by Claude (session 25ef3d95) under the owner's standing database grant and his 17 Oct publish rule: only questions whose two quality judges average 8 or more AND whose fit median is 8 or more, after the full wave 1-2 process (5 blind Haiku solvers with 4 of 5 on the key, 2 rubric judges, 3 fit judges, the acceptance rule, a Sonnet expert pass, 3-solver blind re-solves of every repair that changed solver-visible text (16 of 16 held 3 of 3), a full fresh pass on 7 reworded rows). Hindi stays out.
- Plan `docs/brain/reports/authored-w3/plans/wave3-publish-plan-production-2026-10-17.json` (hash 4743921360457bd1, 153 rows, no blockers); the same plan dry-ran select-only on staging and production first. The main session re-checked all 153 rows against the score entries before applying (0 failures).
- Live after: chemistry 424, gat 283, physics 350. Restore file `docs/brain/reports/authored-publish/authored-publish-restore-2026-10-16T23-05-06-939Z.json` (undo: `--mode=restore --restore=<that file> --expect-project=isrxrxzjocewrdureyhp`); also `supabase/undo/20261017120000_authored_wave3_publish.undo.sql`.
- Held for a later decision: 55 rows at 7-7.9 (`wave3-held-7-2026-10-17.json`). Dropped: 11 by the expert pass (7 Electronic Devices items confirmed outside the 2026 Physics syllabus, Unit 9 quoted in expert/physics.json), 24 by the first-pass rule, 2 duplicates.
- NTA mode: the rows show in practice now; they become NTA-eligible once the code carrying the merged data/nta_agent_scores and data/nta_fit_scores is deployed (this branch merges into the next website release).
- Suites on content/wave3-1017: test:nta 188, test:authored-publish 124 (4 skipped; the CRLF failure is fixed), test:recovery 352.

## 17 October 2026, about 3 am IST - Authored wave 3 prepared (branch content/wave3-1017, local, not pushed; nothing published, no database written)

- 294 drafts (general_test 97, physics 74, chemistry 74, hindi 49; source claude-authored-2026-10-17-w3) passed one blind Haiku check each (6 rejected). A second checker (Opus) solved a stratified 45 and then the whole of gat-02, hin-02 and hin-01 (107 rows) without the key: no wrong key, but 7 of the 45 had a defect (15.6 percent), so 3 batches were re-checked in full. Defects, repairs and advisories: docs/brain/reports/authored-w3/wave3-audit-2026-10-17.json. Repairs (28 rows) are text-only: Hindi chapter names, one passage typo, two explanations, three listed-order keys.
- Wave 3 did NOT go through the wave 1 and 2 scoring: no 5 blind solvers, no two agent judges, no three CUET-fit judges, no expert pass, so no score entries exist and the NTA engine admits none of the 294. Verdict values on the rows are haiku_blind_verified (187) and opus_audited (107), not ready or repaired.
- Dry run against production (select-only): 294 rows (chemistry 74, gat 97, hindi 49, physics 74), 5 Hindi passage groups, 0 existing ids, no missing columns; the one blocker is the missing score entries.
- Hindi: blueprint data/nta_blueprints/hindi.json (from the 2026 Hindi 102 syllabus PDF, which lists only Reading Comprehension and Verbal Ability; Kavya Khand, Gadya Khand, Anuvad and Rachnatmak Lekhan are excluded). Registered in the engine and in index.json pendingSubjects; Hindi is still not a public subject, so no route serves it. Two engine gates were Latin-only and refused every Hindi passage and match item; fixed (danda counts as a full stop, verse kept in lines counts, सूची-II is read as List-II).
- Tests: test:nta 188, test:recovery 352, test:authored-publish 93 of 94 (the failing one, "merging wave 2 again reproduces the committed tables byte for byte", fails the same way on origin/main on Windows: CRLF against LF), authored_w3 15.

## 17 October 2026, about 12:25 am IST - Batch 1016d production migrations applied (before its deploy)

- Applied by Claude (session cc0bf1af) under the standing database grant, in this order, each with a pre-check and a post-check on production (isrxrxzjocewrdureyhp); each was dry-run on staging per the batch merge report and has an undo in supabase/undo:
  - 20261016170100_webhook_event_lease: webhook_events.claimed_at (pre 0, post 1).
  - 20261016110000_study_weekdays: study_goals.weekday_mask plus the 1-127 check (pre 0, post 1 and the constraint).
  - 20261016140000_ai_reply_report: public.ai_reply_reports, RLS on, anon and authenticated cannot select, service_role can insert.
  - 20261016120100_funnel_product_steps: users.funnel_seen, the widened funnel_daily step check (0 rows broke it), funnel_count_once (service_role only, anon cannot execute). FUNNEL_ENABLED stays off.
- Not re-applied (already live): 20261016141000 questions lockdown (anon select on public.questions is false), 160100, 170000, 170300, 170400, submit_rival_battle; 170200 is a no-op on production.
- Production records these by apply time, not by the repo file names; keep applying by SQL, never `supabase db push`.

## 16 October 2026 - Batch 1016d assembled (branch deploy/batch-1016d from main 8a0141ba; local, not pushed, not deployed; nothing applied to production)

- Merged with --no-ff: fix/security-1016, fix/security-2-1016, db/status-1016e, fix/health-1016, web/usp-mocks-1016, web/revise-events-1016, web/parity-you-1016, web/weekdays-1016, web/ai-report-1016, web/college-search-1016, web/compass-card-1016, web/timed-nudge-1016, web/help-faq-1016, web/copy-1016, web/rival-mobi-1016, web/funnel-calls-1016, web/auth-cache-1016, web/egress-1016, web/art-1016, play-f4, sec-tests. Held back: fix/feed-keys-1016 (until the new app ships), web/credit-rpc-1016 and the credit_consume_fast_path migration (dropped), web/egress-practice-1016 (WIP), the practice-verdict migration, the landing, unfinished wip branches and the rejected lineages.
- Production migrations still to apply, in order: 20261016110000_study_weekdays, 20261016120100_funnel_product_steps (renamed from 120000, which is question_option_stats), 20261016140000_ai_reply_report, 20261016170100_webhook_event_lease. 20261016170200_server_only_functions_drift is a no-op on production. Each was dry-run on staging (undo, apply, smoke) inside a transaction that was rolled back; staging is unchanged.
- Verification: lint clean; test:app 343, recovery 352, learning 307, nta 185, du 41, auth 97, answer-integrity 11, billing 118 all pass; next build --webpack passes. Not looked at in a browser: Today (Compass, timed nudge, colleges), Progress badges, Account weekdays, Rival result, Help and the device switch, Lab empty state, the briefcase art. The briefcase files from web/art-1016 needed their sizes, feet and alt text updated in data/subject_art.mjs and startModel.mjs (the branch left the stamp's numbers); feet are estimated, the owner's OK on the briefcase is still pending.

## 16 October 2026 - AI reply report (Play generative-AI blocker) (branch web/ai-report-1016, local, not pushed, not deployed, nothing applied to production)
- Cherry-picked ff230163 (POST /api/ai/mentor/report) and reworked it: signed in only (bearer or cookie), two per-student limits (10 a minute, 40 a day, persistent when PERSISTENT_LIMITS_ENABLED), reason from the app's four labels (stored as a code), reply capped at 1200, body capped at 8000, and the reply must be one the student received (assistant message with the charge reference `prepos:<user>:<requestId>`, else a committed credit operation). One row per student per request id; the Idempotency-Key header is ignored. Logic in `src/lib/server/aiReplyReport.js`, tests in `data/tests/ai_reply_report.test.mjs` (in test:app).
- Migration `20261016140000_ai_reply_report.sql` plus undo in supabase/undo. Dry-run on STAGING (onwkqxmjqjrhfbjjdydu): apply, verify (RLS on, no policy, no anon or authenticated read or write, service role can write), undo, apply again. Staging now has the table. Production not touched. Run it before deploying the route; the app's Report key stays hidden until `aiReplyReportLive` is true in a build.
- Account deletion deletes `ai_reply_reports`. `/privacy` (16 Oct) now names the question stream events seen, attempted and skip as required app interactions and the AI reply report; the Play data-safety draft (PLAY-RELEASE-2026-10-16.md section 4, branch app/play-prep-1016) matches.

## 16 October 2026 - NTA index rebuilt on production after the signature fix shipped (batch 3, 8a0141ba)

- The index was emptied at 14:55 after its rows failed the runtime signature check (verified_at signed as Z, read back as +00:00). The fix 35a078e3 shipped in batch 3 (main 8a0141ba, Vercel READY, 0 runtime errors).
- At about 10:05 pm IST, Claude (session 604ced81, standing grant) ran scripts/nta-index-build.mjs from the live code: dry run (english 173, accountancy 135, business_studies 181, economics 164 = 653 rows; slim reads 0.32-0.43 MB against 5.3-6.6 MB full), then --write --allow-production.
- Verified at once with the read-only scripts/nta-engine-run.mjs on production: 0 score_signature_invalid; accountancy, business_studies and economics build 3 of 3 papers with factory-scored questions eligible (769, 93, 137). English refuses a full NTA paper (34 too few questions), as it did on 13 Oct before any index: a content gap, not the index.
- Switch-off if ever needed: truncate public.nta_question_index (the runtime falls back to the full read).

## 16 October 2026 - Production database: health migrations applied (leaderboard function, least privilege for browser roles, pinned search_path, payments policy)

- From the production health audit (docs/brain/PROD-HEALTH-2026-10-16.md) and branch fix/health-1016 (verifier PASS at 18567057). Each was dry-run on staging by the health fixers (applied, checked, undone), with undo files in supabase/undo/.
- Applied by Claude (session 604ced81) under the standing grant at about 7:20 pm IST, in order: 20261016160100_leaderboard_group_by (mm_leaderboard(), service role only; live code still pages until fix/health-1016 ships, then uses it), 20261016170000_browser_roles_least_privilege (revoke anon/authenticated on RLS tables with no policy; revoke execute on 10 server-only functions), 20261016170300_function_search_path (17 functions pinned to public, pg_temp), 20261016170400_payments_policy_initplan (same rule, (select auth.uid()) form).
- Pre-check: mm_leaderboard missing; 23 RLS-no-policy tables open to the browser roles; 6 server-only functions executable by anon; 7 unpinned functions; payments policy per-row auth.uid(). Post-check: mm_leaderboard returns 794 rows and anon cannot execute it; 0 open tables; 0 anon-executable server functions; 0 unpinned; policy in the select form; service_role still reads attempts. Live smoke after: /, /pricing, /api/stats, /leaderboard, /api/leaderboard all 200.
- Undo, newest first: supabase/undo/20261016170400_payments_policy_initplan.undo.sql, 20261016170300_function_search_path.undo.sql, 20261016170000_browser_roles_least_privilege.undo.sql, 20261016160100_leaderboard_group_by.undo.sql (files on fix/health-1016).

## 16 October 2026 - Production database: missing submit_rival_battle applied (Rival submissions were failing closed)

- Found by the post-crash reconciliation: live code (src/services/ai-rival/scoreRivalBattle.js) calls rpc submit_rival_battle, but production never had the function (migration 20261002122000_rival_atomic_submission.sql was saved but not applied). Any Rival submission would have returned 503 battle_submission_temporarily_unavailable. No student was affected today: the last Rival battle was created 7 May 2026.
- Dry run on PRODUCTION inside a rolled-back transaction (staging has no Rival tables): create the function, insert a throwaway battle, submit two answers, replay the same submission. Result: first and replay calls return the same response, status submitted, 2 answer rows; after ROLLBACK no leftover rows and no function.
- Applied by Claude (session 604ced81) under the owner's standing database grant at about 6:15 pm IST, service role execute only. Undo: supabase/undo/20261002122000_rival_atomic_submission.undo.sql.

## 16 October 2026 - The Mob (social loop) server and website, SP-1 and SP-2 (branch web/ux-social-1016, local, not pushed, not deployed, NOT applied to production, MOB_ENABLED off)

Spec `mockmob-next/docs/design-decisions/pass-1016e/SOCIAL-SPEC.md`. App contract `mockmob-next/docs/design-decisions/pass-1016e/SOCIAL-APP-CONTRACT.json` (shapes, errors, limits, copy and the six fixture bodies). Design note `docs/design-decisions/web-mob-1016.md`. Nothing grants, spends or rewards credits; an invite tied to credits is left as TODO(owner D-S4).

- **Migration** `supabase/migrations/20261017100000_mob.sql` (9 tables, 14 functions, RLS on, service role only), undo `supabase/undo/20261017100000_mob.undo.sql`.
- **Staging (onwkqxmjqjrhfbjjdydu, execute_sql, no migration-history row):** applied, undone (0 tables, 0 functions), re-applied (9 tables, 14 functions, RLS on, anon and authenticated have no table or function grant). A smoke run inside one transaction that raised at the end (create, invite, lookup, 2 joins, already, sitting and its repeat, nudge count 2, seen, report, block, leave passes the owner role on, remove, last leave closes the Mob) left no rows. Then the real service over PostgREST (4 temporary staging users, fake question bank and practice start): create, invite, lookup, 3 joins, 3 starts, 3 sittings, the trap for a sitter and none for a non-sitter, show score, nudge and its repeat refused, nudge seen, report, non-owner remove refused, leave and block, blocked rejoin refused as an invalid code, owner leaves and the next member becomes owner; every row and the 4 users were deleted afterwards (all 9 tables at 0). **The migration stays applied on staging for the app walk.**
- **Account deletion:** the processor keeps the users row as a tombstone, so nothing cascaded and its fail-closed guard would have refused to delete any student in a Mob. `DELETION_STEPS` now names every mob_* table (tested on PGlite with the real processor).
- **Verification:** `data/tests/mob.test.mjs` 21 tests (now in `test:app`); `test:app` 344, `test:recovery` 359, `test:learning` 302, `test:auth` 52, all pass (run before the Today wiring and the mob test joined test:app). eslint clean on every touched file. On the shared dev server (3181) with one headless Chrome over CDP and real pointer clicks: `/preview/arena?view=mob` in 10 fixture states and `view=join` signed in, signed out and invalid, at 360, 390 and 1440, Night and Day, every control at least 44 px and the topmost element at its centre, no sideways scroll, no console error; member menu, report, Escape returns focus, nudge reply, show-score switch, invite dialog and start a Mob clicked; reduced motion leaves no animation. Captures: `mockmob-next/tmp/mob-web-1016`. With MOB_ENABLED unset the API answers 404 MOB_DISABLED; `/mob` renders the not-found page (HTTP 200 on the dev server because the arena layout streams first).
- **Not done / gates:** owner decisions D-S1 (minors), D-S2 (paper cost; built as a quick 10), D-S3/SP-0 (leaderboard privacy fix, not touched), D-S4 (invite rewards, not built); the Practice row, Review trap row and result-page line (other packets' files); the Mobi moment on Today; the /admin/funnel Mob block; the privacy page section (with the change that enables the flag); `next build --webpack` not run here (the shared dev server serves this worktree); applying to production.

## 16 October 2026 - Production database: slice 5 refresh v2 applied; first refresh filled 461 questions in 13 s

- Applied by Claude (session 604ced81) under the standing grant at about 11:10 IST: migration 20261016130000_question_option_stats_refresh_v2 (create or replace of refresh_question_option_stats; same signature, grants and results as v1, proven by the v1/v2 equality tests on PGlite; staging dry run 1.2 s at production size, then undone).
- First production refresh: 13 s; 461 questions, 13,877 first answers counted (the same 461 questions as the committed snapshot), 0 timed answers yet (no question has 10 or more timed first answers since the 15 Oct capture), so every cohort-time line stays hidden, as designed. refreshed_at 2026-10-16 05:40:41 UTC. The nightly pass on /api/internal/refresh-inventory keeps it current once batch 1016c ships.
- Undo: supabase/undo/20261016130000_question_option_stats_refresh_v2.undo.sql (restores v1), then the v1 undo drops the table and function.

## 16 October 2026 - Production database: slice 5 table question_option_stats applied; first refresh timed out, nothing written

- Applied by Claude (session 604ced81) under the owner's standing database grant at about 10:35 IST to production isrxrxzjocewrdureyhp: migration 20261016120000_question_option_stats (table question_option_stats, RLS on, service role only; function refresh_question_option_stats(), service role only). Staging dry run passed earlier (web/slice5-1016 13347c3e).
- The first `select public.refresh_question_option_stats()` on production hit the 2-minute statement timeout (57014) at production size (1,815 attempts, 35,067 answers). It runs in one transaction, so nothing was written: the table is empty and the website falls back to the committed snapshot of other students' picks exactly as before slice 5. The live code (09421b29) does not read the table yet.
- Next: an optimised function (migration 20261016130000_question_option_stats_refresh_v2, being written on web/slice5-1016 with v1/v2 equality and volume tests) replaces it before batch 1016c ships; then one manual refresh, and the nightly pass on /api/internal/refresh-inventory keeps it current.
- Undo: supabase/undo/20261016120000_question_option_stats.undo.sql (drops the function and the table; derived data only).

## 16 October 2026 - Mistake Lab v4 slice 5: cohort time (branch web/slice5-1016 from the 1016 batch merge c87407e0; local, not pushed, not deployed; NOT applied to production)

Spec `mockmob-next/tmp/mistake-lab-v4/SPEC.md` 4.13 and "Slice 5". The owner decision on shared anchor questions per NTA paper is deferred and not built.

- **Migration (not applied to production; needs the owner's standing database grant):** `supabase/migrations/20261016120000_question_option_stats.sql`, undo `supabase/undo/20261016120000_question_option_stats.undo.sql`. One table `question_option_stats` (one row per question; no user id, no attempt id; RLS on, no policy, service role only) and one function `refresh_question_option_stats()` (service role only, one advisory lock, idempotent, deletes rows of questions that stop passing the guards). First answers only (the 15 Oct export's own rule), the same truth guards as `scripts/cohort/question_picks.sql`, today's key by option-text hash, under 10 students no row. Time is the paper trace's one rule rebuilt in SQL (away time out, set and sheet pages, the 30-minute break only on records with no away data), used only for server-scored records that matched the answers and carry an end event, per question 2 s or more with no break. "Changed" is the ledger's own (`observed.answerChanges`); "moved off the key" is first pick on the key and final answer off it; strike data is a captured record from the web runner or holding a strike-out. The sorted whole-second right-answer times are stored (up to 1,000 a question) so the student's own time can be left out exactly. Columns: option picks, first-answer right count, timed counts and median and quartiles (right and wrong), changed, moved-off-key, strike basis, struck key, first and last first-answer dates, `counted_through`, `refreshed_at`.
- **Staging dry run (onwkqxmjqjrhfbjjdydu, via the Supabase MCP, production not touched):** the migration applied, the refresh ran twice on the real staging data (6 attempts: 0 rows, correct, nobody reaches 10), then a synthetic run inside one transaction that raised at the end to roll back (36 attempts of 12 captured students on 3 live questions): 3 rows with the exact medians, quartiles, changed, moved-off-key and struck counts I computed by hand; the rollback left 6 attempts and 0 stat rows; RLS on, anon and authenticated have no table or function grant; then the undo ran and the table and function are gone. Staging is back as it was (I used `execute_sql`, so no migration-history row was written).
- **Nightly refresh:** no cron added (`vercel.json` untouched). `/api/internal/refresh-inventory` now runs `refreshCohortStats` (`src/lib/server/cohortStats.js`) after the inventory work, within `min(120 s, 250 s minus time used)`, production only (`data/full_bank_guard.js`); a failure, a missing table or a timeout is a log line and a `cohortStats` field in the body and never changes the status (403, 409, 503 and 200 are the inventory's own). The inventory's own 409 (not production) still returns before it. When `web/ntaidx-1016` merges, its NTA index pass sits in the same route: keep both passes, the NTA index first, then the cohort table (a textual merge conflict, no logic conflict).
- **Read path:** `readCohortWithTime` (the attempt route's cohort reader). A table whose newest `refreshed_at` is at most 48 hours old is the source (its rows become a snapshot for the unchanged `cohortForAttempt`, so the guards and the student's own first-answer subtraction are the same code); a missing, empty or stale table, or any failed read, falls back to the committed snapshot exactly as before, with no time line. `data/cohort_time.js` leaves the student's own first answer out of the picks, the median (from the stored seconds), and the changed, moved-off and strike counts, using the same reliability rules as the SQL on the student's own record; if the student's own time is not among the stored times, nothing of theirs is taken out. Gates in `LAB_RULES` (30 timed right answers; 20 timed students; 20 with strike data; 5 slow questions each with 15 or more timed right answers; strictly more than twice the median; own record must have ended). Sentences in `data/mistake_lab.copy.json` (`cohort.time`); additive fields `others.lines` and `cohort.slow` (absent when no gate passes, so every existing contract file is byte for byte unchanged).
- **UI:** the lines are in the opened answer under "How others answered" (same class, the secondary ink after the first line, `text-wrap: pretty`) and the ledger finding is a second paragraph and chip row in the existing cohort block. No new decoration. Dev preview `/preview/arena?view=result&mock=full&cohort=time` (every gate met) and `&cohort=time-gated` (one short of each).
- **Verification:** `test:recovery` 272, `test:app` 328, `test:learning` 277, all pass. New `data/tests/cohort_time.test.mjs` (30: every gate at its boundary, forms, student left out, fallback over a fake client for missing, stale, empty and failing tables, refresh over a fake client for ok, skipped, missing, failed, thrown, timeout and not-production, the refresh run twice gives the same result, the Lab with every gate met and one short of each, no new cron) and `data/tests/cohort_time_sql.test.mjs` (11, on a real Postgres via PGlite: the migration, idempotent re-apply, the undo, privileges, first answers only, the under-10 gate, guards, the cutoff, idempotent refresh, a break, and the SQL's time, changed, moved-off and strike numbers equal to `ownContribution` over the five replay papers, including passage sets, the submit sheet and an NTA paper). Both are in `test:recovery`. eslint clean on every touched file. Captured on my own dev server (port 3170, stopped) with my own headless Chrome over CDP, real pointer clicks, at 390x844 and 1440x900, Night and Day, three fixture states, no sideways scroll and no console error: `mockmob-next/tmp/mistake-lab-v4/slice5-captures`. Design note: `docs/design-decisions/web-slice5-1016.md`.
- **Not done / gates:** applying the migration to production (owner's standing grant; run the refresh once afterwards and read `refreshed_at`); until enough papers carry the 15 Oct capture almost every line stays hidden, which is the intended behaviour; the Android app does not render the new fields yet; no instrumentation for the lines; the first production refresh has not been timed (the function is set to stop at 120 s and the route does not wait longer).

## 16 October 2026 - Monthly pay gate: visual and honest-money pass (branch web/pay-monthly-1016, local, not pushed, not deployed, nothing applied to production, no Razorpay call)
- Gate on a dev server (port 3160, webpack) with real pointer clicks, 390x844 and 1440x900, Night and Day, env unset and a fake plan id set in the process environment only. Findings, fixes and the evidence IDs are in `docs/design-decisions/web-pay-monthly-1016.md`.
- Fixed: the first-payment confirmation was lost after checkout; a pending payment re-offered Start Pro; the charge-on-start and renewal terms moved above the button; Account names the rupees and next payment, has a lapsed state, a retryable cancel and switches at once after a cancel; a failed payment with Pro off no longer offers a refused action; /refunds follows the plan setting; PrepOS, Radar and XP removed from /pricing; table labels, dead band and nested confirm card fixed.
- Verified: lint clean; test:app 268, test:auth 52, test:recovery 182, test:learning 277, test:billing 87 (11 new); `next build --webpack` passes (the default Turbopack build fails on the node_modules junction in this worktree). Not covered: real Razorpay modal, screen reader, reduced motion, real device.
- Open: the shared mobile dock arrow and price note (landing owner), "Open PrepOS" in the Account wallet strip, runbook Part 2 TEST run still to do.

## 16 October 2026 - Q8b finished: nta_question_index kept current by every publish path and the existing daily cron (branch web/ntaidx-1016, local, not pushed, not deployed, nothing applied to production)
- vercel.json is back to its two crons (finalise-sessions, refresh-inventory): the third entry added on 15 Oct is removed. The daily safety rebuild now runs inside `/api/internal/refresh-inventory`, after the inventory refresh, with a 250 s start deadline; `/api/internal/rebuild-nta-index` stays for manual runs (`?subject=`, `?force=1`). It rebuilds a subject only for `newer_questions`, `content_changed` (content-hash drift of an indexed question) or `max_age` (7 days), oldest first; a repeat run writes nothing; one log line per run (`describeNtaIndexRun`) and the outcome under `ntaIndex` in the response; an index failure never changes the inventory status code.
- Publish paths wired (`data/nta_index.js`): authored publish (already), `question-republish.mjs`, `question-hold.mjs --mode=restore`, `question-reorder.mjs` (keep-live apply, restore, release), and the factory/worker (`publishFactoryQuestion`, `publishFactoryGroup`, `publishQuestion`) through a throttled queue (at most one rebuild per subject per 30 minutes, flushed at batch ends; `NTA_INDEX_REBUILD=off`). Concurrent rebuilds of one subject are serialised with one follow-up run. Website routes (moderation, uploads, admin factory) publish no indexable question; a test pins that.
- `_userProgress` chunked (`data/practice_progress.js`, chunks of 100 ids, 4 in flight, partial failure flagged and logged): above about 700 ids the single `.in()` was refused and the history was silently ignored (Accountancy). `_weakConcepts` had the same cliff plus the 1000-row cap; it now pages and chunks. Decision: id chunks, not a per-subject scan, because that keeps the result identical for rows whose `subject` is null.
- Tests: new `nta_index_maintenance.test.mjs` (10, in test:nta), `practice_progress.test.mjs` (7, in test:app), `ntaIndexFakeDb.mjs` shared fake; vercel_config pins two crons. test:nta 180, test:recovery 182, test:app 275, test:factory 332, question-reorder 25 (1 skipped) pass; eslint clean on data, src/app/api, scripts/pipeline and the touched scripts. test:authored-publish 78 of 79 with the same one failure as before ("merging wave 2 again reproduces the committed tables byte for byte"; CRLF in the committed agent tables on this checkout, code this change does not touch).
- To switch on, the owner needs: apply migration `20261013190000_nta_question_index.sql`; set `CUET_EVIDENCE_SIGNING_KEY` in Vercel production and redeploy; run `scripts/nta-index-build.mjs --write --allow-production` once. See the runbook section "Switching it on".

## 16 October 2026 - Production database: five additive tables for the 1016 batch applied (trap_atlas, revise_cards, my_colleges, app_errors, funnel_daily)

- Why: the 1016 batch (deploy/batch-1016) reads and writes these tables: Mistake Lab slice 4 (trap atlas, Revise), My colleges (Today, Compass, Account), app crash reports, and the landing funnel. The live code (77713336) does not use them, so applying them before the deploy changes nothing for students.
- Applied by Claude (session 604ced81) under the owner's standing database grant (14 Oct), at about 04:20 IST, to production isrxrxzjocewrdureyhp, in this order: 20261015210000_trap_atlas, 20261015210100_revise_cards, 20261016090000_my_colleges, 20261016100000_app_errors, 20261015233000_funnel_daily. Each was dry-run on staging onwkqxmjqjrhfbjjdydu first by the batch merger, with a rolled-back smoke test. None of the five tables existed in production before.
- Verified after: all five tables have row level security on, no policies, and table grants only to postgres and service_role. The seven functions (record_trap_atlas, my_colleges_replace, my_colleges_add, my_colleges_remove, app_error_record, app_errors_top, funnel_increment) are executable only by postgres and service_role. No rows were written.
- Undo, newest first: supabase/undo/20261015233000_funnel_daily.undo.sql, 20261016100000_app_errors.undo.sql, 20261016090000_my_colleges.undo.sql, 20261015210100_revise_cards.undo.sql, 20261015210000_trap_atlas.undo.sql. Run the undo only after rolling the website back to a build that does not use the table.
- Still owner-gated: FUNNEL_ENABLED stays off until the owner sets it; nta_question_index (web/ntaidx-1016) is not applied.

## 15 October 2026 - Q8b: nta_question_index kept current (branch web/q8b-1015 from production 3fc0095b, local, not pushed, not deployed, no migration change, nothing applied to production)
- (a) `scripts/question-publish-authored.mjs` apply rebuilds the index rows of the touched subjects after a clean read-back (`data/nta_index.js` `rebuildNtaIndexForSubjects`; never fails the publish; skipped without the signing key or the table; `--no-index-rebuild`). (b) New daily cron `/api/internal/rebuild-nta-index` (vercel.json `0 22 * * *`): production only via `data/full_bank_guard.js`, existing CRON_SECRET or x-internal-secret check, rebuilds only subjects whose index is older than their newest live question, one subject read at a time, 240 s deadline, skips never-built subjects. (c) `data/nta_pool.js` falls back to the full read when the subject's index is older than its newest live question (`data/nta_index_freshness.js`: max verified_at against max created_at or live_at; a failed check also falls back; `timings.indexStale`). `scripts/nta-index-build.mjs` now uses the shared builder and stamps verified_at per subject. Runbook updated.
- Tests: new `data/tests/nta_index_fresh.test.mjs` (14, in test:nta), publish hook test in authored_publish, vercel_config now pins three crons. test:nta 169, test:recovery 182, test:app 235, answer-integrity 11, question-reorder 25 (1 skipped) pass; test:authored-publish 78 of 83 with 1 failure, "merging wave 2 again reproduces the committed tables byte for byte" (agent biology), in code this change does not touch. eslint clean on the changed files. Staging check (read only): the columns the check reads exist and accountancy's index (built 15 Oct 16:07) is newer than its newest question.
- Production gates unchanged: apply `20261013190000_nta_question_index.sql`, run the build with `--write --allow-production`, set CUET_EVIDENCE_SIGNING_KEY in Vercel production before the cron can rebuild.

## 15 October 2026 - Usage limits: A5 slim session start and A6 nta_question_index prepared (branch web/fix5-1015 from main 3be06112, local, not pushed, not deployed, migration NOT applied to production)

- A5 `data/practice_pick.js` (used by `Database.getQuestions` for Quick, Smart and Full; NTA mode and `data/nta_engine.js` are untouched): a session start reads the subject's questions WITHOUT the `evidence` and `provenance` columns (every other column, plus three json-path columns that place an evidence row), ranks and picks on those, then reads full rows only for the picks and the newest-N window the usage meta looks at. Evidence-managed rows (136-181 per Commerce subject, about 35-40 KB each, 65-75% of the bytes) are presumed eligible until their full record passes `readablePracticeQuestions`; rows that fail are dropped and the picks re-run (up to 8 rounds). Anything not provably identical (recency threshold straddling, empty after verification, too many rounds, any read error) falls back to the old whole-subject read, as does `PRACTICE_SLIM_READ=off`. The light pool is kept 5 minutes per server and subject (`PRACTICE_POOL_CACHE_MS`); the picks themselves are always re-read fresh and re-checked.
- Comparison test `data/tests/practice_pick_parity.test.mjs` (in `test:app`): before (whole-subject read) against after (slim read) over 6 generated subjects (legacy rows, signed eligible evidence rows, stale/bad-signature/changed/factory-looking rows), Quick, Smart and Full, with progress, recency, weak topics, holds, exclusions, chapters, difficulty, requireEvidence and passages: picks, order, tiers, usage meta, validation and every returned row are deep-equal; fallbacks are rare. Also run on real staging data (666 evidence rows, real signatures): identical picks for accountancy Quick 10, business_studies Full 50, english Smart 15, economics Quick 25.
- Bytes per start, production figures from SQL on 15 Oct (full read -> slim read, JSON bytes): Accountancy 8.3 MB -> about 3.5 MB (10 questions), Business Studies 7.4 -> about 1.7, Economics 7.1 -> about 1.8, English 6.2 -> about 1.7; a 50-question Full mock reads about 3 MB for the three smaller subjects and about 5 MB for Accountancy. With the 5-minute light pool warm, Business Studies Quick is about 0.8 MB. Real gain is roughly 3-5 times fewer bytes per start (not 10 times): every evidence row must be read to be verified, and the evidence rows are what most picks are. A further step would need the verified verdict stored per row.
- A6 `supabase/migrations/20261013190000_nta_question_index.sql` is unchanged; its undo is `supabase/undo/20261013190000_nta_question_index.undo.sql` (outside `migrations/` so the CLI never applies it); runbook `docs/brain/RUNBOOK-NTA-QUESTION-INDEX-2026-10-15.md`. Dry run on staging onwkqxmjqjrhfbjjdydu (15 Oct, owner's 14 Oct database grant): migration applied (RLS on, only service_role grants, 2 indexes), `scripts/nta-index-build.mjs` dry run then `--write` indexed english 156, accountancy 105, business_studies 162, economics 112 (all loaded rows verified; slim 0.25-0.39 MB against 4.2-5.9 MB full), `loadNtaPool` read source `index`, the undo dropped the table and NTA mode fell back to `full` at once, then the migration and index were put back on staging. Production was not touched: `nta_question_index` is absent there (checked), questions.id is text with a primary key, roles anon, authenticated and service_role exist.
- Verified 15 Oct: `test:recovery` 145, `test:nta` 155, `test:learning` 277, `test:app` 232 (new parity test), `test:auth` 50, `test:answer-integrity` 11, `test:factory` 332, all pass; `test:question-reorder` 25 of 26 (one skipped); eslint --max-warnings 0 clean on the changed files; `npm run build` 76 of 76 pages (turbopack root set to the parent folder for the junction, then edited back; not committed). Not caused by this change (data tables, no file of this branch touched): `test:authored-publish` fails "merging wave 2 again reproduces the committed tables byte for byte" (agent biology) and `test:study` fails the WordNet "LICENSE_UNAVAILABLE" check.
- Deploy gates: (1) deploy A5 after the owner OK; first practice start in each Commerce subject logs `[practice-pick] {"rounds":2,...}`; `[practice-pick] slim_fallback` or `slim_error` lines mean the old read ran (watch for them). Rollback: set `PRACTICE_SLIM_READ=off` in Vercel and redeploy, or redeploy the previous deployment. (2) A6 production apply is the orchestrator's: apply the migration, verify, then run the index build with `--write --allow-production` from a machine that has the production keys; until rows exist NTA keeps the full read (no behaviour change). (3) Open, owner decision: `Database._userProgress` sends every pool id in one `.in()` URL and swallows the error; on staging a 800-id list returns HTTP 400, so for pools of about 700 ids or more (Accountancy, 1,405) the student's history is silently ignored in ranking today. A5 keeps that behaviour identical on purpose; chunking the call (150 ids a time) would make Accountancy honour history and change its picks.

## 15 October 2026 - Usage limits: fixes A1 to A4 from USAGE-LIMITS-DIAGNOSIS-2026-10-15 (branch web/usage-fixes from main 48309076, local, not pushed, not deployed)

- A1 counts refresh once a day: `publicInventory` (home page, dashboard, practice quote, app) serves the stored `public_inventory_snapshot` row and never counts; the 15-minute `after()` refresh and the inline count on a missing or day-old row are gone. Only the daily cron (`/api/internal/refresh-inventory`, 21:30 UTC) recounts. A row older than 36 hours is still served, marked `stale: true`, with one `[inventory]` log line; with no usable row `/api/stats` answers its existing 503 `unavailable` (no-store) and the quote its existing `inventory_unknown` (nothing charged). A failed snapshot write now fails the cron instead of being ignored. Production row checked read-only on 15 Oct: present, `available`, 8,197 questions, refreshed 3 minutes earlier.
- A2 evidence files once per server: `sharedEligibilitySnapshot()` in `data/evidence_registry.js` parses `calibration_manifest.json` and `source_registry.json` once per instance (frozen, re-read only if a file's size or mtime changes, a failed read is never remembered) and is passed by answerReviews (result page), Mistake Repair, the learning plan (also its pathway registry read), `/api/sessions/[id]/check` and question moderation in `data/db.js`. Local measure: 50 checks 2,051 ms before, 17 ms after (about 40 ms for the one parse); about 11 MB of heap per instance. Verdicts equal a fresh read on 17 fixtures bound to the shipped files (one eligible, the rest covering every refusal kind).
- A3 `vercel.json` `"regions": ["sin1"]` (Singapore, AWS ap-southeast-1; the production Supabase project isrxrxzjocewrdureyhp is ap-southeast-1). Hobby allows one region; crons unchanged.
- A4 `data/full_bank_guard.js`: whole-bank reads (the inventory refresh, `Database.getAllQuestions`) run only when `VERCEL_ENV === 'production'`; anywhere else one `[full-bank-read] blocked` line and the cron route answers 409 `full_bank_read_blocked`. Local servers and agents get the stored counts. The admin factory dashboard's bank read is not guarded (local commissioning against staging uses it). Fix 5 (practice start selection) untouched; no .env file changed.
- Verified 15 Oct: `test:recovery` 145, `test:learning` 277, `test:app` 224, `test:auth` 50, `test:du` 19, all pass (new: evidence_shared_snapshot, inventory_snapshot rewritten, full_bank_guard, vercel_config; evidence_snapshot added to test:recovery); `test:nta` 154 of 155: the CPU-timed "2,000-question pool" test ran 3.0 to 4.1 s against a 3 s target with the machine at 100% CPU, and none of its 70 imported files changed. eslint clean on the 15 changed files. Production build (Turbopack, root pointed at the parent folder for the node_modules junction, then reverted) compiled, 76 of 76 pages.
- Deploy gates: owner OK to deploy. After deploy check (1) the first 21:30 UTC cron logs `[inventory] daily refresh stored N questions` (a 409 would mean `VERCEL_ENV` is not exposed to functions: Settings, Environment Variables, system variables), (2) the deployment shows `regions: ["sin1"]` and `/api/stats` answers 200, (3) Supabase gateway logs show no whole-bank `questions` reads outside the cron. Expected: about 25 of 26 daily whole-bank copies gone (about 1 GB a day of raw egress), per-question evidence parsing gone from result, repair, plan and check paths, and database round trips from about 220 ms to a few ms.

## 15 October 2026 - Website v2 deployed (branch web/v2-1015 to main)

- What: the live site made richer (owner rejected the cut-down restructure): logo B only, brand switch (Bricolage plus lamp-lit 3D subject objects), held scroll stories on phones and desktop (Lab, feature tour, Mistake Lab), the statement shelf, livelier Mobi, designed controls, the Start key and sheet, the account page, 2-step onboarding, Practice tiles with lit objects, arena phone polish, copy pass without hedges; Mistake Lab v4 slice 1 on the result page (marks ledger, first-pick re-mark, how others answered; cohort snapshot data/cohort/question_picks.v1.json, aggregates only).
- Checks before push: eslint clean on 47 changed files; test:app 213, learning 277, recovery 71, auth 50, nta 150, du 19; production build 76/76 pages; headless sweep at 360 and 1440 px with no sideways scroll and no console errors; two critic and fix rounds on phone and desktop captures (mockmob-next/tmp/web-v2-pass2).
- Not in this deploy: Mistake Lab slice 2 (capture, one time rule, Replay) stays on web/alive-1015 until its fixes pass.
- Rollback: redeploy the previous production deployment in Vercel (main was 11e30ec3).
## 15 October 2026 - Mistake Lab v4 slice 2: capture, one time rule, Replay, passage sets and the submit sheet, independently verified (branch web/alive-1015 and ui/phase2, local, not pushed, not deployed)

Spec `mockmob-next/tmp/mistake-lab-v4/SPEC.md` 4.5, 4.6, 6 and 8. Web commits 49760343, 5551d2e3, acb7bb0b, c7911899, 365f5211, 5a386558, dd7a45e9, 299a822f; app commits e4144e87, 8d8c07a5, c4cd5dac, 57aed8a9. No migration: `record_recovery_events` checks only seq and clock.

- Server: accepts end, away, back, strike and via on a visit (next, previous, palette, swipe, resume, set, sheet), keeps marks; `data/paper_trace.js` is the one time calculator for Time and decisions, the ledger, the Replay, the session read and PrepOS. Rule 5: a question shown with its passage set (via `set`) counts as opened, never as time. Rule 6: from a `sheet` visit (the submit sheet or the NTA submit check) to the next visit or answer, time is on no question. A time-up that reaches the server after `expires_at` keeps its end at the paper limit, only when every earlier event is already stored (`lateTimeUpEnd`); nothing is added to the session log.
- Web runner: capture is data only. A passage page records every other question of its set (via `set`) before the question in focus; the submit sheet and the NTA submit check record a `sheet` visit; strike parity with the app; the 5,000-event record keeps room for answers. App: the same capture, the submit page as a `sheet` visit, the practice result on the one time rule (`lib/core/domain/paper_trace.dart`, a port), and `OldServerFallbackApi`, which resends a refused save or submit with the event set an older server knows.
- Verified 15 Oct (independent check): `test:recovery` 138, `test:nta` 155, `test:learning` 277, `test:app` 147, all pass; eslint clean on the 27 changed files. `runner_nta_ui.test.mjs` is unchanged since c7911899 and the old-payload golden (`score_session_golden_v1.json`) since 49760343; both pass. 3,000 random old-format records through the 5a386558 modules and HEAD give identical trace, Time and decisions, ledger, PrepOS dwell and session read; the Replay differs only in the new denominators and in return-visit time that now leaves out time away. Time and decisions on the Business Studies and English passage fixtures matches a hand count (for example Q41 3m 10s, Q43 50s until the sheet at 49:40, Q45 and Q50 shown only). App: analyze clean apart from one warning in another session's uncommitted test edit; `test/unit/result`, `practice` and `runner` 836 pass; `test/golden/runner` and `result` 168 pass with the runner goldens untouched; the five replay contracts and inputs are byte-identical to the web's.
- Fixed in the check (299a822f): `onScreenQid` used `Array.prototype.findLast`, which Next.js does not polyfill, outside any try just before the NTA submit check; on a browser without it the Submit test button would have thrown. It is now a plain loop, and the sheet visit is recorded inside a try.
- Deploy gates: deploy this server before any APK built from ui/phase2 (the app's fallback is a safety net, not the plan: a server deployed in the middle of a paper whose app restarts before the submit can still meet EVENT_CONFLICT). `next build` was not run in this check (about 2.6 GB of RAM free); the Replay change in dd7a45e9 was not rendered in a browser.
- Open, owner decision: web passage records made before set visits existed still read their unanswered, never-focused sub-questions as never opened (no inference from passage group ids, so old payloads read exactly as before). Low: on the web a tab closed within a frame of an answer tap can leave the saved draft one answer behind its events (as before slice 2).

## 15 October 2026 - Time and decisions restored in the Lab, website and app (branch web/alive-1015 and ui/phase2, local, not pushed, not deployed)

What was lost: 236c49c6 replaced the Lab's "Replay your decisions" slider (every visit and pick with its time, and the net first-to-final marks effect) with a folded change log; 220e8d51 then hid the whole Find step (rushed-pick and changed-answer observations) on Full and NTA results once the SWOT was ready. Per-question time was left only as a bare "2m 41s" chip; nothing compared it with what the paper allows, and the app never showed time or when an answer changed (only "Answer changed").

- `data/time_decisions.js` (pure, free, no model): the paper's pace (durationMinutes, else the mode's limit in test_modes), per-question time from the device timeline (gaps over 30 minutes left out and said so; the last question on screen is "At least"), median over 10 or more timed questions, revisits, every pick with its paper-clock time and the gap since the previous one ("Picked B at 0:42. Changed to C at 1:55, 1m 13s later."), the marks effect of each question's changes and the paper's net, the time split by right, wrong and blank, and the 5 longest questions. Held or corrected questions keep their times and leave the marks effect. No cohort numbers: there is no cross-student time data yet.
- Website: the Lab's Find step is back on every result (1 Find, 2 Repair, 3 Prove). With the SWOT ready it shows only Time and decisions (no second chapter list); without it, chapters and observations first, then Time and decisions (the changed-answers observation is dropped there, the list replaces it). Each opened answer shows "Your time and picks"; its repair then leaves out its own change and time record lines so nothing repeats. The folded log keeps only the playbook note. `src/components/result/TimeDecisions.jsx`, `time-decisions.css`.
- App (ui/phase2, commit 3feab035): the same read ported line for line (`lib/features/result/model/time_decisions.dart`), a Time and decisions section after "Where the marks went" and "Your time and picks" in each answer. The app already records visit and answer events in every runner (practice, Full, NTA) through the session engine, so no recording change.
- Verified 15 Oct (Claude): eslint clean on the changed files; `test:recovery` 48 of 48 (with the new `time_decisions.test.mjs`), `test:learning` 274 of 274; a server render of TimeDecisions on a generated 50-question NTA paper (no undefined or NaN). App: analyze clean, result tests 47 of 47 (new time_decisions_test and time_section_test with the same fixture sentences). Not rendered in a browser or on a device (no dev server or emulator this run).

## 15 October 2026 - Mistake Repair v3 and the post-mock SWOT on the website (branch web/alive-1015, local, not pushed, not deployed)

Built from `mockmob-next/tmp/repair-v3/SPEC.md`. Nothing is migrated: trap type and prompt version live in `ai_credit_reservations.receipt`; the SWOT and the record lines are computed per request from rows the attempts route already reads.

- Repair v3 (server): `REPAIR_PROMPT_VERSION` (default 3; set `REPAIR_PROMPT_VERSION=1` to roll back to the v1 prompt and payload). The call gets a typed trap, why the key is right, optional contrast, one line for each option that is neither the pick nor the key (all or none), rule, memory hook and "another way" in one call and one credit, `maxTokens` 1400 (`providerCore.generateAIResponse` takes an optional `maxTokens`, clamped 200 to 2000, default unchanged). The model's "next step" is gone: "Do this next" is the real `Practise 5 on {chapter}` action. Every field is trimmed to a sentence end, checked for claims about the student and for contradicting the key, and a bad optional field is dropped, never the repair. Stored v3 responses also carry the `why_tempting` and `key_idea` aliases and `pattern`; stored v1 and v2 payloads come back without `version`.
- Trap pattern: `data/repair_pattern.js`. One line from the student's own typed repairs: in a chapter, at least 3 typed repairs with at least 2 sharing the trap; else in the subject, at least 5 with at least 3 sharing it and at least 30%; v1 and v2 repairs count in neither number. The line is dated from the earliest repair it counts, in India time ("Since 9 Oct, 2 of your 3 repairs in Goodwill had this trap."), so it is the whole count for that period; an untyped repair inside the period that could be in scope (a v1 rollback) or an undated counted repair gives no line. A failure or a read over 1.5 s gives `pattern: null`, never a failed repair.
- SWOT (free, no model): `data/attempt_ledger.js` (one set of per-chapter counts for the paper and the record), `data/mistake_insights.js` ("From your record" lines per wrong answer), `data/mock_swot.js` (four quadrants, "Do these next" plan of up to 3 rows, later lines). Full and NTA mocks only; practice attempts get `not_available`. `GET /api/attempts/[id]` gains `mistakeInsights` and `swot` (each in its own try/catch; `SWOT_ENABLED=off` omits `swot`). The Lab's Find step is left out only while the SWOT is `ready`.
- Web: `MistakeRepair.jsx` v3 layout and loading lines on real elapsed time, `SwotPanel.jsx`, `ScoreRecoveryLab.jsx` `hideFind`. Preview fixtures: `/preview/arena?view=result&mock=full|nta` (real SWOT over illustrative papers), `&repair=v3|v3-stored`, `&checks=unavailable`.
- Also fixed: the repair run track (`.rt__seg`) inherited the app shell's `min-width: 44px` on every button, so a run of 10 mistakes made the result page wider than a 375 px phone (found in the preview). The steps now share the row (`repair-run.css`).
- Verified 15 Oct (Claude, web integrator): `npm run lint` clean; `test:learning` 266 of 266, `test:recovery` 40, `test:app` 147, `test:nta` 150, `test:auth` 50, `test:answer-integrity` 11, all pass; `test:study` 21 of 22 (the known Windows CRLF failure in the content gate). `next build` passes (turbopack root temporarily pointed at the parent folder for the node_modules junction, then reverted). Dev preview on port 3109: Full mock shows the panel, the plan and the Q buttons; NTA mock shows the panel and no Mobi; quick practice shows no panel and keeps the three Lab steps; a v3 repair and a v1 repair both render; light and dark, 375 px and desktop; no console errors. The app's parse test (`swot_model_test.dart`, 19 tests) passes against this branch's `data/tests/fixtures/swot/contract_v1.json` with no model change.
- Truth review fixes (15 Oct, same branch): the pattern line above is dated; `claimsAboutStudent` also catches "You confused / may have confused / forgot / overlooked / missed / misread / ignored / rushed / assumed", "you were ..." and "your mistake was" (not "If you add ...", "If you were the buyer", "you were asked to", quoted option text, or the record's own "you missed this in Mock 2"); `cleanRepairText` turns "42!" at a sentence end into "42." and keeps "!" only as clear maths ("5! = 120", "n!/(r!(n-r)!)", "5! is 120"); SWOT counts carry denominators ("4 of 50 questions left blank", "7 of 50 questions were never opened", "2 of the 3 questions you had missed before were wrong again", m read from the attempts themselves); `untried` says what was checked ("have no answers in your last 4 Accountancy papers", N = the record's papers, and any paper in that span, device-scored included, removes a chapter); `mistakeInsights` is `{}` until the answer checks are ready. `findRepairTraps` now also reads `created_at`; its select was checked against production as SQL on 15 Oct (read only): `receipt` is jsonb, `receipt->'repair'->>'trap_type'`, `receipt->>'subject'` and `receipt->>'chapter'` resolve, the plan uses `ai_credit_reservations_user_idx`, and the 6 committed production repairs are all v1 (no trap, no subject), so no pattern line can show until v3 repairs exist. Tests: `test:learning` 272, `test:recovery` 40, `test:app` 147, all pass; eslint clean on the touched files; next build --webpack exit 0 (placeholder env, build command only).
- Not done: no live repair yet (about USD 0.0005 and 1 test credit; needs the owner's OK); the `findRepairTraps` select has not run through live PostgREST itself (the SQL equivalent has; a failure gives `pattern: null`); model output quality and field drop rates for v3 are unmeasured until a live call (spec D.3, watch 7 days after shipping); not deployed. `APP-API-CONTRACT.md` for the new fields is in `wt-phase2` (ui/phase2), not in this branch.

## 15 October 2026 - Production database: account takeover guard applied (migration 20261013150000_auth_unconfirmed_passwords), Mistake Repair verified live

- Why: /api/auth/email-login (live) calls public.auth_clear_unconfirmed_password, which did not exist in production; Vercel logged PGRST202 twice at about 09:00 IST on the owner's sign-in (sign-in itself worked, the call is best effort). The migration closes auth review H2: a password set through the public sign-up endpoint on an unconfirmed email would survive the student's later confirmation.
- Applied by Claude (session 604ced81) under the owner's standing database grant and security-hotfix OK: staging onwkqxmjqjrhfbjjdydu first, with a rolled-back test (RPC cleared 1 row case-insensitively, the trigger dropped a password set before confirmation, a confirmed account kept its password, only service_role can execute), then production isrxrxzjocewrdureyhp at about 09:35 IST. Verified after: 2 functions, 1 trigger on auth.users, anon cannot execute, service_role can.
- Effect: 97 of 1,639 accounts are unconfirmed and carry a password. Nothing changes for them until they request a code or confirm; then the pre-confirmation password is removed and they sign in with the code. Confirmed accounts are untouched.
- Undo: drop trigger if exists mm_drop_password_set_before_confirmation on auth.users; drop function if exists public.auth_drop_password_set_before_confirmation(); drop function if exists public.auth_clear_unconfirmed_password(text);
- Owner step still open: Supabase Authentication > Sign In / Providers > Email > Confirm email ON (cannot be checked by SQL).
- Mistake Repair verified live: 08:47 IST runtime_ai_requests row openai gpt-6-luna, stage primary, receipted, 480 in / 196 out tokens, USD 0.00015 (the owner's signed-in repair). The missing OPENAI_API_KEY root cause is closed.

## 15 October 2026 - Mistake Repair website client catches up with the server's failure codes (branch fix/repair-reliability, local, not pushed, not deployed)

`MistakeRepair.jsx` now sends through `data/repair_client.mjs`. (1) After any failure body with `charged: 0` the next attempt uses a fresh requestId (it used to reuse a released one, so the first retry hit `operation_released` and wasted a click); a timeout or dropped connection has no body, so it keeps the id and can never double charge. (2) The request is aborted after 95 s (the route budget is 90 s) with "This took too long. You were not charged.". (3) The server's own `message` is shown for every code (`provider_timeout`, `provider_unavailable`, `budget_reached`, `wallet_unavailable`, `paused`, `unusable_output`, `could_not_start`), never a generic line when one was sent. `budget_reached` and `paused` offer no retry button (trying again cannot help); the others do. Tests: `data/tests/repair_client.test.mjs` (in `test:learning`). The Flutter app has a matching change on ui/phase2 (not committed by this branch).

## 14 October 2026 - Mistake Repair reliability fixes (branch fix/repair-reliability, from deploy/nta-r5; local, not pushed, not deployed)

From `docs/brain/REPAIR-LAB-AUDIT-2026-10-14.md`. (1) The passage is now sent: the repair and blind prompts read `passageText` (snapshots) or `passage_text` (rows) and the passage title, before the question. (2) NTA shuffled options: key checks compare by option identity (option ids when both sides have them, else the comparable text with letter prefixes removed; `data/option_compare.js` `alignOptions` and `sameKeyOption`, with the snapshot's recorded `optionOrder` as the fallback when an option was also edited). `repairEligibility` no longer refuses a harmless shuffle as `key_changed`. `answerReview` (and so `readAnswerReviews`, `sessionCheck` and the repair refusal review) had the same bug, proved by failing tests first: a shuffled snapshot read as `content_changed` and the result page hid its key. It now reports `currentIndex` in the order the student saw. The one older test that pinned "a pure reorder is content_changed" now pins "edited options are content_changed". (3) Time (owner D1: Hobby with Fluid compute): `maxDuration = 90` on the repair route; per-call SDK timeouts (25 s main, 30 s blind), main work done by 45 s, everything by 78 s, worst case about 81 s; every OpenAI-compatible client has a 45 s default (`OPENAI_TIMEOUT_MS`) instead of the SDK's 10 minutes; a timeout releases the reservation. (4) Stuck credits: an open repair reservation that is expired or older than 150 s is released (`mm_ai_release_credits`, reason `expired`) and answers 409 `operation_released`; one that may still run answers 409 `in_progress` and blocks a second charge; a failed commit is retried once, then released; the daily cron `/api/internal/finalise-sessions` also calls `mm_ai_release_expired(100)`. (5) Visibility: failed provider calls keep status, code and type (receipt and result), the runtime guard's three stops keep their kind, one log line per failed repair (stage, code, kind, provider status and code, model, ms; no student data), new codes `provider_timeout` 504, `provider_unavailable` 503, `budget_reached` 503, `wallet_unavailable` 503 beside the existing ones. (6) The response filter blocks only claims about the student (predicted marks, scores, ranks, percentiles, cut-offs, admission chances, guaranteed gains), not the words rank, percentile, guarantees or "you will get x = 3". (D2) One fallback after a failed Luna call (timeout, quota or 429, 5xx, rejected parameter) to Anthropic `claude-haiku-5-5` at low effort, no temperature, only after the primary failed; the receipt records the provider and model that ran.

Not done, needs the owner: apply `supabase/migrations/20261014120000_runtime_ai_price_claude_haiku_5_5.sql` (USD 0.10 / 0.50 per million, NOT APPLIED; until then the guard refuses the model and the fallback simply does not run); set `ANTHROPIC_API_KEY` in Vercel Production if absent; the one-time release of credits already stuck in production (D8, the owner runs it in the Supabase SQL editor; nothing was run against production). Web `repairRetryPolicy` and the app still reuse a released request id, so the first retry after a failure meets `operation_released` once; the app must map the new codes (the generic 5xx copy covers them meanwhile). Verification: `npm run test:recovery` 40 of 40, `test:learning` 161 of 161 (now includes the new provider, flow, failure-copy, wiring and Haiku-price tests), `test:app` 108 of 108, `test:nta` 150 of 150, `test:answer-integrity` 11 of 11, `test:auth` 50 of 50; a scratch smoke of the real SDKs with a faked fetch confirmed the Haiku wire body has no temperature or thinking and carries `output_config.effort: low`, and that a stalled Luna call times out through the SDK and falls back. No paid model was called.

## 14 October 2026 - Authored wave 2: General Test rows were planned under the wrong subject id, fixed before any publish (local, not pushed, not deployed, not published)

The wave-2 publish plan wrote the public subject `general_test` into `questions.subject`; the live bank stores General Test as `gat` (`data/cuet_controls.js`). Practice and NTA reads use `gat`, so the 77 General Test rows would have been invisible, and the dry run's `liveBefore` read 0 for `general_test`. `toQuestionRow` and `toPassageGroupRow` now store the internal id; every read of the target (live counts, lookalikes) uses it. The content hash covers `subject`, so the 77 General Test entries of `data/nta_agent_scores/general_test.json` and `data/nta_fit_scores/general_test.json` were merged again against the `gat` hash (hash fields only; no score, flag or other file changed). Wave 1 is unaffected (no alias; plan hash `39a4b051...` unchanged). New expected dry-run values: `summary.bySubject` gat 77 (not general_test 77), plan hash `73b630705530e07588c6eef2ba9857927d8faed9cabf0d118da065af679207c4`, candidates sha unchanged, 382 rows, 1 group, scores bound 382 of 382 (agent and fit), blockers none. Any plan file from before the fix (hash `89e4b3c6...`) is void. Tests: `test:authored-publish` 82, `test:nta` 150, `test:nta-e2e` 418, all pass. Not run: the online dry run, the apply, any deploy. Runbook: `docs/brain/RUNBOOK-PUBLISH-AUTHORED-W2-2026-10-14.md`, section 1 item 9.

## 14 October 2026 - Authored wave 2 prepared for a publish dry-run: 386 questions, agent and fit tables merged (local, not pushed, not deployed, not published)

Acceptance re-run with the re-run judge files (451 written, 400 accepted by the rule), the 10 reworded questions judged afresh (9 pass; `87c9264b` fails: all five fresh solvers answered A against a key of D that is right by computation, left out, not invented), expert verdicts and the spot-check applied, 27 questions reviewed by one reviewer (this pass) because they became accepted after the expert pass. Final set 386: Biology 53, Computer Science 74, English 55, General Test 77, Geography 55, Mathematics 65, Political Science 7. 31 drops with reasons in `docs/brain/reports/authored-w2/wave2-dropped-2026-10-14.json`; 12 of them are expert-repaired questions held until a 3-solver blind re-solve of the repaired text exists (none was run; no result invented). Wave-1 tooling made wave aware (source per wave, five more subjects, English verbal types, Geography case sets, a question that completes a wave-1 set, provenance per wave): the 55 wave-1 tests are unchanged and green, 20 wave-2 tests added. The agent and fit tables of the seven subjects carry the 386 entries (existing entries untouched). Offline engine check: 386 of 386 admitted, both new sets servable. Verification: test:authored-publish 75 of 75, test:nta 150 of 150, test:nta-e2e 418 of 418. Not run: the dry run against production, the apply, any deploy. Runbook with the commands and expected counts: `docs/brain/RUNBOOK-PUBLISH-AUTHORED-W2-2026-10-14.md`.

## 14 October 2026 - NTA engine r5.1: pre-deploy review fixes on deploy/nta-r5 (local, not pushed, not deployed)

Three fixes from the pre-deploy review, so one push carries them with r5. (1) Repeats never refuse a paper: holding back seen questions (earlier NTA papers, practice answers) left a student's second paper short on the 13 Oct export (General Test 46 to 44, Economics 45 to 44, both refused). When the seen-first build is refused for too few questions or passages, the engine builds again with repeats allowed and every gate, quota and structure check unchanged: 'relaxed' (a seen question gives way only to an equally useful new one), then 'none'. The notice says "N questions repeat from your earlier NTA papers"; structure.repeatFallback and crossPaper.repeatsAllowed record the builds. Gate verdicts are shared across the builds of one call, so the extra builds are cheap. Offline on the export (papers 1/2/3 for one student): General Test 46/46/45 (was 46/44 refused/44 refused), Economics 45/45/45 (was 45/44 refused/44 refused), Biology 46/45/46 (unchanged). Unsubmitted NTA sessions still count as earlier papers (their paper was on screen; the finaliser turns them into attempts after the deadline anyway). (2) Website refusal: a refusal the bank decides (detail.retryable false for no_scored_questions, no_passage_sets, too_few_questions) now shows "No NTA paper for <subject> yet", the engine's sentence, Start a Full Mock (direct for Premium, the dashboard set-up otherwise) and Back to dashboard, not "This did not load" with a futile Try again; a refused paper's notice no longer describes positions of a paper nobody sees ("Q12-21 are standalone instead"). (3) When no question can be placed, the sentence names the gate that kept most questions out (refusal.cause: quality, fit_not_judged, fit_below_bar, veto, syllabus, unscored), instead of always blaming quality. Also: .next-staging/ ignored by eslint; two lint false positives fixed; the NTA e2e fake now reads json paths (selection_meta->>mode), so the e2e second paper exercises the earlier-papers path. Verified: lint clean; test:nta 143, test:nta-e2e 418, test:recovery 40, test:app 108, test:auth 50, all pass; next build (Turbopack) passes; refusal panel and the second-paper notice driven in a browser through /preview/arena/nta with the local backend at 375 px and 1366 x 650, light and dark, links clicked with a pointer. Not run: the production engine run, any deploy.

## 14 October 2026 - CUET-fit gate merged into fix/nta-mode (engine r5), authored wave-1 entries in the agent and fit tables (local, not pushed, not deployed)

`wip/cuet-fit` merged with `--no-ff` (47e0880): engine r5 (fit gate, judges' stored type and chapter, newest-first) on top of r4.1, the holds, the listed-order reorder and the authored publish tooling. No textual conflicts; semantic ones fixed in the merge: the authored check passes the merged fit tables to the engine, `engine_type_guess` uses `heuristicNtaType`, and two e2e checks were adjusted (time-up sessions start as a fresh student's first paper; the leak check no longer trips on the Computer Science chapter "Stack"). Then `scripts/authored-scores-merge.mjs --mode=merge --repaired-text=admit` (d593e84): 475 entries added to six agent and six fit tables, no existing entry changed. Verified offline: `--mode=check --impact` 475 of 475 eligible through r5 with the merged tables, 11 of 12 English sets servable; offline publish dry run binds 475/475 in both tables, plan hash unchanged. Tests: test:nta 134, test:recovery 40, test:question-reorder 26, test:authored-publish 55, test:nta-e2e 418, all passing. No database, network or model used. Open gates: the owner's approval to publish (RUNBOOK-PUBLISH-AUTHORED-2026-10-14.md section 10) and to deploy r5, which changes NTA mode for every subject (General Test 46 questions, Mathematics refused, Biology served).

## 13 October 2026 - NTA engine r4.1: verification findings on r4 (branch fix/nta-mode, not deployed)

Fixed after the independent check of 2c6e5a1. (1) Option shuffle: the explanation remap now reads "Option B", "option is B", "option B gives ...", "the choice would be C" (capitalised word, a linking word between word and letter); a reference it still cannot rewrite ("option, as powers add, B ...") keeps the stored order instead of going stale (shuffleBlockers). (2) Blocking judge flags match whatever the spelling ("Wrong_Key", "factual error"). (3) Seed and demo rows: "seed_import", "demo_import", "seed 2026-04", "PYQ 2023 (seed)", "PYQ demo" are caught; ids must be exact UUIDs (a padded id is rejected). (4) The "mainly" gate no longer flags "5 items, 2 mainly for households" or "Vitamin A, B mainly ..." (a comma needs a bracketed label or a roman numeral). (5) Listed-order keys: numbered ("1. 2. 3. 4."), item-text keys in printed order and two-pair match keys are caught; a stem that prints its items out of alphabetical order is judged by the printed order; label ranges agree (P-T). (6) Difficulty: an id such as "constructor" is not a correction; the run report separates corrections in the file from corrections that change a loaded row. (7) Cross-paper: the earlier-papers read asks only for NTA attempts (a student with 40+ other attempts keeps every NTA paper in view), orders sessions newest first, and a failed read is recorded as structure.crossPaper.lookupFailed. (8) Test fixes: finding 2 no longer assumes the paper is otherwise eligible (the CUET-fit gate has its own fixtures); the concept guard test pins the 5-gram check; new tests for every phrasing above.

Not changed, on purpose. Trailing "mainly" ("Which factor is mainly?") and "mainly found in" cannot be told from real corruption by pattern; a false positive only removes one item, so the gate stays strict and the second form stays a known gap. A "seed-bank" source is excluded (conservative). Short stems (under 60 characters) are covered by the key-answer, concept-key and chapter guards, not the 5-gram guard; same_key_answer is not limited to one chapter, so pool sizes should be re-read after the next production run (not run here). Two-level difficulty corrections stay automatic by the policy in NTA-ENGINE-POLICIES.md. A fresh pool that can only give a closest paper is served as that shorter paper with its shortfall recorded, not topped up with repeats (owner may choose the other way). Without a shuffle key the engine falls back to a fixed key; both server paths (practiceSessions.js, recoverySessions.js) require a generation key of 12 or more characters, so this is an offline default only.

Mark for review and the clock, accurately. Marks are saved on the server only in durable mode (LEARNING_SESSIONS_ENABLED=true). In the default device-ticket mode they live in the saved draft and in the submitted event log, like answers, and are lost with the draft; they never affect the score. The device-ticket clock holds while the signed start receipt travels with the page address or the saved draft: a lost draft with the receipt still in the address keeps the original start, but a start without a receipt (a bookmarked address without it, or a relaunch from the dashboard, which mints a new generation key) is a new test with a new 60-minute clock. Making relaunch resume the old clock is a product decision, not made here.

Verification (HEAD plus these edits, in an isolated copy because the shared working tree carries uncommitted CUET-fit work whose gate rejects the old fixtures): test:nta 123 of 123, test:nta-e2e 481 of 481, test:recovery 40 of 40. Not run: the production engine run, any deploy.

## 13 October 2026 — NTA engine r4: the expert review's findings 1-4 and 6-9 (branch fix/nta-mode, not deployed)

Policies and details: docs/brain/NTA-ENGINE-POLICIES.md. (1) Options are served in a per-session order (seeded by the generation key and the question id) with the key, the A-D letters and explicit option references in the explanation remapped; the permutation rides on each row (nta_option_order) for the session's stored option layout; options that name other options, error-spotting parts and "No error" keep their order; stored letter prefixes are stripped first (data/option_text.js now also strips "A 36"). Offline on the 13 Oct export, paper 1 keys for Mathematics went from 37 A of 47 to 14/16/7/10, Physics 33 A of 50 to 11/14/14/11. (2) A blocking flag from either agent judge vetoes any source, factory included. (3) Non-UUID ids and seed or demo rows are never served. (4) Wording gate for the only-to-mainly corruption: catches all 34 held rows plus 12 more (ids for the owner's clean-up: tmp/nta-review-cleanup/CLEANUP-2026-10-13.md; no database write). (6) Concept guard without matching tags: rarity-weighted character 5-grams of the stem, the same short answer, and shared key concept phrases of either judge's tag; the stored objective tag is now the one both judges gave. (7) Difficulty: the stored label stands unless both judges put it two levels away (merge policy two_level_gap_only: 80 corrections, 1,267 one-level disagreements not applied). (8) Sequence and match keys in the listed order are kept out (63 live rows listed). (9) A student's next NTA paper leaves out earlier NTA papers' questions when the pool allows, otherwise falls back with the reason in structure.crossPaper; the production run script builds papers 2 and 3 that way. Refusals are worked out with a fixed seed so a retry reads the same sentence. Re-ran scripts/nta-pass-merge.mjs on the completed re-judge (618 result files, 0 missing, 0 invalid; 5,326 judged, 384 key disputes). Tests (HEAD plus these changes only, in an isolated copy, because the CUET-fit work was in progress in the shared tree): nta 122, nta-e2e 481, recovery 40, all pass. Not run: the production engine run (the orchestrator runs it). Offline on the export, paper 2 still repeats paper 1 for General Test (35 of 50) and Mathematics (20 of 47) because their pools cannot fill a paper without them; finding 5 (chapters) is the CUET-fit work.

## 13 October 2026 — NTA mode final end-to-end pass over all 15 subjects, three runner fixes (branch fix/nta-mode, not deployed)

Ran every suite on the merged branch: nta 95, nta-e2e 465 (as-is and promoted, 15 subjects each, one new per-subject step), recovery 39, answer-integrity 11, auth 33, du 19, learning 91, factory 332 all pass; study 21 of 22 (WordNet licence file absent, unrelated, as before). The production read (scripts/nta-engine-run.mjs) was not run. Browser drive: the site ran locally against the staging project (copy of stagingLocalApp.mjs on port 3107) with the dev-only page /preview/arena/nta and the local session backend (promoted mode); signed-in staging sessions are not possible for an agent. Every subject at 375 px and 1366 px, MockMob and NTA-style interface, light and dark: served subjects pass 23 of 23 runner checks (palette states, Save & next, Mark for review, Clear response, keyboard, Previous disabled on Q1), bulk answering of the whole paper matches the palette, submission scores exactly +5/-1/0 against the stored key, no horizontal scroll, no text under 4.5:1 in either theme. Passage text (a real 2,682 character English passage injected for layout) is visible at 375 px and 1366 px, contrast 8.6 light and 10.3 dark. Reload resumes answers, marks, current question and the running clock; the 15-second clock auto-submits and scores; an offline submit keeps the paper and the retry scores once.

Fixed: (1) live questions store each option with its own letter ("A  7/2", "B. Planning", "C) A-2, B-1"; 5 to 30 per subject, 14 of 15 subjects) so the runner and the result review showed the letter twice; data/option_text.js strips the marker for display only when every option carries its own letter in order, scoring and keys use the index. (2) NTA-style timer was 4.4:1 and the Marked palette chip 2.47:1 in both themes; darker timer backing and chip highlight. (3) the e2e driver compares option text through the same rule.

Not fixed (larger): (Superseded by the 13 Oct r4.1 entry above: marks are saved with a durable session and the device-ticket clock is kept by a signed start receipt, with the limits listed there.) 15 old seed questions (g1-g3, a1-a3, b1-b3, e1-e3, m1-m3) are live with source PYQ; as shipped (production scores plus the agent tables) NTA mode starts for General Test, Accountancy, Business Studies, Economics, Mathematics and Physics only; English (no passage sets) and Chemistry, Biology, History, Political Science, Geography, Psychology, Sociology, Computer Science refuse cleanly (too few fitting questions, 37 to 43 of 50 in the promoted run).

## 13 October 2026 — NTA mode end-to-end tests for all 15 subjects, three runner fixes (branch fix/nta-mode, not deployed)

New `npm run test:nta-e2e` (data/tests/nta_e2e_session.test.mjs, 390 checks, all pass) runs the real /api/sessions and /api/attempts handlers, practiceSessions, data/db.js, the pool read and the engine in plain Node over read-only production fixtures (`node --use-system-ca scripts/nta-fixture-export.mjs` writes tmp/nta-fixtures; select only, never committed). Only the Supabase client (in-memory, strict about selected columns and missing tables) and sign-in are stand-ins. Two data modes per subject: as-is (production scores) and promoted (synthetic signed scores where production has none, to exercise the session path; says nothing about quality). Per subject it checks the paper (45-50 unique live questions, four A-D options, key never sent to the browser, sealed snapshot key equals the bank key, passage sets whole), the 60-minute timer, replay, free student 402, difficulty override refused, variants, tampered or foreign ticket refused, submit scoring +5/-1/0 with exact counts and per-question verdicts, attempt and progress stored once, double submit, time-up (61 minutes in is scored, 63 refused), durable sessions (events, resume by key and by id, no timer restart, late answers not counted), and refusals (clean 422, sentence for the student, no session, no write, no charge). The real runner was driven in the built-in browser through a dev-only page, /preview/arena/nta, that sends only the two session endpoints to a local backend (data/tests/nta_e2e_server.mjs) running the same handlers; driver data/tests/nta_e2e_driver.js. Desktop 1366, tablet 768 and phone 375, both themes, NTA-style and MockMob interfaces: palette states, Save & next, Mark for review, Clear response, keyboard, reload resume, integrity strikes, time-up auto submit, offline submit and retry, whole-paper answer mapping checked against the stored key.

Result: as-is, Accountancy, Business Studies and Economics start and pass everything; English and the 11 unscored subjects refuse cleanly. Promoted, the session path passes for General Test, Accountancy, Business Studies, Economics, Mathematics (both variants), Physics, History, Political Science and Sociology; English, Chemistry, Biology, Geography, Psychology and Computer Science still refuse even with every live question scored 8 or more (no 200-300 word passages for English; 40-43 of 50 placed elsewhere because the bank has no match-the-following, sequence or statement items that fit; 15-34 questions per subject are typed as match-the-following but their options are not pairings). Scoring alone will not unlock those six; new questions of those types will.

Fixed in the runner (src/app/(app)/test/TestPageClient.jsx): a durable session resumed from the server restored a cleared answer as answered and showed every visited question as not visited; a free student starting NTA mode saw the raw code PREMIUM_REQUIRED; the "differs from the real paper" notice was open on phones and pushed the first question below the fold (now open only from 1024 px). Not fixed here (see the r4.1 entry for what later changed): the device-ticket clock and Mark for review gaps; 15 old seed questions (ids g1-g3, a1-a3, b1-b3, e1-e3, m1-m3) are live in production with source "PYQ 2023/2022/2024".

## 13 October 2026 — NTA agent pass: merge and engine source, r3 (branch fix/nta-mode, not deployed)

Agent scores are now a recorded third score source (agent_scored) next to factory evidence and the signed index. scripts/nta-pass-merge.mjs (offline, no database, no model) merges the two judges' result files from tmp/nta-pass/results into data/nta_agent_scores/<subject>.json with provenance: rubric version (nta-agent-rubric-1) and rubric hash, each judge's model and date, both scores, both blind answers, key agreement, flags, notes, objective tags, difficulty checks and per-subject agreement measures (mean absolute difference, within 1, Pearson r, key and tag agreement). Questions where either judge's blind answer differs from the key go to data/nta_key_disputes.json and are kept out of NTA mode whatever their source; objective tags go to data/nta_objectives.json (agent_questions; hand tags win); difficulty corrections where both judges agree go to data/nta_difficulty.json. data/nta_agent_scores.js checks provenance in code: the table must be calibrated (threshold mapping the owner's 8), the rubric version current, two different judges with model and date, both at or above the threshold, both blind answers on the key, no blocking flag, and the row's content hash unchanged; factory evidence always wins and is never rescued by an agent score. The pool loader adds only agent ids that already pass those checks, without the evidence column and only where the question has no factory evidence. scripts/nta-pass-export.mjs now also writes hashes.json (the content hash the engine computes). State: tmp/nta-pass does not exist (the export has not been run), 0 result files, 0 missing, calibration pending, so the agent source admits nothing and the read-only production run (docs/brain/NTA-ENGINE-RUN.md, engine r3) equals the factory-only run: Accountancy, Business Studies and Economics serve closest valid papers of 50 (3 of 3 starts), English refused (no passage sets), the other 11 subjects refused (no scored questions); 0 key disputes. Tests: nta 93 (6 new), recovery 39, answer-integrity 11, auth 33, du 19, learning 91, factory 332; study 21/22 (WordNet licence file absent, unrelated, as before); eslint clean on the changed files; webpack build passes. Next: run the export, the calibration judges and the comparison, write tmp/nta-pass/calibration.json, run the judges, merge, re-run the engine.

## 13 October 2026 — NTA engine review fixes, r2 (branch fix/nta-mode, not deployed)

Applied the CUET paper-setter review of 053d2a0 (no subject was ready: the same concept repeated in a paper, items that give their answer away, one broken item, one likely wrong key). New data/nta_item_checks.js. Structural gate: sequence options must order the stem's own items, match options must use List-I and List-II labels the stem shows, statement options must use its statement labels, and no item may print its options again inside the stem. Wording gate: stems that state the rule ("For this question...", "Use this rule", "terms defined here", "in the supplied sense"), cite "the stated condition" or "the excerpt", point at options ("options B-D"), narrate the order a sequence asks for, or order a book's modules; explanations that cite "the excerpt" or "the stem". NTA-only, reversible quarantine (data/nta_quarantine.json): Accountancy 40d8ffd9... (key pays capital in capital ratio; by the realisation-loss rule P gets Rs 1,65,000, no option) and Business Studies 24ff7d61... (sequence with match options). Same question in other words: stem + options or stem + key text at Jaccard 0.5, same chapter and concept-name overlap 0.5, same chapter and shared figures, English shared headword (quoted target, one-word key, short match entries), passage children with the same answer; passage children are no longer exempt. Learning-objective tags (data/nta_objectives.json, or nta_question_index.objective_tag) cap each objective at one per paper; only the 38 questions in the review's named clusters are tagged. Type counter: statement-based needs labelled statements and label-combination options (Both/Neither wording is a plain MCQ; roman and lower-case labels count). English passages must be 200-300 words with at least 4 distinct children. Numerical share follows the blueprint overlay (Accountancy at most 17, Economics at most 15). Scores fail closed: both judges and both blind solvers are required, and the unsigned quality_score column never admits a question. Pool read: supabase/migrations/20261013190000_nta_question_index.sql (saved, not applied) and scripts/nta-index-build.mjs (dry run by default) give signed slim index rows; the runtime reads them plus questions without evidence (0.27-0.36 MB instead of 5.3-6.6 MB), re-checks signature and content hash, falls back to the full read while the table is missing, and caches each subject's pool for 5 minutes. A spent read budget now returns a student sentence; a missing shortfall table costs one failed insert per process; the engine says "General Test".

Read-only production run (docs/brain/NTA-ENGINE-RUN.md): the review gates keep out English 11 of 149, Accountancy 20 of 127, Business Studies 26 of 145, Economics 20 of 130 questions at the bar. Accountancy, Business Studies and Economics serve closest valid papers of 50 (Accountancy now differs in chapter weightage; Business Studies and Economics have Q41-50 standalone); English is refused (no passage of 200-300 words; at 7.5 also refused); the other 11 subjects are refused (no scored questions). End to end 0.95-2.6 s cold, 0.39-0.47 s from the pool cache; assembly 11-57 ms. Five fresh papers per serving subject: 0 pairs at stem+options Jaccard 0.5, 0 repeated tags. Not fixed (owner decisions): concept tags for every eligible question, a signed per-item review record (hedges, trivial arithmetic labelled hard, difficulty), case sets for commerce subjects, English passages of 200-300 words and sentence-part rearrangement and idiom items, scoring the 11 unscored subjects, the dashboard variant picker (Applied Mathematics) and showing availability before Start. Tests: nta 87 (11 new), recovery 39, answer-integrity 11, auth 33, learning 91, mock selector and session recovery 9; webpack build passes. Deployment gates: both NTA migrations saved, not applied; the index build has not been run with --write anywhere.

## 13 October 2026 — NTA paper engine: score bar plus CUET blueprints (branch fix/nta-mode, not deployed)

NTA mode now starts from data/nta_engine.js instead of the evidence-certified pool. Eligibility: a score of NTA_MIN_SCORE (8) or more out of 10, read as the mean of the two factory judge scores in the signed evidence record (or quality_score x 10 if that column is ever filled), plus hard gates: the score record must be signed, name this question, match its current content hash and have both blind solvers on the stored key; answer-key guard; content gate; live and undeleted; no open key dispute; no family hold; chapter in the 2026 syllabus. Evidence expiry, source registry and calibration state no longer gate NTA, so the 5-6 November expiry does not empty it. Assembly follows data/nta_blueprints: section order, per-type quotas, whole passage or case sets at the blueprint's place, unit and chapter ranges, difficulty mix, no repeated family or near-duplicate stem, unseen questions first. A bank that cannot meet the blueprint gives either the closest valid paper (at least 45 questions) with the differences in plain sentences, or a refusal with the reason and a Full Mock suggestion; both are logged and, once supabase/migrations/20261013170000_nta_paper_shortfalls.sql is applied, stored for the content team. Read-only production run (docs/brain/NTA-ENGINE-RUN.md): Accountancy exact; Business Studies and Economics 50 questions with Q41-50 standalone because the bank has no case sets; English refused (1 complete passage set at the bar, 2 needed; at 7.5 it would serve); the other 11 subjects refused (no scored questions). End to end 0.9-3.4 s per paper, assembly 5-61 ms. Tests: nta 76 (29 new engine tests), recovery 39, answer-integrity 11, auth 33, learning 91, du 19, selector/session 22; study 21/22 (the WordNet licence file is absent in this worktree, unrelated); webpack build passes. Deployment gates: the shortfall migration is saved, not applied; the notice UI was not checked in a browser.

## 13 October 2026 — NTA mode paper pattern, NTA-style passage text, NTA mode on phones (branch fix/nta-mode, not deployed)

Root cause of the "passages and passages" English paper: the NTA selector (data/nta_question_selector.js, since 7dd32c3) had no paper pattern. It took every passage set in each quality tier before any standalone question and put them first. Since 0d961f1 (7 Oct) NTA reads only the evidence-certified pool, where English has 35 passage questions in 13 small sets, so a read-only rebuild from production gave questions 1 to 32 as passages. Commits e2a9dab and 52de7fe did not change eligibility. New data/nta_paper_pattern.js lays out each paper: English has 2 to 4 whole passage sets of at least 3 questions (8 to 20 questions), with the rest split across vocabulary, correct word usage, para jumbles and match the following (12/9/7/7, each capped at 1.5 times its share). Verbal blocks and passage sets alternate and the paper opens with vocabulary. Domain subjects go round-robin across syllabus chapters and follow syllabus order. A short bank gives fewer than 50 questions with a stated reason, so the session does not start; the paper is never padded with one question type. Production rebuild (read-only): English has 50 questions, 4 sets (15 questions), longest passage run 5. Accountancy, Business Studies and Economics have 50 each. The other 11 subjects have 0 evidence-certified questions, so NTA mode cannot start for them (unchanged since 0d961f1; changing that is an owner decision). NTA-style skin: it had pinned the dark-theme ink tokens on its light surface, which made passage text, the warnings pill, alerts and the palette close icon invisible. They are now dark ink in both themes. Below 1024 px, a fixed bar keeps Back, Clear response, Palette, Mark for review & next and Save & next on screen; the timer stays in the sticky header and the palette opens as a bottom sheet. Tests: nta 29, recovery 39, auth 33, answer-integrity 11, mock selector/ui/session 14; webpack build passes.

## 13 October 2026 — app backend release branch (release/app-backend), not deployed

Branch release/app-backend is origin/main (5f7d53e, sign-in reliability and inventory snapshot kept) plus only the backend the Android app (in.mockmob.app) calls, taken from feat/app-and-web f4451cd: /api/me/{consent,notification-prefs,devices,goal,rhythm,bests,repair-record,sample-import,delete}, /api/events, /api/attempts/summary, /api/sessions/[id]/check (off unless SESSION_CHECK_ENABLED=1), /api/assetlinks with the /.well-known/assetlinks.json rewrite, /api/internal/finalise-sessions with a daily cron, bearer auth on bookmarks, ai/credits, ai/usage, ai/mentor/history, learning/summary and the questions feed/vote/interact/explore routes, structured action fields (plan, quote, replay, repair), the result recap block, the server modules, data/db.js mode and formatId, 7 migrations, tests, the deletion processor script, and the Play-required /account-deletion page, privacy update and Profile usage-data and delete controls. Homepage, /app, landing, result QR and security headers were left out.

New here: the deadline finaliser never touches sessions that expired before 2026-10-13 00:00 UTC (SESSION_FINALISE_FROM overrides), so deploying it is not an implicit backfill; migration 20261013170000_app_service_role_grants.sql states the service-role grants the usage tables relied on from Supabase defaults; scripts/dev/production-app-sql.mjs builds ../PRODUCTION-app-backend-2026-10-13.sql (one transaction, preflight, idempotent, verification last) and dry-runs it.

Verified locally: test:recovery 39/39, test:auth 50/50, test:app 107/107 (plus app_bearer_routes in test:auth), test:learning 91/91; test:study 21/22 with the same content-gate failure on unchanged origin/main; next build --webpack passes. PGlite: the bundle applies on the replayable production history with and without the inventory snapshot table, applies a second time unchanged, 17/17 verification rows ok; the preflight stops it on a database without the recovery tables and nothing is created. Staging read-only check: every table, function and users.deleted_at present.

Deployment gates (owner): run PRODUCTION-app-backend-2026-10-13.sql in the production SQL editor first, then push release/app-backend to main; set ANDROID_CERT_SHA256 (Play App Signing and upload key SHA-256) in Vercel; CRON_SECRET must be set for both crons. Account deletions are fulfilled only when an operator runs scripts/ops/process-account-deletions.mjs within 30 days. 20261013150000_auth_unconfirmed_passwords.sql is still not applied anywhere and is not in this bundle.

## 7 October 2026, 14:22 UTC — 575 verified production retrievals and current accounting

Owner-corrected signing configuration redeployed as GnJ42mkLjHXgbwUs4SvPY6oSWgpD (c235606), Ready/Latest in 77 seconds. The actual production student check passed at 14:12:38: 575/575 unique new approved questions retrieved, ten complete passage groups, zero rejected IDs, unchanged USD 25 student-AI monthly cap. The authenticated rendered dashboard confirms 575 usable / 579 historical publication records, four withheld, and after a metadata-only accounting refresh shows USD 12.82 settled + USD 0.28 held and a USD 92.76 conditional lifetime forecast. That refresh preserves paused=true, phase=1000 and publication_enabled=false, and changes no questions, payments or student budgets; its receipts are in production-accounting-sync.json/.jsonl. Export refreshes now maintain this snapshot when production publication was explicitly authorized.

The retained ledger at 14:22:16 is USD 12.824160 settled + USD 0.276446 held = USD 13.100606 committed, 7,146 requests. Sixteen accepted candidates remain submitted; five historical/terminal-failure requests remain unresolved and retain their USD 0.090248 maximum holds. Provider invoices remain unavailable. Eight completed cohorts retain 800 candidates, 575 usable approvals and USD 4.860017 gross; the current author contract's three complete cohorts retain 300 candidates, 250 approvals and USD 2.108597 gross. Current overall craft distribution remains 233 seven, 341 eight, one nine, zero ten; this is a mixed bank, not a uniformly premium or perfect bank.

Stricter craft-filter scenarios retain all 800 completed candidates and their USD 4.860017 gross costs. Overall scores of at least eight select 342 questions, USD 0.014211 per selected question and a conditional lifetime 10,000 cost of USD 150.346349. Requiring an overall score of at least eight plus every individual craft subscore of at least seven selects 160, USD 0.030375 per selected question and USD 311.991652 conditional lifetime cost. These are observed rating filters, not accuracy or premium-quality proof. The mixed-bank USD 92.762624 forecast cannot substantiate a uniformly premium bank under USD 100. The automated report includes these distinctions and preserves all rejected and failed-call costs.

Staging repeated statement timeouts (57014) on large status upserts and snapshot reads. Sync writes now use byte-bounded chunks while preserving every evidence byte; full snapshot reads keep their usual pagination and retry a timed-out evidence-heavy page once at 100 rows with the same offset. Metadata errors and further failures still fail closed. Four targeted byte/boundary/error tests pass; full factory/snapshot tests 335, recovery 39, question/payment/wallet/ticket 65 pass, with the earlier application-learning 84 retained as dated evidence. Controller 59386 resumed the same accepted campaigns; no new cohort or paid evaluation was registered. Paid IDs, reservations and evidence gates remain intact. Production availability is established; the combined 1,000-candidate campaign is still incomplete while the last 16 provider candidates finish.

## 7 October 2026, 13:31 UTC — production signing key and request-scoped evidence checks

The owner saved CUET_EVIDENCE_SIGNING_KEY as a Vercel Production Secret. Redeployment 2S7jeLumVt3bf59yBrJ5JTUmmUXs of e9e1ffb is Ready (53 seconds). Public endpoints return 200; anonymous admin returns 401. The authenticated overview timed out at 30 and 90 seconds and remains unverified. It was reparsing approximately 4.85 MB of registry/calibration JSON per inventory row (9,821 production rows). The overview now binds one fresh registry/calibration snapshot per request; item signatures, content hashes, source versions, expiry, disputes and release predicates are still independently evaluated, with no cached item verdict. Real 575 approved records remain eligible in 0.297 seconds locally; sampled existing-path verdicts match. Factory plus snapshot safety tests pass 331, recovery 39, question/payment/wallet/ticket 65; the release build passes. Production retrieval is to be rerun after this optimization deploys. Native provider IDs, remaining 19 candidates, all costs/holds and the running controller remain intact. No new paid evaluations, production migrations or payment changes.

## 7 October 2026, 12:52 UTC — native Gemini failure receipts preserve holds without publication deadlock

The accepted 64-item Gemini validation batch succeeded at the provider level; 60 usage receipts settled and four item records reported native code 14, service unavailable, with no usage. The four $0.019788 reservations remain fully committed ($0.079152 total), and all four corresponding candidates are quarantined. The transport now retains each exact native metadata key, batch identity, terminal state and error record. Cohort accounting recognizes only matching terminal failures on quarantined items as bounded receipt holds, so unrelated approved questions can publish once their pending work finishes. A failed call with reported usage is charged for its candidate plus reasoning tokens; no service failure is assumed free. Missing/duplicate identities, a running batch, missing failure evidence, invalid bounds or an approved failed item still block publication.

The fix passed 28 targeted receipt/restart/identity/budget/publication tests, all 328 factory tests and the full release build. It was applied atomically after preserving the old files; the existing controller and active paid calls were left running. Actual SQLite proof at 12:51:38 UTC verifies all four native keys, terminal errors, unchanged full holds and quarantined item states. The academic generation/validation contract is unchanged; no repeated paid evaluation or accepted-ID resubmission was introduced. Two OpenAI batches and later repair-validation work remain pending; the controller must finish them before the combined campaign is called complete. Production signing-key entry and the historical 503 receipt remain external dependencies.

## 7 October 2026, 12:22 UTC — 575 actual staging retrievals and deployed currency correction

The signed-in staging student check at 12:15:53 UTC retrieved all 575 current approved questions: English 149, Accountancy 123, Business Studies 159 and Economics 144. Ten passage groups were complete; no rejected item was retrieved. The authenticated admin overview distinguishes 579 retained publication records from 575 currently usable factory items. Funded checkpoint replay, the unfunded 10,000 checkpoint rejection and the existing $25 student-AI monthly cap passed. This is actual API evidence; it does not replace a current rendered dashboard inspection.

The serving guard now preserves the sign in grouped rupee amounts, including Indian grouping, while rejecting mathematically equal options such as ₹3,00,000 and ₹300000. This corrected a false positive on one independently validated Economics item without changing its key, explanation or academic evidence. Fractional signed scalars are also covered. Question/selector/payment/wallet/ticket checks pass 65, factory 324, recovery 39 and the release build passes. Vercel shows production commit 4a9c002e7ce957d78715c409f0ec45f7d5ce3cca Ready/Latest, deployment Fr8c2aHmfwxtzqjXF1inXovKTdSm, 57 seconds. The frozen academic contract remains byte-identical to the release checkout: d80135b0271f350a1864c9d107b078f07fbefa54419c4615a8891aa096308399.

The existing controller was restarted only after two independent child-empty checks to reload the guard. Restart evidence retains all 7,047 prior ledger requests and 2,438 stored accepted provider IDs, with zero missing IDs and no replay calls. The resumed controller reports 575 usable items and 83 pending candidates in the two already registered later cohorts; no further cohort was registered. Eight complete fixed cohorts preserve their entire 800-candidate denominator, 575 approvals and $4.860017 gross cost. At the dated 12:15:30 snapshot, lifetime settled usage is $12.521966, holds $1.378190, committed $13.900156; the conditional lifetime 10,000 forecast is $93.562174 across all completed cohorts and $93.394263 for all completed current-author-contract cohorts. Neither a uniformly premium bank nor a $50–70 forecast is established. These are usage receipts and conservative holds, not provider invoices.

Additional application/learning verification completed at 12:32 UTC: 84/84 existing tests pass. They exercise the production-shaped monthly AI budget migrations, conservative missing-usage accounting, duplicate dispatch suppression, credit reserve/commit/refund lifecycle and historical payment-plan resolution. These are local database and application checks, not a captured production payment or live student-provider claim. The report retains exact commands, test counts and log hashes in continuation-500/local-verification.json and includes them automatically in future exports.

Production student availability remains unverified while the owner-controlled CUET_EVIDENCE_SIGNING_KEY form awaits entry and submission; storage receipts and a Ready deployment do not establish availability. The browser credential rule requires the owner to complete that step. The historical OpenAI 503 request remains conservatively held at $0.011096; the read-only billing lookup encountered an authentication failure, and no zero-cost assumption or resubmission was made. The accepted native batches remain under the persistent controller for completion, export and final retrieval checks.

## 7 October 2026, 10:15 UTC — current usable admin counts and lifetime forecast

The actual staging check at 10:12:30 UTC passes 491/491 current approved questions, ten complete passage groups, and zero rejected items retrieved. The authenticated overview now separates 495 retained publication records from 491 currently usable factory questions. All four withheld historical publications remain stored and unavailable. The admin headline, subject counters and checkpoint gates use the intersection of current usable coverage with new factory publication IDs; unrelated legacy inventory cannot fill these checkpoints. The lifetime forecast includes existing committed spending and conservative holds once, rather than showing only marginal cost for 10k.

Four targeted count/forecast tests cover retained withholding, legacy exclusion, an insufficient 999-usable/1000-historical checkpoint, and absent cost evidence. Factory passes 324; the full release build passes. Recovery 39 and scoped question/payment/wallet/ticket 64 remain passing. At the dated aggregate snapshot 10:06:44 UTC, seven completed cohorts retain all 700 candidates, with 491 usable approvals and $4.128471 gross. Lifetime settled is $11.398041 and conservative reservations $0.782782, committed $12.180823. Conditional lifetime 10k is $92.135264 across all completed cohorts; uniform premium quality and a $50–70 fit are not established.

The accepted native batches are still processing (99/100, 98/100 and 0/7 in the latest direct read). Their output files are not available yet, so partial provider counters cannot be collected as completed questions or settled receipts. All accepted IDs remain retained; no paid regeneration or accepted-request resubmission was introduced. Production signing-key entry and the historical 503 billing receipt remain precise external dependencies.

## 7 October 2026, 10:04 UTC — unsupported antonym explanation withheld

The actual supplied dictionary span does not entail the generated rule that an antonym 'must oppose both qualities'. Both independent model checks and the explanation audit passed that unsupported claim. The publication inspection now rejects it automatically, and the already published item abb793b3de99185acb169170f420b335 has been withheld in both authorized environments with content, provider costs and prior publication history retained. This is an observed validator miss and dated regression evidence; it is not a fresh benchmark success or proof of general accuracy. The three duplicate passage children remain withheld. Cohort 007 now has 78 approvals and 22 rejections, preserving its full 100-candidate denominator and $0.681212 settled gross cost.

Inspection contract evidence-content-idea-inspection-v3 binds publication reuse to these current guards and unchanged content. The frozen academic model contract remains d80135b0271f350a1864c9d107b078f07fbefa54419c4615a8891aa096308399. Factory passes 320 tests; recovery 39 and scoped answer/selector/payment/wallet/ticket checks 64 remain passing. Actual staging retrieval passed 492/492 at 09:55 before this additional withholding, so that proof is dated; the updated usable count must exclude this item. Remaining native requests are retained, and no fresh paid benchmark or uncontrolled regeneration was run.

## 7 October 2026, 09:50 UTC — actual novelty withholding and serving guard corrections

Vercel reports production 224e63a1ad3928f592f945d88be1b3ae351a7510 Ready (53 seconds). The retained seven completed cohorts originally approved 495 candidates. A new automatic passage-fact check found three children of the same passage group asking the same factual condition, despite differing concept labels. All three are now withheld in staging and approved production through retained dispute receipts; no content, publication receipt or spending record was erased. The local cohort retains the former publication history and now reports 79 approvals and 21 rejections. The strengthened prepublication check also withholds every sibling if a duplicate child fails. Numeric quantities, negations, different passages and genuinely distinct facts remain distinct in regression tests.

Two serving false positives were found from actual inventory: the guard collapsed +3.75 and -3.75, and treated vocabulary definitions containing 'true' as answer verdicts. Signed scalars now preserve value/sign, equivalent scalar options still collide, and truth assertions require an actual verdict. Independent key, support and explanation validation remain unchanged. The frozen academic contract is unaffected; no fresh paid benchmark was purchased.

Factory passes 319, recovery 39, and the scoped answer/selector/payment/wallet/ticket checks pass 64. The controller was stopped only after two child-empty checks, preserving accepted provider jobs; it resumed with the same persistent ledger. Remaining accepted cohorts 008–010 are still processing. The current count and lifetime figures are in artifacts/question-factory/continuation-500/REPORT.md; neither pending work nor historical duplicate publications count as delivery. Production student availability still needs the owner to save the prepared signing secret; OpenAI billing login returned an authentication error, and its historical 503 maximum reservation remains fully counted.

## 7 October 2026, 09:05 UTC — content-bound retrieval and automatic final evidence

The stronger real staging check passes 413/413 approved items across all four subjects, verifies actual passage-group IDs and nine complete groups, and finds no rejected questions in retrieval or storage. Its proof binds the complete exported content/evidence hash and the unchanged academic validation contract d80135b0271f350a1864c9d107b078f07fbefa54419c4615a8891aa096308399. Anonymous/student admin denial, cross-origin rejection, funded checkpoint replay, unfunded 10k denial and the preserved $25 monthly student AI cap also pass. No paid model calls, emails or production data writes occur in these checks.

The final export now refreshes REPORT.md automatically. Once every registered candidate and accepted provider processing stage is terminal and the actual usable bank reaches 500, it runs one real staging retrieval and, under the existing production authorization, one real production retrieval. Attempts are persisted before dispatch; content, evidence, academic verification contract and retrieval-script content bind reuse. Interrupted/failed checks remain explicit rather than being presented as completion. After an external configuration fix, --refresh-final-evidence rechecks without generation or paid evaluations. This lets the persistent worker finish reviewable evidence if chat usage ends while native results are still pending.

The factory suite passes 317 tests. Recovery passes 39 and question/payment/ticket checks pass 67. Production submission fix 2e50d71 remains Ready; new production factory retrieval still needs owner submission of the prepared signing key. The fixed 1000-candidate campaign remains incomplete and its pending native requests are retained, not resubmitted or counted as delivered.

## 7 October 2026, 08:38 UTC — deployed submission fix and safe campaign restart

Production 2e50d719cf86e83dc6fc8fbab5fcfaef5f45f8a8 is Ready/Latest (50-second cloud build), verified on its exact Vercel overview. The expanded recovery command passes 39 tests. Actual full mocks for all four subjects and English quick practice pass the separate-staging launch/submission/replay check; every selected item is in the new approved bank.

The controller was restarted only after two inspections confirmed no active worker child. Its old process ended; no worker child or provider job was terminated. Actual restart evidence retains all 293 previous accepted provider IDs, zero missing IDs and all 6079 ledger requests. The resumed controller reports the current 413 usable questions rather than the old module's conservative undercount of 410. Accepted request IDs were not resubmitted.

Pending-capacity scheduling now waits for already accepted candidates or settled approvals that can fill the target before buying another cohort. This potential is an upper bound, not promised yield. Terminal receipt-only holds contribute no fictitious delivery capacity and remain fully committed; bounded unrelated work remains permitted. The new scheduling cases and existing budget/concurrency/recovery checks pass (17 targeted tests). The export report binds its coverage snapshot to its own inventory measurement so an older running controller cannot overwrite the report's count or topic contract.

The live campaign remains unfinished: six completed fixed cohorts, 600 candidates, 413 unique published questions; cohort 007 has 78 approvals, 17 rejected and five accepted requests pending, and cohorts 008–010 still await accepted authoring results. At 08:25:58 UTC, lifetime receipt-settled usage is $10.680328 and conservative holds $1.139486, committed $11.819814 under $50. Production student retrieval still requires owner entry/submission of the prepared signing key; provider invoices and the historical 503 usage remain unresolved. None of the queued work is counted as completed delivery.

## 7 October 2026, 08:20 UTC — actual full-paper submission repaired and verified

Production commit 66aef5f is Ready (50-second cloud build), including source families through fixed cohort 010. This does not establish new factory student retrieval: owner submission of the prepared Production CUET_EVIDENCE_SIGNING_KEY remains pending.

Actual separate-staging API launches exposed a real issue: 50 selected factory questions carried sufficient verification records to make the encrypted device-held session ticket exceed the 600k submission limit. New p2 tickets compress the complete server snapshot before AES-GCM encryption, retain an 8 MiB decompression bound and the existing 500k ticket ceiling, and keep valid p1 tickets readable. No academic evidence, keys, source records or historical receipts were dropped. Sealing still precedes charging; oversized sets fail before spend.

The corrected live staging check passed English quick practice and all four 50-question/60-minute full mocks, actual approved-question selection, four options, passage delivery, hidden timed-session keys, free replay and idempotent submissions. Synthetic unanswered attempts score zero; these are test records, not learner-gain or fresh academic reliability evidence. Failed initial checks remain in practice-launch-checks.json. The existing disposable student received a separately recorded 160-credit non-monetary staging fixture; production balances, entitlements, payment receipts and AI budgets remain untouched.

Verification: 35 existing recovery checks and 67 question/payment/ticket checks passed; the four new ticket checks cover exact large-snapshot recovery, legacy readability, authentication/tampering/ownership/expiry, and decompression limits. The complete release build passes. The new ticket suite is now included in test:recovery. Accepted generation requests continue under their original IDs; the 500 delivery target and final accounting remain unfinished.

# Implementation status — latest update: 7 October 2026

## 7 October 2026 — owner-approved production release and cost optimization (ongoing)

- Update 07:57 UTC: six completed fixed cohorts retain all 600 candidates: 413 approved, 187 withheld, gross cohort cost $3.447259. Actual signed-in staging retrieval at 07:51 verifies all 413 exact records (English 111, Accountancy 86, Business Studies 111, Economics 105), nine complete passage groups and zero rejected items. All 413 have production atomic storage receipts; new production student retrieval still needs the owner signing-key entry. The original fixed 100 remains 50 approved/50 rejected/$0.515798, not substituted by continuation yields.
- Release 9085d02849756710323abf3e702c633b4608dfcf is visibly Ready/Latest on www.mockmob.in after a same-commit clean rebuild (70 seconds). Initial Vercel restored-cache build failed in Turbopack Google-font module resolution; the uncached rebuild passed. Actual production feed preserves existing library access in all four subjects. Factory 315/315, recovery 35/35, question/payment 63/63 and production build pass; frozen academic contract remains d80135b0271f350a1864c9d107b078f07fbefa54419c4615a8891aa096308399.
- A repeated authenticated staging check hit the 30-second request timeout because controls downloaded/classified the full bank twice. Controls now retain the first inventory's explicit counts_snapshot_at, apply the same funding/evidence gates, then re-read actual database controls without a second whole-bank download. Live authenticated release/replay and all-413 retrieval pass, as do the subsequent build and recovery checks. No correctness gate or paid-model stage was removed.
- The local helper's IPv4-only binding did not match this host's localhost (::1) resolution. Helpers now bind only to localhost and the direct localhost health check returns 200. Existing browser error pages are additionally blocked by Browser Use's data-URL policy; no raw browser/security workaround was used. Current rendered admin recapture needs that browser page restored; earlier actual admin/student screenshots remain dated evidence.
- Cohorts 007–010 retain accepted IDs and fixed 100-candidate denominators. Pending authoring and independent batch checks are provider work, not completed questions. The live exclusive guarded controller continues; the $50 content cap and $25/IST-month student cap remain intact. Current exports and dated lifetime reservations/forecasts are in continuation-500/REPORT.md; no global settled-cost or invoice claim while the saved historical 503 remains held.

- Update 07:40 UTC: original fixed 100 and continuation cohorts 002–006 are academically complete (600 candidates; 413 approved, 187 withheld), with completed-cohort gross cost $3.447259. Publication of cohort 003 is still progressing; dated actual counts and receipts are in `artifacts/question-factory/continuation-500/REPORT.md`. Cohorts 007–009 retain their fixed denominators and accepted provider IDs; queued candidates are not counted as usable delivery.
- Actual signed-in staging retrieval at 07:27 verifies all then-published 253 exact keys/options/explanations, six complete passage groups and zero rejected items. Monthly student AI cap remains $25. Latest deployed commit fc060f2 is visibly Ready/Latest in Production (43-second Vercel build). New factory production student availability still requires the owner signing-key entry and current family registry deployment.
- Fixed a deterministic answer-guard false positive: the ordinary dictionary definition “understood in more than one way” was wrongly treated as a combined-answer choice. Combined-answer options remain withheld; two regressions pass. Independently validated academic content and keys were unchanged. Recovery 35/35 and question/payment 63/63 pass after this correction.
- English coverage now separates exact numbered/lettered official syllabus phrases instead of treating the whole PDF as a single unfillable topic; independent tag disagreement remains unclassified. Five official-topic regression checks pass. Aggregate exports now disclose all completed cohort economics alongside the predeclared current-author-contract subset and lower independent craft ratings; no partial or favorable-cohort selection.
- The first v3 authoring cohort completed 88/100 approvals for $0.695839, with overall scores 28 at 7 and 60 at 8. These are sound-to-ordinary practice ratings, not uniform premium or accuracy guarantees. Actual committed lifetime snapshots include all outstanding reservations and the historical $0.011096 OpenAI 503 hold; no provider invoice or globally settled-cost claim.

- Update 06:00 UTC: two fixed 100-candidate cohorts are complete. Original: 50 approved/50 rejected/$0.515798; native cohort 002: 53 approved/47 rejected/$0.482092. All **103** newly approved items are published in staging and production database. Signed-in staging student retrieval verifies all 103 exact keys/options/explanations and two complete passage groups; no rejected item retrieved. Production student availability of new factory items still requires the pending owner signing-key entry; it is not counted as verified delivery.
- Production compatibility release **9bf60d0cf6e4faaf62ef12dfeae048d7fa90e6c7** is Ready (49-second Vercel build). Its actual public feed again returns existing library questions in all four subjects. Fixed a regression requiring screening receipts on every pre-existing row; existing holds and any failed/stale receipt still withhold a row, and modern factory evidence/provenance cannot use legacy compatibility. 313 factory, 35 recovery and 61 question/payment checks pass; production build passes.
- Atomic publication caught three individually approved children with differing chapter classifications in one registered passage. The publisher stopped correctly. Prepublication inspection now uses that same unchanged group contract and quarantines the entire affected group before RPCs. Three additional removals reduced native cohort 002 from 56 to 53; no forced repair, rewritten answer or score inflation.
- Cohort 004 authoring finished with 87 responses and 13 provider-confirmed invalid-schema failures: strict quote enums cannot contain newline characters. Failed requests remain in its denominator. New author contract v3 uses exact contiguous source spans without control characters. Existing accepted v2 bodies and idempotency keys are preserved byte for byte; no accepted ID is replaced. Regression tests cover both.
- At 05:59 UTC the actual lifetime ledger was $9.230111 committed, including pending validations and conservative holds. This is a dated snapshot, not a final cost or provider invoice. Cohorts 003–005 are still in progress. **500 registered candidates is not 500 approved questions.** The guarded worker continues toward 500 new usable publications; current-author-contract forecast remains unmeasured until complete cohorts exist. Content cap stays $50; student cap stays $25/IST month.


## Earlier release record (retained)

# Implementation status — latest update: 5 October 2026

## 5 October 2026 — Source-linked study expansion and journey fixes

Implemented in the isolated `artifacts/study-suite/release` checkout; the original dirty
checkout and its unfinished owner edits are preserved. Existing Android/offline work is
retained. See `STUDY-CONTENT-WORKFLOW.md` for inexpensive expansion and correction rules.

- Current manifest: 21 lessons / 86 cards / 221 task variants; partial lesson coverage
  in 15 of 54 chapters, up from 8. Seven new concept packets cover Planning, Staffing,
  Directing, Money & Banking, Government Budget, Share Capital and Accounting Ratios.
  The preceding 14 lessons and 65 cards retain their exact canonical content hashes.
- Source-linked authoring compiles teaching, contrasts, concept maps, original checks,
  recall and printable material once. Strict PDF/digest reconciliation, independent
  arithmetic and packet/key checks passed with no quarantine. Skipping PDF checks cannot
  publish; same-version mutations fail. No paid content generation ran.
- Saved SQL and PGlite receipts preceded current-project inserts. Read-only live plan
  matched all 79 preceding rows; insert verification matches all 107 current unit/card
  rows. Share-capital title narrowed to the three stages actually taught through an
  immutable v2 correction, not an overwrite. Superseded v1 withdrawal follows deployment.
  No question-bank, attempt, entitlement or balance changes were made by the importer.
- Recall introduces new cards only after teaching. Corrected sessions link to current
  lessons. Mixed revision navigates directly and lists learned concepts within the
  20-concept limit. Results show all matched lessons. Student controls use large selection
  tiles, explicit assistance choices, specific next actions and reduced-motion-safe reveals.
- Session validation reads only its bound lesson IDs, with current publication and canonical
  hash checks retained. Catalog growth no longer increases records transferred on every
  Continue/answer request. No latency or field-CWV improvement is claimed without measurement.
- Owner-authorised chapter summaries return reading blocks only, record teaching
  exposure and do not certify completion. Browser print/PDF action and print CSS included.
- Optional one-credit tutor uses only the current published lesson or already revealed
  feedback, validated against owner, version, revision and item before credit reservation.
  Existing $25/IST-month runtime guard and 10/50 Free/Pro allowances retained. One owner QA
  explanation completed: one credit committed, provider receipt $0.00032835. Content
  generation spend remains $0. Same-step saved explanations can replay without a second
  charge. Removed the obsolete Demo Login provider; server-validated Supabase auth retained.
- Fresh verification: recovery 35, learning 80, study 22, payment/answer-integrity/NTA/UI
  45 — 182 distinct tests, all passed without skips. Lint and production build passed.
  Sandbox build stalled; the normal-filesystem build completed, with no config workaround.
  Canonical source/content validation and isolated import/correction dry runs passed.
- Browser preview completed a new Planning lesson, two keyboard checks and the transition
  into three recall cards. Real signed-in run saved and resumed step 2 after reload;
  the tutor returned a correct policy/procedure/rule explanation. Server-backed chapter
  summary loaded in both themes. Comparison/summary at 320/390/768/1024/1440 and short
  landscape: no document overflow; inspected controls at least 44px. These are owner QA
  and viewport-emulation checks, not student outcomes or physical-device performance.

Evidence: `artifacts/study-suite/v3/` and `artifacts/study-suite/coverage.json`.
Published as `86accc3` on `origin/main`. Vercel production deployment
`63WAusDST9US1pFBq9ZEhMMb4W42` is Ready (39s build), created 5 October at 02:06:43 IST.
Live public/auth checks passed: home/Learn/summary shell 200, anonymous catalog/summary
API 401, dev preview 404, Google-only auth providers and apex-to-www 307. Signed-in live
Learn showed 21 lessons and the new chapter entries; Pro mixed revision opened its saved
five-card run directly. The owner's corrected old run now links to the current vocabulary
lesson. The new Planning run resumes across localhost/production with the same saved step.
Share-capital v1 was quarantined after deployment; all 107 current hashes still match.
Rollback keeps records: revert the release commit or disable the existing independent
study flags and redeploy; no deletes.
New rows are ignored by the preceding release manifest. Remaining: 39 chapters without
lessons, deeper coverage within the 15 touched chapters, real-device/offline-pack checks,
screen reader/200% zoom/OS reduced motion, actual print output, field CWV, delayed unseen
question outcomes and Supabase CLI migration-history reconciliation. No full-coverage,
mastery or superiority claim is authorized by this source/self-study gate.

## 4 October 2026 — Mobile refinement publication authorized (Codex)

The owner explicitly requested committing these changes to the live website. Publishing
the verified mobile refinement through `main` and the existing Git deployment integration.
Physical-device/background-tab acceptance and the inconsistent throttled LCP result remain
documented limitations, not completed checks. No database or environment changes are part
of this publication. Deployment completion is to be checked against the live domain.

## 4 October 2026 — Mobile refinement implemented locally (Codex)

Owner approved implementation and the public companion name **Mobi**. Detailed changes,
measurements and limits: `MOBILE-REFINEMENT-IMPLEMENTATION-2026-10-04.md`.

- Lab starts only when its content is readable. One clock pauses offscreen/hidden;
  manual steps pause and explicit Replay restarts. Compact phone controls and natural
  panel sizing; Mobi uses contained local reactions, preserving desktop travel.
- Phone hero/exam palette refined. Practice summary repaired at 320px (390px → 166px).
  Result Find shortened through disclosure (1247px → 399px at 390px). Light answer-state
  contrast corrected; navigation glass has opaque accessibility fallbacks.
- Arena header now sticks correctly. More opens without page jumps, scrolls between
  measured header/dock bounds, and restores opener focus on Escape. Final checks at
  320px, 390px with 200% text, and 844×390 landscape reached the last account action.
- Responsive matrix: 56 homepage/Practice/Result/quick-runner configurations across seven
  widths and both themes; no root overflow or page exceptions. Timing, reduced motion,
  text zoom, Mobi fallback, both NTA skins' answer/palette flows, public demo, theme
  persistence and free/error states verified in development fixtures. Result contrast
  scans had no flagged text. Evidence: `artifacts/mobile-refinement-2026-10-04/`.
- Lint/build passed. Recovery 35, learning 80, NTA/answer-integrity/payment 40: all 155
  tests passed without skips. Diff whitespace check passed. Build EPERM was resolved by
  approved filesystem access, with no cache deletion or configuration workaround.
- Isolated Slow 4G/4× CPU production samples: CLS 0; LCP 1.604–3.532s, so the 2.5s
  target is not consistently met. Physical Android/Safari, actual background-tab resume,
  assistive technology and real signed-in acceptance remain open. Local emulation does
  not establish hardware or production readiness. No paid model, migration or deploy.
- Preview: localhost:3010. Temporary production server 3011 stopped. Existing edits/
  untracked artifacts preserved. No commit or push; publication awaits device/performance
  acceptance and an explicit deployment decision.

## 4 October 2026 — Published mobile audit and Preparoo reference study (Codex)

Audit and plan only; no product behaviour or production changes. Plan:
`MOBILE-REFINEMENT-PLAN-2026-10-04.md`. Evidence: `artifacts/mobile-audit-2026-10-04/`.

- Live homepage: 390/1280px, both themes; Lab autoplay advances to Find while the replay
  has zero visible pixels on phones. The phone rail occupies 376px before the replay.
- Preparoo public reference: 390/1280px, wheel-scroll samples, phone illustration and
  backdrop-filter inventory. Observed mobile hero asset is WebP, plus PNG/SVG assets.
  Phone feature/explanation/preview hierarchy is the useful reference; no assets copied.
- Hydrated Arena fixtures: Practice, branded quick runner, Result at 320/390/430px,
  both themes, 18 captures. Zero document overflow/page exceptions. Narrow Practice
  cost text wraps nearly letter by letter; Result Find occupies 1247px at 390px.
  Light Result option letters produce two contrast flags (~2.75/2.82:1).
- Menu taps and Escape close verified at 320/390px. Public reduced motion shows a
  complete static replay and removes the floating guide. Initial unhydrated captures
  were rejected; localhost-origin retry restored fixture hydration without config edits.
- Next: playback readability gate + compact Lab + Practice summary + Result density/
  contrast, then phone-local mascot, previews/navigation and daylight depth. Mobi is
  a suggested name only, not an approved or implemented rename.
- Browser emulation is not physical-device proof. Real Android/Safari, screen reader,
  throttled production performance, both premium NTA skins and live signed-in workflows
  remain acceptance gates. No attempt, model call, checkout, migration or deploy ran.
  Only audit scripts/docs changed; product suites/build were not rerun. Local preview
  is running on port 3010. Existing untracked evidence directories were preserved.

## 5 October 2026 — Mistake Repair on GPT-6 Luna (Claude)

Owner chose GPT-6 Luna (USD 0.10 in / 0.50 out per 1M) for Mistake Repair: reasoning effort `low` for
the repair, `high` for the blind second opinion (`REPAIR_ROUTE`/`REPAIR_EFFORT` in
`src/services/recovery/mistakeRepair.js`; `AI_REPAIR_MODEL` overrides). `providers.js` now sends
`max_completion_tokens` + `reasoning_effort` (no temperature) to GPT-5/6/o-series and reserves budget
for hidden reasoning tokens. gpt-4o-mini remains the fallback. Price row inserted in production
`runtime_ai_prices` (owner instruction to ship now; file `20261005090000_runtime_ai_price_gpt6_luna.sql`).
Not verified: a live GPT-6 Luna call (the live eval run was blocked by the local permission
classifier). If Luna rejects a parameter, repairs fall back to gpt-4o-mini rather than failing.
Open: key disputes ("No repair for this one") still are not logged as evidence about the key; the
dispute flow designed on 5 October (soft flags, proposed key, student-was-right signal) is next.

## 4 October 2026 (late night) — Result page + Score Recovery Lab redesign after owner test (Claude)

Owner tried a 10-question quick practice (3 right, 7 wrong) and rated the Lab 5/10: no meaningful use,
weird "replay your decisions" slider, page too tall; wanted summary + Pip first, then the Lab, then
each answer with Mistake Repair. Done (see DESIGN.md "Score Recovery Lab"):
- `data/session_recovery.js` (new, pure): marks gap (6 per wrong, 5 per blank), chapters ranked by
  marks lost, per-question time from device events, factual observations. Tests:
  `data/tests/session_recovery.test.mjs` (added to `test:recovery`).
- `ResultPageClient.jsx` rewritten: summary hero with question strip → Lab → accordion answers.
  Removed from this page: ArenaHead, MistakeReplay, SessionReadout, the separate next-step block and
  the compact LearningNextAction (all duplicated the Lab). Components still exist for other pages.
- `ScoreRecoveryLab.jsx` rewritten as Find / Repair / Prove; slider replaced by a folded decision log.
- `MistakeRepair.jsx`: staged loading, two-card trap/why-wrong layout, "matched the key" check,
  auto-run when launched from the Lab queue, "Next mistake: Qn" chaining.
- `/preview/arena?view=result` fixture is now a realistic 10-question session scored by the real
  engine; `/preview/recovery` redirects there.
Verified: recovery 35, learning 80, nta 22, answer-integrity 6, du 19, payment/questions/PrepOS/repair
81 pass; lint clean; `next build` 62/62. Browser: desktop, 375px (no horizontal scroll), light theme,
Start repairing → Q2 repaired → Next mistake Q3 → Q4. Page height on the fixture fell from ~5.8k to ~3.6k px.
Second pass (owner: UI 9/10, clarity 7/10, "too much AI framing"): repair copy no longer narrates
the AI ("Why option C felt right", "Where it breaks", "Checked against the answer key"); server
held/not-explained messages rewritten the same way; sparkle icon replaced by a wrench; observations
are now tag + fact + consequence + one tip; step headers say what each step is for; mono uppercase
labels replaced with sentence case; motion added (score count-up, Pip entrance, strip stagger, bars
and chapter tracks grow when the Lab scrolls into view, repair cards stagger in; all off under reduced
motion). Owner approved commit and push to main.

## 4 October 2026 (night) — Score Recovery + AI unblocked and live in production DB (Claude)

Owner decisions in chat: names (marketing "Score Recovery", feature "Score Recovery Lab", action
"Mistake Repair"); student AI USD 25 per IST month; content generation USD 50 lifetime; AI migrations to
production "with my OK" (then explicit yes on the dry-run report); provider "whichever is best, make a
report" (AI-MODEL-REPORT-2026-10-04.md); OpenAI tonight because the Anthropic key is invalid.
Plan of record: PLAN-2026-10-04-NEXT-DAYS.md.

**Production database changes (owner-approved, applied via Supabase MCP):**
`runtime_ai_guard`, `prepos_credit_reservations`, `runtime_ai_monthly_cap` (new file
20261004120000). Dry run: reports/ai-migrations-dry-run-2026-10-04.json (PGlite rehearsal + production
precondition checks: no collisions, 879 wallets / 108 ledger rows untouched). Found and fixed before
applying: the ledger `reason` check would have rejected every reserve/release (all paid replies would
have failed); a single missing-usage response paused all student AI; prices expired after 30 days.
Verified after apply: cap 25, prices for claude-haiku-4-5, claude-sonnet-5-5, gpt-4.1-mini, gpt-4o-mini
(gpt-4o-mini added by SQL insert), all functions present, readiness script all green.

**Code:**
- `RELEASE_GATES.runtimeAi = true` (PrepOS replies + Mistake Repair); new `aiCommerce = false` keeps
  top-up checkout and charged Rival battles closed (order route, packs, pricing page, Rival).
- Anthropic provider in `src/services/ai/providers.js` (SDK retries off, per-model params: Sonnet 5.5
  without custom temperature / thinking off). `.env.local` routing: OpenAI gpt-4.1-mini fast+smart,
  gpt-4o-mini fallback (Claude routing documented for when the key is fixed).
- **Mistake Repair**: `data/mistake_repair.js` (eligibility, solve-then-explain prompt, blind second
  opinion, output validation incl. banned score/rank promises), `src/services/recovery/mistakeRepair.js`
  (1 PrepOS credit via reserve/commit/release; finished repair stored on the committed reservation and
  reopened free; dispute → blind check → question withheld exactly like a student report, credit
  released), `POST /api/recovery/repair`, `src/components/recovery/MistakeRepair.jsx` on result-page
  wrong answers with "Prove it: 5 fresh questions on this chapter".
- Budgets: AGENTS.md rewritten (limits are owner-set; do not invent stricter ones);
  `CONTENT_LIFETIME_CEILING_USD = 50` in budgetLedger.mjs; COST-POLICY, QUALITY, ROADMAP, README,
  PRODUCT, DECISION, IMPLEMENTATION, BACKLOG, LEARNING-DEPLOYMENT reconciled.

**Verification actually run** (logs: artifacts/ai-night-2026-10-04/):
- Live smoke through the production guard: gpt-4.1-mini ×2, gpt-4o-mini ×1 valid JSON, receipted
  (~$0.00007 each). Anthropic: 401 invalid key (booked conservatively, no pause).
- Live Mistake Repair eval on 10 real published bank questions: 10/10 solved = key, explained,
  $0.0038 total. Sample was all Accountancy (selection by ID order) — not representative.
- Tests: recovery 30/30, learning 80/80 (+5 Mistake Repair, +1 production-migration PGlite), nta 22/22,
  answer-integrity 6/6, du 19/19, payment 12/12, questions 9/9, recovery:validate; lint clean; build 62/62.
- Browser (preview fixture, localhost:3010): repair explained / withheld / out of credits / failure
  states, light theme; result page renders the panel only under wrong answers.
- Month-to-date runtime spend after all tests: ≈ $0.008 of $25.

**Deployed (owner chose "commit and push to main"):** `3c88f92` (all source/docs in the tree, incl.
the owner's and earlier agents' uncommitted work; untracked `artifacts/` 121 MB deliberately not committed).
**Incident:** that tree contained an earlier agent's www→apex redirect in next.config.mjs while Vercel
redirects apex→www, so production looped (50 redirects) for ~15–20 minutes. Hotfix `499475a` removed the
rule; site verified 200 at 01:03 IST on /, /pricing, /cuet-subject-combination, /api/stats; new
/api/recovery/repair and /api/ai/mentor/chat answer 401 signed out. Lesson: before pushing a dirty tree,
diff next.config/middleware against the deployed commit and probe redirects right after deploy. To make
the apex canonical, change Vercel's domain redirect first, then add the rule.
**Not done / gates:** Vercel `AI_*` env vars (code defaults to OpenAI gpt-4o-mini/gpt-4.1-mini, both
priced, so replies work if Vercel has OPENAI_API_KEY — unverified); signed-in production
check of a real PrepOS reply and repair; Anthropic key; learning/recovery migrations (triggers on live
`questions`) still unapplied; homepage/store copy not yet renamed to "Score Recovery"; AI purchases
closed; AI dispute quarantine relies on one model family tonight (both opinions from OpenAI).

Rollback: `update runtime_ai_budget set monthly_cap_usd=0` stops all student AI instantly; or set
`RELEASE_GATES.runtimeAi=false` / `PREPOS_MODEL_REPLIES_DISABLED=true`. Remove the repair route and
component to withdraw Mistake Repair. Wallets and ledger history are never rewritten.

## 4 October 2026 — Differentiator decision and first validation slice (Claude)

Decision: [DECISION-2026-10-03-DIFFERENTIATOR.md](DECISION-2026-10-03-DIFFERENTIATOR.md). Primary bet
"repair that holds", proven on one pathway before eight; trustworthy practice and goal-aware DU tools
support it. Rename to "Mistake Repair" proposed, **not applied** (owner decision). Brain reconciled:
README, PRODUCT.md, ROADMAP-2027 (amendment), IMPLEMENTATION-2027 (Stage 2), BACKLOG (ordered next).

Implemented (local source only; nothing deployed, migrated, seeded, purchased or sent to a model):
- Candidate pathway `data/recovery_candidates/sacrificing_gaining.{source,pathway}.json`: original
  wording, CUET UG 2026 Accountancy (301) Unit II locator with PDF SHA-256, 3 probes / 5 repair /
  6 checks, 14 families, hypotheses secure / direction_reversed / old_ratio_default / new_ratio_used,
  boundary checks (old ratio correct; unaffected partner). State `candidate`; manifest still
  `blocked_sources` with `pathways: []`. `source_registry.json` deliberately untouched (the paid
  worker treats an empty registry as a pause signal).
- Validator `data/pathway_validation.js` + `npm run recovery:validate`: exact-fraction recomputation of
  every key, matrix cell, derived ratio, unique key, option-text/claim binding, family disjointness,
  isomorphic scenarios, sources. 97/97. Corruption tests prove it fails on 13 seeded defects; it caught
  one real weakness during this work (swapped partner attribution passed), now fixed.
- Engine: no-gap diagnosis label; clearer feedback when repair ends; shared plan `primary.facts`
  (record vs rule) incl. immediate-check and upcoming-check states. Server digest now reuses
  `pathwayDigest` from the validator (same algorithm, one implementation).
- PrepOS: "Why this step" facts in the plan panel; free record reply appends the facts; model prompt
  states facts are authoritative (paid replies remain paused).
- Metrics `data/recovery_metrics.js` + read-only `scripts/learning/recovery-metrics.mjs`: completion,
  immediate/delayed/maintenance pass rates (Wilson, n), overdue and stalled attrition, defects,
  diagnosis counts, probe concordance, cost; groups < 5 suppressed; no decision < 30 episodes.
- Capability registry: `EVIDENCE_LEVELS`, `DIFFERENTIATORS`, `differentiatorClaimable()` (false for all).
- Dev-only fixture `/preview/arena?view=recovery&recovery=candidate[&net=lose-once][&clock=h]`: real
  recovery UI on the real engine, idempotent by request key; pathway read server-side in development
  only. Production build contains no candidate item IDs (grep of .next/static and .next/server: 0).

Verification actually run (logs in `artifacts/differentiator-2026-10-04/`):
- `npm.cmd run test:recovery` 30/30 (was 17; +13 candidate tests incl. PGlite storage),
  `test:learning` 74/74, `test:nta` 22/22, `test:answer-integrity` 6/6, `test:du` 19/19,
  payment_entitlements 12/12, mock selector + explore feed 9/9, `recovery:validate` passed.
- Candidate tests cover: per-hypothesis diagnosis/routing/timing (24h, 72h), secure path, conflicting
  probes → general repair, repeat exposure (seen family/question, failed checks consume families,
  exhaustion → blocked_content), interruption (stale submit rejected, expired check reopens repair),
  no key/matrix/claim leakage, concurrent start retries → one episode and one weekly allowance, refused
  start consumes nothing, second concept same week refused, idempotent response retry, answer
  correction → episode invalidated → counted as a defect.
- `npm.cmd run lint` clean; `npm.cmd run build` 61/61 pages.
- Browser (in-app pane, existing dev server on localhost:3010): start → probe 1 with response lost
  after commit → retry returned the committed state, 1 commit → probe 2 → supported old-ratio
  diagnosis, explanation, contrast → routed repair → hand-off to unassisted fresh check (4 commits for
  4 answers); conflicting probes → general explanation; PrepOS shows "Take your first fresh check"
  with record/rule facts; 320px: no overflow, 76px option targets; PrepOS facts contrast ≥ 9:1.
- Read-only metrics against the configured database: `learning_episodes` absent (PGRST205) → n = 0.
  The connected-learning migration is not applied there. Fixture report is labelled simulated.

Not done / gates: academic validation (independent Accountancy reviewer; one definition item flagged
for review); backend-signed evidence for the 14 items; staging migration + seeding + digest
registration; opted-in pilot flag (not built); scored fresh check through `/test` with real
sessions; real devices and screen readers; DPDP legal review (under-18 consent and telemetry before
~13 May 2027); owner decision on the rename; Testbook research (pages unavailable on 3 Oct).

Rollback: delete `data/recovery_candidates/`, `data/pathway_validation.js`, `data/recovery_metrics.js`,
`data/tests/recovery_pathway_candidate.test.mjs`, `data/tests/recoveryCohortFixture.mjs`,
`scripts/learning/{validate-pathway,recovery-metrics}.mjs`, the `candidates` key in
`data/recovery_pathways.json`, and the `recovery:validate`/test-list additions in package.json; revert the
small edits in learning_engine.js, capabilities.js, server/learning.js, MockMobAIHub.jsx, prepos.css,
mentor chat route, systemPrompt.js and the preview files. No data, credit, entitlement or payment path changed.


## 3 October 2026 — Owner round 2: motion, social proof, hero, Arena, Compass Pro, Combo Planner (Claude)

Owner decisions taken in chat this round: demos autoplay by default with an explicit pause; creators shown
with real follower numbers, ordered by reach; Compass gets Pro features (projection, college mapping); a new
USP feature; ₹99/month to be executed; live-site testimonials described by the owner as authenticated.

Implemented (local source only; nothing deployed, migrated, purchased or sent to a model):
- **Mistake Lab** no longer pauses under a passing cursor, a tap or the 35% visibility threshold; it pauses only
  fully offscreen, on keyboard focus, or by its button. Step descriptions share one fixed-height slot, removing the
  6-second layout shift that moved everything below on phones. Verified: steps advance while scrolling, rail
  height constant (376px at 390 wide).
- **Compass ladder** autoplays again by default as an eased, time-based rAF sweep (600–960, 11s); Pause/Play
  resumes from the visitor's score; filters no longer stop it; drag or quick score takes control.
- **Creators section** reframed "Trusted by CUET creators with 199K+ followers": counts read from public profiles on
  3 Oct 2026 (Garima Jain 25.2K + runs @du__club 161K; Rahul Thapa 13K; Prathna Jain 188), bios paraphrased from
  their own profiles, reel likes/comments where Instagram exposed them, sorted by reach, glass summary panel.
  Rahul's reel is marked Partner (his bio offers paid collaborations and the caption carries a discount code).
- **Hero**: CSS scroll-driven depth on the existing planes (aurora/grid/dots lag; drill card lifts on desktop
  only), a glass proof dock (199K+ creator reach, 73 DU programmes, 2 exam screens, 50 in 60), and a
  scroll-scrubbed statement. Progressive enhancement; reduced motion and unsupported browsers get the static page.
- **Compass Pro** (`data/compass_projection.js`, `/api/compass/pro`, `CompassPro.jsx`): per-paper practice
  projection out of 250 (attempt share × +5/−1 accuracy, Wilson range, ≥30 questions), four-paper total (one
  language + three strongest domain), personal DU shortlist (≤8 eligible programme+college targets, Rounds I–III
  in the chosen category, band position), next move (paper with most marks open + weakest ranked chapter).
  Pro enforced server-side; free sees a locked explainer. Labelled a projection, never a prediction or chance.
  No paid model call (runtime AI gate stays off). Advertised on landing, pricing and FAQ.
- **New USP: CUET Subject Combo Planner** (`/cuet-subject-combination`, `src/lib/du/combos.js`): targets + candidate
  subjects → every combination up to the paper limit checked with DU's own eligibility evaluator, ranked by targets
  met, programmes unlocked, fewer papers; "do not drop" subjects computed over all qualifying combinations; deep
  links into the calculator. Free, no signup. Promoted on landing, footer, CUET 2027 guide, sitemap.
- **Arena**: shared `ArenaHead`/`ArenaStats` (Practice's header and ruled stat strip); Today, Review, Progress
  rebuilt from a light "recovery-lab" slab into Arena pages; shared next-step card (full and compact); Radar's
  stray next-step moved under its header; Saved header; shared Empty/Error states restyled (no "// Error").

Not done, needs the owner:
- **₹99/month**: code is complete; creating the live Razorpay plan was blocked by the session's permission
  classifier. Create Plan (₹99, monthly, interval 1) in the Razorpay dashboard, set
  `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` in `.env.local` and Vercel production, redeploy. `publicOffer()` then flips
  every price surface. Run the LEARNING-DEPLOYMENT.md §A staging checks first.
- **Wall of Love**: not published. The July 2026 audit records the live-site quotes as fabricated and removed,
  and one is attributed to the owner. Publish only with written consent per quote; a founder quote must be
  labelled as such (ASCI/CCPA disclosure).

Verification: lint clean; build 56/56 (Edge Runtime warning unchanged); recovery 17/17, du 19/19 (+3 combos),
learning 74/74 (+5 compass projection), nta 22/22, answer-integrity 6/6, payment 12/12. Headless Chrome (CDP,
real input events): Mistake Lab and Compass autoplay timings; creators section 1280 dark / 390 light; hero
depth transforms at 400px scroll; statement word scrub; Compass Pro Pro/free/dark/light/390 with shortlist adds
and verdicts, contrast audit 0 failures; Today/Review/Progress/Radar/Saved fixtures; planner flow at 1280/390,
no overflow. Fixture APIs are stubs; real signed-in data, Instagram embeds on phones, real devices unverified.

Rollback: revert the files above; delete `src/app/cuet-subject-combination/`, `src/app/api/compass/pro/`,
`src/components/du/CompassPro.jsx`, `src/components/du/ComboPlanner.jsx`, `src/lib/du/combos.js`,
`data/compass_projection.js`, `src/components/arena/`, `src/app/hero-depth.css` and the two new tests.
No data, credit, entitlement or payment path changed.

## 3 October 2026 — Astra UI continuation: verification pass and confirmed fixes (Claude)

Local source only. No deployment, migration, checkout, paid generation, bank mutation or external message.
The PrepOS reservation migration remains unapplied. No image generated (none warranted).

Method: the in-app browser pane could not paint while occluded, so interaction checks ran in headless
Chrome driven over the DevTools protocol (scratch script, not committed) with real `Input.dispatch*`
mouse, touch and key events, `Emulation.setEmulatedMedia` for `prefers-reduced-motion` and colour
scheme, and touch emulation (`pointer: coarse`) below 900px. This is lab emulation, not real hardware.

Confirmed defects, each reproduced before fixing and re-checked after:
- **Signed-in Admission Compass, dark theme (high):** `du.css` reads marketing tokens defined only on
  `.mm`; inside the app shell they fell back to light ink (`#0a0a0a` on `#0b100e`, ~1.1:1 headings,
  buttons, notes), unset radii/shadows/`--volt-ink`. Bridged to `--a-*` tokens on `.app-shell .cmp`
  (`arena.css`). Light theme's active "All" chip was also unreadable; fixed by the same bridge.
- **Calculator sticky summary, light theme:** fixed night fill under theme ink (~1.1–1.6:1), public and
  signed-in, below 1100px. Now follows `--paper-raised`.
- **Calculator results at 320px:** implicit auto grid tracks (`.du-main`, `.du-list`) grew to card
  min-content, pushing cards 23–41px past the column. Pinned to `minmax(0, 1fr)`.
- **Wall of Love, 4 entries:** each lane held 2 cards, narrower than the lane, leaving an empty stretch
  every loop. Lanes now repeat hidden copies to at least 4 cards; duration scales per card (~16px/s).
  Accessible tree still lists each quote once. Removed `aria-pressed` beside a state-changing label.
- **Keyboard focus loss to `<body>`:** carousel arrow reaching its end (now `aria-disabled`, focus kept);
  activating an Instagram card (focus moves to "Open original"); demo drill after answering, Next and
  finish (focus moves to Next, first option, readout); Escape from the mobile nav sheet (returns to the
  menu button). Arrow group gained `role="group"` so its label is exposed. Nav `aria-controls` now set
  only while the sheet exists.
- **Mistake Lab, reduced motion:** tapping a question always snapped back to Q4 (effect re-ran on
  `picked`). Fixed. Score live region is quiet while the tour auto-plays.
- **Compass ladder:** UR/SC chips were 42x40 (now ≥44x44); "0 of 0 colleges" when a round/category has
  no published cutoff now says no cutoff was published for that cycle.
- **Narrow/zoomed phones:** below ~300px CSS width (≥125% zoom on a 360px phone) the menu button left the
  screen; hero title and dock CTA clipped at 200% text. Wordmark is visually hidden under 300px (still
  named), theme switch moves into the sheet under 240px, rotating hero phrase may wrap, phone title floor
  1.5rem, dock note yields under a 17rem container, dock spacer grows with text size and safe area.
  320px and wider are unchanged (measured).
- Touch tablets (761–1023px, `pointer: coarse`): NTA comparator's live palette cells 22x36 -> 49x44.
  Breadcrumb and stale-subject links raised to 44px targets.

Not changed after testing: MobileDock clearance at 320x640/740x360 (last footer line 41px above dock);
phone carousel arrows were already visible (44px) at 375/390, so code and notes agree.

Browser coverage actually exercised: homepage at 320, 390, 768, 1024, 1440, 1920 in dark and light
(no document overflow, no console errors, no broken images); 195px and 240/288px nav; 200% root font on
`/`, `/pricing`, calculator, `/cuet/english`; short landscape 740x360 and 568x320; full five-question demo
by touch and by keyboard only; comparator answer/review/switch preservation; Compass programme, category,
round, quick score, range keys and missing rows; Mistake Lab pause, step and tile selection in normal and
reduced motion; Wall fixtures 0/4/many incl. reduced motion at 320; Instagram arrows to both ends and
card activation (a real reel rendered); calculator alias search (BST, Accounts), score, share link,
reload persistence, Edit subjects; 20 public routes at 320 dark and 1280 light; `/preview/arena`
fixture views (free, Pro, inventory down, stale subjects, test, PrepOS plan/record/wallet, Compass,
Radar, Saved) at 320 and 1280. Computed-contrast audit (text vs nearest opaque surface) on home,
calculator, pricing and fixture views, both themes: remaining flags are the logotype dot (exempt) and
two probe false positives (gradient avatar, oklab launcher fill).

Verification: `npm.cmd run lint` clean; `npm.cmd run build` 55/55 pages, existing Edge Runtime warning;
`test:recovery` 17/17, `test:du` 16/16, `test:learning` 69/69, `test:nta` 22/22,
`test:answer-integrity` 6/6, `payment_entitlements` 12/12. `git diff --check` clean on edited files.

Still unverified: real phones (sticky hover, safe-area values, keyboard, 60fps), true browser page zoom
(root-font scaling and narrow viewports were used as proxies), screen readers, Instagram login walls,
signed-in persistence/entitlements/billing (`/preview/arena` is a stubbed fixture), creator permission
for the curated reels. Wall of Love stays hidden: no consented quotes exist.

Rollback boundary: revert the edits in `WallOfLove.jsx`, `CreatorReels.jsx`, `CompassLadder.jsx`,
`DemoDrill.jsx`, `MistakeLab.jsx`, `NavBar.jsx`, `Logo.jsx`, `social-proof.css`, `compass-ladder.css`,
`home-refinements.css`, `landing.css`, `globals.css` (crumbs, dock, nav-narrow, drill result),
`(app)/arena.css` (`.cmp` bridge, `.pr-alert a`) and `du/du.css` (`.du-sum`, `.du-main`, `.du-list`).
CSS/markup/focus only: no data, scoring, credit, entitlement or payment path changed.

## 3 October 2026 — Astra UI continuation handover (Codex)

The previous UI-refinement agent reached the usage limit during the final browser pass. A complete continuation prompt is saved at `docs/brain/CLAUDE-ASTRA-UI-CONTINUATION-2026-10-03.md`. This pass completed focused homepage, Compass, Mistake Lab, reveal, morph and historical-copy refinements, plus integrated social, authenticated-page and public-page work documented in the three `ASTRA-*-UI-NOTES.md` files. No image asset was generated because existing campus artwork and code-native product surfaces cover the meaningful visual needs.

Fresh verification: `npm.cmd run lint` passed with 0 errors and 0 warnings; `npm.cmd run build` passed with 55 generated pages and the existing Edge Runtime warning; `npm.cmd run test:recovery` 17/17; `npm.cmd run test:learning` 69/69; `npm.cmd run test:nta` 22/22; `npm.cmd run test:answer-integrity` 6/6; `npm.cmd run test:du` 16/16; `node --test data/tests/payment_entitlements.test.mjs` 12/12. Browser evidence covers homepage light/dark at 1440, homepage at 390 and compact 320 opening, Compass filters/keyboard/demo/missing-data state, Mistake Lab manual replay, and one real deferred Instagram embed. Wall fixtures, reduced motion, all route states, 200% zoom and real-device behavior remain unverified.

Open UI follow-ups: verify/fix phone carousel arrow visibility versus `ASTRA-SOCIAL-UI-NOTES.md`; inspect Wall fixtures and reduced motion; verify closed NavBar `aria-controls` target and MobileDock height at narrow/landscape sizes; complete route/theme/keyboard browser pass; preserve the honest empty public Wall. No production data, migration, checkout, deployment, paid generation or external communication was performed.

## 3 October 2026 — Astra UI handoff preparation (Codex)

Saved `ASTRA-UI-HANDOVER-2026-10-03.md`: current-source continuation prompt for
homepage refinement and remaining student-facing UI, Scroll Craft plus all 14
Emil Kowalski skill applicability, built-in image generation, and acceptance checks.
Read current contracts and Stage R/R2 notes; inspected the local homepage at phone
and desktop sizes, Compass, dark Instagram strip, and development-only Wall preview.
Confirmed the curated social strip is already present and public testimonials remain
hidden because the consented quote list is empty. No embeds activated in this pass.

No application code changed, no test/build suites rerun, no generation, migration,
checkout or deployment performed. This is prompt preparation, not UI completion.
Signed-in routes, all motion states and real-device behavior remain unverified here.
Rollback: remove the new handoff document and this entry; application source is unchanged.

## 2 October 2026 — Stage R2: original-site comparison, Compass, Radar, NTA, creators (Claude)

Local source only. Nothing deployed, migrated, purchased or sent to a model.

Compared with the live mockmob.in (read in the in-app browser): it had a Compass showcase with a cycling score card
and college labels, a Wall of love, a PrepOS section and a college marquee. Its Compass card showed "Reach / Moderate /
High" chances and a "score band predictor"; those claims are NOT reproduced (AGENTS.md: no admission probability, no
mock-to-CUET conversion). The three quotes on that site were not carried over.

Implemented:
- **Landing Compass ladder** (`CompassLadder.jsx`, `src/lib/du/showcase.js`): a score sweeps (or is dragged) across last
  year's real published Round I-III minimum allocation scores for 10 colleges in 4 programmes and 4 categories, from
  `public/du/2026`. About 10 KB shipped. It states a gap to a past cutoff only and links to the free eligibility tool.
- **Instagram strip** (`CreatorReels.jsx`, `src/lib/social.js`): 9:16 horizontal cards for the 3 creator reels and 3
  MockMob posts found on the public profile. Instagram's own embed loads only when a card is pressed. Edit the list in
  `src/lib/social.js` to add reels. Instagram's login wall blocks reading the feed, so entries are curated, not synced.
- **Wall of love** (`WallOfLove.jsx`, `src/lib/voices.js`): two opposing drifting rows (a grid under 4 voices), hidden when
  empty, only entries with `consent: true`. Dev-only prototype with labelled placeholders at `/preview/wall`. No
  testimonial is published.
- **Practice**: NTA Mode is a featured row (mini exam-console preview, chips, "Closest to exam day") with an exam-screen
  choice (MockMob / NTA style) for Pro and a free preview link for others. The grid is Quick, Full, Smart.
- **Admission Compass page** rebuilt as a product page: opens already ticked from the student's profile subjects
  (link, then saved choice, then profile), a three-step explainer, an honesty note, a bridge from the practice record
  ("Your practice says: ..."), and the sources. Calculator logic is unchanged apart from the seed prop.
- **Radar** rebuilt on the PrepOS record engine plus a theme-aware score trend (Chart.js reads Arena tokens and re-reads on
  theme change). Removed the invented composites ("Rank readiness", "Focus score"), the 1-4 axis radar chart, the
  non-functional "Ask Radar" box and the blurred paywall over made-up metrics.
- **Free vs Pro for the record**: free = marks ledger, top 3 chapters, findings, weekly summary; Pro = every ranked
  chapter, thin-chapter list, changed-answer and pace detail. Enforced in the record view and in Ask (server and client),
  and stated in the pricing page, landing page and PrepOS wallet copy.

Verification actually run: lint clean; `test:learning` 69/69 (adds landing_content 4: real-file cutoff match, embed
format, consent filter, Pro gating of Ask); recovery 17/17, du 16/16, nta 22/22, answer-integrity 6/6; build 55/55.
Browser: landing Compass ladder, reels (the embed loaded a real reel), Wall prototype, Practice with the NTA tile, Compass
page, Radar, at 1280 and 375 widths in light; no horizontal overflow.

Not verified: no signed-in session, so Radar/Compass/Practice used the dev preview with stubbed account APIs (real engines,
real DU data). Saved, Explore, Ranks, Contribute and My uploads were not touched this round. A dark-mode pass of the new
sections was not repeated. Creator names and handles come from the public profile page; the owner should confirm permission.

## 2 October 2026 — Stage R: Arena design language, PrepOS record and wallet, ₹99/month, landing (Claude)

Local source only. Nothing deployed, migrated, purchased, or sent to a model; no real wallet or ledger row was
read or written. Owner decisions taken this round: Pro is **₹99/month auto-renewing**; PrepOS model replies for a
small monthly allowance are **built but switched off** until the gates in LEARNING-DEPLOYMENT.md pass.

Implemented:
- **One icon language.** `src/components/ui/Glyph.jsx`: one lucide family at one stroke weight (`AppIcon`,
  `StatusIcon`, `SubjectIcon` for all 42 subject ids, `ModeIcon`) and two distinct credit coins (`CreditMark`:
  bolt = practice credits, orbit = PrepOS). Replaced the mixed nav icons, the star + "∞" credit pill, the
  38 decorative subject characters, and emoji/text glyphs (✅ ❌ 💡 🌵 ⚡ ★ ▲ ▼ ↻ ✓ ✗ ⚠) in Arena, uploads, feed
  cards, onboarding and votes. Remaining hits in `scripts/design-audit/glyph-audit.mjs` are the now-unused
  `glyph` data fields, a comment and a seed question.
- **Credit display fixed everywhere.** Pro now reads "Unlimited" (coin + word, not "∞" or "no credits") in the
  top bar, Practice, Account and the modal; free reads the number. A second chip shows the PrepOS wallet
  (unknown wallets show "—", never a number). Practice credits and PrepOS credits are always labelled apart.
- **Practice screen rebuilt** (`DashboardPageClient.jsx` + `.pr-*` in `arena.css`): two-column layout with a
  sticky session summary (a pinned launch bar on phones), subject and mode tiles with icons, official subject
  codes and entitlement badges, segmented controls, a Fine-tune disclosure, ruled stat strip, recent sessions
  with subject icons, status badges with icons. No inline `<style>`. Launcher no longer covers the Start button.
- **₹99/month.** `pro_monthly_99` plan, `/create-monthly-subscription`, `/api/billing/cancel`, checkout in
  `RazorpayPaymentButton`, `PlanCard` on Account (renewal date, two-step cancel). `publicOffer()` is the single
  source for pricing page, landing page, Arena upsell, modal, SEO title and mobile dock. Closed until
  `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set; until then the existing ₹99 one-time access stays the honest offer
  and copy says monthly "opens soon". When set, new one-time checkouts close; old orders keep verifying.
- **PrepOS record engine** (`data/prepos_insights.js`, free, no model): marks ledger (+5/−1, blanks), accuracy with a
  Wilson range, chapters ranked by marks left open only with ≥4 answered questions (thin chapters listed apart),
  difficulty split, pace from device events, answer changes counted both directions with the net, last-7-days vs
  previous week. Surfaces: PrepOS "Your record" tab, "Ask" answers record questions instantly and free, Today
  shows the top finding, the Result page shows "Where your marks went" for that session.
- **PrepOS wallet clarity.** Monthly meter ("38 of 50 left", reset date, no carry-over), purchased credits shown
  apart, plain list of what is always free and what costs 1 credit.
- **Model replies, gated.** Migration `20261002130000_prepos_credit_reservations.sql` (saved, NOT applied) adds the
  reserved→executing→committed|released lifecycle; `runModelReply` wraps the existing provider/runtime-budget
  guard; chat route answers record questions free, explains the plan while paused, and runs the lifecycle only
  when `RELEASE_GATES.runtimeAi` is true. Client keeps one request id per action and reuses it only after an
  unknown outcome.
- **Landing.** The section after the hero is now the interactive "Mistake lab" (`MistakeLab.jsx`, `mistake-lab.css`):
  four auto-advancing, tappable, pausable steps (replay → leak → one next move → fresh check later) on one
  labelled illustrative session, reduced-motion and keyboard safe; the recovery step shows its real release state.
  Sharper hero and section copy; offer-aware trust row, pricing block, FAQ and stats cell. NTA/MockMob comparison,
  scroll reveals and the rest were left untouched.

Verification actually run:
- `npm.cmd run lint` clean. `npm.cmd run build` 54/54 pages, new routes present.
- `test:learning` **65/65** (adds `monthly_billing` 5, `prepos_insights` 8, `prepos_reservations` 9 in real Postgres
  via PGlite, `prepos_model_reply` 9, plus the earlier quote/wallet suites). `test:recovery` 17/17, `test:nta` 22/22,
  `test:answer-integrity` 6/6, `test:du` 16/16, `payment_entitlements` 12/12, selection/offline 16/16.
- Reservation SQL cases proven: retry same key charges once; over-reserve refused; release restores included then
  bonus exactly and is idempotent; released key cannot be reused; commit final both ways; month rollover returns
  expired included credits as bonus; expiry sweep; ledger explains balance; service-role only. PGlite is one
  connection, so these prove arithmetic and idempotency, NOT multi-session lock contention.
- Browser (dev-only `/preview/arena`, stubbed account APIs built from the real pure engines, plus the real `/`
  and `/pricing`): Practice, PrepOS record/ask/wallet and landing at 320–1366 widths in light and dark; computed
  contrast audit (full text coverage) clean on Practice, PrepOS record and wallet (light), Practice (dark; one
  false positive: black on a volt gradient avatar), landing and pricing. No horizontal overflow. Unauthenticated
  boundary: new endpoints return 401.
- Lab auto-advance, pause, step taps, tile inspector exercised in the browser.

Not verified / known gaps:
- No real signed-in session: Account PlanCard, Result-page readout and Today glimpse are lint/build verified and use
  the same components as the verified previews, but were not rendered with live data. No real Razorpay checkout
  (test or live), no webhook replay, no model call, no real Android or screen-reader run.
- Research: 20 pages requested, 16 usable; far below the 300–400 requested. See DESIGN-REFERENCES.md.
- The Chart.js screens (Radar), Moderation, Saved and Explore were not re-skinned in this round.
- Account plan card forgets a requested cancellation across reloads; subscription is created with 24 cycles.

Next incomplete criteria: staging for the reservation migration + Razorpay test plan (LEARNING-DEPLOYMENT.md A/B);
signed-in two-theme pass of the remaining app routes; then Stage C (durable sessions) and Stage D (bank audit).

## 2 October 2026 — Claude handover execution, Stage A (Arena capability/theme truth)

Local source only. No deployment, migration, checkout, paid model call or content
generation. Existing user edits preserved. Checklist: `CLAUDE-WORKLOG.md`.

Implemented:
- `data/subject_registry.js`: versioned subject registry with official codes verified
  against the NTA CUET(UG)-2026 subject list (cuet.nta.nic.in, "Last Updated Sep 02,
  2026", checked 2 Oct 2026; provisional for 2027). Crosswalk keeps old IDs
  (`gat`→501, `applied_mathematics`→319; Engineering Graphics, Entrepreneurship, Legal
  Studies, Teaching Aptitude are not in the 2026 list → `retired`). Stored choices are
  never deleted; unsupported ones show a reason and cannot launch.
- `data/capabilities.js`: capability IDs/versions, inventory purposes (ordinary,
  recovery-eligible, original sample, verified historical — none claimed), and per-mode
  capabilities with entitlement copy that never ranks question quality.
- `data/practice_quote.js` + `GET /api/practice/quote`: read-only server launch quote
  (entitlement + expiry, allowance, credit cost, duration, inventory policy/count,
  reason, 60-second staleness, server-minted idempotency token). Unknown inventory or
  an unreadable allowance is unavailable, never free. Dashboard renders only this; the
  launch button is disabled unless the quote for the exact selection is launchable,
  re-checks a stale quote, and reuses the server token across retries.
- Dashboard copy: removed "Fast lane active", "highest-quality selection layer",
  "Upgrade for premium question quality", "Most Popular" badge and "unlock more premium
  mocks"; counts say "usable questions in the ordinary library" with unavailable state.
  Onboarding lists only practice-supported subjects and lets stale saved ones be removed.
- Today: the 10/20/30 choice now sets the session (`/dashboard?mode=quick&count=10|20`,
  30 min = 20 questions + 10 minutes review) and states the duration/charging contract.
- Arena theme: semantic `--a-*` tokens for dark (Night Arena, unchanged values) and an
  intentional light palette, scoped to `html:has(.app-shell)` so portals/toasts follow.
  Tailwind's variable-backed palette is remapped in light mode; volt-as-text becomes
  `--a-accent-text`. Theme switch added to the app top bar (≥640px) and mobile sheet,
  using the existing `mm:theme:v1` preference (set pre-paint by the root script). The
  pre-shell auth screen has a light variant. The NTA-style console pins its previous
  token values so it renders exactly as before in either Arena theme. PrepOS launcher
  stays a deliberate dark island.

Verification actually run:
- `npm.cmd run test:learning` 12/12 before adding the new file; new
  `data/tests/practice_quote.test.mjs` 10/10 (final suite totals are in Stage B below) (registry codes, stale/retired/unknown
  subjects, premium block, unknown/short/empty inventory, zero credits, included/used/
  unknown allowance, expiry, no quality ranking, minutes→session). `test:recovery` 17/17.
- `npm.cmd run lint`: clean. `npm.cmd run build`: first attempt failed fetching the Geist
  Mono Google Font (network); immediate retry compiled and generated 54/54 pages.
- Browser, dev-only `/preview/arena` (mock user, stubbed account APIs, quote built by the
  real `buildPracticeQuote`) on the owner's running dev server: computed-contrast audit of
  every visible text node (`scripts/design-audit/contrast-audit.js`) and overflow check.
  Dashboard light: 0 failures at 320/375/768/1024/1280/1920 after fixes; dark at 320 and
  1280: 0 (one false positive: black on volt-gradient avatar). Branded runner light 375:
  0; answer selection causes no layout shift (paper 598px before/after); selected border
  #6f8700 ≈3.9:1. NTA console in both Arena themes: unchanged conventional skin (only its
  existing orange "visited" chip, 4.4:1, which predates this change). Exercised states:
  stale saved subjects, inventory outage, insufficient inventory (15 > 12), Pro included
  with expiry, theme toggle click + persistence. No horizontal overflow at any width.

Not verified / remaining for Stage A:
- Signed-in routes other than the dashboard/runner harness (Today, Review, Progress,
  Radar, Account, Saved, Compass, PrepOS, Explore, Ranks, Upload, Result) were not
  rendered: no session in the built-in browser and no credentials may be entered. They
  inherit the token remap, but charts (Chart.js colours), page-specific inline styles
  (TestPageClient result states, MyUploads, Moderation, Upload, Analytics) still need a
  signed-in two-theme pass. Keyboard-only and screen-reader passes not done.
- Recovery-launch quotes (`purpose=baseline/full_sample`) are computed but not exposed in UI.
- Lead, not fixed: the root font is 15px, so Tailwind `min-h-11` renders 41.25px (17 uses
  outside PrepOS). New PrepOS controls use explicit 44px.

## 2 October 2026 — Stage B (PrepOS wallet safety and explanation layer)

Local source only. Paid PrepOS stays paused (`CAPABILITIES.optionalAi.state = 'paused'`).
No wallet balance, ledger row, payment or migration was changed; no model was called.

Implemented:
- `src/services/credits/aiWalletState.js` (pure): explicit wallet states `available`,
  `empty`, `paused`, `schema_unavailable`, `error`, with a safe message. An unreadable
  wallet has `known:false` and null balances — never a synthetic allowance or a spendable
  zero. Paused wallets still show real stored balances, not spendable. Central
  `isPaidUser` uses `effectivePremiumFromRow` (status / paid-through / legacy flag) at call
  time, so expired access stops counting.
- `aiCreditWallet.js`: `readAIWallet` is one select; it never inserts, resets or syncs
  (the monthly reset/allowance sync is projected and applied only inside the atomic RPC).
  `consumeDirectly`/`grantDirectly` and the swallowed ledger insert are deleted. Spend is
  RPC-only, requires a caller-stable operation key, and returns `prepos_paused` before any
  RPC while paused; a missing RPC fails closed (503). Grants for captured purchases still
  use the atomic grant RPC (historical orders and webhook/verify paths unchanged).
  Narrowed missing-function detection so real RPC errors are not treated as "missing".
- `consumeAIAllowance`: refuses while paused before reading or charging; uses the caller's
  operation key (Rival: `rival:<battleId>:<action>`), never `Date.now()`. Rival refuses a
  paid benchmark before creating a battle row while paused. Usage snapshot accepts a
  pre-read wallet and refuses charges unless the wallet is spendable.
- `GET /api/ai/credits`: one wallet read, `state`/`message`, practice credits labelled as a
  separate ledger, `checkout.open`, packs carry `status: 'paused'`.
- PrepOS hub rewritten as an explanation layer: "Next step" renders `/api/learning/plan`
  with the same 10/20/30 choices as Today; "Ask" answers product/credit/DU questions
  deterministically and sends plan questions to the existing no-charge server route;
  "Tools and wallet" shows the wallet state read-only with no pack buttons. Removed local
  missions/day plans/setup planner (20/45/60/90), benchmark entitlements, "GPT-4.1 mini"
  and "college and course direction" copy. DU wording now: published 2026 eligibility
  rules and Round I–III minimum allocation scores by category, historical only, no
  admission prediction or mock→CUET score conversion. Hub remounts per account.
- Retired unreferenced legacy `MockMobAssistant.jsx`, `AIAssistantDrawer.jsx`,
  `AIAssistantLauncher.jsx` (no importers; tracked in git) and a dead charge helper in
  `/api/ai/actions/execute`. `/pricing/prepos` shows the paused message, "—" for unknown
  figures and lists packs only when checkout is open. Rival shows "—" for unknown wallets.
- `scripts/learning/wallet-reconciliation.mjs`: read-only wallet↔ledger reconciliation
  (grants − bonus spends vs stored bonus; included spends this period vs stored usage;
  orphan ledgers). Offline `--fixture` or explicit `--remote-read`; never writes.
- PRODUCT.md lines promising fast lane, score-band estimate, college recommendations,
  peer review and live AI packs are marked superseded.

Verification actually run (all exit 0):
- `test:learning` **33/33** (includes `practice_quote` 10 and new `prepos_wallet` 11:
  expired/legacy entitlement, missing schema, read error, paused, stale period projection,
  unmaterialised wallet, client mapping of failed/legacy responses, narrow missing-function
  detection, source guards against direct writes/time-based keys, real
  `mm_ai_consume_credits` in PGlite: two consumes over balance → one succeeds, same-key
  retry charges once, ledger insert failure rolls back the balance; grant idempotency;
  reconciliation flags drift). PGlite runs on one connection, so "concurrent" consumes are
  serialised — this proves arithmetic/idempotency, not multi-session lock contention.
- `test:recovery` 17/17, `test:nta` 22/22, `test:answer-integrity` 6/6, `test:du` 16/16,
  `payment_entitlements` 12/12; payment + mock selector + practice filtering + offline
  batch (schema/dedup/alignment/generation/import) 24/24. `npm.cmd run lint` clean.
  `npm.cmd run build` 54/54 pages.
- Unauthenticated dev-server checks: `/api/practice/quote` 401 with unavailable state,
  `/api/ai/credits` 401, `/api/learning/plan` 401, `/api/subjects` 200.
- Browser (`/preview/arena?view=prepos`, stubbed APIs built from the real pure functions):
  plan at 375 light; paused wallet shows 68 / 38/50 / 30 with the required message and no
  pack buttons; `wallet=down` shows only "could not be read… Nothing has been charged";
  Ask answers for credits, DU chances and "what next" at 320 dark; keyboard focus ring on
  section tabs. Contrast audit was corrected mid-run (it had skipped oklch/oklab colours)
  and every Stage A/B view was re-run with full coverage: 0 failures except the known
  avatar false positive.

Remaining gates before any paid PrepOS reactivation (unchanged: stays paused):
1. Student-ledger reservation lifecycle (`reserved → executing → committed/released`)
   does not exist yet; only provider-side runtime reservations/receipts
   (`20261002121000_runtime_ai_guard.sql`). Provider timeout, unusable output and
   deterministic-fallback reversal tests cannot be written until that path exists.
2. Staging verification of `ai_credit_wallets`/`ai_credit_ledger` and both RPCs, then a
   `--remote-read` reconciliation run reviewed by the owner (not run; production data was
   not read).
3. Real multi-session concurrency test against staging Postgres.
4. Signed-in browser pass of `/mentor`, `/rival`, `/pricing/prepos` and account switching.

Next incomplete acceptance criterion: Stage A signed-in two-theme pass of the remaining
app routes, then Stage C (durable sessions/recovery integration) and Stage D (read-only bank
audit against the subject registry). Stage 1 explicit staging schema remains the release gate.

## Approved roadmap execution — source implementation, launch still gated

The complete product is **not released or definition-of-done complete**. Existing
user edits were preserved. No production/staging migration, quarantine application,
deployment, real checkout/refund or paid generation was performed in this run.
The content ceiling remains $2 calibration within $10 lifetime; runtime AI funding
has not been authorized. Current offer remains ₹99 through 31 July 2027.

Implemented local behavior:

- Central capability/release truth, versioned ₹299 plan and coordinated future copy;
  old ₹99 orders, access and offer amounts are retained. New sales remain gated.
- Bounded diagnosis, selected/general reasoning repair, independent numeric solvers,
  choice/numeric/evidence-span responses, fresh-family reservation and two delayed
  checks. Wrong/unanswered/expired checks reopen repair; repeats and assistance
  cannot certify understanding. No hidden keys/matrices/future questions in plans.
- Saved service-only owner/allowance/episode/observation/exposure transactions,
  durable sessions behind a switch, legacy ticket compatibility, revision/idempotency
  checks, account ownership and changed/held-content invalidation.
- Shared next action for Today/Radar/results/PrepOS; ordinary mistake Review and
  episode-based Progress; functional recovery forms/check launch in the existing shell.
  Decision replay distinguishes event effects and net changes. Experiments deferred.
- Compass now uses sourced DU rules/cutoffs; fictional chance/score predictor removed.
- Persistent request reservations/usage receipts and rate limiting saved in Postgres
  migrations. Unknown costs/funding block physical AI dispatch. Core plans/repairs
  have no paid model dependency. New AI top-ups/replies paused; wallets preserved.
- Rival duplicate/ownership guard and atomic completion SQL. Answer changes archive
  history and queue recomputation; comparable revalidated score derivation keeps
  original attempts intact. Edited/reordered answers cannot reinterpret old indexes.
- Shared practice eligibility for inventory, truthful zero/unavailable counts, public
  aggregate caching; current copy/legal/theme refinements and optional shorter guide.
  Open test-email sending is disabled by default and admin/rate limited if enabled.
- Roadmap authority, implementation checklist, local preflight and deployment/rollback
  instructions saved in the brain. Earlier pilot/count/store order is superseded.

Verification actually performed:

- `npm.cmd run test:recovery`: 17/17 passed.
- `npm.cmd run test:learning`: 12/12 passed. Includes isolated PGlite transactions
  for allowance concurrency, owner restrictions, response retries/CAS, original
  snapshot preservation, answer correction queues and family-hold invalidation;
  zero-funding/unknown-price/reservation/receipt/rate-limit behavior; Rival atomicity.
- Combined `node --test data/tests/*.test.mjs` plus recoverySafety, evidencePipeline,
  sourceAdapters, practiceModeFiltering and offlineBatchSchema/Dedup/Alignment/
  Generation/Import: **101/101 passed**. Includes NTA, answer integrity, mock selection,
  payment/entitlement, DU and offline import gates. Fixtures are software-only.
- `npm.cmd run lint` and `npm.cmd run build`: passed before the final HTTP boundary
  follow-up; final repeat results and HTTP checks are recorded below.
- `node scripts/learning/preflight.mjs`: sources 0, academic calibration paused,
  pathways 0, current price ₹99, ₹299 disabled. See reports/learning-preflight.json.
- Browser (local development server): homepage at 320px in both themes, keyboard
  Space theme toggle, pricing at 320px, honest count failure display and unreleased
  recovery notice. No horizontal overflow on inspected home/pricing. Recovery rendered
  its unavailable state with ordinary Practice/Review links; existing session resolved
  and GET /api/learning/plan returned 200. No new study attempt or payment initiated.
  One navigation timed out before its rendered state resolved; it was not treated
  as a completed flow until the DOM showed the actual unavailable state.
- Initial local production boundary pass: 8/9 expected statuses. Empty anonymous
  mentor payload returned 400 before authentication; auth/rate limiting moved before
  parsing/context work, with a bounded payload. Final repeat recorded below.
- No screen-reader, real Android, constrained-network, Lighthouse or field CWV
  result. Theme/320px inspection does not establish accessibility or device readiness.

Release gates and remaining implementation:

1. Explicit staging schema verification/application of saved migrations, including
   older interactions, bookmarks/progress, atomic credits and recovery foundations.
   Rival additionally requires the older db/migrations AI-overlay tables before its
   new submit service deploys. No source deployment should bypass this dependency.
2. Eight permitted/versioned, independently calibrated concept pathways with complete
   fresh inventory. Sources and academic benchmarks are empty; no academic accuracy,
   student learning gain or source-backed coverage is established by these tests.
3. Real authenticated baseline → investigation → repair → immediate → two delayed
   checks, resume/account-switch/concurrency/expiry/invalidation/exhaustion tests in
   staging. Audit legacy device-ticket wall-clock limitations; its telemetry cannot
   prove answer timing. Durable server checks enforce deadlines without grace answers.
4. Correction-queue worker, report-triggered evidence re-evaluation, payment
   reconciliation and cohort/cost/support reporting remain unfinished. Uncertain
   content stays withheld. Fresh timed decision experiments wait for the core loop.
5. Real staging captured checkout, old pending orders, new V2, signature/owner/amount,
   webhook retries and refund/revocation. Optional runtime wallet reservation/reversal
   and price/funding receipts remain gates; paid AI stays paused.
6. Android/accessibility/performance, season receipts and ≥70% contribution margin;
   opted-in cohort before public recovery/₹299. Do not sell planned features as live.

Next incomplete acceptance criterion: **Stage 1 explicit staging schema and real
authenticated session/owner flow**. Stage 2 cannot release until academic source and
calibration gates pass. See IMPLEMENTATION-2027.md for the dependency checklist and
LEARNING-DEPLOYMENT.md for switches, migration order and non-destructive rollback.

Final follow-up results:

- Final `npm.cmd run build`: exit 0; optimized Next 16.2.4 build completed. Existing
  edge-runtime/static-generation warning remains informational.
- Final standalone `npm.cmd run lint`: exit 0, no diagnostics. One preceding
  overlapping lint invocation ended exit 1 without diagnostic output; this was
  not called a pass. The separate repeat completed successfully.
- `node scripts/learning/http-check.mjs`: exit 0, **9/9** expected production-build
  authentication/unavailable statuses. Saved reports/learning-http-checks.json.
  Includes the corrected anonymous mentor 401, disabled email 404 and production
  preview 404s. No cookies, credentials, provider dispatch or payment was used.
- Temporary development and production inspection servers were stopped, browser
  viewport restored and temporary inspection tab closed. No deployment made.

## 2 October 2026 — roadmap gap audit and Claude handoff

This follow-up was documentation-only. No product source, database, migration,
entitlement, wallet balance, payment, content record or deployment was changed.
The existing user-owned development server was left running. The companion audit
`ROADMAP-GAP-AUDIT-2026-10-02.md` records the evidence; the copy-ready execution
contract is `CLAUDE-MASTER-HANDOVER.md`.

Confirmed current issues include the Arena app shell staying dark while the
marketing theme reports light, no Arena theme control, stale Fast lane and mixed
availability copy, inconsistent subject catalogs, PrepOS local planner/time
choices, and wallet degraded/fallback paths that can expose synthetic balances or
non-atomic direct consumption. These findings are release blockers or staging
work; they were not patched in this audit.

The Impeccable detector returned 95 heuristic advisories across Arena/dashboard/
PrepOS files (49 font-size, 28 color, 15 radius, plus grid/transition/easing).
They are retained as review leads in `reports/claude-handover-static-audit.json`,
not counted as confirmed defects. A read-only local browser check observed the
Arena computed dark shell under `data-theme="light"` and the 320px Today fallback.
No new mock, purchase, paid model call, migration or content generation occurred.

Next incomplete acceptance criterion remains the explicit staging schema and real
authenticated session/owner flow. The next Claude run must fix Arena/capability
truth and PrepOS wallet safety before enabling paid AI, then begin the authoritative
CUET syllabus registry and read-only question-bank audit. Existing prior test/build
numbers remain prior-run evidence and were not rerun in this documentation pass.
- `git diff --check` identified three trailing-space lines introduced while editing
  pricing; they were removed. Other existing user changes remain intact.

## Historical status — October 1 2026

This is a locally implemented foundation and redesigned recovery pilot journey,
NOT a completed production launch. No production migration, bank mutation, deploy,
paid content request, APK signing, store submission or real-device test was made.

| Milestone | Completion evidence | Remaining gate |
|---|---|---|
| Project brain | AGENTS, PRODUCT, DESIGN and brain specifications/architecture/quality/cost/benchmark/backlog | Keep updating actual results |
| Read-only inventory | 9,342 records; saved per-item report and 59-row quarantine dry run | Independent semantic checks, schema deployment before applying quarantine |
| Historical failure classification | Ten zero-candidate/zero-validator routes classified unknown | Request-level receipts needed to reconstruct old bills |
| Durable cost controls | Shared SQLite reservations, usage receipts, crash/concurrency/zero-yield/repair/cache tests | Verified prices, durable worker deployment; distributed ledger not implemented |
| Evidence publication | Signed hashes, source/family/version checks, blind solving, alternative challenges, route calibration; worker/offline importer integrated | Source registry/academic fixtures empty; source-backed model adapter configured but not executed; numerical family solvers not supplied |
| Practice/recovery backend | Server scoring, event replay, idempotency, ownership, credits, playbook/review queue, changed-evidence progress exclusion | Saved SQL needs staging/production setup; correction recomputation and fuller timing/review behavior pending |
| Web pilot UI | Immediate illustrative replay, separate pilot signup, observed/inferred results, four launch subjects; public reference notes | Remaining legacy screens, live authenticated content flow |
| Mobile beta source | Bundled React/Vite/Capacitor assets/fonts, OTP/bearer, native secure storage, cached reviews/drafts, reminders; Android project generated | Public environment config, signing, JDK/SDK, macOS/iOS, real-device QA and store review |

## Verification

- npm run test:recovery: 15 focused software regressions, including local Postgres
  transaction/owner/credit/idempotency/quarantine/passage rollback tests.
- Existing answer integrity, NTA selection, mock selection, payment/entitlement and
  offline batch suites: 52 tests. Academic fixture release remains unverified.
- Production web and mobile asset builds compile. Targeted edited React lint is clean.
- Production-mode HTTP checks reject unauthenticated/forged-token attempt, analytics,
  recovery, session and mobile reads/submissions with 401. The illustrative preview
  returns 404 in production. Saved results: artifacts/recovery/http-checks.json.
- Desktop/390px captures in artifacts/recovery; no horizontal overflow in inspected
  home/lab. Replay control is 44px. Public catalog references include >1,000 designs;
  no claim that 1,000 screens were individually inspected.
- Fresh Impeccable design review: initial disposition fix; all six material fixes
  resolved in one batch; final disposition ship. DESIGN and sidecar reconciled.

Artifacts are local evidence, not live app success. Lab screenshots contain clearly
labelled development-only illustrative data. Existing user edits/payment changes
were preserved. No independent academic accuracy or model-versus-human result exists.

## Next agent

Read brain README, BANK-AUDIT and BACKLOG. Verify live setup before claiming anything
deployed. Start with authenticated source/key extraction and development/held-out
fixtures; do not open paid generation on missing prices or empty references. Keep
the $2 calibration hold and $10 ceiling. Never reset the ledger or publish the old
Economics sample based on its heuristic grade. Follow BACKLOG in order.

## 2026-10-01 stabilisation and landing rebuild (Claude)

Done and verified locally (dev server, port 3100):
- Homepage was unstyled: ChatGPT's last pass shipped about 20 `cuet-*` classes with no CSS.
  `src/app/page.js` rebuilt on the existing `.mm` system plus `src/app/landing.css`
  (`.lp-*`): hero with playable five-question drill, subject keys, live stats band,
  Arena/Radar/Compass screens (static, labelled illustrative), steps, Score Recovery
  Lab replay, free vs Pro (₹99 once) comparison, FAQ, close. On phones the drill
  follows the lead directly; subject keys follow the drill.
- `/api/leaderboard` returned 500: `Database.getLeaderboard` put 512 user ids in one
  `.in()` filter (20 KB URL, HeadersOverflowError) and silently read only the first
  1000 of 1807 attempts. Now pages attempts and chunks user lookups by 100
  (`data/db.js`). Synthetic practice rivals remain labelled.
- `LiveStatsBand` fallback claimed "10,000+" questions; live bank is 6,963
  (`/api/stats`). Fallbacks are now "6,900+" and "40". Bank note reworded to
  "automated schema, duplicate and answer-key checks".
- `/login` and `/signup` still used legacy dark utility classes inside the paper
  world. Rebuilt with `AuthShell`, `auth.css` and a restyled `SignupCard` (auth
  logic unchanged: Google, email link, 8-digit OTP).
- Testimonials: no invented student quotes were added. `src/lib/voices.js` is an empty
  list; the landing section renders only when real, consented quotes are added.

Verification: `npm run lint` clean; `npm run build` passes, all routes; test:recovery
15/15, test:nta 22/22, test:answer-integrity 6/6, payment_entitlements 11/11.
Public routes and `/api/stats|subjects|leaderboard` return 200 locally; 390px and
1440px landing/auth captures show no horizontal overflow.

Not verified: any signed-in screen (dashboard, test, result, saved, profile, Compass,
PrepOS) was NOT visually checked this pass (no test credentials used); Quick Practice
submit/resume/idempotency from the handover; Razorpay checkout end to end; production.
Remaining legacy dark-style screens inside `(app)` still need the same audit.

## 2026-10-02 landing redesign round 2 (Claude)

Owner rejected the paper homepage as less polished than mockmob.in, prepium.in and
ug.preparoo.app. Rebuilt `/` as "Night Arena" (see DESIGN.md): layered grid/dot-matrix
backdrop with pointer-lit dots, hero stage (playable drill + Example chips), subject
marquee, live stats, wide/pair/wide/trio bento (Arena, Radar, PrepOS, Compass, three
small tiles), animated three-step section, Score Recovery Lab replay, live per-subject
counts, free vs Pro, FAQ, closing band. Restored FAQ + breadcrumb JSON-LD from the old page.

Root cause of the hover "shake": `DecodeWord` re-scrambled on hover and glyph widths
differ. Deleted; replaced by width-reserving `MorphWord`. Verified by measuring every
hero element's box before/after hovering the primary CTA: no movement (only the
decorative chips on their own loop). Drill height is constant before/after answering.

Verified in the browser at 320, 390, 820x1180, 1024x768, 1280x720, 1440x900,
3440x1440 and 844x390 landscape: no horizontal overflow at any size; hero balanced;
mobile nav works on dark. `npm run lint` clean; `npm run build` passes; test:recovery 15/15;
payment_entitlements 11/11.

Not verified: real-device performance on a budget Android (backdrop uses static CSS layers;
pointer layer is disabled on touch); reduced-motion behaviour was reviewed in CSS, not
exercised in a browser; Lighthouse not run; no screen-reader pass beyond the a11y tree.
`DynamicCompassPreview.jsx`, `ArenaPreview.jsx`, `RadarField.jsx` are now unused by `/`.

## 2026-10-02 free DU eligibility and cutoff calculator (Claude)

New public tool at `/cuet-cutoff-calculator` plus a landing-page teaser (`#du-eligibility`),
nav and footer links, a hero link, a Compass-tile link, a Radar-page link that pre-fills the
student's practised subjects, and a pointer from the Admission Compass page.

Data (all from four public DU documents, user-approved download of five PDFs, ~9.7 MB):
UG Bulletin of Information 2026-27, and the Round I, II, III minimum-allocation-score lists.
Pipeline in `scripts/du-csas/` (geometry-based PDF parsing, hard failure on ambiguity);
output is static JSON in `public/du/2026/` (no serverless function runs for the tool).

Verified:
- Cutoffs: S.NO contiguous (1,393 / 1,393 / 956), identical seat lists across Rounds I and II,
  Round III a subset, and the multiset of every parsed score equals the numbers printed in the
  PDFs: 17,316 cells (two whole-number cells in Round I located individually). One displayed
  value (Dyal Singh B.Com. (Hons.) Round I OBC-NCL 695.3) traced to the raw PDF coordinates.
- Eligibility: 73 Bulletin programmes, 149 combinations all parsed into typed slots, every
  combination satisfiable. Engine tested (`npm run test:du`, 12 tests) including language
  specific rules, GAT combinations, the "considered only if seats remain" combinations III/IV,
  and the UR-merit rule for reserved categories.
- `npm run lint` clean; `npm run build` passes (route prerendered static); test:recovery 15/15,
  test:nta 22/22, test:answer-integrity 6/6, payment_entitlements 11/11.
- Browser: desktop 1440/1024 and mobile 390 on the calculator and the landing teaser; no
  horizontal overflow; selection, URL sharing, expand-to-cutoffs, score status all exercised.

Also fixed: `html, body { overflow-x: hidden }` in globals.css made `<body>` a scroll container,
so `position: sticky` (including the site's own nav) never stuck. On marketing-system pages
(`.mm.lp`) it is now `overflow-x: clip`.

Not done / limits:
- Seat counts (Prepium shows them): the seat-matrix PDF is organised differently and was not
  parsed. Not shown rather than guessed.
- 5 Bulletin programmes (3 music, B.F.A., B.Sc. PE) have test-based merit and no CUET cutoff
  list; shown for eligibility only.
- 2026 data only. Add a 2025 cycle by adding a second dataset folder; the UI reads `meta`.
- No Lighthouse or real-device run. No screen-reader pass beyond the a11y tree and aria states.
- `src/lib/admissionCompass.js` (existing, untouched) still uses invented per-college "target"
  scores and category adjustments. It is clearly labelled as an estimate, but it should not be
  presented as cutoffs. The calculator is the source of real published numbers.

## 2026-10-02 calculator rework after owner feedback (Claude)

Owner reported the cutoff calculator "not updating live", no way to recheck, clunky UX, and that
subject mapping did not show that IP/Computer Science (and similar) are one CUET subject.

What I could and could not reproduce: scripted clicks always updated state, so I found no
single hard failure. I did demonstrate real defects that make live updates invisible or
unreliable for a person: a floating "N programmes unlocked" bar sat over the chip grid (scripted
`.click()` bypasses overlays, a finger does not), the results were far below a very long picker,
and the address bar was rewritten on every change. All three are removed.

Changes: two-pane layout from 1100px (sticky subjects pane, results beside it, live); below that a
sticky summary bar with the live count and Edit / View buttons; removable selected-subject tray;
full official subject names on chips plus a finder that maps aliases (IP, Informatics Practices,
Biotech, Book Keeping, Applied Maths...) to the one subject DU/NTA count; every programme card shows
the Bulletin's exact combinations with met / missing marks, and "Not eligible yet" rows open to the
same rules. The URL is read once on load and then cleaned; edits persist in localStorage; Share
builds the link on demand.

Accuracy check: B.Sc. (Hons.) Computer Science has two Bulletin combinations and BOTH require
Mathematics/Applied Mathematics, so a commerce student with only IP is not eligible. Tests added
(16 total in `npm run test:du`): that case, the Computer Science / IP equivalence, rule
explanations, alias search. Verified in the browser with a real click: adding Mathematics took
35 -> 41 programmes and made B.Sc. CS Honours and Economics Honours appear.

Note: Prepium lists Sanskrit under List B; the 2026 Bulletin's List B (22 subjects) does not,
so the tool follows the Bulletin. Lint, build, test:du 16/16, recovery 15/15, nta 22/22,
answer-integrity 6/6, payments 11/11. No real-device or screen-reader run.

## October 2, 2026 — homepage refinement and exam-interface comparison

Preserved the existing homepage and added a refined hero practice frame, persistent
animated light/dark switch, four original campus illustration cards, and an
interactive MockMob/NTA-style comparison. Premium NTA sessions now offer a
presentation switch on the same runner; the existing scoring, timing, entitlement
and credit logic is unchanged. College cards hand off a validated programme filter
to the existing DU calculator.

Verification: production build and ESLint pass; NTA 22/22, DU 16/16, recovery 15/15,
answer integrity 6/6, payment entitlements 11/11. Browser checks at desktop and
390px/320px confirm theme persistence, mobile menu, no horizontal document overflow,
preview answer/review/clear/reset state, and Commerce preset 35/73. Premium setup
link selects NTA Mode with 50 questions / 60 minutes without starting the mock.
New browser tab reported no console errors. Generated campus asset is 276 KB WebP.

No production deployment, migration, checkout or scored exam submission performed.
The real premium exam submission path with the classic skin remains a release check.
NTA style is a reference-based practice console, not a guarantee about the official
2027 UI. Source changes and their rollback boundary, reference survey, image prompt
and evidence are in HOMEPAGE-REFINEMENT-2026-10-02.md and artifacts/homepage/.

## October 2, 2026 (second pass) — repair, theme, Arena alignment (Claude)

Local source only. Nothing deployed, migrated, purchased or generated. Screenshots:
`artifacts/refinement-2026-10-02b/`.

Confirmed defects fixed (cause → fix):
- Radar/analytics was empty for every student: `/api/analytics` kept only `server_snapshot_v1`
  attempts (Score Recovery pilot, not launched) while practice writes `server_practice_v1`.
  Now counts the owner's practice; pre-server browser-scored attempts are included and labelled
  (owner decision). Recovery/progress evidence rules are unchanged. `data/attempt_scoring.js`.
- Submission could be rejected by clock skew: runner timed events as client `Date.now()` minus
  server `startedAt`; server rejects events later than its elapsed time + 2 s. Runner now times
  from receipt using only the server duration; `finishPractice` scores answers without the
  (discarded) event log if the log is malformed (`scorePracticeSubmission`). Answers still fully
  validated. Recovery-pilot `finishSession` is unchanged.
- Result page called every new practice attempt "historical… not scored from a server-held
  snapshot". Copy now distinguishes server-scored practice from older browser-scored attempts.
- Nav dropped Radar, Saved, Compass, PrepOS, Explore, Ranks, Contribute, My uploads (pages still
  existed; several are sold as Pro). Restored as a "Tools" group (owner decision). App tour pointed
  at nine missing nav targets; rewritten for the current nav.
- Light mode: subject-card hover was `#121712` behind `#172016` text (1.08:1); landing secondary
  button hover `#151a14` (1.05:1); dark mode on paper sub-pages: shared `.mm-btn--secondary:hover`
  was `#fff` behind near-white text (1.11:1); calculator/teaser lime, amber and pink text on paper
  (1.2–2:1). Cause: night-only literals in `landing.css`/`du.css`/`globals.css`. Fixed with theme
  roles (`--accent-text`, `--accent-line`, `--accent-wash`, `--tint`, `--surface-hover`,
  `--warn/bad/good-text`) defined per theme in `marketing-theme.css`; per-selector light patches removed.
- 900–1023 px: marketing nav labels wrapped onto two lines after the toggle was added. Text links
  now move into the menu below 1024 px; CTA and Log in stay. NTA-style "Mark for Review & Next" and
  "Clear response" were hidden at 761–1023 px; now visible below 1024 px.

Refinements: theme switch redesigned (sun/moon thumb, inset-shadow crescent, stars, spring travel,
press squash, circular View Transition reveal from the switch; instant under reduced motion or
without support). Hero practice bay restored (framed bay, lit slate card, deep shadow, skeleton
explanation) plus a two-card stack; status row and purpose rail kept. Campus cards pair as
landscape cards at 761–1023 px. Arena: scoped `src/app/(app)/arena.css` re-skins shell, dashboard,
shared app primitives and the branded runner; NTA-style console untouched apart from the
breakpoint fix. Dashboard copy and numbered setup steps; no logic change.

Verified locally:
- Tests: recovery 17/17 (2 new), NTA 22/22, DU 16/16, answer integrity 6/6, payments 11/11,
  mock selector + practice filtering + offline batch (pure) 13/13. Paid-model pipeline tests not run.
- `npm run lint` clean; `npm run build` passes. Production server: `/preview/arena` and
  `/preview/recovery` 404; unauthenticated `/api/analytics`, `/api/attempts`, PATCH `/api/sessions` 401.
- Browser: computed-state contrast audit of every hover/focus/pressed/selected/disabled rule on
  `/`, `/pricing`, `/cuet-cutoff-calculator`, `/login`, `/about`, `/cuet-2027`, `/features` in both
  themes; light homepage clean; calculator text (542 nodes) passes in light with results open.
  Real-pointer hovers checked in both themes. Toggle: click, Space, Enter, focus ring, aria-checked,
  persistence, reveal animation from the switch. No document overflow at 15 widths 320–1440.
  Drill answer causes no layout shift (stage 718 px before and after).
- Arena via `/preview/arena` (development-only, mock user, stubbed account APIs, no production
  writes): dashboard subject/mode/count selection, 50-credit gate disabled with top-up hint, launch
  URL; branded runner answer, mark, clear, navigate, submit; captured payload scored by the real
  `scorePracticeSubmission`; NTA-style console at 1366 and 900 px; mobile menu at 375 px.

Not verified / release checks:
- A real signed-in Quick Practice (start → submit → result → Radar) was approved by the owner but
  not run: the browser pane had no session and credentials cannot be entered for the owner.
- Live premium NTA submission with either interface; Razorpay checkout; production deploy.
- Reduced-motion paths reviewed in code, not emulated. No real-device, Lighthouse or screen-reader run.
- `/api/bookmarks` hides saved questions that fail the current quality gate, but the free-tier
  25-save limit still counts them (not changed).
- Other app pages (Compass, Radar, Saved, Profile…) inherit the re-skinned primitives but their
  page-specific layouts were not redesigned.

## 3 October 2026 — Round 4: restored craft, Pip guide, motion system, study loop (Claude)

Local source only. Nothing deployed, migrated, purchased, generated or sent. Full record:
`docs/brain/ROUND4-NOTES.md`; motion rules: `docs/brain/MOTION.md`; brief:
`scrollcraft/builds/mockmob-round4/BRIEF.md`; evidence: `artifacts/round4/`.

- Regressions fixed at their measured causes: comparator palette (44px min-width in 1fr tracks,
  5-column phone override with span-2 holes, lost NTA placeholder skin, clipped focus rings);
  Arena entry and exam-day card (round-3 blanket overrides; containers now fade, leaves rise, so the
  fixed phone dock is never re-anchored); exam-day clock now really counts down, offscreen-paused.
- Pip: one guide that hands off between five perches and reacts to page events (drill answer, Mistake
  Lab next move, exam preview answers). Chosen over two other built prototypes (archived). Static
  perches remain the no-JS/reduced-motion experience. No mascot motion in the timed runner.
- Study loop: Result ends with one next step from the PrepOS insights engine (no chapter named
  below its 4-answer ranking rule), plus Review, Saved, Radar, Back to Practice. Saved links back to
  Practice.
- Sweep: 760 loads (38 routes × 10 sizes × 2 themes): root overflow 0, console errors 0. Found and
  fixed a Practice panel cut off from 320–1440px (grid `auto` tracks) and six sub-44px controls.
- Verified: `npm run lint` clean; `npm run build` passes; recovery 17, DU 19, learning 74, NTA 22,
  answer-integrity 6, payments 12, Explore/contribution 8 = 158/158 pass (logs in
  `artifacts/round4/logs`). Reduced motion, 200% text, real-touch flows, light theme and contrast on
  new surfaces checked in Chrome. Lab perf (prod build, 390px, 4× CPU, Slow 4G): LCP 2.9–3.3s, CLS 0.
- Not verified / release checks: physical phones, screen reader, authenticated persistence and
  resume, live premium NTA submission, payments; LCP above target with cause not isolated.

## 3 October 2026 — Round 5: continuous Pip journey and Arena handover

Local implementation. Full evidence and limits: `docs/brain/ROUND5-NOTES.md`; scoped future
work: `docs/brain/ROUND5-NEXT-FEATURES.md`; artifacts: `artifacts/round5/`.

- Seven ordered perches with hysteresis replace the narrow observer band. One desktop actor
  carries through a reserved gutter; phone motion stays local and follows document scrolling.
  Reverse/fast crossings coalesce. Larger original art, pose fades and static reduced motion.
- Lab celebration waits for the visible next-move control and settled visible Pip. One peak
  per view. Today, Practice, Review and Saved gain calm companion states; recorded-session
  acknowledgment uses server data. PrepOS keeps its orb, voice and capability/credit wall.
- Three travel/PrepOS studies archived; temporary Round 5 route removed. One requested image
  concept generated; original six pose assets remain in product. Exact GPT Image 2.5 selection
  is unavailable through the tool, so no such model-version claim is made.
- Lint and production build pass. Recovery/DU/learning/NTA/answer-integrity/payment/Explore
  suites: 158 passed, plus two station-selection tests. 760 verified layout loads: 380 public
  production + 380 development fixtures; zero root overflow, pageerrors or failed loads.
  Reduced motion, quarter-interval reverse journeys and six 200%-text fixture views checked.
- Hero-animation ablation reproduced lower text LCP (phone 1.60–1.94s versus guide baseline
  2.27–3.64s). Removed only the measured lead paragraph's entrance animation; other entrances
  remain. Final production measurements and methodological limits are in ROUND5-NOTES.md.
- No deployment, production migration, bank writes, paid-content generation, outgoing email
  or checkout. Live authenticated persistence/resume, premium NTA submission, payments,
  physical devices and screen-reader acceptance remain release gates. Fixture counts and
  laboratory performance are not live account evidence or field Core Web Vitals.

## 3 October 2026 — owner-approved Round 5 follow-up and local-server recovery

Local implementation; full source map, evidence and limits: `docs/brain/ROUND5-COMPLETION.md`.
The owner subsequently approved implementing the remaining plan and restoring the site.

- Tonight's plan now uses the shared server plan and ties its recorded state to a current-day
  server-scored attempt. First-session/fresh-check milestones use real validated records.
  Thirty minutes includes ten minutes of review, which is not automatically marked done.
- Result offers evidence-gated, unseen-family five-question replay only when inventory permits;
  ownership/rate limits and launch checks remain authoritative. No generation or bank writes.
- Install/PWA support caches only three public fallback assets. Open-runner drafts preserve
  session identity, answers and deadline. Network submission freezes answers and supports
  bounded reconnect/reload without a new timer, debit or local score. Logout purges own drafts.
- Monthly cancellation now uses the installed Razorpay SDK's boolean argument and confirms
  rejected requests only through a matching terminal provider state. No provider operation ran;
  monthly activation remains gated because the plan ID is absent. One-time Pro access remains.
- Local dev restored at `http://localhost:3010/` with separate `.next-dev` output and disabled
  Turbopack development filesystem cache. The phone-blocking Next dev indicator is disabled.
  No reset/cache deletion/bulk revert. Earlier worker/cache/chunk failure logs are retained.
- Final build and lint passed; 172 automated tests passed, including question/payment/recovery
  contracts. 760 route/size/theme loads passed. New feature suite: 43 checks passed. Acceptance:
  37 forward/reverse wheel, clipped control/focus clearance, reduced-motion, 200%-text and iOS
  help checks passed. Rebuilt homepage: 20 size/theme checks passed; production PWA check passed.
  A concurrent autoplay timing run paused and failed; unchanged sequential rerun passed, both
  retained. Fixtures, browser touch and device emulation are not live persistence/hardware proof.
- Existing signed-in browser session inspected read-only: Today 20-minute plan → Practice setup,
  fixed-expiry Account, existing legacy Result and Review. No new attempt, score or debit.
  Opera/native-app access was unavailable; Gmail/OTP access was unnecessary and not performed.
- Remaining release gates: authenticated staging submission/resume and premium NTA with both
  skins, configured monthly plan plus sandbox billing/webhook evidence, physical Android/iPhone
  and screen reader. No deploy, migration, paid content generation, checkout or external message.

## 3 October 2026 — Pip intent and PrepOS refinement (Round 6)

Owner asked to preserve the good motion, make mascot actions contextual, reduce generic hero
details, strengthen PrepOS with its existing API/wallet and prepare next steps. Full handoff and
paste-ready Claude prompt: `CLAUDE-PIP-PREPOS-HANDOFF-2026-10-03.md`.

- Added one GPT-generated attentive pose with open eyes and relaxed arms. Removed sleep/wink
  defaults from scroll reading, pricing, comparison, Arena setup and loading. Original art stays.
- Pip points inward, including its static reduced-motion fallback. Single-face 140 ms entry
  replaces the overlapping-visors dissolve. Small scroll corrections retain the expression.
  Correct sample answers keep their hop; wrong answers receive an attentive nod. Keyboard
  answers trigger no mascot reaction. The Lab peak and mascot-free timed answering remain.
- Hero now states one fixed practice promise and leads with the actual five-question sample.
  PrepOS connects its next step with the record observation and an inspect/ask handoff.
- PrepOS Ask explicitly separates free record facts from optional one-credit model guidance.
  Source labels, receipts, wallet refresh, unknown-balance handling and same-ID retry are visible.
  Unresolved requests/conversations survive PrepOS section changes; late history cannot replace
  a new conversation. Effective paid expiry is recomputed using the shared entitlement rule.
  Explicit free requests cannot fall through to a paid model; new saved replies carry their source.
- Final build and lint passed. **172 existing automated tests passed** across recovery, question,
  payment, wallet, reservation, model lifecycle and other contracts. A final focused PrepOS rerun
  also passed all 26 tests. **147 browser report entries passed** at four widths and both themes:
  forward/reverse stations, inward pointing, one face, reduced motion, free/paid/unknown wallet
  states, lost-after-commit idempotent retry, keyboard/mouse reactions, wheel reversal and quiet
  companions with doubled root font size. Browser AI responses are labelled fixtures, not live
  model calls. Evidence and earlier failed test assumptions are retained in `artifacts/round6/`.
- Read-only configured Supabase check: wallet, ledger, reservation, runtime request and price
  tables answered. Funding table unavailable through the Data API (`PGRST205`); configured
  model prices not verified; available funding not established. Paid AI remains release-gated.
  Table readability does not establish RPC correctness or applied migration history. No migration
  was executed and no model/credit/budget call was made during this check.
- Public live PrepOS still shows its earlier public-guide/missions interface. That observation
  does not establish deployment of this checkout's guarded contracts. No outgoing email, paid
  educational generation, attempt/score fabrication, checkout or deploy. Port 3010 dev is left
  running; the temporary port 3011 production verification server is stopped.
- Next gates: resolve funding-table availability, verify actual schema/RPCs against saved SQL
  without blindly reapplying migrations, establish authorized runtime funding/current prices,
  reconcile wallets and run real staging concurrency/retry/release. Then consider activation.
  Durable client retry after reload/drawer closure, physical phones, screen reader and prior
  authenticated staging/payment acceptance remain unverified. This refinement preserves the
  retry ID across section changes only; it does not claim paid-request reload recovery.

## 5 October 2026 — Luna-only routing, shorter mobile home, light default, AI purchases

Source changes (not yet deployed; deploy needs `AI_LUNA_MODEL` optional and the Razorpay env below):
- **Model routing:** `src/services/ai/providers.js` now runs GPT-6 Luna only. `fast` tier = no reasoning, `smart` tier =
  low effort; callers that solve/generate questions pass `reasoningEffort` explicitly (medium+). Fallback is Luna, no
  reasoning. Question moderation (`src/lib/moderation/ai.js`) moved from a direct Claude call to the budget-guarded
  router, Luna at medium effort. `AI_FAST_MODEL`/`AI_SMART_MODEL`/`AI_FALLBACK_*` no longer route anywhere.
- **Homepage:** removed Subjects, Marquee, How-it-works, Proof band, mini tiles, Compass Pro box, college destinations;
  Instagram moved up under the statement; stats are now combined followers, reel views (owner-stated 100K+ floor,
  `REEL_VIEWS_FLOOR`) and recorded likes+comments. Product screens hidden under 700px. Mobile page 20.2k → 15.1k px.
- **Theme:** light is the default (`layout.js`); first-visit hint on the switch (`ThemeToggle hint`), shown once.
- **Payments:** `RELEASE_GATES.aiCommerce = true` (owner, 5 Oct); PrepOS top-up packs (₹10/50, ₹20/150, ₹50/400) now sell
  on `/pricing`. Monthly Pro ₹99 opens when `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set; create it with
  `scripts/payments/create-razorpay-plan.mjs`. Pro keeps 50 PrepOS credits/month, Free 10.
- Verification: `test:learning` 80/80, `test:recovery` 35/35, payment + landing tests 16/16; browser checks on 375px.
- **Unresolved gates:** Razorpay keys + plan ID + webhook secret are empty in `.env.local`; no real captured top-up or
  subscription charge has been verified; Vercel env not updated.

### 2026-10-21 — Website release 16 deployed (main 832e88031, deployment dpl_G17kKZkn2bw24a5SGL8xNaXHxv95, READY 1:40 am IST)
Rollback point: dpl_HsKRboUQsi1oUdC8ffrWV9QsnHpT (main 7f7e3f19f). No migrations. Env set before the deploy: RAZORPAY_PLAN_ID_PRO_MONTHLY_99 (owner's ₹99 monthly plan, D193/D197; the owner fixed the Razorpay webhook URL to https://www.mockmob.in/webhook) and MOB_LIVE_ENABLED=true (owner disabled Realtime "Allow public access to channels"; both clients use private channels).
Contains (owner 20 Oct 11:20 pm, D191): /pricing rebuilt like the app's Pro page with "Get Pro" everywhere (W1/W2); the phone hero as the app's lamp-lit welcome, desktop unchanged (W3); subjects-first onboarding with the Commerce preset (W4); the scroll statement bigger on phones with "marks slipped" copy (W5); Mistake Lab Time plays when it scrolls into view (W6); tour screens as devices with a charcoal surface in dark mode (W7); warmer invite copy mirroring the app; /api/auth/me carries deletionRequestedAt; lab fixture copy without "lost"/"last".
Verified before the push: test:app 985/989 then the 2 failures fixed (CRLF in hero-scene.css; a test that read a removed worktree), billing 453, mob 351, auth 125, recovery 637, subjects 38, today 120, dock 55, landing 81; eslint clean; next build --webpack ok; headless browser QA at 390 and 1440, Night and Day (no blockers; findings in tmp/v16-web/qa of wt-1020-web16). Smoke after the deploy: /pricing shows ₹99 a month + Get Pro, no first-free line; / shows the new hero scene; /mob, /onboarding, /cuet/accountancy, assetlinks 200; /api/mob 401.
Open (not regressions): the hero rotation phrase "See the lost marks." stays pending the owner's call (as D194); Day theme keeps dark product cards; dense text on /cuet pages; onboarding at 1440 left-aligned.

### 2026-10-19 00:45 IST: website release 10 LIVE (75ac3f23) and production migrations; final app v15.2 installed

**Live:** www.mockmob.in = main 75ac3f23 (fast-forward from 9b3661e8), Vercel dpl_Hj8uNjjdG7hGe287MhU1UUBmf7ev READY, 0 runtime errors in the first 15 min. Smoke (signed out): /, /pricing, /pricing/ai-credits, /wallet, /today, /mob, /review 200; /api/wallet, /api/attempts?view=summary, /api/me/credits 401; /api/billing/play/verify 404 (PLAY_BILLING_ENABLED off). The live pricing page carries "1 credit is 1 practice question or 1 chat reply; a full mock is 50 and deeper analysis is 3." No Play price on the web.

**Release 10 =** one credits balance core (D78), web wallet (/wallet, GET /api/wallet; Razorpay order/verify closed unless WALLET_COMMERCE_OPEN=true), web Pro nudges (D79-D81, D84), Google Play billing server (closed unless PLAY_BILLING_ENABLED=true), Today taste fixes (web/r10-taste), GET /api/attempts?view=summary (the app's list without the heavy snapshot; staging 29 MB -> about 0.8 MB).
**Checks:** lint 0; test:billing 326/326; test:app 756 pass, 1 skipped; test:learning 357/357; test:recovery 604 pass, 3 todo; test:mob 78/78; test:today 120/120; next build --webpack 0. One Opus verifier (head bbb163e7): NO-GO only on 2 copy HIGHs; all HIGH and MEDIUM fixed in 75ac3f23 (H1 resets line, H2 free back to 50, M1 Pro-only refund evidence, M3 true credit sentence, M4 cap lift only for bought-credit replies, M5 no top-up promise while closed, M6 no table read on timeout, M7 /pricing/ai-credits adds up). Not fixed (later): L2 Razorpay credit-pack refund clawback, L3, L4, L7.

**Production migrations (owner's standing grant), applied 19 Oct ~12:38-12:40 am IST, each dry-run on staging first:**
1. play_purchases (20261018190000): staging matrix passed (grant, replay, cross-account, revoke, double revoke, tombstone, Pro never shortened, Pro-only evidence). Pre-check: deps present, table absent.
2. one_credits_balance (20261018210000): pre-check production bodies spend_credits 911105fd, mm_ai_consume_credits c1ce92df, mm_ai_reserve_credits 499b44d1, mm_ai_release_credits 9c1d744b, reserve_runtime_ai f6026ff6 (= the undo file), 0 reservations breaking the new split check.
3. attempts_list_summary_fn (20261018230100).
**Post-check (md5 of prosrc, CR stripped) = staging for all 11:** attempts_list_summary cbf25393, mm_ai_consume_credits f43c5c1e, mm_ai_release_credits 8313e28a, mm_ai_reserve_credits 01e87c89, mm_bought_ai_credits_spent c728032b, mm_play_grant_purchase 83743a07, mm_play_revoke_purchase d3e2356d, mm_wallet_take ca977c24, mm_wallet_window c16763e6, reserve_runtime_ai c09163e9, spend_credits a2d71600. anon/authenticated cannot execute any; play_purchases RLS on, no anon/authenticated select; runtime_ai_budget student_bought_credit = 0.02.
**Undo:** supabase/undo/20261018{190000,210000,230100}*.undo.sql (code first for the core: the code probes for the functions).
**Flags (owner):** WALLET_COMMERCE_OPEN after his Razorpay test-card run; PLAY_BILLING_ENABLED after Play Console setup; PERSISTENT_LIMITS_ENABLED untouched.

**App:** v15.2 = ui/v15.2-1018 ab04b067 (1.0.15+7), release APK arm64 obfuscated prod.json, mockmob-next/tmp/apk/mockmob-v15.2-ab04b067.apk + .zip; installed on the owner's phone 10BF370PA6002XR (versionCode 7) at ~12:47 am. One fix pass over the final walk (15 HIGH, 11 MEDIUM): all HIGH fixed, MEDIUM all fixed; flutter analyze clean; unit suite 6,043 pass (the 1 failure was a stale string test, fixed). No golden suite, no second walk (owner D96).

### 5 October 2026 (later) — landing page restructure, feature tour
- Reverted the over-trimmed homepage: Compass Pro box, college destinations, stats band restored. Removed only the Subjects
  block (owner), the subject marquee and the three-step "how it works". Instagram stays where Subjects was.
- New `FeatureTour` (`src/components/landing/FeatureTour.jsx`, `src/app/feature-tour.css`): eight tools, one idea per slide,
  swipe on phones (scroll-snap), list + stage on desktop, autoplay with pause, only while on screen. Replaces the bento.
  Slides accept `video: '/demos/<id>.mp4'`; no recordings exist yet, so the animated screens play.
- Phone polish: glass header with progressive blur, floating glass dock, blur-in reveals (`.lp .rv`, reduced-motion safe).
- Reference studied: ug.preparoo.app (Webflow + GSAP; 7.1k px on mobile; one feature carousel, product mocks, sticky CTA).
- Tour v2 (same day): desktop is tool pills + a split stage (copy left, screen right); phones get equal-height cropped glass cards.
  Copy rewritten; Rival slide now says what it is (a fixed accuracy-and-pace target, not other students).
  `LiveStatsBand` drops a figure that fails to load instead of printing "Unavailable". Cause of the "unavailable" the owner saw:
  the preview dev server lacked `--use-system-ca` (TLS to Supabase failed); `.claude/launch.json` now uses it. Production unaffected.
- Tour v3 (same day): slides now use `TourScreens.jsx` + `tour-screens.css`, compact demo screens that play a scripted
  sequence each time their slide becomes active while the tour is on screen (timer ticks, options tapped, rows arriving,
  typing, bars filling), then hold the finished state; reduced motion shows the finished state. Nothing is cropped on phones.
  Verified frame by frame in a foreground Chrome (chrome-devtools) at 390x844 mobile and 1440x900: all 8 demos play and settle.
  Note: the desktop app's Browser pane throttles timers when hidden, so it is not reliable for checking motion.

## 4 October 2026 — UI/UX audit (audit-session date)

- Documentation-only audit saved to `docs/brain/UI-UX-AUDIT-2026-10-04.md`; raw evidence and screenshots in
  `artifacts/ui-ux-audit-2026-10-04/`. Independent visual and implementation reviewers completed before synthesis.
- Design health 26/40; technical health 14/20. Ten accepted groups: P0 0, P1 1, P2 8, P3 1. Highest priority:
  illustrative key agreement must not imply official correctness or explanation safety. Other priorities:
  phone journey/feature repetition, result mascot overlap and split percentage, touch/keyboard semantics.
- Homepage checked at widths 320/360/390/430/768/1024/1440/1920; all observed MockMob global widths fit.
  Public pages, 15 student fixture views, both themes, live home/signup and three live competitors sampled.
  Initial profile/test loading frames are not full-state verification. Incorrectly labelled initial desktop rows
  are retained as provenance and excluded; corrected 1440 measurements are the desktop evidence.
- Sampled answer feedback/focus, menu Escape, tour ArrowRight, timed palette, malformed email without sending,
  and long-name/empty/error fixtures. Contrast sampling had no eligible content-text failures within its limited
  coverage; gradients/animation and other unsupported cases were skipped. No whole-site WCAG certification.
- Detector ran once: 137 raw alerts, largely contextual advisories; no bulk theme/runner normalization warranted.
  Current aiCommerce=true supersedes the older closed-top-up assessment; target-size equivalent-control exception
  prevents declaring a definitive WCAG failure from dots alone. Both reconciliations are explicit in the report.
- No UI code changes, tests/builds, paid model calls, real attempts, migrations, auth completion, emails, payments or
  deploys performed. Existing dirty tree/dev server preserved. Audit tabs and temporary viewport overrides cleaned up.
- Open gates: real phone keyboards/safe areas, screen reader, 200% text zoom, full hover/focus/reduced-motion matrix,
  background interruption and budget-device/slow-network performance; authenticated persistence/payments/AI receipts.
  Live landing differs from local; this audit does not establish deployment of the new feature tour or configured AI.

### 4 October 2026 — owner-selected UI/UX implementation plan

- Saved `UI-UX-IMPLEMENTATION-PLAN-2026-10-04.md` and linked it from the brain README/audit.
  Owner retains official-key trust wording; wording-first audit priority is superseded for this sprint.
- Order: reproducible baseline → phone performance/composition → accessibility → student/error states
  → activation flow → final measurement and release evidence. Cosmetic detector cleanup, unused demos,
  arbitrary competitor page-height targets and blanket motion/feature removal are excluded/deferred.
- Current source review found held/not-explained repair outcomes enter the Result `repaired` set, which
  drives a Repaired badge. Plan requires fixture reproduction and separate handled/outcome states;
  no runtime reproduction or fix is claimed in this planning pass.
- Planning only: no UI edits, performance runs, tests, paid calls, migration or deployment performed.
  Performance acceptance separates controlled production-build traces from real-user Core Web Vitals.

### 4 October 2026 — UI/UX plan implementation

- Implemented phone hero/sample composition; tour carousel controls, inert slides, focus/manual pause,
  bounded pausable demo timelines, hidden/offscreen gating and 44px controls; official-key wording retained.
- Practice setup now precedes supplementary commentary/statistics and no longer waits for optional panel
  reads. Pending/unavailable counts are explicit; matching/expiry/idempotent server quote guards remain.
  Scoped load retry retains choices; phone summary exposes subject, mode, count, time, marking and cost.
- Result mascot height/entrance and metric units fixed; distinct explanation/held/unexplained outcomes,
  handled queue vs explanation progress, retained visited answer state across collapse/filter, and safe
  same-ID retry/in-progress/released handling. No scoring, wallet, model, budget or entitlement changes.
- DU category arrows/Home/End and clear focus fixed; editable phone/tablet fields 16px; key targets 44px;
  transform progress bars; one main in timed runner and PrepOS.
- Baseline/final production builds and final lint passed; 179 tests passed (35 recovery, 80 learning,
  59 payment/question/NTA/DU, 5 new UI state tests). Final key-route light 320/390/768/1440 and dark
  320/390/1440 matrices have zero horizontal overflow and no result mascot/metric overlap.
  Fixtures cover distinct repair outcomes, pending/error states and retained held panels. Browser
  checked DU keyboard, menu Escape focus return, sample feedback, tour freeze and one-main wrappers.
- Local production preview on 3020 checked public home, themes and sample; existing authenticated
  setup was read-only. Signup redirected to setup, so current-run native email validation is unverified.
  No new real session/paid repair/payment/signup completion, data migration or deploy performed.
- Several local inventory reads took 7.5-11s and had blocked setup; dependency removed and tested with
  never-resolving-statistics fixture. No device speedup, Core Web Vitals or field gains claimed.
- Full evidence/open gates: UI-UX-IMPLEMENTATION-RESULTS-2026-10-04.md and
  artifacts/ui-ux-implementation-2026-10-04/. Physical phone, screen reader, actual 200% zoom,
  reduced-motion browser/full contrast matrix, controlled throttled traces/field CWV, real transaction
  receipts and production deployment remain open. Measurements cannot be replaced with screenshots.
- Existing checkout changes retained. Diff check only reported the pre-existing ProductScreens.jsx EOF
  blank line. Do not bulk-reset/revert these files; review the scoped implementation hunks.

### 4 October 2026 — authorized UI production release preflight

- Owner requested publication of the UI changes. The staged release includes the reviewed landing/tour,
  mobile/accessibility, dashboard, result/repair presentation and DU refinements with their source dependencies.
- Existing AI-routing/moderation, aiCommerce enablement, pricing, payment scripts and corresponding
  backend-test edits are excluded and retained locally. This release does not activate new commerce,
  change model routing, migrate data or call a paid model.
- Exact staged source tree `7cfe2abf1d958767fb32f5bcd270560900cddd58` was exported independently:
  production build and lint passed, with 179/179 recovery/learning/payment/question/NTA/DU/UI-state tests.
  Evidence: `artifacts/ui-ux-release-2026-10-04/`. Shared dependency junction was rejected by Turbopack;
  the successful build used a real dependency copy. No application workaround was introduced.
- Push/Vercel readiness and live-domain/mobile/desktop smoke are pending at this preflight entry.
  Hardware, screen-reader, measured throttled performance/CWV and real transaction gates remain open.

### 4 October 2026 — UI release live verification

- Pushed `f70e385909ff454f10bf83e60d96a6883bb31c17` to `origin/main`. `Vercel – mockmob`
  reached success at `2026-10-04T12:50:34Z`; deployment:
  https://vercel.com/atishay07s-projects/mockmob/6VA6xyZTYuXB87urHXQLAgeusbAx.
- `https://www.mockmob.in/` serves the new tour, short hero lead and sample CTA with HTTP 200.
  Apex redirects once (307) to www, then 200. Calculator returns 200; no redirect loop.
- Live home light/dark checks at 320/390/1440px: no horizontal overflow, one main.
  Sample CANDID/Frank feedback works; selecting Mistake Repair pauses the tour with one active,
  seven inert slides and 44x44px controls. Live calculator at 390px: category ArrowRight selects
  and focuses OBC-NCL with one tab stop; clear empties search, restores focus, and input is 16px.
  No captured browser error logs in this smoke. Phone and desktop screenshots saved.
- Evidence: `artifacts/ui-ux-release-2026-10-04/{github-status.json,live-http.json,live-ui.json}`
  and build/test/lint logs. This post-deployment receipt is a local status update; deployed source
  and preflight documentation are in the release commit above.
- Existing unrelated AI/commerce/payment edits remain local. No production migration, paid model
  call, real attempt, purchase or signup completion was performed. Physical devices, screen reader,
  actual zoom, controlled performance/field CWV and real accounting receipts remain unresolved.

### 4 October 2026 — guided tour follow-up

- Owner rejected the phone dropdown and easily interrupted/slow feature playback after the UI
  publication. Rebuilt the tour as an automatic 4.8-second chapter sequence with shared progress,
  explicit Pause, a chapter strip and an Up next nudge. Normal vertical browsing no longer turns
  rotation off. Pointer navigation resumes its cycle; horizontal input holds briefly while settling.
- Preserved keyboard reading holds, explicit resume, reduced motion, inactive-slide isolation and
  hidden/offscreen suspension. Phone product panels fit without overhang; the sample dock steps
  aside during the tour. Nearby Mistake Lab stages also use 4.8 seconds. Official-key copy retained.
- Final isolated application source build and lint passed; nine relevant tests passed. Both-theme
  320/390/768/1024/1440 matrices have zero root overflow, no screen overhang and 44px controls.
  Browser observed auto progression/loopback, scrolling/navigation without sticky pause, explicit
  pause, and keyboard hold/resume. No measured wall-clock/FPS/device performance claim.
- See `TOUR-REFINEMENT-2026-10-04.md` and `artifacts/tour-refinement-2026-10-04/` for details.
  Production readiness/live smoke pending at this entry. Physical phones, screen reader and CWV
  gates remain open. Unrelated AI/commerce/payment edits retained locally; no migration/paid call.

### 4 October 2026 — connected preparation suite verified for rollout

- Implemented shared Today sequence, Learn, server-scheduled Recall, durable versioned runs/events,
  separate study progress, selected subjects/time, Pro weekly plans and custom mixed recall.
  Mobile Today/Practice/Learn/Review retains the other destinations through More. Active sessions
  and due checks replace their plan blocks; a persistent full-mock shortcut retains the existing
  quote/eligibility/credit path. Teaching/card exposure excludes those families from fresh checks.
- Owner explicitly authorized current Supabase project `isrxrxzjocewrdureyhp` with existing data.
  Saved migrations and isolated dry runs preceded SQL-editor application of score-recovery,
  connected-learning and study foundations; the published-version backlog follow-up also applied.
  The original transaction verified existing questions/attempts/credits/entitlements/credit receipts
  unchanged. Current service-role retry/scheduling/stale-revision smoke passed and rolled back all
  verification writes. CLI migration history remains unreconciled; do not blindly reapply pending SQL.
- Published two units and 23 cards: English twenty-word deck and sacrificing/gaining ratios.
  Canonical hashes and anonymous table denial verified against the current project. WordNet license
  preserved; NCERT formula/source reconciliation and exact arithmetic passed. This does not release
  formal recovery pathways or certify academic calibration, exam fit, mastery or score gains.
  Remaining four-subject coverage is visibly pending; offline packs and curriculum expansion remain.
- Clean isolated release excludes owner's unfinished pricing/provider/AI-evaluation/payment-script/
  landing edits. Lint and production build passed. 166 distinct tests passed: recovery 35, learning
  80, answer integrity 6, NTA 22, payment entitlements 12, study 11. Final plan changes passed study
  tests again; final mock/lesson links passed targeted lint and production rebuild. Complete local
  four-migration/import/retry/runtime dry run passed. Authenticated browser saved/resumed/completed
  the English lesson, persisted/reloaded a recall rating and saved/restored time preferences.
- No paid model calls. Existing Free/Pro prices, entitlements, atomic credit RPCs and AI allowances/
  persistent $50 generation and $25 monthly runtime guards unchanged. Only three independent study
  flags were saved as true in production on the domain-verified Vercel `mockmob` project.
  Publication/live verification pending at this entry; local build is not proof of deployment.
- See `STUDY-SUITE-2026-10-04.md` and local `artifacts/study-suite/` receipts. Real Android/keyboard,
  screen reader, actual 200% text/zoom/reduced-motion settings, field CWV and delayed unseen-question
  outcomes remain unverified. Rollback disables study flags and retains learning records.

### 4 October 2026 — preparation suite published

- Commit `a6a61cc276d9df36b43e4760c08df0dfe83802a3` is on `origin/main`.
  Domain-verified Vercel project `mockmob` deployment is Ready:
  https://vercel.com/atishay07s-projects/mockmob/FeimHt2rAGpA3qG4Eepoqfa43PNJ.
  Vercel showed 49 seconds and 23:21:17 IST on 4 October. Production flags are enabled.
- Live HTTP smoke passed: apex 307 once to www then 200; www and Learn 200; anonymous
  study catalog 401; dev-only study preview 404. Public Learn redirects signed-out users
  through existing authentication. Live signed-in browser check awaits owner Google sign-in;
  the Google chooser shows the existing account signed out. No credential was generated,
  transferred from localhost or changed to bypass login.
- Authenticated current-project readback passed: English lesson complete, recall cursor one
  after the first card, answer hidden on the next card, one persisted FSRS review whose due
  date matches the run receipt, and original twenty-minute preference restored. Actual
  owner QA records remain resumable; they are not student outcome evidence.
- Final authenticated release library and recall checks across 320/390/768/1024/1440 plus
  short landscape showed zero root overflow and no study buttons/links below 44px. Dark
  phone library also had no overflow. Full-mock shortcut selected the existing Full Mock
  and displayed its access quote without starting or charging a practice session.
- Evidence: `artifacts/study-suite/{production-release-receipt.json,production-deployed.png,
  live-http.json,authenticated-study-receipt.json,responsive-release-library.json,
  responsive-release-recall.json,phone-library-dark.png}`. This post-release receipt remains
  local; application source and pre-release verification status are already published.
- Original dirty checkout and unrelated owner edits remain intact; release checkout/branch is
  `artifacts/study-suite/release` / `codex/connected-study-suite`. Original local main still
  points at its prior commit; reconcile intentionally before later publishing owner edits.
  Full curriculum/offline packs, formal calibration, CLI migration-history reconciliation,
  physical-device/assistive-technology/200%-zoom and field performance/outcome gates remain open.


### 4 October 2026 — signed-in preparation-suite production smoke passed

- Owner completed normal Google sign-in. Live library rendered both English and Accountancy
  units, existing Pro access, the completed lesson and recall progress. The existing recall run
  resumed at card two. A live reveal was saved and survived page reload; its answer, optional
  pronunciation, linked lesson and four rating controls rendered correctly. No scored session,
  practice-credit charge, purchased-entitlement change or paid AI call was made.
- Actual live library viewport checks passed at 320/390/768/1024/1440 and short landscape.
  Revealed recall passed at 320/390/1440 and short landscape. Each measurement asserted actual
  width/height, zero root overflow and no study buttons/links below 44px. No error logs were
  captured in the final live test tab. Earlier viewport results that targeted the build-queue
  tab were discarded and replaced with these measurements; they are not release evidence.
- Evidence: `live-responsive-library.json`, `live-responsive-recall.json`, `live-phone-library.png`,
  `live-phone-recall.png` and updated `production-release-receipt.json` in `artifacts/study-suite/`.
  Physical-device, assistive-technology, actual zoom/reduced-motion, field performance and
  curriculum/calibration/offline/history-reconciliation gates listed above remain open.


- Final signed-in live Today showed the same resumable study run, twenty-minute preference and
  the 4/6/10-minute sequence plus full-mock shortcut. Temporary viewport overrides were reset.


### 5 October 2026 — Learn rebuilt as one connected loop; content v2 across four subjects

Owner feedback: "Even I cannot understand what Learn actually does." Diagnosis from the live/local walk-through:
Learn opened on "Start recall" before anything was taught; the English "lesson" taught the recall method and no
words; cards were bare dictionary definitions; lesson completion did not lead to recall or practice; starting a
second lesson silently resumed the first (the database resumes any active run of the same mode).

What changed (branch `codex/connected-study-suite`, on top of a6a61cc):
- One loop per concept, stated everywhere: **Learn (5–7 min) → Lock it in (2–3 min recall) → Apply (chapter
  practice with marks)**. Learn home gives one next action (continue / due review / recommended lesson, subjects
  rotated by fewest lessons read or by recent practice mistakes), then subject → chapter → concept with status,
  "practice available, lessons later" for untaught chapters, study record and mock shortcut.
- Lesson overview: objectives ("You'll be able to"), "How CUET asks this", three-step status, contents, sources.
- Lessons: idea, formula, method, worked example tables, common-mistake callouts, word sets with WordNet examples,
  numbered practice passages; quick checks with per-option "why that is wrong" feedback. Completion screen offers
  Lock it in (that lesson's cards), then Practise <chapter> (`/dashboard?subject&chapter&mode=quick&count=10`).
- Recall: one card = one memory with rotating task variants (meaning in context, gap fill/spelling, synonym or
  opposite; numeric/ratio calculations; scenario classification). Answers checked exactly (equivalent fractions,
  ratios in lowest terms, ₹/commas, British/US spelling from the source). After each card: when it returns.
  Summary lists remembered/forgot with next review, reread links and the Apply step.
- Server: `set_aside` transition closes an older active session (history kept, nothing introduced) when a
  different lesson or focused recall starts; same request resumes. Per-unit memory status, lock-in availability,
  explicit `DAILY_NEW_LIMIT_REACHED` / `NOTHING_DUE`. Unchanged: 5 new cards per IST day, >20 overdue pauses new
  cards, FSRS 5.4.2 defaults at 0.90, append-only events, revision checks, DB-enforced daily limit, RLS/grants.
- Today steps carry purpose, minutes and what "done" means; practice step links the recommended chapter.
  Result page Repair step links every mistaken chapter that has a lesson (count + minutes). Review/Progress
  study card reworded. Homepage tour gains a flag-gated Learn slide; its counts come from `release.json`.

Content v2 (released 14 units / 65 cards / 179 task variants; zero paid model calls):
| Subject | Units | Chapters with lessons |
| --- | --- | --- |
| English | 6 vocabulary sets (30 WordNet words; 10 new) + main idea + stated/inferred | Vocabulary, Factual Passage, Narrative Passage (3 of 7) |
| Accountancy | sacrificing/gaining ratios (v2), revaluation | Change in Profit Sharing Ratio, Admission of Partner (2 of 16) |
| Business Studies | delegation/decentralisation, planning/controlling | Organising, Controlling (2 of 13) |
| Economics | what GDP counts (final goods, value added, GVA/NVA, non-monetary), nominal/real/deflator | National Income & Related Aggregates (1 of 18) |
All eight concept blueprints now have teaching units. This is **not** full syllabus coverage and does not release
formal recovery pathways or assessment families.

Validation (`scripts/learning/validate-study-content.mjs --write --strict`): every number recomputed
independently; WordNet meanings/examples/synonyms/antonyms re-derived from hashed source lines (licence kept);
NCERT reconciliation phrases found on cited PDF pages (leac102 p.3,5,6,30,31; leac103 p.3; leec102 p.3,10,21,23;
lebs105 p.20,26; lebs108 p.5,6,8; PDFs downloaded with owner approval, sha256 in registry, git-ignored);
original reading passages checked for evidence/not-stated/key structure; family IDs disjoint from recovery
pathways. Tamper tests prove changed arithmetic, definitions, relations, reading keys and answer keys quarantine.

Production data (owner-authorised project isrxrxzjocewrdureyhp): phase 1 insert-only applied 5 Oct via
`scripts/learning/apply-study-content-v2.mjs insert` after the PGlite dry run
(`artifacts/study-suite/content-v2-import-dry-run-report.json`: idempotent, invisible to old code, changed
same-version content refused, supersede quarantines not deletes, stale run invalidated with event, unrelated
data unchanged). Receipt: 14/14 units, 65/65 cards present and hash-matched. Phase 2 (`supersede`, retires
english-vocabulary-01@1 and accountancy-sacrificing-gaining@1) runs only after the v2 deploy is live.

Verification (local, release checkout): tests recovery 35, learning 80, study 19, answer-integrity 6, NTA 22,
payment entitlements 12, landing/UI 9 — all pass; full lint clean; production build passes. Fixture walk-through
(dev-only `/preview/study`, real engine and scheduler) and **owner-signed-in walk-through on production data**
on localhost: revaluation lesson resumed at step 3 after reload; triple click advanced one step; stale second-tab
event returned 409 with server state unchanged; wrong choice explained; "₹3,000" accepted; completion → Lock in 5
cards → summary with next review times → reread link → practice opened with Accountancy / Admission of Partner
preselected and "Included" (nothing started or charged); different lesson set the earlier one aside, same lesson
resumed; Today led with the unfinished lesson. 320 px library/overview/lesson: zero overflow, no study targets
<44 px; wide comparison tables stack on phones. Both themes checked. These are owner QA records, not student
outcome evidence.

Still open: real budget Android with keyboard, physical screen reader, actual 200% zoom/OS reduced motion, field
Core Web Vitals, delayed unseen-question outcomes, comprehension testing with real students, offline packs
(print summary only), remaining chapters, CLI migration-history reconciliation. Device TTS pronunciation is
labelled as device voice; no licensed pronunciation source is bundled.

Rollback: set STUDY_CONTENT_ENABLED/STUDY_RECALL_ENABLED/STUDY_GUIDED_PLAN_ENABLED to false and redeploy (records
kept), or `git revert` the release commit and redeploy. If phase 2 has run and the old code is restored, set the
two v1 units back to `published` (no deletes are needed; v2 rows are ignored by the old release proof).

### 5 October 2026 — Learn v2 published

- Commit `78a627f` pushed to `origin/main`; www.mockmob.in served it about 80 s later. Live HTTP: home 200 with
  the flag-gated Learn tour slide, `/learn` 200, anonymous study catalog 401, dev preview 404.
- Content phase 2 applied after the deploy: english-vocabulary-01@1 and accountancy-sacrificing-gaining@1
  quarantined (v2 published); the correction trigger invalidated the 5 owner QA runs on v1, one event each; no
  deletes. Receipts: `artifacts/study-suite/v2/apply-{insert,supersede}-receipt.json`, `live-receipt.json`.
- Signed-in live check (owner Pro account, 375px): Learn led with the unfinished lesson and due cards; the
  lesson completed with check feedback and the daily new-card limit message; Organising practice linked.
- Local `main` in the original checkout still points at 6c5e05b with the owner's uncommitted work; it is now
  three commits behind `origin/main`. Reconcile deliberately before publishing those edits.

## 5 Oct 2026: Key Review + NTA integrity guard + Luna routing
- Key Review: when Mistake Repair's solve and blind second check both disagree with the key, the student sees an
  acknowledgement ("We may have got this one wrong") with who picked what, plus a result-page log of held keys.
  A reload shows the same panel via `question_under_review`. Marks are NOT changed automatically; copy says so.
  No migration, no extra model calls.
- NTA integrity guard: leaving the tab/window = strike; warnings 1-2 show an animated modal, strike 3 submits the
  session. Strikes persist across reload (`<session key>:integrity`); copy/paste/context menu blocked. Browser-side
  deterrent only: strikes are NOT sent to the server (attempt events accept only answer/visit), so there is no
  server-verified proctoring record.
- Also shipped: GPT-6 Luna-only model routing (providers.js, moderation/ai.js, live-eval scripts).
- Deliberately NOT shipped: AI top-up opening (RELEASE_GATES.aiCommerce, pricing pages) from the local tree; needs an explicit owner go-ahead and Razorpay keys.
- Verified: unit tests and eslint (see commit); preview walkthrough of both flows. Not verified: real multi-window/mobile
  app-switch behaviour, signed-in NTA run, live Luna calls.

## 6 Oct 2026: Key Review / NTA release verification
- Prepared an isolated normal checkout from 82d3341 (base origin/main 23ac1dd), preserving the owner's dirty main checkout.
- The handoff commit omitted seven new component/data/test files plus package.json and this status entry. Recovered these exact files from the handoff worktree; no AI commerce, pricing, artifacts, study-suite edits or migration included.
- Removed a duplicate question_under_review response handler; corrected the illustrative held-response fixture so both checks actually disagree with its key.
- Actual checks: npm run build passed with physical node_modules (Next.js 16.2.4 / Turbopack); eslint passed; test:learning 84/84, test:recovery 35/35, answer-integrity plus payment-entitlements 18/18 passed. No paid-model invocation or production-data migration performed.
- Earlier preview interaction evidence is from the handoff, not repeated in this release check. Browser-only strikes are not a server proctoring record. After reload, Key Review is returned on a repair request for the already-held question; the result-page log is rebuilt from those responses.
- Deployment is pending the non-forced main push and Vercel verification. Live Luna compatibility, signed-in NTA, real mobile/multi-window focus behaviour and captured AI top-up checkout remain unverified. AI top-up purchasing remains closed.
- Rollback: revert the feature commit and release-completion commit; no database rollback is needed.
### Production publication evidence (6 Oct 2026)
- Published 82d3341 plus completion commit d2e3f2b to GitHub main by non-forced fast-forward from 23ac1dd.
- GitHub check `Vercel – mockmob` succeeded for d2e3f2b. Production deployment 6868841235 succeeded at https://mockmob-9stt6no29-atishay07s-projects.vercel.app (Vercel dashboard: https://vercel.com/atishay07s-projects/mockmob/BXoio53KjaFuPBdUUJ49fc4Sqnxc).
- Post-deploy live checks: apex https://mockmob.in redirects to https://www.mockmob.in/ with final HTTP 200; www homepage and /pricing return 200; unsigned /test redirects to /signup with final 200. No redirect loop observed.
- These checks confirm production publication and public entry routes; they do not prove authenticated Key Review/NTA interactions, physical-device focus handling, live model compatibility or payment capture. Those gates remain as recorded above. Other duplicate Vercel projects attached to the repo are outside this live-domain release verification.

## 6 Oct 2026: corrective NTA fullscreen and answer-change audit
- Owner reported that fullscreen rehearsal and confirmed-key correction UX were incomplete. Audit and source-backed question findings: docs/brain/reports/KEY-REVIEW-NTA-CORRECTIVE-AUDIT-2026-10-06.md.
- NTA now requests actual fullscreen, requires re-entry after warnings, counts one absence once, persists strikes per session, submits on warning 3, removes the in-app Exit shortcut, locks answering behind native themed dialogs and exposes failed-submission retry. Browser/OS exits remain possible; unsupported browsers disclose a focus-only fallback. Timer deadlines are unchanged.
- Results now hydrate changed/held questions from current server records on reload. Confirmed corrections show an apology, corrected answer/explanation/source and separate marks adjustment; unverified changes do not claim correctness. Old snapshots/account/leaderboard scores remain intact. No paid model calls on reading corrections.
- Exact screenshot question is already D in production (dea6e298-269e-4b18-afd4-53c0b3be7cf5). Source-backed matching display receipt confirms D; pick B stays wrong, adjustment 0. No production data update or migration performed. The historical A-to-D change has no returned version-history receipt, so its timing/provenance is not claimed.
- Verified: learning 91/91, recovery 35/35, answer-integrity/payment-entitlements 18/18, eslint and production build. Isolated Chrome exercised real fullscreen entry/exits, warning progression, reload persistence, auto-submit, failure/retry, denial, and Quick Practice. Desktop/390px mobile compositions inspected; controlled visibility/blur events reached the real hook. JSON/screenshots retained locally in artifacts/corrective-checks/.
- Remaining: corrective deployment verification, signed-in production result/NTA, real OS/tab/window switching, physical phones, screen readers and live Luna. A real headless tab switch did not expose focus change; synthetic events are not hardware proof. Strikes remain browser-only. AI commerce stays closed; entitlements and atomic RPCs untouched.
- Rollback: revert the corrective code commit. No database rollback needed.

## 13 Oct 2026 - NTA session state (fix/nta-mode)
- Mark for review is now an event (`type: 'mark'`, `marked: true|false`) in the session log, saved like answers: durable sessions keep it on the server and rebuild it on resume (`progressFromEvents`, data/session_draft.js); the scored timeline never contains marks. Old local drafts add their marks to the log on first load.
- Device-ticket clock: the server signs the start time in a start receipt (`meta.startReceipt`, data/practice_ticket.js); the runner keeps it in the page address (`startReceipt`), and a start with the same key and the receipt returns the original start and deadline instead of a new clock. Past the 2-minute grace it answers SESSION_EXPIRED; a forged, edited or foreign receipt answers INVALID_START_RECEIPT. Limit: a start with no receipt is a new session (a first start or a new key), and a receipt lost with the address (other device) cannot be recovered; durable mode (LEARNING_SESSIONS_ENABLED=true) has no such limit.
- Option layout: the session stores `selection_meta.ntaOptionLayout` ({order, key, shuffled}) from the engine's `nta_option_order`; a paper whose remapped key does not point at the served option is refused before a session or a credit exists.
- Tests: data/tests/nta_session_state.test.mjs (test:nta), data/tests/nta_e2e_state.test.mjs (test:nta-e2e), plus a mark test in recovery.test.mjs.

### 2026-10-17 about 2:35 am IST - Per-user AI cap and two-model allowlist APPLIED on production

- Migration 20261017120000_runtime_ai_user_cap applied to production (isrxrxzjocewrdureyhp) under the standing grant, after a staging dry run and an independent verifier pass.
- Post-check: runtime_ai_requests.user_id exists; reserve_runtime_ai now takes 7 arguments; anon cannot execute it.
- Owner decision (17 Oct, 2:15 am): the paid cap is Rs 5 a month, so `update runtime_ai_budget set monthly_cap_usd=0.0568 where id='student_user_paid'` ran right after.
- Caps now: student_ai 25 (global, unchanged), student_user_paid 0.0568, student_user_free 0.0114.
- Undo: supabase/undo/20261017120000_runtime_ai_user_cap.undo.sql.

### 2026-10-14 13:43 IST — Authored wave 1 published to production (owner approved in chat)
- 475 questions and 12 passage groups inserted (source `claude-authored-2026-10-14`) with `scripts/question-publish-authored.mjs --mode=apply`; plan hash 39a4b051… and candidates sha 18b27c06… matched the runbook exactly; read-back: missing 0, notVisible 0, hashMismatch 0.
- Live before → after: chemistry 281→376, english 269→327, history 192→273, political_science 191→272, psychology 82→161, sociology 199→280.
- Visible in practice and full mock now. NOT in NTA mode until engine r5 (fix/nta-mode, not deployed) ships; not in Explore (no question_scores rows).
- Restore: `node --use-system-ca scripts/question-publish-authored.mjs --mode=restore --restore=docs/brain/reports/authored-publish/authored-publish-restore-2026-10-14T08-12-59-785Z.json --expect-project=isrxrxzjocewrdureyhp` (default hides; keeps attempt history).

### 2026-10-14 23:59 IST: production diagnosis via Supabase MCP, and one config row applied
- **Owner grant:** standing authority for MockMob database work (AI OS decisions log, 14 Oct).
- **Diagnosis (read only, production isrxrxzjocewrdureyhp):**
  - **Volume:** 11 Mistake Repairs in 14 days, by 2 accounts.
  - **4 Oct:** 5 of 7 explained, all on gpt-4.1-mini.
  - **Since the Luna-only deploy (5 Oct 21:01 UTC):** every repair (4 of 4) released as unusable_output within 0.7 to 2.4 s.
  - **No model call reached the runtime guard:** no runtime_ai_requests row exists after 4 Oct 20:25 UTC.
  - **Not the guard or budget:** the cap is fine ($0.011 of $25, not paused), no credits are stuck, and a rolled-back call to reserve_runtime_ai('openai','gpt-6-luna') returns dispatch true.
  - **Cause:** Vercel Production env. Either OPENAI_API_KEY is missing (getOpenAIClient returns null, giving provider_unavailable), or AI_REPAIR_MODEL names a model with no price row.
  - **Open:** the owner checks Vercel env. The fix branch's per-failure log line will name the cause once deployed.
- **Applied:** migration 20261014183050 runtime_ai_price_claude_haiku_5_5 (one config row; undo: `delete from public.runtime_ai_prices where provider='anthropic' and model='claude-haiku-5-5'`). This lets the Haiku 5.5 fallback in fix/repair-reliability run once deployed. No student data was changed.

### 2026-10-15 00:18 IST: authored wave 2 published to production (owner approved in chat)
- **Dry run:** plan hash 73b63070..., the same as the reviewed plan. 0 blockers, 0 warnings. 382 bound to both the agent and fit tables, 0 lookalikes.
- **Apply:** source claude-authored-2026-10-14-w2. 382 questions and 1 case-set group inserted, 0 missing, 0 not visible, 0 hash mismatches.
- **Live counts:**

  | Subject | Before | After |
  |---|---|---|
  | Biology | 360 | 416 |
  | Computer Science | 311 | 387 |
  | English | 327 | 382 |
  | General Test (gat) | 150 | 227 |
  | Geography | 179 | 223 |
  | Mathematics | 267 | 332 |
  | Political Science | 272 | 281 |

- **Restore file:** docs/brain/reports/authored-publish/authored-publish-restore-2026-10-14T18-48-05-150Z.json (`--mode=restore` hides wave 2 only).

### 2026-10-16 about 15:25 IST — NTA index: applied, built, rolled back (signature mismatch), fix in progress

- 14:00 IST: `nta_question_index` applied to production under the standing grant (RLS on, service role only) and built with `scripts/nta-index-build.mjs --write --allow-production`: 653 rows (english 173, accountancy 135, business_studies 181, economics 164). `CUET_EVIDENCE_SIGNING_KEY` was already in Vercel production; Vercel's own nightly snapshot verified the same 653 evidence records, so the keys match.
- The read-only `scripts/nta-engine-run.mjs` then showed every index row rejected as `score_signature_invalid`: Accountancy and Business Studies could not start an NTA paper, Economics fell to 45 questions.
- 14:55 IST: rolled back with `truncate public.nta_question_index` (the runbook's switch-off; the table stays). The engine run after it: Accountancy 3 of 3 papers (57 factory + 713 agent eligible), Business Studies 3 of 3 (56 + 71), Economics 3 of 3 at 50. English cannot start, as on 13 Oct (separate cause).
- Exposure: 0 attempts completed on production from 14:00 IST to 15:20 IST, and no NTA log lines from 14:33 (Hobby keeps 1 h), so most likely no student hit it.
- Cause (suspected, being proven on staging by branch fix/nta-index-sig-1016): `ntaIndexSignedBody` signs `verified_at` and `luna`/`gemini` as the builder holds them in JS, but PostgREST returns timestamptz as `+00:00` and numeric(4,2) rounded, so the canonical JSON differs. Tests used fakes that returned the builder's own values. Do not rebuild the index until that fix is deployed and the engine run shows `poolSource` index with 0 signature failures.

### 2026-10-16 about 13:50 IST — Security: the question bank closed to the public anon key (production)

- Found by the 16 Oct security review: `public.questions` kept Supabase's default grants for `anon` and `authenticated` plus the policy "anon read live questions", so anyone with the browser's public key could read all 8,196 live questions with answer keys, explanations, evidence and internal fields straight from PostgREST.
- Checked first that nothing needs it: every server read uses the service role (`src/lib/supabase.js`), the browser client and both apps use Supabase only for sign-in.
- Applied under the standing database grant: `supabase/migrations/20261016141000_questions_private_to_browser_roles.sql` (revoke all from anon and authenticated; service_role keeps all). Staging dry run first; undo `supabase/undo/20261016141000_questions_private_to_browser_roles.undo.sql`.
- Verified on production: grants now postgres and service_role only; `/rest/v1/questions` with the anon key answers 401 `permission denied for table questions`; with the service role 200; www.mockmob.in `/`, `/pricing`, `/api/stats` 200.
- Still open from the review: PERSISTENT_LIMITS_ENABLED (rate limits per instance), `/api/questions/feed` sends keys to signed-out callers (owner decision), revoke default grants on other RLS-only tables (defence in depth), the low items in the review.

