from datetime import date
import indep_pricer as ip
d_buy = date(2027, 1, 4)   # Laura's purchase (first business day of 2027)
# Book L bond rungs (face from the Sheet's Book L tab), payment date each funds
rungs = [("T 4.750% Feb-2037", 4.75, date(2037,2,15), 30000, date(2038,1,1)),
         ("T 4.500% May-2038", 4.50, date(2038,5,15), 29000, date(2039,1,1)),
         ("T 4.375% Nov-2039", 4.375, date(2039,11,15), 27000, date(2040,1,1)),
         ("T 4.250% Nov-2040", 4.25, date(2040,11,15), 26000, date(2041,1,1)),
         ("T 3.125% Nov-2041", 3.125, date(2041,11,15), 29000, date(2042,1,1))]
def fv(flows, pay, r):
    return sum(cf * (1 + r/2) ** (2 * ip.yf(d, pay)) for d, cf in flows)
print("Terminal value at each payment date of the bond rungs bought 4 Jan 2027 (coupons reinvested at flat r)")
print(f"{'rung':20s} {'face':>7s} {'no reinvest':>11s} " + " ".join(f"{'r='+str(r)+'%':>9s}" for r in (0,2,3,4,5)))
tot = {r: 0 for r in (0,2,3,4,5)}
for name, cpn, mat, face, pay in rungs:
    flows, _ = ip.bond_flows(cpn, mat, d_buy)
    flows = [(d, cf * face / 100) for d, cf in flows]
    row = []
    for r in (0,2,3,4,5):
        v = fv(flows, pay, r/100); tot[r] += v; row.append(v)
    print(f"{name:20s} {face:7,d} {sum(cf for _,cf in flows):11,.0f} " + " ".join(f"{v:9,.0f}" for v in row))
print(f"{'5 bond rungs total':20s} {'':7s} {'':11s} " + " ".join(f"{tot[r]:9,.0f}" for r in (0,2,3,4,5)), " (target 250,000)")
# share of each rung's $50k owed as set coupons+principal (no reinvestment)
