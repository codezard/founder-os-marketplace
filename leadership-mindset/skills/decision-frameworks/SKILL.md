---
name: decision-frameworks
description: "Classifies a decision as reversible or not and applies the fitting frame, then logs it with kill criteria. Use when the user says 'should I', asks for help deciding, pros and cons, a trade-off, that they're stuck between options, mentions a big decision, pivot-or-persevere, or a co-founder choice — any high-stakes fork. Stage-independent; always available."
---

# Decision Frameworks

Speeds up reversible decisions and slows down irreversible ones, then records the call. Inherits `founder-core/references/principles.md` (A8 two-way vs one-way doors).

**Owner role:** Founder (any hat)
**Stage:** Stage-independent (always on)

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: the decision itself, options, what's reversible, time pressure, information available, and what would change the founder's mind.

## Inputs
The decision, options, reversibility, time pressure, information available, what would change your mind.

## Process
1. **Classify:** Reversible (two-way door) → decide in < 1 day with 70% information. Irreversible (one-way door) → run the full process.
2. **Write the decision in one sentence** and the deadline.
3. **Generate a third option** — the false binary is the most common trap.
4. **Apply the fitting frame:** Expected value with ranges; Regret minimization (10-year view); Pre-mortem ("it's 12 months later and this failed — why?"); Inversion (what guarantees failure — avoid that); 10/10/10 (how will I feel in 10 min / 10 months / 10 years).
5. **Ask "what would I need to believe?"** for each option; identify the cheapest test of the key belief.
6. **Decide,** set the review date and the kill criteria, and log it.

## Outputs
Appended entry in `founder/decision-log.md` (uses `founder-core/assets/templates/decision-log-entry.md`): date, decision, options, frame used, reasoning, review date, outcome-to-be-filled.

## Utils
**Door classifier.** **Framework picker.** **Pre-mortem template.** **Decision-log schema.**

## Gate
`Decision logged with kill criteria.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Pro/con lists without weights. Deliberating on reversible decisions. Asking for more data when the real issue is fear.

## Evals
- **Should fire:** "Should I pivot or keep going?" / "Help me decide between these two options." / "I'm stuck on a big call."
- **Should NOT fire:** "What should I work on today?" (→ founder-productivity) / "Should I raise money?" (→ fundraising)
- **Golden run checklist:** door classified; decision in one sentence + deadline; third option generated; fitting frame applied; key belief + cheapest test; kill criteria + review date; `decision-log.md` appended; gate line emitted.
