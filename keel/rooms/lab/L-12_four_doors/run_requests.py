"""AI-generated (Claude Code), Thu 29 Oct 2026, the Genius Lab (round 2 beat 5, second pass). MODEL.
(Keel is a simulated team, AI-written.) Open requests to the Lab, answered on V29's design (LR8 "MB+T +lock"):
  ninety   (Kitchen, 27 Oct): the quoted 2031 bottom under the rule at p0.1, p1, p5, p50 and its model minimum
  top      (Courtroom 27 Oct + Long Room 28 Oct): "reaching the top" four ways: exact, within $1k, the top quoted
           rounded down to $1k, and to $5k; with the 2031 lock
  rung     (Library, 29 Oct, bank #71): paths where the ladder is funded in total (2042 projection, full rate path)
           but one rung is short of its cheque by over $1k, the largest such gap, and how many of those a pooled
           coupon account could not carry in time (running sum of rung surpluses, earliest cheque first, below -$1k)
  corner   (Writing Room, 27 Oct, line 3b; and the framework's door 2): payments short >$1k against the 2028 deposit
           ($0-$75k), with yields as on 22 Oct and 1 point lower before the Jan 2027 build
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | basis: LR8 run.py chain unchanged; one block appended | MODEL.
Run from repo root: python3 keel/rooms/lab/L-12_four_doors/run_requests.py [requests|corner]"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / "long_room" / "LR8_banked_at_the_mark" / "run.py"
_spec = importlib.util.spec_from_file_location("LR8", P)
LR8 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LR8)
LR05, L11 = LR8.LR05, LR8.L11
L10 = L11.L10

REQ = '''
    # ---- Genius Lab L-12, second pass: open requests on V29's design (MB+T +lock) ----
    cash, sold, g = at_2033(L33 + x * bill2, S33 + C, half_b, True, top, lockd)
    tot_short = np.maximum(S33 + extra_ - cash, 0) + unfilled
    q = q_mc
    pc = lambda a, ps: [round(float(np.percentile(a, p_))) for p_ in ps]
    rq = {"p_payment_short_over_1k": sm((tot_short > 1000).mean()),
          "ninety": {"quoted_bottom_p0.1_p1_p5_p50": pc(q, (0.1, 1, 5, 50)), "quoted_bottom_min": round(float(q.min())),
                     "p_quoted_bottom_at_least_125k": sm((q >= 125000).mean()), "p_at_least_120k": sm((q >= 120000).mean()),
                     "p_below_quoted_bottom": sm((g < q - 1e-6).mean())},
          "top": {"top_p50": round(float(np.median(top))),
                  "p_exact": sm((g >= top - 1).mean()), "p_within_1k": sm((g >= top - 1000).mean()),
                  "p_quoted_top_rounded_down_1k": sm((g >= np.floor(top / 1000) * 1000 - 1).mean()),
                  "p_quoted_top_rounded_down_5k": sm((g >= np.floor(top / 5000) * 5000 - 1).mean()),
                  "median_short_of_top_when_missed_1k": md(top - g, g < top - 1000)}}
    if FULL:
        iY = len(step_t) - 1
        V = np.zeros((N, len(RUNGS)))
        for jj, (py, (name, mat, cpn)) in enumerate(sorted(RUNGS.items())):
            T = yrs(T27, mat); y0p = np.maximum(curve(T + TOFF) + s27, YMIN)
            cc = (y0p if cpn is None else np.full(N, cpn)) / 100
            kk = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
            ii = np.clip(np.searchsorted(step_t, kk + TOFF), 0, len(step_t) - 1)
            relf = shifts[:, np.minimum(ii, iY)] - s27[:, None]
            ykk = np.maximum(y0p[:, None] + relf, YMIN) / 100
            dd = 1 + (cc / 2) * ((1 + ykk / 2) ** (2 * (T - kk))).sum(axis=1)
            db = 1 + (cc / 2) * ((1 + y0p[:, None] / 200) ** (2 * (T - kk))).sum(axis=1)
            V[:, jj] = PAY * dd / db
        net = V - PAY
        funded = net.sum(axis=1) >= -1000
        worst = (-net).max(axis=1)
        red = funded & (worst > 1000)
        run_min = np.cumsum(net, axis=1).min(axis=1)
        rq["rung"] = {"p_total_short_over_1k": sm((~funded).mean()),
                      "p_funded_in_total_but_one_rung_short_over_1k": sm(red.mean()), "n": int(red.sum()),
                      "largest_single_rung_gap_when_so": round(float(worst[red].max())) if red.any() else 0,
                      "median_single_rung_gap_when_so": md(worst, red),
                      "of_those_pooled_cash_short_in_time_over_1k": int((red & (run_min < -1000)).sum()),
                      "which_rung_is_worst_when_so_by_cheque_year": {str(2033 + j): int(((-net).argmax(axis=1)[red] == j).sum()) for j in range(len(RUNGS))}}
    lr["L12_requests"] = rq
    res["LR05"] = lr'''


def build(full):
    add = LR8.ADD
    add = add.replace('    res["LR05"] = lr', REQ.replace("if FULL:", f"if {full}:"))
    block = LR05.BLOCK.replace('    res["LR05"] = lr', add)
    return block


def main():
    mode = (sys.argv[1:] or ["requests"])[0]
    orig = L11.EXTRA
    out = {"stamp": "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 unless S0 | MODEL"}
    if mode == "requests":
        L11.EXTRA = orig.replace('    out["L11"] = res', build(True))
        for k in ("S0", "S1", "S6"):
            name = L11.SCEN[k]
            out[name] = L11.run(**L10.SCENARIOS[name])["LR05"]["L12_requests"]
            print(name, json.dumps(out[name], indent=1), flush=True)
    else:
        L11.EXTRA = orig.replace('    out["L11"] = res', build(False))
        for dy in (0.0, -1.0):
            for d28 in (0.0, 5_000.0, 10_000.0, 20_000.0, 30_000.0, 50_000.0, 75_000.0):
                key = f"dy_build {dy:+g}pt, 2028 deposit ${d28:,.0f}"
                r = L11.run(d28=d28, dy_build=dy)["LR05"]["L12_requests"]
                out[key] = {"p_payment_short_over_1k": r["p_payment_short_over_1k"],
                            "quoted_bottom_p5_p50": r["ninety"]["quoted_bottom_p0.1_p1_p5_p50"][2:]}
                print(key, json.dumps(out[key]), flush=True)
    (HERE / f"results_{mode}.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
