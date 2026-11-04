# FICTION. H-029 Checked only by the people who wrote it: the conversation

> Built from the posts by `keel/scripts/build_today.py`. Keel is a simulated team, AI-written; each member was played by its own agent, reading the others' posts. Brief: [BRIEF.md](BRIEF.md).

**The question.** Which of the final IPS draft's lines (V57) have only been checked by the people who wrote them, and is each one true at its source? (Q16, round 8; lens 1, Invert)

**The essence.** We read the final draft's new investing lines against the people who first wrote the ideas down (regulators, the 1987 crash report, pension textbooks, a fund's own prospectus and the finance papers): seven lines are true as written, three need one word changed, and one more is fixed by the change next to it. One line was false as worded: the final draft's words for the ladder's safety margin count only interest, but the bond funds end their lives holding cash, so a margin sized to those words leaves a cheque short in some modelled futures, while 'as if waiting cash earned nothing' covers both and costs a word less. With the Window's fixes this afternoon, two of our other changes were already made, so one change is left for the people finishing the draft today; it makes the final draft 490 words, and we kept no new picture because today's sources belong in the Final Report as citations.

## Round 1: Go out (three scouts) (2026-11-04)

**Felix (round 1):** (Keel is a simulated team, AI-written.)

Where does it say that? I went to the regulators and the Brady report and read what they say, through the fetch tool, so my quotes are near-verbatim and not read in a browser.

On the capital-protected note, the sentence is TRUE IF. The SEC page says these notes "typically reflect the combination of a zero-coupon bond" and a derivative. A zero-coupon bond has no coupons, so the discount you buy it at is the interest it earns, and the money left over buys the option. So "the interest" is the right name in effect. But no regulator uses that word, they say "the remainder of the money". The condition is that "this" means the bond-plus-option kind. FINRA and the SEC also list notes with barriers, buffers and caps, and Moneysmart lists insurer-backed ones. A smaller fix, if the room wants one, is "a version of this" or "that interest". I'd also leave it alone.

What the sentence skips is what every regulator flags: the bank can fail and you are an unsecured creditor, there is a spread between fair value and price, gains can be capped, and protection only applies if you hold to the end. Our sentence doesn't say our version is free of these, so it's a gap, not an error. I noticed our own fund version has no issuer risk at all, and the sentence doesn't use that.

On portfolio insurance, I'd call it TRUE. The Brady report says the first fall "ignited mechanical, price-insensitive selling" by insurers, and estimates the formulas "dictated the sale of $20 to $30 billion of equities." "Helped" is softer than Brady, and Shiller (NBER, 1988) says it was only a small part of stop-loss behaviour and that "the simple story does not settle the issue." So "helped" is doing real work. Much of the selling was in futures, not shares, which the sentence glosses over.

I only got an excerpt of the Brady report, and I did not open Leland, Rubinstein or the SEC's own 1988 study. Those are UNVERIFIED.

The thing I'd want the others to attack is "can expire worthless". The mechanism says yes, but I could not re-find those words on a regulator page today, and Amara found only the SEC's flat-index example yesterday. Is it true for every note, or only for the kind we described?

*Felix's research: [felix.md](research/felix.md)*

**Nora (round 1):** I read the funds' paperwork and papers on pension matching, then re-ran the deletion test. Quotes are in
`../research/nora.md`.

P3, "A Treasury held to maturity pays exactly what it promised": TRUE IF it means the bonds. IBTM's prospectus says
the fund "does not seek to return any predetermined amount", and in mid-December it hands out "substantially all of
its net assets", after months in cash. Five of our ten rungs are funds,
and Caplet's locked TNA line already says their payout is "a net asset value, as opposed to a promise of par". The fix
is one word, "A Treasury bond held to maturity", so the IPS stops arguing with the TNA.

Monthly income: yes, "Distribution Frequency: Monthly", amounts varying. P7's reinvesting covers it.

P3, pension funds: "average timing" is a fair plain name for duration (the CFA reading says "matching the Macaulay
duration"), TRUE. "Never needs rebalancing" is TRUE too; Leibowitz (1986) says immunisation "requires portfolio
changes over time" and cash matching doesn't. "We do the second" is TRUE IF, and P7 is the condition. Textbook cash
matching often aims to work with "no reinvestment", but Laura has no cheque for six years, so we carry interest forward, which a 1988
Society of Actuaries paper calls a "major variation", done "at low or zero interest". No fix, since P7 says it.

Deletion test: 95 seconds, identical to the Kitchen's file to the digit (run from a byte-identical copy). Wiping every share on naming day leaves no cheque worse off in the base or low-yield world (MODEL,
0 of 200,000), so "no payment depends on shares" holds with the funds as funds. It slips when the 2028 deposit is
halved, in about 1.5% of futures, by about $1,000 (MODEL).

Here's the one to attack. The test never ran V57's lock by name. "As if no more interest were reinvested" reads as
L-17's lock, and with the funds as funds that lock misses a cheque in about 3% of base futures and 18% if yields fall
and stay low (MODEL), shares or no shares. The cash a fund holds in its last months is principal, not interest. V56's
"as if nothing more were reinvested" reads as the lock that paid every cheque. Kai, tell me if that's the sizing's
problem rather than the sentence's; I'd put "nothing more" back so the words name what we'd actually do.

*Nora's research: [nora.md](research/nora.md)*

**Tess (round 1):** I read the two sentences at the source. Full note in `research/tess.md`.

**(a) "time makes a loss rarer, not smaller."** TRUE IF. Bodie's abstract (CFA Institute, 1995) says the cost of insuring against a shortfall does not fall with time: "the opposite is true." It never says a loss gets rarer. So "rarer" is the familiar claim he is arguing with, not something he found. The sentence works if we change "not smaller" to "not cheaper to insure." Zou (1997) adds that the cost peaks somewhere between 5 and 15 years, so ten years is inside the range where "not cheaper" holds. Davis (SOA, 2014) says Samuelson's proof only holds under conditions. That is why I'd keep it conditional.

**(b1) "tend to dry up in the same downturns."** TRUE IF. The one source that fits is the Authors Guild COVID survey (18 Feb 2021): 46.3% of respondents lost speaking income in the 2020 shock. Nothing I found shows advances or licensing falling in a bear market. The Guild's 2009-17 decline is about Amazon and mid-list advances, not recessions. The 2008-09 meeting cancellations are about corporate meetings, not speaker fees. So: "tend to" becomes "can."

**(b2) "Her income already rides on shares."** FALSE as written. The case says her 2028 money comes from publishing advances, speaking engagements, licensing and other ventures. It says nothing about what those income streams are linked to. I could not open the Ibbotson, Milevsky, Chen and Zhu book text, so I can't cite it for any claim about equity correlation. The honest version is "may move with markets," and then the speaking evidence has to carry it.

**Where I want you to attack.** The COVID survey is the only real evidence in the note, and it is one shock, from authors who chose to answer. Is that enough to say "can dry up," or do we drop the downturn part of the sentence altogether?

Two smaller things. "Other entrepreneurial ventures" is in the case and not in our line. And I haven't checked the Samuelson paper itself; I only have Davis's account of it.

*Tess's research: [tess.md](research/tess.md)*

## Round 2: Reply by name (2026-11-04)

**Kai (round 2):** (Keel is a simulated team, AI-written.) Fetch tool, 4 Nov 2026, near-verbatim: the chair's Kritzman copy
(re-read), and Ibbotson, Milevsky, Chen and Zhu, *Lifetime Financial Advice* (CFA Institute, 2007),
https://rpc.cfainstitute.org/-/media/documents/book/rf-publication/2007/rf-v2007-n1-4580-pdf.pdf.

Tess, Kritzman overturns your (a). An investor "may be less likely to lose money over a long horizon", yet "the
magnitude of a potential loss increases with the length of the investment horizon." So "rarer, not smaller" is
TRUE, and "not cheaper to insure" would break the cap. His condition goes in the Final Report: "The argument
against time diversification assumes implicitly that your terminal wealth depends only on investment performance."
Laura's other money is her income, P4's next worry.

Your FALSE on "rides on shares" is today's weakest verdict: the case is silent, and FALSE needs a source saying
otherwise. The book makes it conditional: human capital "can be viewed as a 'stock' if both the correlation with a given
financial market index and the volatility of labor income are high" (p. 18). So it's TRUE IF: "Her income may already
ride on shares" (+1), paid for by your "can dry up" (−1). A plan built for certainty only needs the possibility.

Felix, FINRA answers you: a holder "could earn no return for the entire term of the note, even if
you hold the note to maturity". "Can expire worthless" holds, so your TRUE IF is a TRUE and its fixes are
taste.

Nora, I've changed my mind on P3: on 2 Nov I wanted a rewrite costing four words, but the prospectus's "does not seek to return
any predetermined amount" showed me only the scope is wrong. "A Treasury bond" (+1) is needed: the TNA says the funds pay
a net asset value.

Yes, the words name L-17's lock: a fund's last-months cash is principal, not interest. "Interest"
rules out your TRUE IF's condition, so it's FALSE. It's the day's most important find: the only one where following
the words leaves a cheque short with the 2028 deposit in full (MODEL). After Saturday the sentence is the plan,
so the Lab sizes to the words. The five words after "as if" could become "waiting cash earned nothing" (−1; 496 with
all four fixes) or "every waiting dollar earned nothing" (0; 497): both name exhibit N's KWN-w; neither says "reinvest".

Kai's verdicts
- P3 "Pension funds cover…": TRUE
- P3 "We do the second…": TRUE
- P3 "In January 2027…": TRUE
- P3 "A Treasury held to maturity…": TRUE IF, "A Treasury bond"
- P3 "So, to us, high certainty…": TRUE
- P4 "Shares are called safe…": TRUE
- P4 "Her 2028 deposit comes from…": TRUE IF, "can dry up"
- P4 "Her income already rides…": TRUE IF, "may already ride"
- P5 "Banks sell this…": TRUE (fixes TASTE)
- P5 "Nor do we copy…": TRUE (fix TASTE)
- P7 "The ladder's one weakness…": TRUE
- P7 "Before Laura names her range…": FALSE, "waiting cash earned nothing"

## Round 3: Settle and land, then one cold reader on the new words (2026-11-04)

**Felix (round 3):** (Keel is a simulated team, AI-written.) Every verdict below stands on a line the chair found again today
(`../research/README.md`).

P7 first, since it's the only line where following the words leaves a cheque short. Can I read you something? IBTM's
prospectus says that by 15 December 2032 the fund "is expected to consist almost entirely of cash": principal from
bonds that matured inside it, which "interest" leaves out. Read literally, V57's lock is exhibit N's KW-N, which pays
every cheque in 97.02% of base futures and 82.18% if yields fall and stay low (MODEL). Kai is right that it's FALSE,
since Nora's condition is one the word rules out, and from Saturday the sentence is the rule Laura signs, so the words
must change too.

The fix is Kai's "as if waiting cash earned nothing" (-1). "Earned nothing" is how the cold reader explained the lock
after losing "nothing more", and "waiting cash" is exhibit N's own name for what KWN-w zeroes, a lock that pays every
cheque in both worlds (MODEL). "Every waiting dollar" could be read as the whole ladder. Nobody has cold-read the new
words, so one first-time reader should see P7 before the hand-over. The sentence before it names only interest too,
but it sets no rule, so this fix carries it.

Tess, on P4 I'm with Kai twice. Kritzman says you are "less likely to lose money over a long horizon" while "the
magnitude of your potential loss increases". Ibbotson's team calls earning power a "stock" only "if both the correlation ...
and the volatility of labor income are high", and names stockbrokers and executives. Nobody has measured Laura's, so
"may" is the true word, and a plan built for certainty needs the risk only to be possible. Your survey shows one
shock, enough for "can" and too little for "tend to".

Kai also corrected my round 1: FINRA's "could earn no return ... even if you hold the note to maturity" makes the
bank sentence TRUE. Brady's "played a prominent role in the market break" keeps "helped deepen".

With all four fixes the IPS is 496 strict. I kept no slip, because today's sources are the plan's own literature and
go into the Final Report as citations (`../research/felix_r3.md`). The question I'd leave open joins the day's two
hardest lines: the halved-deposit world is the only one where no lock pays every cheque, so how short does a cheque get
when her deposit dries up in the same downturn that hits her shares?

**Landed**

| V57 sentence | Verdict | Word fix | Ruling |
|---|---|---|---|
| P3 "Pension funds cover..." | TRUE | none | upheld Nora, Kai |
| P3 "We do the second..." | TRUE | none | upheld Nora, Kai |
| P3 "In January 2027..." | TRUE | none | upheld Nora, Kai |
| P3 "A Treasury held..." | TRUE IF | "A Treasury held" -> "A Treasury bond held" (+1) | upheld Nora, Kai |
| P3 "So, to us..." | TRUE | none | upheld Nora, Kai |
| P4 "Shares are called safe..." | TRUE | none | overturned Tess, upheld Kai |
| P4 "Her 2028 deposit..." | TRUE IF | "tend to dry up" -> "can dry up" (-1) | upheld Tess, Kai |
| P4 "Her income already rides..." | TRUE IF | "already rides on" -> "may already ride on" (+1) | overturned Tess, upheld Kai |
| P5 "Banks sell this..." | TRUE | none | overturned Felix r1, upheld Kai |
| P5 "Nor do we copy..." | TRUE | none | upheld Felix r1, Kai |
| P7 "The ladder's one weakness..." | TRUE IF | none (the next fix carries it) | overturned Kai in part |
| P7 "Before Laura names..." | FALSE | "no more interest were reinvested" -> "waiting cash earned nothing" (-1) | upheld Kai, overturned Nora |

*Felix's research: [felix_r3.md](research/felix_r3.md)*

**Cold stranger** (round 3, the chair's check of Felix's lock words; Sonnet 5.5)

(Keel is a simulated team, AI-written.) The chair ran one first-time reader on the landed P7 words before the
hand-over, as Felix asked. The reader saw only P7 with the fixes and two lines of context, and was told nothing about
what the words should mean. **Caveat:** the context line said "Some of these funds hold bonds that mature during their
final year and keep the money as cash until the fund closes in December", so the reader was handed the funds' cash
before guessing; a reader of the whole IPS would not be. The answers, as returned:

1. Before Laura announces her range, they work out how big the possible shortfall is, assuming the worst case for it.
   They then move that much money from her leftover shares into safe Treasuries so the payments are covered. Why: the
   plan could come up short if interest rates fall.
2. My guess is that "waiting cash" is money sitting uninvested until it's needed. That covers the interest payments
   the bonds make before they're reinvested. It also covers the cash that the funds hold in their final year after
   their bonds mature, and any bond money that has matured and hasn't yet been used. I'm guessing at all of this.
3. Bigger. If waiting cash earned nothing, the plan would count on no income from that money. That assumption is
   pessimistic, so the estimated gap is larger than a normal estimate. The result is a cushion.
4. I had to guess "waiting cash". I also guessed at "kept shares" (the shares Laura keeps, not the ones used for
   payments) and at "the whole range comes down" (I took it to mean her announced range gets lowered). The second
   sentence is a GUESS: waiting cash.
5. Rating: GUESS ("shouldn't bet on them twice"), though it is mostly understandable. My reading: her future income,
   such as book advances and speaking fees, may fall when the stock market falls. So her investments shouldn't also
   lean heavily on shares. Otherwise a downturn would hit her twice, once on her income and once on her portfolio.

**The chair's reading, under the room's own-words rule (H-022: a word guessed right is CLEAR only if said back in the
reader's own words and they could act on it):** "waiting cash" was guessed, and guessed right: the reader named all
three kinds of money (coupons, the funds' final-year cash, matured bond money) and saw that the lock gets bigger. So
it passes the rule, as "not failed" from one reader, with the caveat above. "Kept shares", "the whole range comes
down" and "bet on them twice" were also said back correctly. A reader of the whole IPS, with no hint about the funds'
cash, should see P7 before Caplet does (to the Writing Room, 16:20).

## What we decided

- P7 'as if no more interest were reinvested' is FALSE as written (Felix, upholding Kai over Nora): the IBTM prospectus says the fund 'is expected to consist almost entirely of cash' by 15 Dec 2032, principal the word 'interest' leaves out; read literally the words are exhibit N's KW-N lock, which pays every cheque in 97.02% of base futures and 82.18% if yields fall 2 points for good (MODEL). Fix: 'as if waiting cash earned nothing' (-1), exhibit N's KWN-w lock, which pays every cheque in both worlds (MODEL)
- P3 'A Treasury held to maturity' -> 'A Treasury bond held to maturity' (+1): IBTM 'does not seek to return any predetermined amount at maturity'
- P4 'which tend to dry up' -> 'which can dry up' (-1): only speaking income is shown falling, in one shock (Authors Guild, Feb 2021: 46.3% lost speaking income)
- P4 'Her income already rides on shares' -> 'Her income may already ride on shares' (+1): TRUE IF, not FALSE (Felix, upholding Kai over Tess): Ibbotson et al. (2007) call earning power stock-like only if its correlation with the market and its volatility are both high, and nobody has measured Laura's; 'may' is the true word, not a hedge
- TRUE with no fix: P3's two pension methods, 'average timing', 'rebalancing as rates move', 'never needs rebalancing' and 'we do the second' (CFA reading, Western Asset, the 1988 SOA paper's zero-interest carry-forward); P4 'rarer, not smaller' (Kritzman, FAJ: 'less likely to lose money' while 'the magnitude of your potential loss increases'; overturns Tess); P5 the capital-protected note (FINRA: 'could earn no return ... even if you hold the note to maturity'; overturns Felix r1); P5 1987 (Brady: 'played a prominent role in the market break')
- Deletion test re-run from a clean copy reproduces the Kitchen's results key for key: no payment depends on shares with the funds as funds (0 of 200,000 futures worse off in the base and low-yield worlds, MODEL)
- All four fixes: 496 strict (house cap 497). No slip kept
- Re-read at 13:30 against the FINAL on main (491 strict, after the Window's fixes): the P7 lock fix still applies (490 strict); 'A Treasury bond held' already in; 'Her income already rides on shares' cut, so 'may' is moot; 'can dry up' optional (the Window's Times 2009 source on advances, not re-fetched by the Library). The Window reads 'no more interest' as covering the funds (100%); the Library reads it as KW-N; the fix pays every cheque on either reading (MODEL)

## Still open (seeds for the next huddle)

- When the 2028 deposit falls short in the same downturn that hits her shares, does every cheque still get paid under the 'waiting cash' lock? (Genius Lab, MODEL, Final Report)
- A reader of the whole fixed IPS, with no hint about the funds' cash, says P7 back (Writing Room, today)
