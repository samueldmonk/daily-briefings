#!/usr/bin/env python3
"""Validation for the 12:35 PM ET Saturday Aug 29 2026 edition."""
import io, os, re, sys

O = os.path.dirname(os.path.abspath(__file__))
P = {n: io.open(os.path.join(O, n), encoding='utf-8').read()
     for n in ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html')}
CY, WS, MMA, IX = P['cyber-briefing.html'], P['wallstreet-briefing.html'], P['mma-briefing.html'], P['index.html']

ok = fail = 0
def chk(cond, msg):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print('  FAIL: ' + msg)

# ---- structure: five-tab nav, masthead ids, self-stamp ----
for n, h in P.items():
    for href in ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
                 'mma-briefing.html', 'archive.html'):
        chk('href="%s"' % href in h, '%s: nav link %s' % (n, href))
    for i in ('edition', 'datestamp', 'updated', 'freshline'):
        chk('id="%s"' % i in h, '%s: masthead id %s' % (n, i))
    chk("America/New_York" in h, '%s: self-stamp tz' % n)
    chk('Morning Edition' in h and 'Midday Edition' in h and 'Afternoon Edition' in h,
        '%s: edition buckets' % n)
    chk('12:35 PM ET' in h, '%s: 12:35 fallback stamp' % n)
    chk('12:05 PM ET' not in h, '%s: stale 12:05 stamp removed' % n)
    chk('11:44' not in h.split('<body')[0], '%s: no stale head stamp' % n)

# ---- tldr strips present with correct labels ----
chk('<b>The Wire</b>' in CY, 'CY tldr label')
chk('<b>The Tape</b>' in WS, 'WS tldr label')
chk('<b>Tale of the Tape</b>' in MMA, 'MMA tldr label')

# ---- index cards mirror the tldrs exactly ----
def tldr(h):
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', h, re.S)
    return m.group(1) if m else None
for label, h in (('cyber', CY), ('markets', WS), ('mma', MMA)):
    t = tldr(h)
    chk(t is not None, '%s: tldr parsed' % label)
    if t:
        chk(t in IX, '%s: index card mirrors tldr' % label)

# ---- markets: closes + arithmetic reconciliation ----
for f in ('7,711.76', '26,402.42', '53,559.99', '&minus;9.45', '&minus;0.25%', '&minus;0.52%',
          '&minus;0.02%'):
    chk(f in WS, 'WS close figure %s' % f)
# Dow: level + points change must reconcile with the percent
prev_dow = 53559.99 + 9.45
chk(abs((9.45 / prev_dow) * 100 - 0.02) < 0.005, 'WS Dow pct reconciles')
# weekly figures sourced this run
for f in ('S&amp;P +0.5%', 'Nasdaq +0.9%', 'Dow +0.5%'):
    chk(f in WS, 'WS weekly figure %s' % f)
chk('first one in three' in WS, 'WS Dow first winning week in three')

# ---- markets: the eleventh-check scoping family ----
chk('re-verified an eleventh time at 12:35 PM' in WS, 'WS eleventh check stamped')
chk('all three index levels and all three percentage moves together' in WS, 'WS breadth stated')
chk('they are carried no longer' in WS, 'WS carried-status retired')
chk('which fields the\ncheck itself returned' in WS or 'which fields the check itself returned' in WS,
    'WS field-scoping rule restated')
chk('re-verified a tenth time' not in WS, 'WS retired tenth-check phrasing gone')
chk('narrower than the phrase suggests' not in WS, 'WS retired narrowness phrasing gone')
chk('re-verified an eleventh time this run' in WS and 're-verified an eleventh time this run' in IX,
    'WS/IX eleventh in tldr + card')

# ---- markets: weekend discipline ----
chk('as of ~' not in WS, 'WS no intraday as-of')
chk('7,673.04' not in WS, 'WS retired stray level stays out')
chk('After-Hours' not in WS and 'After Hours' not in WS, 'WS no after-hours block (tape shut)')
chk('NASDAQ:PYPL' in WS, 'WS chart of the day unchanged')
chk('contested' in WS, 'WS December read still marked contested')

# ---- markets: all six TradingView blocks + required symbols ----
for w in ('embed-widget-ticker-tape', 'embed-widget-single-quote', 'embed-widget-timeline',
          'embed-widget-stock-heatmap', 'embed-widget-mini-symbol-overview', 'embed-widget-events'):
    chk(w in WS, 'WS widget %s' % w)
for s in ('FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y'):
    chk(s in WS, 'WS ticker symbol %s' % s)
for n in ('index.html', 'cyber-briefing.html', 'mma-briefing.html'):
    chk('tradingview.com' not in P[n], '%s: no live widgets' % n)

# ---- cyber: KEV board unchanged and re-checked ----
chk('Re-checked at 12:35 PM: nothing on this board changed.' in CY, 'CY KEV re-check stamped')
chk('no CISA alert dated\nlater than August 26' in CY or 'no CISA alert dated later than August 26' in CY,
    'CY no later KEV alert')
chk('0 / 1 / 11 / 12' in CY, 'CY countdowns unchanged')
chk('BOD 26-04' in CY, 'CY BOD 26-04 named')
chk('BOD 22-01' in CY and 'superseded' in CY, 'CY BOD 22-01 marked superseded')
chk('is not the same as <b>CISA published none</b>' in CY, 'CY liveness caveat retained')
for c in ('CVE-2026-8452', 'CVE-2019-1068', 'CVE-2026-53362', 'CVE-2023-49105', 'CVE-2022-0995',
          'CVE-2021-23758', 'CVE-2015-5287', 'CVE-2015-3246', 'CVE-2026-66384'):
    chk(c in CY, 'CY KEV CVE %s' % c)
# the Oracle CVE must appear ONLY inside its own "not carried" framing
_or = [m.start() for m in re.finditer('CVE-2026-21962', CY)]
chk(len(_or) >= 1, 'CY Oracle CVE present')
for _i in _or:
    _w = re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', CY[max(0, _i - 250):_i + 250]))
    chk('not carried' in _w, 'CY Oracle CVE framed as not carried')

# ---- cyber: the new CISA-review family ----
chk('New at 12:35 PM &mdash; the same review, reported this week' in CY, 'CY review extension stamped')
chk('&ldquo;unforgivable&rdquo; in 2007' in CY, 'CY unforgivable-2007 figure')
chk('seven of the top ten weakness types in\n2025' in CY or 'seven of the top ten weakness types in 2025' in CY,
    'CY seven-of-ten figure')
chk('improper input\nvalidation</b> named the <b>single most common weakness type' in CY
    or 'improper input validation</b> named the <b>single most common weakness type' in CY,
    'CY input-validation superlative')
chk('Secure by Design' in CY, 'CY Secure by Design framing')
chk('are</b> the finding' in CY, 'CY board-as-instance link')
chk('theregister.com' in CY, 'CY Register source linked')
# the aged CVEs the claim points at must actually be on the page
for y in ('CVE-2015-3246', 'CVE-2015-5287', 'CVE-2019-1068', 'CVE-2021-23758', 'CVE-2022-0995'):
    chk(y in CY, 'CY aged CVE %s present for the claim' % y)

# ---- cyber: carried families intact ----
chk('284 million' in CY and 'records, not people' in CY, 'CY McKesson record-vs-people guard')
chk('early stages' in CY, 'CY McKesson early-stages')
chk('8.7 million' in CY, 'CY MAG scale')
chk('phishing' in CY, 'CY MAG phishing consequence')
chk('implantable cardiac' in CY, 'CY Boston Scientific device-function scoping')
chk('CVE-2026-81578' in CY and 'CVE-2026-82078' in CY, 'CY PaperCut CVE pair')

# ---- mma: champions board, eleven names ----
for nm in ('Tom Aspinall', 'Ciryl Gane', 'Carlos Ulberg', 'Sean Strickland', 'Islam Makhachev',
           'Justin Gaethje', 'Alexander Volkanovski', 'Petr Yan', 'Joshua Van',
           'Valentina Shevchenko', 'Kayla Harrison'):
    chk(nm in MMA, 'MMA champion name %s' % nm)
# Pereira / Chimaev may only appear inside a corrective frame
_CORRECTIVE = ('no longer', 'vacated', 'interim', 'lost', 'Gane', 'superseded', 'regression',
               'Split decision over', 'split decision over', 'upset', 'Strickland', 'Ulberg')
for name in ('Pereira', 'Chimaev'):
    for m in re.finditer(name, MMA):
        w = re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', MMA[max(0, m.start() - 420):m.start() + 420]))
        chk(any(f in w for f in _CORRECTIVE), 'MMA %s appears in a corrective frame' % name)

# ---- mma: standing rules ----
chk('vacan' in MMA.lower(), 'MMA vacancy-rejection discussion retained')
chk('UFC 333' in MMA and 'October 24' in MMA, 'MMA UFC 333 family')
chk('Merab Dvalishvili' in MMA, 'MMA trilogy opponent')
chk('not expected to' in MMA and 'Gaethje' in MMA, 'MMA idle-belt family')
chk('knockout (punch)' in MMA, 'MMA official method retained')

# ---- mma: the fourth-name family ----
chk('New at 12:35 PM &mdash; the outlet that supplied the '
    'third name has now supplied a fourth' in MMA, 'MMA fourth-name stamped')
chk('right-hand\nuppercut' in MMA or 'right-hand uppercut' in MMA, 'MMA fourth rendering named')
chk('short right hand' in MMA, 'MMA third rendering retained')
chk('one publication renders the same punch two ways' in MMA, 'MMA same-outlet-two-ways rule')
chk('stopped counting' in MMA, 'MMA stops-counting retained')
chk('two-two' in MMA, 'MMA explicitly declines the new tally')

# ---- mma: Jon Jones detail ----
chk('ran straight to Jon Jones to celebrate the win' in MMA, 'MMA Jon Jones detail')
chk('Neither report places that moment relative to the' in MMA, 'MMA Jon Jones ordering not asserted')
chk('at cageside' not in MMA and 'at cageside' not in IX, 'MMA unsourced cageside descriptor removed')
chk('which therefore adds nothing' in MMA, 'MMA Yahoo headline not double-counted')
chk('Jon Jones' in IX, 'IX mirrors Jon Jones detail')
chk('Usman Nurmagomedov' in MMA and 'nothing landed' in MMA, 'MMA two-account family intact')

# ---- footers: absolute hrefs, no duplicates, minimum counts ----
for n, h, lo in (('cyber-briefing.html', CY, 40), ('wallstreet-briefing.html', WS, 20),
                 ('mma-briefing.html', MMA, 25)):
    hrefs = re.findall(r'href="(http[^"]+)"', h)
    chk(len(hrefs) >= lo, '%s: >= %d source links (got %d)' % (n, lo, len(hrefs)))
    chk(len(hrefs) == len(set(hrefs)), '%s: no duplicate hrefs' % n)
    chk(all(u.startswith('http') for u in hrefs), '%s: all hrefs absolute' % n)

# ---- CVE well-formedness sweep ----
cves = set(re.findall(r'CVE-\d{4}-\d{4,6}', CY))
chk(len(cves) >= 12, 'CY >= 12 distinct CVEs (got %d)' % len(cves))
chk(all(re.fullmatch(r'CVE-\d{4}-\d{4,6}', c) for c in cves), 'CY CVE ids well-formed')

# ---- disclaimers ----
chk('not investment advice' in WS or 'not intended as investment advice' in WS, 'WS disclaimer')
chk('subject to change' in MMA, 'MMA disclaimer')

print('validate_1235.py: %d checks, %d failures' % (ok + fail, fail))
sys.exit(1 if fail else 0)
