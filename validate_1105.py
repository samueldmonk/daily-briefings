# -*- coding: utf-8 -*-
import io,re,sys
O="/sessions/tender-hopeful-newton/mnt/outputs/"
F=["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]
S={f:io.open(O+f,encoding='utf-8').read() for f in F}
fails=[];checks=0
def req(f,p,why):
    global checks; checks+=1
    if p not in S[f]: fails.append("MISSING [%s] %s :: %s"%(f,why,p[:80]))
def forbid(f,p,why):
    global checks; checks+=1
    if p in S[f]: fails.append("FORBIDDEN [%s] %s :: %s"%(f,why,p[:80]))

# --- structural: five-tab nav, masthead ids, tldr on briefings
for f in F:
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        req(f,'href="%s"'%tab,"five-tab nav")
    for i in ['id="edition"','id="datestamp"','id="updated"']:
        req(f,i,"masthead pill")
    req(f,"America/New_York","self-stamp JS")
for f in F[1:]:
    req(f,'class="tldr"',"summary strip"); req(f,'id="freshline"',"freshline")
    req(f,'Data as of 11:05 AM ET',"freshline stamped this edition")
    forbid(f,'Data as of 10:50 AM ET',"stale freshline")
req("index.html",'Data as of 11:05 AM ET',"index freshline")

# --- markets live widget blocks A-F
for w in ["embed-widget-ticker-tape.js","embed-widget-single-quote.js","embed-widget-timeline.js",
          "embed-widget-stock-heatmap.js","embed-widget-mini-symbol-overview.js","embed-widget-events.js"]:
    req("wallstreet-briefing.html",w,"live widget block")
req("wallstreet-briefing.html","FOREXCOM:SPXUSD","index widget"); req("wallstreet-briefing.html","TVC:US10Y","10y in tape")
req("wallstreet-briefing.html","TVC:USOIL","oil in tape")

# --- MARKETS numbers (Friday closes, reconciliation)
for p in ["7,711.76","26,402.42","53,559.99","7,730.99","26,541.35","53,569.44"]:
    req("wallstreet-briefing.html",p,"verified close")
forbid("wallstreet-briefing.html","7,673.04","aggregator level never promoted")
forbid("wallstreet-briefing.html","After-Hours Movers","weekend: no after-hours section")
forbid("wallstreet-briefing.html","as of ~","no intraday as-of on a closed tape")
assert abs(53569.44-9.45-53559.99)<0.005
assert abs((7711.76/7730.99-1)*100+0.2487)<0.005
assert abs((26402.42/26541.35-1)*100+0.5234)<0.005
checks+=3
# new payroll items
for p in ["Capital Economics","<b>a modest 90,000</b>","+58,000","<b>+80,000</b>","<b>June was revised down to a +20,000 gain</b>",
          "Neither is adopted and nothing is averaged","roughly <b>32,000 apart</b>"]:
    req("wallstreet-briefing.html",p,"11:05 payrolls block")
assert 90000-58000==32000
checks+=1
req("wallstreet-briefing.html","Tuesday, September 1","week-ahead dates")
req("wallstreet-briefing.html","Beige Book","week-ahead dates")
req("wallstreet-briefing.html","Only the days are asserted, not the consensus figures","no invented consensus")
req("wallstreet-briefing.html","not investment advice","disclaimer")
forbid("wallstreet-briefing.html","with Friday&rsquo;s payrolls report the next test","stale tldr")

# --- CYBER: Avada family
cy="cyber-briefing.html"
for p in ["CVE-2026-18431","<b>9.8</b>","Avada up to 7.16","up to 3.16","Avada 7.16.1","Fusion Builder 3.16.1",
          "<b>Argus</b>","<b>about two hours</b>","<b>more than 1 million sales</b>","July 30","August 5","August 10"]:
    req(cy,p,"Avada verified detail")
req(cy,"not KEV-listed","Avada KEV disclaimer")
req(cy,"No source seen this run states <b>in-the-wild","Avada exploitation disclaimer")
req(cy,"&le; 7.1&rdquo;","aggregator discrepancy disclosed")
# Ubiquiti rows keep their disclaimers, demoted tags
for p in ["CVE-2026-77537","CVE-2026-77550","CVE-2026-77554"]: req(cy,p,"ubnt row")
forbid(cy,"New &middot; 10:50 AM","stale New tag on cyber")
# McKesson record-vs-people refusal must survive
for p in ["records, not people","does not know how many unique people","This page prints neither as a victim count",
          "not independently verified","$55,236,150","mckesson[.]claims"]:
    req(cy,p,"McKesson guard")
req(cy,"puts it at <b>two</b> employees","11:05 vishing count")
# ATF DOJ family
for p in ["cut off access to the affected system","senior Department of Justice officials designated",
          "not a severity adjective the agency","Qilin has made no specific claim"]:
    req(cy,p,"ATF 11:05 block")
req(cy,"ATF itself has not attributed the incident to Qilin","ATF attribution guard")
# KEV deadlines consistent
for p in ["CVE-2026-8452","CVE-2019-1068","due today"]: req(cy,p,"KEV deadline family")

# --- MMA
mm="mma-briefing.html"
for p in ["$400,000 in bonuses","corroboration of the same four, not a fifth\naward" .replace("\n"," "),
          "Denise Gomes did not receive a bonus","Song Yadong</b> by name"]:
    if p not in S[mm]:
        # allow line-wrapped
        if re.sub(r'\s+',' ',p) not in re.sub(r'\s+',' ',S[mm]): fails.append("MISSING [mma] bonus corrob :: "+p[:70])
    checks+=1
req(mm,"Fight of the Night: Liu Ce vs. Levi Rodrigues Jr.","bonus recipients")
req(mm,"<b>Performance of the Night: Song Yadong</b> and <b>Bilal Hasan</b>","bonus recipients")
# champions board correctness (CORRECTIONS.md authority)
CH=[("Heavyweight","Tom Aspinall"),("Light Heavyweight","Carlos Ulberg"),("Middleweight","Sean Strickland"),
    ("Welterweight","Islam Makhachev"),("Lightweight","Justin Gaethje"),("Featherweight","Alexander Volkanovski"),
    ("Bantamweight","Petr Yan"),("Flyweight","Joshua Van"),("Kayla Harrison","Kayla Harrison"),
    ("Valentina Shevchenko","Valentina Shevchenko"),("Mackenzie Dern","Mackenzie Dern")]
for d,c in CH: req(mm,c,"champion "+d)
req(mm,"Ciryl Gane","interim HW")
# every Pereira/Chimaev mention must sit next to its rejection/interim framing
flat=re.sub(r'\s+',' ',S[mm])
for name in ["Pereira","Chimaev"]:
    for m in re.finditer(name,flat):
        checks+=1
        ctx=flat[max(0,m.start()-320):m.start()+320]
        if not any(k in ctx for k in ["Interim","interim","superseded","split decision","took the middleweight belt",
                                      "naming Alex","rejected","regressions","KO2"]):
            fails.append("CONTEXT [mma] bare %s mention :: %s"%(name,ctx[:120]))
req(mm,"fifty-first consecutive","board-unchanged counter advanced")
forbid(mm,"fiftieth consecutive","stale counter")
req(mm,"agrees with this board on every men&rsquo;s\nbelt it covered".replace("\n"," ") if "agrees with this board on every men&rsquo;s belt it covered" in flat else "agrees with this board","11:05 ESPN re-check")
req(mm,"the exact reverse\nof the 10:50 AM result".replace("\n"," ") if "the exact reverse of the 10:50 AM result" in flat else "exact reverse","re-check framing")
req(mm,"a single search is not a verification method","method statement")
req(mm,"UFC Shanghai carried no title bout","independent reason board static")
req(mm,"Cards and bouts are subject to change","disclaimer")
# no fabricated business figures
forbid(mm,"viewership of","unsourced viewership")

# --- index cards mirror each page's own tldr
def tl(f):
    m=re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>',S[f],re.S); return m.group(1).strip()
for f in F[1:]:
    checks+=1
    if tl(f) not in S["index.html"]: fails.append("INDEX card out of sync with "+f)

# --- no duplicate source hrefs, all footers non-empty
for f in F[1:]:
    hrefs=re.findall(r'<div class="srcs">.*?</div>',S[f],re.S)
    checks+=1
    if not hrefs: fails.append("no sources footer in "+f); continue
    links=re.findall(r'href="(http[^"]+)"',hrefs[0])
    checks+=1
    if len(links)!=len(set(links)): 
        d=[x for x in set(links) if links.count(x)>1]
        fails.append("DUPLICATE source links in %s :: %s"%(f,d[:3]))
    if len(links)<8: fails.append("thin sources footer in "+f)

# --- chronology: nothing "upcoming" that has passed
forbid(mm,"Upcoming</span></div>\n<h4>UFC Fight Night &mdash; Nurmagomedov","completed card tagged upcoming")
req(mm,"Complete.","completed card labelled")

print("CHECKS: %d   FAILURES: %d"%(checks,len(fails)))
for x in fails: print("  X",x)
sys.exit(1 if fails else 0)
