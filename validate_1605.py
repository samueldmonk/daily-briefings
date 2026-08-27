import re,sys
F={p:open(p).read() for p in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
ok=0; fail=[]
def A(c,m):
    global ok
    if c: ok+=1
    else: fail.append(m)

# --- freshness / edition stamp guard ---
for p,h in F.items():
    if p=='index.html': continue
    for m in re.finditer(r'<span class="tag new">(.*?)</span>',h):
        t=m.group(1)
        A('4:05' in t, f"{p}: stale/bare freshness tag {t!r}")
    A('tag new">New</span>' not in h, f"{p}: bare 'New' tag")
    A(len(re.findall(r'<span class="tag new">',h))>=1, f"{p}: no fresh tag at all")
# prospect tags exempt (design tags), confirm they are not 'tag new'
A('class="tag ok">prospect' in F['mma-briefing.html'] or 'prospect' in F['mma-briefing.html'], "mma: prospect tags gone")

# --- champions board: parse real td cells, regression traps ---
mm=F['mma-briefing.html']
sec=mm[mm.find('Champions Board'):]
rows=re.findall(r'<tr>(.*?)</tr>',sec,re.S)
cells=[re.findall(r'<td.*?>(.*?)</td>',r,re.S) for r in rows]
champ=[c[1] for c in cells if len(c)>=2]
A(len(champ)>=11, f"champions board only {len(champ)} rows")
def strip(x): return re.sub(r'<[^>]+>','',x)
champtxt=' | '.join(strip(c) for c in champ)
for bad in ['Pereira','Chimaev','Topuria']:
    A(bad not in champtxt, f"REGRESSION: {bad} in a champion cell")
A('vacant' not in champtxt.lower(), "REGRESSION: 'vacant' in a champion cell")
for good in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Van','Shevchenko','Harrison','Dern']:
    A(good in champtxt, f"champion missing: {good}")

# --- name traps ---
for p,h in F.items():
    for bad in ['Shamil Yakhyaev','Cody Salkilld','Abdul-Rakhman']:
        A(bad not in h, f"{p}: forbidden name {bad}")
# spelling splits preserved
A('Balleto' in mm and 'Balletto' in mm, "mma: Balleto/Balletto split not preserved")
A('Qileng Aori' in mm and 'Aoriqileng' in mm, "mma: Aoriqileng split not preserved")
A('Su Mudaerji' in mm and 'Sumudaerji' in mm, "mma: Sumudaerji split not preserved")

# --- new MMA facts present & exact ---
for s in ['Gregory Rodrigues','Anthony Hernandez','six-month suspensions','MarQuel Mederos','Mason Jones',
          'Carli Judice','Jeisla Chaves','UFC 331','Crypto.com Arena','Alexandre Pantoja','Arman Tsarukyan',
          'Mauricio Ruffy','Marlon Vera','Charles Jourdain','Adam Darby','Patrick Rivera','Gabriel Louren',
          '&minus;170' if False else '−170','+295','−380']:
    A(s in mm, f"mma missing: {s}")
A('48-47, 49-46, 48-47' in mm, "mma: scorecards changed")
A('26 seconds into the first round' in mm, "mma: UFC323 detail missing")
A('September 19' in mm and 'UFC 227' in mm, "mma: UFC331 date/history missing")
# Dariush descriptor guard
A('Dariush' not in mm or 'title challenger' not in mm, "mma: Dariush mislabelled challenger")

# --- markets ---
ws=F['wallstreet-briefing.html']
for s in ['1.31%','0.66%','0.33%','156 of the 503','23 of the 30','$461 billion','7,727','7,675.70','22.87%','20.47%','8.4%']:
    A(s in ws, f"ws missing: {s}")
# arithmetic guard
A(abs(7675.70*1.0067-7727.1)<0.15, "ws: reconciliation arithmetic wrong")
A('7,727.1' in ws, "ws: reconciliation figure absent")
A(abs(156/503*100-31)<0.5, "ws: 31% breadth derivation wrong")
A('31%' in ws, "ws: breadth percentage absent")
# no close asserted for Aug 27
A('not published here as the official close' in ws or 'not asserted' in ws, "ws: close disclaimer missing")
A('still carries no August 27 row' in ws, "ws: scorecard disclaimer missing")
sc=ws[ws.find('Weekly Scorecard</h2>'):ws.find('Rates, Bonds')]
A('Aug 27' not in sc and 'August 27' not in sc.replace('no August 27 row',''), "ws: an Aug 27 row leaked into the scorecard")
# rejected figures window-scoped
A('7,673.04' in ws and 'Neither is published' in ws, "ws: 7673.04 rejection text missing")
A('fifth time' in ws and '1.82%' in ws, "ws: energy fifth rejection missing")
# the 'faded' claim must NOT be asserted
A('the tape faded into the bell' in ws and 'is not written' in ws, "ws: faded claim not properly withheld")
# after-hours section
A('After-Hours Movers' in ws, "ws: after-hours section missing")
A('empty of numbers on purpose' in ws, "ws: after-hours honesty line missing")

# --- widgets ---
A(len(set(re.findall(r'embed-widget-[a-z-]+\.js',ws)))==6, "ws: not 6 distinct TradingView widget types")
A(ws.count('s3.tradingview.com')==8, f"ws: expected 8 TV script tags (5 blocks + 3 quotes), got {ws.count('s3.tradingview.com')}")
A(ws.count('embed-widget-single-quote.js')==3, "ws: not exactly 3 single-quote widgets")
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    A(sym in ws, f"ws: ticker symbol missing {sym}")
A('NASDAQ:OKTA' in ws, "ws: Chart of the Day symbol changed")
for p in ['index.html','cyber-briefing.html','mma-briefing.html']:
    A('s3.tradingview.com' not in F[p], f"{p}: live widget leaked onto non-markets page")

# --- cyber ---
cy=F['cyber-briefing.html']
A('BOD 22-01' not in cy, "cyber: BOD 22-01 present")
A('BOD 26-04' in cy, "cyber: BOD 26-04 absent")
A(cy.count('Aug 29')+cy.count('August 29')>=4, "cyber: Aug 29 not in >=4 places")
A('overdue — deadline expired today' in cy, "cyber: Oracle countdown not flipped to overdue")
A('due today, August 27' not in cy, "cyber: stale 'due today' text survives")
A('CVE-2026-8452' in cy and '2 days left' in cy, "cyber: Citrix countdown wrong")
for s in ['x.php','z.php','June 30, 2026','Nutex Health','afd.sys','Babuk','CVE-2026-55040','CVE-2026-33824']:
    A(s in cy, f"cyber missing: {s}")
# CVE whitelist
WL={'2026-21962','2026-8452','2026-60004','2026-68820','2026-73570','2015-3246','2015-5287','2019-1068',
 '2021-23758','2022-0995','2026-45659','2026-58231','2026-20253','2026-19490','2026-18963','2026-19912',
 '2026-19913','2026-62815','2026-62893','2026-64633','2026-65641','2026-69836','2026-12569','2026-8037',
 '2026-55040','2026-33824','2026-20349','2026-59310','2026-65400','2026-72529','2026-72530','2026-72898'}
found=set(re.findall(r'CVE-(\d{4}-\d{4,6})',cy))
A(len(found)>=20, f"cyber: only {len(found)} CVE ids (liveness)")
for f_ in sorted(found-WL): fail.append(f"cyber: CVE-{f_} not in whitelist — verify in page context")
if not (found-WL): ok+=1
# CVSS sanity: Citrix vendor 8.8 kept, no blog 9.8 substituted for it
A('CVSS 8.8' in cy, "cyber: Citrix vendor CVSS missing")
A('CVSS 10.0' in cy, "cyber: Oracle CVSS missing")

# --- structural: nav, masthead, freshline, stamp JS ---
for p,h in F.items():
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        A(f'href="{tab}"' in h, f"{p}: nav missing {tab}")
    for i in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        A(i in h, f"{p}: masthead/freshline {i} missing")
    A('America/New_York' in h, f"{p}: self-stamp JS missing")
    A(h.count('<div class="tldr">')==(0 if p=='index.html' else 1), f"{p}: tldr count wrong")
A('id="ufccdn"' in mm, "mma: countdown element missing")

# --- index cards byte-identical to tldrs ---
for p,cls in (('cyber-briefing.html','c-cy'),('wallstreet-briefing.html','c-ws'),('mma-briefing.html','c-mm')):
    t=re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>',F[p],re.S).group(1)
    A(t in F['index.html'], f"index card {cls} not byte-identical to {p} tldr")

print(f"validate_1605: {ok} checks passed, {len(fail)} failures")
for f_ in fail: print("  FAIL:",f_)
sys.exit(1 if fail else 0)
