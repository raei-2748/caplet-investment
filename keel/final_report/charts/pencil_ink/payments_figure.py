"""Figure: sources of each $50,000 payment (Table 2 as a stacked column chart), same style as figure2_final.
Rows: NUMBERS 8h fee_and_margin.by_payment (also the draft's Table 2). Run: python3 -I payments_figure.py <out_dir>"""
import pathlib, sys
ROWS = [(2033, 47_101, 2_899), (2034, 46_497, 3_503), (2035, 45_911, 4_089), (2036, 45_204, 4_796), (2037, 44_268, 5_732),
        (2038, 43_195, 6_805), (2039, 43_061, 6_939), (2040, 43_043, 6_957), (2041, 42_180, 7_820), (2042, 42_469, 7_531)]
assert all(a + b == 50_000 for _, a, b in ROWS) and sum(a for _, a, _ in ROWS) == 442_929
F = "'Times New Roman', Tinos, 'Liberation Serif', Times, serif"
DARK, LIGHT, GRID, TXT = "#26394D", "#829887", "#EBEBEB", "#333333"
W, H = 468, 228
x0, x1, y0, y1, vmax = 60, 464, 196, 66, 50_000
y = lambda v: y0 - (y0 - y1) * v / vmax
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}" font-family="{F}" fill="{TXT}">',
     f'<rect width="{W}" height="{H}" fill="#fff"/>',
     '<text x="0" y="13" font-weight="bold" font-size="12">Figure 1</text>',
     '<text x="0" y="32" font-style="italic" font-size="12">Sources of Each $50,000 Operating Payment, 2033–2042</text>']
for t in range(0, vmax + 1, 10_000):
    s.append(f'<line x1="{x0}" x2="{x1}" y1="{y(t):.1f}" y2="{y(t):.1f}" stroke="{GRID if t else "#8C8C8C"}" stroke-width="{0.6 if t else 0.8}"/>')
    s.append(f'<text x="{x0-6}" y="{y(t)+3.5:.1f}" text-anchor="end" font-size="9.5">${t:,}</text>')
step = (x1 - x0) / len(ROWS); bw = 24
for i, (yr, own, extra) in enumerate(ROWS):
    c = x0 + step * (i + 0.5)
    s.append(f'<rect x="{c-bw/2:.1f}" y="{y(own):.1f}" width="{bw}" height="{y0-y(own):.1f}" fill="{DARK}"/>')
    s.append(f'<rect x="{c-bw/2:.1f}" y="{y(50_000):.1f}" width="{bw}" height="{y(own)-y(50_000)-1:.1f}" fill="{LIGHT}"/>')
    s.append(f'<text x="{c:.1f}" y="{y0+14}" text-anchor="middle" font-size="10">{yr}</text>')
lx = x1 - 205
s.append(f'<rect x="{lx}" y="48" width="8" height="8" fill="{DARK}"/><text x="{lx+12}" y="55.5" font-size="9.5">Original ladder</text>')
s.append(f'<rect x="{lx+82}" y="48" width="8" height="8" fill="{LIGHT}"/><text x="{lx+94}" y="55.5" font-size="9.5">Additional Treasuries (2028)</text>')
s.append('</svg>')
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent)
(out / "figure_payments.svg").write_text("".join(s))
