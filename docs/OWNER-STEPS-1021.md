# Your steps for version 16 (closed testing)

Written 21 Oct 2026, night. One screen at a time. Nothing here needs code. Same flow as version 15, with version 16 replacing it.

**Already done for you:** the website is live with everything version 16 needs: monthly Pro at ₹99 (your Razorpay plan), live Mob rooms (your Realtime switch), the referral copy, the pricing page, the phone hero.

**Use this file:** `mockmob-1.0.18+16-sells.aab` in this folder. Do not upload the `.apk`; it is for installing on a phone directly (it is the arm64 build for a real phone).

## Step 1. Take version 15 out of review (only if it is still in review)

1. Play Console, choose MockMob, open **Publishing overview** in the left menu.
2. Under **Changes in review**, press **Remove changes**. Confirm.
3. If version 15 was never sent, or is already approved, skip this step.

## Step 2. Replace the Alpha release with version 16

1. Left menu: **Test and release**, then **Testing**, then **Closed testing**. On the **Alpha** row press **Manage track**.
2. If a version 15 release is still a draft, open it and press **Discard release**.
3. Press **Create new release**.
4. Under **App bundles**, upload `mockmob-1.0.18+16-sells.aab`. Play checks the version code (16); it is higher than 15, so it passes.
5. **Release name:** leave the pre-filled one, or type `16 (1.0.18) closed test`.
6. **Release notes** (under 500 characters):

```
<en-US>
Version 16. Your first minute: a welcome with your 50 credits and a way to bring a friend (you both get 100). The Mob greets you with its room and shows you how it works. Live rooms are on: play together, now. Quiet notes from Mobi point you to what matters today. Invites, credits and account details are clearer, and the words throughout are kinder.
</en-US>
```

7. Press **Next**. Errors block you; warnings do not. If an error is unclear, paste its text in chat.
8. Press **Save**, then go to **Publishing overview** and press **Send changes for review**.

## Step 3. Nothing else

Content rating, Data safety and the app-signing key are unchanged from version 13. Testers install from Play as before; the `.apk` is only for your own phone.

## What to look at first on your phone

1. A fresh account: the welcome with the 50 credits, then "Invite a friend".
2. The Mob tab: the room with the three Folds, then "See how it works".
3. Start a game: "Live · together now" is there.
4. Credits: the invite card with the 100, and "Have a friend's code?".
5. Today over the next days: Mobi's note appears at most once a run, and the X keeps it quiet for a week.
