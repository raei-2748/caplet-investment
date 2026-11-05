# R6 facts check (R3 Fact-Checker, Fri 6 Nov 2026, Sydney)

Counts (strict `textcheck.py`): **pitch 50 / 50, IPS 499 / 500: pass.**

## Must fix

| # | R6 words | Verdict | Fix |
|---|---|---|---|
| 1 | P1: "American public pensions … have spent two decades taking on more risk to keep up with it" | **STILL IN, still UNVERIFIED.** The Andonov, Bauer & Cremers abstract (*RFS* 2017) supports the mechanism only and gives no span of years (R5_facts #1; R6 Library) | "… whose accounting rules let them do exactly this, take on more risk to keep up with it." (−3 words) |

## Should fix

| # | R6 words | Verdict | Fix |
|---|---|---|---|
| 2 | P2: "If falling rates make it cost more than $300,000, **as they do today**" | **True on the 4 Nov close** ($300,608) and on 2 Nov, **false on 3 Nov** ($299,021), and the IPS is read weeks later. A dated fact stated as permanent present (FACTS N1) | "as they did in early November", or cut the clause (−5 words) |
| 3 | Pitch: "its interest buys world shares" | Loose: the shares are bought in 2028 with a sum roughly equal to the interest the fund will earn later. The IPS says it right ("roughly the interest it will earn") | Optional: "a sum near its interest buys world shares" |

## The 2027 "that day" overclaim (R5 #2): resolved
The IPS P1 still says "buys the Treasuries that will pay it that day", and the pitch says "the day she commits to it".
But both now disclose the top-up in the very next sentence: the pitch with "topped up in 2028 if needed", and P2
with "her 2028 deposit makes up the difference". That's honest. **Pass.**

## New in R6: checked, pass

| # | Claim | Verdict |
|---|---|---|
| 4 | P2: "Held to its end, each one pays out what its Treasuries repay, whatever markets do" | **Pass.** It is true for both the bonds and the funds (a fund's net assets at its end are its matured Treasuries, less a tiny fee). It doesn't claim a fixed sum |
| 5 | P5: "its bonds pay interest, and two repay months early" | **True.** Feb-2037 repays 10.5 months before Jan 2038, May-2038 repays 7.5 months before Jan 2039 (locked notes). The Nov bonds are about 47 days early, so "two" is right |
| 6 | P4: "she can be as confident of landing inside it as she is of Treasuries" | **Pass, strong but true by design.** After naming day both ends sit in Treasury holdings. The before-naming shortfall rule moves the range, not the payments. Never upgrade to "certain" or "guaranteed" (the harsh-world lock is 98.71%, FACTS N6) |
| 7 | P5: "If they can't, the rest comes out of the 2032 fund, and her range starts lower" | Consistent with the FINAL design ("she names a lower range") and the locked IBTR note (the top-up leaves less for the facility) |
| 8 | P1: "because future growth is expected to cover part of it. But that growth is a return nobody has earned yet" | Sound reasoning (this is the gap between an expected-return discount rate and a Treasury discount rate) |
| 9 | P3: "the late-2032 fund that pays her first January"; the "extra sets her minimum" | Matches the IBTM note's two jobs |
| 10 | P6: the reserve = ladder + the shortfall set-aside; "one holding is redeemed before each January" | Pass (redemption timing correct) |
| 11 | Never-say sweep | Clean |

**Gate verdict (facts): fails on #1 only.** It's a one-clause fix that saves words. #2 is strongly advised.
