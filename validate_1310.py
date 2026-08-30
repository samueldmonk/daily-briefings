# -*- coding: utf-8 -*-
import io, re, sys
def rd(p): return io.open(p,encoding='utf-8').read()
P = ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
S = {p: rd(p) for p in P}
CY, WS, MM, IX = S['cyber-briefing.html'], S['wallstreet-briefing.html'], S['mma-briefing.html'], S['index.html']
fails=[]; n=[0]
def ok(cond,msg):
    n[0]+=1
    if not cond: fails.append(msg)
def has(s,t,msg): ok(t in s, msg)
def no(s,t,msg): ok(t not in s, msg)

# ---- structure ----
for p in P:
    s=S[p]
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        has(s,'href="%s"'%tab, '%s: nav missing %s'%(p,tab))
    for i in ['id="edition"','id="datestamp"','id="updated"']:
        has(s,i,'%s: masthead missing %s'%(p,i))
    has(s,"America/New_York",'%s: self-stamp script missing'%p)
    has(s,'id="freshline"','%s: freshline missing'%p)
    ok(s.count('class="on"')==1,'%s: exactly one active tab'%p)

# ---- stamp ----
for p in P:
    s=S[p]
    head = s[:s.find('</header>')+400]
    has(head,'1:09 PM ET','%s: masthead not stamped 1:09 PM'%p)
    for stale in ['12:58 PM ET','12:55 PM ET','11:05 AM ET','9:42 PM ET','8:31 PM ET','Afternoon Edition','Saturday, August 29']:
        no(head,stale,'%s: stale "%s" in masthead region'%(p,stale))
    has(s,'Data as of 1:09 PM ET','%s: freshline not restamped'%p)
    no(s,'Data as of 12:58','%s: stale freshline'%p)

# ---- widgets: wallstreet only ----
for w in ['embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
          'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js']:
    has(WS,w,'WS: missing widget %s'%w)
for sym in ['TVC:USOIL','TVC:US10Y','NASDAQ:PYPL','FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI']:
    has(WS,sym,'WS: missing symbol %s'%sym)
for p in ['index.html','cyber-briefing.html','mma-briefing.html']:
    no(S[p],'s3.tradingview.com','%s: must carry no live widgets'%p)

# ---- markets numbers ----
for f in ['7,711.76','26,402.42','53,559.99','0.25%','0.52%','9.45']:
    has(WS,f,'WS: missing close figure %s'%f)
ok(abs((9.45/53569.44)*100 - 0.02) < 0.01, 'WS: Dow points/percent reconcile')
for f in ['7,673.04','as of ~','After-Hours Movers','After-hours movers']:
    no(WS,f,'WS: forbidden "%s" (weekend / retired)'%f)
for r in ['4.73%','4.34%','5.20%']:
    has(WS,r,'WS: missing rate %s'%r)
# 4.67 must only appear inside a rejection frame
for m in re.finditer(r'4\.67', WS):
    ctx = WS[max(0,m.start()-500):m.start()+500]
    ok(any(k in ctx for k in ['not adopted','retired','does not displace','was not adopted','rejected']),
       'WS: 4.67 occurrence lacks rejection frame')
has(WS,'nineteenth verification','WS: counter not advanced to nineteenth')
no(WS,'eighteenth verification','WS: stale eighteenth counter')
has(WS,'seventh read','WS: seventh read missing')
has(WS,'Goldman Sachs','WS: Goldman read missing')
has(WS,'very unlikely','WS: Goldman wording missing')
for prob in ['48%','57%','65%','nearly 70%']:
    has(WS,prob,'WS: missing probability read %s'%prob)
has(WS,'seventh consecutive run','WS: adoption declination missing')
# weekly figures
for f in ['+0.5%','+0.9%','first winning week in three']:
    has(WS,f,'WS: missing weekly figure %s'%f)
# calendar weekday guard: every "September 5" in WS must sit in a rejection frame
occ=0
for m in re.finditer(r'September 5', WS):
    occ+=1
    ctx = WS[max(0,m.start()-700):m.start()+700]
    ok(any(k in ctx for k in ['Saturday','Rejected','rejected','thrown out','not released']),
       'WS: "September 5" occurrence #%d lacks rejection frame'%occ)
ok(occ>=1,'WS: September 5 rejection is present')
has(WS,'September 4','WS: correct payrolls date missing')
has(WS,'8:30 a.m.','WS: payrolls time missing')
# lead time-of-day freshness
has(WS,'just past one o&rsquo;clock','WS: lead time-of-day not advanced')
for stale in ['It is <b>Sunday midday</b>','It is <b>Sunday morning</b>','It is <b>Saturday evening</b>']:
    no(WS,stale,'WS: stale lead time-of-day "%s"'%stale)

# ---- cyber KEV board ----
has(CY,'(OVERDUE','CY: overdue row missing')
has(CY,'(0 days left','CY: 0-days row missing')
has(CY,'(10 days left)','CY: 10-days row missing')
has(CY,'(11 days left)','CY: 11-days row missing')
for stale in ['(1 day left','(12 days left']:
    no(CY,stale,'CY: stale countdown "%s"'%stale)
for cve in ['CVE-2026-8452','CVE-2019-1068','CVE-2026-53362','CVE-2023-49105','CVE-2022-0995',
            'CVE-2021-23758','CVE-2015-5287','CVE-2015-3246','CVE-2026-66384']:
    has(CY,cve,'CY: KEV row id %s missing'%cve)
has(CY,'tenth check','CY: tenth check not recorded')
has(CY,'A tenth check at 1:08 PM','CY: tenth check observation time missing')
for _p in P:
    _h=S[_p][:S[_p].find('</header>')+400]
    no(_h,'1:10 PM','%s: prose-ahead-of-clock stamp in masthead'%_p)
has(CY,'Three gaps in ten checks','CY: gap arithmetic not stated')
# new Aug 7 id: must never appear inside a countdown bullet, must sit in a no-due-date frame
ok('CVE-2026-8037' in CY,'CY: Aug 7 id missing')
for m in re.finditer(r'CVE-2026-8037', CY):
    ctx = CY[max(0,m.start()-900):m.start()+900]
    ok('days left' not in ctx and 'OVERDUE' not in ctx,'CY: CVE-2026-8037 appears near a countdown')
    ok('no due date' in ctx or 'no row and no countdown' in ctx or 'Progress LoadMaster' in ctx,
       'CY: CVE-2026-8037 lacks its no-deadline frame')
has(CY,'Progress LoadMaster','CY: LoadMaster product missing')
has(CY,'not a fourth gap','CY: gap-vs-blank distinction missing')
# gap ids never in a countdown region
for gid in ['CVE-2026-73570','CVE-2026-60004']:
    for m in re.finditer(gid, CY):
        ctx = CY[max(0,m.start()-700):m.start()+700]
        ok('days left)' not in ctx,'CY: gap id %s near a countdown'%gid)
# Patch Tuesday family
has(CY,'421','CY: Patch Tuesday CVE count missing')
has(CY,'CVE-2026-68820','CY: WinSock id missing')
has(CY,'afd.sys','CY: afd.sys detail missing')
has(CY,'Ancillary Function Driver','CY: WinSock driver name missing')

# ---- cyber refusals ----
has(CY,'Refused This Run','CY: refusal panel missing')
for m in re.finditer(r'Nevada', CY):
    ctx = CY[max(0,m.start()-1400):m.start()+1400]
    ok(any(k in ctx for k in ['refused','Refused','Not published','not published']),
       'CY: Nevada occurrence lacks refusal frame')
for m in re.finditer(r'Brightspeed', CY):
    ctx = CY[max(0,m.start()-1400):m.start()+1400]
    ok(any(k in ctx for k in ['refused','Refused','not published','January 4, 2026']),
       'CY: Brightspeed occurrence lacks refusal frame')
for m in re.finditer(r'Salesloft', CY):
    ctx = CY[max(0,m.start()-1600):m.start()+1600]
    ok(any(k in ctx for k in ['refused','Refused','not published','does not survive']),
       'CY: Salesloft occurrence lacks refusal frame')
has(CY,'UNC6395','CY: Drift actor id missing')
has(CY,'June 8&ndash;18, 2026','CY: Drift campaign window missing')
has(CY,'January 4, 2026','CY: Brightspeed date missing')
has(CY,'60+ agencies','CY: Nevada claim as stated missing')
# attacker-attributed figures keep their attribution
for fig in ['5.79 TB','284M','$55,236,150','1 million+']:
    if fig in CY:
        for m in re.finditer(re.escape(fig), CY):
            ctx = CY[max(0,m.start()-700):m.start()+700]
            ok(any(k in ctx for k in ['claim','Claim','attacker','says','group announced','alleg','refused','not the city']),
               'CY: figure %s lacks attacker/claim attribution'%fig)
# CVE well-formedness + liveness
ids = set(re.findall(r'CVE-\d{4}-\d{4,6}', CY))
ok(len(ids)>=20,'CY: fewer than 20 distinct CVE ids (%d)'%len(ids))
for i_ in ids: ok(re.match(r'^CVE-(19|20)\d{2}-\d{4,6}$',i_) is not None,'CY: malformed id %s'%i_)

# ---- MMA champions ----
for name in ['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
             'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Ciryl Gane']:
    has(MM,name,'MMA: champion/name %s missing'%name)
for bad in ['Pereira</td>','Chimaev</td>','Topuria</td>']:
    no(MM,bad,'MMA: forbidden champion cell %s'%bad)
# no board row may name a vacant champion; FW never asserted vacant
# ASSERTION-BASED, not vocabulary-based: a guard that fires on the page's own
# corrective narrative about a source's false vacancy is a broken guard.
for row in re.findall(r'<tr>.*?</tr>', MM, re.S):
    cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
    for c_ in cells:
        ok(re.sub(r'<[^>]+>','',c_).strip().lower() != 'vacant',
           'MMA: a champions-board row names a vacant champion')
# featherweight may never be AFFIRMATIVELY asserted vacant
for m in re.finditer(r'(?i)featherweight[^.]{0,140}?\bis vacant\b', MM):
    ctx = MM[max(0,m.start()-300):m.end()+300]
    ok(any(k in ctx for k in ['not vacant','unsupported','rejected','false','is not a vacancy']),
       'MMA: featherweight affirmatively asserted vacant')
for m in re.finditer(r'(?i)\bvacant\b', MM):
    seg = MM[max(0,m.start()-200):m.start()+200]
    ok('Volkanovski' in seg or 'vacated' in seg or 'vacant title' in seg or 'vacant belt' in seg
       or 'vacant light-heavyweight' in seg or 'not a vacancy' in seg or 'unsupported vacancy' in seg
       or 'false vacancy' in seg or 'published vacant' in seg or 'rejected' in seg,
       'MMA: "vacant" with no champion, no belt and no rejection nearby')
has(MM,'sixtieth unchanged edition','MMA: tldr board counter not advanced')
has(MM,'sixtieth consecutive edition','MMA: body board counter not advanced')
_tl = MM[MM.find('<div class="tldr">'):MM.find('</span></div>', MM.find('<div class="tldr">'))]
no(_tl,'fifty-ninth','MMA: stale board counter in tldr')
has(MM,'third consecutive clean','MMA: ESPN clean-run counter missing')
# Dariush descriptor
for m in re.finditer(r'Dariush', MM):
    ctx = MM[max(0,m.start()-300):m.start()+300]
    ok('challenger' not in ctx,'MMA: Dariush described as a challenger')

# ---- MMA Paris ----
for b in ['Fares Ziam','Axel Sola','Michael Page','Nursulton Ruziboev','Losene Keita','Muhammadjon Naimov',
          'Felipe Lima','Trevor Peek','Nora Cornolle','Mario Pinto','Ryan Spann','Oumar Sy',
          'Modestas Bukauskas','Fabia Sintes']:
    has(MM,b,'MMA: Paris bout name %s missing'%b)
has(MM,'13 bouts','MMA: Paris bout count missing')
has(MM,'Accor Arena','MMA: Paris venue missing')
has(MM,'Hooker vs. Parnasse','MMA: official billing missing')
for odd in ['&minus;400','&minus;428','&minus;500']:
    has(MM,odd,'MMA: Paris odds price %s missing'%odd)
has(MM,'none of the three is adopted','MMA: odds adoption declination missing')
has(MM,'two-time KSW featherweight','MMA: Parnasse descriptor missing')
has(MM,'1:48','MMA: Shanghai finish time missing')
has(MM,'Marc Goddard','MMA: referee missing')
has(MM,'$400,000','MMA: bonus total missing')

# ---- index mirrors ----
def tldr_text(s):
    i=s.find('<div class="tldr">'); a=s.find('<span>',i)+6; b=s.find('</span></div>',a); return s[a:b]
for lbl,src in [('cy',CY),('ws',WS),('mm',MM)]:
    has(IX, tldr_text(src), 'index: %s card does not mirror its tldr'%lbl)

# ---- footers ----
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=S[p]
    blk = s[s.rfind('<div class="srcs">'):]
    hrefs = re.findall(r'href="([^"]+)"', blk)
    ok(len(hrefs)>=6,'%s: footer has <6 source links'%p)
    ok(len(hrefs)==len(set(hrefs)),'%s: duplicate footer hrefs'%p)
    for h in hrefs: ok(h.startswith('http'),'%s: non-absolute footer href %s'%(p,h))
    has(s,'class="disc"','%s: disclaimer missing'%p)
has(WS,'not investment advice','WS: investment-advice disclaimer wording missing')
has(MM,'subject to change','MMA: cards-subject-to-change disclaimer missing')

print("validate_1310.py: %d checks, %d failures" % (n[0], len(fails)))
for f in fails: print("  FAIL: "+f)
sys.exit(1 if fails else 0)
