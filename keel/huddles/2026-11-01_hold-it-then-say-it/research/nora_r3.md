# FICTION. H-010 round 3, Nora's counts (Sun 1 Nov 2026)

> Keel is a simulated team, AI-written. Tool: `keel/office/tools/textcheck.py` (strict = the larger count). Texts are
> AI DRAFT (Claude, 1 Nov 2026). Word rule: IPS at most 497 strict. Post: `../posts/r3_nora.md`.

## V47 P7 (as it stands)

```
$ python3 keel/office/tools/textcheck.py - <<< "paragraph"
A capped range has a catch: once named, every fall in stocks comes off the gift while every rise past the top goes to Laura. On the day she names it, the half she promised moves into Treasuries, and in our model the gift reaches its top about 97 times in 100.
---
words: 52 by spaces (a spaced dash counts), 52 split on hyphens; quote the larger
characters: 259
non-ASCII characters: 0
```

## (i) A only

```
$ python3 keel/office/tools/textcheck.py - <<< "paragraph"
A capped range has a catch: once named, every fall in stocks comes off the gift while every rise past the top goes to Laura. Before she names it, the half she'll promise moves into Treasuries, and in our model the gift reaches its top about 97 times in 100.
---
words: 50 by spaces (a spaced dash counts), 50 split on hyphens; quote the larger
characters: 257
non-ASCII characters: 0
```

## (ii) A + C

```
$ python3 keel/office/tools/textcheck.py - <<< "paragraph"
A capped range has a catch: once named, every fall in stocks comes off the gift while every rise past the top goes to Laura. Before she names it, the half she'll promise moves into Treasuries. In our model the gift lands within the range in all but one of 600,000 paths across three worlds, and at its top about 97 times in 100.
---
words: 64 by spaces (a spaced dash counts), 64 split on hyphens; quote the larger
characters: 328
non-ASCII characters: 0
```

## P9 clause that would pay for (ii)

```
$ python3 keel/office/tools/textcheck.py - <<< "paragraph"
and it runs itself down: each turns to cash before its cheque.
---
words: 12 by spaces (a spaced dash counts), 12 split on hyphens; quote the larger
characters: 62
non-ASCII characters: 0
```

## Whole IPS (V47 with the paragraph swapped in)

### V47 as it stands
```
words: 494 by spaces (a spaced dash counts), 497 split on hyphens; quote the larger
characters: 2723
non-ASCII characters: 4
  at 324: '–' EN DASH
  at 336: '–' EN DASH
  at 1025: '–' EN DASH
  at 1064: '–' EN DASH
```

### V47 with (i)
```
words: 492 by spaces (a spaced dash counts), 495 split on hyphens; quote the larger
characters: 2721
non-ASCII characters: 4
  at 324: '–' EN DASH
  at 336: '–' EN DASH
  at 1025: '–' EN DASH
  at 1064: '–' EN DASH
```

### V47 with (ii), unpaid
```
words: 506 by spaces (a spaced dash counts), 509 split on hyphens; quote the larger
characters: 2792
non-ASCII characters: 4
  at 324: '–' EN DASH
  at 336: '–' EN DASH
  at 1025: '–' EN DASH
  at 1064: '–' EN DASH
```

### V47 with (ii), P9 clause cut
```
words: 494 by spaces (a spaced dash counts), 497 split on hyphens; quote the larger
characters: 2729
non-ASCII characters: 4
  at 324: '–' EN DASH
  at 336: '–' EN DASH
  at 1025: '–' EN DASH
  at 1064: '–' EN DASH
```

## Strict differences
| Version | P7 strict | vs V47's P7 | IPS strict |
|---|---|---|---|
| V47 | 52 | 0 | 497 |
| (i) A only | 50 | -2 | 495 |
| (ii) A + C | 64 | +12 | 509; 497 with P9's 12-word clause cut |

## B, Final Report text (AI DRAFT (Claude, 1 Nov 2026); for the Final Report, not the IPS)

```
$ python3 keel/office/tools/textcheck.py - <<< "paragraph"
In our model the rival's lead, counting the gift and what Laura keeps by 2042, comes from strong 2028-30 stock markets: outside the best fifth of them it averages under $2,000, and in the worst fifth our plan leaves her $28,000 to $29,000 ahead (S0, S1). If yields fall 2 points for good (S6), the lead spreads: about $11,000 outside the best fifth, with our plan still about $24,000 ahead in the worst.
---
words: 73 by spaces (a spaced dash counts), 74 split on hyphens; quote the larger
characters: 403
non-ASCII characters: 0
```

Figures, MODEL, from `../../../rooms/lab/L-15_hold_it_then_say_it/results.json` (B_price_address, PRIMARY_by_2028_30_stocks, mean_lead_A09 by fifth, 1 = worst):
- S0: -27,896 / -5,352 / +11,069 / +29,929 / +66,837; mean of fifths 1-4 = $1,938.
- S1: -28,869 / -5,740 / +11,363 / +30,815 / +69,426; mean of fifths 1-4 = $1,892.
- S6: -24,361 / +1,737 / +21,487 / +44,643 / +92,064; mean of fifths 1-4 = $10,877; mean lead $27,114.
- C (inside the quoted range): 200,000 / 200,000 / 199,999 of 200,000 (S0 / S1 / S6) = all but one of 600,000.
