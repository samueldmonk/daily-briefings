import re,sys,datetime,html as H
FAIL=[];N=0
def ck(cond,msg):
    global N;N+=1
    if not cond: FAIL.append(msg)

P={f:open(f).read() for f in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
AUTH={'Tom Aspinall','Ciryl Gane','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
      'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison','Mackenzie Dern'}
FORBID={'Alex Pereira','Khamzat Chimaev','Ilia Topuria','Alexandre Pantoja','Merab Dvalishvili'}

# --- nav / masthead / freshline on all four ---
for f,h in P.items():
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%tab in h, '%s missing nav tab %s'%(f,tab))
    for pid in ['edition','datestamp','updated']:
        ck('id="%s"'%pid in h, '%s missing pill id=%s'%(f,pid))
    ck('id="freshline"' in h, '%s missing freshline'%f)
    ck(h.count('<div')==h.count('</div>'), '%s div imbalance %d/%d'%(f,h.count('<div'),h.count('</div>')))
    ck(h.count('<table')==h.count('</table>'), '%s table imbalance'%f)
    ck(h.count('<script')==h.count('</script>'), '%s script imbalance'%f)
    # orphaned-entity guard (standing rule after the sed incident)
    for ent in ['mdash;','rsquo;','ldquo;','rdquo;','ndash;','minus;','nbsp;','middot;']:
        for m in re.finditer(re.escape(ent),h):
            ck(m.start()>0 and h[m.start()-1]=='&', '%s orphaned entity %s at %d'%(f,ent,m.start()))

# --- New-tag accounting: cyber 1, ws 0, mma 0, index 0 ---
ck(P['cyber-briefing.html'].count('class="t new"')==1,'cyber New count != 1')
ck(P['wallstreet-briefing.html'].count('class="t new"')==0,'ws New count != 0')
ck(P['mma-briefing.html'].count('class="t new"')==0,'mma New count != 0')
ck(P['index.html'].count('class="t new"')==0,'index New count != 0')
ck('Cyber carries 1 New tag, Wall Street 0, MMA 0.' in P['cyber-briefing.html'],'cyber tag-count sentence wrong')

# --- the New item must be ABSENT from the prior snapshot, and PRESENT now ---
prev=open('archive/cyber-2026-09-06-1715.html').read()
for tok in ['Flagged','not currently publishing detailed information','home device users']:
    ck(tok not in prev,'NEW token %r already in 1715 snapshot'%tok)
    ck(tok in P['cyber-briefing.html'],'NEW token %r missing from cyber page'%tok)
# --- the stripped tags must be gone but their content retained ---
for tok in ['Raiu','Bouma','busybox','eComscan']:
    ck(tok in P['cyber-briefing.html'],'carried token %r lost'%tok)
pw=open('archive/wallstreet-2026-09-06-1715.html').read()
for tok in ['Real Investment Advice','Waller']:
    ck(tok in pw,'ws token %r should be in prior snapshot'%tok)
    ck(tok in P['wallstreet-briefing.html'],'ws token %r lost'%tok)

# --- champions board: exactly 12 rows, champion column only ---
mm=P['mma-briefing.html']
i=mm.find('<h2 class="sec">Champions Board</h2>'); j=mm.find('</table>',i)
rows=re.findall(r'<tr><td>([^<]+)</td><td><b>([^<]+)</b></td>',mm[i:j])
ck(len(rows)==12,'champions rows = %d'%len(rows))
champs={H.unescape(c).strip() for _,c in rows}
ck(champs==AUTH,'champion set mismatch: extra=%r missing=%r'%(champs-AUTH,AUTH-champs))
for bad in FORBID:
    ck(bad not in champs,'FORBIDDEN champion %s in champion column'%bad)
# Harrison must be bantamweight in the table
ck(re.search(r"Women&rsquo;s Bantamweight</td><td><b>Kayla Harrison",mm) or
   re.search(r"Bantamweight</td><td><b>Kayla Harrison",mm),'Harrison not filed under bantamweight')
ck("filed <b>Kayla Harrison under &ldquo;Women&rsquo;s Featherweight.&rdquo;</b>" in mm,'Harrison label refusal missing')

# --- Parnasse guards ---
for m in re.finditer(r'[^.]*Parnasse[^.]*\.',mm):
    s=m.group(0)
    if 'Contender Series' in s:
        ck('not' in s or 'NOT' in s,'Parnasse/Contender-Series assertion: %r'%s[:120])
ck('2:25' in mm and '2:35' in mm,'stoppage both figures must be printed')
ck('2026-09-05T18:40:35&minus;0400' in mm,'modified_time not printed')
ck('<b>six</b> consecutive runs' in mm,'modified_time run-count not updated')
ck('ninth consecutive edition' in mm,'stoppage edition count not updated')

# --- KEV countdowns recomputed from today ---
today=datetime.date(2026,9,6)
cy=P['cyber-briefing.html']
for due,lbl in [(datetime.date(2026,9,18),'18 Sep'),(datetime.date(2026,9,16),'16 Sep')]:
    d=(due-today).days
    ck('%d days left'%d in cy or '(%d days left)'%d in cy,'countdown for %s should be %d days'%(lbl,d))
ck('overdue' in cy.lower(),'5 Sep overdue marker missing')

# --- markets refusals hold ---
ws=P['wallstreet-briefing.html']
ck('Not asserted' in ws,'10Y/Brent refusal rows missing')
# TIGHTENED: 4.79% may appear ONLY inside the 10-year refusal cell, never as a live level
_i=ws.find('US 10-year Treasury yield'); _j=ws.find('</tr>',_i)
_cell=ws[_i:_j]
ck(_cell.count('4.79%')>0 and ws.count('4.79%')==_cell.count('4.79%'),
   '4.79 pct appears outside the 10-year refusal cell (%d total vs %d in cell)'%(ws.count('4.79%'),_cell.count('4.79%')))
ck('Not asserted' in _cell,'10-year cell no longer marked Not asserted')
# TIGHTENED: VIX may appear ONLY in a refusal ("No VIX ..."), never as a published level
for m in re.finditer('VIX',ws):
    ck(ws[max(0,m.start()-3):m.start()]=='No ','VIX published rather than refused at %d'%m.start())
ck(ws.count('VIX')>0,'VIX refusal sentence disappeared')
ck('seventeenth consecutive run without one' in ws,'VIX streak count not advanced this run')
ck('after-hours' not in ws.lower() or 'closed' in ws.lower(),'after-hours block on a weekend')
ck('$91.48' in ws and 'Trading Economics' in ws,'WTI attributed figure missing')
ck('corroborated a second time' in ws,'10Y second corroboration missing')

# --- widgets ---
for w in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']:
    ck('embed-widget-%s.js'%w in ws,'missing widget %s'%w)
ck(ws.count('embed-widget-single-quote.js')==3,'single-quote count != 3')
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(sym in ws,'ticker missing %s'%sym)

# --- tldr labels + index cards match tldrs verbatim ---
lbl={'cyber-briefing.html':'The Wire','wallstreet-briefing.html':'The Tape','mma-briefing.html':'Tale of the Tape'}
for f,l in lbl.items():
    m=re.search(r'<div class="tldr"><b>%s</b>\s*<span>(.*?)</span></div>'%re.escape(l),P[f],re.S)
    ck(bool(m),'%s tldr/label missing'%f)
    if m:
        ck(m.group(1).strip() in P['index.html'],'index card does not match %s tldr verbatim'%f)

# --- weekday guard ---
MON={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
DAY=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for f,h in P.items():
    txt=H.unescape(re.sub(r'<[^>]+>',' ',h))
    for m in re.finditer(r'(%s),?\s+(\d{1,2})\s+(%s)'%('|'.join(DAY),'|'.join(MON,)),txt,re.I):
        wd,dd,mo=m.group(1),int(m.group(2)),m.group(3).lower()
        real=DAY[datetime.date(2026,MON[mo],dd).weekday()]
        if real.lower()!=wd.lower():
            seg=txt[max(0,m.start()-260):m.start()+260]
            ck('own page dates' in seg or 'is a Friday' in seg or 'is wrong' in seg or 'not taken' in seg or 'says so' in seg,
               '%s weekday mismatch: %s %d %s (real %s)'%(f,wd,dd,mo,real))
    for m in re.finditer(r'(%s),\s+(%s)\s+(\d{1,2})'%('|'.join(DAY),'|'.join(k.capitalize() for k in MON)),txt):
        wd,mo,dd=m.group(1),m.group(2).lower(),int(m.group(3))
        real=DAY[datetime.date(2026,MON[mo],dd).weekday()]
        if real.lower()!=wd.lower():
            seg=txt[max(0,m.start()-300):m.start()+300]
            ck('is a Friday' in seg or 'own page dates' in seg or 'The page states Friday' in seg or 'states Friday' in seg,
               '%s weekday mismatch(2): %s %s %d (real %s)'%(f,wd,mo,dd,real))

# --- duplicated-headline guard ---
for f,h in P.items():
    for m in re.finditer(r'<h3[^>]*>(.*?)</h3>',h,re.S):
        t=re.sub(r'<[^>]+>','',m.group(1)).strip()
        ck(len(t)<200 and t[:30] not in t[30:],'%s duplicated headline fragment: %r'%(f,t[:80]))

# --- disclaimers ---
_d=ws.lower()
ck('investment advice' in _d and ('nothing here is investment advice' in _d or 'not investment advice' in _d),'ws disclaimer missing')
ck('information only' in _d,'ws information-only disclaimer missing')
ck('subject to change' in mm.lower(),'mma disclaimer missing')

print('checks:',N,'failures:',len(FAIL))
for x in FAIL: print('  FAIL:',x)
sys.exit(1 if FAIL else 0)
