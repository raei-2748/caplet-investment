# FINAL IPS for Caplet's review (Wed 4 Nov 2026, Sydney)

**AI DRAFT (Claude, 4 Nov 2026). GPTZero: not yet checked.** This is Keel's final candidate, V56
(`../D36/`). Caplet reads it Thu 5 Nov, rewrites it in its own words, and submits it on the SMApply form by
**Sat 7 Nov 09:00 Sydney** (Fri 6 Nov 5:00 p.m. ET). Keel doesn't submit anything.

- `pitch.txt`: the 50-word elevator pitch field. **48 words.**
- `ips.txt`: the 500-word IPS field. **493 words** on the strict count (hyphenated words split; `keel/office/tools/textcheck.py`).
  The house cap is 497.
- `COMMANDMENTS_CHECK.md`: the Commandments, Book 11 and I80 check, filled in by a cold reader who didn't write V56.

## 1. The checks
| Check | Result |
|---|---|
| **Commandments (cold reader)** | PASS 5 (II, III, IV, V, VII), FAIL 2, OPEN 3. Both FAILs were record-keeping and are now done: VIII (the idea ledger now records V55 and V56) and X (the thinking log has its "What Caplet would say"). The reader's three text fixes are in: the reinvestment method logged, "redeemed for each January", and "just" cut. OPEN: I (panel, now run, below), VI (GPTZero), IX (rank agreement). Book 11: PASS 8, OPEN 1 (sounds human: GPTZero). I80 habits: PASS 8, OPEN 1 (the closing line) |
| **Panel V56 (six blind judges, Wharton's criteria only)** | V56 above V55 (Ray's plain rewrite) with **five of six**. First with the actuary ("the only plan where I can follow every cash flow from 2027 to 2042 without a forecast propping up a promise") and the teacher. Our plan is first with four of six judges across its versions. V54's older wording beats V56 with four of six on style, which is Caplet's call (section 5). `../../judges/panel_V56/SUMMARY.md` |
| **Cold read (first-time reader)** | All four say-backs right: the ending (never sell a holding before it matures, even for the building); what protects the payments (Treasuries held to maturity, no payment depends on shares); 2031 and the shortfall rule. It found the closing sentence "a tidy slogan" (see section 5) |
| **Book 11** | No opening question. No model numbers, "our model" or citations. No team history. No subheadings. Caplet XR set up in P2 ("do not crush") and paid off in the last sentence |

## 2. Every number and where it comes from
| In the IPS | Source |
|---|---|
| $50,000 each January, ten years from 2033 (to 2042), "a high degree of certainty", the residency | The case, Operating Commitment (client profile lines 87-92) |
| $300,000 in January 2027; the 2028 deposit and its sources (book advances, speaking, licensing) | The case, lines 43-45 ("publishing advances, speaking engagements, licensing, and other entrepreneurial ventures") |
| $450,000 | $300,000 + $150,000, from the case |
| The 2031 range for co-sponsors | The case, lines 109-115 (co-sponsors approached in 2031) |
| "a Treasury fund maturing in late 2032" | IBTM's summary prospectus (27 Feb 2026): holds Treasuries maturing in 2032; the fund terminates "on or about December 15, 2032" (Library, 2 Nov) |
| "less than a tenth" of her money in shares | MODEL: the floor's expected interest is about 6.6% of $450,000 at the 30 Oct curve, and stays under a tenth for five-year yields up to about 6.9%. The frozen WInS book holds VT at 8.6% (snapshot 23 Oct). Stated as an allocation, not a model output |
| about 7.5% a year from shares | J.P. Morgan 2027 Long-Term Capital Market Assumptions (released 19 Oct 2026), global equities in US dollars (Window, 27 Oct, `../../../office/outbox/2026-10-27_window_7-5-and-three-checks.md`). It's the same figure as the submitted Trading Notes. Stated as an assumption that no payment relies on |
| ten Treasury holdings | The WInS book: five iBonds Treasury funds and five Treasury bonds (`competition/wins/2026-10-23_snapshot.md`) |
| half her shares | The plan's own rule, not a number from outside |

## 3. What changed since V33 (Fri 30 Oct), and why
V33 was the Book 10 draft (`../D13/`). It opened with team history ("We started where most investors would ...") and
printed model results ("one future in thirty", "97 times in 100", "one time in four").
- **Book 11 (Ahaan, 1 Nov) rebuilt it (V50).** Out went the team history, every model number and "our model" (all
  moved to the Final Report, with each idea's landing in `../../IDEA_LEDGER.md`), the opening question and the
  subheadings. Caplet XR now runs full circle, and every sentence has to make plain sense.
- **The rooms' fact-checks (V51-V54).** No wording may be false at its source. An XR pill may sometimes be opened; it's
  crushing that breaks it. The floor is a Treasury fund, not loose Treasuries. "A fifteenth" holds only at today's
  yields, so it's now "under a tenth". "Do not crush" had to say what it forbids: selling a holding before it matures,
  even for the building. The reinvestment money needed a home (Treasuries) and a place in the operating reserve.
- **Ray's note (3 Nov): it reads as AI and corny (V55).** The slogan flips, two-word kickers, "That is X." runs and the
  one-line ending all came out (the habit list is in `../D35/README.md`). The ideas stayed.
- **The last real hole (V56).** The gap from reinvesting at lower rates used to be priced once, at that day's rates.
  Now it's priced as if nothing more were reinvested, which can only overstate it. So every cheque is paid in every
  modelled future, and no cheque depends on shares. The cost is that her spare shares are used up more often, and the
  IPS says so ("Her spare money shrinks first").

## 4. GPTZero: still not checked, and the one-minute check
Book 10 asks for GPTZero "human-written" above 50% before Caplet sees a draft. Keel couldn't run it. On Tue 3 Nov
gptzero.me loaded from Keel's session for the first time, but sending the draft's text to it was refused by the
session's permission check. So there is no score, and none has been made up.
**The one-minute check (any teammate):** open gptzero.me in a browser, paste the text of `ips.txt` into the free box,
run the scan, and note the human-written figure it gives. Do the same for `pitch.txt` if you like. Below 50%, tell
Keel which sentences it highlights, or rewrite those first: the team's own words are the real fix.

## 5. Caplet's calls (Keel's recommendation in brackets)
1. **V56's plain wording or V54's.** The mock judges preferred V54's wording 4-2. Ray read that style as AI and corny,
   and one judge called V54's ending "a brochure". (V56: the judges are machines too, and their taste in prose is the
   one thing not to trust them on. V54 is in `../D34/`; V56's reinvestment rule drops into it in one sentence if you
   want it.)
2. **The closing sentence**, "Like the tablet it is named after, the plan works as long as nobody crushes it." The
   cold reader and the Commandments reader both found it a little neat. (Keep it, or end on the reserve sentence. Your
   ear is the test.)
3. **Printed confidence levels.** The rival that beats us with some judges prints them. Book 11 and Wharton keep
   projections for the Final Report. (Leave them out.)
4. **The 7.5% assumption.** (Keep it. It's named, sourced and not load-bearing.)
