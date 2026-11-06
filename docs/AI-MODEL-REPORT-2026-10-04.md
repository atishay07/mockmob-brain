# AI model report — student-facing replies, 4 October 2026

Question from the owner: which provider has the best, most efficient models for MockMob's student AI
(PrepOS replies, Score Recovery "Mistake Repair")? Workload: short grounded replies (~1–2.5k input
tokens, ~300 output), strict JSON, explanations that must agree with a verified answer key.

## Official prices (USD per million tokens, read 4 October 2026)

| Provider · model | Input | Output | Cached input | Source |
| --- | --- | --- | --- | --- |
| Anthropic · Claude Haiku 4.5 | 1.00 | 5.00 | 0.10 | [platform.claude.com pricing](https://platform.claude.com/docs/en/about-claude/pricing) |
| Anthropic · Claude Sonnet 5.5 | 2.00 | 10.00 | 0.20 | same |
| Anthropic · Claude Opus 5.5 | 4.00 | 20.00 | 0.20 | same |
| OpenAI · gpt-4.1-mini | 0.40 | 1.60 | 0.10 | [developers.openai.com pricing](https://developers.openai.com/api/docs/pricing) |
| OpenAI · gpt-4o-mini | 0.15 | 0.60 | 0.075 | same |
| OpenAI · gpt-5-mini | 0.25 | 2.00 | 0.025 | same (reasoning model: extra hidden output tokens) |
| DeepSeek · V4.1 Flash | ~0.30 | ~1.20 | ~0.006 | third-party aggregators only; not verified |
| Google · Gemini 3.1 Flash-Lite | ~0.25 | ~1.50 | — | third-party aggregators only; not verified |

## Estimated cost per reply and replies per USD 25/month

| Model | ≈ per reply (2.5k in / 350 out) | ≈ replies in USD 25 |
| --- | --- | --- |
| Claude Haiku 4.5 | $0.0043 | ~5,900 |
| Claude Sonnet 5.5 | $0.0085 | ~2,900 |
| gpt-4.1-mini | $0.0016 | ~15,600 |
| gpt-4o-mini | $0.0006 | ~41,000 |

Measured on production tonight (short prompts): gpt-4.1-mini $0.00007 per smoke reply; Mistake Repair on
10 real bank questions cost $0.0038 in total (≈ $0.0004 each), all 10 agreed with the stored key.
Reports: `reports/ai-live-smoke-2026-10-04.json`, `reports/mistake-repair-live-eval-2026-10-04.json`.

## Recommendation

- **Target: Claude Haiku 4.5 (fast) + Claude Sonnet 5.5 (smart, blind second opinions), gpt-4.1-mini
  fallback.** Best quality for careful, grounded explanations at a cost the $25 cap comfortably covers;
  a second provider gives outage resilience.
- **Tonight: OpenAI gpt-4.1-mini (both tiers) + gpt-4o-mini fallback**, because the configured Anthropic
  key returns 401. Verified working end to end through the budget guard.
- **Not chosen:** DeepSeek — student (mostly minor) data would be processed by a China-based provider,
  a DPDP and trust risk; Gemini — no runtime adapter yet and prices not verified first-hand; GPT-5 family —
  reasoning tokens make cost unpredictable and the current code sends `temperature`/`max_tokens`, which
  those models reject.
- **Question generation (Day 2) is a separate decision:** a strong generator plus a blind solver from a
  different model family; budget USD 50 lifetime.

## Switching to Claude once the key is fixed

1. Replace `ANTHROPIC_API_KEY` in `.env.local` and Vercel.
2. Set `AI_DEFAULT_PROVIDER=anthropic`, `AI_FAST_PROVIDER=anthropic`, `AI_FAST_MODEL=claude-haiku-4-5`,
   `AI_SMART_MODEL=claude-sonnet-5-5`, `AI_FALLBACK_PROVIDER=openai`, `AI_FALLBACK_MODEL=gpt-4.1-mini`.
3. Run `node --use-system-ca --env-file=.env.local scripts/learning/ai-live-smoke.mjs`. Prices for all
   three are already verified in `runtime_ai_prices` (valid 90 days, re-verify by 2 January 2027).
