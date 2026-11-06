# Handoff, 3 Nov 2026, about 9:15 pm IST: everything stopped for the move to a new account; one session from here on

**The owner's rule (3 Nov, verbatim):** "Can you just stop everything running on this account right now? Prepare a handoff and a
prompt which I can paste into a new account, where everything can just be worked upon in a single session. If multiple tasks are
going on, you have to start workflows or sub-agents, not start sub-sessions or fork sessions."

So: ONE session does everything. Parallel work goes to Workflow scripts or Agent subagents, never to start_session, forks or
messages to other sessions. All earlier sessions on the old account are stopped; nothing of theirs runs.

## 1. Live now (production www.mockmob.in, main f0186302f, no runtime errors)
- **Learn v2 rounds 2-5** and the Explore feed (LK24-LK47 mostly live): option shuffle (no more "every answer is A", LK44), keys
  say when a card returns (LK38), one done count, wheel scroll, tab order Practice Papers Learn Explore (LK46), landing scroll
  (LK47), choose what goes in a run (LK37, 4006a7c04).
- **Key cards:** 15,707 cards in 14 subjects. Every subject is over 3 hours except Mathematics (548 cards, about 2.9 h; NCERT
  2026-27 supports about this much). Mathematics carries typeset formulas (KaTeX 0.19.0, server-drawn, `tex` field; spec
  handoff-1102/MATHTEX-SPEC.md). All web fonts are self-hosted (src/app/fonts), so Vercel's Turbopack build no longer fails on
  Google Fonts.
- **App:** 1.0.19+17 (C:/Users/atish/Desktop/MockMob-build-17) is in Play review / closed testing; the owner uploaded it.

## 2. Unfinished work, by lane (nothing is running; each needs its next step)

**A. Physics formula cards (LK34, owner: "Yes, start Physics").** Written and reviewed, NOT published.
- All 14 chapters leph101-108 and leph201-206 were authored and double-reviewed (Opus formula reviewer against the page image,
  Sonnet content reviewer): 362 new cards plus 49 held cards reworked; 269 of 411 passed both and are merged into
  ncert-books/reviews. A fix round on 58 cards is written and reviewed but NOT merged: ncert-books/ptex2, ptex2-reviewsA,
  ptex2-reviewsB, fixlists-ptex2.
- An unpushed checker fix is on web/1101-content (958f2b8c3: Greek read as the Symbol-font letter the PDF prints, e.g. "4pe0").
- Steps: (1) `MTEX_DONE=ptex2 MTEX_RA=ptex2-reviewsA MTEX_RB=ptex2-reviewsB MTEX_BAK=drafts-bak-ptex2-1103 node
  handoff-1102/merge-ptex-reviews-1103.mjs <the 12 codes with ptex2 done files>` and the ptex guard. (2) Publish in
  wt-1101-content: merge origin/main, `node scripts/keycards/review-merge.mjs`, `validate.mjs --subject=physics`, `tier.mjs`,
  compare the deck with HEAD (no published card removed or changed), suites keycards/keycards-ui/learn, `eslint .`, BOTH `next
  build` and `next build --webpack`, a look at 390 and 1440 Night and Day (no card back overflows), STATUS, push, read the deploy
  state, runtime errors. (3) NOW, the LK34 ledger row, delete ncert-books/pages.
- Physics baseline 1,090 cards, 5.5 h. Scripts and brief: handoff-1102/PHYSTEX-AUTHOR-BRIEF.md, ptex-*-1103.*.
- Checkpoint: AI OS handoffs/mockmob/20261103T154357.792265Z-e3a36b7d.md.

**B. App 1.0.20+18 (LK50-LK53).** Code on branches, not released.
- ui/1103-app-18 (wt-1103-app-rel) merges ui/1103-sending (LK50: stale "Sending your answers" drafts settled),
  ui/1103-r5-port (round 5 in the app, Explore as Practice's fourth door, LK51) and ui/1103-learn-calm (calmer Learn, LK52/53).
  Analyze clean; the full suite has 113 failures: the known old golden drift plus at least 4 NEW Learn failures from the merge
  (two run screen, one feed, one chapter page). No emulator walk yet, no 1.0.20 build.
- Steps: fix the 4 new failures, emulator walk against the live web (emulator RAM 2-3 GB), build the 1.0.20+18 AAB with --sell
  (upload key in C:/Users/atish/MockMob-keys, never print or commit), package for the owner like MockMob-build-17.
- The calmer-Learn prototype APK: C:/Users/atish/Desktop/MockMob-prototype-learn-calm.apk (reads Learn from this PC over Wi-Fi).

**C. Web prototypes waiting for his live look (LK39, LK41, LK42, LK43, LK59, LK60, LK62).** Not live.
- web/1103-proto (top bar capsule, LK42), web/1103-cards / wt-1103-web-cards (card look LK39/43), web/1103-icons (branded "desk
  object" icons, LK60), web/1103-webfull (phone website as the full product, one "Up next" recommendations module, LK59/LK62;
  its agent finished but its report was not read: check its diff and tests first).
- He judges only live prototypes on his phone. The PC must be on Wi-Fi (192.168.1.8; Ethernet .15 is blocked by the firewall
  for phones; never change the firewall). Preview links must carry `decks=real&study=on` or Learn v2 is hidden; open each link
  at 375x812 before sending it. Ship each web change only after his look.
- Specs: wt-1103-app-r5-port/docs/brain/learn-1031/r6/R6-SPEC.md and r7/R7-SPEC.md.

**D. English rewrite (LK61).** A table of 101 rewritten lines, not applied: wt-1103-web-cards/docs/brain/learn-1031/r7/E-ENGLISH.md.
Apply after C lands (it touches the same screens).

## 3. Waiting on the owner
1. A live look at the prototypes in lane C (links rebuilt once the PC is on Wi-Fi).
2. Saved on phones: back to one tap, or keep it inside Explore?
3. App switch: "Practise | Papers | Learn | Explore" OK?
4. LK36 gaps, content only on his yes: (1) English reading-comprehension cards, (2) Financial Markets from NCERT's 2022 edition,
   (3) Computerised Accounting (needs NCERT's PDF downloaded).
5. Upload 1.0.20+18 when lane B delivers it.

## 4. Rules that matter (all in memory and docs/brain; newest wins)
- Read docs/brain/NOW.md and OWNER-MASTER-LEDGER.md first; record his words verbatim (OWNER-FEEDBACK-2026-10-31-LEARN.md) before
  acting; update NOW and the ledger at every session end.
- One session; Workflow/Agent for parallel work; every agent prompt says SUBAGENT with ONE task; pass workflow args from files.
- Before any push to main: suites green except the known failures (authored-publish 13, factory 5, mob 7, study 1), `eslint .`,
  BOTH builds, a look at 390 and 1440 Night and Day; then list_deployments and get_runtime_errors. Vercel project
  prj_uSolddribHQDl1mM5AKxg3O9qCIu, team atishay07s-projects.
- Machine: at most 2 dev servers (tmp-devslots/slot-1|slot-2) and one headless browser (tmp-devslots/browser.lock); start dev
  servers with preview_start and .claude/launch.json; many worktrees' node_modules are junctions into mockmob-next/node_modules:
  never npm install through one, and rmdir a junction before removing a worktree. Real node_modules: wt-1101-content,
  wt-1101-r2-home.
- Never write to the production database (prepare SQL and its undo for him). Never sign in on production.
- Read the clock with `date` before writing any time. Check get_usage before every wave; stop new agents near 90%.
- Product: refine, never rebuild; never cut a feature; exact NCERT text with book, chapter and page; uncertainty means held back.
  No vague icons; plain, correct English; the phone website is the full product, not a copy of the app.
