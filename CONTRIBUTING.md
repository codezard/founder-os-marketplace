# Contributing to Founder OS

Thanks for helping make Founder OS better. This marketplace is a *system*, so contributions should keep the pieces consistent.

## Ground rules

1. **One skill = one `SKILL.md`** under `<plugin>/skills/<skill-name>/`, with frontmatter `name` (kebab-case, different from the plugin name) and a `description` written as a pushy, third-person trigger.
2. **Keep `SKILL.md` under 500 lines.** Push rubrics, templates, and question banks into `references/` (one level deep) or `assets/`; put deterministic logic in `founder-core/scripts/`.
3. **Follow the shared contracts.** Every skill: reads `founder/constraints.md` first, names its upstream artifact(s), writes a fixed output filename, and ends a run with a `Gate: PASS/OPEN — because …` line. See `founder-core/references/workspace-contract.md`.
4. **No fabrication.** Market numbers, community sizes, and competitor prices are sourced or explicitly marked as assumptions. Use the metric formulas in `founder-core/references/metrics-glossary.md` — don't invent new ones.
5. **Vendor-neutral.** Skills describe methods, not specific products.

## Adding a skill

1. Create the skill folder and `SKILL.md`.
2. Add it to the plugin's `README.md` skills table and to the plugin's entry in `.claude-plugin/marketplace.json` (`skills` array).
3. Add the evals block: 3 trigger prompts that should fire, 2 near-misses that should not, and 1 golden-run checklist.

## Workflow

- Branch from `main`, open a pull request, and describe what changed and why.
- Validate JSON before pushing: `jq empty .claude-plugin/marketplace.json`.
- Keep commits focused.
