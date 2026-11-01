"""LR-09, Laura's Room, Sun 1 Nov 2026 (round 5 beat 6). (Keel is a simulated team, AI-written.)

The promise has no number: how often does V47's design pay all ten cheques in full, at any size, and does that
survive the two failures the IPS names (a smaller 2028 deposit; yields lower before the 2027 build)?

Re-uses the Genius Lab's L-15 chain unchanged (curve 22 Oct 2026, J.P. Morgan 2027 world stocks 7.5%, 200,000 paths,
seed 20261016, V47's design via L-13 -> L-14 -> A26) and only adds three outputs to each arm: the share of paths with
ANY cheque shortfall, over $100, and the median shortfall when there is one. Writes LR-09_results.json beside this file;
never touches the Lab's results. MODEL.

    python3 keel/rooms/lauras_room/LR-09_the_promise_has_no_number.py            # S0 S1 S2 S4 S6 S9
    python3 keel/rooms/lauras_room/LR-09_the_promise_has_no_number.py S0 S6      # a subset
"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
L15P = HERE.parent / "lab" / "L-15_hold_it_then_say_it" / "run.py"
_s = importlib.util.spec_from_file_location("L15", L15P); L15 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L15)

OLD = '"p_cheque_short_over_1k": sm((tot_short(cash) > 1000).mean()),'
NEW = OLD + (' "p_cheque_short_any": float((tot_short(cash) > 0.5).mean()),'
             ' "p_cheque_short_over_100": float((tot_short(cash) > 100).mean()),'
             ' "short_p50_when_short": float(np.median(tot_short(cash)[tot_short(cash) > 0.5]))'
             ' if (tot_short(cash) > 0.5).any() else 0.0,')
assert L15.BLOCK15.count(OLD) == 1
L15.BLOCK15 = L15.BLOCK15.replace(OLD, NEW)
L14 = L15.L14
KEEP = ("p_top_reached", "p_below_quoted_bottom", "p_cheque_short_any", "p_cheque_short_over_100",
        "p_cheque_short_over_1k", "short_p50_when_short", "gift_mean")


# P4's recession in one world (Felix's round-3 test): yields a point lower before the 2027 build AND the 2028 deposit
# halved, recession-linked stocks (rho 0.5). The Lab's S3/S5 (deposit missing) break L-15's fifths sort, so not run.
L14.L10.SCENARIOS.setdefault("S9 yields 1pt lower before the build + 2028 deposit halved",
                             dict(dy_build=-1.0, d28=75_000.0))


def main():
    b = L14.BLOCK14.replace("for k in (0.80, 0.65):", "for k in (0.80, 0.76):")
    b = b + L15.BLOCK15
    blk = L14.L13.BLOCK13.replace('    lr["L13"] = out13', b)
    add = L14.LR8.ADD.replace('    res["LR05"] = lr', blk)
    block = L14.LR05.BLOCK.replace('    res["LR05"] = lr', add)
    L14.L11.EXTRA = L14.L11.EXTRA.replace('    out["L11"] = res', block)
    names = {k.split()[0]: k for k in L14.L10.SCENARIOS}
    f = HERE / "LR-09_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "V47's design via the Lab's L-15 chain, unchanged | three outputs added | MODEL")
    for k in sys.argv[1:] or ["S0", "S1", "S2", "S4", "S6", "S9"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L15"]["A_order_and_lock_timing"]
        out[names[k]] = {arm: {kk: r[arm][kk] for kk in KEEP if kk in r[arm]}
                         for arm in ("same day (V47)", "skipped everywhere (no lock)")}
        print(names[k], json.dumps(out[names[k]]), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
