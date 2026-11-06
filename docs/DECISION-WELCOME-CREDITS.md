# Decision: 150 or 50 credits for a new account

**For:** Atishay. **From:** the CTO session, 20 Oct 2026, written while you were asleep. **Your question (I8, 19 Oct 11:42 pm):** "How do I have 150 credits on this account? ... 150 credits instead of 50?" Numbers come from main 48985a8d.

## Recommendation: 50

Give a new account 50 credits, not 150. In practice, we stop the one-time grant of 100 and keep the 50 free credits every month. A new student still gets a complete first week for free, and every keen student reaches the Pro decision on about day 3 rather than day 7. That is just after their first free full mocks and debriefs, when they want more most. The 100 extra credits cost us almost nothing in AI. What they actually cost is pack revenue from Pro students, who are the ones who buy packs (your D157). They also make throwaway accounts about a third more useful. The change is one database default and three lines of copy, and we can undo it in a minute if the closed test shows students leaving at the wall.

## Why a new account shows 150 today

- **50:** this month's free credits. They come back on the 1st of every month (IST) and are spent first. You set this on 18 Oct.
- **100:** a one-time signup grant. It is the old column default (`users.credit_balance DEFAULT 100`, from migration 0011). These credits never expire and are spent last. The pricing page promises it ("New accounts start with 100 credits."), and the Wallet calls it "welcome credits".
- Under one credits balance (D78), the two add up to 150. Two parts with two different rules is exactly what confused you, and it would confuse a 17-year-old too.

## What credits buy, and what is free anyway

1 credit buys 1 practice question or 1 Mobi job. A full mock costs 50 credits. On Free, these cost nothing: today's 10-question set (every day), the first full mock in each subject (250 questions across 5 subjects), the weekly Mob paper, the debrief, Where you stand, Revise and Learn. Pro (Rs 99 a month on the web, Rs 150 on Play) makes all practice free and includes 50 credits a month for Mobi. Packs cost Rs 10 for 50, Rs 29 for 150 and Rs 49 for 300 on the web, which is Rs 0.16 to Rs 0.20 a credit. On Play they cost Rs 15, 45 and 75, which is Rs 0.25 to Rs 0.30 a credit.

## A fresh Free student's first week

| Student | Paid use per day | Out of credits with 50 | Out of credits with 150 |
|---|---|---|---|
| Light: 4 days active, free set only, 3 Mobi jobs in the week | about 0.5 | never | never |
| Steady: the free set, 5 extra questions and 2 Mobi jobs | 7 | day 8 | day 22 |
| Keen (the likely Pro buyer): the free set, 20 extra questions and 3 Mobi jobs | 23 | day 3 | day 7 |

- Running out is never a dead end on either option, because today's free set, the free full mocks still left and the Mob paper stay open.
- The light student never notices the difference.
- The steady student gets a refill on the 1st, so with 150 they usually never meet the wall in their first month.
- The keen student's practice adds up to about 690 credits a month. In packs that costs Rs 113 on the web or Rs 172 on Play, so Pro at Rs 99 or Rs 150 is clearly the better deal. With 50, the wall sends them to Pro in their first week. With 150, it arrives after the week is over.

## Cost to us

- **Practice has no model cost.** Questions come from the bank.
- **A Mobi job costs us very little.** Fix it for good costs about Rs 0.027 (at most Rs 0.042). A doubt thread costs about Rs 0.05 (at most Rs 0.08).
- **The extra 100 credits, per new account.** Realistically about Rs 0.7 to Rs 1.25, if a quarter of them go to Mobi. The ceiling is Rs 5, if every one of them becomes a doubt thread.
- **Per 1,000 new accounts.** About Rs 700 to Rs 1,250 (USD 8 to 15). The ceiling is Rs 5,000 (USD 59).
- **The monthly worst case per account does not change.** It is set by the free per-student AI cap of Rs 2.50 a month (USD 0.0284), not by the welcome grant. The grant only stretches it over more months.
- **Against the old USD 25 monthly cap.** About 880 free students would each have to hit their own cap to use up USD 25 in a month, on either option. You removed that global ceiling on 17 Oct, and AGENTS.md on main says so. The per-student caps are still in place.
- **The real cost is pack revenue.** 100 credits are worth Rs 16 to Rs 20 on the web and Rs 25 to Rs 30 on Play. A student who goes Pro spends those credits on Mobi after the 50 Pro includes, and only then needs a pack. A Pro student who needs 30 extra jobs a month would buy nothing for about 3 months.

## Abuse with throwaway accounts

- **Making accounts is free.** Gmail plus-addresses give unlimited new accounts, and the code has no disposable-email check.
- **Free questions per throwaway on its first day.** About 310 with 50 (250 in free full mocks, 10 in today's set, 50 from credits). About 410 with 150, which is 32% more. So with 50, scraping the bank takes about a quarter more accounts.
- **AI per throwaway.** At most Rs 1.83 to Rs 2.50 in the first month with 50. With 150 it is capped at Rs 2.50. The difference is under Rs 0.70 a month.
- **The bigger leak is the free first full mock in each subject.** It stays on either option. A per-device or per-IP signup limit is the real fix, and it is a separate follow-up.

## If you say 50 (what changes; nothing has been changed yet)

1. **Production migration (needs your yes).** `alter table public.users alter column credit_balance set default 0;` The 1,541 existing students keep their 111,961 credits.
2. **Copy.** The pricing page (`src/app/pricing/page.js`) line becomes "Every account gets 50 free credits a month, used first." The Wallet's kept note (`src/components/wallet/walletModel.mjs`) becomes "Credits you buy or earn. They do not expire." The app's copy gets the same check.
3. **Tests.** `community_1018.test.mjs` line 118 and `money_v13_1020.test.mjs` line 63.
4. **The Wallet's kept row.** It must read well at 0 for a new student.
5. **Timing.** Testers who sign up before the change keep their 100 credits. That is harmless.

**How we will know if 50 is wrong.** In the closed test, watch the share of new accounts that reach 0 credits in their first week, and whether they come back the next day. If more than 1 in 3 keen students stop after the wall, bring back a welcome grant. That is the same one-line change, reversed.
