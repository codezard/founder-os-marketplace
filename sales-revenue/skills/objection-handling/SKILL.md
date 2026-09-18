---
name: objection-handling
description: "Classifies a sales objection and drafts live and written responses, then logs recurring objections to fix the offer, price, or page. Use when the user reports an objection — too expensive, no budget, 'we already use X', not now, 'I need to ask my boss', how to respond to a prospect — or after any sales-call debrief. Refuses reflexive discounting."
---

# Objection Handling

Turns objections into responses and, over time, into product/offer feedback. Inherits `founder-core/references/principles.md`.

**Owner role:** Founder-Seller
**Stage:** 3 — First Customers → Repeatable Sale

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: the objection verbatim, deal context, `founder/08-offer.md`, and proof available. No hard blocker — but pull the offer for reframes.

## Inputs
Objection verbatim, deal context, offer, proof available.

## Process
1. **Classify the objection:** Price, Timing, Trust, Authority, Need, Competitor, or Status quo.
2. **Apply the pattern:** Acknowledge → Isolate ("if that weren't an issue, would you move forward?") → Reframe with evidence → Confirm → Advance.
3. **Draft two responses:** one for live conversation (short, question-led) and one for written follow-up.
4. **Log the objection** in the Objection Library with a frequency count. When any objection appears **≥ 3 times**, feed it back to `offer-creation`, `pricing-strategy`, or the `landing-page` FAQ.

## Outputs
Response drafts inline + an appended entry in `founder/objection-library.md` (objection, type, count, best reframe, where it should be pre-empted).

## Utils
**Objection taxonomy** with 3 reframes each (Price, Timing, Trust, Authority, Need, Competitor, Status quo).
**Isolate-question bank:** "Besides X, is there anything else holding you back?" / "If we solved X, would you move forward this quarter?"
**Follow-up templates** per type.

## Gate
`No single objection type causing > 30% of losses.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Discounting as the default response to "too expensive". Arguing. Handling objections that were never actually raised.

## Evals
- **Should fire:** "The prospect said we're too expensive — what do I say?" / "They want to think about it." / "Debrief this sales call with me."
- **Should NOT fire:** "Write a cold outreach sequence." (→ cold-outreach) / "Should I lower my price?" (→ pricing-strategy for policy)
- **Golden run checklist:** objection classified; Acknowledge-Isolate-Reframe-Confirm-Advance applied; live + written drafts; logged with count; ≥3× objections routed upstream; `objection-library.md` appended; gate line emitted.
