# D4: Growth-sleeve design

**Status:** DECIDED · **Evidence:** `tables.md` → "A: equity share of growth sleeve (base)" and "(bear + inflation regime)"; `results.json` → `sensitivity.A_sleeve`, `sensitivity.A_sleeve_bear`

## Question
Under Strategy A, the growth sleeve is almost all of the 2028 $150k plus whatever remains after the ladder. What should it hold, how concentrated should it be, and how should Laura's values show up?

## Options
1. 60/40 equity/Treasuries
2. 80/20
3. 100% equity
4. Values-themed portfolio: education, creator economy, Asia/Taiwan

## Evidence
| Equity share of sleeve (A) | Base: facility p10 / p50 / p90 | Bear + inflation: p10 / p50 / p90 |
|---|---|---|
| 60% | $127k / $166k / $212k | $115k / $154k / $201k |
| **80%** | $118k / $167k / $230k | $103k / $152k / $214k |
| 100% | $107k / $168k / $249k | $91k / $149k / $228k |

- **Operating payments:** 100% funded in every row. Under A the sleeve's risk *only* affects the facility.
- **Median vs spread:** moving from 60% to 100% equity barely moves the median (+$2k in base, −$5k in bear). It mainly widens the spread of outcomes. With Treasuries near 5%, forecast equity premiums are thin: Vanguard 4.2–6.2% for US equities; J.P. Morgan 6.7% US large cap and 7.0% global.
- **Thematic funds:** Morningstar finds only 14–18% of thematic funds both survive and beat global equities over long periods, and 55% closed within 15 years. Fees and theme timing are the main causes.
- **Concentration risk:** Laura's income depends on publishing, media and speaking. Wealth managers for creatives stress diversifying away from the client's own industry.
- **Stock-bond correlation:** it turned positive in 2022, and AQR finds it depends on inflation uncertainty. The model tests both regimes, and the ranking of choices does not change.

## Debate
- **Advocate (80/20 with an index core):** The facility is aspirational money. In Chhabra's framework it belongs in the "market/aspirational" bucket, where risk is appropriate *because* the essential goal is already secured. 80/20 gives more upside (+$18k at p90 vs 60/40) at a modest downside cost (−$9k at p10). The 20% in Treasuries is also the dry powder for rebalancing.
- **Opponent (100% equity):** If the reserve is locked, why hold any bonds in the sleeve? Go all in.
- **Advocate:** The median gain is zero or negative in the bear case, and the 2031 announcement (D6) needs a sleeve whose 2-year range is not extreme. 100% equity raises the chance that the 2031 figure is disappointing just when Laura is making promises.
- **Opponent 2 (values themes):** Laura's story is identity, education and community. Judges loved "impact-minded" teams (2025 client: "Thank you for making the investment plans not just about the numbers").
- **Judge:** 80/20, built on a diversified core. Values show up through *selection criteria and engagement*, not a concentrated theme bet. Keep stock picks meaningful but bounded, so the WInS work has a purpose.

## Decision
**Growth sleeve = 80% equities / 20% intermediate US Treasuries, rebalanced annually.**

Equities:
- **~60% diversified core:** global all-cap exposure. In the real portfolio use broad US plus international index funds, with ~30–40% outside the US. This matches global market weights, because J.P. Morgan and Vanguard both give developed ex-US equities returns similar to or higher than US equities.
- **~40% conviction stocks:** 8–12 names, max ~5% of the sleeve each. These are the team's research picks and the WInS trading activity.
- **Selection filters** (the D4 "values lens"):
  1. Quality: ROIC above cost of capital, and the balance sheet conditions from the existing `config/client_mandate.yaml` strategy section, which can be reused.
  2. Relevance to Laura's world where it doesn't compromise 1: education and learning, creative tools and platforms, community, and Asia-Pacific (including Taiwan, which also partly offsets the TWD currency exposure of the facility).
  3. **No concentrated bet on publishing/media**, which would double Laura's career risk.
- **No thematic funds**, because of Morningstar's survival evidence.
- **Engagement:** say how the team would vote proxies or engage on education access and creator rights. This is a low-cost way to show values.

## What would change our mind
- WInS rules forbid ETFs, or require a minimum number of stocks → see D7.
- Laura says she wants a specific exclusion list (the case lists none).

## Plain English for Laura
The money for your building is invested mostly in a broad mix of global companies, with a smaller set of companies we've researched closely. It's steadied by some government bonds. We keep it diversified rather than betting on themes, because themed funds usually disappoint and your own career already depends on publishing and media. We looked for companies connected to education, creativity and Asia where the business case holds up.

**Sources:**
- [Morningstar: Thematic fund landscape in 7 charts](https://www.morningstar.com/funds/thematic-fund-landscape-7-charts)
- [Vanguard return forecasts](https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html)
- [J.P. Morgan 2026 LTCMA](https://am.jpmorgan.com/us/en/asset-management/institutional/about-us/media/press-releases/jp-morgan-releases-2026-long-term-capital-market-assumptions/)
- [AQR: A changing stock-bond correlation](https://www.aqr.com/Insights/Research/Journal-Article/A-Changing-Stock-Bond-Correlation)
- [Chhabra: Beyond Markowitz](https://www.ssrn.com/abstract=925138)
- [Wealthspire: Financial planning for creatives](https://www.wealthspire.com/blog/the-art-of-financial-planning-for-artists-entertainers-and-creatives/)
- [Wharton: 2025 finale (client quote)](https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/)
