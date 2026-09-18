---
name: mvp-scoper
description: "Cuts a product idea down to the single paid outcome and a build plan sized to the founder's real hours. Use when the user mentions an MVP, asks what v1 should include, wants to scope something, asks for a build plan or minimum viable version, or starts listing features — challenge every feature against the paid outcome. Defaults to the most manual MVP customers will accept."
---

# MVP Scoper

Forces the first version down to what customers actually paid for, and no further. Inherits `founder-core/references/principles.md` (A3 build before polish, A9 constraints).

**Owner role:** Founder-Builder
**Stage:** 2 — MVP

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` (hours/week, budget, technical skill). The build plan must fit these.
- Upstream: `founder/02-validation-report.md` and `founder/04-competitive-matrix.md`. If absent, run `validate-idea` (and ideally `competitive-analysis`) first.

## Inputs
Validation report, positioning, constraints, and the promised outcome to the first customers.

## Process
1. **Restate the single outcome** the customer paid for. Everything not required to deliver it is out.
2. **Choose the MVP type:** concierge (manual) → Wizard of Oz (manual behind a UI) → single-feature tool → no-code assembly. Default to the leftmost that customers will accept.
3. **List every step** from signup to outcome. Tag each **Manual / Semi-automated / Must-build**. Build only "Must-build".
4. **Define the Time-to-Value target** and the one instrumentation event that proves it.
5. **Produce a build plan** sized to real hours (e.g. "8 weekends"), with a weekly deliverable and a demo checkpoint at the midpoint.
6. **Write the "Not Now" list** explicitly, each item with the condition that unlocks it.

## Outputs
`founder/05-mvp-spec.md` — outcome, MVP type, step table (with Manual/Semi/Must-build tags), build plan, and the Not-Now register.

## Utils
**MVP-type decision tree:** can you deliver the outcome by hand for the first 10 customers? → concierge. Do customers need a self-serve surface to trust it? → Wizard of Oz / single-feature. Is the value purely in connecting existing tools? → no-code.
**Step-table template:** step | who/what does it | Manual/Semi/Must-build | notes.
**Not-Now register:** item | why deferred | unlock condition.

## Gate
`Build plan ≤ 8 weeks at stated hours, and every built item traces to the paid outcome.` End with `Gate: PASS/OPEN — because …`. Recommend `first-customers` and `pricing-strategy` (v0) next.

## Anti-patterns
Auth, billing, dashboards, or admin panels in v1 unless customers literally can't get value without them. Building for hypothetical personas. Automating before doing it by hand.

## Evals
- **Should fire:** "What should be in v1?" / "Here's my 20-feature list for the MVP." / "Scope this build for me."
- **Should NOT fire:** "How do I get my first customers?" (→ first-customers) / "Automate this workflow." (→ automation-workflows)
- **Golden run checklist:** constraints + upstream read; single outcome restated; MVP type chosen (leftmost acceptable); step table tagged; TTV + instrumentation event; ≤8-week plan; Not-Now list; `05-mvp-spec.md` created; gate line emitted.
