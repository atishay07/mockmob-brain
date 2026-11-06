# R7 packet W: the phone website as the full product, and recommendations that read as one module (LK62, LK59, LK48, LK56, LK57)

3 Nov 2026, evening. Branch `web/1103-webfull` (worktree wt-1103-webfull, on web/1103-proto: live main, the new cards, the new top bar).
Prototype only: nothing pushed, merged or deployed; no production read or write.

His words (3 Nov, about 3:15 pm): "you have added some intelligent recommendation. But it's making the overall UI very much more
cluttered. Not exactly cluttered, I would say, but the implementation in the UI is just not good." And: "The mobile UI of the website is
now somewhat an exact copy of the app, but the website has more features and needs to be a full-fledged experience ... especially the Learn
thing, which I said is not visible in this specific version that you have sent me." Earlier (2 Nov, LK48): "many options now are hidden or
you are unable to access them. Let me just confirm if that's the case or not."

## 1. How it was measured

`scripts/design-audit/learn-r7-w-webfull-audit.mjs` against this branch's dev server (Learn v2 on, as production; preview with the real
decks, Pro, the Commerce student, Accountancy). Eight signed-in pages (Learn home, Find, a chapter, its Cards view, Explore, Practice, Today,
Your papers) at 390 x 844 and 1440 x 900, Night and Day: a first-screen shot of each, a full page at 390, and a census of every visible link
and button (where it sits, whether it is on the first screen) plus every line that recommends something (its words, size and colour).
Shots: `tmp/learn-1103/r7-w/before/` and `after/` (not committed; the script re-makes them).

## 2. Findings with numbers

### 2a. The phone hides the website's own tools (LK48: yes, partly)

| Web feature | 1440 | 390 (phone) |
|---|---|---|
| Find's field | first screen | first screen |
| Find's four sets: Due today (9), Missed lately (6), In Revise (26), Must-know lines (236 cards) | no way in from Learn home | no way in from Learn home |
| Cards view of a chapter | chapter page, first row of "Everything in this chapter" | same, one tap from the chapter |
| Print sheet | chapter page, last shelf row | same; on the first screen its top (y 769) sits under the dock (y 768) |
| Roadmap sort, part choice | first screen / in the roadmap | in the roadmap |
| Subjects | four at once, with counts | one picker row and a sheet (one more tap) |
| Explore single questions and filters | first screen | under the covers, below the first screen |
| Saved | sidebar row | only "Saved 2" in Explore's head |
| Wallet, Colleges, Ask Mobi, Progress, Marks trend, Guide | 19 sidebar rows, always in view | behind You (two taps); Wallet also on the credits pill |

- Three of Learn's four sets (Missed lately, In Revise, Must-know lines) had no entry on Learn home at any width. They opened only from
  Find with nothing typed (`/learn/find`), and no button anywhere led there (0 links in the census). Due today was reachable only as the
  offer's "Revise 9 due cards" row. These sets are web-only: the app has none of them.
- The phone shell holds 26 links it does not show on a page (13 on the desktop): the app's five-place dock was copied as is.
- Learn home on the phone was 2.6 screens long with 9 controls on its first screen (19 at 1440).
- The prototype he opened (port 3463) could not reach Learn at all: in the dev preview the shell's own tabs dropped `decks=real`, the
  student and the subject, and its Learn tab went to the old Learn v1 preview (`/preview/study`). Explore opened from those tabs without
  the real decks, so its covers failed: "Chapter feeds did not load." (LK56, LK57). A preview fault, not the live site's.

### 2b. The recommendations: five surfaces, four looks, five phrasings (LK59)

| Where | What it says (preview data) | How it looks |
|---|---|---|
| Learn home, offer | "Pick up Admission of a Partner", "6 of 16 done", Continue · 5 min | 28 px title, volt key; no reason given |
| Learn home, Or rows | "Revise 9 due cards · 2 min"; "Fix 3 open mistakes · 3 min" + chapter name | full-width list rows with chevrons: the same anatomy as the roadmap rows below |
| Learn roadmap rows | "Needs work · from your papers" (2 rows); "Up next" (1 row) | 13 px amber text; a volt-filled chip (a second volt on the screen) |
| Explore covers | "For you: 3 open mistakes to fix"; "Needs work" x2; "2 open mistakes to fix"; "New to you" x3 | volt "For you:" prefix; one line on each of 7 covers |
| Today, Up next card | "Revise what came back", "5 mistakes due back today", a two-sentence reason, "Why this?", two other moves marked Suggested | the lit next-step card |
| Practice, Your papers | "2 questions to repair in Accountancy", "Ask Mobi what to practise", a record line | a card with two keys |

- Learn home's first phone screen carried 3 next steps at near-equal weight (the key and two rows that looked like the roadmap's rows), and
  below them 2 amber verdicts and a volt chip: 6 recommendation marks in 4 different looks, and 2 volts where the page has one.
- The same mistakes were named five ways: "Fix 3 open mistakes" (Learn), "3 open mistakes to fix" (Explore), "2 questions to repair"
  (Practice), "5 mistakes due back today" and "37 open mistakes" (Today), "Fix 2 open mistakes" (a chapter page). The counts differ because
  they count different things (a subject, a chapter, what is due today; the preview also mixes fixture sources), and no line says which.
- The server's pick had three names: "For you" (Explore), "Up next" (Today, the roadmap chip), "Suggested" (Today's footer).
- Today's card says why; Learn's offer did not. Two voices for one job.

Why it reads badly, in short: no single place (three peers at one weight), colour used to shout (amber and a second volt), the same
"· from your papers" repeated on every weak row, and different words and numbers for the same thing.

## 3. The plan

### 3a. Recommendations: one module, one voice, one place per page
- **Up next** is the one module, with Today's anatomy (owner-approved D1 to D3): ONE move on the card at a time (its headline, one line
  saying why, its length, the page's one volt key), the other moves as short cells in its footer; a tap makes that one the move, and the
  server's pick waits in the footer marked "Suggested". A cell never starts anything; only the key does.
- One word for the pick everywhere: **Suggested** (Today's footer, Learn's footer, the lead Explore cover).
- Lists say state, never advice: a roadmap row says "Needs work" with its ring in ink; where it comes from is said once, under the head.
  "Up next" on a row is a quiet outlined tag; the volt belongs to the key.
- Next, not built here: Practice's "Your papers" card and the chapter page's mistakes row take the same word and the same count rule; one
  definition of "open mistakes" across Today, Learn and Practice, each line saying its scope ("in Accountancy", "in this chapter"). This
  needs the server's counts lined up and the English pass (packet E), so it waits for them.

### 3b. The phone website as the full product
- Learn home shows the web's own tools on the phone: Find's sets as keys under the field (two to a row on a phone, one row of four on a
  computer); a tap opens the set in place with its cards and its Study key, as from Find.
- Up next uses the wide screen: the move on the left, the other moves beside it, so Learn's first screen on a laptop holds the move, the
  field, the four sets and the roadmap's head.
- The preview's own tabs keep the settings the page was opened with, and its Learn opens Learn v2, so a phone walk never loses Learn or
  Explore's covers.
- Next, not built here (for his call): the Print sheet and Cards view as keys in the chapter head on the phone (they are the last shelf rows
  now); Saved and Ask Mobi as rows on Learn home's foot on the phone (they are in Explore's head and behind You). Refine, not rebuild: the
  dock, the four tabs (LK46) and the subject sheet (R3 ruling R1) stay.

### Two earlier rulings this changes (his call on the live look)
1. R4 removed the row of keys under the Find field ("no status line under the search"). The sets come back here, as keys that open the
   sets, not as a status line, because without them three web-only sets had no way in.
2. R2 ruling 1 drew the offer as type on the page, not a card. Up next now wears Today's next-step card (its volt line, no glow), so the
   product recommends in one look.

## 4. What was built (commits on web/1103-webfull)
- `RoadmapHero.jsx` is the Up next module; `upNextMoves` and `otherMoves` (homeModel.mjs) build its moves from the server's roadmap, with no
  new numbers. The offer's length (LK37), the pending key, Free's See Pro and the quiet link are kept.
- `ChapterMap.jsx`: "Needs work" plus its ring on the row, one line under the head saying where it comes from (from the papers, or from
  both), the full words kept in the row's spoken name; the "Up next" tag outlined.
- `CardSets.jsx` on Learn home under the field.
- `coverModel.js`: the lead cover says "Suggested:" where it said "For you:".
- `ArenaPreviewClient.jsx`: the shell's links carry decks, student, subject and the session key; Learn opens Learn v2 when Learn v2 is on.
- Tests: `r7Webfull.test.mjs` (8), the cover and offer-length pins updated; the audit script.
