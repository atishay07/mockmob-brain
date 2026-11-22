---
name: nested-sessions-usage
description: "22 Nov 2026: owner allowed nested sessions (start_session) for big overnight tasks; Fable sessions burn the 5-hour limit very fast, so run them on Opus"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 777be139-a000-4c98-9286-70590b597225
  modified: 2026-11-22T01:51:55.387Z
---

On 22 Nov 2026 (ledger LK368) the owner said nested sessions may be used for big tasks ("you can utilize the nested sessions feature ... instead of subagents ... I don't know how beneficial that is, but if it is, you can utilize that"). This relaxes [[single-session-no-subsessions]] for overnight runs he asks for; it is not a standing order to use them.

What happened that night: two fresh Fable sessions (hero film, Mistake Lab) plus the orchestrator took the 5-hour limit from 36% to 54% in 13 minutes. A session's whole task is one turn, so `set_session_model` only takes effect after `stop_session` and a follow-up message. On Opus 5.5 both sessions finished well (film v6 in about 2.5 h, Lab redesign in about 2 h).

**Why:** the 5-hour limit is a hard wall even when he says usage is not an issue; hitting it stalls every lane for up to two hours.

**How to apply:** start nested sessions on Opus (`model: 'claude-opus-5-5'`) from the first call, `use_worktree: false` with strict file ownership so the orchestrator can commit without merging branches, `permission_mode: 'auto'`, and have each write its plan to a file early so a limit cut can be resumed. Keep the orchestrator's own calls few when its context is large. Check `get_usage` right after launching anything. Related: [[no-fable-when-limited]], [[subagent-wave-pacing]], [[hero-film-fable-only]] (the film rule was kept in spirit: one dedicated session made every film decision).
