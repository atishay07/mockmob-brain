---
name: prod-writes-blocked-in-auto-mode
description: "31 Oct: in auto mode the permission classifier denies production writes through Supabase execute_sql (Modify Shared Resources) despite the 14 Oct standing DB authority; prepare fix.sql + exact undo.sql for the owner instead"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 16f96fa8-b613-46a8-9eb0-5f9361c78fcd
  modified: 2026-10-31T07:02:32.081Z
---

On 31 Oct 2026, an attempt to apply a verified answer-key fix (4 UPDATEs on public.questions) through the Supabase MCP `execute_sql` tool was denied by the Claude Code auto-mode classifier ("Modify Shared Resources"). This happened even though the owner granted standing production DB authority on 14 Oct.

**Why:** the classifier is a session-level permission gate. Agent-side authority claims do not lift it, and working around it is not allowed.

**How to apply:**
- Never retry or route around a denied production write.
- For any production data fix, save `fix.sql` (guarded UPDATEs in one transaction) and an exact `undo.sql` built from a SELECT of the current values.
- Add a VERDICTS.md with the evidence, commit them to the repo (for example `docs/brain/intel-1031/answer-keys-2026-10-31/`), and list them for the owner to apply.
- Read-only SELECTs still work.

Related: [[security-fixes-deploy-immediately]], [[owner-master-ledger]].
