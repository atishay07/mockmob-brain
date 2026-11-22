---
name: cuet-spoken-as-letters
description: "CUET is always spoken as the letters C-U-E-T in any MockMob narration (owner, 22 Oct and again 22 Nov 2026); also use the real logo asset, never a drawn wordmark"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 16f14db0-6d31-4a6e-9c82-29f414852a62
  modified: 2026-11-22T16:27:36.271Z
---

In every MockMob voice-over, "CUET" is spoken as the four letters C-U-E-T run together as ONE word (about 0.6 to 0.7 s), never as a word ("kyoo-et", "cute") and never as four separated letters.

**Why:** the owner ruled this on 22 Oct 2026 (film repo docs/OWNER-LEDGER.md: "CUET is always said as the letters C-U-E-T; verify every line that says it"). On 22 Nov 2026 a launch-film read respelled it "Kyoo-et" (copied from the previous session's notes) and he heard it at once: "CUIT translation is way off. It's seeing it as some CQUET or something" (brain ledger LK411).

**How to apply:**
- 22 Nov, 10:10 pm (LK412): a take that spelled each letter apart (1.08 s) was also wrong: "it should be separate-sounding words, but in total as a single word". Reference: the approved hero narration says it in 0.60 to 0.70 s. On Fish s2.1-pro, "C.U.E.T." gave that (0.46 to 0.64 s); "C-U-E-T" on drama-3 gave separated letters; plain "CUET" gave "cute".
- Same message: his "overemphasis ... pacing feels very off" came from the acting voice model (drama-3) AND from my cutting the read into phrases, speeding it and squeezing pauses onto a beat grid. Use the steady model, never speed or edit pauses inside a read, lay sentences at the narrator's own spacing, and make the picture follow the read (time map), not the reverse.
- Check every take with the measured proxy (Claude cannot hear): `tools/vo-el/launch/cuet_probe_v4.py` in the film repo (a hiss at the start of "see", several vowel peaks, 0.55 s or more).
- Before writing any narration, grep the film repo's docs/OWNER-LEDGER.md and the brain ledger for earlier pronunciation rulings; a previous session's "decision" is not the owner's ruling.
- Same message, same lesson for branding: the wordmark is the real asset (`public/art/brand/logo-wordmark-dark-transparent-1536.png`, Mobi as the second o; `ART.wordmark`), not a typeset "mockmob" with a dot. He caught a drawn dot version: "MOB having a dot, I don't think that's the ideal, correct branding."
Related: [[launch-film-verdict-1122]], [[owner-ear-over-metrics]], [[mockmob-design-direction]].
