#!/usr/bin/env python3
"""Daily Briefings validator — 2026-08-30 2:11 PM edition.
Assertion-based: checks the CLAIM, not the vocabulary. A guard that fires on
correct prose is a broken guard."""
import re, sys, io, os

D = sys.argv[1]
FAILS, N = [], 0
# The edition stamp is DERIVED from the pages, not hardcoded, so the guard checks that all
# four agree rather than that they match a number typed into the validator.
_seed = io.open(os.path.join(D, 'index.html'), encoding='utf-8').read()
_m = re.search(r'Data as of ([0-9]{1,2}:[0-9]{2} (?:AM|PM)) ET', _seed)
if not _m:
    print('validate: cannot derive edition stamp from index.html'); sys.exit(1)
STAMP = _m.group(1)

def load(n): return io.open(os.path.join(D, n), encoding='utf-8').read()
CY, WS, MM, IX = (load(f) for f in
    ('cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html', 'index.html'))
PAGES = {'cyber': CY, 'wallstreet': WS, 'mma': MM, 'index': IX}
BRIEFS = {'cyber': CY, 'wallstreet': WS, 'mma': MM}

def ck(cond, msg):
    global N
    N += 1
    if not cond: FAILS.append(msg)

def has(page, name, s):   ck(s in PAGES[page], f'{name}: missing in {page}: {s[:70]!r}')
def hasnt(page, name, s): ck(s not in PAGES[page], f'{name}: FORBIDDEN present in {page}: {s[:70]!r}')

# ── 1. structure: five-tab nav, one active tab, masthead ids, self-stamp ──
TABS = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
        'mma-briefing.html', 'archive.html']
for p, h in PAGES.items():
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', h, re.S)
    ck(nav is not None, f'nav: missing on {p}')
    if nav:
        for t in TABS:
            ck(f'href="{t}"' in nav.group(1), f'nav: {p} missing tab {t}')
        ck(nav.group(1).count('class="on"') == 1,
           f'nav: {p} must have exactly one active tab, found {nav.group(1).count(chr(34)+"on"+chr(34))}')
    for i in ('edition', 'datestamp', 'updated'):
        ck(f'id="{i}"' in h, f'masthead: {p} missing id={i}')
    ck("Intl.DateTimeFormat" in h and "America/New_York" in h, f'self-stamp: {p} missing')

# ── 2. clock: this edition's stamp everywhere, stale stamps forbidden ──
STALE = ['1:09 PM', '1:08 PM', '12:58 PM', '12:55 PM', '11:05 AM', '9:42 PM', '8:31 PM']
for p, h in PAGES.items():
    ck(f'Data as of {STAMP} ET' in h, f'freshline: {p} not stamped {STAMP}')
    mast = h[:h.find('<nav class="tabs">') if '<nav class="tabs">' in h else 4000]
    for s in STALE:
        ck(s not in mast, f'masthead region: {p} carries stale stamp {s}')
    ck('Saturday, August 29' not in mast, f'masthead region: {p} carries stale date')
# prose may not run ahead of the clock
for p, h in PAGES.items():
    ck('2:12 PM' not in h, f'prose-ahead-of-clock: {p} still carries drafted 2:12 PM')

# ── 3. Wall Street: closes, weekly, rates, counters, calendar, seasonality ──
for s in ['7,711.76', '26,402.42', '53,559.99', '&minus;9.45', '0.25%', '0.52%']:
    has('wallstreet', 'close figure', s)
# Dow points/percent reconciliation
ck(abs((9.45 / (53559.99 + 9.45)) * 100 - 0.02) < 0.005, 'Dow points/percent do not reconcile')
for s in ['+0.5%', '+0.9%', 'first winning week in three']:
    has('wallstreet', 'weekly', s)
for s in ['4.73%', '4.34%', '5.20%']:
    has('wallstreet', 'rates', s)
# retired 10-year figure: every occurrence must sit in a rejection frame
for m in re.finditer(r'4\.67', WS):
    ctx = WS[max(0, m.start() - 400):m.start() + 400].lower()
    ck(any(w in ctx for w in ('retire', 'reject', 'does not displace', 'not adopted', 'refus')),
       'retired 4.67 appears outside a rejection frame')
hasnt('wallstreet', 'retired level', '7,673.04')
hasnt('wallstreet', 'weekend intraday', 'as of ~')
hasnt('wallstreet', 'weekend after-hours', 'After-Hours Movers')
has('wallstreet', 'counter', 'twentieth verification')
hasnt('wallstreet', 'stale counter', 'nineteenth verification')
has('wallstreet', '10yr count', 'back for a sixth time')
hasnt('wallstreet', 'stale 10yr count', 'back for a fifth time')
has('wallstreet', 'Sept declination', 'seventh consecutive run')
for s in ['48%', 'near 50%', '57%', '65%', 'very unlikely']:
    has('wallstreet', 'Sept read', s)
# payrolls: Sept 4 asserted, "September 5" only ever in a rejection frame
has('wallstreet', 'payrolls date', 'September 4')
has('wallstreet', 'payrolls time', '8:30')
for m in re.finditer(r'September 5', WS):
    ctx = WS[max(0, m.start() - 500):m.start() + 500].lower()
    ck(any(w in ctx for w in ('reject', 'saturday', 'refus', 'failed')),
       'WS "September 5" appears outside a rejection frame')
# new calendar family
for s in ['New York Fed', 'Employment Situation on Friday, September 4',
          'ISM Manufacturing and JOLTS', 'ADP National Employment Report', 'ISM Services']:
    has('wallstreet', 'calendar', s)
# new seasonality family — must be framed as history, not forecast
for s in ['&minus;0.7% in September', '46%', '50 years']:
    has('wallstreet', 'seasonality', s)
i = WS.find('0.7% on average during September')
ck(i != -1, 'seasonality: body figure missing')
if i != -1:
    ctx = WS[max(0, i - 900):i + 900].lower()
    ck('historical average' in ctx or 'not a forecast' in ctx,
       'seasonality: figure not framed as history rather than forecast')
has('wallstreet', 'lead time-of-day', 'Sunday, early afternoon')
for s in ['just past one o&rsquo;clock', 'Sunday midday', 'Sunday morning', 'Saturday evening']:
    hasnt('wallstreet', 'stale lead time', s)

# ── 4. live widgets: six TradingView blocks on WS only ──
W = ['embed-widget-ticker-tape', 'embed-widget-single-quote', 'embed-widget-timeline',
     'embed-widget-stock-heatmap', 'embed-widget-mini-symbol-overview', 'embed-widget-events']
for w in W: has('wallstreet', 'widget', w)
for s in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y', 'NASDAQ:PYPL']:
    has('wallstreet', 'widget symbol', s)
for p in ('cyber', 'mma', 'index'):
    for w in W: hasnt(p, 'no-widgets', w)

# ── 5. Cyber: KEV board, countdowns, CVE hygiene, Patch Tuesday spread ──
has('cyber', 'KEV check', 'eleventh check')
hasnt('cyber', 'stale KEV check', 'a <b>tenth check of the KEV catalogue at 1:08 PM</b>')
for s in ['CVE-2026-8452', 'CVE-2019-1068', 'CVE-2026-53362', 'CVE-2023-49105',
          'CVE-2026-66384', 'CVE-2022-0995', 'CVE-2021-23758', 'CVE-2015-5287', 'CVE-2015-3246']:
    has('cyber', 'KEV id', s)
for s in ['OVERDUE', '0 days left', '10 days left', '11 days left']:
    has('cyber', 'countdown', s)
for s in ['1 day left', '12 days left']:
    hasnt('cyber', 'stale countdown', s)
# gap CVEs must never sit in a countdown region
for cve in ['CVE-2026-8037', 'CVE-2026-60004']:
    for m in re.finditer(re.escape(cve), CY):
        ctx = CY[max(0, m.start() - 500):m.start() + 500]
        ck('days left' not in ctx and 'OVERDUE' not in ctx,
           f'gap CVE {cve} appears in a countdown region')
# the newly-reported 68820 deadline must be framed as unsourced-to-CISA, no countdown row
i = CY.find('due date of <b>August 25</b>')
ck(i != -1, 'CY: 68820 August 25 deadline missing')
if i != -1:
    ctx = CY[max(0, i - 800):i + 800]
    ck('not given a countdown row' in ctx, '68820 deadline: not excluded from countdown rows')
    ck('news write-up' in ctx or 'rather than from a CISA alert' in ctx,
       '68820 deadline: not attributed as non-CISA')
# CVE well-formedness + liveness
ids = set(re.findall(r'CVE-\d{4}-\d{4,6}', CY))
ck(len(ids) >= 20, f'CVE liveness: only {len(ids)} distinct ids')
for c in ids:
    ck(re.fullmatch(r'CVE-(19|20)\d{2}-\d{4,6}', c) is not None, f'malformed CVE id {c}')
# Patch Tuesday spread
for s in ['421', '398', '751', 'CVE-2026-68820', 'afd.sys']:
    has('cyber', 'patch tuesday', s)
# assertion, not proximity: the body must (1) print the competing counts, (2) keep 421 as
# this page's figure, (3) state that the exploited-zero-day finding is not in dispute.
ck('<b>398 CVEs</b>' in CY, 'patch tuesday: competing 398 count not printed in the body')
ck('421 stays' in CY and 'one count among three' in CY,
   'patch tuesday: 421 not preserved as this page\'s figure alongside the spread')
ck('exactly one flaw in the release was being exploited' in CY,
   'patch tuesday: single-exploited-zero-day agreement not stated')
ck('Nothing fetched reconciles the three' in CY,
   'patch tuesday: the spread is presented as reconciled')
# Berlin volume: variant recorded, figure not swapped
has('cyber', 'berlin volume', '5.79')
i = CY.find('5.8TB')
ck(i != -1, 'berlin: 5.8TB variant not recorded')
if i != -1:
    ctx = CY[max(0, i - 600):i + 400]
    ck('not swapped' in ctx or 'rounding' in ctx, 'berlin: 5.8TB not framed as a rounding variant')
# refusals: every refused item must sit in a refusal frame
for item in ['Nevada', 'Salesloft', 'Brightspeed']:
    found = False
    for m in re.finditer(item, CY):
        ctx = CY[max(0, m.start() - 700):m.start() + 700].lower()
        if any(w in ctx for w in ('refus', 'not published', 'rejected')):
            found = True
        else:
            FAILS.append(f'{item} appears outside a refusal frame'); N += 1
    ck(found, f'{item}: no refusal frame found')
has('cyber', 'Nevada count', 'refused for a fourth consecutive run')
has('cyber', 'Nevada run count', 'on any of the four runs')
hasnt('cyber', 'stale Nevada count', 'refused for a third consecutive run')
hasnt('cyber', 'stale Nevada runs', 'on any of the three runs')
# attacker attribution proximity
for fig in ['5.79', '284 million', '$55,236,150']:
    for m in re.finditer(re.escape(fig), CY):
        ctx = CY[max(0, m.start() - 700):m.start() + 700].lower()
        ck(any(w in ctx for w in ('claim', 'alleg', 'says', 'reported', 'attribut', 'group')),
           f'figure {fig} printed without an attribution nearby')

# ── 6. MMA: champions board, counters, odds, Shanghai, Paris ──
CHAMPS = ['Tom Aspinall', 'Carlos Ulberg', 'Sean Strickland', 'Islam Makhachev',
          'Justin Gaethje', 'Alexander Volkanovski', 'Petr Yan', 'Joshua Van',
          'Valentina Shevchenko', 'Kayla Harrison', 'Mackenzie Dern']
for c in CHAMPS: has('mma', 'champion', c)
# forbidden champion assertions (the three this project has historically got wrong)
for bad in ['Pereira</td>', 'Chimaev</td>', 'Topuria</td>']:
    hasnt('mma', 'wrong champion cell', bad)
# A champion cell may never NAME a vacancy as the current holder. "won/for the vacant title"
# is correct history and must pass — the guard checks the assertion, not the word.
for m in re.finditer(r'<td[^>]*>([^<]*)</td>', MM):
    cell = m.group(1).strip()
    low = cell.lower()
    if 'vacant' not in low:
        continue
    ck(low not in ('vacant', 'vacant title', '&mdash; vacant &mdash;'),
       f'champions board cell names a vacancy as the holder: {cell[:50]!r}')
    ck(re.search(r'(for|won|win|winning) the vacant', low) is not None,
       f'champions board cell uses "vacant" outside a won-the-vacant-title frame: {cell[:60]!r}')
for m in re.finditer(r'featherweight[^.]{0,140}?is vacant', MM, re.I):
    ctx = MM[max(0, m.start() - 400):m.end() + 400].lower()
    ck(any(w in ctx for w in ('not vacant', 'reject', 'wrong', 'refus', 'was published')),
       'featherweight asserted vacant without a rejection frame')
# Dariush descriptor
for m in re.finditer(r'Dariush', MM):
    ctx = MM[max(0, m.start() - 300):m.start() + 300].lower()
    ck('champion' not in ctx or 'contender' in ctx or 'never' in ctx,
       'Dariush described with a title descriptor')
has('mma', 'board counter', 'sixty-first unchanged edition')
has('mma', 'board counter body', 'sixty-first consecutive edition')
has('mma', 'ESPN counter', 'fourth consecutive clean run')
for s in ['sixtieth unchanged edition', 'sixtieth consecutive edition',
          'third consecutive clean run against ESPN']:
    hasnt('mma', 'stale board counter', s)
# Paris family
for s in ['Accor Arena', '13 fights', 'Hooker vs. Parnasse', 'Salahdine Parnasse',
          'Dan Hooker', '12:00 PM ET', '3:00 PM ET', 'KSW featherweight']:
    has('mma', 'paris', s)
for s in ['&minus;400', '&minus;428', '&minus;500', '+375', '+300', '+292']:
    has('mma', 'paris odds', s)
has('mma', 'paris odds declination', 'No line is adopted')
has('mma', 'paris third return', 'third independent return')
for s in ['Far&egrave;s Ziam &minus;150 / Axel Sola +125',
          'Michael Page &minus;200 / Nursulton Ruziboev +165']:
    has('mma', 'undercard odds', s)
i = MM.find('&minus;150 / Axel Sola')
if i != -1:
    ctx = MM[max(0, i - 400):i + 700]
    ck('one book' in ctx or 'not as a consensus' in ctx,
       'undercard odds: not framed as a single book')
# Shanghai family
for s in ['Song Yadong', 'Umar Nurmagomedov', '1:48', 'first finish loss',
          'two-fight win streak', '6-to-1', '&minus;625', 'Everything is fine with me']:
    has('mma', 'shanghai', s)
i = MM.find('6-to-1')
if i != -1:
    ctx = MM[max(0, i - 700):i + 900]
    ck('printed rather than adopted' in ctx or 'not adopted' in ctx,
       '6-to-1 characterisation adopted rather than printed')
for s in ['$400,000', 'Liu Ce', 'Bilal Hasan', 'Hector Santiago', 'Francesco Nuzzi',
          'Rei Tsuruya', 'Kai Asakura', 'Denise Gomes']:
    has('mma', 'bonuses', s)
# UFC 331
for s in ['Crypto.com Arena', 'Alexandre Pantoja', 'Arman Tsarukyan', 'Mauricio Ruffy',
          'title shot against lightweight']:
    has('mma', 'ufc331', s)
hasnt('mma', 'stale 331 comain', 'over five rounds, with title implications.')
# countdown target
ck('ufccdn' in MM, 'MMA: countdown element missing')

# ── 7. index mirrors each briefing tldr exactly ──
def tldr(h):
    m = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', h, re.S)
    return m.group(1) if m else None
for cls, h, name in (('c-cy', CY, 'cyber'), ('c-ws', WS, 'wallstreet'), ('c-mm', MM, 'mma')):
    t = tldr(h)
    ck(t is not None, f'tldr missing on {name}')
    i = IX.find(f'<div class="bigcard {cls}">')
    ck(i != -1, f'index card missing for {name}')
    if t and i != -1:
        ps, pe = IX.find('<p>', i), IX.find('</p>', IX.find('<p>', i))
        ck(IX[ps + 3:pe] == t, f'index card for {name} does not mirror its tldr')

# ── 8. footers: >=6 absolute links, no duplicate hrefs, disclaimer present ──
for name, h in BRIEFS.items():
    fi = h.rfind('Sources')
    ck(fi != -1, f'{name}: no Sources footer')
    if fi != -1:
        hrefs = re.findall(r'href="(https?://[^"]+)"', h[fi:])
        ck(len(hrefs) >= 6, f'{name}: footer has only {len(hrefs)} source links')
        ck(len(hrefs) == len(set(hrefs)), f'{name}: duplicate href in footer')
        for u in hrefs:
            ck(u.startswith('http'), f'{name}: non-absolute footer href {u}')
    ck(any(s in h.lower() for s in ('information only', 'not investment advice',
                                    'subject to change', 'disclaimer')),
       f'{name}: no disclaimer')
ck('not investment advice' in WS.lower(), 'WS: investment-advice disclaimer missing')
ck('subject to change' in MM.lower(), 'MMA: cards-subject-to-change disclaimer missing')

# ── report ──
print(f'validate_1412: {N} checks, {len(FAILS)} failures')
for f in FAILS: print('  FAIL:', f)
sys.exit(1 if FAILS else 0)
