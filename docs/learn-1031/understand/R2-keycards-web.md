# R2. Website Key cards, as built (read-only map)

Scope: `C:/Users/atish/Desktop/mockmob copy/wt-1031-keycards-web` (production main plus the Key cards build). Nothing was changed, run or committed. Paths below are relative to that worktree unless they start with a drive letter. Line numbers were read on 31 Oct 2026.

Owner feedback read first: `docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md` (items LK1 to LK14).

Screenshots looked at (all in the worktrees named in the task): `home-commerce-pro-accountancy-390-night`, `cards-home-option-1440-night`, `entry-learn-row-390/1440-night`, `deck-econ-long-read-pro-390-night`, `deck-read-free-390-night`, `deck-study-answer-390-night`, `deck-last-look-390-night`, `deck-print-sheet-1440-night`.

---

## 1. Files and what each one is

| File | Lines | Role |
|---|---|---|
| `src/app/(app)/cards/page.jsx` | 12 | Route `/cards`, wraps `KeycardsHome` in a `student-page--cards` div |
| `src/app/(app)/cards/[chapter]/page.jsx` | 15 | Route `/cards/<chapterKey>`, wraps `ChapterDeck` |
| `src/components/keycards/KeycardsHome.jsx` | 223 | Home: head, Today panel, Pro nudge, subject tabs, `OptionPicker` (the "Your part" control), chapter rows |
| `src/components/keycards/ChapterDeck.jsx` | 395 | One chapter: head, side panel, three modes (Read, Study, Last look), print sheet |
| `src/components/keycards/KeyCard.jsx` | 287 | Shared card parts: `CardHead`, `Prompt`, `NcertText`, `CardSource`, `InShort`, `CardMenu`, `ReportForm`, `ProGate`, `KeyCardPlayer` (used by Study and Revise) |
| `src/components/keycards/LineYouNeeded.jsx` | 72 | "The line you needed" under a wrong answer on the paper result (not part of Learn) |
| `src/components/keycards/KeycardsLinks.jsx` | 40 | The two ways in: `LearnKeycardsRow` (Learn hub row) and `ChapterKeycardsLink` (Review chapter) |
| `src/components/keycards/links.js` | 26 | `useCardsLinks()`: `/cards`, `/cards/<key>?mode=`, `/review/revise`; in `/preview/*` it keeps links inside the fixture preview |
| `src/components/keycards/kinds.js` | 376 | Pure copy and shapes: labels, `MODES`, `RATINGS`, `PRO_LINE`, `countsLine`, `blocksOf`, `stateCue`, `limitCopy`, `entryRows`, `formulaLines` |
| `src/components/keycards/api.js` | 84 | Fetch layer, shared home cache (`homeRead`, `refreshHome`), `useKeycardsHome` hook |
| `src/components/keycards/keycards.css` | 380 | All styling and motion for the above |
| `src/components/keycards/fixtures.js` | 385 | Dev-preview answers for the same API paths (instant, never slow) |
| `src/lib/server/keycards.js` | 506 | Server service: `overview`, `deck`, `add`, `due`, `review`, `line`, `report`, `chapters`, `putOption`, `reviseSource`, `dueCount` |
| `data/keycards.js` (repo root `data/`, not `src/data/`) | 254 | Pure rules: `KEYCARD_RULES`, `tasteIds`, `deckView`, `chapterAddSet`, `canAdd`, `dueQueue`, FSRS `schedule` |
| `src/lib/server/keycardsHttp.js` | 56 | Flag, auth, rate limit (120 a minute a user), body cap 4000 bytes, `Cache-Control: no-store` |
| `src/lib/server/keycardsSyllabus.js` | | Syllabus adapter: `subjectOptions`, `unitsFor`, `chipFor` |
| `data/cuet_syllabus.js` | | `SUBJECT_OPTIONS` (line 18), `unitsFor` (718), `sectionAllowed` (699) |
| `src/components/revise/*` | | Revise run; Key cards are the fifth source in the queue |

Routes:
- `GET /api/keycards` (home), `GET /api/keycards/deck?chapter=`, `POST /api/keycards/add`, `GET /api/keycards/due`, `POST /api/keycards/review`, `GET /api/keycards/line?questionId=`, `POST /api/keycards/report`
- `GET /api/me/chapters?subject=`, `PUT /api/me/subject-options`
- `GET /api/me/revise` (`?queue=1` adds Key cards via `keycardsService().reviseSource`)

Not found: any Key cards or card feed inside Explore (`src/app/(app)/explore`). Cards appear in Explore nowhere today (LK12 is entirely new).

---

## 2. How a student gets to Key cards today (LK1)

No tab. `AppLayoutClient.jsx:338-340` just marks Learn as the active place on `/cards*`. Phone dock is Today, Practice, Start, Mob, You. Path today:

Practice (dock) then the Learn tab in Practice's tab row, then the "Key cards" row on the Learn page, then a chapter row on `/cards`, then a mode.

On the Learn page the row is `LearnKeycardsRow` (`KeycardsLinks.jsx:13-25`), placed in `StudyLibrary.jsx:90` after the big volt "next lesson" card and the Revise rows, before the search box. It uses the Learn hub's plain `.cx-row` style (`src/components/study/concepts.css:41-46`): bold 15.5px title "Key cards", one grey 13.5px line, a chevron, a bottom hairline. Same visual weight as "Test it in a full mock". Screenshot `entry-learn-row-390-night.png`: it is easy to read as a footnote under the lesson button.

Copy: title `Key cards`; line `NCERT’s exact lines, chapter by chapter. {n} cards due today.` or, with none due, `NCERT’s exact lines, chapter by chapter, each with its page.` Hidden while loading, when off, on error.

Other entry points: `ChapterKeycardsLink` on Review chapter rows (`ChapterRows.jsx:200`, `ReviewChapters.jsx:147`): link text `Key cards for this chapter`, small line `{5 of 38 open | 18 cards, 6 due}, in NCERT’s exact words`; hidden if the chapter has no cards. "Revise now" on `/cards` goes to `/review/revise`. `LineYouNeeded` on the result page.

Learn itself (`StudyLibrary.jsx`) is a separate system: "Learn" head, "Short lessons on the ideas behind your mistakes.", one "next lesson" card, Revise rows, Key cards row, search, subject tabs (Accountancy, Business Studies, Economics, English), "Where you lose marks", "All {subject} chapters" accordions, a right column with "lessons read / cards in Revise / cards recalled". Key cards and lessons share no subject selection, no chapter list and no progress; they only share the word "Revise".

---

## 3. Home `/cards` (KeycardsHome.jsx)

### Layout top to bottom (screenshots: `home-commerce-pro-accountancy-390-night`, `cards-home-option-1440-night`)
1. Back-less page. Head: h1 `Key cards`, lede `NCERT’s exact lines, chapter by chapter, each with the page it is on.` (`:105-112`)
2. Today panel (`:174-180`): h2 `{n} cards due today` (bold number) or `Nothing due today`; line `About {m} minutes in Revise, with the rest of today’s work.` or, with none due, `Open a chapter and add it to Revise. Its cards come back there when they are due.`; the one volt key `Revise now` only when due > 0. Panel is raised and flat only when due.
3. Free only: `InlineNudge placement="keycards"` (`:181`), dismissable. Copy (`src/lib/proNudge.mjs:191`): `Pro opens every card in every chapter and keeps them on a schedule.` with `See Pro`.
4. Subject tabs (`:190-206`), shown only if more than one subject: pill buttons with a `SubjectObject` icon; scrolls sideways, selected one scrolled into view (`:134-147`). Order = `user.subjects` array order (the screenshots differ only because the fixture users differ).
5. `OptionPicker` (see section 5) for Mathematics, Computer Science, Accountancy only.
6. English only: `English cards are written for MockMob, not taken from an NCERT book.` (`:208`)
7. Units and chapter rows (`:209-218`). Rows from `blocksOf` (`kinds.js:286-290`): if every unit holds one chapter (Business Studies) one plain list with no headings; otherwise each unit is a headed group.

### Chapter row (`ChapterRow`, `:46-69`), whole row is one link
- Title (650 weight 16px). Under it `Accountancy Part 1, Ch 1` (or just `Ch 7` under a unit heading that is the book name) plus the chip (`CUET only` or `CBSE teaches this in Class 11`).
- State: a 16px pie glyph plus word from server: `Not started`, `Too few answers`, `Needs work`, `Getting there`, `Holding`, `Could not load`; `, fading` appended when fading.
- Counts: `46 cards, 3 due` (`, N due` only once the chapter has anything added or due), `No cards yet` when empty; Free adds `5 of 27 open`.
- Screen reader label joins everything with full stops (`:52`).
- Desktop 4-column grid (title, state 168px, counts 132px, chevron) from 720px; phone two lines.

Row data from `overview()` (`src/lib/server/keycards.js:266-271`): `{ key, title, ncert:{book,chapter}, chip, cards, mustKnow, unlocked, added, due, state:{state,label,fading} }`. The home body does not carry question counts or marks lost; `/api/me/chapters` does (`available:{questions,cards}`, `marksLost`, `n`, `right`, `reason`, `memory` for Pro; `chapter_state.js:115-117`).

Accountancy today (verified by running `unitsFor`): units Accounting for Partnership (2 chapters), Reconstitution of a Partnership firm (4), Dissolution of Partnership Firm (1), Company Accounts (2), then the option units: Analysis of Financial Statements (5 chapters, 364 cards) when AFS or no option; Computerised Accounting System (1 chapter, **0 cards**) when CAS or no option. So with no choice 15 chapters show; the CAS row says "No cards yet".

### Home states
| State | Copy |
|---|---|
| loading | skeleton: today block, tabs, 5 rows, `aria-label="Loading Key cards"` |
| off (flag) | h2 `Key cards are not open yet`, `They open here once the first chapters are checked against the book. Lessons and practice are all still open.` |
| error | `ErrorState` title `Key cards did not load`, `Check your connection and try again. Your cards and their schedule are safe.`, Retry |
| no subjects | `No subjects to show` / `Key cards follow the subjects you chose. Add your CUET subjects in Account and their chapters appear here.` |
| no chapters | `No chapters with cards in {subject} yet.` |

Motion on home: each `.kc-row` rises 6px and fades, 260ms, stagger 24ms by index capped at 12 (`keycards.css:111`, `--i` from `ChapterRow`). Subject tab and option button colour transitions 200ms. Row chevron nudges 2px on hover. Nothing else.

---

## 4. Chapter deck `/cards/<key>` (ChapterDeck.jsx)

Fetches `GET /api/keycards/deck?chapter=` (`useDeck`, `:25-38`) and, for Pro, `GET /api/me/chapters?subject=` for the reason line (`useReason`, `:41-55`). Mode lives in `?mode=study|last` (read = no param), written with `replaceState` (`:276-279`).

### Head (`:343-355`)
Back link `Key cards` (always to `/cards?subject=`). Optional unit line (only when it adds something), h1 chapter title, reference line `Introductory Microeconomics, Ch 2` plus chip, Pro only a reason line, e.g. `6 of 9 right on the latest try at each question. Cards: 6 of 91 holding.`

### Side panel (`:367-381`), phone: after the mode tabs; desktop: sticky right column 280px at 1024px
- Count: Free with locks `{open} of {total} cards open, {n} Must-know in all`; else `{total} cards, {n} Must-know`.
- Either `In Revise. Due cards come back there.` (green check) or the key `Add chapter to Revise` (volt in Read, outline in the other modes) with line under it: Pro `Adds the {n} Must-know cards. Good-to-know cards you add one at a time.` / Free `Adds the {n} open cards. Free reviews 10 cards a day.`
- Add errors: `Adding these cards needs Pro. Reading them stays open.` / `The cards were not added. Try again.`
- Pro with any Must-know: quiet underlined button `Print chapter sheet` (printer icon), calls `window.print()`.
- On phone in Study and Last look, side panel and reason line are hidden (`keycards.css:372-375`).

### Mode control (`ModeTabs`, `:57-74`)
Segmented control `Read | Study | Last look`, `aria-label="How to use these cards"`, a thumb that slides 240ms; each mode switch remounts the panel (`key={mode}`) with a 200ms fade. Mode definitions live in `kinds.js:45-49`; there is no explanatory text for any mode anywhere on screen.

### Read (`ReadMode`/`ReadEntry`, `:78-109`)
One long vertical list of every open card in book order (`readingRows`, `kinds.js:254`). Per card, top to bottom:
1. `CardHead`: kind label (Definition, Term, Key line, List, Formula, Entry...), then **`Must-know` volt tag** when `importance === 'must'`, then `Asked in {n} past paper(s)` when `asked > 0`, optional `In Revise` tick, and a `...` menu (right).
2. `Prompt`: the front, as a small grey 15px line (omitted for Term and Key line, where the cloze line itself is the back).
3. `NcertText`: the book's words in Literata 17.5-19px with a 1px left rule; lists keep NCERT's own numbers, formulas break before "=", journal entries drawn as Dr/To rows with amounts, the blanked words underlined heavier.
4. `CardSource`: `Business Studies Part 1, Ch 1, p. 3` (small grey).
5. `InShort`: `In short ...` paraphrase in the app's face (for English the note stands alone).
6. Report form inline if opened.
Free: after the open cards one stub row (a small lock icon, then `21 more cards in this chapter.`) plus the `PRO_LINE` and `See Pro`. No per-card locks.
Entrance: each entry rises 280ms, 30ms stagger, only the first 12 (`keycards.css:249,378`).

Card menu (`CardMenu`, `KeyCard.jsx:111-137`): `...` button, popover (160ms pop) with `Add this card to Revise` (Pro, Good-to-know cards not yet in Revise only; `ReadEntry:80-81`) and `Report this card`. Report form (`ReportForm`, `:140-165`): label `What looks wrong with this card?`, textarea (300 max, placeholder `For example: a word differs from the book, or the page is wrong`), `Send report` / `Cancel`, counter `n / 300`; sent state `Thank you. Your report is saved, and reported cards are checked against the book.`; failure `The report was not sent. Your words are still here. Try again.` Three distinct reports suspend a card for everyone (`keycards.js:36`).

### Study (`StudyMode`, `:120-177`) (the part the owner likes, LK5)
- Plays `open` cards (all open cards, Must-know and Good-to-know) in book order, 20 a round (`STUDY_ROUND`). Progress bar (3px, scaleX 260ms), position line `4 of 20` with, for long chapters, `Cards 21 to 40 of 165` at the right.
- `KeyCardPlayer` (`KeyCard.jsx:197-287`): card surface (lit gradient and grain, 20px radius) with `CardHead` (with menu), the Prompt as a 19-23px display-face h2, then a dashed rule. Front only until revealed. `Show answer` (volt, `Space` key chip) or tap anywhere on the card; Space or Enter also reveal. Revealed: NcertText, source, In short (220ms reveal), focus moves to the rating row and scrolls it into view.
- Ratings: `Missed` (key 1, rating 1), `Got it` (key 2, rating 3, volt), `Easy` (key 3, rating 4). Counts only after the server confirms (`sendReview` with mode `study`); button shows a spinner meanwhile; failure `That rating was not saved. Try again.`
- Under the card: `Each card you rate joins Revise: Missed brings it back soon, Got it and Easy space it out.` plus on desktop ` Space shows the answer; 1, 2 and 3 rate it.`
- Motion today: new card slides in (`kc-in`, 240ms, 8px) because the player is keyed by round and card id (`:173`); answer fades in; rating row fades 180ms; progress bar eases. **Nothing happens when Got it is pressed** other than the next card sliding in: no confirmation, no count, no streak (LK5 gap).
- Round end (`:150-169`): h2 `{n} cards studied`, `Cards 1 to 20 of 165.` (or ` That was the last of the chapter.`), counts `Missed / Got it / Easy`, keys: `Study the next 20` / `Study the last {n}` / `Study the last card`, `Add chapter to Revise` (if not in Revise), `Study again` or `Study again from the start`, `Read the chapter`; Free also sees the Pro gate with lead `You studied the {n} open cards.`
- Limit states (`limitCopy`, `kinds.js:351-357`): `Today’s new cards are used` (Free 5 new a day; also remembered in module var `newCardsUsedOn` for the page visit), `Today’s free reviews are used` + `Free includes 10 card reviews a day. Reading the cards stays open, and the reviews come back tomorrow.`, `This card is part of Pro`; each with the Pro gate and a `Read the chapter` key.

### Last look (`LastLookMode`, `:181-231`)
- Plays only `must` cards (`ChapterDeck:282`), one at a time, same card surface (`.kc-look`). Position line `2 of 18`, progress bar. Card shows `CardHead` (with `Must-know` tag, redundant since all are), Prompt (unless cloze), NcertText, CardSource. **No `InShort`, no menu, no report, no hide/reveal, no rating.**
- Keys `Previous` / `Next` (becomes `Finish`), swipe (56px threshold) and arrow keys.
- Fine print: `Must-know only, and nothing is scheduled. Swipe to move on, or use the arrow keys.`
- End: `That was every Must-know card` / `{n} cards, nothing scheduled. Last look never changes when a card comes back.` / `Look again`. Empty: `No Must-know cards are open in this chapter yet.`
- The server accepts `mode: 'last_look'` (`data/keycards.js:18`, `review()` handles it as logged-not-scheduled) but **the web never calls it**: Last look sends nothing at all.

### Read versus Last look in code (LK7)
| | Read | Last look |
|---|---|---|
| Cards | every open card (Free: taste only; Pro: all, incl. Good-to-know) | Must-know only |
| Layout | one scrolling list | one card at a time, card surface, swipe |
| Prompt, NCERT text, source | yes | yes (identical components) |
| In short | yes | no |
| Menu (report, add single card) | yes | no |
| Progress | none | bar and `n of N` |
| Writes | add to Revise by buttons | nothing |
So Last look is Read with the Good-to-know cards and the paraphrase removed and a pager added. The label "Last look" and the line "Must-know only, and nothing is scheduled" are the only explanation; nothing says "revision before the exam". The distinction the student cannot see: both show the same words, and Read already shows the same `Must-know` tag.

### Must-know density (LK13)
`importance` is only `must` or `good`. Counts in `data/keycards/decks/*.json`: accountancy 618 of 868 must (71%), biology 916/1394 (66%), business studies 629/900 (70%), economics 832/1193 (70%), English 193/349 (55%), political science 728/1096 (66%); all decks 3,916 of 5,800 (68%). `CardHead` (`KeyCard.jsx:173`) prints the volt `Must-know` tag on every one of them, so most cards in Read, Study and Last look carry it. It also decides: Free taste (first 5 Must-know in book order, `tasteIds`), what Pro `Add chapter` adds, what `Print` prints, what Last look plays. Card kinds vary heavily: accountancy `fact` 252, `key_line` 130, `entry` 118; polsci `fact` 860 of 1096.

### Print chapter sheet (LK6)
- Pro only (`isPro && must.length`), key `Print chapter sheet` calls `window.print()` (`ChapterDeck.jsx:379`).
- `PrintSheet` (`:235-258`) renders into `document.body` via portal a `.kc-print` section: h1 chapter title, a reference line `Business Studies Part 1, Ch 1. 18 Must-know cards in NCERT’s exact words, each with its page.` (or the deck origin for English), then an ordered list of Must-know cards: Prompt (unless cloze), NcertText, CardSource. Section is `display: none` on screen.
- Print CSS (`keycards.css:349-367`): hides every other body child, white background black text, 11pt, Literata for the book text, `@page { margin: 16mm 14mm }`, avoids breaking inside a card. Screenshot `deck-print-sheet-1440-night.png` shows exactly that: plain text only.
- **No watermark of any kind, no MockMob name or logo, no student name, no date, no page footer, no copyright line.** The text is real selectable DOM text, and a Pro student can also "Save as PDF" from the print dialog. Browser print dialogs normally leave "Background graphics" off, so a background-image watermark would not print by default; a repeated fixed-position element would.
- "Got it then Print that chapter sheet" in the owner's words most likely refers to the Study end screen, but Print is not offered there: it exists only in the side panel (hidden on phone in Study and Last look, `keycards.css:373`). So on a phone, in Study, the student cannot reach Print at all.

### Deck states
loading skeleton (`Loading the chapter's cards`); off/missing (`Key cards are not open yet` + `Your lessons and practice are all still here.` / `This chapter is not in Key cards` + `It may have left the CUET syllabus, or the link is old. Your other chapters are in Key cards.`, `See all chapters`); error (`The cards did not load` / `Check your connection and try again. Nothing you added is lost.`); empty (`No cards for this chapter yet` + NCERT or no-book explanation + `See all chapters`).

### Free versus Pro summary (as shown)
Free: 5 Must-know cards open per chapter, one stub row for the rest, Add adds the open cards, 10 reviews and 5 new cards a day, no reason line, no Print, no per-card Add, one Pro line per screen. Pro: everything, Good-to-know cards via per-card Add.

---

## 5. The "Your part" bug (LK2): root cause

### The control
`OptionPicker`, `KeycardsHome.jsx:71-101`. Shown for subjects whose server body has `options` (Mathematics, Computer Science, Accountancy; `SUBJECT_OPTIONS` at `data/cuet_syllabus.js:18`). Accountancy: label `Your part in Accountancy`, two radios in this fixed order `Analysis of Financial Statements`, `Computerised Accounting`. Fine print: none saved `Choose your part and only its chapters show here and in your practice. Until then, both parts show.`; saved `Only that part’s chapters show here and in your practice. You can change it at any time.`; saving `Saving your choice`; fail `Your choice was not saved. Try again.` Not used anywhere else (practice has no copy of this component; `grep` shows only `KeycardsHome.jsx` renders it; the same option is read server-side for question selection via `src/lib/server/syllabusOption.js`).

### What the options do not do
The two choices themselves can never reorder: `opts.choices` comes straight from the constant (`keycardsSyllabus.js`, `subjectOptions`), the server never sorts it, and the subject tab order is `user.subjects` (a stored array; `me.subjects.filter(isTopSubject)` at `keycards.js:246`). What reorders and flickers is the **selected state** and the **list under it**.

### The sequence, step by step
1. Student taps CAS. `choose()` (`:80-85`) runs `setPending('CAS')`. `current = pending || subject.option` (`:77`), so CAS shows selected at once (optimistic). Good.
2. `await saveOption(...)` PUT `/api/me/subject-options` succeeds.
3. Line 84: `refreshHome()` then, in `finally`, `setPending(null)` in the same tick. `refreshHome` (`api.js:56-59`) nulls the shared cache and bumps every hook listener (`setNonce`). React 18 batches both into one render.
4. In that render `pending` is null and `read.data` is **still the old body** (`useKeycardsHome`, `api.js:66-84`, keeps the previous data while refetching and never goes back to `loading`), so `subject.option` is the OLD value (the previous choice, or `null` on a first choice). `current` therefore reverts: the radio for the old part (or nothing) is highlighted again, the fine print falls back to the old sentence ("Choose your part... Until then, both parts show."), and the chapter list below is still the old list.
5. The effect re-runs with the new nonce and fires `GET /api/keycards` (`api.js:60-63`). That endpoint is the heaviest read in the feature: it pages all the student's `key_card_states`, all answered progress rows, and the learning allowances, then builds every subject's units (`keycards.js:238-277`). It plausibly takes one to several seconds on a cold or busy serverless instance. (Inferred from the code; not timed.)
6. When it lands, `subject.option` becomes the new value: the radio jumps back to CAS, the fine print changes again, and the chapter list swaps at once: the five Analysis of Financial Statements chapters (364 cards) vanish and the Computerised Accounting System unit appears with a "No cards yet" row (`unitsFor` result above). Content under the picker jumps up with no transition.

What the owner sees: tap, selection flips back to the other option, then forward again, then the whole list below jumps. On a no-saved-option first choice the selection simply disappears and reappears. While in the stale window the control also accepts taps against stale state (`:81` compares against the stale `current`), so a student who thinks the first tap failed taps again and fires a second PUT and a second GET; the hook discards the older GET (`alive` flag) so it ends consistent, but the control flickers a second time.

Why it is "sometimes": it depends on how long the home refetch takes. On a warm fast response the revert window is a few frames; on a slow one it lasts seconds. The development preview hides it completely because `fixtures.js:318-385` answers instantly, and no test covers `OptionPicker` (`rg` finds `kc-opt` only in `KeycardsHome.jsx` and the CSS).

### Secondary causes of glitchy feel (same code path)
- Refetch failure wipes the page. `api.js:79`: any failed GET (including a 429 from the 120 a minute limit or a 503) sets `{ state: 'error', data: null }`, so `KeycardsHome` returns the full-page `ErrorState` (`KeycardsHome.jsx:167`) even though the PUT succeeded.
- `refreshHome()` clears the cache but there is no loading or "updating" state, so the stale list is shown as if current.
- The fine-print line swaps among four texts of different lengths (`:95-98`), which moves the list down and up by a line.
- Rows of any block that remounts replay the rise animation (`.kc-row` animation, `keycards.css:111`); sections are keyed `b.label || plain-{bi}` (`:211`), so a change in block shape (plain list versus groups, `blocksOf`) re-keys sections and replays.
- With no saved option the picker shows nothing selected even though the server default is `AFS` (`data/cuet_syllabus.js:21`); both parts show until a choice is made. Picking AFS first therefore removes the CAS row (a visible "shuffle" with no change of selection).
- Module-level cache `homeRead` (`api.js:54`) survives client-side navigation and is only cleared by `refreshHome` from `ChapterDeck`/`LineYouNeeded`/`OptionPicker`. `ReviseRun` does not call it, so after a Revise session in the same browser tab the home's `due` numbers can be stale until a reload (not tested).

### Minimal fix (no redesign)
In `src/components/keycards/KeycardsHome.jsx`, keep the saved choice locally until the server body agrees with it:

```jsx
// :73 add
const [saved, setSaved] = useState(null);
// :77 replace
const current = pending || saved || subject.option || null;
// :84 replace
try { await saveOption({ subject: subject.subject, option: id }); setSaved(id); refreshHome(); } catch { setFailed(true); } finally { setPending(null); }
// after the hooks, add
useEffect(() => { if (saved && subject.option === saved) setSaved(null); }, [saved, subject.option]);
```
Also make the fine-print line 95-98 show a fixed-height slot (or keep `Saving your choice` until `saved` is cleared) so nothing jumps. A sturdier version: have `refreshHome()` in `api.js:56` return the new read promise and `await` it inside `choose` before `setPending(null)`, and in `useKeycardsHome` keep the previous `data` on a failed refetch (`api.js:79`, set `state: 'error'` only when `read.data` is null) so a failed refresh no longer replaces the screen. Add a unit test that renders `OptionPicker` with a delayed `GET` and asserts `aria-checked` never reverts.

---

## 6. Revise integration (src/components/revise, /api/me/revise)

- `reviseQueue.js:1-30,76-80`: Key cards are source 5 of 5 (`keycards`), appended after questions, repaired mistakes, Checks and lesson cards, never under the 5 or 10 daily cap, 15 seconds each in the time estimate (`KEYCARD_SECONDS`), absent when the flag is off. `mixParts` says `{n} Key card(s)` in the head mix line. `kindLine` for a Key card title is just `Key card` (no chapter, no subject).
- `/api/me/revise` (`route.js`): `readKeyCards = keycardsService().reviseSource(userId)`; in the plain body via `keyCards`, in `?queue=1` via `queue.readKeyCards`; a failed read leaves the cards out.
- `reviseSource` (`keycards.js:494-498`) is `dueCards({limit: 20})`: `dueQueue(...)` of due then new cards with the Free allowance; restricted to the student's saved option (`playable`, `:151-162`, so switching AFS to CAS removes AFS cards from Revise).
- `ReviseRun.jsx:344-366` `KeyCardRun`: wraps `KeyCardPlayer card mode="revise"`, same player as Study (so identical Show answer and Missed / Got it / Easy, same keys). On rate it confirms the item (`correct: rating > 1`) and moves on. Free limit shows `limitCopy(kind, {where:'revise'})` (`Today’s free card reviews are used` / `Free includes 10 Key card reviews a day. These cards stay due and come back tomorrow.`) with key `Go on without Key cards` or `Finish for today`, then the Pro gate. Summary line `{n} Key cards reviewed, {m} missed and coming back soon.`
- `ReviseEntry.jsx` (Review's row) says nothing about Key cards; `useRevise.js` reads the plain body.
- Server logging: `mode` values `revise`, `study`, `last_look`; `added_from` is `chapter | taste | mistake | manual` (`data/keycards.js:19`). Study ratings create the schedule row (so rating in Study silently adds the card to Revise, said only by the small line under the card).
- "Add chapter to Revise" in Read adds `chapterAddSet` (Pro: all Must-know; Free: taste cards). A Pro student who only studies cards in Study already has them in Revise one by one.
- Revise start options (counts, a way to choose how many or which chapter) do not exist for Key cards: the only controls are the Today panel's `Revise now` and the chapter's Add.

---

## 7. What differs, in one place, for the redesign

1. Entry is a footnote-weight row in Learn; Key cards have their own subject tabs and chapter list parallel to Learn's own subject tabs and chapter accordions (two lists of the same chapters).
2. There is no "pick a time" and no mix: Study is 20 cards of one chapter in book order; there are no questions, no time, no choice of Must-know only or all, no weakness or revise-specific path. Only one "next action" exists per screen (`Revise now`, `Add chapter to Revise`, `Study the next 20`).
3. Read is a flat card dump (a card per block, tag row, grey front, quote, source, paraphrase, menu) with `Must-know` on about two cards in three; Last look is the same content one card at a time. Neither explains itself.
4. Study works and feels right but has zero reward motion; the reveal and the rating are the only interaction.
5. Print exists, Pro-only, unreachable in phone Study, unwatermarked.
6. The part picker flickers by design (section 5).
7. No Explore feed. No time-boxed session ("10-minute lesson") exists anywhere; `minutesPerCard` is 0.25 (`data/keycards.js:11`), so the server already has the unit to size one.
8. No mastery language is allowed (`kinds.js` comment: never "mastered", no percentage under 6 answers); states are Not started, Too few answers, Needs work, Getting there, Holding, Could not load.

## 8. Motion that exists today (all in `keycards.css`)
`kc-in` 240ms (card, end panel), `kc-rise` 260/280ms with 24/30ms stagger (rows, Read entries, first 12), `kc-reveal` 220ms (answer), `kc-fade` 180-200ms (rating row, panel), `kc-pop` 160ms (menu), progress bar scaleX 260ms, segmented thumb 240ms translate, button press scale 100ms, `kc-spin` 900ms. Easing is `--ease-out`. Reduced motion removes all (`:345-347`). No celebration, count-up, card flip, swipe animation or session summary animation.

## 9. Files to know for the redesign
`KeycardsHome.jsx`, `ChapterDeck.jsx`, `KeyCard.jsx`, `kinds.js`, `api.js`, `keycards.css`, `KeycardsLinks.jsx`, `src/components/study/StudyLibrary.jsx` (Learn hub, lines 66-160), `src/components/study/concepts.css`, `src/lib/server/keycards.js` (`overview`, `deck`, `add`, `due`), `data/keycards.js`, `src/components/revise/ReviseRun.jsx`, `AppLayoutClient.jsx:338-340`.
