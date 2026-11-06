# Mistake Repair audit and the Score Recovery plan (14 October 2026)

Owner report: Mistake Repair ("Repair Lab" on the website, the repair flow in the app) often fails and is about 60% of what it should be. A repair costs 1 PrepOS credit, but the app's repair screen mostly shows what is already free (your answer and the correct answer). The feature was meant to be Score Recovery: more insight, the mistake explained another way, and a real path to not repeating it.

How this was done: read-only. No code changed, no database written, no model called (not even a small one). Code read:
- Website: `mockmob-hotfix`, branch `deploy/nta-r5` at `b5f07fb3`, which equals production main.
- App: `wt-phase2/flutter_app`, branch `ui/phase2` at `3661f246`.

The diagnostic SQL in section 3 was run only against an in-memory PGlite built from the real migrations, to prove it parses and the columns exist. All 12 queries ran. It has not been run on production.

Paths below are relative to `mockmob-hotfix/` (website) or `wt-phase2/flutter_app/` (app) unless they say otherwise.

---

## 0. The short version

**Why it fails so often.** Three causes, most likely first.

1. **Nothing limits how long a repair may take, and a killed repair keeps the student's credit for good.**
   - The route has no `maxDuration` (`src/app/api/recovery/repair/route.js`, 22 lines, none set).
   - The OpenAI client has no timeout (`src/services/ai/providers.js:51`), so the SDK default of 10 minutes applies (openai 6.34.0, `client.js:637`).
   - One repair can make up to 6 reasoning calls in a row. The blind check runs at `high` effort with a 10,900-token output cap.
   - The app gives up after 45 s (`lib/features/review/data/repair_api.dart:26`) and tells the student "You are offline".
   - When Vercel kills the function, the credit reservation stays `executing` forever. The expiry sweep `mm_ai_release_expired` exists but nothing ever calls it (`supabase/migrations/20261002130000_prepos_credit_reservations.sql:259`; the only caller is a test).
   - From then on, every retry with the same request answers 409 "still being prepared", and the credit is gone until the month resets.

2. **Bugs in what the model is given make some mistakes fail every time.** These are deterministic.
   - Reading-comprehension questions are sent **without their passage**. The prompt reads `question.passage_text` (`data/mistake_repair.js:53,62`), but attempt snapshots store `passageText` (`data/db.js:184`).
   - What follows is one of three things: a dispute, "No repair for this one", a good question **pulled from practice**, or an explanation invented without the passage.
   - **NTA papers with shuffled options** (live since 13 to 14 Oct) are compared index by index with the unshuffled database row (`data/mistake_repair.js:34-35`). Most NTA mistakes are therefore refused as "answer was corrected after your session", which is false.
   - The banned-words filter (`data/mistake_repair.js:14`) rejects normal teaching text: "rank" (Spearman's rank correlation, ranking puzzles), "percentile", "guarantees" (Constitution), "you will get".

3. **Provider failures can't be seen or told apart, and the fallback can't help.**
   - Quota (429 `insufficient_quota`), rate limits, a rejected parameter, the monthly cap and a missing price row all end as the same 502 `unusable_output`.
   - The provider's error text is thrown away (`providers.js:177`), and nothing is logged.
   - The "fallback" is the same model from the same provider (`providers.js:250-252`). An OpenAI credit or quota problem therefore fails 100% of repairs and every PrepOS reply.
   - Live GPT-6 Luna was never verified in production (`docs/brain/STATUS.md:318`, `:1726`, `:1734`, `:1748`).

Also important for the app:
- Any error while reserving the credit comes back as `paused` (`src/services/recovery/mistakeRepair.js:68,72`).
- The app then turns the **rest of the run** into key-only reviews (`lib/features/review/data/repair_run.dart:208-211,254`).
- That gives exactly what the owner saw: a screen with the question, your answer and the key.

**What makes the credit worth it.** Five product changes, all on both web and app.

1. **Repair v2 content** in one model call, grounded in the passage and the book explanation:
   - the trap named from a fixed list;
   - why the option tempted and where it breaks;
   - the idea explained another way, with a worked contrast;
   - a one-line rule to keep.

   The paid part leads the screen, and the question folds away.
2. **A fresh check right after the repair**: 2 unseen bank questions from the same chapter and concept, answered inline and free. This makes "Checked" real.
3. **Free, factual context**:
   - what this answer cost in this session ("6 marks: 5 not earned and 1 penalty");
   - "you also missed this question in Mock 3";
   - the pattern across this student's repaired mistakes (same trap, same chapter).
4. **"Holds"**: a spaced re-check at +2 and +7 days on another unseen question, with a reminder, kept on the server so it follows the student across devices.
5. **"Explain it another way" once per repair**, included in the credit, plus a shared cache per (question, chosen option) so repeats are instant and consistent.

---

## 1. What a repair does today

### 1.1 The server path, step by step

`POST /api/recovery/repair { attemptId, questionId, requestId }`

| # | Step | Code | If it fails |
|---|---|---|---|
| 1 | Sign-in (cookie or `Authorization: Bearer`) | `route.js:10-11`, `src/lib/auth.ts:55-58` | 401 |
| 2 | Rate limit: 12 per minute per user and IP, held **in memory per server instance** | `route.js:12-13`, `src/lib/server/rateLimit.js:27-69` | 429 `rate_limited` (no `Retry-After` header) |
| 3 | Body check, then load the user | `route.js:14-18` | 422 / 404 |
| 4 | `requestId` must match `^[A-Za-z0-9_-]{16,64}$` | `mistakeRepair.js:19,41` | 400 `request_id_required` |
| 5 | Load the attempt and the **current** question row | `mistakeRepair.js:43-45` | 503 `question_unavailable` |
| 6 | Eligibility: own attempt, a wrong answer, a valid snapshot, a live question that is not disputed, and the current key index equal to the snapshot key index | `data/mistake_repair.js:23-37` | 404 / 422 / 409, with an answer review attached when one exists (`mistakeRepair.js:47-52`) |
| 7 | **Stored repair?** The latest committed reservation for `repair:<mistake id>:%` that has `receipt.repair` is returned free | `mistakeRepair.js:57-60` | none (this also works while AI is paused) |
| 8 | Gate: `RELEASE_GATES.runtimeAi` and not `PREPOS_MODEL_REPLIES_DISABLED` | `mistakeRepair.js:62`, `src/services/prepos/replyDeps.js:12-14`, `data/capabilities.js:8,24` | 503 `paused` |
| 9 | Reserve 1 credit with `mm_ai_reserve_credits` (wallet locked, ledger row written, idempotent per operation key) | `mistakeRepair.js:66-74`, migration `…130000…:46-144` | 402 out of credits; 409 released or in progress; **503 `paused` for any other error** |
| 10 | Mark executing (expiry set to now + 10 min) | `mistakeRepair.js:81-82`, migration `:146-170` | release, then 503 `could_not_start` |
| 11 | Model call(s) through `generateAIResponse` (section 1.3) | `mistakeRepair.js:84-88` | release, then 502 `unusable_output` |
| 12 | Interpret: `solved_index` must equal the key and `agrees_with_key` must be true; each text field must be at least 8 characters; banned words are checked | `data/mistake_repair.js:69-78` | release, then 502 `unusable_output`; or the dispute path (1.4) |
| 13 | Commit the credit with the repair stored in the receipt, then read the wallet | `mistakeRepair.js:110-117` | the student is told `charged: 0`, but the reservation stays `executing` and the credit is not returned (no sweep) |

### 1.2 What is free and what is charged

- **Charged:** 1 PrepOS credit, only when the outcome is `explained` and the commit succeeds (`mistakeRepair.js:111-115`).
  - Credits come from the same monthly wallet as PrepOS replies: 10 a month free, 50 a month Pro (`src/services/credits/aiCreditWallet.js:16-17,53-56`).
  - Bonus credits from top-ups exist, but top-up sales are closed (`data/capabilities.js:8`, `aiCommerce: false`).
- **Free:**
  - reopening a stored repair (`stored`);
  - every refusal before the reservation (eligibility, gate, out of credits);
  - every failure after it, which is released (`fail()`, `mistakeRepair.js:76-80`);
  - `held_for_recheck` and `not_explained`, which are released (`:104`);
  - the book explanation and the key on the result page;
  - the "Practise 5 on this chapter" link. That one is a separate practice session with its own practice-credit cost: web `practiceHref`, `data/mistake_repair.js:81-83`; app `RetryCard`, `lib/features/review/widgets/outcome_views.dart:176-211`.
- **Charged by accident:** a credit stays taken when the function dies mid-call, or when the commit fails. Nothing ever returns it (section 2, rows 1 and 15).

### 1.3 Every model call in one repair

All calls go through `generateAIResponse` (`src/services/ai/providers.js:225-346`). Before each physical call the runtime guard books its own reservation, keyed `<operationKey>:<stage>` (`providers.js:146`, `src/services/ai/runtimeGuard.js:3-10`).

| Stage | When | Model | Reasoning | Output cap (`max_completion_tokens`) | Format | Timeout | Reserved USD (about) |
|---|---|---|---|---|---|---|---|
| `…:primary` | always | `AI_REPAIR_MODEL` or `gpt-6-luna` (`mistakeRepair.js:37`) | `low` (`:38`) | 950 + 2,500 headroom = **3,450** (`providers.js:89-94,254`) | `json_object` | **none** (SDK default 10 min) | ~$0.0019 |
| `…:repair` | the first reply was not valid JSON or failed the schema | same | `low` | 3,450 | `json_object` | none | ~$0.0019 |
| `…:fallback` | the first call failed, or the JSON is still invalid | `AI_LUNA_MODEL` or `gpt-6-luna`, **same provider** (`providers.js:250-252`) | `none` (`:301`) | 950 | `json_object` | none | ~$0.0007 |
| `…:blind:primary` | only when the first answer disputes the key | same Luna | `high` (`mistakeRepair.js:38,96`) | 900 + 10,000 = **10,900** | `json_object` | none | ~$0.0055 |
| `…:blind:repair` | invalid blind JSON | same | `high` | 10,900 | `json_object` | none | ~$0.0055 |
| `…:blind:fallback` | blind still failing | same | `none` | 900 | `json_object` | none | ~$0.0005 |

- **Typical success:** 1 call. **Worst case:** 6 calls, in sequence.
- **Booked when every call fails:** about $0.016. The guard books the full reservation when a call fails (migration `20261004120000…:61`).
- **Input bound:** UTF-8 bytes of the messages + 64 per message (`runtimeGuard.js:6`).
- **Prices:** `gpt-6-luna` costs $0.10 per million input tokens and $0.50 per million output (`supabase/migrations/20261005090000…:5`). Price rows are refused 90 days after `verified_at` (`20261004120000…:40`).
- The 4 Oct measurement on gpt-4.1-mini was about $0.0004 per repair (`docs/brain/AI-MODEL-REPORT-2026-10-04.md`). No Luna measurement exists.
- `temperature` is not sent. Luna is treated as a reasoning model (`providers.js:90,154-156`).
- The prompt does not include the book explanation, and (because of the bug) not the passage either (`data/mistake_repair.js:39-55`).

### 1.4 The second opinion (blind check)

1. The first call is told the key (`data/mistake_repair.js:44`) and must "solve from scratch" first. It returns `solved_index` and `agrees_with_key`.
2. If the solve differs from the key, or `agrees_with_key !== true`, the result is "disputed" (`:73`).
3. A **blind** call (key not shown) solves at `high` effort (`mistakeRepair.js:94-98`).
   - **Blind answer also differs from the key** (it may also differ from the first answer):
     - the question is withheld, exactly like a student report (`mistakeRepair.js:24-33`);
     - a `question_interactions` row is written (`report`, `metadata.source = 'ai_key_dispute'`);
     - the question becomes `status='pending'`, `verification_state='disputed'`, `exploration_state='pending_review'`;
     - the credit is released and the outcome is `held_for_recheck`.
   - **Blind answer matches the key, or the blind call fails:** the outcome is `not_explained`, released (`:104-107`).
     - Even when the key and the high-effort solve agree, the student gets no repair. The system never re-explains with that confidence.
4. Both opinions come from the same model family. STATUS flagged this on 4 Oct ("AI dispute quarantine relies on one model family").

### 1.5 Stored repairs (caching)

- **Server:** a finished repair lives only in `ai_credit_reservations.receipt.repair` of the committed row. It is found by `user_id`, `state='committed'` and `operation_key like 'repair:<sha256(user|attempt|question)[0:24]>:%'` (`mistakeRepair.js:22,57-60`).
  - It is per student and per attempt. The same question answered wrong in another attempt is a new mistake and is charged and generated again.
  - Nothing is shared between students, although the trap behind (question, chosen option) is the same for everyone.
- **Cross-device record:** `GET /api/me/repair-record` rebuilds the list from those committed rows (`src/lib/server/repairRecord.js:74-86`). `checkedState` is always `not_available` while the content gate is closed (`:65`).
- **App:** `repair_local` keeps the status and the `requestId` per mistake, not the text (`lib/core/repositories/repair_local_repository.dart:72-75`). A reopen asks the server, so it needs a connection. The app does not call `/api/me/repair-record` yet (WEB-PARITY A12, "Missing (local only)").
- **Web:** outcomes are held in page state only. After a reload the button says "1 credit" again (`src/components/recovery/MistakeRepair.jsx:92`), but clicking it returns the stored repair free.

### 1.6 Website: what the student sees

The repair sits on the result page, under each wrong answer (`src/app/(app)/result/[id]/ResultPageClient.jsx:253-255`). It is fed by the "Repair" step of the Score Recovery Lab (`src/components/ScoreRecoveryLab.jsx:177-197`).

| Outcome | Web shows (`src/components/recovery/MistakeRepair.jsx`) |
|---|---|
| Idle | Button "Repair this mistake", "Why option B felt right, where it breaks, and the idea to keep", "1 credit" (`:86-96`) |
| Loading | Three stage lines that advance **on a 1.4 s timer, not on real state** (`:13-14,66-70`). This breaks the owner's standards on fake progress. |
| `explained` / `stored` | "Mistake Repair" and "Checked against the answer key (C)". Two cards: "Why option B felt right" and "Where it breaks". Then "The idea to keep", then **"Do this next Â· 10 minutes"** (a double-encoded middle dot, bytes C3 82 C2 B7 at `:141`). Footer: "1 credit used Â· N left" or "Saved repair Â· no credit used" (`:145`) |
| `held_for_recheck` | "We may have got this one wrong", with rows for your pick, the key, the first check and the blind check. Facts: out of practice, not charged, marks unchanged (`src/components/recovery/KeyReviewNotice.jsx`) |
| `not_explained` | "No repair for this one" and the server message (`:117-128`) |
| 402 | "Mistake Repair uses 1 PrepOS credit and you have 0 left this month. The stored explanation and fresh practice are still free." No retry. |
| 503 `paused` | "PrepOS paid features are temporarily unavailable. Your credits have not been used." and Try again |
| 502 | "The repair could not be prepared reliably this time. You were not charged." Try again first hits 409 "That attempt did not go through…", which is a wasted click (`data/repair_presentation.mjs:3-6`) |
| 409 `in_progress` | "This repair is still being prepared. Nothing extra is charged." and "Check again". This **loops forever** after a killed function. |
| Vercel 504 (non-JSON body) | "We could not confirm the repair result. Try again with the same request." Then the 409 loop above. |
| Network drop | "The connection dropped. Try again…" |

The web `fetch` has no timeout (`:33`).

### 1.7 App: what the student sees

The flow is `/review/repair/:attemptId/:questionId`: an entry screen, then one mistake at a time, then the ending (`lib/features/review/screens/repair_screen.dart`).

| Outcome | App shows |
|---|---|
| Entry | Chapter, number of mistakes, "Uses 1 credit per mistake. You have N." Variants for a short wallet, an empty wallet or a pause (`widgets/repair_entry_view.dart:26-47`) |
| Loading | "Working out the explanation" with skeleton lines (`widgets/mistake_view.dart:136-148`) |
| `explained` / `stored` | **The question panel with your answer and the correct answer comes first** (`mistake_view.dart:82`). Then the stage thread Found to Repaired (Checked and Holds dashed). Then "What happened here" (why_tempting and why_wrong), "The idea" (key_idea) and "Next time" (next_step) (`widgets/outcome_views.dart:57-65`). Then a Learn concept link, then "Practise 5 on <chapter>", a separate session (`:176-211`) |
| `held_for_recheck` | "Answer key under check. You were not charged." (`lib/features/review/copy.dart:184`) |
| `not_explained` | "We could not explain this one. You were not charged. Try another." and "Read the key explanation" (`copy.dart:186`) |
| 402 | **Every remaining mistake in the run** switches to the key explanation, with "Credits used up. They renew on <date>." (`repair_run.dart:208-211,253`) |
| 503 `paused` | **Every remaining mistake** switches to the key explanation, with "Explanations are paused right now." (`:254`). The server sends `paused` for any reserve error, not only a real pause. |
| 502 / 503 other / 504 | "The explanation could not be made. Try again." (`copy.dart:191`) |
| 409 `in_progress` | "Still working on this one. Try again in a moment." (`copy.dart:193`). Loops forever after a killed function, because the app reuses the stored `requestId` (`repair_local_repository.dart:74`). |
| 409 key changed, under review or withdrawn | "Answer key under check. Nothing was charged." (`repair_run.dart:255-261`) |
| Client timeout after 45 s | **"You are offline. Your place is kept."** (`api_error.dart:82` treats a timeout as offline; `copy.dart:194`) |

The app makes no automatic retry for a POST (`lib/core/api/api_client.dart:157`). It does retry once by itself after `operation_released`, with a fresh `requestId` (`repair_run.dart:243-247`).

### 1.8 Why the paid part feels thin

- The paid text is 4 fields capped at 45, 45, 45 and 30 words (`data/mistake_repair.js:9,46-49`). That is about 150 words in total.
- In the app it sits **under** a full question panel that repeats your answer and the key. That information is already free on the result and answer sheet.
- The model never sees the book explanation, so "The idea" often restates it rather than explaining it differently.
- `next_step` is generic and leads nowhere in the product. The only follow-up is a paid 5-question practice session.
- "Checked" and "Holds" exist as words and drawn stages, but nothing can fill them ("Fresh checks are not available yet…", `copy.dart:241`; `repairRecord.js:65`).
- Nothing connects this mistake to the student's other mistakes. Repeats of the same trap, or of the very same question, go unseen.

---

## 2. Every failure path, ranked

Likelihood is from code evidence. Production data has not been read, so section 3 gives the SQL that confirms or rules out each one. "Released" means the credit is returned at once. "Held" means it is taken and **never** returned, because no sweep runs.

| Rank | Condition | Evidence | HTTP and code | Student sees (web / app) | Credit |
|---|---|---|---|---|---|
| 1 | **Function killed or too slow**: no `maxDuration`; no OpenAI timeout; up to 6 sequential reasoning calls; blind at `high` with a 10,900-token cap | `route.js` (no `maxDuration`); `providers.js:51`; openai `client.js:637` (600,000 ms); `mistakeRepair.js:38,96`; `providers.js:89,254` | Vercel 504 | Web: "We could not confirm…", then the 409 loop. App: "You are offline…" after 45 s, or "could not be made" on a 504 | **Held for good**: the reservation stays `executing` and the runtime row stays `reserved` |
| 2 | **Stuck "in progress"** after any kill: retries reuse the `requestId`; the reserve finds the open row and returns 409 every time | `mistakeRepair.js:74`; migration `…130000…:90-99`; sweep never called (`:259-280`, test only); web `MistakeRepair.jsx:19,28`; app `repair_local_repository.dart:74` | 409 `in_progress` | Web: "still being prepared", Check again forever. App: "Still working on this one" forever. | Held |
| 3 | **App 45 s client timeout** while the server keeps working (the dispute path is the most exposed) | `repair_api.dart:26`; `api_error.dart:82` | none (client side) | App: "You are offline. Your place is kept." On retry: `stored` if it committed; a fresh full rerun after `operation_released`, often timing out again; or the 409 loop if it was killed | Charged if it later committed; otherwise released or held |
| 4 | **Passage never sent** (`passage_text` versus `passageText`): English reading comprehension and other passage sets | `data/mistake_repair.js:53,62` against `data/db.js:184`; no passage test in `data/tests/mistake_repair.test.mjs` | 200 `not_explained`, 200 `held_for_recheck`, or 200 `explained` with an invented reading | "No repair for this one" or "We may have got this one wrong" for a **good** question, which is then **pulled from practice** (`mistakeRepair.js:30`) | Released, or charged for a made-up explanation |
| 5 | **NTA shuffled options**: the snapshot holds served order and a remapped key, while the current row holds the original order | `src/lib/server/ntaPaper.js:49-79`, `data/nta_item_checks.js:877-903`, `src/lib/server/practiceSessions.js:63,75`; compared index by index in `data/mistake_repair.js:34-35` and `data/answer_corrections.mjs:4-11,36` | 409 `key_changed`, with review `content_changed` | Web: "The question changed after your session…" (false). App: "Answer key under check." | None. The repair is never offered. |
| 6 | **Provider error**: OpenAI 429 `insufficient_quota` or rate limit, 5xx, network, or a rejected parameter (`reasoning_effort` `none`/`low`/`high` or `json_object` with Luna, never verified live) | `providers.js:176-181` swallows it; same-provider fallback `:250-252`; STATUS `:318,1726,1734,1748` | 502 `unusable_output` (the `provider_error` path at `mistakeRepair.js:87` can never run, because `generateAIResponse` never throws) | Web: "could not be prepared reliably…". App: "could not be made. Try again." | Released |
| 7 | **Reserve RPC error** (Supabase timeout or connection, unexpected wallet error) is reported as "paused" | `mistakeRepair.js:67-68,72`; `replyDeps.js:25-29` | 503 `paused` | Web: "PrepOS paid features are temporarily unavailable." App: **the rest of the run becomes key explanations**, "Explanations are paused right now." | None |
| 8 | **Low-effort solve disputes a correct key**; the blind check agrees with the key, so nothing is explained | `mistakeRepair.js:92-107` | 200 `not_explained` | "No repair for this one" / "We could not explain this one" | Released |
| 9 | **Banned-words false positive**: `rank`, `percentile`, `guarantee[ds]`, `you will get` | `data/mistake_repair.js:14,76` | 502 `unusable_output` | as rank 6 | Released |
| 10 | **Invalid JSON or schema**: adds 1 or 2 more calls (more latency, feeding rank 1); a partial parse can still fail interpretation | `providers.js:269-323`; `mistakeRepair.js:88-90` | 502 `unusable_output` | as rank 6 | Released |
| 11 | Out of credits (10 a month free, shared with PrepOS replies) | `mistakeRepair.js:70`; `aiCreditWallet.js:16-17` | 402 | Web: the balance message. App: key-only run. | None (expected behaviour, but students feel it as a failure) |
| 12 | Monthly cap reached, guard paused by an overrun, or price row missing or older than 90 days, or `AI_REPAIR_MODEL`/`AI_LUNA_MODEL` set to an unpriced id. The cap is **shared** with PrepOS, Rival and question moderation (Luna `medium`, `src/lib/moderation/ai.js:100-109`). | migration `20261004120000…:33-46,64-65`; `runtimeGuard.js:8`; `providers.js:148` | 502 `unusable_output` | as rank 6, but every retry fails until the cause is fixed | Released |
| 13 | Gate closed (`runtimeAi` false or `PREPOS_MODEL_REPLIES_DISABLED=true`) | `replyDeps.js:12-14` | 503 `paused` | as rank 7 | None |
| 14 | Our own rate limit (12 per minute, in memory per instance) | `route.js:12-13` | 429 `rate_limited` | Web: "Please wait a moment…". App: "Please wait a minute." plus a 60 s local hold (`api_client.dart:187-188`) | None |
| 15 | Commit fails after a good repair | `mistakeRepair.js:112-115` | 200 `explained`, `charged: 0` | The repair shows and says no credit was used. It is **not stored**, so a reopen charges again. | Held (no sweep) |
| 16 | Withholding the question fails during a dispute | `mistakeRepair.js:100-103` | 503 `quarantine_not_confirmed` | "…Please report this question. You were not charged." | Released |
| 17 | `markExecuting` fails | `mistakeRepair.js:81-82` | 503 `could_not_start` | "The repair could not start. You were not charged." | Released |
| 18 | Page reload while a repair runs: the web makes a new `requestId`, so a second reservation runs alongside | `MistakeRepair.jsx:20,28`; no "one open repair per mistake" check | 200 twice | Two explanations | **Can charge 2 credits** |
| 19 | Eligibility refusals that are correct (not yours, not a mistake, bad snapshot, withdrawn, under review, key really changed) | `data/mistake_repair.js:23-37` | 404 / 422 / 409 | Answer review or notice | None |

**What explains "it fails many times".**
- Ranks 1 to 3 together:
  - with no time budget, slow repairs die;
  - with no sweep, every later retry of that mistake fails (409 forever), and the credit is gone;
  - in the app the student is told they are offline.
- Ranks 4 and 5 fail **every** time on whole classes of questions: English passages, which is a launch subject, and NTA papers since 13 to 14 Oct. Retrying cannot help.
- Rank 6 fails **everything at once** when it happens (an OpenAI credit balance or project limit). Today it looks like ordinary 502s, and PrepOS replies fail the same way.
- Rank 7 explains the app's "mostly free content" screen even when the model is fine: one wallet hiccup turns the whole run into key reviews.

**Related bug outside Mistake Repair (please route to the NTA owner).**
- `readAnswerReviews` (`src/services/recovery/answerReviews.js:16`) runs the same index-by-index comparison on every question of a shuffled NTA attempt. `sameQuestionContent` fails whenever options moved, so the review becomes `content_changed`.
- The result page then marks those questions as held (`ResultPageClient.jsx:72`) and hides the key.
- This is high confidence from the code, but untested: no test runs `answerReview` on a shuffled snapshot. Reproduce it on one NTA attempt before fixing.

---

## 3. Production diagnostics (read only)

### 3.1 SQL for the Supabase SQL editor (production)

SELECT only. Run one query at a time. Table and column names come from the migrations: `20261002121000_runtime_ai_guard.sql`, `20261002130000_prepos_credit_reservations.sql`, `20261004120000_runtime_ai_monthly_cap.sql`, `20261005090000_runtime_ai_price_gpt6_luna.sql`, `0001_init.sql`, `0010_phase1_compat.sql`. All 12 queries were checked on an in-memory copy of those migrations.

```sql
-- Mistake Repair diagnostics for production. READ ONLY: every statement is a SELECT.
-- Window: the last 14 days unless a query says otherwise. Times are shown in IST.

-- Q1. Repair operations by final state and release reason, with how long each took
--     (reserve -> last update; for committed rows that is reserve -> commit).
select r.state,
       coalesce(r.release_reason, '-') as reason,
       count(*) as repairs,
       count(distinct r.user_id) as students,
       round((percentile_cont(0.5) within group (order by extract(epoch from (r.updated_at - r.created_at))::float8))::numeric, 1) as p50_seconds,
       round((percentile_cont(0.9) within group (order by extract(epoch from (r.updated_at - r.created_at))::float8))::numeric, 1) as p90_seconds,
       round(max(extract(epoch from (r.updated_at - r.created_at)))::numeric, 1) as max_seconds,
       count(*) filter (where r.state in ('reserved', 'executing') and r.expires_at < now()) as stuck_past_expiry
from public.ai_credit_reservations r
where r.action = 'score_recovery_repair'
  and r.created_at > now() - interval '14 days'
group by 1, 2
order by repairs desc;

-- Q2. Per IST day: repairs started, explained, and each kind of failure.
select (r.created_at at time zone 'Asia/Kolkata')::date as ist_day,
       count(*) as started,
       count(*) filter (where r.state = 'committed') as explained_and_charged,
       count(*) filter (where r.release_reason = 'unusable_output') as model_or_output_failed,
       count(*) filter (where r.release_reason = 'ai_key_dispute') as held_for_recheck,
       count(*) filter (where r.release_reason = 'ai_inconsistent') as not_explained,
       count(*) filter (where r.release_reason in ('could_not_start', 'provider_error', 'quarantine_not_confirmed')) as other_failures,
       count(*) filter (where r.release_reason = 'expired') as returned_by_sweep,
       count(*) filter (where r.state in ('reserved', 'executing')) as still_open,
       round(100.0 * count(*) filter (where r.state = 'committed') / nullif(count(*), 0), 1) as success_pct
from public.ai_credit_reservations r
where r.action = 'score_recovery_repair'
  and r.created_at > now() - interval '14 days'
group by 1
order by 1 desc;

-- Q3. Is it repair-specific or every paid AI feature? All AI credit actions side by side.
select r.action,
       r.state,
       coalesce(r.release_reason, '-') as reason,
       count(*) as operations
from public.ai_credit_reservations r
where r.created_at > now() - interval '14 days'
group by 1, 2, 3
order by 1, operations desc;

-- Q4. Every physical model call behind repairs, by stage and outcome.
--     stage: repair_primary / repair_repair (JSON retry) / repair_fallback, and the same for blind_.
--     never_receipted = the function died (timeout) or the call is still running.
select case when q.request_key like '%:blind:%' then 'blind_' else 'repair_' end
         || substring(q.request_key from '[^:]+$') as stage,
       q.model,
       case when q.state = 'reserved' then 'never_receipted'
            when q.receipt ? 'error' then 'transport_error'
            when coalesce((q.receipt -> 'response' ->> 'ok')::boolean, false) then 'ok'
            else 'other' end as outcome,
       count(*) as calls,
       count(*) filter (where q.receipt ? 'response' and coalesce(q.receipt -> 'response' ->> 'raw', '') = '') as empty_text,
       round(avg((q.receipt -> 'usage' ->> 'prompt_tokens')::numeric), 0) as avg_input_tokens,
       round(avg((q.receipt -> 'usage' ->> 'completion_tokens')::numeric), 0) as avg_output_tokens,
       round(avg((q.receipt -> 'usage' -> 'completion_tokens_details' ->> 'reasoning_tokens')::numeric), 0) as avg_reasoning_tokens,
       round(sum(coalesce(q.actual_usd, q.reserved_usd)), 4) as usd_booked
from public.runtime_ai_requests q
where q.request_key like 'repair:%'
  and q.created_at > now() - interval '14 days'
group by 1, 2, 3
order by 1, 2, 3;

-- Q5. Student AI spend this IST month against the cap, and the guard's own state.
with m as (select (date_trunc('month', now() at time zone 'Asia/Kolkata') at time zone 'Asia/Kolkata') as month_start)
select b.monthly_cap_usd,
       b.paused as guard_paused,
       round(s.month_spend, 4) as month_spend_usd,
       round(100 * s.month_spend / nullif(b.monthly_cap_usd, 0), 1) as pct_of_cap,
       b.spent_usd as spent_all_time_usd,
       b.reserved_usd as open_reservations_usd
from public.runtime_ai_budget b
cross join (select coalesce(sum(coalesce(q.actual_usd, q.reserved_usd)), 0) as month_spend
            from public.runtime_ai_requests q, m
            where q.created_at >= m.month_start) s
where b.id = 'student_ai';

-- Q6. This month's spend by feature (repair, prepos, moderation, rival ...). The cap is shared.
with m as (select (date_trunc('month', now() at time zone 'Asia/Kolkata') at time zone 'Asia/Kolkata') as month_start)
select split_part(q.request_key, ':', 1) as feature,
       q.model,
       count(*) as calls,
       count(*) filter (where q.state = 'reserved') as never_receipted,
       round(sum(coalesce(q.actual_usd, q.reserved_usd)), 4) as usd_this_month
from public.runtime_ai_requests q, m
where q.created_at >= m.month_start
group by 1, 2
order by usd_this_month desc;

-- Q7. Prices the guard accepts (a model with no usable row is refused on every call).
select provider,
       model,
       input_per_million,
       output_per_million,
       verified_at,
       verified_at + interval '90 days' as refused_after,
       verified_at + interval '90 days' > now() as usable_now
from public.runtime_ai_prices
order by provider, model;

-- Q8. Credits held by reservations that never finished (all AI actions, all time:
--     nothing schedules the expiry sweep, so these never come back on their own).
select r.action,
       r.state,
       count(*) as open_rows,
       count(*) filter (where r.expires_at < now()) as past_expiry,
       count(distinct r.user_id) as students,
       sum(r.amount) as credits_held,
       sum(r.from_bonus) as bonus_credits_held,
       min(r.created_at at time zone 'Asia/Kolkata') as oldest_ist,
       max(r.created_at at time zone 'Asia/Kolkata') as newest_ist
from public.ai_credit_reservations r
where r.state in ('reserved', 'executing')
group by 1, 2
order by open_rows desc;

-- Q9. The open repair reservations themselves (newest first).
select r.operation_key,
       r.user_id,
       r.state,
       r.amount,
       r.created_at at time zone 'Asia/Kolkata' as created_ist,
       r.expires_at at time zone 'Asia/Kolkata' as expires_ist,
       round(extract(epoch from (now() - r.created_at)) / 60) as minutes_open
from public.ai_credit_reservations r
where r.state in ('reserved', 'executing')
  and r.action = 'score_recovery_repair'
order by r.created_at desc
limit 100;

-- Q10. Physical calls never receipted (a killed function leaves these), per IST day and feature.
select (q.created_at at time zone 'Asia/Kolkata')::date as ist_day,
       split_part(q.request_key, ':', 1) as feature,
       count(*) as never_receipted,
       round(sum(q.reserved_usd), 4) as usd_counted_at_full_reservation
from public.runtime_ai_requests q
where q.state = 'reserved'
  and q.created_at < now() - interval '10 minutes'
  and q.created_at > now() - interval '14 days'
group by 1, 2
order by 1 desc, 3 desc;

-- Q11. Questions pulled from practice by a repair dispute, and whether they carry a passage.
--      (to_jsonb keeps this query working even if a column is missing in production.)
select qi.created_at at time zone 'Asia/Kolkata' as reported_ist,
       q.subject,
       q.chapter,
       q.id as question_id,
       q.status,
       q.verification_state,
       (coalesce(to_jsonb(q) ->> 'passage_text', '') <> '' or to_jsonb(q) ->> 'passage_group_id' is not null) as passage_question,
       qi.metadata ->> 'solved_index' as first_check,
       qi.metadata ->> 'blind_index' as blind_check,
       qi.metadata ->> 'model' as model
from public.question_interactions qi
join public.questions q on q.id::text = qi.question_id::text
where qi.interaction_type::text = 'report'
  and qi.metadata ->> 'source' = 'ai_key_dispute'
  and qi.created_at > now() - interval '14 days'
order by qi.created_at desc;

-- Q12. NTA papers with shuffled options (their mistakes are refused as "key changed" today).
select (a.completed_at at time zone 'Asia/Kolkata')::date as ist_day,
       count(*) as nta_attempts,
       count(*) filter (where a.selection_meta -> 'ntaOptionLayout' ->> 'shuffled' = 'true') as shuffled_attempts,
       coalesce(sum(a.wrong) filter (where a.selection_meta -> 'ntaOptionLayout' ->> 'shuffled' = 'true'), 0) as wrong_answers_in_shuffled
from public.attempts a
where a.selection_meta ->> 'mode' = 'nta'
  and a.completed_at > now() - interval '14 days'
group by 1
order by 1 desc;
```

### 3.2 How to read the results

| You see | It means | Fix in section 4 |
|---|---|---|
| Q1: `executing` rows with `stuck_past_expiry` > 0, plus Q10 `never_receipted` on the same days | Functions are being killed (rank 1). Q8 shows how many credits students lost. | R2, R5 |
| Q1 `max_seconds` clustering near 10, 15, 60 or 300 | That number is the effective Vercel limit (see 3.5) | R2 |
| Q4 `repair_primary` mostly `transport_error`, while `repair_fallback` is `ok` | Luna rejects `reasoning_effort: low` or `json_object` with reasoning. The `none` fallback is doing all the work. | R3, R4 |
| Q4 everything `transport_error`, and Q3 shows `prepos_*` failing too | Provider-wide: an OpenAI credit balance, project limit, key or model access problem (rank 6). Check the OpenAI dashboard (3.4). | R4, R6 |
| Q4 `empty_text` > 0 with high `avg_reasoning_tokens` | Reasoning used up the output cap and returned no text | R3 |
| Q2 `model_or_output_failed` high but Q4 mostly `ok` | Output rejected after the model answered: banned words, short fields, out-of-range index (ranks 9 and 10) | R8 |
| Q2 `not_explained` and `held_for_recheck` high, and Q11 `passage_question = true` | The passage bug (rank 4). Q11 lists the good questions that were pulled from practice. | R1, D5 |
| Q12 shuffled NTA attempts with wrong answers > 0, and no repairs from them in Q2 | NTA refusals (rank 5) | R1 |
| Q5 `pct_of_cap` near 100, or `guard_paused = true`; Q7 `usable_now = false` for the model in use | Budget or price stop (rank 12) | owner check; R7 copy |
| Q6 `moderation` or another feature using most of the month | The USD 25 is shared. Repairs are starved by another feature. | D10 |

Not visible in the database: refusals that never reserve (eligibility, gate, out of credits, rate limit). Those only show as status codes in the Vercel logs.

### 3.3 What to look for in the Vercel logs

Project `mockmob`, then Logs. Filter on path `/api/recovery/repair`, method POST, last 14 days.

- **504**, or the line `Vercel Runtime Timeout Error: Task timed out after N seconds`, means the function was killed (rank 1). Note N: it is your real limit. The Duration column clustering at one value says the same.
- **502** means `unusable_output`, which covers provider errors, banned words and bad JSON. **503** means `paused`, `could_not_start`, `question_unavailable` or `quarantine_not_confirmed`. **409** means `in_progress` (look for the same student repeating it), `key_changed` or `operation_released`. **402** means out of credits. **429** is our own limit.
- **The 429 `insufficient_quota` text will not appear in today's logs.**
  - The repair code logs nothing.
  - The provider error is dropped (`providers.js:177-181`).
  - The OpenAI SDK reports failed responses only at `info` level, and its default is `warn` (openai `client.js:150-156,353`).
- To see status lines temporarily, set `OPENAI_LOG=info` in Vercel Production and redeploy. This is a config change, so it is the owner's call. Lines then read `POST https://api.openai.com/v1/chat/completions failed with status 429 in 312ms`. They show the status but not the error code; R6 adds that.
- Compare `/api/ai/mentor/chat` (PrepOS) over the same hours. If it fails together with repairs, the cause is the provider, not the repair code.

### 3.4 OpenAI dashboard

- **Settings, Organization, Billing**: prepaid credit balance and auto-recharge. A balance at or below zero gives 429 `insufficient_quota` on every call.
- **Settings, Organization, Limits**: usage tier, monthly budget, and the rate limits for `gpt-6-luna` (RPM and TPM).
  - The requested `max_completion_tokens` counts toward the token-rate estimate: 3,450 per repair call and 10,900 per blind call.
- **Usage** (filter by project, API key and model `gpt-6-luna`): request counts and errors on the failing days.
- **Settings, Project, Limits** for the project that owns the production key: the model allowlist must include `gpt-6-luna`, and any project budget must not be exhausted. Match the key by its last 4 characters against Vercel's `OPENAI_API_KEY`.
- The free key checks at 22:30 IST were made with the **local** key. Production keys live in Vercel and may belong to a different project.

### 3.5 Vercel settings to check

These come from Vercel docs, read on 14 Oct through Context7.

| Fluid compute | Hobby default / max | Pro default / max |
|---|---|---|
| On (the default for projects created after 23 Apr 2025) | 300 s / 300 s | 300 s / 800 s |
| Off (older projects) | 10 s / 60 s | 15 s / 300 s |

`src/app/api/internal/refresh-inventory/route.js:6` deploys with `maxDuration = 300`. That most likely rules out Hobby without fluid compute. If the project is **Pro without fluid compute, every repair has 15 s**, which a reasoning call with a schema retry can easily exceed.

Check: Project Settings, Functions (the Fluid Compute switch and default max duration), and the team plan.

---

## 4. Reliability fixes (concrete)

Ordered by impact. Every server change keeps the reserve, execute and commit-or-release lifecycle and the runtime guard. Every client change ships on web and app together.

**R1. Fix the two input bugs (deterministic failures).**
- `data/mistake_repair.js:53,62`:
  - use `question.passageText ?? question.passage_text`, and include `passageTitle`, in both the repair prompt and the blind prompt;
  - add the stored book explanation as evidence ("Book explanation: …") to the repair prompt only, never to the blind prompt, because it reveals the key;
  - add tests in `data/tests/mistake_repair.test.mjs` with a real snapshot shape.
- NTA: map served indices to stored ones before comparing. Use `attempt.selectionMeta.ntaOptionLayout.order[qid]`, where served position i shows stored option `order[i]`.
  - Repair eligibility: `data/mistake_repair.js:23-37` (pass the layout from `src/services/recovery/mistakeRepair.js:46`). Keep using the snapshot (served order) for the prompt, `chosenIndex` and `keyIndex`, so the letters match what the student saw.
  - `answerReview`: `data/answer_corrections.mjs:4-11,30-37`, called from `src/services/recovery/answerReviews.js:16` and `mistakeRepair.js:50`. Compare option text as a set or through the mapping, and map `currentIndex` back to served order.
  - Tests: shuffled snapshot cases in `data/tests/answer_corrections.test.mjs`.

**R2. A real time budget, end to end.**
- `src/app/api/recovery/repair/route.js`: `export const maxDuration = 90;`. Every plan above allows it. It leaves room for after-response work (R3).
- `src/services/ai/providers.js`:
  - pass a per-request timeout: `client.chat.completions.create(body, { timeout: ms, maxRetries: 0 })` (supported, openai `client.js:526`), and the same for Anthropic;
  - add a `deadlineAt` to `generateAIResponse`; skip any further attempt when less than 8 s remain.
- Student path:
  - server deadline 40 s from request start;
  - main call timeout 25 s;
  - fallback call timeout `min(12 s, remaining)`.
- App: `lib/features/review/data/repair_api.dart:26`, `receiveTimeout` 60 s (above the 40 s server deadline plus network).
- Web: `src/components/recovery/MistakeRepair.jsx:33`, an `AbortController` at 60 s.

**R3. Fewer, cheaper calls on the student path.**
- Use Structured Outputs (`response_format: { type: 'json_schema', json_schema: { strict: true, … } }`) in place of `json_object`.
  - This removes the same-model JSON retry (`providers.js:273-292`) for the repair.
  - Check first that `gpt-6-luna` supports it. The API lists it, but "not all reasoning models support every value".
- Take the blind check **off the student's wait**:
  - when the main call doubts the key, release the credit at once and answer `not_explained` with the reason `key_check_pending`;
  - run the blind check in `after()` from `next/server` (it runs inside the route's `maxDuration`), at `medium` effort with a 30 s timeout;
  - if it also disagrees, withhold the question as today. The student sees Key Review on the next open (the existing `question_under_review` path).
- When the blind check **agrees** with the key, store a flag. The next request for that mistake runs the explanation at `medium` effort instead of returning "No repair for this one".
- Student path: 1 call (2 with the fallback). Worst case booked drops from about $0.016 to about $0.003.

**R4. A fallback that can actually help.** This needs owner decision D2.
- On timeout, 5xx, network, rate-limit 429 or 400 (parameter), the fallback goes to a **different provider**: Claude Haiku 4.5 without thinking (`providers.js:187-219` already supports it).
  - Its price row was verified on 4 Oct, so it is usable until about 2 Jan 2027 (Q7).
  - The Anthropic key was valid locally at 22:30; the production key must be checked.
- On `insufficient_quota`, go straight to the fallback with no same-provider retry.
- Config: `AI_REPAIR_FALLBACK_PROVIDER` / `AI_REPAIR_FALLBACK_MODEL`, set in `src/services/recovery/mistakeRepair.js:37`.

**R5. Never keep a credit on failure, and give stuck ones back.**
- **One open repair per mistake.** In `mistakeRepair.js`, before reserving, look up `ai_credit_reservations` for `user_id` and `operation_key like 'repair:<id>:%'` with state `reserved` or `executing`.
  - Past `expires_at`: call `mm_ai_release_credits(key, 'expired')` and answer 409 `operation_released`. Web and app already restart with a new `requestId`.
  - Still live: answer 409 `in_progress` with `retryAfter: 5`.
  - This also blocks the double charge after a reload (rank 18).
- **A sweep** (no migration needed): a daily Vercel cron `/api/internal/release-expired` calling `mm_ai_release_expired(1000)`, added to `vercel.json` (Hobby allows daily crons).
  - Optional and better: a `pg_cron` job every 5 minutes. That is a production migration, so it needs the owner's explicit OK.
- **Shorter expiry for repairs:** an optional `p_ttl_seconds` on `mm_ai_mark_executing` (migration, owner OK). Use 180 s for repairs and keep 600 s for PrepOS.
- **Commit failure** (`mistakeRepair.js:112-115`):
  - retry the commit once;
  - also write the repair to the new `repair_records` table (P1) so a reopen is free;
  - say "charged: 0" only once the release has actually happened.
- **One-time return** of credits already stuck: `select public.mm_ai_release_expired(1000);`. This is a database write, so it waits for owner OK (D8). Q8 shows the count beforehand.

**R6. Make failures visible.**
- `providers.js:176-181`:
  - return `errorKind`: `timeout`, `quota`, `rate_limit`, `bad_request`, `auth`, `server`, `network`, `budget`, `price` or `guard_paused`;
  - write `{ error: kind, status, code, type }` into the failure receipt (no prompt text). Q4 can then group by it.
- `mistakeRepair.js`: on every failure, one `console.error(JSON.stringify({ route: 'repair', stage, kind, status, code, model, ms }))` with no student text. This is what the Vercel logs will show.

**R7. Clear, honest codes and messages, the same on web and app.**

| Situation | Code (HTTP) | Copy (web and app) | Credit |
|---|---|---|---|
| Deadline hit | `provider_timeout` (504) | "This one took too long. You weren't charged. Try again." The app must not say "offline". | released |
| Provider down, quota or rate | `provider_unavailable` (503) | "Repairs aren't available right now. You weren't charged. The book explanation is below." | released |
| Monthly student AI budget used | `budget_reached` (503) | "Repairs are paused until 1 November. You weren't charged." | released |
| Wallet or database hiccup | `wallet_unavailable` (503) | "We couldn't reach your credits. Nothing was charged. Try again." | none |
| Real gate pause only | `paused` (503) | "Repairs are paused right now. The key explanations still work." (drop "PrepOS" in this context) | none |
| Output failed checks | `unusable_output` (502) | "We couldn't write a reliable repair this time. You weren't charged. Try again." | released |
| Key in doubt | 200 `not_explained`, `reason: key_check_pending` | "We're double-checking this question's answer key, so there's no repair yet. You weren't charged." | released |
| Still running | `in_progress` (409, `retryAfter`) | "Still writing this one." The client checks again once, by itself, after `retryAfter`. | held, then committed or released |

Files:
- Server: `mistakeRepair.js`.
- Web: `MistakeRepair.jsx:39-55`, `data/repair_presentation.mjs:3-6`.
  - Reset the `requestId` whenever a failure body says `charged: 0`, which removes the wasted 409 click.
- App: `lib/features/review/data/repair_run.dart:252-271`.
  - Only the real `paused` and the 402 switch the run to key-only. The new codes map to `OutcomeFailed`.
  - Also `repair_state.dart:5-20` (add `slow`, `serviceDown` and `budget`), `copy.dart:184-196` and `widgets/mistake_view.dart:160-176`.
  - Check `ApiErrorKind.timeout` before `isOffline`.

**R8. Validation that does not reject good teaching.**
- `data/mistake_repair.js:14`: ban only promises. Keep "you will score/gain", "marks you will gain/recover", "guaranteed marks/score/selection/rank", "your rank will", "your percentile will" and "admission chance". Drop the bare words `rank`, `percentile`, `guarantee` and `you will get`.
- Tests: "Spearman's rank correlation", "the Constitution guarantees", "you will get x = 3".
- `interpretRepair` (`:69-78`): cut over-long text instead of rejecting it; require only the core fields (see 5.3); keep the key-agreement rule.

**R9. Web UI truth fixes** (`src/components/recovery/MistakeRepair.jsx`).
- Replace the timer-driven fake stages (`:13-14,66-70`) with one honest working state.
- Fix the mojibake and remove the middle-dot meta strings (`:141,145`). Write, for example, "1 credit used. 7 left."
- Show "Open your repair (free)" instead of "1 credit" when a repair is stored. The result payload can carry a `repaired` flag per question from `/api/me/repair-record`.

**R10. App flow fixes.**
- After `in_progress`, poll once by itself after `retryAfter` (`repair_run.dart:93`).
- Use key-only mode only for a real pause or a 402 (`:208-211`).
- Map a timeout to "This one took too long", not "offline" (`mistake_view.dart:161-168`).

---

## 5. "Complete" Mistake Repair: Score Recovery worth a credit

### 5.1 What the credit should buy

A student spending a credit should leave with four things:
1. a clear name for the trap they fell into;
2. the idea explained in a way the book did not;
3. one rule they can say back;
4. proof on a fresh question that it held.

The free parts stay free: the key, the book explanation, the marks this answer cost, and the record. Everything obeys the truth rules:
- no predicted scores, no "gain", no rank or percentile;
- no claims about the student's mind ("This option is a 'partly true' trap", not "you rushed");
- success only after the server acknowledges it (`src/services/prepos/replyDeps.js:18-22`; owner UI standards, section 7).

### 5.2 Options weighed

| Option | Value to the student | Cost per repair | Risk | Recommendation |
|---|---|---|---|---|
| **The trap named** (a fixed list of about 10 types plus a one-line "why it looked right") | High: a name makes it recognisable next time | in the same call | Low, if worded about the option and not the student | **P0, paid** |
| **Explained another way, with a worked contrast** ("If the question asked X, B would be right. It asks Y, so C.") | Highest: the part the book cannot give | same call, about 150 more output tokens | Medium: needs the passage and book explanation as grounding | **P0, paid** |
| **A one-line rule to remember** (15 words or fewer) | High: carried into Holds and the record | same call | Low | **P0, paid** |
| **Marks-at-stake line** ("This answer cost 6 marks in this session: 5 not earned and 1 penalty.") | Medium: makes the stake concrete | none (deterministic, CUET +5/−1) | None if past tense and from the record | **P0, free** |
| **2 to 3 fresh similar questions right after** (Checked) | High: the real path to not repeating it | none (bank questions, no AI) | Supply per chapter and concept; must never show the key first; must be labelled as ordinary practice while `RELEASE_GATES.content` is false | **P1, free** (D6, D7) |
| **Pattern across this student's mistakes** (same trap, same chapter, "you also missed this exact question in Mock 3") | High, and personal | none | Needs stored trap types; small samples stated as small | **P1, free** |
| **"Explain it another way" on demand** (simpler, with an example; optionally Hinglish) | Medium to high | about $0.0008 | Low | **P1, one included per repair** (D4, D9) |
| **Spaced review (Holds)**: one unseen question at +2 and +7 days, with a reminder | High: the "repair that holds" promise | none | Supply; reminders must be the student's choice | **P2, free** |
| **Shared cache per (question, chosen option, prompt version)** | Instant, consistent, no failures for repeats | saves calls | The cached text must be personalised only by free deterministic lines | **P1** (pricing D4) |
| Generated new practice questions by AI | Looks rich | high, plus quality risk | Breaks the content contract ("never publish generated cards", `replyDeps.js:23`) | **Do not do** |

### 5.3 Repair v2: one call, richer and grounded

Prompt input:
- the question;
- the **passage**;
- options in served order;
- the student's option;
- the key;
- the **book explanation** marked as evidence;
- the subject and chapter.

The prompt is versioned (`REPAIR_PROMPT_VERSION = 2`, stored in the receipt).

Strict JSON output:

| Field | Limit | Required |
|---|---|---|
| `solved_index`, `key_check` (`agree` or `doubt`) | — | yes |
| `trap_type` | one of `partly_true`, `reversed`, `look_alike_term`, `missed_not_except`, `not_in_passage`, `calculation_slip`, `wrong_rule`, `one_step_short`, `extreme_word`, `assertion_reason_link`, `other` | yes |
| `trap` | 30 words: why this option looks right (about the option) | yes |
| `why_wrong` | 40 words | yes |
| `another_way` | 70 words, simpler than the book, not a restatement | yes |
| `contrast` | 50 words: a worked "if X then B; here Y, so C", or the step where B's number comes from | no |
| `rule` | 15 words, imperative | yes |
| `next_step` | 25 words, pointing at the fresh check | no |

The old v1 fields still render for stored repairs. The app model makes the new fields optional (`lib/core/models/repair.dart:14-20,77-94`).

Cost: about 600 to 2,500 input tokens (with a passage) plus about 1,500 output tokens at `low` effort, so about $0.001 per repair. Even 10,000 repairs a month is about $10. The USD 25 IST-month cap stays as it is; it is shared with PrepOS, Rival and moderation (Q6), so watch it.

### 5.4 Free versus paid

| Free | Paid (1 credit) |
|---|---|
| Your pick and the key, the book explanation | The trap named and why it tempted |
| "This answer cost 6 marks in this session" | Where it breaks |
| "You also missed this question in <paper> on <date>" | The idea explained another way, with a worked contrast |
| Pattern across repaired mistakes (once trap types exist) | The rule to keep, and the next 10 minutes |
| Fresh check right after (Checked), and the +2/+7 day checks (Holds) | One "explain it another way" |
| Reopening any stored repair | |
| Every failure, every key doubt, every held question | (never charged) |

### 5.5 The screen, the same on web and app

The paid part leads. Once explained, the question folds to one line ("Q7. Your pick B. Key C.") with "Show the question".

The order:
1. the trap name as the heading;
2. "Why B looked right" and "Where it breaks";
3. "Another way to see it", with the contrast;
4. the rule, given visual weight;
5. the free marks line;
6. the fresh check ("Check it on 2 new questions"), which lights Checked on the stage thread only after the server scores it.

The stage thread (Found, Repaired, Checked, Holds) stays on both surfaces. Under the owner's standards:
- no fake stages;
- no middle-dot meta strings;
- no AI badge;
- success only after acknowledgement.

### 5.6 Phased build list

**P0: reliability plus v2 content (both surfaces)**
- Server:
  - `data/mistake_repair.js` (R1 passage, R8 validation, v2 schema and prompt, NTA mapping in eligibility);
  - `data/answer_corrections.mjs`, `src/services/recovery/answerReviews.js` (NTA mapping);
  - `src/services/recovery/mistakeRepair.js` (R2 deadline, R3 dispute off the wait, R5 one open repair per mistake, R6 logging, R7 codes);
  - `src/services/ai/providers.js` (timeouts, error kinds, receipts, Structured Outputs, a cross-provider fallback after D2);
  - `src/app/api/recovery/repair/route.js` (`maxDuration`);
  - new `src/app/api/internal/release-expired/route.js` and `vercel.json` (daily sweep);
  - `data/repair_presentation.mjs` (retry policy; `marksAtStake()`).
- Tests: `data/tests/mistake_repair.test.mjs`, `data/tests/answer_corrections.test.mjs`, `data/tests/prepos_reservations.test.mjs` (stale release).
- Web: `src/components/recovery/MistakeRepair.jsx` and `mistake-repair.css` (v2 layout, honest loading, abort timeout, codes, mojibake); `src/components/recovery/KeyReviewNotice.jsx` (the "double-checking" copy); `src/components/ScoreRecoveryLab.jsx:180,196` copy.
- App:
  - `lib/core/models/repair.dart` (v2 fields optional);
  - `lib/features/review/data/repair_api.dart` (60 s);
  - `data/repair_run.dart` (error mapping, in-progress poll, key-only only on a real pause or 402);
  - `data/repair_state.dart`;
  - `widgets/outcome_views.dart` (v2 blocks);
  - `widgets/mistake_view.dart` (folded question, marks line);
  - `copy.dart`;
  - a Dart port of `marksAtStake`;
  - unit and golden tests under `test/`.
- Docs: `mockmob-next/docs/brain/APP-API-CONTRACT.md` section 2.9 (new codes and fields); `DESIGN.md`, "Score Recovery Lab".

**P1: Checked, patterns, explain again, cache (both surfaces)**
- Migration, which needs the owner's OK because it touches production AI and learning:
  - `repair_records`: `user_id`, `attempt_id`, `question_id`, `subject`, `chapter`, `chosen_index`, `key_index`, `trap_type`, `rule`, `prompt_version`, `model`, `created_at`;
  - `repair_checks`: `repair_id`, `question_id`, `kind` (`immediate` / `delayed`), `due_at`, `answered_index`, `correct`, `answered_at`;
  - `repair_explanations`: `question_id`, `content_hash`, `chosen_index`, `prompt_version`, `payload`, `created_at`.
- Server:
  - `src/app/api/recovery/repair/check/route.js`: GET returns 2 unseen live, undisputed questions of the same subject, chapter and concept (key withheld); POST is scored on the server;
  - selector in `data/db.js` or a new `src/lib/server/repairChecks.js`;
  - `src/lib/server/repairPattern.js` (counts by trap type and chapter, repeat-question detection, small-sample wording);
  - an explain-again variant in `mistakeRepair.js`;
  - `src/lib/server/repairRecord.js` reads `repair_records` and `repair_checks`, so `checkedState` becomes real.
- Web: a new `src/components/recovery/RepairCheck.jsx`; the pattern line and "Explain it another way" in `MistakeRepair.jsx`; Review record rows (`src/app/(app)/review`).
- App:
  - a new `lib/features/review/widgets/fresh_check_view.dart` and `data/repair_check_api.dart`;
  - the pattern line and explain-again in `outcome_views.dart`;
  - `screens/record_screen.dart` and `core/repositories/repair_local_repository.dart` merged with `GET /api/me/repair-record` (WEB-PARITY A12: the server wins on `repairedAt`).

**P2: Holds and trust**
- Holds: `repair_checks` with `kind='delayed'` at +2 and +7 days.
  - Shown in Today and Review on both surfaces: the web's Today/Review pages and the app's `features/today` and `features/review`.
  - An app reminder through the existing notification plan; on the web, a "check due" line.
- A cross-family blind check (a Claude model) in `after()`; a moderator dispute queue; and restoring questions withheld by the passage bug (Q11).
- Pre-warming the shared cache for the most-missed (question, option) pairs, within the USD 25 month and with owner OK.
- A paid evaluation of v2 on about 50 real mistakes across the launch subjects (passages, NTA, Accountancy numericals). It runs only through the runtime guard and after owner OK.

### 5.7 Decisions for the owner

| # | Decision | Recommendation |
|---|---|---|
| D1 | Vercel plan and fluid compute (3.5); allow `maxDuration = 90` for the repair route | Check now; yes to 90 |
| D2 | Allow a non-Luna **fallback** for repairs (this relaxes the 5 Oct "Luna only" rule, for failures only) | Claude Haiku 4.5 (priced row exists) |
| D3 | Move the blind check off the student's wait (`after()`), at `medium` effort | Yes |
| D4 | What 1 credit buys: v2 plus one "explain it another way"; and whether a cached repair still costs 1 credit | v2 plus one re-explain; cached costs the same (the value is the content) |
| D5 | Keep auto-withholding a question after two AI disagreements, or make it a soft flag for moderators. Review the Q11 list (passage-bug victims). | A soft flag until two model families disagree; restore wrongly withheld questions |
| D6 | Fresh checks from ordinary bank questions while `RELEASE_GATES.content` is false, labelled "a new question from this chapter" and free | Yes |
| D7 | What "Checked" means: both fresh questions right, or at least one | Both right; otherwise "Not yet", and the mistake stays open |
| D8 | Return credits stuck today (one database write), and schedule the sweep (daily cron now; `pg_cron` 5 min with a migration) | Yes, after Q8 |
| D9 | Explain-again styles, including a Hinglish option | Simpler and with an example now; Hinglish as an option |
| D10 | The USD 25 cap is shared with moderation, PrepOS and Rival. Is a per-feature share wanted? (Q6 first) | Watch Q6; add a share only if one feature starves the others |

---

## 6. Limits of this audit

- No production data was read. Every likelihood above is from code, and section 3 confirms it.
- No model was called. Luna's latency, and whether it accepts `reasoning_effort` `none`/`low`/`high` or Structured Outputs, are unknown. STATUS says live Luna was never verified.
- The Vercel plan, the fluid-compute setting and the production env (`OPENAI_API_KEY` project, `AI_REPAIR_MODEL`, `AI_LUNA_MODEL`, `PREPOS_MODEL_REPLIES_DISABLED`) were not seen.
- The NTA findings (rank 5 and the result-page note) are from code and have not been reproduced on a real shuffled attempt.
- Cost figures are reservation bounds and estimates from the price rows, not bills.
