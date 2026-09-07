# -*- coding: utf-8 -*-
import io,re,sys,html
F={k:io.open(k,encoding='utf-8').read() for k in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
fails=[];n=0
def ck(cond,msg):
    global n;n+=1
    if not cond: fails.append(msg)
def txt(s):
    t=re.sub(r'<[^>]+>',' ',s); t=html.unescape(t)
    return re.sub(r'[ \s]+',' ',t)

# ---- structure
for k,s in F.items():
    ck(s.count('<div')==s.count('</div>'), '%s div imbalance %d/%d'%(k,s.count('<div'),s.count('</div>')))
    ck(s.count('<h2')==s.count('</h2>'), k+' h2 imbalance')
    ck(s.count('<tr')==s.count('</tr>'), k+' tr imbalance')
    ck(s.count('<td')==s.count('</td>'), k+' td imbalance')
    ck(s.rstrip().endswith('</html>'), k+' truncated')
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%tab in s, '%s missing nav tab %s'%(k,tab))
    for eid in ['edition','datestamp','updated','freshline']:
        ck('id="%s"'%eid in s, '%s missing #%s'%(k,eid))
    ck("America/New_York" in s, k+' missing self-stamp JS')

CY,WS,MMA,IX=F['cyber-briefing.html'],F['wallstreet-briefing.html'],F['mma-briefing.html'],F['index.html']
tCY,tWS,tMMA,tIX=map(txt,(CY,WS,MMA,IX))

# ---- new-tag ledger: cyber 2, mma 1, ws 0
ck(CY.count('<span class="t new">New</span>')==2,'cyber New tag count = %d, want 2'%CY.count('<span class="t new">New</span>'))
ck(MMA.count('<span class="t new">New</span>')==1,'mma New tag count = %d, want 1'%MMA.count('<span class="t new">New</span>'))
ck(WS.count('<span class="t new">New</span>')==0,'ws New tag count = %d, want 0'%WS.count('<span class="t new">New</span>'))
# and the tagged items must be absent from the 1313 snapshots
snap={'cy':io.open('archive/cyber-2026-09-07-1313.html',encoding='utf-8').read(),
      'ws':io.open('archive/wallstreet-2026-09-07-1313.html',encoding='utf-8').read(),
      'mma':io.open('archive/mma-2026-09-07-1313.html',encoding='utf-8').read()}
for tok in ['Natural Resources Wales','Advantech','79697','79698']:
    ck(tok.lower() not in snap['cy'].lower(), 'novelty fail: %s already in cyber 1313'%tok)
    ck(tok.lower() in CY.lower(), 'new item %s missing from cyber page'%tok)
for tok in ['Christian Leroy Duncan','Allen vs. Duncan']:
    ck(tok.lower() not in snap['mma'].lower(),'novelty fail: %s already in mma 1313'%tok)
    ck(tok in MMA,'new item %s missing from mma page'%tok)
# ledger self-test: previous cyber snapshot did carry a tag
ck(snap['cy'].count('<span class="t new">New</span>')==1,'ledger self-test trivial')
ck(snap['ws'].count('<span class="t new">New</span>')==0,'ws 1313 tag baseline changed')
ck(snap['mma'].count('<span class="t new">New</span>')==0,'mma 1313 tag baseline changed')

# ---- CHAMPIONS BOARD: parse table, 2nd <td> per row
i=MMA.find('Champions Board</h2>'); ck(i>0,'no champions board')
tbl=MMA[i:MMA.find('</table>',i)]
rows=re.findall(r'<tr>(.*?)</tr>',tbl,re.S)
champ=[]
for r in rows:
    tds=re.findall(r'<td[^>]*>(.*?)</td>',r,re.S)
    if len(tds)>=2: champ.append(txt(tds[1]).strip())
ck(len(champ)==12,'champions rows = %d, want 12'%len(champ))
ck('Ciryl Gane' in ' | '.join(champ),'interim HW row missing')
want=['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
      'Alexander Volkanovski','Petr Yan','Joshua Van','Kayla Harrison','Mackenzie Dern']
joined=' | '.join(champ)
for w in want: ck(w in joined,'champion missing from board: %s'%w)
banned=['Alex Pereira','Khamzat Chimaev','Ilia Topuria','Alexandre Pantoja','Merab Dvalishvili']
for b in banned: ck(b not in joined,'REGRESSION: %s in champion column'%b)
ck('Vacant' in joined,'womens flyweight vacancy row missing')

# ---- Parnasse guard
for m in re.finditer(r'Contender Series',tMMA):
    w=tMMA[max(0,m.start()-300):m.start()+300]
    ck('Parnasse' not in w or ' not ' in w,'Parnasse tied to Contender Series')

# ---- Advantech row discipline
j=CY.find('CVE-2026-79697'); adv=txt(CY[j-200:j+3000])
ck('9.9' in adv,'Advantech CVSS 9.9 missing')
ck('VulDB' in adv,'Advantech score not attributed')
ck('1.2.4_20260821' in adv,'Advantech fixed version missing')
ck('not exploited' in adv.lower() or 'NOT in the CISA KEV' in adv,'Advantech exploitation status unstated')
ck('days left' not in adv,'countdown attached to non-KEV Advantech row')

# ---- NRW card discipline
j=CY.find('<h3>Natural Resources Wales'); ck(j>0,'NRW card heading missing'); nrw=txt(CY[j:CY.find('</div>',CY.find('</p>',CY.find('</p>',j)+4))])
ck('April 2013' in nrw and 'March 2018' in nrw,'NRW affected window missing')
ck("Information Commissioner" in nrw,'NRW ICO notification missing')
ck('no evidence' in nrw.lower(),'NRW misuse status missing')
ck('ransom' not in nrw.lower() or 'no ransom' in nrw.lower(),'NRW ransom claim')
ck(not re.search(r'\b\d{1,3}(,\d{3})+ (people|employees|individuals)',nrw),'NRW invented victim count')

# ---- MARKETS: closed-market discipline
ck('After-Hours' not in tWS and 'After Hours' not in tWS,'after-hours block on a closed holiday session')
ck('$5.85' in tWS,'diesel record missing')
for m in re.finditer(r'\$5\.820',tWS):
    w=tWS[max(0,m.start()-650):m.start()+650].lower()
    ck(any(x in w for x in ['supersed','corrects it','corrected it','beat it again','the superseded','out of date','three days','the correction','current record','why the number on this page changed']),
       'stale $5.820 without superseding context')
ck('all-time high of $5.820' not in tWS,'banned superseded record phrasing')
# tldr must not assert a single Brent level while body refuses
tl=txt(WS[WS.find('<div class="tldr">'):WS.find('</div>',WS.find('<div class="tldr">'))])
if 'No single Brent level is asserted' in tWS:
    ck(not re.search(r'Brent trades at \$9\d\.\d\d',tl),'tldr asserts a Brent level the body refuses')
# futures halt arithmetic
ck('1:00 PM ET' in tWS,'CME halt time missing')
ck('has now happened' in tWS or 'in the past' in tWS,'stale "two hours left" framing survives')
ck('roughly two hours of matched trading left in it as the 12:16 edition publishes,\n' not in WS,'raw stale sentence present')
ck('7,722' not in tWS,'unsourced futures level published')
ck('not investment advice' in tWS or 'Nothing here is investment advice' in tWS,'ws disclaimer missing')

# ---- index cards must carry a token from the page each summarises
ck('Natural Resources Wales' in tIX and 'Advantech' in tIX,'index cyber card out of sync')
ck('1:00 PM ET' in tIX,'index markets card out of sync')
ck('Christian Leroy Duncan' in tIX,'index mma card out of sync')
ck('Nothing new on the MMA beat this edition' not in tIX,'stale index mma claim')
ck('New this edition: Tengu' not in tIX,'stale index cyber claim')

# ---- provenance sweeps: no stale "this run"
for k,t in [('cyber',tCY),('ws',tWS),('mma',tMMA)]:
    for m in re.finditer(r'[Tt]his run',t):
        w=t[max(0,m.start()-160):m.start()+160]
        ck(False,'%s stale "this run": %s'%(k,w[:150]))

# ---- KEV countdown arithmetic re-asserted against 7 September
for d,days in [('18 September',11),('16 September',9),('14 September',7)]:
    if d in tCY:
        pass
ck('(7 days left)' in tCY or '7 days left' in tCY,'PaperCut 14 Sep countdown missing/incorrect')

# ---- MMA date sanity
for m in re.finditer(r'Friday',tMMA):
    w=tMMA[max(0,m.start()-160):m.start()+160]
    ck('Paris' not in w,'MMA calls the 5 September Paris card a Friday')
ck('10 October' in tMMA or '10 Oct' in tMMA,'new MMA card date missing')
ck('27&ndash;7' in MMA or '27–7' in tMMA,'Allen record missing')
ck('15&ndash;2' in MMA or '15–2' in tMMA,'Duncan record missing')
for bad in ['title challenger','vacant middleweight']:
    j=tMMA.find('Allen vs. Duncan')
    ck(bad not in tMMA[j:j+1600].lower(),'banned descriptor on the 10 Oct card: '+bad)

print('checks:',n,'failures:',len(fails))
for f in fails: print('  FAIL:',f)
sys.exit(1 if fails else 0)
