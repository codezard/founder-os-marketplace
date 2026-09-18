---
name: find-business-idea
description: "Mines the founder's own career history for hard-to-copy, experience-gap business ideas and scores them. Use whenever the user says they want to start something, asks what to build, wants a side project that makes money, mentions a business idea, or just vents recurring work frustrations — even if they never ask for idea help. Fire proactively on career-frustration talk; do not wait to be asked."
---

# Find Business Idea

Turns the founder's lived experience into a scored shortlist of business ideas rooted in gaps only they can see clearly. Inherits `founder-core/references/principles.md` (esp. A1 experience gaps, A9 constraints) and `references/writing-standards.md`.

**Owner role:** Founder-Researcher
**Stage:** 0 — Discover

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` first. If missing, create it from the founder-core template by asking: hours/week, runway in months, risk tolerance, salary-replacement deadline. Adapt everything below to real hours.
- Upstream: none. This is the first skill.

## Inputs
Career history (roles, industries, tools), recurring frustrations, things people repeatedly ask the founder for help with, skills that took > 2 years to acquire, and the constraints above.

## Process
1. **Experience Audit interview.** For each past role ask: "What did you do repeatedly that felt stupid, manual, or under-tooled? Who else had to do it? What did it cost when done wrong?" Use the question bank in `references/experience-audit.md`.
2. **Extract 15–30 raw gaps.** Cluster by who suffers (buyer persona) and when (trigger event).
3. **Score each on the Gap Scorecard** (below). Kill anything under 6/10 on founder advantage.
4. **Top 5 → Wedge Statements**, one line each: *[Persona] who [trigger] currently [painful workaround] because [why existing tools fail]. I know this because [founder evidence].*
5. **Flag the unfair advantage** per gap: domain access, regulatory knowledge, existing network, proprietary data, or technical depth others lack.
6. **Recommend 1–2** to take to `validate-idea`, and say why the others wait.

Apply the "boring is good" lens: compliance, reporting, reconciliation, data cleanup, scheduling, and document handling are where durable self-serve products hide.

## Outputs
`founder/00-idea-shortlist.md` — the scored table, wedge statements, unfair-advantage notes, and the recommended pick.

## Utils
**Gap Scorecard** (1–10 each, weighted; max 120; **≥ 84 is a go**):

| Factor | Weight |
|---|---|
| Pain frequency | ×2 |
| Pain cost | ×2 |
| Founder advantage | ×3 |
| Reachability of sufferers | ×1 |
| Willingness-to-pay signal | ×2 |
| Difficulty for outsiders to copy | ×2 |

Full Experience Audit question bank (25 prompts) and the "boring is good" checklist: `references/experience-audit.md`.

## Gate
`≥ 1 gap scoring ≥ 84 with a clear persona.` End the run with a line: `Gate: PASS/OPEN — because …`. On PASS, recommend `community-finder` next.

## Anti-patterns
Suggesting generic ideas ("an AI wrapper for X", "a marketplace for Y") unconnected to the founder's history. Scoring optimistically to please the user. Skipping the constraints step.

## Evals
- **Should fire:** "I've got 10 years in logistics and I'm sick of the manual customs paperwork." / "What could I build as a weekend business?" / "Help me come up with a startup idea."
- **Should NOT fire:** "How do I price my existing SaaS?" (→ pricing-strategy) / "Write a cold email to this lead." (→ cold-outreach)
- **Golden run checklist:** constraints read; 15–30 gaps extracted; scorecard applied with numbers; ≥1 gap ≥84; wedge statements written; `00-idea-shortlist.md` created; gate line emitted.
