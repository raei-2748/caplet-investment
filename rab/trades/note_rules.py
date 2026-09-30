"""Shared rules for WInS trade notes (standard library only). Used by build_notes.py and note_check.py.

WS6-notes, RAB Kit, 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet.
Sources: rab/premortem.md Gate C items 1-5 and PM-12..PM-18, PM-20, PM-23, PM-28, PM-31; insight_v1
trading_notes_pack.md s6.2 and D9_draft_checker.py (word lists reused); Competition Guide p.3 (role words);
WInS note box maxlength 300 (tab WInS Notes, SEEN 29 Sep 2026).
"""
import re

MAX_NOTE = 285   # kit limit (PM-12): leaves 15 characters of margin under the box
BOX = 300        # WInS note box maxlength (SEEN 29 Sep 2026)

# pattern -> why it is banned in a note
BANNED = {
    r"(?i)guarantee": "overclaim (PM-14)",
    r"(?i)risk[- ]free|riskless|\bno risk\b": "overclaim; say 'backed by the U.S. government' (PM-28)",
    r"(?i)\block(ed|s)?\b|lock[- ]in": "overclaim (PM-14)",
    r"(?i)\bmatch(es|ed|ing)?\b": "false for ETFs and coupon bonds (PM-14, PM-23)",
    r"(?i)cash[- ]flow match": "overclaim: coupons must be reinvested (PM-23)",
    r"(?i)no rebalancing": "IPS overclaim under review (PM-23)",
    r"\bI[- ]bonds?\b": "'I bond' is a U.S. savings bond, not an iBonds ETF (PM-14)",
    r"(?i)\bsafe(ly|r|st)?\b|\bstable\b|\bstability\b|reduc\w* (portfolio )?volatility": "vague overclaim (pack s6.2)",
    r"(?i)\bcertain(ly|ty)?\b|\b100 ?%": "certainty only with its conditions, never in a note (pack s6.2)",
    r"(?i)\bpromise[sd]?\b|\bpledge[sd]?\b": "nothing is promised in a note (pack s6.2)",
    r"(?i)\bforecast|\bwill (grow|return|earn|outperform)|\boutperform|\bCAPE\b|overvalued": "no return forecasts",
    r"(?i)\bprofit|\bgain(s|ed)?\b|\brank(ing)?\b": "WInS results are not judged (Guide p.3; PM-18)",
    r"(?i)root-and-branch|roots first|\broots?\b|\bbranch(es)?\b": "no strategy name until Ray confirms it (PM-16)",
    r"(?i)laura's portfolio": "the WInS book is a scaled model, not her portfolio (pack s6.2)",
    r"(?i)operating reserve": "reserve size is Final Report material (TN guide)",
    r"(?i)statistics degree|taiwan|heritage": "not a reason for a trade (pack s6.2; team decision D8)",
    r"\bbp\b|(?i:basis point)": "jargon: say 'points of yield' (plain English)",
    r"\bIEF\b|\bTLH\b|\bVGSH\b|\(ii\)R|(?i:duration match)|(?<![\d,.$])9\.90(?!\d)": "superseded book (PM-20)",
    r"100,000|\$100k|Dec 4\b|500k|(?i:no Treasuries)|\$0 commission": "stale repo fact (PM-31)",
    r"(?i)\brepa(y|ys|id)\b": "never for an iBonds fund; for one bond say 'the amount due at maturity' (PM-14)",
    r"[‒-―‘’“”~]|<=|>=": "not plain ASCII punctuation (PM-12)",
}
ROLE_WORDS = ["growth", "liquidity", "risk management", "future funding"]   # Competition Guide p.3
# A payment year alone is not an anchor: it could fit any client (judge panel, 30 Sep 2026).
LAURA_ANCHORS = [r"Laura", r"\bher\b", r"(?i)facility", r"(?i)co-?sponsor", r"(?i)residency"]
# A note that may be featured in the Trading Notes Analysis must also say what the payment is for or who hears the
# range: the residency, co-sponsors, or which of her ten payments ("her ninth", "the fourth of Laura's ten").
PICK_ANCHORS = [r"(?i)residency", r"(?i)co-?sponsor",
                r"(?i)\b(her|laura's) (ten|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|last)\b"]
CASE_FACTS = {"$50,000", "$300,000", "$150,000"}   # client case design facts (Laura's plan)
SECURITY_COUPONS = {"3.125%", "4.250%", "4.375%", "4.500%", "4.750%", "1.375%", "2.000%", "5.000%", "4.5%",
                    "4.25%", "4.75%", "3.5%"}
MONTHS = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
ASCII_FIX = {"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": ", ",
             "…": "...", " ": " "}


# Quantities written in words count as numbers too (notes.md s1; judge panel round 2, 30 Sep: the digit-only check let
# untraced comparisons through). Each hit must be declared (a numbers.yaml key or a dated source), like a digit.
# Order matters: the first pattern that matches a span takes it, so "a quarter of a percentage point" is one token.
WORD_CASE = [   # IPS design facts, like the $50,000 case facts: the range is the floor plus half the fund
    r"(?i)\bhalf (?:of )?the (?:stock |equity )?fund\b",
]
WORD_QUANT = [
    r"(?i)\ba (?:quarter|fifth|third|tenth|half) of a percentage point\b",
    r"(?i)\b(?:a full|one|two|three|half a) percentage points?\b",
    r"(?i)\bpercentage points?\b",
    r"(?i)\ba (?:quarter|fifth|third|tenth) of\b",
    r"(?i)\bhalf (?:of|the)\b",
    r"(?i)\babout the same\b",
    r"(?i)\balmost exactly\b",
    r"(?i)\btwice\b",
    r"(?i)\bmost of\b",
]


def word_numbers_in(text):
    """(token, kind, start) for every quantity written in words: kind 'case' (IPS design) or 'analytic'."""
    taken, out = [], []
    for pats, kind in ((WORD_CASE, "case"), (WORD_QUANT, "analytic")):
        for pat in pats:
            for m in re.finditer(pat, text):
                if any(a < m.end() and m.start() < b for a, b in taken):
                    continue
                taken.append((m.start(), m.end()))
                out.append((m.group(0).lower(), kind, m.start()))
    return sorted(out, key=lambda x: x[2])


def is_declared(tok, declared):
    """Traced if a declared entry is the token itself (words) or starts with it (digits: '9%' declared as '9%')."""
    return any(tok == d.lower() or tok == d.split()[0] for d in declared if d)


def numbers_in(text):
    """(token, kind) for every number, in digits or in words: kind is 'date', 'year', 'coupon', 'case' or
    'analytic'. Word quantities (word_numbers_in) follow the digits."""
    out = []
    for m in re.finditer(r"\$?\d[\d,]*(?:\.\d+)?%?", text):
        tok = m.group(0).rstrip(",.")
        before, after = text[max(0, m.start() - 5):m.start()], text[m.end():m.end() + 4]
        if tok in CASE_FACTS:
            kind = "case"
        elif tok in SECURITY_COUPONS:
            kind = "coupon"
        elif re.fullmatch(r"20[2-4]\d", tok):
            kind = "year"
        elif re.match(r"\s" + MONTHS, after) or re.search(MONTHS + r"\s$", before):
            kind = "date"
        else:
            kind = "analytic"
        out.append((tok, kind))
    out += [(tok, kind) for tok, kind, _ in word_numbers_in(text)]
    return out


def check_text(text, declared=()):
    """List of (check, ok, detail, severity). severity FAIL blocks; WARN asks for a second look."""
    res = []
    n = len(text)
    res.append(("length", n <= MAX_NOTE, f"{n} characters (kit limit {MAX_NOTE}, box {BOX})",
                "FAIL" if n > BOX else "WARN"))
    bad = sorted({c for c in text if not c.isascii()})
    res.append(("ascii", not bad, " ".join(f"{c!r}->{ASCII_FIX.get(c, '?')!r}" for c in bad), "FAIL"))
    res.append(("one paragraph", "\n" not in text.strip() and "\r" not in text, "", "FAIL"))
    hits = [f"'{m.group(0)}': {why}" for pat, why in BANNED.items() for m in [re.search(pat, text)] if m]
    res.append(("banned words", not hits, "; ".join(hits), "FAIL"))
    res.append(("role word", any(w in text.lower() for w in ROLE_WORDS),
                "name one: growth / liquidity / risk management / future funding", "WARN"))
    res.append(("Laura anchor", any(re.search(p, text) for p in LAURA_ANCHORS),
                "name her payment date, the floor or the facility", "WARN"))
    nums = numbers_in(text)
    analytic = [t for t, k in nums if k == "analytic"]
    untraced = [t for t in analytic if not is_declared(t, declared)]
    res.append(("at most one analytic number", len(analytic) <= 1, ", ".join(analytic), "WARN"))
    res.append(("numbers traced", not untraced,
                ", ".join(untraced) + (" (find each in rab/numbers.yaml or name a dated source)" if untraced else ""),
                "WARN"))
    dollars = [t for t, k in nums if t.startswith("$") and k != "case"]
    res.append(("dollar scale", not dollars or "Laura's plan" in text,
                ", ".join(dollars) + (" (say 'in Laura's plan', or use a percentage of the WInS portfolio)"
                                      if dollars else ""), "WARN"))
    return res


def pick_anchor(text):
    """(ok, detail) for a note that may be featured: it names the residency, co-sponsors or which of her ten payments."""
    ok = any(re.search(p, text) for p in PICK_ANCHORS)
    return ok, "" if ok else "a featured note names the residency, co-sponsors or which of her ten payments"


def words(text):
    return [w for w in (re.sub(r"[^a-z0-9$%.']", "", t.lower()).strip(".'") for t in text.split()) if w]


def phrase_overlap(draft, other, n=3):
    """Share of the draft's n-word phrases that also occur in `other`, and the longest shared run of words."""
    a, b = words(draft), words(other)
    ga = [tuple(a[i:i + n]) for i in range(len(a) - n + 1)]
    gb = {tuple(b[i:i + n]) for i in range(len(b) - n + 1)}
    share = sum(1 for g in ga if g in gb) / len(ga) if ga else 0.0
    best = 0
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            best = max(best, k)
    return share, best
