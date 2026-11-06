# UI blitz, track you-rhythm: the You hub, the rhythm, the milestones

14 October 2026. Branch `ui/you-rhythm`. Owns `lib/features/you/**` and `lib/features/rhythm/**`.
Authority: BUILD-BRIEF "Night Sheet" (sections 1, 3 to 8, 10, 12), OWNER-FEEDBACK-1110 ("milestones
should be improved", "weekly needs more thinking over"), ref-high / ref-revolut / ref-fampay, and
the owner's UI standards (his glass, light and motion direction overrides the generic "no glass,
no gradient, no glow" lines; one dominant action, real data only, every state, 44 px targets,
reduced motion all still apply).

## 1. What is wrong now (device shots in tmp/app-shots r3 and r4, and the committed goldens)

- You: one long stack of three identical raised row panels (Progress, Settings, CUET tools). The
  eye has nowhere to land after the sheet. Section names are 15 sp grey labels, so there is no
  hierarchy between "Milestones" and "Settings". The subjects are a 2 by 2 grid of 36 dp glyph
  tiles: the most personal part of the sheet is the smallest. The week pane is text plus seven
  dots.
- Rhythm: the week is a number over seven dots, the same thing the strip below already says. The
  run is two numbers. Closed weeks are a list of sentences. Pause is three identical rows with the
  same pause icon. Nothing on the screen is a picture of the student's rhythm.
- Milestones: three identical cards, each a 4-column rail with 12 sp names that cannot fit, a
  grey "Next" box inside the card (a box in a box), and the nine steps share three token images.
  It reads as a settings list, not as something earned.
- Week sheet: three text blocks and a strip. Right but flat; "2 more study days meet your goal"
  has no picture behind it.
- Celebrations: a raised rectangle with a ring and a line. The moment has no light and no weight.

## 2. Target: one idea, "the week is a ring, the run is a ribbon, the milestones are medals"

All three are drawn in code (CustomPainter), real data only, and used the same way on every screen
so You, Rhythm, the week sheet and the celebrations read as one product.

### 2.1 WeekDial (new, `rhythm/widgets/week_dial.dart`)
A ring of exactly `goal` segments (goal 4 gives four arcs with gaps). Each study day counted this
week inks one segment, left to right, like the pencil stroke of the bubble sheet. The count sits
in the middle as a MonumentalNumber ("2") over a plain "of 4 study days". Days past the goal draw
as small inner arcs. A met week closes the ring: a 700 ms light sweep runs once round it and a
soft volt glow (the one permitted glow, the signature visual) settles under the arcs. A paused
week draws the segments dashed and grey with no count claim. Sizes 184 (rhythm hero), 104 (You),
92 (week sheet). Fill timing: 160 ms lead, then 300 ms per segment, 110 ms apart, glide curve.
Reduced motion: drawn settled. The dial never contains the key words "Counted" or "Not counted"
(those stay in the one-line key under the strip).

### 2.2 RunRibbon (new, `rhythm/widgets/run_ribbon.dart`)
The last closed weeks (the server sends at most 12) plus this week, as capsules left to right
(old to new). Capsule height is days studied of 7. A week that met its goal is volt, a week that
did not is a quiet grey, this week is outlined until it is met. A short tick across each capsule
marks that week's own goal. The strip scrolls (40 dp per week, so every week is a 40 dp target);
it opens scrolled to this week. Tapping a week says it in words under the ribbon ("Week of 5
October, 4 of 4 days. Goal met."), with the tick haptic. Capsules grow in left to right, 40 ms
apart, 360 ms, glide. With no closed week yet there is no ribbon, only the one plain line.
Truth rule: every capsule is a number the server sent; nothing is estimated.

### 2.3 Medal (new, `rhythm/widgets/medal.dart`)
A brass coin drawn in code: sweep-gradient rim, radial disc, an engraved numeral or glyph, and a
lit arc. Earned = brass. Next = dashed ring in volt (Night) or ink (Daylight) with the glyph.
Later = faint ring. A step that just landed plays once: the coin settles from 0.92 with a soft
overshoot while a diagonal light band crosses it (500 ms, the milestone ceiling). Nine steps get
nine different engravings (1, a sheet, 10, a tick, 5, 10, 25, a turning arrow, 4), so no two look
alike; the three generated brass tokens stay as the large headline object of each path.

## 3. Screens

### 3.1 You (hub)
- Hero: identity on the ground in the lamp pool. Name at display size (36), Mobi 120 dp waving and
  alive (tap reacts), the stage line, the email small. Top row: back key and Edit.
- This week: the one lit pane. WeekDial (104) on the left; on the right the plain words (the
  count sentence, the run line); the planned strip and key beneath; "Show me" only with evidence.
  The whole pane opens Rhythm (tick haptic).
- The sheet: course as a title, colleges as a ranked list (rank rings, as before), then Subjects as
  a horizontal row of art tiles (the rendered subject objects on their own light field, 96 by 128,
  scrolls with a peek if it overflows). Edit stays at the end of the label line. Unknown fields
  are left off (no "Not set" walls).
- Section titles are Bricolage 22 (Milestones, Progress, Settings, CUET tools): clear steps of
  hierarchy. The shelf shows its count ("2 of 9 landed") and the tokens at 88 dp.
- Progress and CUET tools are flat lists on the ground (hairlines, no panel, larger values on the
  right). Settings is the one raised panel. So the page is hero, pane, shelf, flat list, one solid
  panel, flat list, Mobi: five different shapes, not one repeated box.
- Entrance: five blocks glide up 10 dp and fade, 60 ms apart, once.

### 3.2 Rhythm
- Hero (no card): the WeekDial 184 centred over a lamp pool, with a soft volt glow only when met.
  Under it the week range, then the one lit pane: seven day columns (the existing PlanWeekStrip,
  tap a day to hear it in words, tick haptic), the key, the status line. Mobi cheers beside the
  dial when the week is met, rests when paused, is absent otherwise.
- Your run: the monumental weeks-in-rhythm number and the best run, then the RunRibbon.
- Plan: Weekly goal and Study days (two rows, one raised panel). Unchanged behaviour.
- Pause: the one line "Paused weeks do not break your run." then three pill keys (This week, 2
  weeks, Pause for about 3 months) in a wrap; a paused week shows Resume instead.
- Celebrations: the segmented control and its hint. Turn off rhythm stays a quiet key.
- States: loading skeleton shaped like the dial, error StateView, off (a panel with Turn on),
  paused (dashed dial, Mobi resting, run line "Paused weeks do not break your run"), run ended
  (a new run starts this week; best kept), stale ("As of ...").

### 3.3 Milestones
- Summary: "3 of 9 landed" as a monumental figure, and nine small medals grouped as 3 | 4 | 2 for
  the three paths, so the shape of the whole is visible at a glance.
- Each path is a section on the ground, not a card: the brass token at 92 dp in its own lamp pool,
  the path name at 24 sp, "2 of 3 landed", then a vertical trail. The trail has one 44 dp Medal
  per step joined by a line that draws itself volt down to the last landed step (400 ms). Landed
  steps show name and date. The next step is ringed, shows what lands it in words and, where the
  app can count it exactly, a thin bar with "6 of 10 so far". Later steps are named quietly. A
  link to the record behind the path ends the section.
- Mobi speaks only at the ends (nothing landed yet; everything landed). A step that landed since
  the last visit plays its medal moment once with Mobi hopping beside the title.
- No locks, no streak pressure, nothing expires, no guessed progress.

### 3.4 Week sheet (`/today/week`)
Title and dates, then the dial (92) left of the status words, the strip and key, the week's work as
two small figures when the server sent them (mocks, mistakes repaired), the run line, the rule,
the two keys. Every state kept: loading, failed, off, paused, run ended, stale, no plan.

### 3.5 Celebrations
Inline moment on glass with the lit edge: ring (or Mobi) and one sentence. L2 adds a 700 ms light
sweep across the pane, once. Quiet mode is the same words, no motion. Haptic stays with the
controller (success only after the server acknowledged). The returning card gets a bigger Mobi and
a mini ribbon of the last weeks instead of sentences. The weekly ending card gets the dial.

## 4. Type, spacing, motion, haptics

Type: figure (Bricolage condensed) for counts; Bricolage 22 and 24 for section and path titles;
Hanken for everything read. Spacing: 4 point scale, 32 between groups, 16 gutters. Motion tokens
only from `Motion` (glide 300, emphasized 420, sweep 700, number roll 500, milestone 500); every
animation is transform, opacity or a painter on a RepaintBoundary; nothing loops. Reduced motion:
all of it drawn settled. Haptics: tick on a day, a ribbon week, a card open; settle on a saved
goal; the controller owns the success pattern. No blur is added by this track (FakeGlass only), so
the budget phone cost stays at the painters.

## 5. How it meets the references

HIGH: monumental figures, light as the material, one lit edge, a cinematic hero with nothing boxed
around it. Revolut: calm solid settings below a bold identity, real data as the picture (the ribbon
is the app's own chart). FamApp: collectible objects (the medals and the subject tiles) with weight
and a reason to come back. None of it is gamified: a medal is earned only when the server dates it.
