---
name: web-restructure-rejected
description: 15 Oct 2026 ~13:15 IST - owner rejected the website restructure (Gate A) as a major regression; never simplify by cutting richness; his per-page verdicts and the logo decision
metadata:
  node_type: memory
  type: feedback
  originSessionId: cc0bf1af-4c1f-4097-81a5-97ba84470f41
  modified: 2026-10-15T07:49:34.132Z
---

On 15 Oct 2026 at about 13:15 IST, the owner reviewed the Gate A previews of the website restructure (branch web/ia-1015, never deployed). He called it "a huge regression", "so basic compared to what we had before", "looking like the old website we had in 2025", and "far, far from the expectations".

**Why it failed:** the plan read "confusing for a new student" as "cut it down". It did these things:
- trimmed the landing from about 12 sections to 7, removing the feature showcase, tour, scroll animations and flying Mobi, and adding a 15-subject grid;
- merged the navigation into 5 places with denser pages;
- rebuilt pages plainer.

What he wanted was everything made more advanced, more fluid and more premium. Clarity should come from guidance and better design, layered on top of what exists.

**His verdicts:**
- **Regressed, use the old version and improve it:**
  - landing (wants it "more advanced and better", with a feature showcase and scroll animation);
  - navigation ("Cluttering each page with more information is not the solution");
  - Practice ("previously it was such a beautiful UI");
  - leaderboard;
  - pricing typography;
  - the cutoff calculator (the "New" tag and the green line).
- **Same as before:** sign-up and login.
- **Keep:**
  - the onboarding;
  - Study day (refine it);
  - the guide;
  - the Start sheet ("good", but needs graphics, spacing and typography);
  - the You account part and the light/dark setting ("finally like");
  - the brand switch (Bricolage display font plus the 3D subject objects: "This looks good").
- **Today:** okay, but its dropdowns and controls aren't designed properly.
- **Logo:** remove the bolt mark and the old logo everywhere. Use only logo B, keeping the small dot with the wordmark.

**How to apply:**
- Never remove a section, animation, showcase or richer UI to "simplify". Compare every redesign against the previous version's richness, and flag any loss before showing it.
- Build owner-visible page design with Opus, not Sonnet. The Sonnet-built pages (Practice, Review, You, Pricing) and the Opus plan both missed his taste.
- Start from the live site (web/alive-1015) and port in only what he kept.
- Preview the landing before building on it.

See [[mockmob-design-direction]], [[features-over-retesting]], [[subagent-model-choice]].

**Third time, 18 Oct 2026, about 1:45 am:**
- The Today redesign (release 4) was called "a huge regression": clean, but not tangible, and without the information he needs. The Today before it "just needed refinement in terms of UI and functionality". This came after the 17 Oct result redesign ("not acceptable at all").
- His N1 words "replace the strip and the slider" were read as "rebuild the page". He meant: keep the structure and the information, and fix those two controls.
- **Rule:** refine; don't rebuild. Any replacement layout goes to him as a mock-up before it ships.
- **His other rules from that night:**
  - Nothing may look like a form; every surface leads to the next thing.
  - Night mode must stay subtle, not neon.
  - A changed animation must be at least as good as the old one.
- Ledger: docs/brain/OWNER-MASTER-LEDGER.md (see [[owner-master-ledger]]).
