"""Test renders for the Final Report's exhibits: first designs, Mon 16 Nov 2026 (Final Report Day 9). Keel.

Run from the repo root:  python3 -I keel/final_report/charts/build_charts.py   (about 20 seconds)

Writes PNG previews (192 dpi, "2x") and SVGs (text kept as text) into keel/final_report/charts/, and checks every
plotted figure against the number register (NUMBERS.md) or the engine's own results files before drawing; it stops on
any mismatch. These are test versions for comparison with the four built exhibits in ../exhibits/ (which stay the
working versions); DESIGNS.md says which form wins for each need and why.

Print style (exhibit rules, ../exhibits/specs.md section 0): Times New Roman metrics (Liberation Serif), black plus two
greys, no colour carrying meaning, at least 10 pt at printed size, hairline rules, no vertical rules in tables.
Dataviz skill, applied to print: form first; emphasis (the plan in black, the alternatives in grey); one axis; thin
marks; selective direct labels instead of a legend; identity carried by words, never by tone alone. No hover layer: the
medium is a printed PDF, so every value a reader needs is printed or in the prose.

Charts:
  c1  What $300,000 bought on every day since 2000 (NUMBERS 8e): a full-width strip and a word-sized sparkline
  c2  What more shares would buy (NUMBERS 8n): two panels on one row set, the stated range and all the money left
  c3  When each part of the money becomes owned in Treasuries (NUMBERS 2, 4, 8h): a dated timeline
  c4  Table 2's five markets as a dot-range chart (NUMBERS 8i), to compare with the table
  c5  Ten promises each 1-in-100 unsafe: an icon array (dropped Mon 16 Nov after the cold aha test; arithmetic kept)
"""
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
FR = HERE.parent
NUM = FR / "numbers"
sys.path.insert(0, str(NUM))
import engine as E  # noqa: E402

INK = "#000000"
DARK = "#505050"      # the second tone (as Figure 1's bonds)
LIGHT = "#c8c8c8"     # the third tone (as Figure 1's funds)
RULE = "#9a9a9a"
DPI = 192


def pick_font():
    names = {f.name for f in font_manager.fontManager.ttflist}
    for n in ("Times New Roman", "Liberation Serif", "Tinos"):
        if n in names:
            return n
    return "serif"


plt.rcParams.update({"font.family": pick_font(), "font.size": 10, "svg.fonttype": "none", "pdf.fonttype": 42,
                     "axes.linewidth": 0.6, "text.parse_math": False, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
                     "xtick.major.size": 3, "ytick.major.size": 0, "axes.edgecolor": INK})
CHECKS = []


def check(name, got, want, tol=0.5):
    ok = abs(got - want) <= tol
    CHECKS.append((name, got, want, ok))
    if not ok:
        raise SystemExit(f"FAIL {name}: got {got}, register says {want}")


def tnr_svg(path):
    """Mon 23 Nov (Wharton: 12-pt Times New Roman; exhibits/build_exhibits.py's _svg_font_fallback): the SVG names
    Times New Roman first, with Liberation Serif (the same metrics, the build's stand-in) as its fallback."""
    s = path.read_text()
    s = re.sub(r"font-family: ?'Liberation Serif'", "font-family: 'Times New Roman', 'Liberation Serif', serif", s)
    path.write_text(s)


def save(fig, stem):
    fig.savefig(HERE / f"{stem}.png", dpi=DPI)
    fig.savefig(HERE / f"{stem}.svg")
    tnr_svg(HERE / f"{stem}.svg")
    plt.close(fig)


def money(x):
    return f"${x:,.0f}"


def clean(ax, left=False):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if not left:
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="y", length=0)


# ================================================================================================= c1 cost history
FRED = E.ROOT / "archive/rab/data/fred"
TEN = {"DGS1MO": 1 / 12, "DGS3MO": .25, "DGS6MO": .5, "DGS1": 1, "DGS2": 2, "DGS3": 3, "DGS5": 5, "DGS7": 7,
       "DGS10": 10, "DGS20": 20, "DGS30": 30}
days = {}
for col, t in TEN.items():
    for r in csv.DictReader(open(FRED / f"{col}.csv")):
        if r[col] in ("", ".") or r["observation_date"] >= "2026-01-01":
            continue
        days.setdefault(r["observation_date"], {})[t] = float(r[col])
for fn in ("daily-treasury-rates_2026-10-23.csv", "daily-treasury-rates_2026-11-06.csv"):
    for r in csv.DictReader(open(E.ROOT / "competition/official_market_data" / fn)):
        d = datetime.strptime(r["Date"], "%m/%d/%Y").date().isoformat()
        par = {}
        for k, t in E.TENORS.items():
            try:
                par[t] = float(r[k])
            except (KeyError, ValueError):
                pass
        days[d] = par
keys, costs = [], []
for d in sorted(days):
    if d < "2000-01-01":
        continue
    par = days[d]
    if 1 not in par or 10 not in par or not ({20, 30} & set(par)):
        continue
    keys.append(d)
    costs.append(E.ladder_cost(E.Curve(par)))
c = np.array(costs)
kd = dict(zip(keys, costs))
ph = json.load(open(NUM / "results_price_history.json"))["daily"]
check("8e dearest since 2000 (4 Aug 2020)", kd["2020-08-04"], ph["dearest_since_2000"]["cost"], 1)
check("8e days since 2000", len(keys), ph["days_since_2000"], 0)
check("8e days under $300,000 since 2000", int((c <= 300_000).sum()), ph["days_since_2000_under_300k"], 0)
check("8e share of days since 2000 over $300,000 (nine in ten)", round(float((c > 300_000).mean()), 2), 0.89, 0.006)
check("8e 19 Oct 2023 (NUMBERS: $299,293)", kd["2023-10-19"], 299_293, 1)
check("8e 5 Oct 2026 (NUMBERS: $288,333)", kd["2026-10-05"], 288_333, 1)
check("8e 7 Oct 2026 (NUMBERS: $288,889)", kd["2026-10-07"], 288_889, 1)
x = np.array([datetime.fromisoformat(k) for k in keys])

# c1a: the strip, full text width, short
fig, ax = plt.subplots(figsize=(6.5, 2.2))
fig.subplots_adjust(left=0.10, right=0.76, top=0.95, bottom=0.14)
under = c <= 300_000
ax.plot(x, c / 1000, color="#8a8a8a", lw=0.7)
ax.scatter(x[under], c[under] / 1000, s=5, color=INK, zorder=3, lw=0)
ax.axhline(300, color=INK, lw=0.8)
ax.set_ylim(240, 480)
ax.set_yticks([250, 300, 350, 400, 450])
ax.set_yticklabels(["$250k", "$300k", "$350k", "$400k", "$450k"])
ax.tick_params(axis="y", length=3, width=0.6)
clean(ax, left=True)
ax.set_xlim(datetime(2000, 1, 1), datetime(2026, 12, 31))
ax.set_xticks([datetime(y, 1, 1) for y in (2000, 2005, 2010, 2015, 2020, 2025)])
ax.set_xticklabels(["2000", "2005", "2010", "2015", "2020", "2025"])
ax.annotate("4 Aug 2020: $470,217", xy=(datetime(2020, 8, 4), 470.2), xytext=(datetime(2010, 1, 1), 466),
            fontsize=10, va="center", arrowprops=dict(arrowstyle="-", lw=0.5, color=INK))
ax.annotate("19 Oct 2023: the one day from August 2007\nto August 2026 when $300,000 was enough", xy=(datetime(2023, 10, 19), 299.3),
            xytext=(datetime(2005, 6, 1), 262), fontsize=10, va="center",
            arrowprops=dict(arrowstyle="-", lw=0.5, color=INK))
ax.plot([datetime(2026, 10, 5)], [288.3], "o", ms=3, color=INK)
ax.text(1.02, (300 - 240) / 240 + 0.07, "$300,000: the\nfirst deposit", transform=ax.transAxes, fontsize=10,
        va="center", ha="left")
ax.text(1.02, (288.3 - 240) / 240 - 0.10, "5 Oct 2026: the\ncheapest since\nMay 2002", transform=ax.transAxes,
        fontsize=10, va="center", ha="left")
save(fig, "c1a_cost_history_strip")

# Mon 23 Nov (NUMBERS 8e, corrected Sun 22 Nov evening; card Q210 row 27; AHA_REGISTER row 3): "from August 2007",
# never "June 2007" (the engine finds 13 more closes under $300,000 from 2 to 19 July 2007)
# c1d: c1a drawn from a zero baseline (card Q14b row 4: the SEC handbook, p. 51, "avoid graphics that start at a
# non-zero baseline"), to set beside c1a for the Mon 23 Nov fresh reader
fig, ax = plt.subplots(figsize=(6.5, 2.6))
fig.subplots_adjust(left=0.10, right=0.76, top=0.95, bottom=0.12)
ax.plot(x, c / 1000, color="#8a8a8a", lw=0.7)
ax.scatter(x[under], c[under] / 1000, s=5, color=INK, zorder=3, lw=0)
ax.axhline(300, color=INK, lw=0.8)
ax.set_ylim(0, 500)
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.set_yticklabels(["$0", "$100k", "$200k", "$300k", "$400k", "$500k"])
ax.tick_params(axis="y", length=3, width=0.6)
clean(ax, left=True)
ax.set_xlim(datetime(2000, 1, 1), datetime(2026, 12, 31))
ax.set_xticks([datetime(y, 1, 1) for y in (2000, 2005, 2010, 2015, 2020, 2025)])
ax.set_xticklabels(["2000", "2005", "2010", "2015", "2020", "2025"])
ax.annotate("4 Aug 2020: $470,217", xy=(datetime(2020, 8, 4), 470.2), xytext=(datetime(2010, 1, 1), 480),
            fontsize=10, va="center", arrowprops=dict(arrowstyle="-", lw=0.5, color=INK))
ax.annotate("19 Oct 2023: the one day from August 2007\nto August 2026 when $300,000 was enough",
            xy=(datetime(2023, 10, 19), 299.3), xytext=(datetime(2006, 1, 1), 150), fontsize=10, va="center",
            arrowprops=dict(arrowstyle="-", lw=0.5, color=INK))
ax.plot([datetime(2026, 10, 5)], [288.3], "o", ms=3, color=INK)
ax.text(1.02, 300 / 500 + 0.07, "$300,000: the\nfirst deposit", transform=ax.transAxes, fontsize=10,
        va="center", ha="left")
ax.text(1.02, 288.3 / 500 - 0.12, "5 Oct 2026: the\ncheapest since\nMay 2002", transform=ax.transAxes,
        fontsize=10, va="center", ha="left")
save(fig, "c1d_cost_history_zero_base")

# c1b: the sparkline, word-sized (Tufte 2006): 0.95 in x 0.16 in at print size
fig = plt.figure(figsize=(0.95, 0.16))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, c, color=INK, lw=0.5)
ax.axhline(300_000, color=DARK, lw=0.4)
ax.plot([x[-1]], [c[-1]], "o", ms=1.6, color=INK)
ax.plot([datetime(2020, 8, 4)], [kd["2020-08-04"]], "o", ms=1.6, color=INK)
ax.set_xlim(x[0], x[-1])
ax.set_ylim(c.min() - 8000, c.max() + 8000)
ax.axis("off")
save(fig, "c1b_cost_sparkline")

# the sparkline in a sentence, 12 pt, as the report would set it (one line of text)
fig = plt.figure(figsize=(6.5, 0.32))
t1 = "From 2000 to 2026 the ten cost"
fig.text(0.0, 0.5, t1, fontsize=12, va="center")
sx = 0.335
spark = plt.imread(HERE / "c1b_cost_sparkline.png")
iax = fig.add_axes([sx, 0.18, 0.95 / 6.5, 0.16 / 0.32 * 1.0])
iax.imshow(spark)
iax.axis("off")
fig.text(sx + 0.95 / 6.5 + 0.008, 0.5, "more than $300,000 on nine days in ten.", fontsize=12,
         va="center")
save(fig, "c1c_sparkline_in_text")

# ================================================================================================= c2 share split
ss = json.load(open(NUM / "results_share_split_2026-11-15.json"))
order = ["A", "B", "C", "D", "E"]
names = {"A": "All to the floor", "B": "The plan", "C": "Half and half", "D": "Three-quarters shares",
         "E": "All shares"}
reg = {  # NUMBERS 8n, simulated futures table: stated range; all money median / 1-in-20 low (to $1,000)
    "A": (130_000, 130_000, 186_000, 159_000), "B": (95_000, 115_000, 191_000, 159_000),
    "C": (65_000, 100_000, 194_000, 154_000), "D": (30_000, 85_000, 198_000, 145_000),
    "E": (0, 70_000, 202_000, 134_000)}
vals = {}
for k in order:
    o = ss["options"][k]
    lo, hi = o["central_today"]["stated_bottom"], o["central_today"]["stated_top"]
    p5, p50, _ = o["house"]["all_money_p5_p50_p95"]
    check(f"8n {k} stated bottom", lo, reg[k][0], 0)
    check(f"8n {k} stated top", hi, reg[k][1], 0)
    check(f"8n {k} all money median ($1,000)", round(p50, -3), reg[k][2], 0)
    check(f"8n {k} all money 1-in-20 low ($1,000)", round(p5, -3), reg[k][3], 0)
    vals[k] = (lo, hi, p50, p5)

flex_reg = {"A": 9_000, "B": 29_000, "C": 47_000, "D": 66_000, "E": 84_000}   # NUMBERS 8n, median flexibility
flexm = {}
for k in order:
    f50 = ss["options"][k]["house"]["flexibility_p5_p50_p95"][1]
    check(f"8n {k} flexibility median ($1,000)", round(f50, -3), flex_reg[k], 0)
    flexm[k] = f50
b50, b5 = vals["B"][2], vals["B"][3]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.5, 2.6), sharey=True, gridspec_kw={"width_ratios": [1.15, 1]})
fig.subplots_adjust(left=0.25, right=0.86, top=0.80, bottom=0.25, wspace=0.10)
ys = np.arange(len(order))[::-1]
for y, k in zip(ys, order):
    lo, hi, p50, p5 = vals[k]
    col = INK if k == "B" else DARK
    lw = 2.4 if k == "B" else 1.4
    bold = "bold" if k == "B" else "normal"
    if hi > lo:
        a1.plot([lo / 1000, hi / 1000], [y, y], color=col, lw=lw, solid_capstyle="butt")
    a1.plot([lo / 1000, hi / 1000], [y, y], "|", color=col, ms=7, mew=1.0)
    a1.text(hi / 1000 + 4, y, f"${lo / 1000:.0f}k-${hi / 1000:.0f}k" if hi > lo else f"${hi / 1000:.0f}k",
            fontsize=10, va="center", fontweight=bold)
    if k != "B":
        dm, dl = (p50 - b50) / 1000, (p5 - b5) / 1000
        a2.plot([dl, dm], [y, y], color=col, lw=0.8)
        a2.plot([dm], [y], "o", ms=5, color=col)
        a2.plot([dl], [y], "o", ms=5, mfc="white", mec=col, mew=0.9)
    else:
        a2.text(0.8, y, "the plan", fontsize=10, va="center", fontweight="bold")
    a2.text(1.04, y, f"${flexm[k] / 1000:.0f}k", transform=a2.get_yaxis_transform(), fontsize=10, va="center",
            ha="left", fontweight=bold)
a2.axvline(0, color=INK, lw=0.6)
for a in (a1, a2):
    clean(a)
    a.set_ylim(-0.6, len(order) - 0.4)
a1.set_yticks(ys)
a1.set_yticklabels([names[k] for k in order])
for t in a1.get_yticklabels():
    if t.get_text() == "The plan":
        t.set_fontweight("bold")
a1.set_xlim(0, 160)
a1.set_xticks([0, 50, 100, 150])
a1.set_xticklabels(["$0", "$50k", "$100k", "$150k"])
a2.set_xlim(-30, 15)
a2.set_xticks([-25, -10, 0, 10])
a2.set_xticklabels(["-$25k", "-$10k", "0", "+$10k"])
a1.set_title("The range she can state in 2031", fontsize=10, loc="left")
a2.set_title("All left to her, against the plan", fontsize=10, loc="left")
a2.text(1.04, len(order) - 0.3, "Her flexibility\n(median)", transform=a2.get_yaxis_transform(), fontsize=10,
        va="bottom", ha="left")
fig.text(0.02, 0.05, "Middle, against the plan: filled dot, median of 200,000 simulated futures; open, a bad 1-in-20."
         , fontsize=10, va="center")
save(fig, "c2_more_shares")

# ================================================================================================= c3 ink timeline
# Rows: what is owned in Treasuries, and from when (NUMBERS 2, 4, 8h; CONCEIT V2.2's dates).
rows = [
    ("Ten payments, $500,000", [(2027.0, 2028.0, "most", "89%"), (2028.0, 2033.0, "all", "all owned")],
     "paid 2033-2042"),
    ("Bottom of the range, $95,000", [(2027.0, 2028.0, "none", ""), (2028.0, 2033.0, "all", "owned")],
     "paid Jan 2033"),
    ("Top of the range, $115,000", [(2027.0, 2031.0, "none", "moves with shares"), (2031.0, 2033.0, "all", "owned")],
     "paid Jan 2033"),
    ("Her flexibility", [(2027.0, 2033.0, "none", "never promised to anyone")], "hers"),
]
fig, ax = plt.subplots(figsize=(6.5, 1.95))
fig.subplots_adjust(left=0.33, right=0.84, top=0.80, bottom=0.17)
for i, (lab, segs, end) in enumerate(rows):
    y = len(rows) - 1 - i
    for a, b, kind, txt in segs:
        if kind == "all":
            ax.add_patch(Rectangle((a, y - 0.28), b - a, 0.56, color=INK, lw=0))
            ax.text((a + b) / 2, y, txt, color="white", fontsize=10, ha="center", va="center")
        elif kind == "most":
            ax.add_patch(Rectangle((a, y - 0.28), b - a, 0.56, color=DARK, lw=0))
            ax.text((a + b) / 2, y, txt, color="white", fontsize=10, ha="center", va="center")
        else:
            ax.add_patch(Rectangle((a, y - 0.28), b - a, 0.56, facecolor="white", edgecolor=DARK, lw=0.6,
                                   hatch="////"))
            if txt:
                ax.text((a + b) / 2, y, txt, color=INK, fontsize=10, ha="center", va="center",
                        bbox=dict(facecolor="white", edgecolor="none", pad=1.0))
    ax.text(2033.1, y, end, fontsize=10, va="center")
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows][::-1])
ax.set_xlim(2027, 2033)
ax.set_ylim(-0.6, len(rows) - 0.4)
ax.set_xticks([2027, 2028, 2029, 2030, 2031, 2032, 2033])
ax.set_xticklabels(["Jan 2027", "2028", "2029", "2030", "2031", "2032", "2033"])
clean(ax)
fig.text(0.0, 0.93, "Solid: owned in Treasuries that will pay it (grey: 89%, if waiting cash earns nothing). "
         "Hatched: rests on markets.", fontsize=10, va="center")
res = json.load(open(NUM / "results_reserve_2026-11-15.json"))
own0 = sum(r["own_holding_pays"] for r in res["fee"])
check("8h own Treasuries pay at no interest (Figure 1: $444,080)", own0, 444_080, 1)
check("share of the $500,000 owned from Jan 2027 (89%)", round(own0 / 500_000 * 100), 89, 0)
save(fig, "c3_when_owned")

# ================================================================================================= c4 Table 2 as dots
# Mon 23 Nov (card Q210 row 30; ATTACKS D7): Table 2's history rows are the 5th and 95th percentiles of 585 overlapping
# starting months, never "1-in-20", so the rows read here and printed below take Table 2's new names
t2 = (FR / "exhibits/tables.md").read_text()
worlds = []
for line in t2.splitlines():
    m = re.match(r"\| (Today's market rates|Replay from 2006: shares fall|Rates 3 points lower from Jan 2027|"
                 r"Replay from 2007: rates fall early|Inflation: rates 3 points higher|"
                 r"&nbsp;&nbsp;Median) \| All paid \| \$([\d,]+) \| \$([\d,]+) \| "
                 r"\$([\d,]+) \|", line)
    if m:
        worlds.append((m.group(1).replace("&nbsp;", ""), *(int(g.replace(",", "")) for g in m.groups()[1:])))
# Mon 23 Nov, later (the lead's decisions 2 and 3): Table 2's history is the median alone, and the report's Figure 2
# is drawn by exhibits/build_exhibits.py (figure2); c4 stays here as the candidate it was, on the same rows
assert len(worlds) == 6, worlds
check("8i today's range bottom", worlds[0][1], 95_000, 0)
check("8i today's range top", worlds[0][2], 115_000, 0)
# Mon 23 Nov: one history row (the median), so the axis starts under it and the figure is 0.45 in shorter
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.5, 2.25), sharey=True, gridspec_kw={"width_ratios": [1.5, 1]})
fig.subplots_adjust(left=0.33, right=0.97, top=0.81, bottom=0.14, wspace=0.10)
ys = [8.4, 7.4, 6.4, 5.4, 4.4, 2.4]
for y, (w, lo, hi, flex) in zip(ys, worlds):
    col = INK if w == "Today's market rates" else DARK
    a1.plot([lo / 1000, hi / 1000], [y, y], color=col, lw=2.0, solid_capstyle="butt")
    a1.plot([lo / 1000, hi / 1000], [y, y], "|", color=col, ms=7, mew=1.0)
    a1.text(hi / 1000 + 2, y, f"${lo / 1000:.0f}k-${hi / 1000:.0f}k", fontsize=10, va="center")
    a2.plot([flex / 1000], [y], "o", ms=4.5, color=col)
    a2.text(flex / 1000 + 2.5, y, f"${flex / 1000:.1f}k", fontsize=10, va="center")
a1.axhline(3.75, color=RULE, lw=0.5)
# Mon 16 Nov night: WORDS's names, as Table 2 now prints them ("Today's market rates", "every starting month since
# 1962"; coherence reader 6, L2), so the row names above are read from tables.md under the new first name
a1.text(52, 3.25, "Every starting month since 1962:", fontsize=10, style="italic", va="center")
a2.axhline(3.75, color=RULE, lw=0.5)
a1.set_yticks(ys)
a1.set_yticklabels([w for w, *_ in worlds])
for a in (a1, a2):
    clean(a)
    a.set_ylim(1.7, 9)
a1.set_xlim(50, 175)
a1.set_xticks([50, 100, 150])
a1.set_xticklabels(["$50k", "$100k", "$150k"])
a2.set_xlim(0, 70)
a2.set_xticks([0, 20, 40, 60])
a2.set_xticklabels(["$0", "$20k", "$40k", "$60k"])
a1.set_title("Stated range in 2031", fontsize=10, loc="left")
fig.text(0.0, 0.96, "The ten payments are paid in full in every row.", fontsize=10, va="center")
a2.set_title("Her flexibility, Jan 2033", fontsize=10, loc="left")
save(fig, "c4_table2_as_dots")

# ================================================================================================= c5 icon array
# Dropped Mon 16 Nov after the cold aha test (research/goldmine/aha_test_2026-11-16/RESULTS.md): the ten black squares
# read as "the ten payments", and the words did the job better for numerate judges. The arithmetic stays checked.
p_one = 1 - 0.99 ** 10
check("ten 1-in-100 promises: chance one or more fails (per cent)", round(p_one * 100, 1), 9.6, 0.05)

# ================================================================================================= report
print(f"{len(CHECKS)} checks, {sum(ok for *_, ok in CHECKS)} PASS")
for n, g, w, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + n, round(g, 2), round(w, 2))
