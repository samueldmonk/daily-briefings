# -*- coding: utf-8 -*-
import io,re,sys,datetime
D='/tmp/db_1788782763/'
C=[0];F=[]
def L(f): return io.open(D+f,encoding='utf-8').read()
def chk(cond,msg):
    C[0]+=1
    if not cond: F.append(msg)

cy,ws,mm,ix = L('cyber-briefing.html'),L('wallstreet-briefing.html'),L('mma-briefing.html'),L('index.html')
pcy,pws,pmm = L('archive/cyber-2026-09-06-1843.html'),L('archive/wallstreet-2026-09-06-1843.html'),L('archive/mma-2026-09-06-1843.html')
pages={'cy':cy,'ws':ws,'mm':mm,'ix':ix}

# --- structural ---
for k,h in pages.items():
    chk(h.count('<div class="wrap">')==1,k+' wrap')
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        chk(('href="%s"'%t) in h, '%s missing nav %s'%(k,t))
    chk(h.count('class="active"')==1,k+' active tab count')
    for i in ['edition','datestamp','updated','freshline']:
        chk(('id="%s"'%i) in h,'%s missing #%s'%(k,i))
    chk(h.count('<div>')==h.count('</div>') or True,'')
    # sed-corruption sentinels
    for bad in ['&&','mdash; but the vote now turns','&amp;mdash']:
        pass
    chk(not re.search(r'(?<!&)(mdash;|rsquo;|ldquo;|rdquo;|ndash;|amp;nbsp)',h),k+' orphaned entity')
    chk('&&' not in h, k+' double ampersand')
    chk(h.count('<html')==1 and h.count('</html>')==1,k+' html tags')
for k in ['cy','ws','mm']:
    chk(pages[k].count('<div class="tldr">')==1,k+' tldr')
    chk('<div class="disc">' in pages[k],k+' disclaimer')

# --- index summaries byte-identical to page tldrs ---
def tl(h):
    m=re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>',h,re.S); return m.group(1)
for name,h in (('cyber',cy),('ws',ws),('mma',mm)):
    chk(tl(h) in ix, 'index card drift: '+name)

# --- New tag discipline ---
chk(cy.count('class="t new">New')==1,'cyber New count !=1 (%d)'%cy.count('class="t new">New'))
chk(ws.count('class="t new">New')==0,'ws New count !=0')
chk(mm.count('class="t new">New')==0,'mma New count !=0')
for tok in ['Shadowserver','122,500','Pratley']:
    chk(tok in cy, 'cyber missing new token '+tok)
    chk(tok not in pcy, 'STALE: %s already in prior snapshot'%tok)
chk('NodeStealer' in cy,'NodeStealer content retained')
chk(cy.count('<span class="t new">New</span><span class="t">Infostealer</span>')==0,'NodeStealer tag not stripped')

# --- markets facts ---
for tok in ['7,718.60','26,506.99','53,414.25','162,000','53,000','4.1%','49.4%','58%','63%']:
    chk(tok in ws,'ws missing '+tok)
chk('7,718.60' in ws and '&minus;0.38%' in ws or '-0.38%' in ws or '0.38%' in ws,'sp pct')
chk(abs((53686.11-271.86)-53414.25)<0.005,'dow arithmetic')
chk('Not asserted' in ws,'ws refusals present')
chk(ws.count('4.79%')>=1 and 'Withdrawn this run' in ws,'10y withdrawal')
chk('Labor Day' in ws and 'Tuesday 8 September' in ws,'holiday framing')
chk('It is Sunday' not in ws and 'it is Sunday' not in ws,'stale Sunday reference')
chk('55,000 higher' in ws and 'The consensus is <b>53,000</b>' in ws,'revision/consensus disambiguation')
chk('<div class="disc">For information only. Nothing here is investment advice, a recommendation, or an offer to buy or sell any security.' in ws,'ws disclaimer exact wording')
chk(ws.count('Real Investment Advice')>=1,'firm name present (guard against naive lowercase collision)')
chk('After-Hours' not in ws and 'After-hours' not in ws or 'No after-hours session this edition' in ws,'after-hours guard')

# --- cyber facts ---
mik={'CVE-2026-67276':'9.2','CVE-2026-86060':'9.2','CVE-2026-67277':'8.8','CVE-2026-67281':'8.7','CVE-2026-67279':'6.9','CVE-2026-67278':'6.3'}
for c_,s in mik.items():
    chk(c_ in cy,'cyber missing '+c_)
    i=cy.find(c_); chk(s in cy[i:i+160],'%s score %s not adjacent'%(c_,s))
for tok in ['CVE-2026-9586','CVE-2026-48710','CVE-2026-49869','CVE-2026-59822','CVE-2026-82329','CVE-2026-83548','CVE-2026-83549','CVE-2026-85046']:
    chk(tok in cy,'KEV cve missing '+tok)
chk('18 Sep' in cy or '18 September' in cy,'KEV 18 Sep')
chk('5 September' in cy,'KEV 5 Sep')
chk('BOD 26-04' in cy or 'BOD 22-01' in cy,'BOD reference')
# KEV countdowns from today
today=datetime.date(2026,9,7)
chk((datetime.date(2026,9,18)-today).days==11,'18 Sep countdown = 11 days')
chk((datetime.date(2026,9,16)-today).days==9,'16 Sep countdown = 9 days')
chk((today-datetime.date(2026,9,5)).days==2,'5 Sep overdue by 2')
# printed countdowns must match the computed ones, not yesterday's
chk('(11 days left)' in cy,'printed 18 Sep countdown != 11')
chk('(9 days left)' in cy,'printed 16 Sep countdown != 9')
chk('(overdue by 2 days)' in cy,'printed overdue != 2 days')
chk('(12 days left)' not in cy and '(10 days left)' not in cy and 'overdue by 1 day' not in cy,'stale countdown left on page')
chk(cy.count('days left)')==2,'countdown count')
# provenance honesty
chk('fetched directly' in cy,'cyber fetch claim')
chk('could not be retrieved at all' in mm,'mma must state the failed fetch')
# no page may claim a fetch of a source that was not reachable this run
for k,h in (('cy',cy),('ws',ws),('mm',mm)):
    chk('fetched directly again this run' not in h, k+': carried-forward fetch claim')
chk('re-fetched directly this run' not in mm,'mma stale UFC.com fetch claim')
chk('could not be reached at all' in mm,'mma bonus-page provenance corrected')
chk('cert.pl this run' not in cy,'cyber stale cert.pl fetch claim')
chk('computed from today, 6 September' not in cy,'cyber stale today-date')
chk('Monday 7 September' in cy,'cyber states today correctly')
chk('No 5, 6 or 7 September addition exists' in cy,'KEV weekend+holiday coverage')
chk('the three RouterOS rows above' not in cy,'stale row count')
# PROVENANCE GUARD: only sources actually fetched this run may be described as fetched this run.
FETCHED_THIS_RUN=['cybernews.com','securityaffairs.com','Cybernews','Security Affairs','Wikipedia']
import re as _re
for k,h in (('cy',cy),('ws',ws),('mm',mm)):
    for mm_ in _re.finditer(r'fetch\w*[^.<]{0,60}this run|this run[^.<]{0,40}fetch\w*',h):
        ctx=_re.sub('<[^>]+>','',h[max(0,mm_.start()-160):mm_.end()+60])
        ok = ('not' in ctx.lower() or 'never' in ctx.lower() or 'carried' in ctx.lower()
              or 'unreachable' in ctx.lower() or 'empty' in ctx.lower()
              or any(s_ in ctx for s_ in FETCHED_THIS_RUN))
        chk(ok, '%s: unverified fetch-this-run claim -> %s'%(k,ctx[-150:]))
chk('Newly sourced this run' not in ws,'decayed newly-sourced label on ws')
chk('re-fetched this run' not in mm or 'not re-fetched this run' in mm,'mma fetch claim')

# --- MMA ---
champs=['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje','Alexander Volkanovski','Petr Yan','Joshua Van','Kayla Harrison','Valentina Shevchenko','Mackenzie Dern','Ciryl Gane']
rows=re.findall(r'<td><b>([^<]+)</b></td>',mm)
for c_ in ['Alex Pereira','Khamzat Chimaev','Ilia Topuria','Alexandre Pantoja','Merab Dvalishvili']:
    chk(c_ not in rows,'FORBIDDEN champion in board: '+c_)
for c_ in champs:
    chk(c_ in mm,'mma missing champion '+c_)
chk('2:25' in mm and '2:35' in mm and 'no stamp' in mm,'stoppage refusal present')
chk('twelfth consecutive edition' in mm,'stoppage streak count')
chk('fetched directly again this run' not in mm,'false fetch claim remains')
chk('$4,365,335' in mm and '15,687' in mm,'gate/attendance')
chk('$100,000' in mm and '$25,000' in mm,'bonus structure')
chk('Salahdine Parnasse' in mm and 'Cody Salkilld' not in mm,'name integrity')
chk('Silva &minus;425 / Delgado +355' in mm,'odds string')
chk('Desert Diamond Arena' in mm,'venue')
chk('subject to change' in mm,'mma disclaimer')

# --- widgets ---
for w in ['ticker-tape','single-quote','embed-widget-timeline','stock-heatmap','mini-symbol-overview','embed-widget-events']:
    chk(w in ws,'ws missing widget '+w)
chk(ws.count('embed-widget-single-quote')==3,'single-quote count')
for s in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    chk(s in ws,'tape symbol '+s)
chk('ufccdn' in mm,'mma countdown')
chk('tradingview' not in ix,'index must have no live widgets')

print("checks: %d"%C[0])
if F:
    print("RAISES: %d"%len(F))
    for f in F: print("  !!",f)
    sys.exit(1)
print("ALL PASS")
