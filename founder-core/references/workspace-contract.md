# Founder OS — Shared Workspace Contract

Every skill in this marketplace reads from and writes to a single `founder/` directory at the root of the founder's own project (not this marketplace repo). This is what makes the marketplace a *system* rather than a bag of prompts.

## Layout

```
founder/
├── constraints.md            # hours/week, runway, risk, salary target — read by EVERY skill FIRST
├── decision-log.md           # appended by decision-frameworks and any skill making a call
├── evidence-ledger.csv       # validate-idea; read by copywriting, pricing, landing-page
├── objection-library.md      # objection-handling; read by landing-page, offer-creation
├── copy-bank.md              # copywriting; read by email, social, ads
├── story-bank.md             # social-media; read by copywriting, pitch-deck
├── 00-idea-shortlist.md … 26-team-operating-system.md   # numbered stage artifacts
├── sops/                     # sop-builder
├── automations/              # automation-workflows
├── hiring/                   # hiring-playbook
├── content/                  # seo-content briefs
└── weekly-reviews.md         # founder-productivity
```

## The three rules every skill obeys

1. **Constraints first.** Step 0 of every skill: read `founder/constraints.md`. If it is missing, create it by asking the founder for hours/week, runway in months, risk tolerance, and whether/when this must replace a salary. Adapt the plan to real hours — never assume full-time.
2. **Upstream check.** Each skill names the artifact(s) it depends on. If a required upstream artifact is absent, offer to run the upstream skill first; never fabricate the upstream output.
3. **Fixed output filename.** Each skill writes to the exact filename listed in its card so downstream skills can find it.

## Numbered artifact map

| File | Written by |
|---|---|
| `00-idea-shortlist.md` | find-business-idea |
| `01-community-map.md` | community-finder |
| `02-validation-report.md` + `evidence-ledger.csv` | validate-idea |
| `03-market-brief.md` | market-research |
| `04-competitive-matrix.md` | competitive-analysis |
| `05-mvp-spec.md` | mvp-scoper |
| `06-pmf-report.md` | pmf-measure |
| `07-landing-page.md` | landing-page |
| `08-offer.md` | offer-creation |
| `09-pricing.md` | pricing-strategy |
| `10-outreach-sequences.md` + `outreach-tracker.csv` | cold-outreach |
| `11-first-customers.md` | first-customers |
| `12-marketing-plan.md` | marketing-plan |
| `13-content-plan.md` + `content/` | seo-content |
| `14-email-sequences.md` | email-campaigns |
| `15-social-plan.md` + `story-bank.md` | social-media |
| `16-paid-ads-plan.md` | paid-ads |
| `17-process-inventory.md` | processize |
| `sops/<task>.md` | sop-builder |
| `automations/<slug>.md` | automation-workflows |
| `18-delegation-plan.md` | delegation-framework |
| `hiring/<role>-scorecard.md` | hiring-playbook |
| `19-unit-economics.md` | unit-economics |
| `20-financial-model.xlsx` | financial-model |
| `21-pitch-deck.pptx` + `21-pitch-narrative.md` | pitch-deck |
| `22-fundraising-decision.md` | fundraising |
| `23-values.md` | company-values |
| `24-minimalist-review-<quarter>.md` | minimalist-review |
| `25-growth-plan.md` | sustainable-growth |
| `26-team-operating-system.md` | team-building |
| `decision-log.md` | decision-frameworks (+ any skill making a call) |
| `week-template.md` + `weekly-reviews.md` | founder-productivity |
