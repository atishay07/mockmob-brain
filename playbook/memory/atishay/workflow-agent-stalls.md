---
name: workflow-agent-stalls
description: "1 Nov: a workflow agent can end its turn waiting on its own Monitor and return one line; check each worktree's commits and diff before trusting any packet report"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3b7877eb-5583-4711-a116-f19495e8e628
  modified: 2026-11-01T18:10:22.539Z
---

On 1 Nov the R4-server packet (Opus) returned only "The monitor will notify me when all six suites have exited." Its work (530 lines in 9 files) sat uncommitted and untested in its worktree; the other four packets were fine.

**Why:** a subagent that waits on a background Monitor or task gets no notification after the workflow ends, so it stops mid-task, and its one-line "report" reads like progress.

**How to apply:**
- After every fix workflow, run `git log base..HEAD` and `git status` in each packet worktree before reading reports as truth.
- Tell packet agents in the prompt to run their suites in the foreground (no Monitor or background waits) and to commit before they return.
- An unfinished packet can be rescued: run the suites on its diff yourself and commit it if they pass.
- Pass workflow `args` from the source file (for example chapters-9.json), never retyped: a retyped em dash ("An Imperial Capital — Vijayanagara") almost mislabelled a whole chapter.

Related: [[no-sendmessage-to-workflow-agents]], [[subagent-wave-pacing]].
