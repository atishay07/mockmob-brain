# Higgsfield API research, 16 Oct 2026

Read-only research for the USD 15 budget in HIGGSFIELD-PLAN-2026-10-16.md. Nothing was signed in, nothing was paid, no API was called. Every claim cites a source ID (section 8) fetched on 16 Oct 2026. "Inferred" means arithmetic or reasoning from verified numbers, not a statement by Higgsfield. The plan file was not edited.

## 0. Findings that change the plan

1. **The owner's "from" prices are the 480p (or cheapest-config) rates, not the production rates.** Higgsfield prices per resolution. Wan 3.0 0.020/s is 480p; 720p is about 0.040/s and 1080p about 0.080/s (S4, S5; discount arithmetic inferred for non-Prime). Seedance 2.5 0.144/s is 480p; 720p is 0.3235/s and 1080p is 0.796/s (S6, token formula checked by hand). Seedance 2.5 at 1080p is 5.5x its "from" price.
2. **Plan step 5 is wrong for Seedance 2.5.** Three 5 s shots at 1080p cost about USD 11.94 on one try each, not 3.0-4.5. At 720p they cost about USD 4.85 (S6, inferred multiplication).
3. **Plan step 2 is wrong for Kling "1080p about 2x".** Kling 3.0 Standard i2v has no resolution field at all; it is a separate endpoint from Pro, 4K and Turbo (S7, S8). Standard is priced USD 0.042 to 0.063/s after 50% off; Pro 0.056 to 0.084/s (S9, S10). Turbo is 0.056/s at 720p and 0.07/s at 1080p (S11).
4. **The Kling discount is 50% on the model pages (S9, S10, S11), not 60% as in the owner's screenshot.** Prices match the screenshot (0.042) but the label differs. Expiry of the Kling and Seedance promos is not stated anywhere I could find.
5. **Resolution needed for U1 is tiny.** U1 ships at 512x512, so a 480p or 720p source is enough. The plan paid for 1080p on U1. That is the largest avoidable cost.
6. **Failed and moderated generations are not charged** (S1, S2, S3). Clips that render but that MockMob rejects are charged, so budget by "attempts per kept clip".
7. **There is no draft mode.** The cheap path is 480p on Wan 3.0 (USD 0.02/s) (inferred from S4, S5). Seedance 2.5 has a 4 s minimum, so its cheapest possible clip is about USD 0.58 (inferred).

## 1. Verified facts

### 1a. API mechanics, billing, limits

| Fact | Detail | Source |
|---|---|---|
| Base URL | https://api.higgsfield.ai | S12 |
| Auth | Header `Authorization: Key KEY_ID:KEY_SECRET`; keys created in the console; server-side only, never browser or app | S13 |
| Submit | `POST https://api.higgsfield.ai/{model path}` with JSON body; send an `Idempotency-Key` header on every submit | S12, S14 |
| Async flow | Submit returns `status: queued`, `request_id`, `status_url`, `cancel_url`. Poll `status_url`: queued, in_progress, then terminal completed, failed, nsfw or canceled. Poll from 2 s growing to 10 s with jitter; webhooks recommended for long jobs | S12, S14, S15 |
| Cancel | Only while still queued (202); after start it returns 400. A cancelled queued request is refunded | S12, S1 |
| Image input | Public HTTPS URL, or presigned upload: `POST /files/generate-upload-url` (JPEG, PNG, WebP, GIF; upload URL valid 1 h) then PUT, then pass `public_url` | S16 |
| Model paths | Wan 3.0 `/alibaba/wan-3.0/image-to-video`; Wan 3.0 Prime `/alibaba/wan-3.0-prime/image-to-video`; Kling 3.0 `/kling-video/v3.0/{std,pro,4k}/image-to-video` and `/kling-video/v3.0-turbo/image-to-video`; Seedance 2.5 `/bytedance/seedance-2.5/image-to-video` | S7, S8, S17, S18 |
| Cost estimate | `POST /estimate/{model path}` with the same body returns credits and USD; "authoritative cost". Whether the estimate call itself is free is not stated | S1 |
| Charging | Only successful generations are charged. Failed and nsfw requests are not charged and reserved credit is refunded. Requests over a model timeout are marked failed and not charged | S1, S2, S3 |
| Refunds | Automatic for failed, nsfw and queued-cancelled. No other refund policy stated | S1, S3 |
| Top-up and balance | Pay as you go from a USD balance, minimum top-up USD 5, balance cannot go below zero, 403 when credits are insufficient; same rate regardless of top-up size | S19, S2 |
| Credit expiry | Funds expire one year after they are added | S1, S19 |
| Output retention | Output URLs kept at least 7 days; download to our own storage | S1, S12 |
| Rate limits | Concurrency only, per account and model; exceeding returns 400. Docs example shows a limit of 4; the help centre says a new key unlocks 20 concurrent. Check the console | S20, S19 |
| Free credits | No API free credits or trial found. "Free generations" and unlimited are website-plan features and do not apply to API use | S21, S22 |
| API vs app credits | The API balance is separate from website app credits (third-party statement) | S22 |

### 1b. Per-mode prices (Higgsfield model pages, rates shown after discount unless marked list)

| Model and endpoint | 480p | 720p | 1080p | Notes | Source |
|---|---|---|---|---|---|
| **Wan 3.0 i2v** | list 0.05, now ~0.02 (inferred) | list 0.10, now ~0.04 (inferred) | list 0.20, now ~0.08 (inferred) | Page states list rates per resolution and "before any applicable customer discount"; the comparison table shows 0.02-0.08/s, which equals list x 0.4. Owner screenshot: 60% off until 31 Oct, then 50% (then 0.025 / 0.05 / 0.10) | S4, S5 |
| **Wan 3.0 Prime i2v** | 0.0272 | 0.056 | 0.112 | Stated on page: "60% off until November 1". List = 0.068 / 0.14 / 0.28 (inferred) | S5 |
| **Kling 3.0 Standard i2v** | n/a | n/a | n/a | Page states "0.042/s for 1 s clips and 0.063/s for 3 or 15 s clips", 50% off (list 0.084 and 0.126). The 0.042 vs 0.063 split is unexplained; resolution is not stated | S9 |
| **Kling 3.0 Pro i2v** | n/a | n/a | n/a | 0.056 (1 s) and 0.084 (3 or 15 s), 50% off (list 0.112 and 0.168). Resolution not stated | S10 |
| **Kling 3.0 Turbo i2v** | n/a | 0.056 | 0.07 | 50% off; list 0.112 / 0.14. No sound, no last frame | S11 |
| **Kling 3.0 4K i2v** | n/a | n/a | n/a | 0.21/s | S10 |
| **Seedance 2.5 i2v** (16:9, no video input) | list 0.2056, now 0.144 (30%) | list 0.4622, now ~0.3235 (inferred) | list 1.1372, now ~0.796 | Price table range 0.144-0.7961 matches. Billing formula: ceil(height x width x seconds x 24 / 1024) video tokens at USD 0.0214 per 1,000 (480p, 720p) or 0.0234 per 1,000 (1080p). I checked 720p (21,600 tokens/s) and 1080p (48,600 tokens/s) by hand and they match | S6 |

The 30% Seedance discount is as stated in the owner's screenshot and on the pricing page (S23); the model page itself only shows list rates.

Inferred, not confirmed: ByteDance generally keeps pixel area roughly constant across aspect ratios, so 1:1 probably costs about the same per second as 16:9 at the same named resolution. Do not budget a 1:1 saving.

### 1c. Capabilities for the four models (image-to-video endpoints)

| | Wan 3.0 | Wan 3.0 Prime | Kling 3.0 Std / Pro / 4K | Kling 3.0 Turbo | Seedance 2.5 |
|---|---|---|---|---|---|
| First frame | `image_url` | `image_url` | `image_url` | `image_url` | `image_url` |
| **Last frame** | **Yes** `end_image_url` | **Yes** `end_image_url` | **Yes** `last_image_url` | **No** | **Yes** `end_image_url` |
| Duration | 2-30 s (default 5) | 2-30 s | 3-15 s (default 5) | 3-15 s | 4-30 s (default 5) |
| Resolution | 480p, 720p, 1080p (default 1080p) | same | not a field (Std/Pro/4K are separate endpoints) | 720p, 1080p | 480p, 720p, 1080p (default 720p) |
| Aspect ratio | explicit: 16:9, 4:3, **1:1**, 3:4, 9:16, adaptive (default adaptive) | same | not documented | not documented | not a field; "output framing follows `image_url`" |
| Seed | Yes, 0-2147483647 (0 is accepted but not forwarded, so use a nonzero seed) | same | Not documented | No | Not in schema (schema rejects unknown fields) |
| Negative prompt | Not documented on i2v | same | Not documented (only `cfg_scale` 0-1) | No | Not in schema |
| Audio | `generate_audio` default true | same | `sound` on/off, default on | none | `generate_audio` default true |
| Other | `enable_thinking` (prompt reasoning, default false) | same | `multi_shots`, `multi_prompt`, `elements`, prompt max 2,500 chars | none | `bitrate_mode` standard/high (price effect unknown) |
| Loop | none documented | none | none | none | none |

Sources: S17 (Wan 3.0), S18 (Prime, same schema), S7, S8, S24 (Kling), S25 (Seedance). Kling 2.5 Turbo (legacy, in the OpenAPI file) has `negative_prompt` and `cfg_scale` but only 5 or 10 s and no last frame in that schema (S26).

Practical consequence for 1:1: **Wan is the only one of the four with an explicit 1:1 switch.** For Kling and Seedance, supply a 1:1 still and verify the output ratio on the first test (the docs say output follows the input only for Seedance).

## 2. Evidence on quality (independent where possible)

Strength key: **A** independent, controlled, relevant; **B** crowd or arena data, general content; **C** vendor-run test; **D** marketing or spec sheet. No source found is an A for our content (a single stylised object with small, precise motion). Nobody has published a ledger-opens or briefcase-unlatches test for these models. The honest conclusion is that the 3-subject test in the plan is the only real evidence we will get.

| Finding | Models | Strength | Source |
|---|---|---|---|
| Artificial Analysis image-to-video arena (with audio, human blind votes; undated snapshot, newest entry Aug 2026): Seedance 2.5 rank 2 (Elo 1139), Wan 3.0 rank 4 (1127), Seedance 2.0 rank 6, Kling 3.0 Omni Pro rank 17 (1004), Kling 3.0 Pro rank 18 (1000, anchor). Seedance 2.5 and Wan 3.0 intervals overlap (1122-1156 vs 1111-1143), so they are statistically close. Wan 3.0 Prime and Kling 3.0 Std are not listed. This is a no-audio-unknown board, so Kling's weakness may partly be audio | all | B (general scenes, not object motion) | S27 |
| In a 49-case same-first-frame, same-seed, 720p test, Wan 3.0 kept faces, clothing, rooms and mountains stable where Seedance 2.0 drifted; when the prompt contradicted the image, Wan mostly kept the image and Seedance followed the prompt. Wan 3.0 beat rivals on glass-shatter and billiard physics. Main defect: uncommanded camera cuts, sometimes with ghosting, at about 3.5 s in an 8 s clip and 4-5 s and 15-17 s in 30 s clips. Compared against Seedance 2.0 and Wan 2.7, not Kling | Wan 3.0 | C (Atlas Cloud sells Wan, 25 Aug 2026) | S28 |
| Wan 3.0 Prime is the speed tier targeting the same visual output as Wan 3.0 | Prime | D | S29 |
| Wan 3 vs Wan 2.7 (fal, 30 Sep 2026): six test designs published, outcomes not written up, videos only. Notes prompt expansion on by default and can add 20-60 s latency | Wan | C, no results in text | S30 |
| Wan 3.0 vs Kling 3.0 (seedance.tv, 30 Aug 2026): a test method and benchmark prompts, no outcomes; samples explicitly "not a controlled A/B result" | Wan, Kling | D | S31 |
| Wan 3.0 vs Kling 3 (OrcaRouter, 18 Sep 2026): Kling ranks much higher on i2v than t2v in an arena (Pro 1080p Elo 1282, #9 on a board that differs from S27), attributed to element binding; lip-sync is Kling's most flagged weakness; about 2 of 5 dialogue clips needed retakes (one unnamed test). Competitor/reseller blog | Kling | C | S32 |
| Seedance 2.5 vs Kling 3.0 (AIReiter, 5 Aug 2026): no tests; claims Kling text legibility "strong", Seedance "average" and blurry distortions, no evidence | both | D | S33 |
| Seedance 2.5 review (Segmind, 8 Aug 2026): 18 runs, latency 60-227 s, small detail like condensation holds up, fast motion softens, a prompt naming a film stock was refused after full generation; reroll rate "the one number no review can give you". Says only 480p/720p, which conflicts with Higgsfield's schema (S25) | Seedance | C | S34 |
| Seedance 2.5 guide (Higgsfield, 2026): pin "FIRST FRAME AND BLOCKING" and PHYSICS in the prompt; prompts that omit detail fail "in a specific, predictable way"; prompts carry explicit negatives such as "no plastic CGI sheen"; nothing on last frame, drafts or cost | Seedance | D (vendor) | S35 |
| Kling 3.0 start/end frame: vendors describe the end frame both as a morph/transition tool and as drift reduction. No lid or hinge test found. Interpolating toward an end frame is a morphing risk for rigid objects | Kling | D | S36 |
| Kling 3.0 vs Seedance 2.0 (fal, 20 Apr 2026): four same-prompt tests (wind chime, paper boat), no written results, no i2v | Kling, Seedance 2.0 | C, no results | S37 |

### Cinematic promo shots (U2, separate view)

The only independent-ish ranking is the arena in S27: Seedance 2.5 and Wan 3.0 sit at the top, Kling 3.0 Pro far lower on the with-audio i2v board. Vendor pages claim Kling is strongest for multi-shot storytelling and text, and Seedance for reference control (S32, S33, S38). Nothing tests lamp-lit still-life shots. Treat the arena as a weak prior that Seedance 2.5 and Wan 3.0 are not clearly different for hero shots, with Wan about a quarter of the per-second price at 1080p (0.08 vs 0.796, inferred).

## 3. Unverified or conflicting (do not rely on these)

1. Resolution and sound meaning of Kling Standard's 0.042 vs 0.063/s. Strong hypothesis (inferred): 0.042 is sound off and 0.063 is sound on, because Kling's own audio uplift is 1.5x and 0.063 / 0.042 = 1.5, and the Pro pair (0.056 / 0.084) is also 1.5x. Higgsfield's page does not say it. Budget at 0.063 and test `sound: "off"` through the estimate endpoint.
2. Whether Kling Standard is 720p and Pro is 1080p on Higgsfield. Kling's own tiers say so (S39); Higgsfield pages leave the resolution blank.
3. Whether Seedance 2.5, Kling or Wan price changes with audio on or off. Not stated. Set audio off for MockMob clips regardless.
4. Whether the `/estimate/` call is itself free.
5. When the Kling 50% and Seedance 30% promos end. Wan ends 31 Oct (owner screenshot) or "November 1" (S5). Kling 3.0 at list would double the U1 cost.
6. Whether 1:1 output costs less, the same or more per second than 16:9 on Seedance and Kling (the token formula in S6 depends on pixel count; the exact 1:1 pixel size is not documented).
7. Whether Kling Standard and Seedance output matches a 1:1 input ratio. Docs say so only for Seedance.
8. Whether Wan 3.0 i2v accepts a negative prompt on Higgsfield (not in the schema; one reseller says Wan 3 supports it elsewhere).
9. Higgsfield's seed and negative prompt support for Kling 3.0 (not documented; the third-party claim of a seed option is unconfirmed).
10. Concurrency limit: 4 in the docs example vs 20 in the help centre.
11. Whether any free or starter credits exist on a new API account. None found; affiliate pages claiming so are unverified.
12. How reliably any of the four keeps a rigid stylised object on-model with a last-frame target, and the rejection rate. No evidence exists; the plan's 3-subject test is the experiment.
13. Seedance 2.5 maximum resolution (Segmind says 720p, Higgsfield schema lists 1080p and prices it) and whether `bitrate_mode: standard` is cheaper.
14. Kling 4.0 is reported as upcoming (S40, 27 Sep 2026) and not released; ignore.

## 4. Cost-saving tactics that are supported

| Tactic | Evidence | Saving |
|---|---|---|
| Draft at **480p on Wan 3.0** (USD 0.02/s) | S4, S5, S17 (480p allowed, 2 s minimum) | A 3 s draft is USD 0.06; 720p is about 2x, 1080p about 4x |
| Use the **shortest duration that works**: Wan min 2 s, Kling min 3 s, Seedance min 4 s | S17, S24, S25 | U1 needs 1.5-3 s; Seedance cannot go below 4 s so it is a poor fit for U1 |
| **Ship from a 480p or 720p source for U1** (target 512x512) | plan section 2 | No 1080p spend on U1 at all |
| **Audio off** on every call (`generate_audio: false`, `sound: "off"`) | S17, S24, S25; Kling's audio costs 1.5x in the vendor list (inferred for Higgsfield) | Up to one third on Kling (hypothesis 1) |
| Call `/estimate/` before every batch and write the number to the ledger | S1 | Catches price drift and the 1:1 and sound questions for free or near free |
| Use a **fixed nonzero seed** on Wan to compare prompt variants | S17 | Cuts retries; seed does not exist on Kling or Seedance |
| Send an `Idempotency-Key` on every submit; poll, do not resubmit | S14 | Avoids double billing on timeouts |
| Do not pay for failures: failed, nsfw, over-timeout and queued-cancelled are free; rejected-but-rendered are not | S1-S3 | Stop a clip early only while queued |
| Wan 3.0 beats Wan 3.0 Prime on cost; Prime is the speed tier | S5, S29 | Prime costs 1.36x for speed only; skip it |
| Run Wan work before 31 Oct (60% off; 50% afterwards) | owner screenshot, S5 | 25% |
| Upscale separately: Higgsfield has a Video Upscale tool but its price and quality were not found | S41 | Unknown; do not plan on it |
| Free daily credits | None for API (S19, S21) | None |
| Check the top-up path: minimum USD 5, same rate at any size; fund USD 5 first, top up only after the owner approves the test | S19 | Limits exposure |

## 5. Recommendation per use

**U1, object one-shots (ledger opens, briefcase unlatches, chart rises; 512x512, 1.5-3 s).**
- Explore and probably produce with **Wan 3.0 at 480p then 720p**, fixed nonzero seed, `generate_audio: false`, `aspect_ratio: "1:1"`, 3 s, `end_image_url` = the canonical existing still, `image_url` = a "before" keyframe (closed ledger, latched case, flat chart) made once with the GPT account. Reasons: explicit 1:1, seed, last frame, vendor-run evidence that Wan stays faithful to the first frame (S28, weak), and the lowest cost (USD 0.06 to 0.12 per 3 s clip, inferred).
- Run **Kling 3.0 Standard** (3 s, sound off, last frame, `cfg_scale` raised toward 0.7 to hold the prompt) as the A/B fallback on the same 3 subjects. USD 0.13 to 0.19 per 3 s clip. Kling has no seed and no negative prompt (S24).
- Do not use Seedance 2.5 or Prime for U1: 4 s minimum, 4-8x cost, no seed, no gain on a 512 px output.
- Test start-only vs start-plus-end on one subject first. End-frame control can interpolate and morph instead of moving rigidly (S36, vendor); it also guarantees the clip lands on the canonical still, which is the plan's ship rule.
- Keep prompts to one motion, one camera lock, "no other objects, no text changes, plain background unchanged". Put "camera static" in every prompt.

**U2, promo hero shots (2-4 cinematic shots).**
- Candidate round, 5 s each: **Wan 3.0 at 1080p** (about USD 0.40) and **Kling 3.0 Pro** (USD 0.28 to 0.42). Cost per shot about 0.8 for both.
- **Seedance 2.5 at 720p only** (about USD 1.62 per 5 s) for any shot the cheaper pair cannot hold, and only after the owner picks that shot. Never 1080p unless one final is explicitly approved (USD 3.98 per 5 s).
- Watch Wan for uncommanded cuts after about 3 s (S28): keep U2 shots 4 to 5 s and ask for one continuous shot.

**U3, milestone moment.** Reuse the U1 winner and settings. One clip, 3 s, 720p, 1 to 2 tries, about USD 0.5 total.

## 6. Revised USD 15 budget

Rates used: Wan 3.0 480p 0.02, 720p 0.04, 1080p 0.08 (inferred, 60% off, expires 31 Oct); Kling 3.0 Standard 0.063 (pessimistic end); Kling Pro 0.084 (pessimistic end); Seedance 2.5 720p 0.3235. Attempts per kept clip: 2 in the test, 2.5 in the rollout (no rejection data exists, so this is an assumption).

| Step | Model and mode | Plan | Cost (USD) |
|---|---|---|---|
| 0 | none | Keyframes from the GPT account (before-state stills), prompt sheets, call `/estimate/` for every planned mode and log it | 0 |
| 1 | Wan 3.0, 480p | 3 subjects x 4 prompt variants x 3 s = 36 s, seed fixed, audio off | 0.72 |
| 2 | Wan 3.0 720p and Kling 3.0 Std | 3 subjects x 3 s x 2 tries each: Wan 18 s (0.72), Kling 18 s (1.13) | 1.85 |
| 3 | Owner review | Watch in place; stop unless approved | 0 |
| 4 | Winner of step 2 | 12 subjects x 3 s x 2.5 attempts = 90 s: Kling 5.67, or Wan 720p 3.60. Budget the Kling case | 5.70 |
| 5 (U2) | Wan 1080p and Kling Pro, plus Seedance 2.5 720p | 3 shots x 5 s, both cheap models one try each (about 2.5), plus Seedance 720p on 1 shot, 1 try (1.62) | 4.10 |
| 6 (U3) | winner | 1 clip x 3 s x 2 tries | 0.40 |
| | | **Planned spend** | **12.77** |
| | | **Reserve** (failures, rejected clips, Wan price rise to 50% after 31 Oct, estimate drift) | **2.23 (about 15%)** |
| | | **Hard cap** | **15.00** |

If rollout in step 4 is Wan 720p instead of Kling, planned spend falls by 2.10 and the reserve grows to about 4.3. If the Kling promo ends before step 4 (list price doubles Kling), step 2 grows by 1.1 and step 4 by 5.7 if Kling wins; in that case switch step 4 to Wan 720p. If step 1 and 2 show that U1 is clean at 480p, shipping 480p cuts the Wan lines by half.

Rules to add to the plan's ledger rule: log the `/estimate/` result before each call; compare actual balance to estimate after each call; stop at USD 12.77 planned spend and ask the owner before touching the reserve; fund USD 5 first (minimum top-up) and top up the rest only after the step 3 approval.

Sensitivity of Seedance 2.5 (USD 15 cap): one 5 s clip at 1080p is 3.98, three are 11.94 and exhaust 80% of the budget on a single model. That is why it is limited to 720p and one hero shot here.

## 7. Verified vs the draft plan, summary

| Plan statement | Verdict |
|---|---|
| Wan 3.0 USD 0.020/s for exploration | True at 480p only; 720p 0.04, 1080p 0.08 (inferred) |
| Wan 3.0 Prime better drafts | Prime is the speed tier at 1.36x the price (S5, S29); no quality evidence; skip |
| Kling 3.0 USD 0.042/s production | 0.042 is the "1 second" or sound-off figure; 3-15 s clips show 0.063; 50% off not 60%; no resolution field on Standard |
| Kling "1080p about 2x" | Wrong model of pricing; Pro and Turbo are separate endpoints (Pro 0.056-0.084, Turbo 0.056/0.07) |
| Seedance 2.5 USD 0.144/s for hero shots | 480p only; 720p 0.3235, 1080p 0.796; 4 s minimum |
| Step 5 USD 3.0-4.5 for 15 s | 15 s at 720p is 4.85; at 1080p 11.94 |
| Failed generations | Not charged (confirms the plan's reserve logic) |
| Last frame to end on the canonical still | Supported on Wan, Wan Prime, Kling Std/Pro/4K and Seedance; not on Kling Turbo |

## 8. Sources (all fetched 16 Oct 2026; document dates in brackets where shown)

- S1 https://docs.higgsfield.ai/docs/concepts/billing-and-retention.md (official docs)
- S2 https://docs.higgsfield.ai/docs/concepts/errors.md (official)
- S3 https://docs.higgsfield.ai/docs/help/faq.md (official)
- S4 https://open.higgsfield.ai/models/alibaba%2Fwan-3.0%2Fimage-to-video (official model page, Wan 3.0 list rates)
- S5 https://open.higgsfield.ai/models/alibaba%2Fwan-3.0-prime%2Fimage-to-video (official model page, Prime rates, "60% off until November 1")
- S6 https://open.higgsfield.ai/models/bytedance%2Fseedance-2.5%2Fimage-to-video (official model page, per-resolution rates and token formula)
- S7 https://docs.higgsfield.ai/docs/models/kling-3.md (official)
- S8 https://docs.higgsfield.ai/docs/models/kling-3/standard-image-to-video.md and https://docs.higgsfield.ai/docs/models/kling-3/pro-image-to-video.md (official)
- S9 https://open.higgsfield.ai/models/kling-video%2Fv3.0%2Fstd%2Fimage-to-video (official model page)
- S10 https://open.higgsfield.ai/models/kling-video%2Fv3.0%2Fpro%2Fimage-to-video (official model page)
- S11 https://open.higgsfield.ai/models/kling-video%2Fv3.0-turbo%2Fimage-to-video (official model page) and https://docs.higgsfield.ai/docs/models/kling-3/turbo-image-to-video.md
- S12 https://docs.higgsfield.ai/docs/concepts/requests.md (official)
- S13 https://docs.higgsfield.ai/docs/authentication.md (official)
- S14 https://docs.higgsfield.ai/docs/quickstart.md (official)
- S15 https://docs.higgsfield.ai/docs/concepts/polling.md (official)
- S16 https://docs.higgsfield.ai/docs/concepts/file-uploads.md (official)
- S17 https://docs.higgsfield.ai/docs/models/wan-3/image-to-video.md (official schema)
- S18 https://docs.higgsfield.ai/docs/models/wan-3-prime/image-to-video.md (official schema)
- S19 https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api (official help centre)
- S20 https://docs.higgsfield.ai/docs/concepts/rate-limits.md (official)
- S21 https://higgsfield.ai/blog/ai-video-api-pricing-vs-subscriptions [13-14 Oct 2026] (official blog; Kling 3.0 Standard 720p audio off USD 0.084 list)
- S22 https://omidsaffari.com/blog/higgsfield-api-pricing (third-party, Sep 2026, partly read via search snippet)
- S23 https://open.higgsfield.ai and https://www.wireflow.ai/blog/higgsfield-ai-pricing [12 Oct 2026] (pricing page list vs discounted; Wireflow is a competitor blog)
- S24 https://docs.higgsfield.ai/docs/models/kling-3/4k-image-to-video.md (official schema, same fields as Std/Pro)
- S25 https://docs.higgsfield.ai/docs/models/seedance-2-5/image-to-video.md (official schema)
- S26 https://docs.higgsfield.ai/docs/openapi.json (official; legacy Kling 2.5 paths with negative_prompt)
- S27 https://artificialanalysis.ai/video/leaderboard/image-to-video (arena, undated snapshot, newest entry Aug 2026)
- S28 https://www.atlascloud.ai/blog/guides/wan-3-0-review [25 Aug 2026] (vendor-run test)
- S29 https://www.cometapi.com/models/aliyun/wan-3-0-prime/ (reseller spec page, via search)
- S30 https://fal.ai/learn/devs/wan-3-vs-wan-2-7 [30 Sep 2026] (vendor, no results written)
- S31 https://www.seedance.tv/blog/wan-3-0-vs-kling-3-0 [30 Aug 2026] (method only)
- S32 https://www.orcarouter.ai/blog/wan-3-0-vs-kling-3 [18 Sep 2026] (reseller blog)
- S33 https://aireiter.com/blog/seedance-2-5-vs-kling-3-0-video-comparison [5 Aug 2026] (no tests)
- S34 https://blog.segmind.com/seedance-2-5-review-five-real-world-use-cases-and-exactly-what-each-one-costs/ [8 Aug 2026] (host vendor, hands-on, named author)
- S35 https://higgsfield.ai/blog/seedance-2-5-prompting-guide (official blog, read first 100,000 of 132,030 characters)
- S36 https://higgsfield.ai/blog/Expectations-from-Kling-3.0-User-Discussions-on-Updates and https://www.rundiffusion.com/kling-3-0-pro-ai-tool (vendor, via search)
- S37 https://fal.ai/learn/tools/seedance-2-0-vs-kling-3-0 [20 Apr 2026] (vendor, no written outcomes)
- S38 https://picsart.com/compare-models/seedance-2-5-vs-kling-3-0/ (undated marketing page)
- S39 https://higgsfield.ai/blog/ai-video-api-pricing-vs-subscriptions (Kling developer platform: 720p 0.6 units, 1080p 0.8 units at USD 0.14)
- S40 https://wavespeed.ai/blog/ai-comparisons/kling-4-0-vs-wan-3-0/ [27 Sep 2026] (Kling 4.0 not released)
- S41 https://creatify.ai/blog/higgsfield-vs-kling-ai-quality-cost-per-second-and-which-to-use-for-ads-in-2026 (third-party, via search; Video Upscale tool exists, cost not found)
