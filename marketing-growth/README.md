# marketing-growth

Predictable attention. The skills that pick one channel and one message, write copy that earns action, build organic content and lifecycle email, grow the founder's brand on a single platform, and run paid ads — but only after PMF and unit economics say it's safe.

## What it does

Stops the four-channels-at-once trap. It scores channels against the founder's real skills and hours, picks one primary and one secondary, and enforces the sequence: message before spend, organic before paid, PMF before ads.

## Installation

```
/plugin marketplace add codezard/founder-os-marketplace
/plugin install founder-core@founder-os-marketplace
/plugin install marketing-growth@founder-os-marketplace
```

Install `founder-core` first.

## Skills

| Skill | Stage | Reads → Writes |
|---|---|---|
| `marketing-plan` | 3 | `06-pmf-report.md`, `01-community-map.md` → `12-marketing-plan.md` |
| `copywriting` | 3 | `evidence-ledger.csv` → `copy-bank.md` (+ inline copy) |
| `seo-content` | 4 | `12-marketing-plan.md` → `13-content-plan.md`, `content/` |
| `email-campaigns` | 4 | `07-landing-page.md`, `11-first-customers.md` → `14-email-sequences.md` |
| `social-media` | 5 | ICP, founder story → `15-social-plan.md`, `story-bank.md` |
| `paid-ads` | 5 | `06-pmf-report.md`, `19-unit-economics.md` → `16-paid-ads-plan.md` |

`paid-ads` uses `founder-core/scripts/ads_math.py` and is gated behind PMF + unit economics. Check gates with `/founder-os:status`.

---

*Part of the Founder OS marketplace — from experience gap to first $1M.*
