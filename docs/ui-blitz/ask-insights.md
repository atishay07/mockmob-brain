# ui-blitz / ask-insights: Ask Mobi and Your record

Track owner: ask-insights. Scope: `lib/features/insights/**` (Ask, Your record, Saved, Stream) and
`lib/features/learn/**`, plus their goldens and tests. Design system: Night Sheet (warm charcoal, volt the
only accent, Bricolage plus Hanken, GlassSurface/FakeGlass, OMR bubbles, MonumentalNumber). Owner references:
HIGH, Revolut, FamApp. No pasted AI pictures; every graphic is code.

## 1. What is wrong now

Evidence: `test/golden/insights/goldens/ask_start_night.png`, `ask_conversation_night.png`,
`record_full_pro_night.png` (HEAD).

Ask
- The start state is 70 percent empty ground: a small Mobi, one grey paragraph, three identical outlined pills.
  It reads as a settings page, not a conversation with a character.
- Mobi never reacts. It is a static avatar, not present while the student asks or when a reply lands.
- Replies are the same rounded dark box as the student's message. Nothing says "this came from your record"
  beyond a grey caption; no figures, no evidence, nothing to tap. The model reply shows a block of grey disclaimers.
- No motion between send and reply: a 16 px spinner, then a box appears.
- The composer is a hairline-topped strip with a disabled grey button.

Your record
- One long column of the same thing: a heading, then a dark rounded box or divider list, repeated eight times.
  Findings, chapters, changed answers, pace, week and subjects all look identical, so nothing leads.
- The headline 77 percent is good but the "where the marks went" bar is a thin line, and the 112 questions behind
  it are invisible. The chart is a grey line on a grey grid. Chapters are a list of text with a thin bar.
  Changed answers, pace and week are two-by-two number grids with no picture of the comparison they state.
  Subjects is a list again.
- Nothing animates in as you scroll; the page is born complete.

## 2. Target

Principles: one lead element per screen; the moment layer (hero, lead finding, trend) gets light and numbers,
the work layer (chapters, rows) stays calm; every figure is real and says what it counts; each chart shows the
comparison its sentence makes; each claim keeps its Show me. Motion is transform and opacity (plus painted
progress), once per visit, inside RepaintBoundary; reduced motion shows final state.

### 2.1 Ask Mobi (`/ask`)

Title "Ask Mobi", caption "Reads your last N sessions" (real N, hidden when the record is not loaded).

Stage (empty conversation)
- Lamp light field behind the upper part. A living `Mobi` (size 132, hello entrance) on a pool of light. Mobi says
  one line in its glass bubble, typed in, using real data: "Hi Riya. I have read your last 7 sessions. Ask me
  anything about them." (no name: no name; no record: "Ask me about your marks, chapters, pace or week.").
- Prompts grouped by intent, each group a small eyebrow label.
  - "About your marks": a 2 by 2 grid of prompt tiles. Each tile: a code-drawn glyph on top (marks bar, chapter
    ladder, clock arc, week bubbles), the question in Hanken 15/20 w600, a live preview line from the record
    (top chapter, typical seconds per question, sessions this week), a "Free" chip. The first tile carries the
    lit edge (the one lead).
  - "Ask anything": two wide rows (icon tile, question, "1 credit" chip): a plan request and an explain request
    seeded with the student's top chapter.
- Entrance choreography (once): Mobi 0 ms; bubble types in; eyebrows fade 380 ms; tiles rise 14 dp and fade,
  60 ms stagger, 320 ms each, `Motion.glide`; rows after. Tap: press spring (core), haptic `selection`, sends
  (the disclosure sheet still precedes anything that leaves the phone).

Conversation
- Mobi is present in the header (44 dp, beside the title) and acts: `think` while a reply is pending, `talk` when
  a reply lands, then back to idle.
- Student turn: right aligned, ink-tinted bubble with a volt edge hairline, tail corner 6 dp. Slides 10 dp from
  the right with a fade, 240 ms.
- Pending reply: a bubble holding three OMR bubbles that ink in sequence (loop while pending) and "Thinking it
  through".
- Reply: left aligned with a painted Mobi mark (volt diamond, visor) 28 dp. The first sentence is the lead
  (Bricolage 19/24), the rest is body (16/24, ink 2) with the figures ("35 marks", "6 right") in a heavier tabular
  weight. A newly arrived reply reveals word by word (about 18 ms a word, capped at 900 ms); history and reduced
  motion show it at once. Then the source strip, actions and follow-ups rise in order, 200 ms apart.
- Source strip (citations to the student's own record): "From your record", "Based on 13 questions" and Show me
  (the sessions behind it, via the existing evidence sheet). Model replies show "MockMob AI, 1 credit used", one
  plain line that it can be wrong, an "Open your record" key and Report this reply. Paused replies say no credit
  was used.
- Failures keep the InlineBanner inside the Mobi reply frame.
- Follow-ups: a rail of up to 3 prompts the student has not asked yet.
- Composer: a floating pill (FakeGlass, edge light), 4 line field, a 44 dp volt send disc that scales in with
  text (200 ms); busy shows inking bubbles. Cost line under it. Haptics: `selection` on a prompt, `light` on send,
  `light` when a model reply lands.

States: start, conversation, pending, each failure, paused, offline, 1.3x text.

### 2.2 Your record (`/review/insights`)

Sections: a quiet eyebrow plus a Bricolage headline, 40 dp between sections; each section fades up 16 dp over
360 ms as it is built (the ListView builds lazily, so it reveals as it nears the viewport), once.

1. Hero ledger (moment layer, lamp light, lit edge): the monumental share right with its likely range, and the
   **answer sheet**: one bubble per answered question (capped at 120; above that each bubble stands for n
   questions and the caption says so), inking in reading order over 700 ms (volt right, coral cross wrong,
   dashed ring blank). Legend keeps counts and marks. Show me stays.
2. "What stands out": the strongest finding is the lead card (lit edge, large kind glyph, headline in Bricolage,
   "Based on N questions" tag, Show me, action). The other findings are compact rows with a kind rail.
3. "Marks, session by session": latest result as a compact monumental number with a delta chip against the
   previous session; chart with a soft volt area fading under the line, hollow bubbles for earlier sessions, a lit
   bubble with a halo for the latest, a dashed rule for the best. Draws in over 600 ms. Tap a dot: same note.
4. "Chapters by marks left open": a ranked bar chart, bar length = open marks over the largest, figure at the
   end of the bar, rank numeral, counts under. First row lit. Bars grow staggered, 70 ms apart.
5. "Changed answers": one split bar, helped (volt) against hurt (coral), figures large either side, net below.
6. "Pace": two bars, seconds on right against seconds on wrong answers, typical and slowest markers.
7. "This week and last": two rows of seven day-bubbles, inked on days with a session; net marks above each.
8. "By subject": 2-up plates with the subject's light field and object, monumental percent right, thin marks
   bar, "of 34 answered".

Pro locks keep the ProRow. Loading skeletons match the new blocks. Empty keeps Mobi read. Error/offline/stale
keep their meaning.

### 2.3 Haptics and accessibility
`selection` on a prompt, a chip, a chart dot; `light` on send. Targets 48 dp; every graphic has a semantics label
that carries the figure. 1.3x text wraps, never clips. Reduced motion: no reveals, no draw-in.

## 3. How it meets the references
- HIGH: cinematic lamp light behind a living character, big condensed figures, glass prompts, one lit edge.
- Revolut: a lead insight with a monumental number, charts that carry the comparison their sentence states,
  ranked bars with the figure at the end, a delta chip.
- FamApp: tactile, playful prompt tiles with their own small drawings; the character reacts.
- Duolingo's Duo: Mobi stays in the Ask header for the whole conversation and acts (think, talk).

## 4. Budget
All painted: one CustomPainter per chart. No BackdropFilter added (FakeGlass only). No per-frame layout: animations
drive painters or Opacity/Transform. The answer sheet is at most 120 circles per frame.
