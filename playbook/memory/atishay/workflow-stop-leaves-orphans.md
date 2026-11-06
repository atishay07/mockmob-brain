---
name: workflow-stop-leaves-orphans
description: "24 Oct: TaskStop on a workflow does not end background bash / renders its agents started; one orphan bake switched REEL_MUSIC after the stop"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b448f889-ae88-4a58-b8a4-87f72631156e
  modified: 2026-10-24T12:42:55.534Z
---

Stopping a workflow (TaskStop) ends its agents but NOT the background shell jobs they launched. On 24 Oct an integration agent's `pipeline.sh b37` kept running after the stop, rebuilt the bed, switched REEL_MUSIC in planReel.ts to an unverified bed, ran a full audio render on the shared lock, and the cuts lane then cut its beds from that wrong bed.

**Why:** the orphan silently changed live config that renders and other lanes read; it cost a re-render and a cut-bed rebuild.

**How to apply:** right after stopping a workflow, run `ps -ef | grep -E "pipeline.sh|arender|audio_slice|render.sh|zone_check"` and stop the ones the stopped agents started (by PID tree, never by image name); re-check config lines they could touch (REEL_MUSIC, REEL_VOICE, CUT_BED) with grep before the next render. Related: [[workflow-resume-prefix-cache]], [[agent-swarm-resource-hygiene]].
