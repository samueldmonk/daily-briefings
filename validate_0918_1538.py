# -*- coding: utf-8 -*-
import re, os, datetime, html as H
OUT="/sessions/eloquent-magical-fermat/mnt/outputs"
F={k:open(os.path.join(OUT,v),encoding='utf-8').read() for k,v in
   {"ix":"index.html","cy":"cyber-briefing.html","ws":"wallstreet-briefing.html","mm":"mma-briefing.html"}.items()}
N=[0];FAIL=[]
def ck(c,m):
    N[0]+=1
    if not c: FAIL.append(m)

# ---- structure
for k,s in F.items():
    ck(s.count("<!DOCTYPE html>")==1,k+" doctype")
    ck(s.count("<body>")==1,k+" body")
    ck(s.count('<nav class="tabs">')==1,k+" nav")
    ck(s.count('nav.tabs')>=1,k+" navcss")
    ck(len(re.findall(r'<nav class="tabs">.*?</nav>',s,re.S)[0].split('<a ')) -1==5,k+" 5 navlinks")
    ck(re.findall(r'<nav class="tabs">.*?</nav>',s,re.S)[0].count('class="active"')==1,k+" 1 active")
    ck(s.count("<footer>")==1 or k=="ix",k+" footer")
    ck("@@" not in s,k+" no @@")
    for g in ("&#9733;","&#9960;","&#9650;","&#8856;","&#128452;"):
        ck(g in s,k+" glyph "+g)
    ck("&#9924;" not in s and "&#9704;" not in s,k+" bad glyph")
    ck('id="datestamp"' in s and 'id="updated"' in s and 'id="edition"' in s,k+" meta ids")
    ck('id="freshline"' in s,k+" freshline")
    ck("Intl.DateTimeFormat" in s,k+" stamp js")
# tldr strip only on the three briefings
for k in ("cy","ws","mm"): ck(F[k].count('class="tldr"')==1,k+" one tldr")
ck('class="tldr"' not in F["ix"],"ix no tldr")
ck("The Wire" in F["cy"] and "The Tape" in F["ws"] and "Tale of the Tape" in F["mm"],"tldr labels")

# ---- index cards match TLDRs verbatim
import importlib.util
spec=importlib.util.spec_from_file_location("b","/tmp/db_1789760104/build_0918_1538.py")
b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
for tl,pg in ((b.TL_CY,"cy"),(b.TL_WS,"ws"),(b.TL_MMA,"mm")):
    ck(tl in F["ix"],"ix card verbatim "+pg)
    ck(tl in F[pg],"tldr verbatim "+pg)

# ---- TradingView blocks
blocks=["ticker-tape","single-quote","timeline","stock-heatmap","mini-symbol-overview","events"]
for bl in blocks:
    ck(("embed-widget-%s.js"%bl) in F["ws"],"ws has "+bl)
    for k in ("ix","cy","mm"): ck(("embed-widget-%s.js"%bl) not in F[k],k+" lacks "+bl)
ck(F["ws"].count("embed-widget-single-quote.js")==3,"3 single quotes")
for sym in ("FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"):
    ck(sym in F["ws"],"tape keeps "+sym)
ck('"symbol":"NASDAQ:XENE"' in F["ws"],"chart of day XENE")

# ---- KEV countdown: computed, exactly 3 mentions of the date, BOD 22-01 once
due=datetime.date(2026,9,19); today=datetime.date(2026,9,18)
ck((due-today).days==1,"due is tomorrow")
ck(F["cy"].count("19 September 2026")+F["cy"].count("Saturday, 19 September")==0 or True,"noop")
n19=len(re.findall(r'19 September 2026',F["cy"]))
ck(n19==3,"19 September 2026 x3 (got %d)"%n19)
ck(F["cy"].count("1 day left")==3,"countdown x3 (got %d)"%F["cy"].count("1 day left"))
ck(F["cy"].count("BOD 22-01")==1,"BOD 22-01 once")
ck(F["cy"].count("BOD 26-04")>=1,"BOD 26-04 named")
ck("21 September 2026" in F["cy"],"linux kev date attributed")
ck("could not be re-confirmed this run" in F["cy"],"linux kev caveat")
ck("No due date for this entry was confirmed" in F["cy"],"acronis no date")

# ---- champions
tb=re.search(r'Champions Board.*?</table>',F["mm"],re.S).group(0)
rows=re.findall(r'<tr><td>(.*?)</td><td class="(win|nc)">(.*?)</td><td>(.*?)</td></tr>',tb)
ck(len(rows)==11,"11 champ rows (got %d)"%len(rows))
vac=[r[0] for r in rows if r[2]=="VACANT"]
ck(len(vac)==2,"2 vacant")
ck("Heavyweight" in vac[0] and "Flyweight" in vac[1],"vacant are HW + WFlyw")
cells=" ".join(r[2] for r in rows)
for bad in ("Pereira","Chimaev","Shevchenko","Aspinall","Topuria","Ankalaev","Pantoja","Dvalishvili","Nunes","Proch"):
    ck(bad not in cells,"banned in champ cell: "+bad)
for div,champ in (("Light Heavyweight","Carlos Ulberg"),("Middleweight","Sean Strickland"),
                  ("Welterweight","Islam Makhachev"),("Lightweight","Justin Gaethje"),
                  ("Featherweight","Alexander Volkanovski"),("Bantamweight","Petr Yan"),
                  ("Flyweight","Joshua Van"),("Women&rsquo;s Bantamweight","Kayla Harrison"),
                  ("Women&rsquo;s Strawweight","Mackenzie Dern")):
    ck(any(r[0]==div and r[2]==champ for r in rows),"belt pinned %s=%s"%(div,champ))
ck("Ciryl Gane" in tb and "Ciryl Gane" not in cells,"Gane interim only")
ck(tb.count("Carlos Ulberg")==1,"Ulberg once in table")

# ---- dates chronology
ck("Sat 19 Sep" in F["mm"] and "Sat 26 Sep" in F["mm"] and "Sat 3 Oct" in F["mm"] and "Sat 24 Oct" in F["mm"],"4 cards")
ck("12 September" in F["mm"],"last event past")
ck("2026-09-19T21:00:00-04:00" in F["mm"],"countdown target")
ck('id="ufccdn"' in F["mm"],"countdown el")

# ---- new tags
ck(F["cy"].count('tag new">New')==2,"cyber 2 new (got %d)"%F["cy"].count('tag new">New'))
ck(F["ws"].count('tag new">New')==0,"ws 0 new (got %d)"%F["ws"].count('tag new">New'))
ck(F["mm"].count('tag new">New')==1,"mma 1 new (got %d)"%F["mm"].count('tag new">New'))
ck("<b>Two</b> items are tagged New" in F["cy"],"cy states count")
ck("<b>zero</b> New tags" in F["ws"],"ws states count")
ck("<b>one</b> New tag" in F["mm"],"mma states count")

# ---- markets arithmetic
def pct(lvl,chg): return chg/(lvl-chg)*100
for lvl,chg,want in ((7641.18,4,0.05),(51655,-123,-0.24),(29517,70,0.24)):
    ck(abs(pct(lvl,chg)-want)<0.006,"reconcile %s"%lvl)
for lvl,chg,want in ((103.204,1.29,1.27),(4354.39,13.00,0.30),(66.394,1.20,1.84),
                     (104.789,-0.03,-0.03),(79038,2627,3.44)):
    ck(abs(pct(lvl,chg)-want)<0.01,"reconcile cmdty %s"%lvl)
# VIX inconsistency asserted, refused
ck("refused for a seventh consecutive edition" in F["ws"],"vix refusal")
ck("15" in F["ws"] and "&minus;0.23%" in F["ws"],"vix figures shown")
# colour classes by sign
for name,cls in (("WTI crude","up"),("Brent crude","down"),("Gold","up"),("Silver","up"),
                 ("Bitcoin","up"),("US 10-year Treasury yield","up")):
    m=re.search(r'<td>%s</td><td>[^<]*</td><td class="(\w+)">'%re.escape(name),F["ws"])
    ck(m and m.group(1)==cls,"colour %s=%s"%(name,cls))
# scorecard empty
ck(F["ws"].count("Not re-verified this run")==12,"12 empty cells (got %d)"%F["ws"].count("Not re-verified this run"))
ck(F["ws"].count("Session in progress")==3,"friday in progress")
ck(F["ws"].count("7,637.29")==1,"withheld level once")
# no after-hours section before 4pm
ck("After-Hours Movers" not in F["ws"],"no after-hours section")
ck("as of ~3:37 PM ET" in F["ws"] or "~3:37 PM ET" in F["ws"],"as-of time stated")

# ---- refusals named on page
for t in ("40% in early 2026","CVE-2026-58138","empty bodies"):
    ck(t in F["cy"],"cy refusal "+t)
for t in ("$100.70","impossible","Meta appears twice"):
    ck(t in F["ws"],"ws refusal "+t)
ck("not re-cross-checked against ESPN this run" in F["mm"],"mma espn note")

# ---- misc content
ck("0:36" in F["mm"] and "0:33" not in F["mm"],"king ko time")
ck("Joseph Morales" in F["mm"] and "No winner asserted" not in F["mm"],"moreno row")
ck("Doo Ho Choi" in F["mm"],"choi name")
ck(F["cy"].count("class='warn'")==0 and F["cy"].count('class="warn"')==0,"no undefined warn class")

print("CHECKS: %d   FAILURES: %d"%(N[0],len(FAIL)))
for f in FAIL: print("  FAIL:",f)
