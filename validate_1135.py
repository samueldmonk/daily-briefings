import io,re,sys
D='/sessions/optimistic-youthful-curie/mnt/outputs/'
F={k:io.open(D+v,encoding='utf-8').read() for k,v in
   {'idx':'index.html','cy':'cyber-briefing.html','ws':'wallstreet-briefing.html','mma':'mma-briefing.html'}.items()}
fails=[];checks=[0]
def ok(cond,msg):
    checks[0]+=1
    if not cond: fails.append(msg)
def has(k,sub,msg=None): ok(sub in F[k], msg or ('%s missing: %s'%(k,sub[:90])))
def no(k,sub,msg=None): ok(sub not in F[k], msg or ('%s must NOT contain: %s'%(k,sub[:90])))
def cnt(k,sub,c,msg=None): ok(F[k].count(sub)==c, msg or ('%s count %d != %d for %s'%(k,F[k].count(sub),c,sub[:70])))

# ---- structure: nav, masthead, stamp js -------------------------------------
for k in F:
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        has(k,'href="%s"'%tab)
    for pill in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        has(k,pill)
    has(k,"Morning Edition")
    has(k,"Midday Edition")
    has(k,"Afternoon Edition")
    has(k,"briefings refresh every 30 minutes")
    ok(F[k].count('<div')==F[k].count('</div>'),'%s unbalanced div (%d/%d)'%(k,F[k].count('<div'),F[k].count('</div>')))
    ok(F[k].count('<table')==F[k].count('</table>'),'%s unbalanced table'%k)
    ok(F[k].count('<tr')==F[k].count('</tr>'),'%s unbalanced tr'%k)
    ok(F[k].count('<td')==F[k].count('</td>'),'%s unbalanced td'%k)
# active tab per page
has('idx','href="index.html" class="on"'); has('cy','href="cyber-briefing.html" class="on"')
has('ws','href="wallstreet-briefing.html" class="on"'); has('mma','href="mma-briefing.html" class="on"')
# tldr labels
has('cy','<b>The Wire</b>'); has('ws','<b>The Tape</b>'); has('mma','<b>Tale of the Tape</b>')
no('idx','class="tldr"','index must use cards, not a tldr strip')

# ---- live widgets: wall street only -----------------------------------------
for w in ['embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
          'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js']:
    has('ws',w)
cnt('ws','embed-widget-single-quote.js',3)
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    has('ws',sym,'ws missing mandatory tape symbol '+sym)
for k in ['idx','cy','mma']:
    no(k,'s3.tradingview.com','%s must carry no live widgets'%k)
has('ws','"symbol":"NASDAQ:OKTA"','Chart of the Day must track the session biggest mover (OKTA)')
has('ws','NASDAQ:ZS'); has('ws','NASDAQ:OKTA')

# ---- WALL STREET editorial ---------------------------------------------------
for x in ['217.20','+0.41%','327.22','+1.25%','169.90','300.97','11:35 AM ET','Midday session']:
    has('ws',x)
# rejected sets must appear ONLY inside rejection context
for bad,label in [('7,673.04','aggregator close set'),('6,279','2025 S&P level'),('$3.97 trillion','2025 NVDA cap')]:
    idxs=[m.start() for m in re.finditer(re.escape(bad),F['ws'])]
    ok(len(idxs)>0,'ws: rejection marker %s vanished (guard is dead)'%bad)
    for i in idxs:
        win=F['ws'][max(0,i-1400):i+900]
        ok(('rejected' in win.lower()) or ('Those are 2025 levels' in win),
           'ws: %s (%s) appears outside a rejection context'%(bad,label))
# older window-scoped guards still alive
for bad in ['232,000','$5.90']:
    idxs=[m.start() for m in re.finditer(re.escape(bad),F['ws'])]
    ok(len(idxs)>0,'ws: guard string %s vanished'%bad)
    for i in idxs:
        win=F['ws'][max(0,i-1500):i+700].lower()
        ok(('reject' in win) or ('not published' in win) or ('withheld' in win) or ('still not published' in win),
           'ws: %s appears outside a non-publication note'%bad)
# Jackson Hole must be PUBLISHED (inverted guard, per 9:36 lesson)
has('ws','August 27&ndash;29'); has('ws','Jackson Lake Lodge'); has('ws','Kevin Warsh')
has('ws','That reasoning was wrong.')
has('ws','kansascityfed.org')
# newly verified this run
has('ws','5.25%','30-year yield must now be published')
no('ws','<td class="mono" style="color:var(--mut)">not verified this run</td>')
has('ws','$79,836.71'); has('ws','$81.63')
has('ws','26.17%'); has('ws','surged 19%')
has('ws','8.7%'); has('ws','$184.32')
has('ws','203,000'); has('ws','205,500')
# sector figures rejected
for bad in ['+1.03%','1.25%</b>, Energy','Information Technology +1.03%']:
    pass
i=F['ws'].find('Information Technology +1.03%')
ok(i>0,'ws: sector rejection note missing')
ok('is not published' in F['ws'][i-260:i+400],'ws: sector figures not framed as rejected')
# scorecard: no level without corroboration
has('ws','7,675.70'); has('ws','level not corroborated this run')
# disclaimer wording (real wording, not the phantom phrase)
has('ws','Nothing here is investment advice')
ok(F['ws'].count('<li><a href=')>=25,'ws sources footer too thin')

# ---- CYBER -------------------------------------------------------------------
has('cy','CVE-2026-21962'); has('cy','CVE-2026-8452')
cnt('cy','id="kev1"',1); cnt('cy','id="kev2"',1); cnt('cy','id="kev3"',1); cnt('cy','id="kev4"',1)
has('cy',"set('kev4',d(2026,8,29))")
has('cy','callout crit','Patch Priority must carry the crit border')
# Oracle Aug 27 must appear in all three required places
ok(F['cy'].count('August 27')>=2 and 'due date <b>Aug 27</b>' in F['cy'],'cy: Oracle Aug 27 not carried in all required places')
# Citrix Aug 29 must be consistent across Top Story, Patch Priority, Vuln Watch, KEV board
for frag in ['due <b>Aug 29</b>','federal due date <b>Aug 29</b>','<b>Saturday, August 29</b>']:
    has('cy',frag,'cy: Citrix deadline missing from a required place: '+frag)
has('cy','14.1-72.61'); has('cy','13.1-63.18'); has('cy','13.1-37.272'); has('cy','watchTowr')
# Server Killers must appear ONLY as a rejected attribution
i=F['cy'].find('Server Killers')
ok(i>0,'cy: Server Killers rejection note vanished')
ok('is not published' in F['cy'][max(0,i-400):i+500],'cy: Server Killers appears outside a rejection note')
has('cy','Boston Scientific'); has('cy','8-K filing with the SEC')
has('cy','Louis Michael Gaebler'); has('cy','Ruben Ian Thomson'); has('cy','TeamPCP')
has('cy','Perth Magistrates Court'); has('cy','Checkmarx KICS'); has('cy','LiteLLM')
has('cy','18 vulnerabilities in NemoClaw and OpenShell')
# Adobe counts must not be asserted
ok('51 across 5 products' in F['cy'] and '55 across 11 products' in F['cy'] and 'are not averaged into one' in F['cy'],
   'cy: conflicting Adobe counts must be shown as unresolved')
# CVE whitelist: no invented identifiers
allow={'CVE-2026-21962','CVE-2026-64633','CVE-2026-65641','CVE-2026-12569','CVE-2026-69836','CVE-2026-68820',
       'CVE-2026-62815','CVE-2026-62893','CVE-2026-60004','CVE-2026-18963','CVE-2026-19913','CVE-2026-19912',
       'CVE-2026-73570','CVE-2026-8452','CVE-2026-72529','CVE-2026-72530','CVE-2026-33824','CVE-2026-55040',
       'CVE-2026-59310','CVE-2026-65400','CVE-2026-20349','CVE-2026-72898','CVE-2026-8037','CVE-2015-3246',
       'CVE-2015-5287','CVE-2019-1068','CVE-2021-23758','CVE-2022-0995','CVE-2026-20253'}
found=set(re.findall(r'CVE-\d{4}-\d{4,6}',F['cy']))
ok(found<=allow,'cy: NON-WHITELISTED CVE ids: %s'%(found-allow))
ok(len(found)>=20,'cy: CVE whitelist guard found only %d ids — parser may be dead'%len(found))
has('cy','BOD 26-04')
no('cy','add-date + 21 days')
ok(F['cy'].count('<li><a href=')>=30,'cy sources footer too thin')
has('cy','not a substitute for your own security review')

# ---- MMA ---------------------------------------------------------------------
has('mma','id="ufccdn"'); has('mma','Fight week')
has('mma','Umar Nurmagomedov'); has('mma','Song Yadong'); has('mma','−500'); has('mma','+380')
has('mma','Meta UFC Rankings'); has('mma','June 22, 2026')
ok('does <b>not</b> assert that the transition explains' in F['mma'],'mma: Meta rankings causal disclaimer missing')
for w in ['Alex Apodaca','Bella Mir','Guilherme Uriel','Mario Piazzon','Sean Clancy Jr.','Gary Balleto',
          'Ronald Humphrey','Alexis Miranda','Nick Galanti','Carlos Petruzzella']:
    has('mma',w,'mma: DWCS wk3 name missing: '+w)
has('mma','R1, 0:50'); has('mma','R2, 3:54'); has('mma','R1, 4:03'); has('mma','R1, 0:35')
# champions board parsed as real cells, with all four historical regressions tested
board=F['mma'][F['mma'].find('Champions Board'):]
rows=re.findall(r'<tr>(.*?)</tr>',board,re.S)
cells=[re.findall(r'<td[^>]*>(.*?)</td>',r,re.S) for r in rows]
cells=[c for c in cells if len(c)>=2]
ok(len(cells)>=11,'mma: champions parser found only %d rows — parser is dead'%len(cells))
champ=' | '.join(re.sub(r'<[^>]+>','',c[1]) for c in cells)
for bad in ['Pereira','Chimaev','vacant','Vacant','Topuria']:
    ok(bad not in champ,'mma: REGRESSION — "%s" appears in a champion cell'%bad)
for good in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Van','Shevchenko','Harrison','Dern']:
    ok(good in champ,'mma: champion missing from board: '+good)
has('mma','Cards and bouts are subject to change')
ok(F['mma'].count('<li><a href=')>=12,'mma sources footer too thin')

# ---- INDEX card <-> page lead agreement --------------------------------------
has('idx','CVE-2026-8452'); has('idx','August 29')
has('idx','217.20'); has('idx','327.22')
has('idx','Nurmagomedov'); has('idx','Contender Series')
has('idx','Read the briefing')
cnt('idx','Read the briefing',3)

# ---- chronology / tense / trap greps ----------------------------------------
for k in F:
    for trap in ['Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman','Fight Night 286','Server Killers claimed responsibility']:
        if k=='cy' and trap=='Server Killers claimed responsibility': continue
        no(k,trap,'%s TRAP: %s'%(k,trap))
no('ws','After-Hours Movers','no after-hours section before 4 PM ET')
no('mma','weights are due on August 28','stale future-tense on a released item')
no('ws','New · 9:35'); no('cy','Updated · 9:35')


# ---- freshness of tags (the 9:36 read-through lesson, now programmatic) -----
import re as _re
for k in ['cy','ws','mma']:
    stale=_re.findall(r'<span class="tag[^"]*">(?:New|Updated) · (?!11:35)[^<]*</span>',F[k])
    ok(not stale,'%s carries a stale edition stamp: %s'%(k,stale[:3]))
    bare=F[k].count('<span class="tag new">New</span>')
    ok(bare==0,'%s has %d unstamped "New" tags — every New must be dated or demoted'%(k,bare))
ok('New · 11:35' in F['cy'],'cy: the two genuinely new items must be stamped')

print('CHECKS: %d   FAILURES: %d'%(checks[0],len(fails)))
for f in fails: print('  FAIL:',f)
sys.exit(1 if fails else 0)
