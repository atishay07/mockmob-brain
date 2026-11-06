# Learn v2 round 2: phone clarity (390 wide), first-timer and returning student

Lens: the phone website at 390 px, as a 16-year-old opening Learn for the first time and as a returning student. Owner items: LK24 clutter, LK26 the top tabs, LK27 the Learn landing must lead with a start offer, LK29 first-time cues, LK30 blank space, LK31 end screens. Evidence: `tmp/learn-1101/r2-before/` (390 shots; "night"/"day" as in INDEX.md). Read-only review: nothing in the code was changed.

## The Learn landing on a phone: proposed structure

Today (83, 86-full, 87, 88-full) the phone shows, before any action: the tab row (scrolls, cut "E›"), a 155 px subject rail of 3D objects, a search field, then either a row of three number keys ("9 due today / 6 missed lately / 26 in Revise", which reads "0 due today / 0 missed lately / N in Revise" for a student with nothing due: that is the owner's "0 in, revise 0") or the line "Nothing in Revise yet. Cards you study land here.", and only then the start card at y ≈ 430 CSS px. Then a second full card ("Find your level") with its own big key, a third card (the feed), the chapter list with two levels of headings and five status words, a "Your part" chooser in the middle of the list, and two footer links.

**New order, top to bottom (one screen at 390x844 holds 1-3 entirely):**

1. **Tab row** (44 px, no scroll; item 3).
2. **Subject row, compact** (84 px tall, was 155): object 44 px, name 13 px/600 under it, 4 subjects visible, a 24 px edge fade instead of a cut word; the chosen subject has the lime 3 px bar. No "9 due" under each subject (one due number lives in the hero only).
3. **The offer (hero), one per state.** One title, one line, one lime key, one quiet text key. No container card on the phone: it sits on the page, 20 px top padding, so it reads as the page's headline, not one card among three.
   - **First time in this subject:** title `Start learning Accountancy` (28/32, 700). Line `Begin with Chapter 1, Accounting for Partnership: Basic Concepts. Key cards, then questions.` Key `Start 10 minutes`. Text key under it: `Pick another chapter` (scrolls to the roadmap, 320 ms ease-out).
   - **Unfinished run:** title `Pick up Admission of a Partner`. Line `6 of 16 done. About 5 min left.` The 4 px progress track. Key `Pick up, 5 min`.
   - **Cards due, nothing unfinished:** title `9 cards are due in Accountancy`. Line `About 2 min, from 3 chapters.` Key `Revise 9 cards`.
   - **Nothing due, nothing unfinished:** title `Next up: Goodwill: Nature and Valuation`. Line `Chapter 4 on your roadmap. 10 minutes of Key cards and questions.` Key `Start 10 minutes`.
   The engine already ranks these (Suggestions, `data.suggestions[0]`); only the drawing changes.
4. **"Or" rows** (the other two suggestions), max 2, each one 56 px row on a hairline, no card, no button: title 15/600 + one 13 px line + chevron. Examples: `Find your level` / `6 questions, about 6 min`; `Swipe through a chapter` / `The Explore feed, 10 min`; `Fix 3 mistakes from Mock 3` / `About 3 min`. This is where "Find your level" moves (it is a full second card with a second big key today, 87).
5. **Search**, 48 px, placeholder `Find a topic, like goodwill` (not "Search 868 Key cards": the number means nothing to a first-timer). Under it, only the shelves that are not zero, as one line of text keys: `9 due` · `6 missed` · `26 in Revise`. If all are zero, draw nothing at all (drop "Nothing in Revise yet..."; Revise is taught at the end of the first run, item 12).
6. **Your roadmap** (item 6): heading `Your roadmap` (20/700), right side the existing `Book order` sort. Line under it only when true: `2 of 15 chapters started`. Then the chapters as a path.
7. **Moves away:** the footer links `Study plan` and `Your record` (both already live in Today and You: moved, not removed); the unit sub-headings in the list; the mid-list "Your part" chooser (item 9); the zero line.

---

## Ranked findings

### 1. Learn home leads with zeros and a search box, not with an offer (LK27)
- **Wrong:** 87 (fresh Free, no subject) and 92 put `Nothing in Revise yet. Cards you study land here.` above the start card; 83/88 put a search field and three number keys above it. A student with nothing due sees `0 due today` and `0 missed lately` drawn as keys (ShelfKeys draws zeros "quiet", homeModel `zero: true`): the owner's "0 in, revise 0". The start offer starts at about 430 CSS px.
- **Why:** the first thing a 16-year-old reads is an empty state about a feature they have never heard of. Product rule: never lead with a line of zeros. LK27 asks for "Start learning <subject>" / "Your roadmap" first.
- **Fix:** the order above. ShelfKeys: return only keys with `count > 0`, drawn as text keys (14/600, 44 px tall hit area) under the search, never above the hero; the all-zero sentence is deleted. The hero is the first block after the subject row (top at about 190 CSS px on a 390x844 phone, fully in the first screen with its key).
- **Files:** `src/components/learn2/home/LearnHome.jsx` (block order, lines ~276-313), `home/ShelfKeys.jsx`, `home/homeModel.mjs` (`shelfKeys` filters zeros), `home/Suggestions.jsx`, `home/learn-home.css`, `src/lib/server/learn.js` (suggestion titles: "Start learning <subject>").

### 2. The Explore feed gives no sign that it moves by swiping (LK29)
- **Wrong:** 91-first-item and 91-after-4s: a card sits in the middle with about 130 CSS px of empty space above and 190 below; nothing on screen says "swipe up". The current cue (ChapterFeed.jsx ~264) is a 24 px, 360 ms bounce of the track, once, 700 ms after the first turn, and only on touch: easy to miss, and the next item is not on screen, so the bounce shows nothing.
- **Why:** the owner found the swipe himself only by accident. A first-timer taps "Turn over", then "Next", and never learns the story-like gesture that makes the feed feel like the feature.
- **Fix (three parts, all first feed only, flag `learn2.feed.nudge.v2`):**
  1. **Peek:** each item's height is the stage height minus 56 px, so the top 56 px of the next item shows under the current one: its kind label (`Question` / `Key card`) and the top edge of its card, at 60% opacity. This also takes up the empty space (item 8).
  2. **Lift:** 600 ms after the first item settles (not after the turn), the track lifts 96 px and settles back: 420 ms up with `cubic-bezier(.2,.8,.2,1)`, 380 ms back with a light overshoot (spring stiffness 260, damping 22). Twice, 1.6 s apart. The next card is visibly there.
  3. **Chip:** a pill 36 px tall, centred 12 px above the action bar: Mobi's head (20 px) + `Swipe up for the next one` + an up-chevron that rises 6 px and returns, 1200 ms ease-in-out, looping until the first swipe. It fades out (180 ms) on the first successful swipe, or after the third item, and never shows again.
  The Next key stays, so tapping still works. Reduced motion: no lift, no loop; the peek and the chip stay.
- **Files:** `src/components/learn2/feed/ChapterFeed.jsx` (hints, the effect at ~190 and ~264), `stage/usePager.js` (item height minus peek), `stage/Stage.jsx` (ActionBar `hint` becomes the chip), `stage/stage.css`.

### 3. The Practice tab row scrolls sideways and hides Explore (LK26)
- **Wrong:** 80, 83, 87, 89, 92: five tabs (Practice, Learn, Your papers + "8 to revise", Explore, Saved) do not fit; the scroll chevron sits on top of the fourth tab (`E›`), and on Explore and Saved (81, 82) the row is scrolled so "Learn" is cut to "earn"/"n". Saved is a tiny utility at the same rank as Learn.
- **Why:** a first-timer sees three "ways to study" (Practice, Learn, Explore) plus two lists, half of them off screen. Hidden tabs are features they will never find (audience rule: never hide features).
- **Fix:** four equal tabs that always fit, no scroll, no chevron: `Practice` · `Learn` · `Explore` · `Papers` (each 89 px at 390 minus the 16 px gutters, 15/600, 44 px tall, the lime 3 px bar under the current one). "8 to revise" becomes a 6 px lime dot on Papers (the number is on the Papers page). **Saved moves into Explore** as a text key at the right of Explore's header: `Saved 2` (saved items come from Explore; moved, not removed). Saved keeps its address; the tab row marks Explore while on it.
- **Files:** `src/lib/arenaNavigation.js` (`practicePages`, `placeTabs`), `src/components/nav/PlaceTabs.jsx` (equal-width row, drop the scroll key), the Explore head in `src/components/feed/DiscoveryFeed.jsx`.

### 4. Two big start cards compete on the fresh Learn home (LK24, LK11)
- **Wrong:** 87/86-full: `Start with Accounting for Partnership...` (lime key) and `Find your level` (a second full card with a second big outlined key, cut by the dock), then a third card for the feed. Three stacked rounded cards, each with a title, a sentence and a key.
- **Why:** the owner wants one straight thing to do, with options, not three equal walls. Stacked cards are what reads as clutter at 390.
- **Fix:** the hero (structure point 3) plus "Or" rows (point 4): one lime key on the page; the rest are 56 px rows with a chevron. No card containers on the phone (`.lh-sug` loses background, border and 24 px padding below 600 px; the rows get a 1 px hairline).
- **Files:** `home/Suggestions.jsx`, `home/learn-home.css`.

### 5. Explore is two pages stacked: covers, then the old question list (LK24)
- **Wrong:** 90-full / 81-full (7,410 px tall): headline `One question. One useful step.` + a sentence + a Subject select + `Chapter feeds` + a 5/10/20 switch + the covers; then `Questions`, two filters, 12 full question cards with all four options open, `Load more questions`, `Answer first. Then ask why.`, `Open saved questions`, `Review your timed sessions`, `7 questions solved in your recorded untimed practice`, `See progress`.
- **Why:** the covers are the standout feature the owner loves (LK21, LK18), and they are buried under a slogan; below them a first-timer scrolls through a wall of identical-looking question cards.
- **Fix:** header becomes one line: `Explore` is already the tab, so the h1 goes; the subject is a 36 px chip `Accountancy ▾` at the left and `Saved 2` at the right on the same row. The 5/10/20 switch shrinks to a 32 px segmented control on the same line as `Chapter feeds` (as now) but the covers start at y ≈ 150 CSS px. Below the covers: `Single questions` (20/700) with 3 question cards collapsed to the stem only (tap opens the options), then `More questions` (a quiet key). Delete the slogan, the "Answer first..." block and the closing record line (the record lives in You > Progress).
- **Files:** `src/components/feed/DiscoveryFeed.jsx`, `src/app/(app)/explore/explore.css`, `src/components/learn2/feed/ExploreCovers.jsx`, `feed/covers.css`.

### 6. The chapter list is a dense table, not a roadmap (LK27 "Your roadmap", LK24)
- **Wrong:** 88-full: two heading levels (Part, then unit in grey), each row = title + "46 cards" + a status word + "Ch 1, 3 due, 3 open mistakes". Five status words a teen cannot tell apart: `Getting there`, `Too few answers`, `Needs work`, `Holding`, `Not started`. 86-full: `All 15 chapters are new to you.`
- **Why:** this is where "Your roadmap" belongs, and it should read as a path with a "you are here", not a ledger.
- **Fix:** heading `Your roadmap`. Each row (60 px): a 28 px node on a 2 px vertical rail at the left with the chapter number inside; title 16/600; one meta line 13 px. Node states: hollow = not started (meta: `46 cards`); half-lime = started (meta: `Started · 3 due`); amber ring = `Needs work · 2 mistakes open`; full lime = `Going well`. "Too few answers" and "Holding" go. The next chapter to do gets a lime pill `Start here` (first-timer: Ch 1) or `Up next`. Unit sub-headings go on the phone; Part headings stay (17/700). Delete `All 15 chapters are new to you.` `Computerised Accounting System` with nothing to practise: greyed, no chevron, meta `Coming soon`.
- **Files:** `home/ChapterMap.jsx`, `home/homeModel.mjs` (status words), `home/learn-home.css`. Never "mastered" (Going well is the top word).

### 7. End screens are walls of lines (LK31)
- **Wrong:** 18 (feed end): title 40 px + `All 17 done in 1 min.` + the card fan + `3 kept` + `They are first in Revise.` + a 3-row ruled table + two buttons + a link. 95 (Free): `Nothing kept this time. Keep a card and it comes back in Revise.` + table with `0 kept` + a two-sentence Free paragraph + `See Pro` + button + link. 55 (run end): Mobi + title + fan + `16 in Revise / 14 back Wed, 2 back in 20 days` + table + `Next:` block + `Start 10 minutes` + `Another 5 minutes here` + `Fix 2 open mistakes` (runs off screen).
- **Why:** after a good 10 minutes the student gets a report. The owner: "too many lines and walls of text".
- **Fix (feed and run share it):** Mobi 56 px top-left does a 500 ms nod; title is the chapter (17/600, grey); headline `17 done in 1 min` (32/700). One row of three stats, no rules, each 2 lines (number 22/700, label 13): `12` `cards`, `3 of 3` `right`, `1` `mistake fixed`. Drop any stat that is zero (no "0 kept", no "Nothing kept this time"). The fan only when something was kept, with one line under it: `3 kept for Revise`. Then one lime key and one quiet key, and nothing else: run end `Next chapter, 10 min` (the chapter name as the line above the key, 15/600, one line with ellipsis) + `Another 5 minutes here`; feed end the same with `Back to Explore` as a text link. "Fix 2 open mistakes" moves to the Learn hero's "Or" rows. The "14 back Wed, 2 back in 20 days" line goes (it is in Revise).
- **Files:** `src/components/learn2/stage/EndForm.jsx`, `run/RunEnd.jsx`, `feed/ChapterFeed.jsx` (end branch), `stage/stage.css`, `run/run.css`.

### 8. The feed and the run float a small card in a big empty stage (LK30)
- **Wrong:** 91-first-item / 10: the card is about 380 CSS px tall in a 640 px stage; 130 px of nothing above it, 190 below. 11 (turned): same frame, NCERT's line in 26 px serif with 120 px of empty card under it.
- **Why:** the owner's "too much blank space"; on a phone, empty bands read as unfinished.
- **Fix:** with the 56 px peek (item 2) the card takes the stage from 16 px under the top bar to 16 px above the peek (min 70% of the stage). Front text stays 34/1.12 but is vertically placed at 38% (optical centre), not 50%. The source line (`Accountancy Part 1, Ch 2, p. 52`) stays pinned at the card's foot. On the turned side the card does not resize (no jump).
- **Files:** `stage/stage.css`, `stage/CardFace.jsx`, `stage/usePager.js`.

### 9. "Your part" asks a hard question in the middle of the list (LK24, LK2)
- **Wrong:** 86-full/88-full: between Part 2 chapters, a segmented control `Analysis of Financial Statements 5 chapters | Computerised Accounting 1 chapter` and `Both parts show until you choose.`
- **Why:** a first-timer does not know which their school teaches and meets the question mid-scroll, unexplained.
- **Fix:** move it to sit directly under the `Part 2` heading, as one line: `Your school teaches` + the two choices as 32 px chips (`Analysis` / `Computerised`). Delete the hint line; when nothing is chosen, both show (that is already the behaviour, it needs no sentence).
- **Files:** `home/ChapterMap.jsx` (~135-160), `home/learn-home.css`.

### 10. Two names for one action: "Keep" on cards, "Save" on questions (first-timer cue)
- **Wrong:** 91/10: the left key on a card is `Keep`; 13: on a question it is `Save`. Kept cards go to "Revise"; saved questions go to "Saved".
- **Why:** a teen cannot tell why the same left key has two names and two destinations.
- **Fix:** both say `Keep` with the same bookmark glyph; a kept question goes to Revise as a question (or, if the model must keep Saved, the key says `Keep` and the toast says `Kept. Find it in Saved.`). On the first Keep ever, a 2.4 s toast above the bar: `Kept. It comes back in Revise.` That replaces the end screen's teaching sentence.
- **Files:** `feed/ChapterFeed.jsx`, `stage/Stage.jsx`, `stage/Question.jsx`.

### 11. Two counters on a feed question (first-timer cue)
- **Wrong:** 13: `Question 1 of 3` above the stem and `5 of 16 ⌄` in the top bar, plus the 16-segment story bar.
- **Why:** three progress signals; "1 of 3" and "5 of 16" contradict each other at a glance.
- **Fix:** keep the story bar and the top-bar `5 of 16`; replace `Question 1 of 3` with the kind label used on cards: `Question` (13/500 grey, like `Definition` on cards).
- **Files:** `stage/Question.jsx`, `feed/ChapterFeed.jsx`.

### 12. Free end offers "Next chapter" that the Free plan will refuse
- **Wrong:** 95: after `Your free Learn session for today is done...`, the outlined key is `Next chapter: Retirement and Death of a Partner`; 21 shows that starting a feed on Free after the session is used is refused.
- **Why:** the only big key leads to a refusal: a dead end for the student most likely to churn.
- **Fix:** Free end, session used: line (one sentence) `That was today's free session.` + text link `See Pro`. Lime key `Answer single questions` (free, unlimited: goes to Explore's Single questions). Quiet key `Back to Explore`. No next-chapter key until tomorrow.
- **Files:** `feed/ChapterFeed.jsx` (~490-500), `run/RunEnd.jsx`, `stage/EndForm.jsx`.

### 13. "Due" means two things on one screen
- **Wrong:** 83/88: the dock's Practice badge says `8 due`, Your papers says `8 to revise`, the subject rail says `9 due` (Accountancy), `6 due` (others), the keys say `9 due today`.
- **Why:** a teen reads "8 due" and "9 due" as the same thing that does not add up.
- **Fix:** the dock badge becomes a 8 px lime dot (no word). The subject rail drops its due numbers (structure point 2). "Due" is used for Key cards only, in the hero and the Revise text keys.
- **Files:** the dock in `src/app/(app)/AppLayoutClient.jsx` (badge), `home/SubjectShelf.jsx`.

### 14. Practice page: four "Included" badges and a second Learn door (LK24)
- **Wrong:** 80-full: `Unlimited` pill + `Quick practice and Full mock are included with your access.` at the top and `Your access ... Unlimited` at the bottom; every mode card says `Included`; `Fine-tune` appears twice (a strip and a block); a `Learn` block (`Short lessons on the ideas behind your mistakes`, `All lessons`) sits on Practice while Learn is the next tab.
- **Why:** the first screen a student lands on in Practice is mostly plan copy; the old Learn block points at a different "Learn" from the tab.
- **Fix:** Pro: no `Included` badges, no top pill or sentence (access stays in the bottom block). Free: a 16 px lock only on what is locked. One `Fine-tune` (the block; the strip goes). The old Learn block becomes one row in Learn's "Or" rows when a lesson is due (`Revaluation of assets and liabilities, 7 min`); it leaves Practice (moved, not removed).
- **Files:** `src/app/(app)/dashboard/DashboardPageClient.jsx`.

### 15. The subject rail is 155 px of objects before anything happens (LK30)
- **Wrong:** 83/87/92: the rail of 3D objects (about 70 px object + 2-line names + a due line + the bar) takes 155 CSS px; `English` is cut at the edge; the same rail appears again on Practice (80) at 190 px.
- **Why:** on the first screen it pushes the offer below the middle; the cut word looks broken.
- **Fix:** structure point 2: 84 px, 44 px objects, one-line names (13/600, ellipsis), a 24 px fade mask at the right edge instead of a cut word. Selecting a subject: the object scales 1.0 to 1.08 and back (220 ms, ease-out) and the hero text cross-fades (160 ms).
- **Files:** `home/SubjectShelf.jsx`, `home/learn-home.css`.

### 16. The chapter page ends in a zero line and keeps the first-timer guessing (LK27)
- **Wrong:** 89-fresh-full: status `Not started` beside the title; `Tap a pile to leave it out.`; the long underlined `Or a quick recap: the 5 Must-know lines, about 1 min` wraps to two lines; the page ends `No lesson yet. No open mistakes.`
- **Why:** a zero sentence as the last thing read; the recap link reads like body text.
- **Fix:** drop `Not started` for a fresh chapter (show a status only once started). Delete the last line. The recap becomes a 48 px quiet key under the lime key: `Quick recap, 1 min`. `Tap a pile to leave it out.` becomes 13 px grey only on the first chapter page ever (flag), then gone. `Your own` becomes `Other`.
- **Files:** `src/components/learn2/chapter/ChapterPage.jsx`, `chapter/chapter.css`, `chapter/chapterModel.mjs`.

### 17. First-time cues missing elsewhere (LK29: every place a first-timer gets stuck)
| Where | Stuck on | Cue (once, flag per cue) |
|---|---|---|
| Feed card front (91) | that the card turns | The card tilts 4° on Y and back, 600 ms, 1.2 s after it lands; `Turn over` stays the key. |
| Feed: Keep (91) | what Keep does | First Keep: toast `Kept. It comes back in Revise.` 2.4 s (item 10). |
| Feed: Chapter key (91) | what the book icon opens | Its label already says `Chapter`; on first open the panel title is `Accountancy Part 1, Ch 2` so it is clearly the book. No extra cue. |
| Run: the four rating keys (51) | what they mean | On the first revealed card only, one 13 px line above them: `How well did you know it? This sets when it comes back.` Gone after the first rating. |
| Explore covers (90) | that covers page sideways | The second cover's 32 px peek exists; add a 1 s, 24 px nudge of the row to the left and back on first visit (420 ms out, 380 ms back), reduced motion: none. |
| Chapter page piles (89) | that piles toggle | The 13 px line on the first chapter page only (item 16). |
| Learn home roadmap | where to begin | `Start here` pill on Ch 1 (item 6). |
| Saved (82) | swipe left/right on a question | The sentence `Swipe a question left to remove it...` goes; the first row slides 40 px left showing a red `Remove` edge, then back (500 ms), once. |
- **Files:** `feed/ChapterFeed.jsx`, `stage/CardFace.jsx`, `run/RunParts.jsx`, `feed/ExploreCovers.jsx`, `chapter/ChapterPage.jsx`, the Saved page component, one shared `firstTime(flag)` helper next to `seenFlag`/`markFlag`.

### 18. Explore cover copy "For you:" / "Start here:" is fine; "5 Key cards, 7 questions" is not a promise (small)
- **Wrong:** 90: `5 Key cards, 7 questions` above `Play 10 minutes`; a first-timer does not know what a Key card is.
- **Fix:** `Cards and questions, 10 min` on the first visit (Key cards are named once they have seen one); returning students keep the counts.
- **Files:** `feed/ExploreCovers.jsx`.

### 19. Today for a brand-new student shows a repair of 12 mistakes and "72 marks they cost you"
- **Wrong:** 85 (student=new, Free): `Repair your last paper`, `12 mistakes to repair`, `72 marks they cost you`, `All 12 are from your Accountancy full mock on 29 Oct`.
- **Why:** either the preview fixture ignores `student=new` on Today, or a brand-new student is shown invented history. And "marks they cost you" is the same promise as the banned "marks to recover".
- **Fix:** check the fixture first (`/preview/arena?view=today&student=new`). Copy: drop the marks line; the size line becomes `about 40 min` alone.
- **Files:** `src/lib/today/lead.mjs` (line 56), the Today preview fixture.

### 20. Feed questions: a long stem hides the options; "Options below" chip sits on the text (LK30)
- **Wrong:** 13: a match-the-column stem fills the screen; the `Options below ⌄` chip overlaps the list text.
- **Fix:** the chip moves to the action bar's centre slot in place of `Skip` until the first option is on screen (`Options below` with a down-chevron, tap scrolls 320 ms); List-I/List-II items set at 15/1.45 instead of 17/1.5 on phones below 400 px.
- **Files:** `stage/Stage.jsx` (M10 chip), `stage/Question.jsx`, `stage/stage.css`.

---

## Notes for the builder
- Every change above is on the phone breakpoint (`max-width: 599px`) unless it is copy; desktop keeps its layout unless the item says otherwise.
- Nothing is removed: Saved, Study plan, Your record, the old lessons and "Fix mistakes" move to named places.
- After building: capture 83, 86, 87, 88, 89, 90, 91 (first item, after 4 s), 18, 55, 95 again at 390 Night and Day and compare to these before-shots.
