---
name: mockmob-differentiator-decision-oct-2026
description: "Oct 2026 Score Recovery direction, owner budgets/names, AI live in prod DB, and traps found while unblocking AI"
metadata:
  node_type: memory
  type: project
  originSessionId: 211e0761-691c-4fa4-abce-e4dad380fcc1
  modified: 2026-10-03T19:16:11.403Z
---

Owner plan (4 Oct 2026, docs/brain/PLAN-2026-10-04-NEXT-DAYS.md): Night 1 Score Recovery + AI; Day 2 AI-verified error-free questions + NTA mode; then Google Play app (Android only). Names: marketing "Score Recovery", feature "Score Recovery Lab", action "Mistake Repair". Owner rejected "Repair that holds" (vague) for public copy.

Budgets set by the owner: student AI USD 25 per IST month (DB-enforced, runtime_ai_budget.monthly_cap_usd); content generation USD 50 lifetime (budgetLedger.mjs). Owner explicitly complained that agents invent stricter constraints from the brain — treat these as the limits and ask before tightening.

Non-obvious facts:
- Production Supabase is the only project (isrxrxzjocewrdureyhp). AI migrations applied 4 Oct with owner OK; learning/recovery migrations are NOT applied (they add triggers on live `questions`).
- The configured ANTHROPIC_API_KEY returned 401 on 4 Oct; routing is OpenAI (gpt-4.1-mini / gpt-4o-mini) until the owner replaces it.
- Sonnet 5.5 rejects custom temperature and thinks by default; GPT-5 models reject temperature/max_tokens — providers.js handles Claude per model, avoid GPT-5 without code changes.
- `RELEASE_GATES.aiCommerce` (false) separately gates top-up checkout and charged Rival battles; runtimeAi (true) only opens replies.
- Never add sources to `data/source_registry.json` casually: the paid content worker treats an empty `sources` map as a pause condition.

Owner tested the Lab on 4 Oct, rated it 5/10: wants summary + Pip first, Lab second, answers last; hates tall pages and abstract widgets (the replay slider) with no clear use. Every Lab element must tie to a concrete action. Owner offered Opera access for signed-in tests; the in-app browser cannot sign in, so use the /preview/arena?view=result fixture locally.

**Why:** these change what is safe to build and claim.
**How to apply:** read the plan file first each session; keep `differentiatorClaimable()` false until evidence exists. Related: [[mockmob-pricing-and-prepos-decisions-oct-2026]], [[mockmob-round4-oct-2026]].
