---
name: unit-economics
description: "Computes per-customer economics — ARPA, LTV, CAC, payback, LTV:CAC — by channel with guardrail checks. Use when the user mentions unit economics, CAC, LTV, payback, margin, contribution margin, churn math, or whether the business is profitable per customer — and run before any paid-growth or hiring decision. Uses gross-margin-adjusted LTV, never revenue LTV."
---

# Unit Economics

Computes the numbers that decide whether growth is safe, per channel. Inherits `founder-core/references/metrics-glossary.md` (exact formulas) and `references/principles.md`.

**Owner role:** Founder-Finance
**Stage:** 3 — First Customers → Repeatable Sale

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: price and tiers (`09-pricing.md`), cost to serve per customer, acquisition spend by channel, and customer counts and churn by month. If churn has < 3 months of data, flag lifetime estimates as unreliable.

## Inputs
Price/tiers, cost to serve (hosting, tools, human time), acquisition spend by channel, customer counts and churn by month.

## Process
1. **Compute per customer:** ARPA, gross margin, monthly churn → lifetime, gross-margin-adjusted LTV, CAC by channel, payback months, LTV:CAC. Run:
   ```bash
   python founder-core/scripts/unit_econ.py founder/customers.csv
   ```
   (CSV: `customer_id, channel, arpa, monthly_churn, gross_margin, cac`.)
2. **Segment by ICP and channel;** find the profitable pockets and the leaks.
3. **Sensitivity:** what happens at +20% price, −25% churn, +50% CAC.
4. **Set the Guardrails:** payback ≤ 6 months, LTV:CAC ≥ 3, gross margin ≥ 60%.
5. **Recommend the one lever** with the highest impact this quarter.

## Outputs
`founder/19-unit-economics.md` + `founder/unit-economics.csv`.

## Utils
**Metric definitions:** the shared glossary — so every skill uses the same formulas. **Calculator:** `founder-core/scripts/unit_econ.py`. **Guardrail thresholds:** payback ≤ 6mo, LTV:CAC ≥ 3, GM ≥ 60%.

## Gate
`All three guardrails met on the primary channel.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
LTV on revenue instead of gross margin. Blended CAC hiding an unprofitable channel. Assuming churn from < 3 months of data.

## Evals
- **Should fire:** "What are my unit economics?" / "Is each customer profitable?" / "What's my CAC payback?"
- **Should NOT fire:** "Build a 3-year forecast." (→ financial-model) / "Should I raise money?" (→ fundraising)
- **Golden run checklist:** upstream read; per-customer metrics computed via script; segmented by channel; sensitivity at +20%/−25%/+50%; three guardrails checked; top lever named; `19-unit-economics.md` + CSV created; gate line emitted.
