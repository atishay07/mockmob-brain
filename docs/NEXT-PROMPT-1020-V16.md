Continue MockMob as CEO/CTO in a FRESH session (Claude Code or Codex). Goal tonight, in ONE pass: app VERSION 16 (1.0.18+16), the final closed-testing build, signed in C:\Users\atish\Desktop\MockMob-build-16, plus the phone-first website pass, both deployed and checked (owner D191). Version 15 verification is closed.

START
1. continuum_start with project "mockmob". Run `date` (IST, 12-hour). Record the owner's words verbatim with real times in docs/brain/OWNER-FEEDBACK-2026-10-19.md.
2. Repo C:\Users\atish\Desktop\mockmob copy\mockmob-next (branch feat/app-and-web holds the docs). Read:
   - docs/brain/NOW.md, last section "20 Oct NIGHT".
   - OWNER-FEEDBACK-2026-10-19.md from "Owner, 20 Oct 11:20 pm" (his full feedback, verbatim, D191) and D177-D190 above it.
   - docs/design-decisions/pass-1020/MOB-MINIMAL.md and DECISION-WELCOME-CREDITS.md.
3. App base: ui/1020-v15 at d71078fe6 (worktree wt-1020-v15app; v15 was built from 9e6ad500f). Cut ui/1020-v16 from it. Web base: origin/main 7f7e3f19f (live).

THE VISION (unchanged)
- MockMob is CUET UG 2027 prep for 16-17-year-olds, many new to apps. It is built on unlimited mocks from one central bank: find where marks slip, fix each mistake, check the fix holds.
- It must feel premium, alive and genuinely smart.
- The Mob's moat is experience: UI, character animation, motion.
- Clean means easy to find and never overwhelming. It does not mean fewer features. Every approved feature stays.

APP, VERSION 16 (owner's words, 11:20 pm)
A1. **Welcome pop-up after sign-up.** On the first screen after a new student signs up, show a pop-up (not a walkthrough).
   - It says the 50 welcome credits are theirs and invites them to earn more by inviting friends: "you both get 100 credits when your friend finishes one practice".
   - Make it intuitive and interesting, visual first: the credits as a figure, the Folds or Mobi, one line per idea, Invite key and Not now.
   - Current invite copy is "boring": rewrite it everywhere to be warm and a little playful, within the copy rules.
   - Show it once per account. Never on top of onboarding.
A2. **Invite card in the credits section.** The owner says it shows "only when it's not" right. Check when it should show (invites live, student can still invite, monthly cap not reached) and make it correct.
   - Verify the "Have a friend's code?" row appears for a new account (it did not for him).
   - Verify the credits figure for a new account. His fresh temp-mail account went 50 to 39 after one practice, which is correct.
   - Explain the "150/200" he saw earlier: it was on an account he had deleted. Delete only records a request, and the account is still usable until deletion is processed. Check that this is clear on the delete screen and after sign-in, and fix if not.
A3. **Mob first visit.** The explainer did not play automatically on a fresh account. Today it plays only from Start a Mob, Join or "See how it works" (mob_v3_nav.dart startMob/joinMob).
   - Fix: the first time a student opens the Mob tab, play a short WELCOME animation (the Folds arriving in the den, premium motion), then the How it works slides.
   - Once per account. Reduced motion respected.
A4. **Smart pop-ups and nudges**, like good consumer apps, never pushy and within D181.
   - Guide a student who is not doing something: no practice today, an unfinished repair, a Mob game waiting, credits running low, a friend joined, a streak at risk.
   - Point to Pro at real limits. Point to Invite at good moments, such as after a good result or when credits are low.
   - At most one per session, each dismissible and remembered.
   - Design the full set first (when, where, words, look), then build.
A5. **Live mode in the Mob.**
   - Guide the owner one screen at a time to turn off Supabase Realtime "Allow public access" (Supabase dashboard, project isrxrxzjocewrdureyhp, Realtime settings) and ask for a screenshot.
   - Then set MOB_LIVE_ENABLED=true on Vercel production and redeploy.
   - Check that "Live, together now" appears in Start a game and a live room works in demo mode.
A6. **Be creative.** Beyond his direction, find what to improve, perfect or double down on, from the 20 Oct walk screenshots (tmp/walk-1020/app-v15) and your own walk. Known items:
   - "lost"/"last" copy outside the Mob, for example Today "Repair your last paper", "You lost 99 marks in Goodwill", result "You lost N marks", ask doors, and the welcome hero "Every lost mark has a pattern" (ask him before changing his approved hero);
   - the den "studying" chip timing (den_stage StudyDesk).

WEBSITE, PHONE FIRST (owner: "that's where the landing page matters the most")
W1. **Pricing page:** an entire revamp, visual first, like the app's Pro page (one plan, Get Pro, Rs 149 a month).
W2. **"Get access for 99"** (find it on the site): rebuild it like the app's Pro/Get Pro flow, and check the price is right.
W3. **Landing hero (the first section):** make it like the app's welcome (Mobi, the lamp scene, one line, one key).
W4. **Onboarding question screen:** ask subjects first.
   - Commerce preselected: Accountancy, Business Studies, Economics, and the finance/maths option the app uses. Check the exact CUET subject names in the bank.
   - One big key to accept the default.
   - Most students are commerce.
W5. **The scroll story** ("you lost marks somewhere / MockMob shows you where / picks the chapter"): better copy, and on phone it must fill most of the screen.
   - It is perfect on desktop (half-screen animation beside the text) but too small on phone.
   - Resize it for the 390 px phone.
W6. **Mistake Lab:** the time animation is frozen.
   - It should play when it scrolls into view, not once on page load.
   - The others (change, repair, swap) work: match them.
W7. **Bot (Mobi) screens:** they look good but need more depth and effects. In dark mode their screen background is black and merges with the page; give it a surface that separates.
W8. **Razorpay:** guide the owner step by step to set up the monthly Pro plan for the website (plan, webhook, keys; RAZORPAY_* env vars exist on Vercel; RAZORPAY_PLAN_ID_PRO_MONTHLY). Find why the website is not on monthly yet and finish it. Ask him for screenshots; never type his credentials. The app's Razorpay comes later.
Web checks: real browser at 390 px first, then 1440, Night and Day; screenshots looked at; suites; `next build --webpack`; deploy by pushing main (D156); smoke.

FACTS AND COMMANDS
- **Flutter:** only via `MOCKMOB_FLUTTER_SLOTS=6 bash tool/flutter_locked.sh <args>` in flutter_app, with GRADLE_OPTS=-Dorg.gradle.daemon=false.
- **Emulator:** one only. AVD mockmob_budget, -memory 3072, lock %TEMP%\mm-emu-lock, `adb -s emulator-5554`. A release APK for the emulator needs `--target-platform android-x64`; the arm64 APK will not run there.
- **Demo builds:** `bash mockmob-next/tmp/v15-night/build_walk.sh <scenario> <billing>` (scenarios formats, heavy, fresh, mockdone; billing free or pro) in a separate worktree (wt-1020-v15walk). Never build and test in one worktree at once.
- **Signed build:**
  - In flutter_app run `bash tool/build_release_aab.sh --bump --name 1.0.18 --sell`, and check the versionCode is 16.
  - Then build the arm64 APK the same way as 20 Oct NIGHT in NOW.md.
  - prod.json: copy from wt-v15-3/flutter_app/dart_defines.
  - key.properties: copy from C:\Users\atish\MockMob-keys. NEVER print or commit keys.
  - Check the signer SHA-256 is 62:AC:58:...:EC:47.
  - Launch-check an x64 release APK.
  - Copy the AAB, APK, README with SHA-256s, symbols and OWNER-STEPS.md (upload to Alpha, replacing 15) to Desktop\MockMob-build-16.
- **Known golden drift:** about 117 old images that fail on the base too (mockmob-next/tmp/v15-night/known-drift.txt). Do not chase them. Flaky: run_r5_flag, run_r6_done, billing_sub_renewal_off.
- **Website:** node_modules is a junction. Suites: npm run test:mob / billing / app / auth / recovery. Supabase production is isrxrxzjocewrdureyhp. Vercel project prj_uSolddribHQDl1mM5AKxg3O9qCIu, team team_V5PhMz9hqV42vblUMcvhYqoN.

HARD RULES
- No walks, seeds or tests against Supabase staging or production. Use demo mode and local tests only. Production touches are allowed only for deploys, migrations (with an undo, and checks before and after) and a smoke check.
- Never create accounts or set passwords on the live site; headless browsers only; never touch his phone.
- Agents: set `model` on EVERY agent (D188). Sonnet builds, walks, verifies and captures. Opus only for taste judges, motion and tricky logic. One writer per worktree. Never SendMessage a workflow agent.
- Usage: check every 10 minutes. The owner allows up to 98% (D190). At 95%: STOP POINT commits, NOW.md, next prompt, Continuum checkpoint.
- No regressions (D186): walk the FINAL build on the emulator before calling it done (Night and Day, text 1.0 and 1.3, every changed screen plus the main flows). Record findings in Continuum as they happen (D187).
- Copy rules: plain, warm; no exclamation marks, emoji, arrows or hype; never "lost", "behind", "last"; numbers with units; 12-hour times; 44 dp targets; reduced motion; Night and Day both first-class. The Pro key is always "Get Pro"; no text bombardment (D185).
- End every update to the owner with "Things needed from you right now:" or "Nothing needed from your side".
