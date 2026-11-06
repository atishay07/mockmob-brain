# Your steps tonight, 16 Oct 2026

Three jobs (the fourth turned out to be done already). Each says what you do, what to send me, and what I do next. Never paste a secret (a key, a password or a connection string) into the chat. Put secrets only where a step says.

## 1. Razorpay monthly plan (TEST first), about 10 minutes

1. Razorpay Dashboard, switch the top toggle to **Test mode**.
2. Subscriptions, Plans, Create Plan:
   - name `MockMob Pro monthly`;
   - Monthly, every 1 month;
   - amount 99 INR;
   - description `MockMob Pro, billed monthly`.

   If Subscriptions is missing from the menu, use the activation button on that page. Live subscriptions can need Razorpay's approval, so start that now.
3. Copy the **Plan ID** (`plan_...`) and send it to me in chat. A plan ID is not a secret.
4. Still in Test mode, open Account and Settings, then API Keys, and generate a test key. Put both values in a new file, `C:\Users\atish\Desktop\mockmob copy\wt-batch2\.env.razorpay-test.local`, as two lines:
   ```
   RAZORPAY_KEY_ID=rzp_test_...
   RAZORPAY_KEY_SECRET=...
   ```
   This file is ignored by git and never leaves this PC. Tell me "test keys saved". Do not paste them in chat.
5. Webhooks (Live mode): the existing webhook must point at `https://www.mockmob.in/webhook`. Tick these events:
   - `subscription.authenticated`, `subscription.activated`, `subscription.charged`, `subscription.pending`, `subscription.halted`, `subscription.paused`, `subscription.resumed`, `subscription.cancelled`, `subscription.completed`;
   - `payment.captured`, `payment.failed`.

**Then I run the TEST purchase** (runbook `RUNBOOK-MONTHLY-BILLING-2026-10-16.md`, part 2):
- a local site on this PC against the staging database, with the test account `app-e2e-student@example.com` (never a new account);
- Razorpay's published test card, run headless;
- every webhook event simulated;
- cancel, the second-purchase refusal, a bad signature;
- cleanup.

I report each step as pass or fail.

**Only after that passes:** create the same plan in **Live mode**, add `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` = the LIVE plan ID in Vercel (Production), and tell me. I redeploy and check `/pricing`. Rollback is removing that variable.

**The 6 old accounts:**
- All six paid once for a month in May 2026. Their paid dates ended 1 to 4 June 2026.
- They stayed Pro only because of the old "active means forever" rule.
- My recommendation: leave them on Free. That matches what they paid for.
- Say if you want any of them kept on Pro.

## 2. Weekly backup (SUPABASE_DB_URL), about 10 minutes

1. Supabase dashboard (production project), **Connect**, **Session pooler** (port 5432). Copy the connection string, with your database password in it.
2. Windows Settings, System, About, Advanced system settings, Environment Variables. Under **User variables**, click New:
   - name `SUPABASE_DB_URL`;
   - value: the string.
3. Install the PostgreSQL **Command Line Tools**, version 17 or newer, from postgresql.org/download/windows. Tick only Command Line Tools. Add `C:\Program Files\PostgreSQL\17\bin` to your user PATH.
4. Tell me "backup set".

**Then I run** the dry run and then the first real backup. The backup only reads the database. You get the file size and table count. After that, I ask you once before scheduling it weekly (Sunday 03:30).

## 3. Play developer account and upload key, about 20 minutes plus Google's checks

1. Register at play.google.com/console (one-time fee, identity check), with contact email `support@mockmob.in`. Tell me which account type it is (personal or organisation).
2. Tell me when you are at the PC with 5 minutes. Then you run one command in a terminal: `tool\make_upload_key.ps1` in `mockmob-next\flutter_app`. It asks for a password that only you type. Save the `.jks` file and its password in two separate places. Never send them to anyone.
3. Google Cloud, Credentials: copy the **Web application** OAuth client ID and send it to me. It is not a secret.

The 14-day closed test with 12 to 20 testers starts at the first upload, so this step is the long pole.

## 4. CUET_EVIDENCE_SIGNING_KEY: already done, nothing to do

The key is already set in Vercel production (checked by name on 16 Oct; its value was not read). Vercel verified 653 of 666 signed evidence records last night, so it matches the factory's key. The `nta_question_index` table was applied to production at about 14:00 and built, then switched off at 14:55 after a signature mismatch made it reject its own rows (no student was affected). It goes back on once the fix is deployed and checked.

## Your own testing

- **A fresh timed mock, then one repair.** This verifies Mistake Repair v4 live. Tell me when you have done the repair. I check the live logs for `/api/recovery/check` and the receipt calls at once, and report what happened.
- **The landing on a local server:** I send you the link once it scores 90 or more. Nothing goes live without your OK.
- **The app, v12:** I send it with a pass or fail list of all 39 items and screenshots. It goes on your phone only when you say the phone is connected.
