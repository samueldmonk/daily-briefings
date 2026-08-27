import re,sys
F=[];C=[0]
def ck(cond,msg):
    C[0]+=1
    if not cond: F.append(msg)
R={f:open(f,encoding='utf-8').read() for f in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
ws,cy,mm,ix=R['wallstreet-briefing.html'],R['cyber-briefing.html'],R['mma-briefing.html'],R['index.html']

# --- structure: five-tab nav, masthead ids, tldr, freshline, stamp js ---
for f,s in R.items():
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck(f'href="{t}"' in s, f'{f}: nav missing {t}')
    for i in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        ck(i in s, f'{f}: missing {i}')
    ck("America/New_York" in s, f'{f}: missing stamp js')
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    ck(R[f].count('class="tldr"')==1, f'{f}: tldr count')
ck('<b>The Tape</b>' in ws and '<b>The Wire</b>' in cy and '<b>Tale of the Tape</b>' in mm,'tldr labels')

# --- index cards byte-identical to page tldrs ---
def tldr(s):
    return re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>',s,re.S).group(1)
for nm,s in (('ws',ws),('cy',cy),('mm',mm)):
    ck(tldr(s) in ix, f'index card not byte-identical to {nm} tldr')

# --- TradingView widgets on WS ---
for w in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']:
    ck(f'embed-widget-{w}.js' in ws, f'ws: missing widget {w}')
ck(ws.count('embed-widget-single-quote.js')==3,'ws: single-quote count != 3')
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(sym in ws, f'ws: ticker symbol {sym}')
ck('NASDAQ:OKTA' in ws,'ws: chart-of-day symbol')
for s in (cy,mm,ix): ck('tradingview' not in s.lower(),'live widget on non-WS page')

# --- freshness: no bare "New", every new tag stamped 2:41 ---
for f,s in R.items():
    for m in re.finditer(r'<span class="tag new"[^>]*>([^<]*)</span>',s):
        t=m.group(1).strip()
        if t=='prospect': continue  # design tag, not a freshness tag
        ck('2:41' in t, f'{f}: stale/bare new tag {t!r}')
for f,s in R.items():
    ck('>New</span>' not in s, f'{f}: bare unstamped New tag')

# --- CHAMPIONS BOARD: parse real <td> champion cells ---
mrows=re.findall(r'<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>',mm,re.S)
board=re.search(r'Champions Board.*?<table>(.*?)</table>',mm,re.S)
ck(board is not None,'mma: champions table missing')
if board:
    rows=re.findall(r'<tr>(.*?)</tr>',board.group(1),re.S)
    cells=[re.findall(r'<td[^>]*>(.*?)</td>',r,re.S) for r in rows]
    champ=[re.sub('<[^>]+>','',c[1]).strip() for c in cells if len(c)>=2]
    ck(len(champ)>=11, f'mma: champions rows {len(champ)} < 11')
    joined=' | '.join(champ)
    for bad in ['Pereira','Chimaev','Topuria','vacant','Vacant']:
        ck(bad not in joined, f'mma: REGRESSION {bad} in champion cell')
    for good in ['Ulberg','Strickland','Gaethje','Volkanovski','Aspinall','Makhachev','Yan','Van','Shevchenko','Harrison','Dern']:
        ck(good in joined, f'mma: champion {good} missing')

# --- name trap greps ---
for f,s in R.items():
    for bad in ['Shamil Yakhyaev','Cody Salkilld','Abdul-Rakhman']:
        ck(bad not in s, f'{f}: trap name {bad}')

# --- CVE whitelist ---
WL={'2026-21962','2026-8452','2019-1068','2026-60004','2026-68820','2026-73570','2015-3246','2015-5287','2021-23758','2022-0995','2026-72529','2026-72530','2026-33824','2026-55040','2026-59310','2026-65400','2026-20349','2026-72898','2026-8037','2026-19490','2026-45659','2026-58231','2026-20253','2026-18963','2026-19912','2026-19913','2026-62815','2026-62893','2026-12569','2026-59287','2026-40890','2026-31324','2026-53770','2026-49704','2026-30397','2026-64633','2026-65641','2026-69836'}
ids=set(re.findall(r'CVE-(\d{4}-\d{4,6})',cy))
ck(len(ids)>=20, f'cyber: only {len(ids)} CVE ids (liveness)')
for i in sorted(ids-WL): F.append(f'cyber: CVE-{i} not in whitelist'); C[0]+=1

# --- KEV / deadline coherence ---
ck(cy.count('Aug 29')+cy.count('August 29')>=4,'cyber: Aug 29 in <4 places')
ck('BOD 22-01' not in cy,'cyber: BOD 22-01 present (retired)')
ck('BOD 26-04' in cy,'cyber: BOD 26-04 missing')
for kid in ['kev1','kev2','kev3','kev4','kev5','kev6']:
    ck(f'id="{kid}"' in cy, f'cyber: {kid} id missing')
    ck(f"'{kid}'" in cy or f'"{kid}"' in cy, f'cyber: {kid} not set by js')

# --- window scoping: rejected figures must appear ONLY inside their rejection text ---
def scoped(s,fig,words,win=1400):
    ok=True
    for m in re.finditer(re.escape(fig),s):
        seg=s[max(0,m.start()-win):m.start()+win]
        if not any(w in seg for w in words): ok=False
    return ok
ck(scoped(ws,'7,673.04',['rejected','not published','Not published','impossible']),'ws: 7,673.04 unscoped')
ck(scoped(ws,'6,279',['2025 levels','rejected','Not published']),'ws: 6,279 unscoped')
ck(scoped(ws,'$3.97 trillion',['2025 levels','rejected','Not published']),'ws: 3.97T unscoped')
ck(scoped(ws,'232,000',['rejected','2022']),'ws: 232,000 unscoped')
ck(scoped(ws,'1.82%',['not published','Not published','refused','withheld']),'ws: 1.82% unscoped')
ck(ws.count('1.82%')>=2,'ws: 1.82% fourth-rejection text missing')
ck('refused a fourth time' in ws,'ws: fourth rejection not stated')

# --- inverted Jackson Hole guard ---
ck('That reasoning was wrong.' in ws,'ws: Jackson Hole correction must remain published')
ck('August 27' in ws and 'Jackson Lake Lodge' in ws,'ws: Jackson Hole details')

# --- this run: new facts present ---
for fig,f,s in [('9.3%','ws',ws),('1.51%','ws',ws),('1.5% in the second quarter','ws',ws),('1.1% in July','ws',ws),
                ('TeamPCP','cy',cy),('Gaebler','cy',cy),('Thomson','cy',cy),('12,933,413','cy',cy),('8.7 million','cy',cy),
                ('16,867','mm',mm),('$3,300,000','mm',mm),('Reinier de Ridder','mm',mm)]:
    ck(fig in s, f'{f}: new fact {fig!r} missing')

# --- index must not carry retired figures ---
for bad in ['under three hours','doubled to 0.8% on the afternoon read','Desert Diamond Arena']:
    ck(bad not in ix, f'index: stale text {bad!r}')

# --- arithmetic guard: "Four" ladder must list four Dow reads ---
m=re.search(r'Four point-and-percent index reads(.{0,2400}?)</p>',ws,re.S)
ck(m is not None,'ws: ladder paragraph missing')
if m:
    plain=re.sub('<[^>]+>','',m.group(1))
    dows=re.findall(r'\+\d{3}\.\d{2} \(\+\d\.\d{2}%\)',plain)[:4]
    nasd=re.findall(r'\+\d{3}\.\d{2} \(\+\d\.\d{2}%\)',plain)
    ck(len(nasd)==8, f'ws: ladder should list 8 pairs (4 Dow + 4 Nasdaq), lists {len(nasd)}')
    ck(len(dows)==4, f'ws: ladder says Four but lists {len(dows)} Dow reads')

# --- gate arithmetic sanity ---
ck(abs(3300000/16867-195.6)<2,'mma: $196/ticket arithmetic wrong')

print(f'validate_1441: {C[0]} checks, {len(F)} failures')
for x in F: print('  FAIL:',x)
sys.exit(1 if F else 0)
