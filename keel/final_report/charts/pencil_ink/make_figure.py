"""Pencil and ink: one figure (Sat 28 Nov 2026).

Ink: what Laura has promised and holds Treasuries for from January 2028 (ten payments of $50,000 and the
building's first $95,000). Pencil: everything else she has in January 2033 (the contribution above $95,000
plus what she keeps), in four share-market worlds. Every figure is read from the model outputs below.
Run: python3 -I make_figure.py <out_dir>
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
NUM = HERE.parent.parent / "numbers"
rows = json.load(open(NUM / "results_range_rule_2026-11-17.json"))["exhibit3_rows"]

INK = 10 * 50_000 + 95_000          # ten payments + the bottom held since Jan 2028 (NUMBERS section 4)
def pencil(gift, kept_plus):        # contribution above the bottom + her flexibility incl. paid above the top
    return (gift - 95_000) + kept_plus

worlds = [
    ("Shares do very well", pencil(rows["shares_1in20_high_2028_31"]["gift"], rows["shares_1in20_high_2028_31"]["kept_plus"])),
    ("Shares earn 7.5% a year", pencil(rows["shares_median"]["gift"], rows["shares_median"]["kept_plus"])),
    # NUMBERS 8p: 40% below Jan 2028 cost at the move, then 7.5%: contribution $105,000, kept $10,229, above top $7,091
    ("Shares fall 40% before 2031", pencil(105_000, 10_229 + 7_091)),
    ("Shares become worthless", pencil(rows["vt_to_zero"]["gift"], rows["vt_to_zero"]["kept_plus"])),
]
for w in worlds: print(f"{w[0]:32s} pencil ${w[1]:,.0f}")

NAVY, GRAPH, GRAPH_LIGHT, TEXT, MUTED = "#26394D", "#6E6D69", "#D4D3CF", "#1F1F1F", "#6E6D69"
FONT = "'Times New Roman', Tinos, 'Liberation Serif', Times, serif"
W, H = 468, 138                      # points: 6.5 in x 2.39 in
x0, label_w = 2, 150
k = (W - x0 - label_w - 8) / (INK + max(p for _, p in worlds))
ink_w = INK * k
top, pitch, bar_h = 26, 24, 14
n = len(worlds)
block_top, block_h = top, n * pitch - (pitch - bar_h)
gap = 2
label_x = x0 + ink_w + gap + max(p for _, p in worlds) * k + 8

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}" font-family="{FONT}">')
s.append('<defs><pattern id="pencil" patternUnits="userSpaceOnUse" width="3" height="3" patternTransform="rotate(45)">'
         f'<rect width="3" height="3" fill="{GRAPH_LIGHT}"/><line x1="0" y1="0" x2="0" y2="3" stroke="{GRAPH}" stroke-width="0.9"/></pattern></defs>')
s.append(f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>')
# headers
s.append(f'<text x="{x0}" y="{top-12}" font-size="10.5" fill="{TEXT}" letter-spacing="1.2" font-weight="bold">INK</text>')
s.append(f'<text x="{x0+26}" y="{top-12}" font-size="10.5" fill="{MUTED}" font-style="italic">promised, and held in Treasuries from January 2028</text>')
px = x0 + ink_w + gap
s.append(f'<text x="{px:.2f}" y="{top-12}" font-size="10.5" fill="{TEXT}" letter-spacing="1.2" font-weight="bold">PENCIL</text>')
s.append(f'<text x="{px+50:.2f}" y="{top-12}" font-size="10.5" fill="{MUTED}" font-style="italic">not yet promised</text>')
# ink block: one block, the same in every world
s.append(f'<rect x="{x0}" y="{block_top}" width="{ink_w:.2f}" height="{block_h}" fill="{NAVY}"/>')
cy = block_top + block_h / 2
s.append(f'<text x="{x0+12}" y="{cy-3}" font-size="17" fill="#FFFFFF">$595,000</text>')
s.append(f'<text x="{x0+12}" y="{cy+13}" font-size="10.5" fill="#FFFFFF">ten payments of $50,000 and $95,000 for the building</text>')
# pencil strokes, one per world
for i, (name, p) in enumerate(worlds):
    y = top + i * pitch
    s.append(f'<rect x="{px:.2f}" y="{y}" width="{p*k:.2f}" height="{bar_h}" fill="url(#pencil)"/>')
    s.append(f'<text x="{label_x}" y="{y+bar_h-3.5}" font-size="11" fill="{TEXT}">{name}</text>')
# scale bar
sy = block_top + block_h + 16
s.append(f'<line x1="{x0}" y1="{sy}" x2="{x0+100000*k:.2f}" y2="{sy}" stroke="{MUTED}" stroke-width="0.8"/>')
for xx in (x0, x0 + 100000 * k):
    s.append(f'<line x1="{xx:.2f}" y1="{sy-3}" x2="{xx:.2f}" y2="{sy+3}" stroke="{MUTED}" stroke-width="0.8"/>')
s.append(f'<text x="{x0+100000*k+6:.2f}" y="{sy+3.5}" font-size="9.5" fill="{MUTED}">$100,000</text>')
s.append('</svg>')

out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE)
out.mkdir(parents=True, exist_ok=True)
(out / "pencil_and_ink.svg").write_text("\n".join(s))
print("wrote", out / "pencil_and_ink.svg", f"ink {ink_w:.1f}pt, label_x {label_x:.1f}")
