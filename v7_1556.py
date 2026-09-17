# -*- coding: utf-8 -*-
import datetime, re, os, sys
OUT = "/sessions/eager-bold-galileo/mnt/outputs"
P = {k: open(os.path.join(OUT, f)).read() for k, f in
     [("ix","index.html"),("cy","cyber-briefing.html"),("ws","wallstreet-briefing.html"),("mm","mma-briefing.html")]}
n = 0; fails = []
def ck(cond, msg):
    global n; n += 1
    if not cond: fails.append(msg)

TODAY = datetime.date(2026,9,17)

# ---- market arithmetic COMPUTED, never trusted
for base, chg, lvl, pct in [(7551.81, 87.21, "7,639.02", "1.15"),
                            (51461.90, 355.36, "51,817.26", "0.69"),
                            (28945.06, 480.96, "29,426.02", "1.66")]:
    tot = round(base + chg, 2)
    ck(f"{tot:,.2f}" == lvl, f"level mismatch {tot} vs {lvl}")
    ck(f"{chg/base*100:.2f}" == pct, f"pct mismatch {chg/base*100:.4f} vs {pct}")
    ck(lvl in P["ws"], f"{lvl} absent from ws")
    ck(pct+"%" in P["ws"], f"{pct}% absent from ws")
# movers reconcile
for last, chg, pct in [(977.36,50.81,"5.48"),(955.80,17.82,"1.90"),(348.66,9.15,"2.70"),(219.66,5.76,"2.69")]:
    prev = round(last-chg,2)
    ck(f"{chg/prev*100:.2f}" == pct, f"mover pct {chg/prev*100:.4f} vs {pct}")
ck("7,551.81" in P["ws"] and "51,461.90" in P["ws"] and "28,945.06" in P["ws"], "scorecard settles absent")

# ---- KEV countdowns COMPUTED
ck((datetime.date(2026,9,17)-TODAY).days == 0, "76461 not 0 days")
ck((datetime.date(2026,9,19)-TODAY).days == 2, "19 Sep not 2 days")
ck((TODAY-datetime.date(2026,9,14)).days == 3, "ScreenConnect not overdue 3")
ck((TODAY-datetime.date(2026,8,21)).days == 27, "vCenter not overdue 27")
ck(datetime.date(2026,9,19).strftime("%A") == "Saturday", "19 Sep not Saturday")
ck("Saturday" in P["cy"], "computed weekday absent")
ck("0 days left, today" in P["cy"], "0-day phrasing absent")
ck("2 days left" in P["cy"], "2-day phrasing absent")
ck("overdue by 3 days" in P["cy"], "overdue 3 absent")
ck("overdue by 27 days" in P["cy"], "overdue 27 absent")
# Patch Priority CVE == KEV-today CVE
ck(P["cy"].count("CVE-2026-76461") >= 3, "76461 not in all three cyber places")
ck("BOD 22-01" not in P["cy"], "BOD 22-01 present")
ck("three weeks" not in P["cy"], "'three weeks' present")

# ---- champions board: per-division parse
board = re.findall(r"<tr><td><b>(.*?)</b></td><td>(.*?)</td>", P["mm"])
ck(len(board) == 12, f"expected 12 champion rows, got {len(board)}")
vac = [d for d,c in board if "Vacant" in c]
ck(len(vac) == 2, f"expected exactly 2 vacant, got {len(vac)}: {vac}")
ck(any(d=="Heavyweight" and "Vacant" in c for d,c in board), "HW not vacant")
ck(any("Flyweight" in d and "Vacant" in c for d,c in board), "W-FLW not vacant")
champ_cells = " | ".join(c for d,c in board)
for banned in ["Pereira","Chimaev","Shevchenko","Aspinall","Topuria","Ankalaev","Pantoja","Procházka","Prochazka"]:
    ck(banned not in champ_cells, f"BANNED name {banned} in a champion cell")
ck(sum(1 for d,c in board if "Ulberg" in c) == 1, "Ulberg not exactly once")
ck(any(d=="Light Heavyweight" and "Ulberg" in c for d,c in board), "Ulberg not at LHW")
ck(any(d=="Heavyweight (interim)" and "Gane" in c for d,c in board), "Gane not interim HW")
for d,c in [("Middleweight","Strickland"),("Welterweight","Makhachev"),("Lightweight","Gaethje"),
            ("Featherweight","Volkanovski"),("Bantamweight","Yan"),("Flyweight","Van")]:
    ck(any(dd==d and c in cc for dd,cc in board), f"{c} not at {d}")

# ---- MMA dates: upcoming must be future, last event past
for ds in ["Sat 19 September 2026","Sat 3 October 2026","Sat 24 October 2026"]:
    ck(ds in P["mm"], f"{ds} absent")
ck(datetime.date(2026,9,19) > TODAY and datetime.date(2026,10,3) > TODAY and datetime.date(2026,10,24) > TODAY,
   "an upcoming card is not in the future")
ck("Noche UFC" in P["mm"], "Noche UFC absent")
ck("0:36" in P["mm"], "King III KO time 0:36 absent")
ck(P["mm"].count("0:33") == 1, "0:33 appears more than once")
ck(re.search(r"timing it at 0:33 is refused", P["mm"]) is not None, "0:33 not confined to refusal clause")
ck(re.search(r"headlines at <b>0:36</b>", P["mm"]) is not None, "0:36 not the asserted KO time")
ck("2026-09-19T21:00:00-04:00" in P["mm"], "countdown target absent")
ck("ufccdn" in P["mm"], "countdown element absent")

# ---- refusals present (named on page, not silently dropped)
ck("15.49" in P["ws"] and "Not published" in P["ws"], "VIX refusal not stated")
ck("7,596" in P["ws"], "superseded S&P snapshot not named")
ck("5.01%" in P["ws"], "10-yr 5.01% refusal not named")
ck("7635" in P["ws"], "TE meta inconsistency not named")
ck("Nasdaq Composite" in P["ws"], "Nasdaq Composite omission not stated")
ck("no usable content" in P["mm"], "ESPN empty-fetch not stated")
ck("Alex Pereira at light heavyweight" in P["mm"], "Pereira LHW refusal not named")
ck("heavyweight champion" in P["mm"], "Ulberg-at-HW refusal not named")
ck("New&rdquo; tag this edition" in P["ws"] or "New&rdquo; tag" in P["ws"], "markets zero New not stated")

# ---- structure, all four pages
GLYPH = {"cy":"⛨","ws":"▲","mm":"⊘","ix":"★","ar":"\U0001f5c4"}
for k, h in P.items():
    ck(h.count("<body>") == 1, f"{k}: body count")
    ck(h.count("<!DOCTYPE html>") == 1, f"{k}: doctype count")
    ck(h.count('<nav class="tabs">') == 1, f"{k}: nav count")
    ck(h.count('nav.tabs') >= 1, f"{k}: nav css")
    navblk = h.split('<nav class="tabs">')[1].split("</nav>")[0]
    ck(navblk.count("<a href=") == 5, f"{k}: nav links != 5")
    ck(navblk.count('class="active"') == 1, f"{k}: active tab != 1")
    for f in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        ck(f in navblk, f"{k}: nav missing {f}")
    ck("@@" not in h, f"{k}: unreplaced @@")
    ck(h.count("<footer>") == 1, f"{k}: footer count")
    ck('id="edition"' in h and 'id="datestamp"' in h and 'id="updated"' in h, f"{k}: masthead pills")
    ck('id="freshline"' in h, f"{k}: freshline")
    ck("briefings refresh every 30 minutes" in h, f"{k}: freshness text")
    ck("&#9924;" not in h and "⛄" not in h, f"{k}: snowman glyph present")
# nav glyphs at code-point level
for ent, cp in [("&#9960;","⛨"),("&#9650;","▲"),("&#8856;","⊘"),("&#9733;","★"),("&#128452;","\U0001f5c4")]:
    ck(all(ent in h for h in P.values()), f"nav glyph {cp!r} missing from a page")

# ---- TLDR strips: exactly on the three briefings, not index
for k in ["cy","ws","mm"]:
    ck(P[k].count('class="tldr"') == 1, f"{k}: tldr count")
ck('class="tldr"' not in P["ix"], "index carries a tldr")
ck("The Wire" in P["cy"] and "The Tape" in P["ws"] and "Tale of the Tape" in P["mm"], "tldr labels")

# ---- index cards must string-match each briefing's own TLDR verbatim
def tldr(h):
    return h.split('<div class="tldr">')[1].split("</span>")[0].split("<span>")[1]
for k in ["cy","ws","mm"]:
    t = tldr(P[k])
    ck(t in P["ix"], f"index card does not match {k} TLDR verbatim")
ck(P["ix"].count("Read the briefing &rarr;") == 3, "index: 3 read links")

# ---- TradingView blocks: all six on ws, none elsewhere
blocks = ["ticker-tape","single-quote","timeline","stock-heatmap","mini-symbol-overview","events"]
for b in blocks:
    ck(f"embed-widget-{b}.js" in P["ws"], f"ws missing block {b}")
    for k in ["ix","cy","mm"]:
        ck(f"embed-widget-{b}.js" not in P[k], f"{k} must not carry {b}")
ck(P["ws"].count("embed-widget-single-quote.js") == 3, "not exactly 3 single-quote widgets")
tt = P["ws"].split("embed-widget-ticker-tape.js")[1].split("</script>")[0]
for must in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(must in tt, f"ticker missing {must}")
ck('"symbol":"NASDAQ:MU"' in P["ws"], "Chart of the Day not set to MU")

# ---- disclaimers
ck("not investment advice" in P["ws"].lower(), "ws disclaimer")
ck("subject to change" in P["mm"], "mma disclaimer")
ck("vulnerability management" in P["cy"], "cyber disclaimer")

# ---- freshness honesty: no claim of an official Thursday close
ck("no official closing figures were verified" in P["ws"], "close caveat absent")
ck("3:50" in P["ws"], "as-of time absent from ws")

print(f"{n} checks, {len(fails)} failures")
for f in fails: print("  FAIL:", f)
sys.exit(1 if fails else 0)
