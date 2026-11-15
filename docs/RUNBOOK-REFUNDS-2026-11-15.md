# Refund runbook (M4, 15 Nov 2026)

Webhook events to tick in Razorpay (Live, Account and Settings, Webhooks): `refund.processed`, `payment.dispute.created`,
`payment.dispute.won`, `payment.dispute.lost`, `payment.dispute.closed` (plus the ones already ticked).

What the site does by itself (`src/app/webhook/route.js`, `processMoneyBackEvent`):

- Every refund and dispute is recorded once in `audit_logs` (`billing.refund_processed`, `billing.dispute`, target = our payment row).
- Full refund of the payment that pays for the current Pro month or a one-time pass: Pro for that payment ends now
  (audit row `billing.refund_revoked_premium` + the existing revoke). A monthly subscription is also cancelled at once at Razorpay.
  Other paid access (a pass, another subscription, Google Play) keeps Pro to its own date.
- Partial refund, refund of an earlier month, any dispute: recorded only. Access does not change.
- Credit pack refunded: the credits are taken back from what is unspent, never below zero, shortfall kept in the ledger,
  once migration `20261115120000_razorpay_refund_credit_takeback.sql` is applied.

Manual steps (clearly marked):

1. MANUAL, until migration 20261115120000 is applied: a refunded credit pack shows as `billing.refund_credits_manual` in
   `audit_logs`. Apply the migration (with its undo saved), then run, once per such row (service role, SQL editor):
   `select public.mm_ai_take_back_refunded_credits('<user id>', <credits>, '<order id>', 'razorpay_refund:<payment id>', '{"source":"manual"}');`
   The answer says how many credits came back and the shortfall.
2. MANUAL: a lost dispute (`billing.dispute` with `disputeStatus` 'lost') does not end access by itself. If the money is
   gone and access should end, insert the revocation (every later event and verify then keeps that payment's access off):
   `insert into audit_logs (action, target_type, target_id, metadata) values ('billing.refund_revoked_premium', 'user', '<user id>', '{"paymentId":"<payment id>","key":"revoked:<payment id>","source":"manual_dispute"}');`
   then set the user's plan by hand only if no other paid access exists. Cancel the subscription in the Razorpay dashboard.
3. To refund a month but keep the subscription running, refund a partial amount (less than the full charge): it is recorded only.
