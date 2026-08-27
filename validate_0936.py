#!/usr/bin/env python3
"""Validator for the 2026-08-27 ~9:36am ET Morning Edition (fourth run, POST-OPEN).
Derived from validate_0906.py. Edition-specific block rewritten: the Jackson Hole
guard is INVERTED (the 9:05 run wrongly deleted a real, current event; it is restored
and the guard now requires it to be published with its correction note), and the
CVE whitelist gains the two Veeam ONE identifiers.
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
    'CVE-2026-62815', 'CVE-2026-62893', 'CVE-2026-60004', 'CVE-2026-73570', 'CVE-2026-8037',
    'CVE-2026-20349', 'CVE-2026-72898', 'CVE-2026-18963', 'CVE-2026-19913',
    'CVE-2026-19912', 'CVE-2026-72529', 'CVE-2026-72530', 'CVE-2026-33824',
    'CVE-2026-55040', 'CVE-2026-59310', 'CVE-2026-65400', 'CVE-2026-8452',
    'CVE-2015-3246', 'CVE-2015-5287', 'CVE-2019-1068', 'CVE-2021-23758',
    'CVE-2022-0995', 'CVE-2026-64633', 'CVE-2026-65641',
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
ck('New \u00b7 9:35 AM ET' in WS and '~9:35 AM ET' in WS, 'ws: as-of time missing')
# before the open: no after-hours section, lead must be pre-open
ck('After-Hours Movers' not in WS, 'ws: after-hours section must not appear before 4 PM ET')

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


# ── additional checks for the 9:36 AM ET edition (fourth run of 2026-08-27, POST-OPEN) ─

CY = D['cyber-briefing.html']; MM = D['mma-briefing.html']; IX = D['index.html']

# ---- Markets: post-open lead, with its own honesty caveat ----
ck('Just after the open' in WS, 'ws: lead tag must mark the post-open state')
ck('The regular session is open.' in WS, 'ws: post-open lead sentence missing')
ck('S&amp;P 500 up 0.4%' in WS, 'ws: S&P read missing')
ck('Nasdaq Composite up about 1%' in WS, 'ws: Nasdaq read missing')
ck('Dow hovering near the flat line' in WS, 'ws: Dow read missing')
ck('not</b> asserted as prices struck after the 9:30 bell' in WS,
   'ws: the index-figure provenance caveat is missing')
# live single-stock quotes, each printed alongside its pre-market read
ck('up 5.87%' in WS, 'ws: NVDA live quote missing')
ck('up 14.78%' in WS, 'ws: CRM live quote missing')
ck('up 14.34%' in WS, 'ws: CRWD live quote missing')
ck('up more than 20%' in WS, 'ws: OKTA live quote missing')
ck('7.4%' in WS and '7.32%' in WS and '6%' in WS, 'ws: NVDA pre-market reads must remain printed')
ck('nearly 12%' in WS and '8.9%' in WS, 'ws: CRM/CRWD pre-market reads must remain printed')
ck('$333 million' in WS and '51%' in WS, 'ws: CrowdStrike net-new-ARR figure missing')
ck('$1.05 per share on revenue of $805 million' in WS, 'ws: Okta results missing')
ck('97 cents' in WS and '$795 million' in WS, 'ws: Okta consensus missing')
ck('Neutral from Underperform with a $170 price target' in WS, 'ws: Okta upgrade missing')
ck('$4.17 per diluted share on $1.267 billion' in WS, 'ws: ANF results missing')
ck('$13.10' in WS and '$13.60' in WS, 'ws: ANF raised guidance missing')
ck('fell 1.4%' in WS and 'Citi downgraded' in WS, 'ws: ANF downgrade/move missing')
# carried, still-verified figures
ck('203,000' in WS and 'week ending <b>August 22</b>' in WS, 'ws: claims print missing')
ck('205,500' in WS and '207,000' in WS, 'ws: claims revision / 4-week average missing')
ck('$1.47 billion' in WS and '$0.31' in WS, 'ws: CrowdStrike quarter figures missing')
ck('$96.2 billion' in WS and '$108 billion' in WS, 'ws: Nvidia quarter/guide missing')
ck('7,675.70' in WS, 'ws: verified Wednesday S&P close missing')
ck('4.64' in WS and '4.66' in WS, 'ws: 10-year yield range missing')
ck('4.75%' in WS and 'Aug 21' in WS, 'ws: 20-month-high context missing')
ck('$81.36' in WS, 'ws: WTI level missing')
ck('nearly 52% chance' in WS and 'down from 67%' in WS, 'ws: September-meeting odds missing')

# ---- the two standing rejections stay rejections ----
for _m in re.finditer(r'232,000', WS):
    _w = WS[max(0, _m.start()-500):_m.start()+300]
    ck('reject' in _w.lower(), 'ws: 232,000 appears outside a rejection context')
for _m in re.finditer(r'\$5\.90', WS):
    _w = WS[max(0, _m.start()-500):_m.start()+700]
    ck('withheld' in _w.lower() or 'not published' in _w.lower(),
       'ws: $5.90 EPS appears outside a non-publication note')
ck('$4.17' in WS and '$1.99' in WS, 'ws: the ANF comparison that weakens the $5.90 objection must be shown')

# ---- Jackson Hole: guard INVERTED this run ----
ck('Jackson Hole' in WS, 'ws: Jackson Hole must be published this run, not removed')
ck('August 27&ndash;29' in WS or 'August 27\u201329' in WS, 'ws: symposium dates missing')
ck('Jackson Lake Lodge' in WS, 'ws: symposium venue missing')
ck('Financial Innovation: Implications for Payments and Policy' in WS, 'ws: symposium theme missing')
ck('Kevin Warsh' in WS and 'Friday, August 28' in WS, 'ws: Warsh keynote timing missing')
ck('That reasoning was wrong.' in WS, 'ws: the self-correction must be stated in the open')
ck('kansascityfed.org' in WS, 'ws: primary Jackson Hole source missing from the footer')
# and it must NOT be scoped as a removal any more
_jh = WS[WS.index('Jackson Hole is this week'):]
ck('has been removed' not in WS.split('On the Radar')[1], 'ws: stale removal note still present')

# ---- Cyber: the new Veeam pair, Aurora, Displaydata ----
ck('CVE-2026-64633' in CY and '10.0 (CVSS v4.0)' in CY, 'cyber: Veeam max-severity CVE missing')
ck('13.0.2.6723' in CY and '13.1.0.7034' in CY, 'cyber: Veeam affected/fixed builds missing')
ck('KB4892' in CY and 'KB4905' in CY, 'cyber: Veeam KB references missing')
ck('CVE-2026-65641' in CY and '9.3 (CVSS v4.0)' in CY, 'cyber: Veeam SMB-coercion CVE missing')
ck('No source seen this run reports exploitation in the wild' in CY,
   'cyber: Veeam must state that no exploitation was verified')
ck('exploitation plus a deadline beats severity alone' in CY,
   'cyber: Patch Priority must explain why Oracle still outranks the new 10.0')
ck('Aurora' in CY and 'AI coding assistant' in CY, 'cyber: Aurora ransomware item missing')
ck('more than 20 organisations' in CY, 'cyber: Aurora victim count missing')
ck('Displaydata' in CY, 'cyber: Displaydata item missing')
ck('does not name the group' in CY, 'cyber: Displaydata unknowns must be stated')
ck('Citrix NetScaler ADC and NetScaler Gateway' in CY, 'cyber: CVE-2026-8452 identification missing')
# carried cyber facts
ck('CareCloud' in CY and '3.7 million' in CY and '350,000' in CY, 'cyber: CareCloud figures missing')
ck('3,750,000' in CY, 'cyber: prior anonymous-figure note missing')
ck('AA26-222A' in CY and 'Gunra' in CY, 'cyber: Gunra advisory missing')
ck('at least seven US states' in CY, 'cyber: FBI water-sector item missing')
ck('Nutex Health' in CY and 'August 24' in CY, 'cyber: Nutex 8-K item missing')
ck('BOD 26-04' in CY, 'cyber: risk-based directive reference missing')
for _m in re.finditer(r'until <b>August 21</b>', CY):
    _w = CY[_m.start():_m.start()+700]
    ck('rather than asserted' in _w, 'cyber: Aug 21 window asserted rather than reported')
ck('CVE-2026-8037' in CY and 'Progress LoadMaster' in CY, 'cyber: Aug 7 KEV addition missing')
# every KEV batch verified against a CISA alert page this run must be sourced
for _u in ['/2026/08/11/', '/2026/08/18/', '/2026/08/20/', '/2026/08/24/', '/2026/08/26/']:
    ck(_u in CY, 'cyber: CISA alert source missing for %s' % _u)

# ---- MMA: new card, corrected tense, added detail ----
ck('Jean Silva' in MM and 'Jos&eacute; Miguel Delgado' in MM, 'mma: Noche UFC main event missing')
ck('SAT SEP 12' in MM, 'mma: Noche UFC date line missing')
ck('Pudong Development Bank Shanghai Oriental Sports Center' in MM, 'mma: full venue name missing')
ck('Road to UFC season 5 semifinals' in MM, 'mma: Road to UFC item missing')
ck('5 a.m. ET / 5 p.m. CST' in MM, 'mma: Road to UFC start time missing')
ck('published official weights' in MM, 'mma: weights status not updated')
ck('due on August 28' not in MM.split('Top Story')[1].split('Fight Week')[0]
   or 'have since been released' in MM, 'mma: stale future-tense weights line')
ck('Bilal Hasan' in MM and 'preparing for his UFC debut' in MM, 'mma: Bilal Hasan debut missing')
ck('Cory Sandhagen' in MM and 'Mario Bautista' in MM, 'mma: Umar resume detail missing')
# carried MMA facts
ck('seven-fight winning streak' in MM and 'four-defence reign' in MM, 'mma: UFC 331 detail missing')
ck('lightweight title eliminator' in MM, 'mma: Tsarukyan/Ruffy stakes missing')
ck('Merab Dvalishvili at UFC 311' in MM, 'mma: Umar title-challenge context missing')
ck("China's highest-ranked male UFC contender" in MM, 'mma: Song context missing')
ck('\u2212500' in MM and '+380' in MM, 'mma: Shanghai odds missing')
ck('Gregory Rodrigues' in MM and '48-47, 49-46, 48-47' in MM, 'mma: last-event result missing')
ck('Curtis Blaydes' in MM, 'mma: named eight-fight-deal item missing')
# the unresolved rankings disagreement is still printed unresolved
ck('neither is adopted' in MM, 'mma: rankings disagreement must stay unresolved')

# ---- index cards agree with the page leads ----
ck('Okta is the biggest mover' in IX, 'index: markets card does not reflect the page lead')
ck('up more than 20%' in IX, 'index: Okta figure missing from the markets card')
ck('CVE-2026-21962' in IX and 'Veeam ONE' in IX, 'index: cyber card lead missing')
ck('Noche UFC' in IX, 'index: MMA card does not reflect the new booking')
ck('203,000' not in IX or '203,000' in WS, 'index: stale claims headline')

print('CHECKS: %d   FAILURES: %d' % (checks, len(fails)))
for f in fails:
    print('  FAIL:', f)
sys.exit(1 if fails else 0)
