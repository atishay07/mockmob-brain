---
name: perf-bench-quiet-machine
description: "5 Nov: 4x-CPU swipe benches read 14 long frames while test suites ran, 0 on a quiet PC; packets deleted each other's browser.lock"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 34abe724-bccd-4ea2-badf-26b6f6615d8a
  modified: 2026-11-05T02:14:51.378Z
---

On 5 Nov 2026 the home page's 22-swipe bench (4x CPU throttle, production build) reported 14 frames over 100 ms while 20 npm test suites ran in the background; the same build re-measured on a quiet machine gave 0. CDP CPU throttling multiplies host load, so any concurrent build or test run fakes a regression.

**Why:** a false regression nearly sent tonight's merge back for a bisect; a true one would be hidden the other way round.

**How to apply:** run perf benches (runPerf, traces, LCP/TBT) only when no build, test suite or other agent's browser is running; say so in the STATUS numbers. In packet prompts, also say "never delete a browser.lock you did not write": two of seven packets removed another packet's lock on 5 Nov, letting two headless Chromes run at once. See [[agent-swarm-resource-hygiene]] and [[workflow-stop-leaves-orphans]].
