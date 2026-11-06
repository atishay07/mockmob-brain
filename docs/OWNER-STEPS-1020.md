# Your morning steps for version 13

Written for you on 20 Oct 2026, while you were asleep. Plain steps, one screen at a time. Nothing here needs code. Every Play Console menu name below was checked against Google's current help pages; where Google's own page does not confirm a name, the step says so ("may differ").

**What is already done (you do not need to touch it):** the website with the Mob, the Pro page, the Wallet and the new Ask Mobi is live. Pro on Google Play works (you proved it with the licence tester).

**What is left, and why only you can do it:** these are your Play Console, Vercel and money decisions. Nothing here can be done by an agent.

## The order to follow (about 30 minutes in all)

1. Step 1: get version 13 ready in the Alpha track, but only press **Save**. Do not send it for review yet.
2. Step 2: content rating.
3. Step 3: Data safety. Then press **Send changes for review** (the last part of Step 3). One review then covers version 13, the rating and the Data safety form together.
4. Step 4: Vercel, so the email sign-in link opens the app.
5. Steps 5 and 6: two decisions. Tell the main session your answers in chat.

**Before Step 1:** open the folder `Desktop\MockMob-build-13`. You need a file ending in `.aab` with `+13` in its name (for example `mockmob-1.0.16+13-sells.aab`). If the folder or the file is missing, the build has not finished: stop, and read `docs\brain\NOW.md` (top of the file) to see where it stands. Do not upload the `.apk`; Play wants the `.aab`.

---

## Step 1. Upload version 13 to closed testing (Alpha), replacing version 11

Version 11 is in review. Google does not allow a second release on the same track while one is in review, so version 11 has to be pulled out of review first. Version 13 replaces it anyway.

**Screen 1: pull version 11 out of review**

1. Open Play Console and choose the MockMob app.
2. In the left menu open **Publishing overview** (it sits near the bottom of the left menu; the **Dashboard** also links to it).
3. Under **Changes in review**, press **Remove changes** (Google words this as removing the changes from review). Confirm.
4. What to expect: the changes go back to "Changes not yet sent for review". Your store listing text and graphics should still be there. If the listing looks empty later, re-upload from `Desktop\MockMob-store-listing\UPLOAD-THIS`.

**Screen 2: discard the old release**

1. Left menu: **Test and release**, then **Testing**, then **Closed testing**.
2. On the **Alpha** row press **Manage track**, then open the **Releases** tab.
3. Open the version 11 release summary and press **Discard release**. Confirm.

**Screen 3: create the version 13 release**

1. Still on Alpha, press **Create new release** (top right). If the button is greyed out, open the **Dashboard** and finish the tasks it lists first.
2. Under **App bundles** drag in the `.aab` from `Desktop\MockMob-build-13`. Wait until it shows as uploaded and Play has read it. Play checks the version number: 13 is higher than 11, so it passes.
3. **Release name:** leave the pre-filled name, or type `13 (1.0.16) closed test`. Only you see it.
4. **Release notes:** paste this (it is about 400 characters; Google's limit is 500 per language). Check it against `NOW.md` before you paste, and delete any line for something that did not make it into the build.

```
<en-US>
Version 13. The Mob is now a daily place: join with a code, play the weekly quest with your friends and finish on the podium. Pro has its own page and the Wallet shows your credits clearly. Ask Mobi can fix a mistake for good and tell you where you stand against your colleges. The finish screen after a paper reads like a debrief. Many bug fixes. If anything feels wrong, write to support@mockmob.in.
</en-US>
```

5. Press **Next**. If an **Errors summary** appears, press **Show more** and read it. Errors block you; warnings do not. If an error is unclear, copy its text into chat.
6. Press **Save** (not **Publish**, and do not send for review yet). The release now waits under "Changes ready to send for review" on the Publishing overview page.

---

## Step 2. Content rating: "users can interact" Yes, "purchase digital goods" Yes

The Mob lets members interact (preset stickers, Mob names, running games together), and the app now sells Pro and credits through Google Play. The old answers said No to both, so they are out of date.

1. Left menu: **Policy and programs**, then **App content**. (Google's page says "Policy, App content"; the group name may differ slightly.)
2. Find **Content rating** (it also appears under "Target audience and content" with the date it was submitted). Open it.
3. If you see **Edit** or **Manage**, use it. Otherwise press **Start new questionnaire**. Google's page says this button lets you redo the answers. A new questionnaire asks everything again, so use the table below.
4. Email address: `support@mockmob.in`. Category: **Reference, News or Educational**. (The IARC wording changes from time to time; pick the educational option.)
5. Answer like this. The two changes from last time are in bold.

| Question (wording may differ slightly) | Answer |
|---|---|
| Violence, blood, fear | None |
| Sexual content or nudity | None |
| Bad language | None |
| Drugs, alcohol, tobacco | None |
| Gambling or simulated gambling, contests with prizes | No |
| **Can users interact or exchange content with each other?** | **Yes.** The Mob: preset stickers and first names only, no free text, no photos. If the form asks whether users can send messages or share their own content: stickers only, no free text. Be honest about this and let the form decide the rating. |
| Shares the user's location with others | No |
| Collects or shares personal information | Yes (email, name, study record). Not shared beyond service providers. |
| **Can users purchase digital goods or make in-app purchases?** | **Yes.** Pro subscription and credit packs through Google Play. If it asks about random or loot-style items: No, nothing is random. |
| Unrestricted internet access or a web browser | No |
| Generative AI features | Yes: Ask Mobi writes study replies; users can report a reply. |
| Ads | No |

6. Press **Save**, then **Next**, then **Submit**. You will see a summary of ratings. Accept whatever it shows. Do not change an honest answer to get a lower age rating. It may now show labels such as "Users Interact" and "In-App Purchases". That is expected and fine.

If the screen has different questions from the table, answer the question in the spirit of the row (the two bold rows are the point).

---

## Step 3. Data safety: add Financial info, Purchase history

Google Play now sends us purchase records (which product, when, renewal, refund). That counts as collected "purchase history".

1. Left menu: **Policy and programs**, then **App content**. Under **Data safety** press **Manage** (or **Start** if it only shows that).
2. On the first page ("Data collection and security") keep the answers as they are: collects data Yes, encrypted in transit Yes, deletion Yes (the web link `https://www.mockmob.in/account-deletion` stays). Press **Next**.
3. On the data types page open the **Financial info** group and tick **Purchase history** only. Do not tick "User payment info" (card details never reach us; Google handles them) and do not tick "Credit score" or "Other financial info".
4. Press **Next**. For Purchase history answer:
   - **Collected:** ticked. **Shared:** not ticked. Google's own page says sending data to a service provider that acts only for you is not "sharing"; Our database host (Supabase) and web host (Vercel) only process the records for us.
   - **Processed ephemerally:** No.
   - **Required or optional:** **Optional.** Google allows this only if every user can skip it. A student who never buys anything sends no purchase record, so that holds.
   - **Purposes:** **App functionality** and **Account management**. Nothing else.
5. Keep going through the remaining pages without changing the other answers. Press **Save**, then submit. Then open the **Preview** of the Data safety card and read it once against `https://www.mockmob.in/privacy`.

**One thing I found that is not yours to fix by clicking:** the privacy page at `/privacy` does not mention Google Play purchase records at all. Google compares the page with this form. I have not changed it (not my task, and a deploy is the main session's job). Tell the main session: "add one line to the privacy page about Play purchase history".

**Now send everything for review**

1. Left menu: **Publishing overview**.
2. Under **Changes ready to send for review** you should see: the version 13 Alpha release, the content rating, Data safety, and the store listing.
3. **Do not turn on "Managed publishing"** (it would delay going live by hand).
4. Press **Send changes for review** (top right), confirm.
5. Reviews often take a few days; Google gives no fixed time.

---

## Step 4. Make the email sign-in link open the app (Vercel)

Right now the app-link file on the website is empty (`[]`), so the sign-in link in the email opens a web page instead of the app. It needs one value from Google.

**Screen 1: copy the value from Play Console**

1. Play Console, MockMob app, left menu **Test and release**, then **App integrity**, then the **Play app signing** tab.
2. Google's own help page puts the same screen at "Protected with Play, Play Store distribution, Go to Play app signing". The menu names move around; look for a page titled **App signing** or **Play app signing**. This may differ on your screen.
3. In the box **App signing key certificate** find **SHA-256 certificate fingerprint** (a long line of 32 pairs of letters and numbers with colons). Press the copy icon.
4. Use the **App signing key** one. Do not use the **Upload key certificate** one for the main value.

**Screen 2: paste it into Vercel**

1. Open vercel.com, sign in, and open the MockMob project (project id starts `prj_uSolddr`).
2. **Settings**, then **Environment Variables**.
3. Press **Add New** (or **Add Environment Variable**).
   - **Key:** `ANDROID_CERT_SHA256`
   - **Value:** paste the fingerprint. Colons, upper or lower case and spaces are all fine. The server removes anything that is not a valid fingerprint, so a typo cannot publish a broken file; it just stays empty.
   - **Environments:** tick **Production** only.
   - Leave **Sensitive** off.
4. Press **Save**.
5. Optional, helps the APK you install by hand: the same value box can hold more than one fingerprint, separated by a comma. If you want the sideloaded APK (signed with your upload key) to open links too, add the **Upload key certificate** SHA-256 after a comma. Skip this if unsure.

**Screen 3: redeploy so it takes effect** (a new variable only applies to a new deployment)

1. In the same project open the **Deployments** tab.
2. On the top deployment marked **Production** press the three dots, then **Redeploy**, then confirm. Wait until it says **Ready**.

**Screen 4: check it worked**

1. Open `https://www.mockmob.in/.well-known/assetlinks.json` in a browser. It should show `in.mockmob.app` and your fingerprint. If it still shows `[]`, wait a few minutes and refresh; the file is cached for up to an hour.
2. Android checks the link file when the app is installed or updated. So do this step before the testers install version 13. A phone that installed version 13 before the file went live can fix it by updating or reinstalling the app. Until it is verified, the emailed link still works; it opens a web page.

---

## Step 5. Welcome credits: keep 150 or go down to 50

**What happens today:** a brand new account holds 150 credits. That is two things added together: 100 one-time welcome credits (from the very first version of the product) plus 50 free credits every month. Nobody ever decided on the 100 on top of the 50. It was left over when the two wallets were merged into one balance. Existing accounts are not affected by either choice.

**What it costs us:** the model cost of an AI job is about Rs 0.037 per credit on average (`AI-COST-PER-USER-2026-10-17.md`), with a measured worst case of Rs 0.042 for one model call. So 150 credits, all used, cost at most about Rs 6, or about Rs 13 if every credit were a two-call job. A credit sells for about Rs 0.16 to Rs 0.30 depending on the pack and where it is bought, so the margin stays wide either way.

**Your choices**

- **A. Keep 150** and say it plainly in the Wallet ("100 welcome credits and 50 free every month"). Nothing to build.
- **B. 50 only** (a new account starts with the monthly 50). This needs a small change and a production database change, so it waits for your yes to the main session.
- **C. A middle number**, such as 50 welcome and 50 monthly (100).

**My recommendation:** A for the closed test. The 14 to 15 testers get your best first impression, and 15 testers cost under Rs 100 in model fees in the worst case. Decide again before the public launch with real usage in front of you. The choice only affects new accounts, so it is easy to change later.

The file `docs\brain\DECISION-WELCOME-CREDITS.md` was meant to hold this decision. It did not exist when I wrote this guide, so everything you need is above. Reply in chat with "keep 150", "50 only" or a number.

---

## Step 6. Pro price in Play Console: Rs 149 or Rs 150

**What you have said, in order:**

- Rs 150 (ledger D75, D82, D121: "Pro Rs 150 final", prices confirmed).
- Then on 19 Oct (ledger D135 and D136, your words "₹149 a month"): Rs 149 on Play, Rs 99 on the website.
- Later you saw the Google sheet show "₹150 / 5 minutes" (the 5 minutes is only how fast licence-tester renewals run) and the main session's notes say the price in Console is 150.

So the Console and the notes may disagree, and the "149 or 150" question is open. **First look at what the Console really says**, then choose.

**Where to look and change it**

1. Play Console, left menu **Monetize with Play**, then **Products**, then **Subscriptions**.
2. Press the arrow next to **pro_monthly**.
3. Under **Base plans and offers** press the arrow next to the base plan **monthly**.
4. Find the price for India. To change it, press the pencil icon in the **Price** column, type the new price, **Save**. (For many countries at once, use **Update prices**.)
5. Google's page calls this the tax-exclusive price. Your own test sheet showed exactly the number you entered, so what a buyer sees should match. After you change it, look at the price on the Get Pro sheet in the app once to be sure.

**Things to know**

- The app and the website never hold this price. The app shows Google's own price string, so no new build and no deploy is needed.
- A price change applies to new buyers within a few hours. People already subscribed stay on their old price (Google calls them a legacy price cohort). Right now those are only licence testers.
- The website stays Rs 99 a month. The app never shows that price.

**My recommendation:** Rs 149. It is the number you gave last (D136), it is the one the app test notes expect, and 149 looks like a deliberate price where 150 looks rounded. The difference is one rupee, so if you set 150 on purpose and like it, keeping it is also fine. Tell the main session which one you want so the notes stop saying both.

---

## When you are finished

Tell the main session in chat: "Step 1 to 3 done, review sent", "Step 4 done" and your answers for Steps 5 and 6. It will then check the link file, update `NOW.md`, and do any code change your choice needs.

## Where this guide may be out of date

- **Menu names.** Google moves the Play Console menus. The paths came from Google's current help pages for releases, Data safety, content ratings and subscriptions. The App integrity path (Step 4) is the least certain: Google's own page uses a different name (see Step 4). If a name differs, look for the same words in the left menu or use the Play Console search box at the top.
- **The content rating questionnaire** is run by IARC. Google's help page does not list its questions, so the table is matched by topic, not by exact wording.
- **Review times** are not fixed by Google.
