# Spacing, alignment and Night/Day audit

14 October 2026, against the system in `SPACING.md`. Method: every area's `_night` and `_day` goldens in `flutter_app/test/golden/<area>/goldens/` were laid side by side and looked at (about 330 states across 15 areas), plus `tmp/app-shots/now-1810.png`. Gaps were measured with a row scan (appendix) on the 384 x 853 goldens, 1 px = 1 dp. Files are under `flutter_app/lib/` and are the likely owner of the problem (found by reading the code behind the render). Section references (S3.2, S8.1 ...) point into `SPACING.md`.

Severity: **H** the owner will see it in the first minute of use or it breaks a rule everywhere; **M** visible inconsistency; **L** polish.

Not covered: motion (static goldens only; see `MOTION.md`), the NTA exam look (identical in both themes by design), the mascot and emblem galleries (art, not layout), live-device behaviour. Findings marked "(code)" come from reading the source, not from a render.

## Counts by area

| Area | H | M | L | Total |
| --- | --- | --- | --- | --- |
| Global (cuts across areas) | 5 | 7 | 1 | 13 |
| Today | 3 | 4 | 1 | 8 |
| Practice | 1 | 5 | 2 | 8 |
| Review (tab, repair, record) | 3 | 3 | 1 | 7 |
| You | 2 | 2 | 1 | 5 |
| Rhythm (RH) | 0 | 3 | 1 | 4 |
| Onboarding | 1 | 4 | 1 | 6 |
| Runner (mock and practice; NTA excluded) | 0 | 3 | 2 | 5 |
| Result | 1 | 4 | 1 | 6 |
| Tools (TL) | 0 | 3 | 1 | 4 |
| Insights | 0 | 1 | 2 | 3 |
| Learn | 0 | 2 | 1 | 3 |
| Notifications | 0 | 1 | 1 | 2 |
| Auth | 0 | 0 | 2 | 2 |
| Core (shared widgets, sheets, dock) | 0 | 2 | 2 | 4 |
| **Total** | **16** | **44** | **20** | **80** |

The first-screen answer to the owner's example: Today's move card is T1 and T2 below, fixed by `SPACING.md` S4.1 and S3.2.

---

## Global (G)

**G1 [H] Two gutters plus a +4 hack.** `lib/core/theme/tokens.dart` has `gutter` 16 and `cardGutter` 20. `cardGutter` is used by today (`screens/today_body.dart`), `review/widgets/review_state_view.dart`, `review/widgets/repair_entry_view.dart`, `review/screens/repair_ending_screen.dart`, `onboarding/screens/welcome_view.dart`, `result/recap/*`; the rest use 16; `you/widgets/you_page.dart:159,252,266` and `you/you_hub_screen.dart:198,252` use `gutter + 4` (`youText`), `you/hub/sheet_fields.dart:217` uses `side = gutter + 4`. Evidence: `tab_new_night` (hero card x=16) vs `today_ready_night` (hero card x=20); `review_tab_full_night` (hero text x=20, "Mistakes to repair" x=16); `hub_new_night` ("Subjects" block text x=36, "Milestones" x=20). Fix: S1.1: `gutter` 16 everywhere, `momentGutter` 24 for card-free moments, sheets 20, delete `gutter + 4`, `youText`, the 4 dp outer paddings (`rhythm/screens/milestones_screen.dart:170,183,214`, `rhythm/screens/bests_screen.dart:149`, `notifications/widgets/settings_sections.dart:105,243`, `you/subjects/subject_rows.dart:33,73`).

**G2 [H] Six different sub-page headers.** Stacked back-arrow row plus a 28/31 headline: `you/widgets/you_page.dart:152-160`, `tools/widgets/tools_page.dart:97` (`large ? type.headline : type.title`), rhythm pages; inline back plus 26/30 title: insights, learn, review (`review/widgets/page_header.dart`); plus `practice/widgets/practice_app_bar.dart`, and `_TopBar` in `auth/auth_page.dart:175`, `result/full/full_result_screen.dart:216`, `review/widgets/mistake_view.dart:235`. Evidence: `appearance_night` (title y=85, content starts y=127) vs `record_full_pro_night` (title y=41 inline). The stacked variant costs 44 dp of height on every page and sets the title in a heavier, tighter cut than the tab roots. Fix: S9: build `MmPageHeader` in `core/widgets/` (back 44, 12, `screenTitle`, trailing, row 56), migrate the six, keep the stacked large title only for moments.

**G3 [H] Letter spacing too tight, letters touch.** `core/theme/mm_type.dart`: `display`/`moment` -2.5%, `headline` -2%, `title` -1.5% on Bricolage cuts at 22 to 36 sp. Evidence: `appearance_night` ("Appearance and feel"), `stage_class12_night` ("Which CUET are you writing?"), `submit_ready_night` ("Submit now?"), `welcome_night` ("Every lost mark has a pattern."), `celebration_moments_night`, `delete_ask_night`. Fix: S9: headline -1%, display/moment -1.5%, title -1%, word spacing +0.5; re-check at the 130% goldens. This reads as "cheap" next to the clean Hanken body and is the quickest visible polish.

**G4 [M] Off-scale numbers still in the code.** Gaps: `SizedBox(height: 10)` x17 (`result/recap/sheet_share.dart:97`, `result/sheet/flap_faces.dart:72`, `runner/nta/nta_status_strip.dart:139`, `runner/widgets/runner_message.dart:166-170`, `review/widgets/mistake_view.dart:145`, `core/widgets/skeleton.dart:276-296`, `core/widgets/lab/lab_sections.dart`), `height: 3` x3 (`practice/widgets/composer_ticket.dart:489`, `tools/compass/programme_rows.dart:53`, `account_access/widgets/sign_in_methods.dart:230`), 22, 28 (`practice/widgets/result_states.dart:209`), 56 (`runner/widgets/submit_stage_view.dart:70`). Radii outside 28/24/18/12: 14 (`auth/code_slots.dart:290,306`, `rhythm/widgets/plan_week_strip.dart:313`, `tools/widgets/tools_parts.dart:23`), 16 (`practice/widgets/composer_parts.dart:159`, `composer_ticket.dart:459,519`), 20 (`insights/widgets/ask_messages.dart:85-87`, `tools/compass/category_score.dart:173,177`, `you/hub/sheet_fields.dart:160`), 22 (`practice/widgets/length_dial.dart:71`, `core/router/quick_start.dart:442`). Fix: map to the nearest token (S1, S2). The two most visible: `length_dial.dart` 22 -> 18 and `quick_start.dart` hero 22 -> 24.

**G5 [H] Day sheet scrim is taupe.** `core/theme/mm_colors.dart:217`: Day `0x425A4528` over cream gives about #CBC3B5. Evidence: `quick_start_deck_day`, `prompt_ask_day`, `time_sheet_day`, `privacy_events_day`, `sign_out_plain_day`, `confirm_*_day`: the page behind each Day sheet is a flat grey-brown, while Night keeps the page's warm dark. Fix: S8.4: Day `0x2E4A3A20` (18%) so the page stays cream; sheet shadow stays. Also `app_shell.dart:89` and `core/widgets/mm_sheet.dart:149,182` use the same getter, so one change.

**G6 [M] Day surface ladder is inverted for state surfaces.** Day `raised2` (#E9E4D8) is darker than the ground, so anything that uses it for "selected", "answer" or "correct" looks disabled. Evidence: `repair_explained_day`, `repair_key_review_day`, `result_open_answer_day` (the correct option is taupe, the wrong one is white); `run_card_shown_day` (the Answer card is a taupe slab); Night shows the same states as lighter-than-card. Fix: S8.1: add `MmColors.selectedSurface`; replace `raised2` reads on state surfaces in `review/widgets/answer_sheet.dart`, `review/widgets/question_panel.dart`, `learn/widgets/run_step.dart`, `practice/widgets/result_question_card.dart`.

**G7 [M] Hit targets laid out as padding.** `core/widgets/show_me_pill.dart:39` (height 48, visual 32), `core/widgets/controls/segmented.dart`, quiet `KeyButton`, filter chips: each adds about 8 dp of phantom gap above and below. This is why every Today and Review card reads gappy even when the coded gaps are small. Fix: S3.3, a `MmHitSlop` wrapper (hit region outside layout), visuals at 32/40/44.

**G8 [M] Figure leading inflates every number box.** `features/today/widgets/today_type.dart:25-27` (`stageNumber` 124 sp on 104 dp), `core/theme/mm_type.dart` (`hero` 112/96, `figure` 52/50, `countdownFigure` 76/68). The "4" on Today is 82 dp of ink in a 104 dp box. Visible gaps above and below the number are 25 and 29 dp against coded 8 and 12. Fix: S3.3 (`TextHeightBehavior` with first-ascent and last-descent off, line 0.9) and rebase the gap table. Touches `core/widgets/monumental_number.dart` and every use of the figure styles.

**G9 [M] Parity coverage gaps in the goldens.** 22 result goldens exist only for Night: `card1_first`, `card1_held`, `card1_higher`, `card1_lower`, `card1_reveal_mid`, `card4_first`, `card4_share`, `compact_card1`, `compact_sealed`, `full_answers`, `full_blanks_folded`, `full_blanks_open`, `full_loading`, `large13_card2`, `large13_card3`, `large13_card4`, `large_card1`, `large_card4`, `sealed_unfold25`, `sealed_unfold80` (night only), and `compact_card4_day`, `large13_full_top_day` (day only). Runner motion frames (`motion_lock_in_*`, `motion_next_*`, `motion_palette_wave`) carry no theme suffix. So the whole result reveal's Day look is unverified, and it is the app's biggest moment. Fix: pair them in `test/golden/result/` and suffix the runner frames.

**G10 [M] Content half-hidden under pinned bars.** A row or chip is cut by a pinned bar with no fade and no bottom padding: `confirm_mock_*` (line "Water, pencil, rough sheet" cut at the footer), `finish_settled_*` and `result_mixed_*` (first wrong-answer row half visible under "Repair these 3"), `today_ready_text130_*` (a "Show me" chip sliver above the key), `today_returning_*` (chip 6 dp above the bar), onboarding steps (last option row faded to 30% under Continue). Fix: S4.5, one `MmBottomBar` with a 24 dp fade and content padding of bar height + 16; adopt in `practice/widgets/confirm_sheet.dart`, `practice/widgets/finish_stage.dart`, `result_foot.dart`, `today/screens/today_body.dart` (`_StickyScrim`, fade 24 -> 40), onboarding `step_scaffold`.

**G11 [H] Moments top-stack and leave a hole above the pinned action.** Measured longest empty band at 853 dp: `goal_night` 256, `sealed_folded_night` 240, `repair_ending_nothing_night` 232, `card4_night` 232, `save_night` 224, `stream_question_night` 224, `repair_entry_night` 192, `mock_answered_night` 192 (this last is by design). Fix: S7 `MomentScaffold` (flex 2 above, flex 3 below, pinned `MmBottomBar`). Per-screen entries below (R4, R5, X1, X3, O6).

**G12 [M] Pale-ink rows of the same kind drawn differently: subject plates.** Practice tiles (white raised card with art, `practice/widgets/subject_tiles.dart`), You hub tiles (`you/hub/sheet_fields.dart`, dark field tiles), Core subjects (`core/widgets/subjects` goldens `subjects_*`, gradient tiles). Evidence: `tab_new_day`, `hub_day`, `subjects_day`. Fix: one `SubjectPlate` (S8.4).

**G13 [L] Raw colours outside the theme.** 25 files paint `Color(0x...)` or `Colors.white/black` outside `core/theme`, `core/art`, `core/mascot` (list in S8.4). No visible defect found in the renders reviewed, but none carries a documented Day counterpart. Fix: per-file role mapping during the pass; start with `practice/widgets/choice_glyphs.dart` and `today/widgets/today_tones.dart`.

---

## Today (T)

**T1 [H] The subject art is stuck to the top and crammed against the label; the card has dead space around "4 to repair today".** Images: `today_ready_{night,day}`, `today_ready_5min`, `today_morning`, `today_practice`, `today_error` (art absent). `today/widgets/hero_stage.dart`: art box 212 x 212 at `top: -44, right: -44`, emblem 168 centred (`heroEmblemSize`, `heroParallax` 0.12 which travels another 25 dp), so the visible emblem spans card y -22 to 146 and is cropped by the top edge; the number row's label "to repair tonight" starts at y about 130 right under the emblem with 0 to 4 dp of air, while the card's right column beside the number and below the emblem is empty. Same recipe in `review/widgets/tonight_card.dart:119-126` (168, cropped), `today/widgets/resume_hero.dart`. This is the owner's example. Fix (S4.1): `heroArtWidth = heroArtHeight = 156`, replace `heroArtBleed` with `heroArtTop = 8` and `heroArtBleedRight = 10`, `heroEmblemSize = 136`, `heroParallax = 0.05`, `heroArtClear = 158`; keep the Positioned art centred on the title-to-number band; the label sits beside the number, bottom-aligned to the baseline.

**T2 [H] Uneven rhythm inside the hero.** `today_ready_night`: visible whitespace overline to title 10, title to number 25, number to meaning 29, meaning to Show me 25, Show me to the length control 25, control to key 15, key to the card bottom 8 plus the quiet row. Coded 8/12/12/16/20 in `today/widgets/move_hero.dart:96-179`. Causes: figure leading (G8), 48 dp hit boxes (G7), `EdgeInsets.fromLTRB(20, 20, 20, 8)` bottom padding at `move_hero.dart:130`. Fix: S3.2 table; bottom padding 20; `show_me_tag.dart` and the length control through `MmHitSlop`; remove the `padding: bottom 14` baseline hack in `today/widgets/number_block.dart:79`. Expected card height 365 -> about 325.

**T3 [H] The header stack eats a third of the first screen.** Hero top is at y 283 of 853 in every Today golden. Rows: avatar row 56, 20, "1 of 4 study days" row about 40, 12, weekday letters, 10, bubbles, 20, legend row ("Counted, Planned, Rest"), 24, hero (`today/widgets/today_header.dart:48`, `week_ledger.dart`, `screens/today_body.dart` `SizedBox(height: MmSpace.s24)`). On a 360 x 640 phone the key is below the fold and the pinned bar has to stand in. Fix: header to week 12, drop the legend row except when a "Not counted" or rest state is on screen (it moves into the week sheet), merge "3 more by Sunday" onto the count row (already there), header to hero 16; target hero top <= 225 (S3.1).

**T4 [M] Pinned bar clips chips (also G10).** `today_ready_text130_{night,day}`: sliver of the "Show me" chip above the key; `today_returning_*`, `today_late_night_*`: the chip sits 6 dp above the bar edge. `today/screens/today_body.dart`: `_StickyScrim._fade = 24`, `_barPad = _scrimRise = 48`. Fix: fade 40; while pinned, hide the card's chips with opacity 0 under the bar or add `MmBottomBar`'s content inset.

**T5 [M] Resume hero wraps the title and drops the unit.** `today_resume_{night,day}`: "Mock 8, Accountancy" wraps to two 28/31 lines (art clear 140 + `_titleAirBesideArt` 16 in `move_hero.dart:60`), "23" with "of 50 answered" stacked under with 29 dp of gap because the beside-width check fails. Fix: T1 shrinks the art column (158 -> label fits beside "23" when the label is one line "of 50 answered"); title style `headline` 28 -> `title` 22 when the move subject has two words.

**T6 [M] Header height jumps when connectivity changes (code).** `today/widgets/today_header.dart:45-57`: the "Updated 7:30 PM. You are offline." row adds 18 dp (`today_offline_*`: week strip moves from y 170 to 188), so a Wi-Fi flip shifts the whole page. Fix: S3.3: reserve the 18 dp always (opacity 0), or overlay it on the status bar line.

**T7 [M] The Mobi variants and the object variant have different header bands.** `today_day_one_*`, `today_returning_*`, `today_late_night_*` (Mobi 96 dp at the left, bubble at the right, title under) against `today_ready_*` (emblem at the right, title at the left): the band is about 130 dp in one and about 150 in the other, and the number starts at a different y, so when a refresh swaps the state the card changes height and the number jumps. Fix: S4.1.7: both variants use the same 156 dp band and the same y for the title and the number.

**T8 [L] Section gaps are 40 and 32 mixed.** `screens/today_body.dart`: `MmSpace.s40` before "Your sheet", `s32` before the road (or `s40` when no sheet). Visible: `today_ended_night` "Recent papers" starts 55 dp below the pinned-move row, `today_road_night` colleges heading 80 dp below "About 100 study sessions". Fix: S3.1, 32 with a rule.

---

## Practice (P)

**P1 [H] Practice's "move" card is a second, denser implementation of the Today hero.** `tab_new_{night,day}`, `tab_resume_*`, `tab_chapter_late_*`, `tab_offline_*` (`practice/widgets/suggestion_hero.dart`): art 44 dp at the left, Mobi 36 dp at the top right (two characters in one card, breaks S5), the body copy wraps to three lines in a 168 dp column beside a 92 dp Start pill, Start is not the full-width key. The Today card is airy and full-width; this one is crowded. Fix: build both on the same hero composition (S4.1): emblem band on top, body full width, key full width; drop the small Mobi (keep it in the header only when the card has an emblem).

**P2 [M] Gap between the hero and "Choose your own" is 65 dp.** `tab_new_night`: card bottom y 200, heading y 265 (longest void 64). `practice/practice_screen.dart` / `practice_composer.dart`. Fix: group gap 24 below the hero then the heading (no rule needed), or section gap 32 with rule.

**P3 [M] Three heading styles in one scroll.** `tab_choose_concepts_night`: "Exam conditions" is a 13 sp caption, "In Accountancy" is a 15 sp label with an icon, "Explore and plan" and "Concepts" are 22 sp titles; sections are separated by 40, 24 and 56. Files `practice/widgets/mode_list.dart`, `more_rows.dart`, `concepts_shelf.dart`. Fix: two levels only: section title 22 (with the rule and 32 gap) and group label 15 w600 `ink2` (12 below); sub-groups inside a section use the group label with 12 above.

**P4 [M] Confirm sheet content is cut by the pinned footer (G10).** `confirm_mock_*`, `confirm_chapter_credits_*`, `confirm_quick_free_*`: a half line of text above the key. `practice/widgets/confirm_sheet.dart`. Fix: `MmBottomBar`.

**P5 [M] Finish and result stack seven blocks, then a half row under the bar.** `finish_settled_*`, `finish_stamp_*`, `result_mixed_*`, `result_all_correct_*`: headline 112, summary, dot card, Mobi with bubble, marks bar and caption, "Practice finished. Recorded at 11:51 PM." row, "That is a good place to stop for tonight. Dismiss" row, then "Wrong answers (3)" with a half-visible row under "Repair these 3". `practice/widgets/finish_stage.dart`, `result_foot.dart`, `result_list.dart`. Fix: merge the receipt and the stop line into one receipt row; Mobi row 24 gap instead of 32+; bottom padding bar + 16 (G10).

**P6 [M] The Questions length dial mis-aligns baselines and uses radius 22.** `setup_chapters_hard_*`, `setup_credits_low_*`: the selected cell's numeral (15) is larger than its neighbours and sits 4 dp higher than the 5 and 10; the dot matrices under them are not baseline-aligned. `practice/widgets/length_dial.dart:71`. Fix: same numeral size, selected state = surface and ring (S8.1), align numerals to a shared baseline, radius 18.

**P7 [L] Quick-start deck cards leave a hole beside the art.** `quick_start_deck_*`, `quick_start_deck_resume_*`: 260 dp cards, art top right, title bottom left, 100 dp of empty card above the title. Same pattern as T1. `practice/widgets/quick_start_deck.dart`, `core/router/quick_start.dart:442`. Fix: card height 180, art 136 in the band, title to the left of it.

**P8 [L] Horizontal subject row is clipped hard at the screen edge.** `tab_new_*`: "More subjects" tile is cut at the right edge with no fade; label baselines differ by 2 dp between tiles (Accountancy y 408, English y 410). `practice/widgets/subject_tiles.dart`. Fix: 24 dp edge fade (`insights/widgets/edge_fade.dart` exists), label anchored at the plate bottom.

---

## Review (R)

**R1 [H] The Review hero is full-bleed with a different gutter, and the art is cropped by the screen edge.** `review_tab_full_*`, `review_tab_*`, `review_tab_late_*`, `review_tab_text130_*` (`review/widgets/tonight_card.dart`): text at x=20, the list under it at x=16 (G1); no card edge, so the calculator emblem (168, `tonight_card.dart:126`) is cut by the screen. Fix: render it in the shared hero (S4.1) at gutter 16.

**R2 [H] Two characters and a 96 dp Mobi-plus-key row.** Same images: the calculator emblem at the top right, plus Mobi (96 dp, `tonight_card.dart:201-206`) left of the Start pill; gaps chips to Mobi row 70 dp, Mobi row to "Mistakes to repair" 60 dp. Breaks S5 and makes the hero 560 dp tall. Fix: drop Mobi from the hero (keep it in the empty and all-clear states), Start full-width key under the chips with 16, section gap 32. Expected hero height 560 -> about 400.

**R3 [M] Hero title wraps to three lines to clear the art.** `tonight_card.dart:148` right padding 140 (72 when `large`), title `headline` 26/29: "Partnership: admission of a partner" takes three lines, 87 dp. Fix: title style 22 on two lines with the 158 clear (T1), or truncate the chapter to "Partnership" with the full name in the evidence tag.

**R4 [H] Repair entry hole.** `repair_entry_{night,day}`: content ends at y 447 (the thread and "Checked and Holds come later"), the credit line and Begin sit at y 628 to 700: 192 dp of nothing in the middle; Mobi (56) again sits left of Begin. `review/widgets/repair_entry_view.dart`. Fix: `MomentScaffold` (S7); Begin full width; the credit line moves directly under the thread (24 gap); Mobi leaves the bottom bar and joins the header band (the speech line replaces the bubble).

**R5 [M] Repair ending: 232 dp hole.** `repair_ending_nothing_*`, `repair_ending_more_*`, `repair_ending_first_*`: sheet of bubbles, headline with Mobi, thread, then a hole, then the receipt and "Share a card" just above the key. `review/screens/repair_ending_screen.dart`, `review/widgets/ending_sheet.dart:61` (padding 20/18/20/22). Fix: S7; receipt directly under the thread (24); only the key and "Finish for tonight" are pinned.

**R6 [M] Correct option is taupe in Day (G6).** `repair_explained_day`, `repair_key_review_day`, `repair_retry_short_day`. `review/widgets/answer_sheet.dart`. Fix: selectedSurface plus 2 px ink border, volt glyph (as Night).

**R7 [L] Thread rail and rows start on different edges.** `review_mistakes_*`: the rail dot is at x=41, the row text at x=68, the group heading at x=14 and the group icon at x=40. `review/widgets/mistake_view.dart`, `review_rows.dart`. Fix: rail dot on E1 + 8, row text on E2, heading on E0 (S1.2).

---

## You (Y)

**Y1 [H] Identity block is inset 20 dp deeper than everything around it.** `hub_new_*`, `hub_*`, `hub_loading_*`, `hub_full_page_*`: Course, Colleges and Subjects text at x=36 (`you/hub/sheet_fields.dart:217` `side = gutter + 4` on top of the page's 16), "Milestones", "See all" and the Mobi header at x=20. The block has no visible card, so the indent reads as misalignment. `you/you_hub_screen.dart:117,134,198,252`. Fix: S1.1: the block is a Plain card (padding 16) at E0, or flat text at E0; nothing at 36.

**Y2 [H] Sub-page titles are heavy, tight and 4 dp off the cards (G2, G3).** `appearance_*`, `account_*`, `help_*`, `privacy_*`, `goal_*`, `subjects_*`, `sheet_editor_*`: title text x=20 over cards at x=16 (`you_page.dart:159`, `gutter + 4`), set in the 28/31 headline cut. Fix: `MmPageHeader`.

**Y3 [M] Ghost keys have no edge on Day.** `privacy_minor_day` ("See every event we collect", "Change my answer"), `sign_out_plain_day` ("Sign out"), `delete_ask_day` ("Request deletion"): white pill on cream, no hairline, only a faint shadow. Night's raised pill has the edge light. `core/widgets/key_button_face.dart` (ghost). Fix: S8.2: 1 dp `line` in Day (Night keeps the edge light).

**Y4 [M] The week ring on the hub starts a new text edge.** `hub_*`, `hub_new_*`: the ring (96 dp) and its text column ("This week", "3 more study days to reach your goal.") start at x=36 with the text at x=147, while the Course row text starts at x=36 and the milestones shelf at x=20. Three edges in 200 dp. Fix: S1.2: ring on E1, text column at E1 + 112 (ring 96 + 16), with the Course and Colleges rows on E1.

**Y5 [L] The lit edge is visible on Night and nearly invisible on Day.** `account_free_*`, `account_pro_*`, `hub_*` (and Tools: `hub_*`, `compass_full_*`): the volt top edge on the one focal card is a clear line on Night; on Day it is a faint olive hairline on a white card, so the "one lit element" rule is only met on Night. `core/widgets/materials/` (the lit edge). Fix: S8.3: Day lit edge is `accentText` at 70%, 1.5 dp, with the 14% volt glow beneath.

---

## Rhythm (RH)

**RH1 [M] Stat figure and label are 24 dp apart.** `rhythm_screen_top_*` "Your run": "3" and "6" at 40 sp, labels "weeks in rhythm", "best run, weeks" 35 dp below (the figure box is 40 high, the label sits after a 20 dp gap in `rhythm/screens/rhythm_screen.dart`). Fix: S4.2: label 4 dp under the figure box (after G8 trimming).

**RH2 [M] Milestones: section gaps of 55 to 70 dp and a 64 dp coin header against 36 dp rail coins.** `milestones_list_*`, `milestones_empty_*`, `milestones_complete_*`: divider, then 50 dp, then the section header; between sections 70 dp. `rhythm/screens/milestones_screen.dart:170-214` (4 dp outer padding, G1). Fix: section 32 with rule, heading 12; header coin 48 with 12 to text; rail coins 36 on E1 + 8.

**RH3 [M] Plan rows and pause rows are 48 dp with 16/20 mixed padding and a different divider start.** `rhythm_screen_scrolled_*`: "Weekly goal", "Study days", "This week", "2 weeks", "About 3 months": padding left 16, divider full width. `rhythm/screens/rhythm_screen.dart`. Fix: S4.3 (divider from E2 or none for text-only rows).

**RH4 [L] Celebrations pill group (`Full | Quiet | Off`) is 44 tall with 4 dp inner gap; every other segmented control is 48 (Appearance).** `rhythm_screen_scrolled_*` vs `appearance_*`. Fix: one `MmSegmented` height 44 visual.

---

## Onboarding (O)

**O1 [H] The "today" bubble is olive on Day and volt on Night.** `first_move_{night,day}`, `first_move_practice_*`: `onboarding/widgets/week_ahead.dart:78`, `week_track.dart:27` use `isNight ? volt : accentText` for the filled mark; the Today tab's week ledger uses volt fill both themes. Fix: S8.3: filled marks are volt on both, `accentText` only for text and strokes; also check the other `isNight ? volt : accentText` sites: `answer_sheet_card.dart:325`, `choice_tile.dart:110,214`, `course_grid.dart:94`, `hold_to_seal.dart:99`, `pace_line.dart:65`, `plan_sheet.dart:136,407`, `subjects_step.dart:97`, `worry_step.dart:79`.

**O2 [M] The step-1 sheet card is 183 dp tall; the choices fall below the fold.** `stage_class12_{night,day}`: sheet card y 87 to 270, title 305, first choice 450; only two of four choices fit above the pinned Continue and the last row fades. Steps 2 to 7 use a 40 dp dots card (`course_grid_*`, `subjects_*`). `onboarding/widgets/answer_sheet_card.dart`. Fix: the large card only for the cold reveal (first 1.2 s) then collapses to the 72 dp variant; steps keep one header height.

**O3 [M] "Tomorrow at 8:00 PM" is an unframed centred line between the card and "Your first week".** `first_move_*`, `first_move_practice_*`: 28 dp under the card, 80 dp to the next block (longest void 80), and no affordance (it is a control). `onboarding/steps/first_move_step.dart`. Fix: ghost key (48, `line` border, 8 under the primary), section gap 24 to "Your first week".

**O4 [M] Save step is top-stacked with a 224 dp hole.** `save_{night,day}`, `after_sign_in_saved_*`: sheet card, age chips, "Not now", then nothing (fill 0.58). `onboarding/screens/save_view.dart`. Fix: `MomentScaffold`; "Not now" pinned as the quiet key; Google and email keys pinned above it.

**O5 [M] Step titles collide with their subtitle.** `subjects_*` ("Your subjects. How solid is each, honestly?" two lines at 28/31 with -2% tracking, 8 dp to the subtitle), `rhythm_*`, `worry_*`. G3 plus: title to subtitle 4 -> 8, title style `headline` -> `title` 22 for two-line step questions (keep `headline` for one-liners).

**O6 [L] Plan sheet leaves 80 dp between the sheet card and the Hold to seal key.** `plan_*`: card bottom y 565, key y 646 (pinned). Acceptable; included so S7 is applied here too (no fixed top stack).

---

## Runner (N) (NTA excluded)

**N1 [M] The "Questions" chip differs in weight between themes.** `mock_first_{night,day}`, `practice_first_*`, `palette_*`: Night chip is dark glass with a dim label (about 3:1) and no border; Day is a white pill with a hairline. `runner/widgets/runner_top_bar.dart`. Fix: both a 1 dp `line` border, label `ink`.

**N2 [M] The "of 50" unit is 10 to 11 sp.** `mock_first_*` ("1 of 50"), `practice_first_*`: below the 12 sp floor and smaller than the 20 sp timer beside it. `runner/widgets/runner_top_bar.dart`. Fix: unit 12 sp w600 `ink2`, top-aligned to the figure (S4.2).

**N3 [M] Question to options void on short questions.** `mock_answered_*`, `mock_first_*`, `practice_first_*`: 150 to 190 dp between the stem and the first option (options are pinned to the thumb zone by design in `runner/widgets/runner_layout.dart`; keep that, the brief says options never move). Make the void useful rather than empty: in practice, "Marks come after you submit" and "Mark for review" sit 16 dp under the stem instead of floating beside the top bar; verify on 360 x 640.

**N4 [L] Palette legend wraps to two rows with mixed icon sizes.** `palette_*`: "Not answered 3 / Not visited 26 / Marked 3" then "On this phone 2". `runner/widgets/palette_sheet.dart`. Fix: 2 x 2 grid, icons 16.

**N5 [L] In the NTA instructions golden the headings render as black bars.** `nta_instructions_pro_{night,day}`: a font that the golden harness does not load (the test font box). Test fix, not a product bug: load the heading font in `test/golden/practice/` harness. (The NTA look being identical in both themes is intentional.)

---

## Result (X)

**X1 [H] The sealed sheet sits in the lower half with a 240 dp hole above it.** `sealed_folded_{night,day}`, `sealed_unfold50_*`: headline and one line at the top (y 100 to 132), the sheet at y 350 to 700, keys at 740: longest void 240. `result/recap/sheet_stage.dart`. Fix: S7: centre the sheet in the free band between the title and the key stack (equal 24 to 40 above and below).

**X2 [M] The sealed sheet has almost no edge on Night, and a hard grey strip on Day.** Night: sheet #1B1A16 on a #12110E ground with a black desk shadow (invisible); Day (`sealed_unfold50_day`): a hard 8 dp strip under the sheet at y 697 to 705. `result/sheet/folded_sheet.dart:180-195` (`_DeskShadow`: 0.4 black, blur 40 offset 16, plus 0.16 at blur 6). Fix: S8.2: Night adds the `edgeTop` light and a 6% lamp rim; Day shadow is `0x1F2A2010`, blur at least 24, drawn without a clip (give the layer 40 dp padding).

**X3 [M] Result recap cards 3 and 4 leave 160 to 232 dp holes.** `card3_*` (hole 160 above the key), `card4_*` (232): content top-stacked, key pinned (G11). `result/recap/card_page.dart`. Fix: S7.

**X4 [M] Night-only result goldens (G9).** 22 files; the Day look of the reveal, the lower and held results, the share card and the full result is unverified. Add pairs.

**X5 [M] Emblem sizes differ per screen.** `full_top_*` (64 dp calculator), Today (168), Review (168), Practice tile (56), result card 3 Mobi 72. Fix: S4.1: 24 / 40 / 56 / 136 only.

**X6 [L] Full result: the "Continue recap, card 3 of 4" link, the submitted line and the number sit at 8, 12 and 20 dp spacing.** `full_top_*`: link y 89, caption y 125, number y 150. `result/full/full_result_screen.dart`. Fix: link 12 under the header, caption 8, number 12.

---

## Tools (TL)

**TL1 [M] Compass has two lit surfaces.** `compass_full_*`, `compass_score_full_*`: the hero card has the volt top edge and the "Category and score" row has an olive-tinted border and fill (`tools/compass/category_score.dart:173-177`, radius 20, alpha 0.4 edge). Breaks S5. Fix: the row becomes a Plain card with a `line` border; the tint goes.

**TL2 [M] Stacked heavy titles (G2).** `hub_*`, `combo_full_*`, `compass_full_*`, `programme_bcom_*`, `guide_full_*` (`tools/widgets/tools_page.dart:97`). Fix: `MmPageHeader`.

**TL3 [M] Chip rows cut at the screen edge with no fade.** `compass_full_*` ("General Aptitude Test +3" loses its "+3"; filter row "All, Commerce, Humanities, Sc..."), `compass_score_full_*`. `tools/compass/compass_screen.dart`. Fix: edge fade 24 dp, or wrap the first chip row.

**TL4 [L] Radii 14 and 20 on tool cards.** `tools/widgets/tools_parts.dart:23`, `tools/compass/category_score.dart:173`. Fix: 18 and 24 (G4).

---

## Insights (I)

**I1 [M] The question stream pins Skip about 220 dp under the options.** `stream_question_*`, `stream_wrong_*`, `stream_right_*`: options end near y 440, Skip sits at y 700 (longest void 224). `insights/screens/stream_screen.dart`. Fix: keep the pin (stable thumb position); put the Save, vote, Ask why row 16 under the options, and set the question to 18/28 so a short stem fills more of the screen.

**I2 [L] Insights "Ask Mobi" rows and cards use radius 20 and padding 20 (bubbles) next to Plain cards at 16.** `ask_start_*`, `ask_conversation_*`: `insights/widgets/ask_messages.dart:85-87,261`. Fix: bubble radius 18, padding 12 / 16.

**I3 [L] `entries_*` card: body copy line height is 18 where body is 16/24.** `insights/widgets/ledger_hero.dart`. Fix: body style, S4.3.

---

## Learn (E)

**E1 [M] Two intro blocks before the one action.** `learn_tab_full_{night,day}`: a 2-line paragraph, then "How Concepts work" and 2 more lines, 150 dp of copy above "12 cards due" (`learn/screens/learn_screen.dart` near line 360, `widgets/screen_bits.dart`). Fix: the "How Concepts work" block shows only on the first visit (it is the first-visit state already); keep one 2-line intro.

**E2 [M] Answer card is taupe on Day (G6).** `run_card_shown_day`, `run_changed_day`, `run_choice_picked_day`: `learn/widgets/run_step.dart`. Fix: selectedSurface.

**E3 [L] Unit page: the first title is 24 sp crushed and the offline banner has 12 dp padding while the title below it has 20.** `unit_read_*`. Fix: G3 and banner padding 16.

---

## Notifications (F)

**F1 [M] Day sheet scrim (G5).** `prompt_ask_day`, `time_sheet_day`: grey-brown page behind the sheet. Fix: G5.

**F2 [L] The permission explainer has three text weights in 190 dp.** `prompt_ask_*`: title 22, lead 18/26, "What they would say" 13, three rows 14 with 8 dp row gaps, a quiet footnote. Fix: drop the lead (the rows say it), rows 12 gap.

---

## Auth (A)

**A1 [L] Sign-in stack touches both ends.** `sign_in_empty_*`, `sign_in_error_*`, `code_partial_*`: Mobi 200 dp, headline, subtitle, tabs, field, key, footnote fill the screen (the footnote is at y 700 to 718) and the error line pushes "Send code" down 28 dp (`sign_in_error` vs `sign_in_empty`). Fix: reserve the error line's 28 dp always.

**A2 [L] Code cells 14 radius, 28 wide.** `code_partial_*`: `auth/code_slots.dart:290,306`. Fix: radius 12, 44 tall.

---

## Core (C)

**C1 [M] Quick-start sheet: card, tiles and rows use four paddings.** `quick_start_{night,day}`: hero card 20, tiles 16, "Repair the next mistake" row 16, "Ask Mobi" row 12; gaps between them 12, 16 and 8. `core/router/quick_start.dart`. Fix: Plain cards 16, item gap 12, side padding 20.

**C2 [M] Core subject grid, Day vs Night plates differ (G12).** `subjects_day` is pastel gradients with no card edge; `subjects_night` is dark fields. Fix: `SubjectPlate`.

**C3 [L] Skeleton heights are literals (G4).** `core/widgets/skeleton.dart:276-296`. Fix: scale.

**C4 [L] Dock to content: last row sits 24 dp above the dock in `surfaces_*`/`dock_today_*`; `DOCK.md` section 3.4 changes the clearance.** Apply `MmBarInsets` everywhere instead of `MmDock.clearanceAbove`, and re-baseline the goldens.

---

## Appendix: the row-scan script

Used for every measured gap in this audit (Python 3 with Pillow and numpy; run from `flutter_app/test/golden`).

```python
from PIL import Image
import numpy as np

def bands(path, x0, x1, y0=0, y1=None, thr=38):
    im = np.asarray(Image.open(path).convert('RGB')).astype(int)
    y1 = y1 or im.shape[0]
    strip = im[:, x0:x1, :]
    out, cur = [], None
    for y in range(y0, y1):
        row = strip[y]
        d = np.abs(row - np.median(row, axis=0)).sum(axis=1)
        on = (d > thr).sum() >= 2
        if on and cur is None: cur = y
        if not on and cur is not None: out.append((cur, y - 1)); cur = None
    return out

prev = None
for s, e in bands('today/goldens/today_ready_night.png', 24, 150, 60, 700):
    print(s, e, 'h', e - s + 1, '' if prev is None else f'gap {s - prev - 1}')
    prev = e

def fill(path):  # share of 8 dp rows carrying ink, and the longest empty band
    im = np.asarray(Image.open(path).convert('RGB')).astype(int)
    occ = tot = longest = cur = 0
    for y0 in range(0, im.shape[0] - 8, 8):
        blk = im[y0:y0 + 8]
        on = (np.abs(blk - np.median(blk.reshape(-1, 3), axis=0)).sum(axis=2) > 45).sum() >= 3
        tot += 1; occ += on
        cur = 0 if on else cur + 8; longest = max(longest, cur)
    return occ / tot, longest
```

Measured on `today_ready_night.png` (x 24 to 150): bands 307-318 overline, 328-347 title, 372-453 number (82 dp of ink), 483-519 body (two lines), 545-576 Show me, 601-648 length control; gaps 10, 25, 29, 25, 25.
