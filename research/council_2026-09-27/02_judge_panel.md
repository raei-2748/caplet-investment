**Judge Panel Chair: evaluation of the Team Caplet council debate**

I scored against the five SMApply criteria, the IPS and Trading Notes instructions, and the Laura Gao case (all re-read this session). Two things in those documents shape everything below. First, the IPS guidance asks for "the strategy and decision-making framework… rather than… detailed financial calculations". It says the IPS is not expected to include final reserve calculations or the co-sponsor draft. Second, evaluators read all three deliverables together and check that they agree.

### Candidate architectures that emerged

**A. Static defeasance plus growth sleeve.** Buy the full 2033–42 Treasury zero ladder on 1/1/2027 (about $293–298k). The 2028 $150k goes into a sleeve with 50–70% equity that de-risks in 2031–32.

**B. Rule-based policy engine.** This is where the council converged. It has four rules:
1. A hedge ratio of min(100%, assets ÷ Treasury-priced liability) that only ratchets up.
2. Risk is measured on the surplus, not on total assets.
3. A funding waterfall: shortfall from the 2027 deposit comes out of the 2028 deposit first, and the ladder is bought from the nearest maturity outward.
4. For 2031, a "paid-for floor plus stated-probability stretch" rule, with the floor locked in a 2-year Treasury.

**C. Growth-first glide path.** This was the team's original plan, plus the Strategist's first draft. It holds about 75% equity with a glide path and buys the reserve in 2031 or 2033, or rolls the 2037–42 payments short.

| Criterion | A | B | C |
|---|---|---|---|
| Investment Strategy | 7: clear and disciplined, but the 2027 snapshot is about 99% bonds, which is weak on "appropriate diversification" | 9: the thesis is a policy, not a rate forecast, and it handles "changing time horizons" explicitly | 5: its own sensitivity runs show the reserve exposed to rates for 4–6 years |
| Client Knowledge | 7: meets "high certainty", but under-uses Laura's "thoughtful risks" and her 2031 need | 9: the waterfall answers her lumpy income, and the stated-model probabilities suit a Statistics graduate | 4: 3–9% failure (40–60% if the 2028 deposit never arrives) breaks the case's "high degree of certainty" requirement |
| Portfolio Analysis | 8: liability pricing plus stresses | 9: market-consistent certainty definition, and model risk shown across four models | 6: can be modelled, but the models condemn it |
| Articulation | 6: little process to narrate | 8: the lock-timing contradiction and how it was resolved make a genuine learning story (provisional until the Final Report) | 6 |
| Creativity/Presentation | 6: reads as "safe bucket + growth bucket" | 9: the co-sponsor rule is original and credible, but at risk of over-complexity | 5 |

### What would make Caplet stand out

Most strong teams will write "safe bucket + growth bucket" with a Monte Carlo "95%". Four things are distinctive here and still correct:
1. **Define certainty without using a model.** The payments are funded when assets are at least the Treasury-priced liability and each payment is matched to a bond held to maturity. Then use the 3–9% spread across four models as evidence of why a single Monte Carlo percentile is fragile. This is exactly what a statistics-trained client would value.
2. **Answer the case's "how should the reserve's composition change" question with a self-liquidating ladder.** The composition does not need active management. Add one sentence reconciling "economically locked in 2027" with "set aside in 2033", or a judge may think the case was misread.
3. **Put all the risk in the surplus, and say so plainly.** Laura's risk appetite is honoured where it cannot hurt the promise. The line that extra equity "buys range, not median" is backed by +$2–10k of median against −$26–29k at p5. A team that says this confronts the "too conservative" objection head-on.
4. **Make the 2031 range a rule the team will apply in 2031, not a forecast made today.** The floor is paid for, the stretch is stated with its model, and if the 2028 money never arrives the rule says "aspiration only". That speaks directly to the credibility criterion.

A stronger team would also cover what the debate barely touches: facility-cost inflation and TWD exposure, which the case asks about explicitly. It would also give one reasoned sentence on how much flexibility to keep after the facility contribution.

### Things that would hurt the team

- **Jargon.** DV01, Vasicek, AR(1), bootstrapping, no-arbitrage forward, covered interest parity, Solvency II, defeasance and LDI should not appear in the IPS. The IPS is 500 words with no charts, so translate the ideas into plain language. The technical detail belongs in the Final Report appendix.
- **Numbers the IPS doesn't need.** The instructions say the IPS need not carry calculations. Putting "$297k" or "96.7%" in it invites challenge. Use at most one rounded, sourced anchor.
- **Unsupported numbers.**
  - Every yield came from a search snippet. Primary pages were blocked.
  - The Solvency II 99.5% figure was cited from memory.
  - TWD volatility of 5–7% is unsourced.
  - Equity volatility of 16% is an assumption.
  - The Vanguard figures come in three versions.
  - The JPM and Vanguard CMAs are 2025 vintage, and the council didn't reconcile them with 5% yields.
  - The CIO models 4.0% bond returns while quoting yields of about 5%.
- **Overpromising.** "100%" and "guaranteed" need the qualifiers "barring US Treasury default" and "in nominal USD". The floor is not guaranteed in TWD or in real terms.
- **Inconsistency across deliverables.**
  - WInS "mirrors 65/35", but the strategy's 2027 state is about 99% bonds. Pick one framing now.
  - Trading Notes (due Oct 23) come before the IPS, but the IPS locks the strategy on Nov 6. The Notes must already use the IPS's vocabulary and rules.
  - Long-duration Treasury ETFs may lose money during WInS. Say that P&L is not the test.
  - Target-maturity ETFs may not be on the approved list. Starting capital and trade limits are unknown, and the 6-sector minimum is unverified. Confirm all of these on the WInS platform before placing the first trade.
- **A model bug.** The Actuary's curve code has no DF(0)=1 anchor. Its "$297k confirmed" is an artefact; the corrected figure is about $293.3k. The bug must not propagate.
- **AI-policy risk.** The debate contains ready-made slogans ("fund the promise first / grow the dream", "we bought the promise at $X", "floor plus stretch", the gauge visual) and Trading Note seeds. If these are pasted in, the submission is AI-generated work. The students should choose the architecture, redo the key calculations themselves, and write every sentence. They should also keep a decision log, which becomes their Articulation evidence.

### Numbers still disputed between members

| Item | Values in the debate |
|---|---|
| Ladder cost at 1/1/2027 | $293.3k (bug fixed), $294k (curve unchanged), $295.2k (CIO/Strategist recompute), $296.7k (Actuary, with the bug), $297.7k (par treated as zero) |
| Reserve cost in 2033 | $395.9–397.0k (forward curve) vs $404–405k (flat 5%) |
| Reserve cost at 2031 (L31) | $356.9k (forward) vs $364k (curve unchanged) |
| No-lock shortfall probability | 3.3% (Quant) / 4.4–6.8% (CIO) / 7.4–9.3% (Actuary). The spread is driven by each model's built-in rate drift. |
| Growth-sleeve equity | 50–60% (CIO, revised) vs 70% (Quant) |
| Median 2033 facility | $194–212k |
| 2031 floor rule | 0.55×S (a=50%), 0.66×S (60% locked), 1.10×S (100% locked), or 0.96×S (a 95% model percentile) |
| Vanguard US equity | 3.5–5.5% / 3.9–5.9% / 4.2–6.2% |
| 10y TIPS real yield | 2.653% (9/17 auction) vs 2.85% (9/25) |
| Curve points | 5y 4.98/4.99 (dates 9/23 vs 9/25 vs 9/26); 10y 5.17 vs 5.11; 30y 5.47/5.48/5.49 |
| USD/TWD | 31.79 (9/24) vs 31.73 (9/26); 2-year forward 30.07 vs 30.11 |
| Duration | DV01 $286/$291/$298; modified duration 9.8 vs 10.0 |
| Two-year equity loss probability | 35.9% (arithmetic mean) vs 31.8% (geometric) |
| Shortfall tolerance | 0.5%, anchored to Solvency II but unsourced |

**Recommendation to the team:** adopt architecture B in plain language. Verify one Treasury curve on a single date from treasury.gov or H.15, and use one sourced equity assumption. Re-derive the numbers yourselves before the Oct 23 Trading Notes.