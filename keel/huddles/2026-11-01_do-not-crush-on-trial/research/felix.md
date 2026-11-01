# Felix, evidence notes, H-013 round 1 (read Sun 1 Nov 2026, Sydney)

(Keel is a simulated team, AI-written.) Paths are from the repo root `/home/user/caplet-investment`. V50 line numbers
are the lines of `keel/huddles/2026-11-01_do-not-crush-on-trial/exhibits/V50_ips.txt` (odd lines hold the paragraphs:
1 opener, 3 XR, 5 ladder, 7 income risk, 9 deposit/floor/note, 11 range, 13 floor argument, 15 weak point,
17 reserve, 19 "Do not crush."). textcheck on the exhibit: 497 words by spaces and split. I did not open any other file in posts/.

## HARD 1: "Nobody else can help." (V50 :1)
- Case `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt:91`: "Teams may not rely on co-sponsors, grants,
  program fees, or other outside funding to meet this requirement." A rule for the team's plan ("may not rely"), not a
  claim that nobody can.
- Same file `:83-86`: the portfolio "may also cover part of the facility's cost. Any remaining facility cost ... may come
  from co-sponsors, grants, collaborators, program fees, continued business income, or other sources."
- V50 :1 puts the sentence straight after "to fund her Taiwan residency"; V50 :11 then has co-sponsors giving money.
- `:61`: her living costs are covered by outside income, so "nobody" is also false of Laura's life.

## HARD 2: shares at zero v "cannot expire worthless" (V50 :9)
- Both clauses are in the same paragraph, two sentences apart. Plain reading: "fell to zero" and "worthless" are the same
  state. "Expire" is the option's word (the bank's note's option expires), so the line is defensible only for a reader who
  already knows that.
- `keel/ips_rewrite/IDEA_LEDGER.md:150-152`: the sibling line "wipe out every share" (C5) was moved to the Final Report
  because the Window found it false in a few hundred of 600,000 paths ("the shares can help a cheque, never hurt one").
- Idea ledger C3 (`:95`) IN: the capital-protected note; the critique is the intended joke, but the page never says the
  option is what expires.

## HARD 3: "regardless of what markets do in between" / "not a probability, but a purchase" (V50 :5)
- `keel/ips_rewrite/inbox/2026-10-26_archive.md:11-12`, rule A16: "Hold to maturity shuts out price, not rates. 'Price
  swings can't touch a payment' is fine; 'markets/rates can't' is not."
- V50 :15 contradicts it: "If yields fall and stay low ... earn less ... any gap".
- `keel/library/ips_numbers_2026-10/IPS_number_sheet.md:40-42`, `:46-48`: "Once bought, each payment depends mainly on the
  US government" is true for principal "but not for the coupons"; in 6-7 of 100 paths a later payment is not covered, so
  "cannot miss is not literally true" (MODEL, 15 Oct curve, quoted for context only, no number goes in the IPS).
- `keel/ips_rewrite/00_GROUND_TRUTH.md:66-69`: locked TNA note 2 says IBTM's "final payout is not fixed"; terminal payout
  is NAV not par. `competition/wins/2026-10-23_snapshot.md:22-26`: five of the ten rungs are funds (IBTM, IBTO, IBTP, IBTQ, IBTR).
- Bible allows strong words ("near-ironclad", BIBLE.md:397; Ahaan's own "exact NAV", BIBLE.md:216-217), so "exactly" on its
  own is not the flaw. The flaw is "regardless of what markets do" (A16), and "not a probability" for the whole ladder.

## HARD 4: "bonds that mature early earn less while waiting" (V50 :15)
- `keel/ips_rewrite/lab/R08_4_coupons.py:7-9` (docstring): the model's leak is coupons, each one buying more of its own rung
  "on the day it arrives, locking that day's yield"; the alternative is a sweep into a bill fund. Number sheet `:27-28`:
  "the coupons the ladder pays must be reinvested at lower yields."
- Maturity wait is real only for the five T-bond rungs (Feb-2037 pays the Jan 2038 cheque, 10.5 months early; archive
  rule A14, `inbox/2026-10-26_archive.md:6-8`). The five iBond funds close in December, about a month early.
- V39-V41 had the plain version, "early cash earns less if yields fall" (`drafts/D19/ips.txt:9`); V49 "cash from bonds that
  mature early" (`drafts/D29/ips_V49.txt:7`); V50 drops "cash from", so the bonds are the ones said to earn less.
- Also "reinvestment" is never glossed in V50 (SOFT).

## HARD 5: the order (V50 :9, :11, :15, :17, pitch last line)
- :9 "money she will own outright even if every share ... fell to zero"; :11 "money she already owns, a commitment rather than
  a forecast"; pitch: "Stocks move the ceiling. Never the floor."
- :15 "any gap comes from Laura's kept half before the floor": so the floor is the next draw after the kept half. The kept half is
  stocks (:11 "half her stocks"). If shares fall, the kept half cannot absorb a gap, and the floor does. So stocks can move the floor.
- Timing: case `:94` the facility money goes at the start of 2033, the last cheque is 2042 (`:88`); "before the floor" works only for a
  gap visible by January 2033. Lab on an older design: a coupon gap reaches the floor in 7.0-8.7% of paths, a payment is short after
  2033 in 6.8-8.4% (`keel/pm/REQUESTS.md:103`, MODEL, context only). V47-V49 had the 2031 set-aside (ledger D6 `:112`, V44 `:172-173`);
  V50 has no set-aside and no date for the gap.
- :17 "the cheques, then the floor, then the gift": the floor is the bottom of the gift (:11 "The bottom is her floor"), so the
  floor is counted twice; the kept half (first to be drawn per :15) is not in the order. "The order" itself is never defined
  (priority when money is short).

## HARD 6: Wharton's questions (WHARTON_WORD.md)
- `keel/WHARTON_WORD.md:19` "uses appropriate diversification" (Investment Strategy); `:66` "portfolio construction and
  diversification"; `:68` "managing the operating reserve's asset composition over time".
- V50 diversification evidence: "one world index fund" (:9), "every share in the world" (:9). No word "diversif*", no reason why the
  ladder is one borrower (ledger B6 `:80`, FR "candidate to return"), nothing on why the world fund. A ticker marks it thin/missing.
- Reserve composition: V50 :17 "the ladder becomes the operating reserve, unwinding one bond at a time" = answered, thinly (no size,
  no mention of the cash and reinvested coupons that also sit in it). Case `:94-97` asks size, initial composition, how it changes.
- Present: central idea (:5 "We buy them"); principles (:1 "cheques come first", :13); balance of growth/risk/flexibility (:9, :11, :13);
  how composition changes (:5, :9, :11, :17); protect cheques while keeping flexibility (:7, :11). Liquidity appears only as "liquid
  any day" on the kept half (:11). "Responsible" contribution: the range's logic is there, why half is not (not required in the IPS).

## HARD 7: Commandment VIII, ledger rows A5 and B7
- A5 `IDEA_LEDGER.md:63`: IN, "Nothing is sold before it pays". `IDEA_BANK.md:278` #28: "Do not crush = no Treasury is sold before it
  pays ... keep". Grep of V50 for sold/sell: no hits. "Held to maturity" (:5) and "unwinding" (:17) are the only echoes. So "Do not crush"
  (:3, :19) is named for the pill and never for Laura's plan.
- B7 `IDEA_LEDGER.md:81`: IN "(new)": $500,000 of cheques cost about $300,000, the government's interest pays the rest (if nobody sells early),
  "sets up do not crush". Grep V50 for 500/interest: only "the interest those Treasuries are expected to earn" (:9). The ledger itself says
  (`:53`) B7 was "cut since V32 (no source in the sentence)" while row 81 still reads IN. The ledger has no V50 section (last entry V48, `:11`).
- Also dropped since V31 and still marked IN: D6 (`:112`, coupon gap set aside in 2031); B9 (`:83`, inflation; moved to FR at V32, `:150`).
  Each is arguable; A5 and B7 are the two that carry "do not crush".

## SOFT notes
- V50 :11 "Before she names it, that half moves into Treasuries.": "it" = the top (nearest subject, ":11 The top adds"); the range is the other
  candidate; "names" is new (the prior sentence has her "give" a range). "valued that day" then "before" gives two days. The reason ("a number said
  aloud ... cannot be quietly halved", :13) sits in the paragraph about the floor, after the kept half. The cost (after naming, a rise never reaches
  the gift) is not said (ledger D5 `:111` IN in V31). Writing Room source: `keel/drafts/writing_room_2026-11-01/V50_check.md:17-24`.
- V50 :7 "the gift" appears before it is said that the gift is the building contribution (:1 "contribute to the building"); :9 "her floor" before
  "floor of what" (the pitch says "floor for the facility gift", the IPS never does). :1 "the building" has no antecedent; "her Taiwan residency"
  can be misread as where Laura lives (CLAUDE.md "Rejected ... residency = where she lives").
- V50 :11 "whether the building costs more in Taiwan dollars or she simply needs flexibility": the clause is garbled and never says why Taiwan dollars matter.
- V50 :3 "ten Treasuries" and pitch "ten Treasuries" v :5 "Treasury bonds and funds that mature like bonds": Book 5 made the distinction optional
  (ledger B8 `:82`), so only SOFT. A cold reader may stall on "funds that mature".
- V50 :13 "time makes a stock-market loss less likely without making it smaller": true in dollars (time-diversification debate), compressed; "smaller than what?".
- V50 :7 "income that dries up in exactly the kind of downturn that makes bonds more expensive": the case (`:44`) says only "earnings from publishing
  advances, speaking engagements, licensing"; the correlation is the team's inference. Number sheet `:69-70`: VT and the iBond ladder moved together in
  the last year (correlation about +0.5), so "a downturn makes bonds more expensive" is not always so.
- V50 :5 v :9: "first $300,000 buys a ladder ... one rung falling due before each cheque" v "first finishes any rung the first $300,000 couldn't buy";
  :7 "A cheque funded by a Treasury already bought does not [shrink]" is true, but the 2028 deposit can still be the thing that finishes a rung
  (number sheet `:13`: ladder costs over $300k on 1 Jan 2027 in about 1 case in 3, 15 Oct; WInS note on IBTR in 00_GROUND_TRUTH.md `:75-76`).
- Pitch: "ceiling" (never used in the IPS, which says "top"); "the expected interest" never says whose; "releases" is the verb for XR in the pitch (R never "release" as a name).
- Caplet XR (:3): XR delivers over time, not "on schedule"; fine for a pharmacist's gloss, a pill nerd might pause.

---

# Felix, round 2 checks (read Sun 1 Nov 2026, Sydney; after reading posts/r1_kai.md, r1_amara.md, research/kai.md, research/amara.md)

Paths from the repo root. V50 line numbers as above. Post: `posts/r2_felix.md`, 499 by textcheck's larger count.

## Changed my mind (two)
- **Top flaw.** Round 1 I ranked l.9 (zero v "expire worthless") as the flaw a judge would catch. Kai (`posts/r1_kai.md:17`) and
  Amara (`posts/r1_amara.md:11`) found the motif's own clash: l.3 "Break it open and you ruin how it works" v l.17 "every one
  bought before the first is opened". That clash sits in the first and last lines; Book 11 calls the set-up/payoff "the whole
  power" (`keel/BIBLE.md:327`, reading point 4 at `:333`); Commandment II (`:353-356`) says judge the whole page, not one line.
  So the repair goes to "do not crush"; l.9 stays a truth fix (CORD) that rides along.
- **Round-1 HARD 3 dropped from the cords.** Re-read V50 l.5: the subject is "A Treasury held to maturity pays exactly what it
  promises, regardless of what markets do in between", which is true of one bond. Archive A16 (`keel/ips_rewrite/inbox/2026-10-26_archive.md:11-12`)
  bans "markets/rates can't [touch a payment]", and V50 says it of the bond, not the payment; l.15 owns the rates risk. Amara's point
  holds: the case asks teams to "define" certainty (case `:97-98`), so "not a probability, but a purchase" is a definition.
  What's left of it is truth fix 4 (the funds).

## Hit on Kai: "funds don't mature"
- iShares (issuer page, re-read 28 Sep 2026): the funds "will terminate on or about October or December 15 of the year in each Fund's
  name" and "do not seek to return any predetermined amount" (`keel/library/insight_v1/securities_and_allocation.md:61`; also
  `keel/library/insight_v1/phase_D/audit_rates_D1.md:72`). Newer check, 21 Oct: fund "terminates on or about 15 Dec 2036",
  "payout is not fixed" (`keel/library/assistant_review_2026-10/oct21_tna/factcheck.md:108`). WInS lists them by end date
  ("iBonds Dec 2032" etc., `competition/wins/2026-10-23_snapshot.md:22-26`).
- So: they do end on a set date (Kai wrong); they don't promise a sum (the real problem next to "pays exactly what it promises").

## Hit on Kai: B4 v V50 l.9 (which is the real plan?)
- Ledger B4 (`keel/ips_rewrite/IDEA_LEDGER.md:78`): the 2028 deposit "never carries a cheque".
- Frozen WInS IBTR note (`caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:15`): "If yields fall more
  than about 0.2 percentage points by January, the 2028 deposit would top up the ladder, leaving less for the facility." IBTO note
  (`:20`): "one of the first payments we would top up if yields fall before January". Ground truth (`keel/ips_rewrite/00_GROUND_TRUTH.md:75-79`):
  the IPS is bound to "2028 deposit tops up the ladder first". Writing Room put l.9's sentence back for this reason
  (`keel/drafts/writing_room_2026-11-01/V50_check.md:25-31`).
- Verdict: V50 l.9 is the real plan; the ledger's B4 wording is the overstatement (should read: the deposit carries no cheque except to
  finish a rung the first $300,000 couldn't buy). Ledger edit is for the rewrite thread; I touched nothing.
- Para 4 (l.7) "A cheque funded by a Treasury already bought does not [shrink]" still holds, because the deposit finishes rungs first.

## Hit on Amara: "about $300,000 buys them, time pays the rest" (posts/r1_amara.md:9)
- The two numbers are case facts ($300,000 case `:43`; ten x $50,000 `:88-90`). The claim linking them is a market price on one date:
  `keel/ips_rewrite/00_GROUND_TRUTH.md:86-88` ("'the first $300,000 buys all ten payments' is a one-close call, not a fact"). The only
  "says who?" (Commandment V, `keel/BIBLE.md:368-370`) is the model, banned by Book 11 (reading point 2, `:331`). Ledger `:53`: B7 "cut
  since V32 (no source in the sentence)". Commandment VII (`:377-379`): sums go to the Final Report.
- "Time pays the rest": the gap between $500,000 and the cost is interest, and part of it is reinvested coupons ("reinvested coupons fund
  the rest", Nov-2039 note; "reinvested coupons funding part of each", Nov-2041 note; `00_GROUND_TRUTH.md:76-77`), whose rate is unknown:
  V50's own weak point (l.15).
- "loses the interest" (r1_amara :9 and :11): a bond sold before maturity fetches the day's price, which is the value at the day's yields
  of the interest and principal still to come (plus accrued interest). What is lost is the certainty of the promised sum, not the
  interest. Standard bond pricing, not looked up today; consistent with A16 ("Hold to maturity shuts out price", archive `:11-12`).
- Her "a promised $50,000 becomes whatever the market pays that morning" is right and should stay in any definition.

## The repair's job (evidence)
- Wharton: Creativity and Presentation "a compelling, well-organized narrative" (`keel/WHARTON_WORD.md:34`); Investment Strategy
  "disciplined planning across Laura's changing time horizons and cash-flow needs" (`:19`); IPS question 2 "What principles will guide
  your investment decisions?" (`:51`).
- The generosity temptation is in the case: a meaningful contribution "may ... make potential co-sponsors more willing to contribute"
  (case `:111-112`); "If Laura promises more than she can ultimately contribute, she could damage her credibility" (`:114`).
- Ledger A5 (`IDEA_LEDGER.md:63`) is the ledger's meaning: no Treasury sold before it pays. V50 l.13 already has the words a definition
  can pay off: "a floor that was bought, not hoped for".
- Steal: l.3 already says "one redeemed in time for each January", so l.17 can end "before the first is redeemed" (R = redemption, the
  standing rule, `keel/BIBLE.md:396`).

## Truth fixes: evidence for the post's four
1. l.9 zero v "cannot expire worthless" (CORD). Ledger C3 (`IDEA_LEDGER.md:95`): the bank's note = bond + option + fee; V50 never names the
   option, so "expire" has nothing to attach to. The fix's claim (an option bought with the interest is worth nothing at its date if the
   market merely ends where it started; a share is worth the same) is the standard at-the-money call payoff, not looked up today.
2. Pitch "Never the floor." (`exhibits/V50_pitch.txt:1`) v l.15 "any gap comes from Laura's kept half before the floor" (CORD). Fix sentence
   tested in memory: pitch goes from 40 to 48 words (split count), under 50. The fix's "could" is true: the floor pays only if rates fall
   long and the kept half (stocks) can't cover the gap.
3. l.1 "Nobody else can help." (CORD). Case `:91` "Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet
   this requirement"; `:85-86` remaining facility cost and operating support beyond Laura's commitment "may come from co-sponsors, grants,
   collaborators, program fees, continued business income, or other sources".
4. l.5 "funds that mature like bonds" + "pays exactly what it promises" (no cord). TNA note 2: "final payout is not fixed"; locked reflection:
   iBonds "behave a lot like bonds when held to their end" (`00_GROUND_TRUTH.md:66-68`), so the fix sentence echoes Caplet's own locked
   words. Standing rule: "near-ironclad" (`keel/BIBLE.md:396-397`).

## Lower items (not in the post for room; still worth the rewrite thread's eye, no cord)
- l.15 "bonds that mature early earn less while waiting": the bigger leak is coupons (`00_GROUND_TRUTH.md:76-77`;
  `keel/ips_rewrite/lab/R08_4_coupons.py:5-6`). Fix: "The interest these bonds pay along the way has to be reinvested at whatever yields
  are on offer then, and so does the cash from any that mature months before their cheque."
- l.5 v l.9: "her first $300,000 buys a ladder" reads complete; l.9 then says it may not. Fix, in para 3: "If Treasury prices rise before
  January 2027 and the first $300,000 falls short, her 2028 deposit finishes the ladder before it does anything else."
- l.17 "the cheques, then the floor, then the gift": the floor is the gift's bottom (l.11), so it is counted twice. Fix: "the cheques, then
  the floor, then anything above it."
- l.17 "unwinding one bond at a time": in finance "unwinding" means closing a position, i.e. selling, which fights "do not crush"
  (research/kai.md:24-26). Fix: "each bond falling due in time for its cheque".
- l.7 "income that dries up in exactly the kind of downturn that makes bonds more expensive": the case (`:43-45`) is silent on timing; the
  link is Keel's inference and not always so (round 1, number sheet `:69-70`). Fix: "income that tends to dry up in a downturn, often the
  same downturn in which bonds cost more."
