# Founder OS — Metrics Glossary

One definition per metric so no two skills disagree. When a skill computes or cites any of these, it uses exactly this formula.

| Metric | Definition | Formula / rule |
|---|---|---|
| **MRR** | Monthly recurring revenue | Sum of normalized monthly subscription revenue from active paying customers. Exclude one-time fees. |
| **ARR** | Annual recurring revenue | MRR × 12. The $1M target is $83,333 MRR. |
| **ARPA** | Average revenue per account | MRR ÷ number of active paying accounts. |
| **Gross margin** | Share of revenue left after cost to serve | (Revenue − COGS) ÷ Revenue. COGS = hosting, third-party tools per customer, and human delivery time. Target ≥ 60%. |
| **Monthly churn** | Share of customers lost per month | Customers lost in month ÷ customers at start of month. Compute logo churn and revenue churn separately. |
| **Lifetime (months)** | Expected customer lifespan | 1 ÷ monthly churn. Only trust with ≥ 3 months of data. |
| **LTV** | Lifetime value (gross-margin adjusted) | ARPA × gross margin × lifetime (months). Never compute LTV on revenue instead of gross margin. |
| **CAC** | Customer acquisition cost | Fully loaded sales + marketing spend for a channel ÷ customers acquired from that channel. Compute per channel, never only blended. |
| **CAC payback** | Months to recover CAC | CAC ÷ (ARPA × gross margin). Guardrail: ≤ 6 months. |
| **LTV:CAC** | Return on acquisition | LTV ÷ CAC. Guardrail: ≥ 3. |
| **NRR** | Net revenue retention | (Starting MRR + expansion − contraction − churn) ÷ starting MRR, for a fixed cohort over 12 months. Target ≥ 100%. |
| **Activation** | Reaching first value | % of new customers who complete the one instrumentation event that proves they got the promised outcome. |
| **TTV** | Time-to-value | Elapsed time from signup/payment to the activation event. |
| **PMF score** | Sean Ellis product-market-fit score | % of active users who would be "very disappointed" if the product disappeared. ≥ 40% with a flattening retention curve = strong. |
| **Rule of 40** | Growth + profit health | Annual growth rate % + profit margin % ≥ 40. Used at Stage 5. |
