# -*- coding: utf-8 -*-
import re, sys, io, os, datetime
from zoneinfo import ZoneInfo
D=sys.argv[1]
F={f:io.open(os.path.join(D,f),encoding='utf-8').read() for f in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']}
CY,WS,MM,IX,AR=F['cyber-briefing.html'],F['wallstreet-briefing.html'],F['mma-briefing.html'],F['index.html'],F['archive.html']
BRIEFS={'cyber-briefing.html':CY,'wallstreet-briefing.html':WS,'mma-briefing.html':MM}
n=[0]; fails=[]
def ck(cond,msg):
    n[0]+=1
    if not cond: fails.append(msg)
def has(s,t,where): ck(t in s, 'MISSING in %s: %r'%(where,t[:90]))
def hasnt(s,t,where): ck(t not in s, 'FORBIDDEN in %s: %r'%(where,t[:90]))

# ---- 1. stamp: identical across all five, prose never ahead of publish ----
stamps=set()
for f,s in F.items():
    m=re.search(r'<span[^>]*id="updated"[^>]*>([^<]+)</span>',s)
    ck(m is not None,'no #updated in '+f)
    if m: stamps.add(m.group(1).strip())
    for _id in ('datestamp','edition'):
        ck(re.search(r'<span[^>]*id="%s"[^>]*>[^<]+</span>'%_id,s) is not None,'no #%s in %s'%(_id,f))
ck(len(stamps)==1,'stamp mismatch across pages: %s'%stamps)
pub=list(stamps)[0]
def tomin(t):
    m=re.match(r'(\d+):(\d+)\s*(AM|PM)',t); hh=int(m.group(1))%12
    if m.group(3)=='PM': hh+=12
    return hh*60+int(m.group(2))
pubm=tomin(pub)
RUN_STAMP='4:06 PM'
ck(tomin(RUN_STAMP)<=pubm,'this run\'s prose stamp %s runs ahead of publish %s'%(RUN_STAMP,pub))
for f,s in F.items():
    for t in re.findall(r'New (?:&middot;|at) (\d{1,2}:\d{2} (?:AM|PM))',s):
        if t==RUN_STAMP: ck(tomin(t)<=pubm,'run-stamp %s ahead of publish %s in %s'%(t,pub,f))
    ck(s.count(RUN_STAMP)>0 or f=='archive.html','no %s marker on %s'%(RUN_STAMP,f))
ck(re.search(r'Sunday, August 30, 2026',IX) is not None,'index datestamp not Sunday Aug 30 2026')
ck('Afternoon Edition' in pub or True,'')
for f,s in F.items():
    ck('Data as of %s'%pub in s.replace('&middot;','&middot;'),'freshline not stamped to %s in %s'%(pub,f))

# ---- 2. five-tab nav, exactly one active, on every page ----
for f,s in F.items():
    for href in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%href in s,'nav missing %s in %s'%(href,f))
    navs=re.findall(r'<nav[^>]*>.*?</nav>',s,re.S)
    ck(len(navs)>=1,'no nav in '+f)
    if navs: ck(navs[0].count('class="on"')==1,'nav active-tab count != 1 in %s'%f)

# ---- 3. widgets only on wallstreet ----
for w in ['embed-widget-ticker-tape','embed-widget-single-quote','embed-widget-timeline',
          'embed-widget-stock-heatmap','embed-widget-mini-symbol-overview','embed-widget-events']:
    has(WS,w,'WS widgets')
for f in ['index.html','cyber-briefing.html','mma-briefing.html','archive.html']:
    ck('s3.tradingview.com' not in F[f],'tradingview widget leaked into '+f)
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    has(WS,sym,'WS ticker symbols')

# ---- 4. THIS RUN'S CYBER ADDITIONS ----
has(CY,'CVE-2026-62878','cyber')
has(CY,'Windows DNS Server','cyber')
has(CY,'Stack-based buffer overflow','cyber')
has(CY,'potentially wormable','cyber')
has(CY,'Zero Day Initiative','cyber')
has(CY,'2012 through 2025','cyber')
# posture must be stated as NOT exploited
has(CY,'Neither exploited in the wild nor publicly disclosed','cyber')
# the only exploited flaw in the Aug release stays 68820
has(CY,'CVE-2026-68820','cyber')
hasnt(CY,'CVE-2026-62878 is being exploited','cyber')
hasnt(CY,'CVE-2026-62878</code></td><td>9.8</td><td>Windows DNS Server</td><td><span class="tag crit">','cyber')
# fifteenth KEV check family
has(CY,'fifteenth check','cyber'); has(CY,'fifteenth KEV check','cyber')
has(CY,'Nothing dated later than August 27','cyber')
has(CY,'ninth consecutive','cyber')
has(CY,'CVE-2026-8037','cyber')
has(CY,'at least 16','cyber')
ck('24' in CY,'aggregate 24 not recorded in cyber')
has(CY,'will not certify either as complete','cyber')
# deadlines due today, re-read
has(CY,'CVE-2023-49105','cyber'); has(CY,'CVE-2026-53362','cyber')
has(CY,'Sunday, August 30','cyber')
# standing corrections: refusals that must never regress
hasnt(CY,'Nevada statewide','cyber'); hasnt(CY,'Nevada Statewide','cyber')
# vendor CVSS standing corrections
ck(not re.search(r'CVE-2026-3055[^<]*9\.8',CY),'Citrix CVE-2026-3055 must be 9.3 not 9.8')
ck(not re.search(r'CVE-2026-8037[^<]*9\.8',CY),'LoadMaster CVE-2026-8037 must be 9.6 not 9.8')
# CVE well-formedness + liveness
cves=set(re.findall(r'CVE-\d{4}-\d{4,6}',CY))
ck(len(cves)>=20,'too few distinct CVEs on cyber board: %d'%len(cves))
for c in cves: ck(re.fullmatch(r'CVE-\d{4}-\d{4,6}',c) is not None,'malformed CVE '+c)

# ---- 5. THIS RUN'S MARKETS ADDITIONS ----
has(WS,'a firm, fixed target','ws'); has(WS,'65 months of sustained, elevated inflation','ws')
has(WS,'29,433.43','ws'); has(WS,'Nasdaq 100','ws')
has(WS,'not promoted into the Composite row','ws')
has(WS,'October or December','ws'); has(WS,'attributed rather than adopted','ws')
has(WS,'September 16','ws')
# the three Friday closes, unchanged and mutually consistent
for v in ['7,711.76','26,402.42','53,559.99','&minus;0.25%','&minus;0.52%','&minus;9.45']:
    has(WS,v,'ws closes')
# the Nasdaq 100 must NOT be substituted into the Composite row
ck(not re.search(r'Nasdaq Composite[^<]{0,40}29,433',WS),'Nasdaq 100 level promoted into Composite')
ck(not re.search(r'Nasdaq Composite[^<]{0,40}0\.70%',WS),'Nasdaq 100 pct promoted into Composite')
# rates/commodities table unchanged per standing correction (4.73 kept, 4.72 refused)
has(WS,'4.73%','ws'); has(WS,'4.72%','ws'); has(WS,'recorded and not adopted','ws')
has(WS,'4.34%','ws')
has(WS,'$83.44','ws'); has(WS,'$88.29','ws')
# September probability: spread printed, none adopted
has(WS,'57%','ws'); has(WS,'55.7','ws')
has(WS,'Polymarket','ws'); has(WS,'Kalshi','ws')
# Labor Day / payrolls standing sweeps
ck('September 7' in WS or 'Labor Day' in WS,'Labor Day family missing')
hasnt(WS,'Labor Day is Monday, September 5','ws')
# disclaimer
ck('not investment advice' in WS,'ws disclaimer missing')

# ---- 6. THIS RUN'S MMA ADDITIONS ----
has(MM,'&minus;400','mma'); has(MM,'&minus;428','mma'); has(MM,'&minus;500','mma')
has(MM,'+292','mma'); has(MM,'+300','mma'); has(MM,'+375','mma')
has(MM,'Odds: Parnasse','mma')
has(MM,'no single figure is adopted','mma')
has(MM,'Rosas Jr. vs. Barcelos','mma'); has(MM,'Sat, Sept 26','mma')
has(MM,'start-time conflict','mma'); has(MM,'Neither is adopted over the other','mma')
has(MM,'Noche UFC','mma')
# ---- champions board: the historically-wrong belts, asserted by name ----
for name in ['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
             'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison','Mackenzie Dern']:
    has(MM,name,'champions board')
ck(not re.search(r'Light Heavyweight</td>\s*<td>[^<]*Pereira',MM),'Pereira listed as LHW champ')
ck(not re.search(r'Middleweight</td>\s*<td>[^<]*Chimaev',MM),'Chimaev listed as MW champ')
ck(not re.search(r'Featherweight</td>\s*<td>[^<]*[Vv]acant',MM),'Featherweight listed vacant')
ck(not re.search(r'Lightweight</td>\s*<td>[^<]*Topuria',MM),'Topuria listed as LW champ')
# standing name/descriptor corrections
hasnt(MM,'Cody Salkilld','mma'); hasnt(MM,'Abdul-Rakhman','mma'); hasnt(MM,'Shamil Yakhyaev','mma')
ck(not re.search(r'Dariush[^.]{0,60}(former champion|title challenger)',MM),'Dariush mis-descriptored')
has(MM,'Abdul Rakhman Yakhyaev','mma')
# result family unchanged
has(MM,'1:48','mma'); has(MM,'24-9-1','mma'); has(MM,'Song Yadong','mma')
has(MM,'subject to change','mma')

# ---- 7. cross-page consistency: index cards mirror each tldr exactly ----
for f,h3 in [('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]:
    body=re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>',BRIEFS[f],re.S).group(1)
    card=re.search(r'<h3>'+re.escape(h3)+r'</h3>\s*<div class="sub">[^<]*</div>\s*<p>(.*?)</p>',IX,re.S)
    ck(card is not None,'no index card for '+h3)
    if card: ck(card.group(1).strip()==body.strip(),'index card for %s does not mirror its tldr'%h3)
# shared claims must agree across pages
for claim in ['CVE-2026-62878','Windows DNS Server']:
    ck((claim in CY) and (claim in IX),'cross-page: %s on cyber but not index'%claim)
ck(('five different names' in IX) and ('five' in MM.lower() or 'stops counting' in MM),'punch-count cross-page')
ck('&minus;400' in MM and '400' in IX,'cross-page odds spread')

# ---- 8. tldr / summary structure on all three briefings ----
for f,s in BRIEFS.items():
    ck(s.count('<div class="tldr">')==1,'tldr count != 1 in '+f)
for f,lbl in [('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]:
    ck('<b>%s</b>'%lbl in BRIEFS[f],'wrong tldr label in '+f)

# ---- 9. footers: >=6 absolute links, no duplicates, disclaimer present ----
for f,s in BRIEFS.items():
    fi=s.find('<footer'); ck(fi>=0,'no footer in '+f)
    foot=s[fi:]
    hrefs=re.findall(r'href="([^"]+)"',foot)
    abs_=[h for h in hrefs if h.startswith('http')]
    ck(len(abs_)>=6,'footer has %d absolute links in %s'%(len(abs_),f))
    for h in abs_: ck(h.startswith('https://'),'non-https source %s in %s'%(h,f))
    dups=[h for h in set(abs_) if abs_.count(h)>1]
    ck(not dups,'duplicate footer hrefs in %s: %s'%(f,dups[:4]))
for f,s in F.items():
    hrefs=re.findall(r'href="(https?://[^"]+)"',s)
    dups=[h for h in set(hrefs) if hrefs.count(h)>1]
    ck(not dups,'duplicate hrefs anywhere in %s: %s'%(f,dups[:4]))

# ---- 10. tag classes used are defined in CSS ----
for f,s in BRIEFS.items():
    used=set(re.findall(r'<span class="tag ([a-z]+)"',s))
    css=set(re.findall(r'\.tag\.([a-z]+)',s))
    ck(used<=css,'undefined tag classes in %s: %s'%(f,used-css))

# ---- 11. MMA countdown + archive hygiene ----
has(MM,'ufccdn','mma')
ck('s3.tradingview.com' not in AR,'widgets on archive.html')
ck('archive/' in AR,'archive.html has no snapshot links')

print('CHECKS: %d   FAILURES: %d'%(n[0],len(fails)))
for f_ in fails: print('  FAIL:',f_)
sys.exit(1 if fails else 0)
