# Independent quick check of the floor-size trade-off (my own simple lognormal model, not the repo's engine).
import numpy as np
rng = np.random.default_rng(1)
N = 400_000
mu, sig = np.log(1.07), 0.155          # world equities: 7.0% compound (JPM 2026 LTCMA AC World), ~16.8% arithmetic vol
T = 5.0                                  # Jan 2028 -> Jan 2033
g = np.exp(rng.normal(mu * T, sig * np.sqrt(T), N))
df_floor = 1 / (1 + 0.0506 / 2) ** (2 * 4.95)   # 5y par ~5.06% on 28 Sep, floor matures Dec 2032
cash = 150_000 + 7_600 * 1.045          # 2028 deposit + 2027 leftover
print(f"floor cost per $1 in Dec 2032: {df_floor:.3f}")
print(f"{'floor':>8s} {'stocks Jan28':>12s} {'p5 total':>9s} {'p50 total':>9s} {'p95 total':>9s}")
for F in (150_000, 125_000, 100_000, 75_000, 50_000, 0):
    E0 = cash - F * df_floor
    tot = F + E0 * g
    p5, p50, p95 = np.percentile(tot, [5, 50, 95])
    print(f"{F:8,d} {E0:12,.0f} {p5:9,.0f} {p50:9,.0f} {p95:9,.0f}")
# all-Treasury comparison: everything to Dec 2032 Treasuries
print(f"All-Treasury total (certain): {cash / df_floor:,.0f}")
