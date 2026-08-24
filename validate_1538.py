import re, io, json, sys
from html.parser import HTMLParser

D = "/sessions/vibrant-festive-ramanujan/mnt/outputs/"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
fails = []; checks = [0]

def ck(cond, msg):
    checks[0] += 1
    if not cond:
        fails.append(msg)

H = {p: io.open(D + p, encoding="utf-8").read() for p in PAGES}

# ---- 1. HTML balance ----
class B(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.stray=0
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
        else: s.stray+=1

for p in PAGES:
    b=B(); b.feed(H[p])
    ck(len(b.st)==0 and b.stray==0, "%s unbalanced: %d unclosed %s / %d stray" % (p,len(b.st),b.st[:6],b.stray))

# ---- 2. five-tab nav, exactly one active ----
for p in PAGES:
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', H[p], re.S)
    ck(nav is not None, "%s no nav.tabs" % p)
    if nav:
        n = nav.group(1)
        for href in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
            ck(href in n, "%s nav missing %s" % (p, href))
        ck(len(re.findall(r'class="[^"]*\bon\b[^"]*"', n))==1,
           "%s nav active-tab count != 1" % p)

# ---- 3. stamp ids ----
for p in PAGES:
    for i in ["datestamp","updated","edition","freshline"]:
        ck(('id="%s"' % i) in H[p], "%s missing id=%s" % (p,i))

# ---- 4. tldr rules ----
LABELS = {"cyber-briefing.html":"The Wire","wallstreet-briefing.html":"The Tape","mma-briefing.html":"Tale of the Tape"}
for p,lab in LABELS.items():
    m = re.findall(r'<div class="tldr"><b>([^<]+)</b>\s*<span>(.*?)</span></div>', H[p], re.S)
    ck(len(m)==1, "%s tldr count %d != 1" % (p,len(m)))
    if m:
        ck(m[0][0].strip()==lab, "%s tldr label %r != %r" % (p,m[0][0],lab))
        ck(m[0][1] in H["index.html"], "index.html missing verbatim tldr text of %s" % p)
ck('class="tldr"' not in H["index.html"], "index.html must not carry a .tldr")

# ---- 5. TradingView widget JSON ----
blocks = re.findall(r'embed-widget-[a-z\-]+\.js"\s+async>(\{.*?\})</script>', H["wallstreet-briefing.html"], re.S)
ck(len(blocks)==8, "TradingView block count %d != 8" % len(blocks))
for i,b in enumerate(blocks):
    try: json.loads(b)
    except Exception as e: fails.append("TV block %d bad JSON: %s" % (i,e)); checks[0]+=1
    else: checks[0]+=1

tape = re.search(r'embed-widget-ticker-tape\.js"\s+async>(\{.*?\})</script>', H["wallstreet-briefing.html"], re.S).group(1)
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(sym in tape, "ticker tape missing %s" % sym)

# Chart of the Day scoped to mini-symbol-overview ONLY (gotcha #4)
mini = re.search(r'embed-widget-mini-symbol-overview\.js"\s+async>(\{.*?\})</script>', H["wallstreet-briefing.html"], re.S).group(1)
ck('"symbol":"NASDAQ:AAOI"' in mini, "Chart of the Day symbol != NASDAQ:AAOI")
ck("SNDK" not in mini, "SNDK must not be the Chart-of-the-Day symbol")

# ---- 6. KEV countdowns ----
cds = re.findall(r'<span class="kevdue[^"]*">(.*?)</span>', H["cyber-briefing.html"])
ck(len(cds)==12, "KEV countdown count %d != 12" % len(cds))
past = [c for c in cds if "PAST DUE" in c]
today = [c for c in cds if "DUE TODAY" in c]
ahead = [c for c in cds if "PAST DUE" not in c and "DUE TODAY" not in c and "left" in c]
ck(len(past)==8, "KEV past-due count != 8 (got %d)" % len(past))
ck(len(today)==1, "KEV due-today count != 1 (got %d)" % len(today))
ck(len(ahead)==3, "KEV ahead count != 3 (got %d)" % len(ahead))
ck("DUE TODAY" in H["cyber-briefing.html"] and "CVE-2026-73570" in H["cyber-briefing.html"],
   "Zimbra due-today entry missing")

# ---- 7. champions board: CHAMPION COLUMN ONLY ----
tbl = re.search(r'Champions board.*?</table>', H["mma-briefing.html"], re.S)
ck(tbl is not None, "champions table not found")
if tbl:
    rows = re.findall(r'<tr><td>[^<]*</td><td>(.*?)</td>', tbl.group(0))
    ck(len(rows)==11, "champions rows %d != 11" % len(rows))
    col = " | ".join(rows)
    for name in ["Aspinall","Ulberg","Strickland","Makhachev","Gaethje","Volkanovski","Yan","Van"]:
        ck(name in col, "champions column missing %s" % name)
    for bad in ["Pereira","Chimaev","Topuria","Vacant","vacant"]:
        ck(bad not in col, "champions column contains STALE %s" % bad)

# ---- 8. Friday closes / cached figures confined out of the LEAD block ----
lead = re.search(r'<div class="lab">The lead</div>(.*?)</section>', H["wallstreet-briefing.html"], re.S).group(1)
for bad in ["7,674.37","53,277.01","26,180.46","7,659.82","53,392.55","26,067.27","79,032.63","+517.80","33.21"]:
    ck(bad not in lead, "LEAD block contains blacklisted/Friday figure %s" % bad)
ck("7,674.37" in H["wallstreet-briefing.html"], "Friday S&P close must still appear in the Weekly Scorecard")
# gotcha #6: anchor the hour
ck(re.search(r'(?<!1)2:59', H["wallstreet-briefing.html"]) is None, "wrong 2:59 stamp present (must be 12:59)")

# ---- 9. New-tag counts: WS 1 / CY 1 / MMA 0 ----
counts = {"wallstreet-briefing.html":1, "cyber-briefing.html":1, "mma-briefing.html":0}
for p,n in counts.items():
    got = H[p].count('class="tag new"')
    ck(got==n, "%s New-tag count %d != %d" % (p,got,n))

# footnote must name the ACTUAL tagged card (1413 lesson)
ck("shadow-fleet targets of the Iran sanctions package" in H["wallstreet-briefing.html"],
   "WS movers footnote does not name the actually-tagged card")
ck("risk gauges waking up, has been dropped" in H["wallstreet-briefing.html"],
   "WS footnote does not record the dropped tag")
ck("Exactly one item on this page carries a New tag" in H["cyber-briefing.html"],
   "CY footnote does not record the single New tag")

# ---- 10. after-hours SECTION LABEL absent (gotcha #5) ----
ck(re.search(r'class="lab"[^>]*>\s*After-Hours', H["wallstreet-briefing.html"]) is None,
   "After-Hours section label present during a regular session")

# ---- 11. freshness / stale-source assertions ----
FRESH_WS = ["3:38 p.m. ET","fifth consecutive run","seventh time today","twelfth consecutive run",
            "Mohsen Rezaei","seismic manner","shadow fleet vessels","2 million to the dollar",
            "Ant&oacute;nio Guterres","Alan Eyre","Monster Beverage up 2.3%","SanDisk down 10%",
            "U.S. markets open in 5h 6m"]
for s in FRESH_WS:
    ck(s in H["wallstreet-briefing.html"], "WS missing fresh string: %s" % s)
STALE_WS = ["Under an hour from the close","As of roughly 3:05 p.m. ET","sixth cached page",
            "eleventh consecutive run","fourth consecutive run"]
for s in STALE_WS:
    ck(s not in H["wallstreet-briefing.html"], "WS still carries STALE string: %s" % s)

FRESH_CY = ["WordlistLoader","SynkLoader","Amatera","EtherHiding","PhishLocker","StreamMaster",
            "Marcus Hutchins","Vojt&#283;ch Krejsa","seven modules",
            "ends a run of four consecutive cyber editions with zero New tags"]
for s in FRESH_CY:
    ck(s in H["cyber-briefing.html"], "CY missing fresh string: %s" % s)
ck("That makes two consecutive cyber editions with zero New tags" not in H["cyber-briefing.html"],
   "CY still carries the stale zero-New-tag footnote")
# THN mis-stated the Expel detection year (2025); it must not be published
ck("mid-August 2025" not in H["cyber-briefing.html"], "CY published the unreliable mid-August 2025 date")

# ---- 12. trap greps ----
TRAPS = ["Cody Salkilld","Abdul-Rakhman","Shamil Yakhyaev","title challenger Beneil","Shanghai Indoor Stadium"]
for p in PAGES:
    for t in TRAPS:
        ck(t not in H[p], "%s TRAP string present: %s" % (p,t))

# ---- 13. no leftover edit scaffolding ----
for p in PAGES:
    ck("<!--OLD" not in H[p], "%s contains leftover <!--OLD scaffolding" % p)

# ---- 14. MMA countdown target unchanged & Zimbra deadline consistent ----
ck("2026-08-29T06:00:00-04:00" in H["mma-briefing.html"], "MMA countdown target missing/changed")
ck("Shanghai Oriental Sports Center" in H["mma-briefing.html"] or "Oriental Sports Center" in H["mma-briefing.html"],
   "MMA venue string missing")
ck(H["cyber-briefing.html"].count("CVE-2026-73570")>=3, "Zimbra CVE not consistently referenced")
ck("10.1.20" in H["cyber-briefing.html"], "Zimbra fixed version missing")

print("checks run: %d" % checks[0])
if fails:
    print("FAILURES: %d" % len(fails))
    for f in fails: print("  - " + f)
    sys.exit(1)
print("ALL CHECKS PASSED")
