# IPS Version 5: line-by-line edit sheet (17 Oct 2026)

AI-generated review (Claude Code) for Team Caplet. **No replacement wording.** Each row quotes a V5 passage, says
what is wrong, what the fix must achieve, and the fact to use. The students write every new sentence (Wharton AI
policy; CLAUDE.md working rules; `research/assistant_review_2026-10/supporting/ips_v5_review_merged_14Oct.md` s4, s7).
Log this file in the AI-use record. Source text: `team/google_drive/ips_report/01_version_5.md` (export of 14 Oct).

New since the 14 Oct review: the 2031 range numbers on the WInS-only basis (`research/range_2031/README.md`) and the
16 Oct curve, on which the ladder costs **$298,087** and the headroom under $300k is **$1,913 (about 7bp)**.

## Pitch (V5 line 16; 47 words; target 45 or fewer)

| V5 passage | Problem | The fix must... | Use |
|---|---|---|---|
| "co-sponsors who fund the building rarely pay to run it" | "rarely" is not in the case; the SSIR source backs only "under-fund running costs" | base the reason on the case rule: payments come from the portfolio alone | Client_Profile.txt:91-92 |
| "about $292,000 of Treasuries" | superseded 25 Sep idealised number; dollar figure in the pitch was voted against | remove the figure | 16 Oct cost is $298,087 and moving daily |
| "further Treasuries secure her minimum" | "secure" implies a fixed payout; the IBTM trade note says "the final payout is not fixed" | describe the floor the same way the IBTM note does | TNA note 10/06 10:01 PM |
| "Root-and-Branch" | name differs from COMPETITION.md ("Roots First") | use the one name the team votes (Set A) in TNA, IPS and Final Report alike | |

## Paragraph 1 (line 20): objectives

| V5 passage | Problem | The fix must... | Use |
|---|---|---|---|
| "each payment depends mainly on the US government paying its debts" | ignores coupon reinvestment and the non-fixed ETF payouts, which your own trade notes name | list the leftover risks honestly, in one short clause | holdings deliver ~$503k at today's yields, ~$466k if coupons earn 2% (rab/numbers.yaml, MODEL) |
| no definition of "high degree of certainty" | the case asks for a definition, how it was tested, and assumptions | state the standard (paid for at purchase by Treasuries held to maturity) and one test result | Client_Profile.txt:97-99 |
| "a floor Laura can promise co-sponsors" | "promise" + floor that can shrink = contradiction | say what the floor is (the 2028 remainder in a Dec-2032 Treasury fund) and that it is quoted rounded down | range_2031 README point 1 |

## Paragraph 2 (line 22): risk profile

| V5 passage | Problem | The fix must... | Use |
|---|---|---|---|
| "As a statistics graduate and entrepreneur she accepts measured risk" | a degree is not evidence of risk appetite | ground willingness in the case's words | "willing to take thoughtful risks", "an appropriate balance" (Client_Profile.txt:69-74) |
| "since the artists would bear the loss" | team inference presented as fact | label it as the team's reasoning or cut | |
| "we judge her tolerance above average" | unbacked; and <10% stock looks like low tolerance | explain that the stock share is what is left after both promises are bought, not a sign of low tolerance | mix after 2028 about 66% payments / 25% floor / 9% stocks |

## Paragraph 3 (line 24): construction

| V5 passage | Problem | The fix must... | Use |
|---|---|---|---|
| "At late-September 2026 yields they cost about $292,000" | stale; superseded basis | no number, or one dated figure on the WInS basis re-priced the week of 6 Nov | 6 Oct $292,327; 13 Oct $294,336; 16 Oct $298,087 (model, WInS-listed rungs) |
| "if falling yields push that above $300,000 before January, the 2028 deposit completes them" | right rule; now the likely case (about 44% of model paths; 7bp left) | keep the rule; make clear the floor then shrinks | a 0.5pt fall: top-up ~$13k, floor ~$136k |
| "a 2032 Treasury ETF sized to return that remainder" | "return" implies a fixed payout | say "aimed at" / match the IBTM note's "not fixed" (team's words) | |
| no mix, return objective, or trade-off | judges asked for all three | add the rough mix, the return the payments need, and the central trade-off once | required return ~5.1%/yr on $300k (MODEL) |
| "no dollar asset is safer" | sweeping claim | soften or support | |

## Paragraph 4 (line 26): hold and review

| V5 passage | Problem | The fix must... | Use |
|---|---|---|---|
| "held without trading" | contradicts the 2028 purchase | say held to maturity after the 2028 purchase | |
| "income reinvested in the holding that paid it" | WInS will hold iBond distributions as cash around 6 Nov (frozen book) | word the income rule so the frozen WInS book is consistent with it | COMPETITION.md s8 |
| shortfall order "2027 leftover, then the half Laura keeps, then the contribution above the floor" | never names the floor; the case says the range must protect the payments | complete the order so the payments rank above every facility dollar, floor included | Client_Profile.txt:119-120 |
| "Our WInS portfolio shows this allocation, scaled down" | drops "after both deposits" | say the WInS book is the plan after both deposits at about two-thirds scale | |

## Paragraph 5 (line 28): risks

| V5 passage | Problem | The fix must... | Use |
|---|---|---|---|
| "but never below the floor" | absolute; IBTM payout is not fixed | replace with a stated confidence, or the rule that makes it hold (rounding down) | gift never fell below the quoted bottom ($145k on a $150k floor) in 600,000 model paths, *given* the rounding and the cap |
| "the equity half Laura keeps is her defense" | fine in idea; size it | optionally give the bad-case cushion | Laura keeps ~$12k (bad case, p5) / ~$29k (median) |
| no inflation number | | one clause: payments are nominal so the ladder is unaffected; the floor buys ~12% less after 5 years at 2.5% inflation | 1/1.025^5 = 0.88 |

## Paragraph 6 (line 30): 2031 and 2033 rules

| V5 passage | Problem | The fix must... | Use |
|---|---|---|---|
| "quoted rounded down after any expected shortfall" | ambiguous (V5 vs Tab 15 meaning) | define "rounded down" once (Set A vote) | model: worst-case IBTM payout (~2.5% under), then down to $5k = $145k on a $150k floor |
| "to the floor plus half the equity fund's value then" | correct; the reason for "half" is weak | give the reason as Laura's cushion, not credibility: the share does not change the odds of reaching the top | P(reach top) ~74-76% at any share; cushion p5 $16k / $12k / $8k / $0 for 1/3, 1/2, 2/3, all |
| "so she cannot miss the range" | absolute | keep the logic (capped gift, owned floor) but drop "cannot" or name the conditions | conditions: 2028 deposit arrives; IBTM pays close to its yield; no ladder gap after 2031 |
| "missing a narrower one would harm her credibility more" | true in spirit but the stronger, checkable point is the two-odds statement | optionally state the confidence: top ~3 in 4, at least halfway ~99 in 100 (the IPS does not need final numbers) | IPS instructions :68-70 |

## Format, after the rewrite
Pitch 45 or fewer, IPS 485 or fewer by spaces (and with hyphens split). No figures, links or citations. Pages 2-3 only,
checked on the exported PDF. Title page names exactly as on the roster. Full list: merged review s6.
