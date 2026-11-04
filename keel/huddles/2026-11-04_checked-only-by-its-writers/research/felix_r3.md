# H-028 round 3 · Felix's working note: the count, the lock against exhibit N, the Final Report shelf (Wed 4 Nov 2026)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code). Not a Caplet deliverable. Every source line used
below is one the chair re-found today (`README.md`); a line marked "not re-found" carries no verdict. Every model figure
is MODEL (V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17 + exhibit N; 22 Oct 2026 curve; J.P. Morgan 2027 LTCMA
global equities 7.5%; 200,000 paths, seed 20261016) and none goes into an IPS line (Book 11).

## 1. The count

Three scratch copies in this folder; the FINAL file was only copied, never counted or edited.
- `felix_r3_scratch_V57.txt`: a byte copy of `keel/ips_rewrite/drafts/FINAL/ips.txt` (the baseline).
- `felix_r3_scratch_landed.txt`: V57 with the four fixes I land (below).
- `felix_r3_scratch_alt_dollar.txt`: the landed text with Kai's 0-word lock instead ("as if every waiting dollar earned nothing").

The four fixes (`diff felix_r3_scratch_V57.txt felix_r3_scratch_landed.txt`):

| Para | Old | New | Words |
|---|---|---|---|
| P3 | A Treasury held to maturity | A Treasury bond held to maturity | +1 |
| P4 | which tend to dry up | which can dry up | -1 |
| P4 | Her income already rides on shares | Her income may already ride on shares | +1 |
| P7 | as if no more interest were reinvested | as if waiting cash earned nothing | -1 |

Command, run from the repo root:

    for f in V57 landed alt_dollar; do echo "== $f"; python3 keel/office/tools/textcheck.py keel/huddles/2026-11-04_checked-only-by-its-writers/research/felix_r3_scratch_$f.txt --limit 497; done

Output:

    == V57
    words: 493 by spaces (a spaced dash counts), 496 split on hyphens; quote the larger
    characters: 2835
    word limit 497: PASS (stricter count 496, margin 1)
    non-ASCII characters: 0
    == landed
    words: 493 by spaces (a spaced dash counts), 496 split on hyphens; quote the larger
    characters: 2834
    word limit 497: PASS (stricter count 496, margin 1)
    non-ASCII characters: 0
    == alt_dollar
    words: 494 by spaces (a spaced dash counts), 497 split on hyphens; quote the larger
    characters: 2842
    word limit 497: PASS (stricter count 497, margin 0)
    non-ASCII characters: 0

**IPS with every fix I endorse: 496 strict (493 by spaces), cap 497, margin 1.** Same as Kai's four-fix figure. The
pitch (48) is untouched: none of the four phrases is in it.

## 2. Each lock candidate against exhibit N

Exhibit N (`keel/rooms/courtroom/C-06_w5_on_trial/EXHIBIT_N.md`) scores locks with the five fund rungs at net asset
value. KW zeroes coupons paid after naming day; KWN-w also zeroes the cash a fund holds after the bonds inside it
mature ("the funds' waiting cash", its own words), with the 0.07% fee unpriced; KWN adds the fee. What the IPS words
must do: name a lock that, followed literally, pays every cheque. IBTM's summary prospectus (re-found today): "By
December 15, 2032, the Fund is expected to consist almost entirely of cash"; that cash is principal from matured
bonds, so a lock worded on "interest" leaves it out.

| Words after "as if" (in P7) | +/- | What a literal reader zeroes | Exhibit N arm | Every cheque, base / yields 2 pts lower for good (MODEL) | First-time reader | Landed |
|---|---|---|---|---|---|---|
| "no more interest were reinvested" (V57) | 0 | coupons only | **KW-N** | **97.02% / 82.18%**; short p50 $1,372 / $2,160 when short | not cold-read (added after the read) | **FALSE** |
| "nothing more were reinvested" (V56, Nora's fix) | -1 | all waiting money | KWN-w (Nora's reading; exhibit N never scored these words by name) | 100.00% / 100.00% | **LOST**: the cold reader took it as "stop reinvesting", a change of plan (`../../../ips_rewrite/drafts/FINAL/COMMANDMENTS_CHECK.md`, LOST 1) | true, unreadable |
| "its interest from then on earned nothing" (cold reader's own fix, never in a draft) | +3 | interest only | KW-N | 97.02% / 82.18% | the reader's own frame | same hole as V57 |
| "later bond payments sat idle" (C-06's older words) | 0 | KWN-w only if a reader counts the bonds inside a fund as "bond payments" | KWN-w by exhibit N's definition | 100.00% / 100.00% | a reader won't look inside the funds | not chosen |
| "every waiting dollar earned nothing" (Kai) | 0 | KWN-w if read as cash; read as every dollar waiting for a January, it zeroes the bonds' own coupons too, a lock nobody scored | KWN-w (or unscored) | 100.00% / 100.00% for KWN-w | ambiguous | not chosen; 497, margin 0 |
| **"waiting cash earned nothing" (Kai)** | **-1** | coupons once paid and the funds' cash after their bonds mature | **KWN-w** | **100.00% / 100.00%** | keeps the cold reader's "earned nothing"; "waiting cash" is exhibit N's own noun; **not yet cold-read** | **landed** |

Limits that travel with the landed words (MODEL): the fee is unpriced in KWN-w, yet exhibit N scores it with the fee in
the real leg and every cheque is still paid in both worlds. Exhibit N has **no S9 row for KWN-w**; in S9 (yields 1 pt
lower before the build, 2028 deposit halved) no lock pays every cheque (KW 98.71%, KW-N 91.97%, KWN 98.27%), because
there the money to buy the lock or a rung was never there (L-17). The funds' real maturity dates are unread (exhibit
N spreads them evenly, its ASSUMPTION). None of this goes into an IPS line.

## 3. What carries each verdict (re-found lines only)

| V57 line | Verdict | Carried by |
|---|---|---|
| P3 "Pension funds cover fixed payments either by..." | TRUE | CFA refresher reading 2026: "immunization is achieved by matching the Macaulay duration of the bond portfolio to the horizon date"; "the portfolio needs to be rebalanced" |
| P3 "We do the second, which never needs rebalancing." | TRUE | Western Asset (Pieterse 2023) heading: "Cash Flow Matching Eliminates Rebalancing, Drawdown and Liquidity Risk"; the reinvestment it still needs is P7's, and rebalancing is a different act |
| P3 "In January 2027 ... each maturing before a January payment." | TRUE | IBTM summary prospectus: "will terminate on or about December 15, 2032" |
| P3 "A Treasury held to maturity pays exactly..." | TRUE IF -> "bond" | IBTM summary prospectus: "The Fund does not seek to return any predetermined amount at maturity or in periodic distributions."; Caplet's locked TNA: "a net asset value, as opposed to a promise of par" |
| P3 "So, to us, high certainty means no payment depends on shares." | TRUE | Nora's re-run of the deletion test (MODEL): shares wiped on naming day, 0 of 200,000 futures with a cheque worse off in the base and low-yield worlds; it slips only with the 2028 deposit halved |
| P4 "Shares are called safe ... rarer, not smaller ... can't wait for a recovery." | TRUE | Kritzman (course copy): "although you are less likely to lose money over a long horizon than over a short horizon, the magnitude of your potential loss increases with the duration of your investment horizon."; Bodie 1995: "For guarantors of money-fixed annuities ... unambiguously wrong." |
| P4 "... which tend to dry up in the same downturns ..." | TRUE IF -> "can" | Authors Guild 2021: "46.3% reported losing income from speaking engagement cancellations."; "12.9% ... book contract cancellations or payment delays"; one shock, 669 self-selected respondents; nothing found for a pattern ("tend") |
| P4 "Her income already rides on shares ..." | TRUE IF -> "may already ride" | Ibbotson et al. 2007 p. 18: human capital "can be viewed as a 'stock' if both the correlation with a given financial market index ... and the volatility of labor income are high."; p. 16 "the typical investor need not worry"; their examples are stockbrokers, portfolio managers and executives; the case is silent (lines 43-45) |
| P5 "Banks sell this as a capital-protected note ..." | TRUE | SEC 2011: "typically reflect the combination of a zero-coupon bond" (and a derivative); FINRA 2023: "could earn no return for the entire term of the note, even if you hold the note to maturity"; ASIC: "invest the remainder of the money in options and other derivatives" |
| P5 "Nor do we copy portfolio insurance ... helped deepen the 1987 crash." | TRUE | Brady 1988 p. 41: "played a prominent role in the market break"; p. v "ignited mechanical, price-insensitive selling"; Shiller 1988 (the dissent in degree): "might be one important factor" |
| P7 "The ladder's one weakness ... its bonds' interest ..." | TRUE IF, no fix | The same prospectus line as the lock: the funds also reinvest matured principal ("the proceeds will typically be reinvested"). It describes the weakness and sets no rule, so the next sentence, once it says "waiting cash", carries the condition |
| P7 "... as if no more interest were reinvested ..." | FALSE -> "waiting cash earned nothing" | Section 2 |

## 4. The slip: nothing kept today

A slip needs a source from outside the plan whose mechanism works like a part of it. Every source today is the plan's
own literature: the regulators describe the very note P5 rejects, Brady the very insurance P5 rejects, the SOA paper
the very carry-forward P7 prices, Ibbotson the very human-capital idea P4 uses. Each is a citation, and a citation
needs no picture. The nearest thing to a picture is the SOA's "cash carry-forward (at low or zero interest)" with
"To be conservative, one would set ... [the carry-forward rate] to be small" (OCR: l_t), which is P7's lock in an
actuary's words; it goes into the Final Report as the convention, not as a slip. No `felix_slip_S-13.md` written.

## 5. Where each source goes in the Final Report (one line each)

Re-found today unless marked; criteria are Wharton's five.
- **SEC Office of Investor Education, 2011** (structured notes with principal protection): Investment Strategy, why not a bank note: zero-coupon bond plus derivative, spread over fair value, caps, issuer credit.
- **FINRA, 2023**: Investment Strategy, "could earn no return ... even if you hold the note to maturity" and the unsecured-creditor risk our Treasury floor doesn't carry.
- **ASIC Moneysmart, 2013 PDF and web page**: Investment Strategy, a second regulator's plain account (bond portion, "the remainder ... in options", protection only if held to term); optional beside SEC and FINRA.
- **Brady report, 1988**: Investment Strategy, why no portfolio insurance; quote p. 41 "played a prominent role in the market break" and the "$20 to $30 billion" estimate.
- **Federal Reserve History, Bernhardt and Eckblad**: Investment Strategy, the plain one-line account ("accelerated the crash's pace") and the other causes.
- **Shiller, NBER Macroeconomics Annual 1988**: Investment Strategy, the dissent in degree, cited beside Brady so a judge sees why the IPS says "helped".
- **Bodie, FAJ 1995**: Investment Strategy and Client Knowledge, why fixed cheques can't lean on time ("For guarantors of money-fixed annuities ... unambiguously wrong").
- **Kritzman, FAJ (course copy at Buffalo)**: Investment Strategy, "rarer, not smaller" in his words; open the publisher's page before citing; his condition on terminal wealth (Kai's fetch, not re-found) is the bridge to human capital once re-fetched.
- **Zou, FAJ 1997** (one line re-found): Portfolio Analysis, insurance cost peaks "typically between 5 and 15 years", so ten years sits at the peak.
- **Ibbotson, Milevsky, Chen and Zhu, 2007**: Client Knowledge, the human-capital rule with its two conditions, the advice to hold less risky assets when income moves with markets, and plainly that Laura's case is a risk we plan for, not a measured fact.
- **Authors Guild, COVID-19 Survey 3, 2021**: Client Knowledge, speaking income lost in one shock (46.3%), book contracts (12.9%), options unpaid (3.4%), with its limits; the 2020 share-price fall is not on that page, so fetch a market source before the FR says "same downturns".
- **The case, lines 43-45 and 61-65**: Client Knowledge, the deposit's four sources, "other entrepreneurial ventures" included.
- **IBTM summary prospectus, 27 Feb 2026**: Portfolio Analysis, no "predetermined amount", the December close, the last months in cash: the waiting cash the lock zeroes.
- **CFA Institute refresher reading, 2026**: Investment Strategy, immunisation as duration matching that "needs to be rebalanced".
- **Western Asset, Pieterse 2023**: Investment Strategy, cash-flow matching "Eliminates Rebalancing".
- **Kocherlakota, Rosenbloom and Shiu, TSA 1988**: Portfolio Analysis, the lock is the actuaries' conservative convention for carried-forward cash.
- **Not re-found, not citable until opened:** Leibowitz 1986 parts I and II (the "no reinvestment" line, the best single source for P7; re-fetch first), the IBTM/IBTO fact sheets ("Monthly"), the 2025 terminations release, BlackRock UK's LDI note, the Duke page, Davis (SOA 2014), the SLCG note, the Authors Guild "42 percent" page, Business Travel News, Zou's other lines.

## 6. The seed

**If the 2028 deposit comes in short in the same downturn that hits Laura's shares, which is P4's own warning, does
every cheque still get paid under the "waiting cash" lock, and if not, which IPS words promise too much?** Exhibit N's
S9 halves the deposit without tying it to a share fall, and has no KWN-w row. For the Lab after Saturday, MODEL,
Portfolio Analysis in the Final Report. Smaller open item: IBTM-IBTR's real maturity dates (the holdings files), before
the FR repeats exhibit N's even spread.

## 7. For the rewrite thread (files I did not edit)
- `keel/ips_rewrite/drafts/FINAL/README.md` section 3 says the V57 lock "can only overstate it, so every cheque is paid
  in every modelled future". With the funds as funds that holds for "waiting cash earned nothing" (KWN-w), not for
  "no more interest were reinvested" (KW-N), and not in S9 under any lock.
- `COMMANDMENTS_CHECK.md`, "Applied after this check" item 4, says the cold reader's "earned nothing" version would
  "say the same" as "no more interest": both name interest only, so both miss the funds' waiting cash.
- One first-time reader should read P7 with "waiting cash" before the hand-over; nobody has yet.
