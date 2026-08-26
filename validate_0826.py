import re,sys,json,datetime
from html.parser import HTMLParser
D='/sessions/eloquent-kind-maxwell/mnt/outputs/'
F={'index':'index.html','cy':'cyber-briefing.html','ws':'wallstreet-briefing.html','mma':'mma-briefing.html'}
S={k:open(D+v,encoding='utf-8').read() for k,v in F.items()}
fails=[];checks=0
def ck(cond,msg):
    global checks;checks+=1
    if not cond: fails.append(msg)

VOID={'br','hr','img','meta','link','input','source','col','area','base','embed','param','track','wbr'}
class P(HTMLParser):
    def __init__(s):super().__init__();s.st=[];s.unclosed=0;s.stray=0
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st[-1]!=t: s.st.pop();s.unclosed+=1
            s.st.pop()
        else: s.stray+=1
for k,s in S.items():
    p=P();p.feed(s)
    ck(p.unclosed==0,f'{k}: {p.unclosed} unclosed');ck(p.stray==0,f'{k}: {p.stray} stray');ck(len(p.st)==0,f'{k}: left open {p.st}')

# nav: five tabs in order, exactly one .on correctly targeted
order=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']
self_href={'index':'index.html','cy':'cyber-briefing.html','ws':'wallstreet-briefing.html','mma':'mma-briefing.html'}
for k,s in S.items():
    m=re.search(r'<nav class="tabs">(.*?)</nav>',s,re.S); ck(bool(m),f'{k}: no nav')
    nav=m.group(1)
    hrefs=re.findall(r'href="([^"]+)"',nav)
    ck(hrefs==order,f'{k}: nav order {hrefs}')
    ons=re.findall(r'<a href="([^"]+)" class="on">',nav)
    ck(ons==[self_href[k]],f'{k}: on-tab {ons}')

# stamp ids
for k,s in S.items():
    for i in ['edition','datestamp','updated','freshline']:
        ck(f'id="{i}"' in s,f'{k}: missing id {i}')
    ck("Morning Edition" in s and "America/New_York" in s,f'{k}: stamp js')

# tldr: exactly 1 per briefing with correct label, none on index
labels={'cy':'The Wire','ws':'The Tape','mma':'Tale of the Tape'}
ck(S['index'].count('class="tldr"')==0,'index: has tldr')
for k,lab in labels.items():
    ck(S[k].count('<div class="tldr">')==1,f'{k}: tldr count')
    ck(f'<b>{lab}</b>' in S[k],f'{k}: tldr label {lab}')

# index cards carry each page's tldr verbatim
def tldr_text(s):
    m=re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>',s,re.S);return m.group(1).strip()
cardmap={'c-sec':'cy','c-mkt':'ws','c-mma':'mma'}
for cls,pk in cardmap.items():
    m=re.search(r'class="bcard '+cls+r'"[^>]*>.*?<p>(.*?)</p>',S['index'],re.S)
    ck(bool(m),f'index: no {cls} card')
    ck(m.group(1).strip()==tldr_text(S[pk]),f'index: {cls} card p != {pk} tldr')
    h=re.search(r'class="bcard '+cls+r'"[^>]*>.*?<h2>(.*?)</h2>',S['index'],re.S)
    ck(bool(h) and len(h.group(1).strip())>20,f'index: {cls} headline missing')

# TradingView JSON blocks parse
blocks=re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>',S['ws'],re.S)
ck(len(blocks)==8,f'ws: TV blocks {len(blocks)}')
for b in blocks:
    try: json.loads(b)
    except Exception as e: fails.append(f'ws: TV JSON parse {e}')
    checks+=1
tape=[b for b in blocks if '"symbols"' in b][0]
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(sym in tape,f'ws: tape missing {sym}')
cod=re.search(r'embed-widget-mini-symbol-overview\.js" async>(\{.*?\})</script>',S['ws'],re.S)
ck(json.loads(cod.group(1))['symbol']=='NASDAQ:NVDA','ws: chart of the day symbol')

# KEV countdowns
kev=re.findall(r'<span class="kevdue[^"]*">([^<]+)</span>',S['cy'])
ck(len(kev)==13,f'cy: kev rows {len(kev)}')
ahead=[int(re.match(r'(\d+) days? left',x).group(1)) for x in kev if re.match(r'\d+ days? left',x)]
past=[x for x in kev if 'past due' in x]
today=[x for x in kev if 'due today' in x.lower()]
ck(sorted(ahead)==[1,7,8],f'cy: ahead {ahead}')
ck(len(past)==10,f'cy: past due {len(past)}')
ck(len(today)==0,f'cy: due today {len(today)}')
ck(len(ahead)+len(past)+len(today)==13,'cy: kev bucket total')

# per-CVE duplicate row check
cves=set(re.findall(r'(CVE-20\d\d-\d+)',S['cy']))
rows=re.findall(r'<tr><td>(CVE-20\d\d-\d+)</td>',S['cy'])
for c in set(rows):
    ck(rows.count(c)==1,f'cy: duplicate vuln row {c}')

# champions board: 11 rows, no vacant, champion column only
mb=re.search(r'Champions board.*?<table>(.*?)</table>',S['mma'],re.S)
trs=re.findall(r'<tr>(.*?)</tr>',mb.group(1),re.S)
ck(len(trs)==12,f'mma: champ trs {len(trs)}')
champs=[re.findall(r'<td>(.*?)</td>',t,re.S)[1] for t in trs[1:]]
ck(len(champs)==11,f'mma: champ cells {len(champs)}')
good=['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje','Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison','Mackenzie Dern']
for g in good: ck(any(g in c for c in champs),f'mma: champion missing {g}')
for bad in ['Pereira','Chimaev','Topuria','vacant','Vacant','Dvalishvili','Pantoja']:
    ck(not any(bad in c for c in champs),f'mma: stale champion {bad}')

# markets arithmetic gate vs Monday closes
mon={'sp':7652.86,'dow':53417.16,'nas':25980.19}
tue={'sp':(7677.28,24.42,0.32),'dow':(53577.40,160.24,0.30),'nas':(26151.30,171.11,0.66)}
for k,(lvl,pts,pct) in tue.items():
    ck(round(lvl-mon[k],2)==pts,f'ws: {k} pts gate {round(lvl-mon[k],2)} vs {pts}')
    ck(round((lvl-mon[k])/mon[k]*100,2)==pct,f'ws: {k} pct gate {round((lvl-mon[k])/mon[k]*100,2)} vs {pct}')
for lit in ['7,677.28','+24.42','+0.32%','53,577.40','+160.24','+0.30%','26,151.30','+171.11','+0.66%','3,010.02']:
    ck(lit in S['ws'],f'ws: missing {lit}')
# rejected Dow level appears exactly once, inside the rejection
occ=[m.start() for m in re.finditer('53,579.94',S['ws'])]
ck(len(occ)==1,f'ws: 53,579.94 count {len(occ)}')
ck('NOT published' in S['ws'][occ[0]-260:occ[0]+260],'ws: 53,579.94 not scoped to rejection')

# forward dates still in the future
today_d=datetime.date(2026,8,26)
for d in [datetime.date(2026,8,27),datetime.date(2026,8,29),datetime.date(2026,9,2),datetime.date(2026,9,3),datetime.date(2026,9,19),datetime.date(2026,10,3),datetime.date(2026,10,24)]:
    ck(d>today_d,f'forward date past: {d}')

# content guards
ws_guard=['7,687.00','53,701.00','29,215.50','3,014.70','15.67','4,682.80','78,998.81','80.15','core PCE','3.3%','Kevin Warsh','$91.0 billion','$92.2 billion','$91.85 billion','$46.74 billion','CrowdStrike','Williams-Sonoma','Okta','Abercrombie','4.629%','4.183%','5.163%','124.31','30.68%','357.46','100.92','44.27','21.81%','information technology and health care','consumer staples and energy']
cy_guard=['Operation Economic Outcast','Scott Bessent','CVE-2026-21962','CVE-2026-19478','GraphQL','watchTowr','Mirage2FA','ANY.RUN','48%','63.7%','4,500','NemoClaw','Oasis Security','Elad Luz','v0.0.35','v0.0.34','OX Security','Moshe Siman Tov Bustan','Vitalii Chepurko','unpkg','passkey','BOD&nbsp;26-04','CVE-2026-18963','CVE-2026-75149','CVE-2026-15981','CVE-2026-61979','Weedhack','6,300','E4del','PINHOLE','Medusa','CVE-2026-60004','1.27.1']
mma_guard=['Umar Nurmagomedov','Song Yadong','Shanghai Oriental Sports Center','20-1','23-9-1','Yan Xiaonan','Denise Gomes','Aoriqileng','Kai Asakura','&minus;700','+500','&minus;500 / +385','Gregory Rodrigues','Anthony Hernandez','48&ndash;47, 49&ndash;46, 48&ndash;47','MarQuel Mederos','Carli Judice','180-day','26 fighters','Sean Strickland','Joshua Van','Alexandre Pantoja','Arman Tsarukyan','Mauricio Ruffy','Renato Moicano','Brian Ortega','Crypto.com Arena','Movsar Evloev','Deiveson Figueiredo','Merab Dvalishvili']
for g in ws_guard: ck(g in S['ws'],f'ws guard: {g}')
for g in cy_guard: ck(g in S['cy'],f'cy guard: {g}')
for g in mma_guard: ck(g in S['mma'],f'mma guard: {g}')

# trap greps across all pages
traps=['Cody Salkilld','Abdul-Rakhman','Shamil Yakhyaev','title challenger Beneil','Shanghai Indoor Stadium','Pereira retains','Featherweight vacant','markets closed higher today','@@T@@','UFC 336','UFC 335']
for k,s in S.items():
    for t in traps: ck(t not in s,f'{k} trap: {t}')

# countdown script present on mma
ck("id='ufccdn'" in S['mma'] or 'id="ufccdn"' in S['mma'],'mma: no ufccdn')
ck('Fight week — live/completed' in S['mma'],'mma: countdown elapsed text')

print(f'CHECKS: {checks}  FAILURES: {len(fails)}')
for f in fails: print('  FAIL:',f)
sys.exit(1 if fails else 0)
