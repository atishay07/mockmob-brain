---
name: small-passes-no-subagents
description: "22 Nov 2026 (LK367) owner: sub-agents slow small fix passes; do small UI tasks in the main session in one go"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 777be139-a000-4c98-9286-70590b597225
  modified: 2026-11-21T21:47:51.704Z
---

On 22 Nov 2026 (ledger LK367) the owner said: "I have seen that subagents usually slow you down mostly. These are very small tasks, so try to do all of these just yourself in one go so that all these are done quickly."

**Why:** the LK366 pass used three Opus agents for the Lab, Daily Five and Compass and took over an hour for what he saw as small changes; he then judged the result as "not much of a major difference".

**How to apply:** for a feedback pass of small UI fixes, edit, film and ship from the main session; keep agents for genuinely large or independent builds, or when he asks for them. Still run the full release gate before a deploy. My interpretation: this narrows [[orchestrator-thinks-agents-do]] for small passes; it does not ban agents for big waves. Related: [[fewer-messages-only-what-matters]], [[visible-change-build-first]].
