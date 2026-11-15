---
name: build-features-before-audits
description: "15 Nov 2026, owner on the production pass: he wanted new things built, got mostly audit and fixes; start feature builds in the first wave, decide small things myself"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 409ddd8f-7b5b-4a40-b2f3-25fada6ee352
  modified: 2026-11-15T13:26:15.187Z
---

On 15 Nov 2026 the owner asked for a production pass ("add any features... innovative ideas... take this entire platform to the next level"). I ran an 11-lane audit, then security and bug fixes, and sequenced every new feature last; a usage limit then cost about three hours and no feature had started when he asked for an update. His words: "focus more on building and building more things... rather than just doing an audit and thinking long on smaller things and refinements... tangible, actual results, not small refinements"; the pending decisions "can easily be built at the end... in like 30 minutes"; "You can think for yourself what's useful, what's not, and apply everything. Push it to live. Then we'll come back to the pending decisions."

**Why:** he measures a pass by new things he can see and use; audit findings and hardening read as "not at the scale I was expecting" (see [[visible-change-build-first]], [[features-over-retesting]]).

**How to apply:** in any build pass, start new-feature lanes in the FIRST wave beside the fixes, not after them; keep audits short and targeted. Decide small product questions myself, ship, and keep a running list of what truly waits on him instead of stopping. In updates, list every plan item with its status, including the unstarted ones (my interpretation: he reads an omitted item as dropped). Pace agents for the 5-hour window: 23 Opus agents emptied it in about 90 minutes.
