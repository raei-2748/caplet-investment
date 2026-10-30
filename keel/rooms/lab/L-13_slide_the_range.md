# FICTION (the room) + real work (the test). L-13: slide the range (one mark moves both ends)

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Genius Lab, Fri 30 Oct
2026, 13:40 Sydney, round 3 beat 5 (Nora builds; Kai roasts; Jun and Kai give the verdicts). Script
`L-13_slide_the_range/run.py`; results `L-13_slide_the_range/results.json`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | V29's design = LR8 "MB+T +lock" via L-12's chain, unchanged, one block appended | MODEL.**
Reproduction: S0/S1/S6 top within $1k 84.62 / 82.87 / 41.48% and quoted top (rounded down to $5k) 86.6 / 84.8 / 44.0%,
identical to L-12; cheques short >$1k 0.03 / 0.03 / 0.05%; quoted bottom broken 0 of 200,000 in every world.

**For a judge, in plain words.** Our 2031 range missed its own top about one time in seven, and in a world where yields
fall it missed more often than not. We thought that was caution. It wasn't. Almost every miss was money the plan
already knew, on the day Laura names the range, that the cheques would need. That money was taken off the bottom but
never off the top. Take it off both ends, so the whole range steps down together before she says it, and the top is
reached 96-98 times in 100 in all four worlds we tried. The bottom is still never broken, and the typical gift doesn't
move. The draft needs one word changed.

**Why this, today.** Q10 (why a range, and what each end costs) and the Library's K3: the newsvendor reading of C5's top
swung from "over-promising is 6 times worse" (S0) to "under 1 time" (S6), which the case contradicts. North stars 3
and 4; Client Knowledge (the range is the case's own centre, :110-114), Investment Strategy, Portfolio Analysis. IPS
line that could change: B3 para 10 / V29 para 17, "anything they can't cover comes off the [quoted] bottom".

## Pairings tried
- **K3 (newsvendor) x V29's top:** if the implied cost ratio swings with the world, the top isn't set by a cost at all.
  So what sets it? (-> the "why missed" split, below.)
- **F1 (half of IPOs miss their range) x the door table:** an IPO misses because the market moves; does Laura's top
  miss because the market moves? No: her promised half is locked in Treasuries on naming day. Her misses come from her
  own cheques' first claim, which is a known, dated thing.
- **W-03 (SEC: a range wider than 20% of its top isn't bona fide) x the width:** counted, both designs.
- **T1 (seed money, "don't whisper the part you're sure of") x B3's "gifts":** the low side's cost is the co-sponsors'
  giving. A wording point (-> D), for the Writing Room.

## Challengers, with the novelty check
(`../../IDEAS.md`, this book, the Library's slips, R02, R05, `../../loop/FRONTIER.md` s3, the binned list, the bank)

| # | Challenger | Novelty | Builder |
|---|---|---|---|
| A | **Slide the range:** the 2031 mark takes what the cheques still need off both ends, not just the bottom | **New.** Nearest: bank #64 (bank it at the mark, which cuts the bottom only), #65 (the lock); nobody has asked why the top misses | Nora |
| B | **A top named at a fixed chance** on naming-day prices: what the bought Treasuries project to pay, less the gap, less a fixed cushion (Library #84 b) | **Return** of #84 / stepping stone S5 (newsvendor), run as A's rival | Nora |
| C | **"Bona fide" width as the range's why** (W-03, #83) | **Return** of #83; this is its count | Nora |
| D | **Say the bottom loud: "too low costs their gifts"** (T1, #85) | **Return** of #85; wording only, no model | not built (Writing Room) |

## Kai's roast (before the run)
"Lower the bar and you'll clear it more often. That's not a finding, that's limbo in reverse. And Tess's own paper says a
timid number costs the co-sponsors nearly sixfold. My bet: your slide knocks ten grand off the typical gift."

## Test: why the top misses, and the slide (four worlds, 200,000 paths each, MODEL)
| World | V29: top reached | of the misses: cheques' 2033 claim / anchor | mark cut the bottom (median) | **Slide: top reached** | slide: median miss | bottom broken | median top / gift, V29 -> slide | mean gift change |
|---|---|---|---|---|---|---|---|---|
| S0 base | 86.6% | 11.9 / 1.5 pts | 16.9% ($10k) | **97.9%** | $865 | 0 | $165k / $165k -> same | -$843 |
| S1 fall together | 84.8% | 13.3 / 1.9 pts | 18.4% ($10k) | **97.6%** | $948 | 0 | $165k / $165k -> same | -$918 |
| S6 yields -2pt for good | 44.0% | 54.1 / 1.8 pts | 62.9% ($20k) | **96.0%** | $1,062 | 0 | $155k / $150k -> $145k / $145k | -$3,482 |
| S2 deposit halved | 72.8% | 26.3 / 0.9 pts | 37.9% ($10k) | **96.7%** | $1,194 | 0 | $80k / $80k -> same | -$1,905 |

"Anchor" = the Treasuries bought on naming day project to pay less than the quoted top (the top counts the floor at its
face, not its payout). The mean gift change stays with Laura: the cap hands anything above the top to her half.
**Rival B** (projected top, fixed cushion): cushion $0 reaches 96.5 / 96.3 / 94.8 / 95.8%; $2,500 reaches 99.0-99.6%
but trims the median top by up to $5k. As good as A, never better at the same median, and it needs a second projection
of the floor. A wins on simplicity; #84 stays a reading, not a rule.
**The implied over/under cost ratio** (reach / miss, Kai's K3): V29 6.5 / 5.6 / 0.8 / 2.7, slide 47 / 41 / 24 / 29. The
swing was the flaw, not the world: with the slide it never falls below 20 to 1, which is what the case's "could damage
her credibility" asks for.
**C, the bona fide count** (width as quoted over the top): V29's median width is 14.7 / 14.7 / 16.7 / 20.0% of the top,
over 20% in 11.0 / 11.2 / 35.0 / 46.7% of paths; slide 14.3 / 13.8 / 10.3 / 17.6%, over 20% in 5.6 / 5.5 / 0.5 / 23.5%.
The typical range passes the SEC's test in every world with a full deposit; never "always".

## Side answers (open requests)
- **Writing Room (door 4):** after naming, the 2033 top-up takes from the gift in 16.1 / 17.9 / 61.2 / 35.7% of paths
  (median $7.6k / $8.1k / $16.7k / $8.0k), pushing it below the quoted top in 12.8 / 14.6 / 55.8 / 27.1%. So "her half
  after, a cheque last" is missing "then the gift", **unless** the slide is adopted: then the known part is off the top
  before it is said, and what's left touches the top in 2.1-4.0% of paths by a median of about $1,000.
- **Courtroom (door table, share of paths S0 / S1 / S6 / S2):** (a) the hope before 2031 (stocks below their 2028 cost
  on naming day) 22.9 / 23.1 / 23.1 / 23.1%; (b) her half sold for the cheques in 2031 or 2033 71.7 / 71.7 / 88.0 /
  71.7%; (c) the bottom cut before it is quoted 16.9 / 18.4 / 62.9 / 37.9%; (d) the gift after naming 16.1 / 17.9 / 61.2
  / 35.7% (top missed 13.4 / 15.2 / 56.0 / 27.2%; with the slide 2.1 / 2.4 / 4.0 / 3.3%); (e) a cheque short >$1k 0.03 /
  0.03 / 0.05 / 0.05%.
- **Library #84 (a) and (b), Window W-03:** above.

## Verdicts (the builder doesn't judge)
- **A, slide the range: ADOPT** as the Lab variant for tonight's Long Room (B3 with one word swapped). Jun: "The bottom
  was told and the top wasn't. That's a bug, not a policy." Kai: won half his bet in S6 only (median top -$10k), lost it
  in the other three (median unchanged), and the $10k in S6 was a top V29 reached 44 times in 100.
- **B: PARK** (Final Report: the fixed-chance top as the theory the slide approximates in one word).
- **C: PARK** (FR table; in the IPS only as "narrow", never "a regulator would call it honest": it fails in 1 path in
  20 even with the slide, 1 in 4 with half a deposit).
- **D: to the Writing Room** (wording).

**Breach this exposes:** B3 para 11 / B2 "the change lands on what isn't yet promised" is false at the top in 1 path in
7 (S0) to more than half (S6) under the current text; with the slide it is true to within about $1,000 in 96-98%.

**Ninety-second rule:** "When the cheques need money, the whole range steps down together, before she says it, not
after."
