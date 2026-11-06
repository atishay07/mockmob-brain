# Handoff: Key cards and the intelligence layer (31 Oct 2026, about 3:45 am IST)

**Session:** 3b7877eb, Claude Opus 5.5.

**Why it stopped:** the owner's usage reached 93%. Wave 1 (workflow `wf_80b94c0f-4c0`) was stopped, its leftover
Flutter test processes were killed, and every worktree was committed at a STOP POINT. Nothing is pushed, deployed or
written to production.

## Read first
- `docs/brain/INTELLIGENCE-LAYER-PLAN-2026-10-31.md`: the plan, with production numbers.
- **Owner decisions D200-D206** (end of `OWNER-MASTER-LEDGER.md`). In short:
  - CUET is the single reference, with NCERT chapters under its units.
  - There is no older-syllabus shelf.
  - Cards use NCERT's exact text with book, chapter and page.
  - The pilot covers 5-6 subjects.
  - The USD 50 ceiling is removed.
  - Free is a taste; Pro holds the value.
  - "The main thing that I really care about ... is the card and the feature."
- `docs/brain/intel-1031/`:
  - `KEYCARDS-BUILD-SPEC.md` is binding: branches, API contract, rules and the Free/Pro split.
  - `KEYCARDS-CONTENT-SPEC.md` holds the card kinds and checks.
  - `syllabus-verified.md` holds the rulings, each checked from two sides.
  - Supporting material: `syllabus-audit.md`, `rival-research.md`, `verify.json`.

## Where things are (all under `C:\Users\atish\Desktop\mockmob copy\`)

| Part | Branch / place | State |
|---|---|---|
| Ceiling removal | `web/1031-keycards` 528fe5e18 | Done; tests pass (budgetContinuation 11/11, questionFactory 65/65) |
| Integration branch | `web/1031-keycards` 812a6be6f (worktree `wt-1031-keycards-web`) | Specs copied in; nothing merged yet |
| Syllabus v2 | `web/1031-syllabus` 129c3b5b0 (`wt-1031-syllabus`) | 4 real commits: `data/cuet_syllabus.js`, canonical map from CHAPTERS, alias-aware validators, retired rows never served, migration + undo (generated, NOT applied), re-tag hook, tests. The top commit is a STOP POINT: the agent's stash, re-applied (cuet_syllabus, inventory_fingerprint). Review it and run the suites. |
| Key cards server | `web/1031-kc-server` 95e23f26d (`wt-1031-kc-server`) | 5 commits, clean: validate.mjs and review-merge.mjs (checks 1-6), pure rules, chapter state, routes behind KEY_CARDS_ENABLED, Revise/Today integration, 180-day simulation, route tests. The agent's final report was not received: re-run its test list. |
| Web screens | `web/1031-kc-ui` d59a336ae (`wt-1031-kc-ui`) | STOP POINT only: `/cards`, `/cards/[chapter]`, KeyCard, ChapterDeck, KeycardsHome, LineYouNeeded, fixtures, api.js, CSS, ChapterRows/Result/AppLayout edits, capture script `scripts/design-audit/keycards-1031-capture.mjs`. Unreviewed, no screenshots checked. |
| App | `ui/1031-keycards` 9d6cc2f3d (`wt-1031-keycards-app`, base `ui/1020-v16` = version 16) | STOP POINT: 66 files, +5,220 lines. Unreviewed; analyze and the tests were not confirmed. |
| NCERT PDFs | `ncert-books/pdf/` (74 files, Reprint 2026-27, not in git) | Accountancy, Business Studies, Economics (macro = leec1, micro = leec2, IED = keec1), Biology lebo101-113, Political Science leps101-107 and leps201-208, plus contents pages `*ps.pdf`. Download method: plain `node fetch` (curl gets reset; never spoof). |
| Card drafts | `ncert-books/drafts/*.json` (40 files) | english 322, economics 1,502, accountancy 1,055, business_studies 1,043 cards. `keec106.interleaved.json` is an agent scratch file: ignore it. |
| Reviews | `ncert-books/reviews/*.json` (35) | 3,475 cards reviewed, 839 flagged, so they quarantine. **Missing reviews:** leec102, leec106, leec202, leec204, leec205. |

**Facts found:**
- The current NCERT Business Studies Part 2 is Ch 9 Financial Management (lebs201), Ch 10 Marketing (lebs202) and
  Ch 11 Consumer Protection (lebs203). The book has **no Financial Markets chapter, but CUET 2026 lists it**. Keep it in
  the syllabus; it gets no NCERT cards.

## Next, in order
1. **Usage check first** (the 5-hour window reset at about 7:20 am IST on 31 Oct). Keep waves small.
2. **Reviews:** run the 5 missing reviews (leec102, leec106, leec202, leec204, leec205), one Sonnet agent each, using the
   same prompt as `review:<code>` in the wave-1 script
   (`~/.claude/projects/.../workflows/scripts/keycards-wave1-wf_80b94c0f-4c0.js`).
3. **Run the checks.** In `wt-1031-kc-server`, run `node scripts/keycards/validate.mjs` and then `review-merge.mjs`
   (see the script headers for arguments).
   - Read `data/keycards/coverage/*.json` and the quarantine reasons.
   - 839 of 3,475 flagged is high (24%). Sample the reasons.
     - If they are mostly fixable (page number, importance), run a fix pass on the flagged cards only. Use fresh author
       agents told to fix the listed reasons, then review again.
     - Never publish a flagged card.
4. **Review and finish each code part,** one owner each:
   - **Syllabus:** run `test:nta`, `test:recovery`, `test:subjects`, `test:learning`, lint.
   - **Server:** run `test:keycards`, `test:recovery`, `test:study`, `test:today`, `test:egress`, `test:app`, lint and
     `next build --webpack`.
   - **Web UI:** fix its build and run the screenshot loop at 390/1440, Night/Day. Look at every shot against the
     owner's UI standards.
   - **App:** run analyze and the keycards/learn/review tests and goldens. No emulator until the code is green; then
     a demo-mode walk (RAM rule: 2-3 GB AVD).
5. **Biology and Political Science decks:** run the same author + review pipeline over lebo101-113, leps101-107 and
   leps201-208.
   - **Stored chapter names, Political Science:** Alternative Centres of Power, Contemporary South Asia, End of
     Bipolarity, Environment & Natural Resources, Globalisation, International Organisations, Security in the
     Contemporary World, Challenges of Nation Building, Challenges to & Restoration of the Congress System, Crisis of
     the Democratic Order, Democratic Upsurge and Coalition Politics, Era of One-Party Dominance, India's External
     Relations, Politics of Planned Development, Recent Issues and Challenges, Regional Aspirations.
     - leps208 (Recent Developments in Indian Politics) feeds both "Democratic Upsurge and Coalition Politics" and
       "Recent Issues and Challenges", split by the CUET sub-topics.
   - **Stored chapter names, Biology:** Sexual Reproduction in Flowering Plants (lebo101), Human Reproduction,
     Reproductive Health, Principles of Inheritance & Variation, Molecular Basis of Inheritance, Evolution, Human
     Health & Disease, Microbes in Human Welfare, Biotechnology Principles & Processes, Biotechnology & its
     Applications, Organisms & Populations, Ecosystem, Biodiversity & Conservation (lebo113).
   - **Check the stored names against `data/cuet_syllabus.js` on `web/1031-syllabus` first.**
6. **Merge:** syllabus, then server, then UI, then content into `web/1031-keycards`. Then run the full suites and the
   build.
7. **Wave 2:** question-to-card links per pilot chapter (agents read live questions through the Supabase MCP,
   read-only) and the re-tag pass (retired and split chapters, written to `data/syllabus/retag-2026-10-31.json`).
8. **Production:**
   - Dry-run the syllabus v2 and key_cards migrations, then apply them (owner standing DB authority, 14 Oct; save the
     undo).
   - Check each subject's mock pool after retiring about 340 questions.
   - **Deploy behind `KEY_CARDS_ENABLED`. Turn it on only after the owner has seen the screens.**
9. **App version 17** after the device walk.
10. **Ask the owner for a USD 500 API key** when the question fill starts (about 3,500-4,300 questions to reach 40
    per chapter).
