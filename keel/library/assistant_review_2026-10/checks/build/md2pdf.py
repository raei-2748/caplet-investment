"""Render the team brief Markdown to a styled A4 PDF (Chromium via Playwright), with embedded fonts.
Usage: md2pdf.py input.md output.pdf "Footer text" """
import asyncio
import re
import sys

import markdown
from playwright.async_api import async_playwright

SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__))  # inputs, fonts/ and outputs sit next to this script
F = f'file://{SP}/fonts'
src, out, foot = sys.argv[1], sys.argv[2], sys.argv[3]
md = open(src).read()

def prep(text):
    item = re.compile(r'^\s*([-*+]|\d+\.)\s+')
    out, prev = [], ''
    for line in text.split('\n'):
        if line.startswith(' '):
            n = len(line) - len(line.lstrip(' '))
            if n % 4:
                line = ' ' * (n * 2) + line.lstrip(' ')
        if item.match(line) and prev.strip() and not item.match(prev) and not prev.lstrip().startswith('|'):
            out.append('')
        out.append(line)
        prev = line
    text = '\n'.join(out)
    parts = re.split(r'(`[^`]*`)', text)
    parts = [p if p.startswith('`') else re.sub(r'(?<![`\w])([\w./\[\]-]*/\*[\w.*-]*)', r'`\1`', p) for p in parts]
    return ''.join(parts)

md = prep(md)
body = markdown.markdown(md, extensions=['tables', 'sane_lists', 'toc'], output_format='html5')
body = body.replace('<table>', '<div class="tw"><table>').replace('</table>', '</table></div>')

CSS = f'''
@font-face {{ font-family: "Public Sans"; src: url("{F}/PublicSans-normal-400.woff2") format("woff2"); font-weight: 100 900; font-style: normal; }}
@font-face {{ font-family: "Public Sans"; src: url("{F}/PublicSans-italic-400.woff2") format("woff2"); font-weight: 100 900; font-style: italic; }}
@font-face {{ font-family: "Source Serif 4"; src: url("{F}/SourceSerif4-normal-700.woff2") format("woff2"); font-weight: 200 900; font-style: normal; }}
@font-face {{ font-family: "IBM Plex Mono"; src: url("{F}/IBMPlexMono-normal-400.woff2") format("woff2"); font-weight: 400; font-style: normal; }}
:root {{ --ink:#16201b; --ink2:#44514a; --ink3:#66726b; --rule:#d3d9d4; --wash:#eef2ef; --accent:#1d5c47; }}
@page {{ size: A4; margin: 13mm 15mm 15mm; }}
* {{ box-sizing: border-box; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ margin: 0; font-family: "Public Sans", Arial, sans-serif; font-size: 9pt; line-height: 1.42; color: var(--ink); }}
h1 {{ font-family: "Source Serif 4", Georgia, serif; font-size: 19pt; line-height: 1.12; margin: 0 0 4pt; }}
h1 + p {{ color: var(--ink3); font-size: 8.4pt; padding-bottom: 6pt; border-bottom: 1.5pt solid var(--accent); margin-bottom: 8pt; }}
h2 {{ font-family: "Source Serif 4", Georgia, serif; font-size: 13pt; margin: 14pt 0 4pt; break-after: avoid; color: var(--ink); }}
h3 {{ font-size: 10pt; margin: 9pt 0 3pt; break-after: avoid; color: var(--accent); }}
h4 {{ font-size: 9.2pt; margin: 7pt 0 2pt; break-after: avoid; }}
p {{ margin: 0 0 5pt; }}
ul, ol {{ margin: 0 0 6pt; padding-left: 15pt; }}
li {{ margin: 0 0 2.5pt; }}
li > ul, li > ol {{ margin-top: 2pt; margin-bottom: 2pt; }}
strong {{ font-weight: 700; }}
code {{ font-family: "IBM Plex Mono", monospace; font-size: 7.9pt; background: var(--wash); padding: 0 2pt; border-radius: 2pt; overflow-wrap: anywhere; }}
blockquote {{ margin: 4pt 0 6pt; padding: 3pt 9pt; border-left: 3pt solid var(--accent); background: #f5f8f6; color: var(--ink2); }}
.tw {{ margin: 3pt 0 8pt; }}
table {{ width: 100%; border-collapse: collapse; font-size: 8.3pt; line-height: 1.35; }}
tr {{ break-inside: avoid; }}
th {{ text-align: left; font-size: 7.8pt; color: var(--ink2); padding: 3pt 5pt; border-bottom: 1pt solid var(--ink3); vertical-align: bottom; }}
td {{ padding: 3pt 5pt; border-bottom: 0.6pt solid var(--rule); vertical-align: top; }}
hr {{ border: 0; border-top: 0.8pt solid var(--rule); margin: 10pt 0; }}
a {{ color: var(--accent); text-decoration: none; }}
'''
HTML = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Caplet Team Brief</title><style>{CSS}</style></head><body>{body}</body></html>'
html_path = out.replace('.pdf', '.html')
open(html_path, 'w').write(HTML)

FOOT = ('<div style="width:100%;font-family:Arial,sans-serif;font-size:7.3px;color:#66726b;padding:0 15mm;display:flex;'
        f'justify-content:space-between"><span>{foot}</span><span>Page <span class="pageNumber"></span> of '
        '<span class="totalPages"></span></span></div>')


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = await b.new_page()
        await pg.goto(f'file://{html_path}', wait_until='load')
        await pg.evaluate('document.fonts.ready')
        await pg.pdf(path=out, format='A4', print_background=True, display_header_footer=True,
                     header_template='<div></div>', footer_template=FOOT,
                     margin={'top': '13mm', 'bottom': '15mm', 'left': '15mm', 'right': '15mm'})
        await b.close()

asyncio.run(main())
print('written', out)
