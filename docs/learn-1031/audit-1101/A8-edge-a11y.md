# A8: edge cases, broken states and accessibility of Learn v2, the Explore feed and the Explore covers (audit, 1 Nov 2026)

**Scope:** `src/components/learn2/**` (home, chapter, run, cards, feed incl. `ChapterFeed.jsx`, `ExploreCovers.jsx`), the Explore page that hosts the covers (`src/components/feed/DiscoveryFeed.jsx`), and the service they call (`src/lib/server/learn.js`, `learnPreview.js`, `data/learn/feed.js`). Read-only: nothing in the repo was changed, no browser or server was started.

**What I used:** the 138 captures and the measurements in `tmp/learn-1101/audit/index.md` (I opened about 40 of the PNGs: feed at 360, 390, 1366, 1440 in Night and Day; covers; home; chapter; run; end screens; Free and new-student states), the owner's verbatim feedback LK20 to LK23, FEED-2.md, BUILD-1101.md Part 1 and A5-logic.md for the logic context, and the owner's standards (slop list, done check). Evidence IDs from the research brain are cited as T and S numbers only where they apply: T001 (defaults come from visible, editable context), T002 (progress only for completed steps), T003 and T004 (value before the wall, specific CTAs), S014 and S016 are not used because I did not open the paper PDFs in this pass; I say so rather than cite them.

**Limits you must read first (no invented numbers):**
- Everything marked "model" is arithmetic on the real deck lengths (5,451 cards in `data/keycards/decks`, 53 fixture questions) and the CSS in the repo. It is not a browser measurement. Verify with the checks in section 5.
- Contrast ratios are computed from the token hex values in `src/app/(app)/arena.css` with the WCAG formula (script in this session's scratchpad), not sampled from pixels.
- I did not run a screen reader (NVDA with Chrome, TalkBack, VoiceOver). Every screen-reader finding is from the ARIA rules and the markup; mark each as "verify with a real reader" before it is called fixed.
- Two React warnings in the capture ("state update on a component that hasn't mounted yet", feed-session 390 and chapter-lengths 390) have no cause I could find by reading (see F27).

---

## 1. What works and must be kept

Feed and covers
- **The feed's snap logic is thought through.** `scroll-snap-stop: always`, the rest-position safety net (`rest()` in `ChapterFeed.jsx`, which leaves a taller-than-screen slot alone), the 45 percent line for which item is active, `still()` for reduced motion in every programmatic scroll. Keep all of it.
- **No key on the client before an answer.** The server grades and the client only paints the verdict. The service is idempotent per item (`answer()` returns the stored event first), which is what makes a retry safe.
- **Resume is already server-side.** A start with the same request key, or the same chapter and kind on the same India day, returns the same run with only the items not done (`learn.js` `start`, `resumeOrBody`). A reload does not burn Free's one session. Keep it (the client just does not show it yet, F11).
- **The Free rule is said once, at the real limit, in a screen and not a modal** (`19-feed-free-end`, `20-feed-free-second`). The server even sends `next.run = null` on Free, so "Next chapter" does not lead to a dead limit screen.
- **Key rows:** at least 58 px tall, letter badge, text wraps (`overflow-wrap: anywhere`), the right row fills volt with ink text (14.36 to 1), the wrong row has an X icon and the word state, the key row has a check icon. State is never colour alone.
- **Reduced motion is covered in CSS** for the flip (120 ms cross-fade), drift, shake, flight, fan, streak and sheet. Keep the block at the end of `feed.css`.
- **Touch targets are already 44 px or more almost everywhere:** close 44, rail glyph 44, text keys 44, sheet close 44, length control 48, chapter page radios 48, Run's `lr-more` 44, Cards `l2c-show` 44.
- **Layout is stable:** CLS 0.000 to 0.004 on feed, run and chapter, no horizontal spill at any size (0 px at 1440, 1366, 390, 360), zero failed requests, zero HTTP errors apart from the designed 402.
- **Skeletons keep their final shape** (`PageSkeleton`, `fx-skel`, `fxc` skeleton); do not remove them.

Learn
- **Chapter page radiogroup is correct:** roving tabindex, arrows and Home and End, `aria-checked`, and the capped label ("10 min, enough for 9 min today"). The Your own sheet is a real dialog: focus moves in, Tab is trapped, Escape closes and returns focus.
- **Chapter map is the most accessible surface in the build:** each row has a spoken label (`rowSpoken`), the state ring is a second, non-colour cue behind a word, the live filter announces "N chapters match", the sort menu is a menu with `menuitemradio`, the part switch has a status line that becomes an alert on failure.
- **Run player:** focus follows the item (prompt gets focus on each new item), the end heading takes focus, ratings have `kbd` hints (aria-hidden) and keys 1 to 3, `Space` and `Enter` as documented, the Revise pile and the under-dock line are polite live regions, errors are `role="alert"`.
- **The end screens say true things in plain words** (`Fixed`, `2 of 3 right`, a real return day). Keep the tone.

---

## 2. Findings by severity

IDs are stable; section 3 says how to fix each. "Model" and "verify" are explained above.

### Blocker

**F1. A screen-reader student cannot read the answer side of a feed card.** `ChapterFeed.jsx:73-76`: the card is a `div role="button"` with an `aria-label` ("...The NCERT line is showing. Tap to turn it back."). A button's children are presentational and the label replaces its content, so the NCERT text and the source never reach the accessibility tree; the `h2` inside the button also loses its heading role. The line is the point of a flashcard. Verify with NVDA and TalkBack; the ARIA rule is unambiguous.

**F2. Keyboard-only focus order is broken for the feed, and Run leaks it too.** `ChapterFeed.jsx:227` renders the feed into `document.body` after the app shell, moves no focus on mount, and does not hide the shell. The first Tab goes to the shell's sidebar and top bar, which sit under the fixed overlay (z-index 60, invisible), about 20 stops before the feed's Close. Shift+Tab from the feed goes back into them. There is no `role="dialog"`, and Escape closes only the line sheet (`ChapterFeed.jsx:445`), never the feed. Run (`RunPlayer.jsx:455-460`) does move focus into the prompt, which is good, but also has no trap and no Escape. Evidence: `index.md` section 2 (c) lists the only visible controls as Close, Keep, Chapter.

**F3. On a long question the wrong-answer sheet, "The line you needed", is off screen.** `feed.css:115` positions `.fx-sheet` `absolute; bottom: 0` inside `.fx-slot`, whose height is `min-height: 100dvh` and grows with the stem. Evidence: `18-feed-wrong-sheet-1366-night.png` shows the sheet top at y 634 of 768, its text cut after two lines, and option D hidden behind it; `18-feed-wrong-sheet-360-night.png` shows no sheet at all (a 13-line stem pushes options A and B to the bottom of the first screen; the verdict and the line are a full screen below). The same stem shows no cue that anything is below. Data: 6 of 53 fixture stems are over 600 characters, the longest is 1,186 (about 1,330 px tall at 360 wide, model). A case-based CUET question will be like this often. It is the payoff of a wrong answer and it is invisible.

### High

**F4. The header has no scrim, so scrolled content runs under the Close key and the title.** `.fx-top` is `position: absolute; z-index: 6` with no background. `22-feed-chapter-one-question-end-390-night.png` shows option C's text crossing "Profit and Loss Appropriation Account" and the X. Happens on any slot taller than the screen once scrolled (see F3 stems), at every width.

**F5. The NCERT line is clipped inside the card with no cue.** `12-feed-card-turned-360-night.png`: the line stops at "However, the firm" and the rest is cut at the card's rounded edge. The back face scrolls (`overflow-y: auto`) but there is no fade, no scrollbar styling, no label. Model of the deck, fraction of cards whose back does not fit at the current layout (20 px serif, card height `100dvh - 106 px - 14dvh`): 360x640 about 23 percent; 360x780 about 8 percent; 390x844 about 3 percent; 1366x650 about 1.4 percent. Back length p50 129, p90 250, p99 426, max 723 characters (15-line list). Keyboard users cannot scroll it at all because the window handler turns ArrowUp, ArrowDown, PageUp, PageDown into item moves (`ChapterFeed.jsx:437-438`). WebKit is known to scroll badly inside a `backface-visibility: hidden` 3D face; test on iOS.

**F6. On a computer there is still no visible way to the next item, and nothing tells a keyboard user the keys exist** (the owner's LK20, measured in `index.md` section 2). A notch of the wheel does nothing (mandatory snap returns it), three keys the hint implies (`j`, `k`, `Home`, `End`) do nothing, the progress ticks are plain spans, there is no scrollbar, and the only hint is touch wording ("Tap to turn it over"). This is also a WCAG failure by the owner's own rule "never hide features behind gestures alone". Layout is owned by another audit; this document fixes the interaction and the labels (3.4).

**F7. Screen-reader announcements are unreliable and incomplete.**
- The verdict (`role="status"` sr-only, `ChapterFeed.jsx:133`), the streak chip (`:519`) and the keep stamp (`:95`) are inserted already containing their text. Live regions need to exist before their text changes; several readers do not announce an insertion. Run's `lr-verdict` (`RunPlayer.jsx:262`) is built the same way.
- The letter badge on an option is `aria-hidden` (`:121`) yet the verdict says "The answer is B." A listener does not know which option is B (Run adds an sr-only "Option B." prefix, the feed does not).
- The sheet's content ("The line you needed" and the line) is never announced.
- After an answer every option becomes `disabled` (`:120`); a focused button that becomes disabled loses focus in some browsers (focus falls to `body`), and the window key handler then stops receiving a sensible target. Use `aria-disabled` and move focus on purpose.
- The card's aria-label includes the raw front, so a fill-in-the-blank reads "underscore underscore underscore" (`cardFace(card).front` before `splitBlanks`).

**F8. Server error kinds are ignored, which makes dead ends.** `api.js` documents `question_changed`, `question_held`, `run_expired`, `run_ended` and `session_used`. The feed's `choose` catch (`:417-419`) and Run's `pick` catch (`RunPlayer.jsx:530-532`) treat every failure as "Try again".
- A question edited or held by an open Mob paper returns 409 forever. In Run the options stay locked (`disabled={Boolean(picked)}`) and the only key is Try again, which fails the same way; the student can only Close. In the feed the options re-enable, so the student can swipe past, but the same sentence loops.
- A tab left open past `answerHours` returns 409 RUN_EXPIRED on every answer: same loop.
- Free with two tabs: the second tab's answer returns 402 FREE_SESSION_USED and shows "not saved".
- A missing or retired chapter (404) says "We could not line this up. Try again." on the chapter page, "The feed did not start, check your connection" in the feed and "This run did not start, nothing was lost, check your connection" in Run. A wrong link never recovers by retrying.

**F9. A re-inserted card that was "moved" is duplicated in the feed.** `ChapterFeed.jsx:416` splices `res.reinsert.item` in at `at` whenever `item` exists. The server marks the case where the line's card is still ahead with `moved: true` and the same `item_id` (`learn.js:884`, `keycardsMemoryDb.js:353-357`): the client now holds the card twice, duplicate React key, shared `states`, a "Card n of N" that counts it twice. Run's `insertAfter` refuses a duplicate id (so it does not duplicate, but then it also does not move the card, and the sheet says "This card comes back later in this run." while the card stays where it was).

**F10. Failures on the end screen invent facts.** `ChapterFeed.jsx:347`: when `runEnd` fails the catch builds an end with `kept: { count: 0 }` and no lines, which renders "Nothing kept this time. Keep a card and it comes back in Revise." even if the student kept eight. The server is the only source of those numbers. Also `end` is fetched once (`!end` guard at `:345`): scroll to the end, scroll back, keep or answer more, return, and the screen still shows the first numbers (and a chapter that has no cards at all says "Keep a card", `22-...-end-390`).

**F11. A resumed feed looks like a new one.** The server returns only items not done (`runBody ... resumed`), the client ignores `run.resumed` and the `?run=<id>` of BUILD-1101 1.3: ticks restart at "1", `aria-posinset` restarts, checkpoints count only what is left (`numberBefore`), and `res.reinsert.at` (an index into the full server list) is spliced into the shorter client list (`Math.min(at, length)`), so the line's card lands in the wrong place. Back and forward, a reload mid-feed and "Chapter" then Back all hit this path.

**F12. Chapter page: the Start key sits under the floating dock on the first screen of a phone** (`40-chapter-10min-360-night.png`: the key at y 690 of 780, the dock from 705, so the key is half hidden and dimmed; at 1366x768 it ends at y 752). The page's one volt action is where the owner's slop item 1 (floating UI over controls) says it must not be. The label can also lie: the link already carries the new length (`runHref`) while `startLabel` still shows the previous dry run until the preview lands.

### Medium

**F13. Pile sublabels truncate real data.** `.lc-pile__min` is `white-space: nowrap; text-overflow: ellipsis` (`chapter.css:179`); `40-chapter-10min-360-night.png` shows "2 of 3, about 2 ..." The standard says never truncate costs and counts.

**F14. Day-theme contrast.**
- Rest options use `opacity: 0.55` (`feed.css:111`): Day text is **3.79 to 1** (needs 4.5). Night is 5.58, passes.
- Upcoming progress ticks use `--a-line`: **1.22 to 1** in Day, 1.40 in Night; the ticks are the only visible progress.
- Card and option borders use `--a-line-strong`: 1.63 (Day) and 1.94 (Night) against the page; the card is told apart by a shadow only.
- `.fx-pile__k` is 10.5 px and `.fx-pile__f` 12.5 px (end-screen pile): under any readable minimum.
- Passes (keep): ink-3 on page 5.89 Day and 7.00 Night; accent text on white 6.66; bad text on its wash 5.80 Day, 7.67 Night; focus ring 6.07 Day, 14.8 Night; volt row text 14.36.

**F15. Chapter title in the feed header is truncated to one line.** `.fx-title` is nowrap with ellipsis. Real titles run to 50 characters ("Challenges to & Restoration of the Congress System"); "Accounting for Partnership: Basic Concepts" (42) needs about 290 px at 13 px semibold and 272 px is free at 360. The full name is not reachable by touch or keyboard on the header (the feed's `aria-label` has it, the eye does not).

**F16. The three visible placeholder ticks are fake progress.** In the loading, Free, error and empty states `shell()` draws six ticks (`ChapterFeed.jsx:472`, `[0,1,2,3,4,5]`): `20-feed-free-second-390-night.png`, `23-feed-chapter-no-cards-first-390-night.png`. Research T002: progress only for completed steps.

**F17. Checkpoint and Stop here.** After Stop here, the checkpoint stays in the list and its **Keep going** key calls `go(i + 1)`, which is the end screen: it says "keep going" and ends. The checkpoint number counts cards "seen" by position, not by view (a student who flings past eight cards is told "8 cards seen"). With nothing kept, the line "...save what you kept" refers to nothing.

**F18. Double answer.** Two taps in one frame: `choose` reads `states` from its closure, so both go out. The server replays the first stored result for the second call; the client pairs it with the second choice (the UI shows the wrong row as chosen and a verdict that does not match it), and the replay's `reinsert` is spliced in twice (F9). Rare on touch, cheap to close (a ref lock; and echo the stored `choice` in the answer body so the client can detect a replay).

**F19. Covers (Explore).**
- On a computer with a mouse, covers past the third are unreachable: the row is `overflow-x: auto` with the scrollbar hidden, no arrows, and a vertical wheel does not scroll it (at 1440 exactly three covers fit, so there is not even a peek).
- Three identical volt Play keys in one viewport at 1440 (`01-explore-covers-1440-night.png`): the owner's "one volt action per viewport" and slop item 3. Only the For-you cover should lead.
- The 5, 10, 20 control is 40 px high (`covers.css:12`; the standard is 44).
- Switching the subject keeps the previous subject's covers on screen while `refreshing` (`ExploreCovers.jsx` renders `data.covers` unless `loading`), with the new subject's object drawn on them and Play links to the old subject's chapters.
- If the covers request fails the whole section silently disappears (`return null`): no message, no retry.
- The length resets to 10 on every return from the feed and ignores the length the chapter page remembered (`mm:learn2:minutes`); the row's own scroll position is lost too.
- Switching length announces nothing.
- Free at 20 minutes shows "9 minutes, 5 Key cards and 7 questions" under the 20 control (`04-explore-new-390-night.png` shows the 10-minute case; the server caps Free's 20 to 10 and flags `capped: true`, the client never says so).
- `GET /api/learn/covers` already returns `hook` (the opening Key card, or `{ front: null, locked: true }` on Free), `reason`, `studentLine` and `forYou`; the client uses none of them. These are the data for the owner's LK21 replacement of the repeated object; the locked hook must be handled (front is `null`, never print it).
- On a phone at 390 the covers are below the first screen (`01-explore-covers-390-day.png`: the hero text and three filters fill it); the feature is a scroll away.

**F20. Chapter page.**
- OwnSheet returns focus only on Escape (`ChapterPage.jsx:135`); choosing a length unmounts it and focus falls to `body`.
- `role="radio"` carries `aria-expanded` and `aria-haspopup` (`:96-97`), which that role does not allow.
- Each pile's `aria-label` repeats its state in words ("Tap to leave it out") while `aria-pressed` already carries it.
- The shake when the last pile cannot be left out is silent for a screen reader.
- A first-load failure leaves the heading "This chapter" (the title comes from the preview response).
- Free at the 20 length: the control and Start say "Start 20 minutes" while the run is composed at 10 (the server note appears in the small line under the key only after the preview lands).

**F21. Learn home.**
- Focusing the search field with the keyboard swaps the whole panel (`onFocus` calls `changeView('find')`, which re-keys the region). WCAG 3.2.1 (On Focus): receiving focus must not start a change of context; Tab past the field should not rebuild the page.
- After Cancel or Escape the field is blurred (`changeView` calls `blur()`), so focus falls to `body` and the next Tab restarts at the top of the page.
- `FreeNote` renders first and hides itself in a microtask for a student who dismissed it (one frame of layout shift); initial state should be read synchronously.
- A subject with no parts shows an empty section with only a header; no empty state.
- CLS 0.011 to 0.014 on home at 1440 and 1366, **0.069 at 360** (limit 0.1). Likely causes: the subject shelf centring script and the Free note; reserve their space.
- On a phone the first screen is the app's pill row, the heading, the subject shelf and the search (`30-home-top-360-night.png`), so the first real work starts at about 450 px of 780.

**F22. Run.**
- The wrong-answer line sits under the dock on first view (`53-run-wrong-line-390-night.png`: only the heading "The line you needed" peeks above the dock; the line is a scroll away, reachable only by finding it). It is also a card inside a card (`lr-line` inside `lr-q`).
- A lesson item's `h2` has an id but no `tabindex`, so the "focus follows the item" effect does nothing there.
- `RunEnd` counts numbers up frame by frame inside live text; a reader that lands mid-count reads a partial number.
- Run does not close on Escape.

### Low

**F23. Option text stripping.** `optionText` in `ChapterFeed.jsx:39` strips `^<key>[ .):-]+` from any option, so an option A that legitimately begins with the article ("A reduction in capital...") loses its first word. The server (`servedOptions`) only strips when every option carries its letter; the client should do the same. In Run, `runMath.optionText` uses a case-insensitive regex with an optional separator, which is looser still.

**F24. Option keys beyond four.** Feed keys answer only 1 to 4 and A to D (`:447`); Run handles 1 to 6. A five-option question cannot be answered by key in the feed.

**F25. Small things.**
- `ul role="group"` (`:113`) strips list semantics from its `li` children; use a `div role="group"` with `aria-labelledby` the stem.
- Keep is `aria-pressed` and cannot be undone: a toggle that does not toggle, and a mis-tap has no undo. Use a non-toggle button ("Keep", then "Kept" with an Undo) or drop `aria-pressed`.
- Keep and Save failures are silent (`catch` sets `keeping: false` only); a 402 turns the label to "Pro" with no explanation until a second tap.
- "Tap to turn it over" is centred on the viewport, not on the stage (30 px left of the card centre at 1440).
- "Next chapter: Retirement and Death of a Partner" wraps with a one-word orphan at 360.
- No "Report this card" in the feed, which exists in Run and Cards.
- `.kc-menu__btn` is 44 x 36 (Run's card menu).
- Window high-contrast mode: the right row is a fill; add a border state (see 3.8).

**F26. Streak chip.** `.fx-streak` mounts and unmounts as the active slot changes type and uses `role="status"` on first render (same live-region problem as F7); at 3 or more it is shown on card slots where nothing changes it.

**F27. Console.** Two React warnings ("Can't perform a React state update on a component that hasn't mounted yet", capture `feed-session` 390 night and `chapter-lengths` 390 night). Candidates from reading: `useCountUpState` calling `setShown` in a layout effect during the first mount of a chapter `Pile`, and the portal mount of the feed (`useSyncExternalStore` returning true then false). I could not isolate it. The owner's standard is no console errors; add a test that fails on any console error in these routes.

---

## 3. Proposal (exact values)

Rules for the builder: nothing below changes the product rules (no middle dots, sentence case, 12-hour time, one volt action per viewport, never "mastered", Free limits only at the real limit, no key on the client before an answer). Where I give a number it is a decision, not a range.

### 3.1 Feed shell, focus, keys, announcements (F1, F2, F6, F7, F24, F25)

**Structure.** `.fx.kc` becomes `role="dialog" aria-modal="true" aria-label="{chapter title}, feed"`, `tabIndex={-1}`.

On mount:
1. `const opener = document.activeElement`.
2. Set `inert` on `.app-shell` (and any other child of `<body>` that is not the feed's portal host); remove it on unmount.
3. `root.focus({ preventScroll: true })`. The reader says the dialog name, then the first item.

On unmount: `opener?.isConnected ? opener.focus() : null` (the route change usually unmounts the opener; then focus the page's `h1`).

**Inert slots.** `slot` elements other than `active` get `inert`. The Tab ring is then: Close, the pager (3.4), the active item's controls. 80 tab stops become about 6. Set `active` synchronously in `go()` (before the scroll) so a focus move into the next item works. Keep `role="feed"` on the scroller, `aria-posinset` and `aria-setsize` on each item.

**Keys** (window handler, ignored when `e.metaKey || e.ctrlKey || e.altKey`, when typing, and when the key belongs to a scrollable focus target, see below):

| Key | Does |
|---|---|
| Down, PageDown, `J` | next screen |
| Up, PageUp, `K` | previous screen |
| Home, End | first and last screen |
| Space | on a face-up card: turn it; face-down or any other item: next screen (as now) |
| Enter | on the card's flip key: turns it (native button) |
| 1 to 6, `A` to `F` | answer the open question (up to the number of options) |
| `S` | Keep (card) or Save (question) |
| Escape | closes the line sheet if open, else the feed |
| `?` | opens and closes the keys list (3.4) |

Arrow and Page keys are **not** intercepted when `event.target.closest('[data-scroll]')` is scrollable in that direction (`el.scrollHeight > el.clientHeight + 1` and not at that end): this is the long NCERT back and the sheet body, so a keyboard user can read them. At the end of the region the next press moves the screen.

**One live region, always mounted** (never conditional): `<p id="fx-say" class="sr-only" aria-live="polite" aria-atomic="true"></p>` at the root, plus the existing `role="alert"` for errors. Messages, one at a time, queued 350 ms apart:
- On the active screen settling (250 ms after the last scroll or key, so a flick does not chatter): `Card 4 of 21. Definition, Must-know. What is reconstitution of a partnership firm?` or `Question 5 of 21. You missed this in Mock 4 on 24 Oct. <stem, first 160 characters>`. The blank in a front reads "blank" (replace `_{3,}` with "blank" before building any label).
- On a flip: `The NCERT line. <full text>. <source>.` and on flipping back: `Question side.`
- On an answer: `Right. 3 in a row.` or `Not quite. The answer is B, <option B text>. The line you needed: <line>. <source>.`
- On Keep or Save: `Kept. In Revise, back Wed.` or `Saved.`; on failure: `Could not keep that card. Try again.`

Remove `role="status"` from `.fx-verdict`, `.fx-streak` and `.fx-stamp` (they keep their visual role). Add the sr-only prefix `Option B. ` to each option's text exactly as Run does.

**Answer buttons:** use `aria-disabled="true"` plus an early return in the click handler instead of `disabled`; keep focus where it is, except after a wrong answer, when focus goes to the sheet's heading (`h3 tabIndex={-1}`). On a right answer, focus stays on the chosen row.

**Do not intercept letter keys on a focused link or button** (Close, Chapter): only when focus is on `body`, the feed root or a slot's own controls.

### 3.2 Card flip and the back face (F1, F5)

Replace the `role="button"` card with:

```
<div class="fx-card" role="group" aria-label="Definition, Must-know" data-flipped>
  <div class="fx-face fx-face--front" aria-hidden={flipped}> kind line, <h2> front </h2> </div>
  <div class="fx-face fx-face--back" aria-hidden={!flipped} data-scroll tabIndex={more ? 0 : -1}
       role="region" aria-label="NCERT line"> kind line, back, source </div>
  <button class="fx-flip" type="button" aria-label="Show the NCERT line"> (front only) </button>
  <button class="fx-turnback" type="button">Turn back</button> (back only)
</div>
```

- `.fx-flip { position: absolute; inset: 0; z-index: 2; border: 0; border-radius: 24px; background: none; cursor: pointer }`; focus ring: `outline: 2px solid var(--a-focus); outline-offset: 4px` (as `.fx-card:focus-visible` today). Pressing it anywhere, Space or Enter, flips.
- On the back the full-card button is removed (it would fight the scroll). `Turn back` is a 44 px high, 16 px side padding, 999 px radius, `border: 1px solid var(--a-line-strong)`, 14 px/650 text key at the card's bottom left (`left: 22px; bottom: 16px`). The back's bottom padding becomes 76 px so text never sits under it.
- Both faces stay in the DOM; only the visible one is not `aria-hidden`, so a reader reads the front or the NCERT line as ordinary text. `h2` is no longer inside a button.

**Back text size by length** (set `data-len` from `back.length + 12 * (line breaks)`; min size 16 px, never lower):

| class | characters | size / line-height |
|---|---|---|
| s | up to 110 | 22 px / 1.5 |
| m | 111 to 200 | 20 px / 1.5 |
| l | 201 to 320 | 17 px / 1.5 |
| xl | over 320 | 16 px / 1.5 |

Deck split: 2,067 s, 2,486 m, 731 l, 167 xl.

**Card height.** Change `bottom: calc(14dvh + var(--fx-safe-b))` to `bottom: calc(20px + var(--fx-safe-b))` in `.fx-cardwrap` (the first-card hint moves into the card, below). The card gets 70 px more on a 640 px phone. Result of the model with the size table and the Turn back row: cards that still need to scroll, 360x640 6.1 percent (was 23), 360x780 0.8 percent (was 8), 390x844 0.2 percent (was 3), 1366x650 0.1 percent (was 1.4).

**Scroll cue.** `.fx-face--back { scrollbar-width: thin; scrollbar-color: var(--a-line-strong) transparent }`, and while scrollable and not at the end `[data-more] { mask-image: linear-gradient(to bottom, #000 calc(100% - 52px), transparent) }` (a functional fade, allowed by the standards); set `data-more` from a scroll listener (`scrollHeight - scrollTop - clientHeight > 4`). Where `mask-image` misbehaves under 3D (Safari), use an absolutely positioned 52 px sibling gradient from `var(--a-raised)` to transparent, same rule. Keep swipe passing to the feed at the region's ends as today.

**First-card hint** (inside the card, 14 px/500 ink-3, bottom centre of the card, `bottom: 16px`): `Tap to turn it over` for `(pointer: coarse)`, `Click the card or press Space to turn it over` for `(pointer: fine)`. Shown only on a student's first card, as now.

**Front text.** Keep 30 px (34 px from 1100 px). Give the front face `overflow-y: auto; data-scroll` too (a 150-character front at 360x640 is about 11 lines and a zoomed viewport has less room).

### 3.3 Tall questions, the sheet, the header scrim (F3, F4, F18, F23, F25)

**Header scrim** (functional, opaque for the first 74 px):
```css
.fx-top::before { content:''; position:absolute; z-index:-1; left:0; right:0; top:0;
  height: calc(var(--fx-safe-t) + 74px + 16px); pointer-events:none;
  background: linear-gradient(to bottom, var(--a-bg) 0, var(--a-bg) calc(100% - 16px), transparent 100%); }
```
The streak chip and counter (3.4) sit at `top: safe-top + 70px`; they have their own surface, so the 16 px fade under them is enough.

**One sheet, rendered at the feed root,** not inside a slot: state `sheetFor = itemId`. Position `absolute; left:0; right:0; bottom:0; z-index: 8`, content column `width: min(100%, 560px)` centred with the same `--fx-side` padding, `max-height: min(56dvh, 480px)`, radius `22px 22px 0 0`, same shadow and 280 ms rise. Role `region`, `aria-label="The line you needed"`, `tabIndex={-1}` and takes focus on a wrong answer (3.1). The close key stays 44 px.

When the sheet is open the active slot gets `--fx-sheet-h` (the sheet's measured height, via ResizeObserver) and:
- `.fx-slot--question { padding-bottom: calc(max(170px, var(--fx-sheet-h, 0px) + 24px) + var(--fx-safe-b)) }`
- the key row is scrolled into view with `scrollIntoView({ block: 'nearest' })`, `scroll-margin-top: 120px`, `scroll-margin-bottom: calc(var(--fx-sheet-h) + 16px)`.

So the right row, the student's row and the sheet are visible together on a 360x780 phone and on 1366x650, however long the stem. While the sheet is open, the answered question's slot may scroll freely under it; Escape or the X closes it.

**Wheel and tall slots:** see 3.4 (the slot scrolls first, the screen moves only at its end).

**Double answer:** `const sent = useRef(new Set())`; `choose` returns at once if `sent.current.has(item.id)`, adds it before the first `await`, deletes it on a failure that allows a retry. Ask for `choice` to be echoed in the answer body (additive field, API-CONTRACT rule); on a replay whose `choice` differs from what the student tapped, show the server's choice. Splice a re-inserted item only if `!list.some(x => x.id === item.id)`, and if `res.reinsert.moved` remove the old entry first, then insert at `at`.

**Options:** strip a leading `<key>` + separator only when every option in the question carries its own letter (the server's `servedOptions` rule); never strip a lone article. Support keys for up to six options.

**Group:** `div role="group" aria-labelledby={stemId}` in place of `ul role="group"`.

### 3.4 Moving on a computer, and what a phone shows (F6)

The other audits decide the composition. This is the interaction that must survive any composition. Everything here is visible, labelled and works by pointer, keyboard and touch.

**Pager** (shown when `(min-width: 900px), (pointer: fine)`):
- Two buttons, **48 x 48**, circles, `border: 1px solid var(--a-line-strong)`, `background: var(--a-raised)`, 22 px chevron icons. Labels `Previous item` and `Next item`, `title` carries the key (`Next item (Down arrow)`). Disabled at the first and last screen with `aria-disabled` and 40 percent opacity (non-text contrast is not required for a disabled control).
- Between them the counter, **13 px / 600, tabular figures, ink-2**: `3 of 21` (checkpoint screens say `After 8 of 21`; the end screen says `Done`). The counter is the visible text for the live region's "Card 3 of 21".
- Placement from 900 px up, in the column to the right of the stage: `left: calc(50% + (var(--fx-stage) / 2) + 24px)`, vertically centred, 12 px gaps. With the stage column unchanged at 560 px: 1440 -> x 1024 to 1072; 1366 -> x 987 to 1035; 1024 -> x 816 to 864 (fits; nothing overlaps the 60 px rail). Below 900 px with a fine pointer: a horizontal pair centred at the foot, `bottom: 20px`, 12 px gap, counter between.
- Tab order: Close, Previous item, Next item, then the active item's controls.
- Phone (coarse pointer, under 900 px): no pager (swipe is the way and the keys of a connected keyboard still work), but the counter `3 of 21` is shown at the left of the streak lane (`top: safe-top + 70px; left: var(--fx-side); height: 28px; font: 600 13px/28px`, tabular, ink-2), so progress is a number as well as ticks.

**Keys list.** A 44 px text key `Keys` at the stage's bottom left (fine pointer only) toggles a popover listing the table in 3.1 in 14 px/500, two columns; `?` toggles it; Escape closes it first. No permanent legend (calm Night).

**Wheel** (fine pointer only, `passive: false`):
```js
let lock = false, acc = 0, last = 0;
onWheel(e) {
  if (scrollableUnder(e.target, e.deltaY)) return;           // NCERT back, sheet body: let it scroll
  const slot = slots[active]; if (!atEdge(slot, e.deltaY)) return; // a tall slot scrolls first
  e.preventDefault();
  const now = performance.now();
  if (now - last > 120) acc = 0;           // a new gesture
  last = now; acc += e.deltaY;
  if (lock || Math.abs(acc) < 24) return;  // 24 px: one notch is 100, a light trackpad touch about 30
  lock = true; go(active + Math.sign(acc));
  setTimeout(() => { lock = false; }, 450); // longer than the 420 ms flip; inertia events within 120 ms of the last do not re-trigger
}
```
`atEdge(slot, dy)`: for `dy > 0`, `slot.getBoundingClientRect().bottom <= innerHeight + 2`; for `dy < 0`, `top >= -2`. Reduced motion: `go` uses `behavior: 'auto'`. This replaces the measured behaviour in `index.md` (a notch of 100 left the feed on the same item in every size). Check: one notch moves exactly one screen at 1440x900 and 1366x768, and 30 events of 40 px move exactly one.

**Scroll bar:** none (calm), the pager and counter are the place cue.

### 3.5 States and errors (F8, F10, F11, F16, F17)

Classify every failure with `LearnError.kind` and render this:

| Situation | Feed | Run |
|---|---|---|
| Answer 409 `question_changed` or `question_held` | the item gets `skipped`; options unlock but greyed; a 14 px ink-2 line `This question was updated. It will not count. Press Down for the next one.` (touch: `Swipe up for the next one.`); the end screen's counts are the server's | same line, and the dock key becomes `Next` (enabled); never a locked screen with only Try again |
| Answer 409 `run_expired` or `run_ended` | scroll to the end screen and read `GET /end`; if that fails, the end-failure state below | `finish()` |
| Answer 402 `session_used` (Free, two tabs) | the Free line (`FREE_SESSION_DONE`) inside the item, two keys `Open the chapter` and `Back to Explore`, no "not saved" | the existing Free `looks` line |
| Answer network error | unchanged: options stay enabled, `role="alert"` `That answer was not saved. Try again.` | unchanged |
| Start 404 (`CHAPTER_NOT_FOUND`) | `h2 This chapter is not in your book list.` + `Back to Explore` | same with `Back to Learn`; chapter page the same |
| Start slow | after 8 s: add under the skeleton `Taking longer than usual.` and a `Try again` text key; the request keeps running | same |
| Reload or Back mid-feed (resumed) | use `run.resumed = { done, of }`: tick offset, counter and posinset start at `done + 1`; one quiet 14 px ink-3 line under the counter for 4 s, `Picked up at 10 of 21.`; the checkpoint numbers come from the server's counts for the whole run, not the remaining items | same |
| `GET /end` fails | `h2 Your feed is saved` + `Its summary did not load.` + `Try again` + `Back to Explore` (copy from Run's end), never zeros | existing |
| Revisit the end after more answers or keeps | refetch `/end` when any `patch` has happened since the last fetch | n/a |
| Zero cards and zero questions | the existing screen, **no ticks** | existing |
| Loading, Free, error, empty | **no ticks** (reserve the 2 px lane so nothing shifts) | n/a |
| One item | one tick, no checkpoint, counter `1 of 1` | n/a |
| 60 or more items (20 minutes) | ticks may fall to 2.5 px each; the counter is the accurate cue | n/a |
| Stop here, then Keep going | **Keep going** clears `stopAt` (the cut items return) and scrolls to the next screen; **Stop here** hides the checkpoint's keys and shows `Stopped here.` and the end | n/a |
| Checkpoint number | `seen` counts screens that were active (a `viewed` set), not positions; `Keep going, or stop here and save what you kept.` only when `kept > 0`, else `Keep going, or stop here.` | n/a |
| End, chapter with no cards | replace `Nothing kept this time. Keep a card and it comes back in Revise.` with nothing (no kept pile, no line) | n/a |

Reinserted items: always splice by id (see 3.3). `res.reinsert.at` is an index in the full server list; when the run was resumed, subtract `run.resumed.done` or map by `itemId` to the item it follows.

### 3.6 Covers (F19)

- **Length control:** `min-height: 44px; min-width: 60px` per segment (container 48 px high). Persist and read `mm:learn2:minutes` (the key the chapter page uses); if the stored value is 30 or higher use 20. On change, set a polite status (sr-only `role="status"`, mounted from the start): `Showing 5 minute feeds, 8 chapters.`
- **One volt:** the `For you` cover's Play is `kc-btn--volt`; every other cover's Play is `kc-btn--line` (same size 50 px).
- **Row on a computer:** `(hover: hover) and (min-width: 768px)`: two 44 px circle buttons over the row's left and right edges (`top: calc(50% - 22px)`, `left: -8px` and `right: -8px`, same surface as the pager), `aria-label` `Earlier chapters` and `Later chapters`, shown only when the row overflows and hidden (not disabled) at that end, step `floor(clientWidth / 292) * 292` px (one cover is 280 plus a 12 px gap). The row is `role="region" aria-label="{subject} chapters, scroll sideways"`; it keeps snap and touch scroll. At 1440 with three covers and more behind, the arrows show; at 1366 and 1024 likewise.
- **Stale subject:** render the skeleton when `data.subject?.id !== subject`.
- **Failure:** keep the section, show one 14 px ink-2 line `Chapter feeds did not load.` and a 44 px text key `Try again` (calls `read.refresh`).
- **Free at 20:** under the control, 14 px ink-2, only when `counts[20].capped` and the student has chosen 20: `Free feeds run up to 10 minutes.` The cover line then uses the real counts (it already does).
- **Return:** save the row's `scrollLeft` in `sessionStorage` (`mm:fxc:left:<subject>`) on pagehide and on navigation, restore after the covers paint.
- **Data for the owner's LK21:** `hook`, `reason`, `studentLine` and `forYou` are already served. When the object is replaced by the hook card, handle `hook.locked` (`front: null`): draw the kind label and `Pro card`, never an empty block or the word null; the cover text order stays title, line, key.
- **Phone first screen:** move the covers above the filters on a phone (or show the first cover's top within 120 px of the first screen). The filters stay for the list below.
- Titles: real titles run to 50 characters; at 22 px in a 244 px column that is 3 lines, so the existing 3-line clamp is safe. Add `title` attributes anyway and keep the full title in the Play `aria-label` (it is there).

### 3.7 Chapter page, Learn home, Run (F12, F13, F20, F21, F22)

Chapter page
- **Start key:** at `max-width: 1023px`, `.lc-go { position: sticky; bottom: calc(var(--dock-h, 84px) + env(safe-area-inset-bottom)); z-index: 2; padding: 10px 0 10px; background: var(--a-bg); border-top: 1px solid var(--a-line); margin-inline: -16px; padding-inline: 16px }` (opaque; the Study page's sticky actions use a gradient, do not copy that). The page already pads for the dock at its end (`--dock-h + 24px`).
- **Label:** show `Start {minutes} minutes` immediately; use `data.startLabel` only while `read.status === 'ready'`. While `refreshing`, the link has `aria-disabled="true"` and its click is prevented.
- **Pile sublabel:** `.lc-pile__min { white-space: normal; text-wrap: balance; overflow: visible; min-height: 2.6em }`; never ellipsis.
- **Pile name:** `aria-label="Key cards, 16, about 4 min"` (stable); the state is `aria-pressed`; one sr-only sentence on the list, `aria-describedby`: `Press a pile to leave it out of this run.` On the blocked toggle, set the polite status `At least one kind has to stay in.`
- **Radios:** drop `aria-expanded` and `aria-haspopup` from the `role="radio"` buttons; give the Your own sheet its own label via `aria-describedby`.
- **Own sheet:** after `onChoose`, focus `ownRef`; return focus on scrim click too.
- **404 and first-load errors:** the heading stays `Chapter` (not "This chapter"), the error says `This chapter is not in your book list.` for 404 and `We could not line this up.` + `Try again` otherwise.
- **Free at 20 or Your own over 10:** the length control keeps the chosen length, the key reads the real minutes once the preview lands, and the quiet line reads the server's `capped.text`.

Learn home
- **Search field:** open Find on `pointerdown`, `click`, typing, Enter or ArrowDown; not on `focus` from the keyboard (`:focus-visible`). After Cancel or Escape: `document.getElementById('lh-panel')?.focus()` with `tabIndex={-1}` on the region (a quiet focus ring is not needed on a programmatic focus target; set `outline: none`).
- **FreeNote:** read the dismissal in a lazy `useState` initialiser (this component only renders after data has loaded, so there is no server render to mismatch).
- **No parts:** `lh-none` block `No chapters here yet.`
- **Sort menu:** close on `focusout` that leaves the menu and on Tab.
- **CLS at 360:** reserve `min-height: 28px` for `.lh-subject__line`, give `.lh-free` a fixed `min-height: 64px` when shown, and run the shelf's centre-scroll before first paint (`useLayoutEffect`, `behavior: 'auto'`). Target 0.02 or less.

Run
- **Errors:** as in 3.5 (skip key for 409 question states, end screen for expired).
- **Line you needed:** after a wrong answer, replace the R3 effect's target (the student's own row at the top) with: scroll so both the student's row and the line's heading are above the dock, `scroll-margin-bottom: 150px` on `.lr-line`; if both cannot fit, the line's heading wins.
- **Live region:** one persistent polite region (as the feed's), message `Not quite. The answer is C, Debit side of Current A/c.` plus the line when it shows. Remove the insertion-time `role="status"` dependency.
- **Lesson:** `tabIndex={-1}` on the lesson `h2`.
- **Counts:** the end numbers are `aria-hidden` while counting with the final value in an sr-only copy.
- **Escape** closes Run to the chapter (same as Close) unless a menu or the report form is open.
- Do not nest a card in a card: `lr-line` drops its own surface and uses a 1 px top hairline and 16 px spacing inside `lr-q`.

### 3.8 Day and Night tokens (F14)

All values use the existing tokens or derive from them; nothing new is invented.

| Where | Now | Change | Result |
|---|---|---|---|
| `.fx-opt[data-state='rest']` | `opacity: 0.55` | remove opacity; `color: var(--a-ink-3)`; letter badge `opacity: .7` | Day 5.89 (was 3.79), Night 7.00 |
| Upcoming ticks | `--a-line` | `color-mix(in srgb, var(--a-ink) 40%, transparent)` | Night 3.55, Day 2.43; Day needs 46 percent for 3.0, so use `--fx-tick: 40%` on Night and `48%` on Day (`:root[data-theme='light']`) |
| Done ticks | `--a-ink-2` | keep | 8.57 Day |
| Card and option borders | `--a-line-strong` | keep for the surface; the pager and flip key use `color-mix(in srgb, var(--a-ink) 50%, transparent)` | Day 3.27, Night 4.92 |
| `.fx-pile__k` and `__f` | 10.5 px and 12.5 px | 12 px minimum for both; the pile is decorative so the count line below it stays the text | |
| Right row (Day) | `#d2f000` fill on `#f4f5f0` (1.18 to 1) | add `border: 2px solid var(--a-select)` (4.08 on white) in the Day theme only | boundary visible, text unchanged at 14.36 |
| Forced colours | none | `@media (forced-colors: active) { .fx-opt[data-state='right']{ border: 3px solid Highlight } .fx-opt[data-state='wrong']{ border: 3px dashed } }` | state is not a fill only |

### 3.9 Motion and reduced motion

Unchanged: flip 420 ms `cubic-bezier(0.32, 0.72, 0, 1)`, sheet rise 280 ms, settle 200 ms, shake 240 ms, pop 180 ms, tick fill 600 ms. New:
- Pager press: `transform: scale(0.94)` 100 ms; chevron buttons change state in 150 ms.
- Wheel and key moves: smooth scroll as now (the browser's ~400 ms), `behavior: 'auto'` under reduced motion.
- Fade on the back face: static (no animation).
- Reduced motion: no change to the above beyond `behavior: 'auto'`; the flip stays a 120 ms cross-fade; announcements are unaffected.

### 3.10 Copy strings (sentence case, no middle dots, no exclamation marks)

`Previous item`, `Next item`, `Keys`, `Turn back`, `Show the NCERT line`, `Question side.`, `3 of 21`, `After 8 of 21`, `Picked up at 10 of 21.`, `Stopped here.`, `This question was updated. It will not count. Press Down for the next one.` (touch: `Swipe up for the next one.`), `This chapter is not in your book list.`, `Taking longer than usual.`, `Your feed is saved`, `Its summary did not load.`, `Chapter feeds did not load.`, `Free feeds run up to 10 minutes.`, `Showing 5 minute feeds, 8 chapters.`, `Earlier chapters`, `Later chapters`, `At least one kind has to stay in.`, `Press a pile to leave it out of this run.`, `Keep going, or stop here.` (when nothing is kept), `Click the card or press Space to turn it over` (fine pointer), `Could not keep that card. Try again.`

### 3.11 Worst-case state matrix (build the fixture, then screenshot each)

| Data | Required result |
|---|---|
| Chapter title of 50 characters | header title wraps to 2 lines at 13 px/1.25 (clamp 2, `title` attribute), row height stays 44 |
| Front of 150 characters (11 lines at 360) | front face scrolls inside, nothing clipped, no overlap with the rail |
| Back of 723 characters (15-line list) | class xl, 16 px, scroll cue, keys still reach it |
| Stem of 1,186 characters (about 44 lines at 360) | slot scrolls; header scrim keeps the Close key readable; after a wrong answer the sheet is on screen with the key row |
| 6 options | letters A to F, keys 1 to 6 |
| Zero cards, zero questions | existing empty screen, no ticks |
| One question, no card | `Question 1 of 1`, end without a kept pile line |
| Huge due count (say 999) | cover and card lines use `toLocaleString('en-IN')`; no layout change (Learn home is the only place a due count shows; test the "Due" suggestion) |
| Free at the real limit (402 on start, 402 on answer) | the Free screen or line, never "not saved" |
| Slow start (10 s) and failed start | slow line at 8 s; failure with `Try again` and `Back` |
| Expired run id (409) | end screen |
| Double tap, double submit | one request, one verdict |
| Back, forward, reload mid-feed | resumed counter, no duplicate cards, end numbers true |

---

## 4. Anti-slop test and 0/1/2 rubric

Evidence IDs are only those I can tie to a claim: T002 (progress only for completed steps) for F16; T001 (defaults from visible, editable context) for the length memory in 3.6; T003 and T004 for specific CTAs (`Play`, `Start 10 minutes` pass; the covers' line `10 minutes, 16 Key cards and 5 questions` is the right pattern). The rest is the owner's own standards page.

### 4.1 The 12-part anti-slop acceptance test (pass, partial, fail)

| # | Test | Feed now | Feed proposed | Covers now | Covers proposed | Learn (home, chapter, run) now | proposed |
|---|---|---|---|---|---|---|---|
| 1 | Identity with the logo hidden | pass | pass | partial (same object on every cover) | partial (needs the LK21 hook cover) | pass | pass |
| 2 | One primary action | pass | pass | fail (3 volt Play keys) | pass | partial (Start under the dock) | pass |
| 3 | True content | partial (fabricated zeros, placeholder ticks, positional "seen", stale end) | pass | partial (Free 20 shows 9 minutes; stale subject) | pass | partial (A5: "Start 9 minutes") | partial (A5 owns the rest) |
| 4 | Hierarchy at first scan | partial (calm on a phone; blank on a computer) | partial (the composition audit decides) | partial (below the first screen on a phone) | pass | partial (phone first screen is chrome) | pass |
| 5 | Intentional composition | partial | partial | pass | pass | pass | pass |
| 6 | Typography by role | pass (10.5 px pile text aside) | pass | pass | pass | pass | pass |
| 7 | Every state | fail (sheet off screen, 409 loops, resume, end failure) | pass | partial (vanishing failure, stale) | pass | partial (409 loop, 404 text) | pass |
| 8 | Accessible interaction | fail (F1, F2, F7) | pass (verify with readers) | partial (no arrows, 40 px) | pass | partial | pass |
| 9 | No pseudo-evidence | partial (placeholder ticks, positional seen) | pass | pass | pass | pass | pass |
| 10 | Motion with a reason | pass | pass | pass | pass | pass | pass |
| 11 | One leading metric plus one guardrail | fail (no events exist: `grep track|analytics|logEvent` in `learn2` returns nothing) | defined, not built (see below) | fail | defined | fail | defined |
| 12 | What would be better without this? | the six placeholder ticks, the Chapter key repeated on every item, "Tap to turn it over" on a computer | all three removed or moved (Chapter into the header) | the repeated object, two of three volt keys | both addressed | the nested card in Run, the first-screen pill row on phones | nested card removed |

Leading metric plus guardrail, to define now and build with the instrumentation work: Feed, leading = share of started feeds that reach the end screen having answered or kept at least one item; guardrail = answer-not-saved rate (any non-2xx on `/answer`) under 1 percent. Covers, leading = Play taps per covers view; guardrail = feed-start failure rate. Learn, leading = runs started per chapter page view; guardrail = run-error screens shown.

### 4.2 The 0/1/2 rubric (12 dimensions; this is an internal checklist, not proof of quality, and the owner signs off)

| Dimension | Feed now | Feed prop. | Covers now | Covers prop. | Learn now | Learn prop. |
|---|---|---|---|---|---|---|
| Task fit | 1 | 2 | 2 | 2 | 2 | 2 |
| Information architecture | 1 | 2 | 1 | 2 | 2 | 2 |
| Content truth | 1 | 2 | 1 | 2 | 1 | 1 (A5) |
| Readable hierarchy | 1 | 2 | 1 | 2 | 1 | 2 |
| Visual specificity | 2 | 2 | 1 | 1 (LK21) | 2 | 2 |
| Accessibility | 0 | 2 | 1 | 2 | 1 | 2 |
| Functional states | 1 | 2 | 1 | 2 | 1 | 2 |
| Trust | 1 | 2 | 1 | 2 | 2 | 2 |
| Intentional motion | 2 | 2 | 2 | 2 | 2 | 2 |
| Performance | 2 | 2 | 2 | 2 | 1 (CLS 0.069 at 360) | 2 |
| Responsive integrity | 1 | 2 | 1 | 2 | 1 | 2 |
| Instrumentation | 0 | 1 | 0 | 1 | 0 | 1 |
| **Total of 24** | **13** | **23** | **14** | **22** | **16** | **22** |

Notes: "proposed" assumes the proposal is built and the section 5 checks pass; Instrumentation stays at 1 until events exist. A high visual score never cancels a correctness failure: the feed's 13 is held down by F1 to F3, not by looks.

---

## 5. Acceptance checks (the builder runs these; a screenshot alone does not close an item)

Keyboard and focus
1. Open the feed by keyboard from the cover's Play: within 1 Tab press focus is inside `.fx`; `document.querySelector('.app-shell').inert === true`; Tab from Close reaches the pager and the active item's controls, and the 8th Tab stop is back at Close (a closed ring). Escape closes the sheet, then the feed, and focus returns to the opener or the page `h1`.
2. Walk the whole feed with the keyboard only (Down, Space, 1 to 4, S, Escape) on a 21-item feed at 1366x768: every item reachable, the NCERT line of a 723-character card scrolls with ArrowDown before the screen moves.
3. A reader (NVDA with Chrome, TalkBack): the NCERT line is read on flip; a right and a wrong answer are announced with the option's text; the sheet line is announced; `Card 4 of 21` on arrival. Record the result in the notes file.
4. Run: Escape closes; Shift+Tab never leaves the player.

Layout and contrast
5. At 360x640, 360x780, 390x844, 1366x650, 1366x768, 1440x900 and 1024x768, Night and Day: for every state in 3.11, `getBoundingClientRect` of the sheet, the key row and the Close key are inside the viewport and none overlap; no horizontal scroll (`scrollWidth <= innerWidth`).
6. Computed contrast from the page's real colours: every text 4.5 or higher; pager, flip key, borders, ticks 3.0 or higher (use the 3.8 table's values).
7. 44 px: every control's rect is at least 44 x 44 (the covers' length segments included), except the progress ticks.
8. CLS 0.02 or lower on Learn home at 360.

Behaviour
9. Wheel: one notch of 100 at 1440x900 and 1366x768 moves exactly one screen; 30 events of 40 px move exactly one; 1 notch inside a scrollable NCERT back scrolls it, not the feed.
10. A question edited mid-run (return 409 `QUESTION_CHANGED`), an expired run (409 `RUN_EXPIRED`), a Free second tab (402) and a missing chapter (404) each show the table in 3.5; none shows "Try again" twice.
11. Reload mid-feed at item 10 of 21: counter reads `10 of 21`, no duplicate cards, the end numbers equal the server's `/end`.
12. Two rapid taps on two different options send one request and show one verdict.
13. A wrong answer whose line's card is still ahead (the `moved` case) leaves one copy of the card in the list (assert unique ids).
14. `/end` failure never prints zeros; keeping a card after the end was shown makes the end screen refetch.
15. Zero console errors on every route in this audit (fixes the two warnings of F27 or explains them).
16. Unit tests: `optionText` leaves a lone article ("A reduction in capital") and strips a full lettered set; `feedSlots` with a resumed offset; `checkpointNumber` from a viewed set; the 3.2 length-class function.

---

## 6. Cross-checks with the other audits and the owner's words

- LK20 (no way on, blank space): 3.4 gives the way on; blank space is the composition audit's.
- LK21 (same object on every cover): F19 notes the server already serves `hook`, `reason` and `studentLine`; the locked-hook case is the edge to handle.
- LK22 and LK23 (the run is quite good, refine, build completely, test everything): section 5 is the test list; F8, F9, F10, F11 are logic defects that the screenshots do not show.
- A5 (logic) covers F1 and F2 of its own numbering (Free 9 minutes, order); not repeated here.
- Not verified here and flagged for a real device: iOS scroll in the 3D back face, notch-wheel and trackpad feel, real finger flings (the capture's synthetic swipe numbers say a 300 px swipe moves one item in 1 of 3 quick flicks and 0 of 6 slow drags).
