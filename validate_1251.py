# -*- coding: utf-8 -*-
import re, io, sys
FAIL=[]; N=0
def chk(cond,msg):
    global N; N+=1
    if not cond: FAIL.append(msg)
P={f:io.open(f,encoding='utf-8').read() for f in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}

# --- structural guards on every page ---
for f,s in P.items():
    chk('id="freshline"' in s, f+': freshline missing')
    chk('Data as of 12:51 PM ET' in s, f+': stale freshline stamp')
    chk(s.count('<a href="archive.html"')>=1, f+': archive tab missing')
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
        chk('href="%s"'%t in s, '%s: nav missing %s'%(f,t))
    chk('id="edition"' in s and 'id="datestamp"' in s and 'id="updated"' in s, f+': masthead pills missing')
    chk("America/New_York" in s, f+': self-stamp JS missing')
    # empty section headings
    chk(re.search(r'<h2 class="sec">\s*<div',s) is None, f+': empty section heading')
    chk(re.search(r'<h2 class="sec">\s*</h2>',s) is None, f+': blank section heading')
    # no stale New tags from previous runs
    chk('tag new">New &middot; 12:24 PM' not in s, f+': undemoted 12:24 New tag')
    chk('tag new">New &middot; 11:50' not in s, f+': undemoted 11:50 New tag')
    # tag hygiene: no bare clock "Carried · from the" without a day
    chk(re.search(r'Carried &middot; from the \d',s) is None, f+': bare-clock carried tag')

# --- three briefings: summary strip ---
for f,label in [('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]:
    s=P[f]
    chk('<div class="tldr">' in s, f+': tldr missing')
    chk('<b>%s</b>'%label in s, f+': wrong tldr label')
    chk(s.count('<div class="tldr">')==1, f+': duplicate tldr')

# --- WALL STREET ---
ws=P['wallstreet-briefing.html']
chk('Chart of the Day &mdash; Edison International (NYSE:EIX)' in ws,'ws: chart heading not fixed')
# symbol/caption agreement guard (owed to CORRECTIONS.md)
m=re.search(r'<h2 class="sec">Chart of the Day &mdash; [^(]*\((\w+:\w+)\)</h2>',ws)
chk(m is not None,'ws: chart heading has no symbol')
if m:
    sym=m.group(1)
    w=re.search(r'mini-symbol-overview\.js[^{]*\{"symbol":"([^"]+)"',ws)
    chk(w is not None and w.group(1)==sym,'ws: chart heading symbol %s != widget symbol %s'%(sym, w.group(1) if w else None))
chk('PG&amp;E (NYSE:PCG)</h2>' not in ws,'ws: old chart heading survives')
# live widget blocks A-F
for blk in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']:
    chk('embed-widget-%s.js'%blk in ws,'ws: widget block %s missing'%blk)
chk(ws.count('embed-widget-single-quote.js')==3,'ws: need 3 single-quote widgets')
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    chk(sym in ws,'ws: ticker tape missing '+sym)
# refusal adjacency: the refused levels must sit beside an explicit refusal
for lvl in ['7,711.76','26,402.42']:
    for mm in re.finditer(re.escape(lvl),ws):
        w=ws[max(0,mm.start()-1400):mm.start()+1400]
        chk(('has not closed' in w) or ('Refused' in w) or ('refused' in w) or ('Weekly Scorecard' in w) or ("Friday" in w),
            'ws: %s printed without refusal/close context'%lvl)
chk('53,885.10' not in ws or 'has not closed' in ws,'ws: phantom Dow level without refusal')
# XLK contradiction must be stated as the refusal
chk('XLK' in ws and 'weak on AI stocks' in ws or 'weak performance by AI stocks' in ws,'ws: XLK contradiction not stated')
i=ws.find('XLK'); chk(i>0 and 'Refused' in ws[max(0,i-2500):i+2500],'ws: XLK figure not adjacent to a refusal')
# PayPal must never be asserted as today
_srcstart=ws.find('Sources checked this run')
for mm in re.finditer(r'PayPal',ws):
    if _srcstart>0 and mm.start()>_srcstart-200: continue      # link labels in the sources footer are not assertions
    if '</a>' in ws[mm.start():mm.start()+120] and '<a ' in ws[max(0,mm.start()-400):mm.start()]: continue
    w=ws[max(0,mm.start()-1500):mm.start()+1500]
    chk(('Friday' in w) or ('refus' in w.lower()),'ws: PayPal move without Friday/refusal context')
# 4.705% must be refused on date
if '4.705' in ws:
    i=ws.find('4.705'); w=ws[max(0,i-1200):i+1200]
    chk('August 10' in w and ('refused' in w.lower()),'ws: 4.705% not refused on date')
# both Chevron renderings printed
chk('+2.84%' in ws and '+1.86%' in ws,'ws: both Chevron renderings required')
# both EIX/PCG rendering families printed
for v in ['&minus;22.3%','more than 22%','&minus;21.0%']: chk(v in ws,'ws: missing EIX rendering '+v)
for v in ['&minus;16.7%','around 19%','&minus;20.0%']: chk(v in ws,'ws: missing PCG rendering '+v)
# both WTI renderings recorded, neither in the table
chk('$80 a barrel' in ws and 'near $86' in ws,'ws: both WTI renderings required')
# Weekly Scorecard purity: no intraday level inside the scorecard section
i=ws.find('<h2 class="sec">Weekly Scorecard')
j=ws.find('<h2',i+10)
sec=ws[i:j] if i>=0 and j>i else ''
chk(i>=0,'ws: Weekly Scorecard missing')
chk('7,678.68' not in sec,'ws: intraday level leaked into Weekly Scorecard')
chk('53,885.10' not in sec,'ws: phantom level leaked into Weekly Scorecard')
# seventh rendering family printed in full
for v in ['&minus;0.43%','&minus;0.45%','&minus;0.47%','&minus;0.5%','&minus;0.55%']:
    chk(v in ws,'ws: missing S&P rendering '+v)
chk('none is adopted' in ws or 'not adopted' in ws,'ws: adoption disclaimer missing')
chk('not investment advice' in ws.lower() or 'information only' in ws.lower(),'ws: disclaimer missing')

# --- CYBER ---
cy=P['cyber-briefing.html']
chk('Patch Priority' in cy and 'CVE-2026-8452' in cy,'cy: patch priority CVE missing')
# KEV deadline consistency: added Aug 26 / due Aug 29 everywhere 8452 appears with a date
chk('added it to the Known Exploited' in cy or 'August 26' in cy,'cy: KEV add date missing')
chk('August 29' in cy,'cy: KEV due date missing')
chk('September 9' in cy and 'September 10' in cy,'cy: pending deadlines missing')
chk('August 31, 2026' in cy,'cy: countdown baseline missing')
# never assert a same-week/today deadline for a past date
for mm in re.finditer(r'due TODAY, Sunday, August 30',cy):
    pre=cy[max(0,mm.start()-160):mm.start()]
    chk('&ldquo;' in pre,'cy: stale "due today Sunday" asserted unquoted')
for mm in re.finditer(r'due today',cy,re.I):
    pre=cy[:mm.start()]
    tags=re.findall(r'<span class="tag[^"]*">([^<]*)</span>',pre)
    last=tags[-1] if tags else ''
    if 'New &middot; 12:51 PM' not in last: continue   # only a block published THIS RUN can assert a current deadline
    w=cy[max(0,mm.start()-800):mm.start()+800]
    chk(('&ldquo;' in w) or ('August 30' in w) or ('refus' in w.lower()),
        'cy: current-run "due today" assertion without a verified date')
# BOD heuristic superseded
chk('BOD 22-01' not in cy or 'supersed' in cy.lower(),'cy: BOD 22-01 three-week rule not marked superseded')
# CVSS provenance guards
if '8.8' in cy:
    i=cy.find('CVE-2026-8452'); chk(i>0,'cy: 8452 missing')
# U.S. Bank: the denial must be scoped
chk('fourth party event' in cy,'cy: U.S. Bank fourth-party wording missing')
i=cy.find('LockBit 5')
chk(i>0 and ('disputes' in cy[i-800:i+2500] or 'dispute' in cy[i-800:i+2500]),'cy: LockBit claim not marked disputed')
chk('September 3' in cy,'cy: LockBit deadline missing')
# OpenAI item must be dated
i=cy.find('reward hacking')
chk(i>0 and 'August 26' in cy[max(0,i-2000):i+2500],'cy: OpenAI report date missing')
chk('July 11 and July 13' in cy,'cy: Hugging Face compromise window missing')
# Bouygues must be refused on date, never a live card
if 'Bouygues' in cy:
    i=cy.find('Bouygues'); w=cy[max(0,i-1500):i+1500]
    chk('refused' in w.lower() and 'August 4' in w,'cy: Bouygues not refused on date')
# Nevada permanent exclusion
chk('Nevada' not in cy or 'refus' in cy.lower(),'cy: Nevada statewide item must never appear as current')
# Hasbro dated to March
for mm in re.finditer(r'Hasbro',cy):
    w=cy[max(0,mm.start()-2500):mm.start()+2500]
    chk(('March' in w) or ('sources' in w.lower()) or ('Sources' in w),'cy: Hasbro mention without March dating')
# Carhartt synthetic caveat travels with the number
for mm in re.finditer(r'12\.9 million',cy):
    w=cy[max(0,mm.start()-1500):mm.start()+1500]
    chk('synthetic' in w or 'fake' in w,'cy: 12.9M without synthetic-records caveat')
# Patch Tuesday counts
chk('421' in cy and '62 Critical' in cy and '349' in cy,'cy: Patch Tuesday breakdown incomplete')
chk('751' in cy and 'not adopted' in cy,'cy: 751 variant must be recorded and not adopted')
chk('CVE-2026-68820' in cy and 'afd.sys' in cy,'cy: exploited zero-day detail missing')
chk('CVE-2026-62878' in cy,'cy: new DNS CVE missing')
# threat level banner + by the numbers
chk('Threat Level' in cy or 'threat-level' in cy or 'Threat level' in cy,'cy: threat level banner missing')

# --- MMA ---
mm_=P['mma-briefing.html']
CH={'Tom Aspinall':'Heavyweight','Carlos Ulberg':'Light Heavyweight','Sean Strickland':'Middleweight',
    'Islam Makhachev':'Welterweight','Justin Gaethje':'Lightweight','Alexander Volkanovski':'Featherweight',
    'Petr Yan':'Bantamweight','Joshua Van':'Flyweight'}
for name in CH: chk(name in mm_,'mma: champion missing '+name)
# forbidden regressions
i=mm_.find('<h2 class="sec">Champions Board')
_t=mm_.find('<table',i)
board=mm_[_t:mm_.find('</table>',_t)] if (i>=0 and _t>=0) else ''
chk(i>=0,'mma: champions board missing')
chk('Champions Board</h2>' in mm_,'mma: champions board heading text missing')
_rows=re.findall(r'<tr>(.*?)</tr>',board,re.S)
_champcells=[]
for _r in _rows:
    _c=re.findall(r'<td>(.*?)</td>',_r,re.S)
    if len(_c)>=2: _champcells.append(re.sub(r'<[^>]+>','',_c[1]))
chk(len(_champcells)>=8,'mma: fewer than 8 champion rows')
for _bad in ['Pereira','Chimaev']:
    chk(not any(_bad in _c for _c in _champcells),'mma: %s listed AS a champion'%_bad)
for _c in _champcells:
    chk('acant' not in _c and _c.strip()!='','mma: a champion cell is vacant or empty')
chk(re.search(r'(currently|now) vacant',board,re.I) is None,'mma: a belt is described as currently vacant')
chk('Interim: Ciryl Gane' in board,'mma: Gane interim note missing from the board')
chk('Tom Aspinall' in _champcells[0] if _champcells else False,'mma: heavyweight champion cell wrong')
# interim/undisputed: Gane must never be undisputed HW
for mmx in re.finditer(r'Gane',mm_):
    w=mm_[max(0,mmx.start()-500):mmx.start()+500]
    chk('nterim' in w or 'Sources' in w or 'sources' in w,'mma: Gane mentioned without interim qualifier')
chk('Aspinall' in board,'mma: Aspinall missing from board')
# Blaydes descriptor refusal
i=mm_.find('Blaydes')
chk(i>0,'mma: Blaydes missing')
chk('ex-UFC title challenger' not in mm_ or 'omitted rather than repeated' in mm_,'mma: Blaydes challenger descriptor not refused')
for mmx in re.finditer(r'Blaydes',mm_):
    w=mm_[max(0,mmx.start()-1500):mmx.start()+1500]
    chk('title challenger' not in w or 'omitted' in w or 'not described here' in w or 'Sources' in w,'mma: Blaydes called a title challenger')
# Dariush standing rule
chk('Dariush' not in mm_ or 'challenger' not in mm_[max(0,mm_.find('Dariush')-300):mm_.find('Dariush')+300] or 'Dariush was miscalled' in mm_,'mma: Dariush descriptor')
# odds must name a source/book
i=mm_.find('&minus;550')
chk(i>0,'mma: Parnasse odds missing')
chk('+400' in mm_,'mma: Hooker odds missing')
w=mm_[max(0,i-1500):i+1500]
chk('Yahoo' in w or 'book' in w.lower(),'mma: odds without an attributed book/source')
# Noche UFC details
for v in ['September 12','Desert Diamond Arena','Glendale','Waldo Cortes-Acosta']:
    chk(v in mm_,'mma: Noche detail missing '+v)
# Paris details
for v in ['Accor Arena','September 5','Salahdine Parnasse','Dan Hooker','Michael Page','Nursulton Ruziboev']:
    chk(v in mm_,'mma: Paris detail missing '+v)
# countdown targets the NEXT card (Paris Sep 5), not the next numbered card
chk('ufccdn' in mm_,'mma: countdown element missing')
chk('2026-09-05' in mm_,'mma: countdown must target Sep 5 Paris')
chk('2026-09-19' not in mm_ or mm_.find('2026-09-05')<mm_.find('2026-09-19') or 'ufccdn' in mm_,'mma: countdown target order')
# bonuses only with sourced figures
chk('$400,000' in mm_ and '$100,000' in mm_,'mma: bonus figures missing')
i=mm_.find('$400,000'); w=mm_[max(0,i-1200):i+1200]
chk('Song Yadong' in w,'mma: bonus pool not tied to the event')
# result method/round/time unchanged
chk('KO, round two, 1:48' in mm_ or ('1:48' in mm_ and 'round two' in mm_),'mma: main event method/time missing')
chk('uppercut' in mm_ and 'right hand' in mm_,'mma: both finish readings must remain printed')
# spelling guards from CORRECTIONS.md
chk('Cody Salkilld' not in mm_,'mma: Salkilld first-name regression')
chk('Abdul-Rakhman' not in mm_,'mma: Yakhyaev hyphen regression')
chk('Shamil Yakhyaev' not in mm_,'mma: Yakhyaev name regression')
# seventy-fourth edition claim consistent
chk('seventy-fourth' in mm_,'mma: edition counter not advanced')
chk('seventy-third consecutive edition' not in mm_.split('Sources')[0] or 'seventy-fourth' in mm_,'mma: stale edition counter')
chk('subject to change' in mm_.lower(),'mma: disclaimer missing')

# --- INDEX ---
ix=P['index.html']
chk(ix.count('<a href="')>=6,'index: too few links')
chk(len(re.findall(r'<a href="http',ix))>=6,'index: fewer than 6 source links')
chk('Weekend note' not in ix,'index: stale weekend note')
chk('markets are closed today' not in ix.lower(),'index: stale closed-market note')
for cls in ['c-cy','c-ws','c-mm']: chk('bigcard '+cls in ix,'index: missing card '+cls)
# index summaries must match their pages' leads
chk('Parnasse' in ix and 'Parnasse' in mm_,'index/mma summary mismatch')
chk('LockBit 5' in ix and 'LockBit 5' in cy,'index/cyber summary mismatch')
chk('XLK' in ix and 'XLK' in ws,'index/markets summary mismatch')
chk('U.S. Bank' in ix and 'U.S. Bank' in cy,'index/cyber subject mismatch')

print('CHECKS: %d   FAILURES: %d'%(N,len(FAIL)))
for x in FAIL: print('  FAIL:',x)
sys.exit(1 if FAIL else 0)
