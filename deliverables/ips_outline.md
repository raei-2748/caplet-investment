# Investment Policy Statement: section outline (due 6 Nov 2026)

> **Bullet outline only.** Students write all prose. Each bullet names its number and its source in `model/` or `decisions/`. Check the length and format limits (Q5).

## 1. Client summary
- Who Laura is. Her goals in her own framing: a promise (operating payments) and an aspiration (facility).
- Cash flows: $300k (Jan 2027), $150k (Jan 2028); ten $50k payments 2033–42; nothing else. *(case)*
- Risk: willing to take thoughtful risks, but wants the capital her goals require protected. *(case)*
- Values: storytelling, identity, education, community. No exclusions specified. *(case; D4)*

## 2. Investment objectives
- **Primary:** fund all ten payments with a high degree of certainty, as defined in §4. *(D2)*
- **Secondary:** maximise the responsible 2033 facility contribution while keeping flexibility. *(D5)*
- **Tertiary:** support a credible 2031 co-sponsor commitment. *(D6)*

## 3. Strategy: "Lock, then grow"
- **Two sleeves:** reserve ladder and growth sleeve. Show chart 02 (certainty vs facility).
- **Why now:** ~5.15% yields on 6–15 year Treasuries mean the ladder costs ≈ $298k. *(tables: Liability)*
- **Why not the alternatives:**
  - C80 is only 93.1% funded (86.6% in bear); its median is +$20k but its p10 is −$92k.
  - B fails more often if the 2028 money is late or smaller. *(D1, D8)*
- **Fallback rule:** if yields are below ~4% in Jan 2027, use staged hedge B (70%→100%). *(D1)*

## 4. Certainty definition *(D2)*
- A mechanism plus a standard of ≥ 99.5% in every scenario, 93/93 historical windows, and funded with no 2028 money. Benchmark: Solvency II's 1-in-200.
- Residual risks listed.

## 5. Asset allocation and ranges
| Sleeve | Target (2028 onward) | Range | Holdings |
|---|---|---|---|
| Reserve ladder | = PV of payments (≈ 66% at today's yields) | Not traded; held to maturity | iBonds IBTM–IBTR + Treasuries 2037–41 *(D3)* |
| Growth: equity | 80% of sleeve | 75–85% | ~60% core index, ~40% in 8–12 names *(D4)* |
| Growth: Treasuries | 20% of sleeve | 15–25% | Intermediate Treasuries |

## 6. Security selection (growth sleeve) *(D4)*
- Quality filters, the values lens, no thematic funds, no concentrated bet on publishing/media.
- Position limits: max ~5% of the sleeve per name; sector cap.

## 7. Rebalancing and monitoring
- Rebalance the sleeve annually, or when drift exceeds 5 points.
- Never sell the ladder early.
- Review the facility projection each January.
- Early-warning metric: surplus ÷ projected facility need.

## 8. The 2031 rule *(D6)*
- Lock 70% of the surplus into Treasuries maturing Dec 2032.
- Two-tier announcement: committed minimum plus 80% range.

## 9. 2033 decisions *(D3, D5)*
- Designate the ladder as the operating reserve; median value ≈ $413k.
- Contribute 80% of the surplus to the facility; keep a 20% buffer.

## 10. Key assumptions *(assumptions.yaml)*
- Returns: equity arithmetic 7.5% / 16% vol (base); bear/bull cases. Sources: J.P. Morgan LTCMA 2026, Vanguard.
- Rates: y0 5.15%, long-run 4.2% (FOMC longer-run 3.2% + term premium), volatility 0.9pp a year (FRED).
- Inflation: 2.5% US (breakeven); Taiwan facility costs 2.5%.
- No outside funding; beginning-of-year cash flows; taxes excluded (per case).

## 11. WInS implementation note *(D7)*
- State clearly what WInS represents: branch 1 (ETFs allowed) or branch 2 (stocks only).

## 12. Risks and limitations *(red team #4)*
