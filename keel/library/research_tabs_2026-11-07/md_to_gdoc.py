"""Turn a small Markdown file into Google Docs batchUpdate requests for one tab.

Supports: '# ', '## ', '### ' headings, '- ' bullets, plain paragraphs, **bold** and [text](url) links.
Usage: python md_to_gdoc.py FILE.md TAB_ID > requests.json
The tab must be empty (text is inserted at index 1).
"""
import json
import re
import sys

TOKEN = re.compile(r"\*\*(.+?)\*\*|\[([^\]]+)\]\((https?://[^)]+)\)")


def u16(s):
    return len(s.encode("utf-16-le")) // 2


def main(path, tab):
    lines = [l.rstrip("\n") for l in open(path, encoding="utf-8")]
    text, paras = "", []  # paras: (start, end, kind)
    spans = []  # (start, end, kind, url)
    pos = 1
    for line in lines:
        if not line.strip():
            continue
        kind = "P"
        for pre, k in (("### ", "H3"), ("## ", "H2"), ("# ", "H1"), ("- ", "B")):
            if line.startswith(pre):
                kind, line = k, line[len(pre):]
                break
        line = re.sub(r"(?<![*\w])\*([^*\n]+?)\*(?![*\w])", r"\1", line)
        out = ""
        last = 0
        for m in TOKEN.finditer(line):
            out += line[last:m.start()]
            start = pos + u16(out)
            if m.group(1) is not None:
                seg = m.group(1)
                spans.append((start, start + u16(seg), "bold", None))
            else:
                seg = m.group(2)
                spans.append((start, start + u16(seg), "link", m.group(3)))
            out += seg
            last = m.end()
        out += line[last:]
        para = out + "\n"
        paras.append((pos, pos + u16(para), kind))
        text += para
        pos += u16(para)
    reqs = [{"insertText": {"location": {"index": 1, "tabId": tab}, "text": text}}]
    reqs.append({"updateParagraphStyle": {
        "range": {"startIndex": 1, "endIndex": pos, "tabId": tab},
        "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}})
    names = {"H1": "HEADING_1", "H2": "HEADING_2", "H3": "HEADING_3"}
    for s, e, k in paras:
        if k in names:
            reqs.append({"updateParagraphStyle": {
                "range": {"startIndex": s, "endIndex": e, "tabId": tab},
                "paragraphStyle": {"namedStyleType": names[k]}, "fields": "namedStyleType"}})
    # merge consecutive bullet paragraphs into one bullet request each
    run = None
    for s, e, k in paras + [(0, 0, "END")]:
        if k == "B":
            run = (run[0], e) if run else (s, e)
        elif run:
            reqs.append({"createParagraphBullets": {
                "range": {"startIndex": run[0], "endIndex": run[1] - 1, "tabId": tab},
                "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
            run = None
    for s, e, k, url in spans:
        style = {"bold": True} if k == "bold" else {"link": {"url": url}}
        reqs.append({"updateTextStyle": {
            "range": {"startIndex": s, "endIndex": e, "tabId": tab},
            "textStyle": style, "fields": "bold" if k == "bold" else "link"}})
    json.dump(reqs, sys.stdout, ensure_ascii=False)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
