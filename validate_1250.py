#!/usr/bin/env python3
"""Programmatic fact-check / structure gate for the 12:50 ET edition, 2026-08-26."""
import re, sys, datetime

F=[]; N=0
def ck(cond, msg):
    global N; N+=1
    if not cond: F.append(msg)

PAGES = ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
H = {p: open(p, encoding='utf-8').read() for p in PAGES}
ws, cy, mm, ix = H['wallstreet-briefing.html'], H['cyber-briefing.html'], H['mma-briefing.html'], H['index.html']

# ---------- site-wide structure
for p,h in H.items():
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%tab in h, '%s: missing nav tab %s'%(p,tab))
    for i in ['edition','datestamp','updated','freshline']:
        ck('id="%s"'%i in h, '%s: missing id %s'%(p,i))
    ck("America/New_York" in h, '%s: missing self-stamp JS'%p)
    ck(h.count('<a href="index.html"')>=1, '%s: nav'%p)
    ck(h.strip().endswith('</html>'), '%s: truncated'%p)
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    ck('class="tldr"' in H[p], '%s: missing tldr'%p)
ck('The Tape' in ws and 'The Wire' in cy and 'Tale of the Tape' in mm, 'tldr labels')

# ---------- live widget blocks (Wall Street)
for w in ['embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
          'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js']:
    ck(w in ws, 'ws: missing widget '+w)
ck(ws.count('embed-widget-single-quote.js')==3, 'ws: need exactly 3 single-quote widgets')
tape = re.findall(r'"proName":"([^"]+)"', ws)
for m in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(m in tape, 'ws tape missing mandatory '+m)
ck(len(tape)==len(set(tape)), 'ws tape duplicate symbols')
ck('NASDAQ:SMMT' in tape, 'ws tape: SMMT added this run')
ck('NASDAQ:SEDG' not in tape, 'ws tape: SEDG should have been swapped out')
ck('NYSE:DKS' not in tape, 'ws tape: DKS must stay absent')
chart = re.search(r'embed-widget-mini-symbol-overview\.js" async>\{"symbol":"([^"]+)"', ws)
ck(chart and chart.group(1)=='NYSE:ANF', 'ws Chart of the Day must be NYSE:ANF')

# ---------- markets arithmetic (three-way reconciliation, computed here)
PRIOR = 7677.28
for lvl, pts, pct in [(7661.57, 15.71, 0.20), (7662.54, 14.74, 0.19)]:
    ck(abs((lvl + pts) - PRIOR) < 0.005, 'S&P read %s does not subtract to Tuesday close'%lvl)
    ck(abs(pts/PRIOR*100 - pct) < 0.006, 'S&P read %s percent mismatch'%lvl)
ck(abs((7681.36 - 4.08) - PRIOR) < 0.005, '11:06 carried read broken')
ck(abs((7686.64 - 9.36) - PRIOR) < 0.005, '9:59 carried read broken')
ck(abs((142.50 - 33.59) - 108.91) < 0.005, 'ANF implied prior close broken')
ck(abs((345.35 + 12.11) - 357.46) < 0.005, 'INTU reconciliation broken')

for s in ['7,661.57','&minus;15.71','0.20%','12:41:56&nbsp;p.m. EDT','7,662.54','&minus;14.74',
          '12:39&nbsp;p.m. EDT','7,677.28','Nasdaq&nbsp;100 down 0.5%','7,681.36','+30.85%','$142.50']:
    ck(s in ws, 'ws missing: '+s)
ck('$108.91' in ws and 'implied' in ws, 'ws: ANF implied close must stay labelled implied')
ck(ws.count('$108.91')==1, 'ws: $108.91 must occur exactly once')
# CFD must be flagged, never presented as the index
i = ws.find('7,674')
ck(i>0 and 'contract-for-difference' in ws[i-400:i+400], 'ws: 7,674 CFD must be flagged as a CFD')
ck('noted and not\nused' in ws or 'noted and not used' in ws.replace('\n',' '), 'ws: CFD must be marked unused')

# movers this run
for s in ['Summit Therapeutics','&plus;12.49%','ivonescimab','HARMOni','Kura Oncology','&plus;10.5%',
          'Troy Edward Wilson','100,000 shares','$12.39','$0.77','$0.88','$20.87','$20.16',
          'J.M. Smucker','Jefferies Financial Group','&plus;5.5%','fiscal-2027']:
    ck(s in ws, 'ws movers missing: '+s)
# rates
ck('4.65%' in ws and 'Wed, Aug 26 (Trading Economics)' in ws, 'ws: Wednesday 10-year row')
ck('4.629%' in ws, 'ws: Tuesday 10-year retained')
ck('Kevin Warsh' in ws and 'Jackson Hole' in ws, 'ws: Warsh/Jackson Hole')
ck('$280 Billion Earnings' in ws or '$280 billion' in ws.lower(), 'ws: Nvidia options figure')
# no fabricated Dow/Nasdaq levels at the new clock time
seg = ws[ws.find('New at 12:50'):ws.find('New at 12:50')+3000]
ck('53,5' not in seg, 'ws: no Dow level may appear in the 12:50 block')
ck('26,1' not in seg, 'ws: no Nasdaq level may appear in the 12:50 block')

# ---------- cyber
for s in ['CVE-2026-15981','CVE-2026-61979','9.8','8.1','Xecurify','Patchstack','miniOrange',
          'Hut American Group','Flynn Group','3,528','August&nbsp;21, 2026','Apple American Group',
          'August&nbsp;18, 2026','Social Security numbers','TCP port 4307','Head Mare','Kaspersky',
          'September&nbsp;3, 2026','CVE-2026-72529','CVE-2026-72530','BOD&nbsp;26-04']:
    ck(s in cy, 'cy missing: '+s)
ck('nothing seen this run' in cy, 'cy: required wording rule phrase')
ck('CVE-2026-21962' in cy and 'Oracle' in cy, 'cy: Oracle KEV entry')
ck('CVE-2026-60004' in cy and 'Gitea' in cy, 'cy: Gitea KEV entry')
i = cy.find('CVE-2026-60004')
ck('Oracle' not in cy[i:i+120], 'cy: 60004 must not be labelled Oracle')
# KEV board integrity: countdown text must agree with its colour class
spans = re.findall(r'<span class="kevdue (ok|crit)">([^<]+)</span>', cy)
ck(len(spans)==14, 'cy: KEV board must have 14 countdown spans, found %d'%len(spans))
ok = sum(1 for c,t in spans if c=='ok'); crit = sum(1 for c,t in spans if c=='crit')
ck(ok==4 and crit==10, 'cy: board must be 4 ahead / 10 past due, got %d/%d'%(ok,crit))
for c,t in spans:
    if c=='ok':  ck('left' in t, 'cy: ok span text mismatch: '+t)
    if c=='crit': ck('past due' in t or 'due today' in t, 'cy: crit span text mismatch: '+t)
ck('14 rows: 10 past due, none due today, four ahead' in cy or '14</b> entries' in cy, 'cy: board summary')
# deadline consistency: Patch Priority and KEV must name the same deadline
ck(cy.count('due <b>Aug 27</b>')>=1, 'cy: Oracle Aug 27 deadline in board')
pp = cy[cy.find('Patch priority') if cy.find('Patch priority')>0 else cy.find('Patch Priority'):][:2500]
ck('Aug' in pp, 'cy: patch priority must carry a deadline')
# TrueConf CVSS both renderings present and unmerged
ck('9.5' in cy and '9.0 for this CVE' in cy, 'cy: TrueConf CVSS renderings')

# ---------- mma
for s in ['Gregory Rodrigues','#7','Anthony Hernandez','#9','Vitor Petrino','Serghei Spivac',
          'Carli Judice','Jeisla Chaves','Reinier de Ridder','Mike Perry','Dillon Danis',
          'Duel Arena 1','Kia Center','August&nbsp;29','Bare Knuckle Fighting']:
    ck(s in mm, 'mma missing: '+s)
ck('Shanghai Oriental Sports Center' in mm or 'Oriental Sports Center' in mm, 'mma venue')
for m in re.finditer('Shanghai Indoor Stadium', mm):
    ctx = mm[max(0,m.start()-500):m.start()+300]
    ck('Oriental Sports Center name is the one published' in ctx or 'rejected' in ctx or 'again renders' in ctx,
       'mma: "Shanghai Indoor Stadium" outside an explicit-rejection context')
ck('ufccdn' in mm, 'mma countdown element')
# champions board: 11 divisions, correct incumbents, no stale names in the champion column
champs = ['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
          'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison','Mackenzie Dern']
for c in champs:
    ck(c in mm, 'mma champions missing: '+c)
tbl = mm[mm.find('Champions board') if mm.find('Champions board')>0 else mm.find('Champions Board'):]
tbl = tbl[:tbl.find('</table>')]
ck(tbl.count('<tr>')==12, 'mma champions table must have 12 <tr> incl. header, got %d'%tbl.count('<tr>'))
rows = re.findall(r'<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>', tbl, re.S)
champ_col = ' '.join(r[1] for r in rows)
for stale in ['Pereira','Chimaev','Topuria','vacant','Vacant']:
    ck(stale not in champ_col, 'mma STALE/VACANT in champion column: '+stale)
# odds: all four renderings, unmerged
for o in ['&minus;470','+360','&minus;700','+500','&minus;500','+385','+375']:
    ck(o in mm, 'mma odds missing: '+o)

# ---------- index card summaries must match each page's own tldr lead
ck('7,661.57' in ix and '12:41:56' in ix, 'index: markets card must carry the current read')
ck('Hut American' in ix or 'Pizza Hut and Taco Bell franchise operator' in ix, 'index: cyber card')
ck('Gregory Rodrigues up three to #7' in ix, 'index: mma card')
ck('Read the briefing' in ix and ix.count('Read the briefing')==3, 'index: three cards')

# ---------- New-tag hygiene
for p,h in H.items():
    stale = re.findall(r'tag new">New &middot; (?!12:50)([0-9:]+)', h)
    ck(not stale, '%s: undemoted New tags %s'%(p,stale))
counts = {p: len(re.findall(r'tag new">New &middot; 12:50', h)) for p,h in H.items()}
ck(counts['index.html']==0, 'index must carry no New tags')
ck(counts['wallstreet-briefing.html']>=1 and counts['cyber-briefing.html']>=1
   and counts['mma-briefing.html']>=1, 'each briefing needs at least one New tag')

# ---------- trap greps (standing, from CORRECTIONS.md)
TRAPS = ['Fight Night 286','$1.4 trillion','Suno','slipped 0.12%','No opening level for any index',
         'largest single-name move any source fetched this run puts a number on is Intuit',
         'Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman']
for p,h in H.items():
    for t in TRAPS:
        ck(t not in h, '%s: TRAP GREP HIT %r'%(p,t))
# "nothing added" only allowed in a correction/wording-rule context on the cyber page
for m in re.finditer('nothing added', cy):
    ctx = cy[max(0,m.start()-400):m.start()+400]
    ck('wording rule' in ctx or 'never as' in ctx or 'That was wrong' in ctx or 'corrected' in ctx.lower(),
       'cy: "nothing added" outside a correction context')

# ---------- chronology: nothing "upcoming" that has already happened
TODAY = datetime.date(2026,8,26)
ck('August&nbsp;29' in mm, 'mma: next card date')
ck(datetime.date(2026,8,29) > TODAY, 'mma: next card must be in the future')

print('validate_1250: %d checks, %d failures' % (N, len(F)))
for f in F: print('  FAIL:', f)
sys.exit(1 if F else 0)
