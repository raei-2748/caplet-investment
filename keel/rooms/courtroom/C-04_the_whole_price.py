"""AI-generated (Claude Code), Sat 31 Oct 2026, the Courtroom (round 4 beat 8). MODEL. (Keel is a simulated team,
AI-written.) C-04: Kai's first charge against LR-08's paragraph, "about $9,000 of her own money in a typical 2033".
That is a MEDIAN of (gift + what Laura keeps). A09's gift has a far fatter top (p95 ~$250k v ~$182k), so the median
may understate what the floor costs on average. Same engine, same paths, same f as LR-08 (imported, nothing changed):
per path, A09 minus XR in (gift + kept, 2033) and in (gift + Laura's money left in 2042); mean, median, spread; how
often XR leaves her ahead; and the same difference in the worst twentieth of 2028-30 stock markets (what the floor buys).
STAMP: as LR-08 (curve 22 Oct 2026, J.P. Morgan 2027 LTCMA world stocks 7.5% compound, 16.78% vol; 50,000 paths per
world + every start month since 1871). Run from repo root: python3 keel/rooms/courtroom/C-04_the_whole_price.py"""
import importlib.util, json, pathlib
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("lr08", ROOT / "keel/rooms/lauras_room/LR-08_the_bad_naming_day.py")
lr = importlib.util.module_from_spec(spec); spec.loader.exec_module(lr)
OUT = pathlib.Path(__file__).with_name("C-04_results.json")


def diff_stats(d, mask5):
    q = lambda a, v: round(float(np.percentile(a, v)))
    return {"mean": round(float(d.mean())), "p5_p25_p50_p75_p95": [q(d, v) for v in (5, 25, 50, 75, 95)],
            "share_xr_ahead": round(float((d < 0).mean()), 4),
            "worst5pct_2028_30_mean": round(float(d[mask5].mean())), "worst5pct_2028_30_p50": q(d[mask5], 50)}


def run():
    W = {"house": lr.gens.lognormal(lr.N), "storms": lr.gens.regime(lr.N), "bootstrap": lr.gens.bootstrap(lr.N),
         "history": lr.gens.history()}
    res, f = {"stamp": "as LR-08; A09 minus XR, per path; negative = XR ahead", "worlds": {}}, None
    for name, p in W.items():
        xr = lr.xr_marked(p)
        if f is None:
            f = lr.calibrate(p, float(np.median(xr["bottom"])))
        a = lr.a09(p, f)
        r3 = lr.stock_3y(p); c5 = r3 <= np.percentile(r3, 5)
        t33x, t33a = xr["gift"] + xr["kept33"], a["gift"] + a["kept33"]
        t42x, t42a = xr["gift"] + xr["laura_2042"], a["gift"] + a["laura_2042"]
        res["worlds"][name] = {
            "gift_plus_kept_2033": {"xr_mean": round(float(t33x.mean())), "a09_mean": round(float(t33a.mean())),
                                    "diff": diff_stats(t33a - t33x, c5)},
            "gift_plus_laura_2042": {"diff": diff_stats(t42a - t42x, c5)},
            "gift_only": {"diff": diff_stats(a["gift"] - xr["gift"], c5)}}
        print(name, json.dumps(res["worlds"][name]))
    res["f"] = f
    OUT.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    run()
