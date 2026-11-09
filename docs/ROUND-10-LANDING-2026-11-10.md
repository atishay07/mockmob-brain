# Round 10: landing taste refinement and the phone scroll decision (10 Nov 2026)

LIVE on www.mockmob.in since 10 Nov 2026, about 4:30 am IST: main `7c28f3ea7` (Vercel `dpl_6cJqMnU6b1AwqjBNna1FX1KJTGdt`;
rollback `dpl_F112hcu3ezRJratCkZem1eQMpYSm`, main `5dbcea349`). Branch `web/1110-conversion` (worktree `wt-1110-convert`).
Commits: `a0745a808` (the first pass: sample result carried to sign-up, theme note off the phone headline, funnel
steps), `1d81f27eb` (round 10 visual refinement), `100427445` (phone scroll: flow), merged as `6aff554e1`, then
`857d2193f` (reserved section heights, Compass fill variable) and `7c28f3ea7` (subgrid guard). Verification counts:
STATUS.md.

## The owner's words

- 10 Nov ~2:40 am (LK189): "you don't need to see historic signups ... or calculate conversion rate ... I think you have
  made some small, meaningful changes, but I think you can take it deeper and improvise a lot more. I'm treating this more
  as a UI/UX refinement and design taste refinement ... When you are satisfied with the overall landing page and
  everything, then you can commit the site and deploy it live."
- 10 Nov ~2:55 am (LK190): "the scroll decision, which was pending on our side ... find the balance of what could be the
  best solution, because I am conflicted on it ... if we remove scroll, we aren't able to really show the features to the
  people. If we keep the scroll, then it feels very locked in. People will just not scroll to the end of the pricing
  page. The goal is to make people scroll through the entire page ... without making it so forceful and so irritating
  that they leave the page".

## The phone scroll decision: FLOW (settles LK179; replaces "one gesture, one step" on touch screens)

The three models, as a student feels them on a phone:

| Model | What it does | What it costs |
|---|---|---|
| Held (live until this round; LK69) | Every swipe inside a story moves exactly one step, however hard; flings are stopped at a story's door | 22 separate swipes for the four stories; a hard flick does nothing more than a soft one: "very locked in" |
| Free (9 Nov prototype, LK179) | Nothing holds; each story is a card to swipe sideways or tap | The steps are hidden behind a sideways gesture: "we aren't able to really show the features" |
| **Flow (this round)** | The stage still pins and still shows every step, but the scroll is always the browser's own | A flick can pass steps quickly; that is the reader's choice |

Flow, exactly (code: `storyGesture.mjs` FLOW_QUERY, `storyController.mjs`, `ScrollStory.jsx`, `scroll-story.css`):
1. On a touch screen (`(hover: none), (pointer: coarse)`) no touch is owned, no track is locked, no fling is put back
   on a rest while it runs. A mouse or trackpad keeps one gesture, one step (he likes the desktop feel, LK161).
2. The stage shows the step under the middle of the window as the page passes. So a gentle swipe (more than half a
   step's distance) moves one step, less than half goes back, and a flick passes several steps or leaves the story.
3. A scroll that comes to rest inside a story settles on the nearest step's resting place (invisible, the stage is
   sticky). So from any rest the next step is always the same distance away: no "sometimes one, sometimes three".
4. One stop, once per story: the first fling that brings the Mistake Lab, the tour or the Recovery Lab on from above
   lands on its first step. Never a finger's own drag, never on the way back up, never the statement, and never again
   after that first arrival. This is the "show the features" half of the balance: no story can be flown past unseen.
5. A story costs 0.6 of the scroll it cost before on touch (`--ss-run`): about 8 screens for all four, not 13.

What to feel on a phone: flick down from the hero and the page flies until the Mistake Lab catches it once on "Time".
Swipe gently and the scenes change one at a time; flick and they run past and the page moves on. Nothing ever refuses
the finger. The bottom bar (Top, name, n of N, Skip) is unchanged.

If he wants more grip: raise FLOW_SHARE (0.6) toward 1, or land on every story each time. If he wants less: turn the
landing off (`land={false}` on a story). Both are one-line changes.

Checked in real Chrome with real touch flings at 390x844 (`oneGestureBench.mjs` modes `flow`, `landing`, `journey`):
flow 78/78 cells, landing 8/8 (also 8/8 on the live site). The journey, 300 px flicks from the top of the page until
the plans are within half a screen:

| Flick | Before (5dbcea349, held) | Now (7c28f3ea7, flow, live) |
|---|---|---|
| Gentle, 1200 px/s | 41 | 38 |
| Ordinary, 2000 px/s | 31 | 19 |
| Quick, 3000 px/s | 23 | 10 |
| Page height at 390 px | 27,173 px | 22,956 px |

A gentle reader still gets every step, one per swipe; an ordinary one reaches the plans in about 40% fewer flicks, a quick
one in under half. Not checked: a physical phone, iPhone Safari, an in-app browser.

## Round 10 visual refinement (five groups, each looked at before and after at 390 and 1440, Day and Night)

Rules kept: refine in place, nothing removed, no new claims or numbers, Night quiet, labels of actions unchanged.
Boards (before | after) per group: `wt-1110-convert/tmp/1110-refine/<group>/board-390.jpg` and `board-1440.jpg`.

- **Hero:** the typed third line no longer leaves the headline empty in its first seconds (typing starts at 2.2 s, or
  1 s after the opening); the two stray links are the features card's foot; the price hook is one price tag; "Sound on"
  is a small pill concentric with the film's corner; the film sits on the headline's cap line; keys sized to their
  words on tablets; the college strip runs edge to edge with soft ends.
- **Sample and statement:** from 1024 px Mobi's room sits beside the card and the question fits one screen (the one
  layout move of the round: same elements, rearranged for wide windows); "Try 5 questions first" lands with the heading,
  room and card on screen; the section's sub is "Get your score, with every miss explained." (it repeated the card's
  note); the five dashes record each answer; the result's score, misses and quiet keys; subject list states.
- **Mistake Lab and tour:** on desktop the tabs and words are one block centred against the device; the tour's head is
  one line with its sub on the baseline; ten tools in one row; the stage is an inset well; on phones every tour card
  shares one stage and one title line; two-sentence titles break at the full stop; Learn's title is "Learn the idea.
  Then make it stick."; the bottom bar is centred and its name is no longer cut at 360.
- **Score Recovery, Key cards, Compass, DU, exam:** step 4's checks are a timeline with "Fresh checks open soon." on its
  dashed tail; "Shows up in" is a labelled line; Key cards' heading breaks by phrase, its count and segments are one
  progress row, its foot is one panel; the Compass slider looks draggable and the ladder is tighter; DU chips carry a
  quiet plus, the result is a tray, the cutoff chips are four equal tiles; the NTA gate is a card.
- **Creators, pricing, FAQ, close, footer, /signup, /login:** numbers lead the stat tiles and the date sits under them;
  the Free line is a panel with its own quiet key; the value card keeps its own height beside the plan on desktop;
  FAQ answers unfold; Mobi's close line is a bubble; footer headings sit on their lists; the desk and its three points
  are one card and the Google key is drawn whole.

## Owner calls flagged by the builders (shipped as built; easy to turn back)

1. The sample's desktop side-by-side layout (room left, card right).
2. Learn's tour title: "Learn the idea. Then make it stick." (was "Learn the idea behind the mark, then keep it.").
3. The sample's sub line and the coloured progress dashes (missed red, right green).
4. The value card riding beside the plan on desktop (sticky).
5. Plus marks on unpicked DU chips.
6. The landing: one stop per story on phones (section above).
