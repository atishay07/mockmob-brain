# Prompt for the next session (paste as the first message)

You are continuing MockMob's production pass before marketing as the orchestrator. Call `continuum_start` for project
`mockmob`, then read, in this order, in `C:/Users/atish/mockmob-brain/docs/`: `HANDOFF-2026-11-15-PRODUCTION-PASS.md` (everything
that shipped, the exact repo state, the build list, the owner's waiting list, lessons), `NOW.md` (top entry), and section 3a and
section 1 of `UI-AUDIT-LOG.md`. Open `PRODUCTION-PASS-2026-11-15.md` only for a finding you are about to act on.

## What the owner wants from this session, in his words

"Focus more on building and building more things, and thinking about just the ideas to build more. Rather than just doing an audit
and thinking long on smaller things and refinements ... it is build-focused and production-focused. Keep building things and
improvising them ... tangible, actual results, not small refinements." "You can think for yourself what's useful, what's not, and
apply everything. Push it to live. Then we'll come back to the pending decisions."

So: no new audit. Build new, visible things for 16 and 17 year olds preparing for CUET on a phone, ship each to
www.mockmob.in when it is good, and keep one running list of what waits on him. Decide small product questions yourself.

## First 20 minutes (no agents)

1. In `C:/Users/atish/Desktop/mockmob copy/wt-1110-convert` (branch `web/1115-prod`, equal to `origin/main` at `6472026f0`):
   confirm on Vercel that the last production deployment is READY and that `https://www.mockmob.in/pricing` and `/daily` answer
   200. If the last build failed, read its log, fix, push.
2. Run `bash tmp/gate.sh` (24 suites, lint, `next build --webpack`) and read `tmp/gate.log`. Fix anything red; then trace the five
   tests the handoff lists as red outside the scripts.
3. Stop the dev server on port 3571 if it is still up; delete `.next` and `.next-dev`; remove today's merged lane worktrees as the
   handoff says (rmdir each `node_modules` junction first).

## Then build, in waves of three or four agents

Use the handoff's "Not done" list as the backlog, most valuable first: (2) the Daily Five as a habit, (3) the DU data check and
then the cutoff pages, (4) the Sunday Mock without the ranking line, (5) the two emails behind a switch, (6) late upload,
(7) the durable-sessions blocker, (8) first paint, then your own pick from (10). Items in (9) are small: batch them into one
Sonnet lane with exact instructions.

How to run a lane (this worked today):
- One worktree per lane cut from `web/1115-prod`, with a `node_modules` junction made in PowerShell
  (`New-Item -ItemType Junction -Path "<wt>\node_modules" -Target "C:\Users\atish\Desktop\mockmob copy\wt-1103-web-cards\node_modules"`),
  `.env.local` copied in, its own branch, its own dev-server port (3581 and up, `next dev --webpack`).
- The brief for every build agent is `wt-1110-convert/tmp/1115-prod/BUILD-BRIEF.md` (rules, the owner's UI rules, the report
  format); for a fix on sensitive code use `FIX-BRIEF.md`. Tell each agent to read it first, then give: the lane's goal and why it
  matters to a student, the files that are its own, the decisions you have already made, what to look at on screen, and the tests
  to run. Opus for anything with edge cases, money, or taste; Sonnet only for exact, mechanical changes.
- Scope the WHAT tightly (behaviour, states, copy that must be true, files) and leave the HOW IT LOOKS to the agent within the
  product's design: say "fit the design that is there, read DESIGN.md and the CSS beside it, one volt key per view, look at your
  own screens at 390 Day, 390 Night and 1440 Day and fix what you would not be proud of". Ask for real captures and look at one
  or two yourself before merging; send the owner an image of each new feature.
- When a lane reports: merge into `web/1115-prod`, add its new test files to the right `test:*` script, run `test:app` plus the
  suites it touched and eslint on its files, fix cross-lane test breaks, then push `web/1115-prod` to `main`. Before a push that
  touches payments, sign-in or the test runner, get an independent Opus review of that diff. After each push wait for the new
  build to serve (poll a URL that only the new build answers) and check the public pages.
- After every two or three merged lanes, one Opus agent looks at the MERGED branch on the dev server at 390 Day, 390 Night and
  1440 Day and reports only what is broken.

## Rules that do not bend

- `.env.local` points at the PRODUCTION database: no writes, no sign-ups, no sign-ins, no payments, no emails, no paid model
  calls from agents. Signed-in screens are seen through `/preview/arena` fixtures. Production schema changes are written as a
  migration plus an undo and left for the owner.
- Never publish a question outside the public sample windows (30 a subject) without his yes; never show a rank or percentile
  without his yes; nothing that states a fact the code cannot back; no exclamation marks, emoji or arrows on buttons; refine and
  add, never remove or restructure what he has approved.
- Security fixes ship at once and alone. Features ship when their tests pass and you have looked at them.
- Usage: a 5-hour window empties in about 90 minutes with twenty Opus agents. Keep to three or four at once, check
  `get_usage` before each wave, and write the handoff before 90%.

## How to report to him

Short, plain, honest. Each update lists every plan item with its status, including the ones not started, says what is live with
what was checked, what was not checked, and what waits on him. Send an image when there is something new to see. Update
`NOW.md`, `PRODUCTION-PASS-2026-11-15.md` (section 4, the record) and the owner master ledger at the end, and save a
`continuum_checkpoint`.
