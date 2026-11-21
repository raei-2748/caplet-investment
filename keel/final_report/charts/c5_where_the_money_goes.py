"""c5: where Laura's money goes, from each deposit to its use (Fri 20 Nov 2026, Final Report analysis line). Keel.

Run from the repo root:  python3 -I keel/final_report/charts/c5_where_the_money_goes.py   (a few seconds)

A test render, not a built exhibit: the design, the figure table and the test against Caplet's version 61 questions are
in MONEY_PICTURE_2026-11-20.md beside this script. Writes c5_where_the_money_goes.png (192 dpi) and .svg (text kept as
text) into keel/final_report/charts/.

Every dollar figure is read from the number engine's results files (the same files NUMBERS.md quotes) and checked
against the register's printed figure before anything is drawn; the script stops on any mismatch. Sums printed in the
picture that the register does not print itself (the first deposit's split by lane) are Keel arithmetic on NUMBERS
section 1's rung table, and are checked to add up.

Print style (../exhibits/specs.md section 0): Times New Roman metrics (Liberation Serif), black and two greys, no colour
carrying meaning, 10 pt at printed size, 6.5 in wide. Treasuries are grey, shares are hatched, uses are white boxes: the
words in each mark carry its identity, never the tone alone. No pencil or ink in the picture (CONCEIT V2.2: the conceit
is said beside an exhibit, never in it).
"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Rectangle, FancyBboxPatch  # noqa: E402

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
NUM = HERE.parent / "numbers"

INK = "#000000"
DARK = "#505050"
LIGHT = "#c8c8c8"
GUIDE = "#b4b4b4"
HATCH = "#7a7a7a"
DPI = 192
FS = 10


def pick_font():
    names = {f.name for f in font_manager.fontManager.ttflist}
    for n in ("Times New Roman", "Liberation Serif", "Tinos"):
        if n in names:
            return n
    return "serif"


plt.rcParams.update({"font.family": pick_font(), "font.size": FS, "svg.fonttype": "none", "pdf.fonttype": 42,
                     "text.parse_math": False, "hatch.linewidth": 0.5, "hatch.color": HATCH})

# ===================================================================================== figures, checked
CHECKS = []


def check(name, got, want, tol=0.5):
    ok = abs(got - want) <= tol
    CHECKS.append((name, got, want, ok))
    if not ok:
        raise SystemExit(f"FAIL {name}: got {got}, register says {want}")


def load(name):
    return json.loads((NUM / name).read_text())


R = load("results_2026-11-17.json")
TOP = load("results_topup_2026-11-17.json")
RET = load("results_returns_2026-11-17.json")
RES = load("results_reserve_2026-11-17.json")
ONE = load("results_one_fund_2026-11-19.json")

rungs = R["C3"]["rungs"]
ten_cost = R["C3"]["ten_instruments_with_fund_fees"]
check("NUMBERS 1: the ten instruments with the funds' fee", ten_cost, 302_287)
check("NUMBERS 1: the 2033 rung (IBTM) at today's forwards", rungs["2033"]["cost"], 37_908)
unbought = ten_cost - 300_000                                   # NUMBERS 1: $2,287 in 1 Jan 2027 money
check("NUMBERS 1: the part of the ten still unbought in Jan 2027", unbought, 2_287)
ibtm_lot_2027 = rungs["2033"]["cost"] - unbought                # Keel arithmetic: the 2033 lot bought in Jan 2027
nine = sum(rungs[str(y)]["cost"] for y in range(2034, 2043))    # Keel arithmetic: the other nine rungs
check("Keel arithmetic: the first deposit's two lanes add to $300,000", ibtm_lot_2027 + nine, 300_000, 0.01)
four_funds = sum(rungs[str(y)]["cost"] for y in range(2034, 2038))
five_bonds = sum(rungs[str(y)]["cost"] for y in range(2038, 2043))
check("Keel arithmetic: the nine split into four funds and five bonds", four_funds + five_bonds, nine, 0.01)

topup = TOP["ten_still_lack_jan2028"]
extra = TOP["for_no_interest_jan2028"]
first_slice = TOP["topup_jan2028"]
check("NUMBERS 2 / WORDS: the top-up (Jan 2028 money)", topup, 2_388)
check("NUMBERS 2: the extra Treasuries (Jan 2028 money)", extra, 36_774)
check("NUMBERS 2: the first $39,162 of the 2028 deposit", first_slice, 39_162)

c = R["plan"]["H_plain"]["central"]
rule = R["plan"]["H_plain"]["central_rule"]
floor_money = c["R"] - c["vt28"]
check("NUMBERS 4: floor money (Jan 2028)", floor_money, 81_244)
check("NUMBERS 4: VT bought (Jan 2028)", c["vt28"], 29_594)
check("The 2028 deposit adds up: top-up + extra + floor + VT", topup + extra + floor_money + c["vt28"], 150_000, 0.01)
check("NUMBERS 4: VT on 1 Jan 2031 (shares at 7.5% a year)", c["vt31"], 36_698)
moved = c["vt31"] / 2
check("NUMBERS 8w: the shares moved into the late-2032 fund", moved, 18_349)
check("NUMBERS 4: floor payout, late 2032", c["floor"], 102_365)
check("NUMBERS 4: the moved half, paid late 2032", c["moved"], 20_138)
check("NUMBERS 4: what the late-2032 fund pays on its two purchases", c["top"], 122_503)
check("NUMBERS 4: bottom Laura states", rule["bottom"], 95_000, 0)
check("NUMBERS 4: top Laura states", rule["top"], 115_000, 0)
check("NUMBERS 4: the 2033 contribution", rule["gift"], 115_000, 0)
check("NUMBERS 4: paid above the top (the excess)", rule["excess"], 7_503)
check("NUMBERS 4: the half kept on 1 Jan 2033", c["kept33"], 21_179)
check("NUMBERS 4: half kept plus anything above the top", rule["kept_plus_excess"], 28_682)
check("NUMBERS 8w: the 2033 payment's own lot pays at today's forwards", ONE["promises"]["own_lot_pays_forwards"], 50_000)
check("NUMBERS 8k: the extra Treasuries' money back, 1 Jan 2033 money", RET["joint_stress_forwards"]["backstop_left_jan2033"], 46_566)
check("NUMBERS 8h: the same money on 1 Jan 2042, nominal", RES["base_left_after_2042"], 75_934)
check("NUMBERS 8w: promises resting on the late-2032 fund after the move", ONE["promises"]["on_ibtm"], 165_000, 0)


def money(x):
    return f"${x:,.0f}"


# ===================================================================================== the picture
W, H = 6.5, 3.76
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

# Event columns, not to scale: Jan 2027, Jan 2028, Jan 2031, mid-Dec 2032; then the uses column.
X27, X28, X31, X32 = 0.48, 1.25, 2.45, 3.32
UX0, UX1 = 3.46, 6.48
PAD = 0.07
TEXTS = []   # (artist, container or None): checked after drawing for fit and overlap


def rect(x0, y0, x1, y1, kind):
    if kind == "treasury":
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=LIGHT, edgecolor=INK, lw=0.5, zorder=2))
    elif kind == "shares":
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor="white", edgecolor=HATCH, hatch="////", lw=0,
                               zorder=2))
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor="none", edgecolor=INK, lw=0.5, zorder=3))
    elif kind == "use":
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor="white", edgecolor=INK, lw=0.8, zorder=2))
    elif kind == "deposit":
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=DARK, edgecolor="none", zorder=3))
    elif kind == "group":
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor="none", edgecolor=INK, lw=0.6,
                               ls=(0, (2, 2)), zorder=1))
    return (x0, y0, x1, y1)


def t(x, y, s, ha="left", va="center", bold=False, white_bg=False, box=None, z=5):
    bb = dict(facecolor="white", edgecolor="none", pad=0.8) if white_bg else None
    a = ax.text(x, y, s, ha=ha, va=va, fontsize=FS, fontweight="bold" if bold else "normal", bbox=bb, zorder=z,
                linespacing=1.12)
    TEXTS.append((a, box))
    return a


def line(pts, dashed=False):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=INK, lw=0.7, ls=(0, (3, 2)) if dashed else "-", zorder=4, solid_capstyle="butt")


def arrow(pts, dashed=False):
    """A polyline through pts with an arrowhead at the last point."""
    if len(pts) > 2:
        line(pts[:-1], dashed)
    ax.annotate("", xy=pts[-1], xytext=pts[-2], zorder=4,
                arrowprops=dict(arrowstyle="-|>", lw=0.7, color=INK, mutation_scale=7, shrinkA=0, shrinkB=0,
                                linestyle=(0, (3, 2)) if dashed else "-"))


def mid(lane):
    return (lane[0] + lane[1]) / 2


# --- header: the dates and what happens on them
HY = H - 0.05
for x, head, body in ((X27, "Jan 2027", "$300,000\ndeposited"),
                      (X28, "Jan 2028", "$150,000\ndeposited"),
                      (X31, "Jan 2031", "half the shares move,\nthen she tells co-sponsors\n"
                       f"{money(rule['bottom'])} to {money(rule['top'])}")):
    t(x, HY, head, ha="center", va="top", bold=True)
    t(x, HY - 0.165, body, ha="center", va="top")
t(UX0, HY, "Dec 2032 to 2042", va="top", bold=True)
t(UX0, HY - 0.165, "where the money goes, on today's figures:\nTreasury yields of 6 Nov 2026; shares 7.5% a year",
  va="top")

# --- lanes, from the top down (y0, y1)
L1 = (2.68, 3.04)     # Treasuries for 2034-2042, first deposit
L1b = (2.32, 2.60)    # the extra Treasuries, second deposit
L2a = (1.86, 2.20)    # late-2032 fund: the 2033 payment's lot (first deposit, completed by the top-up)
L2b = (1.46, 1.80)    # late-2032 fund: the floor (second deposit)
L2c = (1.06, 1.40)    # late-2032 fund: the half of the shares moved in Jan 2031
L3 = (0.28, 0.64)     # world shares (VT), second deposit
L3h = (0.28, 0.46)    # the half kept, after the move

for x in (X27, X28, X31, X32):   # date guides
    ax.plot([x, x], [0.24, HY - 0.68], color=GUIDE, lw=0.5, ls=(0, (1, 2)), zorder=1)

# the late-2032 fund: one dashed outline round its three purchases, its name inside on the left
G = rect(0.02, L2c[0] - 0.05, X32 + 0.035, L2a[1] + 0.05, "group")
t(0.07, mid((L2c[0], L2b[1])), "The late-2032\nTreasury fund\n(IBTM): one\nfund, bought\nthree times",
  box=(0.02, L2c[0] - 0.05, X28 - 0.04, L2b[1]))

# deposits: dark bars at their dates, across the lanes they feed
rect(X27 - 0.035, L2a[0], X27 + 0.035, L1[1], "deposit")
rect(X28 - 0.035, L3[0], X28 + 0.035, L1b[1], "deposit")

# L1: the Treasuries for 2034-2042
b = rect(X27 + 0.035, L1[0], X32, L1[1], "treasury")
t(X27 + 0.035 + PAD, mid(L1), f"{money(nine)}: Treasuries for 2034\u20132042\n"
  "(four iBonds funds, then five Treasury bonds)", box=b)
# L1b: the extra Treasuries
b = rect(X28 + 0.035, L1b[0], X32, L1b[1], "treasury")
t(X28 + 0.035 + PAD, mid(L1b), f"{money(extra)}: extra Treasuries", box=b)

# L2: the late-2032 fund, bought three times
rect(X27 + 0.035, L2a[0], X32, L2a[1], "treasury")
t(X27 + 0.035 + PAD, mid(L2a), money(ibtm_lot_2027), box=(X27, L2a[0], X28 - 0.035, L2a[1]))
t(X28 + 0.035 + PAD, mid(L2a), f"+ {money(topup)} top-up: together\nthey pay the 2033 payment",
  box=(X28, L2a[0], X32, L2a[1]))
b = rect(X28 + 0.035, L2b[0], X32, L2b[1], "treasury")
t(X28 + 0.035 + PAD, mid(L2b), f"{money(floor_money)}: the floor;\npays {money(c['floor'])} in Dec 2032", box=b)
b = rect(X31, L2c[0], X32, L2c[1], "treasury")
t(X31 + PAD, mid(L2c), f"{money(moved)};\npays {money(c['moved'])}", box=b)

# L3: world shares
b = rect(X28 + 0.035, L3[0], X31, L3[1], "shares")
t(X28 + 0.035 + PAD, mid(L3), f"{money(c['vt28'])}, growing\n7.5% a year", white_bg=True, box=b)
b = rect(X31, L3h[0], X32, L3h[1], "shares")
t(X31 + PAD, mid(L3h), "other half", white_bg=True, box=b)
t(0.07, mid(L3), "World share\nfund (VT)", box=(0, L3[0] - 0.05, X28 - 0.04, L3[1] + 0.05))
# the 2031 move: half the shares into the late-2032 fund
arrow([(X31 + 0.10, L3[1]), (X31 + 0.10, L2c[0])])
t(X31 + 0.02, mid((L3[1], G[1])), f"half of {money(c['vt31'])}\nmoves", ha="right", box=(X28 + 0.05, L3[1], X31 + 0.05, G[1]))

# --- uses
# U1: the ten payments (and which holding pays which)
U1 = rect(UX0, L1[0] - 0.04, UX1, L1[1] + 0.13, "use")
t(UX0 + PAD, U1[3] - 0.05, "Ten payments of $50,000, each 1 January", va="top", box=U1)
sq_w, sq_g, sq_h = 0.264, 0.024, 0.22
sq_y0 = U1[1] + 0.05
for i in range(10):
    x0 = UX0 + PAD + i * (sq_w + sq_g)
    rect(x0, sq_y0, x0 + sq_w, sq_y0 + sq_h, "treasury")
    t(x0 + sq_w / 2, sq_y0 + sq_h / 2, f"{2033 + i}"[2:], ha="center", box=(x0, sq_y0, x0 + sq_w, sq_y0 + sq_h))
# the nine Treasuries feed the payments at the title's height, above square 33, which has its own arrow
arrow([(X32, L1[1] - 0.07), (UX0, L1[1] - 0.07)])
# the 2033 payment comes from the late-2032 fund: up a channel left of U1b, into square 33's foot
CH = UX0 + PAD + sq_w / 2
arrow([(X32, mid(L2a)), (CH, mid(L2a)), (CH, sq_y0)])
# U1b: the extra Treasuries' job, and what comes back; its arrow hops the channel
U1b = rect(CH + 0.18, L2a[0] - 0.02, UX1, U1[1] - 0.06, "use")
t(U1b[0] + PAD, mid((U1b[1], U1b[3])),
  "Extra Treasuries fill any gap in the ten if\ncash waiting earns nothing. If rates hold\n"
  "they are never needed, and all of it is hers\n"
  f"by 2042: {money(RET['joint_stress_forwards']['backstop_left_jan2033'])}, valued at 1 January 2033",
  box=U1b)
line([(X32, mid(L1b)), (CH - 0.05, mid(L1b))], dashed=True)
arrow([(CH + 0.05, mid(L1b)), (U1b[0], mid(L1b))], dashed=True)

# U2: the facility contribution
U2 = rect(UX0, L2c[0] + 0.12, UX1, L2b[1] + 0.02, "use")
t(UX0 + PAD, U2[3] - 0.05,
  f"Facility contribution: {money(rule['top'])}, the top\n"
  f"  the bottom, {money(rule['bottom'])}: held in Treasuries since 2028\n"
  f"  the rest, {money(rule['top'] - rule['bottom'])}: from the shares moved in 2031\n"
  "Each end is counted below the expected payout", va="top", box=U2)
# the floor and the moved shares both feed the contribution: a joiner from each lot's end
JX = X32 + 0.075
line([(X32, mid(L2b)), (JX, mid(L2b)), (JX, mid(L2c)), (X32, mid(L2c))])
arrow([(JX, mid((L2b[0], L2c[1]))), (UX0, mid((L2b[0], L2c[1])))])

# U3: her flexibility
# WORDS l.28: $28,682 is her flexibility PLUS anything above the top, never "her flexibility" alone
U3 = rect(UX0, 0.20, UX1, 0.86, "use")
t(UX0 + PAD, U3[3] - 0.05,
  f"Her flexibility, {money(c['kept33'])} in shares, and {money(rule['excess'])}\n"
  f"paid above the top: {money(rule['kept_plus_excess'])} in 2033, promised to\n"
  "no one, for building costs that overrun, a stronger\nTaiwan dollar or a co-sponsor falling short",
  va="top", box=U3)
arrow([(X32, mid(L3h)), (UX0, mid(L3h))])
arrow([(UX1 - 0.30, U2[1]), (UX1 - 0.30, U3[3])])
t(UX1 - 0.36, mid((U3[3], U2[1])), f"{money(rule['excess'])} above the top", ha="right",
  box=(UX0, U3[3], UX1, U2[1]))

# --- key and basis
KY = 0.09
rect(0.03, KY - 0.06, 0.25, KY + 0.06, "treasury")
t(0.30, KY, "Treasuries: held to the end, they pay out on set dates")
rect(3.40, KY - 0.06, 3.62, KY + 0.06, "shares")
t(3.67, KY, "shares: value moves")
SWATCHES = [(0.03, KY - 0.06, 0.25, KY + 0.06), (3.40, KY - 0.06, 3.62, KY + 0.06)]
t(UX1, KY, "Not drawn to scale", ha="right")

# --- collision check: every label inside its box, no two labels overlapping, nothing off the page
fig.canvas.draw()
rend = fig.canvas.get_renderer()
inv = ax.transData.inverted()
boxes = []
for a, box in TEXTS:
    bb = a.get_window_extent(rend)
    (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
    boxes.append((x0, y0, x1, y1, a.get_text().split("\n")[0]))
    if x0 < 0 or x1 > W or y0 < 0 or y1 > H:
        print("OFF PAGE:", a.get_text()[:40])
    if box is not None and (x0 < box[0] - 0.005 or x1 > box[2] + 0.005 or y0 < box[1] - 0.005 or y1 > box[3] + 0.005):
        print(f"DOES NOT FIT ({x1 - box[2]:+.2f} in right, {box[1] - y0:+.2f} in below): {a.get_text()[:50]!r}")
for sx0, sy0, sx1, sy1 in SWATCHES:
    for x0, y0, x1, y1, name in boxes:
        if x0 < sx1 and sx0 < x1 and y0 < sy1 and sy0 < y1:
            print(f"OVERLAPS A KEY SWATCH: {name!r}")
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        a, b = boxes[i], boxes[j]
        if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
            print(f"OVERLAP: {a[4]!r} / {b[4]!r}")

fig.savefig(HERE / "c5_where_the_money_goes.png", dpi=DPI)
fig.savefig(HERE / "c5_where_the_money_goes.svg")
plt.close(fig)

# page cost in Wharton's format (../exhibits/specs.md section 0: a double-spaced line is 27.6 pt; a Letter page of text
# holds 23.5 of them); number, title and the blank line after are whole lines, as the specs count them
LINE_IN = 27.6 / 72
img = H / LINE_IN
print(f"image {W} x {H} in = {img:.1f} lines; with number, one-line title and blank line {img + 3:.1f} lines "
      f"({(img + 3) / 23.5:.2f} page); two-line title {img + 4:.1f} ({(img + 4) / 23.5:.2f} page); "
      f"prose displaced about {round((img + 3) * 14, -1):.0f} words")
print(f"{len(CHECKS)} checks, {sum(ok for *_, ok in CHECKS)} PASS")
for n, g, w, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + n, round(g, 2), round(w, 2))
