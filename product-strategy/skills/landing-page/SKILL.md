---
name: landing-page
description: "Writes a single-goal landing page in the customer's own words using a proven skeleton. Use when the user mentions a landing page, website or homepage copy, a hero section, a waitlist or pre-order page — and run automatically right after validate-idea or offer-creation completes, because a page is the natural next step. Enforces one CTA and no jargon the customer never used."
---

# Landing Page

Drafts a conversion-focused page (v0 validation / v1 MVP / v2 growth) that leads with the outcome in the customer's words. Inherits `founder-core/references/writing-standards.md` (specificity, one-CTA, banned words, proof hierarchy).

**Owner role:** Founder-Marketer
**Stage:** 1 (v0) / 2 (v1) / 5 (v2)

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: `founder/04-competitive-matrix.md` (positioning), `founder/08-offer.md` (offer), `founder/evidence-ledger.csv` (customer language), and `founder/objection-library.md` if it exists. If the offer/positioning are missing, run `offer-creation` / `competitive-analysis` first.

## Inputs
Positioning statement, offer, customer language from the evidence ledger, and the stage (v0/v1/v2).

## Process
1. **Pick the single conversion goal**: deposit / trial / demo / email. One goal, one CTA type.
2. **Draft with the Page Skeleton:** Headline (outcome in customer words) → Sub (who it's for + how) → Proof (numbers, named quotes, "used by X professionals") → Problem agitation (3 bullets in their words) → How it works (3 steps) → Offer + price + guarantee → Objections FAQ (from the objection library) → Final CTA.
3. **Write 3 headline variants:** outcome-led, pain-led, contrarian.
4. **Produce copy as markdown**, and — if the stack is known — a single-file `landing/index.html` with no dependencies.
5. **Define the analytics events:** view, scroll-50%, CTA click, convert.

Pull every proof number and phrase from real evidence; no invented testimonials or logos. Follow the proof hierarchy: specific number > named quote > anonymous quote > adjective.

## Outputs
`founder/07-landing-page.md` (+ optional `founder/landing/index.html`).

## Utils
**Page Skeleton** (above). **Headline formulas:** outcome-led ("Ship X in Y without Z"), pain-led ("Stop losing N hours to …"), contrarian ("Everyone says … . Here's what actually works.").
**CTA verbs:** Start, Claim, Reserve, Book, Get. One verb, repeated.

## Gate
`v0 converts ≥ 3–5% of qualified visitors to the goal; v1 ≥ 2% to paid.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Feature lists above the fold. Jargon the customer never used in interviews. More than one CTA type. Banned words (see writing standards).

## Evals
- **Should fire:** "Write my landing page." / "I need a waitlist page for pre-orders." / (offer-creation just finished)
- **Should NOT fire:** "Write a 5-email welcome sequence." (→ email-campaigns) / "Draft LinkedIn posts." (→ social-media)
- **Golden run checklist:** upstream read; one goal/CTA; full skeleton drafted in customer words; 3 headline variants; proof sourced (no fabrication); analytics events; `07-landing-page.md` created; gate line emitted.
