# AI cost per paid user: audit, 17 Oct 2026 (USD 1 = Rs 88)

**Owner's rule (17 Oct):** "For 50 credits in total, however the user finds it... it doesn't cost us more than 5-10 rupees in total API usage per paid user. This has to be a confirmed figure."

## Facts

**Grants.** Source: `src/services/credits/aiCreditWallet.js` and the wallet RPCs.

| Plan | AI credits |
|---|---|
| Free | 10 a month |
| Pro (Rs 99 season pass, or the monthly plan) | 50 a month while paid-through, resetting on the 1st (IST), no rollover |

- A season pass bought in October runs to 31 Jul 2027, so it gives up to **500 credits**, not 50.
- The 64 current payers expire on 31 Dec 2026: up to 150 credits each.
- Top-ups (50 for Rs 10, 150 for Rs 20, 400 for Rs 50) are paused in code (`RELEASE_GATES.aiCommerce` false).

**Model paths.**
- Every paid call runs on gpt-6-luna ($0.10 / $0.50 per million tokens); Repair can fall back to claude-haiku-5-5 at the same price.
- No route uses gpt-4.1-mini or Sonnet.
- Every credit action costs 1 credit. The "smart" Ask Mobi modes are also charged 1, not the 3 in `CREDIT_COSTS`.
- Up to 3 physical calls per action: the primary, a JSON retry, then a fallback.
- A disputed repair adds a 3-call blind key-check, which is free to the student.
- Failed or unusable replies release the credit, but the calls still cost us.
- The rival intro and outro and moderation make no calls today.

**Measured** (production `runtime_ai_requests`):

| Measure | Cost per call |
|---|---|
| Live Luna repairs, average | USD 0.000307 (Rs 0.027) |
| Live Luna repairs, max | USD 0.000479 (Rs 0.042) |
| Blended, with released-credit overhead, per credit | USD 0.000415 (Rs 0.0365) |

Actual cost runs at about 13% of the guard's reservation.

## The figure

**50 credits:**

| Case | Cost |
|---|---|
| Typical | Rs 1.4-1.8 |
| At the measured max call | Rs 2.1 |

The rule holds with about a 5x margin.

**Theoretical worst case for 50 credits,** if every credit fires the full 3-call ladder at the guard's bounds: Rs 33 (repair, largest question) to Rs 57 (Ask Mobi smart at a 30 KB input). This has not been seen in use.

**Whole season:**

| Case | Cost |
|---|---|
| Up to 500 credits, all used, typical | Rs 13.5-18.3 |
| 150 credits (current payers) | Rs 4.1-5.5 |

**Gaps:**
- No per-user rupee cap exists. `runtime_ai_requests` has no `user_id`.
- Released-credit loops (retrying a failing or disputed question) are bounded only by a per-instance 12/min limit, unless `PERSISTENT_LIMITS_ENABLED` is on.
- The global guard is USD 25 a month for all students. A loop could pause AI for everyone.

## Fix (decided by the main session; build on a branch, gate, deploy)

1. **Per-user rupee cap in the guard (the hard guarantee).**
   - Add `user_id` to `runtime_ai_requests` and to `reserve_runtime_ai`.
   - Refuse a reservation when that user's month-to-date `coalesce(actual_usd, reserved_usd)` plus the new reservation exceeds the cap.
   - Cap: Rs 10 (USD 0.1136) a month for paid users, Rs 1 (USD 0.0114) for free users.
   - Typical use reaches the paid cap only after about 270-370 credits, so it only stops loops.
   - On refusal the student sees an honest message and is not charged.
2. **Cut the reasoning headroom** (Repair low and smart Ask Mobi) from 2,500 to 1,000 tokens. The measured max completion was 754 tokens.
3. **At most 2 physical calls per charged action.**
4. **Cap the Ask Mobi context** at about 12 KB.
5. **Turn on `PERSISTENT_LIMITS_ENABLED`** (owner's switch, recommended).
6. **Re-verify the Luna price row before about 1 Jan 2027.** The guard rejects price rows older than 90 days.

**Owner decision open:** is "50 credits" meant as 50 in total per paid user (the owner's words) or 50 a month (what the code and the pricing copy say)? If it is 50 in total, the grant changes and the pricing copy changes with it. The per-user cap protects the money either way.

## Owner decision, 17 Oct about 2:15 am IST

- Credits: Pro stays at 50 AI credits a month; Free stays at 10 a month.
- Models: only gpt-6-luna and claude-haiku-5-5, anywhere in the app or the website. This is enforced in code and in reserve_runtime_ai on branch fix/ai-user-cap-1017.
- Paid cap: **Rs 5 a month** (USD 0.0568), down from the Rs 10 the branch defaults to. Set it with one UPDATE of the student_user_paid row in runtime_ai_budget right after applying the migration.
- Free cap: Rs 1 (USD 0.0114).
- Typical use is about Rs 2 a month, so the cap only stops runaway loops.

## Owner decision, 17 Oct about 3:10 am IST: the global ceiling is removed

- His words: "remove the Rs 2,200 ceiling... The realistic cap is until my API credits run out."
- Done on production: `update runtime_ai_budget set monthly_cap_usd=1000000 where id='student_ai'`. Effectively no ceiling. A number was kept rather than NULL because the readiness scripts expect a positive value.
- The per-student caps stay: Rs 5 a month paid (0.0568), Rs 1 a month free (0.0114).
- The owner gets notified through the low-balance and billing alerts in the OpenAI and Anthropic consoles.
- AGENTS.md still says "USD 25 per IST month". Update that line in the next website deploy.
