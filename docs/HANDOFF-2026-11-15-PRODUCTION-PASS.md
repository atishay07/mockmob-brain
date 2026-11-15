# Handoff: production pass before marketing, 15 Nov 2026 (stopped about 7:35 pm IST at 95% usage)

Read with: `PRODUCTION-PASS-2026-11-15.md` (plan, audit findings, owner list), `NOW.md`, `UI-AUDIT-LOG.md` (section 3a is new),
`RUNBOOK-REFUNDS-2026-11-15.md`. Lane notes with file and line for every finding: `wt-1110-convert/tmp/1115-prod/*.md`.

## The owner's words that bind the next session

- 15 Nov, 11:45 am: the final pass before marketing; "not a refinement pass"; add features, refine features, flows, sign-in options,
  bugs, security; "innovative ideas"; orchestrate Opus (edge cases, taste) and Sonnet (exact specs) agents; quality first, then speed.
- 15 Nov, about 7:15 pm, after seeing mostly audit and fixes: "focus more on building and building more things ... rather than just
  doing an audit and thinking long on smaller things and refinements ... tangible, actual results, not small refinements." "You can
  think for yourself what's useful, what's not, and apply everything. Push it to live. Then we'll come back to the pending decisions.
  Keep adding any stuff left to the list which you have not done and are waiting for my decision."
- He reads an item missing from an update as dropped: every update lists every plan item with its status.

## State of the code

- Production: `www.mockmob.in` serves main. Last push `6472026f0` (parent pay) at about 7:31 pm: its Vercel build was NOT confirmed.
  Confirmed live before it: `2039eb7d6` (Daily Five: `/daily` 200, in the sitemap). Rollback points, newest first: the Daily Five
  build, the share-card build `12921356b`, the product half `d479b78ef`, the security release `dpl_8hgVk5zUo8EqbVhSuP7xvnWQeX3k`
  (`e6b041acf`), and before today `dpl_HVKC1RyErDXQVvTH5xS8BnewnNjb` (`38a09a4e7`).
- Integration worktree: `C:/Users/atish/Desktop/mockmob copy/wt-1110-convert`, branch `web/1115-prod` = `origin/main` = `6472026f0`.
  Work there or cut new worktrees from it. Dev server: launch config `convert-1110`, port 3571 (it was left running: stop it, delete
  `.next` and `.next-dev`).
- `node_modules` in every `wt-1115-*` worktree is a junction to `wt-1103-web-cards/node_modules`, which still holds Next 16.2.4 while
  package.json says 16.2.12 (Vercel installs 16.2.12). Local tests and `next build --webpack` work. `wt-1115-next` has its own real
  install of 16.2.12 (567 MB).
- Today's lane worktrees, all merged, safe to remove (rmdir the `node_modules` junction FIRST, then `git worktree remove`):
  `wt-1115-sec-a..e`, `wt-1115-w1-a..e`, `wt-1115-w2-a`, `wt-1115-w2-c`, `wt-1115-w3-a`, `wt-1115-f-a..c`. Keep `wt-1115-w2-b`
  (the paused DU data check, 3 uncommitted files) and `wt-1115-next`. Captures the lanes made are under each worktree's
  `tmp/1115-shots/`: copy what is worth keeping before removing. Disk had about 24 GB free.
- Gate used today (`wt-1110-convert/tmp/gate.sh`): 24 test scripts, `npx eslint src --max-warnings=0`, `next build --webpack`.
  Last full run on `36511c192`: all green except `test:study` (a CRLF checkout artefact in this worktree: `git checkout --
  data/study/sources/WORDNET-LICENSE.txt` after the `.gitattributes` rule fixes it). After it: test:app 1,237, test:billing 514,
  test:auth 191, test:today 146, 0 failures. No full gate and no local build ran after the sign-in, share-card, Daily Five and
  parent-pay merges: run the gate first thing.
- Known red, not traced: `data/tests/web_r4_nav_1105` A5 (Practice page), `home_sections_r4_1105` H1, `landing_checklist_1104` L-040,
  `funnel_calls.test.mjs:198`, `round5_completion` "Tonight metadata". None is in a `test:*` script. Find which lane caused each.

## What shipped today (all on main)

Security (independent Opus review, no blocker; six findings fixed or checked): feed and Saved behind sign-in with held questions'
keys withheld and a 120-pages-a-day cap; payments (no Pro without an end date, one checkout one subscription, deletion cancels the
Razorpay subscription, refunds end access, referral and creator-code checks); the Mob (removed members stay out, reports email
support, 8-character codes, name filter, the 7 stale tests fixed); Ask Mobi's fixed support reply (Tele-MANAS 14416, 112); sign-in
email limits across servers; security headers; same-origin check on API writes; Rival behind `RIVAL_ENABLED`; Next 16.2.12.

Product: the runner keeps answers (reload at time-up, Back, second tab, offline) and a left paper resumes from Today and Practice;
error pages at four levels; the first run ends on a question; result page report sheet, tomorrow line, install card; fresh-account
states; sign-in card for in-app browsers, the code in the email subject, typo catch, remembered method, One Tap behind
`NEXT_PUBLIC_GOOGLE_CLIENT_ID`; share images under 300 KB; the bubble texture gone; privacy page facts; phone poster.

New features: the result share card (canvas, 1080 x 1350, two switches); the Daily Five (`/daily`, `GET /api/daily?day=n`, 60
public questions, 12-day cycle, device streak, rows on the home page and Today); ask a parent to pay (`POST
/api/billing/parent-link`, Razorpay `short_url` with `expire_by`, `PARENT_PAY_ENABLED` default on).

Never exercised by anyone: any signed-in flow on production; a real payment, cancel, refund or parent link; whether live Razorpay
accepts `expire_by`; the support reply through a real model turn; a real Instagram browser; a physical phone; One Tap.

## Not done (the build list for the next session, most valuable first)

1. Confirm the `6472026f0` build is READY and live; run the gate; trace the five red tests above.
2. Make the Daily Five a habit, not a toy: save a signed-in student's result to the account (it is device-only today), count it in
   the study-day chain, show the Mob each other's rows, add it to the top navigation, and a "how everyone did" line per question
   once 30 have answered (needs a small table: write the migration and undo, not applied). Its pool is 60 questions: see decisions.
3. A cutoff page per DU course and college (about 135 static pages from `public/du/2026/`, each linking to Compass and sign-up,
   with the source and date). Blocked on the DU data check: resume it in `wt-1115-w2-b` (brief in this session's transcript; the
   prompt is in `tmp/1115-prod/` lane list of the plan doc). Verdict first, pages second.
4. Sunday Mock (rivals' biggest draw): one fixed full paper per subject each week, open Sunday 10 am to 10 pm, a Mob can sit it
   together. Build everything except the ranking line, which is his decision.
5. Day-2 return: the welcome email on account creation (one action) and a day-2 email are both unbuilt; build them behind
   `EMAILS_ENABLED` off with an unsubscribe route, since consent wording for under-18s is his.
6. Late upload: the server half of a paper finished offline (`bugs-core.md` B8; the client already sends answer times; keep late
   papers out of ranks).
7. Durable sessions: fix the one known fault that blocks `LEARNING_SESSIONS_ENABLED` (STATUS.md line 772: a start quoted free that
   loses a race is charged 50), show a local run on the e2e harness (`src/app/preview/arena/nta`), and hand the switch to the CTO.
8. First paint: merge the 25 home stylesheets (about 1.1 s of FCP by the trace), drop the Literata preload on `/`, stop preloading
   the three creator photos, 48 px college logos.
9. Smaller: Android Back with the NTA warning dialog open may close it and leave answers locked (`ExamIntegrityGuard`); B11 average
   score on Practice (`DashboardPageClient.jsx:328`); `programme` still in `src/lib/du/compassLine.mjs`, `src/lib/colleges/model.mjs`,
   `admission-compass/page.js:7`; an "Open in Chrome" link at the top of `/signup` in Android in-app browsers; `expire_by` on Get
   Pro's own subscriptions; `referralAttributionFromCheckout` reads payer-set notes; `/create-monthly-subscription` and
   `/verify-payment` sit outside the same-origin rule; delete unused `CloseSheet`; remove `chart.js` and `react-chartjs-2`.
10. Ideas not started that fit his "build more" brief (pick by taste, mock-up nothing, build): Mob class leagues (a class code, a
    weekly paper, class average, no names); "bring a mistake from any test" (Mobi explains a pasted question and sets two fresh
    checks); public Key card decks per chapter; a corrections log; badges refined (his D19: keep, refine presentation and what
    earning one does); desktop two-column layouts for Wallet, Progress and the result; a tablet-width walk (never done).
11. Next 16.3.8 (closes the next/og and Windows advisories; a minor upgrade, CTO's call, own release with the full gate).

## Waiting on the owner (keep this list current; do not stop for it)

Decisions: widen the Daily Five's pool beyond the 60 public questions; "your place among N who sat it" (against the no-percentile
line, PRODUCT.md:95); WhatsApp code sign-in (Twilio account, Meta verification, minors' phone numbers); the day-2 email's consent
wording; pricing says "until you cancel" but the plan is 24 payments; phones always take the 480p film (3.6 MB against 6.4 MB);
Today and Review count open mistakes differently (12 against 22, by design: newest paper against all papers); when the first Pro
sheet may open (1.8 s today, never over a blank paper now); "Guide" or "Show me around"; grouping 8-character Mob codes.

Only he can do: Vercel Hobby to Pro and Supabase Free to Pro; check the Resend plan and set `AUTH_EMAIL_DAILY_CEILING` (default
2,000; about 80 on a free plan); tick `refund.processed` and `payment.dispute.*` in the Razorpay webhook; apply
`20261115120000_razorpay_refund_credit_takeback.sql` and the AI-cap migration if he wants them; a DMARC record; the 20 Oct
deletion request before 19 Nov (the script now needs `RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET`); the Rs 69 payment of 26 Apr
captured at Razorpay but stored failed; One Tap's four console steps; mark the four Vercel secrets Sensitive; the privacy page's
legal entity, address and grievance contact; one real Rs 99 purchase and cancel, and one parent-link payment from a second phone
(steps in the f-parent and fix-money lane reports, quoted in this session's transcript); the 15-minute signed-in walk
(`bugs-core.md`, last section). Content track: five Mathematics rows with malformed text (ids in the w1-result report), one
possibly with a wrong key (`ddbac3ae-10d8-4219-a4d2-6841ebc45f66`).

## Lessons from today for whoever orchestrates next

- 23 Opus agents emptied the 5-hour window in about 90 minutes; a second window went from 6% to 95% in about three hours with up
  to nine at once. Run three or four at a time and start feature lanes first.
- Give every agent a worktree, a file list and a port; merges then conflict only in `package.json` (resolve by taking one side and
  re-adding the other's test files) and in shared preview fixtures.
- Agents resume by name with SendMessage after a limit stop; their uncommitted work stays in the worktree.
- Tests that read source text break across lanes: after each merge run `test:app` and fix the assertion to the merged code.
- Heredoc-fed Python mangles backslashes (a regex backreference became a control character): write the script to a file with the
  Write tool, or use Edit.
- A visual check of the MERGED branch found a blocker no lane saw (button minimum size from the shell). Always run one.
