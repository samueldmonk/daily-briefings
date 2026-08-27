# -*- coding: utf-8 -*-
import re,sys,datetime
D='/tmp/db_1787854887/'
F={f:open(D+f,encoding='utf-8').read() for f in ('index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html')}
fails=[]; checks=0
def ck(cond,msg):
    global checks; checks+=1
    if not cond: fails.append(msg)
def has(f,t,msg=None): ck(t in F[f], msg or "%s missing: %s"%(f,t[:70]))
def nohas(f,t,msg=None): ck(t not in F[f], msg or "%s must NOT contain: %s"%(f,t[:70]))

# ---- 1. structural: five-tab nav, masthead ids, tldr, freshline, self-stamp ----
for f in F:
    for tab in ('index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html'):
        has(f,'href="%s"'%tab)
    for i in ('id="edition"','id="datestamp"','id="updated"','id="freshline"'):
        has(f,i)
    has(f,"America/New_York")
    has(f,"briefings refresh every 30 minutes")
for f in ('cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html'):
    has(f,'<div class="tldr">')
ck('<div class="tldr">' not in F['index.html'],"index must not carry a tldr strip")

# ---- 2. TradingView widget blocks (WS) ----
w=F['wallstreet-briefing.html']
for wid in ('ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events'):
    ck('embed-widget-%s.js'%wid in w,"WS missing widget %s"%wid)
for sym in ('FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y'):
    ck(sym in w,"WS ticker tape missing %s"%sym)
ck(w.count('embed-widget-single-quote.js')==3,"WS needs exactly 3 single-quote widgets")
ck('"symbol":"NASDAQ:OKTA"' in w,"Chart of the Day symbol must be OKTA")
for f in ('index.html','cyber-briefing.html','mma-briefing.html'):
    ck('tradingview' not in F[f].lower(),"%s must carry no live widgets"%f)

# ---- 3. EDITION-STAMP FRESHNESS GUARD ----
for f in ('cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html'):
    for m in re.finditer(r'<span class="tag new">([^<]*)</span>',F[f]):
        t=m.group(1)
        ck('2:21' in t, "%s: 'new' tag not stamped 2:21 -> %r"%(f,t))
    ck('<span class="tag new">New</span>' not in F[f], "%s: bare unstamped New tag"%f)
    ck('12:38</span>' not in F[f].replace('Carried · 12:38</span>','').replace('Carried &middot; 12:38</span>',''),
       "%s: a 12:38 tag survived un-demoted"%f)

# ---- 4. index cards byte-identical to each page's tldr ----
def tldr(f):
    return re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>',F[f],re.S).group(1).strip()
for f in ('cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html'):
    ck('<p>'+tldr(f)+'</p>' in F['index.html'], "index card not byte-identical to %s tldr"%f)

# ---- 5. MARKETS: this run's verified figures present; retired ones gone from index ----
for t in ('up 0.4%','up 0.8%','up 1.5%','1:25 p.m. in New York','Okta up 17.4%','Salesforce up 10.4%',
          'Nvidia up 9%','CrowdStrike up 9%','6.5%','$82.86','$87.65','203,000','3.7%','0.2% on the month'):
    has('wallstreet-briefing.html',t)
# the ladders must survive, not be overwritten
for t in ('+169.90','+217.20','+147.67','+208.48','+300.97','+327.22','+279.61','+400.29',
          '26.17%','19%','21.04%','17.93%','9.48%','14.78%','11.2%','5.87%'):
    has('wallstreet-briefing.html',t)
nohas('index.html','400.29',"index still carries the retired 12:38 Nasdaq point figure")
nohas('index.html','208.48',"index still carries the retired 12:38 Dow point figure")
# the false 'no source stamped a time' claim must be struck
ck('<b>No source stamped its figures with a time</b>' not in w,"the falsified no-timestamp claim survives")
has('wallstreet-briefing.html','Struck at 2:21')
# arithmetic guard: 'Four point-and-percent index reads' must be followed by exactly four Dow reads
seg=w[w.index('Four point-and-percent index reads'):]
seg=seg[:seg.index('</p>')]
ck(sum(seg.count(x) for x in ('+169.90','+217.20','+147.67','+208.48'))==4,"ladder count word does not match its list")
# window-scoped rejections: figures that must ONLY appear inside a rejection note
for fig,scope in (('7,673.04','rejected'),('6,279','2025 levels'),('$3.97 trillion','2025 levels'),
                  ('232,000','rejected'),('1.82%','withheld')):
    ck(w.count(fig)>=1,"rejection-scoped figure vanished (guard is dead): %s"%fig)
ck('Energy declined 1.82%' in w and 'It is withheld again' in w,"1.82% not scoped to its rejection")
ck('A number does not become sourced by being offered three times' in w,"third-rejection rule missing")
# INVERTED Jackson Hole guard — must be PUBLISHED
ck('Jackson Hole' in w,"Jackson Hole must be published, not removed")
ck('August 27&ndash;29' in w or 'August 27–29' in w,"Jackson Hole dates missing")
ck('That reasoning was wrong.' in w,"Jackson Hole correction sentence missing")
ck('Friday, August 28' in w,"Warsh keynote date missing")
# rates
for t in ('4.64','4.22%','5.25%','3.50%–3.75%'): has('wallstreet-briefing.html',t)
ck('Nothing here is investment advice' in w,"WS disclaimer missing")

# ---- 6. CYBER ----
c=F['cyber-briefing.html']
CVE_OK={'CVE-2026-21962','CVE-2026-8452','CVE-2019-1068','CVE-2015-3246','CVE-2015-5287','CVE-2021-23758',
 'CVE-2022-0995','CVE-2026-19490','CVE-2026-64633','CVE-2026-65641','CVE-2026-18963','CVE-2026-19912',
 'CVE-2026-19913','CVE-2026-62815','CVE-2026-62893','CVE-2026-45659','CVE-2026-58231',
 'CVE-2026-12569','CVE-2026-20349','CVE-2026-33824','CVE-2026-55040','CVE-2026-59310','CVE-2026-60004',
 'CVE-2026-65400','CVE-2026-68820','CVE-2026-69836','CVE-2026-72529','CVE-2026-72530','CVE-2026-72898',
 'CVE-2026-73570','CVE-2026-8037'}
found=set(re.findall(r'CVE-\d{4}-\d{4,6}',c))
ck(len(found)>=12,"CVE liveness: only %d ids found"%len(found))
for cid in sorted(found):
    ck(cid in CVE_OK,"unlisted CVE id on cyber page: %s"%cid)
# Aug 29 deadline consistency in >=4 places
ck(c.count('Aug 29')+c.count('August 29')>=4,"Aug 29 deadline not repeated in >=4 places")
ck('September 9' in c or 'Sept 9' in c,"Sept 9 tail deadline missing")
for t in ('Amazon Kiro','prompt injection','471.2M','CVE-2026-45659','CVE-2026-58231','Threat level'):
    has('cyber-briefing.html',t)
# no CVSS may be invented for the two new CVEs
for cid in ('CVE-2026-45659','CVE-2026-58231'):
    row=c[c.index(cid):]; row=row[:row.index('</tr>')]
    ck('Not confirmed this run' in row,"%s must not carry a borrowed CVSS"%cid)
ck('countdown' in c.lower() or 'days left' in c.lower(),"KEV countdown missing")
ck('BOD 26-04' in c,"risk-based BOD reference missing")
ck('BOD 22-01' not in c,"stale three-week BOD 22-01 heuristic present")

# ---- 7. MMA: champions board regressions ----
m=F['mma-briefing.html']
rows=re.findall(r'<tr>(.*?)</tr>',m[m.index('Champions Board'):],re.S)
cells=[re.findall(r'<td[^>]*>(.*?)</td>',r,re.S) for r in rows]
cells=[r for r in cells if len(r)>=2]
ck(len(cells)>=11,"champions board liveness: only %d rows"%len(cells))
champ_col=' '.join(re.sub('<[^>]+>','',r[1]) for r in cells)
for bad in ('Pereira','Chimaev','vacant','Topuria'):
    ck(bad.lower() not in champ_col.lower(),"CHAMPION REGRESSION: %s in a champion cell"%bad)
for good in ('Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Van','Shevchenko','Harrison','Dern'):
    ck(good in champ_col,"champion missing from board: %s"%good)
# trap greps
for trap in ('Shamil Yakhyaev','Cody Salkilld','Abdul-Rakhman'):
    nohas('mma-briefing.html',trap,"TRAP: %s"%trap)
for t in ('Desert Diamond Arena','Glendale','UFC Fight Night 288','withdrew','Balletto','UFC debut at UFC Shanghai'):
    has('mma-briefing.html',t)
ck('ufccdn' in m,"MMA countdown element missing")
ck('subject to change' in m,"MMA disclaimer missing")
# chronology: nothing 'upcoming' that has passed
ck('SAT AUG 29' in m,"next card line missing")

print("CHECKS: %d   FAILURES: %d"%(checks,len(fails)))
for f in fails: print("  FAIL:",f)
sys.exit(1 if fails else 0)
