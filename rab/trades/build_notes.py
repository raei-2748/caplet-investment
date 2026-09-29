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
    "EQUITY": ("Equities should outperform Treasuries over five years but can fall sharply, so moving money from the "
               "floor into equities raises the expected outcome modestly but widens the range of results."),
}


# ----------------------------------------------------------------------------------------------- the notes
# Each spec: exemplar text; the numbers it uses (token -> source); brief fields. Per-book sizes come from tickets.csv.
# Payment order: 1 Jan 2033 is Laura's 1st payment ... 1 Jan 2042 her 10th (case: ten $50,000 payments 2033-2042).
# Revised 30 Sep after the judge panel (rab/trades/judge_response.md): picks rebuilt around a real test (IBTR) and a
# real refinement (the Nov-2040 bond), VT moved to order 11, T40 retired, exact names, floor gloss, varied openings.
NOTES = [
    dict(
        id="IBTR", ticker="IBTR", books={"Portfolio": 1, "BookL": 1}, use="Friday order 1 (both books)",
        rung="IBTR", job="payments", tn_role="tested", pick="Pick 1 (tested)",
        serves="Laura's 5th payment, $50,000 on 1 Jan 2037 (2027 deposit)",
        facts=["iShares iBonds Dec 2036 Term Treasury ETF: 4 Treasuries maturing in 2036; ends on or about "
               "15 Dec 2036; pays income monthly (iShares, 28 Sep)",
               "the test this note records: before the first order, `refresh_tickets.py` prints what Laura's ten "
               "payments cost on 1 Jan 2027 on the latest Treasury curve. The IPS claims it is under $300,000 (28 Sep: "
               "about $292,000, laura.ladder.cost_2027_strips). The claim fails if yields fall about a quarter of a "
               "percentage point before then (laura.ladder.breakeven_fall_bp_strips). The October check re-runs it on "
               "the 14 Oct close (october_trade.md trigger B); the reflection reports that result either way",
               "the IPS rule 'latest payments first' says which payments a short 2027 deposit leaves for the 2028 "
               "deposit: the earliest. A small fall leaves part of the first payment; a large one (2020-level yields) "
               "several. It is not the order of WInS trades",
               "thinnest fund: about $38m in assets (iShares, 28 Sep); place it after the first hour"],
        ips=["COST", "LATEST", "FALL"],
        number=("'about a quarter of a percentage point' (the fall in yields before 1 Jan 2027 that lifts the ten "
                "payments above $300,000)",
                "laura.ladder.breakeven_fall_bp_strips (26.2bp, MODEL, 28 Sep curve); after Friday's re-lock use its "
                "new quote_as. $50,000 and $300,000 are case facts"),
        dont=["that the fund pays a set $50,000",
              "'any gap falls on her first payment' (a large fall leaves several of the earliest payments; the IPS "
              "says 'some payments')",
              "'thin' or 'risky' as a description of the holding", "any WInS dollar amount as if it were Laura's",
              "'we buy the latest payments first' (that is the IPS funding rule, not the WInS trade order)"],
        friday=("Friday fact: the refresh line 'ten payments cost $X on 1 Jan 2027'. Write it in the Trade Log. If X is "
                "above $300,000 the note's result is wrong: stop and tell Ray. Use the WInS name string for IBTR if it "
                "differs from the issuer's. If IBTR cannot be bought, the order becomes IBTQ and this note changes."),
        exemplar=("Future funding: the iShares iBonds Dec 2036 Term Treasury ETF ends before Laura's 2037 payment. We "
                  "first re-priced her ten $50,000 payments: under her $300,000 deposit at latest yields. A fall of "
                  "about a quarter of a percentage point by 2027 leaves the earliest to her 2028 deposit."),
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
        dont=["that no Treasury matures in those years at all (notes do; WInS just does not list them)",
              "that the fund repays or delivers a set $50,000"],
        friday="Friday fact: the WInS name string for IBTQ, copied exactly; re-read the drop-down for the gap.",
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
               "fair-price test, 28 Sep: the fund's price was 0.06% above the value of the Treasuries it holds (NAV "
               "$24.09, close $24.10; wins.ibond_checks.IBTP.premium_to_nav_pct). That premium, not the fund's yield, "
               "is the test of a fair ETF price: a fund holding only Treasuries always yields about the Treasury curve"],
        ips=["PITCH"],
        number=("none in the exemplar: 'almost exactly the value of the Treasuries it holds' is the 28 Sep premium "
                "in words. A figure such as 'within 0.1%' needs a quote_as that WS1 adds at the Friday re-lock",
                "wins.ibond_checks.IBTP.premium_to_nav_pct = 0.06 (numbers.yaml has no quote_as for it yet)"),
        dont=["'bp'", "that the yield is locked in for Laura",
              "'its yield was close to the Treasury curve, so the price was fair' (a Treasury fund's yield always is)"],
        friday=("Friday fact: re-run the premium test (the iShares IBTP page shows Thursday's NAV; compare it with the "
                "price WInS shows) and use that date, or keep 'On 28 Sep'. Copy the WInS name string for IBTP."),
        exemplar=("The iShares iBonds Dec 2034 Term Treasury ETF is future funding for Laura's $50,000 residency "
                  "payment on 1 Jan 2035: it holds Treasuries maturing in 2034. Our check on 28 Sep found its price "
                  "almost exactly the value of those Treasuries, so her money buys them at a fair price."),
        nums={},
    ),
    dict(
        id="IBTO", ticker="IBTO", books={"Portfolio": 4, "BookL": 4}, use="Friday order 4 (both books)",
        rung="IBTO", job="payments", tn_role="supported",
        serves="Laura's 2nd payment, $50,000 on 1 Jan 2034 (2027 deposit)",
        facts=["iShares iBonds Dec 2033 Term Treasury ETF: 11 Treasuries; ends on or about 15 Dec 2033; monthly "
               "income (iShares, 28 Sep)",
               "trap: in WInS, IBTN is INSCORP Inc (SEEN 29 Sep); iShares has no fund with the ticker IBTN "
               "(iShares product list, 30 Sep). The name check belongs in the Trade Log and in the Final Report's "
               "account of the team's experience, not in the note (judge panel, 30 Sep)"],
        ips=["PITCH"],
        number=("none needed", "-"),
        dont=["anything about IBTN in the note (record the check in the Trade Log)",
              "anything unkind about the other company"],
        friday=("Type IBTO and IBTN once each; copy both names exactly as WInS shows them into the Trade Log. Friday "
                "fact: the WInS name string for IBTO."),
        exemplar=("Role: future funding. The iShares iBonds Dec 2033 Term Treasury ETF is for the second of Laura's ten "
                  "$50,000 payments, on 1 Jan 2034. WInS lists no Treasury bond maturing in 2033, so we use a fund of "
                  "Treasuries maturing that year, which then closes. Its reinvested income can vary."),
        nums={},
    ),
    dict(
        id="IBTM_P", ticker="IBTM", books={"Portfolio": 5}, use="Friday order 5 (Portfolio book)",
        rung="IBTM", job="payments + floor", tn_role="supported", pick="Alternate A (supported)",
        serves=("two jobs: Laura's 1st payment, $50,000 on 1 Jan 2033 (2027 deposit), and the facility floor, the least "
                "she plans to give the facility (2028 deposit)"),
        facts=["iShares iBonds Dec 2032 Term Treasury ETF (SEEN in WInS 29 Sep): 15 Treasuries; ends on or about "
               "15 Dec 2032; monthly income (iShares, 28 Sep)",
               "WInS lists no Treasury maturing in late 2032 (SEEN 29 Sep), so in WInS the IPS floor ('Treasuries "
               "maturing in late 2032') is held in this fund, together with the 2033 payment. In Laura's real account "
               "the floor can sit in Treasury notes maturing in late 2032, e.g. 4.125% 15 Nov 2032 (91282CFV8) or "
               "3.75% 30 Nov 2032 (91282CPM7) (MSPD Table V, 31 Aug 2026, `data/mspd_table5_2026-08-31.json`)",
               "iShares says its iBonds funds \"do not seek to return any predetermined amount\" (IBTM product page, "
               "28 Sep 2026)",
               "the limit, measured: if its income is reinvested at only 2%, IBTM delivers about 97% of the curve case, "
               "the least exposure of any rung (reinvest.rung.IBTM at_2pct 48,192 / at_curve 49,856; M9). Its quote_as "
               "says appendix only: quote it only after WS1 adds a quote_as",
               "Portfolio tab: 32.5% of the book, of which 24.3 points are the floor",
               "Laura's plan: the floor costs about $117,000 of her 2028 deposit at the 28 Sep 5-year yield "
               "(laura.floor_cost_2028, MODEL; never in a note)"],
        ips=["FLOOR", "PITCH"],
        number=("none in the exemplar ('about a third of our WInS portfolio' is available)",
                "wins.portfolio.holdings_close_0928 IBTM weight 0.3254 (WInS book)"),
        dont=["that it 'repays' or 'holds' a dollar floor (never '$150,000' next to this holding: PM-15)",
              "any 2031 dollar figure: range, top or co-sponsor amount (TN guide: not expected yet); the idea of the "
              "2031 range is welcome",
              "that the floor or the payment is a fixed amount (the fund's end value is not fixed)",
              "'facility floor' without its gloss (the TN Analysis is read before the IPS)"],
        friday=("Re-read the WInS bond list for a late-2032 Treasury (if one appears, tell Ray before trading). Friday "
                "fact: the Preview price, dated, if the team wants it as the note's one number."),
        exemplar=("Future funding and risk management: the iShares iBonds Dec 2032 Term Treasury ETF holds 2032 "
                  "Treasuries. In Laura's plan it covers her first $50,000 payment, then the facility floor (the least "
                  "she plans to give) that she can name to co-sponsors in 2031. What its income earns can vary."),
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
        dont=["the floor (Book L does not hold it)", "'repays $50,000'"],
        friday="As for the Portfolio book.",
        exemplar=("Role: future funding. The iShares iBonds Dec 2032 Term Treasury ETF ends before the first of Laura's "
                  "ten $50,000 residency payments, on 1 Jan 2033. WInS lists no Treasury bond maturing in late 2032, "
                  "so this dated fund is the closest fit, with its income reinvested."),
        nums={},
    ),
    dict(
        id="T41", ticker="T 3.125% 15-Nov-2041", books={"Portfolio": 6, "BookL": 6},
        use="Friday order 6, first bond (both books)", rung="T_3.125%_15-Nov-2041", job="payments",
        tn_role="supported",
        serves="Laura's 10th and last payment, $50,000 on 1 Jan 2042 (2027 deposit)",
        facts=["U.S. Treasury bond 3.125% due 15 Nov 2041, CUSIP 912810QT8; matures 47 days before the payment; "
               "coupons twice a year",
               "no iBonds Treasury fund ends between Dec 2037 and Dec 2043 (iShares product list, 30 Sep), so the "
               "2038-2042 payments use individual bonds",
               "WInS price 76.367 (28 Sep) is 1.9bp from the curve: passes"],
        ips=["PITCH"],
        number=("none needed", "-"),
        dont=["that the bond delivers a fixed $50,000 including coupons"],
        friday=("Price inside the 25bp band; if the team swaps to the 2.000% Nov-2041, use SW41. Friday fact: 'its "
                "price passed our curve check' fits if the team trims a clause."),
        exemplar=("Role: future funding. The 3.125% Treasury bond maturing 15 Nov 2041 is for the last of Laura's ten "
                  "$50,000 payments, on 1 Jan 2042. No iBonds Treasury fund ends between 2037 and 2043, so her last "
                  "five payments use single bonds, each with a set amount due at maturity."),
        nums={},
    ),
    dict(
        id="T40b", ticker="T 4.250% 15-Nov-2040", books={"Portfolio": 7, "BookL": 7},
        use="Friday order 7 (both books), default: WInS does not list the 1.375% Nov-2040",
        rung="T_4.250%_15-Nov-2040", job="payments", tn_role="refined", pick="Pick 2 (refined), if typed",
        serves="Laura's 9th payment, $50,000 on 1 Jan 2041 (2027 deposit)",
        facts=["U.S. Treasury bond 4.250% due 15 Nov 2040, CUSIP 912810QL5; WInS price 89.186 (28 Sep) is 5.1bp "
               "from the curve: passes",
               "same-date alternate 1.375% 15 Nov 2040 (912810ST6): it exists (MSPD Table V, 31 Aug 2026); its WInS "
               "listing is UNVERIFIED until the Friday drop-down read. About 38% of the 4.250% bond's cash before 2041 "
               "comes as coupons, against 17% (M9, MODEL; not in numbers.yaml)",
               "which note: T40b if WInS does not list the 1.375%; SW40 if it is listed, passes and the 1 Oct vote "
               "swaps; T40c if it is listed but kept for October (trigger D). T40 ('we are checking') is retired"],
        ips=["PITCH"],
        number=("none from numbers.yaml; the M9 coupon shares (38% vs 17%) need a numbers.yaml entry before any "
                "note uses them", "M9_selection.md (MODEL)"),
        dont=["'we are checking' (the drop-down read settles it before the order)", "that a swap will happen"],
        friday="Read the drop-down first. Not listed: this note. Listed and swapped: SW40. Listed, kept for October: T40c.",
        exemplar=("Future funding: the 4.250% Treasury bond maturing 15 Nov 2040 is for the ninth of Laura's ten "
                  "$50,000 payments, on 1 Jan 2041. A lower-coupon bond of that date would leave less income to "
                  "reinvest, but WInS does not list one, so we use this. Its WInS price passed our curve check."),
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
               "the certainty alternate: the one note that says why price swings do not change what Laura is owed",
               "trap: WInS also lists a 4.375% bond of 15 Feb 2038, with a stale price; pick by coupon AND date"],
        ips=["HELD"],
        number=("none needed ('about seven weeks' is date arithmetic)", "15 Nov 2039 to 1 Jan 2040 = 47 days"),
        dont=["that its price cannot fall (it can; only the amount due at maturity is set)",
              "'we hold it to maturity' about WInS (the WInS book freezes on 6 Nov; holding to maturity is Laura's plan)",
              "'only' before the unknowns (reinvested coupons and the money waiting seven weeks both earn unknown rates)"],
        friday="Price inside the 25bp band. Friday fact: 'its WInS price passed our curve check', if the team trims.",
        exemplar=("Future funding: the 4.375% Treasury bond maturing 15 Nov 2039 ends about seven weeks before Laura's "
                  "$50,000 residency payment on 1 Jan 2040. Its price will move until then, but her plan holds it to "
                  "maturity, when the U.S. government owes a set amount; what its coupons earn can vary."),
        nums={},
    ),
    dict(
        id="T38", ticker="T 4.500% 15-May-2038", books={"Portfolio": 9, "BookL": 9},
        use="Friday order 9 (both books)", rung="T_4.500%_15-May-2038", job="payments", tn_role="supported",
        pick="Alternate C (supported, with a price check)",
        serves="Laura's 7th payment, $50,000 on 1 Jan 2039 (2027 deposit)",
        facts=["U.S. Treasury bond 4.500% due 15 May 2038, CUSIP 912810PX0: the latest Treasury bond maturing before the "
               "payment (MSPD Table V, M9; ends about 7.6 months early)",
               "price check, 28 Sep prices: this bond 14.4bp from the curve (passes); the 4.375% Feb 2038 bond at "
               "99.98 was 92bp off and the 4.5% Feb 2036 at 102.95 was 111bp off (both stale). The Feb 2038 bond was "
               "only the runner-up and ends earlier, so the check did not change the choice: it is a data check",
               "why a 25bp band: the five good prices sat 2 to 15 hundredths of a point of yield from the curve and "
               "the stale ones 92 and 111 hundredths (wins.bond_check.*), so a quarter point separates them cleanly",
               "the Sheet records this bond's accrued interest as 0.530; 1.66 is right on 28 Sep (1.71 on 2 Oct): fix "
               "before 6 Nov"],
        ips=["PITCH", "COST"],
        number=("'almost a full percentage point of yield' (the stale Feb 2038 price, 29 Sep)",
                "wins.bond_check.T_4.375%_15-Feb-2038 gap_bp -92.1 (MODEL). Its quote_as says 'about 1 point of "
                "yield'; bond prices are quoted in points, so notes say 'percentage point of yield'; WS1 to align the "
                "quote_as at the re-lock"),
        dont=["that WInS is 'wrong' or 'broken' (say 'stale')", "'bp'", "'1 point of yield' (reads as a price point)",
              "the Sheet's accrued-interest typo"],
        friday=("Re-check both prices on Friday. If the Feb 2038 price now passes, keep the date on the stale reading "
                "('On 29 Sep ...', as the exemplar does) or say what Friday's check showed."),
        exemplar=("Role: future funding. The 4.500% Treasury bond maturing 15 May 2038 is the last before Laura's "
                  "$50,000 residency payment on 1 Jan 2039. Its WInS price passed our curve check. On 29 Sep the Feb "
                  "2038 bond was almost a full percentage point of yield off, so we treated it as stale."),
        nums={},
    ),
    dict(
        id="T37", ticker="T 4.750% 15-Feb-2037", books={"Portfolio": 10, "BookL": 10},
        use="Friday order 10, last bond (both books)", rung="T_4.750%_15-Feb-2037", job="payments",
        tn_role="supported",
        serves="Laura's 6th payment, $50,000 on 1 Jan 2038 (2027 deposit)",
        facts=["U.S. Treasury bond 4.750% due 15 Feb 2037, CUSIP 912810PT9; matures about 10.5 months (320 days) before "
               "the payment, so its money waits",
               "WInS price 97.152 (28 Sep) is 15.3bp from the curve: passes",
               "the only later bond of this class before the payment is the 5.000% 15 May 2037 (912810PU6; MSPD Table "
               "V). Its WInS listing is UNVERIFIED; it comes out about the same once coupons are counted (90.5% each "
               "at 2%, M9, MODEL)"],
        ips=["PITCH", "HELD"],
        number=("'about ten and a half months early' (date arithmetic)", "15 Feb 2037 to 1 Jan 2038 = 320 days"),
        dont=["that the waiting money earns interest in WInS (WInS cash earns 0%)", "'about ten months' (it is 10.5)"],
        friday=("Read the drop-down: if WInS shows no 5.000% May 2037 bond, replace the last sentence with 'It is the "
                "last WInS bond maturing before 2038.' Price inside the 25bp band; the last bond order."),
        exemplar=("For future funding, the 4.750% Treasury bond maturing 15 Feb 2037 is for Laura's $50,000 payment on "
                  "1 Jan 2038. It matures about ten and a half months early and the money waits. The only later bond "
                  "before 2038, the 5.000% May 2037, comes out about the same once coupons count."),
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
               "why so little stock: the ten payments use almost all of Laura's first deposit (about $292,000 of "
               "$300,000 on 1 Jan 2027, laura.ladder.cost_2027_strips)",
               "Laura's tolerance: 'willing to take thoughtful risks' (Client Profile p.2); the IPS rates it above "
               "average for facility money above the floor",
               "IPS range: from the floor to the floor plus half the fund's value in 2031; the other half stays with "
               "Laura as a cushion; the 2033 contribution is capped at the announced top",
               "Portfolio tab: 8.7% of the book; in Laura's plan about $41,000 on 2 Jan 2028 (MODEL; never in a note)"],
        ips=["BRANCH", "DECLINE", "FIRST"],
        number=("'about 9% of our WInS portfolio'", "wins.portfolio.split_close_0928 vt 0.0868 (WInS book)"),
        dont=["a return forecast (the IPS's 'should outperform' belongs in the IPS, not a note)",
              "probabilities, CAPE or valuation calls", "'Laura likes risk'", "any 2031 or 2033 dollar figure",
              "'bought last' if VT was placed before the bonds by mistake"],
        friday=("Mon 5 Oct: VT's share after `--cash-before-vt` (still 'about 9%' unless it moves by a point). Friday "
                "fact: the Preview price, dated, could replace the 9% as the one number."),
        exemplar=("Growth: bought last, the Vanguard Total World Stock ETF gets what was left after Laura's payments and "
                  "facility floor (the least she plans to give): about 9% of our WInS portfolio. A fall cuts only her "
                  "contribution above the floor; a rise lifts the top of the range co-sponsors hear."),
        nums={"9%": "wins.portfolio.split_close_0928 (vt 0.0868)"},
    ),
]

# Variants and conditional notes (not Friday tickets unless the team decides so).
VARIANTS = [
    dict(
        id="T40c", ticker="T 4.250% 15-Nov-2040",
        use="Friday order 7, if WInS lists the 1.375% Nov-2040 but the team keeps the swap for October",
        tn_role="refined", pick="Pick 2 (refined), if typed", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"],
        brief=("Same bond as T40b. Says exactly where the decision stands when the order is placed: the better bond is "
               "listed, the switch waits for the IPS wording on coupons (october_trade.md trigger D)."),
        exemplar=("Role: future funding. The 4.250% Treasury bond maturing 15 Nov 2040 is for the ninth of Laura's ten "
                  "$50,000 payments. WInS also lists a 1.375% bond of that date, which leaves less income to reinvest; "
                  "we plan to review a switch in October, once our policy wording on coupons is agreed."),
        nums={},
    ),
    dict(
        id="SW40", ticker="T 1.375% 15-Nov-2040", use="Friday --swap, only if listed, passing, and voted on 1 Oct",
        tn_role="refined", pick="Pick 2 (refined), if typed", serves="Laura's 9th payment (1 Jan 2041)", ips=["PITCH"],
        brief=("Replaces T40b on Friday. CUSIP 912810ST6. Accept a WInS clean price only between 58.474 and 62.116 "
               "(25bp band, tickets.md). 'About the same cost on today's curve' is M9 (MODEL: $23,266 against "
               "$23,146 for the 2041 payment at forward rates); WS1 adds a numbers.yaml entry before any reflection "
               "quotes a figure. The IPS must also gain a sentence on reinvested coupons."),
        exemplar=("Future funding: the 1.375% Treasury bond maturing 15 Nov 2040 is for the ninth of Laura's ten $50,000 "
                  "payments. We chose it over the 4.250% bond of that date: its low coupon leaves less income to "
                  "reinvest, at about the same cost on today's curve. Its WInS price passed our curve check."),
        nums={},
    ),
    dict(
        id="SW41", ticker="T 2.000% 15-Nov-2041", use="Friday --swap, only if listed, passing, and voted on 1 Oct",
        tn_role="refined", serves="Laura's 10th payment (1 Jan 2042)", ips=["PITCH"],
        brief=("Replaces T41 on Friday. CUSIP 912810TC2. Accept a WInS clean price only between 62.639 and 66.568 "
               "(25bp band, tickets.md)."),
        exemplar=("Role: future funding. The 2.000% Treasury bond maturing 15 Nov 2041 is for the last of Laura's ten "
                  "$50,000 payments, on 1 Jan 2042. We chose it over the 3.125% bond of the same date: a lower coupon "
                  "means less income to reinvest before the payment. Its price passed our curve check."),
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
        tn_role="refined", pick="Pick 2 (refined), if trigger D fills", serves="Laura's 9th payment (1 Jan 2041)",
        ips=["PITCH"],
        brief=("Face value from refresh_tickets.py --swap on the day; WInS price inside the 25bp band the refresh "
               "prints (28 Sep band: 58.474 to 62.116). Replaces the Friday Nov-2040 note as the 'refined' pick if it "
               "fills with a saved note by 20 Oct ET. 'About the same cost' is M9 (MODEL), as for SW40."),
        exemplar=("Future funding: we are buying the 1.375% Treasury bond maturing 15 Nov 2040 for Laura's ninth "
                  "payment, in place of the 4.250% bond we sold. More of its value comes at maturity, so less rides on "
                  "reinvested coupons, at about the same cost today. Its price passed our curve check."),
        nums={},
    ),
    dict(
        id="OB_S", ticker="VT", use="October trigger B: sell part of VT (rates-fall test)",
        tn_role="tested", pick="Pick 1 (tested), if trigger B fills", serves="the floor and the 2033 payment, before growth",
        ips=["FALL"],
        brief=("Fires only if the refresh on the 14 Oct close says the ten payments cost more than $300,000 on "
               "1 Jan 2027 (today about $292,000, laura.ladder.cost_2027_strips). Size from the refresh; only if at "
               "least $2,500. WS1 adds the new cost to numbers.yaml before any note quotes it. Unchanged after the "
               "judge panel (two of the three judges scored it 3 of 3): rule, consequence for Laura, tradeoff. In a "
               "two-week move the gap stays inside the first payment; if the refresh ever shows more, write 'the "
               "earliest payments'."),
        exemplar=("Role: future funding. Yields have fallen, so in our model the ten payments now cost more than "
                  "Laura's $300,000 first deposit and her 2028 deposit must finish the 2033 payment. Less is left for "
                  "stocks, so we are moving part of this world stock fund into the 2032 Treasury fund."),
        nums={},
    ),
    dict(
        id="OB_B", ticker="IBTM", use="October trigger B: buy IBTM with the VT proceeds",
        tn_role="tested", serves="Laura's 1st payment and the floor", ips=["FALL", "LATEST"],
        brief="The buy leg of trigger B; OB_S is the stronger note to feature.",
        exemplar=("Role: future funding. We are adding to the iShares iBonds Dec 2032 Term Treasury ETF with money from "
                  "the stock fund. After yields fell, Laura's 2028 deposit must complete her 2033 payment, as our plan "
                  "allows, so the payments come first. Its income is reinvested too."),
        nums={},
    ),
    dict(
        id="OC", ticker="VT", use="October trigger C: spare cash above $6,300 into VT",
        tn_role="supported", serves="growth for the facility contribution", ips=["BRANCH"],
        brief="Buy VT with everything above the $3,300 float (october_trade.md). The reason is Laura's plan, not WInS.",
        exemplar=("Role: growth. Our cash is more than fees and rounding need, so the extra goes to the Vanguard Total "
                  "World Stock ETF: in Laura's plan, money left after her payments and floor joins the stock fund "
                  "held to 2033. Her dated Treasury holdings stay as they are."),
        nums={},
    ),
]
# Notes that may be featured in the Trading Notes Analysis: they must also name the residency, co-sponsors or which
# of her ten payments (judge panel, 30 Sep: a year alone could fit any client).
PICK_IDS = {"IBTR", "T40b", "T40c", "SW40", "OD_B", "VT", "IBTM_P", "T39", "T38"}

# ----------------------------------------------------------------------------------------------- reflection outlines
# Bullets for the Trading Notes Analysis reflections (TN guide: why / how it aligned / how it served the client).
# Each outline is 70 words or fewer (checked in main), leaving room in the 100-word reflection for the scale sentence
# (SCALE, 15 words) and for what was checked or changed after Friday. Students write the prose; these are prompts.
SCALE = "Our WInS portfolio is Laura's plan after both deposits, scaled down to $300,000."
SCALE_L = "Our WInS portfolio is Laura's 2027 deposit; the floor and stock fund come in 2028."
CERTAINTY = ("a high degree of certainty, meaning U.S. Treasuries dated before each payment and held to maturity; "
             "what reinvested income and waiting money earn can vary")
OUTLINES = [
    ("Pick 1, IBTR (tested)", [
        "Why: before the first order we re-priced the ten payments on the latest curve, testing the IPS claim that "
        "they cost under $300,000.",
        "Tested: report Friday's figure; it fails after a fall of about a quarter of a percentage point. Say what the "
        "14 Oct re-check showed.",
        "Aligned: any shortfall falls on the earliest payments, for the 2028 deposit.",
        "Served Laura: the certainty phrase, once, with its condition.",
    ]),
    ("Pick 2, the Nov 2040 bond (refined: SW40, T40b or T40c; OD_B if trigger D fills)", [
        "Why: pricing each rung showed coupons arrive early and are reinvested at unknown rates; a low-coupon bond of "
        "the same date leaves less to chance.",
        "Refined: name the change: the swap, or, if WInS lacks the bond, an IPS that no longer says \"needs no "
        "rebalancing\".",
        "Served Laura: her ninth payment rests less on future rates, at about the same cost.",
        "Use only once the team agrees that wording.",
    ]),
    ("Pick 3, VT (supported)", [
        "Why: her payments take almost all her first deposit; after them and the floor (the least she plans to "
        "give), about 9% of our WInS portfolio remained.",
        "Aligned: bought last; a fall cannot cut her contribution below the floor.",
        "Served Laura: thoughtful risk only above the floor; a rise lifts the range's top; half stays hers.",
        "Tradeoff: more stock widens the range and shrinks the floor co-sponsors hear in 2031.",
    ]),
]
ALT_OUTLINES = [
    ("Alternate A, IBTM (supported)", [
        "Why: one fund holds her first payment and the floor (the least she plans to give); WInS lists no late-2032 "
        "Treasury, though her real account can hold one.",
        "Limit: iShares says its iBonds funds \"do not seek to return any predetermined amount\", so the floor she "
        "names in 2031 counts only what its Treasuries pay.",
        "If kept as refined, name that change.",
    ]),
    ("Alternate B, 4.375% Nov 2039 bond (supported: certainty)", [
        "Why: its price moves, but her plan holds it to maturity, when the U.S. government owes a set amount, about "
        "seven weeks before her 2040 payment.",
        "Served Laura: the plainest case of the certainty phrase.",
    ]),
    ("Alternate C, 4.500% May 2038 bond (supported, with a price check)", [
        "Why: every WInS bond price was checked against the latest official curve; good prices sat within about 0.15 of a "
        "percentage point, stale ones almost a full percentage point off.",
        "Aligned: the check tests the IPS cost claim at the prices actually paid.",
    ]),
]
MAX_OUTLINE_WORDS = 70




def outline_words(bullets):
    return len(" ".join(bullets).split())


def check_note(n):
    """Every check in note_rules.check_text must pass for an exemplar (FAIL and WARN alike); a note that may be
    featured must also pass the pick anchor (residency, co-sponsors or which of her ten payments)."""
    out = [(name, ok, detail) for name, ok, detail, _sev in check_text(n["exemplar"], list(n.get("nums", {})))]
    if n["id"] in PICK_IDS:
        ok, detail = pick_anchor(n["exemplar"])
        out.append(("pick anchor", ok, detail))
    else:
        out.append(("pick anchor", True, "n/a"))
    return out


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
               "do not seek to return any predetermined amount"}   # numbers.yaml quote_as strings; iShares text
    quoted = list(IPS.values())
    for _, bullets in OUTLINES + ALT_OUTLINES:
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
                             ips_quote=" / ".join(IPS[k] for k in n["ips"])))
    for v in VARIANTS:
        brief = (f"Serves: {v['serves']}. {v['brief']} IPS: " +
                 " / ".join(f"\"{IPS[k]}\"" for k in v["ips"]))
        rows.append(dict(ticker=v["ticker"], brief=brief, exemplar=v["exemplar"], char_count=len(v["exemplar"]),
                         book="conditional", seq="", note_id=v["id"], use=v["use"], label=LABEL,
                         numbers="; ".join(f"{k} = {x}" for k, x in v.get("nums", {}).items()),
                         role=role_of(v["exemplar"]), tn_role=v["tn_role"], pick=v.get("pick", ""),
                         ips_quote=" / ".join(IPS[k] for k in v["ips"])))
    order = {"Portfolio": 0, "BookL": 1, "conditional": 2}
    rows.sort(key=lambda r: (order[r["book"]], int(r["seq"]) if r["seq"] != "" else 99))
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ticker", "brief", "exemplar", "char_count", "book", "seq", "note_id",
                                          "use", "label", "numbers", "role", "tn_role", "pick", "ips_quote"])
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
    ok = all(c[1] for c in checks)
    L += ["", f"> **{LABEL}** ({len(n['exemplar'])} characters; checks {'pass' if ok else 'FAIL'})", ">",
          f"> {n['exemplar']}", ""]
    return L




def write_md(path, T, Y, h, results, boiler):
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
      "2026 curve and closes, WInS prices seen 29 Sep. Revised after the judge panel of 30 Sep; every point and the "
      "answer to it is in `judge_response.md`. Nothing here changes the strategy.")
    A("")
    A("**Bottom line.**")
    A("")
    longest = max(len(x["exemplar"]) for x in NOTES + VARIANTS)
    A("- Every Friday ticket (both books) has a brief and an exemplar; so do the Friday swap variants and each "
      f"October trigger. All exemplars are {longest} characters or fewer, plain ASCII, one paragraph, and pass the "
      "banned-word, number, Laura and variety checks (s8).")
    A("- **Feature these three** (Portfolio book): **IBTR** (tested: before the first order the team re-prices the "
      "ten payments against Laura's $300,000 deposit, the IPS claim that fails after a fall in yields of about a "
      "quarter of a percentage point; the 14 Oct check runs it again), **the Nov 2040 bond note that is typed** "
      "(refined: coupons arrive early and must be reinvested, so the team chose, or looked for, the low-coupon bond "
      "of the same date and changes the IPS wording), and **VT** (supported: bought last, with only the money above "
      "the payments and the floor). Certainty, then a refinement, then growth. Alternates: IBTM (the floor), the "
      "Nov 2039 bond (certainty), the May 2038 bond (price check).")
    A(f"- **VT is now order 11**, placed in the session after the bonds fill ({vt_time}), so WInS Order History shows "
      "the payments and the floor bought before any stocks, as the IPS says (`tickets.md`, `friday_checklist.md`).")
    A(f"- **Every reflection says once:** \"{SCALE}\" Without it, a judge who sees a $21,000 holding next to "
      "\"Laura's $50,000 payment\" will think the numbers are wrong.")
    A("- **Book L** would leave the analysis with payments only: the floor and the stock fund never appear in WInS. "
      "That is a Laura-lens reason for the Portfolio book at the 1 Oct vote, not a change to the plan (s6).")
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
    A("- **One Friday fact:** each note carries one thing only WInS showed that day: the exact WInS name string, that "
      "its price passed the check, or the Preview price as the note's one number (dated). No exemplar can contain it, "
      "so no note is a copy.")
    A("- **Numbers:** at most one analytic number, from `numbers.yaml` or a named, dated source; a number written in "
      "words counts too. Dollar figures only as Laura's case facts ($50,000 payments, $300,000 first deposit) or "
      "\"in Laura's plan\"; WInS amounts as percentages. Never a WInS gain, loss or ranking.")
    A("- **Coupon caveat, short and varied:** two to five words (\"what its income earns can vary\", \"a set amount "
      "due at maturity\"), never the same tail on every note (premortem PM-23). A bond's amount due at maturity is "
      "set; the total with reinvested coupons is not. An iBonds fund's end value is never fixed. Only the refined "
      "pick spells the issue out.")
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
    A("- \"I bond\" (a U.S. savings bond); write \"iBonds\" or the fund's full name. Never \"repays $X\" for an iBonds fund.")
    A("- Forecasts and results: will grow / will outperform, CAPE, overvalued, profit, gain, rank.")
    A("- \"Laura's portfolio\" for the WInS book; the operating reserve's size; **any 2031 dollar figure** (the range, "
      "its top or a co-sponsor amount; the TN guide says these are not expected yet); Laura quotes; her degree, "
      "heritage or Taiwan as a reason. **The ideas are encouraged:** the floor, co-sponsors, the 2031 range, the "
      "residency, her operating payments.")
    A("- Jargon without a gloss: bp, basis points, duration, immunization. Say \"percentage point of yield\", not "
      "\"point of yield\" (bond prices are quoted in points).")
    A("")
    A("## 3. How the team uses this (Thu 1 Oct to Mon 5 Oct)")
    A("")
    A("1. Each note has a named student writer (Friday runbook roles). The writer drafts **from the brief, with the "
      "exemplar closed**, then compares, and adds the Friday fact.")
    A("2. Run the checker on the draft: `/Users/ray/Research/rab-ws/.venv/bin/python rab/trades/note_check.py --ticker "
      "IBTM --text \"...\"` (add `--pick` for a note that may be featured). It counts characters, checks ASCII, banned "
      "words and the Laura anchor, and measures **phrase overlap with the exemplar** (share of the draft's three-word "
      "phrases found in it). 50% or more: rewrite (FAIL). 25-49%: not a pass; rewrite, or disclose the exemplar in "
      "Works Cited (PM-13).")
    A("3. Note keeper holds the final texts, pastes each at Preview, reads it aloud once.")
    A("4. After saving: Order History > Add/View Notes, copy the note back into the Trade Log and compare it with the "
      "plan character for character (the box cuts silently at 300).")
    A("5. Log in `docs/AI_USE.md` which exemplars were read and whether any wording was kept.")
    A("")
    A("## 4. Friday notes, Portfolio book (Book L differences inline)")
    A("")
    A("Order: iBonds funds (1-5), then the bonds (6-10), both on Friday; **VT (11) in the next session**, once the "
      "bonds show Filled (`tickets.md`). Book L is orders 1-10; only IBTM's note differs. For the Nov-2040 bond "
      "(order 7) the drop-down decides the note: **T40b** if WInS does not list the 1.375% Nov-2040, **SW40** if it "
      "is listed and swapped, **T40c** if it is listed but kept for October. Sizes are the Gate A tickets; Friday's "
      "refresh re-sizes them. WInS names of IBTO-IBTR and every bond string are UNVERIFIED until read on Friday.")
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
    A("| 1 | IBTR, Friday #1 (IBTR) | **tested** | payments (certainty) | A test that could have failed, run before "
      "the first order: the IPS claim that the ten payments cost less than Laura's $300,000 deposit, re-priced on the "
      "latest curve. It fails after a fall in yields of about a quarter of a percentage point, and the plan already "
      "says what happens then (the earliest payments go to the 2028 deposit; October trigger B). The 14 Oct check "
      "re-runs it, so the reflection reports a second result either way. |")
    A("| 2 | The Nov 2040 bond, Friday #7: **SW40** if swapped, **T40b** if WInS lists no 1.375% bond, **T40c** if "
      "it is listed and kept for October; **OD_B** if trigger D fills | **refined** | payments (reinvestment) | A real "
      "discovery with its reason: pricing each rung showed coupons arrive early and must be reinvested at unknown "
      "rates, so a low-coupon bond of the same date is better at about the same cost. What changed: the bond (SW40, "
      "OD_B), or the IPS wording on coupons (all cases). Use it only once the team has agreed that wording. |")
    A("| 3 | VT, order 11 (VT) | **supported** | growth | Bought last, with only the money left after the payments "
      "and the floor, so Order History matches the note and the IPS. It answers \"why so little stock?\" (the "
      "payments use almost all of her first deposit) and says who carries the risk (only the contribution above the "
      "floor). |")
    A("")
    A("**Alternates (keep all three ready):** (A) **IBTM, Friday #5** (supported: one fund holds her first payment "
      "and the floor; if the team insists on 'refined', the reflection must name what changed); (B) **the 4.375% Nov "
      "2039 bond, Friday #8** (supported: the plainest statement of certainty); (C) **the 4.500% May 2038 bond, "
      "Friday #9** (supported, with the price check; it tested WInS data, not the strategy, so it is no longer a pick).")
    A("")
    A(f"**If an October trade fills with a saved note by {oct_close}:**")
    A("")
    A("- **Trigger D (coupon swap):** feature the **buy leg (OD_B)** as pick 2 (refined) in place of the Friday Nov "
      "2040 note.")
    A("- **Trigger B (rates fall):** feature **OB_S** (the VT sale) as pick 1 (tested) in place of IBTR; two of the "
      "three judges scored it 3 of 3, the top mark (rule, consequence for Laura, tradeoff). IBTR becomes an alternate.")
    A("- **Trigger C or none:** keep the three above; the IBTR reflection says \"checked 14 Oct: the rule said hold\". "
      "Never add a trade to create a pick.")
    A("")
    A(f"**If the 1 Oct vote picks Book L:** feature IBTR (tested), the Nov 2040 bond note (refined) and the Nov 2039 "
      f"bond (supported: certainty); alternates IBTM_L and the May 2038 bond. All three are payments: each reflection "
      f"uses \"{SCALE_L}\" in place of the scale sentence.")
    A("")
    A("### Reflection outlines (bullets only; each 70 words or fewer; students write the prose)")
    A("")
    A("Each follows the TN guide's three questions: why the team made the decision, how it aligned with the strategy, "
      "and how it served Laura's goals, funding needs or risks. Paraphrase the IPS rather than quoting it. Every "
      "reflection also carries:")
    A("")
    A(f"- **the scale sentence** ({len(SCALE.split())} words): \"{SCALE}\" (Book L: \"{SCALE_L}\")")
    A(f"- **what was checked or changed after Friday** (about 15 words): the 14 Oct check, an October trade, or "
      "\"no change\" with the reason;")
    A(f"- where certainty comes up, **the certainty phrase** once, never alone: {CERTAINTY};")
    A("- the strategy name once, if Ray confirms it by 22 Oct.")
    A("")
    for title, bullets in OUTLINES + ALT_OUTLINES:
        A(f"**{title}** ({outline_words(bullets)} words)")
        A("")
        for b in bullets:
            A(f"- {b}")
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
      "Wording only: e.g. \"maturing before it\", as the pitch says, plus a sentence on reinvested coupons. | "
      "fix-before-6-Nov (the team decides); the refined pick needs it by 22 Oct | IPS snapshot 30 Sep; premortem "
      "PM-14, PM-23; M9 reinvestment table |")
    A("| No sentence says which money covers a coupon-reinvestment shortfall. If coupons earn only 2%, keeping every "
      "payment whole costs about $20,000 more today (`reinvest.bookL_buffer_cost`), more than the about $7,600 of "
      "room under $300,000 (`laura.ladder.headroom_2027_strips`). If the floor were tapped, the bottom of the "
      "co-sponsor range would break. One sentence naming the order (e.g. the half of the stock fund Laura keeps, "
      "before the floor) closes it. | fix-before-6-Nov (wording only; the team chooses) | `reinvest.*`; IPS "
      "\"The other half remains with Laura as a cushion\" |")
    A("| If the 1 Oct vote picks Book L, the IPS sentence \"Our WInS portfolio shows the allocation after both "
      "deposits, scaled down\" becomes false, and the TN Analysis cannot show the floor or the stock fund. | decide at "
      "the 1 Oct vote; fix-before-6-Nov if Book L | Sheet tab Book L header; s6 |")
    A("| In Laura's real account the floor can be Treasury notes maturing in late 2032 (4.125% 15 Nov 2032, "
      "91282CFV8; 3.75% 30 Nov 2032, 91282CPM7), as the IPS says. IBTM is only WInS's stand-in, and its end value is "
      "not fixed. | note-in-Final-Report | MSPD Table V, 31 Aug 2026 (`data/mspd_table5_2026-08-31.json`) |")
    A("| No iBonds Treasury fund ends Dec 2037 to Dec 2043, so the 2038-2042 payments use coupon bonds (the larger "
      "reinvestment exposure). The last two dated funds launched in March (IBTQ 25 Mar 2025, IBTR 25 Mar 2026), so a "
      "Dec 2037 fund could appear after Laura's January 2027 purchase (UNVERIFIED). | note-in-Final-Report | "
      "iShares product list, fetched 30 Sep (`data/ishares_ibonds_treasury_list_2026-09-30.csv`) |")
    A("| The Sheet's accrued interest for the 4.500% May 2038 bond is 0.530; 1.66 is right on 28 Sep (1.71 on 2 Oct). "
      "| fix-before-6-Nov (Sheet input); keep it out of notes | `wins.bond_accrued_mismatch`; tickets row 9 |")
    A("| Strategy name: kept out of WInS notes; the reflections lose their easiest link to the IPS without it. | "
      "decide by 22 Oct (Ray confirms the name) | IPS snapshot pitch paragraph |")
    A("")
    A("**Requests to WS1 for the Friday re-lock** (WS6 does not write `numbers.yaml`, PM-35; until they land, no note "
      "or reflection quotes these figures):")
    A("")
    A("1. Re-lock `laura.ladder.cost_2027_strips` and `breakeven_fall_bp_strips` on Friday's curve (the IBTR note and "
      "pick 1).")
    A("2. A `quote_as` for `wins.ibond_checks.*.premium_to_nav_pct` (e.g. \"its price was within 0.1% of the value of "
      "its Treasuries\"), for IBTP.")
    A("3. `wins.bond_check.T_4.375%_15-Feb-2038`: `quote_as` \"almost a full percentage point of yield off the curve\" "
      "in place of \"about 1 point\" (a price point to a bond reader); optionally the clean-price gap (99.98 against "
      "92.183, about 8.5% rich).")
    A("4. A `quote_as` for IBTM only: \"about 97% even if its income earns only 2%\" (`reinvest.rung.IBTM`).")
    A("5. The M9 swap figures for the 2041 payment: 93.9% against 87.9% at 2%, and $23,266 against $23,146 at forward "
      "rates (`out/m9_screen_2026-09-28.json`), for picks 2 and OD_B.")
    A("6. The ladder cost at the WInS prices actually paid against the curve (all five bonds were 2 to 15 hundredths "
      "of a point of yield rich), for alternate C.")
    A("7. `market.etf_2026-09-28`: add the Nasdaq 30-session `adv30` the tickets use and relabel `avg_volume_20d` "
      "(it equals iShares' 30-day figure).")
    A("8. A scale-factor key (WInS book against Laura's plan after both deposits), only if the team wants a ratio in "
      "a reflection.")
    A("")
    A("## 8. Checks run by build_notes.py")
    A("")
    A("| Note | Chars | Length | ASCII | 1 para | Banned | Role | Laura | One number at most | Numbers traced | "
      "Dollar scale | Pick anchor |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for nid, cs in results.items():
        chars = next(x for x in NOTES + VARIANTS if x["id"] == nid)["exemplar"]
        A(f"| {nid} | {len(chars)} | " + " | ".join(("n/a" if c[2] == "n/a" else "pass") if c[1] else f"FAIL {c[2]}"
                                                    for c in cs) + " |")
    A("")
    A(f"Variety (judge panel, 30 Sep), across the {boiler['n']} Portfolio notes typed on Friday and Monday: the most "
      f"common opening (first three words) is used by {boiler['open'][1]} (\"{boiler['open'][0]}\", limit "
      f"{MAX_SAME_OPEN}); the most common ending (last four words) by {boiler['end'][1]} (\"{boiler['end'][0]}\", "
      f"limit {MAX_SAME_END}). Across all {boiler['all_n']} exemplars, including the conditional ones never typed "
      f"together: {boiler['all_open'][1]} and {boiler['all_end'][1]}.")
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
      "product-screener-v3.1.jsn (extract, with inception dates, in `data/ishares_ibonds_treasury_list_2026-09-30.csv`).")
    A("- U.S. Treasury MSPD Table V, record date 31 Aug 2026: https://api.fiscaldata.treasury.gov/services/api/"
      "fiscal_service/v1/debt/mspd/mspd_table_5 (`data/mspd_table5_2026-08-31.json`): late-2032 notes, the 2037-2041 "
      "bonds and the low-coupon Nov 2040 and Nov 2041 issues.")
    A("- `rab/numbers.yaml` (Gate A lock), `tickets.md`, `M9_selection.md`, `october_trade.md`, `rab/premortem.md`, "
      "insight_v1 `trading_notes_pack.md` (rules reused; its book is superseded), `D9_draft_checker.py` (ideas reused "
      "in `note_check.py`), Winning Team Portrait and Scoresheet.md, `judge_response.md` (panel of 30 Sep).")
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
    csv_path, md_path = os.path.join(HERE, "notes.csv"), os.path.join(HERE, "notes.md")
    rows = write_csv(csv_path, T, Y)
    write_md(md_path, T, Y, h, results, boiler)
    g = grep_outputs([csv_path, md_path])
    ips_missing = check_ips_quotes()
    long_outlines = [(t, outline_words(b)) for t, b in OUTLINES + ALT_OUTLINES if outline_words(b) > MAX_OUTLINE_WORDS]
    seq_ok = all(any(r["book"] == b and int(r["seq"]) == s and r["id"].split(" (")[0] == n["ticker"] for r in T)
                 for n in NOTES for b, s in n["books"].items())
    for nid, cs in results.items():
        bad = [f"{c[0]} ({c[2]})" for c in cs if not c[1]]
        print(f"{nid:7s} {len(next(x for x in NOTES + VARIANTS if x['id'] == nid)['exemplar']):4d} chars  "
              f"{'pass' if not bad else 'FAIL: ' + ', '.join(bad)}")
    print(f"notes.csv rows: {len(rows)}; superseded/stale grep hits: {g or 'none'}; numbers.yaml {h[:12]}")
    print(f"IPS quotes not verbatim in the 30 Sep snapshot: {ips_missing or 'none'}")
    print("reflection outlines (words): " + ", ".join(f"{t.split(',')[0]} {outline_words(b)}"
                                                        for t, b in OUTLINES + ALT_OUTLINES)
          + (f"; OVER {MAX_OUTLINE_WORDS}: {long_outlines}" if long_outlines else ""))
    print(f"variety: opening '{boiler['open'][0]}' x{boiler['open'][1]} (max {MAX_SAME_OPEN}), ending "
          f"'{boiler['end'][0]}' x{boiler['end'][1]} (max {MAX_SAME_END}): {'pass' if boiler['ok'] else 'FAIL'}")
    print(f"note seq matches tickets.csv (security and order): {'pass' if seq_ok else 'FAIL'}")
    nfail = fails + len(g) + len(ips_missing) + len(long_outlines) + (not boiler["ok"]) + (not seq_ok)
    print(f"{nfail} fail")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
