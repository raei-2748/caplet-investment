"""AX2_audit_checks.py - reproducible checks behind the AX2 audit corrections to D2, D4 and D10.

Agent AX2 (cluster auditor: equity, Taiwan/FX, compliance), insight_v1 run, 2026-09-28.
Audit file: research/insight_v1/phase_D/audit_markets_rules.md

What it does (plain English):
1. D4 (correction C2): how much the market still moves the 2033 facility money when Laura speaks in 2031, for
   different shares of the growth money locked as the 2031 floor (the model uses 80%, an open team parameter), at 50%
   and 60% sleeve equity. Compare with D4's FX spread (0.068) and construction spread (0.058).
2. D2 (correction C2): the forward earnings-yield yardstick treated the same way as D2's CAPE yardstick (add
   breakeven inflation to make it nominal) and against the 10-year TIPS real yield.
3. D2 (correction C10): D2's own sleeve simulation compared with a zero-spread Treasury-only sleeve at today's implied
   forward rates, instead of D2's "0% equity" row (which uses 4.8% with 2% volatility).
4. D10 (correction C3): D10's page-fit model re-run with whole lines per page (a line cannot split across a page
   break) and with a 27.6pt "double" line (Word's possible Times New Roman 12 setting).

Inputs (status labels):
- research/verified_2026-09-27/strategy_mc.py (VERIFIED-REPO-FILE model; JPM 2026 LTCMA inputs; lognormal returns and
  2y yield 4.81% in 2031 are ASSUMPTIONS as in that file). Median 2031 sleeve $187,630 from the D4 run (DERIVED).
- FX spread 0.068 and construction spread 0.058 (2-year log sd): D4 script outputs on live FRED DEXTAUS and DGBAS CCI,
  re-run 2026-09-28 (VERIFIED-PRIMARY inputs, derived).
- Forward P/E 19.2 (FactSet Earnings Insight 25 Sep 2026, re-read 2026-09-28, VERIFIED-PRIMARY); breakeven 2.34%
  (FRED T10YIE 2026-09-25, VERIFIED-PRIMARY); 10y TIPS 2.83% (F-008, VERIFIED-PRIMARY); CAPE 41.48 (multpl.com,
  SNIPPET-UNVERIFIED: secondary source read directly).
- Hurdle 5.23% (2028->2033) and ~4.5% for 2027 money: official 2026-09-25 curve (VERIFIED-REPO-FILE inputs,
  ASSUMPTION method as in D2). D2's simulation settings copied verbatim (ASSUMPTION).
- Page-fit: D10_ips_page_fit.py functions reused unchanged (Liberation Serif metrics, ASSUMPTION); 27.6pt line height
  is an ASSUMPTION (commonly measured Word behaviour for Times New Roman 12; also used by D9_ips_page_fit.py).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/AX2_audit_checks.py
"""
import importlib.util
import random
import sys

import numpy as np

sys.path.insert(0, "research/verified_2026-09-27")
import strategy_mc as smc  # noqa: E402

# ---------- 1. D4: 2031-view market spread by floor share ----------
print("1. D4: 2031-view market log sd by floor share f and sleeve equity w (FX 0.068, construction 0.058)")
rng = np.random.default_rng(smc.SEED + 1)
z1, z2 = rng.standard_normal((2, 200_000, 2))
ze, zb = z1, smc.RHO * z1 + np.sqrt(1 - smc.RHO ** 2) * z2
req = np.exp(smc.EQ[0] + smc.EQ[1] * ze) - 1
rbd = np.exp(smc.BD[0] + smc.BD[1] * zb) - 1
S31 = 187_630
for w in (0.5, 0.6):
    g2 = np.prod(1 + w * req + (1 - w) * rbd, axis=1)
    cells = []
    for f in (0.5, 0.6, 0.7, 0.8, 0.9):
        tot = f * S31 * (1 + smc.Y2) ** 2 + (1 - f) * S31 * g2
        cells.append(f"f={f:.0%}: {np.log(tot).std():.3f}")
    print(f"  w={w:.0%}: " + ", ".join(cells))

# ---------- 2. D2: valuation yardsticks like for like ----------
print("\n2. D2: forward earnings-yield yardstick on the same basis as the CAPE yardstick")
HURDLE = 0.0523
ep, be, tips = 1 / 19.2, 0.0234, 0.0283
print(f"  forward E/P {ep*100:.2f}% + breakeven {be*100:.2f}% = {(ep+be)*100:.2f}% -> premium {(ep+be-HURDLE)*100:+.2f} pts")
print(f"  forward E/P {ep*100:.2f}% vs 10y TIPS {tips*100:.2f}% -> real premium {(ep-tips)*100:+.2f} pts")
print(f"  CAPE E/P {100/41.48:.2f}% + breakeven = {(1/41.48+be)*100:.2f}% -> premium {(1/41.48+be-HURDLE)*100:+.2f} pts (as D2)")

# ---------- 3. D2: sleeve vs a zero-spread Treasury-only sleeve ----------
print("\n3. D2: sleeve outcomes vs a zero-spread Treasury-only sleeve (D2 run() settings copied verbatim)")
PATHS, SEED = 200_000, 20260927
SLEEVE_2027, DEPOSIT_2028, Y2 = 300_000 - 292_264, 150_000, 0.0481
BOND_C, BOND_V = 0.048, 0.020


def ln(c, v):
    s = np.sqrt(np.log(1 + (v / (1 + c)) ** 2))
    return np.log(1 + c), s


def run(ec, ev, w, f=0.8):
    r = np.random.default_rng(SEED)
    me, se = ln(ec, ev)
    mb, sb = ln(BOND_C, BOND_V)
    e = r.standard_normal((PATHS, 6))
    b = r.standard_normal((PATHS, 6))
    re, rb = np.exp(me + se * e) - 1, np.exp(mb + sb * b) - 1
    s = np.full(PATHS, float(SLEEVE_2027))
    for y in range(4):
        if y == 1:
            s += DEPOSIT_2028
        s *= 1 + w * re[:, y] + (1 - w) * rb[:, y]
    fl, rest = f * s * (1 + Y2) ** 2, (1 - f) * s
    for y in (4, 5):
        rest *= 1 + w * re[:, y] + (1 - w) * rb[:, y]
    return fl + rest


locked = (SLEEVE_2027 * 1.045 + DEPOSIT_2028) * (1 + HURDLE) ** 5
print(f"  Treasury-only sleeve at today's implied rates: ~${locked/1e3:.1f}k on 2033-01-01 (no spread; ASSUMPTION)")
for name, c in (("JPM AC World 7.00%", 0.07), ("Vanguard blend mid 5.08%", 0.0508), ("Vanguard U.S. low 4.2%", 0.042)):
    for w in (0.5, 0.6):
        t = run(c, 0.1678, w)
        print(f"  {name:26s} w={w:.0%}: median ${np.median(t)/1e3:.1f}k; P(below Treasury-only) {np.mean(t < locked)*100:.0f}%")

# ---------- 4. D10: page fit with whole lines and a 27.6pt line ----------
print("\n4. D10: page-fit with whole lines per page (and Word's possible 27.6pt double line)")
spec = importlib.util.spec_from_file_location("pf", "research/insight_v1/scripts/D10_ips_page_fit.py")
pf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pf)


def page_use(page, n_par, space_after, line):
    r = random.Random(20260928)
    text_w, text_h = (page[0] - 2) * 72, (page[1] - 2) * 72
    lpp = int(text_h // line)
    used = []
    for _ in range(400):
        start = r.randrange(0, len(pf.words) - 600)
        seq = pf.words[start:start + 550]
        pitch, ips = seq[:50], seq[50:]
        cuts = sorted(r.sample(range(40, 460), n_par - 1))
        pars = [ips[a:b] for a, b in zip([0] + cuts, cuts + [500])]
        lines = 2 + pf.wrap(pitch, text_w, 0) + sum(pf.wrap(p, text_w, 0) for p in pars)
        lines += space_after * (n_par + 1) / line
        used.append(lines / (2 * lpp))
    used.sort()
    return lpp, used[200], used[380]


for line, label in ((pf.LINE, "26.58pt (D10 model)"), (27.6, "27.6pt (Word, possible)")):
    for pname, page in (("Letter", (8.5, 11.0)), ("A4", (8.27, 11.69))):
        for n_par, sa in ((5, 0.0), (7, 0.0), (7, 8.0)):
            lpp, p50, p95 = page_use(page, n_par, sa, line)
            print(f"  {label:24s} {pname:6s} paras {n_par} after {sa:.0f}pt: {lpp} lines/page; "
                  f"median {p50*100:5.1f}% (p95 {p95*100:5.1f}%) of two pages")
