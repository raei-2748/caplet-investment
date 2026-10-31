# FICTION. H-007 · The bad naming day (Laura's Room, Sat 31 Oct 2026, 15:10 Sydney; Amara chairs)

(Keel is a simulated team, AI-written.) Keel's events are fiction and never enter a Caplet deliverable as Caplet's
experience. What the members cite must be the real repo facts below or real fetched sources. Simulated co-sponsors
and judges are tests, never quotes; no Laura quotes ever.

## The question (continues H-004's seed)
**Q12 from the co-sponsor's chair: why not a safe ladder and the rest in stocks (rival A09)?** After naming day both
plans lock what they name, so a co-sponsor holding the range in 2032 can't tell them apart. The only thing a
co-sponsor ever sees is *which number Laura can name in 2031*. Is that difference worth what it costs her, and is it
the paragraph-sized answer the current draft (V45) is missing for a growth-minded judge?

## Budget
3 members, 3 rounds, 8 agent calls (round 3 only the two on either side of the real fight). Commandments bind
(`keel/BIBLE.md`); marking only by `keel/WHARTON_WORD.md`.

## The real facts (quote these, don't invent others)
- **V45** (`keel/ips_rewrite/drafts/D25/ips_V45.txt`, AI DRAFT, current): the ladder buys the ten cheques in Jan 2027;
  "Most of the 2028 deposit buys Treasuries maturing late in 2032, just enough to grow back into all of it: her
  floor. What's left ... buys one world index fund"; the only rival argued is a 60/40 ("about one time in three ...
  ours, under one in sixty"). **No sentence in V45 answers A09** (Amara's read, section 3 of the LR-08 memo).
- **A09** (`keel/ips_rewrite/rivals/A09.md`): same ladder; the rest ~80% world stocks / 20% intermediate Treasuries;
  in 2031 the bottom of the range moves into Treasuries; gift = locked floor + at most half the rest. Two of six
  panel-4 judges ranked it first.
- **LR-08 run** (`keel/rooms/lauras_room/LR-08_the_bad_naming_day.py`, results `LR-08_results.json`; MODEL: curve
  22 Oct 2026, J.P. Morgan 2027 world stocks 7.5%, 50,000 paths per world + every start month since 1871; engine
  `keel/models/xr_core.py`). A09 locks 74% of its 2031 pot, chosen so both plans name the **same median bottom,
  $145k**. Then:
  - Worst 5% of 2028-30 stock markets: XR names **$145k**; A09 names **$90k** (house), $80k (storms), $90k
    (bootstrap), $95k (history). Even locking its whole pot, A09 would name about $125k (Felix re-ran f = 1.0, house, round 1; the $90k / 0.74 proxy said $120k).
  - A09's bottom moves with stocks (correlation 0.95-0.99); XR's doesn't (about 0). Bottom under $100k: A09 6.2%
    (house), 7.4% (storms), 3.3% (history); XR 0.05%, 0.04%, 0.
  - XR's bottom still varies (p1 $115k, house) because of rates before the Jan 2027 build, which is known by Jan 2028.
  - **The price:** A09's median gift is $2-9k higher; median gift + Laura's kept money in 2033 is **$9k-$16k higher**
    (house $191.9k vs $182.4k; history $202.5k vs $186.5k); A09's p95 gift $250k vs XR's $182k; Laura's mean money
    in 2042 $9-13k higher. A09 reaches its top 93% (house) vs XR 84% in this engine (L-13's slide puts XR at ~97%).
  - **Against us, honestly:** in this engine XR misses a cheque in 0.19% of house paths, A09 in 0.004%, because A09
    leaves Laura more of her own stock money to cover the coupon leak after 2033. This engine predates the 2031 mark,
    so its count of gifts below XR's named bottom (1.3% house) is not the design's; on L-13's chain the bottom breaks
    0-2 of 200,000 (Window, 31 Oct).
- **W-04** (Window, Giving USA 2010): giving "typically ... stays flat or falls in recession years"; -2.4% and -3.2%
  real in 2008-09; "three to five years" to recover.
- **Case** (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`): :109-112 she approaches co-sponsors
  in 2031; "A meaningful personal contribution may signal that the residency is financially viable ... and make
  potential co-sponsors more willing to contribute"; :114-116 promising more than she can contribute damages her
  credibility; :117-120 the range, its confidence, favourable and unfavourable outcomes; :68-74 "thoughtful risks",
  "an appropriate balance between pursuing growth and protecting the capital required for her goals".
- **Library 31 Oct** (`keel/loop/rounds/2026-10-31.md` s4): Harvard, Yale, Princeton shelved buildings in 2009 when
  endowments fell; UNC collects building money in cash before the contract; GFOA: building money's "investment
  duration is no longer than the expected drawdown schedule"; farmers lock each slice "where there is relative
  certainty"; J3: for Laura, locking early is not free (the equity premium).

## Who reads what
Each member: their profile (`keel/members/<name>.md`, above "## Agent profile"), `keel/CAST.md`, `keel/VOICE.md`,
`keel/CULTURE.md`, this brief, and every earlier post in `posts/`.
- **Amara** (host): sits in the co-sponsor's chair. "What does Laura feel in a bad year?"
- **Kai** (dissent): argues A09's side at its strongest; the price is real money.
- **Felix** (the gate): attacks the numbers and the engine; what would a judge with the case open believe?

## Correction after the huddle (31 Oct, PR #84 review)
The LR-08 run in this brief left L-13's 2031 mark off both bottoms. Re-run with it on both (A09 re-matched, f = 0.743):
A09 names under $100k in 7.5% of house worlds (one in thirteen), XR in 0.69% (one in 150), not one in two thousand;
XR's bottom moves slightly with stocks (correlation 0.08); worst 5%: $140k vs $90k; the price is unchanged (~$9.4k);
neither gift ever lands below its named bottom. The posts above argued over the first numbers and are kept as written.
