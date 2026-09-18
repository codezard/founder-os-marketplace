# Founder OS — a Claude Code skill marketplace

**From experience gap to your first $1M in revenue.**

Founder OS is a Claude Code plugin marketplace that turns the founder journey into a *system* of 34 skills across 8 plugins. Each skill is a self-contained expert that fires when you need it, reads and writes a shared `founder/` workspace, and refuses to let you skip steps (no ads before product-market fit, no hiring before you've written the SOP, no raising before Stage 3).

## Install

```
/plugin marketplace add codezard/founder-os-marketplace
/plugin install founder-core@founder-os-marketplace
/plugin install discovery@founder-os-marketplace
# …install whichever plugins match your current stage
```

Install `founder-core` first — every other plugin reads its principles, stage map, glossary, and writing standards. Then check where you are any time:

```
/founder-os:status
```

## The plugins

| Plugin | Theme | Skills |
|---|---|---|
| **founder-core** | Shared principles, stage map, glossary, scripts, `/founder-os:status` | — |
| **discovery** | Find and validate the idea | find-business-idea · community-finder · validate-idea |
| **product-strategy** | Know the market, ship the smallest thing that wins | market-research · competitive-analysis · mvp-scoper · pmf-measure · landing-page |
| **sales-revenue** | Turn attention into money | offer-creation · pricing-strategy · cold-outreach · first-customers · objection-handling |
| **marketing-growth** | Predictable attention | marketing-plan · copywriting · seo-content · email-campaigns · social-media · paid-ads |
| **operations-systems** | Get the founder out of the machine | processize · sop-builder · automation-workflows · delegation-framework · hiring-playbook |
| **finance-fundraising** | Know the numbers, raise only if you must | unit-economics · financial-model · pitch-deck · fundraising |
| **leadership-mindset** | Run yourself and the company | company-values · minimalist-review · sustainable-growth · decision-frameworks · founder-productivity · team-building |

## How it works

- **A shared workspace.** Every skill reads and writes a `founder/` directory in *your* project (not this repo). One skill's output is the next skill's input — `validate-idea` writes the evidence ledger, `copywriting` reads the customer's own words from it. See `founder-core/references/workspace-contract.md`.
- **Constraints first.** Every skill reads `founder/constraints.md` (your hours/week, runway, risk) before planning, so a 15-hour-a-week side-founder gets a different plan than a full-time one.
- **Gates, not vibes.** Six stages, each with a hard gate. Skills refuse out-of-sequence work and route you to the prerequisite. `/founder-os:status` reports which gates are open.
- **Evidence over opinion.** Validation counts only money, time, or access — never compliments. Market numbers are sourced or marked as assumptions; nothing is fabricated.

## The stage map

| Stage | Objective | Gate to exit |
|---|---|---|
| 0 · Discover | Shortlist experience-gap problems + a reachable community | A gap scoring high with a named community ≥ 500 people |
| 1 · Validate | Kill or confirm with money/time/access | ≥ 3 payers OR ≥ 5 weekly manual users |
| 2 · MVP | Deliver the outcome, by hand if needed | 10 paying customers, ≥ 40% "very disappointed" |
| 3 · Repeatable sale | One channel, one message that acquires predictably | One channel ≥ 10/mo, payback < 6mo, MRR ≥ $8–10k |
| 4 · Processize | Remove the founder from delivery | ≤ 5 founder ops-hours/week, MRR ≥ $25–30k |
| 5 · Grow to $1M | Second channel, expand revenue, protect margin | $83k MRR × 3 months, GM ≥ 60%, NRR ≥ 100% |

Full detail: `founder-core/references/stage-map.md`.

## Repository layout

```
founder-os-marketplace/
├── .claude-plugin/marketplace.json
├── founder-core/            # principles, stage map, glossary, scripts (install first)
├── discovery/               # skills 1–3
├── product-strategy/        # skills 4–8
├── sales-revenue/           # skills 9–13
├── marketing-growth/        # skills 14–19
├── operations-systems/      # skills 20–24
├── finance-fundraising/     # skills 25–28
└── leadership-mindset/      # skills 29–34
```

## Contributing

Issues and pull requests are welcome. Each skill keeps its `SKILL.md` under 500 lines and pushes rubrics and question banks into `references/`. See `CONTRIBUTING.md`.

## License

MIT — see [LICENSE](LICENSE). Free for anyone to use, fork, and adapt.
