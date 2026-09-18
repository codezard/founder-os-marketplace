---
name: email-campaigns
description: "Designs lifecycle email — welcome, onboarding, sales, newsletter, win-back — with one goal per stage and trigger logic. Use when the user mentions an email sequence, newsletter, drip, onboarding emails, nurture, re-engagement, a welcome series, or lifecycle emails — and after a landing page or first customers exist. Plain-text-first, one CTA per email, never buys lists."
---

# Email Campaigns

Builds the core lifecycle sequences with clear triggers and exits. Inherits `founder-core/references/writing-standards.md` (plain-text-first, one CTA).

**Owner role:** Founder-Marketer
**Stage:** 4 — Processize

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: list segments, available product events, `founder/08-offer.md`, and tone. A landing page (`07`) or first customers (`11`) should exist so there's a list to email.

## Inputs
List segments, product events available, offer, tone, tool in use.

## Process
1. **Define lifecycle stages and one goal per stage:** Subscriber → Trial/Lead → Activated → Paying → Expanding → Churn-risk → Won-back.
2. **Build the core sequences:** Welcome (5 emails, 7 days); Onboarding (event-triggered, to first value); Sales (7 emails, objection-led); Weekly newsletter (one idea, one story, one CTA); Win-back (3 emails).
3. **Each email:** single purpose; subject + preview line written last; plain-text-first design; one CTA.
4. **Set triggers and exits** (someone who converts exits the sales sequence).
5. **Define metrics:** open (directional only), click, reply, conversion; weekly review.

## Outputs
`founder/14-email-sequences.md` — every email drafted with its trigger logic.

## Utils
**Sequence blueprints** (Welcome/Onboarding/Sales/Newsletter/Win-back). **Subject-line formulas.** **Deliverability checklist:** SPF/DKIM/DMARC, warmup, list hygiene. **Segment schema.**

## Gate
`Onboarding sequence lifts activation ≥ 15% vs. a no-sequence cohort.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Buying lists. Image-heavy templates. Sending without segment logic.

## Evals
- **Should fire:** "Write my onboarding email sequence." / "I need a win-back drip." / "Set up a welcome series."
- **Should NOT fire:** "Write one cold email." (→ cold-outreach) / "Plan my blog." (→ seo-content)
- **Golden run checklist:** lifecycle stages + one goal each; 5 core sequences drafted; one CTA/email; triggers + exits; deliverability checklist; metrics defined; `14-email-sequences.md` created; gate line emitted.
