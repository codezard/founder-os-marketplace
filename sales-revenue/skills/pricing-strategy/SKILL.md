---
name: pricing-strategy
description: "Prices to value, not cost, and designs Good/Better/Best tiers with staged increases. Use for any pricing question at any stage — how much to charge, pricing, price, tiers, freemium, subscription vs one-time, raising prices, discounts. Anchors to what the problem costs the customer per year and refuses cost-plus or 'cheaper than X' pricing."
---

# Pricing Strategy

Sets price from the value delivered, picks the value metric, and stages increases as evidence accrues. Inherits `founder-core/references/principles.md` (A6 sustainable) and uses `founder-core/references/metrics-glossary.md` (gross margin, payback).

**Owner role:** Founder-Seller / Founder-Finance
**Stage:** 2 (v0) / 5 (v2)

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: `founder/08-offer.md`, cost-to-deliver, competitor prices, and the customer's current spend on the workaround. If the offer is missing, run `offer-creation` first.

## Inputs
Offer, cost-to-deliver, competitor prices, customer's current workaround spend, stage.

## Process
1. **Anchor to value:** what does the problem cost the customer per year (time × rate + errors + risk)? Price at **10–20% of that**, never cost-plus.
2. **Choose the model by the value metric:** per seat, per usage, per outcome, or flat. Pick the one that grows as the customer's value grows.
3. **Design ≤ 3 tiers** (Good/Better/Best) with the **middle tier as the intended default**; the top tier exists to anchor.
4. **Stage rules:** v0 = founding-customer price (higher touch, lower price, locked 12 months, in exchange for testimonials + calls); v1 = list price; v2 = raise 20–40% for new customers once close rate > 40% or churn is unaffected.
5. **Define discount policy** (annual prepay only, no ad-hoc) and refund policy.
6. **Run the sensitivity script** over willingness-to-pay data if available:
   ```bash
   python founder-core/scripts/pricing_bands.py founder/wtp.csv
   ```

## Outputs
`founder/09-pricing.md` — model, tiers, rationale, discount/refund policy, and the next-review trigger.

## Utils
**Value-anchor calculator:** annual cost of the problem × 0.10–0.20.
**Tier template:** Good (core outcome) / Better (default: + speed/support) / Best (anchor: + done-for-you/SLA).
**Van Westendorp bands:** `founder-core/scripts/pricing_bands.py`.
**Price-increase email template** for v2 (grandfather existing customers).

## Gate
`Gross margin ≥ 60% at list price AND payback < 6 months at expected CAC.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Pricing to be "cheaper than X". Free tiers before PMF. Per-seat pricing for tools whose value doesn't scale with seats.

## Evals
- **Should fire:** "How much should I charge?" / "Should I do freemium or a subscription?" / "Is it time to raise prices?"
- **Should NOT fire:** "What should the offer include?" (→ offer-creation) / "Build my financial model." (→ financial-model)
- **Golden run checklist:** upstream read; value anchor computed; value-metric model chosen; ≤3 tiers with default middle; stage rule applied; discount/refund policy; margin ≥60% & payback <6mo checked; `09-pricing.md` created; gate line emitted.
