"""MODEL (Keel, 6 Nov 2026). Ten $50,000 payments (1 Jan 2033..2042) priced with the instruments Caplet holds in WInS, at market prices.
Each rung = the curve rung (5 Nov treasury.gov curve, payment-date basis) x how rich or cheap our instrument is
against that curve, so the only differences from the curve figure are the instruments' own prices and the fund fee.
Bonds: 5 Nov 2026 bid/ask mid (onvista/finanzen.net, Baader or Stuttgart, ~16:00 ET); ratio = market dirty / curve dirty.
iBonds funds: iShares average YTM, 4 Nov 2026, vs the 4 Nov curve's par yield at the fund's average maturity;
ratio = exp(-duration x spread) x (1.0007)^years to the fund's 15 Dec end (0.07% fee).
Sources (read 6 Nov 2026 with the WebFetch tool): ishares.com / blackrock.com product pages for IBTM 328944,
IBTO 332291, IBTP 337745, IBTQ 342105, IBTR 350028 (YTM, WAM, duration as of 4 Nov); onvista.de pages for
US912810PT97, US912810QD37, US912810QL52 and finanzen.net pages for US912810PX00, US912810QT88 (5 Nov quotes).
Results 6 Nov: curve $302,137 (67.1% of $450k), our instruments $303,269 (67.4%), money idle at 0% $306,663
(68.1%); the WInS positions hold 67-72% of each full rung (the book is the plan scaled to the $300k simulator).
Usage: python3 keel/scripts/holdings_ladder.py"""
import math, sys
from pathlib import Path
from datetime import date
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "library/assistant_review_2026-10/checks"))
import indep_pricer as P
CSV = str(Path(__file__).resolve().parents[2] / "competition/official_market_data/daily-treasury-rates_2026-11-05.csv")
d0, d4, J27 = date(2026, 11, 5), date(2026, 11, 4), date(2027, 1, 1)
c5, c4 = P.Curve(P.load_curve(CSV, "11/05/2026")), P.Curve(P.load_curve(CSV, "11/04/2026"))
pts4 = P.load_curve(CSV, "11/04/2026")
def par4(t):
    import numpy as np
    return float(np.interp(t, [p[0] for p in pts4], [p[1] for p in pts4]))
fwd = 1 / c5.df(P.yf(d0, J27))
rung = lambda Y: 50000 * c5.df(P.yf(d0, date(Y, 1, 1))) * fwd
FUNDS = [("IBTM Dec 2032", 2033, 4.73, 5.65, 4.98), ("IBTO Dec 2033", 2034, 4.76, 6.62, 5.65),
         ("IBTP Dec 2034", 2035, 4.81, 7.66, 6.36), ("IBTQ Dec 2035", 2036, 4.85, 8.65, 7.00),
         ("IBTR Dec 2036", 2037, 4.88, 9.53, 7.55)]
BONDS = [("4.75% Feb-2037", 2038, 4.75, date(2037, 2, 15), 99.934, 100.197),
         ("4.50% May-2038", 2039, 4.50, date(2038, 5, 15), 97.19, 97.28),
         ("4.375% Nov-2039", 2040, 4.375, date(2039, 11, 15), 94.004, 94.437),
         ("4.25% Nov-2040", 2041, 4.25, date(2040, 11, 15), 91.762, 92.218),
         ("3.125% Nov-2041", 2042, 3.125, date(2041, 11, 15), 79.05, 79.09)]
ti = tc = 0
print(f"{'held instrument':16s} pays  market    curve     rung@curve  rung@ours   diff")
for nm, Y, ytm, wam, dur in FUNDS:
    spread = ytm / 100 - par4(wam)
    ratio = math.exp(-dur * spread) * 1.0007 ** P.yf(d0, date(Y - 1, 12, 15))
    a, b = rung(Y), rung(Y) * ratio; ti += b; tc += a
    print(f"{nm:16s} {Y}  {ytm:.2f}%    {par4(wam)*100:.2f}%    ${a:>9,.0f}  ${b:>9,.0f}  {b-a:>+5,.0f}")
for nm, Y, cp, m, bid, ask in BONDS:
    ai = P.accrued(cp, m, d0); mid = (bid + ask) / 2; cv = P.dirty_from_curve(c5, cp, m, d0) - ai
    ratio = (mid + ai) / (cv + ai)
    a, b = rung(Y), rung(Y) * ratio; ti += b; tc += a
    print(f"{nm:16s} {Y}  {mid:7.3f}   {cv:7.3f}   ${a:>9,.0f}  ${b:>9,.0f}  {b-a:>+5,.0f}")
print(f"TOTAL, valued 1 Jan 2027: curve ${tc:,.0f} ({tc/450000:.1%} of $450k); our instruments ${ti:,.0f} ({ti/450000:.1%}); diff {ti-tc:+,.0f}")

# 2) money waits at 0%: each rung must exist in full on the instrument's own end date (fund 15 Dec, bond maturity)
MAT = {2033: date(2032, 12, 15), 2034: date(2033, 12, 15), 2035: date(2034, 12, 15), 2036: date(2035, 12, 15),
       2037: date(2036, 12, 15), 2038: date(2037, 2, 15), 2039: date(2038, 5, 15), 2040: date(2039, 11, 15),
       2041: date(2040, 11, 15), 2042: date(2041, 11, 15)}
# 3) what the WInS positions cover: position value today / today's cost of the full $50,000 rung
WINS = {2034: 1024 * 23.46, 2035: 927 * 24.65, 2036: 894 * 24.27, 2037: 853 * 24.11}
UNITS = {2038: 20, 2039: 20, 2040: 18, 2041: 18, 2042: 20}
tz = 0; cover = []
for nm, Y, *rest in FUNDS + BONDS:
    if Y <= 2037:
        ytm, wam, dur = rest
        ratio = math.exp(-dur * (ytm / 100 - par4(wam))) * 1.0007 ** P.yf(d0, date(Y - 1, 12, 15))
    else:
        cp, m, bid, ask = rest
        ai = P.accrued(cp, m, d0); mid = (bid + ask) / 2
        ratio = (mid + ai) / (P.dirty_from_curve(c5, cp, m, d0))
        WINS[Y] = UNITS[Y] * 10 * (mid + ai)
    r = rung(Y) * ratio
    tz += r * c5.df(P.yf(d0, MAT[Y])) / c5.df(P.yf(d0, date(Y, 1, 1)))
    if Y in WINS: cover.append((Y, WINS[Y], WINS[Y] / (r / fwd)))
print(f"Money earns nothing between maturity and 1 Jan: ${tz:,.0f} ({tz/450000:.1%})")
print("WInS positions as a share of each full $50,000 rung, today's prices:")
for Y, v, s in cover: print(f"  {Y}: ${v:,.0f} = {s:.0%}")
print(f"  2034-42 combined {sum(v for _, v, _ in cover):,.0f}")
