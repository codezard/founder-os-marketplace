---
name: sop-builder
description: "Writes a standard operating procedure a new person can follow with almost no questions. Use when the user mentions an SOP, standard operating procedure, a runbook, a checklist for a task, documenting a process, or writing something down so someone else can do it. Produces numbered steps with a definition of done — never paragraph prose."
---

# SOP Builder

Captures a task walkthrough and turns it into a followable procedure. Inherits `founder-core/references/principles.md`.

**Owner role:** Founder-Operator
**Stage:** 4 — Processize

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: a walkthrough (recording transcript, screenshots, or the founder narrating), tools used, definition of done, failure modes. If missing, ask the founder to narrate the task once.

## Inputs
Task name, a walkthrough, tools used, definition of done, failure modes.

## Process
1. **Capture the narrated walkthrough**; ask clarifying questions about decision points and exceptions.
2. **Write the SOP in the fixed template:** Purpose, Trigger, Owner, Inputs, Steps (numbered, one action each, with screenshot placeholders), Decision points (if/then), Definition of Done, Common failures + fixes, Escalation rule, Time budget, Last reviewed.
3. **Add the QA checklist** a reviewer uses to verify the output.
4. **Set the review cadence** (quarterly or on every failure).
5. **Register it** in `founder/17-process-inventory.md` with stage = Documented, then rebuild the index:
   ```bash
   python founder-core/scripts/sop_index.py --sops-dir founder/sops
   ```

## Outputs
`founder/sops/<task-slug>.md` (uses the founder-core SOP template).

## Utils
**SOP template:** `founder-core/assets/templates/sop.md`. **Decision-point notation** (If X → do Y). **QA checklist template.** **SOP index generator:** `founder-core/scripts/sop_index.py`.

## Gate
`A new person completes the task from the SOP alone with ≤ 2 questions.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Paragraph prose instead of steps. Missing definition of done. SOPs that describe the ideal instead of the actual process.

## Evals
- **Should fire:** "Write an SOP for customer onboarding." / "Document this so my VA can do it." / "I need a runbook for month-end close."
- **Should NOT fire:** "Which tasks should I delegate?" (→ delegation-framework) / "Automate this." (→ automation-workflows)
- **Golden run checklist:** walkthrough captured with decision points; full template filled; numbered one-action steps; definition of done; failures + fixes; QA checklist; review cadence; registered + index rebuilt; `sops/<task>.md` created; gate line emitted.
