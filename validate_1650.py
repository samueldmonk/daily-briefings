# -*- coding: utf-8 -*-
import re, io, json
from html.parser import HTMLParser
D="/tmp/db_1787690028/"
PAGES=["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]
fails=[]; checks=0
def ck(cond,msg):
    global checks
    checks+=1
    if not cond: fails.append(msg)
def rd(p): return io.open(D+p,encoding="utf-8").read()

VOID=set("area base br col embed hr img input link meta param source track wbr".split())
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

pg={p:rd(p) for p in PAGES}
for p in PAGES:
    b=B(); b.feed(pg[p])
    ck(len(b.st)==0, "%s unclosed %s"%(p,b.st[:6]))
    ck(b.stray==0, "%s stray %d"%(p,b.stray))
    nav=re.search(r'<nav class="tabs">(.*?)</nav>', pg[p], re.S)
    ck(nav is not None, "%s no nav"%p)
    if nav:
        hrefs=re.findall(r'href="([^"]+)"', nav.group(1))
        ck(hrefs==["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"], "%s nav order %s"%(p,hrefs))
        on=re.findall(r'<a href="([^"]+)" class="on">', nav.group(1))
        ck(on==[p], "%s active tab %s"%(p,on))
    for i_ in ["edition","datestamp","updated"]:
        ck(('id="%s"'%i_) in pg[p], "%s missing id %s"%(p,i_))
    ck(pg[p].count('<div class="tldr">')==(0 if p=="index.html" else 1), "%s tldr count"%p)
    ck('id="freshline"' in pg[p] or p=="index.html", "%s freshline"%p)

# per-page tldr labels
ck('<b>The Wire</b>' in pg["cyber-briefing.html"], "cy tldr label")
ck('<b>The Tape</b>' in pg["wallstreet-briefing.html"], "ws tldr label")
ck('<b>Tale of the Tape</b>' in pg["mma-briefing.html"], "mma tldr label")

# index cards carry tldr verbatim
def tl(page,key):
    p=pg[page]; s=p.index('<div class="tldr"><b>%s</b> <span>'%key)+len('<div class="tldr"><b>%s</b> <span>'%key)
    return p[s:p.index('</span></div>',s)]
for cls,page,key in [("c-sec","cyber-briefing.html","The Wire"),("c-mkt","wallstreet-briefing.html","The Tape"),("c-mma","mma-briefing.html","Tale of the Tape")]:
    a=pg["index.html"].index('<a class="bcard %s"'%cls)
    seg=pg["index.html"][a:a+4000]
    ck(tl(page,key) in seg, "index card %s not verbatim"%cls)

# TradingView JSON blocks parse
tv=re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>', pg["wallstreet-briefing.html"], re.S)
ck(len(tv)==8, "tv block count %d"%len(tv))
for j in tv:
    try: json.loads(j)
    except Exception as e: fails.append("tv json %s"%e)
    checks+=1
tape=[t for t in tv if '"symbols"' in t][0]
for s in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(s in tape, "tape missing %s"%s)
mini=[t for t in tv if 'dateRange' in t][0]
ck(json.loads(mini)["symbol"]=="NYSE:DKS", "chart of day symbol")

# KEV countdowns
kev=re.findall(r'class="kevdue([^"]*)"', pg["cyber-briefing.html"])
ck(len(kev)==13, "kev rows %d"%len(kev))
body=pg["cyber-briefing.html"]
ck(body.count("DUE TODAY &mdash; 0 days left")==1, "kev due today count")
ck(len(re.findall(r'class="kevdue crit">\d+ days? PAST DUE',body))==9, "kev past due count")
ck(len(re.findall(r'class="kevdue ok">\d+ days left',body))==3, "kev ahead count")

# champions column only
mma=pg["mma-briefing.html"]
champ_tbl=mma[mma.index('Champions board'):]
rows=re.findall(r'<tr>(.*?)</tr>', champ_tbl, re.S)[:12]
ck(len(rows)==12, "champ rows %d"%len(rows))
champcells=[]
for r in rows[1:]:
    tds=re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
    if len(tds)>=2: champcells.append(re.sub('<[^>]+>','',tds[1]))
ck(len(champcells)==11, "champ cells %d"%len(champcells))
allc=" | ".join(champcells)
for name in ["Aspinall","Ulberg","Strickland","Makhachev","Gaethje","Volkanovski","Yan","Van"]:
    ck(name in allc, "champ missing %s"%name)
for bad in ["Pereira","Chimaev","Topuria","Pantoja","Dvalishvili","vacant","Vacant"]:
    ck(bad not in allc, "champ stale %s"%bad)

# index reconciliations
recs=[(7677.28,7652.86,24.42,0.32),(53577.40,53417.16,160.24,0.30),(26151.30,25980.19,171.11,0.66)]
for close,prev,chg,pct in recs:
    ck(round(close-prev,2)==chg, "recon chg %s"%close)
    ck(abs(round(chg/prev*100,2)-pct)<=0.01, "recon pct %s"%close)

ws=pg["wallstreet-briefing.html"]
for g in ["7,677.28","26,151.30","53,577.40","+24.42","+160.24","+171.11","3,010.02","15.49","4,723.10","78,851.16","80.57","&minus;5.22%","30.68%","124.31","7,676.62","26,145.47","53,572.91","preliminary","4.625%","$4.03","$4.35","22.88","27.34","23.7","6.08","184%","&minus;7.3%","16%","consumer confidence fell in August","25-basis-point rate increase","Quinlan","Malek","third straight winning session","eighteenth consecutive run"]:
    ck(g in ws, "ws guard missing: %s"%g)
ck('class="lab">After-hours movers</div>' in ws, "ws after-hours section present")
ck('markets closed higher today' not in ws.lower(), "ws trap phrase")
ck("Nvidia&rsquo;s results" not in ws and "Nvidia's results" not in ws, "ws nvidia results trap")
ck(ws.count('<span class="tag new">New</span>')==2, "ws New count %d"%ws.count('<span class="tag new">New</span>'))

cy=pg["cyber-briefing.html"]
for g in ["E4del","PINHOLE","FTP banner","SOCRadar","MalwareHunterTeam","Halo","Early Bird APC","69.48.228[.]126:5000","11 execution events","119&nbsp;KB","Weston Computing Systems","CVE-2026-15981","CVE-2026-61979","17.0.6","17.0.5","mo_saml_validate_signature","openssl_verify","wp_set_auth_cookie","64.225.25.188","Mirage2FA","9,426","LinX Coders","CVE-2026-21962","CVE-2026-68820","CVE-2026-73570","BOD&nbsp;26-04","Nothing was added on August&nbsp;25","ninth"]:
    ck(g in cy, "cy guard missing: %s"%g)
ck(cy.count('<span class="tag new">New</span>')==0, "cy New count %d"%cy.count('<span class="tag new">New</span>'))

mm=pg["mma-briefing.html"]
for g in ["Umar Nurmagomedov","Song Yadong","Shanghai Oriental Sports Center","Yan Xiaonan","Denise Gomes","Aoriqileng","Kai Asakura","23-9-1","20-1","&minus;500","&minus;470","Carlos Ulberg","UFC Fight Night 286","ninth"]:
    ck(g in mm, "mma guard missing: %s"%g)
ck(mm.count('<span class="tag new">New</span>')==1, "mma New count %d"%mm.count('<span class="tag new">New</span>'))
for bad in ["Cody Salkilld","Abdul-Rakhman","Shamil Yakhyaev","title challenger Beneil","Shanghai Indoor Stadium","Pereira retains","Featherweight vacant"]:
    for p in PAGES: ck(bad not in pg[p], "trap %s in %s"%(bad,p))

idx=pg["index.html"]
ck(idx.count('<span class="tag new">New</span>')==0, "index New count")

print("checks=%d fails=%d"%(checks,len(fails)))
for f in fails: print("  FAIL:",f)
