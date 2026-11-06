# Handoff: Key cards, end of the 31 Oct morning session (about 6:00 am IST)

**Session:** 16f96fa8, Claude Opus 5.5 (orchestrator). Continues `HANDOFF-2026-10-31-KEYCARDS.md`.
**State in one line:** the card feature is built end to end on branches, with real content, and every suite is green.
Nothing is pushed, deployed or written to production.

## Where everything is (all under `C:\Users\atish\Desktop\mockmob copy\`)

| Part | Branch / place | State |
|---|---|---|
| **Web integration** | `web/1031-keycards` at 90fddb40d (`wt-1031-keycards-web`) | Syllabus v2 + Key cards server + web screens + polish merged, plus the decks, links and re-tag file. Builds with `next build --webpack`. |
| App | `ui/1031-keycards` at bb4da376b (`wt-1031-keycards-app`, base `ui/1020-v16`) | Section 4 done; analyze clean; unit keycards 55, golden keycards 42, learn and review unit + golden all pass. Never run on a device. |
| Card drafts / reviews | `ncert-books/drafts`, `ncert-books/reviews` (not in git) | 70 NCERT chapter drafts + English. Every card has an independent review entry. |
| Briefs | `ncert-books/AUTHOR-BRIEF-, FIX-BRIEF-, REVIEW-BRIEF-, LINKS-BRIEF-2026-10-31.md` | The rules that produced the content; reuse them for new subjects. |

## Content (in `web/1031-keycards`, `data/keycards/`)
- **Published: 5,721 cards.** Accountancy 863, Business Studies 875, Economics 1,184, Biology 1,392, Political Science
  1,089, English 318. **Quarantined: 137**, each with its reason (`data/keycards/quarantine/`).
- Every published card passed machine checks 1-5 (quote exact on the cited printed page, shape, blanks, duplicates,
  CUET 2026 syllabus) and an independent reviewer (check 6). Flag rate fell from 24% (round 1) to about 10% with the new
  author brief; every flagged card went through one fix pass and a re-review.
- **Every pilot chapter has cards** except the two with no NCERT text by design: Computerised Accounting and Business
  Studies "Financial Markets". Thinnest: Accountancy "Change in Profit Sharing Ratio" (10 cards).
- **Links ("The line you needed"):** 1,632 live questions linked (Accountancy 847, Economics 253, Business Studies 225,
  Biology 208, Political Science 99). Only links where the card's text decides the answer; the rest fall back to the
  word match.

## Code changes this session (on `web/1031-keycards`, all with tests)
- Quote check reads a second extraction (`scripts/keycards/pdfium_pages.py`, pdfium reading order): pdftotext
  interleaves two-column pages and side boxes, which had cost whole key sentences.
- New check `shape:front_dangling`: a front that starts with It/This/Thus/However or a lowercase fragment is quarantined.
- Running heads up to 120 characters are stripped (Accountancy's even-page head is 71), so cross-page quotes pass.
- Published cards take their chapter name and CUET unit from syllabus v2 (drafts and reviews unchanged).
- Key cards read syllabus v2 by a static import; the webpack ignore hack is gone. `.gitattributes` keeps deck, links
  and manifest bytes exact (they are sha256-checked).
- Web polish: no middle-dot strings (owner rule T-124), ellipsis on backs that start mid-sentence, Revise and Today
  copy, phone deck header. App: Revise entry shows when only cards are due; Free "line you needed" limit shows the Pro gate.

## Verification (integration head 90fddb40d)
test:keycards 42, keycards-ui 10, syllabus 22, nta 229, subjects 60, learning 357, today 120, egress 101, recovery 637
(3 known todo), study 61/62 (the WordNet licence test also fails on the base branch), lint clean, `next build --webpack`
passes. The landing heroScene test fails on base too (CRLF in this checkout).
Screens: web shots at 390 and 1440, Night and Day, in `wt-1031-kc-ui/tmp/walk-1031/web/` (looked at); app goldens in
`wt-1031-keycards-app/flutter_app/test/golden/keycards/goldens/` (looked at). They use fixture cards (real NCERT lines),
not the full decks.

## Re-tag pass (syllabus v2), read-only on production
- 525 live questions in retired or split chapters: **85 re-tagged** to live chapters (`data/syllabus/retag-2026-10-31.json`),
  **440 leave the pools** when the migration runs. Table: `docs/brain/intel-1031/RETAG-2026-10-31.md`.
- **Pools that shrink most:** Biology 451 to 369 (-18%), Chemistry 466 to 395 (-15%), Computer Science 387 to 331
  (-14%), Political Science -29. Chemistry loses six whole chapters. **This is for the owner to see before the migration.**

## Found along the way (not fixed; need the content pipeline)
- **Probable wrong answer keys** (stored answer disagrees with NCERT): accountancy `2370d28b`, `b29a66fb`, `01dc09dc`,
  `577f9005`, `d0e86513` (id prefixes).
- **Many questions sit under the wrong chapter** (Business Studies "Nature & Significance of Management" and "Business
  Environment", Economics micro chapters, Biology "Evolution"). A chapter re-tag pass for live chapters would sharpen
  chapter state and practice by chapter.
- Coverage gaps the decks cannot fill from NCERT text: debenture redemption, sinking fund, bonus and rights shares,
  Financial Markets.

## Next, in order
1. **Show the owner the screens** (web shots + app goldens) and the pool numbers above. His decisions: the flag on, and
   whether the pool shrink is acceptable or should wait for new questions.
2. **Real-deck preview:** a dev-only mode that feeds the bundled decks to the web preview, then shots of real chapters
   (the current shots use the 6-card fixture).
3. **Production** (owner standing DB authority, 14 Oct): dry-run then apply `20261031130000_syllabus_v2.sql` (with the
   re-tag file) and `20261031140000_key_cards.sql`, undo saved; check every subject's mock pool; merge
   `web/1031-keycards` to main and deploy with `KEY_CARDS_ENABLED` off; turn it on only after the owner has seen the screens.
4. **App version 17:** demo-mode emulator walk (2-3 GB AVD) with screenshots against the owner ledger, then the build.
5. Content: second fix round on the 137 quarantined cards (optional); fix the 5 answer keys; chapter re-tag of
   mislabelled live questions; English links; question fill toward 40 per chapter (ask the owner for the USD 500 key).

## Rules that bit this session
- Concurrent subagent cap is 20. Sonnet subagents burned about 1% of the 5-hour window per minute at 6-9 at once;
  20 at once ran about 2.5% a minute.
- Subagents share the scratchpad: give each its own folder (`kc-<code>-<role>`).
- The Read tool cannot render PDFs here (no pdftoppm); agents render pages with pypdfium2 to PNG.
- Reviewers can be wrong on chapter assignment: CUET units, not NCERT chapters, decide it (for example revenue and
  producer's equilibrium sit under Production and Costs).
