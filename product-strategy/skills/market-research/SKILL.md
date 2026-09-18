---
name: market-research
description: "Sizes a market bottom-up and maps the buying process so the founder knows if the opportunity is big enough. Use when the user asks about market size, TAM, SAM, who buys this, industry trends, whether a market is growing, or requests market research — and run automatically right after validate-idea returns Go. Refuses top-down TAM hand-waving and uncited figures."
---

# Market Research

Sizes the reachable opportunity from the bottom up and maps who actually buys. Inherits `founder-core/references/principles.md` and the no-fabrication rule in `references/writing-standards.md`; uses metric definitions from `founder-core/references/metrics-glossary.md`.

**Owner role:** Founder-Strategist
**Stage:** 1 — Validate

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: `founder/02-validation-report.md` (persona, wedge) and any price hypothesis. If absent, run `validate-idea` first.

## Inputs
Persona, wedge, geography, price hypothesis.

## Process
1. **Bottom-up sizing only:** `(# of personas) × (% with the trigger) × (realistic annual price) = SAM`. Show the arithmetic. Cite every number's source, or mark it explicitly as an assumption.
2. **Map the buying process:** who feels the pain, who approves budget, who blocks, and how long the cycle is.
3. **Tailwinds / headwinds:** regulation, platform shifts, macro, labor cost.
4. **List 5 substitute behaviors** — what they do instead of buying anything. This is the real competition.
5. **State the "why now".**

Use web search when available to source the persona count and price comparables; when not, mark those cells as assumptions and leave them for the founder to confirm.

## Outputs
`founder/03-market-brief.md` — one page, plus an assumptions table (each row: figure, source or ASSUMPTION, confidence).

## Utils
**Bottom-up worksheet:** personas × trigger-rate × price, with a low/base/high column.
**Source-quality tiers:** government/regulator > industry body > vendor report > blog/forum. Prefer the highest tier available and label the tier used.
**Buyer map:** feeler → approver → blocker → cycle length.

## Gate
`SAM large enough that 1% share ≥ $1M ARR.` End with `Gate: PASS/OPEN — because …`. On PASS, recommend `competitive-analysis`.

## Anti-patterns
Top-down TAM slides ("if we get 1% of a $50B market"). Uncited figures presented as facts. Ignoring the "do nothing" substitute.

## Evals
- **Should fire:** "How big is this market?" / "What's my TAM/SAM?" / (validate-idea just returned Go)
- **Should NOT fire:** "Who are my competitors?" (→ competitive-analysis) / "Write my landing page." (→ landing-page)
- **Golden run checklist:** upstream read; bottom-up arithmetic shown; every figure sourced or marked assumption; buyer map; 5 substitutes; why-now; 1%-≥-$1M check; `03-market-brief.md` created; gate line emitted.
