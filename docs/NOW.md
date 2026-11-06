# NOW: MockMob current state

## 6 Nov 2026, about 1:05 pm IST — Round 4 live (main 068a7a061, dpl_34h9RLVRZwqfGwEZ62R93vu4kR7q)

- Round 4 (LK117-LK147, LK150) is on www.mockmob.in. Runtime is `06aed8557`; `068a7a061` adds only the corrected source assertion (outside touches checked in `onTouchStart`) and the STATUS gate note.
- Gate on the 06aed8557 build: landing suites 437 pass / 0 fail; eslint clean on all changed files; 22 swipes at 4x CPU over100 = 0 cold (max 97 ms) and warm (max 97 ms); matrix 128/128 at 390; all 72 section captures (390/1440, Night/Day) looked at. The 1440 Key cards shots caught the count-up mid-roll; it settles on 16,458.
- Live check: Vercel READY and the production alias points at the matching SHA; no private runtime errors in the 15 minutes after; www.mockmob.in at 375 px renders, no horizontal scroll, no console errors.
- Not exercised: signed-in use, production sample data, a physical phone, a screen reader. App 1.0.21+19 still awaits the owner's Play upload. Financial Markets Key cards still untouched.

## 6 Nov 2026, about 3:16 am IST — Round 4 integrated and paused at the owner's request

- Round 3 is live on `400d647a8`. Round 4 is committed locally on `web/r4-release` in `wt-1104-web-polish`, with runtime tip `06aed8557`. All six web packets are merged.
- Both final builds and the App suite passed. The last runtime revision still needs the source assertion updated, the full cold/warm and gesture runs, and the final visual sweep. Private Vercel access now works.
- Resume using [the detailed handoff](HANDOFF-2026-11-06-ROUND-4-RELEASE.md) and [next-session prompt](PROMPT-NEXT-SESSION-2026-11-06-ROUND-4-RELEASE.md). App build 19 awaits the owner's Play upload.

## 6 Nov 2026, about 12:40 am IST: stopped at ~90% weekly usage; round 4 saved on branches (not live); next session prompt written
- Live: main 400d647a8 (rounds 1-3). App 1.0.21+19 awaits his upload.
- Round 4 (LK117-LK147): branches web/r4-{demo,pricing} done; web/r4-{hero,learn,nav} fix stage unfinished (WIP commits);
  web/r4-sections build unfinished (WIP); ui/r4-app done. Backups: origin tags archive/r4-r4-*.
- Next: HANDOFF-2026-11-06.md and PROMPT-NEXT-SESSION-2026-11-06.md. The owner may run that prompt on another model as a
  temporary trial (experiments/MODEL-TRIAL-2026-11.md); that session leaves a branch, it does not ship.

## 5 Nov 2026, about 4:45 pm IST: round 3 live (main ce24dc682, dpl_AgxLoHQJ3uoLMdyeifYvm2qJnr9G); new Key cards for Computerised Accounting and English reading
- **Web:** Day palette fixed (#526700 text green, rimmed selected states, no volt slabs on cream), brand stamps and branded creator cards back, "MockMob" green in the statement, calmer hero with a branded fact strip, held stories stop above a bottom bar (Top, n of N, Skip), logo to top, Pricing pill, tour glitch fixed, phone exam screen, one-plan pricing with Rs-per-day/per-mock framing from the offer and a dated same-period comparison, Key cards flip section. Spec: docs/brain/night-1105/SPEC-R3.md.
- **Content:** Computerised Accounting 207 cards, English reading skills 231 cards (live with the site). Financial Markets blocked: Wayback lebs202 2022/2023 truncated; try the full 2021 capture.
- **Usage:** weekly at about 80% after round 3; keep to small fixes until the week resets (10 Nov 9:30 am IST).
- **Open:** real-phone look; count-up figures may read "0 5,765" to screen readers (check CountUp markup); app 1.0.21+19 awaits his upload; leftover empty folder wt-r3-bottom (locked).

## 5 Nov 2026, about 7:50 am IST: round 2 of the night refinement shipped (main 88ff026cc)
- **Web:** the app's motion on the web (the result score's digit roll at his 720 ms tempo, the finish stamp with one ring on a good set, the Start sheet growing out of its key); public pages with Sign up free / Log in everywhere (site bar, phone menu, a PublicDock), "CUET 2027" never split, even lines, nav links from 1120 px, phone footer in two columns; the logged-in web scanned at 25 views x 6 sizes x 2 themes and fixed (Learn feed bar overlap, Practice tiles at 1280, Your papers, wallet alignment, no decorative monospace, 44 px targets). Gate: suites 0 new failures, eslint clean, both builds, 22 swipes over100 = 0, matrix 128/128. Not measured: the Start sheet open at 4x CPU on a production build (dev build showed frames up to ~130 ms).
- **Earlier tonight (round 1, main 7b47b4c90):** LK81-LK97 live; app 1.0.21+19 in Desktop/MockMob-build-19 for his upload.

## 5 Nov 2026, about 5:50 am IST: the night refinement shipped (LK81-LK97); app 1.0.21+19 built for his upload
- **Web (main 7b47b4c90, deploy dpl_q2i33v9L2XTafEoR83f8k8B9LzFi):** slow-phone stutter fixed (idle predraw; 22 swipes at 4x CPU: 0 frames over 100 ms); Sign up free / Log in lead with "Try 5 questions first" second and a dock that never changes; "CUET 2027." and the tour's MockMob in the brand volt (one green); even lines; the statement's green words back; the opening waits for first paint, the typed line lands whole, Ask Mobi reads your record first; the exam screen in a desktop monitor with an address bar and a faithful NTA style, and the test runner's NTA style matching it; no demo-jump loop and a quiet arrival; fast swipes land on the right step; DU section there on arrival; the web account pop-over like the app's sheet; subject options at web onboarding and "Yours is ..." in Learn; Practice at 1024 px fixed; the numbers band never shows an empty slab. Spec: docs/brain/night-1105/SPEC.md on main; design notes docs/design-decisions/web-1105-*.md.
- **App:** Desktop/MockMob-build-19 (mockmob-1.0.21+19-sells.aab, upload key 62:AC:58:08...EC:47, 16 KB aligned; arm64 APK; OWNER-STEPS.md, README.txt). Branch ui/1105-app-19 (c34db6b69) pushed. New: subject options at onboarding and You > Subjects, Learn's chosen-option line, the card turn's lift and light. Suite 12,469 pass / 111 known old golden drift. His step: upload 19 (it replaces 18).
- **Not verified:** a real phone; signed-in hero states in a browser; app onboarding on the emulator (the demo is always signed in; goldens cover it).
- **Next (LK98, until morning):** more refinement passes on the web and the app; content only when everything else is done and he is away.

## 5 Nov 2026, about 3:45 am IST: night refinement under way (his 2:40 am live-site look, LK81-LK98); slow-phone fix done, seven build packets running
- **His words:** verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md ("5 Nov 2026, about 2:40 am"); ledger LK81-LK98. Keep refining the web and app until morning; then a Play build and the live site; when all of it is done and he is away, add content.
- **Done:** LK81 slow-phone stutter on branch web/1105-perf (0c21de817): held stories drawn while the page is idle (storyPredraw.mjs), the tour keeps its screens mounted, pausing restyles only what animates. 22-swipe bench at 4x CPU: frames over 100 ms 11 -> 0, worst 442 -> 91 ms, p95 24 -> 12 ms. Not live yet (ships with the night's merge).
- **Spec:** docs/brain/night-1105/SPEC.md on web/1105-perf (682712138): D1 CTAs Sign up free / Log in lead, "Try 5 questions first" second, a two-key dock that never changes; D2 the "CUET 2027." line; D3 even lines; D4 the statement's green words back; D5 opening/typing/PrepOS polish; D6 exam screen faithful NTA mode with the real URL inside a desktop mock-up; D7 the demo-jump loop (edge clamp on the landing frame), a quiet arrival, DU section without the reveal gap, fast-scroll hunt; D8 web account pop-over like the app's Account sheet; D9 subject options asked at onboarding (the options, table and Learn picker already exist); D10 card turn lift; app build 19.
- **Running:** workflow wf_8325864d-cee, packets P1 hero (wt-1105-hero), P2 brand (wt-1105-brand), P3 exam (wt-1105-exam), P4 scroll (wt-1105-scroll), P5 account (wt-1105-account), P6 options (wt-1105-options), P7 app (wt-1105-app, branch ui/1105-app-19).
- **Next:** review each packet's renders, merge into one branch, full gate (tests, lint, both builds, gesture matrix, perf, 390/1440 Night/Day critique), ship to main; app emulator walk and 1.0.21+19 AAB in Desktop/MockMob-build-19.

## 5 Nov 2026, about 12:35 am IST: Play build 1.0.20+18 ready for his upload; the new home page (Desk Light) shipped to www.mockmob.in
- **App:** Desktop/MockMob-build-18: mockmob-1.0.20+18-sells.aab (upload key, SHA-256 62:AC:58:08...EC:47, 16 KB aligned), arm64 APK, symbols, OWNER-STEPS.md with release notes. Branch ui/1103-app-18 at c93a34c95, pushed. Contains LK50-LK53, LK42, LK60, LK61, the card look, the bug-review fixes and the emulator-walk fixes. Full suite 12,438 pass, 114 = known old golden drift. His step: upload to Play closed testing (OWNER-STEPS.md).
- **Web:** main 09a5bbe39 (deploy dpl_4PEoVBRVjXEXg6kHvyMZi55K3fUF): the Desk Light home page (LK67-LK75: words-first hero with a typed line and Mobi handing the first question on phone and desktop, the "mo" opening, warm Night without neon, one gesture = one step, the real exam screen, shorter copy, one Mobi finish, a state-aware centred dock) and the Learn walk fixes. Gate: tests (only known failures), eslint, both builds, L-checklist 40 pass, gesture matrix all pass, LCP 0.9-1.2 s at 4x CPU. Left: a one-time first-draw hitch of the Lab and tour sections at 4x CPU (10-11 frames over 100 ms); no real-phone check yet; Instagram post cards without captions.
- **Owner words today:** LK77 (status, ETA), LK78 (backup push already done), LK79 (what is deployed), LK80 (speed up, deploy everything, as perfect as it can be).
- **Next:** his upload of 1.0.20+18 and his look at the live home page on his phone (Night and Day); then the Lab/tour first-draw performance follow-up; LK36 content gaps; Saved on phones; the app's switch labels.

## 4 Nov 2026, about 4:55 am IST: one session; web Learn fix live; app 1.0.20+18 fixed and settled, emulator walk running; home page spec written, build running
- **Live:** main ced6f747f (dpl_DP3B34H1NjgFudfSbiVWzxk3onaf READY, no runtime errors): the ratings coach line is true for every card ("Each key shows when this card comes back: Missed it soonest, Easy latest."), a feed checkpoint and its Stop here end show one count (no zero), the run's deck edges are whole cards.
- **App (ui/1103-app-18 at acd7be66d, not pushed yet):** WIP settle edits taken (b3c3507a7); all 5 medium and 5 of 6 low review findings fixed with tests (sync: 6e9d589f8 via ui/1104-app-sync; Learn: 65be52363, 42fa00a88); explore-learn-calm-3 left (needs a server field, not a regression). Goldens re-recorded and looked at; full suite 12,428 pass, 111 fail = the known old drift only. Emulator walk (Day, Night, text 1.3, Pro and Free) running; then bump to 1.0.20+18, signed AAB with --sell, Desktop/MockMob-build-18.
- **Home page (LK67-LK75):** audit, scroll forensics (real touch: a fling's speed decides how many steps it skips; a gesture-owned controller gave one step in 32 of 32 bench cases), brand inventory done; three designs with mock-ups, three judges (brand-first "Desk Light" best for owner fidelity 8.2 and anti-slop 8.0). The CTO's spec: docs/brain/handoff-1104/home-spec/SPEC-HOME-1104.md (19 decisions: words first with a one-pass typed line, Mobi hosting the first question on phone and desktop, the app's "mo" opening as a 1.3-1.6 s skippable loader, Night on the app's warm charcoal with volt only as fills, the real MockMob exam screen with an NTA-style switch, copy cut to about 2,000 words, one Mobi finish). Five build packets running on web/1104-polish, then integration and the full gate, then ship.

## 4 Nov 2026, about 3 am IST: stopped at his order (usage ~95%); web live, app 1.0.20+18 merged but not built; home page research started
- **Live:** main 5df0c1c72: Physics 1,403 cards; the new Key card look, top-bar capsule, Up next, Find's sets on Learn home, brand icons, English (web). No runtime errors.
- **App:** ui/1103-app-18 at 6079162d5 holds every app change (LK50-LK53, LK42, LK60, LK61, card look). A bug review found 5 medium and 6 low issues plus the version bump; none fixed yet. Not walked, not built. WIP of a stopped agent: wip/1104-app-settle-partial.
- **Home page (LK67-LK76):** his words recorded; Preparoo study and a 40-tell AI-slop checklist done (handoff-1104/home-research); audit, scroll forensics and brand inventory stopped part-way; no design or build yet.
- **Next session:** paste PROMPT-NEXT-SESSION-2026-11-04.md; full state in HANDOFF-2026-11-04-SINGLE-SESSION.md.

## 4 Nov 2026, about 12:05 am IST: new account, one session; Physics live; final Play build and live website in progress (LK63-LK66)
- **His words (3 Nov ~11:55 pm), verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md:** finish every lane, review the UI against his past feedback until satisfied, then NO prototype links or test builds: a final AAB he uploads to Play and the final web changes on www.mockmob.in; commit all uncommitted work for handover/onboarding. Ledger LK63-LK66. His message was cut off at "Everything then should be sent to" (asked).
- **Live:** main dadc12807 = Physics 1,090 to 1,403 cards (312 typeset; ~7.2 h), deployment dpl_HmnRzrJPoKdNYyjuxw3YSwHVhEze READY, no runtime errors.
- **Running (subagents of this one session):** app test fixes on ui/1103-app-18; a stronger Key card look on web/1103-webfull (merged with web/1103-icons at 867376462: Up next module, Find's sets, top-bar capsule, brand icons); English table, web half, on web/1104-english; top bar + brand icons ported to the app on ui/1104-app-look; WIP snapshot commits of old worktrees on their own branches (none pushed).
- **Next:** merge, gate, ship the web to main; app English + card look port, emulator walk, 1.0.20+18 AAB in Desktop/MockMob-build-18.

## 3 Nov 2026, about 9:15 pm IST: all work stopped for the move to a new account; one session from here on
- His words: stop everything; hand off to a new account where everything happens in a single session, with workflows or
  subagents for parallel work (no sub-sessions, no forks). Full state and next steps: HANDOFF-2026-11-03-SINGLE-SESSION.md;
  paste-ready prompt: PROMPT-NEW-ACCOUNT-2026-11-03.md.
- Live: main f0186302f. Unfinished: Physics formula cards (reviewed, not published), app 1.0.20+18 (branches, 4 new test
  failures), web prototypes awaiting his look, English rewrite table.

## 3 Nov 2026, about 3:15 pm IST: STOPPED by the owner; feedback LK55-LK62 recorded; he restarts the PC, then we continue
- His words verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md ("3 Nov 2026, about 3:15 pm"); ledger LK55-LK62. "Don't start doing anything right now. Just record everything that I said."
- Live: main f0186302f (Mathematics 548, fonts self-hosted, LK37 run choices). Nothing of the Key cards session is running.
- After the restart: dev servers and agents are gone; LAN preview address is the Wi-Fi one, 192.168.1.8 (not .15, the Ethernet address the firewall blocks).

## 3 Nov 2026, about 2:45 pm IST: Mathematics 548 live (all 13 NCERT chapters typeset); fonts self-hosted, so the Vercel font failure is gone
- **Live:** main 4006a7c04 (app port session's LK37 run choices, on top of 29b001d8e). 29b001d8e = Mathematics 349 to 548 (221 typeset cards; the other 10 chapters plus a fix round, each card through an Opus formula reviewer against the page image and a Sonnet content reviewer) and Bricolage, Gabarito, Hanken and Literata served from src/app/fonts. Both builds READY on the first try; no runtime errors; no Google Fonts requests.
- **Mathematics: about 2.9 hours** (data/learn/seconds.js), just under his 3-hour bar. NCERT's 2026-27 text supports about this much: Application of Integrals and Probability Distributions were cut by NCERT (coverage notes), and the four Applied Maths chapters have no NCERT book.
- **Queued:** rework of two Probability formulas written as fractions of long phrases (they scroll on a phone); ncert-books/pages to delete after it.
- **Needs his answer (running list):** the app port session's three questions (top bar live look at http://192.168.1.15:3463/preview/arena?view=dashboard&plan=pro, same Wi-Fi; Saved one tap or inside Explore; "Practise | Papers | Learn | Explore" in the app), LK36 gaps 1-3, Physics formula pipeline, Applied Maths source.

## 3 Nov 2026, about 1:45 pm IST: Maths formula cards pushed (Mathematics 349); 10 more chapters being written; app feedback LK50-LK53 with the app port session
- **His words (3 Nov ~1:30 pm), verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md:** the app looks good but the UI can be better in many places; a stuck "Sending your answers · Computer Science mock" strip on every screen of his main account (LK50); no Explore ("Flow") feed in the app (LK51); Learn still cluttered (LK52); stronger, more premium, in the direction of Duolingo (LK53). "Continue doing all that"; he answers questions when back in 30-40 minutes. His stop of 2 Nov ~11:20 am is lifted.
- **Pushed:** main 2152e0b74 = typeset Maths formulas on Key cards (KaTeX 0.19.0, server-drawn, readable plain text for the app), Mathematics 310 to 349 (Inverse Trigonometric Functions 21, Probability 29, Application of Integrals 11), Geist Mono self-hosted. Deploy check below in STATUS once READY.
- **Running:** workflow wf_87f52d2b-817 writes formula cards for the other 10 Maths chapters (Sonnet author, Opus formula reviewer against the page image, Sonnet content reviewer each). Then: check-drafts-mtex-1102.mjs, merge-mtex-reviews-1102.mjs, publish, look, push.
- **App (LK50-LK53):** handed to the app port session (local_3c5cb01e) with the diagnosis of the stuck strip (a stale local draft keeps pendingSubmission after its submit window, or after the token refresher gave up). Ends in 1.0.20+18 for him to upload.
- **Needs his answer (running list):**
  1. LK36 gaps: (1) English reading-comprehension cards (~200, authored like the vocabulary cards), (2) Financial Markets from NCERT's 2022 edition, (3) Computerised Accounting from NCERT's CAS book (a PDF download). Any of 1-3?
  2. Physics: the same formula pipeline could recover the ~400 Physics cards held for flattened notation. Start it?
  3. The four Applied Maths chapters have no NCERT book; leave them, or name a source?

## 2 Nov 2026, about 9:50 am IST: +668 Key cards live (15,469); Maths formula pipeline started on his yes; app 1.0.19+17 waiting for his upload
- **Live:** main a16fbd62e, deployment dpl_8XasSMKTRgwwiwN6CXtVc5UtuvkW (first build passed). /, /learn, /explore, /today, /pricing, /api/stats and a Computer Science cards page answer 200.
- **Recovery round 2:** 1,003 held cards (876 held as ambiguous, 127 Computer Science front wording) were fixed and re-reviewed independently; 668 passed. Computer Science 1,544, History 1,587, Geography 1,345, Sociology 1,190, Chemistry 1,411, Physics 1,090, Psychology 826, Mathematics 310, Accountancy 920. No published card removed or changed.
- **His words (2 Nov morning), verbatim:** "Yes, start it" (to: start the Maths formula card pipeline). Later: "Can you give me an update on what has been running over the past 24 hours? ... check the logs, check what all is done and what's left, and then give me a status update on everything that's left or something that has not even been done yet?" Answered in the session with the full list (58 open ledger rows untouched in two days; Today is the suggested next area).
- **Maths formula pipeline (LK34):** spec handoff-1102/MATHTEX-SPEC.md, author brief handoff-1102/MATHTEX-AUTHOR-BRIEF.md. A card may carry `tex` (LaTeX of its front/back), checked by machine (KaTeX parse; same letters and digits as the PDF-checked back) and by an independent reviewer against the page image; the server sends the app and search a readable Unicode version. Code on web/1102-mathtex (wt-1101-r2-home), pilot lemh102, then 12 chapters. Page images: ncert-books/pages (43 MB; delete after the wave). Backups: ncert-books/drafts-bak-mtex-1102, reviews-bak-mtex-1102.
- **LK25:** 1.0.19+17 is built and signed for him: C:/Users/atish/Desktop/MockMob-build-17/mockmob-1.0.19+17-sells.aab (steps in OWNER-STEPS.md there). His step: upload to Play closed testing, then check Learn on his phone.
- **Decisions waiting on him:** the app keeps its navigation (the web's four equal tabs, LK26, are not in the app); the stop sheet counts acted items ("3 of 18 done") while the end screen counts seen items ("9 of 18 done"). Self-hosting Geist Mono goes in the next release unless he says no.

## 2 Nov 2026, about 4:40 am IST: +911 Key cards (14,801): wording recovery, English to 650, Accountancy thin chapters (LK34)
- **Live:** main e120b004d, deployment dpl_4WjR4cqaxDCjgKuWZn8ct4f8Qcts (a redeploy: the first build of this commit failed on the Geist Mono font fetch, as one did at 4:15 am). No runtime errors; /, /learn, /explore, /today, /pricing, /api/stats and the English, Accountancy and History chapter pages answer 200. Rollback: dpl_9D1LG3MWRpJ6qB6DCWpBic8a4NLQ (main feb30935e).
- **What students get:**
  - 663 cards that were held back only for front wording are back, re-cut and checked by an independent reviewer: Chemistry +97, Geography +76, History +79, Mathematics +30, Physics +112, Psychology +52, Sociology +119.
  - English 350 to 650 (word meanings, idioms, one-word substitutions, confused words, grammar rules): about 3.2 h, above his 3-hour bar.
  - Accountancy 866 to 912: Change in Profit Sharing Ratio, Retirement & Death, Analysis of Financial Statements, Comparative & Common Size Statements.
  - No published card was removed or changed.
- **Per subject now:** Accountancy 912, Biology 1,394, Business Studies 901, Chemistry 1,354, Computer Science 1,350, Economics 1,195, English 650, Geography 1,238, History 1,497, Mathematics 290, Physics 1,044, Political Science 1,096, Psychology 778, Sociology 1,102.
- **Still short:** Mathematics (290 cards, about 2 h). The formula pipeline waits for his yes.
- **LK25:** the app port session was resumed at about 4:40 am with the web changes since 1 Nov (rounds 2-4, Key cards for every subject) and the plan: finish its walk, align with LK24-LK33, emulator walk, release AAB for him to upload.
- **Reliability:** 2 of 4 Vercel builds today failed fetching Geist Mono from Google Fonts. A redeploy passes. The lasting fix (self-host the font) is proposed, not done.
- **Next (scheduled in this session for 8:27 am, after the 8:20 am usage reset):** recovery round 2. 1,003 held cards: 876 held only as ambiguous, plus 127 Computer Science cards held only for front wording. They go through the same fix and independent re-review: handoff-1102/recovery2-1102.js, args in recovery2-args-1102.json, guards check-drafts-r2-1102.mjs and merge-reviews4-1102.mjs. If the session has ended, a new one runs it from those files.

## 2 Nov 2026, about 4:15 am IST: Computer Science Key cards live (LK34); a recovery round and the English top-up are being checked
- **Live:** main feb30935e, deployment dpl_9D1LG3MWRpJ6qB6DCWpBic8a4NLQ. No runtime errors; /, /learn, /explore, /today, /pricing and a Computer Science chapter page answer 200.
  - The first deploy of this commit (dpl_3mveaRtzPDRYTRTnZFSQGsy6bpaA) failed when the build could not fetch the Geist Mono font from Google Fonts; a redeploy of the same commit passed.
  - Rollback: dpl_8B5HtwbPkxUfDXTKa5UeBzyTdd8F (main 7f1b204a7).
- **Computer Science:** 1,350 cards across 18 chapters, from Computer Science XII Ch 1-12 and Informatics Practices XII Ch 1-7; 567 held back. Project Based Learning (CS Ch 13) is outside CUET Section B1, so it has no cards.
- **Blanks:** a comma or bracket that touches a blank now stays on its line (1,087 fronts had one; a line could start with ", and").
- **Every subject now has Key cards (13,890):** Accountancy 866, Biology 1,394, Business Studies 901, Chemistry 1,257, Computer Science 1,350, Economics 1,195, English 350, Geography 1,162, History 1,418, Mathematics 260, Physics 932, Political Science 1,096, Psychology 726, Sociology 983.
- **Short of his 3-hour bar:** Mathematics (about 2 h; needs the formula pipeline, offered to him) and English (about 1.7 h; the top-up below adds about 300).
- **In progress (next release):** workflow recovery-topup-1102 (handoff-1102/recovery-topup-1102.js).
  - 778 cards held back only for front wording (It/This openings, over-long fronts) are being fixed and re-reviewed by an independent reviewer.
  - English: 322 new cards written, 22 flagged. Accountancy thin chapters: 80 new, 34 flagged.
  - Then: handoff-1102/check-drafts-1102.mjs, merge-reviews3-1102.mjs, review-merge, validate per subject, tier, suites, a look, build, deploy.
- **LK25:** the app port session (Port Learn v2 and the Explore feed to the app) stopped on 1 Nov at about 3 pm at the old account's usage limit, before its emulator walk. It has not resumed.

## 2 Nov 2026, about 4 am IST: Physics and Mathematics Key cards live (LK34); Maths is thin
- **Live:** main 7f1b204a7, deployment dpl_8B5HtwbPkxUfDXTKa5UeBzyTdd8F. No runtime errors.
- **Physics:** 932 cards across 14 chapters.
- **Mathematics:** 260 cards across 14 chapters, about 2 hours of study. That is below his 3-hour bar.
  - Some chapters are very thin: Three Dimensional Geometry has 1 card; Inverse Trigonometric Functions and Vector Algebra have 5 each.
  - Why: the PDF text flattens formulas, so maths cards were limited to definitions and theorems in words.
  - The fix is a follow-up job: transcribe NCERT's formulas from the page images into LaTeX and draw them on the cards.
- **Still being written:** Computer Science.

## 2 Nov 2026, about 3:40 am IST: Geography, Psychology and Sociology Key cards are live too (LK34)
- **Live:** main 26e5f359a, deployment dpl_6hhcRyXQwLwtknmeVNiL1aDbyuqQ. No runtime errors.
- **New subjects:**
  - Geography: 1,162 cards, 17 chapters
  - Psychology: 726 cards, 7 chapters
  - Sociology: 983 cards, 14 chapters
- **With Chemistry and History, live since about 3 am:** 5 new subjects and 5,546 new cards.
- **Still being written:** Physics, Mathematics, Computer Science.

## 2 Nov 2026, about 3 am IST: Chemistry and History Key cards are live (LK34)
- **Live:** main 90679d8c0, deployment dpl_Bb2sB56bG5wADahBaBkiQvzAQEyh. No runtime errors; rollback is the previous deployment.
- **Chemistry:** 1,257 cards from 10 NCERT chapters.
  - Formulas are drawn as real chemistry (CH₃OH, [Co(NH₃)₆]³⁺, 3d⁸).
  - I looked at them on screen.
- **History:** 1,418 cards from 12 NCERT chapters.
- **Both subjects:** exact NCERT text with book, chapter and page. Each chapter was checked by an independent reviewer, and the cards it flagged are held back.
- **Being written now:**
  - Geography, Psychology and Sociology
  - Physics, Mathematics and Computer Science
  - Physics and Maths cards hold only text that reads right without formulas, because extraction flattens powers and fractions.

## 1 Nov 2026, about 11:55 pm IST: Learn v2 rounds 2 to 4 are live (his LK24-LK33)
- **Live:** main 668341aea, deployment dpl_kmM3Rym59riGDcmQ1MVgRzs9RbGa.
  - No runtime errors.
  - The pages answer 200.
  - /api/stats is served from the CDN cache.
  - Rollback: dpl_DoGHp6AAWaCKngaFxKAckyhq7vAy.
- **What he will see:**
  - **Learn:** opens with a start offer and no zeros, one subject picker on phones, Free rows show each chapter's real size, chapters are named "Chapter 5 of 14", and "Needs work · from your papers".
  - **Cards:** read like flashcards, with the next card peeking and a one-time swipe chip.
  - **Ends:** short, with the keys at the bottom. Free gets one true line: questions come back tomorrow, Key cards stay open.
  - **Today:** for a new student, no false history and no zeros, and the start key is above the dock.
  - **Home hero:** the headline stays still.
- **How it was checked:**
  - 3 rounds of fixes.
  - Round 3 was reviewed by 5 lenses, and every serious finding was checked by 1 to 3 skeptics (docs/brain/learn-1031/r4/R3-REVIEW-FINDINGS.md in the web repo).
  - The suites, lint and build passed.
  - 180 screenshots, which I looked at.
- **Not checked:** a real phone, a trackpad, or a screen reader. He should look on his phone.
- **Cards (LK34, subscription):**
  - Chemistry (1,257) and History (1,418) are published on branch web/1101-content. They are not live yet: the chemistry formulas need a look first.
  - Geography: 15 of 17 chapters are written.
  - Next: Physics, Mathematics, Psychology, Computer Science and Sociology, after the 1:50 am usage reset.
- **Open:**
  - LK25, the Play release, waits on the app port session's emulator walk.
  - The Day hero poster needs a repaint (an image job).
  - Practice may say 15 chapters on the live site if the chapters table holds Computerised Accounting.

## 1 Nov 2026, about 4:15 pm IST: his first live feedback on Learn v2 (LK24-LK35); round 2 starting
- **His words:** verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md (1 Nov, about 4:05 pm). Items LK24-LK35 are in the ledger.
- **What he asked for:**
  - the phone website is cluttered and slow
  - Learn leads with a real start offer, not zeros
  - first-time cues (the feed swipe)
  - less blank space and fewer walls of text on end screens
  - a home hero that is more branded, tighter and reacts to taps
  - content for every subject (3 hours or more each)
  - a fresh Play release when the app update is ready
  - keep going
- **Done since he went live:** the stop-sheet count fix, web/1031-learn-v2 584542985 (not pushed). Live: main 978edc236, with no runtime errors.

## 1 Nov 2026, about 1 pm IST: Learn v2 and the Explore feed are LIVE (switches on)
- Owner applied the migration (dry run OK, then apply); verified by read: both tables, both functions, flow_context learn, no anon read.
- LEARN2_ENABLED=true, NEXT_PUBLIC_LEARN2=on (Vercel production); main 978edc236 READY (dpl_DoGHp6AAWaCKngaFxKAckyhq7vAy).
  /api/learn/* now answers 401 signed out (on); /learn/c/<key> renders; no runtime errors. Off = set both off and redeploy.
- Next: the owner tests live and gives feedback (he saw bugs on the local server); fix round after his list.

## 1 Nov 2026, about 12:30 pm IST: Learn v2 code is LIVE with its switches off; the owner applies the migration next
- **Owner:** "Ship it", then: he wants it live to test everything properly; "mostly loved the direction"; refinement and fixes after
  deploy. He still has feedback from the local server (it was a bit buggy there).
- **Live:** main 106e53720 on mockmob.in (Vercel dpl_4KiFy8nhFkomrN5pgA3H1284MF5k, READY). Switches off: /api/learn/* answers 404
  LEARN_OFF, /learn/run, /explore/run and /learn/c/* serve the not-found page, the v1 Key cards API is unchanged, no runtime errors.
  The Learn v2 nav (Learn, Key cards first; the Start sheet's Learn a chapter) is gated too (cf552bac8), so the live nav is unchanged.
- **Blocked for agents:** the production migration (the auto-mode classifier denied even the rolled-back dry run). The owner runs
  wt-1031-learn-v2/supabase/dryrun/20261101150000_learn_runs.dryrun.sql, then supabase/migrations/20261101150000_learn_runs.sql in the
  Supabase SQL editor (project isrxrxzjocewrdureyhp). Read-only pre-checks passed; question_interactions is about 3,500 rows.
- **Then:** set LEARN2_ENABLED=true and NEXT_PUBLIC_LEARN2=on (Vercel, production) and redeploy; NOT before the migration (a redeploy
  with the switches on and no tables would break every Learn run). Then smoke test, his test, his feedback.
- **App port:** session local_3c5cb01e (Port Learn v2 and the Explore feed to the app) started by the owner.

## 1 Nov 2026, about 6:20 am IST: Learn v2 and the Explore feed built completely (LK20-LK23); waiting for his look
- **Branch web/1031-learn-v2 (wt-1031-learn-v2), not pushed or deployed.** Spec BUILD-1101.md; audits A1-A8, 00-critic, 09-final-critic in
  docs/brain/learn-1031/audit-1101/. Commits: 06d7b40f5 e61e5517e e8e6d3c0c 0cd13b463 978699f89 2e90b5be7 f684d507a eea222a3f ee3f61abe
  e36c92f4f 6bffc64c2 153f534e9 ea6543d7d d9afdf8e8 2be498715 1bfd86ee9 4bba8db6f.
- **What is built:** real pager (one wheel notch, swipe or key = one item; slow drag works; visible Previous and one named volt key),
  desktop session panel, cards that fit their words, the line in place, covers that show each chapter's own opening card, Learn home
  with search and shelves, chapter page, run on the same stage, stop sheet, ends with real numbers, watermarked v2 print sheet,
  production service + 11 /api/learn routes behind LEARN2_ENABLED, pages behind NEXT_PUBLIC_LEARN2, one Key cards world when on.
- **Verified:** final capture 182 stills at 1440/1366x650/1024/390/360, Night (Day at 1440/390), 0 console errors, 0 sideways scroll; wheel,
  trackpad, keys and touch measures pass; owner-eye critic M1-M10 fixed (1bfd86ee9). Not verified: real phone or trackpad, screen reader,
  real Ctrl+P margins; the two films predate the last fixes.
- **Owner links (LAN, this PC on):** http://192.168.1.15:3451/preview/arena?decks=real&study=on&view=learn2-feed&plan=pro&student=commerce&chapter=accountancy.admission-of-partner&min=10
  (also view=explore, view=learn2&subject=accountancy, view=learn2-chapter&chapter=accountancy.admission-of-partner). Owner set:
  wt-1031-learn-v2/tmp/learn-1101/for-owner/.
- **Needs him:** his look and verdict; confirm the CTO decisions (Keep = add to Revise; realistic seconds; LK15 claimed at the first answer,
  Free clamped to 10 min, second Free run cards only; no Must-know tag on feed/run cards; chapter page keeps the subject object); content
  calls (duplicate card "Define partnership." vs "What is partnership?"; the card "If this amount is paid..." reads oddly alone); to ship:
  run supabase/dryrun/20261101150000_learn_runs.dryrun.sql, then apply the migration, approve merge + deploy, set LEARN2_ENABLED=true and
  NEXT_PUBLIC_LEARN2=on; then the app port (A7, stale in places; the web is the source of truth).

## 1 Nov 2026, about 3:45 am IST: Learn v2 built for production behind flags; UI rebuild running
- **Branch web/1031-learn-v2 (wt-1031-learn-v2), not pushed or deployed.** Spec: docs/brain/learn-1031/BUILD-1101.md in that worktree
  (logic Part 1, production Part 2, UI Part B with B7 decisions); audits in docs/brain/learn-1031/audit-1101/ (A1-A8).
- **Done:** S2a service + 11 /api/learn routes behind LEARN2_ENABLED (06d7b40f5); S2b migration 20261101150000_learn_runs.sql with undo and
  PGlite test, saved only, never applied (e61e5517e); S1 engine rules: honest Keep, feed moves forward, resume, slot-first order, realistic
  seconds, LK15 claimed at the first answered question (e8e6d3c0c); P production pages behind NEXT_PUBLIC_LEARN2, no shell flash (0cd13b463).
  test:learn 133/133, test:keycards 81/81.
- **Running:** workflow learn-build-1101-ui: U1 feed (real pager: one swipe, wheel notch or key = one item; visible Previous and a named volt
  key; desktop session panel) and shared study parts; U2 covers (the opening card as the cover, no repeated object); U3 Learn home; U4 chapter
  page and run; S3 server fields. Then capture, critique and fix rounds, the owner's phone link.
- **Owner decisions taken by the CTO (he can override):** Keep = add to Revise (no fake rating); realistic seconds (about 12 cards and
  5 questions in 10 min); LK15 counts chapter runs and feeds, claimed at the first answer, Free clamped to 10 min with a line; a second
  Free run that day is Key cards only. Needs him later: apply the migration after the dry run; turn the two flags on; the app port.

## 1 Nov 2026, about 1:30 am IST: his look at the feed prototype (LK20-LK23); full build under way
- **His look (on a computer):** likes the feed direction, but on a PC there is no way to the next item and too much blank space (LK20); loves the
  Explore covers, but every Accountancy cover shows the same object (LK21); the chapter run is "quite good" but needs a lot of refinement (LK22).
- **His task (LK23):** build the feature completely now, test everything, fix every issue, refine the UI/UX and the logic, make it more useful; then tell
  him what is needed from him and his next steps.
- **Running:** workflow learn-map-1101 (logic audit, production wiring plan, Flutter app map) and learn-ui-audit-1101 (desktop and phone captures in
  wt-1031-learn-v2/tmp/learn-1101/audit, then audits A1-A4, A8 and a critic); reports go to wt-1031-learn-v2/docs/brain/learn-1031/audit-1101/.
  Then the main session writes the refinement spec, and build, capture, critique and fix rounds follow.

## 1 Nov 2026, about 12 am IST: nav v2 rejected; building the Explore feed v2 live prototype
- **Nav v2 rejected:** he says the current structure is cleaner, so it was reverted on web/1031-learn-v2 (60a7071e4, b54885382).
- **Building:** a phone-first Explore feed per learn-1031/FEED-2.md:
  - full-screen swipe-up items, cards that flip, Keep, the wrong-answer sheet, a checkpoint and an end screen;
  - Explore chapter covers;
  - Find as a search field in Learn.
- **Phone link:** he will open it on his phone over the LAN at http://192.168.1.15:3451. allowedDevOrigins was added in e723aaf4a.

## 31 Oct 2026, about 11:30 pm IST: the owner answered A9 and N1
- **A9 (LK15):** feed and Learn questions are free up to a limit. The rule is one free Learn session a day, up to 10 minutes. Not built yet.
- **N1 (LK16):** Learn becomes its own section, but the app bar cannot grow. NAV-2.md is on branch web/1031-learn-v2:
  - On the website, Learn is a place in the sidebar.
  - On phones, the Practice tab gets a Practice/Learn title switch.
  - An agent is rendering it as `&nav=n2`.
- **LK17:** he could not see any change because nothing is deployed. The local preview (port 3451) was opened in his browser pane.

## 31 Oct 2026, about 9:45 pm IST: Learn redesign renders sent to the owner
- **Sent:** 11 real renders and a run video (wt-1031-learn-v2/tmp/learn-1031/for-owner/), from branch web/1031-learn-v2
  (commits 5af8f8a2f slice, a47da5caf merge of the live release, b9bc5fe80 and the volt-quiet fix). Full set of 143 captures in
  tmp/learn-1031/final2; critique docs/brain/learn-1031/CRITIQUE-1.md (all four blockers fixed).
- **Must-know:** one overlay only, the live data/keycards/tiers.json (12 of 46 in Basic Concepts; 229 in Accountancy).
- **Checks:** test:learn 43/43, test:keycards 76/76, test:app 986 pass 2 fail (heroScene landing tests, also failing on main), lint clean.
- **Open:** E4 deck content (two near-duplicate opening definition cards, both Must-know; one Ch 1 card cites Ch 2), E6 Free
  "Your papers" fixture count, R9 Explore chapter label "Partnership Fundamentals", /learn/run as a focus route. Not wired
  to production yet (Supabase-backed /api/learn routes), no app parity yet.
- **Owner next:** his look at the renders; A9 (questions free inside Learn) and N1 (Learn as its own desktop sidebar place).

## 31 Oct 2026, about 6:55 pm IST: Learn feedback (LK1-LK14): fixes live, redesign in preview
- **Live (main b7e68f8e2):** Your part picker fixed (LK2); Study motion (LK5); MockMob watermark on every printed sheet (LK6);
  Must-know re-tiered to 25% via data/keycards/tiers.json (LK13). Suites, build and captures in STATUS.md.
- **Building (not live):** the Learn redesign as real screens in the dev preview: `wt-1031-learn-v2` (branch web/1031-learn-v2),
  spec `docs/brain/learn-1031/DESIGN-SPEC.md` (concept B "the chapter is the home" plus amendments A1-A12), data contract
  `API-CONTRACT.md`, workflow learn-v2-slice (engine, home, chapter page with piles, run player, cards view, Explore feed,
  then capture, Opus critique, fix). Dev server: .claude/launch.json "learn-v2-dev" on port 3451.
- **Owner next:** see the real renders when they land; decide whether questions inside Learn are free (A9) and whether
  Learn gets its own desktop sidebar place (N1). App version 17 can wait for the redesign.

## 31 Oct 2026, about 4:50 pm IST: 218 off-syllabus questions pulled
- **Owner:** "Pull them all". The 218 are off-syllabus, pending and frozen on production (dry-run, then applied; undo saved).
- **Bug fixed on the way:** the morning's 25 flawed-question pulls were still served (pending, but verified and active
  is still visible). They are frozen now. Visible questions 8,571 to 8,328.
- **Thin now:** Accountancy, Financial Statements of Company, 1 question; Political Science, Recent Issues and
  Challenges, 4.
- **Record:** STATUS.md on main 0149bf45b; `docs/brain/intel-1031/off-syllabus-2026-10-31/` on main.
- **Owner next:** app version 17 build; open /cards signed in once; say if Accountancy should get new questions.

## 31 Oct 2026, about 1:35 pm IST: Key cards ON for students
- **Flag:** the owner said "Turn it on". KEY_CARDS_ENABLED=true and redeployed (dpl_7dHWVGYYCxR753iJ8wW6Ppgaoyx4).
- **Smoke:** the routes answer 401 signed out; no errors. The signed-in flow on production is not yet seen by anyone.
- **Owner next:** decide on the 218 outside-syllabus questions; app version 17 build.

## 31 Oct 2026, about 1:20 pm IST: Key cards release LIVE with the flag off; syllabus v2 and Key cards migrations applied
- **Live:** main 5c1d03a37, dpl_jzeVzYF2yT6F8EwUQxM9EcnPvPau.
- **Database:** syllabus v2 plus its live-rows fix and the Key cards tables are applied; 561 re-tags; 59 flawed questions fixed.
- **Pools:** Biology 369, Chemistry 395, Political Science 252.
- **Record and undo:** STATUS.md on main.
- **Owner next:** see the screens, turn KEY_CARDS_ENABLED on, decide on the 218 outside-syllabus questions, build app version 17.

## 31 Oct 2026, about 1:00 pm IST: Key cards hardened, content grown, question pools audited; owner steps ready
- **Live production is unchanged** (main 0b7d6bc03). Nothing pushed, deployed or written to production. The session's
  permission check blocks production writes, so every production step is saved with its undo for the owner.
- **Web integration** `web/1031-keycards` 5c1d03a37. The merge to main is a fast-forward.
  - Code review fixed: 4 high, 6 medium, 12 low.
  - Screens polished against the real decks.
  - Content: 5,800 cards, 2,144 linked questions; 18 conflict cards and 49 duplicates held back.
  - Mocks: at most 2 copies of one template stem per paper.
- **App** `ui/1031-keycards`: walked on the emulator with real cards; fixes plus web display parity.
- **Pool audit** of 2,875 live questions: 515 wrong chapter (476 verified re-tags ready), 218 outside CUET 2026,
  50 flawed (59 fix-or-pull SQLs ready), and about 849 Accountancy template copies.
- Read `docs/brain/HANDOFF-2026-10-31-KEYCARDS-3.md`.

## 31 Oct 2026, about 6:00 am IST: Key cards built end to end on branches; waiting for the owner's look
- **Live production is unchanged** (main 0b7d6bc03). Nothing pushed, deployed or written to production.
- **Web integration** `web/1031-keycards` 90fddb40d: syllabus v2, Key cards server, web screens, 5,721 published NCERT
  cards in 6 subjects (137 quarantined), 1,632 question links, re-tag file. All suites green; webpack build passes.
- **App** `ui/1031-keycards` bb4da376b: done and tested; no device walk yet.
- **Owner decisions waiting:** see the screens; turn `KEY_CARDS_ENABLED` on; accept the pool shrink when syllabus v2
  retires 440 questions (Biology -18%, Chemistry -15%, Computer Science -14%).
- Read `docs/brain/HANDOFF-2026-10-31-KEYCARDS-2.md`. Next prompt: `docs/brain/PROMPT-NEXT-SESSION-2026-10-31.md`.

## 31 Oct 2026, about 3:45 am IST: Key cards build PAUSED at the owner's 93% usage
- **Live production is unchanged** since the version 16 web release (main 0b7d6bc03). Nothing from this work is pushed
  or deployed.
- **Work in progress:** Key cards (NCERT exact-quote flashcards), syllabus v2 (CUET-referenced) and chapter state.
  - Owner decisions: D200-D206.
  - Read `docs/brain/HANDOFF-2026-10-31-KEYCARDS.md`. Next prompt: `docs/brain/PROMPT-NEXT-SESSION-2026-10-31.md`.

(Older state below.)


**Last written:** 20 Oct 2026, about 3:20 am IST (updated from 2:35 am), by session 801f0d1a (Claude Opus 5.5, CEO/CTO). The owner is asleep with FULL AUTONOMY for this session (D156: decide independently, no mock-ups or results to show, deploy when tests pass). His words are verbatim in `docs/brain/OWNER-FEEDBACK-2026-10-19.md` (to D157 and I1-I16, J1-J6). Decisions: `OWNER-MASTER-LEDGER.md` (C-dec 3 and 3b at the end).

## 1. Vision (stable)
CUET UG 2027 prep for 16-17-year-olds. USP: unlimited mocks from one central bank. Score Recovery (find, fix, check the fix holds); Ask Mobi; the Mob. Premium, alive, smart. **The website is the main product** (D157); the app follows. Version 13 is the closed-test first impression for 14-15 testers starting 20 Oct (D155): no bugs, exceed expectations.

## 2. Rules in force
R1-R8 (PLAN-1019 section 0). D150 build-and-look loop (agents capture visuals while building). D156 autonomy for this session. D157: Pro does NOT make Mobi free; credits bought mostly by Pro students; depth over volume; keep AI margins wide. Never sign in from a staging build (C1: it reached production; guard now in ui/v17-bugs). Production writes allowed this session only for the Mob v3 go-live (D152) and what the owner named.

## 3. Live now
- **Web v13 + Mob v3 LIVE (3:13 am, D152):** main 65afa5d0, deployment dpl_4nA9juLKE9wFKjPHRAcdtfx7Ffha (rollback point dpl_F8qxHxpnXyZPqjCEAFrPrBbSnE9L). Mob v3 migrations core/games/chains/realtime applied on production (recorded as 20261019213134-213528), MOB_V3_ENABLED=true in Vercel Production, MOB_LIVE_ENABLED unset. Includes web Mob den/play, web Pro page + Wallet (J1/J3), /app/login email link page, assetlinks from ANDROID_CERT_SHA256 (unset: returns []), no email-prefix names. Smoke clean, 0 runtime errors.
- **Web:** main 58793f9c = Play subscriptions LIVE (PLAY_BILLING_ENABLED=true set by him; deploy dpl_F8qxHxpnXyZPqjCEAFrPrBbSnE9L; RTDN works). Production migration 20261019210000 applied 9:51 pm. Licence-tester purchase proven end to end (Pro, 4 renewals, 50-credit pack, refund+revoke). Stray test auth user chai-fresh@example.com deleted (D151).
- **Play Console:** listing uploaded (v11b text option A, feature graphic A, screenshot set 2 from Desktop\MockMob-store-listing\UPLOAD-THIS); internal testing has version 11 (link showed "Item not found": Google propagation; he used other routes); closed testing Alpha has version 11 IN REVIEW. Version 12 built (Desktop\MockMob-build-12) and SKIPPED by him (D154). Pro price shows Rs 150 (he set 150; D136 said 149; his call). Content rating (users interact: yes; purchases: yes) and Data safety (Purchase history) still need his update before Alpha review completes.

## 4. Version 13 in flight (all local, nothing pushed)
**App** base ui/v16-1020 2485e83e (= v12). Branches (each its own worktree wt-1020-*):
- done: ui/v17-bugs 6b659e43 (Ask Mobi ties, API origin guard C1, email App Link /app/login + verifyOTP, G13), ui/v17-mob-switch 449e8fde (MobRead v3Available/serverV3, MOB_V3_ENABLED default on), ui/v17-mob-art 9cc7e7dc (moments order, FINAL FOLDS art: idle/cheer/think, parcel, seal; shrug/wave fall back to idle), ui/v17-mob-den 6ea7f777 (H1/H2/H5/M1 etc.), ui/v17-mob-play e8a0d38e (H4 race, H6 podium, M2, M5), ui/v17-pro-page 6cb1c9d2 (full-screen Pro page /you/pro, owner J1/J2 applied).
- still working: ui/v17-wallet (owner J3: packs as Mobi answers/repairs), ui/v17-finish (SWOT-style paper read = Mobi's debrief + full-mock reveal), ui/v17-mobi + web/v13-mobi (Ask Mobi value per C-dec 3b: Where you stand, Fix it for good, doubt threads, mentor reads colleges).
- **Integrator** (Sonnet) building ui/v17-release in wt-1020-app-rel: merges bugs, mob-switch, mob-art, mob-den, mob-play, pro-page; full tests; demo-mode emulator walk; screenshots tmp/walk-1020/app-v13. Then wallet, finish, mobi to merge.
**Web** base web/1019pm-mob-v3 e2eb2462 (Mob v3 server + live main + v3Available). Branches: web/1020-fixes 55bcbad0 (app sign-in link page, assetlinks from ANDROID_CERT_SHA256, no email-prefix names), web/v13-mob-den 2e3cea79, web/v13-mob-play 8757518d, web/v13-money afea69dd (Pro page + Wallet, J1/J3). **Integrator** (Sonnet) building web/v13-release in wt-1020-web-rel (+ server folds.mjs colours); web/v13-mobi to merge after.

## 4b. In flight at 3:20 am
- App integrator: ui/v17-release (wt-1020-app-rel) has bugs, mob-switch, mob-art, mob-den, mob-play, pro-page merged (d915d22d); merging ui/v17-wallet 536de4b5, ui/v17-finish 6fdfff26, ui/v17-mobi (wt-1020-mobi); then full tests, demo walk, signed build 1.0.16+13 to Desktop\MockMob-build-13.
- Web Mobi deployer: merging web/v13-mobi (wt-1020-web-mobi) into wt-1020-web-rel at 65afa5d0, suites, push main, smoke, STATUS.
- Mobi owner finishing app tests on ui/v17-mobi.
- Handoff prompt for a fresh account: docs/brain/NEXT-PROMPT-1020-AM.md.

## 5. Next (in order, autonomous)
1. Finish merges (app ui/v17-release, web web/v13-release) incl. wallet, finish, mobi; full suites (app unit ~7k, web test:mob/billing/recovery/auth/app/subjects, next build --webpack).
2. Adversarial review per surface (Mob, money, finish, sign-in), fix wave.
3. GO LIVE (D152): pre-check prod; apply Mob v3 migrations 20261020100000 core, 100100 games, 100200 chains, 100300 realtime (files in wt-1019pm-mobsrv supabase/migrations, undo in supabase/undo); set MOB_V3_ENABLED=true in Vercel Production (MCP create_project_env; if blocked, note for owner); push web/v13-release to origin main (fast-forward from 58793f9c? it is a merge descendant: check `git merge-base --is-ancestor origin/main HEAD`); Vercel check; smoke (/, /mob, /pricing, /wallet, /api/mob 401). STATUS entry with undo.
4. Build version 13: bump to 1.0.16+13 (or 1.0.17+13), `bash tool/build_release_aab.sh --bump --sell` in the release worktree (copy MockMob-keys\key.properties to android\ if missing), APK too, emulator launch check, copy to Desktop\MockMob-build-13.
5. Folds shrug/wave: Codex account 2 resets 5:38 am (account 1 after 2:58 am); commands in tmp/design-1019pm/mob-v3/characters/final/FINAL-ART.md section 6; then `python tool/fold_manifest_final.py` in the app.
6. Morning summary to the owner: what is live, version 13 path, what he must do (upload v13 to closed testing, content rating + data safety, ANDROID_CERT_SHA256 = Play app-signing SHA-256 in Vercel for the email link).
7. Follow-ups: 150 vs 50 welcome credits (his decision); weekly Mob paper answer hold (C-dec 2 item 1); Mob live rooms (Phase B); Ask Mobi remaining capabilities (ASK-MOBI-VALUE.md); golden baseline drift (~110 stale goldens at base).

## 6. Commands and facts
Flutter: `MOCKMOB_FLUTTER_SLOTS=6 bash tool/flutter_locked.sh <args>` (slot max file %TEMP%\mockmob-flutter.lock.max = 6). Emulator lock %TEMP%\mm-emu-lock; AVD mockmob_budget -memory 3072; adb -e only; demo entry test/device_demo/demo_main.dart. Staging rig: 3104 (r11, shim 3114), 3105 (Mob v3 server, shim 3115), seed scripts/mob/seed-v3-staging.mjs (chai-* @example.com). Supabase prod isrxrxzjocewrdureyhp, staging onwkqxmjqjrhfbjjdydu. Vercel prj_uSolddribHQDl1mM5AKxg3O9qCIu / team_V5PhMz9hqV42vblUMcvhYqoN (env listing may be blocked by the permission classifier). Upload key fingerprint SHA-256 62:AC:58:08:...:EC:47. Codex images: account 2 signed in now.


## HANDOFF 20 Oct about 4:00 am (D159): every agent STOPPED; exact leftovers
- **Live (done):** main 48985a8d (deployment dpl_GNLLoKcKYZDo34nkpXbqMqnT5WSs): Play billing, web v13, Mob v3 (4 migrations on prod, MOB_V3_ENABLED on), Ask Mobi v13 web (credits buy jobs, Pro still pays, no migration). Rollback points: dpl_4nA9juLKE9wFKjPHRAcdtfx7Ffha (before Mobi), dpl_F8qxHxpnXyZPqjCEAFrPrBbSnE9L (before Mob v3).
- **App release ui/v17-release (wt-1020-app-rel) head 72af5155, clean:** merged bugs 6b659e43, mob-switch 449e8fde, mob-art 9cc7e7dc, mob-den 6ea7f777, mob-play e8a0d38e, pro-page 6cb1c9d2, wallet 536de4b5, finish 6fdfff26 (+ golden regenerations on the merged Folds art). pubspec still 1.0.16+12. NOT done: merge ui/v17-mobi; full unit run after the last three merges; demo emulator walk; version 13 build (Desktop\MockMob-build-13 does not exist yet).
- **ui/v17-mobi (wt-1020-mobi) head 096fa2db = STOP POINT** over 758b4547 (Where you stand, doubt thread, Fix it for good, goldens): its last 3 files were uncommitted work of a helper (App Ask Mobi v13 UI) stopped mid-way: review before merging.
- **Folds art:** idle, cheer, think for all 12 + parcel + seal are in the app (mob-art) and web (public/mob/folds); shrug, wave, Patang think redo NOT generated (FINAL-ART.md section 6; Codex account 2 resets 5:38 am).
- **Web leftovers (from the den/play owners):** D6 den room skeleton not wired; public /join/<code> page not v3-aware; sticker flights not live; podium first-place Fold head touches the lamp edge; signed-in walk of live Mobi flows not done (agents never sign in).
- **Owner steps:** upload v13 to Alpha; content rating + Data safety; ANDROID_CERT_SHA256; 150 vs 50 credits; Pro 149/150.
- **Next prompt:** docs/brain/NEXT-PROMPT-1020-AM.md (goal-first, 5-6 hour plan).

## PAUSE 20 Oct 5:30 am (session 604ced81, account usage 90%; window resets 9:00 am IST): every agent STOPPED, every dirty worktree has a STOP POINT commit
Blitz (D160/D161) results, all local branches, nothing pushed or deployed since main 48985a8d:
- **App v13 release** ui/v17-release (wt-1020-app-rel) 668df841 = STOP POINT over f345ebee (Ask Mobi v13 merged at e52a9490; uncommitted Wallet/Mob copy fixes were in progress: review; Wallet text still said "2 real CUET questions"/"Mobi job"). ui/v17-mobi finished at 361abc62. NOT done: full unit run on the final tree, demo walk completion (wt-1020-app-walk f345ebee has demo work), signed build 1.0.16+13, Desktop\MockMob-build-13.
- **Fix lists:** tmp/review-1020/FIX-WAVE-LENSES-1020.md (66 items; build blockers L-01..L-12, B-SUBMIT L-07b/L-08, live hotfixes L-09 blocking across Mobs, L-10 share-marks switch leak); per-surface reviews tmp/review-1020/*.md (FIX-WAVE-1020.md synthesis was stopped; merge the surface files).
- **Web branches ready to integrate (from 48985a8d, tested by their owners):** web/1020-web-practice-parity 6f4dde82, web/1020-web-goal-more eb37f6d5 (needs web/1020-goal-minutes fa635fc5 server + migration on prod), web/1020-web-subject-pages b2024553 (15 CUET pages; 9 subjects' copy needs one read), web/1020-web-onboarding-parity e22f7d34, web/1020-web-live-client fbbb8433 (behind live flag), web/1020-mob-polish 7bc2dd02, web/1020-join-v3 4a10d0f3, web/1020-set-password c3dfc2b4, web/1020-landing-health a68aba16, web/1020-paper-hold 54ff19a5 (+ app ui/1020-paper-hold 422811e1), web/1020-mob-live 6b0cf827 (Phase B server). Expect conflicts on Today (practice-parity strip vs onboarding name card) and subject pages vs landing.
- **App side branches:** ui/1020-small-fixes ba19dbbb, ui/1020-mob-live 99f5fde0 (STOP POINT). Marketing: mkt/1020-folds-kit 3d284a11. Analyses: check docs/brain/DECISION-WELCOME-CREDITS.md, OWNER-STEPS-1020.md, docs/design-decisions/pass-1020/MOBI-NEXT.md, Desktop\MockMob-store-listing\LISTING-v13.txt, tmp/walk-1020/GOLDEN-DRIFT.md (exist only if their agents finished).
- **Next after 9:00 am:** (1) one app owner: fix build blockers L-01..L-12 on ui/v17-release, full unit, demo walk, build v13 to Desktop\MockMob-build-13; (2) one web integrator: merge the web branches above into web/1020-release, suites, deploy (D156) with smoke + STATUS, plus L-08 legal pages and L-09/L-10 hotfixes; (3) Folds shrug/wave via Codex; (4) morning summary. Keep waves small: the blitz burnt about 80% of a window in 80 minutes.

## MORNING 20 Oct 11:05 am (session 604ced81): goal met
- **Version 13 ready:** C:\Users\atish\Desktop\MockMob-build-13 (mockmob-1.0.16+13-sells.aab SHA-256 cfc2dd9e..., mockmob-1.0.16+13-arm64.apk 50b459d6..., README, symbols, OWNER-STEPS.md). Built from ui/v17-release 19ac295b (head fe076156 adds goldens only). Signer = upload key 62:AC:58:08...EC:47. Blockers L-01..L-12 fixed; Folds shrug 12/12, wave 11/12 (Stamp wave missing, idle fallback); full unit+widget 7,337 pass; 454 intended goldens regenerated; 17 golden failures not from this release (4 Mob title cut at text 1.3 = real older bug B1; 13 noise/clock); demo walk ~75 shots (tmp/walk-1020/app-v13/r2, JUDGEMENTS.txt), 6 findings fixed; launch check on an x86_64 twin (emulator cannot run arm64).
- **Web live:** main 36492ed2 (dpl_8EU7duoJuwKFQuU8WEe5uPWyGhT9; rollback dpl_6uV9Z3cLWcFeHGcXcpBx85fJxn1M): hotfixes L-09, L-10, L-01 server, L-08 legal pages, L-07b from=app; 13 branches merged (practice/colleges parity, goal More + daily_minutes migration 20261020110000 on prod with undo, 15 CUET subject pages, onboarding parity, mob polish, join v3, set password, landing health, paper hold, live rooms code with MOB_LIVE_ENABLED off), Folds shrug/wave on web. Not applied: 20261020100400_mob_v3_live (live off until presence fix L-55). Today shows "Your colleges" twice (strip + older card), kept per his D126 "the block stays": revisit.
- **Docs for him:** docs/brain/DECISION-WELCOME-CREDITS.md (recommend 50: drop the one-time 100 signup grant), OWNER-STEPS-1020.md (= Desktop\MockMob-build-13\OWNER-STEPS.md), Desktop\MockMob-store-listing\LISTING-v13.txt, docs/design-decisions/pass-1020/MOBI-NEXT.md, docs/marketing/FOLDS-LAUNCH-KIT.md (branch mkt/1020-folds-kit).
- **Open:** Stamp wave pose; B1 Mob title at large text; Mob live rooms (presence fix L-55, migration 100400, Realtime public access off, his go); app live client ui/1020-mob-live STOP POINT 99f5fde0; ANDROID_CERT_SHA256 (his); remaining MEDIUM/LOW items in tmp/review-1020; welcome credits and Pro 149/150 (his decisions).

## 20 Oct ~12:30 pm: owner Play/Vercel steps DONE
Version 11 approved on the closed track; version 13 sent for review (he sent it before reading the steps; fine). Content rating redone (interact yes, digital purchases yes, no loot boxes, online/AI content yes, educational yes); Data safety Purchase history added. ANDROID_CERT_SHA256 set in Vercel Production and redeployed (dpl_13vbidun9MJtWKaNPub88Hj5NfSY): live assetlinks.json lists the Play app-signing key B2:45:68:DA:...:05:C9 and the upload key 62:AC:58:08:...:EC:47. Pro on Play stays Rs 149; welcome bonus 100 kept (150 total). Play "Automatic protection" (block unofficial installs) is ON: testers install from Play, not the APK. Next: his feedback on version 13; then the improvement list (real-device walk, Folds life, live rooms, remaining review items, smart layer).

## HANDOFF 20 Oct PM (session 604ced81, written ~3:45 pm at account usage 85%, context 86%)
His words today: OWNER-FEEDBACK-2026-10-19.md from "Owner, 20 Oct about 12:05 pm IST" (K1-K11, D165-D176).

**LIVE (production):**
- Website main bd9e03ea7 (code fb1e22e5, deployment dpl_2juF25MkVrVzCqrWFMXDwiGMHjBP; a docs-only build dpl_Fo9PLU76SS13bfLGP4sHbDXqKk1A was still BUILDING: confirm it reaches READY with FIRST_FULL_MOCK_ENABLED=false). Contains: the 11 am release (36492ed2), referral credits (2ffaf29d, REFERRALS_ENABLED=true; 50 welcome, +100 each after the friend's 5 answers; migration referrals applied, total credit_balance unchanged 112311/1545 users), web Mob explainer, Mob formats server + web client with MOB_FORMATS_ENABLED and MOB_LIVE_ENABLED UNSET; migrations 20261020095603 mob_v3_live and 20261020095712 mob_v3_formats applied (hashes match).
- D175: FIRST_FULL_MOCK_ENABLED=false (env aldFAoz9qJXBPpAQ): no free first full mock; /pricing line gone.
- ANDROID_CERT_SHA256 set (Play key B2:45:68:DA...05:C9 + upload key); assetlinks live.
- App version 13 (1.0.16+13) in closed-testing review (version 11 approved). Play Console: content rating redone, data safety Purchase history added.

**SUPABASE (URGENT, K11/D176):** org xnhuqcazqyqvnsodmqyf egress 14.42 GB of 5.5 GB (Free); grace until 22 Oct, then 402s on production AND staging until the quota refills at the next billing cycle (or an upgrade). Owner refuses $25 Pro during testing. Cause: staging (onwkqxmjqjrhfbjjdydu) is in the SAME org and agent walks, seeds and test runs hammered it; no weekly usage check. Done: agents told not to use staging. Waiting on him: billing-cycle end date (Billing > Upcoming invoice) and egress split per project (Usage > Egress). Next: move staging to its own free org (dashboard project transfer, he clicks); cut production egress (top queries, select only needed columns, caching); add a usage check to every session; never run agent walks against staging until the new cycle; if the cycle resets after ~22 Oct, tell him plainly the outage window and that Pro for one month (downgrade after reset, credited) is the only instant fix.

**APP BRANCHES (all from ui/v17-release fe076156 = version 13 source; none merged; nothing on a phone yet):**
- ui/1020-v14-polish 44073e9f (wt-1020-v14-polish): K1 Day mode, K3 You plan strip (credits + Upgrade to Pro), K4 Pro table, K6 Wallet; done, tests green. MUST change: remove "your first in each subject is free" copy (D175).
- ui/1020-finish-reveal 0942a34e (wt-1020-finish-reveal): K7 mark-sheet reveal on every paper; done, 7,138 tests. Remove any first-free wording.
- ui/1020-referrals ed2a8b93 (wt-1020-referrals-app): D165 app side; done.
- ui/1020-mob-explainer 1a7a622c (wt-1020-mob-explainer): D166/K9 explainer + one-question setup; builder STOPPED at 3:45 pm (usage 90%) just before its demo-mode emulator walk; code, tests and walk fixes 1-2 committed. Left: the demo walk of the explainer and setup, then merge.
- ui/1020-mob-formats d1d2c095 = STOP POINT (wt-1020-mob-formats-app; 12 files were uncommitted): race, Full mock together and the live client in the one Start a game sheet; stopped at 3:45 pm while writing the race goldens and frame strips. Review the STOP POINT diff, finish the goldens and frame strips, full unit, then merge.
- ui/1020-mob-live 99f5fde0 STOP POINT (merged into mob-formats as its live base); ui/1020-small-fixes ba19dbbb; ui/1020-paper-hold 422811e1.

**DECISIONS WAITING / OPEN:**
- Mob V4 (docs/design-decisions/pass-1020/MOB-MINIMAL.md "MOB-V4"; mock-ups tmp/design-1020/mob-minimal): APPROVED to build (D174), with Mob hours YES, a clear Pro call to action for Free members in Full mock together, both streaks visible, results as a short sequence plus celebration screens. NOT built yet.
- Full mock together rule: Pro starts; Free members pay 50 credits (no free first mock now, D175); Pro sits free. The SERVER currently lets everyone sit free: enforce the rule before MOB_FORMATS_ENABLED=true.
- Live rooms: owner must turn OFF Supabase Realtime "Allow public access"; app live client must ship; then MOB_LIVE_ENABLED=true.
- Stamp's wave pose and a desk-lamp image still to generate (Codex image route, FINAL-ART.md section 6).

**NEXT (in order):** (1) Supabase egress plan above. (2) Version 15: merge v14-polish, finish-reveal, referrals, explainer, mob-formats (+ small-fixes, paper-hold) into a v15 branch; remove first-free copy; build Mob V4; full analyze + unit + touched goldens; demo-mode walk only (NO staging); signed build to Desktop\MockMob-build-15. (3) Enforce the Full mock together pricing on the server, then MOB_FORMATS_ENABLED=true. (4) Live rooms after his Realtime click.
- **Supabase update (3:35 pm):** his Billing page shows the overage was in the PREVIOUS cycle and the last invoice is 21 Sep, so the cycle resets on the 21st: the quota refills 21 Oct, before the grace ends 22 Oct. Most likely no outage and no payment. BUT no second grace: the cycle 21 Oct-21 Nov must stay under 5 GB egress (~160 MB/day). He is confirming the "Upcoming invoice" date and sending the per-project egress split.

- **All agents STOPPED at 3:45 pm (usage 90%).** Leftover Dart processes and the emulator were killed; the emulator lock was removed. Web explainer branch web/1020-mob-explainer c4546a70 is already merged and live.

## SESSION b7e1b5da, 20 Oct from 4:06 pm (goal: version 15 to Play review tonight, D179/D180)
- **Supabase (parked, D178):** cycle 21 Sep-21 Oct confirmed (refills 21 Oct, grace ends 22 Oct); org egress 15.72 GB; spikes 7 Oct 3.8 GB and 18 Oct 3.3 GB were agent days. Staging transfer to org `mockmob-staging` is BLOCKED during grace: owner retries 22 Oct afternoon. Staging rig on 3104 killed 4:10 pm; no staging traffic since 5:30 am. D177 plan in OWNER-FEEDBACK. Egress cut: workflow on web/1020-egress (wt-1020-egress), first commit 2340ccb2d (inventory skip-if-unchanged), not deployed yet.
- **Live:** main 85c715756 = D175 hotfix (pricing comparison row no longer promises a free first mock), deployed and checked 5:17 pm.
- **Server:** web/1020-mob-fulltogether-price 185eaaf2b (wt-1020-fulltogether): Pro starts, Free sits for 50 credits, Pro free; contract APP-API-CONTRACT 2.12 (camelCase: v3.starts.mock, game.price, MOCK_PRO_REQUIRED 403, MOCK_CREDITS 402); test:mob 308, billing 448, build ok. Not merged/deployed.
- **App v15 base:** ui/1020-v15 (wt-1020-v15app), agent v15-integrator: merged small-fixes, paper-hold, referrals, v14-polish, finish-reveal, mob-explainer; D175 copy removal + full unit in progress.
- **Mob modes:** ui/1020-mob-formats (wt-1020-mob-formats-app), agent mob-formats-finisher: a5142e33f pricing client; aligning to the final camelCase contract.
- **Mob V4:** spec docs/design-decisions/pass-1020/MOB-V4-BUILD.md; branches ui/1020-v4-den (29283d0f1 part 1), ui/1020-v4-sheets, ui/1020-v4-results (all from a5142e33f), web/1020-mob-hours (Mob hours server at v3.hours). Workflows wf_0a2d44a4-ae6 (results track) and wf_6cde204f-70c (den, sheets, hours restart); coordination file tmp/v4-coord.md (agents never SendMessage each other: it wakes duplicates).
- **Owner feedback sweep:** workflow wf_4fa546de-309 writes tmp/review-1020/V15-OWNER-SWEEP.md (fix packages for after integration).
- **Next:** merge mob-formats + V4 branches into ui/1020-v15; sweep fix wave; full analyze/unit/goldens; demo-mode emulator walk Night+Day; signed build 1.0.17+15 to Desktop\MockMob-build-15; then web release (fulltogether price, Mob hours migration, V4 web, egress cut, MOB_FORMATS_ENABLED after price is live).

## PAUSE 20 Oct 6:28 pm (session b7e1b5da, account usage 91%): every agent STOPPED; exact stop points
Owner switches accounts; THIS session resumes (same session). Never SendMessage to workflow agents (wakes duplicates); coordination file tmp/v4-coord.md.
- **ui/1020-v15** (wt-1020-v15app) 18aa9341c: 6 merges + D175 copy removal (72906a94d) + goldens. Clean. Integrator was stopped before its final full unit report: re-run full analyze + unit.
- **ui/1020-mob-formats** (wt-1020-mob-formats-app) d97a2e167 DONE: races, Full mock together on the final camelCase contract (sit sheet, Pro CTA, MOCK_PRO_REQUIRED/MOCK_CREDITS), live client. Full suite 9,802 pass / 141 fail = 140 old non-Mob golden drift + 1 fixed motion guard.
- **ui/1020-v4-den** (wt-1020-v4-den) 70f9a64b0: den built + review fixes (two fixer runs). Clean. Needs: final look at goldens vs mock-ups, the friend-join/reaction/desk act calls (API from results track, see v4-coord.md), ResultsRun.showPending on den open.
- **ui/1020-v4-sheets** (wt-1020-v4-sheets) 4e61e9209: sheets built + review fixes. Clean.
- **ui/1020-v4-results** (wt-1020-v4-results) STOP POINT 8ac38ab9f over 5ded98382: reviewer fixes 1-3 committed (eyes without seams, X to den, rule box in view); fixes 4+ (Fix it together headline/one key, parallel reads + loading frame, podium your-place card + 3.5 s), A9 lobby For-you card, haptics, hours crown/ticks, 4.3 frame strips, acts API were IN PROGRESS: review the STOP POINT diff (tmp/review-1020/V4-RESULTS-REVIEW.json has the fix list).
- **ui/1020-v15-calm** (wt-1020-v15-calm) STOP POINT 2b78a0576: D181 first Pro ask waits, D183 usage data on for Rather not say, delete-account Play warning; was on onboarding save_step copy. Finish + tests.
- **ui/1020-v15-invite** (wt-1020-v15-invite) STOP POINT d51a71625: Play Install Referrer + "Have a friend's code?" row + live flag + D182 copy; was opening goldens. Finish + tests + debug apk compile check.
- **web/1020-referral-any** dabbf31d6 DONE: D182 migration 20261020150000_referral_any_practice (+undo, NOT applied), Android /r/<code> -> Play referrer; billing 440, auth 125, app 962, build ok.
- **web/1020-mob-fulltogether-price** 185eaaf2b DONE. **web/1020-mob-hours** 25940b5f6 (two fix rounds; RENAME its migration 20261020150000_mob_hours -> 20261020151000 at web integration: version clash with referral-any).
- **web/1020-egress** STOP POINT d8c35687e over 8e5d00430: F1 inventory skip-if-unchanged + many A/F cuts; the workflow was in its fix stage; verification not done.
- **Next after the switch:** (1) finish v4-results, v15-calm, v15-invite (3 agents); (2) one integrator merges mob-formats, v4-den, v4-sheets, v4-results, v15-calm, v15-invite into ui/1020-v15, fixes Mob explainer slide 3 (K9: real modes, no "Coming soon"), full analyze + unit + touched goldens; (3) demo-mode emulator walk Night + Day with screenshots (tmp/walk-1020/app-v15), fix what it shows; (4) signed build 1.0.17+15 to Desktop\MockMob-build-15; (5) web release: merge fulltogether, referral-any, mob-hours, egress, V4 web; apply the three migrations with pre/post checks; MOB_FORMATS_ENABLED=true after price is live.
- **Next prompt for any agent (Codex or Claude):** docs/brain/NEXT-PROMPT-1020-EVE.md.

## PAUSE 20 Oct 7:11 pm (session e5b2f75b, account usage 91%): every agent STOPPED; exact stop points
Owner rules this evening: D185 (Get Pro, never "See Pro plans"; no text bombardment, visual first), D186 (sheet and slide 3 approved; NO regressions; check the brain when unclear), D187 (record findings in Continuum as they happen). Next prompt: docs/brain/NEXT-PROMPT-1020-NIGHT.md.
- **ui/1020-v15** (wt-1020-v15app) 717aa3a89, clean: merged ui/1020-mob-formats, ui/1020-v4-den, ui/1020-v4-sheets, ui/1020-v4-results + integration (den plays achievements through ResultsRun.showPending; Week stitched reads v3.hours; all six V4 sheets wired; How the Mob works -> explainer replay; Your Mobs Start another -> explainer/setup; den header chip fix; own game rows "Your sprint"); explainer slide 3 "Ways to play" (K9: Sprint, Race 5/10, Your own round, Full mock together, Every week box: Mob paper + Mob hours; no Coming soon); Sit the full mock sheet redesigned (D185, approved D186). `flutter analyze` clean; Mob unit+widget 712/712 pass. Goldens NOT yet regenerated on the merged tree (Mob v3 goldens drift from merges; ~140 old non-Mob goldens are known drift).
- **ui/1020-v15-invite** (wt-1020-v15-invite) 3e9eb69e6, clean: agent finished review commits (referrer read exactly as the website sends it, hardened claim, Android Play Store query in the manifest, wallet row room + goldens, claimer can never fail the first build). Its final report never arrived: re-run analyze + referrals/wallet tests; debug/release APK compile not confirmed.
- **ui/1020-v15-calm** (wt-1020-v15-calm) STOP POINT 353a98fc9 over 2b78a0576: the review agent's uncommitted work (74 files incl. new onboarding goldens) committed unreviewed; it was running the touched-area unit tests. Review the diff, run analyze + onboarding/pro_nudge/you/core_data/billing tests.
- **Not wired (follow-up, not a blocker):** den join/reaction acts (DenActPlayer in widgets/fold_acts.dart) into den_stage (desk act and sticker flights already run); A9 MockLobbyBody (the sit sheet is the lobby). v3.fix (den Now card steps 2-3) has no server field yet: those steps never show.
- **Emulator:** AVD mockmob_budget was booted at 6:56 pm by this session; lock %TEMP%\mm-emu-lock (owner file says e5b2f75b). A new session may take the lock over (one emulator only).
- **Next:** merge ui/1020-v15-calm and ui/1020-v15-invite into ui/1020-v15; analyze; full unit/widget; regenerate Mob goldens on the merged tree and open the changed ones; demo-mode walk Night + Day (360 dp, text 1.0 and 1.3) with screenshots in tmp/walk-1020/app-v15 + JUDGEMENTS.txt; fix; signed 1.0.17+15 to C:\Users\atish\Desktop\MockMob-build-15; then web release.

## 20 Oct NIGHT (session 604ced81, 7:18 pm to ~10:30 pm): version 15 finished in one window (owner D189, D190)
- **App, ui/1020-v15 9e6ad500f built (+ goldens-only commit after), version 1.0.17+15, signed AAB + arm64 APK in C:SERSTISHDESKTOPMOCKMOB-BUILD-15 (AAB SHA256 4BCA8F3C..., UPLOAD KEY 62:AC:58...). FULL SUITE 10,491 PASS, 117 FAIL = KNOWN GOLDEN DRIFT + 2 FLAKY; RELEASE X64 LAUNCH CHECK OK; FINAL DEMO WALK DEN/START/SIT/YOU/WALLET NIGHT+DAY OK.** Merged tonight on top of 717aa3a89: ui/1020-v15-invite (Have a friend's code row, Play install referrer), ui/1020-v15-calm reviewed by 20 agents then fixed (555d8e45f, 31bf4bb80: consent never promotes an age band, D181 first result per attempt id, returns to Today counted by the router, privacy unanswered key), ui/1020-v15-calm-ui (first-session Pro sheet visual first with renewal stated, save step age note one line; 6e1b5a239, 02a286aaa), ui/1020-den-acts (d58d15862: a friend who joined hops in, a sticker makes the Mob cheer), ui/1020-mob-polish (7 commits: chain chip beside the gear, Your Mob never cut (B1), Week stitched pennant hero, sit sheet price row flush, short Free start row with Pro starts it tag, Mob copy without "last", This week sheet), my copy fixes 8cc4c9add (Get Pro on Wallet and inline links, Rather not say everywhere, short Mob Pro ledes), motion guard 94623c2a9 (shared curves in Fold acts). Mob goldens regenerated 06dbe24a0 and judged against the mock-ups (tmp/v15-night/golden-judge.json).
- **Website, LIVE: main 7f7e3f19f** (release 2c71cb810 + STATUS): Full mock together price enforced on the server, referral after any one practice (D182), Mob hours, egress cuts (19 commits reviewed), v3.fix for the den Now card steps 2-3 (APP-API-CONTRACT 2.14), D183 consent on server + Profile + privacy policy (updated 20 Oct, parent route, crash reports disclosed). 7 migrations applied on production 9:00-9:15 pm (list and checks in STATUS.md). MOB_FORMATS_ENABLED=true (env xJZ4QrcRIdcShmYI). Rollback deployment dpl_4bn4VVutv4Lyxf2JE1yLyCMrTQVG.
- **Known drift (not regressions, proven on the base):** ~117 old golden images (onboarding ladder/rhythm/taste/balance, credits, tools, account sheet, rhythm, art scenes, etc.): tmp/v15-night/known-drift.txt. Flaky: run_r5_flag/run_r6_done (Kabir's eye 0.08%), billing_sub_renewal_off.
- **Follow-ups for the next session:** copy sweep of "lost"/"last" outside the Mob (Today "Repair your last paper", "You lost 99 marks in Goodwill", result "You lost N marks", ask doors); the den's studying chip timing in den_stage (StudyDesk, goldens only); web Mob V4 (MOB-MINIMAL W1-W7) and the web den fix card; MOB_LIVE_ENABLED after the owner turns off Supabase Realtime "Allow public access"; staging moves to its own org on 22 Oct; the stopped 4-build walk left 298 screenshots of build A in tmp/walk-1020/app-v15/A-formats-free (contact sheets in ../contact).

## HANDOFF 20 Oct 11:25 pm (session 604ced81, usage ~91%): version 15 closed, version 16 next
- Version 15 (1.0.17+15) is in Desktop\MockMob-build-15; the owner tested it on his phone (feedback 11:20 pm, D191). It is NOT being sent to review: version 16 (1.0.18+16) is the final closed-testing build, tonight.
- Owner findings on v15: the Mob explainer never plays automatically on a fresh account (it is wired only to Start/Join/See how it works); the invite card in credits shows at the wrong time; no welcome-credits + invite pop-up after sign-up; Live hidden (MOB_LIVE_ENABLED unset, waits for his Supabase Realtime switch); delete only records a request, so a "deleted" account kept working and showed odd credits (a fresh account showed 50 -> 39, correct).
- Website feedback (phone first): pricing revamp, "Get access for 99" like the app, hero like the app, subjects first with commerce preselected, scroll story bigger on phone with better copy, Mistake Lab timer animation frozen, bot screens need depth in dark mode, Razorpay monthly setup guidance.
- Next prompt: docs/brain/NEXT-PROMPT-1020-V16.md (copy on Desktop as NEXT-PROMPT-V16.md). The v15 verify prompt is withdrawn.

## 21 Oct 12:58 am (session b7e1b5da, Fable 5.1): version 16 in flight
- **Owner tonight:** D192 (Fable orchestrates), D193 (web ₹99), D194 (hero line stays), D195 (Realtime public access OFF; Razorpay plan id set as RAZORPAY_PLAN_ID_PRO_MONTHLY_99 on Vercel; MOB_LIVE_ENABLED=true set; webhook URL fixed to www). Plan: docs/brain/V16-PLAN.md.
- **App ui/1020-v16 (wt-1020-v16) eff27472d:** merged ui/1020-v16-nudges 879068666 (A4: rules by Fable + Opus card/sheet/facts; demo MOCKMOB_DEMO_NUDGE=<kind>), ui/1020-v16-welcome 4dad2e850 (A1 welcome-credits sheet + warmer invite copy; demo DEMO_WELCOME_CREDITS=true), ui/1020-v16-mobwelcome b93276a66 (A3 welcome room then explainer on the first Mob tab visit; demo MOB_V3_SCENARIO=fresh). Analyze clean. STILL RUNNING: ui/1020-v16-sweep (A2 invites/deletion clarity, A6 copy sweep, studying chip). Then: full unit suite, demo walks Night/Day, signed 1.0.18+16 to Desktop\MockMob-build-16.
- **Web web/1020-v16 (wt-1020-web16) dabf26d1c:** merged onboard c9ee1b5fe (W4), landing 864f7816d (W5/W6/W7), pricing ef5837ecb (W1/W2), hero 9156786a8 (W3), invite copy 7e410cc06, deletionRequestedAt in /api/auth/me 53c2022b7. Suites on the tree before hero: app 980, billing 453, mob 351, auth 125, recovery 637, landing 73, all green. Next: npm ci restore of mockmob-next/node_modules (my worktree removal followed junctions and emptied it, 12:42 am), then suites + eslint + build, browser check 390/1440 Night/Day, push main, smoke (monthly ₹99 + live rooms go live with it), STATUS entry.
- **Disk:** 1 GB free at 12:20 am -> 107 GB after deleting build output and 197 finished worktrees. scripts/sweep_build_output.sh (before builds, end of waves) and scripts/remove_worktree.sh (junction-safe). 21 dirty worktrees kept.
- **Open:** web hero phrase "See the lost marks." (approved rotation; width-pinned by tests) left for the owner's call like D194; web Wallet "opens the invite section" lands at the Wallet top; nudges and welcome need the emulator walk.

## 21 Oct 2:28 am: version 16 app at the test and walk stage
- **Website release 16 LIVE:** main 832e88031 + STATUS 0b7d6bc03 (deployment dpl_G17kKZkn2bw24a5SGL8xNaXHxv95, rollback dpl_HsKRboUQsi1oUdC8ffrWV9QsnHpT). Monthly ₹99 (RAZORPAY_PLAN_ID_PRO_MONTHLY_99) and live rooms (MOB_LIVE_ENABLED) on. Owner fixed the Razorpay webhook URL to www.
- **App ui/1020-v16 (wt-1020-v16):** 0fd6f644a merge of ui/1020-v16-sweep (A2 invites, deletion note, A6 copy sweep, studying tag) + referral goldens commit; analyze clean; full suite 10,638 pass / 118 fail (expected = known drift 111 + flaky; the rerun capturing failure names runs now: tmp/v16-unit-fails.txt). Signing inputs staged in wt-1020-v16/flutter_app (key.properties, prod.json; git-ignored).
- **Walk:** agent v16-walk in wt-1020-v16walk (ui/1020-v16-walk = 0fd6f644a): demo x64 builds (fresh + DEMO_WELCOME_CREDITS + MOB_V3_SCENARIO=fresh; MOCKMOB_DEMO_NUDGE kinds), Night and Day, screenshots to tmp/walk-1021/app-v16, JUDGEMENTS.txt.
- **Promo kit (D196/D197):** Desktop\MockMob-promo-kit (PROMPT.md price ₹99 only); another session (7a597d) is building the teaser in Claude Motion.
- **Next:** classify the 118 failures (regenerate only intended goldens; any real failure fixed), fix walk findings, bump to 1.0.18+16 with `bash tool/build_release_aab.sh --bump --name 1.0.18 --sell` (+ arm64 APK as in 20 Oct NIGHT), launch-check an x64 release APK, copy AAB/APK/README/symbols/OWNER-STEPS to Desktop\MockMob-build-16.
- Time-sense "last" ("since your last look", "in each of your last 3 mocks") stays: v13-approved and test-pinned; the rule is applied to "lost"/"behind"/"last place" senses.

## 21 Oct 3:52 am: VERSION 16 DONE (session b7e1b5da, Fable 5.1)
- **App 1.0.18+16 signed:** C:\Users\atish\Desktop\MockMob-build-16 (mockmob-1.0.18+16-sells.aab SHA-256 da7d67a7..., arm64 APK, symbols and mapping, README.txt, OWNER-STEPS.md). Built from ui/1020-v16 f72207c27 (tree dcd87253f + version bump). Owner uploads to Alpha (sent 3:52 am). x64 release launch check on the emulator: MainActivity up, no fatal exception (tmp/walk-1021/v16-release-launch.png).
- **Website release 16 live** (main 832e88031; STATUS entry 0b7d6bc03): see the STATUS entry; monthly ₹99 and live rooms on.
- **Evidence:** analyze clean; full suite 10,639 pass / 117 fail = known drift (tmp/v15-night/known-drift.txt) + start_v13_following_picked stale; demo walk 140 shots (tmp/walk-1021/app-v16, JUDGEMENTS.txt), no blockers, 3 high fixed; web suites green, build ok, browser QA no blockers.
- **Next session (owner's words tomorrow first):** the three medium walk items (explainer slides 3-6 text density; Today date at text 1.3; repairOpen note next to the repair hero); the web hero rotation phrase "See the lost marks." (owner's call, like D194); Day theme product cards on the website; dense /cuet pages; nudges and welcome sheet on a real account; Supabase staging transfer on 22 Oct afternoon (grace ends); Mob hours on the web; promo video (Desktop\MockMob-promo-kit, another session is cutting the teaser in Claude Motion).
- **Branches merged into ui/1020-v16:** nudges, welcome, mobwelcome, sweep, fixa (Wallet deep link), walk (Mob clips). Worktrees kept: wt-1020-v16 (app, final), wt-1020-web16 (web, = main), wt-1020-v15app/walk, wt-v15-3; the v16 side worktrees can be removed with scripts/remove_worktree.sh.
- **Disk:** 1 GB -> ~120 GB free; rules in scripts/sweep_build_output.sh and remove_worktree.sh (junction-safe). Owner's own: Documents\Wondershare 119 GB.
