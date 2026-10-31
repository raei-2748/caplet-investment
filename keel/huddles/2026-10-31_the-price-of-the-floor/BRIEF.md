# FICTION. H-005 The price of the floor (Genius Lab, Sat 31 Oct 2026, round 4 beat 5)

> Keel is a simulated team, AI-written. Chair: Felix (builder today). Members: **Felix** (builder), **Jun** (Lab head),
> **Kai** (roasts). Budget: 3 rounds x 3 members = 9 agent calls. Started from H-004's seed: "Does V36's
> floor-from-2028 actually beat A09's lock-in-2031 on our own model paths, and what does it give up?"

## The question (Q12, round 4)
**Why not a safe ladder and the rest in stocks?** The rival A09 (`../../ips_rewrite/rivals/A09.md`) buys the same
Treasury ladder for Laura's ten $50,000 cheques, keeps the 2028 deposit about 80% in world stocks, and buys the gift's
bottom in Treasuries only in 2031, when Laura names her range. Caplet XR (current draft V39,
`../../ips_rewrite/drafts/D19/ips.txt`) buys a Treasury floor with the 2028 deposit and puts only the floor's expected
interest (about a fifteenth of the portfolio) in stocks. Two of six blind mock judges put A09 first. V39 beats a 60/40
and a three-quarters-stocks plan in words; it never argues with A09. Wharton's own IPS question: "How does your strategy
balance growth, risk, liquidity, funding reliability, and financial flexibility?" (`../../WHARTON_WORD.md`).

## The test the Lab ran today (L-14, `../../rooms/lab/L-14_price_of_the_floor/run.py`, results.json)
MODEL: curve 22 Oct 2026, J.P. Morgan 2027 world stocks 7.5% a year, 200,000 paths, seed 20261016, same paths for both
plans. A09 at its strongest: given every XR rule (the 2031 mark, cushion, slide); after naming it keeps the same fifth
in stocks as XR (k = 0.8). Base world (S0) / recession-linked rates and stocks (S1):
| | XR (V39) | A09 |
|---|---|---|
| Cheque more than $1,000 short | 0.03% | 0.02% |
| Gift, typical (median) | $165k | $170k |
| Gift, average (mean) | $160k | $175k |
| Gift, best 1 in 20 (p95) | $180k | $257-260k |
| Bottom Laura can quote in 2031, typical / 1 in 20 low | $145k / $110-115k | $150-155k / $90-95k |
| Bottom below $100k | about 1 path in 100 | about 1 in 15-19 |
| In the worst 5% of 2028-30 stock markets: bottom / gift (median) | $135-140k / $150-155k | $90-95k / $100-105k |
| Top reached | 98% | 92% |
| Laura's own money in 2042 (median) | $38-39k | $36-37k |
**Premium test** (gift money alone, 2033): with stocks at 7.5%, A09 is $11-12k richer on average; with the same shocks
but stocks earning only the 2028 five-year Treasury yield, the gap is -$0.4k to -$1.0k. So A09's whole extra is the
stock premium: pay for carrying a crash in 2028-30. If yields fall 2 points after the build (S6), the floor costs more
(median gift -$10k, mean -$19k) and XR's stock slice shrinks to 1/24 of the portfolio. Halved 2028 deposit (S2): medians
equal, mean -$7k.

## Today's finds (Library, 31 Oct; verified quotes in `../../loop/rounds/2026-10-31.md` section 4)
Harvard slowed then paused its Allston science building in 2009 after its endowment fell about 30%; Yale and Princeton
shelved buildings "until funding is secured or market conditions improve"; UNC collects 100% in cash before a building
contract; public treasurers buy building money to mature by its drawdown date (GFOA); farmers forward-sell only what
they're sure to grow and lock more as the crop gets surer, but for a farmer the hedge is nearly free on average and for
Laura it isn't (J3). Window W-04: US giving "typically ... stays flat or falls in recession years" (Giving USA 2010).

## Rules
Wharton's word first (`../../WHARTON_WORD.md`), then the Ten Commandments (`../../BIBLE.md`): one paragraph-sized idea,
taken or dropped whole; every number says where it came from ("we modelled"); no "every team will"; Caplet XR is
subtle. Talk like yourself (`../../VOICE.md`), short. Fiction never enters a Caplet deliverable; the numbers are real
MODEL output.
