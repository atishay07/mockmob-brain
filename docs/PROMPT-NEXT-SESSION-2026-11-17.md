You are continuing MockMob's production pass before marketing as the orchestrator, working autonomously. Call `continuum_start`
for project `mockmob`, then read in `C:/Users/atish/mockmob-brain/docs/`: `HANDOFF-2026-11-16.md` (all of it), `NOW.md` (top
entry), `UI-AUDIT-LOG.md` sections 1, 3 and 3c. The owner-only list is in `HANDOFF-2026-11-15-PRODUCTION-PASS.md`.

## The owner's direction (16 Nov 2026; his words are quoted in the handoff)

He rejected a quiet, correct Daily Five row in one look and approved a large calendar page in MockMob's own identity in one
look. He wants: a highly converting website; every feature thought through for how it is presented, how it works and its
whole flow; "not always taking the safest approach"; each recurring thing shown clearly, "what it is exactly and how we do it
every time"; no copying a rival; no generic, templated UI ("AI slop"); "keep going until you attain perfection". He judges on
his Android phone, from what is live on www.mockmob.in.

## Do, in this order, without stopping to ask

1. If `web/1116-race` (worktree `wt-1116-race`) is committed and not merged: read its `tmp/1116-race/CTO-NOTE.md`, get an
   independent Opus review of the diff (credit code), fix what it finds, merge, gate, ship. Its migration stays unapplied for
   the CTO.
2. The landing, feature by feature, in his direction. For each feature: look at its section on the live home page at 390 Day
   as a 16-year-old would, decide what one confident block would make them want it, build it large with one idea from
   MockMob's own world (paper, ink, volt, the desk, Mobi), say what it is and when it happens in plain chips or a line, give
   it a full-size key. Start with what the landing does not show at all: Ask Mobi's "bring a mistake"; then the Mistake Lab's
   entry, the exam screen, pricing. The reference for the level: the two calendar pages under the sample card
   (`src/components/daily/DailyFiveRow.jsx`, `DailyParts.jsx`). Do the bold design work yourself in the main session; give
   lanes the exact, well-specified parts.
3. The first minute after sign-up, with the same care (`wt-1110-convert/tmp/1115-prod/flow-first-run.md`).
4. Then by value: Mob class leagues (class code, weekly paper, class average, no names; migration plus undo for the owner), a
   public corrections log, the remaining loading states, Next 16.3.8 with `chart.js` removed (own release, its own
   `node_modules`).

## How to run it (what worked)

- Lanes: one worktree each, cut from `web/1115-prod`, `node_modules` as a PowerShell junction
  (`New-Item -ItemType Junction -Path "<wt>\node_modules" -Target "C:\Users\atish\Desktop\mockmob copy\wt-1103-web-cards\node_modules"`),
  `.env.local` copied, a port from 3595 up, its own tools folder. Every build lane reads
  `wt-1110-convert/tmp/1115-prod/BUILD-BRIEF.md`; credit, payment, sign-in or runner code also `FIX-BRIEF.md`. Two or three
  Opus lanes at once; each cost about 12% of a 5-hour window.
- On each report: open one or two captures, merge into `web/1115-prod`, add new test files to `package.json` with a JSON
  edit, run the touched suites. Credit, payment, sign-in, runner or session code gets an independent Opus review first.
  Before a push: `bash tmp/gate.sh` (24 suites, lint, build), and captures of the merged branch
  (`node tmp/1116-daily/quick.mjs <label> <WxH> <theme> <path...>`, `merged.mjs`). After a push: wait for something only the
  new build serves, check the public pages, compare the home page's sections in the browser pane at 390 against the numbers
  from before the push, `get_runtime_errors`, and send him an image of each new thing.
- Rules that do not bend: `.env.local` is the PRODUCTION database (no writes, sign-ins, payments, emails or paid model calls
  by agents; signed-in screens through `/preview/arena` fixtures); schema changes are a migration plus undo left for the
  owner; no question published beyond the 30-a-subject public samples without his yes; no rank or percentile without his
  yes; nothing stated that the code cannot back; no exclamation marks, emoji or arrows on buttons; never remove or hide what
  he approved; the den's rule F2. Security fixes ship at once and alone.
- Usage: check `get_usage` before each wave. Write the handoff and a `continuum_checkpoint` before 90%.

## Report to him

Short and plain, every update: each item with its status (done and live, built not live, running, not started), what was
checked and what was not, and what waits on him (the list is in the handoff). At the end update `NOW.md`,
`PRODUCTION-PASS-2026-11-15.md` section 4, the owner master ledger and the UI audit log, and save a `continuum_checkpoint`.
