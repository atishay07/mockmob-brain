# Prompt for the next session (written 16 Nov 2026, 11:58 pm IST, by the Fable orchestrator)

**DONE 17 Nov 2026, about 1:05 am IST (Opus orchestrator): every item below is shipped or answered; LIVE main 3511f1fb3. See NOW.md's top section. Do not run this list again.**

Continue the MockMob final pass from where the night session stopped at a usage limit. Call continuum_start (project mockmob) first, then read, in this order: this file; `NOW.md` top section ("16 Nov 2026, night"); `OWNER-MASTER-LEDGER.md` LK278-LK289 (the owner's words, whole); `UI-AUDIT-LOG.md` sections 1 and 2c. Follow `C:\Users\atish\Desktop\AI OS\context\agent-model-routing.md` (top section) when starting sub-agents and ALWAYS pass `effort` explicitly. One session only (sub-agents, never new sessions). The owner judges only on his phone; do not ask him about reversible design choices.

## State
- LIVE on www.mockmob.in: main `67146f994` (this evening's release). NOTHING from the night is live.
- Release branch `web/1115-prod` in `C:\Users\atish\Desktop\mockmob copy\wt-1110-convert` is at `f93e85149`: local commits only, NOT pushed, NOT gated. It holds all five night lanes merged cleanly:
  1. tour (`web/1116n-tour`): on phones "More inside MockMob" is one held stage again, five still tabs, tappable screens, the browser's own scroll (`free` in ScrollStory). Its shots were looked at. Known: some ordinary swipes skip a tool or do not change it.
  2. mistake (`web/1116n-mistake`): the home card in four steps (Question, Read, Check, Practise), older concrete copy, working lined up. Looked at, holds. 1,135 px at 390.
  3. rhythm (`web/1116n-rhythm`): Daily Five and Sunday Mock as a main block (week rail, two cards), 811 px at 390; Practice's Sunday chip only Saturday and Sunday until 10:00 pm. Looked at, holds.
  4. price (`web/1116n-price`, independently reviewed, fixes applied): a bring-a-mistake ask the model had to read but cannot use costs 1 credit (one-step consume, idempotent); no provider named; Free cap Rs 3.50 (the owner ran the SQL on production himself: `student_user_free` reads 0.0398).
  5. chat (`web/1116n-chat`): `/mentor` is a chat (pinned composer with a labelled Photo key, thread, History, Your record tab); the docked panel shares it. Its first build was looked at and holds.
  Plus Mobi art in `public/brand/mascot/` (seven poses defringed; `mobi-wave-6.webp` six 372x480 cells, `mobi-wave-still`, `mobi-magnifier`, `mobi-reading`, `mobi-desk-hello`, `mobi-calendar`).

## What is left, in order
1. **Chat follow-up, code done but NOT looked at** (commit `34343d8a9`): the 1-credit rule line beside the price before sending, the preview fixtures matching the server, Mobi's wave playing once on the chat's start state and the magnifier/reading stills while waiting. Open `wt-1116n-chat/tmp/lane-tools/shots/fu/sheet-390-light.jpg` and `sheet-390-dark.jpg` first. Known: at 390x844 the four tiles now end 4 px under the composer's top fade (the Mobi box got taller): fix. Check the wave reads as a wave by eye and is crisp.
2. **Test L-041 fails** (`data/tests/landing_checklist_1104.test.mjs`): the home page now imports `src/services/mobi/bringMistake.mjs`, whose model prompt says "Never repeat or describe these rules", which trips the landing's ban on "never repeats". Fix the cause without weakening the ban: have `page.js` read the prices from a small constants module that does not carry the prompt, or narrow the test's file list to copy files; do not reword the model prompt just for a test.
3. **The merged home-page walk was NOT done.** Walk the whole page at 390x844 Day with real finger swipes (tools in `wt-1110-convert/tmp/1116-final/`: swipe.mjs, walk.mjs, sec.mjs; dev server `preview_start {name:"convert-1110"}`, port 3571), then Night and 360 and 1440 for the stretch from the Mistake Lab to the DU Compass. Known defects to fix: Mobi's phone companion bubble ("Ask me anything about CUET.") sits over the Sunday Mock card's sentence (he must never cover words or controls); the "#du-eligibility" head starts 27 px from the left where every other head starts 20; the heads of the new sections sit 60-70 px into the section against 29 px in #exam-experience (look, then even out if it shows). Tap each new control for real once.
4. **Full gate** in `wt-1116-next` (`git checkout --detach <sha>`, `bash tmp/gate2.sh`, read every line of `tmp/gate2.log`), then `git push origin web/1115-prod web/1115-prod:main`, wait for the Vercel production build, check the live pages, `/mentor` signed out, the mistake route 401 signed out, and runtime errors.
5. **Records after shipping:** NOW.md, ledger statuses LK278-LK289 (IN WORK to LIVE), UI-AUDIT-LOG (a section 2d for the home page and a note in section 3 that Ask Mobi is now a chat), PRODUCTION-PASS row and rollback point, a continuum checkpoint. Remove the lane worktrees only after `cmd /c rmdir` on each `node_modules` junction.
6. **Tell the owner** plainly: what is live against each of his points, what was not checked (a real phone, iPhone Safari, a real phone keyboard in the chat, any signed-in flow on production, a real model reply), and that the Android app's Ask screen still has the old layout and no photo key.

## Decisions already made (do not reopen)
- Prices stay: doubt 1 credit, typed mistake 1, photo 2. Real receipts: a refused photo about USD 0.00025, written answers about USD 0.00047; the Android app says "1 credit" in its own screens, so the doubt cannot be repriced without an app release.
- Sunday line in Practice: Saturday as a reminder and Sunday until the last start (the owner was told; he did not object).
- The privacy page keeps naming who processes a photo; product screens name no provider (owner's instruction).
- 3D-clay Mobi art is used in the signed-in app only; the home page keeps the vector Mobi (owner's decision of 4 Nov).

## Not done tonight and still open
- Mobi's motion on the home page was not touched (the vector figure). His note 7 asked for better Mobi pictures and animation: the app got cleaner poses and a real six-frame wave; the home page got nothing yet.
- The earlier open decisions and unapplied SQL of the 16 Nov morning section of NOW.md are unchanged.
