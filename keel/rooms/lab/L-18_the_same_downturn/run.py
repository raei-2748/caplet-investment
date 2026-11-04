"""AI-generated (Claude Code), Wed 4 Nov 2026, the Genius Lab (round 8 beat 5). MODEL.
(Keel is a simulated team, AI-written.) L-18 "The same downturn": the Library's H-029 seed.

Question (the Library, 4 Nov): when the 2028 deposit falls short in the same downturn that hits her shares (the FINAL
IPS P4's own warning), does every cheque still get paid under the FINAL's lock, "as if every dollar waiting for a
cheque earned nothing" (Courtroom exhibit N's KWN-w arm, the words' reading; the lock is sized with the funds' bonds
idle and scored with the funds paid at net asset value)?

The chair's hypothesis, written before the test (Kai roasts it blind, huddle H-030): in this plan Laura owns no shares in 2027. The first $300,000 is all ladder; shares are
bought on 2 Jan 2028 with what the deposit leaves. So a 2027 downturn can shrink the deposit, push rates down (the
ladder's reinvestment gap grows) and make the floor dearer, but it cannot also hit shares she doesn't yet own. The
worlds below put every leg of that downturn in at once.

New worlds (exhibit N's machinery unchanged; only the scenario arguments of L-10's run() differ):
  S10  2027 downturn: yields fall 2 points just after the build, for good; 2028 deposit halved ($75k); rho 0.5
  S11  as S10 with the 2028 deposit missing ($0)
  S12  as S10, and shares halve again before the 2031 range is named (h_pre 0.5)
  S13  as S10 with the deposit cut to $112,500 (a quarter off)
  S14, S15  as S10 with the deposit at $50,000 and $25,000 (where does the cheque cover break?)
Reference rows (S0, S6, S9) are read from exhibit N's results.json, not re-run.
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 |
rho 0.5 | V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17 -> exhibit N (the FINAL's lock = KWN-w) | MODEL.
Run from repo root: python3 keel/rooms/lab/L-18_the_same_downturn/run.py [S10 S11 S12 S13 S14 S15]  (~2 min each)"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
EXN = HERE.parents[1] / "courtroom" / "C-06_w5_on_trial" / "exhibit_N_funds_at_nav.py"
_s = importlib.util.spec_from_file_location("EXN", EXN); N = importlib.util.module_from_spec(_s); _s.loader.exec_module(N)
L17, L16, L14 = N.L17, N.L16, N.L14

NEW = {
    "S10 2027 downturn: yields -2pt for good after the build + 2028 deposit halved": dict(dy_after=-2.0, d28=75_000.0),
    "S11 2027 downturn: yields -2pt for good after the build + 2028 deposit missing": dict(dy_after=-2.0, d28=0.0),
    "S12 S10 + shares halve before the 2031 range is named": dict(dy_after=-2.0, d28=75_000.0, h_pre=0.5),
    "S13 2027 downturn: yields -2pt for good after the build + 2028 deposit a quarter short": dict(dy_after=-2.0, d28=112_500.0),
    "S14 2027 downturn: yields -2pt for good after the build + 2028 deposit $50,000": dict(dy_after=-2.0, d28=50_000.0),
    "S15 2027 downturn: yields -2pt for good after the build + 2028 deposit $25,000": dict(dy_after=-2.0, d28=25_000.0),
}


def patch():
    """Exactly exhibit N's main() patch chain (copied, so its own file stays untouched)."""
    b17 = L17.BLOCK17
    assert b17.count('    out16["L17"] = out17') == 1
    blk17 = b17.replace('    out16["L17"] = out17', '    out16["L17"] = out17' + N.BLOCKN)
    b = L16.BLOCK16
    assert b.count('    lr["L16"] = out16') == 1
    L16.BLOCK16 = b.replace('    lr["L16"] = out16', blk17 + '\n    lr["L16"] = out16')
    blk14 = L14.BLOCK14
    assert blk14.count("for k in (0.80, 0.65):") == 1
    blk14 = blk14.replace("for k in (0.80, 0.65):", "for k in (0.80, 0.76):") + L16.BLOCK16
    blk = L14.L13.BLOCK13.replace('    lr["L13"] = out13', blk14)
    add = L14.LR8.ADD.replace('    res["LR05"] = lr', blk)
    block = L14.LR05.BLOCK.replace('    res["LR05"] = lr', add)
    L14.L11.EXTRA = L14.L11.EXTRA.replace('    out["L11"] = res', block)


def main():
    patch()
    f = HERE / "results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 | "
                    "V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17 -> exhibit N; FINAL's lock = KWN-w | MODEL")
    names = {k.split()[0]: k for k in NEW}
    for k in sys.argv[1:] or list(names):
        r = L14.L11.run(**NEW[names[k]])
        row = r["LR05"]["L16"]["L17"]["C06N"]
        row["ladder_headroom"] = r.get("ladder_headroom")
        out[names[k]] = row
        print(names[k], json.dumps(row), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
