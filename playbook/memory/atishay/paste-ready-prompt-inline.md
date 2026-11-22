---
name: paste-ready-prompt-inline
description: "22 Nov 2026 - when the owner asks for a prompt to paste somewhere, the reply is the full prompt text inline, first, nothing around it"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 16f14db0-6d31-4a6e-9c82-29f414852a62
  modified: 2026-11-22T11:29:06.643Z
---

When the owner asks for "a prompt I can paste" (into Cowork, another chat, another tool), give the complete prompt text in the chat itself, in one copyable block, as the first thing in the reply. Do not answer with a pointer to a file, a one-line "read file X" prompt, or the prompt buried inside a longer status message.

**Why:** On 22 Nov 2026 (ledger LK398 to LK401) he asked for the Cowork prompt three times in ten minutes ("where is the prompt??", "I have said so many times") while leaving the house. My answers pointed to gen-queue/COWORK-WORKER.txt or sat inside mid-turn progress text he did not see. He reads the reply itself, often on the way out, and mid-turn text may not reach him.

**How to apply:** Any request for something to paste or run: the thing itself, whole, in a fenced block, at the top; one line above it saying where to paste. Keep everything else for later. He also wants such helpers to be self-running ("it can automatically keep communicating with you; you don't need to give it everything at once"): design a standing loop that talks through files, not one-off batches he must paste each time. Related: [[fewer-messages-only-what-matters]], [[higgsfield-video-plan]].
