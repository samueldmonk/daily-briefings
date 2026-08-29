# -*- coding: utf-8 -*-
import io, re, sys
F = ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
S = {p: io.open(p, encoding='utf-8').read() for p in F}
def txt(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    import html as H
    return re.sub(r'\s+', ' ', H.unescape(s))
T = {p: txt(S[p]) for p in F}
n = [0]; fails = []
def ck(cond, msg):
    n[0] += 1
    if not cond: fails.append(msg)

# --- structure: nav, masthead ids, self-stamp ---
for p in F:
    for h in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"' % h in S[p], '%s: nav missing %s' % (p, h))
    for i in ['edition','datestamp','updated']:
        ck('id="%s"' % i in S[p], '%s: missing id %s' % (p, i))
    ck('America/New_York' in S[p], '%s: no self-stamp' % p)
    ck('Morning Edition' in S[p] and 'Midday Edition' in S[p], '%s: edition buckets' % p)
    # freshness stamp
    ck('Data as of 1:05 PM ET' in S[p], '%s: freshline not stamped 1:05' % p)
    ck('Data as of 12:35 PM ET' not in S[p], '%s: STALE 12:35 freshline' % p)
    ck('12:35 PM ET</span>' not in S[p], '%s: stale masthead 12:35' % p)

# --- widgets: only on wallstreet ---
W = ['embed-widget-ticker-tape','embed-widget-single-quote','embed-widget-timeline',
     'embed-widget-stock-heatmap','embed-widget-mini-symbol-overview','embed-widget-events']
for w in W: ck(w in S['wallstreet-briefing.html'], 'ws: missing widget %s' % w)
for p in ['index.html','cyber-briefing.html','mma-briefing.html']:
    for w in W: ck(w not in S[p], '%s: widget leaked %s' % (p, w))
ck('TVC:USOIL' in S['wallstreet-briefing.html'], 'ws: oil missing')
ck('TVC:US10Y' in S['wallstreet-briefing.html'], 'ws: US10Y missing')
ck('NASDAQ:PYPL' in S['wallstreet-briefing.html'], 'ws: chart-of-day changed off PYPL')

# --- markets: closes + reconciliation ---
ws = T['wallstreet-briefing.html']
for f in ['7,711.76','26,402.42','53,559.99','0.25%','0.52%','0.02%']:
    ck(f in ws, 'ws: missing close figure %s' % f)
ck(abs((53559.99+9.45)/53559.99*100 - 100 - 0.01764) < 0.005, 'ws: Dow reconciliation')
ck('7,673.04' not in ws, 'ws: forbidden 7,673.04 reappeared')
ck('After-Hours' not in ws and 'After Hours' not in ws, 'ws: after-hours block present on a weekend')
ck('as of ~' not in ws, 'ws: intraday as-of on a closed market')
ck('twelfth time' in ws, 'ws: twelfth-verification not stated')
ck('second consecutive check of that breadth' in ws, 'ws: breadth framing missing')
ck('the second consecutive check to return all three levels' not in ws, 'ws: retired redundant phrasing present')
ck('contested' in ws, 'ws: contested-December marking lost')
ck('Kalshi' in ws and '48%' in ws, 'ws: Kalshi post-speech read lost')
ck('4.45' in ws, 'ws: Nvidia precise figure lost')

# --- cyber: ServiceNow family ---
cy = T['cyber-briefing.html']
for c in ['CVE-2026-18885','CVE-2026-18886','CVE-2026-74820','CVE-2026-6876','CVE-2026-6875']:
    ck(c in cy, 'cy: missing %s' % c)
ck(cy.count('10.0') >= 3, 'cy: three CVSS 10.0 not present')
ck('8.7' in cy, 'cy: 6876 CVSS 8.7 missing')
ck('not currently aware of exploitation' in cy, 'cy: vendor no-exploitation statement missing')
ck('August 27' in cy, 'cy: advisory date missing')
# 6875/6876 must not be collapsed: each appears with its own status near it
for cve, must in [('CVE-2026-6875','exploited'), ('CVE-2026-6876','not exploited')]:
    idxs = [m.start() for m in re.finditer(re.escape(cve), cy)]
    ck(bool(idxs), 'cy: %s absent' % cve)
    for i in idxs:
        ck(must in cy[max(0,i-420):i+420], 'cy: %s not framed as %s' % (cve, must))
ck('6875 is exploited and old; 6876 is new and not exploited' in cy, 'cy: explicit pair distinction missing')
ck('does not carry 6875 as a row' in cy, 'cy: 6875 row-exclusion framing missing')
ck('recorded, not resolved' in cy, 'cy: KB-vs-trade discrepancy framing missing')
ck('self-hosted' in cy.lower(), 'cy: self-hosted exposure note missing')
# no false KEV claim for ServiceNow
sn = cy[cy.find('CVE-2026-18885'):cy.find('CVE-2026-18885')+3000]
ck('not KEV-listed' in sn or 'not KEV' in sn, 'cy: ServiceNow rows must state not-KEV')
# KEV board intact
ck('BOD 26-04' in cy, 'cy: BOD 26-04 framing lost')
ck('BOD 22-01' in cy, 'cy: BOD 22-01 reference lost')
for c in ['CVE-2015-3246','CVE-2015-5287','CVE-2019-1068','CVE-2021-23758','CVE-2022-0995','CVE-2026-8452']:
    ck(c in cy, 'cy: KEV cve %s lost' % c)
# Oracle still not carried
for i in [m.start() for m in re.finditer(r'CVE-2026-21962', cy)]:
    ck('not carried' in cy[max(0,i-420):i+420], 'cy: Oracle 21962 lost its not-carried frame')
ck('unforgivable' in cy, 'cy: CISA review family lost')
ck('McKesson' in cy and '284 million' in cy, 'cy: McKesson lead lost')
ck('records, not people' in cy, 'cy: McKesson records-vs-people guard lost')
ck('Boston Scientific' in cy, 'cy: Boston Scientific lost')

# --- mma: champions board + standing corrections ---
mm = T['mma-briefing.html']
CH = ['Tom Aspinall','Ciryl Gane','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
      'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison','Mackenzie Dern']
for c in CH: ck(c in mm, 'mma: champion missing %s' % c)
for bad, frames in [('Pereira', ['vacat','interim','KO2','superseded','regression','no longer','lost']),
                    ('Chimaev', ['Split decision','split decision','superseded','regression','no longer','took the belt'])]:
    for i in [m.start() for m in re.finditer(bad, mm)]:
        w = mm[max(0,i-420):i+420]
        ck(any(f in w for f in frames), 'mma: %s appears without corrective frame' % bad)
ck('vacant' not in mm.lower() or 'not vacant' in mm.lower() or 'vacancy' in mm.lower(), 'mma: unframed vacancy')
ck('UFC 333' in mm and 'October 24' in mm, 'mma: UFC 333 family lost')
ck('Dvalishvili' in mm, 'mma: trilogy co-main lost')
ck('Song' in mm and 'Umar Nurmagomedov' in mm, 'mma: main event lost')
ck('knockout (punch)' in mm.lower() or 'KO (Punch)' in mm, 'mma: official method lost')
ck('$400,000' in mm or '$400K' in mm, 'mma: bonus total lost')
ck('Jon Jones' in mm, 'mma: Jon Jones item lost')
ck('at cageside' not in mm, 'mma: forbidden unsourced "at cageside"')
ck('Gaethje' in mm and ('nothing is booked' in mm or 'no title defence scheduled' in mm or 'not expected' in mm),
   'mma: idle-belt family lost')
ck('Salkilld' not in mm or 'Gamrot' in mm, 'mma: Salkilld without latest fight')

# --- index mirrors tldrs ---
for p, label in [('cyber-briefing.html','The Wire'), ('wallstreet-briefing.html','The Tape'), ('mma-briefing.html','Tale of the Tape')]:
    m = re.search(r'<div class="tldr"><b>%s</b>\s*<span>(.*?)</span></div>' % re.escape(label), S[p], re.S)
    ck(m is not None, 'index: no tldr found on %s' % p)
    if m:
        ck(m.group(1) in S['index.html'], 'index: card does not mirror %s tldr' % label)

# --- footers: absolute, no duplicate hrefs, minimum links ---
for p, mn in [('cyber-briefing.html',24), ('wallstreet-briefing.html',24), ('mma-briefing.html',24)]:
    i = S[p].find('Sources checked this run')
    ck(i > 0, '%s: no sources footer' % p)
    hrefs = re.findall(r'href="(https?://[^"]+)"', S[p][i:])
    ck(len(hrefs) >= mn, '%s: only %d source links' % (p, len(hrefs)))
    ck(len(hrefs) == len(set(hrefs)), '%s: duplicate source hrefs: %s' % (p, [h for h in set(hrefs) if hrefs.count(h) > 1]))
    ck(all(h.startswith('http') for h in hrefs), '%s: relative source href' % p)

# --- CVE well-formedness ---
allcve = set(re.findall(r'CVE-\d{4}-\d{4,6}', S['cyber-briefing.html']))
ck(len(allcve) >= 15, 'cy: CVE liveness (%d)' % len(allcve))
for c in allcve: ck(re.match(r'^CVE-(19|20)\d{2}-\d{4,6}$', c) is not None, 'cy: malformed %s' % c)

print("CHECKS: %d   FAILURES: %d" % (n[0], len(fails)))
for f in fails: print("  FAIL:", f)
sys.exit(1 if fails else 0)
