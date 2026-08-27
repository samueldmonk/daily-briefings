#!/usr/bin/env python3
"""Validator for the 2026-08-27 ~8:40am ET Morning Edition.
Rewritten this run: validate_1836.py was stale (asserted Okta fundamentals, a
"33rd edition" string, and &nbsp;/&minus; HTML entities the pages no longer use),
and its champions-board parser returned None for every cell. A stale harness that
fails on correct pages is worse than no harness, so it is replaced, not worked around.
"""
import sys, re, io, html as _html

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
D = {p: io.open(OUT + '/' + p, encoding='utf-8').read() for p in PAGES}

fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

def strip_scripts(s):
    return re.sub(r'<script.*?</script>', '', s, flags=re.S)

# ---------- 1. five-tab nav + active tab ----------
TABS = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
        'mma-briefing.html', 'archive.html']
LABELS = ['★ Front Page', '⛨ The Cyber Wire', '▲ The Closing Bell', '⊘ The Octagon', '🗄 Archive']
for p, s in D.items():
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', s, re.S)
    ck(nav is not None, '%s: nav block missing' % p)
    if nav:
        n = nav.group(1)
        for t in TABS:
            ck(('href="%s"' % t) in n, '%s: nav missing link %s' % (p, t))
        for l in LABELS:
            ck(l in n, '%s: nav missing label %s' % (p, l))
        on = re.findall(r'<a href="([^"]+)"[^>]*class="on"', n)
        ck(on == [p], '%s: active tab should be %s, got %s' % (p, p, on))

# ---------- 2. masthead pills + self-stamp JS ----------
for p, s in D.items():
    for pid in ['edition', 'datestamp', 'updated', 'freshline']:
        ck(('id="%s"' % pid) in s, '%s: missing id=%s' % (p, pid))
    ck('pill live' in s, '%s: missing LIVE pill' % p)
    ck("getElementById('datestamp')" in s and "getElementById('updated')" in s
       and "getElementById('edition')" in s, '%s: self-stamp JS incomplete' % p)
    ck("'Morning Edition'" in s and "'Midday Edition'" in s
       and "'Afternoon Edition'" in s, '%s: edition buckets missing' % p)
    ck('briefings refresh every 30 minutes' in s, '%s: freshline text missing' % p)

# ---------- 3. per-page tldr labels; index uses cards ----------
ck('>The Wire</b>' in D['cyber-briefing.html'], 'cyber: tldr label "The Wire" missing')
ck('>The Tape</b>' in D['wallstreet-briefing.html'], 'ws: tldr label "The Tape" missing')
ck('>Tale of the Tape</b>' in D['mma-briefing.html'], 'mma: tldr label missing')
ck('class="tldr"' not in D['index.html'], 'index: must use cards, not a tldr strip')
for p in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    ck(D[p].count('class="tldr"') == 1, '%s: expected exactly one tldr' % p)

# ---------- 4. TradingView blocks: Wall Street only ----------
WS = D['wallstreet-briefing.html']
for w in ['ticker-tape', 'single-quote', 'timeline', 'stock-heatmap',
          'mini-symbol-overview', 'events']:
    ck(('embed-widget-%s.js' % w) in WS, 'ws: missing widget %s' % w)
ck(WS.count('embed-widget-single-quote.js') == 3, 'ws: need exactly 3 single-quote widgets')
for sym in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y']:
    ck(sym in WS, 'ws: ticker tape missing mandatory symbol %s' % sym)
ck('livebar' in WS and 'LIVE QUOTES' in WS, 'ws: livebar wrapper missing')
for p in ['index.html', 'cyber-briefing.html', 'mma-briefing.html']:
    ck('tradingview.com/external-embedding' not in D[p], '%s: must have no live widgets' % p)

# ---------- 5. balanced div / table markup ----------
for p, s in D.items():
    b = strip_scripts(s)
    ck(b.count('<div') == b.count('</div>'),
       '%s: div imbalance %d/%d' % (p, b.count('<div'), b.count('</div>')))
    ck(b.count('<table') == b.count('</table>'), '%s: table imbalance' % p)
    ck(b.count('<tr') == b.count('</tr>'), '%s: tr imbalance' % p)
    ck(b.count('<td') == b.count('</td>'), '%s: td imbalance' % p)

# ---------- 6. MMA countdown ----------
M = D['mma-briefing.html']
ck('id="ufccdn"' in M, 'mma: countdown element missing')
ck(re.search(r'getElementById\([\'"]ufccdn[\'"]\)', M) is not None, 'mma: countdown script missing')
ck('Fight week' in M, 'mma: countdown elapsed string missing')

# ---------- 7. Cyber: patch priority, KEV countdowns, stat strip ----------
C = D['cyber-briefing.html']
ck('callout crit' in C, 'cyber: Patch Priority must carry the crit border today (deadline expires)')
ck('CVE-2026-21962' in C, 'cyber: patch-priority CVE missing')
for kid in ['kev1', 'kev2', 'kev3']:
    ck(('id="%s"' % kid) in C, 'cyber: KEV countdown %s missing' % kid)
ck(C.count('class="stat"') >= 4, 'cyber: stat strip needs >=4 tiles')
# the same verified deadline in all three places
for frag in ['due <b>Aug 27</b>', 'due today, August 27', 'federal due date <b>Aug 27</b>']:
    ck(frag in C, 'cyber: Aug 27 deadline missing from one of the three required places (%s)' % frag)
ck('August 28' not in C.split('Patch Priority')[1].split('</div>')[0],
   'cyber: Patch Priority must not cite the Gitea date')

# ---------- 8. Invented-CVE guard ----------
ALLOWED = {
    'CVE-2026-21962', 'CVE-2026-12569', 'CVE-2026-69836', 'CVE-2026-68820',
    'CVE-2026-62815', 'CVE-2026-62893', 'CVE-2026-60004', 'CVE-2026-73570',
    'CVE-2026-20349', 'CVE-2026-72898', 'CVE-2026-18963', 'CVE-2026-19913',
    'CVE-2026-19912', 'CVE-2026-72529', 'CVE-2026-72530', 'CVE-2026-33824',
    'CVE-2026-55040', 'CVE-2026-59310', 'CVE-2026-65400', 'CVE-2026-8452',
    'CVE-2015-3246', 'CVE-2015-5287', 'CVE-2019-1068', 'CVE-2021-23758',
    'CVE-2022-0995',
}
found = set(re.findall(r'CVE-\d{4}-\d{4,7}', C))
ck(found <= ALLOWED, 'cyber: unverified CVE id(s) present: %s' % sorted(found - ALLOWED))

# ---------- 9. Champions board parsed as real cells ----------
tbl = re.search(r'<h2 class="sec">Champions Board</h2>\s*<table>(.*?)</table>', M, re.S)
ck(tbl is not None, 'mma: champions board table not found')
champs = {}
if tbl:
    for row in re.findall(r'<tr>(.*?)</tr>', tbl.group(1), re.S):
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
        if len(cells) == 3:
            div = re.sub(r'<[^>]+>', '', cells[0]).strip()
            champ = re.sub(r'<[^>]+>', '', cells[1]).strip()
            champs[div] = champ
ck(len(champs) == 11, 'mma: champions board has %d division rows, expected 11' % len(champs))
EXPECT = {
    'Heavyweight': 'Tom Aspinall', 'Light Heavyweight': 'Carlos Ulberg',
    'Middleweight': 'Sean Strickland', 'Welterweight': 'Islam Makhachev',
    'Lightweight': 'Justin Gaethje', 'Featherweight': 'Alexander Volkanovski',
    'Bantamweight': 'Petr Yan', 'Flyweight': 'Joshua Van',
    "Women's Flyweight": 'Valentina Shevchenko',
    "Women's Bantamweight": 'Kayla Harrison',
    "Women's Strawweight": 'Mackenzie Dern',
}
for d, c in EXPECT.items():
    ck(champs.get(d) == c, 'mma: %s champ = %r, expected %r' % (d, champs.get(d), c))
# the three historical regressions, tested by name in champion cells only
cells_only = ' | '.join(champs.values())
ck('Pereira' not in cells_only, 'mma REGRESSION: Pereira listed as a champion')
ck('Chimaev' not in cells_only, 'mma REGRESSION: Chimaev listed as a champion')
ck('acant' not in cells_only, 'mma REGRESSION: a division listed as vacant')
ck('Topuria' not in cells_only, 'mma REGRESSION: Topuria listed as LW champ')

# ---------- 10. Markets discipline ----------
# the mislabelled Aug 25 close set may appear ONLY inside the rejection note
for lvl in ['7,677.24', '53,577.40', '26,151.30']:
    for occ in [m_.start() for m_ in re.finditer(re.escape(lvl), WS)]:
        window = WS[max(0, occ - 700):occ + 700]
        ck('mislabelled' in window or 'not published here' in window,
           'ws: %s appears outside a rejection context' % lvl)
ck('7,675.70' in WS, 'ws: verified Wednesday S&P close missing')
ck('level not corroborated this run' in WS, 'ws: uncorroborated-level disclosure missing')
ck('not verified this run' in WS, 'ws: 30-year row must say not verified')
# the stale-2022 jobless-claims trap must be rejected, never asserted as current
if '232,000' in WS:
    w2 = WS[WS.index('232,000') - 400: WS.index('232,000') + 400]
    ck('2022' in w2 and 'rejected' in w2, 'ws: 232,000 claims figure not framed as rejected')
    checks += 1
# as-of time stated
ck(re.search(r'as of roughly <b>8:40 AM ET</b>', WS, re.I) is not None, 'ws: as-of time missing')
# before the open: no after-hours section, lead must be pre-open
ck('After-Hours Movers' not in WS, 'ws: after-hours section must not appear pre-open')

# ---------- 11. index cards agree with each page's lead ----------
I = D['index.html']
ck(I.count('class="card c-') == 3, 'index: expected 3 big cards')
def tldr_text(p):
    m_ = re.search(r'<div class="tldr">.*?<span>(.*?)</span>', D[p], re.S)
    return _html.unescape(re.sub(r'<[^>]+>', '', m_.group(1))).strip() if m_ else ''
for p in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    t = tldr_text(p)
    ck(len(t) > 40, '%s: tldr sentence too short' % p)
    key = t.split()[0:6]
    ck(all(k.strip('.,') in _html.unescape(I) for k in key if len(k) > 4),
       'index: card does not track %s lead' % p)

# ---------- 12. sources footers + disclaimers ----------
for p in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    foot = D[p][D[p].rindex('<footer'):]
    ck(foot.count('<a href="http') >= 10, '%s: sources footer too thin' % p)
    ck('<div class="disc">' in foot, '%s: disclaimer missing' % p)
ck('Nothing here is investment advice' in D['wallstreet-briefing.html'], 'ws: disclaimer wording')
ck('subject to change' in D['mma-briefing.html'], 'mma: disclaimer wording')
ck('not a substitute for your own security review' in D['cyber-briefing.html'], 'cyber: disclaimer wording')

# ---------- 13. trap greps: names/events that were wrong in past editions ----------
TRAPS = ['Cody Salkilld', 'Shamil Yakhyaev', 'Abdul-Rakhman', 'Fight Night 286',
         'Bella Mir won', 'title challenger Beneil']
for p, s in D.items():
    for t in TRAPS:
        ck(t not in s, '%s: TRAP string present: %s' % (p, t))

# ---------- 14. chronology: nothing "upcoming" that has passed ----------
ck('Saturday, August 29' in M or 'SAT AUG 29' in M, 'mma: next card date missing')
ck('August 22' in M, 'mma: last-event date missing')

print('CHECKS: %d   FAILURES: %d' % (checks, len(fails)))
for f in fails:
    print('  FAIL:', f)
sys.exit(1 if fails else 0)
