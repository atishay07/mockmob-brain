# Credits wallet: what the owner wires for Razorpay (D76 and D78, 18 Oct 2026)

ONE credits balance. The wallet is built and closed: packs show their prices; no order is created until you turn the flag on. Everything below is what is left for you.

## 1. Keys and the flag (Vercel env)

| Variable | Value | Notes |
| --- | --- | --- |
| `RAZORPAY_KEY_ID` | your key id | already used by Pro checkout; the wallet reuses it |
| `RAZORPAY_KEY_SECRET` | your key secret | signs and verifies `order_id|payment_id` |
| `RAZORPAY_WEBHOOK_SECRET` | the webhook secret | required by the existing `/webhook` route |
| `WALLET_COMMERCE_OPEN` | `true` | the only switch. Anything else (or unset) = closed: no order, no payment row, keys say "Top-ups open soon" |

`WALLET_COMMERCE_OPEN` governs both order routes: `POST /api/wallet/order` and the older `POST /api/ai/credits/order`, which also still needs `RELEASE_GATES.aiCommerce` (CAPABILITIES.aiTopUps) and sells only live packs. Either gate closed = no order. Flipping `aiCommerce` alone opens nothing.

## 2. Webhook

Endpoint: `POST https://<your domain>/webhook` (already live for Pro). Credit packs use `payment.captured` and `payment.failed`; nothing new to subscribe to if Pro already uses `payment.captured`. The webhook finds a credit pack from the stored order's plan id (`credits_10_50`, `credits_29_150`, `credits_49_300`, and the retired `ai_credits_prepos_*` ids for old orders). Verify and the webhook share the grant key `ai_topup:<order id>:<payment id>`, so a payment adds credits once even when both arrive.

## 3. Packs and the database

One set, usable for everything, in one file: `src/services/credits/creditPacks.mjs` (Rs 10 -> 50, Rs 29 -> 150, Rs 49 -> 300 featured). Packs are `credits_10_50`, `credits_29_150` and `credits_49_300` (owner D82). The server prices every order from it. A purchase is granted through the existing AI purchase grant (`mm_ai_grant_bonus_credits`) into the held balance. This branch adds no migration; the unified balance math and any database change belong to the core credits work.

## 4. Routes

| Route | Purpose |
| --- | --- |
| `GET /api/wallet` | one read for the page and the Android app (cookie or bearer) |
| `POST /api/wallet/order` `{ packId }` | validates the pack id server-side, creates the Razorpay order; 503 `WALLET_COMMERCE_CLOSED` while the flag is off. Cookie only |
| `POST /api/wallet/verify` `{ razorpay_order_id, razorpay_payment_id, razorpay_signature }` | checks the signature and Razorpay's own record of the payment, then grants once. Not gated by the flag: a payment already taken is always settled. A row already `captured` is never set back to `failed` by a replayed bad signature or mismatched payment. Cookie only |
| `POST /api/ai/credits/order` | the older order route, same order step; closed unless `WALLET_COMMERCE_OPEN=true` and `RELEASE_GATES.aiCommerce` are both on. `/api/ai/credits/verify` has the same captured-row guard |

The app does not sell credits in v1 (Play billing rules), so order and verify take no bearer token; the app reads `GET /api/wallet`.

## 5. GET /api/wallet (the app reads this; field names are stable: add, never rename)

Cookie or `Authorization: Bearer <app token>`. `Cache-Control: no-store`. Read-only: it never writes, spends, grants or orders. Exact body (illustrative values, a Free student, top-ups closed):

```json
{
  "ok": true,
  "credits": {
    "total": 108,
    "freeLeft": 38,
    "freeAllowance": 50,
    "held": 70,
    "resetAt": "2026-10-31T18:30:00.000Z",
    "renewsOn": "2026-11-01",
    "parts": { "included": 38, "bonus": 30, "balance": 40 },
    "label": "Credits",
    "buys": "1 credit = 1 question or 1 Ask Mobi reply. A full mock is 50."
  },
  "plan": { "name": "Free", "until": null },
  "proOffer": { "rupees": 99, "expires": "31 July 2027", "planId": "pro_cuet_2027" },
  "packs": [
    { "packId": "credits_10_50", "label": "50 credits", "credits": 50, "priceInr": 10, "pricePaise": 1000, "perCreditInr": "0.20", "fullMocks": 1, "featured": false },
    { "packId": "credits_29_150", "label": "150 credits", "credits": 150, "priceInr": 29, "pricePaise": 2900, "perCreditInr": "0.19", "fullMocks": 3, "featured": false },
    { "packId": "credits_49_300", "label": "300 credits", "credits": 300, "priceInr": 49, "pricePaise": 4900, "perCreditInr": "0.16", "fullMocks": 6, "featured": true }
  ],
  "commerce": { "open": false, "message": "Top-ups open soon." },
  "history": [
    { "at": "2026-10-18T10:10:00.000Z", "pool": "practice", "what": "Practice set", "delta": -10, "balanceAfter": 108 }
  ],
  "historyState": "ready"
}
```

Field by field:

| Field | Type | Meaning |
| --- | --- | --- |
| `ok` | `true` | always true on a 200 |
| `credits.total` | int or `null` | `freeLeft + held`: what the student can spend. `null` when any part could not be read: never draw it as 0 |
| `credits.freeLeft` | int or `null` | this month's free credits left (equals `parts.included`) |
| `credits.freeAllowance` | int or `null` | this month's free allowance (50) |
| `credits.held` | int or `null` | credits the student holds, never expire: `parts.bonus + parts.balance` |
| `credits.resetAt` | ISO instant or `null` | when the free credits come back (the IST month end) |
| `credits.renewsOn` | `"YYYY-MM-DD"` (India time) or `null` | the same instant as an India date |
| `credits.parts` | `{ included, bonus, balance }`, ints or `null` | spend order: free credits first (`included`), then bought (`bonus`, the AI bonus balance), then held (`balance`, `users.credit_balance`) |
| `credits.label` | string | always `"Credits"`: the one name |
| `credits.buys` | string | the one sentence on what a credit buys; the full-mock price comes from the practice price list |
| `plan.name` | `"Free"` or `"Pro"` | |
| `plan.until` | `"YYYY-MM-DD"` (India time) or `null` | the Pro end date |
| `proOffer` | `{ rupees, expires, planId }` or `null` | the WEB Pro offer; `null` for Pro students |
| `packs[]` | see example | the WEB packs, priced by the server from `creditPacks.mjs`. `perCreditInr` is a string with two decimals; `fullMocks` is whole full mocks the pack pays for |
| `commerce.open` | bool | `WALLET_COMMERCE_OPEN` is exactly `true` |
| `commerce.message` | string or `null` | `"Top-ups open soon."` while closed |
| `history[]` | array of 20 or `null` | newest first. `delta` is signed credits; `balanceAfter` is the running total of this one balance counted back from today's total (`null` when the total is unknown); `pool` (`"practice"` or `"ai"`) only names the ledger a line came from; `what` is already in credit wording |
| `historyState` | `"ready"` or `"unavailable"` | a failed history read leaves the balances intact and sets `history: null` |

Errors: `401 { "error": "Unauthorized", "message": "Please sign in." }` when signed out; `503 { "error": "unavailable", "message": "..." }` when the student cannot be read.

Anti-steering (rule from D72; the Play prices, Pro Rs 150 and packs Rs 15, 45 and 75, are D82): `proOffer`, `packs` and `commerce` are the website's own prices and checkout state. The Android app must never draw them: its Pro and pack prices come only from Google Play (Pro Rs 150, packs Rs 15, 45 and 75). The current app (`wallet_data.dart`) reads only `credits`, `plan`, `history` and `historyState`.

`total = freeLeft + held`; `held = parts.bonus + parts.balance`; `parts.included = freeLeft`.

### Compatibility with the credits core

This branch carries two stand-ins that the release 10 merge replaces with `wt-credits-core`'s files, with no change to the wallet:

- `src/services/credits/creditPacks.mjs` is a byte copy of the core's catalog (`CREDIT_PACKS`, `LEGACY_AI_PACKS`, `PLAY_PRODUCT_IDS`, `findCreditPack`, `findBuyableCreditPack`; a pack is `{ key, planId, playProductId, label, shortLabel, amountInr, amountPaise, credits, featured, legacy }`). The wallet imports only those names and reads a pack by `key`; the "N credits" title, the per-credit value and `fullMocks` are built in `src/lib/wallet/walletPacks.mjs`. A test (`compat with the credits core`) fails if a wallet file imports anything else.
- `src/services/credits/unifiedWallet.js` returns the core's shape, `{ known, total, freeLeft, freeAllowance, resetAt, held, parts: { included, bonus, balance }, wallet }`. The route reads `parts` and the totals. The core's version also fixes the sum: it reads `users.credit_balance` inside `readAIWallet`, so take its `aiCreditWallet.js` and `aiWalletState.js` with it.
- `src/services/credits/aiCreditWallet.js` here only swaps its pack list for the catalog (the same lines as the core's `withStatus` and `findCreditPack`); on conflict take the core's whole file.

## 6. Test before opening

The live `/wallet` page has only been checked on `/preview/arena?view=wallet` fixtures (the shell's top bar now draws one credits chip, the same total as the page; on the release 10 merge the core's `AppLayoutClient` draws the same single chip, linked to `/pricing/ai-credits` there, so keep the `/wallet` link). The real Razorpay checkout, a real signature and a real grant have not been run. Do the steps below on a preview deploy before `WALLET_COMMERCE_OPEN` is set to `true` in production.

1. Set test keys and `WALLET_COMMERCE_OPEN=true` on a preview deployment.
2. Buy `credits_29_150` with a Razorpay test card: the balance rises by 150 and one "Credits added" line appears; replay the verify call: nothing is added.
3. Turn the flag off: the keys read "Top-ups open soon" and `POST /api/wallet/order` answers 503.
