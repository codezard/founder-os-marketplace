---
name: processize
description: "Inventories the founder's recurring work and sequences it through do → document → delegate → automate → delete. Use when the user says they're the bottleneck, have too much on their plate, want to systematize or make something repeatable, keep doing the same thing, or are moving from getting-customers to scaling. Refuses to automate before documenting."
---

# Processize

Turns a week of the founder's actual activity into a prioritized transfer plan. Inherits `founder-core/references/principles.md` (A5 processize before delegate).

**Owner role:** Founder-Operator
**Stage:** 4 — Processize

## Step 0 — Constraints & upstream
- Read `founder/constraints.md`.
- Upstream: a week of the founder's actual activities (time log or calendar export), the customer journey, and current tools. If there's no time log, ask for one before estimating.

## Inputs
A week of activities (time log/calendar export), customer journey, current tools.

## Process
1. **Inventory every recurring task** from the time log. Tag each: frequency, minutes, who could do it (only founder / trained human / software), revenue impact.
2. **Compute Founder Hours at Risk** — time spent on tasks a trained human or software could do.
3. **Sequence each task** with Do → Document → Delegate → Automate → Delete: mark its current stage and next stage.
4. **Prioritize the top 5** by (hours saved × ease of transfer).
5. **Hand each off:** to `sop-builder` (document), `delegation-framework` (hand off), or `automation-workflows` (software) — with the explicit condition that marks the handoff complete.

## Outputs
`founder/17-process-inventory.md` — the master register every ops skill updates.

## Utils
**Time-log template.** **Task-tagging schema:** frequency | minutes | who-could-do | revenue impact | current stage | next stage. **DDDAD sequencing rules.** **Prioritization formula:** hours saved × ease of transfer.

## Gate
`Founder operational hours down 50% within one quarter.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Automating before documenting. Delegating tasks that still change weekly.

## Evals
- **Should fire:** "I'm the bottleneck in everything." / "How do I systematize my business?" / "I keep doing the same manual tasks."
- **Should NOT fire:** "Write the SOP for onboarding." (→ sop-builder) / "Should I hire someone?" (→ hiring-playbook)
- **Golden run checklist:** time log ingested; every recurring task tagged; Founder Hours at Risk computed; DDDAD stage per task; top 5 prioritized; handoffs routed with completion conditions; `17-process-inventory.md` created; gate line emitted.
