import html, re, sys
from html.parser import HTMLParser
class T(HTMLParser):
    def __init__(s): super().__init__(); s.out=[]; s.skip=0; s.links=[]; s.href=None
    def handle_starttag(s, t, a):
        if t in ('script','style','noscript','svg'): s.skip+=1
        if t=='a':
            s.href=dict(a).get('href')
        if t in ('p','div','br','li','h1','h2','h3','h4','h5','tr','section','article','summary','details'): s.out.append('\n')
    def handle_endtag(s, t):
        if t in ('script','style','noscript','svg') and s.skip: s.skip-=1
        if t=='a': s.href=None
    def handle_data(s, d):
        if s.skip: return
        s.out.append(d)
        if s.href and d.strip(): s.links.append((d.strip(), s.href))
for src in sys.argv[1:]:
    raw=open(src,'rb').read().decode('utf-8','replace'); t=T(); t.feed(raw)
    txt=html.unescape(''.join(t.out)); txt='\n'.join(re.sub(r'[ \t]+',' ',l).strip() for l in txt.split('\n')); txt=re.sub(r'\n{2,}','\n',txt)
    out=src.replace('/raw/','/').replace('.html','.txt')
    open(out,'w').write(txt)
    open(out.replace('.txt','.links.txt'),'w').write('\n'.join(f'{h} | {a[:120]}' for a,h in t.links))
    print(out, len(txt.split('\n')))
