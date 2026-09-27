"""Fetch a web page through the environment's egress proxy and print it as plain text.

Why: in this environment the WebFetch tool is blocked for many hosts, while curl through the proxy works.
Usage (from the repo root):
    .venv/bin/python research/insight_v1/scripts/fetch_text.py URL [--grep "exact phrase"] [--raw]
- Prints the page's visible text (scripts/styles removed, whitespace collapsed per line).
- --grep "phrase": also reports whether the exact phrase appears in the page text (case-sensitive, after collapsing
  whitespace and normalising curly quotes/apostrophes), with surrounding context. Use this to verify quotes verbatim.
- --raw: print the raw HTML instead.
- PDFs are detected and converted with pypdf.
Pages are cached under /tmp/insight_v1_fetch_cache/ for the session.
"""
import hashlib
import html
import io
import os
import re
import subprocess
import sys
from html.parser import HTMLParser

CACHE = "/tmp/insight_v1_fetch_cache"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


def fetch(url):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest())
    if not os.path.exists(path):
        r = subprocess.run(["curl", "-sSL", "-m", "40", "-A", UA, "-o", path, "-w", "%{http_code}", url],
                           capture_output=True, text=True)
        code = r.stdout.strip()
        if r.returncode != 0 or not code.startswith("2"):
            if os.path.exists(path):
                os.remove(path)
            sys.exit(f"FETCH FAILED: {url} (curl exit {r.returncode}, HTTP {code}) {r.stderr.strip()}")
    return open(path, "rb").read()


class Text(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "head"}
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "section", "article", "blockquote"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def to_text(raw):
    if raw[:5] == b"%PDF-":
        from pypdf import PdfReader
        return "\n".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(raw)).pages)
    p = Text()
    p.feed(raw.decode("utf-8", errors="replace"))
    lines = [re.sub(r"[ \t\r\f\v]+", " ", l).strip() for l in "".join(p.out).split("\n")]
    return "\n".join(l for l in lines if l)


def norm(s):
    s = html.unescape(s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-"),
                 (" ", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    url = args[0]
    raw = fetch(url)
    if "--raw" in args:
        print(raw.decode("utf-8", errors="replace"))
        sys.exit()
    text = to_text(raw)
    if "--grep" in args:
        phrase = norm(args[args.index("--grep") + 1])
        flat = norm(text)
        i = flat.find(phrase)
        print(f"URL: {url}\nPHRASE FOUND VERBATIM: {'YES' if i >= 0 else 'NO'}")
        if i >= 0:
            print("CONTEXT: ..." + flat[max(0, i - 300): i + len(phrase) + 300] + "...")
        else:
            words = phrase.split()[:4]
            j = flat.find(" ".join(words))
            if j >= 0:
                print("PARTIAL MATCH (first words) CONTEXT: ..." + flat[max(0, j - 200): j + 500] + "...")
    else:
        print(text)
