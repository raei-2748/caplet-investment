"""Render the Final Report's figure drafts (Tue 10 Nov 2026). Black and white, print-safe, Times New Roman metrics.

    python3 keel/final_report/exhibits/build_exhibits.py

Writes, next to this file:
  exhibit2_reserve.png / .svg   APA Figure 1 image (the operating reserve running down, NUMBERS 8h)
  exhibit3_range_candidate.png  a former Exhibit 3 candidate (the range forming), PLACEHOLDER numbers from NUMBERS 4

The tables (Exhibit 1 = APA Table 1, Exhibit 3 = APA Table 2) are built as real Word tables by
../template/build_template.py, and their PNG previews are cropped from the template PDF by that script.

Needs matplotlib (pip install matplotlib). Fonts: Times New Roman if installed, else Liberation Serif, which has the
same character widths (it is metrically compatible), so sizes and line breaks match.
"""
import os
import sys
from datetime import date

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import exhibit_data as D  # noqa: E402

# ---- house style for print (dataviz skill: two categories, two well-separated greys, hairline recessive axes) ----
INK = "#000000"
FUND = "#c8c8c8"      # iBond Treasury ETF: light grey
BOND = "#505050"      # Treasury bond: dark grey
RULE = "#9a9a9a"      # hairlines


def pick_font():
    names = {f.name for f in font_manager.fontManager.ttflist}
    for n in ("Times New Roman", "Liberation Serif", "Tinos"):
        if n in names:
            return n
    return "serif"


FONT = pick_font()
plt.rcParams.update({
    "font.family": FONT, "font.size": 11, "svg.fonttype": "none", "pdf.fonttype": 42,
    "axes.linewidth": 0.6, "xtick.major.width": 0.6, "xtick.minor.width": 0.4,
})


def yearfrac(y, m, d):
    start = date(y, 1, 1)
    return y + (date(y, m, d) - start).days / (date(y + 1, 1, 1) - start).days


def fmt_money(v):
    return f"${v:,.0f}"


def exhibit2(path_base, width_in=6.5, height_in=3.85):
    """APA Figure 1: which holding pays each year's $50,000, and when its cash arrives (NUMBERS 8h, MODEL).

    Rows are the ten payments, top to bottom. Each bar is one holding, held until its cash arrives; the black tick is
    the $50,000 payment on 1 January. The bars step down one a year (the reserve runs down by one holding a year) and
    the light-grey funds are gone after 2037 (composition moves from half funds to all bonds). The right column is
    what each holding pays above $50,000 if rates follow today's forwards (it pays exactly $50,000 in the world 3
    points lower, which is what the design is sized for)."""
    over = D.rung_over_50k()
    rungs = D.RESERVE_RUNGS
    n = len(rungs)

    fig = plt.figure(figsize=(width_in, height_in), dpi=300)
    # column geometry in figure fractions
    x_year, x_hold = 0.0, 0.105
    ax_left, ax_right = 0.355, 0.835
    x_over = 1.0
    top, bottom = 0.85, 0.20
    ax = fig.add_axes([ax_left, bottom, ax_right - ax_left, top - bottom])

    # the axis starts in January 2027, when every holding was bought, and is broken before 2033 so the ten
    # payments keep their room: a "2027" tick at the left edge and a cut through every bar say so
    x0, x1 = 2031.35, 2042.25
    x_cut = 2031.85
    ax.set_xlim(x0, x1)
    ax.set_ylim(n - 0.5, -0.5)  # first payment at the top

    row_h = 0.56
    for i, (yr, label, kind, (cy, cm, cd), months) in enumerate(rungs):
        end = yearfrac(cy, cm, cd)
        fill = FUND if kind == "iBond ETF" else BOND
        ax.add_patch(Rectangle((x0, i - row_h / 2), end - x0, row_h, facecolor=fill, edgecolor=INK, linewidth=0.5))
        _cut(ax, x_cut, i, row_h)
        # the payment: a black tick on 1 January of the payment year
        ax.plot([yr, yr], [i - 0.38, i + 0.38], color=INK, linewidth=2.0, solid_capstyle="butt")
        # where cash waits long enough to see, a hairline from payout to payment, labelled once
        if months >= 7:
            ax.plot([end, yr], [i, i], color=INK, linewidth=0.6, linestyle=(0, (1.5, 1.5)))
            ax.text(yr + 0.12, i, f"cash waits {months:g} months", va="center", ha="left", fontsize=9.5)
        # left text columns
        fig.text(x_year, _rowy(i, n, top, bottom), str(yr), ha="left", va="center", fontsize=11)
        fig.text(x_hold, _rowy(i, n, top, bottom), label, ha="left", va="center", fontsize=11)
        fig.text(x_over, _rowy(i, n, top, bottom), "+" + fmt_money(over[yr]), ha="right", va="center", fontsize=11)

    # recessive axis: years along the bottom, hairline year grid behind the bars
    ax.set_xticks([x0] + list(range(2033, 2043)))
    ax.set_xticklabels(["2027"] + [f"{y}" if y % 2 == 1 else "" for y in range(2033, 2043)], fontsize=10)
    _cut(ax, x_cut, n - 0.5, 0.0, on_axis=True)
    ax.set_xticks([], minor=True)
    for y in range(2033, 2043):
        ax.axvline(y, color=RULE, linewidth=0.35, zorder=0)
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(axis="x", length=3, pad=2)
    ax.set_xlabel("1 January of each year", fontsize=10, labelpad=2)

    # column heads (sentence case, as APA asks of table column heads)
    head_y = top + 0.05
    fig.text(x_year, head_y, "Year", ha="left", va="bottom", fontsize=11, fontweight="bold")
    fig.text(x_hold, head_y, "Paid from", ha="left", va="bottom", fontsize=11, fontweight="bold")
    fig.text((ax_left + ax_right) / 2, head_y, "Held from January 2027 until its cash arrives", ha="center", va="bottom",
             fontsize=11, fontweight="bold")
    fig.text(x_over, head_y, "Above $50,000", ha="right", va="bottom", fontsize=11, fontweight="bold")

    # legend inside the figure, below the axis (APA: legend within the figure's borders)
    handles = [
        Rectangle((0, 0), 1, 1, facecolor=FUND, edgecolor=INK, linewidth=0.5),
        Rectangle((0, 0), 1, 1, facecolor=BOND, edgecolor=INK, linewidth=0.5),
        Line2D([0], [0], color=INK, linewidth=2.0),
    ]
    labels = ["iBond Treasury ETF", "Treasury bond", "$50,000 paid on 1 January"]
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.0), ncol=3, frameon=False,
               fontsize=10, handlelength=1.4, columnspacing=1.4, handletextpad=0.5)

    for ext in ("png", "svg"):
        out = f"{path_base}.{ext}"
        fig.savefig(out, dpi=300 if ext == "png" else None, facecolor="white")
    plt.close(fig)
    if os.path.exists(f"{path_base}.svg"):
        _svg_font_fallback(f"{path_base}.svg")
    return f"{path_base}.png"


def _cut(ax, x, y, h, on_axis=False):
    """A broken-axis mark: a white slanted gap edged by two short ink lines, through a bar or on the bottom axis."""
    dx, gap = 0.09, 0.07
    half = 0.16 if on_axis else h / 2 + 0.06
    xs = [x - dx, x + dx]
    ys = [y + half, y - half]
    ax.fill([xs[0], xs[1], xs[1] + gap, xs[0] + gap], [ys[0], ys[1], ys[1], ys[0]], color="white", zorder=3,
            clip_on=False, linewidth=0)
    for off in (0.0, gap):
        ax.plot([xs[0] + off, xs[1] + off], ys, color=INK, linewidth=0.6, zorder=4, clip_on=False)


def _rowy(i, n, top, bottom):
    # centre of row i in figure fractions, matching the axes' inverted y range (n - 0.5 .. -0.5)
    h = (top - bottom) / n
    return top - h * (i + 0.5)


def _svg_font_fallback(path):
    with open(path) as fh:
        s = fh.read()
    s = s.replace(f"font-family: '{FONT}'", "font-family: 'Times New Roman', 'Liberation Serif', serif")
    s = s.replace(f"font-family:'{FONT}'", "font-family:'Times New Roman','Liberation Serif',serif")
    with open(path, "w") as fh:
        fh.write(s)


def exhibit3_range_candidate(path_base, width_in=6.5, height_in=2.6):
    """A former Exhibit 3 candidate, kept as a draft for the record: the 2031 range forming (bottom fixed in January
    2028, top fixed on the move day), with NUMBERS 4's house-model 1-in-20 bands as PLACEHOLDERS (another worker is
    recomputing them; SKELETON v2 replaced this candidate with a scenario table)."""
    R = D.RANGE_PLACEHOLDERS
    fig = plt.figure(figsize=(width_in, height_in), dpi=300)
    ax = fig.add_axes([0.12, 0.2, 0.62, 0.72])
    stages = ["Today\n(Nov 2026)", "Jan 2028:\nbottom bought", "Before the 2031\nmeetings: top owned"]
    xs = [0, 1, 2]
    lo_b, mid_b, hi_b = R["floor_payout_bottom"]
    lo_t, mid_t, hi_t = R["top"]
    # bottom: a band today, a point from Jan 2028
    ax.plot([0, 0], [lo_b, hi_b], color=BOND, linewidth=7, solid_capstyle="butt")
    ax.plot([1, 2], [mid_b, mid_b], color=BOND, linewidth=2.2)
    ax.scatter([1, 2], [mid_b, mid_b], color=BOND, s=28, zorder=3)
    # top: a band today and in 2028, a point once owned
    ax.plot([0.12, 0.12], [lo_t, hi_t], color=FUND, linewidth=7, solid_capstyle="butt")
    ax.plot([1.12, 1.12], [lo_t, hi_t], color=FUND, linewidth=7, solid_capstyle="butt")
    ax.scatter([2.12], [mid_t], color=INK, s=28, zorder=3, marker="D")
    ax.set_xticks(xs)
    ax.set_xticklabels(stages, fontsize=10)
    ax.set_xlim(-0.4, 2.5)
    ax.set_ylim(80000, 180000)
    ax.set_yticks([80000, 100000, 120000, 140000, 160000, 180000])
    ax.set_yticklabels([f"${v // 1000}k" for v in ax.get_yticks()], fontsize=10)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color=RULE, linewidth=0.35)
    ax.set_axisbelow(True)
    fig.text(0.77, 0.80, "Dark: the bottom (floor)", fontsize=10)
    fig.text(0.77, 0.70, "Light: the top (floor plus", fontsize=10)
    fig.text(0.77, 0.62, "the moved half of VT)", fontsize=10)
    fig.text(0.77, 0.50, "Bands: 1-in-20 each side", fontsize=10)
    fig.text(0.77, 0.30, "PLACEHOLDERS:", fontsize=10, fontweight="bold")
    fig.text(0.77, 0.22, "NUMBERS 4, being redone", fontsize=10, fontweight="bold")
    fig.text(0.77, 0.10, "Superseded (SKELETON v2)", fontsize=10)
    fig.savefig(f"{path_base}.png", dpi=300, facecolor="white")
    plt.close(fig)
    return f"{path_base}.png"


if __name__ == "__main__":
    print("font:", FONT)
    print(exhibit2(os.path.join(HERE, "exhibit2_reserve")))
    print(exhibit3_range_candidate(os.path.join(HERE, "exhibit3_range_candidate")))
