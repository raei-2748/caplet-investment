# FICTION (the room) + real work. L-04: do the two claims on Laura's half arrive together?

Run Sat 24 Oct 2026 (Sydney, evening) by Jun, four days early (due Wed 28 Oct; Laura's Room request, 24 Oct). Kai
roasted first. HISTORY + MODEL. Criterion: Investment Strategy (balance); Client Knowledge (flexibility); the case asks
for "assumptions about ... the effect of inflation" (`Laura_Gao_2026_Client_Profile.txt`:146-147).

1. **Hypothesis.** A payment shortfall (yields fall and stay down while coupons are reinvested) and a facility cost
   overrun (fast inflation between the 2031 quote and the 2033 gift) rarely arrive together, so the half Laura keeps
   backs two risks that seldom strike in the same years.
2. **Kai's roast.** "2022. Inflation at forty-year highs and bonds getting smashed in the same year. Your 'rarely' is
   one chart away from embarrassing."
3. **Test.** `L-04_two_risks_run.py` on Shiller monthly GS10 and CPI (`archive/rab/data/history/shiller_monthly.csv`),
   January values. For each start year Y (= 2027): shortfall if the average 10-year yield over Y+1..Y+14 is at least
   1 point below Y; overrun if CPI rises more than 3.5% a year from Y+4 to Y+6 (2031 to 2033). Wrong if the joint rate
   is at or above what independence gives.
4. **Result** (`L-04_results.json`).
   | Sample | P(shortfall) | P(overrun) | Both | Both if independent | Overrun given shortfall | Overrun otherwise |
   |---|---|---|---|---|---|---|
   | 1954-2011 (58 start years) | 43% | 38% | **8.6%** | 16.3% | **20%** | **51.5%** |
   | 1871-2011 (141 start years) | 23% | 29% | 5.0% | 6.8% | 21% | 31% |
   Correlation of yield change with quote-to-gift inflation: +0.42 post-war, +0.22 full sample. Limits: overlapping
   windows (post-war is roughly four independent 15-year episodes, dominated by the 1981 peak), US CPI not Taiwan
   building costs, and Kai's 2022 is inside neither test window's tail because the yields that fell for good after it
   have not been seen yet.
5. **Verdict: ADOPT for the Final Report, BIN for the IPS.** The pattern is real and points the right way (post-war,
   about half as often together as chance), so the Final Report can say the kept half backs two risks that seldom
   arrived together "in US history". The Courtroom struck it from the IPS: no citation is allowed there, so "who
   says?" has no answer in 500 words (`L-05_ips_push/courtroom.md`, C6). Kai's roast half-stands: "rarely" is too
   strong for 1871-2011; "less often" is the honest word.
