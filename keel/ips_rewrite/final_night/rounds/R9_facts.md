# R9 facts check: the last check (R3 Fact-Checker, Fri 6 Nov 2026, Sydney)

Counts (strict `textcheck.py`): **pitch 50 / 50; IPS 496 by spaces, 500 split on hyphens: pass, no word to spare.**
Scope: every sentence re-checked, plus a full never-say sweep. The R8 passes still stand where the text is unchanged
(R8_facts.md #4-#13).

## Must fix (one clause, regression of R7 #3)

| # | R9 words | Verdict | Fix (saves a word) |
|---|---|---|---|
| 1 | P5: "Falling shares before 2031 can lower only the top, and rising shares lift it." | **R8's "on its own" has gone, so the absolute is back.** If shares fall *and* rates stay low, the smaller kept half can't cover the waiting-money gap, and P6's own rule takes the rest from the 2032 fund, so "her range starts lower". Falling shares then *do* help lower the bottom. P6 discloses this two sentences later, which makes P5 contradict P6 | "Falling shares alone, before 2031, lower only the top; rising shares lift it." (12 words, against 13 now) |

## Changed since R8: checked, pass

| # | Claim | Verdict |
|---|---|---|
| 2 | P1: "Pricing a fixed sum at what shares usually earn makes it look cheaper, because it counts growth that hasn't happened yet." | Sound (an expected-return discount rate against a Treasury one) |
| 3 | P1: "American public pensions are allowed to price their promises that way, and they have taken on more risk to keep up." | **True.** US public plans may discount at expected return (GASB 67/68). Andonov, Bauer & Cremers (*RFS* 2017) find they "act on their regulatory incentives" and take more risk. No span claimed |
| 4 | P2: "Each holding, kept to its end, pays out what its Treasuries repay, whatever its price does meanwhile." | Pass (bonds: par; funds: net assets of matured Treasuries; no fixed sum claimed) |
| 5 | P3/pitch: "Roughly the interest they will earn" / "roughly its interest" | True (about $32k of interest; VT p50 $30.9k, FACTS N4/N8) |
| 6 | P6: "interest and early repayments sit for months before their January, earning less than planned if rates fall and stay low" | True (Feb-2037: 10.5 months, May-2038: 7.5 months; the coupons in between) |
| 7 | P6: "move enough of the half of her shares she kept into Treasuries … If that falls short, the 2032 fund covers the rest and her range starts lower." | Consistent with the FINAL design and the locked IBTR note |

## Unchanged since R8 (re-read, still pass)
Living costs outside the portfolio (case l.61-63) · dollar Treasuries for payments "not adjusted for inflation" (case
l.90; TNA reflection 1) · "can shrink in the same recessions" (keep "can") · the 2032 fund's two jobs (IBTM note) ·
bottom "rounded down because a fund's final payout isn't fixed" (IBTM note) · "as sure of landing inside it as of
Treasuries" · financial flexibility wording (case) · "never whether she meets a payment or a number already named"
(holds on the case's fixed deposits; the only modelled misses come from a halved 2028 deposit, FACTS N6) · "no
holding is sold early" · "one holding is redeemed before each January" · "the tenth redemption pays the last $50,000
in 2042" (Nov-2041 bond, for Jan 2042) · pitch: "topped up if needed", "secures", "owned before she names it".

## Never-say sweep (full)
Searched for: risk-free, guarantee(d), STRIPS, TIPS, CPPI, portfolio insurance, immunise/immunize, duration(-matched),
floor, cheques, building gift, promises (as a label), never below, T-bills/bills, cash as the parking place, tickers
(IBT*, VT), printed range/dollar model figures/percentages, "two decades", "ever sold", "in January" for redemptions,
"pays exactly" for funds, "rides on", "risk-free".
**Hits:** "exactly" once, in "dollar Treasuries match them exactly". That's the inflation basis only, and it matches
reflection 1 ("matches the liability perfectly"), so it passes. "promises" appears once as an ordinary verb-object
("price their promises"), describing the pensions, not as a coined label for Laura's payments, so it passes. No other
hits. Numbers printed: $300,000, $50,000, years. All are case facts.

**Gate verdict (facts): PASS once fix 1 is in.** It saves a word (IPS goes to 499 strict). Without it, a careful
reader finds P5 and P6 disagreeing.
