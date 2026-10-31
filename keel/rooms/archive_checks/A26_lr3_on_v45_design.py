"""AI-generated (Claude Code), Sat 31 Oct 2026, the Archive (round 4 beat 9, Tess). MODEL.
(Keel is a simulated team, AI-written.) A26: LR3's three numbers re-run on V45's OWN design.
LR3 (the Courtroom's promoted paragraph, keel/rooms/courtroom/C-04_LR3_ips.txt) quotes $145,000 (both plans' median
named bottom), about $19,000 (A09's mean lead in gift + Laura's 2042 money) and $90,000 v $140,000 (median named
bottom in the worst 5% of 2028-30 stock paths). Those come from LR-08's engine (Model Suite), not from the L-13 chain
that V45 describes (2031 mark, slide, lock). L-14 (Genius Lab) put A09 on the L-13 chain but matched it by stock share
(k = 0.80, median bottom $150k), not by LR3's rule (same $145k median bottom). This script reuses L-14 unchanged and
only widens its k grid, so A09 can be matched to name the same median bottom as XR, then prints LR3's numbers per k.
STAMP: curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | V45's design via
L-13 -> L-14 chain | MODEL.  Run from repo root: python3 keel/rooms/archive_checks/A26_lr3_on_v45_design.py [S0 S1 S6]"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parent / "lab" / "L-14_price_of_the_floor" / "run.py"
_s = importlib.util.spec_from_file_location("L14", P); L14 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L14)
KS = (0.80, 0.78, 0.77, 0.76, 0.75, 0.65)
b = L14.BLOCK14
assert b.count("for k in (0.80, 0.65):") == 1
b = b.replace("for k in (0.80, 0.65):", f"for k in {KS}:")
extra = '''
    out14["A26_per_k"] = {}
    for kk in sorted(gA):
        bA_, gA_, lA_ = gA[kk]
        out14["A26_per_k"][str(kk)] = {
            "A09_bottom_p50": round(float(np.median(bA_))), "XR_bottom_p50": round(float(np.median(q_mc))),
            "mean_gift_plus_laura2042_A09_minus_XR": round(float((gA_ + lA_).mean() - (gX + l42X).mean())),
            "mean_gift_A09_minus_XR": round(float(gA_.mean() - gX.mean())),
            "worst5_bottom_p50_A09_v_XR": [round(float(np.median(bA_[worst]))), round(float(np.median(q_mc[worst])))],
            "p_A09_ahead_gift_plus_laura2042": sm(((gA_ + lA_) > (gX + l42X) + 1).mean())}
    lr["L14"] = out14'''
assert b.endswith('    lr["L14"] = out14')
L14.BLOCK14 = b[: -len('    lr["L14"] = out14')] + extra.lstrip("\n")

def main():
    f = HERE / "A26_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    names = {k.split()[0]: k for k in L14.L10.SCENARIOS}
    blk = L14.L13.BLOCK13.replace('    lr["L13"] = out13', L14.BLOCK14)
    add = L14.LR8.ADD.replace('    res["LR05"] = lr', blk)
    block = L14.LR05.BLOCK.replace('    res["LR05"] = lr', add)
    L14.L11.EXTRA = L14.L11.EXTRA.replace('    out["L11"] = res', block)
    for k in sys.argv[1:] or ["S0", "S1", "S6"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L14"]
        out[names[k]] = {"A26_per_k": r["A26_per_k"], "check_XR_gift_mean": r["XR (V39)"]["gift_mean"]}
        print(names[k], json.dumps(out[names[k]], indent=1), flush=True)
        f.write_text(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
