"""W-01 (Window, 28 Oct 2026): how much of the coupon gap is a choice of bond? MODEL.
Same maturity, same yield to maturity, two coupons: what share of the money that pays the cheque arrives early as
coupons, and what is lost if every coupon is reinvested 2 points lower for good? Coupons sourced from Treasury
auction results (TreasuryDirect, read 28 Oct 2026) and the WInS snapshot of 23 Oct (competition/wins/).
Simplifications (MODEL): settle 1 Jan 2027, flat yield, semiannual coupons on 15 May/15 Nov (Feb/Aug for Feb bonds),
first coupon a full one, reinvested at the flat rate to maturity; both bonds priced on the same yield (on the real
curve the low-coupon issue can trade a few bp off)."""
import json, datetime as dt

def months(a, b): return (b.year - a.year) * 12 + (b.month - a.month) + (b.day - a.day) / 30.0

def coupon_dates(maturity, start):
    d, out = maturity, []
    while d > start:
        out.append(d)
        m = d.month - 6; y = d.year
        if m <= 0: m += 12; y -= 1
        d = dt.date(y, m, 15)
    return sorted(out)

def run(coupon, maturity, ytm, shock, need=50_000.0, start=dt.date(2027, 1, 1)):
    ds = coupon_dates(maturity, start)
    h = ytm / 2
    # face F such that coupons reinvested at ytm + face grow to `need` at maturity
    fv_per_face = sum((coupon / 2) * (1 + h) ** (months(d, maturity) / 6) for d in ds) + 1.0
    face = need / fv_per_face
    cost = need / (1 + h) ** (months(start, maturity) / 6)
    h2 = (ytm - shock) / 2
    fv_shock = face * (sum((coupon / 2) * (1 + h2) ** (months(d, maturity) / 6) for d in ds) + 1.0)
    early = face * sum(coupon / 2 for d in ds)
    return dict(coupon=coupon, maturity=str(maturity), ytm=ytm, face=round(face), cost=round(cost),
                coupon_cash_share=round(1 - face / need, 3), coupons_paid=round(early),
                shortfall_if_minus_2pt=round(need - fv_shock))

rungs = [  # (label, high-coupon bond held in WInS, low-coupon bond of the same maturity, yield from WInS snapshot 23 Oct)
    ("Jan 2041 cheque", (0.0425, dt.date(2040, 11, 15)), (0.01375, dt.date(2040, 11, 15)), 0.0529),
    ("Jan 2042 cheque", (0.03125, dt.date(2041, 11, 15)), (0.02, dt.date(2041, 11, 15)), 0.0537),
]
out = []
for label, hi, lo, y in rungs:
    a, b = run(hi[0], hi[1], y, 0.02), run(lo[0], lo[1], y, 0.02)
    out.append(dict(rung=label, held=a, low_coupon=b))
    print(label, "\n  held   ", a, "\n  low cpn", b)
# a zero (for scale only; STRIPS are banned for Laura's plan)
z = run(0.0, dt.date(2040, 11, 15), 0.0529, 0.02); print("zero (banned, scale only)", z)
out.append(dict(rung="zero-coupon reference (STRIPS banned; scale only)", held=z))
json.dump(out, open(__file__.replace(".py", "_results.json"), "w"), indent=1)
