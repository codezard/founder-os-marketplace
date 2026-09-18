# founder-core

The shared foundation every other Founder OS plugin depends on. Install this first.

## What it does

Holds the operating principles, the stage map to $1M, the metrics glossary, the ICP schema, and the writing standards that keep all 34 skills consistent — plus the shared templates and the scripts they call. It also ships the `/founder-os:status` command, which reports which stage gates are open or closed for your project.

## Installation

```bash
/plugin marketplace add codezard/founder-os-marketplace
/plugin install founder-core@founder-os-marketplace
```

## Commands

- `/founder-os:status` — Run the gate checker and show where you are on the stage map.

## References (read by other skills)

- `references/principles.md` — the 10 operating principles (A1–A10).
- `references/stage-map.md` — the six stages, their metrics, and their gates.
- `references/metrics-glossary.md` — one formula per metric so no two skills disagree.
- `references/icp-schema.md` — the persona fields every skill uses.
- `references/writing-standards.md` — specificity rule, banned words, one-CTA rule.
- `references/workspace-contract.md` — the shared `founder/` folder layout and the three rules every skill obeys.

## Scripts

- `scripts/gate_check.py` — reports open/closed stage gates (behind `/founder-os:status`).
- `scripts/unit_econ.py` — ARPA, LTV, CAC, payback, LTV:CAC with guardrail checks.
- `scripts/retention.py` — cohort retention curves for PMF.
- `scripts/pricing_bands.py` — Van Westendorp price-sensitivity bands.
- `scripts/ads_math.py` — Max CPA / CPC and test budget for paid ads.
- `scripts/sop_index.py` — builds an index of the SOPs in `founder/sops/`.

## Templates

`assets/templates/` holds the constraints doc, decision-log entry, one-page brief, SOP, hiring scorecard, and weekly review that the skills fill in.

---

*Part of the Founder OS marketplace — from experience gap to first $1M.*
