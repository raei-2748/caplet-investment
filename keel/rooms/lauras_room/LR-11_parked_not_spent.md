# LR-11: parked, not spent? (Laura's Room, Tue 3 Nov 2026, round 7 beat 6; huddle H-024)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code). MODEL. Not for submission.

**For a judge, first.** The Lab's new rule for the ladder's one weak point (set money aside on naming day as if nothing
more is reinvested, so nobody has to look again) keeps every cheque and the named range safe. Someone pays for it, and
it is Laura's flexibility: the stocks she keeps run dry by 2033 more often. But most of that money is parked, not spent:
the cheques almost never need the full zero-rate amount, and public bond escrows, which are sized exactly this way,
hand the leftover back to the owner once what remains still covers every later payment at zero. V54 says her
flexibility pays; it never says it comes back.

## 1. The question (round 7 beat 6: the Lab's challengers, read three ways)
The Genius Lab (13:40, H-023, `../lab/L-17_interest_that_earns_nothing.md`) adopted Kai's lock (C1, arm KW) and binned or
parked C2-C4. This room reads each as a co-sponsor deciding whether to give, as a competition judge with the case open,
and as the practitioner from the field the lock came from (public defeasance escrows), and asks who pays for C1.

## 2. The test (chair's check for the huddle)
`LR-11_parked_not_spent.py` reuses the Lab's L-17 chain unchanged and adds one parameter to its arm function: the
stocks Laura keeps pay the lock only down to a share of themselves (a quarter: this room's Monday rule, LR-10 H25; a
half: H50); the rest comes from the range's money on naming day, so the range is lowered before anyone hears it. KW
re-run here equals the Lab's `results.json` (asserted: cheques, gift mean, Laura's 2042 mean, range lowered).
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA world stocks 7.5% | 200,000 paths, seed 20261016 |
rho 0.5 unless S0 | V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17 | MODEL. Results: `LR-11_results.json`.

## 3. Results (MODEL; base / yields 2 points lower for good / yields 1 point lower before the build + 2028 deposit halved)
| | KW (the lock) | KW + keep a quarter (H25) | KW + keep a half (H50) |
|---|---|---|---|
| Every cheque in full | 100% / 100% / 98.71% | 100% / 100% / 98.69% | 100% / 100% / 98.67% |
| Kept stocks all gone by Jan 2033 | 28.1% / 72.8% / 90.3% | 0.0% / 1.5% / 11.0% | 0.0% / 0.4% / 3.6% |
| Kept stocks in Jan 2033, mean | $12,039 / $3,338 / $449 | $13,406 / $5,641 / $1,731 | $15,627 / $8,334 / $3,136 |
| Range lowered on naming day | 26.9% / 71.9% / 89.1% | 39.8% / 79.6% / 94.0% | 57.1% / 86.7% / 97.8% |
| Median top she names | $165k / $145k / $35k | $160k / $140k / $35k | $160k / $140k / $35k |
| Top reached once named | 99.3% / 99.6% / 99.8% | 99.5% / 99.6% / 99.75% | 99.6% / 99.6% / 99.7% |
| Gift below the named bottom | never | never | never |
| Gift mean | $159,286 / $141,580 / $35,983 | $157,800 / $139,450 / $34,802 | $155,495 / $137,013 / $33,545 |
| Laura's own money in 2042, mean | $48,722 / $24,914 / $17,639 | $51,954 / $29,988 / $20,434 | $57,062 / $35,859 / $23,454 |
| Lock not needed, back to her after 2033, median (incl. the 2027 leftover) | $17,953 / $12,633 / $12,350 | the same | the same |

- **Who pays for the lock:** Laura's flexibility in January 2033 (median $8,746 under KW against $14,319 under V54 as
  written, base, the Lab's table; KW's mean $12,039), not the gift (KW costs it about $670 on average against the
  unnamed second look) and never the cheques.
- **Most of it comes back:** the median $17,953 the cheques never needed returns to her after 2033 (it includes the 2027
  leftover). The model counts it in her 2042 money but does not time it rung by rung.
- **H25 under the lock:** her pocket is never empty in 2033 in the base world (0.0% v 28.1%), the gift mean falls
  about $1,500 and the median top she names falls $5,000; she ends 2042 about $3,200 richer on average (the kept
  quarter stays in stocks). In a bad world the quarter is small (a mean of $1,731 to $5,641): a principle, not a
  building overrun.

## 4. The Lab's challengers, read three ways (huddle H-024; posts in `../../huddles/2026-11-03_parked-not-spent/posts/`)
| | Co-sponsor and SIMULATED Laura (Amara) | Practitioner: public escrows, their own words (Kai) | Judge with the case and Wharton open (Felix) | Verdict |
|---|---|---|---|---|
| C1 Kai's lock | Officer: no cheque ever touches the gift once named, and the range is trimmed before she hears it: fundable (:109-116). Laura: it buys a safe cheque with her flexibility (:101-103), and "money paid later" asks "paid by whom?" | The field doesn't price reinvestment, it sizes it out: "sufficient, without reinvestment" (MWRA 2025-2 s3; Mendocino-Lake 2022 s5(iii)). Escrows hand the leftover back to the owner, early only on a sufficiency test (Wisconsin 2021 s4.1(b), s4.5; Santa Monica 2018 s3.1; MWRA s7, s10). "Never look again" is wrong: they look again, only to give money back | The lock is the evaluation :99 asks for and meets :119-120. Weakest answer of V54 + C1: flexibility (p.4; :102-103): it is spent and never said to come back | **SHARPEN 3-0**: wording A; keep a quarter back; P9 says the money comes home |
| C2 bank's note, bond first | Moves neither seat | Escrows hold government bonds, not bank paper | P5 already goes floor first; no words to spare | **BIN** |
| C3 how likely the top is | Answers :117, but in the Final Report | The field says "sufficient", never "likely" | Wharton: "a final facility-contribution range" is "Not expected in the IPS"; P6's "already in bonds" is the plain version | **Final Report** |
| C4 the faces add up to less | Moves neither seat | Every verification schedule is that table | P8 already gives the reasoning | **Final Report** |

## 5. Case check on what survives (Felix, round 1; the chair's re-read)
- :94-99 size, initial composition, change as payments are made: P3 + P9 name and run down the ladder; thin but passes.
  With the add-on, it also says what happens to the money the zero-rate rule over-sets: the answer to Wharton's IPS
  question 4 gets its second half.
- :96-99 certainty defined (P3), evaluated (P8: priced at its worst, bought), assumptions named (7.5%; "as if nothing
  more is reinvested"): passes, and stronger with A, which names the assumption in plain words.
- :117 "state how confident": not in words, and not expected in the IPS (Wharton s2). Final Report.
- Flexibility (p.4; :102-103; :146-148): the weakest. Fixed at both ends by the package (a quarter kept on naming day;
  the unneeded money returned after 2033).

## 6. Verdict and offer (round 3 votes)
- P8 A, 3-0. Flexibility "both", 3-0. P9 "...and returning to Laura what the cheques don't need." ("to Laura" 2-1 over
  "her"; "the cheques don't need" 2-1 over Kai's "what no remaining cheque needs", left to the Writing Room's strangers).
- Paid by "for good", "first", "over the long run", "in a downturn" (2-1; Amara: "roughly"). 497 strict.
- Offer: `../../ips_rewrite/inbox/2026-11-03_lauras-room.md`; full text `LR-11_offered_ips.txt`.

## 7. Limits
- The model credits the lock's leftover to Laura's 2042 money but does not time it rung by rung; "returning to Laura"
  is a rule (the escrows' test), not a modelled cash-flow schedule.
- Kai's escrow quotes were read through WebFetch (near-verbatim; the fetch script got HTTP 403 on every escrow host);
  Wisconsin s4.1(b) was read twice and matched in order. Check every quote at its source before the Final Report prints it.
- No escrow Kai read keeps a slice liquid for the issuer at the start: the quarter is our rule, not the field's (it
  doesn't break the field's rule; the cheques barely move).
- Same model limits as L-17: yields floored at 0.25%; the five fund rungs paid at par, not net asset value.
