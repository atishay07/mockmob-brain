# Production pass, 15 Nov 2026: plan and running record

Owner's brief (15 Nov, about 11:45 am IST): the final pass on the website before marketing. Not a refinement pass:
features to add or refine, flows, sign-in options, anything broken, bugs, security, "anything else required" for a
10/10 product. Questions and Key cards content is a separate track and is out of scope. Work as an orchestrator with
Opus (edge cases, taste), Sonnet (exact specs) and Haiku (bulk small fixes) agents. Quality first, then speed.

Code: branch `web/1115-prod` in `wt-1110-convert` (integration), cut from main `38a09a4e7` (live). Working notes for
every lane: `wt-1110-convert/tmp/1115-prod/` (not shipped). Status words below: RUNNING, DONE, NEXT, HIS (owner's call).

## 1. What the audit found (eleven read-only lanes, 15 Nov, 11:50 am to 12:40 pm)

| Lane | Result |
|---|---|
| Database | Sound. Row-level security on all 120 tables, nothing readable with the public key except the chapter list, no open functions or buckets. 166 MB of 500 MB. |
| Sign-in and admin | No bypass, no way to read another student's data. Real gaps: rate limits are per server in production (the flag is unset), so sign-in emails can be flooded; no security headers; Next 16.2.4 has published advisories. |
| Payments | Signatures, prices and credit moves are sound. Real gaps: replaying an old payment check gives Pro for ever; account deletion does not cancel a website subscription; two open checkouts can become two subscriptions; refunds change nothing. Rs 99 monthly has never been captured in production. |
| Mob and public routes | The question feed gave the whole bank with answers to anyone without an account (known since 16 Oct, fix was held for the app). A removed Mob member can rejoin with the old link. Mob reports alert nobody. |
| Tests and AI | Scores, timers and paid-model caps are sound. Gaps: Ask Mobi has no reply for a student in distress; three accounts can switch off any Key card; Rival serves withdrawn questions. |
| Core loop bugs | A reload just after time-up submits the paper empty. The phone's Back button drops a running paper and the next start is charged again. Three "Practise this chapter" links open "This paper link has expired". No error page exists anywhere. |
| Mechanical sweep | Lint clean, links clean, 24 of 26 suites green (the 8 red tests are stale tests, not product bugs). A hidden agent brief ships in every page. Upload links lead to a paused page. |
| First run | Inside Instagram's browser the first key leads to Google's block page. The first run ends on Practice with the Start key 1.4 screens down and a six-stop guide over it. The sample's subject is dropped at sign-up. Nothing reaches a student on day 2. |
| Rivals | PW and Testbook sign in by phone code only. Rivals have previous-year papers, an all-India rank and a scheduled mock; none has a shared daily set, a result share card, parent pay or cutoff pages. PW (Rs 599 a stream) and Testbook (Rs 479 a year) cost less than Pro to May (Rs 693): lead on unlimited mocks and fixing, not on price. |
| Owner's open asks | Most October rows are done in code or replaced by later instructions; the ledger was never updated. Truly open: the answer-sheet bubble texture still on three home sections (he rejected it, LK208); "until you cancel" against a 24-payment plan; Compass cutoffs never checked against the DU PDFs; tablets never walked; badges kept but never refined. |
| Launch readiness | Vercel is on Hobby and Supabase on Free (confirmed 15 Nov). A friend's invite link on Android sends the friend to a Play listing that is not public (404). The hero film is 3.6 to 6.4 MB of every phone visit. Home LCP 4.9 s on a slow phone profile (CLS 0). Nothing would tell anyone the site is down: logs last one hour, no error capture, no analytics. The home share image is 330 KB (WhatsApp may drop it). The privacy page leaves out what the code does with cookies, the referral device id and guest Ask Mobi. |
| Fresh-account screens | Still running when this was written. |

## 2. The waves

### Wave 0, security (RUNNING; ships alone, first, under the owner's standing order of 12 Oct to fix and deploy security holes at once)

| Lane | What |
|---|---|
| SF-A | Feed needs sign-in, no key for a held question (feed and Saved), no anonymous cache; the unused question-write route is closed. |
| SF-B | Removed members cannot rejoin; reports email support; 40-bit invite codes with limits that hold across servers; name filter for Hindi and look-alike letters; the 7 stale Mob tests settled (one of them guards hidden picks). |
| SF-C | A fixed, kind reply with Tele-MANAS 14416 and 112 for a student in distress, before any model call; Key card reports cannot be farmed; Rival off behind a switch; session restarts keep their clock. |
| SF-D | No Pro without an end date; deletion cancels the website subscription; one checkout, one subscription; refunds recorded and access ended; referral and creator-code checks tightened. |
| SF-E | Sign-in email limits that hold across servers, with honest messages; security headers; a same-origin check on writes; password set needs a fresh sign-in; the dead coming-soon route removed. |

### Wave 1, the product's weak points (RUNNING)

| Lane | What |
|---|---|
| W1-A runner | Answers survive a reload at time-up; Back opens the Leave sheet; a left paper can be resumed; no raw codes; chapter links open Practice with the price shown. |
| W1-B failure pages | Error pages for public pages, the signed-in shell, the runner and the whole app; the hidden agent brief removed; the offline page. |
| W1-C result | A real report sheet; "tomorrow" on the result; the install card after the first result; priced starts everywhere. |
| W1-D first run | The last onboarding key starts the first free set; Practice shows the first set on its first screen; the guide ends on Start; the sample's subject travels into onboarding and Practice. |
| W1-E cleanup | 12.5 MB of old video, tracked logs, a `.vercelignore`, the Study test's line endings, a server guard on /moderation. |

### Wave 2, after those merge (NEXT)

- Sign-in card: an "Open in Chrome" key inside Instagram's browser with the email code first; Google One Tap on Chrome; "last time you used Google"; a typo catch for email addresses; the code first in the sign-in email.
- A share card for a result (opt-in, carries the referral link).
- Launch readiness: invite links stay on web sign-up until the Play listing is public; a lighter first paint on a budget phone (a phone-size poster, the font preload, long-lived caching for the film); a share image under 300 KB and real previews for Mob and invite links; the service worker registered from the app shell; the privacy page brought in line with the code (his wording to confirm).
- Fresh-account screens (from the walk) and the small open asks (the bubble texture, course/programme wording, the AI-cap migration).
- DONE 15 Nov (main session, f623876ff): the hero film no longer starts by itself on a link the browser calls 2G or 3G.
- The server half of a late upload for a paper finished offline; Today and Review counting open mistakes the same way.
- Next.js security upgrade on its own branch with the full gate (CTO's call to ship).
- The one known fault that blocks server-saved papers (durable sessions), so that switch is ready.

### Wave 3, new things, each behind a switch that starts off (NEXT, some HIS)

- "Ask a parent to pay": Razorpay already returns a shareable link for each subscription; the page drops it.
- A cutoff page per DU course from the Compass data (after the cutoffs are checked against the DU PDFs).
- HIS: a daily five for everyone; a Sunday mock with "your place among N who sat it"; WhatsApp code sign-in; a day-2 email.

### Gate before any deploy

All suites, eslint, `next build --webpack`, an independent Opus review of the whole diff, screens looked at on a
phone size and a laptop size in Day and Night, a Vercel preview, then production and live checks. Security ships first
and alone.

## 3. For the owner

### Decisions (my default in brackets; I go ahead on the default unless he says otherwise)

1. A public daily five from English and the General Test publishes five new questions with answers a day, beyond the 30-a-subject sample limit. [build it behind a switch, off]
2. "Your place among N who sat this paper" on a weekly mock goes against the no-percentile line in PRODUCT.md. [not built until he says]
3. WhatsApp code sign-in needs a Twilio account and Meta business verification, and stores minors' phone numbers. [not built until he says; One Tap and the Instagram escape are built now]
4. A day-2 email to 16 and 17 year olds needs his consent wording and an opt-out. [not sent until he says]
5. Pricing says Pro renews "until you cancel"; the plan is 24 payments. [his wording]
6. Server-saved papers (durable sessions) on before marketing. [CTO; I fix the blocker and show a local run]
7. The held "reveal the answer only after answering" change to Explore breaks Explore in installed app builds. [stay held; sign-in is now required]

### Only he can do

- Hosting, confirmed 15 Nov: Vercel is on Hobby (it forbids commercial use, the site takes payments, and runtime logs last one hour); Supabase is on Free (no backups, and a second egress overage restricts the project at once). Both to Pro before marketing (about USD 45 a month together).
- Switches for seeing what happens: `FUNNEL_ENABLED`, Vercel Web Analytics and Speed Insights, an uptime ping.
- The hero film on phones: most Androids download the 720p file (6.4 MB). Phones could always take 480p (3.6 MB). His eye decides; not changed.
- The privacy page needs the legal entity, an address and a grievance contact, and counsel on consent for under-18s (DPDP).
- Check the Resend plan: on the free plan (100 emails a day) email sign-in stops after the hundredth code.
- Add a DMARC record for mockmob.in.
- Vercel: mark the four production secrets it flags (database service key, session secret, Anthropic key, internal secret) as Sensitive.
- Google Cloud and Supabase steps for One Tap (listed in `sec-auth.md`).
- Process or cancel the account-deletion request of 20 Oct before 19 Nov.
- Look at the Rs 69 payment of 26 Apr in Razorpay: captured there, stored as failed here.
- One real Rs 99 purchase and cancel, and the 15-minute signed-in walk on his phone (`bugs-core.md`, last section).

## 4. Record

(appended as waves merge and ship)

### 15 Nov, from about 7:40 pm IST (Opus orchestrator, second half)

- Live check: production `6472026f0` (parent pay) is READY (`dpl_FrLEwppYrcbQLF99CvqrRt1eNbST`); `/`, `/pricing`, `/daily`,
  `/signup`, `/api/daily?day=1` answer 200.
- Gate on `6472026f0`: all 24 suites green (app 1,237, auth 191, billing 514, Mob 368, learning 377, recovery 646, keycards
  127, today 146, learn 440, NTA 234, study 62 after restoring the WordNet licence file's LF), eslint clean, `next build
  --webpack` 116/116.
- The five red tests outside the scripts, traced (commit `37f917b1b`): `web_r4_nav_1105` A5 followed the F2 start key (15 Nov),
  `home_sections_r4_1105` followed the round 13 and 14 sheets (13 Nov), `funnel_calls` followed the L4 start routing (15 Nov),
  `round5_completion` followed the 5 to 999 minute goals (20 Oct): each now checks the new code. `landing_checklist_1104`
  L-040 was real: Ask Mobi's visual-viewport scroll listener (13 Nov) is now passive.
- Cleaned: 16 merged lane worktrees removed (junctions unlinked first; the shared `node_modules` checked intact), their
  captures kept in `wt-1110-convert/tmp/1115-prod/lane-shots/`; `.next` and `.next-dev` deleted.
- Not done: removing `chart.js` and `react-chartjs-2` (npm's lock-only uninstall also rewrites unrelated optional entries;
  do it with the Next 16.3 upgrade, which needs a real install anyway).
- Wave 1 started (four lanes, own worktrees and ports): Daily Five as a habit (`wt-1115-daily`, 3581), the DU data check then
  cutoff pages (`wt-1115-w2-b`, 3582), the Sunday Mock (`wt-1115-sunday`, 3583), small fixes B11, "course" wording, Open in
  Chrome on `/signup`, Back with the NTA warning open, unused CloseSheet (`wt-1115-small`, 3584, Sonnet).
- Decided by me (his "decide small things"): the Sunday Mock is free for every signed-in student, one sitting per subject a
  week; its answer key opens when the window closes at 10:00 pm; it shows how many sat it and, from 30 sitters, the share
  right per question, with no rank. The Daily Five goes in the public site's top bar, not the signed-in dock (its item count
  is his). The Daily Five's "how everyone did" line appears from 30 saved answers per question.
- LIVE `a3bad4078` (about 8:35 pm): small fixes. Practice "Average score" averages signed marks (B11); students read
  "course" in 19 files (degree names such as "B.A. (Programme)" kept); "Open in Chrome" at the top of `/signup` in Android
  in-app browsers; a warning dialog closed by Android Back comes back while the paper runs, not after it ended (independent
  Opus review: no blocker, one should-fix applied); unused CloseSheet deleted. Checked live: the new wording served, nine
  public routes answer as expected, no runtime errors. Not checked: a real Instagram browser, a physical phone.
- LIVE `12516f20f` (about 9:10 pm): the DU data check passes all three rounds (17,316 printed scores match the served data;
  `data/du-csas-2026/verification/REPORT.md`), and the cutoff pages: `/du-cutoffs`, 68 course pages, 67 college pages, in the
  sitemap (136 entries). Checked live: index, a course, a college 200, an unknown course 404, titles served.
  Open: the calculator opened from a course page waits for subjects before showing that course (next small batch); the
  Bulletin's free-text course notes are mis-parsed in places (B.Com carries the BBA text), so the pages leave them out:
  content track.
- LIVE `79ff0d94e` (about 10:50 pm): the Daily Five as a habit, the Sunday Mock, the emails built and off. Two independent
  Opus reviews: the Sunday draw was predictable and repeating (BLOCKER, fixed: seeded draw, skips 8 Sundays); a Sunday
  sitting used up the free first Full mock (fixed); stats for any week (fixed); the den named non-sitters against rule F2
  (fixed in both strips); answers opened while late starters sat (now 11:05 pm); a scripted 5/5 Daily Five (fixed: server
  checks, first check stands); a sign-in blip made a student a guest (fixed: 503). Merged visual check: everything holds
  except the home page cascade from the first-paint join, so first paint was reverted out of this release. Gate on the
  release: all 24 suites, lint, build 256 pages; Vercel preview READY.
- HELD: first paint (`web/1115-paint`) and late upload plus the durable start (`web/1115-sess`); steps in
  `HANDOFF-2026-11-15-NIGHT.md`.
- Checked live after `79ff0d94e` (about 10:55 pm): `/`, `/daily`, `/sunday-mock`, `/du-cutoffs`, `/pricing`, `/signup`, `/login`,
  `/cuet/accountancy` 200; `/api/today` 401; `/api/daily?day=1` 200 with no answer key in the body, a wrong day 400; an
  unsigned unsubscribe POST 400; `/sunday-mock` in the sitemap; 28 stylesheets on `/` (27 before: the Daily Five bar sheet);
  no runtime errors in 20 minutes. Not checked: any signed-in flow on production, a real Sunday sitting (first on 22 Nov), a
  physical phone.

### 16 Nov, about 12:05 am to 2:05 am IST (Fable orchestrator)

| Release | What | Checked |
|---|---|---|
| `acc95ac67` | First paint: the home sheets as one file, order-proof | live `/` at 390 and 1440 Day identical to the baseline (every section height, `.ft-story` 2,924, `.lc` 3,570, the DU teaser fill), 21 sheets from 28, 9 public pages 200, no runtime errors |
| `85ed294e8` | The Daily Five redesigned: `/daily` around a board, a clock and a run; the home block as a calendar page (second version, after his "not up to the mark") | gate on 001d211e6 (24 suites, lint, build), then app and dock suites, lint and build on the block's rework; headless Chrome walk with real clicks at 360, 390, 1440, Day and Night; live block 533 px at 390, the try section 996 to 1,538, every other section unchanged |
| `844e608fe` | Lanes merged: route bar, reading line, shorter opening, loading states (`web/1116-load`); public Key card decks (`web/1116-decks`); bring a mistake (`web/1116-mistake`, independent Opus review, three fixes) | gate on the merged branch (24 suites, 0 failures, lint, build); merged captures at 390 Day and Night and 1440; live pages 200, mistake route 401 signed out, no runtime errors |
| `15286120f` | The week as two calendar pages (Daily Five, Sunday Mock with a clock to next Sunday); `/daily` wears the same day band | app, dock, today suites, lint, build; walk at 360, 390, 1440 |
| `91f8f8aaf` | Badges refined (`web/1116-badges`) | full gate (24 suites, lint, build); merged Progress, You and result captures at 390; live pages 200, no runtime errors |
| `e137d3575` | Desktop two columns for the result, Progress and the Wallet; tablet walk fixes (`web/1116-desk`) | full gate (24 suites, lint, build); merged captures at 1440 and 390; live pages 200, no runtime errors |
| `aecaf31c5` | Home Key cards: pick your subject (14 links into `/key-cards`) | app, keycards, keycards-ui, dock suites, lint, build; live links and anchors, no runtime errors |
| `329e257ba` | The durable release race (`web/1116-race`): SQL function and undo unapplied, fallback in code, independent review | full gate (24 suites, billing 554, lint, build); live pages 200, `/api/sessions` 401 signed out, no runtime errors |
| `05510626d` | Bring a mistake on the home page; spinners and shimmers made one pattern (`web/1116-spin`) | app, billing, keycards-ui, du, dock suites, lint, build; pointer walk of the block at four sizes; live sections compared; no runtime errors |
| `f5f6774c5` | Sunday Mock page day band; Daily Five carry-over; corrections log unlisted | full gate with one Mob test failed (passed 369/369 on a rerun, a timeout under load: pushed before the line was read); live pages 200, `/corrections` noindex and unlinked |
| `d40a6160b` | First minute after sign-up (`web/1116-first`, independent review) | full gate, 24 of 24 |
| `b42dd5bb4` | The race cases (`web/1116-race2`, independent review) | billing 564, recovery, learning, app suites, lint, build |
| `a6ab71edc` | Mob class leagues, switch off (`web/1116-league`, independent review, seven fixes) | full gate (billing passed on a rerun; one source-pin test fixed for CRLF, Mob 408); live `/api/class` 404 |

Rollback points, newest first: `dpl_8sQbt8w44NeXzAiAZua45V2bXwcE` (`b42dd5bb4`), `dpl_8327xRwwkwniXccga2DqT183B49P` (`d40a6160b`), the `05510626d` build, `dpl_236uTaRypn1V8DjtJYG2E7C4V9ak` (`329e257ba`), the `aecaf31c5` build, `dpl_spJ7iRVRQnF6zMgpVd8MmVSXPfsK` (`e137d3575`), `dpl_7ckikYsAgs2nrBvbeoTBaKVj5rRQ` (`91f8f8aaf`), the `15286120f` build, the `844e608fe` build, `dpl_8qDxPcYVur2NgGHNFoC5DgQJEHZZ` (`85ed294e8`), `dpl_62mUqYSE1WWeHGv3pwSA7VgkBAss` (`acc95ac67`), `dpl_Het1EhstDtjofTqpxr1A4FB57YsW` (`6858ccef5`).
Lessons: a broken `package.json` (a regex edit) killed the dev server and blanked a visual check: edit JSON as JSON. A file used by the app shell must not carry `mm-btn` classes (`css_split.test.mjs`). The sticky room in the desk grid slides over anything placed in a second grid row: keep new blocks outside `.lp-desk`.
