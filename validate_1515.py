# -*- coding: utf-8 -*-
import re,sys
F={p:open(p,encoding='utf-8').read() for p in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
cy,ws,mm,ix=F['cyber-briefing.html'],F['wallstreet-briefing.html'],F['mma-briefing.html'],F['index.html']
n=0; fails=[]
def chk(cond,msg):
    global n
    n+=1
    if not cond: fails.append(msg)

# --- structural: five-tab nav, masthead pills, freshline, self-stamp on all four
for p,s in F.items():
    for href in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        chk('href="%s"'%href in s, "%s missing nav %s"%(p,href))
    for pid in ['edition','datestamp','updated']:
        chk('id="%s"'%pid in s, "%s missing pill %s"%(p,pid))
    chk("America/New_York" in s, p+" missing self-stamp JS")
    chk('id="freshline"' in s, p+" missing freshline")
    chk(s.count('<html')==1 and s.rstrip().endswith('</html>'), p+" malformed")

# --- tldr present on the three briefings, absent from index
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    chk('class="tldr"' in F[p], p+" missing tldr")
chk('class="tldr"' not in ix, "index must not carry a tldr strip")
chk('The Wire' in cy and 'The Tape' in ws and 'Tale of the Tape' in mm, "tldr labels wrong")

# --- index cards byte-identical to tldrs
def tldr(s):
    return re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>', s, re.S).group(1)
for cls,src,lab in [('c-cy',cy,'cyber'),('c-ws',ws,'markets'),('c-mm',mm,'mma')]:
    m=re.search(r'<div class="card '+cls+r'">.*?</div>\n<h3>.*?</h3>\n<p>(.*?)</p>', ix, re.S)
    chk(m is not None and m.group(1)==tldr(src), "index card not byte-identical to tldr: "+lab)

# --- freshness tag guard
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    tags=re.findall(r'<span class="tag new">([^<]*)</span>', F[p])
    chk(len(tags)>0, p+" has no fresh tag")
    for t in tags:
        chk('3:15' in t, "%s stale fresh tag: %r"%(p,t))
    chk('<span class="tag new">New</span>' not in F[p], p+" bare New tag")

# --- TradingView widget blocks (Wall Street)
for w in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']:
    chk('embed-widget-%s.js'%w in ws, "ws missing widget "+w)
chk(ws.count('embed-widget-single-quote.js')==3, "ws must have exactly 3 single-quote widgets")
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    chk(sym in ws, "ws ticker tape missing "+sym)
chk('NASDAQ:OKTA' in ws, "Chart of the Day symbol missing")
chk('class="livebar"' in ws, "ws missing livebar")
for p in ['index.html','cyber-briefing.html','mma-briefing.html']:
    chk('tradingview' not in F[p].lower(), p+" must not carry live widgets")

# --- champions board: parse real <td> cells, regression traps
rows=re.findall(r'<tr>(.*?)</tr>', mm[mm.find('Champions Board'):], re.S)
cells=[re.findall(r'<td[^>]*>(.*?)</td>', r, re.S) for r in rows]
champrows=[c for c in cells if len(c)>=2]
chk(len(champrows)>=11, "champions board has %d rows, expected >=11"%len(champrows))
def champcell(div_kw):
    for c in champrows:
        if div_kw.lower() in re.sub('<[^>]+>','',c[0]).lower(): return re.sub('<[^>]+>','',c[1])
    return None
lhw=champcell('Light Heavyweight'); mw=champcell('Middleweight')
fw=champcell('Featherweight'); lw=champcell('Lightweight')
chk(lhw and 'Ulberg' in lhw and 'Pereira' not in lhw, "LHW regression: %r"%lhw)
chk(mw and 'Strickland' in mw and 'Chimaev' not in mw, "MW regression: %r"%mw)
chk(fw and 'Volkanovski' in fw and 'vacant' not in fw.lower(), "FW regression: %r"%fw)
chk(lw and 'Gaethje' in lw and 'Topuria' not in lw, "LW regression: %r"%lw)
for d,exp in [('Heavyweight','Aspinall'),('Welterweight','Makhachev'),('Bantamweight','Yan'),('Flyweight','Van')]:
    c=champcell(d); chk(c is not None, "no champion cell for "+d)

# --- name traps
for bad in ['Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman']:
    chk(bad not in mm, "MMA trap string present: "+bad)
chk('Balleto' in mm and 'Balletto' in mm, "MMA: both Balleto spellings must remain printed")
chk('Aoriqileng' in mm and 'Qileng Aori' in mm, "MMA: both Aoriqileng spellings must be printed")
chk('Sumudaerji' in mm and 'Su Mudaerji' in mm, "MMA: both Sumudaerji spellings must be printed")
chk('Nilson Rojas' in mm, "MMA: Hasan opponent missing")
chk("the favourite's price is stable across them" not in mm, "MMA: retired 'stable across them' claim still present")
for o in ['−550','+400','−500','−470','+380','+385','+360']:
    chk(o in mm, "MMA odds read missing: "+o)

# --- MMA countdown
chk('ufccdn' in mm, "MMA countdown element missing")
chk('Oriental Sports Center' in mm, "MMA next card venue missing")

# --- Cyber: CVE whitelist
WL={'2026-21962','2026-8452','2019-1068','2015-3246','2015-5287','2021-23758','2022-0995','2026-60004','2026-68820','2026-73570','2026-72529','2026-72530','2026-33824','2026-55040','2026-59310','2026-65400','2026-20349','2026-72898','2026-8037','2026-45659','2026-58231','2026-20253','2026-12569','2026-64633','2026-65641','2026-69836','2026-18963','2026-19490','2026-19912','2026-19913','2026-62815','2026-62893'}
found=set(re.findall(r'CVE-(\d{4}-\d{4,6})', cy))
chk(len(found)>=25, "CVE liveness: only %d ids found"%len(found))
unlisted=found-WL
chk(not unlisted, "unlisted CVE ids on cyber page: %s"%sorted(unlisted))

# --- Cyber: deadlines consistent in 4+ places, BOD directive
chk(cy.count('Aug 29')+cy.count('August 29')>=4, "Aug 29 must appear in >=4 places")
chk('BOD 22-01' not in cy, "retired BOD 22-01 present")
chk('BOD 26-04' in cy, "BOD 26-04 missing")
chk('September 9' in cy or 'Sept 9' in cy, "Sept 9 tail missing")
chk('due today' in cy or 'expires today' in cy, "today's deadline not stated")
chk('(0 days left)' in cy, "WebLogic countdown must read 0 days left")
chk(cy.count('CVE-2026-21962')>=6, "WebLogic CVE under-referenced")
chk('Infosecurity Magazine' in cy, "new KEV conflict source not cited")
chk('Help Net Security' in cy, "vendor corroboration source not cited")
chk('Memory-overflow flaw' in cy, "8452 vendor framing missing")
chk('8.8 (assigned by Citrix)' in cy, "8452 vendor score missing")
chk('with the business day nearly over' in cy, "cyber deadline not retimed for this run")
chk(cy.count('with the business day nearly over')>=2, "retimed deadline must appear in tldr and banner")
chk('about two hours of the East Coast' not in cy, "stale 'two hours' text still present")
chk('2,200' in cy and '1,900' in cy, "both Qilin counts must be printed")
# Patch Priority callout severity
chk('class="callout crit"' in cy, "Patch Priority must be crit (deadline today)")
# threat level banner + stat strip
chk('Threat level' in cy, "threat banner missing")
chk(cy.count('<div class="stat">')>=4, "stat strip needs >=4 tiles")

# --- Wall Street: window-scoped rejected figures stay rejected
for fig in ['7,673.04','6,279','$3.97 trillion','1.82%']:
    chk(fig in ws, "ws lost rejection record for "+fig)
chk('Not published' in ws, "ws rejection language missing")
# Jackson Hole inverted guard
chk('That reasoning was wrong.' in ws, "Jackson Hole self-correction must stay published")
# new figures present
for fig in ['0.15%','1.32%','8.34%','2.3%','0.58%','$435 billion','7,727','208,000','22.68%','19.67%','22.75%','19.75%']:
    chk(fig in ws, "ws missing new figure "+fig)
# retired sentences gone
chk('remain the only numeric sector reads printed here' not in ws, "ws stale sector claim present")
chk('The S&amp;P 500 and Dow are unchanged from the 2:21 read' not in ws, "ws stale unchanged claim present")
# arithmetic: 7,727 must reconcile with 7,675.70 at +0.67%
chk(abs(7675.70*1.0067-7727.1)<0.5, "7,727 reconciliation arithmetic wrong")
chk('7,675.70' in ws, "prior close missing")
# no close asserted before the bell
chk('closed at 7,7' not in ws, "ws must not assert a close for today")
# as-of time stated
chk('as of ~3:15 PM ET' in ws, "ws lead must state the as-of time")
chk('3:05 PM ET' in ws, "ws missing timestamped read")

# --- footers / disclaimers
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    chk('<footer>' in F[p], p+" missing footer")
    chk(F[p].count('https://')>=10, p+" too few source URLs")
    chk('Fetched 3:15 PM ET' in F[p], p+" missing this-run sources")
chk('investment advice' in ws and 'class="disc"' in ws, "ws disclaimer missing")
chk('subject to change' in mm, "mma disclaimer missing")

print("checks:",n,"failures:",len(fails))
for f in fails: print("  FAIL:",f)
sys.exit(1 if fails else 0)
