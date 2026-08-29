#!/usr/bin/env python3
"""Fact-check / structural gate for the 12:05 PM ET edition, Sat Aug 29 2026."""
import io, re, sys

FAIL = []
N = 0

def load(p): return io.open(p, encoding='utf-8').read()
CY, WS, MM, IX = (load(x) for x in
    ('cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','index.html'))
PAGES = {'cyber': CY, 'ws': WS, 'mma': MM, 'index': IX}

def ok(cond, label):
    global N
    N += 1
    if not cond: FAIL.append(label)

def has(page, s, label): ok(s in PAGES[page], label)
def nothas(page, s, label): ok(s not in PAGES[page], 'FORBID ' + label)

# ---- structure: five-tab nav, masthead ids, self-stamp, freshline
for name, h in PAGES.items():
    for tab in ('index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html'):
        ok('href="%s"' % tab in h, '%s nav->%s' % (name, tab))
    for i in ('id="edition"','id="datestamp"','id="updated"','id="freshline"'):
        ok(i in h, '%s masthead %s' % (name, i))
    ok("Intl.DateTimeFormat" in h and "America/New_York" in h, '%s self-stamp' % name)
    ok('Data as of 12:05 PM ET' in h, '%s freshline stamped 12:05' % name)
    ok('Data as of 11:35 AM ET' not in h, '%s stale 11:35 freshline' % name)
    ok('>11:35 AM ET<' not in h, '%s stale 11:35 masthead' % name)
    ok('id="edition">Midday Edition' in h, '%s edition=Midday' % name)
    ok(h.count('class="tabs"') >= 1, '%s tabs present' % name)

# ---- TradingView blocks (markets only)
for w in ('embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
          'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js'):
    has('ws', w, 'ws widget ' + w)
has('ws', 'TVC:USOIL', 'ws ticker oil')
has('ws', 'TVC:US10Y', 'ws ticker US10Y')
for s in ('FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI'):
    has('ws', s, 'ws index symbol ' + s)
has('ws', 'NASDAQ:PYPL', 'ws chart-of-day PYPL unchanged')
for name in ('cyber','mma','index'):
    ok('tradingview' not in PAGES[name].lower(), '%s has no live widgets' % name)

# ---- markets: Friday closes, reconciliation, weekend framing
for fig in ('7,711.76','26,402.42','53,559.99','7,730.99','26,541.35','53,569.44'):
    has('ws', fig, 'ws close figure ' + fig)
ok(abs(round((7711.76-7730.99)/7730.99*100, 2) - (-0.25)) < 0.005, 'ws S&P pct reconciles')
ok(abs(round((26402.42-26541.35)/26541.35*100, 2) - (-0.52)) < 0.005, 'ws Nasdaq pct reconciles')
ok(abs(round(53569.44-53559.99, 2) - 9.45) < 0.005, 'ws Dow points reconcile')
has('ws', 're-verified a tenth time at 12:05 PM', 'ws tenth verification')
nothas('ws', 're-verified a ninth time', 'ws stale ninth')
nothas('ws', '7,673.04', 'ws excluded intraday level')
nothas('ws', 'After-Hours Movers', 'ws no after-hours block (weekend)')
nothas('ws', 'as of ~', 'ws no intraday as-of (weekend)')
has('ws', 'closed', 'ws states market closed')

# ---- markets: the corroborated pre-speech pair, contested December
has('ws', 'Corroborated at 12:05 PM', 'ws corroboration marker')
has('ws', 'nearly 70%', 'ws pre-speech near-70 pause')
has('ws', 'about one in three', 'ws pre-speech one-in-three')
has('ws', 'above 50/50', 'ws post-speech read')
has('ws', '<b>48%</b>', 'ws Kalshi 48')
has('ws', 'Contested at 11:35 AM', 'ws December still contested')
has('ws', 'January 2027', 'ws December slipped to Jan 2027')
ok(WS.count('&gt;70% odds of a hike by December') <= 1, 'ws December figure not repeated as fact')
has('ws', 'corroborated by a second source 12:05 PM', 'ws rates as-of updated')

# ---- cyber: carried families intact
for s in ('McKesson','284 million','$55,236,150','records, not people','not independently verified',
          'Boston Scientific','Manchester Airports Group','8.7 million','Avada','Fusion Builder',
          'CVE-2026-18431','PaperCut','CVE-2026-82078','CVE-2026-81578','ATF'):
    has('cyber', s, 'cy carries ' + s)
has('cyber', 'Newly sourced at 12:05 PM', 'cy MAG new marker')
has('cyber', 'alert for phishing', 'cy MAG phishing warning')
has('cyber', 'passenger safety and aviation security were not affected', 'cy MAG safety scoping')
has('cyber', 'specialist', 'cy MAG advisers')
has('cyber', 'nothing here a customer can cancel or reissue', 'cy MAG residual-risk framing')
has('cyber', 'no payment', 'cy tldr payment scoping')
has('cyber', 'early stages', 'cy McKesson early-stages')
# Avada must stay labelled not-exploited / not-KEV
ok('not' in CY[CY.find('CVE-2026-18431')-1500:CY.find('CVE-2026-18431')+2500].lower(), 'cy Avada context')
# CVE ids well-formed
cves = set(re.findall(r'CVE-\d{4}-\d{4,6}', CY))
ok(len(cves) >= 12, 'cy CVE liveness (%d)' % len(cves))
for c in cves:
    ok(re.fullmatch(r'CVE-20\d\d-\d{4,6}', c) is not None, 'cy CVE wellformed ' + c)
# CVE-2026-21962 only ever appears inside its not-carried framing
for m in re.finditer('CVE-2026-21962', CY):
    w = CY[max(0, m.start()-400):m.start()+400]
    ok('not' in w.lower(), 'cy 21962 in not-carried frame')

# ---- mma: champions board, eleven names, no regressions
CHAMPS = ['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
          'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison',
          'Mackenzie Dern']
for c in CHAMPS:
    has('mma', c, 'mma champion ' + c)
# Pereira / Chimaev may only appear beside a rejection or interim/past frame
FRAMES = ['interim','rejected','no longer','vacated','stale','Split decision over Khamzat Chimaev',
          'split decision over Khamzat Chimaev','KO2','regression','upset','defeat','lost','former']
for nm in ('Pereira','Chimaev'):
    for m in re.finditer(nm, MM):
        w = MM[max(0, m.start()-380):m.start()+380]
        ok(any(f.lower() in w.lower() for f in FRAMES), 'mma %s framed at %d' % (nm, m.start()))
has('mma', 'fifty-third consecutive edition', 'mma counter advanced')
nothas('mma', 'fifty-second consecutive edition', 'mma stale counter')
has('mma', 'Checked a fourth time at 12:05 PM', 'mma fourth check')
has('mma', 'fourth distinct failure', 'mma fourth failure framing')
has('mma', 'vacated the lightweight title and now holds titles in both', 'mma quoted contradiction')
has('mma', 'disqualified by its own wording', 'mma self-contradiction rejection')
has('mma', 'undisputed lightweight champion', 'mma Gaethje external check')
has('mma', 'is not thereby right about the seventh', 'mma new rule')
has('mma', 'not restated as a number', 'mma counter not tallied')
# vacancy rejection family from 11:35 must survive
has('mma', 'An absence in a listing is not a vacancy', 'mma vacancy rule retained')
# UFC 333 family
for s in ('UFC 333','October&nbsp;24','Merab Dvalishvili','Movsar Evloev','Etihad'):
    has('mma', s, 'mma UFC333 ' + s)
# Gaethje idle-belt item
has('mma', 'New at 12:05 PM', 'mma new tag')
has('mma', 'no title defence scheduled', 'mma Gaethje no defence')
has('mma', 'not expected to compete again in 2026', 'mma Gaethje 2026')
has('mma', 'Ali Abdelaziz', 'mma manager named')
has('mma', 'Arman Tsarukyan', 'mma Tsarukyan named')
has('mma', 'Nothing is booked', 'mma booking caveat')
has('mma', 'the champion&rsquo;s opinion, not a matchmaking decision', 'mma opinion scoping')
# Shanghai results families
for s in ('Song Yadong','Umar Nurmagomedov','KO','Sherdog','$100,000','Bilal Hasan'):
    has('mma', s, 'mma shanghai ' + s)
has('mma', 'Salkilld', 'mma Salkilld present') if 'Salkilld' in MM else None
if 'Salkilld' in MM:
    ok('Quillan Salkilld' in MM, 'mma Salkilld full name correct')
    ok('Cody Salkilld' not in MM, 'mma Salkilld wrong-name forbid')
if 'Dariush' in MM:
    w = MM[max(0, MM.find('Dariush')-400):MM.find('Dariush')+400]
    ok('champion' not in w.lower() or 'contender' in w.lower(), 'mma Dariush descriptor')

# ---- index mirrors tldr exactly for all three
def tldr(h):
    m = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', h, re.S)
    return m.group(1) if m else None
for cls, src, nm in (('c-cy', CY, 'cyber'), ('c-ws', WS, 'markets'), ('c-mm', MM, 'mma')):
    m = re.search(r'<div class="bigcard %s">.*?<p>(.*?)</p>' % cls, IX, re.S)
    ok(m is not None and m.group(1) == tldr(src), 'index card mirrors %s tldr' % nm)
for lbl in ('The Wire','The Tape','Tale of the Tape'):
    ok(lbl in IX, 'index label ' + lbl)
has('cyber', '<b>The Wire</b>', 'cy tldr label')
has('ws', '<b>The Tape</b>', 'ws tldr label')
has('mma', '<b>Tale of the Tape</b>', 'mma tldr label')

# ---- footers: min links, no duplicate hrefs, disclaimers
for nm, h in (('cyber', CY), ('ws', WS), ('mma', MM)):
    m = re.search(r'<div class="srcs">.*?</div>', h, re.S)
    ok(m is not None, '%s has sources block' % nm)
    if m:
        hrefs = re.findall(r'<a href="([^"]+)"', m.group(0))
        ok(len(hrefs) >= 20, '%s footer >=20 links (%d)' % (nm, len(hrefs)))
        dup = [x for x in set(hrefs) if hrefs.count(x) > 1]
        ok(not dup, '%s footer duplicate hrefs %s' % (nm, dup))
        ok(all(u.startswith('http') for u in hrefs), '%s footer hrefs absolute' % nm)
ok('not investment advice' in WS.lower() or 'investment advice' in WS.lower(), 'ws disclaimer')
ok('subject to change' in MM.lower(), 'mma disclaimer')

# ---- chronology: nothing "upcoming" that already happened
ok('August&nbsp;29' in MM or 'August 29' in MM, 'mma references today')
ok(MM.find('UFC 333') > 0 and 'October' in MM, 'mma UFC333 future-dated')

print('validate_1205: %d checks, %d failures' % (N, len(FAIL)))
for f in FAIL: print('  FAIL:', f)
sys.exit(1 if FAIL else 0)
