# Design decisions: merge of ui/phase2b-1016 into ui/phase2 (16 Oct 2026)

User task: a CUET student who has just finished a mock (result recap), opens Review to repair mistakes, or
plans colleges (Today, Compass, You). Evidence IDs per AGENT_RULES (rules 2 and 39); where the rules name
no ID the rule number is cited.

## What came in
- f428d2ef My colleges: one server list (up to 8) shared by Today, Compass and You. Rule 8 (rank content by what helps the
  next decision: the same list everywhere), rule 18 (what happens next: "0 of 8 colleges", "Add a college"),
  rule 35 (empty, failed and offline-copy states have goldens).
- e69a0731 Result, critic packet D: the key names the work ("Repair 3 mistakes") with its denominator as a line above;
  one main action per screen (rule 7), share demoted to one 48 dp chip, Choose something else opens a sheet.
- b41aee9e Review and repair, critic packet E: To repair / History switch, one filled track per chapter row with its
  denominator (rule 9, value before label), the repair's break and why it looked right in one raised surface
  (rule 33, cards group meaningful items), the idea as a pull quote.

## Merge decisions
- Source merged without textual conflicts. The 38 golden conflicts (result 26, review 12) were all binary: both
  branches had regenerated them. They were regenerated from the merged code; every new master is byte-identical to
  the one packet D/E produced, so the Mobi rig v2 and Day welcome work on ui/phase2 do not change these screens.
  Old (phase2) against new was opened for all 38, Day and Night: changes are the intended ones above (answers slab
  keeps the flap's lamp and rim, 12 sp Sankey captions, one-line share chip, raised repair surface, pull quote).
- Review's section switch used a bare AnimatedSwitcher, which the motion guard forbids (its cross-fade dips to half
  strength and flashes the ground). It now uses MmOverlapSwitcher (rule 31: motion with a purpose, reduced-motion
  fade kept).
- The harness (pumpMockmob) now supplies a quiet My colleges repository, so two tests that re-pumped a bare
  ProviderScope (key_button_test, review_phase2_test) failed on the override count; they re-pump through
  pumpMockmob instead.

## Dock contrast (critic E: Day measured 1.75:1)
Not reproducible on this branch. Measured from the Today goldens in Day (dock with the Start key, capsule and
content scrolling under the glass): idle labels and icons 9.3:1, active label 18:1, Start label 14.9:1, in 21
Day Today states. Flutter's textContrastGuideline passes on the dock in both themes, and a new token test
(bar_guidelines_test) holds ink2 and ink above 4.5:1 on the glass composited over the ground (rule 36). The
1.75 figure most likely came from the earlier custom-icon bar (superseded) or a non-text edge. No code change needed.

## Unresolved
- No device check (no emulator; RAM). Verification is analyzer, unit tests and goldens.
