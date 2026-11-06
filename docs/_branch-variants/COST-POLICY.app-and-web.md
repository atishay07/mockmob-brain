# Persistent incremental content budget

> **Owner update, 4 Oct 2026:** content generation ceiling is USD 50 lifetime
> (`CONTENT_LIFETIME_CEILING_USD`); student-facing AI is funded at USD 25 per IST month, enforced
> by `reserve_runtime_ai` in production. Older $10 figures below are superseded.

Hard lifetime ceiling: $10. Initial ledger allowance: $2 for calibration. Session
authoring consumes the owner's existing session usage; it is not a free API. Store
fees, hosting and subscription charges are tracked separately and are not included.

BudgetLedger uses integer micro-dollars, SQLite WAL and BEGIN IMMEDIATE. All paid
workers/providers must share the SAME durable CUET_BUDGET_LEDGER path. Back it up;
never reset/delete/rotate it to get fresh allowance. Do not use ephemeral Vercel
disk or separate machine copies. Distributed content dispatch remains unavailable.

Each physical transport request reserves the maximum configured input plus output
cost before sending. SDK retries are disabled; any explicit repair/helper/fallback
request still enters this transport and creates a separate reservation. Actual
usage reconciles the reservation and records provider/status/token usage/prices.
Missing usage, network uncertainty, overruns or abandoned reservations from a dead
worker block further dispatch. Active concurrent reservations still count in full.

data/pipeline-prices.json intentionally has no prices. For each approved model,
verify current official pricing AND full model input limit, then record:

```json
{
  "source_url": "official pricing page",
  "expires_at": "bounded ISO expiry",
  "models": {
    "exact-provider-model-id": {
      "provider_host": "exact.api.host",
      "input_per_million": 0,
      "output_per_million": 0,
      "max_input_tokens": 0
    }
  }
}
```

Zeros above are placeholders, NOT an approved free route. Unknown pricing/token
limits/host, missing output cap and streaming are blocked. Gemini/Anthropic content
transports remain paused until their billing endpoints have equivalent accounting.
Do not compensate by switching to an unguarded SDK or web moderation endpoint.

Budget release requires a real calibration report: independent fixtures, >=95%
valid survival, zero critical false accepts, every required category and disjoint
splits. releaseAfterCalibration can raise the persistent cap up to $10; it never
adds $10 per job. Reconcile unresolved requests from provider receipts, preserving
the original reservation and receipt trail, before reopening dispatch.

After two consecutive zero-yield chapter batches, assertRoute blocks the route.
One targeted repair per stable candidate is persisted across jobs. Failed repairs
remain quarantined. Cache keys include candidate/content, source, family and verifier
versions. Zero acceptance means undefined/infinite effective unit cost, never zero.

No paid content requests were made in this implementation. Historic bills cannot
be reconstructed from local aggregate reports alone. Current inventory check cost
is $0 incremental API spend; future semantic cost/yield is unknown until measured.
10,000 questions for $10 remains conditional. No volume quota may weaken a gate.
