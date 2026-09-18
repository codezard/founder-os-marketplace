---
name: company-values
description: "Mines the decision log for costly choices and turns them into behavioral values with hiring/firing implications. Use when the user mentions company values, culture, operating principles, a mission statement, how the team works, or what the company stands for — and at the first hire. Refuses poster words and values every company would claim."
---

# Company Values

Derives values from decisions the founder actually paid for, not aspirations. Inherits `founder-core/references/principles.md`.

**Owner role:** Founder-CEO
**Stage:** 5 — Grow Sustainably (or at first hire)

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: `founder/decision-log.md` (real decisions made so far). If it's thin, gather stories of hard trade-offs first.

## Inputs
Decision log, stories of hard trade-offs, what the founder refuses to do for money, who the ideal customer and teammate are.

## Process
1. **Mine the decision log** for moments where the founder chose the harder path; each becomes a candidate value. Values not backed by a costly decision are aspirations, not values.
2. **Reduce to 3–5.** Write each as a behavior ("We tell customers when our product isn't right for them"), not a noun ("Integrity").
3. **For each value, write:** what it looks like, what it does NOT look like, a real story, and how it shows up in hiring and firing.
4. **Define the Non-Negotiables** (things that get someone removed) separately from values.
5. **Embed:** hiring-scorecard competencies, onboarding day-1 reading, a quarterly review question.

## Outputs
`founder/23-values.md`.

## Utils
**Decision-log mining prompts.** **Behavior-phrasing patterns** (behavior, not noun). **Values-to-hiring mapping.**

## Gate
`Each value has a real story and a hiring/firing implication.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Poster words. More than 5. Values that every company would claim.

## Evals
- **Should fire:** "Help me define our company values." / "What's our culture?" / (about to make the first hire)
- **Should NOT fire:** "Write interview questions." (→ hiring-playbook) / "How do I run 1:1s?" (→ team-building)
- **Golden run checklist:** decision log mined; 3–5 behavioral (not noun) values; each with looks-like / not-like / story / hire-fire implication; non-negotiables separated; embedding points; `23-values.md` created; gate line emitted.
