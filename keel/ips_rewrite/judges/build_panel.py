"""AI-generated (Claude Code), 31 Oct 2026. Builds a blind panel folder for the six judges in README.md.
Usage (from keel/ips_rewrite/): python3 judges/build_panel.py panel_VNN SEED CODE=PATH ...
  CODE=PATH  an entry: a draft folder or ips file of ours (pitch.txt beside it), rivals/<CODE>.md, or entries/<CODE>.txt
Writes judges/<panel>/judgeN_entries.txt (each judge a different order), KEY.json, and judges/<panel>/judgeN_prompt.txt
from judges/prompts/judgeN.txt. Rival files are cut at "## SIMULATOR NOTES" so no judge sees our notes."""
import json, pathlib, random, re, sys

ROOT = pathlib.Path(__file__).resolve().parent


def entry(path):
    p = pathlib.Path(path)
    if p.suffix == ".md":                                      # a rival file
        t = p.read_text()
        pitch = re.search(r"## PITCH\n(.*?)\n## IPS", t, re.S).group(1).strip()
        ips = t.split("## IPS", 1)[1].split("## SIMULATOR NOTES")[0].strip()
    elif p.parent.name == "entries":                          # a ready-made entry
        return p.read_text().strip()
    else:                                                     # one of our drafts
        ips_f = p / "ips.txt" if p.is_dir() else p
        pitch = (ips_f.parent / "pitch.txt").read_text().strip()
        ips = ips_f.read_text().strip()
    return f"ELEVATOR PITCH (max 50 words):\n{pitch}\n\nINVESTMENT POLICY STATEMENT (max 500 words):\n{ips}"


def main():
    panel, seed = sys.argv[1], int(sys.argv[2])
    pairs = dict(a.split("=", 1) for a in sys.argv[3:])
    texts = {c: entry(p) for c, p in pairs.items()}
    for c, t in texts.items():
        assert "SIMULATOR" not in t, c
    out = ROOT / panel; out.mkdir(exist_ok=True)
    key = {}
    for j in range(1, 7):
        order = list(texts); random.Random(seed + j).shuffle(order)
        key[f"judge{j}"] = {f"Entry {k + 1}": c for k, c in enumerate(order)}
        (out / f"judge{j}_entries.txt").write_text(
            "".join(f"===== Entry {k + 1} =====\n{texts[c]}\n\n" for k, c in enumerate(order)))
        (out / f"judge{j}_prompt.txt").write_text((ROOT / "prompts" / f"judge{j}.txt").read_text().replace("PANEL", panel))
    (out / "KEY.json").write_text(json.dumps(key, indent=1))
    print(json.dumps({j: list(v.values()) for j, v in key.items()}))


if __name__ == "__main__":
    main()
