# Chapter state: which surfaces should move to it later (31 Oct 2026)

**What this is:** `data/chapter_state.js` (KEYCARDS-BUILD-SPEC.md 2d) is a new read for the new screens only:
- the Key cards home (`GET /api/keycards`, each chapter's `state`)
- `GET /api/me/chapters`

In this release every other weak-chapter rule stays as it is. This note lists the surfaces that should move to chapter
state in a later release, so a chapter carries one state everywhere.

**Why move them:**
- Chapter state counts each question once, by its latest answer. It resolves aliases through the syllabus, skips retired
  chapters, uses the Wilson interval from `prepos_insights.js` and shows no percent below 6 answers.
- The rules below count differently (every wrong answer in a window of papers, or a fixed number of recent papers), so the
  same chapter can read "weak" on one screen and "Getting there" on another.

## Candidates

| Surface | Today | Move | Note |
|---|---|---|---|
| `data/prepos_insights.js` `computePrepOSInsights` (chapters ranked, used by `/api/prepos/insights`, Mobi standing, `TodayPaper.jsx`, mentor chat) | Ranks chapters by marks open from recent attempts | Take the state and label from chapter state; keep its marks ranking | Highest value: Today and Mobi name chapters from here |
| `data/mock_swot.js` (`SwotPanel.jsx`, the result screen) | Strengths and weaknesses from the mock's own chapters, Wilson on the mock's answers | Keep the per-mock view; add the chapter-state label as the "across your practice" line | Per-mock evidence must stay per-mock |
| `data/learning_weak.js` `weakChapters` (the guided plan, `src/lib/server/learning.js`) | Wrong answers in the newest 10 papers | Pick lessons for chapters in state `weak`, then `mid`, ordered by `marksLost` | Removes the 10-paper window |
| `data/review_chapters.mjs` `chapterRows` (Review) | Marks lost per chapter across papers | Keep it as the source of `marksLost` (chapter state already reuses it); add the state label beside each row | No change to the marks figures |
| `src/app/api/analytics/route.js` | Its own per-chapter accuracy | Return chapter state rows instead of a raw percentage | Removes a percent shown below 6 answers |
| App (`flutter_app` review and learn chapter rows) | Ports of the rules above | Read `/api/me/chapters` | After the web moves |

## Order and gates

1. **prepos_insights and Mobi standing first.** They name chapters to students most often.
2. **Then the guided plan and Review's label.**
3. **SWOT and analytics last.**

Each move needs:
- a parity test that the old and the new surface name the same chapters for the reference fixtures
  (`data/tests/fixtures/review/student-1018.json`)
- the owner's approval of the wording change
