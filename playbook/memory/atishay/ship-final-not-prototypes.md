---
name: ship-final-not-prototypes
description: "3 Nov 11:55 pm: owner wants no prototype links/APKs; finish, self-review UI against his feedback, deploy to www.mockmob.in and hand him a Play-ready AAB; commit everything"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c5a8da45-5c74-46ba-abca-73f6160b75cd
  modified: 2026-11-03T18:25:30.696Z
---

On 3 Nov 2026 ~11:55 pm IST the owner said: keep going through all open lanes, then review the UI against his past feedback and keep improving until satisfied; then "don't give me prototype links or builds. Give me a final build which I can upload straight to Google Play, and deploy the final changes to the website, main website only". Also commit all uncommitted work so the project is final and up to date for handover/onboarding other members.

**Why:** LAN links and emulator builds kept failing to show him the change (see [[prototype-links-must-show-the-change]], [[live-prototype-over-renders]]); he would rather judge the real product on every device.

**How to apply:** for this round the CTO decides UI against the ledger and ships to production after the full gate (suites, eslint, both builds, 390/1440 Night/Day look, deploy check). Deliver one signed AAB (see [[mockmob-upload-key]]). Supersedes "ship each web change only after his live look" unless he says otherwise later.
