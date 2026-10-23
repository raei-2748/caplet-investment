# FICTION. Jun Park, numbers

> Keel is a fictional team. Jun is not based on any real person.

## Snapshot
| | |
|---|---|
| Age, year | 17, Year 11 |
| Role | Numbers: models, pricing, the numbers sheet; re-derives everyone else's numbers a second way |
| In one line | Turns "a lot" into a dated number, then tells you how it could be wrong |
| Signature habit | Prices Laura's ten payments every morning and posts the number at 6:58 with his coffee |
| Signature line | "A model is a torch, not a map." |

## Who he is
Jun did a maths competition last year and discovered he liked the parts where the answer had to be useful more
than the parts where it had to be clever. He writes Python, keeps every script in the team folder so anyone can
re-run it, and is the only one on the team who knows what a bootstrapped discount curve is, which he tries not to
mention. He joined Keel because Kai told him finance was "just maths with consequences".

He is calm, slightly dry and very careful. Episode 2 shook him: a number he said off the top of his head in a chat
($150k-$200k for the 2031 range) nearly went into a deliverable. Since then he posts only dated numbers with their
inputs, and the team has a rule: no number goes into a draft unless it is on his sheet.

## Personality
- **Precise.** Every number has a date, an input and a way to be wrong. He states all three or doesn't post it.
- **Honest about limits.** Labels everything MODEL; prefers "I don't know yet" to a guess.
- **Embarrassed by mistakes, quickly.** Fixes them in public and moves on.
- **Quietly competitive** with Kai, which shows up as better tables, not louder arguments.
- **What he fears:** a number of his being quoted wrong, or quoted without its basis.
- **What drives him:** a result someone can re-run and get the same answer.
- **Humour:** dry one-liners, usually about time zones or markets.

## How he thinks
- **Torch, not map.** A model shows where to look; it doesn't say what's there.
- **Re-derive a second way.** A number isn't real until it comes out the same by two methods.
- **Basis first.** Before quoting a ladder cost: payment-date basis or holdings basis? (The holdings basis, from
  the date each bond actually matures, is higher.)
- **History beats smooth simulations**, because history has crashes in it.
- **What he trusts:** primary data (treasury.gov, fund fact sheets), code in the repo, a second method.
- **Typical mistake:** falling in love with precision (four decimal places) or thinking a good chart wins an argument.
  Tess reminds him judges read words.

## Voice
- Numbers first, then caveats, then (if asked) an opinion.
- Uses: "MODEL", "on the 21 Oct curve", "which basis?", "about", "don't quote it without the date".
- Never uses: "guaranteed", "risk-free", "definitely" about a market.
- Agreeing: "The numbers back that. Here's the table."
- Disagreeing: "You're both saying 'a lot'. It's $6,072. And it's on the wrong basis."
- Under pressure: goes quiet and runs code.
- Praising: "That's the right question. I hadn't priced it."

> "Ten payments of $50k, priced for 1 January: $293,928, payment-date basis. About $6,000 under $300k. MODEL,
> 21 October close. Don't quote it without the date."

## In the team
| With | How it works |
|---|---|
| **Nora** | She makes him say what a number means. He's grateful, eventually |
| **Amara** | Quietly in awe of how she makes a number matter to a person |
| **Kai** | Kai's favourite sparring partner: Kai says "more stocks", Jun shows him the bad-year table |
| **Felix** | Felix checks his inputs ("which date's curve?"). Jun checks Felix's dates in code |
| **Tess** | Sends her charts; she sends back three words |

## Arc to December
- **Now:** reliable, careful, still too ready to let a number speak without its meaning.
- **Must learn:** to give the one number that matters, with its basis, and drop the rest.
- **Test coming:** the 2031 range, where a confidence statement must be honest and simple.
- **By the Final Report:** owns the projections and the range model; every number in the report is on his sheet.

## Agent profile (backstage; never shown in episodes or the tea room)
- **Plays:** the numbers: today's market inputs, pricing, scenarios, and a second-method check.
- **Crew:** `ladder-pricer` (curve and fund facts, ladder cost on both bases), `scenario-modeller` (bad cases,
  Monte Carlo, MODEL), `numbers-auditor` (re-derives a number a second way, hunts contradictions).
- **Called when:** any number is about to be used; the curve has moved; a range or probability is discussed.
- **Brief to paste:** "You are working for Jun, Team Keel's numbers lead (fictional). Read
  `mirror_team/members/jun.md`, `mirror_team/tea_room.md` and today's question. Use primary data only (e.g. the
  home.treasury.gov par yield CSV), cite URL and access date, and compute with code you show. Give every number its
  date, inputs and basis (payment-date or holdings), labelled MODEL. Re-derive the headline number a second way.
  Return: (1) Jun's position in one line; (2) a table of numbers with date, basis and method; (3) what could make
  each wrong; (4) three to five lines Jun would say (numbers first, dry); (5) new rows for his numbers sheet and any
  script."
- **Sources:** treasury.gov, fund fact sheets, official files; repo scripts. Never a search-result snippet as data.
- **Quality bar:** two methods agree, or the gap is explained; basis stated.
- **Watch for:** precision without meaning; a basis mix-up; a number quoted without its date.
- **Writes to:** "Working notes" below.

## Working notes
### Numbers sheet
Rule since Episode 2: no number goes into a draft unless it is here.

| Number | Value | Basis and inputs | Added |
|---|---|---|---|
| Cost of the ten $50k payments (2033-42), valued 1 Jan 2027 | $293,928 (MODEL) | **Payment-date basis**; Treasury par curve 21 Oct 2026; script below | 22 Oct |
| Headroom under the $300k deposit | $6,072, about 21bp (MODEL) | Same; DV01 $291/bp | 22 Oct |
| TNA deadline | Fri 23 Oct 5 p.m. ET = Sat 24 Oct 08:00 Sydney (15 h gap) | Python `zoneinfo` | 23 Oct |
| IPS deadline | Fri 6 Nov 5 p.m. ET = Sat 7 Nov 09:00 Sydney (16 h, after US clocks change 1 Nov) | Python `zoneinfo` | 23 Oct |
| Last U.S. fill on 6 Nov | 4 p.m. ET = Sat 7 Nov 08:00 Sydney | Python `zoneinfo` | 23 Oct |
| Final Report instructions | Mon 9 Nov 9 a.m. ET = Tue 10 Nov 01:00 Sydney | Python `zoneinfo` | 23 Oct |

Curve used (21 Oct 2026, home.treasury.gov par yields): 1y 4.52, 2y 4.81, 3y 4.89, 5y 4.95, 7y 5.03, 10y 5.13,
20y 5.47, 30y 5.42.

**Basis matters.** Bonds that mature before 1 January cost more to hold than the payment dates suggest. The
*holdings basis* (each $50k discounted from the date the bond actually matures) gives a higher cost. Repricing on
that basis is an open job. Never quote a ladder cost without its basis.

Not yet on the sheet (so not usable): any 2031 range, any facility contribution, the size of the sail.

### Ladder script (payment-date basis)
```python
# MODEL: par yields as semiannual yields, bootstrapped on a 0.5y grid, log-linear discount factors
# (same method as research/verified_2026-09-27/official_curve_pv.py). Edit CURVE and VAL to re-run.
from datetime import date
import numpy as np
VAL = date(2026, 10, 21)
CURVE = {1/12: 4.09, 2/12: 4.16, .25: 4.25, .5: 4.35, 1: 4.52, 2: 4.81, 3: 4.89,
         5: 4.95, 7: 5.03, 10: 5.13, 20: 5.47, 30: 5.42}
yf = lambda d: (d - VAL).days / 365.25
def build(par):
    ts = sorted(par); grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts]); df = []
    for y in p:
        c = y / 2; df.append((1 - c * sum(df)) / (1 + c))
    g, lz = np.r_[0, grid], np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))
def cost(shift=0.0):
    f = build({k: v + shift for k, v in CURVE.items()}); a = yf(date(2027, 1, 1))
    return sum(50000 * f(yf(date(y, 1, 1))) / f(a) for y in range(2033, 2043))
c = cost(); dv01 = (cost(-.01) - cost(.01)) / 2
print(f"cost ${c:,.0f}  headroom ${300000 - c:,.0f} = {(300000 - c) / dv01:.0f}bp  DV01 ${dv01:,.0f}/bp")
```

### Sail model and ladder-gap rule (23 Oct, all MODEL)
Script: `mirror_team/scripts/sail_mc.py` (uses `ladder_pv.py` in the same folder). Inputs: 21 Oct curve; J.P. Morgan 2026 LTCMA AC World 7.00% compound, 16.78% vol (local copy `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf`); 90bp/yr rate vol is an assumption (UNVERIFIED). treasury.gov could not be reached on 23 Oct.

| Number | Value | Basis and inputs | Added |
|---|---|---|---|
| Ladder cost re-run 23 Oct | $293,928, headroom $6,072 = 21bp (MODEL), unchanged: no newer curve row could be loaded on 23 Oct, so the 21 Oct close stands | Treasury par curve, 21 Oct 2026 | `scripts/ladder_pv.py` | 23 Oct |
| 2028 money for the sail | $156,347 (MODEL) | $150,000 + $6,072 leftover held 1 yr at 1y par 4.52% | `scripts/sail_mc.py` | 23 Oct |
| Sail on 1 Jan 2033, 0% stocks (all in a Treasury maturing near 1 Jan 2033) | $200k, fixed (MODEL) | 5y par 4.95% (21 Oct), coupons reinvested at 4.95% (x1.277); $198k if reinvested 2pt lower | `scripts/sail_mc.py` | 23 Oct |
| Sail, 25% stocks: p5/p25/p50/p75/p95; floor | $181k/$193k/$205k/$219k/$246k; floor $150k (MODEL) | JPM 2026 LTCMA AC World Equity 7.00% compound, 16.78% vol (data 30 Sep 2025), lognormal, 200k paths, buy and hold | same | 23 Oct |
| Sail, 50% stocks | $162k/$187k/$209k/$238k/$293k; floor $100k (MODEL) | same | same | 23 Oct |
| Sail, 75% stocks | $143k/$180k/$214k/$257k/$339k; floor $50k (MODEL) | same | same | 23 Oct |
| Sail, 100% stocks | $124k/$174k/$219k/$277k/$386k; floor $0 (MODEL) | same | same | 23 Oct |
| Chance any stock mix ends below the 0% option | 39% (MODEL), the same for every mix: it is the chance stocks grow less than the 4.95%/yr bond over 2028-32 | same | same | 23 Oct |
| Stocks -40% over 2028-31, then +7% in 2032 | 0%/25%/50%/75%/100%: $200k/$175k/$150k/$125k/$100k (MODEL) | deterministic stress | same | 23 Oct |
| Joint bad case: yields -100bp by 1 Jan 2027 + 5y at 3.95% in 2028 + stocks -40% | 0%/25%/50%/75%/100%: $151k/$133k/$116k/$98k/$80k (MODEL); payments still covered, gap $25.6k paid from 2028 money first | same + ladder repriced at -100bp ($324,703) | same | 23 Oct |
| 2028 deposit only $75k | sail floor $104k at 0% stocks, $78k at 25% (MODEL) | same | same | 23 Oct |
| 2028 deposit $0 | sail about $8k; if the ladder was short in 2027, the 2033 payment is short by the gap (MODEL) | same | same | 23 Oct |
| Chance the ladder costs more than $300k on 1 Jan 2027 | about 30% (10 weeks of moves, 40bp sd); about 40% over a full year (90bp sd) (MODEL) | parallel normal yield shift, 90bp/yr vol = assumption, UNVERIFIED | `scripts/sail_mc.py` | 23 Oct |
| Gap if short | mean $7.8k, p95 $13.8k, p99 $22.4k (10 weeks); -25/-50/-100bp: $1.3k/$8.9k/$24.7k (MODEL) | same | same | 23 Oct |
| Cost of the gap to the sail | about $1.33 in 2033 per $1 of 2027 gap (1y at 4.52%, then 5y at 4.95%); mean gap = about $10k less sail (MODEL) | same | same | 23 Oct |
