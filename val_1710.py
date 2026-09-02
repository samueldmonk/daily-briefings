# -*- coding: utf-8 -*-
import re,sys,os
OUT="/sessions/fervent-pensive-ramanujan/mnt/outputs"
P={n:open(os.path.join(OUT,n)).read() for n in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
IX,CY,WS,MM=P['index.html'],P['cyber-briefing.html'],P['wallstreet-briefing.html'],P['mma-briefing.html']
fails=[];n=0
def ck(name,cond):
    global n;n+=1
    if not cond: fails.append(name)
def ran(name,cond):
    # assert a guard actually matches something (guard-is-alive check)
    global n;n+=1
    if not cond: fails.append("GUARD-DEAD:"+name)

# ---- structural, all four pages
for nm,h in P.items():
    ck(nm+":doctype", h.startswith('<!DOCTYPE html>'))
    ck(nm+":5tabs", h.count('nav class="tabs"')==1 and all(x in h for x in
        ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']))
    ck(nm+":1active", h.count('class="active"')==1)
    for pid in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        ck(nm+":"+pid, pid in h)
    ck(nm+":livepill", 'pill live' in h)
    ck(nm+":stampjs", "America/New_York" in h and "Morning Edition" in h and "Afternoon Edition" in h)
    ck(nm+":freshtext", "briefings refresh every 30 minutes" in h)
    ck(nm+":balanced-body", h.count('<body>')==1 and h.count('</body>')==1)
    ck(nm+":noplaceholder", 'TKTK' not in h and 'TODO' not in h and 'XXX' not in h)
# tldr only on the three briefings, index uses cards
for nm in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    ck(nm+":tldr", 'class="tldr"' in P[nm])
ck("index:no-tldr", 'class="tldr"' not in IX)
ck("cy:label", '<b>The Wire</b>' in CY)
ck("ws:label", '<b>The Tape</b>' in WS)
ck("mm:label", '<b>Tale of the Tape</b>' in MM)

# ---- index has no live widgets
ck("index:no-widgets", 'tradingview.com' not in IX)
ck("index:3cards", IX.count('Read the briefing')==3)

# ---- wall street widget blocks A-F
for blk in ['embed-widget-ticker-tape','embed-widget-single-quote','embed-widget-timeline',
            'embed-widget-stock-heatmap','embed-widget-mini-symbol-overview','embed-widget-events']:
    ck("ws:"+blk, blk in WS)
ck("ws:3singlequotes", WS.count('embed-widget-single-quote')==3)
ck("ws:livebar", 'class="livebar"' in WS and 'LIVE QUOTES' in WS)
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck("ws:tickersym:"+sym, sym in WS)
ck("ws:notenote", 'Quotes stream live' in WS)
ck("ws:afterhours", 'After-Hours Movers' in WS)      # post-4pm run
ck("ws:scorecard", 'Weekly Scorecard' in WS)
ck("ws:disc", 'Nothing here is investment advice' in WS and 'class="disc"' in WS)

# ---- MARKETS: closes must reconcile
ck("ws:spx", 7631.47+35.13==round(7666.60,2))
ck("ws:dow", round(52766.88+295.07,2)==53061.95)
ck("ws:ndq", round(26099.77+118.06,2)==26217.83)
for lv in ['7,666.60','26,217.83','53,061.95','+295.07','+0.46%','+0.45%','+0.56%']:
    ck("ws:level:"+lv, lv in WS)
# levels must NOT appear anywhere on cyber/mma
for lv in ['7,666.60','53,061.95']:
    ck("noleak:"+lv, lv not in CY and lv not in MM)

# ---- 10-year: the disputed "highest since" must never be asserted in a table cell
tds=re.findall(r'<td[^>]*>(.*?)</td>', WS, re.S)
ran("ws:tds-exist", len(tds)>10)
for t in tds:
    ck("ws:no-highest-since-in-cell", 'highest since' not in t.lower())
ck("ws:three-descriptors", all(x in WS for x in ['November 2023','October 2023','January 2025']))
ck("ws:yield-close", '4.799%' in WS and '4.765%' in WS and '4.820%' in WS)

# ---- Dell conflict printed both ways, neither adopted alone
ck("ws:dell-both", '+13%' in WS and 'nearly 11%' in WS)
ck("ws:dell-chart", 'NYSE:DELL' in WS and 'Chart of the Day &mdash; Dell' in WS)
# AVGO four magnitudes
for m in ['&minus;3.5%','&minus;5%','&minus;6.5%','&minus;4.14%']:
    ck("ws:avgo:"+m, m in WS)
ck("ws:sector-refused", 'refused for a seventh consecutive run' in WS)

# ---- CYBER
ck("cy:banner", 'banner high' in CY and 'Threat Level' in CY)
ck("cy:stats4", CY.count('class="stat"')==4)
ck("cy:patchbox", 'callout crit' in CY and 'Patch Priority' in CY)
ck("cy:spotlight", 'Threat Actor Spotlight' in CY)
ck("cy:cvetable", 'Vulnerability Watch' in CY and '<th>CVSS</th>' in CY)
ck("cy:kev", 'CISA KEV' in CY)
# every countdown must be arithmetic from Sept 2 to the stated due date
ck("cy:mlflow-0", 'today, September 2' in CY and '0 days left' in CY)
ck("cy:9586-3", 'September 5' in CY and '3 days left' in CY)     # Sep 2 -> Sep 5 = 3
ck("cy:48710-14", 'September 16' in CY and '14 days left' in CY) # Sep 2 -> Sep 16 = 14
ck("cy:oracle-6", '6 days overdue' in CY)                        # Aug 27 -> Sep 2 = 6
# patch priority CVE must match the KEV section's same deadline
ck("cy:patch-matches-kev", 'CVE-2026-64849' in CY.split('Patch Priority')[1][:1200] and 'CVE-2026-64849' in CY.split('CISA KEV')[1])
# no assumed 3-week window
ck("cy:no-22-01-assumption", 'BOD 26-04' in CY and 'superseded' in CY)
# every 9.8 must be attributed/refused within 700 chars
# narrowed: only a "9.8" used as a CVSS needs attribution; a "9.8 million records" is a count.
cvss98=[m for m in re.finditer(r'9\.8', CY) if 'million' not in CY[m.start():m.start()+40]]
ran("cy:9.8-guard-alive", len(cvss98)>0)
for m in cvss98:
    seg=CY[max(0,m.start()-700):m.start()+700]
    ck("cy:9.8-attributed@%d"%m.start(), ('reported' in seg or 'attributed' in seg or 'not adopted' in seg))
# Nevada must only appear beside the refusal language, never as a breach heading
h4s=re.findall(r'<h4[^>]*>(.*?)</h4>', CY, re.S)
ran("cy:h4-exist", len(h4s)>3)
for t in h4s: ck("cy:no-nevada-heading", 'Nevada' not in t)
for m in re.finditer(r'Nevada', CY):
    ck("cy:nevada-refusal@%d"%m.start(), 'refused on sight' in CY[max(0,m.start()-600):m.start()+600])
ran("cy:nevada-guard-alive", 'Nevada' in CY)
# Entra correction must be present and must NOT call it exploited
ck("cy:entra-corrected", 'changed the exploitation status' in CY)
entra=CY.split('CVE-2026-69836')[1][:700] if 'CVE-2026-69836' in CY else ''
ran("cy:entra-seg", len(entra)>100)
ck("cy:entra-not-exploited", 'not exploited in the wild' in entra)
# Switchvox patch date and CVSS
ck("cy:9586-cvss", 'CVSS 4.0' in CY and '9.3' in CY)
ck("cy:9586-patch", '8.4.0.2' in CY and 'July 14, 2026' in CY)

# ---- MMA
ck("mm:countdown", 'ufccdn' in MM and "2026-09-05T12:00:00-04:00" in MM)
ck("mm:cdn-elapsed", 'Fight week' in MM)
ck("mm:top", 'Top Story' in MM)
ck("mm:cards", 'Upcoming Cards' in MM)
ck("mm:odds", '&minus;667' in MM and '+417' in MM)
ck("mm:results", 'Last Event' in MM and 'KO (uppercut), Round 2, 1:48' in MM)
ck("mm:bonuses", 'Performance of the Night' in MM and 'Fight of the Night' in MM)
ck("mm:prospects", 'Prospect Watch' in MM)
ck("mm:around", 'Around the Sport' in MM)
ck("mm:rankbiz", 'Rankings &amp; Business' in MM)
ck("mm:champs", 'Champions Board' in MM)
ck("mm:disc", 'subject to change' in MM)
# champions board: correct names in the champion cells only
cb=MM.split('Champions Board')[1].split('</table>')[0]
ran("mm:cb-seg", len(cb)>500)
wins=re.findall(r'<td class="win">(.*?)</td>', cb)
ck("mm:cb-12-13cells", 11<=len(wins)+1<=13)
ck("mm:cb-strickland", 'Sean Strickland' in wins)
ck("mm:cb-no-chimaev-champ", not any('Chimaev' in w for w in wins))
ck("mm:cb-ulberg", 'Carlos Ulberg' in wins)
ck("mm:cb-no-pereira-champ", not any('Pereira' in w for w in wins))
ck("mm:cb-volk", 'Alexander Volkanovski' in wins)
ck("mm:cb-gaethje", 'Justin Gaethje' in wins)
ck("mm:cb-van", 'Joshua Van' in wins)
ck("mm:cb-vacant-wfw", 'Vacant' in cb)
ck("mm:cb-24th", 'twenty-fourth time' in MM)
# Parnasse provenance
ck("mm:parnasse-spelling", 'Salahdine Parnasse' in MM and 'Saladhine' not in MM)
ck("mm:parnasse-not-dwcs", 'did <u>not</u> come through Dana White' in MM)
for m in re.finditer(r'Parnasse', MM):
    seg=MM[max(0,m.start()-900):m.start()+900]
    ck("mm:parnasse-no-dwcs-claim@%d"%m.start(),
       not re.search(r'earned his contract on Dana White', seg))
ran("mm:parnasse-guard-alive", 'Parnasse' in MM)
# Hooker record not a fight count
ck("mm:hooker-record", '24-14 as a professional' in MM)
ck("mm:hooker-no-fightcount", 'fought 24 times' not in MM)
# Dariush descriptor
ck("mm:dariush", 'title challenger' not in MM)
# dates chronological: nothing "upcoming" already past
for d in ['Sept 5','Sept 12','Sept 19','Sept 26']:
    ck("mm:upcoming:"+d, d in MM)
ck("mm:last-event-past", 'August 29' in MM)

# ---- index card summaries must match each page's tldr sentence
def tldr(h):
    return h.split('class="tldr"')[1].split('<span>')[1].split('</span>')[0]
for nm,key in [('cyber-briefing.html','Switchvox'),('wallstreet-briefing.html','Dell'),('mma-briefing.html','Parnasse')]:
    t=tldr(P[nm])
    ck("index-echoes-"+nm, t in IX)
ran("index-echo-alive", 'Switchvox' in IX)


# ==== guards added after the 5:20 PM read-through (defect classes it caught, guards had not)
import datetime
# (a) any weekday named next to a date on any page must be the real weekday
MONTHS={m:i+1 for i,m in enumerate(['January','February','March','April','May','June','July','August',
 'September','October','November','December'])}
WD=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
pat=re.compile(r'(%s),?\s+(%s)\s+(\d{1,2})'%('|'.join(WD),'|'.join(MONTHS)))
hits=0
for nm,h in P.items():
    txt=re.sub(r'<[^>]+>',' ',h)
    for m in pat.finditer(txt):
        hits+=1
        d=datetime.date(2026,MONTHS[m.group(2)],int(m.group(3)))
        ck("weekday:%s:%s"%(nm,m.group(0)), d.strftime('%A')==m.group(1))
ran("weekday-guard-alive", hits>0)
# (b) Sept 5 must never be called a Friday anywhere; Sept 2 must never be called anything but Wednesday
for nm,h in P.items():
    ck("no-fri-sep5:"+nm, not re.search(r'Friday[^.]{0,25}(Sept(ember)?\.? ?5|5 Sept)', re.sub(r'<[^>]+>',' ',h)))
# (c) the Switchvox KEV add-date must agree between headline and body on the cyber page
ck("cy:kev-adddate-agrees", 'flagged yesterday' not in CY and 'added to CISA' in CY and 'on <b>September 2</b>' in CY)
# (d) Palo Alto must not carry a fiscal-quarter label (sources say only "quarterly results")
ck("ws:panw-no-fiscal-label", not re.search(r'fiscal Q[1-4][^.]{0,60}(topped|beat)[^.]{0,60}(Wall Street|expectations)', WS))
ran("ws:panw-present", 'Palo Alto Networks' in WS)
# (e) the $7.04 Dell figure must always be qualified as before certain costs
for m in re.finditer(r'\$7\.04', WS):
    ck("ws:704-qualified@%d"%m.start(), 'before certain costs' in WS[max(0,m.start()-200):m.start()+120])
ran("ws:704-alive", '$7.04' in WS)
# (f) MMA prose must not assert a day-count that fights the live countdown
ck("mm:no-stale-daycount", 'three days out' not in MM and 'three days out' not in IX)

print("checks:",n,"failures:",len(fails))
for f in fails: print("  FAIL",f)
sys.exit(1 if fails else 0)

