# -*- coding: utf-8 -*-
import io,re,sys
F={f:io.open(f,encoding='utf-8').read() for f in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
fails=[];checks=[0]
def ck(cond,msg):
    checks[0]+=1
    if not cond: fails.append(msg)

# --- structural, all four pages ---
for f,s in F.items():
    for href in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck(('href="%s"'%href) in s, '%s: missing nav link %s'%(f,href))
    for i in ['id="edition"','id="datestamp"','id="updated"']:
        ck(i in s,'%s: missing %s'%(f,i))
    ck("Intl.DateTimeFormat" in s,'%s: missing self-stamp JS'%f)
    ck('Midday Edition' in s,'%s: missing edition bucket'%f)
    ck(s.rstrip().endswith('</html>'),'%s: truncated'%f)
    # freshness: no New/Updated tag stamped other than 12:38
    for m in re.findall(r'class="tag new">([^<]*)</span>',s):
        ck('12:38' in m, '%s: stale edition stamp %r'%(f,m))
    ck('class="tag new">New</span>' not in s,'%s: bare unstamped New tag'%f)

for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    ck('class="tldr"' in F[f],'%s: missing tldr'%f)
    ck('id="freshline"' in F[f],'%s: missing freshline'%f)

# --- trap greps (never publish) ---
for f,s in F.items():
    for trap in ['Shamil Yakhyaev','Cody Salkilld','Abdul-Rakhman']:
        ck(trap not in s,'%s: TRAP %s'%(f,trap))

# --- champions board parsed as real cells ---
mma=F['mma-briefing.html']
tbl=mma[mma.find('<h2 class="sec">Champions Board'):]
tbl=tbl[:tbl.find('</table>')]
rows=re.findall(r'<tr><td>([^<]+)</td><td>(.*?)</td><td>(.*?)</td></tr>',tbl,re.S)
ck(len(rows)>=11,'champions board rows=%d (<11)'%len(rows))
champcells=' | '.join(r[1] for r in rows)
for bad,div in [('Pereira','Light Heavyweight'),('Chimaev','Middleweight'),('Topuria','Lightweight'),('vacant','any')]:
    ck(bad.lower() not in champcells.lower(),'CHAMPION REGRESSION in champion cell: %s'%bad)
for good in ['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje','Alexander Volkanovski','Petr Yan','Joshua Van']:
    ck(good in champcells,'champions board missing %s'%good)

# --- CVE whitelist ---
cy=F['cyber-briefing.html']
allow={'CVE-2026-21962','CVE-2026-8452','CVE-2026-19490','CVE-2026-64633','CVE-2026-65641',
 'CVE-2026-12569','CVE-2026-69836','CVE-2026-60004','CVE-2026-68820','CVE-2026-73570',
 'CVE-2015-3246','CVE-2015-5287','CVE-2019-1068','CVE-2021-23758','CVE-2022-0995',
 'CVE-2026-72529','CVE-2026-72530','CVE-2026-33824','CVE-2026-55040','CVE-2026-59310',
 'CVE-2026-65400','CVE-2026-20349','CVE-2026-72898','CVE-2026-8037','CVE-2026-3055',
 'CVE-2026-50751','CVE-2026-20253','CVE-2026-58136','CVE-2026-25256','CVE-2026-54918',
 'CVE-2026-9061','CVE-2026-18963','CVE-2026-19912','CVE-2026-19913','CVE-2026-62815','CVE-2026-62893'}
found=set(re.findall(r'CVE-\d{4}-\d{4,6}',cy))
ck(len(found)>=20,'CVE liveness: only %d ids found'%len(found))
for c in sorted(found-allow): ck(False,'CVE not in whitelist: %s'%c)

# --- KEV / deadline consistency ---
ck(cy.count('August 29')+cy.count('Aug 29')>=4,'Aug 29 must appear in >=4 places (got %d)'%(cy.count('August 29')+cy.count('Aug 29')))
for i in ['id="kev1"','id="kev4"','id="kev5"','id="kev6"']: ck(i in cy,'cyber: missing %s'%i)
for c in ["set('kev1',d(2026,8,27))","set('kev4',d(2026,8,29))","set('kev5',d(2026,8,29))","set('kev6',d(2026,9,9))"]:
    ck(c in cy,'cyber: missing countdown %s'%c)
ck('September 9' in cy,'cyber: Sept 9 deadline missing')
ck('CVE-2019-1068' in cy,'cyber: CVE-2019-1068 missing')

# --- new cyber facts present ---
for t in ['140,000','21 countries','SNOWLIGHT','more than 100 countries','ATF','Qilin','1,900','Nutex Health','28 facilities across 12 US states','8-K']:
    ck(t in cy,'cyber: missing %r'%t)
# rejections still window-scoped
ck('Server Killers' not in cy or 'no group has claimed' in cy,'cyber: Server Killers not scoped to rejection')

# --- markets ---
ws=F['wallstreet-briefing.html']
for t in ['400.29','1.53%','208.48','0.39%','9.48%','21.04%','17.93%','203,000','4.65%']:
    ck(t in ws,'ws: missing %r'%t)
ck('Four index reads' in ws,'ws: reconciliation count line missing')
# the four-read list must actually list four Dow and four Nasdaq reads
para=ws[ws.find('Four index reads'):ws.find('Four index reads')+1600]
for v in ['169.90','217.20','147.67','208.48','300.97','327.22','279.61','400.29']:
    ck(v in para,'ws: reconciliation list missing %s'%v)
# Jackson Hole guard (INVERTED: must be published with the admission)
ck('Jackson Hole' in ws,'ws: Jackson Hole must be PUBLISHED')
ck('That reasoning was wrong.' in ws,'ws: Jackson Hole admission missing')
# aggregator rejections window-scoped
for v,scope in [('7,673.04','rejected'),('6,279','2025 levels'),('$3.97 trillion','2025 levels'),('232,000','rejected'),('$5.90','not published')]:
    i=ws.find(v)
    ck(i!=-1,'ws: %s window missing'%v)
    if i!=-1: ck(scope.lower() in ws[max(0,i-1400):i+1400].lower(),'ws: %s not scoped to a rejection'%v)
ck('ended the session slightly lower' in ws,'ws: second aggregator rejection missing')
# index.html must not carry the stale lead figures
ck('147.67' not in F['index.html'],'index: stale 147.67')
ck('279.61' not in F['index.html'],'index: stale 279.61')
ck('400.29' in F['index.html'],'index: fresh figure missing')

# --- mma ---
for t in ['$340,000','$170,000','Curtis Blaydes','one-time interim heavyweight title challenger','Josh Hokit','Renato Moicano','Brian Ortega','Gregory Rodrigues','Nurmagomedov','Song Yadong','August 29']:
    ck(t in mma,'mma: missing %r'%t)
ck('ufccdn' in mma,'mma: countdown element missing')
ck('−500' in mma and '−470' in mma,'mma: odds spread missing')
ck('all three lines' not in mma,'mma: false "-500 across all three lines" claim resurfaced')

# --- index card summaries must match the page tldrs ---
idx=F['index.html']
for f,label in [('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]:
    m=re.search(r'<div class="tldr"><b>'+label+r'</b> <span>(.*?)</span></div>',F[f],re.S)
    ck(bool(m),'%s: tldr unparsed'%f)
    if m: ck(m.group(1) in idx,'index: card summary does not match %s tldr'%f)

# --- widget blocks ---
for w in ['embed-widget-ticker-tape','embed-widget-single-quote','embed-widget-timeline',
          'embed-widget-stock-heatmap','embed-widget-mini-symbol-overview','embed-widget-events']:
    ck(w in ws,'ws: missing widget %s'%w)
ck(ws.count('embed-widget-single-quote')==3,'ws: need 3 single-quote widgets')
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(sym in ws,'ws: ticker tape missing %s'%sym)
for w in ['embed-widget']:
    ck(w not in idx,'index: must have no live widgets')

print("validate_1238: %d checks, %d failures"%(checks[0],len(fails)))
for x in fails: print("  FAIL:",x)
sys.exit(1 if fails else 0)
