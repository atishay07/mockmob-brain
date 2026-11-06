---
name: landing-checklist-gate
description: 17 Oct ~10:20 pm owner decision - the landing ships on a fixed binary checklist (his 45 L items, zero truth, zero high, each fix locked by a test), not a critic's 88/100 score
metadata:
  type: feedback
---

On 17 Oct 2026 about 10:20 pm the owner chose "Fixed checklist" for the landing gate, after 15 critic rounds never converged ("just imagine 15 rounds: a lot").

**The rule:** ship the landing as soon as:
- all of his landing items (L-001 to L-045 in docs/brain/WEB-OWNER-LEDGER-2026-10-17.md) pass, except L-001 and L-002, which pass only by shipping;
- there are zero truth defects (every feature claim read from the same capability gate the product uses);
- there are zero high-severity defects.

Each fixed item gets a test so it cannot regress. A 100-point critic score is recorded as advisory only and never blocks. After shipping, improve it live every 1-2 hours.

**Why:** fresh critics each round find new small issues, so the score swung 74-88 on the same page (it hit 88 in round 5 and never shipped). Fixers also regressed earlier fixes, such as one-gesture-one-slide paging. This supersedes ledger item L-002's "88 or more".

**How to apply:** never gate a release on a subjective score from new critics. Gate on a fixed list plus tests, ship, then iterate. See [[agent-swarm-resource-hygiene]] and [[owner-feedback-1017]].
