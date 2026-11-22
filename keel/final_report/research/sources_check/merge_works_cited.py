"""Merge sources checks S1-S4 (Mon 23 Nov 2026) into research/WORKS_CITED_DRAFT.md: one APA 7 list, alphabetical,
deduplicated, with the works not yet verified and the dropped works in their own lists."""
import re, pathlib, unicodedata

HERE = pathlib.Path(__file__).parent
rows = []
for f in sorted(HERE.glob("S[1-4].md")):
    lines = f.read_text().splitlines()
    hdr = next(i for i, l in enumerate(lines) if l.startswith("| # |"))
    for l in lines[hdr + 2:]:
        if not l.startswith("|"):
            if rows and l.strip() == "":
                continue
            continue
        cells = [c.strip() for c in l.strip().strip("|").split(" | ")]
        if len(cells) < 8:
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 8:
            continue
        num, short, apa, checked, date, status, part, ref = cells[:8]
        rows.append(dict(src=f.stem, num=num, short=short, apa=apa, checked=checked, status=status, part=part, ref=ref))

def kind(status):
    s = status.lower()
    if s.startswith("dropped"):
        return "dropped"
    if s.startswith("not verified"):
        return "unverified"
    if s.startswith("fixed"):
        return "fixed"
    return "verified"

def norm(apa):
    t = unicodedata.normalize("NFKD", apa).lower()
    t = re.sub(r"\*|\[|\]|https?://\S+", "", t)
    t = re.sub(r"[^a-z0-9一-鿿 ]+", " ", t)
    return " ".join(t.split())[:70]

rank = {"verified": 3, "fixed": 3, "unverified": 1, "dropped": 0}
merged = {}
for r in rows:
    r["kind"] = kind(r["status"])
    k = norm(r["apa"])
    if k in merged:
        m = merged[k]
        m["parts"].add(r["part"]); m["refs"].add(f'{r["src"]} #{r["num"]}')
        if rank[r["kind"]] > rank[m["kind"]]:
            m.update(apa=r["apa"], kind=r["kind"], status=r["status"], short=r["short"])
    else:
        merged[k] = dict(r, parts={r["part"]}, refs={f'{r["src"]} #{r["num"]}'})

# A work checked under two slightly different entries keeps the better status by its short cite as well.
by_short = {}
for k, m in list(merged.items()):
    s = re.sub(r"\W+", " ", m["short"].lower()).strip()
    if s in by_short and by_short[s]["kind"] != m["kind"]:
        a, b = by_short[s], m
        best, worse = (a, b) if rank[a["kind"]] >= rank[b["kind"]] else (b, a)
        if rank[best["kind"]] >= 3 and worse["kind"] in ("unverified",):
            best["parts"] |= worse["parts"]; best["refs"] |= worse["refs"]
            best.setdefault("note", "")
            best["note"] += f' (also checked as {worse["refs"]} with status "{worse["status"][:60]}")'
            del merged[[kk for kk, vv in merged.items() if vv is worse][0]]
            by_short[s] = best
            continue
    by_short[s] = m

def sortkey(m):
    t = re.sub(r"^[\*\[\(\s]+", "", m["apa"])
    latin = re.match(r"[A-Za-z]", t) is not None
    return (0 if latin else 1, unicodedata.normalize("NFKD", t).lower())

good = sorted([m for m in merged.values() if m["kind"] in ("verified", "fixed")], key=sortkey)
unver = sorted([m for m in merged.values() if m["kind"] == "unverified"], key=sortkey)
drop = sorted([m for m in merged.values() if m["kind"] == "dropped"], key=sortkey)

out = [
"# Works cited, draft (Mon 23 Nov 2026)",
"",
"One APA 7 list built from the four sources checks of Mon 23 Nov (`sources_check/S1.md` to `S4.md`), each work opened",
"at its source that day (author, year, title, publisher or journal, volume, pages, DOI or stable URL, and any",
"retraction or correction). Reading taken for \"every source the store's tier-A ideas rely on\": the sources the report",
"will cite, which are the works the argument tree names and REFERENCES_PLAN section 4's forty works with its second",
"rank, not every one of the store's 2,674 tier-A rows (most of those rest on the same works, and the rest will not be",
"cited). The References page on 27 Nov takes its entries from here, keeps only the works the prose and tables cite, and",
"lists them alphabetically with a 0.5-inch hanging indent, double-spaced, on a new page titled \"References\"",
"(Wharton; APA 7). In this file italics are marked with asterisks. Wharton's own pages stay out except the case;",
"Caplet owns the citation of anything else Wharton asks to be cited.",
"",
f"Counts: {len(rows)} checks of {len(merged)} distinct works; {len(good)} ready to cite (verified or fixed at source),",
f"{len(unver)} not yet verified at source, {len(drop)} dropped.",
"",
"Before citing, read in full (APA: cite only what was read; otherwise cite \"as cited in\" the work read): Sharpe and",
"Tint (1990), Roy (1952), Black and Perold (1992), McDonald and Siegel (1986) (S1); Spence (1973), Crawford and Sobel",
"(1982), Kőszegi and Rabin (2006), Andonov et al. (2017), Tobin (1974), Rogers and Stocken (2005), Markova et al.",
"(2018) (S2). Two works by one author in one year take letters by title (Barber and Odean 2000a, 2000b; Damodaran's",
"2026 packets, beside card Q169's 2026a-g), settled on the References page once the cited set is known.",
"",
"## Ready to cite",
"",
]
for m in good:
    out.append(m["apa"])
    out.append("")
    parts = "; ".join(sorted(p for p in m["parts"] if p))
    out.append(f"<sub>Supports: {parts}. Checked: {', '.join(sorted(m['refs']))}, {m['kind']}{m.get('note','')}.</sub>")
    out.append("")
out += ["## Not yet verified at source", ""]
for m in unver:
    out += [m["apa"], "", f"<sub>{m['status']} ({', '.join(sorted(m['refs']))}).</sub>", ""]
out += ["## Dropped, with the reason", ""]
for m in drop:
    out += [f"- {m['short']}: {m['status']} ({', '.join(sorted(m['refs']))})"]
out.append("")
(HERE.parent / "WORKS_CITED_DRAFT.md").write_text("\n".join(out))
print(len(rows), len(merged), len(good), len(unver), len(drop))
