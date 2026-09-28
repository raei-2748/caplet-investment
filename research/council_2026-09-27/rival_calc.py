# Rival strategist arithmetic. All return inputs are ASSUMPTIONS unless noted.
def ann_due(r,n=10,p=50000): return sum(p/(1+r)**k for k in range(n))
print("Reserve cost 2033 at flat 5/4/3%:",[round(ann_due(r)) for r in (.05,.04,.03)])
# IEF/TLT blend for duration 10 (durations from instruments.md snippets, UNVERIFIED)
for dief in (6.95,7.5):
    w=(15.31-10)/(15.31-dief); print(f"IEF dur {dief}: IEF weight {w:.3f}")
# Headroom in $300k: ladder $292.3k (curve A), DV01 $289
print("headroom bp curveA:", round((300000-292323)/289,1), " curve B shortfall:",314465-300000)
# G deterministic: 300 (2027) + 150 (2028) at blended r, 6 and 5 yrs
for r in (.05,.06,.07):
    V=300*(1+r)**6+150*(1+r)**5
    print(f"G 2033 value at {r:.0%}: {V:.0f}k; surplus vs 396k fwd {V-396:.0f}k, vs 439k (3%) {V-439:.0f}k")
# G without 2028 deposit
for r in (.05,.06,.07): print(f"G no-2028 at {r:.0%}: {300*(1+r)**6:.0f}k")
# L: ladder fwd value 2033 ~396k; sleeve 150+7.7 grows 5y
for r in (.05,.06,.07): print(f"L sleeve 2033 at {r:.0%}: {157.7*(1+r)**5:.0f}k")
# G stress: grow to 2031 at 6%, then 2032 equity -35% on 50% equity, bonds +5%; reserve priced at 3% in 2033
V31=300*1.06**4+150*1.06**3
V33=V31*1.06  # 2031->2032 normal
V33=V33*(0.5*0.65+0.5*1.05)
print(f"G stress: V2031 {V31:.0f}k, V2033 {V33:.0f}k, minus reserve@3% 439k -> {V33-439:.0f}k; minus 405k -> {V33-405:.0f}k")
# ERP vs 10y: JPM 6.7% (Oct-2025 vintage) vs 10y 5.17% (2026-09-25 snippet)
print("ERP JPM:",round(6.7-5.17,2),"Vanguard mid ~4.5-5.2 ->",round(4.5-5.17,2),round(5.2-5.17,2))
