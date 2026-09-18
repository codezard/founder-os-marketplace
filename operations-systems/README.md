# operations-systems

Get the founder out of the machine. The Stage 4 skills that inventory recurring work, turn it into SOPs, automate only what's stable, delegate with a trust ladder, and hire against a scorecard — following do → document → delegate → automate → delete.

## What it does

Attacks the founder-as-bottleneck problem in the right order. It measures where founder hours actually go, documents before delegating, delegates before automating, automates before hiring, and never hires for a job with no SOP.

## Installation

```
/plugin marketplace add codezard/founder-os-marketplace
/plugin install founder-core@founder-os-marketplace
/plugin install operations-systems@founder-os-marketplace
```

Install `founder-core` first.

## Skills

| Skill | Stage | Reads → Writes |
|---|---|---|
| `processize` | 4 | time log, customer journey → `17-process-inventory.md` |
| `sop-builder` | 4 | a task walkthrough → `sops/<task>.md` |
| `automation-workflows` | 4 | a proven SOP → `automations/<slug>.md` |
| `delegation-framework` | 4 | `17-process-inventory.md` → `18-delegation-plan.md` |
| `hiring-playbook` | 4 | `17-process-inventory.md`, SOP coverage → `hiring/<role>-scorecard.md` |

`sop-builder` uses `founder-core/scripts/sop_index.py`. Check gates with `/founder-os:status`.

---

*Part of the Founder OS marketplace — from experience gap to first $1M.*
