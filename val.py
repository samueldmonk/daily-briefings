# -*- coding: utf-8 -*-
import re,sys
F={n:open(n,encoding='utf-8').read() for n in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
ok=0; fail=[]
def a(cond,msg):
    global ok
    if cond: ok+=1
    else: fail.append(msg)
def has(f,s,n=None):
    c=F[f].count(s)
    a(c>0 if n is None else c==n, '%s: expected %s of %r, got %d' % (f,n or '>0',s,c))
def absent(f,s):
    a(F[f].count(s)==0, '%s: forbidden %r appears %d times' % (f,s,F[f].count(s)))

# --- 1. structure: every page ---
for f in F:
    for s in ['id="edition"','id="datestamp"','id="updated"','America/New_York',
              'index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html',
              '★ Front Page','⛨ The Cyber Wire','▲ The Closing Bell','⊘ The Octagon','Archive']:
        has(f,s)
    a(F[f].count('class="active"')==1, '%s: active tab count %d' % (f,F[f].count('class="active"')))
    a(F[f].startswith('<!DOCTYPE html>'), '%s: doctype' % f)
    a(F[f].rstrip().endswith('</html>'), '%s: closing html' % f)
    a(F[f].count('<body')==1 and F[f].count('</body>')==1, '%s: body tags' % f)
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    has(f,'id="freshline"'); has(f,'class="tldr"',1)
has('cyber-briefing.html','<b>The Wire</b>'); has('wallstreet-briefing.html','<b>The Tape</b>')
has('mma-briefing.html','<b>Tale of the Tape</b>')

# --- 2. index cards mirror each page's TLDR ---
def tldr(f):
    m=re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>',F[f],re.S); return m.group(1)
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    a(tldr(f) in F['index.html'], 'index card does not match %s TLDR' % f)

# --- 3. markets: the hike, the tape, the quotes ---
W='wallstreet-briefing.html'
for s in ['3.75%–4.00%','first increase since <b>July 2023</b>','12–0','Kevin Warsh',
          '751 points','−1.5%','financial-related shares leading the way lower',
          '3:28 p.m. ET','Dow down 0.9%','S&amp;P 500 down 0.3%','near the flat line',
          'plain fact is that inflation is too high and has been for too long',
          'underlying inflation is moving to our objective, clearly and at sufficient speed',
          'standard has not been satisfied','do not tell me that underlying trends have meaningfully improved',
          'unemployment rate has\nchanged little'.replace('\n',' '),
          'one additional hike in 2026','4.1%','3.0%–4.0%','2.0% by 2029','holding steady in\n2027'.replace('\n',' '),
          'neither is reconciled','post-decision index level was verified this run']:
    has(W,s)
# stale / never-publish levels
for s in ['26,197.96','7,609','26,151','7,601','Powell']:
    absent(W,s)
# widgets A-F
for s in ['embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
          'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js']:
    has(W,s)
a(F[W].count('embed-widget-single-quote.js')==3,'three single-quote widgets')
for s in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    has(W,s)
has(W,'"symbol":"NASDAQ:JBHT"')
has(W,'not investment advice')
# scorecard levels intact
for s in ['7,585.73','25,981.57','52,093.11','7,619','26,186','52,421']: has(W,s)
# movers / rates
for s in ['5% to 10%','Starship Flight 14','Sept. 22','Lumentum up <b>8%</b>','Diamondback Energy was down <b>8%</b>',
          '$75,716.63','49–50','4.965%','4.625%','5.346%','5.041%','$4,388.80','$65.28','$107.80','0.96']:
    has(W,s)
a(F[W].count('tag new')==1,'markets: exactly one New tag, got %d'%F[W].count('tag new'))

# --- 4. cyber ---
C='cyber-briefing.html'
for s in ['HSIN','Homeland Security Information Network','late May and early\nJune 2026'.replace('\n',' '),
          'SharePoint','sensitive-but-unclassified','no indication that classified networks were affected',
          'World Cup 2026','CVE-2026-84869','11 September','14 September','BOD 26-04','forensic triage',
          'CWE-269','CWE-862','2 days overdue','CVE-2026-48710','CVE-2026-59822','16 September',
          'due today','CVE-2026-87491','23 September','7 days left','153.0.8010.36','seventh Chrome zero-day of 2026',
          'CVE-2026-84388','9.1','CVE-2026-5430','9.8','CVE-2026-89026','9.3','VulnCheck',
          'NightEagle','APT-Q-95','GhostContainer','Kaspersky','Shai-Hulud','PyPI','GitHub OAuth',
          'CenterPoint Energy','AEPD','autonomous AI agent','6,000 active installs','100,000',
          'Threat level: High']:
    has(C,s)
a(F[C].count('tag new')==1,'cyber: exactly one New tag, got %d'%F[C].count('tag new'))
a('callout crit' in F[C],'cyber: patch priority uses crit border')
absent(C,'4.1.0.257')
# the three patch-count figures must not be asserted as a total
for s in ['230 vulnerabilities','42 vulnerabilities']: absent(C,s)
has(C,'42 vs 230')

# --- 5. MMA ---
M='mma-briefing.html'
for s in ['UFC 331','Crypto.com Arena','Saturday 19 September','Paramount+','Van −130','Pantoja +110',
          'DraftKings','−132','+113','26 seconds into round one','Thursday 17 September','Friday 18 September',
          'Arman Tsarukyan','Maurício Ruffy','Marlon Vera','Charles Jourdain','UFC 332','3 Oct','Wang Cong',
          'Natália Silva','CBS','UFC 333','Etihad Arena','Josh Hokit','Ciryl Gane','Conor McGregor',
          'Ki MMA','Scott Coker','Peter Levin','Michael “Venom” Page','ufccdn','2026-09-19T21:00:00-04:00',
          'subject to change','Mayton Perea','Igor Cavalcanti','Akbar Abdullaev','Luis Hernandez','Tyshawn Williams',
          '28 fighters signed across 30 fights','Jean Silva','Brandon Moreno','Alexa Grasso','Tommy Gantt']:
    has(M,s)
# champions board: correctness
champrow=re.findall(r'<tr><td>([^<]+)</td><td><b>(.*?)</b></td>',F[M])
d=dict(champrow)
exp={'Heavyweight':'VACANT','Light Heavyweight':'Carlos Ulberg','Middleweight':'Sean Strickland',
     'Welterweight':'Islam Makhachev','Lightweight':'Justin Gaethje','Featherweight':'Alexander Volkanovski',
     'Bantamweight':'Petr Yan','Flyweight':'Joshua Van','Women’s Flyweight':'VACANT',
     'Women’s Bantamweight':'Kayla Harrison','Women’s Strawweight':'Mackenzie Dern'}
for k,v in exp.items():
    a(k in d and v in d[k], 'champions: %s should be %s, got %r' % (k,v,d.get(k)))
a(sum(1 for v in d.values() if 'VACANT' in v)==2,'exactly two VACANT cells')
champblock=F[M][F[M].find('Champions Board'):F[M].find('Champions Board')+4000]
for bad in ['Pereira','Chimaev','Topuria','Aspinall','Shevchenko']:
    a(('<b>%s'%bad) not in champblock and ('<td><b>%s'%bad) not in champblock,
      'champions: %s must not occupy a champion cell' % bad)
# these names may appear as prose but never as a seated champion
a(re.search(r'<td><b>(Alex Pereira|Khamzat Chimaev|Ilia Topuria|Tom Aspinall|Valentina Shevchenko)</b></td>',F[M]) is None,
  'champions: a refused name is seated')
a(F[M].count('tag new')==1,'mma: exactly one New tag, got %d'%F[M].count('tag new'))

# --- 6. no unsourced fabrication guards ---
for f in F:
    absent(f,'Lorem'); absent(f,'TODO'); absent(f,'undefined')

print('checks passed: %d' % ok)
if fail:
    print('FAILURES: %d' % len(fail))
    for x in fail: print('  -',x)
    sys.exit(1)
print('0 failures')
