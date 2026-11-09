"""Data for the Final Report exhibits (Tue 10 Nov 2026). Every figure here is copied from keel/final_report/NUMBERS.md,
with its section, or read from the engine file that section names. Nothing is computed here except sums and
rounding. If NUMBERS.md changes, change this file the same day and rerun build_exhibits.py and the template.

MODEL marks Keel's calculation (NUMBERS.md stamp: "Everything here is MODEL" except 8g, which is the WInS record).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
NUMBERS_DIR = os.path.join(HERE, "..", "numbers")

# ---------------------------------------------------------------------------------------------------------------
# Exhibit 1 (APA Table 1): the holdings table. NUMBERS.md 8g, version 2 (Tue 10 Nov). The WInS record at cost, not a
# model. Bond identifiers are placeholders until Caplet's final WInS export arrives (8g "Identifiers").
# "Pays for" comes from the 23 Oct snapshot's "Pays for" column (competition/wins/2026-10-23_snapshot.md), worded
# plainly; it is a label, not a number.
# ---------------------------------------------------------------------------------------------------------------
HOLDINGS = [
    # (identifier, name, asset type, amount, percent, pays for)
    ("IBTM", "iShares iBonds Dec 2032 Term Treasury ETF", "ETF (Treasury)", 97489.95, 32.50, "2033 payment and floor stand-in"),
    ("IBTO", "iShares iBonds Dec 2033 Term Treasury ETF", "ETF (Treasury)", 23408.64, 7.80, "2034 payment"),
    ("IBTP", "iShares iBonds Dec 2034 Term Treasury ETF", "ETF (Treasury)", 22155.30, 7.39, "2035 payment"),
    ("IBTQ", "iShares iBonds Dec 2035 Term Treasury ETF", "ETF (Treasury)", 20973.24, 6.99, "2036 payment"),
    ("IBTR", "iShares iBonds Dec 2036 Term Treasury ETF", "ETF (Treasury)", 19823.72, 6.61, "2037 payment"),
    ("[WInS ID]", "T-Bond 4.750% 15-Feb-2037", "Treasury bond", 19203.80, 6.40, "2038 payment"),
    ("[WInS ID]", "T-Bond 4.500% 15-May-2038", "Treasury bond", 18615.26, 6.20, "2039 payment"),
    ("[WInS ID]", "T-Bond 4.375% 15-Nov-2039", "Treasury bond", 16200.95, 5.40, "2040 payment"),
    ("[WInS ID]", "T-Bond 4.250% 15-Nov-2040", "Treasury bond", 15790.32, 5.26, "2041 payment"),
    ("[WInS ID]", "T-Bond 3.125% 15-Nov-2041", "Treasury bond", 14991.00, 5.00, "2042 payment"),
    ("VT", "Vanguard Total World Stock ETF", "ETF (equity)", 26524.61, 8.84, "Growth: top of the range and the half kept"),
    ("N/A", "Cash", "Cash", 3513.79, 1.17, "Cash"),
    ("N/A", "Commissions and bond interest paid at purchase", "Cost", 1309.42, 0.44, "Cost of buying"),
]
HOLDINGS_TOTAL = (300000.00, 100.00)  # 8g: "must equal $300,000 and 100%"

# 8g note facts (used in the table note, not in the body): $200 commissions (six ETF trades at $25, five bond trades at
# $10) and $1,109.42 interest accrued since each bond's last coupon; cash = WInS cash $3,513.79; prices paid 6-7 Oct (ET).
HOLDINGS_NOTE_FACTS = {"commissions": 200.00, "accrued_interest": 1109.42, "wins_cash": 3513.79}

# ---------------------------------------------------------------------------------------------------------------
# Exhibit 2 (APA Figure 1): the operating reserve running down, 2033-2042. NUMBERS.md 8h (MODEL: design A at Keel's
# call, valued at the 6 Nov 2026 curve's forward rates). Table values as printed in 8h.
# ---------------------------------------------------------------------------------------------------------------
# (payment year, holding short label, holding type, cash-arrival date as (y, m, d), months early as stated in 8h)
RESERVE_RUNGS = [
    (2033, "IBTM", "iBond ETF", (2032, 12, 15), 0.5),
    (2034, "IBTO", "iBond ETF", (2033, 12, 15), 0.5),
    (2035, "IBTP", "iBond ETF", (2034, 12, 15), 0.5),
    (2036, "IBTQ", "iBond ETF", (2035, 12, 15), 0.5),
    (2037, "IBTR", "iBond ETF", (2036, 12, 15), 0.5),
    (2038, "4.750% bond, Feb 2037", "T-bond", (2037, 2, 15), 10.5),
    (2039, "4.500% bond, May 2038", "T-bond", (2038, 5, 15), 7.6),
    (2040, "4.375% bond, Nov 2039", "T-bond", (2039, 11, 15), 1.5),
    (2041, "4.250% bond, Nov 2040", "T-bond", (2040, 11, 15), 1.5),
    (2042, "3.125% bond, Nov 2041", "T-bond", (2041, 11, 15), 1.5),
]
# 8h text: "the iBond ETFs about half a month (15 December); the Feb-2037 bond 10.5 months; the May-2038 bond 7.6
# months; the three November bonds 1.5 months". The engine file gives 0.6 for the ETFs (17 days / 30.44).

# 8h table: 1 January | reserve before | paid | reserve after | payments still owed | their value at forwards | bonds share
RESERVE_TABLE = [
    (2033, 427028, 50000, 375323, 450000, 349089, 50),
    (2034, 394700, 50000, 342614, 400000, 317111, 58),
    (2035, 360429, 50000, 307931, 350000, 283600, 68),
    (2036, 324259, 50000, 271281, 300000, 248639, 81),
    (2037, 286016, 50000, 232421, 250000, 212144, 100),
    (2038, 245360, 50000, 190873, 200000, 173954, 100),
    (2039, 201737, 50000, 147165, 150000, 133855, 100),
    (2040, 155733, 50000, 101085, 100000, 91648, 100),
    (2041, 107126, 50000, 51860, 50000, 47124, 100),
    (2042, 55025, 50000, 0, 0, 0, None),
]
# 8h: "each rung pays $1,705 (2033) to $5,266 (2041) more than $50,000, $36,859 in all", "if rates follow today's
# forwards"; "If every reinvestment earns 3 points less, each rung pays exactly $50,000 (the design)".
RESERVE_FIRST_PAYMENT_TOTAL = 427028     # 8h composition, 1 Jan 2033
RESERVE_OVER_50K_TOTAL = 36859           # 8h text


def rung_over_50k():
    """Each rung's payout above $50,000 at today's forwards, per payment year. Read from the engine file that 8h names
    (numbers/results_reserve.json, key base[].this_rung_over_50k), checked against the 8h table (before - paid - after)
    to within $2 of rounding. NUMBERS 8h prints only the ends and the sum; add the column to 8h before 27 Nov."""
    path = os.path.join(NUMBERS_DIR, "results_reserve.json")
    with open(path) as fh:
        base = json.load(fh)["base"]
    out = {}
    for row, tab in zip(base, RESERVE_TABLE):
        year = int(row["date"][:4])
        assert year == tab[0]
        v = round(row["this_rung_over_50k"])
        derived = tab[1] - tab[2] - tab[3]
        assert abs(v - derived) <= 2, (year, v, derived)
        out[year] = v
    assert abs(sum(out.values()) - RESERVE_OVER_50K_TOTAL) <= 2
    assert out[2033] == 1705 and out[2041] == 5266
    return out


# ---------------------------------------------------------------------------------------------------------------
# Exhibit 3 (APA Table 2): the plan under several markets. SKELETON version 2: rows for today's forward rates, a
# recession replayed from history, rates lower for good, an inflation world; columns for the ten payments, the stated
# bottom and top, the gift, and the half kept. Data from cards Q19 and Q24 (other workers; not landed on Tue 10 Nov).
# Only the central row has register figures today, and NUMBERS 4 flags its stated top as "under review" (the per-end
# deduction gives $130,000 rather than $135,000). Every cell below is a PLACEHOLDER until Q19/Q24 land in NUMBERS.
# ---------------------------------------------------------------------------------------------------------------
SCENARIO_COLUMNS = ["Market from today", "Ten payments", "Stated range (2031)", "Gift (late 2032)", "Half kept (2033)"]
SCENARIO_ROWS = [
    # NUMBERS 4 central (MODEL): payments full; bottom stated $110,000; stated top $130,000 per the correction under
    # review ($133,412 rounded down to $5k); gift = floor $115,929 + moved half $22,806 = $138,735 (but capped at the
    # stated top if CANON D12's cap rule is adopted); kept half $23,986.
    ("Today's forward rates", "All ten in full", "$110,000 to $130,000*", "$138,735*", "$23,986"),
    # NUMBERS 2 and 8h: design A is sized so each rung pays exactly $50,000 if reinvestment earns 3 points below
    # forwards. The other cells need Q24.
    ("Rates 3 points lower for good", "All ten in full", "[Q24]", "[Q24]", "[Q24]"),
    ("Recession replayed (shares and rates fall together)", "[Q24]", "[Q24]", "[Q24]", "[Q24]"),
    ("Inflation (rates up, shares flat)", "[Q24]", "[Q24]", "[Q24]", "[Q24]"),
]

# NUMBERS 4 figures that the former "range forming" candidate would use (house model, 1-in-20 low / median / high,
# MODEL; another worker is recomputing them, so they are placeholders here).
RANGE_PLACEHOLDERS = {
    "floor_payout_bottom": (93000, 115929, 140000),      # "Floor payout, late 2032 (bottom)": $93k / $116k / $140k
    "top": (111000, 138735, 171000),                     # "Top of the range": $111k / $139k / $171k
    "kept_half": (12000, 23986, 47000),                  # "Half kept ... 1 Jan 2033": $12k / $24k / $47k
    "stated_bottom": 110000,                             # "Bottom Laura states"
    "stated_top_corrected": 130000,                      # correction under review, NUMBERS 4
}

# NUMBERS 4 C8 (all-Treasury benchmark), for the former candidate "the gift against an all-Treasury plan".
ALL_TREASURY = {"certain_with_margin": 158157, "certain_without_margin": 185987,
                "final_total_median_with_margin": 164000, "final_total_low_with_margin": 128000,
                "benchmark_low_with_margin": 127000, "share_of_paths_final_total_ahead": 0.63}

if __name__ == "__main__":
    tot = sum(h[3] for h in HOLDINGS)
    pct = sum(h[4] for h in HOLDINGS)
    print(f"Holdings: ${tot:,.2f}  {pct:.2f}%")
    assert abs(tot - 300000) < 0.005 and abs(pct - 100) < 1e-9
    print("Rung surplus at forwards:", rung_over_50k())
