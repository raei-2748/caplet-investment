import json,sys
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_BREAK, WD_LINE_SPACING
d=json.load(open(sys.argv[1]))['content']
want=sys.argv[2]
FORCE=sys.argv[4] if len(sys.argv)>4 else None
def find(tabs):
    for t in tabs:
        if t['tabProperties']['tabId']==want: return t
        r=find(t.get('childTabs',[]))
        if r: return r
dt=find(d['tabs'])['documentTab']
named={s['namedStyleType']:s for s in dt.get('namedStyles',{}).get('styles',[])}
doc=Document()
sec=doc.sections[0]; sec.page_width=Pt(612); sec.page_height=Pt(792)
for m in ('left_margin','right_margin','top_margin','bottom_margin'): setattr(sec,m,Inches(1))
st=doc.styles['Normal']; st.font.name='Times New Roman'; st.font.size=Pt(12)
pf=st.paragraph_format; pf.space_after=Pt(0); pf.space_before=Pt(0)
def mag(x,default=None):
    return x.get('magnitude',default) if isinstance(x,dict) else default
def para(p, container, cell=False):
    ps=p.get('paragraphStyle',{})
    nst=ps.get('namedStyleType','NORMAL_TEXT')
    base=named.get(nst,{}).get('paragraphStyle',{})
    ls=ps.get('lineSpacing', base.get('lineSpacing',100))
    np=container.add_paragraph()
    if ps.get('pageBreakBefore') or (FORCE and ''.join(e.get('textRun',{}).get('content','') for e in p.get('elements',[])).startswith(FORCE)): np.paragraph_format.page_break_before=True
    f=np.paragraph_format
    f.line_spacing=(ls or 100)/100
    f.space_before=Pt(mag(ps.get('spaceAbove', base.get('spaceAbove')),0) or 0)
    f.space_after=Pt(mag(ps.get('spaceBelow', base.get('spaceBelow')),0) or 0)
    ind=mag(ps.get('indentFirstLine', base.get('indentFirstLine')),0)
    if ind: f.first_line_indent=Pt(ind)
    al=ps.get('alignment', base.get('alignment'))
    if al=='CENTER': f.alignment=1
    bts=named.get(nst,{}).get('textStyle',{})
    for e in p.get('elements',[]):
        if 'textRun' in e:
            ts=e['textRun'].get('textStyle',{})
            txt=e['textRun']['content']
            parts=txt.split('\x0c')
            for i,ptxt in enumerate(parts):
                if i: np.add_run().add_break(WD_BREAK.PAGE)
                r=np.add_run(ptxt.rstrip('\n'))
                r.font.name='Times New Roman'
                sz=mag(ts.get('fontSize', bts.get('fontSize')),12)
                r.font.size=Pt(sz or 12)
                r.bold=ts.get('bold', bts.get('bold'))
        elif 'inlineObjectElement' in e:
            io=dt['inlineObjects'][e['inlineObjectElement']['inlineObjectId']]['inlineObjectProperties']['embeddedObject']
            h=io['size']['height']['magnitude']
            r=np.add_run(); r.add_break()
            np.paragraph_format.space_after=Pt(h)  # placeholder height
        elif 'pageBreak' in e:
            np.add_run().add_break(WD_BREAK.PAGE)
    return np
for el in dt['body']['content']:
    if 'paragraph' in el: para(el['paragraph'], doc)
    elif 'table' in el:
        rows=el['table']['tableRows']; nc=max(len(r['tableCells']) for r in rows)
        t=doc.add_table(rows=len(rows), cols=nc); t.style='Table Grid'
        for i,r in enumerate(rows):
            for j,c in enumerate(r['tableCells']):
                cell=t.cell(i,j); cell._tc.remove(cell.paragraphs[0]._p)
                for ce in c['content']:
                    if 'paragraph' in ce: para(ce['paragraph'], cell, True)
    elif 'sectionBreak' in el: pass
doc.save(sys.argv[3])
