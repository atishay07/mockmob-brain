# R4: Explore (web and app), the swipe deck, and where a chapter feed could plug in

Reading job only. Nothing was changed, built or run. Web code: `C:/Users/atish/Desktop/mockmob copy/wt-1031-keycards-web` (paths below are relative to it unless they start with a drive letter). App code: `C:/Users/atish/Desktop/mockmob copy/wt-1031-keycards-app/flutter_app` (written as `app:lib/...`). Owner feedback read first: `docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md`, items LK12 (Explore chapter feed) and LK13 (too many "Must-know" marks) matter here.

## 1. The short version

1. Web Explore (`/explore`) is a long vertical list of full question cards for one subject, with three filters (Subject, Chapter, Difficulty). It is untimed practice: pick an option, see the verdict and the reason at once, Save, Show answer, "Load more questions". It has no session, no length, no end other than "up to date", no time choice, no mix of anything except questions, and it knows nothing about Key cards.
2. Items are not personalised. The order is the same for every student: community score high to low, then newest first, then id. Already-solved questions come back. The page size is 12.
3. The swipe stack the owner approved on 18 Oct (D90, D94) is **only in the Android app**, on Today, as "Suggested for you" (`app:lib/features/today/widgets/suggested_stack.dart`, 2,773 lines). It is not in the website's Explore and not on the website's Today. The website has swipe pieces to reuse (`useDragCommit`, `useSwipeCommit`) but no deck.
4. The app's Explore is the "question stream" at `/practice/stream`, entry row "Untimed questions" under Practice. It is one question at a time (not a scroll), with Skip, Next question, Previous, a running tally and an end screen. It reads the same `/api/questions/feed`.
5. A chapter feed (a 10-minute run alternating Key cards and MCQs) can be built almost wholly from parts that exist: the Key cards deck read, the feed read with `chapter=`, the question-to-card link files, the drag primitive, the Revise run's mixed-queue rules. The real gaps are listed in section 8: no mixed endpoint, no "unseen first" in the feed, link coverage only about one card in five, Free sees only 5 Key cards a chapter, rating a card schedules it.

## 2. Web Explore, exactly what is on screen

Route and files:
| What | Where |
|---|---|
| Page (server) | `src/app/(app)/explore/page.js` (11 lines; `dynamic = "force-dynamic"`; title "Explore — MockMob"; description "Practise CUET questions at your pace, check the reasoning and save what needs another go.") |
| The whole screen | `src/components/feed/DiscoveryFeed.jsx` (141 lines) |
| One question card | `src/components/feed/QuestionCard.jsx` (118 lines) |
| One-Mobi-at-a-time store | `src/components/feed/feedMobi.js` (9 lines): only the most recently answered card shows Mobi, so a long scroll never gets a crowd of Mobis |
| Styles | `src/app/(app)/explore/explore.css` (57 lines, `.ex-*`), imported in `src/app/(app)/AppLayoutClient.jsx:27` |
| Helpers | `data/explore_feed.js`: `feedWindow`, `advanceFeedPage`, `appendUniqueQuestions`, `chapterGroups`, `questionFeedback`, `feedOptions`, `exploreRowOut`, `publicExploreOptions` |
| Question service | `src/lib/services/questionService.js`: `interactWithQuestion`, `setQuestionBookmark`, `voteOnQuestion`; `fetchFeed` (line 42) calls the other route and is **never used** (grep finds no caller) |
| Vote arrows | `src/components/questions/VoteControls.jsx`; draw nothing unless `CONTRIBUTE_ENABLED` (returns null at line 39) |

Where it sits in navigation: `src/lib/arenaNavigation.js`, `PRACTICE_PAGES = [Practice, Your papers, Learn, Explore, Saved]` (line 34). On a phone it is the 4th of 5 tabs in the Practice row (`src/components/nav/PlaceTabs.jsx`); from 1024 px it is an indented row under Practice in the sidebar. The Today lead card never links to it. The only in-product links to `/explore` are in Saved (`src/app/(app)/saved/SavedPageClient.jsx:272` "Explore questions" and `:288` "Open Explore") and the contributions-paused page (`src/components/contribute/ContributionsPaused.jsx:13`). `src/lib/seo.js:275` advertises `/explore?q={search_term_string}`, but the page ignores `q`.

### Layout (DiscoveryFeed.jsx lines 110 to 139)
- Header via `ArenaHead`: title **"One question. One useful step."**, lede **"Try it, check the reasoning, save what needs another go. This is practice, separate from your timed mock score."** The component is passed `eyebrow="Explore · untimed practice"`, but `ArenaHead` ignores `eyebrow` (src/components/arena/ArenaHead.jsx comment says so), so that line is never drawn.
- Two columns from 1100 px up (`.ex-layout`, main and a 250 px sticky aside), one column below.
- Filter form (`.ex-filters`, a 3-column grid, `1.2fr 1.5fr .8fr`; under 600 px Subject takes the full first row and Chapter and Difficulty share the second). Three `Listbox` controls (`src/components/ui/controls/Listbox.jsx`; a bottom sheet on a coarse-pointer phone, a floating list elsewhere). Labels: **Subject**, **Chapter**, **Difficulty**.
  - Subject: from `GET /api/subjects`, minus any `practice === 'merged'` or `mergedInto`. **First load picks Accountancy** (`available.find(s => s.id === 'accountancy')`, line 40), else the first subject. It does not use the student's own subjects (the app does). Placeholder while loading: "Loading subjects…"; "Choose a subject".
  - Chapter: from `GET /api/chapters?subject=`; shown grouped by unit; first option "All chapters" (or "Loading chapters…"). The value is the chapter **name** (`chapter.name`).
  - Difficulty options: "All levels", "Easy", "Medium", "Hard". Single choice.
  - Changing the subject resets chapter and difficulty.
- List head: the subject's object art (96 px, `SubjectObject`), the subject name as an h2, and "Clear filters" only when a chapter or difficulty is set. A screen-reader status says "Loading questions" or "N questions loaded".
- The cards: every loaded question stacked, full height, in one column. No pagination controls except the bottom button.
- Bottom: **"Load more questions"** (or "Loading…") while `hasMore`; when done: **"You’re up to date for these filters. Saved questions are ready for your next round."**
- Aside, "Make practice count" (a mono label "Tonight’s rule", h2 **"Answer first. Then ask why."**, body "A wrong answer with a clear reason is worth coming back to. Keep those questions close."), two route rows **"Open saved questions"** (`/saved`) and **"Review your timed sessions"** (`/review`), then, once `GET /api/learning/summary?subject=` has answered, **"{n} questions solved in your recorded untimed practice. See progress"** (`/progress`). If contribute is on: "Community votes help organise the feed. They do not certify an answer."

### States
| State | What shows |
|---|---|
| Subjects loading | Subject listbox disabled, "Loading subjects…" |
| Subjects failed | `ErrorState` "Subjects did not load. Check your connection and try again." with retry |
| Chapters failed | `ErrorState` title "Chapter filters did not load", message "You can still practise all chapters." |
| Page loading | "Finding questions…" plus 4 skeleton lines (`.ex-loading`); `aria-busy` on the list |
| Page failed | `ErrorState` scene "unreachable", title "Questions did not load", message "Your answers above are still here. Try loading this page again." |
| Empty, more pages exist | `EmptyState` "No ready questions on this page." / "Some questions are held for checks. Continue to the next page." (the server pages over raw rows and drops held ones after, so a page can be empty) |
| Empty, no more | "No questions for these filters yet." / "Try all chapters or another subject. Held questions stay out of practice." with "Clear filters" when a filter is on |
| End | the "You’re up to date…" line above (focus moves to it if the Load-more button was focused) |

### One question card (QuestionCard.jsx)
- `<article className="ex-question">`: header row = chapter name (or "Practice question") on the left, difficulty word on the right (`easy`/`medium`/`hard`, else "Unlabelled"; hard is tinted warn).
- Optional "Reading passage" block (`passage_text`), then the stem as an h3 (`formatQuestionText`).
- Options as full-width buttons with a key chip (A to D) and text. Picking reveals at once (no confirm step, one answer only, locked by `answerLock`). Correct option turns good-green with a success icon; a wrong pick turns bad-red with an error icon.
- Feedback panel (`role="status"`, focused when the pick came from the keyboard): bold line **"Correct. Keep the reasoning."** / **"The answer is {key}. Here’s why."** / **"Answer: {key}"** (after Show answer) / "The answer is unavailable."; then `q.explanation` or "An explanation is not available for this question." Mobi appears beside the line (`MobiReact`, 44 px) only on the most recent answered card, at most one reaction per 2.5 s, depending on the Celebrations setting (off: none; quiet: a nod).
- "Feedback is shown, but this activity could not be recorded." if the interaction write failed. "This question has no usable answer key. Try the next one." when `correct_answer` is missing.
- Footer: vote arrows (only with contribute on) and, on the right, **Save** / "Saving…" / **Saved** (`aria-pressed`) and **Show answer** (only before answering).
- Save: `POST /api/bookmarks {questionId, saved, source:'explore'}`. Success toast **"Saved for another go."** with "Open saved". A 402 opens the Upgrade sheet (`openUpgrade({trigger:'saves'})`); other errors toast "Could not update saved questions. Check your connection and try again."
- Telemetry per card: an `IntersectionObserver` at 40 percent visibility writes `seen` once (`interaction_type:'seen'`); an answer writes `attempted` with `dwell_ms` and `metadata.selected_key`; Show answer writes `skip` with `dwell_ms`. All use `flow_context:'explore'` (the default in `interactWithQuestion`). The card also has a `variant="saved"` mode (a ruled row, options hidden until "Try it again"), used by the Saved page (`SavedPageClient.jsx:94`). `ReviseRun.jsx` has its own local `QuestionCard` function (line 159), a different component with the same name.
- Important: the card draws the verdict **client-side** from `correct_answer` and `explanation`, which the feed sends in the payload (see below). So this card cannot be reused for a surface that must hide the key until the server confirms.

## 3. How Explore chooses items

Two routes exist. Only the first is used by the screen.

### 3a. `GET /api/questions/feed` (used; `src/app/api/questions/feed/route.js`)
- Params: `subject` (required; 400 if missing; 422 `SUBJECT_NOT_SUPPORTED` for a retired CUET paper), `chapter`, `difficulty` (easy|medium|hard), `search` (the API supports it, the screen never sends it), `limit` (default 20, max 50; the screen sends 12), `offset`.
- Rate limit 180 requests per window per caller (`checkRateLimit`, line 17).
- Query (lines 72 to 97): table `questions`, `is_deleted = false`, `status = live` **or** (`verification_state = verified` and `exploration_state = active`), `subject = ?`, optional `chapter = ?` (**exact match on the name**, so a question still tagged with an old alias name would not match a live chapter name), optional difficulty. Order: `score` desc (with `score >= 0`, only when the votes columns exist), then `created_at` desc, then `id` desc, then `range(offset, offset+limit-1)`. If the score columns are missing it falls back to `created_at` desc only.
- After the page is cut, `readablePracticeQuestions` (`data/practice_library.js:8`) drops: retired chapters, rows outside the student's syllabus option, empty bodies, `score < -2`, rows failing answer integrity, rows not publication-eligible, rows in held families. So a page can come back short or empty while `hasMore` is true. `nextOffset = offset + rawCount`; `hasMore = rawCount === limit` (`advanceFeedPage`).
- No sign-in is needed to call it; if there is a session it adds the student's `userVote` and `saved` flags. **No exclusion of already-answered or already-seen questions.** No shuffling. No concept or difficulty progression. No personalisation.
- Response row fields: `id, subject, chapter, difficulty, body, options[{key,text}], passage_text, passage_group_id, order_index, correct_answer, explanation, tags[], ai_tier, ai_score, verification_state, verification_methods[], source_refs[], upvotes, downvotes, score, userVote, saved`; page fields `questions, total:null, nextOffset, hasMore`.
- `question.tags` and `order_index` exist but nothing uses them for ordering.
- Note: a reconcile doc says a signed-ticket answer flow (`fix/feed-keys-1016`) was drafted so the feed would stop sending the key; it is not in this code. `docs/brain/RECONCILE-WEB-2026-10-16.md` lines 128 and 248.

### 3b. `GET /api/questions/explore` (ranked; **not used by the screen**; `src/app/api/questions/explore/route.js`)
- Reads `question_scores` joined to `questions`, `is_eligible_for_discovery = true`, `exploration_lane` in {standard (default), shadow, fast_track}, three difficulty buckets with quotas **easy 10 percent, medium 60, hard 30** (`DIFFICULTY_QUOTAS`, line 16), each paged by its own `rank_score` cursor (`cursor_easy|medium|hard`), boosting rows with community score above 5. Needs no sign-in; the public row shape (`exploreRowOut`) has **no answer key and no explanation** (security fix 17 Oct).
- Only `questionService.fetchFeed` (unused) calls it. Whether `question_scores` is populated in production was not checked (unknown). This route is the closest thing to a ready "ranked, difficulty-mixed" source, but it has no chapter-aware sequencing and no answer check endpoint.

### 3c. Interactions and progress
`POST /api/questions/[id]/interact` (`src/app/api/questions/[id]/interact/route.js`): needs sign-in (cookie session or Bearer token). Types: seen, attempted, like, unlike, save, unsave, report, report_resolved, explanation_opened, answer_challenged, skip, shallow_bounce. **`flow_context` must be one of `mock | review | explore | shadow`** (line 25; anything else is a 400). skip needs `dwell_ms`. seen, attempted and skip upsert `user_question_progress` (`seen_count, attempt_count, correct_count, skip_count, last_correct, ...`; the correct key is read server-side from `questions.correct_answer`). like and save through this route are only valid in a completed mock or review flow, so Explore saves go through `/api/bookmarks` instead. `GET /api/learning/summary?subject=` supplies `solvedTotal` (and weekly goals, streak, saved count; the Free weekly goal is 30, Pro 80).

## 4. Free and Pro in Explore

- Reading, answering, filtering and "Load more": no gate, no credits, no daily limit. Free and Pro see the same questions.
- Save: Free is capped at **25 saves** (`FREE_BOOKMARK_LIMIT`, `src/app/api/bookmarks/route.js:9`). The 26th returns 402 with `premiumHint: 'Premium unlocks unlimited saved questions.'`; the card opens the Upgrade sheet with trigger `saves`. Pro: unlimited.
- Voting is hidden unless contribute is on.
- Key cards (for comparison, since a chapter feed would mix them): Free sees only each chapter's first 5 Must-know cards in book order (`tasteIds`, `data/keycards.js:66`), the rest as `{locked:true}` stubs; Free is limited to 10 card reviews and 5 new cards a day (`KEYCARD_RULES.free`, line 8); Pro has everything and picks 10, 15 or 25 new a day. A rating in `study` or `revise` mode schedules the card (it joins Revise); mode `last_look` logs without scheduling and uses no allowance, but `review()` still refuses a card Free cannot hold (`PRO('keycards')`, `src/lib/server/keycards.js:362`).

## 5. The app's Explore: the question stream

| What | Where |
|---|---|
| Screen | `app:lib/features/insights/screens/stream_screen.dart` (341 lines), route `/practice/stream?subject=&chapter=&difficulty=` (`app:lib/features/insights/insights_paths.dart`; web href `/explore` maps to it) |
| State | `app:lib/features/insights/data/stream_controller.dart` (252 lines) |
| Card | `app:lib/features/insights/widgets/practice_card.dart`, `question_actions.dart` (Save, vote, flag, "Ask why") |
| Filters | `app:lib/features/insights/widgets/stream_filters.dart`: one chip rail of three keys, each opens a picker |
| Door | `StreamEntry` row in Practice "More" (`app:lib/features/practice/widgets/more_rows.dart:34`): title **"Untimed questions"**, note **"One question at a time, with the reason after each answer."**; also from the empty Saved screen |
| API | `app:lib/features/insights/data/feed_api.dart`: the same `GET /api/questions/feed`, page size 12, and the same `interact` and `vote` routes |

Behaviour: one question on screen, the options reveal on pick (one pick per question), bottom bar with **Skip** (before answering) or **Next question** (after), plus **Previous** once past the first. It reads ahead when 3 questions are left, keeps paging past up to 3 empty pages in a row (the held-page problem), de-duplicates by id in the session, and logs seen, attempted (with `is_correct`) and skip with `flow_context:'explore'` (`'review'` when walking Saved). The header shows a running tally **"{n} of {m} right this sitting"** after the first answer (the website has no tally). The end screen (`_StreamEnd`): Mobi reading, **"That is every ready question here"**, the tally, **"Try another chapter or difficulty, or practise what you saved."**, keys "Change filters" and "Previous". Default subject: the student's first saved subject (the website defaults to Accountancy). Same Free/Pro rules (25 saves, `SaveLimitReached` gets a Mobi refusal). The page switch is a fade with a 3 percent upward slide (reduced motion: a short fade).

The app has no website-style "Explore" tab; the name "Explore" appears only as a comment mapping the web route.

## 6. The swipe stack approved on 18 Oct (D90, D94)

Where the decisions are: `docs/brain/OWNER-MASTER-LEDGER.md` lines 419 (D90) and 431 (D94); spec and mock `docs/design-decisions/pass-1018/SWIPE-V2-1018.md` (321 lines; mock in `tmp/design-1018/swipe-v2/`, not opened). D90 (his words): learn from Tinder and other taste-learning swipe apps; a first-time user must understand what the cards do and what left and right mean; build the whole first-run process in. D94: "Swipe v2 approved as drawn (Up next / Not now, buttons under the deck, first-time demo, undo, honest learning)".

What it is: Today's "Suggested for you" deck under the lead card, **in the Android app only**. Files:
- `app:lib/features/today/widgets/suggested_stack.dart` (2,773 lines): the widget, drag, stamps, demo wiggle, controls row, confirmation bar, end card.
- `app:lib/features/today/logic/suggested_deck.dart` (602 lines): `SuggestedCard`, `DeckPass` (pass with undo and "go through again"), `DeckCoach` (first-run coaching state), `DeckMemory` (kinds passed on 2 of the last 7 days sit lower, local only, key `today_deck_memory`).
- `app:lib/features/today/copy_suggested.dart` (169 lines): all copy. `app:lib/features/today/logic/smart_cards.dart`, `starter_cards.dart` build cards.
- Also `app:lib/features/onboarding/widgets/swipe_preview.dart` (348 lines): the onboarding preview of the gesture.

How it works (spec, section 3 to 5; the code follows it):
- One card on top, two peeking behind. Each card holds only its cost line, title, one evidence line and art. The controls are outside the card in one fixed row under the deck: left button, **Undo** (middle), right button, each 48 dp tall; the button on the dragged side grows and lights as you drag.
- Right = the card moves into the lead card above and becomes "Up next, your pick". It never starts a session and never spends a credit. Left = "Not now": the card tucks in behind the deck and waits at the back; nothing is hidden for good. Tap on a card = the right action. Undo reverses the last swipe. A card whose only action starts a session cannot be swiped right (resists at x0.35); its button is the path.
- Thresholds: 30 percent of the width or a fling of 700 dp/s; 12 dp lock and slope 0.5 against vertical scroll; lean x/20 degrees, clamped to 12 degrees; stamps fade in with the drag; haptics: tick at the threshold, light on commit.
- First run (once in the phone's life): intro line, a 2.2 s self-playing demo (card glides 72 dp right then left with its stamp and the matching button lit), coach lines that change while you drag, a glass confirmation bar after the first right swipe ("holds 5 s, pauses while touched"), and a line after the first left swipe. Coaching ends after both directions are used or 3 visits.
- Count: one line ("4 cards" on first run, then "{n} more after this", "Last of {n}"); page dots were removed.
- End card (Mobi thinking) with **Undo** and **Go through them again**; reduced motion drops the demo and shows both meanings as two lines.

**Copy drift to know about:** the spec names the right action **"Up next"**. The shipped copy file now says **"Do this next"** for the stamp, button, coach line and semantics, and keeps "Up next" only for the result (the bar and the lead card's overline), after two later rounds ("round 1, item 4", "round 2, item 3" in the file header of `copy_suggested.dart`). Left is "Not now" in both. Current strings (`copy_suggested.dart`): title "Suggested for you"; `coachIdle` "Drag the card, or tap a button."; `coachRight` "Right: do this next. It moves into the card above."; `coachLeft` "Left: not now. It waits at the back."; `letGoRight` "Let go: it moves into the card above"; `letGoLeft` "Let go: it waits at the back"; `upNext` "Do this next"; `notNow` "Not now"; `barLine` "It's up next in the card above."; `barLineFirst` "It's up next in the card above. Nothing starts until you tap Start."; end copy `allSeen` "You've seen all four." and so on; `again` "Go through them again"; `everyWay` "See every way to practise".

On the website there is **no deck**. What exists there:
- `src/lib/motion/useDragCommit.js` (a sideways drag that follows the finger 1:1, commits past 35 percent or a 700 px/s fling, springs away or home, rubber-bands the side that does not commit at 0.35, sets `--mk-drag-progress`, and says every action also needs a button). This is the port of the app's `MmDragCommit`. Used by `src/lib/motion/index.js` and `motion-kit.css`.
- `src/lib/motion/useSwipeCommit.js` (+ `swipeRelease.js`): used by Saved rows (`SavedPageClient.jsx:24, :77`): swipe left removes, right practises that chapter, with a visible button for each and the hint "Swipe a question left to remove it, right to practise its chapter."
- `src/components/keycards/ChapterDeck.jsx` Last look (lines 140 to 190): a plain pointer-up swipe (56 px, ratio 1.4), arrow keys, Previous and Next buttons. Not a drag-follow card.
- Web Today's lead card has one "More ways to practise" sheet (`src/components/today/TodayMove.jsx:295`, `SomethingElse`), and the paper reel's "Not now" (`TodayReel.jsx:93`). Neither is a stack.
- `src/app/preview/arena/ArenaPreviewClient.jsx:754` lists `explore`, `cards` and `deck` as preview views (reachable at `/preview/arena?view=explore`), useful for screenshots.

## 7. What a chapter feed would be built from (what exists)

### Key cards, the content side
- Decks: `data/keycards/decks/<subject>.json`, loaded per process and checked against `data/keycards/manifest.json` (`src/lib/server/keycards.js` `loadDecks`). Six subjects: accountancy (868 cards, 14 chapters), biology (1,394, 13), business_studies (900, 11), economics (1,193, 17), english (349, 2), political_science (1,096, 16).
- Card shape (a real one, accountancy): `id "kc.accountancy.accounting-ratios.def-a-ratio"`, `v`, `subject`, `chapterKey "accountancy.accounting-ratios"`, `chapter "Accounting Ratios"`, `unit`, `kind` (definition, term, key_line, list, difference, steps, types, formula, fact, example, entry, quote; English: word, idiom, one_word, usage, rule), `front`, `back`, `quote`, `blanks[]`, `source {kind, book, code, chapterNo, page, section}`, `importance "must" | "good"`, `asked` (number), `tags[]`, `order`, optional `note`. Locked stub for Free: `{id, kind, label, locked:true}`.
- Counts by `importance` (I counted from the deck files): accountancy 618 must of 868 (71 percent), biology 916 of 1,394 (66), business_studies 629 of 900 (70), economics 832 of 1,193 (70), english 193 of 349 (55), political_science 728 of 1,096 (66). This is the data behind LK13: about two cards in three carry "Must-know".
- `asked` is 0 on every card in all six real decks (I counted cards with `asked > 0`: none), so "Asked in N past papers" never shows from real data. (The screenshots show it because the preview uses fixtures.)
- Accountancy chapter sizes: from 8 (Change in Profit Sharing Ratio) to 164 (Accounting Ratios). The chapter the owner named, "Accounting for Partnership: Basic Concepts", is the NCERT title of the chapter whose key is `accountancy.partnership-fundamentals` (46 cards) and `accountancy.profit-and-loss-appropriation-account` (42 cards), both in unit "Accounting for Partnership" (`data/cuet_syllabus.js:104 to 106`). The chapter name in the Explore filter, the question `chapter` column and the card `chapter` field all use the same syllabus name ("Partnership Fundamentals"), and the card key is the slug of it (`chapterKeyOf`, `slugChapter` in `src/components/keycards/kinds.js`). So a chapter chosen in Explore maps straight to a card deck key.
- Reads: `GET /api/keycards/deck?chapter=<key>` returns `{chapter, cards, counts:{total, mustKnow, locked}, added}` (`src/components/keycards/api.js:readDeck`); `GET /api/keycards` the home (`subjects[].units[].chapters[]` with state, due, unlocked, questions count, cards count); `GET /api/me/chapters?subject=` (Pro: n, right, reason, memory); `GET /api/keycards/line?questionId=` (the card(s) behind a question, source linked or matched; needs the question to have `attempt_count > 0`, uses a daily Free allowance of 3, `lineNeededPerDay`); writes `POST /api/keycards/review {cardId, rating 1|3|4, mode, clientReviewedAt}`, `POST /api/keycards/add`, `POST /api/keycards/report`.
- Time rules in code: a Key card is 15 seconds (`KEYCARD_RULES.minutesPerCard = 0.25`, `cardMinutes`; `KEYCARD_SECONDS = 15` in `src/components/revise/reviseQueue.js:30`); a question is 40 seconds (`REVISE_RULES.secondsPerCard`, `data/revise.js:25`, `minutesFor` rounds up to the next 5 minutes). So 10 minutes is about 40 cards, or 15 questions, or a mix such as 24 cards (6 min) plus 6 questions (4 min). These are estimates, not measured times.
- Study runs (the older "Study" lessons system, separate from Key cards): `POST /api/study/runs {mode:'learn'|'recall', unitId, requestKey}`; item types `reveal, choice, text, numeric, ratio, reading`; the server withholds answers until the step is revealed; events `reveal, answer, rate, continue, set_aside` (`data/study_engine.js`, `src/lib/server/study.js:179`). Only four subjects (`STUDY_SUBJECTS = english, accountancy, business_studies, economics`). The app's Learn run screens mirror it (`app:lib/features/learn/models/run_item.dart`). Their unit ids do not equal Key card chapter keys; both carry subject plus chapter name.

### Question to card links (the "alternate cards and MCQs" glue)
`data/keycards/links/<subject>.json` maps a question id to up to 2 card ids. Coverage, from reading the files: accountancy 1,072 questions linked touching 198 of 868 cards (23 percent); biology 235 questions, 257 of 1,394 cards (18); business_studies 267, 220 of 900 (24); economics 296, 318 of 1,193 (27); english 155, 76 of 349 (22); political_science 119, 141 of 1,096 (13). Per chapter it is very uneven. Accountancy examples (linked questions, cards covered of chapter): Partnership Fundamentals 11 questions, 9 of 46 cards; P&L Appropriation 165, 17 of 42; Change in Profit Sharing Ratio 136, 4 of 8; Admission of Partner 159, 16 of 53; Financial Statements of Company 3 questions, 2 of 85 cards. When a link is missing, `lineNeeded` falls back to a text-overlap match of the question's text to Must-know card quotes (needs 3 shared content words, score 0.35).

### Mixed-run machinery that already exists
`src/components/revise/reviseQueue.js` plus `ReviseRun.jsx` (581 lines) already plays **one run of mixed item kinds with one progress line**: `question`, `again`, `check`, `card` (lesson recall), `keycard`. It has `itemKey`, `positionLine` ("{k} of {n}"), `mixParts` ("5 questions back, 2 Key cards"), `mergeQueue`, `filterSource` (`?source=keycards|questions|...`), `recordAnswer`, `advance`, `summary`, minute estimates (40 s a question, 15 s a Key card) and an end screen. It is a **due queue** (what the schedule says is due), not a student-chosen chapter run. It plays Key cards with `KeyCardPlayer mode="revise"` (`ReviseRun.jsx:361`) and questions with its own local `QuestionCard` (line 159).

### Reusable web components for a feed
| Piece | File | Notes for reuse |
|---|---|---|
| Chapter and subject pickers | `Listbox`, `chapterGroups` (`data/explore_feed.js`) | already feed `chapter=` name to the feed |
| Question card | `QuestionCard.jsx` | feed variant shows everything at once, draws verdict client-side; for one-at-a-time you would host it in a stage and hide the vote and Save row, or use the Revise one |
| Key card player | `KeyCard.jsx` `KeyCardPlayer` | front, "Show answer" (Space or tap), Missed / Got it / Easy (1, 2, 3); props `card, mode, position, active, detail, onRated, onLimit`; every rating posts a review and is acknowledged before it counts |
| Card faces | `Prompt`, `NcertText`, `CardSource`, `InShort`, `CardHead` | CardHead prints the kind label, "Must-know" and "Asked in N past papers" |
| Study chrome | `src/components/study/StudyRun.jsx` (`sx-pips`, `flyAway`, `softClick`, Mobi reactions, "Step n of N", ink-the-right-answer motion, `studyFeel.js` with shared numbers also in the app) | pips and the fly-away on rate are the motion the owner liked in Study |
| Drag deck | `useDragCommit` (and `useSwipeCommit`) | gives 1:1 follow, threshold and fling, `--mk-drag-progress` for a stamp or reveal, 0.35 resistance on a side that must not commit |
| Quota and ranking | `/api/questions/explore` | difficulty quotas 10/60/30 if its table is populated |
| Limits and copy | `limitCopy`, `ProGate`, `PRO_LINE` in `src/components/keycards/kinds.js` | "Today’s free reviews are used", "Today’s new cards are used", "This card is part of Pro"; the one Pro line "Pro opens every card in every chapter and keeps them on a schedule." |

### Reusable app pieces
`StreamController` (read-ahead, empty-page skipping, de-dup, tally, `_markSeen`, guard against double taps via `fromId`), `PracticeCard`, `suggested_stack.dart` drag, stamps and the demo wiggle, `DeckPass` with undo, `learn/widgets/card_stack.dart` (a paper-pile mark drawn from a count), `learn/widgets/run_pips.dart`, `keycards/widgets/key_card_run.dart` (Last look: swipe left or Next, swipe right back; lines 226 to 290).

## 8. Gaps for a chapter feed

1. **No mixed source.** Nothing returns "this chapter's cards and questions together". A client would call `readDeck(chapterKey)` and `/api/questions/feed?subject=&chapter=` (maybe two or three pages) and compose the run. The feed has no `exclude=` or `unseen` param and ignores `user_question_progress`, so a student who answered 20 questions yesterday sees them again first. `user_question_progress` has what is needed (`attempt_count`, `last_correct`, `last_attempted_at`).
2. **Order is popularity, not teaching order.** Cards have `order` (book order) and `kind`; questions have `tags` and `order_index`, but there is no concept id on a question and no map from concept to card other than the partial link files. An "alternate card, question, card, question" run is only honestly paired where a link exists (about one card in five). Elsewhere it can only be chapter-level alternation (cards in book order, questions by difficulty), and the screen should not claim a question "tests the card before it" without a link.
3. **Free limits shape a 10-minute run.** Free sees 5 Key cards in a chapter (Must-know, book order); more are locked stubs. A 10-minute Free run is then 5 cards plus questions, or a clear "the rest of the cards are part of Pro" line. Free also caps card reviews at 10 a day and new cards at 5 a day (rating in `study` mode), and the 402 handling exists but is built for Study and Revise end screens.
4. **Rating schedules a card.** `study` and `revise` ratings join Revise (`added_from` manual or mistake). A feed that shows cards as "just look, then try a question" should use `mode: 'last_look'` (no schedule, no allowance) or must say that rating adds the card. `KeyCardPlayer` is documented for `'study' | 'revise'`; passing `last_look` is allowed by the server but is untested in the player.
5. **`flow_context` has no "chapter run" value.** The interact route rejects anything other than mock, review, explore, shadow. A feed run would log as `explore` (the Explore default) unless the route is extended.
6. **Answer key in the payload.** `/api/questions/feed` sends `correct_answer` and `explanation`; fine for untimed practice, but it means no "check on the server" step like Study has. The explore route hides them and offers no answer endpoint.
7. **Page-size and quarantine behaviour.** Raw-offset paging with held rows removed after the cut means short or empty pages; the app handles it (3 empty pages in a row), the website screen just shows "No ready questions on this page." A fixed-size 10-minute run needs the app's loop on the web too.
8. **`chapter=` is an exact-name filter.** It works for live chapter names (what the picker sends). Rows still tagged with an alias or retired name will not show; `data/cuet_syllabus.js` `CHAPTER_ALIASES` (line 443) and `resolveChapter` (line 639) exist to map them, but `/feed` does not use them (it relies on `readablePracticeQuestions` for retired chapters only).
9. **No time choice anywhere in Explore.** There is no "pick 5, 10 or 15 minutes" control. The nearest existing thing is the goal-minutes system for Today (`data/goal_minutes.js`, 5 to 999) and Study's `guidedSequence`.
10. **No Explore entry from Learn or Key cards, none from Today.** The owner's flow (subject, concept, time, mix) would need doors from Learn and from Today into the same run, since Explore itself is 4th in a row of tabs and is linked from Saved only.
11. **Defaults ignore the student.** Web Explore opens on Accountancy for everyone (`DiscoveryFeed.jsx:40`); the app opens on the student's first saved subject. A chapter feed started from a chapter does not have this issue, but the standalone Explore page does.
12. **The ranked route is orphaned.** `/api/questions/explore` and `fetchFeed` are unused; if the ranked ordering is wanted, someone must confirm the `question_scores` table is populated and add chapter-aware ordering.
13. **Web has no swipe deck.** A swipe format on the web means building the deck UI on `useDragCommit` and porting the first-run teaching (demo, coach line, undo) from the app spec; D90 requires that first-time teaching wherever the deck appears. The spec's rule "every swipe has a visible button doing the same thing" (also in `useDragCommit` comments and the Saved page) holds for any new web deck.

## 9. Existing owner rulings that constrain the feed (read from the ledger and the spec; check before design)
- D90: a swipe deck must teach its gestures the first time, with the meaning of left and right in words.
- D94: right never starts a session or spends a credit (that is the Today deck's safeguard; for a practice feed the equivalent is that no swipe should change the student's schedule or spend anything without a visible key).
- COMMUNITY-1018 (owner, 18 Oct dawn, `OWNER-FEEDBACK-2026-10-18-DAWN.md:121`): keep Explore; hide vote arrows and Contribute behind the flag. A new feed card should not bring voting back.
- Explore is deliberately kept apart from mock scores ("This is practice, separate from your timed mock score."); a chapter feed should keep saying it is untimed and unscored. Progress and marks rules in `AGENTS.md`: do not claim practice is "observed gains".
- UI rules (`ui-ux-standards`, DESIGN.md), not read in this job: no arrows or middle dots in copy, sentence case, one primary key per screen.

## 10. File index
Web: `src/app/(app)/explore/page.js`, `explore.css`; `src/components/feed/{DiscoveryFeed,QuestionCard,feedMobi,UploadForm}.jsx|js`; `src/app/api/questions/{feed,explore,[id]/interact,[id]/vote}/route.js`; `data/explore_feed.js`, `data/practice_library.js`; `src/lib/services/questionService.js`; `src/app/api/bookmarks/route.js`; `src/app/api/learning/summary/route.js`; `src/lib/arenaNavigation.js`; `src/components/nav/PlaceTabs.jsx`; `src/components/keycards/{ChapterDeck,KeyCard,KeycardsHome,kinds,api}.js*`; `src/lib/server/keycards.js`; `data/keycards.js`; `data/keycards/{decks,links,manifest.json}`; `src/components/revise/{ReviseRun.jsx,reviseQueue.js}`; `data/revise.js`; `src/components/study/{StudyRun.jsx,studyFeel.js}`; `data/study_engine.js`; `src/lib/server/study.js`; `src/lib/motion/{useDragCommit,useSwipeCommit,swipeRelease}.js`.
App: `lib/features/insights/{screens/stream_screen.dart,data/stream_controller.dart,data/feed_api.dart,widgets/practice_card.dart,widgets/stream_filters.dart,widgets/entry_points.dart,insights_paths.dart,copy.dart}`; `lib/features/practice/widgets/more_rows.dart`; `lib/features/today/{widgets/suggested_stack.dart,logic/suggested_deck.dart,copy_suggested.dart}`; `lib/features/onboarding/widgets/swipe_preview.dart`; `lib/features/learn/{models/run_item.dart,data/run_starter.dart,widgets/card_stack.dart}`; `lib/features/keycards/widgets/key_card_run.dart`.
Docs: `docs/brain/OWNER-MASTER-LEDGER.md` (D90, D94, LK12), `docs/design-decisions/pass-1018/SWIPE-V2-1018.md`, `docs/brain/RECONCILE-WEB-2026-10-16.md` (feed keys).

## 11. Things I could not confirm
- Whether `question_scores` rows exist in production (so whether `/api/questions/explore` would return anything).
- How many live questions each chapter has in the bank (the Key cards home carries a per-chapter `questions` count from the cached inventory; I did not call it).
- The visual state of Explore on web or app: there are no Explore screenshots in the three walk folders, so layout statements come from the code and CSS, not from a picture.
- Whether the shipped app deck is exactly as the spec describes after the 19 Oct rounds; I read the copy file and the deck logic header, not the 2,773-line widget.
