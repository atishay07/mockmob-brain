# The bar: MockMob's bottom navigation, rethought (UI phase 2)

14 October 2026, written after the owner's 18:30 feedback (`design-2026-10-13/OWNER-FEEDBACK-1014-1830.md`). This is a read-only spec. The foundation owner of `lib/core/widgets/dock`, `lib/core/router/app_shell.dart` and `lib/core/router/router.dart` builds it. On navigation it replaces BUILD-BRIEF section 6, the "dock untouched" line in WEB-PARITY (line 22 and decision 3) and directions-final A.5. The owner has asked for the structure to change, so those older decisions no longer hold.

---

## 0. What is wrong today (from the code and the renders)

Sources: `split_dock.dart`, `dock_pill.dart`, `start_button.dart`, `app_shell.dart`, goldens `test/golden/core/goldens/dock_*`, `quick_start_*`, and device shots `tmp/app-shots/r3/03`, `07` and `115`.

1. **The structure has not changed since 13 Oct 04:00.** It is three tabs (Today, Practice, Review) plus a separate Start circle, with You hidden behind a header avatar. The owner says it "looks pretty the same as 25 hours ago". He is right, because the shell has not changed.
2. **The layout is unbalanced.** `SplitDock` centres the whole group (pill + 12 dp gap + 60 dp circle), so the tabs sit left of centre and Start hangs off to the right. At thumbnail size it reads as two objects that do not belong together.
3. **The indicator looks unfinished.** The lit tile is a grey stadium with a 1.5 dp volt arc wrapped over its top-left shoulder (`LitEdgePainter`, `wrap: 0.4`). In `dock_travel_right_night.png` and on device, the arc reads as a rendering glitch rather than light. This is the "green dot" finish he asked for twice.
4. **The glass cannot be seen.** `DockScrim` turns content into solid ground at the dock's top edge (stops 0, 0.28, 0.38). Nothing ever passes behind the glass, so the "glassmorphism" he asked for on 13 Oct 02:30 is invisible: you see a dark band. In Daylight (shot 115) the volt key fades out under a white slab.
5. **Start is ambiguous.** It is a play glyph on a volt disc that "breathes" twice for reasons a student cannot read. The sheet behind it (Quick 10, Full mock, NTA, Repair, Ask) repeats the Practice tab's modes and Today's hero. The same three starts appear in three places.
6. **You is not discoverable.** The only way in is a 40 dp header avatar. Tools (Compass, Combo planner, CUET guide) are two levels under it.
7. **Badges are not real.** Review shows a dot for an unopened result. The real daily count (tonight's repairs) appears nowhere on the bar.
8. **Scrubbing is too easy to trigger.** It starts from any horizontal drag anywhere on the pill, including drags 16 dp from the screen edge, inside Android's back-gesture zone.

## 1. What the bar is for

A CUET student opens MockMob once or twice a day, mostly at night, for 10 to 60 minutes. The loop is: see tonight's move, do the work (practice, mock or repair), read the result, then come back tomorrow. The bar has three jobs, in this order:

1. **Start work in one tap from anywhere.** Getting into work is the product. Everything else serves it.
2. **Move between the four places a student owns:**
   - Today: tonight's move, the week and the road to May.
   - Practice: choose a subject, mode or chapter, plus the question stream, Concepts and NTA mode.
   - Review: mistakes and repair, the record, saved questions and Ask.
   - You: their sheet (goal, colleges, subjects, rhythm, milestones), the CUET tools and settings.
3. **Show live state truthfully:** a session in progress, a result waiting, answers being sent, being offline. Show nothing else.

What is deliberately not on the bar:
- **Ask:** it answers from the record, so it lives in Review's header and on recap cards.
- **NTA mode:** it is a way to sit a paper, so it is in the Start sheet and in Practice.
- **Learn:** the Concepts shelf in Practice, and from the mistake it explains.
- **Tools:** under You.
- **Streaks and any gamified counter.** The owner ranks over-gamified as bad as sparse.

## 2. Two structures considered

### Option A: four places and a Start key (chosen)

`Today · Practice · [ Start ] · Review · You`

This is one glass bar, centred, with five slots. Start is a volt key in the middle slot. It is an action, not a destination, and it opens the Start sheet. A **live capsule** rises above the bar only when something is in progress.

**Gains**
- It is balanced and symmetric, and You becomes discoverable.
- The pattern is familiar to Indian 17-year-olds: PhonePe, Paytm and Fampay all put the main action in the centre.
- Start and Practice get clean, separate jobs: Start means go now with good defaults; Practice means choose and browse.
- The capsule gives the bar real, purposeful motion (resume, sending, marked) instead of decoration.
- The visible change is large.

**Costs**
- Five slots are tight on 320 to 360 dp phones. Tab slots are 52 to 60 dp, and "Practice" scales down slightly at 320 dp.
- The indicator has to cross the Start slot.
- Start and Practice can still blur together unless the content contract in section 6 is enforced.

### Option B: three places, Start absorbs Practice

`Today · [ Start ▲ ] · Review · You`

Practice stops being a tab. A wide volt Start pill opens a tall sheet whose last row, "Choose your own", pushes the old Practice screen.

**Gains**
- Fewest choices and the strongest action-first story.
- Wider slots (about 80 dp).
- Start can carry a contextual label ("Resume 23/50").

**Costs**
- Subject tiles, the question stream, Concepts, NTA setup and Edit subjects become two taps deep. On the website, Practice is the most-used page after the dashboard (WEB-PARITY A2), so this breaks the "extension of the website" promise.
- A label that changes with context duplicates Today's hero, and students learn a button by its position, not its words.
- It drifts toward sparse, which the owner ranks with over-gamified as the worst outcome.

### The pick

**Option A.** It is the balanced choice the owner ranks highest, it keeps website parity, and it fixes every problem in section 0. Option B's best idea, the bar showing live state, survives as the capsule. The baseline (polishing the split dock) is rejected because the owner asked for a structural rethink, and the asymmetry and hidden You are structural problems.

---

## 3. Layout (dp)

The baseline is 360 x 780. The Galaxy M06 is 384 x 853. Every measurement below must also hold at 320 and 411 width.

### 3.1 The bar
- **Width:** `min(screenWidth - 32, 440)`, centred. That gives 328 at 360 wide and 352 on the M06.
- **Height:** 64 expanded, 52 compact.
- **Corner radius:** half the height (32, then 26).
- **Position:** the bottom edge sits `viewPadding.bottom + 12` above the screen bottom. With 3-button navigation it sits 12 dp above the system bar.
- **Inner padding:** 6 on every side.
- **Slots:**
  - The Start slot is 76 wide, or 68 when the screen is under 360.
  - The four tab slots share the rest equally: `(barWidth - 12 - startSlot) / 4`. That is 60 at 360, 66 on the M06 and 52 at 320.
  - Visual order: Today, Practice, Start, Review, You.
- **Tab slot contents:**
  - The icon is 24 x 24, with its top 11 dp below the bar's top.
  - A 3 dp gap, then the label: Hanken 12/16, w600, letter-spacing -0.1, one line.
  - The label always uses w600. Only its colour changes between states, so changing tabs never shifts the text.
  - Text scale is clamped at 1.2. Above that, `FittedBox(scaleDown)` shrinks the label, never clips it, and never wraps.
- **The lens (active indicator):**
  - Size: slot width − 4 by bar height − 12 (52 tall expanded, 40 compact).
  - Corner radius: half its height.
  - Centred on its slot.
- **The Start key:**
  - A volt stadium, 60 x 40 (compact 52 x 34), radius 20 (17), centred in its slot.
  - It shows the word **Start**: Hanken 15/18 w700 in `voltInk #0B1000` (compact 14). There is no glyph and no label underneath.
  - Its touch target is the whole slot (76 x 64).
- **Badges:**
  - Minimum 16 x 16. Two characters make it a stadium 22 wide.
  - Text: Hanken 11/14 w700, tabular figures.
  - Position: the badge's centre sits at the icon's top-right corner + (2, 1).
  - A 1.5 dp ring in the bar's tint colour separates it from the icon.
- **Dots** (when there is a state but no count): 8 dp at the same position, with the same ring.

### 3.2 The live capsule
- **Size and shape:** height 44, radius 22, width = bar width − 32, centred. Its bottom edge sits 8 dp above the bar's top.
- **Contents, left to right:**
  - 14 padding;
  - a 24 dp glyph;
  - a 10 gap;
  - one text line: the title in Hanken 14/18 w600 ink, then ", " and the detail in ink 2, ellipsised at the end. Truncation cuts the detail first; the title never truncates below 12 characters.
  - a 12 gap;
  - the action word: Hanken 14/18 w700, volt on Night (`#D2F000`), `#526700` on Daylight;
  - 16 padding.
- **Touch target:** the whole capsule is one target, 44 tall. That is under 48, so add 2 dp of invisible hit slop above and below to reach 48.

### 3.3 The scrim behind the bar (it replaces `DockScrim`)
- It runs from the bar's top − 40 to the screen's bottom.
- Gradient stops:
  - 0 at the top;
  - ground at 0.85 at 16 dp below the bar's top;
  - ground at 1.0 at the bar's bottom edge.
- **Why:** the upper half of the bar, where the icons sit, now shows blurred content moving behind the glass. The lower half, where the labels sit, is always over at least 85% ground, so labels keep 4.5:1 against the worst backdrop.
- When the capsule shows, the scrim starts 52 dp higher, with the same stops measured from the capsule's top.

### 3.4 Content clearance
- **`MmBarInsets`** replaces `MmDock.clearanceAbove`. Tab roots get `bottom padding = viewPadding.bottom + 12 + 64 + 20`, plus 52 while the capsule shows.
- The value changes only when the capsule appears or goes, never while the bar collapses, so scrolling never relayouts.
- Lists still end with their last row fully clear of the expanded bar.

### 3.5 Where the bar is not shown
- **Every route pushed on the root navigator.** That covers setup and loading pages, the runner and its submit page, NTA instructions, results and recap, repair and its ending, the stream, Learn, the tools, Ask, the You sub-pages and the lab. It also covers any time the keyboard is open (`viewInsets.bottom > 0`).
- **Under modal sheets and dialogs.** The bar stays put and drops to Lite (it already does).

---

## 4. Visual design and glass tiers

| Part | Night | Daylight |
| --- | --- | --- |
| Bar tint (Full) | `#1B1A16` at 0.72 | `#FFFDF8` at 0.80 |
| Bar tint (Lite) | `#1B1A16` at 0.92, plus a 64 dp noise tile at 3% | `#FFFDF8` at 0.94, plus noise at 2% |
| Bar tint (Off) | `#1B1A16` solid, hairline `#312E27` 1 dp | `#FFFDF8` solid, hairline `#D8D1C2` 1 dp |
| Edge light | 1 dp, white 16% at the top fading to 3% at mid-height | 1 dp, white 90% at the top fading to 0; hairline `#D8D1C2` at 60% around the shape |
| Shadow (one, analytic rounded rect) | 0 8 24, black 40% | 0 8 24, `#3A3020` at 12% |
| Lens | `#F4F0E6` at 10%, with its own 1 dp top edge (white 18% fading to 0). **No volt arc.** | `#FFFFFF` solid, shadow 0 1 3 `#17150F` at 10%, hairline `#D8D1C2` |
| Inactive icon and label | icon `#BDB6A6` (ink 2), label `#BDB6A6` | icon `#454036`, label `#454036` |
| Active icon and label | icon outline `#F4F0E6`, bubble filled `#D2F000`, label `#F4F0E6` | icon outline `#17150F`, bubble filled `#D2F000` with a `#526700` 1 dp rim, label `#17150F` |
| Start key | fill `#D2F000`, top highlight 1 dp white 35%, rim `voltEdge` 1 dp; a 14% volt glow 6 dp beneath (the bar's one lit element) | fill `#D2F000`, rim `#526700` at 45%, no glow |
| Badge | fill `#D2F000`, text `#0B1000` | fill `#17150F`, text `#F4F0E6` |
| Capsule | same tier and tint as the bar; glyph and progress arc in volt | same as the bar; arc in `#526700` |

**Glass tiers**
- **Full:** one `BackdropFilter.grouped` per surface (bar, capsule) inside the shell's existing `BackdropGroup`, each clipped to its own shape.
  - Filter: `ImageFilter.compose(outer: blur σ20, inner: colorFilter saturation 1.15)`. The saturation gives HIGH's "juicy" frost.
- **Lite:** no live blur; the tint and noise from the table.
- **Off:** solid.
- **Auto-downgrade:** the existing `GlassActivity` rule stays (Full to Lite when raster p90 stays above 12 ms for 2 s while scrolling).

**Icons**
> **Superseded 14 Oct 2026, 22:00 IST (owner: the custom icons "look extremely weird").** The bar now uses Material Symbols pairs, Rounded filled when active and Outlined at rest: Today `home`, Practice `quiz`, Review `fact_check`, You the initial as an avatar (a 22 dp ring at rest, a filled disc when active; `person` with no name). The active icon is volt on Night and ink on Day; at rest, icon and label are ink 2. Arrival: the fill starts after the lens passes 70%, fills over 200 ms and settles 0.9 to 1.0. Departure: empties over 160 ms on `Motion.out`. The filled glyph replaces the inked bubble everywhere below (reduced motion, colour-alone). The original paragraph is kept for history:

Custom 24 dp icons, 1.75 dp stroke, round caps, on a 2 dp grid. Each has an answer bubble of 8 dp diameter that inks when the tab is active. This is the "green dot" the owner liked, now built into the icon instead of floating behind it.
- **Today:** a ruled baseline with a bubble resting on it like a low sun, plus two short rays above. The bubble inks.
- **Practice:** a pencil at 45 degrees whose tip touches a bubble. The bubble inks.
- **Review:** a bubble with a tick. The bubble inks, then the tick draws in `voltInk` across it.
- **You:** the student's initial in Hanken 11 w700 inside a 16 dp bubble ring. Active, the ring fills volt and the initial turns `voltInk`. With no name, use Mobi's visor glyph.

Lucide `sunMoon`, `penLine` and `listChecks` are retired from the bar.

---

## 5. States and behaviour

### 5.1 Tabs
- **Tap another tab:**
  - `selectionClick`;
  - `goBranch`;
  - the lens travels (5.4);
  - the old icon's bubble drains and the new one inks;
  - the content fades through (5.4).
- **Re-tap the active tab:**
  - deep in the branch: pop to the root;
  - at the root: scroll to the top (the existing `tabReselectProvider`);
  - already at the top: nothing.
  - No haptic.
- **Scrub (kept: he called it "fluent and snappy"):**
  - Starts with a horizontal drag that begins on a tab slot. It never starts from the Start slot, and never inside `MediaQuery.systemGestureInsets.left/right`.
  - The lens follows the finger 1:1, with a `selectionClick` at each slot boundary.
  - The lens passes **under** the Start key: Start is drawn above it, so the lens visibly slides beneath and comes out the other side. While the lens is under it, Start dips to 0.97 scale.
  - On release, it lands on the nearest tab, projected by velocity × 80 ms. That tab opens.
- **Long-press a tab:** does nothing in P0. P1 option: TalkBack custom actions and app shortcuts cover the power paths instead of hidden trays.
- **Horizontal swipes on page content never switch tabs.** They would fight the week row, subject carousels and Android back.
- **Back:** from any tab root other than Today, back goes to Today; from Today it exits (unchanged). With predictive back the bar is part of the shell page, so it follows the gesture.

### 5.2 Start
- **Tap:**
  - `lightImpact`;
  - press scale 0.94 in 100 ms, with the volt deepening 16% toward `voltEdge`;
  - on release, the existing ink-ring spread (380 ms, kept);
  - the key morphs into the Start sheet (5.4).
- **Drag up from Start** (P0):
  - The sheet follows the finger, growing out of the key's rect.
  - A `selectionClick` when the drag crosses 35% of the open height.
  - On release it opens if past 35% or moving faster than 700 dp/s upward; otherwise it settles back on `Springs.smooth`.
- **Press and slide** (P1):
  - Holding Start for 350 ms opens the sheet under the finger, with `lightImpact`.
  - Sliding onto a row highlights it, with a `selectionClick` per row.
  - Releasing on a row starts it; releasing elsewhere leaves the sheet open.
  - The plain tap path is unchanged.
- **The breathing glow is removed.** "Something to resume" is now the capsule's job, stated in words.

### 5.3 Live capsule
One capsule at most. It is driven by a sealed `BarLive` state in `barLiveProvider`, built only from real state. Priority, highest first:

| State | Source of truth | Glyph | Text (title, detail) | Action | Ends |
| --- | --- | --- | --- | --- | --- |
| Sending | submit in flight (the real call, `submitStageProvider`) | three 5 dp bubbles inking in turn, one cycle per real stage (no loop) | "Sending your answers", "Accountancy mock" | none | "Saved at 11:51 PM" after the 200, for 3 s, then the next state |
| Marked | a received result not yet opened (`unopenedResultsProvider`) | a folded sheet with a volt foil dot | "Mock 8 is marked", "Accountancy" | Open | the result is opened |
| Resume | an open draft (`resumeDraftProvider`) | 20 dp ring, 2 dp, volt arc = answered / total | "Accountancy mock, 23 of 50", "41 min left" (minute resolution, from `endsAtWallMs`) | Resume | the session ends or is submitted |
| Offline with pending work | connectivity off and the sync queue not empty | a cloud with a slash | "Offline", "3 answers saved on this phone" | none | the queue drains (then "Synced" for 2 s) |

Other rules:
- The capsule never shows on Today while Today's hero is showing the same draft or the sealed sheet: `todayHeroCoversProvider(kind) == true`.
- **Swipe to dismiss:**
  - The capsule follows the finger horizontally.
  - Past 35% of its width, or faster than 600 dp/s, it slides out with a `selectionClick`.
  - It stays hidden until the next cold start or until its state changes. Resume is still in the Start sheet.
  - For Marked, Review gets an 8 dp dot until the result is opened.

### 5.4 Motion

Every animation below uses transforms, opacity or a painter, inside its own `RepaintBoundary`. None of it triggers layout.

| Moment | Spec |
| --- | --- |
| Lens travel | Two edges on two springs. The leading edge uses `edgeLead` (240 ms, bounce 0.14); the trailing edge uses `edgeTrail` (420 ms, bounce 0.04). The stretched lens thins up to 8% in height. Re-target from the current velocity if tapped mid-flight. |
| Anticipation | On press-down of an inactive tab, the near edge of the lens leans 0.18 of a slot toward it over 120 ms on `Motion.out`. On release, the full travel starts from there. On cancel, it springs back on `Springs.smooth`. |
| Icon arrival | The bubble inks with a circular mask growing from the side the lens came from, over 260 ms on `Motion.glide`. It starts when the leading edge passes 70% of the travel, so the ink lands with the light. The icon settles from 0.9 to 1.0 on a 420 ms spring with bounce 0.12 (calmer than today's 0.82 with a 28 degree turn). Review's tick then draws over 220 ms. |
| Icon departure | The bubble drains over 160 ms on `Motion.exit`, and the label colour cross-fades over 160 ms. |
| Content switch | The outgoing branch fades out over 90 ms. The incoming branch fades in over 200 ms on glide and slides 10 dp from the side of travel (transform only). Branches stay mounted. |
| Collapse (scroll down) | Triggered after 24 dp of cumulative user-drag scroll downward. Over 240 ms on `Motion.emphasized`: the bar's painted height goes from 64 to 52, bottom-anchored, by clipping (no layout); labels fade 1 to 0 over the first 120 ms; icons move down 6 dp; Start goes from 60x40 to 52x34; the lens follows; the capsule sinks 8 dp and fades to 0 over 150 ms. |
| Expand | On 8 dp of upward user scroll, at either end of the scroll extent, on a tab change, on a deep link and when the keyboard closes. 300 ms on `Motion.glide`. **No expansion on idle**, so the bar never moves while the student reads. A tap on a compact bar acts at once; it does not expand first. |
| First appearance (once per cold start) | The bar rises 16 dp and fades in over 300 ms on glide. Its items stagger left to right, 30 ms apart. Start comes last, with a 1.0 to 1.05 to 1.0 pop on `Springs.smooth`. |
| Capsule in | It rises from behind the bar: 16 dp to 0, scale 0.92 to 1, opacity 0 to 1, over 420 ms on `Motion.emphasized`. Its glyph, text and action stagger 40 ms apart. |
| Capsule out | It moves 12 dp down and fades over 200 ms on `Motion.exit`. Between states, the content cross-fades over 200 ms and the shape stays. |
| Start morph | A container transform from the key's rect to the sheet over 420 ms on `Motion.emphasized`. The volt cross-fades to the sheet surface over the first 30%. Sheet rows stagger in 45 ms apart after 160 ms. Closing reverses over 280 ms on `Cubic(0.3, 0, 0.8, 0.15)`. The existing `MorphSheetRoute` is kept and re-pointed to the new key rect. |
| Bar leaving for a pushed page | Driven by the shell page's `secondaryAnimation`: translate down 24 dp and opacity 1 to 0. Predictive back therefore scrubs it in and out with the finger. |
| Badge | Appears with scale 0.6 to 1 on `Springs.smooth` and a 160 ms fade. When the count changes, the digits roll over 300 ms. It never pulses or loops. |
| Keyboard | The bar slides down 24 dp and fades over 200 ms when the keyboard opens, and comes back over 300 ms. |

### 5.5 Haptics (through `hapticsProvider`; the user's Haptics switch turns all of them off)

| Event | Haptic |
| --- | --- |
| Tab change by tap; each boundary crossed while scrubbing | `selectionClick` |
| Re-tap the active tab | none |
| Start press | `lightImpact` |
| Drag-up crosses the open threshold; press-and-slide row change | `selectionClick` |
| Capsule tap | `lightImpact` |
| Capsule dismissed | `selectionClick` |
| "Saved" in the capsule | the success pattern, **only after the server's 200** |
| Badge appears or changes | none |

### 5.6 Badges: real counts only
- **Review:** the number of mistakes in tonight's repair, from `reviewIndexProvider.tonight.items.length`, until tonight's repair is recorded. Above 9 it shows "9+". If the Marked capsule was dismissed, an 8 dp dot shows instead until the result is opened.
- **You:** an 8 dp dot only when sign-in needs renewing, or when a sync has failed for more than 24 h.
- **Today and Practice:** never.
- **Start:** never. It is an action.
- No more than two badges or dots on the bar at once. Nothing counts streaks, credits or "new" content.

---

## 6. The Start sheet's contract (how it relates to the bar)

**Start means "go now".** One tap on a row starts work with good defaults; the only step left is the existing cost-confirm sheet when credits apply. **Practice means "choose".** The sheet never offers a choice Practice cannot also make, and it never browses.

Rows, top to bottom, five at most:
1. **The hero.** It shows one of these:
   - "Resume Accountancy mock, 23 of 50", when a draft exists;
   - otherwise **Tonight's move**, from the same `TonightPick` builder that feeds Today's hero, so the two can never disagree (REVIEW-ROUND1 finding).
2. **Quick 10.** Under it, a single row of subject chips (the student's practice-supported subjects, the current one selected). Changing a chip changes what Quick 10 starts. This fixes "starting from Business Studies redirects to Accountancy" by making the subject visible.
3. **Full mock** in the selected subject.
4. **NTA mode** in the selected subject. A "Pro" tag shows when the quote says so.
5. **Repair the next mistake.** Only when the hero is not already a repair.

Footer: one quiet text key, **"Choose your own in Practice"**. It closes the sheet (reverse morph) and switches to the Practice tab, so the lens travels as the sheet closes.

Ask moves out of the sheet to Review's header. The sheet keeps its Mobi corner and its title "Pick tonight's work" or "Pick today's work". Its visual polish (spacing, the solid nested cards from DEVICE-FINDINGS 1) belongs to the Practice area fixer. This spec owns only the morph, the row contract and the subject chip state (`startSubjectProvider`, defaulting to tonight's subject).

---

## 7. Accessibility

- **Semantics:**
  - The bar is `Semantics(container: true, explicitChildNodes: true)`. Each tab is `button: true, selected:` with label "Review, tab 3 of 4, 3 to repair tonight". Tabs are counted as 4; Start is not a tab.
  - Start: "Start. Opens quick start." Custom actions: "Resume Accountancy mock" when a draft exists.
  - Capsule: one node, e.g. "Resume Accountancy mock, 23 of 50 answered, 41 minutes left". Its custom action is "Dismiss", which replaces the swipe.
  - Compact state: labels are hidden visually but the semantic labels stay.
- **Order:** page content, then the capsule, then Today, Practice, Start, Review, You (`OrdinalSortKey`).
- **Targets:** every slot is at least 52 x 52 (compact) and normally 60 x 64. The capsule is 48 with its slop. Add `androidTapTargetGuideline`, `labeledTapTargetGuideline` and `textContrastGuideline` tests for the bar and the capsule.
- **Focus** (keyboard, D-pad, switch access): a 2 dp ring in ink (Night `#F4F0E6`, Day `#17150F`), offset 2 dp, following the lens shape. Arrow keys move between slots; Enter activates.
- **Contrast:**
  - Labels need 4.5:1 against the tint over the worst backdrop. With the scrim in 3.3 that is about 85% ground, giving Night ink 2 about 6.8:1 and Day ink 2 about 6.5:1.
  - Inactive icons need 3:1.
  - Recompute and record the figures in the test.
- **Text scale:** goldens at 1.3x and 2.0x. Labels scale down and never clip; the bar height stays fixed.
- **State is never carried by colour alone:** the active tab has the lens, the inked bubble and the ink label; badges have numbers.

**Reduced motion:**
- The lens jumps (no travel, no stretch, no anticipation); the bubble shows filled at once; the tick appears whole.
- The content switch is a 120 ms fade.
- Collapse and expand become a 120 ms cross-fade of the labels, with the height change applied instantly.
- The capsule fades over 120 ms with no movement.
- The Start morph becomes a 200 ms cross-fade.
- First appearance is instant.
- Scrubbing still works, snapping slot to slot.
- Haptics are unchanged (they are not motion).

---

## 8. Budget-phone cost (Galaxy M06, Mali-G57, about 2.0 dp-to-px)

- **Live blur:**
  - The bar: 352 x 64 dp, about 700 x 128 px.
  - The capsule, when shown: about 640 x 88 px.
  - Both sit in one `BackdropGroup` and share a single snapshot.
  - Under a sheet the bar drops to Lite (existing rule), so a sheet's animation never runs three backdrop passes.
- **Painters:** the lens and the icon ink are `CustomPainter`s with a `repaint:` listenable, in their own `RepaintBoundary`. The bar does not rebuild on lens frames.
- **Collapse:** a clip-and-transform painter. No `AnimatedContainer`, no layout, no `saveLayer`.
  - The label fade uses `Opacity` on a `RepaintBoundary`-wrapped row. Opacity on a small boundary composites as a layer; it does not re-raster.
- **Capsule:** the resume countdown repaints once a minute, not every second. The "Sending" bubbles repaint only during a real stage change.
- **Badge:** static until the count changes.
- **Targets:**
  - Bar raster cost p90 at or under 1.5 ms while flinging Today in Full.
  - Whole-frame raster p90 at or under 8 ms on Today (directions-final budget).
  - Lens travel and collapse add no UI-thread build frames beyond the first.
  - Measure with a profile APK and DevTools on the M06 and Vivo, Full forced and auto-downgrade off (REVIEW-ROUND1 open item).
- **Memory:** no new raster assets. Icons are paths; the noise tile already exists.

---

## 9. Migration plan

### 9.1 Code
- **Tokens:** `lib/core/theme/tokens.dart`: replace `MmDock` with `MmBar`. It holds `height 64`, `compactHeight 52`, `lift 12`, `pad 6`, `startSlot 76/68`, `startKey 60x40`, `capsuleHeight 44`, `capsuleGap 8`, `gutter 16`, `maxWidth 440`.
- **Widgets:** `lib/core/widgets/dock/` becomes `lib/core/widgets/bar/`:
  - `mm_bar.dart`: the bar, slots, collapse, scrub and first appearance. It replaces `split_dock.dart` and `dock_pill.dart`.
  - `bar_lens.dart`: the lens painter. It replaces `_LiquidTilePainter` and `lit_tile.dart`. The volt arc is removed.
  - `bar_icons.dart`: four custom icon painters with an `ink` progress (0 to 1) and `tick` progress.
  - `start_key.dart`: replaces `start_button.dart`. Keep the ink-ring painter; remove the breathing.
  - `live_capsule.dart` plus `bar_live.dart`: the sealed state and `barLiveProvider`.
  - `bar_badges.dart`: `barBadgesProvider` (Review count, Review dot, You dot). It replaces `reviewDotProvider`.
  - `bar_tabs.dart`: replaces `dock_tabs.dart`. It holds the four tabs, the `slotToBranch` map (visual slots 0, 1, 3, 4 map to branches 0, 1, 2, 3; slot 2 is Start) and the semantics labels.
  - Keep `morph_sheet_route.dart`.
- **`app_shell.dart`:**
  - Wire `MmBar` and `LiveCapsule`, the new scrim, `MmBarInsets` and keyboard hiding.
  - Drive the bar's exit from `secondaryAnimation`.
  - Delete `dockHiddenAt`; root routes already cover the shell.
  - Keep `BackdropGroup`, `StatusScrim`, the back rule and `tabReselectProvider`. `GlassActivity` and the Lite-under-modal rule stay.
- **`router.dart` and `routes.dart`:**
  - Add a fourth `StatefulShellBranch` holding `tabRoot('/you', youScreen, routes: [...])`. The You sub-pages keep `root: true`, so they still cover the bar and their paths do not change.
  - Remove the standalone `/you` root page and its `rise` transition.
  - `AppRoutes.tabRoots` becomes `[today, practice, review, you]`.
- **`tab_root_header.dart`:** remove `YouAvatarButton` from Practice and Review; Today keeps its date and greeting without the avatar. Delete `YouAvatarButton` or keep it for the lab only.
- **`main.dart`:** move the `reviewDotProvider` and `dockResumeKeyProvider` overrides to `barBadgesProvider` and `barLiveProvider` inputs (`hasUnopenedResultProvider`, `resumeDraftProvider`, the submit stage and the sync queue). Keep the default-null pattern so shells under test never open the session journal.
- **Start sheet (`quick_start.dart`):** apply section 6:
  - the hero from `TonightPick`;
  - subject chips through `startSubjectProvider`;
  - Ask removed;
  - the footer switches to the Practice branch.
- **Today:** expose `todayHeroCoversProvider` so the capsule can stand down.

### 9.2 Deep links and entry points
- `/you` now opens the You tab with the bar.
- `/you/*`, `/today/*`, `/practice/*`, `/review/*`, `/dashboard`, notification payloads and `action_router.dart` targets are unchanged. The test in 9.3 checks that each template still resolves.
- **New `/start` route (P1):** redirects to `/today` and sets `openStartSheetOnceProvider`, so the shell opens the sheet after the first frame. This is for Android launcher static shortcuts: "Resume", "Quick 10" and "Tonight's repair", each with its own query (`/start?row=resume`). Add the shortcuts in `android/app/src/main/res/xml/shortcuts.xml` (P1, after the core lands).
- **Website parity:** the bar's four places map to the website's Dashboard, Practice, Review/Progress and Profile.

### 9.3 Tests
- **Goldens** (`test/golden/core`, 360x780 and 384x853, Night and Daylight):
  - the bar on each of the four tabs;
  - compact;
  - with a Review badge "3" and "9+";
  - each capsule state (Sending, Saved, Marked, Resume, Offline);
  - Start pressed;
  - lens travel frames at 0, 40, 80, 130, 200 and 420 ms, Practice to Review across Start;
  - text at 1.3x and 2.0x;
  - width 320;
  - Full, Lite and Off;
  - the morph at 0, 30, 60 and 100%.
  - Re-render `quick_start_*`. Delete the `dock_*` goldens.
- **Unit tests:**
  - `slotToBranch`;
  - scrubbing skips Start and ignores the gesture-inset zones;
  - re-tap behaviour;
  - the back rule;
  - capsule priority and the Today stand-down;
  - dismissal lasts one app session;
  - badge rules (count, cap, dot after a dismissed Marked, none for Today and Practice);
  - reduced motion reaches the final states;
  - the keyboard hides the bar;
  - `MmBarInsets` changes only with the capsule;
  - semantics labels and order;
  - the tap-target and contrast guidelines;
  - the Start sheet and Today hero agree on `TonightPick`;
  - the subject chip changes what Quick 10 starts.
- **Router:** every `AppRoutes.templates` entry still resolves; `/you` builds inside the shell; runner, result, repair, setup and NTA paths build with no bar.
- **Device:** a screen recording at 90 Hz on the M06 (or the emulator within its 2 to 3 GB RAM rule) of:
  - tab taps and a scrub across Start;
  - collapse and expand on Today;
  - drag-up to open Start;
  - the capsule through resume, sending, saved and marked, from a real practice;
  - predictive back from a pushed page;
  - Daylight.
  - Then frame timings as in section 8. **Done means watching the recording, not only reading goldens.**

### 9.4 Order and coordination
1. Core and the foundation owner, landed as one change:
   - tokens, icons, lens, the bar, the shell wiring and the scrim;
   - the fourth branch;
   - removing the avatar from the headers;
   - goldens.
2. Then the capsule and badges.
3. Then the Start sheet contract, coordinated with the Practice fixer. They own the sheet's visual polish; this spec owns the row contract.

Feature fixers working in `lib/` now must not edit `lib/core/widgets/dock`, `app_shell.dart` or `router.dart` until step 1 lands. Any screen that read `MmDock.clearanceAbove` switches to `MmBarInsets` (`grep -rn "MmDock" lib`).

**Risk:** two parallel edits to `router.dart`. The foundation owner takes it for the duration of step 1.

---

## 10. Done check (owner's standards, section-by-section)

- **The visible change is large:**
  - one centred bar, not two objects;
  - You is on it;
  - custom icons with inking bubbles;
  - no volt arc;
  - glass you can see content move behind;
  - a capsule that speaks real state.
- **Balanced:**
  - four places and one action;
  - at most two badges;
  - no streaks;
  - no motion while the student is still;
  - no idle loops (the breathing is removed).
- **Robust:**
  - every capsule state comes from a real provider;
  - "Saved" and success haptics fire only after the 200;
  - the Start sheet and Today come from one `TonightPick`;
  - the subject is visible before Quick 10 starts.
- **Light and dark:** every colour in section 4 has both values, and the goldens cover both.
- **Accessibility and performance:** sections 7 and 8 pass on the device, and the recording has been watched.
