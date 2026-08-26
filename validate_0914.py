#!/usr/bin/env python3
"""Programmatic validation for the 2026-08-26 ~9:14am ET Morning Edition."""
import sys, io, re, json, datetime
from html.parser import HTMLParser

D = sys.argv[1].rstrip('/')
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {p: io.open(f"{D}/{p}", encoding="utf-8").read() for p in PAGES}
TODAY = datetime.date(2026, 8, 26)
fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

# ---------- 1. HTML balance ----------
VOID = {"br","img","hr","meta","link","input","source","col","area","base","embed","param","track","wbr"}
class B(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=False); s.st=[]; s.unc=[]; s.stray=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if t in s.st:
            while s.st and s.st.pop()!=t: pass
        else: s.stray.append(t)
for p in PAGES:
    b=B(); b.feed(S[p])
    ck(not b.stray, f"{p}: stray end tags {b.stray[:5]}")
    ck(len(b.st)<=0, f"{p}: {len(b.st)} tags left open {b.st[:5]}")

# ---------- 2. nav ----------
HREFS=["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]
for p in PAGES:
    nav=re.search(r'<nav class="tabs">(.*?)</nav>', S[p], re.S)
    ck(nav is not None, f"{p}: no <nav class=\"tabs\">")
    if nav:
        got=re.findall(r'href="([^"]+)"', nav.group(1))
        ck(got==HREFS, f"{p}: nav hrefs {got}")
        on=re.findall(r'<a[^>]*href="([^"]+)"[^>]*class="on"|<a[^>]*class="on"[^>]*href="([^"]+)"', nav.group(1))
        flat=[x or y for x,y in on]
        ck(len(flat)==1 and flat[0]==p, f"{p}: active tab {flat}")

# ---------- 3. stamp ids ----------
for p in PAGES:
    for i in ["datestamp","updated","edition","freshline"]:
        ck(S[p].count(f'id="{i}"')==1, f"{p}: id={i} count {S[p].count(chr(34)+i+chr(34))}")

# ---------- 4. tldr ----------
LAB={"cyber-briefing.html":"The Wire","wallstreet-briefing.html":"The Tape","mma-briefing.html":"Tale of the Tape"}
TL={}
for p,l in LAB.items():
    t=re.findall(r'<div class="tldr"><b>([^<]+)</b> <span>(.*?)</span></div>', S[p], re.S)
    ck(len(t)==1, f"{p}: {len(t)} tldr blocks")
    if t:
        ck(t[0][0]==l, f"{p}: tldr label {t[0][0]!r} != {l!r}")
        TL[p]=t[0][1]
ck('class="tldr"' not in S["index.html"], "index.html carries a .tldr (it must not)")

# ---------- 5. index cards mirror their page ----------
i=S["index.html"]
for slug,page in [("sec","cyber-briefing.html"),("mkt","wallstreet-briefing.html"),("mma","mma-briefing.html")]:
    mm=re.search(r'<a class="bcard c-'+slug+r'" href="([^"]+)">\s*<div class="kicker">([^<]*)</div>\s*<h2>(.*?)</h2>\s*<p>(.*?)</p>\s*<div class="go">(.*?)</div>', i, re.S)
    ck(mm is not None, f"index: bcard c-{slug} not parsed")
    if mm:
        ck(mm.group(1)==page, f"index c-{slug}: href {mm.group(1)}")
        ck(len(mm.group(3).strip())>20, f"index c-{slug}: empty h2")
        ck(mm.group(4)==TL.get(page), f"index c-{slug}: summary does not match the page tldr verbatim")
        ck("Read the briefing" in mm.group(5), f"index c-{slug}: missing CTA")

# ---------- 6. TradingView blocks ----------
tv=0
for p in PAGES:
    for blk in re.findall(r'embed-widget-[a-z-]+\.js" async>(\{.*?\})</script>', S[p], re.S):
        tv+=1
        try: json.loads(blk)
        except Exception as e: fails.append(f"{p}: TradingView JSON parse error {e}")
    checks+=1
ck(tv==8, f"TradingView blocks: {tv} (expected 8)")

# ---------- 7. tape symbols ----------
w=S["wallstreet-briefing.html"]
tape=re.search(r'embed-widget-ticker-tape\.js" async>(\{.*?\})</script>', w, re.S)
ck(tape is not None, "no ticker-tape block")
if tape:
    syms=[s["proName"] for s in json.loads(tape.group(1))["symbols"]]
    for req in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
        ck(req in syms, f"ticker tape missing required symbol {req}")

# ---------- 8. chart of the day ----------
mini=re.search(r'embed-widget-mini-symbol-overview\.js" async>(\{.*?\})</script>', w, re.S)
ck(mini and json.loads(mini.group(1))["symbol"]=="NASDAQ:NVDA", "Chart of the Day symbol != NASDAQ:NVDA")

# ---------- 9. KEV board ----------
c=S["cyber-briefing.html"]
kev=re.findall(r'<span class="kevdue (ok|crit)">([^<]+)</span>', c)
ck(len(kev)==14, f"KEV countdowns: {len(kev)} (expected 14)")
past=[t for k,t in kev if "past due" in t]
today=[t for k,t in kev if t.strip().lower() in ("due today","0 days left")]
ahead=sorted(int(re.match(r'(\d+)', t).group(1)) for k,t in kev if "left" in t)
ck(len(past)==10, f"KEV past due: {len(past)} (expected 10)")
ck(len(today)==0, f"KEV due today: {len(today)} (expected 0)")
ck(ahead==[1,2,7,8], f"KEV ahead: {ahead} (expected [1,2,7,8])")
for k,t in kev:
    ck((k=="crit")==("past due" in t or t.strip().lower()=="due today"), f"KEV colour/text mismatch: {k} / {t}")
ck("<b>14</b> entries" in c and "4 remain ahead of schedule" in c, "KEV summary note not reconciled to 14 / 4 ahead")
ck("<b>13</b> entries" not in c, "KEV summary still says 13 entries")

# ---------- 10. CVE rows unique ----------
rows=re.findall(r'<tr><td>(CVE-\d{4}-\d+)</td>', c)
ck(len(rows)==len(set(rows)), f"duplicate CVE rows: {[x for x in rows if rows.count(x)>1]}")
ck("CVE-2026-69836" in rows, "Entra ID CVE row missing from Vulnerability Watch")

# ---------- 11. champions ----------
m=S["mma-briefing.html"]
tbl=re.search(r'Champions board.*?<table>(.*?)</table>', m, re.S).group(1)
trs=re.findall(r'<tr>(.*?)</tr>', tbl, re.S)
ck(len(trs)==12, f"champions rows incl header: {len(trs)}")
champ=[re.findall(r'<td>(.*?)</td>', r, re.S)[1] for r in trs[1:]]
ck(len(champ)==11, f"champion cells: {len(champ)}")
GOOD=["Tom Aspinall","Carlos Ulberg","Sean Strickland","Islam Makhachev","Justin Gaethje",
      "Alexander Volkanovski","Petr Yan","Joshua Van","Valentina Shevchenko","Kayla Harrison","Mackenzie Dern"]
for g in GOOD: ck(any(g in x for x in champ), f"champion missing: {g}")
for bad in ["Pereira","Chimaev","Topuria","Pantoja","Dvalishvili","Della Maddalena","O'Malley","Nurmagomedov"]:
    ck(not any(bad in x for x in champ), f"STALE champion name in champion column: {bad}")
ck(not any("vacant" in x.lower() for x in champ), "a belt is listed vacant")

# ---------- 12. index reconciliation (Tuesday's closes vs Monday's) ----------
MON={"S&P":7652.86,"Dow":53417.16,"Nasdaq":25980.19}
TUE={"S&P":(7677.28,24.42,0.32),"Dow":(53577.40,160.24,0.30),"Nasdaq":(26151.30,171.11,0.66)}
for k,(lvl,pts,pct) in TUE.items():
    ck(round(MON[k]+pts,2)==lvl, f"{k}: {MON[k]}+{pts} != {lvl}")
    ck(round(pts/MON[k]*100,2)==pct, f"{k}: pct {round(pts/MON[k]*100,2)} != {pct}")
    ck(f"{lvl:,.2f}" in w, f"{k} close {lvl:,.2f} not on the page")

# ---------- 13. rejected Dow level ----------
ck(w.count("53,579.94")==1, f"53,579.94 appears {w.count('53,579.94')} times (expected 1)")
occ=w[w.find("53,579.94"):w.find("53,579.94")+120]
ck("NOT published" in occ, "53,579.94 occurrence is not inside its rejection sentence")

# ---------- 14. forward dates still in the future ----------
FWD=[(datetime.date(2026,8,27),"Oracle KEV deadline"),(datetime.date(2026,8,28),"Gitea KEV deadline"),
     (datetime.date(2026,8,29),"UFC Shanghai"),(datetime.date(2026,9,2),"MLflow KEV"),
     (datetime.date(2026,9,3),"TrueConf KEV"),(datetime.date(2026,9,12),"Noche UFC"),
     (datetime.date(2026,9,19),"UFC 331"),(datetime.date(2026,10,3),"UFC 332"),
     (datetime.date(2026,10,24),"UFC 333"),(datetime.date(2026,10,31),"Szabova debut")]
for d,l in FWD: ck(d>=TODAY, f"forward item already elapsed: {l} {d}")

# ---------- 15. MMA countdown target ----------
ck("2026-08-29T06:00:00-04:00" in m, "MMA countdown does not target Aug 29 06:00 EDT")
ck("2026-08-29T00:00:00-04:00" not in m, "MMA countdown still targets midnight")

# ---------- 16. content guards ----------
GUARD = {
 "wallstreet-briefing.html": ["rose 0.2% from a month ago","up 3.7% on an annual basis","polled by LSEG",
   "0.1% and 3.6%","3.3% higher than last year","8:35&nbsp;a.m. EDT","Eric Revell",
   "38% probability on a quarter-point rate hike","down from 55% one month ago","3.4% year-on-year peak",
   "65th consecutive month","Kevin Warsh","DBS Bank","0.75% lower on the month",
   "personal income up 0.4%","Nasdaq-100 futures down 0.4%","Form 8-K","ability to process and ship customer orders",
   "$91.0 billion","$92.2 billion","$91.85 billion","$46.74 billion","4.629%","4.183%","5.163%","315.30"],
 "cyber-briefing.html": ["CVE-2026-69836","Robert Fitzpatrick","not exploited in the wild",
   "Deserialization of untrusted data","greater transparency","August 25, 2026, Boston Scientific Corporation",
   "global disruption to the Company","ability to process and ship customer orders",
   "timeline for a full restoration is not yet known","third-party cybersecurity experts","Susan Thompson",
   "reasonably likely to have a material impact","CVE-2026-21962","CVE-2026-60004","CVE-2026-19478",
   "Mirage2FA","63.7%","4,500","BOD&nbsp;26-04","1.27.1","1.27.2"],
 "mma-briefing.html": ["Oriental Sports Center","Pudong District","6:00 a.m. EDT","Paramount+",
   "second consecutive year and the third time overall","20-1 MMA, 8-1 UFC","23-9-1 MMA, 12-4-1 UFC",
   "Mario Bautista","UFC&nbsp;321","UFC&nbsp;324","Sean O&rsquo;Malley","Yan Xiaonan","Denise Gomes",
   "Kai Asakura","Sumudaerji","Levi Rodrigues&nbsp;Jr.","Bilal Hasan","Nilson Rojas","12-fight undercard",
   "never lost in China","four-fight winning streak","first in line to face the winner of Yan-Dvalishvili 3",
   "&minus;470","&minus;700","&minus;500","two different fights","Curtis Blaydes","Lucia Szabova",
   "Gregory Rodrigues","Anthony Hernandez"],
}
for p,gs in GUARD.items():
    for g in gs: ck(g in S[p], f"{p}: MISSING content guard {g!r}")

# ---------- 17. trap greps ----------
TRAP=["Cody Salkilld","Abdul-Rakhman","Shamil Yakhyaev","title challenger Beneil","Shanghai Indoor Stadium",
      "Pereira retains","Featherweight vacant","markets closed higher today","@@T@@","UFC Fight Night 286",
      "core PCE came in at 3.6","no source fetched at 8:44","is not printing a number yet",
      "&minus;500 / +380","Figueiro"]
for p in PAGES:
    for t in TRAP: ck(t not in S[p], f"{p}: TRAP HIT {t!r}")

# ---------- 18. New-tag accounting ----------
for p in PAGES:
    ck("New &middot; 8:18" not in S[p] and "New &middot; 8:46" not in S[p], f"{p}: undemoted New tag")
counts={p:S[p].count('<span class="tag new">New</span>') for p in PAGES}
print("New tags:", counts)

print(f"\n{'='*60}\n{checks} checks, {len(fails)} failures")
for f in fails: print("  FAIL:", f)
sys.exit(1 if fails else 0)
