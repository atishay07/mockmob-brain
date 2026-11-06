# Round 4 fix spec (1 Nov 2026, about 10:20 pm IST): the verified findings on the merged round 3

**Sources:**
- `R3-REVIEW-FINDINGS.md` in this folder. It holds the five lenses' findings, each checked by 1 to 3 independent skeptics.
- The findings' IDs (for example `ui-correctness#1`) are what this spec cites. Open the finding for its full problem, fix, images and evidence.
- Screenshots: `tmp/learn-1101/r3-merged/INDEX.md` in the `wt-1031-learn-v2` worktree.
- R3-SPEC.md and R2-SPEC.md still bind. Where they disagree, this file wins.

**Owner rules that bind every packet:**
- Refine, never rebuild. Never cut or hide a feature.
- No "mastered", no mastery %, no "marks to recover".
- Sentence case. No exclamation marks, emoji or arrows on buttons.
- Motion only answers an action or shows state. Respect reduced motion: `prefers-reduced-motion` AND the app's own `html[data-motion='reduced']`.
- Nothing floats over content. Never confirm success before the server does.

## 0. New rulings

### N. A chapter is named by its place in the roadmap
- **On screen,** a chapter's number is its place among the student's playable chapters, in roadmap order:
  - "Chapter 5 of 14" (`chapterPlace(place)` in `data/learn/words.js`)
  - "Chapter 5" in tight spots (`chapterShort(place)`), such as Explore covers
- **The NCERT chapter number** appears only inside a card's source line, which already starts "NCERT, …" and is true to the book.
- **Never draw a bare "Part 1, Ch 2" as a chapter label.** Today three different chapters show "Ch 2" (owner-eye#2, ui-correctness#13).
- **The server contract (R4-server builds it):**
  - Every chapter object that the Learn API returns to a page showing a chapter label carries `place: { n, of }`. That covers the chapter page, Explore covers, the run and feed start payloads, and the end payloads.
  - `n` is the 1-based position in the same order and with the same playable filter as the roadmap, including the student's part option. `of` is the playable count (C2).
  - `ref` stays in the payload, but only for source lines.
  - Clients render `place` through the two helpers. When it is missing, they draw no label, never "Ch N".

### V. Verdicts say where they come from
- **`needsWorkFrom` on roadmap rows** is either `'papers'` or `'learn'`, and R4-server sets it.
- **When the evidence is only from papers,** the row reads "Needs work · from your papers" (first-timer#13).

## 1. Packets, files owned, and findings each one fixes
Every packet branches from `web/1031-learn-v2` at the commit that adds this file, reusing its round-2 worktree on a new branch. Never edit a file another packet owns. Write cross-packet requests in `docs/brain/learn-1031/r4/NOTES.md` (append only).

### R4-server (Opus)
- **Worktree / branch:** `wt-1101-r2-home` / `web/1101-r4-server`
- **Owns:**
  - `src/lib/server/learn.js`
  - `data/learn/*.js`, except `words.js` and `allowance.js`'s constants, which are shared and read-only
  - the `/api/learn/*` routes
  - their tests: `data/tests/learn_*.test.mjs`
- **Fixes:**
  - **server-security#1 (high):**
    - Free must never be offered a "Continue" or fix key that the server then refuses. Treat today's unfinished counted run as the pending holder.
    - Add the route test the finding names.
  - **server-security#2 (high):**
    - `dueNow` and `dueSummary` filter by the student's part option (`syllabus.sectionAllowed`) and drop retired chapters.
    - The Revise label's count equals its `cardIds.length` (it shares one list).
    - Add an options fixture to the C1 test, and assert `due.all === kc.dueCount`.
  - **server-security#4 and first-timer#6 (medium):** the 402 refusal's Revise option uses the same subject-wide, filtered due list as home.
  - **server-security#3 (medium):**
    - `start()` resumes only a run with the same full `leave_out` set.
    - Roadmap's fix row (and the suggestions' fix action) send `fresh: true`.
    - Add the test the finding names.
  - **server-security#5, #6, #7 (low, do them):**
    - An ended run never gets the stopped keys.
    - A stopped level run is consistent.
    - The Revise label states the run's own count and minutes when capped at 100.
  - **N:** `place` on every chapter payload listed above. Keep `ref` for source lines.
  - **V:** set `needsWorkFrom` on roadmap rows.
  - **owner-eye#9 (medium):** when the offer line already says "N due cards first, then new ones here", drop the "Revise N due cards" Or row (keep one).
  - **first-timer#7 (medium):** the feed Or row's line becomes "Scroll through the chapter, stop any time".
  - **Content route checks:** none. The decks are not this packet's.

### R4-run (Opus)
- **Worktree / branch:** `wt-1101-r2-run` / `web/1101-r4-run`
- **Owns:**
  - `src/components/learn2/run/**`, `feed/**` (except Explore's cover files), `stage/**`
  - `src/components/learn2/links.js`
- **Fixes:**
  - **client-code#1 (high):**
    - Every in-place start or resume writes the address with `router.replace(?run=<newId>…)`, dropping `end=1` and `fresh`, in the run and in the feed.
    - Test: after onStart, the URL names the new run id.
    - Add a `fresh` option to `links.run`.
  - **ui-correctness#5 (high):** "Options below" shows only when the options are really below the fold. It goes inside the stage, never on the peek strip.
  - **ui-correctness#7 (medium):** after a wrong answer, the stem's first line and the context line stay in view. Never scroll them under the bar.
  - **owner-eye#14 (medium):**
    - Fan minis use `text-wrap: pretty` (not balance) and a smaller size, so 3 lines of about 18 characters fit.
    - Truncate at a word boundary, never mid-word.
  - **ui-correctness#14 and client-code#4 (medium):**
    - The desktop pile reads `pileLabel(n)` with the card-stack icon, in the SessionPanel and the TopBar.
    - It has an accessible name ("4 cards to revise later") via `role="img"` or a visually hidden span.
    - "In Revise" stays only for a card's confirmed state.
  - **first-timer#4 (medium):** on a Free end, when the seen cards equal the free count, the bar reads "5 of 45 cards seen · the rest open with Pro".
  - **Lows, do them all:**
    - The question hint shows once per student (not per run), above the options.
    - Run and feed use one close control, X plus "Close", on runs, feeds, ends and refusal.
    - The stop sheet's quiet key becomes "Back to it", so "Keep going" means only the end key.
    - The source line is pinned to the card's bottom on the back too.
    - `begin()` gets a request token. Stale responses are ignored, and the keys are disabled while a start loads.
    - Announce the first Revise through the player's live region.
    - Mirror every reduced-motion rule under `html[data-motion='reduced']`.
  - **N:** the run and feed rails show `chapterPlace(place)` instead of any "Part 1, Ch N" label.
  - **Science notation (new):**
    - Add a pure `sciText(text)` in `stage/` with a unit test. It returns segments of plain, subscript and superscript text. The stage renders it for card front, back and quote when the subject is `chemistry`.
    - Rules:
      - A table of common ions sets the charge: NH4+, OH−, NO3−, SO42−, CO32−, PO43−, HCO3−, Cu2+, Fe2+, Fe3+, Zn2+, Ag+, Na+, K+, Cl−, Ca2+, Mg2+, Al3+, H3O+ and the like. For example SO42− becomes SO₄²⁻ and NH4+ becomes NH₄⁺.
      - Otherwise, inside a formula token (starts uppercase, made only of element symbols, digits and brackets, with at least one digit), a digit after an element symbol or `)` is a subscript: CH3OH, (CH3)2NH, PbO2, H2SO4, C6H5OH.
      - `[X]0` gets a subscript 0, and `t1/2` becomes t₁/₂.
    - Never touch plain numbers ("Table 2.4", "Unit 4", "p. 52", "step 1", "373 K").
    - The quote's stored text is unchanged: this is display only.

### R4-home (Sonnet)
- **Worktree / branch:** `wt-1101-r2-explore` / `web/1101-r4-home`
- **Owns:**
  - `src/components/learn2/home/**`
  - the app shell (`AppLayoutClient.jsx`, sidebar, dock)
- **Fixes:**
  - **ui-correctness#1 (blocker) and first-timer#1 (high):**
    - Free roadmap rows show the chapter's real size from `row.cards`, never the free count: "45 cards · 10 questions".
    - Free progress reads against the real total: "5 of 45 cards seen".
    - The roadmap header reads "5 Key cards free in each chapter".
    - Add a copy test that a Free row's card count equals the chapter total.
  - **owner-eye#4 and first-timer#8 (high):**
    - The Part 2 option pills get a visible checked style (`aria-checked` is already there).
    - Until a choice is saved, add one line: "Showing Analysis of Financial Statements until you pick." The option name comes from data, not a literal.
  - **V:** render "Needs work · from your papers" when `needsWorkFrom === 'papers'`.
  - **Lows, do them all:**
    - Remove the "Start here" pill's glow at 390.
    - In SubjectPicker, use plain buttons with `aria-pressed` in a list, with no radiogroup on the listitems.
    - Define `--lh-ease` for the portalled sheet, so the scrim fades.

### R4-today (Sonnet)
- **Worktree / branch:** `wt-1101-r2-speed` / `web/1101-r4-today`
- **Owns:**
  - Today's components, `useToday`, `src/lib/today/**`
  - the Today preview fixtures (`src/app/preview/arena/previewFirstWeek.js` and Today's fixture lines)
  - the home hero's bubble CSS in `src/components/landing/**` (one item)
- **Fixes:**
  - **owner-eye#5 and first-timer#3 (high):**
    - TodayCue never draws over content: add the swap row to `KEEP_CLEAR`, or anchor the cue below the start card.
    - Reword the coach line "Tap one to swap it in as your move" to "Or start with one of these".
  - **client-code#2 (medium):**
    - Today does not shift on load: gate the header colleges strip on `everSessions !== null && !dayOne`.
    - Mount one strip, placed with CSS, never two copies.
  - **ui-correctness#8 (medium):**
    - Weak chapters reads "6 of 10 wrong or blank", never "missed".
    - Last paper reads "5 of the 20 questions you lost (4 wrong, 1 blank)".
    - Canonical titles: "Accounting Ratios", not "Ratios". Fix the source: the fixture, or `chapterTitle`.
  - **Lows, do them:**
    - For a student with no history, today shows as the planned first day (an empty ring), never the rest-day dot (ui-correctness#15).
    - "This week" header with the count "4 study days" (first-timer#15).
  - **Hero:** re-anchor the phone speech bubble's tail so it points at Mobi's head (owner-eye#1 residue). CSS only, and the heroTaps tests stay green.

### R4-explore (Sonnet)
- **Worktree / branch:** `wt-1101-r2-hero` / `web/1101-r4-explore`
- **Owns:**
  - `src/components/learn2/chapter/**`
  - Explore's covers (`feed/ExploreCovers.jsx`, `coverModel.js`, `covers.css`)
  - `DiscoveryFeed.jsx`, `exploreModel.mjs`
  - the Saved page
  - the Practice dashboard (`DashboardPageClient.jsx`, `practice.css`)
  - `src/app/preview/arena/previewFixtures.js`
- **Fixes:**
  - **ui-correctness#2 (high):**
    - Practice's chapter count and picker ("all 5 chapters") and the Your papers chapter name ("Partnership Fundamentals") must agree with Learn: 14 playable chapters with canonical titles.
    - Find where Practice gets its chapter list (likely the static `data/subjects.js`).
    - Map it onto the syllabus chapters, keeping the stored names for the question query.
    - If it is only a preview-fixture artifact, fix the fixture and say so.
  - **owner-eye#7 (medium) and ui-correctness#17 (low):**
    - Remove the dead band before "Your papers": reserve the sticky bar's height only at the true end of the scroll area.
    - Fix the summary card's square bottom corners.
    - On Free, keep one Pro mention, not two.
    - Pro never draws the Cost row or the bar's cost slot, not even while loading (client-code#9).
  - **owner-eye#10 (medium), Explore covers:**
    - The cover line is never a cloze or blank card: pick the first short non-cloze front.
    - Tighten the empty middle.
    - The cover's label is `chapterShort(place)`.
  - **owner-eye#11 and first-timer#16 (medium), Saved:**
    - Tapping the question row opens it.
    - Each item keeps one quiet "Remove".
    - "Practise this chapter" shows once per chapter group, not per item.
  - **client-code#3 (medium):** Explore singles keep a stable order once shown (remember the shown ids). New questions only append.
  - **client-code#8 (low):** reset the top-up counter when the subject, chapter or difficulty changes.
  - **owner-eye#9 (medium, chapter page):** the mistakes pile's number and the "Fix N open mistakes" line agree, or the pile says "2 fit in 10 min".
  - **ui-correctness#19 (low):** "Lesson · 7 min, not read yet".
  - **N:** the chapter page's ref line becomes `chapterPlace(place)`.
  - **ui-correctness#4, first-timer#10, owner-eye#12:** the preview fixture tags the goodwill question ("Goodwill brought in by an incoming partner…") to its true chapter.

## 2. How every packet works
- **Read first:**
  - AGENTS.md, then `node_modules/next/dist/docs/` before writing Next code
  - DESIGN.md
  - the owner's UI standards at `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`
  - this file
  - your findings in `R3-REVIEW-FINDINGS.md`
  - the shots they cite, in `tmp/learn-1101/r3-merged/` of `wt-1031-learn-v2`
- **Tests:**
  - Keep the suites green and extend them: `test:learn`, `test:keycards`, `test:today`, `test:app`, `test:auth`, `test:egress`, `test:dock` and lint, whichever touch your files.
  - Write a unit test for every new pure rule, and pin every exact string you add.
  - Read the fail count before you commit. Never commit on a red suite.
- **Look (RAM rule):**
  - At most 2 dev servers on this PC. Take a slot with `mkdir "C:\Users\atish\Desktop\mockmob copy\tmp-devslots\slot-1"` (or slot-2). If both exist, wait 60 s and retry.
  - Run `npx next dev --webpack -p <port>`. Ports: server 3481, run 3482, home 3483, today 3484, explore 3485.
  - Hold the global browser lock (`mkdir "C:\Users\atish\Desktop\mockmob copy\tmp-devslots\browser.lock"`; it is stale after 10 minutes) around every headless browser run.
  - Capture your surfaces at 390x844 and 1440x900, Night and Day, into `tmp/learn-1101/r4-after/<packet>/`. Base the capture on `scripts/design-audit/learn-1101-r3-merged-capture.mjs`, which is in the worktree from the `web/1101-r3-look` branch; copy it if it is missing.
  - Open every shot and look. Fix and capture again: at most 2 rounds.
  - Stop the server and remove the slot and the lock when done.
  - R4-server has no screens of its own: prove its changes with route tests, not shots.
- **Finish:**
  - Commit on your branch.
  - Kill every process you started (track the PIDs; never kill others).
  - Return per finding ID what changed (file:line), the test counts, the shot folder, and anything left with the reason.
- **Never** push, deploy, sign in to production, or write to a database.
