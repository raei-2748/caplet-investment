# R63 review (e): facts and the locked record
AI-generated review (Claude, 6 Nov 2026). Not submission text.

`ladder_pv.py` re-run on every 2026 close. **Nothing contradicts a submitted note or reflection.**

| Claim | Verdict | Evidence | A true version must convey |
|---|---|---|---|
| ips:1 "buy each promise before she makes it"; pitch "buys its repayment ... beforehand" | TRUE | Bought 2027-2031, before naming (A33 `archive.md:101`) | - |
| ips:1 "...which makes them a debt" | STRAINS (mild) | Facts true (case L90-92); the case says "commitment" (L87, L120) | They behave like a debt, so the plan treats them as one (the pitch's "treats") |
| ips:1 "ten Treasury holdings her first $300,000 buys in January 2027" | HALF-TRUE | 23 Oct $297,636 (`00_GROUND_TRUTH.md:87`), actual holdings a little over $300k (`02c:236`, `:260`); ips:5 allows a top-up | Buys the ten, or nearly all |
| ips:1 "one in the year before each payment" | TRUE | Notes `05_...md:15-24` | - |
| ips:3 balanced mix "probably richer by 2042" | TRUE (MODEL) | 60/40: $229k-$285k left in 2042 v XR $31k-$56k (`models/README.md:73`) | No number |
| ips:3 "about two thirds of her $450,000" | TRUE | Re-run: 66.1% on 23 Oct; 64-72% on every 2026 close | - |
| ips:3 facility "only what was left over" | TRUE, not a contrast | Case L101-102: true of XR too | The difference is the swing |
| ips:3 heavily borrowed company | TRUE in direction | Unmodelled; rough check: a 60/40 leftover moves ~2x the share market | Holds for a share-heavy mix; no number |
| ips:5 five funds, one calendar year, December payout, "no individual Treasury for some of those years" | TRUE | `casestudy_pack.md:55`, `:78`; WInS none 15 Feb 2031-15 Feb 2036 (`wins_notes.csv:18`) | "Some" is exact; never "all five" |
| ips:5 2028 deposit "first covers anything the ten cost above $300,000" | TRUE | IBTR note `:15`, IBTO `:20` | - |
| ips:5 "...enough more of the fund ... to return about $150,000" | **HALF-TRUE** | Every model sizes the floor at the deposit **less** any top-up: `ips_numbers.py:182-183`; `range_2031/README.md:23`, `:54-58` (0.5-point fall: ~$136k); `02c:270` | What is left of $150,000 after any top-up |
| ips:5 rounded down, "payout isn't fixed" | TRUE | IBTM note `:19`; `02c:248` | - |
| ips:7 interest early, "weeks or months", near-zero rates leave the ten short | TRUE | `02c:241-243`; notes `:16-18` | - |
| ips:7 "earn nothing ... nobody has to forecast rates"; half her shares into Treasuries before naming | TRUE (tested) | KW lock, every payment in full (`L-17_...md:56`); A19 `archive.md:87` | Zero isn't a hard floor (bills briefly negative 2008, 2020; model floors 0.25%, `:71`): never "the worst case" |
| ips:7 shortfall "comes out of the bottom, moving the whole range down" | TRUE | `L-17_...md:37`; A33 | - |
| ips:9 "Co-sponsors will plan around its top, and missing it would cost her the credibility" | **STRAINS (case)** | Case L114-118: the risk is promising "more than she can ultimately contribute"; the test is "within that range". Clashes with ips:13 | The risk is a top markets could still take after she names it; co-sponsors "may" lean on it |
| ips:9 "top is the bottom plus what they fetch" | TRUE | T16 `02c:249`; A27 `archive.md:95` | - |
| ips:9 "barring a US default, no payment waits on shares, interest rates or an early sale" | TRUE, with the cover | T12 `02c:245`; A33 | Rests on the 2028 deposit arriving (halved: 98.71%) |
| ips:11 income and giving "can" shrink | TRUE | "can" is the ceiling (`02c:261`) | - |
| ips:13 "at least the bottom" | TRUE | No payment draws on the gift after naming (`L-17_...md:56`) | - |
| ips:13 "how close to the top depends on ... the building's cost" | **STRAINS** | Untested rule: the tested design reaches the top 99.3% (`L-17_...md:56`); VT note: shares "only set how far her gift rises" | Who sets the 2033 gift and why (case L101-102), without undoing ips:9 |
| ips:13 unpromised rest; reserve shrinks yearly | TRUE | Case L94-97 | - |
| ips:13 "the debt she paid for in 2027" | HALF-TRUE | Same draft: 2028 top-up, 2031 cover | Paid before she named the range |
| pitch "Her first $300,000 does that for her ten ... payments" | **HALF-TRUE** | A24 `archive.md:92`: never say 2027 money alone secures every payment | Buys (nearly all of) the ten; the 2028 deposit finishes them |
| pitch 2028 deposit and half its shares "fund both ends" | TRUE | Bottom = its fund; top = bottom + promised half | - |

## What the locked record and the case need that R63 lacks
1. **How certainty was evaluated** (case L97-99): the deletion test (every share gone, waiting money earning nothing: no payment worse off; T12).
2. **Assumptions** (L98-99, L146-149): the 2028 deposit arrives in full; US Treasuries pay.
3. **Confidence basis** (L117-118): both ends owned before she names the range.
4. **Liquidity**: reflection 2's trade (C6); the form asks for it.
5. **A top-up lowers the bottom** (row above).
6. Optional: early money's home (a short-term Treasury fund, never "cash"); the replacement rule (A4); the good-market path.
