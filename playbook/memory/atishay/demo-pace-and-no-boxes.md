---
name: demo-pace-and-no-boxes
description: "22 Nov 2026 (LK366) owner's verdict on the self-playing home demos; what he loved, what he rejected, and the pace that reads"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 777be139-a000-4c98-9286-70590b597225
  modified: 2026-11-21T20:54:10.920Z
---

On 22 Nov 2026 (ledger LK366) the owner judged the self-playing demos on the live home on his phone.

- Loved: the captioned story direction, the Ask Mobi film ("really good"), the Mob story, Benchmarks, the Mistake Lab's stacked cards with automatic hand-off.
- Rejected: outline boxes with the rest dimmed on the real Practise and Key cards screens ("just introducing some boxes here and there, which are not looking as they should").
- Pace: five Lab scenes in 11 s was "way too fast ... no one can even read it"; he prefers a slower one. About 7 s a scene with no dead time is what shipped. The two plain rows at 12 to 14 s were "quite slow"; about 10 s shipped.
- A section must say what the feature IS in one plain sentence; the Daily Five block failed that ("unable to understand").
- Smoothness regressions get noticed (Compass bars went "choppy" after a jank fix removed their easing).

**Why:** he compares each release with the one before on his Galaxy M06 and names both too slow and too fast.

**How to apply:** on real product screens let the cursor and the change be the stress, no rings round groups; give every beat time to be read and nothing but reading time; measure scene times in a phone context before shipping; never trade away visible smoothness for a frame-time number without re-looking. My interpretation, not his words: purpose-built story screens (like Ask Mobi) can keep a small ring on one control. Related: [[phone-is-the-product]], [[visible-change-build-first]], [[owner-ear-over-metrics]].
