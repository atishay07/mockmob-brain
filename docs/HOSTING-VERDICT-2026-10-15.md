# Hosting verdict

15 Oct 2026. Read-only research; nothing was changed. It builds on `USAGE-LIMITS-DIAGNOSIS-2026-10-15.md`. All prices are list prices in USD, checked today.

## Supabase: yes, stay on Free until public launch, under four conditions

**This month is not fully in your control.** Usage already counted stays counted until the billing month resets. The reset date is under Billing, then "Upcoming invoice".
- **What can happen.** When the grace period ends, Supabase can restrict both production and staging: 402 errors, a read-only database, or paused projects. The grace period's end date is in the dashboard notice.
- **If the grace period ends before the reset,** the only instant fix is Pro ($25). You can downgrade after the reset, and the unused time comes back as credit.

**From the next billing month, Free holds if all four of these are true:**
1. Fixes 1-4 are live, and local and agent testing use staging, not production.
2. Fix 5 ships before you add testers. Before it, about 8 students doing two Commerce sessions a day pass 5 GB. After it, the ceiling is about 50-60 daily students. Expect about 1.5-3 GB a month at testing scale.
3. You check Usage weekly. A second overage is restricted immediately, with no new grace period.
4. You accept that Free has no automatic backups. Take a weekly dump yourself.

Move to Pro at public launch: 1,000 daily students is about 60 GB of egress a month.

## Vercel: Hobby is fine on limits, not on terms

- **Limits.** After the fixes, testing traffic sits far below Hobby's limits. Hobby runs out at about 200-300 daily students.
- **Terms.** Hobby is "non-commercial personal use only", and "any method of requesting or processing payment" counts as commercial.
  - If students can reach the Razorpay checkout today, upgrade now. If not, upgrade the day it goes live.
  - On Hobby, going over a limit blocks the feature for up to 30 days. Pro bills the extra usage instead.
- **Pro is not unlimited.** It costs $20 a month, which includes $20 of usage; after that, usage is billed. At 10,000 daily students, expect about $150-250 a month. Set a spend alert, and only switch on auto-pause at a ceiling where you would rather go offline than pay.
- **Fluid compute does not lower ping.** It cuts cold starts and bills CPU only while code runs. Latency depends on the region.

## Region

- **Functions: `sin1` (Singapore), next to the database.** Mumbai (`bom1`) is a Vercel compute region. But from there each database call crosses to Singapore and back, about 60 ms, and 10 calls add about 0.6 s. Vercel has no Middle East compute region, which doesn't matter for students in India.
- **Database: stay in Singapore.** Supabase offers Mumbai, but moving it means a new project, a data migration, new keys and a new app build. It would save one round trip of about 40-60 ms per request. That isn't worth the cost.

## Vercel or Cloudflare: stay on Vercel

**Latency is about the same.** The database is in Singapore, so both platforms run our server code in Singapore; Cloudflare does it with a placement hint. Cloudflare's 22 Indian cities only speed up static files.

**Cloudflare is cheaper at scale,** about $40 against about $200 a month at 10,000 daily students. But moving takes **5-8 working days plus a tail of bugs.**

Risks of moving:
- **The tools are in flux.** Cloudflare now recommends its own adapter, vinext, which is still in beta, over OpenNext.
- **Our sign-in proxy may not run there.** OpenNext lists Node middleware as not yet supported, and that is what Next 16's `proxy.js` is.
- **Files read from disk.** About 10 server files read JSON from disk.
- **Memory.** About 24 MB of JSON loads into most routes, against a limit of 128 MB per Worker instance.

Revisit Cloudflare if the Vercel bill stays above $150 a month for two months.

A VPS is the cheapest option at scale, but uptime, deploys, TLS, crons and security patches become your job. Netlify, Render, Railway, Fly.io and Amplify offer nothing better for this setup.

## Monthly cost

| Daily students | Vercel Pro | Cloudflare Workers Paid | VPS (DigitalOcean Singapore) | Supabase (any host) |
|---|---|---|---|---|
| Testing, under 50 | $20 (usage inside the credit) | $5 | about $12 | $0 on Free, if the conditions hold |
| Launch, 1,000 | about $25-35 | about $5-8 | about $24 | $25 on Pro |
| 10,000 | about $150-250 | about $35-45 | about $50-70 (2 servers + load balancer) | about $60-110 (Pro, a bigger server, about 350 GB of extra egress) |
| One-time move | none | 5-8 days, plus risk | 2-3 days, plus ongoing operations | none |

The table assumes this per daily student:
- About 110 function calls a day: 10 pages, 40 API calls, and 60 saves during tests after fix A8.
- About 35 ms of CPU per call.
- About 150 CDN requests.
- About 0.4 MB of data sent from our functions.
- Two Commerce practice sessions.
- About 2 MB of Supabase egress after fix 5 (about 14 MB before it), counted before compression.
- Prices use Vercel's Singapore and Mumbai rates.

## Sources

- Supabase: [Billing FAQ (grace period, restrictions, reset)](https://supabase.com/docs/guides/platform/billing-faq), [Egress quotas](https://supabase.com/docs/guides/platform/manage-your-usage/egress), [Pricing](https://supabase.com/pricing), [Billing cycle](https://supabase.com/docs/guides/platform/your-monthly-invoice), [Downgrade credits](https://supabase.com/docs/guides/platform/manage-your-subscription), [Regions](https://supabase.com/docs/guides/platform/regions)
- Vercel: [Hobby plan](https://vercel.com/docs/plans/hobby), [Commercial use](https://vercel.com/docs/limits/fair-use-guidelines#commercial-usage), [Pro plan](https://vercel.com/docs/plans/pro-plan), [Fluid compute pricing](https://vercel.com/docs/functions/usage-and-pricing), [Fluid compute](https://vercel.com/docs/fluid-compute), [Regions](https://vercel.com/docs/regions), [Function regions](https://vercel.com/docs/functions/configuring-functions/region), [sin1 pricing](https://vercel.com/docs/pricing/regional-pricing/sin1), [bom1 pricing](https://vercel.com/docs/pricing/regional-pricing/bom1), [Flat Rate CDN](https://vercel.com/docs/pricing/flat-rate-cdn), [Spend management](https://vercel.com/docs/spend-management), [Crons](https://vercel.com/docs/cron-jobs/usage-and-pricing)
- Cloudflare: [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/), [Workers limits](https://developers.cloudflare.com/workers/platform/limits/), [Next.js guide (vinext)](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/), [OpenNext support matrix](https://opennext.js.org/cloudflare), [Placement](https://developers.cloudflare.com/workers/configuration/placement/), [Network](https://www.cloudflare.com/network/)
- Latency from Mumbai to Singapore, about 60 ms (secondary source, 2021): [Stream](https://getstream.io/blog/low-latency-chat-messaging-asia-pacific/)
