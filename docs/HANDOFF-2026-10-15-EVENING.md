# MockMob handoff, 15 Oct 2026, evening (about 21:30 IST)

From session 604ced81 (Opus 5.5, account support@mockmob.in). Usage was at about 80% when this was written. If the session stops, the next agent continues from here.

Read first, in this order:
1. The owner's standing goal, verbatim with its checklist: `docs/brain/OWNER-VISION-2026-10-15-PM.md`.
2. The memory files `cto-mode-standing-goal.md`, `platform-focus-mobile-first.md`, `web-restructure-rejected.md`, `features-over-retesting.md`, `mockmob-design-direction.md` and `quality-bar-and-stop-rule.md`.
3. HANDOFF-2026-10-15-AFTERNOON.md and HANDOFF-2026-10-15-FULL.md, for older context.

## 1. The owner's direction today (newest first, his words in the files above)

- **Act as the CTO.** Keep building and refining without waiting for him. Decide taste from his recorded preferences, and ask only about money, accounts, legal matters or irreversible steps. "Keep up the pace... right now it's a bit too slow."
- **The website (v2) is "a step in the right direction, maybe 30%".** The landing page is mobile-first. The arena is desktop-first but must work on phones. The app is mobile only.
- **His app review of APK v8** (long, 15 Oct about 21:00):
  - Google login did not return to the app. Fixed: Supabase Redirect URL `in.mockmob.app://login-callback`.
  - The "Couldn't load" banner's Try again does nothing, and the back button exits the app.
  - The NTA tile overflows in Practice and in the Start sheet.
  - Start animations wanted: a clock that turns 360 for a full mock, and an NTA-specific moment.
  - Review shows odd copy ("we could include your mistakes").
  - The You tab is too thin. He wants profile from a top-bar avatar, light/dark easy to find, and proper account settings.
  - Road to May: wants a board that is interactive and editable, placed higher with a scroll cue, and a stronger blur.
  - Your Colleges shows "Could not load a suggestion", Start does nothing, and a stray "last week" section appears.
  - The Admission Compass, Combo planner and CUET tools need hierarchy and to be built into the flow. "Confusing doesn't mean cut it."
  - Ask Mobi must be integrated with credits.
  - "Many things are out": find more of these ourselves.
- **His landing review:**
  - The held scroll stories skip several slides on a fast scroll. He wants one gesture to move exactly one slide, at any speed. "What's inside MockMob" was much too fast.
  - The footer's "Try CBT question" button doesn't work, and Sign up and Free to start are missing.
  - The illustrations should explain: time bars around the pace line, and changes shown as a red crossed D, an arrow, then a green checked B.

## 2. Live now

| What | Where |
| --- | --- |
| Website v2 plus Mistake Lab slices 1 and 2 | Production main 48309076 on www.mockmob.in, Vercel READY, 0 runtime errors |
| Repair v3 and the SWOT | Live since this morning |
| APK v8 (feat/app-and-web b0a61496) | Installed on the owner's Vivo phone over adb (serial 10BF370PA6002XR, connected by USB) |

Website v2 includes logo B, the brand switch, held scroll stories, designed controls, the Start sheet, the account page, 2-step onboarding and the copy pass. Mistake Lab slice 1 is the ledger, re-mark and cohort; slice 2 is capture, the one time rule and Replay.

**Fixed with the owner today:**
- The Vercel Attack Challenge Mode, which blocked every app API call, was turned off by the owner. The app's email sign-in works.
- The Supabase Redirect URLs entry was added by the owner. Google returns to the app.
- Supabase Confirm email is ON.

**Production database:** migration `auth_unconfirmed_passwords` (the account-takeover guard) was applied this morning and logged in STATUS.md.

## 3. Running when this was written (check each journal; resume only in this session)

| Run | Worktree and branch | What it does | When it finishes |
| --- | --- | --- | --- |
| wf_d376733c-656 | wt-web-v2, web/v2-1015 | Landing fixes: G1 one gesture per step (ScrollStory), G2 footer buttons and a link crawl, G3 explanatory illustrations, then a gesture verifier | Merge web/v2-1015 into main (it is based on f652aba0; main has slice 2 on top) and deploy, if deployReady |
| wf_b5d5d70e-d19 | wt-web-v2 | Speed pass: Lighthouse on mobile, lazy-loading, images, fonts. CI is already done (503c0e4f, `.github/workflows/web-tests.yml`) | Same merge as above |
| wf_08ca7750-ebb | wt-deploy web/lab-s3 and wt-phase2 ui/phase2 | Mistake Lab slice 3: Across your mocks, the Rule book, "Use in my next mock", the rule check, the start-sheet line, repair order by cohort. Core is done (b297706a to b0ef84c6); the web and app builders, a truth review and checks follow | Merge web/lab-s3 into main, deploy, then the app |
| wf_63529225-f11 | wt-usage web/usage-fixes, and wt-phase2 | Usage fixes 1-4: counts once a day, evidence files cached, Singapore region, a guard against whole-bank reads. App wave 3: auth return and the error banner with back, Practice/Start NTA and start animations, Today's road and colleges, tools. A read-only UX audit writes `docs/brain/APP-UX-AUDIT-2026-10-15.md` | **Deploy the usage fixes as soon as they pass.** They are what keeps Supabase and Vercel on their free plans |
| wf_b75ed0a8-8fc | wt-phase2 | App wave 4a: a top-bar avatar with an Account sheet (profile, light/dark, plan and credits, settings, help, sign out) and Ask Mobi with credits | Merge with the other app work |

Workflow scripts are copied to `mockmob-next/tmp/workflows/` (landing-fixes-1015.js, speed-and-ci-1015.js, lab-slice3-1015.js, usage-fixes-app-wave3-1015.js, app-wave4a-1015.js and the earlier ones). Journals are in `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\604ced81-3aa7-4deb-b42c-f324ca5f51e2\subagents\workflows\<run id>\journal.jsonl`.

**If the session stopped mid-run:**
1. In each worktree, commit the WIP: wt-web-v2, wt-deploy, wt-usage and wt-phase2. Never commit next.config.mjs, which only differs by line endings.
2. Read each journal for finished results.
3. Re-run only the unfinished packets.

## 4. What to do next, in order

1. **Usage fixes (wt-usage, web/usage-fixes):** when the checks pass, merge into main and deploy, then confirm Vercel is READY with no runtime errors. Then build **fix 5**: a practice start downloads only the questions it picks, and the slim NTA index table is added to production. It needs the full suites. It is required before more testers join (HOSTING-VERDICT). Also set up a weekly database backup (Free has no automatic backups) and move agent testing to staging.
2. **Landing fixes and the speed pass:** merge web/v2-1015 into main (through wt-deploy or a fresh worktree) and deploy. Keep both sides of any conflict; the STATUS.md conflict pattern is "keep both".
3. **Lab slice 3:** read the truth review. When it is clean, merge web/lab-s3 into main and deploy, server first, before the app sends anything new.
4. **App:**
   - Merge wave 3, wave 4a and the slice 3 app work on ui/phase2 into feat/app-and-web.
   - Build APK v9. The command is in HANDOFF-2026-10-15-FULL.md, section 5; zip the result.
   - Install it on the owner's phone with `adb -s 10BF370PA6002XR install -r <apk>`, using the adb at `C:\Users\atish\AppData\Local\Android\Sdk\platform-tools\adb`, with MSYS_NO_PATHCONV=1. Launch it with monkey. Also send the zip.
5. **App wave 4b,** after slice 3 releases you/** and review/**:
   - The You tab as a real hub: the audit's recommendations, plus credits history, study days, notifications and tools.
   - The Review copy ("we could include your mistakes").
   - Then the UX audit's top findings.
6. **Website arena on phones,** pass 3: Today's dropdowns, Review details, and the critic's leftovers in `tmp/web-v2-pass2/critic-2`.
7. **Then:**
   - the analytics funnel (server-side, respecting the consent switch);
   - crash reporting in the app;
   - Mistake Lab slice 4: the trap atlas, the same mistakes later, and the key-quality loop.
8. Update the goal checklist in OWNER-VISION-2026-10-15-PM.md after each wave.

## 5. Decisions and facts from today

- **Supabase:** stay on Free (`docs/brain/HOSTING-VERDICT-2026-10-15.md`).
  - The grace period ends **9 Nov 2026** (owner). The billing month resets before that, so no Pro is needed if fixes 1-4 are live, fix 5 ships before more testers join, the owner checks Usage weekly, and backups are taken.
  - Move to Pro ($25) at public launch, about 1,000 daily students.
- **Vercel:** stay on Vercel; do not move to Cloudflare now.
  - Upgrade to Pro ($20 a month, which includes $20 of usage) when payments go live. Hobby forbids commercial use; the owner must say whether students can reach Razorpay checkout today.
  - Pro is not unlimited: about $25-35 a month at 1,000 daily students, about $150-250 at 10,000. Cut it with caching and fewer API calls.
  - Revisit Cloudflare if the bill stays above $150 a month for two months.
- **Regions:** functions in Singapore (sin1), next to the Supabase Singapore database (fix 3); the database stays in Singapore.
- **Usage causes** (`docs/brain/USAGE-LIMITS-DIAGNOSIS-2026-10-15.md`):
  - question-count refreshes pulled the whole bank (41 MB) every 15 minutes;
  - 59 timeouts of 300 s from per-question file re-reads;
  - functions ran in the USA while the database is in Singapore;
  - our own machines hit production;
  - five duplicate Vercel projects built on every push (now paused; the owner will delete them).
- **The 3D calculator on the landing** is the lamp-lit Accountancy object. It was intentional and is now shown on phones too.
- **The repair copy on the landing** was corrected to the truth: "written from the official key; no repair and no charge if the AI's working disagrees".
- **A Vercel build failed once** on a transient Google Fonts fetch. An empty-commit retry fixed it. If it repeats, make the font loading resilient.

## 6. Owner's open items

- Delete the 5 paused duplicate Vercel projects (mockmob-1uhb, -mmzs, -nxud, -pf37, -sjsj).
- Say whether students can reach the Razorpay checkout today. That decides the timing of Vercel Pro.
- Optionally confirm the Supabase reset date (Billing, under "Upcoming invoice"); it should be before 9 Nov.
- Play Store: the upload key, the Google client ID and the Play Console setup.
- One Mistake Repair on the site to verify the v3 cost (still no v3 row in runtime_ai_requests).

## 7. Gotchas

- **Dev server:** the owner's local preview runs on port 3110 from wt-web-v2 through `.claude/launch.json` "web-v2-local", which uses `.claude/web-v2-dev.cjs` so `process.cwd()` is the worktree. If every route returns 500 with "UNKNOWN: open ...layout.js", stop it, delete `.next-dev` and start it again.
- **Browsers:**
  - Never drive the owner's browser, and never sign in or create accounts.
  - The chrome-devtools MCP opens visible windows, so use headless playwright-core or Chrome only.
  - The built-in browser pane is fine for the main session.
- **Builds:** a production build needs the turbopack root set to the parent folder in next.config.mjs, then set back by hand. A build while the dev server runs can crash it (memory).
- **Python on Windows:** writing text mode turns \n into \r\n. Use binary mode or newline='' when editing workflow scripts, or the permission check rejects "control characters".
- **Usage hook:** it can show the other account's number right after a switch.
