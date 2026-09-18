---
name: fundraising
description: "Decides bootstrap vs raise, and if raising, sizes the round and plans the process with term-sheet literacy. Use when the user asks whether to raise, bootstrap vs VC, mentions investors, a term sheet, SAFE, valuation, dilution, angels, grants, or revenue-based financing. Defaults to bootstrapping and non-dilutive options; refuses raising before Stage 3."
---

# Fundraising

Makes the raise-or-not decision on the merits, then runs a disciplined process if the answer is Raise. Inherits `founder-core/references/principles.md` (A6 sustainable > fast, A8 one-way doors).

**Owner role:** Founder-CEO
**Stage:** 5 — Grow Sustainably

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` (founder goals: control, speed, exit).
- Upstream: `founder/20-financial-model.xlsx`, `founder/19-unit-economics.md`, market type, current traction. If the business is pre–Stage 3 gate, refuse to raise and explain why.

## Inputs
Financial model, unit economics, market type, founder goals, current traction.

## Process
1. **Raise-or-not decision.** Raise only if (a) the market is winner-take-most and speed decides, (b) capex precedes revenue, or (c) proven unit economics are capital-constrained. Otherwise recommend bootstrapping or non-dilutive options (revenue-based financing, grants, customer prepayments).
2. **If Raise:** size the round from the model (18–24 months to the next milestone + 20% buffer), state the milestone it buys, and pick the instrument (SAFE / convertible / priced).
3. **Build the investor list** (30–50), tiered by thesis fit, stage, check size, and portfolio conflicts; sequence outreach to create parallel conversations.
4. **Process design:** a 6–8 week sprint, a weekly update to all active investors, a data-room checklist.
5. **Term-sheet literacy:** explain valuation, option pool, liquidation preference, pro-rata, and board; flag founder-unfriendly terms; state plainly that this is not legal advice and a lawyer must review.

## Outputs
`founder/22-fundraising-decision.md` (+ investor list and data-room checklist if Raise).

## Utils
**Raise/bootstrap decision tree.** **Non-dilutive options guide.** **Investor-list schema.** **Data-room checklist.** **Term-sheet glossary.** **Weekly investor update template.**

## Gate
`Decision documented with the milestone the money buys — or an explicit bootstrapping plan.` End with `Gate: PASS/OPEN — because …`. On Raise, recommend `pitch-deck`.

## Anti-patterns
Raising because peers did. Raising before the Stage 3 gate. Taking the first term sheet without parallel options.

## Evals
- **Should fire:** "Should I raise or bootstrap?" / "What does this SAFE mean?" / "How much should I raise?"
- **Should NOT fire:** "Make the deck." (→ pitch-deck) / "Model my cash flow." (→ financial-model)
- **Golden run checklist:** Stage-3 gate checked; raise-or-not decision on the three criteria; non-dilutive options considered; if Raise: round sized to a milestone + instrument + tiered investor list + process + term-sheet literacy with legal caveat; `22-fundraising-decision.md` created; gate line emitted.
