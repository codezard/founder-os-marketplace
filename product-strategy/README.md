# product-strategy

Know the market, ship the smallest thing that wins. The skills that size the opportunity bottom-up, stake out a position no one owns, scope an MVP down to the paid outcome, measure real product-market fit, and turn a page into pre-orders.

## What it does

Keeps you honest between "validated" and "scaling": it sizes the market from the bottom up (no 1%-of-a-huge-TAM slides), finds the positioning gap, forces the MVP down to what customers actually paid for, and refuses to declare PMF on vanity growth.

## Installation

```
/plugin marketplace add codezard/founder-os-marketplace
/plugin install founder-core@founder-os-marketplace
/plugin install product-strategy@founder-os-marketplace
```

Install `founder-core` first — every skill reads its principles, stage map, glossary, and writing standards.

## Skills

| Skill | Stage | Reads → Writes |
|---|---|---|
| `market-research` | 1 | `02-validation-report.md` → `03-market-brief.md` |
| `competitive-analysis` | 1 | `03-market-brief.md` → `04-competitive-matrix.md` |
| `mvp-scoper` | 2 | `02-validation-report.md`, `04-competitive-matrix.md` → `05-mvp-spec.md` |
| `pmf-measure` | 3 | customer usage/payment data → `06-pmf-report.md` |
| `landing-page` | 1/2/5 | `04-competitive-matrix.md`, `08-offer.md`, `evidence-ledger.csv` → `07-landing-page.md` |

`pmf-measure` uses `founder-core/scripts/retention.py`. Check gate status with `/founder-os:status`.

---

*Part of the Founder OS marketplace — from experience gap to first $1M.*
