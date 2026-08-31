#!/usr/bin/env python3
"""Fact-check / structure guards for the 1:12 PM ET edition, Aug 31 2026."""
import io, re, sys

FAIL = []
N = [0]

def ck(cond, msg):
    N[0] += 1
    if not cond:
        FAIL.append(msg)

PAGES = {p: io.open(p, encoding='utf-8').read()
         for p in ['index.html', 'cyber-briefing.html',
                   'wallstreet-briefing.html', 'mma-briefing.html']}
IDX, CY, WS, MM = (PAGES['index.html'], PAGES['cyber-briefing.html'],
                   PAGES['wallstreet-briefing.html'], PAGES['mma-briefing.html'])

def strip_footer(h):
    i = h.find('<footer')
    return h[:i] if i > 0 else h

def unlinked(h):
    """Prose only: drop the footer and every anchor's link text."""
    h = strip_footer(h)
    return re.sub(r'<a\b[^>]*>.*?</a>', ' ', h, flags=re.S)

# ============================================ 1. UNIVERSAL STRUCTURE
for p, h in PAGES.items():
    ck('id="edition"' in h, '%s: edition pill' % p)
    ck('id="datestamp"' in h, '%s: datestamp pill' % p)
    ck('id="updated"' in h, '%s: updated pill' % p)
    ck('>1:12 PM ET<' in h, '%s: stamp not restamped to 1:12 PM ET' % p)
    ck('id="freshline"' in h, '%s: freshline' % p)
    ck('Data as of 1:12 PM ET' in h, '%s: freshline not restamped' % p)
    ck(h.count('<nav class="tabs">') == 1, '%s: exactly one nav' % p)
    for tab in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
                'mma-briefing.html', 'archive.html']:
        ck('href="%s"' % tab in h, '%s: nav missing %s' % (p, tab))
    ck('12:24 PM ET<' not in h, '%s: stale 12:24 stamp survived' % p)
    ck('12:51 PM ET<' not in h, '%s: stale 12:51 stamp survived' % p)
    ck('Data as of 12:51' not in h, '%s: stale freshline' % p)
    ck('<h2 class="sec"><div' not in h, '%s: empty section heading' % p)
    ck(h.count('<footer>') == 1, '%s: exactly one footer' % p)
    # sources present and plural
    ck(h.count('<a href="http') >= 6, '%s: >=6 source links' % p)
    # day-roll hygiene: no weekend note on a Monday
    ck('markets are closed today' not in h.lower(), '%s: weekend note on a Monday' % p)

for p in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    ck('class="tldr"' in PAGES[p], '%s: tldr strip' % p)
ck(PAGES['wallstreet-briefing.html'].count('class="tldr"') == 1, 'ws: exactly one tldr')
ck(PAGES['cyber-briefing.html'].count('class="tldr"') == 1, 'cy: exactly one tldr')
ck(PAGES['mma-briefing.html'].count('class="tldr"') == 1, 'mma: exactly one tldr')
ck('<b>The Tape</b>' in WS, 'ws: tldr label')
ck('<b>The Wire</b>' in CY, 'cy: tldr label')
ck('<b>Tale of the Tape</b>' in MM, 'mma: tldr label')

# ============================================ 2. LIVE WIDGETS (WS only)
for w in ['embed-widget-ticker-tape.js', 'embed-widget-single-quote.js',
          'embed-widget-timeline.js', 'embed-widget-stock-heatmap.js',
          'embed-widget-mini-symbol-overview.js', 'embed-widget-events.js']:
    ck(w in WS, 'ws: missing widget %s' % w)
ck(WS.count('embed-widget-single-quote.js') == 3, 'ws: three single-quote widgets')
for sym in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI',
            'TVC:USOIL', 'TVC:US10Y']:
    ck(sym in WS, 'ws: ticker tape missing %s' % sym)
ck('class="livebar"' in WS, 'ws: livebar')
for p in ['cyber-briefing.html', 'mma-briefing.html', 'index.html']:
    ck('tradingview.com' not in PAGES[p], '%s: live widget on a non-markets page' % p)

# --- symbol/caption agreement for Chart of the Day (guard owed 8/31 12:24)
m = re.search(r'<h2 class="sec">Chart of the Day[^<]*?\(([A-Z]+:[A-Z.]+)\)', WS)
ck(bool(m), 'ws: Chart of the Day heading carries a symbol')
if m:
    head_sym = m.group(1)
    m2 = re.search(r'embed-widget-mini-symbol-overview\.js"[^>]*>\s*\{"symbol":"([^"]+)"', WS)
    ck(bool(m2), 'ws: mini-symbol-overview symbol parseable')
    if m2:
        ck(head_sym == m2.group(1),
           'ws: Chart of the Day heading %s != widget %s' % (head_sym, m2.group(1)))

# ============================================ 3. MARKETS FACTS
wsp = unlinked(WS)
# the fourth refusal must be present AND adjacent to its refusal language
ck('53,885.10' in wsp, 'ws: refused Dow level recorded')
for occ in [m.start() for m in re.finditer(r'53,885\.10', wsp)]:
    win = wsp[max(0, occ - 2500):occ + 2500].lower()
    ck('refused' in win or 'has not closed' in win or 'does not close' in win,
       'ws: 53,885.10 at %d without refusal context' % occ)
ck('fourth time' in wsp, 'ws: fourth refusal stated')
ck('closing values' in wsp.lower(), 'ws: the mislabel itself is quoted')
ck('does not close until 4 PM ET' in wsp, 'ws: the clock rebuttal')
# Friday's verified closes must still be attributed to Friday wherever asserted
ck('7,711.76' in wsp and '26,402.42' in wsp, 'ws: Friday closes carried')
ck('53,559.99' in wsp, "ws: Friday's verified Dow close carried")
# PayPal: Friday's move, never today's news.
# NARROWED (10th refusal-context false positive): the guard fired on the page's own
# "this page does not speculate" paragraph, which asserts no move at all. Re-anchored
# to fire only where a PayPal PERCENTAGE is present -- an assertion, not a mention.
for occ in [m.start() for m in re.finditer(r'PayPal', wsp)]:
    win = wsp[max(0, occ - 1800):occ + 1800]
    if not re.search(r'1[23]\.?\d*%|12\.63|12\.7', win):
        continue
    ck('Friday' in win or 'refus' in win.lower() or '12.63' in win,
       'ws: PayPal percentage at %d not marked as Friday/refused' % occ)
# the new Dow points figure must travel with its reconciliation and its non-adoption
ck('315 points' in wsp, 'ws: new Dow points figure')
i = wsp.find('315 points')
ck('0.588' in wsp[i - 2500:i + 2500] or '0.6%' in wsp[i - 800:i + 800],
   'ws: 315 points without its percent')
ck('no index level is published for the live session' in wsp.lower()
   or 'no index level published for the live session' in wsp.lower(),
   'ws: live-session level refusal restated')
# S&P rendering family all printed
for r in ['0.43%', '0.45%', '0.47%', '0.5%', '0.55%']:
    ck('&minus;' + r in wsp or r in wsp, 'ws: S&P rendering %s missing' % r)
ck('none is adopted' in wsp or 'none adopted' in wsp, 'ws: non-adoption stated')
# premarket set must be labelled premarket, never as the live session
for occ in [m.start() for m in re.finditer(r'0\.27%', wsp)]:
    win = wsp[max(0, occ - 1200):occ + 1200].lower()
    ck('premarket' in win, 'ws: 0.27%% at %d not labelled premarket' % occ)
# sector story
ck('energy' in wsp.lower() and 'only' in wsp.lower(), 'ws: energy-only-sector line')
ck('1.6%' in wsp, 'ws: utilities figure')
# Weekly Scorecard purity: no intraday level inside the table
m = re.search(r'<h2 class="sec">Weekly Scorecard.*?</table>', WS, flags=re.S)
ck(bool(m), 'ws: Weekly Scorecard table present')
if m:
    ck('53,885.10' not in m.group(0), 'ws: refused level leaked into Scorecard')
# rates: table still carries Friday's stated close
ck('4.73%' in wsp, 'ws: 10-year Friday close carried')
ck('disclaimer' in WS.lower() or 'not investment advice' in WS.lower(),
   'ws: investment-advice disclaimer')

# ============================================ 4. CYBER FACTS
cyp = unlinked(CY)
# FulcrumSec top story, with attribution scoping
ck('FulcrumSec' in cyp, 'cy: FulcrumSec named')
ck('86 GB' in cyp or '86GB' in cyp, 'cy: 86 GB figure')
for occ in [m.start() for m in re.finditer(r'86 GB', cyp)]:
    win = cyp[max(0, occ - 3000):occ + 3000].lower()
    ck('claim' in win or 'attacker' in win, 'cy: 86 GB at %d unattributed' % occ)
ck('Iterable' in cyp, 'cy: Iterable named')
ck('client-side JavaScript' in cyp, 'cy: the method stated')
ck('21.5 GB' in cyp, 'cy: sample size')
ck('8.7 million' in cyp, 'cy: MAG own figure carried')
# the two figures must never be reconciled against each other
i = cyp.find('8.7 million')
ck('company' in cyp[max(0, i - 3500):i + 3500].lower(),
   'cy: 8.7M not marked as the company figure')
ck('August 25' in cyp and 'August 27' in cyp, 'cy: MAG timeline carried')
# Berlin
ck('Rhysida' in cyp, 'cy: Rhysida named')
ck('5.79' in cyp, 'cy: Berlin claimed volume')
for occ in [m.start() for m in re.finditer(r'5\.79', cyp)]:
    win = cyp[max(0, occ - 2500):occ + 2500].lower()
    ck('claim' in win or 'posting' in win or 'attacker' in win,
       'cy: 5.79 TB at %d unattributed' % occ)
ck('September 20' in cyp, 'cy: Berlin election date')
ck('30 bitcoin' in cyp, 'cy: ransom in BTC')
i = cyp.find('30 bitcoin')
ck('2.3 million' in cyp[i:i + 1200], 'cy: dollar conversion adjacent')
ck('derived' in cyp[i:i + 1600] or 'reporting' in cyp[i:i + 1600],
   'cy: dollar conversion not hedged')
ck('will not pay' in cyp, 'cy: Berlin refusal to pay')
ck('Iris Spranger' in cyp, 'cy: named official')
# GiveWP
ck('CVE-2026-82222' in cyp, 'cy: GiveWP CVE')
ck('4.16.7.2' in cyp and '4.16.7.1' in cyp, 'cy: GiveWP versions')
ck('10.0' in cyp, 'cy: GiveWP CVSS')
i = cyp.find('CVE-2026-82222')
win = cyp[i:i + 6000].lower()
ck('no vendor advisory' in win or "reporting&rsquo;s" in cyp[i:i + 6000],
   'cy: GiveWP 10.0 not marked as the reporting figure')
ck('not in CISA KEV' in cyp or 'not KEV-listed' in cyp, 'cy: GiveWP KEV status')
ck('give_action=user_register' in cyp, 'cy: the registration bypass detail')
# the two-account contradiction must be reconciled, not hidden
ck('Neither is dropped' in cyp or 'neither is dropped' in cyp,
   'cy: GiveWP contradiction handled')
# KEV
ck('twenty-fourth' in cyp, 'cy: 24th KEV check')
ck('seventeenth consecutive' in cyp, 'cy: KEV streak')
for cve in ['CVE-2026-33824', 'CVE-2026-55040', 'CVE-2026-59310', 'CVE-2026-65400',
            'CVE-2026-72529', 'CVE-2026-72530', 'CVE-2026-21962', 'CVE-2015-3246',
            'CVE-2015-5287', 'CVE-2019-1068', 'CVE-2021-23758', 'CVE-2022-0995',
            'CVE-2026-8452', 'CVE-2023-49105', 'CVE-2026-53362', 'CVE-2026-66384']:
    ck(cve in cyp, 'cy: KEV identifier %s missing' % cve)
ck('August 31, 2026' in cyp, 'cy: deadline baseline is today')
# no same-week/derived KEV deadline invented
ck('three weeks' not in cyp.lower() or 'superseded' in cyp.lower(),
   'cy: BOD 22-01 heuristic used without the supersession note')
ck('none is derived' in cyp or 'none derived' in cyp, 'cy: derived-deadline refusal')
# the stale "due TODAY, Sunday, August 30" defect must not be ASSERTED
for occ in [m.start() for m in re.finditer(r'due TODAY', CY)]:
    win = CY[max(0, occ - 400):occ + 400]
    ck('&ldquo;' in win or '&rdquo;' in win or 'Sunday, August 30' not in win,
       'cy: unquoted "due TODAY, Sunday, August 30" at %d' % occ)
# Patch Priority present with a severity border
m = re.search(r'<h2 class="sec">Patch Priority.*?</div>', CY, flags=re.S)
ck(bool(m), 'cy: Patch Priority block')
ck('CVE-2026-8452' in CY, 'cy: Patch Priority CVE carried')
# permanently excluded item
ck('Nevada' not in cyp or '2025' in cyp, 'cy: Nevada 2025 exclusion')
# date-refused items must stay refused
for name in ['Bouygues', 'fairlife']:
    for occ in [m.start() for m in re.finditer(name, cyp)]:
        win = cyp[max(0, occ - 2500):occ + 2500].lower()
        ck('refus' in win or 'not published as current' in win or 'weeks old' in win,
           'cy: %s at %d not marked refused' % (name, occ))

# ============================================ 5. MMA FACTS
mmp = unlinked(MM)
CHAMPS = {'Heavyweight': 'Aspinall', 'Light Heavyweight': 'Ulberg',
          'Middleweight': 'Strickland', 'Welterweight': 'Makhachev',
          'Lightweight': 'Gaethje', 'Featherweight': 'Volkanovski',
          'Bantamweight': 'Yan', 'Flyweight': 'Van',
          'Shevchenko': 'Shevchenko', 'Harrison': 'Harrison', 'Dern': 'Dern'}
for k, v in CHAMPS.items():
    ck(v in mmp, 'mma: champion %s (%s) missing' % (v, k))
ck('eighteenth' in mmp.lower(), 'mma: 18th cross-check')
ck('seventy-fifth' in mmp.lower(), 'mma: 75th consecutive edition')
# champion CELLS must not name a deposed champion as champion
m = re.search(r'<h2 class="sec">Champions Board.*?<table>(.*?)</table>', MM, flags=re.S)
ck(bool(m), 'mma: Champions Board table')
if m:
    tbl = m.group(1)
    rows = re.findall(r'<tr>(.*?)</tr>', tbl, flags=re.S)
    ck(len(rows) >= 10, 'mma: >=10 champion rows')
    cells = []
    for r in rows:
        tds = re.findall(r'<td>(.*?)</td>', r, flags=re.S)
        if len(tds) >= 2:
            cells.append(re.sub('<[^>]+>', '', tds[1]))
    joined = ' | '.join(cells)
    ck('Pereira' not in joined, 'mma: Pereira listed AS a champion')
    ck('Chimaev' not in joined, 'mma: Chimaev listed AS a champion')
    ck('Topuria' not in joined, 'mma: Topuria listed AS lightweight champion')
    ck('Pantoja' not in joined, 'mma: Pantoja listed AS flyweight champion')
    ck('vacant' not in joined.lower(), 'mma: a belt listed vacant')
    ck('Ulberg' in joined and 'Strickland' in joined and 'Volkanovski' in joined,
       'mma: the three regression-prone belts')
# interim/undisputed must not be conflated
i = mmp.find('Gane')
ck(i > 0, 'mma: Gane present')
if i > 0:
    ck('interim' in mmp[max(0, i - 900):i + 900].lower(),
       'mma: Gane not qualified as interim')
ck('undisputed' in mmp.lower(), 'mma: Aspinall undisputed restated')
# Dariush / Blaydes descriptor rules.
# NARROWED: the Dariush sweep fired on the page's own statement of the RULE (the
# Blaydes refusal cites "the one written after Beneil Dariush was miscalled a
# challenger"). Re-anchored: a Dariush window carrying champion/challenger must
# also carry the rule language or "contender". Tests the assertion, not the name.
for occ in [m.start() for m in re.finditer(r'Dariush', mmp)]:
    win = mmp[max(0, occ - 700):occ + 700].lower()
    if not re.search(r'champion|challenger', win):
        continue
    ck(('contender' in win or 'miscalled' in win or 'never' in win
        or 'omitted' in win or 'standing rule' in win),
       'mma: Dariush asserted as champion/challenger at %d' % occ)
# NARROWED: "FORMER title challenger" is a sourced descriptor for fighters who have
# in fact fought for a belt (Umar Nurmagomedov, Yan Xiaonan -- both taken from
# UFC.com event copy in a prior edition and recorded as such on the page). The rule
# this guard exists for is the UNQUALIFIED descriptor applied without sourcing.
for m_ in re.finditer(r'title challenger', mmp):
    occ = m_.start()
    prefix = mmp[max(0, occ - 12):occ].lower()
    if 'former' in prefix or 'ex-ufc ' in prefix or 'ex-' in prefix:
        continue
    win = mmp[max(0, occ - 1500):occ + 1500].lower()
    ck('refus' in win or 'omitted' in win or 'nothing fetched' in win
       or 'not described here' in win,
       'mma: unqualified, unsourced "title challenger" at %d' % occ)
# Salkilld regression guard
if 'Salkilld' in mmp:
    ck('Quillan' in mmp, 'mma: Salkilld first name')
    ck('Cody Salkilld' not in mmp, 'mma: wrong Salkilld first name')
    ck('Gamrot' in mmp, 'mma: Salkilld latest fight')
ck('Shamil Yakhyaev' not in mmp, 'mma: Yakhyaev misrendering')
if 'Yakhyaev' in mmp:
    ck('Abdul Rakhman Yakhyaev' in mmp, 'mma: Yakhyaev spelling')
# UFC Edmonton
ck('Rogers Place' in mmp, 'mma: Edmonton venue')
ck('October 17' in mmp, 'mma: Edmonton date')
ck('Joaquin Buckley' in mmp and 'Mike Malott' in mmp, 'mma: Edmonton headliners')
ck('Erin Blanchfield' in mmp and 'Jasmine Jasudavicius' in mmp, 'mma: Edmonton co-main')
ck('Chad Anheliger' in mmp and 'Steven Koslow' in mmp, 'mma: Edmonton corroborated bout')
ck('5 PM ET' in mmp and '8 PM ET' in mmp, 'mma: Edmonton start times')
# refused UFC 331 name-mangling must not have leaked.
# NARROWED (11th refusal-context false positive): each mangled name appears ONLY
# inside the 12:24 paragraph that quotes it as the reason for the refusal. A guard
# that forbids the string forbids the page from explaining itself. Re-anchored to
# require every occurrence to sit inside a refusal window.
for bad in ['Erik Shahbazyan', 'Jamall Emmers Brito', 'additional fighter']:
    for m_ in re.finditer(re.escape(bad), mmp):
        win = mmp[max(0, m_.start() - 1600):m_.start() + 1600].lower()
        ck('refus' in win or 'mangl' in win or 'not printed' in win
           or 'not earned' in win or 'omitted' in win,
           'mma: refused name %s ASSERTED at %d' % (bad, m_.start()))
# countdown bar targets the NEXT card, not the next numbered one
ck('ufccdn' in MM, 'mma: countdown element')
m = re.search(r"(2026-\d\d-\d\dT[\d:]+Z)", MM)
ck(bool(m), 'mma: countdown target datetime')
if m:
    ck(m.group(1).startswith('2026-09-05'),
       'mma: countdown targets %s, expected UFC Paris 2026-09-05' % m.group(1))
ck('Paris' in mmp, 'mma: next card named')
# odds must name a book / be attributed
for occ in [m.start() for m in re.finditer(r'&minus;550', mmp)]:
    win = mmp[max(0, occ - 1500):occ + 1500]
    ck('+400' in win, 'mma: Parnasse odds without the other side')
ck('subject to change' in MM.lower(), 'mma: cards-subject-to-change disclaimer')

# ============================================ 6. INDEX MIRRORING
idxp = unlinked(IDX)
for cls in ['c-cy', 'c-ws', 'c-mm']:
    ck('bigcard %s' % cls in IDX, 'index: card %s' % cls)
ck('Read the briefing' in IDX, 'index: read-through links')
ck(IDX.count('Read the briefing') == 3, 'index: three read-through links')
# each summary must agree with its page's own lead subject
ck('FulcrumSec' in idxp and 'FulcrumSec' in cyp, 'index/cy: subject agreement')
ck('closing values' in idxp.lower() and 'closing values' in wsp.lower(),
   'index/ws: subject agreement')
ck('Eighteenth' in idxp and 'eighteenth' in mmp.lower(),
   'index/mma: subject agreement')
ck('seventy-fifth' in idxp.lower(), 'index: champions streak mirrored')
# index must carry no numbers its pages refuse
ck('53,885.10' not in idxp or 'closing values' in idxp.lower(),
   'index: refused level without its refusal')
ck(IDX.count('class="srcs"') == 1, 'index: exactly one sources block')
ck('fetched 1:12 PM ET' in IDX, 'index: sources restamped')

# ============================================ 7. CHRONOLOGY / TAG HYGIENE
today = 'August 31'
for p, h in PAGES.items():
    hp = unlinked(h)
    # nothing "upcoming" that has already happened
    for past in ['August 29, 2026', 'August 25, 2026']:
        for occ in [m.start() for m in re.finditer(re.escape(past), hp)]:
            win = hp[max(0, occ - 300):occ + 300].lower()
            ck('upcoming' not in win, '%s: past date %s called upcoming' % (p, past))
    # bare clock stamps must carry a date or say "earlier edition"
    for m in re.finditer(r'Carried &middot; ([^<]{0,40})', hp):
        t = m.group(1)
        ok = ('Aug' in t or 'earlier edition' in t or 'August' in t
              or 'from the' in t)
        ck(ok, '%s: undated carried tag "%s"' % (p, t.strip()))
    # this run's tag spelled consistently
    ck('New &middot; 1:12 PM' in h or p == 'index.html',
       '%s: no new-content tag for this run' % p)

# ---------------------------------------------------------------- report
print('validate_1312: %d checks, %d failures' % (N[0], len(FAIL)))
for f in FAIL:
    print('  FAIL:', f)
sys.exit(1 if FAIL else 0)
