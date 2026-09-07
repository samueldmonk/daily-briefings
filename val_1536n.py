# -*- coding: utf-8 -*-
import io,re,sys,datetime
P={k:io.open(f,encoding='utf-8').read() for k,f in
   [('IX','index.html'),('CY','cyber-briefing.html'),('WS','wallstreet-briefing.html'),('MM','mma-briefing.html')]}
L={k:v.lower() for k,v in P.items()}
S={k:io.open('archive/%s-2026-09-07-1518.html'%k,encoding='utf-8').read() for k in ['cyber','wallstreet','mma']}
n=[0]; fails=[]
def ck(name,cond):
    n[0]+=1
    if not cond: fails.append(name)

for k,s in P.items():
    ck('%s h2 balance'%k, s.count('<h2')==s.count('</h2>'))
    ck('%s div balance'%k, s.count('<div')==s.count('</div>'))
    ck('%s tr balance'%k, s.count('<tr')==s.count('</tr>'))
    ck('%s td balance'%k, s.count('<td')==s.count('</td>'))
    ck('%s p balance'%k, s.count('<p')==s.count('</p>'))
    ck('%s span balance'%k, s.count('<span')==s.count('</span>'))
    ck('%s table balance'%k, s.count('<table')==s.count('</table>'))
    ck('%s no empty h2'%k, '<h2 class="sec"></h2>' not in s)
    ck('%s stamp ids'%k, all(('id="%s"'%i) in s for i in ['edition','datestamp','updated','freshline']))
    ck('%s five-tab nav'%k, all(h in s for h in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']))

for k in ['CY','WS','MM','IX']:
    ck('%s no undemoted new-items claim'%k, not re.search(r'the (two|three|four) new items in this edition', L[k]))
    ck('%s no broken demotion grammar'%k, 'item the 3:05' not in L[k] and 'return the 3:05' not in L[k] and 'read the 3:05' not in L[k])

ck('CY tag count 2', P['CY'].count('class="t new"')==2)
ck('WS tag count 1', P['WS'].count('class="t new"')==1)
ck('MM tag count 0', P['MM'].count('class="t new"')==0)
ck('IX tag count 0', P['IX'].count('class="t new"')==0)
ck('ledger totals stated', all('2 cyber + 1 markets + 0 MMA = 3' in P[k] for k in ['CY','WS','MM']))
ck('CY ledger says 2', 'ledger &mdash; 2 tags' in P['CY'])
ck('WS ledger says 1', 'ledger &mdash; 1 tag on this page' in P['WS'])
ck('MM ledger says 0', 'ledger &mdash; 0 tags' in P['MM'])
ck('ledger stamped 3:35', all('3:35&nbsp;PM ET edition' in P[k] for k in ['CY','WS','MM']))

for t in ['84353','84352','84325','WebGL','DataTransfer','Shared Tab Groups','7977.75','58641','62815','58612','50376']:
    ck('novel cyber %s'%t, t not in S['cyber'])
for t in ['14.7','24.6','energy component']:
    ck('novel ws %s'%t, t not in S['wallstreet'])
ck('mma prev snapshot had 2 tags', S['mma'].count('class="t new"')==2)

ck('CY 84353 row', 'CVE-2026-84353' in P['CY'])
ck('CY 84352 row', 'CVE-2026-84352' in P['CY'])
ck('CY 84325 row', 'CVE-2026-84325' in P['CY'])
ck('CY supersede stated', 'a <i>later</i> build than the .75' in P['CY'])
ck('CY no countdown in chrome rows', not re.search(r'CVE-2026-84353.{0,2600}?days left', P['CY'], re.S))
ck('CY chrome not exploited', 'Nothing here is exploited and nothing is in KEV' in P['CY'])
ck('CY no invented CVSS', 'no return read this run stated one' in P['CY'])
ck('CY 84325 High', 'rate 84325 <b>High</b>' in P['CY'])
ck('CY refuses grouping', 'that grouping is <b>refused</b>' in P['CY'])
ck('CY sequence', '25 August' in P['CY'] and '327' in P['CY'] and '7977.64' in P['CY'])
ck('CY zero-day intact', 'CVE-2026-85046' in P['CY'] and '152.0.7977.82' in P['CY'])
ck('CY four MSRC CVEs', all(c in P['CY'] for c in ['CVE-2026-58641','CVE-2026-62815','CVE-2026-58612','CVE-2026-50376']))
ck('CY refuses EST', 'is <b>2:00&nbsp;PM ET</b> on daylight time' in P['CY'])
ck('CY refuses template', 'not adopted' in P['CY'] and '9 CVEs, 9 Critical' in P['CY'])
ck('CY ShieldBreak expected', 'expected rather than promised' in P['CY'])
ck('CY tldr carries android qualifier', 'specifies Chrome on Android' in P['CY'])
ck('IX card carries android qualifier', 'specified on <b>Android</b>' in P['IX'])
ck('CY PaperCut lead', 'PaperCut' in P['CY'] and '14 September' in P['CY'])
ck('CY disclaimer', 'informational' in L['CY'] or 'not security advice' in L['CY'] or 'disclaim' in L['CY'])

ck('WS 14.7', '14.7% year over year in July' in P['WS'])
ck('WS 24.6', '24.6' in P['WS'])
ck('WS july labelled', 'July figures, not a forecast' in P['WS'] or 'July readings, not a forecast' in P['WS'])
ck('WS refuses 91.30', '$91.30' in P['WS'] and 'refused' in L['WS'])
ck('WS refuses 95.52', '$95.52' in P['WS'])
ck('WS 96.28 held', '$96.28' in P['WS'])
ck('WS no monday settlement', 'no monday settlement' in L['WS'])
ck('WS markets shut', 'shut all day for Labor Day' in P['WS'])
ck('WS reopen', '9:30&nbsp;AM ET Tuesday' in P['WS'])
ck('WS three halts', '1:30&nbsp;PM ET' in P['WS'] and '2:30&nbsp;PM ET' in P['WS'] and '1:00&nbsp;PM ET' in P['WS'])
ck('WS halt past tense', 'have <b>all halted too</b>' in P['WS'] or 'have all halted since' in P['WS'])
ck('WS two-hours claim only inside its correction',
   ('two hours of matched trading left' not in P['WS'])
   or ('that sentence was true when it was written and false ninety minutes later' in P['WS']))
ck('WS halt elapsed restamped this edition', 'about two and a half hours in the past' in P['WS'])
ck('WS halt elapsed not stale', 'about an hour and a quarter in the past' not in P['WS'])
ck('WS nowcast not retagged', '3.38' in P['WS'] and 're-tagged' in P['WS'])
ck('WS no single brent level', 'no single Brent level is asserted' in P['WS'])
for b in ['embed-widget-ticker-tape','embed-widget-single-quote','embed-widget-timeline',
          'embed-widget-stock-heatmap','embed-widget-mini-symbol-overview','embed-widget-events']:
    ck('WS widget %s'%b, b in P['WS'])
ck('WS disclaimer', 'investment advice' in L['WS'])

ck('MM zero-new stated', 'There is no new MMA item this edition' in P['MM'])
ck('MM refuses lopes2', 'Lopes 2' in P['MM'] and 'already happened' in P['MM'])
ck('MM refuses gp booking', 'no Gaethje&ndash;Pimblett booking is printed' in P['MM'])
ck('MM 325 date', '31 January 2026' in P['MM'])
ck('MM no overclaim about 325', 'and this page carries the result' not in P['MM'])
ck('MM hooker skid', 'three-fight skid' in P['MM'] or 'three straight losses' in P['MM'])
ck('MM hooker aug2024', 'August 2024' in P['MM'])
ck('MM parnasse spelling', 'Salahdine Parnasse' in P['MM'] and 'Saladhine' not in P['MM'])
ck('MM countdown el', 'ufccdn' in P['MM'])
ck('MM disclaimer', 'subject to change' in L['MM'])

CH=P['MM'][P['MM'].find('Champions Board'):]
CH=CH[:CH.find('</table>')]
rows=re.findall(r'<tr>(.*?)</tr>',CH,re.S)
def champ(div):
    for r in rows:
        cells=[re.sub('<[^>]+>','',c) for c in re.findall(r'<td.*?>(.*?)</td>',r,re.S)]
        if cells and cells[0].strip().lower().startswith(div.lower()): return cells[1] if len(cells)>1 else ''
    return ''
for div,who in [('Heavyweight','Aspinall'),('Light Heavyweight','Ulberg'),('Middleweight','Strickland'),
                ('Welterweight','Makhachev'),('Lightweight','Gaethje'),('Featherweight','Volkanovski'),
                ('Bantamweight','Yan'),('Flyweight','Van')]:
    ck('champ %s = %s'%(div,who), who in champ(div))
ck('champ LHW not Pereira','Pereira' not in champ('Light Heavyweight'))
ck('champ MW not Chimaev','Chimaev' not in champ('Middleweight'))
ck('champ LW not Topuria','Topuria' not in champ('Lightweight'))
ck('champ FW not vacant','Vacant' not in champ('Featherweight'))

ck('IX three cards', P['IX'].count('<h3>')==3)
ck('IX cyber card', '84353' in P['IX'] and '152.0.7977.82' in P['IX'] and '14 September' in P['IX'])
ck('IX ws card', '14.7' in P['IX'] and '24.6' in P['IX'] and '9:30&nbsp;AM ET Tuesday' in P['IX'])
ck('IX mma card', 'No new MMA item' in P['IX'] and 'UFC&nbsp;325' in P['IX'])
ck('IX no stale cyber summary', 'No new item in the 3:05' not in P['IX'])
ck('IX no live widgets', 'tradingview' not in L['IX'])

for due,days in [('14 September',7),('16 September',9),('18 September',11)]:
    ck('countdown %s = %d'%(due,days), ('%d days left'%days) in P['CY'])

print("CHECKS: %d   FAILURES: %d"%(n[0],len(fails)))
for f in fails: print("  FAIL:",f)
sys.exit(1 if fails else 0)
