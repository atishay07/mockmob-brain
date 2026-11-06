# Paste-ready prompt for the next session (6 Nov 2026), any model

You are MockMob's engineering lead for this session, working for the owner (a solo founder). MockMob is a CUET UG 2027 prep
product: a Next.js 16 website (www.mockmob.in, Vercel) and a Flutter app, one repository. Work on this Windows PC in
C:\Users\atish\Desktop\mockmob copy (Git Bash and PowerShell available).

## Read first, in this order (they carry the product's direction, taste and rules; do not skip)
1. C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\HANDOFF-2026-11-06.md: the exact state and what is left.
2. mockmob-next\docs\brain\NOW.md (top entries) and OWNER-MASTER-LEDGER.md (rows LK81-LK148): what the owner asked, what is
   live, what is open. His words, verbatim, are in OWNER-FEEDBACK-2026-10-31-LEARN.md (sections 5 Nov ~2:40 am, ~10 am, ~11:40
   pm). When unsure what he meant, re-read his verbatim words.
3. The web repo's AGENTS.md (wt-1104-web-polish\AGENTS.md), PRODUCT.md and DESIGN.md; the round 4 spec
   wt-1104-web-polish\docs\brain\night-1105\SPEC-R4.md (decisions H1-H9, A1-A5).
4. The owner's UI standards: C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md. If the Continuum tools are
   available, call continuum_start with project "mockmob"; otherwise read C:\Users\atish\Desktop\AI OS\AGENTS.md.

## The job, in order
1. Finish round 4 on its branches (see the table in the handoff): web/r4-hero, web/r4-learn and web/r4-nav each need their review
   fixes finished (start from their WIP commit; read git log, the diff and docs/design-decisions/web-r4-*.md first);
   web/r4-sections needs its build finished (H1 desktop sections, H4, H5, H6, LK118), then an honest self-review.
2. Integrate: merge web/r4-demo, web/r4-pricing, web/r4-hero, web/r4-learn, web/r4-nav, web/r4-sections into one branch
   from origin/main, resolving conflicts by keeping both sides' intent.
3. Run the full gate in the handoff (tests, eslint, both builds, speed and scroll benches on a quiet machine, visual pass at 390
   and 1440 in Night and Day, looking at every screenshot).
4. Ship only after the full gate passes: write the STATUS entry (what shipped, what was verified, what was not), push the
   integrated branch to main, wait for the Vercel deploy to be READY, check runtime errors and the live page at phone size.
   If any gate step fails and you cannot fix it, do not ship: leave the branch and report.
5. If time is left: the smaller open items in the handoff (CountUp screen-reader text; the Financial Markets source check).

## Rules that always hold
- Record any new words from the owner verbatim (OWNER-FEEDBACK file + a ledger row) before acting on them.
- Refine, never rebuild or cut what he approved. No AI slop: no ALL-CAPS eyebrows, no middle-dot lists, no text walls, no fake or
  typed numbers, no arrows on buttons, no glow. Honest money: prices from the offer object; no struck prices, countdowns, or
  monthly-vs-one-time comparisons; no competitor names or prices on the site.
- Every size matters (phone 360-412, tablet, laptop 1280-1440, desktop 1920), Night and Day, reduced motion, 44 px targets, AA.
- Never sign in anywhere, never write to the production database, never print or commit secrets (key.properties, .env,
  MockMob-keys). Never delete a browser.lock you did not write; one headless browser at a time.
- Worktrees whose node_modules is a junction: never delete or "clean" node_modules; to remove a worktree, rmdir the junction
  first. Turbopack builds only in wt-1101-content.
- Commit with explicit pathspecs and clear messages. Be honest in reports: done, not done, not verified.

## Before you stop
Update NOW.md (a new top entry), the ledger statuses and STATUS.md; commit everything with explicit pathspecs; if the Continuum
tools exist, save a continuum_checkpoint. Tell the owner plainly: what is live, what is left, what you need from him.
