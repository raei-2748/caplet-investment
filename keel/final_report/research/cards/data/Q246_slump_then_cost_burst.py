"""Card Q246 (Tue 24 Nov 2026, Sydney): a slump then a cost burst, a level deeper.

Keel arithmetic on series read at source on Tue 24 Nov 2026 (Sydney). Research notes, not report prose; no plan
figure is made here (the plan's own Taiwan figures are NUMBERS 8q and 8x).

Data, every value embedded below as read today:
  * MSCI ACWI Index, USD, PRICE (index_variant=STRD, code 892400), end-of-month levels, Jan 1997 to Oct 2026, from
    https://app2.msci.com/products/service/index/indexmaster/getLevelDataForGraph?currency_symbol=USD&index_variant=STRD
    &start_date=...&end_date=...&data_frequency=END_OF_MONTH&index_codes=892400 (four reads through WebFetch).
  * DGBAS construction cost index, general index (營造工程總指數, 2021 = 100), monthly Jan 1991 to Oct 2026, CSV output of
    https://nstatdb.dgbas.gov.tw/dgbasall/webMain.aspx?sys=220&ym=8001&ymt=11510&kind=21&type=1&funid=A030502015
    &cycle=41&outmode=2&compmode=0&outkind=1&fldspc=0,1, (Parallel web_fetch). Also the building-construction
    sub-index (fldspc=130,1), metal products and rebar (fldspc=20,2) for Jan 2003 to Dec 2005.
  * FRED EXTAUS (G.5, monthly averages, last updated 2026-11-02), https://fred.stlouisfed.org/data/EXTAUS.txt, read
    today through Parallel web_fetch. The full series is the repo's copy of the same FRED release,
    keel/final_report/numbers/extaus_fred_read_2026-11-22.txt; every month this script prints is asserted equal to
    today's read (FX_TODAY below).
  * FRED WPUSI012011 (BLS PPI, construction materials, 1982 = 100, last updated 2026-11-13) and CPIAUCNS (CPI-U, NSA,
    1982-84 = 100, last updated 2026-11-10), https://fred.stlouisfed.org/data/<id>.txt, the months used.
  * FRED SPASTT01USM661N (OECD, share prices for the United States, 2015 = 100, monthly averages, last updated
    2026-11-16), the months used.
  * Architectural Services Department, Hong Kong, Building Works Tender Price Index (quarterly; Q1 1970 = 100 per card
    Q66, the base is not printed on the page), https://www.archsd.gov.hk/en/reports/bwtpi-published-in-earlier-years.html.

Conventions (NUMBERS 8j, 8q, 8x):
  * Laura's shape: world shares bought at month 0, the 2031 meetings at month 36, the contribution at month 60. The
    building move runs from the meetings' index month to the contribution's (8q: purchase + 36 to + 60 months; 8x's
    replay: Jan 2003 to Dec 2004).
  * US-dollar cost of a fixed NT$ budget = index_end / index_start x (NT$ per US$ at start / at end) - 1 (8q's joint
    move). Two-year windows: start month to the same month two years later.
  * MSCI: a start-of-month date uses the previous month's close (Laura's calendar, 8x); "end-Jan" uses January's close.

Run: python3 -I keel/final_report/research/cards/data/Q246_slump_then_cost_burst.py   (well under a second)
"""
import json
import os
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_FINAL = os.path.normpath(os.path.join(HERE, "..", "..", ".."))  # .../keel/final_report

# ---------------------------------------------------------------- MSCI ACWI price, USD, end of month (read today)
ACWI_TEXT = """
1997 204.85838707062786 207.33925531701456 202.84233088811013 208.9934842977204 221.10853721290732 232.0807530395079 242.23691464399576 224.91706710393143 236.58184115228374 222.17416797344669 225.256009214822 227.8745002207188
1998 232.57611225966096 248.1644646933163 258.38860334619795 260.4547404569424 255.14110163296596 259.39512401121584 259.11822779917867 222.45210288681002 226.52678844813371 246.87438417727301 261.5273229093827 273.3014408293663
1999 278.55069605036755 271.2108336262803 283.0434533619148 294.9154193350139 284.106648628376 297.89204697036774 296.31061806559387 295.59876147998114 292.0552922056045 306.4968184078302 315.678552953464 341.6261446134503
2000 322.8336191306643 323.59182176860276 344.49806574210595 328.68395800471603 319.77552940839433 330.208686066807 320.1600318108838 329.76054552306164 311.3085053713249 304.89547714413374 285.6820995115192 290.11335667934014
2001 297.27106254726164 271.96821659565 253.11723538705982 271.0887101285381 267.3743963170163 258.84445290668526 254.5417554239939 242.41443532991798 219.96113625246042 224.48187288229465 238.0002866732213 240.03300546787315
2002 233.2584451315602 231.20776280801357 241.17131546303176 233.13116425447825 232.82355234215717 218.2517953366431 199.7291529062495 199.84643309081673 177.6254093508385 190.48893367960346 200.60437414795422 190.79652005872836
2003 185.03288527891905 181.41565389005171 180.20128647499732 195.75280052407354 206.53530278669396 210.07926048750255 214.45512421753102 219.09810165135548 220.15128371832887 233.23615023266206 236.4241099023149 251.13111782587663
2004 255.1950059237385 259.51114873597254 257.4303903579204 250.93196593654676 252.27785169096083 256.8948047348999 248.45089297910093 249.5068094049302 254.37335610792283 260.3790943980712 274.1704828312793 284.5205214535708
2005 278.29937602205104 287.49405135397905 280.5116914497408 273.702213988287 278.07380782224106 280.43791306576117 290.5703866785001 292.20212257507364 300.6039695638 292.3189241395712 302.43244371824693 309.63012106751114
2006 324.65813315717395 323.74461243898463 329.7906687150227 340.1898413057445 325.7381736711645 325.1079669147774 327.03680164403175 334.8090470324752 338.27588775158557 350.7495462360612 360.04292936805314 367.783806531323
2007 371.2022094222974 368.7770389381529 375.2951515336205 391.1750535695232 401.5154088616512 399.7821248573574 393.33941729993813 391.48918820470067 411.9179782928689 427.6292885952327 408.0993587807016 403.24633949543824
2008 369.93061056308017 370.4065608717574 363.9808476855142 383.2954944605176 387.74383744375024 355.3979739232564 345.745524026679 337.61131687940036 294.79028438692416 236.1113984346851 220.0495728772012 227.68339971769205
2009 208.02274057316058 187.1676493556246 202.03607783505933 225.24083447963582 246.6937692454049 244.90490513412863 266.14183950422824 275.09560988775746 287.2324189701082 282.58849234228074 293.66663212307327 299.43515661954115
2010 286.32728732979473 289.4973817898959 307.4044336843655 307.34781936502685 277.17303420271526 268.2472928760135 289.75105821787406 279.0642622167077 305.1635251875188 315.94665250105083 308.38110316463593 330.6363804691693
2011 335.58085031373366 344.82257160333205 343.64048112608646 356.90220683959853 347.89573420116756 341.81703614112735 335.8960605849276 310.61798220696824 280.63940884692107 310.43421509758247 300.4467466386415 299.5107378754187
2012 316.654852060744 331.9274271618662 333.29731101738497 328.6725904387576 297.98461130951046 312.1108357798507 316.0236550786844 322.1365499902804 331.5775947601931 329.0670235173977 332.6418091982406 339.74919196153775
2013 355.1016014670633 354.4303560751417 360.05669739552116 369.4220268210552 367.1947995036501 355.8113107496407 372.4897911790431 363.9761374191698 382.06995252619186 397.10935873833836 402.04749439674106 408.5487646738515
2014 391.9210840567256 410.129421825798 411.0213084717236 414.09401788480136 421.53415078218796 428.74630344020767 423.0430560029281 431.54944549214076 416.85020801048563 419.45086129340643 425.8214254964101 417.12033464196185
2015 410.3278787071175 432.4743044781271 424.75843828062995 436.29609800567164 434.5147578896478 423.5093877665465 426.781417474648 396.7333059919685 381.6511911573598 411.2490609630876 407.1971264183833 399.3624330015731
2016 375.0167369503212 371.66231980035286 398.2554852324853 403.33967540163917 402.57438606332806 399.2897308198123 416.0883600475038 416.61346197339105 418.43435041851814 411.0149937641976 413.42969083415045 421.8394074918882
2017 433.1283190202218 444.5033003221542 448.86637846968057 455.1734388089914 463.79407207373544 465.0878986294058 477.58346590643646 478.4056153123971 486.8786739779294 496.6246686039396 505.44238431960247 513.0259476741394
2018 541.6732571620657 518.0791014972415 505.8076426628622 509.69378159412213 508.76903771284503 505.19823270972995 519.8179353362044 522.8810068009703 524.2526706226415 484.5709655484851 490.85732588636927 455.6621751123716
2019 491.19414377789485 503.48056876683984 508.54849037303586 524.8438091862882 492.1152970867467 523.442031988877 524.3502953532072 510.8770779704405 520.6508846699153 534.4112017515122 546.694995315811 565.2439077721461
2020 558.6211846083633 512.7573146134496 442.34647605292224 489.1686648241692 509.4703388767405 524.9076299467093 551.894367282309 584.8639335453655 565.148481664562 550.9953598571941 618.2657414306195 646.2683419236695
2021 642.9065652883003 657.1462336454132 673.2877200769058 701.8300475649576 711.4503671438607 719.9699610603276 724.2089778567506 741.2705343081078 709.5119874581495 745.2286279640575 726.5314411624557 754.828116375572
2022 717.3754821065744 698.0201945711951 711.5577179610269 653.6670414475088 652.8142174225576 596.7739327000652 637.717121374625 613.1067162001721 553.3712786711997 586.3744596263949 630.9183900600289 605.3823322507119
2023 648.3652880210356 629.0228868757058 646.76207550648 654.9967043439431 646.3746630556441 682.8413421003987 707.1094314901212 686.150393288168 656.8201325574033 636.6545879343446 694.3798747779718 726.995723023297
2024 730.8382559197465 761.2820461586822 783.583601732468 756.6088864524655 785.5369243858427 802.0098586167662 814.1553716152722 833.6818308140166 851.783137718947 832.3028226726439 862.4888844463959 841.3320721873529
2025 869.0398211714045 862.9489856267288 827.1546034372934 833.5375276877953 879.495991950266 917.8930228930487 929.6204972015677 951.5678199272522 984.7812687128986 1006.2324299305712 1005.1389191501662 1014.6233306881799
2026 1044.2570636032622 1056.764820723422 978.9434687032649 1077.1017639155773 1130.747036328151 1120.4593185643917 1120.509306993309 1149.2199337456066 1134.770279198428 1115.5514444837934
"""

# ---------------------------------------------------------------- DGBAS construction cost index, total (read today)
CCI_TEXT = """
1991 43.91 43.99 43.89 43.93 43.82 43.68 43.72 43.71 43.89 44.00 44.09 44.10
1992 44.46 44.82 48.85 50.48 50.62 50.89 51.62 51.90 52.48 52.91 52.94 53.70
1993 53.85 53.65 53.91 54.14 54.13 53.89 53.73 53.71 53.42 53.12 52.87 52.41
1994 51.90 51.95 51.81 51.76 51.54 51.33 51.08 51.02 51.11 51.26 51.03 50.86
1995 51.17 51.60 51.83 51.90 51.83 52.08 51.90 52.07 52.18 52.15 52.11 51.91
1996 51.85 51.74 51.62 51.50 51.40 51.09 51.26 51.67 51.75 51.67 51.53 51.67
1997 51.70 52.13 52.38 52.62 52.77 52.75 52.74 52.70 52.79 52.72 52.98 53.30
1998 53.72 54.02 54.02 53.93 53.97 54.09 54.09 54.09 53.99 53.98 53.78 53.57
1999 53.45 53.46 53.52 53.66 53.69 53.66 53.71 53.65 53.59 53.76 53.74 53.70
2000 53.35 53.41 53.62 53.66 53.67 53.65 53.56 53.33 53.14 53.15 52.99 52.91
2001 52.84 52.77 52.69 52.57 52.56 52.80 52.91 53.12 52.91 52.93 52.95 52.93
2002 52.98 53.14 53.30 53.53 53.84 54.49 54.57 54.49 54.16 54.13 54.25 54.48
2003 55.05 55.97 56.69 56.51 56.08 55.89 56.31 56.59 56.69 56.64 57.00 58.18
2004 60.12 63.17 64.92 64.47 64.06 63.78 64.93 65.62 65.58 65.98 65.53 65.18
2005 64.91 65.30 65.53 65.43 64.95 64.24 64.13 64.39 64.92 64.98 64.88 65.04
2006 65.38 65.66 66.50 67.92 70.31 70.78 71.10 71.02 71.23 71.59 71.83 71.84
2007 72.11 72.75 73.82 74.95 75.47 76.16 76.25 76.44 76.94 77.91 78.11 79.41
2008 81.09 82.87 86.00 88.13 89.74 91.98 92.10 90.92 87.90 85.00 81.59 80.33
2009 79.77 79.70 78.52 78.29 78.19 78.19 78.45 78.92 79.33 78.77 78.63 78.97
2010 79.80 80.12 81.01 82.75 82.51 81.31 81.05 81.26 81.36 81.23 81.50 82.01
2011 83.02 83.35 84.12 83.98 84.07 84.15 84.11 84.31 84.47 84.56 84.01 84.23
2012 84.45 84.60 84.87 85.70 85.96 85.43 84.95 84.81 84.19 83.71 84.00 84.11
2013 84.53 84.75 84.88 84.48 84.14 83.92 83.96 84.10 84.49 84.48 84.69 84.88
2014 85.19 85.26 85.28 85.82 86.03 86.42 86.62 86.72 86.61 86.19 85.96 85.74
2015 85.43 84.93 84.69 84.50 84.10 84.01 83.42 82.93 82.74 82.14 82.02 81.79
2016 81.64 81.46 81.56 82.48 83.02 82.44 82.18 82.13 81.93 81.73 82.24 83.02
2017 83.52 83.59 83.98 83.71 83.20 83.28 83.50 84.38 84.97 84.89 85.15 85.33
2018 85.80 85.61 86.08 86.22 86.47 86.78 87.30 87.49 87.82 88.13 87.94 87.74
2019 87.84 88.57 89.04 89.11 88.93 89.06 89.05 89.20 89.00 88.66 88.82 89.23
2020 89.52 89.42 89.64 89.23 89.29 89.57 89.59 89.94 90.59 90.84 91.31 92.76
2021 94.90 94.94 95.97 97.34 99.60 101.25 101.87 102.15 102.39 102.98 103.36 103.25
2022 103.67 104.47 106.88 108.83 109.05 109.02 108.11 107.32 107.96 107.69 107.45 107.92
2023 108.69 109.21 109.49 109.60 109.00 108.76 108.96 109.04 109.25 109.48 109.38 109.88
2024 110.26 110.48 110.50 111.07 111.60 111.91 112.02 111.82 111.56 111.75 112.04 111.84
2025 111.81 112.16 112.56 112.49 112.23 111.97 111.83 112.15 112.09 112.43 112.66 112.86
2026 113.81 114.69 115.62 117.50 118.77 119.16 119.14 119.48 120.26 120.50
"""
# Sub-indices read today, Jan 2003 to Dec 2005 (2021 = 100): building-construction total, metal products, rebar
BLD = {"2003-01": 56.89, "2003-12": 59.99, "2004-03": 67.26, "2004-10": 68.20, "2004-12": 67.33, "2005-01": 67.00}
METAL = {"2003-01": 44.56, "2003-12": 53.48, "2004-03": 70.27, "2004-12": 64.14}
REBAR = {"2003-01": 48.19, "2003-12": 59.80, "2004-03": 82.42, "2004-12": 68.56}

# EXTAUS values read today (Parallel web_fetch of FRED's EXTAUS.txt), for every month this script prints
FX_TODAY = {"1988-01": 28.6278, "1991-01": 27.1968, "1993-01": 25.4519, "2002-01": 35.0271, "2002-12": 34.7990,
            "2003-01": 34.5714, "2003-03": 34.7216, "2004-03": 33.2522, "2004-10": 33.7748, "2004-12": 32.1703,
            "2005-01": 31.8465, "2005-03": 31.1055, "2006-07": 32.6170, "2008-07": 30.4141, "2009-01": 33.3695,
            "2009-02": 34.2389, "2009-03": 34.3041, "2010-12": 29.9014, "2011-01": 29.1105, "2011-02": 29.2779,
            "2011-03": 29.4930, "2019-08": 31.3886, "2021-08": 27.8591, "2026-10": 32.2695}

# US series (FRED), months used, read today
PPI_MAT = {"1972-01": 42.8, "1973-01": 44.9, "1974-12": 58.0, "1975-01": 58.8, "1976-01": 62.5, "1976-12": 68.0,
           "1977-12": 73.5, "2003-01": 144.4, "2004-12": 166.3, "2006-07": 182.3, "2009-01": 193.3,
           "2010-12": 194.2, "2011-12": 202.2}
CPI = {"1972-01": 41.1, "1973-01": 42.6, "1974-12": 51.9, "1975-01": 52.1, "1976-01": 55.6, "1976-12": 58.2,
       "1977-12": 62.1, "2003-01": 181.7, "2004-12": 190.3, "2009-01": 211.143, "2010-12": 219.179,
       "2011-12": 225.672}
US_SHARES = {"1972-01": 5.663243, "1973-01": 6.376020, "1974-12": 3.506448, "1975-01": 3.818399,
             "1976-01": 5.081689, "1988-01": 13.918340, "1991-01": 17.622130, "2000-01": 62.866020,
             "2003-01": 47.349900}
# Hong Kong BWTPI, quarterly, read today
HK = {"1972-Q4": 158, "1973-Q1": 160, "1974-Q2": 213, "1974-Q4": 191, "1975-Q1": 145, "1975-Q3": 137,
      "1976-Q4": 149, "2003-Q1": 720, "2004-Q4": 701, "2008-Q3": 1401, "2009-Q1": 1074, "2009-Q2": 983,
      "2010-Q1": 1134, "2010-Q4": 1266, "2011-Q1": 1273, "2011-Q4": 1408, "2012-Q4": 1496}


def parse_year_rows(text):
    out = {}
    for line in text.strip().splitlines():
        parts = line.split()
        year = int(parts[0])
        for i, v in enumerate(parts[1:]):
            out[f"{year}-{i + 1:02d}"] = float(v)
    return out


ACWI = parse_year_rows(ACWI_TEXT)
CCI = parse_year_rows(CCI_TEXT)
assert len(ACWI) == 358 and len(CCI) == 430


def read_fx():
    path = os.path.join(REPO_FINAL, "numbers", "extaus_fred_read_2026-11-22.txt")
    fx = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line[:1].isdigit():
                d, v = line.split()
                fx[d[:7]] = float(v)
    return fx


FX = read_fx()
for m, v in FX_TODAY.items():
    assert FX[m] == v, (m, FX[m], v)  # today's read equals the repo's 22 Nov copy of the same release


def months(start, end):
    y, m = map(int, start.split("-"))
    ye, me = map(int, end.split("-"))
    out = []
    while (y, m) <= (ye, me):
        out.append(f"{y}-{m:02d}")
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return out


def shift(ym, k):
    y, m = map(int, ym.split("-"))
    t = y * 12 + (m - 1) + k
    return f"{t // 12}-{t % 12 + 1:02d}"


def pct(a, b):
    return b / a - 1


def joint(a, b):
    """US-dollar cost rise of a fixed NT$ budget from month a to month b (8q's joint move)."""
    return CCI[b] / CCI[a] * FX[a] / FX[b] - 1


def ntd_move(a, b):
    return FX[a] / FX[b] - 1


R = {}

# ---- (a) the share slump on MSCI's own price series
R["a_endJan2000_endJan2003"] = pct(ACWI["2000-01"], ACWI["2003-01"])
R["a_endDec1999_endDec2002"] = pct(ACWI["1999-12"], ACWI["2002-12"])
R["a_endJan2000_endDec2002"] = pct(ACWI["2000-01"], ACWI["2002-12"])
R["a_peak_Mar2000_to_low_Sep2002"] = pct(ACWI["2000-03"], ACWI["2002-09"])
R["a_rise_endJan2003_endDec2004"] = pct(ACWI["2003-01"], ACWI["2004-12"])
R["a_rise_endDec2002_endDec2004"] = pct(ACWI["2002-12"], ACWI["2004-12"])
R["a_five_years_endDec1999_endDec2004"] = pct(ACWI["1999-12"], ACWI["2004-12"])
assert round(R["a_endJan2000_endJan2003"] * 100, 1) == -42.7
assert round(R["a_endDec1999_endDec2002"] * 100, 1) == -44.2
assert round(R["a_endJan2000_endDec2002"] * 100, 1) == -40.9
assert round(R["a_rise_endJan2003_endDec2004"] * 100, 1) == 53.8  # NUMBERS 9 (Mon 23 Nov evening)

# ---- (b) the building cost that followed, and the Taiwan dollar over the same window
R["b_ntd_Jan2003_Dec2004"] = pct(CCI["2003-01"], CCI["2004-12"])
R["b_usd_Jan2003_Dec2004"] = joint("2003-01", "2004-12")
R["b_fx_Jan2003_Dec2004"] = ntd_move("2003-01", "2004-12")
R["b_ntd_Jan2003_Jan2005"] = pct(CCI["2003-01"], CCI["2005-01"])
R["b_usd_Jan2003_Jan2005"] = joint("2003-01", "2005-01")
R["b_ntd_Dec2002_Dec2004"] = pct(CCI["2002-12"], CCI["2004-12"])
R["b_usd_Dec2002_Dec2004"] = joint("2002-12", "2004-12")
R["b_ntd_Jan2003_peak_Oct2004"] = pct(CCI["2003-01"], CCI["2004-10"])
R["b_usd_Jan2003_Oct2004"] = joint("2003-01", "2004-10")
R["b_ntd_Dec2003_Mar2004_three_months"] = pct(CCI["2003-12"], CCI["2004-03"])
R["b_ntd_Jan2003_Dec2003"] = pct(CCI["2003-01"], CCI["2003-12"])
R["b_ntd_low_May2001_to_Dec2002"] = pct(CCI["2001-05"], CCI["2002-12"])
R["b_ntd_Jan2002_Dec2004"] = pct(CCI["2002-01"], CCI["2004-12"])
R["b_building_sub_Jan2003_Dec2004"] = pct(BLD["2003-01"], BLD["2004-12"])
R["b_metal_Jan2003_Dec2004"] = pct(METAL["2003-01"], METAL["2004-12"])
R["b_rebar_Jan2003_Dec2004"] = pct(REBAR["2003-01"], REBAR["2004-12"])
R["b_rebar_Dec2003_Mar2004"] = pct(REBAR["2003-12"], REBAR["2004-03"])
R["b_rebar_Jan2003_Mar2004"] = pct(REBAR["2003-01"], REBAR["2004-03"])
assert round(R["b_ntd_Jan2003_Dec2004"] * 100, 1) == 18.4 and round(R["b_usd_Jan2003_Dec2004"] * 100, 1) == 27.2
assert round(R["b_ntd_Jan2003_Jan2005"] * 100, 1) == 17.9 and round(R["b_usd_Jan2003_Jan2005"] * 100, 1) == 28.0

# On $115,000 (the stated top, NUMBERS 8q's convention: need = rise x $115,000; pots are 8q's central ones)
TOP, POT_EXCESS, POT_HALF = 115_000, 28_682, 21_179
need = R["b_usd_Jan2003_Dec2004"] * TOP
R["b_need_on_top_usd"] = need
R["b_left_with_excess"] = POT_EXCESS - need
R["b_left_half_kept_alone"] = POT_HALF - need

# Cross-check today's DGBAS read against card Q131's earlier read (all 430 months)
q131 = {}
with open(os.path.join(HERE, "Q131_cci_parts_ntd_monthly.csv"), encoding="utf-8") as fh:
    head = fh.readline().strip().split(",")
    i_m, i_c, i_f = head.index("month"), head.index("cci_total"), head.index("twd_per_usd")
    for line in fh:
        p = line.strip().split(",")
        q131[p[i_m]] = (float(p[i_c]), float(p[i_f]))
R["check_cci_months_equal_to_Q131"] = sum(1 for m in CCI if abs(q131[m][0] - CCI[m]) < 1e-9)
R["check_fx_months_equal_to_Q131"] = sum(1 for m in CCI if abs(q131[m][1] - FX[m]) < 1e-9)
assert R["check_cci_months_equal_to_Q131"] == 430 and R["check_fx_months_equal_to_Q131"] == 430

# ---- (c) the four episodes since 1991 (two-year joint rises of 28% or more), and what shares did before each
starts = months("1991-01", "2024-10")
assert len(starts) == 406
jr = {s: joint(s, shift(s, 24)) for s in starts}
sorted_jr = sorted(jr.values())
R["c_windows"] = len(starts)
R["c_worst"] = max(jr.values())
R["c_worst_start"] = max(jr, key=jr.get)
R["c_count_at_or_above_28pct"] = sum(1 for v in jr.values() if v >= 0.28)
big = [s for s in starts if jr[s] >= 0.28]
runs, cur = [], [big[0]]
for s in big[1:]:
    if s == shift(cur[-1], 1):
        cur.append(s)
    else:
        runs.append(cur)
        cur = [s]
runs.append(cur)
R["c_runs_of_start_months"] = [(r[0], r[-1], len(r)) for r in runs]
assert round(R["c_worst"] * 100, 1) == 38.9 and R["c_worst_start"] == "2006-07"
assert R["c_count_at_or_above_28pct"] == 20


def acwi_before(start):
    """World shares over the 36 months before a window starts (Laura's purchase to her meetings).
    Start-of-month dates: the close of the month before each date (Laura's calendar, NUMBERS 8x)."""
    a, b = shift(start, -37), shift(start, -1)
    if a not in ACWI:
        return None
    return pct(ACWI[a], ACWI[b])


episodes = {"1991-93": ("1991-01", "1991-05"), "2002-05": ("2002-03", "2003-05"),
            "2006-08": ("2006-02", "2006-08"), "2019-21": ("2019-06", "2019-09")}
ep = {}
for name, (s0, s1) in episodes.items():
    ss = [s for s in months(s0, s1) if jr[s] >= 0.28]
    before = [acwi_before(s) for s in ss]
    ep[name] = {"windows_at_28pct": len(ss), "largest_joint": max(jr[s] for s in ss),
                "largest_start": max(ss, key=lambda s: jr[s]),
                "acwi_36m_before_min": min(before) if before[0] is not None else None,
                "acwi_36m_before_max": max(before) if before[0] is not None else None}
R["c_episodes"] = ep
assert sum(v["windows_at_28pct"] for v in ep.values()) == 20
# 1991-93: MSCI serves nothing before 1997, so the stand-in is OECD US share prices (monthly averages)
R["c_1991_us_shares_Jan1988_Jan1991"] = pct(US_SHARES["1988-01"], US_SHARES["1991-01"])

# Every meetings month whose 36 months before saw world shares 30% or more down, and the next 24 months in Taiwan
slump_meetings = [s for s in months("2000-01", "2024-10") if acwi_before(s) is not None and acwi_before(s) <= -0.30]
R["c_slump_meetings_count"] = len(slump_meetings)
R["c_slump_meetings_first_last"] = (slump_meetings[0], slump_meetings[-1])
groups, cur = [], [slump_meetings[0]]
for s in slump_meetings[1:]:
    if s == shift(cur[-1], 1):
        cur.append(s)
    else:
        groups.append(cur)
        cur = [s]
groups.append(cur)
R["c_slump_groups"] = []
for g in groups:
    vals = [jr[s] for s in g if s in jr]
    R["c_slump_groups"].append({"first": g[0], "last": g[-1], "n": len(g),
                                "acwi_worst": min(acwi_before(s) for s in g),
                                "joint_next24_min": min(vals), "joint_next24_median": statistics.median(vals),
                                "joint_next24_max": max(vals),
                                "cost_ntd_next24_median": statistics.median(pct(CCI[s], CCI[shift(s, 24)]) for s in g),
                                "fx_next24_median": statistics.median(ntd_move(s, shift(s, 24)) for s in g)})
all_med = statistics.median(jr.values())
R["c_all_406_windows_median_joint"] = all_med
# Laura's January calendar: meetings in January after a 30% slump
R["c_january_slump_meetings"] = {s: {"acwi_before": acwi_before(s), "joint_next": joint(s, shift(s, 23)),
                                     "cost_ntd_next": pct(CCI[s], CCI[shift(s, 23)])}
                                 for s in slump_meetings if s.endswith("-01")}

# The 2009-11 case named in 8q (meetings 2009 after the 2008 slump): Feb 2009 to Feb 2011 and Mar 2009 to Mar 2011
R["c_2009_Feb_joint"] = joint("2009-02", "2011-02")
R["c_2009_Feb_cost_ntd"] = pct(CCI["2009-02"], CCI["2011-02"])
R["c_2009_Feb_fx"] = ntd_move("2009-02", "2011-02")
R["c_2009_Mar_joint"] = joint("2009-03", "2011-03")
R["c_2009_Jan_to_Dec2010_joint"] = joint("2009-01", "2010-12")
R["c_2009_Jan_acwi_before"] = acwi_before("2009-01")
R["c_2009_Feb_acwi_before"] = acwi_before("2009-02")

# ---- (d) outside Taiwan
# Hong Kong (HK$ linked to the US$ at about 7.80 since 17 Oct 1983, so HK$ tender prices are US$ prices within the band)
R["d_hk_acwi_bought_Jan2006_meet_Jan2009"] = pct(ACWI["2005-12"], ACWI["2008-12"])
R["d_hk_bwtpi_Q1_2009_Q4_2010"] = pct(HK["2009-Q1"], HK["2010-Q4"])
R["d_hk_acwi_bought_Jan2007_meet_Jan2010"] = pct(ACWI["2006-12"], ACWI["2009-12"])
R["d_hk_bwtpi_Q1_2010_Q4_2011"] = pct(HK["2010-Q1"], HK["2011-Q4"])
R["d_hk_acwi_bought_Jan2008_meet_Jan2011"] = pct(ACWI["2007-12"], ACWI["2010-12"])
R["d_hk_bwtpi_Q1_2011_Q4_2012"] = pct(HK["2011-Q1"], HK["2012-Q4"])
R["d_hk_bwtpi_peak_Q3_2008_low_Q2_2009"] = pct(HK["2008-Q3"], HK["2009-Q2"])
R["d_hk_bwtpi_low_Q2_2009_to_Q4_2011"] = pct(HK["2009-Q2"], HK["2011-Q4"])
R["d_hk_bwtpi_Q1_2003_Q4_2004"] = pct(HK["2003-Q1"], HK["2004-Q4"])
# 1973-75: the burst came with the slump, not after it
R["d_us_shares_Jan1973_Dec1974"] = pct(US_SHARES["1973-01"], US_SHARES["1974-12"])
R["d_us_shares_Jan1972_Jan1975"] = pct(US_SHARES["1972-01"], US_SHARES["1975-01"])
R["d_us_materials_Jan1973_Dec1974"] = pct(PPI_MAT["1973-01"], PPI_MAT["1974-12"])
R["d_us_cpi_Jan1973_Dec1974"] = pct(CPI["1973-01"], CPI["1974-12"])
R["d_us_materials_Jan1975_Dec1976"] = pct(PPI_MAT["1975-01"], PPI_MAT["1976-12"])
R["d_us_cpi_Jan1975_Dec1976"] = pct(CPI["1975-01"], CPI["1976-12"])
R["d_us_shares_Jan1973_Jan1976"] = pct(US_SHARES["1973-01"], US_SHARES["1976-01"])
R["d_us_materials_Jan1976_Dec1977"] = pct(PPI_MAT["1976-01"], PPI_MAT["1977-12"])
R["d_us_cpi_Jan1976_Dec1977"] = pct(CPI["1976-01"], CPI["1977-12"])
R["d_hk_bwtpi_Q4_1972_Q2_1974"] = pct(HK["1972-Q4"], HK["1974-Q2"])
R["d_hk_bwtpi_Q2_1974_Q3_1975"] = pct(HK["1974-Q2"], HK["1975-Q3"])
R["d_hk_bwtpi_Q1_1975_Q4_1976"] = pct(HK["1975-Q1"], HK["1976-Q4"])
# 2000-03 then 2003-04 in the US: materials only (not a selling-price index), the same world steel burst
R["d_us_shares_Jan2000_Jan2003"] = pct(US_SHARES["2000-01"], US_SHARES["2003-01"])
R["d_us_materials_Jan2003_Dec2004"] = pct(PPI_MAT["2003-01"], PPI_MAT["2004-12"])
R["d_us_cpi_Jan2003_Dec2004"] = pct(CPI["2003-01"], CPI["2004-12"])
R["d_us_materials_Jan2009_Dec2010"] = pct(PPI_MAT["2009-01"], PPI_MAT["2010-12"])

if __name__ == "__main__":
    def fmt(v):
        if isinstance(v, float):
            return round(v * 100, 2) if abs(v) < 5 else round(v, 2)
        if isinstance(v, dict):
            return {k: fmt(x) for k, x in v.items()}
        if isinstance(v, list):
            return [fmt(x) for x in v]
        if isinstance(v, tuple):
            return tuple(fmt(x) for x in v)
        return v
    for k, v in R.items():
        print(k, fmt(v))
    print("(percent unless a dollar figure or a count; dollar figures: b_need_on_top_usd, b_left_*)")
