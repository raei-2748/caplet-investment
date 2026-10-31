# FICTION (the room and the simulated people) + real arguments. C-04: the whole price

(Keel is a simulated team, AI-written.) AI-generated (Claude Code), Sat 31 Oct 2026, the Courtroom, round 4 beat 8.
Not for submission. Huddle: `../../huddles/2026-10-31_the-whole-price/` (H-006). Numbers are MODEL: curve 22 Oct 2026
(treasury.gov par), J.P. Morgan 2027 LTCMA world stocks 7.5% compound, 16.78% vol, 50,000 paths in each of three
worlds plus every start month since 1871, engine `../../models/xr_core.py`, A09 as LR-08 builds it (f = 0.743).

**Vote note (LS-06).** Caplet's newest message, Sat 31 Oct 13:39 Sydney: applying the voice studies is now the top
priority, above everything else. So the trial had a voice gate, not only a judge panel.

## 1. On trial
LR-08's paragraph (Laura's Room; `../lauras_room/LR-08_the_bad_naming_day.md`, PR #84), which replaces V45's heading
"Sell low, by appointment" and both 60/40 paragraphs, whole. It had won two blind panels (WR31b: LR 1.83 v V45 3.0) but
nobody had tried the truth of its price, its clarity or its voice. The Writing Room asked for LR v V45 tonight.

## 2. The exhibit the Courtroom ran: C-04 (`C-04_the_whole_price.py`, `C-04_results.json`)
LR-08's "about $9,000 ... in a typical 2033" is the gap between two medians. Per path, A09 minus XR:

| MODEL, A09 minus XR | House | Storms | Bootstrap | History |
|---|---|---|---|---|
| Gift + kept, 2033: median / mean | $9.8k / $13.9k | $12.7k / $12.2k | $11.5k / $14.1k | $15.3k / $18.9k |
| Gift + Laura's money left in 2042: median / mean | $14.1k / $18.6k | $16.4k / $16.6k | $16.3k / $19.2k | $21.3k / $26.0k |
| Paths where XR leaves her ahead (2033) | 38% | 34% | 36% | 32% |
| Worst twentieth of 2028-30 stocks, 2033: XR ahead by (median) | $43.7k | $51.7k | $47.9k | $41.9k |

"$9,000" sat under every cell, even its own per-path median. The premium is a mean: about **$19,000 by 2042** (house).
What it buys is the bad tail: in the worst twentieth of 2028-30 markets XR names $135-145k against A09's $80-95k
(LR-08) and leaves her about $44,000 ahead.

## 3. The trial (posts in the huddle)
- **Tess (prosecutor):** (1) the price is the smallest cell; (2) the payoff is odds, the price dollars; "ten one-year
  bills" lost; (3) "Set to promise the same $145,000" reads two ways, terms before they're defined, donors unsourced.
- **Kai (as Spinnaker):** the mean is the premium; XR leaves her behind in 62-68% of paths; a smaller promise kept is
  not a broken one. Conceded: the worst twentieth (XR ~$44k ahead) is three times the mean premium.
- **Amara (defence):** median is "typical"; the co-sponsor's number IS the benefit (case :111, :114); the donors line
  has a source (Window W-04, Giving USA); "ten one-year bills" answers a risk A09 doesn't carry. One fix: $10,000.
- **Felix (one repair, LR2, 497):** moved after the range paragraph; the price as a 2042 mean; the payoff in dollars;
  "promise" -> "name"; donors and ten bills to the Final Report.
- **Panel C04** (`../../ips_rewrite/judges/panel_C04/SUMMARY.md`, six blind judges, tau 0.50): **LR2 1.83**, LRa 2.5,
  S01 2.5, V45 3.33; LR2 beats LRa 5-1, V45 4-2. The hawk, actuary and professor gave one reason: it concedes the rival
  usually wins, prices that, then shows the tail. V45's "ten one-year bills" is still the line three judges could retell;
  four called its 60/40 a straw man. J5 could not place "$145,000 at the median" beside "our $140,000".
- **Voice reader 1** (`C-04_voice_reader.md`): V45's paragraph first, LR2 second ("a results table read aloud"), LRa third.
- **Round 3:** Amara concedes the price (5-1 was fair); Kai: aim V45's appointment at the right rival, A09 sells
  stocks in January 2031 (true; XR also sells its promised half on naming day, so never "ours never sells"); Tess:
  "after the 2031 set-aside" explains $145k -> $140k (LR-08: XR's bottom moves "only through the mark").

## 4. Ruling (Nora): AMENDED, 5-0, Jun absent; the two changes 3-1, Felix abstaining
Both round-3 changes in; they cost 503, so "and leaves her over $40,000 behind" goes to the Final Report. **LR3**
(`C-04_LR3_ips.txt`, 497 strict, pitch unchanged):
> There is a serious case against all this, and we made it first: our first plan was three-quarters stocks, until our
> own model sank it. Laura is willing to take thoughtful risks, so the strongest rival keeps our ladder, puts the 2028
> deposit mostly in stocks, and sells stocks in January 2031, whatever they fetch that morning, to buy its bottom.
> Matched in our model to name our $145,000 median bottom, it usually wins: counting the gift and what she keeps, it
> leaves Laura about $19,000 more on average by 2042. But in the twentieth of our paths where 2028-30 is worst for
> stocks, it names about $90,000 to co-sponsors against our $140,000 after the 2031 set-aside. We'd pay the $19,000.

**The one change that matters most:** the rival's sale on a date fixed years ahead. It says *why* A09 names $90,000,
and it is the paragraph's only picture. Criterion: Investment Strategy ("reasoning, assumptions, and tradeoffs"; the
case's "appropriate balance between pursuing growth and protecting the capital").

**Voice gate (pre-committed, passed):** a fresh blind reader (`C-04_voice_gate.md`) ranked V45's paragraph first,
**LR3 second, LR2 third**: LR3's sale "on a set morning" is "the only place ... where a person seems to be telling you
what will happen". So LR3 goes to the rewrite inbox. Its offered fix, untested and uncounted: "But in the worst
twentieth of our paths for stocks in 2028-30, that January morning arrives mid-slump, and the rival names about
$90,000 to co-sponsors against our $140,000 after the 2031 set-aside."

**To the Final Report, named (Commandment VIII):** "ten one-year bills" and the sequence-of-sales point; donors give
less in recessions (Giving USA 2008-09, W-04); "leaves her over $40,000 behind"; XR ahead in 32-38% of paths; the
worst-twentieth table and correlations (LR-08); one in thirteen v one in 150.

**Honest weaknesses left:** V45's paragraph still wins on voice; LR3 still carries five figures in four sentences;
"our $145,000 median bottom" is a noun stack; the $19,000 is the house world (16.6k-26.0k across four). GPTZero: not
yet checked.
