import re,os,datetime
O='/sessions/adoring-eloquent-dirac/mnt/outputs/'
P={k:open(O+k,encoding='utf-8').read() for k in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
PREV={'cyber':'cyber-2026-09-03-1733.html','wallstreet':'wallstreet-2026-09-03-1733.html','mma':'mma-2026-09-03-1733.html'}
AR='/tmp/db_1788471313/archive/'
prev={k:open(AR+v,encoding='utf-8').read() for k,v in PREV.items()}
E=[]
def ck(c,m):
    if not c: E.append(m)

mma=P['mma-briefing.html']; cy=P['cyber-briefing.html']; ws=P['wallstreet-briefing.html']; ix=P['index.html']
# champions guards
for bad in ['Alex Pereira</td>','Khamzat Chimaev</td>','Ilia Topuria</td>']:
    ck(bad not in mma, 'stale champion cell: '+bad)
ck('Carlos Ulberg' in mma and 'Sean Strickland' in mma and 'Justin Gaethje' in mma and 'Alexander Volkanovski' in mma,'champions board missing verified names')
ck('Anderson Silva' not in mma,'Anderson Silva must never appear (it is Jean Silva)')
ck('Jean Silva' in mma and 'Jose Miguel Delgado' in mma,'Noche main event missing')
seg=mma.split('On Salahdine Parnasse')[1][:500]
ck('not a Contender Series signee' in seg,'Parnasse negation sentence missing')
ck(len(re.findall(r'Contender Series',seg))==1,'Parnasse segment mentions Contender Series more than once')
ck('KSW' in mma,'Parnasse KSW provenance missing')
# cyber guards
ck('Nevada' not in cy,'Nevada 2025 incident must stay excluded')
ck('BOD 22-01' not in cy,'BOD 22-01 superseded')
ck('September 14' not in cy,'blocked date September 14')
ck('BOD 26-04' in cy,'BOD 26-04 missing')
ck(cy.count('due Sept 5')==5,'expected 5 KEV rows due Sept 5, got %d'%cy.count('due Sept 5'))
ck(cy.count('due Sept 16')==2,'expected 2 KEV rows due Sept 16')
ck('three other flaws' in cy and 'three other flaws' in ix,'KEV tranche arithmetic wording')
ck('2 days left' in cy and '13 days left' in cy,'KEV countdowns')
# countdown arithmetic
today=datetime.date(2026,9,3)
ck((datetime.date(2026,9,5)-today).days==2,'Sept 5 countdown')
ck((datetime.date(2026,9,16)-today).days==13,'Sept 16 countdown')
# calendar weekday checks
for d,name in [((2026,9,5),'Sat'),((2026,9,8),'Tue'),((2026,9,12),'Sat'),((2026,9,19),'Sat'),((2026,10,3),'Sat'),((2026,9,16),'Wed'),((2026,9,20),'Sun')]:
    ck(datetime.date(*d).strftime('%a')==name,'weekday mismatch %s'%(d,))
# markets arithmetic
ck(abs(53686.11-624.16-53061.95)<0.01,'Dow reconciliation')
ck(abs((7747.71/7666.60-1)*100-1.058)<0.01,'S&P pct')
ck(abs((26584.06/26217.83-1)*100-1.397)<0.01,'Nasdaq pct')
# New-tag comparator
def cards(h):
    return re.findall(r'<div class="card">(.*?)</p>',h,re.S)
for key,page in [('cyber',cy),('mma',mma),('wallstreet',ws)]:
    for c in cards(page):
        if '<span class="t new">New</span>' not in c: continue
        h3=re.search(r'<h3>(.*?)</h3>',c,re.S)
        if not h3: continue
        title=re.sub(r'<[^>]+>','',h3.group(1))
        nouns=[w for w in re.findall(r"[A-Z][A-Za-z'&-]{3,}",title) if w not in ('The','This','From','Five','Four')]
        for n in nouns:
            if n in prev[key]:
                E.append('%s: New tag on "%s" but "%s" was in the 1733 snapshot'%(key,title.strip(),n))
                break
# widget count
ck(ws.count('s3.tradingview.com')==8,'expected 8 tradingview widgets, got %d'%ws.count('s3.tradingview.com'))
# nav present on all pages
for k,v in P.items():
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck(t in v,'%s missing nav link %s'%(k,t))
    ck('id="freshline"' in v and 'id="edition"' in v and 'id="datestamp"' in v and 'id="updated"' in v,'%s missing meta ids'%k)
ck('&#9960;' in ix,'index security glyph')
print('checks done. issues:',len(E))
for e in E: print(' -',e)
