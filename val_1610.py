# -*- coding: utf-8 -*-
"""Validator for the 1610 edition. python3 val_1610.py <repodir>"""
import sys, io, os, re, datetime
R = sys.argv[1]
F = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
P = {f: io.open(os.path.join(R, f), encoding='utf-8').read() for f in F}
fails, n = [], 0

def ck(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)

# --- 1. nav + masthead on all four pages
for f, h in P.items():
    for href in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
                 'mma-briefing.html', 'archive.html']:
        ck('href="%s"' % href in h, '%s: nav missing %s' % (f, href))
    for pid in ['edition', 'datestamp', 'updated']:
        ck('id="%s"' % pid in h, '%s: missing pill id=%s' % (f, pid))
    ck(h.count('class="active"') == 1, '%s: active tab count != 1' % f)
    ck('America/New_York' in h, '%s: no stamp JS' % f)
    for t in ['div', 'table', 'script']:
        ck(h.count('<%s' % t) == h.count('</%s>' % t),
           '%s: unbalanced <%s> (%d/%d)' % (f, t, h.count('<%s' % t), h.count('</%s>' % t)))

# --- 2. tldr labels + freshline on the three briefings
for f, lab in [('cyber-briefing.html', 'The Wire'),
               ('wallstreet-briefing.html', 'The Tape'),
               ('mma-briefing.html', 'Tale of the Tape')]:
    ck('<div class="tldr"><b>%s</b>' % lab in P[f], '%s: tldr label wrong' % f)
    ck('id="freshline"' in P[f], '%s: no freshline' % f)
ck('class="tldr"' not in P['index.html'], 'index: should use cards not tldr')
ck(P['index.html'].count('class="card ') == 3, 'index: card count != 3')

# --- 3. TradingView widget blocks A-F + 3 single quotes + required symbols
w = P['wallstreet-briefing.html']
for blk in ['ticker-tape', 'single-quote', 'timeline', 'stock-heatmap',
            'mini-symbol-overview', 'events']:
    ck('embed-widget-%s.js' % blk in w, 'ws: missing widget %s' % blk)
ck(w.count('embed-widget-single-quote.js') == 3, 'ws: single-quote count != 3')
for sym in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI',
            'TVC:USOIL', 'TVC:US10Y']:
    ck(sym in w, 'ws: ticker missing %s' % sym)
ck('class="livebar"' in w, 'ws: no livebar')
for other in ['index.html', 'cyber-briefing.html', 'mma-briefing.html']:
    ck('tradingview' not in P[other].lower(), '%s: live widget leaked' % other)

# --- 4. New-tag counts must be exactly cyber 0 / ws 1 / mma 0
TAG = re.compile(r'<span class="t new"[^>]*>New</span>')
for f, want in [('cyber-briefing.html', 0), ('wallstreet-briefing.html', 1),
                ('mma-briefing.html', 0)]:
    got = len(TAG.findall(P[f]))
    ck(got == want, '%s: New count %d != %d' % (f, got, want))

# --- 5. every New item must be absent from the prior snapshot
PRIOR = '2026-09-06-1540'
prior_ws = io.open(os.path.join(R, 'archive', 'wallstreet-%s.html' % PRIOR),
                   encoding='utf-8').read()
for token in ['Morningstar', 'Russell Price', 'Inflation Nowcasting']:
    ck(token not in prior_ws, 'ws: New item "%s" already in prior snapshot' % token)
    ck(token in w, 'ws: New item "%s" missing from page' % token)

# --- 6. champions board: exactly 12 rows, champion column matched, regressions forbidden
m = P['mma-briefing.html']
i = m.find('Champions Board')
tbl = m[i:m.find('</table>', i)]
rows = re.findall(r'<tr><td[^>]*>(?!<th).*?</tr>', tbl, re.S)
rows = [r for r in rows if '<th>' not in r]
ck(len(rows) == 12, 'mma: champions rows %d != 12' % len(rows))
champs = []
for r in rows:
    cells = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
    if len(cells) >= 2:
        champs.append(re.sub(r'<[^>]+>', '', cells[1]).strip())
AUTH = ['Tom Aspinall', 'Carlos Ulberg', 'Sean Strickland', 'Islam Makhachev',
        'Justin Gaethje', 'Alexander Volkanovski', 'Petr Yan', 'Joshua Van',
        'Valentina Shevchenko', 'Kayla Harrison', 'Mackenzie Dern', 'Ciryl Gane']
for a in AUTH:
    ck(any(a in c for c in champs), 'mma: champion missing from board: %s' % a)
for bad in ['Pereira', 'Chimaev', 'Topuria', 'Pantoja', 'Dvalishvili']:
    ck(not any(bad in c for c in champs), 'mma: FORBIDDEN champion on board: %s' % bad)

# --- 7. Parnasse guard: never attributed to the Contender Series (negation-exempt)
for s in re.split(r'(?<=[.!?])\s+', re.sub(r'<[^>]+>', ' ', m)):
    if 'Parnasse' in s and 'Contender Series' in s:
        ck(re.search(r'\bnot\b|\bnever\b|NOT\b', s) is not None,
           'mma: Parnasse tied to Contender Series without negation: %s' % s[:120])

# --- 8. stoppage-time refusal intact and count advanced
ck('2:25' in m and '2:35' in m, 'mma: stoppage refusal lost a figure')
ck('sixth consecutive edition' in m, 'mma: refusal run-count not advanced')
ck('2026-09-05T18:40:35' in m, 'mma: modified_time not cited')

# --- 9. KEV deadlines: countdowns recomputed from today
today = datetime.date(2026, 9, 6)
c = P['cyber-briefing.html']
for due, txt in [(datetime.date(2026, 9, 18), '(12 days left)'),
                 (datetime.date(2026, 9, 16), '(10 days left)')]:
    ck((due - today).days == int(txt.split()[0].strip('(')),
       'cyber: countdown arithmetic wrong for %s' % due)
    ck(txt in c, 'cyber: missing countdown %s' % txt)
ck('(overdue by 1 day)' in c, 'cyber: 5 Sep group not marked overdue by 1 day')
# same deadline in Patch Priority and KEV section
ck(c.count('18 September 2026') >= 2, 'cyber: 18 Sep not stated in both places')
ck(c.count('5 September 2026') >= 2, 'cyber: 5 Sep not stated in both places')

# --- 10. weekday guard on every published date
MON = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,
       'August':8,'September':9,'October':10,'November':11,'December':12}
DAY = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
pat = re.compile(r'\b(%s)\s+(\d{1,2})\s+(%s)\b' % ('|'.join(DAY), '|'.join(MON)))
for f, h in P.items():
    txt = re.sub(r'<[^>]+>', ' ', h)
    for dn, dd, mo in pat.findall(txt):
        d = datetime.date(2026, MON[mo], int(dd))
        ck(DAY[d.weekday()] == dn,
           '%s: %s %s %s is a %s' % (f, dn, dd, mo, DAY[d.weekday()]))

# --- 11. markets: verified Sept 4 closes present and internally consistent
for fig in ['7,718.60', '26,506.99', '53,414.25', '271.86', '162,000', '53,000']:
    ck(fig in w, 'ws: missing verified figure %s' % fig)
ck(abs((53686.11 - 271.86) - 53414.25) < 0.005, 'ws: Dow arithmetic')
# standing refusals must not have been quietly dropped
ck('VIX' not in w or 'no VIX' in w.lower() or 'not published' in w.lower(),
   'ws: an unsourced VIX level may have appeared')
ck('after-hours' in w.lower() or 'After-Hours' in w, 'ws: after-hours guard sentence missing')

# --- 12. index cards must echo each page tldr sentence
ix = P['index.html']
for f in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    mm = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', P[f], re.S)
    ck(mm is not None, '%s: tldr sentence unparseable' % f)
    if mm:
        sent = mm.group(1).strip()
        ck(sent in ix, 'index: card does not match %s tldr' % f)

print('checks: %d  failures: %d' % (n, len(fails)))
for x in fails:
    print('  FAIL', x)
sys.exit(1 if fails else 0)
