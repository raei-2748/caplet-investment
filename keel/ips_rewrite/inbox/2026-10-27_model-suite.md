# The Model Suite -> the rewrite (and the rival scan), Tue 27 Oct 2026

AI-generated (Claude Code), Ray's thread "Build a bigger model suite for the IPS". Research, not submission text.
Full page, charts and every assumption: [`../../models/README.md`](../../models/README.md). **STAMP: curve 22 Oct 2026 |
J.P. Morgan 2027 global equities 7.5% | 50,000 paths per world | history = Shiller monthly 1871-2023 (US stocks for
VT) | MODEL.** Worlds: the house model, a fitted storm (regime-switching, fat-tailed) model, a block bootstrap of
1871-2023, and a replay of every start month since 1871. Plans: V25, today's champion (V25 + lock + rule G cushion,
from R10), and five rival archetypes.

Book 7 reading: the IPS carries one or two of these as reasons for a rule; the rest are Final Report evidence.

## For Thursday's synthesis, in order of use
1. **A new "why buy them now" fact (nobody else will have it).** $300,000 could have bought all ten cheques outright
   in only one month in four since 1871, and in no month from mid-2007 until this autumn (it needs a 10-year yield
   near 5%). At the 2020 low they cost $469k, more than both deposits. This turns "we would rather buy them" from
   caution into timing: certainty is on sale, briefly. Raw line, not draft text: "For the first time since 2007,
   $300,000 buys all ten." (True on the 22 Oct curve by $1,139; the IBTR note already says what happens if it isn't.)
2. **The sceptic paragraph gets its proof.** Start the plan in January 1923: stocks return ~7% a year over the next
   fifteen years and beat bonds, yet a 60/40 pot runs dry and bounces the 1937 and 1938 cheques. One clause in the
   IPS at most ("stocks won the decade and the cheques still bounced"); the Final Report gets the exhibit.
3. **Fix V25's inflation sentence.** "Half the stocks stay Laura's ... the project's second cheque" implies her half
   protects the cheques' buying power. At 3.5% Taiwan building inflation the 2042 cheque buys ~60% of today's $50,000
   (1-in-20: 39%); topping all ten back up needs ~$177k in 2033 against ~$26k she keeps, so her half covers it in ~5%
   of worlds (21% at 2%). Keep "Inflation can make $50,000 buy less. It cannot make $50,000 cost more." Call her half
   flexibility, not inflation insurance.
4. **The break-point sentence checks out.** Yields -2pt before the build need $65k of the 2028 deposit, so a cheque
   breaks only if the deposit also falls by more than ~56%. "More than halves" is right, with a little to spare.
5. **The cushion rule is load-bearing.** V25 as written bounces a cheque in ~2% of house worlds; the champion in 0.2%.
   A smaller 2028 deposit thins Laura's half and pushes V25's figure to 7.5% at $50k; a coverage rule keeps the cheques
   whole down to a ~$40k deposit.
6. **The 3:1 ratio is the cautious end.** The V25 top is reached 75% (house), 79% (storms), 84% (history): odds 3:1,
   3.6:1, 5:1. The champion's lock lifts it to 84-97%.
7. **Tested against every month since 1871:** neither version of the plan ever bounced a cheque or landed below its
   bottom (1,636 full paths; 1,756 range windows). Closest call: a 1928-29 start, still $8,400 (V25) / $3,100
   (champion) above the bottom. Usable in the IPS only as a phrase, never as a table.

## For "Out-think every rival team for semis"
Five rival archetypes, each using only Wharton-allowed instruments (`../../models/xr_core.py`, `rival()`): 60/40
balanced, target-date glide, three-year bucket, bond-fund immunisation (IEF/TLT, no maturities), and all-stocks-then-
ladder-in-2032. Each keeps a reserve, gives the rest, and quotes its 2031 range as its own projection +/-20%.
- **Promise broken (a cheque >$1k short, or the gift below the quoted bottom):** champion 0-1.6% across the five
  worlds; V25 0-3.6%; rivals 22-36% (17-24% even at +/-40%). Their main failure is the range, not the cheques.
- **Cheques short:** 60/40 4-8% in the model worlds (1.3% in history, all in 1922-24 starts); immunisation 10-14%
  (funds never mature; duration drifts after 2033); lock-late 6-11% (if stocks are down in 2032, the ladder can't be
  bought).
- **Where rivals beat us, honestly:** lock-late's median gift is $254-325k vs our ~$166k; the 60/40, glide and bucket
  plans leave Laura $170-290k in 2042 vs our $31-56k. Flexibility is our thinnest number; the Final Report should own it.
- Storm world chart: `../../models/charts/c2_rivals.png`.

## Takes
- **Jun:** The 1871 chart is the first number I've seen that a judge could feel. Twenty years of "too expensive",
  then a window, and we bought in it.
- **Kai:** Rival plans are our own sketches, so the 22-36% is a property of those rules, not of any real team. Quote
  the mechanism (ranges built on a forecast break; ranges built on owned Treasuries don't), never "other teams fail".
- **Amara:** Take the inflation line seriously. If a judge reads "the project's second cheque" and then sees $26k
  against a $177k inflation hole, we lose the trust we spent 400 words earning.
