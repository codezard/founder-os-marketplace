---
name: community-finder
description: "Maps the real-world and online watering holes where a target persona already gathers, and builds a named outreach seed list. Use when the user asks where their customers hang out, how to find their audience, which communities or forums serve a persona, who they should talk to, or right after an idea shortlist exists. Fire automatically once find-business-idea completes, for the top gap."
---

# Community Finder

Finds where the sufferers of a chosen gap already congregate and turns that into an entry plan plus a concrete seed list for validation. Inherits `founder-core/references/principles.md` and `references/writing-standards.md` (no fabrication rule is critical here).

**Owner role:** Founder-Researcher
**Stage:** 0 — Discover

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` first; adapt reach targets to available hours.
- Upstream: `founder/00-idea-shortlist.md` (for the wedge statement and persona). If absent, run `find-business-idea` first — do not invent a persona.

## Inputs
Wedge statement, persona, geography, language.

## Process
1. **Enumerate watering holes** across six types: professional associations; regulatory/portal forums; Slack/Discord/WhatsApp groups; subreddits and niche forums; LinkedIn groups and hashtags; conferences/meetups; newsletters/podcasts they consume.
2. **Profile each**: estimate size, activity (posts/week), gatekeeping (open/invite/paid), and whether selling is tolerated. Use the scoring rubric below.
3. **Identify 5–10 "lighthouse" individuals** — respected practitioners who publicly complain about the problem.
4. **Draft an entry plan**: how to contribute value for two weeks before asking for anything.
5. **Produce the outreach seed list**: 30 named/handle-identified people to contact in `validate-idea`.

When web search is available, use it to find and size communities. When it is not, say so explicitly and leave a clearly-marked gap for the founder to fill — never guess a name or a member count.

## Outputs
`founder/01-community-map.md` — a table of communities (type, size, activity, gatekeeping, sell-ok), the lighthouse list, the entry plan, and the 30-name seed list.

## Utils
**Community score = reach × relevance × permission-to-sell** (each 1–5). Prioritize high-relevance, sell-tolerant communities even if smaller.

**Search-query patterns** per platform (adapt the persona/job terms):
- Reddit: `site:reddit.com "<job>" "<pain phrase>"`
- LinkedIn: `"<role>" group OR hashtag "<industry>"`
- Forums: `"<software/portal name>" forum problems`
- Events: `"<industry>" conference OR meetup <year>`

## Gate
`≥ 500 reachable people across the map AND ≥ 30 named seeds.` End with `Gate: PASS/OPEN — because …`. On PASS, recommend `validate-idea`.

## Anti-patterns
Inventing community names or member counts. Recommending spam tactics or pitching before contributing value.

## Evals
- **Should fire:** "Where do compliance officers actually hang out online?" / "Who should I talk to about this idea?" / (just finished find-business-idea)
- **Should NOT fire:** "Write my LinkedIn launch post." (→ social-media) / "How big is this market?" (→ market-research)
- **Golden run checklist:** upstream shortlist read; six community types covered; each scored; ≥500 reachable; 5–10 lighthouses; 30-name seed list; sources cited or gaps flagged; `01-community-map.md` created; gate line emitted.
