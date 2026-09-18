---
name: cold-outreach
description: "Writes personalized, trigger-based 3-touch outreach sequences that earn replies, in research, sale, or partnership mode. Use when the user mentions cold email, cold DMs, LinkedIn outreach, reaching out to prospects, prospecting, a sequence, or getting meetings — and whenever validate-idea or first-customers needs conversations. Refuses mass sends and fake personalization."
---

# Cold Outreach

Builds a per-channel, per-person sequence with a real reason to reach out this week. Inherits `founder-core/references/writing-standards.md` (specificity, one CTA).

**Owner role:** Founder-Seller
**Stage:** 1 (research) / 3 (sale)

## Step 0 — Constraints & upstream
- Read `founder/constraints.md` — set daily volume to what the founder can personalize.
- Upstream: ICP and `founder/01-community-map.md` seed list. If no list exists, run `community-finder` first.

## Inputs
ICP, seed list, mode (research / sale / partnership), channel, proof available.

## Process
1. **Confirm the mode.** Research mode asks for 20 minutes and offers nothing. Sale mode leads with a specific observation about them and one outcome. Partnership mode leads with mutual benefit.
2. **Build the list with a Trigger column:** why *this* person *this* week (job change, post, regulation, hiring, complaint).
3. **Write a 3-touch sequence per channel:** Touch 1 = observation + one-line relevance + tiny ask (< 75 words); Touch 2 = value add (insight, benchmark, resource); Touch 3 = breakup, door left open.
4. **Personalize the first line of every message** — never templated openers.
5. **Set daily volume** (typically 10–20) and the tracking sheet: sent, opened, replied, meeting, outcome.
6. **Review weekly:** reply rate < 5% → fix the list; replies but no meetings → fix the ask.

## Outputs
`founder/10-outreach-sequences.md` + `founder/outreach-tracker.csv` (columns: contact, channel, trigger, sent_date, opened, replied, meeting, outcome).

## Utils
**Trigger taxonomy:** role change, funding, hiring, public complaint, regulation, product launch, content they posted.
**Sequence templates** per channel: email, LinkedIn, community DM, WhatsApp.
**Reply-rate diagnostic:** low reply → list/targeting; reply-no-meeting → ask/offer; meeting-no-close → route to `objection-handling`.

## Gate
`≥ 10% reply rate and ≥ 3% meeting rate on a qualified list.` End with `Gate: PASS/OPEN — because …`.

## Anti-patterns
Mass sends. Fake "I saw your post" personalization. Selling in research mode.

## Evals
- **Should fire:** "Write a cold email to these 20 prospects." / "How do I get meetings on LinkedIn?" / (validate-idea needs interviews)
- **Should NOT fire:** "Write a nurture email to my list." (→ email-campaigns) / "How do I answer 'too expensive'?" (→ objection-handling)
- **Golden run checklist:** mode confirmed; list has a trigger per contact; 3-touch sequence per channel; first lines personalized; daily volume set to real capacity; tracker created; `10-outreach-sequences.md` created; gate line emitted.
