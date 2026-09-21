# -*- coding: utf-8 -*-
import io, re, datetime
B = "/sessions/youthful-bold-tesla/mnt/outputs/"
P = {k: io.open(B+f, encoding="utf-8").read() for k, f in
     [("index","index.html"),("cyber","cyber-briefing.html"),("ws","wallstreet-briefing.html"),("mma","mma-briefing.html")]}
FILES = {"index":"index.html","cyber":"cyber-briefing.html","ws":"wallstreet-briefing.html","mma":"mma-briefing.html"}
n=0; fails=[]
def ck(cond,msg):
    global n
    n+=1
    if not cond: fails.append(msg)

TODAY = datetime.date(2026,9,21)

# --- chrome on all four ---
for k,s in P.items():
    ck(s.startswith("<!doctype html>"), k+": doctype")
    for pid in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        ck(pid in s, "%s: missing %s" % (k,pid))
    ck('pill live' in s, k+": live pill")
    ck("Intl.DateTimeFormat" in s and "America/New_York" in s, k+": stamp js")
    ck("briefings refresh every 30 minutes" in s or "freshline" in s, k+": freshline text")
    # five-tab nav, exactly one active, and it is this page
    tabs = re.findall(r'<a href="([a-z\-\.]+\.html)"( class="active")?>', s)
    hrefs = [t[0] for t in tabs[:5]]
    ck(hrefs == ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"],
       k+": nav order/links %r" % (hrefs,))
    act = [t[0] for t in tabs[:5] if t[1]]
    ck(len(act)==1, k+": exactly one active tab")
    ck(act and act[0]==FILES[k], k+": active tab is self")
    # every class used appears in that page's own stylesheet
    css = s[s.find("<style>"):s.find("</style>")]
    used=set()
    for m in re.finditer(r'class="([^"]+)"', s):
        for c in m.group(1).split():
            used.add(c)
    for c in sorted(used):
        ck(("."+c) in css, "%s: class .%s not in own stylesheet" % (k,c))

# --- tldr labels ---
ck('<div class="tldr"><b>The Wire</b>' in P["cyber"], "cyber tldr label")
ck('<div class="tldr"><b>The Tape</b>' in P["ws"], "ws tldr label")
ck('<div class="tldr"><b>Tale of the Tape</b>' in P["mma"], "mma tldr label")
ck('class="tldr"' not in P["index"], "index must not have a tldr strip")

# --- index cards byte-identical to each page's tldr, exactly once ---
for key in ("cyber","ws","mma"):
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', P[key], re.S)
    ck(m is not None, key+": tldr parse")
    t = m.group(1)
    ck(P["index"].count(t)==1, "index: card text for %s not present exactly once" % key)

# --- live widgets: six blocks on ws only ---
W = P["ws"]
for blk in ["embed-widget-ticker-tape.js","embed-widget-single-quote.js","embed-widget-timeline.js",
            "embed-widget-stock-heatmap.js","embed-widget-mini-symbol-overview.js","embed-widget-events.js"]:
    ck(blk in W, "ws: missing widget "+blk)
ck(W.count("embed-widget-single-quote.js")==3, "ws: exactly three single-quote widgets")
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(sym in W, "ws: ticker missing "+sym)
for k in ("index","cyber","mma"):
    ck("tradingview.com" not in P[k], k+": must carry no tradingview reference")

# --- section ordering by heading markup ---
def heads(s): return re.findall(r'<h2 class="sec">(.*?)</h2>', s)
hw = heads(W)
want_ws = ["Live Index Quotes","The Lead","Movers","Chart of the Day","Sector Heat","The Calendar",
           "Live Market Headlines","Weekly Scorecard","Rates, Bonds","On the Radar","Sources"]
ck(len(hw)==len(want_ws), "ws: heading count %d" % len(hw))
for i,w in enumerate(want_ws):
    ck(i<len(hw) and hw[i].startswith(w), "ws: heading %d is %r, expected %r" % (i, hw[i] if i<len(hw) else None, w))
hc = heads(P["cyber"])
want_cy = ["Top Story","Patch Priority","Threat Actor Spotlight","Breaches","Vulnerability Watch",
           "CISA KEV","Sources"]
ck(len(hc)==len(want_cy), "cyber: heading count %d" % len(hc))
for i,w in enumerate(want_cy):
    ck(i<len(hc) and hc[i].startswith(w), "cyber: heading %d is %r" % (i, hc[i] if i<len(hc) else None))
hm = heads(P["mma"])
want_mma = ["Top Story","Fight Week","Last Event","Prospect Watch","Around the Sport","Rankings","Champions Board","Sources"]
ck(len(hm)==len(want_mma), "mma: heading count %d" % len(hm))
for i,w in enumerate(want_mma):
    ck(i<len(hm) and hm[i].startswith(w), "mma: heading %d is %r" % (i, hm[i] if i<len(hm) else None))

# --- cyber: vuln table row count + every CVE id present ---
CVES = ["CVE-2025-39682","CVE-2026-53266","CVE-2025-39964","CVE-2026-76460","CVE-2026-76461",
        "CVE-2026-94097","CVE-2026-55366","CVE-2026-86462","CVE-2026-58704"]
for c in CVES: ck(c in P["cyber"], "cyber: missing "+c)
tbl = re.search(r'Vulnerability Watch</h2>(.*?)</table>', P["cyber"], re.S).group(1)
ck(tbl.count("<tr>")==len(CVES)+1, "cyber: vuln table rows = %d (want %d)" % (tbl.count("<tr>"), len(CVES)+1))

# --- cyber: KEV countdowns recomputed from today ---
DUE = {"CVE-2025-39682":datetime.date(2026,9,21),"CVE-2026-53266":datetime.date(2026,9,21),
       "CVE-2025-39964":datetime.date(2026,9,21),"CVE-2026-76460":datetime.date(2026,9,19),
       "CVE-2026-76461":datetime.date(2026,9,17)}
for cve,d in DUE.items():
    delta = (d-TODAY).days
    if delta==0: ck("today" in P["cyber"], "cyber: %s due today wording" % cve)
    elif delta<0:
        ck(("%d days overdue" % (-delta)) in P["cyber"], "cyber: %s should read %d days overdue" % (cve,-delta))
# patch box: 21 September and no other due date
box = re.search(r'Patch Priority</h2>(.*?)</div>', P["cyber"], re.S).group(1)
ck("21 September" in box, "cyber: patch box must name 21 September")
for bad in ["17 September","19 September","20 September","22 September"]:
    ck(("due "+bad) not in box, "cyber: patch box names another due date "+bad)

# --- mma: results table 6 rows, champions 11 rows, division<->name equality ---
rt = re.search(r'Last Event(.*?)</table>', P["mma"], re.S).group(1)
ck(rt.count("<tr>")==7, "mma: results table rows = %d" % rt.count("<tr>"))
ct = re.search(r'Champions Board</h2>(.*?)</table>', P["mma"], re.S).group(1)
ck(ct.count("<tr>")==12, "mma: champions rows = %d" % ct.count("<tr>"))
PAIRS = [("Heavyweight","Ciryl Gane"),("Light Heavyweight","Carlos Ulberg"),("Middleweight","Sean Strickland"),
         ("Welterweight","Islam Makhachev"),("Lightweight","Justin Gaethje"),("Featherweight","Alexander Volkanovski"),
         ("Bantamweight","Petr Yan"),("Flyweight","Joshua Van"),
         ("Women&rsquo;s Bantamweight","Kayla Harrison"),("Women&rsquo;s Flyweight","VACANT"),
         ("Women&rsquo;s Strawweight","Mackenzie Dern")]
rows = re.findall(r'<tr><td>([^<]+)</td><td[^>]*><b>([^<]+)</b></td>', ct)
ck(len(rows)==11, "mma: parsed champion rows = %d" % len(rows))
for (d,c) in PAIRS:
    ck((d,c) in rows, "mma: champions row mismatch %s -> %s" % (d,c))
ck(sum(1 for r in rows if r[1]=="VACANT")==1, "mma: exactly one VACANT")
BANNED = ["Alex Pereira","Khamzat Chimaev","Tom Aspinall","Valentina Shevchenko","Ilia Topuria",
          "Merab Dvalishvili","Alexandre Pantoja","Jack Della Maddalena","Amanda Nunes",
          "Diego Lopes","Jiri Prochazka","Sean O'Malley"]
champ_cells = [r[1] for r in rows]
for bnd in BANNED:
    ck(bnd not in champ_cells, "mma: banned stale champion name in champion cell: "+bnd)

# --- mma: upcoming card dates are in the future ---
for d in [(2026,9,26),(2026,10,3),(2026,10,24),(2026,11,14)]:
    ck(datetime.date(*d) > TODAY, "mma: card date not in the future %r" % (d,))
ck("26 September" in P["mma"] and "3 October" in P["mma"] and "24 October" in P["mma"] and "14 November" in P["mma"],
   "mma: card dates present")
ck('id="ufccdn"' in P["mma"] and "2026-09-26T20:00:00-04:00" in P["mma"], "mma: countdown target")
# refused odds numerals absent
for bad in ["1011","+133"]:
    ck(bad not in P["mma"], "mma: refused odds numeral present: "+bad)
ck("&minus;210" in P["mma"] and "+177" in P["mma"], "mma: published opening line missing")

# --- ws: index levels appear exactly once and only inside the Weekly Scorecard ---
sc = re.search(r'Weekly Scorecard(.*?)</table>', W, re.S).group(1)
for lvl in ["7,650.50","26,522.55","51,682.64"]:
    ck(W.count(lvl)==1, "ws: level %s appears %d times" % (lvl, W.count(lvl)))
    ck(lvl in sc, "ws: level %s not inside scorecard" % lvl)
ck(W.count('class="card"')==7, "ws: mover cards = %d" % W.count('class="card"'))
ck("NASDAQ:WBD" in W, "ws: chart of the day symbol")

# --- no empty tag classes anywhere ---
for k,s in P.items():
    ck('class="tag "' not in s and 'class="tag"' in s or k=="index", k+": tag sanity")

print("checks:", n, "failures:", len(fails))
for f in fails: print("  FAIL:", f)
