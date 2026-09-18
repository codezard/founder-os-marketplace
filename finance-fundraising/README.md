# finance-fundraising

Know the numbers, raise only if you must. The skills that compute unit economics with hard guardrails, build a driver-based financial model, and — only when the business genuinely requires capital — produce a pitch deck and run a disciplined raise.

## What it does

Keeps money decisions evidence-based. It computes LTV, CAC, and payback the same way every time (from the shared glossary), stress-tests survival in a downside scenario, and treats fundraising as a tool for a specific class of business — defaulting to bootstrapping and non-dilutive options.

## Installation

```
/plugin marketplace add codezard/founder-os-marketplace
/plugin install founder-core@founder-os-marketplace
/plugin install finance-fundraising@founder-os-marketplace
```

Install `founder-core` first.

## Skills

| Skill | Stage | Reads → Writes |
|---|---|---|
| `unit-economics` | 3 | pricing, cost-to-serve, channel data → `19-unit-economics.md` |
| `financial-model` | 5 | `19-unit-economics.md`, MRR/cash → `20-financial-model.xlsx` |
| `pitch-deck` | 5 | positioning, traction, model → `21-pitch-deck.pptx`, `21-pitch-narrative.md` |
| `fundraising` | 5 | `20-financial-model.xlsx` → `22-fundraising-decision.md` |

`unit-economics` uses `founder-core/scripts/unit_econ.py`. `pitch-deck` and `fundraising` are gated behind a Raise decision and Stage 3. Check gates with `/founder-os:status`.

---

*Part of the Founder OS marketplace — from experience gap to first $1M.*
