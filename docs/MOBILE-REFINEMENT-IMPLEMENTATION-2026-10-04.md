# Mobile refinement implementation — 4 October 2026

Local implementation of the owner-approved mobile plan. The owner selected **Mobi** as
the public companion name. Existing desktop identity, educational claims, scoring,
entitlements, credit RPCs, question gates and AI budgets are preserved. No deployment,
migration, checkout or paid model call was performed. Existing untracked evidence was retained.

## Changes

- Lab playback observes a bounded content region, subtracting actual header/dock space.
  One elapsed-time clock owns step progress and tile reveals. It pauses offscreen, on
  document hidden, keyboard inspection or explicit pause, then resumes without catching up.
  Manual steps pause autoplay; the new Replay control explicitly restarts it.
- Phone Lab has four compact steps, full accessible labels, concise explanations and
  natural-height overlapping panels. The fresh-question heading replaces repeated phone
  labels. The layout grows with text size rather than clipping longer panels.
- Mobi's public copy and accessible names are consistent across landing, Arena loading/
  setup/results, holding page and brand preview. Internal Pip identifiers remain compatible.
  Below 1100px, the fallback stays in-flow and short reactions render in the same reserved
  box. No fixed phone actor or delayed offscreen reaction queue. Desktop travel remains.
- Compact hero companion, readable 48px hero actions, and a phone exam palette showing
  the five interactive questions. Desktop retains the illustrative 50-cell palette.
- Practice cost/reason uses the available width, with a full-width launch action beneath.
  Results initially expose one chapter and one observation; a disclosure preserves the
  remaining details. Result question/repair controls have larger touch targets.
- Light result answer letters use white on the green/red state fill. Lab elevation is
  softer on paper. Navigation uses restrained 8px glass with opaque reduced-transparency/
  high-contrast fallbacks; no blur was added to question-reading surfaces.
- Arena sticky header repaired by removing the body's unintended overflow scroll container.
  More opens without moving the page; its menu scrolls within measured header/dock bounds.
  Escape restores focus, outside pointer/focus closes it, and desktop resize dismisses it.
  Public navigation also has bounded scrolling.

## Measured before and after

| Check | Before | After |
| --- | --- | --- |
| Lab heading-only dwell, 390px | Advanced to Find after 6.8s with no stage visible | Replay, zero revealed tiles after 6.8s |
| Leave/return mid-replay | Independent clocks ran ahead | Two revealed tiles remain two offscreen; return continues to four |
| Lab total height, 390px | 1036px | 804px; stage 572px |
| Practice summary, 320px | 390px, near-letter wrapping | 166px, usable cost line and full-width action |
| Result Find, 320 / 390px | 1490 / 1247px | 532 / 399px, remaining detail expandable |
| Light result state letters | Approximately 2.75 / 2.82:1 flags | No flags in current result text scan |

## Verification performed

- Chrome responsive matrix: homepage, Practice, Result and branded quick runner at
  320, 360, 390, 430, 768, 1024 and 1440px, both themes: 56 page configurations, plus
  reduced motion, short landscape and 200% text checks. Zero document overflow and
  page exceptions in the matrix. Screenshots were visually inspected at phone/desktop.
- Timing assertions at 390 and 1440px: heading dwell, first arrival, offscreen pause,
  preserved progress, manual selection and explicit restart passed.
- Phone Mobi reactions at 320/390px: actor remains inside its 52×62 reserved Lab box;
  static fallback returns after reaction; no fixed flyer. Reduced motion remains static.
- 200% Lab text: all four panels grow naturally, with equal client/scroll width and
  height (no clipped panel content). Tiles reflow rather than forcing five tiny columns.
- Both premium NTA skins at 320/390px in both themes: answer, clear, mark, next,
  palette navigation, Escape/focus restoration and cancelled submission passed.
  Fixture submission count stayed zero. Public demo preserves answers across skin changes;
  review/clear and theme change/reload persistence passed.
- Free Practice cost and subject-load failure states checked at 320/390px, both themes.
  Failure displays an error and no launch action. No real authenticated session was used.
- Result contrast scans: 155–157 text elements per case at 320/390px in both themes,
  zero flagged elements and zero skipped gradient cases in these particular scans.
- `npm.cmd run lint` and production build passed. Recovery 35/35, learning 80/80,
  combined existing NTA/answer-integrity/payment suites 40/40 passed: 155 tests, no skips.
  `git diff --check` passed. Build initially hit sandbox EPERM scanning `.next`; approved
  filesystem access resolved it without cache deletion or source/config changes.

Evidence: `artifacts/mobile-refinement-2026-10-04/` contains `report.json`,
`interactions.json`, `motion-final.json`, `navigation-final.json`, `performance.json`,
screenshots and check logs. Corresponding reproducible scripts are in `scripts/design-audit/`.
Earlier screenshots in the matrix precede the last removal of repeated phone check labels;
`final-*-lab.png` and `motion-final.json` capture that final compact panel.

## Performance and release gates

Local production-build sampling at 390px, cold browser cache, 150ms latency, 1.6Mbps
download and 4× CPU: LCP 1.604–3.532s; CLS zero in four isolated runs. One run exceeds
the 2.5s target, so performance acceptance remains open. Navigation/dock glass vs opaque
scroll samples had p95 frame intervals 12.2–18.2ms vs 12.2ms. This small emulated sample
does not prove phone frame rate or a causal LCP difference: the opaque override was applied
after load, for scrolling only. An earlier concurrent test run is retained separately and
was not accepted as the isolated comparison. The measured build preceded final offscreen
check-label compaction/menu-height/copy edits; the final source build also passed.

Physical Android Chrome/Safari, browser chrome/safe areas, keyboard, screen-reader use,
and live authenticated workflows remain unverified. Headless tab switching left
`document.hidden` false; the visibilitychange pause is implemented, but genuine background
tab suspension/resume remains a hardware acceptance check. No emulation result is presented
as physical-device proof. Desktop travel was visually checked, not an exhaustive journey
across every possible scroll speed. Real question supply and production readiness are
governed by the existing product release gates.

Development preview remains at `http://localhost:3010`. The temporary production server
on 3011 was stopped after performance sampling. Review the mobile pass, complete the
remaining device/performance checks, then make an explicit deployment decision.
