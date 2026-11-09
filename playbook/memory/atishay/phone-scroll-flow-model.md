---
name: phone-scroll-flow-model
description: "10 Nov 2026 — the home page's phone scroll is FLOW (not held, not free): stage pins and shows every step, scroll is native, one landing per story; knobs and how to test it"
metadata:
  node_type: memory
  type: project
  originSessionId: 585e670b-982c-44d4-b5f2-1ceca346163e
  modified: 2026-11-09T23:11:38.174Z
---

Since 10 Nov 2026 (main 7c28f3ea7, owner LK190, settles LK179) the home page's stories behave differently by input:
a mouse or trackpad keeps "one gesture, one step"; a touch screen (`(hover: none), (pointer: coarse)`) uses FLOW. In
flow no touch is owned and nothing is locked; the sticky stage shows the step under the window's middle; a scroll at
rest settles on the nearest step; the first fling that brings the Mistake Lab, the tour or the Recovery Lab on from above
lands once on its first step (never the statement, never a drag, never on the way up); the hold is 0.6 of the mouse's.

**Why:** the owner was conflicted: held stories felt "very locked in" ("People will just not scroll to the end of the
pricing page"), and the free prototype of 9 Nov "isn't able to really show the features". Flow shows every step without
ever refusing the finger. From the top to the plans on a phone: 31 ordinary flicks before, 19 after.

**How to apply:** do not bring back touch holds or sideways-only stories without his say. The knobs are `FLOW_SHARE`
(storyGesture.mjs, with the 0.6 in scroll-story.css `--ss-run`) for more or less grip, and `land` on a ScrollStory for
the one stop. Test any change with `oneGestureBench.mjs` modes `flow`, `landing` and `journey` (real Chrome; set
`MM_BROWSER_LOCK` to your own file, the shared tmp-devslots/browser.lock is stale), and `wheel` at 1440 for the mouse.
When a story's length changes, re-measure the reserved section heights in landing.css (touch and mouse have separate
fits). Not yet checked on a physical phone or iPhone Safari. Related: [[web-restructure-rejected]],
[[conversion-means-taste-not-metrics]], [[perf-bench-quiet-machine]].
