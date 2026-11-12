---
name: ui-audit-log-first
description: 12 Nov 2026 - before any MockMob UI work read mockmob-brain/docs/UI-AUDIT-LOG.md and add findings to it; the owner was unhappy that a 2-hour pass was mostly looking and shipped only small fixes
metadata:
  node_type: memory
  type: feedback
  originSessionId: 896125b8-1f9e-4660-b761-2d31487746ee
  modified: 2026-11-12T15:54:38.612Z
---

Owner, 12 Nov 2026 (about 9:40 pm), after the final pass shipped only small fixes: "what exactly were you doing? ... I don't see any major changes as such on the landing page, hero section". Then: "log everything and your findings ... no other agent has to spend this kind of time looking ... It spends time again and again looking and reading. That's the major issue. Log all of this in the brain, keep it updated".

**Why:** each pass re-walks the same screens and re-reaches the same verdicts; he pays for the looking and sees little change.

**How to apply:** read `C:\Users\atish\mockmob-brain\docs\UI-AUDIT-LOG.md` before capturing any screen; skip surfaces marked "seen, holds" unless their code changed since; write every new finding there (date, commit, sizes). My reading, not his words: when he asks for an "improvement" pass he expects change he can see on his phone, so say early what visible moves are possible and which I intend, instead of ending with polish only. Related: [[fewer-messages-only-what-matters]], [[web-restructure-rejected]], [[phone-is-the-product]].
