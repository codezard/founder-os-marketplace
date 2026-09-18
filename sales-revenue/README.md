# sales-revenue

Turn attention into money. The skills that build the offer before the product, price to value, get meetings with personalized outreach, land the first ten paying customers by hand, and turn objections into product feedback.

## What it does

Keeps selling ahead of building. It packages a dream outcome into an offer a stranger can repeat, anchors price to the value delivered (not cost-plus), runs research- and sale-mode outreach that earns replies, and runs the founding-customer playbook for the first ten paying users.

## Installation

```
/plugin marketplace add codezard/founder-os-marketplace
/plugin install founder-core@founder-os-marketplace
/plugin install sales-revenue@founder-os-marketplace
```

Install `founder-core` first.

## Skills

| Skill | Stage | Reads → Writes |
|---|---|---|
| `offer-creation` | 1 | `02-validation-report.md` → `08-offer.md` |
| `pricing-strategy` | 2/5 | `08-offer.md`, `evidence-ledger.csv` → `09-pricing.md` |
| `cold-outreach` | 1/3 | `01-community-map.md`, ICP → `10-outreach-sequences.md`, `outreach-tracker.csv` |
| `first-customers` | 2 | `08-offer.md`, `09-pricing.md`, `05-mvp-spec.md` → `11-first-customers.md` |
| `objection-handling` | 3 | sales-call debriefs → `objection-library.md` |

`pricing-strategy` uses `founder-core/scripts/pricing_bands.py`. `cold-outreach` has a research mode that `validate-idea` reuses. Check gates with `/founder-os:status`.

---

*Part of the Founder OS marketplace — from experience gap to first $1M.*
