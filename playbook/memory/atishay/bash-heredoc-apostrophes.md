---
name: bash-heredoc-apostrophes
description: On this PC a Bash-tool heredoc whose body has an apostrophe can fail to parse; write file content with Write/Edit and run scripts from files
metadata:
  node_type: memory
  type: reference
  originSessionId: 1b0e2998-ac98-4f04-83cf-c78491c0f986
  modified: 2026-11-12T18:40:19.847Z
---

On 13 Nov 2026 a Bash call that appended CSS with `cat >> file <<'EOF'` failed before running anything: "unexpected EOF while looking for matching `''". The body had apostrophes in comments ("Night's", "Mobi's") and a second quoted heredoc after it in the same command.

**How to apply:** put multi-line file content in with the Write or Edit tool, and put multi-step Python edits in a script file (scratch folder) and run that. Short heredocs with no apostrophes worked all session. After such a failure, check `git status` first: the command is rejected whole, so nothing is half-applied.
