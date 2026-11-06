# Round 3 fix spec (1 Nov 2026, about 7:50 pm IST): the critics' findings on the merged round 2

**Sources:**
- Screenshots of the merged round 2: `tmp/learn-1101/r2-merged/INDEX.md` (folders `p1`, `p2`, `p3`, `hero`, `extra`, `final`). Every item below names the shots that show it.
- Owner's words: `OWNER-FEEDBACK-2026-10-31-LEARN.md` in the mockmob-next docs (LK24-LK35).
- R2-SPEC.md rulings still bind, except where this file changes them. Where they disagree, this file wins.
- Shared words: `data/learn/words.js`. Free's after-session headline and line: `FREE_DONE_HEADLINE` and `FREE_DONE_LINE` in `data/learn/allowance.js`. Both exist already: import them, never retype the strings.

**Owner rules that bind every packet:**
- Refine, never rebuild.
- Never cut or hide a feature. Reordering, shortening and dropping a zero are fine.
- No "mastered", no mastery %, no "marks to recover".
- Sentence case. No exclamation marks, emoji or arrows on buttons. 12-hour time.
- Motion only answers an action or shows state (150-350 ms, ease-out) and respects reduced motion.

## 0. Rulings

### W. Words: one word for each thing, everywhere
Pin these in your copy tests.

| Thing | Use exactly | Never |
|---|---|---|
| Turning a Key card | Button "Turn over" (`WORDS.turnOver`). First-run cue "Tap the card to turn it over" (`WORDS.turnCue`). | "Show answer", "Flip", "Tap the card to turn it" |
| Hint on a question | "Pick the answer you think is right." (`WORDS.pickHint`). Show it only on the first question a student ever sees, once. | "Tap the answer…" (a desktop has no tap) |
| Key to resume an unfinished or stopped run | "Continue · 6 min" (`withMinutes(WORDS.continue, n)`). On every surface: home, chapter page, Explore cover, end screens. | "Pick up where you stopped", "Pick up, 9 minutes" |
| Heading that introduces a resume | "Pick up Admission of a Partner". Home offer only, as now. | |
| End key: more left in this chapter (run and feed) | "Keep going · 10 min" | "25 new cards left here, 10 min", "Another 10 minutes" |
| End key: every card in the chapter seen | "Next chapter · 10 min" | |
| Question mistakes | "Fix 3 open mistakes · 3 min" (`fixMistakes`). Counts read "3 open mistakes", or "2 open mistakes fixed" on ends. | "old mistakes", "mistakes tried", "missed" as a count of mistakes |
| A Key card to Revise | "Revise later" (`WORDS.reviseLater`). After the server confirms: "In Revise" with a check. Card-stack icon. | "Keep"; a bookmark icon for cards |
| A question to Saved | "Save" / "Saved". Questions only, by design. Bookmark icon. | |
| Due Key cards | "Revise 9 due cards · 3 min" (`reviseDue`) | a bare "9 due" or "8 due" anywhere |
| Today's paper questions to revise | "Revise · 5 questions" (`reviseQuestions`) | "Revise 0 of 5 questions" |
| Learn's level check (kind 'level') | Label "Skip what you already know" (`WORDS.skipKnown`). Line "6 questions · about 6 min". Today keeps "Find your starting point": that is a different thing, a 10-question paper. | "Find your level" |
| Time | " · N min" after a label, N rounded up, at least 1 (`withMinutes`) | ", 10 min", "minutes" |

### F. Free after the day's session: one rule, true to `data/learn/allowance.js`
**What the server allows.** Free has one counted session a day, a 'mix' or a 'feed'. After it:
- A new feed is refused.
- A new chapter run is Key cards only: the chapter's 5 open cards.
- These stay open: Revise due cards ('cards'), quick recap ('recap'), the level check ('level'), and picking up today's own run.
- Explore's single questions stay free.

**Learn home's Free-done state and the feed refusal screen** (shots: `p1/home-free-done-390-*`, `p2/21-feed-free-refused-390-day.png`):
- Both show the same block.
- Headline: `FREE_DONE_HEADLINE`. Line: `FREE_DONE_LINE`.
- Main key: "See Pro".
- Up to 2 quiet Or rows, in this order, only those that apply:
  1. "Continue · N min" (today's unfinished run)
  2. "Revise N due cards · M min" (due > 0)
  3. "Answer single questions" (Explore)
- "Learn opens again tomorrow" must not appear anywhere.

**Free run end or feed end when the session is used** (`extra/96-run-end-free-390-night.png`, `extra/95-feed-end-free-full-390-night.png`):
- One quiet line directly above the keys: `FREE_DONE_HEADLINE` + " Questions come back tomorrow."
- Main key: "Quick recap · 1 min" when the session had cards. Otherwise "See Pro".
- Quiet link: "See Pro" (unless it is already the main key).

**Server checks:**
- Every key above must be accepted by the server for that student. Add a test per key against `freeSession` and the start route.
- `FREE_SESSION_DONE` (the 402 line) becomes `${FREE_DONE_HEADLINE} ${FREE_DONE_LINE}`.
- `FREE_CARDS_ONLY` keeps its meaning. Reword it as "That was today's free session, so this one is Key cards only. Questions come back tomorrow."

### Z. No zero leads
This extends ruling 1 to Today, Practice, the ends and the badges.
- Never render a count of 0 as a lead or as "0 of N". Show the goal instead ("4 study days this week") or drop the count. `hasZeroCount` in `data/learn/roadmap.js` is the test helper.
- The sidebar and phone dock never show a due number. Each mark is a dot with an aria-label: "Key cards due in Learn", "Questions to revise".
- Every dot has an aria-label, including the Papers tab dot.

### L. Layout: run, feed and ends (390x844 and 1440x900, Night and Day)
**L1. Key card, front and back, all sizes** (`extra/91-feed-first-visit-first-item-390-night.png`, `p2/57-run-first-card-new-390-night.png`)
- The card keeps filling the stage.
- Inside the card:
  - type label top-left, menu top-right (as now)
  - the text block vertically centred in the space between them and the source line
  - the source line pinned to the card's bottom (as now)
- Front size by length, phone / desktop:

  | Front length | Size |
  |---|---|
  | ≤ 60 characters | 34 / 40 px |
  | ≤ 140 characters | 28 / 32 px |
  | longer | 22 / 26 px |

  Line-height 1.15. `text-wrap: balance`. `hyphens: manual`.
- When the content does not fit (long backs), top-align it and scroll inside the card.

**L2. Questions** (`p2/52-run-question-390-night.png`, `p2/52-run-question-1440-night.png`)
- **Phones (< 768 px):**
  - The context line ("You missed this in Mock 3 on 16 Oct") and the stem sit at the top.
  - The options group (options, then Skip) is anchored to the bottom of the stage with `margin-top: auto`, so it sits in the thumb zone.
  - When the stem and options are taller than the stage, use plain top-to-bottom flow and scroll.
- **Desktop:** centre the play column vertically in the viewport, with a top margin of at least 48 px.

**L3. Feed peek, always, all sizes** (`extra/91-feed-first-visit-first-item-390-night.png`, `…-1440-night.png`)
- **The peek:**
  - The next item's top 40 px shows directly above the action row as a real card edge: the same width as the current card, with top radius, border, the card background, and the next item's type label inside at the left.
  - It must never show as a bare word.
- **The chip, first visit only:**
  - The chip sits centred inside that 40 px strip and is 36 px tall. The type label is hidden while it shows.
  - Phone: Mobi's head + "Swipe up for the next one" + an up chevron.
  - Desktop: Mobi's head + "Scroll or press ↓ for the next one", with no chevron.
  - Nothing moves when the chip goes. The bob and the seen-only-after-moving rules from R2 ruling 7 stay.
- **The feed checkpoint** (`p2/16-feed-checkpoint-390-night.png`) follows the end-screen layout (L5).

**L4. Top bar, run and feed** (`p2/53-run-wrong-line-390-night.png`, `extra/91-…`)
- **The bar:** one row with the X, the progress bar and the counter "4 of 20". Under it, one quiet line with the chapter name (one line, with an ellipsis).
- **The Revise-later pile:**
  - Phones: not in the bar.
  - Desktop (≥ 1024): one card-stack icon, the visible label "4 to revise" (`pileLabel`), and aria-label "4 cards to revise later". Shown only when the count is at least 1.
  - The feed's "Revise later" button uses the same card-stack icon, not a bookmark.
- **"Revise later" on phones:** with no pile, the button itself shows the confirmed state ("In Revise" with a check) once the server confirms. Never before.

**L5. End screens: run, feed, stopped, Free** (`p2/55-run-end-390-night.png`, `p2/56-run-end-stopped-390-*.png`, `p2/18-feed-end-390-day.png`, `p2/55-run-end-1440-night.png`)
- **Phones:**
  - The content group is centred vertically in the space between the X and the key group: chapter line, headline with Mobi, card fan, numbers row, bar.
  - The key group is pinned to the bottom with padding-bottom `max(24px, env(safe-area-inset-bottom))`. It holds the Free line when present, the main key and the quiet link.
- **Desktop:** one column, at most 560 px wide, centred both ways in the viewport. Mobi sits in the headline row, to its right.
- **Headline:** "18 done". Add " in 12 min" only when the time is at least 2 min.
- **Numbers row:**
  - At most 3 numbers, zeros dropped, with the same labels on run and feed ends:
    - "14 in Revise, back Wed"
    - "1 of 2 questions right"
    - "2 open mistakes fixed"
  - No "cards seen" number in the row. The bar's label carries it: "20 of 45 cards seen".
- **Card fan:** both ends show it when at least 1 card went to Revise this session, and neither shows it otherwise.
- **Keys:** main key "Keep going · 10 min", or "Next chapter · 10 min". Quiet link "Fix N open mistakes · M min" when there are any.
- **Stopped run (`stopped: true`, the blocker C2-1):**
  - Headline "5 of 20 done".
  - Main key "Continue · N min". It resumes that run by its run id.
  - Quiet link "Fix N open mistakes · M min", only if it starts a NEW mistakes-only run. Pass `fresh: true` or the mistake ids, and never resume the stopped run.
  - Today, both end keys start a 'mix' of the same chapter. `start()` (`src/lib/server/learn.js` about L808) then resumes the same-day stopped run at item 4. Fix that.
  - Add a test: stop, then the end's fix key gives a mistakes-only run, and the end's main key resumes the stopped run.

**L6. Card text everywhere** (the minis, the fan, First up, the piles; `p2/18-feed-end-390-day.png`, `extra/89-chapter-fresh-free-full-390-night.png`): `hyphens: manual; text-wrap: balance`. Minis clamp to 3 lines with an ellipsis. No "partner-ship", "sacri-fice".

**L7. Day theme scrim** for the stop sheet and the other Learn sheets (`extra/93-run-stop-sheet-390-day.png`): a light, tinted scrim (the Day background colour at about 60% opacity), never a grey wash.

### H. Home hero
**H1.** The H1 is static: "CUET 2027. One mock. Know what to fix." "CUET 2027." keeps its accent colour.
- Remove: the typing, the caret, the cycling lines, any highlight animation.
- Mobi's taps carry the reactions, not the H1.
- Shots: `hero/hero-tap4-390-night.png`, `hero/hero-first-1440-night.png`.

**H2. The trust line** never breaks inside a segment.
- Render each " · " segment with `white-space: nowrap` ("No auto-renewal" stays whole). The line may wrap between segments.
- The price words stay driven by `OFFER`. One-time vs monthly is decided by the environment and is true: leave it.

**H3. Desktop** (`hero/hero-first-1440-day.png`, `hero/hero-tap4-1440-night.png`)
- The host Mobi and its bubble sit fully in the gutter left of `.lp-stage__card`, with no overlap of the card's border or content at 1280, 1440 and 1920.
- The Night bubble text has contrast of at least 4.5:1.

**H4. The Day room poster:**
- If its marks are HTML or SVG, make Day's marks as sparse as Night's (a few filled, most empty).
- If they are painted into the image, leave it and say so.

### C. Counts: one source each
**C1. Key-card due:**
- One server function returns `due.all` and `due.bySubject`. `/api/learn/home` and `/api/learn/shelves` both use it.
- Test: the same fixture gives the same `due.all` from both routes.
- The Learn home Revise row reads only this.

**C2. Chapter counts:** a subject's chapter count is its playable chapters. Exclude coming-soon chapters and chapters with no cards. This applies everywhere Learn shows it: the desktop subject tab line, the offer's "Chapter 1 of 14", the roadmap.

**C3. Practice's subject tile "2 chapters"** (`extra/80-practice-dashboard-390-night.png`): find what it counts, then either label it for what it is or drop it.

### R. Learn home (`extra/86-learn-home-fresh-free-390-night.png`, `…-1440-night.png`, `extra/88-learn-home-returning-pro-full-390-night.png`)
**R1. Phones (< 768):** replace the subject strip with a single subject picker: the subject's icon, its name and a chevron, opening the subject list as a sheet. Use Explore's picker if it has one. Desktop keeps its tabs.

**R2. The offer:** keep "Chapter 1 of 14 · <chapter>" under the headline. Delete the row of ring dots.

**R3. Or rows:** at most 2, in this order, only those that apply:
1. "Revise N due cards · M min" (due > 0)
2. "Skip what you already know", line "6 questions · about 6 min". Only while the subject has no Learn activity.
3. "Play this chapter as a feed"

**R4. Delete the status line under search** ("9 due · 6 missed · 26 in Revise"). The Revise row replaces it.

**R5. Roadmap:**
- Drop the subline "14 chapters, in book order". The sort control already says it.
- Unstarted rows: the title and "45 cards · 10 questions", with no bar.
- Started rows: as R2 ruling 2.
- Free: say "5 free in each chapter" once in the roadmap header, never on rows.
- A part with options (Accountancy Part 2): one line above the pills, "Part 2 has two options. Pick the one your school teaches."
- Chapters with no cards are hidden. If the student's picked option has none at all, show one line: "Cards for this option are coming."

**R6. Desktop subject tab line:** "14 chapters · 866 Key cards · 4 lessons". No due count there.

### T. Today: refine, never cut; every section stays (`extra/85-today-brand-new-free-390-night.png`, `…-full-390-night.png`, `extra/84-today-returning-pro-full-390-day.png`)
**T1.** For a student with no history:
- Drop the line "Tomorrow: your first mistakes come back. Day 7 is done already: your plan is set."
- No day is ticked before it happens. Day 7 must not show a tick.

**T2.** No zero leads (Z):
- "0 of 4 study days" becomes "4 study days this week".
- The Road to CUET counters show goals without "0 of": "1 session today", "4 study days this week", "13 full mocks".
- "Revise 0 of 5 questions" becomes "Revise · 5 questions" (`reviseQuestions`).

**T3.** At 390x844, a brand-new student sees the start card's main key fully above the dock, with nothing cut.
- First, apply T1.
- If the key is still not visible, move the "Your colleges" card below the start card. Keep both colleges entries: the owner calls them edit paths, never cut.

**T4.** The three explainer sections (Weak chapters, Repairs and Revise, Your colleges) keep their headings, with one line of explainer each (at most 90 characters).

**T5.** Weak-chapter names use the canonical syllabus titles, from the same source the roadmap uses ("Goodwill: Nature and Valuation", not "Goodwill").

### X. Explore, Saved, Practice, chapter page
**X1. Explore singles** (`extra/90-explore-first-visit-full-390-night.png`, `p3/82-explore-singles-390-night.png`):
- Show 3 questions with distinct stems: normalise the stems and drop duplicates.
- Take them only from the student's CUET syllabus chapters ("Accounting Equation", Class 11, is out), preferring 3 different chapters.

**X2. Explore's header:** "Saved 2" only when the count is at least 1, otherwise just "Saved". Fix the preview fixture so a brand-new student has 0 saved.

**X3. The Saved page:** chapter labels use the canonical syllabus titles.

**X4. The Explore cover:** "For you: 3 open mistakes to fix". The resume key is "Continue · 9 min".

**X5. The Practice page** (`extra/80-practice-dashboard-full-390-night.png`, `p3/80-practice-full-390-night.png`):
- Confirm that P3's Practice changes survived the merge: compare `git show 739687993` for the Practice files with HEAD.
- For Pro, remove every one of these: "Included", "Included with access", "Included with your Pro access (valid until …)", "Your access … Unlimited".
- The hero is one line.
- Merge the duplicate Quick practice summary card into the sticky bar.
- The sticky Fine-tune bar never covers the mode cards: reserve its height at the end of the scroll area.

**X6. The chapter page** (`extra/89-chapter-fresh-free-full-390-night.png`):
- "Quick recap · 1 min" only after the student has seen at least 1 card in the chapter.
- The pile tip ("Tap a pile to leave it out.") shows once per student.
- At 390 the piles share the full row width.
- The resume key is "Continue · N min".

**X7. Explore with `l2=off`:** no hydration error. Render the flag-dependent branch the same on the server and the client.

### S. Shell
- **S1. Sidebar:** the yellow active bar shows only on the current route's item. Learn's bar must not show on Practice, Explore or Saved (`p3/80-practice-1440-day.png`).
- **S2. Badges:** Z's dots apply to the sidebar ("Learn 27 due", "Your papers 8 due") and to the phone dock's "8 due".
- **S3. The theme switch:** no hydration mismatch. Render a neutral state on the server and set the real one after mount, or read the cookie on both sides (`p1/find-new-free-1440-day.png`).

## 1. Packets and the files each one owns
**Branching:** every packet branches from `web/1031-learn-v2` at the commit that adds this file. Each one reuses its round-2 worktree on a new branch.

**Ownership:**
- Never edit a file another packet owns.
- If you need a change in another packet's file, append it to `docs/brain/learn-1031/r3/NOTES.md`, and the orchestrator merges it.
- `data/learn/words.js` and `allowance.js`'s two constants are shared and read-only. R3-run owns the rest of `allowance.js`.

| Packet | Worktree / branch | Owns | Implements |
|---|---|---|---|
| R3-run (Opus) | `wt-1101-r2-run` / `web/1101-r3-run` | `src/components/learn2/run/**`, `feed/**`, `stage/**` (the card minis, the fan, the top bar, the end screens, the refusal screen, the sheet scrims); in `src/lib/server/learn.js`, the end, feed-end, stop and Free-end functions and `start()`'s resume branch; `data/learn/suggest.js`; `data/learn/allowance.js` (the lines) | W for run, feed and ends; F for ends, refusal and the allowance lines; L1-L7 |
| R3-home (Sonnet) | `wt-1101-r2-home` / `web/1101-r3-home` | `src/components/learn2/home/**`, `data/learn/roadmap.js`; in `learn.js`, the home, shelves, subject and search functions; `src/components/learn2/api.js`; the app shell (sidebar, phone dock, theme switch) | W for home; F for home; Z for badges; C1, C2; R; S |
| R3-today (Sonnet) | `wt-1101-r2-speed` / `web/1101-r3-today` | Today's components, `useToday`, `src/lib/today/**`, the Today read path (`todayReads.js`) | T; Z and W on Today |
| R3-explore (Sonnet) | `wt-1101-r2-explore` / `web/1101-r3-explore` | `src/components/learn2/chapter/**`; the Explore page, its covers and `DiscoveryFeed.jsx`; the Saved page; the Practice dashboard components; the preview arena fixtures | X, C3; W on Explore and the chapter page |
| R3-hero (Sonnet) | `wt-1101-r2-hero` / `web/1101-r3-hero` | `src/components/landing/**` hero parts, `src/app/page.js` hero section, public hero images | H |

## 2. How every packet works
- **Read first:**
  - AGENTS.md, then `node_modules/next/dist/docs/` before writing Next code
  - DESIGN.md
  - the owner's UI standards at `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`
  - this file
  - the shots it names, in `tmp/learn-1101/r2-merged/` of the `wt-1031-learn-v2` worktree
- **Tests:**
  - Keep the suites green and extend them: `test:learn`, `test:keycards`, `test:today`, `test:app`, `test:auth`, `test:egress` and lint, whichever touch your files.
  - Write a unit test for every new pure rule, and pin every exact string from W and F that you render.
  - Read the fail count before you commit. Never commit on a red suite.
- **Look (RAM rule):**
  - At most 2 dev servers on this PC. Take a slot with `mkdir "C:\Users\atish\Desktop\mockmob copy\tmp-devslots\slot-1"` (or slot-2). If both exist, wait 60 s and retry.
  - Run `npx next dev --webpack -p <port>`. Ports: run 3482, home 3481, today 3484, explore 3483, hero 3485.
  - Hold the global browser lock (`mkdir "C:\Users\atish\Desktop\mockmob copy\tmp-devslots\browser.lock"`; it is stale after 10 minutes) around every headless browser run.
  - Capture your surfaces at 390x844 and 1440x900, Night and Day, into `tmp/learn-1101/r3-after/<packet>/` of your worktree. Use the `/preview/arena` views and params from `tmp/learn-1101/r2-merged/INDEX.md` in `wt-1031-learn-v2`. R3-hero uses `/`.
  - Open every shot and look at it against these rulings and the UI standards' done check. Fix and capture again: at most 2 rounds.
  - Stop the server and remove the slot and the lock when done.
- **Finish:**
  - Commit on your branch.
  - Kill every process you started: the dev server, browsers, node.
  - Return per ruling item what changed (file:line), the test counts, the shot folder, and anything left with the reason.
- **Never** push, deploy, sign in to production, or write to a database.
