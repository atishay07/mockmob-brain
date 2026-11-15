# Handoff: production pass, second half, 15 Nov 2026 (about 7:40 to 10:50 pm IST, Opus orchestrator)

Read with: `HANDOFF-2026-11-15-PRODUCTION-PASS.md` (the first half and the owner's list), `PRODUCTION-PASS-2026-11-15.md` section 4
(the record), `NOW.md` top entry. His brief for this half, his words: "Focus more on building and building more things ...
tangible, actual results, not small refinements." "Think for yourself what's useful ... apply everything. Push it to live."

## What is live on www.mockmob.in (main `79ff0d94e`)

| Release | What | Checked |
|---|---|---|
| `a3bad4078` | Practice average uses signed marks (B11); students read "course" (19 files; degree names kept); "Open in Chrome" at the top of `/signup` in Android in-app browsers; Android Back cannot leave the NTA warning closed with answers locked (not after the paper ended); unused CloseSheet gone | review (no blocker, 1 should-fix applied); live wording, 9 routes, no runtime errors |
| `12516f20f` | DU data check (all 3 rounds, 17,316 printed scores match; `data/du-csas-2026/verification/REPORT.md`); cutoff pages `/du-cutoffs`, 68 courses, 67 colleges, in the sitemap | live 200s, 404 for unknown, titles |
| `79ff0d94e` | Daily Five as a habit (each answer checked on the server, a signed-in student's first check is the account's record; a study day; the Mob's rows in the den, only sitters; "Daily Five" in the public bar; "64% got this right" from 30 students; the run from the account); the Sunday Mock (one fixed free full paper per subject each Sunday, starts 10:00 am to 10:00 pm IST, answers and counts at 11:05 pm, a seeded draw that skips the last 8 Sundays, the den block, Today card, Practice row, `/sunday-mock`; first one 22 Nov); welcome and day-2 emails built and OFF | 2 independent reviews (blocker fixed, should-fixes applied); merged visual check; gate 24 suites, lint, build 256 pages; Vercel preview READY |

Rollback points, newest first: the `12516f20f` build, the `a3bad4078` build, `dpl_FrLEwppYrcbQLF99CvqrRt1eNbST` (`6472026f0`).

## Built but NOT live (do these first)

1. **First paint** (branch `web/1115-paint`, merged then reverted in `79ff0d94e`): the 23 home sheets joined into one generated
   `src/app/home-sheets.css` (FCP 5.5 s to 4.4 s locally, 4x CPU slow 4G), Literata not preloaded, creator photos lazy, logos
   at 96 px (262 to 89 KB). Held because the merged visual check saw, in the webpack build, the joined sheet load BEFORE
   `scroll-story.css`, `section-position.css` and `du.css`, which flips same-specificity rules: the tour hold +502 px at 390,
   the Lab cinema hold -144 px, the DU teaser card's fill (near-white in Day instead of beige), the position bar gaps
   (`wt-1115-look/tmp/look/`). Production (Turbopack) may order differently and the preview is behind Vercel sign-in. To
   return it: `git revert 79ff0d94e`'s paint part (or re-merge `web/1115-paint`), then make the cascade order-proof (raise
   the home rules that override those three sheets, or move those three sheets' home-only rules into the join), check the
   three spots, ship, and on production compare `/` at 390 Day/Night and 1440 Day against today (page height 20,885 px at
   390 before), with the rollback ready.
2. **Late upload and the durable start race** (branch `web/1115-sess`, pushed; worktree `wt-1115-sess`): built and green.
   Held: a modified client can send a looked-up perfect paper up to 7 days late. The exact list is in the branch at
   `tmp/1115-prod/SESS-FOLLOWUP.md`: late papers earn no badges, study day, Mob chain or Mob hours (new migration for
   `mob_hours_rows`); a line on the result; `readLatePapers` fails soft plus an index; the durable start gives the free row
   back if the RPC fails. Then an independent review, then ship alone. The CTO note: `tmp/1115-prod/durable-sessions-ready.md`.
3. **Sunday Mock, before 22 Nov:** replacing a withdrawn question re-runs the whole draw (pass the missing count; cache per
   week, subject and frozen ids, `service.js:123`, `draw.js:35,47-51`); the draw ignores the evidence-tier preference the Full
   mock has (`singleTier`, `mock_question_selector.js:131`): prefer verified tiers. The `/sunday` page has no top-bar title
   (`AppLayoutClient` `currentTitle`).
4. Small: the calculator opened from a cutoff page should show that course before subjects are picked
   (`CutoffCalculator.jsx`, `?course=`); `/daily` loading placeholder is taller than the card (CLS 0.05-0.08).

## Not started from the build list

The small payment items (`expire_by` on Get Pro, `referralAttributionFromCheckout` reads payer-set notes, same-origin for
`/create-monthly-subscription` and `/verify-payment`); the ideas list (Mob class leagues, "bring a mistake", public Key card
decks per chapter (the free taste of 5 a chapter), corrections log, badges refined, desktop two-column Wallet/Progress/
result, a tablet walk); Next 16.3.8 with `chart.js` removal.

## Waiting on the owner (new tonight; the earlier list in the first handoff still stands)

- Apply `supabase/migrations/20261115180000_student_emails.sql` (undo in `supabase/undo/`), write the under-18 consent line,
  add both emails to the privacy page, then set `EMAILS_ENABLED=true` (optional `EMAILS_DAILY_CAP`, default 40). Look at
  the two emails: `wt-1110-convert/tmp/1115-prod/lane-shots/mail/`.
- When `web/1115-sess` ships: apply `20261115200000_late_papers_out_of_cohort_stats.sql` and the Mob hours migration.
- Decide: the NTA warning comes back on Android Back while the paper runs (built so; letting Back dismiss it would skip
  fullscreen); the Sunday Mock is free, one sitting a subject a week (my call); the Daily Five is an honour system (its
  questions are the public sample's, whose answers are public); a late paper counts on the day it arrives.
- Content: the Bulletin's free-text course notes are mis-parsed (B.Com carries the BBA text), so the cutoff pages omit them.

## Lessons

- A merged-branch visual check again caught what no lane saw (the cascade). Keep it before every push of UI.
- Reviews found a blocker in a lane that passed its own tests by faking the selector: ask lanes to test with the real
  selector or the real query, not a fake of the piece that matters.
- The den's rule F2 beats a brief: read the area's own rules before writing a lane brief.
- Usage: four Opus lanes plus three reviews and a visual check took about 75% of a 5-hour window in 3 hours.
- Agents share the session scratchpad: give each its own tools folder inside its worktree.
