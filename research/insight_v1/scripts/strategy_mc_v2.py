"""strategy_mc_v2.py - Laura Gao lock-early model, version 2 (D3 Quant Modeler, insight_v1 run, 2026-09-28).

WHAT IT IS (one paragraph, plain English)
Each of 200,000 simulated "futures" draws yearly returns for stocks and bonds from J.P. Morgan's published
long-term assumptions. Laura's $300,000 first buys ten Treasury zero-coupon bonds that pay each $50,000 operating
payment (2033-2042). Whatever is left (the "sleeve"), plus the $150,000 she adds in 2028, is invested in a stock/bond
mix. In 2031 part of the sleeve is moved into a 2-year Treasury: that is the floor she can promise co-sponsors. In
2033 the floor plus the rest is the money available for the facility and for flexibility. Version 2 adds switches for
the things version 1 assumed away: rates moving before the January 2027 purchase, a smaller/late/missing/market-linked
2028 deposit, fees, a global stock fund and short Treasuries (what WInS holds), fat-tailed returns, the 2031 range
rules and the 2033 contribution/flexibility rules. Every switch is OFF by default, so the defaults reproduce the
verified model exactly (2033 surplus p5/p50/p95 $159k/$207k/$273k; seed 20260927; 200,000 paths).

EXTENDS research/verified_2026-09-27/strategy_mc.py (same seed, same first random draws, same formulas when every
switch is off). New randomness comes from separate, seeded streams so turning one switch on never changes another
switch's draws (common random numbers: differences between runs are caused by the switch, not by noise).

INPUTS AND STATUS LABELS
VERIFIED (repo files, read with the verified method):
- Official Treasury par curve 2026-09-25 (competition/official_market_data/daily-treasury-rates_2026-09.csv):
  bootstrap as in official_curve_pv.py -> ten payments at 2027-01-01 $292,264 (VERIFIED-REPO-FILE).
- Real ladder: ten STRIPS maturing each Nov 15 2032-2041, $294,387 at 2027-01-01 on the same curve
  (research/insight_v1/wins_now/S1_treasury_sleeve.md section 3; recomputed here) (VERIFIED-REPO-FILE inputs + method).
- JPM 2026 LTCMA (competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf p.2, VERIFIED-REPO-FILE):
  U.S. Large Cap 6.70/7.94/16.47 (compound/arithmetic/vol %); AC World 7.00/8.28/16.78; U.S. Intermediate
  Treasuries 4.00/4.06/3.48; U.S. Short Duration Government/Credit 4.00/4.01/1.63. Correlations: large cap vs
  intermediate Treasuries -0.01; AC World vs intermediate 0.00; large cap vs short govt/credit 0.16; AC World vs
  short govt/credit 0.21.
- Expense ratios (issuer pages via wins_now/securities_and_allocation_v0.md, VERIFIED-PRIMARY 2026-09-27): VT 0.06%,
  VGSH 0.03%, IEF/TLH 0.15%.
- 2026 realised volatility of the 10-year yield 71bp/yr (F-014; recomputed from FRED DGS10: 70.6bp);
  98-calendar-day changes of the 10-year since 1990: sd 47.7bp (FRED DGS10, VERIFIED-PRIMARY inputs, derived).
ASSUMPTIONS (each switchable; see Cfg below): lognormal (or Student-t) i.i.d. yearly returns; the 2031 2-year yield
equals today's 4.81%; the Jan-2028 5-year lock rate equals today's 4.98% (barbell only); parallel yield shifts with
zero drift from today's forwards; deposit-cut probability and correlation; fee levels; a 1pp-sd flat 5.26% 2033 rate
for strategies that buy payments in 2033 (the verified convention; ~$6k too expensive vs forwards, F-408).
Taxes are out of scope (case). WInS gains/losses are never added (case p.4).

HOW TO RUN (from the repo root):  .venv/bin/python research/insight_v1/scripts/strategy_mc_v2.py
It prints the reproduction check and one table per switch (a)-(g). Other D3 scripts import `simulate`, `Cfg` etc.
"""
import csv
from dataclasses import dataclass, replace
from datetime import date

import numpy as np
from scipy.stats import norm

PATHS, SEED = 200_000, 20260927
CURVE_CSV = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
VAL, ANCHOR = date(2026, 9, 25), date(2027, 1, 1)
PAY = [date(y, 1, 1) for y in range(2033, 2043)]
STRIPS = [date(y - 1, 11, 15) for y in range(2033, 2043)]          # Nov 15 of the year before each payment
TENOR = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}

# ------------------------------------------------------------------ asset assumptions (label, compound, arith, vol)
ASSETS = {
    "US_LC": ("JPM U.S. Large Cap (VERIFIED-REPO-FILE)", 0.0670, 0.0794, 0.1647),
    "ACWI": ("JPM AC World Equity (VERIFIED-REPO-FILE)", 0.0700, 0.0828, 0.1678),
    "US_LC_VANGUARD": ("Vanguard VCMM U.S. equity midpoint 5.2% (B10a, VERIFIED-PRIMARY range 4.2-6.2%; JPM vol "
                       "ASSUMPTION)", 0.0520, 0.0520 + (0.0794 - 0.0670), 0.1647),
    "INT_TSY": ("JPM U.S. Intermediate Treasuries (VERIFIED-REPO-FILE)", 0.0400, 0.0406, 0.0348),
    "SHORT_GC": ("JPM U.S. Short Duration Govt/Credit, closest JPM row to VGSH (VERIFIED-REPO-FILE)",
                 0.0400, 0.0401, 0.0163),
    "SHORT_TSY_FWD": ("Short Treasuries at forward-implied ~4.9% (ASSUMPTION; forwards are not forecasts)",
                      0.0490, 0.0491, 0.0163),
    "SHORT_TSY_LOW": ("Short Treasuries at 3.5% (ASSUMPTION; Fed longer-run funds rate 3.2% + small term premium)",
                      0.0350, 0.0351, 0.0163),
    "INT_TSY_FWD": ("Intermediate Treasuries at 5.0% (ASSUMPTION, B10a forward-consistent)", 0.0500, 0.0506, 0.0348),
}
CORR = {("US_LC", "INT_TSY"): -0.01, ("ACWI", "INT_TSY"): 0.00, ("US_LC", "SHORT_GC"): 0.16,
        ("ACWI", "SHORT_GC"): 0.21}                     # JPM matrix, VERIFIED-REPO-FILE
BOND_CORR_FAMILY = {"INT_TSY": "INT_TSY", "INT_TSY_FWD": "INT_TSY", "SHORT_GC": "SHORT_GC",
                    "SHORT_TSY_FWD": "SHORT_GC", "SHORT_TSY_LOW": "SHORT_GC"}
EQ_CORR_FAMILY = {"US_LC": "US_LC", "US_LC_VANGUARD": "US_LC", "ACWI": "ACWI"}
EXPENSE = {"VT": 0.0006, "VGSH": 0.0003, "IEF": 0.0015, "TLH": 0.0015}   # VERIFIED-PRIMARY (S3 ticket)


def lognorm_params(compound, arithmetic, vol=None, method="ca"):
    """Log-mean/log-sd so the median yearly return = compound. method 'ca' (the verified one) matches the arithmetic
    mean; method 'cv' matches the published volatility (used only for low-volatility bond rows, where JPM's two-decimal
    rounding of compound vs arithmetic makes 'ca' imprecise)."""
    mu = np.log(1 + compound)
    if method == "ca":
        return mu, np.sqrt(2 * np.log((1 + arithmetic) / (1 + compound)))
    return mu, np.sqrt(np.log(1 + (vol / (1 + arithmetic)) ** 2))


def asset_params(name):
    _, c, a, v = ASSETS[name]
    method = "cv" if name.startswith("SHORT") else "ca"
    return lognorm_params(c, a, v, method)


# ------------------------------------------------------------------ curve (verified method, any parallel shift)
def load_par(csv_path=CURVE_CSV, day="09/25/2026"):
    row = next(r for r in csv.DictReader(open(csv_path)) if r["Date"] == day)
    return {t: float(row[k]) for k, t in TENOR.items()}


PAR = load_par()
yf = lambda d: (d - VAL).days / 365.25


def build(par):
    ts = sorted(par)
    grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts])
    df = []
    for y in p:
        c = y / 2
        df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]
    lz = np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))


SHIFTS = np.round(np.arange(-500, 501) / 100.0, 2)        # parallel par shifts, percentage points, 1bp steps


def _curve_tables():
    """Per 1bp parallel shift of today's par curve: rung prices (Nov-15 STRIPS and exact Jan-1 zeros) as forward
    values at 2027/2028/2029-01-01, the ladder at 2033-01-01, and forward zero rates used for locks."""
    when = {k: date(2026 + k, 1, 1) for k in (1, 2, 3, 7)}
    out = {"strip": {k: np.zeros((len(SHIFTS), 10)) for k in when}, "exact": {k: np.zeros((len(SHIFTS), 10)) for k in when}}
    for i, s in enumerate(SHIFTS):
        f = build({t: v + s for t, v in PAR.items()})
        for k, d in when.items():
            base = f(yf(d))
            out["strip"][k][i] = [50_000 * f(yf(m)) / base for m in STRIPS]
            out["exact"][k][i] = [50_000 * f(yf(m)) / base for m in PAY]
    return out


TABLES = _curve_tables()
I0 = int(np.where(SHIFTS == 0)[0][0])
LADDER_EXACT_2027 = float(TABLES["exact"][1][I0].sum())      # $292,264 (verified)
LADDER_STRIPS_2027 = float(TABLES["strip"][1][I0].sum())     # $294,387 (S1)
f0 = build(PAR)
FWD_ZERO_27_33 = 2 * ((f0(yf(ANCHOR)) / f0(yf(date(2033, 1, 1)))) ** (1 / (2 * (yf(date(2033, 1, 1)) - yf(ANCHOR)))) - 1)
FWD_FACTOR_27_33 = (1 + 0.0508 / 2) ** 12                    # verified script's rounded 5.08% (semiannual)
FWD_28_33 = (f0(yf(date(2028, 1, 1))) / f0(yf(date(2033, 1, 1))))  # growth factor locked today, 2028 -> 2033
FWD_27_28 = f0(yf(ANCHOR)) / f0(yf(date(2028, 1, 1)))


def interp_rows(table, shift):
    """Interpolate table rows (len(SHIFTS) x n) at per-path shifts (array, percentage points)."""
    x = np.clip(shift, SHIFTS[0], SHIFTS[-1])
    pos = (x - SHIFTS[0]) / 0.01
    lo = np.floor(pos).astype(int)
    lo = np.clip(lo, 0, len(SHIFTS) - 2)
    w = (pos - lo)[:, None]
    return table[lo] * (1 - w) + table[lo + 1] * w


def annuity_due(rate):
    t = np.arange(10)
    return (50_000 / (1 + rate[..., None]) ** t).sum(-1)


# ------------------------------------------------------------------ configuration (every switch OFF = verified)
@dataclass(frozen=True)
class Cfg:
    paths: int = PATHS
    seed: int = SEED
    # strategy L core -- ASSUMPTION parameters the team still has to choose
    eq_w: tuple = (0.60,) * 6            # sleeve equity weight per year 2027..2032 (rest of sleeve after 2031 too)
    floor_share: float = 0.80            # share of the sleeve locked in 2031 (one-date design)
    floor_design: str = "one_date"       # 'one_date' | 'ratchet' | 'barbell' | 'none'
    ratchet_rates: tuple = (0.0496, 0.0494, 0.0481)   # 4y/3y/2y par today (ASSUMPTION: unchanged at lock dates)
    barbell_share: float = 0.50          # share of the Jan-2028 sleeve locked to 2033 (barbell only)
    barbell_rate: float = 0.0498         # 5y par today (ASSUMPTION: unchanged in Jan 2028)
    barbell_eq_w: float = 1.00           # equity weight of the unlocked barbell part
    y2_2031: float = 0.0481              # VERIFIED 2y par today; ASSUMPTION it holds in 2031 (test 3-4%)
    # (a) rate risk before the Jan-2027 purchase
    ladder: str = "exact"                # 'exact' ($292,264 verified) | 'strips' (Nov-15 STRIPS, $294,387)
    pre_rate_sd: float = 0.0             # sd of the parallel shift 2026-09-25 -> 2027-01-01, in pp (0.37 = F-014)
    yearly_rate_sd: float = 0.71         # sd of yearly parallel shifts after purchase, pp (F-014) - top-ups only
    markup: float = 0.0                  # broker mark-up on the ladder purchase (ASSUMPTION 0-0.5%, unsourced)
    # (b) 2028 deposit
    deposit: float = 150_000             # case: "will contribute an additional $150,000"
    deposit_year: int = 1                # 1 = start of 2028 (case); 2 = late, start of 2029 (ASSUMPTION scenario)
    cut_prob: float = 0.0                # probability the deposit is cut (ASSUMPTION scenario)
    cut_frac: float = 0.5                # size of the cut (0.5 -> $75k, 1.0 -> $0)
    rho_deposit: float = 0.0             # correlation of the cut with the 2027 stock shock (ASSUMPTION range 0-0.9)
    rho_stock_rate: float = 0.0          # corr(2027 stock shock, 2027 yield change); JPM ~0; 2000-21 era ~+0.65
    # (c) fees
    fund_expense: float = 0.0            # sleeve fund expense ratio per year (e.g. 0.00048 = 60% VT + 40% VGSH)
    adv_fee_sleeve: float = 0.0          # advisory fee on sleeve + floor, per year (ASSUMPTION 0/0.5/1.0%)
    adv_fee_ladder: float = 0.0          # advisory fee on the ladder's market value, paid from the sleeve
    # (d) assets
    eq_asset: str = "US_LC"
    bd_asset: str = "INT_TSY"
    eq_mu_shift: float = 0.0             # verified script's equity drift shift (log points)
    # (e) tails
    tails: str = "normal"                # 'normal' | 't'
    t_nu: float = 5.0
    t_clip: float = 8.0
    # strategies that buy payments in 2033 (G, partial locks): verified convention
    rate33_mean: float = 0.0526
    rate33_sd: float = 0.010


def draws(cfg):
    """Random numbers. The first stream is IDENTICAL to the verified script (z1, z2, rate33)."""
    rng = np.random.default_rng(cfg.seed)
    z1 = rng.standard_normal((cfg.paths, 6))
    z2 = rng.standard_normal((cfg.paths, 6))
    z33 = rng.standard_normal(cfg.paths)
    rr = np.random.default_rng(np.random.SeedSequence([cfg.seed, 1]))     # rates (a)
    zpre = rr.standard_normal(cfg.paths)
    zy = rr.standard_normal((cfg.paths, 6))
    rd = np.random.default_rng(np.random.SeedSequence([cfg.seed, 2]))     # deposit (b)
    ud = rd.standard_normal(cfg.paths)
    rt = np.random.default_rng(np.random.SeedSequence([cfg.seed, 3]))     # t mixing (e)
    chi = rt.chisquare(cfg.t_nu, size=(cfg.paths, 6))
    return dict(z1=z1, z2=z2, z33=z33, zpre=zpre, zy=zy, ud=ud, chi=chi)


def returns(cfg, d):
    """Yearly equity and bond returns (paths x 6, years 2027..2032)."""
    rho = CORR[(EQ_CORR_FAMILY[cfg.eq_asset], BOND_CORR_FAMILY[cfg.bd_asset])]
    xe, xb = d["z1"], rho * d["z1"] + np.sqrt(1 - rho ** 2) * d["z2"]
    if cfg.tails == "t":                                     # multivariate t, unit variance, clipped
        scale = np.sqrt((cfg.t_nu - 2) / d["chi"])
        xe = np.clip(xe * scale, -cfg.t_clip, cfg.t_clip)
        xb = np.clip(xb * scale, -cfg.t_clip, cfg.t_clip)
    me, se = asset_params(cfg.eq_asset)
    mb, sb = asset_params(cfg.bd_asset)
    req = np.exp(me + cfg.eq_mu_shift + se * xe) - 1
    rbd = np.exp(mb + sb * xb) - 1
    return req, rbd


def rate_path(cfg, d):
    """Parallel par-curve shifts (pp): dy0 before the Jan-2027 purchase, dys[:, y] during year y (2027 = 0)."""
    dy0 = cfg.pre_rate_sd * d["zpre"]
    e = d["zy"].copy()
    e[:, 0] = cfg.rho_stock_rate * d["z1"][:, 0] + np.sqrt(1 - cfg.rho_stock_rate ** 2) * d["zy"][:, 0]
    return dy0, cfg.yearly_rate_sd * e


def deposit_amounts(cfg, d):
    dep = np.full(cfg.paths, float(cfg.deposit))
    if cfg.cut_prob > 0:
        u = cfg.rho_deposit * d["z1"][:, 0] + np.sqrt(1 - cfg.rho_deposit ** 2) * d["ud"]
        cut = u < norm.ppf(cfg.cut_prob)
        dep = np.where(cut, dep * (1 - cfg.cut_frac), dep)
    return dep


def ladder_value_path(cost27):
    """Market value of the held ladder at the start of 2027..2032 on today's forwards (fee base)."""
    g = FWD_FACTOR_27_33 ** (1 / 6)
    return np.array([cost27 * g ** y for y in range(6)])      # scalar-per-path arrays broadcast later


def simulate(cfg=Cfg(), strategy="L", lock_frac=1.0, ret=None):
    """Run one configuration. strategy 'L' (lock early), 'G' (growth first, verified), 'P' (partial lock of
    lock_frac of the ladder in 2027; rest bought in 2033), 'C' (riskless control: all surplus in Treasuries maturing
    2033). ret=(req, rbd) replaces model returns (e.g. historical sequences); arrays must be (n, 6)."""
    d = draws(cfg)
    req, rbd = returns(cfg, d) if ret is None else ret
    n = req.shape[0]
    if ret is not None:
        d = {k: v[:n] for k, v in d.items()}
    dy0, dys = rate_path(cfg, d)
    dep = deposit_amounts(cfg, d)[:n]
    eqw = np.array(cfg.eq_w if len(cfg.eq_w) == 6 else cfg.eq_w * 6)
    mix = lambda y, w=None: 1 + (eqw[y] if w is None else w) * req[:, y] + (1 - (eqw[y] if w is None else w)) * rbd[:, y]
    fee_s = cfg.fund_expense + cfg.adv_fee_sleeve
    out = {"deposit": dep}

    if strategy == "G":                                       # verified growth-first, all money on a glide path
        glide = (0.75, 0.75, 0.75, 0.75, 0.60, 0.40)
        rate33 = cfg.rate33_mean + cfg.rate33_sd * d["z33"]
        v = np.full(n, 300_000.0)
        for y in range(6):
            if y == cfg.deposit_year:
                v = v + dep
            v = v * mix(y, glide[y]) * (1 - fee_s)
        out["surplus"] = v - annuity_due(np.maximum(rate33, 0.0))
        out["short"] = np.maximum(-out["surplus"], 0)
        return out

    # ---- January 2027: buy the ladder (longest rungs first if it costs more than $300k) ----
    kind = "strip" if cfg.ladder == "strips" else "exact"
    rung27 = interp_rows(TABLES[kind][1], dy0) * (1 + cfg.markup)          # (n, 10) rung costs
    if strategy == "P":
        rung27 = rung27 * lock_frac
    order = rung27[:, ::-1]                                               # longest first
    cum_before = np.cumsum(order, axis=1) - order
    frac_long_first = np.clip((300_000 - cum_before) / order, 0, 1)
    frac = frac_long_first[:, ::-1]                                       # funded fraction per rung (2033..2042)
    cost27 = (rung27 * frac).sum(1)
    unfunded = 1 - frac                                                   # share of each rung still to buy
    s = 300_000 - cost27                                                  # sleeve at 2027-01-01
    out["cost27_full"] = rung27.sum(1)
    out["gap27"] = np.maximum(out["cost27_full"] - 300_000, 0)
    lad_val = np.outer(np.ones(n), [1.0] * 6) * cost27[:, None] * (FWD_FACTOR_27_33 ** (np.arange(6) / 6))[None, :]
    short_face = np.zeros(n)
    topup_paid = np.zeros(n)
    fees_paid = np.zeros(n)

    if strategy == "C":                                                   # riskless control
        # 2027 leftover locked in a zero maturing 2033-01-01 at the (shifted) forward; the deposit locked the same way
        # in its arrival year at that year's (shifted) forward. Growth factor = value at 2033 / value at lock date.
        g27 = interp_rows(TABLES["exact"][7], dy0)[:, 0] / interp_rows(TABLES["exact"][1], dy0)[:, 0]
        lock27 = np.maximum(s, 0) * g27
        cum = dy0 + dys[:, :cfg.deposit_year].sum(1)
        k = 1 + cfg.deposit_year
        gd = interp_rows(TABLES["exact"][7], cum)[:, 0] / interp_rows(TABLES["exact"][k], cum)[:, 0]
        need = (unfunded * interp_rows(TABLES[kind][k], cum)).sum(1)
        top = np.minimum(dep, need)
        out["surplus"] = lock27 * (1 - cfg.adv_fee_sleeve) ** 6 + (dep - top) * gd * (1 - cfg.adv_fee_sleeve) ** (6 - cfg.deposit_year)
        out["short_face"] = np.where(need > 0, (need - top) / np.maximum(need, 1e-9), 0) * (unfunded * 50_000).sum(1)
        return out

    floor33 = np.zeros(n)
    locked_extra = np.zeros(n)                                            # ratchet / barbell locks (2033 value)
    for y in range(6):                                                    # start of years 2027..2032
        if y == cfg.deposit_year:
            s = s + dep
            if unfunded.any():                                           # top up the short rungs first
                cum = dy0 + dys[:, :y].sum(1)
                need = (unfunded * interp_rows(TABLES[kind][1 + y], cum)).sum(1)
                paid = np.clip(np.minimum(s, need), 0, None)
                ratio = np.where(need > 0, paid / np.maximum(need, 1e-9), 1.0)
                short_face = ((1 - ratio)[:, None] * unfunded * 50_000).sum(1)
                s = s - paid
                topup_paid = paid
                unfunded = unfunded * (1 - ratio)[:, None]
        fee_lock = cfg.adv_fee_sleeve                                     # individual Treasuries: no fund expense
        if cfg.floor_design == "barbell" and y == 1:
            lock = cfg.barbell_share * np.maximum(s, 0)
            s = s - lock
            locked_extra = locked_extra + lock * (1 + cfg.barbell_rate) ** 5 * (1 - fee_lock) ** 5
        if cfg.floor_design == "ratchet" and y in (2, 3, 4):
            k = y - 2
            share = [(cfg.floor_share / 3), (cfg.floor_share / 3) / (1 - cfg.floor_share / 3),
                     (cfg.floor_share / 3) / (1 - 2 * cfg.floor_share / 3)][k]
            lock = share * np.maximum(s, 0)
            s = s - lock
            locked_extra = locked_extra + lock * (1 + cfg.ratchet_rates[k]) ** (6 - y) * (1 - fee_lock) ** (6 - y)
        if cfg.floor_design == "one_date" and y == 4:
            out["S31"] = s.copy()
            lock = cfg.floor_share * np.maximum(s, 0)
            s = s - lock
            floor33 = lock * (1 + cfg.y2_2031) ** 2 * (1 - fee_lock) ** 2  # announced floor is net of its own fee
            out["R31"] = s.copy()
        if y == 4 and cfg.floor_design != "one_date":
            out["R31"] = s.copy()                                          # unlocked money on 2031-01-01
        # fees: sleeve fee on the unlocked sleeve; ladder fee paid from the unlocked sleeve
        fee_now = fee_s * np.maximum(s, 0) + cfg.adv_fee_ladder * lad_val[:, y]
        w = cfg.barbell_eq_w if (cfg.floor_design == "barbell" and y >= 1) else None
        s = s * mix(y, w) - fee_now
        fees_paid = fees_paid + fee_now
    locked = floor33 + locked_extra
    breach = np.maximum(-s, 0)                                            # fees that ate into bought money
    out.update(floor33=floor33, locked33=locked, rest33=s, surplus=locked + s, short_face=short_face,
               topup=topup_paid, fees=fees_paid, breach=breach, cost27=cost27)
    if strategy == "P":                                                    # buy the unlocked share of the ladder in 2033
        rate33 = cfg.rate33_mean + cfg.rate33_sd * d["z33"]
        out["surplus"] = out["surplus"] - (1 - lock_frac) * annuity_due(np.maximum(rate33[:n], 0.0))
        out["short"] = np.maximum(-out["surplus"], 0)
    return out


def pct(x, ps=(5, 50, 95), k=1000):
    return [int(round(np.percentile(x, p) / k)) for p in ps]


def growth_2y(cfg):
    """2-year growth factor of the unlocked sleeve mix in 2031-2032 (net of the sleeve fee) under cfg."""
    d = draws(cfg)
    req, rbd = returns(cfg, d)
    eqw = np.array(cfg.eq_w if len(cfg.eq_w) == 6 else cfg.eq_w * 6)
    if cfg.floor_design == "barbell":
        eqw = np.full(6, cfg.barbell_eq_w)
    fee_s = cfg.fund_expense + cfg.adv_fee_sleeve
    g = np.ones(cfg.paths)
    for y in (4, 5):
        g = g * (1 + eqw[y] * req[:, y] + (1 - eqw[y]) * rbd[:, y]) * (1 - fee_s)
    return g


def range_eval(res, top_rule, plan_growth, contribution="all", share=1.0, k_excess=0.5):
    """2031 co-sponsor range [F, U] (2033 dollars) and where the 2033 contribution lands.
    top_rule: ('pct', p) -> U = F + R31 * p-th percentile of the planning model's 2-year growth;
              ('mult', m) -> U = m * F;  ('keep', None) -> U = F + R31 (the unlocked money keeps its 2031 value).
    contribution: 'all' (C = whole surplus), 'cap' (C = min(S, U)), 'share' (C = share*S, range scaled by share),
                  'share_cap' (C = share*min(S, U)), 'excess' (C = F + k*(S - F))."""
    F, R31, S = res["locked33"], res["R31"], res["surplus"]
    kind, p = top_rule
    if kind == "pct":
        U = F + R31 * np.percentile(plan_growth, p)
    elif kind == "mult":
        U = p * F
    else:
        U = F + R31
    if contribution == "all":
        C, lo, hi = S, F, U
    elif contribution == "cap":
        C, lo, hi = np.minimum(S, U), F, U
    elif contribution == "share":
        C, lo, hi = share * S, share * F, share * U
    elif contribution == "share_cap":
        C, lo, hi = share * np.minimum(S, U), share * F, share * U
    else:
        C, lo, hi = F + k_excess * (S - F), F, F + k_excess * (U - F)
    tol = 0.5                                                           # dollars (floating-point tolerance)
    below, above = C < lo - tol, C > hi + tol
    return dict(lo=lo, hi=hi, C=C, flex=S - C, p_below=below.mean(), p_above=above.mean(),
                p_within=1 - below.mean() - above.mean(), p_top=(C >= hi - tol).mean())


# ------------------------------------------------------------------ printed tables
def fmt(ps):
    return "/".join(f"${v}k" for v in ps)


def main():
    base = simulate(Cfg())
    print("REPRODUCTION CHECK (all switches off = verified strategy_mc.py)")
    print(f"  ladder exact-date cost ${LADDER_EXACT_2027:,.0f} (verified $292,264); Nov-15 STRIPS ${LADDER_STRIPS_2027:,.0f}"
          f" (S1 $294,387); forward zero 2027->2033 {FWD_ZERO_27_33 * 100:.2f}% (F-012 5.08%)")
    print(f"  2033 surplus p5/25/50/75/95 {fmt(pct(base['surplus'], (5, 25, 50, 75, 95)))} (verified $159k/$186k/$207k/$232k/$273k)")
    print(f"  2031 floor p5/50/95 {fmt(pct(base['floor33']))} (verified $127k/$165k/$217k)")
    g = simulate(Cfg(), "G")
    print(f"  growth-first miss {np.mean(g['surplus'] < 0) * 100:.1f}% (verified 3.2%); surplus {fmt(pct(g['surplus']))}")

    # (a) ------------------------------------------------------------------------------------------------
    print("\n(a) RATE RISK BEFORE THE JANUARY 2027 PURCHASE (longest rungs first; short rungs topped up from the 2028 "
          "deposit at 2028 prices)")
    print("  ladder | pre-purchase sd | P(cost>$300k) | mean gap if >0 | p95 gap | P(payments short) | surplus p5/p50/p95")
    for lad in ("exact", "strips"):
        for sd in (0.0, 0.37, 0.48):
            r = simulate(Cfg(ladder=lad, pre_rate_sd=sd))
            gp = r["gap27"]
            mg = gp[gp > 0].mean() if (gp > 0).any() else 0
            print(f"  {lad:6s} | {sd:.2f}pp | {np.mean(gp > 0) * 100:5.1f}% | ${mg:,.0f} | ${np.percentile(gp, 95):,.0f} | "
                  f"{np.mean(r['short_face'] > 0) * 100:.2f}% | {fmt(pct(r['surplus']))}")
    r = simulate(Cfg(ladder="strips", pre_rate_sd=0.37, markup=0.0025))
    print(f"  strips + 0.25% broker mark-up (ASSUMPTION), sd 0.37pp: P(cost>$300k) {np.mean(r['gap27'] > 0) * 100:.1f}%; "
          f"surplus {fmt(pct(r['surplus']))}")

    # (b) ------------------------------------------------------------------------------------------------
    print("\n(b) 2028 DEPOSIT SCENARIOS (lock-early; Nov-15 STRIPS; pre-purchase sd 0.37pp) vs growth-first")
    print("  scenario | L: P(short) | L: mean short if short | L: surplus p5/p50/p95 | G: miss")
    base_a = dict(ladder="strips", pre_rate_sd=0.37)
    scen = [("full $150k 2028", {}), ("$75k 2028", {"deposit": 75_000}), ("late: $150k in 2029", {"deposit_year": 2}),
            ("missing", {"deposit": 0.0}),
            ("cut to $75k in 25% of paths, rho 0.6", {"cut_prob": 0.25, "cut_frac": 0.5, "rho_deposit": 0.6}),
            ("cut to $0 in 25% of paths, rho 0.6", {"cut_prob": 0.25, "cut_frac": 1.0, "rho_deposit": 0.6}),
            ("cut to $0 in 25%, rho 0.6, stock-rate +0.65", {"cut_prob": 0.25, "cut_frac": 1.0, "rho_deposit": 0.6,
                                                          "rho_stock_rate": 0.65})]
    for name, kw in scen:
        r = simulate(Cfg(**base_a, **kw))
        gg = simulate(Cfg(**kw), "G")
        sh = r["short_face"]
        ms = sh[sh > 0].mean() if (sh > 0).any() else 0
        print(f"  {name:44s} | {np.mean(sh > 0) * 100:5.2f}% | ${ms:,.0f} | {fmt(pct(r['surplus']))} | "
              f"{np.mean(gg['surplus'] < 0) * 100:.1f}%")
    print("  correlation sensitivity (deposit cut to $0 in 25% of paths; L with (a) on):")
    for rho in (0.0, 0.3, 0.6, 0.9):
        r = simulate(Cfg(**base_a, cut_prob=0.25, cut_frac=1.0, rho_deposit=rho))
        gg = simulate(Cfg(cut_prob=0.25, cut_frac=1.0, rho_deposit=rho), "G")
        print(f"    rho {rho:.1f}: L P(short) {np.mean(r['short_face'] > 0) * 100:.2f}%, surplus {fmt(pct(r['surplus']))}; "
              f"G miss {np.mean(gg['surplus'] < 0) * 100:.1f}%")

    # (c) ------------------------------------------------------------------------------------------------
    print("\n(c) FEES (verified base otherwise). Fund expense 0.048% = 60% VT 0.06% + 40% VGSH 0.03%")
    print("  fund exp | advisory | on | surplus p5/p50/p95 | median change | P(fees dent the floor)")
    b50 = np.median(base["surplus"])
    for fe, adv, on in ((0.0, 0.0, "-"), (0.00048, 0.0, "-"), (0.00048, 0.005, "sleeve"), (0.00048, 0.01, "sleeve"),
                        (0.00048, 0.005, "sleeve+ladder"), (0.00048, 0.01, "sleeve+ladder")):
        kw = dict(fund_expense=fe, adv_fee_sleeve=adv if adv else 0.0,
                  adv_fee_ladder=adv if on == "sleeve+ladder" else 0.0)
        r = simulate(Cfg(**kw))
        print(f"  {fe * 100:.3f}% | {adv * 100:.1f}% | {on:13s} | {fmt(pct(r['surplus']))} | "
              f"{(np.median(r['surplus']) - b50) / 1000:+.1f}k | {np.mean(r['breach'] > 0) * 100:.2f}%")
    r = simulate(Cfg(deposit=0.0, adv_fee_ladder=0.01, adv_fee_sleeve=0.01))
    print(f"  stress: 1% on everything AND deposit missing: P(fees exceed the leftover money) "
          f"{np.mean(r['breach'] > 0) * 100:.0f}%, mean dent ${r['breach'][r['breach'] > 0].mean():,.0f}")

    # (d) ------------------------------------------------------------------------------------------------
    print("\n(d) ASSETS (what the sleeve holds)")
    print("  equity | sleeve bonds | surplus p5/p50/p95 | 2031 floor p5/p50/p95")
    for eq, bd in (("US_LC", "INT_TSY"), ("ACWI", "INT_TSY"), ("ACWI", "SHORT_GC"), ("ACWI", "SHORT_TSY_LOW"),
                   ("ACWI", "SHORT_TSY_FWD"), ("US_LC_VANGUARD", "INT_TSY"), ("US_LC_VANGUARD", "SHORT_TSY_FWD")):
        r = simulate(Cfg(eq_asset=eq, bd_asset=bd))
        print(f"  {eq:15s} | {bd:13s} | {fmt(pct(r['surplus']))} | {fmt(pct(r['floor33']))}")

    # (e) ------------------------------------------------------------------------------------------------
    print("\n(e) FAT TAILS (multivariate Student-t, same median and sd of log returns, clipped at 8 sd)")
    print("  tails | 1-yr equity p1/p5 | simulated arithmetic mean | surplus p1/p5/p50/p95 | floor p5")
    for tails, nu in (("normal", 5.0), ("t", 6.0), ("t", 4.0), ("t", 3.0)):
        cfg = Cfg(tails=tails, t_nu=nu)
        rq, _ = returns(cfg, draws(cfg))
        r = simulate(cfg)
        print(f"  {tails}{'' if tails == 'normal' else int(nu)} | {np.percentile(rq, 1) * 100:.1f}%/"
              f"{np.percentile(rq, 5) * 100:.1f}% | {rq.mean() * 100:.2f}% | "
              f"{fmt(pct(r['surplus'], (1, 5, 50, 95)))} | ${pct(r['floor33'], (5,))[0]}k")

    # (f) ------------------------------------------------------------------------------------------------
    print("\n(f) 2031 CO-SPONSOR RANGE: floor bought in a 2-year Treasury; top set by a rule in 2031")
    print("  contribution = whole surplus. P(below) is 0 because the floor is bought.")
    print("  floor share | top rule | median floor | median top | median width | P(within) | P(below) | P(above)")
    for a in (0.6, 0.7, 0.8, 0.9, 1.0):
        cfg = Cfg(floor_share=a)
        r = simulate(cfg)
        pg = growth_2y(cfg)
        for rule in (("pct", 80), ("pct", 90), ("keep", None), ("mult", 1.25)):
            e = range_eval(r, rule, pg)
            lab = {"pct": f"p{rule[1]}", "keep": "keep 2031 value", "mult": "1.25 x floor"}[rule[0]]
            print(f"  {a:.0%} | {lab:15s} | ${np.median(e['lo']) / 1000:.0f}k | ${np.median(e['hi']) / 1000:.0f}k | "
                  f"${np.median(e['hi'] - e['lo']) / 1000:.0f}k | {e['p_within'] * 100:.1f}% | "
                  f"{e['p_below'] * 100:.1f}% | {e['p_above'] * 100:.1f}%")
    print("  2031 2-year yield sensitivity (floor 80%): median floor at 3.0% / 4.0% / 4.81%: " + ", ".join(
        f"${np.median(simulate(Cfg(y2_2031=y))['floor33']) / 1000:.1f}k" for y in (0.03, 0.04, 0.0481)))
    print("  robustness: range set with the JPM-normal planning model (80% floor, p80 / p90 top); outcomes from:")
    plan = growth_2y(Cfg())
    for name, cfg in (("same model", Cfg()), ("Student-t nu=4", Cfg(tails="t", t_nu=4.0)),
                      ("Vanguard-midpoint equities", Cfg(eq_asset="US_LC_VANGUARD")),
                      ("equities 1.7pp/yr weaker", Cfg(eq_mu_shift=np.log(1.05) - np.log(1.067)))):
        r = simulate(cfg)
        e80, e90 = range_eval(r, ("pct", 80), plan), range_eval(r, ("pct", 90), plan)
        print(f"    {name:28s}: P(within) p80-top {e80['p_within'] * 100:.1f}%, p90-top {e90['p_within'] * 100:.1f}%")

    # (g) ------------------------------------------------------------------------------------------------
    print("\n(g) 2033 CONTRIBUTION RULE vs FLEXIBILITY KEPT (80% floor; top = p80 rule)")
    print("  rule | contribution p5/p50/p95 | flexibility p5/p50/p95 | flex share of surplus (median) | P(flex=0) | "
          "P(within range)")
    r = simulate(Cfg())
    for name, kw in (("give everything", dict(contribution="all")), ("cap at the top", dict(contribution="cap")),
                     ("90% of surplus", dict(contribution="share", share=0.9)),
                     ("80% of surplus", dict(contribution="share", share=0.8)),
                     ("80% of surplus, capped", dict(contribution="share_cap", share=0.8)),
                     ("floor + half the excess", dict(contribution="excess", k_excess=0.5))):
        e = range_eval(r, ("pct", 80), plan, **kw)
        fl = e["flex"]
        print(f"  {name:24s} | {fmt(pct(e['C']))} | {fmt(pct(fl))} | {np.median(fl / r['surplus']) * 100:.0f}% | "
              f"{np.mean(fl < 1) * 100:.0f}% | {e['p_within'] * 100:.1f}%")


if __name__ == "__main__":
    main()
