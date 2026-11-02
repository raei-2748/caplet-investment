# FICTION (the room) + real work. Huddle H-016: two jobs, one pocket (Genius Lab, Mon 2 Nov 2026, round 6 beat 5)

> (Keel is a simulated team, AI-written.) Chair: Amara (builder, 13:40). Members: Jun (head of the Lab; today's cold
> judge), Kai (roasts; the round's flaw-hunter). One round, three agent calls (the routine's cap of three subagents);
> the chair lands it from what the three actually posted and writes no member's lines.

## The question
V52 (`../../ips_rewrite/drafts/D32/ips_V52.txt`, AI DRAFT, 495 strict) gives the stocks Laura keeps two jobs. P6:
"The other half stays with Laura, liquid any day, as her flexibility, in case the building costs more in Taiwan
dollars." P8: "Before she names the range, we price that gap at the day's yields and set it aside from the stocks
Laura keeps; whatever they can't cover lowers the whole range." Two open requests to the Lab:
- Library (H-015 seed 2): in the bad cases, how much of the kept half does the reinvestment gap take by Jan 2033, and
  how often is nothing left?
- Laura's Room (Kai, H-011): LR-09's world S9 (yields a point lower before the 2027 build + 2028 deposit halved) bounces
  a cheque in 1 in 66 futures, median gap $5,032. Is that a rung never bought, or thin reinvestment after 2033? Does
  Laura's half kept to 2042, or a bigger 2031 set-aside, close it, at what cost to the gift?

## What the test found (L-16, MODEL; `../../rooms/lab/L-16_two_jobs_one_pocket/`, results.json)
STAMP: curve 22 Oct 2026 | J.P. Morgan 2027 world stocks 7.5% | 200,000 paths, seed 20261016 | V52's design via the
Lab's L-13 -> L-14 chain (= L-15's "same day" arm) | MODEL. Worlds: S0 independent, S1 linked (rho 0.5), S2 deposit
halved, S6 yields fall 2 points just after the build for good, S9 = S2 + yields a point lower before the build.

1. **The model sets aside a $7,500 margin on top of the gap priced at the day's yields (LR-05's C). V52's text does not
   say so** (IDEA_LEDGER D6 had "with a cushion ..." IN; V52 lost it). Without the margin, all ten cheques are paid in
   full in 76% of futures (S0; median gap when short $3,076, all of it reinvestment after 2033); with it, 99.82%.
   S6: 47% v 99.68%. Cross-check on a separate code path (L-11 D1, Wed 28 Oct, 2033 set-aside only): 26.8% short with no
   cushion, 0.34% with $7.5k (S0).
2. **The kept half (S0 / S1 / S2 / S6 / S9):** the gap (with its margin) takes some of it in 71 / 71 / 72 / 88 / 99% of
   futures; half or more in 38 / 37 / 61 / 77 / 98%; **all of it in 19 / 21 / 42 / 65 / 86%**. Median left in Jan 2033:
   $13.9k of an untouched $21.7k (S0); $0 of $13.3k (S6). Unused margin comes back to Laura after the last cheque.
3. **S9's gap is the deposit, not reinvestment:** of the short dollars, 35% a rung never bought (the $300,000 bought less
   ladder at lower yields and the halved deposit couldn't finish it), 49% the 2033 gap with no floor or stocks left to
   pay it, 15% after 2033. Kept stocks as a backstop to 2042: 98.49% -> 98.50%. A $15,000 margin: 98.58%, and the gift's
   mean falls $37,464 -> $30,166.
4. **Challenger G, gap first, then halve** (the gap comes out of all the stocks, then the rest is split): flexibility
   gone in 6.6% (S0) instead of 19%, 47% instead of 65% (S6); costs: gift mean -$2.4k (S0), median top $160k v $165k,
   and the gift falls below the quoted bottom in 3 in 10,000 futures (S0), 15 (S6), 31 (S9), which breaks "money she
   already owns". Laura's 2042 money +$6.3k mean.
5. **Kept stocks as a backstop after 2033 with the margin (B0):** cheques 99.82% -> 99.94% (S0); sold after 2033 in
   0.13% of futures. Without the margin (B1): 92%.

## The offers on the table (Book 11: no number in the IPS; cap 497 strict)
- **m1** (`offer_V52_m1.txt`, 498): P8 "we price that gap at the day's yields, add a margin, and set it aside ..."
- **m3 + cut** (`offer_V52_m3_cut.txt`, 497): m1 plus "..., so her flexibility shrinks before her promise does.
  Whatever they can't cover lowers the whole range."; paid by cutting P3's mirror "We don't invest toward these
  payments. We buy them." (the pitch keeps it; two cold readers called the repeat a set piece)
- **FR only:** the margin as a pharmacist's overage. ICH Q8(R2) s2.2.2 (fetched 2 Nov 2026): "In general, use of an
  overage of a drug substance to compensate for degradation during manufacture ... or to extend shelf life, is
  discouraged."; overages "should be justified"; give "1) amount of overage, 2) reason for the overage ... and 3)
  justification for the amount of overage." Break: the regulator's better answer is a stable formula; ours would be
  zero-coupon Treasuries, which Wharton bans.

## Rules
Wharton's word first (`../../WHARTON_WORD.md`); the case's "Preserves appropriate financial flexibility when
determining the facility contribution" (case :145) and "committing all remaining assets could limit her financial
flexibility as the project develops" (:102-103). Book 11 (`../../BIBLE.md`): no model numbers, no "our model" in the
IPS; every sentence plain. Simulated people are tests, never quotes.
