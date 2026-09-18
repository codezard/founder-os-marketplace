---
name: delegation-framework
description: "Decides what to hand off and builds a delegation brief plus a trust ladder for each task. Use when the user mentions delegating, handing off work, a VA or virtual assistant, a contractor, what they should stop doing, trusting their team with something, or 'I do everything myself'. Refuses to delegate outcomes that have no SOP."
---

# Delegation Framework

Classifies tasks by transferability and consequence, then hands them off with clear authority and a trust ladder. Inherits `founder-core/references/principles.md` (A5).

**Owner role:** Founder-Operator
**Stage:** 4 — Processize

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` (risk tolerance).
- Upstream: `founder/17-process-inventory.md` and the candidate delegate's role/skill level. If no inventory, run `processize` first.

## Inputs
Process inventory, candidate delegate (role/skill level), founder's risk tolerance.

## Process
1. **Classify each candidate task** on the Delegation Matrix: (Founder-unique judgment vs. Transferable) × (High vs. Low consequence of error).
2. **Route by quadrant:** Transferable + Low → delegate fully now; Transferable + High → delegate with checkpoint review; Founder-unique → keep, but timebox.
3. **Write the Delegation Brief** per task: outcome, SOP link, authority level (Do & report / Do after approval / Recommend only), deadline, budget, definition of done, check-in cadence.
4. **Set the Trust Ladder:** week 1 review everything → week 3 review samples → week 6 review exceptions only, with explicit criteria to advance.
5. **Weekly 30-minute delegation review**; log what came back to the founder and why (feeds SOP fixes).

## Outputs
`founder/18-delegation-plan.md` + per-task briefs.

## Utils
**Delegation Matrix** (2×2). **Authority-level definitions.** **Brief template.** **Trust-ladder tracker.**

## Gate
`≥ 80% of delegated tasks stay delegated after 6 weeks.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Delegating outcomes without SOPs. Taking tasks back after one error instead of fixing the SOP. Micromanaging via constant check-ins.

## Evals
- **Should fire:** "What should I delegate to my VA?" / "I do everything myself and I'm stuck." / "How do I hand this off without it breaking?"
- **Should NOT fire:** "Write the SOP." (→ sop-builder) / "Should I hire a full employee?" (→ hiring-playbook)
- **Golden run checklist:** inventory read; each task placed on the matrix; quadrant routing; delegation brief per task with authority level; trust ladder with advance criteria; weekly review ritual; `18-delegation-plan.md` created; gate line emitted.
