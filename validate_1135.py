import re,sys
P={f:open(f).read() for f in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
N=lambda s: re.sub(r'\s+',' ',s)
FL=[];C=0
def ck(cond,msg):
    global C;C+=1
    if not cond: FL.append(msg)
def has(f,s,msg=None):
    ck(s in N(P[f]), msg or f+': MISSING '+s[:70])
def hasnt(f,s,msg=None):
    ck(s not in N(P[f]), msg or f+': STALE '+s[:70])

# --- structure: every page ---
for f in P:
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        has(f,'href="%s"'%tab, f+': nav missing '+tab)
    for i in ['id="edition"','id="datestamp"','id="updated"']:
        has(f,i,f+': masthead id '+i)
    has(f,"getElementById('edition')",f+': self-stamp js')
    has(f,'Data as of 11:35 AM ET',f+': freshline not stamped 11:35')
    hasnt(f,'Data as of 11:05 AM ET',f+': stale 11:05 freshline')
    has(f,'Updated <span id="updated">11:35 AM ET</span>',f+': masthead time')
    hasnt(f,'Updated <span id="updated">10:50 AM ET</span>',f+': stale 10:50 masthead')
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    has(f,'id="freshline"',f+': freshline id')
    ck('class="tldr"' in P[f], f+': tldr strip')
has('cyber-briefing.html','<b>The Wire</b>'); has('wallstreet-briefing.html','<b>The Tape</b>')
has('mma-briefing.html','<b>Tale of the Tape</b>')

# --- markets: TradingView blocks + closes ---
W='wallstreet-briefing.html'
for w in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']:
    has(W,'embed-widget-'+w, W+': widget '+w)
for s in ['TVC:USOIL','TVC:US10Y','FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','NASDAQ:PYPL']:
    has(W,s)
for v in ['7,711.76','26,402.42','53,559.99','7,730.99','26,541.35','53,569.44']:
    has(W,v,W+': close '+v)
ck(abs(53569.44-9.45-53559.99)<0.005,'dow reconciliation')
ck(abs((7711.76/7730.99-1)*100+0.25)<0.005,'sp reconciliation')
ck(abs((26402.42/26541.35-1)*100+0.52)<0.005,'ndx reconciliation')
hasnt(W,'as of ~',W+': intraday as-of on a closed tape')
hasnt(W,'7,673.04',W+': unverified aggregator level')
hasnt(W,'After-Hours',W+': after-hours block on a weekend')
has(W,'re-verified a ninth time at 11:35 AM')
hasnt(W,'re-verified a seventh time at 10:50 AM')
has(W,'No figure on this movers board changed at 11:35 AM either')
hasnt(W,'No figure on this movers board changed at 11:05 AM either')
# rate family
has(W,'Contested at 11:35 AM:')
has(W,'January 2027')
has(W,'roughly 30% odds of a 25bp September hike')
has(W,'rising to almost')
has(W,'&ldquo;extremely unlikely&rdquo;')
has(W,'3.50%&ndash;3.75%')
has(W,'Jan Hatzius')
has(W,'All of that is pre-Jackson-Hole and is labelled so.')
has(W,'No forecast is offered and no figure is averaged.')
has(W,'about one in three'); has(W,'above 50/50'); has(W,'48%')
has(W,'+58,000'); has(W,'90,000'); has(W,'32,000')
ck(90000-58000==32000,'payrolls gap arithmetic')
has(W,'Friday, September 4')
has(W,'Markets are closed at time of publication.')
has(W,'not investment advice')

# --- cyber ---
C_='cyber-briefing.html'
has(C_,'CVE-2026-18431'); has(C_,'Avada &le; 7.16 with Fusion Builder &le; 3.16')
has(C_,'7.16 stands; the &le;&nbsp;7.1 rendering is the outlier and is recorded, not deleted.')
has(C_,'wrote a working proof of concept from scratch with no human involvement')
has(C_,'Still not KEV-listed; no in-the-wild exploitation stated by any source seen this run.')
has(C_,'has not found any impact')
has(C_,'implantable cardiac rhythm management device function')
has(C_,'timeline for full restoration is not yet known')
has(C_,'No actor, ransom demand or data-theft claim is stated; none printed.')
# KEV countdowns unchanged & consistent
for d in ['(0 days left','(1 day left','(11 days left','(12 days left']:
    has(C_,d,C_+': countdown '+d)
has(C_,'CVE-2026-8452'); has(C_,'CVE-2019-1068')
has(C_,'federal deadline expires TODAY')
# McKesson record-vs-people guards
has(C_,'records, not people')
has(C_,'This page prints neither as a victim count.')
has(C_,'$55,236,150')
has(C_,'not independently verified') if 'not independently verified' in N(P[C_]) else has(C_,'has not independently verified')
# CVE id liveness
ids=set(re.findall(r'CVE-\d{4}-\d{4,6}',P[C_]))
ck(len(ids)>=15,'cyber: expected >=15 distinct CVE ids, got %d'%len(ids))
wl={'CVE-2026-18431','CVE-2026-77537','CVE-2026-77550','CVE-2026-77554','CVE-2026-8452','CVE-2026-82078','CVE-2026-81578','CVE-2019-1068','CVE-2026-69836','CVE-2022-0995','CVE-2021-23758','CVE-2015-5287','CVE-2015-3246','CVE-2026-53362','CVE-2026-66384','CVE-2023-49105','CVE-2026-21962'}
ck(ids<=wl,'cyber: unexpected CVE id(s): %s'%(ids-wl))
# CVE-2026-21962 may appear ONLY inside its not-carried framing
for m in re.finditer('CVE-2026-21962',N(P[C_])):
    w=N(P[C_])[max(0,m.start()-200):m.start()+200]
    ck('not carried' in w,'cyber: CVE-2026-21962 outside its not-carried framing')

# --- MMA ---
M='mma-briefing.html'
champs=['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
        'Alexander Volkanovski','Petr Yan','Joshua Van','Kayla Harrison','Valentina Shevchenko','Mackenzie Dern']
for c in champs: has(M,c,M+': champion missing '+c)
# every Pereira / Chimaev occurrence must sit near a rejection/interim frame
for name in ['Pereira','Chimaev']:
    for m in re.finditer(name,N(P[M])):
        w=N(P[M])[max(0,m.start()-360):m.start()+360]
        ck(any(k in w for k in ['Interim','interim','superseded','rejected','took the middleweight belt from','naming Alex','no longer','regressions','Split decision over Khamzat Chimaev']),
           M+': unframed %s occurrence'%name)
has(M,'rendered <b>men&rsquo;s bantamweight as &ldquo;vacant&rdquo;</b>')
has(M,'That was rejected.')
has(M,'An absence in a listing is not a vacancy')
has(M,'a champion with a booked defence is not a vacancy')
has(M,'three different outcomes in')
# UFC 333 family
has(M,'UFC 333 &mdash; Volkanovski vs. Evloev, and Yan vs. Dvalishvili 3')
has(M,'Etihad Arena, Yas Island, Abu Dhabi')
has(M,'Sat, Oct 24')
has(M,'Movsar Evloev'); has(M,'Merab Dvalishvili'); has(M,'one win apiece')
has(M,'Lone&rsquo;er Kavanagh'); has(M,'Ramazan Temirov')
has(M,'No betting line for this card was stated by any source seen this run, so none is printed')
# callout withdrawal
has(M,'already assigned to someone else')
hasnt(M,'no bantamweight title bout appears on any card in the Fight Week section above.')
has(M,'it is <b>no longer the useful statement</b>')
# punch family
has(M,'short right hand')
has(M,'three different names for one punch')
has(M,'stops counting')
has(M,'connected near his right ear')
has(M,'three finishing shots on the mat')
has(M,'knockout (punch)</b>, remains the only description with a primary source behind it')
hasnt(M,'That is <b>two sources for the uppercut against one for the hook</b>. This page still prints')
has(M,'a count this edition retires')
# odds family
has(M,'&ldquo;nearly 5-1 underdog&rdquo; at DraftKings')
has(M,'no source seen this run states a DraftKings')
has(M,'neither is adopted')
# Usman family
has(M,'Usman Nurmagomedov')
has(M,'nothing landed')
has(M,'Khabib Nurmagomedov helped treat a cut')
has(M,'they differ on')
has(M,'No disciplinary action, commission statement or promotion comment was stated by any')
# results integrity
has(M,'KO (punch), 1:48 of round 2'); has(M,'4:49 of round 1')
has(M,'Quillan') if 'Quillan' in P[M] else None
has(M,'Cards and bouts are subject to change.')

# --- index mirrors each tldr exactly ---
def tldr(f):
    return re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>',P[f],re.S).group(1)
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    ck(N(tldr(f)) in N(P['index.html']), 'index does not mirror tldr of '+f)
has('index.html','UFC 333 in Abu Dhabi on October 24')
has('index.html','contested')
has('index.html','three different names across at least four reports')
has('wallstreet-briefing.html','December read contested 11:35 AM')
hasnt('wallstreet-briefing.html','December read carried')
has('mma-briefing.html','(the reporting does not say where)')
has('index.html','rejected')

# --- footers: links present, no duplicate hrefs ---
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    hrefs=re.findall(r'href="(https?://[^"]+)"',P[f])
    ck(len(hrefs)>=15,f+': too few source links (%d)'%len(hrefs))
    d=[h for h in set(hrefs) if hrefs.count(h)>1]
    ck(not d, f+': duplicate source hrefs: %s'%d[:3])

print('CHECKS:',C,'FAILURES:',len(FL))
for m in FL: print('  FAIL:',m)
sys.exit(1 if FL else 0)
