# Google Play billing: your checklist to subscribe to Pro and buy a credit pack as a tester

Written 19 Oct 2026 for Atishay; Part 4 rewritten the same evening for the monthly subscription (your decision D135/D136). Goal: on your phone, as a licence tester, you subscribe to MockMob Pro (Rs 149 a month), see Pro unlock, watch it renew, cancel it, buy a credit pack and see the credits arrive, then refund Pro and see it switch off. Test purchases cost nothing.

**How to read this.** Each step says **YOU** or **US**. You do everything inside Play Console, Google Cloud and Vercel, because those are your accounts and agents never sign in to them. We build the app, prepare the database and check that each purchase landed. Tick the boxes as you go.

**Never paste a secret into chat.** The service account key and the RTDN token go straight into Vercel. What you send us back is safe to share: an email address, a topic name, fingerprints, and "done".

**Time.** About 1.5 hours of clicking in total, spread over two sittings. Google needs up to 24 hours to switch on the service account, so start with Part 2 today. If it activates quickly, you can buy the same evening.

---

## The upload key in two sentences

An **upload key** is a private file on this PC that proves a new app build really comes from you; Play checks it on every upload, then signs the app for students with its own **app signing key**, which Google keeps safe for you (that is **Play App Signing**). If you lose the upload key, the app is not lost, but you cannot publish an update until Google support resets it, which takes days, so back the key up in two places on the day it is made.

---

## Part 0. Done (your answers, 19 Oct)

- [x] **0.1 The upload key** is made: `C:\Users\atish\MockMob-keys\` (the key file, its password in `READ-ME-BACK-ME-UP.txt`, and `key.properties`). Backed up by him to a pen drive and Google Drive (19 Oct, done).
- [x] **0.2 The test Google account** is `atishay07jain@gmail.com`, the account on your phone's Play Store and your Play Console account.
- [x] **The MockMob app already exists** in Play Console.

---

## Part 1. Play Console basics (YOU, about 20 minutes)

Open https://play.google.com/console and sign in with your developer account.

- [ ] **1.1 Does the MockMob app exist yet?** Look at **All apps**.
  - **If you see MockMob:** open it. If it already has a release on any track, tell us now, because every new build must be signed with the same upload key as that release.
  - **If not:** click **Create app** and fill in:
    ```
    App name:          MockMob
    Default language:  English (India) – en-IN
    App or game:       App
    Free or paid:      Free
    ```
    Tick the declarations, then click **Create app**. "Free" is right: the app is free to install and sells Pro inside it. The package name `in.mockmob.app` is set by our first upload, not on this form.
  - **You should see** the MockMob dashboard.
- [ ] **1.2 Payments profile.** Go to **Settings** (the gear icon) > **Payments profile**. If a profile is already linked (your other app may have one), skip this step. If none is linked, click **Create payments profile** and enter your legal name, address, a contact and your public support details, then **Submit**. Play will not let you create products until a payments profile is linked.
- [ ] **1.3 Licence testers.** Go to **Settings** > **License testing**. Choose **Email lists** > **Create list**:
  ```
  List name:  MockMob testers
  Emails:     atishay07jain@gmail.com
  ```
  Tick the list, then click **Save changes**. You should see the list ticked. Your developer account is a licence tester even without this step.
- [ ] **1.4 Internal testers.** Open the MockMob app, then go to **Test and release** > **Testing** > **Internal testing** > **Testers** tab. Tick the `MockMob testers` list (or create one with the same Gmail), add your email as the feedback address and click **Save changes**. The opt-in link appears here after Part 3.

**Send us:** "Part 1 done", and whether the app already existed.

---

## Part 2. Google Cloud: the service account and notifications (YOU, about 40 minutes)

The service account is a robot Google account that lets www.mockmob.in ask Google, "Is this purchase real?" Pub/Sub is how Google tells our server about refunds.

Use **one** Google Cloud project for all of Part 2. Make it with the same Google account as Play Console and leave it outside any organisation. The reason: newer Google Workspace organisations (created on or after 3 May 2024) block service account keys and block the Play notifications account by default.

- [ ] **2.1 Project.** Go to https://console.cloud.google.com, click the project picker > **New project**:
  ```
  Project name:  mockmob-play
  Location:      No organization
  ```
  Click **Create** and make sure `mockmob-play` is selected at the top. Note the **Project ID** shown on the dashboard (it may have a number added, for example `mockmob-play-123456`).
- [ ] **2.2 Turn on the API.** Go to **APIs & Services** > **Library**, search for `Google Play Android Developer API`, open it and click **Enable**. You should see "API enabled".
- [ ] **2.3 Create the service account.** Go to **IAM & Admin** > **Service accounts** > **Create service account**:
  ```
  Service account name:  play-billing
  Service account ID:    play-billing
  ```
  Click **Create and continue**. Skip the optional roles (it needs none in Cloud) and click **Done**. Copy its email address. It looks like `play-billing@<project-id>.iam.gserviceaccount.com`.
- [ ] **2.4 Create its JSON key.** Click the `play-billing` account > **Keys** tab > **Add key** > **Create new key** > **JSON** > **Create**. A `.json` file downloads. It is a password: do not email it or paste it into chat.
  - If Google says key creation is blocked by an organisation policy, the project is inside an organisation. Go back to 2.1 and make the project with **No organization**.
- [ ] **2.5 Put the key in Vercel.** In Vercel, open the MockMob project > **Settings** > **Environment Variables** > **Add**:
  ```
  Key:           GOOGLE_PLAY_SERVICE_ACCOUNT_JSON
  Value:         (open the .json file in Notepad, select all, copy, paste here)
  Environments:  Production only
  Sensitive:     on
  ```
  Click **Save**, then delete the downloaded `.json` file from your Downloads folder. If it is ever lost, you just create a new key in 2.4.
- [ ] **2.6 Give it access in Play Console.** In Play Console, go to **Users and permissions** > **Invite new users**:
  ```
  Email address:  play-billing@<project-id>.iam.gserviceaccount.com
  ```
  Open the **App permissions** tab > **Add app** > choose **MockMob** > **Apply**, and tick:
  - **View app information (read-only)**
  - **View financial data**
  - **Manage orders and subscriptions**

  Click **Apply**, then **Invite user**. You should see the service account in the users list. It accepts by itself. **Google can take up to 24 hours to switch this access on.** Until then, a purchase check answers "not allowed", which is why this part comes first.
- [ ] **2.7 The RTDN token (a random password for the notification link)** is already made: open `C:\Users\atish\MockMob-keys\PLAY_RTDN_TOKEN.txt` and copy the long line. In Vercel, add it the same way as 2.5:
  ```
  Key:           PLAY_RTDN_TOKEN
  Value:         (paste the line from PLAY_RTDN_TOKEN.txt)
  Environments:  Production only
  Sensitive:     on
  ```
  The same file shows the full push URL you need in 2.10.
- [ ] **2.8 Pub/Sub topic.** In Google Cloud, go to **Pub/Sub** > **Topics** > **Create topic**:
  ```
  Topic ID:  play-rtdn
  ```
  **Untick** "Add a default subscription", then click **Create**. Copy the full topic name. It looks like:
  ```
  projects/<project-id>/topics/play-rtdn
  ```
- [ ] **2.9 Let Google Play publish to the topic.** On the topic page, open **Permissions** (or tick the topic and click **Show info panel**) > **Add principal**:
  ```
  New principals:  google-play-developer-notifications@system.gserviceaccount.com
  Role:            Pub/Sub Publisher
  ```
  Click **Save**.
- [ ] **2.10 Push subscription.** Go to **Pub/Sub** > **Subscriptions** > **Create subscription**:
  ```
  Subscription ID:   play-rtdn-push
  Cloud Pub/Sub topic:  projects/<project-id>/topics/play-rtdn
  Delivery type:     Push
  Endpoint URL:      https://www.mockmob.in/api/billing/play/rtdn?token=<paste the token from 2.7>
  Enable authentication:  off (for now)
  Enable payload unwrapping:  off  (important: our server reads the normal wrapped message)
  Retry policy:      Retry after exponential backoff delay
  ```
  Leave everything else as it is and click **Create**. Then copy something harmless over the clipboard so the token does not linger.
- [ ] **2.11 Switch on notifications in Play Console.** Open the MockMob app > **Monetize with Play** > **Monetization setup** > **Real-time developer notifications**:
  - Tick **Enable real-time notifications**.
  - **Topic name:** `projects/<project-id>/topics/play-rtdn`
  - **Notification content:** **Get notifications for subscriptions and all voided purchases**. Pro is a subscription now, so these messages are how the server hears about every renewal, cancel and refund. ("Get all notifications for subscriptions and one-time products" also works. It only adds purchase messages that we log.)
  - Click **Save changes**. Do not click **Send test message** yet: our endpoint stays switched off until Part 5, so the test would only show a failure.

**Send us:** the service account email, the full topic name, and "2.5 and 2.7 are in Vercel".

---

## Part 3. The first build with billing on (US, then YOU)

- [ ] **3.1 US: build.** We build v15.3 as build 10 (versionCode 10) with Play billing switched on, pointed at www.mockmob.in and signed with the upload key. We check it is not debug-signed and send you the file path, for example `flutter_app\build\release-archive\10\mockmob-1.0.15+10.aab`, plus the upload key fingerprints.
- [ ] **3.2 YOU: upload to Internal testing.** Go to **Test and release** > **Testing** > **Internal testing** > **Create new release**.
  - The first time, Play asks about the app signing key: keep the default, **Use Google-generated key** (Play App Signing).
  - Under **App bundles**, upload the `.aab` file. Release name fills in by itself (`10 (1.0.15)`). Release notes: `Play billing test build.`
  - Click **Next**, then **Save and publish**. If **Publishing overview** shows **Send changes for review**, click it.
  - **You should see** the release as "Available to internal testers". It is usually ready within minutes. The first release of a new app can take a few hours.
- [ ] **3.3 YOU: copy the app signing fingerprints (for later, not for the test).** Go to **Protected with Play** > **Play Store distribution** > **Go to Play app signing** (on older layouts: **Test and release** > **App integrity** > **App signing**). Under **App signing key certificate**, copy **every** SHA-1 and SHA-256 shown. New apps now get "quantum-ready" signing, which can show up to three keys. Fingerprints are public, so pasting them in chat is fine.

**Send us:** "uploaded", plus the fingerprints from 3.3.

---

## Part 4. Pro (a monthly subscription) and the three credit packs (YOU, about 25 minutes, after Part 3)

Play only lets you create products once a build with Play billing inside is published to a track, and once the payments profile is linked. Product IDs can never be changed or reused, so copy them, do not retype them.

**Do not create a one-time Pro product.** Pro on Play is only the monthly subscription below. If you already made a one-time Pro product, leave it **Inactive** and never activate it.

### 4A. Pro: the monthly subscription

- [ ] **4A.1** Go to **Monetize with Play** > **Products** > **Subscriptions**, then click **Create subscription**.
- [ ] **4A.2** Fill in these two, then click **Create**:
  ```
  Product ID:  pro_monthly
  Name:        MockMob Pro
  ```
- [ ] **4A.3** Click **Edit subscription details**. Under **Benefits**, add these four lines (Play allows four, each up to 40 characters, with no prices or trials), then click **Save changes**:
  ```
  Unlimited mocks from one question bank
  Smart practice on the chapters you miss
  The exam-day screen, as on the day
  Easy, Medium and Hard sets
  ```
  Leave **Description** empty (students never see it) and leave **Icon** as it is.
- [ ] **4A.4** Back on the subscription, click **Add base plan** and fill in:
  ```
  Base plan ID:    monthly
  Type:            Auto-renewing
  Billing period:  Monthly
  ```
  - **Grace period:** leave Google's default.
  - **Account hold:** leave Google's default (on).
  - **Resubscribe:** leave it **on**, so a student whose Pro ended can start again from the Play Store.
  - **Billing plan and offer changes:** leave the default.
  - Do **not** add an offer or a free trial. The app sells the base plan only.
- [ ] **4A.5** Under **Price and availability**, click **Manage country/region availability**, tick **India**, and click **Apply**. (You may tick other countries too. Play converts the price for them.)
- [ ] **4A.6** Click the pencil in the **Price** column for **India**, enter **149** (INR), and click **Save**. If Play shows the price both with and without tax, the price the student pays must read **₹149**.
- [ ] **4A.7** Click **Save**, then **Activate**. **You should see** the base plan `monthly` as **Active** and the subscription `pro_monthly` as **Active**.

### 4B. The three credit packs (one-time products)

Go to **Monetize with Play** > **Products** > **One-time products** > **Create one-time product**. Create these three, exactly.

| Product ID | Name | Description | Price (India) |
|---|---|---|---|
| `credits_10_50` | `50 MockMob credits` | `50 credits to use anywhere in MockMob.` | `₹15` |
| `credits_29_150` | `150 MockMob credits` | `150 credits to use anywhere in MockMob.` | `₹45` |
| `credits_49_300` | `300 MockMob credits` | `300 credits to use anywhere in MockMob.` | `₹75` |

For each one:
- [ ] **4B.1** Fill in the Product ID, name and description from the table, then click to add a **purchase option**:
  ```
  Purchase option ID:  buy
  Type:                Buy
  ```
- [ ] **4B.2** Under **Advanced options**, leave **Quantities and limits** (multi-quantity) **off**. The server refuses a purchase of more than one at a time.
- [ ] **4B.3** Under **Pricing**, set **India** to the price in the table, in INR. Let Play fill in the other countries by itself.
- [ ] **4B.4** Click **Save**, then **Activate**. **You should see** the product listed as **Active**.

Keep one purchase option per pack. The first "Buy" option is the one our billing library uses.

**Send us:** "Pro subscription and 3 packs active".

---

## Part 5. Switch the server on (US with your OK, then YOU)

- [x] **5.1 Done:** the `play_purchases` table is already on the production database (added 18 Oct, checked 19 Oct).
- [ ] **5.1b US, with your OK:** one more database step for the subscription (migration `20261019210000_play_subscriptions`: a few new columns on `play_purchases` and the function that keeps Pro in step with Google). We ask you first, apply it and check it. It changes nothing for anyone until a subscription is bought.
- [ ] **5.2 YOU:** In Vercel, add:
  ```
  Key:           PLAY_BILLING_ENABLED
  Value:         true
  Environments:  Production only
  ```
  Then redeploy production so the new values load: **Deployments** > the latest production deployment > **⋯** > **Redeploy**. Or tell us "redeploy" and we will do it. Setting a variable alone does nothing until the redeploy.
- [ ] **5.3 YOU: the test message.** In Play Console > **Monetize with Play** > **Monetization setup** > **Real-time developer notifications**, click **Send test message**. You should see a success note. Tell us the time, and we check that the server log says `test notification received`.

---

## Part 6. Buy (YOU on the phone, US watching)

- [ ] **6.1 Install from Play.** On the phone, make sure the Play Store is signed in with the test Gmail (Play Store > your profile picture). Open the opt-in link from **Internal testing** > **Testers** > **Copy link**, tap **Become a tester**, then **Download it on Google Play**, and install MockMob.
  - First **uninstall the MockMob you have now**. It was signed with a different key, so Play cannot update it. Your progress is on the server, so you only sign in again.
- [ ] **6.2 Sign in with a MockMob account that is not Pro.** The Get Pro button stays hidden for an account that already has Pro. A fresh account is best. Your own account is fine only if it is Free.
- [ ] **6.3 Subscribe to Pro.** Open **Get Pro**. It shows **₹149.00 a month** and "Renews every month. Cancel anytime in Google Play." Tap **Get Pro**. Google's sheet shows a "test purchase" notice. Choose **Test instrument, always approves** (some phones call it **Test card, always approves**) and confirm. **You should see** Pro switch on at once, and the Pro-only modes unlock. Open Get Pro again: it says when Pro renews and shows **Manage subscription**.
- [ ] **6.3b Watch it renew.** For a licence tester a "month" lasts about **5 minutes**, and a test subscription renews up to 6 times, then ends by itself. Leave the app for 10 minutes, then open Get Pro again: the renewal date has moved on. Tell us the time, and we check that the server heard each renewal.
- [ ] **6.3c Cancel it.** In Get Pro, tap **Manage subscription**. Google Play opens on MockMob Pro. Tap **Cancel subscription**. Back in MockMob, Get Pro says "Renewal is off, so nothing more will be charged. Pro stays on until ..." About 5 minutes later Pro switches off by itself. Then subscribe again (6.3) for the refund test.
- [ ] **6.4 Buy the 50-credit pack.** Open the credits page, buy **50 credits** the same way, and watch the balance go up by 50.
- [ ] **6.5 Tell us.** We check (read-only) that each subscription and the pack landed in `play_purchases`, that Pro's end date follows Google's renewal date, and that the 50 credits are there. In Play Console, **Order management** shows the orders marked as test orders.
- [ ] **6.6 The refund test.** In Play Console > **Order management**, search for the test Gmail, open the newest **MockMob Pro** order and choose **Refund**, with **Revoke** (or "remove entitlement") ticked. Within a few minutes Pro should switch off in the app, and you can subscribe again.

**Done when** you have subscribed to Pro and bought a pack, seen Pro and the balance change, seen Pro renew, cancelled it and seen it end on its date, and seen a refund take Pro away at once.

**Plan B if the Play link is slow.** Licence testers can test billing in a build installed straight from a file, as long as the app exists in Play Console. We can send you an APK of the same build 10. Uninstall the current app first, as in 6.1.

---

## Later, before real students pay (not needed for the test)

- **15% service fee.** In India the fee is 30%, or 15% on your first USD 1 million a year once you enrol. Enrol on the **Associated developer accounts** page: create your account group, click **Review and enroll**, accept the terms. If you already enrolled for your other app, the enrolment covers this app too. It counts only from the day you enrol, so do it before the public launch. (Google's 2026 fee changes so far cover the US, UK, EEA, Australia and Japan, not India.)
- **Tax.** Test purchases have no tax. Before real sales, ask your CA how GST works for Play sales by an Indian developer.
- **App links and one-tap Google sign-in.** These use the fingerprints from 3.3. We set `ANDROID_CERT_SHA256` in Vercel to all the app signing SHA-256 values, separated by commas (plus the upload key's SHA-256 for builds installed from a file). In Google Cloud (the project with the website's Web sign-in client), you add one **Android** OAuth client per SHA-1, all for package `in.mockmob.app`. Today's build has one-tap switched off (`GOOGLE_WEB_CLIENT_ID` is empty) and signs in through the browser, so billing does not need this.
- **Stronger notification check (optional).** Turn on **Enable authentication** on the push subscription with a service account and set **Audience** to `https://www.mockmob.in/api/billing/play/rtdn`. The Pub/Sub service agent `service-<project-number>@gcp-sa-pubsub.iam.gserviceaccount.com` needs the **Service Account Token Creator** role on that service account. Then set `PLAY_RTDN_OIDC_AUDIENCE` to the same audience in Vercel. Always set the audience yourself: our server compares it exactly.

---

## If something goes wrong

| What you see | What it usually means | What to do |
|---|---|---|
| "This version of the application is not configured for billing through Google Play" | The installed build is not one Play knows, and the phone's Play account is not a licence tester | Install from the internal testing link (6.1), or add the Play Store account to **License testing** (1.3). Make sure the Play Store on the phone uses the test Gmail. Then clear the Play Store cache (Settings > Apps > Google Play Store > Storage > Clear cache) and try again. |
| "The item you requested is not available for purchase" | The product is not **Active**, the ID differs, or the account has not opted in to internal testing | Check that the product is Active and its ID matches Part 4 exactly. Open the opt-in link again and tap **Become a tester**. A product made in the last hour may need a little longer. |
| No prices show in the app, or the Buy buttons are missing | Same causes as above, or the account is already Pro | As above, and use a Free account (6.2). |
| No test payment methods, only real cards | The Play Store account on the phone is not a licence tester | Add it in **Settings** > **License testing**, switch the Play Store to that account, clear the Play Store cache, and reopen MockMob. |
| You paid, the app says "Purchases are not available right now", and a few minutes later you get a refund email | The server could not check the purchase. Usually the service account is not switched on yet (Google can take up to 24 hours), or a Vercel value is missing. Google refunds an unconfirmed test purchase after 3 minutes, so nothing is lost | Wait a few hours and try again. Check 2.2, 2.5, 2.6 and 5.2. Saving a small edit to a product's description sometimes speeds up the activation. We read the Vercel log for the `[play]` line and tell you which one it is. |
| Service account key creation blocked | The project is inside an organisation with key creation switched off | Use a project with **No organization** (2.1). |
| Adding `google-play-developer-notifications@...` fails ("domain restricted sharing") | The same organisation rule | Use the **No organization** project. |
| **Send test message** fails in Play Console | Wrong topic name, or the Publisher role is missing | Check 2.8 and 2.9. The topic name must be the full `projects/.../topics/play-rtdn`. |
| Test message succeeds but our log shows nothing | The flag is off (the endpoint answers 404), the token in the URL differs from Vercel, or payload unwrapping is on | Check 5.2 and the redeploy, compare the token (re-copy it into both places), and turn payload unwrapping off. |
| "You're already subscribed" or "You already own this item" on Pro | That Play account already has the Pro subscription, perhaps for another MockMob account | Sign in to the MockMob account that subscribed. Or cancel it in Google Play and wait for it to end (about 5 minutes for a tester), or refund and revoke it as in 6.6. |
| Get Pro says Google Play could not take your payment, so Pro is paused | A test card declined a renewal (account hold) | Tap **Manage subscription** and switch to **Test instrument, always approves**. Pro comes back within a few minutes. |
| Upload rejected: "signed with the wrong key" | The build was signed with a different upload key than the app's first release | Tell us. We sign with the key you used before. |

---

## Sources (all accessed 19 Oct 2026)

- Test Google Play Billing Library integration (licence testers, sideloaded builds, test instruments, 3-minute refund of unacknowledged tester purchases), last updated 16 Oct 2026: https://developer.android.com/google/play/billing/test
- Integrate Google Play Billing: getting ready (a build with the billing library must be published to a track before products can be configured; RTDN setup, notification content options, Publisher role, "View financial data"), last updated 9 Sep 2026: https://developer.android.com/google/play/billing/getting-ready
- Create a one-time product (Monetize with Play > Products > One-time products, purchase options, Buy, quantities and limits, pricing, Activate), Play Console Help: https://support.google.com/googleplay/android-developer/answer/16430488
- Create and manage subscriptions (Monetize with Play > Products > Subscriptions, Create subscription, product ID up to 40 characters, name up to 55, up to 4 benefits of 40 characters with no prices or trials, Add base plan, base plan ID, Auto-renewing, billing period, grace period, account hold (default 60 days minus the grace period), resubscribe, Manage country/region availability, price, Activate), Play Console Help, accessed 19 Oct 2026: https://support.google.com/googleplay/android-developer/answer/140504
- Test subscriptions (a monthly test subscription renews about every 5 minutes, up to 6 times; grace 5 minutes, account hold 10 minutes), accessed 19 Oct 2026: https://developer.android.com/google/play/billing/test
- Subscription lifecycle (grace keeps access, account hold blocks it, a cancel keeps access to the paid date, a revoke ends it at once), accessed 19 Oct 2026: https://developer.android.com/google/play/billing/lifecycle/subscriptions
- Create an in-app product (product ID rules: starts with a lowercase letter or number, then lowercase letters, numbers, underscores and periods; IDs cannot be changed or reused), Play Console Help: https://support.google.com/googleplay/android-developer/answer/1153481
- Multiple purchase options and offers for one-time products (the first Buy option is the backwards-compatible one), last updated 9 Sep 2026: https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers
- Set up an open, closed or internal test (Testing > Internal testing, email lists, up to 100 testers, available within minutes, a first test link can take several hours): https://support.google.com/googleplay/android-developer/answer/9845334
- Set up licence testing (Settings > License testing, email lists): https://support.google.com/googleplay/android-developer/answer/6062777
- Use Play App Signing (Protected with Play > Play Store distribution > Go to Play app signing; quantum-ready hybrid signing with three keys; upload key reset): https://support.google.com/googleplay/android-developer/answer/9842756
- Getting started with the Google Play Developer API (enable the API, service account, invite in Users and permissions with "View financial data, orders, and cancellation survey responses" and "Manage orders and subscriptions"; no Cloud project linking needed any more), last updated 18 Dec 2025: https://developers.google.com/android-publisher/getting_started
- Add developer account users and manage permissions (app-level "View financial data", "Manage orders and subscriptions"): https://support.google.com/googleplay/android-developer/answer/9844686
- Service account activation can take up to 24 hours (vendor documentation, not Google's): https://docs.apphud.com/docs/google-play-service-credentials
- Secure-by-default organisations (key creation and domain-restricted sharing enforced for organisations created on or after 3 May 2024): https://cloud.google.com/resource-manager/docs/secure-by-default-organizations
- Create push subscriptions (Delivery type Push, endpoint, authentication, payload unwrapping), last updated 13 Oct 2026: https://docs.cloud.google.com/pubsub/docs/create-push-subscription
- Authenticate push subscriptions (Token Creator role for the Pub/Sub service agent, token claims), last updated 13 Oct 2026: https://docs.cloud.google.com/pubsub/docs/authenticate-push-subscriptions
- Real-time developer notifications reference (testNotification, voidedPurchaseNotification, productType 2 = one-time), last updated 15 Oct 2026: https://developer.android.com/google/play/billing/rtdn-reference
- Payments profile (Settings > Payments profile, Create payments profile): https://support.google.com/googleplay/android-developer/answer/7161426
- Service fees (15% tier for other markets; 2026 changes for the US, UK, EEA, Australia and Japan): https://support.google.com/googleplay/android-developer/answer/112622
- Enrolling in the 15% tier (Associated developer accounts, account group, Review and enroll): https://support.google.com/googleplay/android-developer/answer/10632485
- Refunds (Order management, Refund): https://support.google.com/googleplay/android-developer/answer/2741495
- purchases.products resource (purchaseState, purchaseType 0 = test, obfuscatedExternalAccountId), Google Play Developer API reference via Context7: https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products
- Play Billing Library 8 required for new apps and updates from 31 Aug 2026 (our plugin, in_app_purchase_android 0.5.4, uses billing 8.0.0): https://revenuecat.com/blog/engineering/play-billing-8-migration/

From our code (wt-rel11 at 4af47969, wt-v15-3 at 4472b373): `src/lib/payments/playGoogle.js` (scope `https://www.googleapis.com/auth/androidpublisher`, the key needs `client_email` and `private_key`, raw JSON or base64), `playRtdn.js` (the `?token=` check, optional OIDC audience compared exactly), `playBilling.js` (reads `message.data`, so payload unwrapping must stay off; quantity must be 1), `flutter_app/lib/features/billing/data/play_products.dart` (pro_monthly on base plan monthly, and the three pack IDs).
