---
name: validate-idea
description: "Kills or confirms a business idea with real evidence (money, time, or access) before any building. Use when the user wants to validate an idea, asks if something is worth building, mentions customer interviews, testing demand, pre-selling, or a smoke test — and ESPECIALLY when they are about to start building with no proof of demand. Interrupt and offer this before writing product code."
---

# Validate Idea

Designs the cheapest experiment that could kill the idea, runs the interviews, logs the evidence, and returns a Go/Pivot/Kill verdict. Inherits `founder-core/references/principles.md` (A2 evidence not opinion, A3 sell before build).

**Owner role:** Founder-Researcher / Founder-Seller
**Stage:** 1 — Validate

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` first.
- Upstream: `founder/00-idea-shortlist.md` (wedge) and `founder/01-community-map.md` (seed list). If missing, run `find-business-idea` / `community-finder` first.

## Inputs
Wedge statement, seed list, constraints, and the hypothesis to kill.

## Process
1. **Write the Riskiest Assumption** — the single belief that, if false, kills the business. Usually "they will pay" or "they can be reached".
2. **Pick the cheapest experiment** that tests it (Validation Ladder below). Default: 15 problem interviews + a landing page with a paid pre-order or refundable deposit.
3. **Generate the interview script** using Mom Test rules: ask about past behavior, not opinions; never pitch; ask what they've spent and how they work around it. Use the 12-question template in `references/interview-kit.md`.
4. **Run outreach** via `cold-outreach` in **research mode** (ask for 20 minutes, offer nothing).
5. **Log every interview** in the Evidence Ledger: quote, workaround, money spent, urgency 1–5, would-they-pay signal.
6. **Synthesize**: % who have the problem, % who actively solve it today, what they pay, and the exact words they use (feeds `copywriting`).
7. **Deliver a verdict** — **Go / Pivot / Kill** — with the evidence *type* (money / time / access) that justifies it.

## Outputs
`founder/02-validation-report.md` (riskiest assumption, method, synthesis, verdict + evidence type) and `founder/evidence-ledger.csv` (schema in `references/interview-kit.md`).

## Utils
**Validation Ladder** (cheapest → most expensive): conversations → landing page + waitlist → landing page + deposit → concierge delivery → paid pilot → MVP. Always start at the cheapest rung that can produce the evidence type you need.

**Go/Pivot/Kill rule:** Go = **≥ 3 payers OR ≥ 5 weekly manual users**. Pivot = strong problem, weak wedge/segment. Kill = no urgency, no spend, no reach.

Interview script + Evidence Ledger CSV schema: `references/interview-kit.md`.

## Gate
`Verdict = Go with the evidence type stated.` End with `Gate: PASS/OPEN — because …`. On PASS, recommend `offer-creation` and `market-research`. On Pivot/Kill, route back to `find-business-idea` with the next gap.

## Anti-patterns
Counting "I'd totally use that" as evidence. Interviewing friends. Building before running this. Pitching during research-mode calls.

## Evals
- **Should fire:** "Is this idea worth building?" / "I'm about to start coding my app." / "How do I test demand for this?"
- **Should NOT fire:** "Design my logo." / "What's my TAM?" (→ market-research)
- **Golden run checklist:** constraints + upstream read; riskiest assumption named; ladder rung chosen; Mom-Test script produced; evidence ledger populated (or method to populate stated); Go/Pivot/Kill verdict with evidence type; both output files created; gate line emitted.
