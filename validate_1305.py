# -*- coding: utf-8 -*-
import io,re,sys
def rd(p): return io.open(p,encoding='utf-8').read()
P={k:rd(k) for k in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
fails=[]; n=0
def chk(cond,msg):
    global n; n+=1
    if not cond: fails.append(msg)
def has(page,s,msg=None): chk(s in P[page], msg or (page+' :: missing '+s[:70]))
def hasnt(page,s,msg=None): chk(s not in P[page], msg or (page+' :: FORBIDDEN '+s[:70]))

STAMP=u'12:58 PM'
# --- structure on every page ---
for p in P:
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        has(p,'href="'+tab+'"',p+' nav missing '+tab)
    for i in ['id="edition"','id="datestamp"','id="updated"']: has(p,i)
    has(p,"Intl.DateTimeFormat",p+' self-stamp js')
    has(p,'America/New_York')
    has(p,'<span id="updated">'+STAMP+' ET</span>',p+' stamp')
    has(p,'Sunday, August 30, 2026'); has(p,'>Midday Edition<')
    # stale stamps must not survive in masthead region
    head=P[p][:P[p].find('</nav>')] if '</nav>' in P[p] else P[p][:6000]
    for stale in ['12:55 PM ET','11:05 AM ET','9:42 PM ET','8:31 PM ET','Afternoon Edition','Saturday, August 29']:
        chk(stale not in head, p+' stale masthead: '+stale); n+=0
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    has(p,'id="freshline">Data as of '+STAMP+' ET')
    has(p,'class="tldr"')

# --- widgets: wall street only ---
ws=P['wallstreet-briefing.html']
for wdg in ['embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
            'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js']:
    has('wallstreet-briefing.html',wdg)
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y','NASDAQ:PYPL']:
    has('wallstreet-briefing.html',sym)
for p in ['index.html','cyber-briefing.html','mma-briefing.html']:
    hasnt(p,'s3.tradingview.com',p+' must have no live widgets')

# --- markets facts ---
for f in ['7,711.76','26,402.42','53,559.99','0.25%','0.52%','9.45','4.73%','4.34%','5.20%']:
    has('wallstreet-briefing.html',f)
chk(abs(9.45/53569.44*100-0.02)<0.01,'Dow points/percent reconcile')
hasnt('wallstreet-briefing.html','7,673.04')
hasnt('wallstreet-briefing.html','as of ~')
hasnt('wallstreet-briefing.html','After-Hours Movers')
has('wallstreet-briefing.html','an eighteenth verification')
hasnt('wallstreet-briefing.html','a seventeenth verification')
has('wallstreet-briefing.html','Sunday midday')
hasnt('wallstreet-briefing.html','Sunday morning')
hasnt('wallstreet-briefing.html','Saturday evening')
has('wallstreet-briefing.html','sixth read')
has('wallstreet-briefing.html','Six reads now')
hasnt('wallstreet-briefing.html','Four reads, all pointing')
# 4.67 must never be asserted as the close: every occurrence sits in a rejection/retired frame
for m in re.finditer(r'4\.67', ws):
    w=ws[max(0,m.start()-320):m.start()+320]
    chk(re.search(r'retired|not adopted|refused|does not displace|was &ldquo;', w) is not None,
        'ws 4.67 without rejection frame @%d'%m.start())
# correct calendar weekdays preserved
has('wallstreet-briefing.html','Friday, September 4')
for m in re.finditer(r'September 5', ws):
    w=ws[max(0,m.start()-400):m.start()+400]
    chk(re.search(r'thrown out|Saturday|not a source|rejected|weekday', w) is not None,
        'ws September 5 without rejection frame @%d'%m.start())

# --- cyber facts ---
cy=P['cyber-briefing.html']
for cve in ['CVE-2026-8452','CVE-2019-1068','CVE-2026-53362','CVE-2023-49105','CVE-2022-0995',
            'CVE-2021-23758','CVE-2015-5287','CVE-2015-3246','CVE-2026-66384','CVE-2026-60004',
            'CVE-2026-73570','CVE-2026-20349','CVE-2026-68820','CVE-2026-72898','CVE-2026-33824',
            'CVE-2026-55040','CVE-2026-59310','CVE-2026-65400','CVE-2026-72529','CVE-2026-72530']:
    has('cyber-briefing.html',cve)
ids=set(re.findall(r'CVE-\d{4}-\d{4,6}',cy)); chk(len(ids)>=20,'cyber >=20 distinct CVE ids, got %d'%len(ids))
chk(all(re.match(r'^CVE-\d{4}-\d{4,6}$',i) for i in ids),'cyber CVE well-formedness')
has('cyber-briefing.html','(OVERDUE')
has('cyber-briefing.html','(0 days left')
has('cyber-briefing.html','(10 days left)')
has('cyber-briefing.html','(11 days left)')
hasnt('cyber-briefing.html','(1 day left)')
hasnt('cyber-briefing.html','(12 days left)')
has('cyber-briefing.html','ninth check at 12:58 PM')
has('cyber-briefing.html','A ninth check')
# Zimbra gap: id must never appear in a countdown bullet, and must sit in a no-due-date frame
for m in re.finditer(r'CVE-2026-73570', cy):
    w=cy[max(0,m.start()-500):m.start()+500]
    chk('days left' not in w,'cyber Zimbra id inside a countdown region @%d'%m.start())
    chk(re.search(r'no source fetched this run states a due date|no row and no countdown|never carried|third', w) is not None,
        'cyber Zimbra without gap frame @%d'%m.start())
for m in re.finditer(r'CVE-2026-60004', cy):
    w=cy[max(0,m.start()-600):m.start()+600]
    chk('days left' not in w,'cyber Gitea id inside a countdown region @%d'%m.start())
# Nevada must stay out (2025 incident resurfacing in a 2026 roundup)
hasnt('cyber-briefing.html','Nevada')
# attacker figures must carry attacker attribution
for fig in ['5.79','284 million','$55,236,150','700GB','700 GB']:
    for m in re.finditer(re.escape(fig), cy):
        w=cy[max(0,m.start()-500):m.start()+500]
        chk(re.search(r'attacker|claim|ShinyHunters|Rhysida|not independently verified|marketing|leak site|own figure|not the city',w,re.I) is not None,
            'cyber %s without attacker attribution @%d'%(fig,m.start()))
# new items present
has('cyber-briefing.html','Anthropic')
has('cyber-briefing.html','infostealer')
has('cyber-briefing.html','AnonyMousKIT')
has('cyber-briefing.html','Apple Support')
# no invented victim count for the Anthropic item
i=cy.find('AnonyMousKIT')
chk('no number of affected accounts' in cy.lower() or 'No number of affected accounts' in cy,'cyber Anthropic count declination')

# --- mma facts ---
mm=P['mma-briefing.html']
champs=['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
        'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison']
for c_ in champs: has('mma-briefing.html',c_)
for bad in ['Pereira is the light heavyweight champion','Chimaev is the middleweight champion',
            'featherweight title is vacant','Topuria is the lightweight champion',
            'vacant featherweight title']:
    hasnt('mma-briefing.html',bad)
# no champions-board row may name a vacant champion
# STRICTER than a vocabulary sweep: assert what may never be true, per occurrence and per row.
for m in re.finditer(r'vacan', mm):
    w=mm[max(0,m.start()-420):m.start()+420]
    chk(re.search(r'(win|won|for) the vacant|vacated|false vacancy|An absence in a listing|published vacant|not vacant|is not a vacancy',w) is not None,
        'mma vacan without accepted frame @%d'%m.start())
# (a) no champions-board table row may name a vacant champion
for row in re.findall(r'<tr>.*?</tr>', mm, re.S):
    if re.search(r'Heavyweight|Welterweight|Lightweight|Featherweight|Bantamweight|Flyweight|Middleweight', row):
        chk(not re.search(r'>\s*[Vv]acant\s*<', row), 'mma champions row names a vacant champion')
# (b) featherweight may never be asserted vacant, and Volkanovski must hold it
chk('Featherweight' in mm and 'Alexander Volkanovski' in mm, 'mma featherweight champion named')
for m in re.finditer(r'[Ff]eatherweight', mm):
    w=mm[m.start():m.start()+140]
    chk(not re.search(r'title is vacant|belt is vacant|currently vacant', w), 'mma featherweight asserted vacant @%d'%m.start())
has('mma-briefing.html','fifty-ninth')
hasnt('mma-briefing.html','fifty-eighth')
# bonuses family
for b in ['$400,000','$100,000','$25,000','Liu Ce','Levi Rodrigues Jr.','Bilal Hasan',
          'Hector Santiago','Francesco Nuzzi','Rei Tsuruya','Kai Asakura','Denise Gomes','ten finishes']:
    has('mma-briefing.html',b)
has('mma-briefing.html','Re-confirmed at 12:58 PM')
# Paris family
for b in ['Accor Arena','Salahdine Parnasse','Dan Hooker','&minus;400','&minus;428','&minus;500',
          'Mario Pinto','Ryan Spann','Oumar Sy','Modestas Bukauskas','12:00 PM ET','3:00 PM ET']:
    has('mma-briefing.html',b)
chk('No single line is adopted' in mm,'mma odds adoption declination')
# Dariush descriptor rule
for m in re.finditer(r'Dariush', mm):
    w=mm[max(0,m.start()-260):m.start()+260]
    chk('title challenger' not in w,'mma Dariush mislabelled challenger @%d'%m.start())
# Song finish facts
for b in ['Song Yadong','Umar Nurmagomedov','Marc Goddard','1:48']: has('mma-briefing.html',b)
# countdown script + next card
has('mma-briefing.html','ufccdn')
has('mma-briefing.html','Sept 5')

# --- index mirrors the three tldrs exactly ---
def tl(path,label):
    s=P[path]; i=s.find('class="tldr"><b>'+label+'</b> <span>')
    j=s.find('</span></div>',i); return s[i+len('class="tldr"><b>'+label+'</b> <span>'):j]
x=P['index.html']
for cls,(pg,lb) in {'c-cy':('cyber-briefing.html','The Wire'),
                    'c-ws':('wallstreet-briefing.html','The Tape'),
                    'c-mm':('mma-briefing.html','Tale of the Tape')}.items():
    i=x.find('<div class="bigcard '+cls+'"'); p=x.find('<p>',i); q=x.find('</p>',p)
    chk(i>0 and p>0,'index card '+cls)
    chk(x[p+3:q]==tl(pg,lb),'index card %s does not mirror %s tldr'%(cls,pg))

# --- footers ---
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=P[p]
    chk('Sources checked this run' in s, p+' sources label')
    hrefs=re.findall(r'<a href="(https?://[^"]+)"', s[s.rfind('<footer'):])
    chk(len(hrefs)>=6, p+' footer needs >=6 source links, got %d'%len(hrefs))
    chk(len(hrefs)==len(set(hrefs)), p+' duplicate footer hrefs')
    chk(all(h.startswith('http') for h in hrefs), p+' non-absolute footer href')
    chk('class="disc"' in s or 'disclaim' in s.lower(), p+' disclaimer')

print('%d checks, %d failures'%(n,len(fails)))
for f in fails: print('  FAIL:',f)
sys.exit(1 if fails else 0)
