---
name: pull-needs-frozen
description: "Pulling a MockMob question needs exploration_state='frozen' too; status='pending' alone leaves it served"
metadata:
  node_type: memory
  type: project
  originSessionId: 16f96fa8-b613-46a8-9eb0-5f9361c78fcd
  modified: 2026-10-31T11:16:58.776Z
---

A MockMob question is served when `status = 'live'` OR (`verification_state = 'verified'` AND `exploration_state = 'active'`) (VISIBLE_QUESTION_FILTER in data/practice_source.js; also the feed, repair check and inventory). Setting only `status = 'pending'` does not take it out of the pools.

**Why:** On 31 Oct 2026 the 25 flawed-question pulls set only status and stayed served for hours, until the off-syllabus pull found it and froze them.

**How to apply:** Any pull SQL sets `status = 'pending'` and `exploration_state = 'frozen'` (plus `is_cuet_syllabus = false` for off-syllabus), and the undo restores all of them. Votes only ever freeze, never unfreeze. See [[prod-writes-blocked-in-auto-mode]].
