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
from datetime import datetime

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from trades_clock import ET, both  # noqa: E402

LABEL = "EXAMPLE - team rewrites"

# ----------------------------------------------------------------------------------------------- word rules
# One rule set for exemplars and team drafts: rab/trades/note_rules.py (standard library only).
from note_rules import BANNED, MAX_NOTE, check_text  # noqa: E402,F401

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
    "EQUITY": ("Equities should outperform Treasuries over five years but can fall sharply, so moving money from the "
               "floor into equities raises the expected outcome modestly but widens the range of results."),
}

# ----------------------------------------------------------------------------------------------- the notes
# Each spec: exemplar text; the numbers it uses (token -> source); brief fields. Per-book sizes come from tickets.csv.
# Payment order: 1 Jan 2033 is Laura's 1st payment ... 1 Jan 2042 her 10th (case: ten $50,000 payments 2033-2042).
NOTES = [
    dict(
        id="IBTR", ticker="IBTR", books={"Portfolio": 1, "BookL": 1}, use="Friday order 1 (both books)",
        rung="IBTR", job="payments", tn_role="supported",
        serves="Laura's 5th payment, $50,000 on 1 Jan 2037 (2027 deposit)",
        facts=["iShares iBonds Dec 2036 Term Treasury ETF: 4 Treasuries maturing in 2036; ends on or about "
               "15 Dec 2036; pays income monthly (iShares, 28 Sep)",
               "first order of the day: the IPS buys the latest payments first",
               "thinnest fund: about $38m in assets (iShares, 28 Sep); place it after the first hour"],
        ips=["LATEST", "FALL"],
        number=("optional, Laura's plan: 'yields would have to fall about a quarter of a percentage point before "
                "1 Jan 2027 for the ten payments to cost more than $300,000'",
                "laura.ladder.breakeven_fall_bp_strips (26.2bp, MODEL, 28 Sep curve; re-lock after Friday)"),
        dont=["that the fund pays a set $50,000", "'thin' or 'risky' as a description of the holding",
              "any WInS dollar amount as if it were Laura's"],
        friday="WInS name string for IBTR; if IBTR cannot be bought, the order becomes IBTQ and this note changes.",
        exemplar=("Role: future funding. This iShares iBonds Treasury fund ends in Dec 2036, before Laura's 1 Jan "
                  "2037 payment. We buy the latest payments first, so if yields fall before 2027 any gap is in the "
                  "earliest payment, which her 2028 deposit can fill. Its income is reinvested at unknown rates."),
        nums={},
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
        dont=["that no Treasury matures in those years at all (notes do; WInS just does not list them)"],
        friday="WInS name string for IBTQ; the gap in the bond list (re-read the drop-down).",
        exemplar=("Role: future funding. For Laura's $50,000 payment on 1 Jan 2036 we are buying this iShares iBonds "
                  "Treasury fund, which ends in Dec 2035. WInS lists no Treasury bond maturing between Feb 2031 and "
                  "Feb 2036, so a dated fund is the closest fit. Its income must be reinvested until then."),
        nums={},
    ),
    dict(
        id="IBTP", ticker="IBTP", books={"Portfolio": 3, "BookL": 3}, use="Friday order 3 (both books)",
        rung="IBTP", job="payments", tn_role="supported",
        serves="Laura's 3rd payment, $50,000 on 1 Jan 2035 (2027 deposit)",
        facts=["iShares iBonds Dec 2034 Term Treasury ETF: 4 Treasuries; ends on or about 15 Dec 2034; monthly "
               "income (iShares, 28 Sep)",
               "yield check, 28 Sep: the fund's average yield (5.19%) was 1.7bp from the Treasury par curve at its "
               "average maturity; price 0.06% above the value of its bonds"],
        ips=["PITCH"],
        number=("'within 0.02 of a percentage point' of the Treasury curve on 28 Sep",
                "wins.ibond_checks.IBTP.avg_ytm_minus_par_at_wam_bp = 1.7 (MODEL; quote_as 'within 2bp')"),
        dont=["'bp'", "that the yield is locked in for Laura"],
        friday="Keep 'On 28 Sep' unless the team re-runs the check on Friday's numbers (then use that date).",
        exemplar=("Role: future funding. This iShares iBonds Treasury fund ends in Dec 2034, before Laura's $50,000 "
                  "payment on 1 Jan 2035. On 28 Sep its yield was within 0.02 of a percentage point of the Treasury "
                  "curve, so the price looked fair. Its income must be reinvested, so the end value can vary."),
        nums={"0.02": "wins.ibond_checks.IBTP (1.7bp)"},
    ),
    dict(
        id="IBTO", ticker="IBTO", books={"Portfolio": 4, "BookL": 4}, use="Friday order 4 (both books)",
        rung="IBTO", job="payments", tn_role="supported",
        serves="Laura's 2nd payment, $50,000 on 1 Jan 2034 (2027 deposit)",
        facts=["iShares iBonds Dec 2033 Term Treasury ETF: 11 Treasuries; ends on or about 15 Dec 2033; monthly "
               "income (iShares, 28 Sep)",
               "trap: in WInS, IBTN is INSCORP Inc (SEEN 29 Sep); iShares has no fund with the ticker IBTN "
               "(iShares product list, 30 Sep)"],
        ips=["PITCH"],
        number=("none needed", "-"),
        dont=["anything unkind about the other company; just 'an unrelated company'"],
        friday="Type IBTO and IBTN once each; copy both names exactly as WInS shows them.",
        exemplar=("Role: future funding. For Laura's $50,000 payment on 1 Jan 2034 we are buying the iShares iBonds "
                  "Dec 2033 Term Treasury ETF. We typed IBTO and read the name aloud, because IBTN in WInS is an "
                  "unrelated company. Its income must be reinvested, so the amount it delivers can vary."),
        nums={},
    ),
    dict(
        id="IBTM_P", ticker="IBTM", books={"Portfolio": 5}, use="Friday order 5 (Portfolio book)",
        rung="IBTM", job="payments + floor", tn_role="refined",
        serves=("two jobs: Laura's 1st payment, $50,000 on 1 Jan 2033 (2027 deposit), and the facility floor "
                "(2028 deposit)"),
        facts=["iShares iBonds Dec 2032 Term Treasury ETF (SEEN in WInS 29 Sep): 15 Treasuries; ends on or about "
               "15 Dec 2032; monthly income (iShares, 28 Sep)",
               "WInS lists no Treasury maturing in late 2032 (SEEN 29 Sep), so the IPS floor ('Treasuries maturing "
               "in late 2032') is held in this fund, together with the 2033 payment",
               "iShares: an iBonds fund 'does not seek to return any predetermined amount'",
               "Portfolio tab: 32.5% of the book, of which 24.3 points are the floor",
               "Laura's plan: the floor costs about $117,000 of her 2028 deposit at the 28 Sep 5-year yield "
               "(laura.floor_cost_2028, MODEL; never in a note)"],
        ips=["FLOOR", "PITCH"],
        number=("'about a third of our WInS portfolio'",
                "wins.portfolio.holdings_close_0928 IBTM weight 0.3254 (WInS book)"),
        dont=["that it 'repays' or 'holds' a dollar floor (never '$150,000' next to this holding: PM-15)",
              "any 2031 range, top or co-sponsor figure (TN guide: not expected yet)",
              "that the floor or the payment is a fixed amount (the fund's end value is not fixed)"],
        friday="Re-read the WInS bond list for a late-2032 Treasury (if one appears, tell Ray before trading).",
        exemplar=("Role: future funding and risk management. This iShares iBonds Treasury fund, ending Dec 2032, has "
                  "two jobs in Laura's plan: her first $50,000 payment and the facility floor her 2028 deposit buys. "
                  "WInS lists no late-2032 Treasury bond, so we use this fund. Its end value is not fixed."),
        nums={},
    ),
    dict(
        id="IBTM_L", ticker="IBTM", books={"BookL": 5}, use="Friday order 5 (Book L only)",
        rung="IBTM", job="payments", tn_role="refined",
        serves="Laura's 1st payment, $50,000 on 1 Jan 2033 (2027 deposit); Book L holds no floor",
        facts=["iShares iBonds Dec 2032 Term Treasury ETF (SEEN 29 Sep): ends on or about 15 Dec 2032; monthly income",
               "WInS lists no Treasury maturing in late 2032 (SEEN 29 Sep)",
               "Book L = Laura's 2027 deposit dollar for dollar: the floor and the stock fund are bought in 2028 "
               "and never appear in WInS"],
        ips=["PITCH"],
        number=("none needed", "-"),
        dont=["the floor (Book L does not hold it)", "'repays $50,000'"],
        friday="As for the Portfolio book.",
        exemplar=("Role: future funding. This iShares iBonds Treasury fund ends in Dec 2032, before Laura's first "
                  "$50,000 payment on 1 Jan 2033. WInS lists no Treasury bond maturing in late 2032, so this fund is "
                  "the closest fit. Its income must be reinvested, so its end value is not fixed."),
        nums={},
    ),
    dict(
        id="VT", ticker="VT", books={"Portfolio": 6}, use="Friday order 6 (Portfolio book only)",
        rung=None, job="stock fund (growth)", tn_role="supported",
        serves="the return-seeking portfolio: growth for Laura's 2033 facility contribution above the floor",
        facts=["Vanguard Total World Stock ETF (SEEN in WInS 29 Sep): a global index fund of thousands of companies",
               "bought after all ten dated holdings and the floor: payments first, then growth",
               "Portfolio tab: 8.7% of the book; in Laura's plan about $41,000 on 2 Jan 2028 (MODEL)"],
        ips=["BRANCH", "DECLINE"],
        number=("'about 9% of our WInS portfolio' (or, not both: 'about $41,000 in Laura's plan')",
                "wins.portfolio.split_close_0928 vt 0.0868 (WInS book); laura.stock_fund_2028_usd.strips 40,736"),
        dont=["a return forecast (the IPS's 'should outperform' belongs in the IPS, not a note)",
              "probabilities, CAPE or valuation calls", "'Laura likes risk'", "any 2031 or 2033 dollar figure"],
        friday="VT's share after re-sizing (still 'about 9%' unless the refresh moves it by a point).",
        exemplar=("Role: growth. Money goes to stocks only after the payments and the facility floor are bought: "
                  "about 9% of our WInS portfolio, in this world fund of thousands of companies, held to 2033. A "
                  "stock fall can shrink only the part of Laura's facility contribution above the floor."),
        nums={"9%": "wins.portfolio.split_close_0928 (vt 0.0868)"},
    ),
    dict(
        id="T41", ticker="T 3.125% 15-Nov-2041", books={"Portfolio": 7, "BookL": 6},
        use="Friday bond order (both books)", rung="T_3.125%_15-Nov-2041", job="payments", tn_role="supported",
        serves="Laura's 10th and last payment, $50,000 on 1 Jan 2042 (2027 deposit)",
        facts=["U.S. Treasury bond 3.125% due 15 Nov 2041, CUSIP 912810QT8; matures 47 days before the payment; "
               "coupons twice a year",
               "no iBonds Treasury fund ends between Dec 2037 and Dec 2043 (iShares product list, 30 Sep), so the "
               "2038-2042 payments use individual bonds",
               "WInS price 76.367 (28 Sep) is 1.9bp from the curve: passes"],
        ips=["PITCH"],
        number=("none needed", "-"),
        dont=["that the bond delivers a fixed $50,000 including coupons"],
        friday="Price inside the 25bp band; if the team swaps to the 2.000% Nov-2041, use exemplar SW41.",
        exemplar=("Role: future funding. The 3.125% Treasury bond maturing 15 Nov 2041 is for Laura's last $50,000 "
                  "payment, on 1 Jan 2042. No iBonds Treasury fund ends between 2037 and 2043, so her last five "
                  "payments use individual Treasury bonds. Its coupons must be reinvested until then."),
        nums={},
    ),
    dict(
        id="T40", ticker="T 4.250% 15-Nov-2040", books={"Portfolio": 8, "BookL": 7},
        use="Friday bond order (both books), if the low-coupon question is still open",
        rung="T_4.250%_15-Nov-2040", job="payments", tn_role="supported",
        serves="Laura's 9th payment, $50,000 on 1 Jan 2041 (2027 deposit)",
        facts=["U.S. Treasury bond 4.250% due 15 Nov 2040, CUSIP 912810QL5; WInS price 89.186 (28 Sep) is 5.1bp "
               "from the curve: passes",
               "same-date alternate 1.375% 15 Nov 2040 (912810ST6): WInS listing UNVERIFIED; about 38% of the "
               "4.250% bond's cash before 2041 comes as coupons against about 17% (M9, MODEL; not in numbers.yaml)"],
        ips=["PITCH"],
        number=("none from numbers.yaml; the M9 coupon shares (38% vs 17%) need a numbers.yaml entry before any "
                "note uses them", "M9_selection.md (MODEL)"),
        dont=["that the swap will happen; say 'we are checking'"],
        friday="If the 1.375% is listed and swapped, use SW40; if WInS does not list it, use T40b.",
        exemplar=("Role: future funding. The 4.250% Treasury bond maturing 15 Nov 2040 is for Laura's $50,000 "
                  "payment on 1 Jan 2041. Reinvesting its coupons until then is the main risk, so we are checking "
                  "whether WInS lists a lower-coupon bond of the same date. Its price passed our curve check."),
        nums={},
    ),
    dict(
        id="T39", ticker="T 4.375% 15-Nov-2039", books={"Portfolio": 9, "BookL": 8},
        use="Friday bond order (both books)", rung="T_4.375%_15-Nov-2039", job="payments", tn_role="supported",
        serves="Laura's 8th payment, $50,000 on 1 Jan 2040 (2027 deposit)",
        facts=["U.S. Treasury bond 4.375% due 15 Nov 2039, CUSIP 912810QD3; matures 47 days before the payment",
               "WInS price 91.363 (28 Sep) is 6.6bp from the curve: passes",
               "trap: WInS also lists a 4.375% bond of 15 Feb 2038, with a stale price; pick by coupon AND date"],
        ips=["HELD"],
        number=("none needed", "-"),
        dont=["that its price cannot fall (it can; only the amount due at maturity is set)"],
        friday="Price inside the 25bp band.",
        exemplar=("Role: future funding. The 4.375% Treasury bond maturing 15 Nov 2039 is for Laura's $50,000 "
                  "payment on 1 Jan 2040. Its price will move with interest rates, but we hold it to maturity, so "
                  "the amount due then does not change. Only the rate its coupons earn until then is unknown."),
        nums={},
    ),
    dict(
        id="T38", ticker="T 4.500% 15-May-2038", books={"Portfolio": 10, "BookL": 9},
        use="Friday bond order (both books)", rung="T_4.500%_15-May-2038", job="payments", tn_role="tested",
        serves="Laura's 7th payment, $50,000 on 1 Jan 2039 (2027 deposit)",
        facts=["U.S. Treasury bond 4.500% due 15 May 2038, CUSIP 912810PX0: the latest Treasury bond maturing before the "
               "payment (MSPD list, M9; ends about 7.6 months early)",
               "yield check, 28 Sep prices: this bond 14.4bp from the curve (passes); the 4.375% Feb 2038 bond at "
               "99.98 was 92bp off and the 4.5% Feb 2036 at 102.95 was 111bp off (both stale)",
               "the Sheet records this bond's accrued interest as 0.530; about 1.66 is right (fix before 6 Nov)"],
        ips=["PITCH", "COST"],
        number=("'about 1 point of yield' (the stale Feb 2038 price)",
                "wins.bond_check.T_4.375%_15-Feb-2038 gap_bp -92.1 (MODEL; quote_as 'about 1 point of yield off')"),
        dont=["that WInS is 'wrong' or 'broken' (say 'stale')", "'bp'", "the Sheet's accrued-interest typo"],
        friday=("Re-check both prices on Friday. If the Feb 2038 price now passes, say what the check showed that "
                "day, or date the stale price ('on 29 Sep ...')."),
        exemplar=("Role: future funding. For Laura's 1 Jan 2039 payment we chose this 4.500% Treasury bond of 15 May "
                  "2038, coupons reinvested. We checked each candidate's WInS price against the Treasury yield curve: "
                  "the 4.375% Feb 2038 bond was about 1 point of yield off, so we treated it as stale."),
        nums={"1 point": "wins.bond_check.T_4.375%_15-Feb-2038 (gap -92.1bp)"},
    ),
    dict(
        id="T37", ticker="T 4.750% 15-Feb-2037", books={"Portfolio": 11, "BookL": 10},
        use="Friday bond order, last of the day (both books)", rung="T_4.750%_15-Feb-2037", job="payments",
        tn_role="supported",
        serves="Laura's 6th payment, $50,000 on 1 Jan 2038 (2027 deposit)",
        facts=["U.S. Treasury bond 4.750% due 15 Feb 2037, CUSIP 912810PT9; matures about 10.5 months before the "
               "payment, so its money waits",
               "WInS price 97.152 (28 Sep) is 15.3bp from the curve: passes",
               "alternate 5.000% 15 May 2037 (912810PU6): WInS listing UNVERIFIED; about equal at 2% reinvestment "
               "(M9)"],
        ips=["PITCH", "HELD"],
        number=("'about ten months early' (date arithmetic)", "maturity 15 Feb 2037 vs payment 1 Jan 2038"),
        dont=["that the waiting money earns interest in WInS (WInS cash earns 0%)"],
        friday="Price inside the 25bp band; last order, sized from the cash left.",
        exemplar=("Role: future funding. The 4.750% Treasury bond maturing 15 Feb 2037 is for Laura's $50,000 "
                  "payment on 1 Jan 2038. It matures about ten months early, and that money waits for the payment. "
                  "Its coupons must be reinvested until then, so the total depends partly on future rates."),
        nums={},
    ),
]

# Variants and conditional notes (not Friday tickets unless the team decides so).
VARIANTS = [
    dict(
        id="T40b", ticker="T 4.250% 15-Nov-2040", use="Friday, if WInS does not list the 1.375% Nov-2040",
        tn_role="supported", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"],
        brief="Same bond as T40. Use when the drop-down shows no 1.375% 15 Nov 2040 bond.",
        exemplar=("Role: future funding. The 4.250% Treasury bond maturing 15 Nov 2040 is for Laura's $50,000 "
                  "payment on 1 Jan 2041. We looked for a lower-coupon bond of the same date, which would leave less "
                  "income to reinvest, but WInS does not list one. Its price passed our curve check."),
        nums={},
    ),
    dict(
        id="SW40", ticker="T 1.375% 15-Nov-2040", use="Friday --swap, only if listed, passing, and voted on 1 Oct",
        tn_role="refined", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"],
        brief=("Replaces T40 on Friday. CUSIP 912810ST6. Accept a WInS clean price only between 58.474 and 62.116 "
               "(25bp band, tickets.md). The IPS must also gain a sentence on reinvested coupons."),
        exemplar=("Role: future funding. The 1.375% Treasury bond maturing 15 Nov 2040 is for Laura's $50,000 "
                  "payment on 1 Jan 2041. We chose it over the 4.250% bond of the same date because its low coupon "
                  "leaves less income to reinvest at unknown rates. Its price passed our curve check."),
        nums={},
    ),
    dict(
        id="SW41", ticker="T 2.000% 15-Nov-2041", use="Friday --swap, only if listed, passing, and voted on 1 Oct",
        tn_role="refined", serves="Laura's 10th payment (1 Jan 2042)", ips=["PITCH"],
        brief=("Replaces T41 on Friday. CUSIP 912810TC2. Accept a WInS clean price only between 62.639 and 66.568 "
               "(25bp band, tickets.md)."),
        exemplar=("Role: future funding. The 2.000% Treasury bond maturing 15 Nov 2041 is for Laura's last $50,000 "
                  "payment, on 1 Jan 2042. We chose it over the 3.125% bond of the same date: a lower coupon means "
                  "less income to reinvest before the payment. Its price passed our curve check."),
        nums={},
    ),
    dict(
        id="OD_S", ticker="T 4.250% 15-Nov-2040", use="October trigger D, day 1: sell (october_trade.md)",
        tn_role="refined", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"],
        brief=("Sell the whole holding (Portfolio $17,000 face; Book L $26,000). Never on the day it was bought. "
               "Only if the team has agreed the IPS wording on coupons."),
        exemplar=("Role: future funding. We are selling the 4.250% Treasury bond maturing 15 Nov 2040 to replace it "
                  "with the 1.375% bond of the same date, for Laura's 2041 payment. The lower coupon leaves less "
                  "income to reinvest at unknown rates. We buy the new bond once this sale's cash shows."),
        nums={},
    ),
    dict(
        id="OD_B", ticker="T 1.375% 15-Nov-2040", use="October trigger D, day 2: buy (october_trade.md)",
        tn_role="refined", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"],
        brief=("Face value from refresh_tickets.py --swap on the day; WInS price inside the 25bp band the refresh "
               "prints (28 Sep band: 58.474 to 62.116). The natural 'refined' pick if it fills with a saved note by "
               "20 Oct ET."),
        exemplar=("Role: future funding. We are buying the 1.375% Treasury bond maturing 15 Nov 2040 in place of the "
                  "4.250% bond we sold. Same date and issuer, for Laura's 2041 payment, but more of its value comes "
                  "at maturity, so less rides on reinvesting coupons. Its price passed our curve check."),
        nums={},
    ),
    dict(
        id="OB_S", ticker="VT", use="October trigger B: sell part of VT (rates-fall test)",
        tn_role="tested", serves="the floor and the 2033 payment, before growth", ips=["FALL"],
        brief=("Fires only if the refresh on the 14 Oct close says the ten payments cost more than $300,000 on "
               "1 Jan 2027 (today about $292,000, laura.ladder.cost_2027_strips). Size from the refresh; only if at "
               "least $2,500. WS1 adds the new cost to numbers.yaml before any note quotes it."),
        exemplar=("Role: future funding. Yields have fallen, so in our model the ten payments now cost more than "
                  "Laura's $300,000 first deposit and her 2028 deposit must finish the 2033 payment. Less is left for "
                  "stocks, so we are moving part of this world stock fund into the 2032 Treasury fund."),
        nums={},
    ),
    dict(
        id="OB_B", ticker="IBTM", use="October trigger B: buy IBTM with the VT proceeds",
        tn_role="tested", serves="Laura's 1st payment and the floor", ips=["FALL", "LATEST"],
        brief="The natural 'tested' pick if trigger B fires and fills by 20 Oct ET.",
        exemplar=("Role: future funding. We are adding to the iShares iBonds Dec 2032 Treasury fund with money from "
                  "the stock fund. After yields fell, Laura's 2028 deposit must complete her 2033 payment, as our "
                  "plan expects, so the payments come first. Its end value is not fixed."),
        nums={},
    ),
    dict(
        id="OC", ticker="VT", use="October trigger C: spare cash above $6,300 into VT",
        tn_role="supported", serves="growth for the facility contribution", ips=["BRANCH"],
        brief="Buy VT with everything above the $3,300 float (october_trade.md).",
        exemplar=("Role: growth. WInS pays no interest on cash, and our cash is above what fees and rounding need, so "
                  "we are adding the extra to the world stock fund, the part of Laura's plan held for growth to 2033. "
                  "The dated Treasury holdings for her payments stay as they are."),
        nums={},
    ),
]

def check_note(n):
    """Every check in note_rules.check_text must pass for an exemplar (FAIL and WARN alike)."""
    return [(name, ok, detail) for name, ok, detail, _sev in check_text(n["exemplar"], list(n.get("nums", {})))]


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
        lines.append(f"Laura's plan: {round_k(r['cost'])} of her 2027 deposit buys {what}; if its income earns "
                     f"only 2%, it delivers {round_k(r['at_2pct'])} of the $50,000 (reinvest.rung.{n['rung']}, "
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
                             numbers="; ".join(f"{k} = {v}" for k, v in n.get("nums", {}).items())))
    for v in VARIANTS:
        brief = (f"Serves: {v['serves']}. {v['brief']} IPS: " +
                 " / ".join(f"\"{IPS[k]}\"" for k in v["ips"]))
        rows.append(dict(ticker=v["ticker"], brief=brief, exemplar=v["exemplar"], char_count=len(v["exemplar"]),
                         book="conditional", seq="", note_id=v["id"], use=v["use"], label=LABEL,
                         numbers="; ".join(f"{k} = {x}" for k, x in v.get("nums", {}).items())))
    order = {"Portfolio": 0, "BookL": 1, "conditional": 2}
    rows.sort(key=lambda r: (order[r["book"]], int(r["seq"]) if r["seq"] != "" else 99))
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ticker", "brief", "exemplar", "char_count", "book", "seq", "note_id",
                                          "use", "label", "numbers"])
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
    L.append(f"- **Serves:** {n['serves']}. **Job:** {n['job']}. **Likely TN role:** {n['tn_role']}.")
    for f_ in n["facts"]:
        L.append(f"- {f_}")
    for l in book_facts(n, T, Y):
        L.append(f"- {l}")
    for k in n["ips"]:
        L.append(f"- **IPS:** \"{IPS[k]}\"")
    L.append(f"- **One number:** {n['number'][0]}. Source: {n['number'][1]}.")
    L.append(f"- **Do not say:** {'; '.join(n['dont'])}.")
    L.append(f"- **Re-check Friday:** {n['friday']}")
    ok = all(c[1] for c in checks)
    L += ["", f"> **{LABEL}** ({len(n['exemplar'])} characters; checks {'pass' if ok else 'FAIL'})", ">",
          f"> {n['exemplar']}", ""]
    return L


def write_md(path, T, Y, h, results):
    tn_due = t2(2026, 10, 23, 17, 0)
    submit = t2(2026, 10, 22, 2, 0)
    oct_close = t2(2026, 10, 20, 15, 30)
    L = []
    A = L.append
    A("# WInS note briefs, EXAMPLE notes and the three Trading Notes Analysis picks")
    A("")
    A("WS6-notes, RAB Kit, 30 Sep 2026 (Sydney). AI-generated research (Claude Code, Claude Opus 5.5) for Team "
      "Caplet. **Every exemplar is labelled `EXAMPLE - team rewrites`.** Students write the notes typed into WInS "
      "and every reflection; this file supports them and is logged in `docs/AI_USE.md`. If any exemplar wording is "
      "used, the Final Report's Works Cited discloses it. Generated by `rab/trades/build_notes.py` from "
      f"`tickets.csv` and the locked `rab/numbers.yaml` (sha256 {h[:12]}...); do not edit by hand. Basis: 28 Sep "
      "2026 curve and closes, WInS prices seen 29 Sep. Nothing here changes the strategy.")
    A("")
    A("**Bottom line.**")
    A("")
    longest = max(len(x["exemplar"]) for x in NOTES + VARIANTS)
    A("- Every Friday ticket (both books) has a brief and an exemplar; so do the Friday swap variants and each "
      f"October trigger. All exemplars are {longest} characters or fewer, plain ASCII, one paragraph, and pass the "
      "banned-word and number checks (s8).")
    A("- **Feature these three in the Trading Notes Analysis** (Portfolio book): **IBTM** (refined: a dated fund "
      "carries the floor because WInS lists no late-2032 Treasury), **the 4.500% May 2038 bond** (tested: the price "
      "check that rejected a stale WInS price), and **VT** (supported: growth only with money nobody else relies on). "
      "They cover payments, floor and growth, and one is a process check. Alternates: IBTR and the October trade (s6).")
    A("- **Book L** would leave the analysis with payments only: the floor and the stock fund never appear in WInS. "
      "That is a point for the 1 Oct vote, not a change to the plan (s7).")
    A("")
    A("## 1. What a note must do")
    A("")
    A("- **Official test** (Competition Guide p.3): a note captures \"the reasoning behind the decision, including its "
      "alignment with your strategy, the supporting research or analysis, and its expected role in growth, "
      "liquidity, risk management, or future funding.\" The TN Analysis later quotes three notes \"exactly as it "
      "appears in WInS\" and asks how each decision \"aligned with, tested, or refined\" the strategy (Trading Note "
      "Instruction).")
    A("- **Shape used by every exemplar:** `Role: <official role word>.` + what is bought and which of Laura's needs "
      "it serves + the research or check behind it + the honest limit. About 45 words.")
    A("- **The box:** 300 characters maximum (maxlength, SEEN 29 Sep). The kit limit is **285**, plain ASCII (straight "
      "quotes; no dashes, `~` or `<=`), one paragraph. Whether a saved note can be edited is UNVERIFIED: treat the first "
      "save as final.")
    A("- **Laura-specific:** name the payment date, the floor or the facility. Would the note be true of any client? "
      "Then rewrite it.")
    A("- **Numbers:** at most one analytic number, from `numbers.yaml` or a named, dated source. Dollar figures only as "
      "Laura's case facts ($50,000 payments, $300,000 first deposit) or \"in Laura's plan\"; WInS amounts as "
      "percentages. Never a WInS gain, loss or ranking.")
    A("- **Coupon caveat:** every note that ties a holding to a payment says, in a few words, that its income or "
      "coupons must be reinvested (premortem PM-23). A bond's amount due at maturity is set; the total with "
      "reinvested coupons is not. An iBonds fund's end value is never fixed.")
    A("- **No strategy name** in WInS notes (Root-and-Branch / Roots First / Roots are all in use) and no "
      "roots-and-branch metaphors until Ray confirms the name. Plain words survive a rename.")
    A("")
    A("## 2. Words never used in a note")
    A("")
    A("This list quotes the banned words on purpose; `build_notes.py` checks the exemplars, not this section.")
    A("")
    A("- guaranteed, risk-free, no risk, locked, lock in, safe, stable, \"reduce volatility\", certain, 100%, promised, "
      "pledged (overclaims; say \"backed by the U.S. government\").")
    A("- match / matched (false for funds and coupon bonds), \"cash-flow matched\", \"needs no rebalancing\".")
    A("- \"I bond\" (a U.S. savings bond); write \"iBonds\" or the fund's full name. Never \"repays $X\" for an iBonds fund.")
    A("- Forecasts and results: will grow / will outperform, CAPE, overvalued, profit, gain, rank.")
    A("- \"Laura's portfolio\" for the WInS book; operating reserve size; any 2031 range, top or co-sponsor figure "
      "(the TN guide says these are not expected yet); Laura quotes; her degree, heritage or Taiwan as a reason.")
    A("- Jargon without a gloss: bp, basis points, duration, immunization.")
    A("")
    A("## 3. How the team uses this (Thu 1 Oct to Sat 3 Oct)")
    A("")
    A("1. Each note has a named student writer (Friday runbook roles). The writer drafts **from the brief, with the "
      "exemplar closed**, then compares.")
    A("2. Run the checker on the draft: `/Users/ray/Research/rab-ws/.venv/bin/python rab/trades/note_check.py --ticker "
      "IBTM --text \"...\"`. It counts characters, checks ASCII and banned words, and measures **phrase overlap with "
      "the exemplar** (share of the draft's three-word phrases found in it). 50% or more: rewrite, or disclose the "
      "exemplar in Works Cited (PM-13). Plain word overlap is not used: an honest rewrite shares the facts.")
    A("3. Note keeper holds the final texts, pastes each at Preview, reads it aloud once.")
    A("4. After saving: Order History > Add/View Notes, copy the note back into the Trade Log and compare it with the "
      "plan character for character (the box cuts silently at 300).")
    A("5. Log in `docs/AI_USE.md` which exemplars were read and whether any wording was kept.")
    A("")
    A("## 4. Friday notes, Portfolio book (Book L differences inline)")
    A("")
    A("Order: iBonds funds latest payment first, then VT, then bonds latest payment first (`tickets.md`). Book L is "
      "the same list without VT; only IBTM's note differs. Sizes are the Gate A tickets; Friday's refresh re-sizes "
      "them. WInS names of IBTO-IBTR and every bond string are UNVERIFIED until read on Friday.")
    A("")
    for n in NOTES:
        L.extend(md_note(n, T, Y, results[n["id"]]))
    A("## 5. Variants and October notes (conditional)")
    A("")
    A("Use only when the named condition holds. October trades follow `october_trade.md`; if trigger A (repair) fires, "
      "reuse that ticket's Friday note and, if it fits, add \"Friday's order did not fill.\"")
    A("")
    A("| Id | Holding | Use when | Serves | Brief | EXAMPLE - team rewrites | Chars |")
    A("|---|---|---|---|---|---|---|")
    for v in VARIANTS:
        A(f"| {v['id']} | {v['ticker']} | {v['use']} | {v['serves']} | {v['brief']} IPS: "
          f"\"{IPS[v['ips'][0]]}\" | {v['exemplar']} | {len(v['exemplar'])} |")
    A("")
    A("## 6. Trading Notes Analysis: the three notes to feature")
    A("")
    A(f"Due {tn_due}. Target: submit {submit}, a day early. Rules (TN guide; premortem PM-19): only trades that "
      "**filled** and have a **saved note**; three different jobs; each note quoted exactly as WInS shows it; "
      "reflections of 100 words or fewer, written by students without AI (plan 95 by two counters).")
    A("")
    A("| Pick | Note | Role | Job | Why this one |")
    A("|---|---|---|---|---|")
    A("| 1 | IBTM, Friday #5 (IBTM_P) | **refined** | payments + floor | The most Laura-specific holding: the floor "
      "is what she can tell co-sponsors, and it carries her first payment. It shows the plan adapting to what WInS "
      "offers: the IPS says \"Treasuries maturing in late 2032\", WInS lists none (SEEN 29 Sep), so a fund ending "
      "Dec 2032 does both jobs. Honest limit: its end value is not fixed. |")
    A("| 2 | 4.500% 15 May 2038 bond, Friday #10 (T38) | **tested** | payments + process check | A check a judge can "
      "verify: the WInS price of every bond the team considered was tested against the official Treasury curve "
      "before buying. Two prices failed, one of them the other 2038 bond. It links the plan's cost claim to the "
      "prices actually paid (funding reliability). |")
    A("| 3 | VT, Friday #6 (VT) | **supported** | growth | Shows the balance the Guide asks for: growth only with money "
      "nobody else relies on, bought after the payments and floor. Answers \"why so little stock?\" with the "
      "client's own priorities. |")
    A("")
    A("**Alternates (keep two):** (a) **IBTR, Friday #1** (supported: \"latest payments first\", the rule for a fall "
      "in yields); (b) **the 3.125% Nov 2041 bond, Friday #7** (supported: why the last five payments use bonds).")
    A("")
    A(f"**If an October trade fills with a saved note by {oct_close}:**")
    A("")
    A("- **Trigger D (coupon swap):** feature the **buy leg (OD_B)** as **refined** in place of pick 2, and relabel "
      "IBTM **supported**. The D reflection carries the price check the new bond passed, so a process check stays in.")
    A("- **Trigger B (rates fall):** feature the **IBTM buy (OB_B)** as **tested** in place of pick 1; keep the May "
      "2038 bond as **supported (with a price check)**. The B reflection covers the floor.")
    A("- **Trigger C or none:** keep the three above. Never add a trade to create a pick.")
    A("")
    A("**If the 1 Oct vote picks Book L:** feature IBTM (IBTM_L, refined), the May 2038 bond (tested) and IBTR "
      "(supported); alternates the Nov 2041 bond and IBTQ. All three are payments: each reflection must say once "
      "that WInS holds only Laura's 2027 deposit, and the floor and stock fund come in 2028.")
    A("")
    A("### Reflection outlines (bullets only; students write the prose, 100 words or fewer)")
    A("")
    A("**Pick 1, IBTM (refined).**")
    A("")
    A("- Why: the IPS floor is \"Treasuries maturing in late 2032\"; WInS lists no Treasury between Feb 2031 and "
      "Feb 2036 (SEEN 29 Sep); a fund ending about 15 Dec 2032 was the closest fit, so one holding took two jobs.")
    A("- Aligned: IPS floor sentence and \"latest payments first\" (the 2033 payment is the one the 2028 deposit can "
      "complete).")
    A("- Served Laura: the first payment her artists rely on, and the least she can quote co-sponsors, sit outside "
      "the stock market.")
    A("- Refined (only if true): the 29 Sep WInS Notes entry is dated before the order; cite that change, not a new "
      "strategy.")
    A("- Honest limit: iShares says the fund \"does not seek to return any predetermined amount\"; its income is "
      "reinvested. If confidence is mentioned: \"certain by construction if the floor holdings pay, the 2028 deposit "
      "arrives and the gift is capped\"; no dollar figure (the floor announced rounded down is Final Report "
      "material).")
    A("- One number at most: \"about a third of our WInS portfolio\".")
    A("")
    A("**Pick 2, 4.500% May 2038 bond (tested).**")
    A("")
    A("- Why: before any bond order the team compared each WInS price with the Treasury's own yield curve (25bp band, "
      "stated in words).")
    A("- What the test showed: this bond passed; the 4.375% Feb 2038 (and 4.5% Feb 2036) prices were about 1 point "
      "of yield off, so the team treated them as stale. Use Friday's result if it differs.")
    A("- Aligned: \"Laura's 2027 deposit buys Treasuries maturing before each of her ten $50,000 payments\"; the "
      "stated cost of the payments assumes fair prices.")
    A("- Served Laura: funding reliability. The plan's cost of the payments rests on fair prices; the stale price was "
      "about 8 points per $100 above the curve price (99.98 against 92.18; wins.bond_check, MODEL), so it would have "
      "misstated what her deposit buys.")
    A("- The May 2038 bond is also the latest bond maturing before the 2039 payment (Treasury MSPD list), so "
      "skipping the stale one cost nothing.")
    A("- One number at most (either \"about 1 point of yield\" or \"about 8 points per $100\").")
    A("")
    A("**Pick 3, VT (supported).**")
    A("")
    A("- Why: after the ten payments and the floor, what is left (about 9% of the WInS portfolio, which shows her "
      "plan after both deposits, scaled down) goes into one global fund of thousands of companies, held to 2033.")
    A("- Aligned: IPS \"The rest, plus any 2027 remainder, forms the return-seeking portfolio ...\" and \"A market "
      "decline can reduce the facility contribution, but not below the floor.\"")
    A("- Served Laura: growth and flexibility for the facility, from money no artist or co-sponsor relies on.")
    A("- The tradeoff (\"why so little stock?\"): moving floor money into stocks raises the expected outcome modestly "
      "but widens the range, and the floor quoted in 2031 would no longer hold (IPS paragraph 4).")
    A("- Never: a return forecast, a probability, a 2031 or 2033 figure. One number at most.")
    A("")
    A("## 7. Triage (the strategy is unchanged; nothing here is applied to the IPS or the Sheet)")
    A("")
    A("| Finding | Class | Evidence |")
    A("|---|---|---|")
    A("| The IPS defines high certainty as each payment being \"matched by a dated Treasury ETF or bond\" and \"once "
      "bought it depends essentially on the US government\". Funds and coupon bonds are not matched (coupons must be "
      "reinvested). | fix-before-6-Nov (wording; the team decides) | IPS Google Doc, read 30 Sep; premortem PM-14, "
      "PM-23; `reinvest.bookL_delivered` (about $466,000 of $500,000 if coupons earn 2%, MODEL) |")
    A("| If the 1 Oct vote picks Book L, the IPS sentence \"Our WInS portfolio shows the allocation after both "
      "deposits, scaled down\" becomes false, and the TN Analysis cannot show the floor or the stock fund. | decide at "
      "the 1 Oct vote; fix-before-6-Nov if Book L | Sheet tab Book L header; s6 |")
    A("| No iBonds Treasury fund ends Dec 2037 to Dec 2043, so the 2038-2042 payments must use coupon bonds (the "
      "larger reinvestment exposure). | note-in-Final-Report | iShares product list, fetched 30 Sep "
      "(`data/ishares_ibonds_treasury_list_2026-09-30.csv`) |")
    A("| The Sheet's accrued interest for the 4.500% May 2038 bond (0.530; about 1.66 is right). | fix-before-6-Nov "
      "(Sheet input); keep it out of notes | `wins.bond_accrued_mismatch` |")
    A("| The M9 coupon-share figures (38% vs 17%) are not in numbers.yaml, so no note may quote them yet. | "
      "fix-before-6-Nov only if the team wants that number in a note (WS1 adds it at the Friday re-lock) | "
      "`M9_selection.md` |")
    A("")
    A("## 8. Checks run by build_notes.py")
    A("")
    A("| Note | Chars | Length | ASCII | 1 para | Banned | Role | Laura | One number at most | Numbers traced | "
      "Dollar scale |")
    A("|---|---|---|---|---|---|---|---|---|---|---|")
    for nid, cs in results.items():
        chars = next(x for x in NOTES + VARIANTS if x["id"] == nid)["exemplar"]
        A(f"| {nid} | {len(chars)} | " + " | ".join("pass" if c[1] else f"FAIL {c[2]}" for c in cs) + " |")
    A("")
    A("Superseded-book and stale-fact greps run over this file and `notes.csv` too (premortem Gate C items 4-5).")
    A("")
    A("## 9. Sources")
    A("")
    A("- Trading Note Instruction.pdf and Competition Guide.pdf p.3 (Drive folder Knox Wharton 2026; official 2026-27).")
    A("- IPS Google Doc 1qtEuzXq_QYdQ9VJlusPY9km2l80E1hkk8FPR0iw71-w, read 30 Sep 2026 (read-only).")
    A("- Sheet 1EHCJxbFI0UOzNOpOWvDfzNqbK45qWuopZcL7HNN3VPM tabs WInS Notes, Portfolio, Book L (snapshots in "
      "`rab/data/sheet/`, read 30 Sep 00:30-00:34 AEST).")
    A("- iShares product pages, 28 Sep (`rab/data/ishares/`): monthly distributions; \"terminate on or about ... "
      "December 15\"; \"does not seek to return any predetermined amount\".")
    A("- iShares product screener, fetched 30 Sep 2026 ~02:34 AEST: https://www.ishares.com/us/product-screener/"
      "product-screener-v3.1.jsn (extract in `data/ishares_ibonds_treasury_list_2026-09-30.csv`).")
    A("- `rab/numbers.yaml` (Gate A lock), `tickets.md`, `M9_selection.md`, `october_trade.md`, `rab/premortem.md`, "
      "insight_v1 `trading_notes_pack.md` (rules reused; its book is superseded), `D9_draft_checker.py` (ideas reused "
      "in `note_check.py`), Winning Team Portrait and Scoresheet.md.")
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


def main():
    Y, T, h = load_inputs()
    results, fails = {}, 0
    for n in NOTES + VARIANTS:
        cs = check_note(n)
        results[n["id"]] = cs
        fails += sum(1 for c in cs if not c[1])
    csv_path, md_path = os.path.join(HERE, "notes.csv"), os.path.join(HERE, "notes.md")
    rows = write_csv(csv_path, T, Y)
    write_md(md_path, T, Y, h, results)
    g = grep_outputs([csv_path, md_path])
    for nid, cs in results.items():
        bad = [f"{c[0]} ({c[2]})" for c in cs if not c[1]]
        print(f"{nid:7s} {len(next(x for x in NOTES + VARIANTS if x['id'] == nid)['exemplar']):4d} chars  "
              f"{'pass' if not bad else 'FAIL: ' + ', '.join(bad)}")
    print(f"notes.csv rows: {len(rows)}; superseded/stale grep hits: {g or 'none'}; numbers.yaml {h[:12]}")
    print(f"{fails + len(g)} fail")
    return 1 if fails or g else 0


if __name__ == "__main__":
    sys.exit(main())
