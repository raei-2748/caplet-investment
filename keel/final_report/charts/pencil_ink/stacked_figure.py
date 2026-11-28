"""Figure 2 in the stacked form ChatGPT suggested (Sat 28 Nov 2026): floor plus the part above it, dashed floor line.
Numbers: results_range_rule_2026-11-17.json exhibit3_rows and NUMBERS 8p. Run: python3 -I stacked_figure.py <out_dir>"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
r = json.load(open(HERE.parent.parent / "numbers" / "results_range_rule_2026-11-17.json"))["exhibit3_rows"]
D = [("Total loss", r["vt_to_zero"]["bottom"], r["vt_to_zero"]["top"]),
     ("−40%", 95_000, 105_000),
     ("7.5% a year", r["shares_median"]["bottom"], r["shares_median"]["top"]),
     ("1-in-20 high", r["shares_1in20_high_2028_31"]["bottom"], r["shares_1in20_high_2028_31"]["top"])]
F = "'Times New Roman', Tinos, 'Liberation Serif', Times, serif"
DARK, LIGHT, GRID, TXT = "#26394D", "#829887", "#EBEBEB", "#333333"
W, H = 468, 246
x0, x1, y0, y1, vmax = 52, 464, 196, 66, 150_000
y = lambda v: y0 - (y0 - y1) * v / vmax
k = lambda v: f"${v/1000:,.0f}k"
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}" font-family="{F}" fill="{TXT}">',
     f'<rect width="{W}" height="{H}" fill="#fff"/>',
     '<text x="0" y="13" font-weight="bold" font-size="12">Figure 2</text>',
     '<text x="0" y="32" font-style="italic" font-size="12">Range Laura Could State to Co-Sponsors in 2031, by VT Outcome</text>']
for t in range(0, vmax + 1, 50_000):
    s.append(f'<line x1="{x0}" x2="{x1}" y1="{y(t):.1f}" y2="{y(t):.1f}" stroke="{GRID if t else "#8C8C8C"}" stroke-width="{0.6 if t else 0.8}"/>')
    s.append(f'<text x="{x0-6}" y="{y(t)+3.5:.1f}" text-anchor="end" font-size="10">{k(t)}</text>')
step = (x1 - x0) / len(D); bw = 58
for i, (lab, b, t) in enumerate(D):
    c = x0 + step * (i + 0.5)
    s.append(f'<rect x="{c-bw/2:.1f}" y="{y(b):.1f}" width="{bw}" height="{y0-y(b):.1f}" fill="{DARK}"/>')
    if t > b:
        s.append(f'<rect x="{c-bw/2:.1f}" y="{y(t):.1f}" width="{bw}" height="{y(b)-y(t)-1:.1f}" fill="{LIGHT}"/>')
    s.append(f'<text x="{c:.1f}" y="{(y(b)+y0)/2+4:.1f}" text-anchor="middle" font-size="11" fill="#fff">{k(b)}</text>')
    s.append(f'<text x="{c:.1f}" y="{y(t)-5:.1f}" text-anchor="middle" font-size="11.5" font-weight="bold">{k(t)}</text>')
    s.append(f'<text x="{c:.1f}" y="{y0+14}" text-anchor="middle" font-size="10.5">{lab}</text>')
s.append(f'<line x1="{x0}" x2="{x1}" y1="{y(95_000):.1f}" y2="{y(95_000):.1f}" stroke="{LIGHT}" stroke-width="0.9" stroke-dasharray="4 3"/>')
s.append(f'<text x="{(x0+x1)/2:.1f}" y="{y0+30}" text-anchor="middle" font-size="9.5">Return on VT (world shares), 2028–2031</text>')
lx = x1 - 168
s.append(f'<rect x="{lx}" y="48" width="8" height="8" fill="{DARK}"/><text x="{lx+12}" y="55.5" font-size="9.5">Protected floor</text>')
s.append(f'<rect x="{lx+80}" y="48" width="8" height="8" fill="{LIGHT}"/><text x="{lx+92}" y="55.5" font-size="9.5">Potential upside</text>')
s.append('</svg>')
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE)
(out / "figure2_stacked.svg").write_text("".join(s))
