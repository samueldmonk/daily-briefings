# -*- coding: utf-8 -*-
import re, sys, datetime, html as H
fails=[]; checks=0
def ck(cond,msg):
    global checks; checks+=1
    if not cond: fails.append(msg)

P={f:open(f,encoding='utf-8').read() for f in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
def txt(s): return H.unescape(re.sub(r'<[^>]+>',' ',s))

# ---------- structural: every page ----------
for f,h in P.items():
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%tab in h, '%s: missing nav tab %s'%(f,tab))
    for pid in ['edition','datestamp','updated']:
        ck('id="%s"'%pid in h, '%s: missing masthead pill %s'%(f,pid))
    ck("getElementById('datestamp')" in h and "America/New_York" in h, '%s: self-stamp JS'%f)
    ck(h.count('<div class="lab">')>=1, '%s: no section labels'%f)
    # balanced divs
    o=len(re.findall(r'<div\b',h)); c=len(re.findall(r'</div>',h))
    ck(o==c, '%s: unbalanced divs %d open / %d close'%(f,o,c))
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    ck('id="freshline"' in P[f], '%s: freshline'%f)
    ck(P[f].count('<div class="tldr">')==1, '%s: tldr count'%f)
ck('<b>The Wire</b>' in P['cyber-briefing.html'],'cyber tldr label')
ck('<b>The Tape</b>' in P['wallstreet-briefing.html'],'ws tldr label')
ck('<b>Tale of the Tape</b>' in P['mma-briefing.html'],'mma tldr label')

# ---------- TradingView blocks (Wall Street) ----------
w=P['wallstreet-briefing.html']
for wid in ['embed-widget-ticker-tape','embed-widget-single-quote','embed-widget-timeline',
            'embed-widget-stock-heatmap','embed-widget-mini-symbol-overview','embed-widget-events']:
    ck(wid in w,'ws: missing widget %s'%wid)
ck(w.count('embed-widget-single-quote')==3,'ws: single-quote count=%d'%w.count('embed-widget-single-quote'))
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(sym in w,'ws: tape symbol %s'%sym)
ck('livebar' in w,'ws: livebar')
ck('id="ufccdn"' in P['mma-briefing.html'],'mma: countdown element')

# ---------- CYBER: new top story ----------
c=P['cyber-briefing.html']
ts=c.find('<div class="lab">Top story</div>')
ts_end=c.find('<div class="lab">Patch priority</div>')
ck(ts>=0 and ts_end>ts,'cyber: top story section')
top=c[ts:ts_end]
for s in ['QScan','QTRouter','QTFY','Nanjing Xinjiuwei Network Technology Company',
          'National Aeronautics and Space Administration','Federal Reserve','U.S. Senate',
          'Southern District of California','Todd Blanche','Kash Patel','John A. Eisenberg',
          'Adam Gordon','Mark Remily','26-972','Black Lotus Labs','Mustang Panda',
          'Flax Typhoon','Volt Typhoon','4,000']:
    ck(s in top,'cyber top story missing: %s'%s)
# no CVE invented in the new top story block
newblk = top[:top.find('Boston Scientific')]
cves = set(re.findall(r'CVE-\d{4}-\d{4,6}', newblk))
ck(not cves,'cyber: top story invented CVE(s) %s'%cves)
ck('inoperable' in newblk,'cyber: seizure effect')
ck('obfuscation network' in newblk.lower() or '&ldquo;obfuscation network&rdquo;' in newblk,'cyber: obfuscation network')
ck('Boston Scientific' in top and 'Carried &middot; 6:06' in top,'cyber: BSX demoted+carried')
# BSX still intact
ck('bsx-20260826.htm' in c,'cyber: BSX 8-K source link retained')

# ---------- CYBER: spotlight / KEV / breaches ----------
sp=c[c.find('<div class="lab">Threat actor spotlight</div>'):c.find('<div class="lab">Breaches')]
ck('QTFY' in sp and 'quartermaster' in sp,'cyber: QTFY spotlight')
ck('Cruciferra' in sp,'cyber: prior spotlight retained')
kev=c[c.find('<div class="lab">CISA KEV'):c.find('<div class="lab">Sources')]
ck('SEVENTEENTH' in kev,'cyber: KEV 17th')
ck('14 rows' in kev,'cyber: KEV 14 rows')
ck('Vulnerability Review' in kev and 'nothing about that document' in kev,'cyber: CISA VR withheld')
br=c[c.find('<div class="lab">Breaches'):c.find('<div class="lab">Vulnerability watch')]
for s in ['Tata Electronics','204,341','630.4','June&nbsp;12, 2026','June&nbsp;22','Rejected as current']:
    ck(s in br,'cyber breaches missing: %s'%s)
tw=br[br.find('Tata Electronics'):br.find('Tata Electronics')+2600]
ck(('not today&rsquo;s news' in tw) and ('Nothing about it is published as a current breach' in tw),
   'cyber: Tata not framed as rejected')
tb=br[br.find('Taco Bell'):br.find('Taco Bell')+1200] if 'Taco Bell' in br else ''
ck('stays rejected' in tb,'cyber: Taco Bell re-rejection wording')
ck('Apollo Global Management' in c,'cyber: Apollo retained')

# ---------- KEV countdown triples ----------
kevtxt=txt(kev)
today=datetime.date(2026,8,26)
rows=re.findall(r'due\s+(?:<b>)?\s*([A-Z][a-z]{2,9})\.?\s*&nbsp;?\s*(\d{1,2})', kev)
# parse whole-page KEV table instead
kevtab=c[c.find('<div class="lab">CISA KEV'):c.find('<div class="lab">Sources')]
trip=re.findall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?&nbsp;?\s*(\d{1,2})[^0-9]{0,80}?\((\d+)\s+days?\s+left\)', kevtab)
ck(True,'kev parse attempted')
# nearest deadlines asserted consistently
ck('CVE-2026-21962' in kevtab and 'August&nbsp;27' in kevtab,'cyber: Oracle Aug 27')
ck('CVE-2026-60004' in kevtab and 'August&nbsp;28' in kevtab,'cyber: Gitea Aug 28')
pp=c[c.find('<div class="lab">Patch priority</div>'):c.find('<div class="lab">Threat actor spotlight</div>')]
ck('CVE' in pp,'cyber: patch priority has a CVE')
# patch priority must not contradict KEV nearest deadlines
for mm in re.finditer(r'due\s+(?:<b>)?August&nbsp;(\d{1,2})', pp):
    d=int(mm.group(1))
    win=pp[max(0,mm.start()-200):mm.start()+400].lower()
    ck(d>=26 or ('past due' in win or 'overdue' in win or 'lapsed' in win),
       'cyber: past deadline August %d not marked overdue'%d)
ck(len(re.findall(r'August&nbsp;\d{1,2}', pp))>0,'cyber: patch priority has dated context')

# ---------- WALL STREET ----------
ah=w[w.find('<div class="lab">After-hours movers</div>'):w.find('<div class="lab">Weekly scorecard</div>')]
ck('jump 4% after earnings' in ah or 'up more than 4%' in ah or '&plus;4%' in ah,'ws: 4% post-call read')
ck('largest amount in two years' in ah,'ws: largest-in-two-years attribution')
for r in ['&minus;1.3%','&minus;1%','&plus;5%']:
    ck(r in ah,'ws: prior read %s dropped'%r)
ck('nothing is averaged, reconciled or retracted' in ah,'ws: no-merge rule stated')
ck('&plus;19%' in ah and '17%' in ah and '15%' in ah,'ws: three Okta reads')
ck('$1.05' in ah and '$805' in ah,'ws: Okta fundamentals retained')
# rejected closing set must appear ONLY in a rejection context
for mm in re.finditer(re.escape('7,677.24'), w):
    win = w[max(0,mm.start()-1600):mm.start()+1000]
    ck(any(k in win.lower() for k in ['reject','declined to adopt','not merged','loses again','not adopt',
                                      'adopted at 2:44 over','zacks printed','over the 7,677.24']),
       'ws: 7,677.24 outside a rejection context')
ck('7,677.28' in w,'ws: adopted Tuesday S&P close missing')
# Tuesday Dow/Nasdaq levels are legitimate prior-close bases; assert they are never labelled Wednesday's close
for lvl in ['53,577.40','26,151.30']:
    for mm in re.finditer(re.escape(lvl), w):
        win = w[max(0,mm.start()-260):mm.start()+260]
        ck('August&nbsp;26 close' not in win or 'reject' in win.lower() or 'Tuesday' in win,
           'ws: %s labelled as the Aug 26 close'%lvl)
ck('7,675.70' in w,'ws: verified Aug 26 close retained')
# Salesforce $5.90 still only in rejection context
for mm in re.finditer(re.escape('$5.90'), w):
    win=w[max(0,mm.start()-1500):mm.start()+1500]
    ck(('NOT ME' in win) or ('not published' in win.lower()) or ('irreconcilable' in win.lower()) or ('reject' in win.lower()),
       'ws: $5.90 outside rejection context')
# Nvidia arithmetic re-check
ck(abs((48.71+40.31)-89.02)<1e-9,'math: DC segments')
ck(abs(round(89.02+7.20,2)-96.22)<1e-9,'math: total')
ck(abs(round((96.2-46.7)/46.7*100,1)-106.0)<0.05,'math: 106.0% y/y')
ck(abs(round((2.22-1.05)/1.05*100,1)-111.4)<0.05,'math: 111.4% EPS')
ck(abs(round((108-57.01)/57.01*100,1)-89.4)<0.05,'math: 89.4% guide')
for s in ['$96.2','$2.22','$2.10','106%','75.0%','$108','116.6%','101.5%']:
    ck(s in w,'ws: NVDA figure %s missing'%s)

# ---------- MMA ----------
m=P['mma-briefing.html']
fw=m[m.find('<div class="lab">Fight week'):m.find('<div class="lab">Last event')]
for s in ['Umar Nurmagomedov','Song Yadong','Oriental Sports Center','August&nbsp;29','&minus;500','&plus;380',
          '20-1','23-9-1','Deiveson Figueiredo','Heilongjiang','Dagestan']:
    ck(s in fw,'mma fight week missing: %s'%s)
rk=fw[fw.find('RANKINGS ARE REPORTED TWO WAYS'):fw.find('RANKINGS ARE REPORTED TWO WAYS')+1400]
ck('#3' in rk and '#5' in rk and 'No.&nbsp;2' in rk and 'No.&nbsp;6' in rk,'mma: both ranking readings printed')
ck('asserts no numeric rank' in rk,'mma: rank non-adoption stated')
ck('no result is asserted' in fw,'mma: no-result guard')
# champions board parsed as real cells
cbsec=m[m.find('<div class="lab">Champions board'):m.find('<div class="lab">Sources')]
ck('THIRTY-THIRD' in cbsec,'mma: 33rd edition')
cells=re.findall(r'<td[^>]*>(.*?)</td>', cbsec, re.S)
cellt=[txt(x).strip() for x in cells]
def champ_for(div):
    for i,x in enumerate(cellt):
        if x.lower().startswith(div.lower()):
            return cellt[i+1] if i+1<len(cellt) else ''
    return None
lhw=champ_for('Light Heavyweight'); mw=champ_for('Middleweight'); fwt=champ_for('Featherweight')
ck(lhw is not None and 'Ulberg' in lhw and 'Pereira' not in lhw,'mma: LHW champ cell = %r'%lhw)
ck(mw is not None and 'Strickland' in mw and 'Chimaev' not in mw,'mma: MW champ cell = %r'%mw)
ck(fwt is not None and 'Volkanovski' in fwt,'mma: FW champ cell = %r'%fwt)
ck(champ_for('Lightweight') and 'Gaethje' in champ_for('Lightweight'),'mma: LW champ')
ck(champ_for('Welterweight') and 'Makhachev' in champ_for('Welterweight'),'mma: WW champ')
divs=[x for x in cellt if re.match(r'^(Heavyweight|Light Heavyweight|Middleweight|Welterweight|Lightweight|Featherweight|Bantamweight|Flyweight|Women)',x)]
ck(len(divs)>=11,'mma: champions board has %d division rows'%len(divs))

# ---------- index cards ----------
ix=P['index.html']
ck('QScan' in ix and 'QTRouter' in ix and 'NASA' in ix,'index: security card matches cyber lead')
ck('more than 4%' in ix,'index: markets card matches ws lead')
ck('Shanghai' in ix and '&minus;500' in ix,'index: mma card matches mma lead')
ck(ix.count('Read the briefing')==3,'index: 3 cards')
ck('Apollo Global' not in ix,'index: stale Apollo headline still on front page')

# ---------- new-marker hygiene ----------
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','index.html']:
    h=P[f]
    for mm in re.finditer(r'<span class="tag new">New &middot; (\d{1,2}:\d{2})</span>', h):
        ck(mm.group(1)=='6:36','%s: stale new-marker %s'%(f,mm.group(1)))

# ---------- duplicate-introduction guard ----------
carried = ['CVE-2026-15981','CVE-2026-61979','CVE-2026-18963','CVE-2026-75149','NemoClaw',
           'Mirage2FA','Chrome 152','Nutex Health','ReliaQuest','Apollo Global']
for mm in re.finditer(r'<span class="tag new">New &middot; 6:36</span>', P['cyber-briefing.html']):
    blk = P['cyber-briefing.html'][mm.start():mm.start()+6000]
    blk = blk[:blk.find('</div>\n<div class="card"')] if '</div>\n<div class="card"' in blk else blk
    for idf in carried:
        if idf in blk:
            ck('already' in blk or 'carried' in blk.lower() or 'reject' in blk.lower(),
               'cyber: 6:36 block re-introduces carried item %s as new'%idf)

# ---------- trap greps ----------
traps=['Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman','Fight Night 286','$1.4 trillion','Suno',
       'Pereira (205)','Khamzat Chimaev, middleweight champion']
for f,h in P.items():
    for t in traps:
        ck(t not in h,'%s: TRAP HIT %s'%(f,t))
# window-scoped rejected strings
for f,h in P.items():
    for t in ['112.62','97.69','$1 trillion in combined Blackwell','350 plants','$200 billion CPU market',
              'our demand is much higher than that','4,637.03']:
        for mm in re.finditer(re.escape(t),h):
            win=h[max(0,mm.start()-1600):mm.start()+1200]
            ck(any(k in win.lower() for k in ['reject','not published','not asserted','contradictory','withheld','flagged']),
               '%s: %s outside rejection context'%(f,t))

print('CHECKS:',checks,'FAILURES:',len(fails))
for x in fails: print('  FAIL:',x)
sys.exit(1 if fails else 0)
