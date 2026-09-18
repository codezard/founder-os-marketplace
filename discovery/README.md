# discovery

Find and validate the idea. The Stage 0–1 skills that mine your experience for a hard-to-copy problem, find where its sufferers gather, and prove demand with evidence before you write a line of product code.

## What it does

Turns "I want to start something" into a scored shortlist of experience gaps, a map of the communities where buyers already are, and a Go/Pivot/Kill verdict backed by money, time, or access — never opinion.

## Installation

```
/plugin marketplace add codezard/founder-os-marketplace
/plugin install founder-core@founder-os-marketplace
/plugin install discovery@founder-os-marketplace
```

Install `founder-core` first — every skill reads its principles, stage map, and writing standards.

## Skills

| Skill | Stage | Reads → Writes |
|---|---|---|
| `find-business-idea` | 0 | `constraints.md` → `00-idea-shortlist.md` |
| `community-finder` | 0 | `00-idea-shortlist.md` → `01-community-map.md` |
| `validate-idea` | 1 | `00-idea-shortlist.md`, `01-community-map.md` → `02-validation-report.md`, `evidence-ledger.csv` |

Run them in order. `validate-idea` uses `cold-outreach` (from `sales-revenue`) in research mode. Check gate status any time with `/founder-os:status`.

---

*Part of the Founder OS marketplace — from experience gap to first $1M.*
