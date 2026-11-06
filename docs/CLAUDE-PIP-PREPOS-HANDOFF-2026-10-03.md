# Pip intent and PrepOS refinement handoff — 3 October 2026

Continue in `C:\Users\atish\Desktop\mockmob copy\mockmob copy`. The owner asked to retain the
good animation while improving the meaning of the poses, refine the hero, advance PrepOS with
the existing API/wallet, and prepare this handoff. This is local work, not a deployment.
Read AGENTS.md, PRODUCT.md, DESIGN.md and docs/brain/README.md before further behavior changes.
The large dirty tree includes owner and earlier-agent work. Never reset, clean or bulk-revert.

## What changed and why

| Before | After | Why |
| --- | --- | --- |
| Overlapping old/new faces during a dissolve | One raster face, 140 ms opacity entry | Two visors and eye sets read as a grimace, not an expression change. |
| Winking chin-touch while reviewing; closed-eyed idle during pricing/demo | Newly generated open-eyed attentive pose | Reading and choosing need engaged presence, not confusion or sleep. |
| Character in the right gutter pointing farther right | Image and blink layer face inward together | A gesture now has a visible destination. Static/reduced-motion pointing also faces left. |
| Tiny positional adjustments swap the face | Under-18-pixel corrections retain the station expression | Ordinary scroll should not keep changing Pip's emotional state. Larger travel is neutral. |
| Arena mode choices imply feelings before any result | Still attentive setup, loading and recorded-session companions | Choosing NTA or Smart does not warrant worry or celebration. |
| Incorrect sample answer prompts an exaggerated gesture | Short attentive nod; correct answer keeps its hop | Support the learner without shaming a mistake. Keyboard answers trigger no mascot reaction. |
| Rotating hero slogans and creator reach in the first proof row | Fixed “CUET 2027. One mock. A clearer next step.” and the five-question sample | The actual practice sequence carries the promise. Creator reach remains in its own sourced section. |
| PrepOS plan with little supporting context | Record finding, observed session count, inspect-record and ask handoff | Students can inspect the observation behind a next move. Empty/unreadable records remain explicit. |
| Ask without an explicit free/paid decision | Your record (free) versus written guidance (one PrepOS credit) | An unknown free question cannot silently become a paid model call. |
| Unlabelled replies and fragile network retry | Source labels, cost receipt, fresh wallet, stable-request retry | Facts, optional guidance and service status are distinguishable; lost responses can be retried once. |
| Changing PrepOS sections destroys the current conversation | Ask stays mounted while hidden | A pending/ambiguous operation and its retry ID survive section changes. Account changes still remount the hub. |

Pip's original identity, existing artwork, PrepOS orb, paid entitlements, provider budget guard
and atomic credit RPCs remain. One new pose was sufficient; the owner's permission for many
images was not a requirement to create unused assets. There are no new dependencies.

## Expression and gesture contract

| Context | Pip | Meaning |
| --- | --- | --- |
| Hero arrival / closing departure | Greeting | Welcome, then see you in practice. |
| Large travel between stations | Attentive | Accompany the reader without inventing an emotion. |
| Lab replay / pricing / screen comparison | Attentive | Let the content lead; remain awake. |
| DU comparison and eligibility | Inward pointing | Direct attention to the source or subject controls. |
| Correct sample answer | Celebrating hop | Acknowledge a completed correct action. |
| Incorrect sample answer | Attentive nod | Continue with the explanation; no disappointment judgement. |
| Lab next-move peak | Existing once-per-page jump | The illustrative replay has reached one useful next move, not proven a real score gain. |
| Arena setup, loading, Review and recorded states | Still attentive | The server readout supplies the facts. |
| Loading/read failure | Existing encouraging pose where applicable | Support a service problem, never diagnose the student. |
| Timed answering | Absent | Keep answering focused in both skins. |

Closed-eyed `idle` and winking `thinking` remain in the asset library, but the main journey and
setup/reading defaults no longer use them. Further poses need a named state and intended meaning
before generation. Avoid random pose rotation, worry tied to a practice mode, and celebration
merely because an existing record was loaded.

## Source map

- Intent/rendering: `src/components/brand/{pipIntent.js,PipGuide.jsx,PipActor.jsx,Mascot.jsx,ArenaCompanion.jsx}`;
  `src/app/brand-pip.css`; `public/brand/mascot/{attentive.webp,manifest.json}`.
- Landing: `src/app/page.js`, `src/components/landing/{DemoDrill,ExamComparator}.jsx`.
- Quiet Arena companions: `src/app/(app)/dashboard/DashboardPageClient.jsx`,
  `src/app/(app)/test/TestPageClient.jsx`, `src/components/{LearningNextAction,RecoveryOverview}.jsx`,
  `src/components/ui/Skeleton.jsx`.
- PrepOS: `src/components/ai/{MockMobAIHub.jsx,prepos.css}`;
  `src/app/api/ai/mentor/chat/route.js`. New stored replies carry their source. The API's explicit
  `replyKind: 'record'` branch returns without a model call even when the paid release gate opens.
  Older clients without that field retain the existing guarded contract.
- Development fixtures: `src/app/preview/arena/ArenaPreviewClient.jsx`. `ai=live|network|failure`
  exercises fake model receipts only inside this labelled preview. No real provider, score or
  wallet mutation occurs. `network` loses a response after a simulated commit; the same request
  ID reads the one receipt. `wallet=down` stays unknown, not zero.
- Evidence: `scripts/design-audit/round6-{asset,verify}.mjs`,
  `scripts/learning/prepos-readiness.mjs`, `artifacts/round6/`.
- Image master and exact GPT prompt: `artifacts/round6/{pip-attentive-master.png,IMAGE-PROMPT.md}`.
  The available GPT image tool has no version selector; do not claim a confirmed Image 2.5 run.

## Verification actually performed

- Final local production build and ESLint passed. Build logs retain two existing OpenGraph
  image dimension warnings for string `width="235"` / `height="280"` in `opengraph-image.jsx`.
- **172 automated tests passed, zero failures:** recovery/pipeline/source adapters 17; learning,
  runtime guard, monthly billing, wallet/reservations/model replies and insights 74; question
  selection/integrity and DU 47; remaining contribution/feed/payment/Pip/completion contracts 34.
  Logs: `artifacts/round6/logs/{recovery,learning,questions-du,remaining-contracts,lint-final}.txt`.
- **147 browser report entries passed:** seven stations forward/reverse across 320, 390, 768,
  1280 widths in both themes; one face, no idle/thinking default, inward pointer matrix;
  reduced-motion static fallback; free record and paused paid states; live/failure/unknown-wallet
  fixtures; lost-after-commit retry, one charge and identical ID; free unknown question never
  billed; still keyboard answering; correct hop, supportive wrong-answer nod; real wheel reversal;
  quiet Arena companions with doubled root font size. `artifacts/round6/verification.json` and
  `logs/verification-final.txt`. This is not physical-device, screen-reader or live AI evidence.
- In-app browser: phone hero, free record answer, paid-preview availability and public live
  PrepOS entry inspected. The public live site still exposes the earlier “public guide / missions”
  interface. It is not evidence that this checkout's budget/reservation lifecycle is deployed.
- Read-only configured Supabase readiness at 17:15 UTC: wallet, ledger, reservations, runtime
  request and price tables answered. `runtime_ai_budget` was unavailable through the configured
  Data API (`PGRST205`); no available funding was verified; configured fast/smart prices were not
  verified. The code release gate remains false. Evidence: `artifacts/round6/prepos-readiness.json`.
  Table readability does not prove RPC correctness, applied migration history or concurrency.
- A sandboxed build stalled and was restarted with normal worker access. Early harness attempts
  used an overly short teardown delay, an ambiguous wallet selector, an imprecise focus label and
  an invisible-phone reaction expectation. Those logs remain. Event-based waits, scoped controls
  and returning Pip into view produced the passing full run. No preview reset/cache deletion.

Motion review decision: **Approve for the locally verified refinement.** The single-face fix is
at `PipActor.jsx:23` / `brand-pip.css:143`; inward mapping and small-correction stability are at
`PipGuide.jsx:86`. New animation is opacity/transform only, uses the established strong ease-out,
and respects reduced motion. Existing travel stops its RAF when settled. This decision does not
certify hardware performance or unrelated motion elsewhere in the dirty tree.

## Skills used for concrete decisions

Emil design engineering / animation review supplied the frequency and keyboard rules, single-face
entry and exact easing. Apple design supplied spatial mapping and interruption continuity; its
existing bounded glass header and reduced-transparency fallback remain. Scroll Craft supplied the
existing journey/one-peak/quiet-reading structure; this is a refinement of that approved grammar,
not a fresh template or engine rewrite. Frontend design and existing-project redesign supplied
specific sample-led hero copy and a quieter evidence/composer hierarchy. Mobile-native supplied
16-pixel input text, 44-pixel controls and phone-specific presence. GPT image generation supplied
only the missing attentive state. Supabase guidance was used for the read-only readiness check,
using its official [select documentation](https://supabase.com/docs/reference/javascript/select).
The earlier broad skill work remains recorded in ROUND5-NOTES.md. No unrelated email feature
or external message was introduced.

## Next steps, in order

1. Review this build's landing and PrepOS at `http://localhost:3010/`; the actual account remains
   gated. The fixture paths above show optional guidance behavior without spending credits.
2. For AI activation, first resolve why the configured funding table is unavailable. Verify the
   actual schema and RPC signatures against saved runtime/reservation migrations. Reservations
   are already readable: **do not blindly reapply the “NOT APPLIED” file**. Name staging and save
   dry-run/schema reports before any migration. Never migrate production implicitly.
3. Set verified current provider prices and an explicitly authorized bounded student-AI funding
   amount. This is separate from the educational content $2 calibration / $10 lifetime ceiling.
   A key being present is not funded permission. Run read-only wallet reconciliation and real
   multi-session staging reserve/retry/release/commit tests, including response loss after commit.
4. Only after those reports pass, enable `runtimeAi` and the required environment switches.
   Validate a real funded reply, history provenance, fresh balance and emergency pause. Keep
   record questions free; never substitute a guessed balance or unguarded provider call.
5. Physical Android/iPhone, screen-reader and actual browser text-zoom acceptance remain.
   Phone reload/closing a drawer during an ambiguous paid request needs a durable client retry
   affordance; the server key lifecycle remains safe, but this refinement only preserves the key
   across PrepOS section changes. Do not claim reload recovery has been tested.
6. Carry forward Round 5's authenticated staging submission/resume, premium NTA and sandbox
   billing/webhook gates. Those live operations were not repeated during this refinement.

Rollback: revert only the edits listed here from a reviewed patch/snapshot, not the whole dirty
tree. Keep existing generated assets and guarded service contracts. `attentive` can fall back to
`greeting` in the manifest if required. Preserve the explicit free-request guard and original
request ID when changing Ask UI. No production data or migrations changed in this round.

## Ready prompt for Claude

```text
Continue MockMob in C:\Users\atish\Desktop\mockmob copy\mockmob copy.
Read AGENTS.md, PRODUCT.md, DESIGN.md, docs/brain/README.md, STATUS.md,
CLAUDE-PIP-PREPOS-HANDOFF-2026-10-03.md and ROUND5-COMPLETION.md first.
The owner likes the motion and asked for thoughtful Pip action placement, a less generic
hero and more useful PrepOS. That refinement is implemented locally: attentive GPT-generated
pose, inward pointing, one face at a time, meaningful reactions, quiet Arena setup, fixed
sample-led hero and explicit free-record/optional-model PrepOS UI with stable retry and receipts.
172 tests, lint/build and 147 browser report entries passed; inspect artifacts/round6.
Preserve these changes and the owner dirty tree. Use only extremely light subagents if authorized.
Keep port 3010 dev output isolated from .next production builds; use npm.cmd on Windows.
Do not copy the old public live site's missions/claims into this checkout.
Paid AI is still closed for a concrete reason: runtime_ai_budget was unavailable via the
configured API (PGRST205), configured prices weren't verified, and real funding/concurrency
release evidence is missing. Existing wallet/reservation tables are readable. Audit actual
schema/RPCs and named staging first, save dry-run reports, establish explicitly funded runtime
budget and verified prices, reconcile credits and run real reserve/retry/release tests before
activation. Never bypass persistent provider budget guards or atomic wallet RPCs, migrate
production implicitly, spend educational content money outside the $2/$10 guard, invent
academic truth/score gains, or create fake personal scores. Improve ambiguous-request recovery
across reload/drawer closure next, preserving the same owner-bound request key. Verify physical
devices and screen reader, then complete the existing staging/payment gates. Record actual
evidence and unresolved limits in STATUS.md; never claim fixture behavior is live evidence.
```
