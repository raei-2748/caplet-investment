# L-18 The same downturn (Genius Lab, Wed 4 Nov 2026, round 8 beat 5; huddle H-030)

(Keel is a simulated team, AI-written. MODEL throughout: 22 Oct 2026 Treasury par curve, J.P. Morgan 2027 global
equities 7.5%, 200,000 paths, seed 20261016, rho 0.5, V54's design through the L-13 -> L-17 chain and the Courtroom's
exhibit N, scored on the final IPS's lock words, "as if every dollar waiting for a cheque earned nothing" = exhibit N's
KWN-w arm. Never an IPS number: Book 11. Script `L-18_the_same_downturn/run.py`, results `L-18_the_same_downturn/results.json`.)

**For a judge, first.** The final IPS warns that Laura's income "can dry up in the same downturns that hit share
prices". We put that warning against our own plan. Because her first $300,000 holds no shares, a downturn in 2027 can
only shrink the 2028 deposit; it can't also hit shares she doesn't yet own. In the model, with the deposit halved and
interest rates down two points for good, every cheque is still paid in 9,996 futures in 10,000, and the damage lands on
the building gift. The cheques never lean on shares in any world we tried. They do lean on the 2028 deposit arriving:
with no deposit at all, the same downturn leaves a cheque short in four futures in five.

## Hypothesis (the chair, before the test)
In a 2027 downturn (rates down for good, deposit cut), every cheque is paid under the final lock and the damage lands
on the gift, because the plan's order (ladder first, shares only from what the deposit leaves) means the downturn can
hit her income or her shares, never both at once.

## Kai's roast (written blind, `../../huddles/2026-11-04_the-look-alike-card/posts/r1_kai.md`)
"Weaker than it sounds." (1) Shares bought in 2028 sit until 2031, so a 2029 slump still hits the shares the lock is
moved out of; the test only covers 2027. (2) The WInS book holds VT bought with the simulator's $300,000, so a judge
sees shares in 2027 beside a line saying there aren't any. (3) Falling rates are the real shared hit. **Sealed
prediction: deposit halved, rates down for good, cheques paid in full in about 94% of futures.** Proven wrong if any
cheque is short with the deposit halved, or if the damage lands on the cheques, not the gift.

## Test
Four worlds added to exhibit N's machinery (its patch chain copied, its file untouched): rates fall two points just
after the January 2027 build and stay down (the 2027 downturn), with the deposit at $112,500, $75,000, $50,000,
$25,000 and $0; and Kai's point (1), the $75,000 world with shares halving again before the range is named. Reference
rows from exhibit N, not re-run. S10 re-run from a clean start: identical.

| World (MODEL, KWN-w = the final IPS's lock) | Every cheque in full | Short, median / p90 when short | Her kept shares all gone | Gift mean |
|---|---|---|---|---|
| Rates down 2 for good, full deposit (exhibit N S6) | 100% | none | 78.2% | $139,045 |
| ... deposit a quarter short ($112,500) | 100% | none | 85.0% | $95,953 |
| ... **deposit halved ($75,000)** | **99.96%** | $2,188 / $8,290 | 90.9% | $52,578 |
| ... halved, **and shares halve before naming** (Kai's 2029 slump) | **99.96%** | $2,256 / $7,988 | 95.4% | $46,693 |
| ... deposit $50,000 | 96.00% | $5,635 / $15,825 | 94.0% | $23,415 |
| ... deposit $25,000 | 66.76% | $12,989 / $29,835 | 96.6% | below zero |
| ... **no deposit** | **18.46%** | $27,180 / $52,089 | all | below zero |
| Rates 1 lower before the build, deposit halved (exhibit N S9) | 98.28% | $5,980 / $17,550 | 95.2% | $33,422 |

## Result
- **Kai's prediction (94%) was too gloomy: 99.96%.** The hypothesis holds where the deposit is at least half: the cheques
  stay whole and the gift and her kept shares take the hit. Kai's 2029 slump changes no cheque (99.96% both ways); it
  costs the gift about $5,900 more on average, which is the lock doing its job: kept shares first, then the range.
- **"No payment depends on shares" survives every world here.** What a cheque does depend on, in the worst world, is
  the 2028 deposit arriving: with rates down for good, cheques start falling short once the deposit drops below about
  half (1 future in 25 at a third of it, 4 in 5 with none). A
  pre-build rate fall with a halved deposit (S9) is worse than the 2027 downturn (98.28% v 99.96%), because then the
  deposit must first complete a dearer ladder.
- Kai's point (2) stands and is already open for the Final Report (the simulator's VT; FRONTIER F24).

## Verdict
**ADOPT for the Final Report, no IPS change.** Portfolio Analysis ("reasonable assumptions and projections to evaluate
funding reliability"): one sentence and this table, "our cheques depend on the government and, in the worst world, on
her 2028 deposit arriving; in no world we tested do they depend on shares." The order argument ("she owns no shares
until her income has landed") is the Investment Strategy line behind P5 of the IPS. For Caplet's rewrite, one row on
the look-alike card (the 2028 deposit never carries a cheque is false). Headline to the Window to re-derive (S10, S11).
