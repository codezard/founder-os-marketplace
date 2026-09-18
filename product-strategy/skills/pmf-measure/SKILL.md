---
name: pmf-measure
description: "Measures real product-market fit from survey plus retention data, not vanity growth. Use when the user asks whether they have product-market fit, mentions PMF, retention, whether customers are happy, whether they should scale, the Sean Ellis test — and ALWAYS before the user spends money on growth or ads. Measure first; refuse to declare PMF from growth alone."
---

# PMF Measure

Answers "do we have product-market fit?" with the Sean Ellis score, cohort retention, and the real ICP hiding in the "very disappointed" segment. Inherits `founder-core/references/principles.md` (A4 revenue can't lie) and uses `founder-core/references/metrics-glossary.md` (PMF score, retention).

**Owner role:** Founder-Strategist
**Stage:** 3 — First Customers → Repeatable Sale

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: a customer list with usage/payment data (CSV) and survey access. If there are fewer than ~30 active customers, say the reading will be directional and proceed cautiously.

## Inputs
Customer list with usage/payment data (CSV: `customer_id, signup_date, active_date`), survey access.

## Process
1. **Run the PMF survey** to all active customers: the Sean Ellis question ("How would you feel if you could no longer use this?") + 4 follow-ups (who are you, main benefit, what would you use instead, how to improve).
2. **Compute:** % "very disappointed"; cohort retention curves (does the curve flatten?); organic/referral share of new customers; expansion vs. churn revenue. Run:
   ```bash
   python founder-core/scripts/retention.py founder/activity.csv --period week
   ```
   (CSV: `customer_id, signup_date, active_date`.)
3. **Segment the "very disappointed" cohort** — who they are, what they use it for, the words they use. That segment **is** the real ICP; update `references/icp-schema.md`-shaped record.
4. **Verdict: Strong / Emerging / Absent**, naming the one bottleneck (acquisition, activation, retention, or monetization).
5. **Recommend:** Absent → back to positioning/MVP; Emerging → narrow the ICP; Strong → unlock `marketing-plan` and `unit-economics`.

## Outputs
`founder/06-pmf-report.md` + an updated ICP record.

## Utils
**PMF thresholds:** ≥ 40% very disappointed = strong signal; 25–40% = emerging; < 25% = absent. A flattening retention curve (a stable floor > 0) is required alongside the score.
**Survey template** and **retention script** (`founder-core/scripts/retention.py`).

## Gate
`≥ 40% "very disappointed" AND a flattening retention curve.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Declaring PMF from growth or signups alone. Averaging across segments (hides the real ICP). Surveying churned users as if they were active.

## Evals
- **Should fire:** "Do we have product-market fit yet?" / "Should we pour money into ads now?" / "What's our retention like?"
- **Should NOT fire:** "Write a re-engagement email." (→ email-campaigns) / "How much should we charge?" (→ pricing-strategy)
- **Golden run checklist:** survey run; % very-disappointed computed; retention curve produced via script; very-disappointed segment profiled as ICP; Strong/Emerging/Absent verdict + bottleneck; `06-pmf-report.md` created; gate line emitted.
