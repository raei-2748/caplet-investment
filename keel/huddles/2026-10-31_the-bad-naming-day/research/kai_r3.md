# Kai, round 3: what I checked (31 Oct 2026; FICTION, Keel is simulated; every number MODEL)

**Read:** BRIEF.md, Kai's profile (above "Agent profile"), VOICE.md, posts r1-r2 (Amara, Felix, Kai), research/*.md,
`keel/ips_rewrite/drafts/D25/ips_V45.txt`, `keel/rooms/lauras_room/LR-08_results.json` (read only, untouched),
`LR-05_who_pays_the_blind_fifth.md` (head) and `LR-05_results.json` (grep). No URL fetched.
Stamp of LR-08: curve 22 Oct 2026, J.P. Morgan 2027 world stocks 7.5%, 50,000 paths per world (history 1,636 start
months), engine `keel/models/xr_core.py`, A09 locks f = 0.74 so both median bottoms are $145k.

## (a) Felix + Amara's sentence against LR-08_results.json
| World | A09 p_bottom_under_100k | XR p_bottom_under_100k | Gift+kept 2033 p50, A09 / XR | Price (A09 - XR) |
|---|---|---|---|---|
| house | 6.16% (1 in 16.2) | 0.05% (1 in 2,000) | $191,861 / $182,434 | $9,427 |
| storms | 7.42% (1 in 13.5) | 0.04% (1 in 2,500) | $195,551 / $182,790 | $12,761 |
| bootstrap | 5.13% (1 in 19.5) | **0.27% (1 in 370)** | $198,548 / $185,565 | $12,983 |
| history | 3.30% (1 in 30) | 0 | $202,461 / $186,528 | $15,933 |

- "One in sixteen" and "one in two thousand" are both house only: true for house.
- "$9,000 to $16,000" spans all four worlds; $16k is history, where A09's risk is 1 in 30, not 16. The sentence pairs
  one world's odds with four worlds' price. Not a lie, but not one model either. A judge reads it as one world.
  (It overstates our cost against the odds shown, so it isn't self-serving; still mixed.) Fix: one world, both numbers.
  House is the world V45 already uses ("in our model, with world stocks at 7.5% a year").
- The brief's XR row ("0.05%, 0.04%, 0") skips bootstrap: XR is 0.27% there (1 in 370). Still ~19x safer than A09's
  5.13%, but "one in two thousand" is not true in every world. Another reason to name one world only.
- "50,000 stock markets": true per world for house/storms/bootstrap (history is 1,636 start months).
- "the rest in stocks": A09 is ~80% world stocks / 20% intermediate Treasuries (A09.md via BRIEF). "mostly" is true.
- Missing: the matching. Without "set to name the same $145,000" a judge can read A09 as a plan built to lose
  (Felix r2 asked for "matched at the median").
- "less of her own money": the field is median gift + kept money in 2033 (the gift is her money too, given away).
  The kept part alone differs by ~$5.8k (house $22,902 vs $17,150). "gift and kept money" is the true label.

**Proposed wording (44 words strict, house world, MODEL):**
"A rival keeps our ladder, the rest mostly stocks. Set to name our usual $145,000, in our model it names under
$100,000 one time in sixteen; ours, one in two thousand. Ours costs about $9,000 of gift and kept money in a typical 2033."
- Sources: house a09/xr p_bottom_under_100k (0.0616, 0.0005); bottom_p1_p5_p10_p50 p50 = 145,000 both;
  laura_gift_plus_kept_2033_p50 difference $9,427 ("about $9,000"; "typical" = median).

**What it pushes out (Book 10: whole idea):** the 60/40 comparison, both sentences: "Laura is willing to take
thoughtful risks, and in our model ... a 60/40 portfolio usually ends 2042 almost $200,000 ahead of ours." and
"But "usually" is the whole trick: about one time in three the 60/40 misses a cheque or breaks its word to
co-sponsors; ours, under one in sixty." (29 + 30 strict). New paragraph goes after "...comes in dearer." and before
"A capped range has a catch". Tested in /tmp (V45 untouched): 496 -> 481 strict (textcheck.py). The "Sell low" section
still reads: first plan three-quarters stocks, model sank it, ten one-year bills, sell low on a timetable.
- Side effects: closes BIBLE_CHECK E1 ("who stands behind under one in sixty") by removing the line. Loses the case's
  "thoughtful risks" phrase and the "$200,000 ahead" admission; 16 words now spare if the team wants "thoughtful
  risks" back in front of the rival (its own decision, not squeezed in here). The 60/40 numbers go to the IDEA_LEDGER.

## (b) Does V45 say who pays the coupon leak?
V45: "One leak remains: coupons paid early earn less if yields fall. In 2031 we price that shortfall and set it aside
from the hope, before she names any gift."
- So V45 does name a payer: "the hope", which V45 defines as "a gift towards the residency's building". Felix's
  "never says whose" is half wrong.
- But LR-05 (MODEL, 200,000 paths) sets the rule as "the defaulter pays first": Laura's own spare money stands behind
  her promise; the co-sponsors' number is touched only where hers runs out. V45's "from the hope" reads as the gift
  paying first. Name mismatch, worth a fix by the drafters.
- The residual after 2031 pricing is unnamed: LR-05 with the mark still has payments short over $1k in 0.07% of paths
  (S0; 0.07% / 0.09% S1 / S6). Felix r2 (LR-08 engine, no 2031 mark): misses come where Laura kept $0 in 2033, median
  shortfall $680 over all ten cheques, largest $5,647. After 2033 the gift is given, so the only payer left is Laura's
  kept half, and when it's empty, the cheque. V45's "the cheques come first, then the floor, then the hope" can't
  bind after 2033. That residual is a Final Report line (size beside the rate), not an IPS sentence.
