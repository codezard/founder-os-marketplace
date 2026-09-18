---
name: copywriting
description: "Writes persuasive, specific marketing copy matched to the reader's awareness level and one desired action. Use when the user asks to write copy, a headline, tagline, ad copy, an email subject, a value proposition or CTA, or to make text more persuasive or rewrite it — any marketing-text drafting. Enforces the specificity rule and the banned-word list."
---

# Copywriting

Produces copy that leads with the customer's own words and one action. Inherits `founder-core/references/writing-standards.md` (specificity, banned words, one CTA, proof hierarchy).

**Owner role:** Founder-Marketer
**Stage:** 3 — First Customers → Repeatable Sale

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: `founder/evidence-ledger.csv` (customer language) and proof available. If no customer language exists, ask for it or pull from interviews — don't invent phrasing.

## Inputs
Asset type, audience awareness level, customer language from the evidence ledger, proof, one desired action.

## Process
1. **State the reader's awareness level** — unaware → problem-aware → solution-aware → product-aware → most-aware. It determines where the copy starts.
2. **Choose a framework:** PAS (problem-agitate-solve) for problem-aware; AIDA for cold; BAB (before-after-bridge) for case studies; 4U (useful/urgent/unique/ultra-specific) for headlines.
3. **Draft with the Specificity Rule:** every claim gets a number, a name, or a time.
4. **Run the Edit Pass:** cut adverbs, replace abstractions with concrete customer phrases, one idea per sentence, read-aloud test.
5. **Deliver 3 variants** with a note on what each tests.

## Outputs
Inline copy + an appended entry in `founder/copy-bank.md` (winning lines by asset type, read by email, social, ads).

## Utils
**Awareness-level guide** (start point per level). **Framework picker** (PAS/AIDA/BAB/4U). **Specificity checklist.** **Banned words** (see writing standards: revolutionary, seamless, leverage, unlock, empower, …). **Swipe structure, not swipe text** — reuse structures, never others' words.

## Gate
`Passes the Specificity checklist; a persona member understands the offer in 5 seconds.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Clever over clear. Reproducing others' copy. Claims without proof. Banned words.

## Evals
- **Should fire:** "Write a headline for this." / "Make this landing copy more persuasive." / "Rewrite this value prop."
- **Should NOT fire:** "Which channel should I use?" (→ marketing-plan) / "Plan my blog." (→ seo-content)
- **Golden run checklist:** customer language sourced; awareness level stated; framework chosen; specificity applied (numbers/names/times); edit pass; 3 variants with test notes; `copy-bank.md` appended; gate line emitted.
