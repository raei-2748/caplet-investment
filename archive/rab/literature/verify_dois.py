"""Re-check that every DOI in references.bib resolves (doi.org handle API) and that Crossref's title matches.
Run: /Users/ray/Research/rab-ws/.venv/bin/python rab/literature/verify_dois.py"""
import re, pathlib, difflib, requests
bib = pathlib.Path(__file__).with_name("references.bib").read_text()
entries = re.findall(r"@\w+\{(\w+),(.*?)\n\}", bib, re.S)
bad = 0
for key, body in entries:
    doi = re.search(r"doi\s*=\s*\{([^}]+)\}", body).group(1)
    title = re.sub(r"[{}\\']|---|--", " ", re.search(r"title\s*=\s*\{(.+?)\},\n", body).group(1)).lower()
    h = requests.get(f"https://doi.org/api/handles/{doi}", timeout=30).json().get("responseCode")
    cr = requests.get(f"https://api.crossref.org/works/{doi}", timeout=30,
                      headers={"User-Agent": "rab-kit-ws5"}).json()["message"]
    cr = " ".join(cr.get("title", [""])[:1] + cr.get("subtitle", [])[:1]).lower()
    sim = difflib.SequenceMatcher(None, " ".join(title.split()), " ".join(cr.split())).ratio()
    ok = h == 1 and sim > 0.6
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {key:28s} {doi:34s} resolves={h==1} title_match={sim:.2f}")
print(f"{len(entries)} entries, {bad} problems")
