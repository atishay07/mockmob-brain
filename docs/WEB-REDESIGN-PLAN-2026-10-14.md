# MockMob website experience redesign plan

Status: **PROPOSED, 14 October 2026.** Plan only: no code was changed to write it. Nothing here is authorized to build until the owner has answered the decisions marked **[OWNER DECISION Dn]** (ledger in section 12), or has said which defaults he accepts. Where this plan and a newer owner message conflict, the owner message wins.

Written for the owner and for the agents who will build it. Section 11 sizes the work for parallel agents with file ownership.

## 0. What this plan is built from

Read for this plan (all of it, line by line unless noted):

- The owner's notes, `docs/brain/WEBSITE-REDESIGN-NOTES-2026-10-13.md` (his 13 Oct, about 2:15 PM, words kept verbatim there). The same notes are echoed in the 13 Oct handoff digest (AI OS `handoffs/DIGEST-20261013.md`).
- `docs/brain/PLAN-2026-10-12-APP-AND-WEB-EXPERIENCE.md`, in particular sections 2 (one product, two surfaces, the 12 rules), 4 (interlinking), 5 (promoting the app), 6 (website UI upgrade), 8 (phases) and 9 (decisions).
- The app direction: `docs/brain/design-2026-10-13/BUILD-BRIEF.md` (Night Sheet, wins on conflicts inside the app), `WEB-PARITY.md`, `OWNER-FEEDBACK-1110.md`, and `docs/brain/PENDING-2026-10-14.md` and `HANDOVER-2026-10-13-NIGHT.md` for current state.
- The owner's UI standards: `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`.
- The live site code in `mockmob-web2` on branch `fix/web-state-home` (head 613235c, logo B): `src/components/NavBar.jsx`, `MobileDock.jsx`, `MemberDockAction.jsx`, `MarketingFooter.jsx`, `landing/VisitorHero.jsx`, `LandingActions.jsx`, `VisitorSync.jsx`, `AuthProvider.jsx`, `LearningNextAction.jsx`, `ai/RecordGlimpse.jsx`, `ai/useInsights.js`, `src/app/page.js`, `(app)/AppLayoutClient.jsx`, `(app)/today/page.jsx`, `(app)/dashboard/DashboardPageClient.jsx`, `lib/arenaNavigation.js`, `src/proxy.js`, `src/app/layout.js`, `src/app/visitor.css`, `data/visitor_state.mjs`, `data/capabilities.js`, `api/learning/plan/route.js`, `lib/server/learning.js`, plus `PRODUCT.md`.

Limits of this evidence, stated so nobody over-trusts it:

- **Code was read, the site was not run.** Every statement about what a visitor sees comes from reading source, not from a browser, and nothing was timed. "Slow" below is the owner's report plus a code reading of why it probably is; the first task in section 11 measures it before anything is changed.
- **The research PDF** (`MarkMob_Product_Research_and_UX_Specification`) was not found on the Desktop in this lane. The 12 Oct plan records that it was checked page by page and adds six reference screens (its pages 15 to 20: mobile home, result to repair, card anatomy, "Why this?", honest card states, evidence before wording). This plan relies on that plan's summary of it, not on the PDF itself.
- `brain.py search "website redesign"` did not return within two minutes in this lane, so the notes were found by direct file search. Nothing was missed that matters: the notes file was in this repo's `docs/brain` and is mirrored in the handoff digest.
- The branch `fix/web-state-home` is local only, was never checked in a browser at 375 px or 1024 px, and is **diverged from `origin/main`**: origin/main has two commits it lacks (04e99cf "App backend release", 4bf41b8 "finaliser pass"), which, judging by the file diff, carry the server modules (rhythm, usage, repair record, sample import, finaliser) this plan wants to reuse. Confirm the routes exist after combining. Any build starts by combining them (section 11, task W0.1).

## 1. What the owner said, and the plan in one page

| He said (13 Oct, 2:15 PM) | What it means | Plan answer |
| --- | --- | --- |
| A logged-in person still lands on the normal home page. "At least they should have a button somewhere to directly enter the Arena." It still says "Start Free Practice, Try 5 Questions". | The site does not act on who is visiting. | The state-aware home already built on `fix/web-state-home` is the base (it has the right idea, unverified in a browser). Make the member path the default and verify it. Section 4 and 7.1. |
| "Websites should understand the state ... free, paid, signed in, signed out, or first-time visitor." | Seven distinct visitor states, not two. | Section 4 defines them, maps them to the existing `data-visitor` mechanism and names the one gap (a signed-in student with no session yet). |
| The menu: "Free Mock Test, Cutoff Eligibility, Go to Home, Arena, and Something Else." First-time people do not understand "Arena". | The menu mixes jargon, duplicates and a catch-all, and the same labels serve everyone. | A new menu per state (section 5), plain labels, and the word "Arena" retired from visitor-facing copy. The app never uses the word: grep of `flutter_app/lib` finds no "Arena". |
| Profile loads, then Today: "Today itself is a bit slow ... Practice maybe should be shifted to the first section. Maybe, not sure if Today is not made more useful." | Today is the weakest first impression of the signed-in product. | Lead with Practice now (cheap, reversible); in parallel make Today fast and truly useful; then decide on evidence whether Today earns the first slot back. Section 6. |
| "We need to work on a lot of things on the website" (the redesign). | Bring the site in line with the app. | Night Sheet brand reuse (section 8), one navigation source for public and signed-in surfaces, one copy glossary (section 9), a phased build (section 11). |

The core move: **the site stops being a catalogue that treats everyone the same and becomes one product with four modes: a stranger gets a free try, a returning visitor gets a sign-in, a new member gets one first action, and an active member gets Practice.**

## 2. Baseline: what the site does today (from the code)

**Public header** (`NavBar.jsx`): five fixed links for everyone: Free mock test, Cutoff calculator, Your prep tools (an anchor into the home page, `/#your-prep`), CUET PYQs, Pricing. The right side shows "My Arena" (member) or "Log in" and "Start free" (guest), chosen by CSS from `<html data-visitor>`. The mobile sheet lists the same five links plus About, then Profile and Sign out. A signed-in student reading the sheet therefore sees marketing links, the word Arena and an account row, with no clear single destination. This matches the owner's list.

**Signed-in shell** (`(app)/AppLayoutClient.jsx`, `lib/arenaNavigation.js`): the sidebar has four groups (Study, Planning, Community, Account) holding Today, Practice, Learn (only when study content is on), Review, Explore, Saved, Progress, Radar, Compass, PrepOS, Ranks, Contribute, My uploads, Account: **13 or 14 destinations, flat**. Mobile gets a bottom bar of four (Today, Practice, Learn or Explore, Review) plus "More", which opens the full list as a sheet. The route called Practice is `/dashboard`, and the Arena entry constant is `ARENA_HREF = '/dashboard'`. Today is the first item in the list and the first tab.

**"Arena"** is the name of the signed-in area. It appears in 41 source files (many are component names and CSS classes). The visitor-facing strings include "My Arena" (nav), "Enter the Arena" and "Go to the Arena" (home, dock), "Open the Arena first when I visit mockmob.in" (home setting), "Open my Arena" (pricing), "Arena navigation" (sidebar label), and "across the Arena" (profile). **Nothing on the site says what the Arena is.** (The Feature tour card is titled "Practice" with the kicker "Arena" and no definition either.)

**Home page by state** (`data/visitor_state.mjs`, `VisitorHero.jsx`, `VisitorSync.jsx`): three kinds, new, returning, member, plus plan (free or pro), set before first paint from a localStorage hint and kept current by `VisitorSync`. Guests get the marketing hero with the five-question sample. Returning gets a "Welcome back" note and a Sign in action. Members get a welcome with first name, plan line, "Enter the Arena" (or "Resume your test" when a saved draft exists), a "Where to next" card, and an opt-in checkbox "Open the Arena first". The redirect only runs for a confirmed member who ticked that box, on a fresh visit to `/`. **It is off by default, so the owner's "enter directly" case is still not the default.** There is no state for "signed in but has not finished a session yet".

**Today** (`today/page.jsx`): an `ArenaHead` ("Your next useful step"), `LearningNextAction` (time chooser 10/20/30, the step, alternatives), `RecordGlimpse`, and a fixed sentence about provisional 2027 specs. What happens before it paints, by reading the code:

1. `AppLayoutClient` renders only a full-screen "Loading your session..." until `AuthProvider` reports `authenticated`. `AuthProvider` first calls Supabase `getSession` (allowed up to 12 s) and then `/api/auth/me` (up to 5 tries, 8 s timeout each). **No part of any Arena page, including Practice, appears before that finishes.**
2. Only then does Today mount and fetch `/api/learning/plan`. That handler (`lib/server/learning.js`) does a series of awaits: study preferences, all of the student's attempts (`Database.getAttempts`), learning episodes and active sessions, a pathway validation per episode, released pathways, and the study record. Parts run sequentially.
3. `RecordGlimpse` fetches `/api/prepos/insights` in parallel after mount.
4. Until the plan arrives the card shows a three-bar skeleton and a mascot line, "Getting your next step".

So the likely critical path is bundle, session check, `/api/auth/me`, then the plan call, in series. That is a hypothesis to measure (W0.2), not a finding. Profile "loading up details" before Today is the same auth step being felt twice.

**Look and system**: light theme is the default (since 5 Oct), type is Gabarito + Hanken Grotesk + Geist Mono, volt `#D2F000` as the action colour. The app is Night default (warm charcoal `#12110E`), Bricolage Grotesque + Hanken Grotesk, volt. Three CSS dialects exist on the site (the `.mm` marketing layer, the `.app-shell` Arena layer, and legacy dark Tailwind utilities in 19 files), per the 12 Oct plan. Several visible patterns the owner's standards forbid are in use: all-caps eyebrows and kickers (`ArenaHead` `.eyebrow`, `lp-kicker`, `vs-card__head`), numbered step badges ("01 · Answer", "1 Subject"), trailing arrow icons on button text, and a mono label style.

**State of related work, so this plan does not collide with it:** NTA mode is being fixed on `mockmob-hotfix` `fix/nta-mode` (out of scope here); the Flutter app is being edited right now in `mockmob-next/flutter_app` (do not touch); the state-aware home and the test-screen notices are in `mockmob-web2` `fix/web-state-home`.

## 3. Principles for this redesign

These apply to every item below. They come from the owner's notes, the 12 Oct plan rules, BUILD-BRIEF and the UI standards.

1. **One product, two surfaces.** The site and the app share names, order of tabs, vocabulary, tokens and tone. A student never relearns the product. (12 Oct plan, 2.2 and 3.2; owner note 3.)
2. **The site reads who is visiting and shows the right thing first.** Server HTML stays the same for everyone and the visitor attribute picks the version before first paint (the pattern already built, which also keeps pages cacheable and crawlable). Never wait for the auth check to show something sensible.
3. **One dominant action per screen**, per state. (Standards section 3.)
4. **Stable primary navigation, state-specific entry.** Signed-in tabs never move or disappear with state (students learn them once). What changes with state is the entry point, the empty states, the account strip and the single dominant action. The public header does vary by state, because the job differs.
5. **Plain words for first-timers.** A branded name is allowed only with a plain descriptor the first time it appears, in menus and on first use. No unexplained names.
6. **Fast before fancy.** Budget Android on patchy 4G is the device floor (PRODUCT.md). Shell and skeleton in about 1 s, data in about 1.5 s are the targets from the standards; they are targets to verify, not claims. Animation never masks a slow flow.
7. **Every feature stays reachable and marketed.** Restructure and re-craft; do not delete features to shorten pages (owner preference, 12 Oct plan rule 11). Demoting to a "More" or "Resources" disclosure is allowed; removal is not.
8. **Truth first.** No invented numbers, no success before acknowledgment, no testimonials or headcounts (PRODUCT.md). Illustrative demos stay labelled where a label prevents a wrong impression (see D8).
9. **The owner sees it before it replaces what he already uses.** Standards, section 11: show screenshots or a side preview and get his OK before replacing a visible UI. Each phase in section 11 has a review gate for this.
10. **Where the standards and the app brief disagree on look, the owner's newest instruction wins, then the project's design system, then the standards.** Known disagreements are in section 8.3 and D5, D6.

## 4. Visitor states

The owner named five (free, paid, signed in, signed out, first-time visitor). The experience needs seven, because "signed in" splits and one state overlays the rest.

| Id | State | How the site knows | Exists today? |
| --- | --- | --- | --- |
| S1 | **First-time visitor**: signed out, never signed in on this device | `data-visitor="new"` (no hint) | Yes |
| S2 | **Returning visitor**: signed out, signed in here before | `data-visitor="returning"` (hint says member, then signed out) | Yes |
| S3 | **New member**: signed in, no scored session yet (just signed up, or finished onboarding) | Needs a cheap signal. Proposal: add `started: true` to the stored hint once `/api/auth/me` or the plan returns any attempt, and expose `data-visitor-stage="first"` before it is true | **No (the one real gap)** |
| S4 | **Active free member**: signed in, free plan, has a session | `data-visitor="member"`, `data-visitor-plan="free"` | Yes |
| S5 | **Pro member**: signed in, paid | `data-visitor="member"`, `data-visitor-plan="pro"` | Yes |
| S6 | **Test in progress** (overlay on S3 to S5): an unfinished test is saved on this device | `useResumableTest` / `findResumableTest` (local drafts) | Yes |
| S7 | **Cannot reach MockMob** (overlay): signed in, but the check failed or timed out; the student is not signed out | `AuthProvider` status `unavailable`, falls back to the stored hint | Yes |

Rules that make the states safe:

- Hints hold no personal data (kind, plan, and the new stage flag only). Nothing private is rendered from a hint; private data waits for the confirmed session. A stale hint can show the member shell skeleton for a moment, then the visitor is sent to log in; that is acceptable and must be tested.
- Crawlers and anyone without storage get S1. The guest HTML is unchanged for SEO.
- A returning visitor whose hint is stale and who is actually still signed in (cookie alive) is promoted to S4 or S5 on the first confirmed check.
- "Free" and "Pro" are the entitlement the server confirms (`user.isPremium`, `premiumUntil`, `creditBalance`), never inferred client-side.

## 5. Information architecture and menu per visitor state

### 5.1 The name "Arena"  **[OWNER DECISION D1]**

The owner said first-time users do not understand it. The app does not use it. Three options:

- **Recommended: retire it in everything a visitor reads.** The signed-in landing is simply **Practice**. The area has no brand name: the logo is Home, the tabs are Practice, Today, Review. CTAs: "Start practice", "Continue practice", "Resume your test". Internal code names (`app-shell`, `ArenaHead`) can stay until the cleanup phase; user-visible strings change first. This matches the app.
- Keep the word and define it once ("Your practice room") in the menu descriptor and first-run. Costs a line of copy at every entry point and still needs a descriptor.
- Rename to something else ("Your prep", "My MockMob"). Only worth it if the owner wants a named room.

Everything in this plan assumes the recommended option. If he picks another, only the labels in the tables change.

### 5.2 Public header (marketing pages, SEO pages, pricing, tools)

Desktop shows at most five top-level items. Everything that exists today stays reachable, grouped.

| Item | S1 First-time | S2 Returning | S3 New member | S4 Free member | S5 Pro member |
| --- | --- | --- | --- | --- | --- |
| Left | Logo (links to Home) | same | same | same | same |
| 1 | Free mock test (`/cuet-mock-test-free`) | same | **Practice** (`/dashboard`, or first-check entry) | **Practice** | **Practice** |
| 2 | DU cutoffs and eligibility, a disclosure: Cutoff calculator, Subject combination planner, CUET 2027 guide | same | DU planning (same disclosure) | same | same |
| 3 | What you get (the loop and tools, `/#your-prep`; replaces "Your prep tools") | same | Review | Review | Review |
| 4 | Pricing | Pricing | Pricing | Pricing | *(hidden: Pro sees plan status in the account menu)* |
| 5 | Resources, a disclosure: Previous year questions, Online practice tests, English, Accountancy, Economics and Business Studies guides, About, Contact | same | same | same | same |
| Right | Log in (text), **Start free** (primary) | **Log in** (primary), Start free (text) | **Start your first check** (primary), account menu | **Continue practice** or **Resume your test** (primary), account menu | same as S4 |

Notes:

- The account menu (avatar, first letter if no photo) holds: Account, Plan and credits (S4) or Plan status (S5), Theme, Help, Sign out. It is the one place "Profile" and "Sign out" live; they leave the main list.
- "Go to Home" disappears: the logo is Home. "Something else" disappears: Resources is a labelled disclosure, never a catch-all.
- Member rows 1 and 3 intentionally mirror the signed-in tabs, so moving between a calculator page and Practice does not change the shape of the header.
- Every state-specific item pair is rendered and picked by the existing CSS classes (`vs-guest-only`, `vs-member-only`, plus new `vs-first-only` and `vs-pro-only`), as the current NavBar does, so there is no flash.
- **Mobile sheet:** same items in the same order, one flat list with the two disclosures expanded inline; the primary action sits in the thumb zone (the existing `MobileDock` pattern), and for members the dock shows Continue practice or Resume your test. The "Theme" row stays for very high zoom.
- **Open question for the owner [D12]:** whether Pricing stays top-level for free members or moves into the account menu only. Recommended: stays for S1 to S4 (free members are the buyers), hidden for S5.

### 5.3 Signed-in navigation (what used to be the Arena)

One list for all members, not varied by state (principle 4). Practice first, as the owner suggested. **[OWNER DECISION D3]**

| Level | Items | Where |
| --- | --- | --- |
| Primary (always visible) | **Practice**, **Today**, **Review**, **Learn** (only while study content is switched on, as now) | Desktop: top of sidebar, large. Mobile: bottom bar |
| Start action | **Start** opens a quick-start sheet: Resume (when a draft exists), Quick 10, Full mock, Repair the next mistake, NTA mode (Pro tag). Reuses the app's Start pattern (BUILD-BRIEF section 6) | Mobile: a button beside the bar. Desktop: a button in the header |
| Plan | Weak chapters, DU Compass, Subject combinations, Ask about your record | Sidebar group "Plan"; mobile: inside the account/More sheet |
| Study tools | Explore questions, Saved, Progress | Sidebar group, collapsed by default on desktop; mobile: More sheet |
| Community | Leaderboard, Contribute, My uploads | Behind a "More" disclosure on both |
| Account menu | Account, Plan and credits, Start page setting, Theme, Guide, Help, Sign out | Avatar at top right (replaces "More" as the home of account things) |

Naming of the feature names **[OWNER DECISION D10]**: the website calls them Radar, Compass, PrepOS; the app (WEB-PARITY section 2) calls the same things Insights, CUET tools and Ask. One product should have one set. Recommended: choose the plain names first-timers can read at a glance, keep the brand names as a second line of descriptor during a transition. For example "Weak chapters (Radar)", "DU Compass", "Ask about your record (PrepOS)". The owner decides the final names; whichever he picks is applied to both surfaces (the app side is outside this lane and goes on the app's list).

Free versus Pro in this shell:

- Free: the header chip shows practice credits as now; it links to Plan and credits, not straight to the pricing page. Upgrade entries appear in the account menu and at a locked feature (Smart practice, NTA mode, difficulty) with the reason written out. No upsell strips on tabs.
- Pro: a quiet "Pro" tag with the end date in the account menu; no upgrade UI anywhere; locked-feature tags disappear.

Moderation access stays as it is (moderator-only band and link).

### 5.4 Where each state lands, and what is dominant

| State | Opening `/` | First screen after | One dominant action |
| --- | --- | --- | --- |
| S1 | Marketing home | n/a | Try 5 questions (sample), secondary Start free |
| S2 | Marketing home with the existing Welcome back note | n/a | Log in, secondary Try 5 questions |
| S3 | Goes straight to Practice **[D2]** | Practice, day-one state | Start your 10-question check (the app's onboarding also ends on this check) |
| S4 | Goes straight to Practice **[D2]** | Practice | Resume (if S6), else the next step, else Start practice |
| S5 | Same as S4 | Practice | Same as S4 |
| S6 | Same, with "Pick up where you stopped" first | The saved test | Resume your test |
| S7 | Home keeps the hinted member panel, with a quiet "Can't reach MockMob. You are still signed in" line and Try again | n/a | Try again |

**D2: should a signed-in visit to the home page go straight to Practice by default?** **[OWNER DECISION D2]** The owner's words ("they still come to the website's normal home page instead of entering directly") say yes. Today it is a checkbox, off. Recommended: on by default for confirmed members, on a fresh visit only (typed address, bookmark, external link), never when they came from a MockMob page, with the existing `?home` override and a setting "Start on: Practice | Today | Home" in Account. Two ways to do it, the second needs a spike first:

1. Client redirect after the session is confirmed (what exists). Simple; costs a flash of the hinted member panel before the move.
2. Edge redirect in `src/proxy.js` when a valid Supabase session cookie is present. No flash. But `proxy.js` is deliberately a never-redirect layer (its comment says a slow Supabase call must not bounce a signed-in student), so this needs a short spike and a safe fallback (cookie present but session dead sends them to Practice, which shows login). Recommend doing 1 now and the spike in Phase 2.

## 6. Today: make it fast and genuinely useful, or lead with Practice

The owner offered both. The plan does both in order, and lets measurement decide the rest. **[OWNER DECISION D3]**

**Step 1, now (cheap, reversible): Practice leads.** Reorder the primary tabs and the landing to Practice first (section 5.3), as he suggested. Practice carries a compact next-step strip at the top (`LearningNextAction compact` already exists), so the plan is one glance away without being the gate to everything.

**Step 2: remove the waterfall.** Candidate fixes in order of expected payoff. All need measuring first (W0.2) and none ships without a before and after number.

1. **Do not block the shell on the auth check.** When the stored hint says member, render the real shell (header, tabs, page skeleton) immediately and keep private data empty until the session is confirmed; only a confirmed `unauthenticated` redirects to login. Replaces the full-screen "Loading your session..." for every Arena page, so Practice, Review and Profile are fast too, which is the feeling the owner described when he went Profile then Today.
2. **Speed up `/api/learning/plan`.** Run its independent queries in parallel (`Promise.all`), stop reading every attempt when a summary will do, and return the primary step first with the heavier parts (the study sequence, alternatives, weekly plan) on a second lazy call. Consider a short per-student server cache with explicit invalidation on a new attempt.
3. **Keep the last plan on screen.** Store the last plan in a small client cache and show it immediately on return, marked with its age ("from 4 minutes ago") and refreshed in place. Truthful (age shown) and instant.
4. **Prefetch.** When Practice mounts for a member, fetch the plan once so Today opens with data.
5. **No layout shift.** Reserve the height of the plan card; the skeleton matches the final shape.
6. **Lazy secondary content.** `RecordGlimpse` loads after the plan, below the fold, and never competes with it.

**Targets (from the standards; verify, do not assume):** shell and skeleton about 1 s on a throttled 4G budget profile, plan data about 1.5 s at the 75th percentile, no CLS, no console errors.

**Step 3: make Today earn its place.** What Today should be, borrowing from the app's Today (BUILD-BRIEF section 12) and the plan's A1:

- One hero "Tonight's move": the single next step with a 10/20/30 minute chooser, a "Why this?" line with the real counts behind it ("Show me" opens the exact questions, section 8.2).
- Resume and check-due slots above it when valid.
- The week as seven marked days (from `/api/me/rhythm`, if it exists after the origin/main merge), and an unopened result takes over the hero.
- Day-one and return-after-days states designed: a new member sees "Start your first check", not an empty plan; return after three or more days asks "How long have you got tonight?".
- Remove the standing sentence "2027 exam specifications remain provisional..." from the page body; it moves to the footer and to the place a date is actually shown (D8). The mascot line above the plan goes unless it carries a real state (error or empty).
- A real "days to CUET" or road only with owner-confirmed dates (**[OWNER DECISION D19]**: the app is waiting on the same answer, PENDING-2026-10-14 item b3; until then use the app's wording "expected May 2027 window" and the board dates in BUILD-BRIEF section 8).

**The decision rule for Today's position [D3]:** after Step 2 and Step 3, if plan data is ready within the target and members open Today and then start the step it offers, promote Today back to first. If not, it stays second and the app's order (Today, Practice, Review) is revisited for the app too. Without any analytics the "members open Today" half cannot be measured; that needs the first-party event table decision [D14]. Until then the rule is speed plus the owner's own use.

## 7. Page-by-page changes

Priority: **P0** first build, **P1** next, **P2** later. Size: S about half a day, M about a day, L two days or more for one builder. Owner-decision items are marked.

### 7.1 Global

| Item | Change | Pri | Size | Notes |
| --- | --- | --- | --- | --- |
| One navigation source | A single module (`src/lib/navigation.js`) defines every item, label, descriptor, href and which states see it. `NavBar`, `MobileDock`, the Arena sidebar, the Arena bottom bar, the More sheet and the footer read from it. Replaces `arenaNavigation.js` and the hard-coded `LINKS` array | P0 | M | Single owner of the shell files (section 11) |
| Header and sheet by state | Section 5.2 and 5.3 | P0 | M to L | D1, D3, D10, D12 |
| Retire "Arena" in visitor copy | A copy inventory first (W0.3), then change every user-facing string and `aria-label` | P0 | S | D1 |
| Account menu | Avatar menu replacing "Profile" and "Sign out" rows and the Arena "More" account row | P0 | M | |
| Resume chip | While a draft exists (S6) a small "Resume, 23 min left" chip in the header on every page | P1 | S | Reuses `useResumableTest` |
| Footer | State-aware: members see Practice links first; guests unchanged. "App" entry added only after the Play listing is live (D13) | P1 | S | |
| Notices system | Section 10 | P0 | M | |
| Auth gate | Shell renders from the hint; no full-screen loading for members (section 6, fix 1) | P0 | M | Highest-leverage speed change. Needs careful tests: stale hint, dead session, slow network |

### 7.2 Home `/`

| Item | Change | Pri | Size | Notes |
| --- | --- | --- | --- | --- |
| Member path | Default straight to Practice for confirmed members **[D2]**; the existing member panel remains for S7 and for people who open Home on purpose; the "Open the Arena first" checkbox becomes the Account setting "Start on" | P0 | S | Logic exists in `shouldEnterArena`; make the default on and rename |
| First-time member | New hero state for S3: "Start your 10-question check" | P0 | S | Needs the S3 flag |
| Guest hero | Keep the five-question sample, the kinetic headline moment and the DU calculator link (owner keepers) | P0 | n/a | No change this phase |
| Remove forbidden patterns | Eyebrows and kickers, numbered badges ("01 · Answer"), pill labels that read as eyebrows | P1 | S | Standards section 4. Owner OK needed since he sees it [D7] |
| Restructure around the loop | The 12 Oct plan section 6.1 order: hero + sample, the loop (Find, Repair, Prove), tour grouped by job, one DU block, app band, truthful counters, creators, pricing, FAQ. Shorter on phones | P1 | L | Already owner-approved in direction (12 Oct, D3 there). Visual replacement still needs the owner's screenshot OK |
| Pricing section by state | Already state-aware (free member: Go Pro; Pro: none). Keep. Price copy follows `publicOffer()` | P1 | S | D15: monthly plan ID still not live |
| App band | After the Play listing is live only; Android browsers only; dismissible; never an interstitial | P2 | S | D13 |

### 7.3 Practice `/dashboard` (the member landing)

| Item | Change | Pri | Size | Notes |
| --- | --- | --- | --- | --- |
| Lead with the next step | Compact next-step strip on top (S4/S5), "Start your 10-question check" (S3), "Resume your test" (S6) | P0 | M | One dominant action |
| Setup | Keep Subject, Mode, Questions; remove numbered badges; show the cost and time before Start as the app does ("10 questions, about 10 minutes. 10 credits."); free members see credits, Pro sees "included" | P0 | M | Cost on the confirm line (BUILD-BRIEF section 8) |
| Access panel | Free: credits and what Pro adds, once. Pro: "Your access" with the end date. No repeated pitch | P1 | S | |
| "Feed the bank" | Moves to Contribute (More). Not on the landing | P1 | S | D11 |
| Recent sessions | Keep; add the plain verdict and the Review link; denominators everywhere ("6 of 15 answered") | P1 | S | Standards section 2 |
| Concepts shelf (Learn) | A shelf of chapter lessons here when study content is on, hidden otherwise (as in the app) | P2 | M | |

### 7.4 Today

Section 6. P0 for the speed work (steps 1 and 2), P1 for the useful version (step 3). Size L in total.

### 7.5 Review, Progress, Radar (weak chapters), Compass, Ask (PrepOS), Saved, Explore, Learn

| Item | Change | Pri | Size | Notes |
| --- | --- | --- | --- | --- |
| Names and descriptors | Apply D10 in headings, menu and page titles | P1 | S | |
| Shared header pattern | One page-head component without the eyebrow (replaces `ArenaHead`'s `.eyebrow`) | P1 | S | |
| Honest states | Cold start, thin evidence, ready, unavailable, empty each designed (no wall of "unknown") | P1 | M each | Standards section 7; 12 Oct plan rule 3 |
| Vocabulary | Found, Repaired, Checked, Holds in Review (app words) vs "Find, Repair, Prove" on the home (owner-approved promise) **[D9]** | P1 | S | Must be one coherent set |
| Evidence tags | A quiet "Show me" under claims about the student, opening the questions behind them | P1 | M | From BUILD-BRIEF 12.1; the web already has the data (RecordGlimpse, Radar) |
| Legacy dialect migration | Screens still on the legacy dark Tailwind utilities (`/features`, Chart.js Radar, Moderation, Upload, parts of Saved and Explore, `pricing/prepos`) move to the shared components | P2 | L | Part of the one design system (12 Oct plan 6.4) |

### 7.6 Result

Keep the 4 Oct structure. P1: the honest ending (next ask inside the ending), "Report a problem" kept where the notices work put it, the practice-bank note on this page (done on `fix/web-state-home`), "Continue on your phone" only after the app exists (D13). The sealed-sheet reveal is the app's moment layer; on the web it stays P2 and optional (it would add weight on budget phones).

### 7.7 Account, Plan and credits, onboarding, login, signup

| Item | Change | Pri | Size | Notes |
| --- | --- | --- | --- | --- |
| Account | Start-on setting, plan and credits in one place (read-only facts), theme, edit subjects and name (parity gap listed in WEB-PARITY) | P1 | M | The owner noticed Profile loads details slowly; it benefits from the same shell fix |
| Onboarding | Light pass: same words as the app, ends on the first check. The app's two-minute "Your sheet" deck is **not** ported | P1 | M | **[D16]**: whether the in-app guide tour auto-starts once after signup |
| Login and signup | Brand pass (logo B, tokens), "Log in" for S2 first, safe `next` return. No change to the auth flow, which the owner confirmed works ("working fine, not an issue") | P1 | S | Do not touch the auth reliability work |
| Pricing | State-aware: S1/S2 show plans; S4 shows Go Pro; S5 shows plan status, not a pitch | P1 | S | D15 for the price line |

### 7.8 Public and SEO pages

The free calculator, combo planner, CUET 2027 guide, PYQs, mock-test-free, online practice tests, subject hubs, about, contact, legal.

| Item | Change | Pri | Size | Notes |
| --- | --- | --- | --- | --- |
| Shared header and mobile dock | From the one navigation source; for members the primary CTA becomes Continue practice, not Start free | P0 | S | A signed-in student on the calculator today sees "Start free" |
| Member-aware CTAs | The conversion rail at the end of articles shows Practice for members, Start free for guests (CSS toggle as elsewhere) | P1 | S | SEO HTML unchanged |
| Restyle to the brand | Tokens and type from the shared set; shared layout for legal pages (the 12 Oct plan notes they repeat theirs three times) | P2 | M | |
| Content | No change to the SEO substance in this plan | n/a | | |

### 7.9 Out of this plan

The test runner and NTA mode (owned by `fix/nta-mode`); question supply and the content gates; payments and the Razorpay plan ID; the Flutter app; push; any production data or deploy. Where the runner notices need to match the new notice rules, that is a hand-off to that lane, not a change here.

## 8. What to reuse from the app

### 8.1 Brand and tokens

Source of truth: `docs/brain/design-2026-10-13/BUILD-BRIEF.md` (Night Sheet), and `flutter_app/lib/core/theme` (read only; do not edit). What transfers to the web:

- **Colour roles** (BUILD-BRIEF section 3): Night ground `#12110E`, raised `#1B1A16` and `#25231E`, hairline `#312E27`, ink `#F4F0E6` and two greys; Daylight paper `#F3EFE6` and friends; volt `#D2F000` as the single action colour; the "wrong" surface. Use them as web CSS variables generated from one `shared/tokens.json` (the 12 Oct plan 4.6 and 6.4 call for exactly this; today `shared/tokens.css` has five variables). Lamp amber is environment light only, never a button or text colour.
- **Type** (section 4): Bricolage Grotesque for display and numbers, Hanken Grotesk for reading. The web uses Gabarito today. **[OWNER DECISION D5]** Adopt Bricolage on the web so the brand is one voice; verify the width axis through `next/font` before promising the condensed numerals the app uses (check with Context7 or the font's documentation at build time).
- **Theme default.** The app is Night by default; the web is Light by default since 5 Oct (an earlier 2 Oct decision was night-first, then the 5 Oct change). **[OWNER DECISION D5]** The recommendation: Night default for the signed-in product (to match the app), choice remembered per device, Light kept as the option, marketing pages follow the same choice. Both themes remain and both are tested.
- **Logo.** Logo B is on the web header and icons already (613235c, local). The owner may still pick A **[D17, existing decision b7]**; confirm before more brand assets are produced.
- **Mobi.** The web mascot code still says "Pip" (`PipActor`, `PipGuide`) while the brand name is Mobi (the 12 Oct plan notes `MOTION.md` should use Mobi). Rename in code and copy, keep the poses, show Mobi only at human moments (welcome, empty and error states, return after a gap) and never in a timed exam.

### 8.2 Components and patterns to port (as web components, not Flutter code)

| App pattern | Web form | Pri |
| --- | --- | --- |
| Split dock: three labelled tabs plus a Start circle, lit tile on the active tab, selection feedback | Mobile bottom bar with a Start button; lit tile slides with a short transform; no haptics on web unless `navigator.vibrate` is judged worth it (skip) | P1 |
| Start quick-start sheet (Resume, Quick 10, Full mock, Repair next mistake, NTA with Pro tag) | A sheet from the Start button on both mobile and desktop; cost written as what you get | P1 |
| Tonight's move hero, week of seven marks, sealed unopened result | Today, step 3 of section 6 | P1 |
| "Show me" evidence tags | Under every claim about the student | P1 |
| Found, Repaired, Checked, Holds threads | Review; vocabulary per D9 | P1 |
| First-run: end on the real check | Onboarding end and S3 landing | P1 |
| Time-aware greeting ("Late one tonight. Ten minutes, then sleep.") | Today and Practice greeting, first name, after 11 PM variant | P2 |
| Glass settings (Full, Lite, Off) with automatic downgrade | See 8.3: one `prefers-reduced-transparency` and a "Lite" default on mobile web | P1 |
| Return after 3 or more days: Mobi and "How long have you got tonight?" with 10/20/30 chips | Today | P2 |

### 8.3 Premium glass and motion, reconciled with the standards  **[OWNER DECISION D6]**

The owner wants a premium glass and motion feel (HIGH, Revolut, Fampay), and the memory note says no obvious disclaimers. The UI standards say: no glass blur on content cards (blur only for fixed or sticky chrome), no decorative gradients or glow, neutral charcoal rather than warm. The app brief is warmer and uses light fields and a lit edge. The two are reconcilable if the web follows this rule, which this plan adopts as the default and which the owner must confirm:

- **Glass only on chrome:** header, bottom bar and Start button, sheets, dialogs. Never on content cards. This is the same split the app brief uses (live glass on dock, Start, sheets; solid for reading surfaces), so there is no real conflict on glass.
- **Light and gradient only as environment** on the home hero and the first-run moment: a warm light field behind art, a functional scrim over images. No gradient text, no glow behind text, no neon on ordinary cards. This is the app brief's own rule.
- **Warm Night neutrals** (the app's `#12110E`) rather than standards' neutral `#181818`: the owner's "very ice cold" feedback on 13 Oct is newer than the standards (12 Oct) and wins, and he approved Night Sheet's warmth. Say so in the design notes so a reviewer does not flag it as the standards' "tinted near-black" slop item.
- **Motion:** the app's curves and durations (BUILD-BRIEF section 7), transform and opacity only, about 100 ms press, 150 to 220 ms state change, 220 to 350 ms result; at most one authored page-load moment; reduced motion replaces movement with an instant change or a short fade. No `transition: all`, no scale(0) entrances.
- **Cost on budget Android:** blur is only on fixed chrome, with a solid fallback under `prefers-reduced-transparency` and when a device test shows dropped frames. Measure on one real budget phone (the owner's) before calling it done.

## 9. Copy rules for the site

Voice: a sharp senior who has been through CUET. Short, specific, a little dry, in the student's words (BUILD-BRIEF section 8). One owner-approved line stays: *Find the marks you're losing. Repair the mistake. Prove it on fresh questions.*

Rules (they combine the app's copy rules, the standards and PRODUCT.md):

1. Sentence case everywhere. No all-caps eyebrows, kickers above headings, numbered badges ("01 / 02"), or a single accented word in a headline. No mono "label" costume.
2. Say what it is in plain words. A branded name needs a descriptor beside it in menus and on first use. No unexplained names (Arena, Radar, PrepOS, Compass, Mobi, Recovery Lab).
3. Buttons are verbs that name the action: "Start practice", "Continue practice", "Resume your test", "Try 5 questions", "Start free", "Log in". No "Get started", no arrows appended to button text (use a real icon inside the control if one is needed).
4. Costs are written as what you get, on the confirm line: "10 questions, about 10 minutes. 10 credits."
5. No emoji, no exclamation marks, 12-hour time ("11:42 PM"), tabular numerals in data, units and denominators next to numbers ("6 of 15 answered").
6. Real evidence, not hype: "You missed 4 of 9", never "Unlock your superpowers". Banned: Elevate, Seamless, Unleash, Next-gen, Game-changer, Delve.
7. No build talk in the product: no "staging", "gate", "evidence-certified", "released pathway", service names or codes.
8. Calm after a poor result with one next step; never celebrate a bad outcome. Celebrations only after the server acknowledges.
9. Never invented numbers, testimonials, student counts or headcounts. Counts come from the real stats routes.
10. Greet by first name when known; no "Welcome back" for someone who never signed in (the existing rule on `fix/web-state-home`; keep).
11. Defensive captions: see D8. Default is to remove repeated generic ones and keep labels that prevent a wrong impression (a demo is marked as a demo; a provisional date is marked at the date).
12. Title case is for proper nouns only (MockMob, CUET UG, DU). Subject names are sentence case ("Business studies" in running text; "Business Studies" is the published subject name, so keep official names where they are labels).

Starter glossary (a machine-readable copy lives next to the navigation source once built):

| Today | After (recommended) | Why |
| --- | --- | --- |
| Arena, My Arena, Enter the Arena | Practice, Continue practice | D1 |
| Go to Home, Something else | (removed) | The logo is Home; Resources is a labelled group |
| Your prep tools (nav) | What you get | Says what it is |
| CUET PYQs | Previous year questions (in Resources) | Spelled out |
| Cutoff calculator | DU cutoffs and eligibility | Says the job |
| Radar | Weak chapters (Radar) | D10 |
| PrepOS | Ask about your record (PrepOS) | D10 |
| Ranks | Leaderboard | Plain |
| Open the Arena first when I visit mockmob.in | Start on: Practice, Today or Home | A setting, not a sentence |

## 10. Notices ("contextual notices")

The owner asked for notices that follow the visitor's state. Today there are two mechanisms: the runner notice (a fixed toast for offline and submit-waiting, built on `fix/web-state-home`) and the practice-bank note on the result page. Everything else is an inline sentence in a page body, such as the provisional-specs line on Today.

Proposal: one small notice system, defined once, so the site is never noisy and never silent about something real.

- **One slot, one notice.** At most one notice visible at a time; a priority order decides which. It lives in the shell, never as a persistent strip at the top of a timed test (the always-on strip was removed for good reason).
- **Triggers are real state only**, never a timer or a guess: offline, submit waiting, a session about to expire, free credits at zero, Pro ending within a few days, a feature unavailable and why (for example NTA mode when no paper can be built: plain-language reason from the engine), a maintenance flag, and later "the app is on Play" (D13).
- **Each notice has a state key, a dismissal rule and a "why you see this".** A dismissed notice stays dismissed per device until its underlying state changes. Stored in `localStorage` with try/catch and safe defaults, as the standards require.
- **Never on first paint of a marketing page for a stranger.** Notices belong to members and to real failures.
- **Truth rules:** no success wording before acknowledgment; errors name a recovery action and keep the user's work; no stacked banners.
- **Where captions go instead:** generic legal and provisional lines move to the footer, About and the exact place a date or claim appears (D8).

Owner touches: the order of priority, and which of the website's current captions (`na__note` provisional-specs line, "Illustrative demos; your screens use your own practice", "Not an official PYQ or a scored diagnostic") are kept, moved or cut. **[D8]**

## 11. Phased build order for parallel agents

Rules for every phase:

- Work only in `mockmob-web2` on a new branch `feat/web-redesign`, created from `fix/web-state-home` after combining `origin/main` (task W0.1). **Do not touch `mockmob-next/flutter_app`, `mockmob-hotfix`, any production data, or deploy; no push.** A deploy needs the owner's spoken yes (owner policy). Security hotfixes follow the standing owner OK (12 Oct), separately.
- **Two writers never touch the same file.** Each package lists the files it owns; anything outside them is a request to the owner of that file.
- Each package: write the experience brief (job, outcome, data truth, states, persistence, feel, acceptance; standards section 1) before code, build every state with the feature (loading, empty, error, offline, success, return), and finish with the done check below.
- **Done check** (standards section 11, owner's own): click it for real with a real pointer and hit-test that nothing invisible covers controls; walk the journey in a real browser at 360 px, 375 px, 1024 px, 1366 x 650 and 1920 x 1080, in Light and Night; long real labels; keyboard and focus; reduced motion; no console errors; then run the slop list in standards section 10 against the screen. Report exactly what was exercised (a screenshot shows a composition, a fixture shows behaviour on supplied data; neither proves device performance).
- Model suggestions follow the owner's routing: Opus (high) for signature UI and motion, hard flows, auth-adjacent and integration work; Sonnet for research, inventories, ports and checklist reviews. The owner minds time, so most packages are small.
- Owner review gates are marked **GATE**: the agent produces before and after screenshots at the sizes above and waits for his OK before the change replaces something he already sees.

### Phase 0: ground truth and decisions (serial, small; start immediately)

| Id | Work | Owns | Size | Model |
| --- | --- | --- | --- | --- |
| W0.1 | Create `feat/web-redesign`: bring in `origin/main` (04e99cf, 4bf41b8) so `/api/me/rhythm` and the app backend routes exist; resolve conflicts; run the site's existing unit suites (`data/tests/*`, `npm test` as defined in `package.json`) and record the baseline. Nothing is rewritten | git state only | S | Sonnet |
| W0.2 | **Measure before changing.** Run locally against staging (never production; the emulator cannot reach production HTTPS on this PC anyway). Record: auth check duration, `/api/learning/plan` server timings, bundle size, LCP, INP, CLS for `/`, `/dashboard`, `/today`, `/profile` on a throttled slow-4G budget profile, signed in and signed out. Screenshot the state-aware home at 375 px and 1024 px (pending item 17 has never been done). Output: a short evidence file with numbers and screenshots | a new `docs/brain/WEB-BASELINE-*.md` in web2 | M | Sonnet |
| W0.3 | Copy inventory: every user-visible string for Arena, branded feature names, eyebrows and kickers, numbered badges, trailing-arrow buttons, defensive captions, with file and line. Output: a table the glossary and later packages use | a new docs file only | S | Sonnet |
| W0.4 | **Decision pack for the owner:** the ledger in section 12 with the recommended default for each, plus three static mock-ups (the guest, new-member and Pro headers and the mobile sheet) so he decides on pictures, not prose | a new docs file and a static HTML mock-up in `tmp/` | M | Opus |

Gate: the owner answers D1, D2, D3, D5, D6, D10 (the ones that change what Phase 1 builds). Everything else can follow.

### Phase 1: entry, menu, speed (parallel; five packages, no shared files)

| Id | Work | Owns | Depends | Size | Model |
| --- | --- | --- | --- | --- | --- |
| W1.1 | **Shell and navigation.** `src/lib/navigation.js` (single source), the public `NavBar`, `MobileDock`, `MemberDockAction`, `MarketingFooter`, the Arena shell's nav and bottom bar, the account menu, the Start sheet, **and the auth-gate change** (render from the hint, no full-screen loading for members, confirmed-unauthenticated redirects). Extract the nav out of `AppLayoutClient` into its own file as part of this | `src/components/NavBar.jsx`, `MobileDock.jsx`, `MemberDockAction.jsx`, `MarketingFooter.jsx`, `src/lib/arenaNavigation.js` (replaced), `src/app/(app)/AppLayoutClient.jsx`, new nav and account components, `visitor.css` additions | W0.1, D1, D3, D10, D12 | L | Opus |
| W1.2 | **Member entry.** Default straight to Practice for confirmed members, the S3 "first" flag in the hint and boot script, the S3 hero, the Account "Start on" setting, the proxy edge-redirect spike (report only, no change to `proxy.js`) | `data/visitor_state.mjs`, `data/tests/visitor_state.test.mjs`, `components/landing/VisitorHero.jsx`, `LandingActions.jsx`, `VisitorSync.jsx`, the Account preference UI in `(app)/profile` | W0.1, D2 | M | Opus |
| W1.3 | **Today speed.** Parallelise and trim `/api/learning/plan` (with unit tests that the plan result is identical before and after), lazy second call for heavy parts, client cache with age label, prefetch from Practice, fixed-height skeleton, lazy `RecordGlimpse` | `src/lib/server/learning.js`, `src/app/api/learning/plan/route.js`, `src/components/LearningNextAction.jsx`, `src/components/ai/RecordGlimpse.jsx`, `ai/useInsights.js`, `(app)/today/page.jsx` | W0.2 | M to L | Opus |
| W1.4 | **Practice first.** The Practice page leads with the state-specific dominant action, compact next-step strip, cost and time on the confirm line, the access panel by plan, remove numbered badges, move "Feed the bank" | `(app)/dashboard/DashboardPageClient.jsx` and its CSS | W1.3 for the strip (can stub), D3 | M | Opus |
| W1.5 | **Notices.** The notice slot, rules and tests; migrate the existing runner notice and result note onto it; move the provisional-specs line out of Today | new `src/components/notices/*`, new `data/notice_rules.mjs` and tests, `(app)/test/RunnerNotice.jsx` | W0.3, D8 | M | Sonnet (rules and tests), Opus review |

GATE after Phase 1: owner opens the real site locally on his phone and desktop in S1, S2, S4, S5 and S6 and says yes or sends changes. Phase 2 does not start without it.

### Phase 2: brand and system (one foundation package, then parallel surfaces)

| Id | Work | Owns | Depends | Size | Model |
| --- | --- | --- | --- | --- | --- |
| W2.1 | **Tokens, type, theme.** `shared/tokens.json` generating web CSS variables (and the Dart theme, which stays an app-lane job); Bricolage (D5) and the Night default and Light option; glass-on-chrome rules and the reduced-transparency fallback; button, input and state components with every state; remove eyebrows and trailing arrows at the component level | `shared/*`, `src/app/globals.css`, `marketing-theme.css`, `(app)/arena.css`, `(app)/arena-support.css`, `src/components/ui/*` | Phase 1 gate, D5, D6, D7 | L | Opus |
| W2.2 | Public and SEO pages on the new header and tokens; member-aware CTAs; shared layout for the legal pages | `src/app/{about,contact,privacy,terms,refunds,cuet*,features,pricing}/*`, `components/SeoContentPage.jsx` | W2.1 | M to L | Sonnet |
| W2.3 | Account, login, signup, onboarding on the brand; plan and credits; edit subjects and name | `src/app/{login,signup,onboarding}/*`, `(app)/profile/*` | W2.1 | M | Opus (login flow is auth-adjacent: no change to auth logic) |
| W2.4 | Review, Progress, Radar, Compass, Ask, Saved, Explore, Learn: new page head, names and descriptors, honest states, vocabulary (D9), legacy-dialect migration | `(app)/{review,progress,analytics,admission-compass,mentor,saved,explore,learn,leaderboard}/*` | W2.1, D9, D10 | L (split by two agents by directory) | Sonnet for the migration, Opus for the states |

GATE: screenshots at all sizes in both themes per surface before each replaces what exists.

### Phase 3: useful Today and the app's best ideas

| Id | Work | Owns | Depends | Size | Model |
| --- | --- | --- | --- | --- | --- |
| W3.1 | Today "Tonight's move": hero, week row from `/api/me/rhythm`, unopened-result takeover, day-one and return-after-days states, "Why this?" with "Show me" | `(app)/today/*`, new `components/today/*` | W1.3, W2.1, D19 | L | Opus |
| W3.2 | "Show me" evidence tags and the Found, Repaired, Checked, Holds threads in Review | Review components | W2.4 | M | Opus |
| W3.3 | Result ending and cross-links (next ask inside the ending); resume chip | `(app)/result/*`, header chip | W1.1 | M | Opus |
| W3.4 | Start sheet polish and the lit-tile bottom bar motion, measured on the budget phone | shell nav components | W1.1, W2.1 | M | Opus |

### Phase 4: landing restructure, app band, proof

| Id | Work | Owns | Depends | Size | Model |
| --- | --- | --- | --- | --- | --- |
| W4.1 | Home restructured around the loop (12 Oct plan 6.1), shorter on phones, one DU block, grouped tour; member and guest versions | `src/app/page.js`, `components/landing/*` | W2.1, owner GATE | L | Opus |
| W4.2 | App band, `/app` page, QR for desktop, Android-only prompt, `related_applications` in the manifest | `src/app/app/*`, `manifest.js`, a band component | Play listing live, D13 | M | Sonnet |
| W4.3 | Cleanup: delete orphaned components after confirming unused, split `TestPageClient.jsx` only if the NTA lane is idle (otherwise skip), rename Pip to Mobi in code | various | all | M | Sonnet |
| W4.4 | Proof: budget Android and TalkBack pass, 200% zoom, Web Vitals before and after, a written before and after table against W0.2 | evidence doc | all | M | Sonnet |

### Phase 5: measure and decide

First-party event table and consent (D14) so Practice-first versus Today-first can be settled on use, not opinion; experiments from the 12 Oct plan 8 (Phase 6 there): sample to next step, result ending, "Why this?" copy, and the IA test Practice, Improve, My Goal. Negative results are kept.

### Order summary

Phase 0 serial and short. Phase 1 has five agents in parallel; W1.1 and W1.2 share only the hint contract (W1.2 defines it first; W1.1 reads it). Phase 2 has one foundation agent, then three or four in parallel by directory. Phases 3 and 4 follow the gates. Realistic parallel width is four agents at a time; the owner's machine is memory-tight (emulator rule: 2 to 3 GB), so the heavy browser measurement tasks run one at a time.

## 12. Owner decision ledger

Every item that needs an owner answer, with the recommended default. "Blocks" says what cannot start without it. If he accepts all defaults, Phase 1 can start the same day.

| Id | Decision | Recommended default | Blocks |
| --- | --- | --- | --- |
| **D1** | Retire the name "Arena" in visitor-facing copy and name nothing in its place (section 5.1) | Yes. Practice is the landing; the logo is Home | W1.1, W0.3 follow-up, all copy |
| **D2** | Signed-in visit to `/` goes straight to Practice by default, with a "Start on" setting; edge redirect only after a spike | Yes, on by default for confirmed members on fresh visits | W1.2 |
| **D3** | Practice first in the signed-in tabs; Today second and kept only if it passes the speed target and proves useful (section 6) | Yes | W1.1, W1.4 |
| **D5** | Web look: theme default (Light today, Night in the app) and display typeface (Gabarito today, Bricolage in the app) | Night default for the signed-in product, Light as the option, Bricolage + Hanken on both surfaces | W2.1 |
| **D6** | The glass and light reconciliation in section 8.3 (glass on chrome only; light as environment only; warm Night neutrals override the standards' neutral charcoal) | Yes | W2.1 |
| **D7** | Review process: before and after screenshots per surface, owner OK before a visible UI is replaced (standards 11) | Yes, per surface, not per component | every GATE |
| **D8** | Which captions stay on the site: provisional-2027 line, "illustrative demos", "not an official PYQ or scored diagnostic", non-affiliation. The app removed its own and moved non-affiliation to About and the Play listing. PRODUCT.md still requires illustrative screens to be labelled | Keep a label only where it prevents a wrong impression; non-affiliation to About and footer; remove the rest | W1.5, copy |
| **D9** | Mistake vocabulary on both surfaces: the app's Found, Repaired, Checked, Holds, versus the owner-approved promise "Find, Repair, Prove" on the home | Keep the promise line as the marketing line; use Found, Repaired, Checked, Holds inside Review and in the app so the product reads one way | W2.4, W3.2 |
| **D10** | One set of feature names for site and app: Radar, Compass, PrepOS (site) versus Insights, CUET tools, Ask (app) | Plain name first, brand name as descriptor (section 5.3). The final names are his; the app list gets the same answer | W1.1, W2.4 |
| **D11** | Leaderboard, Contribute, My uploads, Rival (unreachable from the nav today), and the synthetic "practice rival" rows: keep under More, move, or retire. The app brief bans leaderboards | Keep under More; keep synthetic rows clearly labelled or move them to a separate benchmark view (the 12 Oct plan's open item) | W1.1 menu, W2.4 |
| **D12** | Pricing as a top-level header item for free members | Yes for S1 to S4, hidden for Pro | W1.1 |
| **D13** | When the website starts promoting the Android app (band, `/app`, "Continue on your phone", QR) | Only after the Play listing is live; Android browsers; dismissible; no interstitial | W4.2 |
| **D14** | First-party event table with consent wording (and DPDP under-18 handling by about 13 May 2027), needed to judge Today versus Practice on use | Approve a minimal table, no third-party SDK (existing open item) | Phase 5; the Today decision rule |
| **D15** | Price line: Rs 99 once through 31 Jul 2027 (live) versus Rs 99 a month (the owner's decision, plan ID not set) | Follow `publicOffer()`; switch everywhere at once when the plan ID goes live (existing item b11) | pricing and home copy |
| **D16** | The in-app guide tour: auto-start once after signup, or only from the Guide button | Auto-start once, skippable, never again; describes Practice, Today, Review in plain words (and replaces the current four-step tour, which points at Progress even though Progress is not in the mobile bottom bar) | W2.3 |
| **D17** | Logo A or B (existing item b7) | Stay on B, confirm before more brand assets | W2.1 |
| **D19** | Dates for the Today road and any countdown: CSAS end date and registration window (existing item b3) | Use "expected May 2027 window" until confirmed, as the app does | W3.1 |

Numbering skips D4 and D18 on purpose: D4 (merge Today into Practice instead of keeping both) was folded into D3 and D18 was dropped; they are not missing questions.

## 13. Risks

| Risk | Handling |
| --- | --- |
| A stale hint shows the member shell to someone who is no longer signed in | Hints carry no personal data; private data waits for the confirmed session; a test covers stale hint, dead session and slow network. The shell then redirects to login as today |
| Default redirect surprises a student who wanted the home page | Fresh visits only, never from a MockMob page, `?home` override, and a visible setting; the footer and Resources keep About reachable |
| Dropping "Arena" confuses existing students | Tabs and routes stay the same; only labels change, and the landing was already Practice |
| Auth-gate change hides a real failure | `unavailable` still shows the explicit "Can't reach MockMob" state; nothing renders private data from a hint |
| Speed work changes the plan a student sees | A unit test compares the old and new plan output for fixed fixtures; the client cache labels its age; the plan stays server-authoritative |
| Glass is heavy on budget Android | Blur only on fixed chrome, solid fallback, device test before done; measured in W0.2 and W4.4 |
| Branch is diverged and local only | W0.1 combines origin/main first; nothing is pushed; deploy needs the owner's yes |
| Terminology split with the app (D10) | Decide once, apply to both; until then do not rename in one place only |
| Redesign collides with live NTA and app work | Out-of-scope list in 7.9; files owned per package; no edits to `flutter_app` or the runner |
| No analytics, so "Today vs Practice" cannot be measured on use | Decide on speed and the owner's own use first; D14 for real measurement |
| The owner sees every change and iteration is slow | GATES are per surface, with side-by-side screenshots and a one-line change list; Phase 0 mock-ups let him decide on pictures |
| Premium look versus the standards | D6 settled once and written into the design notes so reviewers do not reopen it |
| Content not ready behind features that the menu now surfaces (Learn off, recovery not live) | Items only appear when their capability is on (`CAPABILITIES`, study flag); no whole screen saying "not available" |

## 14. Acceptance for the whole redesign

The redesign is done when, in a real browser and on the owner's phone, with Light and Night:

1. A stranger sees the free try, a returning visitor sees Log in first, and none of them sees the word Arena or a menu item they cannot explain.
2. A signed-in student typing mockmob.in lands on Practice (unless they chose otherwise), sees one dominant action for their state, and never sees a "Start free" pitch.
3. A new member sees "Start your first check", not an empty plan.
4. A Pro member sees no upgrade UI anywhere.
5. The header and tabs are the same shape on the calculator page and in Practice.
6. Practice, Review and Profile paint a shell and skeleton quickly with no full-screen loading, and Today's plan arrives within the measured target or Practice stays first.
7. Menus have at most five top-level public items and four primary signed-in tabs, and every previous feature is still reachable.
8. The brand matches the app (tokens, type, logo B, Mobi) and the copy glossary is applied.
9. W0.2's numbers exist before and after, with screenshots at 360 px, 375 px, 1024 px, 1366 x 650 and 1920 x 1080, both themes, reduced motion, 200% zoom, TalkBack on a budget phone, no console errors, and the slop list in the standards checked and clean.
10. The owner has said yes to the screenshots of each surface.

## 15. Where things are (for the agents)

- This plan: `C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\WEB-REDESIGN-PLAN-2026-10-14.md`
- Owner notes: `...\mockmob-next\docs\brain\WEBSITE-REDESIGN-NOTES-2026-10-13.md` (also copied in `mockmob-web2\docs\brain`)
- Earlier plan: `...\mockmob-next\docs\brain\PLAN-2026-10-12-APP-AND-WEB-EXPERIENCE.md`
- App design: `...\mockmob-next\docs\brain\design-2026-10-13\BUILD-BRIEF.md`, `WEB-PARITY.md`, `OWNER-FEEDBACK-1110.md`
- Pending list and handover: `...\docs\brain\PENDING-2026-10-14.md`, `HANDOVER-2026-10-13-NIGHT.md` (web item is number 16 and number 17 there)
- Site code: `C:\Users\atish\Desktop\mockmob copy\mockmob-web2` (branch `fix/web-state-home`, head 613235c, local only)
- Owner UI standards: `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`
- Logo B files: `mockmob-next\tmp\logo\final-B` (already applied to the web header and icons in 613235c)
