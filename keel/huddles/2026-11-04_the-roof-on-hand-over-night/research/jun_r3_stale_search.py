"""Jun, H-033 round 3 (Wed 4 Nov 2026): the LS-17 search, run on the hand-over folder tonight.

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code, for the fictional Jun). Not text to submit.
Standard library only:  python3 -I jun_r3_stale_search.py > jun_r3_stale_search.txt

What it does, on keel/ips_rewrite/drafts/FINAL/ (reads only; `git show` reads three earlier FINALs):
  0. checks ips.txt and pitch.txt are the handed-over text (sha256 b9368f5b5fa9ffc5 / 2f94abe7c30be498);
  1. QUOTE SEARCH (my round-2 LS-17): every phrase in double quotes (straight or curly; a quote may run over a line
     break) and every backtick span of 3+ words in the seven files beside them, looked for word for word in ips.txt or
     pitch.txt ("..." is a gap; markdown bold, curly marks and line breaks ignored; then a second try ignoring capitals);
  2. OLD-WORDS SEARCH (Amara's): every 4-word run, inside one sentence, that an earlier FINAL had (V56, V57 at 08:26,
     after the Window, after the Library) and this one hasn't, looked for in the seven files, quoted or not;
  3. CUT-IDEA SEARCH: a few patterns written from today's change log (an idea cut in new words can't be found by its
     old words), plus every word count the files state.
Each hit gets Jun's class, read by hand (rules and the table below):
  FINE        in the FINAL word for word, or not presented as the IPS's words (the case's, Wharton's, the TNA's, a
              label, a rule, advice for the rewrite)
  ON PURPOSE  an old, false or offered version, shown as one (change logs, the look-alike card's "False:" lines, the
              cold read of the pre-fix V57 in COMMANDMENTS_CHECK, labelled at its L11 and L162)
  STALE       says the IPS says something it no longer says
  OVERSTATED  not stale (the FINAL never said otherwise) but says more than the FINAL does
"""
import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]                     # the repo
FINAL = ROOT / "keel/ips_rewrite/drafts/FINAL"
FILES = ["README.md", "CASE_CARD.md", "LOOK_ALIKE_CARD.md", "READERS_CARD.md", "KEEL_RECORD.md",
         "COMMANDMENTS_CHECK.md", "LABEL.md"]
HASHES = {"ips.txt": "b9368f5b5fa9ffc5", "pitch.txt": "2f94abe7c30be498"}
OLD_FINALS = {"V56 (059ffe0)": "059ffe0", "V57 at 08:26 (9f287c2)": "9f287c2", "after the Window (f06ad13)": "f06ad13",
              "after the Library (c82e1ee)": "c82e1ee"}
SOURCES = {"the case": "competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt",
           "Wharton": "keel/WHARTON_WORD.md",
           "Wharton's IPS instructions": "competition/official/2026_27/UPDATED_2026_WGY_Investment_Policy_FINAL.txt",
           "the submitted TNA": "keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt",
           "the WInS notes": "caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md"}

# labels, rules, sayings, advice and outside sources: quoted, but never offered as the IPS's words
LABELS = {"human", "human-written", "each payment has its own bond", "we don't duration-match", "Case 88", "IPS 58",
          "truly extraordinary erudite", "erudite", "look erudite", "our model", "That is X.", "every team", "we judge",
          "X, not Y", "every mechanism briefly", "smart adult", "Fixes", "Applied", "?", "stop reinvesting",
          "shares are safe over ten years", "contested but fair as written", "on or about December 15, 2032",
          "the Fund is expected to consist almost entirely of cash", "Laura's career already behaves like a stock."}

ON, ST, OV, FI = "ON PURPOSE", "STALE", "OVERSTATED", "FINE"
# (file, line) -> (class, why), for hits the rules don't settle
OVERRIDE = {
    ("CASE_CARD.md", 9): (FI, "495, the FINAL's strict count, and the house cap 497"),
    ("CASE_CARD.md", 10): (ON, "the old word in the card's change list"), ("CASE_CARD.md", 11): (ON, "the same"),
    ("CASE_CARD.md", 12): (ON, "the same"), ("CASE_CARD.md", 13): (ON, "the same"),
    ("READERS_CARD.md", 7): (ON, "an offered sentence, said not to beat the final"),
    ("KEEL_RECORD.md", 17): (ST, "the FINAL cut 'Her income already rides on shares' (f06ad13); this file's own section 6 says so"),
    ("KEEL_RECORD.md", 25): (ON, "the cold read's LOST phrases, said fixed"),
    ("KEEL_RECORD.md", 40): (ON, "said moved to the Final Report"),
    ("KEEL_RECORD.md", 72): (ON, "a softer wording offered as Caplet's call"),
    ("KEEL_RECORD.md", 83): (ON, "said cut"), ("KEEL_RECORD.md", 84): (FI, "the FINAL's words"),
    ("KEEL_RECORD.md", 86): (ON, "the count after that step, in a dated section"),
    ("KEEL_RECORD.md", 89): (ON, "said false and fixed"), ("KEEL_RECORD.md", 93): (ON, "the Library's offer, spelt out instead"),
    ("KEEL_RECORD.md", 95): (ON, "change log, old -> new"), ("KEEL_RECORD.md", 96): (ON, "change log"),
    ("KEEL_RECORD.md", 97): (ON, "an offer said not needed"), ("KEEL_RECORD.md", 99): (ON, "corrections of other files"),
    ("KEEL_RECORD.md", 100): (ON, "the count after that step, in a dated section"),
    ("KEEL_RECORD.md", 104): (ON, "change log, old -> new"), ("KEEL_RECORD.md", 106): (ON, "change log"),
    ("KEEL_RECORD.md", 107): (ON, "change log"), ("KEEL_RECORD.md", 108): (ON, "change log"),
    ("COMMANDMENTS_CHECK.md", 163): (ON, "said gone"),
    ("COMMANDMENTS_CHECK.md", 164): (ST, "offered as the applied wording; the Window cut it at f06ad13, and no note says so"),
    ("COMMANDMENTS_CHECK.md", 166): (ST, "offered as the applied wording; the FINAL says 'A Treasury bond held' (f06ad13)"),
    ("COMMANDMENTS_CHECK.md", 169): (ON, "old -> new"), ("COMMANDMENTS_CHECK.md", 170): (ON, "corrected in place at L171-172"),
    ("COMMANDMENTS_CHECK.md", 173): (ON, "old -> new"),
    ("COMMANDMENTS_CHECK.md", 174): (ST, "'Strict count after: 496' under 'Applied'; the FINAL is 495"),
    ("README.md", 16): (ST, "the FINAL says 'can dry up' (c82e1ee)"),
    ("README.md", 17): (OV, "the FINAL says portfolio insurance 'helped deepen' the crash; 'made ... worse' drops the"
                            " 'helped' the Library said carries the dispute (and the cold read: 'Don't strengthen it')"),
    ("LOOK_ALIKE_CARD.md", 31): (FI, "'the ladder can fall short' = P7's 'it can fall short'"),
    ("LOOK_ALIKE_CARD.md", 68): (FI, "the card's own reason, not the IPS's words"),
}


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("…", "...").replace("**", "")
    return re.sub(r"\s+", " ", s).strip()


def found_in(phrase, text, fold=False):
    p = norm(phrase).strip(" .,;:()'")
    if fold:
        p, text = p.lower(), text.lower()
    parts = [x.strip(" .,;:") for x in p.split("...") if x.strip(" .,;:")]
    pos = 0
    for part in parts:
        i = text.find(part, pos)
        if i < 0:
            return False
        pos = i + len(part)
    return bool(parts)


def git_show(rev, path):
    try:
        return subprocess.run(["git", "-C", str(ROOT), "show", f"{rev}:{path}"], capture_output=True, text=True,
                              check=True).stdout
    except Exception:
        return ""


def runs(text, n=4):
    """4-word runs inside one sentence or table cell: (run, line it starts on)."""
    out, seg, line = [], [], 1
    for tok in re.finditer(r"[A-Za-z0-9$']+|[.;:!?|\n]", text.replace("**", "")):
        t = tok.group()
        if t == "\n":
            line += 1
            continue
        if t in ".;:!?|":
            seg = []
            continue
        seg.append((t.lower(), line))
        if len(seg) >= n:
            out.append((" ".join(w for w, _ in seg[-n:]), seg[-n][1]))
    return out


def classify_quote(fname, line, ph, rawline, texts, both, srcs, olds):
    where = [n for n in ("ips", "pitch") if found_in(ph, texts[n])]
    if where:
        return FI, "in " + "+".join(where)
    if fname == "LOOK_ALIKE_CARD.md" and "False:" in rawline:
        return ON, "a false look-alike, shown as false"
    if found_in(ph, both, fold=True):
        return FI, "in the FINAL with other capitals"
    if norm(ph) in LABELS:
        return FI, "a label, rule, saying, source or advice; not offered as the IPS's words"
    src = [k for k, t in srcs.items() if found_in(ph, t, fold=True)]
    if src and not any(found_in(ph, norm(t)) for t in olds.values()):
        return FI, f"words of {src[0]}, not the IPS's"
    if (fname, line) in OVERRIDE:
        return OVERRIDE[(fname, line)]
    if fname == "COMMANDMENTS_CHECK.md" and line < 162:
        return ON, "the cold read of the pre-fix V57 (md5 7d73eed5, L11; 'the check above is of the text before these', L162)"
    return "UNCLASSIFIED", ""


def main():
    print("Jun r3 stale search (LS-17), keel/ips_rewrite/drafts/FINAL/, read only. MODEL-free: text matching only.\n")
    print("0. Hashes")
    texts, raw = {}, {}
    for name, want in HASHES.items():
        b = (FINAL / name).read_bytes()
        got = hashlib.sha256(b).hexdigest()
        print(f"  {name}: sha256 {got[:16]}  {'OK' if got.startswith(want) else 'MISMATCH, want ' + want}")
        texts[name.split('.')[0]] = norm(b.decode())
        raw[name] = b.decode()
    both = texts["ips"] + " || " + texts["pitch"]
    olds = {k: git_show(v, "keel/ips_rewrite/drafts/FINAL/ips.txt") for k, v in OLD_FINALS.items()}
    print(f"  earlier FINALs read from git: {sum(1 for t in olds.values() if t)} of {len(olds)}")
    srcs = {k: norm(re.sub(r"(?m)^[ \t]*(?:>[ \t]*)?(?:[-*\u2022][ \t]+)?", "", (ROOT / p).read_text())).lower()
            if (ROOT / p).exists() else "" for k, p in SOURCES.items()}

    tally, flagged = {}, []
    print("\n1. QUOTE SEARCH: every quoted phrase (class; where it is)")
    for fname in FILES:
        text = (FINAL / fname).read_text().replace("“", '"').replace("”", '"')
        lines = text.splitlines()
        hits = [(m.start(), m.group(1), '"') for m in re.finditer(r'"([^"\n]+(?:\n(?![ \t]*\n)[^"\n]*)*?)"', text)]
        hits += [(m.start(), m.group(1), "`") for m in re.finditer(r"`([^`\n]+)`", text)
                 if len(m.group(1).split()) >= 3 and not re.search(r"\.(md|txt|py)\b|/", m.group(1))]
        print(f"\n  {fname}: {len(hits)} phrases")
        for pos, ph, q in sorted(hits):
            line = text.count("\n", 0, pos) + 1
            cls, why = classify_quote(fname, line, ph, lines[line - 1], texts, both, srcs, olds)
            was = [k for k, t in olds.items() if found_in(ph, norm(t))]
            if was and cls != FI:
                why += f" [was in {was[0]}]"
            tally[cls] = tally.get(cls, 0) + 1
            show = norm(ph) if len(norm(ph)) <= 80 else norm(ph)[:77] + "..."
            print(f"    L{line:<4}{cls:<11}{q}{show}{q}  ({why})")
            if cls in (ST, OV, "UNCLASSIFIED"):
                flagged.append(("quote", fname, line, cls, norm(ph), why))
    print("\n  Quote search tally: " + ", ".join(f"{k} {v}" for k, v in sorted(tally.items())))

    print("\n2-3. OLD-WORDS and CUT-IDEA SEARCH, quoted or not (each line once; first old run shown)")
    now = {r for r, _ in runs(raw["ips.txt"])}
    gone = set()
    for t in olds.values():
        gone |= {r for r, _ in runs(t)} - now
    patterns = {r"tends? to dry up": "the income line, before 'can'", r"rides? on shares": "the cut income sentence",
                r"bet on shares already|income as a bet": "the cut income sentence, reworded",
                r"behaves like a share": "the aphorism cut before 08:26",
                r"made the 1987 crash worse|caused the 1987": "the 1987 line, stronger than 'helped deepen'",
                r"\b4[89][0-9]\b (?:strict|words|on the strict)|[Ss]trict count after: \d+|\b4[89][0-9] strict": "a word count"}
    tally2 = {}
    for fname in FILES:
        text = (FINAL / fname).read_text()
        lines = text.splitlines()
        by_line = {}
        for r, ln in runs(text):
            if r in gone:
                by_line.setdefault(ln, []).append(r)
        for i, ln_text in enumerate(lines, 1):
            pats = [why for pat, why in patterns.items() if re.search(pat, norm(ln_text))]
            if not (by_line.get(i) or pats):
                continue
            if pats == ["a word count"] and not by_line.get(i):
                counts = re.findall(r"\b(4[89][0-9])\b", ln_text)
                cls, why = (FI, "495, the FINAL's strict count") if counts in (["495"], ["495", "492"]) and not (
                    fname == "COMMANDMENTS_CHECK.md" and i < 162) else OVERRIDE.get((fname, i), (
                    ON, "the pre-fix text's count") if fname == "COMMANDMENTS_CHECK.md" and i < 162 else ("UNCLASSIFIED", ""))
            elif (fname, i) in OVERRIDE:
                cls, why = OVERRIDE[(fname, i)]
            elif fname == "LOOK_ALIKE_CARD.md" and "False:" in ln_text:
                cls, why = ON, "a false look-alike"
            elif fname == "COMMANDMENTS_CHECK.md" and i < 162:
                cls, why = ON, "the cold read of the pre-fix V57"
            else:
                cls, why = "UNCLASSIFIED", ""
            tally2[cls] = tally2.get(cls, 0) + 1
            what = ([f'old run "{by_line[i][0]}"' + (f" (+{len(by_line[i]) - 1})" if len(by_line[i]) > 1 else "")]
                    if by_line.get(i) else []) + [f"pattern: {p}" for p in pats]
            print(f"  {fname} L{i:<4}{cls:<11}{'; '.join(what)}")
            print(f"        | {norm(ln_text)[:140]}")
            if why:
                print(f"        -> {why}")
            if cls in (ST, OV, "UNCLASSIFIED"):
                if by_line.get(i):
                    flagged.append(("old-words", fname, i, cls, norm(ln_text)[:110], why))
                if [p for p in pats if p != "a word count"]:
                    flagged.append(("cut-idea pattern", fname, i, cls, norm(ln_text)[:110], why))
                if pats == ["a word count"]:
                    flagged.append(("word count", fname, i, cls, norm(ln_text)[:110], why))
    print("\n  Old-words / cut-idea tally (lines): " + ", ".join(f"{k} {v}" for k, v in sorted(tally2.items())))

    print("\nSUMMARY: every STALE / OVERSTATED hit, and which search found it")
    seen = {}
    for how, f, ln, cls, txt, why in flagged:
        seen.setdefault((f, ln), [cls, txt, why, set()])[3].add(how)
    for (f, ln), (cls, txt, why, hows) in sorted(seen.items()):
        print(f"  {cls:<11}{f} L{ln}  found by: {' + '.join(sorted(hows))}\n             {txt}\n             {why}")
    readme16 = seen.get(("README.md", 16))
    print(f"\n  'tends to dry up' (README L16): quote search {'CAUGHT' if readme16 and 'quote' in readme16[3] else 'MISSED (it is not in quote marks)'};"
          f" old-words search {'CAUGHT' if readme16 and 'old-words' in readme16[3] else 'MISSED'}.")


if __name__ == "__main__":
    main()
