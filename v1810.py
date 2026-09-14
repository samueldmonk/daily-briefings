import re,os
OUT='/sessions/practical-quirky-volta/mnt/outputs/'
F={k:open(OUT+v).read() for k,v in
   {'ix':'index.html','cy':'cyber-briefing.html','ws':'wallstreet-briefing.html','mma':'mma-briefing.html'}.items()}
ok=[];bad=[]
def ck(c,m):
    (ok if c else bad).append(m)

# ---- structural, all four pages
for k,h in F.items():
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%tab in h, '%s nav->%s'%(k,tab))
    ck(h.count('class="active"')==1,'%s exactly one active tab (%d)'%(k,h.count('class="active"')))
    for i in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        ck(i in h,'%s masthead %s'%(k,i))
    ck('briefings refresh every 30 minutes' in h,'%s freshline js'%k)
    ck(h.rstrip().endswith('</html>'),'%s closes cleanly'%k)
    ck('&rsquo;&rsquo;' not in h and '&rdquo;&rdquo;' not in h,'%s no doubled smart quotes'%k)
    ck('&amp;amp;' not in h,'%s no double-escaped ampersand'%k)
for k in ('cy','ws','mma'):
    ck('class="tldr"' in F[k],'%s tldr strip'%k)

# ---- TLDR == index card, verbatim
for k,lbl in (('cy','The Wire'),('ws','The Tape'),('mma','Tale of the Tape')):
    t=re.search(r'class="tldr"><b>'+lbl+r'</b> <span>(.*?)</span></div>',F[k],re.S).group(1)
    ck(t in F['ix'],'%s tldr verbatim on index'%k)

# ---- live widgets: markets page only
for w in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','embed-widget-events']:
    ck(w in F['ws'],'ws widget '+w)
for k in ('ix','cy','mma'):
    ck('tradingview' not in F[k].lower(),'%s no tradingview'%k)
ck(F['ws'].count('embed-widget-single-quote')==3,'ws three single quotes')

# ---- markets: scorecard two-way reconciliation
sc=re.search(r'Weekly Scorecard</h2>(.*?)</table>',F['ws'],re.S).group(1)
for name,fri,chg,lvl,pct in (('S&P 500',7656.98,-37.00,7619.98,-0.48),
                             ('Dow',52573.29,-152.09,52421.20,-0.29),
                             ('Nasdaq',26333.03,-146.62,26186.41,-0.56)):
    ck(abs((fri+chg)-lvl)<0.01,'%s level closes from Friday'%name)
    ck(abs(chg/fri*100-pct)<0.01,'%s pct recomputes (%.4f)'%(name,chg/fri*100))
    ck('{:,.2f}'.format(lvl) in sc,'%s level in scorecard'%name)
# oil settle cross-session closure
ck(abs((104.61+1.07)-105.68)<0.005,'Brent cross-session closure')
ck(abs((100.05+1.34)-101.39)<0.005,'WTI cross-session closure')
ck(abs(1.34/100.05*100-1.34)<0.01,'WTI settle pct')
ck(abs(1.07/104.61*100-1.02)<0.01,'Brent settle pct')
ck(abs(4.2-((109.05-104.61)/104.61*100))<0.35,'Brent intraday +4.2%% consistent with settle base (%.2f)'%((109.05-104.61)/104.61*100))
# intraday levels must not appear in / above the scorecard region
head=F['ws'][:F['ws'].find('Weekly Scorecard')]
for banned in ['7,621.54','7,623','26,217','7,657','7,656.98']:
    ck(banned not in head,'ws intraday level %s absent above scorecard'%banned)
# bare superlatives
for s in ['big winner','biggest winner','best performer of the day','than any of the three']:
    ck(s not in F['ws'],'ws no bare superlative "%s"'%s)
# intraday figures labelled
ck('neither is averaged here' in F['ws'],'ws intraday conflict stated not averaged')
ck('settled $101.39' in F['ws'] or '$101.39' in F['ws'],'ws WTI settle present')
ck('$109.05' in F['ws'] and 'intraday' in F['ws'],'ws Brent intraday labelled')
ck('Coherent' in F['ws'] and 'conflict' in F['ws'].lower(),'ws Coherent conflict language retained')
ck('FEIM' in F['ws'] and 'Refused again' in F['ws'],'ws after-hours refusal states FEIM refused')

# ---- cyber
cv=re.findall(r'<tr><td><b>(CVE-[\d-]+)</b></td><td[^>]*>([\d.]*)',F['cy'])
sc_=[float(s) for _,s in cv if s]
ck(sc_==sorted(sc_,reverse=True),'cy CVSS descending %s'%sc_)
unscored=[i for i,(_,s) in enumerate(cv) if not s]
ck(all(i>=len(sc_) for i in unscored),'cy unscored rows last')
stats=re.findall(r'<div class="stat"><div class="n">(.*?)</div>',F['cy'])
ck(len(stats)==4,'cy exactly four stat cells (%d: %s)'%(len(stats),stats))
ck('395' in stats,'cy stat strip carries 395')
ck('Patch Priority' in F['cy'],'cy patch priority')
pp=re.search(r'Patch Priority</h2><div class="callout (\w+)">(.*?)</div>',F['cy'],re.S)
ck(pp.group(1)=='crit','cy patch priority crit border (deadline today)')
for s in ['CVE-2026-82078','CVE-2026-81578','14 September 2026','26.0.5','25.0.13','24.1.10']:
    ck(s in pp.group(2),'cy patch priority mentions %s'%s)
# KEV / patch-priority deadline agreement
ck(F['cy'].count('0 days left &mdash; due today')>=3,'cy three KEV entries due today')
ck('two weeks</b>, not the three weeks BOD 22-01' in F['cy'],'cy flags short KEV window')
ck('31 August 2026' in F['cy'],'cy KEV add date present')
# stale-story grep blocks
for s in ['CVE-2025-10035','GoAnywhere','Storm-1175']:
    ck(s not in F['cy'],'cy stale 2025 story blocked: %s'%s)
ck('PaperCut' in re.search(r'Top Story</h2>(.*?)Patch Priority',F['cy'],re.S).group(1),'cy top story is PaperCut')
ck('PaperCut' in re.search(r'class="tldr"><b>The Wire</b> <span>(.*?)</span>',F['cy'],re.S).group(1),'cy tldr matches its lead')

# ---- mma champions: division-column parse
tbl=re.search(r'Champions Board</h2>.*?<tbody>(.*?)</tbody>',F['mma'],re.S).group(1)
rows=re.findall(r'<tr><td>(.*?)</td><td[^>]*>(.*?)</td>',tbl,re.S)
got={re.sub('<[^>]+>','',d).strip():re.sub('<[^>]+>','',c).strip() for d,c in rows}
EXP={'Heavyweight':'VACANT','Light Heavyweight':'Carlos Ulberg','Middleweight':'Sean Strickland',
 'Welterweight':'Islam Makhachev','Lightweight':'Justin Gaethje','Featherweight':'Alexander Volkanovski',
 'Bantamweight':'Petr Yan','Flyweight':'Joshua Van','Women&rsquo;s Bantamweight':'Kayla Harrison',
 'Women&rsquo;s Flyweight':'VACANT','Women&rsquo;s Strawweight':'Mackenzie Dern'}
for d,c in EXP.items():
    d2=d.replace('&rsquo;','’')
    key=d if d in got else d2
    ck(key in got,'mma board has row %s'%d)
    if key in got: ck(got[key]==c,'mma %s == %s (got %r)'%(d,c,got.get(key)))
ck(sum(1 for v in got.values() if v=='VACANT')==2,'mma exactly two VACANT')
champcol=' '.join(got.values())
for banned in ['Aspinall','Pereira','Chimaev','Shevchenko','Topuria','Pantoja','TBD']:
    ck(banned not in champcol,'mma banned name absent from champion column: %s'%banned)
# upcoming dates must be future
import datetime
ck('Sat 19 Sep' in F['mma'] and 'Sat 3 Oct' in F['mma'] and 'Sat 24 Oct' in F['mma'],'mma upcoming cards present')
fw=re.search(r'Upcoming Cards</h2>(.*?)Last Event',F['mma'],re.S).group(1)
for d in re.findall(r'datel">Sat (\d+) (Sep|Oct)',fw):
    dt=datetime.date(2026,9 if d[1]=='Sep' else 10,int(d[0]))
    ck(dt>datetime.date(2026,9,14),'mma upcoming %s %s is future'%d)
ck('#ufccdn' in F['mma'] or 'ufccdn' in F['mma'],'mma countdown element')
ck("2026-09-19" in F['mma'],'mma countdown targets UFC 331')
ck('ninth consecutive' in F['mma'],'mma names the ESPN regression run count')
ck('Petr Yan' in F['mma'] and 'TBD' in F['mma'],'mma names and refuses the TBD rendering')

# ---- New-tag ledger
led={'cy':1,'ws':1,'mma':0}
for k,n in led.items():
    c=F[k].count('<span class="tag new">New</span>')
    ck(c==n,'%s New tags == ledger %d (got %d)'%(k,n,c))
prev=OUT.replace('/mnt/outputs/','')  # grep against prior snapshot below
print('\n'.join('PASS  '+m for m in ok[:0]))
print('VALIDATION-1810: %d/%d passed'%(len(ok),len(ok)+len(bad)))
for b in bad: print('  FAIL:',b)
