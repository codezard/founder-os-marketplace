---
name: competitive-analysis
description: "Maps direct, indirect, manual, and do-nothing competition, finds the positioning gap no one owns, and writes a one-breath positioning statement. Use when the user mentions competitors, alternatives to something, how their product is different, positioning, competitive landscape, or who else does this — and run automatically whenever a landing page or pitch deck is being drafted."
---

# Competitive Analysis

Finds the persona × job × price-point cell no competitor owns and turns it into positioning. Inherits `founder-core/references/principles.md` and `references/writing-standards.md`.

**Owner role:** Founder-Strategist
**Stage:** 1 — Validate

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: `founder/03-market-brief.md` and the wedge. If absent, run `market-research` first.

## Inputs
Wedge, market brief, list of known competitors (if any).

## Process
1. **Build the Competitor Matrix:** direct competitors, indirect tools, the manual workaround, and "do nothing".
2. **For each row capture:** price, target persona, core promise, distribution channel, top 3 complaints (mined from reviews/forums), and what they *structurally can't* do because of their business model.
3. **Find the Positioning Gap:** the persona × job × price-point cell no one owns.
4. **Write the positioning statement:** *For [persona] who [need], [product] is the [category] that [key benefit]. Unlike [alternative], we [differentiator — because of a structural reason].*
5. **Identify the moat type:** data, workflow lock-in, regulatory expertise, community, speed, or "difficulty" (the thing incumbents won't bother to learn).

Mine real reviews/forum threads (use web search when available) for the complaint column; never invent competitor prices or quotes — source or mark as assumption.

## Outputs
`founder/04-competitive-matrix.md` — the matrix plus the positioning statement and moat type.

## Utils
**Matrix columns:** competitor | type | price | persona | core promise | channel | top-3 complaints | structural blind spot.
**Review-mining queries:** `"<competitor>" review problems`, `"<competitor>" alternative`, `"<competitor>" vs`.
**Moat taxonomy:** data / workflow lock-in / regulatory / community / speed / difficulty.

## Gate
`A positioning statement the founder can say in one breath.` End with `Gate: PASS/OPEN — because …`. Recommend `offer-creation` and `landing-page` next.

## Anti-patterns
Feature checklists as differentiation. Claiming "no competitors" (that means "no market" or "haven't looked"). Copying a rival's positioning.

## Evals
- **Should fire:** "Who else does this and how am I different?" / "Help me position against <incumbent>." / (drafting a landing page)
- **Should NOT fire:** "How do I price against them?" (→ pricing-strategy) / "What's my market size?" (→ market-research)
- **Golden run checklist:** upstream read; 4-category matrix; complaints sourced; positioning gap named; one-breath positioning statement; moat type; `04-competitive-matrix.md` created; gate line emitted.
