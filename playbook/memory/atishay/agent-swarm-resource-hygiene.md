---
name: agent-swarm-resource-hygiene
description: "16 Oct 2026 - big agent swarms crashed the Claude app (0.4 GB free) and hit the 5-hour usage limit mid-work; reap leftovers, cap heavy processes, watch usage before launching"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 604ced81-3aa7-4deb-b42c-f324ca5f51e2
  modified: 2026-10-16T14:52:40.659Z
---

On 16 Oct 2026 evening, about 25 parallel agents first exhausted the 5-hour usage window (28 agents died mid-work around 6:50 pm) and then, after the reset, the Claude desktop app crashed from low RAM (0.4 GB free of 16). The owner: "The app crashed because of low RAM ... keep optimizing the RAM." Earlier the same day he said RAM should not limit agent count and that I should free memory myself.

**Why:** dead or finished agents leave heavy processes behind: Gradle daemons (about 2.6 GB of java), dozens of headless Chrome profiles in Temp (1.6 GB), orphan `next dev` servers, flutter_tester runs, and the staging site (2.4 GB). Nothing reaped them.

**How to apply:**
- Before and during big runs, reap leftovers: java with GradleDaemon in the command line, chrome.exe whose --user-data-dir is under AppData\Local\Temp, flutter_tester and dartaotruntime with no live agent, and dev servers on ports no running agent owns. Never touch the owner's own browsers (no temp profile).
- Put a RAM rule in agent prompts: check free RAM before a server, build or Chrome; one headless Chrome per agent, killed with its profile afterwards; stop your own servers; run `gradlew --stop` after builds.
- Check usage (get_usage) before each wave. Do not launch a large wave when the 5-hour window is past about 60% with more than an hour to the reset. WIP-commit the partial work immediately after any mass agent death.
- Many agents are fine. The limits are leaked processes and the usage window. See [[quality-bar-and-stop-rule]], [[emulator-ram-rule]].

**17 Oct 2026 (session 604ced81) additions:**
- **Usage:** four workflows at once (130 Haiku scoring agents plus 8 website packets, 4 of them Opus) burned 37% of the 5-hour window in 35 minutes; the window lasted about 1 h 40 min of work. Stage waves of about 8 heavy agents, check get_usage every 15-20 minutes, and stop cleanly at 87-90% (STOP POINT commits) instead of letting 100% kill agents.
- **Memory commit:** each webpack `next dev` takes 2-4 GB of commit. Eight of them plus the emulator rig reached 56 of 64 GB (the page file caps at 48 GB). Cap: at most 4 dev servers at once.
- **API TLS failure:** at about 3 am every agent died with "SSL certificate verification failed (UNABLE_TO_VERIFY_LEAF_SIGNATURE)", most likely Avast HTTPS scanning. Save the work as STOP POINTs and resume; the owner may add an Avast exception (his setting).
- **32 GB from 17 Oct afternoon:** the owner upgraded the PC. Long-lived shared `next dev --webpack` servers still bloat (11 GB and 6 GB of commit after about 1 hour of verifier sweeps) and pushed commit to 59 of 64 GB. Start shared dev servers with NODE_OPTIONS=--max-old-space-size=4096 and restart them between waves; prefer `next build` plus `next start` for servers that only serve a fixed commit.
- **Agents killing each other's Chrome:** a critic's broad process filter killed another critic's headless captures. Every prompt must say: stop only processes you started (match your own temp profile path).
- **Never SendMessage a workflow agent by its agentId.** On 17 Oct a message to a running workflow fixer resumed a second copy of it, and both edited the same worktree. To add input to a workflow stage, wait for the stage to return, or relaunch with an edited script.
- **node_modules junctions plus `git worktree remove --force` destroy the shared install.** On 18 Oct, about 12:45 am, removing worktrees followed their node_modules junction into mockmob-hotfix/node_modules and deleted 35 packages (@babel, @anthropic-ai/sdk, .bin and others). It happened twice that night, once from an agent and once from the main session's cleanup. Both times the packages were restored from mockmob-next's install, with versions matched to the lockfile. **Rule:** before removing a worktree, run `cmd /c rmdir <wt>\node_modules` to unlink the junction. Never `rm -rf` or `Remove-Item -Recurse` a folder that holds a junction. Check the shared install afterwards against package-lock.
- **19 Oct 12:48 pm, third time:** mockmob-next/node_modules (shared by every web worktree and the staging rig) was emptied completely, most likely by an agent's R4 worktree cleanup. The rule now sits in docs/brain/BRIEF-1019-COMMON.md (web section), so every brief that cites it carries it; also put it in any brief that creates a worktree. **Fast restore (26 s):** copy the release branch's package.json and package-lock.json into an empty temp folder, `npm ci --prefer-offline --no-audit --no-fund`, then `cmd /c rmdir` the emptied folder and move the new node_modules into place. Every junction works again with no relinking.
- **4 Nov 2026, the window ran out again at 6:38 am** with two workflows mid-run (a scroll packet and an app fix half done, uncommitted); nothing moved for 12 hours until the owner restarted the PC at 6:24 pm. At 77% with 1 h 45 min to the reset I had planned to hold the next wave, but the running agents alone burned the rest. **Rule:** past about 75%, let only already-running agents finish and launch nothing new (integration, gate) until the reset; resume with a fresh script whose prompts say "read the uncommitted diff first".
