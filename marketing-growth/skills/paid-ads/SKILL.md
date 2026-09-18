---
name: paid-ads
description: "Plans and runs paid acquisition with CPA/CPC ceilings derived from unit economics — but only after PMF and a converting page. Use when the user mentions running ads, Google/Meta/LinkedIn ads, paid acquisition, an ad budget, CPC, or retargeting. Precondition-gates the request: refuses ads before PMF ≥ Emerging and a landing page converting ≥ 2%, routing to the fix."
---

# Paid Ads

Runs a disciplined ad test bounded by the unit economics. Inherits `founder-core/references/principles.md` and the glossary (CAC, payback).

**Owner role:** Founder-Marketer / Growth
**Stage:** 5 — Grow Sustainably

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` (budget).
- Upstream: `founder/06-pmf-report.md` and `founder/19-unit-economics.md`, plus a landing page conversion rate.

## Process
1. **Precondition check (refuse if any fail):** PMF ≥ Emerging; landing page converts ≥ 2%; conversion tracking verified. On failure, refuse and route to `pmf-measure`, `landing-page`, or tracking setup.
2. **Compute the ceilings:**
   ```bash
   python founder-core/scripts/ads_math.py --arpa <A> --gross-margin <M> --target-payback 6 --landing-cvr <C> --variants 3
   ```
   Max CPA = target payback (months) × monthly gross profit/customer; Max CPC = Max CPA × landing conversion rate.
3. **Choose the platform by intent:** search for high-intent/problem-aware; social for demand-gen with strong creative; LinkedIn only when ACV > $5k.
4. **Build the test:** 1 campaign, 2–3 audiences, 3 creative angles (pain, outcome, proof), budget = 5× Max CPA per variant to reach significance.
5. **Weekly optimization loop:** kill below-threshold variants, scale winners 20%/week, refresh creative every 3 weeks.
6. **Add a retargeting layer** for page visitors and email non-converters.

## Outputs
`founder/16-paid-ads-plan.md` + a creative brief per angle.

## Utils
**CPA/CPC calculator:** `founder-core/scripts/ads_math.py`. **Creative brief template** (angle, hook, proof, CTA). **Weekly optimization checklist.** **Tracking QA checklist.**

## Gate
`Blended CAC payback < 6 months at ≥ $3k/month spend for 2 months.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Ads before PMF. Optimizing for clicks instead of conversions. Scaling budget before creative fatigue is understood.

## Evals
- **Should fire:** "Should I run Google Ads?" / "Set up a Meta ads test." / "Here's my ad budget — plan it."
- **Should NOT fire:** "Grow my LinkedIn organically." (→ social-media) / "Do we have PMF?" (→ pmf-measure)
- **Golden run checklist:** precondition check run (PMF/CVR/tracking); ceilings computed via script; platform by intent; 3-angle test at 5× Max CPA/variant; weekly loop; retargeting; `16-paid-ads-plan.md` created; gate line emitted (or refusal + route if preconditions fail).
