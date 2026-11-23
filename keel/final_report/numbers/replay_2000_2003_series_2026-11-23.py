"""Mon 23 Nov 2026: the 2000-2003 replay's world-share fall on ONE series read at source.
Series: MSCI ACWI Index, USD, PRICE (index_variant=STRD, code 892400), end-of-month levels, read 23 Nov 2026 at
https://app2.msci.com/products/service/index/indexmaster/getLevelDataForGraph?currency_symbol=USD&index_variant=STRD&start_date=19991201&end_date=20030228&data_frequency=END_OF_MONTH&index_codes=892400
(read through the WebFetch tool; levels identical to card Q85's 16 Nov read at the five dates it kept).
Own arithmetic below (Keel arithmetic, MODEL-free)."""
import json, pathlib
L = {"1999-12": 341.6261446134503, "2000-01": 322.8336191306643, "2000-12": 290.11335667934014,
     "2002-12": 190.79652005872836, "2003-01": 185.03288527891905, "2004-12": 284.5205214535708}  # 2004-12 from Q85 read
# old figures: price to Dec 2000 spliced to GROSS after (gross starts 29 Dec 2000); gross levels from card Q85
G = {"2000-12": 379.85859530133405, "2002-12": 258.79533236342826, "2003-01": 251.24176166627845}
r = lambda a, b: L[b] / L[a] - 1
out = {"series": "MSCI ACWI USD price, code 892400, STRD, end of month", "read": "2026-11-23",
       "levels": L,
       "end_Jan2000_to_end_Jan2003": r("2000-01", "2003-01"),
       "end_Jan2000_to_end_Dec2002": r("2000-01", "2002-12"),
       "end_Dec1999_to_end_Dec2002": r("1999-12", "2002-12"),
       "end_Dec1999_to_end_Jan2003": r("1999-12", "2003-01"),
       "old_start_of_month_spliced": L["2000-12"] / L["1999-12"] * G["2002-12"] / G["2000-12"] - 1,
       "old_end_of_month_spliced": L["2000-12"] / L["2000-01"] * G["2003-01"] / G["2000-12"] - 1,
       "rise_end_Jan2003_to_end_Dec2004_price": r("2003-01", "2004-12")}
assert round(out["end_Jan2000_to_end_Jan2003"] * 100, 1) == -42.7
assert round(out["end_Dec1999_to_end_Dec2002"] * 100, 1) == -44.2
assert round(out["end_Jan2000_to_end_Dec2002"] * 100, 1) == -40.9
assert round(out["old_start_of_month_spliced"] * 100, 1) == -42.1 and round(out["old_end_of_month_spliced"] * 100, 1) == -40.6
pathlib.Path(__file__).with_name("results_replay_2000_2003_series_2026-11-23.json").write_text(json.dumps(out, indent=1))
print({k: round(v * 100, 2) for k, v in out.items() if isinstance(v, float)})
