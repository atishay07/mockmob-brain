You are continuing MockMob's production pass before marketing as the orchestrator, working autonomously. Call `continuum_start`
for project `mockmob`, then read in `C:/Users/atish/mockmob-brain/docs/`: `HANDOFF-2026-11-15-NIGHT.md` (all of it; the last two
sections are the newest), `NOW.md` (top entry), `UI-AUDIT-LOG.md` sections 1, 3a and 3b. `HANDOFF-2026-11-15-PRODUCTION-PASS.md`
holds the owner-only list and older context; open it only for that.

## The owner's words for this session

15 Nov, about 7:15 pm: "Focus more on building and building more things ... tangible, actual results, not small refinements."
"You can think for yourself what's useful, what's not, and apply everything. Push it to live. Then we'll come back to the
pending decisions."

16 Nov, about 12:10 am: "I tested that ask-a-pay-to-pay ... it was successful. The subscription was activated." Then:
"On the landing page, you have mentioned today is daily 5. It's not placed correctly as a proper clock. How do other websites
do it? You can see those, and even the entire UI and flow around it is very bad. We need to do something about that." "The
smaller UI things on the landing page, like having an overall progress bar on the top for the website, maybe we can do like
that, and having better loading everywhere. Right now, we have loading when entering the website every time, but it can be
improved a bit and smaller." "Don't spend too much time thinking on this and keep building."

## Do, in this order, without stopping to ask

1. **Ship first paint.** `wt-1110-convert` branch `web/1115-prod` at `acc95ac67` (pushed as a branch; main is `6858ccef5`).
   Its full gate already passed. Push `web/1115-prod:main`, wait for the new build, then measure live `/` at 390x844 Day in a
   browser against the baseline in the handoff (`.ft-story` 2,924 px, `.lc` 3,570 px, `--ss-beat` 58svh and 76svh,
   `.du-teaser__out` background rgb(234, 229, 218), page 21,372 px, 28 stylesheets: expect fewer). Any difference: roll back
   to `dpl_Het1EhstDtjofTqpxr1A4FB57YsW` and fix before trying again.
2. **The Daily Five, redesigned (his first point).** Look at how daily-challenge products present a daily puzzle on their
   landing and in play (Wordle-style daily games, daily quiz sites): the "today's" entry with a real countdown to the next one,
   the result and streak, sharing. Then redesign the Daily Five's place on the home page and the whole `/daily` flow (start,
   answering, the result, the run, the share, the next-day countdown), and the rows on Today and in the den, within MockMob's
   design (DESIGN.md, the existing tokens and components, one volt key per view). Keep what works: server-checked answers, the
   first check stands, "how everyone did" from 30, the den rule F2 (never name a member who has not played).
3. **Landing polish (his second point).** A thin overall progress bar at the top of the site for page loads and route changes;
   a lighter, smaller entry loader on every visit; consistent, smaller loading states everywhere (skeletons sized like the
   content, no layout shift, motion 150-350 ms, Reduce motion respected).
4. Then the rest of the build list in the handoff and his ideas, by value: Mob class leagues (class code, weekly paper, class
   average, no names); public Key card decks per chapter (the free taste of 5 a chapter); "bring a mistake from any test" (Ask
   Mobi explains a pasted question and sets two fresh checks, inside the existing AI budget guard); desktop two-column
   Wallet, Progress and the result; a tablet-width walk; badges refined (keep them, refine how they look and what earning one
   does); a public corrections log. Also: the durable-sessions release race in
   `wt-1115-sess/tmp/1115-prod/durable-sessions-ready.md` (fix in SQL as a migration plus undo, for the CTO), and Next 16.3.8
   with `chart.js`/`react-chartjs-2` removed (own release, full gate).

## How to run it (what worked)

- Three or four agents at once, each in its own worktree cut from `web/1115-prod` with a `node_modules` junction made in
  PowerShell (`New-Item -ItemType Junction -Path "<wt>\node_modules" -Target "C:\Users\atish\Desktop\mockmob copy\wt-1103-web-cards\node_modules"`),
  `.env.local` copied, its own branch and dev-server port (3590 and up, `next dev --webpack`). Remove a worktree only after
  unlinking its junction with `[System.IO.Directory]::Delete(path, $false)`, then `git worktree remove --force`.
- Every build agent reads `wt-1110-convert/tmp/1115-prod/BUILD-BRIEF.md`; payment, sign-in, runner or credit code uses
  `FIX-BRIEF.md`. Give each: the goal and why it matters to a 16-year-old on a phone, its files, the decisions already made,
  what to look at (390 Day, 390 Night, 1440 Day), tests, and its own tools folder inside its worktree (agents overwrite each
  other's files in the shared scratchpad). Opus for edge cases, money or taste; Sonnet for exact mechanical changes.
- On each report: look at one or two captures yourself, merge into `web/1115-prod`, add new test files to the right `test:*`
  script, run the suites it touched plus `test:app`, eslint. Payment, sign-in, runner, credit or session code gets an
  independent Opus review before the push; after every two or three merged UI lanes, one Opus agent checks the MERGED branch on
  a dev server and compares the home page with live. Before a push run `bash tmp/gate.sh` (24 suites, lint, build). After a
  push, poll something only the new build serves, check the public pages, `get_runtime_errors`, and send him an image of
  each new thing.
- Rules that do not bend: `.env.local` is the PRODUCTION database (no writes, sign-ins, payments, emails or paid model calls
  by agents; signed-in screens through `/preview/arena` fixtures); schema changes are a migration plus undo left for the owner;
  no question published beyond the 30-a-subject public samples without his yes; no rank or percentile without his yes; nothing
  stated that the code cannot back; no exclamation marks, emoji or arrows on buttons; refine and add, never remove or
  restructure what he approved; the den's rule F2. Security fixes ship at once and alone.
- Usage: check `get_usage` before each wave; four Opus lanes plus reviews took about 75% of a 5-hour window in 3 hours. Write
  the handoff and a `continuum_checkpoint` before 90%, and stop at a safe point when he says so.

## Report to him

Short and plain. Every update lists every item above with its status (done and live, built not live, running, not
started), what was checked and what was not, and what waits on him. Waiting on him now: apply
`20261115200000_late_papers_out_of_cohort_stats.sql` and `20261115210000_late_papers_out_of_mob_hours.sql`; for the emails, the
`20261115180000_student_emails.sql` migration, the under-18 consent line and the privacy page, then `EMAILS_ENABLED=true`; the
older list (Vercel and Supabase Pro, Resend plan, webhook events, DMARC, the 19 Nov deletion request, the Rs 69 payment of 26
Apr) in the first handoff. At the end update `NOW.md`, `PRODUCTION-PASS-2026-11-15.md` section 4, the owner master ledger and
the UI audit log, and save a `continuum_checkpoint`.
