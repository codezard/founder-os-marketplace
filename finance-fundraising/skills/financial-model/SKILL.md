---
name: financial-model
description: "Builds a driver-based financial model with Base/Downside/Upside scenarios and a runway view. Use when the user mentions a financial model, projections, a forecast, runway, cash flow, a budget, how long until profitable, hiring-plan cost, or scenario planning. Refuses hockey-stick projections with no drivers and hard-coded output cells."
---

# Financial Model

Builds a model driven by assumptions, not guesses, that shows survival in the downside. Inherits `founder-core/references/metrics-glossary.md`.

**Owner role:** Founder-Finance
**Stage:** 5 — Grow Sustainably

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: `founder/19-unit-economics.md`, current MRR and cash, planned hires, planned spend, growth assumptions by channel. If unit economics are missing, run `unit-economics` first.

## Inputs
Unit economics, current MRR and cash, planned hires, planned spend, growth assumptions by channel.

## Process
1. **Build a driver-based model:** an inputs tab (drivers), a revenue tab (customers × ARPA by segment, churn, expansion), a cost tab (COGS, people, tools, marketing), and a cash tab (monthly, with runway). No hard-coded output cells.
2. **Three scenarios:** Base; Downside (growth −40%, churn +50%); Upside. The Downside must still show survival.
3. **Mark every assumption** with a confidence level and a date to revisit.
4. **Identify the cash-low point** and the trigger to act (cut, raise, or slow hiring) three months before it.
5. **Monthly actuals-vs-plan ritual;** update drivers, not outputs.

## Outputs
`founder/20-financial-model.xlsx` (formulas live, no hard-coded outputs) + a one-page summary.

## Utils
**Model skeleton** (xlsx layout: inputs/revenue/cost/cash tabs). **Scenario switches.** **Assumptions register** (value, confidence, revisit date). **Actuals import** routine.

## Gate
`Downside scenario shows ≥ 6 months runway or profitability.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Hockey sticks with no driver. Hard-coded numbers in output cells. Modeling 5 years when you can't see 2 quarters.

## Evals
- **Should fire:** "Build me a financial model." / "How long is my runway?" / "Forecast cash for the next 18 months."
- **Should NOT fire:** "What's my per-customer LTV?" (→ unit-economics) / "Make my investor deck." (→ pitch-deck)
- **Golden run checklist:** upstream read; driver-based tabs (inputs/revenue/cost/cash); Base/Downside/Upside with surviving downside; assumptions register w/ revisit dates; cash-low point + trigger; `20-financial-model.xlsx` + summary created; gate line emitted.
