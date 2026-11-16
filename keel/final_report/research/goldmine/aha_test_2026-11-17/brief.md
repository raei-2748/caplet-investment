# Cold aha test 4, Tue 17 Nov 2026: row 10 set two ways, and six candidates from cards Q95-Q104

These are notes for the Final Report store, not report prose. The register (`../AHA_REGISTER.md`) asks every run to give
blind readers an aha cold and to have them say back what they had backwards. Tests 1-3 (`../aha_test_2026-11-16/`,
`../aha_test_2026-11-16b/`, `../aha_test_2026-11-16c/`) covered every spine row and filled the open slot. Spine row 10
(3f) is still the weakest (2.7 in test 2). Card Q107 ("Setting the register's rows") puts that score down to the belief
the row corrects. It was the team's 27 Sep belief, not a belief the judge holds. So this test sets row 10 on two beliefs a
reader really holds (items 1 and 2), and tests six new candidates from cards Q95, Q97, Q99, Q100, Q101 and Q104 (items 3-8).

The readers are simulated: three model readers given the roles test 3 used (A, a practitioner who builds Treasury
portfolios; B, a fixed-income professor; C, an arts nonprofit's finance director). Each reads all eight items in words,
in one of three orders, with no repo files. Each item's figures come from the card row or NUMBERS section named in the
table. Keel arithmetic is marked as such.

**Readers get only three sections:** "Context every reader gets", "The items" (in their order) and "What each reader
writes". The tables, the notes and the scoring key are for Keel.

| Item | Register row or candidate | Part | Source rows |
|---|---|---|---|
| 1 | Spine row 10, version A: set on the belief that a crash is the danger in a shares-first plan | 3f | NUMBERS 8s (the 27 Sep model's check, the misses table, "What drives the 3.2%", the gap split, "What it shows"); register row 10 |
| 2 | Spine row 10, version B: set on the belief that a 3.2% chance of falling short sounds like high certainty | 3f | NUMBERS 8s (as item 1, and "About 1 in 31", "'None' needs the 2028 deposit's first dollars"); register row 10; 96.8 is Keel arithmetic (100 less 3.2265) |
| 3 | Candidate beside spine row 5 (3a, the 0% standard): a bond "locks in" its interest payments, not the rate they earn | 3a | Card Q104 rows 41-42 (Renberg 1992; Keel arithmetic on FRED DGS6MO), row 20 (Silver, FRBNY 1981-82); claim 2 with rows 12 and 14 (zero is the strictest practice found); NUMBERS 2 ($35,894; the bill fund's 0.15% fee); IPS l.13 ("pay what they say") |
| 4 | Candidate for 3d: a policy is a fact about the present; Laura states what is owned | 3d | Card Q99 rows 1 and 4 (Kleinwort Benson v Malaysia Mining, CA 1989, and the telex of 3 Dec 1985); IPS l.15; NUMBERS 4 ($115,000 top; nothing moves either end after the move) |
| 5 | Candidate for 3a or 3b: the money outlasted the buildings | 3a or 3b | Card Q101 rows 1, 19, 20, 21, 22 (Aspen Institute notes 2019, updated Nov 2025; Tiffany 1918, 1946, 1949; Rauschenberg FY2012, 27 Aug 2025, 31 Mar 2026); the case ($50,000 a year, 2033-2042) |
| 6 | Candidate deepening the reserve "Taiwan's halls closed when the money stopped": nothing had been set aside to run out | 3a (or a clause in 3.0) | Card Q100 claims 1 and 3, rows 17, 29-30, 35, 41; context paragraph (Treasuries bought January 2027 and January 2028) |
| 7 | Candidate beside IPS l.9's thesis: a regulator judges a fund together with whoever pays into it | 2.3 (or 3a) | Card Q97 rows 1-2 (TPR, Integrated risk management, Dec 2015, Example 8, Scenarios A and B); IPS l.9; NUMBERS 4 (VT bought Jan 2028, $29,829 central) |
| 8 | Candidate for 3a: a later payment is worth only its payer's credibility (the Kenyan dairy farmers, chosen over the Authors Guild's salary) | 3a | Card Q95 rows 37-38 (Casaburi & Macchiavello 2019, AER 109(2)); the case ($50,000, 2033-2042) |

**Why item 8 uses the farmers and not the Authors Guild.** Card Q95 supports the farmers more strongly at source. Rows 37
and 38 come from a peer-reviewed field study (American Economic Review, 2019), read in its accepted version. Its figures
(86%, 15%) and both quoted sentences were checked on the page. Row 4's "bare minimum option ... for lean times" was also
read at source, but it comes from one advice article. The contrast it would carry (a salary that can shrink, against a
$50,000 payment that cannot) is Keel's argument, not the Guild's. Per the Q95 rater (Tue 17 Nov), the item never says the
ladder makes "the same trade" as the farmers. It uses only the half the evidence carries: a payment made later is worth
only its payer's credibility.

**Checks made for this brief.**
- Card Q104 row 42 was re-run on the repo's FRED file (`archive/rab/data/fred/DGS6MO.csv`): $1,000 with every coupon
  rolled in 6-month bills reaches $6,152, against the card's $6,144 (a date convention). That is 9.29% a year either way,
  quoted half-yearly like the bond's 14.25%. Kept as cash, it reaches $3,850 (6.86%). At 14.25% throughout, it reaches $15,690.
- The bond's issue date, price and call status were not checked at source (card Q104, Gaps). The sum assumes a purchase
  at face value on 15 Feb 1982.
- Card Q101's "first artist-founded residency" is false: Yaddo and MacDowell came earlier (rater, Tue 17 Nov). Item 5
  says "Louis Comfort Tiffany's residency (1918)", with no "first".
- Item 4 rests its contrast on what is owned (IPS l.15), never on IPS l.17, which is itself a statement of policy (Q99
  rater, Tue 17 Nov). It neither says nor implies that Laura's 2031 words bind her, or that they do not.

## Context every reader gets

Laura Gao, a graphic novelist, has $300,000 at the start of 2027 and $150,000 at the start of 2028. She must pay ten
fixed $50,000 payments, one each January 2033-2042, to run an artists' residency in Taiwan, "with a high degree of
certainty". In 2031 she tells co-sponsors (other funders) a dollar range for her contribution to the building, with how
confident she is; over-promising would damage her credibility. A student team's plan: the first deposit buys ten US
Treasuries (bonds or Treasury bond funds that end on a set date), one maturing before each payment. The first $38,282 of
the second deposit completes them and buys extra Treasuries so all ten are paid even if cash waiting earns nothing.
Most of the rest buys a Treasury fund ending in late 2032, which fixes the bottom of the range; the remainder buys a
world share fund (VT). Half of the shares move into Treasuries before the 2031 meetings, which fixes the top; the other
half is promised to no one (her flexibility). At today's market rates the range would be about $95,000-$115,000.

## The items

**Item 1.** The usual stress test for a plan built mostly on shares is a crash: one year in which shares fall 20% or more.
The team's first plan (27 September 2026) was tested that day and dropped before any trade. It held about three-quarters
of the money in shares to 2030, gliding to 40% in 2032, and on 1 January 2033 it would have bought all ten payments in
Treasuries with whatever the money had grown or shrunk to. In simulated markets it fell short in 3.2%, about 1 in 31, and
in 35.6% of those misses no year fell 20%, only several poor ones. A crash was never the test. A plan that must buy fixed
payments on one date fails on any run of years that leaves too little on that date, and no money comes after January 2028
to close a gap found then. So the danger was one date, 1 January 2033. 97.5% of misses had shares lower after the four
years at three-quarters, those four years carry about three-quarters of the shortfall, and the median miss was $27,695.

**Item 2.** The case asks for "a high degree of certainty", not certainty, and the common reading of that phrase is
"very likely": a plan that pays in full in 96.8 simulated markets out of 100 sounds as if it qualifies. The team's first
plan (27 September 2026) was tested that day. It held about three-quarters of the money in shares to 2030, gliding to 40%
in 2032, and on 1 January 2033 it would have bought all ten payments in Treasuries with whatever the money had grown or
shrunk to. It fell short in 3.2% of simulated markets, and it was dropped before any trade. "High" is measured against
what the same two deposits can buy. Bought into Treasuries first and sized to pay all ten even if cash waiting earns
nothing, they leave no payment short, by design. Each miss would also have been final: it was settled on 1 January 2033,
before any payment, and no money comes after January 2028 to close it. So 3.2% meant about 1 in 31 against none, with a
median miss of $27,695.

**Item 3.** Buy a Treasury bond and hold it to the end, the common reading goes, and you lock in its rate. A 1992
Baltimore Sun column said that anyone who bought the new 20-year Treasury bonds of January 1982, paying 14.25%, "would
have 'locked in' their higher rate until they mature in 2002". A bond locks in its interest payments and its face value,
not the rate those payments earn while they wait. Held to 2002, $1,000 of that bond grows to $15,690 only if every
interest payment also earns 14.25%. With each payment rolled over in six-month Treasury bills at the rates actually
paid, it reached $6,144, or 9.29% a year. A Federal Reserve bank's 1981 table shows where the difference goes. A bond
that pays nothing until the end keeps its full yield, 16% in the example. The same bond paying 16% interest along the way
earned about 14.2% once the rate on that interest fell to 12% halfway. Laura's Treasuries pay interest for years before
the payments they fund, and the competition's rules bar stripped Treasuries, the long bonds that pay nothing until the
end. So the plan counts the rate on waiting money at zero, the strictest rate practice used, and then also charges a
bill fund's 0.15% yearly fee. With $35,894 of extra Treasuries, all ten are paid even if cash waiting earns nothing.

**Item 4.** A lender reads a large company's written word of support as a promise. Kleinwort Benson lent to Malaysia
Mining's tin-trading company against a letter that said "It is our policy to ensure that the business of M.M.C. Metals
Ltd. is at all times in a position to meet its liabilities to you", and a High Court judge awarded the bank £12.26m with
interest. The tin market collapsed in October 1985. Malaysia Mining then wrote that the policy had been "our policy at
that time" and that "no assurance was given that such policy would not be reviewed in the light of changing
circumstances". The Court of Appeal set the award aside in 1989: the sentence was "a statement of present fact and not a
promise as to future conduct". It described the company's policy on the day, and the crash changed the day. Laura's 2031
figure describes something a crash cannot change. The figure co-sponsors count is the top: money she already owns in
Treasuries held for her before she names it. The bottom is the part held for her since January 2028, which, in the
plan's words, "will remain constant, built on the ever-reliable Treasuries". Once half the shares have moved into
Treasuries before the meetings, no fall in markets can change either end, and the top is $115,000 on today's figures.

**Item 5.** An artists' residency is usually pictured as its place: the house, the studios, the grounds. Louis Comfort
Tiffany's residency (1918) ran on his Long Island estate until its collections and property were sold in 1946 and 1949.
The Rauschenberg Foundation received about $326 million from the artist's estate in 2012 and began residencies on
Captiva that year. In August 2025 its board decided to sell the site after "recurring storm damage, broader climate
risks, and rising maintenance costs", and it was sold in March 2026. Both foundations kept paying artists after the sale:
Tiffany's turned to grants for artists, and Rauschenberg's moved the sale and upkeep money to artists' programmes
elsewhere. The money outlasted the building. The Aspen Institute's estate-planning notes for artists now tell them to
"provide sufficient liquid assets to the foundation to sustain its functions initially without art sales". Laura's ten
operating payments follow that advice in Treasuries. They are kept apart from her building contribution and owned
before the first is due, and none of them waits on selling anything: $50,000 each January from 2033 to 2042.

**Item 6.** The usual story of a founder's museum that closes is that the founder's money ran out: a fortune set aside,
then spent. Thirteen Taiwanese art institutions were found that were paid for by their founders (artists, their
families, collectors and companies), and the founder paid first in every one. Yet none had even one year of running
costs set aside when it opened. Four stopped when the income behind them stopped, the latest in 2025, when digital
photography ended the trade that had paid for the artist-run IT Park for 37 years. There was no fortune to run out. They
ran on the next year's income: a company's profit, sales of the artist's works, or the founder's own earnings. "I must
earn NT$14m a year to give here," Hong-Gah's founder said in 2003. Laura's ten operating payments are not next year's
income. Most of each is owned in Treasuries from January 2027 and the rest from January 2028, five years before the first
falls due in 2033.

**Item 7.** A portfolio's risk is usually judged by what it holds, its mix of shares and bonds, apart from what its owner
earns. The UK Pensions Regulator's own worked example is a house builder whose pension scheme holds property. Such a
scheme "could 'double-up' the risks associated with property markets": if property prices fell, its funding could fall
"at a time when the strength of the employer covenant is weakening and the availability of additional contributions to
the scheme becomes limited". So the regulator judges a fund together with whoever pays into it. Where that payer's
fortunes ride on one market, its fix is "diversification of scheme assets" away from that market. The team's plan makes
that move for a writer. In a recession her advances, speaking fees and licences can come later and smaller just as
shares can fall, so her career "is a large holding of shares, and one you cannot sell". No promised dollar is held in
shares, and only $29,829 of her $450,000 goes into them, on today's figures.

**Item 8.** The time value of money, finance's first rule, says money sooner is worth more than money later, so no one
should take less in order to be paid less often. Yet in a field study in Kenya, 86% of dairy farmers chose to be paid
monthly rather than daily even when the daily price was 15% higher. The authors found that the scarce part is the payer:
"many buyers lack the credibility to offer infrequent payments". A payment made later is worth only its payer's
credibility. Laura's ten payments come years after the money is set aside, so the plan has one payer make them all, the
US Treasury: $50,000 each January from 2033 to 2042.

## Reading orders

| Reader | Order | Row 10 version read first |
|---|---|---|
| A | 1, 3, 5, 7, 2, 4, 6, 8 | A (item 1) |
| B | 2, 8, 6, 4, 7, 1, 5, 3 | B (item 2) |
| C | 4, 6, 1, 3, 8, 5, 7, 2 | A (item 1) |

- **Row 10's two versions.** Items 1 and 2 are never next to each other, and every reader reads both.
- **Items 5 and 6.** These two (founders' institutions) are never next to each other either.
- **Positions.** Each item sits in a different position for each reader.
- **The second version is read knowing the first,** because both share the same facts. So each version is scored on
  its first read (item 1 by A and C, item 2 by B). The second read answers only which framing lands harder once both
  are known.

## What each reader writes, for each item

1. Before reading it, what did you assume about this, if anything? In one sentence: what does it show you had
   backwards (or "nothing new")?
2. Aha strength, 1 (nothing new) to 5 (changed how I see the plan).
3. Any claim that seems overstated, unclear or likely wrong: quote it and say why.
4. The one question you would ask the team.
5. New: the assumption you named in 1, in a few words, and how sure of it you were before reading, from 0 (a guess) to
   100 (certain). If you named none, write "none".

When you have finished all eight items, do this short task without looking back at the items: list ten countries in
alphabetical order. Then, still without looking back, write down from memory each item's key figure: one figure per
item, with the item's number, or "none" if nothing comes to mind.

Then: the three items you would still remember after reading 40 reports, and any two items that clash or repeat.

## For Keel: what the two new fields are, and the scoring key

- **What the new fields are.** Field 5 and the figure written after the filler task come from card Q107's "Cold tests"
  note. These readers are simulated, so both fields are only what each reader reports: a rough check on which assumptions
  were firmly held and which figure stands out. They never measure human confidence or human memory, and nothing these
  readers answer is cited as repeating card Q107's findings about people. A simulated reader can also see its whole
  context, so the filler stands in for a delay without creating one.
- **The score.** Aha strength, "remembered after 40 reports" and whether the key figure is written correctly are read
  together. Claims flagged in field 3 are fixed before any item lands.

| Item | Key figure (accept) |
|---|---|
| 1 | 35.6% of misses with no year down 20% (accept: one date, 1 January 2033; 3.2% or about 1 in 31; 97.5%) |
| 2 | About 1 in 31 against none (accept: 3.2%; 96.8 in 100; $27,695) |
| 3 | 9.29% a year, against the 14.25% "locked in" (accept: $6,144; nearly five points; $15,690) |
| 4 | $115,000, owned before she names it (accept: October 1985; £12.26m) |
| 5 | The sites sold, 1946-1949 and 2025-2026, while the giving went on (accept: about $326 million; $50,000 a year "without art sales") |
| 6 | None of 13 had a year of running costs set aside (accept: NT$14m a year; 37 years; four stopped) |
| 7 | $29,829 of $450,000 in shares (accept: "double-up") |
| 8 | 86% chose monthly even at a 15% higher daily price |

## Notes on each item (what it avoids, and why)

- **Items 1 and 2.**
  - They use only NUMBERS 8s and register row 10.
  - They never say "shares sold to pay each date" or "one of ten dates".
  - They never set 40.8% against "none" (13.7% and 40.8% are left out).
  - "None" rests on NUMBERS 2's standard, said "by design", never on the 27 Sep model's coded "never".
  - The event is told passively ("was tested", "was dropped"), without saying whose work it rested on (standing order 22).
  - Neither version claims the team believed a crash was the danger.
- **Item 3.**
  - "The strictest rate practice used", then a fee below it; never "below every assumption" (Q104 claim 2).
  - "14.2%" is Keel's rounding of Silver's 14.248%, so it is not confused with the 14.25% coupon.
- **Item 4.**
  - It leads with the top and says the bottom once, as the part held since January 2028.
  - It says "held for her", never "secured", "in her name" or "before shares had any say".
  - It does not say Laura can give more than the stated top.
  - It does not call a fund's payout fixed: "no fall in markets can change either end" is NUMBERS 4's "after the move
    nothing changes either end".
- **Item 5.**
  - The reserve is never called an endowment.
  - "About $326 million" rounds row 20's $325,978,217.
  - The Aspen quote was read through a page extract (Q101 Sources).
- **Item 6.**
  - "The founder paid first", never "the largest share".
  - "Found" stands for "the cases found, not a census" (Q100 row 41). Two of the four stops also had other causes (a
    scandal, a lost space), so the item names only IT Park's.
  - It says nothing about the residency's years after 2042. Test 3 failed the halls row partly for inviting "what after
    2042?".
- **Item 7.**
  - "Can", never "tends to".
  - It never says co-sponsors' budgets or her income "fall together".
  - "Employer covenant" stays inside the regulator's quoted words.
- **Item 8.**
  - Never "the same trade" or "the same bargain" (Q95 rater, Tue 17 Nov).
  - The farmers' own motive (to "tie their hands") is left out, since Laura's is a promise to others.
- **All items.**
  - No question marks.
  - None of "optimal", "natural hedge", CPPI, "portfolio insurance", "capital-protected", "fail-safe" or "the safe part
    does the growing".
  - No "barring a US default".
- **Holder named outside a card (items 1 and 2).** The belief's holder is a common reading, and no figure is drawn from
  it. Card Q8b (regulators' certainty standards) and card Q97 row 12 (TPR's minimum 1-in-6 stress, with a sponsor behind
  it) could give version B a named regulatory holder in a later round. They were left out here because the brief limits
  row 10 to NUMBERS 8s and the register.
