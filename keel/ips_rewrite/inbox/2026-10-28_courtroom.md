AI-generated (Claude Code), Courtroom: lock-what-you-announce + WO-R9, 28 Oct 2026

# The Courtroom, Wed 28 Oct: two trials (Kai presiding)

(Keel is a simulated team. The room is fiction; the arguments are real work. Not for submission. Numbers are MODEL,
from `lab/R08_2_lock_results.json` (22 Oct curve, 7.5% / 6.5%, 200,000 paths). I read the THINKING_LOG, the Genius
Lab, R08_2, my 27 Oct ruling, GROUND_TRUTH, the SCORECARD, V25 Shark Tank, all seven books, and the case.)

---

## Trial 1: "Lock what you announce"

### Prosecution
1. **It protects what the case doesn't ask for.** The case's test is "fall within that range" (:117-118), and the cap
   already passes it. Paths below the bottom are 0.75% today and 0.75% locked (1.28% vs 1.26% with rho 0.5). The lock
   moves where she lands *inside* the range: at the top 93% instead of 77%. The mean contribution goes up $615, and
   Laura's kept money goes down $2,228.
2. **"Every promise Laura makes is bought on the day she makes it" is false three ways.** The floor is bought in 2028
   and named in 2031, so early, not on the day. The payments aren't wholly bought in 2027: 4bp of headroom means the
   2028 deposit often tops them up, coupons are reinvested at unknown yields (short by more than $1k in 47% of paths,
   R08_4), and five rungs pay NAV (Note 2: "final payout is not fixed"). And the top isn't a promise; the bottom is.
   Book 7 makes the IPS "the official record", so an overclaim binds December.
3. **It's a known technique.** Moving risk assets into matched bonds once a liability firms up is liability-driven
   de-risking. Treasurers call it hedging a firm commitment rather than a forecast. It isn't CPPI, which is dynamic
   (this is one dated switch), and Keel's reading bars "immunisation". Named correctly, the cure impresses a PM less.
4. **The "free call" is a transfer between Laura's own pockets.** The $1,613 is the equity premium on half the fund
   for two years, near zero risk-adjusted. A derivatives judge won't accept "free" or "worth $4,406".
5. **It breaks drafted lines (not locked ones).** D3's "Until 2033 nothing is sold early" and V25's "nothing traded
   2028-33" go. Idea 5 adds a second dated stock sale in January 2033.
6. **The Lab's two best ideas collide.** Lock plus the 2033 cushion (variant E) puts 2.2% of paths below the bottom
   (3.3-3.6% under stress) and drops the top to 87%.

### Locked lines, one by one: no breach
- Note 3: "They only set how far her gift rises above her promised minimum. A fall can shrink the extra, and a rise
  before 2031 lifts the top of the range co-sponsors hear." Kept, even sharpened: "before 2031" already scopes it, and
  "can shrink" stays true for falls before 2031.
- Reflection 3: "VT is where we allow ourselves to be wrong" still holds for Laura's half for ever, and for the
  contribution's half until she speaks. "How generous can the facility contribution be?" is unchanged (the top is still
  set by the 2031 value, and the mean gift rises).
- Note 2: IBTM as "a floor for her facility contribution" is strengthened, since IBTM ends up holding the whole range.
  "Every year the bonds sit untouched is a good year" also holds, because no Treasury is sold.
- WInS: no trade. It's a 2031 rule using WInS-listed instruments only (Book 6).
- **Not market timing:** a date fixed now by Laura's calendar, blind to price. A crash before 2031 costs the
  contribution nothing extra (the cap already fixed it); only Laura's claim on the rebound goes.
- **"Do not crush" survives, re-aimed.** Crushing breaks a capsule early, so it's a rule about Treasuries, and none is
  sold. The lock pours money *into* the capsule. It becomes "no Treasury is sold before it pays".

### Defence
1. **The diagnosis is the aha.** From 2031 the cap turns the contribution's half of the fund into a covered call nobody
   is paid for. It keeps every fall and hands every rise to Laura ($4,406 a path back to her against a $1,144 expected
   miss). The cure is standard; seeing the need for it in *this* pledge is not.
2. **The newsvendor prices the lock and approves it.** At our own 3:1, the lock's cut in expected shortfall below the
   top ($614) is worth $1,842 against a cost of $1,613. Under stress it's $1,836 vs $1,504 and $2,061 vs $1,036. The
   27 Oct spine is the ruler the lock passes, narrowly at base and clearly under stress.
3. **Credibility is about where you land.** A range whose owner usually lands at its foot reads as padding. The case's
   "how favorable and unfavorable market outcomes could affect the amount" (:118-119) gets a line a co-sponsor can
   repeat: before 2031 markets move the range; once she has named it, no share price can.
4. **Book 7 wants a framework.** One principle generates the 2027 ladder, the 2028 floor, the 2031 switch and the 2033
   reserve without a single calculation.
5. **XR stops being costume.** Zero-order release (fixed dollars need a fixed-dollar release) now covers the last
   promise too. From 2031 the contribution is a fixed sum, released like the payments. That's a motif line carrying an
   investing idea (BIBLE_TRACE B3).

### Verdict: ADOPT as the central idea, in corrected words. "Final Report only" is not available.
- **Procedure:** the strategy "may not be revised after the submission deadline". A 2031 sale left out of the IPS can't
  appear in December. It goes in the IPS or it dies.
- **Central idea:** "No number Laura names rests on a share price: each is owned in Treasuries by the day she names
  it." Kill "bought on the day" and "every promise is bought". "By" is true for 2027-28, 2028 and 2031, and "no share
  price" survives NAV payouts and coupons, which are rate risks the 2033 re-match handles.
- **Rule:** the day she names the range, the contribution's half of the stocks moves into Treasuries maturing before
  2033, and her own half stays in stocks (B, bottom unchanged). C stays killed. D (a quarter) is the fallback if Caplet
  balks at the $1.6k.
- **Newsvendor:** retire it as the spine. One clause of reasoning stays in the IPS ("a broken word costs her far more
  than a modest one, so we pay a little of her upside to keep it"). The derivation and the lock's 3:1 test go to the
  Final Report. "Three times in four" leaves the IPS because it's no longer true of the plan; the Final Report says
  "about nine in ten" (MODEL), with the misses on the bond side.
- **Conditions:** (i) the 2033 cushion draws from leftover cash and Laura's half *before* the contribution, and the Lab
  re-runs B+E to confirm about 99% inside; (ii) no "free", "$4,406" or "covered call" in the IPS; (iii) "no Treasury
  is sold before it pays" replaces "nothing is sold early" and "nothing traded 2028-33"; (iv) the pitch carries the
  idea, not the mechanism.

---

## Trial 2 (WO-R9): audit of `BIBLE_TRACE.md`

### Rows marked MET that aren't
1. **E3 "MET as process": PART.** The trace keeps stale claims. C3's "2pp before the build AND the deposit halves"
   corner is about ten weeks wide and nearly empty (R08_3). IBTR's "0.2pp" is now 0.04pp. "Three in four" had no
   definition until R08_1.
2. **B7 "MET": PART in execution.** Book 2's "clearly applicable ... not ... a stretch" hasn't been tested on readers.
   V25's shark called the label one "I haven't been given a reason to care about yet", and R (B10) is still open.
3. **C2 misquotes me.** I wrote "the one idea here a judge would repeat", not "the only true aha". Superseded anyway:
   rewrite C2 around the lock, with the newsvendor as its ruler.
4. **D1 counts the "defeasance yardstick" as applied.** I ruled it Final Report only. Add "liability-driven de-risking
   (2031 switch)" under that name, never CPPI or immunisation.
5. **B10** has to record that V25 called "R is redemption" "a decoder ring read aloud".

### Missing expectations
**Books 6 and 7 entirely** (the page says "five books"; there are seven, all equal). Add section G:
- G1 Let the strategy lead and connect WInS, TNA, IPS and Final Report (B6). Test: no IPS line contradicts s3.
- G2 "Explain why each investment belongs" (B6) *against* "rather than describing individual investments" (B7).
  Test: each holding appears only as a job in the framework.
- G3 Never count WInS performance (B6).
- G4 Permitted list for both contributions; no derivatives or individual TIPS/STRIPS (B6). "Call" and "put" stay
  analogies, never instruments.
- G5 Book 7's five "make it clear" items and its "consider" questions, each answered by a sentence a judge can point to.
- G6 The pitch states the central idea and how it serves her goals.
- G7 Framework, not calculations; no final range, reserve sum or co-sponsor text; numerals at the one-or-two budget.
- G8 "May not revise": every future action (2028, 2031, 2033) is written into the IPS now.
- G9 Plain text: no graphics, links, footnotes or citations.
- G10 "A team competition" (B6): the Articulation beat is a real Caplet event, told by students.

**From Books 1-5:** Book 1's tie-break ("not a literature competition ... much prefer ... knowledge of investing");
Book 2's name "relevant to the CLIENT"; Book 3 writes XR's meaning as "extended response" while Book 5 and every Keel
file say "extended release" (record the slip and that Book 5 governs); Book 3's "not ... exhaustive ... the general
gist" (meta-row); the cover note's "neither must we be expected to consistently defer to yours" (F3 covers only Keel
disagreeing).

### The "pulls against each other" section
- **Vast vs subtle:** right, but add Book 1's tie-break: investing beats literature in any close call.
- **Knowledge vs lean:** this misses the sharper pull, Books 4-5 "breathtaking" against Book 7 "rather than detailed
  financial calculations". Resolution: show the knowledge in *rules* (a dated switch, a reinvestment rule, a cushion
  sized by forecast error), not in figures. The lock is the model case.
- **Overclaim vs accuracy:** keep "wrong only if false", and add Book 7's stakes (the official record binds December).
  Trial 1 is the worked example: the strength stays ("owned", "no share price") and the falsehood goes ("on the day").
- **Missing pull:** Book 2 ("optimise for ourselves") and Book 3 ("not mini-Lauras") against Book 6 ("Know your client")
  and Book 7 ("Always remember who your strategy is designed to serve"). Resolution: Laura is the brief and the judges
  are the audience. Decisions are made for her; voice, name and motif for us and the judges.
- **Minor:** "never hasty" (cover) against "do not wait until the last possible minute" (B6). The 31 Oct near-final
  satisfies both.

**Required edit to the trace:** say "seven books"; add G1-G10 and the five Book 1-5 rows; apply the five status
changes; rewrite C2 and C3 for the lock and the corrected failure map.
