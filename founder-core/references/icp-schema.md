# Founder OS — ICP / Persona Schema

Every skill that names a customer uses these fields. When a skill writes a persona to the `founder/` workspace, it writes exactly this shape so downstream skills can read it without guessing.

## Persona fields

| Field | Meaning |
|---|---|
| `persona_name` | Short label for the buyer (e.g. "Solo compliance officer at a 50–200-person fintech"). |
| `role` | Job title(s) that feel the pain. |
| `context` | Company size, industry, geography, tools they already use. |
| `trigger_event` | The moment the pain becomes urgent (audit scheduled, hire made, regulation changes, tool sunset). |
| `job_to_be_done` | The outcome they are trying to achieve, in their words. |
| `current_workaround` | What they do today instead of buying anything (the real competition). |
| `current_spend` | Money and hours the workaround costs per period. |
| `willingness_to_pay` | Evidence-backed band from interviews / the evidence ledger. |
| `where_they_gather` | Communities and channels (links to `founder/01-community-map.md`). |
| `words_they_use` | Verbatim phrases from interviews — feeds copywriting and landing pages. |
| `who_approves_budget` | Economic buyer vs. user vs. blocker. |
| `disqualifiers` | Who is NOT the ICP, so acquisition doesn't chase the wrong people. |

## Rules

- The ICP is discovered, not invented. Populate from `find-business-idea`, `validate-idea`, and `pmf-measure` — never fabricate fields.
- The "very disappointed" segment from `pmf-measure` **is** the real ICP. When it disagrees with an earlier guess, the survey wins.
- Keep one canonical persona per product line. If the product serves two personas, write two records and say which one each skill is targeting.
