# -*- coding: utf-8 -*-
import re, os, datetime, sys
D="/tmp/build_1788656196/out"
PREV="/tmp/db_1788643981/archive"
F={k:open(os.path.join(D,f),encoding="utf-8").read() for k,f in
   [("ix","index.html"),("cy","cyber-briefing.html"),("ws","wallstreet-briefing.html"),("mm","mma-briefing.html")]}
fails=[]; n=0
def ck(cond,msg):
    global n; n+=1
    if not cond: fails.append(msg)

# structure
for k,t in F.items():
    ck(len(t)>8000, f"{k}: too short")
    for href in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        ck(f'href="{href}"' in t, f"{k}: missing nav link {href}")
    for pid in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        ck(pid in t, f"{k}: missing {pid}")
    ck('Intl.DateTimeFormat' in t, f"{k}: missing stamp JS")
    ck('class="pill live"' in t, f"{k}: missing LIVE pill")
    ck(not re.search(r'&[A-Za-z]+>', t), f"{k}: malformed entity")
    ck(t.count('<a class="active"')==0, f"{k}: bad active markup")
ck(F["ix"].count('nav.tabs a.active')>=0,"noop")
for k,act in [("ix","index.html"),("cy","cyber-briefing.html"),("ws","wallstreet-briefing.html"),("mm","mma-briefing.html")]:
    ck(f'<a href="{act}" class="active">' in F[k], f"{k}: active tab not self")

# tldr
for k in ("cy","ws","mm"): ck(F[k].count('class="tldr"')==1, f"{k}: tldr count != 1")
ck(F["ix"].count('class="tldr"')==0, "ix: has tldr")
ck('>The Tape<' in F["ws"], "ws: label"); ck('>The Wire<' in F["cy"], "cy: label")
ck('>Tale of the Tape<' in F["mm"], "mm: label")

# index cards verbatim on target pages
CY=("A maximum-severity SonicWall SMA 1000 flaw is confirmed exploited in the wild and can be "
    "chained to remote code execution, while a Chromium V8 zero-day carries a September 18 federal "
    "patch deadline — and Unit 42 has published the anatomy of an AI-directed intrusion that took "
    "root in under ten hours.")
WS=("U.S. markets are closed for the Labor Day long weekend after a hot August jobs report "
    "knocked the three major indexes lower on Friday and pushed bets on a September Fed rate "
    "hike back toward a coin flip; the next session opens Tuesday, September 8.")
MM=("Salahdine Parnasse stopped Dan Hooker in the first round of his UFC debut in Paris, took "
    "Performance of the Night and called for Max Holloway — and UFC.com says the win puts him "
    "straight into the lightweight top 15.")
for txt,k in ((CY,"cy"),(WS,"ws"),(MM,"mm")):
    ck(txt in F["ix"], f"ix: card text missing ({k})")
    ck(txt in F[k], f"{k}: index card text not verbatim on page")

# WS live blocks A-F
for name,needle in [("A","embed-widget-ticker-tape.js"),("B","embed-widget-single-quote.js"),
                    ("C","embed-widget-timeline.js"),("D","embed-widget-stock-heatmap.js"),
                    ("E","embed-widget-mini-symbol-overview.js"),("F","embed-widget-events.js")]:
    ck(needle in F["ws"], f"ws: missing block {name}")
ck(F["ws"].count("embed-widget-single-quote.js")==3, "ws: need 3 single quotes")
for s in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(s in F["ws"], f"ws: ticker missing {s}")
ck('class="livebar"' in F["ws"], "ws: livebar")
ck("Quotes stream live" in F["ws"], "ws: note line")
ck(re.search(r'VIX\s*[:\-]?\s*\d', F["ws"]) is None, "ws: published a VIX level")
ck("No after-hours session this edition" in F["ws"], "ws: after-hours panel")
ck("53,414.25" in F["ws"] and "7,718.60" in F["ws"] and "26,506.99" in F["ws"], "ws: Friday closes")
ck("53,686.11" in F["ws"], "ws: Thursday row")
ck("162,000" in F["ws"], "ws: payrolls")

# cyber
ck('callout crit' in F["cy"], "cy: patch priority not crit")
REF="CISA’s own alert page returned empty on fetch for a third consecutive run"
ck(REF in F["cy"], "cy: patch-priority refusal string")
ck("CISA’s own page returned empty" in F["cy"], "cy: KEV refusal string")
ck("September 18" in F["cy"], "cy: chrome due date")
left=(datetime.date(2026,9,18)-datetime.date(2026,9,5)).days
ck(f"({left} days left)" in F["cy"], "cy: countdown")
ck("CVE-2026-83548" in F["cy"] and "10.0" in F["cy"], "cy: sonicwall")
ck("intrusion, and not a ransomware attack" in F["cy"], "cy: unit42 correction")
ck("152.0.7977.82" in F["cy"], "cy: chrome fixed version")

# mma champions
mrow=re.search(r'<h2 class="sec">Champions Board</h2>.*?</table>', F["mm"], re.S).group(0)
ck(mrow.count("<tr>")==13, f"mm: champions rows = {mrow.count('<tr>')} (want 13 incl header)")
ck("Carlos Ulberg" in mrow and "Sean Strickland" in mrow, "mm: LHW/MW champs")
ck("Alexander Volkanovski" in mrow, "mm: FW champ")
ck("Justin Gaethje" in mrow, "mm: LW champ")
ck(not re.search(r'Light Heavyweight</td><td><strong>Alex Pereira', mrow), "mm: Pereira LHW regression")
ck(not re.search(r'Middleweight</td><td><strong>Khamzat', mrow), "mm: Chimaev MW regression")
ck(re.search(r"Featherweight</td><td><strong>\s*[Vv]acant", mrow) is None, "mm: featherweight listed vacant")
ck("<strong>Not vacant.</strong>" in mrow, "mm: featherweight not-vacant note missing")
ck("Contender Series" not in F["mm"].split("Dana White’s Contender Series, Season 10")[0].split("Top Story")[1][:2500] or "did not come through Dana White’s Contender Series" in F["mm"], "mm: Parnasse DWCS attribution")
ck("did not come through Dana White’s Contender Series" in F["mm"], "mm: Parnasse DWCS denial missing")
ck("Salahdine Parnasse" in F["mm"] and "Saladhine" not in F["mm"], "mm: Parnasse spelling")
ck("Quillan" not in F["mm"] or "Cody Salkilld" not in F["mm"], "mm: Salkilld name")
res=re.search(r'<h2 class="sec">Last Event — Results</h2>.*?</table>', F["mm"], re.S).group(0)
ck(res.count("<tr>")==15, f"mm: result rows = {res.count('<tr>')} (want 15 incl header)")
ck("TKO, R1 2:35" in F["mm"], "mm: main event method")
ck("Performance of the Night" in F["mm"], "mm: bonuses")
ck("$4,365,335" in F["mm"] and "15,687" in F["mm"], "mm: gate/attendance")
ck("ufccdn" in F["mm"] and "2026-09-12T00:00:00-04:00" in F["mm"], "mm: countdown")
# loser-name consistency: Wood must not be described as hunting a win in prospect card
pw=re.search(r'<h2 class="sec">Prospect Watch</h2>.*?<h2 class="sec">', F["mm"], re.S).group(0)
ck("beat</strong> Nathaniel" in pw or "<strong>beat</strong> Nathaniel Wood" in pw, "mm: Andrusca card contradicts table")

# weekday calendar guard
CAL=[("Saturday",datetime.date(2026,9,5)),("Friday",datetime.date(2026,9,4)),
     ("Thursday",datetime.date(2026,9,3)),("Monday",datetime.date(2026,9,7)),
     ("Tuesday",datetime.date(2026,9,8)),("Thursday",datetime.date(2026,9,10)),
     ("Friday",datetime.date(2026,9,11)),("Friday",datetime.date(2026,9,18)),
     ("Saturday",datetime.date(2026,9,12)),("Saturday",datetime.date(2026,9,19)),
     ("Saturday",datetime.date(2026,9,26)),("Saturday",datetime.date(2026,10,17)),
     ("Wednesday",datetime.date(2026,9,16))]
for wd,d in CAL:
    ck(d.strftime("%A")==wd, f"calendar: {d} is {d.strftime('%A')}, page says {wd}")

# "New" tags vs prior snapshot
import glob
def prev(sec):
    g=sorted(glob.glob(os.path.join(PREV,f"{sec}-2026-09-05-*.html")))
    return open(g[-1],encoding="utf-8").read() if g else ""
NEW={"cy":["McKesson confirms a breach"],
     "ws":["Memory and the semis/AI trade led","Tankers and shipping kept surging","FOMC: September 15–16"],
     "mm":["Gross total revenue","Salahdine Parnasse — debut","Axel Sola — back-to-back finishes"]}
secmap={"cy":"cyber","ws":"wallstreet","mm":"mma"}
for k,items in NEW.items():
    p=prev(secmap[k])
    for it in items:
        ck(it in F[k], f"{k}: New item text missing: {it}")
        if p: ck(it not in p, f"{k}: tagged New but present in prior snapshot: {it}")

print(f"CHECKS: {n}   FAILURES: {len(fails)}")
for f_ in fails: print("  FAIL:", f_)
sys.exit(1 if fails else 0)
