# R7 facts check (R3 Fact-Checker, Fri 6 Nov 2026, Sydney)

Counts (strict `textcheck.py`): **pitch 50 / 50, IPS 497 / 500: pass.**

## Must fix (gate fails until these are in)

| # | R7 words | Verdict | Fix |
|---|---|---|---|
| 1 | P1: "American public pensions, which are allowed to do exactly this, have spent two decades taking on more risk" | **STILL IN, still UNVERIFIED** (third round). The source (Andonov, Bauer & Cremers, *RFS* 2017) gives the mechanism, not a span | "… which are allowed to do exactly this, take on more risk to keep up with it." (−3) |
| 2 | P6: "From 2033 the ladder and that set-aside become her operating reserve, and **nothing in it is ever sold**" | **False.** The waiting money must be sold to pay a January. The Feb-2037 and May-2038 proceeds "stay in a short-term Treasury ETF" (locked notes) for 10.5 and 7.5 months, and that ETF is sold to make the 2038 and 2039 payments. The set-aside is also spent, not just held | "and nothing in it is sold before its end date" (+2) or "and no holding is sold early" (+0, with "ever sold" out) |
| 3 | P3: "a crash in 2029 or 2030 can shrink the top of her range but **never its bottom**" | **False in one combined case.** A crash shrinks the kept half. If rates also fall, that smaller half covers less of the shortfall, and P5 says "the rest comes out of the 2032 fund, and her range starts lower". The bottom does move. That's also on the never-say list ("never below the bottom") | "a crash in 2029 or 2030 on its own can shrink the top of her range, not its bottom" (+2) |

## Checked, pass

| # | Claim | Verdict |
|---|---|---|
| 4 | P3: "Her 2028 deposit first fills any gap falling rates have left in the ladder – **at today's rates, a small one**" | **True on the latest close.** On 4 Nov the gap is $608 (payment-date basis) or about $3.9k (holdings-forward basis); on 3 Nov it was nil. The 5 Nov close isn't published yet. "a small one" holds whether the gap is zero or a few thousand, so it's robust. It's still a dated present tense read weeks later; "at early-November rates" is safer, but not a stop |
| 5 | P5: "two repay months early" | **True.** Feb-2037 is 10.5 months before Jan 2038; May-2038 is 7.5 months before Jan 2039. The Nov bonds are about 47 days, so "two" is right |
| 6 | P3: "Buying the minimum in 2028, not 2031, gives up some growth. But it is the last money Laura adds" | **True.** The case has nothing else coming in before 2033, and less money in shares means less expected growth |
| 7 | P7: "markets can change how large a range Laura names, but never whether she meets a payment or a number already named" | **Strong, holds on the case's facts.** Payments sit in Treasuries held to their end; after naming, both ends are in Treasuries. The only modelled misses (98.71% paid in full) come from a *halved* 2028 deposit plus rates 1pt lower (FACTS N6), which is outside the case's fixed $150,000. Keep it (Book 5: no hedging). Never "guaranteed" |
| 8 | P2: "each pays out what its Treasuries repay, whatever markets do" | Pass (R6 #4) |
| 9 | P4: "as sure of landing inside it as of Treasuries" | Pass (R6 #6) |
| 10 | Pitch: "its interest buys world shares" | Loose (the shares are bought in 2028 with a sum near the interest the fund will earn later); the IPS P3 says it right. Optional |
| 11 | Never-say sweep | "never its bottom" (#3) is the only hit. No ticker, printed range, STRIPS, TIPS, CPPI, immunise, floor, guaranteed, risk-free |

**Gate verdict (facts): fail on #1-#3.** All three are clause-level fixes that net about +1 word, so it still fits.
