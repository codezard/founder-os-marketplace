# Validation interview kit

## The 12-question Mom Test script

Rules: ask about the past and about specifics, not the future or opinions. Never describe your idea until the end (if at all). Let silence work.

1. Walk me through the last time you dealt with <problem>. What happened?
2. How often does that come up?
3. What did you do about it — step by step?
4. What tools or people did you use?
5. What was the hardest or most annoying part?
6. What did it cost you when it went wrong (time, money, stress)?
7. Have you tried to fix or improve it? What happened?
8. Did you spend money on anything to help? How much?
9. Who else is affected when this happens?
10. If you had a magic fix, what would it do for you?
11. Who would need to approve paying for a fix like that?
12. Who else deals with this that I should talk to? (the access signal)

Close: "Would it be okay if I followed up when I have something to show you?" — a yes with a real calendar slot is a stronger signal than any compliment.

## Evidence Ledger CSV schema

`founder/evidence-ledger.csv` columns:

```
interview_id,date,name_or_handle,role,has_problem(y/n),solves_it_today(y/n),money_spent,urgency_1_5,would_pay_signal,verbatim_quote,workaround,referral_given(y/n)
```

- `would_pay_signal`: none / interest / soft-commit / deposit / paid
- `verbatim_quote`: the customer's own words (reused by copywriting and landing-page)

## Reading the ledger

- **Money evidence**: any row with `would_pay_signal` = deposit/paid.
- **Time evidence**: `solves_it_today = y` with a repeated manual workaround.
- **Access evidence**: `referral_given = y` (unprompted intro to peers).

Go requires ≥ 3 payers OR ≥ 5 weekly manual users. Report which evidence type you actually collected.
