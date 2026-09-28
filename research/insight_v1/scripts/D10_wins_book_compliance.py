"""D10_wins_book_compliance.py - rule checks for the three candidate WInS books (question M005).

Agent D10 (Compliance Officer), insight_v1 run, 2026-09-28.

What it does (plain English):
1. Builds the three candidate WInS books at $300,000:
   (ii)  the post-2028 mix scaled to $300k (ticket option ii),
   (iii) the literal January-2027 book with the leftover in cash/T-bills (ticket option iii),
   (mid) the "middle path" asked by M005: the literal book, with the leftover sent to the growth mix (60/40) at once.
2. For each book and each possible Session Rules position limit (none / 35% / 25%) it counts positions, trades and
   commissions, and checks the "no more than twice a security's current daily trading volume" rule where volume data
   exist.
3. Compares the WInS equity share with the equity share of Laura's real portfolio at each plan date (the "which date
   does WInS show?" consistency check).
4. Under a 25% cap, estimates how far rates must move before a 24% holding drifts above 25% (in case WInS applies the
   limit continuously; first-order duration arithmetic).

Inputs and status labels:
- $300,000 WInS cash; $150,000 not added; commissions $25 per stock/ETF trade, $10 per bond trade; volume rule 2x
  current daily volume: SMApply Trading Details + FAQ, VERIFIED-PRIMARY (re-read 2026-09-27/28).
- Ladder cost at 2027-01-01 on the 2026-09-25 curve $292,264 (F-101): VERIFIED-REPO-FILE inputs + ASSUMPTION method.
- STRIPS ladder cost $294,387 (ticket section 2): VERIFIED-REPO-FILE (wins_now/securities_and_allocation_v0.md).
- Option (ii) weights IEF 23.6 / TLH 42.4 / VT 20.5 / VGSH 12.5 / cash 1; option (iii) IEF 35.0 / TLH 63.0 / cash 2;
  capped mixes (ticket section 3 and 10): VERIFIED-REPO-FILE (plan, not fact).
- Issuer durations IEF 6.86, TLH 11.59, SPTL 13.65, VGIT 4.9, VGLT 13.5 years; prices IEF 90.00, TLH 93.38,
  SPTL 24.27, VT 160.03, VGSH 57.59; volumes IEF 8,830,020 (30-day avg), TLH 1,969,419 (30-day avg), SPTL 1,088,651
  (prior day): ticket section 1, VERIFIED-PRIMARY there (issuer pages, 2026-09-24/25). Vanguard publishes no volume
  (VT, VGSH, VGIT, VGLT): check in WInS.
- Real-book equity shares by date: 2027 0% (T-bill rule) or ~1% (growth-mix rule, this script); 2028-2030 20.4% at a
  60/40 sleeve (F-409, ASSUMPTION-based); after the 2031 floor ~4% (brief section 16, ASSUMPTION-based).
- Cash float $1,000 minimum (ticket section 5): ASSUMPTION.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/D10_wins_book_compliance.py
Results are recorded in research/insight_v1/phase_D/D10_compliance.md (M005).
"""

CASH = 300_000.0
COMM_ETF = 25.0
DUR = {"IEF": 6.86, "TLH": 11.59, "SPTL": 13.65, "VGIT": 4.9, "VGLT": 13.5, "VT": 0.0, "VGSH": 1.9, "cash": 0.0}
PRICE = {"IEF": 90.00, "TLH": 93.38, "SPTL": 24.27, "VT": 160.03, "VGSH": 57.59}
VOL = {"IEF": 8_830_020, "TLH": 1_969_419, "SPTL": 1_088_651}  # shares per day (see docstring)


def hedge_mix(total_hedge_pct, cap):
    """Duration-weighted hedge (about 10y on issuer numbers) under a single-security cap, following ticket section 3.

    Returns {ticker: % of portfolio}. Target duration: the IEF/TLH 9.90-year mix (ticket), scaled to total_hedge_pct.
    """
    d_target = 9.90
    w_ief = (DUR["TLH"] - d_target) / (DUR["TLH"] - DUR["IEF"]) * total_hedge_pct
    w_tlh = total_hedge_pct - w_ief
    if cap is None or (w_ief <= cap and w_tlh <= cap):
        return {"IEF": w_ief, "TLH": w_tlh}
    # Ticket section 3 rule: IEF keeps its weight (at most cap-1), TLH one point under the cap, SPTL takes the rest.
    c = cap - 1.0
    tot = total_hedge_pct
    mix = {"IEF": min(w_ief, c), "TLH": c}
    mix["SPTL"] = tot - mix["IEF"] - mix["TLH"]
    if mix["SPTL"] <= c:
        return mix
    # Ticket section 10: three funds at cap-1, VGIT + VGLT carry the rest at the same ~9.90y duration
    # (all in VGIT if the solve would need a negative VGLT weight).
    mix = {"IEF": c, "TLH": c, "SPTL": c}
    rest = tot - 3 * c
    b = d_target * tot - (DUR["IEF"] + DUR["TLH"] + DUR["SPTL"]) * c
    w_l = max(0.0, (b - DUR["VGIT"] * rest) / (DUR["VGLT"] - DUR["VGIT"]))
    mix.update({"VGIT": rest - w_l, "VGLT": w_l})
    return mix


def book(option, cap):
    if option == "ii":
        mix = hedge_mix(66.0, cap)
        mix.update({"VT": 20.5, "VGSH": 12.5})
    elif option == "iii":
        mix = hedge_mix(98.0, cap)
    elif option == "mid":
        hedge_pct = 294_387 / CASH * 100
        mix = hedge_mix(hedge_pct, cap)
        n_trades = len(mix) + 2
        growth = CASH - 294_387 - n_trades * COMM_ETF - 1_000
        mix.update({"VT": 0.6 * growth / CASH * 100, "VGSH": 0.4 * growth / CASH * 100})
    mix["cash"] = 100.0 - sum(mix.values())
    return mix


def describe(option, cap):
    mix = book(option, cap)
    trades = [k for k in mix if k != "cash" and mix[k] > 0.005]
    comm = COMM_ETF * len(trades)
    dur_hedge = sum(DUR[k] * mix[k] for k in trades if k not in ("VT", "VGSH")) / sum(
        mix[k] for k in trades if k not in ("VT", "VGSH"))
    vol_checks = []
    for k in trades:
        if k in VOL:
            shares = mix[k] / 100 * CASH / PRICE[k]
            vol_checks.append(f"{k} {shares:,.0f} sh = {shares / (2 * VOL[k]) * 100:.2f}% of the 2x-volume cap")
    return mix, trades, comm, dur_hedge, vol_checks


def drift_threshold(mix, ticker, cap_pct):
    """Rate move (bp) at which ticker's weight reaches cap_pct, first order: w' = w(1-Di dy)/(1-Dp dy)."""
    w = mix[ticker] / 100
    dp = sum(DUR[k] * mix[k] / 100 for k in mix)
    di = DUR[ticker]
    target = cap_pct / 100
    # w(1 - di dy) = target (1 - dp dy)  ->  dy = (w - target) / (w di - target dp)
    dy = (w - target) / (w * di - target * dp)
    return dy * 10_000


if __name__ == "__main__":
    print("=== 1. Candidate books, positions, trades, commissions, volume rule ===")
    for option in ("ii", "iii", "mid"):
        for cap in (None, 35.0, 25.0):
            mix, trades, comm, dh, vols = describe(option, cap)
            eq = mix.get("VT", 0.0)
            cap_s = "no cap" if cap is None else f"cap {cap:.0f}%"
            print(f"({option}) {cap_s}: " + ", ".join(f"{k} {v:.1f}" for k, v in mix.items()))
            print(f"     positions {len(trades)}, first-week trades {len(trades)}, commissions ${comm:.0f}, "
                  f"hedge duration {dh:.2f}y, equity {eq:.1f}% of WInS")
            if vols:
                print("     volume: " + "; ".join(vols))
    print()
    print("=== 2. Middle path: size of the growth slice in dollars ===")
    for hedge_cost, label in ((294_387, "STRIPS ladder cost (ticket)"), (292_264, "F-101 cost at 2027-01-01")):
        for n_tr in (4, 7):
            growth = CASH - hedge_cost - n_tr * COMM_ETF - 1_000
            print(f"{label}, {n_tr} trades: growth ${growth:,.0f} = {growth / CASH * 100:.2f}% of WInS; "
                  f"VT ${0.6 * growth:,.0f} ({0.6 * growth / CASH * 100:.2f}%), VGSH ${0.4 * growth:,.0f}")
    print()
    print("=== 3. WInS equity share vs Laura's real equity share by plan date (percentage points) ===")
    real = {"Jan 2027 (T-bill rule)": 0.0, "Jan 2027 (growth-mix rule)": 1.0, "2028-2030": 20.4,
            "after 2031 floor": 4.0}
    for option in ("ii", "iii", "mid"):
        eq = book(option, None).get("VT", 0.0)
        gaps = ", ".join(f"{d}: {eq - r:+.1f}" for d, r in real.items())
        print(f"({option}) WInS equity {eq:.1f}% -> gap {gaps}")
    print()
    print("=== 4. 25% cap applied continuously: rate move before a 24% holding exceeds 25% ===")
    for option in ("ii", "iii"):
        mix = book(option, 25.0)
        for k in [k for k in mix if k != "cash" and mix[k] >= 23.9]:
            bp = drift_threshold(mix, k, 25.0)
            direction = "fall" if bp < 0 else "rise"
            print(f"({option}) {k} at {mix[k]:.1f}%: breaches 25% after rates {direction} by about {abs(bp):.0f}bp")
