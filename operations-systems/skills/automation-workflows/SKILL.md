---
name: automation-workflows
description: "Designs an automation for a process that already has an SOP and has run manually enough times to be stable. Use when the user mentions automating something, Zapier/Make/n8n, a webhook, scripting a task, integrating one tool with another, or stopping doing something manually. Refuses to automate a process without an SOP or fewer than ~10 manual runs."
---

# Automation Workflows

Automates stable, documented processes with proper failure handling. Inherits `founder-core/references/principles.md` (A5 automate a process you've run ten times).

**Owner role:** Founder-Builder / Ops
**Stage:** 4 — Processize

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` (budget, error tolerance).
- Upstream: the SOP (`founder/sops/<task>.md`) and confirmation it has run manually **≥ 10 times**. If not, refuse and route to `sop-builder` / more manual reps.

## Inputs
The SOP, tools involved and their API/integration availability, volume, error tolerance, budget.

## Process
1. **Confirm the SOP exists and has run manually ≥ 10 times.** If not, route to `sop-builder`.
2. **Map the SOP steps** to: Trigger → Fetch → Transform → Decide → Act → Notify → Log.
3. **Choose the layer:** no-code (Zapier/Make/n8n) for < 1k runs/month and simple logic; scripts/serverless for higher volume or complex transforms; an agentic step only where judgment is unavoidable, with human review.
4. **Design failure handling:** idempotency, retries, dead-letter notification, a weekly exceptions report.
5. **Build with a dry-run mode**; run in parallel with the manual process for one cycle; then cut over.
6. **Update the process inventory**; add a monitoring line (runs, failures, time saved).

## Outputs
`founder/automations/<slug>.md` (design) + any code/config files.

## Utils
**Layer decision tree** (no-code / script / agentic-with-review). **Workflow canvas template** (the 7 stages). **Failure-handling checklist.** **ROI calculator:** hours saved × rate − tool cost.

## Gate
`Zero silent failures for 30 days; manual fallback documented.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Automating an unstable process. Agentic automation without a review step on money or customer-facing actions.

## Evals
- **Should fire:** "Automate my invoicing with Zapier." / "Integrate my CRM with my email tool." / "Stop me doing this by hand every day."
- **Should NOT fire:** "Write the SOP first." (→ sop-builder) / "Who should I delegate this to?" (→ delegation-framework)
- **Golden run checklist:** SOP + ≥10 manual runs confirmed (or refused); 7-stage mapping; layer chosen with rationale; failure handling; dry-run + parallel cycle; inventory + monitoring updated; `automations/<slug>.md` created; gate line emitted.
