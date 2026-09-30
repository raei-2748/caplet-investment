"""Build the WInS note briefs and EXAMPLE notes: rab/trades/notes.csv and rab/trades/notes.md.

WS6-notes, RAB Kit, 30 Sep 2026 (Sydney). AI-generated (Claude Code, Claude Opus 5.5) for Team Caplet.
Every exemplar is labelled "EXAMPLE - team rewrites". Students write the notes that go into WInS; this file is
research support, logged in docs/AI_USE.md. Nothing here is sent to WInS, the IPS or the Sheet.

Inputs (read-only):
  rab/trades/tickets.csv           Friday tickets, Gate A basis (both books)
  rab/numbers.yaml                 locked numbers (sha256 must match rab/numbers.lock)
  rab/trades/trades_clock.py       every time printed in ET and Sydney time (zoneinfo)
Outputs:
  rab/trades/notes.csv             ticker, brief, exemplar, char_count, then book, seq, note_id, use, label,
                                   numbers (each analytic number in the exemplar = its numbers.yaml source)
  rab/trades/notes.md              briefs, exemplars, the three Trading Notes Analysis picks, reflection outlines

Run from the worktree root:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/build_notes.py
It exits 1 if any exemplar fails a check (length, ASCII, one paragraph, banned words, role word, Laura anchor,
untraced number) or if numbers.yaml does not match its lock hash. Checks are the Gate C spec in rab/premortem.md
(items 1-5, 10-11) applied to notes.
"""
import csv
import hashlib
import os
import re
import sys
from collections import Counter
from datetime import datetime

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from trades_clock import ET, both  # noqa: E402

LABEL = "EXAMPLE - team rewrites"

# ----------------------------------------------------------------------------------------------- word rules
# One rule set for exemplars and team drafts: rab/trades/note_rules.py (standard library only).
from note_rules import BANNED, MAX_NOTE, ROLE_WORDS, check_text, pick_anchor  # noqa: E402,F401
from note_check import WHARTON_EXAMPLE  # noqa: E402  (official example note, for its length only)

IPS_SNAPSHOT = os.path.join(HERE, "data", "ips_doc_text_2026-09-30.txt")

# ----------------------------------------------------------------------------------------------- IPS sentences
# Quoted exactly from the IPS Google Doc 1qtEuzXq_QYdQ9VJlusPY9km2l80E1hkk8FPR0iw71-w, read 30 Sep 2026 (Drive
# connector, read-only). The doc is marked "EXEMPLAR ONLY. NOT FOR SUBMISSION."; the strategy text is the adopted one.
IPS = {
    "PITCH": "Laura's 2027 deposit buys Treasuries maturing before each of her ten $50,000 payments.",
    "LATEST": "The January 2027 deposit buys the liability-hedging portfolio, latest payments first.",
    "FALL": "A moderate fall in yields would leave some payments for the 2028 deposit to complete",
    "FLOOR": ("Part of the remainder buys Treasuries maturing in late 2032 that, with coupons reinvested, repay the "
              "whole remainder as Laura's facility floor."),
    "FIRST": ("The roots, meaning the payments and facility floor, are secured before anything is invested in the "
              "branch, the return-seeking portfolio."),
    "BRANCH": ("The rest, plus any 2027 remainder, forms the return-seeking portfolio, a global index fund of "
               "thousands of companies held to 2033."),
    "DECLINE": "A market decline can reduce the facility contribution, but not below the floor.",
    "HELD": ("In January 2033 the hedging portfolio becomes the operating reserve, held to maturity and shrinking as "
             "each holding pays out."),
    "SCALED": "Our WInS portfolio shows the allocation after both deposits, scaled down.",
    "COST": "At September 2026 yields the ten payments cost less than $300,000.",
    "RANGE": ("In 2031 Laura will give co-sponsors a range from the floor to the floor plus half the equity fund's "
              "value then."),
    "CUSHION": "The other half remains with Laura as a cushion if costs rise or co-sponsors fall short.",
    "EQUITY": ("Equities should outperform Treasuries over five years but can fall sharply, so moving money from the "
               "floor into equities raises the expected outcome modestly but widens the range of results."),
}


# ----------------------------------------------------------------------------------------------- the notes
# Each spec: exemplar text; the numbers it uses (token -> source, digits or words); its Friday-fact slot (where the one
# thing only WInS showed that day goes, and how many characters it adds); brief fields. Sizes come from tickets.csv.
# Payment order: 1 Jan 2033 is Laura's 1st payment ... 1 Jan 2042 her 10th (case: ten $50,000 payments 2033-2042).
# Revised 30 Sep after the judge panel (round 1, c11b02f) and again after round 2 (104476c): rab/trades/judge_response.md.
# Round 2: IBTR says 'cost', 'first deposit', 'fall in yields' and who absorbs a gap; no 'set amount' alone; low coupon
# framed as less of her payment resting on reinvested coupons; T40c retired (staged trade); IBTM_R, T40s, SW37, IBTR_F
# added; picks may not share an opening; every exemplar marks its Friday-fact slot.
SLOT_NAME = ("name swap: type the exact WInS name string in place of ours", 0)
NOTES = [
    dict(
        id="IBTR", ticker="IBTR", books={"Portfolio": 1, "BookL": 1}, use="Friday order 1 (both books)",
        rung="IBTR", job="payments", tn_role="tested", pick="Pick 1 (tested)",
        serves="Laura's 5th payment, $50,000 on 1 Jan 2037 (2027 deposit)",
        facts=["iShares iBonds Dec 2036 Term Treasury ETF: 4 Treasuries maturing in 2036; ends on or about "
               "15 Dec 2036; pays income monthly (iShares, 28 Sep)",
               "the test this note records: before the first order, `refresh_tickets.py` prints what Laura's ten "
               "payments cost on 1 Jan 2027 at the latest yields. The IPS claims it is under $300,000 (28 Sep: about "
               "$292,000, laura.ladder.cost_2027_strips). It fails if yields fall more than about a quarter of a "
               "percentage point before then (laura.ladder.breakeven_fall_bp_strips). The 14 Oct check re-runs it "
               "(october_trade.md trigger B); the reflection reports that result either way",
               "basis: both figures are the numbers.yaml zero-coupon (STRIPS) basis. Under the adopted rule reading "
               "R1(a) (`assumptions.md`) her real ladder is the WInS-listed one, which costs more and has less room: "
               "WS4 gets 22.8bp with yields unchanged and WS7 about 22bp on the buyable ladder (both UNVERIFIED for "
               "quoting until WS1 locks them, request 9). Use one basis in the note, the reflection and the IPS",
               "if it fails on Friday: do not stop. Buy orders 1-10 from the `--split-from-curve` ticket (more in the "
               "dated holdings, less VT), as the IPS says: the 2028 deposit tops up the earliest payments before any "
               "stocks (friday_checklist.md; exemplar IBTR_F in s5)",
               "who absorbs a gap: the 2028 deposit tops up the earliest payments first, so the stock fund gets less; "
               "no payment is missed (WS4 `D_pre2027_rate_hedge.md`: the gap lands on the stock fund). 'Latest "
               "payments first' is the IPS funding rule, not the order of WInS trades",
               "thinnest fund: about $38m in assets (iShares, 28 Sep); place it after the first hour"],
        ips=["COST", "LATEST", "FALL"],
        number=("'a quarter of a percentage point' (the fall in yields before 1 Jan 2027 that lifts the ten payments "
                "above $300,000; the note says 'over about', because the room is used up only past it)",
                "laura.ladder.breakeven_fall_bp_strips (26.2bp, MODEL, 28 Sep curve, zero-coupon basis). If WS1 locks "
                "a buyable-basis break-even before Friday, use its quote_as (about a fifth, if it is about 22bp) in the "
                "note, the reflection and the IPS alike. $50,000 and $300,000 are case facts"),
        dont=["'payments under her deposit' without the word 'cost' (reads as ten $50,000 payments under $300,000)",
              "'her $300,000 deposit' without 'first' (the WInS book is also $300,000)",
              "'a fall of a quarter point leaves...' (a fall must be MORE than the break-even, and 'point' alone is a "
              "price point)",
              "'any gap falls on her first payment' (a large fall reaches several of the earliest; the IPS says "
              "'some payments')",
              "that the fund pays a set $50,000; 'thin' or 'risky' about the holding",
              "'we buy the latest payments first' (the IPS funding rule, not the WInS trade order)"],
        friday=("Friday fact, inside the note: the curve date ('at 1 Oct yields'). Write the refresh line 'ten payments "
                "cost $X on 1 Jan 2027' in the Trade Log. If X is above $300,000, type IBTR_F (s5) and follow 'If the "
                "IBTR test fails' in friday_checklist.md. Use the WInS name string for IBTR in the Trade Log. If IBTR "
                "cannot be bought, the order becomes IBTQ and this note changes."),
        slot=("inside: 'at 1 Oct yields'", 0),
        exemplar=("Tested before this first order: at 1 Oct yields, Laura's ten $50,000 payments cost under her "
                  "$300,000 first deposit. This fund is future funding for the fifth. If yields fall over about a "
                  "quarter of a percentage point by January, her 2028 deposit tops up the earliest; stocks get less."),
        nums={"a quarter of a percentage point": "laura.ladder.breakeven_fall_bp_strips (26.2bp, zero-coupon basis)"},
    ),
    dict(
        id="IBTQ", ticker="IBTQ", books={"Portfolio": 2, "BookL": 2}, use="Friday order 2 (both books)",
        rung="IBTQ", job="payments", tn_role="supported",
        serves="Laura's 4th payment, $50,000 on 1 Jan 2036 (2027 deposit)",
        facts=["iShares iBonds Dec 2035 Term Treasury ETF: 4 Treasuries; ends on or about "
               "15 Dec 2035; monthly income (iShares, 28 Sep)",
               "WInS lists no Treasury maturing between 15 Feb 2031 and 15 Feb 2036 (43 bonds in the drop-down, "
               "SEEN 29 Sep), so a dated fund is the closest fit for the 2033-2036 payments"],
        ips=["PITCH"],
        number=("none needed: the dated gap in the WInS bond list is the fact", "tab WInS Notes, SEEN 29 Sep"),
        dont=["that no Treasury matures in those years at all (notes do; WInS just does not list them)",
              "that the fund repays or delivers a set $50,000"],
        friday="Friday fact: the WInS name string for IBTQ, copied exactly; re-read the drop-down for the gap.",
        slot=SLOT_NAME,
        exemplar=("For future funding: the iShares iBonds Dec 2035 Term Treasury ETF is for the fourth of Laura's ten "
                  "$50,000 residency payments, due 1 Jan 2036. WInS lists no Treasury bond maturing between Feb 2031 "
                  "and Feb 2036, so a dated fund is the closest fit. What its income earns can vary."),
        nums={},
    ),
    dict(
        id="IBTP", ticker="IBTP", books={"Portfolio": 3, "BookL": 3}, use="Friday order 3 (both books)",
        rung="IBTP", job="payments", tn_role="supported",
        serves="Laura's 3rd payment, $50,000 on 1 Jan 2035 (2027 deposit)",
        facts=["iShares iBonds Dec 2034 Term Treasury ETF: 4 Treasuries; ends on or about 15 Dec 2034; monthly "
               "income (iShares, 28 Sep)",
               "fair-price test: on 28 Sep the fund's price was 0.06% above the value of the Treasuries it holds (NAV "
               "$24.09, close $24.10; wins.ibond_checks.IBTP.premium_to_nav_pct). The note reports the test on the "
               "trade date, not 28 Sep: a 28 Sep premium says nothing about the 2 Oct order. The premium, not the "
               "fund's yield, is the test: a fund holding only Treasuries always yields about the Treasury curve",
               "why it matters to Laura: the payments leave little room under her $300,000 first deposit (about $7,600, "
               "laura.ladder.headroom_2027_strips), so paying a premium for a fund would eat into it (reflection only)"],
        ips=["PITCH"],
        number=("'almost exactly' (the fund's price against the value of its Treasuries, on the trade date)",
                "wins.ibond_checks.IBTP.premium_to_nav_pct = 0.06 on 28 Sep; re-run on the trade date. A figure such "
                "as 'within 0.1%' needs the quote_as WS1 adds at the Friday re-lock (request 2)"),
        dont=["'her money' or 'Laura's money' for WInS cash (her deposit arrives in Jan 2027)", "'bp'",
              "that the yield is locked in for Laura",
              "'its yield was close to the Treasury curve, so the price was fair' (a Treasury fund's yield always is)"],
        friday=("Friday fact, inside the note: 'On the trade date'. Compare the WInS price with the latest NAV on the "
                "iShares IBTP page (Thursday's). If the gap is more than about 0.1%, write what you found instead. Copy "
                "the WInS name string for IBTP."),
        slot=("inside: 'On the trade date' (the premium re-checked on Friday)", 0),
        exemplar=("The iShares iBonds Dec 2034 Term Treasury ETF is future funding for Laura's $50,000 residency "
                  "payment on 1 Jan 2035. On the trade date its price was almost exactly the value of the 2034 "
                  "Treasuries it holds, so we paid a fair price; its end value is not fixed."),
        nums={"almost exactly": "wins.ibond_checks.IBTP.premium_to_nav_pct (0.06% on 28 Sep; re-run on the trade date)"},
    ),
    dict(
        id="IBTO", ticker="IBTO", books={"Portfolio": 4, "BookL": 4}, use="Friday order 4 (both books)",
        rung="IBTO", job="payments", tn_role="supported",
        serves="Laura's 2nd payment, $50,000 on 1 Jan 2034 (2027 deposit)",
        facts=["iShares iBonds Dec 2033 Term Treasury ETF: 11 Treasuries; ends on or about 15 Dec 2033, when it pays "
               "out; monthly income (iShares, 28 Sep)",
               "trap: in WInS, IBTN is INSCORP Inc (SEEN 29 Sep); no iShares iBonds Treasury fund uses the ticker IBTN "
               "(iShares iBonds Treasury list, 30 Sep). The name check belongs in the Trade Log and in the Final "
               "Report's account of the team's experience, not in the note"],
        ips=["PITCH"],
        number=("none needed", "-"),
        dont=["anything about IBTN in the note (record the check in the Trade Log)",
              "anything unkind about the other company", "'which then closes' (reads as the fund failing)"],
        friday=("Type IBTO and IBTN once each; copy both names exactly as WInS shows them into the Trade Log. Friday "
                "fact: the WInS name string for IBTO."),
        slot=SLOT_NAME,
        exemplar=("Role: future funding. The iShares iBonds Dec 2033 Term Treasury ETF is for the second of Laura's ten "
                  "$50,000 payments, on 1 Jan 2034. WInS lists no Treasury bond maturing in 2033, so we use a fund of "
                  "2033 Treasuries that pays out that December. Its reinvested income can vary."),
        nums={},
    ),
    dict(
        id="IBTM_P", ticker="IBTM", books={"Portfolio": 5}, use="Friday order 5 (Portfolio book)",
        rung="IBTM", job="payments + floor", tn_role="supported",
        pick="Alternate A (supported); pick 2 if no refined note exists",
        serves=("two jobs: Laura's 1st payment, $50,000 on 1 Jan 2033 (2027 deposit), and the facility floor, the least "
                "she plans to give the facility (2028 deposit)"),
        facts=["iShares iBonds Dec 2032 Term Treasury ETF (SEEN in WInS 29 Sep): 15 Treasuries; ends on or about "
               "15 Dec 2032; monthly income (iShares, 28 Sep)",
               "WInS lists no Treasury maturing in late 2032 (SEEN 29 Sep), so the IPS floor ('Treasuries maturing in "
               "late 2032') sits in this fund, together with the 2033 payment. Under the adopted rule reading R1(a) "
               "Laura's real plan is limited to WInS-listed securities too, so this fund is her floor holding as "
               "well. Late-2032 Treasury notes (4.125% 15 Nov 2032, 91282CFV8; 3.75% 30 Nov 2032, 91282CPM7; MSPD "
               "Table V, 31 Aug 2026) are an option only under reading (b)",
               "both jobs fall due in Jan 2033 and come from different deposits (the payment from 2027, the floor "
               "from 2028): neither ranks behind the other",
               "iShares says its iBonds funds \"do not seek to return any predetermined amount\" (IBTM product page, "
               "28 Sep 2026)",
               "the limit, measured: if its income is reinvested at only 2%, IBTM delivers about 97% of the curve case, "
               "the least exposure of any rung (reinvest.rung.IBTM at_2pct 48,192 / at_curve 49,856; M9). Quote it only "
               "after WS1 adds a quote_as (request 4)",
               "Portfolio tab: 32.5% of the book, of which 24.3 points are the floor",
               "Laura's plan: the floor costs about $117,000 of her 2028 deposit at the 28 Sep 5-year yield "
               "(laura.floor_cost_2028, MODEL; never in a note)"],
        ips=["FLOOR", "PITCH"],
        number=("none in the exemplar ('about a third of our WInS portfolio' is available if the team trims)",
                "wins.portfolio.holdings_close_0928 IBTM weight 0.3254 (WInS book)"),
        dont=["'then' between the payment and the floor (both are due in Jan 2033, from different deposits)",
              "that it 'covers', 'repays' or 'holds' a dollar amount (never '$150,000' next to this holding: PM-15)",
              "any 2031 dollar figure: range, top or co-sponsor amount (TN guide: not expected yet); the idea of the "
              "2031 range is welcome",
              "'facility floor' without its gloss (the TN Analysis is read before the IPS)"],
        friday=("Re-read the WInS bond list for a late-2032 Treasury (if one appears, tell Ray before trading). Friday "
                "fact: the WInS name string, or the Preview price, dated, if the team wants it as the one number "
                "(the exemplar leaves room for about 30 characters). If the team adopted the backstop sentence at "
                "the 1 Oct vote, type IBTM_R (s5) instead."),
        slot=("room for the Preview price, dated (e.g. ' Bought at $21.76 on 2 Oct.')", 27),
        exemplar=("Future funding and risk management: the iShares iBonds Dec 2032 Term Treasury ETF has two jobs in "
                  "Laura's plan: her first $50,000 payment and the facility floor (the least she plans to give) she "
                  "can name to co-sponsors in 2031. Its end value is not fixed."),
        nums={},
    ),
    dict(
        id="IBTM_L", ticker="IBTM", books={"BookL": 5}, use="Friday order 5 (Book L only)",
        rung="IBTM", job="payments", tn_role="supported",
        serves="Laura's 1st payment, $50,000 on 1 Jan 2033 (2027 deposit); Book L holds no floor",
        facts=["iShares iBonds Dec 2032 Term Treasury ETF (SEEN 29 Sep): ends on or about 15 Dec 2032; monthly income",
               "WInS lists no Treasury maturing in late 2032 (SEEN 29 Sep)",
               "Book L = Laura's 2027 deposit dollar for dollar: the floor and the stock fund are bought in 2028 "
               "and never appear in WInS"],
        ips=["PITCH"],
        number=("none needed", "-"),
        dont=["the floor (Book L does not hold it)", "'repays $50,000'",
              "'with its income reinvested' as a comfort (whether WInS pays ETF income into cash is UNVERIFIED)"],
        friday="As for the Portfolio book.",
        slot=SLOT_NAME,
        exemplar=("Role: future funding. The iShares iBonds Dec 2032 Term Treasury ETF ends before the first of Laura's "
                  "ten $50,000 residency payments, on 1 Jan 2033. WInS lists no Treasury bond maturing in late 2032, "
                  "so this dated fund is the closest fit; its end value is not fixed."),
        nums={},
    ),
    dict(
        id="T41", ticker="T 3.125% 15-Nov-2041", books={"Portfolio": 6, "BookL": 6},
        use="Friday order 6, first bond (both books)", rung="T_3.125%_15-Nov-2041", job="payments",
        tn_role="supported",
        serves="Laura's 10th and last payment, $50,000 on 1 Jan 2042 (2027 deposit)",
        facts=["U.S. Treasury bond 3.125% due 15 Nov 2041, CUSIP 912810QT8; matures 47 days before the payment; "
               "coupons twice a year",
               "no iBonds Treasury fund ends from Dec 2037 to Dec 2043 (the list ends Dec 2036, then Dec 2044; iShares, "
               "30 Sep), so the 2038-2042 payments use individual bonds",
               "same-date alternate 2.000% 15 Nov 2041 (912810TC2, MSPD): the 1 Oct rule is the same as for Nov 2040: "
               "listed and inside its 25bp band means swap on Friday (SW41). Aug-maturity low coupons (1.125% Aug 2040, "
               "1.75% Aug 2041) are not same-date alternates",
               "in Laura's plan its set coupons plus principal come to about 86% of the $50,000 (reinvest.rung at_0pct "
               "43,047); reinvesting coupons covers the rest (appendix only)",
               "WInS price 76.367 (28 Sep) is 1.9bp from the curve: passes"],
        ips=["PITCH"],
        number=("none needed", "-"),
        dont=["'each with a set amount due at maturity' (reads as a set $50,000; the face is about $29,000 in Book L)",
              "that the bond delivers a fixed $50,000 including coupons", "'between 2037 and 2043' (does 2037 count?)"],
        friday=("Price inside the 25bp band; if the 2.000% Nov-2041 is listed and passes, type SW41 instead. If WInS "
                "lists no 2.000% Nov 2041, the team may add 'WInS lists no lower-coupon bond of that date' if it fits. "
                "Friday fact: the WInS name string for the bond."),
        slot=SLOT_NAME,
        exemplar=("Role: future funding. The 3.125% Treasury bond maturing 15 Nov 2041 is for the last of Laura's ten "
                  "$50,000 payments, on 1 Jan 2042. No iBonds Treasury fund ends from 2037 to 2043, so her last five "
                  "payments use individual bonds; part of each payment comes from reinvested coupons."),
        nums={},
    ),
    dict(
        id="T40b", ticker="T 4.250% 15-Nov-2040", books={"Portfolio": 7, "BookL": 7},
        use="Friday order 7 (both books), default: WInS does not list the 1.375% Nov-2040",
        rung="T_4.250%_15-Nov-2040", job="payments", tn_role="supported",
        serves="Laura's 9th payment, $50,000 on 1 Jan 2041 (2027 deposit)",
        facts=["U.S. Treasury bond 4.250% due 15 Nov 2040, CUSIP 912810QL5; WInS price 89.186 (28 Sep) is 5.1bp "
               "from the curve: passes",
               "same-date alternate 1.375% 15 Nov 2040 (912810ST6): it exists (MSPD Table V, 31 Aug 2026); its WInS "
               "listing is UNVERIFIED until the Friday drop-down read. About 38% of the 4.250% bond's cash before 2041 "
               "comes as coupons, against 17% (M9, MODEL; not in numbers.yaml)",
               "which note (the 1 Oct rule, one rule for all same-slot alternates): T40b if WInS does not list the "
               "1.375%; SW40 if it is listed and its price passes the 25bp check; T40s if it is listed but its price "
               "fails. T40 and T40c are retired (T40c kept a better listed bond for October: a staged trade)",
               "T40b records a constraint, not a change, so it is not a 'refined' pick; pick 2 then goes to IBTM_R or "
               "IBTM_P (s6)"],
        ips=["PITCH"],
        number=("none from numbers.yaml; the M9 coupon shares (38% vs 17%) need a numbers.yaml entry before any "
                "note uses them", "M9_selection.md (MODEL)"),
        dont=["'less income to reinvest' (reads as a loss: say less of her payment rests on reinvested coupons)",
              "'we are checking' (the drop-down read settles it before the order)", "that a swap will happen"],
        friday=("Read the drop-down first. Not listed: this note. Listed and passing: SW40. Listed but failing: T40s. "
                "Friday fact, inside: 'Its price passed our curve check'."),
        slot=("inside: 'Its price passed our curve check'", 0),
        exemplar=("Future funding: the 4.250% Treasury bond maturing 15 Nov 2040 is for the ninth of Laura's ten "
                  "$50,000 payments, on 1 Jan 2041. A lower-coupon bond of that date would leave less of her payment "
                  "resting on reinvested coupons, but WInS does not list one. Its price passed our curve check."),
        nums={},
    ),
    dict(
        id="T39", ticker="T 4.375% 15-Nov-2039", books={"Portfolio": 8, "BookL": 8},
        use="Friday order 8 (both books)", rung="T_4.375%_15-Nov-2039", job="payments", tn_role="supported",
        pick="Alternate B (supported: certainty)",
        serves="Laura's 8th payment, $50,000 on 1 Jan 2040 (2027 deposit)",
        facts=["U.S. Treasury bond 4.375% due 15 Nov 2039, CUSIP 912810QD3; matures 47 days (about seven weeks) before "
               "the payment",
               "WInS price 91.363 (28 Sep) is 6.6bp from the curve: passes",
               "the certainty alternate: the one note that says what Laura is owed and what she is not. In her plan "
               "the rung is about $25,000 of this bond; its set coupons plus principal come to about 86% of the "
               "$50,000 (reinvest.rung.T_4.375%_15-Nov-2039 at_0pct 42,947) and reinvesting coupons covers the rest",
               "trap: WInS also lists a 4.375% bond of 15 Feb 2038, with a stale price; pick by coupon AND date"],
        ips=["HELD"],
        number=("'most of' (the share of the payment owed as set coupons and principal); 'about seven weeks' is date "
                "arithmetic", "reinvest.rung.T_4.375%_15-Nov-2039 at_0pct 42,947 of 50,000 (MODEL); a percentage "
                "needs a quote_as from WS1 first (request 11)"),
        dont=["'the U.S. government owes a set amount' on its own (reads as the whole $50,000)",
              "that its price cannot fall (it can)",
              "'we hold it to maturity' about WInS (the WInS book freezes on 6 Nov; holding to maturity is Laura's plan)"],
        friday="Price inside the 25bp band. Friday fact: the WInS name string for the bond.",
        slot=SLOT_NAME,
        exemplar=("Future funding: the 4.375% Treasury bond maturing 15 Nov 2039 ends about seven weeks before Laura's "
                  "$50,000 residency payment on 1 Jan 2040. Its price will move, but held to maturity its set coupons "
                  "and principal cover most of that payment; reinvesting coupons covers the rest."),
        nums={"most of": "reinvest.rung.T_4.375%_15-Nov-2039 (at_0pct 42,947 of 50,000, about 86%)"},
    ),
    dict(
        id="T38", ticker="T 4.500% 15-May-2038", books={"Portfolio": 9, "BookL": 9},
        use="Friday order 9 (both books)", rung="T_4.500%_15-May-2038", job="payments", tn_role="supported",
        pick="Alternate C (supported, with a price check)",
        serves="Laura's 7th payment, $50,000 on 1 Jan 2039 (2027 deposit)",
        facts=["U.S. Treasury bond 4.500% due 15 May 2038, CUSIP 912810PX0: the latest Treasury bond maturing before the "
               "payment (MSPD Table V, M9); it ends about 7.6 months early (231 days), and in Laura's plan that money "
               "waits in Treasury bills (0% in WInS)",
               "price check: this bond 14.4bp from the curve (passes). The 4.375% Feb 2038 bond at 99.98 (the 28 Sep "
               "close, seen in WInS 29 Sep) was 92bp off and the 4.5% Feb 2036 at 102.95 was 111bp off (both stale). "
               "The Feb 2038 bond was only the runner-up and ends earlier, so the check did not change the choice",
               "why a 25bp band: the five good prices sat 2 to 15 hundredths of a percentage point of yield from the "
               "curve and the stale ones 92 and 111 hundredths (wins.bond_check.*), so a quarter point separates them",
               "the Sheet records this bond's accrued interest as 0.530; 1.66 is right on 28 Sep (1.71 on 2 Oct): fix "
               "before 6 Nov"],
        ips=["PITCH", "COST"],
        number=("none: 'about seven and a half months' is date arithmetic (15 May 2038 to 1 Jan 2039 = 231 days). "
                "'Almost a full percentage point of yield' (the stale gap) is available once WS1 aligns its quote_as "
                "(request 3)", "wins.bond_check.T_4.375%_15-Feb-2038 gap_bp -92.1 (MODEL)"),
        dont=["that WInS is 'wrong' or 'broken' (say 'stale')", "'bp'", "'1 point of yield' (reads as a price point)",
              "'the Feb 2038 bond' without its coupon (WInS lists more than one)", "the Sheet's accrued-interest typo"],
        friday=("Re-check both prices on Friday. If the Feb 2038 price now passes, keep the stale reading dated 29 Sep "
                "or say what Friday's check showed. Friday fact, inside: 'Its WInS price passed our curve check'."),
        slot=("inside: 'Its WInS price passed our curve check'", 0),
        exemplar=("Role: future funding. The 4.500% Treasury bond maturing 15 May 2038 is the last before Laura's "
                  "$50,000 residency payment on 1 Jan 2039, so its money waits about seven and a half months. Its "
                  "WInS price passed our curve check; on 29 Sep the 4.375% Feb 2038 bond's price was stale."),
        nums={},
    ),
    dict(
        id="T37", ticker="T 4.750% 15-Feb-2037", books={"Portfolio": 10, "BookL": 10},
        use="Friday order 10, last bond (both books), if WInS does not list the 5.000% May 2037",
        rung="T_4.750%_15-Feb-2037", job="payments", tn_role="supported",
        serves="Laura's 6th payment, $50,000 on 1 Jan 2038 (2027 deposit)",
        facts=["U.S. Treasury bond 4.750% due 15 Feb 2037, CUSIP 912810PT9; matures about 10.5 months (320 days) before "
               "the payment; in Laura's plan the money waits in Treasury bills (0% in WInS)",
               "WInS price 97.152 (28 Sep) is 15.3bp from the curve: passes. Its max price is now capped at the band "
               "top (97.919; it was 97.940, above the band)",
               "the only later bond before the payment is the 5.000% 15 May 2037 (912810PU6; MSPD Table V; WInS listing "
               "UNVERIFIED). The 1 Oct rule: listed and inside its band means swap on Friday (SW37): it ends three "
               "months nearer the payment and M9 finds the same share at 2% (90.5% each, MODEL). M9's 1.2% cost gap "
               "compares a model price with a WInS price 15bp rich, so it is not a reason on its own"],
        ips=["PITCH", "HELD"],
        number=("'about ten and a half months early' (date arithmetic)", "15 Feb 2037 to 1 Jan 2038 = 320 days"),
        dont=["that the waiting money earns interest in WInS (WInS cash earns 0%)", "'about ten months' (it is 10.5)",
              "'comes out about the same' (an untraced comparison)"],
        friday=("Read the drop-down: 5.000% May 2037 listed and passing: type SW37. Listed but failing: replace 'It is "
                "the last WInS bond maturing before then' with 'The 5.000% May 2037 bond's WInS price failed our "
                "check'. Not listed: this note. Price inside the 25bp band; the last bond order. Friday fact: the WInS "
                "name string."),
        slot=SLOT_NAME,
        exemplar=("For future funding, the 4.750% Treasury bond maturing 15 Feb 2037 is for Laura's $50,000 payment on "
                  "1 Jan 2038. It is the last WInS bond maturing before then, so it ends about ten and a half months "
                  "early; what the waiting money and its coupons earn can vary."),
        nums={},
    ),
    dict(
        id="VT", ticker="VT", books={"Portfolio": 11}, use="Order 11, the session after the bonds fill (Portfolio only)",
        rung=None, job="stock fund (growth)", tn_role="supported", pick="Pick 3 (supported)",
        serves="the return-seeking portfolio: growth for Laura's 2033 facility contribution above the floor",
        facts=["Vanguard Total World Stock ETF (SEEN in WInS 29 Sep): one global index fund of about 10,000 stocks at a "
               "0.06% fee (M9)",
               "order 11, placed Mon 5 Oct ET once the five bonds show Filled, sized from the cash then left "
               "(`--cash-before-vt`). WInS Order History then shows the payments and the floor bought before any "
               "stocks, as the IPS says",
               "in Laura's plan the stock fund is all that is left after the payments and the floor (plan split "
               "ladder 66%, floor 25%, stock fund 9%, laura.plan_split_2028.strips). In WInS about 1.7% stays as cash "
               "for fees and rounding, which is why the note says 'Laura's plan'",
               "why so little stock (reflection): the ten payments use almost all of Laura's first deposit (about "
               "$292,000 of $300,000 on 1 Jan 2027, laura.ladder.cost_2027_strips)",
               "research for the reflection: WS3 compared VT with a U.S.-only fund, a two-fund split and gold or "
               "property tilts; no alternative moved her bad case by more than about $1,500 (`D_fund_choice.md`; "
               "quote only after WS1 merges numbers_ws3.yaml, request 10)",
               "Laura's tolerance: 'willing to take thoughtful risks' (Client Profile p.2); the IPS rates it above "
               "average for facility money above the floor",
               "IPS range: from the floor to the floor plus half the fund's value in 2031; the other half stays with "
               "Laura as a cushion; the 2033 contribution is capped at the announced top, so a rise after 2031 stays "
               "with her"],
        ips=["BRANCH", "DECLINE", "RANGE", "CUSHION"],
        number=("none: 'half the fund' is the IPS design, a case fact; 'about 9% of our WInS portfolio' "
                "(wins.portfolio.split_close_0928 vt 0.0868) moves to the reflection",
                "IPS snapshot 30 Sep ('the floor plus half the equity fund's value'; 'The other half remains with Laura')"),
        dont=["'only' before what a fall cuts (a fall also cuts the half she keeps)",
              "'a rise lifts the top' without 'before 2031' (after 2031 the contribution is capped)",
              "'gets what was left' about WInS (about 1.7% stays as cash; say 'Laura's plan')",
              "a return forecast (the IPS's 'should outperform' belongs in the IPS, not a note)",
              "probabilities, CAPE or valuation calls", "'Laura likes risk'", "any 2031 or 2033 dollar figure",
              "'bought last' if VT was placed before the bonds by mistake"],
        friday=("Mon 5 Oct: VT's size after `--cash-before-vt` (add `--split-from-curve` if the IBTR test failed). "
                "Friday fact: the WInS name string."),
        slot=SLOT_NAME,
        exemplar=("Growth: bought last, the Vanguard Total World Stock ETF gets what Laura's plan has left after "
                  "payments and facility floor (the least she plans to give). A fall can cut her contribution, not "
                  "below the floor; a rise before 2031 lifts the range co-sponsors hear. Half the fund stays hers."),
        nums={},
    ),
]

# Variants and conditional notes (not Friday tickets unless the named condition holds).
VARIANTS = [
    dict(
        id="IBTR_F", ticker="IBTR", use="Friday order 1, only if the refresh says the IBTR test fails",
        tn_role="tested", pick="Pick 1 (tested), if typed", serves="Laura's 5th payment (1 Jan 2037)",
        ips=["FALL", "LATEST"], slot=("inside: 'at 1 Oct yields'", 0),
        brief=("The failed-test version of IBTR: the rule decides the trade. Orders 1-10 come from the "
               "`--split-from-curve` ticket (more in the dated holdings), and VT on Monday gets the smaller share the "
               "refresh prints (friday_checklist.md). Tell Ray; WS1 records Friday's figure."),
        exemplar=("Tested before this first order: at 1 Oct yields, Laura's ten $50,000 payments cost more than her "
                  "$300,000 first deposit. This fund is future funding for the fifth. As our plan says, her 2028 "
                  "deposit tops up the earliest, so we hold less stock than planned."),
        nums={},
    ),
    dict(
        id="IBTM_R", ticker="IBTM", use="Friday order 5 (Portfolio), only if the 1 Oct vote adopts the backstop sentence",
        tn_role="refined", pick="Pick 2 (refined), if typed and no SW40, SW41 or OD_B",
        serves="Laura's 1st payment and the floor", ips=["FLOOR", "CUSHION"], slot=SLOT_NAME,
        brief=("Replaces IBTM_P. Records a real change in the policy, decided before the order: the half of the stock "
               "fund Laura keeps, not the floor, covers any shortfall from coupons or fund end values (`notes.md` s7 "
               "triage row 2; the team decides; nothing here edits the IPS). If the team does not adopt it, type "
               "IBTM_P."),
        exemplar=("Risk management: the iShares iBonds Dec 2032 Term Treasury ETF holds money for Laura's first $50,000 "
                  "payment and her facility floor (the least she plans to give). Its end value is not fixed, so our "
                  "policy now has the half of the stock fund she keeps, not the floor, cover any gap."),
        nums={},
    ),
    dict(
        id="T40s", ticker="T 4.250% 15-Nov-2040",
        use="Friday order 7, if WInS lists the 1.375% Nov-2040 but its price fails the 25bp check",
        tn_role="supported", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"],
        slot=("inside: 'its price failed our curve check today'", 0),
        brief=("Same bond as T40b. A genuinely new fact decides it: the better bond is listed but its price is stale "
               "today. If its price passes on a later check, October trigger D swaps (OD_S, OD_B)."),
        exemplar=("Future funding: the 4.250% Treasury bond maturing 15 Nov 2040 is for the ninth of Laura's ten "
                  "$50,000 payments. WInS lists a 1.375% bond of that date, which leaves less resting on reinvested "
                  "coupons, but its price failed our curve check today, so we buy this one."),
        nums={},
    ),
    dict(
        id="SW40", ticker="T 1.375% 15-Nov-2040", use="Friday --swap: the 1.375% Nov-2040 is listed and passes (1 Oct rule)",
        tn_role="refined", pick="Pick 2 (refined), if typed", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"],
        slot=("inside: 'Its WInS price passed our curve check'", 0),
        brief=("Replaces T40b on Friday. CUSIP 912810ST6. Accept a WInS clean price only between 58.474 and 62.116 "
               "(25bp band, tickets.md). 'At about the same cost' may be added only after WS1 locks the M9 figures "
               "(request 5: $23,266 against $23,146 at forward rates, MODEL)."),
        exemplar=("We chose the 1.375% Treasury bond maturing 15 Nov 2040 over the 4.250% bond of that date for Laura's "
                  "ninth $50,000 payment (future funding): more of its value is owed at maturity, so less of her "
                  "payment rests on reinvesting coupons. Its WInS price passed our curve check."),
        nums={},
    ),
    dict(
        id="SW41", ticker="T 2.000% 15-Nov-2041", use="Friday --swap: the 2.000% Nov-2041 is listed and passes (1 Oct rule)",
        tn_role="refined", pick="Pick 2 (refined), if typed and no SW40", serves="Laura's 10th payment (1 Jan 2042)",
        ips=["PITCH"], slot=("inside: 'Its price passed our curve check'", 0),
        brief=("Replaces T41 on Friday. CUSIP 912810TC2. Accept a WInS clean price only between 62.639 and 66.568 "
               "(25bp band, tickets.md)."),
        exemplar=("Role: future funding. The 2.000% Treasury bond maturing 15 Nov 2041 is for the last of Laura's ten "
                  "$50,000 payments. We chose it over the 3.125% bond of the same date: more of its value is owed at "
                  "maturity, so less rests on reinvesting coupons. Its price passed our curve check."),
        nums={},
    ),
    dict(
        id="SW37", ticker="T 5.000% 15-May-2037", use="Friday --swap: the 5.000% May-2037 is listed and passes (1 Oct rule)",
        tn_role="supported", serves="Laura's 6th payment (1 Jan 2038)", ips=["PITCH"],
        slot=("inside: 'Its WInS price passed our curve check'", 0),
        brief=("Replaces T37 on Friday. CUSIP 912810PU6. Accept a WInS clean price only between 95.905 and 99.884 (25bp "
               "band, tickets.md). The same rule as T38: the last bond before the payment."),
        exemplar=("For future funding, the 5.000% Treasury bond maturing 15 May 2037 is for Laura's $50,000 payment on "
                  "1 Jan 2038. It is the last Treasury bond maturing before then, so its money waits three months less "
                  "than with the Feb 2037 bond. Its WInS price passed our curve check."),
        nums={},
    ),
    dict(
        id="OD_S", ticker="T 4.250% 15-Nov-2040", use="October trigger D, day 1: sell (october_trade.md)",
        tn_role="refined", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"], slot=("inside: 'whose price now passes'", 0),
        brief=("Sell the whole holding (Portfolio $17,000 face; Book L $26,000). Only after a new fact: the 1.375% was "
               "listed on Friday with a stale price (T40s), or was not listed then and is now, and it passes today. "
               "Never on the day it was bought."),
        exemplar=("Role: future funding. We are selling the 4.250% Treasury bond maturing 15 Nov 2040, for Laura's "
                  "ninth payment, to buy the 1.375% bond of the same date, whose price now passes our curve check. "
                  "More of its value is owed at maturity, so less of her payment rests on reinvesting coupons."),
        nums={},
    ),
    dict(
        id="OD_B", ticker="T 1.375% 15-Nov-2040", use="October trigger D, day 2: buy (october_trade.md)",
        tn_role="refined", pick="Pick 2 (refined), if trigger D fills", serves="Laura's 9th payment (1 Jan 2041)",
        ips=["PITCH"], slot=("inside: 'now passes our curve check'", 0),
        brief=("Face value from refresh_tickets.py --swap on the day; WInS price inside the 25bp band the refresh "
               "prints (28 Sep band: 58.474 to 62.116). Pick 2 if it fills with a saved note by 20 Oct ET. 'At about "
               "the same cost' only after WS1 locks request 5. If the bond was not listed on 2 Oct, the last sentence "
               "says so instead ('It was not listed on 2 Oct and now passes our curve check')."),
        exemplar=("Future funding: we are buying the 1.375% Treasury bond maturing 15 Nov 2040 for Laura's ninth "
                  "payment, in place of the 4.250% bond we sold. More of its value comes at maturity, so less rides on "
                  "reinvested coupons. Its price was stale on 2 Oct and now passes our curve check."),
        nums={},
    ),
    dict(
        id="OB_S", ticker="VT", use="October trigger B: sell part of VT (rates-fall test)",
        tn_role="tested", pick="Pick 1 (tested), if trigger B fills", serves="the 2033 payment before growth",
        ips=["FALL"], slot=("inside: the 14 Oct result ('Yields have fallen')", 0),
        brief=("Fires only if the refresh on the 14 Oct close says the ten payments cost more than $300,000 on "
               "1 Jan 2027 (today about $292,000, laura.ladder.cost_2027_strips; zero-coupon basis unless WS1 locks a "
               "buyable one first). Size from the refresh; only if at least $2,500. In a two-week move the gap stays "
               "inside the first payment; if the refresh ever shows more, write 'the earliest payments'."),
        exemplar=("Yields have fallen, so in our model Laura's ten payments now cost more than her $300,000 first "
                  "deposit, and her 2028 deposit tops up her first payment, leaving less for the facility. As future "
                  "funding, we move part of this stock fund into the iShares iBonds Dec 2032 Term Treasury ETF."),
        nums={},
    ),
    dict(
        id="OB_B", ticker="IBTM", use="October trigger B: buy IBTM with the VT proceeds",
        tn_role="tested", serves="Laura's 1st payment and the floor", ips=["FALL", "LATEST"], slot=SLOT_NAME,
        brief="The buy leg of trigger B; OB_S is the note to feature.",
        exemplar=("Role: future funding. We are adding to the iShares iBonds Dec 2032 Term Treasury ETF with money from "
                  "the stock fund. After yields fell, Laura's 2028 deposit must complete her 2033 payment, as our plan "
                  "allows, so the payments come first. Its end value is not fixed."),
        nums={},
    ),
    dict(
        id="OC", ticker="VT", use="October trigger C: spare cash above $6,300 into VT",
        tn_role="supported", serves="growth for the facility contribution", ips=["BRANCH"], slot=SLOT_NAME,
        brief="Buy VT with everything above the $3,300 float (october_trade.md). The reason is Laura's plan, not WInS.",
        exemplar=("Role: growth. Our cash is more than fees and rounding need, so the extra goes to the Vanguard Total "
                  "World Stock ETF: in Laura's plan, money left after her payments and facility floor (the least she "
                  "plans to give) joins the stock fund held to 2033."),
        nums={},
    ),
]
# Notes that may be featured in the Trading Notes Analysis: they must also name the residency, co-sponsors or which
# of her ten payments (judge panel, 30 Sep: a year alone could fit any client). Round 2 added OB_S (it was pick 1
# under trigger B but was never checked), IBTR_F, IBTM_R and SW41.
PICK_IDS = {"IBTR", "IBTR_F", "OB_S", "SW40", "SW41", "OD_B", "IBTM_R", "IBTM_P", "VT", "T39", "T38"}
# The notes that can sit side by side as the three picks (s6). No two may open with the same two words in any
# combination (judge panel round 2: picks 1 and 2 both opened 'Future funding: the').
PICK_SLOTS = [["IBTR", "IBTR_F", "OB_S"], ["SW40", "SW41", "OD_B", "IBTM_R", "IBTM_P"], ["VT"]]

# ----------------------------------------------------------------------------------------------- reflection outlines
# Bullets for the Trading Notes Analysis reflections (TN guide: why / how it aligned / how it served the client).
# Round 2 (judge panel): outlines are 60 words or fewer; the scale sentence goes in pick 1 only and the certainty phrase
# in pick 2 only, so no reflection is pushed past about 90 words before the students' own linking words. Each
# outline + its extra sentence is checked against EXTRA_CAP. Students write the prose; these are prompts.
SCALE = "Our WInS portfolio is Laura's plan after both deposits, scaled down to $300,000."
SCALE_L = "Our WInS portfolio is Laura's 2027 deposit; the floor and stock fund come in 2028."
CERTAINTY = ("a high degree of certainty: Treasuries maturing before each payment, held to maturity; the U.S. "
             "government owes most of each payment, and the rest depends on reinvesting coupons")
MAX_OUTLINE_WORDS, EXTRA_CAP = 60, 90
OUTLINES = [
    ("Pick 1, IBTR (tested; IBTR_F if the test failed; OB_S if trigger B fills)", [
        "Why: a rule set in advance: before the first order we re-priced the ten payments (1 Oct yields; "
        "zero-coupon basis; coupons: pick 2).",
        "Tested: Friday's result, the 14 Oct re-check; since 2000, only 2020-21 yields would have left part of one "
        "payment unfunded.",
        "If it fails: the 2028 deposit tops up the earliest before any stocks; no payment is missed.",
    ], "the scale sentence",
        "Numbers: history.unfunded_days quote_as (the one number). The odds ('about 1 in 3', ws4.gap_odds_2027) and "
        "'typically about $10,000' (ws4.gap_if_any_typical) only after WS1 merges them (request 10), and only with their "
        "basis: both are zero-coupon figures; on the buyable ladder the odds are not computed and likely higher "
        "(ws4.gap_odds_2027_bookL). Name the basis in one clause; if WS1 locks the buyable basis first (request 9), use "
        "it here, in the note and in the IPS alike."),
    ("Pick 2, refined: SW40, SW41 or OD_B (a bond changed), or IBTM_R (the policy changed)", [
        "Why: pricing each rung showed most of each payment is owed as set coupons and principal; the rest depends on "
        "reinvesting coupons.",
        "Refined: a low-coupon bond of the same date (SW40, SW41, OD_B), or the stock-fund half Laura keeps now "
        "covers any shortfall (IBTM_R).",
        "Curve check, once: yield within a quarter of a percentage point of the official curve.",
    ], "the certainty phrase",
        "Numbers: none needed. 'Most of each payment' is reinvest.rung.*.at_0pct (84-95% of the $50,000, MODEL); a "
        "percentage needs WS1 request 11. If no refined note exists, do not force one: feature IBTM_P as supported."),
    ("Pick 3, VT (supported)", [
        "Why: her payments take almost all her first deposit; stocks get what is left after them and the floor, the "
        "least she can name to co-sponsors in 2031.",
        "Research: VT against a U.S.-only fund, a two-fund split and gold or property tilts; none moved her bad case "
        "much.",
        "Served Laura: \"willing to take thoughtful risks\"; half the fund stays hers.",
    ], None,
        "Numbers: 'almost all' is laura.ladder.cost_2027_strips; 'about 9% of our WInS portfolio' is "
        "wins.portfolio.split_close_0928. WS3's 'no more than about $1,500' (D_fund_choice.md) only after WS1 merges "
        "numbers_ws3.yaml (request 10). No 2031 dollar figure."),
]
ALT_OUTLINES = [
    ("Alternate A, IBTM (supported; pick 2 if no refined note exists)", [
        "Why: one fund holds money for her first payment and the floor, the least she can name to co-sponsors in "
        "2031; WInS lists no late-2032 Treasury.",
        "Limit: iShares says its iBonds funds \"do not seek to return any predetermined amount\"; its end value is not "
        "fixed.",
    ], None, "Numbers: none."),
    ("Alternate B, 4.375% Nov 2039 bond (supported: certainty)", [
        "Why: its price moves, but held to maturity its set coupons and principal cover most of her 2040 payment; "
        "reinvesting coupons covers the rest.",
        "Served Laura: the plainest case of the certainty phrase.",
    ], "the certainty phrase", "Numbers: 'most of' is reinvest.rung.T_4.375%_15-Nov-2039 at_0pct (about 86%)."),
    ("Alternate C, 4.500% May 2038 bond (supported, with a price check)", [
        "Why: every WInS bond price was checked against the latest official curve; a yield more than a quarter of a "
        "percentage point off meant stale, and two stale prices failed.",
        "Aligned: the check tests the IPS cost claim at the prices actually paid.",
    ], None, "Numbers: the 25bp band (wins.bond_check.*); 'two stale prices' = the Feb 2036 and Feb 2038 bonds."),
]
EXTRA_WORDS = {"the scale sentence": len(SCALE.split()), "the certainty phrase": len(CERTAINTY.split())}


def outline_words(bullets):
    return len(" ".join(bullets).split())


def check_note(n):
    """Every check in note_rules.check_text must pass for an exemplar (FAIL and WARN alike); a note that may be
    featured must also pass the pick anchor (residency, co-sponsors or which of her ten payments); and the exemplar
    plus its Friday-fact slot must fit the kit limit (judge panel round 2: 283-285-character exemplars left no room)."""
    out = [(name, ok, detail) for name, ok, detail, _sev in check_text(n["exemplar"], list(n.get("nums", {})))]
    if n["id"] in PICK_IDS:
        ok, detail = pick_anchor(n["exemplar"])
        out.append(("pick anchor", ok, detail))
    else:
        out.append(("pick anchor", True, "n/a"))
    slot, extra = n["slot"]
    fits = len(n["exemplar"]) + extra <= MAX_NOTE
    out.append(("Friday fact", fits, f"{slot}: {len(n['exemplar'])} + {extra} characters (kit limit {MAX_NOTE})"))
    return out


def first_words(t, k=2):
    return " ".join(re.sub(r"[^a-z ]", "", t.lower()).split()[:k])


def pick_variety():
    """Across every set of three notes that can be featured together (PICK_SLOTS), how many pairs open with the same
    two words. Judge panel round 2 asked for at most one shared opening; the kit aims for none."""
    by_id = {x["id"]: x["exemplar"] for x in NOTES + VARIANTS}
    worst, where = 0, ""
    for a in PICK_SLOTS[0]:
        for b in PICK_SLOTS[1]:
            for c in PICK_SLOTS[2]:
                ops = [first_words(by_id[i]) for i in (a, b, c)]
                shared = sum(1 for i in range(3) for j in range(i + 1, 3) if ops[i] == ops[j])
                if shared > worst:
                    worst, where = shared, f"{a}/{b}/{c}"
    return worst, where


# ----------------------------------------------------------------------------------------------- inputs
def load_inputs():
    lock = open(os.path.join(ROOT, "rab/numbers.lock")).read().split()[0]
    raw = open(os.path.join(ROOT, "rab/numbers.yaml"), "rb").read()
    h = hashlib.sha256(raw).hexdigest()
    if h != lock:
        sys.exit(f"numbers.yaml hash {h[:12]} does not match rab/numbers.lock {lock[:12]}: stop (PM-35)")
    Y = yaml.safe_load(raw)["numbers"]
    T = list(csv.DictReader(open(os.path.join(HERE, "tickets.csv"))))
    return Y, T, h


def money(x):
    return f"${x:,.0f}"


def round_k(x):
    return f"about ${round(x / 1000):,.0f},000"


def book_facts(n, T, Y):
    """Per-book size lines for a note: WInS quantity, Preview total, share of $300,000; Laura-plan rung cost."""
    lines = []
    weights = {r["holding"]: r["weight"] for r in Y["wins.portfolio.holdings_close_0928"]["value"]}
    for book, seq in n["books"].items():
        row = next(r for r in T if r["book"] == book and int(r["seq"]) == seq)
        qty = int(float(row["qty"]))
        unit = "shares" if row["type"] == "ETF" else "face"
        qty_s = f"{qty:,} {unit}" if unit == "shares" else f"${qty:,} face"
        cost = float(row["cost_locked"])
        if book == "Portfolio":
            key = row["id"].split(" (")[0]
            w = weights.get(key)
            share = f"{w * 100:.1f}% of the book (numbers.yaml)" if w is not None else ""
        else:
            share = f"{cost / 300000 * 100:.1f}% of the book (ticket cost / $300,000)"
        lines.append(f"{'Book L' if book == 'BookL' else 'Portfolio'} #{seq}: {qty_s}, expected Preview total "
                     f"${float(row['preview_expected']):,.2f} (ticket), {share}")
    if n.get("rung"):
        r = Y[f"reinvest.rung.{n['rung']}"]["value"]
        what = "the 2033 payment rung" if n["rung"] == "IBTM" else "this rung"
        lines.append(f"Laura's plan: {round_k(r['cost'])} of her 2027 deposit buys {what}; if its income is "
                     f"reinvested at only 2%, it delivers {round_k(r['at_2pct'])} of the $50,000 (reinvest.rung.{n['rung']}, "
                     f"MODEL; appendix only, never in a note)")
    return lines


# ----------------------------------------------------------------------------------------------- outputs
def brief_cell(n, T, Y, book):
    parts = [f"Serves: {n['serves']}.", "Facts: " + "; ".join(n["facts"]) + "."]
    tag = "Book L" if book == "BookL" else "Portfolio"
    parts.append("Sizes: " + "; ".join(l for l in book_facts(n, T, Y) if not l.startswith(("Portfolio", "Book L"))
                                      or l.startswith(tag)) + ".")
    parts.append("IPS: " + " / ".join(f"\"{IPS[k]}\"" for k in n["ips"]))
    parts.append(f"One number: {n['number'][0]} [{n['number'][1]}].")
    parts.append("Do not say: " + "; ".join(n["dont"]) + "; nor any word in notes.md s2.")
    parts.append(f"Friday: {n['friday']}")
    return " ".join(parts)


def role_of(text):
    """The official role word(s) the exemplar names, wherever they appear (openings vary on purpose)."""
    return " and ".join(w for w in ROLE_WORDS if w in text.lower())


def check_ips_quotes():
    """Every IPS sentence quoted in the kit must appear verbatim in the 30 Sep snapshot of the IPS doc."""
    doc = open(IPS_SNAPSHOT).read()
    not_ips = {"about a third of our WInS portfolio", "about a quarter of a percentage point",
               "do not seek to return any predetermined amount",   # numbers.yaml quote_as strings; iShares text
               "willing to take thoughtful risks"}                  # Client Profile p.2
    quoted = list(IPS.values())
    for _, bullets, _x, _n in OUTLINES + ALT_OUTLINES:
        for b in bullets:   # quotes are checked bullet by bullet, never across bullets
            quoted += [q for q in re.findall(r'"([^"]+)"', b) if q not in not_ips]
    return [q for q in quoted if q.rstrip(".") not in doc]


def write_csv(path, T, Y):
    rows = []
    for n in NOTES:
        for book, seq in sorted(n["books"].items(), key=lambda kv: (kv[0] != "Portfolio", kv[1])):
            brief = brief_cell(n, T, Y, book)
            if book == "BookL" and "Portfolio" in n["books"]:
                brief = (f"Book L: same security, brief and exemplar as Portfolio #{n['books']['Portfolio']}; only the "
                         f"size differs. " + "; ".join(l for l in book_facts(n, T, Y) if l.startswith("Book L")) + ".")
            rows.append(dict(ticker=n["ticker"], brief=brief, exemplar=n["exemplar"], char_count=len(n["exemplar"]),
                             book=book, seq=seq, note_id=n["id"], use=n["use"], label=LABEL,
                             numbers="; ".join(f"{k} = {v}" for k, v in n.get("nums", {}).items()),
                             role=role_of(n["exemplar"]), tn_role=n["tn_role"], pick=n.get("pick", ""),
                             ips_quote=" / ".join(IPS[k] for k in n["ips"]), friday_slot=n["slot"][0]))
    for v in VARIANTS:
        brief = (f"Serves: {v['serves']}. {v['brief']} IPS: " +
                 " / ".join(f"\"{IPS[k]}\"" for k in v["ips"]))
        rows.append(dict(ticker=v["ticker"], brief=brief, exemplar=v["exemplar"], char_count=len(v["exemplar"]),
                         book="conditional", seq="", note_id=v["id"], use=v["use"], label=LABEL,
                         numbers="; ".join(f"{k} = {x}" for k, x in v.get("nums", {}).items()),
                         role=role_of(v["exemplar"]), tn_role=v["tn_role"], pick=v.get("pick", ""),
                         ips_quote=" / ".join(IPS[k] for k in v["ips"]), friday_slot=v["slot"][0]))
    order = {"Portfolio": 0, "BookL": 1, "conditional": 2}
    rows.sort(key=lambda r: (order[r["book"]], int(r["seq"]) if r["seq"] != "" else 99))
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ticker", "brief", "exemplar", "char_count", "book", "seq", "note_id",
                                          "use", "label", "numbers", "role", "tn_role", "pick", "ips_quote",
                                          "friday_slot"])
        w.writeheader()
        w.writerows(rows)
    return rows


def t2(y, mo, d, h, mi):
    e, s = both(datetime(y, mo, d, h, mi, tzinfo=ET))
    return f"{e} = {s}"


def md_note(n, T, Y, checks):
    where = ", ".join(f"{'Book L' if b == 'BookL' else 'Portfolio'} #{s}" for b, s in n["books"].items())
    tag = "" if n["id"] == n["ticker"] else f" ({n['id']})"
    L = [f"### {n['ticker']}{tag}: {where}", ""]
    pick = f" **Trading Notes Analysis:** {n['pick']}." if n.get("pick") else ""
    L.append(f"- **Serves:** {n['serves']}. **Job:** {n['job']}. **Likely TN role:** {n['tn_role']}.{pick}")
    for f_ in n["facts"]:
        L.append(f"- {f_}")
    for l in book_facts(n, T, Y):
        L.append(f"- {l}")
    for k in n["ips"]:
        L.append(f"- **IPS:** \"{IPS[k]}\"")
    L.append(f"- **One number:** {n['number'][0]}. Source: {n['number'][1]}.")
    L.append(f"- **Do not say:** {'; '.join(n['dont'])}.")
    L.append(f"- **Re-check Friday:** {n['friday']}")
    L.append(f"- **Friday-fact slot:** {n['slot'][0]} (adds {n['slot'][1]} characters; exemplar + slot "
             f"{len(n['exemplar']) + n['slot'][1]} of {MAX_NOTE}).")
    ok = all(c[1] for c in checks)
    L += ["", f"> **{LABEL}** ({len(n['exemplar'])} characters; checks {'pass' if ok else 'FAIL'})", ">",
          f"> {n['exemplar']}", ""]
    return L




def write_md(path, T, Y, h, results, boiler, pv):
    tn_due = t2(2026, 10, 23, 17, 0)
    submit = t2(2026, 10, 22, 2, 0)
    oct_close = t2(2026, 10, 20, 15, 30)
    vt_time = t2(2026, 10, 5, 10, 30)
    L = []
    A = L.append
    A("# WInS note briefs, EXAMPLE notes and the three Trading Notes Analysis picks")
    A("")
    A("WS6-notes, RAB Kit, 30 Sep 2026 (Sydney). AI-generated research (Claude Code, Claude Opus 5.5) for Team "
      "Caplet. **Every exemplar is labelled `EXAMPLE - team rewrites`.** Students write the notes typed into WInS "
      "and every reflection; this file supports them and is logged in `docs/AI_USE.md`. If any exemplar wording is "
      "used, the Final Report's Works Cited discloses it. Generated by `rab/trades/build_notes.py` from "
      f"`tickets.csv` and the locked `rab/numbers.yaml` (sha256 {h[:12]}...); do not edit by hand. Basis: 28 Sep "
      "2026 curve and closes, WInS prices seen 29 Sep. Revised twice after the judge panels of 30 Sep (round 1 at "
      "c11b02f, round 2 at 104476c); every point and the answer to it is in `judge_response.md`. Nothing here changes "
      "the strategy.")
    A("")
    A("**Bottom line.**")
    A("")
    longest = max(len(x["exemplar"]) for x in NOTES + VARIANTS)
    A("- Every Friday ticket (both books) has a brief and an exemplar; so do the Friday swap variants, the failed-test "
      f"version of IBTR and each October trigger. All exemplars are {longest} characters or fewer, plain ASCII, one "
      "paragraph, leave room for their Friday fact, and pass the banned-word, number (digits and words), Laura, "
      "variety and pick-opening checks (s8).")
    A("- **Feature these three** (Portfolio book): **IBTR** (tested: before the first order the team re-prices what "
      "the ten payments cost against Laura's $300,000 first deposit; if yields fall more than about a quarter of a "
      "percentage point, her 2028 deposit tops up the earliest and the stock fund gets less; the 14 Oct check runs it "
      "again), **a refined note** (the first that exists: SW40 or SW41, a low-coupon bond swapped in on Friday; OD_B, "
      "the October swap; IBTM_R, a policy sentence the team adopts at the 1 Oct vote), and **VT** (supported: bought "
      "last, with what Laura's plan has left after the payments and the floor). If no refined note exists, feature "
      "IBTM_P as supported: three honest labels beat a hollow 'refined'.")
    A("- **The 1 Oct vote settles three things before Friday:** one rule for every same-slot alternate (listed and "
      "inside its 25bp band means swap on Friday: 1.375% Nov 2040, 2.000% Nov 2041, 5.000% May 2037); whether the "
      "policy names the half of the stock fund Laura keeps, not the floor, as the cover for a shortfall (IBTM_R); and "
      "the book. T40c (a better bond kept for October) is retired: it would look like a staged trade.")
    A(f"- **VT is order 11**, placed in the session after the bonds fill ({vt_time}), so WInS Order History shows "
      "the payments and the floor bought before any stocks, as the IPS says (`tickets.md`, `friday_checklist.md`).")
    A("- **No 'set amount' alone.** In Laura's plan a bond rung's set coupons and principal cover most of its $50,000 "
      "payment (84-90% for the five bonds, `reinvest.rung.*` at_0pct); reinvesting coupons covers the rest. Notes say "
      "so in words, never as a fixed payment.")
    A("")
    A("## 1. What a note must do")
    A("")
    A("- **Official test** (Competition Guide p.3): a note captures \"the reasoning behind the decision, including its "
      "alignment with your strategy, the supporting research or analysis, and its expected role in growth, "
      "liquidity, risk management, or future funding.\" The TN Analysis later quotes three notes \"exactly as it "
      "appears in WInS\" and asks how each decision \"aligned with, tested, or refined\" the strategy (Trading Note "
      "Instruction).")
    A("- **Content, in the writer's own order:** the role word (growth, liquidity, risk management or future "
      "funding) + what is bought and which of Laura's needs it serves + the research or check behind it + the honest "
      "limit. About 45 words. The exemplars open in several ways on purpose: vary yours too (s8 checks it).")
    A("- **The box:** 300 characters maximum (maxlength, SEEN 29 Sep). The kit limit is **285**, plain ASCII (straight "
      "quotes; no dashes, `~` or `<=`), one paragraph. Whether a saved note can be edited is UNVERIFIED: treat the first "
      "save as final.")
    A(f"- **The Guide's own example note** (Trading Note Instruction p.2) is {len(WHARTON_EXAMPLE)} characters, so it "
      "would not fit the WInS box, and it would be true of any client. Use it for tone only; `note_check.py` warns if a "
      "draft echoes it.")
    A("- **Laura-specific:** name which of her ten payments, the floor, the residency or co-sponsors. A date alone "
      "could fit any client, so the checker no longer accepts a year as the Laura anchor. A note that may be "
      "featured must also name the residency, co-sponsors or which of her ten payments (`note_check.py --pick`).")
    A("- **One Friday fact, with room for it:** each note carries one thing only WInS showed that day: the exact WInS "
      "name string, that its price passed the check, the curve or price-check date, or the Preview price as the "
      "note's one number (dated). Each brief names its slot. Most exemplars already hold it; for the rest the exact "
      "WInS name string replaces ours at no cost, and IBTM_P leaves about 30 characters for a dated price. The "
      "285 limit keeps 15 characters spare for a WInS string longer than ours.")
    A("- **Numbers:** at most one analytic number, from `numbers.yaml` or a named, dated source. **A number written in "
      "words counts too**, and the checker now catches it: a quarter, fifth or third of, half of, percentage point, "
      "about the same, almost exactly, most of, twice. Dollar figures only as Laura's case facts ($50,000 payments, "
      "$300,000 first deposit) or \"in Laura's plan\"; WInS amounts as percentages. Never a WInS gain, loss or "
      "ranking.")
    A("- **Coupons, in words that do not reassure falsely:** for an iBonds fund, \"its end value is not fixed\" or "
      "\"what its income earns can vary\"; for a bond, \"part of each payment comes from reinvested coupons\" or \"its "
      "set coupons and principal cover most of that payment\". Never \"a set amount\" alone: next to \"Laura's $50,000 "
      "payment\" it reads as the whole $50,000. Vary the tail (premortem PM-23). Say what a low coupon does for her: "
      "less of her payment rests on reinvested coupons, not \"less income\".")
    A("- **\"Facility floor\" is glossed** the first time it appears in a note or reflection: \"the least she plans to "
      "give the facility\". The TN Analysis reaches judges before the IPS. Never a dollar figure next to it.")
    A("- **No strategy name** in WInS notes. Reflections may use it once if Ray confirms it by 22 Oct (the 30 Sep IPS "
      "draft uses it in its pitch), which links the TN Analysis to the IPS.")
    A("")
    A("## 2. Words never used in a note")
    A("")
    A("This list quotes the banned words on purpose; `build_notes.py` checks the exemplars, not this section.")
    A("")
    A("- guaranteed, risk-free, no risk, locked, lock in, safe, stable, \"reduce volatility\", certain, certainty, "
      "100%, promised, pledged (overclaims; say \"backed by the U.S. government\" or \"the U.S. government owes\"). "
      "A reflection may use the case phrase \"high degree of certainty\" once, with its condition (s6).")
    A("- match / matched (false for funds and coupon bonds), \"cash-flow matched\", \"needs no rebalancing\".")
    A("- \"a set amount\" on its own, \"covers her payment\" for a fund (its end value is not fixed), \"less income to "
      "reinvest\" as the benefit of a low coupon.")
    A("- \"I bond\" (a U.S. savings bond); write \"iBonds\" or the fund's full name. Never \"repays $X\" for an iBonds fund.")
    A("- Forecasts and results: will grow / will outperform, CAPE, overvalued, profit, gain, rank.")
    A("- \"Laura's portfolio\" or \"her money\" for the WInS book; the operating reserve's size; **any 2031 dollar "
      "figure** (the range, its top or a co-sponsor amount; the TN guide says these are not expected yet); Laura "
      "quotes; her degree, heritage or Taiwan as a reason. **The ideas are encouraged:** the floor, co-sponsors, the "
      "2031 range, the half of the fund she keeps, the residency, her operating payments.")
    A("- Jargon without a gloss: bp, basis points, duration, immunization. Say \"percentage point of yield\", not "
      "\"point of yield\" (bond prices are quoted in points).")
    A("")
    A("## 3. How the team uses this (Thu 1 Oct to Mon 5 Oct)")
    A("")
    A("1. Each note has a named student writer (Friday runbook roles). The writer drafts **from the brief, with the "
      "exemplar closed**, then compares, and adds the Friday fact in its slot.")
    A("2. Run the checker on the draft: `/Users/ray/Research/rab-ws/.venv/bin/python rab/trades/note_check.py --ticker "
      "IBTM --text \"...\"` (add `--pick` for a note that may be featured). It counts characters, checks ASCII, banned "
      "words, numbers in digits and in words and the Laura anchor, and measures **phrase overlap with the exemplar** "
      "(share of the draft's three-word phrases found in it). 50% or more: rewrite (FAIL). 25-49%: not a pass; "
      "rewrite, or disclose the exemplar in Works Cited (PM-13).")
    A("3. Note keeper holds the final texts, pastes each at Preview, reads it aloud once.")
    A("4. After saving: Order History > Add/View Notes, copy the note back into the Trade Log and compare it with the "
      "plan character for character (the box cuts silently at 300).")
    A("5. Log in `docs/AI_USE.md` which exemplars were read and whether any wording was kept.")
    A("")
    A("## 4. Friday notes, Portfolio book (Book L differences inline)")
    A("")
    A("Order: iBonds funds (1-5), then the bonds (6-10), both on Friday; **VT (11) in the next session**, once the "
      "bonds show Filled (`tickets.md`). Book L is orders 1-10; only IBTM's note differs. **The Friday drop-down read "
      "decides three notes** under the one 1 Oct rule (listed and inside its 25bp band means swap): order 7 is **T40b** "
      "if WInS does not list the 1.375% Nov 2040, **SW40** if it is listed and passes, **T40s** if it is listed but "
      "its price fails; order 6 is T41 or **SW41**; order 10 is T37 or **SW37**. Order 5 is IBTM_P, or **IBTM_R** if the "
      "1 Oct vote adopted the backstop sentence. Order 1 is IBTR, or **IBTR_F** if the refresh says the payments cost "
      "more than $300,000. Sizes are the Gate A tickets; Friday's refresh re-sizes them. WInS names of IBTO-IBTR and "
      "every bond string are UNVERIFIED until read on Friday.")
    A("")
    for n in NOTES:
        L.extend(md_note(n, T, Y, results[n["id"]]))
    A("## 5. Variants and October notes (conditional)")
    A("")
    A("Use only when the named condition holds. October trades follow `october_trade.md`; if trigger A (repair) fires, "
      "reuse that ticket's Friday note and, if it fits, add \"Friday's order did not fill.\" T40c is retired (round 2): "
      "keeping a listed, passing better bond for October would look like a trade made to create a pick.")
    A("")
    A("| Id | Holding | Use when | Serves | Brief | EXAMPLE - team rewrites | Chars |")
    A("|---|---|---|---|---|---|---|")
    for v in VARIANTS:
        A(f"| {v['id']} | {v['ticker']} | {v['use']} | {v['serves']} | {v['brief']} Fact from the day: {v['slot'][0]}. "
          f"IPS: \"{IPS[v['ips'][0]]}\" | {v['exemplar']} | {len(v['exemplar'])} |")
    A("")
    A("## 6. Trading Notes Analysis: the three notes to feature")
    A("")
    A(f"Due {tn_due}. Target: submit {submit}, about a day and a half early. **Official** (Trading Notes Analysis "
      "instructions): only executed trades with a saved note; each note quoted exactly as WInS shows it; the three "
      "decisions together show a cohesive strategy; reflections of 100 words or fewer on the three questions. **Kit "
      "rules** (premortem PM-19, not official): three different jobs; reflections written by students without AI "
      "(plan 90 by two counters).")
    A("")
    A("| Pick | Note | Role | Job | Why this one |")
    A("|---|---|---|---|---|")
    A("| 1 | IBTR, Friday #1 (IBTR_F if the test fails; OB_S if trigger B fills) | **tested** | payments (certainty) | "
      "A rule set before anyone knew the answer, run before the first order: do the ten payments cost less than "
      "Laura's $300,000 first deposit at the latest yields? If yields fall more than about a quarter of a percentage "
      "point, the 2028 deposit tops up the earliest payments before any stocks: no payment is missed and the stock "
      "fund gets less. On Friday the test decides the ticket (`--split-from-curve` if it fails); the 14 Oct check "
      "runs it again, so the reflection reports two results. |")
    A("| 2 | The first that exists: **SW40** (1.375% Nov 2040 swapped in on Friday), **SW41** (2.000% Nov 2041), "
      "**OD_B** (October trigger D), **IBTM_R** (backstop sentence adopted at the 1 Oct vote) | **refined** | payments "
      "(reinvestment) or the floor | A discovery with its reason: pricing each rung showed that most of each payment "
      "is owed as set coupons and principal and the rest rests on reinvesting coupons. The change is either the bond "
      "(less rests on coupons) or the policy (the half of the stock fund Laura keeps, not the floor, covers a "
      "shortfall). **If none exists, do not force 'refined'**: feature IBTM_P as supported (the floor and "
      "co-sponsors). T40b records a constraint, not a change. |")
    A("| 3 | VT, order 11 (VT) | **supported** | growth | Bought last, with what Laura's plan has left after the "
      "payments and the floor, so Order History matches the note and the IPS. A fall cannot take her contribution "
      "below the floor; a rise before 2031 lifts the range co-sponsors hear; half the fund stays hers (flexibility). "
      "The reflection adds the research (WS3's fund comparison) and her tolerance. |")
    A("")
    A("**Alternates (keep all three ready):** (A) **IBTM_P, Friday #5** (supported: the floor and co-sponsors; also "
      "the pick-2 fallback); (B) **the 4.375% Nov 2039 bond, Friday #8** (supported: what Laura is owed and what rests "
      "on coupons); (C) **the 4.500% May 2038 bond, Friday #9** (supported, with the price check; it tested WInS data, "
      "not the strategy).")
    A("")
    A(f"**If an October trade fills with a saved note by {oct_close}:**")
    A("")
    A("- **Trigger D (coupon swap after a stale Friday price):** feature the **buy leg (OD_B)** as pick 2 (refined), "
      "unless SW40 or SW41 was typed on Friday.")
    A("- **Trigger B (rates fall):** feature **OB_S** (the VT sale) as pick 1 (tested) in place of IBTR; IBTR becomes "
      "an alternate.")
    A("- **Trigger C or none:** keep the three above; the IBTR reflection says what the 14 Oct check showed. Never add "
      "a trade to create a pick.")
    A("")
    A(f"**If the 1 Oct vote picks Book L:** feature IBTR (tested), a refined note if one exists (SW40, SW41 or OD_B) "
      f"and the Nov 2039 bond (supported: certainty); if no refined note exists, the May 2038 bond is the third, and "
      f"all three are honestly labelled. Alternates IBTM_L and the Nov 2041 bond. Pick 1's reflection uses "
      f"\"{SCALE_L}\" in place of the scale sentence.")
    A("")
    A(f"### Reflection outlines (bullets only; each {MAX_OUTLINE_WORDS} words or fewer; students write the prose)")
    A("")
    A("Each follows the TN guide's three questions: why the team made the decision, how it aligned with the strategy, "
      "and how it served Laura's goals, funding needs or risks. Paraphrase the IPS rather than quoting it. Two "
      "sentences are shared out so no reflection is overloaded (judge panel round 2):")
    A("")
    A(f"- **the scale sentence** ({len(SCALE.split())} words), **in pick 1 only**, the one reflection with Laura's "
      f"dollar figures next to a WInS holding: \"{SCALE}\" (Book L: \"{SCALE_L}\")")
    A(f"- **the certainty phrase** ({len(CERTAINTY.split())} words), **once across the set, in pick 2**: {CERTAINTY}. "
      "Once the team decides who covers a shortfall, the same reflection names that money.")
    A("- **what happened after Friday** only where something did: pick 1 (the 14 Oct check) and any October trade.")
    A("- the strategy name once, if Ray confirms it by 22 Oct.")
    A("")
    for title, bullets, extra, numnote in OUTLINES + ALT_OUTLINES:
        tail = (f"; + {extra} = {outline_words(bullets) + EXTRA_WORDS[extra]} words" if extra else "")
        A(f"**{title}** ({outline_words(bullets)} words{tail})")
        A("")
        for b in bullets:
            A(f"- {b}")
        A("")
        A(numnote)
        A("")
    A("**Keep out of all reflections:** any 2031 dollar figure (range, top, co-sponsor amount) and the operating "
      "reserve size (TN guide: Final Report material); WInS gains, losses or rank; a return forecast. The ideas "
      "(floor, co-sponsors, the 2031 range, the half Laura keeps as a cushion) are welcome.")
    A("")
    A("## 7. Triage (the strategy is unchanged; nothing here is applied to the IPS, the Sheet or numbers.yaml)")
    A("")
    A("| Finding | Class | Evidence |")
    A("|---|---|---|")
    A("| The IPS defines high certainty as each payment being \"matched by a dated Treasury ETF or bond maturing just "
      "before it\" and says the ladder \"needs no rebalancing\". Funds and coupon bonds are not matched (coupons must "
      "be reinvested), and the Feb 2037 and May 2038 bonds end 10.5 and 7.6 months early, not \"just before\". "
      "Wording only: e.g. \"Treasuries maturing before each payment, held to maturity, with coupons reinvested in "
      "Treasury bills\". Whichever reflection says \"high degree of certainty\" must also say, in words, that most of "
      "each payment is owed by the U.S. government and the rest depends on reinvesting coupons. | fix-before-6-Nov "
      "(the team decides) | IPS snapshot 30 Sep; premortem PM-14, PM-23; `reinvest.rung.*` at_0pct (84-95%) |")
    A("| No sentence says which money covers a coupon or fund-value shortfall. If coupons earn only 2%, keeping every "
      "payment whole costs about $20,000 more today (`reinvest.bookL_buffer_cost`), more than the about $7,600 of "
      "room under $300,000 (`laura.ladder.headroom_2027_strips`). If the floor were tapped, the bottom of the "
      "co-sponsor range would break. One sentence naming the order (e.g. the half of the stock fund Laura keeps, "
      "before the floor) closes it. WS7 challenges whether keeping half still holds once that half is the backstop "
      "(D6, `rab/redteam/`). | decide at the 1 Oct vote if IBTM_R is to be typed; otherwise fix-before-6-Nov "
      "(wording only; the team chooses) | `reinvest.*`; IPS \"The other half remains with Laura as a cushion\" |")
    A("| The IBTR test and every \"cost under $300,000\" figure are on the zero-coupon (STRIPS) basis of "
      "`numbers.yaml`. Under the adopted rule reading R1(a) the ladder Laura can buy is the WInS-listed one, which "
      "costs more and leaves less room: WS4 gets 22.8bp with yields unchanged; WS7's uncommitted check gets about "
      "$295,100 on 1 Jan 2027, about $4,900 of room and about 22bp (both UNVERIFIED for quoting). The claim still "
      "holds on both bases today, with less room. | note-in-Final-Report (state both bases in one sentence); use one "
      "basis in the note, the reflection and the IPS (WS1 request 9) | `assumptions.md` R1; `numbers_ws4.yaml`; WS7 "
      "`tickets.md` (working tree) |")
    A("| If the 1 Oct vote picks Book L, the IPS sentence \"Our WInS portfolio shows the allocation after both "
      "deposits, scaled down\" becomes false, and the TN Analysis cannot show the floor or the stock fund. | decide at "
      "the 1 Oct vote; fix-before-6-Nov if Book L | Sheet tab Book L header; s6 |")
    A("| Under reading R1(a) Laura's real plan is limited to WInS-listed securities, and WInS lists no Treasury "
      "maturing in late 2032, so IBTM (a fund of late-2032 Treasuries) is her floor holding too, not only WInS's "
      "stand-in. Late-2032 notes (4.125% 15 Nov 2032, 91282CFV8; 3.75% 30 Nov 2032, 91282CPM7) fit the IPS wording only "
      "under reading (b). Either way the floor's end value is not fixed. | note-in-Final-Report | `assumptions.md` "
      "R1; MSPD Table V, 31 Aug 2026 (`data/mspd_table5_2026-08-31.json`) |")
    A("| No iBonds Treasury fund ends Dec 2037 to Dec 2043, so the 2038-2042 payments use coupon bonds (the larger "
      "reinvestment exposure). The last two dated funds launched in March (IBTQ 25 Mar 2025, IBTR 25 Mar 2026), so a "
      "Dec 2037 fund could appear after Laura's January 2027 purchase (UNVERIFIED). | note-in-Final-Report | "
      "iShares product list, fetched 30 Sep (`data/ishares_ibonds_treasury_list_2026-09-30.csv`) |")
    A("| The Sheet's accrued interest for the 4.500% May 2038 bond is 0.530; 1.66 is right on 28 Sep (1.71 on 2 Oct). "
      "| fix-before-6-Nov (Sheet input); keep it out of notes | `wins.bond_accrued_mismatch`; tickets row 9 |")
    A("| Strategy name: kept out of WInS notes; the reflections lose their easiest link to the IPS without it. | "
      "decide by 22 Oct (Ray confirms the name) | IPS snapshot pitch paragraph |")
    A("| WS7's working tree holds uncommitted ticket edits (IBTM split into two orders, VT as order 12, a buyable-basis "
      "test). If they are merged, this file's order numbers go stale. | WS0 decides which tickets are final before "
      "Friday; then re-run `build_notes.py` (it checks note order against `tickets.csv`) | `git status` in ws7, 30 Sep |")
    A("")
    A("**Requests to WS1 for the Friday re-lock** (WS6 does not write `numbers.yaml`, PM-35; until they land, no note "
      "or reflection quotes these figures):")
    A("")
    A("1. Re-lock `laura.ladder.cost_2027_strips` and `breakeven_fall_bp_strips` on Friday's curve (the IBTR note and "
      "pick 1).")
    A("2. A `quote_as` for `wins.ibond_checks.*.premium_to_nav_pct` (e.g. \"its price was within 0.1% of the value of "
      "its Treasuries\"), for IBTP.")
    A("3. `wins.bond_check.T_4.375%_15-Feb-2038`: `quote_as` \"almost a full percentage point of yield off the curve\" "
      "in place of \"about 1 point\" (a price point to a bond reader). Optional now: the T38 exemplar no longer uses it.")
    A("4. A `quote_as` for IBTM only: \"about 97% even if its income earns only 2%\" (`reinvest.rung.IBTM`).")
    A("5. The M9 swap figures for the 2041 payment: 93.9% against 87.9% at 2%, and $23,266 against $23,146 at forward "
      "rates (`out/m9_screen_2026-09-28.json`). Until they land, SW40 and OD_B do not say \"at about the same cost\".")
    A("6. The ladder cost at the WInS prices actually paid against the curve (all five bonds were 2 to 15 hundredths "
      "of a percentage point of yield rich), for alternate C.")
    A("7. `market.etf_2026-09-28`: add the Nasdaq 30-session `adv30` the tickets use and relabel `avg_volume_20d` "
      "(it equals iShares' 30-day figure).")
    A("8. A scale-factor key (WInS book against Laura's plan after both deposits), only if the team wants a ratio in "
      "a reflection.")
    A("9. **The buyable-basis test** (R1(a)): the Book L ladder's cost on 1 Jan 2027, its room under $300,000 and its "
      "break-even fall, each with a `quote_as`, plus the yields-unchanged break-even (`ws4.breakeven_fall_bp`, "
      "22.78bp). If the buyable break-even is about 22bp, the IBTR note says \"about a fifth of a percentage point\"; "
      "the note, reflection and IPS then use that one basis.")
    A("10. Merge into `numbers.yaml`: `ws4.gap_odds_2027` (\"about 1 in 3\", zero-coupon basis) and "
      "`ws4.gap_if_any_typical` (\"typically about $10,000\") for the pick 1 reflection, and the WS3 fund comparison "
      "(\"no alternative moves the bad-case gift by more than about $1,500\", `numbers_ws3.yaml`) for pick 3.")
    A("11. A `quote_as` for the share of each payment owed as set coupons and principal (`reinvest.rung.*` at_0pct, "
      "84-95%), if a reflection wants a percentage for \"most of each payment\".")
    A("")
    A("## 8. Checks run by build_notes.py")
    A("")
    A("| Note | Chars | Length | ASCII | 1 para | Banned | Role | Laura | One number at most | Numbers traced (digits "
      "and words) | Dollar scale | Pick anchor | Friday fact fits |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for nid, cs in results.items():
        chars = next(x for x in NOTES + VARIANTS if x["id"] == nid)["exemplar"]
        A(f"| {nid} | {len(chars)} | " + " | ".join(("n/a" if c[2] == "n/a" else "pass") if c[1] else f"FAIL {c[2]}"
                                                    for c in cs) + " |")
    A("")
    A(f"Variety, across the {boiler['n']} Portfolio notes typed on Friday and Monday: the most common opening (first "
      f"three words) is used by {boiler['open'][1]} (\"{boiler['open'][0]}\", limit {MAX_SAME_OPEN}); the most common "
      f"ending (last four words) by {boiler['end'][1]} (\"{boiler['end'][0]}\", limit {MAX_SAME_END}). Across all "
      f"{boiler['all_n']} exemplars, including the conditional ones never typed together: {boiler['all_open'][1]} and "
      f"{boiler['all_end'][1]}.")
    A("")
    A(f"Pick openings (judge panel round 2): across every set of three notes that can be featured together "
      f"({' x '.join('/'.join(g) for g in PICK_SLOTS)}), the most pairs sharing their first two words in one set is "
      f"{pv[0]} (limit 1{'; ' + pv[1] if pv[1] else ''}).")
    A("")
    A("Superseded-book and stale-fact greps run over this file and `notes.csv` too (premortem Gate C items 4-5).")
    A("")
    A("## 9. Sources")
    A("")
    A("- Trading Note Instruction.pdf and Competition Guide.pdf p.3; Laura Gao 2026 Client Profile (\"willing to take "
      "thoughtful risks\"; payments \"toward the residency's operating expenses\"); Drive folder Knox Wharton 2026, "
      "official 2026-27.")
    A("- IPS Google Doc 1qtEuzXq_QYdQ9VJlusPY9km2l80E1hkk8FPR0iw71-w, read 30 Sep 2026 (read-only); text snapshot in "
      "`data/ips_doc_text_2026-09-30.txt`, and build_notes.py checks every quoted IPS sentence against it.")
    A("- Sheet 1EHCJxbFI0UOzNOpOWvDfzNqbK45qWuopZcL7HNN3VPM tabs WInS Notes, Portfolio, Book L (snapshots in "
      "`rab/data/sheet/`, read 30 Sep 00:30-00:34 AEST).")
    A("- iShares product pages, 28 Sep (`rab/data/ishares/`): monthly distributions; \"terminate on or about ... "
      "December 15\"; the Funds \"do not seek to return any predetermined amount\".")
    A("- iShares product screener, fetched 30 Sep 2026 ~02:34 AEST: https://www.ishares.com/us/product-screener/"
      "product-screener-v3.1.jsn (iBonds Treasury extract, with inception dates, in "
      "`data/ishares_ibonds_treasury_list_2026-09-30.csv`).")
    A("- U.S. Treasury MSPD Table V, record date 31 Aug 2026: https://api.fiscaldata.treasury.gov/services/api/"
      "fiscal_service/v1/debt/mspd/mspd_table_5 (`data/mspd_table5_2026-08-31.json`): late-2032 notes, the 2037-2041 "
      "bonds and the low-coupon Nov 2040 and Nov 2041 issues.")
    A("- `rab/numbers.yaml` (Gate A lock), `rab/assumptions.md` (R1), `tickets.md`, `M9_selection.md`, "
      "`october_trade.md`, `rab/premortem.md`, WS4 `rab/decisions/D_pre2027_rate_hedge.md` (the gap lands on the stock "
      "fund), WS3 `rab/decisions/D_fund_choice.md` (fund comparison), WS7 `rab/redteam/` (reinvestment check), "
      "insight_v1 `trading_notes_pack.md` (rules reused; its book is superseded), `D9_draft_checker.py` (ideas reused "
      "in `note_check.py`), Winning Team Portrait and Scoresheet.md, `judge_response.md` (both panels of 30 Sep).")
    A("")
    with open(path, "w") as f:
        f.write("\n".join(L))


def grep_outputs(paths):
    pats = [r"\bIEF\b", r"\bTLH\b", r"\bVGSH\b", r"\(ii\)R", r"duration match", r"(?<![\d,.$])9\.90(?!\d)",
            r"100,000", r"\$100k", r"Dec 4\b", r"500k", r"no Treasuries", r"\$0 commission"]
    hits = []
    for p in paths:
        txt = open(p).read()
        hits += [f"{os.path.basename(p)}: {q}" for q in pats if re.search(q, txt)]
    return hits


MAX_SAME_OPEN, MAX_SAME_END = 3, 2   # within the 11 Portfolio notes a judge reads together in Order History


def variety():
    """Most common opening (first 3 words) and ending (last 4 words) among the Portfolio notes typed on Friday and
    Monday (judge panel, 30 Sep: 10 of 12 opened alike and 8 ended alike). All exemplars are reported, not failed."""
    ex = [x["exemplar"] for x in NOTES if "Portfolio" in x["books"]]
    allx = [x["exemplar"] for x in NOTES + VARIANTS]
    top = lambda xs, f: Counter(f(t) for t in xs).most_common(1)[0]
    first3, last4 = (lambda t: " ".join(t.split()[:3])), (lambda t: " ".join(t.split()[-4:]))
    opens, ends = top(ex, first3), top(ex, last4)
    return {"n": len(ex), "open": opens, "end": ends, "all_n": len(allx), "all_open": top(allx, first3),
            "all_end": top(allx, last4), "ok": opens[1] <= MAX_SAME_OPEN and ends[1] <= MAX_SAME_END}


def main():
    Y, T, h = load_inputs()
    results, fails = {}, 0
    for n in NOTES + VARIANTS:
        cs = check_note(n)
        results[n["id"]] = cs
        fails += sum(1 for c in cs if not c[1])
    boiler = variety()
    pv = pick_variety()
    csv_path, md_path = os.path.join(HERE, "notes.csv"), os.path.join(HERE, "notes.md")
    rows = write_csv(csv_path, T, Y)
    write_md(md_path, T, Y, h, results, boiler, pv)
    g = grep_outputs([csv_path, md_path])
    ips_missing = check_ips_quotes()
    long_outlines = [(t, outline_words(b)) for t, b, x, _ in OUTLINES + ALT_OUTLINES
                     if outline_words(b) > MAX_OUTLINE_WORDS or (x and outline_words(b) + EXTRA_WORDS[x] > EXTRA_CAP)]
    seq_ok = all(any(r["book"] == b and int(r["seq"]) == s and r["id"].split(" (")[0] == n["ticker"] for r in T)
                 for n in NOTES for b, s in n["books"].items())
    for nid, cs in results.items():
        bad = [f"{c[0]} ({c[2]})" for c in cs if not c[1]]
        print(f"{nid:7s} {len(next(x for x in NOTES + VARIANTS if x['id'] == nid)['exemplar']):4d} chars  "
              f"{'pass' if not bad else 'FAIL: ' + ', '.join(bad)}")
    print(f"notes.csv rows: {len(rows)}; superseded/stale grep hits: {g or 'none'}; numbers.yaml {h[:12]}")
    print(f"IPS quotes not verbatim in the 30 Sep snapshot: {ips_missing or 'none'}")
    print("reflection outlines (words; + shared sentence): " + ", ".join(
        f"{t.split(',')[0]} {outline_words(b)}" + (f"+{EXTRA_WORDS[x]}" if x else "") for t, b, x, _ in OUTLINES + ALT_OUTLINES)
          + (f"; OVER {MAX_OUTLINE_WORDS} (or {EXTRA_CAP} with the shared sentence): {long_outlines}"
             if long_outlines else ""))
    print(f"pick openings: at most {pv[0]} shared pair in any set of three (limit 1){' ' + pv[1] if pv[1] else ''}: "
          f"{'pass' if pv[0] <= 1 else 'FAIL'}")
    print(f"variety: opening '{boiler['open'][0]}' x{boiler['open'][1]} (max {MAX_SAME_OPEN}), ending "
          f"'{boiler['end'][0]}' x{boiler['end'][1]} (max {MAX_SAME_END}): {'pass' if boiler['ok'] else 'FAIL'}")
    print(f"note seq matches tickets.csv (security and order): {'pass' if seq_ok else 'FAIL'}")
    nfail = fails + len(g) + len(ips_missing) + len(long_outlines) + (not boiler["ok"]) + (not seq_ok) + (pv[0] > 1)
    print(f"{nfail} fail")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
